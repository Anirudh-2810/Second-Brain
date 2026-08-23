---
module: "programming"
course: "CS50x — Introduction to Computer Science"
week: 1
topic: "C — Compilation, Data Types, Variables, Functions, Conditionals, Loops"
tags: [programming, computer-science, cs50, harvard, c, compilation, variables, data-types, functions, conditionals, loops, operators, cs50-library]
last_updated: "2026-08-11"
---

# Week 1 — C

> **Goal of the week:** write your first compiled text-based programs in **C**, the language that sits close to the machine. Learn types, variables, functions, conditionals, loops, and the CS50 library that smooths input.
> **PSet 1:** *Hello* (warm-up), *Mario* (loops & shaping output), *Cash* (greedy algorithms), *Credit* (Luhn's algorithm / string math).

---

## 1. From Scratch to C — and What "Compiling" Means

- Last week's Scratch blocks look like a language; **C looks like text**. But a machine only understands **binary**. Something must translate your text into binary → the **compiler**.
- **Source code** (`.c`, human-readable) → **compiler** → **machine code** (`.out`/executable, binary).
- Compile & run inside CS50.dev:

```bash
clang hello.c -o hello        # actually compiles (clang = C language)
./hello                       # runs the machine code
```

- Shortcut (Course Reality): `make hello` = same thing, less typing, because CS50.dev ships a **Makefile**.
- Errors you'll meet: compiler errors (syntax), linker errors (unresolved function), runtime errors. Crash course in error-handling arrives properly in [[cs50/week-2-arrays]].

### A first program — "Hello, world"

```c
#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```

| Piece | Meaning |
|---|---|
| `#include <stdio.h>` | "standard input/output" library; gives you `printf` |
| `int main(void)` | program **entry point**; runs when the app starts; `int` = returns an integer (0 = OK) |
| `printf("...")` | prints text to the console |
| `\n` | **newline** escape — moves to a fresh line |
| `;` | statement terminator |

> **Compare with Scratch:** every Scratch block maps to a line of C. `when green flag clicked` → `main(void)`. `say hello` → `printf`.

---

## 2. The CS50 Library (variables & input without the pain of `scanf`)

```c
#include <cs50.h>
```

| Function | Returns | Purpose | C-idiom it wraps |
|---|---|---|---|
| `get_string("prompt")` | `string` | text input | `scanf` |
| `get_int("prompt")` | `int` | integer input | `scanf("%d", &n)` |
| `get_char("prompt")` | `char` | single character | `scanf("%c")` |
| `get_float(...)` | `float` | decimal input | `scanf("%f")` |
| `get_double(...)` | `double` | double-precision decimal | `scanf("%lf")` |
| `get_long(...)` | `long` | bigger integer | `scanf("%li")` |

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string answer = get_string("What's your name? ");
    printf("hello, %s\n", answer);
}
```

- `%s`, `%i`, `%f`, `%c` are **format codes** (placeholders) filled in left-to-right by the arguments.
- The library *insists* on a prompt and refuses bad input → new learners safely practice **input**, which C's raw `scanf` makes easy to get wrong (see Week 4 for why `scanf` alone is dangerous).

---

## 3. Data Types & Sizes (How Much Memory Does a Variable Take?)

| Type | Typical size (CS50/64-bit) | Values |
|---|---|---|
| `bool` *(cs50.h)* | 1 byte | `true` / `false` |
| `char` | 1 byte | −128…127 (or 0…255) |
| `int` | 4 bytes | ≈ −2³¹…2³¹−1 |
| `long` | 8 bytes | ≈ −2⁶³…2⁶³−1 |
| `float` | 4 bytes | ~7 significant digits |
| `double` | 8 bytes | ~15 significant digits |
| `string` *(cs50.h)* | address of a `char[]` | any text (pointer type — details in Week 4) |

- **Variables create boxes in memory**: `int counter = 0;` reserves a 4-byte box labeled `counter`, writes `0` into it.
- **Types cost memory; choose the smallest adequate one** — floats vs doubles matter when numbers get big/precise.

### Operators

| Kind | Operators | Notes |
|---|---|---|
| Arithmetic | `+ - * / %` | `%` = **modulo** (remainder). `17 % 5 == 2` |
| Assignment | `= += -= *= /= %=` | `counter += 1` ≡ `counter = counter + 1` |
| Increment | `counter++` / `counter--` | shorthand up/down by 1 |
| Comparison | `== != < <= > >=` | `==` is *equality*, not assignment |
| Logical | `&&` (and), `||` (or), `!` (not) | build compound booleans |

**Integer division truncates:** `1 / 3 == 0` (both ints → int result). Fix by casting: `(float) 1 / 3`. Also `1 / 10.0` works because one operand is a `float`. Pure floating-point math can be imprecise (e.g. `0.1 + 0.2 != 0.3`), so **never compare floats for exact equality** — compare with a tolerance.

---

## 4. Conditions & Booleans

### if / else if / else
```c
if (x < y)
{
    printf("x is less than y\n");
}
else if (x > y)
{
    printf("x is greater than y\n");
}
else
{
    printf("x is equal to y\n");
}
```

### switch (a cleaner chain for one variable)
```c
switch (x)
{
    case 1:  printf("One\n"); break;
    case 2:  printf("Two\n"); break;
    default: printf("Other\n"); break;
}
```
- `break` exits the switch (else "fall-through" runs the next case's body).
- `default` = the mandatory catch-all (echoes the Video-1 fundamentals note).

### Ternary — inline if
```c
int y = (x < 3) ? 5 : 6;
```

---

## 5. Loops

### while — check *then* run
```c
int i = 0;
while (i < 3)
{
    printf("meow\n");
    i++;
}
```

### do-while — run *then* check (at least once)
```c
int n;
do
{
    n = get_int("Size: ");
}
while (n < 1);   // loop until a valid size is given
```
> The **"ask until valid" pattern** — PSet 1's Mario uses exactly this to force a positive pyramid height.

### for — all three pieces in one line
```c
for (int i = 0; i < 3; i++)
{
    printf("meow\n");
}
```
`for (init; condition; update)` → the *same* machine behaviour as the while loop, just denser. **Nested loops** (loop inside loop) draw 2D shapes → Mario connects rows and columns.

---

## 6. Writing Your Own Functions

```c
#include <cs50.h>
#include <stdio.h>

void meow(int n);        // prototype: "I exist, I return void, I take an int"

int main(void)
{
    meow(3);             // call
}

void meow(int n)         // definition
{
    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
}
```

- **Why prototype?** C reads top-to-bottom; without the prototype at the top, `main` would not know `meow` exists. (In Python there are no prototypes — the interpreter reads the whole file first.)
- **Parameters = inputs, return value = output** — the function contract mirrors the week-0  **Input → Algorithm → Output** pipeline.

```c
int square(int x)
{
    return x * x;
}                        // return type must match what you promise in the prototype
```

---

## 7. Constants, Comments & Good Hygiene (CS50-ish)

- Use **meaningful names** (`counter`, `n`, `answer`, `x`). Avoid magic numbers — prefer named constants:
```c
const int SENSOR_LIMIT = 100;
```
- **Comment** the *why*, not the *what*. One-line `//` and block `/* ... */`.
- Keep **functions small and single-purpose**; hand "helping hand" functions to the `helper` discipline of PSets.

---

## 8. "The Cuddle" — What Malan Wants You to Take Away

1. **Compile is a real step** you must train yourself to remember (Scratch compiled for you).
2. **Types matter**: memory is finite, division truncates, floats wobble.
3. **Patterns > memorized syntax**: the `do-while` input-guard and nested-`for` grid appear again in scoring games, filters, and every language.
4. **Abstraction via CS50 library** is deliberate: you'll un-hide `scanf`, pointers, and `malloc` in Weeks 2–4.

---

## 9. Cross-Links

- [[cs50/week-0-scratch]] — where each C block came from.
- [[cs50/week-2-arrays]] — next stop: what happens before compile (preprocessing→linking), error types, arrays, and the string data.
- [[programming-cs-fundamentals]] — the 21-segment fundamentals map almost 1:1 onto this week (types, conditionals, loops, functions).
- [[cs50/problem-sets]] — PSet 1 track (Hello / Mario / Cash / Credit).