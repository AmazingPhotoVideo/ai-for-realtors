# Daily Realtor Agent Runbook

Use this for a morning brief, business-hours check, or OpenClaw heartbeat that finds something actionable.

## Inputs

- CRM tasks and opportunities
- calendar events for next 48 hours
- recent prospect/client emails and DMs
- task list/reminders
- active listings and active buyers
- local farm context
- social/content metrics if connected

## Morning brief steps

1. Pull today's calendar.
2. Pull overdue and due-today CRM tasks.
3. Pull hot/new/stale leads.
4. Pull recent prospect/client emails needing response.
5. Pull upcoming listing/buyer appointment context.
6. Generate a ranked plan:
   - revenue-critical
   - appointment-critical
   - reputation/client-service critical
   - content/prospecting opportunities
7. Draft responses and prep notes.
8. Ask only the decisions that need human approval.

## Ranking rules

Prioritize:

1. appointment requests and offer/contract timelines
2. hot inbound leads under 24 hours old
3. seller leads with valuation/listing signals
4. active buyer showings/offers
5. listing launch tasks
6. stale leads with clear next action
7. content/prospecting tasks
8. CRM hygiene

## Output format

```text
Morning brief — [date]

Top 3 priorities
1. ...
2. ...
3. ...

Appointments today/tomorrow
- [person/event] — prep notes — recommended next step

Drafts ready
- [email/SMS/DM] — draft text — approve/revise/skip

CRM/task cleanup
- [task] — prep done / recommendation

Content/prospecting
- [one useful action]

Blocked setup
- [one missing connector/question]
```

## Daily prep prompts

### Appointment brief prompt

```text
Create an appointment brief for [CONTACT/EVENT]. Use CRM notes, emails, calendar, and known property/client context. Include motivation, timeline, source, last touch, likely objections, questions to ask, recommended next action, and a follow-up draft. If data is missing, ask for it instead of inventing.
```

### Email draft prompt

```text
Draft a response to [THREAD/CONTACT]. Keep it in my tone: [TONE]. Goal: [GOAL]. Include one clear CTA. Do not overpromise, invent facts, or use protected-class language. If market/listing facts are missing, bracket them.
```

### Task prep prompt

```text
For each due CRM task, decide whether you can prepare notes, draft a message, find missing context, or recommend a next step. Return only tasks where you made the user's next action easier.
```
