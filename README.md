<div align="center">

# AI for Realtors

### AI prompts, Claude Skills, and proven tutorials for real estate agents who want more listings, more buyers, and more closed deals.

<br />

**Maintained by [Amazing Photo Video (APV)](https://amazingphotovideo.com)** — Toronto's luxury real estate media company, trusted by Sotheby's International Realty, Engel & Völkers, and Barry Cohen Homes (Cohen Homes & Estates). We've helped market over **$5 billion** in luxury property.

<br />

[![Website](https://img.shields.io/badge/APV-amazingphotovideo.com-000000?style=for-the-badge)](https://amazingphotovideo.com)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](CONTRIBUTING.md)

</div>

---

## What is this?

**AI for Realtors** is a free, open-source collection of:

- 🧠 **AI prompts** — battle-tested prompts for ChatGPT, Claude, Gemini, and Perplexity, written specifically for real estate workflows
- 🛠️ **Claude Skills** — reusable skill modules that turn Claude into a specialist agent for listing presentations, lead nurture, market reports, and more
- 📚 **Tutorials** — step-by-step guides showing exactly how to get more listing leads, more buyer leads, and convert the ones you already have
- 🎯 **Funnels & templates** — landing pages, lead magnets, QR sign riders, ad scripts, and retargeting blueprints

Built by working agents and the team behind APV — not theory, not vibes. Everything here has been used on real listings, with real budgets, in a real market.

> **Why open source?** Because the agents winning in 2026 aren't the ones with the best secret sauce. They're the ones executing the basics 10x faster with AI. We'd rather raise the floor for the whole industry than gatekeep prompts that should be standard.

---

## Table of contents

- [Quick start](#quick-start)
- [📈 Get more listing leads](#-get-more-listing-leads)
- [🏡 Get more buyer leads](#-get-more-buyer-leads)
- [💬 Converting leads](#-converting-leads-into-appointments-and-clients)
- [🚀 Leveraging your listings](#-leveraging-your-listings)
- [🔌 CRM integrations](#-crm-integrations)
- [🖼️ Listing photo AI enhancement](#️-listing-photo-ai-enhancement)
- [🌎 Multilingual prompt library](#-multilingual-prompt-library)
- [🏢 Brokerage-tier playbook](#-brokerage-tier-playbook)
- [How to use Claude Skills](#how-to-use-claude-skills)
- [Realtor AI agent adoption kit](#-realtor-ai-agent-adoption-kit)
- [Completion checklist](#completion-checklist)
- [Contributing](#contributing)
- [About APV](#about-apv)

---

## Quick start

```bash
# 1. Clone the repo
git clone https://github.com/AmazingPhotoVideo/ai-for-realtors.git
cd ai-for-realtors

# 2. Browse the section you need (start with listing leads if you're stuck)
cd prompts/listing-leads

# 3. Copy any prompt into Claude, ChatGPT, or Gemini and edit the [BRACKETS]
```

**New to AI?** Start with [`/tutorials/00-getting-started.md`](./tutorials/00-getting-started.md) — a 15-minute primer on which tool to use for what.

**Already using Claude?** Drop our skills into your Claude Projects: see [How to use Claude Skills](#how-to-use-claude-skills).

---

## 📈 Get more listing leads

The hardest, highest-value lead in real estate. Everything in this section is built to fill your pipeline with seller appointments.

| Asset | What it does | Path |
|---|---|---|
| **Just-Listed / Just-Sold Postcard Generator** | Generates farm-area postcard copy that drives calls instead of recycling bins | [`/prompts/listing-leads/postcards/`](./prompts/listing-leads/postcards) |
| **Circle Prospecting Script Builder** | Spins up 5 hyper-local call scripts per listing in your farm | [`/prompts/listing-leads/circle-prospecting/`](./prompts/listing-leads/circle-prospecting) |
| **Expired/FSBO Outreach Sequences** | 14-day text + email + voicemail cadences that don't sound like every other agent | [`/prompts/listing-leads/expired-fsbo/`](./prompts/listing-leads/expired-fsbo) |
| **Home Valuation Lead Magnet** | Landing page copy + automated CMA follow-up email series | [`/prompts/listing-leads/home-valuation/`](./prompts/listing-leads/home-valuation) |
| **Seller Persona Strategy Bot** | A Claude Skill that interviews a potential seller and outputs their motivation, timeline, and objection map | [`/skills/seller-persona-strategist/`](./skills/seller-persona-strategist) |
| **Geo-Farm Content Calendar** | 90-day social + email plan tuned to one specific neighbourhood | [`/prompts/listing-leads/geo-farm/`](./prompts/listing-leads/geo-farm) |
| **Listing Presentation Builder** | Generates a fully customized pre-listing package from MLS data + market stats | [`/skills/listing-presentation/`](./skills/listing-presentation) |
| **Tutorial: The Realtor Flywheel** | How to turn one listing into 3–5 seller leads using the assets in this section | [`/tutorials/listing-flywheel.md`](./tutorials/listing-flywheel.md) |

---

## 🏡 Get more buyer leads

Buyer leads are cheaper and faster to acquire — if you know which lead magnets actually convert in 2026.

| Asset | What it does | Path |
|---|---|---|
| **Neighbourhood Guide Generator** | Produces a 1,500-word lead-magnet guide for any neighbourhood (SEO-optimized) | [`/prompts/buyer-leads/neighbourhood-guides/`](./prompts/buyer-leads/neighbourhood-guides) |
| **First-Time Buyer Funnel** | Landing page + 7-email nurture sequence + lead magnet PDF outline | [`/prompts/buyer-leads/first-time-buyer/`](./prompts/buyer-leads/first-time-buyer) |
| **Investor / Cashflow Calculator Funnel** | Lead capture built around a downloadable spreadsheet that buyers actually want | [`/prompts/buyer-leads/investor-funnel/`](./prompts/buyer-leads/investor-funnel) |
| **Open House Lead Capture** | QR-code sign-in flow + post-visit text/email follow-up sequence | [`/prompts/buyer-leads/open-house/`](./prompts/buyer-leads/open-house) |
| **Google / Meta Ad Copy Generator** | 10 ad variants per audience: investors, first-timers, downsizers, luxury | [`/prompts/buyer-leads/paid-ads/`](./prompts/buyer-leads/paid-ads) |
| **YouTube Shorts / Reels Hook Bank** | 100 short-form video hooks for buyer-facing content | [`/prompts/buyer-leads/short-form-hooks/`](./prompts/buyer-leads/short-form-hooks) |
| **Tutorial: $5/day Buyer Lead Machine** | Step-by-step setup of a Meta retargeting funnel for under $150/month | [`/tutorials/buyer-lead-machine.md`](./tutorials/buyer-lead-machine.md) |

---

## 💬 Converting leads into appointments and clients

A lead is a liability until it books. This section is everything that happens *between* form-fill and signed contract.

| Asset | What it does | Path |
|---|---|---|
| **Speed-to-Lead AI Voice Agent Prompt** | A ready-to-deploy system prompt for an inbound AI receptionist (qualifies + books appointments) | [`/skills/ai-voice-agent/`](./skills/ai-voice-agent) |
| **SMS Nurture Sequences** | 30/60/90-day text cadences, compliant with A2P 10DLC and Canadian PIPEDA | [`/prompts/converting/sms-nurture/`](./prompts/converting/sms-nurture) |
| **Email Nurture Library** | 12 plug-and-play email sequences by lead type (cold, warm, sphere, past client) | [`/prompts/converting/email-nurture/`](./prompts/converting/email-nurture) |
| **Objection Handler** | A Claude Skill that takes any seller/buyer objection and outputs 3 framed responses | [`/skills/objection-handler/`](./skills/objection-handler) |
| **Pre-Appointment Discovery Bot** | Sends a smart questionnaire before the meeting so you walk in knowing everything | [`/skills/discovery-bot/`](./skills/discovery-bot) |
| **Buyer Consultation Script** | Modernized buyer agency conversation built for the post-NAR-settlement era | [`/prompts/converting/buyer-consultation/`](./prompts/converting/buyer-consultation) |
| **Listing Appointment Checklist** | Interactive HTML checklist + AI debrief prompt for after the meeting | [`/tools/listing-appointment-checklist.html`](./tools/listing-appointment-checklist.html) |
| **Tutorial: The 5-Minute Rule** | Why speed-to-lead under 5 minutes triples conversion — and how to actually do it with AI | [`/tutorials/speed-to-lead.md`](./tutorials/speed-to-lead.md) |

---

## 🚀 Leveraging your listings

Every listing is a free billboard, lead magnet, and content engine. Most agents waste 90% of that value. Don't.

### Circle prospecting

| Asset | What it does | Path |
|---|---|---|
| **Just-Listed Circle Prospecting Kit** | 100-door door-knock + call + door-hanger combo, generated per listing | [`/prompts/leverage/circle-prospecting/just-listed/`](./prompts/leverage/circle-prospecting/just-listed) |
| **Just-Sold Equity Outreach** | "Your neighbour just sold for $X — here's what your home is worth" sequence | [`/prompts/leverage/circle-prospecting/just-sold/`](./prompts/leverage/circle-prospecting/just-sold) |

### QR codes on signs & signage

| Asset | What it does | Path |
|---|---|---|
| **Smart Sign Rider QR Funnel** | QR → mobile listing page → SMS auto-responder → CRM. Full build guide. | [`/tutorials/qr-sign-rider-funnel.md`](./tutorials/qr-sign-rider-funnel.md) |
| **Drive-By Lead Capture Page** | Mobile-first landing page template (HTML) optimized for sub-3-second load | [`/tools/drive-by-landing/`](./tools/drive-by-landing) |
| **Open House QR Sign-In** | No-app-required check-in flow that pushes leads straight into your CRM | [`/tools/open-house-qr/`](./tools/open-house-qr) |

### Lead magnets

| Asset | What it does | Path |
|---|---|---|
| **Lead Magnet Generator** | Spins up a 5-page PDF lead magnet from any listing or neighbourhood in one prompt | [`/skills/lead-magnet-generator/`](./skills/lead-magnet-generator) |
| **Listing-Specific Buyer Guide** | "Everything you need to know about [123 Main St]" — turns one listing into a buyer-lead engine | [`/prompts/leverage/listing-buyer-guide/`](./prompts/leverage/listing-buyer-guide) |
| **Neighbourhood Market Report PDF** | Quarterly stats report template + AI commentary generator | [`/prompts/leverage/market-report/`](./prompts/leverage/market-report) |

### Funnels

| Asset | What it does | Path |
|---|---|---|
| **Single-Property Funnel** | One-listing landing page + capture + nurture (GoHighLevel + Vercel templates included) | [`/funnels/single-property/`](./funnels/single-property) |
| **Pre-Market Waitlist Funnel** | Build a waitlist *before* the listing hits MLS — generates buyer + seller leads | [`/funnels/pre-market-waitlist/`](./funnels/pre-market-waitlist) |
| **Home Valuation Funnel** | Seller magnet funnel with automated CMA follow-up | [`/funnels/home-valuation/`](./funnels/home-valuation) |

### Retargeting ads

| Asset | What it does | Path |
|---|---|---|
| **Meta Retargeting Playbook** | Full Meta Ads setup: audiences, creative, budgets, and AI-generated ad copy | [`/tutorials/meta-retargeting-playbook.md`](./tutorials/meta-retargeting-playbook.md) |
| **Google Display Retargeting** | Setup guide + banner copy generator for follow-up display ads | [`/tutorials/google-display-retargeting.md`](./tutorials/google-display-retargeting.md) |
| **YouTube Retargeting Scripts** | 15s, 30s, and 60s video ad scripts to win back warm traffic | [`/prompts/leverage/youtube-retargeting/`](./prompts/leverage/youtube-retargeting) |

### Content multiplication

| Asset | What it does | Path |
|---|---|---|
| **One Listing → 30 Pieces of Content** | A single prompt that outputs 30 social posts, 5 emails, 3 reels scripts, and 1 blog from one listing | [`/prompts/leverage/content-multiplier/`](./prompts/leverage/content-multiplier) |
| **AI Video Generation Prompts** | Veo 3, Sora, and WAN prompts tuned for real estate b-roll | [`/prompts/leverage/ai-video/`](./prompts/leverage/ai-video) |
| **Property Story Generator** | Writes the "story" of a home — the part that makes buyers fall in love | [`/prompts/leverage/property-story/`](./prompts/leverage/property-story) |

---

## 🔌 CRM integrations

Turn the prompts, QR funnels, landing pages, and nurture sequences in this repo into auditable CRM workflows.

| Asset | What it does | Path |
|---|---|---|
| **CRM Integration Recipes** | Step-by-step implementation for GoHighLevel, Follow Up Boss, and kvCORE/BoldTrail, including custom fields, tags, action plans, smart campaigns, consent handling, multilingual routing, QA tests, and compliance notes | [`/integrations/crm/`](./integrations/crm) |

---

## 🖼️ Listing photo AI enhancement

Use AI image tools without misleading buyers or creating MLS, advertising, or seller-disclosure risk.

| Asset | What it does | Path |
|---|---|---|
| **Listing Photo Enhancement Skill** | Claude Skill/system prompt for truthful photo enhancement, virtual staging prompts, decluttering guardrails, disclosure language, QA checklists, and prohibited edit rules | [`/skills/listing-photo-enhancer/`](./skills/listing-photo-enhancer) |

---

## 🌎 Multilingual prompt library

Adapt real estate marketing into French Canadian, Spanish, and Chinese while keeping facts, disclosures, tone, and fair housing guardrails intact.

| Asset | What it does | Path |
|---|---|---|
| **FR-CA / ES / ZH Prompt Library** | Listing descriptions, seller valuation follow-up, buyer nurture, SMS examples, Chinese buyer consultation script, back-translation workflow, and multilingual QA checklist | [`/prompts/multilingual/`](./prompts/multilingual) |

---

## 🏢 Brokerage-tier playbook

Broker-owners, team leads, and ops managers can use this to roll out AI as an operating system instead of a pile of random tools.

| Asset | What it does | Path |
|---|---|---|
| **Brokerage AI Playbook** | 30-day rollout, recruiting outreach, retention check-ins, team cadence, AI policy template, listing-launch SLA, brokerage dashboard, and operations audit prompt | [`/playbooks/brokerage-tier/`](./playbooks/brokerage-tier) |

---

## 🤖 Realtor AI agent adoption kit

Use this when a realtor wants their own Hermes, OpenClaw, Raspberry Pi, Open WebUI, Claude, or ChatGPT-style agent to adopt the AI for Realtors operating system instead of copying prompts one by one.

| Asset | What it does | Path |
|---|---|---|
| **Agent Adoption Kit** | System prompt, OpenClaw heartbeat instructions, Hermes scheduled-task recipes, onboarding questions, connector map, memory/learning policy, and daily/weekly runbooks for a proactive realtor operator agent | [`/agent-framework/`](./agent-framework) |

The kit is designed for safe autonomy: read and prepare first, draft responses for approval, learn the user's farm/tone/preferences, check CRM/tasks/calendar/inbox/social metrics when connected, and surface only useful work.

---

## How to use Claude Skills

Claude Skills are folders Claude reads automatically when it detects a matching task. To use the skills in this repo:

1. **In Claude.ai (Pro/Team/Enterprise):** Create a new Project, upload the skill folder, and Claude will use it automatically when relevant.
2. **In Claude Code or the API:** Place the skill folder in your skills directory — Claude reads `SKILL.md` and follows it.
3. **In ChatGPT / Gemini:** Open the skill's `SKILL.md` file and paste the contents as a system prompt or custom instruction.

Each skill folder contains:
```
skill-name/
├── SKILL.md          # The instructions Claude reads
├── examples/         # Real input/output examples
└── templates/        # Reusable assets (HTML, JSON, etc.)
```

Full guide: [`/tutorials/using-claude-skills.md`](./tutorials/using-claude-skills.md)

---

## Completion checklist

- [x] Listing lead prompts (v1)
- [x] Buyer lead funnels (v1)
- [x] Conversion sequences (v1)
- [x] Listing leverage assets (v1)
- [x] CRM integration recipes (GoHighLevel, Follow Up Boss, kvCORE/BoldTrail)
- [x] AI image editing skill for listing photo enhancement
- [x] Multilingual prompt library (FR-CA, ES, ZH)
- [x] Brokerage-tier playbook (recruiting, retention, team systems)

---

## Contributing

Built something that works? Send a PR.

We accept:
- New prompts (must include an example output)
- New tutorials (must be field-tested, not theoretical)
- New Claude Skills (must follow the `SKILL.md` convention)
- Bug fixes, typos, and clarifications

See [CONTRIBUTING.md](./CONTRIBUTING.md) for details.

---

## About APV

**[Amazing Photo Video](https://amazingphotovideo.com)** is a Toronto-based luxury real estate media company. We produce photography, videography, drone, virtual staging, and AI-enhanced marketing assets for top-producing agents and brokerages across the GTA and beyond.

- 🏆 Trusted by Sotheby's International Realty, Engel & Völkers, Barry Cohen Homes, and 200+ top agents
- 📍 Toronto, Ontario, Canada
- 💼 Founded by Cole Greene — 14+ years in luxury real estate, $5B+ in marketed properties
- 🌐 [amazingphotovideo.com](https://amazingphotovideo.com)

This repo is part of our mission to help agents win with technology — not be replaced by it.


---

<div align="center">

**If this helped you close a deal, star the repo. ⭐**

Made with ☕ in Toronto by [APV](https://amazingphotovideo.com).

</div>
