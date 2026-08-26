---
module: "programming"
topic: "Changing Your Perspective on Math — Intuitive Foundations Over Formulas"
tags: [programming, math, learning, intuition, pedagogy, margin, euler-identity, perspective-shift]
last_updated: "2026-08-26"
source_url: "https://www.youtube.com/watch?v=_OdqYVCTUqs"
source_channel: "Margin"
source_title: "CHANGING your PERSPECTIVE on MATHS fellas - Must Watch"
duration_sec: 1801
description: "Margin's approach to learning math: start from zero, no formulas handed down. Build intuition from concrete foundations (coin, ant, tree, ferris wheel) toward Euler's identity e^(iπ)+1=0. Understanding = ability to change perspective, not memorize procedures."
---

# Changing Your Perspective on Math — Intuitive Foundations Over Formulas

> **Source:** *CHANGING your PERSPECTIVE on MATHS fellas - Must Watch* (Margin).
> **Video:** https://www.youtube.com/watch?v=_OdqYVCTUqs
> **Channel:** Margin — known for intuitive math animations (Euler's identity, complex numbers visualized).

---

## For future agent
This note captures Margin's pedagogical philosophy: math is **not** formula-first. It's about building a **mental model** from intuitive primitives, then seeing how formulas emerge naturally. This mirrors [[math-for-programming]]'s donut case study — math as the "1% edge" that lets you modify, not just implement. Also connects to [[mathematics-of-creativity]] (math as pattern-seeking) and Roger Antonsen's TED talk on *understanding = changing perspective*.

---

## 1. The Core Thesis

> *"Most of us were taught maths the wrong way round. Someone writes a formula on the board, you copy it, you do 30 questions, you take the test, you forget it. Nobody ever tells you where the formula came from or what problem it was solving in the first place."*

**Margin's approach:** Start from **actual zero**. No formulas. Just people looking at the world and noticing patterns.

---

## 2. The Pedagogical Pipeline (Margin's Method)

| Stage | Traditional Teaching | Margin's Method |
|-------|---------------------|-----------------|
| **Input** | Formula given as axiom | Concrete phenomenon (coin flip, ant walking, tree growing, ferris wheel) |
| **Process** | Memorize → Apply → Test | Observe → Question → Pattern → Represent → Generalize |
| **Output** | Correct answers | **Intuition** — you *see* why the formula works |
| **Retention** | Low (procedural) | High (conceptual — you can re-derive) |

This mirrors the **ASCII donut** case study in [[math-for-programming]]: the donut.c code is just trig + linear algebra. If you understand the *why*, you can turn the donut into a cube, a sphere, a game engine.

---

## 3. Three Numbers, Three Centuries, One Equation

Margin's Euler's identity video (companion to this philosophy) builds **e^(iπ) + 1 = 0** from three independent discoveries:

| Number | Origin | Century | Discoverer's Problem |
|--------|--------|---------|---------------------|
| **π** | Circle geometry | Ancient | Measuring circles |
| **e** | Compound interest / growth | 17th (Napier, Bernoulli, Euler) | "How much money grows if compounded continuously?" |
| **i** | "Imaginary" roots of cubics | 16th (Cardano) → 18th (Euler) | Solving x² + 1 = 0 |

**The miracle:** Three numbers from **unrelated problems** (geometry, finance, algebra) "shake hands" in one line. Not because someone designed it — because they **describe the same deep structure**.

---

## 4. The Ferris Wheel Intuition (e^(ix) = cos x + i sin x)

Margin visualizes **e^(ix)** as a **ferris wheel**:

- **e** = growth (compound interest, population, cooling tea)
- **i** = quarter turn (90° rotation operator)
- **e^(ix)** = growth pushed *sideways* → **rotation** instead of explosion
- **cos x** = horizontal shadow (left-right position)
- **sin x** = vertical height (up-down position)

> *"Growth turned sideways becomes rotation. Sit with that for a second — it's the strangest sentence in this video."*

This is the **geometric meaning of complex exponentiation**. The formula e^(ix) = cos x + i sin x isn't a definition to memorize — it's a **description of motion**.

---

## 5. Half a Circle Walk: e^(iπ) = -1

- Start at **1** (one step right of center)
- Walk **half a circle** (π radians) via e^(iπ)
- Land at **-1** (one step left of center)
- **e^(iπ) + 1 = 0** = "growth turned sideways, walked halfway around, brought you exactly home"

The equation isn't "beautiful" because it's compact. It's beautiful because **three stories that never planned to meet all end at the same front door**.

---

## 6. Implications for Learning (and Programming)

1. **Formulas are summaries, not starting points.** Learn the *story* first.
2. **Understanding = perspective-shifting.** See the same thing as: a shadow, a height, a rotation, a complex number, a growth process.
3. **Math for programmers:** Don't memorize `rotation_matrix`. Understand *why* multiplying by i rotates. Then quaternions, shader math, and ML gradients become intuitive.
4. **Cross-domain transfer:** The same **rotation-as-complex-multiplication** insight appears in:
   - [[math-for-programming]] §2 (donut rotation matrices)
   - [[quantitative-finance-foundations]] (stochastic processes, Brownian motion)
   - [[mathematics-of-creativity]] (pattern-seeking across domains)

---

## 7. Related Resources

- [[math-for-programming]] — ASCII donut case study: math as the "1% edge"
- [[mathematics-of-creativity]] — Math as pattern-seeking sense (Eddie Woo's "fractal sense")
- [[learning-resources/index]] — Self-teaching catalogs (OSSU, freeCodeCamp, roadmap.sh)
- [[roadmaps-and-study-guides]] (self-dev) — How to structure learning
- [[Self-Dev/learning-methodology]] — Meta-learning principles

---

## 8. Key Quotes

> *"We start from the very bottom (a coin, an ant, a tree, a ferris wheel) and build all the way up to the equation a lot of people call the most beautiful in mathematics."*

> *"This is the line I showed you at the start. Back then it looked like nonsense. Look at it now."*

> *"Three numbers from three different centuries found by different people who never met for reasons that had nothing to do with each other. And when you put them in one line, they don't argue. They fit like they were made for each other."*

---

## See Also
- [[math-for-programming]] — Why programming needs math (donut case study)
- [[mathematics-of-creativity]] — Math as a "sense" for patterns
- [[quantitative-finance-foundations]] — Same math powering quant models
- [[Self-Dev/learning-methodology]] — How to learn technical subjects