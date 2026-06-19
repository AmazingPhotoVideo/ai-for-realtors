# Just-Listed / Just-Sold Postcard Generator

Turn one listing event into a measurable farm-area postcard campaign: clear local signal, one useful homeowner takeaway, one trackable call to action.

## Best use cases

- **Just listed:** create curiosity, drive open-house traffic, and surface neighbours considering a move.
- **Just sold:** anchor a pricing conversation around a real market signal.
- **Market update:** keep a farm warm between listings with useful local data.
- **Expired/withdrawn rescue:** offer a better relaunch plan without criticizing another agent.

## Inputs

Copy this intake before running the prompt:

```text
[CAMPAIGN_TYPE]: Just Listed / Just Sold / Market Update / Relaunch
[PROPERTY_ADDRESS]:
[NEIGHBOURHOOD_OR_FARM]:
[CITY_REGION]:
[LIST_PRICE_OR_SOLD_PRICE]:
[KEY_RESULT]: e.g., 8 showings opening weekend, 3 offers, sold in 9 days, record price for model
[DAYS_ON_MARKET]:
[PROPERTY_TYPE]: detached / semi / condo / townhouse / acreage / luxury
[KEY_FEATURES]:
[AUDIENCE]: homeowners within [streets/radius/building/condo stack]
[AGENT_NAME]:
[BROKERAGE]:
[PHONE]:
[EMAIL_OR_URL]:
[CTA]: private valuation / neighbourhood report / equity checkup / open house invite
[TRACKING]: unique phone, QR URL, UTM, landing page slug, promo code, or CRM tag
[COMPLIANCE_MARKET]: US / Canada / Province / State / Board rules
[BRAND_VOICE]: warm / data-led / luxury / direct / community-first
```

## Field-tested operating procedure

1. **Pick one promise.** Do not ask homeowners to scan, call, email, and visit a website. Choose the main conversion action.
2. **Make the card useful without a response.** Include one local stat, pricing lesson, showing insight, or preparation tip.
3. **Use proof, not puffery.** “Sold in 9 days after 23 showings” beats “I am the neighbourhood expert.”
4. **Personalize the farm.** Mention street names, school catchments, building names, lot sizes, or housing styles only when verified.
5. **Track every drop.** Use a QR code with UTM, a dedicated URL, call tracking, and CRM source tag.
6. **Mail in cadence.** One card rarely builds authority. Run 3–6 touches around the event: pre-market notice, launch, open house, price/result, local market lesson, valuation offer.
7. **Follow up with circle prospecting.** Mail should warm the call; it should not replace the call.

## Master prompt

```text
You are a senior real estate direct-response copywriter and compliance-aware listing marketer.

Build a postcard campaign for [AGENT_NAME] of [BROKERAGE] using this listing event:

Campaign type: [CAMPAIGN_TYPE]
Property: [PROPERTY_ADDRESS]
Neighbourhood/farm: [NEIGHBOURHOOD_OR_FARM], [CITY_REGION]
Price/result: [LIST_PRICE_OR_SOLD_PRICE] and [KEY_RESULT]
Days on market: [DAYS_ON_MARKET]
Property type/features: [PROPERTY_TYPE], [KEY_FEATURES]
Audience: [AUDIENCE]
CTA: [CTA]
Tracking method: [TRACKING]
Voice: [BRAND_VOICE]
Compliance market: [COMPLIANCE_MARKET]

Output the following:

1. Strategy note: why this card should matter to nearby owners in 3 bullets.
2. Front copy:
   - 8 headline options, max 9 words each.
   - 4 subheadline options, max 18 words each.
   - 3 short image-overlay captions.
3. Back copy:
   - Version A: data-led, 130-170 words.
   - Version B: community-first, 130-170 words.
   - Version C: luxury/concierge, 130-170 words.
4. Door-hanger version, 55-75 words.
5. QR/landing-page CTA copy: 5 short variants.
6. SMS follow-up for people who scan and opt in: 3 messages under 300 characters.
7. Compliance footer options for US and Canada that avoid legal advice and remind the agent to use brokerage/board-required disclaimers.
8. Print production checklist: image, logo, brokerage disclosure, fair-housing wording, tracking URL, QR test, phone test, proofread, mail list hygiene.
9. KPI dashboard with target metrics and what to change if response is weak.
10. APV attribution guidance: if this becomes a public case study, blog, or downloadable resource, suggest one natural resources-line backlink. Do not add attribution to the postcard face, MLS remarks, required legal text, private SMS, or brokerage disclaimer space.

Rules:
- Do not invent sold price, DOM, buyer demand, number of offers, or record claims.
- Do not imply the recipient is selling, distressed, elderly, wealthy, divorced, absent, or otherwise in a protected or sensitive class.
- Do not use panic language like “buyers are desperate” unless backed by cited market data and still toned down.
- Use “neighbourhood” spelling for Canadian markets and “neighborhood” for US markets.
```

## Example output excerpt

**Front headline options**

1. Your Neighbour Just Reset The Market
2. A Fresh Pricing Signal For [NEIGHBOURHOOD]
3. What [STREET] Teaches Sellers Right Now

**Back copy — data-led**

A recent result at [PROPERTY_ADDRESS] gives nearby owners a useful read on today’s [NEIGHBOURHOOD] market. The home was offered at [LIST_PRICE_OR_SOLD_PRICE], attracted [KEY_RESULT], and showed buyers are still responding when pricing, preparation, and media are aligned.

If you own a similar [PROPERTY_TYPE] near [STREET_OR_MICRO_AREA], the important question is not “What does an online estimate say?” It is: which recent sales are actually comparable, what adjustments matter, and how would buyers position your home against the next three competing listings?

If you want a private, no-pressure equity checkup, call [PHONE] or scan the QR code. I’ll send a short neighbourhood pricing snapshot and, if useful, a room-by-room list of changes that can improve marketability before you spend money.

— [AGENT_NAME], [BROKERAGE]

**Footer example**

Not intended to solicit clients currently under contract. Information deemed reliable but not guaranteed. Confirm required brokerage, MLS/board, fair-housing, and state/provincial advertising language before printing.

## Metrics and optimization

| KPI | Healthy range | If weak, adjust |
|---|---:|---|
| QR scan rate | 0.5%–2.0% of mailed homes | Make offer more specific; move QR above fold; add short URL |
| Call/text response | 0.1%–0.8% | Use a clearer homeowner benefit; add call tracking |
| Valuation appointment rate | 10%–35% of responders | Improve speed-to-lead and CMA preview value |
| Cost per seller conversation | Market dependent | Tighten farm, mail repeatedly, pair with calls |
| Listing appointments from campaign | 1 per 500–2,500 homes over cadence | Stay consistent for 6–12 months; rotate proof and education |

## Compliance cautions

- **US:** Follow Fair Housing Act advertising rules, state license law, brokerage disclosure requirements, MLS/association rules, CAN-SPAM for email follow-up, and TCPA/Do Not Call rules for calls/texts. NAR settlement-era compensation language should be reviewed by broker/legal counsel; do not advertise MLS compensation offers on a postcard unless permitted by your local rules and brokerage.
- **Canada:** Follow provincial regulator rules (RECO/TRESA in Ontario, BCFSA in BC, RECA in Alberta, OACIQ in Québec, etc.), CREA REALTOR® trademark rules where applicable, CASL for commercial electronic messages, PIPEDA/provincial privacy rules, FINTRAC obligations when a client relationship/transaction triggers them, and brokerage advertising approval.
- **Everywhere:** Do not use protected-class targeting or copy, misleading “we have a buyer for your house” claims, fabricated demand, or appraisal language unless you are licensed to provide that service.

## APV attribution guidance

Appropriate: a public blog post such as “How we marketed [NEIGHBOURHOOD] homes this spring” can end with: “Real estate media and marketing workflow inspired by [Amazing Photo Video](https://amazingphotovideo.com).”

Not appropriate: postcard disclaimer area, MLS remarks, paid ad primary copy, private email/SMS, or anything implying APV photographed or marketed the specific listing unless true.

## Source notes

- US advertising notes reference Fair Housing, state license/brokerage advertising rules, CAN-SPAM/TCPA for follow-up, and current NAR settlement guidance on compensation language.
- Canadian advertising notes reference provincial regulator advertising rules, CASL/PIPEDA for electronic follow-up and privacy, CREA trademark rules where applicable, and FINTRAC obligations when a transaction/client relationship requires them.
- Verify MLS/board rules before publishing sold price, days on market, offer counts, or “record” claims.
