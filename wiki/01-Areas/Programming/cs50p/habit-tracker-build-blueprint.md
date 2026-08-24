---
module: "programming"
course: "CS50P — Introduction to Programming with Python"
week: "final"
topic: "Habit Tracker Build Blueprint — day-by-day plan, function specs, TDD, tests, submission"
tags: [programming, python, cs50p, final-project, blueprint, habit-tracker, cli, pytest, tdd]
last_updated: "2026-08-19"
---

# Habit Tracker CLI — Build Blueprint

> The hands-on, day-by-day plan for building your **Terminal Task & Habit Tracker** for CS50P. The [[cs50p/final-project-planner|planner]] covers rules + submission; this file is **how to actually write it** — function specs with code skeletons, TDD order, the test matrix, and an exit criterion for every day.
>
> Rule recap: Python · `project.py` with `main()` + ≥3 top-level functions · pytest tests in `test_project.py` · `requirements.txt` (`pytest`) · README ~500 words · submit `submit50 cs50/problems/2022/python/project` · gradebook `cs50.me/cs50p`.

---

## 0. What you're building

A terminal menu where you:

1. Add a task like `Study Physics @2026-08-25 #school`
2. List tasks
3. Complete a task (repeatedly = your habit history)
4. See a dashboard: current streak + completion %

Every change is saved to `data.json` immediately.

```bash
python project.py
```

---

## 1. Project structure

```text
project/
├── project.py          # main() + all functions
├── test_project.py     # pytest tests
├── requirements.txt    # contains: pytest
├── README.md           # ~500-word writeup + video URL
└── data.json           # auto-created on first run
```

---

## 2. Data model (`data.json`)

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

**Rules:**
- ISO dates `YYYY-MM-DD` everywhere (string comparison sorts correctly).
- `completed_dates` = the habit history that feeds the streak.
- Missing file / corrupted JSON → start with `{"tasks": []}` (never crash).

---

## 3. Function specs (code skeletons)

> All functions except `display_tasks`/`main` are **pure** (no `input()`/`print()`) → testable. Copy these as your starting point.

### 3.1 `parse_task_input(raw_text)` → dict

```python
import re
from datetime import date, datetime, timedelta

def parse_task_input(raw_text):
    raw_text = raw_text.strip()
    match = re.match(r"^(.+?)\s*(?:@(\d{4}-\d{2}-\d{2}))?\s*(?:#(\w+))?$", raw_text)
    if not match:
        raise ValueError("Invalid task format")
    title = match.group(1).strip()
    due_date = match.group(2) or ""
    tag = match.group(3) or ""
    if not title:
        raise ValueError("Task title required")
    if due_date:
        datetime.strptime(due_date, "%Y-%m-%d")   # raises on bad date like 2026-13-40
    return {"title": title, "due_date": due_date, "tag": tag}
```

| Input | Output |
|---|---|
| `Study Physics @2026-08-25 #school` | `{"title": "Study Physics", "due_date": "2026-08-25", "tag": "school"}` |
| `Buy milk` | `{"title": "Buy milk", "due_date": "", "tag": ""}` |
| `Meditate #health` | `{"title": "Meditate", "due_date": "", "tag": "health"}` |
| `Bad @2026-13-40` | raises `ValueError` |

### 3.2 `calculate_streak(history, today_str)` → int

```python
def calculate_streak(history, today_str):
    unique = sorted(set(history), reverse=True)
    if not unique:
        return 0
    expected = datetime.strptime(today_str, "%Y-%m-%d").date()
    if unique[0] != today_str:            # today not logged yet → start from yesterday
        expected -= timedelta(days=1)
    streak = 0
    for day in unique:
        if day == expected.isoformat():
            streak += 1
            expected -= timedelta(days=1)
        else:
            break
    return streak
```

| Input | Output |
|---|---|
| `["2026-08-18","2026-08-19"]`, today `2026-08-19` | `2` |
| `[]`, any today | `0` |
| `["2026-08-18"]`, today `2026-08-19` | `1` (today not logged, start yesterday) |
| `["2026-08-15","2026-08-19"]`, today `2026-08-19` | `1` (gap resets) |
| `["2026-08-18","2026-08-18","2026-08-19"]`, today `2026-08-19` | `2` (dupes deduped) |

### 3.3 `calculate_completion_rate(tasks)` → float

```python
def calculate_completion_rate(tasks):
    if not tasks:
        return 0.0
    done = sum(1 for t in tasks if t.get("completed"))
    return round(done / len(tasks) * 100, 1)
```

| Input | Output |
|---|---|
| 3 tasks, 2 done | `66.7` |
| 0 tasks | `0.0` (no divide-by-zero) |
| 3 tasks, 0 done | `0.0` |
| 2 tasks, 2 done | `100.0` |

### 3.4 Persistence

```python
import json

def load_tasks(path="data.json"):
    try:
        with open(path, "r") as f:
            return json.load(f)["tasks"]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks, path="data.json"):
    with open(path, "w") as f:
        json.dump({"tasks": tasks}, f, indent=2)
```

### 3.5 Mutations (pure)

```python
def add_task(tasks, task):
    task["id"] = max((t.get("id", 0) for t in tasks), default=0) + 1
    task["completed"] = False
    task["completed_dates"] = []
    tasks.append(task)
    return tasks

def complete_task(tasks, task_id, today_str):
    for t in tasks:
        if t.get("id") == task_id:
            t["completed"] = True
            if today_str not in t["completed_dates"]:
                t["completed_dates"].append(today_str)
            return tasks
    raise ValueError(f"No task with id {task_id}")
```

### 3.6 The CLI (`main()`) — the only place with `input()`/`print()`

```python
def display_tasks(tasks):
    for t in tasks:
        status = "[x]" if t.get("completed") else "[ ]"
        print(f"  {t['id']}. {status} {t['title']}  @{t['due_date'] or '----'}  #{t['tag'] or '-'}")

def main():
    tasks = load_tasks()
    while True:
        print("\n=== HABIT TRACKER ===")
        print("1. Add task   2. List   3. Complete   4. Dashboard   5. Exit")
        choice = input("> ").strip()
        if choice == "1":
            raw = input("Task (Title @YYYY-MM-DD #tag): ")
            try:
                tasks = add_task(tasks, parse_task_input(raw))
                save_tasks(tasks)
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "2":
            display_tasks(tasks)
        elif choice == "3":
            display_tasks(tasks)
            try:
                tasks = complete_task(tasks, int(input("Task id: ")), date.today().isoformat())
                save_tasks(tasks)
                print("Completed!")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "4":
            today = date.today().isoformat()
            history = [d for t in tasks for d in t.get("completed_dates", [])]
            print(f"Streak: {calculate_streak(history, today)} days")
            print(f"Completion: {calculate_completion_rate(tasks)}%")
        elif choice == "5":
            print("Saved. Goodbye!")
            break
        else:
            print("Pick 1-5.")

if __name__ == "__main__":
    main()
```

---

## 4. Day-by-day plan (TDD — test first, watch it fail, then make it pass)

> Commit after every green point. End every day with a running app.

### Day 1 — Setup & skeleton (exit: `python project.py` opens the menu)
- Create `project/`, `git init`, write `requirements.txt` (`pytest`).
- Write `project.py` with the exact structure: `main()` + empty stubs for the 8 functions + `if __name__ == "__main__"` guard.
- Draw the `data.json` schema (section 2).

### Day 2 — `parse_task_input` (exit: its tests pass)
- Write `test_parse_task_input.py` tests first (title only / full / date-only / tag-only / bad date / empty).
- Implement, run `pytest` until green.

### Day 3 — `calculate_streak` (exit: its tests pass)
- Tests: 2-day streak, empty → 0, yesterday-start, gap reset, duplicates.
- Implement, run `pytest` until green.

### Day 4 — `calculate_completion_rate` + persistence (exit: those tests pass)
- Tests: 66.7%, 0.0% empty, 100.0%; `load_tasks` round-trip via `tmp_path`, missing file → `[]`, corrupted JSON → `[]`.
- Implement, run `pytest` until green.

### Day 5 — CLI wiring (exit: full manual runthrough works)
- Implement `add_task` / `complete_task` / `display_tasks` / `main` from 3.5–3.6.
- Manual smoke test: add → list → complete → dashboard → exit → relaunch → data persists.

### Day 6 — Harden (exit: `pytest` green + no crash on junk input)
- Edge cases: duplicate completion (no double-count), `0` as task id, empty input, weird tags.
- Run the full `pytest` suite. Fix any bug found.

### Day 7 — README + video + submit (exit: certificate claimed)
- README (~500 words): what/why, how to run, file-by-file breakdown, design choices, video URL.
- 3-min video: opening card → `python project.py` demo → close.
- Video form → `submit50 cs50/problems/2022/python/project` → claim on `cs50.me/cs50p`.

---

## 5. Test matrix (full list for `test_project.py`)

| Function | Cases |
|---|---|
| `parse_task_input` | full input · title only · date only · tag only · bad date raises · empty raises · extra whitespace |
| `calculate_streak` | 2-day · empty → 0 · today missing, yesterday present → starts at 1 · gap resets · duplicates dedupe |
| `calculate_completion_rate` | 66.7 · 100.0 · 0.0 · empty → 0.0 |
| `load_tasks` | round-trip (save→load identical) · missing file → `[]` · corrupted JSON → `[]` |
| `save_tasks` | writes `{"tasks": [...]}` to `tmp_path` |
| `add_task` | assigns next id · sets completed=False · appends |
| `complete_task` | marks done · appends today once (no dupes) · unknown id raises |

---

## 6. Exit criteria (definition of done)

- [ ] `pytest` in `project/` → all tests pass
- [ ] `python project.py` runs the full menu without errors
- [ ] Data survives relaunch (add, exit, reopen, task still there)
- [ ] Junk input never crashes the app (errors are caught with a friendly message)
- [ ] `requirements.txt` exists
- [ ] README ~500 words with video URL
- [ ] Video ≤3 min, unlisted, with the 6-item opening card
- [ ] `submit50 cs50/problems/2022/python/project` ran → green banner on `cs50.me/cs50p`

---

## 7. Gotchas

- **Never use `input()` inside the tested functions** — `main()` only.
- Keep function signatures **exactly** as in section 3 so the tests in this blueprint match.
- `submit50` prompts for a GitHub password (shows asterisks) — not a bug.
- If you added a 9th function, add its `test_` too — every custom function the spec sees should be tested.
- Commit often: `git add . && git commit -m "day N: ..."` after every green point.

**Related:** [[cs50p/final-project-planner|CS50P planner (rules + submission)]] · [[cs50/final-project-planner|CS50x planner]] · [[c-programming/index|C notes]] · [[01-Areas/Programming/overview|Programming module]]