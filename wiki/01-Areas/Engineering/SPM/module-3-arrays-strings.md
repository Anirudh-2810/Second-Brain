---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "Module 3 — Introduction to Arrays (3.1) & Character Arrays/Strings (3.2)"
date: "2026-10-01"
description: "SPM Module 3 merged beginner page — 1D/2D arrays, address formulas, row-major layout, string model with '\\0', strlen/strcpy/strcmp/strcat, from-scratch implementations, and a dedicated strcpy exam drill with predict-output traps."
tags: [spm, arrays, strings, c-programming, 316U06C107, strcpy, exam-prep, 1d-arrays, 2d-arrays, row-major, string-handling, from-scratch, lab]
last_updated: "2026-10-01"
confidence: high
prerequisites: ["Module 2: Program Control Functions", "Pointers basics"]
sources:
  - "raw-sources/SPM Lecture/Unit No.3 Arrays_Strings.pdf"
  - "raw-sources/SPM Lab/EX4.docx"
  - "raw-sources/SPM Lab/EX5.docx"
  - "raw-sources/SPM_Syllabus_316U06C107.md"
---

## For future agent

Merged, beginner-first teaching page for SPM Module 3 (both halves: arrays **and** strings). Built by ingesting the faculty handout `Unit No.3 Arrays_Strings.pdf` (34 pp) plus lab records EX4 (Arrays) and EX5 (Strings) from `raw-sources/`. This is the **concept + teaching home** — `module-3-arrays.md` and `module-3-strings.md` remain the deeper exam/OST drill banks and are cross-linked, not replaced.

Staleness caveats: (1) the faculty handout is beginner-slanted and omits address arithmetic, binary search, bubble sort, and `strncpy` — those come from the wiki drill pages, not the source; (2) the handout teaches `scanf("%s", name)` without a width limit and `strcpy`/`strcat` without bounds checks. Those are **what the faculty teaches**, faithfully recorded, but they are unsafe modern C — sections 4.6 and 6.3 flag this explicitly so an agent never mistakes the handout for best practice. Do not "correct" the source blocks in sections 4–5; annotate instead.

---

# SPM Module 3 — Arrays & Strings (Beginner Complete)

> **Syllabus position** ([[syllabus-316U06C107]]): Module 3, **7 hours**, CO3.
> - **3.1** Arrays: 1D, multidimensional, declaration/initialization, reading/displaying
> - **3.2** Character arrays and strings: declaring/init, reading/writing chars & strings, operations, **implementing string handling from scratch**
>
> Self-learning (Module 4 area): file handling.

---

## 0. The One-Page Mental Model

Read this section and you have the shape of the whole module.

```
ARRAYS
   |
   +-- 1-D Array  (a list)         -> declaration, init, read, display, sum, largest
   |                                  address = B + i*S
   |
   +-- 2-D Array  (a table/matrix)  -> nested loops, row-major order
   |                                  address = B + (i*C + j)*S
   |
   +-- CHARACTER ARRAYS
          |
          v
       STRINGS   (char array + '\0')
          |
          +-- Read (scanf %c / %s / fgets)
          +-- Write (printf %s / puts)
          +-- Length (strlen)
          +-- Copy (strcpy)      <-- dedicated exam drill, section 7
          +-- Compare (strcmp)
          +-- Concatenate (strcat)
          +-- Reverse (loop)
          |
          v
       "FROM SCRATCH"  = do the same things one character at a time with a loop
```

**The four sentences to remember forever:**

1. C has **no** string type. A string is a `char` array ending in `'\0'`.
2. Array indexing **starts at 0**. Last valid index = size − 1.
3. `strlen` counts characters **without** `'\0'`; `sizeof` counts **with** it.
4. Arrays are **contiguous** → O(1) access. That is the reason for the address formulas.

---

# PART 1 — ARRAYS

## 1. Why Arrays Exist (the problem they solve)

Suppose you want to store marks of 5 students.

**Without an array** — five separate variables, no loop possible:

```c
int marks1 = 75;
int marks2 = 82;
int marks3 = 68;
int marks4 = 90;
int marks5 = 76;
```

This does not scale. You cannot say "do this to all five" — the compiler sees five unrelated names.

**With an array** — one name, and now a loop works:

```c
int marks[5];   /* stores 5 integers */
```

| Situation | Array |
|---|---|
| Marks of 50 students | `int marks[50];` |
| Temperature of 7 days | `float temp[7];` |
| Ages of 30 people | `int age[30];` |
| A person's name | `char name[20];` |

**Definition (say this in the exam):** an array is a *collection of elements of the same data type, stored in contiguous memory locations, accessed using a single variable name and an index*.

## 2. 1D Arrays — Declaration, Indexing, Initialization

### 2.1 Syntax

```c
data_type array_name[size];
```

Read `int numbers[5];` as three pieces: `int` = data type, `numbers` = array name, `5` = number of elements.

### 2.2 Indexing — the 0 trap

```
   INDEX:       0     1     2     3     4
                |     |     |     |     |
              [75]  [82]  [68]  [90]  [76]
```

There are **5** elements but the last index is **4**.

$$\text{Last index} = \text{Size} - 1$$

| Element | Written as |
|---|---|
| First | `marks[0]` |
| Second | `marks[1]` |
| Third | `marks[2]` |
| Fourth | `marks[3]` |
| Fifth | `marks[4]` |

### 2.3 Initialization — three methods

```c
/* Method 1: size AND values given */
int numbers[5] = {10, 20, 30, 40, 50};

/* Method 2: let C count the size */
int numbers[] = {10, 20, 30, 40, 50};      /* size becomes 5 */

/* Method 3: partial — remaining elements become ZERO */
int numbers[5] = {10, 20};                 /* -> {10, 20, 0, 0, 0} */
```

Method 3 is a **C guarantee**, not a convention. `numbers[2] == 0`, `numbers[4] == 0`. For a `char` array the zero-filling gives you free `'\0'` terminators.

### 2.4 Reading and Displaying

```c
#include <stdio.h>

int main(void)
{
    int numbers[5];
    int i;

    printf("Enter 5 numbers:\n");
    for (i = 0; i < 5; i++) {
        scanf("%d", &numbers[i]);      /* note the & — we need the ADDRESS */
    }

    printf("The array elements are:\n");
    for (i = 0; i < 5; i++) {
        printf("%d ", numbers[i]);
    }
    printf("\n");
    return 0;
}
```

**Why `&numbers[i]`?** `scanf` must **write** into the memory slot, so it needs the address. Contrast with `printf("%d", numbers[i])` which only *reads* the value — no `&` needed.

**Two loops, always.** The first loop fills, the second displays. Merging them does not work: you would display an element before the user had entered it.

### 2.5 Program: Sum of Array Elements

```c
#include <stdio.h>

int main(void)
{
    int numbers[5];
    int i, sum = 0;

    printf("Enter 5 numbers:\n");
    for (i = 0; i < 5; i++) {
        scanf("%d", &numbers[i]);
    }
    for (i = 0; i < 5; i++) {
        sum = sum + numbers[i];     /* sum += numbers[i]; is the short form */
    }
    printf("Sum = %d", sum);
    return 0;
}
```

Trace for input `10 20 30 40 50`:

| Step | `sum` before | add | `sum` after |
|---|---|---|---|
| 1 | 0 | 10 | 10 |
| 2 | 10 | 20 | 30 |
| 3 | 30 | 30 | 60 |
| 4 | 60 | 40 | 100 |
| 5 | 100 | 50 | **150** |

`sum` must be declared **before** the loop and initialized to `0`. Declaring it inside the loop would reset it every iteration — a classic mistake.

### 2.6 Program: Find the Largest Element

```c
int largest = numbers[0];           /* seed with the FIRST element, not 0 */

for (i = 1; i < 5; i++) {
    if (numbers[i] > largest) {
        largest = numbers[i];
    }
}
```

**The seed matters.** If you wrote `largest = 0`, the answer would be wrong whenever every element is negative. Seeding with `numbers[0]` is always correct. And the loop starts at **i = 1** — element 0 was already used as the seed, so re-testing it wastes a comparison.

Trace for `10 25 15 40 30`:

| Compared | Is it larger? | `largest` |
|---|---|---|
| seed | — | 10 |
| 25 | 25 > 10 → yes | 25 |
| 15 | 15 > 25 → no | 25 |
| 40 | 40 > 25 → yes | 40 |
| 30 | 30 > 40 → no | **40** |

### 2.7 Memory Map & the Address Formula

An array's slots sit **back to back** in memory. Say the base address is 1000 and `sizeof(int) = 4`:

```
   INDEX:     [0]    [1]    [2]    [3]    [4]
   ADDRESS:   1000   1004   1008   1012   1016
   VALUE:      10     20     30     40     50
   |<----------------- contiguous: 5 x 4 = 20 bytes -------------->|
```

$$\boxed{\text{Address}(A[i]) = B + i \times S}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $B$ | base address (address of element 0) | bytes |
| $i$ | index | — |
| $S$ | size of one element, `sizeof(type)` | bytes |

**Why it works:** to reach element $i$ you walk past $i$ elements, each $S$ bytes wide. That is $i \times S$ bytes beyond the base. **This is why array access is O(1)** — the CPU does one multiply-add, it never searches.

**Worked drill.** `float a[20]`, base 1024, `sizeof(float) = 4` → address of `a[12]`:

$$1024 + 12 \times 4 = 1024 + 48 = \boxed{1072}$$

### 2.8 `sizeof` — two meanings

```c
int a[5] = {10, 20, 30, 40, 50};
printf("%zu", sizeof(a));                 /* 20  — total bytes (5 x 4) */
printf("%zu", sizeof(a) / sizeof(a[0]));  /* 5   — element COUNT */
printf("%zu", sizeof(a[0]));              /* 4   — size of ONE element */
```

`sizeof(a) / sizeof(a[0])` is the idiom for element count. Use it instead of hard-coding 5.

**CRITICAL CAVEAT:** this only works inside the function that **declared** the array. Once an array is passed to a function it decays to a pointer, and `sizeof` there returns the pointer size (4 or 8 bytes), not the array size. See section 8.4.

### 2.9 Four rules that bite

| Rule | Statement | Consequence if broken |
|---|---|---|
| Zero-based | Valid indices are `0 … size-1` | Off-by-one logic errors |
| No bounds check | C never verifies `i < size` | **Undefined behaviour** — reads/writes unrelated memory |
| Compile-time size | Size must be a constant in basic C | Cannot resize an array after declaring it |
| Contiguous | Slots are adjacent | (Benefit, not a bug) → O(1) + address formula |

> **"Undefined behaviour" is the exam phrase.** Accessing `arr[10]` in a 10-element array is **not** a compile error and **not** a runtime error message — the program silently reads or writes some unrelated memory. This is the root cause of buffer-overflow vulnerabilities. See `module-3-arrays.md` §2.3 for the Heartbleed connection.

---

## 3. 2D Arrays (Multidimensional / Matrices)

### 3.1 The concept

A 2D array stores data in **rows and columns** — think of a table or a spreadsheet.

```
              Column
             0     1     2
          +-----+-----+-----+
  Row 0   | 10  | 20  | 30  |
  Row 1   | 40  | 50  | 60  |
  Row 2   | 70  | 80  | 90  |
          +-----+-----+-----+
```

That is a **3 × 3 matrix** — 9 elements total.

### 3.2 Declaration and initialization

```c
int matrix[3][3];        /* 3 rows, 3 columns = 9 elements */

int matrix[3][3] = {
    {10, 20, 30},
    {40, 50, 60},
    {70, 80, 90}
};
```

**Rule to state in the exam:** `arr[rows][cols]` — the **first** index is always the row, the **second** is always the column. There is no way to swap them.

### 3.3 Nested loops — the only way to traverse

```c
#include <stdio.h>

int main(void)
{
    int matrix[3][3];
    int i, j;

    printf("Enter 9 elements:\n");
    for (i = 0; i < 3; i++) {              /* OUTER = rows */
        for (j = 0; j < 3; j++) {          /* INNER = columns */
            scanf("%d", &matrix[i][j]);
        }
    }

    printf("Matrix is:\n");
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");                      /* newline AFTER the inner loop */
    }
    return 0;
}
```

**Outer loop = rows (`i`), inner loop = columns (`j`).** The inner loop runs to completion for *each* single iteration of the outer loop. Access order is therefore:

```
matrix[0][0] matrix[0][1] matrix[0][2]
matrix[1][0] matrix[1][1] matrix[1][2]
matrix[2][0] matrix[2][1] matrix[2][2]
```

**Where the `printf("\n")` goes is the whole game:** inside the outer loop but **outside** the inner loop. Inside the inner loop would print 9 separate lines; outside both would print one long line.

### 3.4 Program: Addition of Two Matrices

```
A =        B =
1  2       5  6
3  4       7  8

C = A + B:
C[0][0] = A[0][0] + B[0][0] = 1 + 5 = 6
C[0][1] = A[0][1] + B[0][1] = 2 + 6 = 8
C[1][0] = A[1][0] + B[1][0] = 3 + 7 = 10
C[1][1] = A[1][1] + B[1][1] = 4 + 8 = 12

Result:
 6    8
10   12
```

```c
#include <stdio.h>

int main(void)
{
    int A[2][2] = {{1, 2}, {3, 4}};
    int B[2][2] = {{5, 6}, {7, 8}};
    int C[2][2];
    int i, j;

    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            C[i][j] = A[i][j] + B[i][j];   /* same position, element-wise */
        }
    }

    printf("Result:\n");
    for (i = 0; i < 2; i++) {
        for (j = 0; j < 2; j++) {
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }
    return 0;
}
```

**Matrix addition rule:** same dimensions required, and you add **position by position** — `C[i][j]` from `A[i][j] + B[i][j]`. Never from mismatched indices.

### 3.5 Row-major vs. Column-major — the memory question

A `int a[3][4]` is physically **one linear block of 12 elements**. Only the *order* differs between conventions.

```
   ROW-MAJOR  (C, C++, Java)  -- a full row is laid out next
   [0][0] [0][1] [0][2] [0][3] | [1][0] [1][1] [1][2] [1][3] | [2][0] ...
   offset:  0     1     2     3  |   4     5     6     7  |   8 ...

   COLUMN-MAJOR  (FORTRAN, MATLAB, R)  -- a full column is laid out next
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

**Intuition:** to reach row $i$, skip $i$ *whole rows* — each row has $C$ elements — then walk $j$ elements into that row. Total elements before it: $i \times C + j$.

$$\boxed{\text{Column-major: } \text{Address}(a[i][j]) = B + (j \times R + i) \times S}$$

**Intuition:** to reach column $j$, skip $j$ *whole columns* — each has $R$ elements — then walk $i$ elements down it.

**Worked drill.** `int a[3][5]`, base 2000, `sizeof(int) = 4`, find `a[2][3]`:
- Row-major: $2000 + (2 \times 5 + 3) \times 4 = 2000 + 52 = \boxed{2052}$
- Column-major: $2000 + (3 \times 3 + 2) \times 4 = 2000 + 44 = \boxed{2044}$

**Why it matters in real code:** CPUs load memory in cache *lines* (typically 64 bytes). Walking a **row** uses one cache line for many elements. Walking a **column** in a row-major array jumps a whole row each step → a cache miss per access. So the "correct" loop order in C is outer=row, inner=column. That is also the order used in section 3.3.

### 3.6 Array vs. String — the comparison the faculty asks for

| | Array | String |
|---|---|---|
| Holds | any same data type | characters only |
| Example | `int marks[5]` | `char name[20]` |
| Terminator | not required | **must** end with `'\0'` when used as a C string |
| Access | by index | by index |

---

# PART 2 — STRINGS

## 4. The String Model

### 4.1 What a string actually is

C has **no string data type**. A string is a **`char` array terminated by the null character `'\0'`** (ASCII value 0).

```
   "HELLO" is stored as:

   H     E     L     L     O     \0
   [0]   [1]   [2]   [3]   [4]   [5]
   addr  +1    +2    +3    +4    +5
```

**5 visible characters, but 6 array slots.** The terminator is the whole reason a 5-character string needs 6 bytes.

```c
char name[6] = "HELLO";     /* exactly enough */
char name[7] = "HELLO";     /* one spare — also fine */
char name[5] = "HELLO";     /* WRONG — overflows by 1 */
```

### 4.2 Character vs. String — the single most basic exam trap

```c
char ch   = 'A';     /* CHARACTER: single quotes  */
char name[] = "ABC"; /* STRING:    double quotes  */
```

| | Character | String |
|---|---|---|
| Quotes | `'A'` | `"A"` |
| How many | exactly one | a whole sequence |
| Comparison | `a == b` | `strcmp(a, b) == 0` |

`'A'` is **one byte** in memory. `"A"` is **two bytes** (`'A'` + `'\0'`). `'PIYUSH"` in single quotes is not a valid C character — a single-quoted literal holds exactly one character.

### 4.3 Three ways to declare a string — and the cost of each

```c
char a[] = "hi";            /* size 3  (h, i, \0) — auto-sized. PREFERRED */
char b[10] = "hi";          /* size 10 (h, i, \0 + 7 zero-filled)          */
char c[3] = {'h','i','\0'}; /* identical to a[] but verbose                */
char *p = "hi";             /* pointer to a READ-ONLY text-segment literal  */
```

```c
a[0] = 'H';    /* fine — 'a' lives on the stack, it is writable */
p[0] = 'H';    /* CRASH — the literal lives in read-only text memory */
```

| Form | Where it lives | Writable? | Use for |
|---|---|---|---|
| `char a[] = "hi"` | **Stack** | yes | default choice, mutating a string |
| `char *p = "hi"` | **Text (read-only)** | **no** | never mutate; `const char *` for literals |
| `char *p = malloc(n)` | **Heap** | yes | dynamic/variable-size strings |

### 4.4 Reading a Character

```c
char ch;
printf("Enter a character: ");
scanf("%c", &ch);            /* & required */
printf("You entered: %c", ch);
```

**Also available:** `ch = getchar();` — reads one character. It returns `int`, not `char`, precisely so it can report `EOF` (-1). **Never store `getchar()`'s result in a `char`** — you would lose the ability to detect end-of-input.

**Newline trap:** if a previous `scanf` read a number, the Enter key you pressed is still sitting in the input buffer. `scanf("%c", &ch)` then reads that leftover `'\n'` instead of what you typed. **Fix: put a space before `%c` → `scanf(" %c", &ch);`** The space means "skip any whitespace first."

### 4.5 Reading and Writing Strings

**Read a single word (no spaces):**

```c
char name[20];
scanf("%s", name);        /* NOT &name */
```

Two things to know here:

1. **No `&`.** An array name *already* is the address of its first element — that is exactly why `&name` would be a type error (`char (*)[20]` where `char *` is expected). Compare with `scanf("%d", &n)` where `n` is a plain `int`, so it *does* need `&`.
2. **`%s` stops at the first whitespace.** If the user types `Piyush Sharma`, only `Piyush` is stored.

**Read a full line (with spaces) — use `fgets`:**

```c
#include <stdio.h>

int main(void)
{
    char sentence[50];

    printf("Enter a sentence: ");
    fgets(sentence, sizeof(sentence), stdin);   /* reads the whole line */

    printf("You entered: %s", sentence);
    return 0;
}
```

`fgets(buf, size, stream)` reads until a **newline** or until `size - 1` characters — whichever comes first. It is **always bounded**, which is why it is safe where `scanf("%s")` is not. It keeps the trailing `'\n'` in the buffer, which is usually harmless for printing but matters if you later compare or convert the string.

**Write a string — two ways:**

```c
char name[] = "Piyush";
printf("%s\n", name);     /* no newline added automatically */
puts(name);                /* prints + adds a newline automatically */
```

> ### ⚠ Safe-Coding Note (annotation by agent, not from the source)
> The faculty handout writes `scanf("%s", name)` with **no width limit**. In modern C this is unsafe: input longer than 19 characters overflows a `char[20]` buffer. The bounded form is `scanf("%19s", name)` where 19 = size − 1. Same for `strcpy`/`strcat` — see section 7.4. **Exams accept the simple form; production code must not use it.** This is the same class of bug as Heartbleed.

### 4.6 Library string functions (`<string.h>`)

```c
#include <string.h>     /* REQUIRED — or the compiler warns/errors */
```

| Function | Signature | Does | Returns |
|---|---|---|---|
| `strlen` | `size_t strlen(const char *s)` | length **excluding** `'\0'` | count |
| `strcpy` | `char *strcpy(char *dst, const char *src)` | copy **including** `'\0'` | `dst` |
| `strncpy` | `char *strncpy(dst, src, n)` | copy up to `n`; may **omit** `'\0'` | `dst` |
| `strcat` | `char *strcat(char *dst, const char *src)` | append `src` after `dst`'s `'\0'` | `dst` |
| `strncat` | `char *strncat(dst, src, n)` | append up to `n`, **always** terminates | `dst` |
| `strcmp` | `int strcmp(const char *a, const char *b)` | compare ASCII, character by character | `0` equal, `<0` a<b, `>0` a>b |
| `strncmp` | `int strncmp(a, b, n)` | compare first `n` characters only | same |

**Remember the argument order:** `strcpy(destination, source)`. Copy **into** the first one. `strcat(destination, source)` — append the second one **to** the first.

Each in one program:

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
    /* strlen -> length */
    char str[50] = "Hello";
    printf("Length = %d\n", strlen(str));                 /* 5 */

    /* strcpy -> copy */
    char str1[50] = "Hello";
    char str2[50];
    strcpy(str2, str1);
    printf("Copied string = %s\n", str2);                 /* Hello */

    /* strcmp -> compare */
    char s1[50] = "apple", s2[50] = "apple";
    if (strcmp(s1, s2) == 0)
        printf("Strings are equal\n");
    else
        printf("Strings are not equal\n");

    /* strcat -> join */
    char a[50] = "Hello ";
    char b[50] = "World";
    strcat(a, b);
    printf("Combined string = %s\n", a);                  /* Hello World */
    return 0;
}
```

**`strcmp` returns 0 for equal.** That is the counter-intuitive bit: `0` is the "yes, equal" answer. It returns a negative number when `a` sorts before `b` (dictionary order) and a positive number when `a` sorts after. **Never test for `== 1`** — a non-zero return is not guaranteed to be exactly 1.

**Never use `==` to compare strings.** `a == b` compares the two *addresses*, not the contents. Two separate arrays holding `"apple"` almost certainly sit at different addresses, so `==` says "not equal" even though they are. Only `strcmp` looks at the characters.

## 5. String Operations From Scratch (the syllabus requirement)

> **Syllabus wording:** *"implementing string handling from scratch"*. The exam will ask you to write these loops without calling the library. The word **"from scratch" means: process one character at a time with a loop, instead of calling `strlen()`/`strcpy()`/`strcmp()`/`strcat()`.**

All of them share the same skeleton: **start at index 0, keep going while the character is not `'\0'`.**

### 5.1 Length

```
  H  E  L  L  O  \0
  0  1  2  3  4   5
  ^           ^   ^
  |           |   stop here
  start       |   length = 5
              5 chars counted
```

```c
#include <stdio.h>

int main(void)
{
    char str[100];
    int i = 0;
    int length = 0;

    printf("Enter a string: ");
    scanf("%s", str);

    while (str[i] != '\0') {
        length++;
        i++;
    }

    printf("Length = %d", length);
    return 0;
}
```

Trace for `"HELLO"`: `H`→length 1, `E`→2, `L`→3, `L`→4, `O`→5, then `str[5] == '\0'` → stop. **Length = 5.** This is conceptually exactly what `strlen()` does.

As a function (better exam form):

```c
int myStrlen(const char *s) {
    int n = 0;
    while (s[n] != '\0') n++;    /* walk until the terminator */
    return n;
}
```

### 5.2 Copy

```c
char source[100], destination[100];
int i = 0;

while (source[i] != '\0') {
    destination[i] = source[i];    /* character-by-character copy */
    i++;
}
destination[i] = '\0';             /* <-- THE LINE EXAMINERS LOOK FOR */
```

**`destination[i] = '\0';` is not optional.** The loop above copies only the visible characters. Without the terminator, `destination` is not a valid C string, and `printf("%s", destination)` will run off the end of the array until it happens to hit a zero byte somewhere in memory.

Compact from-scratch form (copies the `'\0'` inside the loop):

```c
char *myStrcpy(char *dst, const char *src) {
    int i = 0;
    while ((dst[i] = src[i]) != '\0') i++;   /* assign, then test */
    return dst;
}
```

### 5.3 Compare

```c
char str1[100], str2[100];
int i = 0;
int equal = 1;                     /* assume equal until disproven */

while (str1[i] != '\0' || str2[i] != '\0') {
    if (str1[i] != str2[i]) {
        equal = 0;                 /* difference found */
        break;
    }
    i++;
}

if (equal == 1) printf("Strings are equal");
else            printf("Strings are not equal");
```

Two details worth explaining in an exam:

- The loop condition uses **`||` (OR), not `&&`**. Two strings are equal only if both end at the same index. With `&&` the loop would stop as soon as *either* string ended, so `"HELLO"` and `"HELLO WORLD"` would wrongly compare equal.
- `equal` is a **flag**: start assuming yes, set to no on the first mismatch, `break` out — no need to keep comparing once a difference is proven.

Proper C returns a comparison value instead:

```c
int myStrcmp(const char *a, const char *b) {
    while (*a && *a == *b) { a++; b++; }              /* skip the common prefix */
    return (unsigned char)*a - (unsigned char)*b;     /* signed char is a trap */
}
```

The `unsigned char` cast matters because plain `char` may be signed on some systems, so a negative difference can come out with the wrong sign.

### 5.4 Concatenate

```c
char str1[100], str2[50];
int i = 0, j = 0;

/* Step 1: walk i to the end of str1 */
while (str1[i] != '\0') {
    i++;
}

/* Step 2: copy str2 into the space starting at i */
while (str2[j] != '\0') {
    str1[i] = str2[j];
    i++;
    j++;
}

/* Step 3: terminate the combined string */
str1[i] = '\0';
```

Worked example, `str1 = "Hello"`, `str2 = "World"`:

| After step 1 | `str1 = H e l l o \0` with `i` pointing at the `\0` |
|---|---|
| Iteration 1 | `str1[5] = 'W'` |
| Iteration 2 | `str1[6] = 'o'` |
| Iteration 3 | `str1[7] = 'r'` |
| Iteration 4 | `str1[8] = 'l'` |
| Iteration 5 | `str1[9] = 'd'` |
| Step 3 | `str1[10] = '\0'` |

Final: `H e l l o W o r l d \0` → **"HelloWorld"**.

**Two `i` variables by hand, one via `strlen`:** `i = strlen(str1);` replaces step 1 entirely.

**Why is `str1` declared bigger than `str2`?** `str1` holds both strings plus the terminator. If `str1[100]` and `str2[50]`, the combined result needs up to 149 bytes — it fits. Declaring `str1` the same small size as `str2` would overflow.

### 5.5 Reverse

```c
char str[100];
int length = 0;
int i;

printf("Enter a string: ");
scanf("%s", str);

while (str[length] != '\0') {
    length++;
}

printf("Reverse = ");
for (i = length - 1; i >= 0; i--) {
    printf("%c", str[i]);
}
return 0;
```

For `"HELLO"` (length 5), we print indices:

```
   index:  4     3     2     1     0
   char:   O     L     L     E     H      ->  OLLEH
```

**Three traps examiners set deliberately:**

| Trap | Wrong code | Result | Correct |
|---|---|---|---|
| Off-by-one start | `for (i = length; ...)` | prints the `'\0'` first — nothing visible | start at `length - 1` |
| Off-by-one end | `for (i = length - 1; i > 0; i--)` | **skips `str[0]`** | condition is `i >= 0` |
| Unsigned index | `size_t i` with `i >= 0` | **infinite loop** — unsigned is never negative | use signed `int i` |

### 5.6 Count vowels — a classic applied drill

```c
#include <stdio.h>

int main(void)
{
    char str[100];
    int i = 0;
    int count = 0;

    printf("Enter a string: ");
    scanf("%s", str);

    while (str[i] != '\0') {
        if (str[i] == 'a' || str[i] == 'e' || str[i] == 'i' ||
            str[i] == 'o' || str[i] == 'u') {
            count++;
        }
        i++;
    }

    printf("Number of vowels = %d", count);
    return 0;
}
```

`"education"` → `e, u, a, i, o` → **Number of vowels = 5**.

Note this version tests only **lowercase**. Input `Education` would report 4. Handling both cases means testing `str[i] == 'a' || str[i] == 'A'` — a very common viva question.

## 6. Palindrome Check (combines everything)

Not every string problem has a library function. This one uses `strlen` + indexing + a loop:

```c
#include <stdio.h>
#include <string.h>

int main(void)
{
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

    if (isPalindrome) printf("%s is a palindrome\n", str);
    else               printf("%s is not a palindrome\n", str);
    return 0;
}
```

**The idea:** a palindrome reads the same backwards, so compare the **first half** against the **last half** in mirror positions. `str[i]` pairs with `str[len - 1 - i]` — index `i` from the front, index `len-1-i` from the back. Loop only `i < len / 2` — the second half is guaranteed to match if the first half does.

Trace for `"level"` (len 5):

| i | `str[i]` | index `5-1-i` | `str[...]` | Match? |
|---|---|---|---|---|
| 0 | `l` | 4 | `l` | yes |
| 1 | `e` | 3 | `e` | yes |
| — | — | — | — | `i < 2` now false → loop ends → **palindrome** |

---

# PART 3 — EXAM FOCUS

## 7. `strcpy` — The Dedicated Drill

This is the highest-frequency string function in SPM OST/quiz papers. Learn it until you can write it asleep.

### 7.1 What `strcpy` actually does

```c
char *strcpy(char *destination, const char *source);
```

It copies **every character of `source`, including the terminating `'\0'`**, into `destination`, and returns `destination`.

```
   BEFORE                                AFTER
   source      =  H  e  l  l  o  \0     (6 bytes)
   destination =  ?  ?  ?  ?  ?  ?     (uninitialized)

   strcpy(destination, source) does:
   destination[0] = 'H'
   destination[1] = 'e'
   destination[2] = 'l'
   destination[3] = 'l'
   destination[4] = 'o'
   destination[5] = '\0'      <-- the terminator is copied too

   AFTER
   destination =  H  e  l  l  o  \0     (identical to source)
```

**Total bytes written = `strlen(source) + 1`.**

### 7.2 Library vs. from-scratch, side by side

| | Version |
|---|---|
| **Library** | `strcpy(dst, src);` |
| **From scratch (loop A — copy then terminate)** | `while (src[i] != '\0') { dst[i] = src[i]; i++; } dst[i] = '\0';` |
| **From scratch (loop B — the canonical exam one-liner)** | `while ((dst[i] = src[i]) != '\0') i++;` |

### 7.3 Examiner checklist

When marking a from-scratch `strcpy`, look for exactly these. Miss one, lose the mark.

- [x] Loop condition terminates at **`'\0'`** — not at a fixed count, not `strlen` alone
- [x] The **`'\0'` is copied / re-added** (so `dst` becomes a valid C string)
- [x] Function returns **`dst`** (so calls can be chained: `strcpy(strcpy(a,b),c)`)
- [x] Loop index **starts at 0** and **increments by 1** each pass
- [x] `source` declared `const char *` in the signature (it is not modified)

### 7.4 Traps

| Trap | Code | What happens | Fix |
|---|---|---|---|
| **Destination too small** | `char d[3]; strcpy(d, "hiya");` | writes 5 bytes into 3 → memory corruption | `char d[5];` (strlen+1) or bigger |
| **Source not terminated** | `char s[5] = {'h','i'}; strcpy(d, s);` | runs past `s` until it finds a stray zero | always `'\0'`-terminate |
| **Copying a literal** | `char *p = "hi"; strcpy(p, "bye");` | **segfault** — text segment is read-only | `char p[] = "hi";` |
| **Overlapping regions** | `strcpy(s + 2, s);` | undefined behaviour | use `memmove` |
| **Ignoring the return** | `strcpy(d, s);` works, but | you lose the ability to chain | use the returned pointer |
| **Argument order reversed** | `strcpy(src, dst);` | clobbers your source | it is always `strcpy(dest, src)` |

### 7.5 `strncpy` — the contrast the syllabus loves

```c
char *strncpy(char *dst, const char *src, size_t n);
```

Copies at most `n` characters. **The dangerous part:** if `strlen(src) >= n`, it copies `n` characters and **stops without adding `'\0'`**. The result is not a valid C string.

```c
char dst[5];
strncpy(dst, "hello world", 5);   /* dst = "hello" but NO '\0' */
printf("%s", dst);                 /* reads past dst — garbage or crash */
```

**The fix — always terminate manually:**

```c
strncpy(dst, "hello world", 5);
dst[4] = '\0';                     /* dst[sizeof(dst) - 1] = '\0'; */
```

| Function | Copies | Always ends with `'\0'`? | Bounded? |
|---|---|---|---|
| `strcpy` | everything | **yes** | **no** |
| `strncpy` | up to `n` | **only if `strlen(src) < n`** | yes |
| `strcat` | appends everything | **yes** | **no** |
| `strncat` | up to `n` appended | **yes** | yes |

The pattern: **`strcpy`/`strcat` are unbounded; the `n` versions are bounded.** That is why production C prefers `snprintf(dst, sizeof dst, "%s", src)` or the `n` variants.

### 7.6 Predict-output drills

**Drill 1 — sizes.**

```c
char s[] = "abc";
printf("%zu %zu\n", strlen(s), sizeof(s));
```

<details><summary>Answer</summary>

`3 4` — `strlen` counts `a b c` (excluding `'\0'`); `sizeof` counts all 4 array bytes including the terminator.
</details>

**Drill 2 — write to literal vs. array.**

```c
char s[] = "abc";
char *p = "abc";
printf("%c %c\n", s[1], p[1]);
s[0] = 'x';          /* OK   */
/* p[0] = 'x'; */     /* UB — segfault */
```

<details><summary>Answer</summary>

`b b`, then `s` becomes `"xbc"`. Uncommenting `p[0]='x'` is **undefined behaviour** — the literal is in read-only text memory, so it crashes on virtually every real system.
</details>

**Drill 3 — `strcmp` return value.**

```c
char a[] = "apple", b[] = "apple";
printf("%d\n", strcmp(a, b) == 1);
```

<details><summary>Answer</summary>

`0` — the strings are equal, so `strcmp` returns `0`, and `0 == 1` is false. Testing `== 1` for equality is a **wrong** idiom; the test is `strcmp(a,b) == 0`.
</details>

**Drill 4 — the overflow.**

```c
char d[4];
strcpy(d, "abcde");
printf("%s\n", d);
```

<details><summary>Answer</summary>

**Undefined behaviour.** `"abcde"` needs 6 bytes; `d` has 4. The program silently corrupts adjacent memory. It may print `abcde`, print garbage, or crash — none of that is guaranteed. (`char d[6]` would be correct.)
</details>

**Drill 5 — copy into a literal.**

```c
char *p = "hi";
strcpy(p, "bye");
```

<details><summary>Answer</summary>

**Crash.** `p` points into the read-only **text** segment. Writing there is undefined behaviour; on a normal system it segfaults. Fix: `char p[] = "hi";` — that puts the array on the writable stack.
</details>

**Drill 6 — partial concatenation (EX5 tracing question).**

```c
char a[20] = "Data";
char b[] = "Structures";
strcat(a, b);
```

<details><summary>Answer</summary>

`a` becomes `"DataStructures"` (14 characters + `'\0'` = 15 bytes, fits in 20). `a` needs the extra space because `strcat` appends to whatever `a` already holds — a buffer sized only for `"Data"` (5 bytes) would overflow. This is exactly the EX5 post-lab question.
</details>

## 8. Master Trap Table (whole module)

| Trap | What happens | Fix |
|---|---|---|
| Index starts at 1 | you skip element 0 and read past the end | index range is `0 … size-1` |
| No bounds checking in C | silent memory corruption, **not** an error message | check `i < n` yourself |
| `char s[5] = "hello"` | needs 6 bytes → overflow by 1 | declare `[6]`, or use `[]` |
| `char *p = "hi"; p[0]='H'` | segfault (text segment read-only) | use `char p[] = "hi"` |
| `scanf("%s", s)` with no width | overflow on long input | `"%19s"` for `s[20]`, or `fgets` |
| `scanf("%s", &s)` | type error — array name is already an address | drop the `&` |
| `scanf("%c")` after a numeric read | reads the leftover `'\n'` | `scanf(" %c", &ch)` |
| `==` on strings | compares addresses, not contents | `strcmp(a,b) == 0` |
| `strcmp(...) == 1` for equality | wrong — equal is `0` | test `== 0` |
| `strncpy` with no manual `'\0'` | later `printf` reads past the buffer | `dst[n-1] = '\0';` |
| `gets()` | **removed from C** (unsafe) | `fgets()` |
| reverse: start at `n` | prints the `'\0'` | start at `n - 1` |
| reverse: `i > 0` | skips `str[0]` | condition `i >= 0` |
| reverse: `size_t i` | infinite loop (unsigned never negative) | use signed `int i` |
| 2D loop order flipped | cache misses, 4× slower on big matrices | outer = row, inner = column |
| compare loop uses `&&` | `"HELLO"` == `"HELLO WORLD"` wrongly true | use `\|\|` in the loop condition |

---

## 9. Formula & Syntax Quick Reference

| Quantity | Formula / pattern | Notes |
|---|---|---|
| 1D address | $B + i \times S$ | zero-based |
| Row-major 2D address | $B + (i \times C + j) \times S$ | C / C++ / Java |
| Column-major 2D address | $B + (j \times R + i) \times S$ | FORTRAN / MATLAB |
| Last valid index | size − 1 | indices run `0 … size-1` |
| Element count | `sizeof(a) / sizeof(a[0])` | only inside the declaring function |
| Array total bytes | n × `sizeof(type)` | |
| Row-major cache loop | outer `i` (row), inner `j` (col) | the fast order in C |
| String length | `strlen(s)` | excludes `'\0'` |
| Array size of a string | `sizeof(s)` | includes `'\0'` + spare capacity |
| `strcmp` equal | `== 0` | not `== 1` |
| Copy from scratch | `while ((dst[i]=src[i]) != '\0') i++;` | copies the terminator |
| Copy (2-step) | loop, then `dst[i]='\0';` | the line examiners look for |
| Compare from scratch | `while (*a && *a==*b) {a++;b++;}` then signed difference | cast to `unsigned char` |
| Read a word | `scanf("%19s", s);` | width = size − 1, **no** `&` |
| Read a char | `scanf(" %c", &ch);` | leading space skips newline |
| Read a line | `fgets(s, sizeof s, stdin);` | `gets()` is removed |
| Write a string | `printf("%s", s);` or `puts(s);` | `puts` adds `\n` |

---

## 10. Practice Program List (from the source handout)

| # | Program | Main concept |
|---|---|---|
| 1 | Read and display a 1D array | array basics |
| 2 | Find sum of array | array + loop |
| 3 | Find largest element | array + `if` |
| 4 | Find smallest element | array + `if` |
| 5 | Calculate average | array + arithmetic (`(float)sum / n`) |
| 6 | Read and display a 2D array | matrix, nested loops |
| 7 | Add two matrices | 2D array |
| 8 | Read and display a string | character array |
| 9 | Find string length from scratch | `'\0'` |
| 10 | Copy string from scratch | char-by-char copying |
| 11 | Compare strings from scratch | char comparison |
| 12 | Concatenate strings from scratch | string manipulation |
| 13 | Reverse a string | array indexing |
| 14 | Count vowels and consonants | character processing |

Also required in EX5: **word count** (read with `fgets`), **character frequency**, **lowercase → uppercase without a library**, **anagram check**, **remove all spaces**.

---

## 11. Laboratory Mapping

| Experiment | Topic | Page to revise from |
|---|---|---|
| **EX3** | Looping control structures (`for`/`while`/`do-while`, `break`/`continue`, nested loops) | sections 2.4, 3.3 (the nested-loop patterns) |
| **EX4** | Arrays — declare/init/traverse 1D, sum/average, linear search, max/min, 2D, matrix addition | Part 1 of this page |
| **EX5** | Strings — declare/init/display, `fgets`, `strlen`/`strcpy`/`strcat`/`strcmp`, palindrome | Part 2 + section 7 |

Full write-ups, task lists, and post-lab Q&A: `spm-lab-exp3-4-5-guides.md`.

**`avg` needs a cast:** `avg = (float) sum / 5;` — without the cast, integer division truncates and `150/5` style cases hide the bug until you test a non-divisible case.

---

## 12. Cross-References

- **Deeper exam banks:** [[module-3-arrays]] (binary search, bubble sort, insertion/deletion shifts, full address derivations) · [[module-3-strings]] (from-scratch `myStrcat`, full `fgets` stripping, trap table)
- **Lecture companion:** [[spm-string-functions-char-equality-reverse]] — the classroom cut (char equality, indexing, reverse pattern)
- **Syllabus:** [[syllabus-316U06C107]] · [[assessment-guide-ese-ost-quiz]] (OST/ESE patterns) · [[formula-sheet-spm]]
- **Lab:** [[spm-lab-exp3-4-5-guides]] · [[spm-lab-exp1-exp2-guides]] · [[lab-ca-and-experiments]]
- **Practicals:** [[spm-pic-question-bank]] · [[spm-practice-bank-module2]] · [[spm-quiz-bank]]
- **Pointers view:** [[module-4-structures-unions-pointers]] (`char *` vs `char[]`, array decay)
- **Foundation:** [[module-2-program-control-functions]] (the loops this page depends on) · [[module-1-spm-c-basics]] (memory layout — stack vs text)

*Sources ingested 2026-10-01: `raw-sources/SPM Lecture/Unit No.3 Arrays_Strings.pdf`, `raw-sources/SPM Lab/EX4.docx`, `raw-sources/SPM Lab/EX5.docx`, `raw-sources/SPM_Syllabus_316U06C107.md`.*

> **Unopened sources in the same folders** (recorded 2026-10-01 for the next ingest): `raw-sources/SPM Lecture/` holds **8 PPTX decks** that were NOT opened in this pass — `SPM_Module1.pptx`, `SPM_Module1_1.1_PPT.pptx`, `SPM_Module1_2.pptx` … `SPM_Module1_5.pptx`, `SPM_Module3_1.pptx`, `SPM_Module3_2.pptx`. A PPTX is a ZIP of `ppt/slides/slideN.xml`, so it needs a separate extraction pass (python-pptx or direct unzip) — PyMuPDF will not read it. Module 1 / Module 3 PPT deltas may already be partly captured in [[spm-module1-faculty-companion]]; **verify coverage before re-ingesting.** Note the mismatch: this page is sourced from the Arrays_Strings **PDF**, which is a Module 3 handout — the fact that `SPM_Module3_*.pptx` decks exist unopened is a known gap, not an oversight.