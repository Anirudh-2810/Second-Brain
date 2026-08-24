---
course_code: "KNOWLEDGE-REPO"
course_name: "Knowledge Repository — Curated Learning Resources (niderhoff)"
unit: "Module 10 — Systems Design & Distributed Systems"
tags: [systems-design, distributed-systems, hadoop, docker, kubernetes, airflow, celery, caching, monitoring, scalability]
last_updated: "2026-08-24"
confidence: "high"
source: "https://github.com/niderhoff/knowledge-repository#systems-design"
---

## For future agent
Backend/distributed-systems resources: scalability pattern catalogs, system-design interview material, container orchestration best practices (Docker/K8s), workflow engines (Airflow/Celery/KEDA), and infra utilities. Use when designing a backend, preparing for system design rounds, or debugging K8s.

# Systems Design & Distributed Systems

## Pattern Catalogs & Primers
- **[awesome-scalability](https://binhnguyennus.github.io/awesome-scalability/)** — the patterns of scalable/reliable/performant large-scale systems; massive index
- **[System Design Primer (donnemartin)](https://github.com/donnemartin/system-design-primer)** — THE system design study guide: building blocks + worked designs + flashcards
- [awesome-system-design (madd86)](https://github.com/madd86/awesome-system-design) — second catalog
- Book (from reading list): **[Designing Data-Intensive Applications (Kleppmann)](https://dataintensive.net/)** — the distributed-systems bible

## Big Data
- **[Hadoop: The Definitive Guide (O'Reilly)](http://hadoopbook.com/**)** — canonical Hadoop text
- [Free 3-node Hadoop cluster starter kit](http://hadoopinrealworld.com/hadoopstarterkit/)
- 2026 note `(TBC)`: Hadoop-era batch stack has largely yielded to cloud warehouses (BigQuery/Snowflake) + Spark; learn concepts here, tools elsewhere

## Data Serialization
- [FlexBuffers (schema-less Flatbuffers)](https://google.github.io/flatbuffers/flexbuffers.html) · [HN discussion](https://news.ycombinator.com/item?id=23588558)
- Protobuf adjacent: [Apache Arrow Flight](https://arrow.apache.org/blog/2019/10/13/introducing-arrow-flight/) — columnar transport claiming faster-than-gRPC data transfer

## Docker Best Practices
All three from NodeBestPractices but language-agnostic:
- [Lint your Dockerfile](https://github.com/goldbergyoni/nodebestpractices/blob/master/sections/docker/lint-dockerfile.md)
- **[Avoid build-time secrets](https://github.com/goldbergyoni/nodebestpractices/blob/master/sections/docker/avoid-build-time-secrets.md)** — secrets baked into layers leak forever
- **[Multi-stage builds](https://github.com/goldbergyoni/nodebestpractices/blob/master/sections/docker/multi_stage_builds.md)** — build toolchain out of final image

## Kubernetes

### Learn
- [Katacoda interactive K8s courses](https://www.katacoda.com/courses/kubernetes) — browser labs
- [Magic Sandbox bootcamp platform](https://www.msb.com/)
- [A Gentle Introduction to Kubernetes](https://medium.com/faun/a-gentle-introduction-to-kubernetes-4961e443ba26)

### Avoid Mistakes
- **[10 most common mistakes using kubernetes (pipetail)](https://blog.pipetail.io/posts/2020-05-04-most-common-mistakes-k8s/)** — liveness/readiness misuse, no requests/limits, latest tags… · [HN thread](https://news.ycombinator.com/item?id=23211325)
- [Validating K8s YAML for best practice (learnk8s)](https://learnk8s.io/validating-kubernetes-yaml)

### Tooling
- [Kubernetes YAML Generator](https://k8syaml.com/)
- [Pulumi](https://www.pulumi.com/kubernetes/) — define K8s infra in ts/python/go instead of YAML

## Workflows / Pipelines / Messaging
- [Apache Airflow on Kubernetes Executor + MiniKube (Marc Lamberti)](https://marclamberti.com/blog/airflow-kubernetes-executor/#Introducing_Apache_Airflow_with_Kubernetes_Executor)
- KEDA autoscaling: [queue-triggered jobs sample](https://github.com/tomconte/sample-keda-queue-jobs)
- Celery at scale: **[Scaling effectively when Kubernetes met Celery](https://hackernoon.com/https-medium-com-talperetz24-scaling-effectively-when-kubernetes-met-celery-e6abd7ce4fed)**
- Python-side pairing: django-celery/django-rq in [[languages-python-advanced]]

## Infrastructure Utilities
| Area | Resource |
|------|----------|
| nginx config | [DigitalOcean nginx config generator UI](https://www.digitalocean.com/community/tools/nginx) |
| Caching | [KeyDB](https://docs.keydb.dev/blog/2019/10/07/blog-post/) — multithreaded Redis fork ("5× faster") |
| Monitoring | [Prometheus Basics (yolossn)](https://github.com/yolossn/Prometheus-Basics) — metric types → PromQL primer |
| API testing | [postwoman/Hoppscotch](https://github.com/liyasthomas/postwoman) — open-source Postman alternative |
| Video streaming | [Go + HLS media server how-to](https://hackernoon.com/building-a-media-streaming-server-using-go-and-hls-protocol-j85h3wem) |

## Cross-Vault Links

- [[mlops-production-deployment]] — ML-specific serving on top of these patterns
- [[modules/programming/SAAS_BUILD_NOTES]] — SaaS deployment checklist using this stack's cloud-managed equivalents
- [[software-dev-general]] — architecture thinking that precedes infrastructure
- [[overview]] — module hub