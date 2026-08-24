---
course_code: "LEARNRES"
course_name: "Learning Resource Catalogs"
unit: "Resource 2 — ripienaar/free-for-dev"
tags: [free-tiers, cloud, devops, catalogs, learning-resources]
last_updated: "2026-08-24"
confidence: "high"
source: "https://github.com/ripienaar/free-for-dev"
---

## For future agent
The definitive list of free developer tiers (cloud compute, SaaS, APIs, CI, monitoring — 250KB+ of entries). This page converts it into a decision tool: which free tier serves which stage of your projects, plus the cost-trap failure modes. Fetched 2026-08-24.

# Free-for-Dev — The Free Tier Atlas

## What It Contains

Sections spanning the entire dev stack: major cloud providers' free tiers, PaaS/hosting, CI/CD, APIs (AI, maps, email…), databases, monitoring, DNS, code-quality tools. The value: knowing what's legitimately free BEFORE paying or self-hosting unnecessarily.

## Stage-Mapped Usage for This Vault's Projects

| Need | Where to Look | Vault Example |
|------|--------------|---------------|
| Host a model/API 24/7 free | PaaS section (Render/Fly/Railway-class) | [[roadmap-ml-engineer]] Stage 3 deployment |
| Free GPU notebooks | AI/ML section (Colab/Kaggle) | DL experiments |
| CI for repos | CI/CD section | All portfolio projects |
| Email sending (bots) | Email section | Telegram/automation builds |
| Monitoring/ping | Monitoring section | Keep-warm + uptime for deployed demos |

## Failure Modes

| Failure | Mechanism | Counter |
|---------|-----------|---------|
| **Free-tier archaeology** | Spending hours comparing 5 identical tiers | Decision rule: pick first that meets need, revisit only on pain |
| Card-on-file traps | "Free" requiring credit card → surprise charges | Prefer no-card tiers for learning; calendar-reminder before trial ends |
| Tier-dependency | Project architecture welded to one vendor's free limits | Design for portability: containerize ([[systems-design-distributed]]) |
| Sign-up sprawl | Accounts everywhere = security surface | Track credentials in a manager; unique emails per tier if possible |

**Premortem**: *Surprise ₹3,000 charge from a "free" tier.* Root cause: card-on-file + forgotten auto-scale. Counter-rules above are cheaper than any dispute process.

## Life Integration

- Consult ONLY at deploy-time decisions; never browse recreationally
- Every deployed project logs its hosting tier + renewal date in its README
- Metrics: monthly cloud spend (target ₹0 during learning), services alive

## Example Checkpoint Questions

1. Which of my current services run on which tier — and when does each expire?
2. Is anything I pay for actually replaceable by a listed free tier?

## Cross-Vault Links

[[programming/learning-resources/index|Field Index]] · [[mlops-production-deployment]] · [[build-project-playbook]]