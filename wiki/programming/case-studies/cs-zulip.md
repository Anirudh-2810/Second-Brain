---
course_code: "CASESTUDY"
course_name: "Open-Source Case Studies"
unit: "Case Study 4 — zulip/zulip [Deep R&D + Build Edition]"
tags: [django, python, realtime, open-source, architecture, case-study, build-plan]
last_updated: "2026-08-24"
confidence: "high"
source: "https://github.com/zulip/zulip (fetched 2026-08-24)"
---

## For future agent
Deep-dive on Zulip's actual code organization and technology rationale (Django+Tornado split, RabbitMQ queues, mypy-strict culture), plus a buildable mini-chat — **"miniZulip": a topic-threaded chat with FastAPI + SQLite + SSE** — the single best portfolio-project candidate in this whole case-studies module. Feeds [[repo-fullstack-web-developer-path]] and [[build-project-playbook]].

# Zulip — Deep R&D

## Part 1 — The Code Inventory

| Component | Tech | Role |
|-----------|------|------|
| `zerver/` | Django (Python) | The heart: models (UserProfile, Stream, Recipient, Message…), REST API endpoints, views |
| `zerver/tornado/` | Tornado | Long-lived websocket connections — pushes events to clients; receives events via RabbitMQ |
| Queue workers | Python consumers over **RabbitMQ** | Async jobs: email, outgoing webhooks, thumbnailing, search index updates |
| `analytics/`, `corporate/` apps | Django | Stats collection; separated open-source/proprietary boundary |
| Frontend | TypeScript + React migration from legacy jQuery templates | Web client |
| Storage | PostgreSQL (+ memcached) | Denormalized reads where hot paths demand |
| Tooling | **mypy --strict**, 100%-coverage-on-new-code policy, custom lint bots | The famous quality gates |

**The message model insight**: Zulip routes every message through a generic `Recipient` table (stream / huddle / personal) — an indirection that makes permissions and threading uniform. Schema-first design visible in plain sight.

## Part 2 — Why That Stack Was Used

| Choice | Why | Trade-off Accepted |
|--------|-----|--------------------|
| **Django for CRUD/API** | Batteries: auth, ORM, admin; hiring pool | Monolith weight; async story historically weak |
| **Tornado beside it** | Django/WSGI can't hold thousands of live websocket connections cheaply | Two frameworks to operate — solved by queue handoff |
| **RabbitMQ between them** | DB write → event → fanout must be reliable & decoupled | Operational complexity (queues to monitor) |
| **Postgres denormalization** | Chat reads are hot paths ("latest 50 messages") | Write-time duplication vs read joins |
| **mypy strict + coverage gates** | Volunteer-driven codebase needs machine-enforced quality | Slower contribution velocity per PR — deliberately traded for sustainability |
| **Topic-threading schema** | Product differentiator (async conversations) | Harder mental model than channel-only chat |

**Second-order insight**: Zulip proves **process is architecture**. The same Django code without their gates would rot; the gates ARE why the monolith stays navigable.

## Part 3 — Can I Build My Own Version?

### Full version: ❌ (years, team)
### Similar workflow: ✅ YES — "miniZulip", the best portfolio project in this module

**Core spec** (Python, FastAPI or Django-lite):

```mermaid
flowchart LR
    C1["Client A<br/>(web page)"] -->|POST message| API["FastAPI:<br/>POST /streams/{s}/messages"]
    API --> DB[("SQLite:<br/>messages(id, stream,<br/>topic, sender, content, ts)")]
    API --> BUS["In-process event bus<br/>(asyncio pub/sub)"]
    BUS --> SSE["GET /events?stream=s<br/>Server-Sent Events stream"]
    SSE --> C1 & C2["Client B sees message<br/>appear live under topic"]
```

| Milestone | Deliverable |
|-----------|-------------|
| M1 (weekend 1) | Streams + topics + messages CRUD; auth-lite (single user ok); tests |
| M2 (weekend 2) | Live updates via SSE; two browser tabs see each other |
| M3 (weekend 3) | Unread counts per topic; typing indicator (fun event-bus stretch) |
| M4 | Deploy free tier; README with GIF |

**Why topic-threading matters as a feature**: implementing Zulip's DIFFERENTIATOR (not another Slack clone) gives you a defensible interview narrative: "channels are synchronous noise; topics are async threads — here's how I modeled that in SQL."

### Failure modes while building

| Failure | Counter |
|---------|---------|
| Websocket rabbit hole | Use SSE first — one-way is enough for v0.1 |
| Auth sprawl | Single-user until M3; token after |
| Event-bus rewrite loops | asyncio.Queue-based bus is fine at your scale |

## Part 3.5 — R&D Extension: Message Flow + miniZulip Schema

### Zulip's send-message flow (end-to-end trace worth memorizing)
1. Client POSTs message → Django view validates (auth, stream perms, notification flags)
2. Message INSERTed into PostgreSQL; Recipient row resolves audience
3. Event queued to RabbitMQ (`missedmessage_` queues + user_events queues)
4. Tornado workers consume → push `message` event over websocket to online recipients
5. Offline users → email/push worker paths
6. Client ACKs; server tracks per-client pointer for missed-event replay

Every stage is idempotent-ish and replayable — the design survives any single component dying. THAT is the interview-grade insight.

### miniZulip schema (SQLite DDL)
```sql
CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT UNIQUE);
CREATE TABLE streams(id INTEGER PRIMARY KEY, name TEXT UNIQUE);
CREATE TABLE messages(
  id INTEGER PRIMARY KEY,
  stream_id INT REFERENCES streams(id),
  topic TEXT NOT NULL,
  sender_id INT REFERENCES users(id),
  content TEXT NOT NULL,
  ts DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_msg_stream_topic ON messages(stream_id, topic, id);
-- unread per (user,stream,topic): store last_read_message_id per membership
```
SSE endpoint sketch (FastAPI):
```python
@app.get('/events/{stream_id}')
async def events(stream_id: int, request: Request):
    q = asyncio.Queue(); bus.subscribe(stream_id, q)
    async def gen():
        while True:
            if await request.is_disconnected(): bus.unsubscribe(stream_id,q); break
            yield f'data: {await q.get()}\n\n'
    return StreamingResponse(gen(), media_type='text/event-stream')
```


## Part 4 — Life Integration

- This can BE your group's project tracker (dogfooding!) — real users from day one
- Metrics: messages flowing, SSE reconnect robustness, tests passing
- Interview stories: schema decisions, SSE-vs-websocket tradeoff, concurrent-write handling ([[interview-counter-guide]] STAR bank)

## Part 6 — Internals Push: Recipient Indirection & Queue Lifecycle

### The Recipient triangle (worked example)
Schema: Stream 1:n Recipient(type=stream) ; Message points at recipient_id ; UserMembership(user, recipient_id, last_read_id).
Why the indirection: ONE routing concept covers streams AND huddles AND personal PMs. Permission check is uniform — "is user subscribed to recipient X?" — regardless of audience kind. Adding broadcast channels later = new Recipient subtype, zero message-table migration. Cost: reads join through Recipient, absorbed by denormalized caches. Design law: model RELATIONSHIPS as entities when kinds may grow; direct FKs only when the kind-set is provably closed.

### Queue-worker lifecycle (reliability tiers)
Producers publish events to RabbitMQ exchanges routed into sharded `user_events:<user>` queues (websocket fanout) plus worker pools (email, webhooks, thumbnails). Consumers ack AFTER side-effects complete → crash mid-job means redelivery → workers must be idempotent (dedupe keys). Missed-message backfill: clients track last event id; reconnect asks Tornado for replay; aged-out events pulled from DB. Three reliability tiers: live push, queue replay, DB backfill.

### mypy --strict culture notes
Incremental adoption over years; strictness enforced on NEW modules first; custom mypy plugins check Django-specific idioms. Takeaway: strict typing is a CI-enforced POLICY, achievable gradually — start new-file-only.

## Checkpoint Questions

1. Why does Zulip need BOTH Django and Tornado — what breaks if events go straight through Django?
2. How would MY schema change if I added private groups tomorrow? Is that a migration or a redesign?
3. What did the Recipient-table indirection buy them that direct stream_id on messages wouldn't?

## Cross-Vault Links

[[programming/case-studies/index|Field Index]] · [[systems-design-distributed]] · [[languages-python-advanced]] · [[build-project-playbook]]