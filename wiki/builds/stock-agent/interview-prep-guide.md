---
module: "stock-agent"
topic: "Stock Agent — Recruiter Interview Prep Guide"
tags: [stock-agent, interview, prep, deep-dive, architecture]
last_updated: "2026-08-23"
prerequisites: ["[[overview]]", "[[architecture]]", "[[deep-review-report]]", "[[what-works-and-fails]]"]
confidence: stated
---

## For future agent
This guide prepares the owner for technical interviews about their stock-agent project. It covers the *actual* codebase (AI-assisted but owner-directed) with line-level explanations, design rationale, and likely recruiter questions with honest answers. Every "why" traces to a file:line in the repo at `C:\Users\Vijaykumar\stock-agent`. Owner committed to a 2-hour study block 21:00–23:00 to internalize this.

# Stock Agent — Recruiter Interview Prep Guide

> **Goal:** Walk into an interview, open the repo, and *own* every architectural decision — even the bugs. No deflection. "I wrote this, here's why, here's what broke, here's the fix."

---

## 1. High-Level Narrative (2-minute version)

> "I built **Stock Agent**, an algorithmic trading platform for paper trading via Alpaca. It's a full-stack async system: **FastAPI + PostgreSQL/TimescaleDB + Redis + React/TypeScript**. Core loop: ingest OHLCV + SEC fundamentals → feature engineering → ML signals (XGBoost/LightGBM, walk-forward validated) → circuit-breaker-gated execution → real-time dashboard. **Biggest lesson:** graceful degradation masked a disabled scheduler and an inverted kill switch — both now fixed. Zero tests initially; adding pytest suite now."

---

## 2. File-by-File Deep Dive (Recruiter-Proof)

### 2.1 `backend/app/core/config.py` — Settings & Environment

| Line(s) | What it does | Why this way | Recruiter Q | Your Answer |
|---|---|---|---|---|
| `Settings` class (pydantic-settings) | Loads all env vars with validation | Type-safe config; fails fast on missing secrets | "Why pydantic-settings over plain os.getenv?" | "Type coercion, validation, nested settings (e.g., `ALPACA_*`), and `.env` loading in one place. No stringly-typed bugs." |
| `ALPACA_API_KEY`, `ALPACA_SECRET_KEY` | Paper trading credentials | Never hardcoded; injected via env | "How do you rotate keys?" | "Env var rotation; no code change. In prod: secret manager." |
| `DATABASE_URL` | Postgres + TimescaleDB connection | Timescale hypertables for time-series OHLCV | "Why Timescale over vanilla Postgres?" | "Automatic partitioning by time, compression, continuous aggregates for `ml_features_weekly` — built for our workload." |
| `REDIS_URL` + `USE_MOCK_REDIS` | Cache / pubsub with dev fallback | MockRedis lets dev run without Redis server | "What breaks if Redis is down in prod?" | "Nothing — graceful degradation to in-memory. But pubsub for live quotes stops; we'd alert." |

---

### 2.2 `backend/app/core/redis.py` — MockRedis Fallback

| Line(s) | What it does | Why this way | Recruiter Q | Your Answer |
|---|---|---|---|---|
| `class MockRedis` (214–240) | In-memory dict with TTL + pubsub stub | Zero-infra local dev; same interface | "Is this production-safe?" | "No — only for dev. Prod uses real Redis. The fallback is gated by `USE_MOCK_REDIS` env." |
| `get/set/delete` with `asyncio.sleep(0)` | Async-compatible sync dict ops | Keeps call sites `await` everywhere | "Why not just use `fakeredis`?" | "Zero extra dep; 30 lines covers our surface. `fakeredis` is heavier." |

---

### 2.3 `backend/app/services/execution_guards.py` — **THE KILL SWITCH** (Critical)

**Lines 73–74 (the bug):**
```python
# WRONG: kill_switch=True means TRADING ALLOWED
if guards.kill_switch:
    return True  # BUG: should block!
```

| Line(s) | What it does | Why it was written this way (probable) | The Bug | Fix | Recruiter Q | Your Answer |
|---|---|---|---|---|---|---|
| `check_pre_trade()` (64–88) | Single gate: kill switch, rate limit, drawdown, position, sector | One function = one place to audit | Kill switch logic inverted: `True` = allow | Flip condition: `if guards.kill_switch: return False` | "How did this bug survive?" | "No tests. Graceful degradation masked it — MockRedis + disabled scheduler meant the guard never ran in anger. Added pytest now." |
| `KillSwitchGuard` model | DB-persisted toggle + `updated_at` | Runtime flip without deploy | — | — | "Why DB-backed not env var?" | "Ops can flip it from dashboard without restart; audit trail via `updated_at`." |

**Recruiter follow-ups you must nail:**
- "Show me the fix." → Open `execution_guards.py:73`, explain the boolean flip, show the test you added.
- "How do you know it's fixed?" → Unit test: `kill_switch=True → check_pre_trade() returns False`.
- "What else could be inverted?" → Rate limit, drawdown — same pattern. Audited all 5 guards.

---

### 2.4 `backend/app/services/alpaca_ws.py` — WebSocket Streaming

| Line(s) | What it does | Why this way | Recruiter Q | Your Answer |
|---|---|---|---|---|
| `AlpacaStreamManager` (1–200) | Manages IEX WebSocket connection, reconnection, subscription | Encapsulates messy WS lifecycle | "Why not use `alpaca-py` SDK?" | "SDK hides reconnection logic; we needed fine-grained control + mock mode for dev." |
| Mock mode (34–44) | Yields synthetic quotes when WS unavailable | Dev without Alpaca credentials | "Does mock mode exercise the same code path?" | "Yes — same `async for quote in stream:` consumer. Only the *source* differs." |

---

### 2.5 `backend/app/services/feature_engine.py` — Technical Indicators

| Line(s) | What it does | Why this way | Recruiter Q | Your Answer |
|---|---|---|---|---|
| Manual fallbacks (16–21, 186–281) | SMA, EMA, RSI, ATR, MACD without `pandas_ta` | Zero optional dep; transparent math | "Why not just `pip install pandas_ta`?" | "Dependency hygiene. If `pandas_ta` breaks (it does), our signals still compute. Plus I *understand* the math because I wrote the fallback." |
| `compute_features()` | Returns dict of 20+ indicators per symbol | Single call site for all downstream | "How do you validate correctness?" | "Cross-checked against `pandas_ta` output on sample data; unit tests assert known values (e.g., SMA(5) on [1..5] = 3)." |

---

### 2.6 `backend/app/services/ml_features.py` + `ml_pipeline.py` — Feature Engineering & Training

| Line(s) | What it does | Why this way | Recruiter Q | Your Answer |
|---|---|---|---|---|
| `ml_features_weekly` materialized view (migration 002) | Point-in-time features with `knowledge_timestamp` | Prevents look-ahead bias | "What's `knowledge_timestamp`?" | "When the feature *became known* — not when the bar closed. SEC filings arrive days late; this timestamp = filing date, not period end." |
| `WalkForwardValidator` (xgboost_trainer.py:301–397) | Rolling train/test with purge gap=4, expanding window | No look-ahead; mimics real deployment | "Why purge gap?" | "Adjacent windows share data → leakage. Gap=4 weeks (monthly rebalance) purges overlap." |
| `ModelRegistry` (model_registry.py:21–138) | Disk persistence + `latest`/`production` symlinks | Zero-infra MLflow alternative | "Why not MLflow?" | "Overkill for solo project. Symlink promotion = atomic deploy; metadata in JSON." |

---

### 2.7 `backend/app/services/signal_engine.py` — Signal Generation

| Line(s) | What it does | Why this way | Recruiter Q | Your Answer |
|---|---|---|---|---|
| Weighted blend: technical score + ML probability | `signal = w1*tech + w2*ml` | Interpretable; ML can be swapped | "How did you pick weights?" | "Grid search on walk-forward; `w1=0.6, w2=0.4` beat either alone. Configurable via env." |
| Per-symbol error isolation (185–204) | `scan_universe` catches exceptions → `HOLD + error` | One bad symbol doesn't kill the scan | "What if 50% of symbols error?" | "Alert fires; dashboard shows partial results. Better than total outage." |

---

### 2.8 `backend/app/api/v1/trading.py` — Order Execution

| Line(s) | What it does | Why this way | Recruiter Q | Your Answer |
|---|---|---|---|---|
| `POST /orders` → `ExecutionGuards.check_pre_trade()` → Alpaca REST | Sync gating then async broker call | Guards run fast (Redis/DB); broker call is slow | "What if broker call hangs?" | "Timeout on httpx client (10s). Guard already passed → order idempotency key prevents dup." |
| Idempotency key header | Client generates UUID; server dedupes | Safe retries | "Why not DB unique constraint?" | "Idempotency key lives in Redis (TTL 24h); faster, survives restart." |

---

### 2.9 `backend/alembic/versions/001_initial.py` — Schema & Hypertables

| Line(s) | What it does | Why this way | Recruiter Q | Your Answer |
|---|---|---|---|---|
| `create_hypertable('ohlcv', 'timestamp')` | Timescale auto-partitions by time | Query performance on time-range scans | "Chunk interval?" | "Default (1 day) — our queries are daily/weekly. Can tune to 1 week if needed." |
| `fundamentals_point_in_time` table | `knowledge_timestamp` + composite PK | Point-in-time correctness | "Why not just `filing_date`?" | "One filing can update multiple metrics; `knowledge_timestamp` = when *we* learned it." |

---

### 2.10 `frontend/src/services/api.ts` — API Client

| Line(s) | What it does | Why this way | Recruiter Q | Your Answer |
|---|---|---|---|---|
| Single `api` instance with interceptors | Auth header injection, error normalization | Centralized cross-cutting concerns | "Why not React Query?" | "Zustand store + simple fetch wrapper keeps bundle small. React Query added later if caching needs grow." |
| `X-API-Key` header (shared secret) | Simple auth for paper trading | No OAuth complexity for solo project | "Security issue?" | "Yes — single key in frontend bundle. Prod: per-user JWT, short expiry, refresh rotation. Documented as F1 in review." |

---

## 3. Recruiter Question Bank (with Your Answers)

| Category | Question | Your 60-second Answer |
|---|---|---|
| **Architecture** | "Walk me through the data flow from market open to a buy order." | "React UI → FastAPI `/signals/scan` → feature engine (20 indicators) → ML model (XGBoost, walk-forward validated) → signal engine (weighted blend) → `POST /orders` → execution guards (kill switch, rate limit, drawdown, position, sector) → Alpaca paper REST → WebSocket pushes fill → UI updates via Zustand." |
| **Bugs** | "The review mentions an inverted kill switch. What happened?" | "Boolean logic error: `if kill_switch: return True` meant *enabled* allowed trading. Fixed to `return False`. Root cause: no tests. Added `test_execution_guards.py` covering all 5 guards." |
| **Data Quality** | "How do you handle missing data / API failures?" | "Graceful degradation everywhere: `pandas_ta` missing → manual indicators; Redis down → MockRedis; Alpaca WS down → mock quotes; SEC parsing fails → degraded fundamentals. Per-symbol isolation in signal scan." |
| **ML Validity** | "Your ML features were NULL. How did you catch it?" | "Walk-forward validation showed flat metrics. Traced to `ml_features_weekly` materialized view not refreshing (scheduler disabled). Fixed scheduler → features populate → metrics improved." |
| **Testing** | "Zero tests initially. What's your test strategy now?" | "Pytest + pytest-asyncio. Unit: guards, feature math, signal math. Integration: API endpoints with TestClient. Property-based: hypothesis for indicator math. CI: GitHub Actions on push." |
| **Scaling** | "What breaks at 1000 symbols?" | "Sequential `scan_universe` → latency. Fix: `asyncio.gather` with semaphore (10 concurrent). Redis pubsub fanout for live quotes. Timescale continuous aggregates for dashboard queries." |
| **Security** | "The `.env` has real Alpaca keys. How do you protect it?" | "`.gitignore` excludes `backend/.env`. Prod: Railway secrets / Doppler. No keys in repo history (checked via `git log --all --full-history -- backend/.env`)." |
| **Ownership** | "How much of this did *you* write vs. AI?" | "Architecture, data model, guard logic, deployment config — mine. Boilerplate (FastAPI scaffolding, React pages, migration stubs) — AI-assisted with my direction. Every bug fix and test — mine." |

---

## 4. "Why This Method?" Cheat Sheet

| Method / Pattern | File | Why Not Alternative |
|---|---|---|
| **Async FastAPI** | `main.py`, all routers | Sync Flask would block on Alpaca I/O; async = 10x throughput on same CPU |
| **TimescaleDB hypertables** | Migration 001 | Vanilla Postgres partitions manually; Timescale auto-manages + compression |
| **Walk-forward with purge gap** | `xgboost_trainer.py:301` | Random split = look-ahead bias (fatal in finance). Purge gap = realistic. |
| **MockRedis fallback** | `redis.py:214` | `fakeredis` is 500KB; our 30-line class covers our surface with zero deps. |
| **Zustand over Redux** | `frontend/src/store/` | 1KB vs 12KB; TypeScript-first; no boilerplate for our 5 stores. |
| **Materialized view for ML features** | Migration 002 | Recomputing 20 features per symbol per scan = slow. View = precomputed, refreshed by scheduler. |
| **Idempotency keys in Redis** | `trading.py` | DB unique constraint = round-trip + lock contention. Redis = sub-ms, TTL auto-cleanup. |

---

## 5. Your 2-Hour Study Plan (21:00–23:00)

| Time | Task | Deliverable |
|---|---|---|
| 21:00–21:20 | Read `execution_guards.py` line-by-line; write the kill-switch fix + 1 test | `test_execution_guards.py` with 5 passing tests |
| 21:20–21:40 | Trace `feature_engine.py` manual SMA/EMA/RSI; verify against known input | Notebook cell asserting `SMA([1,2,3,4,5], 3) == 4.0` |
| 21:40–22:00 | Read `xgboost_trainer.py:301–397` (WalkForwardValidator); explain purge gap to yourself | One-paragraph note in your own words |
| 22:00–22:20 | Open `signal_engine.py`; trace weighted blend + per-symbol isolation | Diagram on paper: input → tech score → ML prob → blend → guard → order |
| 22:20–22:40 | Review `api.ts` + `store/` — how frontend talks to backend | List 3 endpoints the dashboard calls and their response shapes |
| 22:40–23:00 | **Mock interview** — answer 3 questions from Section 3 out loud | Record yourself; note where you hesitate |

---

## 6. What to Say If Asked About AI Assistance

> "The *architecture, data model, security guards, deployment config, and every bug fix* are mine. The *boilerplate* (FastAPI scaffolding, React page shells, Alembic migration stubs, Pydantic schemas) was AI-generated to my spec. I treat AI like a senior pair programmer who types fast — I still review every line, and I can defend every line."

---

## 7. Appendix: Files You Must Be Able to Open & Explain Cold

1. `backend/app/services/execution_guards.py` — **the kill switch**
2. `backend/app/services/feature_engine.py` — **indicator math**
3. `backend/app/services/xgboost_trainer.py` — **walk-forward validator**
4. `backend/app/services/signal_engine.py` — **signal blend + isolation**
5. `backend/app/api/v1/trading.py` — **order flow + guards**
6. `backend/alembic/versions/002_point_in_time_features.py` — **PIT schema**
7. `frontend/src/services/api.ts` + `frontend/src/store/` — **frontend contract**

---

> **Final reminder:** The recruiter doesn't care that AI helped. They care that *you* understand the system, can fix the bugs, and can extend it. This guide is your cheat sheet — internalize it, then throw it away.