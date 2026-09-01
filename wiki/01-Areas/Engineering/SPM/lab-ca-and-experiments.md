---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "Laboratory — CA 50 Marks + 10 Experiments (EXP1-8 + Assignments)"
tags: [spm, lab, ca, experiments, 316U06C107, rubric, attendance, ost, quiz]
last_updated: "2026-09-02"
confidence: high
description: "SPM lab CA 50 marks breakdown — experiments & assignments rubric (logic/debug/write-up/timeliness), attendance table, OST/quiz details, and EXP1-8 schedule with CO/PO mapping."
---

## For future agent
This page is the lab execution manual for SPM 316U06C107. It combines [[raw-sources/SPM_LAB_CA_2026-27]] (marks + rubrics) and [[raw-sources/SPM_FY_List_Exp_2026-27]] (10 experiments). Use it to answer any CA, attendance, write-up, or experiment-requirement question. Timeline source: [[lesson-plan-2026-27]].

# SPM Lab — CA 50 Marks + Experiments

> Sources: [[raw-sources/SPM_LAB_CA_2026-27]] · [[raw-sources/SPM_FY_List_Exp_2026-27]] · [[raw-sources/SPM_Lesson_Plan_2026-27]] | Syllabus: [[syllabus-316U06C107]] | Assessment: [[assessment-guide-ese-ost-quiz]]

## 1. Distribution of Lab CA (50 Marks)

| # | Component | Period | Marks | Detail |
|---|-----------|--------|-------|--------|
| 1 | **Laboratory Experiments & Assignments** (EXP1-8 + Assignment 1, 2) | Aug–Nov 2026 | **15** | Rubric §2 below |
| 2 | **Theory & Lab Attendance** | Entire semester | **5** | Table §3 |
| 3 | **On-Screen Test (OST)** — Modules 1,2,3 | MSE week **26–30 Oct 2026** | **15** | 45 min coding + 15 min upload; 1/2 programs |
| 4 | **Quiz** — Entire syllabus | **30 Nov–4 Dec 2026** | **15** | 20 min; Debug 5 + Complete 5 + Predict Output 5 |

> All 50 are **LAB/TUT CA** per the syllabus cover — ESE 50 is separate (see [[assessment-guide-ese-ost-quiz#ese-50-marks]]).

## 2. Laboratory Experiments & Assignments (15 Marks) — Rubric

Weighted: **Logic 35% + Debug 15% + Write-up 30% + Timely 20% = 15**

### Program Logic & Implementation Correctness (35% → 5.25 marks)
| Level | Descriptor |
|-------|------------|
| **L4** | Correct on first attempt; efficient, structured logic |
| **L3** | Correct after minor debugging |
| **L2** | Partially correct with notable errors |
| **L1** | Incorrect or does not execute |

### Debugging (15% → 2.25 marks)
| Level | Descriptor |
|-------|------------|
| L4 | Handles edge cases + runtime errors independently |
| L3 | Handles common errors with minor help |
| L2 | Basic error handling only |
| L1 | Cannot debug/handle errors |

### Write-ups (30% → 4.5 marks)
| Level | Descriptor |
|-------|------------|
| **L4** | Complete write-up with **handwritten algorithm/pseudocode + faculty signature** |
| L3 | Complete without handwritten component/signature |
| L2 | Partial submission |
| L1 | Major mistakes / incomplete |

### Timely Submission (20% → 3 marks)
| Level | Descriptor |
|-------|------------|
| **L4** | On or before due date |
| L3 | Within one week after due |
| L2 | More than one week late |
| L1 | On/before final cut-off only |

**Practical guardrails:** Every EXP requires algorithm/flowchart/pseudocode (M1.1) in the write-up — that's the CO1 evidence. Submit in the lab week per [[lesson-plan-2026-27]] to secure L4 timeliness.

## 3. Attendance Rubric (5 Marks) — No Concessions

| Attendance | Marks |
|------------|-------|
| ≥75% | **5** |
| 75%–64% | 4 |
| 65%–61% | 3 |
| 60%–55% | 2 |
| 54%–50% | 1 |
| <50% | 0 |

> Note on sheet: "Any type of concession will not be considered." Track theory + lab attendance separately but the rubric awards one consolidated 5-mark component.

## 4. OST — 15 Marks (On-Screen Test, Modules 1–3)

- **When:** MSE week **26–30 Oct 2026** (Week 11), per [[lesson-plan-2026-27]]
- **Duration:** **45 min coding + 15 min upload** = 60 min slot
- **Pattern:** Any **1 out of 2** given programs
  - **10 marks** — Code & Output (correctness + observed output)
  - **5 marks** — Algorithm Writing (handwritten-style logic)
- **Syllabus scope:** Modules **1, 2, 3 only** (no M4 UDFs/structures/pointers)
- **Prep focus:** M1 operators/expressions + M2 branching/looping + M3 arrays/strings — exactly [[module-1-spm-c-basics]] through [[module-3-arrays]] + [[module-3-strings]]

## 5. Quiz — 15 Marks (Entire Syllabus)

- **When:** **30 Nov–4 Dec 2026** (Week 16, revision week)
- **Duration:** **20 minutes**
- **Pattern (3 × 5 marks):**
  1. **Code Debugging (5):** identify & correct error(s) in given snippet
  2. **Complete the Code (5):** fill missing statement(s)/logic
  3. **Predict the Output (5):** trace code and write exact output
- **Scope:** **All modules 1–4 + self-learning** (unions, file handling)
- **Drill resource:** [[assessment-guide-ese-ost-quiz#quiz--15-marks]] + [[c-programming-master-study-guide#appendix-one-page-formula--trap-sheet]] (trap sheet) + [[formula-sheet-spm]] (syntax)

## 6. List of Experiments — 10 Items (EXP1-8 + 2 Assignments)

Per [[raw-sources/SPM_FY_List_Exp_2026-27]] — Dept. of Science and Humanities, Programming Lab I/II.

| Sr | Experiment | CO | PO | Lab Week (per [[lesson-plan-2026-27]]) | Teaches |
|----|------------|----|----|----------------------------------------|---------|
| **1** | Demonstrate **data types and operators** | CO1 | 1 | **W3** (31 Aug–4 Sep) | `int/float/char`, `sizeof`, arithmetic/relational/logical/bitwise, precedence |
| **2** | Demonstrate **decision making & branching** | CO2 | 1,2,3,4,5 | **W4** (7–11 Sep) | `if-else`, `switch`, nested branching, `break` |
| **3** | Demonstrate **looping control structures** | CO2 | 1,2,3,4,5 | **W5** (14–18 Sep) | `for/while/do-while`, `continue/break`, flag/counter |
| **4** | Demonstrate **arrays** | CO3 | 1,2,3,4,5 | **W7** (28 Sep–2 Oct) | 1D init/traversal, 2D row-major, search/sort basics |
| **5** | Demonstrate **strings & string handling** | CO3 | 1,2,3,4,5 | **W8** (5–10 Oct) | `char[]`, `'\0'`, `strlen/strcpy/strcat/strcmp`, from-scratch impl |
| **6** | **Assignment 1** | CO1,2,3 | 1,2,3,4,5,8 | **W9** (12–16 Oct) | Integrated M1+M2+M3 problems |
| **7** | Implement **user defined functions** | CO4 | 1,2,3,4,5 | **W10** (19–23 Oct) | Prototypes, pass-by-value, recursion |
| **8** | Demonstrate **structures and unions** | CO4 | 1,2,3,4,5 | **W12** (2–6 Nov) | `struct`/`union`, array of structs, member access |
| **9** | Demonstrate **pointer** | CO4 | 1,2,3,4,5 | **W14** (16–20 Nov) | `&`/`*`, pointer arithmetic, pass-by-reference |
| **10** | **Assignment 2** | CO4 | 1,2,3,4,5,8 | **W15** (23–27 Nov) | Integrated M4 (incl. self-learning file handling) |

**Buffer weeks:** W6 (21–25 Sep) and W16 (30 Nov–4 Dec) — use for clearing backlogs.
**Submission:** Handwritten algorithm/pseudocode + faculty signature required for L4 write-up. TW marksheet deadline **08 Dec 2026**.

## 7. Quick Checklist (copy into daily notes)

```md
- [ ] EXP1-5 write-ups signed (CO1-3)
- [ ] Assignment 1 submitted (W9)
- [ ] OST ready: M1-3 mock (45 min coding + algorithm) — before 26 Oct
- [ ] EXP6-8 write-ups signed (CO4)
- [ ] Assignment 2 submitted (W15) — includes file handling
- [ ] Quiz drills: debug / complete / predict (W16)
- [ ] All TW sheets bound for 08 Dec submission
```

*Related:* [[syllabus-316U06C107]] · [[lesson-plan-2026-27]] · [[assessment-guide-ese-ost-quiz]]
