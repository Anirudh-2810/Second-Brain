---
course_code: ENG
course_name: "Semester 2 source map"
unit: "Survey"
tags: [engineering, sem2, source-map]
last_updated: "2026-09-09"
description: "Survey catalog of BTech Semester-2 raw sources: per-subject file trees, inferred topics and syllabus units, notable files flagged, plus recommended ingest order."
---

## For future agent

This is a SURVEY, not an ingest — it catalogs what exists under `raw-sources/drive-download-20260908T190927Z-1-001/Semester 2/` so a future session can ingest subjects in priority order. Filenames only were scanned, except ~5 syllabus/timetable PDFs read fully. Do not treat inferred units as verified syllabus text; confirm against `Semester II Syllabus.pdf` during ingest. Hub: [[01-Areas/Engineering/INDEX]].

## Source root

`raw-sources/drive-download-20260908T190927Z-1-001/Semester 2/` — 10 subject folders + 6 loose files (~171 files total).

Loose files (notable ★):

- ★ `Semester II Syllabus.pdf` — master scheme + all subject syllabi (text extraction failed; likely scanned — read visually at ingest)
- ★ `ESE-TT-MAY-26-FYBTECH+(SVU-2025)-SEM-II-REG_copy.pdf` — ESE timetable: 4 papers only — 07-May-26 OOPM, 11-May-26 AM-II, 13-May-26 Applied Science / Engg Mech, 15-May-26 DLD (all 10:30am–12:30pm)
- ★ `F.Y.+B+Tech_Academic+Calender_2025-2026.pdf` — academic calendar (text extraction failed; read visually at ingest)
- `Div M Roll.pdf` — class roll list (admin, low ingest value)
- `Holiday list - 2026 - SVV and SVU.pdf` — admin, low ingest value
- `Makerspace Sem II.jpg` — read with PBL/Makerspace Lab

Scheme (from OOPM + AM-II syllabus PDFs, SVU R-2025 v3.0): AM-II 4cr (IA20/MSE30/ESE50) · Applied Science 3cr (ESE50) · DLD 3cr (ESE50) · EVS 2cr (CA-only 50) · OOPM 3cr (LabCA50 + onscreen ESE50 incl. coding/viva) · PCS 2cr (CA-only 50) · AS Lab / DLD Lab 1cr each (CA-only) · Makerspace Lab II 1cr (CA50 + PBL project50).

## 1. Maths - II (~48 files — richest folder)

- `AM II SYLLABUS.pdf` ★ + `MSE 2026 MArch Sem -II AM-II solution.pdf` ★ (worked MSE answers)
- `Module 1 Eigenvalues and Eigenvectors/` (9 files): numbered set 1–4 (eigenvalues/vectors, properties, Cayley-Hamilton, similarity of matrices) + overview PDF + LMR 1.1–1.4 + `Principal Component Analysis_ Solved Examples 2.pdf` + `Practice Problems/` (module-1 practice, SVD practice) → likely Unit 1 (12h, CO1: diagonalization, PCA, SVD, matrix functions)
- `Module 2 Successive Differentiation, Expansion of Functions/` (10 files): 8 numbered PDFs (formulae, nth derivative algebraic/trig/De-Moivre, Leibnitz, Taylor, Maclaurin, series problems) + 2 practice sets → likely Unit 2 (6h, CO2)
- `Module 3 Integration Review and Some new Techniques/` (6 files): BETA, GAMMA, DUIS + 3 matching practice sets → likely Unit 3 (8h, CO3)
- `Module 4 Rectification/` (5 files): CURVE TRACING + Cartesian/Parametric/Polar rectification + 1 practice set → likely Unit 4 (4h, CO4)
- `Module 5 Multiple Integrations and their Applications/` (11 files): 10 numbered PDFs (double/triple, change of order, polar/Cartesian-polar, area, volume, change of variable) + 1 practice set → likely Unit 5 (15h, CO5)
- `My notes/` (5 files): Beta and Gamma, Matrices Sem II, Multiple Integration, Rectification, successive — handwritten revision set paralleling Modules 1–5

## 2. Digital Logic Design (~17 files + Mano textbook)

- ★ `(DE) Digital Design, 5th Edition by M. Morris Mano and Michael Ciletti.pdf` — canonical reference
- ★ `DLD pyqs.pdf` + `DLD aug 17 test 1 Solution 23-Aug-2017.pdf` + `DE test paper_1_Aug 14.doc` + `DE test paper_1_Aug 2018.doc` + `DLD Test 1_Repeat_ Paper 18-19.docx` — exam-prep rich
- `Module 1/` (1): `DLD_FY Module 1.pptx` → likely number systems/codes + Boolean basics
- `Module 2/` (4): `DLD_FY Module 2.pptx`, `CHAPTER 2.pptx`, `Boolean problems.pdf`, `Quine McClusky.pptx` → likely Boolean algebra, K-maps, Quine–McCluskey
- `Module 3/` (3): `Module 3.pdf`, `Chapter 3 upto MSE.pdf`, `MUX DECODER.pdf` → likely combinational circuits (mux/demux, decoder/encoder)
- `Module 4/` (1): `Module 4.pdf` → likely sequential circuits (latches, flip-flops, registers, counters)
- `Module 5/` (2): `DLD_FY_Module 5.pptx`, `Module 5.pdf` → likely FSM/state machines and/or memory/PLDs (verify at ingest)

## 3. Object Oriented Programming (~17 files; continues Sem-1 C)

- `Academic data/` (5) ★: `OOPM Syllabus.pdf` (4 units: 1-OOP fundamentals/Booch complexity 5h CO1; 2-classes/objects/constructors 8h CO2; 3-inheritance/polymorphism/binding 7h CO3; 4-packages/exceptions/multithreading/files 10h CO4) + `Lesson plan OOPM.pdf` + `List of Exp OOPM.pdf` + `ESE Pattern_OOPM.pdf` + `LAB CA OOPM.pdf`
- `Books/` (8): Java-heavy — Complete Reference, Balagurusamy Primer, Choudhary/Malhotra OUP, javanotes5, LearnJava, beginner guide, sjcp + `nptel_java.pdf`. Syllabus allows C++/Java/Python, so language is track-dependent — confirm before ingesting examples
- `PPT/` (3): `Module 1.pptx`, `Module 2.pptx`, `Module 3.pdf` — no Module 4 deck (gap: packages/exceptions/threads only in books)
- `mse soln.pdf` ★ — worked MSE answers
- Bridge: OOP builds on Sem-1 C — see [[SPM/syllabus-316U06C107]] for the C baseline (procedural → modular → OOP per Unit 1.1)

## 4. Object Oriented Programming LAB (22 files)

- 11 student write-up PDFs (`Dhruv Jaiswal M1 16014125021 OOPM EXP 1–12`, missing EXP 5) + 11 prompt docx (`LAB 1–12`, incl. `LAB 5 Complete.docx`) — prompts + worked answers pair up experiment-by-experiment
- Read with `Academic data/List of Exp OOPM.pdf` + `LAB CA OOPM.pdf` for the official experiment list and rubric

## 5. Applied Science (~30 files; two tracks)

Syllabus splits by program: Computer & Allied vs Electronics & Allied; MECH/RAI take Engineering Mechanics instead (confirms timetable footnote).

- `Physics/Module 1/` (9): PN-junction diode, MOS + diode applications, BJT transistors, optoelectronic devices + 3 numerical sets + practice Qs → likely Unit 1 semiconductor devices
- `Physics/Module 2/` (7): Quantum Mechanics PDF, quantum-computing lecture, qubit-operations/quantum-gate problems, tunneling & nanomaterials, QM numericals + sample Qs → likely Unit 2 quantum + nanotech
- `Physics/Module 3/` (2): `Electromagnetism_Part 2.PDF`, `PPT on EMT.pdf` → likely Unit 3 electromagnetism
- Loose ★: `Electrodynamics Class notes (Derivations).pdf`, `Quantum Class Notes (Derivations).pdf` — derivation-focused, exam-oriented
- `Chemistry/Module 4/` (7): energy-storage lecture, solid-state batteries, supercapacitors, MEMS, sensors, data-centre heat management, numerical sensitivity → likely Unit 4 energy devices + sensors
- `Chemistry/Module 5/` (2): `Band gap.pdf`, `Device Fabrication.pdf` → likely Unit 5 semiconductor materials/fabrication
- `Chemistry/ASCP Final Question Bank.docx` ★ — consolidated question bank

## 6. Applied Science Lab (~6 files)

- `Phys/Lab Manual_Sem II_Final.pdf` ★ — the official physics lab manual (single authoritative file)
- `Chem/` (5): ZnO-nanoparticle prep, optical-band-gap of cobalt(II) chloride (docx + pdf), EC-pH-metry, `index sem II 26.pdf` (experiment index — read first at ingest)

## 7. Digital Logic Design Lab (10 files)

- Write-ups `DLD EXPT_1/3/4/5/6/8/9/10` + `16014125021_DhruvJaiswal_1-10.pdf` (one student's full 1–10 set, covers gaps) + `Question Bank Practical exam.docx` ★
- Gaps: no standalone write-ups for Expt 2 and 7 (covered only inside the consolidated PDF — verify at ingest)

## 8. PBL / Makerspace Lab II (13 files + photo)

- `Activity 1/` (2): 3D-printer deck + report template → 3D printing
- `Activity 2/` (3): Arduino–sensor interfacing deck + `sensor_codes.docx` + template → sensors
- `Activity 3/` (3): motors deck + `Codes for Motor Interface.docx` + template → motors/actuation
- `Project/` (5): intro deck, week-wise schedule, one-page write-up format, Review-1 and Review-2 templates → the assessed PBL build (50 marks)
- Read `Makerspace Sem II.jpg` (root) with this folder

## 9. Presentation & Communication Skills (2 files — thin)

- `Emotional Intelligence.pdf` + `Emotional_Intelligence.docx` (same content, two formats) — only EI topic present; PCS is CA-only (50) with tutorial hour, so expect more topics (speaking, writing, visuals) from other sources at ingest

## 10. EVS (0 files — empty folder, gap)

- Folder exists but is empty; EVS is CA-only (50 marks, no ESE). Source for environmental-science content elsewhere at ingest — flag as gap

## Recommended ingest order (future session)

1. Maths-II — ESE paper, most complete sources (numbered PDFs + practice + MSE solution + notes); highest marks weight (125 total)
2. DLD — ESE paper; Mano book + PYQs + module decks in order 1→5
3. OOP theory + OOP Lab together — onscreen ESE with coding; resolve implementation language first (Java vs C++ vs Python)
4. Applied Science Physics then Chemistry (CS track) — derivation notes + question bank; confirm track (Computer vs Electronics)
5. AS Lab + DLD Lab — manuals/question banks; pair with parent theory
6. PBL/Makerspace — activities 1→2→3 then project templates; practical, low theory dependency
7. PCS + EVS last — CA-only and sources thinnest/missing; pull fresh material

## Per-folder counts (files only)

| Folder | Files |
|--------|-------|
| Applied Science (Chem 10 + Phys 20) | 30 |
| Applied Science Lab (Chem 5 + Phys 1) | 6 |
| Digital Logic Design (6 loose + 11 module) | 17 |
| Digital Logic Design Lab | 10 |
| EVS | 0 |
| Maths - II (2 loose + 41 module + 5 notes) | 48 |
| Object Oriented Programming (1 + 5 + 8 + 3) | 17 |
| Object Oriented Programming LAB | 22 |
| PBL (2+3+3+5) | 13 |
| Presentation & Communication Skills | 2 |
| Root loose files | 6 |
| **Total** | **~171** |
