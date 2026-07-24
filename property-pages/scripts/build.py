#!/usr/bin/env python3
"""Validate listing/branding JSON and build three deployable static property pages."""
from __future__ import annotations

import argparse
import html
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

DESIGNS = ("cinematic", "editorial", "neighbourhood")
TOKEN_RE = re.compile(r"__[A-Z][A-Z0-9_]*__")
URL_KEYS = re.compile(r"(?:url|src|href|endpoint|website|image)$", re.I)
HEX_RE = re.compile(r"^#[0-9a-fA-F]{6}$")

class ValidationError(ValueError):
    pass

def load_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"Cannot read valid JSON from {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValidationError(f"{path} must contain a JSON object")
    return value

def require(data: dict, dotted: str, errors: list[str]):
    value = data
    for key in dotted.split("."):
        if not isinstance(value, dict) or key not in value:
            errors.append(f"missing required fact: {dotted}")
            return None
        value = value[key]
    if value is None or value == "" or value == []:
        errors.append(f"missing required fact: {dotted}")
    return value

def is_safe_url(value: str, *, endpoint: bool = False) -> bool:
    if not isinstance(value, str) or not value.strip():
        return False
    if any(ord(ch) < 32 for ch in value) or value.startswith(("//", "\\")):
        return False
    parsed = urlparse(value)
    if endpoint:
        return parsed.scheme == "https" and bool(parsed.netloc) and not parsed.username
    if parsed.scheme:
        return parsed.scheme == "https" and bool(parsed.netloc) and not parsed.username
    return not value.startswith("/") and ".." not in Path(value).parts and not value.startswith("#")

def walk_urls(value, errors: list[str], path="root"):
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            if child not in (None, "") and URL_KEYS.search(key) and isinstance(child, str):
                if key.lower() in {"email", "phone"}:
                    continue
                if not is_safe_url(child, endpoint=key.lower() == "endpoint"):
                    errors.append(f"dangerous or unsupported URL at {child_path}: {child!r}")
            walk_urls(child, errors, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            walk_urls(child, errors, f"{path}[{index}]")

def validate(listing: dict, branding: dict) -> list[str]:
    errors: list[str] = []
    for field in ("status", "address.display", "address.street", "address.locality", "address.region", "address.country", "description", "features", "media.gallery", "location.label", "agent.name", "agent.brokerage", "agent.email", "agent.phone", "disclaimers"):
        require(listing, field, errors)
    for field in ("siteName", "colors.primary", "colors.accent", "form.enabled", "form.consentText", "analytics.enabled"):
        require(branding, field, errors)
    display = listing.get("address", {}).get("display")
    if display not in {"full", "street_only", "city_only", "custom"}:
        errors.append("address.display must be full, street_only, city_only, or custom")
    if display == "custom" and not listing.get("address", {}).get("customLabel"):
        errors.append("missing required fact: address.customLabel (required for custom display)")
    if listing.get("price", {}).get("visible") and not listing.get("price", {}).get("amount"):
        errors.append("missing required fact: price.amount (required when price.visible is true)")
    if not isinstance(listing.get("features"), list) or any(not isinstance(item, str) or not item.strip() for item in listing.get("features", [])):
        errors.append("features must be a non-empty list of non-empty strings")
    if not isinstance(listing.get("disclaimers"), list) or any(not isinstance(item, str) or not item.strip() for item in listing.get("disclaimers", [])):
        errors.append("disclaimers must be a non-empty list of non-empty strings")
    for field in ("bedrooms", "bathrooms", "interiorSize"):
        value = listing.get("specs", {}).get(field)
        if value is not None and (not isinstance(value, (int, float)) or isinstance(value, bool) or value < 0):
            errors.append(f"specs.{field} must be a non-negative number when provided")
    amount = listing.get("price", {}).get("amount")
    if amount is not None and (not isinstance(amount, (int, float)) or isinstance(amount, bool) or amount < 0):
        errors.append("price.amount must be a non-negative number when provided")
    open_houses = listing.get("openHouses", [])
    if not isinstance(open_houses, list):
        errors.append("openHouses must be a list")
    else:
        for index, event in enumerate(open_houses):
            if not isinstance(event, dict):
                errors.append(f"openHouses[{index}] must be an object")
                continue
            parsed = []
            for key in ("start", "end"):
                try:
                    moment = datetime.fromisoformat(event.get(key, ""))
                    if moment.tzinfo is None:
                        raise ValueError
                    parsed.append(moment)
                except (TypeError, ValueError):
                    errors.append(f"openHouses[{index}].{key} must be an ISO-8601 date-time with timezone")
            if len(parsed) == 2 and parsed[1] <= parsed[0]:
                errors.append(f"openHouses[{index}].end must be after start")
    gallery = listing.get("media", {}).get("gallery", [])
    if not isinstance(gallery, list) or not gallery:
        errors.append("media.gallery must contain at least one image")
    else:
        for index, image in enumerate(gallery):
            if not isinstance(image, dict) or not image.get("src") or not image.get("alt"):
                errors.append(f"media.gallery[{index}] requires src and meaningful alt text")
    form = branding.get("form", {})
    if not isinstance(form.get("enabled"), bool):
        errors.append("form.enabled must be true or false")
    analytics = branding.get("analytics", {})
    if not isinstance(analytics.get("enabled"), bool):
        errors.append("analytics.enabled must be true or false")
    if analytics.get("enabled"):
        if analytics.get("provider") not in {"plausible", "google"}:
            errors.append("analytics.provider must be plausible or google when enabled")
        if not analytics.get("siteId"):
            errors.append("analytics.siteId is required when analytics is enabled")
    if form.get("enabled") and not form.get("consentText"):
        errors.append("form.consentText is required when the lead form is enabled")
    endpoint = form.get("endpoint")
    if endpoint and not is_safe_url(endpoint, endpoint=True):
        errors.append("form.endpoint must be an HTTPS URL without embedded credentials")
    fallback = form.get("fallbackEmail") or listing.get("agent", {}).get("email")
    if form.get("enabled") and not endpoint and not fallback:
        errors.append("form requires an HTTPS endpoint or fallback email")
    for color in ("primary", "accent", "surface"):
        value = branding.get("colors", {}).get(color)
        if value and not HEX_RE.match(value):
            errors.append(f"branding colors.{color} must be a six-digit hex colour")
    walk_urls(listing, errors, "listing")
    walk_urls(branding, errors, "branding")
    return sorted(set(errors))

def address_label(listing: dict) -> str:
    address = listing["address"]
    display = address["display"]
    if display == "custom":
        return address["customLabel"]
    if display == "city_only":
        return ", ".join(x for x in (address.get("locality"), address.get("region")) if x)
    if display == "street_only":
        return address["street"]
    return ", ".join(x for x in (address.get("street"), address.get("locality"), address.get("region")) if x)

def absolute_url(base_url: str, candidate: str) -> str:
    if candidate.startswith("https://"):
        return candidate
    return f"{base_url.rstrip('/')}/{candidate.lstrip('./')}"

def json_ld(listing: dict, branding: dict, base_url: str) -> dict:
    address = listing["address"]
    agent = listing["agent"]
    data = {
        "@context": "https://schema.org",
        "@type": "SingleFamilyResidence",
        "name": address_label(listing),
        "description": listing["description"],
        "url": base_url,
        "address": {
            "@type": "PostalAddress",
            "streetAddress": address.get("street"),
            "addressLocality": address.get("locality"),
            "addressRegion": address.get("region"),
            "postalCode": address.get("postalCode"),
            "addressCountry": address.get("country"),
        },
        "image": [absolute_url(base_url, item["src"]) for item in listing["media"]["gallery"]],
        "numberOfBedrooms": listing.get("specs", {}).get("bedrooms"),
        "numberOfBathroomsTotal": listing.get("specs", {}).get("bathrooms"),
        "floorSize": ({"@type": "QuantitativeValue", "value": listing.get("specs", {}).get("interiorSize"), "unitText": listing.get("specs", {}).get("interiorUnit")} if listing.get("specs", {}).get("interiorSize") else None),
        "offers": ({"@type": "Offer", "price": listing.get("price", {}).get("amount"), "priceCurrency": listing.get("price", {}).get("currency"), "availability": "https://schema.org/InStock"} if listing.get("price", {}).get("visible") and listing.get("price", {}).get("amount") else None),
        "seller": {"@type": "RealEstateAgent", "name": agent.get("name"), "email": agent.get("email"), "telephone": agent.get("phone"), "worksFor": {"@type": "RealEstateAgent", "name": agent.get("brokerage")}},
    }
    def prune(value):
        if isinstance(value, dict):
            return {k: prune(v) for k, v in value.items() if v not in (None, "", [], {})}
        if isinstance(value, list):
            return [prune(v) for v in value if v not in (None, "", [], {})]
        return value
    return prune(data)

def build(listing_path: Path, branding_path: Path, output: Path, base_url: str, assets: Path | None = None, designs=DESIGNS) -> list[Path]:
    listing, branding = load_json(listing_path), load_json(branding_path)
    errors = validate(listing, branding)
    if errors:
        raise ValidationError("Validation failed:\n- " + "\n- ".join(errors))
    package = Path(__file__).resolve().parents[1]
    output.mkdir(parents=True, exist_ok=True)
    built = []
    label = address_label(listing)
    hero = listing["media"]["gallery"][0]
    for design in designs:
        if design not in DESIGNS:
            raise ValidationError(f"Unknown design {design!r}; choose from {', '.join(DESIGNS)}")
        target = output / design
        if target.exists():
            shutil.rmtree(target)
        target.mkdir(parents=True)
        template = (package / "templates" / design / "index.html").read_text(encoding="utf-8")
        page_url = f"{base_url.rstrip('/')}/{design}/"
        replacements = {
            "__LISTING_JSON__": json.dumps(listing, ensure_ascii=False).replace("</", "<\\/"),
            "__BRANDING_JSON__": json.dumps(branding, ensure_ascii=False).replace("</", "<\\/"),
            "__JSON_LD__": json.dumps(json_ld(listing, branding, page_url), ensure_ascii=False).replace("</", "<\\/"),
            "__PAGE_TITLE__": html.escape(f"{label} | {branding['siteName']}", quote=True),
            "__META_DESCRIPTION__": html.escape(listing["description"][:155], quote=True),
            "__CANONICAL_URL__": html.escape(page_url, quote=True),
            "__SOCIAL_IMAGE__": html.escape(absolute_url(page_url, hero["src"]), quote=True),
            "__THEME_COLOR__": html.escape(branding["colors"]["primary"], quote=True),
        }
        for token, value in replacements.items():
            template = template.replace(token, value)
        unresolved = TOKEN_RE.findall(template)
        if unresolved:
            raise ValidationError(f"Unresolved placeholders in {design}: {sorted(set(unresolved))}")
        (target / "index.html").write_text(template, encoding="utf-8")
        shutil.copy2(package / "templates" / design / "styles.css", target / "styles.css")
        shutil.copy2(package / "shared" / "app.js", target / "app.js")
        source_assets = assets or package / "assets"
        if source_assets.exists():
            shutil.copytree(source_assets, target / "assets")
        built.append(target)
    return built

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--listing", required=True, type=Path)
    parser.add_argument("--branding", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--base-url", required=True, help="HTTPS deployment root used in canonical/social metadata")
    parser.add_argument("--assets", type=Path, help="Directory copied to output/design/assets")
    parser.add_argument("--design", choices=DESIGNS, action="append", dest="designs", help="Build only this design (repeatable)")
    args = parser.parse_args(argv)
    if not is_safe_url(args.base_url, endpoint=True):
        parser.error("--base-url must be an HTTPS URL without embedded credentials")
    try:
        built = build(args.listing, args.branding, args.output, args.base_url, args.assets, args.designs or DESIGNS)
    except ValidationError as exc:
        print(exc, file=sys.stderr)
        return 2
    for path in built:
        print(path)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
