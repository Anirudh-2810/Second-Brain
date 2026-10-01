---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "Module 3.2 — Character Arrays & Strings"
date: "2026-10-02"
description: "SPM M3.2 strings, complete and beginner-first — the '\\0' model, four declaration styles, character/string I/O, strlen/strcpy/strcmp/strcat both as library calls and written from scratch, a dedicated strcpy exam drill, 12 practice questions and a 5-question quick test."
tags: [spm, strings, c-programming, 316U06C107, string-handling, strcpy, strlen, strcmp, strcat, null-terminator, from-scratch, exam-prep, lab]
last_updated: "2026-10-02"
confidence: high
prerequisites: ["Module 3.1 Arrays", "Module 2: loops", "Pointers basics"]
sources:
  - "raw-sources/SPM Lecture/SPM_Module3_2.pptx"
  - "raw-sources/SPM Lecture/Unit No.3 Arrays_Strings.pdf"
  - "raw-sources/SPM Lab/EX5.docx"
  - "raw-sources/SPM_Syllabus_316U06C107.md"
---

## For future agent

**The dedicated strings page for SPM Module 3.2** (part of Module 3's 7 hours, CO3, Bloom's *Apply*). Rewritten 2026-10-02 as the single home for strings: it absorbs the strings half of the former merged page, **the `strcpy` exam drill**, the classroom cut from [[spm-string-functions-char-equality-reverse]], and deltas from the faculty deck `SPM_Module3_2.pptx` (27 slides, AY 2026-27).

**Arrays live in [[module-3-arrays]] — do not duplicate them here.**

**Two source conventions that differ — the exam follows the faculty form.** The faculty deck and handout write from-scratch functions with `int` returns, `char str[]` parameters, and **explicit `dest[i] = '\0';` after the copy loop**. This page presents the **faculty form first** and notes the compact library-style variant after it, because the marked answer is the faculty form. Both are correct; the two-step version is easier to explain and is what the source emphasises.

**Unsafe-C note:** the source teaches `scanf("%s", name)` with no width limit and unbounded `strcpy`/`strcat`. That is recorded faithfully (it is what the lab prescribes) but flagged in §4.5 and §6.4 — modern C requires the width form or `fgets`.

---

# Module 3.2 — Character Arrays & Strings

> **Syllabus 3.2** ([[syllabus-316U06C107]]): *Character Arrays and Strings: Declaring/Init, Reading/Writing chars & strings, operations, implementing string handling from scratch.*
> Lab: **EXP5** per [[spm-lab-exp3-4-5-guides]]. Arrays half: [[module-3-arrays]]. Module map: [[module-3-arrays-strings]]

---

## 0. The Five Sentences That Cover the Whole Topic

1. C has **no string type**. A string is a `char` array ending in `'\0'`.
2. The terminator is **mandatory** — it is how `printf` and `strlen` know where to stop.
3. `strlen` counts characters **without** `'\0'`; `sizeof` counts the whole array **with** it.
4. The syllabus says *implement string handling **from scratch*** — write the loop, do not call the library.
5. Every from-scratch operation shares one skeleton: **start at index 0, loop while the char is not `'\0'`.**

---

## 1. The String Model

### 1.1 What a string actually is

A string is a **`char` array terminated by the null character `'\0'`** (ASCII value 0).

```
   char str[6] = "Hello";

   'H'   'e'   'l'   'l'   'o'   '\0'
   [0]   [1]   [2]   [3]   [4]   [5]
   base  +1    +2    +3    +4    +5

   5 visible characters + 1 hidden terminator = 6 bytes
```

- **The terminator is mandatory.** Every C string must end with it.
- **`"Hello"` is 6 characters, not 5.** The compiler appends the `'\0'` automatically.
- **A char array is NOT automatically a string.** `{'H','i'}` with no `'\0'` is just two characters — printing it with `%s` reads past the array (undefined behaviour).
- **Rule of thumb:** sizing a char array for a string, always reserve **one extra byte**.

### 1.2 Character vs. string — the most basic trap

```c
char ch   = 'A';     /* CHARACTER: single quotes */
char name[] = "ABC"; /* STRING:    double quotes */
```

| | Character | String |
|---|---|---|
| Quotes | `'A'` | `"A"` |
| How many | exactly one | a whole sequence |
| Bytes in memory | 1 | count + 1 (the `'\0'`) |
| Comparison | `a == b` | `strcmp(a, b) == 0` |

`'A'` is one byte. `"A"` is **two** bytes (`'A'` + `'\0'`).

### 1.3 Four ways to declare a string

```c
char str1[6]  = "Hello";              /* 1. literal — compiler adds '\0' */
char str2[]   = "Hello";              /* 2. size inferred -> size = 6    */
char str3[6]  = {'H','e','l','l','o','\0'};  /* 3. char by char        */
char str4[20];                         /* 4. empty buffer, filled later */
```

| Form | Watch out |
|---|---|
| 1. Literal | the compiler counts the characters and appends `'\0'` — the usual choice |
| 2. Size inferred `[]` | always exactly right for that literal; **safest against off-by-one** |
| 3. Char-by-char | you must add `'\0'` yourself — easy to forget, a common bug source |
| 4. Empty buffer | the normal choice when the string will be filled from input |

**Also valid, and important for the pointer module:**

```c
char *p = "hi";    /* points into READ-ONLY text memory */
p[0] = 'H';        /* CRASH — undefined behaviour */
char a[] = "hi";   /* on the stack, writable */
a[0] = 'H';        /* fine */
```

| Form | Lives in | Writable? |
|---|---|---|
| `char a[] = "hi"` | **Stack** | yes |
| `char *p = "hi"` | **Text (read-only)** | **no** |
| `char *p = malloc(n)` | **Heap** | yes |

### 1.4 Reading and writing a character

```c
char ch;
ch = getchar();        /* reads ONE character  — no & needed, it RETURNS  */
scanf("%c", &ch);      /* also reads ONE char  — & required, it WRITES   */
```

- `getchar()` needs no `&` because it **returns** the character.
- `scanf("%c", &ch)` needs `&` like any `scanf` conversion.
- **Both read exactly one char *including* whitespace** — unlike `%d` or `%s`, `%c` does **not** skip leading spaces.

**The newline trap:** after `scanf("%d", &n);` the Enter key you pressed is still sitting in the input buffer. A following `scanf("%c", &ch);` reads that leftover `'\n'` instead of new input. **Fix: `scanf(" %c", &ch);`** — the leading space means "skip whitespace first."

**Writing:**

```c
char ch = 'A';
putchar(ch);            /* writes ONE character */
printf("%c", ch);       /* same thing, more flexible */
putchar('\n');          /* slightly faster than printf("\n") when that's all you need */
```

### 1.5 Reading and writing a string

**Read a single word:**

```c
char name[20];
scanf("%s", name);      /* NOT &name */
```

Two things to know:

1. **No `&`.** An array name *already is* the address of its first element, so `&name` is a type error (`char (*)[20]` where `char *` is expected). Contrast `scanf("%d", &n)` where `n` is a plain `int`, which does need `&`.
2. **`%s` stops at the first whitespace.** Typing `Piyush Sharma` stores only `Piyush`.

**Read a full line:**

```c
char sentence[50];

printf("Enter a sentence: ");
fgets(sentence, sizeof(sentence), stdin);   /* reads the whole line */
printf("You entered: %s", sentence);
```

`fgets(buf, size, stream)` reads until a **newline** or until `size - 1` characters, whichever comes first. It is **always bounded**, which is why it is safe where `scanf("%s")` is not. It keeps the trailing `'\n'`, which is harmless for printing but matters if you later compare or convert the string — strip it with `s[strcspn(s, "\n")] = '\0';`.

**Write:**

```c
char msg[] = "Hi there";
printf("%s", msg);    /* no newline added */
puts(msg);            /* prints AND appends a newline */
```

**Both stop at `'\0'`.** Anything after the terminator is never printed. If a manually built string is missing its `'\0'`, `printf("%s", …)` and `puts()` keep printing garbage until they happen to hit a zero byte.

---

## 2. Library String Functions

```c
#include <string.h>     /* MANDATORY, or the compiler warns/errors */
```

| Function | Signature | Does | Returns |
|---|---|---|---|
| `strlen` | `size_t strlen(const char *s)` | length **excluding** `'\0'` | count |
| `strcpy` | `char *strcpy(char *dst, const char *src)` | copy **including** `'\0'` | `dst` |
| `strncpy` | `char *strncpy(dst, src, n)` | copy up to `n`; may **omit** `'\0'` | `dst` |
| `strcat` | `char *strcat(char *dst, const char *src)` | append `src` after `dst`'s `'\0'` | `dst` |
| `strncat` | `char *strncat(dst, src, n)` | append up to `n`, **always** terminates | `dst` |
| `strcmp` | `int strcmp(const char *a, const char *b)` | compare by character code | `0` equal, `<0` a<b, `>0` a>b |
| `strncmp` | `int strncmp(a, b, n)` | compare first `n` characters | same |

**Argument order:** `strcpy(destination, source)`, `strcat(destination, source)` — copy/append **into** the first one, same order as assignment.

**`strlen` is O(n)** — it scans byte by byte until it finds `'\0'`. It has no shortcut, because C stores no length field. That is exactly why the syllabus asks you to implement it yourself.

### 2.1 All four in one program

```c
#include <stdio.h>
#include <string.h>

int main(void) {
    char str[50] = "Hello";
    printf("Length = %d\n", strlen(str));              /* 5 */

    char s1[50] = "Hello";
    char s2[50];
    strcpy(s2, s1);
    printf("Copied = %s\n", s2);                       /* Hello */

    char a[50] = "apple", b[50] = "apple";
    if (strcmp(a, b) == 0) printf("Strings are equal\n");
    else                   printf("Strings are not equal\n");

    char g[50] = "Hello ", w[50] = "World";
    strcat(g, w);
    printf("Combined = %s\n", g);                      /* Hello World */
    return 0;
}
```

**`strcmp` returns `0` for equal** — counter-intuitive, but that is the "yes, equal" answer. Negative means `a` sorts before `b` (dictionary order), positive means after. **Never test for `== 1`** — a non-zero return is not guaranteed to be exactly 1.

**Never use `==` to compare strings.** `a == b` compares the two *addresses*, not the contents. Two separate arrays holding `"apple"` almost certainly sit at different addresses, so `==` says "not equal" even though they are.

**Plain assignment cannot copy a string either:** `dest = src;` is illegal for arrays in C — you need a loop or `strcpy`.

### 2.2 `strcat` detail

`strcat(dest, src)` **overwrites `dest`'s old `'\0'`** and appends `src` there, then adds a **fresh** `'\0'` after the combined text.

- **`dest` must have room to grow** — large enough for both strings plus `'\0'`.
- **`src` is unchanged** — only `dest` grows.

---

## 3. From Scratch (the syllabus requirement)

> **Syllabus wording:** *"implementing string handling operations (from scratch)"* — process one character at a time with a loop instead of calling `strlen()`/`strcpy()`/`strcmp()`/`strcat()`.

### 3.1 Length

```c
int myStrlen(char str[]) {
    int count = 0;
    while (str[count] != '\0') {
        count++;
    }
    return count;
}
```

`count` is a **counting loop** (Module 2) that stops exactly when it hits `'\0'` — it never needs to know the array's declared size.

Trace for `"HELLO"`: `H`→1, `E`→2, `L`→3, `L`→4, `O`→5, then `str[5] == '\0'` → stop. **Length = 5.**

### 3.2 Copy — see the full drill in §6

```c
void myStrcpy(char dest[], char src[]) {
    int i = 0;
    while (src[i] != '\0') {
        dest[i] = src[i];
        i++;
    }
    dest[i] = '\0';   /* don't forget this! */
}
```

The loop copies the visible characters only. **The `'\0'` is NOT copied by the loop, so it must be added manually after** — otherwise `dest` is not a valid C string.

### 3.3 Concatenate

```c
void myStrcat(char dest[], char src[]) {
    int i = 0, j = 0;
    while (dest[i] != '\0')   /* find end of dest — copies nothing */
        i++;
    while (src[j] != '\0') {  /* copy src onto it */
        dest[i] = src[j];
        i++;
        j++;
    }
    dest[i] = '\0';
}
```

The **first loop copies nothing** — it just walks `i` forward to find where `dest`'s existing text ends, so the second loop knows where to start writing.

Trace, `dest = "Hello "` and `src = "Somaiya"`:

| Stage | `dest` | `i` |
|---|---|---|
| after loop 1 | `H e l l o   _ _ _` | 6 |
| iter 1 | `H e l l o   S _ _` | 7 |
| iter 2 | `H e l l o   S o _ _` | 8 |
| … | … | … |
| after loop 2 | `H e l l o   S o m a i y a _` | 14 |
| final | `H e l l o   S o m a i y a \0` | 14 |

Result: **`"Hello Somaiya"`**.

### 3.4 Compare

```c
int myStrcmp(char s1[], char s2[]) {
    int i = 0;
    while (s1[i] == s2[i]) {
        if (s1[i] == '\0')
            return 0;        /* both ended at the same point — equal */
        i++;
    }
    return s1[i] - s2[i];    /* first mismatch, ASCII difference */
}
```

`s1[i] - s2[i]` uses the characters' codes directly — `'c'`(99) minus `'d'`(100) = −1, confirming "cat" sorts before "dog".

**A compact variant** you may also be asked for:

```c
int myStrcmp(const char *a, const char *b) {
    while (*a && *a == *b) { a++; b++; }          /* skip the common prefix */
    return (unsigned char)*a - (unsigned char)*b;
}
```

The `unsigned char` cast matters because plain `char` may be signed on some systems, so a negative difference can come out with the wrong sign.

### 3.5 Reverse

```c
char str[100];
int length = 0, i;

while (str[length] != '\0') length++;

for (i = length - 1; i >= 0; i--)
    printf("%c", str[i]);
```

For `"HELLO"` (length 5) we print indices `4 3 2 1 0` → `O L L E H` → **OLLEH**.

**Three traps examiners set deliberately:**

| Trap | Wrong code | Result | Correct |
|---|---|---|---|
| Off-by-one start | `for (i = length; ...)` | prints the `'\0'` first — nothing visible | start at `length - 1` |
| Off-by-one end | `for (i = length - 1; i > 0; i--)` | **skips `str[0]`** | condition `i >= 0` |
| Unsigned index | `size_t i` with `i >= 0` | **infinite loop** — unsigned is never negative | use signed `int i` |

### 3.6 Palindrome — combines everything

Not every string problem has a library function.

```c
int myPalindrome(char str[]) {
    int len = myStrlen(str);
    for (int i = 0; i < len / 2; i++) {
        if (str[i] != str[len - 1 - i])
            return 0;
    }
    return 1;
}
```

A palindrome reads the same backwards, so compare the **first half** against the **last half** in mirror positions: `str[i]` pairs with `str[len - 1 - i]`. Loop only `i < len / 2` — if the first half matches, the second half must too.

Trace `"level"` (len 5): `i=0` `l` vs `l` ✓ · `i=1` `e` vs `e` ✓ · `i=2` fails `2 < 2` → stop → **palindrome**.

### 3.7 Vowel count

```c
int i = 0, count = 0;
while (str[i] != '\0') {
    if (str[i] == 'a' || str[i] == 'e' || str[i] == 'i' ||
        str[i] == 'o' || str[i] == 'u')
        count++;
    i++;
}
```

`"education"` → `e, u, a, i, o` → **5**. This version tests only **lowercase**; input `Education` reports 4. Handling both cases means testing `'a' || 'A' || …` or calling `tolower()` from `<ctype.h>` — a very common viva question.

---

## 4. Comparison Tables

### 4.1 Array vs. string

| | Array | String |
|---|---|---|
| Holds | any same data type | characters only |
| Example | `int marks[5]` | `char name[20]` |
| Terminator | not required | **must** end with `'\0'` when used as a C string |
| Access | by index | by index |

### 4.2 Bounded vs. unbounded

| Function | Copies/appends | Always ends with `'\0'`? | Bounded? |
|---|---|---|---|
| `strcpy` | everything | **yes** | **no** |
| `strncpy` | up to `n` | **only if `strlen(src) < n`** | yes |
| `strcat` | appends everything | **yes** | **no** |
| `strncat` | up to `n` appended | **yes** | yes |

**The pattern:** `strcpy`/`strcat` are unbounded; the `n` versions are bounded. That is why production C prefers `snprintf(dst, sizeof dst, "%s", src)`.

### 4.3 The five string pitfalls (deck slide 24)

| # | Pitfall | Detail |
|---|---|---|
| 1 | **Forgetting the null terminator** | a manually built array without `'\0'` is not a valid string — `printf`/`strlen` read past it |
| 2 | **Buffer too small** | `strcpy`/`strcat` do **not** check the destination size — overflow corrupts nearby memory (classic security bug) |
| 3 | **Comparing strings with `==`** | compares addresses, not content — always use `strcmp` |
| 4 | **`scanf("%s", …)` stops at spaces** | use `fgets` when input may contain spaces |
| 5 | **`sizeof` vs `strlen` confusion** | `sizeof(arr)` is total capacity; `strlen(arr)` is the text length before `'\0'` — they are rarely equal |

### 4.4 Master trap table (whole module)

| Trap | What happens | Fix |
|---|---|---|
| Forget `'\0'` capacity | `char s[5] = "hello"` needs 6 → overflow by 1 | declare `[6]`, or use `[]` |
| `char *p = "hi"; p[0]='H'` | segfault (text segment read-only) | use `char p[] = "hi"` |
| `scanf("%s", s)` with no width | overflow on long input | `"%19s"` for `s[20]`, or `fgets` |
| `scanf("%s", &s)` | type error — array name is already an address | drop the `&` |
| `scanf("%c")` after a numeric read | reads the leftover `'\n'` | `scanf(" %c", &ch)` |
| `==` on strings | compares addresses, not contents | `strcmp(a,b) == 0` |
| `strcmp(...) == 1` for equality | wrong — equal is `0` | test `== 0` |
| `strncpy` with no manual `'\0'` | later `printf` reads past the buffer | `dst[n-1] = '\0';` |
| `strcpy(dest, src)` reversed | clobbers your source | always `(dest, src)` |
| `dest = src;` | illegal — arrays cannot be assigned | loop or `strcpy` |
| `gets()` | **removed from C** (unsafe) | `fgets` |
| reverse: start at `n` | prints the `'\0'` | start at `n - 1` |
| reverse: `i > 0` | skips `str[0]` | condition `i >= 0` |
| reverse: `size_t i` | infinite loop (unsigned never negative) | use signed `int i` |
| storing `getchar()` in a `char` | loses the ability to detect `EOF` | use an `int` |

### 4.5 Safe-coding note (agent annotation, not from the source)

The lab and handout prescribe `scanf("%s", name)` with no width limit, and unbounded `strcpy`/`strcat`. **In modern C both are unsafe:**

```c
char s[20];
scanf("%19s", s);                        /* width = size - 1 */
fgets(s, sizeof s, stdin);               /* or better: bounded by nature */
strncpy(d, s, sizeof d - 1);
d[sizeof d - 1] = '\0';
```

This is the same class of bug as Heartbleed. The simple form is accepted in exams and in the lab write-up; production code must not use it.

---

## 5. Practice Questions (from the faculty deck)

**Q1 — strings, declaration, character I/O**
1. How many bytes does `char city[] = "Mumbai";` actually occupy? Why?
2. Write a program that reads one character and prints whether it is a vowel or consonant.
3. What is wrong with `char name[7] = "Somaiya";` for storing the word "Somaiya"?

<details><summary>Answers</summary>

1. **7 bytes** — 6 visible letters + the `'\0'`.
2. Read with `getchar()`, then test against `"aeiouAEIOU"` (test both cases, or `tolower()` first).
3. **Nothing is wrong** — "Somaiya" is exactly 7 letters, so `name[7]` has room for 7 letters but **no room for the `'\0'`**. Initializing with the literal writes one byte past the array. It must be `char name[8]`.
</details>

**Q2 — reading & writing strings**
1. Rewrite a greet program using `fgets` instead of `scanf("%s", …)` so it accepts a full name with spaces.
2. What does `puts()` do differently from `printf("%s", str);`?
3. Why does an array name in `scanf("%s", name);` **not** need an `&`?

<details><summary>Answers</summary>

1. `fgets(name, sizeof name, stdin);` then strip the newline: `name[strcspn(name, "\n")] = '\0';`
2. `puts()` appends a newline automatically; `printf("%s", …)` does not.
3. An array name **already evaluates to** the address of its first element, so it is already a pointer. Only scalar variables like `int n` need `&`.
</details>

**Q3 — `strlen` and `strcpy`, library & from scratch**
1. What does `myStrlen` return when called on an empty string `""`?
2. In the from-scratch `myStrcpy`, what bug occurs if `dest[i] = '\0';` is removed?
3. Rewrite `myStrlen` using a `for` loop instead of `while`.

<details><summary>Answers</summary>

1. **0** — `str[0]` is already `'\0'`, so the `while` condition fails on the first check and the loop never runs.
2. `dest` never becomes a valid C string. Later `printf("%s", dest)` or `strlen(dest)` reads past the end until it happens to hit a zero byte — garbage output or a crash.
3. `int n = 0; for (; str[n] != '\0'; n++); return n;`
</details>

**Q4 — `strcat` and `strcmp`, library & from scratch**
1. Trace `myStrcat` for `dest = "Go "` and `src = "Team"`, showing `i` and `j` at each stage.
2. What does `myStrcmp` return when comparing `"apple"` with `"app"`?
3. Write a program that reads two strings and prints whether they are equal, using `strcmp`.

<details><summary>Answers</summary>

1. After loop 1, `i = 3` (`"Go "` is 3 chars). Then `i` climbs 3→4→5→6→7 as `T`,`e`,`a`,`m` are written at `dest[3..6]`, with `j` climbing 0→1→2→3→4 in step. Final `dest = "Go Team\0"` at `i = 7`.
2. **Positive** (specifically **1**). The loop matches `a`,`p`,`p` then finds `s1[3]='l'` vs `s2[3]='\0'` and exits; `'l'`(108) − `'\0'`(0) = **108** in plain ASCII terms — but note the deck's version returns the raw difference, so treat "positive" as the safe exam answer, not a specific magnitude.
3. `if (strcmp(s1, s2) == 0) printf("Equal\n"); else printf("Different\n");`
</details>

---

## 6. The `strcpy` Exam Drill

`strcpy` is the highest-frequency string function in SPM OST/quiz papers.

### 6.1 What it does

```c
char *strcpy(char *destination, const char *source);
```

Copies **every character of `source`, including the terminating `'\0'`**, into `destination`, and returns `destination`.

```
   BEFORE                                 AFTER
   source      =  H  e  l  l  o  \0      (6 bytes)
   destination =  ?  ?  ?  ?  ?  ?      (uninitialized)

   destination[0] = 'H'    destination[1] = 'e'
   destination[2] = 'l'    destination[3] = 'l'
   destination[4] = 'o'    destination[5] = '\0'   <-- terminator copied too

   AFTER
   destination =  H  e  l  l  o  \0      (identical to source)
```

**Total bytes written = `strlen(source) + 1`.**

### 6.2 Three ways to write it

| Version | Code | Note |
|---|---|---|
| **Library** | `strcpy(dst, src);` | the real thing |
| **From scratch — faculty form** | loop, then `dst[i] = '\0';` | the source's emphasis; easiest to explain |
| **From scratch — one-liner** | `while ((dst[i] = src[i]) != '\0') i++;` | copies the `'\0'` inside the loop |

```c
/* Faculty form (write this if asked) */
void myStrcpy(char dest[], char src[]) {
    int i = 0;
    while (src[i] != '\0') { dest[i] = src[i]; i++; }
    dest[i] = '\0';
}

/* Compact form (equally accepted) */
char *myStrcpy2(char *dest, const char *src) {
    int i = 0;
    while ((dest[i] = src[i]) != '\0') i++;
    return dest;
}
```

### 6.3 Examiner checklist

- [x] loop terminates at **`'\0'`**
- [x] the **`'\0'` is copied or re-added** (so `dst` becomes a valid C string)
- [x] function **returns `dst`** (enables chaining) — if written `void`, this box does not apply
- [x] index **starts at 0**, increments by 1
- [x] `source` is `const char *` or `char src[]` — it must not be modified

### 6.4 Traps

| Trap | Code | What happens | Fix |
|---|---|---|---|
| **Destination too small** | `char d[3]; strcpy(d, "hiya");` | writes 5 bytes into 3 → memory corruption | `char d[strlen(src)+1];` or bigger |
| **Source not terminated** | `char s[5] = {'h','i'}; strcpy(d, s);` | runs past `s` until it finds a stray zero | always `'\0'`-terminate |
| **Copying a literal** | `char *p = "hi"; strcpy(p, "bye");` | **segfault** — text segment is read-only | `char p[] = "hi";` |
| **Overlapping regions** | `strcpy(s + 2, s);` | undefined behaviour | use `memmove` |
| **Argument order reversed** | `strcpy(src, dst);` | clobbers your source | always `(dest, src)` |
| **Assuming assignment copies** | `dest = src;` | illegal for arrays in C | loop or `strcpy` |

### 6.5 `strncpy` — the contrast the syllabus loves

```c
strncpy(dst, "hello world", 5);   /* dst = "hello" but NO '\0' */
printf("%s", dst);                 /* reads past dst — garbage or crash */
```

**The fix — always terminate manually:**

```c
strncpy(dst, "hello world", 5);
dst[4] = '\0';                     /* i.e. dst[sizeof(dst) - 1] = '\0'; */
```

### 6.6 Predict-output drills

**D1 — sizes.** `char s[] = "abc"; printf("%zu %zu\n", strlen(s), sizeof(s));`
→ `3 4` — `strlen` excludes `'\0'`; `sizeof` includes it.

**D2 — write to literal vs. array.**
```c
char s[] = "abc";  char *p = "abc";
printf("%c %c\n", s[1], p[1]);
s[0] = 'x';          /* OK   */
/* p[0] = 'x'; */     /* UB — segfault */
```
→ `b b`, then `s` becomes `"xbc"`. Uncommenting `p[0]='x'` is undefined behaviour.

**D3 — `strcmp` return value.** `char a[]="apple", b[]="apple"; printf("%d\n", strcmp(a,b) == 1);`
→ `0` — equal strings return `0`, and `0 == 1` is false. Testing `== 1` for equality is a **wrong** idiom.

**D4 — the overflow.** `char d[4]; strcpy(d, "abcde"); printf("%s\n", d);`
→ **Undefined behaviour.** `"abcde"` needs 6 bytes; `d` has 4. It may print `abcde`, print garbage, or crash — none guaranteed. (`char d[6]` is correct.)

**D5 — copy into a literal.** `char *p = "hi"; strcpy(p, "bye");`
→ **Crash.** `p` points into read-only text. Fix: `char p[] = "hi";`

**D6 — partial concatenation (EX5 tracing question).**
```c
char a[20] = "Data";  char b[] = "Structures";  strcat(a, b);
```
→ `a` becomes **`"DataStructures"`** (14 chars + `'\0'` = 15 bytes, fits in 20). `a` needs the extra space because `strcat` *appends* to what `a` already holds — a buffer sized only for `"Data"` (5 bytes) would overflow.

---

## 7. Quick Test — Topic 3.2 (5 questions)

| # | Type | Question | Answer |
|---|---|---|---|
| Q1 | MCQ | The character that marks the end of a C string is: (a) `'\n'` (b) `'\0'` (c) `EOF` (d) `' '` | **(b) `'\0'`** |
| Q2 | Code trace | `char s[] = "Hi";` — value of `strlen(s)`? of `sizeof(s)`? | **2** and **3** |
| Q3 | Short answer | Why should you never compare two strings using `==` in C? | It compares **addresses**, not content — two equal strings in different arrays have different addresses. Use `strcmp` |
| Q4 | Short answer | Why can `strcpy` cause a buffer overflow? | It performs **no bounds checking** — it copies `strlen(src)+1` bytes regardless of the destination's size, overrunning it if it is smaller |
| Q5 | True/False | `scanf("%s", name);` requires an `&` before `name`, just like `scanf("%d", &n);` | **False** — an array name already *is* its address |

---

## 8. Formula & Syntax Quick Reference

| Quantity | Pattern | Notes |
|---|---|---|
| String bytes | chars + 1 | the `+1` is the `'\0'` |
| Length | `strlen(s)` | excludes `'\0'`, O(n) |
| Array size of a string | `sizeof(s)` | includes `'\0'` + spare capacity |
| `strcmp` equal | `== 0` | **not** `== 1` |
| Copy (faculty form) | loop, then `dst[i]='\0';` | the line examiners look for |
| Copy (one-liner) | `while ((d[i]=s[i]) != '\0') i++;` | copies terminator in-loop |
| Length from scratch | `while (s[n] != '\0') n++;` | |
| Compare from scratch | `while (a[i]==b[i]) { if (a[i]=='\0') return 0; i++; }` | then return the difference |
| Concat from scratch | walk `i` to end of dst, copy src, terminate | |
| Read a char | `scanf(" %c", &ch);` or `getchar()` | leading space skips newline |
| Read a word | `scanf("%19s", s);` | width = size − 1, **no** `&` |
| Read a line | `fgets(s, sizeof s, stdin);` | `gets()` is removed |
| Write a string | `printf("%s", s);` or `puts(s);` | `puts` adds `\n` |
| Strip a newline | `s[strcspn(s, "\n")] = '\0';` | after `fgets` |

---

## 9. Practice Program List

| # | Program | Main concept |
|---|---|---|
| 1 | Read and display a string | character array |
| 2 | Find string length from scratch | `'\0'` |
| 3 | Copy string from scratch | char-by-char copying |
| 4 | Compare strings from scratch | char comparison |
| 5 | Concatenate strings from scratch | string manipulation |
| 6 | Reverse a string | array indexing |
| 7 | Count vowels and consonants | character processing |
| 8 | Palindrome check | `strlen` + mirror indexing |
| 9 | Word count in a sentence | read full line with `fgets` |
| 10 | Count occurrences of a character | loop + counter |
| 11 | Lowercase → uppercase without a library | subtract 32 from `'a'`–`'z'` |
| 12 | Anagram check | sort copies, or count character frequencies |
| 13 | Remove all spaces | in-place compaction with two indices |

---

## Cross-References

- **Arrays half of the module:** [[module-3-arrays]] — the char array is a 1D array; read that first if indexing is shaky
- **Module map / routing:** [[module-3-arrays-strings]]
- **Classroom cut:** [[spm-string-functions-char-equality-reverse]] — the shorter lecture version of this page
- **Syllabus:** [[syllabus-316U06C107]] · [[assessment-guide-ese-ost-quiz]] · [[formula-sheet-spm]]
- **Lab:** [[spm-lab-exp3-4-5-guides]] (EXP5 — Strings) · [[lab-ca-and-experiments]]
- **Loops this depends on:** [[module-2-program-control-functions]] (counting loops, flags)
- **Pointers view:** [[module-4-structures-unions-pointers]] (`char *` vs `char[]`, array decay)
- **Cram:** [[c-programming-master-study-guide]]

*Sources ingested 2026-10-02: `SPM_Module3_2.pptx` (27 slides), `Unit No.3 Arrays_Strings.pdf`, `SPM Lab/EX5.docx`.*
