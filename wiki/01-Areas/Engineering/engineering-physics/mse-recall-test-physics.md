---
course_code: "ENG-PHY"
course_name: "Engineering Physics"
unit: "MSE Recall Test — Lasers + Slit/Diffraction"
date: "2026-10-16"
tags: [engineering-physics, lasers, optics, interference, diffraction, slit, thin-film, exam-prep, mse, recall-test, self-test]
last_updated: "2026-10-16"
confidence: high
description: "Numerical + derivation self-test for Engineering Physics MSE: the four must-reproduce laser numericals (A21/B21, g_th, cavity modes, He-Ne λ), thin-film derivation, and decision-table applications (YDSE, single slit, grating). Questions first, worked key in collapsible callouts."
relations:
  depends_on: "[[mse-revision-physics-lasers-slit]]"
  relates_to: "[[mse-flashcards-physics]]"
---

## For future agent

Cold **self-test** for the Engineering Physics MSE (lasers + slit/diffraction). Contains the **four must-reproduce laser numericals** named in the pack, the thin-film derivation, and applied decision-table questions. Reveal the collapsed `> [!success]- Answer` only after attempting. Use the faculty notation where marked. Source of truth: [[lasers-quick-ref]], [[module-1-optics-interference-diffraction]]. Numerical values are illustrative — reproduce the **method and units**, not just the number.

# MSE Recall Test — Physics: Lasers + Slit Theory

Pack: [[mse-revision-physics-lasers-slit]] · Cards: [[mse-flashcards-physics]]

## Q1 — Einstein coefficients (must-reproduce a)

The spontaneous-emission lifetime of a level is **25 ns**. (a) Find $A_{21}$. (b) Write the relation giving $B_{21}$ from $A_{21}$.

> [!success]- Answer
> (a) $A_{21}=\dfrac{1}{\tau}=\dfrac{1}{25\times10^{-9}}=4.0\times10^{7}\ \text{s}^{-1}$.
> (b) $A_{21}=\dfrac{8\pi h\nu^{3}}{c^{3}}B_{21}\Rightarrow B_{21}=\dfrac{A_{21}c^{3}}{8\pi h\nu^{3}}=\dfrac{3.0\times10^{8}}{8\pi h}\,\dfrac{A_{21}}{\nu^{3}}$. (At 632.8 nm, $\nu=4.74\times10^{14}$ Hz, giving $B_{21}\approx6\times10^{20}$ — match the pack's worked value.)

## Q2 — Threshold gain (must-reproduce b)

A laser has $R_1=R_2=0.98$, cavity length $l=0.5$ m, and loss $\alpha=0.01\ \text{m}^{-1}$. Find $g_{th}$.

> [!success]- Answer
> $g_{th}=\alpha+\dfrac{1}{2l}\ln\!\left(\dfrac{1}{R_1R_2}\right)=0.01+\dfrac{1}{1.0}\ln\!\left(\dfrac{1}{0.9604}\right)=0.01+0.0404=\mathbf{0.0504\ m^{-1}}$.
> (Faculty form: replace $l$ with cavity $L$, use $\gamma,\alpha_C$.)

## Q3 — Cavity modes (must-reproduce c)

For $L=0.5$ m: (a) mode spacing $\Delta\nu$; (b) mode number $q$ at $\lambda=632.8$ nm; (c) how many modes fit if the gain bandwidth is $1.5$ GHz.

> [!success]- Answer
> (a) $\Delta\nu=\dfrac{c}{2L}=\dfrac{3\times10^{8}}{1.0}=3\times10^{8}$ Hz $=300$ MHz.
> (b) $q=\dfrac{2L}{\lambda}=\dfrac{1.0}{632.8\times10^{-9}}=1.58\times10^{6}$.
> (c) $N=\dfrac{\Delta\nu_{gain}}{\Delta\nu}=\dfrac{1.5\times10^{9}}{3\times10^{8}}=5$ modes.

## Q4 — He-Ne wavelength (must-reproduce d)

A He-Ne transition has energy difference $E_2-E_1=1.96$ eV. Find $\lambda$.

> [!success]- Answer
> $\lambda=\dfrac{1240}{E_2-E_1}=\dfrac{1240}{1.96}=632.7\ \text{nm}\approx\mathbf{632.8\ nm}$. (Use 632.8, **not 633**.)

## Q5 — Level systems

Why can a two-level system never lase, and which type is Ruby?

> [!success]- Answer
> Boltzmann gives $N_2<N_1$ at equilibrium → net absorption; **two-level can never lase**. **Ruby is 3-level** (needs >50 % pumping, pulsed).

## Q6 — Thin-film derivation

Derive the condition for brightness for a thin film in **one** phase-change geometry, in three lines.

> [!success]- Answer
> ① Optical path difference $\Delta_{geom}=2\mu t\cos r$. ② Rare→dense at the top surface gives $+\lambda/2$; dense→rare at the bottom gives none → **one** $\lambda/2$. ③ Total $\Delta=2\mu t\cos r+\lambda/2$; bright when $\Delta=(2n-1)\lambda/2\Rightarrow 2\mu t\cos r=(2n-1)\lambda/2-n\lambda$ … simplify to **$2\mu t\cos r=(2n-1)\lambda/2$**.

## Q7 — Phase-change count

A soap film in **air** is viewed in reflected light. How many phase changes occur, and which bright/dark formulas apply?

> [!success]- Answer
> **One** phase change (air→film: rare→dense, $+\lambda/2$; film→air: dense→rare, none). Use the "**1 phase change**" row: bright $2\mu t\cos r=(2n-1)\lambda/2$, dark $2\mu t\cos r=n\lambda$.

## Q8 — YDSE fringe width

In a YDSE, $\lambda=600$ nm, $D=1$ m, slit separation $d=0.5$ mm. Find the fringe width, and its value if the whole setup is immersed in water ($\mu=1.33$).

> [!success]- Answer
> $\beta=\dfrac{\lambda D}{d}=\dfrac{600\times10^{-9}\times1}{0.5\times10^{-3}}=1.2\times10^{-3}\ \text{m}=\mathbf{1.2\ mm}$. In water: $\beta'=\dfrac{\beta}{\mu}=\dfrac{1.2}{1.33}=\mathbf{0.9\ mm}$.

## Q9 — Single slit

For a single slit of width $a=0.1$ mm and $\lambda=600$ nm, find the angle of the **2nd dark** fringe.

> [!success]- Answer
> $a\sin\theta=n\lambda\Rightarrow \sin\theta=\dfrac{2\times600\times10^{-9}}{0.1\times10^{-3}}=1.2\times10^{-2}\Rightarrow \theta\approx0.69°$.

## Q10 — Grating

A grating has spacing $d=2\ \mu$m and 10,000 lines, lit with $\lambda=600$ nm. (a) Highest order observable? (b) Resolving power in that order?

> [!success]- Answer
> (a) $d\sin\theta=n\lambda$, $\sin\theta\le1\Rightarrow n\le\dfrac{d}{\lambda}=\dfrac{2\times10^{-6}}{600\times10^{-9}}=3.33\Rightarrow n_{max}=\mathbf{3}$.
> (b) $R=nN=3\times10{,}000=\mathbf{30{,}000}$.

## Q11 — Laser identification

Identify type, λ, and whether CW is possible: (a) Ruby, (b) He-Ne, (c) Nd:YAG.

> [!success]- Answer
> (a) **3-level, 694.3 nm, pulsed.** (b) **4-level, 632.8 nm, CW.** (c) **4-level, 1064 nm, CW** (solid, W–kW).

## Score sheet

| Unit | Pass? | Flag |
|---|---|---|
| Einstein coeffs (Q1) | | |
| Threshold gain (Q2) | | |
| Cavity modes (Q3) | | |
| He-Ne λ (Q4) | | |
| Level systems (Q5, Q11) | | |
| Thin film (Q6, Q7) | | |
| YDSE (Q8) | | |
| Single slit + grating (Q9, Q10) | | |

## See also

- [[mse-revision-physics-lasers-slit]] · [[mse-flashcards-physics]] · [[mse-study-method]]
- [[lasers-quick-ref]] — faculty-verified (source of truth)
- [[module-1-optics-interference-diffraction]] · [[thin-film-interference-revision]] · [[module-1-addendum-sem1-numericals-derivations]]
- [[module-2-laser-fibre-question-bank]]
