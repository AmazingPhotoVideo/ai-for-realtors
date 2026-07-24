#!/usr/bin/env python3
"""Repository-wide structural checks for AI for Realtors assets."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", "node_modules", ".next", "dist", "out", "output", "outputs"}
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
SECRET_PATTERNS = {
    "GitHub token": re.compile(r"\b(?:github_pat_[A-Za-z0-9_]{20,}|gh[oprsu]_[A-Za-z0-9]{30,})\b"),
    "generic private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}
FORBIDDEN_BRAND_REFERENCES = ("stewardengine.com", "harborseo.ai", "IncomeStreamSurfer")


def files_with_suffix(*suffixes: str):
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.suffix.lower() in suffixes:
            yield path


def check_markdown_links(errors: list[str]) -> None:
    for path in files_with_suffix(".md"):
        text = path.read_text(encoding="utf-8", errors="replace")
        for raw in MARKDOWN_LINK.findall(text):
            target = raw.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:", "tel:")):
                continue
            clean = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if clean and not (path.parent / clean).resolve().exists():
                errors.append(f"broken local link: {path.relative_to(ROOT)} -> {target}")


def check_secrets_and_reference_branding(errors: list[str]) -> None:
    text_suffixes = (".md", ".html", ".css", ".js", ".mjs", ".ts", ".tsx", ".json", ".py", ".yml", ".yaml")
    for path in files_with_suffix(*text_suffixes):
        text = path.read_text(encoding="utf-8", errors="replace")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"possible {label}: {path.relative_to(ROOT)}")
        if path.resolve() == Path(__file__).resolve():
            continue
        lowered = text.lower()
        for forbidden in FORBIDDEN_BRAND_REFERENCES:
            if forbidden.lower() in lowered:
                errors.append(f"reference-project branding leaked into {path.relative_to(ROOT)}: {forbidden}")


def check_creative_platform(errors: list[str]) -> None:
    required = (
        "docs/design-asset-licensing.md",
        "docs/realtor-creative-platform.md",
        "design-packs",
        "property-pages",
        "agent-sites",
        "skills/realtor-design-pack-builder/SKILL.md",
        "skills/single-property-page-builder/SKILL.md",
        "skills/realtor-site-crm-builder/SKILL.md",
    )
    for relative in required:
        if not (ROOT / relative).exists():
            errors.append(f"missing creative-platform path: {relative}")

    for directory in ("design-packs", "property-pages", "agent-sites"):
        root = ROOT / directory
        if not root.exists():
            continue
        patterns = ("*.html", "*.tsx") if directory == "agent-sites" else ("*.html",)
        template_files = [
            path
            for pattern in patterns
            for path in root.rglob(pattern)
            if not any(part in SKIP_PARTS for part in path.parts)
        ]
        if not template_files:
            errors.append(f"no public templates found under {directory}")
            continue
        combined = "\n".join(path.read_text(encoding="utf-8", errors="replace") for path in template_files)
        if "amazingphotovideo.com" not in combined:
            errors.append(f"no APV backlink found in public templates under {directory}")
        if re.search(r'rel\s*=\s*["\'][^"\']*\b(?:nofollow|sponsored)\b', combined, re.IGNORECASE):
            errors.append(f"disallowed nofollow/sponsored relationship found in public templates under {directory}")


def main() -> int:
    errors: list[str] = []
    check_markdown_links(errors)
    check_secrets_and_reference_branding(errors)
    check_creative_platform(errors)
    if errors:
        print(f"FAIL: {len(errors)} repository validation issue(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: repository links, secrets, reference branding, required paths, and APV HTML attribution validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
