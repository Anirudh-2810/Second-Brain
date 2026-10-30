---
course_code: "ENG-PHY"
course_name: "Engineering Physics"
unit: "MSE Theory & Derivation Pack (paper-mapped)"
date: "2026-10-27"
tags: [engineering-physics, interference, thin-film, lasers, einstein-coefficients, threshold-condition, numerical-aperture, resolving-power, rayleigh-criterion, diffraction-grating, fiber-optics, derivations, exam-prep, mse]
last_updated: "2026-10-27"
confidence: high
description: "Full MSE theory + derivations in exam-writeable form: superposition/amplitude method, thin-film effective OPD, Einstein coefficients, threshold condition, laser components + 3/4-level diagrams, NA, Rayleigh criterion + grating RP, fibre losses/types — each tagged to its past-paper question."
relations:
  relates_to: "[[mse-past-paper-physics-2025-solved]]"
  derives_from: "[[mse-revision-physics-lasers-slit]]"
---

## For future agent

The **write-out derivations** companion to the recall surfaces ([[mse-revision-physics-lasers-slit]], [[mse-revision-physics-m1-optics]]) — created 2026-10-27 when the owner photographed last year's MSE paper and asked for the full theory + derivations in easy words, paper-mapped. Every derivation is in "how to write it in the answer sheet" form: numbered steps, boxed result, diagram instructions. Numericals are CONDENSED here (formula → answer); full step-by-step solutions live in [[mse-past-paper-physics-2025-solved]] — that page owns the paper walkthrough, this page owns the derivations. Faculty-verified numbers only (He-Ne 632.8 nm; threshold uses L; Δ = (n₁−n₂)/n₁). Sources: [[module-1-optics-interference-diffraction]], [[module-1-addendum-sem1-numericals-derivations]], [[lasers-quick-ref]], [[module-2-fiber-optics]].

# MSE Theory & Derivation Pack — paper-mapped

## Paper map (last year's MSE → where the answer lives here)

| Paper Q | Ask | Write from |
|---|---|---|
| Q1.a | Effective OPD, thin film, diagram | **§A2** |
| Q1.b | Pumping schemes; 4-level vs 3-level | **§B4** |
| Q1.c | Threshold condition + amplification factor | **§B3** |
| Q2.a | NA of step-index fibre, schematic | **§C1** |
| Q2.b | Colours in film; absent in transmitted | **§A2 + §A3** |
| Q2.c | Resolving power of grating + Rayleigh criterion | **§A5** |
| Q3.a | Soap-film visible bright λ | **§D** |
| Q3.b | Population ratio at 27 °C, comment | **§D** |
| Q3.c | Grating lines/cm | **§D** |

**Pattern verdict:** marks live in memorised derivations + diagrams (30–40% of each 5M). Attempt Q3 first, then Q1.b + Q1.a, then Q2.a + Q2.c.

---

## A1 — Interference basics: the amplitude method *(foundation for every derivation)*

Two coherent waves (same ν, constant phase difference φ):

$$E_1 = a\sin(\omega t), \qquad E_2 = a\sin(\omega t + \phi)$$

**Derivation (superposition):**
1. Add and apply $\sin A + \sin B = 2\cos\frac{A-B}{2}\,\sin\frac{A+B}{2}$:

$$\boxed{E = 2a\cos\frac{\phi}{2}\,\sin\!\Big(\omega t + \frac{\phi}{2}\Big)}$$

→ resultant amplitude $A = 2a\cos(\phi/2)$; same frequency; average phase.

2. Intensity ∝ amplitude²:

$$\boxed{I = 4I_0\cos^2\frac{\phi}{2}}$$

3. Checks (write these): φ = 2nπ → I = 4I₀ (bright); φ = (2n+1)π → I = 0 (dark); pattern average = 2I₀ → **energy conserved, only redistributed** dark→bright.

**Unequal amplitudes** (general exam form):

$$I = I_1 + I_2 + 2\sqrt{I_1I_2}\cos\phi, \qquad I_{max}=(\sqrt{I_1}+\sqrt{I_2})^2,\quad I_{min}=(\sqrt{I_1}-\sqrt{I_2})^2$$

**The bridge line:** $\phi = \dfrac{2\pi}{\lambda}\times(\text{path difference})$ — converts any path difference into intensity. Coherence requirement: two independent lamps have random φ (averages to no fringes) → every apparatus **splits one source**.

---

## A2 — Interference due to thin film + effective OPD *(paper Q1.a, Q2.b)*

**Draw:** film (μ, t) in air; ray AB incident at angle i, refracts at r; ray 1 reflects at top surface; ray 2 refracts to C, reflects at bottom, exits parallel to ray 1. Drop normal DE onto ray 1 produced.

```
  B ──────────── top surface (air→film: RARE→DENSE)
   \  ↖ ray1    /\
    \   BC     /  \  r
     \     ↘  /    \
   t  \  C    /     \     film (μ)
       \↖    / CD
        ────/───────  bottom surface (film→air: DENSE→RARE)
           D → ray2 out ∥ ray1
```

**Step 1 — optical path difference:**

$$\Delta = \mu(BC + CD) - BE$$

(ray 2's extra film path minus ray 1's air path BE while ray 2 crosses BD.)

**Step 2 — Snell kills BE.** From the figure, $\mu = \sin i/\sin r = BE/FD$:

$$BE = \mu \cdot FD$$

**Step 3 — substitute** (CD = CF + FD):

$$\Delta = \mu(BC + CD) - \mu(FD) = \mu(BC + CF) = \mu\cdot PF$$

**Step 4 — geometry:** BP = 2t (two film thicknesses); in △BPF, $\cos r = PF/BP$:

$$\boxed{\Delta_{geom} = 2\mu t\cos r}$$

**Step 5 — Stokes' π correction.** Reflecting off a **denser** medium → phase flip π ≡ λ/2. Ray 1 flips (air→film); ray 2 doesn't (film→air). **Count = 1 flip.**

$$\boxed{\Delta_{eff} = 2\mu t\cos r + \frac{\lambda}{2}}$$

**Step 6 — conditions.** Bright: Δ_eff = nλ; Dark: Δ_eff = (2n+1)λ/2:

$$\boxed{\text{Bright (refl): } 2\mu t\cos r = \frac{(2n-1)\lambda}{2}} \qquad \boxed{\text{Dark (refl): } 2\mu t\cos r = n\lambda}$$

Normal incidence: cos r = 1 → use 2μt.

⚠️ **Flips = 0 or 2** (both rare→dense or both dense→rare): bright/dark **swap**. Always count flips first.

**Transmitted = complementary** (energy conservation): transmitted bright ⇔ reflected dark → transmitted bright: $2\mu t\cos r = n\lambda$; dark: $(2n-1)\lambda/2$.

---

## A3 — Applications of interference *(paper Q2.b second half)*

| Application | Idea | Key result |
|---|---|---|
| **Colours of soap bubbles / oil films** | t varies over the film → different λ satisfy the bright condition at different t; colours shift as film drains | film goes "black" just before popping (t→0 hits the dark condition) |
| **Why reflected colours are absent in transmitted** | transmitted rays get no π flip at the top interface → OPD lacks λ/2 → conditions inverted | whatever is bright in reflection is dark in transmission — colours are **complementary** |
| **Anti-reflection coating** (MgF₂ on glass, 2 flips) | reflected dark when $2\mu t = \lambda/2$ | $\boxed{t_{min} = \lambda/4\mu}$ → zero reflection |
| **Newton's rings — flatness testing** | uniform rings ⇔ perfect surface; distorted rings expose defects | λ = $(r_{n+p}^2 - r_n^2)/pR$ |
| **Newton's rings — measure λ or R** | slope of D² vs n = 4λR | dark rings $D_n^2 = 4n\lambda R$ (centre dark, 1 flip) |
| **Michelson interferometer** | mirror moves Δd → N fringes cross; light traverses the arm **twice** | $\boxed{\lambda = 2\Delta d/N}$ |

---

## A4 — Diffraction grating + applications *(paper Q2.c part 1)*

**Definition:** N parallel equally-spaced slits; grating element $d = 1/(\text{lines per unit length})$ (5000 lines/cm → d = 1/5000 cm).

**Theory:** path difference between adjacent slits = d sinθ → principal maxima:

$$\boxed{d\sin\theta = n\lambda}$$

Same condition as YDSE (N doesn't change it) — but between adjacent principal maxima lie **(N−1) minima, (N−2) weak secondary maxima**, and maximum width $\Delta\theta = \lambda/(Nd\cos\theta) \propto 1/N$ → **large N makes maxima razor-sharp on dark background**. Write that sentence — it is why gratings exist.

**Max visible order:** $\sin\theta \le 1 \Rightarrow \boxed{n_{max} = \lfloor d/\lambda \rfloor}$ (count n = 0 too).

**Applications:** precision wavelength measurement (spectrometer); CD/DVD rainbow (tracks = grating); X-ray crystallography (crystal = 3D grating); telecom wavelength demultiplexing (DWDM); DFB laser diodes (grating inside selects one frequency).

---

## A5 — Resolving power + Rayleigh criterion *(paper Q2.c)*

**Rayleigh criterion (state + draw):** two sources are *just resolved* when the **central maximum of one falls exactly on the first minimum of the other.**

```
   just resolved:      unresolved:        resolved:
      ▲▲                 ▲▲▲ (one bump)     ▲  ▲ (clear gap)
     ▲  ▲
    ─────────→ angle
```

- Slit (spectrometer): first minimum at $\theta_{min} = \lambda/a$
- Circular aperture (telescope/microscope): $\boxed{\theta_{min} = 1.22\,\lambda/D}$

**Resolving power of a grating — derivation:**
1. Two nearby wavelengths λ, λ+Δλ give their n-th principal maxima at slightly different angles (grating equation).
2. Rayleigh: just resolved when the (λ+Δλ) maximum sits on the **first minimum** beside the λ maximum in the same order. That first minimum is one "minimum-step" away; with N illuminated rulings the width of a principal maximum in wavelength ≈ λ/nN.
3. Result:

$$\boxed{RP = \frac{\lambda}{\Delta\lambda} = nN}$$

n = order, N = **total illuminated rulings** (lines/cm × grating width — never lines/cm alone). Higher order or more rulings → better resolution. Comparison one-liner: telescope resolves by aperture (D/1.22λ); grating resolves by interference (nN).

---

## B1 — Einstein coefficients: full derivation *(foundation of Q1.b/Q1.c)*

**Three transition rates** (draw each — see B4):

| Process | Rate | Character |
|---|---|---|
| Absorption | $B_{12}\rho(\nu)N_1$ | photon eaten, atom jumps up |
| Spontaneous emission | $A_{21}N_2$ | random phase/direction → **incoherent** (bulb/LED) |
| Stimulated emission | $B_{21}\rho(\nu)N_2$ | **identical copy** photon → coherent → **laser** |

**Derivation:** at **thermal equilibrium** upward rate = downward rate (detailed balance):

$$N_1 B_{12}\rho(\nu) = N_2 A_{21} + N_2 B_{21}\rho(\nu)$$

Solve for ρ and insert Boltzmann $N_1/N_2 = \frac{g_1}{g_2}e^{h\nu/kT}$:

$$\rho(\nu) = \frac{A_{21}}{\dfrac{g_1}{g_2}B_{12}\,e^{h\nu/kT} - B_{21}}$$

**Compare with Planck's law** $\rho(\nu) = \dfrac{8\pi h\nu^3}{c^3}\cdot\dfrac{1}{e^{h\nu/kT}-1}$, matching term by term:

$$\boxed{g_1B_{12} = g_2B_{21}} \qquad \boxed{A_{21} = \frac{8\pi h\nu^3}{c^3}B_{21}}$$

Non-degenerate levels (g₁ = g₂): B₁₂ = B₂₁. Spontaneous lifetime $\tau = 1/A_{21}$ (~10⁻⁸ s).

**Key line:** $A/B \propto \nu^3$ → spontaneous dominates at optical frequencies → without inversion every excited medium is just a lamp. **This is why lasers need population inversion.**

---

## B2 — Population inversion & level systems *(feeds Q1.b)*

Boltzmann at equilibrium: $N_2/N_1 = \frac{g_2}{g_1}e^{-h\nu/kT} \Rightarrow N_2 < N_1$ always → **two-level system can never lase**.

**Metastable state:** lifetime ~10⁻³ s vs 10⁻⁸ s normal — atoms pile up there, making inversion achievable.

| | 3-level (Ruby) | 4-level (He-Ne, Nd:YAG, CO₂) |
|---|---|---|
| Lower laser level | **ground state** | fresh level above ground, **≈ empty** |
| Pumping needed | > 50% of all atoms | trivially small |
| Threshold | high | low |
| Operation | pulsed | CW |
| Example | Ruby 694.3 nm | He-Ne 632.8 nm, Nd:YAG 1064 nm, CO₂ 10.6 μm |

---

## B3 — Threshold condition + amplification factor *(paper Q1.c — faculty form)*

**Draw:** two mirrors (R₁, R₂) separated by L; gain medium fills the cavity; loss coefficient α_C.

**Derivation:** one round trip = through the medium **twice** (path 2L) + both mirror bounces. Start I₀:

$$I = I_0 \cdot R_1R_2\, e^{2(\gamma - \alpha_C)L}$$

**Threshold = round-trip gain exactly cancels round-trip loss** (amplification factor = 1):

$$R_1R_2\,e^{2(\gamma_{th}-\alpha_C)L} = 1 \;\Rightarrow\; 2(\gamma_{th}-\alpha_C)L = \ln\frac{1}{R_1R_2}$$

$$\boxed{\gamma_{th} = \alpha_C + \frac{1}{2L}\ln\!\left(\frac{1}{R_1R_2}\right)}$$

⚠️ **Write L (cavity length), not l** — faculty form (Dr. Suren Patwardhan, SVU R-2023). γ_th = amplification factor per metre at threshold; lasing starts only when γ > γ_th. General form with medium length l: $g_{th} = \alpha + \frac{1}{2l}\ln\frac{1}{R_1R_2}$.

---

## B4 — Laser components + pumping schemes + level diagrams *(paper Q1.b, Q1 part of Q11-topic)*

**Components (draw a horizontal cavity):**
```
 R≈99.9% ┌──────────────────────────┐ R≈98% (output coupler)
   ═══╗  │   GAIN MEDIUM            │   ╔═══→ output beam
      ║  │  (gas / solid / diode)   │   ║
      ╚══┴──────────────────────────┴═══╝
               ↑ PUMP SOURCE
```
1. **Gain medium** — the lasing atoms/ions
2. **Pumping source** — creates population inversion
3. **Optical resonator** — full mirror + partial output coupler → photons amplify per pass, part exits

**Pumping schemes (Q1.b list):**

| Scheme | Mechanism | Example |
|---|---|---|
| **Optical** | flash-lamp photons kick atoms up | Ruby (xenon lamp), Nd:YAG |
| **Electrical (discharge)** | energetic electrons collide-excite gas | He-Ne, CO₂, Ar⁺ |
| **Direct conversion / injection** | current injects carriers across p-n junction | diode laser |
| **Chemical** | exothermic reaction leaves products excited | HF laser |

**Level diagrams (draw both, labelled — the marks are in the arrows):**

```
THREE-LEVEL (Ruby)                FOUR-LEVEL (He-Ne, Nd:YAG)
E₃ ─ ─ ─ pump; fast decay         E₃ ─ ─ ─ pump; fast decay
  ▼                                 ▼
E₂ ─ ─ METASTABLE ← laser top     E₂ ─ ─ METASTABLE ← laser top
  │ LASING                          │ LASING
  ▼                                 ▼
E₁ ─ ─ = GROUND STATE             E₁ ─ ─ (drains FAST to E₀)
                                    ▼
                                   E₀ ─ ─ GROUND STATE
```

**4-level advantages over 3-level (the 5 marks):** lower laser level is **empty** (not the ground state) → inversion needs tiny pumping → **low threshold, CW possible, less heat**; in 3-level over half the atoms must leave the ground state before net gain.

**He-Ne diagram (collision transfer):**
```
 He(2¹S) 20.61 eV ──collision──→ Ne(3s) 20.66 eV (metastable)
                                   │ LASING 632.8 nm
                                   ▼
                                 Ne(2p) → Ne(1s) → ground (fast drains)
 He(2³S) 19.78 eV ──collision──→ Ne(2s) 18.7 eV (faculty value)
```
Write: discharge excites **He** metastables → **near-resonant collision** transfers to Ne → inversion in Ne → 632.8 nm → lower levels drain fast → CW. Metastable values: **Ne 2s = 18.7 eV, 3s = 20.66 eV** (E₂−E₁ = 1.96 eV → 1240/1.96 ≈ 632.8 nm).

---

## C1 — Numerical aperture of step-index fibre *(paper Q2.a)*

**Draw:** fibre end face; external acceptance half-angle θ_C; refracted ray inside at φ_C; critical angle i₀ at the core–cladding wall (refracted angle r = 90°).

**Step 1 — Snell at entry face** (external n₀ → core n₁):

$$n_0\sin\theta_C = n_1\sin\phi_C \qquad (1)$$

**Step 2 — Snell at the wall**, limiting ray (i = i₀, r = 90°):

$$n_1\sin i_0 = n_2\sin 90° \Rightarrow \sin i_0 = \frac{n_2}{n_1} \qquad (2)$$

**Step 3 — geometry:** φ_C and i₀ complementary → $\sin\phi_C = \cos i_0 = \sqrt{1-\sin^2 i_0}$

**Step 4 — combine (1)+(2):**

$$n_0\sin\theta_C = n_1\sqrt{1-\frac{n_2^2}{n_1^2}} = \sqrt{n_1^2-n_2^2}$$

$$\boxed{NA = n_0\sin\theta_C = \sqrt{n_1^2-n_2^2} \approx n_1\sqrt{2\Delta}}$$

with $\Delta = (n_1-n_2)/n_1$ (faculty definition), n₀ = 1 in air. Angles: $\theta_C = \sin^{-1}(NA)$; $i_0 = \sin^{-1}(n_2/n_1) = \sin^{-1}(1-\Delta)$.

**Follow-on lines:** $V = \frac{2\pi a}{\lambda}\cdot NA$; **V < 2.405 → single mode**; $N_m = V^2/2$ (SI), $V^2/4$ (GRIN). TIR principle: denser core (n₁) → rarer cladding (n₂), incidence ≥ critical angle → complete reflection back into core.

---

## C2 — Fibre losses + types & classification *(topic 9)*

**Attenuation:** $\alpha = \frac{1}{L}\,10\log\frac{P_{in}}{P_{out}}$ dB/km (L in **km**).

**Three causes (draw 3 branches):**
1. **Absorption** — (a) *intrinsic*: glass itself — UV electronic band (0.1–0.3 μm) + IR vibrational band (7–12 μm); (b) *impurities* (chief contributors): **OH⁻ radicals**, Cu, Ni, Cr, V, Mn
2. **Rayleigh scattering** — amorphous glass → microscopic density/RI fluctuations: $\boxed{\propto 1/\lambda^4}$ (longer λ → less loss)
3. **Geometric effects** — core/cladding irregularity, cabling stress, **bending loss** (bend breaks the critical angle → light leaks)

**Optical windows:** loss minima at **~1.3 μm and ~1.55 μm** → sources designed there.

**Classification tree:**
```
BY APPLICATION                BY MATERIAL
├─ Single mode (SM)           ├─ All-glass (best quality)
│   axial ray only, core      └─ Plastic / PCS (cheap, lossy)
│   5–10 μm, laser diode only
└─ Multimode (MM), core 50–100 μm, LED or laser
    ├─ Step index (SI): uniform core RI, zigzag rays, pulse spreads
    └─ Graded index (GRIN): RI falls outward, rays curve smoothly;
       longer path offset by faster speed → modes stay synchronous
```

**SI vs GRIN one-liners:** GRIN fixes intermodal dispersion ($\tau_i = n_1L\Delta/c$ SI vs $n_2L\Delta^2/2c$ GRIN) → higher bandwidth, lower attenuation, but harder to manufacture. Dispersion trio: **intermodal** (path difference), **material** (λ-dependent speed; fixed by laser source), **waveguide** (cladding penetration; matters in SM). Bit rate $B \approx 0.7/\tau$.

---

## D — Paper numericals (condensed; full steps: [[mse-past-paper-physics-2025-solved]])

### Q3.a — Soap film μ = 1.34, t = 3900 Å; bright reflected λ in 4000–7000 Å?

Reflected bright (1 flip): $2\mu t = (2n-1)\frac{\lambda}{2} \Rightarrow \lambda = \frac{2\times1.34\times3900}{n-\frac12} = \frac{20904}{2n-1}$ Å

n = 1 → 20904 ✗ · **n = 2 → 6968 Å ✓ (deep red)** · **n = 3 → 4181 Å ✓ (violet)** · n = 4 → 2986 ✗

**Answer: ≈ 6968 Å and ≈ 4181 Å.** (If strict 4000–7000, quote 4181 Å; flag 6968 as red-edge.)

### Q3.b — Population ratio, λ = 694.3 nm, T = 300 K; comment

$$\frac{N_2}{N_1} = e^{-\Delta E/kT}, \quad \Delta E = \frac{hc}{\lambda} = 2.86\times10^{-19}\,\text{J}, \quad kT = 4.14\times10^{-21}\,\text{J}$$

$$\frac{N_2}{N_1} \approx e^{-69} \approx 10^{-30}$$

**Comment (the theory marks):** essentially ALL atoms sit in the ground state — thermal equilibrium can never invert → lasers need artificial pumping (ties into Q1.b).

### Q3.c — Grating: 2nd order of λ = 6000 Å at 30°; lines/cm?

$$d\sin\theta = n\lambda \Rightarrow d = \frac{2\times6000\times10^{-8}}{\sin 30°} = 2.4\times10^{-4}\,\text{cm}$$

Lines/cm = 1/d ≈ **4166 lines/cm**. Unit discipline: λ in cm (10⁻⁸).

---

## Exam-day trap checklist (read before entering)

1. Count **phase flips FIRST** — k = 0/2 vs k = 1 swaps bright/dark
2. YDSE and single slit have **swapped** conditions (grating/slit bright: nλ vs single-slit dark: nλ)
3. He-Ne = **632.8 nm**; metastables **18.7 & 20.66 eV**; coherence ≈ **2 km**
4. Threshold: use **L** (faculty); mode spacing Δν = c/2L depends only on L
5. Two-level can never lase; Ruby = 3-level, pulsed
6. Michelson λ = **2**Δd/N; Newton's rings formulas use **D** (diameter)
7. Grating: "6000 lines/cm" → d = 1/6000 **cm**; RP = nN with N = **total illuminated lines**
8. λ in Å → cm (×10⁻⁸) in every grating/film numerical
9. First polarizer on unpolarized light: exactly I₀/2
10. YDSE max intensity = **4**I₀

---

## Cross-links

- **Paper walkthrough + full numerical steps:** [[mse-past-paper-physics-2025-solved]]
- **Recall surfaces:** [[mse-revision-physics-lasers-slit]] · [[mse-revision-physics-m1-optics]]
- **Drills:** [[mse-flashcards-physics]] · [[mse-recall-test-physics]]
- **Deep theory owners:** [[module-1-optics-interference-diffraction]] · [[module-1-addendum-sem1-numericals-derivations]] (thin-film OPD transcription) · [[lasers-quick-ref]] · [[module-2-fiber-optics]]
- **Hub:** [[engineering-physics/overview]]
