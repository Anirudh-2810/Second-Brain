---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "Module 3.1a — One-Dimensional Arrays"
date: "2026-10-02"
last_updated: "2026-10-02"
description: "SPM M3.1a one-dimensional arrays, beginner-first — why arrays exist, 0-based indexing, four initialization styles, memory layout and the B+i*S address formula, read/display, sum/avg/max/min/second-largest, linear and binary search, bubble sort, insert/delete with shift analysis, O-complexity table, address drills and 6 practice questions with answers."
tags: [spm, arrays, 1d-arrays, c-programming, 316U06C107, address-formula, linear-search, binary-search, bubble-sort, insertion, deletion, second-largest, complexity, exam-prep, lab]
confidence: high
aliases: ["1D arrays", "Module 3.1 Arrays", "SPM 1D arrays"]
prerequisites: ["Module 2: Program Control Functions", "Basic Big-O notation"]
sources:
  - "raw-sources/SPM Lecture/SPM_Module3_1.pptx"
  - "raw-sources/SPM Lecture/Unit No.3 Arrays_Strings.pdf"
  - "raw-sources/SPM Lab/EX4.docx"
---

## For future agent

**The dedicated ONE-DIMENSIONAL arrays page.** Split from the former combined Module-3 page on 2026-10-02 — the user named arrays the weak area and asked for 1D and 2D as separate pages. 2D/multidimensional content moved to [[module-3-arrays-2d]]; the exam question bank is [[spm-array-question-bank]]; strings are [[module-3-strings]].

**This filename was kept deliberately.** 44 inbound wikilinks across 22 files point at `module-3-arrays`. Renaming it would have broken all of them, so this page absorbed the 1D content and the 2D half was moved out. `aliases` above lets it also be reached as "1D arrays".

**Sources folded in:** the faculty deck `SPM_Module3_1.pptx` (27 slides, AY 2026-27) and the handout `Unit No.3 Arrays_Strings.pdf`. Deck-specific details worth remembering: **four** initialization styles (it adds the `{0}` all-zero shortcut), and the linear search uses a **`-1` sentinel** explicitly tied back to the Module 2 Flag concept. The handout and deck use different example data; both appear below.

**Unsafe-C note:** the faculty material takes a runtime-entered `n` straight into a loop against a fixed-size array. Faithfully recorded, flagged in §1.9 — production code would clamp `n`.

---

# Module 3.1a — One-Dimensional Arrays

> **Syllabus 3.1** ([[syllabus-316U06C107]]): *Arrays: 1D, Multidimensional, Declaration/Initialization, Reading/Displaying.* CO3, part of Module 3's 7 hours.
> **2D half:** [[module-3-arrays-2d]] · **Exam bank:** [[spm-array-question-bank]] · **Strings:** [[module-3-strings]] · Hub: [[module-3-arrays-strings]]

---

## 0. The six sentences that cover 1D

1. An array is **one name for a contiguous block of same-type elements**.
2. Indices run **0 … size−1**. Last index = size − 1. There is no "index 1 is the first element".
3. C does **no bounds checking** — an out-of-range index is silent memory corruption, not an error.
4. Contiguity gives address = `base + index × sizeof(element)` → **O(1) access**.
5. Arrays are **O(1) to read, O(n) to insert/delete** — the shift is the price of contiguity.
6. Sorted data unlocks **binary search (O(log n))** — unsorted data forces **linear (O(n))**.

---

## 1. Fundamentals

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
3. **Memory is reserved immediately** — `size × sizeof(type)` bytes allocated at declaration.
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

**Why:** to reach element $i$ you walk past $i$ elements, each $S$ bytes wide. **This is why indexing is O(1)** — one multiply and one add, never a search. The array name `marks` *is* the address of `marks[0]`.

**Worked drill.** `float a[20]`, base 1024, `sizeof(float) = 4`, find `a[12]`:
$$1024 + 12 \times 4 = 1024 + 48 = \boxed{1072}$$

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

### 1.5 Indexing and the bounds trap

```c
int arr[5] = {10, 20, 30, 40, 50};

printf("%d", arr[0]);   /* 10 — first */
printf("%d", arr[4]);   /* 50 — last  */
arr[2] = 100;           /* modifies the 3rd element */
/* arr[5]  -> OUT OF BOUNDS: undefined behaviour */
```

- **Valid range: `0` to `size − 1`.**
- **No automatic bounds checking.** C will not stop you reading or writing `arr[5]` or `arr[-1]`.

**The bounds condition to memorise:** `0 <= i < n` (equivalently `i >= 0 && i < n`).

### 1.6 Read and display — the two-loop pattern

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

**Two separate loops — one to READ, one to DISPLAY.** The most common array shape in the lab and the exams.

`scanf` needs the element's **address**, so `&` is required. Writing `scanf("%d", arr[i]);` (missing `&`) compiles with a warning and then crashes or corrupts memory at runtime.

### 1.7 Core operations

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

`found = -1` works as a sentinel because **−1 is never a valid array index**. This is the **Flag concept from Module 2** ([[module-2-program-control-functions]] §1.7) applied to arrays. A `found = 0/1` flag with `if (!found)` is equally acceptable.

**Second largest / second smallest** (PIC Q16/Q17 — a favourite OST pick):

```c
/* second largest: two trackers, careful with duplicates */
int first = arr[0], second = arr[0];
for (int i = 1; i < n; i++) {
    if (arr[i] > first) { second = first; first = arr[i]; }
    else if (arr[i] > second && arr[i] != first) second = arr[i];
}
```

For `{2, 9, 1, 4, 6}` → first=9, second=**6**. The `arr[i] != first` guard stops a duplicate of the maximum being counted as second. Mirror the logic with `<` for second smallest.

### 1.8 `sizeof` — three different questions

```c
int a[5] = {10, 20, 30, 40, 50};

sizeof(a);                  /* 20 — total bytes (5 x 4)  */
sizeof(a) / sizeof(a[0]);   /* 5  — element COUNT        */
sizeof(a[0]);               /* 4  — size of ONE element   */
```

`sizeof(a)/sizeof(a[0])` is the idiom for element count — use it instead of hard-coding 5.

> **Caveat:** this only works inside the function that **declared** the array. Once an array is passed to a function it decays to a pointer, so `sizeof` there returns the pointer size (4 or 8), not the array size — which is why `n` must be passed separately. See §4.2.

### 1.9 Pitfalls (deck slide 24)

| # | Pitfall | Detail |
|---|---|---|
| 1 | **Off-by-one** | `for (i = 0; i <= 5; i++)` on a 5-element array touches one past the end. Must be `i < 5`. |
| 2 | **Uninitialized = garbage** | `int arr[5];` alone does **not** set elements to 0. Initialize before reading. |
| 3 | **Cannot be resized** | You cannot `int arr[5];` then later make it hold 10. |
| 4 | **Forgetting `&` in `scanf`** | `scanf("%d", arr[i]);` — classic warning that becomes a runtime crash. |
| 5 | **Second largest with duplicates** | `[5,5,3]` has no genuine second largest unless you guard with `arr[i] != first`. |

> **Safe-coding note (agent annotation, not from the source):** the faculty material passes a runtime-entered `n` straight into `for (i = 0; i < n; i++)` against a fixed `arr[10]`. If the user types `n = 15` you overflow. Production code would clamp `n` to the capacity.

---

## 2. Searching

### 2.1 Linear vs. binary — the decision

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

### 2.2 Floor and ceiling (PIC Q40/Q41)

**Ceiling of x** = smallest element **≥ x**. **Floor of x** = greatest element **≤ x**.

```c
/* both in one binary-search pass over a sorted array */
int lo = 0, hi = n - 1;
while (lo <= hi) {
    int mid = lo + (hi - lo) / 2;
    if (a[mid] == x)          { floor = ceil = a[mid]; break; }
    else if (a[mid] < x)      ceil = a[mid], lo = mid + 1;
    else                      floor = a[mid], hi = mid - 1;
}
```

With `a = {1,3,5,7,8,9}` and `x = 0`: floor is `-1` (no element ≤ 0) and ceiling is `1`. **Report `-1` when it does not exist** — that is the convention in the PIC expected output.

---

## 3. Sorting, insertion, deletion

### 3.1 Bubble sort

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

**Descending order** is the same loop with `a[i] < a[i+1]` as the swap condition (PIC Q12).

### 3.2 Insertion — the shift

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
```

**Shift visualisation — insert 99 at index 2 into `[1 2 3 4 5]`:**

```
   before:   [1][2][3][4][5]
   step 1:   a[5] = a[4]  ->  [1][2][3][4][5][5]     (i=5)
   step 2:   a[4] = a[3]  ->  [1][2][3][4][4][5]     (i=4)
   step 3:   a[3] = a[2]  ->  [1][2][3][3][4][5]     (i=3)
   place:    a[2] = 99    ->  [1][2][99][3][4][5]
```

**Insert into a SORTED list** (PIC Q13) is easier — find the position first, then shift:

```c
int pos = 0;
while (pos < n && a[pos] < key) pos++;     /* walk to the insertion point */
insertAt(a, n, cap, key, pos);
```

`{2,5,7,9,11}` + 8 → pos stops at 3 (7 < 8) → `{2,5,7,8,9,11}`.

### 3.3 Deletion

```c
/* delete at position pos; returns new length */
int deleteAt(int a[], int n, int pos)
{
    if (pos < 0 || pos >= n) return n;
    for (int i = pos; i < n - 1; i++)
        a[i] = a[i + 1];                                /* shift left */
    return n - 1;
}
```

`{1,2,3,4,5}` delete position 3 → shift `a[3]=a[4]` → **`1 2 4 5`** (PIC Q15).

**Shift counts:** inserting at position 0 → **n shifts + 1 place**. Deleting position 0 → **n − 1 shifts**. Both O(n) — the price of contiguity.

### 3.4 The extra-space algorithm

**Counting sort** (PIC Q59) — O(n + k) when values are in a bounded range:

```c
int count[18] = {0};
for (i = 0; i < n; i++) count[a[i]]++;      /* tally */
for (i = 1; i < 18; i++) count[i] += count[i-1];   /* prefix sums */
for (i = n - 1; i >= 0; i--) out[--count[a[i]]] = a[i];   /* stable place */
```

**Segregate 0s, 1s and 2s** (PIC Q54) — the Dutch-national-flag trick, **O(n), no extra array**:

```c
int low = 0, mid = 0, high = n - 1;
while (mid <= high) {
    if (a[mid] == 0)      { swap(a[low], a[mid]); low++; mid++; }
    else if (a[mid] == 1) { mid++; }
    else                  { swap(a[mid], a[high]); high--; }   /* mid stays */
}
```

The `mid--` after the last branch is **deliberate** — the swapped-in element has not been examined yet.

---

## 4. Practical notes

### 4.1 Complexity master table

| Operation | Best | Average | Worst | Extra space |
|---|---|---|---|---|
| Traversal (read all n) | O(n) | O(n) | O(n) | O(1) |
| Insert at end (space exists) | O(1) | O(1) | O(1) | — |
| Insert at position k | O(1) | **O(n)** (shift right) | O(n) | O(1) |
| Delete at position k | O(1) | **O(n)** (shift left) | O(n) | O(1) |
| Linear search | O(1) | O(n) | O(n) | O(1) |
| Binary search (**sorted only**) | O(1) | **O(log n)** | O(log n) | O(1) iter |
| Bubble sort | O(n) (flag) | O(n²) | O(n²) | O(1) |
| Counting sort (bounded range) | O(n+k) | O(n+k) | O(n+k) | O(k) |
| Segregate 0/1/2 | O(n) | O(n) | O(n) | O(1) |

> **The single most important sentence:** arrays give **O(1) read** but **O(n) insert/delete**, because everything after the change must shift. That trade-off is exactly why linked lists exist for frequent-insert workloads.

### 4.2 Array parameters and decay

```c
int linearSearch(int a[], int n, int key) { /* ... */ }
```

`int a[]` as a parameter is **identical** to `int *a` — the array *decays* to a pointer to its first element, so the function receives only the address and **never the size**. That is why `n` must be passed separately.

### 4.3 Real-world applications

| Principle | Where it shows up |
|---|---|
| Contiguous O(1) access | Ring buffers / FIFO queues in network drivers, audio sample buffers |
| No bounds checking | Buffer overflows (Heartbleed) — why bounded APIs exist |
| 1D arrays | Sensor logging, DSP lookup tables (sine tables), CPU cache lines |
| Linear vs binary search | Database index lookups, sorted dictionaries, `bisect`-style queries |
| O(n²) sorts | Nearly-sorted data with an early-exit flag; teaching baseline |
| Insert/delete shifting | Sorted leaderboards, priority queues where in-place shift is acceptable |

---

## 5. Practice Questions

**Q1 — declaring, initializing, accessing**
1. Declare an array of 6 floats and initialize only the first 3. What are the remaining 3?
2. What is the index of the last element in `int data[20];`?
3. Given `int x[4] = {5, 10, 15, 20};` what does `printf("%d", x[1] + x[3]);` print?

<details><summary>Answers</summary>

1. **0, 0, 0** — partial initialization zero-fills (C guarantee).
2. **19** — last index = size − 1.
3. **30** — `x[1]=10`, `x[3]=20`.
</details>

**Q2 — reading & displaying**
1. Write a program that reads 5 integers and displays them in **reverse** order.
2. In the `read_display` pattern with `int arr[10]`, what happens if the user enters `n = 15`?
3. Modify it to print each element's index beside its value.

<details><summary>Answers</summary>

1. `for (i = 4; i >= 0; i--) printf("%d ", arr[i]);`
2. **Undefined behaviour** — the loop reads and writes `arr[10]`..`arr[14]`, past the 10-element array.
3. `printf("arr[%d] = %d\n", i, arr[i]);`
</details>

**Q3 — sum/avg, max/min, linear search**
1. Modify sum/avg to also print how many elements are **above** the average.
2. Find the **second largest** element without sorting.
3. Modify linear search to **count** occurrences instead of stopping at the first match.

<details><summary>Answers</summary>

1. Two passes: compute the average, then `if (arr[i] > avg) count++;`
2. Two trackers, `max` and `second` — see §1.7 for the duplicate guard.
3. Drop the `break`; replace `found = i` with `count++`.
</details>

---

## 6. Quick Test — Topic 3.1 (5 questions)

| # | Type | Question | Answer |
|---|---|---|---|
| Q1 | MCQ | In C, array indexing starts from: (a) 1 (b) 0 (c) −1 (d) depends on compiler | **(b) 0** |
| Q2 | Code trace | `int a[4] = {2, 4, 6, 8};` value of `a[1] + a[3]`? | **12** (4 + 8) |
| Q3 | Short answer | Why does `scanf` require `&arr[i]` instead of `arr[i]`? | It must **write** into the slot, so it needs the element's memory address |
| Q4 | Short answer | Why can binary search not be used on an unsorted array? | It discards half the search space each step, which is only valid if the halves are already ordered |
| Q5 | True/False | `int arr[5];` gives you an array of five zeros. | **False** — it gives five **garbage** values. Only `{0}` or partial init zeroes them |

---

## 7. Formula & Syntax Quick Reference

| Quantity | Formula / pattern | Notes |
|---|---|---|
| 1D address | $B + i \times S$ | zero-based |
| Last valid index | size − 1 | indices run `0 … size-1` |
| Bounds check | `0 <= i < n` | |
| Element count | `sizeof(a) / sizeof(a[0])` | only inside the declaring function |
| Array total bytes | n × `sizeof(type)` | |
| Read n elements | `for (i=0;i<n;i++) scanf("%d",&a[i]);` | `&` required |
| Not-found sentinel | `-1` | never a valid index |
| Binary-search steps | $\log_2 n$ | interval halves each step |
| Safe midpoint | `lo + (hi - lo) / 2` | avoids overflow |
| Bubble inner bound | `i < n - 1 - pass` | shrinks each pass |
| Second largest | two trackers + `arr[i] != first` | duplicate guard |
| 0/1/2 segregation | `low/mid/high` three pointers | O(n), in place |

---

## Cross-References

- **2D half of this topic:** [[module-3-arrays-2d]] — row-major order, both address formulas, matrix ops
- **Exam question bank:** [[spm-array-question-bank]] — 107 real exam questions with test data
- **Module map / routing:** [[module-3-arrays-strings]]
- **Strings:** [[module-3-strings]] — a `char` array *is* a 1D array; read that next
- **Lab:** [[spm-lab-exp3-4-5-guides]] (EXP4 — Arrays) · [[lab-ca-and-experiments]]
- **Loops this depends on:** [[module-2-program-control-functions]] (flag concept, counting loops) · [[spm-module2-faculty-companion]]
- **Foundations:** [[module-1-spm-c-basics]] (memory layout, BSS) · [[module-4-structures-unions-pointers]] (pointers, decay)
- **Drills:** [[spm-practice-bank-module2]] · [[spm-quiz-bank]] · [[c-programming-master-study-guide]]

*Sources ingested 2026-10-02: `SPM_Module3_1.pptx` (27 slides), `Unit No.3 Arrays_Strings.pdf`, `SPM Lab/EX4.docx`, `PIC Practice question_Array.docx` (Q1-Q17).*
