---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "Syllabus Hub — All Modules 1-4 (30 hrs)"
tags: [spm, syllabus, kjsce, 316U06C107, structured-programming, c-programming, coe-mapping]
last_updated: "2026-10-01"
confidence: high
description: "Official SPM 316U06C107 syllabus hub — 30 hrs across 4 modules, CO1-CO4 mapping, unit breakdown, SDLC to pointers, with sources and wiki page map."
---

## For future agent
This note is the single-source syllabus registry for SPM 316U06C107 (2026-27). It was ingested from [[raw-sources/SPM_Syllabus_316U06C107]] and maps every unit to its CO and to the wiki module pages that teach it. Use it to answer "what's in SPM unit X?" without re-reading the PDF.

**Verified against the official PDF 2026-10-01** (`raw-sources/SPM Lecture/SPM_Syllabus.pdf` and the root copy). All metadata matches the earlier `.md` extraction — code, title, credits (03), teaching scheme (04 hrs), CA 50 / ESE 50 / LAB CA 50, the 05/06/07/12 hour split totalling 30, and all four COs. The only correction is the **unit wording**, which the earlier `.md` had paraphrased. The verbatim official wording is now in the module map below — use those strings when matching a question to a unit, since exams are set from the official text.

**One wording subtlety worth remembering:** unit **1.1 is officially "Problem solving *skill development*"**, and the 5 sub-items are Problem Definition, fundamentals of algorithms and flowcharts, Program Design, **Pseudocode** — the same five headings the superseded AY 2025-26 Topic 1.1 deck used as its index.

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

**Unit wording below is verbatim from the official syllabus PDF** (verified 2026-10-01). The "Wiki pages" column routes each unit to the page that teaches it.

| Module | Title | Hrs | CO | Units (verbatim from syllabus) | Wiki Pages |
|--------|-------|-----|----|------------------------|------------|
| **1** | Introduction to Structured Programming Methodology | 05 | CO1 | **1.1** Problem solving *skill development*: Problem Definition, fundamentals of algorithms and flowcharts, Program Design, Pseudocode · **1.2** Structured Programming · **1.3** Program execution process, Systems Development Life Cycle · **1.4** Understanding concept and importance of header file/package/namespaces; Data & Operators: Data Types, Identifier, Constants and Variables · **1.5** Types of Operators, Expressions and Evaluation of Expressions, Operator Precedence and Associativity, Type Conversions | [[module-1-spm-c-basics]] (§1.1-1.7 SDLC+compile+memory) · [[spm-module1-faculty-companion]] (PPT wording, quick-tests, **§6a bitwise is out of scope**, §6b superseded AY 2025-26 deck) · [[c-programming-master-study-guide#14-operators--precedence]] · [[formula-sheet-spm#2-data-types--format-specifiers]] |
| **2** | Program Control Functions | 06 | CO2 | **2.1** Decision Making and Branching Control Structures: Two Way Selection, Multiway Selection · **2.2** Looping Control Structures, **Flag Concept, Counting Loops** · **2.3** **Documentation and Making Source Code Readable** | [[module-2-program-control-functions]] (§1.7 flag, §1.8 counting loops, §1.9 documentation, §1.10 trace tables — added 2026-10-01) · [[spm-module2-faculty-companion]] · [[c-programming-master-study-guide#2-control-flow]] |
| **3** | Introduction to Arrays | 07 | CO3 | **3.1** Arrays: Introduction to One Dimensional Arrays, Multidimensional Arrays, Declaration and Initialization of Arrays, Reading and Displaying arrays · **3.2** Character Arrays and Strings: Introduction, Declaring and Initializing String Variables, Reading Character and Writing Character, Reading and Writing Strings, various operation on strings, **Implementation of string handling operations (from scratch)** | [[module-3-arrays]] (dedicated arrays page) · [[module-3-strings]] (dedicated strings page + **strcpy exam drill**) · [[module-3-arrays-strings]] (module hub / routing) · [[spm-lab-exp3-4-5-guides]] (EXP4+5) · [[c-programming-master-study-guide#3-arrays]] |
| **4** | User Defined Functions and Structures | 12 | CO4 | **4.1** User Defined Functions: Need, Function Declaration and Definition, Return Values, Function Calls, Passing Arguments to a Function by Value, Recursive functions, String Handling Functions (inbuilt) · **4.2** Structures and Unions: Introduction, Declaring and defining Structure, Structure Initialization, Accessing and Displaying Structure Members, Array of Structures · **4.3** Introduction to pointers: Pointer declaration and initialization, Pointer addition and subtraction, evaluating pointer expressions; Pointers and Functions: Pass by Reference, Returning pointers from functions · Self-Learning: Unions, Structure vs Union, File Handling | [[module-4-user-defined-functions]] (UDFs, recursion) · [[module-4-structures-unions-pointers]] (structs, unions, pointers, file handling) · [[c-programming-master-study-guide#4-user-defined-functions]] |


**Module 4 note on self-learning:** Unions / Structure vs Union / File Handling are marked as self-learning in the syllabus table footnote — they are examinable and appear in [[lab-ca-and-experiments]] Assignment 2.

## Topic-Level Checklist (use for revision)

- **M1.1-1.2:** algorithm vs flowchart vs pseudocode symbols (terminator/process/decision/I-O) — see [[module-1-spm-c-basics#11-software-development-life-cycle-sdlc--master-flowchart]]
- **M1.3:** SDLC phases + Waterfall/V/Spiral/Agile trade-offs
- **M1.4:** `#include` vs `""`, header guards, data types/sizes, `sizeof`, identifiers vs keywords
- **M1.5:** all 5 operator families, precedence/associativity table, implicit vs explicit casts, promotion rules
- **M2.1-2.2:** `if-else` ladder vs `switch` (integral only, fall-through), `for` exact steps, flag/counter loops, `continue` jumps to update (for) vs condition (while)
- **M2.3:** indentation, comments, meaningful names — rubric item in lab write-ups
- **M3.1:** `a[i]` address `B+i*S`, 2D `B+(i*C+j)*S` row-major vs `B+(j*R+i)*S` col-major, partial init zero-fill, nested loops, cache-friendly loop order → [[module-3-arrays-strings#3-2d-arrays-multidimensional--matrices]]
- **M3.2:** `char s[]` vs `char *s`, `'\0'` terminator, `strlen/strcpy/strcat/strcmp` from scratch vs library, `fgets` vs `scanf("%s")`, **`strcpy` exam drill** → [[module-3-arrays-strings#7-strcpy--the-dedicated-drill]] and [[module-3-arrays-strings#5-string-operations-from-scratch-the-syllabus-requirement]]
- **M4.1:** prototype vs definition, pass-by-value copies, recursion stack frames, tail recursion, string handlers
- **M4.2:** `struct` vs `union` memory layout, dot vs arrow, array of structs
- **M4.3:** `&`/`*`, pointer arithmetic scaled by `sizeof`, pass-by-reference via address, `malloc/free`, returning pointers safety, File I/O (`fopen/fclose/fread/fwrite/fprintf`)

## Cross-References & Learning Path

**Recommended order:** [[syllabus-316U06C107]] (this page) → [[lesson-plan-2026-27]] (week timeline) → [[module-1-spm-c-basics]] → [[module-2-program-control-functions]] → [[module-3-arrays]] + [[module-3-strings]] (the two dedicated Module-3 pages; [[module-3-arrays-strings]] is the hub) → [[module-4-user-defined-functions]] → [[module-4-structures-unions-pointers]] → [[c-programming-master-study-guide]] (cram) → [[formula-sheet-spm]] (syntax) → [[assessment-guide-ese-ost-quiz]] (exam patterns) → [[lab-ca-and-experiments]] + [[spm-lab-exp1-exp2-guides]] + [[spm-lab-exp3-4-5-guides]] (lab execution)

**Bridges:** C craft feeds [[01-Areas/Programming/INDEX]] (DSA/OOP), memory model feeds [[01-Areas/Programming/cs50/week-4-memory]], robotics uses C pointers in `engineering/robotics/`.

## Recommended Books (as listed in syllabus)

1. Busbee, Programming Fundamentals — Modular Structured Approach using C++
2. Forouzan/Afyouni, CS Structured Approach Using C (4th, Cengage 2023)
3. Forouzan/Gilberg, CS Structured Approach Using C++ (2nd, Cengage 2012)
4. Balagurusamy, Programming in ANSI C (8th, McGraw-Hill 2019)
5. Dey/Ghosh, Structured Programming Approach (Oxford 2016)
6. Links: Rebus Structured Programming · TFETimes PDF · OpenUMN 144 · NPTEL C (noc22_cs40) · NPTEL C++ (noc21_cs02)

*Related indexes:* [[01-Areas/Engineering/INDEX]] · [[Roadmaps/INDEX]]
