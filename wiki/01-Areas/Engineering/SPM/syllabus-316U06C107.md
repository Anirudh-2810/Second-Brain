---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "Syllabus Hub — All Modules 1-4 (30 hrs)"
tags: [spm, syllabus, kjsce, 316U06C107, structured-programming, c-programming, coe-mapping]
last_updated: "2026-09-02"
confidence: high
description: "Official SPM 316U06C107 syllabus hub — 30 hrs across 4 modules, CO1-CO4 mapping, unit breakdown, SDLC to pointers, with sources and wiki page map."
---

## For future agent
This note is the single-source syllabus registry for SPM 316U06C107 (2026-27). It was ingested from [[raw-sources/SPM_Syllabus_316U06C107]] and maps every unit to its CO and to the wiki module pages that teach it. Use it to answer "what's in SPM unit X?" without re-reading the PDF.

# SPM 316U06C107 — Syllabus Hub (30 hrs, 4 Modules)

> Somaiya Vidyavihar University, KJ Somaiya School of Engineering — FY B.Tech (Common to All), Sem I, 2026-27.
> Sources: [[raw-sources/SPM_Syllabus_316U06C107]] · [[raw-sources/SPM_Lesson_Plan_2026-27]] · [[raw-sources/SPM_LAB_CA_2026-27]] · [[raw-sources/SPM_FY_List_Exp_2026-27]] · [[raw-sources/SPM_ESE_Pattern_316U06C107]]
> Existing wiki depth: [[module-1-spm-c-basics]] · [[module-2-program-control-functions]] · [[module-3-arrays]] · [[module-4-user-defined-functions]] · [[c-programming-master-study-guide]] · [[formula-sheet-spm]]

## Course Metadata

| Field | Value |
|-------|-------|
| **Course Code** | 316U06C107 |
| **Credits** | 03 (TH 02 + PRACT 01, TUT 00) |
| **Teaching Scheme** | 04 hrs/week (TH 02 + PRACT 02) |
| **Examination Scheme** | CA 50 + ESE (On-Screen*) 50 + LAB CA 50 = 100 (ESE may include theory + coding + viva) |
| **Prerequisites** | Basic computer ops (OS/file mgmt), logical reasoning, arithmetic/simple algebra |

## Course Outcomes (COs)

| CO | Statement | Primarily Assessed In |
|----|-----------|-----------------------|
| **CO1** | Formulate problem statement and develop logic (algorithm/flowchart/pseudocode) | M1, EXP1, OST, ESE Q4a |
| **CO2** | Demonstrate use of control structures (branching + looping) | M2, EXP2-3, OST, ESE Q3 |
| **CO3** | Apply concepts of arrays and strings | M3, EXP4-5, Assignment1, OST |
| **CO4** | Design modular programs using functions, structures, pointers | M4, EXP6-8, Assignment2, Quiz, ESE |

## Module Map — 30 hrs

| Module | Title | Hrs | CO | Units (from syllabus) | Wiki Pages |
|--------|-------|-----|----|------------------------|------------|
| **1** | Introduction to Structured Programming Methodology | 05 | CO1 | 1.1 Problem solving (definition, algorithms, flowcharts, pseudocode) · 1.2 Structured Programming · 1.3 Program execution, SDLC · 1.4 Header files / packages / namespaces, Data & Operators (types, identifiers, constants, variables) · 1.5 Operators, Expressions, Evaluation, Precedence/Associativity, Type Conversions | [[module-1-spm-c-basics]] (§1.1-1.7 SDLC+compile+memory) · [[c-programming-master-study-guide#14-operators--precedence]] (precedence ladder) · [[formula-sheet-spm#2-data-types--format-specifiers]] (types) |
| **2** | Program Control Functions | 06 | CO2 | 2.1 Decision/Multiway Branching · 2.2 Looping, Flag Concept, Counting Loops · 2.3 Documentation & Readable Code | [[module-2-program-control-functions]] (full: if/switch/while/for/break/continue/goto) · [[c-programming-master-study-guide#2-control-flow]] |
| **3** | Introduction to Arrays | 07 | CO3 | 3.1 1D / Multidimensional Arrays, declaration/init, reading/displaying · 3.2 Character Arrays & Strings: declaring strings, reading/writing chars & strings, operations, implementing handlers from scratch | [[module-3-arrays]] (1D/2D, row-major, search/sort) · [[module-3-strings]] (new: char arrays, string ops from scratch) · [[c-programming-master-study-guide#3-arrays]] |
| **4** | User Defined Functions and Structures | 12 | CO4 | 4.1 UDFs: need, declaration/definition, return values, calls, pass-by-value, recursion, inbuilt string handlers · 4.2 Structures & Unions: declaring/defining, init, accessing members, array of structures · 4.3 Pointers: declaration/init, pointer arithmetic, expressions, pass-by-reference, returning pointers · Self-Learning: Unions, Structure vs Union, File Handling | [[module-4-user-defined-functions]] (UDFs, recursion, fn pointers) · [[module-4-structures-unions-pointers]] (new: structs, unions, pointers, file handling) · [[c-programming-master-study-guide#4-user-defined-functions]] |

**Module 4 note on self-learning:** Unions / Structure vs Union / File Handling are marked as self-learning in the syllabus table footnote — they are examinable and appear in [[lab-ca-and-experiments]] Assignment 2.

## Topic-Level Checklist (use for revision)

- **M1.1-1.2:** algorithm vs flowchart vs pseudocode symbols (terminator/process/decision/I-O) — see [[module-1-spm-c-basics#11-software-development-life-cycle-sdlc--master-flowchart]]
- **M1.3:** SDLC phases + Waterfall/V/Spiral/Agile trade-offs
- **M1.4:** `#include` vs `""`, header guards, data types/sizes, `sizeof`, identifiers vs keywords
- **M1.5:** all 5 operator families, precedence/associativity table, implicit vs explicit casts, promotion rules
- **M2.1-2.2:** `if-else` ladder vs `switch` (integral only, fall-through), `for` exact steps, flag/counter loops, `continue` jumps to update (for) vs condition (while)
- **M2.3:** indentation, comments, meaningful names — rubric item in lab write-ups
- **M3.1:** `a[i]` address `B+i*S`, 2D `B+(i*C+j)*S` row-major vs `B+(j*R+i)*S` col-major, partial init zero-fill
- **M3.2:** `char s[]` vs `char *s`, `'\0'` terminator, `strlen/strcpy/strcat/strcmp` from scratch vs library
- **M4.1:** prototype vs definition, pass-by-value copies, recursion stack frames, tail recursion, string handlers
- **M4.2:** `struct` vs `union` memory layout, dot vs arrow, array of structs
- **M4.3:** `&`/`*`, pointer arithmetic scaled by `sizeof`, pass-by-reference via address, `malloc/free`, returning pointers safety, File I/O (`fopen/fclose/fread/fwrite/fprintf`)

## Cross-References & Learning Path

**Recommended order:** [[syllabus-316U06C107]] (this page) → [[lesson-plan-2026-27]] (week timeline) → [[module-1-spm-c-basics]] → [[module-2-program-control-functions]] → [[module-3-arrays]] → [[module-3-strings]] → [[module-4-user-defined-functions]] → [[module-4-structures-unions-pointers]] → [[c-programming-master-study-guide]] (cram) → [[formula-sheet-spm]] (syntax) → [[assessment-guide-ese-ost-quiz]] (exam patterns) → [[lab-ca-and-experiments]] (lab execution)

**Bridges:** C craft feeds [[01-Areas/Programming/INDEX]] (DSA/OOP), memory model feeds [[01-Areas/Programming/cs50/week-4-memory]], robotics uses C pointers in `engineering/robotics/`.

## Recommended Books (as listed in syllabus)

1. Busbee, Programming Fundamentals — Modular Structured Approach using C++
2. Forouzan/Afyouni, CS Structured Approach Using C (4th, Cengage 2023)
3. Forouzan/Gilberg, CS Structured Approach Using C++ (2nd, Cengage 2012)
4. Balagurusamy, Programming in ANSI C (8th, McGraw-Hill 2019)
5. Dey/Ghosh, Structured Programming Approach (Oxford 2016)
6. Links: Rebus Structured Programming · TFETimes PDF · OpenUMN 144 · NPTEL C (noc22_cs40) · NPTEL C++ (noc21_cs02)

*Related indexes:* [[01-Areas/Engineering/INDEX]] · [[Roadmaps/INDEX]]
