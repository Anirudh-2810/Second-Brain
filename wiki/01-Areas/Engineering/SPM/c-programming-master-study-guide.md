---
module: "SPM"
topic: "C Programming — Exhaustive Master Study Guide (Memory, Control Flow, Arrays, Functions)"
tags: [c-programming, study-guide, preprocessor, memory-layout, stack, heap, bss, data-segment, text-segment, operators, precedence, if-else, switch-case, while, do-while, for, break, continue, arrays, 1d-arrays, 2d-arrays, row-major, column-major, address-calculation, binary-search, bubble-sort, matrix-multiplication, functions, call-by-value, call-by-reference, recursion, storage-classes, auto, static, register, extern]
last_updated: "2026-08-19"
prerequisites: ["None (self-contained exam + interview cram guide)"]
---

# C Programming — Exhaustive Master Study Guide

> High-density, exam-and-interview cram guide covering the complete core C syllabus: the **compile pipeline & process memory layout**, the **full control-flow toolbox**, **1D/2D arrays with row-major/column-major address derivations**, and **user-defined functions** (parameter passing, recursion stack mechanics, storage classes). Every section follows the same three-part discipline: **ASCII flowchart → LaTeX derivation → working C code**.
>
> Formatting contract for this guide: each topic block contains (a) an ASCII architecture/flow diagram, (b) mathematical derivation where relevant, (c) compilable C code, (d) a complexity/behaviour table, and (e) an exam-trap callout.

---

## Table of Contents

1. [C Architecture & Memory](#1-c-architecture--memory)
   - [1.1 Preprocessor Pipeline](#11-preprocessor-pipeline)
   - [1.2 Process Memory Layout (Text / Data / BSS / Heap / Stack)](#12-process-memory-layout)
   - [1.3 Variable Types & Sizes](#13-variable-types--sizes)
   - [1.4 Operators & Precedence](#14-operators--precedence)
2. [Control Flow](#2-control-flow)
   - [2.1 if-else & the Dangling-Else](#21-if-else--the-dangling-else)
   - [2.2 switch-case & Fall-Through](#22-switch-case--fall-through)
   - [2.3 while / do-while / for](#23-while--do-while--for)
   - [2.4 break / continue & Loop Interaction](#24-break--continue--loop-interaction)
3. [Arrays](#3-arrays)
   - [3.1 1D Array Memory Layout](#31-1d-array-memory-layout)
   - [3.2 2D Array Layout & Row-Major vs Column-Major](#32-2d-array-layout--row-major-vs-column-major)
   - [3.3 Binary Search](#33-binary-search)
   - [3.4 Bubble Sort](#34-bubble-sort)
   - [3.5 Matrix Operations](#35-matrix-operations)
4. [User-Defined Functions](#4-user-defined-functions)
   - [4.1 Call by Value vs. Call by Reference](#41-call-by-value-vs-call-by-reference)
   - [4.2 Recursion & Stack Execution](#42-recursion--stack-execution)
   - [4.3 Storage Classes](#43-storage-classes)
5. [Appendix: One-Page Formula & Trap Sheet](#appendix-one-page-formula--trap-sheet)

---

## 1. C Architecture & Memory

### 1.1 Preprocessor Pipeline

A C program is **not** compiled in one step. Four (standard) stages transform `source.c` into `a.out`. Each stage has its own error class.

```
   source.c ──► ┌─────────────────────┐
                │ 1. PREPROCESSOR     │  handles #include, #define, #if/#ifdef,
                │  (cpp)              │  #pragma, macro expansion, comment strip
                └──────────┬──────────┘
                           ▼
   source.i ──► ┌─────────────────────┐
                │ 2. COMPILER         │  C → assembly. Syntax + type checking.
                │  (cc1)              │  Errors here = "syntax error", "type mismatch"
                └──────────┬──────────┘
                           ▼
   source.s ──► ┌─────────────────────┐
                │ 3. ASSEMBLER        │  assembly → object (.o/.obj) machine code
                │  (as)               │  Errors here = rare (bad opcodes/labels)
                └──────────┬──────────┘
                           ▼
   source.o ──► ┌─────────────────────┐
                │ 4. LINKER           │  resolves symbols across .o + libs, lays out
                │  (ld)               │  memory addresses, produces executable
                └──────────┬──────────┘
                           ▼
                         a.out / a.exe
```

**What the preprocessor does (memorize all five):**

| Directive | Behaviour | Example |
|---|---|---|
| `#include <h>` / `"h"` | textually pastes header contents | `#include <stdio.h>` |
| `#define X value` | object-like macro; textual replacement, **no type** | `#define PI 3.14159` |
| `#define F(a,b) …` | function-like macro (types unchecked!) | `#define MAX(a,b) ((a)>(b)?(a):(b))` |
| `#if`/`#ifdef`/`#ifndef`/`#elif`/`#endif` | conditional compilation | platform guards |
| `#undef` | removes a macro | `#undef PI` |
| `#pragma` | compiler-specific instructions | `#pragma once` |
| `#error` / `#warning` | emit diagnostic during preprocessing | `#error "unsupported arch"` |

**Preprocessor gotchas (exam + interview traps):**
- Macros are **textual** — `SQUARE(x)` with `x+1` becomes `x+1*x+1`. **Always parenthesize both the argument and the whole body**: `#define SQUARE(x) ((x)*(x))`.
- Macros **have no type checking**, no scope, and evaluate arguments *multiple times* (side effects run more than once). Prefer `inline` functions in modern C.
- `#include "file.h"` searches the current dir first, then include path; `<file.h>` searches the include path only.
- **Compile commands:** `gcc -E prog.c` (preprocess only), `-S` (assembly), `-c` (object), `-o out` (link+name). The classic error-to-stage cheat sheet: undefined reference → **linker**; syntax/type errors → **compiler**; "file not found" for a header → **preprocessor**.

**Macro vs. function decision table:**

| Criterion | Macro | Function |
|---|---|---|
| Speed | faster (no call overhead) | call overhead |
| Type safety | **none** | yes |
| Side-effect safety | unsafe (args re-evaluated) | safe |
| Code size | grows each use | single copy |
| Debuggable | harder (expands away) | yes |

### 1.2 Process Memory Layout

When a compiled program **runs**, the OS gives it a virtual address space split into regions with distinct lifetimes:

```
   HIGH ADDRESS  ┌─────────────────────────────┐
                 │   STACK — grows DOWNWARD     │  automatic variables, call frames,
                 │   (toward lower addresses)   │  return addresses, parameters
                 │                             │  lifetime = function call
                 │            ↕  (gap)         │  stack overflow: too many frames
                 │            ↕                │  (deep recursion / big locals)
                 ├─────────────────────────────┤
                 │   HEAP — grows UPWARD        │  malloc/calloc/realloc/free
                 │   (toward higher addresses)  │  lifetime = manual
                 │   managed by brk/mmap        │  leaks: malloc without free
                 ├─────────────────────────────┤
                 │   BSS  (uninitialized data)  │  globals/statics w/o initializer,
                 │   zero-initialized by OS     │  e.g. `int g;` → 0
                 ├─────────────────────────────┤
                 │   DATA (initialized data)    │  globals/statics with a value,
                 │   e.g. `int g = 5;`          │  string literals' writable copies
                 ├─────────────────────────────┤
                 │   TEXT (code segment)        │  compiled instructions, read-only
                 │   const strings live here    │  writes → segmentation fault
   LOW ADDRESS   └─────────────────────────────┘
```

**Per-region rules (memorize):**

| Region | What lives there | Lifetime | Initial value | Direction |
|---|---|---|---|---|
| **Text** | machine code, `const` string literals | entire process | read-only | — |
| **Data** | initialized globals/statics | process | their initializer | — |
| **BSS** | uninitialized globals/statics | process | **zero** | — |
| **Heap** | `malloc`/`calloc`/`realloc` blocks | until `free` | garbage (malloc) / zero (calloc) | grows **up** |
| **Stack** | locals, params, return addresses | current call | garbage (uninitialized locals) | grows **down** |

**Beginner trap:** *uninitialized* `malloc` memory is garbage; *uninitialized* globals are guaranteed 0; *uninitialized* locals are garbage. Three different defaults — three exam answers.

**malloc vs calloc (behavioural):**

| Function | Signature | Initialization | Size computation |
|---|---|---|---|
| `malloc` | `void *malloc(size_t n)` | garbage | `n` bytes |
| `calloc` | `void *calloc(size_t count, size_t size)` | **all zero** | `count × size` |
| `realloc` | `void *realloc(void *p, size_t n)` | preserves old data | resizes |
| `free` | `void free(void *p)` | releases block | must match a malloc-family ptr |

**Working code — heap demo with region annotation:**

```c
#include <stdio.h>
#include <stdlib.h>

int g_global = 7;        /* DATA segment  */
int g_uninit;            /* BSS segment (guaranteed 0) */
static int s_static = 3; /* DATA segment, file-local */

int main(void)
{
    int local = 10;                              /* STACK */
    static int f_local = 5;                      /* DATA segment (init once) */

    int *p = malloc(4 * sizeof(int));            /* HEAP */
    if (p == NULL) return 1;
    p[0] = 1; p[1] = 2; p[2] = 3; p[3] = 4;      /* heap writes */
    for (int i = 0; i < 4; i++) printf("%d ", p[i]);
    printf("\n");

    printf("g_uninit = %d\n", g_uninit);         /* prints 0 (BSS zeroed) */
    free(p);                                     /* return heap to OS */
    return 0;
}
```

**The `malloc` + `free` contract:** every block allocated must be released exactly once. `free(p)` twice = double-free (undefined behaviour, heap corruption); `p = malloc(...)` without free = leak; `free` on a non-malloc pointer = undefined.

### 1.3 Variable Types & Sizes

| Type | Typical size | Range (typical, 32-bit int) | `printf` | `scanf` |
|---|---|---|---|---|
| `char` | 1 B | −128…127 (signed) or 0…255 | `%c`, `%hhd` | `%c`, `%hhd` |
| `signed char` | 1 B | −128…127 | `%hhd` | `%hhd` |
| `unsigned char` | 1 B | 0…255 | `%hhu` | `%hhu` |
| `short int` | 2 B | −32768…32767 | `%hd` | `%hd` |
| `unsigned short` | 2 B | 0…65535 | `%hu` | `%hu` |
| `int` | 4 B | −2³¹…2³¹−1 | `%d` | `%d` |
| `unsigned int` | 4 B | 0…2³²−1 | `%u` | `%u` |
| `long int` | 8 B (LP64) | −2⁶³…2⁶³−1 | `%ld` | `%ld` |
| `float` | 4 B | ~±3.4e38 (7 sig. digits) | `%f` | `%f` |
| `double` | 8 B | ~±1.8e308 (15–16 digits) | `%f`, `%lf` | `%lf` |
| `long double` | 10–16 B | extended precision | `%Lf` | `%Lf` |
| `size_t` | 8 B (LP64) | 0…2⁶⁴−1 | `%zu` | `%zu` |
| `void*` | 8 B (LP64) | address | `%p` | `%p` |

**Rules that cost marks:**
- **Sizes are implementation-defined** — only guaranteed ordering holds: `char ≤ short ≤ int ≤ long ≤ long long` (in bytes). On a 64-bit Linux box `long` is 8 bytes; on Windows LLP64 it is 4. Always `printf("%zu", sizeof(x))`.
- Integer arithmetic on `char`/`short` promotes to `int` first (usual arithmetic conversions).
- `int` overflow is **undefined behaviour** in C; `unsigned` wraps modulo 2ⁿ (defined).
- Literal types: `5` (int), `5L` (long), `5LL` (long long), `5U` (unsigned), `5.0` (double), `5.0f` (float), `'A'` (int, the ASCII code 65), `"A"` (char array of 2).

### 1.4 Operators & Precedence

**Full precedence ladder (high → low), group of operators with same level listed together:**

| Level | Operators | Associativity | Meaning |
|---|---|---|---|
| 1 | `()` `[]` `.` `->` `++`(post) `--`(post) | left→right | grouping, indexing, member, post-inc |
| 2 | `!` `~` `+`(unary) `-`(unary) `*`(deref) `&`(addr) `sizeof` `++`(pre) `--`(pre) | right→left | negation, bitwise NOT, address-of |
| 3 | `*` `/` `%` | left→right | multiply, divide, modulo |
| 4 | `+` `-` | left→right | add, subtract |
| 5 | `<<` `>>` | left→right | bit shifts |
| 6 | `<` `<=` `>` `>=` | left→right | relational |
| 7 | `==` `!=` | left→right | equality |
| 8 | `&` | left→right | bitwise AND |
| 9 | `^` | left→right | bitwise XOR |
| 10 | `\|` | left→right | bitwise OR |
| 11 | `&&` | left→right | logical AND (**short-circuits**) |
| 12 | `\|\|` | left→right | logical OR (**short-circuits**) |
| 13 | `?:` | **right→left** | ternary |
| 14 | `=` `+=` `-=` `*=` `/=` `%=` `<<=` `>>=` `&=` `^=` `\|=` | **right→left** | assignment |
| 15 | `,` | left→right | comma |

**Working precedence examples (trace each):**

```c
int a = 5, b = 3, c = 2;
int r1 = a + b * c;      /* 5 + (3*2) = 11   (level 3 before 4)   */
int r2 = a * b % c;      /* (5*3) % 2 = 1     (same level, L→R)   */
int r3 = a > b && c;     /* (5>3) && 2 → 1 && 1 = 1  (rel → &&)   */
int r4 = a = b = c;      /* c=2 → b=2 → a=2   (assignment R→L)    */
```

**Exam-trap roundup:**
- `==` vs `=` — `if (x = 5)` assigns and is *always true*. Write `if (5 == x)` (Yoda style) so a typo becomes a compile error.
- `&&` / `||` **short-circuit**: `(ptr != NULL && ptr->len > 0)` — if the first test fails, the second never runs (that's how this idiom is safe).
- `sizeof` is a **compile-time** operator (not a function — parens are just convention) and is evaluated before runtime; `sizeof(x++)` does **not** increment x.
- Pre/post increment in expressions is undefined-before-C++17-style sequencing — never write `x = i++ + i++`.
- `%` with a negative dividend is implementation-defined in C89, truncation-toward-zero in C99+.

---

## 2. Control Flow

### 2.1 if-else & the Dangling-Else

```
                        ┌───────────────────────┐
                        │  if (condition)        │
                        └───────────┬───────────┘
                    TRUE            │            FALSE
                        ▼           │            ▼
                 ┌──────────┐       │      ┌──────────────┐
                 │ if-body  │       │      │ else-body    │
                 └────┬─────┘       │      └──────┬───────┘
                      │             │             │
                      └─────────────┴─────────────┘
                                    ▼
                         next statement (all paths)
```

**Rules:** `if (expr)` — non-zero = true. One statement needs no braces, many need braces. `else` binds to the **nearest unmatched** `if`.

**The dangling-else trap (classic):**

```c
if (a)
    if (b) printf("A");     /* prints only when a && b */
else                        /* BINDS TO if(b), not if(a) */
    printf("B");            /* prints when a && !b  */
```

Braces make the pairing explicit:

```c
if (a)
{
    if (b) printf("A");
}
else                        /* now binds to if(a) */
    printf("B");            /* prints when !a     */
```

### 2.2 switch-case & Fall-Through

```
   switch (expr)   // expr must be INTEGRAL (int/char/enum)
        │
        ▼
   compare expr against each case (compile-time constants)
        │
        ├── MATCH case k ──► execute case k body
        │                       │
        │                       ├── break?  ──YES──► exit switch
        │                       └── NO break (fall-through)
        │                            ▼
        │                   execute case k+1 body ...
        │
        └── NO match ──► run default: (if present)
```

**Working code — the fall-through demonstration:**

```c
#include <stdio.h>

int main(void)
{
    int day = 3;
    switch (day)
    {
        case 1: printf("Mon ");
        case 2: printf("Tue ");
        case 3: printf("Wed ");          /* matches day=3 */
        case 4: printf("Thu ");          /* FALLS THROUGH: no break above */
        case 5: printf("Fri ");
                break;                   /* chain stops here */
        default: printf("Weekend\n");
    }
    printf("\n");
    return 0;
}
/* OUTPUT: Wed Thu Fri   — fall-through from case 3 through case 5 */
```

**switch vs if-else decision table:**

| Criterion | `if-else` | `switch` |
|---|---|---|
| Conditions | any expression | integral constant equality only |
| Ranges (`x >= 60 && x < 70`) | yes | no |
| Compiler strategy | compare chain | **jump table** (O(1) dispatch) when dense |
| Fall-through risk | none | **yes — forgetting `break`** |
| Default branch | `else` | `default:` |
| Strings / floats | possible | **not allowed** |

### 2.3 while / do-while / for

**The three loops — semantics table:**

| Loop | Test timing | Min. runs | Semicolon needed? | Use case |
|---|---|---|---|---|
| `while (cond) {…}` | entry (top) | 0 | no | unknown count: read-until-EOF, wait-for-flag |
| `do {…} while (cond);` | exit (bottom) | **1** | **yes** | must-run-once: menus, validation |
| `for (init; cond; update) {…}` | entry | 0 | no | counted loops |

**Exact for-loop execution sequence (memorize order):**

```
   for ( init ; condition ; update ) { body }
        │1          │2             │4
        ▼           ▼              ▼
   STEP 1: init (runs ONCE before first test)
   STEP 2: test condition
        │
      TRUE ──► STEP 3: execute body
        │              │
        │              ▼
        │         STEP 4: update expression
        │              │
        │              ▼
        └─────── back to STEP 2
      FALSE
        │
        ▼
   exit loop (continue after)
```

**Off-by-one rules (the highest-frequency C bug):**

```c
for (int i = 0; i < n; i++) ...   /* runs n times, i = 0..n-1  */
for (int i = 1; i <= n; i++) ...  /* runs n times, i = 1..n    */
for (int i = 0; i <= n; i++) ...  /* runs n+1 times, i = 0..n  ← off-by-one trap */
for (int i = 0; i < n; i++);      /* EMPTY body — runs n times doing nothing! */
```

**Working code — the three loops side by side (same output):**

```c
#include <stdio.h>

int main(void)
{
    int i = 0;
    while (i < 3) { printf("W%d ", i); i++; }     /* entry-controlled */
    printf("| ");

    int j = 0;
    do { printf("D%d ", j); j++; } while (j < 3); /* exit-controlled, min 1 run */
    printf("| ");

    for (int k = 0; k < 3; k++) printf("F%d ", k);/* init/test/update */
    printf("\n");
    return 0;
}
/* OUTPUT: W0 W1 W2 | D0 D1 D2 | F0 F1 F2 */
```

### 2.4 break / continue & Loop Interaction

```
   ┌──────────────┐   ┌──────────────────────┐
   │ break        │   │ continue             │
   │ exits the    │   │ skips rest of current│
   │ innermost    │   │ iteration, jumps to: │
   │ loop/switch  │   │  while/do-while → cond│
   │ entirely     │   │  for → update, then  │
   └──────────────┘   │        cond          │
                      └──────────────────────┘
```

**THE distinguishing exam question — where does `continue` jump?**

```c
/* (a) for loop: continue → UPDATE step → re-test */
for (int i = 0; i < 5; i++)
{
    if (i % 2 == 0) continue;      /* jumps to i++, then re-tests */
    printf("X");                   /* runs for i = 1, 3 → prints "XX" */
}

/* (b) while loop: continue → CONDITION test (counter may be skipped!) */
int j = 0;
while (j < 5)
{
    if (j % 2 == 0) continue;      /* j++ below is SKIPPED → j stays 0 */
    printf("X");                   /* INFINITE LOOP — never prints */
    j++;
}
```

**Working code — break/continue filter (skip even, stop at 7):**

```c
#include <stdio.h>

int main(void)
{
    for (int i = 1; i <= 10; i++)
    {
        if (i % 2 == 0) continue;      /* skip the rest of THIS iteration */
        if (i == 7) break;             /* stop the whole loop */
        printf("%d ", i);
    }
    printf("\n");
    return 0;
}
/* OUTPUT: 1 3 5 */
```

**Nested-loop rules:**
- `break` exits only the **innermost** enclosing loop/switch.
- To break out of two levels you need a flag, a `goto`, or a helper-function `return`.
- Triangular inner bounds cost **n(n+1)/2** not n²: `for(j=1; j<=i; j++)` inside `for(i=1; i<=n; i++)`.

---

## 3. Arrays

### 3.1 1D Array Memory Layout

An array is one **contiguous** block; the name decays to a pointer to element 0.

```
   int a[5] = {10, 20, 30, 40, 50};     base B = 1000, sizeof(int)=4

   INDEX:      [0]     [1]     [2]     [3]     [4]
   ADDRESS:    1000    1004    1008    1012    1016
   VALUE:       10      20      30      40      50
   ├────────────────────────────────────────────────────┤
   │          ONE CONTIGUOUS BLOCK (5×4 = 20 B)         │
   └────────────────────────────────────────────────────┘

   a ≡ &a[0]          // array name decays to pointer to first element
   sizeof(a) = 20 B   // in the declaring scope
   sizeof(a)/sizeof(a[0]) = 5   // element-count idiom
```

**Working code — declaration & traversal:**

```c
#include <stdio.h>

int main(void)
{
    int a[5] = {10, 20, 30, 40, 50};     /* full init */
    int b[5] = {1, 2};                   /* partial → b[2..4] = 0  */
    int c[5] = {0};                      /* all zeros */

    printf("count = %zu\n", sizeof(a) / sizeof(a[0]));
    for (int i = 0; i < 5; i++)
        printf("%d ", a[i]);             /* prints 10 20 30 40 50 */
    printf("\nb[4] = %d\n", b[4]);       /* 0 — zero-fill guarantee */
    return 0;
}
```

**The 1D address derivation.**

**Definition.** Let the base address be $B$ (the address of element $0$) and let each element occupy $S$ bytes.

**Step 1 — distance.** Element $i$ is reached by walking past elements $0, 1, \dots, i-1$, each $S$ bytes wide:

$$\text{distance} = \underbrace{i}_{\text{steps}} \times \underbrace{S}_{\text{bytes per step}} = i \cdot S$$

**Step 2 — absolute address.**

$$\boxed{\operatorname{Addr}(a[i]) = B + i \cdot S}$$

**Step 3 — general form with lower bound $L$.** If indices start at $L \neq 0$, the walk is only $(i - L)$ elements:

$$\operatorname{Addr}(a[i]) = B + (i - L) \cdot S$$

**Worked example.** `float a[20]` at base 1024, `sizeof(float)=4`:

$$\operatorname{Addr}(a[12]) = 1024 + 12 \times 4 = 1024 + 48 = 1072$$

**1D operation complexity:**

| Operation | Best | Average | Worst | Extra space |
|---|---|---|---|---|
| Traversal | O(n) | O(n) | O(n) | O(1) |
| Access `a[i]` | O(1) | O(1) | O(1) | — |
| Insert at index k | O(1) | O(n) | O(n) | O(1) |
| Delete at index k | O(1) | O(n) | O(n) | O(1) |
| Linear search | O(1) | O(n) | O(n) | O(1) |
| Binary search (sorted) | O(1) | O(log n) | O(log n) | O(1) |
| Bubble sort | O(n) | O(n²) | O(n²) | O(1) |

### 3.2 2D Array Layout & Row-Major vs Column-Major

A 2D array `int a[R][C]` is physically **one linear block of R×C elements**. Two conventions order them.

```
   int a[3][4];

   ROW-MAJOR (C):  rows laid end-to-end
   [0][0] [0][1] [0][2] [0][3] | [1][0] [1][1] [1][2] [1][3] | [2][0] [2][1] [2][2] [2][3]
    0      1      2      3    |   4      5      6      7    |   8      9     10    11

   COLUMN-MAJOR (FORTRAN): columns laid end-to-end
   [0][0] [1][0] [2][0] | [0][1] [1][1] [2][1] | [0][2] [1][2] [2][2] | [0][3] [1][3] [2][3]
    0      1      2    |   3      4      5    |   6      7      8    |   9     10    11
```

| Property | Row-major | Column-major |
|---|---|---|
| Next block after | a whole **row** (C elements) | a whole **column** (R elements) |
| Used by | C, C++, Java | FORTRAN, MATLAB, R |
| Offset of `a[i][j]` | $i \times C + j$ | $j \times R + i$ |
| Cache-friendly loop | outer = row, inner = column | outer = column, inner = row |
| Mnemonic | "go down i rows, then right j columns" | "go down j columns, then right i rows" |

**Row-major derivation (complete).**

**Setup.** Array `a[R][C]`, base $B$, element size $S$, target element $a[i][j]$.

**Step 1 — whole rows before row $i$.** Each of the $i$ rows *above* contains exactly $C$ elements, so the number of elements preceding row $i$ is:

$$N_{\text{rows}} = i \times C$$

**Step 2 — elements inside the target row.** Row $i$ holds indices $0 \dots C-1$; column $j$ means $j$ elements to its left:

$$N_{\text{cols}} = j$$

**Step 3 — total elements before $a[i][j]$:**

$$N = i \times C + j$$

**Step 4 — multiply by the element size and add the base:**

$$\boxed{\operatorname{Addr}(a[i][j]) = B + \big( i \times C + j \big) \times S}$$

**Column-major derivation (complete).**

**Step 1 — whole columns before column $j$.** Each of the $j$ columns *before* contains exactly $R$ elements:

$$N_{\text{cols}} = j \times R$$

**Step 2 — elements above in the target column.** Column $j$ holds indices $0 \dots R-1$; row $i$ means $i$ elements above it:

$$N_{\text{rows}} = i$$

**Step 3 — total elements before $a[i][j]$:**

$$N = j \times R + i$$

**Step 4 — scale and shift:**

$$\boxed{\operatorname{Addr}(a[i][j]) = B + \big( j \times R + i \big) \times S}$$

**General form with non-zero lower bounds $L_r, L_c$ (row-major):**

$$\operatorname{Addr}(a[i][j]) = B + \Big[ (i - L_r) \times C + (j - L_c) \Big] \times S$$

**Worked example.** `int a[3][5]`, base 2000, `sizeof(int)=4`; find `a[2][3]`.

Row-major ($R=3$, $C=5$):

$$\operatorname{Addr} = 2000 + (2 \times 5 + 3) \times 4 = 2000 + 13 \times 4 = 2052$$

Column-major:

$$\operatorname{Addr} = 2000 + (3 \times 3 + 2) \times 4 = 2000 + 11 \times 4 = 2044$$

**Check:** row-major treats `a[2][3]` as element #13, column-major as element #11 — the two conventions genuinely disagree on addresses.

**Working code — row-major traversal (cache-friendly) + pointer-arithmetic equivalence:**

```c
#include <stdio.h>

int main(void)
{
    int a[3][4] = {
        { 1,  2,  3,  4},
        { 5,  6,  7,  8},
        { 9, 10, 11, 12}
    };

    for (int i = 0; i < 3; i++)          /* outer = row (CACHE-FRIENDLY) */
        for (int j = 0; j < 4; j++)      /* inner = column */
            printf("%3d", a[i][j]);
    printf("\n");

    /* pointer-arithmetic equivalence: *(*(a+i)+j) == a[i][j] */
    printf("a[1][2] = %d == %d\n", a[1][2], *(*(a + 1) + 2));
    return 0;
}
/* OUTPUT: row-major:   1  2  3  4  5  6  7  8  9 10 11 12
   and a[1][2] == 7 == 7 */
```

### 3.3 Binary Search

**Requirement: the array MUST be sorted ascending.** Each comparison discards half the remaining interval → O(log n).

```
   lo ← 0, hi ← n-1
        │
        ▼
   lo ≤ hi ? ──NO──► return -1 ("not found")
        │YES
        ▼
   mid ← lo + (hi - lo)/2
        │
        ▼
   a[mid] == key ? ──YES──► return mid
        │NO
        ▼
   a[mid] < key ? ──YES──► lo ← mid + 1  (search RIGHT half)
   else                  ─► hi ← mid - 1  (search LEFT half)
        │
        └──────────── loop again (interval halves)
```

**Why O(log n):** after $k$ comparisons the interval has $n / 2^k$ elements; you stop when $n / 2^k \le 1$, i.e. $k = \log_2 n$.

**Working code:**

```c
#include <stdio.h>

/* returns index of key in a[0..n-1] (sorted asc), or -1 */
int binarySearch(int a[], int n, int key)
{
    int lo = 0, hi = n - 1;
    while (lo <= hi)
    {
        int mid = lo + (hi - lo) / 2;      /* overflow-safe midpoint */
        if (a[mid] == key) return mid;
        else if (a[mid] < key) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}

int main(void)
{
    int a[] = {11, 22, 33, 44, 55, 66};
    int n = sizeof(a) / sizeof(a[0]);
    printf("33 → %d\n", binarySearch(a, n, 33));   /* 2 */
    printf("66 → %d\n", binarySearch(a, n, 66));   /* 5 */
    printf("40 → %d\n", binarySearch(a, n, 40));   /* -1 */
    return 0;
}
```

**Dry-run trace for key = 38 in {10,20,30,40,50,60} (n=6):**

| Step | lo | hi | mid | a[mid] | cmp | action |
|---|---|---|---|---|---|---|
| 1 | 0 | 5 | 2 | 30 | 30<38 | lo=3 |
| 2 | 3 | 5 | 4 | 50 | 50>38 | hi=3 |
| 3 | 3 | 3 | 3 | 40 | 40>38 | hi=2 |
| 4 | 3 | 2 | — | — | lo>hi | return −1 |

**Trap:** `mid = (lo + hi)/2` can overflow for huge `lo+hi`; the safe form `lo + (hi-lo)/2` cannot.

### 3.4 Bubble Sort

Adjacent swaps, n−1 passes, largest value "bubbles" to the end each pass. Early-exit flag gives O(n) best case.

```
   for pass = 0 .. n-2:
        swapped ← false
        for i = 0 .. n-2-pass:            # shrinking window
            if a[i] > a[i+1]:  swap; swapped ← true
        if !swapped: break                 # already sorted → O(n)
```

**Working code:**

```c
#include <stdio.h>

void bubbleSort(int a[], int n)
{
    for (int pass = 0; pass < n - 1; pass++)
    {
        int swapped = 0;
        for (int i = 0; i < n - 1 - pass; i++)
            if (a[i] > a[i + 1])
            {
                int t = a[i]; a[i] = a[i + 1]; a[i + 1] = t;
                swapped = 1;
            }
        if (!swapped) break;               /* sorted early → O(n) */
    }
}

int main(void)
{
    int a[] = {5, 1, 4, 2};
    int n = sizeof(a) / sizeof(a[0]);
    bubbleSort(a, n);
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
/* OUTPUT: 1 2 4 5 */
```

**Trace of {5,1,4,2}:**

| Pass | before | swaps | after |
|---|---|---|---|
| 1 | [5 1 4 2] | 5↔1, 5↔4, 5↔2 | [1 4 2 5] |
| 2 | [1 4 2 5] | 4↔2 | [1 2 4 5] |
| 3 | [1 2 4 5] | none → break | [1 2 4 5] |

**Complexity:** worst & average O(n²) (n(n−1)/2 comparisons); best O(n) with the flag on sorted input; O(1) extra space (in-place, stable).

### 3.5 Matrix Operations

**Matrix addition** — elementwise, O(R×C), both matrices same shape:

```c
#include <stdio.h>

#define R 2
#define C 3

void add(int a[R][C], int b[R][C], int out[R][C])
{
    for (int i = 0; i < R; i++)
        for (int j = 0; j < C; j++)
            out[i][j] = a[i][j] + b[i][j];
}

int main(void)
{
    int a[R][C] = {{1, 2, 3}, {4, 5, 6}};
    int b[R][C] = {{6, 5, 4}, {3, 2, 1}};
    int out[R][C];
    add(a, b, out);
    for (int i = 0; i < R; i++)
    {
        for (int j = 0; j < C; j++) printf("%3d", out[i][j]);
        printf("\n");
    }
    return 0;
}
/* OUTPUT:  7  7  7
            7  7  7 */
```

**Matrix multiplication — the classic triple loop.** $C_{m\times p} = A_{m\times n} \cdot B_{n\times p}$. Each output element $c[i][j]$ is the dot product of row $i$ of $A$ with column $j$ of $B$:

$$c[i][j] = \sum_{k=0}^{n-1} a[i][k] \cdot b[k][j]$$

**ASCII flow of the dot-product kernel:**

```
        B column j           A row i
      ┌──┬──┬──┬──┐        ┌──────────┐
      │b[0][j]│  │        │a[i][0]  ──┐ multiply-add
      ├──┼──┼──┼──┤        ├──────────┤
      │b[1][j]│  │        │a[i][1]  ──┤
      ├──┼──┼──┼──┤        ├──────────┤
      │b[2][j]│  │        │a[i][2]  ──┘──► c[i][j]
      └──┴──┴──┴──┘        └──────────┘
           k = 0..n-1
```

```c
#include <stdio.h>

void matMul(int A[2][3], int B[3][2], int C[2][2])
{
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
        {
            C[i][j] = 0;
            for (int k = 0; k < 3; k++)      /* dot product over shared dim n=3 */
                C[i][j] += A[i][k] * B[k][j];
        }
}

int main(void)
{
    int A[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int B[3][2] = {{7, 8}, {9, 10}, {11, 12}};
    int C[2][2];
    matMul(A, B, C);
    for (int i = 0; i < 2; i++)
    {
        for (int j = 0; j < 2; j++) printf("%4d", C[i][j]);
        printf("\n");
    }
    return 0;
}
/* OUTPUT:   58   64
            139  154   */
```

**Verify by hand for C[0][0]:** 1·7 + 2·9 + 3·11 = 7 + 18 + 33 = **58**. ✓

**Matrix operation complexity:**

| Operation | Shape | Complexity |
|---|---|---|
| Addition / subtraction | both m×n | O(m·n) |
| Scalar multiply | m×n | O(m·n) |
| Transpose (in-place) | m×n → n×m | O(m·n) |
| Multiplication | (m×n)·(n×p) | **O(m·n·p)** — cubic for square: O(n³) |
| Strassen (advanced) | n×n | O(n^2.807) |

---

## 4. User-Defined Functions

### 4.1 Call by Value vs. Call by Reference

C is **strictly call-by-value**: parameters are *copies*. "Call by reference" is **simulated** by passing addresses and dereferencing.

**The call sequence (what the hardware does):**

```
   main()                                     swap(&p, &q)
   ┌───────────────────────┐
   │ int p=2, q=3;         │
   │ swap(&p, &q);         │
   └──────────┬────────────┘
              │ 1. push return address
              │ 2. push COPIES of the arguments:
              │      x = address of p,  y = address of q
              │ 3. jump to swap's code
              ▼
   swap frame ┌───────────────────────┐
              │ return address        │
              │ x = &p,  y = &q       │  ← the ADDRESSES are the values
              │ t = *x = 2            │
              │ *x = *y  →  p = 3     │  ← dereference writes the CALLER's memory
              │ *y = t   →  q = 2     │
              └───────────────────────┘
              │ 4. pop frame, resume main; p=3, q=2
```

**Working code — the canonical demo:**

```c
#include <stdio.h>

void byValue(int v) { v = 100; }          /* changes the COPY only */
void byPointer(int *p) { *p = 100; }      /* writes through the address */

int main(void)
{
    int x = 1, y = 1;
    byValue(x);      /* x unchanged */
    byPointer(&y);   /* y changed  */
    printf("x = %d, y = %d\n", x, y);
    return 0;
}
/* OUTPUT: x = 1, y = 100 */
```

**Decision table:**

| | Call by value | Call by pointer (fake-by-ref) |
|---|---|---|
| What is copied | the value itself | the **address** (4/8 B) |
| Caller's variable changed? | **No** | **Yes** (via `*p`) |
| Cost for a big struct | copies whole struct | copies only the pointer |
| Memory visible | callee's copy | caller's original |
| Use when | computing with scalars | modifying caller data, avoiding copies |

**Array parameters are always by-pointer** — `int a[]` and `int *a` are the same parameter. That is why array *elements* get modified but a bare scalar never does, and why you must pass `n` separately (`sizeof` in the callee only sees a pointer).

### 4.2 Recursion & Stack Execution

Recursion = a function calling itself on a *smaller* problem until the **base case** stops it. Each call pushes a fresh **activation record** (frame) onto the stack.

**Stack execution trace for `fact(4)` (step-by-step):**

```
   int fact(int n)
   {
       if (n <= 1) return 1;
       return n * fact(n - 1);   /* multiply waits for the child → NOT tail */
   }

   CALL PHASE (push frames down the stack):
   fact(4) → fact(3) → fact(2) → fact(1)     stack depth = 4

   STACK (during deepest call):
   ┌─────────────────────────┐
   │ fact(1) frame: n=1      │ ← top (active)
   │ fact(2) frame: n=2      │   waiting for fact(1)
   │ fact(3) frame: n=3      │   waiting for fact(2)
   │ fact(4) frame: n=4      │   waiting for fact(3)
   │ main                    │
   └─────────────────────────┘

   RETURN PHASE (pop frames, bubble values up):
   fact(1)=1 → fact(2)=2*1=2 → fact(3)=3*2=6 → fact(4)=4*6=24
```

**Working code — factorial, power, Fibonacci:**

```c
#include <stdio.h>

long fact(int n)                    /* linear recursion, O(n) time, O(n) stack */
{
    if (n <= 1) return 1;
    return n * fact(n - 1);
}

long power(int b, int e)            /* O(log e) via squaring  */
{
    if (e == 0) return 1;
    long half = power(b, e / 2);    /* compute once, reuse twice */
    return (e % 2 == 0) ? half * half : b * half * half;
}

long fib(int n)                     /* tree recursion, O(2^n) — EXPONENTIAL */
{
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2); /* two calls per frame */
}

int main(void)
{
    printf("fact(5)  = %ld\n", fact(5));   /* 120  */
    printf("2^10     = %ld\n", power(2, 10)); /* 1024 */
    printf("fib(10)  = %ld\n", fib(10));   /* 55   */
    return 0;
}
```

**Tail recursion — the optimization-relevant variant.** The recursive call must be the **very last** operation (nothing waits after it):

```c
long factTail(int n, long acc)      /* acc accumulates the product going DOWN */
{
    if (n <= 1) return acc;
    return factTail(n - 1, acc * n);/* call IS the last op → compiler can
                                       reuse the frame (tail-call optimization)
                                       → O(1) stack instead of O(n) */
}
```

Contrast: `n * fact(n-1)` is **not** tail — the `n *` runs *after* the child returns, so the frame must survive. That one detail is an entire exam question.

**Recursion-type table:**

| Type | Definition | Time | Stack | Example |
|---|---|---|---|---|
| Linear | one self-call | O(n) | O(n) | factorial, countdown |
| Tail | self-call is last op | O(n) | **O(1) w/ TCO** | factorial-with-accumulator |
| Tree | two+ self-calls | O(2ⁿ) | O(n) | naive Fibonacci |
| Mutual | A→B→A | O(n) | O(n) | even/odd checkers (needs prototypes) |

**Stack-overflow math:**

$$\text{max depth} \approx \frac{\text{stack size}}{\text{frames per call}}$$

e.g. 8 MiB stack, 64-byte frames → $8 \times 2^{20} / 64 = 131{,}072$ frames deep. Beyond that: **stack overflow** (crash). Recursion elegance vs. stack budget — that is the engineering trade.

### 4.3 Storage Classes

**The four storage classes + scope/lifetime matrix:**

| Class | Where it lives | Lifetime | Scope | Default value |
|---|---|---|---|---|
| `auto` (default for locals) | stack | function call | block | **garbage** |
| `static` (local) | data segment | **entire program** | still block-local | zero |
| `static` (file/global) | data segment | program | file only | zero |
| `register` (hint) | CPU register (if possible) | function call | block | garbage |
| `extern` | external definition | program | files that declare it | zero |

**Working code — every class in action:**

```c
#include <stdio.h>

extern int g;               /* extern: defined elsewhere (or later in file) */
int g = 5;                  /* file-scope global: DATA segment, zero-init'd */

static int file_local = 1;  /* static file scope: visible only in this file */

int counter(void)
{
    static int c = 0;       /* static local: init ONCE, keeps value between calls */
    return ++c;             /* → 1, 2, 3, ...  */
}

int main(void)
{
    int auto_local = 0;              /* auto (default): stack, garbage if uninit */
    register int r = 10;             /* register: hint to keep in a CPU register */
    for (int i = 0; i < 3; i++)
        printf("counter() = %d\n", counter());
    printf("g = %d, file_local = %d, r = %d\n", g, file_local, r);
    return 0;
}
/* OUTPUT:
   counter() = 1
   counter() = 2
   counter() = 3
   g = 5, file_local = 1, r = 10 */
```

**Rule roundup:**
- `static` local: initialized **once** at program start, survives all calls, retains value — the accumulator idiom.
- `static` file-scope object: **internal linkage** — invisible outside this `.c` file (encapsulation in C).
- `extern`: "defined elsewhere" — enables multi-file programs; `extern int g;` alone declares, does not define.
- `register`: a *hint*; modern compilers ignore it — `&x` is illegal on a register variable.
- **Uninitialized locals are garbage** (stack), uninitialized globals/statics are **0** (BSS).

**Default-initialization trap (three different answers):**

| Declared how | Initial value |
|---|---|
| `int x;` (local/auto) | **garbage** |
| `int g;` (global/BSS) | **0** |
| `static int s;` (any) | **0** |
| `int *p = malloc(n);` | **garbage** |
| `int *p = calloc(n, size);` | **0** |

---

## APPENDIX: One-Page Formula & Trap Sheet

| Topic | Rule / Formula | Trap |
|---|---|---|
| Compile stages | preprocess → compile → assemble → link | undefined ref = linker; syntax = compiler; missing header = preprocessor |
| Memory regions | Text (code), Data (init'd), BSS (zeroed), Heap (up), Stack (down) | uninit locals garbage ≠ globals 0 |
| malloc vs calloc | malloc garbage / calloc zero | every malloc needs exactly one free |
| Precedence | `()` > unary > `* / %` > `+ -` > relational > `==` > `&&` > `\|\|` > `?:` > `=` > `,` | `==` vs `=`; `&&`/`\|\|` short-circuit |
| Pre/post inc | `i++` returns old, `++i` returns new | never `x = i++ + i++` (UB) |
| Dangling else | else binds to nearest unmatched if | brace to force pairing |
| switch | integral expr; case labels const; **fall-through without break** | float/string not allowed |
| do-while | exit-controlled, min 1 run, **semicolon after** | semicolon required |
| for | init → test → body → update | `i < n` = n runs; `i <= n` = n+1 |
| continue (for) | jumps to **update** then test | in while, continue can skip counter → infinite loop |
| break | exits innermost loop/switch only | two-level escape needs goto/flag |
| 1D address | $B + i \cdot S$ | zero-based index |
| 2D row-major | $B + (i \times C + j) \times S$ | C is row-major |
| 2D column-major | $B + (j \times R + i) \times S$ | FORTRAN |
| Array param | `int a[]` ≡ `int *a` | callee's sizeof = pointer size — pass n |
| Binary search | O(log n), sorted only, mid = lo+(hi−lo)/2 | `(lo+hi)/2` can overflow |
| Bubble sort | O(n²) worst, O(n) best w/ flag | stable, in-place |
| MatMul | O(m·n·p); square O(n³); $c_{ij}=\sum_k a_{ik}b_{kj}$ | inner loop = dot product |
| Call by value | copies — caller's scalar never changes | pass address to modify |
| Tail recursion | call is last op → O(1) stack w/ TCO | `n * fact(n−1)` is NOT tail |
| Storage classes | auto=stack/garbage, static=program/0, register=hint, extern=elsewhere | `static` local keeps value between calls |
| Stack overflow | depth ≈ stack size ÷ frame size | 8 MiB / 64 B ≈ 131k frames |

## CROSS-REFERENCES

- Related modules: [[module-1-spm-c-basics]] (compile pipeline & memory layout) · [[module-2-program-control-functions]] (control flow drills) · [[module-3-arrays]] (array operations & address formulas) · [[module-4-user-defined-functions]] (recursion, storage classes) · [[01-Areas/Programming/cs50/week-2-arrays]] · [[01-Areas/Programming/cs50/week-3-algorithms]] · [[01-Areas/Programming/programming-cs-fundamentals]]