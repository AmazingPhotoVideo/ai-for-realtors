---
name: single-property-page-builder
description: Build, verify, preview, and deploy a static single-property website from verified listing facts, approved branding, and owned or licensed media using the repository's cinematic, editorial, or neighbourhood templates.
version: 1.0.0
license: LicenseRef-APV-Design-Asset-Policy-0.2
---

# Single-Property Page Builder

Use this skill when an agent needs a public page for exactly one property. The workflow produces all three design options from one structured listing file and one branding file. It does **not** scrape MLS data, create a feed, or implement VOW/IDX access.

This skill and its page templates are governed by [`docs/design-asset-licensing.md`](../../docs/design-asset-licensing.md), not an open-source licence. APV retains the rights described there, including the right to change, suspend, or withdraw pilot permissions.

## Required intake

Collect and resolve these bracket variables before generation:

```text
[REPOSITORY_ROOT]
[LISTING_SLUG]
[PUBLIC_HTTPS_BASE_URL]
[DESIGN_CHOICE: cinematic|editorial|neighbourhood|all]
[STATUS]
[ADDRESS_DISPLAY: full|street_only|city_only|custom]
[STREET_ADDRESS]
[LOCALITY]
[REGION]
[POSTAL_CODE]
[COUNTRY]
[CUSTOM_ADDRESS_LABEL]
[PRICE_VISIBLE: true|false]
[PRICE_AMOUNT]
[PRICE_CURRENCY]
[BEDROOMS]
[BATHROOMS]
[INTERIOR_SIZE]
[INTERIOR_UNIT]
[PARKING]
[PROPERTY_TYPE]
[DESCRIPTION]
[FEATURES]
[GALLERY_FILES_WITH_ALT_TEXT_AND_CAPTIONS]
[VIDEO_HTTPS_URL]
[TOUR_3D_HTTPS_URL]
[FLOOR_PLAN_HTTPS_URL]
[OPEN_HOUSE_START_END_TIMEZONE]
[LOCATION_LABEL]
[MAP_HTTPS_URL]
[AGENT_NAME]
[AGENT_TITLE]
[BROKERAGE]
[AGENT_EMAIL]
[AGENT_PHONE]
[AGENT_WEBSITE]
[DISCLAIMERS]
[BRAND_SITE_NAME]
[BRAND_PRIMARY_HEX]
[BRAND_ACCENT_HEX]
[BRAND_SURFACE_HEX]
[LOCALE]
[FORM_ENABLED]
[FORM_HTTPS_ENDPOINT]
[FORM_FALLBACK_EMAIL]
[APPROVED_CONSENT_TEXT]
[ANALYTICS_ENABLED]
[ANALYTICS_PROVIDER_AND_SITE_ID]
[ASSET_DIRECTORY]
[OUTPUT_DIRECTORY]
[DEPLOYMENT_TARGET]
```

If a fact is unknown, ask for it or omit it when optional. Never invent a room count, measurement, status, price, date, feature, brokerage claim, licence, media credit, or neighbourhood claim.

## Workflow

### 1. Verify facts and approval

1. Identify the authoritative source for every listing fact: agent/brokerage record, approved listing sheet, seller-approved notes, or board-approved data export.
2. Confirm current status, price-display permission, address-display rule, open-house timezone, measurements, and disclaimers immediately before building.
3. Confirm the seller/brokerage permits a standalone public page and confirm local board/MLS advertising and trademark rules.
4. Record unknown optional facts as absent; JSON-LD deliberately omits absent facts.

### 2. Collect branding and images

1. Copy the sample JSON files to listing-specific working files.
2. Use only owned, commissioned, properly licensed, or explicitly approved media. Do not copy photographs from listing portals or competitor sites.
3. Give every gallery image accurate alt text. Optimize images outside this toolkit and use consistent orientation/quality.
4. Confirm logo, colours, agent identity, brokerage name, contacts, and required legal language.
5. Never say or imply APV shot, staged, measured, or produced the listing media unless that fact is verified.

Exact setup commands:

```bash
cd [REPOSITORY_ROOT]/property-pages
mkdir -p work/[LISTING_SLUG]/assets
cp data/listing.sample.json work/[LISTING_SLUG]/listing.json
cp data/branding.sample.json work/[LISTING_SLUG]/branding.json
# Put approved media in work/[LISTING_SLUG]/assets and edit both JSON files.
```

### 3. Configure address, price, media, forms, and analytics

- Set `address.display` to `full`, `street_only`, `city_only`, or `custom`; provide `customLabel` for custom mode.
- Set `price.visible` false when public price display is not approved. Do not use a fake or placeholder amount.
- Use HTTPS for remote media, map, agent website, form endpoint, and deployment URLs. Local images use paths such as `assets/front.jpg`.
- Set `form.enabled` false when lead capture is not approved.
- For email fallback, leave `endpoint` empty and set `fallbackEmail`. For endpoint mode, use a public HTTPS relay/form provider configured for browser JSON POST and deployed-domain CORS.
- Never put CRM/API credentials, private webhook tokens, signing secrets, or bearer tokens in JSON or static files. Keep secrets server-side.
- Replace consent copy with brokerage/legal-approved text covering the actual communication channels and jurisdiction. Confirm the endpoint stores the fields and consent record as required.
- Analytics is opt-in. Use only `plausible` with a domain or `google` with a `G-...` measurement ID, after privacy/cookie approval.

### 4. Generate all designs

```bash
cd [REPOSITORY_ROOT]/property-pages
python3 scripts/build.py \
  --listing work/[LISTING_SLUG]/listing.json \
  --branding work/[LISTING_SLUG]/branding.json \
  --assets work/[LISTING_SLUG]/assets \
  --output [OUTPUT_DIRECTORY] \
  --base-url [PUBLIC_HTTPS_BASE_URL]
```

To build only the approved design, append `--design [DESIGN_CHOICE]`. The command exits non-zero on missing required facts, invalid display rules, unsafe URLs, incomplete image metadata, invalid colours, or unresolved placeholders.

### 5. Preview and QA

```bash
cd [REPOSITORY_ROOT]/property-pages
python3 -m unittest discover -s tests -v
node --check shared/app.js
python3 -m http.server 8080 --directory [OUTPUT_DIRECTORY]
```

Open `http://localhost:8080/[DESIGN_CHOICE]/` and QA at 320 px, 768 px, and desktop widths. Complete this checklist:

- [ ] Address privacy rule and price visibility are correct.
- [ ] Status, specs, description, features, location, open-house timezone, and contact facts match approved sources.
- [ ] Every image loads, has honest alt text, and is licensed/approved.
- [ ] Gallery opens by keyboard, close control receives focus, Escape closes it, and focus returns to the trigger.
- [ ] Sticky/contact CTAs work without covering essential content.
- [ ] Tab order, focus indicators, labels, colour contrast, and reduced-motion mode are usable.
- [ ] Video, 3D, floor-plan, map, phone, email, and agent links work.
- [ ] Form success and failure/email-fallback paths are tested with non-sensitive test data; consent copy and storage are approved.
- [ ] Canonical URL, Open Graph/Twitter tags, page title, description, and JSON-LD match the final public URL.
- [ ] Source and built HTML contain no `__PLACEHOLDER__`, credentials, test contacts, or unapproved claims.
- [ ] Disclaimers and board/brokerage-required marks appear correctly.
- [ ] APV toolkit attribution remains in the public footer and does not claim APV made the listing media.

### 6. Deploy

Supported static deployment choices include brokerage-approved hosting, GitHub Pages, Cloudflare Pages, Netlify, Vercel static hosting, or an S3-compatible static host. Upload the **contents** of `[OUTPUT_DIRECTORY]/[DESIGN_CHOICE]/`, enforce HTTPS, configure the custom domain, then recheck the final URL and form CORS. Follow the brokerage's data-retention, privacy, accessibility, and takedown process when the listing status changes.

## VOW / IDX / board boundary

These templates make a static page for one verified listing. They are not an MLS feed, VOW, IDX display, or substitute for board-approved data licensing. Obtain seller, brokerage, MLS/board, trademark, and advertising approval before publishing. For compliant VOW/IDX integrations, contact Amazing Photo Video at https://amazingphotovideo.com.

## Required APV attribution

Every generated public page must retain this linked footer credit:

> Property marketing toolkit by Amazing Photo Video — https://amazingphotovideo.com

Link the attribution to `https://amazingphotovideo.com`. Do not put it into MLS remarks or mandatory legal text, and do not phrase it as a photography/media credit unless APV truly produced that media.
