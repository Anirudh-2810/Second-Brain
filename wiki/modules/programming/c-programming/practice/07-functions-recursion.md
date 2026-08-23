---
module: "c-programming"
topic: "Solved Practice — Functions & Recursion (6 problems)"
tags: [programming, c, practice, solved, functions, recursion, exam]
last_updated: "2026-08-19"
---

# 07 · Functions & Recursion — 6 Solved Problems

> Function questions test prototypes, pass-by-value vs. by-address, and recursion traces. The recursion ones need careful **stack-trace** work.

---

## Problem 7.1 — Pass by value (predict the output)

```c
#include <stdio.h>
void change(int x) {
    x = 100;
}
int main() {
    int a = 5;
    change(a);          // does main's a change?
    printf("%d\n", a);
    return 0;
}
```

**<details><summary>Solution</summary>**

Output: `5`

| Call | What happens |
|---|---|
| `change(a)` | `a`'s **value 5 is copied** into the parameter `x` |
| `x = 100` | only the copy changes |
| back in `main` | `a` is still `5` |

**Rule:** C passes **by value** by default — the function operates on a *copy*. To change the original, pass the **address** (next problem).

</details>

---

## Problem 7.2 — Pass by address (predict the output)

```c
#include <stdio.h>
void change(int *x) {
    *x = 100;
}
int main() {
    int a = 5;
    change(&a);         // pass the ADDRESS of a
    printf("%d\n", a);
    return 0;
}
```

**<details><summary>Solution</summary>**

Output: `100`

| Call | What happens |
|---|---|
| `change(&a)` | the **address** of `a` is passed |
| `*x = 100` | dereference → write 100 into that address |
| back in `main` | `a`'s memory was modified → `100` |

**Why `scanf("%d", &a)` works:** exactly this — `scanf` receives the address and writes into your variable.

</details>

---

## Problem 7.3 — Swap using pointers (write the program)

Write a function `swap` that actually exchanges two values in `main`.

**<details><summary>Solution</summary>**

```c
#include <stdio.h>
void swap(int *x, int *y) {
    int t = *x;
    *x = *y;
    *y = t;
}
int main() {
    int p = 5, q = 10;
    printf("Before: %d %d\n", p, q);   // 5 10
    swap(&p, &q);
    printf("After:  %d %d\n", p, q);   // 10 5
    return 0;
}
```

**Trace:**
| Step | `*x` / `*y` | p / q |
|---|---|---|
| before | p=5, q=10 | 5, 10 |
| `t = *x` | t=5 | |
| `*x = *y` | p=10 | 10, 10 |
| `*y = t` | q=5 | 10, 5 |

**Trap:** `swap(p, q)` (without `&`) silently does nothing — you'd swap copies. Exams love this.

</details>

---

## Problem 7.4 — Recursion: factorial (predict the output)

```c
#include <stdio.h>
int fact(int n) {
    if (n <= 1) return 1;
    return n * fact(n - 1);
}
int main() {
    printf("%d\n", fact(5));
    return 0;
}
```

**<details><summary>Solution</summary>**

Output: `120`

**Stack trace (the key skill):**

```
fact(5)
  = 5 * fact(4)
       = 4 * fact(3)
            = 3 * fact(2)
                 = 2 * fact(1)
                      = 1        ← BASE CASE reached
                 = 2 * 1 = 2
            = 3 * 2 = 6
       = 4 * 6 = 24
  = 5 * 24 = 120
```

| n | returns |
|---|---|
| 1 | 1 (base case) |
| 2 | 2×1 = 2 |
| 3 | 3×2 = 6 |
| 4 | 4×6 = 24 |
| 5 | 5×24 = 120 |

**Rules:** every recursion needs a **base case** (`n <= 1`) or it never stops (stack overflow). The calls *go down*, the returns *come back up*.

</details>

---

## Problem 7.5 — Recursion: Fibonacci (predict the output)

```c
#include <stdio.h>
int fib(int n) {
    if (n <= 1) return n;
    return fib(n - 1) + fib(n - 2);
}
int main() {
    printf("%d\n", fib(5));
    return 0;
}
```

**<details><summary>Solution</summary>**

Output: `5`

**Call tree (Fibonacci sequence: 0, 1, 1, 2, 3, 5, ...):**

```
                    fib(5)
                   /      \
             fib(4)        fib(3)
             /    \        /    \
        fib(3)  fib(2)  fib(2) fib(1)
        /   \   /   \   /   \
     fib(2) fib(1) fib(1) fib(0) fib(1) fib(0)
     /   \
  fib(1) fib(0)

fib(5) = 5
```

| n | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| fib(n) | 0 | 1 | 1 | 2 | 3 | 5 |

**Trap:** naive Fibonacci is O(2ⁿ) — it recomputes the same values repeatedly (`fib(3)` is computed twice above). Exams may ask "how many calls?" → count the nodes.

</details>

---

## Problem 7.6 — Recursion: sum of digits (write the program)

Write a recursive function that returns the **sum of digits** of a number. `sumDigits(1234) = 1+2+3+4 = 10`.

**<details><summary>Solution</summary>**

```c
#include <stdio.h>
int sumDigits(int n) {
    if (n == 0) return 0;                 // base case
    return (n % 10) + sumDigits(n / 10);  // last digit + rest
}
int main() {
    printf("%d\n", sumDigits(1234));      // 10
    return 0;
}
```

**Trace:**
```
sumDigits(1234) = 4 + sumDigits(123)
                = 4 + (3 + sumDigits(12))
                = 4 + (3 + (2 + sumDigits(1)))
                = 4 + (3 + (2 + (1 + sumDigits(0))))
                = 4 + 3 + 2 + 1 + 0 = 10
```

**Key idea:** `n % 10` peels off the last digit; `n / 10` chops it off. Repeat until `n == 0`.

**Related classics:** `power(x, n)` = `x * power(x, n-1)`; `gcd` = `b == 0 ? a : gcd(b, a % b)`; count digits = `1 + countDigits(n/10)`.

</details>

---

**Next:** [[c-programming/practice/08-pointers-structs|08 · Pointers & structs]] · **Index:** [[c-programming/practice/README|Problem bank]]