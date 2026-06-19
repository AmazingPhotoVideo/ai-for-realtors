# Memory and Learning Policy

A realtor agent becomes useful when it learns how the user actually works. This policy tells the agent what to remember, what to keep temporary, and when to create a reusable skill/runbook.

## Save as durable user memory

Save compact facts that are likely to remain true:

- local farm definitions and boundaries
- target client types and business priorities
- tone/style preferences
- spelling and language preferences
- outreach time windows and approval rules
- brokerage/team compliance rules
- CRM/task/social/email systems used
- social handle list and metric preferences
- APV attribution preferences
- content pillars and topics to avoid

Examples:

- `User's farm area is East Danforth: Coxwell to Main, Danforth to Gerrard.`
- `User prefers SMS under 240 characters, warm/direct tone, one CTA.`
- `User does not want AI to send texts automatically; draft-only unless explicitly approved.`

## Save as environment/tool memory

Save stable setup facts:

- CRM connector method and safe scopes
- where exports are stored
- which social metrics source is reliable
- task system schema
- known platform quirks

Examples:

- `CRM is Follow Up Boss; action plans are reviewed through exports, not API writes.`
- `Instagram metrics arrive as weekly CSV export in /secure/metrics/instagram/`.

## Do not save as durable memory

Do not save facts that will go stale quickly:

- today's task list
- one-off appointment details
- active negotiation details
- temporary campaign copy
- PR numbers, commit hashes, or build results
- private client facts unless the user explicitly wants CRM-like memory and the platform is approved for that use

## Create or update a skill/runbook when

- the user corrects a process that will repeat
- a workflow takes 5+ steps and succeeds
- a CRM/social/email connector has a special procedure
- a prospecting script style becomes standard
- a compliance rule changes how outputs should be written

Skill examples:

- `follow-up-boss-triage`
- `east-danforth-weekly-content-plan`
- `seller-valuation-lead-response`
- `instagram-metrics-review`

## Correction handling

When the user corrects the agent:

1. Apply the correction immediately.
2. State the durable lesson in one sentence.
3. Save it to memory if it will matter again.
4. Update a skill/runbook if it is procedural.
5. Do not argue or repeat the old behavior.

## User style learning questions

Ask these gradually:

- Do you want messages to sound more polished, casual, luxury, direct, or neighbourly?
- Should I use emojis in texts/social captions?
- Do you prefer short or detailed emails?
- What phrases sound unlike you?
- What claims do you never want in your marketing?
- What local references are safe to use?

## Local/farm learning questions

If unknown, ask:

- What is your main farm area?
- What streets/buildings/schools/landmarks define it?
- What property types and price bands matter?
- What misconceptions do buyers/sellers have there?
- What are the recurring questions you hear?
- What local sources should I trust?

## Prospecting learning questions

Ask:

- What kind of prospecting do you actually want help with?
- Which methods do you dislike or refuse to do?
- What have you talked about with prospects this week?
- Which objections are showing up?
- Which leads are high-value enough for deeper research?
