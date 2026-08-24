---
course_code: "DATA-SCI"
course_name: "Data Science & Machine Learning Field"
unit: "Repo 5 — datastacktv/data-engineer-roadmap"
tags: [roadmap, data-engineering, curriculum, linked-repo]
last_updated: "2026-08-24"
confidence: "medium"
source: "https://github.com/datastacktv/data-engineer-roadmap"
---

## For future agent
The popular visual data-engineer roadmap (2020; image-based README, so this page reconstructs its stage sequence from the repo + standard knowledge of its content). Data engineering is a strong 2026 track ([[market-analysis-tech-2026]]: "strong, steady demand"). Pair with [[repo-scalability-catalogs]] for infra depth.

# Data Engineer Roadmap — Expanded

## The Stage Sequence (as the roadmap orders it)

```mermaid
flowchart TD
    A["CS Fundamentals:<br/>how computers work,<br/>basic algorithms"] --> B["One backend language<br/>(Python or Go/Java)"]
    B --> C["Testing & tooling:<br/>pytest, editors, git"]
    C --> D["SQL deep<br/>(window fns, tuning)"]
    D --> E["NoSQL families<br/>(Redis/Mongo/Cassandra)"]
    E --> F["Data warehouses & modeling<br/>(Snowflake/BigQuery/Redshift,<br/>star schema, OLAP)"]
    F --> G["Frameworks:<br/>Spark (batch),<br/>Kafka (streaming)"]
    G --> H["Orchestration:<br/>Airflow / Luigi / Prefect"]
    H --> I["Cloud platform:<br/>AWS/GCP/Azure data stack"]
    I --> J["DevOps-lite:<br/>Docker, CI/CD, monitoring"]
```

## What Each Stage Means in Practice

| Stage | Minimum Competence Signal |
|-------|--------------------------|
| SQL | Multi-join window-function queries from blank editor |
| Warehouse modeling | Explain star vs snowflake; why columnar storage suits OLAP |
| Spark | Read→transform→write a 10GB job; explain partitions & shuffles |
| Kafka | Producer/consumer demo; at-least-once vs exactly-once vocabulary |
| Airflow | DAG with dependencies + retries + backfill understanding |

## Why Consider This Track (2026 lens)

- Demand rated "strong, broad" while entry-generalist shrinks ([[market-analysis-tech-2026]])
- Less interview DSA pressure than SWE loops; more systems+SQL
- Natural extension of skills you're already building (SQL in [[roadmap-data-scientist]] Stage 1)

## Quit Points

| Quit Point | Counter |
|------------|---------|
| Tool sprawl panic ("Hadoop? Snowflake? Kafka?!") | The roadmap is a map, not a to-do-everything list. Core = Python+SQL+Spark+Airflow+one cloud |
| Cluster envy | Local Dockerized Spark + free-tier BigQuery cover ALL learning stages |

## Example Checkpoint Questions

1. Why are warehouses columnar? What query pattern benefits?
2. Kafka: what does a consumer group guarantee? When do duplicates appear?
3. Your nightly Airflow DAG failed mid-backfill — what does idempotency mean for your tasks?

## Deep Edition Addendum

**Failure modes of DE-roadmap followers**:

| Failure | Mechanism | Counter |
|---------|-----------|---------|
| Tool sprawl paralysis | Learning 15 tools at surface level | Core five: Python+SQL+Spark+Airflow+one cloud |
| Hadoop nostalgia trap | 2020-map followed literally | Learn concepts; deploy modern equivalents `(2026 reality)` |
| No data to pipeline | Learning orchestration without real data | Pick a public dataset with daily updates FIRST |
| Skipping SQL depth | Rushing to Spark | DE interviews screen SQL hardest at entry |

**Premortem**: *"Data engineer in training" for a year; nothing pipelined.* Findings: Kafka studied before any producer existed; Airflow DAGs on fake data; zero warehouse experience because "free tiers feel limited." Fix pattern: one REAL dataset (e.g., city open-data dumps) flowing through every stage of the roadmap as it's learned.

**Rescue flowchart**:
```mermaid
flowchart TD
    S["DE learning stalled"] --> Q{"Where?"}
    Q -->|"Spark won't behave"| L["Local Dockerized Spark +<br/>tiny dataset. Scale later"]
    Q -->|"Kafka abstract"| P["Producer = your own script<br/>streaming something you care about"]
    Q -->|"Airflow confusing"| A["One DAG: extract->load,<br/>schedule daily, add retry"]
    Q -->|"tool FOMO"| CORE["Re-read core-five list.<br/>Ignore the rest until employed"]
    L & P & A & CORE --> G["Ship one working pipeline"]
```

**Life integration**: pipeline runs daily → its failures become your ops education; weekly review checks DAG health; metrics = days-pipeline-alive streak, stages completed against the map.

## Cross-Vault Links

- [[systems-design-distributed]] · [[repo-system-design-primer]]
- [[roadmap-data-scientist]] Stage 1 shares the SQL foundation