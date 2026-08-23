---
module: "programming"
course: "CS50x — Introduction to Computer Science"
week: 10
topic: "Final Project — Ideas, Logic, Build Method & Learning Guide"
tags: [programming, computer-science, cs50, harvard, final-project, portfolio, flask, python, sql]
last_updated: "2026-08-17"
---

# CS50x Final Project — Ideas & Selection Guide

> **What it is:** the climax of CS50x — your chance to build original software that draws on the course's lessons, solves a real problem, and outlives the course. Any language is allowed; the proven path is a **Flask + Python + SQL + JavaScript** web app.
> **This page = idea selection.** For the full step-by-step build-and-submit blueprint, go to **[[cs50/final-project-planner|Final Project Planner]]** (scope → schema → build → README → video → submit → certificate).
> **Deadline (2026 cohort):** Dec 31, 2026 — submit `submit50 cs50/problems/2026/x/project`, then **claim the certificate** on your [gradebook](https://cs50.me/cs50x) or the course is not considered complete.
> **Fits the wiki:** this is the build-first, visible-portfolio move recommended in [[winning-in-tech-art-of-winning]] and the payoff of the whole CS50 arc ([[cs50/index]]).

---

## 1. The Three Deliverables

| Deliverable | Requirement | Why it sinks people |
|---|---|---|
| **Working project** | Compiles/runs without errors; test on a clean environment | Dependencies that work on your machine fail elsewhere |
| **README.md** | **Multiple paragraphs** describing title, what it does, each file, design choices, **and the video URL** | The spec asks for *"several hundred words"* and ~**750 is the soft guideline** (not a hard fail line) — but a thin or vague README is still the **#1 reason projects look under-built**. Write it last, give it real time |
| **Walkthrough video** | **No more than 3 minutes**; must **open with 5 items**: project title, your name, GitHub **and** edX usernames, city & country, and the recording date. Demo with slides/screenshots/voiceover/live action | Silent slideshow of code fails; forgetting the opening card or making it "private" fails submission |

**AI tools are allowed** (this project only — not the PSets) — but the work must essentially be yours, you must **cite any AI use in code comments and the README**, or it's an academic-honesty violation that can cost your certificate retroactively.

**Group work:** 2–3 people allowed, but scope must scale with group size (2–3× a solo project). Every member must contribute equally.

---

## 1b. How to submit — the official 3 steps (do them in order)

> All three steps must be finished **before `2026-12-31T23:59:00+00:00`**. In the CS50 Codespace, keep everything in a directory called **`project`**.

**Step 1 — Video (≤ 3 min).** Record a screencast of your project in action. The opening section **must display** all five of: project title · your name · your GitHub username · your edX username · your city and country · the date you recorded. Narrate it. Upload to YouTube (unlisted is fine — **not** private), copy the URL, then submit it via the **official video form**: <https://forms.cs50.io/65ba090e-aba1-41de-a8f3-13f7701f399b>

**Step 2 — `README.md` + submit.** Create a file named exactly `README.md` in `project/`. Use the official template:

```markdown
# YOUR PROJECT TITLE
#### Video Demo:  <URL HERE>
#### Description:
TODO
```

Then, from inside `project/`, run:

```
submit50 cs50/problems/2026/x/project
```

Log in with your GitHub username/password when prompted. The command uploads the whole directory (code + README).

**Step 3 — Load your gradebook (do not skip!).** A few minutes after submitting, visit **<https://cs50.me/cs50x>**. Loading the gradebook is what triggers the check for completion and generates your free certificate. **Claim the free certificate** (link at the top) before the deadline, then confirm you see the green "course completed" banner — otherwise the course is not complete.

**Troubleshooting:**
- Submission too large → ZIP the folder's contents (except `README.md`) and submit the ZIP; keep it **under 100 MB**; or drag-and-drop onto the `cs50/problems/2026/x/project` branch of `github.com/me50/USERNAME`.
- Submitted but no result in the gradebook → resubmit with **only** the `README.md` this time (no need to resubmit the video form).
- Never make the video "private" — graders can't watch it.

---

## 2. Selection Heuristics

- **Scope by time.** ~2 weeks → Chrome extension / CLI tool. ~4–6 weeks → full web app or game. A *working, well-documented* simple project beats a half-finished ambitious one.
- **Pick a story you can tell in an interview.** Projects that solve a real problem give you a natural "why I built this."
- **Don't resubmit Finance as-is.** It's a known quantity; it proves competence but signals no initiative.
- **Draw on the course's lessons** (C/pointers, algorithms, data structures, SQL, Flask) so the throughline from pset → project is obvious.

---

## 3. Curated Shortlist (tailored picks)

**1. Personal Portfolio / Expense Tracker (Flask + SQL + JS)** — *best fit for the quant track.* Pull live market data (yfinance API), track holdings, compute P/L, allocations, and basic risk stats; chart with Chart.js. Extends the Finance pset into something genuinely custom with real data + SQL.

**2. Spaced-Repetition Flashcard App (Flask + SQLite + JS)** — implement the SM-2/Anki scheduling algorithm. Doubles as a study tool for the AI module's 6 sub-notes; showcases scheduling logic, DB design, and a tool you'll actually use.

**3. "AI-as-tutor" CLI / Study-Buddy (Python + API)** — a quiz/explainer bot over your own notes (JSON + HTTP + command-line arg parsing). Easy win, fits the [[learn-python-fast-system]] theme; cite the AI usage per course rules.

**4. Quant Backtester / Strategy Dashboard (Python + Flask)** — surface the [[event-driven-backtesting]] architecture in a web UI with results tables and equity curves; ties the whole quant + programming stack together.

**5. Ray Tracer in Python (from scratch)** — 3D rendering via vectors/linear algebra; visual payoff and deep math cross-link to [[math-for-programming]] and the [[mathematics/overview|Mathematics]] module.

### Quick wins (< 2 weeks)

- **Chrome extension** (e.g., focus/study blocker) — JavaScript + JSON only, browser handles the UI. Logic: event-driven design (listeners + state). Teaches *delivery* (something installed in Chrome) more than new CS — right call when time is short.
- **Typing speed test** — timers + event listeners, random passages.
- **CLI to-do manager** — file I/O + argparse.
- **Password generator (Tkinter GUI)** — randomness + simple GUI.

---

## 4. Project Deep-Dives — Logic, Method & Learning

### 4.1 Personal Portfolio Tracker (Flask + SQL + JS) — the quant pick

**The logic behind it.** This is Finance *plus two real challenges*: live external data and derived calculations. Finance gives you buy/sell/quote; a portfolio tracker forces you to compute position value, % P/L, and allocation — which means the SQL schema must let *one query sum holdings by asset*, not just dump rows. That's the difference between a CRUD demo and an engineering problem: **the data shape determines the features.** The external API (yfinance) adds JSON, HTTP, caching, and error handling (rate limits, bad tickers, network failures) — no CS50 pset teaches that; it's the genuine "next level" skill.

**Build method (order matters).**
1. **Schema first.** `users (id, username, hash)` · `transactions (id, user_id, symbol, shares, price, timestamp)`. Store each fill as a row and compute positions with `GROUP BY` + `SUM` — more elegant and auditable than maintaining a hand-updated `holdings` table (which drifts). Row-based is the "better" outcome.
2. **API layer.** A small `helpers.py` wrapping yfinance: `get_quote(symbol)` → dict. Cache quotes so you don't hammer the API. **Note:** yfinance is an *unofficial* Yahoo API — it can be flaky or rate-limited in the Codespace. Plan a fallback: cache last-known prices in SQLite, and/or ship a `sample_data.py` that works offline so your demo and README never depend on the network being up.
3. **Auth + sessions.** Port the Finance pattern (`register`/`login`/`logout`, `@login_required`, `session`) — reuse the pset.
4. **Core routes, one at a time.** `index` (dashboard + Chart.js allocation pie), `quote`, `buy`, `sell`, `history`. Each route is an incremental test; one working before the next.
5. **Harden.** Empty states (no holdings yet), bad input, parameterized SQL (no injection), graceful API failures.

**The learning.** SQL aggregation (`GROUP BY`/`SUM`/`JOIN`), relational design (rows vs derived state), API consumption, sessions/auth, charts — and the meta-skill: **turning a vague feature ("show my portfolio") into schema + SQL + route + template.** *Difficulty: medium. Time: 3–4 weeks.*

### 4.2 Spaced-Repetition Flashcard App (SM-2 / Anki-style)

**The logic behind it.** The differentiator is an *algorithm*, not a UI. SM-2 decides *when* each card reappears from your rating (again/hard/good/easy) via a tiny recurrence — pure week-3 algorithms. The "queue" is just cards ordered by due date (week 5 data-structure thinking). Persisting intervals/ease per card is SQL (week 7). It's the closest CS50 project to **an algorithm you can feel running** — and it doubles as the study tool for the AI module's 6 sub-notes.

**Build method.**
1. **Implement the algorithm on paper first.** Write the SM-2 recurrence (rating → new interval + ease factor) in pseudocode *before* any web code. Input: card + rating. Output: interval + ease.
2. **Schema.** `cards (id, deck_id, front, back, ease, interval, due_date)` · `decks` · `reviews` (audit trail).
3. **The review loop route.** Fetch due cards (`WHERE due_date <= now ORDER BY due_date`), present one, rate it, persist the update, repeat.
4. **Stats.** Due today / total, streak — cheap and motivating.
5. **CSV import** for seeding decks — file I/O (week 2) makes it a real daily tool.

**The learning.** Implementing an algorithm from a spec, `datetime`/`timedelta` math, SQL date queries — plus the meta-gain: you internalize the memory science behind Anki. *Difficulty: low–medium. Time: 2–3 weeks.*

### 4.3 "AI-as-Tutor" CLI / Study-Buddy (Python)

**The logic behind it.** Smallest scope, biggest modern payoff. You already own notes as structured text; a CLI that (a) reads a JSON Q&A file, (b) quizzes you, and (c) optionally POSTs to an LLM API — that's file I/O + argparse + HTTP + JSON, all weeks 1/6/7 ideas wrapped in one tool. The learning is *integration*: reading API docs, keeping secrets in environment variables (a real security discipline), modeling data as JSON. No frontend = no distraction = you finish fast.

**Build method.**
1. **Define the data format.** JSON schema: `{"topic": "...", "qa": [{"q": "...", "a": "..."}]}`.
2. **Argparse subcommands:** `quiz`, `ask`, `flash`.
3. **Quiz mode:** shuffle, score, persist session history (CSV or SQLite).
4. **`ask` mode:** POST to the API, parse JSON, print; API key from `os.environ`, never hardcoded.
5. **README documents usage.**

**The learning.** Argument parsing, JSON modeling, HTTP POST + auth headers, env-var security, prompt design. *Difficulty: low. Time: 1–2 weeks.*

### 4.4 Quant Backtester / Strategy Dashboard (Python + Flask)

**The logic behind it.** A backtest is a *simulation loop*: iterate price bars, apply a strategy rule, fill orders at the correct price, track equity, and never peek at future data. The logic skill is **separation of concerns** — the engine is pure, headless Python (testable), and the Flask layer is only a viewer. That's exactly the architecture [[event-driven-backtesting]] argues for, made visible with an equity curve and trade table.

**Build method.**
1. **Engine first, headless.** `backtester.py`: (price series, strategy params) → (equity curve, trade log). Test against a tiny CSV before any web code.
2. **Strategy as a parameter.** Start with SMA crossover (10/50) — simple, transparent.
3. **Look-ahead discipline.** Only data ≤ current bar; make the "no future data" rule explicit in code.
4. **Web layer.** Route runs the backtest on demand, stores results in SQLite, renders equity chart + trade table.
5. **Metrics.** Sharpe ratio / max drawdown readout — connects to [[quant-toolkit-and-skills]].

**The learning.** Event-loop simulation, engine/UI separation, parameterization, financial metrics — and the most transferable lesson: **write the hard logic without a UI, prove it, then hang a UI on it.** *Difficulty: medium–high. Time: 3–5 weeks.*

### 4.5 Ray Tracer in Python (from scratch)

**The logic behind it.** A ray tracer turns linear algebra into pixels: for each pixel, cast a ray; find the nearest surface; shade via dot products and normals. It's week-3 recursion + week-2 arrays + pure math, with zero external dependencies (`math` + a PPM image writer). The logic chain is *visible*: vector → intersection → shading → color → file. Every bug is a visual bug you can stare at — ideal feedback for learning.

**Build method.**
1. **Image I/O first.** Write an empty PPM image (red gradient) — see the pipeline work instantly.
2. **Vector math module.** `Vec3`: add, sub, scale, dot, normalize — [[math-for-programming]] made concrete.
3. **Sphere intersection.** Ray-sphere hit test (quadratic formula) → a circle appears. Big-win moment.
4. **Lighting.** Normal + light direction → diffuse (`dot`), plus ambient.
5. **Reflections via recursion.** Bounce N times, stop at a depth limit (recursion with a base case).
6. **Polish.** Multiple objects, shadows, ground plane.

**The learning.** Applied linear algebra, the quadratic formula in code, recursion, per-pixel loop thinking, visual debugging — plus a stunning portfolio artifact. *Difficulty: medium. Time: 2–3 weeks.*

---

## 5. The Build Method (applies to every idea)

- **Phase 0 — Scope freeze (day 1).** One-line spec: "For [user], [app] does [thing]." Then define **good / better / best** outcomes (CS50's own proposal language). Decide explicitly what you will *not* build. Lock the stack.
- **Phase 1 — Data & hard logic first.** Schema or core algorithm before any UI. The risky 20% is always the logic, never the buttons.
- **Phase 2 — Vertical slice.** Build the thinnest end-to-end path (one input → one stored row → one screen). Expand in loops, one feature at a time, each loop leaving the app working — the learning loop from [[programming-flowcharts]].
- **Phase 3 — Daily working increments.** Winner's loop / never-zero-days from [[modules/self-mastery/life-systems-design|Life Systems Design]]: every day ends with a *running* app. Commit to git at every green point.
- **Phase 4 — Harden.** Empty states, visible errors, secrets in env vars, parameterized SQL.
- **Phase 5 — Prove it on a clean machine.** Fresh venv/Codespace, follow your own README, fix where your docs are wrong.
- **Phase 6 — Document & demo.** README (≥750 words) written last but given real time; video = demo 3 features + explain 1 design decision; cite every AI use.

**Weekly milestones:** M1 = spec + schema + vertical slice · M2 = core feature set · M3 = hardening + clean-machine test · M4 = README + video + submit.

---

## 5b. Your go-forward plan (turn this into a calendar)

> Recommended for **you** given the quant-track wiki: the **Portfolio Tracker** (idea #1) is the highest-leverage pick — it extends Finance (so you reuse proven code), pulls real data, and produces an interview story. If time is tight (< 2 weeks), fall back to the **CLI study-buddy** (idea #3). Whatever you choose, follow this exact order:

**Week 1 — Decide & scaffold (scope freeze).**
1. Write the one-line spec: *"For [me], [app] does [thing]."*
2. Define **good / better / best** outcomes; write down what you will **not** build.
3. Create the `project/` folder, `git init`, and the **schema first** (SQL tables or core data file).
4. Build the **thinnest vertical slice**: one input → one stored row → one screen that works end-to-end.

**Week 2 — Core feature set (one feature per day, app always running).**
5. Add features in order of risk: the hard logic first (portfolio aggregation / SM-2 algorithm / backtest engine), UI last.
6. Commit to git at every green point. Test each route/function before moving on.

**Week 3 — Harden & prove.**
7. Empty states, invalid input, errors that don't crash, secrets in env vars, parameterized SQL.
8. **Clean-machine test:** fresh Codespace/venv → follow your own README → fix whatever breaks. (This is where most people discover their docs lie.)

**Week 4 — Document, record, submit (deadline: Dec 31).**
9. Write `README.md` (multiple paragraphs, ≥~750 words, video URL included).
10. Record the ≤3-min video: opening card with title · name · GitHub + edX usernames · city/country · date, then a live demo of 2–3 features + 1 design choice. Upload (unlisted), submit the video form.
11. `submit50 cs50/problems/2026/x/project` from `project/`.
12. Visit cs50.me/cs50x, **claim the certificate**, confirm the green banner.

**Daily rule:** never let the app be *broken* at the end of a day (winner's loop / never-zero-days). If a feature is half-done, finish or revert before stopping.

---

## 6. Skill Matrix — What Each Idea Teaches

| Idea | CS50 concepts exercised | New skills | Transfers to |
|---|---|---|---|
| Portfolio tracker | SQL, Flask, sessions, JS, HTML/CSS | API integration, aggregation, charts | fintech / data roles |
| Spaced-repetition app | algorithms, SQL dates, file I/O | algorithm-from-spec, `datetime` | backend / study tools |
| AI-as-tutor CLI | argparse, HTTP/JSON, file I/O | API auth, env security, prompt design | automation / LLM apps |
| Quant backtester | simulation logic, separation of concerns | event loops, Sharpe/drawdown | quant engineering |
| Ray tracer | recursion, arrays, math | linear algebra, visual debugging | graphics / math-heavy CS |

---

## 7. Common Pitfalls

- **Plagiarism / un-attributed AI code** → certificate revoked, even after completion. Staff actively audit submissions.
- **README under 750 words or vague** → automatic fail.
- **Silent video / no narration** → fails the video requirement.
- **Over-scoping** → can't finish → can't submit. Cut features ruthlessly to a working core.

---

## 8. Sources

| Item | Detail |
|---|---|
| Official project spec | https://cs50.harvard.edu/x/2026/project/ |
| Deadline | 2026-12-31T23:59:00+00:00 |
| Submit | `submit50 cs50/problems/2026/x/project` |
| Gallery of past projects | Browse the GitHub topic [`cs50-final-project`](https://github.com/topics/cs50-final-project) and the past-project links on the official [project spec page](https://cs50.harvard.edu/x/2026/project/) |
| Idea research | projects2jobs.ai CS50 final project ideas (2026-06-14) — third-party, treat as inspiration only |
