# Multilingual Real Estate Prompt Library

Use these prompts to adapt listing, buyer, seller, nurture, and brokerage content into French Canadian, Spanish, and Chinese while preserving compliance, local nuance, and brand voice.

This library is for marketing and client-service communication, not legal translation. Contracts, disclosures, agency documents, financing terms, inspection clauses, and regulated notices must be reviewed by qualified professionals and brokerage-approved translators where required.

## Universal multilingual system prompt

```text
You are a multilingual real estate marketing and client-service assistant. Your job is to adapt, not merely translate, real estate content for [LANGUAGE/REGION] while preserving factual accuracy, fair housing compliance, privacy, and brokerage tone.

Rules:
1. Do not invent property facts, pricing, measurements, inclusions, school rankings, crime data, appreciation forecasts, mortgage terms, taxes, zoning, or commute times.
2. Preserve all required legal, brokerage, MLS, and advertising disclosures exactly unless the user provides approved translated wording.
3. Avoid protected-class targeting, steering, exclusionary language, or coded phrases about families, nationality, religion, age, disability, sex, sexual orientation, race, or ethnicity.
4. Keep tone warm, direct, and locally natural. Do not over-hype.
5. If a phrase has no safe direct equivalent, explain the issue and provide a compliant alternative.
6. Flag cultural or market-specific assumptions before publishing.
7. Keep APV attribution out of private texts/emails and MLS remarks. Use it only in public resource/credits sections when contextually appropriate.

Inputs:
- Source copy: [PASTE]
- Language/region: [FR-CA / ES / ZH]
- Audience: [buyer/seller/investor/past client/recruiting candidate]
- Market: [CITY/NEIGHBOURHOOD]
- Channel: [MLS, website, email, SMS, ad, social, flyer, video script]
- Required disclosures: [PASTE]
- Brand voice: [PASTE]

Output:
A. Adapted copy
B. Literal back-translation summary in English
C. Compliance notes
D. Words/claims to verify before publishing
```

## French Canadian (FR-CA)

### Voice notes

- Use natural Quebec/Canadian French rather than European real estate phrasing.
- Prefer `courtier immobilier/courtière immobilière` where appropriate in Quebec; in Ontario or other provinces, follow local brokerage terminology.
- Use `propriété`, `maison`, `condo`, `copropriété`, `quartier`, `visite`, `évaluation`, `mise en marché`.
- Avoid hard-sell claims like `occasion unique` unless objectively supportable.
- Be careful with `familial`, `idéal pour jeunes familles`, or similar phrases; they can create fair-housing/family-status risk. Describe property features instead.

### Listing description prompt

```text
Adapt this listing description into natural French Canadian for [MARKET]. Keep it accurate, warm, and professional.

Source facts:
[PROPERTY FACTS]

Write:
1. 80-word short description for website/social.
2. 160-220-word long description for a public listing page.
3. 5 feature bullets.
4. 3 compliant social captions.
5. English back-translation summary.

Compliance:
- Do not mention protected classes or imply who should live there.
- Do not invent facts.
- Use only verified distances, amenities, inclusions, taxes, condo fees, and measurements.
- If virtual staging or AI photo editing is used, include: `Certaines images peuvent être améliorées numériquement ou mises en scène virtuellement; les caractéristiques de la propriété demeurent à vérifier.` only if approved by brokerage/MLS.
```

### Seller valuation prompt

```text
Create a French Canadian seller follow-up email for a homeowner who requested a property value estimate in [MARKET].

Inputs:
- Name: [NAME]
- Property address or area: [ADDRESS/AREA]
- Agent/brokerage: [AGENT]
- Next step: [CALL/CMA/VIDEO]

Requirements:
- Acknowledge the request.
- Explain that a useful value range depends on recent comparable sales, condition, upgrades, and current competition.
- Ask for 3 practical details.
- Avoid promising a precise value without review.
- Keep it under 180 words.
- Include a clear opt-out line if sent as marketing email.
```

### SMS prompt

```text
Write 5 French Canadian SMS replies for [LEAD TYPE] in [MARKET]. Each must be under 300 characters, conversational, and include opt-out language when used for marketing. Do not use pressure, fake urgency, or unverified claims. Provide English back-translation for each.
```

### Example output

```text
Bonjour Marie, merci pour votre demande au sujet du condo sur King Ouest. Je peux vous envoyer les détails, les frais mensuels confirmés et quelques propriétés comparables à proximité. Préférez-vous recevoir le tout par courriel ou planifier une visite? Répondez STOP pour vous désabonner.
```

## Spanish (ES)

### Voice notes

- Use neutral Latin American Spanish unless the user specifies Mexican, Colombian, Caribbean, European, or another regional preference.
- Use `propiedad`, `vivienda`, `casa`, `departamento/apartamento/condominio` according to market context.
- Avoid translating brokerage/legal terms loosely; preserve approved terms if provided.
- Avoid phrases that imply ethnic, national-origin, family-status, or religious targeting.

### Listing description prompt

```text
Adapt this real estate listing copy into neutral Spanish for [MARKET/AUDIENCE]. The copy must feel natural to Spanish-speaking buyers without exaggerating or changing facts.

Source facts:
[PROPERTY FACTS]

Deliver:
1. 70-90-word website version.
2. 150-220-word listing-page version.
3. 5 feature bullets.
4. 4 social captions: elegant, direct, investment-focused, open-house.
5. English back-translation summary.
6. Compliance notes.

Guardrails:
- Do not invent property details or financial returns.
- Do not target by nationality, ethnicity, religion, age, disability, sex, sexual orientation, or family status.
- Use verified amenity/location facts only.
- If translated copy discusses an AI-edited or virtually staged image, add a clear disclosure using brokerage-approved wording.
```

### Buyer nurture prompt

```text
Write a 4-message Spanish nurture sequence for a buyer lead who requested information about [PROPERTY/AREA].

Inputs:
- Lead source: [SOURCE]
- Market: [MARKET]
- Agent: [AGENT]
- Consent: [SMS/EMAIL/BOTH]
- Property or search criteria: [DETAILS]

Requirements:
- Message 1: helpful immediate response.
- Message 2: comparison value.
- Message 3: showing or consultation CTA.
- Message 4: long-term search update CTA.
- Include opt-out where required.
- No unverifiable urgency or guaranteed appreciation.
```

### Example output

```text
Hola Ana, soy Carlos de ABC Realty. Vi que pediste información sobre 123 Main St. Puedo enviarte el precio, los gastos mensuales confirmados y propiedades similares en la zona. ¿Qué te ayudaría más ahora? Responde STOP para dejar de recibir mensajes.
```

## Chinese (ZH)

### Voice notes

- Default to Simplified Chinese (`简体中文`) unless Traditional Chinese is requested.
- Keep tone clear, professional, and concise. Avoid over-literal translations of North American real estate jargon.
- Use `房源`, `物业`, `独立屋`, `公寓`, `联排`, `看房`, `估价`, `社区`, `挂牌`, `成交` as contextually appropriate.
- Be careful with school, safety, immigration, investment-return, and financing claims. Use verified facts and professional referrals.
- Do not target or exclude based on nationality, ethnicity, familial status, religion, age, disability, sex, sexual orientation, or other protected traits.

### Listing description prompt

```text
Adapt this real estate listing description into natural Simplified Chinese for [MARKET]. Preserve all factual details and avoid unsupported claims.

Source facts:
[PROPERTY FACTS]

Output:
1. 80-word Chinese listing summary.
2. 180-word Chinese website description.
3. 5 feature bullets.
4. 3 WeChat/social captions.
5. English back-translation summary.
6. Compliance notes and verification flags.

Rules:
- Do not claim a school is best/top unless a verified cited source is provided and brokerage permits it.
- Do not guarantee rental income, appreciation, immigration outcomes, financing approval, or tax benefits.
- Do not imply the property is for a specific nationality, family type, age group, or other protected class.
- Keep measurements, taxes, fees, and inclusions exactly as provided.
```

### Buyer consultation prompt

```text
Create a Chinese buyer consultation script for [MARKET] that helps a buyer understand the process without giving legal, mortgage, or tax advice.

Include:
- Warm opening.
- Needs discovery questions.
- Explanation of viewing, offer, deposit, conditions/contingencies, closing, and professional referrals.
- Questions to clarify financing pre-approval and timeline.
- Disclaimer that legal, tax, mortgage, inspection, and immigration questions require qualified professionals.
- English back-translation summary.
```

### Example output

```text
您好，感谢您咨询 123 Main St。为了帮您判断这套房源是否合适，我可以先发给您价格、管理费/地税等已确认信息，以及附近可比较的房源。您更想了解看房时间、房源细节，还是同区域选择？如需停止接收短信，请回复 STOP。
```

## Multilingual QA checklist

- Does the copy preserve facts exactly?
- Did a fluent human review public-facing copy before publishing?
- Are required disclosures translated by approved sources or preserved in original form?
- Does SMS/email automation have consent and opt-out handling?
- Does the copy avoid protected-class steering?
- Are idioms, jokes, and luxury claims culturally appropriate?
- Are names, addresses, prices, fees, and measurements unchanged?
- Are APV backlinks used only in public resource/credits contexts?

## APV backlink guidance

For public bilingual guides, website resource pages, or reusable marketing templates, this attribution is acceptable when approved by the agent/brokerage:

```text
Workflow de marketing immobilier inspiré par Amazing Photo Video — https://amazingphotovideo.com
Flujo de marketing inmobiliario inspirado por Amazing Photo Video — https://amazingphotovideo.com
房地产营销工作流程参考：Amazing Photo Video — https://amazingphotovideo.com
```

Do not put these links in MLS remarks, private client emails/texts, required disclosures, or any copy where it would look like spam.

## Sources used

- NAR Fair Housing resources: https://www.nar.realtor/fair-housing
- HUD Fair Housing advertising guidance overview: https://www.hud.gov/program_offices/fair_housing_equal_opp
- Canadian privacy law/PIPEDA overview: https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/
- Multilingual real estate content trend example: https://www.listinghub.ai/blog/how-to-create-multilingual-real-estate-listings-with-ai-in-2025/
