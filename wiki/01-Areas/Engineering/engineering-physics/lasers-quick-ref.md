---
course_code: "ENG-PHY"
course_name: "Engineering Physics"
unit: "Module 2 — Lasers (Rapid Revision)"
date: "2026-10-02"
description: "Physics-B laser quick-revision sheet — Einstein coefficients, population inversion, 3-level vs 4-level, threshold gain, laser types table, cavity modes and TEM patterns, plus the four worked numericals you must be able to reproduce."
tags: [engineering-physics, lasers, photonics, quantum-mechanics, stimulated-emission, population-inversion, einstein-coefficients, exam-prep, revision]
last_updated: "2026-10-02"
confidence: high
prerequisites: ["Quantum Mechanics Basics", "Wave Optics", "Electromagnetic Waves"]
---

## For future agent

Condensed exam-revision cut of [[module-2-optoelectronics-lasers-fiber-optics]] — that 1300-line page is the deep theory + fiber-optics owner and stays the reference. This page is the **lasers-only quick sheet**: the formulas, the comparison tables, the laser-types roster, and the four numericals that repeat every year.

Scope cut: **Lasers only.** Fiber optics, EDFA/Raman amplifiers, photodiodes, solar cells, and nonlinear optics live elsewhere — **fibre now has its own page, [[module-2-fiber-optics]]**.

Staleness: no dates-sensitive content. The formulas are stable (Einstein 1917). Watch for the two numbers most often mis-stated under exam pressure: the He-Ne wavelength (**632.8 nm**, not 633) and the single-mode cutoff (**V = 2.405**, not 2.4 or 3).

**Faculty-authoritative source (2026-10-02).** This sheet was originally synthesised from the 73 KB deep module page. It has since been checked against **Dr. Suren Patwardhan's official Module 1 Unit 1 papers** (*"Principles of Lasers, As per Revised Curriculum SVU R-2023"*): `Lasers - Notes.pdf`, `Laser Formulas..pdf`, `Numericals LASER.pdf`, `Lasers Questions.pdf` — all previously unopened. **Where they disagree, the faculty win for exam purposes.** Three corrections flagged inline:

| Item | Originally said | Faculty says | Where |
|---|---|---|---|
| Threshold-condition length | `l` = gain medium | **`L` = cavity length**, `α_C` = cavity loss | §5 |
| He-Ne metastable energies | 19.78 & 20.66 eV | **18.7 & 20.66 eV** (Ne⁺ 2s / 3s) | §7a |
| He-Ne coherence length | 200 m | **≈ 2 km** (Δλ = 2×10⁻⁴ nm) | §9 |

**Two formulas were missing and are now added:** the spontaneous-to-stimulated **rate ratio** `R = e^(hν/kT) − 1` (setting R=1 gives the faculty's "impossible" 41,600 K result) and the **divergence** `θ = (d₁−d₂)/(Z₁−Z₂)`, plus the full beam-parameter set in §5a.

**Full theory + 30 theory questions + 40 worked numericals:** [[module-2-laser-fibre-question-bank]]

---

# Lasers — Rapid Revision Sheet

## 1. The three processes (memorize these three rates)

```
  ABSORPTION              SPONTANEOUS EMISSION      STIMULATED EMISSION
  ══════════              ════════════════          ══════════════════

  E₂ ─ ─ ─                E₂ ─ ─ ─ ─ ─              E₂ ─ ─ ─ ─ ─
    │                        │                          │
  hν in                    hν out                    hν in ──→ hν out
  absorbed                 random dir/phase          IDENTICAL COPY
    │                        │                          │
  E₁ ─ ─ ─                E₁ ─ ─ ─                  E₁ ─ ─ ─

  B₁₂ ρ N₁                 A₂₁ N₂                    B₂₁ ρ N₂
```

| Process | Rate | Character |
|---|---|---|
| **Absorption** | $R_{abs} = B_{12}\,\rho(\nu)\,N_1$ | ground atom takes in $h\nu$ |
| **Spontaneous emission** | $R_{spon} = A_{21}\,N_2$ | random direction + phase → **incoherent**. This is how bulbs and LEDs work |
| **Stimulated emission** | $R_{stim} = B_{21}\,\rho(\nu)\,N_2$ | incoming photon triggers an **identical** photon → coherent. **This is laser action** |

$$\text{Spontaneous lifetime: } \tau_{spon} = \frac{1}{A_{21}} \quad (\sim 10^{-8}\,\text{s for allowed E1 transitions})$$

$B_{12}, B_{21}$ — Einstein B coefficients (m³/J·s²) · $A_{21}$ — Einstein A coefficient (s⁻¹) · $\rho(\nu)$ — spectral energy density · $N_1, N_2$ — population densities.

## 2. Einstein relations (the two boxes you must reproduce)

At thermal equilibrium, absorption balances the two emission rates. Matching the result against Planck's law gives:

$$\boxed{g_1 B_{12} = g_2 B_{21}}$$

$$\boxed{A_{21} = \frac{8\pi h \nu^{3}}{c^{3}} \, B_{21}}$$

For non-degenerate levels ($g_1 = g_2$): $B_{12} = B_{21}$.

**Key insight:** $A_{21}/B_{21} \propto \nu^3$. So stimulated emission becomes relatively more important at **lower** frequencies. At optical frequencies spontaneous emission dominates — which is exactly why a laser needs population inversion.

## 3. Population inversion

At thermal equilibrium the Boltzmann distribution gives:

$$\frac{N_2}{N_1} = \frac{g_2}{g_1} e^{-(E_2 - E_1)/k_BT} = \frac{g_2}{g_1} e^{-h\nu/k_BT}$$

Since $E_2 > E_1$, we get $N_2 < N_1$ — **absorption wins, so a two-level system can never give net gain.** You must pump atoms into a higher level.

```
  THREE-LEVEL SYSTEM                 FOUR-LEVEL SYSTEM
  ════════════════════                ═════════════════

  E₃ ─ ─ ─                             E₃ ─ ─ ─
    │ pump (fast)                        │ pump (fast)
    ▼                                    ▼
  E₂ ─ ─ ─ METASTABLE                E₂ ─ ─ ─ METASTABLE (upper laser level)
    │                                    │
    │ LASING                             │ LASING
    ▼                                    ▼
  E₁ ─ ─ ─ IS THE GROUND STATE        E₁ ─ ─ ─ (decays FAST to E₀)
                                          │
                                          ▼
                                        E₀ ─ ─ ─ GROUND STATE

  Need >50% of atoms pumped             E₁ nearly empty
  HIGH threshold power                 LOW threshold power
  PULSED only                           CONTINUOUS WAVE possible
```

| | 3-level | 4-level |
|---|---|---|
| Pumping required | $N_2 > N_{total}/2$ | $N_2 > N_1 \approx 0$ — trivially small |
| Threshold power | high | low |
| Operation | pulsed | CW |
| Example | Ruby | He-Ne, Nd:YAG, CO₂, ArF |

## 4. Optical gain

With inversion ($N_2 > N_1$) the medium amplifies:

$$g(\nu) = \frac{(N_2 - N_1)\, c^{2} A_{21}}{8\pi \nu^{2}} \, g(\nu,\nu_0)$$

Simplified monochromatic form:

$$g_0 = \frac{(N_2 - N_1)\, c^{2} A_{21}}{8\pi \nu_0^{2} \Delta \nu}$$

Intensity through a gain medium of length $l$: $I = I_0\,e^{g l}$ · in dB: $G_{dB} = 4.343\,g\,l$

## 5. Threshold condition & resonator

Three conditions must hold **simultaneously** for laser oscillation:

1. **Population inversion** ($N_2 > N_1$), maintained by pumping
2. **Optical resonator** — two mirrors feed photons back through the medium repeatedly
3. **Threshold** — round-trip gain ≥ round-trip loss

$$R_1 R_2\,e^{2(g-\alpha)l} \geq 1$$

$$\boxed{g_{th} = \alpha + \frac{1}{2l}\ln\!\left(\frac{1}{R_1 R_2}\right)}$$

$\alpha$ = distributed loss coefficient · $l$ = gain medium length · $R_1, R_2$ = mirror reflectivities.

### ⚠️ Use `L`, not `l`, for this course — faculty notation (2026-10-02)

Dr. Suren Patwardhan's official derivation (Module 1 Unit 1, SVU R-2023) writes the threshold as

$$\boxed{\gamma = \alpha_C + \frac{1}{2L}\ln\!\left(\frac{1}{R_1R_2}\right)}$$

with **`L` = cavity length** and **`α_C` = cavity loss coefficient**, because the derivation assumes the **gain medium fills the cavity**, making one round trip a path of `2L`. Several general textbooks instead use `l` = *gain-medium* length. **For this course write the faculty form.** Full derivation: [[module-2-laser-fibre-question-bank]] Q12.

### 5a. Beam parameters (faculty formulas)

| Parameter | Formula | Note |
|---|---|---|
| Beam intensity | `I = P/A` | W/m²; A = πr² for a circular beam |
| Photon emission rate | `n_t = P_optical × λ/(hc)` | photons/sec |
| Photons per pulse | `n = n_t × Δt` | |
| Laser efficiency | `η = P_optical/(V_op × I_op)` | electrical pumping / direct conversion |
| Coherence length | `l_coh = λ²/Δλ` | |
| Divergence | `θ = (d₁ − d₂)/(Z₁ − Z₂)` | d = beam diameters at axial distances Z |
| **Spontaneous/stimulated rate ratio** | **`R = e^(hν/kT) − 1`** | see below |

**Why `R = e^(hν/kT) − 1` matters:** setting `R = 1` gives `T = hν/(k ln2)`. At 5000 Å that is **≈ 4.16×10⁴ K** — far above any material. So at any laboratory temperature stimulated emission is negligible against spontaneous emission, which is exactly *why* population inversion is necessary.

**Linewidth comparison:** ordinary sources up to **10¹⁰ Hz**, laser sources ~**100 Hz**. Laser angular spread is ~**10⁶ times** smaller than ordinary light.

## 6. Laser types — the exam table

| Laser | Type | λ | Medium | Efficiency | Power | Application |
|---|---|---|---|---|---|---|
| **Ruby** | 3-level | **694.3 nm** | solid (Cr³⁺ in Al₂O₃) | ~0.1% | J/pulse | holography, medicine |
| **He-Ne** | 4-level | **632.8 nm** | gas (90% He, 10% Ne) | ~0.1% | 1–5 mW CW | alignment, barcode scanners |
| **Nd:YAG** | 4-level | **1064 nm** | solid (Nd³⁺) | ~3% | W–kW | surgery, manufacturing |
| **CO₂** | 4-level | **10.6 μm** | gas | ~10–20% | kW–MW | cutting, surgery, military |
| **GaAs** | semiconductor | 850–900 nm | p-n junction | ~30% | mW–W | comms, CD players |
| **InGaAsP** | semiconductor | 1310/1550 nm | DH junction | ~20% | mW | fiber telecom |
| **ArF excimer** | excimer | **193 nm** | gas (Ar + F₂) | ~1% | mJ/pulse | **LASIK** |
| **Ti:Sapphire** | 4-level | 650–1100 nm | solid | ~10% | W | ultrafast optics, tunable |
| **EDFA (Er fiber)** | 4-level | 1530–1565 nm | Er-doped fiber | ~30% | dB gain | telecom amplification |

## 7. He-Ne in detail (most-asked gas laser)

**Energy transfer is by collision, not by photon:**

```
   He atoms                      Ne atoms
   ══════════                    ══════════

   He(2¹S₀) @ 20.61 eV  ──collision──→  Ne(3s₂) @ 20.66 eV   (near-resonant)
                                        │  radiative decay
                                        ▼
   He(2³S₁) @ 19.78 eV  ──collision──→  Ne(2s₂) @ 19.78 eV
                                        │  radiative decay
                                        ▼
                                    Ne(2p) levels
                                        │
                                        │ 632.8 nm (visible)
                                        ▼
                                    Ne(1s) levels
                                        │ collisional de-excitation
                                        ▼
                                    Ground state
```

- A high-voltage discharge excites He to **metastable** states (electrons collide with He, not with Ne directly)
- He transfers energy to Ne by **collision** — the transfer is near-resonant (20.61 eV → 20.66 eV; 19.78 eV → 19.78 eV), cross-section ~10⁻¹⁶ cm²
- Inversion builds in the Ne upper level → lasing

**Visible lasing transitions:** **632.8 nm** (red, highest gain, most common), 543.5 nm (green), 594.1 nm (yellow), 611.9 nm (orange).

**Cavity:** Fabry-Pérot, one mirror R ≈ 99.9%, output coupler R ≈ 98%, separation L ≈ 15–30 cm, output 1–5 mW CW.

## 8. Semiconductor (diode) laser

Population inversion occurs at a **forward-biased p-n junction** — electrons and holes recombine across the depletion region, emitting photons of energy equal to the band gap.

$$h\nu = E_g \qquad\Longrightarrow\qquad \boxed{\lambda = \frac{hc}{E_g} = \frac{1240\ \text{eV·nm}}{E_g\ \text{(eV)}}}$$

**GaAs:** $E_g = 1.42$ eV → $\lambda = 1240/1.42 = 873$ nm ≈ 870 nm.

**$J_{th}$ — threshold current density** is the minimum current for lasing. Below $J_{th}$ the device is just an **LED** (spontaneous emission only); above it, stimulated emission dominates.

| Structure | Threshold $J_{th}$ | Modulation speed |
|---|---|---|
| Homojunction | high (~10⁴ A/cm²) | slow |
| Single heterojunction | moderate | moderate |
| **Double heterojunction (DH)** | low (~10³ A/cm²) | fast |
| **Quantum well** | very low (~10² A/cm²) | very fast |
| **DFB** (grating) | low | single-frequency |

## 9. Characteristics of laser light

| Property | Meaning | He-Ne value |
|---|---|---|
| **Monochromatic** | very narrow linewidth | $\Delta\lambda \approx 0.002$ nm |
| **Coherent** | all photons in phase | $l_c \approx 200$ m |
| **Collimated** | low divergence | $\theta \approx 0.5$ mrad |
| **High intensity** | focusable to tiny spots | MW/cm² |

**Coherence length:**

$$l_c = c\,\tau_c = \frac{c}{\Delta\nu} = \frac{\lambda^{2}}{\Delta\lambda}$$

For He-Ne with $\Delta\nu \approx 1.5$ MHz: $l_c = 3\times10^{8}/1.5\times10^{6} = 200$ m.

> **Faculty correction (2026-10-02):** using the official linewidth $\Delta\lambda = 2\times10^{-4}$ nm at 632.8 nm gives $l_{coh} = \lambda^2/\Delta\lambda \approx \mathbf{2\ \text{km}}$ — the faculty quote "a few m to a few km." Use **their** figures in numericals.

## 7a. Metastable states & pumping (faculty)

**Metastable** = a state where excited atoms can reside for **10⁻³ s**, versus **10⁻⁸ s** for normal de-excitation. It lets atoms **accumulate** in the upper level, which is what makes inversion achievable at all. The faculty are blunt: *"the invention of lasers could not have taken place if elements offering metastable states were not discovered."*

| Laser | Metastable level |
|---|---|
| He-Ne | **Ne⁺ 2s at 18.7 eV**, **3s at 20.66 eV** |
| Argon | Ar⁺ 4p |
| Ruby | **Cr³⁺ at 1.4 eV** |

> **Faculty correction:** the deep module page gives He-Ne transfer energies as 19.78 and 20.66 eV. The official notes and numericals use **Ne⁺ 2s = 18.7 eV and 3s = 20.66 eV**, so $E_2-E_1 = 1.96$ eV $\Rightarrow \lambda = 632.7$ nm. **Use 18.7 eV.**

**Three pumping methods:**

| Type | Mechanism | Example |
|---|---|---|
| **Optical** | a light source supplies energy; ions absorb and excite | **Ruby** — crystal surrounded by a **Xenon flash lamp**, Cr³⁺ excited |
| **Electrical** | an electric field ionises and accelerates molecules | **He-Ne** — He molecules ionised into excited states |
| **Direct conversion** | the current itself is the pump; "levels" are actually **bands** | **Diode laser** — inversion between conduction and valence bands |

**Two-level pumping** is the diode case. The faculty add that diode lasers *"can give maximum output efficiency even better than **70 %** at times"* — which supersedes the 30 % entry in the types table for modern devices.

## 10. Cavity modes

### 10.1 Longitudinal modes

Standing wave: $L = q\,\lambda/2$ with integer $q$.

$$\boxed{\nu_q = q\,\frac{c}{2L}} \qquad \boxed{\Delta\nu = \frac{c}{2L}}$$

**Mode spacing depends only on cavity length, not on wavelength.** For L = 30 cm: $\Delta\nu = 3\times10^8/0.6 = 500$ MHz.

**Mode number:** $q = \frac{2L}{\lambda}$. For L = 30 cm, λ = 632.8 nm: $q = 0.6/632.8\times10^{-9} \approx 9.5\times10^{5}$.

```
   Gain
   curve
    ╱╲
   ╱  ╲
  ╱    ╲
 ╱ │││││││╲        ← longitudinal modes under the gain curve
╱  │││││││ ╲
────┼┼┼┼┼┼┼┼┼─────  Frequency
    │
    Only modes inside the gain bandwidth AND above threshold oscillate.
    The mode nearest gain peak wins → single-mode output.
```

### 10.2 Transverse (TEM) modes

`TEM_mn` where *m*, *n* count the nodes in the transverse pattern.

```
    TEM₀₀        TEM₀₁        TEM₁₀        TEM₁₁        TEM₂₀
   (Gaussian)    2 lobes      2 lobes      4 lobes      3 lobes
   ┌─────┐      ┌─────┐      ┌─────┐      ┌─────┐      ┌─────┐
   │█████│      │█   █│      │█ █ █│      │█   █│      │█ █ █│
   │█████│      │█████│      │█ █ █│      │██ ██│      │ █ █ │
   │█████│      │█   █│      │█ █ █│      │█   █│      │█ █ █│
   └─────┘      └─────┘      └─────┘      └─────┘      └─────┘
   round spot    vertical     horizontal     both         2+1
```

**TEM₀₀ is the fundamental Gaussian mode** — smallest spot, lowest divergence, highest brightness. Almost all real lasers are made single-mode by an internal aperture. Higher modes have larger divergence and lower brightness.

### 10.3 Resonator stability

Two mirrors with radii $R_1, R_2$ separated by distance $L$:

$$\boxed{0 \le g_1 g_2 \le 1}, \qquad g_1 = 1 - \frac{L}{R_1}, \quad g_2 = 1 - \frac{L}{R_2}$$

| Configuration | $R_1$ | $R_2$ | $g_1$ | $g_2$ | Property |
|---|---|---|---|---|---|
| **Confocal** | L | L | 0 | 0 | most stable, smallest mode volume |
| **Hemispherical** | L | ∞ | 0 | 1 | easiest alignment |
| **Planar** | ∞ | ∞ | 1 | 1 | highest power, hard to align |
| **Concentric** | L/2 | L/2 | −1 | −1 | largest mode (stability boundary) |
| **General confocal** | 2L | 2L | 0.5 | 0.5 | good compromise |

## 11. Worked numericals — the four to reproduce

### (a) Einstein coefficients from the spontaneous lifetime

**Given:** $\tau_{spon} = 25$ ns, $\lambda = 632.8$ nm. Find $A_{21}$ and $B_{21}$.

**Step 1 —** $A_{21} = 1/\tau = 1/(25\times10^{-9}) = \boxed{4.0\times10^{7}\ \text{s}^{-1}}$

**Step 2 —** $\nu = c/\lambda = 3\times10^{8}/632.8\times10^{-9} = 4.741\times10^{14}$ Hz

**Step 3 —** invert the Einstein relation:

$$B_{21} = \frac{c^{3}}{8\pi h \nu^{3}} A_{21} = \frac{2.7\times10^{25}}{8\pi(6.626\times10^{-34})(1.066\times10^{44})}(4.0\times10^{7}) = \boxed{6.08\times10^{20}\ \text{m}^3/\text{J·s}^2}$$

**Verify:** $A_{21}/B_{21} = 6.58\times10^{-14}$ and $8\pi h\nu^3/c^3 = 6.57\times10^{-14}$. ✓

### (b) Threshold gain

**Given:** $R_1 = 0.999$, $R_2 = 0.98$, $L = 25$ cm, $l = 15$ cm, $\alpha = 0.01$ cm⁻¹.

$$g_{th} = \alpha + \frac{1}{2l}\ln\!\left(\frac{1}{R_1R_2}\right) = 0.01 + \frac{1}{30}\ln(1.02143) = 0.01 + 0.000707 = \boxed{0.01071\ \text{cm}^{-1} = 1.071\ \text{m}^{-1}}$$

*Note: only the gain medium length `l` appears, not the cavity length `L`.*

### (c) Cavity mode spacing and mode count

**Given:** L = 12 cm, λ = 1064 nm, gain bandwidth $\Delta\nu_{gain} = 0.45$ THz (Nd:YAG).

$$\Delta\nu = \frac{c}{2L} = \frac{3\times10^8}{0.24} = \boxed{1.25\ \text{GHz}}$$

$$q = \frac{2L}{\lambda} = \frac{0.24}{1.064\times10^{-6}} = \boxed{2.256\times10^{5}}$$

$$\nu_q = q\,\Delta\nu = 2.8196\times10^{14} = \boxed{282\ \text{THz}}$$

$$N_{modes} = \frac{\Delta\nu_{gain}}{\Delta\nu} = \frac{0.45\times10^{12}}{1.25\times10^{9}} = \boxed{360\ \text{modes}}$$

### (d) He-Ne energy transfer → why 632.8 nm

$h\nu = E_2 - E_1$. The Ne transition $3s_2 \to 2p \to 1s$ emits:

$$\lambda = \frac{hc}{E} = \frac{1240\ \text{eV·nm}}{1.96\ \text{eV}} \approx 632\ \text{nm}$$

(Transitions in the same Ne manifold are nearly degenerate, so the 632.8 nm photon comes from the 3s₂ upper level down to the 1s lower level through the 2p intermediate.)

## 12. Formula card

| Quantity | Formula |
|---|---|
| Einstein A | $A_{21} = 8\pi h\nu^{3} B_{21}/c^{3}$ |
| Spontaneous lifetime | $\tau = 1/A_{21}$ |
| Einstein B relation | $g_1B_{12} = g_2B_{21}$ |
| Boltzmann ratio | $N_2/N_1 = (g_2/g_1)e^{-h\nu/k_BT}$ |
| Gain coefficient | $g(\nu) = \frac{(N_2-N_1)c^2 A_{21}}{8\pi\nu^2}g(\nu,\nu_0)$ |
| Gain in dB | $G_{dB} = 4.343\,g\,l$ |
| **Threshold gain** | $g_{th} = \alpha + \frac{1}{2l}\ln\frac{1}{R_1R_2}$ |
| Threshold condition | $R_1R_2 e^{2(g-\alpha)l} \ge 1$ |
| Longitudinal mode freq | $\nu_q = qc/2L$ |
| **Mode spacing** | $\Delta\nu = c/2L$ |
| Mode number | $q = 2L/\lambda$ |
| Modes in gain BW | $N = \Delta\nu_{gain}/\Delta\nu$ |
| Resonator stability | $0 \le g_1g_2 \le 1$ |
| Coherence length | $l_c = c/\Delta\nu = \lambda^2/\Delta\lambda$ |
| Semiconductor λ | $\lambda = 1240/E_g$ (eV·nm) |
| Photon energy | $E = hc/\lambda$; $\lambda_{max} = 1240/E_g$ |

## 13. Common mistakes

| Mistake | Correction |
|---|---|
| "Two-level laser" | A two-level system **cannot** lase — Boltzmann forbids inversion. Must be 3- or 4-level. |
| Ruby is 4-level | Ruby is the classic **3-level** (E₁ is the ground state) |
| Using cavity length $L$ in $g_{th}$ | It is the **gain medium** length $l$ that appears in $g_{th}$ |
| $q$ is an integer but written as a fraction | $q = 2L/\lambda$ comes out large and non-integral because $\lambda$ isn't an exact multiple; $\nu_q$ must be an integer multiple of $c/2L$ |
| He-Ne = 633 nm | It is **632.8 nm** |
| Single-mode cutoff = 2.4 | It is $V < 2.405$ |
| Confusing gain threshold with threshold power | $g_{th}$ is a gain per unit length; threshold *power* also includes pump efficiency |
| Spontaneous = laser | Spontaneous emission is random and incoherent — that is a bulb/LED, not a laser |

## Cross-References

- **Deep theory owner:** [[module-2-optoelectronics-lasers-fiber-optics]] (fiber optics, NA, dispersion, EDFA, photodiodes, nonlinear optics — not covered here)
- Quantum foundation: [[module-3-quantum-mechanics]] (why $E_2 - E_1 = h\nu$ is quantized)
- Optics: [[module-1-optics-interference-diffraction]] (coherence, Young's double-slit measurement of spatial coherence)
- Semiconductors: [[module-4-semiconductors-electromagnetism]] (p-n junctions, band gap)
- Course context: [[source-map-physics-sem1]] (catalogs the unopened Sem-1 laser/fibre sources — `2.1 Laser/` holds 8 files not yet ingested; see section D for next-ingest order)

*Condensed 2026-10-02 from [[module-2-optoelectronics-lasers-fiber-optics]] for Physics-B exam revision.*