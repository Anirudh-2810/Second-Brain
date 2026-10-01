---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "Module 3 — Arrays (3.1) & Strings (3.2) — module hub"
date: "2026-10-02"
description: "SPM Module 3 module map — syllabus coverage for 3.1 arrays and 3.2 strings, the concept-flow diagram, start-here routing to the dedicated arrays and strings pages, exam/lab mapping, and a one-screen formula sheet."
tags: [spm, module-3, arrays, strings, c-programming, 316U06C107, index, hub, exam-prep]
last_updated: "2026-10-02"
confidence: high
prerequisites: ["Module 2: Program Control Functions"]
---

## For future agent

**This is the Module 3 landing page — a map, not a content page.** It carries the syllabus coverage, the concept-flow diagram, routing, and a one-screen formula sheet. The teaching content now lives in two dedicated pages.

Created 2026-10-02 by splitting a former single page that had grown to 40.7 KB (past the vault's ~25 KB threshold). Nothing was deleted — the content was moved into the two pages below and this page was reduced to navigation.

| You want | Go to |
|---|---|
| **Arrays** — 1D, 2D, address formulas, search/sort, beginner-first | [[module-3-arrays]] |
| **Strings** — `'\0'`, `strlen`/`strcpy`/`strcmp`/`strcat`, from scratch, **strcpy exam drill** | [[module-3-strings]] |
| Lab write-ups EXP4 + EXP5 | [[spm-lab-exp3-4-5-guides]] |
| Syllabus position of Module 3 | [[syllabus-316U06C107]] |
| Exam/OST patterns | [[assessment-guide-ese-ost-quiz]] |

**Do not re-merge these three pages.** The split was deliberate: arrays is the user's weak area and deserved its own deep page.

---

# Module 3 — Arrays & Strings (Hub)

> **Syllabus:** Module 3, **7 hours**, **CO3** — *Apply the concepts of arrays and strings*, Bloom's *Apply*.
> - **3.1** Arrays: 1D, multidimensional, declaration/initialization, reading/displaying
> - **3.2** Character arrays and strings: declaring/init, reading/writing chars & strings, operations, **implementing string handling from scratch**
>
> Self-learning (Module 4 area): file handling.

---

## 1. Syllabus coverage — what maps where

| Syllabus item | Covered in | Status |
|---|---|---|
| 3.1 Arrays 1D — declaration, initialization | [[module-3-arrays]] §1.2, §1.4 | complete (4 init styles) |
| 3.1 1D — indexing, reading, displaying | [[module-3-arrays]] §1.5, §1.6 | complete |
| 3.1 Array operations (sum, avg, max/min, search) | [[module-3-arrays]] §1.7, §3.2 | complete |
| 3.1 Multidimensional arrays | [[module-3-arrays]] §2 | complete |
| 3.1 Row-major vs column-major, address formulas | [[module-3-arrays]] §2.2 | complete |
| 3.1 Sorting / insertion / deletion | [[module-3-arrays]] §3.3, §3.4 | complete (beyond the deck, exam-bank depth) |
| 3.2 Character arrays, declaring/initializing | [[module-3-strings]] §1.1, §1.3 | complete (4 styles) |
| 3.2 Reading/writing **chars** | [[module-3-strings]] §1.4 | complete (`getchar`/`putchar`/`%c`) |
| 3.2 Reading/writing **strings** | [[module-3-strings]] §1.5 | complete (`%s`, `fgets`, `%s`, `puts`) |
| 3.2 String operations (library) | [[module-3-strings]] §2 | complete |
| 3.2 **String handling from scratch** | [[module-3-strings]] §3 | complete (length, copy, concat, compare, reverse, palindrome, vowels) |
| 3.2 `strcpy` emphasis | [[module-3-strings]] §6 | full exam drill + 6 predict-output drills |

---

## 2. The concept flow

```
ARRAYS
   |
   +-- 1-D Array  (a list)         -> declaration, init, read, display, sum, largest
   |                                  address = B + i*S
   |
   +-- 2-D Array  (a table/matrix)  -> nested loops, row-major order
   |                                  address = B + (i*C + j)*S
   |
   +-- CHARACTER ARRAYS
          |
          v
       STRINGS   (char array + '\0')
          |
          +-- Read  (scanf %c / %s / fgets)
          +-- Write (printf %c / %s, putchar, puts)
          +-- Length    (strlen)
          +-- Copy      (strcpy)      <-- dedicated exam drill
          +-- Compare   (strcmp)
          +-- Concat    (strcat)
          +-- Reverse   (loop)
          |
          v
       "FROM SCRATCH" = the same operations, one character at a time with a loop
```

**The four sentences to remember forever:**

1. C has **no** string type. A string is a `char` array ending in `'\0'`.
2. Array indexing **starts at 0**. Last valid index = size − 1.
3. `strlen` counts characters **without** `'\0'`; `sizeof` counts the array **with** it.
4. Arrays are **contiguous** → O(1) access. That is the reason for the address formulas.

---

## 3. Exam focus map

| If the question is about… | Jump to |
|---|---|
| `B + i*S` for a 1D array | [[module-3-arrays]] §1.3 |
| `B + (i*C+j)*S` row-major vs `(j*R+i)*S` column-major | [[module-3-arrays]] §2.2 |
| Why outer=row/inner=column in C | [[module-3-arrays]] §2.2, §2.4 |
| Partial initialization zero-fills | [[module-3-arrays]] §1.4 |
| No bounds checking / undefined behaviour | [[module-3-arrays]] §1.5, §1.9 |
| Linear vs binary search, O(n) vs O(log n) | [[module-3-arrays]] §3.1, §3.2 |
| Bubble sort passes and the `swapped` flag | [[module-3-arrays]] §3.3 |
| Insert/delete shift count | [[module-3-arrays]] §3.4 |
| `strlen` vs `sizeof` | [[module-3-strings]] §1.1, §2 |
| `scanf("%s")` stops at whitespace; `fgets` for lines | [[module-3-strings]] §1.5 |
| `strcmp(...) == 0` not `== 1`; never `==` on strings | [[module-3-strings]] §2.1, §4.4 |
| **`strcpy` from scratch + examiner checklist** | [[module-3-strings]] §6 |
| `strncpy` missing-`'\0'` bug | [[module-3-strings]] §6.5 |
| Reverse-string off-by-one and the `size_t` infinite loop | [[module-3-strings]] §3.5 |
| Palindrome mirror indexing | [[module-3-strings]] §3.6 |

---

## 4. Lab mapping

| Experiment | Topic | Where to revise |
|---|---|---|
| **EX3** | Looping control structures (`for`/`while`/`do-while`, `break`/`continue`, nesting) | [[spm-lab-exp3-4-5-guides]]; loops: [[module-2-program-control-functions]] |
| **EX4** | Arrays — 1D/2D, sum/avg, linear search, max/min, matrix addition | [[module-3-arrays]] |
| **EX5** | Strings — declare/init/display, `fgets`, `strlen`/`strcpy`/`strcat`/`strcmp`, palindrome | [[module-3-strings]] |

Full write-ups with sample programs, task lists, and post-lab Q&A with worked answers: [[spm-lab-exp3-4-5-guides]].

---

## 5. One-screen formula sheet

| Quantity | Formula / pattern |
|---|---|
| 1D address | $B + i \times S$ |
| Row-major 2D address | $B + (i \times C + j) \times S$ |
| Column-major 2D address | $B + (j \times R + i) \times S$ |
| Last valid index | size − 1 |
| Bounds check | `0 <= i < n` |
| Element count | `sizeof(a) / sizeof(a[0])` |
| Array total bytes | n × `sizeof(type)` |
| Binary-search spacing | $n/2^k$ per step, $k = \log_2 n$ |
| String bytes | chars + 1 |
| `strlen` | excludes `'\0'` |
| `sizeof` on a string | includes `'\0'` + spare capacity |
| `strcmp` equal | `== 0` |
| Copy (faculty form) | loop, then `dst[i] = '\0';` |
| Copy (one-liner) | `while ((d[i]=s[i]) != '\0') i++;` |
| Read a word | `scanf("%19s", s);` — no `&` |
| Read a char | `scanf(" %c", &ch);` |
| Read a line | `fgets(s, sizeof s, stdin);` |
| Write | `printf("%s", s);` / `puts(s);` |
| Strip newline | `s[strcspn(s, "\n")] = '\0';` |

---

## 6. Source coverage for this module

Ingested 2026-10-02 from `raw-sources/`:

| Source | Used for |
|---|---|
| `SPM Lecture/SPM_Module3_1.pptx` (27 slides, AY 2026-27) | the dedicated arrays page |
| `SPM Lecture/SPM_Module3_2.pptx` (27 slides, AY 2026-27) | the dedicated strings page |
| `SPM Lecture/Unit No.3 Arrays_Strings.pdf` (34 pp) | both pages — beginner narrative + from-scratch loops |
| `SPM Lab/EX4.docx` | arrays lab write-up |
| `SPM Lab/EX5.docx` | strings lab write-up |
| `SPM_Syllabus_316U06C107.md` | syllabus mapping above |

**Source conflicts, resolved and recorded on the child pages:** the deck and the handout use different example data; the deck's from-scratch functions use `int` returns with an explicit `dst[i] = '\0';` while the handout's concatenation uses two indices — both forms are shown, faculty form first, because that is what gets marked.

---

## Cross-References

- [[module-3-arrays]] · [[module-3-strings]] — the two dedicated pages
- [[spm-string-functions-char-equality-reverse]] — shorter classroom version of the strings page
- [[syllabus-316U06C107]] — official module map and CO mapping
- [[spm-lab-exp3-4-5-guides]] — EXP3/4/5 write-ups
- [[module-2-program-control-functions]] — the loops this module runs on (flags, counting loops)
- [[module-1-spm-c-basics]] — memory layout (stack vs BSS vs text) that explains where arrays and string literals live
- [[assessment-guide-ese-ost-quiz]] · [[formula-sheet-spm]] · [[c-programming-master-study-guide]]