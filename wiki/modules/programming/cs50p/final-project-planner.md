---
module: "programming"
course: "CS50P — Introduction to Programming with Python"
week: "final"
topic: "Final Project Planner — Terminal Task & Habit Tracker CLI Engine"
tags: [programming, python, cs50p, harvard, final-project, planner, blueprint, cli, task-tracker, pytest]
last_updated: "2026-08-19"
---

# CS50P Final Project Planner — Task & Habit Tracker CLI

> The corrected, verified blueprint for your **Terminal Task & Habit Tracker CLI Engine**. Requirements below are checked against the **official CS50P spec** (cs50.harvard.edu/python/2022/project/). Key differences from CS50x are flagged — do **not** reuse the CS50x rules for this course.

---

## 0. Verified CS50P essentials (differs from CS50x!)

| Item | The rule (exact for CS50P) |
|---|---|
| Language | **Must be Python.** |
| Core file | `project.py` in the **root** of `project/` with a `main()` function. |
| Functions | **3+ additional top-level functions** (same indent as `main`, not nested, not in a class). |
| Tests | `test_project.py` in root, tests named `test_<function>` for the custom functions, runnable with **`pytest`**. |
| Dependencies | **`requirements.txt` required** — list pip-installable libs one per line (your app is stdlib-only, but **put `pytest` in it**). |
| README | Named exactly `README.md` in `project/`; **multiple paragraphs, ~500 words** is the guideline; must include title + **video URL** + per-file description + design choices. |
| Video | ≤ **3 min**; opens with: title · name · GitHub + edX usernames · city & country · recording date. YouTube, **unlisted OK, never private.** |
| Deadline | **2026-12-31 23:59 UTC.** |
| Submit | `submit50 cs50/problems/2022/python/project` — **the slug is fixed at `2022`**, not per-year like CS50x. |
| Gradebook | Visit **cs50.me/cs50p** (not cs50x!) a few minutes after submitting → triggers certificate; claim it before the deadline. |
| AI | Allowed for the final project only; cite every use in code comments; staff audits submissions. |

**Video form:** https://forms.cs50.io/5e2dd8e8-3c8b-4eb2-b77d-085836253f26

---

## 1. Project spec (your idea, tightened)

**One-line spec:** For a student who uses the terminal, this CLI tracks tasks and daily habits and reports streaks + completion, better than a notebook.

**Deliverables:**

| File | Purpose |
|---|---|
| `project.py` | `main()` CLI menu + all custom functions |
| `test_project.py` | pytest tests for the custom functions |
| `data.json` | persistence (auto-created) |
| `requirements.txt` | **required** — content: `pytest` |
| `README.md` | writeup (~500 words) + video URL |

---

## 2. Data schema (`data.json`) — define this FIRST

```json
{
  "tasks": [
    {
      "id": 1,
      "title": "Study Physics",
      "due_date": "2026-08-25",
      "tag": "school",
      "completed": false,
      "completed_dates": ["2026-08-18", "2026-08-19"]
    }
  ]
}
```

- **Dates are ISO strings** `YYYY-MM-DD` everywhere (compare as strings — ISO sorts correctly!).
- `completed_dates` = the habit history that feeds `calculate_streak`.
- Auto-create `data.json` on first run (empty `{"tasks": []}`).

---

## 3. Custom functions — required three + recommended extras

### The three (meet the requirement)

**`parse_task_input(raw_text)` → dict**
- Regex: `^(.+?)\s*(?:@(\d{4}-\d{2}-\d{2}))?\s*(?:#(\w+))?$`
- `"Study Physics @2026-08-25 #school"` → `{"title": "Study Physics", "due_date": "2026-08-25", "tag": "school"}`
- Edge cases to handle: no date, no tag, extra spaces, invalid date format (raise `ValueError` or return `""` — pick one and test it).
- **Pure (no input()/print()) → perfectly testable.**

**`calculate_streak(history, today_str)` → int**
- `history = ["2026-08-18", "2026-08-19"]`, `today = "2026-08-19"` → `2`.
- Logic: dedupe + sort descending, count consecutive days ending at `today`. If `today` is absent but `yesterday` is present, count from yesterday (you just haven't logged today yet).
- Empty history → `0`.

**`calculate_completion_rate(tasks)` → float**
- `count(completed=True) / len(tasks) * 100`, rounded to 1 decimal (`66.7`).
- Empty list → `0.0` (do not divide by zero).

### Recommended extras (make the project meatier → better grade, more tests)

- `load_tasks(path)` / `save_tasks(tasks, path)` — JSON I/O; test with pytest's `tmp_path` fixture.
- `add_task(tasks, task)` — append + assign id; pure.
- `complete_task(tasks, task_id, today_str)` — mark completed + append today to `completed_dates`; pure.
- `show_dashboard(tasks, today_str)` — prints summary using the functions above (this one can print).

### Required structure (from the spec — copy exactly)

```python
def main():
    ...

def parse_task_input(raw_text):
    ...

def calculate_streak(history, today_str):
    ...

def calculate_completion_rate(tasks):
    ...


if __name__ == "__main__":
    main()
```

---

## 4. Test matrix (`test_project.py`)

| Function | Test cases |
|---|---|
| `parse_task_input` | full input · title only · tag only · date only · `@2026-8-5` invalid date → error · extra whitespace · tag with digits |
| `calculate_streak` | 2-day streak · empty list → 0 · today missing but yesterday present · gap in middle resets streak · duplicates in history · single date → 1 |
| `calculate_completion_rate` | all done → 100.0 · 2/3 → 66.7 · none → 0.0 · empty list → 0.0 |
| `load_tasks` / `save_tasks` | round-trip: save then load returns identical data (use `tmp_path`) · missing file → empty structure · corrupted JSON → handled gracefully |

> **Run:** `pytest` from `project/` — all tests must pass before you even think about the video.

---

## 5. Execution roadmap (5 phases, risk-first)

```
Phase 1  Setup & schema ........ data.json design + project/ + requirements.txt + git init
Phase 2  Core functions (TDD) .. write test FIRST, then function, watch it pass (parse_task_input
         │                       → calculate_streak → calculate_completion_rate)
Phase 3  CLI menu & persistence . main() loop + load_tasks/save_tasks/add_task/complete_task
         │                       wired together; app runs end-to-end from `python project.py`
Phase 4  Full unit testing ...... all 8+ test cases green under pytest
Phase 5  README + video + submit  ~500-word README, ≤3-min video, submit50, gradebook claim
```

**Daily rule:** end every day with a *running* app and all tests passing. Commit at every green point.

---

## 6. Submission — the exact steps (do all three before Dec 31, 2026)

1. **Video (≤3 min):** opening card with the six items → live demo: add a task, complete it, show streak + completion %. Upload (unlisted, not private) → submit the video form.
2. **README + submit:** from inside `project/`:
   ```
   submit50 cs50/problems/2022/python/project
   ```
   (GitHub login; password shows as asterisks.)
3. **Gradebook:** visit **cs50.me/cs50p**, claim the free certificate, confirm completion.

**Troubleshooting:** too large → ZIP contents except `README.md`, keep <100 MB, or drag-drop onto the `cs50/problems/2022/python/project` branch of `github.com/me50/<USERNAME>`.

---

## 7. Master checklist

- [ ] `project.py` has `main()` + ≥3 top-level functions + `if __name__ == "__main__"` guard
- [ ] `test_project.py` with `test_`-prefixed tests for each custom function
- [ ] All pytest tests pass
- [ ] `requirements.txt` exists (contains `pytest`)
- [ ] `data.json` auto-creates; schema matches section 2
- [ ] Edge cases handled (empty data, bad input, invalid dates, missing file)
- [ ] README ~500 words, includes video URL, per-file description, design choices
- [ ] Video ≤3 min with the 6-item opening card, unlisted
- [ ] Video form submitted
- [ ] `submit50 cs50/problems/2022/python/project` ran successfully
- [ ] **cs50.me/cs50p** loaded → certificate claimed → green banner ✅

---

## 8. Sources

| Item | Detail |
|---|---|
| Official CS50P spec | https://cs50.harvard.edu/python/2022/project/ |
| Video submission form | https://forms.cs50.io/5e2dd8e8-3c8b-4eb2-b77d-085836253f26 |
| Gradebook | https://cs50.me/cs50p |
| Deadline | 2026-12-31T23:59:00+00:00 |
| Gallery | https://cs50.harvard.edu/python/2022/gallery/ |

**Related:** [[cs50p/habit-tracker-build-blueprint|Habit Tracker Build Blueprint — day-by-day HOW-TO with code skeletons, TDD order and test matrix]] · [[cs50/final-project-planner|CS50x final project planner]] (different rules — don't mix them) · [[learn-python-fast-system|Python fast-track]] · [[programming/programming-cs-fundamentals|CS fundamentals]]