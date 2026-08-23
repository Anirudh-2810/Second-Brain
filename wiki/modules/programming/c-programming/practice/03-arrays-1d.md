---
module: "c-programming"
topic: "Solved Practice — 1D Arrays & Searching (7 problems)"
tags: [programming, c, practice, solved, arrays, linear-search, binary-search, exam]
last_updated: "2026-08-19"
---

# 03 · 1D Arrays & Searching — 7 Solved Problems

> Arrays are the #1 exam topic. These 7 cover everything: declare, traverse, sum, min/max, reverse, and both searches — with memory pictures.

---

## Problem 3.1 — Declare, fill & print (write the program)

Write a C program to read **5 numbers** into an array, then print them in reverse order.

**<details><summary>Solution</summary>**

```c
#include <stdio.h>
int main() {
    int a[5];
    printf("Enter 5 numbers:\n");
    for (int i = 0; i < 5; i++)
        scanf("%d", &a[i]);           // note: &a[i]

    printf("Reverse order: ");
    for (int i = 4; i >= 0; i--)      // from last index down to 0
        printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```

Input `10 20 30 40 50` → Output: `Reverse order: 50 40 30 20 10`

**Key idea:** reading needs `&a[i]`; the reverse loop runs `4 → 3 → 2 → 1 → 0`.

</details>

---

## Problem 3.2 — Predict the output (index math)

```c
#include <stdio.h>
int main() {
    int a[5] = {10, 20, 30, 40, 50};
    for (int i = 0; i < 5; i += 2)
        printf("%d ", a[i]);
    return 0;
}
```

**<details><summary>Solution</summary>**

Output: `10 30 50`

| `i` | 0 | 1 (skipped) | 2 | 3 (skipped) | 4 | 5 → exit |
|---|---|---|---|---|---|---|
| printed | 10 | — | 30 | — | 50 | |

**Trap:** `i += 2` steps by 2 — the loop prints *every other* element.

</details>

---

## Problem 3.3 — Sum & average (write the program)

Write a program to compute the **sum and average** of `n` numbers stored in an array.

**<details><summary>Solution</summary>**

```c
#include <stdio.h>
int main() {
    int n;
    printf("How many numbers? ");
    scanf("%d", &n);
    int a[n];                 // VLA (C99) — fine for exams
    int sum = 0;
    for (int i = 0; i < n; i++) {
        scanf("%d", &a[i]);
        sum += a[i];          // accumulate on the fly
    }
    float avg = (float)sum / n;   // cast to float, else integer division!
    printf("Sum = %d, Average = %.2f\n", sum, avg);
    return 0;
}
```

Input: `n=3`, `10 20 30` → `Sum = 60, Average = 20.00`

**Trap:** `sum / n` with both `int` truncates (`60/3=20` is fine, but `50/3` would be `16`). Cast: `(float)sum / n`.

</details>

---

## Problem 3.4 — Find min & max (write the program)

Write a program to find the **largest and smallest** element in an array.

**<details><summary>Solution</summary>**

```c
#include <stdio.h>
int main() {
    int a[] = {34, 7, 99, -5, 23, 12};
    int n = sizeof(a) / sizeof(a[0]);   // 6 elements
    int max = a[0], min = a[0];         // seed with FIRST element
    for (int i = 1; i < n; i++) {
        if (a[i] > max) max = a[i];
        if (a[i] < min) min = a[i];
    }
    printf("Max = %d, Min = %d\n", max, min);
    return 0;
}
```

Output: `Max = 99, Min = -5`

**Key idea:** seed `max`/`min` with `a[0]` and compare from `i = 1`. (Seeding with 0 breaks when all values are negative!)

</details>

---

## Problem 3.5 — Reverse array in place

Write a program to **reverse an array** *without* a second array.

**<details><summary>Solution</summary>**

```c
#include <stdio.h>
int main() {
    int a[] = {1, 2, 3, 4, 5};
    int n = sizeof(a) / sizeof(a[0]);
    int left = 0, right = n - 1;
    while (left < right) {
        int temp = a[left];         // swap a[left] and a[right]
        a[left] = a[right];
        a[right] = temp;
        left++;
        right--;
    }
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");                   // 5 4 3 2 1
    return 0;
}
```

| left | right | swap | array |
|---|---|---|---|
| 0 | 4 | a[0]↔a[4] | 5 2 3 4 1 |
| 1 | 3 | a[1]↔a[3] | 5 4 3 2 1 |
| 2 | 2 | stop (`left < right` false) | done |

**Key idea:** the classic two-pointer + `temp` swap. Only `n/2` swaps needed.

</details>

---

## Problem 3.6 — Linear search (write the program)

Search an array for a value and print its **index** (or "not found"). Show the trace.

**<details><summary>Solution</summary>**

```c
#include <stdio.h>
int main() {
    int a[] = {4, 7, 1, 9, 3};
    int n = sizeof(a) / sizeof(a[0]);
    int key, found = -1;
    printf("Enter value to search: ");
    scanf("%d", &key);

    for (int i = 0; i < n; i++) {
        if (a[i] == key) { found = i; break; }   // stop at first match
    }
    if (found != -1) printf("Found at index %d\n", found);
    else             printf("Not found\n");
    return 0;
}
```

Search `key = 9`:

| i | a[i] | match? |
|---|---|---|
| 0 | 4 | no |
| 1 | 7 | no |
| 2 | 1 | no |
| 3 | 9 | **yes → found = 3, break** |

**Complexity:** worst case O(n) — checks every element.

</details>

---

## Problem 3.7 — Binary search (write the program)

Write a program to **binary search** a *sorted* array for `key`, and trace it.

**<details><summary>Solution</summary>**

```c
#include <stdio.h>
int main() {
    int a[] = {2, 5, 8, 12, 16, 23, 38};    // MUST be sorted
    int n = sizeof(a) / sizeof(a[0]);
    int key = 23;
    int low = 0, high = n - 1, found = -1;

    while (low <= high) {
        int mid = (low + high) / 2;
        if (a[mid] == key) { found = mid; break; }
        else if (a[mid] < key) low = mid + 1;   // search RIGHT half
        else                    high = mid - 1; // search LEFT half
    }
    if (found != -1) printf("Found at index %d\n", found);
    else             printf("Not found\n");
    return 0;
}
```

Output: `Found at index 5`

| Step | low | high | mid | a[mid] | action |
|---|---|---|---|---|---|
| 1 | 0 | 6 | 3 | 12 | 12 < 23 → `low = 4` |
| 2 | 4 | 6 | 5 | 23 | **match → index 5** |

**Why it's fast:** each step **halves** the search space → O(log n). For 1000 elements: at most ~10 steps vs 1000 for linear.

**Trap:** if the array is *not* sorted, binary search gives wrong answers.

</details>

---

**Next:** [[c-programming/practice/04-arrays-2d|04 · 2D arrays (matrices)]] · **Index:** [[c-programming/practice/README|Problem bank]]