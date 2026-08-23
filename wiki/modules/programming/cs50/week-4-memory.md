---
module: "programming"
course: "CS50x — Introduction to Computer Science"
week: 4
topic: "Hexadecimal, Pointers, Stack vs Heap, malloc/free, Structs, File I/O"
tags: [programming, computer-science, cs50, harvard, memory, pointers, malloc, valgrind, stack, heap, structs, file-io]
last_updated: "2026-08-11"
---

# Week 4 — Memory

> **Goal of the week:** un-hide the *machine underneath strings* — **pointers**. Learn the stack vs heap memory model, allocate and free memory yourself (`malloc`/`free`), copy data safely, group data with **structs**, and read/write **files**.
> **PSet 4:** *Filter* (manipulate image pixels — arrays of RGB structs), *Recover* (reconstruct JPEGs from a memory card — byte-scanning + file I/O).

---

## 1. Hexadecimal — Shorthand for Bytes

- Hex = **base 16**: digits `0–9` + `A–F`. Each hex digit is exactly **4 bits** → two hex digits = one byte.
- `0x` prefix: `0x41` = 65 = `'A'`; `0xFF` = 255 (all 8 bits on).
- Why programmers love it: **memory addresses** are long; hex compresses a byte into two readable symbols.

| Decimal | Hex | Binary |
|---|---|---|
| 0 | 0x00 | 00000000 |
| 160 | 0xA0 | 10100000 |
| 255 | 0xFF | 11111111 |

---

## 2. Pointers — Variables That Hold Addresses

- Every variable lives at a **memory address**. A **pointer** is a variable *whose value is an address*.
- `&` = "address of". `*` = "go to / dereference".

```c
int n = 50;
int *p = &n;      // p holds the address where n lives
printf("%p\n", p); // prints 0x….  (%p = pointer format code)
printf("%i\n", *p);// dereference: prints 50
```

- **Reveal (Week 2 payoff):** `string` is just `char *` — CS50 hides the star. `string s = "HI!";` makes `s` a pointer to `'H'`; `s[1]` is `*(s+1)`.
- `NULL` = the "no address" sentinel. **Always check `p != NULL` before dereferencing** → prevents crashing on garbage pointers.
- Pointer size: 8 bytes on a 64-bit system (it stores an address), whatever it points to.

### Pointer arithmetic
```c
printf("%c\n", *s);   // 'H'
printf("%c\n", *(s+1)); // 'I'
printf("%c\n", s[1]); // same thing — s[i] == *(s+i)
```

---

## 3. The Memory Model — Stack vs Heap

A running program's RAM contains **segments**; the two that matter now:

```
┌──────────────────────┐  high addresses
│         STACK        │  grows DOWN
│  (local vars,       │  auto-allocated on function entry
│   return addresses, │  auto-freed on return
│   call frames)      │  e.g. main's locals, recursion frames
├──────────────────────┤
│          .           │  (global/static data, code below)
├──────────────────────┤
│         HEAP         │  grows UP
│  (malloc/calloc/     │  manual allocation
│   realloc memory)    │  freed ONLY by free()
└──────────────────────┘  low addresses
```

- **Stack:** automatic; every function call pushes a **call frame** (its locals + return address). Frames pop off when the function returns. Recursion stacks frames → too deep = **stack overflow** (Week 3).
- **Heap:** manual. `malloc(size)` asks the OS for bytes; it returns `NULL` if it fails. **Everything you `malloc` you must `free`** — otherwise **memory leaks** accumulate.

```c
int *x = malloc(sizeof(int));   // 4 bytes on the heap
if (x == NULL) return 1;        // defensive: check failure
*x = 42;
free(x);                        // give the bytes back
```

---

## 4. The Great Gotchas (why string/array code in C is dangerous)

- **Uninitialized memory = garbage values**: `malloc` does *not* clear memory. (Use `calloc` if you want zeros.)
- **Buffer overflows:** writing `strcpy` into too-small space walks off the end of your array — the root of countless real-world exploits (and Week 10's security content).
- **Comparing strings with `==`:** compares the *addresses* (the pointers), NOT the characters — you must use `strcmp`.
- **Copying pointers copies the address, not the data:**
```c
string a = get_string("a: ");
string b = a;      // b now points at the SAME memory as a
```
Change `a`, and `b` "changes" too — a classic Week-3/Pset bug. To copy properly, allocate and `strcpy`:
```c
char *b = malloc(strlen(a) + 1);   // +1 for the '\0'
strcpy(b, a);
```

### swap() — the pointer classic
```c
void swap(int *a, int *b)     // needs addresses, not values
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
```
Without `&`/`*`, the swap only copies values into local frames and does nothing to the caller's variables. **"Pass pointers when you want to modify the caller's data."**

---

## 5. Valgrind — Your Memory Bug Detector

```bash
valgrind ./yourprogram
```
Reports **memory leaks** (allocated but never freed), **invalid reads/writes** (buffer overflows), and use of **uninitialized values** — exactly PSet 4's workflow for `Filter` and `Recover`. Build the habit: run `valgrind` on any code that `malloc`s.

---

## 6. Structs — Group Related Data

```c
typedef struct
{
    string name;
    string dorm;
}
student;

student s;              // now use student as a type
s.name = "Carter";
s.dorm = "Adams";
```
- `typedef` creates an alias so you write `student` instead of `struct student`.
- Arrays of structs: `student students[2];` → `students[0].name = "Emma";`.
- Structs are *copied by value* by default — a `len`/array of structs is exactly PSet 4's **RGB pixel** (`{BYTE rgbtRed, rgbtGreen, rgbtBlue;}`) and the "suits of cards" examples.

---

## 7. File I/O — Persisting Beyond the Run

```c
FILE *file = fopen("phonebook.csv", "a");    // fopen modes: r read, w write(truncate), a append
if (file == NULL) return 1;                  // always check!
fprintf(file, "%s,%s\n", name, number);
fclose(file);                                // always close!
```

- `fopen` → `FILE *` → read/write via `fprintf`, `fgets`, `fread`, `fwrite` → `fclose`.
- **`fread(data,size,count,file)`** is the workhorse of *Recover*: read 512-byte blocks and sniff for the JPEG magic bytes (`0xFF 0xD8 0xFF`).
- Database/serialization alternative: CSV is a flat file — Week 7 shows a *better* persistence layer in SQL.

---

## 8. Why This Week Matters Beyond CS50

- **Pointers = the missing link** to C++ (RAII, references), to linked structures (Week 5), and to any systems code (your future quant/C++ matching-engine module, C++20 in [[quant-toolkit-and-skills]]).
- **Memory discipline** (allocate → check → use → free) is the same discipline as validation and resource cleanup in higher-level languages.
- **Valgrind + debug50** = the "verify what you wrote, not what you hoped" habit.

## 9. Vocabulary to Master

- hexadecimal · pointer / `&` / `*` / dereference · `NULL` · stack · heap · call frame · `malloc` / `calloc` / `realloc` / `free` · memory leak · valgrind · buffer overflow · garbage value · struct / `typedef` · `FILE*` / `fopen` / `fclose` / `fread` / `fwrite`

## 10. Cross-Links

- [[cs50/week-2-arrays]] — strings were secretly pointers all along.
- [[cs50/week-3-algorithms]] — recursion's call frames stack up in the memory you now model.
- [[cs50/week-5-data-structures]] — linked lists, trees, and hash tables are *pointers used structurally*.
- [[cs50/week-6-python]] — Python hides all of this (no pointers); understanding it explains "why Python is slower" and why C++/C are still the performance choice.
- [[quant-toolkit-and-skills]] · [[matching-engine-cpp]] — this week is the direct ramp to C++20 systems code.
- [[cs50/problem-sets]] — PSet 4 (Filter / Recover).