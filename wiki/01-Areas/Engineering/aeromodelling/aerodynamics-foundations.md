---
course_code: "ENG-AERO"
course_name: "Aeromodelling — Team Onyx Round 1"
unit: "Aerodynamics Foundations"
date: 2026-09-19
description: "Four forces of flight, Bernoulli + Newton lift theory with Coanda effect, Equal-Transit myth, bluff vs streamlined bodies and drag split."
tags: [btech, aeromodelling, aerodynamics, lift, bernoulli, drag, airfoil]
last_updated: "2026-09-19"
confidence: high
---

## For future agent
Distilled from `[[raw-sources/Aerodynamics_and_Avionics_Study_Material.pdf]]` §1–2 (Forces, Lift Theory, Bluff Body, Airfoils intro). Covers the theory half of the 10 aero MCQs. Stable physics — no staleness risk.

# Aerodynamics Foundations

> Parent hub: [[INDEX]] · Next: [[wings-controls]] · Revision: [[team-onyx-round1-revision]]

## 1. Four fundamental forces

| Force | Direction | Produced by | Balance condition |
|-------|-----------|-------------|-------------------|
| **Weight** | toward ground | gravity | Lift = Weight → level flight |
| **Lift** | upward | wings (airfoil pressure difference) | Lift > Weight → climb |
| **Drag** | opposite velocity | air resistance | Thrust = Drag → constant speed |
| **Thrust** | forward | engine (propeller / jet stream) | Thrust > Drag → accelerate |

One-line memory hook: **lift beats weight to climb, thrust beats drag to accelerate.**

## 2. Lift theory — the two correct halves

### 2a. Bernoulli's Principle

> Faster fluid → lower pressure (conservation of energy). — Daniel Bernoulli, *Hydrodynamica* (1738).

$$P_1 + \frac{1}{2}\rho v_1^2 + \rho g h_1 = P_2 + \frac{1}{2}\rho v_2^2 + \rho g h_2$$

where $P$ = pressure, $\rho$ = density, $v$ = velocity, $g$ = gravity, $h$ = altitude.

Applied to a wing: airfoil shape speeds airflow **above** the wing and slows it **below** → low pressure above + high pressure below → net upward force.

### 2b. Coanda effect (the glue)

High pressure above pushes near-surface air molecules down onto the curved wing so flow **stays attached** instead of flying straight. Same attachment happens on the lower surface. This forced downward deflection is called **downwash**.

### 2c. Newton's Third Law

> Every force has an equal, opposite reaction.

Wing pushes air **down** (downwash) → air pushes wing **up** with equal magnitude → that reaction **is lift**.

**Neither Bernoulli nor Newton alone is the full story — together they form lift theory.**

### 2d. How lift is NOT generated — Equal Transit Theory (WRONG)

Claims upper and lower air molecules must reunite at the trailing edge simultaneously (longer upper path ⇒ must go faster). **Disproven by experiment** — molecules do not meet up. Classic MCQ trap: if an option says "equal transit time explains lift", it is false.

## 3. Bluff body vs streamlined body

**Bluff body**: cross-section significantly perpendicular to flow, so fluid does NOT touch all boundaries. Examples: skyscraper in wind, truck, car, brick, airfoil at **large** AoA.

- Behind a bluff body sits a slow-flow region = **wake**.
- Periodic large vortices shed behind = **vortex shedding**.
- Wake ⇒ **drag**.

Drag split:

$$C_D = C_{D(PRESS)} + C_{D(FRICTION)}$$

- **Frictional (viscous) drag** — fluid rubbing on the surface.
- **Pressure (form/profile) drag** — surface pressure distribution over the whole body.

Rule: friction-dominated → **streamlined** (fish, airfoil at small AoA). Pressure-dominated → **bluff**.

## 4. Airfoil in one paragraph

Cross-sectional shape of a wing; most efficient lift-per-drag shape; basis of wings, fins, horizontal stabilizer. Full terminology and symmetric/cambered types → [[wings-controls#1-airfoil-terminology-and-types]].

## Quick self-check (answers in revision page)

1. Which force must exceed which for a climb?
2. State Bernoulli's principle in one sentence.
3. What is downwash, and which law turns it into lift?
4. Why is Equal Transit Theory wrong?
5. $C_D$ = ? Name both components and which dominates a bluff body.
