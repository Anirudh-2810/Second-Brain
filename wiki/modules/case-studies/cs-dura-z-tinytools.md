---
course_code: "CASESTUDY"
course_name: "Open-Source Case Studies"
unit: "Case Study 8 — tkellogg/dura + rupa/z [Deep R&D + Build Edition]"
tags: [git, cli-tools, rust, shell, frecency, case-study, build-plan]
last_updated: "2026-08-24"
confidence: "high"
source: "https://github.com/tkellogg/dura + https://github.com/rupa/z"
---

## For future agent
Deep-dive on both tiny tools with exact mechanism inventories (dura's snapshot-branch scheme; z's frecency file format and scoring), WHY each implementation choice exists (Rust daemon vs POSIX shell), and TWO buildable versions — **mini-z for PowerShell** (you'll use it daily on Windows) and **mini-dura in Python**. The most immediately practical builds in this module.

# Tiny Tools: Dura + z — Deep R&D

## Part 1 — Code Inventory

### dura (Rust)
| Piece | Mechanism |
|-------|-----------|
| Watch loop | Scans registered repos for dirty worktrees (libgit2 bindings) |
| Snapshot | `git add -A` equivalent internally → tree written → commit created → ref `refs/dura/<sha>` updated — **HEAD/index untouched** |
| Recovery | Manual: `dura serve` logs recovery hints; you `git checkout <dura-branch>` when disaster strikes |

### z (POSIX shell + awk)
| Piece | Mechanism |
|-------|-----------|
| Hook | `$PROMPT_COMMAND`/chpwd appends `path\|rank\|last-time` to `~/.z` on every cd |
| Score | On lookup: `frecency = rank × age-decay` (age buckets halve weight) |
| Jump | Substring best-match over scores; winner becomes cd target |

## Part 2 — Why Those Implementations

| Choice | Why |
|--------|-----|
| dura never touches HEAD/index | Trust: worst case dura adds refs — harmless by construction. Insurance must be provably harmless |
| Rust daemon | Long-lived background reliability; single static binary distribution via cargo |
| z as ~300-line shell+awk | Zero dependencies; readable/modifiable by any user; runs where bash runs |
| Frecency (not MRU, not pure-frequency) | MRU forgets favorites; frequency traps stale dirs. Product × recency decay models habit correctly |

**Design thesis both prove**: the best tools impose ZERO workflow change while removing a catastrophic tail-risk or micro-friction you'd stopped noticing.

## Part 3 — Can I Build My Own Versions? ✅ BOTH — this weekend each

### Build A: **mini-z for PowerShell** ✅ (daily-use flagship)

```powershell
# Spec (~60 lines): 
# 1. Log: function cd wrapper (or custom jd) appends "path|timestamp" to $env:USERPROFILE\.cdhist
# 2. Score: frecency = visits * exp(-daysSinceLast/14)  (14-day half-life-ish)
# 3. jd <substring>: pick best-scoring match, Set-Location there
# 4. Profile install: dot-source from $PROFILE; add jd to prompt-less usage
```

| Milestone | Deliverable |
|-----------|-------------|
| M1 | Logging works across sessions (file grows) |
| M2 | `jd vault` jumps to your Second-Brain dir |
| M3 | Collision handling (list top-5 on ambiguity); prune command |

Failure modes: path-with-spaces parsing (use `|` delimiter strictly), OneDrive-synced profile weirdness (test), forgetting to log non-cd navigations (acceptable).

### Build B: **mini-dura in Python** ✅

```python
# Spec (~120 lines):
# 1. Config list of repo paths
# 2. Every N minutes: for each repo -> if dirty:
#      git add -A && git write-tree && commit-tree -> update refs/mini-dura/head
#    (use subprocess git plumbing; NEVER touch HEAD)
# 3. Recovery helper: mini-dura recover -> lists snapshots w/ timestamps
```

Failure modes: committing huge build artifacts (respect .gitignore — `add -A` honors it), lock contention if user runs git simultaneously (plumbing is atomic enough at your scale), Windows scheduled-task setup friction (Task Scheduler XML once).

## Part 4 — Life Integration

- mini-z pays off EVERY terminal session from day two — fastest gratification build available
- mini-dura insures THIS VAULT — your second brain deserves crash insurance beyond GitHub pushes
- Metrics: jd-hit-rate daily · mini-dura snapshots count · one real recovery performed (the graduation event)

## Checkpoint Questions

1. Derive why frecency beats pure-MRU after a 2-week vacation.
2. Why is dura safe BY CONSTRUCTION — what's the invariant?
3. What pain of yours repeats 3×/day that deserves its own tiny tool next?

## Cross-Vault Links

[[modules/case-studies/index|Field Index]] · [[cs-jj-vcs]] · [[repo-art-of-command-line]] · [[Gotchas]]