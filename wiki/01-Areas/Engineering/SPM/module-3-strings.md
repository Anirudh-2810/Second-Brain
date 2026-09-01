---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "Module 3.2 — Character Arrays & Strings"
tags: [spm, strings, char-arrays, c-programming, 316U06C107, string-handling, ascii]
last_updated: "2026-09-02"
confidence: high
description: "SPM M3.2 strings — char array vs string, '\\0' terminator, reading/writing, library handlers vs implementing strlen/strcpy/strcat/strcmp from scratch, with exam traps."
prerequisites: ["Module 3.1 Arrays (1D/2D)", "Pointers basics"]
---

## For future agent
This page closes the M3 gap in the vault (previously only arrays). It implements the syllabus unit 3.2 requirement: declaring/initializing strings, R/W of chars and strings, operations, and `from scratch` string handling. Use it for OST/quiz predict-output questions on `'\0'` and string APIs.

# Module 3.2 — Character Arrays & Strings

> Syllabus: [[syllabus-316U06C107#module-map--30-hrs]] M3.2 (CO3, ~3 hrs of M3's 7) | Prereq: [[module-3-arrays]] | Lab: EXP5 per [[lab-ca-and-experiments#6-list-of-experiments--10-items-exp1-8--2-assignments]] | Sources: [[raw-sources/SPM_Syllabus_316U06C107]] ch. 3.2
> Companion: [[c-programming-master-study-guide#31-1d-array-memory-layout]] (contiguous model) · [[formula-sheet-spm#6-strings-char-arrays--0]]

## 1. What Is a String in C?

C has **no string type**. A string is a **`char` array terminated by `'\0'`** (ASCII 0). Every string handler stops at the first `'\0'`.

```
char s[6] = "hello";   // actually 6 bytes: 'h' 'e' 'l' 'l' 'o' '\0'
INDEX:     [0]  [1]  [2]  [3]  [4]  [5]
VALUE:      h    e    l    l    o   \0   ← terminator, NOT counted in strlen
ADDR:    base base+1 ...                base+5
```

**Three declarations — memorize the cost:**

```c
char a[] = "hi";            // size 3 (h,i,\0) — auto-sized, preferred
char b[10] = "hi";           // size 10 (h,i,\0 + 7 garbage/padding) — needs space for \0
char c[3] = {'h','i','\0'}; // identical to a[] but verbose
char *p = "hi";             // p points to TEXT segment literal — READ-ONLY; p[0]='H' crashes
```

**Rules:**
- Array form (`char s[]`) lives in **stack** (mutable); pointer-to-literal (`char *p="hi"`) lives in **text** (read-only).
- `strlen` counts **excluding** `'\0'`; `sizeof` counts **including** `'\0'` and any extra capacity.
- Partial init zero-fills: `char s[5] = "hi";` → `{'h','i','\0','\0','\0'}` — C guarantees rest is `0`.
- **Always allocate +1** for `'\0'`: needing `n` chars → declare `n+1`.

## 2. Reading & Writing Chars and Strings

| Task | Correct pattern | Trap |
|------|----------------|------|
| Read a **char** | `char ch; scanf(" %c",&ch);` (space skips newline) | `scanf("%c")` without space reads leftover `\n` |
| Read a **word** (no spaces) | `char s[20]; scanf("%19s", s);` (no `&`; width = size-1) | Missing width → buffer overflow; `&s` is wrong type |
| Read a **line** (with spaces) | `fgets(s, sizeof s, stdin);` then strip `\n` | `gets()` is **removed** (unsafe) — never use |
| Write | `printf("%s", s);` or `puts(s);` (adds `\n`) | `%s` on non-terminated array is UB |
| Char I/O | `getchar()/putchar()` | These are `int`-returning (EOF = -1) |

**`fgets` newline stripping (exam pattern):**
```c
if (fgets(s, sizeof s, stdin)) {
    s[strcspn(s, "\n")] = '\0'; // replace trailing \n with \0
}
```

## 3. Library String Handlers (inbuilt) — What OST/Quiz Expects You to Know

| Function | Signature | Does | Returns |
|----------|-----------|------|---------|
| `strlen` | `size_t strlen(const char *s)` | length **excluding** `\0` | count |
| `strcpy` | `char *strcpy(char *dst, const char *src)` | copy incl. `\0` | dst |
| `strncpy` | `char *strncpy(dst,src,n)` | copy up to n; may **not** add `\0` if src≥n | dst — must manually add `\0` |
| `strcat` | `char *strcat(char *dst, const char *src)` | append src after dst's `\0` | dst |
| `strncat` | `char *strncat(dst,src,n)` | append up to n chars, always `\0`-terminates | dst |
| `strcmp` | `int strcmp(const char *a, const char *b)` | compare lexicographically (ASCII) | 0 if equal, <0 if a<b, >0 if a>b |
| `strncmp` | `int strncmp(a,b,n)` | compare first n chars | same |

**Never use `==` on strings** — it compares **addresses**, not contents. Use `strcmp(a,b)==0`.

## 4. Implementing Handlers From Scratch (Syllabus Requirement)

Syllabus says "Implementation of string handling operations (from scratch)" — you must be able to write these without the library.

```c
#include <stdio.h>

/* strlen from scratch — count until \0 */
size_t myStrlen(const char *s) {
    size_t n = 0;
    while (s[n] != '\0') n++;
    return n;
}

/* strcpy from scratch — copy incl. \0; caller ensures dst big enough */
char *myStrcpy(char *dst, const char *src) {
    size_t i = 0;
    while ((dst[i] = src[i]) != '\0') i++;
    return dst;
}

/* strcmp from scratch */
int myStrcmp(const char *a, const char *b) {
    while (*a && *a == *b) { a++; b++; }
    return (unsigned char)*a - (unsigned char)*b;
}

/* strcat from scratch */
char *myStrcat(char *dst, const char *src) {
    size_t d = myStrlen(dst);
    size_t i = 0;
    while ((dst[d + i] = src[i]) != '\0') i++;
    return dst;
}

int main(void) {
    char a[20] = "hello";
    char b[20];
    myStrcpy(b, a);
    myStrcat(b, " world");
    printf("%s len=%zu cmp=%d\n", b, myStrlen(b), myStrcmp(b, "hello world"));
    return 0;
}
// Output: hello world len=11 cmp=0
```

**Exam checkers look for:** loop terminating at `'\0'`, casting to `unsigned char` in `strcmp` (plain `char` may be signed), preserving the terminator.

## 5. High-Yield Traps & Quiz Patterns

| Trap | What happens | Fix |
|------|--------------|-----|
| Forget `'\0'` capacity | `char s[5]="hello"` needs 6 → overflow by 1 | Declare `[6]` or `[]` auto-size |
| `char *p="hi"; p[0]='H'` | Segfault (text segment read-only) | Use `char p[]="hi"` to mutate |
| `scanf("%s", s)` without width | Overflow on long input | `"%19s"` for `s[20]` |
| `strcmp(a,b)` checked as `==1` | Wrong — equal is `0`, inequality is `<0` or `>0` (not necessarily 1) | `if (strcmp(a,b)==0)` |
| `strncpy` without terminator | dst may lack `'\0'` when src≥n → later `printf` reads past buffer | `dst[n-1]='\0'` after |
| `strlen` vs `sizeof` | `strlen("hi")==2` but `sizeof("hi")==3` | Know which counts `\0` |

### Predict-the-output drill (quiz-style)

```c
char s[] = "abc";
printf("%zu %zu\n", strlen(s), sizeof(s));
char *p = "abc";
printf("%c %c\n", s[1], p[1]);
s[0]='x'; // ok
// p[0]='x'; // UB — crash on most systems
```
Output: `3 4` then `b b` (sizeof includes `\0`).

## 6. Memory & Performance

- Strings inherit array **O(1) random access** and **O(n) scan** cost — `strlen` is O(n) because it must walk to `\0'`.
- `strcpy/strcat` are **O(n)** and **unsafe** without bounds — prefer `snprintf(dst, sizeof dst, "%s", src)` in production; in exam write the manual loop.

## Cross-References

- Arrays foundation: [[module-3-arrays]] (contiguous + address formulas)
- Pointer view: [[module-4-structures-unions-pointers#3-pointers]] (`char *` vs `char[]`)
- Syntax sheet: [[formula-sheet-spm#6-strings-char-arrays--0]] · Cram: [[c-programming-master-study-guide#12-process-memory-layout]]

*Lab: EXP5 Write a program to demonstrate use of strings and string handling functions — per [[lab-ca-and-experiments]] Week 8.*
