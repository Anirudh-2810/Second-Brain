---
module: "stock-agent"
topic: "Stock Agent — What Works, Where It Fails"
tags: [stock-agent, analysis, bugs, limitations, review]
last_updated: "2026-08-21"
prerequisites: ["[[architecture]]", "[[functions-and-features]]"]
---

# Stock Agent — What Works, Where It Fails

> Honest scorecard from a full source read. "Works" = verified path or well-designed. "Fails" = broken, disabled, misleading, or not wired up.

---

## ✅ What works

| Area | Why it works |
|---|---|
| **Clean architecture** | Well-separated layers (core / services / api / models), easy to extend. |
| **Order placement** | Real Alpaca paper REST; market/limit/stop/stop-limit handled correctly; mid-price auto-pricing for limits. |
| **Circuit breakers** | The 5-guard pre-trade check is a genuinely good safety idea; Redis-backed, configurable, human-readable rejections. |
| **Graceful degradation** | MockRedis, mock WS, optional pandas_ta / VectorBT / Arelle / MLflow — the app runs even when heavy deps are missing. |
| **Signals engine** | Transparent weighted composite; each component is explainable and bounded ±1. |
| **Backtest lab** | VectorBT with 3 strategy families + walk-forward + sweep; separates research from execution. |
| **ML pipeline** | Proper walk-forward discipline (no look-ahead), classifier + regressor, promote-to-production registry. |
| **Point-in-time features** | `fundamentals_point_in_time` table + `ml_features_weekly` view = right idea for leakage-free research. |
| **SEC fundamentals** | Tag-mapping layer (19 metrics, multi-tag fallbacks) is well designed and testable. |
| **Frontend** | Clean React+TS structure; Zustand store; lightweight-charts integration; dedicated pages per feature. |

---

## ❌ Where it fails

### 1. Real-time streaming is dead in the dev environment
- `alpaca_ws.py` returns a **mock** on CPython 3.14 (the installed `websockets` version breaks Alpaca's client). The venv is 3.14, so **no live quotes ever reach the UI** here.
- Consequence: the Paper Trading chart shows **client-generated mock candles**, and the WS page is simulated. Fine for demo, wrong for "real-time trading".

### 2. Scheduler disabled
- `# start_scheduler()  # Disabled for testing` in `main.py` → **daily OHLCV ingest, fundamentals sync, feature computation, equity snapshots, WS health checks never run automatically**.
- Only manual endpoints keep data flowing. On a fresh DB the universe stays empty until someone calls the ingest endpoints by hand.

### 3. ML model is starved of its best features
- The `ml_features_weekly` view defines technical-indicator columns as **`NULL::numeric`** (rsi_14, macd_hist, bb_pct, atr_14, adx_14) and the **view is never refreshed automatically**.
- `feature_engine` *computes* those indicators for signals, but they are **not fed into the ML dataset**. The model trains on returns + momentum + fundamentals only — it never sees RSI/MACD/etc. that the signals engine uses.

### 4. Misleading metrics
- **`daily_pl`** on the account is actually **`unrealized_pl`** (total, not today's P&L).
- **`pe_ratio`** in valuation is computed as **`revenue / net_income`** (≈ inverse net margin), not price / earnings. The name promises P/E but the formula is something else.
- **`confidence`** on signals is just `clip(|score|, 0.3, 1.0)` — a re-scaled score, not a real probability/calibration.

### 5. Infrastructure gaps
- **docker-compose has no PostgreSQL service** — DB must be external (Neon). One-command `docker compose up` gives you an app with no DB → guaranteed failure unless you already have DATABASE_URL.
- **NullPool** on the async engine: no connection reuse; okay for tiny traffic, wasteful otherwise.
- **MockRedis silently substitutes** for real Redis — production outages can hide behind the fallback.

### 6. Security weaknesses
- **Single shared `X-API-Key`** — one key for everything, stored in the frontend bundle (`VITE_API_KEY`). Anyone with the JS bundle has the key.
- WS authenticates via **`?api_key=` query param** — keys leak into logs/URL history.
- No auth on public-facing reads (signal scan, analysis) beyond the same shared key.

### 7. Data quality & correctness edges
- **yfinance** is free but unofficial and rate-limited; gaps require manual babysitting (esp. with scheduler off).
- `DEFAULT_UNIVERSE` contains **`AVGO` twice** → duplicate ingestion work.
- SEC parser downloads **only the primary XBRL document**, not the full filing set → some filings parse partially or not at all (Arelle optional, so output varies by environment).
- Positions/orders come straight from Alpaca; **no local order/fill history is persisted** in the DB (tables exist but the execution path never writes them).
- Ingested data has **no enrichment job** storing computed features → the "feature store" is compute-on-read.

### 8. Frontend polish
- Paper Trading chart = **mock data** by design (a "demo" affordance), so the flagship screen can mislead about liveness.
- Universe strings duplicated across pages instead of shared from backend.

---

## ⚠️ Risk summary

| Risk | Severity | Mitigation |
|---|---|---|
| No live data in current env (Py3.14 WS stub) | High | Pin `websockets<13` or upgrade Alpaca client; test on 3.12 |
| Scheduler off → stale/empty data | High | Re-enable behind env flag; add startup backfill |
| ML never sees technical indicators | Medium | Populate view with real indicator columns; refresh job |
| Shared key in frontend bundle | Medium | Backend-only key usage via proxy; per-user keys |
| Mislabeled metrics (daily_pl, pe_ratio) | Low | Fix semantics or rename |
| No order history persisted | Medium | Write Alpaca order/fill events to DB tables |

## CROSS-REFERENCES

- [[overview]] · [[architecture]] · [[functions-and-features]] · [[value-and-standalone]] · [[improvement-roadmap]]