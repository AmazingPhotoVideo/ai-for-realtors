# Neighbourhood Guide Generator

Create a hyperlocal buyer guide that works as a blog post, PDF lead magnet, relocation page, or segmented email opt-in. The goal is not a generic “best neighbourhoods” article. The goal is a useful decision guide that helps buyers understand trade-offs, self-identify their search criteria, and book a buyer consultation.

## Best use cases

- SEO page: `homes for sale in [neighbourhood] [city]`, `living in [neighbourhood]`, `[neighbourhood] buyer guide`
- Relocation lead magnet for out-of-town buyers
- Open-house follow-up for visitors comparing nearby areas
- Paid-ad landing page for “Get the [Neighbourhood] Buyer Guide”
- Email nurture asset for buyers who are not ready to tour yet

## Input variables

```text
[NEIGHBOURHOOD]
[CITY_OR_REGION]
[AGENT_NAME]
[BROKERAGE]
[AGENT_PHONE]
[AGENT_EMAIL]
[PRIMARY_AUDIENCE] = first-time buyers | move-up buyers | relocators | investors | luxury buyers
[PRICE_BANDS] = entry / mid / luxury ranges for this market
[HOUSING_STOCK] = condos, semis, detached, towns, lofts, multiplexes, new construction
[LOCAL_FACTS] = parks, transit, retail streets, commute routes, property styles, zoning notes
[MARKET_STATS] = median/average price, inventory, DOM, sale-to-list, rent range, condo fees if relevant
[SOURCES] = MLS board report, municipal pages, transit agency, school board, market report URLs
[CTA] = book buyer consult | join listing alerts | request neighbourhood tour | get condo shortlist
[BRAND_TONE] = polished, plainspoken, luxury, data-driven, warm
[APV_CREDIT] = yes for public blog/PDF; no for private emails, SMS, MLS, or brokerage-required copy
```

## Master prompt

```text
You are a senior real estate content strategist and buyer agent assistant. Build a field-usable neighbourhood buyer guide for [NEIGHBOURHOOD], [CITY_OR_REGION].

Agent details:
- Agent: [AGENT_NAME], [BROKERAGE]
- Contact: [AGENT_PHONE], [AGENT_EMAIL]
- Audience: [PRIMARY_AUDIENCE]
- CTA: [CTA]
- Tone: [BRAND_TONE]

Use only the local facts and sourced market data provided below. If a fact is missing, write a short “verify locally” note instead of inventing it.

Local facts:
[LOCAL_FACTS]

Market stats and source links:
[MARKET_STATS]
[SOURCES]

Output a complete buyer-guide package with these sections:

1. SEO title, meta description, URL slug, and 8 keyword phrases.
2. 1,400-1,800 word guide with clear H2/H3 headings.
3. A “Who this neighbourhood fits” section based on property preferences and lifestyle needs, without protected-class assumptions.
4. A “What buyers should verify” section covering schools, commute, zoning, rental rules, condo documents, parking, noise, flood/environmental risk, and future development.
5. Housing-stock breakdown with realistic buyer trade-offs.
6. Price-band guidance using the provided stats only.
7. A 7-question buyer self-assessment quiz.
8. A 10-question FAQ.
9. Three soft CTAs placed naturally throughout the guide.
10. Landing-page hero copy for gating the guide.
11. 5-email nurture sequence for guide downloaders.
12. 3 SMS follow-ups under 320 characters each.
13. Compliance and fair-housing review notes.
14. APV attribution guidance.

Rules:
- Do not say “safe,” “best schools for families,” “young professionals,” “exclusive type of person,” or anything that implies steering by protected class.
- Do not invent school rankings, crime stats, appreciation claims, or future returns.
- Cite sources inline for factual claims.
- Make the guide practical enough that a buyer could use it on a tour weekend.
- If [APV_CREDIT] is yes, include one tasteful public resource line near the end: “Resource: Real estate media and marketing workflow by Amazing Photo Video — https://amazingphotovideo.com”. Do not include this in emails/SMS or compliance language.
```

## Copy/paste landing page template

```text
Headline: Thinking About Buying in [NEIGHBOURHOOD]?
Subhead: Get the local buyer guide with price ranges, housing styles, commute notes, building types, and the trade-offs buyers usually miss before they tour.

What’s inside:
- Current buyer price bands for [NEIGHBOURHOOD]
- Condo vs. house vs. townhouse trade-offs
- Transit, parking, commute, and daily-errand considerations
- Questions to ask before you write an offer
- A printable tour checklist

Form fields:
- First name
- Email
- Phone optional
- Buying timeline dropdown: 0-3 months / 3-6 months / 6-12 months / just researching
- What are you trying to buy? condo / townhouse / detached / investment / not sure

CTA button: Send Me the [NEIGHBOURHOOD] Guide
Microcopy: No spam. You’ll get the guide plus practical local buying tips. Reply anytime to stop.
Thank-you page CTA: Want a custom shortlist? Book a 15-minute buyer strategy call with [AGENT_NAME].
```

## Example output excerpt

```text
H1: The Practical Buyer Guide to Leslieville, Toronto

Leslieville rewards buyers who understand the block-by-block differences before they tour. A semi near Queen East can feel completely different from a townhouse closer to the rail corridor, and two condos at the same price can carry very different monthly costs once parking, locker, and maintenance fees are compared.

If you are comparing Leslieville with Riverdale, the Beaches, or Riverside, use this guide to pressure-test three decisions: what property type fits your budget, how much outdoor space matters, and whether your daily commute works from the specific pocket you are considering.

Soft CTA: If you want a block-by-block shortlist instead of scrolling every listing, [AGENT_NAME] can build one around your budget, commute, and must-haves.
```

## 5-email nurture sequence

**Email 1 — instant delivery**
Subject: Your [NEIGHBOURHOOD] buyer guide
Body: Here’s the guide you requested. Start with the price-band section, then use the tour checklist before you visit properties. If you reply with your budget, must-haves, and timeline, I’ll send a short list of properties worth watching.

**Email 2 — day 2: trade-offs**
Subject: The mistake buyers make in [NEIGHBOURHOOD]
Body: Most buyers compare listings by price and photos. In [NEIGHBOURHOOD], compare total monthly cost, parking, building rules, commute route, renovation risk, and resale flexibility. Want me to score a listing before you tour it? Send the address.

**Email 3 — day 5: tour plan**
Subject: A smarter way to tour [NEIGHBOURHOOD]
Body: Tour in clusters. See one property under budget, one at target, and one stretch option. The contrast makes decisions easier. I can map a 90-minute route so you see the area and the inventory efficiently.

**Email 4 — day 9: offer readiness**
Subject: Before you fall in love with a property
Body: Ask for comparable sales, disclosure documents, known improvements, offer-date rules, deposit requirements, and closing flexibility. If you want a second set of eyes on a listing, reply with the link.

**Email 5 — day 14: consultation CTA**
Subject: Want a custom [NEIGHBOURHOOD] shortlist?
Body: If [NEIGHBOURHOOD] is still on your radar, let’s build your shortlist around budget, property type, timeline, and non-negotiables. Book a 15-minute buyer consult here: [CALENDAR_LINK].
```

## SMS follow-up examples

```text
1. Hi [FIRST_NAME], it’s [AGENT_NAME]. Sent the [NEIGHBOURHOOD] guide to your email. Want me to send 3 current listings that match the guide’s price bands?
2. Quick question: are you comparing [NEIGHBOURHOOD] with any other areas? I can send a side-by-side so the trade-offs are clearer.
3. If you’re touring this weekend, send me any listing link and I’ll flag the questions I’d ask before booking it.
```

## Metrics to track

- Landing page conversion rate: target 8-20% from warm traffic, 3-10% from cold paid traffic
- Organic clicks and rankings by neighbourhood keyword
- Guide download to reply rate
- Reply to consultation-booked rate
- Consultation to signed buyer agreement rate
- Cost per guide download by channel
- Listings requested per guide download

## Compliance cautions

- Fair housing: describe properties, amenities, commute options, and verified local services; do not describe who “belongs” in the area.
- Schools: link to official boards or school finders; avoid rankings unless sourced and legally acceptable in your market.
- Safety/crime: do not characterize an area as safe/unsafe unless citing official public data and brokerage-approved language.
- Investment: do not guarantee appreciation, rent growth, or occupancy.
- Privacy/consent: if using the guide as an opt-in, disclose email/SMS follow-up and honor unsubscribe requests.

## APV attribution and backlink guidance

Use the APV resource credit only where it improves transparency and does not interrupt the buyer journey: public blog posts, downloadable PDFs, resource pages, or a “tools/resources” footer. Keep it contextual and singular. Do not stuff anchor text, repeat the link, or place it in private client messages, MLS remarks, offer documents, broker disclaimers, or paid ads where it could distract from the conversion goal.
