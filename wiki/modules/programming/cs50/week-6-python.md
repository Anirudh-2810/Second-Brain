---
module: "programming"
course: "CS50x — Introduction to Computer Science"
week: 6
topic: "Python — A Friendlier C, Re-Implementing the Course's Ideas"
tags: [programming, computer-science, cs50, harvard, python, interpreted, dynamic-typing, libraries, data-structures]
last_updated: "2026-08-11"
---

# Week 6 — Python

> **Goal of the week:** re-live the first six weeks in **Python** — dramatically less ceremony, no explicit pointers/`malloc`, automatic memory management — and prove the *ideas*, not the syntax, are what matter.
> **PSet 6:** re-implement Mario/Cash/Readability/Credit/Speller in Python + *DNA* (a bioinformatics pattern-match, list/dict/set showcase).

---

## 1. Compiled C → Interpreted Python

| C | Python |
|---|---|
| Must **compile** (`make` → machine code) before running | **Interpreted**: writes and runs immediately |
| Static types declared everywhere | **Dynamic typing** — `x = 5` then `x = "cats"` both legal (values carry types, not names) |
| You manage memory (`malloc`/`free`, pointers) | **Automatic memory management** (no pointers, garbage collected) |
| Runs close to the CPU → fast | Runs through a layer of interpretation → slower, but you barely notice on 99% of tasks |

**The mental `#include` equivalent:**
```python
import cs50          # ≈ #include <cs50.h>
print("hello")       # ≈ printf
```

**Why CS50 swaps languages mid-course:** every idea from Weeks 1–5 is implementable in Python with less risk, more speed, and the exact same complexity analysis — therefore the ideas were never about C.

---

## 2. Python as C-with-Ergonomics — Head-to-Head

| Concern | C | Python |
|---|---|---|
| Entry point | `int main(void)` | `if __name__ == "__main__":` (or just top-level code) |
| Output | `printf("hello, %s\n", name)` | `print(f"hello, {name}")` |
| Input | `get_string("...")` | `s = input("...")` / `cs50.get_string` |
| Block structure | braces `{}` | **indentation only** (matters! consistency is mandatory) |
| For loop | `for (int i=0;i<n;i++)` | `for i in range(n):` |
| Increment | `i++` | no operator — `i += 1` |
| Booleans | `true`/`false` | `True`/`False` |
| "and/or" | `&&`/`||`/`!` | `and`/`or`/`not` |
| Comments | `//` `/* */` | `#` |
| Library import | `#include <stdio.h>` | `import sys` / `from math import sqrt` |

```python
import cs50

name = cs50.get_string("What's your name? ")
print(f"hello, {name}")
```

---

## 3. Python's Data Structures ARE Week 5's Structures

| Python type | == Week 5 structure | Notes |
|---|---|---|
| `list` | growable array / linked list behavior | `append`, `insert`, `pop`, slicing `a[1:3]`, $O(1)$ tail append |
| `dict` | **hash table** | `price = {"bread": 3}`, `price["bread"]`, keys unique, `in` check fast |
| `set` | hash-set | unique, unordered, hash-based membership |
| `tuple` | immutable ordered group | `(x, y)` — like a struct that can't change |
| `str` | array of chars | immutable; `s[0]`, `s.upper()`, `len(s)` |

**The Week 2–5 payoff in one glance:**
```python
words = set()                       # speller
while True:
    word = input()
    if word.lower() in words:       # O(1) membership
        print("already seen")
    words.add(word.lower())
```

---

## 4. Python's Idiosyncrasies to Unlearn From C

- **No `main` required** — scripts run top-to-bottom; use functions anyway for readability.
- **No curly braces / semicolons.** Indentation = structure. **Mixed tabs+spaces = `IndentationError`.**
- **`//` integer division, `%` modulo**, `**` power. `int(x)`/`float(x)` conversions explicit.
- **`range(n)` gives 0…n−1**; `range(2, n)` starts at 2; `len()` methods.
- **Errors are *exceptions***: `try/except ValueError:` replaces C's checking of every input.
- **Everything is an object** — strings/lists have built-in methods (`s.strip().upper()`, `.append`); this is *abstraction at its most pleasant*.

---

## 5. Libraries — Programming "as Home Depot"

```python
from cs50 import get_string        # import specific pieces
import csv                          # flat-file helper → Week 7
import re                           # regexes
import random                       # random.randint(...)
from PIL import Image               # image work (like PSet 4's Filter in Python)
```
The course's stance mirrors [[programming-cs-fundamentals]] segment 14: import the **specific** pieces you need, not the whole universe.

---

## 6. DNA — The Case Study That Ties Everything

- *DNA* loads a CSV of "STR" (short tandem repeat) counts per person and a DNA sequence text.
- Workflow: read files (`csv`, `open().read()`), count the longest run of each STR in the sequence (scanning + lists/dicts), then look up the match in the dict.
- The sequence `AGATAGAT…` counting is *the Week 2 string-scan problem* wearing Python clothes; the person lookup is *Week 5's hash table*; the file IO is *Week 4's fopen/fread*.
- **Lesson: the course's ideas recur across languages — recognize them, don't re-memorize habits.**

---

## 7. When You'd *Still* Choose C (honest engineering)

- Realtime / embedded / OS code where microseconds and tiny memory matter.
- Huge-scale compute where interpreter overhead is dominant.
- Anywhere you must touch hardware or manage exact memory layout.
- Otherwise: **Python-first** is the productive default for ML and scripting — the exact judgment call of [[quant-toolkit-and-skills]] (NumPy/pandas on Python vs C++ for latency-critical paths).

## 8. Vocabulary to Master

- interpreted · dynamic typing · indentation-as-syntax · list / dict / set / tuple · slices `[start:stop]` · f-strings · `range` · exceptions / `try-except` · modules & `import` · GIL mention (interpreter speed)

## 9. Cross-Links

- [[cs50/week-8-html-css-javascript]] → [[cs50/week-9-flask]] — Python's `import` becomes web *apps*.
- [[cs50/week-7-sql]] — CSV flat files (this week) upgrade to a relational database.
- [[learn-python-fast-system]] — CS50 Python is literally Video 5's "best free intro"; this week is your head start.
- [[cs50/problem-sets]] — PSet 6 (re-implement + DNA).
- [[programming-cs-fundamentals]] — all of the abstract fundamentals now have a Python face, too.