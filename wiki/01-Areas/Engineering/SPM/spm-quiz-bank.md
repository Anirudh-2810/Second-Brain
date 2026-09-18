---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "Quiz bank — M1 + M2 timed sets (15 + 15, Debug/Complete/Predict)"
tags: [spm, btech, c, quiz, debugging, output-prediction, complete-the-code, ost-prep, exam-prep]
last_updated: "2026-09-18"
date: "2026-09-18"
description: "SPM faculty quiz bank — both 15-mark timed sets verbatim (Debug 5 + Complete 5 + Predict 5) with worked answers for OST and quiz-week prep."
---

## For future agent

This note is the timed-quiz registry for SPM 316U06C107 — both faculty sets verbatim with worked answers (official key is faculty-discussed in class, not published; answers here are worked, confidence high). Same Debug/Complete/Predict shape as the real Quiz 15 and OST per [[assessment-guide-ese-ost-quiz]]. Untouched theory in [[spm-module1-faculty-companion]] / [[spm-module2-faculty-companion]]; untimed drills in [[spm-practice-bank-module1]] / [[spm-practice-bank-module2]].

# SPM Quiz Bank — M1 + M2 Timed Sets (30 Q)

> Sources: `raw-sources/SPM SEM1 work/QUIZ Practice Questions/Module 1.pdf` + `Module 2.pdf` (each: Section A Debug 5 + B Complete 5 + C Predict 5 = 15 marks, 20 min per [[lab-ca-and-experiments]]) | Pattern: [[assessment-guide-ese-ost-quiz]]

## M1 set (types, operators, conversions)

**A — Debug (pick + fix):** Q1 `z = x/y` with ints → (b): integer division first, stores 2.000000 not 2.5; fix `(float)x/y`. Q2 `int main ()` missing `{` → (a). Q3 average into `int avg` with `%d` → (b): decimal truncated AND wrong specifier; fix `float avg` + `%f`. Q4 `unsigned x = 5; x = x-10;` → (b): underflow wraps to huge positive. Q5 `0.1+0.2` with `%.20f` → (b): prints ~0.30000001192…, binary FP inexactness.

**B — Complete:** Q6 `area = length * breadth;`. Q7 `remainder = num % 5;`. Q8 `runRate = (float)totalRuns / oversPlayed;` (cast BEFORE division). Q9 `larger = (a > b) ? a : b;` (ternary only). Q10 `result = (q > r) && (p > q);` → (3>2)&&(5>3) = 1 ✓.

**C — Predict:** Q11 `15/4, 15%4` → (a) `3 3`. Q12 `y=x++; y=y+x;` (x=5) → y=5 then x=6, y=11 → prints `6 11`. Q13 `a/b, a/c, (float)a/b` (5,2,2.0) → (a) `2 2.50 2.50`. Q14 `'B'+1` as `%d` then `%c` → `67C`. Q15 `2+3*4-(2+3)%4` = 14−1 → (b) `13`.

M1 trap cluster: int-division-before-float (A1/A3/C13/B8 — four faces of one rule), FP representation (A5), unsigned wrap (A4), pre/post-increment (C12).

## M2 set (branching + loops)

**A — Debug (line + fix):** Q1 `if (x=5)` → line 3 (b); fix `if (x == 5)`. Q2 `for(...);` stray semicolon → line 3 (b); delete the `;`. Q3 switch prints "Grade AGrade B" → `break;` missing after `printf("Grade A");` (b); insert `break;`. Q4 triangle row 1 prints zero stars → inner line (a); fix `j<i` → `j<=i`. Q5 `continue` before `i++` loops forever at 3 → the `if(i==3) continue;` line; `i++` never runs so the condition never changes.

**B — Complete:** Q6 `if (num < 0)`. Q7 `for(i=1; i<=10; i++)`. Q8 `case 3:`. Q9 inner `for(j=1; j<=i; j++)`. Q10 missing `n /= 10;` (digit stripped each pass or loop never ends).

**C — Predict:** Q11 x=45 ladder → (c) `C`. Q12 sum 2+4+…+10 → `30`. Q13 inner `break` at j==2 → (a) `11 21 31`. Q14 `switch(2)` no break on case 2 → (b) `BC`. Q15 odd-sum 1+3+5 via `continue` → `9`.

M2 trap cluster: `=`/`==` (A1), stray `;` (A2), fall-through (A3/C14), off-by-one bounds (A4/B9), `continue`-skips-update (A5/C15).

## How to use

20-minute timer, one set, no notes — mirrors quiz week (30 Nov–4 Dec, all modules) and OST Debug/Complete/Predict muscle per [[lab-ca-and-experiments]]. Miss patterns point back: M1 misses → [[spm-module1-faculty-companion]] §5–§6; M2 misses → [[spm-module2-faculty-companion]] §1–§3; fluency gaps → [[spm-practice-bank-module1]] / [[spm-practice-bank-module2]].

## Cross-references

- Theory: [[spm-module1-faculty-companion]] · [[spm-module2-faculty-companion]] · [[module-1-spm-c-basics]] · [[module-2-program-control-functions]]
- Drills: [[spm-practice-bank-module1]] · [[spm-practice-bank-module2]] · Lab: [[spm-lab-exp1-exp2-guides]]
