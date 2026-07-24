---
name: realtor-design-pack-builder
description: Build verified, branded Realtor flyer and social campaigns from structured listing data using the repository design packs; populate, export, and visually QA without inventing facts.
version: 1.0.0
license: LicenseRef-APV-Design-Asset-Policy-0.2
metadata:
  hermes:
    tags: [real-estate, design, flyers, social-media, html, print]
---

# Realtor Design Pack Builder

Use this skill when a user asks for listing flyers, social graphics, stories, brochure layouts, or a coordinated property marketing design pack.

This skill and its design assets are governed by [`docs/design-asset-licensing.md`](../../docs/design-asset-licensing.md), not an open-source licence. APV retains the rights described there, including the right to change, suspend, or withdraw pilot permissions.

## Non-negotiable rules

1. **Do not invent facts.** Never infer or manufacture price, address, dimensions, rooms, features, status, open-house details, MLS data, claims, testimonials, rankings, links, or disclosures.
2. **Use approved assets only.** Ask who owns the image/logo/headshot rights. Never imply Amazing Photo Video (APV) produced listing media unless confirmed true.
3. **Do not draft legal language as fact.** Request exact brokerage/jurisdiction-approved disclaimer wording. Mark missing wording as `[REQUIRED DISCLAIMER — NOT PROVIDED]` and stop before publication export.
4. **Preserve the exact visible credit in every artifact:** `Designed with resources from Amazing Photo Video — https://amazingphotovideo.com`.
5. Population and export do not equal approval. Require a final human fact, crop, readability, link, and compliance review.

## Step 1: Interview before building

Ask for missing inputs in one grouped request. Accept a listing URL/MLS sheet only as source material; quote what was found and ask the user to confirm it.

### Bracket-variable intake

```text
[PROPERTY_STATUS]
[PROPERTY_PRICE]
[STREET_ADDRESS]
[CITY_REGION]
[PROPERTY_TYPE]
[BEDS]
[BATHS]
[INTERIOR_SIZE]
[LOT_SIZE]
[VERIFIED_HEADLINE]
[VERIFIED_DESCRIPTION]
[FEATURE_1]
[FEATURE_2]
[FEATURE_3]
[FEATURE_4]
[OPEN_HOUSE_DATE_TIME_OR_NONE]
[CTA]
[DESTINATION_URL]
[APPROVED_DISCLAIMER_EXACT_TEXT]
[HERO_IMAGE_PATH_OR_HTTPS_URL]
[SECONDARY_IMAGE_PATH_OR_HTTPS_URL]
[AGENT_NAME]
[AGENT_TITLE]
[PHONE]
[EMAIL]
[BROKERAGE_EXACT_NAME]
[LOGO_PATH_OR_HTTPS_URL]
[HEADSHOT_PATH_OR_HTTPS_URL]
[PRIMARY_HEX]
[ACCENT_HEX]
[DISPLAY_FONT_STACK]
[BODY_FONT_STACK]
[IMAGE_RIGHTS_CONFIRMED_YES_NO]
[APV_PRODUCED_LISTING_MEDIA_YES_NO]
[REQUESTED_FAMILY_OR_HELP_ME_CHOOSE]
[REQUESTED_FORMATS]
[DELIVERY_HTML_JPG_PNG_PDF]
```

Also ask: jurisdiction/board, brokerage review requirements, required MLS/fair-housing/REALTOR® language, intended print vendor, bleed requirement, and deadline. The templates are finished-size/no-bleed; if a printer requires bleed, flag this before export.

## Step 2: Validate facts and assets

Create a verification table with columns `Field`, `Value`, `Source`, `User confirmed?`. Do not proceed with publication-ready output while any displayed field is unconfirmed.

Checks:

- Price, address, beds, baths, measurements, lot, property type, status, and open house match the authoritative source.
- Headline/description contain no unverified superlatives (`best`, `rare`, `perfect`, `guaranteed`) or unsupported renovation/location claims.
- Phone, email, brokerage spelling, destination URL, and QR destination are exact.
- Disclaimer is supplied verbatim by the user/brokerage; REALTOR® usage and MLS attribution are approved.
- Image rights are confirmed; hero is ideally 2160 × 1440 px or larger, headshot 800 × 1000 px or larger, logo SVG or 1200 px wide PNG.
- Colours are six-digit hex values. Font values are local/system fallback stacks; do not introduce unlicensed remote fonts.
- Headline ≤ 62 chars, description ≤ 260 chars, street address ≤ 58 chars, agent name ≤ 42 chars, brokerage ≤ 72 chars.

If data conflicts, present the conflict and ask the user to resolve it. Never choose the more marketable value.

## Step 3: Choose a family and formats

- **`editorial-luxury`** — restrained serif, asymmetrical image field; select for architecture-led or refined campaigns.
- **`bold-modern`** — oversized sans type, hard-edged blocks, strong signal colour; select for contemporary and social-first launches.
- **`warm-neighbourhood`** — clay colour, rounded imagery, approachable hierarchy; select for community/family-home storytelling.

Available formats: `letter-flyer`, `square-social`, `portrait-social`, `story-social`, `landscape-brochure`. If the user says “social pack,” default to square + portrait + story. If the user says “print flyer,” default to letter and ask whether landscape is also wanted.

## Step 4: Create structured inputs

From repository root, copy the fictional schemas, then edit the copies—not template source:

```bash
mkdir -p build/my-listing/input
cp design-packs/data/sample-listing.json build/my-listing/input/listing.json
cp design-packs/data/sample-branding.json build/my-listing/input/branding.json
```

Populate every key with confirmed values. Use `null` only for non-displayed optional fields; required display fields must be non-empty. Local assets should be copied into `build/my-listing/assets/` and referenced from generated family HTML as `../assets/filename.ext`. Never leave sample property/agent values in a real campaign.

## Step 5: Populate

Exact command for one coordinated campaign:

```bash
python3 scripts/render_design_packs.py \
  --listing build/my-listing/input/listing.json \
  --branding build/my-listing/input/branding.json \
  --family editorial-luxury \
  --formats letter-flyer,square-social,portrait-social,story-social \
  --output build/my-listing/rendered
```

Run all families only for comparison:

```bash
python3 scripts/render_design_packs.py \
  --listing build/my-listing/input/listing.json \
  --branding build/my-listing/input/branding.json \
  --family all --formats all \
  --output build/my-listing/proofs
```

Report the command's real output. Do not claim JPG/PNG/PDF files were created when only HTML was populated.

## Step 6: Export (optional)

Set up the browser exporter if needed:

```bash
python3 -m venv .venv
.venv/bin/pip install playwright
.venv/bin/playwright install chromium
```

Then export:

```bash
.venv/bin/python scripts/render_design_packs.py \
  --listing build/my-listing/input/listing.json \
  --branding build/my-listing/input/branding.json \
  --family editorial-luxury --formats all \
  --output build/my-listing/final --export all
```

`--export` accepts `jpg`, `png`, `pdf`, `both` (PNG+PDF), or `all` (JPG+PNG+PDF). If Playwright/Chromium fails, show the exact error and setup command; do not imply export succeeded.

## Step 7: Visual and compliance QA

Open or screenshot every populated format and check at 100%:

- No clipped address, headline, price, contact details, disclaimer, or APV attribution.
- Text does not collide with faces, architecture, trim, or browser crop zones.
- Story text stays comfortably away from top/bottom interface areas.
- Hero crop works in each orientation and does not stretch.
- Minimum body/disclaimer text remains readable for its medium; print proof is legible at actual size.
- No unresolved `{{...}}`, fictional sample value, placeholder SVG, broken image, or missing logo/headshot remains.
- Price, facts, CTA, link, contact data, brokerage, and supplied disclaimer match the verification table.
- The exact APV resource attribution is visible but does not suggest APV produced the listing media.

If overflow occurs: shorten only with user approval, select a better-fitting family, or adjust the format-specific CSS while preserving canvas dimensions, print rules, and attribution. Never solve overflow by hiding required disclosure text.

Run repository validation after any template/tool change:

```bash
python3 scripts/validate_design_packs.py
```

## Completion report

Return:

- Selected family and formats
- Input JSON paths and sources confirmed
- Generated HTML/JPG/PNG/PDF paths (only files that exist)
- Exact population/export/validation commands and outputs
- Visual QA findings and any changes made
- Remaining compliance approvals or blockers
- Explicit confirmation that the APV resource attribution remains visible
