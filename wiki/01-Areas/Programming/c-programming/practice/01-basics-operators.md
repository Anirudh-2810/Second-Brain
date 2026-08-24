---
module: "c-programming"
topic: "Solved Practice — Basics, Output Prediction & Operators (6 problems)"
tags: [programming, c, practice, solved, operators, output-prediction]
last_updated: "2026-08-19"
---

# 01 · Basics, Output Prediction & Operators — 6 Solved Problems

> Classic exam format: *"What is the output of the following program?"* Solve on paper first.

---

## Problem 1.1 — Integer division & precedence

```c
#include <stdio.h>
int main() {
    int a = 7, b = 3;
    printf("%d %d %d\n", a / b, a % b, a + b * 2);
    return 0;
}
```

**<details><summary>Solution</summary>**

Output: `2 1 13`

| Expression | Computation | Result |
|---|---|---|
| `a / b` | `7 / 3` integer division (truncates) | `2` |
| `a % b` | `7 % 3` = remainder | `1` |
| `a + b * 2` | `*` binds tighter: `7 + 6` | `13` |

**Trap:** `7/3` is NOT `2.33` — both operands are `int`, so division truncates.

</details>

---

## Problem 1.2 — Precedence & associativity

```c
#include <stdio.h>
int main() {
    int x = 10, y = 20, z;
    z = x = y;                    // assignment is RIGHT-to-left
    printf("%d %d %d\n", x, y, z);
    return 0;
}
```

**<details><summary>Solution</summary>**

Output: `20 20 20`

| Step | What happens |
|---|---|
| `x = y` | evaluated first (right-to-left): `x` becomes `20` |
| `z = x` | then `z` becomes `20` |

**Rule:** assignment `=` chains right-to-left: `a = b = c` means `a = (b = c)`.

</details>

---

## Problem 1.3 — Increment/decrement operators

```c
#include <stdio.h>
int main() {
    int x = 5;
    printf("%d\n", x++);   // post: print 5, THEN x becomes 6
    printf("%d\n", ++x);   // pre:  x becomes 7, THEN print 7
    printf("%d\n", x--);   // post: print 7, THEN x becomes 6
    printf("%d\n", x);     // 6
    return 0;
}
```

**<details><summary>Solution</summary>**

Output:
```
5
7
7
6
```

| Line | Value used | x after |
|---|---|---|
| `printf("%d", x++)` | 5 (post → old value) | 6 |
| `printf("%d", ++x)` | 7 (pre → new value) | 7 |
| `printf("%d", x--)` | 7 (post → old value) | 6 |
| `printf("%d", x)` | 6 | 6 |

**Memory trick:** *post* = use-then-update (`x++`), *pre* = update-then-use (`++x`).

</details>

---

## Problem 1.4 — Bitwise operators

```c
#include <stdio.h>
int main() {
    int a = 5, b = 3;
    printf("%d %d %d\n", a & b, a | b, a ^ b);
    printf("%d %d\n", a << 1, b >> 1);
    return 0;
}
```

**<details><summary>Solution</summary>**

Output:
```
1 7 6
10 1
```

| Operator | Binary (5=101, 3=011) | Decimal |
|---|---|---|
| `a & b` | `101 & 011 = 001` | 1 |
| `a \| b` | `101 \| 011 = 111` | 7 |
| `a ^ b` | `101 ^ 011 = 110` | 6 |
| `a << 1` | `101 << 1 = 1010` (add a 0) | 10 |
| `b >> 1` | `011 >> 1 = 001` (drop last bit) | 1 |

**Trap:** left-shift doubles, right-shift halves (for positive numbers).

</details>

---

## Problem 1.5 — Implicit type conversion (promotion)

```c
#include <stdio.h>
int main() {
    int i = 5;
    float f = 2.5;
    double d = 2;
    printf("%.2f\n", i + f);      // int → float promoted
    printf("%.2f\n", i / 2);      // both int → integer division
    printf("%.2f\n", i / 2.0);    // one double → real division
    printf("%.2f\n", d + f);      // float → double promoted
    return 0;
}
```

**<details><summary>Solution</summary>**

Output:
```
7.50
2.00
2.50
4.50
```

| Line | Promotion chain | Result |
|---|---|---|
| `i + f` | `int` promoted to `float` | `7.5` |
| `i / 2` | both `int`, **no promotion** → truncation | `2` |
| `i / 2.0` | `int` promoted to `double` | `2.5` |
| `d + f` | `float` promoted to `double` | `4.5` |

**Promotion ladder:** `int → float → double`.

</details>

---

## Problem 1.6 — Casting & modulo on characters

```c
#include <stdio.h>
int main() {
    char c = 'A';
    printf("%d\n", (int)c);       // ASCII of 'A'
    printf("%c\n", c + 1);        // character + 1
    printf("%d\n", 7 % -3);       // sign of dividend wins
    printf("%d\n", -7 % 3);
    return 0;
}
```

**<details><summary>Solution</summary>**

Output:
```
65
B
1
-1
```

| Line | Explanation |
|---|---|
| `(int)c` | `'A'` is stored as ASCII `65` |
| `c + 1` | `65 + 1 = 66` = `'B'` |
| `7 % -3` | C: result takes sign of **dividend** → `1` |
| `-7 % 3` | → `-1` |

**Trap:** In C, `a % b` has the sign of `a`. (In Python it's the sign of `b` — don't mix languages!)

</details>

---

**Next:** [[c-programming/practice/02-conditionals-loops|02 · Conditionals & loops]] · **Index:** [[c-programming/practice/README|Problem bank]]