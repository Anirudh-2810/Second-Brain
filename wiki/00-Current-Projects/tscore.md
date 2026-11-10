---
module: "current-projects"
topic: "tscore — ShopBrain forecasting core (data contracts + fake data + baselines)"
tags: [builds, forecasting, shopbrain, data-contract, python, csv, quant, private-repo]
last_updated: "2026-11-11"
confidence: "high"
provenance: "Phase A week-1 build per [[shopbrain-agency-launch]] plan (agent-executed 2026-11-11)."
source: "E:\Brain\tscore"
description: "Private forecasting repo powering ShopBrain: sales + forecast data contract v1, zero-dep seeded fake-sales generator (weekly/pay-day/seasonal patterns), contract tests, real-format example CSV. Pairs with StockOffline's import-sales for end-to-end load verification."
---

# tscore — ShopBrain forecasting core

> **Repo:** https://github.com/Anirudh-2810/tscore (private) · `E:\Brain\tscore`
> **Stack:** Python 3 stdlib only (no deps) · seeded RNG · unittest
> **Role:** data contracts + synthetic data + (later) baselines & models for [[ShopBrain]]

## For future agent
This is the **forecasting brain of ShopBrain** — week-1 delivered the data contract, a fake-sales generator, and contract tests; models come later and only after the baseline gate in [[shopbrain-agency-launch]] passes. Sales history produced here loads into [[inventory-system]] via `import-sales` (stock-safe). Real shop data belongs in `data/real/` and is gitignored — never commit it. Private repo: links render only for the owner.

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

## Next (per plan)

1. Baseline v0 (`reorder = last week's sales`) + holdout on `examples/fake_sales.csv`
2. Seasonal-naive → EWMA → Holt-Winters ladder, each must beat the previous
3. Only after the shop gives real data: profile it, then model selection

## See also

[[shopbrain-agency-launch]] — the 8-week plan this serves · [[ShopBrain]] — platform spec · [[inventory-system]] — the app side (import-sales) · [[projects/index]] — portfolio map
