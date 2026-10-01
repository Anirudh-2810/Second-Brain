---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "Experiments 3, 4, 5 — Loops, Arrays, Strings"
date: "2026-10-02"
description: "SPM lab write-ups for EX3 (looping control structures), EX4 (arrays: 1D/2D, sum/average, linear search, max/min, matrix addition) and EX5 (strings: strlen/strcpy/strcat/strcmp, palindrome) — aims, sample programs, task lists, post-lab Q&A and viva answers."
tags: [spm, lab, experiments, arrays, strings, loops, 316U06C107, ex3, ex4, ex5, lab-ca]
last_updated: "2026-10-02"
confidence: high
sources:
  - "raw-sources/SPM Lab/EX3.pdf"
  - "raw-sources/SPM Lab/EX4.docx"
  - "raw-sources/SPM Lab/EX5.docx"
---

## For future agent

Lab write-ups for **Experiments 3, 4, 5** of 316U06C107, ingested 2026-10-02 from the original lab records in `raw-sources/SPM Lab/`. Theory for EX4/EX5 lives in [[module-3-arrays-strings]] — this page is the **experiment-shaped** cut (aims, numbered sample programs, task lists, post-lab questions) that mirrors how the lab manual and the CA rubric are organised.

Staleness caveats: (1) the EX3 docx extraction shows duplicated boilerplate (`873912329668# include <stdio .h>` etc.) — that is OCR/`docx`-XML noise from the scanner, not part of the lab content; the code blocks below are hand-cleaned and the *logic* is verbatim from the record, but the formatting is not byte-exact. (2) The lab records use unbounded `scanf("%s", ...)` — faithful to what is prescribed, unsafe in modern C. Flagged, not corrected.

EX1/EX2 write-ups are in the companion page [[spm-lab-exp1-exp2-guides]].

---

# SPM Lab — EXP3, EXP4, EXP5

Department of Science and Humanities · Course: Structured Programming Methodology (316U06C107)

---

# EXPERIMENT 3 — Looping Control Structures

## Aim

- To understand the concept of **iteration** in C programs.
- To study the three looping constructs: `for`, `while`, `do-while`.
- To learn `break` and `continue` for controlling loop execution.
- To write C programs using **nested loops** for computation and pattern generation.

## Theory — the three loops at a glance

Iteration is the third fundamental control structure of structured programming, alongside **sequence** and **selection**. It repeats a block of statements while a condition holds.

```c
for   (initialization; condition; update) { statement(s); }
while (condition)                         { statement(s); }
do     { statement(s); } while (condition);
```

| Aspect | `for` | `while` | `do-while` |
|---|---|---|---|
| Condition checked | before each iteration | before each iteration | **after** each iteration |
| Minimum executions | 0 | 0 | **1 (always runs once)** |
| Best used when | iteration count known | count unknown, condition-driven | body must run at least once |

**`do-while` is the natural choice for input validation and menus** — the prompt must be displayed at least once before the condition can be checked.

### Sample Program 1 — Sum of first N natural numbers (`for`)

```c
#include <stdio.h>

int main(void) {
    int n, i, sum = 0;

    printf("Enter N: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++) {
        sum += i;
    }

    printf("Sum = %d\n", sum);
    return 0;
}
```

### Sample Program 2 — Sum of digits (`while`)

```c
#include <stdio.h>

int main(void) {
    int num, digit, sum = 0;

    printf("Enter a number: ");
    scanf("%d", &num);

    while (num != 0) {
        digit = num % 10;    /* pull off the last digit */
        sum  += digit;
        num  /= 10;          /* chop off the last digit */
    }

    printf("Sum of digits = %d\n", sum);
    return 0;
}
```

**The `% 10` / `/= 10` pair is the standard number-dissection idiom**: `n % 10` gives the last digit, `n /= 10` removes it. Works for factorial, digit count, and digit reversal too.

### Sample Program 3 — Input validation (`do-while`)

```c
#include <stdio.h>

int main(void) {
    int num;

    do {
        printf("Enter a positive number: ");
        scanf("%d", &num);
        if (num <= 0)
            printf("Invalid input, try again.\n");
    } while (num <= 0);

    printf("You entered: %d\n", num);
    return 0;
}
```

The prompt appears **at least once** even if the user enters a valid number immediately — that is the defining property of `do-while`.

### Sample Program 4 — Nested loops: right-angled triangle

```c
#include <stdio.h>

int main(void) {
    int i, j, rows;

    printf("Enter number of rows: ");
    scanf("%d", &rows);

    for (i = 1; i <= rows; i++) {        /* outer = which row we're on */
        for (j = 1; j <= i; j++) {        /* inner = how many stars    */
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}
```

**A loop inside a loop: the inner loop completes all its iterations for every single iteration of the outer loop.** Input `4` gives:

```
* 
* * 
* * * 
* * * * 
```

The inner condition `j <= i` (not `j <= rows`) is what makes it a triangle — each row prints exactly as many stars as its row number.

### Sample Program 5 — `continue` and `break`

```c
#include <stdio.h>

int main(void) {
    int i;

    printf("1 to 10, skipping multiples of 3:\n");
    for (i = 1; i <= 10; i++) {
        if (i % 3 == 0)
            continue;               /* skip the rest of THIS iteration */
        printf("%d ", i);
    }

    printf("\nFirst number divisible by 7 (50-100): ");
    for (i = 50; i <= 100; i++) {
        if (i % 7 == 0) {
            printf("%d\n", i);
            break;                  /* leave the loop entirely */
        }
    }
    return 0;
}
```

**Output:** `1 2 4 5 7 8 10` then `56`.

| Keyword | Effect | Scope |
|---|---|---|
| `break` | exits the loop **immediately** | innermost enclosing loop |
| `continue` | skips the rest of the current iteration, moves to the next | innermost enclosing loop |

> **`continue` does NOT skip the loop's update step.** In a `for` loop, `i++` still runs — only the remaining *body* is skipped. This is a classic viva question.

### Points to remember

- `do-while` is the natural choice for input validation and menus (prompt must show at least once).
- **Forgetting the update step** (omitting `i++`) is the most common cause of an infinite loop.
- `continue` skips the remaining body, **not** the update expression.

## Laboratory Tasks — EX3

| # | Task | Focus |
|---|---|---|
| 1 | Print the first N natural numbers **and** their sum | `for` loop |
| 2 | Accept a number; determine with a `for` loop whether it is **prime** | `for` + trial division |
| 3 | `while` loop: generate first N **Fibonacci** terms; also (a) display the sum of all N terms, (b) count and display how many terms are **even** | `while` + accumulator + parity |

**Task 3 hint:** iterate with `while`, holding two variables (`a`, `b`) that shift each pass. To count even terms add `if (term % 2 == 0) evenCount++;` inside the loop.

### Additional practice — EX3

1. Reverse the digits of a number (`while`).
2. Factorial of a number (`for`).
3. Multiplication table 1–10 of a given number (`for`).
4. Count the number of digits in a number (`while`).
5. Print a right-angled star pattern for N rows (nested `for`).

## Post-Lab Questions — EX3

**Conceptual**

1. Difference between `for` and `while` in terms of where initialization, condition, and update are written.
2. Why does `do-while` always execute its body at least once?
3. What is an infinite loop? Give one example of C code that causes one unintentionally.

**Loop-specific**

4. Difference between `break` and `continue`.
5. Rewrite Sample Program 1's `for` loop as an equivalent `while` loop.
6. Why is nesting used in loops? Give one real-world pattern-printing problem that requires it.
7. What happens if the update statement (e.g. `i++`) is left out of a `for` loop?

**Tracing**

8. `for (i = 1; i <= 5; i++) { if (i == 3) continue; printf("%d ", i); }`
9. `int i = 1; while (i <= 3) { printf("%d ", i); i++; }`
10. Final value of `sum` after `int sum = 0; for (int i = 1; i <= 4; i++) sum += i;`

<details><summary>Answers 8–10</summary>

**8.** `1 2 4 5` — at `i == 3` the `continue` skips the `printf`, then `i++` still runs.
**9.** `1 2 3`
**10.** `10` (1+2+3+4)
</details>

**Answer to 3 (infinite loop):** `while (i > 0) { printf("%d", i); }` — the condition never becomes false because `i` never changes.

---

# EXPERIMENT 4 — Arrays

## Aim

- To understand an array as a collection of elements of the **same type**.
- To learn to declare, initialize, and traverse **1D and 2D** arrays.
- To perform common array operations: sum, average, searching, max/min.
- To perform basic operations on 2D arrays (matrices).

## Theory

```c
dataType arrayName[size];
```

An array holds elements of the same data type in **contiguous memory**, accessed with a single name and an index. Indices start at **0**, so an array of size *n* has valid indices `0 … n-1`.

### Sample Program 1 — Declare, initialize, display

```c
#include <stdio.h>

int main(void) {
    int arr[5] = {10, 20, 30, 40, 50};
    int i;

    printf("Array elements: ");
    for (i = 0; i < 5; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
```

### Sample Program 2 — Sum and average

```c
#include <stdio.h>

int main(void) {
    int arr[5], i, sum = 0;
    float avg;

    printf("Enter 5 elements: ");
    for (i = 0; i < 5; i++) {
        scanf("%d", &arr[i]);
        sum += arr[i];              /* accumulate inside the READ loop */
    }
    avg = (float) sum / 5;         /* the cast prevents integer division */

    printf("Sum = %d\n", sum);
    printf("Average = %.2f\n", avg);
    return 0;
}
```

**Two things to point out in a viva:**

- Summing inside the reading loop saves a second pass (O(n) either way, one traversal instead of two).
- **`(float)` cast is mandatory.** Without it `sum / 5` is *integer* division and the fractional part is discarded. `7 / 2` gives `3`, not `3.5`.

### Sample Program 3 — Linear search

```c
#include <stdio.h>

int main(void) {
    int arr[5] = {12, 45, 7, 23, 9};
    int key, i, found = 0;

    printf("Enter element to search: ");
    scanf("%d", &key);

    for (i = 0; i < 5; i++) {
        if (arr[i] == key) {
            printf("Found at index %d\n", i);
            found = 1;
            break;                  /* no point scanning further */
        }
    }

    if (!found)
        printf("Element not found\n");
    return 0;
}
```

**Why "linear"?** Because it checks elements **one after another from the beginning**, in a straight line — up to *n* comparisons worst case. It is called **linear** because the number of comparisons **grows linearly** with *n* (O(n)). (Contrast with binary search: O(log n) — see [[module-3-arrays]].)

The `found` flag exists because `break` jumps **out** of the loop, so a direct `else` on the `if` would never be reached.

### Sample Program 4 — Largest and smallest

```c
#include <stdio.h>

int main(void) {
    int arr[6] = {34, 12, 89, 5, 67, 23};
    int i, max = arr[0], min = arr[0];

    for (i = 1; i < 6; i++) {
        if (arr[i] > max) max = arr[i];
        if (arr[i] < min) min = arr[i];    /* BOTH ifs, not else-if */
    }

    printf("Largest = %d\n", max);
    printf("Smallest = %d\n", min);
    return 0;
}
```

**Both `if`s are separate, not `else if`.** An element could never be both the largest and smallest, but using `else if` would silently break when neither holds. Seed **both** from `arr[0]` — never from `0`, which fails on all-negative data.

### Sample Program 5 — Declare, initialize, display a 2D array

```c
#include <stdio.h>

int main(void) {
    int matrix[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int i, j;

    for (i = 0; i < 2; i++) {         /* outer = rows */
        for (j = 0; j < 3; j++) {     /* inner = columns */
            printf("%d ", matrix[i][j]);
        }
        printf("\n");                 /* after inner loop */
    }
    return 0;
}
```

A 2D array is stored in memory in **row-major order**: all of row 0, then all of row 1, and so on. Address of `[i][j]` = $B + (i \times C + j) \times S$. That is why outer=rows, inner=columns is the cache-friendly loop order in C. Full derivation: [[module-3-arrays-strings]] §3.5.

### Sample Program 6 — Addition of two matrices

```c
#include <stdio.h>

int main(void) {
    int a[2][2] = {{1, 2}, {3, 4}};
    int b[2][2] = {{5, 6}, {7, 8}};
    int c[2][2];
    int i, j;

    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            c[i][j] = a[i][j] + b[i][j];   /* same position, element-wise */
        }
    }

    printf("Sum Matrix:\n");
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            printf("%d ", c[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

### Points to remember

- An array's size must be a **compile-time constant** in basic C — it cannot be resized after declaring.
- Accessing an out-of-range index (e.g. `arr[10]` on a 10-element array) **does not cause a compile error** — it silently reads/writes unrelated memory. This is **undefined behaviour**.
- A 2D array `arr[i][j]` always needs two indices and typically a nested loop to traverse fully.

## Laboratory Tasks — EX4

| # | Task | Focus |
|---|---|---|
| 1 | Read N elements into an array; display them with their **sum and average** | input + accumulate + cast |
| 2 | Find **largest and smallest**; also display the **index** at which each was found | tracking position |
| 3 | Sort N elements **ascending using bubble sort**; display sorted; then accept a search key and do a **linear search** on the sorted array, showing position or "not found" | sorting + searching |

**Task 2 hint:** track indices alongside values — `if (arr[i] > max) { max = arr[i]; maxPos = i; }`.

**Task 3 hint — bubble sort skeleton:**

```c
for (pass = 0; pass < n - 1; pass++) {
    swapped = 0;
    for (i = 0; i < n - 1 - pass; i++) {      /* note: shrinks each pass */
        if (arr[i] > arr[i + 1]) {
            temp = arr[i]; arr[i] = arr[i + 1]; arr[i + 1] = temp;
            swapped = 1;
        }
    }
    if (!swapped) break;                       /* already sorted */
}
```

`n - 1 - pass` shrinks because after each pass the largest remaining element has bubbled to the end and needs no further checking. The `swapped` flag gives O(n) on already-sorted input.

### Additional practice — EX4

1. Count even and odd numbers in an array.
2. Reverse the elements of an array **in place** (no second array) — swap `arr[i]` with `arr[n-1-i]` for `i < n/2`.
3. Count duplicate elements.
4. Merge two arrays into a third, then sort the merged array.
5. Find and display the **transpose** of an M × N matrix.

## Post-Lab Questions — EX4

**Conceptual**

1. What is an array? How does it differ from declaring several individual variables?
2. Why do array indices in C start from 0 instead of 1?
3. What happens, in practice, if a program accesses an array element outside its declared bounds?

**Array operations**

4. Why is the technique in Sample Program 3 called linear search?
5. Write the general condition for checking whether index `i` is within the valid bounds of an array of size *n*.
6. How is a 2D array's data organized in memory (row-major), and why does this matter when choosing loop order?
7. Why must the size of a basic C array be known in advance, unlike in some higher-level languages?

**Tracing**

8. Trace the first pass of bubble sort on `{5, 2, 8, 1}`, showing contents after each swap.
9. `int arr[4] = {3, 6, 9, 12}; int sum = 0; for (int i = 0; i < 4; i++) if (arr[i] % 2 == 0) sum += arr[i];` — final value of `sum`?
10. For `int arr[10];`, explain why `arr[10]` is invalid even though 10 seems like the natural "next" index.

<details><summary>Answers 8–10</summary>

**8.** Start `[5 2 8 1]`:
- i=0: 5>2 → swap → `[2 5 8 1]`
- i=1: 5>8? no → `[2 5 8 1]`
- i=2: 8>1 → swap → `[2 5 1 8]`

After pass 1: **`[2 5 1 8]`** (8 has bubbled to its final place).

**9.** Even elements are 6 and 12 → `sum = 18`.

**10.** Valid indices are `0 … 9`. `arr[10]` is one past the end — reading it touches memory that is not part of the array (writing it corrupts whatever lives there). It compiles without complaint because C performs no bounds checking; the result is **undefined behaviour**.
</details>

**Answers to 1–7:** see [[module-3-arrays-strings]] §1–3 (definition, zero-based indexing, undefined behaviour, O(n) vs O(log n), bounds condition `0 <= i < n`, row-major and cache, compile-time size).

---

# EXPERIMENT 5 — Strings and String Handling Functions

## Aim

- To understand how strings are represented internally in C.
- To learn how to declare, initialize, read, and display strings.
- To study the standard string handling functions: **`strlen()`, `strcpy()`, `strcat()`, `strcmp()`**.
- To write C programs that solve custom string problems using loops and array indexing.

## Theory

A string in C is an array of characters terminated by the special null character **`'\0'`**, which marks where the string ends. **This null terminator is why a string declared to hold 5 visible characters actually needs 6 bytes of storage.**

```c
char name[20];            /* 20 bytes = 19 chars + '\0' */
char greeting[] = "Hi";   /* stored as 'H', 'i', '\0' — size 3 */
```

### Sample Program 1 — Declaring, initializing, displaying

```c
#include <stdio.h>

int main(void) {
    char name1[20] = "Somaiya";
    char name2[]  = "Engineering";
    char name3[20];

    printf("name1 = %s\n", name1);
    printf("name2 = %s\n", name2);

    printf("Enter name3: ");
    scanf("%s", name3);              /* no & — the array name IS the address */
    printf("name3 = %s\n", name3);
    return 0;
}
```

### Sample Program 2 — Reading a full line: `fgets` vs `scanf("%s")`

`scanf("%s", str)` **stops at the first whitespace** — it cannot read a sentence containing spaces. `fgets()` reads an entire line, including spaces, up to a newline or the given size limit.

```c
#include <stdio.h>

int main(void) {
    char sentence[50];

    printf("Enter a sentence: ");
    fgets(sentence, sizeof(sentence), stdin);

    printf("You entered: %s", sentence);
    return 0;
}
```

### Sample Program 3 — `strlen()`

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char str[20] = "Hello";
    printf("Length = %d\n", strlen(str));
    return 0;
}
```

**Output:** `Length = 5`.

### Sample Program 4 — `strcpy()` and `strcat()`

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char first[20]  = "Structured";
    char second[20] = "Programming";
    char result[50];

    strcpy(result, first);      /* result = "Structured"    */
    strcat(result, second);     /* result = "StructuredProgramming" */
    printf("Result = %s\n", result);
    return 0;
}
```

**Note the buffer sizing:** `result[50]` holds both `first` (10) and `second` (11) plus the terminator = 22 bytes. A 20-byte buffer would also fit, but 50 makes the intent obvious. **The destination must be large enough for the final result including its `'\0'`.**

### Sample Program 5 — `strcmp()`

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char s1[20] = "apple";
    char s2[20] = "apple";

    if (strcmp(s1, s2) == 0)
        printf("Strings are equal\n");
    else
        printf("Strings are not equal\n");
    return 0;
}
```

`strcmp` returns **0** when the two strings are exactly equal; **any non-zero result** means they differ. It returns a *negative* value if the first string is lexicographically smaller and a *positive* value if larger. ("Lexicographically" = the way words are ordered in a dictionary.)

### Sample Program 6 — Palindrome check (custom logic)

Not every string problem has a ready-made library function — this combines `strlen()` with array indexing and a loop:

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char str[20];
    int i, len, isPalindrome = 1;

    printf("Enter a string: ");
    scanf("%s", str);

    len = strlen(str);
    for (i = 0; i < len / 2; i++) {
        if (str[i] != str[len - 1 - i]) {
            isPalindrome = 0;
            break;
        }
    }

    if (isPalindrome)
        printf("%s is a palindrome\n", str);
    else
        printf("%s is not a palindrome\n", str);
    return 0;
}
```

### Points to remember

- `strlen()` counts **only the visible characters** — it does **not** include the null terminator in its result. That is why `strlen("Hello") == 5` while the array occupies 6 bytes.
- The destination array passed to `strcpy()` or `strcat()` **must be large enough** to hold the final result including its null terminator, or the program's behavior becomes **unpredictable**.
- `strcmp()` returns **0 only** when the two strings are exactly equal — any non-zero result means they differ.
- `#include <string.h>` is **mandatory** for `strlen/strcpy/strcat/strcmp`.

## Laboratory Tasks — EX5

| # | Task | Focus |
|---|---|---|
| 1 | **String Length and Reversal** — accept a string, display its length using `strlen()`, then print it in reverse using a loop (**no** built-in reverse function) | `strlen` + reverse loop |
| 2 | **Concatenation and Comparison** — accept two strings, use `strcpy()` and `strcat()` to combine them into a third array, then use `strcmp()` to report whether the two **original** strings were equal | all four functions |
| 3 | **Palindrome and Vowel/Consonant Count** — accept a string and (a) check whether it is a palindrome (**ignoring case**), (b) count and display vowels and consonants | indexing + char comparison |

**Task 3 hint (ignore case):** convert with `tolower()` from `<ctype.h>`, or compare both cases:
`if (str[i] == 'a' || str[i] == 'A' || str[i] == 'e' || str[i] == 'E' || ...)`.

### Additional practice — EX5

1. Count the number of **words** in a sentence (read the full line with `fgets`).
2. Count how many times a **specific character** appears in a string.
3. Convert a string **lowercase → uppercase without** any built-in case-conversion function (subtract 32 from each `a`–`z`).
4. Check whether two strings are **anagrams** (same characters, different order) — sort copies and compare, or count character frequencies.
5. **Remove all spaces** from a string and display the result.

## Post-Lab Questions — EX5

**Conceptual**

1. What is the difference between a C string and a plain character array?
2. Why does `strlen("Hello")` return 5 when the array storing it occupies 6 bytes?
3. Why is it risky to use `scanf("%s", ...)` to read a string that may contain spaces?

**String functions**

4. What is the difference between `strcpy()` and `strncpy()`?
5. What could go wrong if the destination array passed to `strcat()` is not large enough to hold the combined result?
6. What does `strcmp(s1, s2)` return when `s1` and `s2` are exactly equal? What does a non-zero result indicate?
7. Which header file must be included to use `strlen()`, `strcpy()`, `strcat()`, `strcmp()`?

**Tracing**

8. `char s[] = "Hello"; printf("%d", strlen(s));`
9. Trace, step by step, the index comparisons made by Sample Program 6 while checking whether `"level"` is a palindrome.
10. `char a[20] = "Data"; char b[] = "Structures"; strcat(a, b);` — what is the resulting content of `a`, and why must `a` be declared with extra space beyond just `"Data"`?

<details><summary>Answers 8–10</summary>

**8.** `5`

**9.** `len = 5`. Loop runs for `i = 0, 1` only (`i < 5/2 = 2`):
- `i=0`: `str[0]='l'` vs `str[4]='l'` → match
- `i=1`: `str[1]='e'` vs `str[3]='e'` → match
- `i=2`: loop condition `2 < 2` is false → stop
- `isPalindrome` still 1 → **"level is a palindrome"**

**10.** `a` becomes **`"DataStructures"`** (14 characters + `'\0'` = 15 bytes, which fits in 20). `a` needs the extra space because `strcat` **appends** `b` to whatever `a` already holds; a buffer sized only for `"Data"` (5 bytes) would be overflowed with 15 bytes of content.
</details>

**Answers to 1–7:**

1. A **C string** is a char array that must be `'\0'`-terminated; a plain char array may contain anything (e.g. a name buffer). `char n[20]` is both; the *difference is whether the `'\0'` is meaningful*.
2. `strlen` counts characters **before** the terminator. `"Hello"` is 5 characters; the 6th byte is the `'\0'` itself, which is not counted.
3. `%s` **stops reading at the first whitespace**, so it silently truncates `Piyush Sharma` to `Piyush` — data loss, not a crash. It is also unbounded: input longer than the buffer overflows it. Use `fgets(s, sizeof s, stdin)`.
4. `strcpy` copies everything and always adds `'\0'`, but is **unbounded**. `strncpy` copies at most `n` characters and may **omit** the `'\0'` if the source is at least `n` long — you must add `dst[n-1] = '\0'` yourself.
5. **Undefined behaviour / buffer overflow.** `strcat` writes past the end of `dst`, corrupting adjacent memory — possibly the stack, which can crash the program or be exploited.
6. Exactly equal → **`0`**. A non-zero result means they differ (negative = first sorts before second, positive = after).
7. **`<string.h>`**

## Learning Outcome — EX5

After completing this experiment you can:

- Understand how strings are represented internally in C.
- Read and display strings safely, including those containing spaces.
- Use the standard string handling functions: `strlen()`, `strcpy()`, `strcat()`, `strcmp()`.
- Apply loops and array indexing to solve custom string problems such as palindrome checking.

---

## Summary — all three experiments

| # | Title | Core concept | Key functions |
|---|---|---|---|
| EX3 | Looping Control Structures | iteration, `break`/`continue`, nesting | `for` `while` `do-while` |
| EX4 | Arrays | contiguous storage, index 0-based, row-major | `scanf`/`printf`, sorting, searching |
| EX5 | Strings and String Handling Functions | `char[]` + `'\0'`, library + from-scratch | `strlen` `strcpy` `strcat` `strcmp` `fgets` |

## Cross-References

- Theory: [[module-3-arrays-strings]] (merged arrays + strings, beginner) · [[module-3-arrays]] · [[module-3-strings]] · [[spm-string-functions-char-equality-reverse]]
- Earlier labs: [[spm-lab-exp1-exp2-guides]] · [[spm-lab-exp-guides]]
- Loops: [[module-2-program-control-functions]] · [[spm-module2-faculty-companion]]
- Marking: [[lab-ca-and-experiments]] (CA rubric: logic / debug / write-up / timely) · [[assessment-guide-ese-ost-quiz]]
- Cram: [[c-programming-master-study-guide]] · [[formula-sheet-spm]]

*Ingested 2026-10-02 from `raw-sources/SPM Lab/EX3.pdf`, `EX4.docx`, `EX5.docx`.*