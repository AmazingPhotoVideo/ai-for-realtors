# Open House QR Sign-In

A no-app QR check-in flow that captures real buyers, respects privacy, and creates instant follow-up while the home is still fresh in the visitor’s mind.

## Flow

Door sign/table tent → QR form → thank-you page with property packet → CRM tags → instant SMS/email → agent task → post-open-house nurture.

## Form fields

Required:
- First name
- Mobile or email
- Are you working with an agent? yes/no/prefer not to say
- What brought you in? buying / neighbour / agent preview / curious

Optional:
- Timeline
- Budget range
- Must-have feature
- Consent checkbox for SMS/email follow-up where required

## Table tent copy

**Check in for the property packet**

Scan for disclosures, floor plans, offer updates, and similar homes.

[QR]

No app needed. Your information is used only for property follow-up and market updates from [AGENT/BROKERAGE].

## Thank-you page copy

Thanks for visiting [ADDRESS].

Choose your next step:
- Download the property packet
- Ask a question about the home
- Book a private second showing
- Get similar listings
- Request a value range for your home nearby

## Immediate SMS

> Thanks for visiting [ADDRESS] today — it’s [AGENT]. Here’s the property packet: [LINK]. What did you think: 1) interested, 2) maybe, 3) not the one? Reply STOP to opt out.

## Immediate email

Subject: Property packet for [ADDRESS]

Hi [FIRST],

Thanks for stopping by [ADDRESS]. Here are the details in one place:

- Photos/tour: [LINK]
- Floor plan/disclosures if available: [LINK]
- Offer or showing instructions: [LINK]
- Similar homes: [LINK]

If you are represented, please have your agent contact me directly for showing and offer questions.

[AGENT]

## Post-open-house nurture

- Hour 0: SMS + email packet
- Hour 2: agent reviews hot leads and calls serious visitors
- Day 1: “What did you think after sleeping on it?”
- Day 3: similar listings or price/status update
- Day 7: buyer consult CTA or homeowner value CTA
- Day 14: neighbourhood market report

## CRM tagging

Tags: `open-house`, `listing:[slug]`, `represented`, `unrepresented`, `neighbour`, `hot`, `needs-financing`, `seller-curious`.

Stages: Checked in → Sent packet → Responded → Showing/consult requested → Appointment booked → Long-term nurture.

## Automation rules

- If “working with agent = yes,” route to listing-agent follow-up only and avoid buyer-agency solicitation.
- If “neighbour,” send seller-value CTA, not buyer pressure.
- If “timeline under 90 days,” create same-day call task.
- If no consent checkbox, send only transactional email required to deliver requested packet and suppress marketing texts.

## KPI targets

- 70%+ visitor check-in rate when sign is visible and host asks consistently
- 30–50% packet click rate
- 10–25% reply rate to same-day SMS
- 1–3 appointments from a strong open house weekend

## Compliance cautions

- Follow local agency disclosure rules and brokerage policy.
- Do not solicit represented buyers; direct them through their agent.
- Use clear consent for automated SMS/email and include STOP.
- Keep visitor data in your CRM; do not share with seller beyond appropriate aggregate feedback unless permitted.

## APV attribution

Do not put APV credit on the sign-in form if it distracts from conversion. If the property packet includes a public resources page, the footer can say:

> Open-house follow-up workflow adapted from Amazing Photo Video resources: https://amazingphotovideo.com
