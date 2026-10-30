---
course_code: "OMNIROUTE"
course_name: "OmniRoute AI Gateway"
unit: "AI Coding & Routing Infrastructure"
tags: [ai, gateway, llm, routing, coding, free-tier, omniroute, tooling]
last_updated: "2026-10-30"
confidence: high
description: "OmniRoute - local free-only AI gateway (npm i -g omniroute, v3.8.51). One endpoint http://localhost:20128/v1, ~1100 models via plugin, auto-fallback combo free ($0 enforced: gemini free-tier + OpenRouter :free + kiro). Integrates OpenCode (plugin), Claude Code (ANTHROPIC_BASE_URL), Roo Code (import file). Server control, call logging in storage.sqlite, CLI recipes inside."
---

## For future agent

Setup + operations manual for the user's OmniRoute gateway, the $0-only LLM router serving all coding tools. Everything here was verified by live CLI/API tests unless marked (TBC). API keys are NEVER written in this note - single source is `C:\Users\Asus\.local\share\opencode\auth.json`. Staleness: model/combo names drift with provider catalogs; re-verify with `omniroute combo list` / dashboard before relying on them. Debugging steps live in `brain/Gotchas.md` (OmniRoute section).

# OmniRoute - Free AI Gateway

> One local endpoint (`http://localhost:20128/v1`) routing to free providers (gemini, OpenRouter `:free`, kiro) with an auto-fallback combo. **$0 enforced** - the OpenRouter key's balance is $0 and fails closed (403, no charges). Verified end-to-end with OpenCode (plugin, ~1100 models), Claude Code, and Roo Code. (TBC: full provider/model catalog size.)

## Quick Start

| Step | Action |
|------|--------|
| 1 | Ensure server is running: `http://localhost:20128/api/health` -> `{"status":"ok"}`. If not: `Start-Process "omniroute.cmd" -ArgumentList "serve" -WindowStyle Hidden` (binary at `C:\Users\Asus\AppData\Roaming\npm\omniroute.cmd`), wait ~12s |
| 2 | OpenCode: restart TUI -> press **Tab** -> select `opencode-omniroute/...` model or the `free` combo system default |
| 3 | Claude Code: `C:\Users\Asus\.claude\settings.json` has `ANTHROPIC_BASE_URL: http://localhost:20128` + model `free`. Test: `claude -p "reply with OK only" --output-format text` (the `[claude-code:unrecognized_model]` warning is cosmetic) |
| 4 | Roo Code (VS Code): import `C:\Users\Asus\.omniroute\roo-settings.json` -> select **OmniRoute** profile -> model `free` |
| 5 | Verify $0 spend in dashboard -> logs/usage; test requests should show a free model at $0 cost |

## Free-Only Setup ($0 Enforced)

| Component | Status |
|-----------|--------|
| Providers | `gemini` (free tier), `kiro` (OAuth, ~50 credits/mo; ToS bans third-party proxy - use sparingly), `openrouter` ($0 balance, `:free` models only) |
| Combo `free` | Priority chain of 5 free models - no paid model in the chain |
| OpenCode default | `opencode-omniroute/gemini/gemini-3.8-flash` |
| Claude Code | model `free` + `ANTHROPIC_MODEL: free` |
| Roo Code | Profile `OmniRoute` / model `free` |
| Why no money can leak | Combo contains only free-tier models; OpenRouter $0 key returns 403 on paid models (fails closed); Gemini free tier cannot bill without user's Google Cloud billing account |

**Critical habit**: never pick bare `auto` or `openrouter/auto` (can route to paid models). Always `free` combo or a `:free`-suffix model.

## Providers

| Provider | Type | Notes |
|----------|------|-------|
| gemini | API key | Google AI Studio key; biggest free quota, best free coding model - but fragile: 429 quota / 503 high-demand / 504 slow-stream outages happen (see `brain/Gotchas.md` 2026-10-30) |
| kiro | OAuth | ~50 free credits/mo, Claude-class quality; ToS prohibits third-party proxying (TBC: exact terms) |
| openrouter | API key | $0-balance key; works only with `:free` models (~20 RPM / 200 RPD each); fallback workhorse |

## Routing Combo: `free`

Priority order (rebuilt 2026-10-30 - cohere promoted during a Gemini outage; swap back when Gemini is stable):

1. `openrouter/cohere/north-mini-code:free` - code-specialized; only provider answering during Gemini's 2026-10-30 outage
2. `gemini/gemini-3.8-flash` - biggest free quota, best coding quality
3. `openrouter/poolside/laguna-s-2.1:free` - Poolside coding model
4. `openrouter/poolside/laguna-xs-2.1:free` - smaller/faster backup
5. `openrouter/google/gemma-4-31b-it:free` - general fallback

Rebuild recipe (delete prompts y/N - non-interactive shells need `echo y |`):

```powershell
echo y | omniroute combo delete free
omniroute combo create free --strategy priority --models "openrouter/cohere/north-mini-code:free,gemini/gemini-3.8-flash,openrouter/poolside/laguna-s-2.1:free,openrouter/poolside/laguna-xs-2.1:free,openrouter/google/gemma-4-31b-it:free"
omniroute combo switch free
```

## CLI Commands

| Command | Purpose |
|---------|---------|
| `omniroute` | Start server + dashboard (port 20128) |
| `omniroute serve` | Start server only |
| `omniroute combo list` | Show combos (**inverted** flag marks active) |
| `omniroute combo switch free` | Activate combo |
| `omniroute combo create/delete free` | Rebuild combo (delete asks y/N) |
| `omniroute providers list` | Show connected providers |
| `claude -p "prompt" --output-format text` | Claude Code headless test |

## Integrations

### OpenCode
- Plugin at `%APPDATA%\opencode\plugins\omniroute` (v3.8.51; `@opencode-ai/plugin` dep installed inside)
- Global default in `%APPDATA%\opencode\opencode.json`: `"model": "opencode-omniroute/gemini/gemini-3.8-flash"`
- Auth: `C:\Users\Asus\.local\share\opencode\auth.json` - BOM-less UTF-8, keys `omniroute` + `opencode-omniroute` (35-char key). MUST stay BOM-less or plugin reads null
- TUI needs full restart to surface plugin models

### Claude Code
- Settings: `C:\Users\Asus\.claude\settings.json`

```json
{"env":{"ANTHROPIC_BASE_URL":"http://localhost:20128","ANTHROPIC_AUTH_TOKEN":"<35-char key, inject from auth.json>","ANTHROPIC_MODEL":"free","CLAUDE_CODE_DISABLE_UNKNOWN_MODEL_WINDOW_ENFORCEMENT":"1"},"model":"free"}
```

- Key handling: never hand-paste - read auth.json -> `.omniroute.key` -> write settings.json via a script (UTF-8 no BOM). Key never enters chat/logs
- `[claude-code:unrecognized_model]` warning is cosmetic with the guard env var set
- Verified 2026-10-30: `claude -p "reply with OK only" --output-format text` -> `OK` via combo fallback
- First interactive run needs the trust dialog (or `--allow-dangerously-skip-permissions`); headless works after

### Roo Code (VS Code)
- Extension `rooveterinaryinc.roo-cline` v3.54.0
- Import file `C:\Users\Asus\.omniroute\roo-settings.json` - profile `OmniRoute`, base URL `http://localhost:20128/v1`, model `free`, real key embedded, `contextWindow: 256000` (Roo schema requires contextWindow)
- Import path: Roo panel -> gear -> Providers -> Import Settings

## Storage / Diagnostics

| Path | Contents |
|------|----------|
| `C:\Users\Asus\.omniroute\` | `storage.sqlite` (+`-shm`/`-wal`), `.env` (STORAGE_ENCRYPTION_KEY), `roo-settings.json`, `cli-history.jsonl` |
| `storage.sqlite` table `call_logs` | timestamp, path, status, requested_model, provider, duration, error_summary, combo_name, ... - the FIRST stop for any routing/debug issue |
| better-sqlite3 access | `node <script.cjs>` requiring `C:\Users\Asus\AppData\Roaming\npm\node_modules\omniroute\node_modules\better-sqlite3` |
| Dashboard | `http://localhost:20128` |

Status interpretations: `499 Request aborted` = client timeout killed the request while waiting; `503 high demand` / `429 resource exhausted` / `504 fetch timeout` = upstream (Gemini) trouble - check the OTHER providers, not the client.

## Gotchas (summary - full detail in `brain/Gotchas.md`)

- **2026-10-30** - Gemini free tier has bad-day outages (429/503/504); diagnose via call_logs first, then reorder combo putting an alive provider first. Route Claude Code through the `free` combo, never a single model
- **2026-10-30** - Inject the OmniRoute key from `auth.json` via script; a Claude settings pointing at `https://openrouter.ai/api` with empty keys is wrong - base URL must be `http://localhost:20128`
- **2026-10-30** - curl.exe JSON body quoting breaks on Windows; write body to a temp file and `--data @file`
- **2026-10-30** - omniroute CLI loads .env from the package dir AND `C:\Users\Asus\.omniroute\.env`; package-dir values are wiped on npm update - keep custom env only in the user-dir file
- **2026-10-12** - Claude Code first-run trust dialog blocks headless; accept once or use `--allow-dangerously-skip-permissions`
- **2026-10-12** - OpenRouter `auto` can route to paid models - never use it; always `:free`-suffix
- **2026-10-12** - OpenCode TUI needs full restart to pick up plugin model changes
- **2026-10-10** - auth.json UTF-8 BOM silently zeroes all models - rewrite BOM-less (UTF8Encoding($false))
- **2026-10-10** - `omniroute setup-*` commands don't install `@opencode-ai/plugin` deps; npm install into the plugin dir manually

## Maintenance

After OmniRoute-related changes: append to `wiki/log.md`, then `python .scripts/update-graph-colors.py` + `python .scripts/generate-index.py`, commit + push. Correction-sweep model lists if the combo changes again.

## Links

- Debugging playbook: [[brain/Gotchas]] (OmniRoute section)
- Related tooling: [[repo-dev-toolbox-minors]]
- Domain hub: [[INDEX]]
