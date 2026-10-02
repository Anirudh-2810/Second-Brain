---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "Module 3.1 — Array Question Bank (107 exam questions)"
date: "2026-10-02"
last_updated: "2026-10-02"
description: "SPM Module 3.1 array question bank — all 107 questions from the official PIC practice set with their test data and expected output, grouped 1D basics (Q1-17), 2D core (Q18-31) and advanced/DSA (Q32-107), with full worked C solutions for the syllabus-core questions and an exam-yield ranking."
tags: [spm, arrays, question-bank, pic, practice, exam-prep, ost, ese, c-programming, 316U06C107, co3]
confidence: high
aliases: ["SPM array questions", "PIC array bank", "107 array questions"]
prerequisites: ["[[module-3-arrays]]", "[[module-3-arrays-2d]]"]
sources:
  - "raw-sources/drive-download-20260908T190927Z-1-001/Semester 1/SPM/PIC Practice question_Array.docx"
---

## For future agent

**The dedicated array question bank**, created 2026-10-02. Before this, [[spm-pic-question-bank]] compressed all 107 array questions into a single dense paragraph of topic labels with only **two** worked solutions (Q16, Q21) — the questions themselves were never written out. This page restores them.

**Source:** `raw-sources/.../Semester 1/SPM/PIC Practice question_Array.docx`, extracted via the DOCX→stdlib-zipfile recipe in [[raw-sources-ingest-workflow]]. All question wording and test data are **verbatim from the official set** — do not paraphrase them, because students will be tested on this exact phrasing.

**Structure and what it means:**

- **Q1–17 (1D basics)** and **Q18–31 (2D core)** are the **syllabus-aligned, exam-realistic** set. Full worked C solutions are given for all of these.
- **Q32–107 (advanced / DSA-flavored)** is an **extension bank beyond ESE scope** — the source file itself calls it *"extension bank beyond ESE, good for quiz predict-output and interviews."* These are listed with topic + expected output for reference, **not** solved. Do not present them as examinable.

**Known defects in the source, preserved rather than corrected** (because the printed expected output is what students are marked against):
- **Q32** prints *"index 0 and 5"* but `0 + 6 = 6`, not 15 — the *values* are wrong even though index 0 and 5 are right. Same issue in **Q52** (*"fromed"*, value 5 unverifiable from the array alone) and **Q83** (*92 − 39 = 53* ✓ this one is correct).
- **Q33** asks for a majority element on `4 8 4 6 7 4 4 8` and answers *"There are no Majority Elements"* — correct, 4 appears 4 times out of 8, which is not *more than* n/2. This trips students up; the strict inequality is the point.
- **Q38**'s boilerplate description is copy-pasted from Q37 (it describes a pivot element for a merge question).
- **Q25**'s expected output interleaves row sums and column sums ambiguously (`5 6 11 / 7 8 15 / 12 14`).

**Teaching use:** [[module-3-arrays]] keeps its 6 *teaching* practice questions and 5-question quick test (understanding checks); this page holds the *exam bank* (recall + application). Different jobs — do not merge them.

---

# SPM Module 3.1 — Array Question Bank (107 questions)

> **Source:** official PIC practice set, verbatim.
> **Theory:** [[module-3-arrays]] (1D) · [[module-3-arrays-2d]] (2D) · Hub: [[module-3-arrays-strings]]
> **Registry:** [[spm-pic-question-bank]] (all three PIC sets: 26 conditional + 59 loop + 107 array)

---

## Exam-yield ranking — do these first

| Priority | Questions | Why |
|---|---|---|
| **Highest** | **Q16** (2nd largest), **Q19** (matrix add), **Q21** (matrix multiply), **Q22** (transpose), **Q9** (max/min) | Textbook 2–3 marks, appear directly in OST/ESE |
| High | Q2 (reverse), Q3 (sum), Q11/Q12 (sort asc/desc), Q15 (delete), Q18 (print 2D), Q23/Q24 (diagonals) | Direct syllabus drills, low complexity |
| Medium | Q1, Q4, Q10, Q13, Q14, Q20, Q26/Q27, Q28, Q30, Q31 | Simple loops + one concept |
| Low | Q5–Q8, Q29, Q53, Q58, Q73 | Frequency/count problems, repetitive |
| **Beyond ESE** | **Q32–107** | Extension bank — awareness only |

---

# PART A — 1D basics (Q1–17) · syllabus-aligned, solved

## Q1 — Store elements in an array and print

> Write a program in C to store elements in an array and print it.
> **Test data:** input 10 elements → `1 1 2 3 4 5 6 7 8 9`
> **Expected output:** `Elements in array are: 1 1 2 3 4 5 6 7 8 9`

```c
#include <stdio.h>
int main(void) {
    int a[10], i;
    printf("Input 10 elements in the array :\n");
    for (i = 0; i < 10; i++) {
        printf("element - %d : ", i);
        scanf("%d", &a[i]);
    }
    printf("Elements in array are: ");
    for (i = 0; i < 10; i++) printf("%d ", a[i]);
    return 0;
}
```

**Point tested:** the two-loop pattern (read, then display) — see [[module-3-arrays]] §1.6.

## Q2 — Read and display in reverse order

> Write a program in C to read n number of values in an array and display it in reverse order.
> **Test data:** `n = 3`, elements `2 5 7`
> **Expected output:** original `2 5 7` → reversed `7 5 2`

```c
int n, i;
printf("Input the number of elements to store in the array :");
scanf("%d", &n);
for (i = 0; i < n; i++) { scanf("%d", &a[i]); }

printf("The values store into the array in reverse are :\n");
for (i = n - 1; i >= 0; i--) printf("%d ", a[i]);
```

**Point tested:** the reverse-loop off-by-one — start at `n - 1`, not `n`, because `a[n]` is `'\0'`/garbage. Same trap as string reversal in [[module-3-strings]] §3.5.

## Q3 — Sum of all elements

> **Test data:** `n = 3`, `2 5 8` → **Expected output:** `Sum of all elements stored in the array is : 15`

```c
int i, sum = 0;
for (i = 0; i < n; i++) { scanf("%d", &a[i]); }
for (i = 0; i < n; i++) sum += a[i];
printf("Sum of all elements stored in the array is : %d", sum);
```

**Point tested:** `sum` declared and zeroed **before** the loop. Declaring it inside resets it every pass.

## Q4 — Copy one array into another

> **Test data:** `n = 3`, `15 10 12` → both arrays print `15 10 12`

```c
for (i = 0; i < n; i++) { b[i] = a[i]; }      /* element by element */
```

**Point tested:** arrays cannot be assigned wholesale (`b = a;` is illegal in C) — copying always needs a loop. Same principle as strings needing `strcpy` ([[module-3-strings]] §6.2).

## Q5 — Count total duplicate elements

> **Test data:** `n = 3`, `5 1 1` → **Expected output:** `Total number of duplicate elements found in the array is : 1`

```c
int count = 0;
for (i = 0; i < n; i++)
    for (j = i + 1; j < n; j++)
        if (a[i] == a[j]) { count++; break; }   /* count each once */
```

**Points tested:** **nested loops**, `j` starts at `i + 1` (avoids comparing an element with itself), and the `break` (counts each duplicate **once**, not every matching pair).

## Q6 — Print all unique elements

> **Test data:** `n = 4`, `3 2 2 5` → **Expected output:** `The unique elements found in the array are: 3 5`

```c
for (i = 0; i < n; i++) {
    int seen = 0;
    for (j = 0; j < i; j++) if (a[j] == a[i]) seen = 1;
    if (!seen) printf("%d ", a[i]);
}
```

**Point tested:** "did this value appear **before** me?" — `j` runs `0 … i-1`, not `0 … n-1`. Scanning forward would suppress every occurrence.

## Q7 — Merge two same-size arrays, descending

> **Test data:** `1 2 3` and `1 2 3` → **Expected output:** `The merged array in decending order is : 3 3 2 2 1 1`

```c
/* both inputs already sorted ascending; merge then output reversed */
int i = 0, j = 0, k = 0;
while (i < n && j < n) {
    if (a[i] >= b[j]) c[k++] = a[i++];
    else               c[k++] = b[j++];
}
while (i < n) c[k++] = a[i++];
while (j < n) c[k++] = b[j++];
for (k = 2 * n - 1; k >= 0; k--) printf("%d ", c[k]);
```

**Points tested:** the **two-pointer merge** (take from whichever array is currently smaller; the leftovers are then drained by the two `while` loops), and outputting backwards for descending order.

## Q8 — Frequency of each element

> **Test data:** `25 12 43` → `25 occurs 1 times / 12 occurs 1 times / 43 occurs 1 times`

```c
for (i = 0; i < n; i++) {
    int freq = 0;
    for (j = 0; j < n; j++) if (a[j] == a[i]) freq++;
    printf("%d occurs %d times\n", a[i], freq);
}
```

**Point tested:** nested loop + counter. The "have I printed this value already?" refinement (see Q6) avoids duplicate output lines.

## Q9 — Maximum and minimum element

> **Test data:** `45 25 21` → **Expected output:** `Maximum element is : 45` / `Minimum element is : 21`

```c
int max = a[0], min = a[0];
for (i = 1; i < n; i++) {
    if (a[i] > max) max = a[i];
    if (a[i] < min) min = a[i];
}
```

**Points tested:** seeding both from `a[0]` (**not** `0` — fails on all-negative data), loop from `i = 1`, and **two separate `if`s** rather than `else if`. See [[module-3-arrays]] §1.7.

## Q10 — Separate odd and even into two arrays

> **Test data:** `25 47 42 56 32` → **Expected output:** Even `42 56 32`, Odd `25 47`

```c
int e = 0, o = 0;
for (i = 0; i < n; i++) {
    if (a[i] % 2 == 0) even[e++] = a[i];
    else               odd[o++]  = a[i];
}
```

**Points tested:** `%` (modulo) on integers, and **two separate indices** `e` and `o` advancing independently into two destination arrays. Note the source array holds `25 47 42 56 32` but the expected output shows evens first — the exam prints the two groups separately, not interleaved.

## Q11 — Sort ascending

> **Test data:** `2 7 4 5 9` → **Expected output:** `2 4 5 7 9`

Bubble sort, swap condition `a[i] > a[i+1]` — see [[module-3-arrays]] §3.1.

## Q12 — Sort descending

> **Test data:** `5 9 1` → **Expected output:** `9 5 1`

Identical loop with the comparison **reversed**: `if (a[i] < a[i + 1])`. State that explicitly in the exam — swapping the condition, not the whole algorithm.

## Q13 — Insert a new value into a **sorted** list

> **Test data:** `2 5 7 9 11`, insert `8` → `2 5 7 8 9 11`

```c
int pos = 0;
while (pos < n && a[pos] < value) pos++;      /* find the slot */

for (i = n; i > pos; i--) a[i] = a[i - 1];     /* shift right */
a[pos] = value;
n++;
```

**Points tested:** because the list is already sorted you can **find the position directly** — no separate search. The `while` stops at `a[2] = 7` because `7 < 8` is false, so `pos = 3`.

## Q14 — Insert at a **given position** (unsorted)

> **Test data:** `1 8 7 10`, insert `5` at position 2 → `1 5 8 7 10`

Same shift, but `pos` comes from the user instead of a search:

```c
scanf("%d", &pos);                     /* position from the user */
for (i = n; i > pos; i--) a[i] = a[i - 1];
a[pos] = value;
```

**Point tested:** position is **0-based** — position 2 is the **third** slot, so the result is `1 5 8 7 10` (5 lands before 8). Students who treat position as 1-based get `1 8 5 7 10` and lose the mark.

## Q15 — Delete an element at a desired position

> **Test data:** `1 2 3 4 5`, delete position 3 → **Expected output:** `The new list is : 1 2 4 5`

```c
scanf("%d", &pos);                      /* 0-based */
for (i = pos; i < n - 1; i++) a[i] = a[i + 1];    /* shift LEFT */
n--;
```

**Points tested:** shift **left** (opposite direction to insertion), and the bound `i < n - 1` — the last element has no successor to copy from. Position 3 is 0-based → removes the `4`. See [[module-3-arrays]] §3.3.

## Q16 — Second largest element ⭐ highest yield

> **Test data:** `2 9 1 4 6` → **Expected output:** `The Second largest element in the array is : 6`

```c
int first = a[0], second = a[0];
for (i = 1; i < n; i++) {
    if (a[i] > first) { second = first; first = a[i]; }
    else if (a[i] > second && a[i] != first) second = arr[i];
}
printf("The Second largest element in the array is : %d", second);
```

Trace on `2 9 1 4 6`:

| i | a[i] | `a[i] > first`? | action | first | second |
|---|---|---|---|---|---|
| 1 | 9 | yes | shift | 9 | 2 |
| 2 | 1 | no | 1 > 2? no | 9 | 2 |
| 3 | 4 | no | 4 > 2? yes | 9 | 4 |
| 4 | 6 | no | 6 > 4? yes | 9 | **6** |

**The `a[i] != first` guard is the whole question.** Without it, `[5,5,3]` returns 5 as the second largest — the same value twice. With it, second-largest is correctly 3.

## Q17 — Second smallest element

> **Test data:** `0 9 4 6 5` (values must be < 9999) → **Expected output:** `The Second smallest element in the array is : 4`

```c
int first = a[0], second = a[0];
for (i = 1; i < n; i++) {
    if (a[i] < first)  { second = first;  first = a[i]; }
    else if (a[i] < second && a[i] != first) second = a[i];
}
```

**Note the test data starts with `0`** — a deliberate trap for anyone who seeds `first`/`second` to `0` or `9999`. Seeding from `a[0]` is correct. Mirror of Q16 with `<`.

---

# PART B — 2D core (Q18–31) · syllabus-aligned, solved

Theory for all of these: [[module-3-arrays-2d]]. Every solution is the **same three-line nested-loop shape** — `i` = row (outer), `j` = column (inner).

## Q18 — Print a 3×3 matrix

> **Test data:** `1 2 3 / 4 5 6 / 7 8 9` → **Expected output:**
> ```
> The matrix is :
> 1 2 3
> 4 5 6
> 7 8 9
> ```

```c
int i, j;
printf("Input elements in the matrix :\n");
for (i = 0; i < 3; i++)
    for (j = 0; j < 3; j++) {
        printf("element - [%d],[%d] : ", i, j);
        scanf("%d", &m[i][j]);
    }
printf("The matrix is :\n");
for (i = 0; i < 3; i++) {
    for (j = 0; j < 3; j++) printf("%d ", m[i][j]);
    printf("\n");                    /* AFTER the inner loop */
}
```

**Point tested:** where the `printf("\n")` goes — outside the inner loop. Also note the prompt prints the **actual indices** `[i],[j]`, which reinforces that i=row, j=column.

## Q19 — Addition of two matrices ⭐ highest yield

> **Test data:** size `2`, `A = 1 2 / 3 4`, `B = 5 6 / 7 8` → **Expected output:**
> ```
> The Addition of two matrix is :
> 6 8
> 10 12
> ```

```c
int a[2][2] = {{1,2},{3,4}}, b[2][2] = {{5,6},{7,8}}, c[2][2], i, j;
for (i = 0; i < 2; i++)
    for (j = 0; j < 2; j++)
        c[i][j] = a[i][j] + b[i][j];
```

**Points tested:** **two** loops (element-wise), **same dimensions required**, and combining matching `[i][j]` positions.

## Q20 — Subtraction of two matrices

> **Test data:** `A = 5 6 / 7 8`, `B = 1 2 / 3 4` → **Expected output:** `4 4 / 4 4`

Identical to Q19 with `-` instead of `+`. **Do not re-derive it** — in the exam write "same as addition, change `+` to `-`" and show one line.

## Q21 — Multiplication of two square matrices ⭐ highest yield

> **Test data:** `A = 1 2 / 3 4`, `B = 5 6 / 7 8` → **Expected output:**
> ```
> The multiplication of two matrix is :
> 19 22
> 43 50
> ```

```c
int a[2][2] = {{1,2},{3,4}}, b[2][2] = {{5,6},{7,8}}, c[2][2] = {0};
int i, j, k;
for (i = 0; i < 2; i++)
    for (j = 0; j < 2; j++)
        for (k = 0; k < 2; k++)
            c[i][j] += a[i][k] * b[k][j];
```

**Verify by hand — one element:** $c[0][0] = a[0][0]b[0][0] + a[0][1]b[1][0] = (1)(5) + (2)(7) = 5 + 14 = \mathbf{19}$ ✓
$c[0][1] = (1)(6) + (2)(8) = 6 + 16 = \mathbf{22}$ ✓ · $c[1][0] = (3)(5) + (4)(7) = 15 + 28 = \mathbf{43}$ ✓ · $c[1][1] = (3)(6) + (4)(8) = 18 + 32 = \mathbf{50}$ ✓

**Three points tested:** the **third `k` loop** over the shared dimension, the **cumulative `+=`** (so `c` must be initialised to `{0}`), and the validity rule $C_1 = R_2$.

## Q22 — Transpose

> **Test data:** `1 2 / 3 4` → **Expected output:** `1 3 / 2 4`

```c
int t[3][3], i, j;                 /* dimensions swap */
for (i = 0; i < 2; i++)
    for (j = 0; j < 2; j++)
        t[j][i] = a[i][j];
```

**Points tested:** the **indices swap** (`t[j][i]`, not `t[i][j]`), and the destination is declared **transposed** — `a` is 2×2 here so it is not visible, but for a 3×4 input you must write `int t[4][3];` or the compiler will reject it.

## Q23 — Sum of right diagonals

> **Test data:** `1 2 / 3 4` → **Expected output:** `Addition of the right Diagonal elements is :5`

```c
int sum = 0;
for (i = 0; i < n; i++) sum += m[i][i];        /* i == j */
```

Right/main diagonal: `1 + 4 = 5`.

## Q24 — Sum of left diagonals

> **Test data:** `1 2 / 3 4` → **Expected output:** `Addition of the left Diagonal elements is :5`

```c
int sum = 0;
for (i = 0; i < n; i++) sum += m[i][n - 1 - i];   /* i + j == n-1 */
```

Left/anti-diagonal: `2 + 3 = 5`. **The condition `i + j == n - 1` only holds for a square matrix.**

## Q25 — Sum of rows and columns

> **Test data:** `5 6 / 7 8` → **Expected output:**
> ```
> The sum or rows and columns of the matrix is :
> 5 6 11
> 7 8 15
> 12 14
> ```

```c
for (i = 0; i < n; i++) {
    int r = 0, c = 0;
    for (j = 0; j < n; j++) { r += m[i][j]; c += m[j][i]; }
    printf("%d %d %d\n", m[i][0], m[i][1], r);   /* matrix row + row sum */
    /* then after the loop, print the column sums and grand total */
}
```

**Points tested:** **`m[j][i]`** to walk a column while the counter stays the same, and both accumulators declared **inside** the outer loop so they reset each row. The expected output is ambiguous in the source (it mixes matrix rows, row sums and column sums) — say so if asked.

## Q26 — Lower triangular matrix

> **Test data:** `1 2 3 / 4 5 6 / 7 8 9` → **Expected output:**
> ```
> Setting zero in lower triangular matrix
> 1 2 3
> 0 5 6
> 0 0 9
> ```

```c
for (i = 0; i < n; i++)
    for (j = 0; j < n; j++)
        if (i > j) m[i][j] = 0;         /* strictly below the diagonal */
```

## Q27 — Upper triangular matrix

> **Expected output:**
> ```
> 1 0 0
> 4 5 0
> 7 8 9
> ```

Same loop with `if (i < j)`. **The diagonal (`i == j`) is kept in both.** Sum of upper triangle here = `2 + 3 + 6 = 11`; lower = `4 + 7 + 8 = 19`.

## Q28 — Determinant of a 3×3 matrix

> **Test data:**
> ```
> 1   0  -1
> 0   0   1
> -1 -1   0
> ```
> **Expected output:** `The Determinant of the matrix is: 1`

```c
int det = m[0][0]*(m[1][1]*m[2][2] - m[1][2]*m[2][1])
        - m[0][1]*(m[1][0]*m[2][2] - m[1][2]*m[2][0])
        + m[0][2]*(m[1][0]*m[2][1] - m[1][1]*m[2][0]);
```

$|A| = 1(0\cdot0 - 1\cdot(-1)) - 0(\cdot) + (-1)(0\cdot(-1) - 0\cdot(-1)) = 1(1) - 0 + (-1)(0) = \mathbf{1}$ ✓

**Points tested:** the **sign pattern `+ − +`** when expanding along the first row. This is the most commonly lost mark in the whole 2D set.

## Q29 — Sparse matrix check

> **Test data:** `0 0 / 1 0` → **Expected output:**
> ```
> The given matrix is sparse matrix.
> There are 3 number of zeros in the matrix
> ```

```c
int zeros = 0;
for (i = 0; i < r; i++)
    for (j = 0; j < c; j++)
        if (m[i][j] == 0) zeros++;
if (zeros > (r * c) / 2) printf("The given matrix is sparse matrix.\n");
printf("There are %d number of zeros in the matrix\n", zeros);
```

**Point tested:** count zeros, then compare against `r*c/2`. Note the source's expected output uses "sparse matrix" for a 2×2 with 3 zeros — 3 > 2 ✓.

## Q30 — Check whether two matrices are equal

> **Test data:** both `1 2 / 3 4` → **Expected output:** `Two matrices are equal.`

```c
int equal = (r1 == r2 && c1 == c2);
for (i = 0; i < r1 && equal; i++)
    for (j = 0; j < c1; j++)
        if (a[i][j] != b[i][j]) { equal = 0; break; }
```

**Points tested:** **dimensions first, elements second** — comparing differently-shaped matrices reads out of bounds.

## Q31 — Identity matrix check

> **Test data:**
> ```
> 1 0 0
> 0 1 0
> 0 0 1
> ```
> **Expected output:** `The matrix is an identity matrix.`

```c
int isId = 1;
for (i = 0; i < n; i++)
    for (j = 0; j < n; j++)
        if ((i == j && m[i][j] != 1) || (i != j && m[i][j] != 0))
            isId = 0;
```

**Points tested:** **both** conditions must hold — diagonal is 1 **and** off-diagonal is 0. A single `else` chain is the usual wrong answer.

---

# PART C — Advanced / DSA-flavored (Q32–107)

> **The source file's own verdict:** *"extension bank beyond ESE, good for quiz predict-output and interviews."*
> **Not examinable under Module 3.1.** Listed with topic + expected output so you recognise them and can attempt the interesting ones — but do not spend exam-prep time here before Parts A and B are solid. All are 1D except Q50, Q60, Q67, Q72, Q85, Q89 (2D).

## C1 — Searching & ordering (Q32–Q49)

| # | Topic | Input → Expected output |
|---|---|---|
| Q32 | Pair with given sum | `6 8 4 -5 7 9`, sum `15` → "index 0 and 5" ⚠️ *printed values wrong: `6+9=15` is index 0 and 5 — the values should be 6 and 9, not the array entries* |
| Q33 | Majority element (> n/2) | `4 8 4 6 7 4 4 8` → "no majority" (4 appears 4× of 8 — **not** *more than* n/2) |
| Q34 | Element occurring odd number of times | `8 3 8 5 4 3 4 3 5` → `3` |
| Q35 | Largest sum of contiguous subarray (Kadane) | `8 3 8 -5 4 3 -4 3 5` → `21` |
| Q36 | Missing number in 1..n, no duplicates | `1 3 4 2 5 6 9 8` → `7` |
| Q37 | Pivot of sorted-rotated array (binary search) | `14 23 7 9 3 6 18 22 16 36` → `3` |
| Q38 | Merge one sorted array into another | `10 12 14 16 18 20 22` + `11 13 15 17 19 21` → `10 11 … 22` |
| Q39 | Rotate array by N positions | `0 3 6 9 12 14 18 20 22 25 27`, from 4th → `12 14 18 20 22 25 27 0 3 6 9` |
| Q40 | Ceiling in a sorted array | `1 3 4 7 8 9 9 10`, ceiling of `5` → `7` |
| Q41 | Floor and ceiling of 0..10 | `1 3 5 7 8 9` → ceiling(0)=1 floor(0)=`-1`; ceiling(10)=`-1` floor(10)=9 — **`-1` when absent** |
| Q42 | Smallest missing element (sorted) | `0 1 3 4 5 6 7 9` → `2` |
| Q43 | Next greater element | `5 3 10 9 6 13` → `10 10 13 13 13 -1` (`-1` when none) |
| Q44 | Two repeating elements | `2 7 4 7 8 3 4` → `7 4` |
| Q45 | Pair whose sum is closest to zero | `38 44 63 -51 -35 19 84 -69 4 -46` → `[44, -46]` |
| Q46 | Smallest positive missing number | `3 1 4 10 -5 15 2 -10 -20` → `5` |
| Q47 | Subarray with given sum (index ranges) | `3 4 -7 1 3 3 1 -4` → `[0..1] [0..5] [3..5] [4..6]` |
| Q48 | Does x appear > n/2 times (sorted) | `1 3 3 5 4 3 2 3 3`, x=`3` → yes |
| Q49 | Majority element | `1 3 3 7 4 3 2 3 3` → `3` |

## C2 — Sorting & rearrangement (Q50–Q58, Q73, Q76, Q77, Q79, Q82)

| # | Topic | Input → Expected output |
|---|---|---|
| Q50 | **Print matrix in spiral form** (2D) | 4×5 `1..20` → `1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12` |
| Q51 | Maximum circular subarray sum | `10 8 -20 5 -3 -5 10 -13 11` → `29` |
| Q52 | Count triangles from array | `6 18 9 7 10` → `5` |
| Q53 | Frequency of a given number | `2 3 4 4 4 4 5 5 5 6 7 7`, count `4` → `4` |
| Q54 | **Sort an array of 0s, 1s and 2s** | `0 1 2 2 1 0 0 2 0 1 1 0` → `0 0 0 0 0 1 1 1 1 2 2 2` |
| Q55 | Is array B a subset of array A | `4 8 7 11 6 9 5 0 2` and `5 4 2 0 6` → subset |
| Q56 | Minimum jumps to reach the end | `1 3 5 8 9 2 6 7 6 8 9 1 1 1` → `3` |
| Q57 | Minimum in a sorted-rotated array | `3 4 5 6 7 9 2` → `2` |
| Q58 | Move all zeroes to the end (order preserved) | `2 5 7 0 4 0 7 -5 8 0` → `2 5 7 8 4 -5 7 0 0 0` |
| Q73 | All unique elements of an unsorted array | `1 5 8 5 7 3 2 4 1 6 2` → `1 5 8 7 3 2 4 6` |
| Q76 | Largest number possible by rearranging | `15 628 971 9 2143 12` → `997162821431512` |
| Q77 | Random permutation (shuffle) | `1..8` → `2 8 7 3 4 5 1 6` |
| Q79 | Sort n numbers in range 0..n² | `37 62 52 7 48 3 15 61` → `3 7 15 37 48 52 61 62` |
| Q82 | All combinations of r elements | `1 5 4 6 8`, r=4 → `1 5 4 6 / 1 5 4 8 / 1 5 6 8 / 1 4 6 8 / 5 4 6 8` |

**Note on Q54 vs Q58:** both move values around, but Q58 must **preserve the relative order of the non-zero elements** (`2 5 7 8 4 -5 7` keeps 7 before 8 before 4 before -5), which needs a **write index**. A naive swap-to-end gets the answer wrong. That distinction is worth knowing even though Q58 is out of scope.

## C3 — Matrix / 2D advanced (Q60, Q67, Q72, Q85, Q89, Q74, Q75)

| # | Topic | Input → Expected output |
|---|---|---|
| Q60 | Row with the maximum number of 1s | 5×5 binary → row index `1` |
| Q67 | Search in row-wise + column-wise sorted matrix | 4×4, find `37` → position `2, 2` (start from top-right) |
| Q72 | Unique rows in a binary matrix | 3×5 → `0 1 0 0 1 / 1 0 1 1 0 / 1 0 1 0 0` |
| Q74 | Sum of upper-triangular elements | `1 2 3 / 4 5 6 / 7 8 9` → elements `2 3 6`, sum `11` |
| Q75 | Sum of lower-triangular elements | same matrix → elements `4 7 8`, sum `19` |
| Q85 | Count all paths top-left → bottom-right (m×n) | 4×4 → `20` |
| Q89 | Maximum square sub-matrix of all 1s (DP) | 6×5 binary → a **4×4** block of 1s |

## C4 — Two-pointer, sliding window & misc (Q59, Q61–Q71, Q78–Q81, Q84, Q91–Q107)

| # | Topic | Input → Expected output |
|---|---|---|
| Q59 | **Counting sort** | `4 14 8 0 2 5 2 1 0 17 9 0 5` → `0 0 0 1 2 2 4 5 5 8 9 14 17` |
| Q61 | Maximum product subarray | `-4 9 -7 0 -15 6 2 -3` → `540` |
| Q62 | Largest subarray with equal 0s and 1s | `0 1 0 0 1 1 0 1 1 1` → index `0 to 7` |
| Q63 | Replace each element with the greatest to its right | `7 5 8 9 6 8 5 7 4 6` → `9 9 9 8 8 7 7 6 6 0` (last becomes `0` — nothing to its right) |
| Q64 | Median of two sorted arrays (same size) | `1 5 13 24 35` and `3 8 15 17 32` → `14` |
| Q65 | Product of array except self | `1 2 3 4 5 6` → `720 360 240 180 144 120` |
| Q66 | Count inversions | `1 9 6 4 5` → pairs `(9,6)(9,4)(9,5)(6,4)(6,5)` → `5` |
| Q68 | Maximum sum, no two adjacent | `1 3 5 9 7 10 1 10 100` → `122` |
| Q69 | Maximum difference (larger element after smaller) | `7 9 5 6 13 2` → `5, 13` → difference `8` |
| Q70 | Two numbers occurring an odd number of times | `6 7 3 6 8 7 6 8 3 3` → `3 & 6` |
| Q71 | Median of two sorted arrays (different sizes) | `90 240 300` and `10 13 14 20 25` → `22.5` (use `float`/double, not int!) |
| Q78 | Four elements summing to a target | `3 7 1 9 15 14 6 2 5 7` → `3, 15, 14, 5` |
| Q80 | Distinct pairs for a given difference | `5 2 3 7 6 4 9 8`, diff `5` → `[7,2] [8,3] [9,4]` → `3` |
| Q81 | Maximum repeating number | `2 3 3 5 3 4 1 7 7 7 7` → `7` |
| Q83 | Pair with a given difference | `1 15 39 75 92`, diff `53` → `(39, 92)` |
| Q84 | Minimum distance between two values | `7 9 5 11 7 4 12 6 2 11` → between `7` and `11` = `1` |
| Q86 | Equilibrium index | `0 -4 7 -4 -2 6 -3 0` → index `5` |
| Q87 | Maximum in a bitonic (increasing-then-decreasing) array | `2 7 12 25 4 57 27 44` → `57` |
| Q88 | Maximum `j - i` such that `arr[j] > arr[i]` | `7 5 8 2 3 2 4 2 1 0` → `3` |
| Q90 | Rearrange so `arr[i] == arr[arr[i]]` | `2 1 4 3 0` → `4 1 0 3 2` (cycle decomposition) |
| Q91 | Min-length subarray whose sort sorts the whole array | `10 12 15 17 28 32 42 18 56 59 67` → indices `4` to `7` |
| Q92 | Do elements appear consecutively? | `7 4 3 5 6 2` yes · `7 4 4 5 6 2` no · `7 4 9 5 6 3` no |
| Q93 | Rearrange positive/negative alternately | `-4 8 -5 -6 5 -9 7 1 -21 -11 19` → `-4 7 -5 1 -21 5 -11 8 -9 19 -6` |
| Q94 | Max of every contiguous subarray of size k | k=4 over `1 3 6 21 4 9 12 3 16 10` → `21 21 21 21 12 16 16` |
| Q95 | Segregate 0s and 1s | `1 0 1 0 0 1 0 1 1` → `0 0 0 0 1 1 1 1 1` |
| Q96 | Segregate even/odd | `17 42 19 7 27 24 30 54 73` → `54 42 30 24 27 7 19 17 73` |
| Q97 | Index of first peak element | `5 12 13 20 16 19 11 7 25` → index `3` |
| Q98 | Largest span between equal values (inclusive) | `17 42 19 7 27 24 17 54 73` → `7` |
| Q99 | Split point where left sum = right sum | `1 3 3 8 4 3 2 3 3` → yes, can be split |
| Q100 | Count clumps (runs of ≥2 equal adjacent values) | `17 42 42 7 24 24 17 54 17` → `2` |
| Q101 | Rearrange so `arr[i] = i` (−1 for absent) | `2 5 -1 6 -1 8 7 -1 9 1` → `-1 1 2 -1 -1 5 6 7 8 9` |
| Q102 | Rearrange min, max, 2nd min, 2nd max, … | `5 8 1 4 2 9 3 7 6` → `1 9 2 8 3 7 4 6 5` |
| Q103 | Each element = product of its neighbours | `1 2 3 4 5 6` → `2 3 8 15 24 30` |
| Q104 | Even-index elements smaller, odd-index greater than next | `6 4 2 1 8 3` → `4 6 1 8 2 3` |
| Q105 | Min swaps to gather all elements ≤ k | `2 7 9 5 8 7 4`, k implied → `2` |
| Q106 | Double equal neighbours, then shift zeros to end | `0 3 3 3 0 0 7 7 0 9` → `6 3 14 9 0 0 0 0 0 0` |
| Q107 | Concatenate two integer arrays | `{10,20,30,40,50,60}` + `{70,80,90,100,110,120}` → `10 20 … 120` |

---

## Self-test — 6 questions across Part A and B

1. In Q16 on `{2,9,1,4,6}`, what are `first` and `second` after the loop, and which line would break on `{5,5,3}`?
2. Q14: position `2` on `1 8 7 10` — is the result `1 5 8 7 10` or `1 8 5 7 10`? Why?
3. Q15: why is the loop bound `i < n - 1` and not `i < n`?
4. Q21: compute `c[0][0]` by hand for `A = 1 2/3 4`, `B = 5 6/7 8`.
5. Q28: what changes if you expand the determinant along the **second** row instead of the first?
6. Q31: why must the identity check test **both** the diagonal and the off-diagonal?

<details><summary>Answers</summary>

1. `first = 9`, `second = 6`. On `{5,5,3}` the line `else if (a[i] > second && a[i] != first)` is what fails — without `a[i] != first`, the duplicate `5` would be taken as `second`, giving 5 instead of the correct 3.
2. **`1 5 8 7 10`.** Positions are **0-based**, so position 2 is the third slot; 5 is written there and 8 shifts right. `1 8 5 7 10` is the 1-based misreading.
3. Because the last element has **no successor** — `a[n-1]` is the final value, so copying `a[i] = a[i+1]` at `i = n-1` would read one past the array.
4. $c[0][0] = a[0][0]b[0][0] + a[0][1]b[1][0] = (1)(5) + (2)(7) = 19$.
5. Only the **sign pattern** — it becomes `− + −` — and that row is treated as the "first" row. The formula shape is identical; expanding along a row always alternates starting `+`.
6. An identity matrix needs **1 on the diagonal AND 0 everywhere else**. Testing only the diagonal would accept `[[1,5],[5,1]]`; testing only the off-diagonal would accept `[[2,0],[0,2]]`.
</details>

---

## Cross-References

- **Theory:** [[module-3-arrays]] (1D) · [[module-3-arrays-2d]] (2D)
- **Registry of all three PIC sets:** [[spm-pic-question-bank]] — 26 conditional + 59 loop + 107 array
- **Hub:** [[module-3-arrays-strings]] · **Strings questions:** [[module-3-strings]] §9
- **Assessment:** [[assessment-guide-ese-ost-quiz]] · **Lab:** [[spm-lab-exp3-4-5-guides]]
- **Drills:** [[spm-practice-bank-module2]] · [[spm-quiz-bank]] · [[c-programming-master-study-guide]]

*Ingested 2026-10-02 from `raw-sources/drive-download-20260908T190917Z-1-001/Semester 1/SPM/PIC Practice question_Array.docx` (107 questions, 31.5 K chars extracted). Question wording and test data verbatim.*

