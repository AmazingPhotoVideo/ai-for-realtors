#!/usr/bin/env python3
"""Contract tests for dependency-free community browser tools."""

from __future__ import annotations

import re
import shutil
import subprocess
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = {
    "AI-safe redactor": ROOT / "tools" / "ai-safe-redactor" / "index.html",
    "Open House QR generator": ROOT / "tools" / "open-house-qr" / "index.html",
}


class DocumentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.labels_for: set[str] = set()
        self.form_control_ids: set[str] = set()
        self.external_scripts: list[str] = []
        self.form_actions: list[str] = []
        self.checked_checkboxes = 0
        self.apv_links: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if values.get("id"):
            self.ids.append(values["id"])
        if tag == "label" and values.get("for"):
            self.labels_for.add(values["for"])
        if tag in {"input", "select", "textarea"} and values.get("id"):
            self.form_control_ids.add(values["id"])
        if tag == "script" and values.get("src"):
            self.external_scripts.append(values["src"])
        if tag == "form" and values.get("action"):
            self.form_actions.append(values["action"])
        if tag == "input" and values.get("type", "").lower() == "checkbox" and "checked" in values:
            self.checked_checkboxes += 1
        if tag == "a" and values.get("href", "").rstrip("/") == "https://amazingphotovideo.com":
            self.apv_links.append(values)


class CommunityToolContractTests(unittest.TestCase):
    maxDiff = None

    def load_tool(self, label: str) -> tuple[str, DocumentParser]:
        path = TOOLS[label]
        self.assertTrue(path.is_file(), f"missing {path.relative_to(ROOT)}")
        text = path.read_text(encoding="utf-8")
        parser = DocumentParser()
        parser.feed(text)
        self.assertEqual(len(parser.ids), len(set(parser.ids)), f"duplicate HTML ids in {path}")
        self.assertEqual(
            parser.form_control_ids - parser.labels_for,
            set(),
            f"unlabelled controls in {path}",
        )
        self.assertFalse(parser.external_scripts, f"external scripts in {path}: {parser.external_scripts}")
        self.assertFalse(parser.form_actions, f"forms must not submit from {path}: {parser.form_actions}")
        self.assertTrue(parser.apv_links, f"missing APV backlink in {path}")
        for attrs in parser.apv_links:
            rel = attrs.get("rel", "").lower().split()
            self.assertNotIn("nofollow", rel)
            self.assertNotIn("sponsored", rel)
        return text, parser

    def assert_browser_local(self, text: str) -> None:
        for forbidden in (
            r"\bfetch\s*\(",
            r"\bXMLHttpRequest\b",
            r"\bWebSocket\b",
            r"\bsendBeacon\b",
            r"\blocalStorage\b",
            r"\bsessionStorage\b",
            r"\bindexedDB\b",
        ):
            self.assertIsNone(re.search(forbidden, text), f"browser-local contract violated by {forbidden}")

    def assert_inline_javascript_parses(self, text: str) -> None:
        if not shutil.which("node"):
            self.skipTest("node is unavailable")
        scripts = re.findall(r"<script(?:\s[^>]*)?>(.*?)</script>", text, flags=re.IGNORECASE | re.DOTALL)
        self.assertTrue(scripts, "expected inline JavaScript")
        with tempfile.NamedTemporaryFile("w", suffix=".js", encoding="utf-8") as handle:
            handle.write("\n".join(scripts))
            handle.flush()
            result = subprocess.run(
                ["node", "--check", handle.name],
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_ai_safe_redactor_contract(self) -> None:
        text, _ = self.load_tool("AI-safe redactor")
        self.assert_browser_local(text)
        self.assertRegex(text, r'id="sourceText"[^>]*spellcheck="false"')
        for phrase in ("Redact", "Load fictional sample", "Copy", "Download", "Clear"):
            self.assertIn(phrase, text)
        self.assertRegex(text.lower(), r"cannot.{0,100}guarantee anonymization|does not guarantee")
        self.assertRegex(text.lower(), r"human review|review.*before")
        self.assertRegex(text.lower(), r"nothing leaves this page|no data.*(?:leave|sent|upload)|stays in your browser")
        self.assert_inline_javascript_parses(text)

    def test_ai_safe_redactor_behavior(self) -> None:
        if not shutil.which("node"):
            self.skipTest("node is unavailable")
        harness = ROOT / "tests" / "redactor_behavior.js"
        result = subprocess.run(
            ["node", str(harness)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("redactor behavior: PASS", result.stdout)

    def test_open_house_qr_contract(self) -> None:
        text, parser = self.load_tool("Open House QR generator")
        self.assert_browser_local(text)
        self.assertRegex(text, r'id="builderForm"[^>]*spellcheck="false"')
        self.assertEqual(parser.checked_checkboxes, 0, "consent choices must never be prechecked")
        for phrase in ("Load fictional sample", "Generate", "Print", "privacy", "retention"):
            self.assertIn(phrase.lower(), text.lower())
        self.assertRegex(text.lower(), r"does not collect|does not submit|does not send")
        self.assertRegex(text.lower(), r"brokerage-approved")
        self.assertRegex(text.lower(), r"represented[- ]buyer|working with an agent")
        self.assertRegex(text.lower(), r"optional marketing|marketing consent")
        self.assertIn("Permission is hereby granted, free of charge", text)
        self.assertIn('THE SOFTWARE IS PROVIDED "AS IS"', text)
        self.assert_inline_javascript_parses(text)


if __name__ == "__main__":
    unittest.main()
