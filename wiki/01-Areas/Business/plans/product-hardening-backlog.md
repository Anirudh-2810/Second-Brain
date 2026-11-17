---
date: 2026-11-18
description: "Hardening + sellability backlog for tscore, inventory-system and roadtrip-pomodoro — 3 P0s found by code scan, security audit results, per-repo fix list, branch plan, and owner manual-check list. No timing estimates."
tags:
  - business
  - plans
  - shopbrain
  - portfolio
  - security
confidence: high
provenance: "Created 2026-11-18 from direct code scans of all three repos (git tracking state, imports, live health endpoint, secret patterns). Every claim below was verified against the code on that date."
relations:
  relates_to: "brain/ShopBrain"
  relates_to: "01-Areas/Business/plans/shopbrain-agency-launch"
---

## For future agent

This is the FIX LIST for the three sellable repos (tscore, inventory-system, roadtrip-pomodoro) after the 2026-11-18 copyright/visibility pass. Read it before suggesting "new features" — the P0s come first, and the security section separates **agent-verified** facts from **owner-must-check** items. Update or check off entries as they land; add nothing that contradicts a verified finding without re-scanning.

# Product Hardening & Sellability Backlog

Scope: make the three resume/sale repos (1) actually work for strangers, (2) security-auditable, (3) shippable to non-technical buyers. No timing estimates (plans law). Order below = priority order.

## P0 — broken right now

- [ ] **inventory-system: public repo is uninstallable.** `src/auth.py`, `src/payments.py`, `src/utils.py` are in `.gitignore` (section "Security files") but imported by `handlers.py`, `security.py`, `server.py`, `store.py`, `test_web.py`. A fresh clone (= any recruiter) hits `ModuleNotFoundError` on the web tier. **Verified 2026-11-18 the files contain NO hardcoded secrets** (all secrets via `os.getenv`, placeholder handled explicitly in `auth.py:17`) → remove the three lines from `.gitignore` and commit the files. This closes the carried owner decision on gitignore fate; evidence says commit.
- [ ] **inventory-system exe: Forecast dead on customer machines.** `forecast_service.find_tscore_dir()` = `TSCORE_DIR` env → else sibling checkout `<Brain>/tscore`. Neither exists on a shopkeeper PC → `FileNotFoundError` for the headline feature inside `StockOffline.exe`. Fix = ship design in §tscore below.
- [ ] **roadtrip-pomodoro: all email broken in production.** Live `GET /api/health` (checked 2026-11-18) returns `"email":"missing RESEND_API_KEY"` — signup verification, per-Pomodoro email, daily/weekly digest silently not sending. Fix is config-side: add `RESEND_API_KEY` in Vercel project env → redeploy → re-check health says `email: configured`. (Supabase ✅ `"configured"`.)

## Should tscore ship with inventory? — YES, vendored

Decision: **vendor tscore as a subpackage of inventory**, not a separate install.

- Target layout: `src/inventory_system/vendor/tscore/` (both repos are yours + proprietary → no license friction).
- Refactor seam: `forecast_service.py:45` currently shells out (`script = find_tscore_dir() / "scripts" / "report.py"`). Change to an in-process import (`from inventory_system.vendor.tscore import report`). This is the single change that makes the exe work — PyInstaller bundles imports, it cannot bundle a subprocess path.
- tscore keeps its own repo + tests as the development home; the vendor copy is synced by a pin (record the tscore commit hash in the vendor folder's README line).
- Keep `TSCORE_DIR` env as a dev override (already documented in the file header).
- PyInstaller: update `StockOffline.spec`/`build_exe.py` with the vendored package (note: `StockOffline.spec` is currently gitignored — after vendoring, commit the spec so builds are reproducible).

## tscore — from demo lib to sellable product

1. **Package it**: add `pyproject.toml` (name, version, license = proprietary, entry points `tscore-report` / `tscore-backtest`). Today there is no install story — scripts only.
2. **Real-data gate**: every accuracy number on record is FAKE data. The plan's W5 pilot (owner-blocked: pharmacy CSV) is the ONLY thing that turns "28.10% vs naive 34.77%" into a sellable claim. Never market synthetic numbers as performance.
3. **Pharmacy-fit models**: current roster = MA + seasonal naive (+ RNN dropped, verdict on record). Pharmacies sell *intermittent* items (many SKUs sell 0 units most days) — MA/seasonal-naive are the wrong tools there. Add **Croston / TSB (exponential smoothing for intermittent demand)** as the next baseline; it is cheap (stdlib), standard in inventory literature, and directly on-wedge. Gate it exactly like W6 was: must beat naive on the same walk-forward, else written DROP.
4. **Prediction intervals** — shopkeepers reason in ranges ("expect 40–70, don't order below 50"), not point forecasts. Even a naive bootstrap interval from backtest residuals is sellable UX.
5. **Cold start**: SKUs with < N weeks of history need an explicit documented policy (report as "new item — no forecast yet" rather than a confident wrong number).
6. **Scale test**: stdlib Python — measure runtime at 5k/10k SKUs × 104 weeks before demoing to a chain. Record the number, don't guess.
7. **Docs**: API page for agency reuse (`docs/api.md`), "add a new forecaster" recipe, data-contract v1 already exists ✅.

## inventory-system — from repo to product

1. P0s above (un-vendor decision + exe forecast) — first.
2. **Code-signing** the exe (SmartScreen warning already documented in README) — costs money, owner decision.
3. **Installer**: Inno Setup/NSIS wrapping the exe + Start-menu shortcut + desktop icon. Shopkeepers download-and-double-click; a raw `.exe` + README is developer UX.
4. **Backup/restore**: single SQLite file = one USB copy away from safe. Ship a one-click "backup now" (copy `inventory.db` to chosen folder with timestamp) + restore doc. #1 buyer fear is data loss; answer it in the product.
5. **Tests**: only 2 test files exist vs tscore's 7. Priority coverage: auth flows, web handlers (authz on every route), CSV import edge cases, forecast approve/reject persistence.
6. **CI** (all repos — see below).
7. **`.gitignore` cleanup**: tracked `marketing/dist/StockOffline.exe` (12 MB binary in git) while the spec file that rebuilds it is ignored — invert that: commit the spec, `git rm --cached` the exe, attach releases to GitHub Releases instead.
8. **Payments**: `verify_razorpay_signature` exists and looks correct ✅ — but whether payments are *live* (webhooks configured, keys issued) is owner knowledge; pricing numbers stay out of all docs until Week-8 shops answer (standing rule).

## roadtrip-pomodoro — from live app to interview-proof

1. P0 email env var (above).
2. **Tests = 0.** Add vitest for pure logic (timer math/drift, guest cache, trip-log reducer) + one Playwright smoke (signup → run 1-min trip → trip log row). Interviewers ask "how do you know it works" more than "what stack".
3. **CI**: GitHub Actions — `lint + tsc --noEmit + build + test` on push (README already shows a workflow slot pattern from wine-shell to copy).
4. **Security checks to run** (owner, browser-side): see §audit below — especially guest **claim** flow (can guest A claim guest B's trips? = IDOR test) and RLS with the anon key from the browser console.
5. Nice-to-have: Sentry/error monitoring, custom domain (note `roadtrip-pomodoro.vercel.app` 404s — the `-taupe` URL is canonical; README already fixed 2026-11-18).

## Security audit — what is VERIFIED vs what the owner must check

### Agent-verified 2026-11-18 (code-level, all three repos)
- No secrets committed anywhere — only `.env.example` tracked (all 3 repos) ✅
- No `.db` tracked in git ✅ (`*.db` gitignored; local `marketing/dist/inventory.db` is an untracked build leftover — delete)
- tscore = pure stdlib (no third-party imports) → zero dependency CVE surface ✅
- inventory secrets are env-driven with startup refusal of placeholders (`auth.py`) ✅
- Razorpay webhook signature verification implemented (`payments.py:16`) ✅
- inventory web tier: bearer auth + in-memory per-IP rate limiter + CORS header builder in one auditable file (`src/web/security.py`) ✅
- roadtrip: session-refresh middleware present; rate-limit code present (~25 references) ✅ — per-route coverage unverified
- No TODO/FIXME/HACK markers in any source of the three repos ✅

### Owner must check (agent cannot — needs live systems/browser)
- [ ] **Clean-clone test** (after P0 fix): fresh `git clone` → follow README exactly → GUI + web + forecast all start. This is exactly what a recruiter does.
- [ ] **Vercel**: add `RESEND_API_KEY`, confirm health flips to `email: configured`, then actually receive a signup verification email.
- [ ] **RLS**: from browser devtools with the anon key, attempt to read another user's rows — must be denied.
- [ ] **Guest claim IDOR**: log in as user A, keep guest session of user B, claim — verify B's trips can't be stolen.
- [ ] **Exe on a clean Windows VM** (no `E:\Brain`) — Forecast must work after the vendor fix.
- [ ] **Roadtrip auth rate limits**: hit login/signup 30× fast — confirm 429 (code exists; per-route wiring unverified).
- [ ] **Secrets hygiene**: confirm no real keys in Vercel/Supabase dashboards match anything in git history (`git log -p | findstr sk_live` style sweep).
- [ ] Inventory payments: are Razorpay keys/webhooks actually provisioned, or dormant? (dormant = fine, but don't demo checkout)

## Branch plan (parallelizable, no timing)

| Branch | Repo | Content |
|---|---|---|
| `fix/commit-src-files` | inventory-system | Un-gitignore + commit auth/payments/utils (P0-1) |
| `feat/vendor-tscore` | inventory-system (+tscore sync) | Vendor subpackage + in-process import (P0-2) |
| `build/packaging` | tscore | pyproject + entry points |
| `ci/gha` | all 4 public repos | One workflow: lint + tests (+build for roadtrip) |
| `test/smoke` | roadtrip-pomodoro | vitest scaffold + Playwright signup smoke |
| `feat/croston-baseline` | tscore | Intermittent-demand model, gated like W6 |
| `chore/exe-installer` | inventory-system | Spec committed, `git rm --cached` exe, installer script |

Owner-side (no branch): Vercel env var, code-signing purchase decision, pricing decision (Week-8 rule).

## Definition of done for this backlog

Each checkbox closes only with: code committed + pushed, tests green, and for anything browser/visual — the owner's manual check ticked above. P0s before any feature work.
