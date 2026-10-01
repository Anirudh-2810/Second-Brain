---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "Lab write-ups — EXP1 (data types/operators) + EXP2 (branching) + Windows toolchain"
date: "2026-10-02"
description: "SPM lab write-ups for EXP1 (data types, operators) and EXP2 (if/else/ladder/nested/switch/ternary) — aims, all sample programs as working code, task lists, post-lab Q&A with worked answers, plus MSYS2+GCC+CodeBlocks setup."
tags: [spm, btech, c, lab, experiments, ex1, ex2, data-types, operators, branching, switch, ternary, codeblocks, gcc, msys2, viva]
last_updated: "2026-10-02"
confidence: high
sources:
  - "raw-sources/SPM Lab/EX1 (1).docx"
  - "raw-sources/SPM Lab/EX2.docx"
---

## For future agent

Executable write-ups for SPM **EXP1** and **EXP2**, rebuilt 2026-10-02 from the current lab records `raw-sources/SPM Lab/EX1 (1).docx` (dated 10/1/2026) and `EX2.docx` — **newer versions** than the `SPM SEM1 work/Experiment/` set the previous revision was built from. The new records add **no new topics** but they do supply the **full working code** for every sample program, which the previous revision only summarised in prose. That code is now reproduced here verbatim-cleaned, and every post-lab question gained a worked answer.

Sibling: [[spm-lab-exp3-4-5-guides]] (EXP3/4/5, same depth). Earlier template set: [[spm-lab-exp-guides]] (EXP1/7/8 — same EXP1 aim, different tasks; use EITHER as the write-up base). Rubric/timeline: [[lab-ca-and-experiments]] · [[lesson-plan-2026-27]]. Theory: [[module-1-spm-c-basics]] · [[module-2-program-control-functions]].

**Write-up must contain** handwritten algorithm/pseudocode + flowchart + faculty signature (L4 per [[lab-ca-and-experiments]]), else capped at L3.

# SPM Lab — EXP1 + EXP2

> Dept. of Science and Humanities · Course: Structured Programming Methodology (316U06C107)

---

# EXPERIMENT 1 — Introduction to C: Data Types and Operators (M1, CO1)

## Aim

- To understand how to write, compile, and execute C programs.
- To study the basic structure of a C program.
- To understand output using `printf()` and input using `scanf()`.
- To learn the fundamental data types, constants, and variables available in C.
- To write simple C programs using arithmetic, relational, logical, and assignment operators.

## Theory — the 3-step toolchain

**Step 1 — write.** Open an editor (Notepad or any IDE). Save with a `.c` extension, e.g. `HelloC.c`.

**Step 2 — compile and link.** From the command prompt in that folder:

```bash
gcc HelloC.c -o HelloC
```

This does **compilation** (source → object code, checking syntax) **and linking** (combining with library code such as `printf`) in one command, producing a single executable.

**Step 3 — run.**

```bash
./HelloC        # Linux / macOS
HelloC.exe     # Windows
```

**Note:** unlike Java, **the C filename does not have to match any identifier inside the program.** Only the `.c` extension is mandatory.

## Theory — program structure

```c
#include <stdio.h>

int main() {
    printf("Hello World\n");
    return 0;
}
```

| Line | What it does |
|---|---|
| `#include <stdio.h>` | a **preprocessor directive** that brings in the declarations of standard I/O functions such as `printf` and `scanf` |
| `int main()` | the **entry point** of every C program — execution always begins here |
| `return 0;` | signals to the OS that the program ended **successfully** |

## Theory — data types, constants, variables

*A data type tells the compiler what kind of value a variable holds, which determines how much memory to reserve and which operations are valid on it.*

| Data type | Holds | Typical size | Format specifier |
|---|---|---|---|
| `int` | Whole numbers | 4 bytes | `%d` |
| `float` | Decimal numbers | 4 bytes | `%f` |
| `double` | Decimal, more precision | 8 bytes | `%lf` |
| `char` | A single character | 1 byte | `%c` |

**Constants vs. variables:**

```c
int marks = 40;                      /* a VARIABLE — value can change while running */
const float PI = 3.14;               /* a CONSTANT, via const   — compiler-enforced */
#define PI 3.14                      /* a CONSTANT, via #define — text substitution */
```

`const` is typed and visible to the debugger; `#define` is a preprocessor substitution with no type checking. Prefer `const`.

## Theory — `printf` vs `scanf`

| Function | Purpose |
|---|---|
| `printf()` | displays output on screen, one format specifier per value |
| `scanf()` | reads a value typed by the user into a variable |

```c
printf("Sum = %d", sum);   /* value  */
scanf("%d", &a);            /* ADDRESS */
```

**`scanf` requires the address of the variable** (using `&`), not the variable itself. That is why `scanf("%d", &a);` uses `&a` while `printf("%d", a);` uses plain `a`.

## Theory — the five operator categories

| Category | Operators | Example |
|---|---|---|
| **Arithmetic** | `+  -  *  /  %` | `a + b`, `a % b` |
| **Relational** | `==  !=  >  <  >=  <=` | `a > b` |
| **Logical** | `&&  \|\|  !` | `a > 0 && b > 0` |
| **Assignment** | `=  +=  -=  *=  /=` | `x += 5;` |
| **Increment / Decrement** | `++  --` | `i++`, `++i` |

**Three points to remember (all classic viva questions):**

1. `a / b` performs **integer division** when both operands are `int` — the decimal part is **truncated, not rounded**.
2. A relational expression such as `a > b` evaluates to **1 (true) or 0 (false)** in C — there is **no separate boolean type**.
3. `i++` (**post-increment**) uses the current value first, then increments. `++i` (**pre-increment**) increments first, then uses the new value.

```c
int i = 5;
printf("%d\n", i++);   /* 5 — prints old value, THEN increments */
printf("%d\n", i);     /* 6 */
printf("%d\n", ++i);   /* 7 — increments FIRST, then prints */
```

## Sample program — sum of two numbers

```c
#include <stdio.h>

int main() {
    int a, b, sum;

    printf("Enter first number: ");
    scanf("%d", &a);

    printf("Enter second number: ");
    scanf("%d", &b);

    sum = a + b;

    printf("Sum = %d\n", sum);
    return 0;
}
```

## Laboratory Tasks — EXP1

| # | Task | Focus |
|---|---|---|
| 1 | Declare and initialize an `int`, a `float`, and a `char` (e.g. Age, Percentage, Grade); display all three using the **correct** specifier for each | data types |
| 2 | Input two integers; display the result of all five arithmetic operators (`+ - * / %`), each on its own line | operators |
| 3 | Input a radius as `float`; compute area ($\pi r^2$) and circumference ($2\pi r$) using a **constant** for $\pi$ (`const` or `#define`); print to two decimals | constants + format |

**Task 3 skeleton:**

```c
#include <stdio.h>
int main() {
    float r, area, circ;
    const float PI = 3.14159f;

    printf("Enter radius: ");
    scanf("%f", &r);

    area = PI * r * r;
    circ = 2 * PI * r;

    printf("Area = %.2f\n", area);
    printf("Circumference = %.2f\n", circ);
    return 0;
}
```

### Additional practice — EXP1

1. Swap two variables using a third (**temporary**) variable.
2. Celsius → Fahrenheit: $F = (C \times 9/5) + 32$.
3. Simple interest, given principal, rate and time, using a constant where appropriate.
4. Average of three integers expressed as a `float` — use **explicit casting** to avoid integer-division truncation.
5. Demonstrate `i++` vs `++i` by printing both in **separate** `printf` statements.

## Post-Lab Questions — EXP1

**Conceptual**

1. What is the difference between a compiler and an interpreter?
2. Why must every variable in C be declared with a data type before it is used?
3. What is the difference between a constant and a variable in C?
4. What is the role of the `#include` directive and header files such as `stdio.h`?

**Operators and expressions**

5. Differentiate between `/` and `%` when applied to two integers.
6. Explain the difference between `i++` and `++i` with a suitable example.
7. What is the difference between implicit and explicit type conversion? Give one example of each.
8. What is operator precedence, and how does it affect `10 + 2 * 3`?

**Input/output**

9. What is the difference between `printf()` and `scanf()`?
10. Why does dividing two integers in C truncate the decimal part? How can this be avoided?

<details><summary>Answers 1–10</summary>

**1.** A **compiler** translates the *whole* program before any of it runs (producing a separate executable, faster, all syntax errors surface up front). An **interpreter** translates and executes *line by line* (needs the interpreter every run, slower, stops at the first error it meets while running). C is compiled; Python is interpreted.

**2.** The type tells the compiler how much memory to reserve and which operations are legal. It is fixed at compile time, so the compiler can check types and catch mistakes before running.

**3.** A **variable's** value can change while the program runs (`int marks = 40;`). A **constant's** value is fixed for the program's life, declared with `const` or `#define`; attempting to change a `const` is a compile error.

**4.** `#include` is a preprocessor directive that pastes in the contents of a header file. `stdio.h` holds the **declarations** (not the code) of `printf`, `scanf`, etc. Without it the compiler does not know those functions exist.

**5.** `/` is the **quotient**; `%` is the **remainder**. `%` works on **integers only** — `10.5 % 3` is invalid. Example: `17/5 = 3`, `17%5 = 2`.

**6.** `++i` increments **first**, then supplies the new value. `i++` supplies the **old** value first, then increments. The difference is only observable when the value is used in the same expression.

**7.** **Implicit** (automatic): C converts automatically when types differ, always widening — `int + float` → `float`. **Explicit** (cast): the programmer forces it with `(type)`, e.g. `(float) 7 / 2` = 3.5 instead of 3.

**8.** Precedence decides the order of evaluation. `*` binds tighter than `+`, so `10 + 2*3` = `10 + 6` = **16**, not `(10+2)*3` = 36. Parenthesise when in doubt.

**9.** `printf()` **displays** a value on screen. `scanf()` **reads** a value the user types into a variable, and needs that variable's **address** (`&var`).

**10.** Because both operands are `int`, C applies **integer division**, discarding the fractional part. Avoid it by making at least one operand a `float`: `(float) 7 / 2` = 3.5.
</details>

## Learning Outcome — EXP1

Compile and execute C programs using gcc; understand the basic structure of a C program; use `printf`/`scanf` effectively; declare variables, constants and fundamental data types correctly; apply arithmetic, relational, logical and assignment operators and predict an expression's result type.

---

# EXPERIMENT 2 — Decision Making and Branching (M2.1, CO2)

## Aim

- To understand the concept of decision making in C programs.
- To study branching control structures: `if`, `if-else`, the `else-if` ladder, nested `if-else`, and `switch-case`.
- To learn the conditional (ternary) operator as a shorthand for simple two-way decisions.
- To write C programs that select between alternative paths of execution based on a condition.

## Theory

A program that runs every statement once, top to bottom, is a **pure sequence**. Often a program must instead **choose** between alternatives depending on a condition — this is **decision making** or **branching**, and it is one of the three fundamental control structures of structured programming (alongside sequence and iteration).

**A non-zero condition is TRUE.** `0` is the only false value.

## Sample Program 1 — the `if` statement (one-way selection)

```c
#include <stdio.h>

int main() {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    if (num > 0) {
        printf("%d is positive\n", num);
    }
    return 0;
}
```

The block runs **only if** the condition is non-zero. With no `else`, the other case simply does nothing.

## Sample Program 2 — `if-else` (two-way selection)

```c
#include <stdio.h>

int main() {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    if (num % 2 == 0) {
        printf("%d is Even\n", num);
    } else {
        printf("%d is Odd\n", num);
    }
    return 0;
}
```

```
        Condition
        /       \
     True       False
      /           \
   IF block     ELSE block
```

## Sample Program 3 — the `else-if` ladder (multi-way selection)

```c
#include <stdio.h>

int main() {
    int marks;

    printf("Enter marks (0-100): ");
    scanf("%d", &marks);

    if (marks >= 90)      { printf("Grade : A\n"); }
    else if (marks >= 75) { printf("Grade : B\n"); }
    else if (marks >= 60) { printf("Grade : C\n"); }
    else if (marks >= 40) { printf("Grade : D\n"); }
    else                  { printf("Grade : F\n"); }
    return 0;
}
```

The program checks one condition after another, **top-down, and the first true one wins** — the rest are skipped entirely.

## Sample Program 4 — nested `if-else` (largest of three)

```c
#include <stdio.h>

int main() {
    int a, b, c;

    printf("Enter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);

    if (a > b) {
        if (a > c)
            printf("Largest = %d\n", a);
        else
            printf("Largest = %d\n", c);
    } else {
        if (b > c)
            printf("Largest = %d\n", b);
        else
            printf("Largest = %d\n", c);
    }
    return 0;
}
```

Nesting means **deciding after deciding**: first find out whether `a` beats `b`, then resolve the remaining pair. Use it when the second question only makes sense given the answer to the first.

## Sample Program 5 — `switch-case` (simple calculator)

```c
#include <stdio.h>

int main() {
    char op;
    float a, b;

    printf("Enter operator (+, -, *, /): ");
    scanf(" %c", &op);
    printf("Enter two numbers: ");
    scanf("%f %f", &a, &b);

    switch (op) {
        case '+':
            printf("Result = %.2f\n", a + b); break;
        case '-':
            printf("Result = %.2f\n", a - b); break;
        case '*':
            printf("Result = %.2f\n", a * b); break;
        case '/':
            if (b != 0)
                printf("Result = %.2f\n", a / b);
            else
                printf("Error: Division by zero\n");
            break;
        default:
            printf("Invalid operator\n");
    }
    return 0;
}
```

**Three things to point out in a viva:**

- The **leading space in `scanf(" %c", &op)`** skips any leftover newline from the previous input.
- The `b != 0` guard prevents a division-by-zero crash.
- `default` catches anything not listed.

## Sample Program 6 — the ternary (conditional) operator

```c
#include <stdio.h>

int main() {
    int a, b, max;

    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    max = (a > b) ? a : b;
    printf("Largest = %d\n", max);
    return 0;
}
```

`condition ? value_if_true : value_if_false` — a one-line shorthand for a simple two-way decision.

## Points to remember

- The **`switch` expression must evaluate to an integer or character type** — it cannot be used directly with `float` or strings.
- **Without a `break`, execution falls through** into the next `case` — a common source of bugs.
- Nested `if-else` and an `else-if` ladder can often express the same logic; choose whichever is more readable for the problem.

## Laboratory Tasks — EXP2

| # | Task | Focus |
|---|---|---|
| 1 | **Leap year check** — divisible by 4, except centuries (÷100), which must also be ÷400 | compound boolean logic |
| 2 | **Vowel or consonant** — accept a single alphabet character and decide using **`switch-case`** | switch on `char` |
| 3 | **Menu-driven calculator** — five operations (add, sub, mul, div, modulus); accept two numbers and the menu choice; perform and display the result; handle **division/modulus by zero** and any **invalid menu choice** with a clear error message instead of crashing or printing garbage | switch + error handling |

**Task 1 — the leap-year rule:**

```c
if ((year % 400 == 0) || (year % 4 == 0 && year % 100 != 0))
    printf("%d is a leap year\n", year);
else
    printf("%d is not a leap year\n", year);
```

### Additional practice — EXP2

1. Check whether a number is positive, negative, or zero.
2. Find the largest of three numbers using **nested** `if-else`.
3. Accept the three angles of a triangle; first check they form a valid triangle (must sum to 180°), then classify as **Equilateral**, **Isosceles**, or **Scalene**.
4. Validate a 4-digit PIN against a stored constant PIN; print "Access Granted" or "Access Denied".
5. Accept a day number 1–7 and print the day name using `switch-case`.

## Post-Lab Questions — EXP2

**Conceptual**

1. What is meant by "decision making" in a program, and why is it necessary?
2. What is the difference between a simple `if-else` and an `else-if` ladder?
3. When would nested `if-else` be preferred over an `else-if` ladder, and vice versa?

**Switch and ternary**

4. What data types can a `switch` expression evaluate to in C?
5. What is the purpose of `break` inside a `switch-case`? What happens if it is omitted?
6. What is the purpose of the `default` case?
7. Rewrite using a single ternary expression: `if (a > b) max = a; else max = b;`

**Logic and tracing**

8. Trace the output: `int x = 15; if (x % 3 == 0 && x % 5 == 0) printf("A"); else if (x % 3 == 0) printf("B"); else printf("C");`
9. Can a `switch` be used to test floating-point values? Why or why not?
10. What is the difference between `=` and `==`, and why is this especially important inside a decision statement?

<details><summary>Answers 1–10</summary>

**1.** Choosing between alternative execution paths based on a condition, rather than running every statement once. It is necessary because real problems require *choice* — grading, validation, menu selection — which a pure sequence cannot express.

**2.** `if-else` handles **exactly two** branches. An `else-if` ladder handles **many** branches, tested in order, where the first true condition wins and the rest are skipped.

**3.** Use **nested** `if-else` when the second question only makes sense given the first answer (dependent decisions). Use a **ladder** when you are testing one value against a ranked list of thresholds (grade bands).

**4.** `int` and `char` only (enumerated types also work). Not `float`/`double`, not strings.

**5.** `break` exits the `switch` so control does not continue into the next `case`. Omitted, execution **falls through** to the following case, running that case's statements too.

**6.** `default` is the catch-all for when no `case` matches. It prevents the switch from doing nothing on unmatched input.

**7.** `max = (a > b) ? a : b;`

**8.** **A.** `x = 15`: `15 % 3 == 0` is true **and** `15 % 5 == 0` is true, so the **first** `if` matches and prints `A`. The `else if` is never reached — a good illustration that only the **first** true condition in a chain executes.
</details>

<details><summary>Answers 9–10</summary>

**9.** **No.** A `switch` expression must be of integer or character type. `float`/`double` cannot be compared by equality reliably (floating-point rounding), so C forbids them. Workaround: nest an `if-else` instead, or convert to `int`.

**10.** `=` is **assignment** — it stores a value. `==` is **comparison** — it asks whether two values are equal. The classic bug is writing `if (x = 5)`, which **assigns** 5 to `x` and then tests 5, which is non-zero, so the branch is **almost always taken**. Inside a decision statement this silently produces wrong output, so it is a favourite viva question.
</details>

## Learning Outcome — EXP2

Understand and apply decision-making constructs in C; differentiate between `if-else`, an `else-if` ladder, nested `if-else`, and `switch-case` and choose the appropriate structure; use the ternary operator as shorthand for simple two-way decisions; design and implement menu-driven programs with proper error handling.

---

# Appendix — Windows toolchain (MSYS2 + GCC + CodeBlocks)

Fresh Windows → C in CMD + Code::Blocks:

1. Install **MSYS2** from `https://www.msys2.org/` (default `C:\msys64`, UCRT64 environment).
2. `pacman -Syu` — **run it twice**, reopening the terminal between runs.
3. `pacman -S --needed mingw-w64-ucrt-x86_64-gcc mingw-w64-ucrt-x86_64-gdb mingw-w64-ucrt-x86_64-make`
4. Verify: `gcc --version` and `which gcc` (should print `/ucrt64/bin/gcc`).
5. Add `C:\msys64\ucrt64\bin` to the **user** Path.
6. **Open a NEW cmd** and re-check `gcc --version` and `where gcc`.
7. Test: `gcc hello.c -o hello.exe` → run `hello.exe` → it should print `Hello, C!`.
8. **Code::Blocks:** point the toolchain at `C:\msys64\ucrt64\bin` (auto-detect usually finds it) → new console project → build and run.

**Failure order to check:** no `gcc.exe` on disk → wrong MSYS2 folder (`which gcc` tells the truth) · CMD says "not recognized" → stale terminal (reopen it) or a Path typo · Code::Blocks "can't find compiler" → toolchain path unset.

---

## Cross-references

- **Sibling write-ups (same depth):** [[spm-lab-exp3-4-5-guides]]
- Depth: [[module-1-spm-c-basics]] · [[module-2-program-control-functions]] · [[spm-module1-faculty-companion]] · [[spm-module2-faculty-companion]]
- Drills: [[spm-practice-bank-module1]] · [[spm-practice-bank-module2]] · [[spm-quiz-bank]]
- Earlier template set: [[spm-lab-exp-guides]] — Rubric/schedule: [[lab-ca-and-experiments]] · [[lesson-plan-2026-27]]

*Ingested 2026-10-02 from `raw-sources/SPM Lab/EX1 (1).docx` and `EX2.docx`.*
