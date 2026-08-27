---
description: "List all installed opencode subagents from .opencode/agents/ with one-line use triggers, grouped by capability."
---

List the installed subagent library for the user.

1. Read every `*.md` in `.opencode/agents/` (12 files).
2. For each, take the frontmatter `description` as its one-line purpose.
3. Present a table: `Name | Call with | What it's for | Permissions` — the "Call with" column is the `@name` trigger and the build/study context it serves (e.g., `@rag-pipeline-engineer` → audit retrieval-agent retrieval quality).
4. Group rows: Writes (can edit notes), Audits (read-only + bash), Advisory (read-only).
5. Close with: total count, how to add more (copy an agent definition into `.opencode/agents/` + restart opencode — config is not hot-reloaded), and the provenance note that 8 of 12 were distilled from msitarzewski/agency-agents (see `[[Agentic AI Playbook]]`).