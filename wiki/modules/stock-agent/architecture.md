---
module: "stock-agent"
topic: "Stock Agent — Architecture Deep Dive"
tags: [stock-agent, architecture, fastapi, backend, frontend, redis, database]
last_updated: "2026-08-21"
prerequisites: ["[[overview]]"]
---

# Stock Agent — Architecture Deep Dive

> How every component fits together, read from the actual source. Paths are relative to `C:\Users\Vijaykumar\stock-agent`.

---

## 1. Backend application factory (`backend/app/main.py`)

- **Lifespan** initializes DB tables (`Base.metadata.create_all`), seeds execution-guard config, loads the ML registry.
- **Scheduler**: `start_scheduler()` is **commented out — "Disabled for testing"** → the APScheduler jobs (daily OHLCV ingest, fundamentals sync, feature computation, equity snapshots, WS health checks) never run automatically.
- All routers mounted under `/api/v1`.

### Router map

| Prefix | Router | Capabilities |
|---|---|---|
| `/trading` | trading | account, positions, orders (market/limit/stop/stop-limit), cancel, close, close-all |
| `/backtest` | backtest | run backtest, walk-forward, parameter sweep, models list |
| `/signals` | signals | scan universe → weighted signals + ML prob |
| `/analysis` | analysis | latest fundamentals, valuation metrics |
| `/data-health` | data_health | coverage summary, OHLCV/fundamentals gaps |
| `/ws` | websocket | real-time quote/trade streaming via WS manager |

---

## 2. Core infrastructure

### Database (`core/database.py`)

- Async SQLAlchemy + **PostgreSQL/TimescaleDB**.
- Uses **`NullPool`** → every connection is opened/closed per query (serverless-style; fine for low traffic, no connection reuse).
- Migrations via Alembic:
  - `001_initial.py` — TimescaleDB hypertables (`ohlcv`, `fundamentals_point_in_time`), tickers.
  - `002_point_in_time_features.py` — materialized view `ml_features_weekly`.

### Redis (`core/redis.py`)

- Real Redis for: rate-limit counters, drawdown peaks, position sizes, guard config, pub/sub.
- **MockRedis fallback** → app runs fully without Redis. Risk: silently hides Redis outages in production.

### Security (`core/security.py`)

- Single shared **`X-API-Key`** (env `API_SECRET_KEY`) checked on all routes via FastAPI dependency.
- Frontend stores it as `VITE_API_KEY` and sends it on every request.
- WS authenticates by **`?api_key=` query param** (visible in URLs / server logs).

---

## 3. Trading & execution layer

### `services/alpaca_rest.py`

- Thin wrapper over **Alpaca paper REST** (account, positions, orders, quotes).
- Computes **mid-price** from latest quotes for order pricing.
- `get_account()` maps `unrealized_pl` into `daily_pl` (≈ not a true "today" figure — see [[what-works-and-fails]]).

### `services/alpaca_ws.py` + `ws_manager.py`

- Streams **IEX quotes/trades** from Alpaca WebSocket → Redis pub/sub → WS manager → connected browsers.
- **Disabled on Python 3.14**: the project venv is CPython 3.14 and `alpaca_ws` returns an "unavailable" mock because the installed `websockets` version breaks Alpaca's client. So in the dev environment all real-time streaming is **simulated**, not live.

### `services/execution_guards.py` — the circuit breakers

| Guard | Default | Mechanism |
|---|---|---|
| Kill switch | off | blocks all order placement when armed |
| Rate limit | 10 orders/min | Redis ZSET per minute |
| Drawdown | 2% from day peak | compares `account:equity:current` vs day peak |
| Position limit | 10% of account | per-symbol notional cap |
| Sector limit | 25% | per-sector notional cap |

- Config stored in Redis (`guard:*` keys) + DB table; default config seeded in `main.py`.
- Each order runs `check_pre_trade()` → 5 guards; violation returns a human-readable `reason`.

### `services/signal_engine.py`

- Weighted composite of **SMA trend, RSI, MACD, momentum, volume, trend** components, each ±1.
- Final score in [−1, 1]; thresholds ±0.4 → BUY/HOLD/SELL.
- Confidence = `clip(|score|, 0.3, 1.0)`.
- Optionally blends an ML probability via `ml_features` when a production model is registered.

---

## 4. Data ingestion & features

### `services/data_ingestion.py`

- Default universe: **60 tickers** (`DEFAULT_UNIVERSE`; note `AVGO` appears twice).
- OHLCV via **yfinance** (free, unofficial; rate-limited) — *not* Alpaca historical bars.

### `services/yfinance_ingester.py`

- Fetches OHLCV + corporate actions; skips via `EXCLUDE_*` lists.

### `services/sec_parser.py` + `sec_tags.py`

- Pulls **SEC EDGAR** 10-K/10-Q XBRL facts for a ticker.
- `sec_tags.py` maps ~19 semantic metrics (revenue, net_income, total_assets, EPS, free_cash_flow…) → US-GAAP tag variants with per-tag fallbacks.
- Parsing uses **Arelle** (optional dependency) — degrades gracefully if missing.

### `services/feature_engine.py`

- Computes technical indicators (SMA/EMA, RSI, MACD, ATR, ADX, Bollinger %B, volume ratio…) via **pandas_ta** (optional; ships a manual fallback).
- Skips symbols with `< 200` rows.

### `services/ml_features.py`

- Builds a **point-in-time** feature frame (forward returns as labels), merges fundamentals, and exposes `get_ml_score()` for live signals.

### `services/ml_pipeline.py` + `xgboost_trainer.py` + `model_registry.py`

- Walk-forward training of **XGBoost / LightGBM** classifier + regressor.
- MLflow logging **optional**; registry stores models locally (joblib) with a JSON index.
- `retrain_weekly_job` / `promote_model` / `train_model` entry points.

---

## 5. Frontend (`frontend/src/`)

| Area | Detail |
|---|---|
| Routing | `/` Overview · `/signals` · `/analysis` · `/backtest` · `/health` · `/trading` |
| State | Zustand store (`store/tradingStore`) |
| API | `services/api.ts` axios client with `X-API-Key` header |
| WebSocket | `hooks/useWebSocket` + `useWebSocketConnection` |
| Charts | Lightweight Charts wrapper (`components/Chart`) |
| Pages | PaperTrading (OrderEntry, PositionsTable, PnLCards, KillSwitch, QuoteTiles) |

- Note: `PaperTrading` chart renders **client-generated mock OHLCV** when no live WS data — a demo affordance, not live data.

---

## 6. Deployment

- **Docker Compose**: services `backend`, `frontend`, `redis`. **No PostgreSQL service** → DB must come from elsewhere (README targets **Neon**).
- **Railway** for hosted deployment.
- `.env.example` expects: `DATABASE_URL`, `REDIS_URL`, `API_SECRET_KEY`, `ALPACA_API_KEY`, `ALPACA_SECRET_KEY`, `ENVIRONMENT`, `VITE_API_URL`, `VITE_WS_URL`, `VITE_API_KEY`.

## CROSS-REFERENCES

- [[overview]] · [[functions-and-features]] · [[what-works-and-fails]] · [[value-and-standalone]] · [[improvement-roadmap]]