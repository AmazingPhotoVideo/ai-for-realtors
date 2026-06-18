# Contributing to AI for Realtors

Thanks for helping improve this open-source playbook for real estate agents.

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

Use plain Markdown, short sections, and bracket variables like `[PROPERTY_ADDRESS]`.
