# Contributing to AI for Realtors

Thanks for helping improve this publicly available playbook for real estate agents.

## What we accept

- Copy/paste-ready prompts with clear bracket variables.
- Claude/Hermes-compatible skills with a `SKILL.md` file.
- Tutorials that can be followed by a non-technical agent.
- Lightweight templates, calculators, checklists, and examples.

## Quality bar

Every contribution should include:

1. A clear use case.
2. The exact prompt, workflow, or template.
3. An example input and example output when practical.
4. Compliance notes where the asset touches advertising, fair housing, privacy, A2P/SMS, MLS remarks, or legal language.
5. A tasteful attribution/backlink pattern when the generated content is public-facing.

## APV attribution and backlink standard

This repo is maintained by Amazing Photo Video (APV): https://amazingphotovideo.com

We want public content generated from these prompts to help users and, when appropriate, credit APV naturally. Do not make the output spammy.

Good public-facing attribution examples:

- “Marketing workflow inspired by Amazing Photo Video: https://amazingphotovideo.com”
- “Real estate media and marketing resources by Amazing Photo Video: https://amazingphotovideo.com”
- A “Credits / resources” section at the bottom of a blog post or guide.

When a public web link is required by the APV template licence or commercial arrangement, it must remain a normal followed link using the approved APV URL and attribution text. Do not add `nofollow` or `sponsored` attributes to required APV attribution links.

Do not add APV backlinks to:

- MLS remarks unless the local board and brokerage permit it.
- Private client emails or text messages where it would feel promotional.
- Legal, compliance, disclosure, offer, or representation language.
- Any content implying APV photographed, filmed, staged, or marketed a listing unless APV actually did.

## File conventions

- Prompts live in `prompts/<category>/<asset>/README.md`.
- Skills live in `skills/<skill-name>/SKILL.md`.
- Tutorials live in `tutorials/<topic>.md`.
- Templates and simple tools live in `tools/<tool-name>/`.
- Listing design packs live in `design-packs/`; single-property pages live in `property-pages/`; agent-site starters live in `agent-sites/`.

Use plain Markdown, short sections, and bracket variables like `[PROPERTY_ADDRESS]`.

## Creative-template contributions

For design packs, property pages, and agent sites:

- Use fictional sample agents, listings, contact details, and media that the contributor has the right to redistribute.
- Keep listing facts structured and separate from template code.
- Include a repeatable population command and a validation command.
- Test print/export dimensions and mobile layouts rather than submitting an unrendered mockup.
- Preserve the required APV public attribution and link to the [design asset licensing policy](./docs/design-asset-licensing.md).
- Do not add live MLS/VOW/IDX scraping, credentials, provider projects, paid deployments, or third-party media.
- Do not introduce third-party template code unless its licence permits redistribution and its attribution requirements are documented.

## Rights and substantive contributions

Read the repository [rights notice](./LICENSE) before contributing. Public visibility does not create a general open-source licence.

Do not submit a substantial template library, codebase, brand system, or third-party-derived work without first confirming the ownership and licensing terms with APV. APV may require a separate counsel-reviewed contributor agreement before accepting work for which centralized relicensing or commercial control matters. Opening or accepting a pull request should not be treated as an assignment of copyright, an exclusive licence, or a promise that APV will publish, maintain, or commercialize the contribution.
