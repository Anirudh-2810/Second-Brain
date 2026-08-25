---
course_code: "SPM"
course_name: "Structured Programming Methodology (C)"
unit: "Master Syntax Sheet (Formula-Sheet Equivalent)"
tags: [spm, c-programming, syntax, cheat-sheet, exam-prep]
last_updated: "2026-08-25"
confidence: "high"
---

## For future agent
SPM's formula-sheet equivalent: every C syntax pattern from modules 1–4 on one page (data types, operators, control flow, arrays/strings, functions/pointers). Pairs with [[c-programming-master-study-guide]] for depth and the module pages for topic detail. In a syntax exam, this page + practice == full marks.

# SPM — Master Syntax Sheet

## 1. Program Skeleton

```c
#include <stdio.h>              // preprocessor: standard I/O

int main(void) {                // entry point — exactly one per program
    printf("Hello\n");          // \n = newline escape
    return 0;                   // 0 = success to the OS
}
```

## 2. Data Types & Format Specifiers

| Type | Size (typical) | Range | Format |
|------|---------------|-------|--------|
| `int` | 4 B | ±2.1×10⁹ | `%d` |
| `float` | 4 B | ~7 digits precision | `%f` |
| `double` | 8 B | ~15 digits | `%lf` |
| `char` | 1 B | −128..127 | `%c` |
| `long long` | 8 B | ±9.2×10¹⁸ | `%lld` |
| `unsigned int` | 4 B | 0..4.29×10⁹ | `%u` |

- Escape sequences: `\n` newline · `\t` tab · `\\` backslash · `\"` quote · `\0` string terminator
- Constants: `const float PI = 3.14f;` or `#define PI 3.14`

## 3. Operators (precedence: high → low)

1. `() [] .` · 2. `! ~ ++ -- (cast) * & sizeof` (unary) · 3. `* / %` · 4. `+ -` · 5. `<< >>` · 6. `< <= > >=` · 7. `== !=` · 8. `&` · 9. `^` · 10. `|` · 11. `&&` · 12. `||` · 13. `?:` · 14. `= += -= *= /=` · 15. `,`

**Traps**: `=` is assignment, `==` is comparison · integer division truncates: `5/2 == 2` but `5.0/2 == 2.5` · `%` needs integers · `++i` (increment, then use) vs `i++` (use, then increment).

## 4. Control Flow

```c
if (marks >= 40) printf("pass"); else printf("fail");

switch (choice) {                    // only int/char
    case 1: printf("one"); break;    // break prevents fall-through
    case 2: printf("two"); break;
    default: printf("invalid");
}

for (int i = 0; i < n; i++) { /* body */ }

while (condition) { /* body */ }     // test first

do { /* body */ } while (condition); // runs at least once

// break = exit loop; continue = skip to next iteration
```

**Loop choice**: known count → `for`; test-first unknown → `while`; run-first → `do-while` (menu programs).

## 5. Arrays

```c
int a[5] = {10, 20, 30, 40, 50};     // indices 0..4 — a[5] is OUT OF BOUNDS
int m[2][3] = {{1,2,3},{4,5,6}};     // 2D: row-major
for (int i = 0; i < 5; i++) printf("%d ", a[i]);
```

- Array name = address of first element (`a == &a[0]`)
- Pass to function as `int arr[]` — arrays are ALWAYS pass-by-reference (address)
- No bounds checking in C — out-of-range writes corrupt memory silently

## 6. Strings (char arrays + '\0')

```c
char name[20] = "Anirudh";
scanf("%19s", name);                 // %s needs no &; width prevents overflow
printf("%s", name);

strlen(name)                         // length (excludes '\0')
strcpy(dst, src)                     // copy
strcat(a, b)                         // append b to a
strcmp(a, b)                         // 0 if equal, <0 / >0 otherwise — never use == on strings
```

**String = char array ending in `\0`** — every function above relies on that terminator.

## 7. Functions (Module 4 core)

```c
int add(int a, int b);               // 1. prototype (declaration)

int main(void) {
    int s = add(3, 4);               // 3. call
}
int add(int a, int b) {              // 2. definition
    return a + b;
}
```

| Concept | Meaning |
|---------|---------|
| Call by value | Copies arguments — changes inside don't affect caller (default) |
| Call by reference | Pass addresses (`&x`) + pointer params — changes DO affect caller |
| Recursion | Function calling itself — MUST have a base case |

```c
int fact(int n) { return (n <= 1) ? 1 : n * fact(n - 1); }   // recursion + ternary
void swap(int *a, int *b) { int t = *a; *a = *b; *b = t; }   // call by reference
swap(&x, &y);                                                // caller passes addresses
```

## 8. Pointers (minimum for SPM)

```c
int x = 5;
int *p = &x;          // p stores the ADDRESS of x
printf("%d", *p);     // *p = dereference = 5
*p = 7;               // changes x itself
```

`&` = "address of" · `*` = "value at address". Relationship: `*p == x`, `p == &x`.

## 9. Common Exam Program Patterns

| Pattern | Skeleton idea |
|---------|--------------|
| Largest in array | `max = a[0]; loop: if (a[i] > max) max = a[i];` |
| Reverse array | Swap `a[i]` with `a[n-1-i]` for i < n/2 |
| Prime check | Loop `i = 2..sqrt(n)`; flag if `n % i == 0` |
| Fibonacci | `t3 = t1 + t2; t1 = t2; t2 = t3;` |
| Factorial (recursion) | `n <= 1 ? 1 : n * fact(n-1)` |
| Palindrome string | Compare `s[i]` vs `s[len-1-i]` for half the length |
| Count vowels | `switch(s[i])` on aeiouAEIOU, or strchr |

## 10. Common Errors (the marking scheme hunts these)

| Error | Fix |
|-------|-----|
| Missing `;` / mismatched braces | Compile first, read the line number |
| `scanf("%d", x)` missing `&` | `scanf("%d", &x)` — arrays/strings exempt |
| `=` in condition | `if (x = 5)` always true — use `==` |
| Array index from 1 | Arrays start at 0 |
| String compare with `==` | Use `strcmp(...) == 0` |
| Un-terminated string | Char array needs space for `'\0'` |
| No base case in recursion | Stack overflow (infinite descent) |

## Exam-Day Checklist

1. Every `printf`/`scanf` format matches the variable type
2. `&` present in scanf (except strings/arrays)
3. Loops: check off-by-one (`i < n` vs `i <= n`)
4. Function: prototype before main, definition after
5. Trace ONE example by hand before writing the final answer

## Related

[[module-1-spm-c-basics]] · [[module-2-program-control-functions]] · [[module-3-arrays]] · [[module-4-user-defined-functions]] · [[c-programming-master-study-guide]] · [[formula-sheet-am]] (the math sibling)