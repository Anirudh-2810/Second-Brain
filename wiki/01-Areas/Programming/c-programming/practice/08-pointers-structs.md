---
module: "c-programming"
topic: "Solved Practice — Pointers & Structs (5 problems)"
tags: [programming, c, practice, solved, pointers, structs, exam]
last_updated: "2026-08-19"
---

# 08 · Pointers & Structs — 5 Solved Problems

> Pointer + struct problems look scary, but they reduce to two ideas: **`&` = address**, **`*` = value at that address**, and **`.` vs `->`**.

---

## Problem 8.1 — Pointer basics (predict the output)

```c
#include <stdio.h>
int main() {
    int x = 10;
    int *p = &x;
    int **pp = &p;
    printf("%d\n", *p);
    printf("%d\n", **pp);
    *p = 20;
    printf("%d\n", x);
    return 0;
}
```

**<details><summary>Solution</summary>**

Output:
```
10
10
20
```

| Expression | Meaning | Value |
|---|---|---|
| `*p` | value at the address p holds (= x) | 10 |
| `**pp` | p points to x; pp points to p → follow twice | 10 |
| `*p = 20` | writes 20 into x's memory | x = 20 |

**Memory picture:**
```
pp ──► p ──► x = 10 (then 20)
```

**Key idea:** `*p` = one level of dereference, `**pp` = two levels. Adding levels never changes *what* you can reach, only *how many hops*.

</details>

---

## Problem 8.2 — Pointer arithmetic (predict the output)

```c
#include <stdio.h>
int main() {
    int a[] = {10, 20, 30, 40};
    int *p = a;                    // points to a[0]
    printf("%d\n", *p);
    printf("%d\n", *(p + 1));      // moves FORWARD one int
    printf("%d\n", *(a + 2));      // same as a[2]
    p += 3;
    printf("%d\n", *p);
    return 0;
}
```

**<details><summary>Solution</summary>**

Output:
```
10
20
30
40
```

| Step | p points to | value |
|---|---|---|
| `p = a` | a[0] | *p = 10 |
| `p + 1` | a[1] | 20 |
| `a + 2` | a[2] | 30 |
| `p += 3` | a[3] | 40 |

**Critical rule:** `p + 1` moves by **`sizeof(int)` = 4 bytes**, not 1 byte! The pointer knows its type. That's why `a[i]` and `*(a + i)` are identical.

</details>

---

## Problem 8.3 — Function returns a value vs. a pointer (predict the output)

```c
#include <stdio.h>
int *findMax(int *arr, int size) {
    int *max = arr;
    for (int i = 1; i < size; i++)
        if (arr[i] > *max) max = &arr[i];
    return max;              // returns the ADDRESS of the max
}
int main() {
    int data[] = {5, 9, 3, 7};
    int *m = findMax(data, 4);
    printf("%d\n", *m);
    *m = 0;
    printf("%d\n", data[1]);     // was 9
    return 0;
}
```

**<details><summary>Solution</summary>**

Output:
```
9
0
```

| Call | What happens |
|---|---|
| `findMax` | walks the array tracking `&arr[i]` of the biggest |
| returns | address of `data[1]` (value 9) |
| `*m = 0` | writes 0 into `data[1]` through the pointer |

**Key idea:** returning a pointer is safe when it points to memory that *outlives* the function (like an array owned by `main`). **Trap:** returning a pointer to a *local* variable is a bug — the local dies when the function returns (dangling pointer).

</details>

---

## Problem 8.4 — Struct access: `.` vs `->` (predict the output)

```c
#include <stdio.h>
#include <string.h>
struct Student { int roll; char name[20]; float marks; };
int main() {
    struct Student s = {101, "Priya", 92.5};
    struct Student *p = &s;
    printf("%d\n", s.roll);
    printf("%d\n", (*p).roll);       // dereference, then dot
    printf("%d\n", p->roll);         // arrow = shortcut
    p->marks = 95.0;                 // modify through pointer
    printf("%.1f\n", s.marks);
    return 0;
}
```

**<details><summary>Solution</summary>**

Output:
```
101
101
101
95.0
```

| Access | Means |
|---|---|
| `s.roll` | dot — s is a struct |
| `(*p).roll` | dereference p to get the struct, then dot |
| `p->roll` | **arrow** — same thing, shorthand |

**Rule:** struct → use **`.`**; pointer-to-struct → use **`->`** (or `(*p).`). `p->marks = 95.0` modifies the original struct through the pointer — same pass-by-address idea.

</details>

---

## Problem 8.5 — Array of structs (write the program)

Write a program to store 3 students (roll, name, marks), print the highest scorer.

**<details><summary>Solution</summary>**

```c
#include <stdio.h>
#include <string.h>
struct Student { int roll; char name[20]; float marks; };

int main() {
    struct Student s[3] = {
        {101, "Priya", 92.5},
        {102, "Raj",  88.0},
        {103, "Sam",  95.5}
    };
    int best = 0;                       // index of top student
    for (int i = 1; i < 3; i++)
        if (s[i].marks > s[best].marks)
            best = i;

    printf("Topper: %s, Roll %d, Marks %.1f\n",
           s[best].name, s[best].roll, s[best].marks);
    return 0;
}
```

Output: `Topper: Sam, Roll 103, Marks 95.5`

**Key idea:** arrays of structs work exactly like arrays of primitives — index with `[i]`, access members with `.`.

**Pro move:** add a `typedef` to drop the `struct` keyword every time:
```c
typedef struct { int roll; char name[20]; float marks; } Student;
Student s[3] = { ... };
```

</details>

---

## Bonus — Pointer + struct combined challenge

```c
typedef struct { int a, b; } Pair;
void swapFields(Pair *p) {
    int t = p->a;
    p->a = p->b;
    p->b = t;
}
int main() {
    Pair pr = {3, 7};
    swapFields(&pr);
    printf("%d %d\n", pr.a, pr.b);
    return 0;
}
```

**<details><summary>Solution</summary>**

Output: `7 3`

| Step | `p->a` | `p->b` |
|---|---|---|
| before | 3 | 7 |
| `t = p->a` | t=3 | |
| `p->a = p->b` | 7 | 7 |
| `p->b = t` | 7 | 3 |

**Everything in one:** `typedef` (nickname), pointer parameter, `->` access, and pass-by-address to modify a struct in the caller.

</details>

---

**Index:** [[c-programming/practice/README|Problem bank]] · **More:** [[c-programming/c-essentials-for-beginners|C essentials]]