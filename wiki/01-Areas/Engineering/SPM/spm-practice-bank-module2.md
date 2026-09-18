---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "M2 practice bank — Easy 15 + Difficult 15 (CO2)"
tags: [spm, btech, c, module-2, practice, branching, loops, patterns, number-theory, exam-prep]
last_updated: "2026-09-18"
date: "2026-09-18"
description: "SPM M2 faculty practice bank — all 30 questions verbatim (Easy 15 + Difficult 15, constructs up to M2 only) with solution sketches and topic index."
---

## For future agent

This note is the verbatim M2 drill registry for SPM 316U06C107 (Easy 15 + Difficult 15; constraint: NO arrays/functions/recursion; no official key — sketches here are worked, confidence high). Theory in [[spm-module2-faculty-companion]] and [[module-2-program-control-functions]]; timed quiz form in [[spm-quiz-bank]]; M1 drills in [[spm-practice-bank-module1]].

# SPM Practice Bank — Module 2 (30 Q: Easy 15 + Difficult 15)

> Sources: `raw-sources/SPM SEM1 work/Practice questions/Module 2/SPM_Module2_Practice_Questions_Easy.pdf` + `..._difficult.pdf` (F.Y. B.Tech, AY 2026-27, CO2; no marks/CO printed; no answer key) | Syllabus: [[syllabus-316U06C107]] M2

## Easy 15 (single-construct fluency)

**2.1 Branching Q1–Q8:** Q1 divisible by 5 (`n%5==0`). Q2 uppercase check (`ch>='A' && ch<='Z'`). Q3 10% discount above Rs 500 else unchanged. Q4 senior-citizen discount (age ≥ 60). Q5 smaller of two via if-else. Q6 multiple of 3. Q7 pass/fail at 35 marks. Q8 ladder vs 100 (greater/less/equal).

**2.2 Loops Q9–Q15:** Q9 evens 1–20 (`for`, `i+=2` or `i%2==0`). Q10 10→1 countdown (`while`). Q11 sum of first 10 evens (loop + accumulate; 2+…+20 = 110). Q12 squares 1–5 (1 4 9 16 25). Q13 print "Welcome" 3× (`do-while`). Q14 count numbers 1–50 divisible by 6 (counter pattern — `⌊50/6⌋` = 8). Q15 total of 5 subject marks (running-total loop).

## Difficult 15 (multi-condition + algorithmic loops)

**2.1 Branching Q1–Q8:** Q1 quadrant from (x,y) — zero coordinate = axis/origin, handled BEFORE quadrant assignment. Q2 classify char (upper/lower/digit/special) via ASCII ranges ONLY, no `ctype.h` (`'A'-'Z'`, `'a'-'z'`, `'0'-'9'`). Q3 CGPA validation-then-ladder: reject outside 0–10 first; then ≥9.0 Distinction, ≥7.5 First, ≥6.0 Second, ≥5.0 Pass, else Fail. Q4 speeding fine in three excess tiers (1–10 A, 11–25 B, >25 C) PLUS independent seatbelt penalty (two separate `if`s — tier ladder + flat add-on). Q5 two-stage bill: amount-tier discount (0/10/15%) THEN 5% member discount applied sequentially on the reduced price. Q6 triangle type from sides only: longest side $c$ — $c^2$ vs $a^2+b^2$ (< acute, = right, > obtuse). Q7 courier charge: base ≤5 kg + per-kg excess surcharge, PLUS flat long-distance fee if >500 km. Q8 4-digit lock with nested if-else ONLY, reporting WHICH digit(s) mismatch (four separate single digits, not one number).

**2.2 Loops Q9–Q15:** Q9 hollow right triangle (star at first/last position per row, final row solid). Q10 alternating series $1-2+3-4+\dots$ to N (sign-flip variable each pass). Q11 GCD by loop, no recursion (count down from min, first common divisor). Q12 second-largest of N inputs tracking top-two variables only, no array. Q13 Pythagorean triplets $a^2+b^2=c^2$ ≤ N (triple nested loop + test). Q14 $e^x \approx 1 + x + x^2/2! + \dots$ summed term-by-term in a loop. Q15 Disarium check ($135 = 1^1+3^2+5^3$; position counted from the left starting 1).

## Scaffolding (Easy → Difficult)

Uppercase Easy-Q2 → ASCII-classify Difficult-Q2. Ladder Easy-Q8 → CGPA Difficult-Q3 (validation + 5 bands). Single-`if` discounts Easy-Q3/Q4 → two-stage modifiers Difficult-Q4/Q5/Q7. Basic `for`/`while` Easy-Q9–Q15 → algorithmic loops Difficult-Q10–Q15 (series, GCD, triplets, Taylor, Disarium). Triangles/patterns bridge to M3 loops-over-arrays in [[module-3-arrays]].

## Cross-references

- Theory: [[spm-module2-faculty-companion]] · [[module-2-program-control-functions]] · Flags/counting: [[spm-module2-faculty-companion#2-flags-and-counting-loops-22--the-two-named-patterns]]
- Sibling: [[spm-practice-bank-module1]] · Timed: [[spm-quiz-bank]] · Lab: [[spm-lab-exp1-exp2-guides]] · Pattern: [[assessment-guide-ese-ost-quiz]]
