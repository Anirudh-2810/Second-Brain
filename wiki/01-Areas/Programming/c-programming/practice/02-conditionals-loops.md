---
module: "c-programming"
topic: "Solved Practice — Conditionals & Loops (6 problems)"
tags: [programming, c, practice, solved, conditionals, loops, exam]
last_updated: "2026-08-19"
---

# 02 · Conditionals & Loops — 6 Solved Problems

> All the classic decision & repetition questions. Solve on paper first, then check the trace table.

---

## Problem 2.1 — Dangling-else: which `if` does the `else` belong to?

```c
#include <stdio.h>
int main() {
    int x = 10, y = 5;
    if (x > 5)
        if (y > 10)
            printf("A\n");
        else
            printf("B\n");      // ← which if does this else pair with?
    return 0;
}
```

**<details><summary>Solution</summary>**

Output: `B`

**Rule (the dangling-else):** an `else` pairs with the **nearest unmatched `if`** — the *inner* `if (y > 10)`, not the outer.

Trace:
| Check | Result |
|---|---|
| `x > 5` | `10 > 5` → true → enter inner if |
| `y > 10` | `5 > 10` → false → execute the `else` |
| prints | `B` |

**Fix when you mean the outer if:** wrap the inner one in braces:
```c
if (x > 5) {
    if (y > 10) printf("A\n");
}
else printf("B\n");
```

</details>

---

## Problem 2.2 — `switch` fall-through (no `break`)

```c
#include <stdio.h>
int main() {
    int n = 2;
    switch (n) {
        case 1: printf("One ");
        case 2: printf("Two ");
        case 3: printf("Three ");
        default: printf("Default");
    }
    return 0;
}
```

**<details><summary>Solution</summary>**

Output: `Two Three Default`

| Step | Action |
|---|---|
| `n = 2` | matches `case 2` |
| prints | `Two ` |
| **no `break`** | **falls through** into `case 3` |
| prints | `Three ` |
| falls through | into `default` |
| prints | `Default` |

**Rule:** without `break`, execution *falls through* every case below the match. Each exam has one of these — spot the missing `break`!

</details>

---

## Problem 2.3 — `while` loop output

```c
#include <stdio.h>
int main() {
    int i = 1, sum = 0;
    while (i <= 5) {
        sum = sum + i;
        i++;
    }
    printf("%d %d\n", i, sum);
    return 0;
}
```

**<details><summary>Solution</summary>**

Output: `6 15`

| Iteration | i (before) | sum before | sum after | i after |
|---|---|---|---|---|
| 1 | 1 | 0 | 1 | 2 |
| 2 | 2 | 1 | 3 | 3 |
| 3 | 3 | 3 | 6 | 4 |
| 4 | 4 | 6 | 10 | 5 |
| 5 | 5 | 10 | 15 | 6 |
| check | 6 ≤ 5? **false → exit** | | | |

**Trap:** `i` exits the loop as `6`, *not* `5` — the update runs one extra time before the condition fails.

</details>

---

## Problem 2.4 — `for` loop with `break` and `continue`

```c
#include <stdio.h>
int main() {
    for (int i = 1; i <= 10; i++) {
        if (i % 3 == 0) continue;
        if (i == 8) break;
        printf("%d ", i);
    }
    return 0;
}
```

**<details><summary>Solution</summary>**

Output: `1 2 4 5 7`

| i | Action |
|---|---|
| 1 | prints `1` |
| 2 | prints `2` |
| 3 | `3%3==0` → `continue` (skips print) |
| 4 | prints `4` |
| 5 | prints `5` |
| 6 | `6%3==0` → skip |
| 7 | prints `7` |
| 8 | `i==8` → `break` (loop ends) |

Multiples of 3 (3, 6, 9) skipped; 8 stops the loop before it prints.

</details>

---

## Problem 2.5 — Nested loop: star pattern

```c
#include <stdio.h>
int main() {
    for (int i = 1; i <= 3; i++) {
        for (int j = 1; j <= i; j++)
            printf("*");
        printf("\n");
    }
    return 0;
}
```

**<details><summary>Solution</summary>**

Output:
```
*
**
***
```

| Outer `i` | Inner `j` runs | Prints |
|---|---|---|
| 1 | `j=1` (once) | `*` |
| 2 | `j=1,2` (twice) | `**` |
| 3 | `j=1,2,3` (3 times) | `***` |

**Pattern rule:** inner loop bound = `i` → increasing triangle. Change `j <= i` to `j <= 3` for a square, or `j <= 4 - i` for a shrinking triangle.

</details>

---

## Problem 2.6 — `do-while` validation

```c
#include <stdio.h>
int main() {
    int n;
    do {
        printf("Enter 1 or 2: ");
        scanf("%d", &n);
    } while (n != 1 && n != 2);
    printf("You picked %d\n", n);
    return 0;
}
```

**<details><summary>Solution</summary>**

Run with input: `5` then `2`

```
Enter 1 or 2: 5
Enter 1 or 2: 2
You picked 2
```

| Round | Input | `n != 1 && n != 2` | Repeats? |
|---|---|---|---|
| 1 | 5 | `true && true` = true | yes |
| 2 | 2 | `false && false` = false | no → exit |

**Why `do-while`?** The prompt must appear at least once before we can validate. A `while` loop would need to set `n` to an invalid value first.

</details>

---

**Next:** [[c-programming/practice/03-arrays-1d|03 · 1D arrays & searching]] · **Index:** [[c-programming/practice/README|Problem bank]]