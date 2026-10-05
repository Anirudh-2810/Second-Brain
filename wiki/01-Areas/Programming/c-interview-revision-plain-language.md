---
course_code: "PROGRAMMING"
course_name: "Programming & Software Engineering Field"
unit: "C Interview Revision — Plain Language"
date: 2026-10-05
description: "Full C revision in plain language for technical interviews - every construct explained in everyday words with runnable snippets, the traps that actually get asked, and what to say out loud. Covers types, memory, pointers, arrays, strings, structs, functions, bitwise, and embedded C idioms."
tags: [c-programming, interview-prep, revision, embedded, pointers, memory, simple-language]
last_updated: "2026-10-05"
confidence: high
---

## For future agent
Plain-language C revision written for the [[01-Areas/Engineering/nexus-robotics/INDEX|Nexus Robotics embedded interview]] and any C-heavy technical round. The design rule: **explain each construct in everyday words first, then show the code, then name the trap.** Dense pages already exist for depth — [[01-Areas/Programming/c-programming/detailed-notes]] (29 KB course notes), [[01-Areas/Engineering/SPM/module-4-structures-unions-pointers]] (exam edition), [[01-Areas/Engineering/SPM/module-1-spm-c-basics]] (memory layout). Do not duplicate their derivations here; this page is the "say it like a human" layer over the top. Staleness: none — C is stable. Confidence `high` except where a behaviour is implementation-defined, which is called out inline.

# C Interview Revision — In Simple Language

> **How to use this:** read a section, **cover it, and say it out loud in one or two sentences.** If you can't say it simply, you don't own it yet. Every section ends with a trap — that's usually what's actually being tested.

---

## 1. The shape of a C program

```c
#include <stdio.h>     // 1. ask the standard library for tools

int main(void) {       // 2. entry point — where the program starts
    printf("Hello\n"); // 3. do the thing
    return 0;          // 4. 0 means success
}
```

**Say it simply:** *"C runs top to bottom. `main` is where it starts. `#include` pastes in declarations from a header so the compiler knows what `printf` is. `return 0` tells the operating system it worked."*

**Trap:** forgetting `#include <stdio.h>` — the compiler then treats `printf` as an unknown function and either errors or, worse in old compilers, silently guesses. **Headers are declarations, not libraries.**

---

## 2. Variables and data types

```c
int    age   = 20;        // whole numbers            (usually 4 bytes)
float  price = 19.99f;    // single-precision decimal  (4 bytes)
double pi    = 3.14159;   // double-precision decimal  (8 bytes)
char   grade = 'A';       // ONE character            (1 byte)
```

**Say it simply:** *"`int` counts. `float` and `double` measure, and `double` has more precision. `char` holds a single character — a whole word needs an array of them."*

**Trap — the big one:** in C, `5 / 2` is **`2`, not `2.5`**. Integer division throws away the remainder. Write `5.0 / 2` or `(float)5 / 2` to keep it. *This is the single most common C bug in an interview.*

```c
int   a = 5 / 2;      // 2   — both are int
float b = 5 / 2;     // 2.0 — int division happens FIRST, then converts
float c = 5.0 / 2;   // 2.5 — correct
```

**Trap — `char` arithmetic:** `char` promotes to `int` before any maths, so `200` stored in a signed 8-bit `char` becomes `-56`. Use `unsigned char` for raw byte data.

---

## 3. Operators — and the one that bites

```c
int x = 10;
x = x + 5;    // 15
x += 5;       // 20   (same thing, shorter)
x++;          // 21   (add 1)
```

### The assignment trap

```c
if (x = 5)    // WRONG — assigns 5, and 5 is truthy
if (x == 5)   // RIGHT — compares
```

**Say it simply:** *"`=` puts a value in a box. `==` asks whether two boxes hold the same thing. In C, mixing them up doesn't error — it silently changes your program."* **In Python `==` is the same trap**, which is why it keeps catching people.

### The bitwise operators

| Op | Name | What it does | Example (`a=12` = `1100`, `b=10` = `1010`) |
|----|------|--------------|------------------------------------------|
| `&` | AND | 1 only if both are 1 | `12 & 10 = 8` (`1000`) |
| `\|` | OR | 1 if either is 1 | `12 \| 10 = 14` (`1110`) |
| `^` | XOR | 1 if they differ | `12 ^ 10 = 6` (`0110`) |
| `~` | NOT | flip every bit | `~12` → all bits inverted |
| `<<` | left shift | multiply by 2 per shift | `1 << 3 = 8` |
| `>>` | right shift | divide by 2 per shift | `12 >> 2 = 3` |

**Say it simply:** *"Each bit is a tiny on/off switch. AND turns on only if both are on. OR turns on if either is. XOR turns on only if they disagree — which is why XOR toggles. Shifting left doubles, shifting right halves."*

**Trap:** `1 << 31` with a plain `1` is **undefined behaviour** — signed overflow. Write `1u << 31`. Same for `~` on signed values and for right-shifting a negative number (that one's implementation-defined).

**Bit manipulation you should be able to write cold:**

```c
#define BIT(n)       (1u << (n))
#define BIT_SET(v,n) ((v) |  BIT(n))    // turn on
#define BIT_CLR(v,n) ((v) & ~BIT(n))    // turn off  — ~ makes all-ones except bit n
#define BIT_TST(v,n) (((v) >> (n)) & 1u) // read it
```

*Why `~BIT(n)` clears exactly one bit: `~` produces a mask with zeros only where `BIT(n)` was 1, so AND-ing keeps every other bit and clears just that one.*

---

## 4. Making decisions

```c
if (temp > 30) {
    printf("Hot\n");
} else if (temp > 20) {
    printf("Warm\n");
} else {
    printf("Cool\n");
}
```

**Say it simply:** *"`if` runs a block only when the condition is true. Order matters — the first matching branch wins, so check the tightest condition first."*

**Anything non-zero is true.** `0` is false; `-1` is **true**; `""` (non-null pointer) is true; `NULL` is false. This trips people who expect only `true`/`false`.

**Trap:** `=` vs `==` again, and the classic missing-braces bug:
```c
if (x > 0)
    y = 1;
    z = 2;      // NOT in the if — it always runs
```
Use braces. Every time.

---

## 5. Loops

```c
for (int i = 0; i < 5; i++) { }   // repeat a known number of times

while (n > 0)      { n--; }       // repeat until a condition fails
do { n--; } while (n > 0);        // run once, THEN check
```

**Say it simply:** *"`for` is 'do this many times'. `while` is 'keep going while something is true'. `do-while` is 'do it once, then decide whether to continue' — the only one that always runs at least once."*

**Trap:** off-by-one — `<= 5` runs six times, `< 5` runs five. **Also:** C counts from **0**, so `i < n` covers indices `0` to `n-1`. An array of 5 elements has indices 0–4.

**Loop control:**

```c
break;     // leave the loop NOW
continue;  // skip to the next iteration
```

---

## 6. Arrays

```c
int marks[5] = {90, 85, 72, 88, 95};
marks[0];     // 90 — first element, NOT marks[1]
sizeof(marks) / sizeof(marks[0])   // 5 — the array length, safely
```

**Say it simply:** *"An array is a row of same-type boxes in memory, side by side. Because they're side by side, the computer can jump to element 3 directly instead of counting past 0, 1, 2 — that's why indexing is instant."*

**Trap:** the length trick. `sizeof(marks)` is 20 bytes (5 × 4). Dividing by `sizeof(marks[0])` (4) gives 5. Just `sizeof(marks)` gives **bytes, not elements** — the classic error.

**Trap:** out-of-bounds. `marks[5]` is not an error in C — it just reads whatever memory is next. No bounds checking. This is why buffer overflows are possible and why C is fast.

```c
int matrix[2][3];   // 2 rows, 3 columns
matrix[1][2]        // row 1 (the second), column 2 (the third)
```

---

## 7. Strings — arrays of `char`

```c
char name[20] = "Anirudh";   // needs 20 bytes: 7 letters + '\0' + spare
```

**Say it simply:** *"A string in C is just an array of characters that ends with a special character, `'\0'` — a zero byte. Everything after the zero is ignored. So `Anirudh` needs 8 slots, not 7."*

**The single most important C fact:** if your buffer is exactly the text length with no room for `'\0'`, every string function runs off the end.

**Library functions** (`#include <string.h>`):

| Function | Does | Trap |
|----------|------|------|
| `strlen(s)` | length | excludes `'\0'`; O(n) every call |
| `strcpy(d,s)` | copy | **no bounds check** — buffer must be big enough |
| `strncpy(d,s,n)` | copy at most n | doesn't guarantee `'\0'` if `s` is ≥ n |
| `strcmp(a,b)` | 0 if equal | returns negative/positive, **not** ±1 |
| `strcat(d,s)` | append | `d` must have room |

**Say it simply:** *"`strlen` counts characters, `strcpy` copies, `strcmp` compares and returns 0 when equal, `strcat` appends. None of them check whether the destination is big enough — that's the programmer's job in C."*

---

## 8. Making decisions on many values — `switch`

```c
switch (grade) {
    case 'A': printf("Excellent\n"); break;
    case 'B':
    case 'C': printf("Fine\n");     break;
    default:  printf("Unknown\n");
}
```

**Say it simply:** *"`switch` jumps straight to the matching `case` instead of testing every `if` in order — faster and easier to read when you're comparing one value against many. The `break` stops it falling through into the next case."*

**Trap:** **missing `break` = fall-through.** Without it, `case 'A'` runs its code *and then* `case 'B'`'s code too. Grouping cases with no `break` between them (like `'B'` and `'C'` above) is intentional; forgetting it anywhere else is a bug.

---

## 9. Functions

```c
int add(int a, int b) {      // returns an int, takes two ints
    return a + b;
}

void greet(void) { }         // no return value, no parameters
```

**Say it simply:** *"A function is a named box of steps you can run again. It takes inputs (parameters), does work, and can hand back a value with `return`."*

**The `void` trick, worth using:**

```c
int divide(int a, int b, int *out) {
    if (b == 0) return -1;      // signal failure
    *out = a / b;               // write the result through a pointer
    return 0;                   // signal success
}
```

*This is C's substitute for exceptions. Return a code, write the value through a pointer.*

**Trap:** C is **always pass-by-value**. Passing an array still copies only the pointer (see §11).

---

## 10. Pointers — the thing everyone fears

```c
int x = 42;
int *p = &x;     // p HOLDS the address of x

printf("%d\n", x);    // 42
printf("%d\n", *p);   // 42   — * means "the value at this address"
printf("%p\n", p);    // the address itself
```

**Say it simply, and this is the sentence that makes it click:** *"A pointer is a variable that stores a memory address. `&x` means 'the address of x'. `*p` means 'go to that address and read what's there'. So `&` goes from thing to address, and `*` goes from address back to thing."*

**Everyday analogy:** a house is the value, its address is the address, and a piece of paper with the address written on it is the pointer. `*paper` gets you back into the house.

### Why pointers exist — the interview answer

*"Three reasons. First, dynamic memory: `malloc` gives you a block sized at runtime, and only a pointer can hold onto it. Second, avoiding copies — passing a 1 MB array to a function by value would copy a megabyte; passing a pointer passes one address. Third, hardware: a memory-mapped register is just an address, so `*(volatile uint32_t *)0x40021000` reads a device register. Pointers aren't a C quirk — they're how you get at memory directly."*

### Pointer arithmetic

```c
int arr[3] = {10, 20, 30};
int *p = arr;      // p points at arr[0]

p++;               // now points at arr[1] — moved 4 bytes, not 1
arr[1] == *(arr+1) == *(p) == p[1]      // all the same thing
```

**Say it simply:** *"Adding 1 to an `int*` moves it past one whole integer — 4 bytes. It's typed, not raw bytes. That's why `char*` steps by 1 and `int*` steps by 4."*

**Traps, all of them real:**
- `int *p = &x; int *q = &p;` — that's a pointer to a pointer. `**q` is `x`.
- Returning `&localvar` — the local dies when the function returns, so the pointer is **dangling**.
- `p + 5` when `p` points at a 3-element array — undefined behaviour.

---

## 11. Structs — grouping different types

```c
struct Student {
    int   roll;
    char  name[30];
    float cgpa;
};

struct Student s1 = {101, "Asha", 8.9};
s1.roll;                 // 101

struct Student *ptr = &s1;
ptr->roll;               // same thing — -> is shorthand for (*ptr).roll
```

**Say it simply:** *"An array holds many of the SAME type. A struct holds one record made of DIFFERENT types — like one student row. `->` gets into a struct through a pointer."*

### The padding trap — a genuine favourite

```c
struct Example {
    char c;   // 1 byte
    int  x;   // wants 4-byte alignment → 3 bytes of padding before it
    char d;   // 1 byte
};             // 3 bytes of tail padding → total 12, NOT 6
```

**Say it simply:** *"The compiler pads structs so each member sits at an address it can read efficiently — an `int` needs a 4-byte-aligned address. That means a struct can be bigger than the sum of its parts. Order members largest-first to waste less."*

**Also:** `struct` assignment copies **all** members (unlike arrays, which can't be assigned at all), and you **cannot** use `==` on structs — compare field by field.

---

## 12. Storage classes — where a variable lives

| Keyword | Lives | Use for |
|---------|-------|---------|
| `auto` | stack (default for locals) | normal variables |
| `static` (local) | whole program, remembered between calls | counters that must persist |
| `static` (file scope) | private to this file | hiding a module's internals |
| `extern` | declared elsewhere | sharing across files |
| `const` | read-only | values that must not change |

```c
void count_calls(void) {
    static int calls = 0;    // survives after the function returns
    calls++;
    printf("%d\n", calls);
}
```

**Say it simply:** *"`static` on a local variable keeps it alive after the function returns, so it remembers. On a file-scope variable or function, `static` means 'private to this file' — nobody else can touch it."*

---

## 13. Preprocessor — `#define`

```c
#define PI 3.14159
#define SQUARE(x) ((x) * (x))     // parentheses are NOT optional

SQUARE(3 + 1)   // ((3+1)*(3+1)) = 16  ✓
```

**Say it simply:** *"`#define` is a find-and-replace the compiler does before reading your code. For functions, the parentheses around the argument matter — without them you get operator-precedence bugs."*

---

## 14. Files

```c
FILE *fp = fopen("data.txt", "r");
if (fp == NULL) { /* handle the failure */ }
fprintf(fp, "hello\n");
fclose(fp);
```

| Mode | Meaning | If the file exists |
|------|---------|---------------------|
| `"r"` | read | opens it |
| `"w"` | write | **erases it** |
| `"a"` | append | writes at the end |

**Say it simply:** *"`fopen` returns a pointer to the file, or `NULL` if it failed — always check. `w` silently truncates, which is the classic way to lose data. `fclose` when you're done."*

---

## 15. Embedded C — the idioms that actually get asked

This is the part no college course covers well, and the part an embedded round is *actually* testing.

### `volatile` — tell the compiler "this can change behind your back"

```c
volatile uint8_t sensor_ready;      // set by an interrupt
volatile uint32_t * const STATUS = (uint32_t *)0x40021000;   // a register
```

**Say it simply:** *"`volatile` means 'read this every single time, don't cache it in a register'. Without it, the compiler sees a variable that never changes in your code, decides it can hold it in a CPU register, and — in an interrupt-driven program — never notices the interrupt changed it. It's mandatory for ISR-shared flags and memory-mapped I/O."*

**The trap everyone gets wrong:** `volatile` does **not** make an operation atomic, and does **not** order memory accesses. If the ISR and your main loop both do read-modify-write on a shared variable, `volatile` alone loses updates. You need interrupts disabled for the critical section.

### ISR discipline

```c
volatile uint16_t sample;

void ADC_ISR(void) {
    sample = ADC_read();    // minimal: read hardware, store it
    ready   = 1;            // flag LAST, after the data is valid
}
```

**Say it simply:** *"An interrupt pauses everything to run this. So it must be short, must not block, must not call heavy library code. It reads hardware and sets a flag; the main loop does the real work. Setting the flag before writing the data lets the main loop read a stale value."*

### Why firmware avoids `malloc`

**Say it simply:** *"`malloc` timing isn't guaranteed, and a fragmented heap over months of uptime causes slow, unpredictable allocation. A control loop with a deadline can't risk that. So firmware uses fixed-size `static` buffers — deterministic, and impossible to leak."*

### Fixed-point, because there's no FPU

```c
// Q8: the value × 256, stored as an int
int32_t to_q8(int32_t x)     { return x * 256; }
float    q8_tof(int32_t q)    { return (float)q / 256.0f; }
```

**Say it simply:** *"On a microcontroller, floating point is often done in software and is slow. Fixed-point stores `3.75` as the integer `960` with a known scale. Division is the same, but it's fast and the timing is predictable."*

### The memory map — five regions

| Region | What lives there | Grows |
|--------|------------------|-------|
| **Text/code** | your compiled instructions | fixed |
| **Data** | initialised globals | fixed |
| **BSS** | uninitialised globals (auto-zeroed) | fixed |
| **Heap** | `malloc` | ↑ up |
| **Stack** | locals, return addresses | ↓ down |

**Say it simply:** *"Globals go in Data or BSS. Function locals go on the stack, which is wiped automatically when the function returns — which is why you can't return a pointer to a local. `malloc` memory lives on the heap and you must `free` it yourself."*

---

## 16. The traps, gathered in one place

Read this list the night before. Each one is a real bug that real interviews ask about.

1. `=` vs `==` in an `if`.
2. `5 / 2` is `2`, not `2.5` — integer division.
3. `sizeof(arr)` gives **bytes**; divide by `sizeof(arr[0])` for length.
4. Off-by-one: arrays run `0` to `n-1`; `<= n` loops one time too many.
5. `char` isn't a whole word — `char name[]` for text, and leave room for `'\0'`.
6. `strcpy`/`strcat` never check bounds. Always your job.
7. Missing `break` in `switch` falls through into the next case.
8. Missing braces around a single-statement `if` body.
9. Returning `&local` — the memory dies with the function.
10. `fopen` with `"w"` erases an existing file.
11. `1 << 31` with a signed `1` is undefined behaviour — use `1u`.
12. Unsigned underflow: `5u - 10` wraps to a huge number, not `-5`.
13. A struct can be bigger than its parts — padding.
14. You cannot `==` two structs.
15. `malloc` without `free` leaks; `free` twice is undefined.
16. `volatile` is not atomic.
17. Arrays have no bounds checking — one past the end is on you.
18. `%d` with a `float` — mismatched format specifiers are undefined behaviour.

---

## 17. If they ask "how would you write this on an MCU"

Say the constraint out loud first — it shows engineering judgement and it buys you time:

> "Before I write code — is this on a Cortex-M with an FPU, or an 8-bit AVR? Are we allowed to allocate? What's the loop deadline? Those three answers decide whether I use `float`, `double`, or fixed-point, and whether I use `static` buffers or `malloc`."

Then write it. The narration is scored as much as the code.

---

## See also

- [[01-Areas/Engineering/nexus-robotics/nexus-c-embedded-drills]] — the live-coding drills built on this
- [[01-Areas/Programming/c-programming/index|C programming library]] — full course notes, practice bank, memory module
- [[01-Areas/Engineering/SPM/module-4-structures-unions-pointers|SPM M4]] — structs/unions/pointers at exam depth
- [[01-Areas/Engineering/SPM/module-1-spm-c-basics|SPM M1]] — memory layout and the compilation pipeline
- [[01-Areas/Programming/c-programming/practice/01-basics-operators|Practice bank]] — solved problems with trace tables
- [[python-interview-revision-plain-language|Companion: the same treatment for Python]] — read both; §18 there is the C-habits-that-bite-you table