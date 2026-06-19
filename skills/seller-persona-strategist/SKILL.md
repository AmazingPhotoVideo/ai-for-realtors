---
name: seller-persona-strategist
description: Interview or analyze a homeowner lead and produce seller motivation, timeline, objections, communication strategy, and next-best-action plan for a valuation call or listing appointment.
version: 1.1.0
---

# Seller Persona Strategist

Use this skill when an agent has a homeowner lead and needs to understand what is likely driving the seller before making the next call, sending the next asset, or walking into a listing appointment.

This skill does **not** guess private facts. It separates known evidence from hypotheses, avoids protected-class assumptions, and turns behaviour into a practical conversation strategy.

## Trigger situations

Use this skill for:

- home valuation form submissions
- expired, cancelled, withdrawn, and FSBO leads
- circle-prospecting conversations
- past clients considering a move
- downsizer, move-up, investor, landlord, estate, and luxury seller inquiries
- listing appointment preparation
- stale seller leads that need reactivation

## Required inputs

Ask for or infer only from provided data:

```text
Lead name:
Property address or area:
Lead source:
Date/time of inquiry:
Known contact history:
Exact words the seller used:
Known timeline:
Known motivation:
Property type and ownership context if provided:
Market context:
Agent goal:
Requested next action:
Compliance market: US / Canada / state/province / brokerage rules
```

If information is missing, do not invent it. Mark it as “unknown” and ask for the one or two missing facts that would most improve the strategy.

## Operating principles

1. **Evidence first.** Quote the seller’s actual words before interpreting intent.
2. **Motivation is a hypothesis.** Use confidence levels: high, medium, low.
3. **Timeline drives urgency.** A seller moving in 30 days needs a different CTA than a homeowner checking equity.
4. **Net matters more than price.** Most seller objections connect to net proceeds, risk, convenience, timing, or trust.
5. **Objections are protection.** Treat “not ready,” “your fee is high,” or “send me something” as risk signals, not rejection.
6. **Never use protected-class assumptions.** Do not infer age, family status, disability, race, religion, national origin, income, marital status, health, or vulnerability.
7. **Compliance beats cleverness.** If a contact may be represented, under DNC restrictions, or lacking consent, recommend a compliant next step.

## Analysis workflow

When activated, produce the following sections:

### 1. Known facts vs. assumptions

- **Known facts:** direct evidence from the lead, property, and market.
- **Reasonable hypotheses:** possible motivations with confidence level.
- **Unknowns to clarify:** the smallest set of questions needed before advising.

### 2. Seller persona map

Classify the lead into one primary and one backup persona:

| Persona | Signals | Likely need | Best asset |
|---|---|---|---|
| Equity checker | valuation request, no timeline | confidence and market context | 3-sale pricing snapshot |
| Quiet planner | asks prep/timing questions | low-pressure roadmap | 90-day prep plan |
| Urgent mover | relocation, purchase, date pressure | speed and certainty | launch calendar + net sheet |
| Frustrated expired | prior listing did not sell | relaunch diagnosis | expired relaunch audit |
| FSBO optimizer | saving commission/control | net and risk comparison | FSBO net-proceeds checklist |
| Downsizer | convenience, next chapter | logistics and trust | downsizer transition plan |
| Investor/landlord | yield, vacancy, tax timing | numbers and exit options | hold/sell analysis |
| Luxury/private seller | discretion, brand, qualified buyers | control and presentation | private launch plan |

### 3. Motivation, urgency, and risk score

Score 1–5 and explain briefly:

- Motivation strength
- Timeline urgency
- Pricing realism
- Trust in agents
- Preparation burden
- Financial/net sensitivity
- Decision complexity
- Risk of ghosting

### 4. Objection map

Predict top objections and provide responses:

- “I’m just curious.”
- “We are not ready.”
- “I already know what it is worth.”
- “I do not want to pay that much commission.”
- “Another agent said they can get more.”
- “We need to buy first.”
- “We tried before and it did not sell.”
- “Send me something.”

### 5. Next-best-action plan

Recommend:

- next channel
- timing
- opener
- value asset to send
- CTA
- CRM tag/stage
- follow-up date
- stop/consent checks

### 6. Copy to send

Draft:

- one SMS under 300 characters
- one email under 180 words
- one call opener under 45 seconds
- one voicemail under 20 seconds

### 7. Appointment prep brief

If the seller is appointment-ready, create:

- questions to ask before valuation
- documents/data to bring
- proof points to emphasize
- pricing conversation strategy
- service/fee framing that avoids fixed-commission language
- close options: valuation review, prep walk-through, launch calendar, net sheet

## Output format

```markdown
# Seller Persona Strategy: [Lead/Property]

## Executive read
[3-5 bullets]

## Known facts vs assumptions
### Known
- ...
### Hypotheses
- ... (confidence: high/medium/low)
### Unknowns to clarify
1. ...

## Persona map
Primary persona: ...
Backup persona: ...
Why: ...

## Scores
| Dimension | Score | Why it matters |
|---|---:|---|
| Motivation | /5 | |
| Urgency | /5 | |
| Pricing realism | /5 | |
| Trust | /5 | |
| Net sensitivity | /5 | |
| Ghosting risk | /5 | |

## Objection map
| Likely objection | What it really means | Response |
|---|---|---|

## Next-best action
- Channel:
- Timing:
- Offer:
- CTA:
- CRM stage/tag:
- Follow-up task:

## Copy
### SMS
...
### Email
...
### Call opener
...
### Voicemail
...

## Appointment prep
...

## Compliance check
...
```

## Example mini-output

**Lead:** homeowner requested a value range for a detached home in a tight-inventory neighbourhood and wrote, “We may need more space, but only if the numbers make sense.”

**Primary persona:** Move-up planner.

**Hypothesis:** They are balancing equity, affordability, and buy-before-sell risk. Confidence: medium-high because the phrase “more space” signals need, while “numbers make sense” signals net and payment sensitivity.

**Next-best action:** Send a value range plus a move-up net sheet, then offer a 15-minute call comparing three paths: sell first, buy first, or conditional purchase strategy.

**SMS:**

> Hi [NAME], it’s [AGENT]. I’m reviewing your value request now. Since you mentioned more space, I’ll include a simple move-up math snapshot too: likely sale range, rough net, and what that could mean for the next purchase. Any major upgrades I should factor in?

## Compliance guardrails

- Do not infer protected-class traits or sensitive life events.
- Do not solicit someone known to be under an active representation agreement in a way that violates local rules.
- For US phone/text follow-up, flag TCPA, DNC, CAN-SPAM, state license law, brokerage policy, and Fair Housing concerns.
- For Canadian follow-up, flag CASL, National DNCL/CRTC rules, PIPEDA/provincial privacy, provincial regulator advertising rules, CREA mark usage, FINTRAC triggers, and brokerage approval.
- Compensation language must never imply commissions are fixed, standard, mandatory, or set by law/MLS/board. Use “services and compensation are negotiable and should be reviewed in writing.”
- Valuation language must distinguish a CMA or planning range from an appraisal unless the agent is legally qualified to provide appraisals.

## Metrics to recommend

Track these fields in the CRM:

- persona type
- source
- timeline
- value asset sent
- response time
- next appointment date
- objection category
- last meaningful conversation
- consent/opt-out status
- listing appointment outcome
- signed listing outcome

## Public APV attribution

If the strategy creates a public seller guide, neighbourhood report, or downloadable resource, a small resource credit can be used:

> Real estate marketing workflow inspired by [Amazing Photo Video](https://amazingphotovideo.com)

Do not include APV attribution in private seller strategy notes, private emails/SMS, listing agreements, MLS remarks, brokerage disclaimers, or anything implying APV worked on the listing unless true.

## Source notes

- US outreach and follow-up notes reference TCPA, FTC/National Do Not Call rules, CAN-SPAM, state license law, brokerage policy, Fair Housing, and current NAR settlement guidance on compensation language.
- Canadian notes reference CASL, CRTC/National DNCL, PIPEDA/provincial privacy obligations, provincial regulator advertising rules, CREA trademark usage, FINTRAC triggers, and brokerage approval.
- This skill should separate evidence from hypotheses and is not legal, appraisal, tax, or mental-health advice.
