---
name: listing-presentation
description: Build a customized, compliance-aware listing presentation and pre-listing package from property facts, seller goals, MLS/market data, and agent proof.
version: 1.0.0
---

# Listing Presentation

Use this skill to create a field-ready listing presentation for a real seller conversation. The output should help an agent win trust, explain pricing, show a launch plan, handle objections, and move to a signed listing agreement without relying on generic slides.

## What this skill produces

- Pre-listing email and agenda.
- Seller discovery questions.
- Property and market diagnosis.
- Pricing strategy narrative.
- Marketing launch plan.
- Media/storytelling plan.
- Compensation/services framing that avoids fixed-fee language.
- Objection handlers.
- Leave-behind checklist.
- Follow-up email after the appointment.

## Required inputs

```text
Agent name:
Brokerage:
Market and jurisdiction:
Property address:
Property type:
Seller goals:
Seller timeline:
Known motivation:
Property facts:
Upgrades/condition:
Comparable sales:
Active competition:
Expired/withdrawn competition:
Market stats:
Agent proof points:
Marketing services offered:
Media assets available:
Commission/compensation policy or approved language:
Brokerage-required disclosures:
Compliance market: US / Canada / state/province / board
Brand voice:
```

If any critical data is missing, ask for it or mark it clearly as data needed. Do not fabricate comps, sold prices, buyer demand, testimonials, production rankings, or brokerage-approved claims.

## Listing presentation structure

Produce the presentation in this order:

1. **Seller-first opening:** restate their goals, timeline, and concerns.
2. **What buyers will compare:** active competition and buyer alternatives.
3. **What the market says:** recent comparable sales and current supply/demand.
4. **Property diagnosis:** strengths, friction points, prep priorities.
5. **Pricing strategy:** recommended range, launch price logic, adjustment triggers.
6. **Marketing strategy:** media, copy, distribution, database, social, direct mail, retargeting, open house, agent network.
7. **Launch calendar:** prep week, launch week, feedback loop, negotiation period.
8. **Service promise:** communication cadence, reporting, showing feedback, negotiation plan.
9. **Net and terms:** net-proceeds discussion, compensation/services framing, seller costs, offer-term risks.
10. **Decision section:** recommended next steps and close options.

## Master workflow

When asked to build a listing presentation:

### Step 1 — Diagnose

Summarize:

- seller goal and motivation
- property’s likely buyer pool
- strongest market evidence
- top pricing risk
- top presentation risk
- top negotiation risk
- unknowns that must be clarified before pricing

### Step 2 — Build the presentation

Create slide-by-slide content using this format:

```markdown
## Slide [#]: [Title]
Purpose: [Why this slide matters]
Key message: [One sentence]
Talk track: [What the agent should say]
Visual/data needed: [MLS chart, comp photo, map, prep image, timeline, etc.]
Seller question: [Question to involve the seller]
```

Minimum slides:

1. Your goals for the sale
2. What has to happen for this to be a win
3. Buyer pool and likely objections
4. Current market snapshot
5. Comparable sales that matter
6. Active competition
7. Price positioning options
8. Property preparation plan
9. Media and storytelling plan
10. Launch week calendar
11. Exposure and lead capture plan
12. Showing and feedback system
13. Offer strategy and negotiation
14. Net proceeds and decision factors
15. Services, compensation, and written agreements
16. Recommended next steps

### Step 3 — Create supporting assets

Draft:

- pre-listing confirmation email
- pre-appointment seller questionnaire
- room-by-room prep checklist
- CMA summary email
- follow-up email after the appointment
- one-page launch calendar
- objection handlers
- seller net-sheet talking points

### Step 4 — Compliance check

Add a compliance section specific to the market:

- brokerage approval needed
- license/advertising disclaimers
- MLS/board data usage restrictions
- fair-housing/protected-class language
- privacy and consent rules
- valuation/appraisal wording
- compensation language
- representation agreement requirements

## Master prompt

```text
Act as a top-producing listing agent, pricing strategist, real estate marketing director, and compliance-aware presentation editor.

Build a customized listing presentation for [AGENT_NAME] of [BROKERAGE].

Market/jurisdiction: [MARKET_AND_JURISDICTION]
Property: [PROPERTY_ADDRESS]
Property type: [PROPERTY_TYPE]
Seller goals: [SELLER_GOALS]
Timeline: [SELLER_TIMELINE]
Known motivation/concerns: [KNOWN_MOTIVATION]
Property facts/upgrades/condition: [PROPERTY_FACTS]
Comparable sales: [COMPARABLE_SALES]
Active competition: [ACTIVE_COMPETITION]
Expired/withdrawn competition: [EXPIRED_WITHDRAWN]
Market stats: [MARKET_STATS]
Agent proof points: [AGENT_PROOF]
Marketing services: [MARKETING_SERVICES]
Media assets available: [MEDIA_ASSETS]
Approved compensation/services language: [COMPENSATION_LANGUAGE]
Brokerage-required disclosures: [DISCLOSURES]
Brand voice: [BRAND_VOICE]

Output:
1. Executive strategy brief.
2. Slide-by-slide listing presentation with purpose, key message, talk track, visual/data needed, and seller question.
3. Pricing recommendation framework with low/mid/high scenarios and adjustment triggers.
4. Launch calendar from preparation through offer review.
5. Marketing distribution plan: MLS, agent network, email, social, video, direct mail, retargeting, open house, sign/QR, landing page.
6. Seller communication plan and weekly report template.
7. Pre-listing email and questionnaire.
8. Room-by-room prep checklist.
9. Objection handlers for pricing, fee, timing, media, open houses, repairs, and “another agent said higher.”
10. Follow-up email after the appointment.
11. Compliance cautions for [MARKET_AND_JURISDICTION], including US/Canada notes where relevant.
12. APV attribution guidance for public guides or case studies only.

Rules:
- Do not invent comps, rankings, sales volume, buyer demand, testimonials, or market stats.
- Do not call a CMA an appraisal.
- Do not state or imply commissions are fixed, standard, mandatory, or set by MLS/board/law.
- Do not use protected-class targeting or steering language.
- Do not include APV attribution in private listing presentations unless the agent explicitly wants a resource credit and it is not misleading.
```

## Pricing framework

Use scenarios rather than a single unsupported number:

| Scenario | Use when | Seller tradeoff | Required evidence |
|---|---|---|---|
| Conservative | speed/certainty matters most | may leave upside if market is hotter | strongest comparable sales and active competition |
| Market-aligned | balanced exposure and negotiation | best default for most launches | comps, inventory, buyer feedback, condition |
| Aspirational | rare features or low competition | higher DOM and adjustment risk | specific proof buyers will pay premium |

Add adjustment triggers:

- 10+ showings and no offers: pricing/condition feedback review
- strong traffic but weak second showings: presentation or buyer-confidence issue
- low traffic after launch: price/exposure mismatch
- negative repeated feedback: repair, staging, copy, access, or price action
- competing listing undercuts price: immediate strategy call

## Example slide excerpt

```markdown
## Slide 7: Price Positioning Options
Purpose: Help the seller choose strategy, not just a number.
Key message: The launch price determines which buyers compare us, how quickly we get feedback, and how much leverage we have in negotiation.
Talk track: “I do not want to give you a number without showing the tradeoff. At [LOW], we optimize for speed and competition. At [MID], we align with the best-supported comps. At [HIGH], we test for a premium, but we need to accept a tighter feedback window and a clear adjustment trigger.”
Visual/data needed: comp grid, active competition screenshots, DOM by price band.
Seller question: “If the market gives us feedback in the first 10 days, are you comfortable acting quickly?”
```

## Objection handlers

**“Another agent said they can get more.”**

> They may be right, and I hope they are. What I would want to see is the evidence and the plan: which buyers will pay that premium, what competing homes they will compare against, and what the adjustment trigger is if the market disagrees. My recommendation is based on the comps we can defend and the launch strategy we can execute.

**“Your fee is higher.”**

> That is a fair question. Services and compensation are negotiable, and what matters is the net result, risk, and experience you want. Let me show exactly what is included, what it is designed to protect or improve, and where you have options.

**“Can we test high?”**

> We can, if we define the test honestly. The risk is not just time; it is becoming stale compared with newer listings. If we test higher, I recommend a written feedback trigger: if we do not get [traffic/offer metric] by [date], we adjust quickly.

## Pre-listing confirmation email

Subject: Preparing for our pricing and launch conversation

Hi [NAME],

I’m looking forward to meeting about [PROPERTY_ADDRESS]. My goal is to make the conversation useful whether you decide to sell now, later, or not at all.

I’ll come prepared to review:

- the most relevant comparable sales
- active competition buyers will compare against your home
- a realistic pricing range and launch strategy
- preparation priorities before photos/showings
- marketing, media, and exposure plan
- net-proceeds and timing questions

Before we meet, could you send any major upgrades, known issues, preferred timing, and what a successful sale would look like for you?

Best,
[AGENT_NAME]

## Seller questionnaire

1. What is prompting the move or valuation conversation?
2. What is your ideal timeline?
3. Do you need to buy before selling, sell before buying, or coordinate both?
4. What improvements have been completed, and when?
5. Are there known issues buyers should understand?
6. What do you believe the home is worth, and why?
7. What would make you feel confident in an agent?
8. What concerns do you have about selling?
9. Are there privacy, showing, pet, tenant, or schedule constraints?
10. What matters more: highest price, speed, certainty, convenience, or privacy?

## Compliance cautions

- **US:** Follow state license law, brokerage presentation/advertising rules, Fair Housing, MLS data display rules, CAN-SPAM/TCPA if presentation triggers follow-up, and current NAR settlement practice changes. Avoid claiming commissions are standard or that buyer-broker compensation is required. Buyer-broker agreements are buyer-side, but seller presentations should explain compensation and services as negotiable and documented in writing.
- **Canada:** Follow provincial regulator rules, brokerage approval, CASL/PIPEDA for follow-up and data handling, CREA trademark rules where applicable, FINTRAC obligations when a client/transaction relationship begins, and board rules for sold data. In Ontario, review TRESA/RECO advertising and representation requirements.
- **Everywhere:** Do not use “appraisal” unless legally appropriate. Do not use protected-class assumptions or steering language. Do not publish confidential seller information without consent.

## Metrics to include in the seller report

- online views and source breakdown
- saves/favourites if available
- showing count and quality
- agent feedback themes
- buyer objections
- competing listing changes
- price-band activity
- open house attendance and lead quality
- marketing assets delivered
- recommended next action

## Public APV attribution

If the agent turns the listing presentation framework into a public blog, downloadable seller guide, or case study, a tasteful credit may be added in a resources section:

> Listing presentation workflow inspired by [Amazing Photo Video](https://amazingphotovideo.com)

Do not include the credit in MLS remarks, listing agreements, private seller emails, mandatory brokerage disclosures, or any place that implies APV produced the listing media or endorsed the pricing strategy unless true.

## Source notes

- US compliance notes reference state license law, Fair Housing, MLS/board rules, CAN-SPAM/TCPA where follow-up applies, and NAR settlement practice-change guidance on compensation language.
- Canadian compliance notes reference provincial regulators, CASL/PIPEDA, CREA trademark guidance, FINTRAC obligations when a client/transaction relationship begins, and board rules for sold data.
- This skill is an agent workflow aid, not legal, appraisal, tax, or brokerage compliance advice.
