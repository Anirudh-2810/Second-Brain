---
module: "physics"
topic: "Physics — JEE Advanced / IIT Level Complete Reference"
tags: [physics, jee, iit, mechanics, electrodynamics, optics, modern, thermodynamics, waves]
last_updated: "2026-08-11"
source: "/raw-sources/Physics/ (Physics IIT Kota notes, Practice questions)"
---

# Physics — JEE Advanced / IIT Level Complete Reference

> Comprehensive topic-wise notes distilled from Kota classroom notes and practice modules. Covers entire JEE Advanced syllabus with derivations, conceptual insights, and problem-solving strategies.

---

## 📚 Module Structure

| Section | Topics | Pages |
|---------|--------|-------|
| **Mechanics** | Kinematics, Laws of Motion, Work-Energy-Power, Rotational Motion, Gravitation, Fluid Mechanics, Properties of Matter | 7 |
| **Electrodynamics** | Electrostatics, Current Electricity, Capacitors, Magnetic Effects, EMI, AC, Electromagnetic Waves | 7 |
| **Optics** | Ray Optics, Wave Optics, Optical Instruments | 3 |
| **Modern Physics** | Atoms & Nuclei, Dual Nature, Semiconductors, Communication | 4 |
| **Thermodynamics & Kinetic Theory** | Laws of Thermodynamics, Kinetic Theory, Calorimetry | 3 |
| **Waves & Oscillations** | SHM, Waves, Sound, Doppler Effect | 4 |
| **Formula Sheets** | Mechanics, Electrodynamics, Optics, Modern, Thermal | 5 |

---

## 🎯 Mechanics

### 1. Kinematics
**Key Concepts:** Vectors, 1D/2D motion, projectile, relative motion, graphs.

**Critical Formulas:**
- $v = u + at$, $s = ut + \frac{1}{2}at^2$, $v^2 = u^2 + 2as$
- Projectile: $R = \frac{u^2 \sin 2\theta}{g}$, $H = \frac{u^2 \sin^2 \theta}{2g}$, $T = \frac{2u \sin \theta}{g}$
- Trajectory: $y = x \tan \theta - \frac{g x^2}{2 u^2 \cos^2 \theta}$
- Relative velocity: $\vec{v}_{AB} = \vec{v}_A - \vec{v}_B$
- Graphs: $x-t$ slope = $v$; $v-t$ slope = $a$, area = displacement

**JEE Traps:** Projectile on inclined plane, relative motion in 2D, variable acceleration ($a = f(t), f(v), f(x)$)

### 2. Laws of Motion
**Key Concepts:** Newton's laws, friction, circular motion, pseudo forces, constrained motion.

**Critical Formulas:**
- $F = ma$; $F_{net} = \frac{dp}{dt}$
- Friction: $f_s \le \mu_s N$, $f_k = \mu_k N$
- Circular: $a_c = \frac{v^2}{r} = \omega^2 r$; banking $\tan \theta = \frac{v^2}{rg}$
- Pseudo force: $-ma_{frame}$ (in non-inertial frame)
- Constrained: $\sum T \cdot v = 0$ (virtual work) or $\sum a \cdot n = 0$

**JEE Traps:** Friction direction in rolling, pseudo force in accelerating wedge, tension in massive rope

### 3. Work, Energy, Power
**Key Concepts:** Work-energy theorem, conservative/non-conservative forces, potential energy, power, collisions.

**Critical Formulas:**
- $W = \int \vec{F} \cdot d\vec{s}$; $W = \Delta K$
- $U = -\int \vec{F}_{cons} \cdot d\vec{s}$; $F = -\frac{dU}{dx}$
- $E = K + U$ (conserved if only conservative forces)
- Power: $P = \frac{dW}{dt} = \vec{F} \cdot \vec{v}$
- Elastic collision: $e = 1$, $K$ conserved, $v_{sep} = v_{app}$
- Inelastic: $e < 1$, $K$ not conserved; perfectly inelastic: $e = 0$, max $K$ loss
- $v_1' = \frac{m_1 - e m_2}{m_1 + m_2} v_1 + \frac{(1+e)m_2}{m_1 + m_2} v_2$

**JEE Traps:** Center of mass frame collisions, variable force work, power from $F-v$ graph

### 4. Rotational Motion
**Key Concepts:** Moment of inertia, torque, angular momentum, rolling, fixed axis rotation.

**Critical Formulas:**
- $\tau = r \times F = I \alpha$; $L = I \omega = r \times p$
- $I = \sum m_i r_i^2$; Parallel axis: $I = I_{cm} + Md^2$; Perpendicular axis: $I_z = I_x + I_y$ (lamina)
- Rolling without slipping: $v = \omega R$, $a = \alpha R$; $K = \frac{1}{2}I\omega^2 + \frac{1}{2}Mv^2$
- $I$ values: Ring ($MR^2$), Disc ($\frac{1}{2}MR^2$), Solid sphere ($\frac{2}{5}MR^2$), Hollow sphere ($\frac{2}{3}MR^2$), Rod about end ($\frac{1}{3}ML^2$)
- Angular momentum conservation: $\tau_{ext} = 0 \implies L = \text{const}$

**JEE Traps:** Instantaneous axis of rotation, toppling vs rolling, angular impulse

### 5. Gravitation
**Key Concepts:** Universal law, field/potential, satellites, escape velocity, Kepler's laws.

**Critical Formulas:**
- $F = \frac{G m_1 m_2}{r^2}$; $g = \frac{GM}{R^2}$
- Field: $E = \frac{GM}{r^2}$; Potential: $V = -\frac{GM}{r}$
- $g_h = g(1 - \frac{2h}{R})$, $g_d = g(1 - \frac{d}{R})$
- Escape velocity: $v_{esc} = \sqrt{\frac{2GM}{R}} = \sqrt{2gR}$
- Orbital velocity: $v_{orb} = \sqrt{\frac{GM}{r}}$
- Time period: $T = 2\pi \sqrt{\frac{r^3}{GM}}$ (Kepler's 3rd: $T^2 \propto r^3$)
- Energy: $E = -\frac{GMm}{2r}$; Binding energy $= \frac{GMm}{2r}$

**JEE Traps:** Geo-stationary satellite, gravitational potential inside/outside shell, two-body problem

### 6. Fluid Mechanics
**Key Concepts:** Pressure, buoyancy, fluid dynamics, surface tension, viscosity.

**Critical Formulas:**
- $P = P_0 + \rho gh$; $P = \frac{F}{A}$
- Buoyancy: $F_b = \rho_{fluid} V_{sub} g$ (Archimedes)
- Continuity: $A_1 v_1 = A_2 v_2$
- Bernoulli: $P + \frac{1}{2}\rho v^2 + \rho gh = \text{const}$
- Torricelli: $v = \sqrt{2gh}$
- Viscosity: $F = \eta A \frac{dv}{dx}$; Stokes: $F = 6\pi \eta r v$
- Surface tension: $F = T l$; Excess pressure: $\frac{2T}{R}$ (drop), $\frac{4T}{R}$ (bubble); Capillary rise: $h = \frac{2T \cos\theta}{\rho g r}$

### 7. Properties of Matter
**Key Concepts:** Elasticity, stress-strain, moduli, thermal expansion.

**Critical Formulas:**
- Stress $= \frac{F}{A}$; Strain $= \frac{\Delta L}{L}$; Young's $Y = \frac{\text{Stress}}{\text{Strain}}$
- Bulk modulus $B = -\frac{V \Delta P}{\Delta V}$; Shear modulus $\eta = \frac{\text{Shear stress}}{\text{Shear strain}}$
- Poisson's ratio $\sigma = -\frac{\text{Lateral strain}}{\text{Longitudinal strain}}$
- Thermal stress: $\frac{F}{A} = Y \alpha \Delta T$ (constrained)
- $\Delta L = L \alpha \Delta T$; $\Delta A = 2A \alpha \Delta T$; $\Delta V = 3V \alpha \Delta T$

---

## 🎯 Electrodynamics

### 1. Electrostatics
**Key Concepts:** Coulomb's law, field, potential, Gauss's law, dipole, capacitors.

**Critical Formulas:**
- Coulomb: $F = \frac{1}{4\pi\epsilon_0} \frac{q_1 q_2}{r^2}$
- Field: $E = \frac{F}{q_0}$; Point charge: $E = \frac{kq}{r^2}$
- Potential: $V = \frac{W}{q} = \frac{kq}{r}$; $V = -\int \vec{E} \cdot d\vec{l}$
- Dipole: $p = qd$; $E_{axial} = \frac{2kp}{r^3}$, $E_{equatorial} = \frac{kp}{r^3}$; $V = \frac{kp \cos\theta}{r^2}$
- Gauss: $\oint \vec{E} \cdot d\vec{A} = \frac{Q_{enc}}{\epsilon_0}$
- Applications: Infinite line $\frac{\lambda}{2\pi\epsilon_0 r}$, Plane sheet $\frac{\sigma}{2\epsilon_0}$, Sphere $\frac{kQ}{r^2}$ (outside), $0$ (inside conductor)
- Energy: $U = \frac{1}{2} \int \rho V d\tau = \frac{1}{2} \sum q_i V_i$

### 2. Capacitors
**Key Concepts:** Capacitance, combinations, dielectrics, energy, charging/discharging.

**Critical Formulas:**
- $C = \frac{Q}{V}$; Parallel plate: $C = \frac{\epsilon_0 A}{d}$
- Series: $\frac{1}{C_{eq}} = \sum \frac{1}{C_i}$; Parallel: $C_{eq} = \sum C_i$
- With dielectric: $C = K C_0$; Partial filling: treat as series/parallel
- Energy: $U = \frac{1}{2}CV^2 = \frac{Q^2}{2C} = \frac{1}{2}QV$
- Energy density: $u = \frac{1}{2}\epsilon_0 E^2 = \frac{1}{2}\epsilon E^2$
- Charging: $q = Q_0(1 - e^{-t/RC})$; Discharging: $q = Q_0 e^{-t/RC}$; $\tau = RC$

### 3. Current Electricity
**Key Concepts:** Drift velocity, Ohm's law, resistivity, Kirchhoff's laws, Wheatstone, potentiometer.

**Critical Formulas:**
- $I = n e A v_d$; $J = \sigma E = \frac{I}{A}$
- $R = \rho \frac{l}{A}$; $\rho = \rho_0[1 + \alpha(T-T_0)]$
- Ohm: $V = IR$; Power: $P = VI = I^2R = \frac{V^2}{R}$
- Series: $R_{eq} = \sum R_i$; Parallel: $\frac{1}{R_{eq}} = \sum \frac{1}{R_i}$
- Kirchhoff: $\sum I = 0$ (junction); $\sum V = 0$ (loop)
- Wheatstone: $\frac{P}{Q} = \frac{R}{S}$ (balanced)
- Meter bridge: $\frac{R}{S} = \frac{l_1}{l_2}$
- Potentiometer: $\frac{E_1}{E_2} = \frac{l_1}{l_2}$; Internal resistance: $r = R(\frac{l_1 - l_2}{l_2})$

### 4. Magnetic Effects of Current
**Key Concepts:** Biot-Savart, Ampere's law, force on charge/wire, torque, magnetic materials.

**Critical Formulas:**
- Biot-Savart: $d\vec{B} = \frac{\mu_0}{4\pi} \frac{I d\vec{l} \times \hat{r}}{r^2}$
- Straight wire: $B = \frac{\mu_0 I}{2\pi r}$
- Circular loop (center): $B = \frac{\mu_0 I}{2R}$; Axis: $B = \frac{\mu_0 I R^2}{2(R^2+x^2)^{3/2}}$
- Solenoid: $B = \mu_0 n I$ (inside); Toroid: $B = \frac{\mu_0 N I}{2\pi r}$
- Ampere: $\oint \vec{B} \cdot d\vec{l} = \mu_0 I_{enc}$
- Force on charge: $\vec{F} = q(\vec{v} \times \vec{B})$; Radius: $r = \frac{mv}{qB}$; $T = \frac{2\pi m}{qB}$
- Force on wire: $\vec{F} = I(\vec{l} \times \vec{B})$
- Torque: $\vec{\tau} = \vec{\mu} \times \vec{B}$; $\mu = I A$
- Magnetic materials: $\vec{M} = \chi \vec{H}$; $B = \mu_0(H + M) = \mu_0(1+\chi)H = \mu H$

### 5. Electromagnetic Induction (EMI)
**Key Concepts:** Faraday's law, Lenz's law, motional emf, self/mutual inductance, eddy currents.

**Critical Formulas:**
- Faraday: $\mathcal{E} = -\frac{d\Phi}{dt}$; $\Phi = \int \vec{B} \cdot d\vec{A}$
- Motional emf: $\mathcal{E} = B l v$ (perpendicular); $\mathcal{E} = \int (\vec{v} \times \vec{B}) \cdot d\vec{l}$
- Self-inductance: $\Phi = L I$; $\mathcal{E} = -L \frac{dI}{dt}$; $L = \frac{\mu_0 N^2 A}{l}$ (solenoid)
- Mutual inductance: $\Phi_2 = M I_1$; $\mathcal{E}_2 = -M \frac{dI_1}{dt}$; $M_{12} = M_{21}$
- Energy: $U = \frac{1}{2} L I^2$; $U = \frac{B^2}{2\mu_0}$ (energy density)
- LR circuit: $I = I_0(1 - e^{-t/\tau})$, $\tau = L/R$; Decay: $I = I_0 e^{-t/\tau}$
- LC oscillations: $\omega = \frac{1}{\sqrt{LC}}$; $Q = Q_0 \cos(\omega t + \phi)$

### 6. Alternating Current (AC)
**Key Concepts:** RMS values, phasors, RLC circuits, resonance, power factor, transformers.

**Critical Formulas:**
- $i = I_0 \sin(\omega t)$; $I_{rms} = I_0/\sqrt{2}$; $V_{rms} = V_0/\sqrt{2}$
- Reactance: $X_L = \omega L$; $X_C = \frac{1}{\omega C}$
- Impedance: $Z = \sqrt{R^2 + (X_L - X_C)^2}$; $\tan\phi = \frac{X_L - X_C}{R}$
- Resonance: $X_L = X_C \implies \omega_0 = \frac{1}{\sqrt{LC}}$; $Z_{min} = R$, $I_{max} = V/R$
- Quality factor: $Q = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 C R} = \frac{\omega_0}{\Delta\omega}$
- Power: $P_{avg} = V_{rms} I_{rms} \cos\phi = I_{rms}^2 R$
- Transformer: $\frac{V_s}{V_p} = \frac{N_s}{N_p} = \frac{I_p}{I_s}$ (ideal)

### 7. Electromagnetic Waves
**Key Concepts:** Maxwell's equations, wave equation, spectrum, radiation pressure.

**Critical Formulas:**
- $c = \frac{1}{\sqrt{\mu_0 \epsilon_0}} = 3 \times 10^8$ m/s
- $\vec{E} = E_0 \sin(kx - \omega t) \hat{j}$, $\vec{B} = B_0 \sin(kx - \omega t) \hat{k}$; $E_0 = c B_0$
- Intensity: $I = \frac{1}{2} \epsilon_0 E_0^2 c = \frac{E_0 B_0}{2\mu_0}$
- Radiation pressure: $P = \frac{I}{c}$ (absorbing), $P = \frac{2I}{c}$ (reflecting)
- Spectrum: $\gamma$-ray < X-ray < UV < Visible < IR < Microwave < Radio

---

## 🎯 Optics

### 1. Ray Optics (Geometrical)
**Key Concepts:** Reflection, refraction, mirrors, lenses, prisms, optical instruments.

**Critical Formulas:**
- Mirror: $\frac{1}{v} + \frac{1}{u} = \frac{1}{f} = \frac{2}{R}$; $m = -\frac{v}{u} = \frac{h'}{h}$
- Refraction: $\frac{\sin i}{\sin r} = \mu$ (relative); $\mu_{21} = \frac{\mu_2}{\mu_1} = \frac{\sin i}{\sin r}$
- Apparent depth: $d_{app} = \frac{d_{real}}{\mu}$ (normal view)
- Lens maker: $\frac{1}{f} = (\mu - 1)(\frac{1}{R_1} - \frac{1}{R_2})$
- Lens formula: $\frac{1}{v} - \frac{1}{u} = \frac{1}{f}$; $m = \frac{v}{u}$
- Power: $P = \frac{1}{f(m)} = \frac{100}{f(cm)}$ (diopter)
- Combination: $P_{eq} = \sum P_i$ (thin lenses in contact)
- Prism: $\delta = i + e - A$; Minimum deviation: $\mu = \frac{\sin\frac{A+\delta_m}{2}}{\sin\frac{A}{2}}$
- Dispersion: $\delta_v - \delta_r = (\mu_v - \mu_r)A$; $\omega = \frac{\mu_v - \mu_r}{\mu - 1}$ (dispersive power)

### 2. Wave Optics
**Key Concepts:** Huygens' principle, interference, diffraction, polarization.

**Critical Formulas:**
- Interference (Young's double slit): $\beta = \frac{\lambda D}{d}$; $y_n = \frac{n\lambda D}{d}$ (bright); $y_n = \frac{(2n-1)\lambda D}{2d}$ (dark)
- Path difference: $\Delta = d \sin\theta \approx \frac{dy}{D}$
- Coherent sources: $\Delta = n\lambda$ (constructive), $\Delta = (2n-1)\frac{\lambda}{2}$ (destructive)
- Thin film: $2\mu t \cos r = n\lambda$ (reflected, phase change); $= (2n-1)\frac{\lambda}{2}$ (transmitted)
- Diffraction (single slit): $a \sin\theta = n\lambda$ (minima); $\theta \approx \frac{n\lambda}{a}$; Central max width $= \frac{2\lambda D}{a}$
- Polarization: Malus' law: $I = I_0 \cos^2\theta$; Brewster's angle: $\tan\theta_p = \mu$; $\theta_p + r = 90^\circ$

### 3. Optical Instruments
**Key Concepts:** Eye, microscope, telescope, resolving power.

**Critical Formulas:**
- Simple microscope: $M = 1 + \frac{D}{f}$ ($D=25$ cm)
- Compound microscope: $M = \frac{v_0}{u_0}(1 + \frac{D}{f_e}) \approx \frac{L}{f_0}(1 + \frac{D}{f_e})$ ($L$ = tube length)
- Telescope (astronomical): $M = \frac{f_0}{f_e}$ (normal); $M = \frac{f_0}{f_e}(1 + \frac{f_e}{D})$ (near point)
- Resolving power (microscope): $R.P. = \frac{2\mu \sin\theta}{\lambda}$; (telescope): $R.P. = \frac{D}{1.22\lambda}$

---

## 🎯 Modern Physics

### 1. Dual Nature of Matter & Radiation
**Key Concepts:** Photoelectric effect, matter waves, Davisson-Germer.

**Critical Formulas:**
- Photon energy: $E = h\nu = \frac{hc}{\lambda}$; Momentum: $p = \frac{h}{\lambda} = \frac{E}{c}$
- Photoelectric: $h\nu = \phi + K_{max}$; $K_{max} = eV_s$ (stopping potential)
- Einstein: $K_{max} = h\nu - \phi$; $V_s = \frac{h}{e}\nu - \frac{\phi}{e}$
- de Broglie: $\lambda = \frac{h}{p} = \frac{h}{\sqrt{2mK}} = \frac{h}{\sqrt{2meV}}$ (accelerated by $V$)
- Davisson-Germer: $n\lambda = 2d \sin\theta$ (Bragg's law)

### 2. Atoms & Nuclei
**Key Concepts:** Bohr model, hydrogen spectrum, nuclear structure, radioactivity, fission/fusion.

**Critical Formulas:**
- Bohr: $r_n = \frac{n^2 h^2 \epsilon_0}{\pi m e^2} = n^2 a_0$ ($a_0 = 0.529$ Å)
- Energy: $E_n = -\frac{13.6}{n^2}$ eV; $E_n = -\frac{me^4}{8\epsilon_0^2 h^2 n^2}$
- Transitions: $\frac{1}{\lambda} = R Z^2 (\frac{1}{n_1^2} - \frac{1}{n_2^2})$; $R = 1.097 \times 10^7$ m⁻¹
- Series: Lyman ($n_1=1$), Balmer ($n_1=2$), Paschen ($n_1=3$)
- Nuclear: $R = R_0 A^{1/3}$ ($R_0 \approx 1.2$ fm); Binding energy $B = \Delta m c^2$
- Radioactivity: $N = N_0 e^{-\lambda t}$; $T_{1/2} = \frac{\ln 2}{\lambda}$; $T_{avg} = \frac{1}{\lambda}$
- $\alpha$-decay: $Z \to Z-2$, $A \to A-4$; $\beta^-$: $n \to p + e^- + \bar{\nu}_e$; $\beta^+$: $p \to n + e^+ + \nu_e$
- Fission: $U^{235} + n \to$ fragments + $2-3 n$ + energy (~200 MeV)
- Fusion: Light nuclei $\to$ heavier + energy (Sun: $p-p$ chain)

### 3. Semiconductor Devices
**Key Concepts:** Energy bands, p-n junction, diodes, transistors, logic gates.

**Critical Formulas:**
- Intrinsic: $n_i^2 = n_e n_h$; $n_i \propto T^{3/2} e^{-E_g/2kT}$
- Doping: $n$-type ($n_e \approx N_D$); $p$-type ($n_h \approx N_A$)
- p-n junction: $V_{bi} = \frac{kT}{e} \ln\frac{N_A N_D}{n_i^2}$; Depletion width $W \propto \sqrt{V_{bi} + V_R}$
- Diode: $I = I_0(e^{eV/kT} - 1)$; Forward: $I \approx I_0 e^{eV/kT}$; Reverse: $I \approx -I_0$
- Zener: Breakdown at $V_Z$ (avalanche/Zener)
- Rectifier: Half-wave ($\eta = 40.6\%$), Full-wave ($\eta = 81.2\%$), Bridge
- Transistor (BJT): $\alpha = \frac{I_C}{I_E}$, $\beta = \frac{I_C}{I_B} = \frac{\alpha}{1-\alpha}$; $I_C = \beta I_B + (1+\beta)I_{CBO}$
- Logic gates: AND, OR, NOT, NAND, NOR, XOR, XNOR

### 4. Communication Systems
**Key Concepts:** Modulation, AM/FM, bandwidth, propagation.

**Critical Formulas:**
- AM: $s(t) = A_c[1 + m \cos(\omega_m t)] \cos(\omega_c t)$; $m = \frac{A_m}{A_c}$ (modulation index)
- Bandwidth: $BW = 2 f_m$ (AM); $BW \approx 2(\Delta f + f_m)$ (FM, Carson's rule)
- FM: $s(t) = A_c \cos(\omega_c t + \beta \sin \omega_m t)$; $\beta = \frac{\Delta f}{f_m}$
- Propagation: Ground wave (< 2 MHz), Sky wave (2-30 MHz, ionosphere), Space wave (> 30 MHz, LOS)

---

## 🎯 Thermodynamics & Kinetic Theory

### 1. Thermodynamics
**Key Concepts:** Laws, processes, heat engines, entropy.

**Critical Formulas:**
- 1st Law: $\Delta U = Q + W$; $W = -\int P dV$
- Isothermal: $W = nRT \ln\frac{V_2}{V_1}$; $Q = -W$
- Adiabatic: $PV^\gamma = \text{const}$; $TV^{\gamma-1} = \text{const}$; $W = \frac{nR(T_1-T_2)}{\gamma-1}$
- Isochoric: $W = 0$; $Q = nC_v \Delta T$
- Isobaric: $W = P \Delta V = nR \Delta T$; $Q = nC_p \Delta T$
- Cyclic: $\Delta U = 0 \implies Q = -W$
- Heat engine: $\eta = 1 - \frac{Q_2}{Q_1} = \frac{W}{Q_1}$; Carnot: $\eta = 1 - \frac{T_2}{T_1}$
- Refrigerator: $\beta = \frac{Q_2}{W} = \frac{T_2}{T_1 - T_2}$
- Entropy: $dS = \frac{dQ_{rev}}{T}$; $\Delta S = \int \frac{C}{T} dT$

### 2. Kinetic Theory of Gases
**Key Concepts:** Microscopic model, pressure, temperature, degrees of freedom, specific heats.

**Critical Formulas:**
- $P = \frac{1}{3} \frac{N m \bar{v}^2}{V} = \frac{1}{3} \rho \bar{v}^2$
- $PV = \frac{1}{3} N m \bar{v}^2 = N k_B T = nRT$
- $\bar{v}^2 = \frac{3RT}{M}$; $v_{rms} = \sqrt{\frac{3RT}{M}}$; $v_{avg} = \sqrt{\frac{8RT}{\pi M}}$; $v_{mp} = \sqrt{\frac{2RT}{M}}$
- $KE_{avg} = \frac{3}{2} k_B T$ per molecule; $U = \frac{f}{2} nRT$ per mole
- $C_v = \frac{f}{2} R$; $C_p = C_v + R = \frac{f+2}{2} R$; $\gamma = \frac{C_p}{C_v} = \frac{f+2}{f}$
- $f = 3$ (monoatomic), $5$ (diatomic, room temp), $7$ (diatomic, high temp), $6$ (polyatomic)

### 3. Calorimetry & Heat Transfer
**Key Concepts:** Calorimetry, conduction, convection, radiation.

**Critical Formulas:**
- Heat: $Q = m c \Delta T$; Latent: $Q = m L$
- Conduction: $\frac{dQ}{dt} = \frac{k A \Delta T}{l}$; Thermal resistance $R = \frac{l}{kA}$
- Convection: $\frac{dQ}{dt} = h A \Delta T$
- Radiation (Stefan-Boltzmann): $\frac{dQ}{dt} = \sigma A e (T^4 - T_0^4)$; $\sigma = 5.67 \times 10^{-8}$ W/m²K⁴
- Wien's displacement: $\lambda_{max} T = b$ ($b = 2.898 \times 10^{-3}$ m·K)
- Newton's cooling: $\frac{dT}{dt} = -k(T - T_0)$

---

## 🎯 Waves & Oscillations

### 1. Simple Harmonic Motion (SHM)
**Key Concepts:** Definition, energy, spring-mass, pendulum, superposition, damped/forced.

**Critical Formulas:**
- $F = -kx$; $a = -\omega^2 x$; $\omega = \sqrt{k/m}$; $T = \frac{2\pi}{\omega} = 2\pi \sqrt{\frac{m}{k}}$
- $x = A \sin(\omega t + \phi)$ or $A \cos(\omega t + \phi)$
- $v = \omega \sqrt{A^2 - x^2}$; $v_{max} = A\omega$
- $a = -\omega^2 x$; $a_{max} = A\omega^2$
- Energy: $E = \frac{1}{2} k A^2 = \frac{1}{2} m \omega^2 A^2$; $K = \frac{1}{2} m \omega^2 (A^2 - x^2)$; $U = \frac{1}{2} k x^2$
- Spring series: $\frac{1}{k_{eq}} = \sum \frac{1}{k_i}$; Parallel: $k_{eq} = \sum k_i$
- Simple pendulum: $T = 2\pi \sqrt{\frac{L}{g}}$; Physical pendulum: $T = 2\pi \sqrt{\frac{I}{mgd}}$
- Damped: $x = A_0 e^{-bt/2m} \sin(\omega' t + \phi)$; $\omega' = \sqrt{\omega_0^2 - (b/2m)^2}$
- Forced: $x = A \sin(\omega t - \delta)$; Resonance at $\omega = \omega_0$ (undamped)

### 2. Wave Motion
**Key Concepts:** Progressive wave, standing wave, reflection, interference.

**Critical Formulas:**
- Progressive: $y = A \sin(kx - \omega t + \phi)$; $k = \frac{2\pi}{\lambda}$; $\omega = 2\pi f$; $v = f\lambda = \frac{\omega}{k}$
- Power: $P = \frac{1}{2} \mu \omega^2 A^2 v$; Intensity: $I = \frac{P}{A} = \frac{1}{2} \rho v \omega^2 A^2$
- Standing wave: $y = 2A \sin(kx) \cos(\omega t)$; Nodes: $kx = n\pi$; Antinodes: $kx = (2n+1)\frac{\pi}{2}$
- Reflection: Fixed end $\to$ phase change $\pi$; Free end $\to$ no phase change
- String fixed both ends: $\lambda_n = \frac{2L}{n}$; $f_n = \frac{nv}{2L} = n f_1$
- Pipe open both ends: $f_n = \frac{nv}{2L}$; Pipe closed one end: $f_n = \frac{(2n-1)v}{4L}$

### 3. Sound Waves
**Key Concepts:** Longitudinal waves, intensity, beats, Doppler effect.

**Critical Formulas:**
- $v = \sqrt{\frac{B}{\rho}} = \sqrt{\frac{\gamma P}{\rho}} = \sqrt{\frac{\gamma RT}{M}}$
- Intensity level: $\beta = 10 \log_{10} \frac{I}{I_0}$ dB ($I_0 = 10^{-12}$ W/m²)
- Beats: $f_{beat} = |f_1 - f_2|$; $y = 2A \cos(2\pi \frac{f_1-f_2}{2}t) \sin(2\pi \frac{f_1+f_2}{2}t)$
- Doppler (source moving): $f' = f \frac{v}{v \mp v_s}$ ($-$ approaching, $+$ receding)
- Doppler (observer moving): $f' = f \frac{v \pm v_o}{v}$ ($+$ approaching, $-$ receding)
- General: $f' = f \frac{v \pm v_o}{v \mp v_s}$

---

## 📐 Formula Sheets

### Mechanics Formula Sheet
See: [[physics/formula-sheet-mechanics]]

### Electrodynamics Formula Sheet
See: [[physics/formula-sheet-electrodynamics]]

### Optics Formula Sheet
See: [[physics/formula-sheet-optics]]

### Modern Physics Formula Sheet
See: [[physics/formula-sheet-modern]]

### Thermal & Waves Formula Sheet
See: [[physics/formula-sheet-thermal-waves]]

---

## 🔗 Cross-References

- **Mathematics:** Calculus (kinematics, fields, waves), Vectors (forces, fields), Complex numbers (AC, waves)
- **Chemistry:** Thermodynamics (chemical thermo), Electrochemistry (batteries), Solid state (crystals)
- **Quant Finance:** Random walks (diffusion), Stochastic calculus (Brownian motion)

---

## 📖 Source Registry

| Source File | Type | Topics Covered |
|-------------|------|----------------|
| `/raw-sources/Physics/Physics IIT/*.pdf` | Kota Notes | 17 chapters: AC, Calorimetry, Capacitor, Collision, Current, EMI, EM Waves, Errors, Electrostatics, Fluid, Gravitation, KTG, Kinematics, MEC, Rotational, Wave on String, Wave Optics |
| [[raw-sources/Physics/QUESTIONS FOR PRACTICE.pdf]] | Practice | Problem bank |
| [[raw-sources/Physics/Physics galazy Website.txt]] | Reference | Additional resources |

---

## 🎯 Study Strategy

1. **Mechanics:** Master vector approach, constraint relations, energy methods; practice rolling, collision, relative motion
2. **Electrodynamics:** Gauss's law applications, circuit analysis (Kirchhoff, Thevenin), EMI/AC phasors
3. **Optics:** Sign conventions, lens/mirror formula derivations, interference/diffraction conditions
4. **Modern:** Photoelectric, Bohr model, nuclear binding energy, semiconductor basics
5. **Thermal/Waves:** Process identification (PV diagrams), SHM energy method, Doppler cases

**High-Yield Topics (JEE Advanced 2020-2024):**
- Rotational motion (rolling, angular momentum, toppling)
- EMI (motional emf, inductance, LR/LC circuits)
- AC (resonance, power factor, transformers)
- Wave optics (YDSE, thin films, polarization)
- Modern: Photoelectric, radioactive decay, semiconductors
- Thermodynamics: Adiabatic processes, Carnot, entropy
- Fluid mechanics: Bernoulli, surface tension, viscosity

---

*Generated from raw-sources/Physics/ — Kota classroom notes and practice modules.*