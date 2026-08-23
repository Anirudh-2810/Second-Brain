---
module: "stock-agent"
topic: "Stock Agent — How to Make It Better (Prioritized Roadmap)"
tags: [stock-agent, roadmap, improvement, engineering, priorities]
last_updated: "2026-08-21"
prerequisites: ["[[what-works-and-fails]]", "[[value-and-standalone]]"]
---

# Stock Agent — How to Make It Better

> Prioritized roadmap derived from the failure analysis. Each item: what to do, why, effort, and the file(s) touched.

---

## P0 — Fix the live-data gap (biggest credibility hit)

| # | Action | Why | Where |
|---|---|---|---|
| 1 | **Pin `websockets` to a version compatible with the Alpaca client**, or upgrade `alpaca-py` to one that supports current websockets | Unblocks real IEX quotes/trades on the existing Python 3.14 env | `backend/requirements*.txt`, `services/alpaca_ws.py` |
| 2 | **Verify WS path end-to-end** (Alpaca → Redis pub/sub → WS manager → browser) and remove the mock stub once pinned | Confirms the streaming pipeline actually works | `services/alpaca_ws.py`, `ws_manager.py` |
| 3 | **Replace mock chart data** with real WS/trades feed; show a clear "LIVE / DELAYED / DEMO" badge | Stops the flagship screen from misleading | `frontend/src/pages/PaperTrading.tsx` |

## P0 — Re-enable the scheduler (data stops going stale)

| # | Action | Why | Where |
|---|---|---|---|
| 4 | Turn scheduler on behind an env flag (e.g., `ENABLE_SCHEDULER`) | Daily ingest, fundamentals, features, equity snapshots, WS health checks resume | `main.py` |
| 5 | Add a **startup backfill** if DB is empty | Fresh deployments work without manual endpoint calls | `data_ingestion.py`, `main.py` lifespan |

## P1 — Make the ML model actually use its best features

| # | Action | Why | Where |
|---|---|---|---|
| 6 | **Populate the technical-indicator columns** in `ml_features_weekly` (real RSI/MACD/BB/ATR/ADX values) instead of `NULL::numeric` | Model currently trains on returns+fundamentals only | migration `002_point_in_time_features.py`, `feature_engine.py` |
| 7 | Add a **scheduled feature-refresh** that recomputes & refreshes the materialized view | Keeps the dataset current | `tasks/scheduler.py` |

## P1 — Persist the trading record

| # | Action | Why | Where |
|---|---|---|---|
| 8 | **Write orders/fills/positions to the DB** on every execution (tables already exist) | Audit trail, history, P&L analytics, reconciliation | `trading.py`, `models/__init__.py` |
| 9 | Add an **Alpaca fill/event listener** (or poll) to capture executions | Order history becomes real | `alpaca_rest.py` / scheduler job |

## P1 — Harden auth & security

| # | Action | Why | Where |
|---|---|---|---|
| 10 | **Move the API key out of the frontend bundle** — frontend talks to backend via a short-lived session/proxy; backend holds the secret | Stops the key being public | `frontend/services/api.ts`, `core/security.py` |
| 11 | Switch WS auth from `?api_key=` to a **header or short-lived token** | Keys stop leaking into logs | `websocket.py`, `ws_manager.py` |
| 12 | (Later) multi-user accounts + per-user keys | Enables SaaS direction | `models/__init__.py`, auth service |

## P1 — Fix mislabeled metrics (cheap credibility)

| # | Action | Why | Where |
|---|---|---|---|
| 13 | `daily_pl` → compute **today's realized+unrealized** from day-start equity, not `unrealized_pl` | Correct semantics | `alpaca_rest.py` |
| 14 | `pe_ratio` → **price / EPS** (or rename to `revenue_to_income`) | Current formula is net-margin, not P/E | `analysis.py` |
| 15 | Replace signal `confidence` with a real calibration (e.g., logistic regression or empirical hit-rate) or label it `score_strength` | Honest naming | `signal_engine.py` |

## P2 — Infrastructure & data hygiene

| # | Action | Why | Where |
|---|---|---|---|
| 16 | Add a **PostgreSQL service to docker-compose** (or document external DB clearly at startup) | One-command boot actually works | `docker-compose.yml` |
| 17 | De-duplicate `DEFAULT_UNIVERSE` (`AVGO` twice) | Cleaner ingest | `data_ingestion.py` |
| 18 | Fetch **full SEC filing sets** for XBRL parsing (not just primary doc) | Higher parse success | `sec_parser.py` |
| 19 | Consider **sourcing OHLCV from Alpaca** (real, structured) instead of yfinance | More reliable data | `yfinance_ingester.py` |
| 20 | Add a **feature-store table** that persists computed indicators on a schedule | Reuse, faster signals, better ML | new migration + scheduler job |

## P3 — Nice-to-have / stretch

| # | Action | Why | Where |
|---|---|---|---|
| 21 | Automated **walk-forward benchmark vs buy-and-hold** per universe | Turns claims into evidence | backtest service |
| 22 | **Equity curve dashboard** from account snapshots | Track paper performance over time | frontend + snapshots job |
| 23 | Add **tests** (pytest: guards, signal engine, sec_tags, backtest helpers) | Prevent regressions in a growing codebase | `backend/tests/` |
| 24 | Universe shared from backend (single source of truth) | Frontend drift disappears | `frontend/` |

---

## Suggested execution order (2–3 focused weeks)

**Week 1 (P0):** items 1–5 → live streaming works + data self-updates.
**Week 2 (P1):** items 6–12 → ML features, order history, security.
**Week 3 (P1–P2):** items 13–20 → metrics honesty + infra hygiene; start tests.
**Ongoing:** items 21–24 as stretch goals.

---

## Definition of "good enough to be a personal platform"

- [ ] Live quotes confirmed end-to-end (WS badge shows LIVE)
- [ ] Scheduler on; fresh deploy backfills automatically
- [ ] ML dataset includes technical indicators; walk-forward scores recorded
- [ ] Orders/fills persisted; daily P&L correct
- [ ] API key not exposed in frontend bundle
- [ ] `pe_ratio` and `daily_pl` correct or honestly named
- [ ] `docker compose up` boots the full stack including DB

## CROSS-REFERENCES

- [[overview]] · [[architecture]] · [[functions-and-features]] · [[what-works-and-fails]] · [[value-and-standalone]]