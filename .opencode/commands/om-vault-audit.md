---
description: "Vault audit. Check indexes, wikilinks, orphans, stale content; report health without changing anything."
---

Audit the vault. Read-only report unless asked to fix.

Check:
1. **Indexes**: does `wiki/index.md` match actual `wiki/modules/` pages? Does `wiki/log.md` have entries for recent additions? Is `daily/index.md` current? Is every `brain/` topic note listed in `brain/Memories.md`?
2. **Links**: broken `[[wikilinks]]`, orphaned notes (no inbound links)
3. **Frontmatter**: notes missing `date`, `description`, or `tags` (exclude `templates/`, `raw-sources/`, `.obsidian/`, `.opencode/`)
4. **Size**: any note over ~25KB that should be split
5. **Stale content**: volatile facts without date stamps ("as of YYYY-MM-DD"), unverified claims stated bare (no TBC marker)

Output a prioritized report: critical (broken links, missing frontmatter), important (orphans, drift), cosmetic (stale phrasing). Offer to fix via `/om-tidy` and `/om-correct`.
