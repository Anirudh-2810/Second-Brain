---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "Module 3.2 — Strings Lecture: functions, char equality, indexing, reverse"
date: "2026-09-30"
description: "SPM lecture notes on C strings — char vs string equality, indexing, string.h functions, and printing a string in reverse with for loops, with from-scratch implementations and exam traps."
tags: [spm, strings, c-programming, 316U06C107, lecture, exam-prep]
last_updated: "2026-09-30"
confidence: high
---

## For future agent

Lecture companion to [[module-3-strings]] (which owns the full M3.2 theory). This page is the classroom cut: char equality vs `strcmp`, indexing, the `string.h` set OST expects, and the reverse-with-`for` pattern with its `n-1` / `>=0` / signed-`int` traps. Concept home stays in [[module-3-strings]]; arrays foundation in [[module-3-arrays]].

# SPM Lecture — Strings: Functions, Equality, Indexing, Reverse

## 1. String model in one paragraph

C has no string type. A string is a `char` array ending in `'\0'`. Every handler stops at the first `'\0'`. `strlen` excludes it, `sizeof` includes it, and you must allocate `+1` for it. Full model: [[module-3-strings#1-what-is-a-string-in-c]].

```c
char s[6] = "hello";  // h e l l o \0  — indexes 0..5
```

## 2. Indexing

`s[i]` is O(1) array access. Valid data lives in `s[0..n-1]` where `n = strlen(s)`; `s[n]` is `'\0'`.

```c
char s[] = "abc";
printf("%c %c\n", s[0], s[1]);  // a b
s[0] = 'x';  // fine on stack arrays -> "xbc"
// char *p = "abc"; p[0] = 'x';  // UB — literal lives in read-only text
```

Loop idiom (scan to terminator):

```c
for (int i = 0; s[i] != '\0'; i++) putchar(s[i]);
```

## 3. Are two chars equal? Char vs string

**Single chars** — plain `==`:

```c
char a = 'x', b = 'x';
if (a == b) printf("same");  // ASCII values compared
```

**Whole strings** — NEVER `==` (compares addresses). Use `strcmp`:

```c
#include <string.h>
if (strcmp(s1, s2) == 0) printf("equal");  // 0 means equal
// <0 means s1<s2, >0 means s1>s2 — never test ==1
```

From scratch (syllabus requirement):

```c
int myStrcmp(const char *a, const char *b) {
    while (*a && *a == *b) { a++; b++; }
    return (unsigned char)*a - (unsigned char)*b;  // unsigned: plain char may be signed
}
```

## 4. String functions OST expects

```c
#include <string.h>
strlen(s)            // length excluding \0 — O(n) scan
strcpy(dst, src)     // copy incl. \0 — caller ensures dst fits
strcat(dst, src)     // append after dst's \0
strcmp(a, b)         // 0 equal / <0 a<b / >0 a>b (ASCII order)
strncmp(a, b, n)     // first n chars only
strncpy(dst, src, n)  // may MISS \0 when src>=n -> add dst[n-1]='\0'
```

Input patterns:

```c
char s[20];
scanf("%19s", s);            // word, no & — width = size-1
fgets(s, sizeof s, stdin);   // line with spaces (preferred)
s[strcspn(s, "\n")] = '\0';  // strip trailing \n
```

From-scratch `strlen` / `strcpy` (exam must-write):

```c
size_t myStrlen(const char *s) { size_t n = 0; while (s[n] != '\0') n++; return n; }
char *myStrcpy(char *dst, const char *src) {
    size_t i = 0; while ((dst[i] = src[i]) != '\0') i++; return dst;
}
```

## 5. Reverse a string with a for loop (the lecture pattern)

```c
#include <stdio.h>
#include <string.h>
int main(void) {
    char s[20] = "hello";
    int n = strlen(s);
    for (int i = n - 1; i >= 0; i--) printf("%c", s[i]);  // olleh
    return 0;
}
```

Without the library:

```c
int n = 0; while (s[n] != '\0') n++;
for (int i = n - 1; i >= 0; i--) putchar(s[i]);
```

Three traps examiners love:

1. Start at `n-1`, not `n` (`s[n]` is `'\0'` — prints nothing/garbage).
2. Condition `i >= 0`, not `i > 0` (else `s[0]` is skipped).
3. `i` must be signed `int`, not `size_t` (unsigned `i >= 0` is always true → infinite loop).

## 6. Quiz drill (predict output)

```c
char s[] = "abc";
printf("%zu %zu\n", strlen(s), sizeof(s));  // 3 4 — sizeof counts \0
printf("%c\n", s[strlen(s)-1]);             // c
for (int i = strlen(s)-1; i >= 0; i--) printf("%c", s[i]);  // cba
```

## See also

- [[module-3-strings]] — concept home (declarations, fgets stripping, myStrcat, full trap table)
- [[module-3-arrays]] — contiguous-array foundation + address formulas
- [[formula-sheet-spm]] — one-page syntax sheet
- [[c-programming-master-study-guide]] — 4-chapter cram guide
