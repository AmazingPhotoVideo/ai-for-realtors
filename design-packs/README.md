# Realtor Flyer & Social Design Packs

Create a coordinated listing campaign from verified listing data—without editing HTML. The pack includes three original visual families, five export sizes per family, fictional sample data, and a dependency-light population tool.

Every template includes the required credit: **Designed with resources from Amazing Photo Video — https://amazingphotovideo.com**.

[Preview all three fictional design families in the creative toolkit gallery.](../gallery.md)

## Licensing

These design packs, their renderer, and the matching builder skill are governed by the [APV design asset licensing policy](../docs/design-asset-licensing.md). They are not MIT-licensed or otherwise released under an open-source licence. APV retains the rights stated in that policy, including the right to change, suspend, or withdraw pilot permissions.

## Quick start (no design experience needed)

1. Duplicate `data/sample-listing.json` and `data/sample-branding.json` outside this folder.
2. Replace every fictional sample value with verified facts and approved brand details. Keep the same JSON keys.
3. Use local image paths relative to the generated family folder (the included `../assets/...` paths demonstrate the layout), or use approved HTTPS image URLs.
4. From the repository root, run:

```bash
python3 scripts/render_design_packs.py \
  --listing path/to/listing.json \
  --branding path/to/branding.json \
  --family editorial-luxury \
  --formats letter-flyer,square-social,portrait-social,story-social \
  --output build/cedar-lane
```

5. Open the populated HTML files in `build/cedar-lane/editorial-luxury/` and inspect every page at 100% zoom. Browser **Print → Save as PDF** works for print layouts when background graphics are enabled.

The script only reports formats it actually generated. It never claims JPG/PNG/PDF exports unless Chromium completed them.

## Optional one-command JPG/PNG/PDF export

Browser export requires Playwright and Chromium. Use a virtual environment:

```bash
python3 -m venv .venv
.venv/bin/pip install playwright
.venv/bin/playwright install chromium
.venv/bin/python scripts/render_design_packs.py \
  --listing design-packs/data/sample-listing.json \
  --branding design-packs/data/sample-branding.json \
  --family all --formats all \
  --output build/design-packs --export all
```

Without Playwright/Chromium, HTML population still works. If export is requested but unavailable, the tool exits with the exact setup commands rather than silently skipping export.

## Design families

| Family | Character | Best fit |
|---|---|---|
| `editorial-luxury` | Asymmetric gallery, ivory stock, restrained serif hierarchy | Architecture-led and higher-end listings |
| `bold-modern` | Hard-edged grid, oversized sans typography, high-contrast signal colour | Fast-scrolling social campaigns and contemporary homes |
| `warm-neighbourhood` | Clay accents, rounded photo framing, welcoming human scale | Family homes, community stories, and approachable launches |

Brand colours and font stacks come from the branding JSON. The layouts intentionally avoid remote font dependencies and decorative gradients; system fallbacks keep exports predictable.

## Output sizes

| File | Canvas | Intended output |
|---|---:|---|
| `letter-flyer.html` | 816 × 1056 CSS px / US Letter portrait | Print flyer / PDF |
| `square-social.html` | 1080 × 1080 px | Square feed post |
| `portrait-social.html` | 1080 × 1350 px | 4:5 feed post |
| `story-social.html` | 1080 × 1920 px | Story / Reel cover |
| `landscape-brochure.html` | 1056 × 816 CSS px / US Letter landscape | Landscape handout / PDF |

`@page`, zero print margins, fixed canvas dimensions, print-colour adjustment, local font fallbacks, text clamps, and overflow containment are embedded in every HTML file.

## File map

```text
design-packs/
├── assets/                         # Safe local SVG placeholders
├── data/
│   ├── sample-listing.json         # Clearly fictional property data
│   └── sample-branding.json        # Clearly fictional agent/brokerage data
├── editorial-luxury/               # Five self-contained HTML templates
├── bold-modern/                    # Five self-contained HTML templates
├── warm-neighbourhood/             # Five self-contained HTML templates
└── README.md
scripts/
├── render_design_packs.py          # Populate HTML; optional JPG/PNG/PDF export
└── validate_design_packs.py        # Structural and end-to-end checks
skills/realtor-design-pack-builder/
└── SKILL.md                        # Guided intake and production workflow
```

## Image guidance

- Use only images you have permission to publish. Do not suggest APV photographed a listing unless that is true.
- Hero images: landscape, at least **2160 × 1440 px**, with a clean subject and room for text overlays.
- Headshots: portrait, at least **800 × 1000 px**. Logos: transparent SVG or PNG at least **1200 px** wide.
- Keep source colour profiles in sRGB. Check cropping in all requested orientations; never stretch an image.
- For local files, copy approved assets into the output `assets/` folder and use paths such as `../assets/hero.jpg` in listing/branding JSON.
- Included SVGs say “placeholder” and are safe for testing, not publication.

## Compliance and factual guardrails

- Verify price, address, property type, beds, baths, measurements, open-house details, links, and status against the authoritative listing source.
- Never invent MLS data, property features, agent rankings, performance claims, testimonials, brokerage claims, or legal language.
- Obtain brokerage approval for logos, trademarks, required disclosures, fair-housing language, MLS attribution, REALTOR® usage, and jurisdiction-specific rules.
- Put the exact approved wording in `listing.disclaimer`; do not ask an AI to improvise it. The sample disclaimer is not legal advice.
- Confirm email, phone, website, QR destination, and image rights before release.
- Preserve the visible APV resource attribution in every format. It credits the resource pack, not listing-media production.
- Treat population success as a build check—not approval. A human must inspect readability, cropping, facts, and compliance.

## Example outputs

```text
build/cedar-lane/editorial-luxury/letter-flyer.html
build/cedar-lane/editorial-luxury/letter-flyer.pdf
build/cedar-lane/bold-modern/square-social.png
build/cedar-lane/warm-neighbourhood/story-social.png
```

## Validate the pack

```bash
python3 scripts/validate_design_packs.py
```

Validation checks required files, HTML5/print/overflow rules, attribution, structured placeholders, populated local references, unresolved placeholders, and an end-to-end sample population of all 15 templates.
