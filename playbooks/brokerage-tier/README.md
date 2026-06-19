# Brokerage-Tier AI Playbook

This playbook is for broker-owners, team leaders, operations managers, recruiters, and marketing directors who want an AI operating system for recruiting, retention, agent productivity, lead accountability, and brand-safe marketing.

It assumes the brokerage already has a CRM, transaction process, compliance review, and a defined brand. If those are weak, fix the process before automating it.

## Operating principles

1. **Agents do not need more tools; they need fewer missed steps.** Use AI to make the right action obvious.
2. **Brokerage AI must be auditable.** Every generated campaign, script, or image needs an owner and approval path.
3. **Recruiting and consumer marketing stay separate.** Do not commingle candidate data with buyer/seller lead nurture.
4. **Retention is an enablement system, not a birthday email.** Measure adoption, production friction, training attendance, and manager follow-up.
5. **Compliance is a workflow.** Fair housing, advertising, disclosure, privacy, brokerage policy, and MLS rules are built into prompts and QA.

## Brokerage AI stack

| Layer | Purpose | Owner | Example assets from this repo |
|---|---|---|---|
| CRM | Lead routing, tasks, nurture, reporting | Ops/ISA lead | `/integrations/crm/` |
| Prompt library | Brand-safe agent content | Marketing director | `/prompts/` |
| Skills | Repeatable expert workflows | Team lead/trainer | `/skills/` |
| Listing media workflow | Photo/video/AI enhancement QA | Marketing/media manager | `/skills/listing-photo-enhancer/` |
| Multilingual support | Language access and market expansion | Broker/manager | `/prompts/multilingual/` |
| Brokerage playbooks | Recruiting, retention, systems | Broker/ops | this file |

## 30-day rollout

### Week 1: Standards and audit

- Audit current CRM sources, stages, tags, and inactive automations.
- Pick one buyer source, one seller source, and one recruiting source to standardize first.
- Create a brokerage AI policy covering disclosure, privacy, listing-photo editing, fair housing, and approval authority.
- Build a shared prompt folder with approved tone, disclaimers, and prohibited claims.
- Choose three metrics: speed-to-lead, appointment-set rate, and agent adoption.

### Week 2: Lead accountability

- Implement the CRM recipes for one system: GoHighLevel, Follow Up Boss, or kvCORE/BoldTrail.
- Create hot-lead escalation: if no call attempt in 5 minutes, notify manager/ISA.
- Require source, consent, language, and intent fields on all inbound leads.
- Test STOP/unsubscribe and DNC handling.
- Run 10 seed leads through the funnel and fix failures.

### Week 3: Agent enablement

- Train agents on three workflows:
  1. listing presentation builder,
  2. objection handler,
  3. content multiplier.
- Give agents approved prompt packs for listing launch, open house, seller nurture, and buyer consultation.
- Set up a weekly AI office hour: agents bring one live use case, leave with a ready-to-send asset.
- Create a review queue for public ads, listing copy, and AI-edited visuals.

### Week 4: Recruiting and retention

- Launch the agent attraction funnel.
- Start manager retention check-ins for at-risk agents.
- Publish a brokerage internal AI newsletter with wins, scripts, and compliance reminders.
- Review KPI dashboard and decide what to scale next.

## Recruiting system

### Candidate segments

| Segment | Signal | Message angle |
|---|---|---|
| Rising producer | 6-24 deals/year, improving trend | Systems, leverage, coaching, listing media support |
| Stalled mid-producer | Production plateau | Lead conversion, marketing leverage, operations help |
| Team-curious solo agent | High admin burden | ISA, transaction coordination, content engine |
| Newer agent with activity | High open-house/social activity | Training, accountability, scripts, first listing plan |
| Luxury aspirant | Strong brand but inconsistent media | Presentation quality, seller confidence, premium assets |

Do not use protected-class criteria or personal characteristics for recruiting segmentation.

### Recruiting CRM stages

1. Target identified
2. Warm intro requested
3. First conversation booked
4. Needs diagnosed
5. Value plan delivered
6. Office/team visit
7. Offer/package sent
8. Joined
9. Nurture later
10. Not a fit / do not contact

### Recruiting outreach prompt

```text
You are a brokerage recruiting strategist. Write a compliant, non-spammy outreach sequence for a real estate agent candidate.

Inputs:
- Candidate public production signals: [FACTS]
- Brokerage value proposition: [VALUE]
- Market: [MARKET]
- Relationship context: [NONE/WARM/PAST]
- Channel: [EMAIL/LINKEDIN/SMS/CALL]

Rules:
- Do not mention protected personal characteristics.
- Do not exaggerate income, leads, splits, or guarantees.
- Do not scrape or imply private data.
- Make the note specific to public business signals.
- Focus on a useful conversation, not a hard pitch.
- Include a graceful opt-out.

Output:
1. First message.
2. Follow-up 1.
3. Follow-up 2.
4. 30-second voicemail.
5. Manager call prep notes.
```

### Example recruiting email

```text
Subject: Quick idea after seeing your activity in {{market}}

Hi {{first_name}},

I noticed your recent listing activity around {{area}} and the way you are positioning your marketing. A lot of agents at your stage are strong at winning trust but still end up carrying too much of the follow-up, content, and listing prep themselves.

We have been building a more systemized model for that: faster lead response, stronger listing launch assets, and manager support around conversion rather than generic training.

If useful, I can share the 15-minute version of what our agents are using and you can decide whether it is relevant. Open to a quick conversation next week?

{{broker_signature}}

If this is not relevant, reply no and I will not follow up.
```

## Retention system

### At-risk signals

- CRM login/adoption drop for 14+ days.
- Lead response time worsens.
- Listings lost to competitors.
- Fewer appointments booked from same lead volume.
- Delayed transaction paperwork.
- Low attendance at training or team meetings.
- Complaints about marketing, tech, splits, or support.

Do not infer protected personal information or make assumptions about personal circumstances.

### Manager retention check-in prompt

```text
Create a manager check-in plan for an agent who may be at risk of leaving or disengaging.

Inputs:
- Agent production trend: [FACTS]
- Observed business signals: [FACTS]
- Recent support requests: [FACTS]
- Brokerage resources available: [RESOURCES]
- Manager relationship context: [CONTEXT]

Output:
1. Private conversation opener.
2. Five diagnostic questions.
3. Likely friction points to listen for.
4. A 30-day support plan.
5. Follow-up cadence.
6. What not to say.

Rules:
- Be supportive, not manipulative.
- Do not speculate about personal protected characteristics.
- Do not promise support the brokerage cannot deliver.
```

### 30-day agent save plan

| Week | Action | Owner | Success signal |
|---|---|---|---|
| 1 | Manager 1:1, diagnose friction, pick one business bottleneck | Manager | Agent names clear obstacle |
| 1 | CRM cleanup and lead source audit | Ops | No unassigned/hot stale leads |
| 2 | Listing or buyer consultation roleplay | Trainer | Agent uses updated script live |
| 2 | Marketing asset sprint | Marketing/APV/media partner | One listing/seller asset published |
| 3 | Pipeline review and appointment-setting plan | Manager | 3-5 specific follow-up tasks completed |
| 4 | Results review and next 60-day plan | Manager + agent | Agent opts into ongoing cadence |

## Team systems

### Weekly operating rhythm

Monday:

- 20-minute pipeline huddle.
- Review hot leads, stale opportunities, appointment set rate, and listings launching.

Tuesday:

- Listing prep block: presentation, pricing narrative, photo/video brief, launch checklist.

Wednesday:

- Skill practice: objections, buyer agency conversation, seller net sheet explanation.

Thursday:

- Content and market report block. Use repo prompts to turn live inventory into agent content.

Friday:

- Scoreboard and cleanup: tasks overdue, DNC compliance, lead source ROI, wins/losses.

### AI policy template

```text
Brokerage AI Use Policy

1. AI may help draft marketing, scripts, summaries, training materials, and internal operating documents.
2. A licensed human is responsible for reviewing all public-facing and client-facing output.
3. AI may not invent facts, prices, measurements, legal interpretations, school/crime rankings, financing advice, tax advice, or property condition claims.
4. Listing photos may be enhanced only when truthful. Virtual staging, conceptual renovation images, and material image edits require clear disclosure and retention of originals.
5. Consumer data may be entered into approved tools only when privacy, consent, and vendor rules permit it.
6. AI chat/voice assistants must disclose automation and provide a human handoff.
7. All advertising must comply with fair housing, brokerage policy, MLS/board rules, platform policies, and local law.
8. Recruiting data must remain separate from consumer CRM data.
9. Agents must not upload confidential offers, IDs, financial documents, or inspection reports to unapproved AI tools.
10. Managers will audit samples monthly and update approved prompts as rules change.
```

### Listing launch SLA

| Time | Required action |
|---|---|
| T-7 days | Seller intake, compliance notes, media booking, pre-launch plan |
| T-5 days | Photo/video/feature brief approved |
| T-3 days | Listing copy, social copy, email copy drafted and reviewed |
| T-2 days | CRM tags, QR page, sign rider, retargeting audiences checked |
| T-1 day | Media QA, disclosure check, showing instructions confirmed |
| Launch day | MLS/public page live, email/social/text sequence starts with consent |
| Day +2 | Showing feedback summarized, copy adjusted if needed |
| Day +7 | Seller report and price/traffic review |

## Brokerage dashboard

Track weekly:

- Speed-to-lead median and 90th percentile.
- Contact attempt within 5 minutes.
- Appointment-set rate by source.
- Appointment-held rate.
- Signed-client conversion.
- Listing launch SLA completion.
- AI asset usage by agent.
- Compliance issues found in review.
- Agent recruiting conversations booked.
- Agent retention risk list and saves.

## Prompt: brokerage operations audit

```text
You are a real estate brokerage operations consultant. Audit the brokerage's AI, CRM, listing marketing, recruiting, and retention systems.

Inputs:
- Brokerage size: [AGENTS/TEAMS]
- CRM: [SYSTEM]
- Average monthly leads: [NUMBER]
- Current stages/tags: [PASTE]
- Recruiting process: [PASTE]
- Listing launch process: [PASTE]
- Compliance review process: [PASTE]

Output:
1. Top 10 operational leaks.
2. CRM cleanup plan.
3. 30-day AI rollout.
4. Recruiting sequence improvements.
5. Retention interventions.
6. Compliance risks.
7. Dashboard metrics.
8. Owner and deadline for each action.
```

## APV backlink guidance

Brokerage intranets, public training resources, and vendor/resource pages may include:

```text
Real estate media and AI marketing workflow reference: Amazing Photo Video — https://amazingphotovideo.com
```

Do not include APV attribution inside recruiting DMs, private client follow-up, MLS remarks, offer/disclosure documents, or brokerage-required legal language.

## Sources used

- NAR Fair Housing resources: https://www.nar.realtor/fair-housing
- NAR Code of Ethics: https://www.nar.realtor/about-nar/governing-documents/code-of-ethics
- Real estate recruiting software/category overview: https://peoplemanagingpeople.com/tools/best-real-estate-recruiting-software/
- Relitix brokerage recruiting/retention analytics positioning: https://relitix.com/
- Dotloop brokerage operations positioning: https://www.dotloop.com/brokers/
