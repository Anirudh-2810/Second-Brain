---
module: "stock-agent"
topic: "Stock Agent — Functions & Features Inventory"
tags: [stock-agent, features, trading, signals, backtest, ml, ingestion]
last_updated: "2026-08-21"
prerequisites: ["[[overview]]"]
---

# Stock Agent — Functions & Features Inventory

> Complete inventory of what the app *does*, grouped by subsystem, with the endpoint/entry point for each.

---

## 1. Paper trading (execution)

| Function | Entry point | Notes |
|---|---|---|
| Account summary (cash, buying power, equity) | `GET /trading/account` | `daily_pl` ≈ unrealized P&L |
| List positions | `GET /trading/positions` | proxied from Alpaca |
| List orders | `GET /trading/orders` | optional status filter |
| Place order | `POST /trading/orders` | market / limit / stop / stop-limit; auto mid-price for limit |
| Cancel order | `DELETE /trading/orders/{id}` | |
| Close position | `DELETE /trading/positions/{symbol}` | |
| Close all positions | `DELETE /trading/positions` | |
| Circuit-breaker pre-check | runs on every order | 5 guards → reject with reason |
| Kill switch arm/disarm | `GET/POST /trading/guards` | Redis-backed state |
| Live quotes | `GET /trading/quotes` | latest IEX quotes |

## 2. Signals

| Function | Entry point | Notes |
|---|---|---|
| Scan universe | `GET /signals/scan` | weighted composite score per symbol |
| Per-symbol signal | `GET /signals/{symbol}` | components breakdown + ML overlay |
| Scan with ML | `POST /signals/scan/ml` | blends model probability |

Signal components: SMA trend · RSI · MACD · momentum · volume · trend. Output `BUY / HOLD / SELL` with `confidence`.

## 3. Market analysis

| Function | Entry point | Notes |
|---|---|---|
| Latest fundamentals | `GET /analysis/{symbol}/fundamentals` | from SEC-parsed facts |
| Valuation snapshot | `GET /analysis/{symbol}/valuation` | derived metrics (note: `pe_ratio` is revenue/net_income — see [[what-works-and-fails]]) |

## 4. Backtesting (VectorBT)

| Function | Entry point | Notes |
|---|---|---|
| Run backtest | `POST /backtest/run` | strategies: SMA cross, RSI mean-reversion, ML predictions |
| Walk-forward | `POST /backtest/walk-forward` | rolling train/test |
| Parameter sweep | `POST /backtest/sweep` | grid over strategy params |
| List registered models | `GET /backtest/models` | |

## 5. ML pipeline

| Function | Entry point | Notes |
|---|---|---|
| Train model | `POST /ml/train` | XGBoost/LightGBM classifier + regressor |
| Walk-forward validation | `POST /ml/walk-forward` | date-based splits, no look-ahead |
| Promote model | `POST /ml/promote` | moves a candidate to "production" registry |
| Weekly retrain | scheduler job | **disabled** ("Disabled for testing") |
| Live ML score | `get_ml_score()` | used by signal engine when production model exists |

Feature set: point-in-time returns (ret_1w … ret_4w), momentum features, fundamentals merge. **No technical-indicator features feed the ML model** — the materialized view stores technical columns as `NULL` (see [[what-works-and-fails]]).

## 6. Data ingestion

| Function | Source | Notes |
|---|---|---|
| OHLCV backfill + daily | yfinance | free but rate-limited |
| Corporate actions | yfinance | |
| Fundamentals | SEC EDGAR (XBRL) | 10-K / 10-Q; ~19 semantic metrics |
| Feature computation | feature_engine | pandas_ta or fallback; universe = 60 tickers |

## 7. Data health

| Function | Entry point | Notes |
|---|---|---|
| Coverage summary | `GET /data-health/summary` | rows per symbol, date spans |
| OHLCV gaps | `GET /data-health/ohlcv-gaps` | missing periods |
| Fundamentals gaps | `GET /data-health/fundamentals-gaps` | symbols without facts |

## 8. Real-time streaming

| Function | Entry point | Notes |
|---|---|---|
| Live quotes feed | `WS /ws` | Alpaca IEX → Redis pub/sub → browser |
| Trade feed | `WS /ws` | same pipeline |
| Reconnect logic | `useWebSocketConnection` | browser auto-reconnect |

**Current limitation:** on Python 3.14 the Alpaca WS client is stubbed to a mock, so this path is effectively **demo/simulated** in the dev environment.

## 9. Frontend pages

| Page | Route | Shows |
|---|---|---|
| Overview | `/` | market snapshot, quick stats |
| Signals | `/signals` | scan results table |
| Analysis | `/analysis` | fundamentals & valuation |
| Backtest Lab | `/backtest` | run/persist backtests |
| Data Health | `/health` | coverage & gaps |
| Paper Trading | `/trading` | order entry, positions, P&L cards, kill switch, quotes, chart |

## CROSS-REFERENCES

- [[overview]] · [[architecture]] · [[what-works-and-fails]] · [[value-and-standalone]] · [[improvement-roadmap]]