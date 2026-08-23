---
module: "SPM"
topic: "Module 3: Introduction to Arrays — 1D/2D Memory Layout, Address Arithmetic & Core Operations"
tags: [c-programming, arrays, 1d-arrays, 2d-arrays, row-major, column-major, address-calculation, linear-search, binary-search, bubble-sort, insertion, deletion, traversal, time-complexity, pointer-arithmetic, array-decay]
last_updated: "2026-08-19"
prerequisites: ["Module 2: Program Control Functions", "Pointers (basic dereference)", "Big-O Notation"]
---

# Module 3: Introduction to Arrays

> Contiguous memory, indexed access, and the address formulas that make arrays O(1)-random-access. Covers 1D and 2D arrays (row-major vs. column-major), every classic operation (traversal, insertion, deletion, linear & binary search, bubble sort), and — critically — the C pitfall that *array index 1 is the second element, not the first*, and that C never checks your bounds. Written for beginners: memory maps are drawn out, every operation has a complexity note, and every formula has a plain-English intuition.

---

## Table of Contents

1. [Conceptual Architecture & ASCII Flowcharts](#1-conceptual-architecture--ascii-flowcharts)
2. [Code Implementation & Memory Analysis](#2-code-implementation--memory-analysis)
3. [High-Yield Exam Problems & Worked Code Drills](#3-high-yield-exam-problems--worked-code-drills)
4. [Real-World System Applications](#4-real-world-system-applications)
5. [Appendix: Formula & Data Quick Reference](#appendix-formula--data-quick-reference)

---

## 1. CONCEPTUAL ARCHITECTURE & ASCII FLOWCHARTS

### 1.0 What Is an Array, Really? — Beginner Foundation

An **array** is a *single block of consecutive memory slots*, all holding values of the *same type*. The array's name is a pointer to the first slot. You reach any slot by its **index**, and because the slots are contiguous, the CPU can compute any element's address in one arithmetic operation — that is why array access is **O(1)** (constant time, independent of size).

**Beginner analogy:** an array is a street with houses numbered 0, 1, 2, … n−1, all the same size. If you know the street's start (base address) and the house size, you can jump straight to house #i without walking past the others.

### 1.1 1D Array — Declaration & Memory Map

```c
int a[5] = {10, 20, 30, 40, 50};
```

```
   Base address = 1000 (say), sizeof(int) = 4 bytes

   INDEX:      [0]     [1]     [2]     [3]     [4]
   ADDRESS:    1000    1004    1008    1012    1016
   VALUE:       10      20      30      40      50
   ├──────────┴──────────┴──────────┴──────────┴──────────┤
   │           CONTIGUOUS BLOCK (5 × 4 = 20 bytes)         │
   └────────────────────────────────────────────────────────┘

   Address(A[i]) = Base + i × sizeof(type)      ← THE formula
   &a[2] = 1000 + 2×4 = 1008
```

**Rules (memorize):**
- Index range is **0 … size−1**. `a[0]` is the first element — there is no `a[1]`-is-first confusion allowed in C.
- Array size must be a **compile-time constant** in standard C (C99 adds variable-length arrays, with caveats).
- Elements are **contiguous** — that contiguity is what enables O(1) access and the address formula.
- The array name **decays to a pointer** to its first element: `a` ≡ `&a[0]`. Passing `a` to a function passes the *address* (Module 4).
- **C does NO bounds checking.** `a[5]` on a 5-element array is **undefined behavior** — it may read/write whatever happens to sit in that memory (the root cause of buffer-overflow vulnerabilities like Heartbleed).
- Total memory = **n × sizeof(type)** bytes.

### 1.2 1D Address Formula — Explicit Derivation

**Step 1.** Let the **base address** be $B$ (address of element 0) and each element occupy $S$ bytes. Element $i$ starts at:

$$\text{Address}(A[i]) = B + i \times S$$

**Why?** To reach element $i$ you walk past $i$ elements, each $S$ bytes wide — that's $i \times S$ bytes beyond the base.

**Step 2.** If the index has a lower bound $L \neq 0$ (e.g. arrays in some languages start at 1), the general form subtracts the bound first:

$$\text{Address}(A[i]) = B + (i - L) \times S$$

| Symbol | Meaning | Unit |
|---|---|---|
| B | base address of array (address of element L) | bytes |
| i | index of the element | — |
| L | lower bound of the index | — |
| S | size of one element (`sizeof(type)`) | bytes |

### 1.3 2D Array — Row-Major vs. Column-Major

A 2D array `int a[R][C]` is physically **one linear block of R×C elements**. The two conventions decide the order in which elements are laid out.

```
   int a[3][4];   /* 3 rows, 4 columns */

   ROW-MAJOR (C):  row 0 all, then row 1 all, then row 2
   INDEX:   [0][0] [0][1] [0][2] [0][3] | [1][0] [1][1] [1][2] [1][3] | [2][0] ...
   OFFSET:    0      1      2      3   |   4      5      6      7    |  8   ...

   COLUMN-MAJOR (FORTRAN): column 0 all, then column 1 all, ...
   INDEX:   [0][0] [1][0] [2][0] | [0][1] [1][1] [2][1] | [0][2] ...
   OFFSET:    0      1      2   |   3      4      5    |  6    ...
```

**Comparison table:**

| Property | Row-Major | Column-Major |
|---|---|---|
| **Next block after** | a full row (C columns) | a full column (R rows) |
| **Used by** | C, C++, Java | FORTRAN, MATLAB (internally), R |
| **Element (i,j) offset** | i × C + j | j × R + i |
| **Cache-friendly loop order** | iterate row-by-row (outer = row, inner = column) | iterate column-by-column (outer = column, inner = row) |
| **Beginner trick** | "go down i rows, then right j columns" | "go down j columns, then right i rows" |

**Why C is row-major and why it matters:** modern CPUs load memory in cache *lines* (e.g. 64 bytes). If your inner loop walks down a column in a row-major array, each access is a cache miss. Walking a row uses one line for many elements. **Loop order is a real performance question in exams and interviews.**

### 1.4 2D Address Formulas — Explicit Derivations

**Row-major** — element $a[i][j]$ in an array with $R$ rows, $C$ columns, base $B$, element size $S$:

$$\text{Address}(a[i][j]) = B + \left( i \times C + j \right) \times S$$

**Intuition (plain English):** to reach row $i$, skip $i$ *whole rows* — each row has $C$ elements — then walk $j$ elements into that row. Total elements before it: $i \times C + j$.

**Column-major:**

$$\text{Address}(a[i][j]) = B + \left( j \times R + i \right) \times S$$

**Intuition:** to reach column $j$, skip $j$ *whole columns* — each column has $R$ elements — then walk $i$ elements down that column. Total elements before it: $j \times R + i$.

**With non-zero lower bounds** $L_r$ (rows) and $L_c$ (columns):

$$\text{Row-major: } B + \big[ (i - L_r) \times C + (j - L_c) \big] \times S$$

| Symbol | Meaning | Unit |
|---|---|---|
| B | base address | bytes |
| i, j | row, column index | — |
| R | number of rows | — |
| C | number of columns | — |
| S | size of one element | bytes |

### 1.5 Array Operation Complexity — Master Table

| Operation | Best case | Average | Worst case | Space (extra) |
|---|---|---|---|---|
| Traversal (read all n) | O(n) | O(n) | O(n) | O(1) |
| Insert at end (if space exists) | O(1) | O(1) | O(1) | — |
| Insert at position k | O(1) | **O(n)** (shift right) | O(n) | O(1) |
| Delete at position k | O(1) | **O(n)** (shift left) | O(n) | O(1) |
| Linear search | O(1) (found first) | O(n) | O(n) | O(1) |
| Binary search (must be sorted) | O(1) | **O(log n)** | O(log n) | O(1) iter / O(log n) recursion |
| Bubble sort | O(n) (already sorted + flag) | O(n²) | O(n²) | O(1) |

**The single most important sentence in this module:** arrays give you **O(1) read** but **O(n) insert/delete** (because everything after the change must shift). That trade-off is exactly why linked lists exist for frequent-insert workloads.

### 1.6 Core Operation Flowcharts

```
   LINEAR SEARCH                      BINARY SEARCH (array MUST be sorted)
   i ← 0                             lo ← 0, hi ← n-1
      │                                  │
      ▼                                  ▼
   i < n ? ──NO──► "not found"      lo ≤ hi ? ──NO──► "not found"
      │YES                                │YES
      ▼                                    ▼
   a[i] == key? ──YES──► return i     mid ← (lo+hi)/2
      │NO                                 │
      ▼                              a[mid]==key? ──YES──► return mid
   i ← i+1, loop                          │NO
                                          ▼
                                    a[mid] < key ? → lo ← mid+1
                                    else            → hi ← mid−1
                                          │
                                          ▼
                                          loop again (search space halves)
```

```
   BUBBLE SORT (n-1 passes, adjacent swaps)
   for pass = 0 .. n-2:
     swapped ← false
     for i = 0 .. n-2-pass:
        if a[i] > a[i+1]:  swap them; swapped ← true
     if !swapped: break          // early exit → O(n) best case
```

**Why binary search is O(log n):** every comparison discards *half* the remaining elements. Starting from n, after k comparisons you have n/2ᵏ elements left. You stop when n/2ᵏ ≤ 1, i.e. k = log₂ n. That is O(log n) — the whole reason sorted data is so valuable.

---

## 2. CODE IMPLEMENTATION & MEMORY ANALYSIS

### 2.1 1D Array — Declaration, Init & Traversal

```c
#include <stdio.h>

int main(void)
{
    int a[5] = {10, 20, 30, 40, 50};   /* full initialization */
    int b[5] = {1, 2};                 /* partial init → rest ZEROED */
    int c[3] = {0};                    /* all zeros */

    for (int i = 0; i < 5; i++)
        printf("a[%d] = %d\n", i, a[i]);

    printf("b[4] = %d\n", b[4]);               /* prints 0 (zero-filled) */
    printf("sizeof(a) = %zu bytes\n", sizeof(a));            /* 5 × 4 = 20 */
    printf("count = %zu\n", sizeof(a) / sizeof(a[0]));       /* 5 */
    return 0;
}
```

**Key idioms (memorize):**
- `sizeof(a)/sizeof(a[0])` = element count. Safe because inside the *declaring* function `sizeof` knows the full size. Use it instead of hard-coding lengths.
- **Partial initialization** (`{1, 2}`) sets the remaining elements to **0** — that's a C guarantee.
- Once an array is *passed* to a function, `sizeof` in the callee gives the pointer size, not the array — hence the separate `n` parameter (see 2.2).

### 2.2 Linear & Binary Search — Production Code

```c
#include <stdio.h>

/* linear search: O(n). Returns index or -1. */
int linearSearch(int a[], int n, int key)
{
    for (int i = 0; i < n; i++)
        if (a[i] == key)
            return i;          /* found at index i */
    return -1;                 /* sentinel for "not found" */
}

/* binary search: O(log n). Array MUST be sorted ascending. */
int binarySearch(int a[], int n, int key)
{
    int lo = 0, hi = n - 1;
    while (lo <= hi)
    {
        int mid = lo + (hi - lo) / 2;   /* overflow-safe midpoint */
        if (a[mid] == key) return mid;
        else if (a[mid] < key) lo = mid + 1;   /* go right half */
        else hi = mid - 1;                     /* go left half  */
    }
    return -1;
}

int main(void)
{
    int a[] = {11, 22, 33, 44, 55};
    int n = sizeof(a) / sizeof(a[0]);
    printf("linear 33 at %d\n", linearSearch(a, n, 33));
    printf("binary 55 at %d\n", binarySearch(a, n, 55));
    printf("binary 40 at %d\n", binarySearch(a, n, 40));
    return 0;
}
```

**Output:**
```
linear 33 at 2
binary 55 at 4
binary 40 at -1
```

**Beginner notes:**
- `int a[]` as a parameter is *identical* to `int *a` — the array **decays** to a pointer, so the function only receives the address, never the size. That's why `n` must be passed.
- `mid = lo + (hi - lo)/2` avoids the overflow that `(lo + hi)/2` can hit for huge arrays — always use the safe form.
- **`-1` as "not found"** is the standard sentinel; it can't collide with a real index (which is ≥ 0).

### 2.3 Insertion & Deletion — With Shift Visualization

```c
#include <stdio.h>

/* insert key at position pos; shifts right. Returns new length. */
int insertAt(int a[], int n, int cap, int key, int pos)
{
    if (n >= cap || pos < 0 || pos > n) return n;   /* guards */
    for (int i = n; i > pos; i--)      /* shift right to make room */
        a[i] = a[i - 1];
    a[pos] = key;
    return n + 1;
}

/* delete at position pos; shifts left. Returns new length. */
int deleteAt(int a[], int n, int pos)
{
    if (pos < 0 || pos >= n) return n;   /* guard */
    for (int i = pos; i < n - 1; i++)    /* shift left to close the gap */
        a[i] = a[i + 1];
    return n - 1;
}

int main(void)
{
    int a[10] = {1, 2, 3, 4, 5};
    int n = 5;

    n = insertAt(a, n, 10, 99, 2);   /* insert 99 at index 2 */
    n = deleteAt(a, n, 0);           /* delete index 0 */

    for (int i = 0; i < n; i++) printf("%d ", a[i]);
    printf("\n");
    return 0;
}
```

**Output:**
```
2 99 3 4 5
```

**Shift visualization (insert at index 2):**

```
   before:   [1][2][3][4][5]
   step 1:   a[5] = a[4]  → [1][2][3][4][5][5]   (i=5)
   step 2:   a[4] = a[3]  → [1][2][3][4][4][5]   (i=4)
   step 3:   a[3] = a[2]  → [1][2][3][3][4][5]   (i=3)
   place:    a[2] = 99    → [1][2][99][3][4][5]
```

**Why insertion is O(n):** in the worst case (position 0) every element shifts. Same for deletion. This is the C code that gives the complexity table its O(n) entry — the price of contiguity, which is exactly why linked lists (non-contiguous nodes) insert in O(1).

### 2.4 2D Array — Traversal (Row-Major, Cache-Friendly)

```c
#include <stdio.h>

int main(void)
{
    int a[3][4] = {
        {1,  2,  3,  4},
        {5,  6,  7,  8},
        {9, 10, 11, 12}
    };

    /* row-major traversal: outer loop = rows, inner = columns (CACHE-FRIENDLY) */
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 4; j++)
            printf("%3d", a[i][j]);
    printf("\n");
    return 0;
}
```

**Memory note:** `a[1][0]` sits 4 elements after `a[0][0]` (offset 4, row-major). If you flip the loops (`j` outer), you'd jump by 4 elements each time — 4× more cache misses on a big matrix.

---

## 3. HIGH-YIELD EXAM PROBLEMS & WORKED CODE DRILLS

---

### Problem 1: 1D Address Calculation

**Problem.** An array `float a[20]` has base address 1024. `sizeof(float) = 4`. Find the address of `a[12]`.

---

**Solution:**

**Step 1 — formula.**

$$\text{Address}(a[i]) = B + i \times S$$

**Step 2 — substitute.**

$$\text{Address}(a[12]) = 1024 + 12 \times 4 = 1024 + 48 = 1072$$

$$\boxed{\text{Address of } a[12] = 1072}$$

---

### Problem 2: 2D Row-Major vs. Column-Major Address

**Problem.** `int a[3][5]` with base 2000, `sizeof(int)=4`. Find the address of `a[2][3]` in (a) row-major and (b) column-major.

---

**Solution:**

**Step 1 — row-major (R=3 rows, C=5 cols).**

$$\text{Addr} = B + (i \times C + j) \times S = 2000 + (2 \times 5 + 3) \times 4 = 2000 + 13 \times 4$$

$$= 2000 + 52$$

$$\boxed{\text{Row-major address} = 2052}$$

**Step 2 — column-major (R = 3).**

$$\text{Addr} = B + (j \times R + i) \times S = 2000 + (3 \times 3 + 2) \times 4 = 2000 + 11 \times 4$$

$$= 2000 + 44$$

$$\boxed{\text{Column-major address} = 2044}$$

**Beginner check:** in row-major, `a[2][3]` is the 13th element (0-indexed) → 13×4 = 52 bytes in. In column-major it's the 11th → 44 bytes in. Different conventions, different addresses — memorize *which* index gets multiplied by which count.

---

### Problem 3: Partial Initialization & sizeof

**Problem.** Predict the output:

```c
int x[6] = {1, 2, 3};
printf("%d %d\n", x[3], x[4]);
printf("%zu\n", sizeof(x) / sizeof(x[0]));
```

---

**Solution:**

**Step 1 — partial init zero-fills.** `x = {1, 2, 3, 0, 0, 0}` (C guarantee).

**Step 2 — outputs.** `x[3] = 0`, `x[4] = 0`.

**Step 3 — element count.** `sizeof(x) = 6 × 4 = 24`; `sizeof(x[0]) = 4`; count = 24/4 = 6.

$$\boxed{0\ 0}\qquad
\boxed{6}$$

---

### Problem 4: Binary Search Dry-Run

**Problem.** Trace binary search for key = 38 in `a = {10, 20, 30, 40, 50, 60}` (n = 6).

---

**Solution — trace table (mid = lo + (hi−lo)/2, integer division):**

| Step | lo | hi | mid | a[mid] | comparison | action |
|---|---|---|---|---|---|---|
| 1 | 0 | 5 | 2 | 30 | 30 < 38 | lo = 3 |
| 2 | 3 | 5 | 4 | 50 | 50 > 38 | hi = 3 |
| 3 | 3 | 3 | 3 | 40 | 40 > 38 | hi = 2 |
| 4 | 3 | 2 | — | — | lo > hi | **stop: not found** |

**Step 5 — result.**

$$\boxed{\text{Not found — returns -1; 4 comparisons}}$$

(If the key were 40, step 3 would return index 3 immediately. Notice how the search interval halves: 6 → 3 → 1 → 0, exactly the O(log₂ 6) ≈ 3–4 comparisons predicted by theory.)

---

### Problem 5: Bubble Sort Trace

**Problem.** Sort `{5, 1, 4, 2}` with bubble sort showing each pass.

---

**Solution — trace table:**

| Pass | Array before | Swaps | Array after |
|---|---|---|---|
| Pass 1 | `[5 1 4 2]` | 5↔1, 5↔4, 5↔2 | `[1 4 2 5]` |
| Pass 2 | `[1 4 2 5]` | 4↔2 | `[1 2 4 5]` |
| Pass 3 | `[1 2 4 5]` | none (swapped=false → break) | `[1 2 4 5]` |

$$\boxed{\text{Sorted: } 1\ 2\ 4\ 5\quad (\text{3 passes, early exit on pass 3})}$$

**Complexity:** worst/reverse-sorted runs n−1 passes with n(n−1)/2 comparisons = **O(n²)**. The `swapped` flag gives **O(n)** best case for already-sorted input.

---

### Problem 6: Insertion/Deletion Shift Count

**Problem.** An array holds n = 6 elements. You (a) insert a new element at position 0 and (b) delete the element at position 0. How many assignments does each operation perform (worst case)?

---

**Solution:**

**(a) Insert at position 0** — every existing element shifts right once:

$$a[6]=a[5],\ a[5]=a[4],\ \dots,\ a[1]=a[0] \quad \Rightarrow \quad 6 \text{ shifts}$$

Then one more assignment places the new element → **6 shifts + 1 place**.

**(b) Delete at position 0** — every element after shifts left once:

$$a[0]=a[1],\ a[1]=a[2],\ \dots,\ a[4]=a[5] \quad \Rightarrow \quad 5 \text{ shifts}$$

$$\boxed{\text{(a) } n \text{ shifts + 1 place } (6+1) \qquad
\text{(b) } n - 1 \text{ shifts } (5)}$$

Both are **O(n)** — the worst case for arrays, confirming the complexity table.

---

## 4. REAL-WORLD SYSTEM APPLICATIONS

| Principle | Real-World Practice |
|---|---|
| **Contiguous random access (O(1))** | Ring buffers & FIFO queues in networking drivers, audio sample buffers, image frame buffers |
| **No bounds checking** | Buffer overflows (Heartbleed, classic `strcpy` attacks) — why safer APIs (`snprintf`, `strncpy`, checked bounds) exist in modern C code |
| **1D arrays** | Sensor data logging, DSP lookup tables (sine tables), CPU cache lines |
| **2D arrays / matrices** | Image pixels, game boards, spreadsheets, ML matrix math (row-major is cache-friendly in C) |
| **Row-major ordering** | Image/video processing in C — row-major loops keep cache hits high |
| **Linear search** | Small unsorted collections, symbol lookup in small tables, unsorted logs |
| **Binary search** | Database index lookup (B-tree leaf scans), sorted dictionaries, codec search tables, `bisect`-style queries |
| **Bubble sort / O(n²) sorts** | Nearly-sorted data with early-exit flag; teaching baseline (industry uses quicksort/mergesort/Timsort) |
| **Insertion/deletion shifting** | Maintaining ordered lists (sorted leaderboards, priority queues) where in-place shift is acceptable |

---

## APPENDIX: Formula & Data Quick Reference

| Quantity | Formula | Notes |
|---|---|---|
| 1D address | $B + i \times S$ | zero-based index |
| 1D with lower bound | $B + (i - L) \times S$ | non-zero lower bound |
| Row-major 2D | $B + (i \times C + j) \times S$ | C/C++ |
| Column-major 2D | $B + (j \times R + i) \times S$ | FORTRAN |
| Array bytes | n × sizeof(type) | use sizeof idiom for count |
| Linear search | O(n) | avg/worst |
| Binary search | O(log n) | sorted only; interval halves each step |
| Bubble sort | O(n²) / O(n) best | early-exit flag |
| Insert/delete | O(n) | due to shifting |
| Array param | `int a[]` ≡ `int *a` | decays to pointer; pass n separately |

## CROSS-REFERENCES

- Related modules: [[module-2-program-control-functions]] (loops drive array ops) · [[module-4-user-defined-functions]] (arrays passed to functions, pointer params) · [[programming/cs50/week-2-arrays]] · [[programming/programming-cs-fundamentals]] (Big-O)