---
module: "SPM"
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
topic: "Module 2: Program Control Functions — Decisions, Loops & Jump Statements in C"
date: "2026-10-02"
description: "SPM Module 2 (6 hrs, CO2) — if/else ladder vs switch, the three loops compared, for-step semantics, nested loops, jump statements, plus the flag concept, counting loops, documentation rules and per-iteration trace tables (syllabus 2.2-2.3), with 6 worked exam problems."
tags: [spm, c-programming, control-flow, if-else, switch-case, fall-through, while, do-while, for-loop, nested-loops, break, continue, goto, return, flag-concept, counting-loops, documentation, operator-precedence, off-by-one, loop-invariant, 316U06C107, exam-prep]
last_updated: "2026-10-02"
confidence: high
prerequisites: ["Module 1: SPM & C Basics", "Relational & Logical Operators", "Operator Precedence"]
---

## For future agent

Theory + exam drills for SPM Module 2 (6 hrs, CO2). Sections 1.7–1.10 were added 2026-10-02 from the faculty handout `raw-sources/SPM Lecture/UnitNo. 2 Program Control Functions.pdf` (14 pp, AY 2026-27) to close three **syllabus gaps**: the handout covers "Flag Concept" and "Counting Loops" (both named in syllabus 2.2) and "Documentation and Making Source Code Readable" (syllabus 2.3), none of which had a section here before. The per-iteration trace tables in §1.10 are the handout's distinctive pedagogical format and match how OST predict-output questions are written.

Deep companion: [[spm-module2-faculty-companion]] (M2 PPT deltas). Loops used by Module 3: [[module-3-arrays]] · [[module-3-strings]].

# Module 2: Program Control Functions

> The decision-making engine of C: conditional branching (`if`/`else`/`switch` with its notorious fall-through), all three loop constructs with their exact execution semantics, and the jump statements `break`, `continue`, `goto`, `return`. This is the highest-yield output-prediction module in the syllabus — examiners love nested loops and `switch` without `break`. Written for beginners: each construct has a plain-English explanation, a flowchart, and a "when would I use this?" note.

---

## Table of Contents

1. [Conceptual Architecture & ASCII Flowcharts](#1-conceptual-architecture--ascii-flowcharts)
2. [Code Implementation & Memory Analysis](#2-code-implementation--memory-analysis)
3. [High-Yield Exam Problems & Worked Code Drills](#3-high-yield-exam-problems--worked-code-drills)
4. [Real-World System Applications](#4-real-world-system-applications)
5. [Appendix: Formula & Data Quick Reference](#appendix-formula--data-quick-reference)

---

## 1. CONCEPTUAL ARCHITECTURE & ASCII FLOWCHARTS

### 1.0 Truth in C — The Foundation Every Decision Sits On

Before any `if` or loop, fix one rule:

- In C, an integer expression is **true** if it is **non-zero**, and **false** if it is **zero**.
- Comparisons (`==`, `!=`, `<`, `>`, `<=`, `>=`) always evaluate to `1` (true) or `0` (false).
- So `if (x)` means "if x is non-zero", and `if (!x)` means "if x is zero".
- **Beginner trap:** `=` (assignment) vs. `==` (comparison). `if (x = 5)` *assigns* 5 to x and the condition is true (5 non-zero) — the #1 C bug. The "safe" style is `if (5 == x)` (Yoda condition) so a typo (`=`) fails to compile.

**Operator precedence quick table (highest → lowest) for conditions:**

| Precedence | Operators | Example meaning |
|---|---|---|
| 1 (highest) | `()` `[]` `.` `->` | grouping / indexing |
| 2 | `!` `-` `++` `--` `*` `&` (unary) | negation, address-of, dereference |
| 3 | `*` `/` `%` | multiply, divide, modulo |
| 4 | `+` `-` | add, subtract |
| 5 | `<` `<=` `>` `>=` | relational |
| 6 | `==` `!=` | equality |
| 7 | `&&` | logical AND (short-circuit) |
| 8 (lowest) | `\|\|` | logical OR (short-circuit) |

**Beginner rule:** when unsure, add parentheses — `if ((a > b) && (c < d))`. Clarity beats cleverness in exams.

### 1.1 Decision Statements — Decision Tree

```
                       if (condition)
                            │
              ┌─────────────┴─────────────┐
        TRUE  ▼                           ▼ FALSE
        ┌─────────────┐          ┌──────────────────┐
        │  if-body    │          │  else-body (if   │
        │  executes   │          │  present)        │
        └──────┬──────┘          └────────┬─────────┘
               │                          │
               └──────────┬───────────────┘
                          ▼
                 next statement (executed in all paths)
```

**Syntax rules (memorize):**
- `if (expr)` — expr non-zero = true, zero = false.
- **One** statement needs no braces; **multiple** statements *require* braces. Always brace — it prevents the classic "only the first statement was guarded" bug.
- `else` binds to the **nearest unmatched** `if` (the **dangling-else** problem). See the trap below.
- `switch(expr)` accepts **integral** values only (int, char, enum — no floats, no strings).
- `case` labels must be **compile-time constants**, unique, integral.
- **Fall-through:** if a case has no `break`, execution *falls into* the next case. Deliberately used sometimes (shared code), but usually a bug.
- `default` is optional; runs when no case matches.

**The dangling-else trap (classic exam question):**

```c
if (a)          /* which if does this else belong to? */
    if (b) printf("A");
else            /* belongs to the INNER if (b), not if (a) */
    printf("B");
```

The `else` pairs with the **nearest** unmatched `if` (the inner one). To make it pair with the outer `if`, brace the inner:

```c
if (a)
{
    if (b) printf("A");
}
else            /* now correctly pairs with if (a) */
    printf("B");
```

### 1.2 switch vs. if-else — What Each Is For

| Criterion | `if-else` ladder | `switch` |
|---|---|---|
| Condition type | Any expression (comparisons, ranges, boolean logic) | **Integral constant** equality only |
| Ranges possible? | Yes (`if (x >= 60 && x < 70)`) | No — each case is one exact value |
| Compiler optimization | Usually a series of compares | Often a **jump table** (O(1) dispatch) |
| Fall-through risk | None | **Yes** — forgetting `break` is the bug |
| Readability | Good for 2–4 branches | Better for many discrete values (menus, opcodes) |
| Default | `else` | `default:` |

**Beginner rule of thumb:** many distinct *exact* values → `switch`; ranges or logical combinations → `if-else`.

### 1.3 while vs. do-while vs. for — Comparison Table

| Feature | `while` | `do-while` | `for` |
|---|---|---|---|
| **Test timing** | Entry-controlled (test at top) | Exit-controlled (test at bottom) | Entry-controlled |
| **Minimum executions** | 0 | **1** (guaranteed) | 0 |
| **Syntax** | `while(cond){...}` | `do{...}while(cond);` | `for(init;cond;update){...}` |
| **Semicolon after** | no | **yes** (after `while(cond);`) | no |
| **Use case** | unknown iteration count (read until EOF, wait for flag) | must-run-once loops (menu, input validation) | known count / counter loops |
| **Counter scope** | manual | manual | counter in `init` (C99: block-scoped) |

### 1.4 for-Loop Execution — Step Sequence (Exact Semantics)

```
   for ( init ; condition ; update )  { body }
        │            │                  │
        ▼            ▼                  ▼
   STEP 1: init           (runs ONCE, before the first test)
   STEP 2: test condition
        │
     TRUE  ────────────►  STEP 3: execute body
        │                          │
        │                          ▼
        │                   STEP 4: update expression
        │                          │
        │                          ▼
        └──────────────   back to STEP 2 (re-test)
     FALSE
        │
        ▼
   exit loop, continue after the loop
```

**Beginner walkthrough for `for (i = 0; i < 3; i++)`:**
1. `i = 0` (once).
2. Test `0 < 3` → true → run body with i=0.
3. `i++` → i=1 → test `1 < 3` → true → body with i=1.
4. `i++` → i=2 → test `2 < 3` → true → body with i=2.
5. `i++` → i=3 → test `3 < 3` → **false** → exit.
Body runs **3 times**, with i = 0, 1, 2. This "zero-to-n−1" pattern is the standard.

**Beginner traps:**
- **Off-by-one:** `i < n` gives n iterations (0..n−1); `i <= n` gives n+1 (0..n). Decide once and be consistent.
- **Empty condition:** `for(;;)` is an infinite loop — equivalent to `while(1)`.
- **Semicolon after `for(...)`: `for(i=0;i<n;i++);` loops do *nothing* (empty body).** A silent classic.

### 1.5 Nested Loops — Pattern & Flow

```
   for(i=0; i<n; i++)               outer loop
     {
       for(j=0; j<m; j++)           inner loop — runs to COMPLETION
         { ... }                    for EACH single outer iteration
     }

   Execution count: inner body runs n × m times → O(n·m)

   Triangular pattern (inner bound uses outer variable):
   for(i=1;i<=3;i++){ for(j=1;j<=i;j++) printf("*"); printf("\n"); }
     i=1: *        i=2: **        i=3: ***
```

**Exam trap:** when the inner condition references the **outer** loop variable (`j <= i`), the inner body count is **triangular**: 1 + 2 + 3 = n(n+1)/2 iterations, not n².

### 1.6 Jump Statements — Decision Tree

```
   ┌────────────┐   ┌──────────────┐   ┌─────────────┐   ┌────────────┐
   │ break      │   │ continue     │   │ goto        │   │ return     │
   │ exits the  │   │ skips REST of│   │ jumps to a  │   │ exits the  │
   │ current    │   │ current loop │   │ labelled    │   │ function,  │
   │ loop/switch│   │ iteration,   │   │ statement   │   │ optionally │
   │ entirely   │   │ re-tests cond│   │ (within same│   │ returns a  │
   │            │   │              │   │ function)   │   │ value      │
   └────────────┘   └──────────────┘   └─────────────┘   └────────────┘
```

**Rules (memorize):**
- `break` is legal only inside `while`/`do`/`for`/`switch` — never in a bare `if`.
- `continue` is legal only inside loops. In a `for` loop, `continue` jumps to the **update** step first, then re-tests; in `while`/`do-while` it jumps straight to the condition test. **This distinction is a favourite exam question.**
- `goto label;` jumps to `label:` anywhere *in the same function*. Cannot jump *into* the middle of another function's scope. Discouraged (spaghetti code) but survives in Linux kernel/driver error-cleanup.
- `return expr;` exits the current function and hands `expr` back; `return;` in a `void` function just exits.
- `return 0;` from `main` = success status to the OS.

**Where does `continue` go in each loop type?**

```
   while (cond) { ... continue; ... }     → jumps back to "cond"
   do { ... continue; ... } while (cond); → jumps back to "cond"
   for (i; cond; update) { ... continue; ... }  → jumps to "update", then cond
```

### 1.7 The Flag Concept (syllabus 2.2) — NEW 2026-10-02

*A flag is a variable that records whether something has happened yet.* It is the standard way to carry information **out** of a loop, because a loop cannot `return` from inside itself.

**The two values, memorise the convention:**

| Value | Means |
|---|---|
| `0` | False / not found / no |
| `1` | True / found / yes |

**Worked example — "check whether 5 exists in an array":**

```c
int arr[5] = {2, 4, 5, 8, 10};
int i;
int flag = 0;                 /* assume NOT found */

for (i = 0; i < 5; i++) {
    if (arr[i] == 5) {
        flag = 1;             /* found it — flip the flag */
        break;
    }
}

if (flag == 1)
    printf("Number found");
else
    printf("Number not found");
```

**The pattern in words:** initialise the flag to the *negative* answer, set it inside the loop when the event occurs, and test it **after** the loop. Because `break` jumps out of the loop, an `if/else` attached directly to the inner `if` would never be reached — this is exactly why the flag exists.

**Three places you will use it:**

1. **Search** — `found = 0` → set to 1 on a match. (`-1` used as a *sentinel* instead of a flag is the array-module variant — see [[module-3-arrays]] §1.7.)
2. **Counting loop** — `count = 0` before, `count++` inside. (Also how `myStrlen` works — see [[module-3-strings]] §3.1.)
3. **Input validation** — `error = 1` on bad input, re-prompt while `error == 1`.

**Common variants (all accepted):** `flag = 0/1` · `found = 0/1` · `success = 0/1` · `isValid = 0/1` · `count = 0`.

### 1.8 Counting Loops (syllabus 2.2) — NEW 2026-10-02

*A counting loop repeats a specific, known number of times.* It is the `for` loop in its purest form — three named parts:

| Part | Example | Job |
|---|---|---|
| **Starting value** | `i = 1` | set once, before the loop |
| **Condition** | `i <= 10` | tested before every iteration |
| **Increment** | `i++` | one step per iteration |

```c
for (i = 1; i <= 10; i++)
    printf("%d\n", i);
```

That loop runs **exactly 10 times** (i = 1 … 10). To run *n* times, count to `n`.

**A worked sum, with the running total shown — good exam form:**

```c
int i, sum = 0;
for (i = 1; i <= 5; i++) {
    sum = sum + i;
}
printf("Sum = %d", sum);
```

| i | sum before | add | sum after |
|---|---|---|---|
| 1 | 0 | 1 | 1 |
| 2 | 1 | 2 | 3 |
| 3 | 3 | 3 | 6 |
| 4 | 6 | 4 | 10 |
| 5 | 10 | 5 | **15** |

`sum` is declared and zeroed **before** the loop. Declaring it inside would reset it every iteration — a classic beginner bug.

### 1.9 Documentation and Making Source Code Readable (syllabus 2.3) — NEW 2026-10-02

*Documentation means adding information that explains the program.* Its readers are the programmer, other students, teachers, and whoever maintains the code later. The most common tool is **comments**.

**A. Single-line comment** — `//` to end of line:

```c
#include <stdio.h>

int main() {
    int a, b, sum;

    // Accept two numbers
    scanf("%d %d", &a, &b);

    // Calculate the sum
    sum = a + b;

    // Display the result
    printf("Sum = %d", sum);

    return 0;
}
```

**B. Multi-line comment** — `/* ... */`:

```c
/*
   This program accepts
   two numbers and
   calculates their sum.
*/
```

**Note:** `//` is C99 and later. In older C (and C++) only `/* */` is standard — which is why you see both styles in the lab sheets.

**Four rules for readable code (memorise — this is also a lab CA rubric item):**

| # | Rule | Bad | Good |
|---|---|---|---|
| 1 | **Meaningful variable names** | `int a, b, c;` | `int marks, total, average;` |
| 2 | **Proper indentation** | `if(a>b){ printf("A is greater"); }` | braces on their own lines, body indented |
| 3 | **Add comments** | `average = total / 3;` | `// Calculate average marks` |
| 4 | **Proper output messages** | `printf("%d", sum);` | `printf("Sum = %d", sum);` |

Rule 1 is the one examiners probe: C accepts `a`, `b`, `x`, `tm` and `totalMarks` equally, so the compiler cannot help you — readability is entirely a discipline you must apply yourself.

**Related:** documentation is a scored element of the lab write-up (see [[lab-ca-and-experiments]]) and an examinable unit in its own right (2.3), so answer it as theory, not as a coding detail.

### 1.10 Per-iteration trace tables (faculty handout format) — NEW 2026-10-02

The handout `UnitNo. 2 Program Control Functions.pdf` presents loops as **trace tables** rather than prose. This is the format OST predict-output questions use, and it is the fastest way to check your own understanding.

**`for` loop — `for (i = 1; i <= 5; i++) printf("Hello\n");`**

The handout's master sequence: **Initialize → Check → Execute → Increment → … → Stop.**

| Step | Value of `i` | Condition `i <= 5` | Action |
|---|---|---|---|
| 1 | 1 | 1 <= 5 → TRUE | Print Hello |
| 2 | 2 | TRUE | Print Hello |
| 3 | 3 | TRUE | Print Hello |
| 4 | 4 | TRUE | Print Hello |
| 5 | 5 | TRUE | Print Hello |
| 6 | 6 | 6 <= 5 → FALSE | **Stop** |

**`while` loop — `i = 1; while (i <= 5) { printf("%d", i); i++; }`**

| Iteration | Value of `i` | Condition | `printf()` | After `i++` |
|---|---|---|---|---|
| 1 | 1 | TRUE | 1 | 2 |
| 2 | 2 | TRUE | 2 | 3 |
| 3 | 3 | TRUE | 3 | 4 |
| 4 | 4 | TRUE | 4 | 5 |
| 5 | 5 | TRUE | 5 | 6 |
| 6 | 6 | FALSE | — | Stop |

**`do-while` loop — `i = 1; do { printf("%d", i); i++; } while (i <= 5);`**

| Iteration | Value of `i` | Printed | After `i++` | Condition |
|---|---|---|---|---|
| 1 | 1 | 1 | 2 | TRUE |
| 2 | 2 | 2 | 3 | TRUE |
| 3 | 3 | 3 | 4 | TRUE |
| 4 | 4 | 4 | 5 | TRUE |
| 5 | 5 | 5 | 6 | TRUE |
| 6 | 6 | 6 | 7 | FALSE → **STOP** |

**Read the last row carefully — that is the whole point of `do-while`.** The body printed `6`, and the loop only *then* discovered the condition was false. A `while` loop with the same condition would have stopped at 5. The tables above are why "minimum executions" is 1 for `do-while` and 0 for the other two (§1.3).

---

## 2. CODE IMPLEMENTATION & MEMORY ANALYSIS

### 2.1 if-else ladder + switch — Production Example

```c
#include <stdio.h>

int main(void)
{
    int grade;
    printf("Enter grade (0-100): ");
    if (scanf("%d", &grade) != 1)   /* check input succeeded */
    {
        printf("Bad input\n");
        return 1;                   /* non-zero = error exit */
    }

    /* if-else ladder over ranges */
    if (grade >= 90)      printf("A\n");
    else if (grade >= 80) printf("B\n");
    else if (grade >= 70) printf("C\n");
    else if (grade >= 60) printf("D\n");
    else                  printf("F\n");

    /* switch over exact values — fall-through DEMO (deliberate, no breaks) */
    int day = 3;
    switch (day)
    {
        case 1: printf("Monday ");
        case 2: printf("Tuesday ");
        case 3: printf("Wednesday ");
        case 4: printf("Thursday ");
        case 5: printf("Friday ");
                break;               /* stops the fall-through chain */
        default: printf("Weekend\n");
    }
    printf("\n");
    return 0;
}
```

**Output for day = 3 (fall-through!):**
```
Wednesday Thursday Friday
```

**Why that output:** `case 3` matches, prints "Wednesday", and — because there is **no `break`** — execution falls through to `case 4` (prints "Thursday") then `case 5` (prints "Friday") and *finally* hits the `break`. Classic fall-through demonstration.

**Memory analysis:** `grade` and `day` are stack locals in `main`'s frame; no heap, no dynamic memory — the whole program uses stack + text segments only.

### 2.2 Loops — Prime Check with break (Early Exit)

```c
#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    int n, i;
    bool isPrime = true;
    printf("Enter n: ");
    if (scanf("%d", &n) != 1) return 1;

    if (n < 2) isPrime = false;
    for (i = 2; i * i <= n; i++)    /* test divisors only up to sqrt(n) */
    {
        if (n % i == 0)
        {
            isPrime = false;
            break;                  /* found a factor — no need to keep going */
        }
    }
    printf("%d is %s\n", n, isPrime ? "prime" : "not prime");
    return 0;
}
```

**Beginner explanation of `i * i <= n`:** if n has any divisor, it has one ≤ √n (because divisors come in pairs p × q = n; the smaller of the pair is ≤ √n). So we only test up to √n. Complexity: **O(√n)** worst case; the `break` gives early exit for composites.

### 2.3 do-while — Menu Loop (Guaranteed One Execution)

```c
#include <stdio.h>

int main(void)
{
    int choice;
    do
    {
        printf("\n1) Start  2) Stop  3) Quit\n> ");
        scanf("%d", &choice);
        /* act on choice ... */
    } while (choice != 3);
    printf("Exiting.\n");
    return 0;
}
```

**Why do-while:** the menu must appear at least once *before* any choice exists. An entry-controlled `while` would require awkward pre-initialization (`choice = 0` first). This is the canonical use of an exit-controlled loop.

### 2.4 continue in a for loop — Filtering

```c
#include <stdio.h>

int main(void)
{
    /* print only ODD numbers from 1..10 (skip evens) */
    for (int i = 1; i <= 10; i++)
    {
        if (i % 2 == 0)
            continue;               /* skip the rest of THIS iteration */
        printf("%d ", i);
    }
    printf("\n");
    return 0;
}
```

**Output:**
```
1 3 5 7 9
```

**Step-by-step for i=2:** condition true → `continue` jumps *directly to the update* (`i++`), skipping `printf`. Note: in this `for` loop, `continue` goes to the update, NOT back to the condition — subtle and exam-critical.

---

## 3. HIGH-YIELD EXAM PROBLEMS & WORKED CODE DRILLS

---

### Problem 1: Switch Fall-Through Output

**Problem.** Predict the output:

```c
int x = 2;
switch (x)
{
    case 1: printf("one ");
    case 2: printf("two ");
    case 3: printf("three ");
            break;
    case 4: printf("four ");
    default: printf("five ");
}
```

---

**Solution:**

**Step 1 — match.** `x = 2` matches `case 2`.

**Step 2 — fall-through.** No `break` at `case 2` or `case 3`; execution falls into `case 3`, prints, then hits `break` and exits the switch.

```
case 2  → prints "two "
case 3  → prints "three "
break   → exit switch
```

$$\boxed{\text{Output: } two\ three}$$

---

### Problem 2: Nested Loop Output (Triangular Pattern)

**Problem.** Predict the output:

```c
for (int i = 1; i <= 3; i++)
{
    for (int j = 1; j <= i; j++)
        printf("%d", j);
    printf("\n");
}
```

---

**Solution — dry-run trace table:**

| Outer i | j values (j ≤ i) | Printed row |
|---|---|---|
| 1 | 1 | `1` |
| 2 | 1, 2 | `12` |
| 3 | 1, 2, 3 | `123` |

$$\boxed{
1\\
12\\
123
}$$

**Total inner iterations:** 1 + 2 + 3 = 6 = n(n+1)/2 (triangular, not 9).

---

### Problem 3: continue vs. break Output

**Problem.** Predict the output:

```c
for (int i = 1; i <= 5; i++)
{
    if (i == 2) continue;
    if (i == 4) break;
    printf("%d ", i);
}
```

---

**Solution — dry-run:**

| i | Action | Printed so far |
|---|---|---|
| 1 | not skipped → print | `1` |
| 2 | `continue` → skip the print, jump to update | `1` |
| 3 | not skipped → print | `1 3` |
| 4 | `break` → exit loop entirely | `1 3` |
| 5 | loop already exited | — |

$$\boxed{\text{Output: } 1\ 3}$$

---

### Problem 4: do-while Execution Count

**Problem.** How many times is the loop body executed?

```c
int i = 10;
do
{
    printf("%d ", i);
    i++;
} while (i < 10);
```

---

**Solution:**

**Step 1 — exit-controlled test.** The body runs first, unconditionally:

- Body executes with i = 10 → prints `10`, i becomes 11.
- Test `i < 10` → `11 < 10` is **false** → loop ends.

$$\boxed{\text{Body executes exactly 1 time; output: } 10}$$

(Contrast: the equivalent `while(i<10)` would run **0** times.)

---

### Problem 5: goto — Legacy Control Flow Trace

**Problem.** Given the following fragment, trace and predict the output:

```c
int i = 0;
start:
i++;
if (i % 2 == 0) goto skip;
printf("%d ", i);
skip:
if (i < 5) goto start;
printf("done\n");
```

---

**Solution — trace table:**

| Step | i before | body | i after | output |
|---|---|---|---|---|
| 1 | 0 | i++ → 1; odd → print | 1 | `1` |
| 2 | 1 | i++ → 2; even → `goto skip` | 2 | — |
| 3 | 2 | i++ → 3; odd → print | 3 | `1 3` |
| 4 | 3 | i++ → 4; even → `goto skip` | 4 | — |
| 5 | 4 | i++ → 5; odd → print | 5 | `1 3 5` |
| 6 | 5 | i++ → 6; even → skip; `i < 5` false → exit | 6 | — |

$$\boxed{\text{Output: } 1\ 3\ 5\ done}$$

**Beginner observation:** this `goto` program is just a roundabout way to print odd numbers — exactly the `continue` example from 2.4. Prefer `continue`/`break` over `goto` unless you're writing kernel error-handling.

---

### Problem 6: continue in for vs. while — Where Does It Jump?

**Problem.** How many times does each fragment print `"X"`?

```c
/* (a) for loop */
int i;
for (i = 0; i < 5; i++)
{
    if (i % 2 == 0) continue;    /* continue → update step → re-test */
    printf("X");                 /* i = 1, 3 → prints twice */
}

/* (b) while loop */
int j = 0;
while (j < 5)
{
    if (j % 2 == 0) continue;    /* continue → re-test, but j NEVER changes! */
    printf("X");
    j++;
}
```

---

**Solution:**

**(a)** `continue` jumps to `i++` (the update), then re-tests. `printf` runs for odd i (1, 3) → **2 prints**, then i=5 stops the loop.

**(b)** `continue` jumps *back to the condition test* — but `j` is incremented only *after* the `printf`. For j=0: continue → test `0 < 5` true → continue → … **infinite loop**, never printing.

$$\boxed{\text{(a) prints X twice} \qquad
\text{(b) infinite loop — j never reaches 5}}$$

**This is THE exam classic:** in `while`, a `continue` before the counter update can cause an infinite loop; in `for`, the update still runs.

---

## 4. REAL-WORLD SYSTEM APPLICATIONS

| Principle | Real-World Practice |
|---|---|
| **if-else decision ladders** | State machines in embedded firmware (sensor threshold checks, emergency stops) |
| **switch-case + fall-through** | Command parsers (IR remote codes, protocol opcodes), event dispatch tables; shared cleanup code in drivers |
| **while / do-while loops** | Polling loops for UART/GPIO, watchdog checks, retry loops with guaranteed-first-pass (menu input, input validation) |
| **for loops** | DMA transfers, PWM ramp tables, string processing, display scan refresh |
| **nested loops** | Matrix multiplication kernels, image convolution filters, search across 2D grids, game-board scans |
| **break** | Early exit in search (find first match), loop termination on error flags |
| **continue** | Filtering outliers in sensor streams (skip bad samples, keep processing) |
| **goto** | Linux kernel & device-driver error-unwind paths (single cleanup label reached from many failure points) |
| **return codes** | Function success/failure contracts; `main` returning exit status to shell/CI |

---

## APPENDIX: Formula & Data Quick Reference

| Construct | Rule | Gotcha |
|---|---|---|
| `if (expr)` | non-zero = true | else binds to nearest if |
| `switch(expr)` | integral expr, const case labels | **fall-through if no break** |
| `while(cond)` | entry-controlled, 0+ runs | infinite loop if cond never false |
| `do{…}while(cond);` | exit-controlled, 1+ runs | **semicolon required** |
| `for(init;cond;update)` | init once → test → body → update | empty cond = forever |
| `continue` (for) | jumps to **update**, then re-test | skips rest of body |
| `continue` (while/do) | jumps to **condition** | can skip the counter → infinite loop |
| `break` | exits innermost loop/switch | not legal in bare if |
| `goto label;` | same-function jump | label unique in scope |
| Nested loops | O(outer × inner) | triangular if inner bound uses outer var |
| `i < n` vs `i <= n` | n vs n+1 iterations | off-by-one trap |

## CROSS-REFERENCES

- Related modules: [[module-1-spm-c-basics]] · [[module-3-arrays]] (loops drive array traversal) · [[module-4-user-defined-functions]] · [[01-Areas/Programming/cs50/week-2-arrays]] · [[01-Areas/Programming/cs50/week-1-c]]

---

*Revision: every syntax pattern from this module is on [[formula-sheet-spm]].*
