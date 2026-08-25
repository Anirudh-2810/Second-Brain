---
module: "SPM"
topic: "Module 1: Introduction to SPM & C Basics — SDLC, Project Management & Compilation Pipeline"
tags: [spm, software-project-management, sdlc, waterfall, agile, spiral, v-model, estimation, cocomo, function-points, scheduling, pert, cpm, risk-management, c-programming, compilation-phases, memory-layout, stack, heap, data-segment, text-segment]
last_updated: "2026-08-19"
prerequisites: ["Basic Programming Concepts", "Computer Organization (Registers, RAM)", "Operating System Process Model"]
---

# Module 1: Introduction to SPM & C Basics

> The project-management + language-foundation layer of the SPM + C course. Half of this module is software project management (SDLC models, Waterfall vs. Agile, estimation, scheduling, risk); the other half is the C execution model — the four-stage compilation pipeline and the four-region process memory layout (Stack, Heap, Data, Text). Written for beginners: every term is explained before it is used, and every diagram is followed by a plain-English walkthrough.

---

## Table of Contents

1. [Conceptual Architecture & ASCII Flowcharts](#1-conceptual-architecture--ascii-flowcharts)
2. [Code Implementation & Memory Analysis](#2-code-implementation--memory-analysis)
3. [High-Yield Exam Problems & Worked Solutions](#3-high-yield-exam-problems--worked-solutions)
4. [Real-World System Applications](#4-real-world-system-applications)
5. [Appendix: Formula & Data Quick Reference](#appendix-formula--data-quick-reference)

---

## 1. CONCEPTUAL ARCHITECTURE & ASCII FLOWCHARTS

### 1.0 What Is a "Program"? — The Beginner's Foundation

Before SPM theory, fix the mental model of what C is actually doing:

- A **program** is a sequence of instructions the CPU executes. C is a language for *writing those instructions* in a human-readable form.
- A **source file** (`.c`) is plain text. The computer does not understand text — so a chain of tools (**compiler pipeline**) converts it into machine code.
- When the program runs, the operating system loads it into RAM as a **process**. That process's memory is divided into regions (the **memory layout**) — each region has a job and a lifetime.
- A **project** is bigger than a program: it is people, requirements, schedules and risks organised to *produce* that program. **SPM** (Software Project Management) is the discipline of planning and controlling that production.

Everything in this module hangs on those three pillars: **SDLC** (how projects flow), **compilation** (how source becomes code), **memory layout** (how code lives in RAM).

### 1.1 Software Development Life Cycle (SDLC) — Master Flowchart

**What SDLC means:** every software product, no matter how small, is *born* (idea), *planned*, *built*, *tested*, *released* and *kept alive*. The sequence of these stages is the Software Development Life Cycle. Models differ only in the **ordering** of stages and how much **feedback** (going back to fix something) is allowed.

```
   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
   │ 1. REQUIRE-  │───►│ 2. DESIGN    │───►│ 3. IMPLEMEN- │───►│ 4. TESTING   │
   │    MENT       │    │    (HLS/LLS) │    │    TATION    │    │    (Unit/Int/│
   │    ANALYSIS   │    │    & ARCH    │    │    (Coding)  │    │    System)   │
   └──────────────┘    └──────────────┘    └──────────────┘    └──────────────┘
          ▲                                                           │
          │                                                           ▼
   ┌──────────────┐                                            ┌──────────────┐
   │ 7. MAINTEN-  │◄───────────────────────────────────────────│ 5. DEPLOY-   │
   │    ANCE      │                                            │    MENT      │
   │ (corrective/ │    6. OPERATION & SUPPORT                  │              │
   │  adaptive/   │◄───────────────────────────────────────────│              │
   │  perfective) │                                            └──────────────┘
   └──────────────┘
```

**Plain-English walkthrough of each stage:**

| # | Stage | What happens | Output document |
|---|---|---|---|
| 1 | **Requirement Analysis** | Find out *what* the customer wants. Interview users, write down every feature and constraint. | **SRS** (Software Requirements Specification) |
| 2 | **Design** | Decide *how* to build it. High-Level Design (HLD) = architecture: which modules, how they talk. Low-Level Design (LLD) = inside each module: data structures, algorithms, interfaces. | HLD + LLD documents |
| 3 | **Implementation** | Write the actual code (in C for this course). | Source code |
| 4 | **Testing** | Verify the code does what the SRS says. Unit (each function), Integration (modules together), System (whole product), Acceptance (customer says yes). | Test reports |
| 5 | **Deployment** | Install / ship to the customer's environment. | Release notes |
| 6 | **Operation & Support** | Run, monitor, answer tickets. | Support logs |
| 7 | **Maintenance** | Change the software after release. Three kinds (memorize): **corrective** (fix a bug), **adaptive** (adapt to new OS/hardware/law), **perfective** (add features/improve performance). Perfective is the biggest cost (~50%+ of lifetime). | Change requests |

**Fundamental rules (memorize):**
- Every project passes through **all** seven stages eventually; the *models* differ in ordering and feedback loops, not in which stages exist.
- An **SDLC model** is just a strategy for sequencing the stages. Think of it as: "How much do I plan ahead, and when am I allowed to go back?"

### 1.2 SDLC Models — The Full Family Tree (goes deeper than the basics)

**a) Waterfall (1970, Winston Royce):** strictly one-way. Finish stage 1 completely before starting stage 2. No going back.

```
   Requirements → Design → Implementation → Testing → Deployment → Maintenance
        └──────────────────────┐
                               ▼
        (rework costs are huge — a design error found in testing means
         rewriting code AND design; a requirement error means ALL of it)
```

**b) V-Model:** a Waterfall variant that pairs every development stage with a testing stage *at the same level* — a visual "V".

```
        Requirements ───────────────► Acceptance Test Design
             │                              │
        High-Level Design ───────────► System Test Design
             │                              │
        Low-Level Design ────────────► Integration Test Design
             │                              │
        Implementation ──────────────► Unit Test Design (code + test)
```

**c) Spiral (Boehm, 1986):** the first model to treat **risk** as the central driver. Each loop (iteration) = plan → risk analysis → build/verify → evaluate, then decide whether to do another loop. Best for large, high-risk projects.

```
          Loop 1         Loop 2         Loop 3
   (gather reqs)  (prototype UI)  (build core)
        │               │               │
   determine risk ── determine risk ── determine risk ── ... until risk is acceptable
```

**d) Agile (2001 Manifesto):** short fixed-length **sprints** (usually 2–4 weeks). Each sprint delivers a small, working, testable slice. Customer feedback every sprint; requirements are allowed to change.

### 1.3 Waterfall vs. Agile — Comparison Table

| Criterion | Waterfall | Agile |
|---|---|---|
| **Model** | Sequential, linear phases | Iterative, incremental sprints |
| **Requirements** | Fixed up-front, frozen (change = expensive) | Evolving, change is welcomed |
| **Customer involvement** | At milestones / final delivery | Continuous (daily stand-ups, demos) |
| **Feedback cycle** | Long (end of each phase) | Short (every 2-4 weeks) |
| **Testing** | After coding completes | Continuous (test as you code) |
| **Delivery** | One big final release | Many small releases |
| **Documentation** | Heavy, phase-gated | Lightweight ("working software over comprehensive documentation") |
| **Risk handling** | Late discovery, huge rework cost | Early discovery via demos each sprint |
| **Best for** | Well-understood, stable, regulated (defence, banking core, avionics) | Uncertain, fast-changing (startups, web/cloud, mobile) |
| **Example methods** | Waterfall, V-Model | Scrum, Kanban, XP (eXtreme Programming) |

**Beginner tip — the one-line exam answer:** Waterfall = "plan everything, then build"; Agile = "build a little, check, adjust, repeat".

### 1.4 Project Planning, Estimation & Scheduling — Flowchart

```
   PROJECT INITIATION
        │
        ▼
   ┌───────────────────────────────┐
   │ WORK BREAKDOWN STRUCTURE (WBS)│  decompose the deliverable into tasks
   └───────────────────────────────┘
        │
        ▼
   ┌───────────────────────────────┐
   │ ESTIMATION                   │
   │ • LOC (Lines of Code)        │  count lines → effort
   │ • FP (Function Points)       │  count functionality → effort
   │ • COCOMO                     │  Effort = a × (KLOC)^b
   │                              │  Time    = c × (Effort)^d
   └───────────────────────────────┘
        │
        ▼
   ┌───────────────────────────────┐
   │ SCHEDULING                   │
   │ • Activity network (PERT/CPM)│  critical path = longest path
   │ • Gantt chart                │  horizontal bar timeline
   │ • Float/slack analysis       │  how much delay a task can absorb
   └───────────────────────────────┘
        │
        ▼
   ┌───────────────────────────────┐
   │ RISK MANAGEMENT              │
   │ Identify → Analyze → Plan →  │  Risk = P(occurs) × Impact
   │ Mitigate → Monitor           │
   └───────────────────────────────┘
```

#### 1.4.1 Estimation in Depth — Three Techniques

**Technique 1 — LOC (Lines of Code).** Count the expected source lines (thousands → **KLOC**). Productivity is measured in LOC per person-month (typical C: ~1000–3000 LOC/person-month). Crude but simple. Problem: you must *guess* the size before you build.

**Technique 2 — Function Points (Albrecht).** Count *user-visible functionality* instead of lines — language-independent. There are **five function types** (memorize the five abbreviations):

| Type | Full name | Meaning | Weight |
|---|---|---|---|
| **EI** | External Input | each distinct input screen/form (data entering the system) | 3–6 (avg 4) |
| **EO** | External Output | each output screen/report (data leaving) | 4–7 (avg 5) |
| **EQ** | External Inquiry | each query that reads data but changes nothing | 3–6 (avg 4) |
| **ILF** | Internal Logical File | each master file/table the system maintains | 7–15 (avg 10) |
| **EIF** | External Interface File | each file referenced from another system | 5–10 (avg 7) |

$$UFP = \sum (\text{count} \times \text{weight}) \quad \text{over all five types}$$

$$FP = UFP \times VAF, \qquad VAF = 0.65 + 0.01 \times \sum_{i=1}^{14} GSC_i$$

- **VAF** = Value Adjustment Factor, 0.65 to 1.35.
- **GSC** = 14 General System Characteristics, each scored 0–5 (e.g., data communications, performance, reusability, complexity). ΣGSC ranges 0–70.

**Technique 3 — COCOMO (Boehm, Constructive Cost Model).** Uses size (KLOC) to predict effort and time. **Basic COCOMO** has three "modes" depending on project complexity:

| Mode | Typical project | a | b | c | d |
|---|---|---|---|---|---|
| **Organic** | Small team, familiar domain, flexible | 2.4 | 1.05 | 2.5 | 0.38 |
| **Semi-detached** | Mixed team, medium size, some constraints | 3.0 | 1.12 | 2.5 | 0.35 |
| **Embedded** | Tight constraints (hardware, real-time) | 3.6 | 1.20 | 2.5 | 0.32 |

$$E = a\,(KLOC)^b \quad \text{(effort in person-months)} \qquad D = c\,(E)^d \quad \text{(time in months)}$$

**What does a "person-month" mean?** The work one person does in one month (~150–160 hours). If E = 12 person-months, one person takes 12 months, two people about 6 months (never perfectly linear — communication overhead grows with team size).

#### 1.4.2 Scheduling — PERT/CPM in Brief

- **Activity network:** nodes = events/milestones, arrows = tasks with durations.
- **CPM** (Critical Path Method): the **critical path** is the *longest* path through the network. It has **zero slack** — delay any task on it and the whole project is late. The project duration = critical path length.
- **Float (slack):** how much a *non-critical* task can slip without delaying the project.
- **PERT** adds probability: each task gets optimistic (o), most-likely (m), pessimistic (p) estimates; expected time $t_e = \dfrac{o + 4m + p}{6}$.
- **Gantt chart:** tasks as horizontal bars over a calendar timeline — the simplest schedule view.

#### 1.4.3 Risk Management in Brief

$$\text{Risk exposure} = P(\text{risk occurs}) \times \text{Impact}$$

Process: **identify** risks → **analyze** (probability & impact) → **plan** mitigation (avoid, transfer, mitigate, accept) → **monitor** throughout. Classic risks: scope creep, key-person loss, technology failure, schedule overrun.

### 1.5 Structure of a C Program — Anatomy

```
   ┌────────────────────────────────────────────────────────────┐
   │  /* comment / documentation section */                    │
   │  #include <stdio.h>            // preprocessor directives │
   │  #define PI 3.14               // macros                  │
   ├────────────────────────────────────────────────────────────┤
   │  int globalVar = 10;           // global declarations     │
   ├────────────────────────────────────────────────────────────┤
   │  int add(int a, int b);        // function declarations   │
   │                                // (prototypes)            │
   ├────────────────────────────────────────────────────────────┤
   │  int main(void) {              // main function           │
   │      int x = 5;                // local declarations      │
   │      ... statements ...        // executable statements   │
   │      return 0;                 // status to OS            │
   │  }                             //                         │
   ├────────────────────────────────────────────────────────────┤
   │  int add(int a, int b) {       // function definitions    │
   │      return a + b;             //                         │
   │  }                             //                         │
   └────────────────────────────────────────────────────────────┘
```

**Plain-English section guide (beginner):**

| Section | Purpose | Beginner analogy |
|---|---|---|
| Comments | Notes for humans; ignored by compiler | sticky notes on a recipe |
| Preprocessor directives (`#include`, `#define`) | Instructions to the preprocessor, start with `#` | "get the measuring cups" (pull in stdio) and "define a nickname for 3.14" |
| Global declarations | Variables usable by *every* function | a shared whiteboard |
| Prototypes | "This function exists with this signature" — tells the compiler before `main` calls it | a company directory before you phone someone |
| `main` | The entry point — where the OS starts executing | the front door of the house |
| Function definitions | The actual code of each function | the rooms behind the doors |

**Rules (memorize):**
- Every executable C program has **exactly one `main`**. The OS calls `main` first.
- `return 0;` signals *success* to the OS; any non-zero value signals an error code.
- Prototypes are **optional** only if the function's definition appears *before* its first call; otherwise a prototype is required (compilers give "implicit declaration" errors/warnings).
- Every statement ends with a **semicolon** `;`. Forgetting it is the single most common beginner compile error.
- `#` lines are handled *before* compilation (by the preprocessor), not by the compiler.

### 1.6 Compilation Pipeline — Four Phases (Deep Dive)

A beginner sees "compile the program"; the exam wants you to name **four** stages and what each produces. Here is the complete picture:

```
   source.c
      │
      ▼  ┌───────────────────────────────────────────────────────────┐
   [1] PREPROCESSOR  (cpp)  "expands" the source                     │
      │  • pastes #include files verbatim                            │
      │  • expands #define macros (text substitution)                │
      │  • evaluates #if / #ifdef / #endif conditionals              │
      ▼  • strips comments → produces source.i                      │
   [2] COMPILER  (cc1)  C → ASSEMBLY                                 │
      │  • lexical analysis: tokens (keywords, identifiers, symbols) │
      │  • syntax analysis (parsing): checks grammar                 │
      │  • semantic analysis: type checking                         │
      │  • SYNTAX / TYPE errors are caught HERE                      │
      ▼  • optimization (dead code, loop unrolling) → source.s      │
   [3] ASSEMBLER  (as)  assembly → OBJECT CODE (machine code)        │
      │  • converts each mnemonic (mov, add) to machine instructions │
      │  • produces relocatable .o / .obj                            │
      ▼  • external references (printf) still UNRESOLVED            │
   [4] LINKER  (ld)  merges .o files + libraries                     │
      │  • resolves external symbols (printf → address in libc)      │
      │  • combines your .o with startup code (crt0) and libraries   │
      ▼  • produces executable a.out / .exe                          │
   EXECUTABLE
```

**Phase-by-phase beginner explanation:**

1. **Preprocessor.** Reads the raw text. When it sees `#include <stdio.h>`, it *copies the entire header file* into your source. `#define PI 3.14` makes every later `PI` become `3.14` (pure text find-and-replace). Comments are deleted. Output: `file.i` (still C, but "expanded").
2. **Compiler.** Reads `file.i` and checks the *grammar* and *types*. `int x = ;` fails here (syntax). `int x = "hello";` fails here (type mismatch). Produces `file.s` — assembly language (human-readable machine instructions).
3. **Assembler.** Translates each assembly instruction into binary machine code. Produces `file.o` — object code. But if your code calls `printf`, that address is *not known yet* — the `.o` has a placeholder.
4. **Linker.** Pulls together your `.o`, the C runtime startup code, and the precompiled libraries (libc), then *resolves* every placeholder (printf now points to the real function in libc). Produces the final executable.

**Error-to-stage cheat sheet (classic exam question):**

| Error example | Stage that catches it |
|---|---|
| `#include <missing.h>` | Preprocessor (file not found) |
| `int x = ;` / missing semicolon | Compiler (syntax) |
| assigning wrong type / calling with wrong arg count | Compiler (semantic/type) |
| "undefined reference to `foo`" | Linker (symbol not resolved anywhere) |
| division by zero / segfault | Runtime (program already running) |

### 1.7 Process Memory Layout — Stack, Heap, Data, Text (Deep Dive)

**Big picture for a beginner:** when the OS runs your executable, it sets aside one big chunk of RAM for the process and carves it into regions. Each region has a **job**, a **growth direction**, and a **lifetime**.

```
   HIGH ADDRESS  ┌─────────────────────────────┐
      ▲          │  STACK  (grows downward)    │  ← automatic local variables,
      │          │  frame per function call;   │    return addresses, params;
      │          │  LIFO; small, fast, finite  │    overflow → stack overflow
      │          ├─────────────────────────────┤
      │          │  ↓ free (unallocated) space ↓│
      │          │  ↑                         ↑│
      │          │  HEAP  (grows upward)       │  ← malloc/calloc/realloc/free
      │          │  dynamic allocation;        │    manual management; leaks
      │          ├─────────────────────────────┤    possible
      │          │  DATA segment               │
      │          │   • initialized data (DS)   │  ← global & static vars with
      │          │     e.g. int g = 10;        │    initializers
      │          │   • uninitialized data (BSS)│  ← global & static without
      │          │     e.g. int g;  (zeroed)   │    init (zero-initialized)
      │          ├─────────────────────────────┤
      │          │  TEXT (code) segment        │  ← machine instructions, RO
      │          │  read-only, shared          │    constants, string literals
   LOW ADDRESS   └─────────────────────────────┘
```

**Region-by-region beginner guide:**

- **Text (code) segment:** the actual machine instructions (from section 1.6). Read-only — the program cannot overwrite its own code. Also holds constant strings like `"hello"`.
- **Data segment (two parts):**
  - **DS (initialized data):** globals/statics that have a value written in the source: `int count = 10;` — the `10` is stored *in the binary file* and loaded at startup.
  - **BSS (uninitialized data):** globals/statics declared without a value: `int buffer[1000];` — the OS *zeros* this region at startup, so uninitialized globals read as `0`. The binary stores only the *size*, not the contents (saves disk space).
- **Heap:** memory handed out at *runtime* on request (`malloc`). Grows **upward** (toward higher addresses). Lifetime = until you call `free`. Two classic beginner bugs: **memory leak** (never `free` → memory runs out) and **dangling pointer** (use after `free`).
- **Stack:** grows **downward**. One **frame** per active function call holding its locals, parameters, and the return address. Frames are created on call and destroyed on return (LIFO). Fast, automatic, but **finite (~8 MB typical)** — deep recursion fills it → **stack overflow** (crash).

**Why do the stack and heap grow toward each other?** So the process can use *all* the middle space as needed — either region can borrow whatever is free. If they collided, you'd run out of memory.

**Memory segment comparison table:**

| Segment | Contents | Growth | Lifetime | Managed by | Overflow risk |
|---|---|---|---|---|---|
| **Text** | Machine code, RO strings | Fixed | Whole program | Compiler/Linker | — |
| **Data (DS)** | Initialized globals/statics | Fixed | Whole program | Compiler | — |
| **Data (BSS)** | Uninitialized globals/statics (zeroed) | Fixed | Whole program | Compiler/Loader | — |
| **Heap** | `malloc`/`calloc` memory | Upward (toward high addr) | Until `free()` | Programmer | Heap exhaustion / fragmentation |
| **Stack** | Locals, params, return addr | Downward (toward low addr) | Function scope | Compiler (auto) | Stack overflow (deep recursion) |

---

## 2. CODE IMPLEMENTATION & MEMORY ANALYSIS

### 2.1 Structure of a C Program — Complete Example with Memory Map

```c
#include <stdio.h>

#define SQUARE(x) ((x) * (x))   /* macro: text substitution, NOT a function */

int globalCount = 100;          /* initialized global → DATA segment (DS) */
int globalZero;                 /* uninitialized global → BSS (auto-zeroed) */

int add(int a, int b);          /* prototype */

int main(void)
{
    int local = 5;              /* automatic local → STACK frame of main */
    int result = add(local, SQUARE(2));
    printf("result = %d\n", result);
    printf("BSS global = %d\n", globalZero);
    return 0;
}

int add(int a, int b)
{
    return a + b;
}
```

**Output:**
```
result = 9
BSS global = 0
```

**Memory map of this program (walk through it carefully):**

```
   ┌──────────────────────────────────────────────┐
   │  STACK                                       │
   │   main frame:  local=5  result=?  [ret addr] │  ← created when main starts
   │   add frame:   a=5      b=4      [ret addr] │  ← created on add() call,
   │                                            │     destroyed on return
   ├──────────────────────────────────────────────┤
   │  DATA  (DS):  globalCount = 100             │  ← initialized global
   │  DATA  (BSS): globalZero  = 0  (zeroed)     │  ← uninitialized global
   ├──────────────────────────────────────────────┤
   │  TEXT: machine code of main() and add(),     │
   │        plus the literal "result = %d\n"      │  ← read-only
   └──────────────────────────────────────────────┘
```

**Why does `add` print 9?** `SQUARE(2)` becomes `((2)*(2))` = 4 (macro expansion happens in phase 1). `add(5, 4)` returns 9. `globalZero` prints 0 because the BSS was zero-filled at load time.

**Beginner trap — macro vs. function:** `#define SQUARE(x) ((x)*(x))` works by *text substitution*, so `SQUARE(1+2)` becomes `((1+2)*(1+2))` = 9 (correct because of the extra parentheses). Without them, `SQUARE(1+2)` = `1+2*1+2` = 5 — wrong! Always parenthesize macro parameters.

### 2.2 Compilation in Practice — The Command Pipeline

```bash
# Phase 1: Preprocess (produces .i — expanded C text)
gcc -E hello.c -o hello.i

# Phase 2: Compile to assembly (produces .s)
gcc -S hello.i -o hello.s

# Phase 3: Assemble to object code (produces .o — machine code with placeholders)
gcc -c hello.s -o hello.o

# Phase 4: Link with libc + startup code to form the executable
gcc hello.o -o hello

# One-shot (all four phases)
gcc hello.c -o hello

# Extra beginner-friendly flags
gcc -Wall hello.c -o hello      # show all warnings (ALWAYS use -Wall)
gcc -g hello.c -o hello         # include debug info (for gdb)
```

**Beginner tip:** `-Wall` turns on warnings — a beginner's best friend. Warnings are the compiler *telling you* you probably made a mistake that still compiles.

### 2.3 Stack vs. Heap — Pointer Demo with Address Comparison

```c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int stackVar = 42;                 /* STACK */
    int *heapPtr = malloc(sizeof(int)); /* HEAP: one int's worth of memory */
    if (heapPtr == NULL)               /* malloc can fail — always check! */
    {
        printf("malloc failed\n");
        return 1;
    }
    *heapPtr = 7;                      /* store 7 into the heap location */

    printf("stackVar addr : %p\n", (void*)&stackVar);
    printf("heapPtr addr  : %p\n", (void*)heapPtr);

    free(heapPtr);                     /* return the heap memory — MATCHES malloc */
    return 0;
}
```

**Expected relationship (typical Linux):** `heapPtr`'s address is **lower** than `stackVar`'s address — the heap grows up from low addresses, the stack grows down from high addresses.

**Beginner explanation of the demo:**
- `int stackVar = 42;` — the 42 lives in `main`'s stack frame. Its address `&stackVar` is high.
- `malloc(sizeof(int))` — asks the heap for 4 bytes. Returns a *pointer* (address) to that block; the address is lower.
- `*heapPtr = 7;` — the `*` operator *dereferences* the pointer: "go to that address and put 7 there."
- `free(heapPtr)` — returns the block. **Every `malloc` must be matched by exactly one `free`.**

**Rules (memorize):**
- `malloc` returns `NULL` on failure — always check before using.
- Every `malloc`/`calloc`/`realloc` must be matched by exactly one `free`.
- Stack allocation is automatic and nearly free (just moves the stack pointer); heap allocation is slow (system call + bookkeeping).
- Stack is small (~8 MB); deep recursion or giant locals overflow it → crash.

---

## 3. HIGH-YIELD EXAM PROBLEMS & WORKED SOLUTIONS

---

### Problem 1: SDLC/Model Theory — Short Answers

**Problem.** (a) In which SDLC phase is the SRS produced? (b) Name two iterative SDLC models. (c) What is the critical path in a PERT/CPM network?

---

**Solution:**

**(a)** The **Requirement Analysis** phase produces the SRS (Software Requirements Specification). It documents *what* the system must do and is the input to the Design phase.

$$\boxed{\text{SRS is produced in Requirement Analysis}}$$

**(b)** **Agile** (Scrum/Kanban) and the **Spiral model** are iterative (Prototype/RAD are also acceptable). The Spiral model loops planning → risk analysis → engineering → evaluation.

$$\boxed{\text{Agile and Spiral (prototype/RAD also acceptable)}}$$

**(c)** The **critical path** is the longest-duration path through the network from start to finish. It has **zero total float/slack** — a one-day delay on any critical-path task delays the whole project — and it determines the minimum project duration.

$$\boxed{\text{Critical path = longest path with zero slack}}$$

---

### Problem 2: COCOMO Estimation

**Problem.** A project is estimated at 50 KLOC, semi-detached mode (a = 3.0, b = 1.12, c = 2.5, d = 0.35). Compute (a) effort in person-months and (b) development time in months. (log₁₀ 50 = 1.6990.)

---

**Solution:**

**Step 1 — effort E.**

$$E = a\,(KLOC)^b = 3.0 \times 50^{1.12}$$

**Step 2 — compute 50^1.12 using logarithms.**

$$\log_{10} 50^{1.12} = 1.12 \times \log_{10} 50 = 1.12 \times 1.6990 = 1.9029$$

$$50^{1.12} = 10^{1.9029} = 79.96$$

$$E = 3.0 \times 79.96 = 239.9 \approx 240\ \text{person-months}$$

**Step 3 — development time D.**

$$D = c\,E^d = 2.5 \times 240^{0.35}$$

**Step 4 — compute 240^0.35.**

$$\log_{10} 240 = 2.3802 \quad\Rightarrow\quad \log_{10} 240^{0.35} = 0.35 \times 2.3802 = 0.8331$$

$$240^{0.35} = 10^{0.8331} = 6.809$$

$$D = 2.5 \times 6.809 = 17.02 \approx 17\ \text{months}$$

**Step 5 — answers.**

$$\boxed{E = 240\ \text{person-months}} \qquad
\boxed{D = 17\ \text{months}}$$

**Interpretation:** the project needs ~240 person-months of work and will take ~17 months to deliver (implying a team of roughly 240/17 ≈ 14 developers).

---

### Problem 3: Memory Layout — Where Does Each Variable Live?

**Problem.** Given the declaration block, identify the memory segment each entity occupies in a typical C process:

```c
int a = 5;                 /* 1. */
static int b;              /* 2. */
const char *s = "hi";      /* 3. */
int main(void){ int c; ... malloc(100); }   /* 4., 5. */
```

---

**Solution:**

| # | Entity | Segment | Reasoning |
|---|---|---|---|
| 1 | `int a = 5` (initialized global) | **Initialized Data (DS)** | has an initializer → value stored in the binary |
| 2 | `static int b` (uninitialized) | **BSS** | no initializer → zeroed by the loader at startup |
| 3 | `"hi"` string literal | **Text (RO)** | read-only constant; the *pointer* `s` itself sits in initialized data |
| 4 | `int c` (local in main) | **Stack** | automatic lifetime — lives only while main runs |
| 5 | `malloc(100)` block | **Heap** | dynamic, freed by `free()` |

---

### Problem 4: Preprocessor vs. Compiler vs. Linker Errors

**Problem.** Classify each error to the compilation stage that would catch it:
(a) `#include <missing.h>`  (b) `int x = ;`  (c) undefined reference to `foo()`  (d) division by zero at runtime.

---

**Solution:**

| Error | Stage | Why |
|---|---|---|
| (a) missing header | **Preprocessor** | it cannot find/read the include file |
| (b) `int x = ;` malformed declaration | **Compiler** | syntax error — the grammar is broken |
| (c) undefined reference to `foo()` | **Linker** | every `.o` compiled fine; no definition of `foo` existed to resolve against |
| (d) division by zero | **Runtime** | only happens when the instruction actually executes (SIGFPE) |

---

### Problem 5: Function Points Calculation

**Problem.** A system has: 3 External Inputs (EI=4 each), 2 External Outputs (EO=5 each), 1 External Inquiry (EQ=4), 2 Internal Logical Files (ILF=10 each), 1 External Interface File (EIF=7). The 14 general system characteristics sum to 35. Compute the adjusted FP. (VAF = 0.65 + 0.01 × ΣGSC.)

---

**Solution:**

**Step 1 — unadjusted FP (UFP).**

$$UFP = (3 \times 4) + (2 \times 5) + (1 \times 4) + (2 \times 10) + (1 \times 7)$$

$$= 12 + 10 + 4 + 20 + 7 = 53$$

**Step 2 — value adjustment factor.**

$$VAF = 0.65 + 0.01 \times 35 = 0.65 + 0.35 = 1.00$$

**Step 3 — adjusted FP.**

$$FP = UFP \times VAF = 53 \times 1.00 = 53$$

**Step 4 — answer.**

$$\boxed{FP = 53\ \text{function points}}$$

---

### Problem 6: Stack vs. Heap Behaviour — Prediction

**Problem.** A program declares `int x;` inside `main` and `malloc`s 10 ints. It calls a recursive function `f(5)`. In which memory regions does each of the following live, and when is `x`'s memory freed? (a) `x` (b) the 10-int block (c) the stack frames of `f`'s recursive calls.

---

**Solution:**

**(a)** `x` is an automatic local → **Stack**, in `main`'s frame. Freed automatically **when `main` returns** (frame popped). No `free` needed.

**(b)** The 10-int block → **Heap**; freed only when the program calls `free(ptr)`. If the program never calls `free`, it's a memory leak (freed only by the OS at process exit).

**(c)** Each of the 5 recursive calls pushes a **Stack** frame; frames are popped in reverse order (LIFO) as `f` returns — 5 frames deep at maximum.

$$\boxed{\text{(a) Stack — freed when main returns} \qquad
\text{(b) Heap — freed by free()} \qquad
\text{(c) Stack — 5 frames, LIFO pop}}$$

---

## 4. REAL-WORLD SYSTEM APPLICATIONS

| Principle | Real-World Practice |
|---|---|
| **SDLC phases & phase-gates** | Regulated industries (medical devices, avionics) require design/traceability gates before any coding begins |
| **Waterfall vs. Agile selection** | Defence/government contracts (fixed spec, waterfall) vs. SaaS startups (Agile sprints, CI/CD) |
| **Estimation (COCOMO, FP)** | Project budgeting and staffing in consultancies; quoting fixed-price contracts |
| **Scheduling (PERT/CPM, critical path)** | Product launch planning, release trains, inter-team dependency management |
| **Risk management** | Startup runway/feasibility risk; contingency buffers in infrastructure rollouts |
| **C compilation pipeline** | Build systems (make/CMake), cross-compilation for embedded targets, diagnosing toolchain errors |
| **Text/Data/BSS segments** | Firmware memory budgeting on microcontrollers (flash layout for code, data, constants) |
| **Heap management** | Embedded RTOS heap pools, server request pools, leak-fighting in long-running daemons |
| **Stack discipline** | Call-depth limits in recursive parsers; embedded interrupt-handler stack sizing (overflow → watchdog reset) |
| **`main` + return codes** | Exit-status conventions in CI/CD pipelines (`0` = pass), service supervisors checking process codes |

---

## APPENDIX: Formula & Data Quick Reference

| Quantity | Formula / Value | Notes |
|---|---|---|
| Function points | FP = UFP × VAF | VAF = 0.65 + 0.01 ΣGSC (14 items, 0–5 each) |
| UFP (5 types) | EI + EO + EQ + ILF + EIF, count × weight | weights ~4, 5, 4, 10, 7 |
| COCOMO effort | E = a(KLOC)ᵇ | person-months |
| COCOMO time | D = c(E)ᵈ | months |
| COCOMO organic | a=2.4, b=1.05, c=2.5, d=0.38 | small, familiar |
| COCOMO semi-detached | a=3.0, b=1.12, c=2.5, d=0.35 | mixed team |
| COCOMO embedded | a=3.6, b=1.20, c=2.5, d=0.32 | tight constraints |
| PERT expected time | $t_e = \dfrac{o + 4m + p}{6}$ | o/m/p estimates |
| Risk exposure | RE = P × U | probability × impact |
| Compile stages | preprocess → compile → assemble → link | gcc -E / -S / -c / link |
| Stack growth | downward (high→low addr) | automatic, finite |
| Heap growth | upward (low→high addr) | malloc/free, manual |

## CROSS-REFERENCES

- Related modules: [[module-2-program-control-functions]] · [[module-3-arrays]] · [[module-4-user-defined-functions]] · [[01-Areas/Programming/programming-cs-fundamentals]] · [[01-Areas/Programming/cs50/week-1-c]]

---

*Revision: every syntax pattern from this module is on [[formula-sheet-spm]].*
