---
module: "ai-ml"
topic: "Event-Driven Backtesting — from design to C++/Python"
tags: [backtest, event-driven, systems, vectorized, python, cpp]
last_updated: "2026-08-09"
---

# Event-Driven Backtesting

> **Sources:** [[raw-sources/btech roadmap]] (Track A — "event-driven backtester" assignment), [[raw-sources/quantstart-self-study-plan]], [[raw-sources/_extracted/rf-v2006-n2-4148-pdf.txt]] (industry practices).

A backtester replays historical market data through your trading logic to produce trades and P&L. **Event-driven** architectures process each market event as it "arrives", keeping order logic realistic (no look-ahead, correct fill handling).

---

## 1. Why event-driven over quick "vectorized" loops?

| | Vectorized (numpy over returns) | Event-driven |
|---|---|---|
| Fill realism | coarse (assume fill at close) | explicit order → fill / partial / reject |
| Transaction costs | applied wholesale | per-trade with queue/slippage models |
| Look-ahead risk | high | structurally prevented |
| Complexity | low | higher (events, registry) |
| Use | research signal screening | production-grade studies |

Use vectorized for *signal discovery*, event-driven for *commitment*.

---

## 2. The event loop

Core events (a nice historical taxonomy):

```
Event
 ├── MarketEvent      (new bar / tick / book update)
 ├── SignalEvent     (strategy computed a target position)
 ├── OrderEvent      (intent: buy/sell + qty + type)
 ├── FillEvent       (execution confirmation w/ price & fees)
 └── PortfolioEvent  (post-fill P&L, equity curve)
```

Loop:

```
next_event → dispatch by type:
  market  → call strategy(data) → maybe signal
  signal  → portfolio → orders
  order   → execution handler → fills
  fill    → portfolio → P&L; update state; (intraday) re-run strategy
```

---

## 3. Look-ahead discipline (non-negotiables)

1. Strategy decision at time $t$ sees **only** data with timestamp $\le t$.
2. Fills happen at **next** bar / at a modeled price (never at the exact signal close against informed data).
3. Corporate actions & splits applied **before** compute.
4. Chronological purge in ML ([[model-selection-and-model-risk]]).

---

## 4. Cost & fill models

- **Spread cost:** ½ (ask − bid) × qty.
- **Commission & fees:** per-share / per-contract / financing rates.
- **Slippage:** both static (bp of notional) and dynamic (square-root-law influences, see [[market-microstructure]]).
- **Partial fills / cancel&retry**: optional refinement for illiquid names.

Represent as a fill model functor so strategies can be tested under multiple market micro assumptions.

---

## 5. Code Gallery

### 5.1 Python — minimal event-driven framework

```python
"""Compact event-driven backtester (bars)."""
from __future__ import annotations
import numpy as np
import pandas as pd
from dataclasses import dataclass, field


@dataclass
class BarData:
    symbol: str
    time: pd.Timestamp
    open: float; high: float; low: float; close: float
    volume: float

@dataclass
class Signal:
    symbol: str; t: pd.Timestamp; target_w: float     # target weight of capital

@dataclass
class Fill:
    symbol: str; t: pd.Timestamp; price: float; qty: float; fee: float


class StrategyBase:
    def on_bar(self, bar: BarData, portfolio) -> Signal | None: ...


class Portfolio:
    def __init__(self, cash: float, fee_rate: float = 0.0, slippage_bp: float = 1.0):
        self.cash, self.fee, self.slp, self.positions: dict[str, float] = cash, fee_rate, slippage_bp, {}
        self.equity = []

    def on_signal(self, sig: Signal, bar: BarData):
        price = bar.close * (1 + self.slp / 1e4)
        target_qty = sig.target_w * self.cash / price
        current = self.positions.get(sig.symbol, 0.0)
        qty = target_qty - current
        if abs(qty) > 1e-9:
            fill_qty = qty - (qty > 0) * 0.0   # simplify: fill whole
            self.cash -= fill_qty * price + abs(fill_qty) * self.fee
            self.positions[sig.symbol] = current + fill_qty

    def mark(self, prices: dict[str, float]):
        self.equity.append(self.cash + sum(q * prices[s] for s, q in self.positions.items()))


def run_backtest(data: pd.DataFrame, strategy: StrategyBase, fee_rate=0.001) -> pd.Series:
    port = Portfolio(cash=1_000_000, fee_rate=fee_rate)
    signal = None
    for t, row in data.iterrows():
        bar = BarData("SPY", t, *row.values)
        sig = strategy.on_bar(bar, port)
        if sig:
            port.on_signal(sig, bar)
        port.mark({"SPY": bar.close})
    return pd.Series(port.equity, index=data.index)


class MeanReversion(StrategyBase):        # toy: SMA crossover
    def __init__(self, fast=5, slow=20, lookback=200):
        self.fast, self.slow, self.lookback = fast, slow, lookback
        self._buf = []
    def on_bar(self, bar, port):
        self._buf.append(bar.close)
        if len(self._buf) < self.slow + 1: return None
        f, s, l = self._buf[-self.fast:], self._buf[-self.slow:], self._buf[-self.lookback:]
        if len(l) < self.lookback: return None
        target = 1.0 if np.mean(f) > np.mean(s) else 0.0     # long state
        return Signal("SPY", bar.time, target)
```

### 5.2 C++20 — event loop skeleton with type-erased handlers

```cpp
// backtest.hpp (C++20)
#pragma once
#include <functional>
#include <variant>
#include <vector>
#include <string>

namespace qfbt {

struct MarketEvent  { std::string sym; double px; double vol; std::int64_t ts; };
struct SignalEvent  { std::string sym; double target_w; std::int64_t ts; };
struct FillEvent    { std::string sym; double price; double qty; double fee;
                      double fwd_pnl = 0; };

using Event = std::variant<MarketEvent, SignalEvent, FillEvent>;

struct OnBar { virtual SignalEvent operator()(const MarketEvent&) = 0; virtual ~OnBar() = default; };

class Engine {
public:
    void register_on_bar(OnBar* s) { strat_ = s; }

    void push(MarketEvent e) {
        SignalEvent sig = (*strat_)(e);            // strategy hook
        if (sig.target_w != 0.0)                   // order -> fill (simplified)
            fills_.push_back(FillEvent{sig.sym, e.px, sig.target_w * equity_, 0. });
        equity_ = mark(e.px);
    }
    double equity_ = 1e6, position_ = 0, cash_ = 1e6, price_ = 100.0;

private:
    OnBar* strat_ = nullptr;
    std::vector<FillEvent> fills_;
    double mark(double px) { return cash_ + position_ * px; }
};
} // namespace qfbt
```

---

## 6. Validation beyond P&L

- **Transaction-cost sensitivity:** re-run with ±2× costs; if edge dies, it isn't real.
- **Statistical checks:** Sharpe, drawdown, calmar, hit rate; **regime splits** (bull/bear/vol).
- **Overfit audit:** count strategies tried; apply multiple-testing corrections; randomized shuffles of returns ("synthetic null") to estimate chance of the observed backtest metric.
- **Walk-forward** ([[model-selection-and-model-risk]]).

---

## 7. Architecture diagram

```
 data (bars / ticks) ──► event stream
        │
        ▼
  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
  │   Engine      │───►│   Strategy   │───►│   Orders     │
  │  (dispatcher) │    │  (signal gen)│    │  (intent)    │
  └──────┬───────┘    └──────────────┘    └──────┬───────┘
         │                                      ▼
         │                              ┌──────────────┐
         │                              │  Fill model  │  (costs, spread, ½→
         │                              └──────┬───────┘
         ▼                                     ▼
   equity curve  ◄────────── portfolio/PnL  ── fills
```

---

## 8. Related

- [[quant-toolkit-and-skills]] · [[model-selection-and-model-risk]] · [[market-microstructure]] · [[predictive-return-models]] · [[matching-engine-cpp]]