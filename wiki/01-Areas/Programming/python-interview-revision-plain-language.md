---
course_code: "PROGRAMMING"
course_name: "Programming & Software Engineering Field"
unit: "Python Interview Revision — Plain Language"
date: 2026-10-05
description: "Full Python revision in plain language for technical interviews - types, containers, functions, comprehensions, classes, exceptions, iterators, generators, decorators, modules, and the Python-specific traps, with runnable snippets and what to say out loud."
tags: [python, interview-prep, revision, simple-language]
last_updated: "2026-10-05"
confidence: high
---

## For future agent
Plain-language Python revision for the [[01-Areas/Engineering/nexus-robotics/INDEX|Nexus Robotics interview]] and any Python round. Same design rule as [[01-Areas/Programming/c-interview-revision-plain-language|the C revision]]: **plain words → runnable code → the trap.** Depth already exists elsewhere — [[01-Areas/Programming/languages-python-advanced]] (advanced + wtfpython), [[01-Areas/Programming/object-oriented-programming/overview|OOP library]], [[01-Areas/Programming/python-mastery-path]] (stage-gated path). Don't duplicate derivations here. Every snippet in this page was executed on CPython 3.13.

# Python Interview Revision — In Simple Language

> **How to use this:** read a section, **cover it, say it back in one or two sentences.** Every section ends with a trap, because the trap is usually the point of the question.

---

## 1. The shape of a Python program

```python
def main():
    print("Hello")

if __name__ == "__main__":
    main()
```

**Say it simply:** *"Python runs top to bottom. A `def` names a function. The `if __name__ == '__main__'` guard means 'only run this when the file is run directly, not when it's imported' — that's what makes a module safe to import."*

**Trap:** forgetting the guard. Importing the file then executes everything, which is a genuinely confusing bug for beginners.

---

## 2. Variables — no declaration needed

```python
age = 20
name = "Anirudh"
pi = 3.14
passed = True
nothing = None
```

**Say it simply:** *"Python figures out the type from the value. `None` is the 'no value' one — it's not `0` and not `False`, it's its own thing, which is why `if x:` on `None` is False."*

**Trap — the truthiness trap:**

```python
0        # False
0.0      # False
""       # False  ← empty string is falsy!
[]       # False  ← empty list is falsy!
{}       # False
None     # False
"0"      # True   ← string "zero" is truthy
```

*"Everything except `0`, empty collections, empty strings, and `None` is truthy."* Never write `if x:` to test for existence — use `if x is not None:`.

---

## 3. The four container types — know which is which

```python
my_list    = [1, 2, 3]        # ordered, changeable, duplicates OK
my_tuple   = (1, 2, 3)        # ordered, NOT changeable
my_set     = {1, 2, 3}        # NOT ordered, unique only, fast lookup
my_dict    = {"a": 1}         # key → value pairs, fast lookup by key
```

**Say it simply, this is the key sentence:** *"Lists are ordered and editable. Tuples are ordered but frozen — use them when the data shouldn't change, like a coordinate. Sets throw away duplicates and are fast to check membership. Dicts map keys to values and are how you count or look things up."*

**The membership test, and why it matters for speed:**

```python
item in my_list       # O(n) — walks the whole list
item in my_set        # O(1) — jumps straight to it
```

**Say it simply:** *"Checking whether something is in a list means looking at every element. In a set it's a direct lookup. That's why counting with a set beats a list when the data is large."*

**Trap:** sets lose order. `{3,1,2}` is not sorted. If you need sorted unique values: `sorted(set(x))`.

---

## 4. Indexing and slicing

```python
nums = [10, 20, 30, 40, 50]

nums[0]      # 10   — first (C and Python agree here)
nums[-1]     # 50   — last
nums[1:3]    # [20, 30]   — start INCLUSIVE, end EXCLUSIVE
nums[:]      # copy of the whole thing
nums[::-1]   # [50, 40, 30, 20, 10] — reversed
```

**Say it simply:** *"Counting starts at 0, like C. A colon means 'from here up to there' — and the end is **excluded**, so `nums[1:3]` gives you index 1 and 2, two items. Negative numbers count from the end."*

**Trap:** the exclusive end is the single most common Python off-by-one. `nums[0:5]` on a 5-element list gives all 5 (because the end 5 doesn't exist), but `nums[0:4]` gives only 4.

---

## 5. Making decisions

```python
if temp > 30:
    label = "Hot"
elif temp > 20:
    label = "Warm"
else:
    label = "Cool"
```

One-liner alternative:
```python
label = "Hot" if temp > 30 else "Cool"
```

**Say it simply:** *"`if` / `elif` / `else` works like C's `if` / `else if` / `else`. There's no semicolon and no braces — indentation defines the block. Python's `elif` is the cleaner spelling of C's `else if`."*

**Trap — the biggest Python bug:**

```python
if x = 5:      # WRONG — assigns, and 5 is truthy, so it always runs
if x == 5:     # RIGHT — compares
```

*Identical trap to C, and it's still the most common one. One `=` sets a variable; `==` asks a question.*

---

## 6. Loops

```python
for i in range(5):        # 0, 1, 2, 3, 4 — NOT 1 to 5
    print(i)

for name in ["a", "b"]:   # loop over anything iterable
    print(name)

i = 0
while i < 5:
    i += 1
```

**Say it simply:** *"`for` walks through a sequence one item at a time. `while` repeats as long as a condition holds. Python has no `do-while`, but `while True:` with a `break` covers it."*

**Loop control:**
```python
break      # leave the loop entirely
continue   # skip to the next iteration
else:      # runs if the loop finished WITHOUT break  ← C has no equivalent
    print("no break happened")
```

**The `else` is worth knowing** — it's a genuinely Pythonic way to say "this completed cleanly".

---

## 7. Functions

```python
def add(a, b):
    return a + b

def greet(name="friend"):     # default value
    return f"Hi {name}"

add(2, 3)        # 5
add(b=2, a=3)    # 5 — keyword arguments, order doesn't matter
```

**Say it simply:** *"`def` defines a function. Parameters can have defaults, and you can pass them by name so the order stops mattering. `return` hands a value back."*

**The `*args` / `**kwargs` pair:**

```python
def f(*args, **kwargs):
    print(args)     # (1, 2, 3)     — all extra positional args, as a tuple
    print(kwargs)   # {"a": 1}       — all extra keyword args, as a dict
```

**Say it simply:** *"`*args` collects any number of unnamed arguments into a tuple. `**kwargs` collects any named arguments into a dictionary. That's how functions like `print` and `max` accept anything."*

**Trap:** a function returns `None` if you forget `return`. Python doesn't warn you — the value just silently becomes `None`.

```python
def add(a, b):
    a + b            # BUG — computed and thrown away

x = add(2, 3)       # x is None, not 5
```

---

## 8. f-strings — string formatting

```python
name, score = "Asha", 9.5
print(f"{name} scored {score:.1f}")      # Asha scored 9.5
print(f"{42:05d}")                        # 00042  — pad to 5 digits
print(f"{3.14159:.2f}")                   # 3.14
```

**Say it simply:** *"An f before the string lets you drop values straight in with `{}`. A colon adds formatting — `.1f` is one decimal place, `05d` is zero-padded to five digits."*

---

## 9. List comprehensions — the Python idiom

```python
# Instead of this:
result = []
for x in range(10):
    if x % 2 == 0:
        result.append(x * x)

# Write this:
result = [x * x for x in range(10) if x % 2 == 0]
```

**Say it simply:** *"'Do this for each item, keep the ones that pass the test' — all in one line. Same for dicts and sets."*

```python
squares = {x: x * x for x in range(5)}        # dict comprehension
evens   = {x for x in range(10) if x % 2 == 0}  # set comprehension
```

**When to use:** once you already know the loop version. The rule in [[01-Areas/Programming/python-mastery-path]] is *"comprehension only when the loop version already works"* — a comprehension you have to think about is worse than a loop you can read.

**Trap:** nested loops in a comprehension become unreadable fast. Three levels deep is a `for` loop.

---

## 10. Classes

```python
class Robot:
    def __init__(self, name):
        self.name = name        # instance attribute
        self.battery = 100

    def move(self, distance):
        self.battery -= distance
        return f"{self.name} moved {distance}, battery {self.battery}%"

r = Robot("R2")
print(r.move(10))     # R2 moved 10, battery 90%
```

**Say it simply:** *"A class is a blueprint. `__init__` runs when you make an object and sets up its data. `self` means 'this particular object'. Methods are functions that live on the class."*

**Class vs instance — the distinction interviewers probe:**

```python
class Robot:
    count = 0                      # CLASS attribute — shared by all

    def __init__(self, name):
        self.name = name           # INSTANCE attribute — per object
```

**Say it simply:** *"A class attribute is shared by every instance; write to it through the class name. An instance attribute belongs to one object; write to it through `self`. A common bug is doing `self.count += 1`, which creates a new instance attribute shadowing the class one — and then `Robot.count` never changes."*

**Four OOP pillars in one line each:**

| Pillar | Plain meaning |
|--------|---------------|
| **Encapsulation** | hide the internals, expose methods |
| **Abstraction** | "do this" without knowing how |
| **Inheritance** | a child reuses the parent's behaviour |
| **Polymorphism** | different objects, same method name, different behaviour |

Deeper coverage: [[01-Areas/Programming/object-oriented-programming/overview|OOP library]].

**Duck typing — the Python way:** *"If it walks like a duck and quacks like a duck, it's a duck."* Python checks for the method at call time, not the type at definition time. That's why you don't need interfaces for simple cases.

---

## 11. Exceptions

```python
try:
    value = int(user_input)
except ValueError:
    print("that wasn't a number")
except (TypeError, KeyError) as e:
    print(f"something else went wrong: {e}")
else:
    print("it worked")
finally:
    print("this always runs")
```

**Say it simply:** *"`try` runs risky code. `except` catches specific errors. `else` runs if nothing broke. `finally` runs no matter what — that's where you close files and release resources."*

**Raising:**

```python
raise ValueError("temperature must be between 0 and 100")
```

**Trap — the bare `except`:** `except:` catches **everything**, including keyboard interrupts and typos. Always name the exception you expect.

**Trap:** catching an exception and doing nothing is worse than not catching it — it hides the bug. If you catch it, handle it or re-raise.

---

## 12. Reading and writing files

```python
with open("data.csv", newline="") as f:      # context manager
    for row in csv.DictReader(f):
        print(row["test"], row["thrust_g"])
```

**Say it simply:** *"`with open(...) as f` opens the file, gives you the handle, and **closes it automatically** when the block ends — even if your code crashes. Always use `with`. Plain `open`/`close` leaks the file handle if anything goes wrong."*

**Writing:**
```python
with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["test", "thrust_g"])
```

**Trap:** mode `"w"` **erases the file** if it already exists. `"a"` appends. Same trap as C's `fopen`.

---

## 13. `enumerate`, `zip`, and the `in` operator

```python
for i, value in enumerate(["a", "b"]):   # index AND value
    print(i, value)

for a, b in zip([1, 2], ["x", "y"]):      # pair up two sequences
    print(a, b)

"a" in "cat"        # True
2 in [1, 2, 3]      # True
```

**Say it simply:** *"`enumerate` gives you the position and the item together, so you never write a manual counter. `zip` walks two sequences side by side."*

---

## 14. Iterators and generators

```python
def count_up(n):
    for i in range(n):
        yield i          # each yield = one value, then pause

gen = count_up(3)
print(next(gen))   # 0
print(next(gen))   # 1
print(next(gen))   # 2
```

**Say it simply:** *"A generator is a function that pauses at `yield` and hands back one value, then resumes when you ask for the next. It produces items on demand instead of storing them all in a list — so a million-item generator uses no extra memory."*

**The `*` unpack trick:**
```python
data = [1, 2, 3, 4]
a, b, *rest = data     # a=1, b=2, rest=[3, 4]
```

**Say it simply:** *"The `*` collects everything left over into a list."*

---

## 15. Decorators — briefly

```python
import time

def timed(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        print(f"{fn.__name__} took {time.time()-start:.2f}s")
        return result
    return wrapper

@timed
def slow():
    time.sleep(1)
```

**Say it simply:** *"`@timed` is shorthand for `slow = timed(slow)`. The decorator takes my function, returns a wrapper that does extra work around it, and Python swaps them. It's how you add logging or timing to many functions without repeating yourself."*

**How it's built, so you can answer a follow-up:** *"A decorator is just a function that takes a function and returns a function. The `*args, **kwargs` in the wrapper is what lets it work on any signature — it forwards whatever arguments it was given."*

---

## 16. Modules and imports

```python
import math                  # use as math.sqrt(4)
from math import sqrt        # use as sqrt(4) — but risks name clashes
import numpy as np           # alias — the convention in science
```

**Say it simply:** *"`import math` gives you the whole module and you qualify names. `from math import sqrt` gives you just that function. The `as` alias keeps names short and avoids clashes."*

---

## 17. The traps, gathered

1. `=` vs `==` in an `if`.
2. Slices exclude the end index — `nums[0:5]` on 5 items is all 5, `nums[0:4]` is 4.
3. `range(5)` is 0 to 4, not 1 to 5.
4. Empty string and empty list are **falsy**.
5. Forgetting `return` silently gives you `None`.
6. `except:` with no name swallows everything.
7. `open(..., "w")` **erases** the file.
8. `self.count += 1` on a class attribute creates an instance attribute instead.
9. Mutating a list while looping over it skips elements.
10. `is` vs `==`: `is` checks identity, `==` checks value. Use `is None`, never `== None`.
11. Late-binding closures in loops — the classic gotcha where all lambdas print the same number.
12. Default arguments are evaluated **once**, not per call — a real source of very confusing bugs.

---

## 18. Side-by-side: the C habits that will bite you

Coming from C, these are the specific places your instincts are wrong.

| C habit | Python reality |
|---|---|
| Braces `{ }` define blocks | **Indentation** defines blocks |
| `int x = 5;` (semicolon, type) | `x = 5` (no type, no semicolon) |
| Index starts at 0 | Index starts at 0 ✓ (same) |
| Loop `i <= n` for n times | `range(n)` is n items — use `range(n)`, not `range(n+1)` |
| `#include <stdio.h>` | `import math` |
| Declare function before use | Define order doesn't matter at call time |
| `char name[20]` | `name = "..."` — Python strings handle length |
| Array index out of range = UB | Out-of-range index raises `IndexError` ✓ safer |
| Compile then run | Run directly ✓ |
| `NULL` | `None` |
| `argc/argv` | `sys.argv` |
| Struct for a record | Class, or a `dict`, or `dataclass` |

---

## 19. If they ask "why Python instead of C?"

Have a real answer ready:

> "I use Python when the bottleneck is iteration speed and the work is data-shaped — parsing, transforming, analysis. I reach for C when the bottleneck is the hardware: timing, memory, or a loop that must run every microsecond. In my telemetry parser I'd use Python because it's about understanding the data; on the robot itself it's C because the control loop has a deadline."

That answer is the whole lesson of [[01-Areas/Engineering/SPM/module-1-spm-c-basics]] and the Nexus drills at the same time.

---

## See also

- [[01-Areas/Programming/c-interview-revision-plain-language|Companion C revision]] — the same treatment for C
- [[01-Areas/Programming/languages-python-advanced|Advanced Python]] — generators, decorators, descriptors, GIL, wtfpython entries
- [[01-Areas/Programming/object-oriented-programming/overview|OOP library]] — pillars, dunders, patterns, interview Q&A
- [[01-Areas/Programming/python-mastery-path|Python mastery path]] — stage-gated learning with exit tests
- [[01-Areas/Programming/languages-polyglot|Languages polyglot]] — how Python and C differ as a pair
- [[01-Areas/Engineering/nexus-robotics/nexus-python-drills|Python live-coding drills]] — the applied version of this page