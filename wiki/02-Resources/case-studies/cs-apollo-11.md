---
course_code: "CASESTUDY"
course_name: "Open-Source Case Studies"
unit: "Case Study 2 — chrislgarry/Apollo-11 AGC [Deep R&D + Build Edition]"
tags: [apollo, assembly, embedded, history-of-computing, case-study, build-plan]
last_updated: "2026-08-24"
confidence: "high"
source: "https://github.com/chrislgarry/Apollo-11 (fetched 2026-08-24)"
---

## For future agent
Deep-dive on the Apollo Guidance Computer source: exact code inventory (AGC4 assembly, Comanche/Luminary, Executive, Interpreter, DSKY), WHY those choices existed (hardware reality), and buildable versions — a full AGC reimplementation is a multi-year effort, but an **AGC-style priority executive simulator** and a **DSKY emulator** are excellent weekend-scale builds. Feeds [[build-project-playbook]].

# Apollo-11 Guidance Computer — Deep R&D

## Part 1 — The Code Inventory

| Component | What It Actually Is |
|-----------|--------------------|
| **Comanche055** | Command Module flight program (AGC4 assembly, ~2,700 pages listing) |
| **Luminary099** | Lunar Module flight program — the code that landed Eagle |
| **AGC4 assembly** | The instruction set: ~34 instruction codes, 15-bit words, 1's complement arithmetic |
| **Interpreter** | A virtual machine INSIDE the AGC: pseudo-instructions for vector/matrix ops (navigation math) implemented over AGC4 |
| **Executive** (`EXECUTIVE` source) | Priority-based scheduler: jobs queued with priorities; runs on timer interrupts |
| **Restart monitor** (`RESTART_MONITOR`/`DYNAMICALLY RESTARTABLE TABLES`) | Crash-only design: every state checkpointed so any overload triggers safe restart |
| **DSKY routines** | Display/keyboard interface (the famous panel with VERB/NOUN keys) |
| **Core rope memory** | Not code in repo, but the storage: programs physically WOVEN as wires through cores by textile workers |

Famous named routines you can find verbatim: `BURN_BABY_BURN -- MASTER IGNITION ROUTINE`, `ERASABLE ASSIGNMENTS`, `GROUND TRACKS`.

## Part 2 — Why That Code Was Used

| Constraint (1966 hardware) | Forced Choice | Engineering Consequence |
|----------------------------|---------------|-------------------------|
| ~36KB fixed memory (core rope) + 2KB erasable | Hand-tuned assembly; zero abstraction slack | Every variable manually assigned to erasable banks (`ERASABLE ASSIGNMENTS` literally lists addresses) |
| 2MHz-class CPU, no FPU | Interpreter VM for vector math | Navigation engineers wrote math-like code; interpreter translated |
| Jobs MUST all eventually run | Priority executive | Radar job (high priority) could preempt navigation (lower) — this SAVED the landing |
| Overload WILL happen (1202/1201 alarms during descent) | Restart protection everywhere | State tables designed so restart loses ≤ one cycle of work |
| No way to patch in flight | Rope memory frozen pre-launch | Exhaustive simulation culture; Margaret Hamilton's systems testing |

**The mechanism behind the famous 1202 alarm**: rendezvous radar was stealing CPU cycles (hardware switch phase issue) → executive overflowed its time slots → alarm → **executive shed low-priority work automatically** → guidance continued. The architecture absorbed a hardware fault. Software resilience as load-bearing structure.

## Part 3 — Can I Build My Own Version?

### Full version: ❌
A faithful AGC emulation exists elsewhere (yaAGC project); building from scratch = years.

### Buildable Version A: **AGC Executive Simulator** ✅ (flagship recommendation)
Simulate the core idea — priority scheduling with restart protection:

```
Spec (Python or C, ~300 lines):
- Task list: (name, priority, worst-case-time)
- Timer interrupt every tick -> run highest-priority ready task slice
- OVERFLOW event when low-priority tasks starve N ticks:
    drop lowest-priority task, log alarm "1202", CONTINUE high-priority work
- Checkpoint file per task state -> on simulated crash, restart from checkpoints
Demo scenario: reproduce the 1202 story — add a rogue "radar" task eating
cycles, watch executive shed it, landing task survives.
```

**Why this build is gold**: it teaches priority scheduling, watchdog/restart design, and graceful degradation — concepts that map directly onto your later backend/MLOps work ([[systems-design-distributed]], [[mlops-production-deployment]]).

### Buildable Version B: **DSKY Emulator** ✅ (UI-flavored alternative)
Recreate the keypad/display: VERB+NOUN entry grammar, register display (R1/R2/R3, flashing), responding to a mock computer. Python/Tkinter or web. Teaches protocol/state-machine UI design.

### Similar workflow C: constraint-coding kata
Pick ONE modern mini-project and impose Apollo rules: ≤4KB RAM budget, no dynamic allocation, full restart-safety. E.g., a sensor logger in C with static allocation only. Constraints-as-teacher exercise.

## Part 3.5 — R&D Extension: AGC Internals Worth Knowing

### Word format & memory banks
AGC words: 15 bits + parity. Fixed memory in 2K-word banks (rope), erasable in 1K-word banks. Bank-switching was MANUAL via instructions — code had to know which bank it lived in (`EBANK=`, `FBANK=` directives pepper the listings). Erasable assignments were hand-allocated: `ERASABLE ASSIGNMENTS` source literally lists every variable's address with comments. Modern takeaway: explicit resource maps beat implicit hope when resources are tight.

### The Interpreter (VM inside a VM)
Navigation math needed vectors/matrices; hardware had none of it. Solution: an interpretive language layered over AGC4 — pseudo-instructions like `DV` (vector dot) executed by a threaded-code interpreter. Cost: slower execution. Benefit: guidance engineers wrote near-math pseudocode. This is the ancestor of every domain-specific VM argument (JVM bytecode, WASM).

### Executive mechanics (what your simulator models)
- Timer interrupt every 10ms → executive runs
- Job queue ordered by priority; NO preemption mid-job except by higher priority
- **Overflow alarm**: if no idle time in a second (all slots consumed) → 1202 (no VAC areas) / 1201 (no core sets) → executive deletes lowest-priority job, restarts cleanly
- Restart tables: every critical state mirrored so a restart resumes correctly

### Simulator extension ideas (post-v0.1)
- Add task dependencies (landing needs radar done)
- Count shed-tasks per minute → 'overload dashboard'
- Toggle 'restart protection OFF' mode → show catastrophic difference (the teaching moment)


## Part 4 — Failure Modes While Building

| Failure | Counter |
|---------|---------|
| Trying to learn AGC4 assembly first | Read listings as ARCHAEOLOGY (comments carry narrative); simulator needs zero assembly |
| Simulator scope creep (adding DSKY+interpreter) | v0.1 sentence: "rogue task gets shed while critical task survives" |
| No visible drama | Log events colorfully ("** ALARM 1202 — shedding NAVIGATION **") |

## Life Integration

- Weekend archaeology: one source file/weekend with notes; each ends with a modern-mapping line
- Interview story banked: "I built a priority executive that reproduces the 1202 rescue" — memorable at fresher level
- Metrics: simulator demo working · restart-drill demonstrated · files-read-with-notes count

## Part 6 — Internals Push: Interpreter, DSKY Protocol, Rope Memory

### Interpreter pseudo-instructions (VM layer)
Native AGC4 ops handle single-word arithmetic only; guidance math needs vectors/matrices. The Interpreter layers pseudo-instructions — DV (dot product), VXV (cross), UNIT (normalize), matrix transforms — as threaded-code tables executed by a small VM. Navigation engineers wrote equations nearly literally; cost paid in exact counted cycles. This is the ancestor argument for every domain-specific VM (JVM bytecode, WASM).

### DSKY protocol (constrained grammar UI)
Verb/Noun grammar: sequences like VERB 37 NOUN 01; responses flash codes then steady register displays (R1/R2/R3, signed 5-digit + exponent). ENTER during alarm triage was priority input during descent. Build lesson: constrained grammars beat menus for reliability under stress — your DSKY emulator should reproduce flash semantics exactly.

### Core rope memory manufacturing
Programs physically woven: wire through core = 1, around = 0, threaded by textile workers from printed LISTINGS. Consequences: bugs unfixable post-weave (hence exhaustive simulators), six-month lead time per rope (requirements frozen brutally early), weavers themselves as QA catching inconsistencies. Extreme proof of a general law: deployment friction determines development discipline.

## Checkpoint Questions

1. Which single design decision let the AGC survive hardware-induced overload?
2. In my simulator, what replaces "core rope memory" as the immovable constraint?
3. Where in MY current projects would restart-protection change the design?

## Cross-Vault Links

[[02-Resources/case-studies/index|Field Index]] · [[systems-design-distributed]] · [[lr-build-your-own-x]] · [[01-Areas/Programming/cs50/week-1-c]]