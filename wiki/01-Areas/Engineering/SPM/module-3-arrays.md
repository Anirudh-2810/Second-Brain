---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "Module 3.1 — Introduction to Arrays"
date: "2026-10-01"
description: "SPM M3.1 arrays, complete and beginner-first — 1D declaration and four init styles, memory layout and address formula B+i*S, read/display, sum/avg/max/min, linear and binary search, bubble sort, insert/delete shift analysis, 2D row-major vs column-major with both address formulas, matrix ops, complexity tables, address drills, 12 practice questions and a 5-question quick test."
tags: [spm, arrays, c-programming, 316U06C107, 1d-arrays, 2d-arrays, row-major, column-major, address-formula, linear-search, binary-search, bubble-sort, insertion, deletion, complexity, exam-prep, lab]
last_updated: "2026-10-01"
confidence: high
prerequisites: ["Module 2: Program Control Functions", "Basic Big-O notation"]
sources:
  - "raw-sources/SPM Lecture/SPM_Module3_1.pptx"
  - "raw-sources/SPM Lecture/Unit No.3 Arrays_Strings.pdf"
  - "raw-sources/SPM Lab/EX4.docx"
  - "raw-sources/SPM_Syllabus_316U06C107.md"
---

## For future agent

**The dedicated arrays page for SPM Module 3.1** (syllabus 3.1; part of Module 3's 7 hours, CO3, Bloom's *Apply*). Rewritten 2026-10-01 as the single home for arrays: it absorbs the beginner-teaching half of the former merged page **and** the deep exam bank that used to live here, plus deltas extracted from the faculty deck `SPM_Module3_1.pptx` (27 slides, AY 2026-27).

**Why it was rewritten rather than appended:** arrays + strings had grown into one 40.7 KB page (`module-3-arrays-strings.md`), past the vault's ~25 KB split threshold. That page is now a slim module hub. **Strings live in [[module-3-strings]] — do not duplicate them here.**

Source-conflict notes: (1) the faculty deck and the faculty handout use different example data (`{78,92,65,88,74}` vs `{10,20,30,40,50}`); both appear below, the deck's is primary since the deck is what is taught from. (2) Both prescribe unbounded input — a runtime-entered `n` straight into a fixed-size array — faithful to the source, flagged in §1.9. (3) The deck's own rule: `int m[3][]` is a **compile error**; only the column count is mandatory.

---

# Module 3.1 — Introduction to Arrays

> **Syllabus 3.1** ([[syllabus-316U06C107]]): *Arrays: 1D, Multidimensional, Declaration/Initialization, Reading/Displaying.*
> Lab: **EXP4** per [[spm-lab-exp3-4-5-guides]]. Strings half: [[module-3-strings]]. Module map: [[module-3-arrays-strings]]

---

## 0. The Five Sentences That Cover the Whole Topic

1. An array is **one name for a contiguous block of same-type elements**.
2. Indices run **0 … size−1**. There is no "index 1 is the first element".
3. C does **no bounds checking** — an out-of-range index is silent memory corruption, not an error message.
4. Because slots are contiguous, address = `base + index × sizeof(element)` → **O(1) access**.
5. Arrays are **O(1) to read, O(n) to insert/delete** — the shift is the price of contiguity.

---

## 1. One-Dimensional Arrays

### 1.1 Why arrays exist

```c
/* WITHOUT arrays — 5 names, no loop possible */
int marks1 = 75, marks2 = 82, marks3 = 68, marks4 = 90, marks5 = 76;
int total = marks1 + marks2 + marks3 + marks4 + marks5;

/* WITH an array — change 5 to 500 and only the loop bound changes */
int marks[5];
int total = 0;
for (int i = 0; i < 5; i++) { scanf("%d", &marks[i]); total += marks[i]; }
```

**Exam definition:** *an array is a collection of elements of the same data type, stored in contiguous memory locations, and accessed using one common name together with an index.*

| Situation | Array |
|---|---|
| Marks of 50 students | `int marks[50];` |
| Temperature of 7 days | `float temp[7];` |
| Ages of 30 people | `int age[30];` |
| A person's name | `char name[20];` |

**Five defining properties (deck slide 4):**

| # | Property | Meaning |
|---|---|---|
| 1 | **Fixed size** | element count set at declaration; cannot grow/shrink at runtime |
| 2 | **Homogeneous** | every element is the same type |
| 3 | **Contiguous** | stored back-to-back — this is what makes indexing fast |
| 4 | **Zero-based** | first element at index 0, last at `size − 1` |
| 5 | **Random access** | any element reachable directly by index, in constant time |

### 1.2 Declaration

```c
dataType arrayName[size];

int marks[5];        /* 5 ints    */
float prices[10];    /* 10 floats */
char grades[26];     /* 26 chars  */
```

**Rules:**

1. **Size must be a positive integer** — a constant or constant expression in standard C, *not* a variable.
2. **Fixed at declaration** — a plain C array cannot be resized.
3. **Memory is reserved immediately** — `size × sizeof(type)` bytes are allocated at declaration.
4. **But it is NOT initialized.** `int marks[5];` reserves 20 bytes holding **garbage values** until you assign them. (Contrast a *global* array, which the OS zeroes automatically — see [[module-1-spm-c-basics]] §1.7 on BSS.)

### 1.3 Memory layout and the address formula

```c
int marks[5] = {78, 92, 65, 88, 74};
```

```
   Index:      0      1      2      3      4
   Value:     78     92     65     88     74
   Address:  0x1000 0x1004 0x1008 0x100C 0x1010
              ^ 4 bytes apart — sizeof(int) = 4
```

$$\boxed{\text{Address}(A[i]) = B + i \times S}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $B$ | base address — the address of element 0 | bytes |
| $i$ | index | — |
| $S$ | size of one element, `sizeof(type)` | bytes |

**Why:** to reach element $i$ you walk past $i$ elements, each $S$ bytes wide. **This is why indexing is O(1)** — the CPU does one multiply and one add; it never searches. The array name `marks` *is* the address of `marks[0]`.

### 1.4 Initialization — four ways

```c
/* 1. Full */
int a[5] = {10, 20, 30, 40, 50};

/* 2. Partial — the rest become 0 (a C guarantee) */
int b[5] = {10, 20};                 /* -> {10, 20, 0, 0, 0} */

/* 3. Size inferred — C counts the initializer list */
int c[] = {1, 2, 3, 4};              /* size becomes 4 */

/* 4. All-zero shortcut */
int d[5] = {0};                      /* every element zeroed */
```

Style 4 is the safe way to start an array you will fill later. Partial init (style 2) is what gives a `char` array its free `'\0'` terminators — see [[module-3-strings]].

### 1.5 Indexing rules and the bounds trap

```c
int arr[5] = {10, 20, 30, 40, 50};

printf("%d", arr[0]);   /* 10 — first */
printf("%d", arr[4]);   /* 50 — last  */
arr[2] = 100;           /* modifies the 3rd element */
/* arr[5]  -> OUT OF BOUNDS: undefined behaviour */
```

- **Valid range: `0` to `size − 1`.** For 5 elements that is `0,1,2,3,4` only.
- **No automatic bounds checking.** C will not stop you reading or writing `arr[5]` or `arr[-1]`.

**The bounds condition to memorise:** `0 <= i < n` (equivalently `i >= 0 && i < n`).

### 1.6 Reading and displaying — the two-loop pattern

```c
#include <stdio.h>

int main(void) {
    int arr[10], n, i;

    printf("How many elements? ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        printf("Enter element %d: ", i + 1);
        scanf("%d", &arr[i]);        /* &arr[i], NOT arr[i] */
    }

    printf("You entered: ");
    for (i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}
```

**Two separate loops — one to READ, one to DISPLAY.** This is the most common array shape in the lab and the exams.

`scanf` needs the element's **address**, so `&` is required. Writing `scanf("%d", arr[i]);` (missing `&`) compiles with a warning and then crashes or corrupts memory at runtime.

### 1.7 Array operations

**Sum and average:**

```c
int arr[5] = {12, 45, 7, 23, 9};
int i, sum = 0;
float avg;

for (i = 0; i < 5; i++) {
    sum += arr[i];
}
avg = (float) sum / 5;
printf("Sum = %d\n", sum);            /* 96     */
printf("Average = %.2f\n", avg);      /* 19.20  */
```

`(float)` is **mandatory** — without it `sum / 5` is integer division and the decimal part is truncated.

**Maximum and minimum:**

```c
int i, max = arr[0], min = arr[0];

for (i = 1; i < 5; i++) {
    if (arr[i] > max) max = arr[i];
    if (arr[i] < min) min = arr[i];
}
```

Both seed from `arr[0]`, **not** `0` — seeding with `0` gives the wrong answer whenever every element is negative. The loop starts at index **1** because `arr[0]` was already the seed. The two `if`s must be **separate**, not `else if`.

**Linear search — `−1` sentinel:**

```c
int arr[5] = {12, 45, 7, 23, 9};
int key = 23, i, found = -1;

for (i = 0; i < 5; i++) {
    if (arr[i] == key) { found = i; break; }
}

if (found != -1) printf("Found at index %d\n", found);
else             printf("Not found\n");
```

`found = -1` works as a sentinel because **−1 is never a valid array index**. This is the **Flag concept from Module 2** ([[module-2-program-control-functions]]) applied to arrays. A `found = 0/1` flag with a final `if (!found)` is equally acceptable.

### 1.8 `sizeof` — three different questions

```c
int a[5] = {10, 20, 30, 40, 50};

sizeof(a);                  /* 20 — total bytes (5 x 4)  */
sizeof(a) / sizeof(a[0]);   /* 5  — element COUNT        */
sizeof(a[0]);               /* 4  — size of ONE element   */
```

`sizeof(a)/sizeof(a[0])` is the idiom for element count — use it instead of hard-coding 5.

> **Caveat:** this only works inside the function that **declared** the array. Once an array is passed to a function it decays to a pointer, so `sizeof` there returns the pointer size (4 or 8), not the array size — which is why `n` must be passed separately. See §4.4.

### 1.9 Array pitfalls (deck slide 24)

| # | Pitfall | Detail |
|---|---|---|
| 1 | **Off-by-one** | `for (i = 0; i <= 5; i++)` on a 5-element array touches one past the end. Must be `i < 5`. |
| 2 | **Uninitialized = garbage** | `int arr[5];` alone does **not** set elements to 0. Initialize before reading. |
| 3 | **Cannot be resized** | You cannot `int arr[5];` then later make it hold 10. |
| 4 | **Forgetting `&` in `scanf`** | `scanf("%d", arr[i]);` — classic warning that becomes a runtime crash. |
| 5 | **Column count mandatory in 2D** | `int m[][3]` is fine; `int m[3][]` is a **compile error**. |

> **Safe-coding note (agent annotation, not from the source):** the faculty material passes a runtime-entered `n` straight into `for (i = 0; i < n; i++)` against a fixed `arr[10]`. If the user types `n = 15` you overflow. Production code would clamp `n` to the capacity. The lab keeps the simple form — know the limit.

---

## 2. Two-Dimensional Arrays (Matrices)

### 2.1 The concept

A 2D array is an **array of arrays** — a table with rows and columns.

```
              Column
             0     1     2
          +-----+-----+-----+
  Row 0   | 10  | 20  | 30  |
  Row 1   | 40  | 50  | 60  |
  Row 2   | 70  | 80  | 90  |
          +-----+-----+-----+
```

`matrix[i][j]` = row `i`, column `j`. **Both indices are zero-based**, exactly like 1D.

```c
dataType name[rows][columns];

int matrix[3][3];        /* 3 rows x 3 cols = 9 elements */
```

**Rule:** `arr[rows][cols]` — the **first** index is always the row, the **second** always the column. They cannot be swapped.

### 2.2 Row-major vs. column-major

A `int a[3][4]` is physically **one linear block of 12 elements**. Only the layout order differs.

```
   ROW-MAJOR  (C, C++, Java) — a full row is laid out next
   [0][0] [0][1] [0][2] [0][3] | [1][0] [1][1] [1][2] [1][3] | [2][0] ...
   offset:  0     1     2     3  |   4     5     6     7  |   8 ...

   COLUMN-MAJOR  (FORTRAN, MATLAB, R) — a full column is laid out next
   [0][0] [1][0] [2][0] | [0][1] [1][1] [2][1] | [0][2] ...
   offset:  0     1     2  |   3     4     5  |   6 ...
```

| Property | Row-major | Column-major |
|---|---|---|
| Next block after | a full row (C elements) | a full column (R elements) |
| Used by | **C**, C++, Java | FORTRAN, MATLAB, R |
| Address of `[i][j]` | $B + (i \times C + j) \times S$ | $B + (j \times R + i) \times S$ |
| Cache-friendly loop | outer = row, inner = column | outer = column, inner = row |
| Memory trick | "go down *i* rows, then right *j* columns" | "go across *j* columns, then down *i* rows" |

$$\boxed{\text{Row-major: } \text{Address}(a[i][j]) = B + (i \times C + j) \times S}$$

**Intuition:** to reach row $i$, skip $i$ *whole rows* — each has $C$ elements — then walk $j$ elements into that row. Elements before it: $i \times C + j$.

$$\boxed{\text{Column-major: } \text{Address}(a[i][j]) = B + (j \times R + i) \times S}$$

**Intuition:** to reach column $j$, skip $j$ *whole columns* — each has $R$ elements — then walk $i$ elements down it.

**This is precisely why the column count must be known at compile time** — the compiler needs it to evaluate $i \times C + j$. Without it there is no way to find where row $i$ begins.

**Worked drill.** `int a[3][5]`, base 2000, `sizeof(int)=4`, find `a[2][3]`:

- Row-major: $2000 + (2\times5 + 3)\times4 = 2000 + 52 = \boxed{2052}$
- Column-major: $2000 + (3\times3 + 2)\times4 = 2000 + 44 = \boxed{2044}$

**Why row-major matters in real code:** CPUs load memory in cache *lines* (~64 bytes). Walking a **row** uses one line for many elements. Walking a **column** in a row-major array jumps a whole row each step → a cache miss per access. So outer = row, inner = column is the fast order in C.

### 2.3 Declaration and initialization

```c
int matrix[3][4];                                  /* declaration only */

/* nested-brace style — clearest, matches the visual rows/columns */
int m[2][3] = {
    {1, 2, 3},
    {4, 5, 6}
};

/* flat style — identical result */
int n[2][3] = {1, 2, 3, 4, 5, 6};
```

| Rule | Detail |
|---|---|
| Row count **can** be omitted | `int m[][3] = {{1,2,3},{4,5,6}};` is valid — C counts rows |
| Column count **cannot** | `int m[3][]` is a **compile error** — the compiler needs the row width |

Prefer nested braces in your own code: they visually match rows and columns, so mistakes are easy to spot.

### 2.4 Reading and displaying — nested loops

```c
#include <stdio.h>

int main(void) {
    int mat[2][3], i, j;

    for (i = 0; i < 2; i++)          /* OUTER = rows */
        for (j = 0; j < 3; j++)      /* INNER = columns */
            scanf("%d", &mat[i][j]);

    for (i = 0; i < 2; i++) {
        for (j = 0; j < 3; j++)
            printf("%d ", mat[i][j]);
        printf("\n");                /* AFTER the inner loop */
    }
    return 0;
}
```

**Outer loop = rows (`i`), inner loop = columns (`j`).** The inner loop completes all its iterations for *each* single iteration of the outer loop, so access order is `[0][0] [0][1] [0][2] [1][0] …`.

**The `printf("\n")` position is the whole game** — inside the outer loop but **outside** the inner. Inside the inner prints every element on its own line; outside both prints one long line.

### 2.5 Matrix addition

```
A =        B =          C = A + B:
1  2       5  6         6   8
3  4       7  8        10  12
```

```c
int a[2][2] = {{1, 2}, {3, 4}};
int b[2][2] = {{5, 6}, {7, 8}};
int sum[2][2], i, j;

for (i = 0; i < 2; i++)
    for (j = 0; j < 2; j++)
        sum[i][j] = a[i][j] + b[i][j];
```

**Two matrices can only be added if they have the SAME dimensions**, and each element is added to the element at the **identical `[i][j]` position** — never a mismatched index.

### 2.6 Array vs. string

| | Array | String |
|---|---|---|
| Holds | any same data type | characters only |
| Example | `int marks[5]` | `char name[20]` |
| Terminator | not required | **must** end with `'\0'` when used as a C string |
| Access | by index | by index |

Strings: [[module-3-strings]].

---

## 3. Searching, Sorting, Insertion & Deletion

### 3.1 Complexity master table

| Operation | Best | Average | Worst | Extra space |
|---|---|---|---|---|
| Traversal (read all n) | O(n) | O(n) | O(n) | O(1) |
| Insert at end (space exists) | O(1) | O(1) | O(1) | — |
| Insert at position k | O(1) | **O(n)** (shift right) | O(n) | O(1) |
| Delete at position k | O(1) | **O(n)** (shift left) | O(n) | O(1) |
| Linear search | O(1) | O(n) | O(n) | O(1) |
| Binary search (**sorted only**) | O(1) | **O(log n)** | O(log n) | O(1) iter / O(log n) recursion |
| Bubble sort | O(n) (flag) | O(n²) | O(n²) | O(1) |

> **The single most important sentence:** arrays give **O(1) read** but **O(n) insert/delete**, because everything after the change must shift. That trade-off is exactly why linked lists exist for frequent-insert workloads.

### 3.2 Linear vs. binary search

```
   LINEAR SEARCH                BINARY SEARCH (array MUST be sorted)
   i <- 0                        lo <- 0, hi <- n-1
      |                            |
      v                            v
   i < n ? --NO--> "not found"  lo <= hi ? --NO--> "not found"
      |YES                          |YES
      v                            v
   a[i] == key ? --YES--> return i   mid <- (lo+hi)/2
      |NO                             |
      v                           a[mid]==key? --YES--> return mid
   i <- i+1, loop                     |NO
                                      v
                                a[mid] < key ? -> lo <- mid+1
                                else            -> hi <- mid-1
                                      |
                                      v
                                    loop (search space halves)
```

```c
/* binary search — array MUST be sorted ascending */
int binarySearch(int a[], int n, int key)
{
    int lo = 0, hi = n - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;      /* overflow-safe midpoint */
        if (a[mid] == key)     return mid;
        else if (a[mid] < key) lo = mid + 1;
        else                   hi = mid - 1;
    }
    return -1;                             /* not found */
}
```

- **Why O(log n):** every comparison discards **half** the remaining elements. From n, after k comparisons you have $n/2^k$ left; you stop when $n/2^k \le 1$, i.e. $k = \log_2 n$.
- Use `mid = lo + (hi - lo)/2` — the form `(lo+hi)/2` can overflow on huge arrays.
- **`-1` is the not-found sentinel** and can never collide with a real index (which is ≥ 0).

**Binary-search trace** for key `38` in `{10, 20, 30, 40, 50, 60}`:

| Step | lo | hi | mid | a[mid] | comparison | action |
|---|---|---|---|---|---|---|
| 1 | 0 | 5 | 2 | 30 | 30 < 38 | lo = 3 |
| 2 | 3 | 5 | 4 | 50 | 50 > 38 | hi = 3 |
| 3 | 3 | 3 | 3 | 40 | 40 > 38 | hi = 2 |
| 4 | 3 | 2 | — | — | lo > hi | **stop: not found** |

The interval halves each step — 6 → 3 → 1 → 0 — exactly the $\log_2 6 \approx 3$ comparisons theory predicts.

### 3.3 Bubble sort

```c
for (pass = 0; pass < n - 1; pass++) {
    swapped = 0;
    for (i = 0; i < n - 1 - pass; i++) {
        if (a[i] > a[i + 1]) {
            temp = a[i]; a[i] = a[i + 1]; a[i + 1] = temp;
            swapped = 1;
        }
    }
    if (!swapped) break;              /* already sorted -> O(n) best case */
}
```

- `n - 1 - pass` **shrinks** each pass: after a pass the largest remaining element has bubbled to the end and needs no further checking.
- The `swapped` flag gives **O(n)** on already-sorted input; without it, always O(n²).
- Worst case: n−1 passes × n(n−1)/2 comparisons = **O(n²)**.

**Trace — sorting `{5, 1, 4, 2}`:**

| Pass | Before | Swaps | After |
|---|---|---|---|
| 1 | `[5 1 4 2]` | 5↔1, 5↔4, 5↔2 | `[1 4 2 5]` |
| 2 | `[1 4 2 5]` | 4↔2 | `[1 2 4 5]` |
| 3 | `[1 2 4 5]` | none → `break` | `[1 2 4 5]` |

### 3.4 Insertion and deletion — the shift

```c
/* insert key at position pos; returns new length */
int insertAt(int a[], int n, int cap, int key, int pos)
{
    if (n >= cap || pos < 0 || pos > n) return n;      /* guards */
    for (int i = n; i > pos; i--)
        a[i] = a[i - 1];                                /* shift right */
    a[pos] = key;
    return n + 1;
}

/* delete at position pos; returns new length */
int deleteAt(int a[], int n, int pos)
{
    if (pos < 0 || pos >= n) return n;
    for (int i = pos; i < n - 1; i++)
        a[i] = a[i + 1];                                /* shift left */
    return n - 1;
}
```

**Shift visualisation — insert 99 at index 2 into `[1 2 3 4 5]`:**

```
   before:   [1][2][3][4][5]
   step 1:   a[5] = a[4]  ->  [1][2][3][4][5][5]     (i=5)
   step 2:   a[4] = a[3]  ->  [1][2][3][4][4][5]     (i=4)
   step 3:   a[3] = a[2]  ->  [1][2][3][3][4][5]     (i=3)
   place:    a[2] = 99    ->  [1][2][99][3][4][5]
```

**Shift counts:** inserting at position 0 → **n shifts + 1 place**. Deleting position 0 → **n − 1 shifts**. Both O(n) — the price of contiguity.

---

## 4. Practical Notes

### 4.1 Flowcharts

```
   TRAVERSE                 INSERT at k                DELETE at k
   i <- 0                    i <- n                     i <- k
      |                        |                          |
      v                        v                          v
   i < n ?                  i > k ?                    i < n-1 ?
   NO -> stop               YES: a[i]=a[i-1]; i--        YES: a[i]=a[i+1]; i++
   YES: use a[i]           NO:  a[k]=key                NO: n--
      |                                                          |
      v                                                          v
   i <- i+1                                                n <- n-1
```

### 4.2 Exam address drills

| Given | Asked | Answer |
|---|---|---|
| `float a[20]`, base 1024, S=4 | address of `a[12]` | $1024 + 12(4) = \mathbf{1072}$ |
| `int a[3][5]`, base 2000, S=4 | `a[2][3]` row-major | $2000 + (2{\cdot}5+3)(4) = \mathbf{2052}$ |
| same | `a[2][3]` column-major | $2000 + (3{\cdot}3+2)(4) = \mathbf{2044}$ |
| `int x[6] = {1,2,3}` | `x[3]`, `x[4]`, count | `0`, `0`, **6** (partial init zero-fills) |

**Worked example — partial init and `sizeof`:**

```c
int x[6] = {1, 2, 3};
printf("%d %d\n", x[3], x[4]);              /* 0 0  */
printf("%zu\n", sizeof(x) / sizeof(x[0]));  /* 6    */
```

Partial initialization zero-fills → `{1, 2, 3, 0, 0, 0}`. Element count = $24/4 = 6$.

### 4.3 Array parameters and decay

```c
int linearSearch(int a[], int n, int key) { /* ... */ }
```

`int a[]` as a parameter is **identical** to `int *a` — the array *decays* to a pointer to its first element, so the function receives only the address and **never the size**. That is why `n` must be passed separately, and why `sizeof(a)` inside the function gives the pointer size, not the array size.

### 4.4 Real-world applications

| Principle | Where it shows up |
|---|---|
| Contiguous O(1) access | Ring buffers / FIFO queues in network drivers, audio sample buffers, image frame buffers |
| No bounds checking | Buffer overflows (Heartbleed) — why `snprintf`/bounded APIs exist |
| 1D arrays | Sensor logging, DSP lookup tables (sine tables), CPU cache lines |
| 2D arrays / matrices | Image pixels, game boards, spreadsheets, ML matrix math |
| Row-major ordering | Image/video processing — row-major loops keep cache hits high |
| Linear search | Small unsorted collections, symbol tables, unsorted logs |
| Binary search | Database index lookups, sorted dictionaries, `bisect`-style queries |
| O(n²) sorts | Nearly-sorted data with an early-exit flag; teaching baseline (industry uses quicksort/mergesort/Timsort) |
| Insert/delete shifting | Sorted leaderboards, priority queues where in-place shift is acceptable |

---

## 5. Practice Questions (from the faculty deck)

**Q1 — declaring, initializing, accessing**
1. Declare an array of 6 floats and initialize only the first 3. What are the remaining 3?
2. What is the index of the last element in `int data[20];`?
3. Given `int x[4] = {5, 10, 15, 20};` what does `printf("%d", x[1] + x[3]);` print?

<details><summary>Answers</summary>

1. **0, 0, 0** — partial initialization zero-fills (C guarantee).
2. **19** — last index = size − 1.
3. **30** — `x[1]=10`, `x[3]=20`, sum = 30.
</details>

**Q2 — reading & displaying**
1. Write a program that reads 5 integers and displays them in **reverse** order.
2. In the `read_display` pattern with `int arr[10]`, what happens if the user enters `n = 15`?
3. Modify it to print each element's index beside its value.

<details><summary>Answers</summary>

1. `for (i = 4; i >= 0; i--) printf("%d ", arr[i]);`
2. **Undefined behaviour** — the loop reads and writes `arr[10]`..`arr[14]`, past the 10-element array, corrupting adjacent stack memory.
3. `printf("arr[%d] = %d\n", i, arr[i]);`
</details>

**Q3 — sum/avg, max/min, linear search**
1. Modify sum/avg to also print how many elements are **above** the average.
2. Find the **second largest** element without sorting.
3. Modify linear search to **count** occurrences instead of stopping at the first match.

<details><summary>Answers</summary>

1. Two passes: compute the average, then `if (arr[i] > avg) count++;`
2. Two trackers, `max` and `second`. When `arr[i] > max`, move `max` into `second`, then set `max = arr[i]`. Otherwise if `arr[i] > second`, set `second`.
3. Drop the `break`; replace `found = i` with `count++`.
</details>

**Q4 — 2D arrays**
1. Declare a 2D array for the marks of **4 students in 3 subjects**. Row and column counts?
2. Sum all elements of a 3×3 matrix using nested loops.
3. Modify matrix addition to do **subtraction**.

<details><summary>Answers</summary>

1. `int marks[4][3];` → 4 rows, 3 columns. **Rows = students, columns = subjects** — the first index is always the row.
2. `for (i=0;i<3;i++) for (j=0;j<3;j++) total += m[i][j];`
3. Change `+` to `-` in `c[i][j] = a[i][j] - b[i][j];`
</details>

---

## 6. Quick Test — Topic 3.1 (5 questions)

| # | Type | Question | Answer |
|---|---|---|---|
| Q1 | MCQ | In C, array indexing starts from: (a) 1 (b) 0 (c) −1 (d) depends on compiler | **(b) 0** |
| Q2 | Code trace | `int a[4] = {2, 4, 6, 8};` value of `a[1] + a[3]`? | **12** (4 + 8) |
| Q3 | Short answer | Why does `scanf` require `&arr[i]` instead of `arr[i]`? | It must **write** into the slot, so it needs the element's memory address |
| Q4 | Short answer | Explain row-major order. | Elements of a whole row are stored consecutively, then the next row — so `a[i][j]` sits at `base + (i×C + j)×S` |
| Q5 | True/False | `int m[3][4];` can later be resized to `int m[5][4];` at runtime. | **False** — a plain C array's size is fixed at declaration |

---

## 7. Formula & Syntax Quick Reference

| Quantity | Formula / pattern | Notes |
|---|---|---|
| 1D address | $B + i \times S$ | zero-based |
| Row-major 2D address | $B + (i \times C + j) \times S$ | C / C++ / Java |
| Column-major 2D address | $B + (j \times R + i) \times S$ | FORTRAN / MATLAB |
| Last valid index | size − 1 | indices run `0 … size-1` |
| Bounds check | `0 <= i < n` | |
| Element count | `sizeof(a) / sizeof(a[0])` | only inside the declaring function |
| Array total bytes | n × `sizeof(type)` | |
| Row-major cache loop | outer `i` (row), inner `j` (col) | the fast order in C |
| Read n elements | `for (i=0;i<n;i++) scanf("%d",&a[i]);` | `&` required |
| Not-found sentinel | `-1` | never a valid index |
| Bubble inner bound | `i < n - 1 - pass` | shrinks each pass |
| Safe midpoint | `lo + (hi - lo) / 2` | avoids overflow |

---

## Cross-References

- **Strings half of the module:** [[module-3-strings]] — string model, `'\0'`, `strlen`/`strcpy`/`strcmp`/`strcat`, the strcpy exam drill
- **Module map / routing:** [[module-3-arrays-strings]]
- **Syllabus:** [[syllabus-316U06C107]] · [[assessment-guide-ese-ost-quiz]] · [[formula-sheet-spm]]
- **Lab:** [[spm-lab-exp3-4-5-guides]] (EXP4 — Arrays) · [[lab-ca-and-experiments]]
- **Loops this depends on:** [[module-2-program-control-functions]] (flag concept, counting loops) · [[spm-module2-faculty-companion]]
- **Foundations:** [[module-1-spm-c-basics]] (memory layout, BSS) · [[module-4-structures-unions-pointers]] (pointers, decay)
- **Practicals:** [[spm-pic-question-bank]] · [[spm-quiz-bank]] · [[c-programming-master-study-guide]]

*Sources ingested 2026-10-01: `SPM_Module3_1.pptx` (27 slides), `Unit No.3 Arrays_Strings.pdf`, `SPM Lab/EX4.docx`.*
