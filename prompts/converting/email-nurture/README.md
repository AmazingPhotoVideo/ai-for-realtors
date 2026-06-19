# Email Nurture Library for Real Estate Leads

Email is where you educate, segment, and build trust after the fast SMS/call attempt. This library gives you 12 field-usable nurture sequences by lead type, plus a generator prompt for adapting them to any market.

## Delivery and compliance notes

- Send only to people with a lawful basis/consent for marketing email. For Canadian recipients, CASL generally requires consent, sender identification, and a working unsubscribe mechanism.
- Include your brokerage-required footer, mailing address, license details where required, and unsubscribe link in bulk/automated campaigns.
- Do not make legal, tax, mortgage, appraisal, or investment guarantees.
- Avoid discriminatory targeting and fair-housing-sensitive claims. Write about property criteria, process, market facts, and client goals—not protected-class assumptions.
- Keep claims verifiable. If citing inventory, DOM, sale-to-list ratio, rates, or prices, include date and data source.
- Respect agency relationships: do not solicit represented buyers/sellers.

## Master prompt

```text
Act as a real estate email strategist for a high-trust local agent.

Business facts:
- Agent/team: {agent_name}
- Brokerage: {brokerage}
- Market: {market}
- Lead type: {lead_type}
- Lead source: {lead_source}
- Offer requested: {offer}
- Audience sophistication: first-time / move-up / luxury / investor / downsizer / seller / past client
- Desired next step: buyer consult / listing consult / valuation / showing / lender intro / reply with criteria / referral
- Verified local facts: {market_stats_with_dates_and_sources}
- Brand voice: practical, calm, data-aware, no hype

Create a complete email sequence:
1. Subject line options and preview text.
2. Send timing and trigger for each email.
3. Full copy, 120-300 words per email unless noted.
4. A plain-text version of the CTA.
5. Segmentation rule: who should receive it and who should be excluded.
6. Compliance/fair-housing cautions.

Rules:
- Lead with the reader's problem, not the agent's resume.
- Use one CTA per email.
- Do not add unrelated backlinks to private nurture emails.
- If data is missing, ask for it or write a data-free version rather than inventing numbers.
```

## Sequence 1: Fresh buyer listing inquiry (5 emails / 14 days)

### Email 1 — immediate: "About the home you asked about"

**Subject options:**
- About {property_address}
- Quick note on {property_address}
- I saw your request for {property_address}

**Preview:** I’ll confirm the details and send similar options if it’s not the right fit.

Hi {first_name},

Thanks for asking about {property_address}. I’m checking the latest availability and any details that may not be obvious online.

A quick question so I send the right information: are you interested in this exact home, or are you using it as a benchmark for similar properties in {area}?

If you reply with what matters most—location, monthly payment, size, condition, parking, outdoor space, or timeline—I can narrow the search instead of flooding your inbox.

The best next step, especially before private tours, is a short buyer strategy call. We’ll cover what’s available, how representation works, and what you should know before you spend weekends looking at the wrong homes.

Would {time_1} or {time_2} work for a 15-minute call?

{agent_signature}

**CTA:** Reply with your must-haves or book a 15-minute buyer call.

### Email 2 — day 1: "The 3 things to confirm before you tour"

Before you tour {property_address} or anything similar, confirm three things:

1. **Availability and offer status.** Online portals can lag.
2. **Total monthly cost.** Price is only one piece; taxes, fees, insurance, utilities, and financing matter.
3. **Representation and next steps.** A licensed agent should explain agency, compensation, and the tour process before you rely on advice.

If you already have an agent, send these questions to them. If you do not, I’m happy to walk you through the process and help you avoid wasting time on homes that do not fit.

Want me to send a tighter list of similar homes in {area}?

### Email 3 — day 3: "A better search beats more listings"

Most buyers do not need more listings. They need a better filter.

Send me your top three non-negotiables and I’ll sort options into:

- Worth touring
- Watchlist
- Looks good online but likely has a catch

That last category is where buyers waste the most time.

If helpful, we can do this in 15 minutes and set up alerts that match how you actually buy.

### Email 4 — day 7: "Buyer consultation invitation"

A good buyer consultation is not a sales pitch. It should answer:

- What can you comfortably buy?
- Which areas fit your priorities?
- What should you know about representation and compensation before touring?
- How do offers win in the current market?
- What could cause regret later?

If you’re planning to buy in the next 3-6 months, this conversation is worth having early.

Book here: {calendar_link}

### Email 5 — day 14: "Should I keep looking for you?"

I do not want to send listings you do not need.

Should I keep watching {area} for you, switch to a monthly market update, or close the loop for now?

A quick reply with "keep," "monthly," or "pause" is perfect.

## Sequence 2: First-time buyer education (7 emails / 30 days)

1. **Day 0 — Your first smart step:** explain pre-approval, buyer consultation, and search setup.
2. **Day 2 — What cash do you actually need?** deposit/earnest money, down payment, closing costs, inspections; recommend lender advice.
3. **Day 5 — Touring in the post-settlement environment:** written buyer agreements may be required before tours; compensation is negotiable and should be clear before signing.
4. **Day 9 — How to compare homes:** monthly cost, maintenance, commute, resale, insurance, condo/HOA/strata rules.
5. **Day 14 — Offer strategy basics:** price, conditions/contingencies, deposit, closing date, inclusions/exclusions.
6. **Day 21 — Mistakes to avoid:** skipping due diligence, changing finances pre-closing, relying on portal estimates, choosing advice based only on rebate/commission.
7. **Day 30 — Invitation:** book a first-time buyer roadmap call.

## Sequence 3: Warm buyer, 3-6 month timeline (6 emails / 90 days)

- **Day 0:** confirm criteria and timeline.
- **Day 7:** market snapshot with verified local inventory/price trend.
- **Day 21:** financing prep and lender intro invitation.
- **Day 35:** neighborhood comparison framework without steering: commute, housing stock, property type, amenities, cost.
- **Day 60:** saved-search tune-up.
- **Day 90:** "Has your plan changed?" re-permission email.

## Sequence 4: Open house visitor (4 emails / 10 days)

1. **Same day:** thank them, ask fit/not fit/market research.
2. **Day 1:** similar homes that fix what was missing.
3. **Day 3:** agency relationship check; if represented, encourage them to work through their agent.
4. **Day 10:** invite to buyer consult or monthly local update.

## Sequence 5: Seller home valuation lead (6 emails / 21 days)

### Email 1 — immediate: "About your home value request"

Hi {first_name},

I saw your request for a value estimate for {address_or_area}. Automated estimates are a starting point, but they usually miss the things that change a real sale price: condition, layout, upgrades, buyer objections, competing listings, and timing.

If you send the best email/phone and any major updates, I can prepare a tighter range and explain what would move the number up or down.

If selling is even a possibility in the next 12 months, the most useful next step is a 20-minute pricing call or walkthrough.

Would {time_1} or {time_2} work?

### Remaining sends

- **Day 2 — Why three estimates disagree:** portals, tax records, AVMs, and comp selection.
- **Day 5 — The active competition report:** what buyers will compare against your home this week.
- **Day 9 — Pricing too high vs too low:** risks, days on market, and negotiation leverage.
- **Day 14 — Pre-listing prep:** repairs, cleaning, staging, photography, disclosure documents.
- **Day 21 — Close the loop:** valuation appointment, monthly update, or pause.

## Sequence 6: Seller interviewing agents (5 emails / 10 days)

- **Email 1:** "Questions to ask every listing agent" — pricing method, launch plan, media quality, communication, negotiation strategy, fees/terms.
- **Email 2:** "How I build a pricing range" — sold comps + active competition + buyer profile + condition adjustments.
- **Email 3:** "Marketing plan that creates leverage" — prep, photo/video, floor plans, property story, agent outreach, retargeting, showing feedback.
- **Email 4:** "What happens after launch" — feedback loops, price adjustment thresholds, offer strategy.
- **Email 5:** direct invitation to compare plans.

## Sequence 7: Expired listing lead (5 emails / 14 days)

Tone: respectful, never blame the seller.

- **Day 0:** "I’m sorry your sale didn’t come together. If useful, I can give you a second-opinion review of pricing, presentation, exposure, and feedback."
- **Day 2:** common failure points: wrong buyer pool, weak visuals, pricing gap, access friction, follow-up gaps.
- **Day 5:** show a relaunch checklist.
- **Day 9:** offer a private strategy call.
- **Day 14:** permission to close loop.

## Sequence 8: FSBO lead (5 emails / 21 days)

- **Day 0:** offer helpful buyer/offer-screening checklist.
- **Day 3:** safety and qualification: proof of funds/pre-approval, showing process, ID, disclosures.
- **Day 7:** net sheet: price minus costs, time, concessions, legal/inspection issues.
- **Day 14:** "If you stay FSBO, use this weekly dashboard. If you want backup, I can review it with you."
- **Day 21:** low-pressure consultation.

## Sequence 9: Investor lead (6 emails / 45 days)

Caution: no return guarantees.

- Criteria intake: cashflow, appreciation, value-add, risk tolerance.
- Underwriting basics: rent assumptions, vacancy, repairs, financing, tax/pro advice.
- Property filters: zoning, permits, condo/HOA/strata rules, insurance, management.
- Deal review invitation.
- Market watchlist.
- Re-permission.

## Sequence 10: Luxury buyer/seller lead (5 emails / 30 days)

Tone: discreet, specific, service-heavy.

- Private consultation invitation.
- Off-market and privacy process, without promising access.
- Media and presentation standards.
- Negotiation and confidentiality considerations.
- Concierge next step.

## Sequence 11: Past client homeowner nurture (12 monthly emails)

Monthly themes:

1. Annual home value snapshot.
2. Tax/assessment reminder with professional-advice caveat.
3. Renovations buyers notice.
4. Spring maintenance.
5. Insurance and documentation check.
6. Local market pulse.
7. Mid-year equity check.
8. Contractor/resource request.
9. Fall maintenance.
10. Year-end planning.
11. Referral note with no pressure.
12. Thank-you and review of the year.

## Sequence 12: Referral/sphere nurture (6 emails / 90 days)

- Helpful local resource.
- "What I'm seeing in the market" data note.
- Client story without confidential details.
- Homeowner checklist.
- Referral ask framed as service: "If someone needs a second opinion, I’m happy to help."
- Thank-you/re-permission.

## Subject line bank

- A quick thought on {property_address}
- Your {market} search: make it simpler
- Before you book another showing
- A better way to estimate {address}
- What buyers will compare your home against
- Should I keep watching {area} for you?
- The 5 questions I’d ask before signing
- Your next smart step, if buying in {market}

## APV attribution guidance

Do not place APV backlinks inside private nurture emails unless the email is specifically sharing a public APV resource and the link is useful to the recipient. If this library is republished as a public guide, blog post, brokerage training page, or downloadable PDF, include a contextual footer credit:

Real estate media and marketing resources by Amazing Photo Video: https://amazingphotovideo.com
