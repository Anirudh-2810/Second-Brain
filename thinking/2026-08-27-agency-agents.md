---
date: "2026-08-27"
description: "Roster digest of the msitarzewski/agency-agents catalog (230+ agent definitions, 18 divisions): what was learned, the 8 installed conversions, the full division map for on-demand future conversions, install paths, and apply-to-builds mapping."
context: "agency-agents repo deep-dive + 8 subagent conversions into .opencode/agents/ (learning-and-appending session)"
tags:
  - thinking
---

# 2026-08-27 — agency-agents roster digest

## Question / Problem

The [agency-agents](https://github.com/msitarzewski/agency-agents) repo (148k★, 400 commits, MIT) ships 230+ AI agent definitions across 18 divisions. How much of it is worth wiring into the Second Brain — and where?

## Conclusions (what was done)

- **Installed 8** curated conversions into `.opencode/agents/` (distilled, local format): multi-agent-systems-architect, rag-pipeline-engineer, prompt-engineer, codebase-archaeologist, minimal-change-engineer, agents-orchestrator, zk-steward, knowledge-graph-engineer. Vault now has 12 subagents (4 pre-existing: context-loader, correction-sweep, cross-linker, vault-librarian).
- **Rejected full-roster import** — opencode caps ~119 agents and silently drops the rest (`anomalyco/opencode#27988`, see `[[Gotchas]]`); the catalog is a reference library, not an install target.
- **Created** `templates/agent-definition.md` (reusable conversion template), `brain/Agentic AI Playbook.md` (portable principles). No new wiki module — user chose vault-native distribution over a new `AI-Data/agentic-ai/` folder.
- Portable principles (also in the playbook): 5 topologies, context-budget compounding, fallback ladders + circuit breakers, HITL gate placement, least privilege, eval-driven dev (≥20 cases/baseline/meets-or-exceeds), prompt-injection isolation.

## The full roster map (18 divisions — for on-demand conversion)

| Division | Agent count (approx) | Notable agents for THIS vault |
|---|---|---|
| engineering | ~45 | multi-agent-systems-architect ✓, rag-pipeline-engineer ✓, prompt-engineer ✓, minimal-change-engineer ✓, knowledge-graph-engineer ✓, (+ sw reporter, dev ops shelver, cloud infra, api, database, backend pipeliner, ai-web-app, mcp, llm-integration) |
| specialized | ~25 | agents-orchestrator ✓, zk-steward ✓, codebase-archaeologist ✓, (+ reality checker, pomodoro engineering, decision framework, cares build audit, security — prompt injection jailbreaker, environment variables, yaml, docker, iac) |
| data | ~30 | data pipeline spec, analisis heredado, metrics y alertas, data products, sql analytics, dashboard |
| academic | ~15 | academic analyst, evaluator, methodology, literature review — study help |
| research | ~15 | deep research, dev research, evals, field researcher |
| finance | ~20 | var modeler, backtester, factor-research, tradebook auditor, market microstructure |
| marketing / sales / paid-media / product / project-management / design / game-development / gis / healthcare / security / spatial-computing / support / testing | many | mostly not aligned with current goals — leave uninstalled |

✓ = installed 2026-08-27.

## Agent-file anatomy (why pre-built agents port so well)

Each `*.md` has YAML frontmatter (`name`, `emoji`, `description`, `color`, `vibe`) + body: identity & memory (role/personality/memory/experience), core mission, critical rules, deliverables/workflows, success metrics. Conversion = keep the mission/rules/method, re-emit YAML in opencode form (`description` + `mode: subagent` + `permission {edit, bash}`), scope examples to the vault. `scripts/convert.sh --tool <tool>` and the Agency Agents app (agencyagents.app) exist but produce tool-native YAML; our distilled manual conversion keeps size sane.

## Install paths (recorded for future use)

- Repo: `scripts/install.sh --tool <tool> <divisions...>` bulk-installs into tool config dirs.
- `scripts/convert.sh --tool <tool>` converts the pack to a given tool's format.
- Agency Agents app (agencyagents.app) — GUI install across 15+ tools.
- Manual: copy the `.md` into `.opencode/agents/` + restart opencode (config not hot-reloaded).

## Next Steps

- [x] Restart opencode; verify all 8 new agents register (confirmed available after reboot 2026-08-27)
- [ ] If any division becomes relevant (e.g., finance for quant, data for DS), convert on demand using `templates/agent-definition.md`
- [ ] Consider a `[[Skills]]` slash-command that lists installed subagents with one-line use triggers

## Feeds Into

- `brain/Agentic AI Playbook.md` — durable principles + installed library index
- `[[Gotchas]]`, `[[Key Decisions]]` — cap/curation entries