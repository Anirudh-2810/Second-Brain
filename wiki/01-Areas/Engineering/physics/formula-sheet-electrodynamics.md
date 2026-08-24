---
module: "physics"
topic: "Physics Formula Sheet — Electrodynamics (JEE Advanced)"
tags: [physics, electrodynamics, formulas, jee, electrostatics, current, magnetism, emi, ac]
last_updated: "2026-08-11"
source: "Kota notes, standard references"
---

# Physics Formula Sheet — Electrodynamics (JEE Advanced)

> Complete electrodynamics formula compendium. Every formula with conditions and sign conventions.

---

## 📐 Electrostatics

| Quantity | Formula |
|----------|---------|
| **Coulomb's Law** | $F = \frac{1}{4\pi\epsilon_0} \frac{q_1 q_2}{r^2}$; $\frac{1}{4\pi\epsilon_0} = 9 \times 10^9$ N·m²/C² |
| **Electric Field** | $\vec{E} = \frac{\vec{F}}{q_0}$; Point charge: $E = \frac{kq}{r^2}$ (radial) |
| **Superposition** | $\vec{E}_{net} = \sum \vec{E}_i$; $V_{net} = \sum V_i$ |
| **Field from Distributions** | |
| Infinite line ($\lambda$) | $E = \frac{\lambda}{2\pi\epsilon_0 r}$ (radial) |
| Infinite plane ($\sigma$) | $E = \frac{\sigma}{2\epsilon_0}$ (perp to plane) |
| Ring (axis) | $E = \frac{kQx}{(R^2+x^2)^{3/2}}$ |
| Disc (axis) | $E = \frac{\sigma}{2\epsilon_0}[1 - \frac{x}{\sqrt{R^2+x^2}}]$ |
| Sphere (outside) | $E = \frac{kQ}{r^2}$; Inside conductor: $E=0$ |
| **Potential** | $V = \frac{W}{q} = \frac{kq}{r}$; $V = -\int \vec{E} \cdot d\vec{l}$ |
| Point charge | $V = \frac{kq}{r}$ |
| Dipole | $V = \frac{kp \cos\theta}{r^2}$ |
| **Dipole** | $\vec{p} = q \vec{d}$ (from -q to +q) |
| Dipole field (axial) | $E = \frac{2kp}{r^3}$ (along $\vec{p}$) |
| Dipole field (equatorial) | $E = \frac{kp}{r^3}$ (opp to $\vec{p}$) |
| Torque | $\vec{\tau} = \vec{p} \times \vec{E}$; $\tau = pE \sin\theta$ |
| Potential energy | $U = -\vec{p} \cdot \vec{E} = -pE \cos\theta$ |
| **Gauss's Law** | $\oint \vec{E} \cdot d\vec{A} = \frac{Q_{enc}}{\epsilon_0}$ |
| **Applications** | |
| Infinite line | $E = \frac{\lambda}{2\pi\epsilon_0 r}$ |
| Infinite plane | $E = \frac{\sigma}{2\epsilon_0}$ |
| Conducting sphere | Outside: $E = \frac{kQ}{r^2}$; Inside: $E=0$ |
| Non-conducting sphere (uniform $\rho$) | Inside: $E = \frac{\rho r}{3\epsilon_0} = \frac{kQr}{R^3}$ |
| **Electrostatic Energy** | $U = \frac{1}{2} \int \rho V d\tau = \frac{1}{2} \sum q_i V_i = \frac{1}{2} C V^2$ |
| Energy density | $u = \frac{1}{2} \epsilon_0 E^2$ |

---

## 📐 Capacitors

| Quantity | Formula |
|----------|---------|
| **Definition** | $C = \frac{Q}{V}$ |
| **Parallel Plate** | $C = \frac{\epsilon_0 A}{d}$; With dielectric: $C = \frac{K \epsilon_0 A}{d}$ |
| **Spherical** | $C = 4\pi\epsilon_0 \frac{ab}{b-a}$ (inner $a$, outer $b$) |
| **Cylindrical** | $C = \frac{2\pi\epsilon_0 L}{\ln(b/a)}$ |
| **Combinations** | Series: $\frac{1}{C_{eq}} = \sum \frac{1}{C_i}$; $Q$ same; Parallel: $C_{eq} = \sum C_i$; $V$ same |
| **Dielectric** | Partial filling: treat as series/parallel of dielectric/air gaps |
| **Energy** | $U = \frac{1}{2} C V^2 = \frac{Q^2}{2C} = \frac{1}{2} Q V$ |
| Energy density | $u = \frac{1}{2} \epsilon_0 E^2 = \frac{1}{2} \epsilon E^2 = \frac{1}{2} \frac{Q^2}{\epsilon_0^2 A^2}$ |
| **Charging (RC)** | $q = Q_0(1 - e^{-t/RC})$; $I = \frac{Q_0}{RC} e^{-t/RC} = I_0 e^{-t/RC}$ |
| **Discharging (RC)** | $q = Q_0 e^{-t/RC}$; $I = -\frac{Q_0}{RC} e^{-t/RC}$ |
| **Time Constant** | $\tau = RC$; $t = \tau \ln 2$ for half charge |
| **Force between plates** | $F = \frac{Q^2}{2\epsilon_0 A} = \frac{1}{2} C V^2 / d$ |

---

## 📐 Current Electricity

| Quantity | Formula |
|----------|---------|
| **Current** | $I = \frac{dq}{dt}$; $I = n e A v_d$ |
| **Current Density** | $\vec{J} = \frac{I}{A} \hat{n} = \sigma \vec{E} = \frac{\vec{E}}{\rho}$ |
| **Ohm's Law** | $V = IR$; $\vec{J} = \sigma \vec{E}$ |
| **Resistance** | $R = \rho \frac{l}{A}$; $\rho = \rho_0[1 + \alpha(T-T_0)]$ |
| **Power** | $P = VI = I^2R = \frac{V^2}{R}$ |
| **Series** | $R_{eq} = \sum R_i$; $I$ same; $V$ divides |
| **Parallel** | $\frac{1}{R_{eq}} = \sum \frac{1}{R_i}$; $V$ same; $I$ divides |
| **Kirchhoff's Laws** | Junction: $\sum I = 0$; Loop: $\sum V = 0$ |
| **Wheatstone Bridge** | Balanced: $\frac{P}{Q} = \frac{R}{S}$; $I_{galvo} = 0$ |
| **Meter Bridge** | $\frac{R}{S} = \frac{l_1}{l_2}$ (balanced) |
| **Potentiometer** | $\frac{E_1}{E_2} = \frac{l_1}{l_2}$; Internal $r$: $r = R(\frac{l_1 - l_2}{l_2})$ |
| **Cells** | Series: $E_{eq} = \sum E_i$; $r_{eq} = \sum r_i$; Parallel: $E_{eq} = \frac{\sum E_i/r_i}{\sum 1/r_i}$; $\frac{1}{r_{eq}} = \sum \frac{1}{r_i}$ |
| **Charging a Capacitor** | $q = C E (1 - e^{-t/RC})$; $V_c = E(1 - e^{-t/RC})$ |

---

## 📐 Magnetic Effects of Current

| Quantity | Formula |
|----------|---------|
| **Biot-Savart** | $d\vec{B} = \frac{\mu_0}{4\pi} \frac{I d\vec{l} \times \hat{r}}{r^2}$ |
| **Straight Wire** | $B = \frac{\mu_0 I}{2\pi r}$ (circular around wire) |
| **Circular Loop** | Center: $B = \frac{\mu_0 I}{2R}$; Axis: $B = \frac{\mu_0 I R^2}{2(R^2+x^2)^{3/2}}$ |
| **Arc** | $B = \frac{\mu_0 I \theta}{4\pi R}$ |
| **Solenoid** | Inside: $B = \mu_0 n I$; End: $B = \frac{1}{2} \mu_0 n I$ |
| **Toroid** | $B = \frac{\mu_0 N I}{2\pi r}$ (inside); $B=0$ (outside) |
| **Ampere's Law** | $\oint \vec{B} \cdot d\vec{l} = \mu_0 I_{enc}$ |
| **Force on Charge** | $\vec{F} = q(\vec{v} \times \vec{B})$; $F = qvB \sin\theta$ |
| Circular Motion | $r = \frac{mv}{qB}$; $T = \frac{2\pi m}{qB}$; $f = \frac{qB}{2\pi m}$ |
| Helical Motion | $r = \frac{mv_\perp}{qB}$; Pitch $= v_\parallel T = \frac{2\pi m v_\parallel}{qB}$ |
| **Force on Wire** | $\vec{F} = I(\vec{l} \times \vec{B})$; $F = BIl \sin\theta$ |
| Force between wires | $F = \frac{\mu_0 I_1 I_2 l}{2\pi d}$ (attract if parallel, repel if anti-parallel) |
| **Torque on Loop** | $\vec{\tau} = \vec{\mu} \times \vec{B}$; $\mu = I \vec{A}$; $\tau = \mu B \sin\theta$ |
| **Magnetic Materials** | $\vec{M} = \chi \vec{H}$; $\vec{B} = \mu_0(\vec{H} + \vec{M}) = \mu_0(1+\chi)\vec{H} = \mu \vec{H}$ |
| Diamagnetic | $\chi < 0$, $\mu_r < 1$ |
| Paramagnetic | $\chi > 0$ small, $\mu_r > 1$ |
| Ferromagnetic | $\chi \gg 0$, $\mu_r \gg 1$, hysteresis |

---

## 📐 Electromagnetic Induction (EMI)

| Quantity | Formula |
|----------|---------|
| **Faraday's Law** | $\mathcal{E} = -\frac{d\Phi}{dt}$; $\Phi = \int \vec{B} \cdot d\vec{A} = BA \cos\theta$ |
| **Lenz's Law** | Induced current opposes change in flux |
| **Motional EMF** | $\mathcal{E} = B l v$ (perpendicular); $\mathcal{E} = \int (\vec{v} \times \vec{B}) \cdot d\vec{l}$ |
| Rotating Rod | $\mathcal{E} = \frac{1}{2} B \omega l^2$ |
| **Self-Inductance** | $\Phi = L I$; $\mathcal{E} = -L \frac{dI}{dt}$; $L = \frac{\mu_0 N^2 A}{l}$ (solenoid) |
| **Mutual Inductance** | $\Phi_2 = M I_1$; $\mathcal{E}_2 = -M \frac{dI_1}{dt}$; $M_{12} = M_{21}$ |
| **Inductor Combinations** | Series: $L_{eq} = L_1 + L_2 \pm 2M$; Parallel: $\frac{1}{L_{eq}} = \frac{1}{L_1} + \frac{1}{L_2} \mp \frac{2M}{L_1 L_2}$ |
| **Energy** | $U = \frac{1}{2} L I^2$; Energy density $u = \frac{B^2}{2\mu_0}$ |
| **LR Circuit** | Charging: $I = I_0(1 - e^{-t/\tau})$; $\tau = L/R$; Decay: $I = I_0 e^{-t/\tau}$ |
| **LC Oscillations** | $\omega = \frac{1}{\sqrt{LC}}$; $Q = Q_0 \cos(\omega t + \phi)$; $I = -\omega Q_0 \sin(\omega t + \phi)$ |
| Energy | $U = \frac{Q^2}{2C} + \frac{1}{2} L I^2 = \text{const}$ |

---

## 📐 Alternating Current (AC)

| Quantity | Formula |
|----------|---------|
| **Instantaneous** | $i = I_0 \sin(\omega t)$; $v = V_0 \sin(\omega t)$; $\omega = 2\pi f = \frac{2\pi}{T}$ |
| **RMS Values** | $I_{rms} = \frac{I_0}{\sqrt{2}}$; $V_{rms} = \frac{V_0}{\sqrt{2}}$ |
| **Reactance** | $X_L = \omega L$; $X_C = \frac{1}{\omega C}$ |
| **Impedance** | $Z = \sqrt{R^2 + (X_L - X_C)^2}$; $\tan\phi = \frac{X_L - X_C}{R}$ |
| **Phasor** | $V_R$ in phase with $I$; $V_L$ leads $I$ by $90^\circ$; $V_C$ lags $I$ by $90^\circ$ |
| **Resonance** | $X_L = X_C \implies \omega_0 = \frac{1}{\sqrt{LC}}$; $f_0 = \frac{1}{2\pi\sqrt{LC}}$ |
| At Resonance | $Z_{min} = R$; $I_{max} = V/R$; $\phi = 0$; $V_L = V_C = Q V$ |
| **Quality Factor** | $Q = \frac{\omega_0 L}{R} = \frac{1}{\omega_0 C R} = \frac{\omega_0}{\Delta\omega}$ |
| **Power** | Instantaneous: $p = vi$; Average: $P_{avg} = V_{rms} I_{rms} \cos\phi = I_{rms}^2 R$ |
| Power Factor | $\cos\phi = \frac{R}{Z}$; $P_{avg} = V_{rms} I_{rms} \cos\phi$ |
| **Transformer** | $\frac{V_s}{V_p} = \frac{N_s}{N_p} = \frac{I_p}{I_s}$ (ideal); $\eta = \frac{P_{out}}{P_{in}}$ |
| **AC Instruments** | Moving iron: measures RMS; Moving coil (PMMC): measures average (DC only) |

---

## 📐 Electromagnetic Waves

| Quantity | Formula |
|----------|---------|
| **Speed** | $c = \frac{1}{\sqrt{\mu_0 \epsilon_0}} = 3 \times 10^8$ m/s |
| **Wave Equation** | $\frac{\partial^2 E}{\partial x^2} = \mu_0 \epsilon_0 \frac{\partial^2 E}{\partial t^2}$ |
| **Fields** | $\vec{E} = E_0 \sin(kx - \omega t) \hat{j}$; $\vec{B} = B_0 \sin(kx - \omega t) \hat{k}$ |
| **Relation** | $E_0 = c B_0$; $\frac{E}{B} = c$; $\vec{E} \times \vec{B}$ along propagation |
| **Intensity** | $I = \frac{1}{2} \epsilon_0 E_0^2 c = \frac{E_0 B_0}{2\mu_0} = \frac{c B_0^2}{2\mu_0}$ |
| **Radiation Pressure** | Absorbing: $P = \frac{I}{c}$; Reflecting: $P = \frac{2I}{c}$ |
| **Poynting Vector** | $\vec{S} = \frac{1}{\mu_0} \vec{E} \times \vec{B}$; $I = \langle S \rangle$ |
| **Spectrum** | $\gamma$-ray < X-ray < UV < Visible < IR < Microwave < Radio |

---

*Electrodynamics formula sheet — sign conventions: $\vec{E}$ from + to -, $\vec{B}$ from N to S outside magnet, current direction = positive charge flow. Cross-reference with topic-wise notes for derivations.*