---
module: "stock-agent"
topic: "Stock Agent — Full-Depth Code Review & Analysis Report"
tags: [stock-agent, review, report, audit, strengths, weaknesses, actions]
last_updated: "2026-08-21"
prerequisites: ["[[overview]]", "[[architecture]]", "[[what-works-and-fails]]"]
---

# Stock Agent — Full-Depth Code Review & Analysis Report

> **Consolidated deep audit** of `C:\Users\Vijaykumar\stock-agent`, read line-by-line across backend, frontend, migrations, infra, Docker, env, requirements, and git hygiene. Every finding below is verified against the source (file:line references included). It covers **strengths, weaknesses (ranked), and a concrete action plan**.

---

## 1. Executive summary

| Dimension | Verdict | Score (1–10) |
|---|---|---|
| Architecture & layering | Clean, well-separated, easy to extend | 8.5 |
| Idea & feature coverage | Genuinely broad: execution + signals + backtest + ML + fundamentals | 8.5 |
| Engineering robustness | Optional-dependency fallbacks are thoughtful | 7 |
| **Correctness of critical logic** | **A few inverted/disabled paths undermine safety** | **4.5** |
| Data pipeline reliability | Scheduler off → data goes stale | 4 |
| ML validity | Walk-forward is right; but features are NULL / not fed | 4.5 |
| Security posture | Single shared key baked into frontend | 4 |
| Test coverage | **None** (no test files found) | 1 |
| Production readiness | Prototype-grade; demo-class in current env | 4.5 |
| **Overall** | **Excellent learning/portfolio project; not yet a dependable personal platform** | **6.5** |

**One-line verdict:** *A well-architected, feature-rich trading lab whose biggest problems are (1) inverted kill-switch logic, (2) a disabled scheduler and live-data path, (3) ML training on NULL/stale features, (4) zero tests, and (5) a real `.env` sitting unguarded one `git init` away from being committed.*

> **⚠ First action before anything else:** add a `.gitignore` (exclude `backend/.env`) before initializing/pushing this repo — see **F1** (§4).

---

## 2. Strengths (verified)

### 2.1 Clean, layered architecture
`core/` (config, db, redis, security) → `services/` (business logic) → `api/v1/` (HTTP) → `schemas/` + `models/`. Each concern has one home. This is genuinely production-shaped for a personal project.

### 2.2 Graceful degradation everywhere
Optional dependencies never crash the app:
- `pandas_ta` absent → manual indicator fallback (`feature_engine.py:16-21, 186-281`)
- `vectorbt` absent → clear `RuntimeError` instead of silent failure (`backtest_engine.py:1-7, 82`)
- `mlflow` absent → local joblib registry (`model_registry.py:1-7`, `xgboost_trainer.py:14-22`)
- `arelle` absent → SEC parsing degrades (`sec_parser.py:14-26`)
- Redis down → **MockRedis** fallback (`core/redis.py:214-240`)
- Alpaca WS unavailable → mock mode (`alpaca_ws.py:34-44`)

This is a strength AND a hazard (see 3.6).

### 2.3 A genuine point-in-time data model
`fundamentals_point_in_time` (migration `002_point_in_time_features.py:22-55`) with `knowledge_timestamp`, plus the `ml_features_weekly` materialized view — the *right idea* for leakage-free research.

### 2.4 Honest walk-forward validation
`WalkForwardValidator` (`xgboost_trainer.py:301-397`) implements rolling train/test with a **purge gap** (`gap=4`) and **expanding window** — no look-ahead. Best-fold selection + metrics aggregation is disciplined.

### 2.5 Model registry with promotion
`ModelRegistry` (`model_registry.py:21-138`) persists models to disk, tracks metadata/metrics, and supports `latest`/`production` symlink promotion — a clean MVP experiment tracker.

### 2.6 Circuit-breaker concept
5 guards (kill switch, rate limit, drawdown, position, sector) in one `check_pre_trade()` gate (`execution_guards.py:64-88`). Concept is right; implementation has bugs (see 3.1).

### 2.7 SEC tag mapping layer
`sec_tags.py` maps 19 semantic metrics → multiple US-GAAP tag variants with a coverage tracker — testable and extensible.

### 2.8 Robust frontend structure
`pages/` · `components/` · `hooks/` · `store/` (Zustand) · `services/api.ts` — clean React/TS discipline.

### 2.9 Per-symbol error isolation
`scan_universe` catches per-symbol exceptions and returns `HOLD + error` rather than killing the whole scan (`signal_engine.py:185-204`).

---

## 3. Weaknesses & bugs (ranked by severity)

### 🔴 CRITICAL

#### 3.1 The kill switch is INVERTED (safety bug)
`execution_guards.py:73-74`:
```python
if not await self.is_enabled("kill_switch"):
    return False, "Kill switch activated"
```
- `is_enabled("kill_switch") == True` (armed) → `not True` → **does NOT block** → trading proceeds.
- `is_enabled(...) == False` (disarmed) → `not False` → **blocks all trading** with "Kill switch activated".

**So activating the kill switch does nothing, and deactivating it halts trading.** Combined with the default `kill_switch: {"enabled": True}` (`execution_guards.py:14`), the default state is "armed yet trading allowed." Exactly backwards from the documented behavior (README: "Kill Switch | Enabled | Blocks all new orders").

**Fix:** `if await self.is_enabled("kill_switch"): return False, "Kill switch activated"` and flip the default to disabled.

#### 3.2 Scheduler is disabled → nothing updates
`main.py:51`: `# start_scheduler()  # Disabled for testing`.
Every automated job (daily OHLCV, SEC sync, feature refresh, equity snapshots, WS health, guard health) never runs. The `equity_snapshot_job` — the thing that feeds the drawdown guard's day-peak — is dead.

**Impact:** data goes stale, drawdown guard has no peak to compare, ML view never refreshes. Everything works "when called by hand."

#### 3.3 The ML materialized view has NULL technical indicators
Migration `002_point_in_time_features.py:95-99`:
```sql
NULL::numeric AS rsi_14, NULL::numeric AS macd_hist,
NULL::numeric AS bb_pct, NULL::numeric AS atr_14, NULL::numeric AS adx_14
```
`feature_engine` *computes* RSI/MACD/ATR/ADX/BB for signals, but the **view intentionally stores them as NULL** → `add_derived_features` produces `(NaN > 70)` flags = all zero (`ml_features.py:130-140`). **The ML model trains only on returns + momentum, never seeing the technical indicators the signals engine uses.**

**Fix:** either persist real indicator columns in a features table and join, or compute indicators inside the view SQL.

#### 3.4 Fundamentals are never fed into ML training
`MLTrainingPipeline.run_training` (`ml_pipeline.py:50-52`) calls:
```python
X, y_reg, y_clf = ml_feature_engine.create_ml_dataset(features_df, target_horizon=...)
```
…without `fundamentals_df`. `load_fundamentals_latest()` exists (`ml_features.py:47-74`) but is **never called in the training path**. The entire PIT-fundamentals infrastructure is unused by ML.

#### 3.5 Cross-symbol feature leakage via `ffill`
`ml_features.py:113`: `X = df[feature_cols].fillna(method='ffill').fillna(0)`
The frame is ordered by `symbol, as_of_date`. At each symbol boundary, the first NaN row (e.g., `ret_52w` for a symbol's first 52 weeks) is filled with the **previous symbol's value** → leakage between tickers.

**Fix:** group by symbol before ffill (`df.groupby('symbol').ffill()`).

### 🟠 HIGH

#### 3.6 MockRedis silently substitutes in production
`core/redis.py:214-240` falls back to an **in-memory mock** if Redis is unreachable. Guards, rate limits, drawdown peaks, and position sizes live in this mock. With multiple backend replicas (Railway), each instance gets its **own divergent mock** → circuit breakers become inconsistent. A production outage is hidden, not surfaced.

**Fix:** mock only when `ENVIRONMENT != "production"`; fail loudly otherwise.

#### 3.7 Guard state is stale / divergent from Alpaca
- `update_position` tracks Redis `position:{symbol}` only for orders placed *through the app* (`trading.py:56-59`). Positions closed via `/positions/{symbol}/close` or `/positions/close-all` **never decrement the Redis counter** → position-limit guard over-counts.
- Initial Alpaca positions are never synced into Redis at startup → the guard starts from zero.
- `update_position` runs as a background task even if Alpaca rejected the order → phantom position.
- **Sector limit is dead code in the trading path**: `place_order` calls `check_pre_trade` with no `sector` (`trading.py:43-49`), and `check_pre_trade` only runs `_check_sector_limit` `if sector:` (`execution_guards.py:85`).

#### 3.8 No live data in the actual dev environment
`alpaca_ws.py:4-9` disables Alpaca WS on **Python 3.14** (websockets lib incompatibility). The project venv is 3.14 → real-time quotes/trades are **mock**. The Paper Trading chart is client-generated random candles (`PaperTrading.tsx:43-64`), clearly labeled "for demo" — the flagship screen is a simulation.

#### 3.9 Zero tests
No `test_*.py` anywhere in `backend/` (glob verified). For a codebase claiming "production-ready," there is no test suite for guards, signals, ML features, or SEC parsing. The inverted kill switch would have been caught by a one-line unit test.

### 🟡 MEDIUM

#### 3.10 Mislabeled metrics
- `daily_pl` is actually `unrealized_pl` (`alpaca_rest.py:36-37`) — total unrealized P&L, not today's.
- `pe_ratio` is `revenue / net_income` (`analysis.py:205`) — that's **1/net-margin**, not price-to-earnings. Misleading valuation.
- Signal `confidence` = `clip(|score|, 0.3, 1.0)` (`signal_engine.py:165-167`) — a re-scaled score, not calibrated probability. Even a flat `HOLD` gets confidence 0.3.

#### 3.11 MLflow path has a NameError
`xgboost_trainer.py:253` references `model_path` **before** it is assigned at line 255, inside `if log_to_mlflow and MLFLOW_AVAILABLE:`. If MLflow is installed, training crashes with `NameError`.

#### 3.12 Infrastructure gaps
- **No PostgreSQL service in `docker-compose.yml`** (only backend, frontend, redis). `docker compose up` produces an app with no DB → guaranteed failure unless `DATABASE_URL` already points somewhere (README documents external Neon — but the "Quick Start" implies it works out of the box).
- `NullPool` on the async engine (`core/database.py:13`) — no connection reuse; wasteful for anything beyond toy traffic.
- `init_db()` runs `create_all` (`core/database.py:33-36`), but the **materialized view is only created by alembic** → a fresh DB without manual `alembic upgrade head` has no `ml_features_weekly`, so ML features fail.
- `DEFAULT_UNIVERSE` contains **`AVGO` twice** (`data_ingestion.py:19,22`).
- Global `logging.DEBUG` in `main.py:16-20` — noisy in production.
- `get_orders` default `limit=100`, `nested=True` — fine, but no pagination on the API.

#### 3.13 Security weaknesses
- Single shared `X-API-Key` verified by `==` comparison (`websocket.py:20` uses `!=` against settings; `core/security.py` header check). No constant-time compare, no per-user keys, no expiry.
- WS auth via **`?api_key=` query param** (`websocket.py:16-18`) → key leaks into logs/URL history.
- Frontend ships the key via `VITE_API_KEY` → **the key is in the public JS bundle**. Anyone who can open the site can read it.
- CORS locked to `localhost:3000` only (`main.py:76-82`) — fine for dev, blocks real deployments unless edited.
- Read endpoints (analysis, signals, data health) all require the same shared key — no public/personal tier.

#### 3.14 SEC parser robustness
`sec_parser.py:132-140` downloads **only the primary XBRL document**, not the full submission set (schema + linkbases). Arelle often needs the whole filing → many filings parse partially or fail. No retry/backoff for SEC rate limits (60 symbols × filings can hit EDGAR's 10 req/s cap).

#### 3.15 Execution-path correctness edges
- `place_order` fetches a quote, mid-prices it, checks guards, then places — but if the quote is stale/missing for the stop/limit path, guards use a best-effort price.
- `get_account()` calls `get_all_positions()` **every time** just to count positions (`alpaca_rest.py:38`) — wasteful.
- `/signals/{symbol}` returns the full OHLCV history payload even though only the last rows are shown (`signals.py:52-97`).
- `signal_engine` requires ≥30 rows (`signal_engine.py:117`), `feature_engine` requires ≥200 rows (`feature_engine.py:54`) → symbols with thin history silently become permanent `HOLD`/empty.

#### 3.16 Frontend deep-dive (full read complete — `frontend/src`, every page/component/hook/store/service)

**F-A — CRITICAL: Kill switch is inverted in BOTH layers (UI vs engine contradiction).**
- Backend blocks orders when OFF (`execution_guards.py:73-74`).
- Frontend `OrderEntry.tsx:21-22`: `killSwitch = guards.kill_switch?.is_active; canTrade = !killSwitch` → UI blocks when ON, allows when OFF.
- Result: **when OFF, the form says "Normal trading enabled" and submits, but the engine 403s every order** ("Kill switch activated"); **when ON, the UI blocks orders that the engine would actually allow.** `KillSwitch.tsx:87-89` even prints "Kill switch ACTIVE - All new orders blocked" for the state that lets orders through. The flagship safety control is 100% contradictory with the engine. (Frontend corollary of bug #1.)

**F-B — HIGH: BacktestLab sends comma-joined symbols to a `List[str]` query param.**
`BacktestLab.tsx:29-35` sends `symbols: 'AAPL,MSFT'`; the backend `/backtest/run` expects `symbols: List[str] = Query(...)` (`backtest.py:31`) — every *other* router takes `str` + comma-split (`analysis.py:30`, `signals.py:28`). A single comma string is parsed as one element `["AAPL,MSFT"]`, and `WHERE symbol = ANY(:symbols)` (`backtest.py:54`) matches nothing → **the default "Run Backtest" yields an empty/failed result.** The ML path is worse: strategy `ml_predictions` requires `model_name` (`backtest.py:78-80`) but `BacktestLab` never sends one → picking ML strategy always 400s. Same `List[str]` mismatch affects `predict` (`api.ts:96-99`).

**F-C — HIGH: Universe drift — 7 hardcoded lists, 3 distinct sets.**
- 9 symbols (no JPM): `Overview.tsx:7`, `DataHealth.tsx:6`
- 10 symbols (incl. JPM): `Signals.tsx:6`, `Analysis.tsx:6`, `OrderEntry.tsx:6`, `QuoteTiles.tsx:18`, `PaperTrading.tsx:106`
- Backend canonical (10, incl. JPM): `signals.py:17`, `analysis.py:20`, `alpaca_ws.py:159`, `websocket.py:72`
- Ingestion universe: a *different* set with `AVGO` twice (`data_ingestion.py:18-22`)
So Overview/Data Health silently drop JPM while trading pages include it, and `QuoteTiles` hardcodes symbols that may not exist in the DB → `--.--` placeholder tiles. No single source of truth (this is the frontend half of D4, now with exact line refs).

**F-D — MED: Guard toggles are fire-and-forget and mis-default.**
`KillSwitch.tsx:43` `guard?.is_active ?? true` renders missing guards as **ACTIVE** before load. Per-guard checkboxes (`KillSwitch.tsx:53`) call `guardsApi.update(...)` with **no error handling and no store refresh** → the checkbox can silently disagree with backend state. Contrast: the kill-switch toggle *does* refresh guards (`KillSwitch.tsx:16-20`).

**F-E — MED: PositionsTable Close is unguarded.**
`PositionsTable.tsx:106-114` — `await positionsApi.close(pos.symbol)` with no try/catch (unhandled rejection), no confirmation, no disabled/loading state. One mis-click instantly closes a position.

**F-F — MED: Chart `height` prop is ignored.**
`Chart.tsx:10` accepts `height` (PaperTrading passes `height={400}` at `PaperTrading.tsx:111`), but `useChart.ts:24,78` hardcodes `height: 400` → the prop can never take effect.

**F-G — LOW: Dead / misleading WS code.**
- `useWebSocket.ts:59-62` `useReconnectingWebSocket` returns a non-reactive snapshot of `wsService.isConnected()` and reconnects nothing; no page uses it.
- `websocket.ts:120-126` exports a `useWebSocket` hook that nothing imports (dead code).
- `websocket.ts:59-61` `onerror` rejects the `connect()` promise only when `reconnectAttempts === 0`; on later reconnect failures the awaiting caller hangs.
- `tradingStore.ts:20,47-49` `updateGuard` is defined but never called (KillSwitch talks to the API directly) — dead store action.

**F-H — LOW: WS default URL is `ws://localhost:8000` (`websocket.ts:18`)** — mixed-content failure if the frontend is ever served over HTTPS; dev default baked into prod build.

**F-I — LOW: Formatting/UI nits.** `BacktestLab.tsx:95` renders max drawdown red (`tone="negative"`) even when positive; percent-format helpers are duplicated per page (`BacktestLab.tsx:45`, `Signals.tsx:145`, `PositionsTable.tsx:14-17`) → drift risk; `DataHealth.tsx:29-33` issues 9 sequential awaited HTTP calls instead of `Promise.all` (slow page).

**F-J — LOW: Half the backtest API surface is unused by the UI.** Only `backtestApi.run` and `backtestApi.models` are consumed; `sweep/train/predict/walkForward/retrainWeekly/promote/getModel` (`api.ts:88-104`) are dead code — some with contract bugs (e.g., `sweep` posts `params.grid` as the body while the backend reads query params).

#### 3.17 Repo hygiene, infra & environment audit (full pull — Docker, git, env, migrations, requirements)

**G-A — CRITICAL: No `.gitignore`, no `.dockerignore`, and a real `backend/.env` sits in the tree.**
The README's own deployment path is "connect GitHub repo to Railway" (`README.md:130-133`), but there is no `.gitignore` anywhere in the repo. A single `git init && git add .` would commit `backend/.env` containing `API_SECRET_KEY`, `ALPACA_SECRET_KEY`, and `DATABASE_URL` (Neon creds). Independently, both Dockerfiles do a blind `COPY . .` (`backend/Dockerfile:16`, `frontend/Dockerfile:10`) with no `.dockerignore` → the backend image bakes in `backend/.env` (secrets), a Windows `.venv` (3.14, broken on the 3.11 image), and the frontend image bakes in `node_modules` + `dist`. Anyone who can pull the image can read the keys.

**G-B — HIGH: `execution_guards.config` type contradicts between model and migration.**
`models/__init__.py:106` declares `config = Column(Numeric, nullable=True)` (comment even says "JSON stored as text"), while the migration creates it as `sa.Text` (`001_initial.py:122`). `init_db()`'s `create_all` (`database.py:33-36`) and `alembic upgrade head` therefore produce **different schemas** for the same table. On a `create_all`-first DB, inserting the JSON guard configs (`001_initial.py:164-167`) into a `Numeric` column fails/garbs on Postgres. The whole `execution_guards` table is near-vestigial (guards actually live in Redis), so this is a latent footgun rather than an active failure.

**G-C — HIGH: The packages that power Phases 2–4 are commented OUT of `requirements.txt`.**
`arelle`, `pandas-ta`, `vectorbt`, `mlflow`, `prophet` are all disabled for Python 3.14 (`requirements.txt:16-17,25,29,33`). Because the Dockerfile also installs `requirements.txt` (`backend/Dockerfile:14`, image `python:3.11-slim`), **SEC XBRL parsing, vectorbt backtesting, pandas-ta indicators, and MLflow tracking are degraded even in the "production" container** — the graceful-degradation code in §2.2 isn't optional, it's the only path. `requirements-phase2.txt` pins installable older versions (`arelle==1.18.0`, `pandas-ta==0.3.14b0`) but nothing in the repo references it (no Dockerfile, no README). The local venv is a **mismatched manual mix** (e.g., `vectorbt` present in `.venv` despite the numpy-2 incompatibility note) — so `requirements.txt` does not reflect any actually-working environment.

**G-D — MED: Python 3.14 SQLAlchemy monkey-patches exist in 4 copies but are wired into zero app entrypoints.**
`sqlalchemy_314_patch.py`, `sqlalchemy_patch.py`, an import-hook wrapper `run_alembic.py`, and an inline patch in `alembic/env.py:1-21` all exist to work around the `FastIntFlag`/`__firstlineno__` break. Yet `app/main.py` imports `app.core.database` → SQLAlchemy directly, with no patch applied. `patch_langhelpers.py` is worse: it hardcodes an absolute path and **rewrites a file inside `backend/.venv`** (`patch_langhelpers.py:3-18`) — machine-specific and non-reproducible. The app only boots because the broken code path isn't hit at import time, and plain `alembic` requires the wrapper. This environment is held together by one-off hacks.

**G-E — MED: README is stale and self-contradictory.**
- Marks Phase 2/3/4 as "Planned" (`README.md:68-80`) though all of it is implemented.
- References `docker-compose.prod.yml` (`README.md:137`) which does **not exist** in the repo.
- "X-API-Key authentication on all *mutation* endpoints" (`README.md:63,142`) is wrong — read endpoints also require it (`websocket.py:71`, analysis/signals/data_health routers).
- Kill Switch documented "Blocks all new orders" (`README.md:121`) — contradicts the inverted implementation (§3.1).
- Calls the project "production-ready" (`README.md:3`).

**G-F — MED: The app has two divergent runtimes.** Local dev = Python 3.14 (Alpaca WS off, migrations patched, pandas-ta/vectorbt/MLflow unreliable); Docker = Python 3.11 but still without the commented-out packages and with no DB service (`docker-compose.yml` has only backend/frontend/redis — confirmed, no Postgres). "It works on my machine" is doing heavy lifting.

**G-H — LOW: Dead code & unclaimed deps.**
- `CorporateActionAdjuster` / `corporate_action_adjuster` (`yfinance_ingester.py:266-314`) are never called → dead; if ever wired, it would double-adjust since `fetch_ohlcv` already uses `auto_adjust=True` (`yfinance_ingester.py:55,88`).
- `ConnectionManager.broadcast` (`ws_manager.py:51-57`) is never used (the router only uses `send_personal`).
- `pytest==8.2.1` + `pytest-asyncio` are in `requirements.txt:14-15` but zero tests exist (framework shipped, none written).
- Frontend `date-fns` dependency (`package.json:18`) is imported nowhere.
- The Vite dev proxy (`vite.config.ts:9-18`) is dead — `api.ts`/`websocket.ts` hit `localhost:8000` directly via env vars.
- Frontend `Dockerfile` sets `NODE_ENV=development` and runs `npm run dev` (`frontend/Dockerfile:5,14`) — the "production" image actually runs a dev server.

---

## 4. What should be done (prioritized action plan)

### Phase A — Safety & correctness (1–2 days) — *do this first*
| # | Action | Why | File(s) |
|---|---|---|---|
| A1 | **Fix kill-switch inversion** (flip check + default to disabled; align `OrderEntry.tsx:21-22` so UI matches engine) | Critical safety bug, both layers | `execution_guards.py:73-74,14`, `OrderEntry.tsx:21-22` |
| A2 | **Group-by-symbol before `ffill`** in ML dataset | Kills cross-ticker leakage | `ml_features.py:113` |
| A3 | **Fix MLflow `model_path` NameError** (move assignment before log) | Training crashes with MLflow | `xgboost_trainer.py:247-258` |
| A4 | **Add a smoke test suite** (pytest): guard logic, signal scoring, ML dataset leakage, sec_tags mapping | Catches regressions like A1 | new `backend/tests/` |
| A5 | Re-enable scheduler behind `ENABLE_SCHEDULER` env flag | Data + guards + ML stay fresh | `main.py:50-52` |
| A6 | **Fix BacktestLab symbols contract** (send repeated `symbols[]` params — or switch `backtest.py` to `str`+comma-split like other routers) and send `model_name` for `ml_predictions` | Backtest page currently yields empty results | `BacktestLab.tsx:29-35`, `backtest.py:31,78-80` |

### Phase B — Real data path (2–3 days)
| # | Action | Why | File(s) |
|---|---|---|---|
| B1 | Fix Alpaca WS on Python 3.14 (pin `websockets<13` or upgrade `alpaca-py`) | Unblocks real live quotes/trades | `alpaca_ws.py:1-21`, requirements |
| B2 | Replace mock chart with live WS feed; add LIVE/DEMO badge | Flagship screen becomes real | `PaperTrading.tsx`, `useWebSocket` |
| B3 | **Feed technical indicators into the ML view** (real columns, not NULL) | Model finally sees RSI/MACD/ATR/ADX | migration `002`, `feature_engine.py` |
| B4 | **Merge fundamentals into `create_ml_dataset`** in the training path | Uses the PIT fundamentals infra that exists | `ml_pipeline.py:50-52`, `ml_features.py` |

### Phase C — Guard & data integrity (2–3 days)
| # | Action | Why | File(s) |
|---|---|---|---|
| C1 | Sync Alpaca positions → Redis at startup; decrement on close/close-all; only update on `filled` orders | Position/sector limits become truthful | `execution_guards.py`, `trading.py` |
| C2 | Pass `sector` into `check_pre_trade` (lookup from Ticker table) or remove sector limit | Sector guard is currently dead code | `trading.py:43-49` |
| C3 | MockRedis only outside production; fail loudly in prod | No hidden divergence across replicas | `core/redis.py:214-240` |
| C4 | Add Postgres service to docker-compose (or a `db` profile) | One-command boot actually works | `docker-compose.yml` |
| C5 | Run alembic migrations on startup (or document loudly) | Fresh DBs get the materialized view | `main.py`, README |

### Phase D — Metrics honesty & polish (1 day)
| # | Action | Why | File(s) |
|---|---|---|---|
| D1 | `daily_pl` → compute from day-start equity snapshot (or rename to `unrealized_pl`) | Correct semantics | `alpaca_rest.py:36-37` |
| D2 | `pe_ratio` → price/EPS, or rename to `revenue_to_income` | Not a real P/E | `analysis.py:205` |
| D3 | Replace `confidence` with calibrated probability or rename `score_strength` | Honest UX | `signal_engine.py:165-167` |
| D4 | De-dupe `AVGO`; share universe from backend | Clean data + consistent UI | `data_ingestion.py:19-25`, frontend |

### Phase E — Security (1–2 days)
| # | Action | Why | File(s) |
|---|---|---|--|
| E1 | Move API key out of the JS bundle: frontend → backend session/proxy | Key stops being public | `frontend/services/api.ts`, `core/security.py` |
| E2 | WS auth via header or short-lived token, not `?api_key=` | Keys stop leaking into logs | `websocket.py:16-18` |
| E3 | Constant-time compare (`hmac.compare_digest`) | Defensive hygiene | `core/security.py` |

### Phase F — Repo hygiene & env determinism (1 day)
| # | Action | Why | File(s) |
|---|---|---|---|
| F1 | **Add `.gitignore` + `.dockerignore` now; confirm `backend/.env` is excluded before any `git init`/push** | One commit away from leaking Alpaca + Neon + API secrets | repo root, both `Dockerfile`s |
| F2 | Reconcile `execution_guards.config` type (use `Text` in model, or drop the vestigial table) | `create_all` vs alembic diverge | `models/__init__.py:106`, `001_initial.py:122` |
| F3 | Make the environment deterministic: pin one Python (3.11 in prod), un-comment Phase 2–4 packages in `requirements.txt`, or commit to `requirements-phase2.txt` as the 3.14 set | Docker ≠ dev; features silently degrade | `requirements.txt`, `backend/Dockerfile` |
| F4 | Wire the SQLAlchemy 3.14 patch into a single import site (app entrypoint) or upgrade SQLAlchemy; delete `patch_langhelpers.py` | Environment held together by hacks | `app/main.py`, `run_alembic.py`, `patch_langhelpers.py` |
| F5 | Fix README (phases done, real compose files, auth claims, kill-switch doc) | Doc contradicts code | `README.md` |

---

## 4b. Master TODO checklist (track progress here)

> Ticks update in Obsidian (`- [x]`). One row per fix from §4, grouped by phase.

### Phase A — Safety & correctness *(do this first)*
- [ ] A1 — Fix kill-switch inversion (flip check + default to disabled; align UI `OrderEntry.tsx:21-22`) — `execution_guards.py:73-74,14`
- [ ] A2 — Group-by-symbol before `ffill` in ML dataset — `ml_features.py:113`
- [ ] A3 — Fix MLflow `model_path` NameError — `xgboost_trainer.py:247-258`
- [ ] A4 — Add pytest smoke suite (guards, signals, ML leakage, sec_tags) — `backend/tests/`
- [ ] A5 — Re-enable scheduler behind `ENABLE_SCHEDULER` flag — `main.py:50-52`
- [ ] A6 — Fix BacktestLab symbols contract + `model_name` for ML strategy — `BacktestLab.tsx:29-35`, `backtest.py:31,78-80`

### Phase B — Real data path
- [ ] B1 — Fix Alpaca WS on Python 3.14 (pin `websockets<13` / upgrade `alpaca-py`) — `alpaca_ws.py`
- [ ] B2 — Live WS chart + LIVE/DEMO badge — `PaperTrading.tsx`, `useWebSocket`
- [ ] B3 — Feed real technical indicators into ML view — migration `002`, `feature_engine.py`
- [ ] B4 — Merge fundamentals into `create_ml_dataset` in training — `ml_pipeline.py`, `ml_features.py`

### Phase C — Guard & data integrity
- [ ] C1 — Sync Alpaca positions → Redis; decrement on close/close-all; update only on filled — `execution_guards.py`, `trading.py`
- [ ] C2 — Pass `sector` into `check_pre_trade` or remove sector guard — `trading.py:43-49`
- [ ] C3 — MockRedis only outside production; fail loudly in prod — `core/redis.py:214-240`
- [ ] C4 — Add Postgres service to docker-compose — `docker-compose.yml`
- [ ] C5 — Run alembic migrations on startup — `main.py`, README

### Phase D — Metrics honesty & polish
- [ ] D1 — `daily_pl` → day-start equity or rename to `unrealized_pl` — `alpaca_rest.py:36-37`
- [ ] D2 — `pe_ratio` → price/EPS or rename — `analysis.py:205`
- [ ] D3 — Replace `confidence` with calibrated probability or rename — `signal_engine.py:165-167`
- [ ] D4 — De-dupe `AVGO`; share universe from backend — `data_ingestion.py`, frontend

### Phase E — Security
- [ ] E1 — Move API key out of JS bundle (session/proxy) — `frontend/services/api.ts`, `core/security.py`
- [ ] E2 — WS auth via header / short-lived token — `websocket.py:16-18`
- [ ] E3 — Constant-time compare (`hmac.compare_digest`) — `core/security.py`

### Phase F — Repo hygiene & env determinism
- [ ] F1 — Add `.gitignore` + `.dockerignore`; exclude `backend/.env` (before any `git init`) — repo root, Dockerfiles
- [ ] F2 — Reconcile `execution_guards.config` type (Text or drop table) — `models/__init__.py:106`, `001_initial.py:122`
- [ ] F3 — Pin one Python; un-comment Phase 2–4 packages or use `requirements-phase2.txt` — `requirements.txt`, `backend/Dockerfile`
- [ ] F4 — Wire SQLAlchemy 3.14 patch into app entrypoint (or upgrade); delete `patch_langhelpers.py` — `app/main.py`, `patch_langhelpers.py`
- [ ] F5 — Fix README (phases done, compose files, auth + kill-switch docs) — `README.md`

### Definition of "personal platform ready"
- [ ] Kill switch verified blocking when ON, allowing when OFF (unit test green) **and** UI shows the same state as the engine (`OrderEntry.tsx` matches `execution_guards.py`)
- [ ] Scheduler running; data + ML view refresh automatically
- [ ] ML dataset contains real technical indicators + fundamentals, no cross-symbol leakage
- [ ] `docker compose up` boots full stack incl. DB + migrations
- [ ] No API key in the public frontend bundle
- [ ] Backtest Lab returns real trades for the default config (A6 green)
- [ ] Universe comes from a single backend source (D4), no page-level lists
- [ ] No secrets in git history / Docker images (F1 green)

---

## 5. Verified bug catalog (quick reference)

| # | Severity | Finding | Location |
|---|---|---|---|
| 1 | CRITICAL | Kill switch blocks when OFF, allows when ON | `execution_guards.py:73-74` |
| 2 | CRITICAL | Scheduler never started | `main.py:51` |
| 3 | HIGH | ML view stores indicators as NULL | `002_point_in_time_features.py:95-99` |
| 4 | HIGH | Fundamentals never merged in training | `ml_pipeline.py:50-52` |
| 5 | HIGH | Cross-symbol ffill leakage | `ml_features.py:113` |
| 6 | HIGH | MockRedis masks prod Redis outages | `core/redis.py:214-240` |
| 7 | HIGH | Guard position state diverges from Alpaca; sector limit dead | `execution_guards.py`, `trading.py` |
| 8 | HIGH | No live data on Python 3.14; demo chart | `alpaca_ws.py:4-9`, `PaperTrading.tsx:43-64` |
| 9 | HIGH | Zero tests | repo-wide |
| 10 | MED | `daily_pl` = unrealized P&L | `alpaca_rest.py:36-37` |
| 11 | MED | `pe_ratio` = revenue/net_income | `analysis.py:205` |
| 12 | MED | MLflow NameError (`model_path`) | `xgboost_trainer.py:253` |
| 13 | MED | No Postgres in compose; view only via alembic | `docker-compose.yml`, `database.py` |
| 14 | MED | `AVGO` duplicated in universe | `data_ingestion.py:19,22` |
| 15 | MED | Shared key in JS bundle; WS key in query string | `frontend`, `websocket.py` |
| 16 | MED | SEC parses single document, no rate-limit backoff | `sec_parser.py:132-140` |
| 17 | LOW | `confidence` is a rescaled score, not probability | `signal_engine.py:165-167` |
| 18 | LOW | DEBUG logging globally; wasteful position count call | `main.py:16`, `alpaca_rest.py:38` |
| 19 | CRITICAL | Kill-switch UI contradicts engine (UI blocks when ON, engine allows; UI allows when OFF, engine blocks) | `OrderEntry.tsx:21-22`, `execution_guards.py:73-74` |
| 20 | HIGH | BacktestLab comma-string symbols vs `List[str]` param; `ml_predictions` missing `model_name` | `BacktestLab.tsx:30`, `backtest.py:31,78-80` |
| 21 | HIGH | Universe drift — 7 hardcoded lists, 3 distinct sets | `Overview.tsx:7`, `Signals.tsx:6`, `DataHealth.tsx:6`, `OrderEntry.tsx:6`, `QuoteTiles.tsx:18`, `PaperTrading.tsx:106` |
| 22 | MED | Guard toggles fire-and-forget; missing guards render ACTIVE | `KillSwitch.tsx:43,53` |
| 23 | MED | PositionsTable Close unguarded (no confirm/error handling) | `PositionsTable.tsx:106-114` |
| 24 | LOW | Chart `height` prop ignored; dead WS code | `useChart.ts:24,78`, `useWebSocket.ts:59-62`, `websocket.ts:120-126` |
| 25 | CRITICAL | No `.gitignore`/`.dockerignore`; real `backend/.env` (API + Alpaca + Neon secrets) would be committed & baked into images | repo root, `backend/Dockerfile:16`, `frontend/Dockerfile:10` |
| 26 | HIGH | `execution_guards.config` Numeric (model) vs Text (migration) mismatch | `models/__init__.py:106`, `001_initial.py:122` |
| 27 | HIGH | Phase 2–4 packages commented out of requirements; degraded even in Docker | `requirements.txt:16-17,25,29,33` |
| 28 | MED | Py3.14 SQLAlchemy patches not wired into app entrypoints; `.venv` rewrite script | `sqlalchemy_314_patch.py`, `run_alembic.py`, `patch_langhelpers.py:3-18` |
| 29 | MED | README stale: Phases "Planned", `docker-compose.prod.yml` missing, auth claim wrong | `README.md:63,68-80,137` |
| 30 | LOW | Dead code: `CorporateActionAdjuster`, `manager.broadcast`; unused `date-fns`; dev-server Dockerfile | `yfinance_ingester.py:266-314`, `ws_manager.py:51-57`, `frontend/Dockerfile` |

---

## 6. What the app helps you do (value recap)

1. **Learn the full quant stack** — data → features → ML → signals → backtest → execution → dashboard, all in one repo.
2. **Paper-trade safely** — Alpaca paper account, no real capital.
3. **Screen a universe fast** — explainable BUY/HOLD/SELL with component breakdown.
4. **Research honestly** — walk-forward + purge gap + PIT fundamentals *concept*.
5. **Showcase in interviews** — a complete, Dockerized, deployable platform.

## 7. Where it stands alone

- Self-contained loop: **no external quant platform needed**. Runs on Railway; local Docker for dev.
- **Not yet** a trustworthy auto-pilot because of the Phase-A bugs; **definitely** a strong learning/portfolio asset.

## 8. Current potential & trajectory

| State | Potential |
|---|---|
| As-is | Strong learning + portfolio project; great demo |
| After Phase A | Correct core; safe to run unattended |
| After Phase A–C | Credible personal paper-trading research platform |
| After A–E | Foundation for a small SaaS/multi-user product |

## 9. CROSS-REFERENCES

- [[overview]] · [[architecture]] · [[functions-and-features]] · [[what-works-and-fails]] · [[value-and-standalone]] · [[improvement-roadmap]]