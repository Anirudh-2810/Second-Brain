---
module: "engineering-physics"
topic: "Revision: Interference due to Reflected Light — Thin Parallel Film of Uniform Thickness"
tags: [engineering-physics, optics, interference, thin-film, reflected-light, stokes-rule, revision]
last_updated: "2026-08-21"
prerequisites: ["Interference Basics", "Path & Phase Difference", "Stokes' Rule", "Snell's Law"]
---

# Revision: Reflected Light from a Thin Parallel Film

> One-page revision of the classic derivation: what happens when light is reflected from the two surfaces of a thin, parallel, uniform film (e.g. soap film, oil film on water, glass plate). **Memorize the end result, understand the 3-line derivation.**

---

## Setup (draw this)

A thin parallel film of thickness $t$ and refractive index $\mu$, in air ($\mu = 1$). A ray falls at angle $i$, refracts inside at angle $r$.

```
              Incident ray
                    \
                     \ i
                      \
             AIR       \ A                ← Ray 1: reflected at TOP (A)
      ─────────────────┐\
      │     film μ, t  │  \
      │                │   \  r  (refracted)
      │                │    \
      │                B     \
      │          Ray 2 │      \
      │      (leaving  │       \
      │       film)    │        C    ← Ray 2 reflected at BOTTOM (C)
      ─────────────────┴─────────────────
```

Two parallel reflected rays emerge (Ray 1 from the top surface at A, Ray 2 from inside after reflecting at the bottom at C). **They are coherent → they interfere.**

---

## Step 1 — Geometric path difference (derive once)

Ray 2 travels **inside the film** the extra distance $AC + CB$ instead of going straight on like Ray 1. Measure the extra **optical** path:

$$\Delta_{geom} = \mu(AC + CB) - AN$$

- $AC = CB = \dfrac{t}{\cos r}$ (film thickness $t$, slanted path)
- $AN = 2t\tan r \cdot \sin i$ (drop perpendicular $N$ from A onto Ray 2's direction)
- Snell: $\sin i = \mu \sin r$

$$\Delta_{geom} = \mu\cdot\frac{2t}{\cos r} - 2t\tan r\,\sin i
= \frac{2\mu t}{\cos r} - \frac{2\mu t\sin^2 r}{\cos r}
= \frac{2\mu t\,(1 - \sin^2 r)}{\cos r}$$

$$\boxed{\Delta_{geom} = 2\mu t \cos r}$$

> Note how elegantly it collapses: the $\mu$ and the geometry combine to leave just $2\mu t\cos r$.

---

## Step 2 — Phase change on reflection (Stokes' rule)

| Reflection | Interface | Phase change |
|---|---|---|
| Ray 1 (top) | air ($\mu{=}1$) → film ($\mu{>}1$) | **rare → dense: $\pi$ change** (= $\lambda/2$) |
| Ray 2 (bottom) | film → air | **dense → rare: no change** (0) |

So only **one** extra $\lambda/2$. Total effective path difference:

$$\boxed{\Delta = 2\mu t \cos r + \frac{\lambda}{2}}$$

---

## Step 3 — Conditions (reflected light)

| | Condition | Using $\Delta = 2\mu t\cos r + \lambda/2$ |
|---|---|---|
| **Maxima (bright)** | $\Delta = n\lambda$ | $$2\mu t \cos r = \frac{(2n-1)\lambda}{2},\quad n = 1,2,3,\dots$$ |
| **Minima (dark)** | $\Delta = (2n+1)\frac{\lambda}{2}$ | $$2\mu t \cos r = n\lambda,\quad n = 0,1,2,\dots$$ |

**Normal incidence** ($r = 0 \Rightarrow \cos r = 1$) — the exam favourite:

- Bright: $2\mu t = \dfrac{(2n-1)\lambda}{2}$
- Dark: $2\mu t = n\lambda$ (note: $n=0$ just gives $t=0$, no film)

---

## Quick-revision table

| Concept | Value |
|---|---|
| Geometric path difference | $2\mu t \cos r$ |
| Phase change count (film in air) | **1** (top surface only) |
| Total effective path difference | $2\mu t \cos r + \lambda/2$ |
| Bright (reflected) | $2\mu t \cos r = (2n-1)\lambda/2$ |
| Dark (reflected) | $2\mu t \cos r = n\lambda$ |
| Transmitted light | **Complementary** — bright in reflected ⟺ dark in transmitted |
| Film of uniform thickness | Single colour (the $\lambda$ that satisfies the condition) |
| Film of varying thickness | Bands of colours (soap bubbles, oil films) |

---

## Exam do's & don'ts

- ✅ Count phase changes **first** — the whole formula depends on it. Film in air = 1 change.
- ✅ Use $\mu t$ for optical path, never just $t$.
- ⚠️ If **both** reflections are rare→dense or both dense→rare (e.g. a coating on glass), there are **0 or 2** phase changes and the bright/dark conditions **flip**: bright becomes $2\mu t\cos r = n\lambda$.
- ✅ Anti-reflection coatings: choose $t$ so reflected rays cancel → $\mu t = \lambda/4$ (quarter-wave) makes them dark.

## CROSS-REFERENCES

- Full module: [[module-1-optics-interference-diffraction]] (§3 Interference in Thin Films)
- Newton's rings & air wedge: same $2\mu t\cos r$ idea with a **varying** film
- Formula sheet: [[physics/formula-sheet-optics]]