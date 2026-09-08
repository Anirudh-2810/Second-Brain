---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "PIC Practice Question Bank — Conditionals, Loops, Arrays (M2-M3)"
tags: [spm, btech, c, pic, question-bank, conditionals, loops, arrays, ost, ese]
last_updated: "2026-09-09"
description: "SPM PIC practice question bank distilled from raw-sources filenames plus full text of 3 practice sets — 26 conditional, 59 loop, 107 array problems with solved C examples and OST/ESE mapping."
---

## For future agent

This note is the PIC (Programming in C) practice-question registry for SPM 316U06C107. It catalogs all 28 SPM theory source files by filename (big PDFs/PPTX never opened) and distills the full text of the three small practice sets: conditional (26 Q), loop (59 Q), array (107 Q). Use it to answer "give me practice/drill problems" or to build OST/ESE mocks. Theory lives in [[module-2-program-control-functions]] and [[module-3-arrays]]; exam pattern in [[assessment-guide-ese-ost-quiz]]; lab mapping in [[lab-ca-and-experiments]].

# SPM PIC Question Bank — Conditionals, Loops, Arrays

> Sources (raw-sources, cataloged by filename — only the 3 small `.docx` practice sets were text-extracted; PPTX/big PDFs listed, not opened):
> `SPM/PIC_Question_Conditional.docx` (26 Q) · `SPM/PIC Question _ LOOP.docx` (59 Q) · `SPM/PIC Practice question_Array.docx` (107 Q) ·
> `SPM/Syllabus_SPM.pdf` · `SPM/Let Us C.pdf` · Module 1 (8 files: 1.1 Problem Solving, 1.2 Structured Programming, 1.3 Execution+SDLC, 1.4 Headers/Operators, 1.5 Operators+Expressions, Data Types, 1.1 PPT, Ternary) ·
> Module 2 (7 files: 2.1 if, 2.2 switch, 2.3 loops, 2.4 while/do-while, 2.5 for, 2.6 flags, 2.7 documentation) ·
> Module 3 (2 files: 3.1&3.2 Arrays+Strings, examples&theory) ·
> Module 4 (6 files: 4.2 Struct/Union PPT, 4.3 Pointers PPT, Let-Us-C Functions&Pointers, 4.1 UDF PPT+PDF, Let-Us-C Structures)
> Syllabus hub: [[syllabus-316U06C107]] | Strings: [[module-3-strings]]

## 1. Conditional Practice — 26 Q (M2.1, CO2)

Groups: **basics** Q1-7 (equal, even/odd, pos/neg, leap year, vote age, sign-of-m, height band) · **branching logic** Q8-12 (largest-of-3, quadrant, admission criteria, quadratic roots, roll/marks/division) · **classification** Q13-18 (temperature bands, triangle type, angle-validity, char class, vowel/consonant, profit/loss) · **bill + menu/switch** Q19-26 (electricity bill with slab+surchage, grade description, day name, digit word, month name, month days, area menu, calculator menu).

Solved reference — leap year (Q4):

```c
#include <stdio.h>
int main(void) {
    int y = 2016;
    if ((y % 400 == 0) || (y % 4 == 0 && y % 100 != 0))
        printf("%d is a leap year.", y);
    else
        printf("%d is not a leap year.", y);
    return 0;
}
```

Solved reference — largest of three (Q8):

```c
#include <stdio.h>
int main(void) {
    int a = 12, b = 25, c = 52;
    int big = (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);
    printf("greatest = %d", big);
    return 0;
}
```

Solved reference — day-number switch (Q21, also covers Q23/Q24 pattern):

```c
#include <stdio.h>
int main(void) {
    int d = 4;
    switch (d) {
        case 1: printf("Monday"); break;
        case 2: printf("Tuesday"); break;
        case 3: printf("Wednesday"); break;
        case 4: printf("Thursday"); break;
        case 5: printf("Friday"); break;
        case 6: printf("Saturday"); break;
        case 7: printf("Sunday"); break;
        default: printf("invalid");
    }
    return 0;
}
```

Electricity-bill slab (Q19 — memorize, classic ESE/OST bill problem): units up to 199 @1.20, 200-399 @1.50, 400-599 @1.80, 600+ @2.00; surcharge 15% if bill > 400; minimum bill Rs 100. Test: 800 units → 800×2.00=1600 + 240 surcharge = 1840.

## 2. Loop Practice — 59 Q (M2.2, CO2)

Groups: **series/sum** Q1-8, 16, 18-19, 21, 23-26, 49, 52 (naturals, odd/even, squares, cubes, harmonic, 9+99+…, 1+11+…, AP/GP, x-series) · **patterns** Q9-14, 17, 20, 22, 31, 33, 36, 40 (asterisk/number triangles, pyramids, diamond, Floyd, Pascal, alphabet pyramid, 121 rows) · **number theory** Q27-30, 32, 34-35, 37-39, 43-48, 56, 59 (perfect, Armstrong incl. n-digit, prime/range, Fibonacci, reverse, palindrome, div-by-9 sum, HCF/LCM, strong numbers, sum-of-two-primes) · **conversions** Q41-42, 46, 50-55 (dec↔bin/oct/hex, bin→oct, oct→bin) · **strings-with-loops** Q57-58 (reverse string, strlen without library — bridges to [[module-3-strings]]).

Solved reference — factorial (Q15):

```c
#include <stdio.h>
int main(void) {
    int n = 5, f = 1;
    for (int i = 1; i <= n; i++) f *= i;
    printf("factorial = %d", f);
    return 0;
}
```

Solved reference — palindrome (Q38):

```c
#include <stdio.h>
int main(void) {
    int n = 121, rev = 0, t = n;
    while (t > 0) { rev = rev * 10 + t % 10; t /= 10; }
    printf(t == 0 && rev == n ? "palindrome" : "not palindrome");
    return 0;
}
```

Solved reference — prime test (Q32):

```c
#include <stdio.h>
int main(void) {
    int n = 13, prime = n > 1;
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0) { prime = 0; break; }
    printf(prime ? "prime" : "not prime");
    return 0;
}
```

Solved reference — Fibonacci (Q35):

```c
#include <stdio.h>
int main(void) {
    int n = 10, a = 0, b = 1;
    for (int i = 0; i < n; i++) { printf("%d ", a); int t = a + b; a = b; b = t; }
    return 0;
}
```

## 3. Array Practice — 107 Q (M3.1, CO3)

Groups: **1D basics** Q1-17 (store/print, reverse, sum, copy, duplicates, unique, merge, frequency, min/max, odd-even split, asc/desc sort, insert sorted+unsorted, delete, 2nd largest/smallest) · **2D core** Q18-31 (3×3 print, add, subtract, multiply, transpose, diagonals, row/col sums, triangular, 3×3 determinant, sparse, equality, identity) · **advanced/DSA-flavored** Q32-107 (pair-sum, majority, odd-occurrences, Kadane max-subarray, missing number, pivot/rotated-min, merge-sorted, rotate-by-N, ceil/floor, next-greater, repeating elements, zero-sum pair, subarray-sum, spiral, circular-max, triangle-count, 0/1/2 sort, subset, min-jumps, zeroes-to-end, counting sort, max-1s-row, max-product, 0/1 balance, product-except-self, inversions, sorted-matrix search, non-adjacent max, max-difference, medians, unique rows, triangular sums, permutations, 4-sum, paths, equilibrium, bitonic max — extension bank beyond ESE, good for quiz predict-output and interviews).

Solved reference — second largest (Q16, favorite OST pick):

```c
#include <stdio.h>
int main(void) {
    int a[] = {2, 9, 1, 4, 6}, n = 5;
    int first = a[0], second = a[0];
    for (int i = 1; i < n; i++) {
        if (a[i] > first) { second = first; first = a[i]; }
        else if (a[i] > second && a[i] != first) second = a[i];
    }
    printf("second largest = %d", second);
    return 0;
}
```

Solved reference — matrix multiply (Q21):

```c
#include <stdio.h>
int main(void) {
    int A[2][2] = {{1,2},{3,4}}, B[2][2] = {{5,6},{7,8}}, C[2][2] = {0};
    for (int i = 0; i < 2; i++)
        for (int j = 0; j < 2; j++)
            for (int k = 0; k < 2; k++) C[i][j] += A[i][k] * B[k][j];
    printf("%d %d\n%d %d", C[0][0], C[0][1], C[1][0], C[1][1]); // 19 22 / 43 50
    return 0;
}
```

## 4. Exam Mapping

- **OST (M1-3, 45 min + algorithm):** highest-yield picks — conditional Q4/Q8/Q19, loop Q15/Q32/Q35/Q38, array Q16/Q19-Q22. Write pseudocode first (5 marks) per [[lab-ca-and-experiments#4-ost--15-marks-ost-modules-13]].
- **ESE Q1/Q2 (programs):** electricity bill, triangle validity, Armstrong-range, matrix multiply/transpose, strlen-from-scratch; **Q3 (complete-the-code):** switch fall-through, loop bounds, `'\0'`; **Q4a (algorithm):** flowchart of any Q above; see [[assessment-guide-ese-ost-quiz#1-ese-50-marks--on-screen-pattern]].
- **Quiz (debug/complete/predict):** `=` vs `==`, missing `break`, off-by-one `<=` vs `<`, `scanf` missing `&`, non-terminated `%s` — drill kit in [[formula-sheet-spm]].

*Related:* [[syllabus-316U06C107]] · [[lesson-plan-2026-27]] · [[c-programming-master-study-guide]]
