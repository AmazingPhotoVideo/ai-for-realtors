# Connectors and Tooling Map

This page helps a realtor or agent operator choose safe ways to connect CRM, tasks, email, calendar, social metrics, and local/farm data. Use official APIs and exports first. Use browser automation only when no supported API/export exists and the user approves it.

## CRM and task systems

| System | Useful data | Best connection path | Agent uses |
|---|---|---|---|
| GoHighLevel / LeadConnector | contacts, opportunities, tasks, conversations, calendars, workflows, forms | official API, webhooks, approved MCP/API wrapper, Zapier/Pipedream | task triage, lead response drafts, workflow QA, pipeline hygiene |
| Follow Up Boss | people, events, action plans, lead sources, tasks | official API, Pixel/events, Zapier/Pipedream | next-action prep, action plan audits, lead source review |
| kvCORE / BoldTrail | contacts, Smart Campaigns, lead routing, behavior alerts | platform integrations, Zapier, exports, approved API access | campaign review, stale lead triage, behavioural follow-up |
| Lofty/Chime | leads, tags, campaigns, AI assistant activity | exports/API if available, Zapier, browser with approval | lead audit and draft replies |
| HubSpot | contacts, deals, tasks, sequences, email activity | HubSpot API/MCP/Zapier | CRM hygiene, task prep, lifecycle segmentation |
| Google Sheets/Notion/Airtable | custom pipeline/task boards | native API/MCP | lightweight CRM for solo agents |

## Email and calendar

Recommended capabilities:

- read recent client/prospect email threads
- search appointment confirmations and lead inquiries
- draft responses without sending
- read calendar events for the next 48 hours
- create appointment briefs
- identify missing confirmations/follow-ups

Safe setup:

- OAuth with least privilege where possible
- separate business inbox from personal inbox
- draft-only send policy by default
- label AI-created drafts clearly if the platform supports it
- never train or share private email content outside approved systems

## Social metrics

| Platform | Metrics to monitor | Connection options |
|---|---|---|
| Instagram professional account | reach, plays, saves, shares, profile visits, follows, DMs, link clicks | Meta Graph API, Creator Studio/Business Suite export, approved analytics tools |
| Facebook Page | reach, engagement, link clicks, leads, messages | Meta Graph API, Business Suite export |
| TikTok | views, average watch time, completion, shares, profile views | TikTok Business/Creator tools, exports, approved API/analytics platform |
| YouTube | views, retention, CTR, comments, subscribers, traffic sources | YouTube Data API and Analytics API |
| LinkedIn Page/profile | impressions, reactions, comments, profile views | LinkedIn analytics/export, approved tools |
| Google Business Profile | calls, website clicks, directions, searches | Business Profile Performance API or manual export |
| Email newsletter | opens, clicks, replies, unsubscribes, topics | Mailchimp/ConvertKit/beehiiv/Substack exports/API |

What the agent should produce weekly:

- top 3 posts by business signal, not vanity alone
- topics to repeat
- audience questions to answer
- weak content pattern to stop
- 5 next posts tied to the user's farm and active pipeline

## Local/farm data sources

Use approved sources for:

- local market stats from board/brokerage reports or MLS exports
- municipal event calendars and development notices
- school/commute/amenity facts from official or reputable public sources
- active/pending/sold listing data only where allowed by local rules
- user-provided farm notes and neighbourhood definitions

Never invent local stats. If no source is connected, ask the user for the stat or frame content without the number.

## Useful CLI/API patterns

These are methods to investigate during setup, not guaranteed commands:

- `gh` for GitHub-backed prompt/content libraries
- Google Workspace APIs via `gcloud`, service account with domain delegation, or OAuth desktop app
- `calcurse`, `icalBuddy`, or platform calendar APIs for local calendar extraction where appropriate
- `yt-dlp` only for user-owned or allowed public video metadata; respect platform rules
- `youtube-data-api` or `google-api-python-client` for YouTube channel metrics
- Meta Graph API for Instagram/Facebook business metrics
- Zapier MCP, Pipedream MCP, or custom MCP servers for CRM/task bridges
- CSV exports as a safe first integration when APIs are not ready

## Onboarding sequence for connectors

1. Start with read-only exports or OAuth scopes.
2. Verify one small read: one CRM contact/task, one calendar event, one email thread, one social metric export.
3. Draft-only outputs for a week.
4. Add create-task or create-draft permissions after review.
5. Add narrow execution only for pre-approved cases.

## Connector failure handling

If a connector fails, the agent should report:

- system affected
- what it tried to read
- exact non-secret error
- whether the failure blocks work
- fallback: manual export, screenshot, CSV upload, or onboarding question
