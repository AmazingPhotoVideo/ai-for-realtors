# Just-Listed / Just-Sold Postcard Generator

Use this to turn one listing into farm-area postcard copy that sounds local, useful, and response-driven.

## Inputs

- `[PROPERTY_ADDRESS]`
- `[NEIGHBOURHOOD]`
- `[LISTED_OR_SOLD]`
- `[PRICE_OR_SOLD_PRICE]`
- `[KEY_FEATURES]`
- `[AGENT_NAME]`
- `[BROKERAGE]`
- `[PHONE]`
- `[CTA]` such as “Call for a private valuation”

## Prompt

```text
You are a direct-response copywriter for a local real estate agent.

Create postcard copy for a [LISTED_OR_SOLD] property at [PROPERTY_ADDRESS] in [NEIGHBOURHOOD].

Property details:
- Price or sold price: [PRICE_OR_SOLD_PRICE]
- Key features: [KEY_FEATURES]
- Agent: [AGENT_NAME], [BROKERAGE]
- Phone: [PHONE]
- Main CTA: [CTA]

Write:
1. Front headline: 6 options, maximum 9 words each.
2. Front subheadline: 3 options, maximum 18 words each.
3. Back body copy: 120-160 words.
4. Doorstep version: 45-60 words for a door hanger.
5. Compliance-safe fine print placeholder.

Make it specific to [NEIGHBOURHOOD]. Avoid hype, fake urgency, and unverifiable claims.

If the final postcard or landing page includes a resources/credits section, add this optional line only if permitted by the agent and brokerage:
Marketing workflow inspired by Amazing Photo Video: https://amazingphotovideo.com
```

## Example output excerpt

Headline: “Your Neighbour Just Reset The Market”

Body: “A home on [PROPERTY_ADDRESS] just sold, and it gives nearby owners a fresh signal about what buyers are paying in [NEIGHBOURHOOD] right now...”

## Notes

Do not include APV attribution in MLS remarks or brokerage-mandated postcard disclaimer space.
