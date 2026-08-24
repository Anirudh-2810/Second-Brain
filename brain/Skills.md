---
date: 2026-08-23
description: "Catalog of vault slash commands, subagents, and workflows — the canonical reference for what the mind can do"
tags:
  - brain
  - index
---

# Skills

Slash commands live in `.opencode/commands/`, subagents in `.opencode/agents/`, write-validation in `.opencode/plugins/mind.ts`. This note is the canonical catalog — keep it current when commands change.

## Slash Commands

### Daily Workflow

| Command | Purpose |
|---------|---------|
| `/om-standup` | Morning kickoff — North Star, recent dailies, streaks, open loops, suggested focus |
| `/om-dump` | Freeform capture — dump anything; each piece gets classified and routed per AGENTS.md |
| `/om-wrap-up` | Session review — verify filing, links, indexes, persist learnings. Auto-triggered on "wrap up" |
| `/om-weekly` | Weekly synthesis — study/exercise/mood stats, wiki progress vs North Star, next-week priorities |

### Knowledge & Maintenance

| Command | Purpose |
|---------|---------|
| `/om-ingest` | Distill a `raw-sources/` file into linked `wiki/modules/` concept pages (index + log updated) |
| `/om-ingest-brain` | Chunk & embed `wiki/` pages into `brain_chunks` for retrieval agent (calls Edge Function `embed` mode) |
| `/om-tidy` | Hygiene pass — orphans, broken links, oversized notes, stale thinking pads, index drift. Never deletes without confirmation |
| `/om-correct` | Sweep a corrected fact: fix the single source plus every restatement (grep AND paraphrase), preserve dated history |
| `/om-vault-audit` | Read-only health report — indexes, links, frontmatter, size signals, stale facts |

## Subagents

Invoke with `@name` in opencode.

| Agent | Purpose |
|-------|---------|
| `@context-loader` | Full briefing on any topic — reads everything related, synthesizes, flags gaps |
| `@cross-linker` | Missing wikilinks, orphans, broken backlinks, index drift (read-only) |
| `@vault-librarian` | Deep maintenance — frontmatter repair, split proposals, index rebuilds |
| `@correction-sweep` | Finds every restatement of a corrected fact, classifies authoritative/restatement/historical |

## Retrieval Agent Commands (Proposed)

| Command | Purpose |
|---------|---------|
| `/om-brain-search` | Query the business brain via Edge Function (test search without n8n) |
| `/om-brain-ingest` | Full pipeline: chunk wiki → embed → upsert to brain_chunks → refresh index |
| `/om-brain-stats` | Coverage report: chunks, notes, embedding %, missing embeddings, index health |

## The Mind Plugin

`.opencode/plugins/mind.ts` runs automatically:
- **After every markdown write**: checks frontmatter (`date`/`description`/`tags`), wikilink presence, ~25KB size signal — appends hints to the tool result
- **Before compaction**: injects persistence rules so long sessions don't lose routing knowledge

## Semantic Search (QMD) — optional

Install once: `npm install -g @tobilu/qmd`, then `node --experimental-strip-types .scripts/qmd-bootstrap.ts`. Then prefer over grep:

```bash
qmd --index second-brain query "<topic>"    # hybrid semantic + keyword
qmd --index second-brain update             # after bulk edits
```

Without QMD everything falls back to grep — nothing breaks.
