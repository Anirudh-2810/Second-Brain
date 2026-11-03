---
module: "stock-agent"
topic: "Stock Agent — Algorithms, Models & Technical Indicators Reference"
tags: [stock-agent, algorithms, ml, indicators, reference]
last_updated: "2026-10-31"
---
# Stock Agent — Algorithms, Models & Technical Indicators Reference

This is a comprehensive catalog of every algorithm, machine learning model, technical indicator, and mathematical model used in the stock-agent codebase at `C:\Users\Vijaykumar\stock-agent`.

---
## 1. Technical Indicators (feature_engine.py)

| # | Indicator | File:Line | Input / Output | Parameters / Config |
|---|---|---|---|---|
| 1 | **SMA** (Simple Moving Average) | `feature_engine.py` | Price series → SMA values | period (default 20) |
| 2 | **EMA** (Exponential Moving Average) | `feature_engine.py` | Price series → EMA values | period (default 20) |
| 3 | **RSI** (Relative Strength Index) | `feature_engine.py:130-140` | Price series → RSI value (0-100) | period (default 14) |
| 4 | **MACD** (Moving Average Convergence Divergence) | `feature_engine.py` | Price series → (macd_line, signal_line, hist) | fast=12, slow=26, signal=9 |
| 5 | **ATR** (Average True Range) | `feature_engine.py` | High/Low/Close → ATR volatility value | period (default 14) |
| 6 | **ADX** (Average Directional Index) | `feature_engine.py` | High/Low/Close → ADX trend strength (0-100) | period (default 14) |
| 7 | **Bollinger %B** | `feature_engine.py` | Price → %B position (-∞ to ∞) | period (default 20), std dev (default 2) |
| 8 | **Volume Ratio** | `feature_engine.py` | Current volume / average volume | period (default 20) |

**Fallback**: When `pandas_ta` is not available, manual pandas implementations are provided at `feature_engine.py:16-21, 186-281`.

---
## 2. Signal Engine Composite (signal_engine.py)

| # | Component | File:Line | Input / Output | Purpose |
|---|---|---|---|---|
| 1 | **SMA Trend** | `signal_engine.py` | Price series → +1 / -1 / 0 | +1 if price > SMA, -1 if price < SMA, 0 otherwise |
| 2 | **RSI** | `signal_engine.py` | RSI value → +1 / -1 / 0 | +1 if RSI > 55 (bullish), -1 if RSI < 45 (bearish), 0 otherwise |
| 3 | **MACD** | `signal_engine.py` | MACD histogram → +1 / -1 / 0 | +1 if histogram > 0, -1 if < 0, 0 otherwise |
| 4 | **Momentum** | `signal_engine.py` | Price change ratio → +1 / -1 / 0 | Based on rate of price change over recent period |
| 5 | **Volume** | `signal_engine.py` | Volume ratio → +1 / -1 / 0 | +1 if volume above average, -1 if below |
| 6 | **Trend** | `signal_engine.py` | Price direction → +1 / -1 / 0 | Overall trend direction filter |

**Composite Score**: `sum of all component scores` → range [-1, 1]

**Thresholds**: 
- Score ≥ 0.4 → BUY
- Score ≤ -0.4 → SELL  
- -0.4 < Score < 0.4 → HOLD

**Confidence**: `clip(|score|, 0.3, 1.0)` → range [0.3, 1.0]

**ML Override**: Optionally blends ML probability via `ml_features.get_ml_score()` when a production model is registered.

---
## 3. ML Pipeline Models (ml_pipeline.py, xgboost_trainer.py, model_registry.py)

| # | Model | File:Line | Input / Output | Purpose / Config |
|---|---|---|---|---|
| 1 | **XGBoost Classifier** | `xgboost_trainer.py:140-210` | Feature frame → class label (BUY/SELL/HOLD) | objective: binary:logistic, eval_metric: logloss |
| 2 | **XGBoost Regressor** | `xgboost_trainer.py:210-280` | Feature frame → forward return value | objective: reg:squarederror, eval_metric: rmse |
| 3 | **LightGBM** (optional) | `xgboost_trainer.py:14-22` | Feature frame → classification/regression | Fallback when XGBoost params not available |
| 4 | **Walk-Forward Validator** | `xgboost_trainer.py:301-397` | Dataset → train/test splits with purge gap | gap=4, expanding window, no look-ahead |
| 5 | **Model Registry** | `model_registry.py:21-138` | Serialized model (joblib) + JSON metadata → "latest"/"production" symlink | Persists to disk, tracks metrics, versioned promotion |
| 6 | **Point-in-Time Feature Frame** | `ml_features.py:47-140` | Raw OHLCV + fundamentals → X matrix with forward returns as labels | ret_1w, ret_2w, ret_3w, ret_4w as target labels |
| 7 | **ML Dataset Creator** | `ml_pipeline.py:50-52` | Feature frame → X, y_reg, y_clf | Calls `create_ml_dataset()` with target horizon |

**Training Pipeline**:
- Walk-forward validation with `WalkForwardValidator` (purge gap=4)
- Splits data into expanding train / test windows
- Trains XGBoost classifier + regressor
- Logs metrics to MLflow (optional) or saves locally via joblib
- Promotes best model to "production" registry

**Feature Set** (critical limitation documented):
- Returns: `ret_1w`, `ret_2w`, `ret_3w`, `ret_4w` (forward returns)
- Momentum features
- **No technical indicators** are fed to ML (view stores them as NULL)
- Fundamentals are not called in training path (though infrastructure exists)

**Cross-Symbol Leakage Fix Needed**: `ml_features.py:113` uses `df.fillna(method='ffill')` without grouping by symbol → first NaN row at each symbol boundary gets previous symbol's value.

---
## 4. Execution Guards (execution_guards.py)

| # | Guard | File:Line | Default | Mechanism | Input / Output |
|---|---|---|---|---|---|
| 1 | **Kill Switch** | `execution_guards.py:73-74` | "enabled": True (default, **inverted bug**) | Blocks ALL order placement when armed | `check_pre_trade()` → returns (False, "Kill switch activated") when enabled |
| 2 | **Rate Limit** | `execution_guards.py:75-78` | 10 orders/min | Redis ZSET per minute, expires after 60s | `check_pre_trade()` → count orders in current minute window |
| 3 | **Drawdown** | `execution_guards.py:78-80` | 2% from day peak | Compares `account:equity:current` vs day peak Redis key | `check_pre_trade()` → if drawdown > 2% block order |
| 4 | **Position Limit** | `execution_guards.py:79-81` | 10% of account | Per-symbol notional cap | `check_pre_trade()` → if notional > 10% account block |
| 5 | **Sector Limit** | `execution_guards.py:80-82` | 25% of account | Per-sector notional cap | `check_pre_trade()` → if sector notional > 25% account block |

**`check_pre_trade()`** (`execution_guards.py:64-88`): Runs 5 guards sequentially; returns first violation reason or (True, "") if all pass.

**Note**: Bug #3.1 in deep-review-report — the kill switch check is inverted: `if not await self.is_enabled("kill_switch")` means armed (True) does NOT block, disarmed (False) blocks all trading.

---
## 5. Data Ingestion Sources (data_ingestion.py, yfinance_ingester.py, sec_parser.py)

| # | Source | File:Line | Data Type | Purpose |
|---|---|---|---|---|
| 1 | **yfinance OHLCV** | `data_ingestion.py:98` | Historical OHLCV bars | Free, unofficial, rate-limited historical data |
| 2 | **yfinance Corporate Actions** | `yfinance_ingester.py` | Dividends, splits adjustments | `auto_adjust=True` in fetch |
| 3 | **SEC EDGAR XBRL** | `sec_parser.py:107-108` | 19 semantic metrics (revenue, net_income, total_assets, EPS, free_cash_flow, etc.) | Pulls XBRL facts from 10-K/10-Q filings |
| 4 | **SEC Tags Mapping** | `sec_tags.py` | Maps ~19 metrics → multiple US-GAAP tag variants with fallbacks | Coverage tracker for incomplete tag parsing |

**SEC Parser**: Uses **Arelle** (optional dependency) — degrades gracefully if missing. Only downloads primary XBRL document (not full filing set with schema + linkbases).

---
## 6. Backtesting Models (backtest.py, VectorBT)

| # | Model | File:Line | Strategies | Purpose |
|---|---|---|---|---|
| 1 | **SMA Crossover** | `backtest_engine.py` (implied) | Fast SMA vs slow SMA cross | Trend-following entry/exit signals |
| 2 | **RSI Mean-Reversion** | `backtest_engine.py` (implied) | RSI oversold/overbought levels | Mean-reversion around RSI 30/70 |
| 3 | **ML Predictions** | `backtest.py:78-80` | XGBoost/LightGBM probability predictions | ML-driven backtest using trained model signals |

**Backtest Framework**: **VectorBT** — portfolio-level backtesting with:
- Multiple strategy families
- Walk-forward validation
- Parameter sweep (grid over strategy params)
- Metrics: total return, drawdown, Sharpe ratio, etc.

**Walk-Forward** (`backtest.py`): Rolling train/test splits, used for strategy optimization and ML model validation.

---
## 7. Mathematical / Statistical Models

| # | Model | File:Line | Description |
|---|---|---|---|
| 1 | **Mid-Price Calculation** | `services/alpaca_rest.py:34-36` | `(bid + ask) / 2` | Computes mid-price from latest quotes for order pricing, especially for limit orders |
| 2 | **Score Clipping** | `signal_engine.py:165-167` | `clip(|score|, 0.3, 1.0)` | Rescales composite signal score to [0.3, 1.0] range for confidence display |
| 3 | **Forward Return Labels** | `ml_features.py:47-140` | `ret_1w`, `ret_2w`, `ret_3w`, `ret_4w` | Forward-period returns used as regression labels in ML training |
| 4 | **Purge Gap** | `xgboost_trainer.py:301-397` | gap=4 | 4-period gap between train/test splits to prevent look-ahead bias |
| 5 | **Expanding Window** | `xgboost_trainer.py:301-397` | Training window expands over time | Simulates real trading horizon; earlier data always included |
| 6 | **Score Thresholds** | `signal_engine.py` | ±0.4 → BUY/HOLD/SELL | Decision boundaries for signal generation from weighted composite |
| 7 | **Confidence Clipping** | `signal_engine.py:165-167` | clip(|score|, 0.3, 1.0) | Minimum confidence 0.3 even for HOLD signals; maximum 1.0 for strong signals |

---
## 8. Summary Table: Where Each Algorithm Lives

| Algorithm/Model | Primary File | Secondary References |
|---|---|---|
| SMA, EMA, RSI, MACD, ATR, ADX, Bollinger %B, Volume Ratio | `backend/services/feature_engine.py` | `backend/services/signal_engine.py` |
| Signal Composite (SMA/RSI/MACD/momentum/volume/trend) | `backend/services/signal_engine.py` | — |
| XGBoost Classifier/Regressor | `backend/ml_pipeline.py`, `backend/xgboost_trainer.py` | `backend/model_registry.py` |
| Walk-Forward Validator | `backend/xgboost_trainer.py:301-397` | — |
| Model Registry (joblib + JSON) | `backend/model_registry.py` | `backend/xgboost_trainer.py` |
| Point-in-Time Feature Frame | `backend/ml_features.py` | `backend/ml_pipeline.py` |
| Execution Guards (5 guards) | `backend/services/execution_guards.py` | `backend/trading.py` |
| yfinance OHLCV Ingestion | `backend/services/data_ingestion.py`, `backend/services/yfinance_ingester.py` | — |
| SEC XBRL Fundamentals | `backend/services/sec_parser.py`, `backend/services/sec_tags.py` | — |
| VectorBT Backtest Strategies | `backend/backtest_engine.py` (implied) | `backend/backtest.py` |
| Mid-Price Calculation | `backend/services/alpaca_rest.py:34-36` | — |