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

## Cross-Vault Links

- [[systems-design-distributed]] · [[repo-system-design-primer]]
- [[roadmap-data-scientist]] Stage 1 shares the SQL foundation