---
name: realtor-site-crm-builder
description: Scaffold and verify an original Realtor marketing website with one of three presets and an optional Convex + Clerk lead CRM. Use for Realtor/agent/team site builds, brand intake, manual featured listings, or a lightweight lead workspace.
version: 1.0.0
license: LicenseRef-APV-Design-Asset-Policy-0.2
---

# Realtor Site + CRM Builder

Build from `agent-sites/` without inventing business facts, scraping listings, or performing unapproved provider/deployment actions. The repeatable path is copy → configure one JSON file → validate → test → build. It is intentionally friendly to local models: complete each numbered step and run its check before continuing.

## Non-negotiable boundaries

- Facts first. Never invent testimonials, sales volume, rankings, awards, years, neighbourhood claims, brokerage, registration/license details, listing availability, or market statistics. Omit unknown testimonials/stats; the schema accepts empty arrays.
- Write original copy from confirmed facts. Do not copy an existing agent's pages, third-party brand voice, testimonials, or proprietary claims.
- Manual featured listings work out of the box and must retain `manual: true` plus a visible not-live-feed disclosure.
- Never scrape MLS®, REALTOR.ca, a board, brokerage portal, or vendor. Live VOW/IDX/DDF/board feeds require the owner's brokerage/board/authorized feed-vendor credentials, agreements, display/refresh/retention rules, and approval. Never promise board approval or imply APV supplies the integration.
- Do not deploy, create cloud projects, spend money, purchase domains, or trigger external/billable provider actions without explicit approval after showing scope and likely costs.
- Do not imply APV shot a property or provides a specific service without confirmation. Phrase public links as contact/consultation requests.
- Keep the mandatory linked footer credit and the two useful APV consultation CTAs.

## Step 1 — intake once

Ask in one message. Record `unknown` rather than guessing.

1. Individual or team name, pronouns, professional title, brokerage legal display name, office/address display rules.
2. Jurisdiction, regulator/board, required registration/license label and number, brokerage disclaimers, trademark rules.
3. Primary markets and objective property/local expertise; languages offered.
4. Biography facts, service process, property types, client types, contact channels, social URLs.
5. Logo/headshot/listing-image files and proof they may be published; preferred colours/type style.
6. Testimonials and stats, each with source/evidence, publication permission, and exact approved attribution. Otherwise omit.
7. Manual featured listings, with permission, status, address-display preference, price, beds/baths, image/alt text, and destination.
8. Neighbourhood facts and sources. Avoid protected-class proxies, subjective demographic fit, steering, school-quality claims, and unsourced market claims.
9. Contact-form purpose, required/optional consent wording, privacy URL, retention/deletion owner, anti-spam jurisdiction (for example CASL/TCPA), and admins.
10. Domain/SEO title/description and whether CRM or live feed is in scope.

Show a compact fact sheet and have the owner mark corrections. Copy from sources as facts only, then generate original language.

## Step 2 — select one preset

- `luxury-editorial`: image-led, restrained, serif, asymmetrical; suited to a premium individual practice without making luxury claims.
- `neighbourhood-journal`: warm local publication rhythm; suited to a place-led neighbourhood expert.
- `modern-team`: bold sans typography and structured grids; suited to teams and broader service lines.

Use the owner's audience/assets—not price point stereotypes—to choose. Set `preset` in `config/site.config.json`. All three remain previewable at `/presets/<name>`.

## Step 3 — scaffold mechanically

```bash
cp -R agent-sites /approved/path/client-slug
cd /approved/path/client-slug
npm ci --include=dev
```

Never copy `.env*`, `.next/`, `out/`, or `node_modules/` from another client. Keep dependency versions pinned unless a tested security update is required.

**CHECK:** `test -f config/site.config.json && test -f config/site.schema.json` exits 0.

## Step 4 — configure one source of truth

Edit only `config/site.config.json` for client identity/content. Replace all fictional Maya Chen data and placeholder `.test` links. Use licensed local assets under `public/`; write descriptive alt text. Keep arrays empty for unverified stats/testimonials. Do not put secrets in config.

Preserve:

- APV `mediaConsultationUrl` and `mediaPlanningUrl` as `https://amazingphotovideo.com`.
- A footer label containing `Amazing Photo Video`.
- Required consent separate from optional marketing consent.
- Manual listing flags and feed disclaimer.

**CHECK:** `npm run validate` prints `Valid Realtor config: <name> / <preset>`.

## Step 5 — original copy and compliance review

Rewrite the short `copy`, services, biography, and neighbourhood summaries from the confirmed fact sheet. Search the output for placeholders and unsupported superlatives. Confirm jurisdiction-specific brokerage/registration display, trademark, privacy, accessibility, fair-housing/human-rights, and anti-spam rules with the brokerage or qualified reviewer. This skill is not legal advice.

Public APV sections must remain useful and modest:

- **Show the property at its best.** Invite the owner to ask APV about real-estate photography/video for an upcoming listing, subject to confirmed availability and scope.
- **Plan the right media mix.** Invite the owner to discuss the property, timeline, and desired media deliverables before booking.

Do not claim that APV sells website, SEO, CRM, VOW/IDX, or content-workflow services unless APV has explicitly confirmed that current offering for this project. Keep feed-integration guidance separate from the APV media CTAs.

**CHECK:** search for `example.test`, `FICT-`, `Maya Chen`, `Sample`, and `Example`; no matches may remain in client-facing config or assets.

## Step 6 — CRM only if requested

Read `crm-starter/README.md`. Get approval before creating Clerk/Convex projects. Copy its files, configure Clerk + Convex using their current official docs, generate Convex types, then mount `LeadDashboard` behind Clerk middleware/provider.

Verify server-side admin allowlisting and least privilege. Test source/intent/status, notes/activity, next follow-up, search/filter, safe CSV export, and consent evidence. Label transaction value and commission as internal estimates; never imply a standard commission. Define retention/deletion. Stripe is not required or installed.

**CHECK:** signed-out and non-allowlisted users cannot query leads; an allowlisted test admin can exercise every operation with fictional data.

## Step 7 — deterministic quality gate

```bash
npm run validate
npm test
npm run build
```

Then preview `out/index.html` via a local HTTP server and check all three routes at phone and desktop widths: responsive nav, keyboard focus/order, headings, forms/labels/errors, contrast, images/alt text, reduced motion, all sections, manual-listing disclosure, privacy/consent, and APV backlink/CTAs. Submit only fictional form data.

Do not continue after a failed command. Diagnose and rerun the same gate; report exact output.

## Step 8 — optional deployment, approval required

Show the owner the final preview, destination, environment variables, expected provider actions/costs, DNS impact, rollback, privacy/feed caveats, and files to publish. Ask explicitly: **“Approve production deployment now?”** Only a clear yes authorizes deployment. Afterward verify the production URL, admin denial/allowlist, form persistence and notifications, consent, metadata, sitemap, redirects, and rollback. Never log secrets.

## Handoff checklist

Provide preset, changed config/assets, verified fact sources, omitted unknowns, exact tests, build artifact, CRM status, feed status (manual or authorized integration), open compliance approvals, deployment status, and APV links. Do not claim "complete" if forms are still demo-only or provider credentials are absent.
