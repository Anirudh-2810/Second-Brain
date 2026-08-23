---
module: "programming"
course: "CS50x — Introduction to Computer Science"
week: 11
topic: "Problem Sets Catalog — CS50 'Suits' with Key Ideas & Skill Mapping"
tags: [programming, computer-science, cs50, harvard, problem-sets, psets, practice, luhn, greedy, ciphers, speller, finance]
last_updated: "2026-08-11"
---

# CS50 Problem Sets — The Full Catalog

> How you *actually* learn the course: each week's lab + problem set "suit" encodes the lectures' ideas as autonomous, graded challenges. `check50` and `submit50` in CS50.dev grade them.
> **Golden rule (Malan):** coachable difficulty beats passive watching — do every PSet, less-comfortable track first.

---

## 1. Quick Reference Table

| PSet / Week | Problems | Core skills exercised |
|---|---|---|
| **PSet 0** | Scratch project | event-driven code, design, storytelling |
| **PSet 1** | Hello · Mario (less/more) · Cash · Credit | loops, `%`, `do-while`, greedy & Luhn math |
| **PSet 2** | Readability · Caesar · Substitution | strings-as-arrays, `ctype.h`, `%` wrap, key validation |
| **PSet 3** | Plurality · Runoff · Tideman | arrays of structs, elimination logic, cycle detection |
| **PSet 4** | Filter · Recover | pointer discipline, structs/RGB, file I/O, `valgrind` |
| **PSet 5** | Speller | hash tables, memory management (`load/check/size/unload`) |
| **PSet 6** | *Week 1–2, 4 problems in Python* + DNA | porting logic, `dict`/`set`, CSV parsing |
| **PSet 7** | Movies · Fiftyville | SQL joins, aggregations, subqueries; forensic reasoning |
| **PSet 8** | Homepage · Trivia | HTML/CSS layout, JS events & DOM |
| **PSet 9** | Finance | full-stack app: routes, sessions, SQL, quotes, buy/sell |
| **PSet 10** | Final Project | everything, synthesis, self-directed scope |

---

## 2. Signature Problems Worth Re-solving

| Problem | Week | Why it's a keeper |
|---|---|---|
| **Mario (more)** | 1 | nested loops; input validation (`do-while`); ASCII art = the "shape think" pattern |
| **Credit** | 1 | *Luhn's algorithm* — string math (`char` → `int`), digit checks, `%` and integer division |
| **Caesar / Substitution** | 2 | string indexing + modulo wrap; validates keys with `ctype.h` |
| **Filter (grayscale/sepia/blur/edges)** | 4 | struct arrays (pixels), nested loops, edge-case index guards |
| **Recover** | 4 | `fopen`-many, byte sniffing, memory + file lifecycle — a real "digital forensics" task |
| **Speller** | 5 | hash table engineering: the *speed × memory* decision is explicit |
| **Fiftyville** | 7 | SQL as a detective game — JOINs and WHERE across 10 tables |
| **Finance** | 9 | the mini-SaaS: auth, sessions, transactions, error/APIs — a real product shape |

---

## 3. The Learning Loop Per Problem

1. **Read the spec** (CS50's plain-language `Specification` + walkthrough videos).
2. **Plan** — pseudocode/flowchart first (Week 0 habit).
3. **Implement less-comfortable**, run `check50`; fix & repeat.
4. **Optional more-comfortable** for depth.
5. **Self-audit:** re-implement the same algorithm in Python two weeks later (especially PSet 6's porting exercise).

---

## 4. Mapping PSets → Wiki Concepts

| PSet | Concepts → revisit these wiki pages |
|---|---|
| 1 | [[cs50/week-1-c]] (§Loops, §Types) |
| 2 | [[cs50/week-2-arrays]] (§Strings-as-arrays, §Crypto) |
| 3 | [[cs50/week-3-algorithms]] (§Recursion, §Big-O) |
| 4 | [[cs50/week-4-memory]] (§Pointers, §Structs, §File I/O) |
| 5 | [[cs50/week-5-data-structures]] (§Hash tables) |
| 6 | [[cs50/week-6-python]] (§Data structures) |
| 7 | [[cs50/week-7-sql]] (§Joins, §Indexes) |
| 8 | [[cs50/week-8-html-css-javascript]] |
| 9 | [[cs50/week-9-flask]] |
| 10 | [[cs50/week-10-cybersecurity]] |

---

## 5. Beyond the PSets — Next-Step Practice

- **CS50P** — Python-only extension that re-derives the same curriculum at greater depth (matches [[learn-python-fast-system]]'s recommended intro).
- **CodingBat, HackerRank, Codewars** — the original Video-1 "next steps" ([[programming-cs-fundamentals]] §21) pair perfectly with each week's finished PSet as daily reps.
- **Build outward:** PSet 9's Finance is your springboard to *your own* SaaS ([[learn-python-fast-system]] §8 style).