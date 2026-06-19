# The Realtor Listing Flywheel

One listing can create more than one commission. A well-run listing can create buyer leads, seller conversations, neighbourhood authority, referral proof, and reusable content. Most agents treat a listing like an inventory item. Top operators treat it like a 60-day media event.

## The goal

For every listing, create:

- 1 signed seller client served exceptionally well
- 10–30 buyer conversations
- 5–15 homeowner conversations around the listing
- 1–3 valuation requests from neighbours or sphere
- 20–40 reusable content assets
- 1 public case study or market lesson, if the seller permits

## The flywheel model

```text
Prepare → Tease → Launch → Capture → Report → Sell → Prove → Farm → Nurture → Repeat
```

Each stage feeds the next. The media created for the seller becomes proof for future sellers. The open house creates buyer leads. The sale result creates homeowner conversations. The homeowner conversations create listing appointments.

## Stage 1: Prepare before launch

**Objective:** Build the listing as a product, not a post.

Actions:

1. Run `skills/listing-presentation/` to clarify seller goals, pricing strategy, and launch plan.
2. Build the property story with `prompts/leverage/property-story/`.
3. Create the prep checklist and media plan: photos, video, floor plan, drone, vertical clips, feature sheet, landing page, sign rider QR.
4. Draft circle-prospecting and postcard assets before the listing goes live.
5. Set tracking: landing page URL, QR code, UTM links, call tracking, CRM tags.

Outputs:

- listing launch calendar
- property story
- seller-approved fact sheet
- open house lead capture
- neighbour outreach list
- compliance-approved ad/disclaimer language

## Stage 2: Neighbourhood teaser

**Objective:** Make the area aware without violating MLS, brokerage, seller privacy, or board rules.

Use when permitted:

- “A new [PROPERTY_TYPE] is preparing for market near [MICRO_AREA].”
- “We are tracking buyer demand for [PROPERTY_TYPE] homes in [NEIGHBOURHOOD].”
- “Want the [NEIGHBOURHOOD] pricing snapshot before the next launch?”

Avoid:

- confidential details without seller permission
- misleading scarcity
- protected-class targeting
- unapproved off-market claims
- compensation claims that are not broker-approved

AI assets:

- `prompts/listing-leads/geo-farm/`
- `prompts/listing-leads/circle-prospecting/`
- `prompts/listing-leads/home-valuation/`

## Stage 3: Launch week

**Objective:** Concentrate attention in the first 7–10 days.

Launch checklist:

- MLS/live listing copy and media approved by brokerage/seller
- single-property landing page with lead capture
- social posts and short-form video
- email to buyer database and sphere
- agent-to-agent outreach
- open house QR sign-in
- sign rider QR to mobile listing page
- first circle-prospecting block
- first postcard or door-hanger drop if budget allows

Recommended daily rhythm:

| Day | Action | Lead goal |
|---:|---|---|
| 1 | Listing goes live, email database, social launch | buyer inquiries + shares |
| 2 | Circle prospect 50–100 nearby homes | homeowner conversations |
| 3 | Short video/Reel + agent network push | reach + showing requests |
| 4 | Open house invite to neighbours | local attendance |
| 5 | Showing feedback review | seller confidence + adjustment signals |
| 6–7 | Open house + lead capture | buyer and seller leads |
| 8–10 | Report early market response | proof + next action |

## Stage 4: Capture every signal

**Objective:** Turn attention into trackable leads.

Capture points:

- sign rider QR
- open house QR sign-in
- landing page form
- “request the price” or “request the feature sheet” CTA where compliant
- valuation CTA for neighbours
- market report subscription
- retargeting pixel/audience
- call tracking number

CRM tags:

- listing-buyer
- open-house-visitor
- neighbour-owner
- valuation-request
- sphere-engaged
- agent-referral
- seller-lead-hot
- seller-lead-nurture

Speed-to-lead rule: respond to inbound leads within five minutes whenever possible. For seller signals, send a value asset first: pricing snapshot, prep checklist, or equity checkup.

## Stage 5: Active market content

**Objective:** Use buyer questions and feedback to educate future sellers.

Content ideas:

- “The three questions buyers keep asking about this home.”
- “What first-week showing feedback tells us.”
- “How buyers compare homes in [NEIGHBOURHOOD].”
- “What sellers can learn from launch week.”
- “Why presentation changes negotiation leverage.”

AI assets:

- `prompts/leverage/content-multiplier/`
- `prompts/leverage/ai-video/`
- `prompts/leverage/market-report/`

## Stage 6: Sold result and proof

**Objective:** Convert the result into a market lesson, not a victory lap.

Use the result to answer:

- What did buyers respond to?
- What pricing strategy worked?
- What preparation mattered?
- How did the result compare with recent sales?
- What should nearby owners know now?

Create:

- just-sold postcard using `prompts/listing-leads/postcards/`
- just-sold call scripts using `prompts/leverage/circle-prospecting/just-sold/` or `prompts/listing-leads/circle-prospecting/`
- seller case study if approved
- social post explaining the market lesson
- email to homeowners in the farm
- valuation CTA tied to the result

## Stage 7: Farm and nurture

**Objective:** Keep the authority created by the listing from disappearing.

Follow-up sequence:

| Timing | Audience | Message | CTA |
|---|---|---|---|
| Within 24 hours of firm sale | neighbours | result/market lesson | request equity checkup |
| Week 1 | open house visitors | similar homes + buyer consult | book buyer call |
| Week 1 | valuation responders | CMA range + assumptions | 15-min review |
| Week 2 | farm/sphere | case study or lesson | ask a pricing question |
| Month 1 | farm | monthly market report | subscribe/book review |
| Month 2–3 | seller nurtures | prep/timing/net content | listing appointment |

Use `skills/seller-persona-strategist/` to segment homeowner replies by motivation and timeline.

## Metrics dashboard

Track one listing as its own campaign:

| Metric | Target/interpretation |
|---|---|
| Listing page visits | Indicates media and traffic quality |
| QR scans | Measures sign, postcard, and open house capture |
| Inquiries | Buyer demand signal |
| Open house sign-ins | Lead capture and market feedback |
| Neighbour conversations | Seller pipeline creation |
| Valuation requests | Highest-value listing-lead signal |
| Seller appointments | Main flywheel outcome |
| Content assets created | Reusable authority inventory |
| Cost per lead | Compare direct mail, ads, QR, social |
| Cost per seller appointment | More important than impressions or likes |
| Time-to-response | Conversion driver |

## Compliance cautions

- Get seller and brokerage approval before publishing property details, sale results, behind-the-scenes content, testimonials, or case studies.
- Follow MLS/board rules for sold data, days on market, offer counts, and advertising statuses.
- Avoid Fair Housing/protected-class language in targeting or copy.
- Do not claim “we have buyers for your home” unless there is a real, documented buyer need and the claim is approved.
- In the US, follow TCPA, Do Not Call, CAN-SPAM, state license law, brokerage policy, and current NAR settlement practice changes. Do not present compensation as fixed, standard, or mandatory.
- In Canada, follow CASL, PIPEDA/provincial privacy, CRTC/National DNCL rules, provincial regulator requirements, CREA trademark rules, FINTRAC obligations when applicable, and brokerage approval.
- Do not call a CMA an appraisal unless legally appropriate.

## APV attribution

If this workflow becomes a public guide, case study, or downloadable resource, a natural resource credit can be used:

> Listing marketing workflow inspired by [Amazing Photo Video](https://amazingphotovideo.com)

Do not imply APV photographed, filmed, marketed, or endorsed a specific listing unless APV actually did. Do not add APV attribution to MLS remarks, private seller emails/SMS, listing agreements, legal disclaimers, or brokerage-required disclosure space.

## Source notes

- US compliance notes reference Fair Housing, MLS/board advertising rules, TCPA, Do Not Call, CAN-SPAM, state license law, brokerage policy, and NAR settlement practice-change guidance.
- Canadian compliance notes reference CASL, PIPEDA/provincial privacy, CRTC/National DNCL, provincial regulator requirements, CREA trademark guidance, FINTRAC obligations, and brokerage approval.
- Verify seller permission, brokerage approval, and local MLS/board rules before publishing property details, sold data, offer counts, testimonials, or case studies.

## Quick implementation checklist

```text
[ ] Seller goals and approvals captured
[ ] Listing presentation and pricing strategy complete
[ ] Property story written
[ ] Media shot list complete
[ ] Landing page and QR tracking live
[ ] Open house capture tested
[ ] Launch content scheduled
[ ] Circle-prospecting list scrubbed and tagged
[ ] Postcard/door-hanger proofed and tracked
[ ] Retargeting audience configured where permitted
[ ] Speed-to-lead workflow tested
[ ] Sold-result plan drafted before firm sale
[ ] Seller case-study permission requested if appropriate
[ ] Leads segmented in CRM
[ ] Monthly nurture scheduled
```
