---
module: "c-programming"
topic: "C Programming — Solved Practice Problem Bank (exam-style)"
tags: [programming, c, practice, solved-problems, exam, output-prediction]
last_updated: "2026-08-19"
---

# Solved Practice Problem Bank

> 45+ **exam-style problems with full solutions** — the classic types colleges actually ask: **predict the output**, **find the error**, and **write the program**. Every solution has a step-by-step **trace table** so you can *see* what the computer does, line by line.

## How to use this bank (before you peek)

1. Cover the **Solution** section.
2. Solve by hand on paper — predict the output exactly.
3. Compare with the trace table.
4. If wrong, find the exact line where your mental model diverged.
5. Re-type the program yourself and run it.

## Topics

| File | Problems | Topics covered |
|---|---|---|
| [[c-programming/practice/01-basics-operators\|01 · Basics & operators]] | 6 | output prediction, precedence, `%`/`/`, bitwise, implicit conversion |
| [[c-programming/practice/02-conditionals-loops\|02 · Conditionals & loops]] | 6 | `if`/`else`, `switch`, `while`/`for`/`do-while`, nested loops, `break`/`continue` |
| [[c-programming/practice/03-arrays-1d\|03 · 1D arrays & searching]] | 7 | declare/init, traversal, sum/avg, min/max, reverse, linear & binary search |
| [[c-programming/practice/04-arrays-2d\|04 · 2D arrays (matrices)]] | 5 | matrix input/output, sum rows, transpose, matrix add/multiply, diagonal sum |
| [[c-programming/practice/05-sorting\|05 · Sorting]] | 6 | bubble sort, selection sort, insertion sort — full trace tables, best/worst case |
| [[c-programming/practice/06-strings\|06 · Strings]] | 5 | `strlen`, palindrome, reverse, count vowels, string functions |
| [[c-programming/practice/07-functions-recursion\|07 · Functions & recursion]] | 6 | prototypes, pass-by-value vs address, factorial, Fibonacci, digit-sum recursion |
| [[c-programming/practice/08-pointers-structs\|08 · Pointers & structs]] | 5 | `&`/`*`, pointer arithmetic, swap via pointers, struct access, array of structs |

## The 3 most common exam traps (watch for these)

1. **Integer division:** `7/3` is `2`, not `2.33`.
2. **Off-by-one:** arrays start at index **0**; a loop `i <= size` over-reads.
3. **Post-increment in use:** `printf("%d", x++)` prints `x` *first*, then increments.

## Reading order

Start with [[c-programming/c-essentials-for-beginners|C Essentials for Absolute Beginners]] if the concepts feel new, then work through 01 → 08. Each file builds on the last.

**Companion:** [[c-programming/detailed-notes|Detailed notes]] · [[c-programming/flowcharts|Flowcharts]] · [[c-programming/projects|Projects]]