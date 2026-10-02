---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "Module 3.1b — Multidimensional (2D) Arrays"
date: "2026-10-02"
last_updated: "2026-10-02"
description: "SPM M3.1b two-dimensional arrays and matrices — row-major vs column-major with both address formulas, why the column count is mandatory, nested-loop traversal, matrix add/subtract/multiply/transpose, diagonal and row-column sums, triangular matrices, 3x3 determinant, sparse and identity checks, spiral print, with flowcharts, address drills and 5 practice questions."
tags: [spm, arrays, 2d-arrays, matrices, c-programming, 316U06C107, row-major, column-major, address-formula, transpose, determinant, sparse-matrix, identity-matrix, spiral, exam-prep, lab]
confidence: high
aliases: ["2D arrays", "matrices", "multidimensional arrays", "SPM 2D arrays"]
prerequisites: ["[[module-3-arrays]]", "Nested loops (Module 2)"]
sources:
  - "raw-sources/SPM Lecture/SPM_Module3_1.pptx"
  - "raw-sources/SPM Lecture/Unit No.3 Arrays_Strings.pdf"
  - "raw-sources/SPM Lab/EX4.docx"
  - "raw-sources/SPM SEM1 work/.../PIC Practice question_Array.docx"
---

## For future agent

**The dedicated TWO-DIMENSIONAL arrays page**, split from [[module-3-arrays]] on 2026-10-02 at the user's request (arrays was the self-declared weak area). The 1D half — declaration, `B+i*S`, search/sort/insert/delete — stays in [[module-3-arrays]].

**Source enrichment:** the faculty deck only teaches matrix *addition*. The **transposition, multiplication, transpose, diagonal sums, row/column sums, triangular matrices, 3×3 determinant, sparse check, equality check, identity check, spiral print, max-1s row and max-square** operations here are drawn from the real exam bank `PIC Practice question_Array.docx` (Q18-Q31, Q50, Q60, Q67, Q72, Q85, Q89) — so this page covers what the exam actually asks, not just what the deck demonstrates. Full question text with test data: [[spm-array-question-bank]].

**The one rule that generates exam questions:** the first index is always the **row**, the second always the **column**, and **both are zero-based**. Almost every 2D bug is a swapped or off-by-one index.

---

# Module 3.1b — Multidimensional (2D) Arrays

> **Syllabus 3.1** ([[syllabus-316U06C107]]): *Arrays: 1D, **Multidimensional**, Declaration/Initialization, Reading/Displaying.* CO3.
> **1D half:** [[module-3-arrays]] · **Exam bank:** [[spm-array-question-bank]] · Hub: [[module-3-arrays-strings]]

---

## 0. The four sentences that cover 2D

1. A 2D array is **an array of arrays** — physically **one linear block** of `rows × cols` elements.
2. `arr[rows][cols]` — **first index = row, second = column.** They cannot be swapped.
3. C is **row-major**: a whole row sits next in memory, so the address is `base + (i*C + j)*S`.
4. **The column count is mandatory** in the declaration — the compiler needs it to compute the address. The row count is not.

---

## 1. The concept

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

A marks example makes the index order concrete: **4 students in 3 subjects → `int marks[4][3];`** — rows = students (4), columns = subjects (3).

---

## 2. Memory layout — row-major vs. column-major

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

**Worked drill.** `int a[3][5]`, base 2000, `sizeof(int)=4`, find `a[2][3]`:

- Row-major: $2000 + (2\times5 + 3)\times4 = 2000 + 52 = \boxed{2052}$
- Column-major: $2000 + (3\times3 + 2)\times4 = 2000 + 44 = \boxed{2044}$

**Why row-major matters in real code:** CPUs load memory in cache *lines* (~64 bytes). Walking a **row** uses one line for many elements. Walking a **column** in a row-major array jumps a whole row each step → a cache miss per access. So **outer = row, inner = column** is the fast order in C.

**This is precisely why the column count must be known at compile time** — the compiler needs `C` to evaluate `i*C + j`. Without it there is no way to find where row $i$ begins.

---

## 3. Declaration and initialization

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

---

## 4. Traversal — nested loops

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

### 4.1 Flowcharts

```
   READ / DISPLAY A MATRIX            TRANSPOSE
   i <- 0                             t[j][i] = a[i][j]
      |                               for i: 0..R-1
      v                                 for j: 0..C-1
   i < R ?  --NO--> stop
      |YES                            note: t must be C rows x R cols
      v
   j <- 0
      |
      v
   j < C ?  --NO--> i <- i+1, loop
      |YES
      v
   act on a[i][j]
      |
      v
   j <- j+1, loop
```

```
   ADD / SUBTRACT                       MULTIPLY
   c[i][j] = a[i][j] + b[i][j]        for i: 0..R1-1
   c[i][j] = a[i][j] - b[i][j]        for j: 0..C1-1
   (same dimensions required)            for k: 0..C2-1
                                          c[i][j] += a[i][k] * b[k][j]
```

---

## 5. Matrix operations

All of these are real exam questions (PIC Q18-Q31, Q50). Solutions below.

### 5.1 Addition and subtraction

```
A =        B =          C = A + B:     D = A - B:
1  2       5  6         6   8          4   4
3  4       7  8        10  12         4   4
```

```c
int a[2][2] = {{1, 2}, {3, 4}};
int b[2][2] = {{5, 6}, {7, 8}};
int sum[2][2], dif[2][2], i, j;

for (i = 0; i < 2; i++) {
    for (j = 0; j < 2; j++) {
        sum[i][j] = a[i][j] + b[i][j];
        dif[i][j] = a[i][j] - b[i][j];
    }
}
```

**Two matrices can only be added or subtracted if they have the SAME dimensions**, and each element combines with the element at the **identical `[i][j]` position**.

### 5.2 Multiplication — the three-loop version

```c
int A[2][2] = {{1,2},{3,4}}, B[2][2] = {{5,6},{7,8}}, C[2][2] = {0};

for (i = 0; i < 2; i++)
    for (j = 0; j < 2; j++)
        for (k = 0; k < 2; k++)
            C[i][j] += A[i][k] * B[k][j];
```

**Result:** `19 22` / `43 50`.

**Why three loops for multiply but two for add?** Addition is *element-wise* — one output per input pair. Multiplication is `C[i][j] = Σₖ A[i][k]·B[k][j]` — an inner accumulation over the shared dimension `k`. **The `k` loop is what makes it multiplication; dropping it silently gives you Hadamard (element-wise) product instead, which is a very common mistake.**

**Validity:** `A` is R₁×C₁, `B` is R₂×C₂ → the product needs **C₁ == R₂**. `C` is R₁×C₂.

### 5.3 Transpose

```c
int t[C][R];                        /* note: dimensions SWAP */
for (i = 0; i < R; i++)
    for (j = 0; j < C; j++)
        t[j][i] = a[i][j];          /* swap the indices */
```

```
   A =        Aᵀ =
   1  2       1  3
   3  4       2  4
```

**The whole operation is swapping `i` and `j`.** The result of an R×C transpose is **C×R**, so the destination array must be declared the other way round — a frequent source of compile errors or partial output.

### 5.4 Diagonal sums

```
   M =            Right diagonal (i == j):  1 + 4 = 5
   1  2           Left  diagonal (i+j == n-1): 2 + 3 = 5
   3  4
```

```c
int rightSum = 0, leftSum = 0;
for (i = 0; i < n; i++) {
    rightSum += m[i][i];              /* main diagonal */
    leftSum  += m[i][n - 1 - i];      /* anti-diagonal */
}
```

Both conditions in one loop. Only meaningful for a **square** matrix — a non-square matrix has no true diagonals.

### 5.5 Row sums and column sums

```
   M =          Row sums:  5+6 = 11,  7+8 = 15
   5  6         Col sums:  5+7 = 12,  6+8 = 14
   7  8         Grand total = 26
```

```c
for (i = 0; i < n; i++) {
    int rowSum = 0, colSum = 0;
    for (j = 0; j < n; j++) {
        rowSum += m[i][j];      /* across the row  */
        colSum += m[j][i];      /* down the column */
    }
    printf("row %d = %d, col %d = %d\n", i, rowSum, i, colSum);
}
```

Note `m[j][i]` in the inner loop — **the indices swap** to walk down a column while the loop counter stays the same.

### 5.6 Triangular matrices

```
   M =            Upper (i <= j): 1 2 3 / _ 5 6 / _ _ 9
   1  2  3        Lower (i >= j): 1 _ _ / 4 5 _ / 7 8 9
   4  5  6
   7  8  9
```

```c
/* zero out the LOWER triangle (i > j) */
for (i = 0; i < n; i++)
    for (j = 0; j < n; j++)
        if (i > j) m[i][j] = 0;

/* zero out the UPPER triangle (i < j) */
        if (i < j) m[i][j] = 0;
```

**Diagonal position test:** `i == j` for the main diagonal, `i + j == n - 1` for the anti-diagonal, `i > j` for lower, `i < j` for upper. The **sum** of the upper triangle in the 3×3 example is `2 + 3 + 6 = 11`; the lower is `4 + 7 + 8 = 19`.

### 5.7 Determinant of a 3×3

Only defined for a **square** matrix. Expanding along the first row:

$$|A| = a(ei - fh) - b(di - fg) + c(dh - eg)$$

```c
int det3(int m[3][3]) {
    return m[0][0] * (m[1][1]*m[2][2] - m[1][2]*m[2][1])
         - m[0][1] * (m[1][0]*m[2][2] - m[1][2]*m[2][0])
         + m[0][2] * (m[1][0]*m[2][1] - m[1][1]*m[2][0]);
}
```

**Worked check** — the matrix from the exam question:

```
   1   0  -1
   0   0   1
  -1  -1   0
```

$$|A| = 1(0\cdot0 - 1\cdot(-1)) - 0(\ldots) + (-1)(0\cdot(-1) - 0\cdot(-1)) = 1(1) - 0 + (-1)(0) = \boxed{1}$$

**The sign pattern is `+ − +`** — expanding along the first row alternates. Getting this wrong is the single most common determinant bug.

### 5.8 Sparse and identity matrices

**Sparse** — most entries are zero. Conventionally "sparse" means **more than half** the entries are zero:

```c
int zeros = 0, total = r * c;
for (i = 0; i < r; i++)
    for (j = 0; j < c; j++)
        if (m[i][j] == 0) zeros++;

if (zeros > total / 2) printf("The given matrix is sparse matrix.\n");
printf("There are %d number of zeros in the matrix\n", zeros);
```

**Identity** — 1s on the main diagonal, 0s everywhere else:

```c
int isIdentity = 1;
for (i = 0; i < n; i++)
    for (j = 0; j < n; j++)
        if ((i == j && m[i][j] != 1) || (i != j && m[i][j] != 0))
            isIdentity = 0;
```

Two separate tests because **both** conditions must hold — the diagonal must be 1 *and* the off-diagonal must be 0.

**Matrix equality** — same dimensions, and every pair of elements equal:

```c
int equal = (r1 == r2 && c1 == c2);
if (equal)
    for (i = 0; i < r1 && equal; i++)
        for (j = 0; j < c1; j++)
            if (a[i][j] != b[i][j]) { equal = 0; break; }
```

**Check dimensions first, elements second** — comparing elements of differently-shaped matrices reads out of bounds.

### 5.9 Spiral print

```
   1  2  3  4  5        Clockwise from the top-left:
   6  7  8  9 10        1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12
  11 12 13 14 15
  16 17 18 19 20
```

**The algorithm — four boundaries that shrink after each pass:**

```
   top = 0, bottom = R-1, left = 0, right = C-1

   while (top <= bottom && left <= right) {
       print a[top][j]    for j = left .. right ; top++
       print a[i][right]  for i = top .. bottom ; right--
       if (top <= bottom) { print a[bottom][j] for j = right .. left ; bottom-- }
       if (left <= right)  { print a[i][left]   for i = bottom .. top ; left++ }
   }
```

**The two `if` guards are essential.** Without them a single-row or single-column matrix double-prints its middle. Getting the shrink order right (`top++` after printing the top row, etc.) is the whole exercise.

### 5.10 Two advanced patterns

**Row with the maximum number of 1s** (PIC Q60) — exploit the fact that rows of 0s then 1s have their first 1 at the boundary; count from the right:

```c
for (i = 0; i < R; i++) {
    int ones = 0;
    for (j = C - 1; j >= 0 && m[i][j] == 1; j--) ones++;
    if (ones > maxOnes) { maxOnes = ones; rowIdx = i; }
}
```

**Maximum square sub-matrix of all 1s** (PIC Q89) — DP, one pass:

```c
/* dp[i][j] = size of the largest all-1 square with bottom-right corner at (i,j) */
dp[i][j] = (m[i][j] == 1) ? 1 + MIN(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) : 0;
```

Track the running maximum and its position. This is **beyond ESE scope** but appears in the bank — know it exists, don't be examined on it.

---

## 6. Exam address drills

| Given | Asked | Answer |
|---|---|---|
| `int a[3][5]`, base 2000, S=4 | `a[2][3]` row-major | $2000 + (2{\cdot}5+3)(4) = \mathbf{2052}$ |
| same | `a[2][3]` column-major | $2000 + (3{\cdot}3+2)(4) = \mathbf{2044}$ |
| `float m[2][5]`, base 5000, S=4 | `m[1][3]` row-major | $5000 + (1{\cdot}5+3)(4) = \mathbf{5032}$ |
| `int a[3][4]` | number of elements | $3 \times 4 = \mathbf{12}$ |
| `int a[3][4]`, base B | offset of `a[2][0]` | $2 \times 4 + 0 = \mathbf{8}$ elements |

**Worked example — partial init and `sizeof`:**

```c
int x[6] = {1, 2, 3};
printf("%d %d\n", x[3], x[4]);              /* 0 0  */
printf("%zu\n", sizeof(x) / sizeof(x[0]));  /* 6    */
```

Partial initialization zero-fills → `{1, 2, 3, 0, 0, 0}`. Element count = $24/4 = 6$.

---

## 7. Practice Questions

**Q1 — 2D fundamentals**
1. Declare a 2D array for the marks of **4 students in 3 subjects**. Row and column counts?
2. Sum all elements of a 3×3 matrix using nested loops.
3. Change matrix addition to subtraction.

<details><summary>Answers</summary>

1. `int marks[4][3];` → 4 rows, 3 columns. **Rows = students, columns = subjects.**
2. `for (i=0;i<3;i++) for (j=0;j<3;j++) total += m[i][j];`
3. `c[i][j] = a[i][j] - b[i][j];`
</details>

**Q2 — the off-by-one traps**
1. `int m[3][];` — does it compile? What about `int m[][3];`?
2. In `printf("%d", m[3][0]);` on a 3×3 matrix, what is wrong and what happens?
3. Your 3×3 loop prints 9 values but all on one line. Where did the `printf("\n")` go?

<details><summary>Answers</summary>

1. `int m[3][]` is a **compile error** — the column count is mandatory. `int m[][3]` is legal.
2. Rows are `0,1,2`, so `m[3]` is one past the end — **undefined behaviour**, silently reading unrelated memory.
3. It must be inside the **outer** loop but **outside** the inner one.
</details>

**Q3 — matrix operations**
1. Transpose a 3×4 matrix. What are the dimensions of the result?
2. Why does matrix multiply need three loops when add needs two?
3. Expand the 3×3 determinant along the **second** row instead — what changes?

<details><summary>Answers</summary>

1. The result is **4×3**. The destination must be declared `int t[4][3];`.
2. Multiply sums over a shared dimension: `C[i][j] = Σₖ A[i][k]·B[k][j]`. Drop the `k` loop and you get element-wise (Hadamard) product, not matrix product.
3. Only the **sign pattern** changes (`− + −`) and you index that row as the "first" row. The formula shape is identical.
</details>

---

## 8. Quick Test — 2D (5 questions)

| # | Type | Question | Answer |
|---|---|---|---|
| Q1 | MCQ | In `int a[2][3] = {{1,2,3},{4,5,6}};` how many elements? | **6** |
| Q2 | Code trace | `int a[2][3] = {{1,2,3},{4,5,6}};` value of `a[1][2]`? | **6** |
| Q3 | Short answer | Why can the row count be omitted but not the column count? | The compiler needs the row width `C` to compute `i*C + j` and find where each row starts |
| Q4 | Short answer | Why is outer-loop-rows the faster order in C? | C is row-major, so walking a row reuses one cache line; walking a column jumps a whole row per access |
| Q5 | True/False | The transpose of a 3×4 matrix is also 3×4. | **False** — it is **4×3**; transpose swaps the dimensions |

---

## 9. Formula & Syntax Quick Reference

| Quantity | Formula / pattern | Notes |
|---|---|---|
| Row-major address | $B + (i \times C + j) \times S$ | C / C++ / Java |
| Column-major address | $B + (j \times R + i) \times S$ | FORTRAN / MATLAB |
| Transpose | `t[j][i] = a[i][j]` | result is C×R |
| Matrix multiply | `C[i][j] += A[i][k]*B[k][j]` | three loops; needs $C_1 = R_2$ |
| Main diagonal | `i == j` | |
| Anti-diagonal | `i + j == n - 1` | square only |
| Lower / upper triangle | `i > j` / `i < j` | |
| 3×3 determinant | $a(ei-fh) - b(di-fg) + c(dh-eg)$ | sign pattern `+ − +` |
| Identity test | `(i==j && m!=1) \|\| (i!=j && m!=0)` | both must hold |
| Sparse test | `zeros > (r*c)/2` | convention, not universal |
| Total elements | `rows × cols` | |

---

## Cross-References

- **1D half of this topic:** [[module-3-arrays]] — declaration, `B+i*S`, search/sort/insert/delete
- **Exam question bank:** [[spm-array-question-bank]] — all 107 questions with test data (2D core = Q18-Q31)
- **Module map / routing:** [[module-3-arrays-strings]]
- **Strings:** [[module-3-strings]] — a `char` array *is* a 1D array
- **Lab:** [[spm-lab-exp3-4-5-guides]] (EXP4 Sample Program 5-6 — 2D display, matrix addition)
- **Loops:** [[module-2-program-control-functions]] (nested loops §1.5)
- **Foundations:** [[module-1-spm-c-basics]] (memory layout) · [[module-4-structures-unions-pointers]] (pointer arithmetic on 2D)

*Sources ingested 2026-10-02: `SPM_Module3_1.pptx` (slides 18-25), `Unit No.3 Arrays_Strings.pdf`, `SPM Lab/EX4.docx`, `PIC Practice question_Array.docx` (Q18-Q31, Q50, Q60, Q67, Q72, Q85, Q89).*
