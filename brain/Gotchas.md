---
description: "Things that have bitten before and will bite again — pitfalls, edge cases, and testing traps"
tags:
  - brain
---

# Gotchas

Things that have bitten before and will bite again.

## Tools & Environment

- **2026-08-23 — Gemini share links are JS-rendered.** `share.gemini.google/<id>` redirects to `gemini.google.com/share/<id>`, but the HTML is an ~820KB empty shell — conversation data loads via client-side RPC. Plain `webfetch`/`Invoke-WebRequest` gets nothing; needs a headless browser (Browserless/Firecrawl) or a manual paste.
- **2026-08-23 — PowerShell flags git's stderr progress as errors.** `git clone` writes progress to stderr, which PowerShell 5.1 surfaces as `NativeCommandError`. Harmless noise — verify success by checking the result (`Test-Path .git`), not by absence of red text.
- **2026-08-23 — opencode directories are plural.** `.opencode/commands/`, `.opencode/agents/`, `.opencode/plugins/` (confirmed against docs). Claude Code conventions are singular (`.claude/commands`) — don't mix them when porting templates.
- **2026-08-23 — obsidian-mind hook scripts are Claude-Code-shaped** (stdin JSON events: SessionStart, PostToolUse…). They don't run under opencode; equivalent logic must be reimplemented as an opencode plugin (`tool.execute.after`, `experimental.session.compacting`).
