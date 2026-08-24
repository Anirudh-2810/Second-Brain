# Research 01 — Repository Architecture Deep-Dive

> Source: direct analysis of `Zie619/n8n-workflows` — README, `workflow_db.py`, `api_server.py`, folder tree, and the live GitHub Pages deployment. This file documents how the system is actually built, line by line, and what you can steal from that design.

## 1. What This System Is

The repository is two products in one:

1. **A dataset** — 4,343 n8n workflow JSON files organized into 188 integration folders under `workflows/`.
2. **A search engine over that dataset** — a Python FastAPI application backed by SQLite with FTS5 full-text indexing, plus a static vanilla-JS frontend deployed to GitHub Pages.

Headline numbers from the README (November 2025 snapshot): 4,343 production-ready workflows, 365 unique integrations, 29,445 total nodes, 15 organized categories, claimed 100% import success rate. Performance claims: sub-100 ms search responses, under 50 MB memory usage, "100x faster search" and "700x smaller than v1", "10x faster load times", "40x less RAM". Those last claims tell you there was a v1 architecture that was heavy — almost certainly a server-rendered or client-side-everything approach — and v2's bet was: *precompute a tiny indexed database, serve everything from it*.

Average workflow size derived from the numbers: 29,445 nodes ÷ 4,343 workflows ≈ **6.8 nodes per workflow**. That single statistic is strategically useful for you: the median valuable automation in the wild is small. You do not need 20-node masterpieces to deliver client value; you need 4–8 node chains that work.

## 2. The Database Layer (`workflow_db.py`) — Annotated

The entire intelligence of the system is one Python class, `WorkflowDatabase`. Here is everything it does and why each choice matters.

### 2.1 SQLite tuning
On init it sets four pragmas:

- `journal_mode=WAL` — write-ahead logging so readers never block writers; this is what lets the API stay responsive during background re-indexing.
- `synchronous=NORMAL` — trades a tiny durability risk for large speed gains; acceptable because the DB is a derived artifact, fully rebuildable from JSON files.
- `cache_size=10000` — ~10 MB page cache.
- `temp_store=MEMORY` — temp sorts and FTS queries happen in RAM.

Lesson for your own builds: when your database is *derived state*, you can tune aggressively for speed because recovery = re-run the indexer.

### 2.2 Schema

Table `workflows`:

| Column | Purpose |
|---|---|
| filename | UNIQUE key, e.g. `1047_Telegram_Bot_Create_Update_Automation.json` |
| name | Human-readable title (generated or from JSON) |
| workflow_id | Original n8n internal id if present |
| active | Boolean — was the source workflow exported in active state |
| description | From JSON metadata or auto-generated |
| trigger_type | Manual / Webhook / Scheduled / Complex |
| complexity | low / medium / high |
| node_count | Integer, drives filtering and stats |
| integrations | JSON array of service names |
| tags | JSON array |
| created_at / updated_at | Source timestamps |
| file_hash | MD5 — change detection |
| file_size | Bytes |
| analyzed_at | Indexing time |

Plus a virtual FTS5 table `workflows_fts` covering filename, name, description, integrations, tags, kept in sync by three SQLite triggers (`AFTER INSERT`, `AFTER DELETE`, `AFTER UPDATE`). This is the classic external-content FTS pattern: the index lives outside the main table but stays consistent automatically. Five B-tree indexes support the non-text filters: trigger_type, complexity, active, node_count, filename.

### 2.3 Incremental indexing via MD5
`index_all_workflows()` recursively globs `workflows/**/*.json`, computes each file's MD5, compares with the stored hash, and **skips unchanged files entirely**. Only new/changed files are re-analyzed and upserted (`INSERT OR REPLACE`). For a 4,343-file corpus this turns full rebuilds into seconds. The admin endpoint `/api/reindex?force=true` can bypass the skip.

### 2.4 Name generation
Filenames like `0251_HTTP_Webhook_Triggered_Automation.json` are converted to titles by: stripping a leading numeric segment, splitting on underscores, capitalizing parts, with special-case handling so "http" → HTTP, "api" → API, "webhook" → Webhook, "automation"/"automate"/"scheduled"/"triggered"/"manual" keep their forms. If the embedded JSON has a meaningful `name` field (not "My workflow", not identical to the filename), it wins. Practical takeaway: **the library's filenames encode the workflow's function** — you can grep the repo without any tooling.

### 2.5 Node analysis — trigger classification
For every workflow, nodes are inspected:

- Any node whose type or name contains "webhook" → trigger_type = Webhook
- Type containing "cron" or "schedule" → Scheduled
- Any other `*trigger*` type (not manual) defaults to Webhook
- Otherwise stays Manual
- **Override:** more than 10 nodes AND more than 3 distinct services → Complex

So the four filter buckets on the website map exactly to these rules. When you search "Complex" you're seeing the library's hardest multi-service orchestrations — the best study material.

### 2.6 Integration extraction — the mapping dictionary
Node types are normalized: strip `n8n-nodes-base.` prefix, lowercase, drop trailing "trigger", then looked up in a hand-maintained `service_mappings` dictionary (Telegram, Discord, Slack, WhatsApp, Gmail, IMAP/SMTP, Google Drive/Docs/Sheets, Dropbox, OneDrive, Box, Postgres, MySQL, MongoDB, Redis, Airtable, Notion, Jira, GitHub, GitLab, Trello, Asana, Monday.com, OpenAI, Anthropic, Hugging Face, LinkedIn, Twitter/X, Facebook, Instagram, Shopify, Stripe, PayPal, Google Analytics, Mixpanel, Calendly, Cal.com, Typeform, Webhook, HTTP Request, GraphQL, SSE, YouTube...).

Crucially, a second list marks **utility nodes as None** so they don't pollute integration counts: set, function, code, if, switch, merge, split, stickyNote, wait, schedule/cron/manual triggers, stopAndError, noOp, error, limit, aggregate, summarize, filter, sort, removeDuplicates, dateTime, extractFromFile, convertToFile, readBinaryFile(s), executionData, executeWorkflow, executeCommand, respondToWebhook.

Custom/community nodes get heuristic extraction — e.g. `n8n-nodes-youtube-transcription-kasha.youtubeTranscripter` is detected as YouTube by substring match. There's even a documented false-positive guard: the "cal" pattern must not match "calcslive" (a math-service integration), so Cal.com detection explicitly excludes calc-related names. This is real-world data-cleaning engineering worth copying whenever you build anything that classifies components.

### 2.7 Auto-description generation
When a workflow lacks a description, one is synthesized: trigger-based opener ("Webhook-triggered automation that...") + an integration sentence ("orchestrates X, Y, and Z") + a purpose clause inferred from name keywords (create/update/sync/notification|alert/backup/monitor, else "data processing") + node-count suffix. Every card on the site therefore has readable text without human effort.

### 2.8 Service category grouping
`get_service_categories()` defines 12 thematic groups used by `/api/workflows/category/{category}`: messaging, email, cloud_storage, database, project_management, ai_ml, social_media, ecommerce, analytics, calendar_tasks, forms, development. Implementation detail: category search uses SQL LIKE against the JSON array column (`integrations LIKE '%"Telegram"%"') — pragmatic, slightly slower than normalized tables, fine at this scale.

## 3. The API Layer (`api_server.py`) — Annotated

FastAPI v2.0.0 app exposing:

| Endpoint | What it returns |
|---|---|
| GET `/` | Static index.html UI |
| GET `/health` | Liveness check |
| GET `/api/stats` | Totals: active/inactive, trigger histogram, complexity histogram, total_nodes, unique_integrations |
| GET `/api/workflows?q=&trigger=&complexity=&active_only=&page=&per_page=` | Paginated FTS-ranked search (per_page ≤ 100) |
| GET `/api/workflows/{filename}` | Metadata + raw JSON |
| GET `/api/workflows/{filename}/download` | File download |
| GET `/api/workflows/{filename}/diagram` | Generated Mermaid flowchart code |
| GET `/api/integrations` | Unique integration count |
| GET `/api/categories` | Category list (from context/unique_categories.json, fallbacks built in) |
| GET `/api/category-mappings` | filename → category dict for client-side filtering |
| GET `/api/workflows/category/{category}` | Category-filtered search |
| POST `/api/reindex?admin_token=` | Background re-indexing, disabled unless ADMIN_TOKEN env var set |

Pydantic models (`WorkflowSummary`, `SearchResponse`, `StatsResponse`) validate all outputs; a `field_validator` coerces int→bool for `active` because SQLite stores booleans as integers — a nice interop gotcha to remember.

### 3.1 Security model — worth studying
This codebase survived a security audit (all CVEs resolved per README). Concrete mechanisms:

- **Path traversal defense**: filenames are URL-decoded **three times** (catches nested encodings like `%252e%252e%252f`), then checked against a blocklist (`..`, backslash, null bytes, newlines, `~`, drive letters, shell metacharacters), then regex-whitelisted to `^[a-zA-Z0-9_\-]+\.json$`. Then — belt and braces — after locating the file on disk, it verifies `file.resolve().relative_to(workflows_path)` succeeds before opening. Three independent layers.
- **Rate limiting**: in-memory defaultdict of timestamps per client IP, 60 requests/minute window, expired entries pruned on each check. Simple, no Redis needed at this scale.
- **CORS**: explicit allowlist — localhost:3000/8000/8080, the GitHub Pages origin, and a community Render deployment. Methods restricted to GET/POST; headers to Content-Type + Authorization.
- **Compression**: GZip middleware for responses ≥ 1 KB.
- **Ops**: startup event fails fast if DB unreachable; global exception handler returns JSON 500s; access logging enabled.

### 3.2 Mermaid diagram generator
`generate_mermaid_diagram()` converts any workflow JSON into a `graph TD` flowchart: nodes become sanitized IDs with labels `Name<br>(type)`, color-styled by role — blue for triggers/webhooks/cron, yellow for IF/Switch conditionals, purple for Function/Code, red for error handlers, gray otherwise — and edges labeled with output index when a node has multiple branches. This is how every workflow card renders its preview diagram. If you want to visualize your own n8n exports in Obsidian docs, this exact algorithm is reusable in a few lines of script.

## 4. Deployment & Delivery

Three deployment surfaces ship from one repo:

1. **GitHub Pages static site** (`docs/` folder) — the zero-backend public face at zie619.github.io/n8n-workflows, vanilla JS + Tailwind CSS, dark/light mode, mobile-ready, direct JSON downloads.
2. **Docker image** — multi-platform builds (linux/amd64 + linux/arm64) published as `zie619/n8n-workflows:latest`; container hardened (non-root user), Trivy-scanned in CI.
3. **Render free-tier community deployment** — whitelisted in CORS, proving the stack runs on ephemeral hosts.

CI runs through GitHub Actions. Funding is a Buy Me a Coffee link. The site cross-promotes Trusera's AI-BOM scanner ("discover Shadow AI in n8n workflows") — evidence of the maintainer's broader ecosystem play around n8n security.

## 5. Steal-Worthy Design Lessons

1. **Derived-state architecture**: source of truth = flat files; everything else (DB, diagrams, stats) is rebuildable cache. Backups trivial, corruption recoverable.
2. **Precompute for speed**: FTS5 index + MD5 skip-list delivers 100 ms search on commodity hardware without Elasticsearch.
3. **Layered input validation** beats any single clever check.
4. **Auto-generated metadata** (names, descriptions, categories) makes large corpora browsable with near-zero curation labor.
5. **Ship three surfaces** (static site for discovery, API for automation, Docker for self-host) from one codebase — the same triple could power *your* future template store or client portal.

## 6. How To Exploit These Endpoints Today

```powershell
# Live stats snapshot
curl.exe https://zie619.github.io/n8n-workflows/api/stats   # if proxied; else use Render deploy
curl.exe https://n8n-workflows-1-xxgm.onrender.com/api/stats

# Search the corpus programmatically
curl.exe "https://n8n-workflows-1-xxgm.onrender.com/api/workflows?q=telegram&complexity=medium&per_page=50"

# Bulk-acquire everything locally (fastest path)
git clone --depth 1 https://github.com/Zie619/n8n-workflows.git
```

With a local clone you own all 4,343 JSONs permanently — no rate limits, offline search, raw material for template products (see Research 05).

---
*Research series:   [[research/02-workflow-science|next]]*
