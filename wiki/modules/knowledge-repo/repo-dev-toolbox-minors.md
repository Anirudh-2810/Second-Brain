---
course_code: "KNOWLEDGE-REPO"
course_name: "Linked Repo Expansions"
unit: "Repo 17 — Developer Toolbox Minors (Grouped Utility Repos)"
tags: [tools, utilities, testing, databases, telegram, visualization, linked-repo]
last_updated: "2026-08-24"
confidence: "high"
source: "Multiple small repos linked from niderhoff/knowledge-repository"
---

## For future agent
All small utility repos from the knowledge-repo README grouped by function — each gets a two-line verdict and when-to-reach-for-it. These don't warrant individual pages; this page is their index. Volatile tools marked.

# Developer Toolbox Minors — Expanded

## Python Craft Utilities

| Repo | Verdict |
|------|---------|
| **instagram/MonkeyType** | Auto-generates type hints from runtime tracing — great bootstrap for typing legacy code; review before committing |
| **rednafi/pysanity** | Opinionated style/philosophy checklist — read once, adopt selectively |
| **norvig/pytudes** *(own page-level coverage in [[languages-python-advanced]])* | Study-quality programs; read like literature |

## Testing & Databases

| Repo | Verdict |
|------|---------|
| **google/googletest** | The C++ unit-test framework standard; learn assertions + fixtures only |
| **pytest-postgresql / pgmock** | Spin real Postgres in integration tests — beats mocking SQL |
| **alembic** | SQLAlchemy migrations; the Python answer to schema versioning |
| **flyway / roundhouse** | DB version control outside Python ecosystems; concept: migrations-as-code |
| **psycopg** | THE Postgres driver for Python; know its parameterized-query idiom (SQL-injection safety) |

## Background Jobs & Messaging

| Repo | Verdict |
|------|---------|
| **rq/django-rq** | Redis Queue for Django — simplest honest background jobs |
| **django-celery era → celery directly** | Historical pypi shim; modern usage configures Celery directly `(TBC)` |
| **tomconte/sample-keda-queue-jobs** | Reference for KEDA queue-triggered scaling demos |

## Bots & Scraping

| Repo/Doc | Verdict |
|----------|---------|
| **Telethon docs** | Full Telegram MTProto client (user-account bots too) — more powerful than Bot API alone |

## Vision / Interactive ML

| Repo | Verdict |
|------|---------|
| **poloclub/cnn-explainer** | In-browser interactive CNN — best teaching artifact for conv layers; show non-ML friends here |
| **victordibia/handtracking** | SSD hand detector w/ pretrained model — quick AR-style demos |
| **google/graph_distillation** | Research code for label-transfer across datasets; niche |

## Infra Utilities

| Tool | Verdict |
|------|---------|
| **liyasthomas/postwoman (now Hoppscotch)** | Open-source Postman in browser; fast API poking |
| **k8syaml.com** | YAML scaffolding generator; start-then-edit tool |
| **Pulumi** | Infra-as-code in real languages vs YAML/HCL; steeper but durable skill |
| **KeyDB** | Multithreaded Redis fork; reach for Redis bottlenecks `(TBC: project activity as of 2026)` |
| **yolossn/Prometheus-Basics** | Metric types → PromQL primer repo; one-evening read before any monitoring work |
| **DigitalOcean nginx config generator** | UI that emits sane nginx configs; learning tool more than prod crutch |

## Reach-For Rules

```mermaid
flowchart TD
    N["Need..."] --> C{"Category"}
    C -->|"types"| M["MonkeyType -> manual pass"]
    C -->|"tests hit real DB"| P["pytest-postgresql"]
    C -->|"schema changes"| A["Alembic"]
    C -->|"background job"| R["django-rq first,<br/>Celery when complex"]
    C -->|"poke an API"| H["Hoppscotch"]
    C -->|"explain CNNs"| CE["cnn-explainer link<br/>in your notes"]
```

## Cross-Vault Links

- [[languages-python-advanced]] · [[systems-design-distributed]] · [[python-datascience-topics]]
- [[modules/automations/quick-start-guide]] — Telegram via n8n as no-code alternative