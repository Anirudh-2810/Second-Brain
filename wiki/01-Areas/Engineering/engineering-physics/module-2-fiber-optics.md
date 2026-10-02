---
course_code: "ENG-PHY"
course_name: "Engineering Physics"
unit: "Module 2 Unit 2 — Optical Fibres"
date: "2026-10-02"
last_updated: "2026-10-02"
description: "Engineering Physics Module 2 Unit 2 optical fibres from Dr. Suren Patwardhan's faculty notes — total internal reflection, SI/GRIN/SM/MM types with comparison tables, modes, full numerical-aperture derivation, V-number and mode counts, attenuation causes, the three dispersion types, optical windows, bit-rate formula, and telecom system architecture with ASCII flowcharts and worked numericals."
tags: [engineering-physics, optical-fibres, fiber-optics, total-internal-reflection, numerical-aperture, v-number, modes, attenuation, dispersion, intermodal-dispersion, graded-index, step-index, single-mode, optical-window, bit-rate, exam-prep]
confidence: high
aliases: ["Optical fibres", "fiber optics notes", "SVU optical fibres"]
prerequisites: ["Snell's law", "Refractive index", "Basic EM waves"]
sources:
  - "raw-sources/drive-download-.../Semester 1/Physics/Module 2 Photonics/2.2 Optical Fibre/Optical Fibre Notes.pdf"
  - ".../Optical Fibre Formulas..pdf"
  - ".../Optical fibres - Numericals.pdf"
  - ".../Optical Fibres - Questions.pdf"
---

## For future agent

**The dedicated optical-fibres page**, created 2026-10-02 from Dr. Suren Patwardhan's official faculty notes (*"As per Revised Curriculum SVU R-2023"*), which had been sitting unopened in `raw-sources/`. Fiber optics was a **complete gap** — the quick-ref deliberately omitted it and the 73 KB deep module treated it as the back half of a mixed page.

**This page is faculty-authoritative.** Where it disagrees with [[module-2-optoelectronics-lasers-fiber-optics]], **faculty wins for exam purposes.** Recorded discrepancies:

| Item | Deep module says | Faculty says | Use |
|---|---|---|---|
| `Δ` definition | `(n₁²−n₂²)/(2n₁²)` | **`Δ = (n₁−n₂)/n₁`** | **Faculty.** Equivalent to first order for small Δ, and only the faculty form is self-consistent with `i₀ = sin⁻¹(1−Δ)` |
| Ne⁺ metastable energies | 19.78 eV and 20.66 eV (He-Ne transfer) | **Ne⁺ 2s = 18.7 eV, 3s = 20.66 eV** | **Faculty.** The He-Ne numericals use 20.66 − 18.7 = **1.96 eV → 632.8 nm** |
| Mode count | `M ≈ V²/2` only | **`V²/2` (SI) and `V²/4` (GRIN)** | **Faculty** — GRIN halves the mode count |

> **Known typo in the faculty notes prose:** page 5 states `Δ = (n₁−n₂)/n₂`. That contradicts the official *Formulas* sheet, which gives `Δ = (n₁−n₂)/n₁` **and** the identity `n₂ = n₁(1−Δ)` and `i₀ = sin⁻¹(1−Δ)`. Only `(n₁−n₂)/n₁` is self-consistent, so the prose is an error. Verified numerically: for `n₁=1.48, n₂=1.46`, faculty `n₁√(2Δ)` = 0.2433 vs exact NA 0.2425 ✓.

**Laser counterpart:** [[lasers-quick-ref]] (revision) and [[module-2-laser-fibre-question-bank]] (30 theory Qs + 40 numericals). Deep theory: [[module-2-optoelectronics-lasers-fiber-optics]].

---

# Module 2 Unit 2 — Optical Fibres

> **Curriculum:** SVU R-2023 · **CO:** photonics/fibre communication · **Lab:** fibre-optic experiments
> **Laser half:** [[lasers-quick-ref]] · **Question bank:** [[module-2-laser-fibre-question-bank]]

---

## 0. The whole topic in six sentences

1. An optical fibre is a **solid glass/plastic thread** (not hollow) that carries light by **total internal reflection**.
2. Two coaxial regions: the inner **core** (n₁, denser) and the outer **cladding** (n₂, rarer).
3. **Numerical aperture** = light-gathering capacity = `√(n₁² − n₂²)` = `sin` of the acceptance angle.
4. **`V < 2.405` → single mode.** `N_m = V²/2` (SI) or `V²/4` (GRIN).
5. **Attenuation** (dB/km) comes from absorption, Rayleigh scattering (∝ 1/λ⁴) and geometric effects. Optical windows at **1.3 and 1.55 µm**.
6. **Dispersion** (pulse broadening) is **intermodal**, **material** and **waveguide**. Bit rate `B ≈ 0.7/τ`.

---

## 1. Introduction & structure

Optical fibres are **glass or plastic solid threads** (not hollow like a capillary), designed to propagate light, typically in the **IR** region. Their function is to accept and transmit as much light as possible along their length. **The working principle is total internal reflection.**

Since the Standard Telecom Labs of England announced fibres with low transmission loss, applications have grown enormously. Today fibres offer the **safest, cheapest, fastest and highest-capacity** data transfer medium — and are used beyond comms, in **surgery, defence and sensors**.

**Two coaxial regions:**

```
   ┌──────────────────────────────────────────┐
   │              Buffer / Coating            │
   │   ┌──────────────────────────────────┐   │
   │   │        Cladding  (n₂)           │   │   n₁ > n₂
   │   │   ┌──────────────────────────┐   │   │
   │   │   │   Core  (n₁)            │   │   │   core dia:  5 – 125 µm
   │   │   │   light is trapped here  │   │   │   cladding dia: 25 – 500 µm
   │   │   └──────────────────────────┘   │   │
   │   └──────────────────────────────────┘   │
   └──────────────────────────────────────────┘
```

| Feature | Value |
|---|---|
| Core diameter | **5 – 125 µm** |
| Cladding diameter | **25 – 500 µm** |
| RI difference (n₁ − n₂) | on the order of **0.01 to 0.1** — too small to see by eye |

**The two characterizing parameters to memorise:** the **numerical aperture (NA)** and the **normalised frequency (V-number)**.

**The acceptance cone** is the measure of light-gathering capacity: if rays from a source fall inside this cone, they undergo total internal reflection.

### Advantages of optical fibres

1. Cheaper, smaller, lighter, durable, chemically stable, mechanically flexible
2. Safer, **immune to stray EM signals**, reduced cross-links, noise-free
3. High bandwidth, very high data speeds
4. Lower losses

---

## 2. Principle — Total Internal Reflection

Light going from a **higher** index (n₁) to a **lower** index (n₂). Let *i* be the incidence angle and *r* the refraction angle.

```
   STAGE-BY-STAGE (what the faculty notes describe)
   ────────────────────────────────────────────

   (1) n2 < n1  ->  ray bends AWAY from the normal, so r < i
        │
        v
   (2) partial reflection + partial transmission
        │
        v
   (3) increase i  ->  r keeps increasing
        │
        v
   (4) i = i0 :  refracted ray runs almost PARALLEL to the interface
        │        this is the CRITICAL ANGLE, and  sin(i0) = n2/n1
        v
   (5) increase i further  ->  NO transmission at all
                               COMPLETE REFLECTION  =  TIR
```

**TIR occurs when light in a denser medium hits a rarer medium at or above the critical angle.** In a fibre the **core is the denser medium** and the **cladding the rarer**, so light stays in the core by successive TIRs.

$$\boxed{\sin i_0 = \frac{n_2}{n_1}}$$

**TIR flow diagram:**

```
   n1 = CORE (denser)
   ──────────────────────────────────────
        │  i0 = critical angle
        │\  refracted ray (r → 90°)
        │ \
   ─────┼──\────────────────  n1 / n2 interface
        │   \___________________________
        │   ↖  reflected back INTO the core
        │        (complete reflection)
   ──────────────────────────────────────
   n2 = CLADDING (rarer)
```

---

## 3. Types of optical fibres

**Simple definition of "mode":** the total number of **allowed paths** inside the core.

```
   BY APPLICATION
   ├── Single mode (SM)   — one mode (axial only)
   └── Multimode (MM)
         ├── Step index (SI)     — core RI uniform, abrupt change at interface
         └── Graded index (GRIN) — RI varies gradually from axis outward

   BY MATERIAL
   ├── All-glass        — superior transmission quality (common now)
   └── Plastic / plastic-coated silica (PCS) — cheaper, higher loss (earlier era)
```

Graded-index RI can be graded in a **linear, parabolic, or staircase** manner.

**Refractive index profile** = the variation of RI with axial distance from the central axis.

### Ray propagation in each type

```
   SINGLE MODE (SM)          GRADED INDEX (MM-GI)        STEP INDEX (MM-SI)
   rays hug the axis         RI highest at axis,          RI uniform, ray
   ~straight line             falls outward -> ray        zig-zags, reflecting
                              curves repeatedly,           off the wall each time
   ─────────────────────      constant path length        ─────────────────────
      ───────────                ╭──╮                      /‾‾\ /‾‾\ /‾‾\
                                ╱    ╲                    ╱    V    V    ╲
   only axial modes       shorter, faster; longer,    longer path, same speed
                           slower  ->  arrive together     -> arrive late
```

- **SM:** rays make a very small angle with the axis; propagation is almost parallel to the axis.
- **MM-SI:** rays go away from the axis undergoing multiple internal reflections (**zig-zag**). They may stay in the axial plane (**meridional rays**) or travel through non-axial planes (**skew rays**).
- **MM-GI:** the ray undergoes constant deviation because the RI continuously changes from axis toward the cladding boundary.

### Single mode vs. multimode

| Property | Single mode | Multimode |
|---|---|---|
| Modes supported | **axial only** | axial and non-axial |
| Core diameter | small (**5–10 µm**) | larger (**50–100 µm**) |
| Source | works with **laser diode only** | works with **LED as well as** laser diode |
| Attenuation | **lowest** | higher |
| Dispersion limiting factor | **waveguide dispersion** | waveguide dispersion insignificant |
| Distance | **very long** | short to medium |
| RI profile | step index only | step **or** graded |
| Material | glass | glass or plastic |

### Step index vs. graded index (both multimode)

| Property | Step index (SI) | Graded index (GRIN) |
|---|---|---|
| Core RI | **uniform** | **gradually lowered** from the axis |
| Pulse distortion | **suffers** from it | **overcome** by RI grading |
| Bandwidth | **lower** | **higher** |
| Numerical aperture | **higher** | lower |
| Reflection losses | **present** | minimal |
| Attenuation | **higher** | lower |
| Modes | can be single-mode or multimode | **only multimode** |
| Manufacturing | **easier** | complex |

---

## 4. Modes of propagation

**Simple sense:** a mode is an **allowed path** for a ray inside the fibre. Even though the TIR condition is satisfied, the fibre does **not** support every ray in the acceptance cone — only certain selective paths, depending on the ratio of **wavelength to core diameter**.

| Type | Path | Description |
|---|---|---|
| **Axial** (axial mode) | along/parallel to the axis | lowest order |
| **Non-axial — meridional** | zigzag **crossing** the axis | |
| **Non-axial — skew** | zigzag **not crossing** the axis | higher order |

**Deeper sense:** the fibre is a **waveguide** for EM waves. To satisfy the electromagnetic boundary conditions, light is in phase only along certain directions (determined by `d/λ`) so the waves reinforce each other. **Those directions are the modes.**

---

## 5. Numerical Aperture — full derivation

**NA is the amount of light the fibre can accept — its light-gathering capacity.** The acceptance cone has semi-vertical angle θ_c, and

$$\boxed{NA = \sin\theta_C}$$

**TIR requires `i ≤ i₀` and therefore `θ ≥ θ_C`.**

### The derivation (follow every step)

```
                    A
                    |\
            θ_C    / | \   n1 = core (n1 > n2)
                  /  |  \
        n0 ----->B   |   \
                / φ_C|    \
   external    /     |     \
   medium  ===C=======+======+====  core-cladding interface
                     i0     r = 90°
                     │\____________________ n2 = cladding
                     ↖ reflected back
```

**Step 1 — Snell at the external/core interface.** In general `sin θ / sin φ = n₁/n₀`, so:

$$n_0 \sin\theta = n_1 \sin\phi$$

At `θ = θ_C`, write `φ = φ_C`:

$$n_0 \sin\theta_C = n_1 \sin\phi_C \qquad \text{(1)}$$

**Step 2 — Snell at the core/cladding interface.** In general `sin i / sin r = n₂/n₁`, so `n₁ sin i = n₂ sin r`. But at `θ = θ_C` the ray hits at the critical angle: **`i = i₀` and `r = 90°`**. Therefore:

$$n_1 \sin i_0 = n_2 \sin 90 \;\Rightarrow\; \sin i_0 = \frac{n_2}{n_1} \qquad \text{(2)}$$

**Step 3 — geometry.** In triangle AOB the two angles at the core interface are complementary, so:

$$\sin\phi_C = \cos(90 - \phi_C) = \cos i_0 = \sqrt{1 - \sin^2 i_0}$$

**Step 4 — combine.**

$$n_0 \sin\theta_C = n_1 \sin\phi_C = n_1 \sqrt{1 - \sin^2 i_0} = n_1 \sqrt{1 - \frac{n_2^2}{n_1^2}} = \sqrt{n_1^2 - n_2^2}$$

**But `n₀ sin θ_C` *is* the numerical aperture.** Hence:

$$\boxed{NA = \sqrt{n_1^2 - n_2^2}}$$

**Step 5 — the practical approximation.** For light incident from **air, n₀ = 1**. With the fractional RI difference `Δ = (n₁ − n₂)/n₁`:

$$\boxed{NA \approx n_1\sqrt{2\Delta}}$$

### The three NA forms (all exam answers)

$$\boxed{NA = n_0 \sin\theta_C = \sqrt{n_1^2 - n_2^2} \approx n_1\sqrt{2\Delta}}$$

### Related angles

$$\boxed{\theta_C = \sin^{-1}(NA)} \quad \text{(external acceptance angle)}$$
$$\boxed{i_0 = \sin^{-1}\!\left(\frac{n_2}{n_1}\right) = \sin^{-1}(1-\Delta)} \quad \text{(internal critical angle)}$$

### Worked numerical — Q1 (classwork)

`n₁ = 1.46`, `n₂ = 1.42`.

$$NA = \sqrt{1.46^2 - 1.42^2} = \sqrt{2.1316 - 2.0164} = \sqrt{0.1152} = \boxed{0.339}$$

$$\theta_C = \sin^{-1}(0.339) = \boxed{19.8°}$$

---

## 6. V-number and number of modes

$$\boxed{V = \frac{2\pi a}{\lambda} \times NA}$$

where *a* = core **radius**, λ = wavelength, NA = numerical aperture. **V is dimensionless** — it is a ratio, which is why it is called *normalised frequency*.

**Maximum number of modes supported:**

$$\boxed{N_m = \frac{V^2}{2} \;\;\text{(multimode step index)} \qquad N_m = \frac{V^2}{4} \;\;\text{(multimode graded index, parabolic)}}$$

**Single-mode criterion** — from electromagnetic theory:

$$\boxed{V < 2.405 \;\Rightarrow\; \text{single-mode fibre}}$$

**Decision flow:**

```
   compute V = (2πa/λ)·NA
          │
          v
    V < 2.405 ?
      /      \
    YES       NO
     │         │
     v         v
  SINGLE    MULTIMODE
  MODE      (SI: Nm = V²/2
  (axial    GRIN: Nm = V²/4)
   only)
```

### Worked numerical — Q4 (classwork)

`NA = 0.3`, `a = 0.05 mm = 5×10⁻⁵ m`, `λ = 1.3 µm = 1.3×10⁻⁶ m`.

$$V = \frac{2\pi \times 5\times10^{-5}}{1.3\times10^{-6}} \times 0.3 = \frac{3.1416\times10^{-4}}{1.3\times10^{-6}} \times 0.3 = 241.66 \times 0.3 = \boxed{72.5}$$

$$N_m = \frac{V^2}{2} = \frac{72.5^2}{2} = \frac{5256}{2} = \boxed{2628 \text{ modes}}$$

Since 72.5 >> 2.405, this is firmly **multimode**.

### Worked numerical — Q5 (classwork): limiting radius for single mode

`NA = 0.025`, `λ = 850 nm`. Set `V = 2.405` and solve for *a*:

$$2.405 = \frac{2\pi a}{850\times10^{-9}} \times 0.025$$

$$a = \frac{2.405 \times 850\times10^{-9}}{2\pi \times 0.025} = \frac{2.044\times10^{-6}}{0.15708} = \boxed{13.0\ \mu m}$$

So the core radius must be **below ≈13 µm** (diameter ≈26 µm) for single-mode at 850 nm.

---

## 7. Attenuation

**Attenuation** is the loss of signal while propagating as light through the fibre. It is measured on a **decibel (dB) logarithmic scale**:

$$\boxed{\alpha = \frac{1}{L}\,10\log\!\left(\frac{P_{in}}{P_{out}}\right) \ \text{dB/km} \quad (L \text{ in km})}$$

Optical fibres typically give **0.1 – 0.2 dB/km**, against copper cables at **2 – 3 dB/km at best**.

### Three causes (memorise all three)

**1. Absorption** — two kinds:

| Kind | Detail |
|---|---|
| **Intrinsic** | absorption by the glass/plastic itself. Glass has two strong bands: **0.1 – 0.3 µm (UV)** = *electronic absorption* and **7 – 12 µm (IR)** = *molecular vibrational absorption*. Plastics have much higher absorption → higher attenuation |
| **Impurities** | the **chief contributors**. Cannot be fully removed. **OH⁻ radicals** mix in during manufacture; also **Cu, Ni, Cr, V, Mn** |

**2. Rayleigh scattering** — light passes through a medium with a **non-uniform distribution of mass and density**. Glass and plastic are **disordered (amorphous)** with local microscopic density variations, hence local RI variations. The scattering is

$$\boxed{\text{scattering} \propto \frac{1}{\lambda^4}}$$

**3. Geometric effects** — from **manufacturing defects**: irregular core/cladding diameters, stress from the coating and cabling process, **bends and kinks** during installation. Includes **bending loss**: if a fibre is bent into a loop, part of the incident light **loses the critical angle** and leaks out.

### Optical windows

```
   Attenuation (dB/km)
        │
   10 ──┤╲
        │ ╲   Rayleigh scattering  ( ∝ 1/λ⁴ )
    5 ──┤  ╲
        │   ╲
    2 ──┤    ╲
    1 ──┤     ╲╱╲    OH⁻ absorption peaks
        │      ╳  ╲
  0.5 ──┤     ╱╲  ╲
        │    ╱   ╲  ╲
  0.2 ──┤   ╱     ╲__╲___
  0.1 ──┤  ╱            ╲___
        │
        └──┬───┬───┬───┬───┬───┬───→ λ (µm)
          0.8  1.0 1.2 1.3 1.5 1.6
                    ▲       ▲
                 WINDOW 1  WINDOW 2
                (~1.3 µm) (~1.55 µm)
```

The net attenuation is **lower in two ranges: around 1.3 µm and around 1.55 µm.** These are the **optical windows**. Almost all LEDs and laser diodes are designed to emit in these ranges so the light suffers minimum attenuation.

### Worked numerical — Q6 (classwork)

`P_in = 5 mW` → `P_out = 0.2 mW` over `L = 50 km`.

$$\alpha = \frac{1}{50}\,10\log\!\left(\frac{5}{0.2}\right) = \frac{1}{50}\times 10\log(25) = \frac{1}{50}\times 13.98 = \boxed{0.2796 \approx 0.28\ \text{dB/km}}$$

---

## 8. Dispersion

**Dispersion** is the **broadening of a pulse** as it travels through the fibre. Measured in **ns/km**. Typical of optical fibres only. Three mechanisms.

**Decision flow:**

```
              DISPERSION (pulse broadening)
                        │
      ┌─────────────────┼──────────────────┐
      v                 v                  v
  MATERIAL         WAVEGUIDE          INTER-MODAL
  different λ      energy leaking     different modes
  travel at        into cladding      travel different
  different        travels faster     paths -> different
  speeds           -> arrive early     arrival times
      │                 │                  │
  fix: laser        significant in      worst in STEP-INDEX
  source            SINGLE MODE        MULTIMODE (zigzag
  (narrow Δλ)       (tiny core)        takes longer)
                                        │
                                        v
                              fixed by GRADED INDEX
                              (longer path offset by
                               higher speed)
```

**1. Material dispersion.** Glass/plastic is **dispersive**: different wavelength components move at different speeds. For an LED (many wavelengths) the **shorter** wavelength travels **slower**, so the pulse broadens. Depends on the **spectral width of the source** — so it is greatly reduced by using a **laser**. But laser circuits costlier than LED.

**2. Waveguide dispersion.** Although the ray is totally internally reflected, **part of the light energy penetrates into the cladding** — because the travelling wave is an EM wave and the medium is a dielectric, so an **induced electric field** appears in the cladding. That penetrated part travels **slightly faster** than the core-confined part, so it arrives early. **Significant in single-mode fibres**, because the core diameter is extremely small.

**3. Inter-modal dispersion.** Different modes travel different directions, so they take different times to cover the same fibre length. The **axial ray takes the least time**; **zigzag rays take longer**. Worst in **step-index multimode**. As time passes the modes no longer arrive together and synchronisation is lost.

**How graded index fixes it — the compensation argument:**

```
   STEP INDEX (SI)                 GRADED INDEX (GRIN)
   axial ray:  ────────────►      axial ray: short path, but SLOW
   zigzag ray: /‾\__/‾\__/►            (highest RI near axis)
                 longer path,
                 SAME speed
   ⇒ arrive at different times     zigzag ray: longer path, but FASTER
   ⇒ PULSE SPREADS                 (RI falls outward)
                                   ⇒ longer distance is compensated
                                     by higher speed
                                   ⇒ ALL MODES STAY SYNCHRONOUS
```

### Intermodal dispersion formulas

$$\boxed{\tau_i = \frac{n_1 L \Delta}{c} \quad \text{(SI fibre)} \qquad \tau_i = \frac{n_2 L \Delta^2}{2c} \quad \text{(GRIN, parabolic)}}$$

$$\boxed{\tau = \sqrt{\tau_i^2 + \tau_m^2}} \quad \text{(total, neglecting waveguide dispersion)}$$

> ### ⚠️ Conversion you must not forget
> $$\boxed{1\ \text{sec/m} \equiv 10^{12}\ \text{ns/km}}$$
> Every intermodal-dispersion answer is wanted in **ns**, and this factor appears in every fibre numerical.

### Maximum bit rate

$$\boxed{B \approx \frac{0.7}{\tau} \ \text{bits/sec}, \qquad \tau = \sqrt{\tau_i^2 + \tau_m^2} \text{ in sec}}$$

Usually expressed in **Mbps**.

### Worked numerical — Q9 (classwork): intermodal dispersion

`n₁ = 1.48`, `n₂ = 1.45`, `L = 2500 m`.

$$\Delta = \frac{n_1 - n_2}{n_1} = \frac{0.03}{1.48} = 0.02027$$

$$\tau_i = \frac{n_1 L \Delta}{c} = \frac{1.48 \times 2500 \times 0.02027}{3\times10^{8}} = \frac{75.0}{3\times10^{8}} = 2.50\times10^{-7}\ \text{s}$$

$$\tau_i = 2.50\times10^{-7}\text{ s} \times 10^{12} = \boxed{250\ \text{ns}}$$

**Sanity check:** 2500 m = 2.5 km, and the standard figure for step-index fibre is ~100 ns/km → 250 ns ✓.

---

## 9. Optical-fibre communication system

Optical fibres carry far higher bandwidth than radio, because they operate at **hundreds of terahertz to petahertz** versus up to **gigahertz** for radio/microwave. A typical system has three blocks:

```
   DATA (music, photo, ...)
        │
        v
  ┌─────────────────────────────────────────────────┐
  │ 1. TRANSMITTER UNIT                             │
  │    electrical data generator                    │
  │      -> modulate onto a high-freq carrier       │
  │         (digital modulation is the norm)        │
  │      -> driver circuit converts to optical form │
  │      -> LED or LASER DIODE is the converter      │
  └─────────────────────────────────────────────────┘
        │  optical signal
        v
  ┌─────────────────────────────────────────────────┐
  │    CHANNEL / WAVEGUIDE = the optical fibre       │
  │    (single mode, SI or GRIN depending on data    │
  │     volume, quality needs, environment)          │
  └─────────────────────────────────────────────────┘
        │
        v
  ┌─────────────────────────────────────────────────┐
  │ 2. RECEIVER UNIT                                │
  │    photodetector (normally OFF; light incident    │
  │      -> small current pulse, ~microamperes)      │
  │      -> amplification to a set value             │
  │      -> wave-shaper + transducer to restore      │
  │        the original signal                       │
  └─────────────────────────────────────────────────┘
        │
        v
   RECOVERED DATA
        │
        v
  ┌─────────────────────────────────────────────────┐
  │ 3. REPEATER UNITS + COUPLERS                     │
  │    needed at regular intervals to redesign the    │
  │    signal in BOTH amplitude and waveform          │
  │    (light suffers attenuation + distortion)       │
  │    optical couplers join fibre-source,           │
  │      fibre-detector, many-to-one or one-to-many   │
  └─────────────────────────────────────────────────┘
```

**The repeater requirement is the direct consequence of §7 and §8:** light attenuates *and* distorts, so the signal must be regenerated periodically rather than merely amplified.

---

## 10. Formula sheet (faculty, authoritative)

| # | Parameter | Formula |
|---|---|---|
| 1 | Numerical aperture | `NA = n₀ sin θ_C = √(n₁² − n₂²) ≈ n₁√(2Δ)` |
| 2 | Acceptance angle (external) | `θ_C = sin⁻¹(NA)` |
| 3 | Critical angle (internal) | `i₀ = sin⁻¹(n₂/n₁) = sin⁻¹(1 − Δ)` |
| 4 | Fractional RI difference | `Δ = (n₁ − n₂)/n₁`, and `n₂ = n₁(1 − Δ)` |
| 5 | V-number | `V = (2πa/λ)·NA`; **SM if `V < 2.405`** |
| 6 | Modes | `N_m = V²/2` (SI); `N_m = V²/4` (GRIN) |
| 7 | Attenuation | `α = (1/L)·10 log(P_in/P_out)` dB/km, **L in km** |
| 8 | Intermodal dispersion | `τ_i = n₁LΔ/c` (SI); `τ_i = n₂LΔ²/2c` (GRIN); **`1 sec/m ≡ 10¹² ns/km`** |
| 9 | Max bit rate | `B = 0.7/τ` bits/sec; `τ = √(τ_i² + τ_m²)` sec |
| — | Rayleigh scattering | `∝ 1/λ⁴` |
| — | Optical windows | ~1.3 µm and ~1.55 µm |

---

## 11. Quick test (10 questions)

| # | Question | Answer |
|---|---|---|
| 1 | What principle makes a fibre work? | **Total internal reflection** in the core (denser) against the cladding (rarer) |
| 2 | State the TIR condition. | Denser → rarer medium at incidence **≥ critical angle**, `sin i₀ = n₂/n₁` |
| 3 | Write NA three ways. | `n₀ sin θ_C = √(n₁²−n₂²) ≈ n₁√(2Δ)` |
| 4 | What is the single-mode criterion? | **`V < 2.405`** |
| 5 | Mode count for SI and GRIN? | `V²/2` and `V²/4` respectively |
| 6 | How many modes can a **single-mode** fibre support? | **Exactly one** (axial only) |
| 7 | Name the three causes of attenuation. | **Absorption** (intrinsic + impurities), **Rayleigh scattering** (∝1/λ⁴), **geometric effects** (bends, kinks, dimension irregularity, stress) |
| 8 | Where are the two optical windows? | **~1.3 µm and ~1.55 µm** |
| 9 | Name the three dispersion types. | **Intermodal**, **material**, **waveguide** |
| 10 | Why does graded index beat step index? | Longer zigzag path is offset by higher speed (RI falls outward), so all modes stay synchronous |
| 11 | Convert 250 ns/km of dispersion into sec/m. | `250 × 10⁻⁹/10³ = 2.5×10⁻¹⁰ sec/m` (or `2.5×10⁻¹⁰ × 10¹² = 250 ns/km` ✓) |

---

## Cross-References

- **Laser half of this module:** [[lasers-quick-ref]] (revision sheet) · [[module-2-laser-fibre-question-bank]] (30 theory Qs + 40 numericals)
- **Deep theory (fibre is ch. 4-6 there):** [[module-2-optoelectronics-lasers-fiber-optics]] — keep its NA/V-number derivations, but **faculty values win** where they differ (see the table at the top)
- **Physics hub:** [[engineering-physics/overview]] · **Module 1:** [[module-1-optics-interference-diffraction]]
- **Quantum background:** [[module-3-quantum-mechanics]] (photon energy `E = hc/λ`)
- **Semiconductors:** [[module-4-semiconductors-electromagnetism]] (source LEDs and laser diodes)
- **Ingest method:** [[raw-sources-ingest-workflow]]

*Ingested 2026-10-02 from Dr. Suren Patwardhan's `Optical Fibre Notes.pdf` (10 pp), `Optical Fibre Formulas..pdf`, `Optical fibres - Numericals.pdf`, `Optical Fibres - Questions.pdf` — all marked "As per Revised Curriculum SVU R-2023".*