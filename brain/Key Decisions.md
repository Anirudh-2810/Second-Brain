---
description: "Architectural and workflow decisions worth recalling across sessions — each links to its source work note"
tags:
  - brain
---

# Key Decisions

Architectural or workflow decisions worth recalling. Link to the full [[Decision Record]] when one exists.

## Vault Architecture

- **2026-08-23 — Adopted obsidian-mind core into Second Brain, then stripped to essentials.** Installed [obsidian-mind](https://github.com/breferrari/obsidian-mind) by clone+merge, then removed all corporate machinery (`work/`, `org/`, `perf/`, `reference/`, `.claude/`, `.codex/`, `.gemini/`). Rationale: vault is a *student* second brain; the template's review-prep/Slack/people stack was dead weight. Kept: brain memory system, linking laws, write-validation, command suite.
- **2026-08-23 — opencode-first, single AGENTS.md.** Merged old `Agent.md` (wiki system spec) + mind's operating manual into one `AGENTS.md`. No CLAUDE.md/GEMINI.md — opencode reads AGENTS.md natively. Claude-specific hook scripts were NOT reused; equivalent behavior lives in `.opencode/plugins/mind.ts`.
- **2026-08-23 — Home.md is the vault home.** No separate template Home; the user's habit-tracker note became the home dashboard (originally `Heatmap.md`, renamed to `Home.md` the same day) with live sections: today's/carry-over tasks, open tasks, North Star embed, mental-health signals, 7-day overview, habit heatmaps.
- **2026-08-23 — Wins live in brain/, not perf/.** `[[Wins]]` replaces the Brag Doc concept, sized for a student.
- **2026-08-23 — raw-sources stays immutable; reference/ deleted.** External knowledge has exactly one inbox: `raw-sources/` → distilled to `wiki/modules/`.

## Retrieval Agent Architecture (Business Brain)

- **2026-08-24 — Grounded Q&A only: no general knowledge fallback.** The retrieval agent (`wiki/modules/retrieval-agent/`) is designed to *only* answer from the vector-searched brain. If the brain doesn't have it, the agent refuses ("That's not in the brain yet"). This prevents hallucination in business contexts where wrong answers are worse than no answers. Source: `[[wiki/modules/retrieval-agent/retrieval-agent#rule-6-refuse-when-not-in-brain-critical]]`
- **2026-08-24 — Tool errors ≠ empty results (critical distinction).** If the Edge Function returns any error (DNS, 401, 500, timeout), the agent must say "I can't reach the brain right now — that's a system problem, not a missing note" and STOP. Without this rule, a downed database looks identical to "fact not documented" — same words, opposite meaning. Source: `[[wiki/modules/retrieval-agent/retrieval-agent#rule-5-tool-errors--empty-results-critical]]`
- **2026-08-24 — n8n as orchestration layer, not logic layer.** n8n handles Chat Trigger → AI Agent → HTTP Request tool wiring. All business logic (search, embedding, vector query) lives in the Supabase Edge Function. This keeps n8n workflows portable and the heavy lifting in version-controlled code. Source: `[[wiki/modules/retrieval-agent/n8n-setup]]`
- **2026-08-24 — Heading-aware chunking with metadata preservation.** Ingestion chunks Markdown by heading (preserving heading path), embeds each chunk, stores path + heading + confidence + status + frontmatter in `brain_chunks.metadata`. This enables filtered search (by confidence/status) and human-readable citations. Source: `[[wiki/modules/retrieval-agent/database-schema#ingestion-chunking-strategy]]`
- **2026-08-24 — Confidence & status as first-class filterable fields.** Every chunk carries `confidence` (high/medium/low/speculation) and `status` (draft/published/archived). The agent weights answers by these fields and the search RPC filters by them. This makes "unverified" content explicit and filterable. Source: `[[wiki/modules/retrieval-agent/database-schema#table-definition]]`, `[[wiki/modules/retrieval-agent/retrieval-agent#rule-8-confidence--status-weighting]]`
