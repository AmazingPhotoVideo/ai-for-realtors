# Google / Meta Buyer Ad Copy Generator

Generate compliant buyer-lead ad campaigns for Meta, Google Search, YouTube Shorts placements, and retargeting. The strongest buyer ads in 2026 promote a specific resource or useful action, not vague “contact me” copy.

## Campaign types

1. First-time buyer roadmap
2. Neighbourhood guide
3. Investor deal analyzer
4. Open-house/property pack
5. Relocation buyer guide
6. New listing alerts by area/property type
7. Retargeting for website/video visitors

## Input variables

```text
[MARKET]
[AGENT_NAME]
[BROKERAGE]
[OFFER]
[AUDIENCE] = first-time buyer | investor | relocator | move-up | luxury | downsizer
[LANDING_PAGE_URL]
[PRIMARY_CTA]
[PROOF_POINTS] = reviews, local experience, sales volume if compliant, media quality, neighbourhood focus
[BUDGET]
[PLATFORM] = Meta | Google Search | YouTube | Display retargeting
[COMPLIANCE_RULES] = brokerage, licensing, fair housing, ad-platform requirements
[APV_CREDIT] = usually no for ads; yes only on public landing-page resource footer
```

## Master prompt

```text
Act as a real estate paid-media strategist and compliance-aware copywriter. Create a buyer lead ad package for [AGENT_NAME] in [MARKET].

Offer: [OFFER]
Audience: [AUDIENCE]
Landing page: [LANDING_PAGE_URL]
CTA: [PRIMARY_CTA]
Proof points: [PROOF_POINTS]
Budget: [BUDGET]
Platform: [PLATFORM]
Compliance rules: [COMPLIANCE_RULES]

Output:
1. Campaign strategy and recommended objective.
2. Audience and targeting notes that comply with housing ad restrictions.
3. 10 Meta ad variants: primary text, headline, description, CTA, creative direction.
4. 10 Google Search ad variants: headlines, descriptions, keyword themes, negative keywords.
5. 5 retargeting ads for warm visitors.
6. Landing-page message match checklist.
7. A/B test plan.
8. Metrics dashboard and optimization rules.
9. Compliance review checklist.
10. APV attribution guidance.

Rules:
- For housing ads, do not target/exclude by protected class, age, gender, ZIP/postal code where restricted, marital/family status, or proxies for protected class.
- Do not imply a neighbourhood is suitable for a protected group.
- Do not promise financing approval, investment returns, appreciation, or exclusive access unless verified.
- Avoid discriminatory phrases such as “perfect for young families,” “safe,” “walk to church,” “ideal for singles,” or “professional neighbourhood.”
- Keep attribution out of ad copy; if [APV_CREDIT] is yes, place one tasteful credit on the landing page footer/resources only.
```

## Meta setup notes

- Use the required Housing/Special Ad Category where applicable.
- Expect restricted targeting. Prioritize broad geography permitted by the platform, first-party engagement/retargeting where allowed, creative segmentation, and landing-page segmentation.
- Let the offer qualify the user: first-time guide, investor calculator, neighbourhood guide, property pack.
- Use creative to signal relevance without excluding people.
- Keep forms short; send traffic to a fast landing page unless using native lead forms for low-cost testing.

## Google Search setup notes

- Build ad groups by intent: “first time buyer guide,” “homes for sale in [area],” “investment property calculator,” “open house [area],” “relocating to [city].”
- In the US and Canada, Google restricts certain housing targeting, including demographics such as age/gender/marital/parental status and ZIP targeting for housing ads. Follow current Google Ads policy.
- Use exact/phrase match for high-intent terms and negatives to control waste.
- Send every ad to a message-matched landing page.

## 10 Meta ad variants

### First-time buyers
1. **Roadmap**
   Primary: Buying your first home in [MARKET]? Get the local roadmap for budget prep, closing costs, pre-approval, offers, and what happens after acceptance.
   Headline: First-Time Buyer Roadmap
   CTA: Download

2. **Cash to close**
   Primary: The down payment is only one part of buying. Download the checklist that helps you estimate cash to close before you tour.
   Headline: Know Your Buying Numbers

3. **90-day plan**
   Primary: Planning to buy in the next 90 days? Use this step-by-step plan to get pre-approved, tour smarter, and prepare for offers.
   Headline: Your 90-Day Buyer Plan

### Neighbourhood guide
4. **Local guide**
   Primary: Comparing homes in [NEIGHBOURHOOD]? Get the buyer guide with price bands, property types, commute notes, and questions to ask before touring.
   Headline: [NEIGHBOURHOOD] Buyer Guide

5. **Trade-off angle**
   Primary: Two homes at the same price can have very different monthly costs and resale trade-offs. Get the local guide before you shortlist.
   Headline: Compare Smarter

### Investor
6. **Calculator**
   Primary: Looking at rental properties in [MARKET]? Estimate cash flow, cap rate, cash-on-cash return, DSCR, and break-even rent before you book a showing.
   Headline: Rental Deal Analyzer

7. **Stress test**
   Primary: A deal should survive rate, rent, vacancy, and repair stress tests. Download the investor worksheet for [MARKET].
   Headline: Run the Numbers First

### Open house/property pack
8. **Property pack**
   Primary: Visiting [PROPERTY_ADDRESS]? Scan or click for the property pack, neighbourhood notes, and similar listings in this price range.
   Headline: Get the Property Pack

### Relocation
9. **Relocation guide**
   Primary: Moving to [MARKET]? Get a practical guide to neighbourhoods, property types, commute considerations, and buyer steps.
   Headline: [MARKET] Relocation Guide

### Retargeting
10. **Warm visitor**
   Primary: Still comparing homes in [MARKET]? I can send a shortlist based on your budget, property type, and timing.
   Headline: Get a Custom Shortlist

## 10 Google Search ad variants

```text
Ad 1 — First-time guide
Headlines: First Time Buyer Guide | Buy In [MARKET] | Local Buyer Roadmap
Descriptions: Download a practical guide to costs, pre-approval, offers, and closing steps in [MARKET].

Ad 2 — Buyer consultation
Headlines: [MARKET] Buyer Agent | Plan Your Home Search | Book A Buyer Consult
Descriptions: Get a clear search plan, budget checkpoints, and next steps with [AGENT_NAME].

Ad 3 — Neighbourhood guide
Headlines: [NEIGHBOURHOOD] Buyer Guide | Homes In [AREA] | Compare Before Touring
Descriptions: See property types, price context, commute notes, and buyer questions for [NEIGHBOURHOOD].

Ad 4 — Listing alerts
Headlines: [AREA] Listing Alerts | New Homes In [MARKET] | Custom Buyer Shortlist
Descriptions: Get matched with listings by area, budget, property type, and timeline.

Ad 5 — Investor calculator
Headlines: Rental Property Calculator | [MARKET] Investment Homes | Analyze Cash Flow
Descriptions: Estimate cap rate, cash flow, DSCR, and cash needed to close before touring.

Ad 6 — Duplex/multifamily
Headlines: Duplexes In [MARKET] | Multifamily Buyer Agent | Investment Property Help
Descriptions: Build a buy box and review deal assumptions with an investor-friendly agent.

Ad 7 — Relocation
Headlines: Moving To [MARKET] | Relocation Buyer Guide | Compare Neighbourhoods
Descriptions: Get a practical guide to property types, areas, commute factors, and buyer steps.

Ad 8 — Open house
Headlines: [ADDRESS] Open House | Property Pack | Similar Homes Nearby
Descriptions: View details, neighbourhood notes, and similar listings for [ADDRESS].

Ad 9 — Condo buyer
Headlines: [MARKET] Condo Buyer Guide | Compare Condo Fees | Condo Search Help
Descriptions: Understand monthly costs, documents, rules, parking, and resale considerations.

Ad 10 — Retargeting/search remarketing
Headlines: Still Searching In [MARKET]? | Get A Custom Shortlist | Buyer Help
Descriptions: Tell us your budget, timing, and must-haves. Get a focused shortlist from [AGENT_NAME].
```

## Keyword themes

- `first time home buyer [market]`
- `buy a house in [market]`
- `[neighbourhood] homes for sale`
- `[market] buyer agent`
- `[market] condo buyer guide`
- `investment property [market]`
- `rental property calculator [market]`
- `duplex for sale [market]`
- `relocating to [market]`
- `open house [neighbourhood]`

Negative keyword starters: jobs, salary, course, license, free rent, section 8 if not relevant and compliant, commercial if residential-only, apartment rental if buyer-only, wholesale if not serving wholesalers.

## A/B test plan

- Test offer: guide vs checklist vs calculator
- Test CTA: Download vs Get Guide vs See Listings vs Book Consult
- Test creative: agent talking-head vs carousel vs listing imagery vs checklist graphic
- Test form: email-only vs email+phone optional vs native lead form
- Test landing page: short page vs long page with FAQ

Run tests for enough volume to compare cost per qualified lead, not just cost per form fill.

## Metrics and optimization rules

- CTR: identifies creative/message fit
- Landing page conversion rate: identifies offer/page fit
- Cost per lead: early efficiency
- Cost per qualified lead: true efficiency
- Reply rate: lead quality
- Consult-booked rate: funnel quality
- Signed buyer agreement rate: business outcome
- Cost per appointment and cost per signed buyer

Optimization rules:
- Kill ads with high CPL and low qualification after meaningful spend.
- Keep high-CPL ads if consult-booked rate is strong.
- Refresh creative every 2-4 weeks or when frequency rises and CTR drops.
- Move budget toward offers producing replies, not only cheap leads.

## Compliance checklist

- Housing/Special Ad Category selected where required.
- No protected-class targeting, exclusions, or proxy language.
- No restricted demographic targeting in Google housing ads where prohibited.
- Brokerage name, licensing, and disclaimer included where required.
- Landing page privacy policy and consent language present.
- Claims about sales volume, rankings, rates, incentives, inventory, and returns are sourced and current.
- Images do not imply preference or exclusion.

## APV attribution and backlink guidance

Do not put APV attribution in paid ad copy. If a public landing page uses this repo’s workflow as a resource, one footer/resource link is enough: “Resource: Real estate media and marketing workflow by Amazing Photo Video — https://amazingphotovideo.com”. Keep it contextual, avoid keyword stuffing, and remove it where brokerage/platform rules prohibit third-party links.
