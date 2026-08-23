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
