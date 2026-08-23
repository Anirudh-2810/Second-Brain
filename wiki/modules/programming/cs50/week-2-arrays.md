---
module: "programming"
course: "CS50x — Introduction to Computer Science"
week: 2
topic: "Compiling Pipeline, Debugging, Arrays, Strings & Command-Line Arguments"
tags: [programming, computer-science, cs50, harvard, c, compilers, arrays, strings, memory, debugging, command-line, cryptography]
last_updated: "2026-08-11"
---

# Week 2 — Arrays

> **Goal of the week:** understand *everything that happens between source code and execution*, learn systematic debugging, and meet the array — a fixed, contiguous list of values — plus the fact that **a string is just an array of chars**.
> **PSet 2:** *Readability* (Coleman–Liau index), *Caesar* & *Substitution* (ciphers → array of letters, `%` arithmetic).

---

## 1. The Compile Pipeline — What Actually Happens

Typing `make hello` or `clang hello.c -o hello` runs **four stages**:

```mermaid
flowchart LR
    A["#include <stdio.h> / <cs50.h>"] --> B[1. PREPROCESS<br/>copies library code in]
    B --> C[2. COMPILE<br/>C source → assembly]
    C --> D[3. ASSEMBLE<br/>assembly → object/machine code (.o)]
    D --> E[4. LINK<br/>combine .o files into one executable]
```

1. **Preprocessing**: directives starting with `#` are resolved — `#include <stdio.h>` literally pastes in that file.
2. **Compiling**: turns C into low-level **assembly**.
3. **Assembling**: turns assembly into **machine code** (the 0/1 the CPU runs).
4. **Linking**: joins your object file with library object files into the final executable.

> "Machine code" from Week 1 is *built* here, not typed by you — linking two files (`clang hello.c helper.c`) is how multi-file projects scale.

---

## 2. Debugging — A Process, Not a Panic

| Technique | How | When |
|---|---|---|
| `printf` ("debugging by printing") | print variable values at suspect lines | always, fast, first |
| `debug50` (CS50 tool) | set a **breakpoint** by clicking the gutter; step line-by-line while watching variables | when you need to *watch* state change |
| Rubber-duck / read-back | explain the code out loud | confusion on a single condition |
| `check50` | automated unit tests of your PSet | verifying correctness mechanically |

- **The process that wins:** form a hypothesis (the exact *line* where output diverges) → inspect → change one thing → re-run → repeat. One change at a time!
- **Common C bugs to pre-declare a mental watch-list for:**
  - forgetting types in `printf` format codes,
  - off-by-one indexes (`< n` vs `<= n`),
  - uninitialized variables holding "garbage",
  - integer overflow ($2^{31}-1 + 1$ wraps).

---

## 3. Memory & RAM (the mental model for everything that follows)

- Programs + data live in **RAM** while running; storage (hard drive/SSD) is for persistence.
- RAM is addressable **byte-by-byte**; each byte has an address; your code asks for chunks.
- CS50's favorite picture — memory as a **grid of boxes**, variables occupying adjacent boxes.

```
int scores[3];        → rise in adjacent 4-byte boxes
```

---

## 4. Arrays — Fixed-Size Contiguous Lists

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int scores[3];
    for (int i = 0; i < 3; i++)
    {
        scores[i] = get_int("Score: ");
    }
    double avg = (scores[0] + scores[1] + scores[2]) / 3.0;
    printf("Average: %.1f\n", avg);
}
```

**Rules:**
- **0-indexed**: `scores[0]` is first; `scores[n-1]` last. `scores[3]` = out of bounds (garbage or crash).
- **Fixed size forever** once declared — arrays *cannot* grow in C (growable lists come in Week 5).
- **Homogeneous**: all elements the **same type** (all `int`, all `char`, …).
- Declare all at once: `int scores[] = {72, 80, 95};` (compiler counts for you).
- Access is $O(1)$ by index — this is *why* arrays feel instant.

**2-D arrays** (grids/matrices, for Mario-like shapes later):
```c
int table[rows][cols];      // table[r][c]
```

---

## 5. Strings = Arrays of Chars (the big reveal)

There is **no `string` type in C** — CS50's `string` is an alias for `char *` (a pointer to a char — Week 4's focus). A string is literally **an array of `char`s ending in `\0`** (the NUL terminator / sentinel).

```
string s = "HI!";
memory:  | 'H' | 'I' | '!' | '\0' |
indexes:    0     1     2      3
```

- The **`\0` (NUL) sentinel** tells functions where the string ends — no length is stored, so reading past it means reading someone else's memory.
- Print one char: `s[0]`, `s[1]`, …
- Iterate every char:
```c
for (int i = 0; s[i] != '\0'; i++)
{
    printf("%c\n", s[i]);
}
```
- **`string.h`** gives you the workhorses: `strlen(s)` (length — loops until `\0`), `strcmp(a, b)` (0 if equal — strings can't be compared with `==`), `strcpy(dest, src)`, `strcat`.
- **ASCII recap (Week 0)**: `'A' == 65`; add `1` to a char to advance it → Caesar cipher: `cipher[i] = (plain[i] - 'A' + k) % 26 + 'A';` — the `% 26` wraps Z→A.

---

## 6. Command-Line Arguments — Letting Users Configure Your Program

```c
#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    for (int i = 0; i < argc; i++)
    {
        printf("%s\n", argv[i]);
    }
}
```

```
$ ./argv hello world how are you
./argv
hello
world
how
are
you
```

- `argc` (argument count) = number of words typed (including the program name).
- `argv` (argument vector) = the array of strings.
- Guards: check `argc` before touching `argv[1]` — *validate your input* (the habit that later becomes security hygiene). This is the seed of PSet 2's requirement to validate cipher keys (`isdigit`, `isalpha` from `ctype.h`).

---

## 7. Cryptography — The Case Study Week (arrays + modulo in the wild)

- **Plaintext + key → cipher → algorithm → plaintext again.**
- **Caesar cipher:** shift every letter by $k$, wrap with modulo: $c = (p + k) \bmod 26$. Key stays constant.
- **Substitution cipher:** a 26-letter *mapping alphabet* replaces each letter (key is a permutation, not a shift). Each index `plaintext[i] - 'a'` chooses the replacement char.
- Points the course makes with the PSets:
  1. Strings are arrays; arrays + modulo are enough for real cryptography.
  2. **Validate keys** — a Caesar key must be an integer, substitution keys must be 26 unique letters. The lesson generalises: *validate before you trust input.*

---

## 8. Vocabulary to Master

- preprocess · compile · assemble · link · format codes (`%i %s %f %c`) · debugger / breakpoint · RAM · array · index · NUL `\0` · string-as-array · argc/argv · cryptography · cipher · modulo wrap

## 9. Cross-Links

- [[cs50/week-1-c]] — the language this week deepens (types, loops, `%`).
- [[cs50/week-3-algorithms]] — binary search returns *and* the string-compare `strcmp` becomes search.
- [[cs50/week-4-memory]] — `string` = `char *` is un-hidden: addresses & pointers.
- [[cs50/week-5-data-structures]] — why fixed arrays force growable lists.
- [[cs50/problem-sets]] — PSet 2 requirements and the validation mindset.