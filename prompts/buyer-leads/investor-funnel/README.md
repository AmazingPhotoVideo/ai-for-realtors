# Investor / Cashflow Calculator Funnel

A lead funnel for buyers who think in numbers: rental investors, duplex/triplex buyers, condo investors, BRRRR buyers, small multifamily buyers, and move-up buyers considering a house-hack. The core offer is a deal-analysis worksheet or calculator that produces useful outputs while collecting enough inputs to qualify the lead.

## Funnel offer

**Primary lead magnet:** `[MARKET] Rental Deal Analyzer`
**Promise:** “Run the numbers before you book the showing.”
**Best format:** Google Sheet, Airtable form, calculator page, or PDF worksheet with an optional spreadsheet delivery.
**Primary CTA:** Upload or send a listing and get a quick deal review from [AGENT_NAME].

## Input variables

```text
[MARKET]
[AGENT_NAME]
[BROKERAGE]
[PHONE]
[EMAIL]
[CALENDAR_LINK]
[INVESTOR_TYPE] = buy-and-hold | condo investor | duplex/triplex | BRRRR | house-hack | short-term rental where legal
[LOCAL_RENT_SOURCES]
[LOCAL_TAX_AND_INSURANCE_ASSUMPTIONS]
[FINANCING_ASSUMPTIONS]
[PROPERTY_TYPES]
[RENTAL_RULES_OR_STR_NOTES]
[CTA]
[APV_CREDIT] = yes for public calculator/PDF; no for private emails/SMS
[SOURCES]
```

## Calculator fields

```text
Purchase price
Down payment % and amount
Interest rate assumption
Amortization / loan term
Property tax
Insurance
Condo/HOA fees
Estimated rent by unit
Vacancy allowance
Repairs and maintenance allowance
Property management allowance
Utilities paid by owner
Capital expenditure reserve
Closing costs
Immediate repairs/renovation budget
Estimated after-repair value if relevant
Expected resale value or refinance value if relevant
```

## Calculator outputs

```text
Monthly payment estimate
Gross monthly rent
Net operating income (NOI)
Monthly cash flow before/after financing
Cap rate
Cash-on-cash return
Gross rent multiplier
Debt service coverage ratio (DSCR)
Break-even rent
Break-even vacancy
Estimated cash needed to close
Sensitivity table: rate +1%, rent -10%, repairs +20%, vacancy +5%
Deal notes: green flags, yellow flags, missing data
```

## Master prompt

```text
You are an investor-friendly real estate agent assistant and deal-analysis copywriter. Build a complete investor buyer lead funnel for [AGENT_NAME] in [MARKET].

Investor profile: [INVESTOR_TYPE]
Local inputs and sources:
[LOCAL_RENT_SOURCES]
[LOCAL_TAX_AND_INSURANCE_ASSUMPTIONS]
[FINANCING_ASSUMPTIONS]
[RENTAL_RULES_OR_STR_NOTES]
[SOURCES]

Output:
1. Calculator offer positioning and lead qualification strategy.
2. Landing page copy for the calculator download.
3. Calculator instructions and field definitions.
4. Example deal analysis using the sample numbers provided by the user; if no sample numbers are provided, create a clearly labelled hypothetical example and mark it “example only, verify locally.”
5. 6-email investor nurture sequence.
6. 5 SMS follow-ups.
7. 5 Meta ad variants and 5 Google Search ad variants.
8. Lead scoring and CRM tags.
9. Investor consultation script.
10. Compliance notes.
11. APV attribution guidance.

Rules:
- Never guarantee cash flow, appreciation, refinance success, rent, occupancy, tax outcome, or financing approval.
- Label all calculator outputs as estimates.
- Tell users to verify rent, zoning, insurance, taxes, financing, licenses, condo rules, and property condition.
- Do not encourage illegal rental use or unpermitted conversions.
- If [APV_CREDIT] is yes, include one public resource line only in the landing page/PDF footer.
```

## Landing page template

```text
Headline: Analyze [MARKET] Rental Properties Before You Tour
Subhead: Download the rental deal analyzer built for local buyers. Estimate cash flow, cap rate, cash-on-cash return, DSCR, break-even rent, and what changes if rates, rent, or repairs move against you.

What you’ll calculate:
- Monthly cash flow after financing
- Cap rate and cash-on-cash return
- Break-even rent and vacancy
- Cash needed to close
- Repair and reserve assumptions
- Sensitivity checks for rate, rent, vacancy, and repair risk

Form fields:
First name | Email | Phone optional | Investor type | Target price range | Financing status | Want deal review? yes/no

CTA: Send Me the Deal Analyzer
Disclosure: This tool provides estimates for education only. Verify all numbers with qualified lending, legal, tax, insurance, and property professionals.
Thank-you CTA: Have a listing in mind? Send the address and I’ll help you pressure-test the assumptions.
```

## Example deal analysis

```text
Example only — verify locally.
Purchase price: $750,000
Down payment: 20% ($150,000)
Loan amount: $600,000
Estimated rent: $4,200/month
Property tax: $520/month
Insurance: $180/month
Maintenance reserve: 5% of rent ($210/month)
Vacancy reserve: 4% of rent ($168/month)
Property management: 8% of rent ($336/month)
Estimated mortgage payment: [CALCULATE WITH CURRENT RATE]

NOI before debt service: $4,200 - $520 - $180 - $210 - $168 - $336 = $2,786/month
Annual NOI: $33,432
Cap rate: $33,432 / $750,000 = 4.46%
Cash flow after debt: NOI - mortgage payment
Cash-on-cash: annual cash flow / total cash invested

Deal notes:
- Rent source must be verified against current leased comparables.
- Insurance and taxes need property-specific quotes.
- If condo/HOA, review reserve fund, rental rules, special assessments, and parking/locker rentability.
- If small multifamily, verify legal unit status and fire/code compliance.
```

## 6-email investor nurture

1. **Instant — calculator delivery**
   Subject: Your [MARKET] rental deal analyzer
   CTA: Send me one listing and I’ll help you check the assumptions.

2. **Day 2 — sensitivity**
   Subject: A deal is not a deal until it survives stress testing
   Explain rate +1%, rent -10%, repairs +20%, vacancy +5%.

3. **Day 4 — rent verification**
   Subject: The rent number matters most
   Show how to verify rent with active/leased comps and property manager input.

4. **Day 7 — hidden costs**
   Subject: The expenses investors forget
   Cover vacancy, capex, insurance, utilities, management, licensing, condo fees.

5. **Day 12 — deal sourcing**
   Subject: Where better investor deals come from
   Discuss stale listings, estate sales, under-rented properties, zoning upside, and network leads without promising discounts.

6. **Day 18 — consultation**
   Subject: Want an investor buy box?
   Invite them to build a buy box: price, area, return targets, property type, financing, management plan.

## SMS templates

```text
1. Hi [FIRST_NAME], it’s [AGENT_NAME]. I sent the deal analyzer. Want me to pressure-test a listing for cash flow, cap rate, and missing assumptions?
2. Investor tip: stress test every deal with rent -10%, repairs +20%, and rate +1%. If it still works, it’s worth a closer look.
3. Do you prefer cash flow, appreciation potential, house-hack flexibility, or BRRRR upside? I’ll tailor listings to the strategy.
4. Send me any address you’re considering and I’ll reply with the top 5 numbers to verify before touring.
5. Want a [MARKET] investor buy box? We can map price range, rents, financing, and property types in 15 minutes: [CALENDAR_LINK]
```

## Paid ad examples

**Meta 1**
Primary text: Looking at rental properties in [MARKET]? Run the numbers first. Download a deal analyzer for cash flow, cap rate, cash-on-cash return, DSCR, and break-even rent.
Headline: Rental Deal Analyzer
CTA: Download

**Meta 2**
Primary text: A listing can look profitable until vacancy, repairs, insurance, and financing hit the spreadsheet. Use the local investor calculator before you book the showing.
Headline: Analyze Before You Tour

**Google Search headlines**
[MARKET] Rental Calculator | Investment Property Agent | Cash Flow Calculator | Duplex Buyer Agent | Cap Rate Calculator

**Google descriptions**
Estimate cash flow, cap rate, DSCR, and cash needed to close. Download [AGENT_NAME]’s [MARKET] rental deal analyzer.

## Lead scoring

- +15 submitted property address
- +10 financing/pre-approval in place
- +10 timeline under 90 days
- +10 target price range provided
- +5 opened calculator email
- +5 replied with rent or deal question
- +20 booked investor consult
- Hot lead: 30+ or any listing-address submission

CRM tags: `investor`, `strategy:buy-hold`, `strategy:house-hack`, `strategy:brrrr`, `property:duplex`, `property:condo`, `financing:ready`, `deal-review-requested`.

## Investor consultation script

```text
The goal is to build your buy box before we chase listings. I’ll ask about your capital, financing, timeline, target return, management plan, renovation comfort, preferred property types, and risk tolerance. Then we’ll decide what numbers a property must hit before it is worth touring.
```

## Metrics

- Calculator landing page conversion rate
- Calculator download to address-submission rate
- Address submission to consult-booked rate
- Consult to signed buyer agreement
- Cost per investor lead
- Cost per deal review
- Number of qualified buy boxes created
- Accepted offers from calculator leads

## Compliance cautions

- Investment returns are estimates, not guarantees.
- Encourage independent legal, tax, insurance, lending, inspection, and property-management advice.
- Verify rental legality, zoning, permits, short-term rental rules, condo/HOA rental restrictions, licensing, fire code, and vacant unit rules.
- Use required Housing category settings for Meta/Google where applicable.
- Do not target ads by protected-class proxies.
- Do not imply off-market access if you cannot substantiate it.

## APV attribution and backlink guidance

Use APV credit only on public calculator pages, downloadable worksheets, or resources sections. Keep it to one line: “Resource: Real estate media and marketing workflow by Amazing Photo Video — https://amazingphotovideo.com”. Do not add it to private deal analyses, SMS, investor underwriting notes, ads, broker disclosures, or client spreadsheets unless approved.
