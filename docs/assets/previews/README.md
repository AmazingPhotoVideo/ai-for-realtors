# Fictional preview assets

These screenshots are generated from the repository's fictional sample data and placeholder artwork. They are documentation previews—not real listings, real agents, or examples of media photographed by Amazing Photo Video.

The tracked images were captured with Google Chrome 150.0.7871.182 on macOS at device scale factor 1. The commands below use static local files, hide browser chrome and scrollbars, wait for compositor work, and write the exact tracked filenames. A newer Chrome release may rasterize fonts slightly differently.

## Rebuild design-pack previews

From the repository root:

```bash
python3 scripts/render_design_packs.py \
  --listing design-packs/data/sample-listing.json \
  --branding design-packs/data/sample-branding.json \
  --family all \
  --formats square-social \
  --output build/community-previews
```

```bash
CHROME='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
for family in editorial-luxury bold-modern warm-neighbourhood; do
  "$CHROME" --headless --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=1 --window-size=1080,1080 \
    --run-all-compositor-stages-before-draw --virtual-time-budget=1000 \
    --screenshot="$PWD/docs/assets/previews/${family}.png" \
    "file://$PWD/build/community-previews/${family}/square-social.html"
done
```

## Rebuild property-page previews

```bash
for design in cinematic editorial neighbourhood; do
  python3 property-pages/scripts/build.py \
    --listing property-pages/data/listing.sample.json \
    --branding property-pages/data/branding.sample.json \
    --assets property-pages/assets \
    --output build/property-page-previews \
    --base-url "https://example.com/${design}/" \
    --design "$design"
done
```

```bash
CHROME='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
for design in cinematic editorial neighbourhood; do
  "$CHROME" --headless --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=1 --window-size=1600,1600 \
    --run-all-compositor-stages-before-draw --virtual-time-budget=1000 \
    --screenshot="$PWD/docs/assets/previews/property-${design}.png" \
    "file://$PWD/build/property-page-previews/${design}/index.html"
done
```

## Rebuild Realtor-site previews

```bash
cd agent-sites
npm ci --include=dev
npm run build
python3 -m http.server 3001 --bind 127.0.0.1 --directory out
```

With that server running, use a second terminal from the repository root:

```bash
CHROME='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
for preset in luxury-editorial neighbourhood-journal modern-team; do
  "$CHROME" --headless --disable-gpu --hide-scrollbars \
    --force-device-scale-factor=1 --window-size=1440,1200 \
    --run-all-compositor-stages-before-draw --virtual-time-budget=3000 \
    --screenshot="$PWD/docs/assets/previews/agent-${preset}.png" \
    "http://127.0.0.1:3001/presets/${preset}/"
done
```

Before replacing tracked previews, confirm that each output contains only fictional sample details, loads all local artwork, has no visible errors, and does not imply APV produced listing media.
