---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "Assessment Guide — ESE 50 + OST 15 + Quiz 15"
tags: [spm, assessment, ese, ost, quiz, exam-pattern, 316U06C107]
last_updated: "2026-09-02"
confidence: high
description: "SPM assessment guide — ESE 50 marks on-screen pattern (Sec A/B, Q1-Q4b), OST 15 and Quiz 15 breakdowns, marking tactics and prep order by CO."
---

## For future agent
This page is the exam-pattern decoder for SPM 316U06C107, distilled from [[raw-sources/SPM_ESE_Pattern_316U06C107]] and [[raw-sources/SPM_LAB_CA_2026-27]]. Use it to answer "what's the ESE/OST/quiz pattern?" or to build a revision plan. It links every question type to the wiki module that teaches it.

# SPM Assessment Guide — ESE 50 + OST 15 + Quiz 15

> Sources: [[raw-sources/SPM_ESE_Pattern_316U06C107]] · [[raw-sources/SPM_LAB_CA_2026-27]] · [[raw-sources/SPM_Syllabus_316U06C107]]
> Lab CA total: [[lab-ca-and-experiments#1-distribution-of-lab-ca-50-marks]] | Timeline: [[lesson-plan-2026-27]]

## 1. ESE 50 Marks — On-Screen* Pattern

> *Per syllabus cover: ESE on-screen may include theory + practical coding tasks + oral/viva

**Total: 50 marks, two sections of 25 each**

| Section | Q | Type | Marks | Options | What It Tests |
|---------|---|------|-------|---------|---------------|
| **A** (25) | **Q1** | Practical/theory mix | **10** | **Attempt 1 out of 2** | Typically one program to write/trace (CO1-CO3) |
| | **Q2** | Practical/theory mix | **15** | **Attempt 1 out of 2** | Longer program or array/string + logic (CO2-CO3) |
| **B** (25) | **Q3** | **Complete the Code** | **10** | **Compulsory, no option** | Fill missing statements/logic — predict output variant |
| | **Q4a** | **Algorithm / Flowchart / Pseudocode** | **5** | **Compulsory, no option** | Draw/write logic for a problem (CO1) |
| | **Q4b** | **Theory** | **10** | **Attempt 2 out of 3** | SDLC, memory, precedence, documentation, structure vs union, etc. |

**Marking flow to expect (on-screen):**
- Q1/Q2 code judged on **correctness + structured logic + output** (mirrors OST rubric: 10 code/output)
- Q4a judged on **algorithm steps + flowchart symbols** (parallelogram for I/O, diamond for decision, etc.)
- Viva (if conducted) probes **why** — e.g., why row-major `B+(i*C+j)*S`, why `continue` jumps to update in `for`.

### Prep by CO

| CO | Highest-yield targets for ESE | Wiki drill pages |
|----|-------------------------------|------------------|
| CO1 | SDLC models, flowchart symbols, operator precedence table, type conversion | [[module-1-spm-c-basics]] · [[c-programming-master-study-guide#11-preprocessor-pipeline]] |
| CO2 | `switch` fall-through, `for` exact steps, flag loops, `continue` vs `break` in `while` | [[module-2-program-control-functions]] |
| CO3 | 1D/2D address formulas, string `'\0'` trap, implement `strlen` from scratch | [[module-3-arrays]] · [[module-3-strings]] |
| CO4 | Pass-by-value vs pointer, `struct` vs `union` (size/layout), file handling `fopen` modes | [[module-4-user-defined-functions]] · [[module-4-structures-unions-pointers]] |

### Time Strategy (50 marks)

- **Q4a (5m, compulsory):** do first — flowchart is fastest marks.
- **Q3 (10m, compulsory):** second — completing code is bounded.
- **Q4b (10m, 2/3):** pick the two you can diagram (SDLC, memory layout score quickly).
- **Q1/Q2 (25m combined):** write one clean program per question, trace one example hand-run in the answer.

## 2. OST — 15 Marks (On-Screen Test, Modules 1–3)

Already detailed in [[lab-ca-and-experiments#4-ost--15-marks-ost-modules-13]] — key recap:

- **When:** MSE week **26–30 Oct 2026** (Week 11), Duration **45 min coding + 15 min upload**
- **Pattern:** Any **1 out of 2** programs → **10 marks Code & Output + 5 marks Algorithm Writing**
- **Scope:** **Modules 1, 2, 3 only** — no functions/structures/pointers
- **Expected problems:** M1 operators + M2 branching/looping + M3 arrays/strings (e.g., "Read array, find second largest using flag loop" or "Implement string length without `strlen`")

**OST tactics:**
1. Write **pseudocode first** on paper (that's the 5-mark algorithm even if upload is code-only).
2. Test with two inputs (normal + edge like empty/single-element).
3. Name algorithm steps exactly as in [[module-1-spm-c-basics#10-what-is-a-program--the-beginners-foundation]] — faculty look for keywords.

## 3. Quiz — 15 Marks (All Modules, 20 Minutes)

Per [[raw-sources/SPM_LAB_CA_2026-27]] — **3 equal parts, 5 marks each:**

| Part | Type | Time hint | What wins |
|------|------|-----------|-----------|
| **A** | **Code Debugging** | ~7 min | Find compile/logic errors: missing `&` in `scanf`, `=` vs `==`, missing `break`, off-by-one, missing `'\0'` |
| **B** | **Complete the Code** | ~7 min | Fill 2-4 missing lines: loop condition, array bound, `*p` vs `p`, `fopen` mode |
| **C** | **Predict the Output** | ~6 min | Trace with table — flag `switch` fall-through, `continue` in `for` vs `while`, recursion unwind |

**When:** **30 Nov–4 Dec 2026** (Week 16, revision week) — see [[lesson-plan-2026-27]]
**Scope:** **Entire syllabus including self-learning** (unions, file handling)

**Quiz drill kit:**
- [[formula-sheet-spm#4-control-flow]] (if/switch/for traps)
- [[formula-sheet-spm#10-common-errors-the-marking-scheme-hunts-these]] (the exact errors quizzes use)
- [[c-programming-master-study-guide#appendix-one-page-formula--trap-sheet]] (trap sheet)
- Run timed: **20 min for 3 questions = ~6-7 min each — practice with a timer**.

## 4. Lab CA ↔ Theory CA Relationship

- **Lab CA 50** (this page + [[lab-ca-and-experiments]]) covers **practical evidence**: experiments, OST, quiz, attendance.
- **Theory CA 50** + **ESE 50** (this page §1) cover **written/on-screen demonstration**.
- Combined total per syllabus: **100** (50 CA + 50 ESE) + **50 LAB CA** tracked separately — confirm with your class coordinator if your portal shows them merged.

*Related:* [[syllabus-316U06C107]] · [[lesson-plan-2026-27]] · [[lab-ca-and-experiments]] · [[01-Areas/Engineering/INDEX]]
