---
course_code: "ENG-PHY"
course_name: "Engineering Physics"
unit: "MSE Revision — Module 1 Optics: Interference, Diffraction, Grating, Polarization"
date: "2026-10-19"
tags: [engineering-physics, optics, interference, ydse, thin-film, newtons-rings, grating, polarization, fraunhofer, exam-prep, mse, revision]
last_updated: "2026-10-19"
confidence: high
description: "MSE revision pack for Engineering Physics Module 1 (optics): coherence, YDSE + modifications, thin-film conditions, Newton's rings, Fraunhofer diffraction, grating orders/resolving power, Malus/Brewster. Formula tables + traps. Companion to the lasers/slit MSE pack."
relations:
  relates_to: "[[mse-revision-physics-lasers-slit]]"
---

## For future agent

Exam-facing consolidation of Engineering Physics **Module 1 (Optics)** for the MSE — the **interference/diffraction core** that [[mse-revision-physics-lasers-slit]] did not cover (that pack owns lasers + the slit decision table). Recall surface: formulas, conditions tables, YDSE-modification results, traps. Deep theory + 12 worked numericals live in [[module-1-optics-interference-diffraction]]; thin-film derivation detail in [[thin-film-interference-revision]]; source-solved grating numericals in [[module-1-addendum-sem1-numericals-derivations]]. If a formula here disagrees with the module page, the module page wins. Phase-change convention here derived from first principles (tested against the quarter-wave AR coating and Newton's-rings black center — both check out). As of 2026-10-19.

# MSE Revision — Physics M1 Optics (Interference → Polarization)

## 1. Coherence (what makes fringes possible)

- Two sources interfere visibly only if **coherent**: constant phase difference + same frequency.
- **Temporal coherence**: coherence **length** $l_c \approx c\,\tau_c \approx \dfrac{\lambda^2}{\Delta\lambda}$ (narrower spectrum → longer coherence). He-Ne is long-coherence; white light gives only a few centimeters→few fringes.
- Two independent lamps never show fringes: their phases randomize faster than any detector resolves. That is why every interference apparatus **splits one source** (YDSE slits, biprism, Lloyd's mirror) — it manufactures two coherent copies of one wave.
- ELI5: two kids splashing at random → mush; two copies of the SAME splash beam → a clean wave pattern.

## 2. Young's Double Slit (YDSE)

| Quantity | Formula |
|---|---|
| Bright (path difference) | $\dfrac{xd}{D} = n\lambda$ |
| Dark | $\dfrac{xd}{D} = (2n\pm1)\dfrac{\lambda}{2}$ |
| **Fringe width** | $\beta = \dfrac{\lambda D}{d}$ (bright-to-bright = dark-to-dark) |
| Screen intensity | $I = 4I_0\cos^2\!\dfrac{\phi}{2},\quad \phi = \dfrac{2\pi}{\lambda}\dfrac{xd}{D}$ |
| $I_{max}/I_{min}$ (slit amplitudes a₁,a₂) | $\left(\dfrac{a_1+a_2}{a_1-a_2}\right)^2 = \left(\dfrac{\sqrt{I_1}+\sqrt{I_2}}{\sqrt{I_1}-\sqrt{I_2}}\right)^2$ |
| White light | center white, colors overlap increasingly; only the first 1–2 fringe pairs look cleanly colored (violet end nearest center) |

### Modifications — each is one exam numerical

| Change | Effect | Formula |
|---|---|---|
| Thin sheet (μ, t) in front of one slit | Whole pattern shifts **toward the covered slit**; β unchanged | extra path $(\mu-1)t$ → $y_0 = \dfrac{(\mu-1)t\,D}{d}$; shifted by n fringes ⇒ $(\mu-1)t = n\lambda$ |
| Source moved δ sideways (source→slit distance D₁, slit→screen D₂) | Pattern shifts rigidly toward the side | $y_0 = \dfrac{\delta\,D_2}{D_1}$ |
| Setup in liquid (μ) | β shrinks | $\beta' = \dfrac{\beta}{\mu} = \dfrac{\lambda D}{\mu d}$ |
| Slit widths unequal (I₁, I₂) | visibility | use the intensity-ratio row above |

⚠️ In every "modified" case: **fringe width never changes, only position/counting does.** The worked sheet-on-one-slit numerical: [[module-1-optics-interference-diffraction]] Example 1.

## 3. Thin-film interference (parallel film, index μ, refraction angle r)

Optical path difference between the two reflected rays: $2\mu t\cos r$, **plus** λ/2 per phase flip on reflection (flip happens only when REFLECTING OFF A HIGHER-index medium — Stokes' rule).

| Phase flips (k) | Reflected BRIGHT | Reflected DARK |
|---|---|---|
| **0 or 2** (e.g. MgF₂-on-glass AR coating — flip at both faces) | $2\mu t\cos r = n\lambda$ | $2\mu t\cos r = (2n+1)\dfrac{\lambda}{2}$ |
| **1** (soap film in air; air film in Newton's rings) | $2\mu t\cos r = (2n-1)\dfrac{\lambda}{2}$ | $2\mu t\cos r = n\lambda$ |

Why the one-flip row matters (checks): quarter-wave AR coating (k=2, two flips) reflects DARK at $2\mu t = \lambda/2$ → t = λ/4μ ✓; Newton's-rings air film (k=1) reflects DARK at thickness 0 ✓ (black central spot). Transmitted-light conditions are the **complement** of the reflected row (energy conservation).

- Count flips by looking at each interface: air→denser = flip; denser→air = no flip.
- Minimum **bright-reflection** film for k=1: $t_{min} = \dfrac{\lambda}{4\mu}$; minimum dark for k=0/2: $t = \dfrac{\lambda}{4\mu}$.
- Derivation (3 steps: path diff, phase count, conditions): [[thin-film-interference-revision]].

## 4. Newton's rings (plano-convex lens on glass plate; air film k=1; t = r²/2R)

| | Reflected light (standard) |
|---|---|
| Central spot | **Dark** (t = 0 hits the k=1 dark condition $2\mu t\cos r = n\lambda$ with n=0) |
| Dark rings | $D_n^2 = 4n\lambda R$ |
| Bright rings | $D_n^2 = 2(2n-1)\lambda R$ |
| Liquid μ in the gap | all diameters shrink: $D_n^2 = \dfrac{4n\lambda R}{\mu}$ |
| Spacing | $\Delta D \propto \dfrac{1}{\sqrt{n}}$ — rings crowd outward |
| Metrology | slope of $D^2$ vs n gives $4\lambda R$ → measure λ (or R) from one slope |

⚠️ Keep D (diameter) and r (radius) consistent: every formula above uses **D = 2r** — the classic half-mark-eater.

## 5. Fraunhofer single slit (width e)

| Feature | Condition / size |
|---|---|
| Dark minima | $e\sin\theta = n\lambda$ |
| Secondary maxima (approx.) | $e\sin\theta \approx (2n+1)\dfrac{\lambda}{2}$; intensity ≈ 1/22, 1/62, … of central |
| Central maximum | spans the two n=±1 minima; **angular width $\dfrac{2\lambda}{e}$** (double any other), linear width $\dfrac{2\lambda D}{e}$ |
| Fresnel vs Fraunhofer | Fresnel = finite source/screen distance, no lens, hard math; Fraunhofer = both at ∞ (lenses), simple sinθ math. Slit problems at MSE level are Fraunhofer unless stated |

## 6. Diffraction grating (N rulings, spacing $d = \frac{1}{\text{lines per m}}$)

- Principal maxima: $\;d\sin\theta = n\lambda$.
- **Maximum visible order:** $n_{max} \le \dfrac{d}{\lambda}$ (sinθ ≤ 1); e.g. d/λ = 2.4 → orders 0, 1, 2 (orders above absent, not dim).
- Between adjacent principal maxima: $N-1$ minima and $N-2$ weak secondary maxima → more rulings = sharper principal maxima.
- **Dispersive power:** $\dfrac{d\theta}{d\lambda} = \dfrac{n}{d\cos\theta}$
- **Resolving power:** $RP = \dfrac{\lambda}{\Delta\lambda} = nN$ (n = order, N = total illuminated rulings)
- Grating vs prism: grating disperses via interference, linear in n, high controllable RP; prism via material dispersion (nonlinear, low RP).
- Source-solved grating numericals: [[module-1-addendum-sem1-numericals-derivations]] §3.

## 7. Michelson interferometer

Mirror moved by Δd → N fringes cross: light travels the arm twice, so

$$\lambda = \frac{2\,\Delta d}{N}$$

(Uses: λ measurement, uniform film/flatness testing.) The classic trap is forgetting the **factor 2**.

## 8. Polarization (light is a transverse wave)

| Item | Formula / fact |
|---|---|
| Unpolarized → one polarizer | $I = \dfrac{I_0}{2}$ |
| Malus' law (θ between axes) | $I = I_0\cos^2\theta$ (chain the cos² for stacked polarizers) |
| Brewster angle (reflected beam fully plane-polarized, ⊥ to the plane of incidence) | $\tan\theta_p = \mu$ → glass 1.5: θₚ ≈ 56.3° |
| λ/4 plate | linear (45° in) ↔ circular polarization |
| λ/2 plate | rotates the polarization plane by 2θ |

## 9. Formula pocket-grid

| Area | Bright | Dark | Spacing/extra |
|---|---|---|---|
| YDSE | xd/D = nλ | (2n±1)λ/2 | β = λD/d |
| Thin film, k=0/2 | 2μtcos r = nλ | (2n+1)λ/2 | min *dark* film: λ/4μ |
| Thin film, k=1 | (2n−1)λ/2 | 2μtcos r = nλ | min *bright* film: λ/4μ |
| Newton's rings (refl.) | 2(2n−1)λR | 4nλR | ΔD ∝ 1/√n |
| Single slit | (2n+1)λ/2 (approx.) | nλ | central width 2λ/e angular |
| Grating | d sinθ = nλ | — | RP = nN |
| Michelson | 2Δd = Nλ | — | λ = 2Δd/N |

## 10. Exam traps

1. **Count phase flips FIRST** — k=0/2 vs k=1 swaps bright↔dark in thin films. Soap film in air: air→film flip + film→air no-flip = k=1 → bright = odd λ/2, film turns "black" just before popping (t→0). Never copy a row without checking the interface indices.
2. Newton's rings: **dark** central spot in reflected light is the default — if your answer says bright center, re-check the flip count.
3. YDSE sheet-on-one-slit: central fringe moves **toward the covered slit** (the covered side needs less geometry to reach the same extra path), β unchanged.
4. White light YDSE: the **violet** fringe sits nearest the center (smallest λ), red farthest.
5. Grating: "6000 lines per cm" ⇒ d = 1/6000 cm; never use the line count as d.
6. sin θ > 1 → that order **does not exist**. Count 0 too (the central image).
7. Liquid problems: use λ_medium = λ/μ in EVERY formula (YDSE β, Newton D², path difference).
8. Michelson: the arm is traversed twice — λ = 2Δd/N, not Δd/N.
9. First polarizer on unpolarized light: always exactly I₀/2 regardless of θ.
10. Intensity at YDSE maxima = 4I₀ (two coherent slits of I₀ each), not 2I₀.

## Cross-Links

- [[mse-revision-physics-lasers-slit]] — companion MSE pack: lasers (M2) + slit decision table
- [[mse-flashcards-physics-m1-optics]] — this pack as drill cards
- [[mse-recall-test-physics-m1-optics]] — this pack as a self-test with worked key
- [[mse-flashcards-physics]] [[mse-recall-test-physics]] — laser + slit drill set
- [[module-1-optics-interference-diffraction]] · [[thin-film-interference-revision]] · [[module-1-addendum-sem1-numericals-derivations]] — deep theory + solved sources
- [[01-Areas/Engineering/engineering-physics/overview|Physics Module Hub]] · [[mse-study-method]] · [[mse-2026-10-26-5-day-plan]]
