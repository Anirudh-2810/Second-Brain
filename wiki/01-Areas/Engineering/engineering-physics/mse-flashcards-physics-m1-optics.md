---
course_code: "ENG-PHY"
course_name: "Engineering Physics"
unit: "MSE Flashcards — Module 1 Optics: Interference, Diffraction, Grating, Polarization"
date: "2026-10-19"
tags: [engineering-physics, optics, interference, ydse, thin-film, newtons-rings, grating, polarization, michelson, exam-prep, mse, flashcards]
last_updated: "2026-10-19"
confidence: high
description: "Flashcard deck for Engineering Physics MSE Module 1 (optics): coherence, YDSE + modifications, thin-film phase-flip conditions, Newton's rings, Fraunhofer diffraction, grating, Michelson, Malus/Brewster. Collapsible Q→A cards."
relations:
  depends_on: "[[mse-revision-physics-m1-optics]]"
  relates_to: "[[mse-flashcards-physics]]"
---

## For future agent

Flashcards for the Engineering Physics MSE **Module 1 (Optics)** — the interference/diffraction half that [[mse-flashcards-physics]] does not cover (that deck = lasers + slit). Question visible, answer in a collapsed `> [!success]- Answer` callout. Drill after reading [[mse-revision-physics-m1-optics]]; deep theory: [[module-1-optics-interference-diffraction]]. The thin-film condition table here is derived by flip-count (validated on AR coating + black central spot), consistent with the revision pack. Tagged `#mse #flashcards`.

# MSE Flashcards — Physics M1: Interference → Polarization

## Part A — Coherence & superposition

**C-1.** Why do two separate lamps never produce interference fringes?

> [!success]- Answer
> No coherence: independent sources have randomly changing phase differences; the maxima/minima swap faster than any detector resolves. Coherent sources are produced by splitting ONE wave (slits, biprism, Lloyd's mirror).

**C-2.** Define temporal coherence and give the coherence-length relation.

> [!success]- Answer
> The duration over which the phase of the wave stays predictable. $l_c = c\,\tau_c \approx \dfrac{\lambda^2}{\Delta\lambda}$ — the narrower the spectral width Δλ, the longer the coherence length (He-Ne ≈ kilometers; white light, millimeters).

**C-3.** Formula for resultant intensity of two superposed beams, and the special YDSE value.

> [!success]- Answer
> $I = I_1 + I_2 + 2\sqrt{I_1I_2}\cos\phi$. Equal slits (I₁=I₂=I₀): $I = 4I_0\cos^2(\phi/2)$ → maxima **4I₀**, minima 0.

## Part B — YDSE & modifications

**C-4.** Fringe-width formula and the bright/dark conditions.

> [!success]- Answer
> $\beta = \dfrac{\lambda D}{d}$. Bright: $\dfrac{xd}{D} = n\lambda$; Dark: $\dfrac{xd}{D} = (2n\pm1)\dfrac{\lambda}{2}$. Spacing identical for both families.

**C-5.** A thin sheet (μ, t) is put in front of ONE slit. What happens to the pattern?

> [!success]- Answer
> Central (whole) pattern shifts **toward the covered slit** by $y_0 = \dfrac{(\mu-1)tD}{d}$; fringe width unchanged. Sheet chosen so the shift = n fringes: $(\mu-1)t = n\lambda$.

**C-6.** The source (distance D₁ from slits) is moved sideways by δ. What happens?

> [!success]- Answer
> The whole fringe set shifts rigidly by $y_0 = \dfrac{\delta D_2}{D_1}$ (D₂ = slit–screen distance). β unchanged. Common trap: reciting β-changes — it doesn't.

**C-7.** The entire YDSE is submerged in liquid of refractive index μ. New fringe width?

> [!success]- Answer
> $\beta' = \dfrac{\beta}{\mu} = \dfrac{\lambda D}{\mu d}$ — use the in-medium wavelength λ/μ everywhere.

**C-8.** YDSE slit intensities are in ratio $I_1/I_2 = 4$. Find $I_{max}/I_{min}$.

> [!success]- Answer
> $I_{max}/I_{min} = \left(\dfrac{\sqrt{I_1}+\sqrt{I_2}}{\sqrt{I_1}-\sqrt{I_2}}\right)^2 = \left(\dfrac{2+1}{2-1}\right)^2 = \mathbf{9}$.

**C-9.** In white-light YDSE, which color fringe is nearest the center, and why?

> [!success]- Answer
> Violet (smallest λ → smallest x for a given order); red farthest. Over the orders the colors overlap — only the first 1–2 fringe pairs look colored, the center of ALL orders (n=0) stays white.

## Part C — Thin films (phase-flip counting)

**C-10.** When does a reflection add a π flip (effective λ/2)?

> [!success]- Answer
> Reflecting off a **higher-index** medium (lower→higher, solid→"denser"); from higher to lower = no flip. Count flips over BOTH reflections first, then apply the table.

**C-11.** Thin-film reflected-light conditions for k = 0 or 2 flips.

> [!success]- Answer
> Bright: $2\mu t\cos r = n\lambda$ · Dark: $2\mu t\cos r = (2n+1)\dfrac{\lambda}{2}$. (Check: MgF₂ AR coating = 2 flips, reflects dark at quarter-wave t = λ/4μ.)

**C-12.** Conditions for k = 1 flip (soap film in air; Newton's-rings air film).

> [!success]- Answer
> Bright: $2\mu t\cos r = (2n-1)\dfrac{\lambda}{2}$ · Dark: $2\mu t\cos r = n\lambda$. (Check: Newton's rings center t=0 → dark ✓; soap film turns black as it thins ✓.)

**C-13.** Minimum thickness of a k=1 film (μ) that reflects **bright** light of wavelength λ?

> [!success]- Answer
> $2\mu t = \dfrac{\lambda}{2} \Rightarrow t_{min} = \dfrac{\lambda}{4\mu}$ (n=1 in the bright condition). The film then reflects the **complementary** color — e.g. a film looks magenta in reflection because green is destructive there (and strongly transmitted).

## Part D — Newton's rings

**C-14.** Why is the Newton's-rings center DARK in reflected light?

> [!success]- Answer
> t = 0 at contact; the film is glass→air→glass with one flip (at glass plate reflection). k=1 dark condition $2\mu t\cos r = n\lambda$ is met at n = 0 — destructive interference, it fills black.

**C-15.** Diameter of the nth dark/bright ring?

> [!success]- Answer
> Dark: $D_n = \sqrt{4n\lambda R}$; Bright: $D_n = \sqrt{2(2n-1)\lambda R}$. Spacing shrinks as $1/\sqrt{n}$ — rings crowd outward.

**C-16.** A liquid of index μ fills the lens–plate gap. What happens to ring diameters?

> [!success]- Answer
> $D_n^2 = \dfrac{4n\lambda R}{\mu}$ → all diameters shrink by $1/\sqrt{\mu}$. Measuring the shrink gives μ.

## Part E — Diffraction & grating

**C-17.** Conditions for single-slit (width e) minima and secondary maxima.

> [!success]- Answer
> Minima: $e\sin\theta = n\lambda$. Secondary maxima ≈ $e\sin\theta = (2n+1)\dfrac{\lambda}{2}$, growing rapidly weaker (≈1/22 of central at first).

**C-18.** Angular width of the central maximum — and the double-trap.

> [!success]- Answer
> $\dfrac{2\lambda}{e}$ (between the ±1 minima) — **double** every other dark-to-dark spacing. Linear on screen: $\dfrac{2\lambda D}{e}$. Narrowing the slit (e↓) WIDENS the pattern.

**C-19.** Fresnel vs Fraunhofer diffraction — one line each.

> [!success]- Answer
> Fresnel: source & screen at finite distance, incident + diffracted waves curved, no lens needed, math hard. Fraunhofer: both effectively at infinity (lenses make it so), plane waves, sinθ linear math. MSE numericals = Fraunhofer unless stated.

**C-20.** Grating equation and the maximum visible order.

> [!success]- Answer
> $d\sin\theta = n\lambda$; $n_{max}$ = largest integer ≤ d/λ. Orders beyond that don't exist (sinθ > 1) — don't call them "dim".

**C-21.** A grating has 6000 lines/cm. Find d for λ = 600 nm usable orders.

> [!success]- Answer
> $d = \dfrac{1}{6000\ \text{cm}^{-1}} = 1.67\ \mu$m. d/λ = 2.78 → n = 0, 1, 2 visible (n=3 needs sinθ = 1.08 > 1).

**C-22.** Resolving power (RP) of a grating — formula and meaning.

> [!success]- Answer
> $RP = \dfrac{\lambda}{\Delta\lambda} = nN$ (n = order actually used, N = total illuminated rulings). More rulings or higher order → closer doublets resolved. Prism RP comes from material dispersion and is far lower.

**C-23.** Dispersive power of a grating?

> [!success]- Answer
> $\dfrac{d\theta}{d\lambda} = \dfrac{n}{d\cos\theta}$ — larger at higher orders and oblique angles (cosθ small).

## Part F — Michelson & polarization

**C-24.** Michelson: mirror moves Δd, N fringes cross. Find λ.

> [!success]- Answer
> $\lambda = \dfrac{2\Delta d}{N}$ — the arm is traversed twice. (Δd = 0.05 mm, N = 200 → λ = 500 nm.)

**C-25.** Malus' law chain: unpolarized I₀ through polarizers at 0°, 45°, 90°.

> [!success]- Answer
> P1: I₀/2. P2 (45°): I₀/2·cos²45 = I₀/4. P3 (90°, 45° from P2): I₀/4·cos²45 = **I₀/8**. Two "crossed" polarizers pass light once a middle 45° polarizer is inserted!

**C-26.** Brewster's law + value for glass (μ = 1.5).

> [!success]- Answer
> $\tan\theta_p = \mu$ → θₚ ≈ **56.3°**. At θₚ the reflected beam is completely plane-polarized (⊥ vibrations only) — its E vector lies parallel to the surface; glass at 56.3° acts as a polarizing mirror.

**C-27.** What does a λ/4 plate do at 45° input?

> [!success]- Answer
> Converts linear polarization to circular (and back). λ/2 plate rotates the plane by 2θ. Optical activity = rotation without a plate (sugar solutions).

## Exam traps checklist

- [ ] Phase-flip count done per-interface before any thin-film condition?
- [ ] Newton's rings: D vs r consistent; dark center assumed in reflection?
- [ ] Sheet-on-slit: shift direction toward covered slit; β unchanged?
- [ ] Liquid: λ/μ used everywhere?
- [ ] Grating d converted from "lines per cm"?
- [ ] sinθ > 1 → order absent?
- [ ] Michelson factor 2 included?
- [ ] Central maximum width = 2λ/e (double higher-order spacing)?
- [ ] First polarizer = I₀/2 always (Malus needs already-polarized input)?

## See also

- [[mse-revision-physics-m1-optics]] — formula tables + traps (source of truth for these cards)
- [[mse-recall-test-physics-m1-optics]] — numerical self-test over the same material
- [[mse-flashcards-physics]] — companion deck: lasers + slit
- [[mse-recall-test-physics]] · [[mse-revision-physics-lasers-slit]] — laser/slit drill set
- [[module-1-optics-interference-diffraction]] · [[thin-film-interference-revision]] · [[module-1-addendum-sem1-numericals-derivations]]
- [[mse-study-method]]
