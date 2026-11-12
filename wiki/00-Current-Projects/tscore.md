---
module: "current-projects"
topic: "tscore — ShopBrain forecasting core (data contracts + fake data + baselines)"
tags: [builds, forecasting, shopbrain, data-contract, python, csv, quant, private-repo]
last_updated: "2026-11-13"
confidence: "high"
provenance: "Phase A week-1 build per [[shopbrain-agency-launch]] plan (agent-executed 2026-11-11); Weeks 2-4 (backtest/reorder/report) delivered 2026-11-13."
source: "E:\Brain\tscore"
description: "Private forecasting repo powering ShopBrain: sales + forecast data contract v1, seeded fake-sales generator, walk-forward backtest with naive gate, reorder guards, weekly report (report.txt + forecast.csv). 42 stdlib unittest green. Pairs with StockOffline import-sales + Forecast screen."
---

# tscore — ShopBrain forecasting core

> **Repo:** https://github.com/Anirudh-2810/tscore (private) · `E:\Brain\tscore`
> **Stack:** Python 3 stdlib only (no deps) · seeded RNG · unittest
> **Role:** data contracts + synthetic data + (later) baselines & models for [[ShopBrain]]

## For future agent
This is the **forecasting brain of ShopBrain** — week-1 delivered the data contract, fake-sales generator, and contract tests; Weeks 2–4 (2026-11-13) delivered the walk-forward backtest + naive gate, reorder logic with guards, and the owner-readable weekly report. The gate PASSED on fake data (`moving_average(k=8)` WAPE 28.10% vs naive 34.77%), so baseline work is unblocked; neural model work (Week 6) still requires the gate to hold. Sales history produced here loads into [[inventory-system]] via `import-sales` (stock-safe) and the app's Forecast button shells back into this repo's `report.py`. Real shop data belongs in `data/real/` and is gitignored — never commit it. Private repo: links render only for the owner.

## What shipped (Phase A, week 1 — 2026-11-11)

| Piece | Path | Notes |
|-------|------|-------|
| Data contract v1 | `docs/data-contract.md` | source of truth for both CSV formats |
| Fake sales generator | `scripts/generate_fake_sales.py` | zero-dep, `--seed`, Poisson demand + weekly/pay-day + seasonal (flu) patterns |
| Contract tests | `tests/test_contract.py` | 6/6 pass: schema, dates, qty/price bounds, round-trip |
| Example: real-format | `examples/real_format_sales.csv` | hand-written, 12 rows — used to prove strict import errors cleanly |
| Example: fake | `examples/fake_sales.csv` | 968 rows, 12 items, 13 weeks, seed=42 |

## Data contract v1 (summary — full text in repo)

**Sales CSV** (input): `item,date,quantity,price`
- ISO dates; `quantity >= 1`; `price >= 0`; UTF-8 or BOM; column order flexible; extra columns ignored
- `item` resolves in StockOffline: sku exact → barcode exact → name (case-insensitive)

**Forecast CSV** (output, later): `item,predicted_demand,suggested_reorder,confidence` with `confidence` in 0–1.

## Import semantics (the non-obvious part)

- Historical sale rows are **dated transactions**; `apply_stock=False` — counted stock is never re-mutated (prevents double-counting against live counts).
- Unknown items are **reported, not guessed**; created only with `--create-missing`.
- Missing contract columns = hard error, imports nothing.
- Verified end-to-end 2026-11-11: fake CSV → 968 rows, stock unchanged; real-format strict → 12 skipped with row-numbered problems; `--create-missing` → 6 items created; garbage file → exit 1.

## What shipped (Weeks 2–4 — 2026-11-13)

| Piece | Path | Notes |
|-------|------|-------|
| Walk-forward backtest | `scripts/backtest.py` | trains on past → predicts next week; dense weekly axis (zero-sale weeks kept); no-leakage test; gate = naive "reorder what sold last week"; verdict PASS / TIE / FAILED — tie does **not** pass (rule 1 needs a BEAT); exit 0 pass / 2 fail / 1 usage |
| Reorder + guards | `scripts/reorder.py` | `raw_need = ceil(forecast × lead × (1+safety)) − on_hand`; guards: `max_order_qty`, `max_multiple_of_last`, `budget_cap` (urgent-first, partial fill); duplicate items rejected |
| Weekly report | `scripts/report.py` | `report.txt` (ORDER / WANTED BUT NOT ORDERED / RUNNING OUT / DEAD STOCK / NOTES) + contract `forecast.csv`; confidence = 1−WAPE, 0.5 placeholder when no folds; gate line discloses PASSED/TIED/FAILED/not-evaluable |
| Tests | `tests/` | 42 green: contract, backtest (incl. dense-axis + no-leakage), reorder grid invariants, report contract |
| Example | `examples/stock_example.csv` | stock rows for trying the report without a shop DB |

**Gate result (fake data, 2026-11-13):** 14 weeks / 12 items / 72 folds — `moving_average(k=8)` WAPE **28.10%** vs naive gate **34.77%** → PASS (exit 0).

## Next (per plan)

1. Week 5: run on a friendly pharmacy (real data, local-only, out of git) — compare vs what the shop actually did
2. Only then: model ladder (EWMA → Holt-Winters), each must beat the previous AND the gate
3. Week 6: `neural-engine` RNN vs baseline — keep only if it clearly wins

## See also

[[shopbrain-agency-launch]] — the 8-week plan this serves · [[ShopBrain]] — platform spec · [[inventory-system]] — the app side (import-sales) · [[projects/index]] — portfolio map
