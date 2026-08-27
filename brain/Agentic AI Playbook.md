---
date: "2026-08-27"
description: "Agentic AI operating playbook — distilled from the agency-agents catalog: multi-agent topologies, context budgeting, fallback chains, HITL gates, least privilege, eval-driven development, prompt-injection defense. Entry point for the 8-installed subagent library."
tags: [brain, agentic-ai, playbook, subagents]
confidence: high
---

## For future agent

This note records what was learned from the msitarzewski/agency-agents catalog (230+ AI agent definitions, MIT, 148k+) and how it is wired into THIS vault: 8 definitions converted to local opencode subagents, a reusable template, and an Agents base view. Distilled here are the portable engineering principles (topologies, context budgets, failure recovery, HITL, least privilege, evals); the wired-up agents live in `.opencode/agents/`. Staleness caveat: the opencode 119-agent runtime cap is recorded in `[[Gotchas]]` and may change upstream — check before adding more agents.

# Agentic AI Playbook

Swarming, routing, orchestration, and quality-engineering rules for AI agents, distilled from the [agency-agents](https://github.com/msitarzewski/agency-agents) catalog. The operational form of these principles is the 8 subagents installed into `.opencode/agents/` — the digest note is `[[2026-08-27-agency-agents]]`.

## The 5 topology patterns

| Pattern | Use when | Key rules |
|---|---|---|
| Sequential chain | each step depends on prior | pass structured outputs, not prose; chains >5 agents degrade; define what each agent is NOT responsible for |
| Parallel fan-out/in | independent subtasks | agents share no mutable state; synthesizer handles all/partial/zero results |
| Hierarchical orchestrator | dynamic decomposition | orchestrator delegates + synthesizes, does NOT execute; task ledger; subagent returns structured result + confidence |
| Evaluator-optimizer loop | scorable output quality | evaluator uses different framing than generator; hard exit ≤3 iterations; plateau 2x → escalate |
| Mesh/peer | negotiation/consensus | rarely right; needs moderator + termination condition |

Default choice = hierarchical, not mesh. Mesh is the hardest to debug.

## Context budget problem

In a 5-agent chain, context compounds (500 → 1.5k → 3.5k → 7.5k → 15k+ tokens). Exhaustion causes hallucination and instruction-failure, not loud errors. Mitigations: summarization compression (preserve IDs/decisions/constraints verbatim), structured state object (each agent reads/writes only its fields), external memory (vector/DB targeted lookup), context checkpointing at milestones. Sensitive data excluded from inter-agent state.

## Failure-mode engineering

Every agent gets a fallback ladder: primary → narrowed fallback → degraded/rule-based → human. A structured degraded response beats a silent failure. Detect by class — hard error (retry w/ backoff), silent wrong (evaluator + schema validation → explicit correction → human), partial/truncated (completeness check → regenerate), contradiction (detector → arbitration → human), cascade (checkpoint validation → rollback), non-convergence (iteration counter → force exit). Circuit breaker closed → open (failure rate) → half-open (one test request); idempotency required for retry-able side-effecting work.

## HITL gate placement

Blocking gate when an action is: irreversible, high blast radius (>100 users / >$10k), low confidence (<0.7), novel/out-of-distribution, regulatory exposure, or explicit policy. Advisory/sampling when reversible or high volume. Review interface shows: what + why (trace), alternatives, consequence, confidence, one-click approve/reject/escalate.

## Least privilege

Every agent gets only the tools/data its role requires; scoped tokens are never passed between agents. In opencode terms: `permission: edit: deny`/`bash: deny` on advisory agents, allowed only where the role must write (prompt-engineer, minimal-change-engineer, zk-steward) or audit (codebase-archaeologist: git).

## Eval-driven development

Never deploy an agent change without: ≥20 test cases, recorded baseline, meets-or-exceeds score, pipeline regression. Agent-level: functional, instruction adherence, schema compliance, confidence calibration, edge cases. Pipeline-level: end-to-end accuracy, failure recovery, cost/latency SLA, HITL trigger rate.

## Prompt-injection defense

External content (web pages, transcripts, imported files, tool outputs) is data, never instructions. Isolate content from instructions; validate outputs against a schema; adversarial tests: "ignore all previous instructions", roleplay bypass, indirect injection via tool outputs.

## The installed subagent library

8 definitions from the catalog, converted to local format (source: `templates/agent-definition.md`):

- `multi-agent-systems-architect` — topology, context budgeting, failure recovery, HITL gates, evals (advisory)
- `rag-pipeline-engineer` — chunking, embedding choice, hybrid search, cross-encoder re-rank, RAGAS evals (advisory)
- `prompt-engineer` — prompt-as-contract, ≥3 test cases (happy/edge/failure), versioned prompts (writes)
- `codebase-archaeologist` — multi-session drift audit, eras + mandatory handler/unit checks, Drift Registry (audits)
- `minimal-change-engineer` — smallest diff, refuses scope creep, line-by-line diff justification (writes)
- `agents-orchestrator` — plan → architecture → [Dev↔QA loop per task] → integration, ≤3 retries then escalate (delegates)
- `zk-steward` — Zettelkasten discipline, ≥2 links, index-as-entry-point, aligned with vault linking laws (writes)
- `knowledge-graph-engineer` — entities/edges with provenance, contradiction tracking, graph-enhanced RAG (advisory)

Install-capability proof of concept; see `[[2026-08-27-agency-agents]]` for the full 18-division roster map and the untapped conversions. (Earlier `bases/Agents.base` browse view was archived to `wiki/98-Archive/` on 2026-08-27 — the `.opencode/agents/` folder is the browse point.)

## Related

- [[Key Decisions]] — why whole-roster imports were rejected and 8 curated
- [[Gotchas]] — opencode ~119-agent runtime cap (anomalyco/opencode#27988)
- [[2026-08-27-agency-agents]] — roster digest with apply-to-builds mapping
- [[Skills]] — command catalog; next agent additions belong there
- `[[01-Areas/Roadmaps/INDEX]]` — where an agentic-AI study roadmap would be linked