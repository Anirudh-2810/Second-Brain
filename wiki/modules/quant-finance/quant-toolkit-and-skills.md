---
module: "quant-finance"
topic: "The Quant Toolkit: Skills, Libraries & Best Practice"
tags: [quant, finance, toolkit, python, cpp, numpy, pandas, eigen, testing]
last_updated: "2026-08-09"
---

# The Quant Toolkit: Skills, Libraries & Best Practice

> **Sources:** [[raw-sources/quantstart-self-study-plan]], [[raw-sources/cmu-mscf-how-to-become-a-quant]], [[raw-sources/btech roadmap]], [[raw-sources/_extracted/rf-v2006-n2-4148-pdf.txt]] (practical optimization software).

The stack a working quant (or quant developer) runs on.

---

## 1. Three layers

```
  LAYER 3  Application  ── backtests, pricers, portfolio optimizers, risk engine
  LAYER 2  Library      ── NumPy/SciPy/pandas · Eigen · Boost · QuantLib
  LAYER 1  Systems      ── C/C++, Python, sockets, lock-free queues, OS
```

**Python** = research + glue. **C++** = production performance & latency (matching engines, market-data handlers, pricers hot path). **Both** = required.

---

## 2. Python stack (research)

| Need | Library |
|---|---|
| Arrays | `numpy` |
| DataFrames | `pandas` (+ `polars` for speed) |
| Math/stat | `scipy`, `statsmodels` |
| ML | `scikit-learn`, `xgboost/lightgbm`, `torch` |
| Optimization | `cvxpy`, `scipy.optimize`, `OSQP` |
| Time series | `statsmodels` (ARIMA/GARCH/VECM), `arch` |
| Backtesting | custom event loop ([[event-driven-backtesting]]) |
| Plotting | `matplotlib`, `plotly` |

### Everyday patterns

```python
import numpy as np, pandas as pd

px = pd.Series(np.random.lognormal(0, .01, 1000))
ret = px.pct_change().dropna()

# rolling risk stats
vol = ret.rolling(20).std() * np.sqrt(252)
sharpe = ret.mean() / ret.std() * np.sqrt(252)            # annualized

# vectorized (never loop over returns!)
position = px / px.rolling(20).mean() - 1                 # z-style signal
pnl = (position.shift(1) * ret).sum()                     # overnight return
```

**Golden rules:** vectorize; never use a Python `for` loop over price arrays in the hot path; use `shift()` to avoid look-ahead.

---

## 3. C++20 stack (production)

| Purpose | Tool |
|---|---|
| Linear algebra | Eigen (template; header-only) |
| HPC / SIMD | `std::mdspan`, `std::execution::par`, SIMD via `#include <experimental/simd>`-style |
| Numerics | `<cmath>`, Boost.Math (normal CDF, special functions) |
| Concurrency | `std::thread`, `std::jthread`, `std::atomic`, lock-free queues (Boost.Lockfree) |
| Networks | Asio/Boost.Beast for FIX-style sockets |

### Code hygiene

```cpp
// black_scholes.hpp style:
// - `constexpr` where possible (see [[stochastic-calculus-black-scholes]])
// - `noexcept` on pure math
// - templated on <std::floating_point T>
// - validate inputs with `std::expected` or precondition checks
// - small header units for pricers/risk functions
```

---

## 4. QuantLib & libraries

- **QuantLib** — the open-source C++ derivatives library (Hull-style measures, instruments, term-structure), wrappers via `ql-python`.
- Useful but *read the source* — you'll need to modify it for exotic contracts.

---

## 5. Software engineering for quants

1. **Determinism:** seed RNGs; make backtests reproducible.
2. **Time handling:** integer-typed timestamps, explicit timezone, never local-time arithmetic in logs.
3. **Monotonic clock** for latency measurement; PTP for distributed stamps.
4. **Testing:** obsessive unit tests on pricers (ﬁxed analytical price vs MC), golden-file backtests, property tests for idempotence/permutation invariance.
5. **Versioning**: pin deps, lockfiles, CI.

---

## 6. Data handling & verification

- Collect from multiple sources; check **survivorship**, **adjusted closes**, **corporate actions (splits/dividends)**.
- Timestamps: exchange-local where meaningful, normalized for analytics.
- Volume/liquidity filters before running backtests (avoid tiny illiquid names distorting P&L).

---

## 7. Architecture diagram — research-to-prod pipeline

```
  jupyter/research ──► python_vectorized_signal
        │                     │
        ▼                     ▼
  test hypothesis ──► cost-aware strategy module
        │                     │
        ▼                     ▼
  walk-forward eval ──► rewrite hot path in C++20
        │                     │
        ▼                     ▼
  risk limits ──► prod OMS / execution ([[market-microstructure]])
```

---

## 8. Related

- [[quantitative-finance-foundations]] · [[stochastic-calculus-black-scholes]] · [[event-driven-backtesting]] · [[matching-engine-cpp]] · [[model-estimation]] · [[quant-careers-and-industry]]