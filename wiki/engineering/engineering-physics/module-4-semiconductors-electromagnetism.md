---
module: "engineering-physics"
topic: "Module 4: Semiconductors & Electromagnetism — Complete Reference"
tags: [semiconductors, electrodynamics, maxwell-equations, em-waves, p-n-junction, transistors, fermi-level, carrier-transport, radiation-pressure, brewster-angle]
last_updated: "2026-08-17"
prerequisites: ["Quantum Mechanics Basics", "Current Electricity", "Electrostatics"]
---

# Module 4: Semiconductors & Electromagnetism — Complete Reference

> Two pillars of modern technology: how we control electrical carriers in solids,
> and how changing electric and magnetic fields create light itself.

---

# PART A: SEMICONDUCTORS

---

## 1. Energy Bands in Solids

### 1.1 From Atoms to Bands

When atoms are far apart, each has discrete energy levels. As atoms are brought together to form a crystal:

- Each discrete atomic energy level **splits** into $N$ closely spaced levels (where $N$ is the number of atoms)
- With $N \sim 10^{23}$, the spacing between levels is $\sim 10^{-23}$ eV — far too small to resolve
- What were discrete levels become **continuous bands** of allowed energies
- Between bands, there are **forbidden gaps** where no electron states exist

**Band structure (from lowest to highest energy):**

1. **Core bands:** Deep-lying, tightly bound electrons that do not participate in conduction
2. **Valence band (VB):** Highest occupied band at $T = 0$ K — filled with bonding electrons
3. **Band gap ($E_g$):** Forbidden energy region between VB and CB — no electron states exist here
4. **Conduction band (CB):** Lowest unoccupied band at $T = 0$ K — electrons here are free to conduct

### 1.2 Classification of Solids

```
+=====================================================================+
|              CLASSIFICATION OF SOLIDS BY BAND GAP                    |
+=====================================================================+
|                                                                     |
|  CONDUCTORS              SEMICONDUCTORS          INSULATORS          |
|  ==========              ================          ===========         |
|                                                                     |
|  +-----------+           +-----------+           +-----------+       |
|  | CB        |           | CB        |           | CB        |       |
|  |///////////|  < 1eV    |///////////|  > 3 eV   |///////////|       |
|  |///////////|           |///////////|           |///////////|       |
|  |///////////|           +-----------+           +-----------+       |
|  +-----------+           |   GAP     |           |   GAP     |       |
|  (Overlapping            |  (small)  |           |  (large)  |       |
|   or zero gap)           +-----------+           +-----------+       |
|                          |///////////|           |///////////|       |
|                          | VB        |           | VB        |       |
|                          +-----------+           +-----------+       |
|                                                                     |
|  sigma ~ 10^7 S/m     sigma ~ 10^-6 to 10^4   sigma < 10^-10 S/m  |
|  Temp coeff: +          Temp coeff: -            Temp coeff: +       |
|  Examples: Cu, Ag, Au   Si(1.1eV),Ge(0.67eV)   Diamond(5.5eV)     |
|                          GaAs(1.42eV)            SiO2(9eV)           |
+=====================================================================+
```

### 1.3 Tight-Binding Model

For a hydrogen molecule (2 atoms):

- **Bonding state** (lower energy): symmetric wave function $\psi_+ = \phi_A + \phi_B$
- **Anti-bonding state** (higher energy): antisymmetric wave function $\psi_- = \phi_A - \phi_B$
- Energy splitting: $\Delta E = 2|J|$ where $J$ is the overlap integral

For $N$ atoms, each state splits into $N$ levels. The **bandwidth** increases with:

- Decreasing interatomic spacing
- Increasing overlap of wave functions (greater $J$)

### 1.4 Effective Mass

Electrons in a crystal do not behave as free particles. We define an **effective mass** $m^*$:

$$m^* = \frac{\hbar^2}{d^2E/dk^2}$$

- Near the **bottom** of the CB: $m^* > 0$ (electron-like, behaves like a free particle)
- Near the **top** of the VB: $m^* < 0$ (hole-like, treated as a positive effective mass particle)
- Typical values: $m_e^* \approx 0.26 m_0$ (Si), $m_h^* \approx 0.39 m_0$ (Si)

---

## 2. Intrinsic Semiconductors

### 2.1 Pure Semiconductor — No Doping

At $T = 0$ K:

- Valence band is **completely full**
- Conduction band is **completely empty**
- The semiconductor acts as a perfect **insulator**

At $T > 0$ K:

- Thermal energy $kT$ excites some electrons across the band gap
- Each excited electron leaves behind a **hole** (missing electron in VB)
- Both electrons (in CB) and holes (in VB) are mobile charge carriers
- An electron-hole pair is created; they can also recombine

### 2.2 Carrier Concentrations — Intrinsic

**Mass action law:**

$$\boxed{n_e \cdot n_h = n_i^2}$$

where $n_e$ = electron concentration (cm⁻³), $n_h$ = hole concentration (cm⁻³), $n_i$ = intrinsic carrier concentration.

**Temperature dependence:**

$$\boxed{n_i = \sqrt{N_c N_v} \; e^{-E_g/(2kT)} \propto T^{3/2} e^{-E_g/(2kT)}}$$

where:

$$N_c = 2\left(\frac{2\pi m_e^* kT}{h^2}\right)^{3/2}, \quad N_v = 2\left(\frac{2\pi m_h^* kT}{h^2}\right)^{3/2}$$

are the effective densities of states in the conduction and valence bands.

**Numerical values at $T = 300$ K ($kT \approx 0.0259$ eV):**

| Material | $n_i$ (cm⁻³) | $E_g$ (eV) | Band Type |
|----------|---------------|-------------|-----------|
| Si | $1.5 \times 10^{10}$ | 1.12 | Indirect |
| Ge | $2.4 \times 10^{13}$ | 0.67 | Direct |
| GaAs | $1.8 \times 10^{6}$ | 1.42 | Direct |
| InSb | $1.6 \times 10^{17}$ | 0.17 | Direct |
| GaN | $1.9 \times 10^{-10}$ | 3.4 | Direct |

### 2.3 Conductivity and Resistivity

$$\boxed{\sigma = e(n_e \mu_e + n_h \mu_h)}$$

where $\mu_e, \mu_h$ are electron and hole mobilities (cm²/V·s), and $e = 1.6 \times 10^{-19}$ C.

**For intrinsic semiconductor:** $n_e = n_h = n_i$

$$\sigma_i = n_i e (\mu_e + \mu_h)$$

**Resistivity:**

$$\rho = \frac{1}{\sigma}$$

**Temperature dependence of resistivity:**

$$\rho \propto e^{E_g/(2kT)}$$

Resistivity **decreases** with temperature — opposite to metals.

### 2.4 Typical Mobility Values

| Material | $\mu_e$ (cm²/V·s) | $\mu_h$ (cm²/V·s) | $\sigma_i$ (S/m) |
|----------|--------------------|--------------------|-------------------|
| Si | 1350 | 480 | $4.35 \times 10^{-4}$ |
| Ge | 3900 | 1900 | 2.2 |
| GaAs | 8500 | 400 | $1.0 \times 10^{-6}$ |
| InSb | 78000 | 1200 | $2.6 \times 10^{4}$ |

### 2.5 Fermi Level in Intrinsic Semiconductor

The **Fermi level** $E_F$ is the energy at which the probability of occupation is exactly 1/2.

$$\boxed{E_F = \frac{E_c + E_v}{2} + \frac{3}{4}kT \ln\left(\frac{m_h^*}{m_e^*}\right)}$$

When $m_e^* = m_h^*$, $E_F$ sits **exactly at mid-gap**: $E_F = (E_c + E_v)/2$.

When $m_e^* < m_h^*$ (most common), the Fermi level is slightly **above** mid-gap.

---

## 3. Extrinsic Semiconductors (Doping)

### 3.1 Semiconductor Classification Flowchart

```
+=====================================================================+
|            SEMICONDUCTOR CLASSIFICATION FLOWCHART                    |
+=====================================================================+
|                                                                     |
|                    +-----------------+                               |
|                    |   SEMICONDUCTOR |                               |
|                    |   (Eg ~ 0.1-3 eV)|                              |
|                    +--------+--------+                               |
|                             |                                        |
|              +--------------+--------------+                         |
|              |                             |                         |
|     +--------v--------+          +--------v--------+                |
|     |    INTRINSIC    |          |    EXTRINSIC    |                |
|     |  (No dopants)   |          |   (Doped)       |                |
|     |  n_e = n_h = n_i|          +--------+--------+                |
|     +-----------------+                   |                          |
|                              +------------+------------+            |
|                              |                         |            |
|                    +---------v---------+    +----------v--------+   |
|                    |     n-TYPE        |    |     p-TYPE        |   |
|                    |  Pentavalent dopant|   |  Trivalent dopant  |   |
|                    |  (P, As, Sb)       |   |  (B, Ga, In)       |   |
|                    |  Donates e-        |   |  Accepts e-        |   |
|                    |  n_e >> n_h        |   |  n_h >> n_e        |   |
|                    |  Majority: e-      |   |  Majority: holes   |   |
|                    |  Minority: holes   |   |  Minority: e-      |   |
|                    |  Ef near CB        |   |  Ef near VB        |   |
|                    +--------------------+   +--------------------+   |
+=====================================================================+
```

### 3.2 n-Type Semiconductor

**Dopant:** Pentavalent atom (P, As, Sb) — has 5 valence electrons

- 4 electrons form covalent bonds with neighboring Si atoms
- The 5th electron is loosely bound and easily ionized (~0.045 eV)
- At room temperature, virtually all donors are ionized

**Energy level:** Donor level $E_d$ sits just below conduction band:

$$E_c - E_d \approx 0.045 \text{ eV (for P in Si)}$$

**Carrier concentrations (at room temperature, complete ionization):**

$$n_e \approx N_D \gg n_h$$

$$n_h = \frac{n_i^2}{N_D}$$

**Fermi level:**

$$\boxed{E_F = E_c - kT \ln\left(\frac{N_c}{N_D}\right)}$$

As $N_D$ increases, $E_F$ moves **closer to the conduction band**.

### 3.3 p-Type Semiconductor

**Dopant:** Trivalent atom (B, Ga, In) — has 3 valence electrons

- 3 electrons form covalent bonds; one bond is incomplete → hole
- An electron from a neighboring atom fills this hole, creating a mobile hole
- At room temperature, virtually all acceptors are ionized

**Energy level:** Acceptor level $E_a$ sits just above valence band:

$$E_a - E_v \approx 0.045 \text{ eV (for B in Si)}$$

**Carrier concentrations:**

$$n_h \approx N_A \gg n_e$$

$$n_e = \frac{n_i^2}{N_A}$$

**Fermi level:**

$$\boxed{E_F = E_v + kT \ln\left(\frac{N_v}{N_A}\right)}$$

As $N_A$ increases, $E_F$ moves **closer to the valence band**.

### 3.4 Compensation Doping

When both donors ($N_D$) and acceptors ($N_A$) are present simultaneously:

- If $N_D > N_A$: material is **n-type**, effective $n_e \approx N_D - N_A$
- If $N_A > N_D$: material is **p-type**, effective $n_h \approx N_A - N_D$
- If $N_A = N_D$: material is **compensated** (intrinsic-like), $n_e = n_h = n_i$

### 3.5 Fermi Level Shift Summary

| Doping Condition | Fermi Level Position |
|-----------------|---------------------|
| Intrinsic ($N_A = N_D = 0$) | Mid-gap |
| Lightly n-type ($N_D \sim 10^{14}$) | Slightly above mid-gap |
| Moderately n-type ($N_D \sim 10^{16}$) | ~0.2 eV below $E_c$ |
| Heavily n-type ($N_D \sim 10^{18}$) | Very close to $E_c$ |
| Lightly p-type ($N_A \sim 10^{14}$) | Slightly below mid-gap |
| Moderately p-type ($N_A \sim 10^{16}$) | ~0.2 eV above $E_v$ |
| Heavily p-type ($N_A \sim 10^{18}$) | Very close to $E_v$ |

---

## 4. Carrier Transport: Drift and Diffusion

### 4.1 Drift Current

Carriers move under an applied electric field $\vec{E}$:

**Drift velocity:**

$$\vec{v}_d = \mu \vec{E}$$

This is valid for **low fields** ($E < 10^4$ V/cm). At high fields, velocity **saturates**:

$$v_{sat} \approx 10^7 \text{ cm/s (for Si)}$$

**Drift current density:**

$$\boxed{J_{drift} = \sigma E = e(n_e \mu_e + n_h \mu_h)E}$$

**Ohm's law in differential form:** $J = \sigma E$

### 4.2 Diffusion Current

Carriers move from regions of **high concentration** to **low concentration** (Fick's first law):

**Diffusion current density:**

$$\boxed{J_{diff} = eD_e \frac{dn_e}{dx} - eD_h \frac{dn_h}{dx}}$$

where $D_e, D_h$ are diffusion coefficients (cm²/s).

**Sign convention:** Electrons diffuse from high $n_e$ to low $n_e$, carrying negative charge — this constitutes current in the $-x$ direction for a positive gradient, hence the positive sign. Holes diffuse from high $n_h$ to low $n_h$, carrying positive charge — this constitutes current in the $-x$ direction for a positive gradient, hence the negative sign.

### 4.3 Einstein Relation

$$\boxed{\frac{D}{\mu} = \frac{kT}{e} = V_T \approx 0.0259 \text{ V at 300 K}}$$

This profound relation connects diffusion (random thermal motion) to drift (directed motion in a field) through temperature.

**Example:** If $\mu_e = 1350$ cm²/V·s in Si at 300 K:

$$D_e = \mu_e \times V_T = 1350 \times 0.0259 = 35.0 \text{ cm}^2/\text{s}$$

### 4.4 Total Current Density

$$\boxed{J_{total} = e(n_e \mu_e + n_h \mu_h)E + eD_e \frac{dn_e}{dx} - eD_h \frac{dn_h}{dx}}$$

This is the starting point for deriving the diode equation and other device physics results.

---

## 5. p-n Junction

### 5.1 Formation Process

```
+=====================================================================+
|              P-N JUNCTION FORMATION FLOWCHART                        |
+=====================================================================+
|                                                                     |
|  Step 1: Join p-type and n-type semiconductors                      |
|  +-------------------+   +-------------------+                      |
|  |   p-TYPE          |   |   n-TYPE          |                      |
|  |   (many holes)    |   |   (many e-)       |                      |
|  +-------------------+   +-------------------+                      |
|                    \        /                                        |
|                     \      /                                         |
|                      v    v                                          |
|                                                                     |
|  Step 2: Diffusion across junction                                  |
|  Holes diffuse p -> n     Electrons diffuse n -> p                   |
|                                                                     |
|  Step 3: Depletion region forms                                     |
|  +----+----+-------+-------+----+----+                              |
|  |    | -A |       |       | +D |    |                              |
|  |    | -A |  E -> |       | +D |    |                              |
|  |    | -A |       |       | +D |    |                              |
|  +----+----+-------+-------+----+----+                              |
|  p-side   ionized   gap  ionized  n-side                            |
|           acceptors       donors                                    |
|                                                                     |
|  Step 4: Equilibrium reached                                        |
|  Diffusion current = Drift current                                  |
|  Net current = 0                                                    |
|  Built-in potential V_bi established                                |
|  Built-in electric field E = V_bi / W                               |
+=====================================================================+
```

### 5.2 Built-in Potential

$$\boxed{V_{bi} = \frac{kT}{e} \ln\left(\frac{N_A N_D}{n_i^2}\right) = V_T \ln\left(\frac{N_A N_D}{n_i^2}\right)}$$

**Physical meaning:** The electrostatic potential barrier that develops across the junction, preventing further diffusion of majority carriers in equilibrium.

**Derivation (from carrier statistics):**

At equilibrium, the Fermi level is constant across the junction. Equating the electron concentrations at the junction edges and applying Boltzmann statistics yields the result above.

### 5.3 Depletion Width

$$\boxed{W = \sqrt{\frac{2\epsilon_s (V_{bi} + V_R)}{e}\left(\frac{1}{N_A} + \frac{1}{N_D}\right)}}$$

where:

- $\epsilon_s = \epsilon_r \epsilon_0$ is the semiconductor permittivity
- $V_R$ = reverse bias voltage (positive value)
- For forward bias, replace $V_R$ with $-V_F$
- Width extends $\sim (N_D/N_A)$ times more into the lightly doped side

**Depletion widths on each side:**

$$x_p = \frac{N_D}{N_A + N_D} \cdot W, \qquad x_n = \frac{N_A}{N_A + N_D} \cdot W$$

The depletion extends **more** into the **lightly doped** side.

### 5.4 Forward Bias

```
+=====================================================================+
|              FORWARD BIAS OPERATIONS                                 |
+=====================================================================+
|                                                                     |
|  External voltage V_F applied:                                      |
|  + terminal connected to p-side                                     |
|  - terminal connected to n-side                                     |
|                                                                     |
|  Effect:                                                            |
|  - Reduces the barrier height: effective barrier = V_bi - V_F       |
|  - Current increases exponentially:                                  |
|    I = I_0 * (e^(V_F/V_T) - 1)                                    |
|  - Depletion width decreases                                        |
|  - Majority carriers flow across junction                           |
|  - Small resistance -> easy current flow                            |
|  - Minority carriers are injected and diffuse away                  |
+=====================================================================+
```

**Current equation:**

$$\boxed{I = I_0\left(e^{V_F/V_T} - 1\right) \approx I_0 e^{V_F/V_T} \text{ for } V_F \gg V_T}$$

### 5.5 Reverse Bias

```
+=====================================================================+
|              REVERSE BIAS OPERATIONS                                 |
+=====================================================================+
|                                                                     |
|  External voltage V_R applied:                                      |
|  + terminal connected to n-side                                     |
|  - terminal connected to p-side                                     |
|                                                                     |
|  Effect:                                                            |
|  - Increases the barrier height: effective barrier = V_bi + V_R     |
|  - Current is small and approximately constant: I ~ -I_0            |
|  - I_0 depends on temperature and material: I_0 ~ n_i^2             |
|  - Depletion width increases                                        |
|  - High resistance -> very little current                           |
|  - Only minority carriers flow (saturation current)                 |
+=====================================================================+
```

**Saturation current:**

$$I_0 = eA\left(\frac{D_e n_{p0}}{L_e} + \frac{D_h p_{n0}}{L_h}\right)$$

where $n_{p0}$ and $p_{n0}$ are equilibrium minority carrier concentrations, and $L_e$, $L_h$ are minority carrier diffusion lengths.

### 5.6 I-V Characteristic Curve

```
         I (mA)
         ^
         |              Forward
         |             /
         |            /
         |           /
         |          /
         |         /
---------+----+---/---------------> V (V)
         |    |  /        Breakdown
         |    | /         |
         |    |/          v
         |    |    Reverse (magnified)
         |    |
         |    |
         |
   Note: The reverse current is very small (nA to uA),
   while forward current is large (mA to A).
   Breakdown voltage depends on doping and material.
```

### 5.7 Junction Capacitance

**Transition (depletion) capacitance** — dominant in reverse bias:

$$C_T = \frac{\epsilon_s A}{W} = A\sqrt{\frac{e \epsilon_s}{2(V_{bi}+V_R)} \cdot \frac{N_A N_D}{N_A + N_D}}$$

Note: $C_T \propto (V_{bi} + V_R)^{-1/2}$ — decreases with increasing reverse bias.

**Diffusion capacitance** — dominant in forward bias:

$$C_D = \frac{\tau_F I}{V_T}$$

where $\tau_F$ is the minority carrier lifetime (forward transit time).

### 5.8 Reverse Recovery Time

When switching from forward to reverse bias, the stored minority carriers take time to be removed:

$$t_{rr} \approx \frac{Q_s}{I_R}$$

where $Q_s$ is the stored charge and $I_R$ is the reverse current. This limits the switching speed of diodes.

---

## 6. Semiconductor Devices

### 6.1 p-n Junction Diode Applications

- **Rectification:** Converting AC to DC (half-wave, full-wave, bridge rectifier)
- **Voltage regulation:** Zener diode operates in breakdown region
- **Light emission:** LED (forward bias -> electron-hole recombination -> photon emission)
- **Photodetection:** Photodiode (reverse bias -> absorbed photons create electron-hole pairs)
- **Solar energy conversion:** Solar cell (photovoltaic effect)

### 6.2 Zener Diode

Operates in **reverse breakdown** region with nearly constant voltage:

- **Zener breakdown** ($V_Z < 5$ V): Quantum mechanical tunneling through the thin barrier
  - Negative temperature coefficient (voltage decreases with temperature)
- **Avalanche breakdown** ($V_Z > 5$ V): Impact ionization chain reaction
  - Positive temperature coefficient (voltage increases with temperature)
- At $V_Z \approx 5$ V: both mechanisms contribute, temperature coefficient $\approx 0$

### 6.3 Bipolar Junction Transistor (BJT)

**Structure:** Two p-n junctions sharing a common base region

- **NPN:** n-emitter, p-base, n-collector (more common in ICs)
- **PNP:** p-emitter, n-base, p-collector

**Regions of operation:**

| Region | B-E Junction | B-C Junction | Application |
|--------|-------------|--------------|-------------|
| Active | Forward | Reverse | Amplification |
| Saturation | Forward | Forward | Switch ON |
| Cut-off | Reverse | Reverse | Switch OFF |
| Reverse | Reverse | Forward | (Special use) |

**Current relations:**

$$\boxed{I_E = I_B + I_C}$$

$$\boxed{I_C = \beta I_B} \quad \text{(active region)}$$

$$\boxed{\alpha = \frac{I_C}{I_E}, \qquad \beta = \frac{I_C}{I_B} = \frac{\alpha}{1 - \alpha}}$$

**Inverse relations:**

$$\alpha = \frac{\beta}{1 + \beta}, \qquad I_B = \frac{I_E}{1 + \beta}$$

**Typical values:**

- $\alpha \approx 0.95$ to $0.99$
- $\beta \approx 20$ to $500$
- $\beta$ varies with $I_C$, $V_{CE}$, and temperature

### 6.4 Field Effect Transistor (FET)

**Structure:** Gate, Source, Drain — voltage-controlled device

**Key advantage over BJT:** Very high input impedance (gate draws virtually no current)

**Types:**

- **JFET:** Junction FET (depletion mode only)
  - Gate voltage controls channel width -> controls current
  - Pinch-off voltage $V_P$: channel fully depleted
- **MOSFET:** Metal-Oxide-Semiconductor FET
  - Enhancement mode: no channel at $V_{GS} = 0$, channel forms when $V_{GS} > V_{th}$
  - Depletion mode: channel exists at $V_{GS} = 0$, can be enhanced or depleted

**Transconductance:**

$$g_m = \frac{\partial I_D}{\partial V_{GS}} \bigg|_{V_{DS}=\text{const}}$$

### 6.5 Logic Gates

| Gate | Symbol | Truth Table | Boolean |
|------|--------|-------------|---------|
| AND | $\cdot$ | 1 only if both inputs 1 | $Y = A \cdot B$ |
| OR | $+$ | 1 if any input is 1 | $Y = A + B$ |
| NOT | overbar | Inverts input | $Y = \overline{A}$ |
| NAND | $\overline{\cdot}$ | 0 only if both inputs 1 | $Y = \overline{A \cdot B}$ |
| NOR | $\overline{+}$ | 0 if any input is 1 | $Y = \overline{A + B}$ |
| XOR | $\oplus$ | 1 if inputs differ | $Y = A \oplus B$ |
| XNOR | $\overline{\oplus}$ | 1 if inputs same | $Y = \overline{A \oplus B}$ |

**NAND and NOR are universal gates** — any Boolean function can be implemented using only one type.

---

# PART B: ELECTROMAGNETISM

---

## 7. Maxwell's Equations

### 7.1 The Four Equations — Integral Form

| Law | Equation | Physical Meaning |
|-----|----------|-----------------|
| Gauss (E) | $\oint \vec{E} \cdot d\vec{A} = \frac{Q_{enc}}{\epsilon_0}$ | Electric charges are sources/sinks of E field lines |
| Gauss (B) | $\oint \vec{B} \cdot d\vec{A} = 0$ | No magnetic monopoles — B field lines always close on themselves |
| Faraday | $\oint \vec{E} \cdot d\vec{l} = -\frac{d\Phi_B}{dt}$ | A changing magnetic flux induces an EMF |
| Ampere-Maxwell | $\oint \vec{B} \cdot d\vec{l} = \mu_0 I + \mu_0\epsilon_0 \frac{d\Phi_E}{dt}$ | Currents AND changing E flux create B fields |

### 7.2 Differential Form

$$\nabla \cdot \vec{E} = \frac{\rho}{\epsilon_0}$$

$$\nabla \cdot \vec{B} = 0$$

$$\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$$

$$\nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0\epsilon_0 \frac{\partial \vec{E}}{\partial t}$$

### 7.3 Maxwell's Correction — Displacement Current

The term $\mu_0\epsilon_0 \frac{d\Phi_E}{dt}$ is the **displacement current** $I_d$:

$$I_d = \epsilon_0 \frac{d\Phi_E}{dt}$$

**Why it is needed:** Without it, Ampere's law gives inconsistent results for a charging capacitor — conduction current exists in the wire but not between the plates. The displacement current bridges this gap and ensures the continuity equation is satisfied everywhere.

**Physical meaning:** A changing electric field creates a magnetic field, completing the symmetry with Faraday's law (changing B creates E). This symmetry is the foundation of electromagnetic waves.

### 7.4 Maxwell's Equations in Matter

$$\nabla \cdot \vec{D} = \rho_f$$

$$\nabla \cdot \vec{B} = 0$$

$$\nabla \times \vec{E} = -\frac{\partial \vec{B}}{\partial t}$$

$$\nabla \times \vec{H} = \vec{J}_f + \frac{\partial \vec{D}}{\partial t}$$

where:

$$\vec{D} = \epsilon_0 \vec{E} + \vec{P} = \epsilon \vec{E}, \qquad \vec{H} = \frac{\vec{B}}{\mu_0} - \vec{M} = \frac{\vec{B}}{\mu}$$

---

## 8. Electromagnetic Waves

### 8.1 Derivation of the Wave Equation

```
+=====================================================================+
|         EM WAVE DERIVATION STEPS FLOWCHART                          |
+=====================================================================+
|                                                                     |
|  +---------------------------+                                      |
|  | Start: Maxwell's Eqns     |                                      |
|  | in free space              |                                      |
|  | (rho=0, J=0)              |                                      |
|  +-------------+-------------+                                      |
|                |                                                     |
|                v                                                     |
|  +---------------------------+                                      |
|  | Take curl of Faraday's Eq |                                      |
|  | grad x (grad x E) =       |                                      |
|  |   - d(grad x B)/dt        |                                      |
|  +-------------+-------------+                                      |
|                |                                                     |
|                v                                                     |
|  +---------------------------+                                      |
|  | Apply vector identity:    |                                      |
|  | grad x (grad x E) =       |                                      |
|  |   grad(grad . E) - grad^2E|                                      |
|  +-------------+-------------+                                      |
|                |                                                     |
|                v                                                     |
|  +---------------------------+                                      |
|  | Use free space: grad . E =0|                                     |
|  | -> -grad^2E = -d(grad x B)/dt|                                   |
|  +-------------+-------------+                                      |
|                |                                                     |
|                v                                                     |
|  +---------------------------+                                      |
|  | Substitute Ampere-Maxwell: |                                      |
|  | grad x B = mu0*eps0*dE/dt  |                                     |
|  +-------------+-------------+                                      |
|                |                                                     |
|                v                                                     |
|  +---------------------------+                                      |
|  | FINAL WAVE EQUATION:      |                                      |
|  | grad^2E = mu0*eps0*d2E/dt2 |                                     |
|  +-------------+-------------+                                      |
|                |                                                     |
|                v                                                     |
|  +---------------------------+                                      |
|  | Read off wave speed:      |                                      |
|  | c = 1/sqrt(mu0*eps0)      |                                      |
|  | = 2.998 x 10^8 m/s       |                                      |
|  +---------------------------+                                      |
+=====================================================================+
```

**Step 1:** Take curl of Faraday's law in free space ($\rho = 0$, $\vec{J} = 0$):

$$\nabla \times (\nabla \times \vec{E}) = -\frac{\partial}{\partial t}(\nabla \times \vec{B})$$

**Step 2:** Apply vector identity $\nabla \times (\nabla \times \vec{E}) = \nabla(\nabla \cdot \vec{E}) - \nabla^2 \vec{E}$:

Since $\nabla \cdot \vec{E} = 0$ in free space:

$$-\nabla^2 \vec{E} = -\frac{\partial}{\partial t}(\nabla \times \vec{B})$$

**Step 3:** Substitute Ampere-Maxwell law $\nabla \times \vec{B} = \mu_0\epsilon_0 \frac{\partial \vec{E}}{\partial t}$:

$$-\nabla^2 \vec{E} = -\mu_0\epsilon_0 \frac{\partial^2 \vec{E}}{\partial t^2}$$

$$\boxed{\nabla^2 \vec{E} = \mu_0\epsilon_0 \frac{\partial^2 \vec{E}}{\partial t^2}}$$

This is the **standard wave equation** with wave speed:

$$\boxed{c = \frac{1}{\sqrt{\mu_0\epsilon_0}} = 2.998 \times 10^8 \text{ m/s}}$$

The same procedure for $\vec{B}$ gives:

$$\nabla^2 \vec{B} = \mu_0\epsilon_0 \frac{\partial^2 \vec{B}}{\partial t^2}$$

### 8.2 Plane Wave Solution

$$\vec{E} = E_0 \sin(kx - \omega t)\;\hat{j}$$

$$\vec{B} = B_0 \sin(kx - \omega t)\;\hat{k}$$

**Key relationships:**

- $E_0 = cB_0$ (electric and magnetic amplitudes)
- $k = \omega/c = 2\pi/\lambda$ (wave number)
- $v = f\lambda = \omega/k$

**Properties of EM waves:**

1. $\vec{E} \perp \vec{B} \perp$ propagation direction (transverse waves)
2. $\vec{E}$ and $\vec{B}$ are **in phase** (both peak together)
3. No medium required for propagation
4. In a medium: $v = c/n$ where $n = \sqrt{\mu_r \epsilon_r}$
5. EM waves carry energy and momentum

### 8.3 Energy, Power, and Momentum

**Energy density:**

$$u = \frac{1}{2}\epsilon_0 E^2 + \frac{B^2}{2\mu_0} = \epsilon_0 E^2$$

(The electric and magnetic contributions are equal, each being $u/2$.)

**Poynting vector (power per unit area):**

$$\boxed{\vec{S} = \frac{1}{\mu_0}\vec{E} \times \vec{B}}$$

Direction: points in the direction of wave propagation (energy flow).

**Average intensity:**

$$\boxed{I = \langle S \rangle = \frac{1}{2}\epsilon_0 c E_0^2 = \frac{E_0^2}{2\mu_0 c} = \frac{cB_0^2}{2\mu_0}}$$

**Momentum density:**

$$\vec{g} = \frac{\vec{S}}{c^2}$$

**Radiation pressure:**

$$\boxed{P_{abs} = \frac{I}{c} \quad \text{(perfect absorber)}}$$

$$\boxed{P_{refl} = \frac{2I}{c} \quad \text{(perfect reflector)}}$$

### 8.4 Electromagnetic Spectrum

| Region | Wavelength | Frequency | Production | Detection |
|--------|-----------|-----------|------------|-----------|
| Radio | $> 1$ m | $< 300$ MHz | Oscillating circuits | Antennas |
| Microwave | 1 mm – 1 m | 300 MHz – 300 GHz | Klystron, magnetron | Point-contact diodes |
| Infrared | 700 nm – 1 mm | 300 GHz – 430 THz | Hot objects, LEDs | Thermopiles, photodiodes |
| Visible | 400 – 700 nm | 430 – 750 THz | Incandescent, lasers | Eyes, photodetectors |
| Ultraviolet | 10 – 400 nm | 750 THz – 30 PHz | Hot bodies, arcs | PMTs, CCD |
| X-rays | 0.01 – 10 nm | 30 PHz – 30 EHz | X-ray tubes, synchrotrons | Film, CCD |
| Gamma | $< 0.01$ nm | $> 30$ EHz | Nuclear decay, cosmic | Scintillation counters |

---

## 9. Electromagnetic Waves in Matter

### 9.1 Reflection and Refraction

**Snell's law:**

$$\boxed{n_1 \sin\theta_1 = n_2 \sin\theta_2}$$

**Fresnel equations (normal incidence):**

$$\boxed{r = \frac{n_1 - n_2}{n_1 + n_2}} \quad \text{(amplitude reflection coefficient)}$$

$$\boxed{t = \frac{2n_1}{n_1 + n_2}} \quad \text{(amplitude transmission coefficient)}$$

Note: $r + t = 1$ (conservation of field amplitude at the interface).

**Reflectance and transmittance:**

$$R = r^2 = \left(\frac{n_1 - n_2}{n_1 + n_2}\right)^2, \qquad T = 1 - R$$

**Example:** At an air-glass interface ($n_1 = 1$, $n_2 = 1.5$):

$$R = \left(\frac{1 - 1.5}{1 + 1.5}\right)^2 = \left(\frac{-0.5}{2.5}\right)^2 = 0.04 = 4\%$$

About 4% of light is reflected at normal incidence from glass.

### 9.2 Brewster's Angle

At Brewster's angle $\theta_B$, reflected light is **completely polarized** (s-polarized only):

$$\boxed{\tan\theta_B = \frac{n_2}{n_1}}$$

**Physical meaning:** At this angle, the reflected and refracted rays are perpendicular to each other ($\theta_r + \theta_2 = 90°$). The oscillating dipoles in the second medium radiate along the direction of the would-be reflected ray for p-polarized light, so no p-polarized light is reflected.

### 9.3 Total Internal Reflection (TIR)

```
+=====================================================================+
|         TOTAL INTERNAL REFLECTION DECISION FLOWCHART                 |
+=====================================================================+
|                                                                     |
|  Light traveling from medium 1 to medium 2                          |
|                    |                                                 |
|                    v                                                 |
|  +---------------------------+                                      |
|  | Is n1 > n2?               |                                      |
|  | (denser -> rarer?)        |                                      |
|  +------+------+------+-----+                                      |
|         |             |                                             |
|     YES |         NO  |                                             |
|         v             v                                             |
|  +------+------+  +---+---+                                        |
|  | Is theta_i > |  | TIR  |                                        |
|  | theta_c?     |  | NEVER|                                        |
|  | theta_c =    |  | OCCURS|                                       |
|  | sin^-1(n2/n1)|  +------+                                        |
|  +------+------+                                                    |
|         |                                                           |
|     YES |        NO                                                 |
|         v         v                                                 |
|  +------+------+  +--------+                                       |
|  |    TIR!     |  | Normal |                                       |
|  | Total       |  | refrac-|                                       |
|  | internal    |  | tion   |                                       |
|  | reflection  |  +--------+                                       |
|  | Evanescent  |                                                   |
|  | wave in     |                                                   |
|  | medium 2    |                                                   |
|  +-------------+                                                   |
+=====================================================================+
```

Occurs when light travels from a **denser** to a **rarer** medium at an angle exceeding the **critical angle**:

$$\boxed{\theta_c = \sin^{-1}\left(\frac{n_2}{n_1}\right) \quad (n_1 > n_2)}$$

**Conditions for TIR:**

1. Light must travel from higher-$n$ to lower-$n$ medium ($n_1 > n_2$)
2. Angle of incidence must exceed $\theta_c$

**Evanescent wave:** When TIR occurs, an exponentially decaying field penetrates into the rarer medium:

$$E \propto e^{-\alpha z}$$

where $\alpha = k\sqrt{n_1^2\sin^2\theta - n_2^2}$ and $z$ is the distance into the rarer medium.

**Applications:** Fiber optics, prisms, TIRF microscopy, waveguide coupling, kaleidoscopes.

### 9.4 Dispersion

**Normal dispersion:** $dn/d\lambda < 0$ (refractive index decreases with wavelength — most transparent materials)

**Anomalous dispersion:** $dn/d\lambda > 0$ (near absorption lines)

**Cauchy's equation:**

$$n(\lambda) = A + \frac{B}{\lambda^2} + \frac{C}{\lambda^4}$$

**Sellmeier equation** (more accurate over wide range):

$$n^2(\lambda) = 1 + \sum_i \frac{B_i \lambda^2}{\lambda^2 - C_i}$$

---

## 10. Magnetism in Matter

### 10.1 Classification of Magnetic Materials

| Type | Behavior | $\chi_m$ | $\mu_r$ | Examples |
|------|----------|---------|---------|----------|
| Diamagnetic | Weakly repelled | Small negative ($\sim -10^{-5}$) | $< 1$ | Cu, Ag, Au, H₂O |
| Paramagnetic | Weakly attracted | Small positive ($\sim 10^{-3}$ to $10^{-5}$) | $> 1$ | Al, Pt, O₂ |
| Ferromagnetic | Strongly attracted | Large positive ($\sim 10^{3}$) | $\gg 1$ | Fe, Co, Ni |
| Antiferromagnetic | Weak attraction | Small positive | $\sim 1$ | MnO, Cr |
| Ferrimagnetic | Moderate attraction | Positive | 1 – 1000 | Fe₃O₄, ferrites |

### 10.2 Diamagnetism

- **Origin:** Induced magnetic moment opposes applied field (Lenz's law at atomic level)
- **Susceptibility:** $\chi_D \approx -10^{-5}$ (independent of temperature)
- Present in **all** materials but masked by para/ferromagnetism when present

### 10.3 Paramagnetism

- **Origin:** Permanent magnetic moments partially align with applied field
- **Curie's law:** $\chi_P = \frac{C}{T}$ where $C$ is the Curie constant
- Dominates over diamagnetism when permanent moments exist

### 10.4 Ferromagnetism

- **Origin:** Exchange interaction aligns neighboring spins parallel
- **Curie temperature ($T_C$):** Above this, ferromagnet becomes paramagnetic
  - $T_C$: Fe = 1043 K, Co = 1394 K, Ni = 631 K
- **Hysteresis loop:** Shows memory effect — remanent magnetization persists after field removed

### 10.5 Magnetic Circuits

**Hopkinson's law** (analogous to Ohm's law):

$$\phi = \frac{NI}{\mathcal{R}}$$

where $\phi$ is magnetic flux, $NI$ is magnetomotive force, $\mathcal{R} = l/(\mu A)$ is reluctance.

---

## 11. Complete Formula Reference Table

### Semiconductors

| Topic | Formula | Notes |
|-------|---------|-------|
| Mass action law | $n_e \cdot n_h = n_i^2$ | Always holds in equilibrium |
| Intrinsic carrier conc. | $n_i = \sqrt{N_c N_v}\;e^{-E_g/2kT}$ | Strong $T$ dependence |
| Conductivity | $\sigma = e(n_e\mu_e + n_h\mu_h)$ | Units: S/m |
| Resistivity | $\rho = 1/\sigma$ | Units: Ohm.m |
| Einstein relation | $D/\mu = kT/e = V_T$ | $V_T \approx 0.0259$ V at 300 K |
| Fermi level (intrinsic) | $E_F = \frac{E_c+E_v}{2} + \frac{3}{4}kT\ln\frac{m_h^*}{m_e^*}$ | Mid-gap if $m_e^* = m_h^*$ |
| Fermi level (n-type) | $E_F = E_c - kT\ln(N_c/N_D)$ | Approaches $E_c$ as $N_D$ increases |
| Fermi level (p-type) | $E_F = E_v + kT\ln(N_v/N_A)$ | Approaches $E_v$ as $N_A$ increases |
| Built-in potential | $V_{bi} = V_T \ln(N_A N_D/n_i^2)$ | Barrier at p-n junction |
| Depletion width | $W = \sqrt{\frac{2\epsilon_s(V_{bi}+V_R)}{e}(\frac{1}{N_A}+\frac{1}{N_D})}$ | Increases with $V_R$ |
| Diode current | $I = I_0(e^{V_F/V_T}-1)$ | Shockley equation |
| BJT: $I_E$ relation | $I_E = I_B + I_C$ | Conservation of charge |
| BJT: current gain | $\beta = \alpha/(1-\alpha)$ | Typical: $\alpha \approx 0.99$, $\beta \approx 100$ |

### Electromagnetism

| Topic | Formula | Notes |
|-------|---------|-------|
| Wave speed (vacuum) | $c = 1/\sqrt{\mu_0\epsilon_0}$ | $= 2.998 \times 10^8$ m/s |
| Wave speed (medium) | $v = c/n = 1/\sqrt{\mu\epsilon}$ | $n = \sqrt{\mu_r\epsilon_r}$ |
| Wave relation | $E_0 = cB_0$ | Electric and magnetic amplitudes |
| Energy density | $u = \epsilon_0 E^2$ | Equal E and B contributions |
| Poynting vector | $\vec{S} = \vec{E}\times\vec{B}/\mu_0$ | Power per unit area (W/m^2) |
| Average intensity | $I = \frac{1}{2}\epsilon_0 c E_0^2$ | Time-averaged Poynting vector |
| Radiation pressure | $P = I/c$ (absorbing), $2I/c$ (reflecting) | Force per unit area |
| Snell's law | $n_1\sin\theta_1 = n_2\sin\theta_2$ | Refraction |
| Brewster's angle | $\tan\theta_B = n_2/n_1$ | Polarized reflection |
| Critical angle | $\theta_c = \sin^{-1}(n_2/n_1)$ | Total internal reflection |
| Reflectance | $R = (n_1-n_2)^2/(n_1+n_2)^2$ | Normal incidence |
| Transmittance | $T = 1 - R$ | Normal incidence |
| Curie's law (para) | $\chi = C/T$ | Paramagnetic susceptibility |

---

## 12. Fully Worked Numerical Examples

---

### Example 1: Intrinsic Carrier Concentration

**Problem:** Calculate the intrinsic carrier concentration $n_i$ for silicon at $T = 300$ K given $N_c = 2.8 \times 10^{19}$ cm⁻³, $N_v = 1.04 \times 10^{19}$ cm⁻³, and $E_g = 1.12$ eV.

**Solution:**

$$n_i = \sqrt{N_c N_v}\;e^{-E_g/(2kT)}$$

**Step 1:** Calculate $\sqrt{N_c N_v}$:

$$\sqrt{N_c N_v} = \sqrt{(2.8 \times 10^{19})(1.04 \times 10^{19})}$$

$$= \sqrt{2.912 \times 10^{38}}$$

$$= 1.706 \times 10^{19} \text{ cm}^{-3}$$

**Step 2:** Calculate $E_g/(2kT)$:

$$\frac{E_g}{2kT} = \frac{1.12}{2 \times 0.0259} = \frac{1.12}{0.0518} = 21.62$$

**Step 3:** Calculate exponential:

$$e^{-21.62} = 4.07 \times 10^{-10}$$

**Step 4:** Final answer:

$$\boxed{n_i = 1.706 \times 10^{19} \times 4.07 \times 10^{-10} = 6.94 \times 10^{9} \text{ cm}^{-3}}$$

This is close to the commonly cited value of $1.5 \times 10^{10}$ cm⁻³ (differences arise from slightly different effective masses used in $N_c$, $N_v$).

---

### Example 2: Conductivity with Doping

**Problem:** A silicon sample is doped with $N_D = 5 \times 10^{16}$ cm⁻³ phosphorus atoms. Given $\mu_e = 1350$ cm²/V·s, $\mu_h = 480$ cm²/V·s, $n_i = 1.5 \times 10^{10}$ cm⁻³, find the conductivity.

**Solution:**

Since $N_D \gg n_i$, this is **n-type** with:

$$n_e \approx N_D = 5 \times 10^{16} \text{ cm}^{-3}$$

**Step 1:** Find hole concentration using mass action law:

$$n_h = \frac{n_i^2}{N_D} = \frac{(1.5 \times 10^{10})^2}{5 \times 10^{16}} = \frac{2.25 \times 10^{20}}{5 \times 10^{16}} = 4.5 \times 10^{3} \text{ cm}^{-3}$$

Note: $n_h \ll n_e$ — holes are negligible minority carriers.

**Step 2:** Calculate conductivity:

$$\sigma = e(n_e\mu_e + n_h\mu_h)$$

$$= (1.6 \times 10^{-19})[(5 \times 10^{16})(1350) + (4.5 \times 10^{3})(480)]$$

$$= (1.6 \times 10^{-19})[6.75 \times 10^{19} + 2.16 \times 10^{6}]$$

The hole term ($2.16 \times 10^6$) is negligible compared to the electron term ($6.75 \times 10^{19}$):

$$\sigma \approx (1.6 \times 10^{-19})(6.75 \times 10^{19}) = \boxed{10.8 \text{ S/m}}$$

**Resistivity:** $\rho = 1/\sigma = 0.093\;\Omega\cdot$m

---

### Example 3: Fermi Level Position

**Problem:** For silicon at 300 K with $N_D = 10^{17}$ cm⁻³, $N_c = 2.8 \times 10^{19}$ cm⁻³, $E_c = 1.12$ eV (relative to VB), find the Fermi level position relative to the conduction band edge.

**Solution:**

$$E_c - E_F = kT \ln\left(\frac{N_c}{N_D}\right)$$

$$= 0.0259 \times \ln\left(\frac{2.8 \times 10^{19}}{10^{17}}\right)$$

$$= 0.0259 \times \ln(280)$$

$$= 0.0259 \times 5.635$$

$$\boxed{E_c - E_F = 0.146 \text{ eV}}$$

So the Fermi level lies **0.146 eV below** the conduction band edge, which is well into the upper half of the band gap — confirming n-type behavior.

---

### Example 4: Built-in Potential

**Problem:** A silicon p-n junction has $N_A = 10^{18}$ cm⁻³ (p-side), $N_D = 5 \times 10^{15}$ cm⁻³ (n-side), $n_i = 1.5 \times 10^{10}$ cm⁻³ at 300 K. Find the built-in potential.

**Solution:**

$$V_{bi} = V_T \ln\left(\frac{N_A N_D}{n_i^2}\right)$$

**Step 1:** Calculate the argument:

$$\frac{N_A N_D}{n_i^2} = \frac{10^{18} \times 5 \times 10^{15}}{(1.5 \times 10^{10})^2} = \frac{5 \times 10^{33}}{2.25 \times 10^{20}} = 2.22 \times 10^{13}$$

**Step 2:** Take logarithm:

$$\ln(2.22 \times 10^{13}) = \ln(2.22) + 13\ln(10) = 0.798 + 29.93 = 30.73$$

**Step 3:** Multiply by $V_T$:

$$\boxed{V_{bi} = 0.0259 \times 30.73 = 0.796 \text{ V}}$$

---

### Example 5: Depletion Width

**Problem:** For the junction in Example 4 ($N_A = 10^{18}$ cm⁻³, $N_D = 5 \times 10^{15}$ cm⁻³, $V_{bi} = 0.796$ V), find the depletion width at zero bias and at 5 V reverse bias. Given $\epsilon_s = 11.7 \times 8.854 \times 10^{-14}$ F/cm.

**Solution:**

$$\epsilon_s = 11.7 \times 8.854 \times 10^{-14} = 1.036 \times 10^{-12} \text{ F/cm}$$

**Step 1:** At zero bias ($V_R = 0$):

$$W = \sqrt{\frac{2 \times 1.036 \times 10^{-12} \times 0.796}{1.6 \times 10^{-19}} \times \left(\frac{1}{10^{18}} + \frac{1}{5 \times 10^{15}}\right)}$$

The $(1/N_A)$ term is negligible compared to $(1/N_D)$:

$$\frac{1}{N_A} + \frac{1}{N_D} \approx \frac{1}{5 \times 10^{15}} = 2 \times 10^{-16} \text{ cm}^3$$

$$W = \sqrt{\frac{2 \times 1.036 \times 10^{-12} \times 0.796 \times 2 \times 10^{-16}}{1.6 \times 10^{-19}}}$$

$$= \sqrt{\frac{3.297 \times 10^{-28}}{1.6 \times 10^{-19}}} = \sqrt{2.06 \times 10^{-9}}$$

$$\boxed{W_0 = 4.54 \times 10^{-5} \text{ cm} = 0.454 \;\mu\text{m}}$$

**Step 2:** At 5 V reverse bias ($V_R = 5$ V):

$$W = W_0 \sqrt{\frac{V_{bi} + V_R}{V_{bi}}} = 4.54 \times 10^{-5} \times \sqrt{\frac{0.796 + 5}{0.796}}$$

$$= 4.54 \times 10^{-5} \times \sqrt{7.28} = 4.54 \times 10^{-5} \times 2.698$$

$$\boxed{W_{5V} = 1.22 \times 10^{-4} \text{ cm} = 1.22 \;\mu\text{m}}$$

The depletion width increased by a factor of ~2.7 with 5 V reverse bias.

---

### Example 6: Diode Current

**Problem:** A silicon p-n junction diode has a reverse saturation current $I_0 = 2$ nA. Find the forward current at $V_F = 0.6$ V and at $V_F = 0.7$ V at 300 K.

**Solution:**

$$I = I_0(e^{V_F/V_T} - 1) \approx I_0\;e^{V_F/V_T}$$

**At $V_F = 0.6$ V:**

$$I = 2 \times 10^{-9} \times e^{0.6/0.0259} = 2 \times 10^{-9} \times e^{23.17}$$

$$e^{23.17} = 1.15 \times 10^{10}$$

$$\boxed{I = 2 \times 10^{-9} \times 1.15 \times 10^{10} = 23.0 \text{ A}}$$

**At $V_F = 0.7$ V:**

$$I = 2 \times 10^{-9} \times e^{0.7/0.0259} = 2 \times 10^{-9} \times e^{27.03}$$

$$e^{27.03} = 5.46 \times 10^{11}$$

$$\boxed{I = 2 \times 10^{-9} \times 5.46 \times 10^{11} = 1092 \text{ A}}$$

**Note:** A mere 0.1 V increase caused current to increase by a factor of ~47.5. In practice, series resistance limits the current. This illustrates why the diode has a relatively sharp "turn-on" voltage around 0.6-0.7 V for silicon.

---

### Example 7: BJT Calculations

**Problem:** An NPN transistor has $\beta = 100$ and is operating in the active region. If $I_B = 50\;\mu$A, find $I_C$, $I_E$, and $\alpha$.

**Solution:**

**Step 1:** Collector current:

$$I_C = \beta I_B = 100 \times 50\;\mu\text{A} = \boxed{5.0 \text{ mA}}$$

**Step 2:** Emitter current:

$$I_E = I_B + I_C = 50\;\mu\text{A} + 5000\;\mu\text{A} = \boxed{5.05 \text{ mA}}$$

**Step 3:** Alpha:

$$\alpha = \frac{I_C}{I_E} = \frac{5.0}{5.05} = \boxed{0.9901}$$

**Verification:** $\alpha = \frac{\beta}{1+\beta} = \frac{100}{101} = 0.9901$ ✓

**Additional check:** Given $I_E = 5.05$ mA, if instead we knew only $I_E$ and $\alpha$:

$$I_C = \alpha I_E = 0.9901 \times 5.05 = 5.0 \text{ mA}$$

$$I_B = (1-\alpha)I_E = 0.0099 \times 5.05 = 0.05 \text{ mA} = 50\;\mu\text{A}$$

---

### Example 8: EM Wave Speed from Constants

**Problem:** Using $\mu_0 = 4\pi \times 10^{-7}$ T·m/A and $\epsilon_0 = 8.854 \times 10^{-12}$ F/m, calculate the speed of light from Maxwell's prediction.

**Solution:**

$$c = \frac{1}{\sqrt{\mu_0\epsilon_0}}$$

**Step 1:** Calculate the product:

$$\mu_0\epsilon_0 = (4\pi \times 10^{-7})(8.854 \times 10^{-12})$$

$$= 12.566 \times 8.854 \times 10^{-19}$$

$$= 1.113 \times 10^{-17} \text{ s}^2/\text{m}^2$$

**Step 2:** Take the square root:

$$\sqrt{\mu_0\epsilon_0} = \sqrt{1.113 \times 10^{-17}} = 3.336 \times 10^{-9} \text{ s/m}$$

**Step 3:** Invert:

$$\boxed{c = \frac{1}{3.336 \times 10^{-9}} = 2.998 \times 10^{8} \text{ m/s} \approx 3 \times 10^8 \text{ m/s}}$$

This was Maxwell's great prediction — light is an electromagnetic wave!

---

### Example 9: Poynting Vector and Energy Density

**Problem:** An EM wave in free space has electric field amplitude $E_0 = 100$ V/m. Find: (a) the magnetic field amplitude, (b) the energy density, (c) the average intensity (Poynting vector magnitude).

**Solution:**

**(a)** Magnetic field amplitude:

$$B_0 = \frac{E_0}{c} = \frac{100}{3 \times 10^8} = \boxed{3.33 \times 10^{-7} \text{ T} = 0.333 \;\mu\text{T}}$$

**(b)** Energy density (at the instant when $E = E_0$):

$$u = \epsilon_0 E_0^2 = (8.854 \times 10^{-12})(100)^2 = 8.854 \times 10^{-8} \text{ J/m}^3$$

$$\boxed{u = 8.85 \times 10^{-8} \text{ J/m}^3}$$

**(c)** Average intensity:

$$I = \frac{1}{2}\epsilon_0 c E_0^2 = \frac{1}{2}(8.854 \times 10^{-12})(3 \times 10^8)(100)^2$$

$$= \frac{1}{2}(8.854 \times 10^{-12})(3 \times 10^8)(10^4)$$

$$= \frac{1}{2}(8.854)(3) \times 10^{0}$$

$$\boxed{I = 13.28 \text{ W/m}^2}$$

**Verification using alternative formula:**

$$I = \frac{E_0^2}{2\mu_0 c} = \frac{(100)^2}{2(4\pi \times 10^{-7})(3 \times 10^8)} = \frac{10^4}{754.0} = 13.26 \text{ W/m}^2 \;\checkmark$$

---

### Example 10: Radiation Pressure

**Problem:** A laser beam delivers an intensity of $I = 10^4$ W/m² to a perfectly reflecting mirror surface. Find the radiation pressure and the force on a mirror of area $A = 1$ cm².

**Solution:**

**Step 1:** Radiation pressure (perfect reflector):

$$P = \frac{2I}{c} = \frac{2 \times 10^4}{3 \times 10^8} = \boxed{6.67 \times 10^{-5} \text{ Pa}}$$

**Step 2:** Force on mirror:

$$F = P \times A = 6.67 \times 10^{-5} \times 1 \times 10^{-4}$$

$$\boxed{F = 6.67 \times 10^{-9} \text{ N} = 6.67 \text{ nN}}$$

**Note:** For comparison, for a perfect **absorber**: $P_{abs} = I/c = 3.33 \times 10^{-5}$ Pa (half the reflecting case).

---

### Example 11: Brewster's Angle

**Problem:** Find Brewster's angle for light going from glass ($n_1 = 1.52$) to air ($n_2 = 1.00$). Also find the critical angle for total internal reflection.

**Solution:**

**(a) Brewster's angle:**

$$\tan\theta_B = \frac{n_2}{n_1} = \frac{1.00}{1.52} = 0.6579$$

$$\boxed{\theta_B = \tan^{-1}(0.6579) = 33.3\degree}$$

At this angle, reflected light is completely s-polarized.

**(b) Critical angle:**

$$\theta_c = \sin^{-1}\left(\frac{n_2}{n_1}\right) = \sin^{-1}\left(\frac{1.00}{1.52}\right) = \sin^{-1}(0.6579)$$

$$\boxed{\theta_c = 41.1\degree}$$

Any angle of incidence greater than 41.1° results in total internal reflection.

**Check:** Note that $\theta_B < \theta_c$ (Brewster's angle is always less than critical angle when $n_1 > n_2$).

---

### Example 12: Total Internal Reflection in Fiber Optic

**Problem:** An optical fiber has core refractive index $n_1 = 1.48$ and cladding refractive index $n_2 = 1.46$. Find: (a) the critical angle at the core-cladding interface, (b) the maximum acceptance angle (numerical aperture) from air ($n_0 = 1$).

**Solution:**

**(a) Critical angle:**

$$\theta_c = \sin^{-1}\left(\frac{n_2}{n_1}\right) = \sin^{-1}\left(\frac{1.46}{1.48}\right) = \sin^{-1}(0.9865)$$

$$\boxed{\theta_c = 80.6\degree}$$

**(b) Numerical Aperture and acceptance angle:**

The numerical aperture is:

$$NA = \sqrt{n_1^2 - n_2^2} = \sqrt{(1.48)^2 - (1.46)^2} = \sqrt{2.1904 - 2.1316} = \sqrt{0.0588}$$

$$NA = 0.2424$$

Maximum acceptance angle from air:

$$\theta_{max} = \sin^{-1}\left(\frac{NA}{n_0}\right) = \sin^{-1}(0.2424)$$

$$\boxed{\theta_{max} = 14.0\degree}$$

Light entering within a cone of half-angle 14.0° will be guided by total internal reflection in the fiber.

---

## 13. Expanded Derivations

### 13.1 Derivation of the Built-in Potential

Start from the equilibrium condition: the Fermi level is constant across the junction.

On the p-side, the hole concentration is $p_p = N_A$.
On the n-side, the hole concentration is $p_n = n_i^2/N_D$.

Using Boltzmann statistics, the ratio of hole concentrations is:

$$\frac{p_p}{p_n} = e^{eV_{bi}/(kT)}$$

Therefore:

$$V_{bi} = \frac{kT}{e} \ln\left(\frac{p_p}{p_n}\right) = \frac{kT}{e} \ln\left(\frac{N_A}{n_i^2/N_D}\right) = \frac{kT}{e} \ln\left(\frac{N_A N_D}{n_i^2}\right)$$

This confirms the built-in potential formula from a statistical mechanics perspective.

### 13.2 Derivation of the Depletion Width

Using Poisson's equation across the depletion region:

$$\frac{d^2V}{dx^2} = -\frac{\rho(x)}{\epsilon_s}$$

In the p-side depletion region ($-x_p < x < 0$):

$$\rho(x) = -eN_A$$

In the n-side depletion region ($0 < x < x_n$):

$$\rho(x) = +eN_D$$

Integrating twice and applying boundary conditions (E = 0 outside depletion region, V continuous at x = 0), we obtain:

$$V_{bi} + V_R = \frac{eN_A x_p^2}{2\epsilon_s} + \frac{eN_D x_n^2}{2\epsilon_s}$$

Using charge neutrality: $N_A x_p = N_D x_n$, and $W = x_p + x_n$:

$$W = \sqrt{\frac{2\epsilon_s(V_{bi}+V_R)}{e}\left(\frac{1}{N_A}+\frac{1}{N_D}\right)}$$

### 13.3 Derivation of the Shockley Diode Equation

Starting from the continuity equation for minority carriers:

$$D_n \frac{d^2(\delta n)}{dx^2} - \frac{\delta n}{\tau_n} = 0$$

where $\delta n$ is the excess minority carrier concentration.

The general solution is:

$$\delta n(x) = A e^{-x/L_n} + B e^{x/L_n}$$

where $L_n = \sqrt{D_n \tau_n}$ is the diffusion length.

Applying boundary conditions:
1. At $x = 0$ (junction edge): $\delta n(0) = n_{p0}(e^{V/V_T} - 1)$
2. At $x = \infty$: $\delta n \to 0$

This gives $\delta n(x) = n_{p0}(e^{V/V_T} - 1)e^{-x/L_n}$.

The diffusion current at $x = 0$ is:

$$J_n = eD_n \frac{d(\delta n)}{dx}\bigg|_{x=0} = \frac{eD_n n_{p0}}{L_n}(e^{V/V_T} - 1)$$

A similar derivation for holes gives the total diode current:

$$I = I_0(e^{V/V_T} - 1)$$

where $I_0 = eA\left(\frac{D_n n_{p0}}{L_n} + \frac{D_p p_{n0}}{L_p}\right)$.

### 13.4 Derivation of Energy Density of EM Wave

The energy stored in the electric field:

$$u_E = \frac{1}{2}\epsilon_0 E^2$$

The energy stored in the magnetic field:

$$u_B = \frac{B^2}{2\mu_0}$$

For an EM wave, $E = cB$ and $c = 1/\sqrt{\mu_0\epsilon_0}$:

$$u_B = \frac{B^2}{2\mu_0} = \frac{E^2/(c^2)}{2\mu_0} = \frac{E^2}{2\mu_0 c^2} = \frac{E^2}{2\mu_0/(mu_0\epsilon_0)} = \frac{\epsilon_0 E^2}{2} = u_E$$

Therefore: $u = u_E + u_B = 2u_E = \epsilon_0 E^2$.

---

## 14. Common Mistakes and Pitfalls

### Semiconductors

| Mistake | Correct Approach |
|---------|-----------------|
| Using $n_e = N_D - n_i$ for n-type | Use $n_e \approx N_D$ (since $N_D \gg n_i$ at room temperature) |
| Forgetting mass action law $n_e n_h = n_i^2$ | Always use this to find minority carrier concentration |
| Confusing Fermi level direction in n-type vs p-type | n-type: $E_F$ moves toward CB; p-type: $E_F$ moves toward VB |
| Using $V_F$ in depletion width formula | Use $V_{bi} - V_F$ for forward bias; $V_{bi} + V_R$ for reverse bias |
| Treating $I_0$ as large current | $I_0$ is very small (nA to $\mu$A); the $-1$ in the diode equation matters at low $V_F$ |
| Using $I_C = \beta I_E$ | Wrong! Use $I_C = \beta I_B$ or $I_C = \alpha I_E$ |
| Assuming $\alpha > 1$ | Always $\alpha < 1$ and $\beta > 1$ |
| Forgetting that intrinsic semiconductor has $n_e = n_h = n_i$ | In extrinsic semiconductors, majority carrier $\neq$ minority carrier |
| Using drift velocity formula at high fields | $v_d = \mu E$ is valid only for low fields; velocity saturates at high fields |
| Confusing effective mass with free electron mass | Use $m^*$ (effective mass) for calculations inside a crystal |

### Electromagnetism

| Mistake | Correct Approach |
|---------|-----------------|
| Using $P = I/c$ for reflection | Reflection uses $P = 2I/c$; absorption uses $P = I/c$ |
| Forgetting the $1/2$ in average intensity | $I = \frac{1}{2}\epsilon_0 c E_0^2$, not $\epsilon_0 c E_0^2$ |
| Using Brewster angle formula with wrong ratio | $\tan\theta_B = n_2/n_1$ (going from medium 1 to medium 2) |
| Applying TIR from rare to dense medium | TIR only occurs when going from higher-$n$ to lower-$n$ |
| Confusing conduction current with displacement current | Conduction current = flow of charges; displacement current = $\epsilon_0 \partial E/\partial t$ |
| Using $E = cB$ for average values | $E_0 = cB_0$ for amplitudes; for instantaneous values, both peak and decrease together |
| Forgetting that $E$, $B$, and $k$ form a right-handed system | $\vec{E} \times \vec{B}$ must point in the direction of propagation |
| Using wrong formula for $R$ at non-normal incidence | $R = (n_1-n_2)^2/(n_1+n_2)^2$ is only for normal incidence |
| Assuming $n$ is always $> 1$ | For plasmas and metals at certain frequencies, $n < 1$ |
| Forgetting that $I_0 \propto n_i^2$ (very T-dependent) | Saturation current doubles roughly every 10°C for Si |

---

## 15. Summary of Key Concepts

### Part A: Semiconductors

1. **Band theory** explains why some materials conduct (overlapping bands or small gap) and others insulate (large gap)
2. **Intrinsic semiconductors** have equal electron and hole concentrations governed by $n_i$
3. **Doping** controls carrier type and concentration — the foundation of all semiconductor devices
4. **Drift** (field-driven) and **diffusion** (concentration-driven) are the two carrier transport mechanisms, connected by Einstein's relation
5. The **p-n junction** is the fundamental building block — its I-V characteristic is exponential in forward bias
6. **BJTs** amplify signals through current gain; **FETs** are voltage-controlled switches

### Part B: Electromagnetism

1. **Maxwell's equations** unify electricity and magnetism and predict electromagnetic waves
2. **Displacement current** was Maxwell's key insight — changing E creates B, completing the symmetry
3. EM waves are **transverse**, propagate at $c = 1/\sqrt{\mu_0\epsilon_0}$, and carry energy and momentum
4. **Poynting vector** gives the direction and magnitude of energy flow
5. **Reflection, refraction, TIR** are consequences of boundary conditions on Maxwell's equations
6. **Brewster's angle** and **critical angle** are key angles to memorize and understand

---

## 16. Cross-References

- [[engineering-physics/module-1-optics-interference-diffraction|Module 1: Interference & Diffraction]] — Maxwell's equations → wave equation → light as EM wave; polarization, Brewster's angle derived from Fresnel equations
- [[engineering-physics/module-2-optoelectronics-lasers-fiber-optics|Module 2: Optoelectronics]] — Semiconductor lasers (GaAs p-n junction), photodiodes, fiber optic TIR, EDFA amplifiers
- [[engineering-physics/module-3-quantum-mechanics|Module 3: Quantum Mechanics]] — Energy bands arise from quantum mechanics; Fermi-Dirac statistics govern carrier distribution; quantum tunneling in tunnel diodes and STM

---

*Module 4 of 4 — [[engineering-physics/module-1-optics-interference-diffraction|← Module 1]] | [[engineering-physics/module-2-optoelectronics-lasers-fiber-optics|← Module 2]] | [[engineering-physics/module-3-quantum-mechanics|← Module 3]]*

## 17. Practice Tips for Exam Success

### Semiconductor Problems

- Always identify the **carrier type** (n-type or p-type) first before doing any calculation
- Remember that $V_T = kT/e \approx 0.0259$ V at 300 K — this value appears in almost every semiconductor formula
- The mass action law $n_e n_h = n_i^2$ is your most powerful tool — use it to find minority carriers
- For BJT problems, always check which region the transistor is in (active, saturation, or cut-off) before applying formulas
- Units matter: keep concentrations in cm⁻³ and mobilities in cm²/V·s consistently

### Electromagnetism Problems

- The factor of $1/2$ in $I = \frac{1}{2}\epsilon_0 c E_0^2$ comes from time-averaging — don't forget it
- Radiation pressure: **absorbing** surface gets $I/c$, **reflecting** surface gets $2I/c$
- Brewster's angle formula uses $\tan$, while critical angle uses $\sin$ — don't confuse them
- Always check that $n_1 > n_2$ before applying TIR formulas
- The Poynting vector direction gives the direction of energy flow — use the right-hand rule with $\vec{E} \times \vec{B}$

### General Tips

- Memorize $V_T = 0.0259$ V, $c = 3 \times 10^8$ m/s, $\epsilon_0 = 8.854 \times 10^{-12}$ F/m
- For numerical problems, always write down the formula first, substitute values, then calculate
- Keep track of powers of 10 carefully — semiconductor concentrations span many orders of magnitude
- In exams, partial credit is given for correct formulas even if the arithmetic is wrong

---

## 18. Quick-Reference Constants

| Constant | Symbol | Value |
|----------|--------|-------|
| Elementary charge | $e$ | $1.6 \times 10^{-19}$ C |
| Boltzmann constant | $k$ | $1.38 \times 10^{-23}$ J/K |
| Thermal voltage (300 K) | $V_T = kT/e$ | $0.0259$ V |
| Planck's constant | $h$ | $6.626 \times 10^{-34}$ J·s |
| Reduced Planck's constant | $\hbar$ | $1.055 \times 10^{-34}$ J·s |
| Permittivity of free space | $\epsilon_0$ | $8.854 \times 10^{-12}$ F/m |
| Permeability of free space | $\mu_0$ | $4\pi \times 10^{-7}$ T·m/A |
| Speed of light | $c$ | $2.998 \times 10^8$ m/s |
| Si relative permittivity | $\epsilon_r$ | 11.7 |
| Si band gap (300 K) | $E_g$ | 1.12 eV |

---

*Module 4 of Engineering Physics — Complete Reference*
