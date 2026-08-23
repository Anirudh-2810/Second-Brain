---
module: "c-programming"
topic: "Solved Practice — Sorting Algorithms (6 problems)"
tags: [programming, c, practice, solved, sorting, bubble-sort, selection-sort, insertion-sort, exam]
last_updated: "2026-08-19"
---

# 05 · Sorting — 6 Solved Problems

> Every exam asks **bubble, selection, or insertion sort** — usually "trace the passes" or "find the error." Learn each with a full trace table and you'll ace any variant.

---

## Problem 5.1 — Bubble sort: write it + trace all passes

Sort `{5, 1, 4, 2, 8}` ascending with bubble sort. Write the code and show every pass.

**<details><summary>Solution</summary>**

```c
#include <stdio.h>
int main() {
    int a[] = {5, 1, 4, 2, 8};
    int n = 5;
    for (int i = 0; i < n - 1; i++) {            // passes
        for (int j = 0; j < n - 1 - i; j++) {    // compare adjacent
            if (a[j] > a[j + 1]) {               // out of order → swap
                int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t;
            }
        }
    }
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    return 0;
}
```

**Trace (each row = end of a pass):**

| Pass | Array after pass | What moved |
|---|---|---|
| start | `5 1 4 2 8` | — |
| 1 | `1 4 2 5 8` | largest `8` bubbled to end |
| 2 | `1 2 4 5 8` | `5` settled |
| 3 | `1 2 4 5 8` | no swaps, but loop still runs |
| 4 | `1 2 4 5 8` | sorted |

**Step-by-step pass 1:** `5↔1 → 1 5 4 2 8` · `5↔4 → 1 4 5 2 8` · `5↔2 → 1 4 2 5 8` · `5<8 no swap`.

- **Inner loop shrinks** (`n-1-i`) because the largest element is already fixed at the end.
- **Best case (already sorted):** still O(n²) with this version (an "optimized" version adds a `swapped` flag → O(n)).
- **Complexity:** O(n²) time, O(1) extra space. **Stable.**

</details>

---

## Problem 5.2 — Bubble sort: predict the output

```c
#include <stdio.h>
int main() {
    int a[] = {3, 0, 2, 1};
    int n = 4;
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - 1 - i; j++)
            if (a[j] > a[j + 1]) {
                int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t;
            }
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    return 0;
}
```

**<details><summary>Solution</summary>**

Output: `0 1 2 3`

| Pass | j=0 | j=1 | j=2 | result |
|---|---|---|---|---|
| 1 | 3↔0 → `0 3 2 1` | 3↔2 → `0 2 3 1` | 3↔1 → `0 2 1 3` | `0 2 1 3` |
| 2 | 0<2 no | 2↔1 → `0 1 2 3` | (j < 4-1-1=2) | `0 1 2 3` |
| 3 | 0<1 no | (j < 1) | | `0 1 2 3` |

**Visual rule:** after pass `k`, the last `k` elements are guaranteed sorted.

</details>

---

## Problem 5.3 — Selection sort: write it + trace

Sort `{29, 10, 14, 37, 13}` with **selection sort** (find smallest each pass, swap to front).

**<details><summary>Solution</summary>**

```c
#include <stdio.h>
int main() {
    int a[] = {29, 10, 14, 37, 13};
    int n = 5;
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;                          // assume a[i] is smallest
        for (int j = i + 1; j < n; j++)
            if (a[j] < a[minIdx]) minIdx = j;    // find the real smallest
        int t = a[i]; a[i] = a[minIdx]; a[minIdx] = t;  // swap it to front
    }
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    return 0;
}
```

**Trace:**

| Pass | Array before | min found | Array after |
|---|---|---|---|
| 1 | `29 10 14 37 13` | 10 (idx 1) | `10 29 14 37 13` |
| 2 | `10 29 14 37 13` | 13 (idx 4) | `10 13 14 37 29` |
| 3 | `10 13 14 37 29` | 14 (idx 2, already) | `10 13 14 37 29` |
| 4 | `10 13 14 37 29` | 29 (idx 4) | `10 13 14 29 37` |

**Key idea:** only **one swap per pass** (fewer swaps than bubble). O(n²) comparisons, O(n) swaps. **Not stable.**

</details>

---

## Problem 5.4 — Insertion sort: write it + trace

Sort `{12, 11, 13, 5, 6}` with **insertion sort** (like sorting playing cards).

**<details><summary>Solution</summary>**

```c
#include <stdio.h>
int main() {
    int a[] = {12, 11, 13, 5, 6};
    int n = 5;
    for (int i = 1; i < n; i++) {
        int key = a[i];            // card to insert
        int j = i - 1;
        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];       // shift bigger cards right
            j--;
        }
        a[j + 1] = key;            // place the card
    }
    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    return 0;
}
```

**Trace:**

| Step | Array state (key in bold) |
|---|---|
| start | `12 11 13 5 6` |
| key=11 | `11 12 13 5 6` (11 shifted before 12) |
| key=13 | `11 12 13 5 6` (already in place) |
| key=5 | `5 11 12 13 6` (5 shifts all the way left) |
| key=6 | `5 6 11 12 13` (6 slots between 5 and 11) |

**Key idea:** grow a sorted prefix one element at a time — shift, don't swap. **Best case (sorted): O(n).** Average/worst: O(n²). **Stable.**

</details>

---

## Problem 5.5 — Which sort is which? (concept matching)

Match the algorithm to its *signature* behavior:

**(a)** Largest element "bubbles" to the end each pass; adjacent swaps.
**(b)** Each pass selects the smallest remaining and swaps it to the front.
**(c)** Builds a sorted prefix; each new card is shifted into place.

**<details><summary>Solution</summary>**

| Description | Algorithm |
|---|---|
| (a) | **Bubble sort** — compare adjacent, swap, largest settles last |
| (b) | **Selection sort** — find min, one swap per pass |
| (c) | **Insertion sort** — shift to insert; O(n) on already-sorted data |

**Exam hint:** if asked "fastest on nearly-sorted data" → **insertion sort** (O(n)). If asked "fewest swaps" → **selection**. If asked "stable and simple" → **bubble**.

</details>

---

## Problem 5.6 — Find the error in the sorting code

```c
int a[] = {4, 3, 2, 1};
int n = 4;
for (int i = 0; i < n; i++)                 // BUG: should be i < n-1
    for (int j = 0; j < n - 1; j++)         // BUG: should be n-1-i
        if (a[j] > a[j + 1]) {
            int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t;
        }
```

**<details><summary>Solution</summary>**

- Outer loop `i < n`: the last pass has nothing left to compare (after n−1 passes it's sorted). Runs one wasted pass, but **harmless** here.
- Inner loop `j < n - 1`: comparing `a[j+1]` when `j = n-2` → `a[n-1]` is the last element — **OK bounds-wise**, but it re-compares already-sorted pairs, doing redundant work.
- **Real bug risk:** if someone writes `j < n` in the inner loop, then `a[j+1]` = `a[n]` → **out-of-bounds / undefined behavior** — the classic fix is `n - 1 - i`.

**Correct version:** outer `i < n-1`, inner `j < n-1-i`.

</details>

---

**Next:** [[c-programming/practice/06-strings|06 · Strings]] · **Index:** [[c-programming/practice/README|Problem bank]]