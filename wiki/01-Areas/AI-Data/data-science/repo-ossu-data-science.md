---
course_code: "DATA-SCI"
course_name: "Data Science & Machine Learning Field"
unit: "Repo 4 — OSSU Data Science (Full Curriculum)"
tags: [curriculum, data-science, mooc, self-taught, linked-repo]
last_updated: "2026-08-24"
confidence: "high"
source: "https://github.com/ossu/data-science"
---

## For future agent
OSSU Data Science's complete free curriculum — structure fetched from its README (2026-08-24). It defines duration (~2 years part-time), course order, and prerequisites per course. This page compresses it into an executable sequence with vault shortcuts. Execution method: [[how-to-self-teach]]; compressed variant: [[roadmap-data-scientist]].

# OSSU Data Science — Expanded

## Its Own Usage Rules

- **Duration**: ~2 years at ~10h/week; courses have listed lengths — trust them
- **Order**: curriculum order matters (prerequisites chain); within a stage, pick ONE of the options
- **Language**: any for intro courses; Python assumed later (R acceptable in stats electives)
- **Track progress**: it suggests checking off courses; use this page's checkboxes

## The Curriculum (its actual stage headings)

| Stage | Courses (pick one unless noted) | Length | Done |
|-------|-------------------------------|--------|------|
| **Intro to DS** | What is Data Science? (IBM) / Data Science for Moneyball | 1–2wk | ☐ |
| **Intro to CS** | CS50 / Intro to CS & Programming (MIT 6.00.1) | 8–12wk | ☐ |
| **DSA** | Stanford CS9-style problem solving via its linked option | 4–10wk | ☐ |
| **Databases** | Stanford Self-Paced DB course (4 mini-courses) | 12wk | ☐ |
| **Calculus** | MIT 18.01 single-variable | 13wk | ☐ |
| **Linear Algebra** | MIT 18.06 (Strang) | 14wk | ☐ |
| **Multivariable Calc** | MIT 18.02 *(optional for ML-track)* | 13wk | ☐ |
| **Stats & Probability** | MIT 18.05 Introduction to Probability and Statistics | 16wk | ☐ |
| **DS Tools & Methods** | Python for DS (edX) + applied track options | 8–15wk | ☐ |
| **Machine Learning** | Stanford CS229 or Columbia ML (edX) + Data Mining option | 10–12wk | ☐ |
| **Final Project** | Build a data product end-to-end, publish | self | ☐ |

## Compression Notes (honest adjustments)

The full path is excellent but heavy for someone also running college. Two legal shortcuts:

1. **Calculus**: if you have JEE-level math ([[01-Areas/Engineering/mathematics/formula-sheet-master]]), test out of 18.01 by doing its exams cold; skip to what you actually forgot.
2. **Linear algebra**: Strang is gold but slow; pair 18.06 lectures with 3Blue1Brown first-pass ([[math-for-ml-survival-guide]]).

## Quit Points

| Quit Point | When | Counter |
|------------|------|---------|
| 18.05 grind fatigue | Stats stage | Alternate weeks with applied sklearn work so progress stays visible |
| Multivariable doubt | "Is 18.02 needed?" | Skip for applied DS; required only for deep DL theory later |
| Mid-curriculum job panic | Anytime | You don't need all 11 stages to intern-hunt — stages 1–4 + tools already qualify you for analyst screens |

## Example Checkpoint Questions

1. After the DB course: write a query using a CTE + window function together.
2. After 18.05: explain why p-values mislead when you test 20 hypotheses.
3. Final-project bar: does a stranger reproduce your result from your repo alone?

## Deep Edition Addendum

**Failure modes of OSSU followers**:

| Failure | Mechanism | Counter |
|---------|-----------|---------|
| Curriculum perfectionism | Waiting for "the right time to start the 2-year journey" | Start stage 1 this week; stages are independent-ish |
| Math-stage residence | 18.05/18.06 becoming permanent homes | Time-box math per [[math-for-ml-survival-guide]]; test out of known parts |
| Certificate collecting | Badges as goals | Exit tests on THIS page define done |
| Solo isolation | No discussion, motivation decays | Its community exists; also pair with vault weekly review |

**Premortem**: *Year 1 of OSSU: 3 courses "in progress," none complete.* Findings: parallel course starts (violating its own order rule), multivariable-calc rabbit hole despite ML track, zero final-project thinking. OSSU's own "How to use" section warns against all three.

**Rescue flowchart**:
```mermaid
flowchart TD
    S["OSSU stalled"] --> Q{"Where?"}
    Q -->|"course mid-way boring"| C{"Still needed for<br/>target role?"}
    C -->|"no"| D["Formally drop; log why.<br/>Curriculum serves you"]
    C -->|"yes"| NZ["Minimum pace: 2 videos +<br/>1 exercise daily"]
    Q -->|"math wall"| MG[[math-for-ml-survival-guide]] intuition path
    Q -->|"lost in catalog"| HUB["Re-read this page's table;<br/>pick CURRENT row only"]
    D & NZ & MG & HUB --> G["One stage gate at a time"]
```

**Life integration**: semester-break windows = heavy stages (ML); exam weeks = never-zero reviews; metrics = stages closed (checkboxes above), assignment submission streaks, final-project scoping started by month 12.

## Cross-Vault Links

- [[roadmap-data-scientist]] — compressed execution variant
- [[repo-teachyourselfcs]] — the CS-side sibling curriculum
- [[math-for-ml-survival-guide]] — lighter math alternative