---
module: "programming"
topic: "Programming — Master Flowcharts (Learning Loop, Debug Loop, Build Loop)"
tags: [programming, flowchart, format, overview, learning-path, debug, build-loop, state-machine, pseudocode]
last_updated: "2026-08-11"
---

# Programming — Master Flowcharts

> The three loops that govern the whole module, rendered as state machines (Mermaid + ASCII).
> Each box = an action, each diamond = a decision.
> 1. **The Learning Loop** — from absolute zero to job-ready ([[learn-python-fast-system]]).
> 2. **The Debug Loop** — how to fix code you broke ([[programming-cs-fundamentals]] §10).
> 3. **The Build Loop** — from idea to shipped product ([[winning-in-tech-art-of-winning]]).

---

## 1. The Learning Loop (zero → builder)

```mermaid
flowchart TD
    START["WHY: Python = gateway to AI/ML<br/>career-long compounding skill"] --> CTX["CONTEXT: where does your code sit?<br/>model deployment / backend / cloud / containers"]
    CTX --> CRS["ONE long-form course<br/>CS50 or Bro Code or Automate-the-Boring or ZTM"]
    CRS --> PR["Halfway: practice on PracticePython +<br/>Python Tutor visualization"]
    PR --> CW["Every session: start with a CODEWARS kata<br/>(the 'gym' for problem-solving)"]
    CW --> AI{"AI = tutor or crutch?"}
    AI -->|"Ask specific questions only"| DI["Deliberate practice continues"]
    AI -->|"Doing the solving for you"| X["STOP — you're outsourcing your brain"]
    DI --> DIS["Embrace the discomfort: Pomodoro +<br/>logical breakdown, no phone"]
    DIS --> PRJ["PROJECTS: 30 Days of Python<br/>web scraping → MongoDB → API"]
    PRJ --> SAAS["Build your own SaaS<br/>Stripe + Postgres + Tailwind + GH Actions"]
    SAAS --> P["Portfolio / business / income"]
```

**ASCII version:**

```
 START ─► CONTEXT ─► ONE COURSE ─► PRACTICE (PracticePython, Python Tutor)
                                        │
        P(product) ◄── SAAS ◄── 30 DAYS OF PYTHON ◄── DISCOMFORT-ZONE ◄──┘
        ▲                                     ▲                ▲
        └────────── portfolio / income ───────┴── CODEWARS DAILY ┘
```

---

## 2. The Debug Loop

See [[programming-cs-fundamentals]] §10 for the full text; the flow: **read the error → is it clear? → (yes) fix → (no) print/breakpoint → comment in/out → isolate → rewrite → re-test** with back-ups and small increments.

```mermaid
flowchart TD
    A[Program misbehaves] --> B{Which error type?}
    B -->|Syntax| C[IDE flags it + blocks run<br/>fix grammar → re-run]
    B -->|Runtime| D[Think through flow<br/>infinite loop? unreachable condition?]
    B -->|Logic| E[No red text — hunt it]
    E --> F[Print statements at suspect lines<br/>+ breakpoints + inspect vars]
    F --> G[Comment sections in/out to isolate]
    G --> H{Culprit found?}
    H -->|No| F
    H -->|Yes| I[Rewrite that section]
    C --> J[Run frequently + back up with Git]
    D --> J
    I --> J
```

---

## 3. The Build Loop (idea → shipped, visible)

```mermaid
flowchart TD
    A[Idea pops into your head] --> B{Idea 'good enough'?<br/>Am I 'skilled enough'?}
    B -->|Self-negotiation| B
    B -->|STOP negotiating| C[BUILD with everything available<br/>AI + libraries + templates + docs]
    C --> D[SHIP it]
    D --> E[SHOW it: LinkedIn post / demo video / write-up]
    E --> F[ITERATE on feedback]
    F --> G{Curiosity still alive?}
    G -->|Yes| C
    G -->|No| H[New idea; identity now = builder]
```

---

## 4. Mathematics & Creativity inside the mix

- **Quantity → quality** ([[mathematics-of-creativity]]) is the engine behind *build → ship → show → iterate*.
- **The 1% math edge** ([[math-for-programming]]) is what converts a copier into a *modifier* of code.
- **Focus/attention** ([[overview]]) is the fuel — Pomodoro, MITs, and distraction-proofing make all three loops run.

---

## 5. Module Navigation

- **[[overview]]** — the module synthesis & concept map.
- **[[programming-cs-fundamentals]]** · **[[math-for-programming]]** · **[[mathematics-of-creativity]]** · **[[winning-in-tech-art-of-winning]]** · **[[learn-python-fast-system]]**.