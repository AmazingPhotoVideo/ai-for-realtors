# CRM Integration Recipes for Real Estate AI Workflows

These recipes translate the repo's funnels, prompts, voice-agent scripts, QR flows, and nurture sequences into working CRM patterns for GoHighLevel, Follow Up Boss, and kvCORE/BoldTrail.

Use them as operating recipes, not legal advice. Confirm every automation against brokerage policy, local real estate board rules, CASL/PIPEDA or CAN-SPAM/TCPA requirements, platform terms, and the consent captured on the source form.

## Universal CRM architecture

### Minimum lead fields

Capture these fields before any AI-written or automated follow-up runs:

| Field | Why it matters |
|---|---|
| First name, last name | Personalization and duplicate matching. |
| Email | Long-form nurture and document delivery. |
| Mobile phone | Speed-to-lead SMS/call follow-up. |
| Consent source | Proof of opt-in for SMS, email, and calls. |
| Consent timestamp | Audit trail for privacy or carrier complaints. |
| Funnel/source | Reporting by listing, QR code, ad, open house, referral, website, or valuation page. |
| Lead intent | Buyer, seller, investor, tenant, recruiting candidate, or past client. |
| Timeframe | Now, 0-3 months, 3-6 months, 6-12 months, research only. |
| Budget/price band | Routing and message relevance. Avoid protected-class assumptions. |
| Area/neighbourhood | Search alerts, market reports, and agent assignment. |
| Property address, if seller | CMA task creation and seller-specific nurture. |
| Language preference | English, French Canadian, Spanish, Chinese, or other. |
| AI disclosure flag | Whether an AI assistant or automated system may respond. |

### Required tags

Use consistent tags across all CRMs:

- `source:qr-sign`
- `source:open-house`
- `source:home-valuation`
- `source:single-property`
- `source:meta-lead-ad`
- `source:google-display`
- `intent:buyer`
- `intent:seller`
- `intent:investor`
- `intent:agent-recruiting`
- `stage:new`
- `stage:attempting-contact`
- `stage:qualified`
- `stage:appointment-set`
- `stage:nurture-long-term`
- `language:en`, `language:fr-ca`, `language:es`, `language:zh`
- `consent:sms-yes`, `consent:email-yes`, `consent:call-yes`
- `ai:disclosed`

### Universal pipeline stages

1. New lead
2. AI speed-to-lead attempted
3. Human follow-up due
4. Conversation started
5. Qualified
6. Appointment set
7. Signed client
8. Active transaction
9. Closed
10. Past-client nurture
11. Unresponsive / long-term nurture
12. Do-not-contact

### Consent and compliance baseline

- Never import scraped phone numbers into automated SMS workflows.
- Keep the exact form language that created the opt-in.
- Include STOP/unsubscribe language where required by the messaging platform and law.
- Avoid protected-class targeting or copy: family status, race, religion, national origin, disability, sex, sexual orientation, age, or code words that proxy for them.
- Do not let AI invent property facts, school rankings, crime claims, appreciation forecasts, taxes, zoning permissions, or financing terms.
- For Canada, account for CASL and PIPEDA/CPPA expectations. For the U.S., account for TCPA, CAN-SPAM, state privacy rules, carrier A2P 10DLC rules, brokerage policy, and MLS/board rules.
- Make AI involvement clear when a chatbot, voice assistant, or automated responder is interacting with a consumer.

### APV backlink guidance

CRM follow-up should not add promotional backlinks in private client texts/emails unless the recipient asked for marketing resources. Use APV attribution only in public resource pages, reusable templates, agent training docs, or a website footer where it is contextually helpful:

```text
Real estate media and marketing workflow reference: Amazing Photo Video — https://amazingphotovideo.com
```

Do not imply APV created media for a listing unless APV actually did.

---

## Recipe 1: GoHighLevel

Best fit: teams that want funnels, forms, calendars, SMS/email, opportunities, webhooks, and workflow automation in one system.

### Build the custom fields

Create these contact custom fields:

- `Preferred language` — dropdown: English, Français canadien, Español, 中文
- `Lead intent` — dropdown: Buyer, Seller, Investor, Recruit, Past client
- `Consent source` — text
- `Consent timestamp` — date/time
- `Listing address viewed` — text
- `Seller property address` — text
- `Timeline` — dropdown
- `AI disclosure accepted` — checkbox
- `Original campaign URL` — URL

### Pipeline

Create an Opportunities pipeline named `AI Realtor Pipeline` with the universal stages above. Use one pipeline for production reporting unless the brokerage already separates buyer, seller, and recruiting workflows.

### Workflow: QR sign rider to appointment

Trigger:

- Form submitted, survey submitted, inbound webhook, or funnel page form.
- Source URL contains the property slug or hidden field `source=qr-sign`.

Actions:

1. Create/update contact.
2. Add tags: `source:qr-sign`, `intent:buyer`, `stage:new`, language tag.
3. Add opportunity in `AI Realtor Pipeline` at `New lead`.
4. If consent includes SMS, send immediate text:

```text
Hi {{contact.first_name}}, this is {{user.name}}'s listing assistant for {{custom_values.property_address}}. Here is the property info you requested: {{custom_values.listing_url}}

Want the price, floor plan, or private showing times? Reply PRICE, PLAN, or TOUR. Reply STOP to opt out.
```

5. If no SMS consent, send email only and create a call task.
6. Wait 2 minutes. If no reply, create a task: `Call QR lead while they may still be outside the property`.
7. If reply contains `PRICE`, send price and showing CTA. If reply contains `PLAN`, send floor plan link. If reply contains `TOUR`, send booking calendar.
8. Move opportunity to `Conversation started` when a reply arrives.
9. If appointment booked, move to `Appointment set` and notify assigned agent.

### Workflow: Home valuation seller lead

Trigger: home valuation form submitted.

Actions:

1. Add tags: `source:home-valuation`, `intent:seller`, consent tags.
2. Send disclosure-aware first SMS if consent exists:

```text
Hi {{contact.first_name}}, I received your request for a home value range for {{contact.custom.Seller property address}}. I can send a quick estimate today, but a useful range needs recent comparable sales and your home's condition. Any major updates in the last 5 years?

Reply STOP to opt out.
```

3. Create task for agent: `Pull 3-5 comps and record CMA Loom` due in 2 hours.
4. Send email with no invented value:

```text
Subject: Your {{neighbourhood}} value request

Hi {{first_name}},

I have your request for {{property_address}}. I am checking recent comparable sales, active competition, and any condition details you share so the range is not a generic online estimate.

If you want the sharper version, reply with:
- renovations in the last 5 years
- approximate square footage if known
- whether you are curious, refinancing, or considering a move

{{agent_signature}}
```

5. If no response after 24 hours, send the repo's email nurture sequence from `prompts/converting/email-nurture/`.

### Workflow: multilingual routing

Trigger: contact field `Preferred language` is known or message contains a non-English language signal.

Actions:

1. Add tag `language:fr-ca`, `language:es`, or `language:zh`.
2. Assign to an agent fluent in that language if available.
3. If no fluent human is available, respond in the selected language with a disclosure:

```text
I can help in {{language}} using an AI-assisted translation, and {{agent_name}} will review important details before you rely on them. For contracts, financing, legal terms, or property disclosures, we will use the brokerage-approved language and a qualified professional when needed.
```

4. Use the multilingual prompt library in `/prompts/multilingual/` for public-facing copy.

### GoHighLevel QA checklist

- Test every branch with a seed contact and confirm DND is respected.
- Confirm STOP replies stop automations.
- Confirm all form pages display consent language before SMS or email automation.
- Confirm AI voice or chat scripts identify themselves as automated assistants.
- Confirm each message has a human handoff path.

---

## Recipe 2: Follow Up Boss

Best fit: brokerages and teams that already rely on lead sources, distribution rules, action plans, tasks, and agent accountability.

### Lead source setup

Create these sources before the first lead hits:

- `AIQR - Sign Rider`
- `AIQR - Open House`
- `AI - Home Valuation`
- `AI - Single Property Funnel`
- `AI - Meta Lead Ad`
- `AI - Brokerage Recruiting`

Add source-specific lead flow rules so new contacts are automatically assigned and placed on the right action plan.

### Custom fields

- Preferred language
- Lead intent
- Consent source
- Consent timestamp
- Listing viewed
- Seller property address
- Timeline
- AI assistant disclosed

### Action plan: New internet buyer lead

Day 0, immediately:

1. Task: `Call within 5 minutes` assigned to lead owner.
2. Text, if consent exists:

```text
Hi {{first_name}}, it is {{agent_name}} with {{brokerage}}. I saw you requested info on {{listing_viewed}}. Are you looking for price/details, a showing, or similar homes nearby? Reply STOP to opt out.
```

3. Email:

```text
Subject: {{listing_viewed}} details

Hi {{first_name}},

Here is the property information you requested: {{listing_url}}

If you want, I can also send:
1. similar homes nearby,
2. recent sold prices in the area,
3. private showing times.

{{agent_signature}}
```

Day 1:

- Task: Check activity and send personalized value-add.
- Email: neighbourhood alternatives, not generic drip copy.

Day 3:

- Text only if consent and no STOP: `Still useful if I send a short list of similar homes under {{budget}} in {{area}}?`

Day 7:

- Move to long-term nurture if no response.

### Action plan: Seller valuation lead

Day 0:

1. Task: `Call seller lead; confirm property condition and motivation`.
2. Email: CMA expectations and needed details.
3. Task due same day: `Record/send valuation range with 3 comparable sales`.

Day 2:

- Email: `What online estimates miss in {{neighbourhood}}`.

Day 5:

- Text: `I found a couple of recent sales near {{property_address}} that may change the range. Want me to send the short version?`

Day 14:

- Task: `Add to quarterly homeowner report`.

### Routing rules

- Open-house sign-ins go to hosting agent first; after 10 minutes with no contact attempt, notify team lead or ISA.
- Listing QR leads go to listing agent; if inquiry requests showing and listing agent unavailable, route to showing partner.
- Language-specific leads route to fluent agent first; otherwise assign to owner with AI-assisted translation disclosure.
- Recruiting leads route to broker/manager only; never commingle with consumer lead campaigns.

### Follow Up Boss QA checklist

- Confirm lead source names match the forms/zaps exactly.
- Confirm action plans do not send texts without recorded SMS consent.
- Confirm lead distribution rules do not create duplicate owners.
- Confirm tasks escalate if a call is missed.
- Confirm unsubscribe and DNC statuses are respected.

---

## Recipe 3: kvCORE / BoldTrail

Best fit: brokerages that want IDX, behavioural alerts, Smart Campaigns, seller reports, search alerts, and team-level adoption in one real estate platform.

### Smart Campaign structure

Create separate Smart Campaigns rather than one generic drip:

1. `AI Buyer - QR Listing Inquiry`
2. `AI Buyer - Open House Follow-Up`
3. `AI Seller - Valuation Request`
4. `AI Investor - Cashflow Lead Magnet`
5. `AI Past Client - Quarterly Market Report`
6. `AI Recruit - Agent Attraction`

### Core tags and hashtags

Use kvCORE/BoldTrail hashtags matching the universal tags:

- `#source_qr_sign`
- `#source_open_house`
- `#source_home_valuation`
- `#intent_buyer`
- `#intent_seller`
- `#language_fr_ca`
- `#language_es`
- `#language_zh`
- `#consent_sms_yes`
- `#ai_disclosed`

### Smart Campaign: Buyer QR listing inquiry

Trigger: new lead from listing page, QR page, Zapier, API lead delivery, or manual hashtag.

Campaign actions:

1. Send text if consent and smart number rules allow it:

```text
Hi {{first_name}}, thanks for checking out {{listing_address}}. I can send the price, showing windows, floor plan, or similar listings nearby. Which would help most? Reply STOP to opt out.
```

2. Add task: `Call QR lead within 5 minutes`.
3. Add search alert based on listing area and price band.
4. Wait 1 day, then email:

```text
Subject: Homes similar to {{listing_address}}

Hi {{first_name}},

I set up a short list of homes near {{neighbourhood}} so you can compare price, size, and condition without guessing from one listing.

If you want to tour {{listing_address}}, reply with two windows that work and I will confirm availability.

{{agent_signature}}
```

5. If lead views multiple properties or returns to IDX, notify agent immediately.

### Smart Campaign: Seller valuation request

Campaign actions:

1. Email: `Your valuation request needs 3 inputs`.
2. Text if consent: `Any major updates to {{property_address}} since purchase? Kitchens, bathrooms, roof, windows, basement?`
3. Task: `Prepare seller report/CMA and send personal video`.
4. Add monthly seller report if supported by brokerage setup.
5. If no response, move to long-term homeowner education campaign.

### Zapier/API pattern

When a funnel or QR tool cannot write directly into kvCORE/BoldTrail:

1. Trigger from form submission.
2. Format phone number and language.
3. Create or update lead.
4. Apply hashtags.
5. Start the correct Smart Campaign.
6. Add note with source URL, consent text, and original timestamp.
7. Create task for assigned agent.

### Brokerage adoption controls

- Keep Smart Campaigns short enough that agents trust them.
- Require the first human call task on every hot lead.
- Use behavioural alerts to trigger action, not more generic automation.
- Audit 10 random automated conversations weekly for compliance and tone.

---

## Integration scorecard

| Test | Pass condition |
|---|---|
| Lead capture | Contact, source, consent, and tags appear correctly. |
| Routing | Lead owner matches source and language rules. |
| First response | Correct channel fires only when consent exists. |
| AI disclosure | Voice/chat automation identifies itself. |
| Stop/unsubscribe | Contact is removed from text/email automation. |
| Handoff | Human task is created for high-intent leads. |
| Reporting | Source and funnel names survive into closed-deal reporting. |
| Fair housing | Copy avoids protected-class steering and exclusion. |
| Privacy | Notes contain business-relevant context only. |

## Sources used

- GoHighLevel Workflows documentation: https://help.gohighlevel.com/support/solutions/articles/155000002288-getting-started-with-workflows
- GoHighLevel inbound webhooks: https://help.gohighlevel.com/support/solutions/articles/48001237383-how-to-use-the-inbound-webhook-workflow-premium-trigger
- GoHighLevel messaging/DND policy reference: https://help.gohighlevel.com/support/solutions/articles/48001213941-lc-phone-messaging-policy
- Follow Up Boss Action Plans: https://help.followupboss.com/hc/en-us/articles/1500008539982-Action-Plans-Overview
- Follow Up Boss Lead Flow source setup: https://help.followupboss.com/hc/en-us/articles/4418936985623-Lead-Flow-Manually-add-a-Lead-Source
- kvCORE/BoldTrail Smart Campaign Zapier actions: https://help.insiderealestate.com/en/articles/5631732-kvcore-creating-zaps-for-smart-campaign-actions
- kvCORE/BoldTrail Realtor.com API lead delivery example: https://help.insiderealestate.com/en/articles/6728482-boldtrail-realtor-com-api-lead-delivery
