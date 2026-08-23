---
module: "c-programming"
topic: "Solved Practice — 2D Arrays & Matrices (5 problems)"
tags: [programming, c, practice, solved, arrays, matrix, exam]
last_updated: "2026-08-19"
---

# 04 · 2D Arrays (Matrices) — 5 Solved Problems

> Grid logic is a guaranteed exam question. Learn the **row × column** loop pattern and the three classic ops: sum, transpose, multiply.

---

## Problem 4.1 — Print a 3×3 matrix from a 2D array

```c
#include <stdio.h>
int main() {
    int m[2][3] = { {1, 2, 3}, {4, 5, 6} };
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++)
            printf("%d ", m[i][j]);
        printf("\n");
    }
    return 0;
}
```

**<details><summary>Solution</summary>**

Output:
```
1 2 3
4 5 6
```

| Memory (row-major) | offset | value |
|---|---|---|
| `m[0][0] m[0][1] m[0][2]` | 0 1 2 | 1 2 3 |
| `m[1][0] m[1][1] m[1][2]` | 3 4 5 | 4 5 6 |

**Pattern:** outer loop = **rows**, inner loop = **columns**. Newline after each inner loop.

</details>

---

## Problem 4.2 — Sum of each row (write the program)

Write a program to read a 3×3 matrix and print the **sum of every row**.

**<details><summary>Solution</summary>**

```c
#include <stdio.h>
int main() {
    int m[3][3];
    printf("Enter 9 numbers:\n");
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            scanf("%d", &m[i][j]);

    for (int i = 0; i < 3; i++) {
        int rowSum = 0;
        for (int j = 0; j < 3; j++)
            rowSum += m[i][j];        // sum one row
        printf("Row %d sum = %d\n", i + 1, rowSum);
    }
    return 0;
}
```

Input: `1 2 3 / 4 5 6 / 7 8 9` →
```
Row 1 sum = 6
Row 2 sum = 15
Row 3 sum = 24
```

**Key idea:** reset `rowSum = 0` **inside** the row loop (once per row). To sum each *column* instead, swap the loops: inner stays on row, outer advances column.

</details>

---

## Problem 4.3 — Matrix transpose (write the program)

Write a program to compute and print the **transpose** of a 3×3 matrix (swap rows ↔ columns).

**<details><summary>Solution</summary>**

```c
#include <stdio.h>
int main() {
    int m[3][3] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
    int t[3][3];
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            t[j][i] = m[i][j];        // swap index order!

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++)
            printf("%d ", t[i][j]);
        printf("\n");
    }
    return 0;
}
```

Output:
```
1 4 7
2 5 8
3 6 9
```

**Key idea:** `t[j][i] = m[i][j]` — you read rows, you write into columns. That's the whole trick.

**In-place (square matrix):** only swap `j > i` (the triangle above the diagonal) — swapping everything twice undoes itself.

</details>

---

## Problem 4.4 — Matrix multiplication (write the program)

Multiply two matrices `A[2][3] × B[3][2]` → `C[2][2]`.

**<details><summary>Solution</summary>**

```c
#include <stdio.h>
int main() {
    int A[2][3] = { {1, 2, 3}, {4, 5, 6} };
    int B[3][2] = { {7, 8}, {9, 10}, {11, 12} };
    int C[2][2] = {0};

    // A is 2x3, B is 3x2 → C is 2x2
    for (int i = 0; i < 2; i++)              // rows of C = rows of A
        for (int j = 0; j < 2; j++)          // cols of C = cols of B
            for (int k = 0; k < 3; k++)      // shared inner dimension
                C[i][j] += A[i][k] * B[k][j];

    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++)
            printf("%d ", C[i][j]);
        printf("\n");
    }
    return 0;
}
```

Output:
```
58 64
139 154
```

**Trace C[0][0] = 1·7 + 2·9 + 3·11 = 7 + 18 + 33 = 58**

| Rule to memorize | Example |
|---|---|
| A is `m×n`, B is `n×p` | must share the middle `n` |
| Result C is `m×p` | 2×3 · 3×2 → 2×2 |
| Triple loop: `i` (rows of A), `j` (cols of B), `k` (inner) | `C[i][j] += A[i][k] * B[k][j]` |

</details>

---

## Problem 4.5 — Diagonal sum & output prediction

```c
#include <stdio.h>
int main() {
    int m[3][3] = { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} };
    int d = 0, anti = 0;
    for (int i = 0; i < 3; i++) {
        d    += m[i][i];        // main diagonal
        anti += m[i][2 - i];    // anti diagonal
    }
    printf("%d %d\n", d, anti);
    return 0;
}
```

**<details><summary>Solution</summary>**

Output: `15 15`

| Diagonal | Elements | Sum |
|---|---|---|
| main (`m[i][i]`) | 1 + 5 + 9 | 15 |
| anti (`m[i][2-i]`) | 3 + 5 + 7 | 15 |

**Pattern:** main diagonal uses the **same index** for row and column; anti-diagonal uses `m[i][n-1-i]`. The middle element (5) belongs to both.

</details>

---

**Next:** [[c-programming/practice/05-sorting|05 · Sorting]] · **Index:** [[c-programming/practice/README|Problem bank]]