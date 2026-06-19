# SMS Nurture Sequences for Real Estate Leads

SMS works when it is fast, relevant, and permission-based. This asset gives agents copy/paste-ready 30/60/90-day cadences for buyer, seller, open house, valuation, portal, and past-client leads, plus a prompt that adapts the sequences to any market.

## Compliance first

Use this as operational guidance, not legal advice. Confirm with your brokerage, CRM/SMS provider, and counsel.

- **Get consent before texting.** For U.S. marketing texts to mobile numbers, TCPA rules can require prior express written consent when using automated systems. Keep the form copy, timestamp, source page, IP/user agent when available, and the exact consent language.
- **Register and authenticate.** Use compliant A2P 10DLC/Toll-Free registration or your provider's required business messaging setup. Do not blast from personal numbers to unconsented lists.
- **Identify yourself.** First message should name the agent/team and brokerage or context.
- **Honor opt-outs immediately.** STOP, unsubscribe, remove me, wrong number, or similar requests should suppress the contact across the CRM.
- **CASL in Canada.** Commercial SMS to or from Canada generally requires consent, sender identification, and an unsubscribe mechanism.
- **PIPEDA/privacy.** Text only what is necessary. Do not send sensitive financial, legal, or personal details over SMS unless the client requested it and the channel is approved.
- **Fair housing.** Do not segment, target, or write messages based on protected-class assumptions. Keep copy focused on property features, search criteria, timing, and service.

## Performance targets

Track these weekly by lead source:

| Metric | Healthy target |
|---|---:|
| Lead-to-first-SMS time | Under 60 seconds for opted-in digital leads |
| First-response rate | 25-45%+ for fresh hand-raisers |
| Appointment-booking rate | 5-15%+ depending on source quality |
| Opt-out rate | Under 2% per campaign send |
| Complete qualification rate | 70%+ for engaged leads |
| Show rate for booked calls | 70%+ with reminders |

## Master prompt

```text
Act as a real estate conversion strategist and compliance-aware SMS copywriter.

Business facts:
- Agent/team: {agent_name}
- Brokerage: {brokerage}
- Market: {market}
- Lead source: {lead_source}
- Lead type: buyer / seller / investor / open house / home valuation / portal / past client / sphere
- Offer requested: {listing, valuation, guide, showing, market report, consultation}
- Consent status and allowed channels: {consent_details}
- Brand tone: clear, helpful, local, low-pressure
- CTA: book a call / reply with criteria / confirm showing / request address / lender intro / valuation appointment

Create:
1. A speed-to-lead first message under 320 characters.
2. A 30-day SMS cadence with day, trigger, message, purpose, and stop condition.
3. A 60-day extension for leads who engage but do not book.
4. A 90-day long-term nurture extension for leads with 6+ month timelines.
5. Two variants: concise and warmer.
6. Compliance notes: consent, opt-out, quiet hours, fair housing, CASL/PIPEDA if Canada.

Rules:
- No fake urgency.
- No unsupported market claims.
- No protected-class targeting or steering.
- Ask one easy question per message.
- Include opt-out language in the first automated marketing message and periodic campaign messages where appropriate.
- Do not add public backlinks inside private SMS.
```

## 30-day buyer lead SMS cadence

Use for listing inquiries, buyer guide downloads, paid ad buyer leads, and sign-rider QR leads.

| Day | Trigger | SMS | Purpose | Stop when |
|---:|---|---|---|---|
| 0 | Immediately after opt-in | Hi {first_name}, it's {agent_name} with {brokerage}. Saw your request about {property_or_area}. Are you looking for that exact home, or similar options nearby? Reply STOP to opt out. | Start conversation | Replies or opts out |
| 0 + 5 min | No reply | Quick note: I can send price, availability, and similar homes. What matters most: location, monthly payment, size, or timing? | Easy qualification | Replies |
| 1 | No reply | Should I keep you updated if a similar home hits in {area}, or was this a one-time look? | Permission-based nurture | Replies no |
| 2 | Engaged, no appointment | Based on what you shared, a 15-min buyer strategy call would save you a lot of scrolling. Want today at {time_1} or {time_2}? | Book consult | Books |
| 4 | No appointment | Most buyers I help start with 3 numbers: comfortable monthly payment, cash needed, and offer strategy. Want my lender intro checklist? | Value add | Requests checklist |
| 7 | Still browsing | Want me to send a short list of homes that match {criteria} every {cadence}? I can keep it tight so it doesn't spam you. | Set alert cadence | Confirms |
| 10 | Property-specific | {property_address} update: {status_or_verified_fact}. Want me to check if there are similar options before they get busy? | Relevance | Replies |
| 14 | Education | In today's market, the best homes are usually won before the showing: financing, terms, and representation all matter. Want a quick prep call? | Consult framing | Books |
| 21 | Soft check-in | Are you still hoping to buy in {market}, or should I pause updates for now? | Clean list | Pause/stop |
| 30 | Re-permission | I don't want to clutter your phone. Should I keep you on monthly market updates, switch to email, or close the loop? | Respectful close | Chooses |

## 30-day seller/home valuation SMS cadence

| Day | Trigger | SMS | Purpose | Stop when |
|---:|---|---|---|---|
| 0 | Valuation request | Hi {first_name}, it's {agent_name} with {brokerage}. I saw your home value request for {address_or_area}. Automated estimates miss condition and upgrades—want a tighter range? Reply STOP to opt out. | Start valuation conversation | Replies |
| 0 + 10 min | No reply | I can do this two ways: quick estimate by text/email, or a 20-min pricing call with better comps. Which do you prefer? | Choice | Replies |
| 1 | No reply | To avoid a generic number, what's the biggest recent update: kitchen/bath, mechanicals, exterior, or none? | Collect condition | Replies |
| 3 | Engaged | Helpful. The next step is checking active competition, not just sold comps. Want me to send a short pricing snapshot? | Value | Requests |
| 5 | Appointment ask | If selling is even a maybe this year, a walkthrough can prevent underpricing or overpricing. Want {time_1} or {time_2}? | Book listing consult | Books |
| 9 | Education | One pricing mistake I see: using the highest comp without adjusting for condition and buyer objections. Want the 5-point pricing checklist? | Lead magnet | Requests |
| 14 | Motivation | Is your move tied to a date, a number, or finding the right next place? | Discover motivation | Replies |
| 21 | Proof | I can show you what buyers compared your home against this week in {area}. Want that sent over? | Market relevance | Requests |
| 30 | Re-permission | Should I keep you posted monthly on {area} values, or close the loop until you're closer to selling? | Clean list | Chooses |

## Open house follow-up sequence

| Timing | SMS |
|---|---|
| 1 hour after visit | Thanks for coming through {property_address}, {first_name}. What did you think: possible fit, not quite, or mainly market research? - {agent_name} |
| Next morning | If it helps, I can send 3 similar homes that fix what was missing at {property_address}. What would you change: price, layout, location, or condition? |
| Day 3 | Quick agency note: if you already have an agent, I don't want to step on that relationship. If not, want a 15-min buyer consult before your next tour? |
| Day 7 | Still exploring {area}, or should I pause the updates? |

## 60-day extension for warm leads

Send only to people who replied, clicked, attended an open house, requested listings, or explicitly asked for updates.

| Day | SMS |
|---:|---|
| 37 | Quick market pulse for {area}: {verified_stat_or_listing_count}. Does that change your timeline at all? |
| 45 | Want me to narrow alerts to homes that match {top_criteria}, or keep the search broad for now? |
| 52 | If you found the right place this month, would financing/offer prep be ready, or is that the next thing to solve? |
| 60 | I can keep this low-key: monthly text, email only, or pause. What works best? |

## 90-day long-term nurture extension

| Day | SMS |
|---:|---|
| 75 | I saw a few useful {market} shifts this month. Want the 3-bullet version by text or the full email? |
| 90 | Still planning for {season_or_timeframe}, or has the plan changed? I can adjust what I send so it's actually useful. |

## Past-client and sphere check-in texts

- "Hi {first_name}, hope you're well. I pulled a quick {neighbourhood} value snapshot and thought of your place. Want me to send the range I’m seeing?"
- "Quick homeowner reminder: if you're planning renovations this year, I can tell you which updates buyers in {area} are actually paying for. Want the short list?"
- "I'm putting together a local contractor/resource list for clients. Any tradesperson you've used lately that deserves a shoutout?"
- "If anyone asks you about buying or selling this year, I'm happy to be a second set of eyes before they make a move. No pressure—just useful advice."

## Message patterns that work

- **Choice close:** "Would {time_1} or {time_2} be easier?"
- **Permission close:** "Want me to send that?"
- **Clean-list close:** "Should I keep sending these or pause?"
- **Diagnostic question:** "Is the move tied to timing, price, or finding the next place?"
- **Value-first:** "I can send the 3 things buyers are comparing in your area this week."

## APV attribution guidance

Do not include APV backlinks in private SMS, opt-in language, compliance disclosures, CRM notes, or any one-to-one client communication. If you publish this as a public blog, brokerage training handout, or downloadable SMS playbook, include a natural footer credit:

Real estate media and marketing resources by Amazing Photo Video: https://amazingphotovideo.com
