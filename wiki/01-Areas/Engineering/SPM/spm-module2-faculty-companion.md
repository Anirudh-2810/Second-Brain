---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "M2 faculty companion — PPT deltas over module-2-program-control-functions"
tags: [spm, btech, c, module-2, branching, loops, switch, ternary, flags, documentation, readability]
last_updated: "2026-09-18"
date: "2026-09-18"
description: "SPM M2 faculty-PPT companion — flag and counting loops, documentation before/after, calculator guard, fall-through grouping, loop-choice tables, infinite-loop fixes."
---

## For future agent

This note holds ONLY what the Sem-1 faculty PPTs add on top of [[module-2-program-control-functions]] — the flag concept, counting loops, documentation demo, and faculty code variants. Loop/switch semantics depth stays in [[module-2-program-control-functions]]. Drills in [[spm-practice-bank-module2]], quiz in [[spm-quiz-bank]], lab in [[spm-lab-exp1-exp2-guides]].

# SPM M2 Faculty Companion — PPT Deltas (Sem-1 Drive)

> Sources: `raw-sources/SPM SEM1 work/PPT/Module 2/` — `SPM_Module2.pptx` (overview) · `SPM_Module2_1.pptx` (2.1 branching) · `SPM_Module2_2.pptx` (2.2 loops) | Syllabus: [[syllabus-316U06C107]] M2 (6 hrs, CO2) | Builds on: [[spm-module1-faculty-companion]] §2–§3

## 1. Branching faculty variants (2.1)

One-way `if` (single path, else absent) vs two-way `if-else` (exactly one of two always runs — unlike two separate `if`s). `else` has no condition; it catches everything the `if` did not. Ternary is an OPERATOR, not a statement — it can sit inside an assignment or `printf`: `max = (a > b) ? a : b;`. Best for short value-choices; elaborate logic deserves plain `if-else`.

Grade-ladder faculty cutoffs (note: differ from the generic wiki example — memorize THESE for lab EXP2): 90→A, 75→B, 60→C, 40→D, else F. Order matters: first true wins, rest never evaluated.

Nested `if-else` (second decision only makes sense after the first narrows it down) — largest-of-three:

```c
if (a > b) {
    if (a > c) printf("Largest = %d\n", a);
    else       printf("Largest = %d\n", c);
} else {
    if (b > c) printf("Largest = %d\n", b);
    else       printf("Largest = %d\n", c);
}
```

Trace `8 8 5`: `a>b` false (8 not > 8) → else branch → `b>c` (8>5) true → prints 8.

Dangling-else: `else` binds to the NEAREST unmatched `if`, regardless of indentation. Always brace to disambiguate.

Switch rules: expression must be int/char (never float/string); `case` labels compile-time constants; `break` essential — without it execution falls through into the next case. Intentional fall-through groups several labels over one block:

```c
switch (day) {
    case 1: case 2: case 3: case 4: case 5:
        printf("Weekday\n"); break;
    default: printf("Weekend\n");
}
```

Calculator with division-by-zero guard (faculty `calculator.c` — note the leading space in `scanf(" %c",...)` consuming leftover newline, and the `b != 0` check):

```c
#include <stdio.h>
int main() {
    char op; float a, b;
    printf("Enter operator (+, -, *, /): ");
    scanf(" %c", &op);
    printf("Enter two numbers: ");
    scanf("%f %f", &a, &b);
    switch (op) {
        case '+': printf("Result = %.2f\n", a + b); break;
        case '-': printf("Result = %.2f\n", a - b); break;
        case '*': printf("Result = %.2f\n", a * b); break;
        case '/':
            if (b != 0) printf("Result = %.2f\n", a / b);
            else printf("Error: Division by zero\n");
            break;
        default: printf("Invalid operator\n");
    }
    return 0;
}
```

Choosing-structure table:

| Situation | Best choice |
|---|---|
| One action, only if condition holds | `if` |
| Exactly two mutually exclusive outcomes | `if-else` (ternary if both are simple values) |
| Several ranked conditions in turn | `else-if` ladder |
| Decision only after an earlier one | Nested `if-else` |
| One variable vs many fixed values | `switch-case` |

Grade ladder CANNOT become a `switch` directly — ranges (`>=`) are not single-variable equality. Pitfalls: `=` vs `==` (`if(x=0)` assigns 0 → false → else runs); trusting indentation over braces; `switch` on float/string (won't compile); nested ternaries (unreadable).

Quick-test answers (2.1): one-var-many-fixed = switch; `if(x=0)` prints B; `break` stops fall-through; dangling-else = else binds nearest if, fix with braces; "switch accepts float" = False.

## 2. Flags and counting loops (2.2 — the two named patterns)

**Flag concept:** a variable (int/bool) recording whether an event occurred during a loop — checked AFTER the loop. Survives the loop (loop index may go out of scope), self-documents (`found=1`), pairs with `break`:

```c
int arr[5] = {12, 45, 7, 23, 9};
int key = 23, found = 0;
for (int i = 0; i < 5; i++) {
    if (arr[i] == key) { found = 1; break; }
}
if (found) printf("Key found!\n");
else       printf("Key not found.\n");
```

**Counting loop:** a dedicated counter incremented once per match, tallying occurrences:

```c
int num, count = 0;
scanf("%d", &num);
while (num != 0) { num = num / 10; count++; }
printf("Digit count = %d\n", count);
```

`4507` → 4 iterations. Sum-of-digits (`348` → 15) follows the same strip-and-accumulate shape with `digit = num % 10; sum += digit; num /= 10;`.

Nested-loop multiplication rule: total inner runs = outer × inner; the inner variable RESETS each outer pass. `(i,j)` trace for outer 3 × inner 2 gives `(1,1) (1,2) (2,1) (2,2) (3,1) (3,2)`. Triangular variant (inner bound = outer variable, `j<=i`) grows per row — the `*` triangle pattern.

## 3. break / continue / infinite loops (2.2)

`break` exits entirely; `continue` skips only the REST of the current iteration. In `for`, `continue` still runs the update (`i++`) before re-testing; in `while`, it jumps straight to the condition — so `continue` placed before the counter update loops forever:

```c
int i = 1;
while (i <= 5) {
    if (i == 3) continue;   /* skips i++ — stuck at 3 forever */
    printf("%d ", i);
    i++;
}
```

Combined demo (prints `2 4 6 8 10`):

```c
for (i = 1; i <= 20; i++) {
    if (i % 2 != 0) continue;  /* skip odds */
    if (i > 10) break;         /* stop after 10 */
    printf("%d ", i);
}
```

Infinite-loop causes: missing update (`for(i=1;i<=10;)` with no `i++`); updating the WRONG variable (condition checks `i`, body increments `j`); condition never false (`while(1)` — deliberate only with an internal `break`, the standard menu pattern). Rule: the variable updated inside must be the SAME one the condition tests. Off-by-one (`i<n` vs `i<=n`) is a separate classic — double-check needed vs needed+1.

Choosing-loop table:

| Situation | Best choice |
|---|---|
| Exact repetitions known upfront | `for` |
| Runtime condition, unknown count | `while` |
| Body must run at least once (menu/validation) | `do-while` |
| Rows/columns, tables, patterns | Nested loops |
| Stop early / skip one iteration | `break` / `continue` |

Any `for` rewrites as `while` and vice versa — choose the clearest. `do-while` trailing semicolon (`while(cond);`) is the easy-to-forget part.

Quick-test answers (2.2): guaranteed-once = do-while; `for(i=1;i<=4;i++){if(i==2)continue;printf(...);}` prints `1 3 4`; three termination ingredients = init + condition + update-toward-false; nested 4×5 = 20 iterations; "continue skips the for-update too" = False.

## 4. Documentation and readable code (2.3)

Four rules: comments (`//` brief, `/* */` longer — explain WHY, not what) · meaningful names (`totalMarks`, not `tm`) · consistent indentation (shows nesting) · logical spacing (blank lines between sections).

Before/after (same function):

```c
int f(int a,int b){int c;if(a>b){c=a;}else{c=b;}return c;}
```

```c
// Returns the larger of two integers
int findMax(int firstNum, int secondNum) {
    int maxValue;
    if (firstNum > secondNum) maxValue = firstNum;
    else                      maxValue = secondNum;
    return maxValue;
}
```

Quick-test answers (2.3 + module): `for(i=0;i<3;i++)` prints `0 1 2`; flag = records event during loop, decided after; "comments are compiled / affect execution" = False.

## Cross-references

- Depth: [[module-2-program-control-functions]] · M1: [[spm-module1-faculty-companion]]
- Drill: [[spm-practice-bank-module2]] · [[spm-quiz-bank]]
- Lab: [[spm-lab-exp1-exp2-guides]] · Pattern: [[assessment-guide-ese-ost-quiz]]
