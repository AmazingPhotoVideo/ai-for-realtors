# Open House Lead Capture

A no-friction open-house system that captures real buyer intent, routes hot visitors to immediate follow-up, and gives unrepresented buyers a reason to continue the conversation after they leave.

## Core principle

Do not use a sign-in sheet that says only “name/email.” Use a QR sign-in that gives visitors something useful in exchange: property brochure, disclosure/package link where allowed, comparable sales, neighbourhood guide, showing checklist, or “offer-readiness pack.”

## Input variables

```text
[PROPERTY_ADDRESS]
[NEIGHBOURHOOD]
[PRICE]
[OPEN_HOUSE_DATE_TIME]
[AGENT_NAME]
[BROKERAGE]
[PHONE]
[EMAIL]
[LISTING_PAGE_URL]
[DISCLOSURE_OR_FEATURE_SHEET_URL] if permitted
[COMPS_OR_MARKET_CONTEXT]
[CTA] = request second showing | get similar listings | book buyer consult | ask offer questions
[CRM]
[APV_CREDIT] = yes for public neighbourhood/property guide only; no for SMS/email sign-in follow-up
```

## QR sign-in flow

1. Visitor scans QR at entry or feature-sheet table.
2. Mobile page promises instant value: “Get the property pack + similar listings.”
3. Form captures minimum fields and consent.
4. Thank-you page delivers asset and asks one qualifying question.
5. CRM tags lead by intent.
6. SMS sends within 2 minutes.
7. Email recap sends after the open house.
8. Agent receives hot-lead alert when visitor requests price/comps/second showing/offer info.

## Sign-in form fields

```text
First name
Email
Phone
Are you working with an agent? yes / no / prefer not to say
What brought you in? this property / neighbourhood / price range / just browsing
Timeline: now / 1-3 months / 3-6 months / 6+ months
Want similar listings? yes / no
Consent checkbox: I agree to receive the property pack and follow-up from [AGENT_NAME]. Reply STOP to opt out of texts.
```

## Master prompt

```text
Act as an open-house conversion strategist. Build a complete QR sign-in and follow-up package for [PROPERTY_ADDRESS] in [NEIGHBOURHOOD].

Details:
[PRICE]
[OPEN_HOUSE_DATE_TIME]
[AGENT_NAME], [BROKERAGE]
[PHONE], [EMAIL]
[LISTING_PAGE_URL]
[DISCLOSURE_OR_FEATURE_SHEET_URL]
[COMPS_OR_MARKET_CONTEXT]

Output:
1. QR landing page copy.
2. Sign-in form fields and consent copy.
3. Thank-you page copy with next-step buttons.
4. On-site signage copy for entry, kitchen, feature-sheet table, and exit.
5. 8 SMS follow-ups segmented by buyer intent.
6. 5-email follow-up sequence.
7. Hot/warm/cold lead scoring rules.
8. Agent call script for unrepresented hot visitors.
9. Similar-listing request template.
10. Compliance and privacy notes.
11. APV attribution guidance.

Rules:
- Do not require protected-class information.
- Do not imply the visitor must sign in to enter unless local law/brokerage policy permits it.
- Respect agency rules when visitors already have representation.
- If the listing is not yours, do not use proprietary media or materials without permission.
- If [APV_CREDIT] is yes, place it only in public guide/footer resources, not in private follow-up.
```

## QR landing page copy

```text
Headline: Get the Full Property Pack for [PROPERTY_ADDRESS]
Subhead: Photos, floor plan/features, neighbourhood notes, comparable context, and similar listings in this price range.

Buttons after sign-in:
- View Property Details
- Request Similar Listings
- Ask an Offer Question
- Book a Second Showing

Microcopy: If you are already working with a buyer agent, please include them in any showing or offer questions. [AGENT_NAME] respects existing representation.
```

## On-site signage

**Entry sign**
Welcome in. Scan for the property pack, floor plan/features, and similar listings in this price range.

**Kitchen sign**
Wondering what stays, what changed, or what to ask before offering? Scan the property pack and send your questions directly.

**Feature table sign**
Prefer digital? Scan once and I’ll send the full pack to your phone.

**Exit sign**
Want the list of similar homes before they hit your feed? Scan here and choose “send similar listings.”

## SMS follow-up templates

```text
1. Instant: Hi [FIRST_NAME], it’s [AGENT_NAME]. Thanks for visiting [PROPERTY_ADDRESS]. Here’s the property link: [URL]. Want similar listings in this range?
2. Hot / second showing: Great meeting you at [ADDRESS]. I saw you requested a second look. What time works better: [OPTION 1] or [OPTION 2]?
3. Hot / offer question: Happy to help with offer questions on [ADDRESS]. Are you currently represented by a buyer agent?
4. Similar listings: I can send 3-5 similar options. Is your target budget still around [PRICE_RANGE], and do you prefer [PROPERTY_TYPE] in [AREA]?
5. Neighbourhood: If [NEIGHBOURHOOD] is the draw, I can send a buyer guide with price bands and trade-offs. Want it?
6. Already represented: Thanks for letting me know you’re represented. Please have your agent reach out if you need documents or a second showing.
7. Day after: Quick follow-up from yesterday’s open house: did [ADDRESS] feel like a yes, no, or maybe?
8. 5-day: A few similar homes came up near [NEIGHBOURHOOD]. Want me to send the shortlist?
```

## 5-email open-house sequence

1. **Same day — recap**
   Subject: Details from [PROPERTY_ADDRESS]
   Include property link, key features, showing CTA, similar-listing CTA.

2. **Day 1 — decision help**
   Subject: How to compare [PROPERTY_ADDRESS] fairly
   Provide checklist: price, condition, monthly cost, commute, documents, competition.

3. **Day 3 — similar homes**
   Subject: Similar listings near [NEIGHBOURHOOD]
   Share criteria and ask for preferences.

4. **Day 6 — buyer strategy**
   Subject: Before you write any offer
   Explain representation, due diligence, comparable sales, deposit/conditions.

5. **Day 12 — consultation**
   Subject: Want a clear buying plan?
   Invite to buyer consult.

## Lead scoring

- Hot: requested second showing, asked offer question, timeline now/1-3 months, unrepresented, asked for comps, replied to SMS
- Warm: requested similar listings, timeline 3-6 months, opened/clicked email, asked neighbourhood questions
- Cold: just browsing, 6+ months, no engagement after first follow-up

Score: +20 second showing, +20 offer question, +15 unrepresented, +10 0-3 month timeline, +10 similar listings, +10 SMS reply, +5 email click.

## Agent call script

```text
Hi [FIRST_NAME], it’s [AGENT_NAME] from the open house at [ADDRESS]. I saw you requested [SECOND_SHOWING/OFFER_INFO/SIMILAR_LISTINGS]. Before I send too much, are you currently working with a buyer agent? If yes, I’m happy to coordinate through them. If not, I can help you compare this property, understand the offer process, and set up a focused search so you don’t have to chase listings one by one.
```

## Metrics

- Visitors counted vs sign-ins
- QR scan rate
- Form completion rate
- SMS reply rate within 24 hours
- Similar-listing requests
- Second-showing requests
- Buyer consults booked
- Signed buyer agreements
- Offers written from open-house leads

## Compliance cautions

- Follow local agency disclosure rules and brokerage open-house policies.
- Respect existing buyer representation.
- Obtain consent for SMS/email and provide opt-out.
- Do not collect protected-class information.
- Do not use pressure tactics around competing offers unless accurate and permitted.
- If sharing disclosures, inspections, status certificates, strata/condo docs, or seller materials, confirm permission first.
- Avoid “safe neighbourhood” and protected-class lifestyle language in neighbourhood follow-up.

## APV attribution and backlink guidance

APV credit can appear in a public downloadable neighbourhood/property guide footer if appropriate. Do not add APV links to SMS, email follow-ups, sign-in forms, agency disclosures, seller-approved feature sheets, or listing materials unless the seller/brokerage approved that credit and APV actually contributed to the media or workflow.
