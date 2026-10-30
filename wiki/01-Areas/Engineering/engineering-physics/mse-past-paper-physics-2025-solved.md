---
course_code: "316U06C102"
course_name: "Engineering Physics"
unit: "MSE (full paper)"
tags: [btech, engineering-physics, thin-film, interference, laser, fiber-optics, resolving-power, numericals, exam-prep, mse, past-paper]
last_updated: "2026-10-21"
confidence: high
date: "2026-10-21"
description: "Solved walkthrough of the Aug-Dec 2025 Engineering Physics MSE paper (midsems-pyp.pdf): thin-film OPD derivation, laser pumping + threshold, numerical aperture derivation, resolving power, and all three Q3 numericals solved step-by-step (soap film, Boltzmann ratio, grating) with similar problems and yield ratings."
---

## For future agent
Full walkthrough of the actual **Augâ€“Dec 2025 Engineering Physics MSE paper** (source: [[raw-sources/midsems-pyp.pdf|midsems-pyp.pdf]], 30 marks, 1 hr 15 min; useful data printed on the paper â€” e, m_e, h, k, Îµâ‚€, Î¼â‚€, N_A). Derivation-style theory Q1/Q2 (any 2 of 3, 5M each) + compulsory numericals Q3. Deep theory: [[module-1-optics-interference-diffraction]], [[module-2-optoelectronics-lasers-fiber-optics]]. As of 2026-10-21.

# Engineering Physics MSE 2025 â€” Solved Paper Walkthrough

## Pattern & verdict

| Q | Type | Marks | Difficulty | Yield |
|---|------|-------|-----------|-------|
| Q1 | Any 2 of 3: thin-film OPD / pumping schemes / threshold condition | 5+5 | Med (diagrams!) | â­â­ |
| Q2 | Any 2 of 3: NA derivation / film colours / resolving power | 5+5 | Med | â­â­ |
| Q3 | Any 2 of 3 numericals | 5+5 | Easy-med (plug-in) | â­â­â­ |

**Verdict: marks live in memorised derivations + 3 formulas for Q3.** The numericals are cheaper than the derivations â€” drill Q3 first.

---

## Q1.a (5M) â€” Optical path difference, thin film of uniform thickness

**The idea:** light bouncing inside a thin film travels a bit extra *and* the extra distance is measured in "wavelengths of the film material", not air. Drawing the two reflected rays and writing that extra distance IS the derivation.

**Skeleton answer (the marks-chasing order):**
1. **Diagram (1-1.5M):** thin film Î¼, thickness t; incident ray at angle i; refracted ray at angle r; mark the upper reflection (at top surface) and the lower one (reflected from bottom surface, travels t up-down).
2. **Geometry:** the lower ray travels an extra path inside the film, $AB+BC = 2t\cos r$ measured as film-wavelength-distance; multiply by Î¼ to convert to air-equivalent/wavelength terms.
3. **Phase flip:** the top-surface reflection (airâ†’denser) picks up a 180Â° phase change = extra Î»/2.
4. **Result:**

$$\text{Effective O.P.D. (reflected)} = 2\mu t\cos r \pm \frac{\lambda}{2} \approx 2\mu t \ \text{(near-normal incidence, with the }\pm\tfrac\lambda2\text{ flip)}$$

5. Map to conditions: reflected **bright** when 2Î¼t cos r = (2nâˆ’1)Î»/2; reflected **dark** when 2Î¼t cos r = nÎ» (transmitted is the exact opposite â€” that fact is Q2.b).

**Similar problems:** wedge film (2Î¼tÂ·cos r via wedge angle), Newton's rings (same formula + rÂ²â‰ˆ geometry), why soap bubbles show colours â†’ [[thin-film-interference-revision]], [[module-1-optics-interference-diffraction]].

---

## Q1.b (5M) â€” Pumping schemes: 4-level vs 3-level

**The idea:** you can't lase until most atoms sit in the upper level. Pumping = any trick to drag them up there. The schemes named in class:

| Scheme | How it works | Example |
|--------|--------------|---------|
| **Optical pumping** | intense flash lamp photons kick atoms up | Nd:YAG, ruby |
| **Electrical (discharge) pumping** | energetic electrons in a gas discharge collide-excite | He-Ne, COâ‚‚, Arâº |
| **Direct conversion / injection pumping** | current injects carriers straight across a p-n junction | semiconductor diode laser |
| **Chemical pumping** | an exothermic chemical reaction leaves products excited | HF laser |

**Why 4-level beats 3-level (the exam-worthy comparison):**
- **3-level (e.g. ruby):** the laser's *lower* level is the ground state â€” over half the atoms must be pumped out first before you even reach transparency â†’ huge threshold, hot, pulsed, inefficient.
- **4-level:** laser transition ends on a **fresh intermediate level that is normally empty**; that level drains to ground instantly. So even a tiny pumping rate creates population inversion â†’ **low threshold, continuous output possible, less wasted heat**.

Draw both level diagrams labelled (pump arrow, fast non-radiative arrow, laser arrow) â€” 1-2 marks hide in the drawing each. Deep: [[module-2-optoelectronics-lasers-fiber-optics]], quick sheet: [[lasers-quick-ref]].

---

## Q1.c (5M) â€” Threshold condition + amplification factor at threshold

**The idea:** the laser cavity has an amplifier with negative feedback from the mirrors. Lasing starts only when **gain per round-trip â‰¥ losses per round-trip** (losses = mirror transmission + absorption + scattering + diffraction). That equality is "threshold".

**Skeleton derivation:** Let gain per m = Î³, intensity Iâ‚€ after one pass through length L with gain $\exp(\gamma L)$; after a round-trip with mirror reflectivities Râ‚, Râ‚‚:

amplification per round trip $= R_1R_2\,e^{2\gamma L}$. Threshold: set this = 1 (gain exactly feeds what the mirrors leak):

$$R_1R_2\,e^{2\gamma_{th}L}=1\ \Rightarrow\ \boxed{\gamma_{th}=\frac{1}{2L}\ln\!\frac{1}{R_1R_2}}$$

With internal losses Î± per m: $\gamma_{th}= \alpha + \frac{1}{2L}\ln\frac{1}{R_1R_2}$. That's the "amplification factor/gain at threshold" expression asked. Connect to Einstein coefficients for the population version: $(N_2-N_1)_{th} = 8\pi h\nu^3 n^3\tau_{21}/(c^3\,g(\nu))$ â€” quote it if you know it cleanly, don't half-derive it.

**Similar problems:** threshold population inversion from Î³_th; "why can't a 2-level system sustain lasing"; gainâ€“length graph sketches â†’ [[lasers-quick-ref]], [[module-2-laser-fibre-question-bank]].

---

## Q2.a (5M) â€” Numerical aperture of step-index fibre

**The idea:** NA = the "light-catching cone half-angle" of the fibre, condensed into a single number. You get it by demanding TIR at the coreâ€“cladding boundary for the most extreme entering ray.

**Skeleton:** 1. **Diagram (1-2M):** core nâ‚, cladding nâ‚‚ (nâ‚>nâ‚‚), construction angle Î¸_A at the entrance face, refraction angle Î¸_r, TIR at core-cladding wall when Î¸_r = 90Â°âˆ’Î¸_c.
2. Snell at entrance: nâ‚€ sin Î¸_A = nâ‚ sin Î¸_r = nâ‚ cos Î¸_c. And sin Î¸_c = nâ‚‚/nâ‚ (critical angle, cladding).
3. Combine:

$$\boxed{NA = \sin\theta_A = \sqrt{n_1^2-n_2^2} = n_0\sqrt{n_1^2-n_2^2}\ (n_0=1\text{ in air})}$$

4. Bonus line: acceptance cone full-angle = 2Î¸_A; light entering outside the cone leaks away. Marks: diagram + the cos/sin shuffle + final box.

**Similar problems:** NA or Î¸_A given nâ‚, nâ‚‚ (e.g. nâ‚=1.50, nâ‚‚=1.47 â†’ NAâ‰ˆ0.297); fractional refractive index Î”=(nâ‚âˆ’nâ‚‚)/nâ‚ and NAâ‰ˆnâ‚âˆš(2Î”). â†’ [[module-2-fiber-optics]].

---

## Q2.b (5M) â€” Colours in thin film; absence in transmitted light

**The idea:** the film splits light into a reflected wave and a transmitted wave that **differ by exactly Î»/2 worth of phase flip** â€” so whatever is BRIGHT in reflection is DARK in transmission. Colours appear because the (2nâˆ’1)Î»/2 condition is satisfied by different Î» for the same film t (angle-dependent too â†’ shifting rainbow).

**Skeleton answer:** transmitted ray goes through film twice more / never gets the extra phase flip â†’ its OPD lacks the Î»/2: $2\mu t\cos r = n\lambda$ â†’ bright transmitted where reflected is dark. For white light, the wavelengths satisfying the condition produce colour; the "missing colour" is the one reinforced in the other beam (they're **complementary**). Write one sentence each way + tiny ray diagram; the exam cares that you connect *the Ï€ flip at the top interface* to *inversion of the conditions*.

---

## Q2.c (5M) â€” Resolving power of grating + Rayleigh's criterion

**The idea:** resolving power = how close two wavelengths can be and still be told apart by the grating. Rayleigh's criterion defines "told apart": the **principal maximum of one line falls on the first minimum of the other**.

**Skeleton:** 1. Criterion statement (sketch two overlapping diffraction envelopes: just-resolved / resolved / unresolved â€” 3 mini-diagrams, 1-2M).
2. Within the m-th principal maximum the grating of N total lines has (Nâˆ’1) minima; width in Î» of one line â‰ˆ Î»/(mN).
3. $\boxed{RP = \dfrac{\lambda}{d\lambda} = mN}$ and for a plane grating, N = (number of lines per cm)Ã—(grating width).

**Similar:** "why more lines = better resolution (and â‰  sharper grating equation)"; compare with telescope resolving 1.22Î»/D. â†’ [[module-1-optics-interference-diffraction]], [[module-2-laser-fibre-question-bank]].

---

## Q3 â€” the numerical half (any 2 of 3, 5M each) â­ drill these

### Q3.a â€” Soap film, Î¼ = 1.34, t = 3900 Ã…; which wavelengths are BRIGHTEST in the reflected visible?

Reflected **max** condition (with the Ï€ flip already built in):

$$2\mu t=\left(n-\tfrac12\right)\lambda\ \Rightarrow\ \lambda=\frac{2\times1.34\times3900}{n-\tfrac12}\,\AA=\frac{20904}{2n-1}\ \AA$$

n = 1 â†’ 20904 Ã… âœ— Â· **n = 2 â†’ 6968 Ã… âœ“ (deep red)** Â· **n = 3 â†’ 4181 Ã… âœ“ (violet)** Â· n = 4 â†’ 2986 Ã… âœ—.

**Answer: â‰ˆ 6968 Ã… and â‰ˆ 4181 Ã…** are intensified in the reflected light. If only one is expected, quote 4181 Ã… (fully inside 4000â€“7000 Ã…; 6968 sits at the red edge (TBC â€” some classes use < 7000 Ã… strictly)). Common mistake: forgetting the Î»/2 and getting 2Î¼t = nÎ» instead â€” check which flip convention your notes use.

### Q3.b â€” Population ratio, Î» = 694.3 nm at 27 Â°C (300 K) â€” comment.

Boltzmann: $\dfrac{N_2}{N_1}=e^{-\Delta E/kT}$, Î”E = hc/Î»:

Î”E = (6.63Ã—10â»Â³â´ Ã— 3Ã—10â¸)/6.943Ã—10â»â· m = **2.86Ã—10â»Â¹â¹ J** (= 1.79 eV)
kT = 1.38Ã—10â»Â²Â³ Ã— 300 = **4.14Ã—10â»Â²Â¹ J**
Exponent: 2.86e-19 / 4.14e-21 â‰ˆ 69 â†’

$$\dfrac{N_2}{N_1}\approx e^{-69}\approx 10^{-30}$$

**Comment (the 2 theory marks):** essentially ALL atoms are in the ground state; thermal light can never produce population inversion â€” this is exactly why lasers need artificial pumping (ties straight into Q1.b).

### Q3.c â€” Grating: 2nd-order maximum of Î» = 6000 Ã… at 30Â°. Lines/cm?

$$d\sin\theta = m\lambda \Rightarrow d=\frac{2\times 6000\times10^{-8}\ \text{cm}}{0.5}=2.4\times10^{-4}\ \text{cm}$$

Lines per cm = 1/d = **â‰ˆ 4166 lines/cm** (â‰ˆ 4.16Ã—10Â³). Unit discipline: Î» in cm (10â»â¸); marks die in Ã…-vs-cm slips.

**Similar problems:** wedge angle from fringe count, grating with normal-incidence oblique incidence twist, Nâ‚/Nâ‚‚ for other Î»/T pairs, max order of a grating. Numeralic banks: [[mse-recall-test-physics]], [[module-1-addendum-sem1-numericals-derivations]].

---

## Exam-day strategy

1. **Do Q3 first** â€” three plug-in formulas, ~30 min â†’ 10M. (a) needs the flip convention memorised, (b) needs Î”E in eV efficiency, (c) needs Î»-in-cm.
2. Q1: **1.b + 1.a** (b is memorisation, a is the standard derivation).
3. Q2: **2.a + 2.c** (a = NA box, c = mN box; both survive with diagram + formula).
4. Every theory answer: **diagram first**, then conditions/derivation â€” diagrams are 30â€“40% of each 5M here.

**Quick sheets:** [[lasers-quick-ref]] Â· [[thin-film-interference-revision]] Â· [[mse-revision-physics-lasers-slit]] Â· [[mse-revision-physics-m1-optics]] Â· flashcards [[mse-flashcards-physics]].

**Relations:** relates_to [[module-1-optics-interference-diffraction]] Â· [[module-2-optoelectronics-lasers-fiber-optics]] Â· source: [[raw-sources/midsems-pyp.pdf|midsems-pyp.pdf]].


