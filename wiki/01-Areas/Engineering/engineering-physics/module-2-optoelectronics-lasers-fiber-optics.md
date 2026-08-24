---
module: "engineering-physics"
topic: "Module 2: Optoelectronics - Lasers & Fiber Optics (Deep Dive)"
tags: [optoelectronics, lasers, fiber-optics, photonics, stimulated-emission, optical-fibers, einstein-coefficients, numerical-aperture, dispersion, laser-resonators, photodiodes]
last_updated: "2026-08-17"
prerequisites: ["Wave Optics", "Quantum Mechanics Basics", "Electromagnetic Waves", "Semiconductor Physics"]
---

# Module 2: Optoelectronics — Lasers & Fiber Optics (Deep Dive)

> The physics of light generation, amplification, and transmission — from Einstein's prediction to modern fiber networks. This module covers the complete theoretical and quantitative framework for lasers, optical fibers, and optoelectronic devices.

---

## Table of Contents

1. [Interaction of Radiation with Matter](#1-interaction-of-radiation-with-matter)
2. [Lasers — Theory & Types](#2-lasers--theory--types)
3. [Laser Resonators & Mode Structure](#3-laser-resonators--mode-structure)
4. [Fiber Optics — Structure & Propagation](#4-fiber-optics--structure--propagation)
5. [Attenuation & Dispersion in Fibers](#5-attenuation--dispersion-in-fibers)
6. [Fiber Optic Communication Systems](#6-fiber-optic-communication-systems)
7. [Optoelectronic Devices](#7-optoelectronic-devices)
8. [Nonlinear Optics](#8-nonlinear-optics)
9. [Worked Example Problems (Step-by-Step)](#9-worked-example-problems-step-by-step)
10. [Common Mistakes & Traps](#10-common-mistakes--traps)
11. [Key Formulas Quick Reference](#11-key-formulas-quick-reference)

---

## 1. Interaction of Radiation with Matter

### 1.1 Three Fundamental Processes — Energy Level Diagram

When electromagnetic radiation interacts with atoms at two energy levels $E_1$ (ground) and $E_2$ (excited), three processes occur:

```
    ABSORPTION              SPONTANEOUS EMISSION        STIMULATED EMISSION
    ═══════════             ═══════════════════         ═══════════════════

    E₂ ─ ─ ─ ─             E₂ ─ ─ ─ ─ ─ ─ ─           E₂ ─ ─ ─ ─ ─ ─ ─
      │                       │                          │
      │ hν (in)               │ hν (out) random          │ hν (in) ──→ hν (out)
      │ (absorbed)            │ (spontaneous)            │   (identical copy)
      │                       │                          │
    E₁ ───────             E₁ ───────                  E₁ ───────

    Rate: B₁₂·ρ(ν)·N₁     Rate: A₂₁·N₂              Rate: B₂₁·ρ(ν)·N₂
```

#### (a) Absorption

An atom in ground state $E_1$ absorbs a photon of energy $h\nu = E_2 - E_1$ and jumps to excited state $E_2$.

$$E_2 - E_1 = h\nu$$

**Rate of absorption:**

$$R_{abs} = B_{12} \cdot \rho(\nu) \cdot N_1$$

where:
- $B_{12}$ = absorption Einstein coefficient (m³/J·s²)
- $\rho(\nu)$ = spectral energy density of radiation at frequency $\nu$ (J/m³·Hz)
- $N_1$ = number density of atoms in ground state (m⁻³)

#### (b) Spontaneous Emission

An excited atom returns to ground state **without external stimulation**, emitting a photon in a random direction with random phase.

**Rate of spontaneous emission:**

$$R_{spon} = A_{21} \cdot N_2$$

where:
- $A_{21}$ = spontaneous emission Einstein coefficient (s⁻¹), also called the Einstein A coefficient
- $N_2$ = number density of atoms in excited state (m⁻³)

**Characteristics:**
- Random phase, random direction → **incoherent light**
- Lifetime: $\tau_{spon} = \dfrac{1}{A_{21}}$ (typically $10^{-8}$ s for allowed electric dipole transitions)
- This is how ordinary light sources (bulbs, LEDs) work

#### (c) Stimulated Emission

An excited atom is "triggered" by an incoming photon to emit an **identical** photon — same frequency, phase, direction, and polarization.

**Rate of stimulated emission:**

$$R_{stim} = B_{21} \cdot \rho(\nu) \cdot N_2$$

This is the fundamental process behind **laser action**.

### 1.2 Einstein Relations — Detailed Derivation

At thermal equilibrium, the radiation field and the atomic system are in balance, so the rate of upward transitions equals the rate of downward transitions:

$$R_{abs} = R_{spon} + R_{stim}$$

$$B_{12} \cdot \rho(\nu) \cdot N_1 = A_{21} \cdot N_2 + B_{21} \cdot \rho(\nu) \cdot N_2$$

From the Boltzmann distribution at thermal equilibrium:

$$\frac{N_2}{N_1} = \frac{g_2}{g_1} e^{-(E_2-E_1)/k_BT} = \frac{g_2}{g_1} e^{-h\nu/k_BT}$$

Substituting into the equilibrium equation:

$$B_{12} \cdot \rho(\nu) = A_{21} \cdot \frac{g_2}{g_1} e^{-h\nu/k_BT} + B_{21} \cdot \rho(\nu) \cdot \frac{g_2}{g_1} e^{-h\nu/k_BT}$$

Solving for $\rho(\nu)$:

$$\rho(\nu) = \frac{A_{21}}{B_{21}} \cdot \frac{g_2}{g_1} \cdot \frac{1}{\dfrac{g_1 B_{12}}{g_2 B_{21}} e^{h\nu/k_BT} - 1}$$

This must match the Planck radiation law:

$$\rho(\nu) = \frac{8\pi h\nu^3}{c^3} \cdot \frac{1}{e^{h\nu/k_BT} - 1}$$

Comparing both expressions term by term:

$$\boxed{g_1 B_{12} = g_2 B_{21}}$$

$$\boxed{A_{21} = \frac{8\pi h\nu^3}{c^3} B_{21}}$$

**For non-degenerate levels** ($g_1 = g_2$):

$$B_{12} = B_{21}$$

> **Key insight:** The ratio $A_{21}/B_{21} \propto \nu^3$ means stimulated emission becomes relatively more important at **lower** frequencies. At optical frequencies, spontaneous emission dominates unless population inversion is achieved.

### 1.3 Population Inversion

At thermal equilibrium, the Boltzmann distribution gives:

$$\frac{N_2}{N_1} = \frac{g_2}{g_1} e^{-(E_2-E_1)/k_BT}$$

Since $E_2 > E_1$, we have $N_2 < N_1$ — **more atoms in the lower state**. This means absorption dominates over stimulated emission, and a two-level system **cannot** achieve net gain.

**To achieve population inversion, we need a multi-level pumping scheme:**

```
    THREE-LEVEL SYSTEM              FOUR-LEVEL SYSTEM
    ═══════════════════             ══════════════════

    E₃ ─ ─ ─ ─                    E₃ ─ ─ ─ ─
      │  pump                        │  pump
      │  (fast)                      │  (fast)
      ▼                              ▼
    E₂ ─ ─ ─ ─ (metastable)       E₂ ─ ─ ─ ─ (metastable, upper laser)
      │                              │
      │  LASING                      │  LASING
      │  TRANSITION                  │  TRANSITION
      ▼                              ▼
    E₁ ─ ─ ─ ─                    E₁ ─ ─ ─ ─ (fast decay)
      │  (this IS the                  │
      │   ground state)               ▼
      │                              E₀ ─────── (ground state)

    Threshold: N₂ > N₁           Threshold: N₂ > N₁
    Need >50% of atoms pumped     Need very few atoms in E₂
    HIGH threshold power           LOW threshold power
```

**Three-level laser:** More than half the atoms must be pumped from $E_1$ to $E_2$ → very high threshold pump power → typically pulsed operation.

**Four-level laser:** The lower laser level $E_1$ empties quickly to $E_0$, so even a small population in $E_2$ creates inversion → low threshold → continuous wave (CW) possible.

### 1.4 Optical Gain

When population inversion exists ($N_2 > N_1$), stimulated emission dominates → light is **amplified**.

**Gain coefficient (per unit length):**

$$\boxed{g(\nu) = \frac{(N_2 - N_1) c^2 A_{21}}{8\pi \nu^2} \cdot g(\nu, \nu_0)}$$

where $g(\nu, \nu_0)$ is the normalized lineshape function (Lorentzian for homogeneous broadening, Gaussian for inhomogeneous broadening).

**For a simplified monochromatic case:**

$$g_0 = \frac{(N_2 - N_1) c^2 A_{21}}{8\pi \nu_0^2 \Delta\nu}$$

where $\Delta\nu$ is the linewidth.

**Amplified intensity through a gain medium of length $l$:**

$$I = I_0 \, e^{g(\nu) \cdot l}$$

**Gain in dB:**

$$G_{dB} = 10 \log_{10}\left(\frac{I}{I_0}\right) = 10 \log_{10}(e^{gl}) = 4.343 \cdot g \cdot l$$

### 1.5 Decision Tree: Which Laser Type to Use?

```
                    ┌─────────────────────────┐
                    │  Need laser light?       │
                    └───────────┬─────────────┘
                                │
                    ┌───────────▼─────────────┐
                    │  What application?       │
                    └───────────┬─────────────┘
                                │
               ┌────────────────┼────────────────┐
               │                │                │
       ┌───────▼──────┐  ┌─────▼──────┐  ┌──────▼───────┐
       │ Communications│  │ Industrial │  │   Medical    │
       │ & Sensing     │  │ Cutting/   │  │   Surgery/   │
       │               │  │ Welding    │  │   Diagnostics│
       └───────┬──────┘  └─────┬──────┘  └──────┬───────┘
               │                │                │
       ┌───────▼──────┐  ┌─────▼──────┐  ┌──────▼───────┐
       │ Short range?  │  │ High power?│  │ Precision?   │
       └───┬───────┬──┘  └───┬────┬───┘  └───┬──────┬───┘
           │       │         │    │           │      │
         Yes      No       Yes   No         Yes    No
           │       │         │    │           │      │
       ┌───▼──┐ ┌──▼───┐ ┌──▼──┐┌▼──┐  ┌────▼──┐┌──▼───┐
       │ GaAs ││InGaAsP││ CO₂ ││Fiber│  │ArF   ││He-Ne │
       │ LED/ ││laser  ││laser││laser│  │excimer││laser │
       │laser ││1310/  ││10.6 ││(EDFA│  │193nm  ││632.8 │
       │      ││1550nm ││μm   ││)    │  │LASIK  ││nm    │
       └──────┘└───────┘└─────┘└─────┘  └───────┘└──────┘
```

---

## 2. Lasers — Theory & Types

### 2.1 Conditions for Laser Action

For laser oscillation, three conditions must be simultaneously satisfied:

1. **Population inversion** — $N_2 > N_1$ must be achieved and maintained by pumping
2. **Optical resonator** — two mirrors provide feedback so photons pass through the gain medium multiple times
3. **Threshold condition** — round-trip gain ≥ round-trip loss:

$$R_1 R_2 \, e^{2(g - \alpha)l} \geq 1$$

where $R_1, R_2$ are mirror reflectivities, $g$ is the gain coefficient, $\alpha$ is the distributed loss coefficient, and $l$ is the gain medium length.

**Threshold gain:**

$$\boxed{g_{th} = \alpha + \frac{1}{2l} \ln\left(\frac{1}{R_1 R_2}\right)}$$

### 2.2 Three-Level Laser (Ruby Laser)

**Energy scheme:**

- Ground state $E_1$ (level 1)
- Pumped level $E_3$ (level 3) — short-lived ($\tau_3 \sim 10^{-9}$ s)
- Metastable level $E_2$ (level 2) — long-lived ($\tau_2 \sim 3 \times 10^{-3}$ s)

**Process:**
1. Pump atoms from $E_1 \to E_3$ using flash lamp (optical pumping)
2. Fast non-radiative decay: $E_3 \to E_2$ ($\tau_3 \ll \tau_2$)
3. Population accumulates in $E_2$ → inversion between $E_2$ and $E_1$
4. Lasing transition: $E_2 \to E_1$ (694.3 nm, red)

**Problem:** Since $E_1$ is the ground state, more than half the atoms must be pumped from $E_1$ to $E_2$:

$$N_2 > \frac{N_{total}}{2}$$

This requires very high pump power → typically pulsed operation only.

**Example — Ruby laser (Cr³⁺ in Al₂O₃):**
- Pump wavelength: 550 nm (green, broad absorption band)
- Laser wavelength: 694.3 nm (red)
- Output: pulsed, ~1-5 J per pulse
- Efficiency: ~0.1%

### 2.3 Four-Level Laser

**Energy scheme:**

- Ground state $E_0$ (level 0)
- Pumped level $E_3$ (level 3) — short-lived
- Upper laser level $E_2$ (level 2) — metastable
- Lower laser level $E_1$ (level 1) — fast decay to $E_0$

**Process:**
1. Pump $E_0 \to E_3$ (fast non-radiative decay to $E_2$)
2. Population inversion between $E_2$ and $E_1$ (since $E_1$ empties quickly to $E_0$)
3. Lasing: $E_2 \to E_1$

**Advantage:** Since $E_1$ is nearly empty (fast decay to $E_0$), even a small population in $E_2$ creates inversion → very low threshold pump power → CW operation possible.

$$N_2 > N_1 \approx 0 \quad \text{(easily achieved)}$$

**Examples:**
- He-Ne laser (632.8 nm)
- Nd:YAG laser (1064 nm)
- CO₂ laser (10.6 μm)
- GaAs semiconductor laser

### 2.4 Types of Lasers — Comprehensive Comparison

| Laser | Type | Wavelength | Medium | Efficiency | Power | Application |
|-------|------|-----------|--------|-----------|-------|-------------|
| Ruby | 3-level | 694.3 nm | Solid (Cr³⁺) | ~0.1% | ~J/pulse | Holography, medicine |
| He-Ne | 4-level | 632.8 nm | Gas | ~0.1% | 1-5 mW CW | Alignment, barcode scanning |
| Nd:YAG | 4-level | 1064 nm | Solid (Nd³⁺) | ~3% | W-kW | Surgery, manufacturing |
| CO₂ | 4-level | 10.6 μm | Gas | ~10-20% | kW-MW | Cutting, surgery, military |
| GaAs | Semiconductor | 850-900 nm | p-n junction | ~30% | mW-W | Communications, CD players |
| InGaAsP | Semiconductor | 1310/1550 nm | DH junction | ~20% | mW | Fiber telecom |
| ArF | Excimer | 193 nm | Gas (Ar+F₂) | ~1% | mJ/pulse | LASIK eye surgery |
| Ti:Sapphire | 4-level | 650-1100 nm | Solid | ~10% | W | Ultrafast optics, tunable |
| Fiber (EDFA) | 4-level | 1530-1565 nm | Er-doped fiber | ~30% | dB gain | Telecom amplification |
| Diode-pumped solid-state | 4-level | Various | DPSS | ~20% | mW-kW | Green pointers, displays |

### 2.5 He-Ne Laser (Detailed Analysis)

**Gas mixture:** 90% He, 10% Ne at low pressure (~0.5-1 torr)

**Energy transfer mechanism:**

```
    He atoms               Ne atoms
    ═════════              ═════════

    He(2¹S₀) at 20.61 eV ──collision──→ Ne(3s₂) at 20.66 eV
                                        │
                                        │ Radiative decay
                                        ▼
    He(2³S₁) at 19.78 eV ──collision──→ Ne(2s₂) at 19.78 eV
                                        │
                                        │ Radiative decay
                                        ▼
                                     Ne(2p) levels
                                        │
                                        │ 632.8 nm (visible)
                                        ▼
                                     Ne(1s) levels
                                        │
                                        │ Collisional de-excitation
                                        ▼
                                     Ground state
```

- Electron impact excites He to metastable states ($2^1S_0$ and $2^3S_1$)
- Near-resonant energy transfer to Ne via collisions (cross-section ~10⁻¹⁶ cm²)
- Ne has metastable levels at 20.66 eV and 19.78 eV
- Population inversion in Ne → lasing

**Lasing transitions (visible):**
- 632.8 nm (red) — most common, highest gain
- 543.5 nm (green)
- 594.1 nm (yellow)
- 611.9 nm (orange)

**Cavity:** Fabry-Pérot resonator with two mirrors:
- One high reflectivity mirror ($R \approx 99.9\%$)
- One output coupler ($R \approx 98\%$)
- Mirror separation: $L \approx 15-30$ cm
- Output: CW, ~1-5 mW

### 2.6 Semiconductor Laser (Diode Laser)

**Principle:** Population inversion at a forward-biased p-n junction.

**Energy band model:**

```
    p-type          │         n-type
    ═══════         │         ═══════
                    │
    ┌──────────┐    │    ┌──────────┐
    │ Valence  │    │    │Conduction│
    │  Band    │    │    │  Band    │
    └──────────┘    │    └──────────┘
                    │
              Depletion
               Region
                    │
                    │  hν = Eg
                    │  (photon emitted)
                    │
              ──────┘

    GaAs: Eg = 1.42 eV → λ = hc/Eg = 870 nm
```

**Photon energy from band gap:**

$$h\nu = E_g \implies \lambda = \frac{hc}{E_g} = \frac{1240 \text{ eV·nm}}{E_g \text{ (eV)}}$$

**Threshold current density:** $J_{th}$ — minimum current density for lasing. Below $J_{th}$, the device operates as an LED (spontaneous emission). Above $J_{th}$, stimulated emission dominates.

**Types of semiconductor lasers:**

| Type | Structure | Threshold | Modulation Speed |
|------|-----------|-----------|-----------------|
| Homojunction | Same material | High (~10⁴ A/cm²) | Slow |
| Single Heterojunction | One interface | Moderate | Moderate |
| Double Heterojunction (DH) | Sandwich structure | Low (~10³ A/cm²) | Fast |
| Quantum Well | Ultra-thin active (~10 nm) | Very low (~10² A/cm²) | Very fast |
| Distributed Feedback (DFB) | Grating structure | Low | Single-frequency |

### 2.7 Characteristics of Laser Light

| Property | Description | Typical Value (He-Ne) |
|----------|-------------|----------------------|
| **Monochromatic** | Very narrow linewidth | $\Delta\lambda \approx 0.002$ nm |
| **Coherent** | All photons in phase | $l_c \approx 200$ m |
| **Collimated** | Low divergence | $\theta \approx 0.5$ mrad |
| **High intensity** | Can be focused to small spots | MW/cm² |

**Temporal coherence length:**

$$l_c = c \cdot \tau_c = \frac{c}{\Delta\nu} = \frac{\lambda^2}{\Delta\lambda}$$

**Example:** For He-Ne laser, $\Delta\nu \approx 1.5$ MHz:

$$l_c = \frac{3 \times 10^8 \text{ m/s}}{1.5 \times 10^6 \text{ Hz}} = 200 \text{ m}$$

**Spatial coherence:** Allows interference patterns over the entire beam cross-section. Measured using Young's double-slit experiment — fringe visibility gives the coherence area.

**Beam quality factor ($M^2$):**

$$w(z) = w_0 \sqrt{1 + \left(\frac{z}{z_R}\right)^2} \cdot M^2$$

where $z_R = \frac{\pi w_0^2}{\lambda}$ is the Rayleigh range. Ideal Gaussian beam has $M^2 = 1$.

---

## 3. Laser Resonators & Mode Structure

### 3.1 Stable Resonator Conditions

Two mirrors with radii $R_1, R_2$ separated by distance $L$:

**Stability condition:**

$$\boxed{0 \leq g_1 g_2 \leq 1}$$

where $g_1 = 1 - \dfrac{L}{R_1}$ and $g_2 = 1 - \dfrac{L}{R_2}$

**Stability diagram:**

```
    g₂
     │
   1 ┤─────────────● Planar: (∞,∞)→(1,1)
     │            ╱
     │          ╱
     │        ╱  Stable
     │      ╱    region
     │    ╱
     │  ╱
   0 ┤╱──────────────────────── g₁
     │╲
     │  ╲
     │    ╲ Unstable
     │      ╲ region
     │
  -1 ┤● Confocal: (L,L)→(0,0)
     │
     └──┬──┬──┬──┬──┬──┬──
       -1  0  1  2  3  4
```

| Configuration | $R_1$ | $R_2$ | $g_1$ | $g_2$ | Properties |
|--------------|-------|-------|-------|-------|------------|
| **Confocal** | $L$ | $L$ | 0 | 0 | Most stable, smallest mode |
| **Hemispherical** | $L$ | $\infty$ | 0 | 1 | Easy alignment |
| **Planar** | $\infty$ | $\infty$ | 1 | 1 | Highest power, hard to align |
| **Concentric** | $L/2$ | $L/2$ | -1 | -1 | Largest mode (boundary) |
| **General confocal** | $2L$ | $2L$ | 0.5 | 0.5 | Good compromise |

### 3.2 Longitudinal Modes

Standing wave condition in the cavity: $L = q \cdot \dfrac{\lambda}{2}$ where $q$ is an integer.

**Resonant frequencies:**

$$\boxed{\nu_q = q \cdot \frac{c}{2L}}$$

**Mode spacing:**

$$\boxed{\Delta\nu = \frac{c}{2L}}$$

**Example:** For He-Ne laser with $L = 30$ cm:

$$\Delta\nu = \frac{3 \times 10^8}{2 \times 0.3} = 500 \text{ MHz}$$

$$q = \frac{2L}{\lambda} = \frac{2 \times 0.3}{632.8 \times 10^{-9}} \approx 9.5 \times 10^5$$

```
    Gain
    curve
     ╱╲
    ╱  ╲
   ╱    ╲
  ╱  │││││╲          Longitudinal modes
 ╱   │││││ ╲         under gain curve
╱    │││││  ╲
─────┼┼┼┼┼─────── Frequency
     │││││
     ▲
     Only modes within gain bandwidth
     above threshold will oscillate
```

### 3.3 Transverse Modes (TEM)

**Mode notation:** TEM$_{mn}$ where $m$ and $n$ are integers representing the number of nodes in the transverse field pattern.

```
    TEM₀₀         TEM₀₁         TEM₁₀         TEM₁₁         TEM₂₀
    (Gaussian)
    ┌─────┐      ┌─────┐      ┌─────┐      ┌─────┐      ┌─────┐
    │█████│      │█   █│      │█ █ █│      │█   █│      │█ █ █│
    │█████│      │█████│      │█████│      │██ ██│      │ █ █ │
    │█████│      │█   █│      │█ █ █│      │█   █│      │█ █ █│
    └─────┘      └─────┘      └─────┘      └─────┘      └─────┘

    Round         Two           Two           Four         Three
    spot          lobes         lobes         lobes        lobes
```

- **TEM₀₀** is the fundamental Gaussian mode — most commonly used
- Higher-order modes have larger beam divergence and lower brightness
- Mode selection can be done with apertures or intracavity etalons

---

## 4. Fiber Optics — Structure & Propagation

### 4.1 Optical Fiber Structure

```
         ┌─────────────────────────────────────────┐
         │              Buffer/Coating             │
         │    ┌───────────────────────────────┐    │
         │    │         Cladding (n₂)         │    │
         │    │    ┌───────────────────┐      │    │
         │    │    │  Core (n₁ > n₂)   │      │    │
         │    │    │                   │      │    │
         │    │    │   n₁ = 1.48       │      │    │
         │    │    │   n₂ = 1.46       │      │    │
         │    │    └───────────────────┘      │    │
         │    │         125 μm                │    │
         │    └───────────────────────────────┘    │
         │              250 μm                     │
         └─────────────────────────────────────────┘

    Fiber dimensions:
    ┌──────────────────────────────────────────┐
    │ Parameter     │ SMF-28   │ MMF (62.5/125)│
    ├──────────────────────────────────────────┤
    │ Core dia.     │ 8.2 μm   │ 62.5 μm       │
    │ Cladding dia. │ 125 μm   │ 125 μm        │
    │ Buffer dia.   │ 242 μm   │ 250 μm        │
    │ NA            │ 0.12     │ 0.275          │
    │ Δ             │ 0.36%    │ 1.0%           │
    └──────────────────────────────────────────┘
```

### 4.2 Total Internal Reflection (TIR)

Light is confined in the core by TIR at the core-cladding interface.

```
    n₀ (air) = 1.0
    ════════════════════════════════
         θₐ (acceptance angle)
    ╲    │    ╱
     ╲   │   ╱
      ╲  │  ╱     n₁ (core)
       ╲ │ ╱
    ════╲│╱════════════════════════  θ_c (critical angle)
        ╱│╲
       ╱ │ ╲     n₂ (cladding)
      ╱  │  ╲
    ════════════════════════════════

    For TIR: angle of incidence at core-cladding boundary > θ_c
```

**Critical angle:**

$$\boxed{\theta_c = \sin^{-1}\left(\frac{n_2}{n_1}\right)}$$

**Condition for TIR:** Angle of incidence at core-cladding boundary $> \theta_c$

### 4.3 Numerical Aperture (NA) — Full Derivation

The **acceptance angle** $\theta_a$ is the maximum angle (from fiber axis) at which light can enter and be guided.

**Step-by-step derivation:**

At the air-core interface, apply Snell's law:

$$n_0 \sin\theta_a = n_1 \sin\theta_r \tag{1}$$

At the core-cladding interface, apply TIR condition:

$$\sin\theta_i = \frac{n_2}{n_1} \tag{2}$$

From the geometry of the fiber, the refraction angle $\theta_r$ and incidence angle $\theta_i$ are complementary:

$$\theta_r + \theta_i = 90° \implies \theta_r = 90° - \theta_i \tag{3}$$

Substituting (3) into (1):

$$n_0 \sin\theta_a = n_1 \sin(90° - \theta_i) = n_1 \cos\theta_i$$

From (2): $\cos\theta_i = \sqrt{1 - \sin^2\theta_i} = \sqrt{1 - \left(\frac{n_2}{n_1}\right)^2}$

Therefore:

$$n_0 \sin\theta_a = n_1 \sqrt{1 - \frac{n_2^2}{n_1^2}} = \sqrt{n_1^2 - n_2^2}$$

For air ($n_0 = 1$):

$$\boxed{NA = \sin\theta_a = \sqrt{n_1^2 - n_2^2}}$$

**Relative refractive index difference:**

$$\boxed{\Delta = \frac{n_1^2 - n_2^2}{2n_1^2} \approx \frac{n_1 - n_2}{n_1}}$$

where the approximation holds for small $\Delta$ (typically 0.01-0.03 for telecom fibers).

### 4.4 V-Number (Normalized Frequency)

$$\boxed{V = \frac{2\pi a}{\lambda} \cdot NA}$$

where $a$ is the core radius.

**Mode classification:**
- $V < 2.405$: **Single-mode** fiber (only LP₀₁ mode propagates)
- $V > 2.405$: **Multi-mode** fiber (multiple modes propagate)

**Number of guided modes (step-index):**

$$M \approx \frac{V^2}{2}$$

**Example calculation:**
- Core radius $a = 4.1$ μm (SMF-28)
- $NA = 0.12$
- $\lambda = 1550$ nm

$$V = \frac{2\pi \times 4.1 \times 10^{-6}}{1550 \times 10^{-9}} \times 0.12 = \frac{25.76 \times 10^{-6}}{1.55 \times 10^{-6}} \times 0.12 = 16.62 \times 0.12 = 1.99$$

Since $V = 1.99 < 2.405$ → **single-mode** ✓

### 4.5 Types of Optical Fibers

```
    STEP-INDEX MULTIMODE          GRADED-INDEX MULTIMODE       SINGLE-MODE
    ═══════════════════          ═══════════════════════      ═══════════════

    n(r)                        n(r)                          n(r)
    ┌──┐                        ╱╲                            ┌─┐
    │  │                       ╱  ╲                           │ │
    │  │ core                 ╱    ╲ parabolic                │ │ small
    │  │                      ╱      ╲                        │ │ core
    └──┘                     ╱        ╲                       └─┘
    ─────── cladding        ╀─────────── cladding             ───── cladding

    Light path:               Light path:                    Light path:
    Zigzag (discrete          Sinusoidal (continuous         Single straight
    angles)                   path, equalized lengths)       path (axial ray)

    Large dispersion          Reduced dispersion              Zero intermodal
    Low bandwidth             Higher bandwidth                Highest bandwidth
    Short distance            Medium distance                 Long distance
```

**Graded-index profile:**

$$n(r) = n_1\sqrt{1 - 2\Delta\left(\frac{r}{a}\right)^\alpha}$$

where $\alpha = 2$ for parabolic profile, $\alpha = \infty$ for step-index.

---

## 5. Attenuation & Dispersion in Fibers

### 5.1 Attenuation

Light intensity decreases exponentially with distance:

$$I(z) = I_0 \, e^{-\alpha_{linear} \cdot z}$$

**Attenuation coefficient in dB/km:**

$$\boxed{\alpha_{dB/km} = \frac{10}{L} \log_{10}\left(\frac{P_{in}}{P_{out}}\right)}$$

**Conversion between dB/km and linear:**

$$\alpha_{linear} \text{ (km⁻¹)} = \frac{\alpha_{dB/km}}{10 \log_{10}(e)} = \frac{\alpha_{dB/km}}{4.343}$$

$$P_{out} = P_{in} \cdot 10^{-\alpha_{dB/km} \cdot L / 10} = P_{in} \cdot 10^{-\alpha \cdot L / 10}$$

**Sources of attenuation:**

```
    Attenuation
    (dB/km)
     10 ┤╲
         │ ╲  Rayleigh
      5 ┤  ╲  scattering (∝1/λ⁴)
         │   ╲
      2 ┤    ╲          OH⁻ absorption
      1 ┤     ╲    ╱╲   peaks
         │      ╲  ╱  ╲
    0.5 ┤       ╲╱    ╲
         │              ╲
    0.2 ┤               ╲___
         │                   ╲___  ← Minimum at 1550 nm
    0.1 ┤                       ╲___
         │
         └──┬──┬──┬──┬──┬──┬──┬──┬── Wavelength (nm)
           800 900 1000 1100 1200 1300 1400 1500 1600
```

| Source | Mechanism | Wavelength Dependence |
|--------|-----------|----------------------|
| **Rayleigh scattering** | Density fluctuations frozen in glass | $\propto 1/\lambda^4$ |
| **Material absorption (UV)** | Electronic transitions in SiO₂ | Exponential tail |
| **Material absorption (IR)** | Molecular vibrations (Si-O) | $\propto e^{-\lambda_0/\lambda}$ |
| **OH⁻ ion absorption** | Water contamination | Peaks at 950, 1240, 1385 nm |
| **Waveguide imperfections** | Bends, micro-bends, splices | Wavelength dependent |

**Wavelength windows:**

| Window | Wavelength | Attenuation | Fiber Type | Application |
|--------|-----------|-------------|-----------|-------------|
| First | 850 nm | ~2.5 dB/km | MMF | LANs, short distance |
| Second | 1310 nm | ~0.35 dB/km | SMF/MMF | Metro networks |
| Second (zero dispersion) | 1300 nm | ~0.4 dB/km | SMF | Zero material dispersion |
| Third | 1550 nm | ~0.2 dB/km | SMF | Long-haul, submarine cables |
| L-band | 1565-1625 nm | ~0.25 dB/km | SMF | Extended DWDM |

### 5.2 Dispersion — Pulse Broadening

Dispersion causes pulse spreading → limits bandwidth and data rate.

```
    Input pulse:                 After propagation:
    ┌──┐                         ┌────────┐
    │  │                         │        │
    │  │                         │        │
    └──┘                         └────────┘
    ↑                            ↑
    Short pulse                  Broadened pulse
    (high BW)                    (limited BW)
```

**Bandwidth-distance product:**

$$B \cdot L = \frac{1}{\Delta t_{total}} \cdot L$$

where $\Delta t_{total}$ is the total pulse broadening.

#### (a) Intermodal Dispersion

Different modes travel different path lengths → pulse spreading.

**For step-index fiber, worst-case broadening:**

$$\Delta t_{IM} = \frac{L \cdot n_1}{c} \cdot \frac{n_1 - n_2}{n_2} = \frac{L \cdot n_1 \Delta}{c}$$

**For graded-index fiber (parabolic profile):**

$$\Delta t_{GI} = \frac{L \cdot n_1 \Delta^2}{2c}$$

Improvement factor: $\Delta t_{GI} / \Delta t_{SI} = \Delta/2 \ll 1$

**For single-mode fiber:** Intermodal dispersion = **zero** (only one mode).

#### (b) Material Dispersion

Refractive index depends on wavelength → different wavelengths travel at different speeds.

**Pulse broadening:**

$$\boxed{\Delta t_{mat} = D_{mat} \cdot L \cdot \Delta\lambda}$$

where $D_{mat}$ is the material dispersion parameter (ps/(nm·km)) and $\Delta\lambda$ is the source spectral width.

**Material dispersion parameter:**

$$D_{mat} = -\frac{\lambda}{c} \cdot \frac{d^2 n}{d\lambda^2}$$

**Zero material dispersion wavelength:** $\lambda_0 \approx 1310$ nm for silica.

#### (c) Waveguide Dispersion

Mode propagation characteristics depend on wavelength. Can be engineered (dispersion-shifted fiber, dispersion-flattened fiber).

**Total chromatic dispersion:**

$$D_{total} = D_{mat} + D_{wg}$$

**Dispersion-shifted fiber (DSF):** $D_{total} = 0$ at 1550 nm (by increasing waveguide dispersion to cancel material dispersion).

**Non-zero dispersion-shifted fiber (NZDSF):** Small non-zero dispersion at 1550 nm to suppress four-wave mixing.

#### (d) Polarization Mode Dispersion (PMD)

Birefringence in fiber → different polarization states travel at different speeds.

$$\Delta t_{PMD} = D_{PMD} \cdot \sqrt{L}$$

where $D_{PMD}$ is the PMD coefficient (ps/√km), typically 0.01-1 ps/√km.

**Important for:** High-speed systems (>10 Gbps) over long distances.

### 5.3 Dispersion Comparison Table

| Type | Cause | Depends On | Mitigation |
|------|-------|-----------|-----------|
| **Intermodal** | Multiple modes, different path lengths | Fiber type, NA, length | Single-mode fiber, graded-index |
| **Material** | $n(\lambda)$, source linewidth | $\Delta\lambda$, $\lambda$ | Narrow-linewidth laser, operate at 1310 nm |
| **Waveguide** | Mode confinement varies with $\lambda$ | Fiber design | Dispersion-engineered fiber |
| **PMD** | Core ellipticity, stress birefringence | $\sqrt{L}$ | PMD compensation, low-PMD fiber |

---

## 6. Fiber Optic Communication Systems

### 6.1 Basic System Architecture

```
    ┌──────┐    ┌─────────┐    ┌──────┐    ┌─────────┐    ┌──────┐
    │Data  │───→│Transmitter│──→│Fiber │───→│Optical  │───→│Receiver│
    │Source│    │(Laser/  │    │      │    │Amplifier│    │(Photo-│
    │      │    │ LED +   │    │      │    │(EDFA)   │    │diode) │
    │      │    │Modulator│    │      │    │         │    │       │
    └──────┘    └─────────┘    └──────┘    └─────────┘    └──────┘

    Electrical → Optical → Transmission → Amplification → Optical → Electrical
```

### 6.2 Link Budget Analysis

**Received power:**

$$\boxed{P_{rx} \text{ (dBm)} = P_{tx} \text{ (dBm)} - \alpha L - L_{splices} - L_{connectors} - M_{margin}}$$

where:
- $P_{tx}$ = transmitter power (dBm)
- $\alpha$ = fiber attenuation (dB/km)
- $L$ = fiber length (km)
- $L_{splices}$ = total splice loss (dB)
- $L_{connectors}$ = total connector loss (dB)
- $M_{margin}$ = safety/engineering margin (dB)

**Power conversion:**

$$P_{dBm} = 10 \log_{10}\left(\frac{P_{mW}}{1 \text{ mW}}\right)$$

$$P_{mW} = 10^{P_{dBm}/10}$$

**Power ratio in dB:**

$$\Delta P_{dB} = 10 \log_{10}\left(\frac{P_1}{P_2}\right)$$

**Loss in dB/km → power at distance L:**

$$P(L) = P(0) \cdot 10^{-\alpha L / 10}$$

### 6.3 Optical Amplifiers

#### (a) EDFA (Erbium-Doped Fiber Amplifier)

```
    Signal (1550 nm) ──→ ┌────────────────────────┐ ──→ Amplified signal
                         │    Er-doped fiber       │
    Pump (980 nm) ──→   │    Er³⁺ ions            │    Gain: 20-40 dB
                         │    Population inversion  │
                         └────────────────────────┘

    Gain spectrum: 1530-1565 nm (C-band)
    Noise figure: ~4-6 dB
    Pump power: 50-200 mW
```

- Pumped at 980 nm or 1480 nm
- Amplifies 1530-1565 nm (C-band)
- Gain: 20-40 dB
- Used in long-haul and submarine cables

#### (b) Raman Amplifier

- Based on stimulated Raman scattering in the fiber itself
- Distributed amplification
- Flexible wavelength (depends on pump wavelength: $\lambda_{signal} \approx 1.1 \times \lambda_{pump}$)

#### (c) Semiconductor Optical Amplifier (SOA)

- Semiconductor gain medium
- Compact, can be integrated on chip
- Used in metro networks

### 6.4 Bit Error Rate and Q-Factor

$$Q = \frac{I_1 - I_0}{\sigma_1 + \sigma_0}$$

$$BER \approx \frac{1}{2} \text{erfc}\left(\frac{Q}{\sqrt{2}}\right)$$

| Q-Factor | BER | Required SNR |
|----------|-----|-------------|
| 6 | $10^{-9}$ | 18 dB |
| 7 | $10^{-12}$ | 21 dB |
| 8 | $10^{-15}$ | 24 dB |

---

## 7. Optoelectronic Devices

### 7.1 Light Emitting Diode (LED)

**Principle:** Spontaneous emission at a forward-biased p-n junction.

**Characteristics:**
- Broad spectrum (30-50 nm linewidth)
- Incoherent
- Lower cost than lasers
- Modulation bandwidth: ~100 MHz - 1 GHz
- Used for: displays, short-distance fiber optics, indicators

**Output power:**

$$P_{out} = \eta_{ext} \cdot \frac{h\nu}{e} \cdot I$$

where $\eta_{ext}$ is the external quantum efficiency and $I$ is the forward current.

### 7.2 Photodiode — Detailed Analysis

**Principle:** Absorption of photons creates electron-hole pairs → photocurrent.

```
    ┌──────────────────────────────────┐
    │           Photodiode              │
    │                                  │
    │    ┌────┐   ┌────┐   ┌────┐     │
    │    │ p  │   │ i  │   │ n  │     │ ← PIN structure
    │    │    │   │    │   │    │     │
    │    └────┘   └────┘   └────┘     │
    │      ↑          ↑         ↑      │
    │    Contact   Depletion  Contact  │
    │              Region              │
    └──────────────────────────────────┘

    hν ──→ e⁻-h⁺ pair created in depletion region
            e⁻ drifts to n-side → photocurrent
```

#### PIN Photodiode

- Intrinsic (i) region between p and n
- Wider depletion region → higher quantum efficiency
- Faster response (less capacitance)
- No internal gain

#### Avalanche Photodiode (APD)

- High reverse bias → impact ionization → internal gain
- Gain factor $M$: $I_{APD} = M \cdot I_{PIN}$
- Typical $M$: 10-100
- Higher sensitivity but more noise

**Responsivity:**

$$\boxed{R = \frac{I_{ph}}{P_{opt}} = \frac{\eta e \lambda}{hc}}$$

where:
- $I_{ph}$ = photocurrent (A)
- $P_{opt}$ = incident optical power (W)
- $\eta$ = quantum efficiency (fraction of photons producing carriers)
- $e$ = electron charge ($1.6 \times 10^{-19}$ C)
- $\lambda$ = wavelength (m)
- $h$ = Planck's constant ($6.626 \times 10^{-34}$ J·s)
- $c$ = speed of light ($3 \times 10^8$ m/s)

**Quantum efficiency:**

$$\boxed{\eta = \frac{R \cdot hc}{e\lambda} = \frac{R \cdot 1240 \text{ (eV·nm)}}{\lambda \text{ (nm)}}}$$

**Detectivity:**

$$D^* = \frac{\sqrt{A \cdot \Delta f}}{NEP}$$

where $A$ is the detector area, $\Delta f$ is the bandwidth, and $NEP$ is the noise equivalent power.

### 7.3 Photovoltaic Cell (Solar Cell)

**Principle:** Same as photodiode but optimized for power generation.

**Open circuit voltage:**

$$\boxed{V_{oc} = \frac{kT}{e}\ln\left(\frac{I_L}{I_0} + 1\right) = V_T \ln\left(\frac{I_L}{I_0} + 1\right)}$$

where $V_T = kT/e \approx 26$ mV at 300K.

**Maximum power point:** Where $V \cdot I$ is maximum on the I-V curve.

**Maximum power:**

$$P_{max} = V_{mp} \cdot I_{mp}$$

**Fill factor:**

$$\boxed{FF = \frac{P_{max}}{V_{oc} \cdot I_{sc}}}$$

Typical FF: 0.7-0.85.

**Efficiency:**

$$\eta = \frac{P_{max}}{P_{in}} = \frac{V_{oc} \cdot I_{sc} \cdot FF}{P_{in}}$$

**Shockley-Queisser limit:** Maximum theoretical efficiency for single-junction solar cell ≈ 33.7% (for bandgap ~1.34 eV).

### 7.4 Optical Modulators

| Type | Mechanism | Speed | Application |
|------|-----------|-------|-------------|
| **Electro-optic (Pockels)** | $\Delta n \propto E$ | >10 GHz | High-speed telecom |
| **Acousto-optic** | Bragg diffraction by sound waves | ~MHz | Q-switching, deflection |
| **Mach-Zehnder** | Interference in two arms | >40 GHz | External modulation |
| **Electro-absorption** | Franz-Keldysh / QCSE | >10 GHz | Integrated with DFB laser |

---

## 8. Nonlinear Optics

### 8.1 Second Harmonic Generation (SHG)

Two photons of frequency $\omega$ combine in a nonlinear crystal to produce one photon of frequency $2\omega$.

$$\omega + \omega \to 2\omega$$

**Phase matching condition:** $n(\omega) = n(2\omega)$ (critical for efficient conversion)

**Example:** Nd:YAG 1064 nm → 532 nm (green) using KDP or BBO crystal.

**Conversion efficiency:**

$$\eta_{SHG} \propto I_{pump} \cdot L^2 \cdot d_{eff}^2$$

where $L$ is the crystal length and $d_{eff}$ is the effective nonlinear coefficient.

### 8.2 Stimulated Raman Scattering (SRS)

A pump photon creates a Stokes photon (lower frequency) and a molecular vibration.

$$\omega_{pump} = \omega_{Stokes} + \omega_{vibration}$$

**Applications:** Raman amplifiers (flexible wavelength), Raman lasers, spectroscopy.

### 8.3 Self-Phase Modulation (SPM)

Intensity-dependent refractive index:

$$n = n_0 + n_2 I$$

Pulse modifies its own phase → spectral broadening. Important in ultrafast optics and supercontinuum generation.

---

## 9. Worked Example Problems (Step-by-Step)

### Problem 1: Einstein Coefficient Calculation

**Problem:** A laser medium has a spontaneous emission lifetime $\tau_{spon} = 25$ ns at wavelength $\lambda = 632.8$ nm. Calculate the Einstein A coefficient and the Einstein B coefficient.

**Solution:**

**Step 1:** Calculate $A_{21}$ from the spontaneous emission lifetime:

$$A_{21} = \frac{1}{\tau_{spon}} = \frac{1}{25 \times 10^{-9} \text{ s}}$$

$$\boxed{A_{21} = 4.0 \times 10^7 \text{ s}^{-1}}$$

**Step 2:** Calculate the frequency:

$$\nu = \frac{c}{\lambda} = \frac{3 \times 10^8}{632.8 \times 10^{-9}} = 4.741 \times 10^{14} \text{ Hz}$$

**Step 3:** Calculate $B_{21}$ using the Einstein relation:

$$B_{21} = \frac{c^3}{8\pi h\nu^3} A_{21}$$

First compute $\nu^3$:

$$\nu^3 = (4.741 \times 10^{14})^3 = 1.066 \times 10^{44} \text{ Hz}^3$$

Now substitute:

$$B_{21} = \frac{(3 \times 10^8)^3}{8\pi \times (6.626 \times 10^{-34}) \times (1.066 \times 10^{44})} \times (4.0 \times 10^7)$$

$$B_{21} = \frac{2.7 \times 10^{25}}{8 \times 3.1416 \times 6.626 \times 10^{-34} \times 1.066 \times 10^{44}} \times 4.0 \times 10^7$$

$$B_{21} = \frac{2.7 \times 10^{25}}{1.775 \times 10^{12}} \times 4.0 \times 10^7$$

$$B_{21} = 1.521 \times 10^{13} \times 4.0 \times 10^7$$

$$\boxed{B_{21} = 6.08 \times 10^{20} \text{ m}^3/\text{J·s}^2}$$

**Verification:** Check that $A_{21}/B_{21} = 8\pi h\nu^3/c^3$:

$$\frac{8\pi h\nu^3}{c^3} = \frac{8 \times 3.1416 \times 6.626 \times 10^{-34} \times 1.066 \times 10^{44}}{(3 \times 10^8)^3} = \frac{1.775 \times 10^{12}}{2.7 \times 10^{25}} = 6.574 \times 10^{-14}$$

$$\frac{A_{21}}{B_{21}} = \frac{4.0 \times 10^7}{6.08 \times 10^{20}} = 6.579 \times 10^{-14} \quad \checkmark$$

---

### Problem 2: Population Inversion and Threshold Pump Rate

**Problem:** A four-level laser has the following parameters:
- Upper laser level lifetime: $\tau_2 = 200$ μs
- Lower laser level lifetime: $\tau_1 = 10$ ns
- Pump rate from $E_0$ to $E_3$: $W_p$ (s⁻¹)
- Total atom density: $N_t = 1.0 \times 10^{24}$ m⁻³
- The non-radiative decay from $E_3 \to E_2$ is very fast ($\tau_3 \to 0$)

Find the pump rate needed to achieve $N_2 = 1.0 \times 10^{22}$ m⁻³.

**Solution:**

**Step 1:** Set up the rate equation for $N_2$:

In steady state, the rate of population into $E_2$ equals the rate of depopulation:

$$W_p \cdot N_0 = \frac{N_2}{\tau_2}$$

Since $E_3 \to E_2$ is very fast, all pumped atoms end up in $E_2$.

**Step 2:** Since $N_0 \approx N_t$ (most atoms in ground state for four-level system):

$$W_p = \frac{N_2}{\tau_2 \cdot N_0} \approx \frac{N_2}{\tau_2 \cdot N_t}$$

**Step 3:** Substitute values:

$$W_p = \frac{1.0 \times 10^{22}}{200 \times 10^{-6} \times 1.0 \times 10^{24}}$$

$$W_p = \frac{1.0 \times 10^{22}}{2.0 \times 10^{20}}$$

$$\boxed{W_p = 50 \text{ s}^{-1}}$$

**Step 4:** Calculate the inversion density:

$$N_2 - N_1 \approx N_2 = 1.0 \times 10^{22} \text{ m}^{-3}$$

(since $N_1$ is nearly zero in a four-level system)

---

### Problem 3: Laser Threshold Gain

**Problem:** A He-Ne laser cavity has the following parameters:
- Mirror reflectivities: $R_1 = 0.999$, $R_2 = 0.98$
- Cavity length: $L = 25$ cm
- Gain medium length: $l = 15$ cm
- Distributed loss coefficient: $\alpha = 0.01$ cm⁻¹

Calculate the threshold gain coefficient $g_{th}$.

**Solution:**

**Step 1:** Write the threshold condition:

The round-trip gain must equal the round-trip loss:

$$R_1 \cdot R_2 \cdot e^{2(g_{th} - \alpha)l} = 1$$

**Step 2:** Take natural log of both sides:

$$\ln(R_1) + \ln(R_2) + 2(g_{th} - \alpha)l = 0$$

**Step 3:** Solve for $g_{th}$:

$$g_{th} = \alpha + \frac{1}{2l}\left[\ln\left(\frac{1}{R_1}\right) + \ln\left(\frac{1}{R_2}\right)\right]$$

$$g_{th} = \alpha + \frac{1}{2l}\ln\left(\frac{1}{R_1 R_2}\right)$$

**Step 4:** Calculate the mirror loss term:

$$R_1 R_2 = 0.999 \times 0.98 = 0.97902$$

$$\frac{1}{R_1 R_2} = \frac{1}{0.97902} = 1.02143$$

$$\ln(1.02143) = 0.02120$$

**Step 5:** Calculate $g_{th}$:

$$g_{th} = 0.01 + \frac{0.02120}{2 \times 15}$$

$$g_{th} = 0.01 + \frac{0.02120}{30}$$

$$g_{th} = 0.01 + 0.000707$$

$$\boxed{g_{th} = 0.01071 \text{ cm}^{-1} \approx 1.071 \text{ m}^{-1}}$$

**Interpretation:** The gain medium must provide a gain of at least 1.071 m⁻¹ to overcome the distributed losses and mirror transmission losses.

---

### Problem 4: Laser Cavity Mode Spacing

**Problem:** A Nd:YAG laser uses a cavity of length $L = 12$ cm. Calculate:
(a) The longitudinal mode spacing $\Delta\nu$
(b) The mode number $q$ for $\lambda = 1064$ nm
(c) The frequency of the $q$-th mode
(d) How many longitudinal modes fall within the Neodymium gain bandwidth of $\Delta\nu_{gain} = 0.45$ THz?

**Solution:**

**(a) Mode spacing:**

$$\Delta\nu = \frac{c}{2L} = \frac{3 \times 10^8}{2 \times 0.12} = \frac{3 \times 10^8}{0.24}$$

$$\boxed{\Delta\nu = 1.25 \text{ GHz}}$$

**(b) Mode number:**

$$q = \frac{2L}{\lambda} = \frac{2 \times 0.12}{1064 \times 10^{-9}} = \frac{0.24}{1.064 \times 10^{-6}}$$

$$\boxed{q = 2.256 \times 10^5 \approx 225,564}$$

**(c) Frequency of the $q$-th mode:**

$$\nu_q = q \cdot \frac{c}{2L} = 225,564 \times 1.25 \times 10^9 = 2.8196 \times 10^{14} \text{ Hz}$$

$$\boxed{\nu_q = 282.0 \text{ THz}}$$

**Verification:** $\lambda = c/\nu = 3 \times 10^8 / 2.8196 \times 10^{14} = 1064$ nm ✓

**(d) Number of modes in gain bandwidth:**

$$N_{modes} = \frac{\Delta\nu_{gain}}{\Delta\nu} = \frac{0.45 \times 10^{12}}{1.25 \times 10^9}$$

$$\boxed{N_{modes} = 360 \text{ modes}}$$

---

### Problem 5: Numerical Aperture and Acceptance Angle

**Problem:** A step-index fiber has core refractive index $n_1 = 1.462$ and cladding refractive index $n_2 = 1.447$. Calculate:
(a) The numerical aperture
(b) The acceptance angle in air
(c) The critical angle at the core-cladding interface
(d) The relative refractive index difference $\Delta$

**Solution:**

**(a) Numerical aperture:**

$$NA = \sqrt{n_1^2 - n_2^2}$$

$$NA = \sqrt{(1.462)^2 - (1.447)^2}$$

$$NA = \sqrt{2.1374 - 2.0938}$$

$$NA = \sqrt{0.0436}$$

$$\boxed{NA = 0.2088 \approx 0.209}$$

**(b) Acceptance angle:**

$$\theta_a = \sin^{-1}(NA) = \sin^{-1}(0.2088)$$

$$\boxed{\theta_a = 12.05°}$$

**(c) Critical angle:**

$$\theta_c = \sin^{-1}\left(\frac{n_2}{n_1}\right) = \sin^{-1}\left(\frac{1.447}{1.462}\right)$$

$$\theta_c = \sin^{-1}(0.9897)$$

$$\boxed{\theta_c = 81.73°}$$

**(d) Relative refractive index difference:**

$$\Delta = \frac{n_1^2 - n_2^2}{2n_1^2} = \frac{0.0436}{2 \times 2.1374} = \frac{0.0436}{4.2748}$$

$$\boxed{\Delta = 0.0102 = 1.02\%}$$

**Verification using approximation:**

$$\Delta \approx \frac{n_1 - n_2}{n_1} = \frac{1.462 - 1.447}{1.462} = \frac{0.015}{1.462} = 0.01026 = 1.03\%$$

The approximation is very good for small $\Delta$. ✓

---

### Problem 6: V-Number and Mode Classification

**Problem:** A fiber has core radius $a = 25$ μm, $NA = 0.22$, and operates at $\lambda = 850$ nm.
(a) Calculate the V-number
(b) Determine if it is single-mode or multi-mode
(c) Estimate the number of guided modes
(d) What core radius would make this fiber single-mode at 850 nm?

**Solution:**

**(a) V-number:**

$$V = \frac{2\pi a}{\lambda} \cdot NA = \frac{2\pi \times 25 \times 10^{-6}}{850 \times 10^{-9}} \times 0.22$$

$$V = \frac{2\pi \times 25 \times 10^{-6}}{0.85 \times 10^{-6}} \times 0.22$$

$$V = \frac{157.08 \times 10^{-6}}{0.85 \times 10^{-6}} \times 0.22$$

$$V = 184.8 \times 0.22$$

$$\boxed{V = 40.66}$$

**(b) Classification:**

Since $V = 40.66 > 2.405$, this is a **multi-mode** fiber.

**(c) Number of guided modes:**

$$M \approx \frac{V^2}{2} = \frac{(40.66)^2}{2} = \frac{1653.2}{2}$$

$$\boxed{M \approx 827 \text{ modes}}$$

**(d) Core radius for single-mode at 850 nm:**

For single-mode: $V < 2.405$

$$\frac{2\pi a}{\lambda} \cdot NA < 2.405$$

$$a < \frac{2.405 \cdot \lambda}{2\pi \cdot NA} = \frac{2.405 \times 850 \times 10^{-9}}{2\pi \times 0.22}$$

$$a < \frac{2.044 \times 10^{-6}}{1.382}$$

$$\boxed{a < 1.48 \text{ μm} \quad \Rightarrow \quad \text{Core diameter} < 2.96 \text{ μm}}$$

This is impractically small — this is why single-mode fibers operate at longer wavelengths (1310/1550 nm) or use smaller NA.

---

### Problem 7: Attenuation — Power Loss Calculations

**Problem:** A fiber optic link has the following specifications:
- Transmitter power: $P_{tx} = 0$ dBm (1 mW)
- Fiber attenuation: 0.35 dB/km at 1310 nm
- Fiber length: 40 km
- 4 splices at 0.1 dB each
- 2 connectors at 0.5 dB each
- Safety margin: 3 dB

Calculate:
(a) The received power in dBm and in mW
(b) The maximum link length if receiver sensitivity is -28 dBm
(c) The fraction of power lost

**Solution:**

**(a) Received power:**

$$P_{rx} = P_{tx} - \alpha L - L_{splices} - L_{connectors} - M_{margin}$$

$$P_{rx} = 0 - (0.35 \times 40) - (4 \times 0.1) - (2 \times 0.5) - 3$$

$$P_{rx} = 0 - 14.0 - 0.4 - 1.0 - 3.0$$

$$\boxed{P_{rx} = -18.4 \text{ dBm}}$$

Convert to mW:

$$P_{rx} = 10^{-18.4/10} = 10^{-1.84} = 0.01445 \text{ mW}$$

$$\boxed{P_{rx} = 14.45 \text{ μW}}$$

**(b) Maximum link length:**

Set $P_{rx} = -28$ dBm and solve for $L$:

$$-28 = 0 - 0.35L - 0.4 - 1.0 - 3.0$$

$$-28 = -0.35L - 4.4$$

$$0.35L = 28 - 4.4 = 23.6$$

$$\boxed{L_{max} = 67.4 \text{ km}}$$

**(c) Fraction of power lost:**

$$\text{Total loss} = 18.4 \text{ dB}$$

$$\frac{P_{in}}{P_{out}} = 10^{18.4/10} = 10^{1.84} = 69.18$$

$$\text{Fraction lost} = 1 - \frac{P_{out}}{P_{in}} = 1 - \frac{1}{69.18} = 1 - 0.01446$$

$$\boxed{\text{Fraction lost} = 98.55\%}$$

Only 1.45% of the input power reaches the receiver!

---

### Problem 8: Dispersion and Bandwidth Calculation

**Problem:** A 50 km fiber optic link uses:
- Step-index multimode fiber
- Core refractive index: $n_1 = 1.48$
- $\Delta = 0.01$
- LED source with spectral width: $\Delta\lambda = 40$ nm at $\lambda = 850$ nm
- Material dispersion: $D_{mat} = 100$ ps/(nm·km) at 850 nm
- Bit rate: 10 Mbps

Calculate:
(a) Intermodal dispersion pulse broadening
(b) Material dispersion pulse broadening
(c) Total dispersion
(d) Maximum achievable bandwidth-distance product
(e) Can this link support 10 Mbps? If not, what is the maximum data rate?

**Solution:**

**(a) Intermodal dispersion:**

$$\Delta t_{IM} = \frac{L \cdot n_1 \cdot \Delta}{c} = \frac{50 \times 10^3 \times 1.48 \times 0.01}{3 \times 10^8}$$

$$\Delta t_{IM} = \frac{740}{3 \times 10^8} = 2.467 \times 10^{-6} \text{ s}$$

$$\boxed{\Delta t_{IM} = 2.467 \text{ μs} = 2467 \text{ ns}}$$

**(b) Material dispersion:**

$$\Delta t_{mat} = D_{mat} \cdot L \cdot \Delta\lambda = 100 \times 50 \times 40$$

$$\boxed{\Delta t_{mat} = 200,000 \text{ ps} = 200 \text{ ns}}$$

**(c) Total dispersion (RSS for independent effects):**

$$\Delta t_{total} = \sqrt{(\Delta t_{IM})^2 + (\Delta t_{mat})^2}$$

$$\Delta t_{total} = \sqrt{(2467)^2 + (200)^2} = \sqrt{6,086,089 + 40,000}$$

$$\Delta t_{total} = \sqrt{6,126,089}$$

$$\boxed{\Delta t_{total} = 2475 \text{ ns} \approx 2.48 \text{ μs}}$$

Note: Intermodal dispersion dominates in step-index multimode fiber.

**(d) Maximum bandwidth-distance product:**

For NRZ signaling, the maximum bit rate is approximately:

$$B_{max} \approx \frac{1}{2 \cdot \Delta t_{total}} = \frac{1}{2 \times 2.475 \times 10^{-6}}$$

$$B_{max} = 202 \text{ kbps}$$

$$B \cdot L = 202 \text{ kbps} \times 50 \text{ km} = 10.1 \text{ Mbps·km}$$

$$\boxed{B \cdot L \approx 10 \text{ Mbps·km}}$$

**(e) Link analysis:**

At 10 Mbps, the bit period is $T_b = 1/10^7 = 100$ ns.

The total dispersion is 2475 ns, which is much larger than the bit period (100 ns). The pulses would overlap severely.

**This link CANNOT support 10 Mbps.**

Maximum data rate:

$$B_{max} = \frac{1}{2 \cdot \Delta t_{total}} = \frac{1}{2 \times 2475 \times 10^{-9}}$$

$$\boxed{B_{max} \approx 202 \text{ kbps}}$$

**Solution:** Use graded-index fiber or single-mode fiber, or reduce the distance.

---

### Problem 9: Photodiode Responsivity and Quantum Efficiency

**Problem:** A silicon PIN photodiode has the following specifications:
- Active area diameter: 1 mm
- Operating wavelength: 850 nm
- Responsivity: $R = 0.55$ A/W
- Dark current: 2 nA
- Load resistance: 50 Ω

Calculate:
(a) The quantum efficiency at 850 nm
(b) The photocurrent for an incident power of 10 μW
(c) The signal voltage across the load
(d) The photocurrent at 1550 nm (same quantum efficiency)
(e) The signal-to-noise ratio if thermal noise current = 5 nA

**Solution:**

**(a) Quantum efficiency:**

$$\eta = \frac{R \cdot hc}{e\lambda} = \frac{R \cdot 1240 \text{ (eV·nm)}}{\lambda \text{ (nm)}}$$

$$\eta = \frac{0.55 \times 1240}{850} = \frac{682}{850}$$

$$\boxed{\eta = 0.802 = 80.2\%}$$

**(b) Photocurrent for $P_{opt} = 10$ μW:**

$$I_{ph} = R \cdot P_{opt} = 0.55 \times 10 \times 10^{-6}$$

$$\boxed{I_{ph} = 5.5 \text{ μA}}$$

**(c) Signal voltage:**

$$V_{signal} = I_{ph} \cdot R_L = 5.5 \times 10^{-6} \times 50$$

$$\boxed{V_{signal} = 275 \text{ μV}}$$

**(d) Photocurrent at 1550 nm:**

Using the same quantum efficiency:

$$R_{1550} = \frac{\eta \cdot e \cdot \lambda}{hc} = \frac{\eta \cdot \lambda}{1240} = \frac{0.802 \times 1550}{1240}$$

$$R_{1550} = \frac{1243.1}{1240}$$

$$\boxed{R_{1550} = 1.003 \text{ A/W}}$$

$$I_{ph} = 1.003 \times 10 \times 10^{-6} = 10.03 \text{ μA}$$

**Note:** Responsivity increases with wavelength for the same quantum efficiency because $\eta$ is the fraction of photons that create carriers, and lower energy photons (longer wavelength) mean more photons per watt.

**(e) Signal-to-noise ratio:**

$$SNR = \frac{I_{ph}}{\sqrt{I_{dark}^2 + I_{thermal}^2}} = \frac{5500 \text{ nA}}{\sqrt{(2)^2 + (5)^2} \text{ nA}}$$

$$SNR = \frac{5500}{\sqrt{4 + 25}} = \frac{5500}{\sqrt{29}} = \frac{5500}{5.385}$$

$$\boxed{SNR = 1021 \quad (30.1 \text{ dB})}$$

---

### Problem 10: Link Budget Analysis

**Problem:** Design a fiber optic link between two buildings 25 km apart. The specifications are:

**Transmitter:**
- DFB laser at 1550 nm
- Output power: $P_{tx} = +3$ dBm (2 mW)

**Fiber:**
- Single-mode, $\alpha = 0.2$ dB/km at 1550 nm

**Splices:**
- 6 fusion splices at 0.05 dB each

**Connectors:**
- 2 pairs (4 connectors) at 0.3 dB each

**Receiver:**
- APD with sensitivity: $P_{sens} = -32$ dBm at 1 Gbps

**Margin:**
- System margin: 3 dB (aging, repairs, temperature)

Calculate:
(a) Total link loss
(b) Received power
(c) System margin (difference between received power and sensitivity)
(d) Maximum additional fiber length possible

**Solution:**

**(a) Total link loss:**

$$L_{fiber} = 0.2 \times 25 = 5.0 \text{ dB}$$

$$L_{splices} = 6 \times 0.05 = 0.3 \text{ dB}$$

$$L_{connectors} = 4 \times 0.3 = 1.2 \text{ dB}$$

$$L_{system} = 3.0 \text{ dB}$$

$$L_{total} = 5.0 + 0.3 + 1.2 + 3.0$$

$$\boxed{L_{total} = 9.5 \text{ dB}}$$

**(b) Received power:**

$$P_{rx} = P_{tx} - L_{total} = 3.0 - 9.5$$

$$\boxed{P_{rx} = -6.5 \text{ dBm}}$$

Convert to mW: $P_{rx} = 10^{-0.65} = 0.224$ mW = 224 μW

**(c) System margin:**

$$M_{sys} = P_{rx} - P_{sens} = -6.5 - (-32)$$

$$\boxed{M_{sys} = 25.5 \text{ dB}}$$

This is an excellent margin — the link has 25.5 dB of spare capacity.

**(d) Maximum additional fiber length:**

Available margin: 25.5 dB

$$L_{additional} = \frac{M_{sys}}{\alpha} = \frac{25.5}{0.2}$$

$$\boxed{L_{additional} = 127.5 \text{ km}}$$

The link could be extended to $25 + 127.5 = 152.5$ km before requiring amplification.

---

### Problem 11: Three-Level vs Four-Level Laser Pump Efficiency

**Problem:** A three-level laser (like Ruby) and a four-level laser (like Nd:YAG) both have:
- Total number of active atoms: $N_t = 10^{20}$ in the gain volume
- Metastable lifetime: $\tau = 200$ μs

The three-level laser needs $N_2 > N_t/2$ for population inversion.
The four-level laser needs $N_2 > 0$ (any population in upper level creates inversion).

Calculate the minimum energy that must be stored in the excited state for each case, if the pump photon energy is 2.0 eV.

**Solution:**

**Three-level laser:**

$$N_{2,min} = \frac{N_t}{2} = \frac{10^{20}}{2} = 5 \times 10^{19}$$

Energy stored:

$$E_{stored} = N_{2,min} \times E_{pump} = 5 \times 10^{19} \times 2.0 \text{ eV} \times 1.6 \times 10^{-19} \text{ J/eV}$$

$$E_{stored} = 5 \times 10^{19} \times 3.2 \times 10^{-19}$$

$$\boxed{E_{stored,3-level} = 16 \text{ J}}$$

**Four-level laser:**

The minimum inversion is $N_{2,min} \approx 0^+$, but practically we need $N_2$ enough to overcome the threshold gain.

Let's say the threshold requires $N_2 = 10^{16}$ atoms (typical):

$$E_{stored} = 10^{16} \times 3.2 \times 10^{-19}$$

$$\boxed{E_{stored,4-level} = 3.2 \times 10^{-3} \text{ J} = 3.2 \text{ mJ}}$$

**Ratio:** The three-level laser needs $5000\times$ more energy to achieve inversion!

This explains why three-level lasers typically require pulsed operation while four-level lasers can operate CW.

---

### Problem 12: Graded-Index Fiber Improvement

**Problem:** A step-index multimode fiber has:
- $n_1 = 1.48$, $\Delta = 0.01$, $L = 10$ km
- Intermodal dispersion: $\Delta t_{SI}$

A graded-index fiber with the same parameters but parabolic profile ($\alpha = 2$) is used instead.

(a) Calculate the improvement in pulse broadening
(b) Calculate the new maximum bandwidth

**Solution:**

**(a) Pulse broadening comparison:**

Step-index:

$$\Delta t_{SI} = \frac{L \cdot n_1 \cdot \Delta}{c} = \frac{10^4 \times 1.48 \times 0.01}{3 \times 10^8}$$

$$\Delta t_{SI} = \frac{148}{3 \times 10^8} = 4.93 \times 10^{-7} \text{ s} = 493 \text{ ns}$$

Graded-index (parabolic):

$$\Delta t_{GI} = \frac{L \cdot n_1 \cdot \Delta^2}{2c} = \frac{10^4 \times 1.48 \times (0.01)^2}{2 \times 3 \times 10^8}$$

$$\Delta t_{GI} = \frac{10^4 \times 1.48 \times 10^{-4}}{6 \times 10^8} = \frac{1.48}{6 \times 10^8}$$

$$\Delta t_{GI} = 2.47 \times 10^{-9} \text{ s} = 2.47 \text{ ns}$$

**Improvement factor:**

$$\frac{\Delta t_{SI}}{\Delta t_{GI}} = \frac{493}{2.47} = 200$$

$$\boxed{\text{Improvement} = 200\times}$$

**Theoretical improvement factor:** $\frac{2}{\Delta} = \frac{2}{0.01} = 200$ ✓

**(b) New maximum bandwidth:**

$$B_{max} = \frac{1}{2 \cdot \Delta t_{GI}} = \frac{1}{2 \times 2.47 \times 10^{-9}}$$

$$\boxed{B_{max} = 202 \text{ MHz}}$$

Compare to step-index: $B_{SI} = 1/(2 \times 493 \times 10^{-9}) = 1.01$ MHz

The graded-index fiber provides 200× higher bandwidth!

---

### Problem 13: EDFA Gain and Noise Figure

**Problem:** An EDFA has the following specifications:
- Input signal power: $P_{in} = -20$ dBm (10 μW) at 1550 nm
- Pump power: 100 mW at 980 nm
- Small-signal gain: 30 dB
- Gain saturation power (3dB): $P_{sat} = 0$ dBm (1 mW)
- Noise figure: 4 dB

Calculate:
(a) The output signal power for small-signal operation
(b) The output signal power when input is -3 dBm (saturated regime)
(c) The ASE noise power in a 1 nm bandwidth

**Solution:**

**(a) Small-signal output:**

$$G_{dB} = 30 \text{ dB} \implies G_{linear} = 10^{30/10} = 1000$$

$$P_{out} = G \cdot P_{in} = 1000 \times 10 \text{ μW} = 10 \text{ mW}$$

$$P_{out} = 10 \text{ mW} = 10 \text{ dBm}$$

$$\boxed{P_{out} = +10 \text{ dBm} = 10 \text{ mW}}$$

**(b) Saturated output:**

For saturated regime, use the gain saturation formula:

$$G = \frac{G_0}{1 + P_{in}/P_{sat}}$$

where $G_0$ is the small-signal gain.

$$G_0 = 1000, \quad P_{in} = 10^{-3/10} = 0.501 \text{ mW}$$

$$P_{sat} = 1 \text{ mW}$$

$$G = \frac{1000}{1 + 0.501/1} = \frac{1000}{1.501} = 666$$

$$P_{out} = G \cdot P_{in} = 666 \times 0.501 = 333.7 \text{ μW}$$

$$\boxed{P_{out} = -4.77 \text{ dBm} = 334 \text{ μW}}$$

Compare to small-signal extrapolation: $G_0 \cdot P_{in} = 1000 \times 0.501 = 501$ mW (impossible!). Gain saturation limits the output.

**(c) ASE noise power:**

Amplified Spontaneous Emission (ASE) noise in bandwidth $B_o$:

$$P_{ASE} = 2 \cdot n_{sp} \cdot (G - 1) \cdot h\nu \cdot B_o$$

where $n_{sp}$ is the spontaneous emission factor related to noise figure:

$$NF = 2 n_{sp} \quad \Rightarrow \quad n_{sp} = \frac{NF}{2} = \frac{10^{4/10}}{2} = \frac{2.512}{2} = 1.256$$

Convert bandwidth: $B_o = 1 \text{ nm}$ at 1550 nm:

$$B_o = \frac{c \cdot \Delta\lambda}{\lambda^2} = \frac{3 \times 10^8 \times 1 \times 10^{-9}}{(1550 \times 10^{-9})^2} = \frac{0.3}{2.4025 \times 10^{-12}} = 124.9 \text{ GHz}$$

Photon energy: $h\nu = hc/\lambda = 6.626 \times 10^{-34} \times 3 \times 10^8 / 1550 \times 10^{-9} = 1.283 \times 10^{-19}$ J

$$P_{ASE} = 2 \times 1.256 \times (1000 - 1) \times 1.283 \times 10^{-19} \times 124.9 \times 10^9$$

$$P_{ASE} = 2 \times 1.256 \times 999 \times 1.283 \times 10^{-19} \times 1.249 \times 10^{11}$$

$$P_{ASE} = 2509 \times 1.603 \times 10^{-8}$$

$$\boxed{P_{ASE} = 4.02 \times 10^{-5} \text{ W} = 40.2 \text{ μW} = -14.0 \text{ dBm}}$$

---

### Problem 14: Semiconductor Laser Wavelength and Band Gap

**Problem:** Calculate the lasing wavelength for the following semiconductor materials:
(a) GaAs ($E_g = 1.42$ eV)
(b) InP ($E_g = 1.35$ eV)
(c) InGaAsP with $E_g = 0.80$ eV
(d) What band gap is needed for a 1550 nm laser?

**Solution:**

**Formula:** $\lambda = \dfrac{hc}{E_g} = \dfrac{1240 \text{ eV·nm}}{E_g \text{ (eV)}}$

**(a) GaAs:**

$$\lambda = \frac{1240}{1.42} = 873.2 \text{ nm}$$

$$\boxed{\lambda_{GaAs} = 873 \text{ nm (near-infrared)}}$$

**(b) InP:**

$$\lambda = \frac{1240}{1.35} = 918.5 \text{ nm}$$

$$\boxed{\lambda_{InP} = 919 \text{ nm (near-infrared)}}$$

**(c) InGaAsP (0.80 eV):**

$$\lambda = \frac{1240}{0.80} = 1550 \text{ nm}$$

$$\boxed{\lambda_{InGaAsP} = 1550 \text{ nm (C-band telecom)}}$$

This is why InGaAsP is used for 1550 nm telecom lasers!

**(d) Required band gap for 1550 nm:**

$$E_g = \frac{1240}{1550} = 0.80 \text{ eV}$$

$$\boxed{E_g = 0.80 \text{ eV for } \lambda = 1550 \text{ nm}}$$

---

### Problem 15: Optical Power Budget with Amplifiers

**Problem:** A 200 km submarine cable uses:
- Transmitter: $P_{tx} = +17$ dBm (50 mW)
- Fiber: $\alpha = 0.2$ dB/km
- 4 EDFAs equally spaced (50 km apart)
- Each EDFA: Gain = 10 dB, Noise Figure = 5 dB
- Connector pairs at each EDFA station: 1 dB total per station
- Receiver sensitivity: -28 dBm at 10 Gbps

Calculate:
(a) Power at each amplifier input
(b) Power after each amplifier
(c) Accumulated ASE noise after 4 amplifiers
(d) OSNR at the receiver

**Solution:**

**(a) Power at each amplifier input:**

Loss per 50 km span:

$$L_{span} = 0.2 \times 50 + 1.0 = 11.0 \text{ dB}$$

After 1st span: $P_1 = 17 - 11 = +6$ dBm
After 2nd span: $P_2 = 6 + 10 - 11 = +5$ dBm
After 3rd span: $P_3 = 5 + 10 - 11 = +4$ dBm
After 4th span: $P_4 = 4 + 10 - 11 = +3$ dBm

$$\boxed{P_{receiver} = +3 \text{ dBm} = 2.0 \text{ mW}}$$

**Verification:** $P_{rx} = P_{tx} - \alpha L_{total} - L_{connectors} = 17 - 40 - 4 = -27$ dBm without amplifiers. With amplifiers, we recover 40 dB of gain, giving +3 dBm.

**(b) After each amplifier:**

| Location | Input (dBm) | Gain (dB) | Output (dBm) |
|----------|------------|-----------|-------------|
| After 1st span | +6 | 10 | +16 |
| After 2nd span | +5 | 10 | +15 |
| After 3rd span | +4 | 10 | +14 |
| After 4th span | +3 | 10 | +13 |

**(c) Accumulated ASE noise:**

ASE power per amplifier per polarization per unit bandwidth:

$$P_{ASE,1} = 2 \cdot n_{sp} \cdot (G - 1) \cdot h\nu \cdot B_o$$

where $n_{sp} = NF/2 = 10^{5/10}/2 = 3.162/2 = 1.581$

For all 4 amplifiers (ASE accumulates additively):

$$P_{ASE,total} = N_{amp} \times P_{ASE,1} = 4 \times P_{ASE,1}$$

In 0.1 nm bandwidth (12.5 GHz at 1550 nm):

$$P_{ASE,1} = 2 \times 1.581 \times 999 \times 1.283 \times 10^{-19} \times 12.5 \times 10^9$$

$$P_{ASE,1} = 3161 \times 1.604 \times 10^{-9} = 5.07 \times 10^{-6} \text{ W} = -23.0 \text{ dBm}$$

$$P_{ASE,total} = 4 \times 5.07 \times 10^{-6} = 2.03 \times 10^{-5} \text{ W} = -16.9 \text{ dBm}$$

**(d) OSNR at receiver:**

$$OSNR = \frac{P_{signal}}{P_{ASE,total}} = \frac{+3 \text{ dBm}}{-16.9 \text{ dBm}} = 19.9 \text{ dB}$$

$$\boxed{OSNR = 19.9 \text{ dB}}$$

For 10 Gbps, the required OSNR is typically 15-20 dB, so this system is marginally adequate.

---

## 10. Common Mistakes & Traps

### Laser Physics Traps

| # | Mistake | Correct Approach |
|---|---------|-----------------|
| 1 | Assuming two-level systems can lase | A two-level system **cannot** achieve population inversion with optical pumping — need at least 3 levels |
| 2 | Using $B_{12} = B_{21}$ for degenerate levels | For degenerate levels: $g_1 B_{12} = g_2 B_{21}$, not $B_{12} = B_{21}$ |
| 3 | Confusing spontaneous and stimulated emission | Spontaneous = random direction/phase (incoherent); Stimulated = identical copy (coherent) |
| 4 | Forgetting the $8\pi h\nu^3/c^3$ factor in the Einstein relation | $A_{21} = (8\pi h\nu^3/c^3) B_{21}$, not $A_{21} = B_{21}$ |
| 5 | Using $\nu$ instead of $\nu^3$ in the Einstein relation | The relation has $\nu^3$, not $\nu$ |
| 6 | Assuming threshold gain is zero | Threshold gain must overcome **both** distributed loss and mirror transmission loss |

### Fiber Optics Traps

| # | Mistake | Correct Approach |
|---|---------|-----------------|
| 7 | Using $NA = n_1/n_2$ or $NA = (n_1-n_2)/n_1$ | Correct: $NA = \sqrt{n_1^2 - n_2^2}$; the approximation $\Delta \approx (n_1-n_2)/n_1$ is for relative index difference, not NA |
| 8 | Forgetting that $a$ is the **radius**, not diameter | $V = 2\pi a/\lambda \cdot NA$ where $a$ = core radius = diameter/2 |
| 9 | Using V = 2.405 for multi-mode boundary | $V < 2.405$ is single-mode; $V > 2.405$ is multi-mode |
| 10 | Not converting dB/km to linear scale | For calculations involving power ratios, convert: $P_{out} = P_{in} \cdot 10^{-\alpha L/10}$ |
| 11 | Using $\log_{10}$ where $\ln$ is needed (or vice versa) | Attenuation: $\log_{10}$; Einstein relations and gain: $\ln$ |
| 12 | Confusing mode number $q$ with mode order | $q \approx 10^5-10^6$ is the longitudinal mode number; TEM$_{mn}$ are transverse mode indices |

### Numerical Calculation Traps

| # | Mistake | Correct Approach |
|---|---------|-----------------|
| 13 | Using eV for energy in Einstein coefficient calculations | Convert eV to Joules: $E_{Joules} = E_{eV} \times 1.6 \times 10^{-19}$ |
| 14 | Forgetting $h = 6.626 \times 10^{-34}$ J·s (not eV·s) | Planck's constant in SI units is $\times 10^{-34}$ |
| 15 | Using $c = 3 \times 10^8$ m/s without checking units | Ensure $\lambda$ is in meters when using $c$ in m/s |
| 16 | Confusing responsivity (A/W) with quantum efficiency (dimensionless) | $\eta$ is fraction (0 to 1); $R$ has units A/W; they are related by $R = \eta e\lambda/(hc)$ |
| 17 | Using $P_{dBm} = 10 \log_{10}(P_{W})$ | Correct: $P_{dBm} = 10 \log_{10}(P_{mW}) = 10 \log_{10}(P_{W}/10^{-3})$ |

### Quick Sanity Checks

- **NA must be between 0 and 1** (for fibers in air)
- **V-number for single-mode is typically 1-2.4** (at operating wavelength)
- **Attenuation at 1550 nm should be ~0.2 dB/km** for standard SMF
- **Laser threshold current is typically mA to A** (not μA)
- **Photodiode responsivity is typically 0.3-1.0 A/W** in the near-IR
- **Quantum efficiency must be between 0 and 1** (0% to 100%)
- **Q-factor > 6 for BER < 10⁻⁹**

---

## 11. Key Formulas Quick Reference

### Laser Physics

| Topic | Formula | Units |
|-------|---------|-------|
| Einstein A/B relation | $A_{21} = \dfrac{8\pi h\nu^3}{c^3} B_{21}$ | s⁻¹ vs m³/J·s² |
| Einstein B relation | $g_1 B_{12} = g_2 B_{21}$ | m³/J·s² |
| Population inversion | $N_2 > N_1$ | m⁻³ |
| Gain coefficient | $g = \dfrac{(N_2-N_1)c^2 A_{21}}{8\pi\nu^2}$ | m⁻¹ |
| Amplified intensity | $I = I_0 e^{gl}$ | W/m² |
| Threshold gain | $g_{th} = \alpha + \dfrac{1}{2l}\ln\left(\dfrac{1}{R_1 R_2}\right)$ | m⁻¹ |
| Mode spacing | $\Delta\nu = \dfrac{c}{2L}$ | Hz |
| Mode frequency | $\nu_q = q \cdot \dfrac{c}{2L}$ | Hz |
| Coherence length | $l_c = \dfrac{c}{\Delta\nu} = \dfrac{\lambda^2}{\Delta\lambda}$ | m |
| Resonator stability | $0 \leq g_1 g_2 \leq 1$ | dimensionless |

### Fiber Optics

| Topic | Formula | Units |
|-------|---------|-------|
| Critical angle | $\theta_c = \sin^{-1}(n_2/n_1)$ | degrees |
| Numerical aperture | $NA = \sqrt{n_1^2 - n_2^2}$ | dimensionless |
| Acceptance angle | $\theta_a = \sin^{-1}(NA)$ | degrees |
| Relative index difference | $\Delta = (n_1^2 - n_2^2)/(2n_1^2) \approx (n_1 - n_2)/n_1$ | dimensionless |
| V-number | $V = (2\pi a/\lambda) \cdot NA$ | dimensionless |
| Single-mode condition | $V < 2.405$ | — |
| Number of modes | $M \approx V^2/2$ (step-index) | — |
| Attenuation (dB/km) | $\alpha = (10/L)\log_{10}(P_{in}/P_{out})$ | dB/km |
| Power after fiber | $P_{out} = P_{in} \cdot 10^{-\alpha L/10}$ | W |
| Intermodal dispersion (SI) | $\Delta t = L \cdot n_1 \cdot \Delta / c$ | s |
| Intermodal dispersion (GI) | $\Delta t = L \cdot n_1 \cdot \Delta^2 / (2c)$ | s |
| Material dispersion | $\Delta t = D \cdot L \cdot \Delta\lambda$ | s |
| Bandwidth-distance | $B \cdot L = 1/(2\Delta t)$ | bps·km |
| Link budget | $P_{rx} = P_{tx} - \alpha L - L_{losses}$ | dBm |

### Optoelectronic Devices

| Topic | Formula | Units |
|-------|---------|-------|
| Photodiode responsivity | $R = I_{ph}/P_{opt} = \eta e\lambda/(hc)$ | A/W |
| Quantum efficiency | $\eta = R \cdot hc/(e\lambda) = R \cdot 1240/\lambda_{nm}$ | dimensionless |
| Solar cell $V_{oc}$ | $V_{oc} = V_T \ln(I_L/I_0 + 1)$ | V |
| Fill factor | $FF = P_{max}/(V_{oc} \cdot I_{sc})$ | dimensionless |
| Band gap ↔ wavelength | $\lambda = 1240/E_g$ | nm ↔ eV |
| Power conversion | $P_{dBm} = 10\log_{10}(P_{mW})$ | dBm |
| Gain in dB | $G_{dB} = 10\log_{10}(G_{linear})$ | dB |

### Numerical Constants

| Constant | Value | Units |
|----------|-------|-------|
| Planck's constant $h$ | $6.626 \times 10^{-34}$ | J·s |
| Speed of light $c$ | $2.998 \times 10^8$ | m/s |
| Electron charge $e$ | $1.602 \times 10^{-19}$ | C |
| Boltzmann constant $k_B$ | $1.381 \times 10^{-23}$ | J/K |
| Thermal voltage $V_T$ | 25.85 mV (at 300 K) | V |
| $hc$ | $1.986 \times 10^{-25}$ | J·m |
| $hc/e$ | 1240 eV·nm | — |
| $hc$ in eV·nm | 1240 | eV·nm |

---

## Cross-References

- [[engineering-physics/module-1-optics-interference-diffraction|Module 1: Interference & Diffraction]] — Fabry-Pérot etalon theory, diffraction grating resolution, coherence requirements for laser cavities
- [[engineering-physics/module-3-quantum-mechanics|Module 3: Quantum Mechanics]] — Stimulated emission is a quantum process; Einstein A/B coefficients from quantum transition rates; energy levels
- [[engineering-physics/module-4-semiconductors-electromagnetism|Module 4: Semiconductors & Electromagnetism]] — p-n junction physics for semiconductor lasers and photodiodes; band gap determines emission wavelength; Maxwell's equations for waveguides

---

*Module 2 of 4 — [[engineering-physics/module-1-optics-interference-diffraction|← Module 1]] | [[engineering-physics/module-3-quantum-mechanics|Module 3 →]] | [[engineering-physics/module-4-semiconductors-electromagnetism|Module 4 →]]*

## Summary Flowchart: Complete Optoelectronics Decision Process

```
    ┌─────────────────────────────────────────────────────────────┐
    │                    OPTOELECTRONICS SYSTEM                    │
    └─────────────────────┬───────────────────────────────────────┘
                          │
         ┌────────────────┼────────────────┐
         │                │                │
    ┌────▼────┐     ┌─────▼─────┐    ┌────▼────┐
    │ SOURCE  │     │ MEDIUM    │    │DETECTOR │
    │ (LED or │     │ (Fiber/   │    │(PIN/APD │
    │  Laser) │     │  Free     │    │Photodiode│
    │         │     │  Space)   │    │         │
    └────┬────┘     └─────┬─────┘    └────┬────┘
         │                │                │
    ┌────▼────┐     ┌─────▼─────┐    ┌────▼────┐
    │ Key:    │     │ Key:      │    │ Key:    │
    │Einstein │     │NA, V-num, │    │R=ηeλ/hc│
    │A,B coeff│     │attenuation│    │η=hcR/eλ │
    │Threshold│     │dispersion │    │SNR calc │
    │condition│     │link budget│    │Bandwidth│
    └─────────┘     └───────────┘    └─────────┘
```

---

*Last updated: 2026-08-17*

## Related Revision
- [[thin-film-interference-revision]] — companion exam-revision sheet for interference/thin-film problems
