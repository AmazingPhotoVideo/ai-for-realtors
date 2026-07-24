#!/usr/bin/env python3
"""Populate Realtor design-pack templates and optionally export with Playwright."""
from __future__ import annotations
import argparse, html, json, re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKS = ROOT / "design-packs"
FAMILIES = ("editorial-luxury", "bold-modern", "warm-neighbourhood")
FORMATS = ("letter-flyer", "square-social", "portrait-social", "story-social", "landscape-brochure")
DIMENSIONS = {
    "letter-flyer": (816, 1056, "8.5in", "11in"),
    "square-social": (1080, 1080, "1080px", "1080px"),
    "portrait-social": (1080, 1350, "1080px", "1350px"),
    "story-social": (1080, 1920, "1080px", "1920px"),
    "landscape-brochure": (1056, 816, "11in", "8.5in"),
}
TOKEN = re.compile(r"{{\s*([a-zA-Z0-9_.-]+)\s*}}")
REQUIRED = (
    "listing.address.street", "listing.address.city_region", "listing.price", "listing.status_label",
    "listing.headline", "listing.description", "listing.beds", "listing.baths", "listing.interior",
    "listing.images.hero", "listing.cta", "listing.website", "listing.disclaimer",
    "branding.agent_name", "branding.phone", "branding.email",
    "branding.brokerage", "branding.logo", "branding.headshot", "branding.primary_color",
    "branding.accent_color", "branding.font_display", "branding.font_body",
)
LIMITS = {
    "listing.headline": 62, "listing.description": 260, "listing.address.street": 58,
    "branding.agent_name": 42, "branding.brokerage": 72,
}

def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"Cannot read JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise SystemExit(f"Expected a JSON object in {path}")
    return value

def lookup(data: dict, key: str):
    value = data
    for part in key.split("."):
        if not isinstance(value, dict) or part not in value:
            raise KeyError(key)
        value = value[part]
    return value

def validate(data: dict) -> None:
    missing = []
    for key in REQUIRED:
        try:
            value = lookup(data, key)
        except KeyError:
            missing.append(key)
            continue
        if value is None or str(value).strip() == "":
            missing.append(key)
    if missing:
        raise SystemExit("Missing required fields:\n  - " + "\n  - ".join(missing))
    for key, limit in LIMITS.items():
        if len(str(lookup(data, key))) > limit:
            raise SystemExit(f"{key} exceeds {limit} characters; shorten it to protect layout readability.")
    for key in ("branding.primary_color", "branding.accent_color"):
        if not re.fullmatch(r"#[0-9a-fA-F]{6}", str(lookup(data, key))):
            raise SystemExit(f"{key} must be a six-digit hex colour (for example #17332d).")

def populate(source: str, data: dict) -> str:
    missing = set()
    def replace(match):
        key = match.group(1)
        try:
            value = str(lookup(data, key))
        except KeyError:
            missing.add(key)
            return match.group(0)
        if key.startswith("branding.font_") or key.endswith("_color"):
            return value
        return html.escape(value, quote=True)
    result = TOKEN.sub(replace, source)
    if missing:
        raise SystemExit("Template references missing fields: " + ", ".join(sorted(missing)))
    return result

def parse_csv(value: str, allowed: tuple[str, ...], label: str) -> list[str]:
    if value == "all":
        return list(allowed)
    selected = [part.strip() for part in value.split(",") if part.strip()]
    unknown = sorted(set(selected) - set(allowed))
    if unknown:
        raise SystemExit(f"Unknown {label}: {', '.join(unknown)}. Choose from {', '.join(allowed)} or all.")
    return selected

def export_files(paths: list[tuple[Path, str]], kind: str) -> int:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise SystemExit(
            "Export requested but Playwright is unavailable. Install with:\n"
            "  python3 -m venv .venv\n  .venv/bin/pip install playwright\n"
            "  .venv/bin/playwright install chromium\nThen rerun with .venv/bin/python scripts/render_design_packs.py ..."
        ) from exc
    count = 0
    try:
        with sync_playwright() as pw:
            try:
                browser = pw.chromium.launch()
            except Exception:
                # Reuse a locally installed stable Chrome when Playwright's bundled
                # Chromium is unavailable; this keeps export practical for agents.
                browser = pw.chromium.launch(channel="chrome")
            page = browser.new_page()
            for path, fmt in paths:
                width, height, pdf_width, pdf_height = DIMENSIONS[fmt]
                page.set_viewport_size({"width": width, "height": height})
                page.goto(path.resolve().as_uri(), wait_until="networkidle")
                page.evaluate("document.fonts.ready")
                if kind in ("png", "both", "all"):
                    page.locator(".canvas").screenshot(path=str(path.with_suffix(".png")))
                    count += 1
                if kind in ("jpg", "all"):
                    page.locator(".canvas").screenshot(
                        path=str(path.with_suffix(".jpg")), type="jpeg", quality=92
                    )
                    count += 1
                if kind in ("pdf", "both", "all"):
                    page.pdf(path=str(path.with_suffix(".pdf")), width=pdf_width, height=pdf_height,
                             print_background=True, margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
                    count += 1
            browser.close()
    except Exception as exc:
        raise SystemExit(
            f"Browser export failed: {exc}\nConfirm Chromium is installed with: .venv/bin/playwright install chromium"
        ) from exc
    return count

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--listing", type=Path, default=PACKS / "data/sample-listing.json")
    parser.add_argument("--branding", type=Path, default=PACKS / "data/sample-branding.json")
    parser.add_argument("--family", default="all", help="Family name, comma-separated names, or all")
    parser.add_argument("--formats", default="all", help="Format name, comma-separated names, or all")
    parser.add_argument("--output", type=Path, default=ROOT / "build/design-packs")
    parser.add_argument(
        "--export",
        choices=("none", "jpg", "png", "pdf", "both", "all"),
        default="none",
        help="both exports PNG+PDF; all exports JPG+PNG+PDF",
    )
    args = parser.parse_args()
    families = parse_csv(args.family, FAMILIES, "family")
    formats = parse_csv(args.formats, FORMATS, "format")
    listing_data = load_json(args.listing)
    branding_data = load_json(args.branding)
    if "listing" not in listing_data:
        raise SystemExit(f"{args.listing} must contain a top-level 'listing' object.")
    if "branding" not in branding_data:
        raise SystemExit(f"{args.branding} must contain a top-level 'branding' object.")
    data = {"listing": listing_data["listing"], "branding": branding_data["branding"]}
    validate(data)
    args.output.mkdir(parents=True, exist_ok=True)
    shutil.copytree(PACKS / "assets", args.output / "assets", dirs_exist_ok=True)
    generated = []
    for family in families:
        target = args.output / family
        target.mkdir(parents=True, exist_ok=True)
        for fmt in formats:
            source = PACKS / family / f"{fmt}.html"
            if not source.exists():
                raise SystemExit(f"Missing template: {source}")
            destination = target / source.name
            destination.write_text(populate(source.read_text(encoding="utf-8"), data), encoding="utf-8")
            generated.append((destination, fmt))
    exports = export_files(generated, args.export) if args.export != "none" else 0
    print(f"Generated {len(generated)} populated HTML file(s) in {args.output}")
    if exports:
        print(f"Exported {exports} file(s) via Chromium ({args.export}).")
    else:
        print("No PNG/PDF export requested; HTML output is ready for browser review.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
