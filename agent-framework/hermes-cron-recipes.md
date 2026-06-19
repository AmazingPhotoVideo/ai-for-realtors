# Hermes Scheduled Task Recipes for Realtor Agents

These are recommended recipes, not installed cron jobs. The user should approve each one before it is created. In Hermes, create them with `/cron add ...`, `hermes cron create ...`, or the cron tool. Attach relevant skills if you import this repo's skills into the profile.

Hermes cron is best for detached scheduled work, reporting, and tasks that should run in a fresh session. OpenClaw heartbeat is best for frequent lightweight main-session check-ins.

## Recommended starter set

### 1. Business-hours CRM and inbox triage

Cadence: every 60 minutes during business hours, or every 30 minutes for high-volume teams.

```text
Check CRM tasks, calendar, and recent prospect/client email. Prepare drafts and appointment briefs. Do not send or change CRM records without approval. If there is nothing actionable, stay silent or report “No action needed” depending on the delivery channel. If setup is incomplete, ask only the next missing connector question.
```

Skills to attach if available:

- `agent-framework/realtor-operator`
- CRM-specific skill or integration notes
- email/calendar/task skill

### 2. Morning command brief

Cadence: weekdays at 08:00 local time.

```text
Prepare my morning realtor brief. Include today's appointments, overdue CRM tasks, hot leads, stale leads, priority follow-ups, content/prospecting block suggestion, and any drafts ready for approval. Keep it short and rank by revenue impact.
```

### 3. Appointment prep

Cadence: every 2 hours during business hours, or one-shot 2 hours before appointments if the calendar integration supports event triggers.

```text
Look for buyer consults, listing appointments, showings, open houses, seller calls, CMA meetings, and inspection/offer dates in the next 48 hours. Prepare a briefing for each: contact summary, goal, timeline, property/context, last touch, likely objections, questions to ask, and follow-up draft.
```

### 4. Lead response audit

Cadence: weekdays at 12:00 and 17:00.

```text
Audit new leads from CRM/forms/DMs/email. Flag any lead without a first response, any hot lead without a next task, and any appointment request not confirmed. Draft the best next response for approval.
```

### 5. Content from conversations

Cadence: weekdays at 15:00 or after the user's prospecting block.

```text
Review notes, tasks, emails, and recent conversations for recurring client questions. Turn the best question into one short-form video hook, one social caption, one email subject/body outline, and one local farm post. Use the user's local area and tone. Ask for missing facts instead of inventing stats.
```

### 6. Social metrics and content iteration

Cadence: weekly, Monday 09:00.

```text
Review connected social/newsletter metrics from the last 7-14 days. Identify top performers, weak posts, audience questions, and one experiment for this week. Recommend 5 posts tied to my farm/listings/prospecting goals. Do not scrape or bypass platform rules; use connected APIs, exports, or approved CLIs only.
```

### 7. Farm-area opportunity scan

Cadence: weekly, Tuesday 08:30.

```text
Review my farm area and local context. Find content angles, community events, market changes, listing activity, buyer/seller questions, and direct-mail/social ideas. Cite sources and do not invent statistics. Output a 7-day farm action plan.
```

### 8. Monthly database hygiene

Cadence: first weekday of the month.

```text
Review CRM segmentation, stale leads, missing next tasks, missing source tags, old nurture memberships, and clients with important dates. Produce a cleanup plan and draft tags/tasks/campaign changes for approval. Do not bulk-edit without approval.
```

## Optional power-user recipes

### Open-house weekend operator

Cadence: Friday 14:00, Saturday/Sunday morning, and Monday 09:00 when open houses are scheduled.

```text
If I have an open house scheduled, prepare the QR sign-in page checklist, property FAQ, visitor follow-up segments, neighbour invitation copy, and Monday follow-up drafts. If there is no open house, stay silent.
```

### Listing launch cockpit

Cadence: daily during active listing launch periods.

```text
For active listings, verify launch checklist status: photos/video/floorplan, listing copy, social posts, email, postcards, retargeting audiences, showing feedback, open-house prep, and neighbour outreach. Draft missing pieces for approval.
```

### Seller nurture monitor

Cadence: twice weekly.

```text
Find seller leads with valuation requests, equity curiosity, downsizing signals, expired/FSBO context, or past-client homeownership milestones. Draft a helpful low-pressure follow-up and recommend the next task.
```

## Safe delivery pattern

For most users:

- Morning brief: deliver to chat/email.
- Frequent triage: silent unless action needed.
- Drafts: put in a “Drafts ready” section, not sent.
- Errors: report connector failures plainly.

## Example Hermes CLI commands

Adapt paths and delivery targets to the user's environment.

```bash
hermes cron create "0 8 * * 1-5" \
  "Prepare my morning realtor command brief from CRM, calendar, tasks, and inbox. Draft but do not send anything." \
  --name "Realtor morning brief"

hermes cron create "every 1h" \
  "Business-hours CRM/inbox triage: find urgent leads, due tasks, appointments, and needed response drafts. Stay silent if nothing actionable." \
  --name "Realtor triage heartbeat"

hermes cron create "0 9 * * 1" \
  "Review social metrics and produce this week's content/prospecting recommendations." \
  --name "Weekly social and content review"
```

## Cron vs heartbeat decision

Use heartbeat when:

- the agent should wake up in the main ongoing session
- the work is short and context-sensitive
- it should mostly stay silent
- the user wants frequent small checks

Use cron when:

- the work is a separate report
- the task may take longer
- the output should be delivered to a specific channel
- you want to attach skills or run from a specific project/workdir
- you want deterministic pre-run scripts or API probes
