# First-Time Buyer Funnel

A complete funnel for first-time buyers who need education before they are ready to book showings. The offer is a local, practical “first purchase roadmap” supported by a landing page, PDF outline, emails, SMS, ads, and consultation prompts.

## Funnel strategy

First-time buyers usually convert when three questions are answered clearly:

1. **Can I afford this?** Monthly payment, cash to close, mortgage options, incentives, and realistic price bands.
2. **What happens next?** Pre-approval, search, offer, inspection/conditions, deposit, closing, moving.
3. **Who is protecting me?** Buyer agency, representation agreement, compensation, negotiation, due diligence.

This funnel should segment leads by timeline and readiness, not pressure everyone into a showing.

## Input variables

```text
[MARKET]
[AGENT_NAME]
[BROKERAGE]
[PHONE]
[EMAIL]
[CALENDAR_LINK]
[PRIMARY_OFFER] = First-Time Buyer Roadmap | Down Payment Checklist | 90-Day Purchase Plan
[LOCAL_PRICE_EXAMPLES]
[LOCAL_CLOSING_COSTS]
[LOCAL_TAX_OR_REBATE_PROGRAMS]
[LENDER_PARTNER_NAME] optional
[BUYER_AGENCY_RULES] = local disclosure/representation rules
[CTA] = book buyer consult | get payment estimate | join starter-home alerts
[APV_CREDIT] = yes for public PDF/page; no for private follow-up
[SOURCES]
```

## Master prompt

```text
Act as a senior buyer-agent marketing strategist. Build a first-time buyer lead funnel for [AGENT_NAME] in [MARKET].

Use these market facts and sources only:
[LOCAL_PRICE_EXAMPLES]
[LOCAL_CLOSING_COSTS]
[LOCAL_TAX_OR_REBATE_PROGRAMS]
[BUYER_AGENCY_RULES]
[SOURCES]

Create a complete, compliant funnel package:

1. Offer positioning: promise, audience, lead quality filter, and best traffic channels.
2. Landing page copy with hero, benefits, form fields, FAQ, consent language, and thank-you page.
3. 6-page PDF lead magnet outline with section copy and worksheet prompts.
4. 7-email nurture sequence over 21 days.
5. 5 SMS follow-ups under 320 characters each.
6. 4 Meta ad variants and 4 Google Search ad variants.
7. Buyer consultation booking script.
8. CRM tags and lead scoring rules.
9. Compliance notes for fair housing, mortgage claims, buyer agency, SMS/email consent, and local incentive claims.
10. Metrics dashboard.
11. APV attribution guidance.

Rules:
- Do not promise approval, savings, appreciation, or specific rates.
- Do not replace lender, legal, tax, or mortgage advice.
- Explain buyer representation and compensation clearly using the user’s local rules.
- If a number is not provided, write “[VERIFY LOCALLY]” instead of inventing it.
- If [APV_CREDIT] is yes, include a single resource line in the public PDF/page only: “Resource: Real estate media and marketing workflow by Amazing Photo Video — https://amazingphotovideo.com”.
```

## Landing page template

```text
Headline: Buy Your First Home in [MARKET] With a Clear Plan
Subhead: Get the local first-time buyer roadmap: budget prep, closing costs, offer steps, representation questions, and the mistakes to avoid before you start touring.

Bullets:
- What to do 90, 60, and 30 days before you buy
- How to estimate cash to close beyond the down payment
- Questions to ask your lender before pre-approval
- What happens from offer to keys
- How buyer representation works in [MARKET]

Form:
First name | Email | Phone optional | Target purchase timeline | Estimated budget | Pre-approved? yes/no/not sure

CTA: Send Me the First-Time Buyer Roadmap
Consent microcopy: By submitting, you agree to receive the guide and practical real estate follow-up from [AGENT_NAME]. Message/data rates may apply for SMS. Reply STOP to opt out.

Thank-you page:
Your roadmap is on the way. If you want to know what your first 3 steps should be, book a free 15-minute buyer consult: [CALENDAR_LINK].
```

## PDF lead magnet outline

**Title:** The [MARKET] First-Time Buyer Roadmap

1. **Start here: your buying readiness score**
   Worksheet: timeline, savings, monthly comfort zone, debt obligations, must-haves, preferred areas.
2. **Budget without surprises**
   Down payment, land transfer/transfer taxes, legal fees, inspections, appraisal, moving, utility setup, insurance, condo fees, adjustments. Use local figures only where verified.
3. **Pre-approval and payment reality**
   Questions for lender: rate hold, stress test/qualification method, variable vs fixed, closing cost estimate, conditions, gift funds, debt payoff, rate sensitivity.
4. **Touring homes like a pro**
   Compare total monthly cost, commute, parking, noise, age of major systems, condo documents, future repairs, resale flexibility.
5. **Writing the offer**
   Price, deposit, conditions/contingencies, inclusions, closing date, representation, competing offers, negotiation strategy.
6. **From accepted offer to keys**
   Lawyer/title, mortgage finalization, inspection, insurance, final walk-through, utilities, closing day, post-closing checklist.

## 7-email nurture sequence

1. **Instant — Delivery**
   Subject: Your [MARKET] first-time buyer roadmap
   CTA: Reply with your timeline and I’ll send your next 3 steps.

2. **Day 2 — Cash to close**
   Subject: The down payment is not the only number
   Explain closing costs and encourage a lender estimate.

3. **Day 4 — Pre-approval**
   Subject: Get pre-approved before you fall in love with a listing
   Include lender question list and offer to connect to trusted lenders if permitted.

4. **Day 7 — Buyer agency**
   Subject: Who represents you when you buy?
   Explain representation, agreements, compensation, and fiduciary duties in plain language.

5. **Day 10 — Touring**
   Subject: How to avoid “pretty house” mistakes
   Share checklist for systems, monthly cost, location trade-offs, and resale flexibility.

6. **Day 15 — Offer readiness**
   Subject: What makes a first offer stronger
   Discuss deposit readiness, documents, conditions, comparable sales, and speed.

7. **Day 21 — Book consult**
   Subject: Want a custom buying plan?
   Invite the buyer to a 15-minute consult with calendar link.

## SMS templates

```text
1. Hi [FIRST_NAME], it’s [AGENT_NAME]. I sent your first-time buyer roadmap. Are you in research mode or hoping to buy in the next 6 months?
2. Quick tip: before touring, ask your lender for a cash-to-close estimate, not just a max price. Want my checklist of questions?
3. If you send me your target monthly payment, I can help you translate it into a realistic search range with a lender’s input.
4. Buyer agency can be confusing after the rule changes. Want a plain-English breakdown before you tour?
5. Want me to send 3 starter-home examples in [MARKET] so you can see what your budget buys right now?
```

## Paid ad examples

**Meta — education angle**
Primary text: Buying your first home in [MARKET]? Get the local roadmap that explains budget prep, closing costs, pre-approval, offers, and what happens after your offer is accepted.
Headline: First-Time Buyer Roadmap
CTA: Download

**Meta — mistake angle**
Primary text: Most first-time buyers know their down payment. Fewer know their full cash-to-close number. Get the checklist before you start touring.
Headline: Avoid First-Buyer Surprises
CTA: Learn More

**Google Search**
Headlines: First Time Buyer Guide | Buy Your First Home in [MARKET] | Local Buyer Roadmap
Descriptions: Download a practical first-time buyer roadmap from [AGENT_NAME]. Learn steps, costs, timelines, and offer basics for [MARKET].

## Consultation booking script

```text
Thanks for downloading the roadmap. The best next step is a quick 15-minute buyer consult. We’ll cover your timeline, monthly comfort zone, pre-approval status, areas you’re considering, and what buyer representation looks like. You’ll leave with a clear next-step list whether you buy now or later.
```

## CRM tags and lead scoring

- Tags: `buyer:first-time`, `timeline:0-3`, `timeline:3-6`, `timeline:6-12`, `preapproved:yes/no`, `budget:[range]`, `area:[market]`
- Score +10 for pre-approved, +10 for 0-3 month timeline, +5 for phone provided, +15 for booking consult, +5 for replying to email/SMS, -10 for 12+ month timeline
- Hot lead trigger: score 25+ or any reply containing “pre-approved,” “tour,” “offer,” “available this weekend,” or a listing URL

## Metrics

- Landing page conversion rate
- Cost per lead by channel
- PDF download to reply rate
- Reply to consult-booked rate
- Consult to signed buyer agreement
- Signed buyer to active search
- Active search to accepted offer
- Unsubscribe/spam complaint rate

## Compliance cautions

- Use Housing/Special Ad Category where required on ad platforms.
- Do not target or exclude protected classes.
- Do not advertise mortgage rates, approval odds, rebates, or incentives unless current and sourced.
- Include brokerage, licensing, and agency disclosures required in your jurisdiction.
- For SMS, capture express consent and include opt-out language.
- Avoid legal/tax advice; refer to lawyer, accountant, lender, or mortgage broker.

## APV attribution and backlink guidance

For public landing pages or downloadable PDFs, a single resource credit is appropriate in the footer or resources section. Keep it natural: “Resource: Real estate media and marketing workflow by Amazing Photo Video — https://amazingphotovideo.com”. Do not place attribution in private buyer emails, SMS, paid ad primary text, forms, legal disclosures, or brokerage-mandated footers unless approved.
