---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "Lab write-ups — EXP1 (data/operators) + EXP2 (branching) + CodeBlocks setup"
tags: [spm, btech, c, lab, experiments, data-types, operators, branching, codeblocks, gcc, msys2, viva]
last_updated: "2026-09-18"
date: "2026-09-18"
description: "SPM lab write-ups for EXP1 (data types, operators) and EXP2 (branching) with tasks, post-lab Q&A, plus MSYS2+GCC+CodeBlocks Windows setup."
---

## For future agent

This note gives executable write-ups for SPM EXP1 and EXP2 from the Sem-1 faculty drive, plus the Windows toolchain setup handout. Sibling: [[spm-lab-exp-guides]] (EXP1/7/8 from the older template set — same EXP1 aim, different tasks; use EITHER as the write-up base). Rubric/timeline in [[lab-ca-and-experiments]] and [[lesson-plan-2026-27]]; theory in [[spm-module1-faculty-companion]] / [[spm-module2-faculty-companion]].

# SPM Lab — EXP1 + EXP2 Write-ups (Sem-1 Drive)

> Sources: `raw-sources/SPM SEM1 work/Experiment/EX1.docx` (= `EX1.pdf`, same 5 pp.) · `Experiment/EX2.docx` (6 pp.) · `PPT/Module 1/Installing C compiler and Code blocks on Windows.docx` | Dept. of Science and Humanities | Footnote on every page: "Course Name: Structured Programming Methodology"

## EXP1 — Data Types and Operators (M1, CO1)

**Aim (5 bullets):** write/compile/execute C programs; basic program structure; `printf`/`scanf`; fundamental data types, constants, variables; simple programs with arithmetic/relational/logical/assignment operators.

**Theory gist:** edit → `gcc HelloC.c -o HelloC` (compile + link together) → run `HelloC.exe` (Windows) / `./HelloC` (Linux). Unlike Java, filename need not match anything inside — only `.c` matters. `#include <stdio.h>` brings I/O declarations; `main()` is the entry; `return 0;` = success. Types: int 4 `%d`, float 4 `%f`, double 8 `%lf`, char 1 `%c`. `scanf` needs `&a` (address), `printf` takes `a` (value). `a/b` truncates when both int; relational → 1/0 (no boolean type); `i++` uses-then-increments, `++i` increments-then-uses.

**Lab tasks:** T1 declare/init int+float+char (Age/Percentage/Grade), print each with the right specifier. T2 input two ints, print all five `+ - * / %` results line by line. T3 circle area ($\pi r^2$) + circumference ($2\pi r$) from float radius, $\pi$ via `const`/`#define`, two decimals. Practice: swap via temp; Celsius→Fahrenheit ($F = C \times 9/5 + 32$); simple interest with a constant; average of three ints as float via explicit cast; `i++` vs `++i` demo in separate `printf`s.

**Post-lab Q&A (10):** compiler (whole-program-before-run) vs interpreter (line-by-line); every variable needs a declared type (fixes memory + valid ops, checked at compile); constant vs variable; `#include`/headers (shared declarations); `/` (quotient) vs `%` (remainder, ints only); `i++`/`++i` + example; implicit (auto widening) vs explicit (`(type)` cast) conversion; precedence deciding `10+2*3` = 16; `printf` (display) vs `scanf` (read into `&var`); int division truncates — avoid by casting one operand to float.

**Outcome:** compile/execute with gcc; program structure; `printf`/`scanf`; declarations; operators + result-type prediction.

Write-up must contain handwritten algorithm/pseudocode + flowchart + faculty signature (L4 per [[lab-ca-and-experiments]]), else capped at L3.

## EXP2 — Decision Making and Branching (M2.1, CO2)

**Aim:** decision-making concept; `if`, `if-else`, `else-if` ladder, nested `if-else`, `switch-case`; ternary shorthand; menu programs with error handling.

**Theory gist:** pure sequence runs everything once; branching CHOOSES by condition (non-zero = true) — one of the three structured pillars. Ladder checks top-down, first true wins; nested decides-after-deciding (EXP2 sample: largest-of-three). Switch takes int/char only (no float/string); missing `break` falls through; nested-ladder and ladder often express the same logic — pick the readable one.

**Samples (6):** positive-check (`if`) · even/odd (`if-else`) · grade ladder (90/75/60/40 → A/B/C/D/F) · largest-of-three (nested) · calculator (`switch` on `char op` with `" %c"` leading-space scan + `b != 0` guard + default) · max-of-two (`max = (a>b) ? a : b;`).

**Lab tasks:** T1 leap year (÷400, or ÷4-but-not-÷100). T2 vowel/consonant via `switch-case`. T3 menu calculator: 5 ops (add/sub/mul/div/mod), two numbers + choice, div/mod-by-zero and invalid-choice error messages (no crash/garbage). Practice: pos/neg/zero; largest-of-three nested; triangle validity (angles sum 180°) then Equilateral/Isosceles/Scalene; 4-digit PIN vs stored constant ("Access Granted/Denied"); day number 1–7 via `switch`.

**Post-lab Q&A (10):** what decision-making is + why; `if-else` (exactly two) vs ladder (many, ordered); nested vs ladder preference (dependent decisions vs ranked list); switch expression types (int/char); `break` purpose (stop fall-through); `default` purpose (catch-all); `if(a>b)max=a;else max=b;` → `max=(a>b)?a:b;`; trace `x=15`: `x%3==0 && x%5==0` true → prints `A`; switch on float — no (int/char only); `=` (assign, almost-always-true) vs `==` (compare) — THE decision-statement bug.

## Appendix — Windows toolchain (MSYS2 + GCC + CodeBlocks)

Fresh-Windows → C in CMD + Code::Blocks: install MSYS2 (`https://www.msys2.org/`, default `C:\msys64`, UCRT64 env) → `pacman -Syu` (twice, reopen terminal between) → `pacman -S --needed mingw-w64-ucrt-x86_64-gcc mingw-w64-ucrt-x86_64-gdb mingw-w64-ucrt-x86_64-make` → verify `gcc --version`, `which gcc` (`/ucrt64/bin/gcc`) → add `C:\msys64\ucrt64\bin` to user Path → NEW cmd: `gcc --version`, `where gcc`. Test: `gcc hello.c -o hello.exe` → `hello.exe` prints `Hello, C!`. Code::Blocks: point toolchain to `C:\msys64\ucrt64\bin` ("auto-detect" finds it); new console project → build-and-run. Failure order: no `gcc.exe` on disk → wrong MSYS2 folder (`which gcc` tells the truth); CMD "not recognized" → stale terminal (reopen) or Path typo; Code::Blocks "can't find compiler" → toolchain path unset.

## Cross-references

- Depth: [[spm-module1-faculty-companion]] · [[spm-module2-faculty-companion]] · [[module-1-spm-c-basics]] · [[module-2-program-control-functions]]
- Drills: [[spm-practice-bank-module1]] · [[spm-practice-bank-module2]] · [[spm-quiz-bank]]
- Sibling write-ups: [[spm-lab-exp-guides]] · Rubric/schedule: [[lab-ca-and-experiments]] · [[lesson-plan-2026-27]]
