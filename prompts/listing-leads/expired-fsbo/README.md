# Expired / FSBO Outreach Sequences

A practical 14-day outreach system for two of the highest-intent seller categories: owners whose listings did not sell and owners trying to sell without representation. The tone: empathetic, specific, and useful. No agent-bashing. No scare tactics.

## Core positioning

- **Expired owners** usually need a relaunch plan: pricing evidence, media, merchandising, showing feedback, buyer objections, and a sharper launch sequence.
- **FSBO owners** usually need leverage: buyer qualification, exposure, negotiation support, liability reduction, net-proceeds math, and time savings.
- **Both** need proof that you understand their goal before you pitch your service.

## Inputs

```text
[AGENT_NAME]:
[BROKERAGE]:
[MARKET]: city/region/state/province
[LEAD_TYPE]: expired / cancelled / withdrawn / FSBO
[PROPERTY_ADDRESS_OR_AREA]:
[PROPERTY_TYPE]: detached / condo / townhome / acreage / luxury / multi-family
[KNOWN_FACTS]: list price, DOM, price changes, showing notes, photos/marketing observations, FSBO asking price
[SELLER_GOAL]: net more / sell faster / privacy / avoid commission / relocation / test market / unknown
[OFFER]: relaunch audit / net sheet / buyer-readiness checklist / photo-and-pricing review / 3-sale CMA
[DIFFERENTIATOR]: media plan, database, negotiation, local results, staging, pricing model, luxury launch
[TONE]: warm / direct / analytical / luxury / no-pressure
[CHANNELS]: call / voicemail / SMS / email / letter / door drop
[COMPLIANCE_MARKET]: US / Canada / state/province / board
[CRM_TAG]:
```

## 14-day cadence

| Day | Channel | Expired angle | FSBO angle | CTA |
|---:|---|---|---|---|
| 1 | Call + voicemail | “I reviewed the market, not to criticize — to find the gap.” | “I have a checklist most private sellers use to avoid weak offers.” | Send audit/checklist |
| 1 | Email | 3 likely reasons strong homes do not sell | FSBO exposure + buyer qualification risks | Reply with goal |
| 2 | SMS if permitted | Offer one-page relaunch audit | Offer net-sheet template | Confirm interest |
| 3 | Call | Ask what feedback they received | Ask what buyer quality has been like | 10-minute consult |
| 4 | Letter/door drop | Relaunch plan outline | Private-sale protection checklist | Scan/download |
| 6 | Email | Case-study style relaunch framework | “Net is not the same as saving commission” | Review numbers |
| 8 | Call/VM | Pricing vs presentation vs access | Buyer objections + inspection/financing | Book review |
| 10 | SMS/email | “Should I close the file?” | “Want the checklist before weekend showings?” | Yes/no |
| 14 | Email + call | Final value asset and opt-out | Final value asset and opt-out | Keep/close |

## Master prompt

```text
You are a real estate listing conversion strategist specializing in expired, cancelled, withdrawn, and FSBO seller leads.

Build a 14-day outreach sequence for [AGENT_NAME] of [BROKERAGE].

Market: [MARKET]
Lead type: [LEAD_TYPE]
Property: [PROPERTY_ADDRESS_OR_AREA]
Property type: [PROPERTY_TYPE]
Known facts: [KNOWN_FACTS]
Likely seller goal: [SELLER_GOAL]
Value offer: [OFFER]
Agent differentiator: [DIFFERENTIATOR]
Tone: [TONE]
Channels: [CHANNELS]
Compliance market: [COMPLIANCE_MARKET]
CRM tag: [CRM_TAG]

Output:

1. Seller psychology brief: likely emotions, risks, and what not to say.
2. Positioning strategy: one sentence for expired leads and one for FSBO leads.
3. 14-day cadence table with channel, message goal, copy, CTA, and CRM task.
4. Call scripts:
   - Expired first call under 90 seconds
   - FSBO first call under 90 seconds
   - Second call after no response
   - Re-engagement call after two weeks
5. Voicemails under 25 seconds for expired and FSBO.
6. SMS messages under 300 characters with opt-out language when appropriate.
7. Emails:
   - Day 1 audit offer
   - Day 3 value asset delivery
   - Day 6 proof/case-study email
   - Day 10 “close the loop” email
   - Day 14 final helpful note
8. One-page letter for print/door drop.
9. Offer asset outline:
   - Expired Listing Relaunch Audit
   - FSBO Net-Proceeds and Risk Checklist
10. Objection handlers for: “I’m relisting with the same agent,” “Agents just want a commission,” “I’m saving money FSBO,” “Bring me a buyer,” “We’re taking a break,” “Your fee is too high,” “Stop contacting me.”
11. Compliance cautions for US and Canada: DNC, TCPA, CASL, privacy, fair housing, brokerage approval, MLS/NAR settlement-era compensation language, and not soliciting represented clients.
12. Metrics dashboard and follow-up rules.
13. APV attribution guidance for public resources only.

Rules:
- Do not criticize the previous agent or the homeowner’s choices.
- Do not say the listing “failed.” Say “did not sell,” “expired,” or “came off market.”
- Do not solicit a client currently under an active representation agreement.
- Do not imply commissions are standard, fixed, required, or universally paid by one side.
- Do not fabricate buyers, showings, sale prices, or market data.
```

## Example: expired first-call script

> Hi [NAME], it’s [AGENT_NAME] with [BROKERAGE]. I know your home recently came off the market, so I’ll be respectful and brief. I’m not calling to criticize what happened — I’m calling because when a good home does not sell, it is usually one of four things: pricing position, presentation, exposure, or buyer confidence. Do you have 30 seconds?
>
> I took a quick look at the competing homes around [AREA]. If you are still open to selling, I can put together a one-page relaunch audit showing what I would adjust before going live again — no obligation, and you can use it either way.
>
> Would that be useful, or are you fully taking the property off the market for now?

## Example: FSBO first-call script

> Hi [NAME], this is [AGENT_NAME] with [BROKERAGE]. I saw your home is being offered privately in [AREA]. I’m not calling to pressure you to list. A lot of owners start privately because they want control and a better net, which makes sense.
>
> I have a short FSBO checklist covering buyer qualification, showing safety, offer terms, inspection/financing risk, and net-proceeds math. Would you like me to send it over?
>
> If you ever want a second set of eyes on pricing or buyer feedback, I’m happy to be a resource.

## Email templates

### Day 1 — Expired audit offer

Subject: A practical relaunch audit for [PROPERTY_ADDRESS]

Hi [NAME],

I noticed [PROPERTY_ADDRESS] recently came off the market. I know that can be frustrating, especially when you have already prepared the home, handled showings, and made plans around a sale.

When a listing does not sell, the answer is rarely “drop the price and hope.” The better question is: what would we change before the next launch?

I can put together a one-page relaunch audit covering:

- the closest competing sales and active listings
- how buyers likely compared the home
- presentation/media opportunities
- pricing position and launch timing
- the first seven days of a stronger relaunch plan

If you want it, reply “audit” and I’ll send it over.

Respectfully,
[AGENT_NAME]
[PHONE]
[Brokerage-required disclosure]

### Day 1 — FSBO checklist offer

Subject: FSBO checklist for [AREA] sellers

Hi [NAME],

I saw your home is being offered privately. Many owners choose that route because they want control and a better net. That is reasonable — but the best FSBO outcomes usually come from treating the process like a professional launch, not just a sign and a few posts.

I have a short checklist you can use before your next showing:

- how to screen buyer financing
- what to confirm before sharing access
- questions to ask after showings
- common inspection and appraisal issues
- how to compare “saving commission” with true net proceeds

If you want it, reply “checklist” and I’ll send it over.

Best,
[AGENT_NAME]
[PHONE]
[Brokerage-required disclosure]

## Value asset outlines

### Expired Listing Relaunch Audit

1. Property snapshot and prior listing timeline.
2. Competing sales and current alternatives.
3. Buyer-friction diagnosis: price, product, presentation, access, confidence.
4. Media/merchandising checklist: photos, video, floor plan, copy, staging, repairs.
5. Relaunch calendar: prep week, launch week, open house, feedback loop, adjustment triggers.
6. Net and timing scenarios.
7. Recommended next step.

### FSBO Net-Proceeds and Risk Checklist

1. Asking price vs likely appraisal range.
2. Buyer qualification questions.
3. Showing safety checklist.
4. Offer-term comparison grid.
5. Inspection, financing, deposit, closing, and condition risks.
6. Marketing exposure audit.
7. Net-proceeds worksheet comparing private sale, limited service, and full-service representation.

## KPIs

| KPI | Target | Improve by |
|---|---:|---|
| Contact rate | 8%–20% | Better numbers, varied call windows, mail + email support |
| Value asset acceptance | 20%–45% of conversations | Make audit specific, not generic |
| Appointment rate | 5%–15% of conversations | Ask diagnostic questions before pitching |
| Signed listing rate | Market dependent | Bring a concrete relaunch plan and seller net sheet |
| Complaint/DNC rate | Near 0 | Respect representation, opt-outs, and tone |

## Compliance cautions

- **Representation:** Do not contact owners in a way that violates active listing agreements, exclusive representation, brokerage policy, MLS/board rules, or provincial/state regulations. Verify status before outreach.
- **US:** Follow TCPA, National and state Do Not Call rules, CAN-SPAM, Fair Housing, state license law, brokerage advertising approval, and current NAR settlement practice changes. Avoid saying buyer-broker compensation is fixed, standard, mandatory, or displayed on MLS if your market prohibits it.
- **Canada:** Follow CASL, National DNCL/CRTC telemarketing rules, PIPEDA/provincial privacy law, FINTRAC obligations when a client/transaction relationship begins, CREA/provincial advertising rules, and brokerage approval. Ontario agents should be mindful of TRESA/RECO advertising and representation rules.
- **All markets:** Make no legal, tax, appraisal, or financing guarantees. Encourage sellers to consult qualified professionals.

## APV attribution guidance

Use APV attribution only when turning this into a public resource such as a blog, downloadable seller guide, or case study:

> Seller outreach workflow inspired by [Amazing Photo Video](https://amazingphotovideo.com)

Do not place APV links in private prospecting emails/SMS, listing agreements, MLS copy, legal disclaimers, or materials that imply APV worked on a specific property unless that is true.

## Source notes

- US outreach guidance: NAR telemarketing resources, FTC National Do Not Call Registry guidance, TCPA considerations, CAN-SPAM, Fair Housing, and NAR settlement practice-change FAQs.
- Canadian outreach guidance: CRTC National DNCL/Unsolicited Telecommunications Rules, CASL, PIPEDA/provincial privacy obligations, FINTRAC real estate obligations, and provincial regulator guidance such as RECO/TRESA in Ontario.
- Always confirm local brokerage, MLS/board, and legal requirements before contacting expired, withdrawn, cancelled, or FSBO owners.
