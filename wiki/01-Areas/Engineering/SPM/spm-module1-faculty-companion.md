---
course_code: "316U06C107"
course_name: "Structured Programming Methodology"
unit: "M1 faculty companion — PPT deltas over module-1-spm-c-basics"
tags: [spm, btech, c, module-1, algorithms, flowcharts, pseudocode, structured-programming, compilation, sdlc, operators, type-conversion]
last_updated: "2026-10-02"
date: "2026-09-18"
description: "SPM M1 faculty-PPT companion — problem-definition method, SI example, largest-of-three chain, Bohm-Jacopini, error trilogy, guards, const-vs-define, conversion demo."
---

## For future agent

This note holds ONLY what the Sem-1 faculty PPTs add on top of [[module-1-spm-c-basics]] — phrasing, examples, and tables worth quoting in exams. Theory depth (COCOMO, memory layout, PERT) stays in [[module-1-spm-c-basics]]. Drills live in [[spm-practice-bank-module1]], quiz items in [[spm-quiz-bank]], lab in [[spm-lab-exp1-exp2-guides]].

**Source-set warning (2026-10-02):** `raw-sources/` now holds **two** copies of the Module-1 decks — `SPM SEM1 work/PPT/Module 1/` (AY 2026-27, used for this page) and `SPM Lecture/` (a second copy, mostly identical). One file in the newer folder, `SPM_Module1_1.1_PPT.pptx`, is an **AY 2025-26** cohort deck and is *superseded* — see §6b for what was salvaged and §"Deck-verification log" for the per-deck diff result. Check the AY header before ingesting any SPM deck: `Topic N.N` + `AY 2026-27` = current family; `First Year -AY 2025-26` = older cohort.

# SPM M1 Faculty Companion — PPT Deltas (Sem-1 Drive)

> Sources: `raw-sources/SPM SEM1 work/PPT/Module 1/` — `SPM_Module1.pptx` (overview, 19 slides) · `SPM_Module1_1_F.pptx` (1.1 deep dive) · `SPM_Module1_2.pptx` (1.2 structured programming) · `SPM_Module1_3.pptx` (1.3 execution + SDLC) · `SPM_Module1_4.pptx` (1.4 headers + data) · `SPM_Module1_5.pptx` (1.5 operators) | Syllabus: [[syllabus-316U06C107]] M1 (5 hrs, CO1) | Prereq for: [[spm-module2-faculty-companion]]

Course meta (repeated on every PPT): 316U06C107, F.Y. B.Tech common, AY 2026-27, Bloom Apply (1.1, 1.5) / Understand (1.2–1.4). References: Busbee 2013, Forouzan/Afyouni C 4th ed 2023, Forouzan/Gilberg C++ 2nd ed 2012, Balagurusamy ANSI C 8th ed 2019, Dey/Ghosh OUP 1st ed 2016, NPTEL `noc22_cs40` (C) / `noc21_cs02` (C++).

## 1. Problem definition method (1.1 — faculty wording)

**Definition:** a well-defined problem statement states *what is to be solved, the given inputs, and the expected output*. Faculty tip: skipping this step is the single biggest cause of programs that compile but solve the wrong problem.

Five steps: Understand (restate) → Analyze (inputs/outputs/constraints) → Plan (algorithm/flowchart) → Solve (code) → Verify (test + refine). Verify feeds back into Understand — testing often reveals the original statement was incomplete.

Good statement must specify: inputs (data, types, ranges), outputs (exact result, form), process/rules (formula/transformation), constraints (e.g. "assume positive integer"). Vague ("write a program for interest") → precise:

> Given principal P, rate R, time T (years), calculate simple interest using $SI = (P \times R \times T)/100$, and display result.

## 2. Algorithm vs flowchart vs pseudocode (1.1)

| Aspect | Algorithm | Flowchart | Pseudocode |
|---|---|---|---|
| Form | Numbered steps, plain language | Diagram, standard symbols | English-like, code-shaped text |
| Best for | High-level planning | Visualizing branches/loops | Bridging to real code |
| Weakness | Wordy when complex | Tedious to redraw | No visual overview |

All three describe the same logic — choice is audience, not correctness. Algorithm characteristics (memorize): finiteness, definiteness, input (zero or more), output (at least one), effectiveness. Language-independent: the same algorithm implements in C, Python, or Java.

Standard flowchart symbols: Terminal (oval, start/end — exactly one of each), Input/Output (parallelogram), Process (rectangle), Decision (diamond — the ONLY symbol with two outgoing arrows, Yes/No), Flow line (arrows), Connector (small circle).

Sum-of-N loop pattern (reappears as C loops in M2):

```
Step 1: Start | Step 2: Read N | Step 3: sum=0, i=1
Step 4: If i > N go to Step 8 | Step 5: sum = sum+i
Step 6: i = i+1 | Step 7: Go to Step 4
Step 8: Print sum | Step 9: Stop
```

Pseudocode conventions: `BEGIN...END`, `READ/INPUT`, `PRINT/DISPLAY`, `IF...THEN...ELSE...END IF`, `WHILE/FOR...DO...END WHILE`. No fixed grammar — clarity over syntax.

Largest-of-THREE full chain (problem → algorithm → pseudocode → C). Algorithm: read A,B,C; if A>B AND A>C → largest=A; else-if B>C → largest=B; else largest=C; print.

```c
#include <stdio.h>
int main() {
    int a, b, c, largest;
    printf("Enter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);
    if (a > b && a > c)
        largest = a;
    else if (b > c)
        largest = b;
    else
        largest = c;
    printf("Largest = %d\n", largest);
    return 0;
}
```

Pitfalls (faculty list): vague statements, no clear stop (infinite loop when coded), inconsistent symbols (rectangle for a decision), pseudocode too language-specific, jumping straight to code.

Quick-test answers (1.1): NOT-a-characteristic = ambiguity; decision symbol = diamond, two arrows; sum N=4 prints 10; "pseudocode must follow exact language syntax" = False.

## 3. Structured programming extras (1.2)

**Böhm–Jacopini theorem (1966):** ANY computable function can be implemented using only sequence/selection/iteration — `goto` is never mathematically necessary. That is why every language has if/loops.

SESE principle: every block has exactly ONE entry and ONE exit — traceable top to bottom. Jumping into the middle (skipping init) violates it. Each nested block keeps its own entry/exit, so nesting never breaks SESE — but 4+ levels signals "split into a function" (M4).

Spaghetti vs structured (both print 1–5):

```c
int i = 1;
start:
    if (i > 5) goto end;
    printf("%d\n", i);
    i++;
    goto start;
end: ;
```

```c
int i;
for (i = 1; i <= 5; i++) printf("%d\n", i);
```

Sum of first 5 evens (= 30) structured version:

```c
int n = 5, i = 1, count = 0, sum = 0;
while (count < n) {
    if (i % 2 == 0) { sum += i; count++; }
    i++;
}
printf("Sum = %d\n", sum);
```

All-three-together demo (`grade_report.c`): SEQUENCE (declarations/prompts) + ITERATION (`for` over students) + SELECTION (pass/fail `if-else`).

Pitfalls: reaching for `goto`; overusing `break`/`continue` as goto substitutes (scattered exits recreate the tangle); arrow-code nesting; confusing single-exit with "exactly one return"; mixing paradigms (structured flow ≠ OOP).

Quick-test answers (1.2): NOT-a-construct = goto; `for(i=1;i<=3;i++){if(i%2==0)printf("%d ",i);}` prints `2`; "Böhm–Jacopini proves goto sometimes necessary" = False.

## 4. Execution + SDLC extras (1.3)

Pipeline faculty wording: Source → Compiler → Object → Linker (+Libraries) → Executable → Execution. `gcc program.c` silently runs compile+link as one command, but internally they stay separate.

Compiler vs interpreter table:

| Aspect | Compiler (C) | Interpreter (Python) |
|---|---|---|
| Translation | WHOLE program before running | One line at a time |
| Errors | All syntax before execution | Stops at first error while running |
| Speed | Faster (pre-translated) | Slower (on-the-fly) |
| Output | Separate executable | Needs interpreter every run |

Error trilogy (exam classic): compile-time/syntax (missing `;`, caught before run, no object generated) · runtime (valid grammar, fails DURING — `a/b` with b=0, array overrun) · logical (runs fine, WRONG output — `avg = a + b / 2` instead of `(a+b)/2`; hardest, only output-checking catches it).

Linker-stage signature: "undefined reference" happens at LINKING, not compilation — each `.c` compiled fine, the linker cannot find the called code (missing library/object, or two files defining the same global function). Separate commands:

```bash
gcc -c hello.c -o hello.o   # compile
gcc hello.o -o hello        # link
./hello                     # execute
```

SDLC faculty framing: Topic-1.1's 5-step is the single-problem version; SDLC is the whole-product version. Six phases: Requirement Analysis (WHAT, output = SRS) → Design (HOW, architecture + algorithms/flowcharts live HERE) → Implementation (usually SHORTEST relative to attention) → Testing (project-scale Verify; catches logical errors) → Deployment (release + training/docs) → Maintenance (LONGEST phase, years; feedback loops back to Requirement Analysis). Skipped requirements found in Testing can force redoing Design + Implementation — the most expensive mistake.

Waterfall: each phase fully finishes before the next begins; rigid — going back is costly. Agile/Spiral (shorter repeated cycles) — know by name only.

Quick-test answers (1.3): object+library combined at Linking; `a/b` with b=0 is runtime; Waterfall "next phase starts before previous completes" = False.

## 5. Headers, data, identifiers (1.4)

`#include <stdio.h>` (angle brackets = system folders) vs `#include "myheader.h"` (quotes = your project folder first). Standard headers: `stdio.h` (printf/scanf), `stdlib.h` (malloc/exit/rand), `string.h` (strlen/strcpy/strcmp), `math.h` (sqrt/pow/sin), `ctype.h` (isdigit/toupper).

Custom header pattern — declare in `.h`, define in `.c`, guard against double-inclusion:

```c
/* mathutils.h */
#ifndef MATHUTILS_H
#define MATHUTILS_H
int square(int n);
int cube(int n);
#endif
```

C has NO namespaces — one shared space for all functions/globals. Workaround is prefix convention (`audio_init()` not `init()`), the hand-rolled equivalent of C++ `std::` / Java packages. Two files defining global `reset()` compile clean separately and fail only at link.

Fundamental types (typical sizes — C guarantees minimums only):

| Type | Holds | Size | Specifier |
|---|---|---|---|
| `int` | Whole numbers | 4 B | `%d` |
| `float` | Decimal | 4 B | `%f` |
| `double` | Decimal, more precision | 8 B | `%lf` |
| `char` | Single character | 1 B | `%c` |

Wrong specifier (float with `%d`) compiles but prints garbage. Identifier rules: letters/digits/underscore only; cannot start with a digit; case-sensitive; no keywords. `const` vs `#define`: `const float PI = 3.14;` is typed, compiler-enforced, debugger-visible (prefer it); `#define PI 3.14` is preprocessor text substitution with no type checking. Uninitialized locals hold garbage — initialize on the declaration line.

Quick-test answers (1.4): project-first include = quotes; `const int MAX=10; MAX=20;` = compile error; "`#define` has a real checkable type" = False.

## 6. Operators and conversions (1.5)

Integer division: `17/5` = 3 (truncated, not rounded); `%` is integers-only. `a>b` evaluates to 1/0 — no separate boolean type. `x+=5` ≡ `x=x+5`. Pre-increment updates BEFORE use (`x=++i` takes the new value); post uses the OLD value first (`x=i++`).

```c
int i = 5;
printf("%d\n", i++);  /* 5 */
printf("%d\n", i);    /* 6 */
printf("%d\n", ++i);  /* 7 */
```

Evaluation walk-through: `10 + 2*3 - 4/2` → `2*3=6`, `4/2=2`, `10+6=16`, `16-2=14`. Same-precedence goes by associativity: `20-4-2` = `(20-4)-2` = 14 (left-to-right); `a=b=c=5` assigns right-to-left. When in doubt, parenthesize.

Implicit conversion widens silently (`int + float` → float); explicit cast forces (`(float)a / b`). The canonical demo:

```c
int a = 5, b = 2;
float r1 = a / b;          /* 2.0 — integer division FIRST, too late */
float r2 = (float) a / b;  /* 2.5 — cast forces float division */
```

Pitfalls: `=` vs `==` (`if(x=5)` assigns, almost always true); assuming `+` outranks `*`; treating `++i`/`i++` as identical; `%` on floats (invalid).

Quick-test answers (1.5): highest precedence = `()`; `printf("%d",i++)` with i=4 prints 4, i becomes 5; `(float)7/2` = 3.5; "`%` works on floats" = False.

### 6a. Bitwise operators are OUT OF SCOPE for 1.5 (verified 2026-10-02)

The AY 2026-27 deck `SPM_Module1_5.pptx` **removed** a whole bitwise-operators section that the earlier 2025-26 deck carried, and replaced it with an explicit scope note:

> *"Not shown: bitwise operators (`&`, `|`, `^`, `~`, `<<`, `>>`) — these work at the individual-bit level and are outside this topic's scope."*

The removed slides had covered `a & b`, `a | b`, `a ^ b` on binary values (e.g. `12 & 10 → 8`) and shifts (`x << 2` multiplies by $2^n$, `x >> 1` divides by 2). **Do not spend exam-prep time on these** — they are not examinable under 1.5 in the current deck family. They still appear in other contexts (device drivers, cryptography) but that is outside this course's stated scope.

Extra practice question added by the new deck: with `int x = 10;`, what does `printf("%d", x--)` print, and what is `x` afterward? (Prints 10; `x` becomes 9.)

### 6b. Supplementary: the superseded AY 2025-26 Topic 1.1 deck

`raw-sources/SPM Lecture/SPM_Module1_1.1_PPT.pptx` (26 slides, 3.3 MB) is an **AY 2025-26 cohort deck** — its header reads *"First Year - AY 2025-26"*, while every other deck in `SPM Lecture/` is **AY 2026-27**. The current 2026-27 Topic 1.1 deck is the one already ingested here (`SPM SEM1 work/PPT/Module 1/SPM_Module1_1_F.pptx`, 27 slides). **The older deck does not replace section 2** — it is superseded. It does however contain a few items the current deck does not, worth knowing:

- **Definition of structured programming** — *"a programming paradigm aimed at improving the clarity, quality, and development time of computer programs by using well-defined control structures and subroutines."* Emphasises **top-down design** and the three control structures (sequence, selection, iteration).
- **Three problem-solving skills** — (1) understanding the problem domain, (2) breaking complex problems into subproblems (**divide-and-conquer**), (3) critical thinking / logic development.
- **Four core aspects** — analytical thinking, pattern recognition, creative solutions, debugging.
- **Quotation** — V. Anton Spraul, *Think Like a Programmer*: *"Problem solving is writing an original program that performs a particular set of tasks and meets all stated constraints."* A safe citation for a 1-mark question on problem solving.
- **Requirements specification** — distinguishes **functional** requirements (what it does) from **non-functional** ones (performance, usability), plus **acceptance criteria** and test scenarios.
- **Alternative 3-stage framing** — Understanding → Planning → Implementing, where Planning covers interface design, data structures, algorithm sketching and pseudocode. Note this differs from the 5-step Understand-Analyze-Plan-Solve-Verify in section 2; the 5-step is the current framing.

## Deck-verification log (2026-10-02)

A second set of Module-1 decks (`raw-sources/SPM Lecture/SPM_Module1*.pptx`) was text-diffed against the `SPM SEM1 work/PPT/Module 1/` set this page was built from. Result per deck:

| Deck | Old → new slides | Content delta | Action |
|---|---|---|---|
| `SPM_Module1.pptx` | 19 → 19 | none (entity-encoding + line-break noise only) | no change needed |
| `SPM_Module1_1_F.pptx` → `SPM_Module1_1.1_PPT.pptx` | 27 → 26 | **whole deck is AY 2025-26**, superseded by the 2026-27 set | extracted to §6b, did **not** overwrite §2 |
| `SPM_Module1_2.pptx` | 28 → 28 | **zero** changed lines | no change needed |
| `SPM_Module1_3.pptx` | 27 → 27 | **zero** changed lines | no change needed |
| `SPM_Module1_4.pptx` | 29 → 27 | none (`&quot;` → `"` encoding, 2 slides dropped) | no change needed |
| `SPM_Module1_5.pptx` | 28 → 27 | **bitwise-operator section removed** | recorded in §6a |

**Method:** PPTX is a ZIP archive; slides were extracted with stdlib `zipfile` by pulling `<a:t>` text runs per `ppt/slides/slideN.xml`, then compared with `difflib.unified_diff`. Speaker notes were checked and are slide-number boilerplate only (adds ~0.3 KB/deck). Repeat this for any future deck revision.

## Cross-references

- Depth: [[module-1-spm-c-basics]] · [[spm-module2-faculty-companion]]
- Drill: [[spm-practice-bank-module1]] · [[spm-quiz-bank]]
- Lab: [[spm-lab-exp1-exp2-guides]] · Pattern: [[assessment-guide-ese-ost-quiz]]
