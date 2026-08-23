---
description: "Freeform capture. Dump anything — decisions, gotchas, wins, study notes, thoughts — and it gets routed to the right notes."
---

Process this freeform dump. For each distinct piece of information:

1. **Classify** per the AGENTS.md routing table: decision, gotcha, pattern, memory, win, study material, or daily log
2. **Search first** (grep or `qmd query` if installed) for a related existing note — prefer appending small updates over creating duplicates
3. **File it correctly**:
   - Decisions → `brain/Key Decisions.md` (Decision Record template if it deserves its own note)
   - Gotchas → `brain/Gotchas.md` · Patterns → `brain/Patterns.md`
   - Wins → `brain/Wins.md` · Other durable facts → relevant `brain/` topic note
   - Study material → `wiki/modules/<subject>/` following the ingestion workflow (frontmatter, cross-links, index + log update)
   - Day-to-day log → today's `daily/` note
4. **Frontmatter + links on everything**: `date`, `description`, `tags`, at least one `[[wikilink]]`
5. **Update indexes** touched: `wiki/index.md`, `wiki/log.md`, `brain/Memories.md`

Finish with a filing summary: what was captured, where it went, new notes created, and anything ambiguous (ask).

Content to process:
$ARGUMENTS
