---
date: 2026-11-10
description: "ShopBrain platform spec — offline AI back-office for small shops (pharmacy wedge): StockOffline app + tscore forecasting lib + stock-agent patterns. Corrected repo roles, no unvalidated revenue numbers."
tags:
  - brain
  - agency-platform
  - shopbrain
confidence: high
provenance: "Rewritten 2026-11-10 (v2). v1 overstated Algorithm101/wine-shell roles and carried fabricated pricing/margin/savings numbers — corrected here per Write-Correctness Laws."
relations:
  relates_to: "01-Areas/Business/plans/shopbrain-agency-launch"
---

## For future agent

This is the platform SPEC for ShopBrain — what each repo actually contributes and what the product is. The execution roadmap with week-by-week Done-when gates lives in [[01-Areas/Business/plans/shopbrain-agency-launch]]. Read that plan for sequencing; read this note for architecture and rules. **v1 of this note (earlier 2026-11-10) overstated two repos and contained invented revenue numbers — if you see $2.5k/$199/85% margin/"20% stock reduction" anywhere in the vault, that is stale v1 text and must be corrected, not repeated.**

# ShopBrain — offline AI back-office for small shops

**One-liner:** the shop records sales and stock; ShopBrain forecasts demand, proposes a weekly reorder list under hard guards, and the owner approves with one click. Nothing is ordered automatically.

**Wedge (decided 2026-11-10): pharmacy.** Highest data discipline (batch/expiry), and expired stock is a direct, easily-pitched loss. Reorder is the product; bill-to-stock scanning is the data feeder and demo hook; expiry/dead-stock tracking is the pitch that gets the meeting.

## Repo roles (corrected — verified against the repos 2026-11-10)

| Repo | Role | What it actually is (verified) |
|------|------|-------------------------------|
| **`inventory-system` (StockOffline)** | **The app shops use** | Offline-first Tkinter GUI + CLI + optional JWT web tier, SQLite. `Product` + `InventoryTransaction` (purchase/sale/adjustment/return, timestamped) already give dated sales history. Has `reorder_level` (static threshold only). **Shipped as of 2026-11-16:** sales CSV import (contract v1, dated rows never touch counted stock), weekly Forecast screen with per-line approve/reject persisted per report date, `forecast` CLI shelling into tscore's `report.py`. |
| **`tscore`** (private repo) | **The forecasting lib** | **Exists and is current through Week 8 (built 2026-11-11 → 11-16).** Owns: sales/forecast data contract v1, seeded fake-sales generator, baselines + walk-forward backtest with naive gate (fake-data gate PASS: WAPE 28.10% vs 34.77% naive), reorder math + guards, weekly report, **W6 RNN experiment (verdict: DROP** — loses to MA(8) under all 8 seed×epoch configs), **W7 live-and-die agent sim + HTML replay dashboard**, **W8 one-command demo driver** (`scripts/demo.py`). 68 stdlib tests. Shared code the agency reuses across shops. |
| **`stock-agent`** | **Patterns source only — not a dependency** | FastAPI + React paper-trading platform. Borrow the *shape* of: `execution_guards.py` (guard/circuit-breaker style), `backtest_engine.py` (walk-forward structure), React dashboard layout, WebSocket event stream. **Its bugs are stock-trading bugs** (e.g. the kill-switch inversion) and are NOT a ShopBrain P0 — do not import its trading logic. |
| **`wine-shell`** | **Parked** | Swift/SwiftUI CrossOver-style Wine wrapper for **Apple Silicon Macs only** — runs Windows apps on Mac. Needs a Mac we don't have; most target shops run Windows. Revisit only as a Mac-installation route. Not a generic installer. |
| **`Algorithm101`** | **Parked** | A **music-trend RNN** app (backend/frontend/tests) — NOT a forecasting library. Inspected at code level 2026-11-13: **no trainable neural net** (backend = rule scores + EMA "hidden state"; `LocalRNN` = decorative wall-clock animation) — confirms this park decision. The Week-6 RNN experiment ran **inside tscore** (stdlib Elman RNN, see below), not here. |

Supporting assets: `stock-predictor` (forecast pipeline + walk-forward habits), `retrieval-agent` (business-knowledge pattern). ~~`neural-engine`~~ — **unreachable as of 2026-11-13** (source lives only on the old machine, not local/GitHub); the W6 substitute was a from-scratch stdlib Elman RNN written into tscore. If the old machine's `Neural net 2/` folder is ever copied over, use it as a cross-check — the DROP verdict is about data sufficiency, not the engine.

## Architecture (what gets built)

```
sales CSV / bill photo ──► StockOffline (records sales + stock, SQLite, local)
                                │
                                ▼
   tscore: baselines ──► walk-forward backtest ──► reorder math + guards
                                │                        │
                                ▼                        ▼
                     weekly report ◄──────── owner approves / rejects (Forecast screen)
                                │
                                ▼
              live-and-die forecaster population (dashboard, stock-agent patterns)
```

- **Data contracts (Week 1):** sales CSV = `item, date, quantity, price`. Forecast output = `item, predicted_demand, suggested_reorder, confidence`.
- **Guards (Week 3, all tested):** max order size · budget cap · never more than a set multiple of the last order. Every suggestion must pass, proven by tests.
- **Report (Week 4):** reorder list · running-out alerts · dead stock · short summary the owner can read unaided, one click.
- **Self-improvement (Week 7 — BUILT 2026-11-13, tscore `scripts/agents_sim.py`):** forecasters as agents with virtual wallets scored on avoided stockouts vs overstock; death at zero, mutated children funded from the parent; replay dashboard. Virtual money only. Lineage finding: lifespan improves founders→gen4 (~3.6×) then declines; descendant wallets worse (structural — children inherit 40 vs founders 100); shape verified on 3 seeds. "Best lineage feeds the weekly report" was NOT built — not required by the plan's Done-when.

## Standing gates (non-negotiable — from the owner's rules)

1. **Baseline gate:** if the baseline can't beat a naive "reorder what sold last week", stop and fix the data or approach. No AI gets added on top of a losing baseline.
2. **Data gate:** permission from every shop for every sample of their data; data stays local and out of git; never claim savings that weren't measured against what the shop actually did.
3. **Money gate:** no new projects started until a shop has paid. Pricing is decided by pilot answers, not by us — all figures are `(speculation)` until then.

## Status

**Build phase effectively complete (2026-11-16):** Weeks 1–4 + 6 + 7 + 8-agent-part shipped across `tscore` (68 tests) and `inventory-system` (forecast screen). Remaining: **W5 real pilot** (owner-blocked: pharmacy outreach) and **W8 owner part** (10 shops approached → their answers set the price). Schedule and week-by-week Done-when gates live in [[01-Areas/Business/plans/shopbrain-agency-launch]] (exam blackout first week of December 2026 gates the calendar).

## Cross-references

- [[01-Areas/Business/plans/shopbrain-agency-launch]] — execution plan (8-week spine)
- [[inventory-system]] — StockOffline deep review + roadmap
- [[stock-agent/overview]] · [[stock-agent/deep-review-report]] — pattern source and its known bugs
- [[neural-engine]] — parked/unreachable (old machine only; W6 substitute was tscore's stdlib Elman RNN) · [[stock-predictor]] — forecasting asset
- [[wine-shell-plan]] — parked repo's own plan
- [[North Star]] — serves "Freelancing start" + "Ship a working ShopBrain prototype"
- [[Key Decisions]] — 2026-08-27 concept born; 2026-11-10 roles corrected
