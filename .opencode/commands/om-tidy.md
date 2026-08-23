---
description: "Vault hygiene pass. Find orphans, broken links, oversized notes, stale thinking pads, outdated indexes — then act."
---

Act on vault hygiene findings. Never delete without explicit confirmation; move carefully (vault may not be git-tracked yet).

Scan for:
1. **Orphans** — markdown notes with zero inbound and zero outbound `[[wikilinks]]` (exclude `.obsidian/`, `.opencode/`, `templates/`, `raw-sources/`)
2. **Broken links** — `[[wikilinks]]` pointing at nonexistent notes
3. **Oversized notes** — any note over ~25KB; propose a split (atomic child notes + one-liner index left behind), never trimming
4. **Stale thinking pads** — old `thinking/YYYY-MM-DD-*.md` drafts whose findings were already promoted (propose deletion, ask first)
5. **Index drift** — `wiki/index.md`, `wiki/log.md`, `daily/index.md`, `brain/Memories.md` missing recent additions

For each finding: report it, then fix what's unambiguous. For judgment calls (archiving, deleting, splitting), propose and wait for approval.
