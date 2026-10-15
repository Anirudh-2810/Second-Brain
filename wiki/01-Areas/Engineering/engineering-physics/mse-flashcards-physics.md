---
course_code: "ENG-PHY"
course_name: "Engineering Physics"
unit: "MSE Flashcards — Lasers + Slit/Diffraction"
date: "2026-10-16"
tags: [engineering-physics, lasers, optics, interference, diffraction, slit, thin-film, exam-prep, mse, flashcards]
last_updated: "2026-10-16"
confidence: high
description: "Flashcard deck for Engineering Physics MSE — lasers (Einstein relations, level systems, threshold gain, cavity modes, laser table) and slit/diffraction theory (YDSE, single slit, grating, thin film, Newton's rings) with watch-numbers and traps. Collapsible callout cards."
relations:
  depends_on: "[[mse-revision-physics-lasers-slit]]"
  relates_to: "[[mse-recall-test-physics]]"
---

## For future agent

Flashcards for the **Engineering Physics MSE** (Physics-B): **lasers (Module 2)** + **slit / wave-optics (Module 1)**. Question always visible; answer in a collapsed `> [!success]- Answer` callout. Source of truth: [[lasers-quick-ref]] (faculty-verified — He-Ne metastable 18.7 eV, coherence ≈ 2 km) and [[module-1-optics-interference-diffraction]]. Two faculty corrections matter (see watch-numbers). Run per [[mse-study-method]]. Tagged `#mse #flashcards`.

# MSE Flashcards — Physics: Lasers + Slit Theory

Pack: [[mse-revision-physics-lasers-slit]] · Test: [[mse-recall-test-physics]] · Plan: [[mse-2026-10-26-5-day-plan]]

## Part A — Lasers: processes & Einstein relations

**P‑01.** Name the three radiative processes.

> [!success]- Answer
> **Absorption**, **spontaneous emission**, **stimulated emission**.

**P‑02.** Give the rate expression for each process.

> [!success]- Answer
> Absorption $B_{12}\rho(\nu)N_1$ · Spontaneous $A_{21}N_2$ · Stimulated $B_{21}\rho(\nu)N_2$.

**P‑03.** Which emission is incoherent and which is coherent?

> [!success]- Answer
> **Spontaneous** → random phase/direction → **incoherent** (bulb/LED). **Stimulated** → identical copy → **coherent** → laser.

**P‑04.** State the three Einstein relations.

> [!success]- Answer
> $g_1B_{12}=g_2B_{21}$; $A_{21}=\dfrac{8\pi h\nu^{3}}{c^{3}}B_{21}$; $\tau_{spon}=\dfrac{1}{A_{21}}$.

**P‑05.** What does $A_{21}/B_{21}\propto\nu^{3}$ imply?

> [!success]- Answer
> Stimulated emission is relatively more important at **low** frequency; at **optical** frequencies spontaneous emission dominates → **population inversion is mandatory** for a laser.

## Part A — Level systems

**P‑06.** From the Boltzmann relation, why can a two-level system never lase?

> [!success]- Answer
> $N_2/N_1=(g_2/g_1)e^{-h\nu/k_BT}$ ⇒ $N_2<N_1$ at equilibrium — no inversion, so net absorption. **Two-level can never lase.**

**P‑07.** Three-level laser — example, threshold, regime?

> [!success]- Answer
> e.g. **Ruby (694.3 nm)**; needs **>50 %** of atoms pumped, **high threshold**, **pulsed** operation.

**P‑08.** Four-level laser — examples, and why it lases so much more easily?

> [!success]- Answer
> He-Ne, Nd:YAG, CO₂. The lower level is **nearly empty**, so inversion is easy: **low threshold**, **CW** possible.

**P‑09.** What is a metastable state and why does it matter?

> [!success]- Answer
> A long-lived excited state (~$10^{-3}$ s vs the usual $10^{-8}$ s); atoms **accumulate** there — a prerequisite for population inversion.

## Part A — Threshold & resonator

**P‑10.** What three conditions must hold simultaneously for laser action?

> [!success]- Answer
> Population **inversion** + an **optical resonator** + round-trip **gain ≥ loss**.

**P‑11.** State the round-trip gain condition.

> [!success]- Answer
> $R_1R_2\,e^{2(g-\alpha)l}\ge1$.

**P‑12.** Write the threshold gain $g_{th}$.

> [!success]- Answer
> $g_{th}=\alpha+\dfrac{1}{2l}\ln\!\left(\dfrac{1}{R_1R_2}\right)$.

**P‑13.** State the two notations for $g_{th}$ (general vs faculty).

> [!success]- Answer
> General textbooks: $l=$ **gain-medium length**. Dr. Suren Patwardhan (SVU R-2023): $\gamma=\alpha_C+\dfrac{1}{2L}\ln\dfrac{1}{R_1R_2}$ with $L=$ **cavity length**. Use the **faculty form** when the derivation is credited.

## Part A — Cavity modes

**P‑14.** Mode frequency and mode spacing?

> [!success]- Answer
> $\nu_q=q\dfrac{c}{2L}$; $\Delta\nu=\dfrac{c}{2L}$.

**P‑15.** Mode number and number of modes in the gain bandwidth?

> [!success]- Answer
> $q=\dfrac{2L}{\lambda}$; $N_{modes}=\dfrac{\Delta\nu_{gain}}{\Delta\nu}$.

**P‑16.** Does mode spacing depend on wavelength or cavity length?

> [!success]- Answer
> **Cavity length only** ($\Delta\nu=c/2L$).

**P‑17.** What is TEM₀₀, and the resonator stability condition?

> [!success]- Answer
> TEM₀₀ = fundamental **Gaussian** mode (lowest divergence). Stability: $0\le g_1g_2\le1$ with $g_i=1-L/R_i$.

## Part A — Laser types (memorize the λ column)

**P‑18.** Ruby laser — type, λ, medium, regime?

> [!success]- Answer
> **3-level**, **694.3 nm**, Cr³⁺:Al₂O₃, **pulsed**.

**P‑19.** He-Ne — type and λ?

> [!success]- Answer
> **4-level**, **632.8 nm**, CW gas.

**P‑20.** Nd:YAG + CO₂ — λ and type?

> [!success]- Answer
> Nd:YAG: 4-level, **1064 nm** (solid, W–kW). CO₂: 4-level, **10.6 μm** (~10–20 % efficient).

**P‑21.** GaAs + ArF excimer — λ and note?

> [!success]- Answer
> GaAs: semiconductor, **870 nm**, $E_g=1.42$ eV. ArF excimer: **193 nm** (LASIK).

**P‑22.** Semiconductor laser — λ from band gap, and the LED/laser threshold?

> [!success]- Answer
> $\lambda=\dfrac{1240}{E_g(\text{eV})}$ (nm). Below $J_{th}$ it is an **LED**; above, a **laser**.

## Part A — Characteristics & watch-numbers

**P‑23.** Coherence length, divergence, and the rate-ratio check?

> [!success]- Answer
> $l_c=\dfrac{\lambda^{2}}{\Delta\lambda}$ · divergence $\theta=\dfrac{d_1-d_2}{Z_1-Z_2}$ · $R=e^{h\nu/kT}-1$ (R=1 ⇒ T ≈ 4.16×10⁴ K at 5000 Å ⇒ inversion mandatory).

**P‑24.** State the four He-Ne watch-numbers.

> [!success]- Answer
> λ = **632.8 nm** (not 633) · single-mode cutoff **V = 2.405** · metastable **18.7 & 20.66 eV** · coherence **≈ 2 km** (faculty), not 200 m.

**P‑25.** Four "must-reproduce" laser numericals?

> [!success]- Answer
> (a) $A_{21}=1/\tau=4.0\times10^{7}$ s⁻¹ → $B_{21}$ via Einstein. (b) $g_{th}$ from $R_1,R_2,l,\alpha$. (c) $\Delta\nu=c/2L$, $q=2L/\lambda$, $N=\Delta\nu_{gain}/\Delta\nu$. (d) He-Ne $\lambda=1240/(E_2-E_1)$.

## Part B — Slit & diffraction: decision table

**P‑26.** YDSE bright vs dark?

> [!success]- Answer
> Bright $d\sin\theta=n\lambda$ · dark $d\sin\theta=(2n-1)\lambda/2$.

**P‑27.** Thin film, **one** phase change (reflected) — bright vs dark?

> [!success]- Answer
> Bright $2\mu t\cos r=(2n-1)\lambda/2$ · dark $2\mu t\cos r=n\lambda$.

**P‑28.** Thin film, **0 or 2** phase changes — bright vs dark?

> [!success]- Answer
> Bright $2\mu t\cos r=n\lambda$ · dark $2\mu t\cos r=(2n-1)\lambda/2$.

**P‑29.** Newton's rings (reflected) — dark and bright radii?

> [!success]- Answer
> Dark $r_n=\sqrt{n\lambda R}$; bright $r_n=\sqrt{(n+\tfrac12)\lambda R}$.

**P‑30.** Single slit (width $a$) bright vs dark?

> [!success]- Answer
> Bright $a\sin\theta=(2n+1)\lambda/2$ · dark $a\sin\theta=n\lambda$. (Central max is **twice** as wide as the others.)

**P‑31.** Grating (spacing $d$) maxima, resolving power, and missing orders?

> [!success]- Answer
> Maxima $d\sin\theta=n\lambda$; resolving power $R=nN$; **missing orders** occur when a slit-diffraction minimum coincides with an interference maximum.

**P‑32.** YDSE fringe width, and its value inside a medium?

> [!success]- Answer
> $\beta=\dfrac{\lambda D}{d}$; in a medium of index $\mu$: $\beta=\dfrac{\lambda D}{\mu d}$.

**P‑33.** Relation between transmitted and reflected thin-film patterns?

> [!success]- Answer
> They are **complementary** — bright ↔ dark swap.

## Part B — Thin-film derivation

**P‑34.** Three lines of the thin-film derivation?

> [!success]- Answer
> ① Optical path difference $\Delta_{geom}=2\mu t\cos r$ (uses Snell). ② Phase change: rare→dense gives $+\lambda/2$, dense→rare gives none → **one** $\lambda/2$ total. ③ Total $\Delta=2\mu t\cos r+\lambda/2$ → substitute into the bright/dark conditions.

**P‑35.** Anti-reflection coating condition?

> [!success]- Answer
> $\mu t=\dfrac{\lambda}{4}$ → the two reflected rays cancel (**dark**).

## Exam traps checklist

**P‑36.** First thing to do in any thin-film problem?

> [!success]- Answer
> **Count the phase changes (0/1/2)** — it decides whether the bright/dark formulas flip.

**P‑37.** Which thickness enters the thin-film formula?

> [!success]- Answer
> The **optical** path $\mu t$, never the bare $t$.

**P‑38.** Two "gotcha" numbers to not round?

> [!success]- Answer
> He-Ne = **632.8 nm** (not 633); single-mode **V = 2.405**.

**P‑39.** Which two facts about laser level systems are most examined?

> [!success]- Answer
> **Two-level can't lase**; **Ruby is 3-level** (needs >50 % pumping, pulsed).

**P‑40.** What does mode spacing depend on, and what is the common error?

> [!success]- Answer
> **Only the cavity length $L$** ($\Delta\nu=c/2L$) — *not* λ.

**P‑41.** YDSE vs single-slit — what is the classic mistake?

> [!success]- Answer
> Their **bright/dark conditions are inverted** — do not mix them up.

## See also

- [[mse-revision-physics-lasers-slit]] — the revision pack
- [[mse-recall-test-physics]] — numerical/derivation self-test
- [[lasers-quick-ref]] — faculty-verified laser sheet (source of truth)
- [[module-1-optics-interference-diffraction]] · [[thin-film-interference-revision]] · [[module-1-addendum-sem1-numericals-derivations]]
- [[module-2-laser-fibre-question-bank]] · [[mse-study-method]]
