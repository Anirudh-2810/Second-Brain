---
course_code: "CAREERS"
course_name: "Careers, Market & Interview Prep"
unit: "Team DataZen Tech Prep (code + stats + SQL + ML)"
date: 2026-09-25
description: "DataZen tech spoke: cold-typable CSV/SQL patterns, survival pandas, stats and viz one-liners, ML/web/git basics with kid-simple analogies and grill answers."
tags: [careers, datazen, interview-prep, python, pandas, sql, statistics, ml]
last_updated: "2026-09-25"
confidence: high
relations:
  relates_to: "[[team-datazen-interview-prep]]"
---

## For future agent

Tech spoke of the DataZen interview package. Hub: [[team-datazen-interview-prep]]. Written beginner-first (owner asked kid-simple, 2026-09-25): every concept gets a one-line analogy, a tiny example, and the interview sentence. Same CSV-parser muscle as Onyx [[01-Areas/Engineering/aeromodelling/team-onyx-interview-mock-01]] Task 2. Deeper ML/math lives in [[01-Areas/AI-Data/INDEX|AI-Data hub]] — link there, don't copy it.

# Team DataZen Tech Prep

## 1. Python core (must type cold)

**Variables = labelled dabbas.** `name = "Anirudh"` puts a mango in dabba `name`. List = train compartments in order (`marks[0]` is seat 0). Dict = almirah with name tags (`{"fest": 120}`).

**Loop = attendance register.** Teacher reads each name one by one — `for r in rows` reads each CSV row one by one. Function = recipe card: ingredients in, dish out. `max(rows, key=...)` = "tallest boy stand up."

**The pattern (show-up rate + top-3 + bad-row report):**

```python
import csv

rows = list(csv.DictReader(open("events.csv")))
clean, bad = [], 0
for r in rows:
    try:
        reg, att = int(r["registrations"]), int(r["attended"])
        if reg == 0:
            bad += 1
            continue
        r["showup"] = att / reg
        clean.append(r)
    except:
        bad += 1
top3 = sorted(clean, key=lambda r: r["showup"], reverse=True)[:3]
print([(r["event"], round(r["showup"], 2)) for r in top3], "bad:", bad)
```

Say while typing: "CSV reads text, cast to int, guard zero, divide, rank, report bad rows." Complexity O(n) time. `dict.get("fee", 0)` = safe default. List comp: `[r for r in rows if r["showup"] > 0.5]`.

Fake-data check (hand first, always): fest 120/200 = 0.6, workshop 45/50 = **0.9 best**, talk 40/100 = 0.4, hack 60/80 = 0.75.

## 2. Survival pandas (5 verbs)

`read_csv, head/info, groupby, fillna, merge.` Same task, shorter:

```python
import pandas as pd
df = pd.read_csv("events.csv")
df["showup"] = df["attended"] / df["registrations"]
print(df.groupby("event")["showup"].mean().sort_values(ascending=False))
```

NaN rule: few rows → `dropna()`; many → `fillna(median)` + say why. Dupes: `drop_duplicates()`. Merge: `pd.merge(df1, df2, on="event", how="inner")` (inner = matches only). Lil advanced: `pivot_table(index="event", columns="month", values="showup", aggfunc="mean")`, `value_counts()`.

## 3. Survival SQL (write cold)

```sql
SELECT event, AVG(attended * 1.0 / registrations) AS showup
FROM events
GROUP BY event
ORDER BY showup DESC
LIMIT 3;
```

Clause order is the answer to "structure a query": SELECT → FROM → WHERE (rows, pre-group) → GROUP BY → HAVING (groups, post-group) → ORDER BY → LIMIT. `*1.0` avoids integer division. `COUNT(*)` counts rows, `COUNT(col)` skips nulls. JOIN: inner = matches only; left = all left rows + nulls on the missing side. Lil advanced: subquery — `SELECT * FROM (SELECT event, AVG(...) s FROM events GROUP BY event) WHERE s > 0.5`.

## 4. Stats (6 one-liners with kid logic)

- **Median beats mean with outliers.** Pocket money 10, 10, 10, 500 — mean 132 lies, median 10 tells truth.
- **Std = spread.** Same average, class A all 5'4", class B has 4'0" + 6'5".
- **Correlation ≠ causation.** Ice cream and drowning both rise in summer — heat causes both.
- **Overfitting = memorized answers.** Kid crams 10 sums, fails the 11th. Fix: hide half as surprise test (train/test split) + simpler model.
- **Missing values:** report the % first; few → drop, many → median fill + say why. Never silently drop.
- **Small n:** n=4 is directional only. "p-value = chance of seeing this gap if nothing real; <0.05 conventional bar" — and n=4 can never clear it.

## 5. Visualization + web + git

Trend = line (fever chart). Compare = bar (4 friends' heights). Relation = scatter (height vs weight dots). Spread = histogram (kids per height bucket). Pie beyond 3 slices = unreadable. Always title + labelled axes; bars start at 0 or you lie. Tool: "matplotlib/seaborn quick; Sheets if faster — chart serves the decision."

API = canteen counter: GET shouts "menu" and gets a JSON chit `{"item":"vada pav","price":20}`; POST hands an order in. 200 served, 404 no-such-item, 500 kitchen fire. Handle loading/error/empty. Git = save games: branch (alternate timeline) → commit (save point + note) → push (cloud) → pull (friend's save).

## 6. ML one-liners (don't bluff depth)

Regression predicts numbers ("how many will come? 60"). Classification predicts labels ("will Riya come? yes/no"). Features = clues, label = answer key. Accuracy for labels, MAE (average miss distance) for numbers. More clean features beats fancier model. AURA story: "past turnout + slot + fee as features, simple model, judged accuracy/MAE. Limits: small offline data, no live validation — the reps I want here."

## 7. Grill answers (verbatim)
- **Freeze:** "Logic first: load rows, cast text to int, divide, rank. Syntax in docs — steps don't change." Type anyway, narrating.
- **Why-chain:** "CSV text must become numbers; mean summarizes an event; groupby collapses rows to it; descending puts the winner first."
- **Dirty traps:** "Headers, types, NaN count, dupes, zero-reg guard; report bad-row % before dropping."
- **Depth probe:** "Beyond my current depth — I'd split-test and ask a senior. What I won't do is dress n=4 as proof."
- **AURA/stock-agent probe:** features > model, metric named, one limit admitted → "shallow ML depth today, council reps close it."
- **Live-task playbook:** restate → inspect → clean aloud → rank → 1 chart → 1 recommendation + 1 caveat. Offer follow-up: "scatter of turnout vs fee next."

## 8. Python basics bank (FY-complete)

- **Types:** int, float, str, bool. `type(5)` → int. Division `/` always float; `//` floors.
- **Strings:** `"fest".upper()`, f-string `f"{r['event']}: {r['showup']:.2f}"` (2 decimals).
- **List vs tuple vs set vs dict:** list ordered + changeable; tuple ordered + frozen (coordinates); set unordered + unique (seen-check for dupes); dict named tags.
- **Dupe check pattern:** `seen = set()` → `key = (r["event"], r["registrations"])` → skip if in seen.
- **Functions:** `def showup(att, reg): return att / reg if reg else 0` — guard lives inside.
- **Exceptions:** try the risky line (int cast, division), except counts bad rows. Never bare-crash a task.
- **File modes:** `"r"` read, `"w"` overwrite, `"a"` append. `with open(...) as f` auto-closes.
- **OOP one-liner (if asked):** "class bundles data + the functions that touch it; I use dataclasses for rows when dicts get messy."
- **Complexity:** single loop over n rows = O(n) time; the pattern above is O(n) time, O(n) space (stores rows).

## 9. SQL extended

- **All aggregates:** COUNT, SUM, AVG, MIN, MAX. `AVG(attended*1.0/registrations)` — ×1.0 avoids integer division.
- **NULL:** missing value, not zero. `WHERE fee IS NULL` (never `= NULL`). COUNT(col) skips nulls, COUNT(*) doesn't.
- **JOINs with 3-row tables (draw aloud):** students(id,name) × attendance(id,came). INNER = only ids in both. LEFT = all students + null where no record (finds no-shows!). RIGHT mirrors. FULL = everyone from both.
- **GROUP BY rule:** every non-aggregated SELECT column must be in GROUP BY.
- **Subquery:** inner query answers "rates per event," outer filters `WHERE s > 0.5`.
- **DISTINCT:** `SELECT DISTINCT event` dedupes. **LIKE:** `WHERE event LIKE 'work%'`.

## 10. Stats extended

- **Distribution shapes:** normal = bell (heights); right-skew = long tail right (incomes, one rich kid pulls mean up — report median).
- **Variance/std worked:** values 40,45,90 — mean 58.3, std ≈ 22. Std in same units as data; variance is its square.
- **Percentiles:** "90th percentile turnout = 90% of events did worse." Median = 50th percentile.
- **Sampling bias:** surveying only attendees about timing ("was the slot good?") misses everyone who skipped — the exact people whose answer matters.
- **A/B intuition:** split audience randomly, change ONE thing (reminder vs none), compare show-up rates, need enough n before claiming.
- **Sheets/Excel mirror:** `=B2/A2` rate, drag-fill, Data → PivotTable = no-code groupby, chart insert = viz answer when code isn't allowed.
