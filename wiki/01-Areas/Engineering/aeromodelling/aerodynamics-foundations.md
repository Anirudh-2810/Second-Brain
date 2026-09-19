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

# Aerodynamics Foundations (simple words)

> Parent hub: [[INDEX]] · Next: [[wings-controls]] · Revision: [[team-onyx-round1-revision]]
> How to use this page: read each heading slowly. Every hard word is explained with a daily-life example. Lines starting with **MCQ:** are the exact traps the test loves.

## 1. The 4 forces on a plane — in plain words

A plane in the sky always has 4 pushes and pulls acting on it. Think of a paper plane you throw:

| Force | Simple meaning | Everyday example |
|-------|----------------|------------------|
| **Weight** | Earth pulling the plane down. | Like gravity pulls you down on a weighing scale. |
| **Lift** | Air pushing the plane up. | Like wind getting under an umbrella and lifting it. |
| **Drag** | Air pushing back, slowing the plane. | Like putting your hand out of a moving car — air pushes your hand back. |
| **Thrust** | Engine pushing the plane forward. | Like a fan blowing air behind you on a skateboard. |

What happens when they fight:

- Lift = Weight → plane flies straight, neither climbs nor falls.
- Lift is MORE than Weight → plane goes **up** (climb).
- Thrust = Drag → speed stays **same**.
- Thrust is MORE than Drag → plane goes **faster** (accelerate).

**Memory trick:** "Lift beats Weight to climb. Thrust beats Drag to go fast."

**MCQ:** Level flight at steady speed always needs Lift = Weight AND Thrust = Drag. If any option says otherwise, cut it.

## 2. How lift is made — two ideas that work together

A wing makes lift because of its shape. The top of the wing is more curved than the bottom. Air going over the top has to move faster. Faster air pushes less. So pressure on top becomes low, pressure below stays high, and the wing gets sucked upward. That is the short story. The full story has two halves below. **You need both halves.**

### 2a. Half 1 — Bernoulli's idea (fast air = less push)

Daniel Bernoulli said in 1738: when a fluid (air or water) moves fast, its pressure drops. This is just energy saving — speed goes up, pressure goes down.

The formula looks scary but read it like a sentence — "pressure + speed-energy + height-energy is same on both sides":

$$P_1 + \frac{1}{2}\rho v_1^2 + \rho g h_1 = P_2 + \frac{1}{2}\rho v_2^2 + \rho g h_2$$

- $P$ = pressure (how hard air pushes)
- $\rho$ (rho) = density (how heavy the air is)
- $v$ = velocity (how fast air moves)
- $g$ = gravity, $h$ = height

On a wing: air above moves **fast** → pressure **low**. Air below moves **slow** → pressure **high**. High pressure below pushes the wing up. That upward push is lift.

Simple test you can feel: blow hard over the top of a paper strip held near your mouth. The strip rises. Fast air above = low pressure = strip gets lifted.

**MCQ:** Low pressure is always on the **top** of the wing, high pressure on the **bottom**. Options that swap them are wrong.

### 2b. The glue — Coanda effect (why air sticks to the wing)

Air could just fly straight past the wing. But it doesn't. It bends and hugs the curved top surface, like water hugging the back of a spoon under a tap. Try it in a kitchen sink — water bends around the spoon instead of falling straight.

Why? The still air far above pushes down on the moving air near the wing, pressing it onto the surface. Same thing happens below the wing.

Because the air is forced to bend **downward** behind the wing, we call this bent flow **downwash** (wash = flow, down = downward).

### 2c. Half 2 — Newton's idea (push air down, wing goes up)

Newton's Third Law: every push has an equal push back. You push a wall, the wall pushes you. A balloon pushes air out the back, the balloon flies forward.

Same here: the wing pushes air **down** (downwash). So air pushes the wing **up** with the same force. That upward push-back IS lift.

**So the complete answer the test wants:** Bernoulli explains the pressure difference. Newton explains the push-back from downwash. **Neither one alone is complete. Together they explain lift.**

**MCQ:** If options give "only Bernoulli" or "only Newton", look for the "both together" option — that is usually correct.

### 2d. The WRONG theory — Equal Transit (very common trap)

The wrong theory says: two air particles split at the front of the wing, travel top and bottom, and MUST meet again at the back at the same time. Since the top path is longer, top air must go faster. Sounds neat. **But it is false.** Experiments show the particles do NOT meet again. Nobody is forcing them to reunite.

So: whenever an MCQ option says lift happens "because air must reach the trailing edge at the same time", **that option is wrong**.

## 3. Bluff body vs streamlined body — in plain words

**Bluff body** = a fat, blocky shape standing across the wind. Air hits it and cannot smoothly touch all its sides. Examples: a tall building in wind, a running truck, a brick, or even a wing tilted too steeply (large angle of attack).

**Streamlined body** = a smooth, fish-like shape. Air flows nicely around all sides. Examples: a fish, or a wing lying almost flat (small angle of attack).

What happens behind a bluff body:

1. Air slows down behind it. This slow zone is called the **wake** (like the disturbed water behind a boat).
2. Sometimes big spinning air balls break off behind it. This is called **vortex shedding** (vortex = whirlpool of air).
3. Wake + vortices = lots of **drag** (backward pull).

Drag has two parts:

$$C_D = C_{D(PRESS)} + C_{D(FRICTION)}$$

- **Friction (viscous) drag** = air rubbing along the skin, like rubbing your palm on a table. Big on smooth, long shapes.
- **Pressure (form) drag** = pushing caused by the shape's pressure pattern, big on blocky shapes.

Simple rule:

- Rubbing wins → call it **streamlined** (fish, flat wing).
- Shape-pressure wins → call it **bluff** (brick, truck, steep wing).

**MCQ:** Brick / truck / skyscraper = bluff = **pressure drag** dominates. Fish / flat airfoil = streamlined = **friction drag** dominates.

## 4. What is an airfoil? (one paragraph, simple)

An airfoil is just the side-view shape of a wing — the curved slice you would see if you cut the wing like bread. It is the best known shape for getting lots of lift with little drag. Wings, tail fins, and tail planes all use it. The names of its parts (leading edge, chord line, camber) and its two types (symmetrical vs cambered) are on the next page → [[wings-controls#1-airfoil-terminology-and-types]].

## Quick self-check (answers in revision page)

1. Which force must exceed which for a climb?
2. State Bernoulli's principle in one sentence.
3. What is downwash, and which law turns it into lift?
4. Why is Equal Transit Theory wrong?
5. $C_D$ = ? Name both components and which dominates a bluff body.
