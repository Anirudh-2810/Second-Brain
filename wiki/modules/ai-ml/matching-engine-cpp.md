---
module: "ai-ml"
topic: "C++20 Matching Engine — design & implementation"
tags: [cpp, systems, matching-engine, order-book, low-latency, concurrency]
last_updated: "2026-08-09"
---

# C++20 Matching Engine — design & implementation

> **Sources:** [[raw-sources/btech roadmap]] (Track A assignment — "C++20 matching engine"); complements [[market-microstructure]].

A matching engine matches incoming orders against resting orders in a **limit order book** — the performance-critical heart of any exchange. This module covers the design, the data structures, the C++20 idioms, and the concurrency model.

---

## 1. Functional requirements

- Build/deposit orders: **add**, **cancel**, **modify**, **execute**.
- Maintain two price-side priority queues: *bids* (desc price), *asks* (asc price).
- Aggressive orders sweep the book; passive orders rest at a price.
- Produce **trades** (execution reports) and an **event log**.
- Handle **house ordering:** price-time priority (best price first; at a price, first-in-first-out).

```
order: { id, side(BUY/SELL), price, qty }
event: trade { buyer_id, seller_id, price, qty, ts }
book:  BID levels 100.05 x 1234,  100.04 x 567, ...
       ASK levels 100.06 x 888,   100.08 x 200, ...
```

---

## 2. Data structures

- **Price level:** sorted container ordered by price (desc for bids — use a mapping invariants; sealed by `std::map` with custom compare).
- **Queue at price:** FIFO of orders (id, remain qty).

The industry-cool option:
- `std::map<double, queue<order>>` gives O(log n) level lookup, dirty-simple, cache-unfriendly.
- **HFT-grade:** an **indexed (HashMap price→bucket)** + intrusive order lists, arena allocators, lock-free queues — microsecond targets.

### A note on doubles for prices
Store prices in **integer tick units** (`int64_t` = price × 10^packet), never `double` key comparisons — derivatives' floating-error cascade is real.

---

## 3. Matching algorithm (pseudocode)

```
func add_order(o):
    side_price = (o.side==BUY) ? best_ask : best_bid
    rest_qty = o.qty
    while rest_qty > 0 and can_cross(side_price):
        lvl = top of opposing book
        match_qty = min(lvl.head.qty, rest_qty)
        fill: emit trade(lvl.head.owner, o.id, lvl.price, match_qty)
        lvl.head.qty -= match_qty; rest_qty -= match_qty
        if lvl.head.qty == 0: pop lvl.head
        if lvl.qty == 0: pop lvl
        recompute top
    if rest_qty > 0:
        place remainder as resting at o.price (price-time priority)
```

**Key invariants:**
- A buy at 100.05 can only hit ask ≤ 100.05; marketable orders match immediately.
- **Post-only** orders (market maker protect) reject if they'd immediately cross.
- **Icebergs / hidden qty**: visible-only matching with reserve at the level — advance to mention.

---

## 4. C++20 code — a clean concurrent matching engine

```cpp
// matching_engine.hpp  (C++20)
#pragma once
#include <cstdint>
#include <map>
#include <queue>
#include <mutex>
#include <shared_mutex>
#include <functional>
#include <concepts>
#include <compare>

namespace qfex {

using Price = std::int64_t;      // ticks (price * scale)
using Qty   = std::int64_t;

enum class Side : std::uint8_t { buy = 0, sell = 1 };

struct Order {
    std::uint64_t id;
    Side          side;
    Price         price;
    Qty           qty;
    std::uint64_t seq;
    auto operator<=>(const Order&) const = default;
};

struct Trade {
    std::uint64_t buy_id, sell_id;
    Price price;
    Qty   qty;
    std::uint64_t seq;
};

class MatchingEngine {
public:
    explicit MatchingEngine(std::function<void(const Trade&)> on_trade = {})
        : emit_{std::move(on_trade)} {}

    std::uint64_t submit(const Order& o) {
        std::unique_lock lock{mu_};
        Order ord = o; ord.seq = ++seq_;
        return exec_order(ord);
    }

    void cancel(std::uint64_t id) {
        std::unique_lock lock{mu_};
        remove(id);                    // locate in side book & drop
    }

private:
    using Q = std::queue<Order>;
    std::map<Price, Q, std::greater<Price>> bids_;   // desc price
    std::map<Price, Q, std::less<Price>>    asks_;   // asc  price
    std::uint64_t seq_ = 0;
    std::shared_mutex mu_;                            // reader-heavy books
    std::function<void(const Trade&)> emit_;

    // generic "best opposing level"
    template <bool IS_BUY>
    auto book() -> auto& {
        if constexpr (IS_BUY) return bids_; else return asks_;
    }

    std::uint64_t exec_order(const Order& o) {
        Qty remaining = o.qty;
        const bool buy = o.side == Side::buy;
        auto& opp = buy ? asks_ : bids_;
        while (remaining > 0 && !opp.empty()) {
            const Price cross = opp.begin()->first;
            // buy matches only against ask <= o.price; sell vs bid >= o.price
            if (buy ? cross > o.price : cross < o.price) break;
            auto& q = opp.begin()->second;
            Order& taker = q.front();
            const Qty m = std::min(taker.qty, remaining);
            if (emit_) emit_(Trade{ buy ? o.id : taker.id,
                                    buy ? taker.id : o.id, cross, m, ++seq_ });
            taker.qty -= m; remaining -= m;
            if (taker.qty == 0) q.pop();
            if (q.empty()) opp.erase(opp.begin());
        }
        if (remaining > 0) {       // rest the remainder
            auto& side = buy ? bids_ : asks_;
            side[o.price].push(Order{o.id, o.side, o.price, remaining, o.seq});
        }
        return o.id;
    }

    void remove(std::uint64_t id) { /* scan both books; erase by id  */ }
};

}  // namespace qfex
```

> **Compilation notes:** `std::map<Price,Q,std::greater<Price>>` uses the C++20 `std::compare_three_way_result` generic comparator — clean since `Price` is a `std::int64_t`. `std::shared_mutex` supports reader-heavy topology inspection while matching tolerance is single-writer.

---

## 5. Concurrency & latency model

```
 market/data thread ──►  order ingest (mutex/atomic)  ──►  matching (hot loop)
        │                                          │
        └──► trade-reports ──► outbox  ◄─RMW──┐    │
                                              │
 topology per best practice:
   - ONE writer thread serializes orders (serializes seq_)
   - readers (market data clients) snapshot books under shared_lock
   - locks replaced with seqlock / ring buffers for <1us target
```

**Real-world tiers**
| Target | Approach |
|---|---|
| seconds | python, simple std::map |
| ms | C++ std::map + mutex |
| µs | lock-free queues, arena allocators, kernel bypass (DPDK), FPGA |

---

## 6. Verification strategy

- **Deterministic unit test:** pre-encoded order stream → exact expected trade stream (golden P&L sum), plus the Qty-conservation invariant: resting + executed qty == submitted qty.
- **Property test:** random orders; invariants:
  - Σ buy-qty == Σ sell-qty (executed portion).
  - Best bid ≤ best ask (never crossed in resting book).
  - Price-time priority respected at each level.
- **Fuzz + sanitizer builds** (`-fsanitize=address,undefined`).
- **Performance:** throughput (orders/sec), p50/p99 latency histogram; compare std::map vs HashMap price bucket.

---

## 7. Architecture diagram

```
                ┌──────────────────────────────┐
 sender/API     │     Matching Engine (C++)     │
 (orders) ────► │  ┌─────────────────────────┐  │
                │  │ bids_ : map ↑price      │  │
                │  │ asks_ : map ↓price      │  │
                │  │  price-time queue per   │  │
                │  │  level                  │  │
                │  └──────────┬──────────────┘  │
                └─────────────┼────────────────┘
                              │ trades
                              ▼
              trade log → market data / OMS / P&L ([[event-driven-backtesting]])
```

---

## 8. Related

- [[market-microstructure]] · [[event-driven-backtesting]] · [[quant-toolkit-and-skills]] · [[reinforcement-learning-ppo]]