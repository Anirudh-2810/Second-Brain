---
module: "SPM"
topic: "Module 4: User-Defined Functions — Call Semantics, Parameter Passing, Recursion & Function Pointers"
tags: [c-programming, functions, user-defined-functions, pass-by-value, pass-by-reference, stack-frame, activation-record, recursion, tail-recursion, mutual-recursion, tree-recursion, function-pointers, varargs, inline, global-variables, static]
last_updated: "2026-08-19"
prerequisites: ["Module 3: Introduction to Arrays", "Pointers (dereference & address-of)", "Module 2: Program Control Functions"]
---

# Module 4: User-Defined Functions

> The unit of modularity in C: declarations, definitions, prototypes, and the exact mechanics of a function call — what goes on the stack, how parameters are passed (by value, always), and how we fake pass-by-reference with pointers. Covers recursion in full depth (tail, tree, mutual recursion, and stack-overflow limits) plus the power tools: function pointers and variadic functions. Written for beginners: the call sequence is drawn step by step, recursion is de-mystified with a full stack trace, and every trap (returning a pointer to a local, prototype mismatches) gets its own callout.

---

## Table of Contents

1. [Conceptual Architecture & ASCII Flowcharts](#1-conceptual-architecture--ascii-flowcharts)
2. [Code Implementation & Memory Analysis](#2-code-implementation--memory-analysis)
3. [High-Yield Exam Problems & Worked Code Drills](#3-high-yield-exam-problems--worked-code-drills)
4. [Real-World System Applications](#4-real-world-system-applications)
5. [Appendix: Formula & Data Quick Reference](#appendix-formula--data-quick-reference)

---

## 1. CONCEPTUAL ARCHITECTURE & ASCII FLOWCHARTS

### 1.0 Why Functions? — Beginner Foundation

A **function** is a named block of code you can *call* from anywhere, passing inputs (**arguments**) and receiving back a **return value**. Three benefits you'll be quizzed on:

1. **Modularity / Decomposition** — break a 1000-line problem into readable units.
2. **Reusability / DRY** — write once, call many times (the `printf` you use every day is a function).
3. **Maintainability** — fix a bug in one function, not in 50 duplicated copies.

**Four pieces of C function anatomy (memorize the names):**

```c
#include <stdio.h>

/* (1) PROTOTYPE / DECLARATION — tells the compiler the signature. Optional
       if definition appears before first call. */
int add(int a, int b);

/* (2) DEFINITION — the actual body */
int add(int a, int b)      /* (3) return type + parameters */
{
    int sum = a + b;       /* (4) body with a local variable */
    return sum;
}

int main(void)
{
    int r = add(3, 4);     /* function CALL — 3, 4 are ARGUMENTS */
    printf("%d\n", r);
    return 0;
}
```

**Beginner rules:**
- A function must be **declared or defined before its first call** (otherwise implicit-declaration warnings/errors).
- `void` return type = returns nothing; `void` parameter list = takes no arguments (in C, `f()` technically means "unspecified args" — write `f(void)` to be strict).
- `return` stops execution of the function immediately and hands back the value. In a `void` function you may use bare `return;`.
- Parameters are **local copies** — the caller's variables are never touched (this is pass-by-value, Section 1.2).

### 1.1 The Call Sequence — What Really Happens

```
   main()
   ┌─────────────────────────────┐
   │ int r = add(3, 4);          │
   └──────────────┬──────────────┘
                  │  1. Push return address
                  │  2. Push arguments (or their copies)   ← pass-by-value
                  │  3. Transfer control (jump to add's code)
                  ▼
   add's STACK FRAME (activation record)
   ┌─────────────────────────────┐
   │ return address  (back to    │
   │                main line)   │
   │ parameters:    a = 3, b = 4 │
   │ local:         sum = 7      │
   └──────────────┬──────────────┘
                  │  4. compute, load result into a register
                  │  5. pop frame, jump back to return address
                  ▼
   main() continues with r = 7
```

**Step-by-step (plain English):**
1. main suspends; CPU pushes the **return address** (where to resume).
2. **Copies** of the arguments are placed on the stack.
3. Control jumps into `add`, which allocates its **frame** (parameters + locals).
4. `add` computes, loads `7` into the return register.
5. The frame is popped; control returns to main; `r` gets `7`.

**Key consequences (exam gold):**
- Changing a parameter inside a function **never** changes the caller's variable — you're editing a *copy*.
- **Never return a pointer to a local variable** — the frame is destroyed on return, and the pointer dangles (the "returning pointer to stack" bug, Section 2.3).
- Every call (recursive or not) builds a **new frame** on the stack. Deep recursion = tall stack = overflow risk.

### 1.2 Pass by Value vs. "Pass by Reference" (via Pointers)

C is **strictly pass-by-value**. The "reference" behavior is *simulated* by passing the **address** of a variable:

```c
void swap(int *x, int *y)   /* receives ADDRESSES (the values are addresses) */
{
    int t = *x;             /* dereference to reach the caller's memory */
    *x = *y;
    *y = t;
}
/* call: swap(&p, &q);   -- pass the ADDRESS of p and q */
```

| | Pass by value | Pass by pointer (fake-by-reference) |
|---|---|---|
| What's copied | the value itself | the **address** of the variable |
| Caller's variable changed? | **No** | **Yes** (via dereference) |
| Cost | copies whole struct (expensive) | copies 4/8 bytes pointer (cheap) |
| Memory visible | callee's copy | caller's original memory |
| Why use | simple scalar computation | modify caller's data; avoid big copies |

**Beginner intuition:** pass-by-value gives the function a *photocopy*; pass-by-pointer gives it the *keys to the office* — it can walk in and change the original.

**Also changed through pointers (module 3):** an array parameter `int a[]` is really `int *a` — the function sees the array *by pointer*, so it can modify the caller's array elements even though the pointer itself was passed by value.

### 1.3 Storage Classes — Where Things Live

| Storage class | Storage | Lifetime | Scope | Default value |
|---|---|---|---|---|
| `auto` (default for locals) | stack | function call | block | **garbage** (uninitialized!) |
| `static` (local) | data segment | **entire program** | still block-local (only that function) | zero |
| `static` (global/file) | data segment | program | **file only** (internal linkage) | zero |
| `global` (file-scope) | data segment | program | whole file (extern-linking) | zero |
| `register` (hint) | register (if available) | function call | block | garbage |
| `extern` | external | program | file(s) that declare it | zero |

**Beginner traps:**
- **Uninitialized local = garbage**, not 0. `int x; printf("%d", x);` is undefined — may print anything.
- **`static` local keeps its value between calls** and initializes to 0 once:
  ```c
  int counter(void) { static int c = 0; return ++c; }   /* 1,2,3,... */
  ```
- Use `static` for locals when you need a value that survives across calls; use it for file-scope objects to limit them to the file.

### 1.4 Recursion — The Self-Calling Function

**Recursion** = a function that calls itself, solving a smaller instance of the same problem until it hits a **base case**. Two mandatory parts:

1. **Base case** — the smallest problem, answered directly (stops the recursion).
2. **Recursive step** — break the problem into a smaller version, call yourself, combine.

**Flowchart — factorial(n):**

```
   int fact(int n)
   fact(4)
      │
      ├─ base case?  n == 0 or n == 1  →  return 1
      │
      └─ else  return n * fact(n-1)
                   │
                   ▼  (call stack grows DOWN the stack)
      fact(3) → 3 * fact(2) → 2 * fact(1) → 1 * fact(0) → 1
      │          │            │            │            │
      ▼          ▼            ▼            ▼            ▼
     4*6=24     3*2=6        2*1=2        1*1=1        1
        ▲        ▲            ▲            ▲            ▲
        └─ unwind (returns bubble back UP)
```

**The classic stack trace for `fact(4)`:**

```
   CALL:  fact(4) → fact(3) → fact(2) → fact(1) → fact(0)  [deepest]
   RETURN:      4*6=24 ← 3*2=6 ← 2*1=2 ← 1*1=1 ← 1         [unwinding]
```

**Why you never actually "recalculate" the same branch in factorial:** each call computes its own multiplication only once the child returns — the total work is O(n) time, O(n) stack space.

### 1.5 Recursion Types — Comparison Table

| Type | Definition | Stack depth | Example | Use / warning |
|---|---|---|---|---|
| **Linear recursion** | one recursive call per frame | O(n) | factorial, power | simplest to reason about |
| **Tail recursion** | the recursive call is the **very last** operation | O(n) naive; **O(1)** with compiler optimization (TCO) | countdown | can be optimized into a loop |
| **Tree recursion** | two+ recursive calls per frame | O(n) depth, O(2ⁿ) work | Fibonacci (naive) | exponential — avoid without memoization |
| **Mutual recursion** | A calls B, B calls A | O(n) | even/odd checkers | needs prototypes before use |

**The tail-recursion detail that wins marks:** `fact` *naive* is **not** tail-recursive (the `n *` multiply happens *after* the call returns — the frame must survive). A **tail** version passes the running product *down*:

```c
int factTail(int n, int acc)          /* acc = accumulator */
{
    if (n == 0) return acc;           /* base case */
    return factTail(n - 1, acc * n);  /* LAST operation = the call itself */
}
```

Because nothing remains after the call, a smart compiler can **reuse the same frame** (tail-call optimization), making it O(1) stack. No `n *` waits for a return — that's the whole point.

### 1.6 Function Pointers & Variadic Functions — The Power Tools

**Function pointer** = a variable that *holds the address of a function*, letting you pass behavior around:

```c
int add(int a, int b) { return a + b; }
int mul(int a, int b) { return a * b; }

/* type:  int (*)(int, int)  → read right-to-left: pointer to a function
         taking (int,int) and returning int */
int apply(int (*fn)(int, int), int x, int y)
{
    return fn(x, y);        /* call through the pointer */
}

int main(void)
{
    printf("%d\n", apply(add, 3, 4));   /* prints 7 */
    printf("%d\n", apply(mul, 3, 4));   /* prints 12 */
    return 0;
}
```

**Beginner notes:**
- **Read the declaration right-to-left:** `int (*fn)(int,int)` → fn is a pointer to a function returning int taking two ints. The parentheses around `*fn` are mandatory — without them `int *fn(int,int)` means a function returning `int*`.
- This is the C mechanism behind callback tables, `qsort`'s comparator, and dispatch tables.

**Variadic function (`...`)**: a function that takes a *variable number* of arguments (`printf`, `scanf`). Uses `<stdarg.h>`:

```c
#include <stdio.h>
#include <stdarg.h>

double average(int count, ...)      /* count = how many numbers follow */
{
    va_list ap;
    va_start(ap, count);
    double sum = 0;
    for (int i = 0; i < count; i++)
        sum += va_arg(ap, double);   /* each call pulls the next argument */
    va_end(ap);
    return count ? sum / count : 0;
}
```

**Safety warning (exam-relevant):** varargs are *untyped* — the compiler can't check that you pass a `double` where you declared one. That's why `printf("%d", 3.14)` misbehaves at runtime. Prefer fixed-signature functions unless you really need varargs.

---

## 2. CODE IMPLEMENTATION & MEMORY ANALYSIS

### 2.1 Pass-by-Value vs. Pointer — Full Demo

```c
#include <stdio.h>

void modify(int v, int *p)   /* v = copy; p = address of original */
{
    v = 100;        /* changes only the COPY */
    *p = 100;       /* dereferences p → changes the CALLER's variable */
}

int main(void)
{
    int x = 1, y = 1;
    modify(x, &y);
    printf("x = %d, y = %d\n", x, y);
    return 0;
}
```

**Output:**
```
x = 1, y = 100
```

**Memory diagram of the frames at the moment `*p = 100` executes:**

```
   main frame                    modify frame
   ┌──────────────┐              ┌──────────────┐
   │  x = 1       │              │  v = 1 (copy)│
   │  y = 100     │←─p (points)  │  p = &y      │
   └──────────────┘              └──────────────┘
```

`x` never changes because `v` was a *copy*; `y` changes because `p` points *at* y.

### 2.2 Recursion — Factorial & Fibonacci, Side by Side

```c
#include <stdio.h>

/* linear recursion — O(n) time, O(n) stack */
long fact(int n)
{
    if (n <= 1) return 1;
    return n * fact(n - 1);
}

/* tree recursion — O(2^n) time, O(n) stack. Exponential! */
long fib(int n)
{
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}

/* tail recursion with accumulator — optimizable to O(1) stack */
long factTail(int n, long acc)
{
    if (n <= 1) return acc;
    return factTail(n - 1, acc * n);
}

int main(void)
{
    printf("fact(5) = %ld\n", fact(5));            /* 120 */
    printf("factTail(5,1) = %ld\n", factTail(5, 1));/* 120 */
    printf("fib(6) = %ld\n", fib(6));              /* 8 */
    return 0;
}
```

**Output:**
```
fact(5) = 120
factTail(5,1) = 120
fib(6) = 8
```

**Why fib is O(2ⁿ):** each call spawns *two* children, and `fib(1)` is recomputed ~8 times for n=6. The call tree for fib(6) looks like a binary tree with 2⁶-ish leaves. This is the classic motivation for **memoization** (storing computed results).

### 2.3 The Dangling Pointer Bug — Never Do This

```c
int *bad(void)
{
    int local = 42;      /* lives in THIS frame */
    return &local;       /* BUG: frame is destroyed when we return! */
}
int main(void)
{
    int *p = bad();
    printf("%d\n", *p);  /* undefined behavior — dangling pointer */
    return 0;
}
```

**Why it's broken:** when `bad` returns, its stack frame is popped. The address in `p` may still contain `42` (the memory isn't erased immediately), but it's been recycled and *any* subsequent call (even `printf`) can overwrite it. **Undefined behavior** — anything may print. The fix: allocate with `malloc` (heap — survives), or return a `static` local, or take an output pointer parameter:

```c
void good(int *out) { *out = 42; }   /* write through the caller's pointer */
```

### 2.4 Function Pointer Table + Variadic — Production Example

```c
#include <stdio.h>
#include <stdarg.h>

int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }
int mul(int a, int b) { return a * b; }

int sumAll(int count, ...)   /* varargs: sum of 'count' ints */
{
    va_list ap; va_start(ap, count);
    int total = 0;
    for (int i = 0; i < count; i++) total += va_arg(ap, int);
    va_end(ap);
    return total;
}

int main(void)
{
    /* dispatch table: an array of function pointers */
    int (*ops[3])(int, int) = {add, sub, mul};
    const char *names[3] = {"add", "sub", "mul"};
    for (int i = 0; i < 3; i++)
        printf("%s(10,4) = %d\n", names[i], ops[i](10, 4));

    printf("sumAll(4, 1,2,3,4) = %d\n", sumAll(4, 1, 2, 3, 4));
    return 0;
}
```

**Output:**
```
add(10,4) = 14
sub(10,4) = 6
mul(10,4) = 40
sumAll(4, 1,2,3,4) = 10
```

**Read `int (*ops[3])(int,int)` right-to-left:** ops is an array of 3 pointers to functions returning int taking (int,int). This pattern drives plugin systems, menu handlers, and parser dispatch.

---

## 3. HIGH-YIELD EXAM PROBLEMS & WORKED CODE DRILLS

---

### Problem 1: Parameter Passing — By Value vs. By Pointer

**Problem.** Predict the output:

```c
void f(int a, int *b)
{
    a = a + 1;
    *b = *b + 1;
}
int main(void)
{
    int x = 5, y = 5;
    f(x, &y);
    printf("%d %d\n", x, y);
    return 0;
}
```

---

**Solution:**

**Step 1 — by value.** `a` is a copy; `a = a+1` changes the copy only → x stays 5.

**Step 2 — by pointer.** `*b = *b + 1` dereferences y's address → y becomes 6.

$$\boxed{x = 5,\ y = 6 \quad \Rightarrow \quad \text{output: } 5\ 6}$$

---

### Problem 2: Recursion Output — Nested Calls

**Problem.** Predict the output:

```c
int mystery(int n)
{
    if (n <= 0) return 0;
    printf("%d ", n);
    return mystery(n - 1) + mystery(n - 2);
}
int main(void)
{
    printf("\n%d\n", mystery(3));
    return 0;
}
```

---

**Solution — trace the call tree:**

**Step 1 — build the tree.**

```
                    mystery(3)
                   /          \
              mystery(2)     mystery(1)
              /        \         |
         mystery(1)   mystery(0) mystery(0)
           /      \
      mystery(0)  mystery(-1)
```

**Step 2 — depth-first (left first) print order.** Each call prints `n` when n > 0:

```
mystery(3) prints 3 → calls mystery(2) → prints 2 → calls mystery(1) → prints 1
→ calls mystery(0) (prints nothing) → calls mystery(-1) (nothing)
→ back to mystery(2)'s right child mystery(0) (nothing)
→ back to mystery(3)'s right child mystery(1) → prints 1 → children print nothing.
```

$$\boxed{\text{Output: } 3\ 2\ 1\ 1 \qquad \text{final return value } 0\ \text{(all base cases return 0)}}$$

**Beginner note:** recursion prints in **pre-order** (print → recurse) — a common exam trap. Reverse the order of print and call and you'd get 1 1 2 3 (post-order).

---

### Problem 3: Static Local Variables — Accumulator

**Problem.** Predict the output:

```c
int next(void)
{
    static int x = 5;   /* initialized ONCE, survives calls */
    return x++;
}
int main(void)
{
    printf("%d ", next());
    printf("%d ", next());
    printf("%d\n", next());
    return 0;
}
```

---

**Solution:**

**Step 1 — `static` init happens once** (at program start), x = 5.

**Step 2 — `return x++` is post-increment:** returns the *old* x, then increments.

| Call | x before | returns | x after |
|---|---|---|---|
| 1st | 5 | 5 | 6 |
| 2nd | 6 | 6 | 7 |
| 3rd | 7 | 7 | 8 |

$$\boxed{\text{Output: } 5\ 6\ 7}$$

(If it were `++x`, output would be 6 7 8. Post- vs. pre-increment in a return is a classic.)

---

### Problem 4: Function Pointers — Qsort-Style Callback

**Problem.** Predict the output:

```c
#include <stdio.h>
int inc(int x) { return x + 1; }
int sq(int x)  { return x * x; }
int twice(int (*f)(int), int v) { return f(f(v)); }
int main(void)
{
    printf("%d ", twice(inc, 3));
    printf("%d\n", twice(sq, 3));
    return 0;
}
```

---

**Solution:**

**Step 1 — `twice(inc,3)`:** `f(f(3))` = `inc(inc(3))` = `inc(4)` = **5**.

**Step 2 — `twice(sq,3)`:** `sq(sq(3))` = `sq(9)` = **81**.

$$\boxed{\text{Output: } 5\ 81}$$

---

### Problem 5: Tail Recursion vs. Non-Tail

**Problem.** Convert the following to tail recursion and trace the accumulator values for n = 4:

```c
int powr(int b, int e)         /* b^e */
{
    if (e == 0) return 1;
    return b * powr(b, e - 1); /* multiply happens AFTER the call → NOT tail */
}
```

---

**Solution — tail version:**

```c
int powrTail(int b, int e, int acc)
{
    if (e == 0) return acc;
    return powrTail(b, e - 1, acc * b);  /* call IS the last operation */
}
```

**Trace (b = 2, e = 4, acc = 1):**

| Call | e | acc | next call |
|---|---|---|---|
| powrTail(2, 4, 1) | 4 | 1 | powrTail(2, 3, 2) |
| powrTail(2, 3, 2) | 3 | 2 | powrTail(2, 2, 4) |
| powrTail(2, 2, 4) | 2 | 4 | powrTail(2, 1, 8) |
| powrTail(2, 1, 8) | 1 | 8 | powrTail(2, 0, 16) |
| powrTail(2, 0, 16) | 0 | 16 | **return 16** |

$$\boxed{2^4 = 16 \quad \text{and, with tail-call optimization, the stack stays O(1)}}$$

---

### Problem 6: Stack-Overflow Depth Estimate

**Problem.** On a system with an 8 MiB default stack and an activation record of 64 bytes per recursion frame, roughly how deep can a naive recursive `fact` go before overflowing?

---

**Solution:**

$$\text{Max depth} \approx \frac{\text{stack size}}{\text{frame size}} = \frac{8 \times 2^{20}\ \text{bytes}}{64\ \text{bytes/frame}} = \frac{8,388,608}{64} = 131,072\ \text{frames}$$

$$\boxed{\approx 131\ \text{thousand frames before stack overflow}}$$

**Beginner takeaway:** recursion is clean but eats a frame per level — an O(1)-stack tail recursion or an explicit loop avoids the limit entirely. This is *why* the syllabus pushes tail recursion and iterative rewrites.

---

## 4. REAL-WORLD SYSTEM APPLICATIONS

| Principle | Real-World Practice |
|---|---|
| **Modularity / decomposition** | OS kernel subsystems (scheduler, memory mgr, VFS) as function libraries |
| **Pass by pointer** | Struct-heavy code (passing big structs by address), `scanf`'s address-of-args, in-place sorting (`qsort`) |
| **Storage classes / static** | File-local helpers in a `.c` module; static locals as counters in drivers (packet counters) |
| **Recursion** | Directory tree traversal, expression tree evaluation (compilers), parsing nested JSON/XML, divide-and-conquer (quicksort/mergesort), Tower of Hanoi |
| **Tail recursion / TCO** | Functional-style pipelines in embedded C (loop-equivalent), compilers turning recursion into iteration |
| **Function pointers** | Signal handlers, `qsort` comparators, driver callback tables, interrupt service routine dispatch, plugin registries |
| **Variadic functions** | `printf`/`scanf` family, logging macros with format strings, error-reporting APIs |
| **Stack frames** | Any crash dump / backtrace is literally a walk of the frame chain |
| **Dangling-pointer risk** | The reason for static-analysis warnings (e.g., GCC `-Wreturn-local-addr`) and Rust's ownership model |

---

## APPENDIX: Formula & Data Quick Reference

| Concept | Rule / Formula | Gotcha |
|---|---|---|
| Declaration | `returnType name(parms);` | declare/define before first call |
| Call | `name(args);` | args are **copied** |
| Pass by value | copy of value | callee can't change caller's scalar |
| Pass by pointer | copy of address | callee CAN change caller's data |
| Array param | `int a[]` ≡ `int *a` | size not conveyed — pass n |
| Return type | `void` = none | `main` returns int status |
| Local uninitialized | garbage | never assume 0 |
| `static` local | lives whole program | init once, keeps value across calls |
| Linear recursion | T = O(n), S = O(n) | fine for shallow depth |
| Tree recursion | fib naive T = O(2ⁿ) | recomputes subtrees; use memoization |
| Tail recursion | call is last op | TCO → O(1) stack |
| Mutual recursion | A→B→A | declare prototypes first |
| Function pointer | `int (*fp)(int,int)` | parens around `*fp` mandatory |
| Variadic | `<stdarg.h>` va_list | untyped — no compile-time checks |
| Stack overflow depth | stack size ÷ frame size | 8 MiB / 64 B ≈ 131k frames |

## CROSS-REFERENCES

- Related modules: [[module-2-program-control-functions]] (loops vs. recursion, break/return) · [[module-3-arrays]] (array params = pointers) · [[module-1-spm-c-basics]] (memory layout: stack vs. heap) · [[01-Areas/Programming/cs50/week-3-algorithms]] (recursion in context)