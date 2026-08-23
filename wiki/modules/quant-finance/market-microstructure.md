---
module: "quant-finance"
topic: "Market Microstructure, Liquidity & Execution"
tags: [quant, finance, microstructure, order-book, execution, hit-latency, market-making, hft]
last_updated: "2026-08-09"
---

# Market Microstructure, Liquidity & Execution

> **Sources:** [[raw-sources/quant-finance-basics]], [[raw-sources/cqf-quant-roles-industry]], [[raw-sources/btech roadmap]] (matching engine, high-frequency backtesting), [[raw-sources/_extracted/rf-v2006-n2-4148-pdf.txt]] (high-frequency dynamics: ~2100 ticks/day median Russell 3000), [[raw-sources/quantstart-self-study-plan]].

Market microstructure studies *how* a trade happens — the mechanics of price formation from order flow, and how you can be smart about *executing* your intended trades.

---

## 1. Limit Order Book (LOB)

Orders sorted by price:

```
   Price      Bid (buy)       Ask (sell)
   100.10         |            3,000
   100.09         |            6,000
   100.08         |           12,000      ← ask side
   ----------- spread ----------
   100.07        5,000                   ← bid side
   100.06       11,000
   100.05       18,000
```

- **Best bid / best ask** (touch); **spread** = ask − bid.
- **Depth** = quantity at each level; **depth at touch** is the relevant liquidity.
- **LOB dynamics**: market orders consume liquidity (walk the book); limit orders add it. Size/queue position/timing decide fills.
- **Microstructure metrics:** spread, depth, order-flow imbalance, realized vs effective spread, price impact ∝ √(size).

---

## 2. Who is in the market

- **High-frequency traders (HFTs)** — market makers, latency-sensitive arbitrageurs/statistical algorithms. Trade in microseconds; job is providing liquidity or capturing temporal mispricings.
- **Market makers** — post both bid and ask; earn spread, manage **inventory risk**.
- **Institutional block traders** — must split big orders to not move price (see optimal execution).
- **Retail / long-only** — usually the liquidity consumer.

**Order types:** market, limit, stop, iceberg, fill-or-kill, IOC, algos (VWAP, TWAP, IS).

---

## 3. Price impact & the square-root law

Empirical relation (Almgren–Chriss style) for a trade of size $Q$ in an asset with volatility $\sigma$ and average daily volume $V$:

$$
\text{impact} \propto \sigma \sqrt{\frac{Q}{V}}
$$

The **square-root law**: linear for tiny $Q$ (transient), then √-shaped as you cross into the top of the book.

**Components:**
- **Temporary impact** — paid in spread crossing/slippage; fades.
- **Permanent impact** — moves the price itself (informational), doesn't revert quickly.

---

## 4. Optimal Execution (Almgren–Chriss model)

Split a large order across time horizon $T$ in $N$ slices to minimize combined trading cost + risk:

$$
\min_{\{x_t\}} \mathbb E\Big[ \sum_t \big( \text{impact} \big)_t \Big] + \lambda\, \operatorname{Var}[\text{cost}]
$$

**Trade-off curve:** aggressive (fast) execution → high impact, low *duration risk*; patient execution → low impact but high uncertainty (price can run against you). **The lambda between cost & variance is the trader's risk appetite.** Algorithms (VWAP, IS - implementation shortfall) are practical implementations of this curve.

*A trading rule of thumb:* for large orders use algos with **participation-rate caps**; for market making, **inventory control** with small size and tight quoting.

---

## 5. Latency & the hardware perspective

Real-time/HFT latency budget (microseconds):

```
   timestamp feed → decode → order → exchange → confirmation
        ─0.5μs─    ─1-3μs─   ─2μs─    ─~1μs────  ─roundtrip target < 5-10μs curbs
```

- **C++20, lock-free queues, kernel bypass (DPDK), FPGA** typical in matching engines.
- Co-location: put your server beside the exchange's.
- Time-stamping & **synchronization (PTP)** out of a mismatched clock wrecks backtest integrity.

---

## 6. Microstructure pricing consequences

- **Volatility & liquidity feedback:** impact lifts vol when liquidity thins; HFTs may pull quotes in stress → flash crashes (2010, 2015) — citing the need for **circuit breakers**.
- Co-movement of liquidity across assets (the "commonality in liquidity" strand).
- For researchers: tick-level data with ~2100 ticks/day median Russell 3000 → decision horizon seconds–minutes; **timestamp precision and survivorship-purged data** are critical.

---

## 7. Architecture Diagram — a low-latency trading stack

```
  market data (itch/OUCH) ──────────────────────► Parser → normalised events
                                                          │
    ┌─────────────────────────────────────────────────────┴──────────┐
    │ strategy (signal → desired position) → execution algo scheduler│
    └────────────────────────────────────────┬───────────────────────┘
                                             ▼
    ┌───────────────┐   ┌──────────────────────────────┐   ┌────────────┐
    │  risk checks   │   │  order manager / compliance  │   │  matching/ │
    │  limits, stop  │   │  (FIX or prop protocol)      │   │  OMS layer │
    └───────────────┘   └──────────────┬───────────────┘   └────────────┘
                                       ▼
                        exchange / venue  ─►  fills  ─► P&L, position, risk
```

---

## 8. Code sketch — simple per-cap participation algo

```python
"""Naive participation-rate (VWAP-like) execution, sized to avoid market impact."""
from __future__ import annotations
import numpy as np


def participation_schedule(total_remaining: np.ndarray, particip: float) -> np.ndarray:
    """For a series of expected volumes (per interval), return the order size per
       interval such that we participate no more than 'particip' fraction."""
    return np.minimum(total_remaining, particip * np.maximum(total_remaining, 0)) \
           * 0  # placeholder for clarity; real impl below
```

```python
def participation_schedule_fix(interval_vols: np.ndarray, position_target: float,
                               particip_rate: float) -> np.ndarray:
    orders, rem = [], position_target
    for v in interval_vols:
        slice_ = min(max(particip_rate * v, 0.0), rem)
        rem -= slice_
        orders.append(slice_)
        if rem <= 0: break
    return np.array(orders)
```

---

## 9. Related

- [[quantitative-finance-foundations]] · [[event-driven-backtesting]] · [[matching-engine-cpp]] · [[model-selection-and-model-risk]] · [[risk-management-value-at-risk]]