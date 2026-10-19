---
course_code: "ENG-PHY"
course_name: "Engineering Physics"
unit: "MSE Recall Test — Module 1 Optics: Interference, Diffraction, Grating, Polarization"
date: "2026-10-19"
tags: [engineering-physics, optics, interference, ydse, thin-film, newtons-rings, grating, polarization, exam-prep, mse, recall-test, self-test]
last_updated: "2026-10-19"
confidence: high
description: "Numerical + theory self-test for Engineering Physics MSE Module 1 (optics): YDSE + modifications, thin-film conditions, Newton's rings, grating orders/RP, Michelson, Malus/Brewster. Questions first, worked key in collapsible callouts."
relations:
  depends_on: "[[mse-revision-physics-m1-optics]]"
  relates_to: "[[mse-recall-test-physics]]"
---

## For future agent

Cold **self-test** for Engineering Physics MSE **Module 1 (Optics)** — the interference/diffraction questions [[mse-recall-test-physics]] does not contain (that test = the four laser numericals + thin-film derivation + slit decision table). Reveal the collapsed `> [!success]- Answer` only after attempting. Method+units matter more than the exact number. Source of truth: [[mse-revision-physics-m1-optics]]; deep worked examples: [[module-1-optics-interference-diffraction]] §12 and [[module-1-addendum-sem1-numericals-derivations]]. Use c = 3×10⁸ m/s where needed.

# MSE Recall Test — Physics M1: Interference → Polarization

Pack: [[mse-revision-physics-m1-optics]] · Cards: [[mse-flashcards-physics-m1-optics]]

## Q1 — YDSE basic (fringe width → λ)

Fraunhofer YDSE: slit separation d = 0.2 mm, screen at D = 1 m. Measured fringe width β = 2.5 mm. Find the wavelength and the distance of the 3rd bright fringe from the center.

> [!success]- Answer
> $\lambda = \dfrac{\beta d}{D} = \dfrac{2.5\times10^{-3} \times 0.2\times10^{-3}}{1} = \mathbf{500\ nm}$.
> 3rd bright: $x_3 = \dfrac{3\lambda D}{d} = 3\beta = \mathbf{7.5\ mm}$.

## Q2 — Sheet on one slit

λ = 600 nm sheet of **μ = 1.5** is placed before one slit. Find t so the central fringe sits where the 5th bright fringe was. Which way does the pattern move?

> [!success]- Answer
> Shift of n fringes: $(\mu-1)t = n\lambda \Rightarrow t = \dfrac{5 \times 600\times10^{-9}}{0.5} = \mathbf{6\ \mu m}$.
> Pattern moves **toward the covered slit** (extra optical path on that side).

## Q3 — Intensity ratio

YDSE slits have intensity ratio I₁:I₂ = 9:4. Find I_max/I_min and the fringe visibility.

> [!success]- Answer
> $\sqrt{I_1}:\sqrt{I_2} = 3:2$. $I_{max}/I_{min} = \left(\dfrac{3+2}{3-2}\right)^2 = \mathbf{25}$.
> Visibility $= \dfrac{I_{max}-I_{min}}{I_{max}+I_{min}} = \dfrac{25-1}{25+1} = \dfrac{24}{26} \approx \mathbf{0.92}$.

## Q4 — Thin-film condition (flip counting)

A soap film (μ = 1.33) in air appears **bright green** (λ = 540 nm) in reflected light near-normal incidence. Of how many phase flips is this film's reflected pair composed, and what is the *minimum* thickness giving bright reflection? What is it just before it pops?

> [!success]- Answer
> Air→film flip (yes), film→air reflection (no) → **k = 1 flip**. k=1 bright: $2\mu t = (2n-1)\dfrac{\lambda}{2}$; n=1 → $t_{min} = \dfrac{\lambda}{4\mu} = \dfrac{540}{4\times1.33} \approx \mathbf{102\ nm}$.
> As it thins toward t = 0 the k=1 dark condition $2\mu t = n\lambda$ turns on → the film goes **black** just before popping.

## Q5 — Newton's rings

A 10th dark ring has diameter 5.0 mm with λ = 600 nm. Find R. What happens to the diameters if μ = 1.4 liquid fills the gap?

> [!success]- Answer
> $D_n^2 = 4n\lambda R \Rightarrow R = \dfrac{D_{10}^2}{40\lambda} = \dfrac{(5.0\times10^{-3})^2}{40 \times 600\times10^{-9}} = \dfrac{25\times10^{-6}}{2.4\times10^{-5}} \approx \mathbf{1.04\ m}$.
> With liquid: $D_n^2 \to \dfrac{4n\lambda R}{\mu}$ → diameters shrink by $\dfrac{1}{\sqrt{1.4}}$ ($\approx \mathbf{0.85\times}$, i.e. the 10th dark → ≈4.3 mm).

## Q6 — Grating orders + RP

A grating of **6000 lines/cm** is illuminated normally with 600 nm light. (a) What orders are visible? (b) If 3 cm width of the grating is illuminated, find the RP at order 1 — can it resolve a 600 / 599.5 nm doublet?

> [!success]- Answer
> (a) d = 1/6000 cm = 1.67 μm; d/λ = 2.78 → **n = 0, 1, 2** (n=3: sinθ = 1.08 > 1, absent).
> (b) RP = nN = 1 × 18000 = **18000**. Needed: $\dfrac{600}{0.5} = 1200 \le 18000$ → **resolved** (Δλ = 0.033 nm at the limit).

## Q7 — Michelson

The movable mirror of a Michelson is displaced **0.05 mm** and 200 fringes sweep past. Find λ.

> [!success]- Answer
> $\lambda = \dfrac{2\Delta d}{N} = \dfrac{2 \times 5\times10^{-5}}{200} = \mathbf{500\ nm}$. (Trap: the factor 2 — light runs the arm twice.)

## Q8 — Single slit

Fraunhofer single slit, e = 0.3 mm, D = 1 m. Find the linear width of the central maximum for λ = 600 nm.

> [!success]- Answer
> Central width $= \dfrac{2\lambda D}{e} = \dfrac{2 \times 600\times10^{-9} \times 1}{0.3\times10^{-3}} = \mathbf{4\ mm}$. (Doubles when e is halved: diffraction spreads as the slit narrows.)

## Q9 — Polarizers around a 90° cancel

Two ideal polarizers are crossed (unpolarized I₀ in). A third is inserted between them at 45°. What now passes?

> [!success]- Answer
> $I = \dfrac{I_0}{2}\cdot\cos^2 45°\cdot\cos^2 45° = \dfrac{I_0}{2}\cdot\dfrac12\cdot\dfrac12 = \mathbf{I_0/8}$. (Unpolarized first stage is I₀/2, not cos².)

## Q10 — Brewster + polarization check

Light in air hits water (μ = 1.33). At what incidence angle is the reflected beam fully polarized, and what is its E-vector direction?

> [!success]- Answer
> $\tan\theta_p = 1.33 \Rightarrow \theta_p \approx \mathbf{53.1°}$. The reflected beam is plane-polarized with its E-vector **parallel to the surface** (perpendicular vibrations only). Practical follow-through: sea glare is horizontally polarized → polarized sunglasses (vertical axis) cut it.

**Scoring: 8+ correct → ready**; pierced method errors → re-drill the matching flashcard row (C-4…C-27) and the pack's trap list.

## See also

- [[mse-revision-physics-m1-optics]] — formulas + traps these questions drill
- [[mse-flashcards-physics-m1-optics]] — the card deck for this material
- [[mse-recall-test-physics]] · [[mse-revision-physics-lasers-slit]] — laser/slit test + pack
- [[module-1-optics-interference-diffraction]] §12 · [[module-1-addendum-sem1-numericals-derivations]] — worked source numericals
- [[mse-study-method]] · [[mse-2026-10-26-5-day-plan]]
