---
date: 2026-11-10
description: "ShopBrain execution plan — 8-week spine from data contract to paid pharmacy pilots, with exam-week blackout, baseline/data/money gates, and per-week Done-when criteria. No timing estimates beyond the confirmed exam window."
tags:
  - business
  - agency-launch
  - shopbrain
  - ai-platform
  - plans
confidence: high
provenance: "Rewritten 2026-11-10 (v2). Merged the owner's 8-week reorder plan with the ShopBrain concept; stripped v1's fabricated pricing/margin/savings numbers and fixed wine-shell/Algorithm101 roles. Supersedes v1."
relations:
  relates_to: "brain/ShopBrain"
---

## For future agent

This is the EXECUTION PLAN for ShopBrain — schedule gate, week order, Done-when criteria, standing rules. The architecture and repo-role map live in [[brain/ShopBrain]]; read that first if you're confused about what any repo contributes. **Plans law: no timing estimates except the confirmed exam window below; update or close this plan when its work completes.** v1 of this plan (earlier 2026-11-10) carried invented revenue figures — all pricing here is a hypothesis until pilot shops answer.

# ShopBrain Agency Launch Plan

**Goal of version 1:** a pharmacy uploads a sales CSV and gets a weekly reorder report that the owner approves.

## Schedule gate (confirmed 2026-11-10)

Owner capacity: **10–14 hrs/week** until exams. **Exams: first week of December 2026 (~Dec 1–7).**

| Window | Dates | Capacity | Work |
|--------|-------|----------|------|
| **Phase A** | Nov 10–23 (~2 wks) | 20–28 hrs | Pre-week + Week 1, start Week 2 if capacity remains |
| **Blackout** | Nov 24 – Dec 7 | ~0 hrs | Exams — no ShopBrain work |
| **Phase B** | Dec 8 → | 10–14 hrs *(TBC — confirm post-exam capacity)* | Weeks 2–8, re-checked each week |

**Phase A hard rule:** nothing may require >28 hrs. Pre-week + Week 1 only; forecasting work does not start early.

## Standing rules (owner's, non-negotiable)

1. **Stop if the baseline can't beat a naive guess** like "reorder what sold last week." Fix the data or the approach before adding AI.
2. **Permission for every shop's data**, keep it local and out of git, and **never claim savings you haven't measured** against what the owner actually did.
3. **Don't start new projects until a shop has paid you.**

Repo roles (StockOffline = app, tscore = new forecasting lib, stock-agent = patterns only, wine-shell + Algorithm101 parked): single-sourced in [[brain/ShopBrain]] — do not restate them here.

## Pre-week (1–2 days, Phase A)

- [x] Profile README that links the repos. (done 2026-11-11 — https://github.com/Anirudh-2810/Anirudh-2810)
- [ ] Pick the shop type — **decided: pharmacy** — and find one friendly pharmacy that would let you test with their data. *(type decided; outreach is the owner's task — open)*
- [x] Create a private `tscore` repo for the shared forecasting code. (done 2026-11-11 — https://github.com/Anirudh-2810/tscore)

## Week 1 — data contract and import (Phase A)

- [x] Define one sales format (`item, date, quantity, price`) and one forecast output format (`item, predicted demand, suggested reorder, confidence`). ([[tscore]] `docs/data-contract.md`, contract v1)
- [x] Add CSV import to StockOffline (`import-sales` CLI + GUI Import button; stock-safe, no double-counting).
- [x] Write a script that generates fake sales data with weekly and seasonal patterns, so testing works before real data exists. (seeded, Poisson + pay-day + flu season; 968-row example committed)

**Done when:** fake and real-format CSVs load without errors. — **met 2026-11-11**, verified end-to-end: fake 968 rows imported (stock unchanged); real-format strict → 12 skipped with row-numbered problems; `--create-missing` → 6 items created; non-contract file → hard error exit 1. Both suites green (`run_tests.py`, `test_web.py`).

## Week 2 — baselines and honest testing (Phase B)

- Build two simple forecasts in tscore: moving average and seasonal naive (same as this time last week / last year).
- Build a walk-forward backtest that trains on the past and tests on the next week, measuring error and stockouts.

**Done when:** you can see which baseline wins on the fake data — and it beats the naive "reorder what sold last week" (standing rule 1). — **met 2026-11-13**: `backtest.py` walk-forward (dense weekly axis, no-leakage test); on fake data `moving_average(k=8)` WAPE 28.10% vs naive gate 34.77% (14 weeks / 12 items / 72 folds, exit 0). Gate display distinguishes PASS / TIE / FAILED; a tie does not pass (rule 1 needs a BEAT). 42 tscore tests green.

## Week 3 — reorder logic and guards

- Turn forecasts into reorder quantities using delivery time, a safety buffer, and the owner's budget.
- Add guards: maximum order size, budget cap, never more than a set multiple of the last order.

**Done when:** every suggestion respects the limits, and tests prove it. — **met 2026-11-13**: `reorder.py` (raw_need − on hand, lead time × safety buffer) with guards `max_order_qty`, `max_multiple_of_last`, `budget_cap` (urgent-first, partial fill); grid-invariant tests in `test_reorder.py` prove every suggestion respects its limits.

## Week 4 — the report

- Generate a weekly report: reorder list, running-out alerts, dead stock, short summary message.
- Add a Forecast screen to StockOffline with an approve/reject step.

**Done when:** one click produces a report a shop owner can read without help. — **build met 2026-11-13** (owner-readability check deferred to the Week 5 pilot): `report.py` → `report.txt` (ORDER / WANTED BUT NOT ORDERED / RUNNING OUT / DEAD STOCK, measured confidence, gate disclosure) + contract `forecast.csv`; StockOffline Forecast button runs the whole pipeline and opens a report + approve/reject screen (decisions persisted, `forecast_decisions` table). Physically verified: GUI launch clean, ForecastWindow smoke, one-click path smoke (report → window → approved line in real DB). All suites green.

## Week 5 — real pilot

- Run it on 1–2 pharmacies with written permission, keeping their data local and out of git.
- Compare against what they actually did. Track stockouts caught, dead stock found, time saved.

**Done when:** you have numbers and the owner's honest feedback.

## Week 6 — neural net test

- Use `neural-engine` (NOT Algorithm101 — that's a music-trend RNN, see [[brain/ShopBrain]]) to test an RNN against the baseline on the same data.
- Only keep it if it clearly wins. If it doesn't, that's a valid result — write it up.

**Done when:** a written keep-or-drop verdict exists. — **met 2026-11-13: DROP.** From-scratch Elman RNN (engine substitute — `neural-engine` source unreachable; `Algorithm101` inspected at code level: no trainable NN, its "hidden state" is an EMA and `LocalRNN` is a wall-clock-driven viz) scored on the identical walk-forward folds: WAPE 39.92% (defaults), 34.92–49.67% across 8 seed×epoch configs — loses to both the naive gate (34.77%) and MA(8) (28.10%) every time. Written up in tscore `docs/w6-rnn-verdict.md`; revisit only with ≥6 months of real pilot data. 51 tscore tests green (incl. fold-parity vs `backtest.evaluate` + no-leakage sentinels).

## Week 7 — the "live and die" agents (small version)

- Create a population of simple forecasters, each with a virtual wallet scored on avoided stockouts and overstock.
- Death at zero and mutated children, with the money coming from the parent.
- Show it on a basic dashboard, reusing parts of stock-agent (guard style, event stream, React layout — patterns only).

**Done when:** you can watch agents die and spawn, and see whether lineages improve. — **met 2026-11-13.** Built `scripts/agents_sim.py` (stdlib): MA(k)×safety agents on the contract demand stream, wallet economy (revenue − orders − stockout penalty − holding − upkeep), death at ≤ 0, parent-funded mutated spawns (child gets `spawn_cost` from parent's wallet), immigrant refill. 52-week run: 189 agents, 17 generations, deaths in every week-bucket, 8 survivors at end. **Lineage answer: lifespan improves founders 2.7w → gen4 9.8w then declines; descendant wallets worse (structural — children inherit 40 vs founders' 100). Shape verified on 3 seeds.** Self-contained `agents_dashboard.html` replay (play/pause/speed, event stream, wallet bars). Written up in tscore `docs/w7-agents-notes.md`; 64 tscore tests green. *(Manual check for owner: open the dashboard HTML and press Play — agent cannot see rendered output.)*

## Week 8 — package and sell

- Write a one-page case study with your pilot numbers, record a short demo, write clear READMEs.
- Approach 10 shops and ask 2–3 to pay for setup plus a monthly fee. **Let their answers set your price.**

**Done when:** 10 shops approached, 2–3 asked to pay, pricing decided by their answers.

## Pricing hypotheses — UNVALIDATED `(speculation)`

v1 of this plan asserted $2,500 setup / $199-mo / $50k enterprise and 80–90% margins as if they were facts. **They were invented and have been removed.** No number lives here until a shop owner agrees to it. The only pricing input that counts: Week 8's answers.

## Pharmacy overlay (feature order for the wedge)

- **Bill-to-stock scanner** (photo of supplier bill → items/qty/prices → stock): the data feeder and the easiest demo — builds the sales history forecasting needs. OCR + vision model on top of StockOffline's existing product table.
- **Expiry / dead-stock tracker** (batch + expiry dates, pre-expiry warnings, discount-to-clear): the money-saving pitch that gets the meeting — expired stock is a direct, countable loss.
- **Weekly reorder assistant** (this plan's spine): the product they pay the monthly fee for.

Sequencing note: the scanner and expiry tracker are sales *conversations*; the reorder report is the *retention*. Standing rule 3 still applies — no new project tracks until a shop has paid.

## Risk register

| Risk | Mitigation |
|------|------------|
| No real data before Week 1 ends | Fake-data generator with weekly + seasonal patterns is a Week 1 deliverable, not a nice-to-have |
| Baseline loses to naive guess | Standing rule 1 — stop, fix data/approach; do not add models |
| Forecast looks fine but shop ignores it | Week 5 measures owner honest feedback and time saved, not model metrics |
| Scope creep into WhatsApp bot / price tracker / mismatch alerts | Standing rule 3; those are post-first-payment candidates |
| Phase B capacity lower than 10–14 hrs | Re-timebox at Dec 8; drop Week 7 (agents) before compressing Weeks 2–5 |

## Next milestone — two-week completion sprint (set 2026-11-13)

Phase A closed early (2026-11-11) and Weeks 2–4 shipped 2026-11-13 (gate PASS). Remaining plan (W5–W8) compressed into **2026-11-14 → 11-27** (owner directive: complete before exams, Dec 1st week). Order and scope only:

1. **W6 neural test — DONE 2026-11-13 (verdict: DROP, written up in tscore `docs/w6-rnn-verdict.md`).** Flag: `neural-engine` source (`Neural net 2/neuralnet.py`) exists only on the old machine, not local or GitHub as of 2026-11-13. Substitute: from-scratch RNN implemented inside tscore, run through the *same* walk-forward gate harness; keep/drop verdict unchanged. Owner pointed at `Algorithm101` as the NN source — inspected at code level: **no trainable neural net** (backend = rule scores + EMA "hidden state"; `LocalRNN` = decorative wall-clock animation), confirming the plan's original "NOT Algorithm101" warning. If the owner later copies the old `Neural net 2/` folder over, use it as a cross-check, not a blocker.
2. **W7 agents (small)** — sanctioned cut first if capacity slips (Risk register rule); never dropped silently.
3. **W8 packaging (agent part)** — READMEs, demo script, case-study skeleton with `(TBC)` placeholders — no numbers before the pilot.
4. **W5 pilot** — runs the moment a pharmacy CSV exists. **Owner critical path: pharmacy outreach** — it gates what "complete" can mean.

Owner thread: pharmacy outreach now → 10-shop approaches once demo + READMEs exist.

## Cross-references

- [[brain/ShopBrain]] — platform spec + repo role map (single source)
- [[inventory-system]] · [[inventory-system/deep-review-report]] — StockOffline as-is
- [[stock-agent/overview]] — pattern source (guards, backtest, dashboard)
- [[neural-engine]] · [[stock-predictor]] — Week 6 RNN experiment source *(original source on old machine only — substitute RNN in tscore per sprint note above)*
- [[01-Areas/Business/plans/automation-agency-launch]] — earlier Make.com agency track (separate offer, not ShopBrain)
- [[North Star]] — serves "Freelancing start" + "Ship a working ShopBrain prototype"
- [[Key Decisions]] — concept born 2026-08-27; roles corrected 2026-11-10
