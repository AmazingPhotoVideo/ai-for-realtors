#!/usr/bin/env python3
"""Validate Realtor design-pack structure, references, and sample population."""
from __future__ import annotations
import json, re, subprocess, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKS = ROOT / "design-packs"
FAMILIES = ("editorial-luxury", "bold-modern", "warm-neighbourhood")
FORMATS = ("letter-flyer", "square-social", "portrait-social", "story-social", "landscape-brochure")
TOKEN = re.compile(r"{{\s*[^}]+\s*}}")
REFERENCE = re.compile(r"(?:src|href)=[\"']([^\"']+)[\"']")
errors: list[str] = []
checks = 0

def check(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        errors.append(message)

for data_file, root_key in (("sample-listing.json", "listing"), ("sample-branding.json", "branding")):
    path = PACKS / "data" / data_file
    check(path.is_file(), f"missing {path.relative_to(ROOT)}")
    if path.is_file():
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            check(root_key in data, f"{data_file} missing top-level {root_key}")
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSON {data_file}: {exc}")

for family in FAMILIES:
    for fmt in FORMATS:
        path = PACKS / family / f"{fmt}.html"
        check(path.is_file(), f"missing {path.relative_to(ROOT)}")
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        check(text.lstrip().lower().startswith("<!doctype html>"), f"{family}/{path.name}: missing HTML5 doctype")
        check("@page" in text and "overflow:hidden" in text.replace(" ", ""), f"{family}/{path.name}: missing print/overflow rules")
        check("data-template-family" in text and "data-format" in text, f"{family}/{path.name}: missing template metadata")
        check("Amazing Photo Video" in text and "https://amazingphotovideo.com" in text, f"{family}/{path.name}: missing APV attribution")
        check(bool(TOKEN.search(text)), f"{family}/{path.name}: not data-driven")

with tempfile.TemporaryDirectory(prefix="design-pack-validation-") as tmp:
    process = subprocess.run(
        [sys.executable, str(ROOT / "scripts/render_design_packs.py"), "--output", tmp],
        cwd=ROOT, text=True, capture_output=True,
    )
    check(process.returncode == 0, "sample population failed: " + (process.stderr or process.stdout).strip())
    if process.returncode == 0:
        populated = list(Path(tmp).glob("*/*.html"))
        check(len(populated) == 15, f"expected 15 populated HTML files, found {len(populated)}")
        for path in populated:
            text = path.read_text(encoding="utf-8")
            check(not TOKEN.search(text), f"{path.name}: unresolved placeholder after population")
            visible = re.sub(r"<[^>]+>", "", text)
            check(
                "Designed with resources from Amazing Photo Video —" in visible
                and "https://amazingphotovideo.com" in text,
                f"{path.name}: populated attribution missing",
            )
            for reference in REFERENCE.findall(text):
                if reference.startswith(("http://", "https://", "mailto:", "data:", "#")):
                    continue
                target = (path.parent / reference).resolve()
                check(target.exists(), f"{path.relative_to(tmp)}: broken local reference {reference}")

if errors:
    print(f"FAIL: {len(errors)} error(s) across {checks} checks")
    for error in errors:
        print(" - " + error)
    raise SystemExit(1)
print(f"PASS: {checks} checks; 3 families × 5 formats; sample population generated 15 clean HTML files.")
