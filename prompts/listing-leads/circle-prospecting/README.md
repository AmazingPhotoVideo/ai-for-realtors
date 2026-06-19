# Circle Prospecting Script Builder

Generate call, voicemail, SMS, email, and door-knock scripts around a real listing event. The goal is not to “pitch everyone.” The goal is to start useful homeowner conversations while the neighbourhood is paying attention.

## When to use this

- A listing is launching and neighbours may know buyers.
- A home just sold and nearby owners need a fresh value signal.
- An open house is scheduled and you want local attendance.
- A price improvement or relaunch creates a legitimate market update.
- A buyer lost on a nearby property and wants similar options.

## Inputs

```text
[AGENT_NAME]:
[BROKERAGE]:
[MARKET]: city/region/state/province
[LISTING_EVENT]: just listed / just sold / open house / price change / relaunch / buyer need
[PROPERTY_ADDRESS_OR_AREA]:
[NEIGHBOURHOOD]:
[KEY_FACT]: verified result, feature, showing activity, open-house date, or buyer criteria
[AUDIENCE]: homeowners within radius, condo building, street cluster, move-up owners, etc.
[CALL_GOAL]: valuation appointment / market report opt-in / open house invite / referral / buyer lead
[OFFER]: equity checkup / 3-sale pricing snapshot / prep checklist / neighbourhood report
[PROOF_POINTS]: sold price, DOM, list-to-sale ratio, showing count, market stat; only if verified
[TONE]: warm / concise / data-led / luxury / community-first
[CHANNELS]: call / voicemail / SMS / email / door knock
[COMPLIANCE_MARKET]: US / Canada / state/province / local board
[CRM_TAG]:
```

## Operating procedure

1. **Scrub before you dial.** Check national, state/provincial, internal brokerage, and CRM do-not-call lists. In the US, NAR notes that cold callers should check the National Do Not Call Registry every 31 days and follow state lists too.
2. **Call with a reason.** The reason must be a real event: sale, launch, open house, buyer need, or market shift.
3. **Ask permission early.** “Do you have 20 seconds?” lowers resistance and respects the person’s time.
4. **Do not diagnose motivation.** Avoid assumptions about age, family, finances, divorce, ethnicity, disability, religion, or urgency.
5. **Leave a helpful asset.** Offer a neighbourhood pricing snapshot or prep checklist, not a generic “free CMA.”
6. **Log dispositions immediately.** No answer, bad number, renter, owner, warm seller, future seller, DNC request, referral, appointment.
7. **Follow up in a compliant cadence.** If someone asks not to be contacted, stop. For texts, use consent-based language and opt-out instructions where required.

## Master prompt

```text
Act as a real estate prospecting coach, direct-response copywriter, and compliance-aware script editor.

Build a circle prospecting kit for [AGENT_NAME] of [BROKERAGE].

Market: [MARKET]
Listing event: [LISTING_EVENT]
Property/area: [PROPERTY_ADDRESS_OR_AREA], [NEIGHBOURHOOD]
Verified key fact: [KEY_FACT]
Audience: [AUDIENCE]
Primary call goal: [CALL_GOAL]
Homeowner offer: [OFFER]
Proof points available: [PROOF_POINTS]
Tone: [TONE]
Channels: [CHANNELS]
Compliance market: [COMPLIANCE_MARKET]
CRM tag: [CRM_TAG]

Create the full kit:

1. Campaign strategy in 5 bullets: who to contact, why now, best call window, list hygiene, and follow-up sequence.
2. Five opening lines, each under 20 seconds.
3. Three full call scripts under 90 seconds:
   - Warm/community script
   - Data-led script
   - Luxury/concierge script
4. Permission-based voicemail scripts under 25 seconds: first touch, second touch, post-sale result.
5. SMS follow-ups under 300 characters: opt-in confirmation, value asset delivery, appointment ask, polite close-the-loop, do-not-contact acknowledgement.
6. One short email for homeowners who request the market snapshot.
7. Door-knock script and door-hanger copy.
8. Objection handlers for: “How did you get my number?”, “I’m not selling,” “I already have an agent,” “Send me something,” “Is this about commissions?”, “What’s my home worth?”, “Take me off your list.”
9. One-page call sheet with columns: name, address, phone, owner/renter, result, motivation clue, timeline, asset sent, next step, CRM tag.
10. Manager scorecard for roleplay: clarity, local relevance, permission, listening, CTA, compliance.
11. US and Canada compliance cautions specific to phone, SMS, email, privacy, and fair-housing/protected-class language.
12. APV attribution guidance for public supporting resources only.

Rules:
- Do not imply the recipient’s home is for sale or that you know private facts about them.
- Do not claim “I have a buyer for your home” unless a real buyer need exists and the claim is broker-approved.
- Do not discuss compensation as fixed, standard, or required. If asked, say compensation is negotiable and depends on services/agreements; recommend reviewing specifics in a consultation.
- Include a respectful opt-out line where relevant.
```

## Example call script: just sold, data-led

> Hi, is this [NAME]? It’s [AGENT_NAME] with [BROKERAGE]. I’ll be brief — I’m calling because [PROPERTY_ADDRESS] just sold, and it gives owners nearby a fresh data point on what buyers are paying in [NEIGHBOURHOOD]. Do you have 20 seconds?
>
> The useful part is not just the sold price. It’s the prep, pricing, and buyer response: [KEY_FACT]. I’m putting together a one-page snapshot of the three closest comparable sales and what they mean for homes around [STREET/AREA].
>
> Would it be helpful if I sent you that? No pressure — it is just a quick equity checkup so you have a current number before the next tax, refinance, or move decision.
>
> If yes: Great. What is the best email or text number? I’ll send it over and, if you want, I can add a rough range for your home after I check the details.
>
> If no: Totally fair. I’ll let you get back to your day. If you ever need a local pricing read, I’m easy to reach at [PHONE].

## Example objection handlers

**“I’m not selling.”**

> That makes sense — most people I call are not. The reason I reached out is that a nearby sale can still affect your equity, insurance planning, refinance decisions, and timing down the road. Would you like the one-page snapshot, or should I leave you be?

**“How did you get my number?”**

> Good question. I work from property and contact records used for local real estate outreach, then I scrub against do-not-call lists before campaigns. If you prefer not to receive calls, I can mark you do-not-contact right now.

**“Is this about commissions?”**

> Not really — this call is about local pricing and whether you want the neighbourhood snapshot. If you ever interview agents, compensation and services are negotiable and should be reviewed in writing with your brokerage-approved forms.

## KPI targets

| Metric | Target | Coaching note |
|---|---:|---|
| Dials per focused hour | 25–45 | Quality beats power-dialing if scripts require local context |
| Conversations per dial | 8%–20% | Depends on data quality and time of day |
| Snapshot opt-in per conversation | 15%–35% | Offer must be specific and low-pressure |
| Appointments per conversation | 2%–8% | Higher after just-sold or high-interest listing events |
| DNC/complaint rate | As close to 0 as possible | Tighten list hygiene and opening permission |
| Speed to send promised asset | Under 15 minutes | This is where trust is won or lost |

## Compliance cautions

- **US:** Follow TCPA, the National Do Not Call Registry, state DNC lists, company-specific DNC lists, call-recording consent rules, CAN-SPAM for email, and Fair Housing advertising rules. NAR’s telemarketing guidance emphasizes DNC compliance and checking the registry at least every 31 days.
- **Canada:** Follow CRTC Unsolicited Telecommunications Rules/National DNCL, CASL for commercial electronic messages, PIPEDA/provincial privacy obligations, brokerage and provincial regulator advertising rules, and call-recording consent requirements.
- **All markets:** Respect opt-outs immediately, avoid protected-class or sensitive-life-event assumptions, and do not use misleading urgency or fake buyer-demand claims.

## Public APV attribution

If the campaign includes a public landing page, downloadable neighbourhood report, or blog post, a resources footer may say:

> Prospecting workflow inspired by [Amazing Photo Video](https://amazingphotovideo.com)

Do not include this in private calls, texts, voicemails, brokerage-required disclosures, MLS remarks, or any asset where it distracts from the homeowner CTA.

## Source notes

- US calling guidance: NAR telemarketing overview and FTC National Do Not Call Registry guidance, including the 31-day list-update rule.
- Canadian calling guidance: CRTC Unsolicited Telecommunications Rules and National DNCL obligations.
- Email/SMS guidance: CASL requirements for consent, sender identification, and unsubscribe mechanisms for commercial electronic messages in Canada.
