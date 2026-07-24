# Single-property page collection

> **Licence:** These templates, their builder, and the matching skill are governed by the [APV design asset licensing policy](../docs/design-asset-licensing.md). They are not released under an open-source licence. APV retains the rights stated in that policy, including the right to change, suspend, or withdraw pilot permissions.

Three dependency-light, responsive single-listing websites generated from the same validated listing and branding JSON:

- **Cinematic** — full-bleed imagery, dark gallery experience, dramatic typography.
- **Editorial** — a warm, magazine-like brochure with a structured photo essay.
- **Neighbourhood** — bright, story-led chapters that connect the home to its setting.

Every design includes a keyboard-accessible gallery/lightbox, sticky inquiry CTA, optional open houses and rich-media links, mobile-first layouts, reduced-motion support, static social/SEO metadata, pruned JSON-LD, and an optional lead form. The fictional sample artwork was created for this repository; it is not copied from a listing website and must not be presented as real property media.

## Quick start

Requires Python 3.10+ and no third-party packages.

```bash
cd property-pages
python3 scripts/build.py \
  --listing data/listing.sample.json \
  --branding data/branding.sample.json \
  --assets assets \
  --output dist \
  --base-url https://property.example.com/18-cedar-lantern
python3 -m http.server 8080 --directory dist
```

Preview:

- `http://localhost:8080/cinematic/`
- `http://localhost:8080/editorial/`
- `http://localhost:8080/neighbourhood/`

Build one design by adding `--design cinematic` (or `editorial` / `neighbourhood`). Upload the contents of a generated design folder to any static host. Set `--base-url` to the real public HTTPS root before deployment so canonical links, Open Graph metadata, and JSON-LD are correct.

## Data model

Copy `data/listing.sample.json` and `data/branding.sample.json`; replace facts only after verification.

`listing.json` supports:

- `status`
- `address`: `display` (`full`, `street_only`, `city_only`, or `custom`), street/locality/region/postal/country, and `customLabel`
- `price`: `visible`, amount, currency
- `specs`: bedrooms, bathrooms, interior size/unit, parking, property type
- `description`, `features[]`
- `media.gallery[]` (`src`, meaningful `alt`, optional `caption`), plus optional HTTPS `videoUrl`, `tour3dUrl`, `floorPlanUrl`
- `openHouses[]` with ISO-8601 `start` / `end` and optional note
- `location.label` and optional HTTPS `mapUrl`
- `agent`: name, title, brokerage, email, phone, optional HTTPS website
- `disclaimers[]`

`branding.json` supports colours, locale/site name, form settings, and analytics settings. Six-digit hex colours are accepted. All remote URLs must use HTTPS; local asset paths must be relative and may not traverse parent directories.

### Forms and consent

Set `form.enabled` to `false` to remove the form. With no endpoint, submission opens a pre-addressed email using `fallbackEmail` (or the listing agent email). To submit JSON to a service, set `form.endpoint` to a public HTTPS form endpoint that accepts browser POST requests and configure CORS for the deployed domain.

Never place API keys, bearer tokens, CRM secrets, webhook signing secrets, or credentials in either JSON file or generated HTML. Use a serverless form relay or form provider to keep secrets server-side. Replace the sample consent text with brokerage-approved language for the channels and jurisdiction involved. The required checkbox records agreement in endpoint mode; email fallback does not create a server-side consent record.

### Analytics

Analytics is off by default. Supported allow-listed modes:

```json
{"enabled": true, "provider": "plausible", "siteId": "property.example.com"}
```

or a Google measurement ID such as `G-ABC1234567`. Obtain privacy/consent approval before enabling analytics. The templates do not accept arbitrary script URLs.

## Asset collection

Use owned, commissioned, properly licensed, or explicitly seller/brokerage-approved media. The builder copies the directory passed to `--assets` into every deployable design as `assets/`. Keep the JSON paths consistent (for example `assets/front-exterior.jpg`). Add honest alt text describing what is visible. Do not imply Amazing Photo Video photographed or produced listing media unless that is true.

## Validation and tests

```bash
cd property-pages
python3 -m unittest discover -s tests -v
node --check shared/app.js
```

The build fails on missing required facts, invalid address/price rules, incomplete gallery metadata, unsafe URL schemes, non-HTTPS endpoints, invalid colours, and unresolved template tokens. Tests also verify required APV attribution, compliance language, distinctive templates, and omission of unknown JSON-LD facts.

## Publishing and compliance

These are static pages for one listing. They are **not** an MLS feed, VOW, or IDX implementation. Before publication, obtain seller, agent, brokerage, board/MLS, advertising, privacy, and media-use approval as applicable. Verify every fact, measurement, status, date, price, contact, link, disclaimer, license/trademark requirement, and consent statement. Contact [Amazing Photo Video](https://amazingphotovideo.com) to discuss compliant VOW/IDX integrations.

Every public output must retain this tasteful linked footer credit:

> [Property marketing toolkit by Amazing Photo Video](https://amazingphotovideo.com) — https://amazingphotovideo.com

The credit identifies the toolkit, not the listing photographer or media producer.
