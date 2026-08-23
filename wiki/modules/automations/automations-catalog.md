# Automations Catalog — The Source Library

> Analysis of https://github.com/Zie619/n8n-workflows — the largest open collection of ready-to-import n8n workflows.

## 1. Library Snapshot

| Metric | Value |
|---|---|
| Total workflows | 4,343 (growing) |
| Unique integrations | 365 services |
| Total nodes used | 29,445 |
| Categories | 15 |
| License | MIT — free to use, sell, modify |
| Search UI | https://zie619.github.io/n8n-workflows |
| Backend of UI | Python FastAPI + SQLite FTS5 full-text search |
| Deploy | Docker one-liner |

**Why this matters:** every workflow here is a blueprint. You never build from zero — you search for the closest match, import it, and customize.

## 2. Category Map (approximate counts)

| Category | ~Workflows | Typical use |
|---|---|---|
| AI / LLM | 1,000+ | Chatbots, summarization, agents |
| Business Ops | 400 | CRM sync, invoicing, reporting |
| Productivity | 400 | Task managers, digests, notes |
| Marketing | 350 | Campaigns, lead capture, SEO |
| Communication | 320 | Slack/Telegram/Email bots |
| IT / DevOps | 300 | Alerts, backups, monitoring |
| Social Media | 260 | Posting, engagement, analytics |
| Sales | 220 | Lead scoring, outreach, pipelines |
| Content Creation | 160 | Blogs, newsletters, repurposing |
| Finance & Accounting | 150 | Expenses, invoices, crypto alerts |
| Data & Analytics | 110 | ETL, scraping, dashboards |
| E-commerce | 100 | Orders, inventory, reviews |
| Education | 60 | Course ops, flashcards |
| HR & Recruiting | 45 | Screening, onboarding |
| Healthcare & Wellness | 30 | Reminders, tracking |

## 3. Top Integrations by Frequency

| Service | ~Workflows using it | Money angle |
|---|---|---|
| Telegram | 2,700 | Bot delivery channel — clients love it |
| Webhook | 800 | Universal entry point for any app |
| OpenAI | 970 | AI features = premium pricing |
| Slack | 550 | Team notifications for B2B clients |
| Google Sheets | 450 | Cheap "database" every client has |
| Gmail | 350 | Email triage and outreach |
| Notion | 250 | Knowledge bases, content calendars |
| Airtable | 200 | Client-facing mini-CRMs |
| Discord | 190 | Community management gigs |
| HTTP Request | everywhere | Fallback for anything without a node |

Rule of thumb: **Telegram + Sheets + OpenAI + Webhook** covers ~80% of what solo clients ask for.

## 4. Anatomy of an n8n Workflow

```
TRIGGER → TRANSFORM → ACTION
```

- **Triggers**: Webhook (URL endpoint), Schedule/Cron (time-based), App event (new email, new row), Chat (built-in chat UI), Manual.
- **Logic nodes**: IF/Switch (branching), Merge, Code (JS/Python), Set (map fields), Wait, Loop Over Items.
- **Actions**: send message, create row, call API, write file, reply webhook.
- **Expressions**: reference data between nodes with `{{ $json.fieldName }}`.

Minimal mental model: *something happens → clean the data → do the valuable thing.*

## 5. Core Architecture Patterns

### Pattern A: Webhook Responder (fast money)
External event hits your URL → process → respond in <1s.
Use for: form handling, chatbots, payment confirmations, API glue.
Full checklist: see `patterns` knowledge below and templates file.

### Pattern B: Scheduled Digest (retention money)
Cron at fixed time → pull from N sources → summarize (AI optional) → deliver to email/chat.
Use for: daily briefings, weekly KPI reports, monitoring summaries. This is the #1 retainer workflow because it runs forever.

### Pattern C: Two-way Data Sync
App A change → upsert into App B (and optionally reverse).
Use for: CRM ↔ Sheets, e-com store ↔ inventory, form tool ↔ database. Watch for: deduplication keys, rate limits, conflict rules ("last write wins").

### Pattern D: AI Enrichment Pipeline
Input batch → loop items → LLM call per item → write results back.
Use for: lead scoring, content classification, summarizing support tickets, generating social posts from blogs.

### Pattern E: Monitoring & Alerting
Poll an API/file/status page on schedule → compare against threshold → alert Telegram/Slack only on change.
Use for: uptime checks, price drops, keyword mentions, SSL expiry. Sells as "peace of mind" retainers.

### Pattern F: Human-in-the-loop Approval
Event → draft action → pause for approval button (Slack/Telegram) → execute or discard.
Use for: posting to client socials, sending bulk emails, refunds. Reduces client fear = easier sale.

## 6. Import / Export Mechanics

1. In n8n canvas: top-right menu → **Import from File** (JSON) or **Import from URL**.
2. Or copy raw JSON → paste onto empty canvas.
3. Every imported workflow needs credential re-linking: open each red node → select/create credential.
4. Export your finished builds as JSON too — that becomes your **sellable product** (see pricing file).

## 7. Hosting Options Comparison

| Option | Cost/mo | Setup | Best for |
|---|---|---|---|
| Local (Docker) | Free | 1 command | Learning, dev |
| n8n Cloud Starter | ~$24 | Zero | First paying clients |
| VPS (Hetzner/DigitalOcean) | $5–12 | 30 min | Self-host production |
| Railway/Render | $10–20 | 15 min | Quick public deploy |
| Queue mode + Redis + workers | $40+ | Advanced | Heavy client loads |

Production self-host essentials: HTTPS via Caddy/Traefik or reverse proxy, `N8N_ENCRYPTION_KEY` backed up, SQLite → Postgres when >5 active workflows, daily volume backup cron.

## 8. Security Checklist (before any client work)

- [ ] Credentials stored in n8n vault, never hardcoded in Code nodes
- [ ] Webhooks use random unguessable paths + header auth where possible
- [ ] Separate n8n instance per client (isolation)
- [ ] Least-privilege API keys (read-only where possible)
- [ ] Log errors to a dedicated error-workflow → your Telegram
- [ ] GDPR: know where client data flows; delete test data

## 9. Performance Notes

- n8n executes each item through nodes — batch large lists with Loop Over Items + batching options.
- Rate-limited APIs: enable node retry-on-fail with wait.
- Long tasks (>2 min): split workflows, chain via webhook calls.
- Scale path: docker-compose with Postgres + Redis + worker replicas (`EXECUTIONS_MODE=queue`).

## 10. My Builds Log

> Append every shipped workflow here. This becomes your portfolio and product inventory.

| Date | Workflow name | Pattern | For whom | Result/time saved |
|---|---|---|---|---|
| | | | | |
