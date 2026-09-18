---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "M1 practice bank — Easy 15 + Difficult 15 (CO1)"
tags: [spm, btech, c, module-1, practice, algorithms, flowcharts, sdlc, operators, exam-prep]
last_updated: "2026-09-18"
date: "2026-09-18"
description: "SPM M1 faculty practice bank — all 30 questions verbatim (Easy 15 + Difficult 15) across 1.1-1.5 with worked answers and exam mapping."
---

## For future agent

This note is the verbatim M1 drill registry for SPM 316U06C107 (Easy 15 + Difficult 15, no official key — answers here are worked, confidence high). Theory in [[spm-module1-faculty-companion]] and [[module-1-spm-c-basics]]; timed quiz form in [[spm-quiz-bank]]; M2 drills in [[spm-practice-bank-module2]].

# SPM Practice Bank — Module 1 (30 Q: Easy 15 + Difficult 15)

> Sources: `raw-sources/SPM SEM1 work/Practice questions/Module 1/SPM_Module1_Practice_Questions_Easy.pdf` + `..._difficult.pdf` (F.Y. B.Tech, AY 2026-27, CO1; no marks/CO printed; no answer key) | Syllabus: [[syllabus-316U06C107]] M1

## Easy 15 (warm-up — one per syllabus point)

**1.1 Algorithms & flowcharts:** Q1 write algorithm for rectangle area (length × width). Q2 draw flowchart: positive/negative/zero. Q3 pseudocode for larger of two numbers.

**1.2 Structured programming:** Q4 name the three control structures + one everyday example each (sequence = recipe steps; selection = umbrella if rains; iteration = stirring until dissolved). Q5 what is modular programming + two benefits (reuse, easier debug). Q6 what does single-entry/single-exit mean (one way in, one way out — traceable top-to-bottom).

**1.3 Execution & SDLC:** Q7 list the six SDLC phases in order (Requirement → Design → Implementation → Testing → Deployment → Maintenance). Q8 one compiler-vs-interpreter difference (whole-program-before-run vs line-by-line). Q9 name the stage — (a) object + libraries combined = linking; (b) executable copied to memory = loading; (c) missing semicolon reported = compilation.

**1.4 Headers/data/identifiers:** Q10 four fundamental types + sizes (int 4 `%d`, float 4 `%f`, double 8 `%lf`, char 1 `%c`). Q11 valid identifiers? `roll_no` valid, `1stName` INVALID (starts with digit), `sum` valid, `int` INVALID (keyword). Q12 variable vs constant + example each (`int marks = 40;` changes; `const float PI = 3.14;` fixed).

**1.5 Operators/expressions:** Q13 evaluate — `15 % 4` = 3; `7 / 2` = 3 (integer truncation); `7.0 / 2` = 3.5. Q14 `int x = 5; printf("%d", x++); printf("%d", x);` prints `5` then `6` (post-increment uses old value first). Q15 four arithmetic operators + example (`+ - * /`, `%` often accepted as fifth).

## Difficult 15 (exam-grade — reasoning + traps)

**1.1:** Q1 algorithm + flowchart for quadratic roots covering all three discriminant cases ($D > 0$ distinct, $D = 0$ equal, $D < 0$ complex; $x = (-b \pm \sqrt{D})/2a$). Q2 binary-search pseudocode with loop-continuation condition (`low <= high`) + why the space shrinks (half discarded each pass via `mid`). Q3 rewrite goto-sum (`repeat: ... if i<=n goto repeat`) as structured loop (`while(i<=n){sum+=i;i++;}` — no goto).

**1.2:** Q4 top-down/stepwise decompose "student report card" into a 2-level module hierarchy (input → compute → print sub-modules). Q5 identify jump-into-loop-middle violation (`goto middle` skips init) and rewrite with a structured condition (`if(skipFirst==1) i=2; while(i<=10){...}`).

**1.3:** Q6 team skips reviews/testing to "fix as reported" — skipped phase = Testing; risks: logical errors ship to users, post-deployment fixes cost far more than pre-release ones. Q7 three plausible logical causes for "every bonus prints 0": wrong formula (multiplies by 0), `=` instead of `==` in the eligibility test, integer division truncating the rate to 0. Q8 two files defining the same global function compile clean alone (compiler sees one file at a time) and collide only at link (duplicate symbol — linker merges objects).

**1.4:** Q9 `a.h` + `b.h` both include unguarded `common.h` → double declaration / redefinition error when one source includes both; invisible per-file because each header alone includes it once — fix = include guards. Q10 validity + rule: `_temp` valid; `2ndValue` INVALID (leading digit); `float` INVALID (keyword); `student-marks` INVALID (hyphen); `Total_Sum` valid; `void` INVALID (keyword). Q11 constant for mixed int/float physics use: prefer `const` (typed, checked at every use) over `#define` (untyped text substitution).

**1.5:** Q12 `int a=5,b=2,c; c = a++ + ++b*2 - a--;` → `++b`=3, `3*2`=6, `a++` uses 5 then a=6, `a--` uses 6 then a=5; c = 5+6−6 = 5; final a=5, b=3, c=5. Q13 `(5/2)*2.0` = 2×2.0 = 4.0 (integer division FIRST) vs `5/2*2.0` left-to-right = same 4.0 here — but NOT generally safe to reorder; trace intermediate types to prove it. Q14 `if(0<=x<=10)` parses as `(0<=x)<=10` → `(0 or 1)<=10` → always true; fix: `if(x>=0 && x<=10)`. Q15 with `i=7, f=2.0, ch='A'`: (a) `i/2` = 3, int; (b) `i/f` = 3.5, float/double; (c) `ch+1` = 66 (`'B'`), int; (d) `(int)f + i%2` = 2+1 = 3, int.

## Prep mapping

Easy = recall + direct apply (ESE Q4b theory, Quiz B/C warm-ups). Difficult = analysis + traps (ESE Q4a algorithm design, OST edge cases). Scaffold: identifiers Easy-Q11 ⊂ Difficult-Q10; division Easy-Q13 → Difficult-Q13/Q15; post-increment Easy-Q14 → Difficult-Q12. Timed form: [[spm-quiz-bank]] §M1.

## Cross-references

- Theory: [[spm-module1-faculty-companion]] · [[module-1-spm-c-basics]] · Pattern: [[assessment-guide-ese-ost-quiz]]
- Sibling: [[spm-practice-bank-module2]] · Timed: [[spm-quiz-bank]] · Lab: [[spm-lab-exp1-exp2-guides]]
