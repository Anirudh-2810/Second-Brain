---
course_code: "ENG-PHY"
course_name: "Engineering Physics"
unit: "MSE Revision — Lasers + Slit/Diffraction Theory"
date: "2026-10-15"
tags: [engineering-physics, lasers, optics, interference, diffraction, slit, thin-film, exam-prep, mse, revision]
last_updated: "2026-10-16"
description: "MSE revision pack for Engineering Physics — lasers (Einstein coefficients, inversion, threshold gain, cavity modes) and slit/diffraction theory (YDSE, single slit, grating, thin film, Newton's rings) with watch-numbers and traps."
confidence: high
---

## For future agent

Exam-facing consolidation of **Engineering Physics (Physics-B)** covering **lasers (Module 2)** and **slit / wave-optics theory (Module 1)** for the MSE. Recall surface — formulas, decision tables, watch-numbers, traps — linking the deep pages: [[lasers-quick-ref]] (lasers, faculty-verified), [[module-1-optics-interference-diffraction]] (slit/interference, source of truth), [[thin-film-interference-revision]], [[module-1-addendum-sem1-numericals-derivations]]. Where a number here disagrees with a deep page, the deep page wins. Two faculty corrections matter (He-Ne metastable 18.7 eV; He-Ne coherence ≈ 2 km). As of 2026-10-15.

# MSE Revision — Physics: Lasers + Slit Theory

## Part A — Lasers (deep: [[lasers-quick-ref]])

### Three processes & Einstein relations
| Process | Rate | Character |
|---|---|---|
| Absorption | $B_{12}\rho(\nu)N_1$ | photon absorbed |
| Spontaneous emission | $A_{21}N_2$ | random phase/dir → **incoherent** (bulb/LED) |
| Stimulated emission | $B_{21}\rho(\nu)N_2$ | identical copy → **coherent** → laser |

$$\boxed{g_1B_{12} = g_2B_{21}} \qquad \boxed{A_{21} = \frac{8\pi h\nu^3}{c^3}B_{21}} \qquad \tau_{spon} = \frac{1}{A_{21}}$$

$A_{21}/B_{21}\propto\nu^3$ → stimulated emission relatively more important at low frequency; at optical frequencies spontaneous dominates → **need population inversion**.

### Population inversion & level systems
- Boltzmann: $N_2/N_1 = (g_2/g_1)e^{-h\nu/k_BT}$ → $N_2<N_1$ at equilibrium. **Two-level can never lase.**
- **3-level** (e.g. Ruby 694.3 nm): need >50% pumped, high threshold, **pulsed**.
- **4-level** (He-Ne, Nd:YAG, CO₂): lower level nearly empty, low threshold, **CW** possible.
- **Metastable** state (~10⁻³ s vs 10⁻⁸ s) lets atoms accumulate — prerequisite for inversion.

### Threshold & resonator
Three simultaneous conditions: inversion + optical resonator + round-trip gain ≥ loss.

$$R_1R_2\,e^{2(g-\alpha)l} \ge 1 \qquad \boxed{g_{th} = \alpha + \frac{1}{2l}\ln\!\left(\frac{1}{R_1R_2}\right)}$$

⚠️ **Notation split (state the one your faculty wants):** general textbooks use $l$ = **gain-medium length**; Dr. Suren Patwardhan (SVU R-2023) writes $\gamma = \alpha_C + \frac{1}{2L}\ln\frac{1}{R_1R_2}$ with $L$ = **cavity length** (medium fills cavity). Use the faculty form when the derivation is credited.

### Cavity modes
$$\nu_q = q\frac{c}{2L} \qquad \Delta\nu = \frac{c}{2L} \qquad q = \frac{2L}{\lambda} \qquad N_{modes} = \frac{\Delta\nu_{gain}}{\Delta\nu}$$

- Mode spacing depends **only on cavity length**. **TEM₀₀** = fundamental Gaussian (lowest divergence). Stability $0 \le g_1g_2 \le 1$, $g_i = 1-L/R_i$.

### Laser type table (memorize the λ column)
| Laser | Type | λ | Note |
|---|---|---|---|
| Ruby | 3-level | 694.3 nm | Cr³⁺:Al₂O₃, pulsed |
| **He-Ne** | 4-level | **632.8 nm** | sig. gas laser, CW |
| Nd:YAG | 4-level | 1064 nm | solid, W–kW |
| CO₂ | 4-level | 10.6 μm | ~10–20% efficient |
| GaAs | semiconductor | 870 nm | $E_g=1.42$ eV |
| ArF excimer | excimer | 193 nm | LASIK |

Semiconductor diode: $\lambda = 1240/E_g$(eV·nm). Below $J_{th}$ = LED, above = laser.

### Characteristics
$l_c = \lambda^2/\Delta\lambda$ · divergence $\theta=(d_1-d_2)/(Z_1-Z_2)$ · rate ratio $R=e^{h\nu/kT}-1$ (R=1 ⇒ T ≈ 4.16×10⁴ K at 5000 Å ⇒ inversion is mandatory).

⚠️ **Watch-numbers:** He-Ne **632.8 nm (not 633)**; single-mode cutoff **V = 2.405**; He-Ne metastable **18.7 & 20.66 eV**; He-Ne coherence **≈ 2 km** (faculty), not 200 m.

### Must-reproduce numericals
(a) $A_{21}=1/\tau=4.0\times10^7$ s⁻¹ → $B_{21}$ via Einstein. (b) $g_{th}$ from $R_1,R_2,l,\alpha$. (c) $\Delta\nu=c/2L$, $q=2L/\lambda$, $N=\Delta\nu_{gain}/\Delta\nu$. (d) He-Ne: $\lambda=1240/(E_2-E_1)$.

## Part B — Slit & diffraction theory (deep: [[module-1-optics-interference-diffraction]])

### Decision table — bright vs dark (the single most useful thing)
| Setup | Bright (maxima) | Dark (minima) |
|---|---|---|
| **YDSE** (path diff $=d\sin\theta$) | $d\sin\theta = n\lambda$ | $d\sin\theta = (2n-1)\lambda/2$ |
| **Thin film** 1 phase change (reflected) | $2\mu t\cos r = (2n-1)\lambda/2$ | $2\mu t\cos r = n\lambda$ |
| **Thin film** 0 or 2 phase changes | $2\mu t\cos r = n\lambda$ | $2\mu t\cos r = (2n-1)\lambda/2$ |
| **Newton's rings** (reflected) | — | $r_n = \sqrt{n\lambda R}$ dark; $r_n=\sqrt{(n+\tfrac12)\lambda R}$ bright |
| **Single slit** (width $a$) | $a\sin\theta = (2n+1)\lambda/2$ | $a\sin\theta = n\lambda$ |
| **Grating** (spacing $d$) | $d\sin\theta = n\lambda$ | — |

- **Fringe width (YDSE):** $\beta = \lambda D/d$. In a medium of index $\mu$: $\beta = \lambda D/(\mu d)$.
- **Single-slit** central maximum twice as wide as others; condition for $n$-th dark is $a\sin\theta = n\lambda$.
- **Grating:** resolving power $R = nN$; missing orders when a slit-diffraction minimum coincides with an interference maximum.
- **Transmitted vs reflected** thin film are **complementary** (bright ↔ dark swap).

### Thin-film derivation (3 lines)
1. Optical path difference $\Delta_{geom} = 2\mu t\cos r$ (uses Snell; collapses cleanly).
2. Phase change: rare→dense (top, film in air) gives +λ/2; dense→rare gives none → **one** λ/2 total.
3. Total $\Delta = 2\mu t\cos r + \lambda/2$ → substitute into bright/dark conditions.

**Anti-reflection coating:** $\mu t = \lambda/4$ → reflected rays cancel (dark).

## Exam traps checklist

1. Count **phase changes first** (0/1/2) — it decides whether bright/dark formulas flip.
2. Use **optical** path $\mu t$, never bare $t$.
3. He-Ne = **632.8 nm**, not 633; single-mode V = **2.405**.
4. Two-level can't lase; Ruby is **3-level**.
5. $g_{th}$: match the notation your faculty uses ($l$ gain-medium vs $L$ cavity).
6. Mode spacing depends only on $L$, not λ.
7. YDSE vs single-slit have **inverted** bright/dark conditions — don't mix them.

## See also

- [[lasers-quick-ref]] — faculty-verified laser sheet (source of truth for lasers)
- [[module-1-optics-interference-diffraction]] — slit/interference deep page
- [[thin-film-interference-revision]] · [[module-1-addendum-sem1-numericals-derivations]] — thin film + worked numericals
- [[module-2-laser-fibre-question-bank]] — full theory + worked numericals
- [[source-map-physics-sem1]] — remaining un-ingested laser/fibre sources
- [[mse-flashcards-physics]] — flashcard deck (collapsible answers)
- [[mse-recall-test-physics]] — numerical + derivation self-test + worked key
- [[mse-study-method]] — how to run the decks (units, not hours)
- [[mse-2026-10-26-5-day-plan]] — the day-by-day plan this pack feeds
