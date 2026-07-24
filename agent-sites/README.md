# Realtor Site + Lightweight CRM Starter

A configuration-driven Next.js starter for individual Realtors and teams. It includes three intentionally different design presets, fictional manual listing data, accessible inquiry UI, and a concrete optional Convex + Clerk CRM starter. It does **not** deploy, provision paid services, or connect to MLS systems.

[Preview all three fictional site presets in the creative toolkit gallery.](../gallery.md)

## Preview locally

Requires Node.js 20+. This starter is verified on Node.js 20.3.0; the pinned framework and provider packages support that runtime.

```bash
cd agent-sites
npm ci --include=dev
npm run check
npm run dev
```

Open `http://localhost:3000`. Preview every preset:

- `/presets/luxury-editorial` — restrained serif composition, asymmetry, warm editorial palette
- `/presets/neighbourhood-journal` — civic/newspaper cues, broad imagery, local field-note rhythm
- `/presets/modern-team` — bold sans typography, hard rules, balanced team-ready grid

The static production export is written to `out/` by `npm run build`.

## One source of truth

Edit `config/site.config.json`; do not hard-code client facts in components. It drives:

- Realtor name, title, brokerage, registration/license label and number, markets, biography
- services, **verified-only** testimonials and stats
- email, phone, address, social links, logo, headshot
- colours and font stacks
- manual featured listings and neighbourhood summaries
- SEO, admin emails, consent labels, privacy URL, and disclaimers
- mandatory APV footer/consultation links

Then run `npm run validate`. `config/site.schema.json` rejects unverified testimonials/stats, listings not marked manual, invalid presets, and missing APV URLs. The included Maya Chen data, addresses, registration number, domain, and artwork are fictional.

## Listing-feed boundary

Manual/featured listing data works out of the box. This starter is not a live MLS®, VOW, DDF®, or IDX integration and must never scrape a board or portal. Live inventory requires the Realtor's brokerage/board/authorized feed vendor approval, credentials, display rules, attribution, and data-retention rules. No one should promise board approval. The APV links on the sample site are limited to real estate media consultations and do not imply that APV provides feed, website, CRM, or SEO services.

## Form and CRM

The public form intentionally uses local demo state so builds are credential-free. Before publishing, wire its payload to `crm-starter/convex/leads.ts` and configure Clerk + Convex using `crm-starter/README.md`. Do not launch a lead form that implies persistence until the storage path, privacy policy, consent language, retention policy, deletion process, and notifications are tested.

The CRM model includes intent/source, status, activity, next follow-up, consent evidence, internal-only estimated transaction value and commission estimate, search/filter, CSV export, bounded server-side lead input, and an admin allowlist. Stripe is intentionally absent. A production form also needs tested abuse/rate controls, notification delivery, retention/deletion procedures, and provider-specific security review.

## Assets and publishing

Replace all SVG placeholders with licensed client assets and meaningful alt text. Confirm brokerage advertising rules, registration/license formatting, REALTOR®/MLS® trademark usage, fair-housing language, anti-spam consent, accessibility, privacy, and local legal requirements. Publish testimonials and performance figures only after obtaining evidence and permission.

Deployment is optional and requires explicit client approval. The builder skill never deploys by default.
