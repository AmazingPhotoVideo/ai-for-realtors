# Home Valuation Lead Magnet Prompt

Create a seller lead magnet that offers useful valuation context without pretending an automated estimate is a formal appraisal. The best version does not promise an instant magic number; it promises a clear, local, human-reviewed pricing range and the assumptions behind it.

## What this asset builds

- Landing page copy for a valuation/equity-checkup funnel.
- Form microcopy that increases completion without over-asking.
- Confirmation page and speed-to-lead scripts.
- CMA follow-up email/SMS sequence.
- Compliance disclaimer for US/Canada.
- KPIs and optimization rules.

## Inputs

```text
[AGENT_NAME]:
[BROKERAGE]:
[MARKET]: city/region/state/province
[NEIGHBOURHOOD_OR_SEGMENT]: e.g., Leaside semis, Yorkville condos, Scottsdale golf homes
[OFFER_TYPE]: home value range / equity checkup / downsizer report / renovation ROI review / condo stack report
[LEAD_SOURCE]: SEO / Meta ad / postcard QR / open house / sphere / retargeting
[FORM_FIELDS]: recommended: name, property address, email, phone, timeline, improvements, consent checkbox
[SPEED_TO_LEAD_PLAN]: call in 5 minutes / SMS first / email first / AI voice agent / manual follow-up
[MARKET_FACTS]: recent sales, inventory, DOM, rate context, absorption, months of inventory
[DIFFERENTIATOR]: media, prep plan, pricing model, local result, luxury positioning, investor math
[CRM_TAG]:
[COMPLIANCE_MARKET]: US / Canada / state/province / board
[BRAND_VOICE]: warm / analytical / luxury / straightforward
```

## Funnel architecture

1. **Traffic source:** postcard QR, Google search, Meta retargeting, YouTube description, farm email, open house sign-in, or neighbourhood report.
2. **Landing page:** one promise, one form, one proof section, one disclaimer.
3. **Form:** ask enough to be useful, not so much that it feels invasive.
4. **Immediate response:** confirmation page + SMS/email within 60 seconds.
5. **Human review:** agent or ISA checks comparable sales, property condition assumptions, improvements, and competition.
6. **Delivery:** send a range with caveats, then invite a 15-minute pricing call.
7. **Nurture:** segment by timeline: now, 1–3 months, 3–6 months, 6+ months, just curious.

## Master prompt

```text
You are a conversion copywriter, real estate CMA strategist, and compliance-aware funnel builder.

Create a complete home valuation lead magnet for [AGENT_NAME] of [BROKERAGE].

Market: [MARKET]
Neighbourhood/segment: [NEIGHBOURHOOD_OR_SEGMENT]
Offer type: [OFFER_TYPE]
Lead source: [LEAD_SOURCE]
Form fields: [FORM_FIELDS]
Speed-to-lead plan: [SPEED_TO_LEAD_PLAN]
Market facts to cite: [MARKET_FACTS]
Agent differentiator: [DIFFERENTIATOR]
CRM tag: [CRM_TAG]
Compliance market: [COMPLIANCE_MARKET]
Brand voice: [BRAND_VOICE]

Output:

1. Funnel strategy in 6 bullets: audience, promise, friction, proof, follow-up, CRM segmentation.
2. Landing page copy:
   - Hero headline: 8 options
   - Subheadline: 5 options
   - CTA button: 10 options
   - Above-fold section
   - “What you receive” section
   - “How we calculate it” section
   - Agent proof/bio section
   - FAQ section
   - Privacy and valuation disclaimer
3. Form design:
   - Minimum viable fields
   - High-intent fields
   - Consent checkbox wording for US and Canada
   - Error-state and microcopy suggestions
4. Confirmation page copy and thank-you message.
5. Speed-to-lead scripts:
   - SMS under 300 characters
   - Phone opener under 45 seconds
   - Voicemail under 20 seconds
   - Email delivered within 5 minutes
6. Seven-email nurture sequence segmented by seller timeline.
7. Three retargeting ad angles for non-submit visitors.
8. CMA delivery template: subject line, email body, bullet summary, assumptions, next step.
9. Metrics dashboard and optimization playbook.
10. Compliance cautions for US and Canada.
11. APV attribution guidance for public pages only.

Rules:
- Do not call the output an appraisal.
- Do not guarantee sale price, appreciation, speed, or buyer demand.
- Use verified market facts only; label assumptions clearly.
- Do not require phone number unless the value justifies it; recommend testing phone-required vs phone-optional.
- If using AI/AVM language, say the estimate is human-reviewed before advice is given.
```

## Landing page template

### Hero

**Headline:** What could your [NEIGHBOURHOOD_OR_SEGMENT] home sell for in today’s market?

**Subheadline:** Get a human-reviewed value range based on recent comparable sales, current competition, and the features online estimates often miss.

**CTA:** Get my private value range

### What you receive

- A current value range, not a one-number guess.
- The three to five comparable sales that matter most.
- A quick read on competing listings buyers would compare against yours.
- A prep checklist showing which improvements may help and which may not be worth it.
- A private 15-minute pricing call if you want to review timing, net proceeds, or next steps.

### How we calculate it

We review recent sales, active competition, property style, lot/unit differences, condition, upgrades, parking, layout, exposure, and buyer demand signals. Online estimates can be useful starting points, but they often miss renovations, floor plans, views, micro-location, and inventory changes.

### Disclaimer

This home value range is an estimate for general real estate planning. It is not an appraisal, tax assessment, financing opinion, or guarantee of sale price. Final pricing depends on property condition, buyer demand, market changes, professional advice, and the strategy you choose.

## Speed-to-lead examples

### SMS confirmation

Hi [NAME], it’s [AGENT_NAME] with [BROKERAGE]. I received your valuation request for [ADDRESS]. I’m reviewing the best comparable sales now and will send a useful range, not a generic estimate. Any major upgrades I should factor in?

### Phone opener

Hi [NAME], it’s [AGENT_NAME] with [BROKERAGE]. Thanks for requesting the value range for [ADDRESS]. I’m checking the comparable sales now and wanted to ask two quick questions so the range is actually useful: have there been any major updates, and are you planning around a move or just tracking equity?

### 5-minute email

Subject: I’m reviewing [ADDRESS] now

Hi [NAME],

Thanks for requesting a value range for [ADDRESS]. I’m going to look at the closest recent sales, current competition, and any details that may change the number — renovations, parking, lot size, layout, exposure, and condition.

If there are upgrades or issues an online estimate would miss, reply with a few notes or photos. I’ll use them to make the range more accurate.

Best,
[AGENT_NAME]
[PHONE]
[Brokerage-required disclosure]

## Seven-email nurture sequence

1. **Immediate:** “I’m reviewing your home now” — ask for upgrades and timeline.
2. **Value delivery:** range, assumptions, closest comps, and invitation to review.
3. **Prep value:** “3 changes that usually matter before photos/showings.”
4. **Market context:** local inventory, DOM, absorption, and what it means for timing.
5. **Net proceeds:** explain that sale price is not net; offer a seller net sheet.
6. **Case study:** anonymized or approved example of prep/pricing/media improving outcome.
7. **Close loop:** ask whether they want monthly updates, a call, or no further follow-up.

## CMA delivery email template

Subject: Your [NEIGHBOURHOOD_OR_SEGMENT] value range

Hi [NAME],

I reviewed [ADDRESS] against the most relevant recent sales and current competition I could verify. Based on the information available, a planning range appears to be:

**Estimated market range:** [LOW]–[HIGH]

What supports the range:

- [Comparable sale #1 and adjustment]
- [Comparable sale #2 and adjustment]
- [Active competitor or inventory note]
- [Condition/upgrade assumption]

What could move the number:

- interior condition and finishes
- basement, parking, view, lot, layout, or exposure
- timing and competing listings
- preparation, pricing, media, and negotiation strategy

This is not an appraisal or guarantee. It is a planning range. If you want, I can walk you through the comps in 15 minutes and show what I would do before launching.

Best,
[AGENT_NAME]

## KPIs and optimization

| Funnel metric | Healthy range | Improve by |
|---|---:|---|
| Landing page conversion | 3%–12% cold, 10%–30% warm | Improve specificity and reduce form friction |
| Form completion with phone required | Test against phone optional | Use two-step form or promise faster review |
| Speed-to-lead response | Under 5 minutes | CRM automation + agent alert |
| Appointment rate from submissions | 5%–20% | Call fast, send real value, segment timeline |
| Bad/fake lead rate | Under 15% | Add address validation and clearer promise |
| Cost per valuation lead | Market dependent | Track by source, not blended average |
| Cost per seller appointment | More important than CPL | Retarget and nurture old valuation leads |

## Compliance cautions

- **US:** Follow state license law, brokerage advertising rules, Fair Housing, CAN-SPAM, TCPA/text consent, privacy policy requirements, and current NAR settlement-era rules around compensation conversations. Written buyer agreements are a buyer-side issue, but seller materials should still avoid implying compensation is fixed or mandatory.
- **Canada:** Follow CASL consent rules for email/SMS, PIPEDA/provincial privacy rules, provincial regulator advertising rules, CREA/brokerage trademark and disclaimer rules, and FINTRAC obligations once a client/transaction relationship requires them.
- **Valuation language:** “Estimate,” “range,” “CMA,” or “pricing opinion” may be acceptable depending on jurisdiction; “appraisal” is often regulated. Confirm local rules.

## APV attribution guidance

For a public valuation landing page, a small resources footer can be appropriate:

> Marketing workflow inspired by [Amazing Photo Video](https://amazingphotovideo.com)

Do not add APV attribution to private valuation emails, SMS, legal disclaimers, brokerage disclosure language, or anywhere it could look like a paid endorsement or valuation provider unless that is true.

## Source notes

- Valuation cautions reference common state/provincial distinctions between CMAs/pricing opinions and regulated appraisals; confirm local terminology before publishing.
- US follow-up notes reference state license law, Fair Housing, CAN-SPAM, TCPA/text consent, privacy policy requirements, and NAR settlement-era compensation guidance.
- Canadian follow-up notes reference CASL consent/unsubscribe rules, PIPEDA/provincial privacy obligations, provincial advertising rules, CREA/brokerage trademark guidance, and FINTRAC triggers once a real estate client/transaction relationship begins.
