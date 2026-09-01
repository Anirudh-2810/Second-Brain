---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "Module 4.2-4.3 + Self-Learning — Structures, Unions, Pointers & File Handling"
tags: [spm, structures, unions, pointers, file-handling, c-programming, 316U06C107, 316U06C107-M4]
last_updated: "2026-09-02"
confidence: high
description: "SPM M4.2-M4.3 + self-learning — structs/unions (declaration, init, members, array of structs), struct vs union layout, pointers (decl, arithmetic, pass-by-ref, returning pointers) and file handling basics."
prerequisites: ["Module 4.1 User Defined Functions", "Module 3 Arrays & Strings", "Pointers basics"]
---

## For future agent
This page finishes M4 for the official syllabus. Prior vault page [[module-4-user-defined-functions]] covered UDFs/recursion only; this page adds the remaining syllabus units 4.2 (structures/unions), 4.3 (pointers + pointer-functions), and self-learning file handling/unions-vs-structs. Use it for EXP7-8 and Assignment 2, plus ESE theory Q4b.

# Module 4.2–4.3 — Structures, Unions, Pointers & File Handling

> Syllabus: [[syllabus-316U06C107#module-map--30-hrs]] M4 (12 hrs, CO4) | Units 4.2–4.3 + Self-Learning | Sources: [[raw-sources/SPM_Syllabus_316U06C107]] §§4.2-4.3
> Prereq: [[module-4-user-defined-functions]] (call semantics) · [[module-3-arrays]] (array of structs is array) · [[module-3-strings]] (strings are char arrays)
> Labs: EXP7 structures/unions (W12), EXP8 pointers (W14), Assignment 2 (W15) — see [[lab-ca-and-experiments#6-list-of-experiments--10-items-exp1-8--2-assignments]] | Cram: [[c-programming-master-study-guide#43-storage-classes]]

## 1. Structures — Declaring, Defining, Initialization, Accessing Members

**Why structs?** C arrays hold **one type**; a `struct` holds **heterogeneous** fields (a record) — e.g., a student has `int roll + char name[30] + float cgpa`. This is the user-defined type mechanism for M4.

### 1.1 Declaration & Definition

```c
#include <stdio.h>
#include <string.h>

// Declaration (blueprint) — no memory yet beyond type definition
struct Student {
    int   roll;
    char  name[30];
    float cgpa;
};

// Definition + initialization (allocates memory)
struct Student s1 = {101, "Asha", 8.9};
struct Student s2 = {.roll=102, .name="Ravi", .cgpa=9.1}; // designated init (C99)

int main(void) {
    printf("%d %s %.1f\n", s1.roll, s1.name, s1.cgpa); // dot operator
    return 0;
}
```

**Access:**
- `obj.member` when `obj` is a struct **value**.
- `ptr->member` when `ptr` is `struct Student *` — sugar for `(*ptr).member`.

### 1.2 Array of Structures — the Lab Pattern

```c
#define N 3
struct Student cls[N];

for (int i = 0; i < N; i++) {
    scanf("%d %29s %f", &cls[i].roll, cls[i].name, &cls[i].cgpa);
    // note: cls[i].name needs no & — it decays to char*
}
for (int i = 0; i < N; i++)
    printf("%d %s %.1f\n", cls[i].roll, cls[i].name, cls[i].cgpa);
```

Array of structs inherits array's contiguity — `cls[1]` starts `sizeof(struct Student)` bytes after `cls[0]`.

### 1.3 Struct Memory — Padding & sizeof

```c
struct Example {
    char  c;   // 1 byte
    // 3 bytes padding (alignment to 4)
    int   x;   // 4 bytes
    char  d;   // 1 byte
    // 3 bytes tail padding → total 12, not 6
};
printf("%zu\n", sizeof(struct Example)); // typically 12, not 6
```

**Rule:** Compiler inserts **padding** to align each member to its natural alignment (int→4, double→8). `sizeof(struct)` ≥ sum of members. Ordering members largest-first reduces padding — an ESE theory favorite.

### 1.4 Passing Structs to Functions

```c
void printByValue(struct Student s) { printf("%s %.1f\n", s.name, s.cgpa); } // copies whole struct — expensive
void bumpCgpa(struct Student *p) { p->cgpa += 0.5; }                          // pass address — cheap + mutable

// call:
printByValue(s1);      // copy
bumpCgpa(&s1);         // pass-by-reference via pointer
```

**Exam trap:** `struct` assignment (`a = b`) copies **all** members (unlike arrays). `==` on structs is **illegal** — compare field by field.

## 2. Unions — And Structure vs Union

### 2.1 Declaration

```c
union Data {
    int   i;
    float f;
    char  str[20];
};
union Data d;
d.i = 10;           // active member is i
d.f = 3.14f;        // now active member is f — overwrites same memory!
printf("%f\n", d.f); // 3.14 — correct if f is the last written member
// printf("%d\n", d.i); // UB — reading inactive member (type punning)
```

### 2.2 Structure vs Union — Layout Comparison

```
struct S { int i; float f; };   // TWO slots
┌─────────┬─────────┐
│  i (4B) │  f (4B) │  size ≈ 8 (+ padding), members independent
└─────────┴─────────┘

union U { int i; float f; };    // ONE shared slot
┌─────────────────┐
│  i / f overlap  │  size = max(sizeof members) = 4, only one member valid at a time
└─────────────────┘
```

| Property | `struct` | `union` |
|----------|----------|---------|
| Memory | Sum of members + padding | **Max** of members (shared storage) |
| `sizeof` | ≥ sum | = max |
| Members valid | All simultaneously | **Only last written** |
| Use case | Records (student, employee) | Memory-saving variants (protocol packets, variant records), embedded registers |
| Init | Can init multiple members | Only **first** member in C89, designated union init in C99 |

**Assignment 2 relevance:** Syllabus self-learning explicitly lists "Unions, Structure Vs Unions" — expect a Q4b theory question asking the table above plus `sizeof` calculation.

## 3. Pointers — Declaration, Initialization, Arithmetic, Expressions

### 3.1 Declaration & Initialization

```c
int x = 42;
int *p = &x;        // p holds ADDRESS of x
int **pp = &p;      // pointer to pointer
int *q = NULL;      // null pointer — safe sentinel; dereferencing is UB

printf("x=%d via *p=%d addr %p\n", x, *p, (void*)p);
printf("* deref vs &: *p==x (%d), p==&x (%d)\n", *p==x, p==&x);
```

**Operators:** `&` = "address of" (value → pointer), `*` = "value at" (pointer → value). `*(&x)==x` always.

### 3.2 Pointer Arithmetic — Scaled by sizeof (Exam-Critical)

Pointer arithmetic is **typed** — adding 1 advances `sizeof(*p)` bytes, not 1 byte.

```c
int arr[3] = {10,20,30};
int *p = arr;           // decays to &arr[0]
printf("%d\n", *p);     // 10
p++;                    // advances 4 bytes (sizeof int), now points to arr[1]
printf("%d\n", *p);     // 20
printf("p[1]=%d same as *(p+1)=%d\n", p[1], *(p+1)); // 30,30 — a[i] ≡ *(a+i)

// difference is in ELEMENTS, not bytes:
int *q = &arr[2];
printf("q-p = %td\n", q - p); // 1 (element count), not 4
```

| Expression | Result | Notes |
|------------|--------|-------|
| `p + 1` | `p + sizeof(*p)` | scaled |
| `p - q` | (`p - q`)/sizeof(*p) in elements | only within same array — else UB |
| `p++` / `++p` | advance/retreat | valid only inside array bounds (one-past-end allowed but not dereferenceable) |

**Common ESE trap:** `char *cp` → `cp+1` moves 1 byte; `int *ip` → `ip+1` moves 4 bytes. Same `+1`, different distance.

### 3.3 Pointers and Functions — Pass by Reference, Returning Pointers

C is **pass-by-value** — but passing the **address** simulates pass-by-reference:

```c
void swap(int *a, int *b) { int t=*a; *a=*b; *b=t; }
int x=1,y=2; swap(&x,&y); // x=2,y=1

// Returning a pointer — safe vs unsafe
int *makeArray(size_t n) {
    int *p = malloc(n * sizeof *p); // HEAP — survives return
    return p; // safe — caller must free(p)
}
int *bad(void) {
    int local[3]={1,2,3};
    return local; // BUG — returns address of STACK frame that dies on return (dangling)
}
```

**Rule:** Never return address of a local/stack variable. Return heap (`malloc`) or `static` storage, and document who frees.

### 3.4 Pointer Expressions — Operator Precedence

| Declaration | Meaning | Dereferences like |
|-------------|---------|-------------------|
| `int *p[3]` | array of 3 pointers | `*p[i]` ≡ `*(p[i])` |
| `int (*p)[3]` | pointer to array of 3 ints | `(*p)[i]` |
| `int *f(void)` | function returning pointer | — |
| `int (*f)(int)` | pointer to function | `(*f)(5)` |

Read declarations **right-to-left** — see [[module-4-user-defined-functions#16-function-pointers--variadic-functions]] for function-pointer depth.

## 4. Array-Pointer Duality (Quiz Favorite)

```c
int a[5]={10,20,30,40,50};
int *p = a; // a decays to &a[0] in most contexts
// These are identical:
a[i] == *(a+i) == *(p+i) == p[i]
// But these differ:
sizeof(a) // 20 (array size)
sizeof(p) // 8 (pointer size on 64-bit)
```

**Parameter rule:** `void f(int a[])` ≡ `void f(int *a)` — array parameter **decays** to pointer; inside `f`, `sizeof(a)` is pointer size, so you must pass `n`.

## 5. File Handling — Self-Learning (Expected in Assignment 2 & Quiz)

Syllabus self-learning lists File Handling — not taught in lecture weeks but examinable. Minimum viable coverage:

| Mode | Meaning | If file exists | If not |
|------|---------|---------------|--------|
| `"r"` | read (text) | open for reading | `NULL` / error |
| `"w"` | write (text) | **truncate** (erase) | create |
| `"a"` | append | open at end | create |
| `"r+"` | read+write | open, no truncate | error |
| `"w+"` | read+write | truncate | create |
| `"a+"` | read+write append | open at end | create |
| Add `b` (`"rb"`, `"wb"`) for binary | — | — | — |

```c
#include <stdio.h>
int main(void) {
    FILE *fp = fopen("data.txt", "w");
    if (!fp) { perror("fopen"); return 1; }
    fprintf(fp, "roll=%d name=%s\n", 101, "Asha");
    fclose(fp);

    fp = fopen("data.txt", "r");
    if (!fp) return 1;
    char buf[100];
    while (fgets(buf, sizeof buf, fp)) printf("%s", buf);
    fclose(fp);
    return 0;
}
```

**Key APIs:** `fopen/fclose`, `fprintf/fscanf`, `fgets/fputs`, `fread/fwrite` (binary), `fseek/ftell/rewind`, `feof/ferror`. Always check `fopen` for `NULL` and `fclose` every opened file.

**Binary vs text:** On Windows, text mode translates `\n` ↔ `\r\n`; binary (`"wb"`) does not.

## 6. Exam-Trap Checklist (from [[lab-ca-and-experiments]] write-up rubric)

- Assignment 2 must demonstrate **structures + pointers + file handling** — include handwritten algorithm and `sizeof(struct)` with padding explanation for full write-up marks.
- Quiz debug pattern: missing `&` in `scanf("%d",&s.roll)`, `==` vs `=` in `if (p->cgpa==8.5)`, forgetting `->` vs `.`, dereferencing `NULL`, forgetting `free` after `malloc`.
- ESE Q4b sample: "Structure vs Union with diagram and `sizeof` example" — draw §2 layout diagram.

## Cross-References

- UDFs/recursion: [[module-4-user-defined-functions]] (stack frames, tail recursion)
- Arrays/strings: [[module-3-arrays]] · [[module-3-strings]]
- Memory layout: [[module-1-spm-c-basics#17-process-memory-layout--stack-heap-data-text-deep-dive]] (stack vs heap for returned pointers)
- Cram: [[c-programming-master-study-guide#42-recursion--stack-execution]] · Syntax: [[formula-sheet-spm#7-functions-module-4-core]]

*Labs: EXP7 structures & unions, EXP8 pointers, Assignment 2 (Module 4) — due per [[lesson-plan-2026-27#week-by-week]].*
