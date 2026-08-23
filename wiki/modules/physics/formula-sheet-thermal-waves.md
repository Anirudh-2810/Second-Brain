---
module: "physics"
topic: "Physics Formula Sheet — Thermal & Waves (JEE Advanced)"
tags: [physics, thermal, waves, thermodynamics, kinetic, shm, sound, jee]
last_updated: "2026-08-11"
source: "Kota notes, standard references"
---

# Physics Formula Sheet — Thermal & Waves (JEE Advanced)

> Complete thermal physics, oscillations, and waves formula compendium.

---

## 📐 Thermodynamics

| Quantity | Formula |
|----------|---------|
| **Zeroth Law** | Thermal equilibrium: $T_A = T_B$, $T_B = T_C \implies T_A = T_C$ |
| **First Law** | $\Delta U = Q + W$; $W = -\int P dV$ (work done **on** system) |
| **Heat** | $Q = m c \Delta T$; $Q = m L$ (latent) |
| **Processes** | |
| Isothermal (ideal gas) | $PV = \text{const}$; $W = nRT \ln\frac{V_2}{V_1}$; $Q = -W$; $\Delta U = 0$ |
| Adiabatic | $PV^\gamma = \text{const}$; $TV^{\gamma-1} = \text{const}$; $T^\gamma P^{1-\gamma} = \text{const}$ |
| | $W = \frac{nR(T_1 - T_2)}{\gamma - 1} = \frac{P_1 V_1 - P_2 V_2}{\gamma - 1}$; $Q = 0$; $\Delta U = W$ |
| Isochoric | $W = 0$; $Q = nC_v \Delta T = \Delta U$ |
| Isobaric | $W = P \Delta V = nR \Delta T$; $Q = nC_p \Delta T$; $\Delta U = nC_v \Delta T$ |
| Cyclic | $\Delta U = 0$; $Q = -W$; $\oint P dV = -W$ (area in $PV$ diagram) |
| **Heat Capacities** | $C = \frac{Q}{\Delta T}$; $C_v = (\frac{\partial U}{\partial T})_V$; $C_p = (\frac{\partial H}{\partial T})_P$ |
| Ideal Gas | $C_p - C_v = R$; $\gamma = \frac{C_p}{C_v} = \frac{f+2}{f}$ |
| Degrees of Freedom | $f = 3$ (mono), $5$ (diatomic, RT), $7$ (diatomic, HT), $6$ (poly) |
| **Second Law** | Kelvin-Planck: No 100% efficient engine; Clausius: No self-acting fridge |
| **Carnot Engine** | $\eta = 1 - \frac{Q_2}{Q_1} = 1 - \frac{T_2}{T_1}$ (max possible) |
| Refrigerator/Heat Pump | $\beta = \frac{Q_2}{W} = \frac{T_2}{T_1 - T_2}$ (COP); $\beta_{HP} = \frac{Q_1}{W} = \frac{T_1}{T_1 - T_2}$ |
| **Entropy** | $dS = \frac{dQ_{rev}}{T}$; $\Delta S = \int \frac{dQ_{rev}}{T}$ |
| | Ideal gas: $\Delta S = nC_v \ln\frac{T_2}{T_1} + nR \ln\frac{V_2}{V_1}$ |
| | $\Delta S_{universe} \ge 0$ (equality for reversible) |
| **Thermodynamic Potentials** | $H = U + PV$; $F = U - TS$; $G = H - TS$ |
| Maxwell Relations | $(\frac{\partial T}{\partial V})_S = -(\frac{\partial P}{\partial S})_V$ etc. |

---

## 📐 Kinetic Theory of Gases

| Quantity | Formula |
|----------|---------|
| **Pressure** | $P = \frac{1}{3} \frac{N m \bar{v}^2}{V} = \frac{1}{3} \rho \bar{v}^2 = \frac{2}{3} \frac{N \bar{K}}{V}$ |
| **Ideal Gas Law** | $PV = N k_B T = nRT$; $R = 8.314$ J/mol·K; $k_B = 1.38 \times 10^{-23}$ J/K |
| **Speed Distribution** | |
| RMS Speed | $v_{rms} = \sqrt{\frac{3RT}{M}} = \sqrt{\frac{3k_B T}{m}}$ |
| Average Speed | $v_{avg} = \sqrt{\frac{8RT}{\pi M}} = \sqrt{\frac{8k_B T}{\pi m}}$ |
| Most Probable | $v_{mp} = \sqrt{\frac{2RT}{M}} = \sqrt{\frac{2k_B T}{m}}$ |
| Ratio | $v_{rms} : v_{avg} : v_{mp} = \sqrt{3} : \sqrt{8/\pi} : \sqrt{2} \approx 1.73 : 1.60 : 1.41$ |
| **Kinetic Energy** | $\bar{K} = \frac{1}{2} m \bar{v}^2 = \frac{3}{2} k_B T$ per molecule |
| **Internal Energy** | $U = \frac{f}{2} nRT$; $f$ = degrees of freedom |
| **Specific Heats** | $C_v = \frac{f}{2} R$; $C_p = C_v + R = \frac{f+2}{2} R$; $\gamma = \frac{C_p}{C_v} = \frac{f+2}{f}$ |
| **Maxwell-Boltzmann** | $f(v) = 4\pi (\frac{m}{2\pi k_B T})^{3/2} v^2 e^{-mv^2/2k_B T}$ |
| **Mean Free Path** | $\lambda = \frac{1}{\sqrt{2} \pi d^2 n}$; $d$ = molecular diameter |

---

## 📐 Heat Transfer

| Quantity | Formula |
|----------|---------|
| **Conduction** | $\frac{dQ}{dt} = \frac{k A \Delta T}{l}$; $k$ = thermal conductivity |
| Thermal Resistance | $R_{th} = \frac{l}{kA}$; Series: $R_{eq} = \sum R_i$; Parallel: $\frac{1}{R_{eq}} = \sum \frac{1}{R_i}$ |
| **Convection** | $\frac{dQ}{dt} = h A \Delta T$; $h$ = heat transfer coefficient |
| **Radiation (Stefan-Boltzmann)** | $\frac{dQ}{dt} = \sigma A e (T^4 - T_0^4)$; $\sigma = 5.67 \times 10^{-8}$ W/m²·K⁴ |
| Emissivity | $0 \le e \le 1$; Blackbody: $e=1$ |
| **Wien's Displacement** | $\lambda_{max} T = b$; $b = 2.898 \times 10^{-3}$ m·K |
| **Newton's Law of Cooling** | $\frac{dT}{dt} = -k(T - T_0)$; valid for small $\Delta T$ |
| **Thermal Conduction (Composite)** | $\frac{dQ}{dt} = \frac{\Delta T}{\sum R_{th}}$ |

---

## 📐 Calorimetry

| Quantity | Formula |
|----------|---------|
| **Heat Gained/Lost** | $Q = m c \Delta T$ (no phase change); $Q = m L$ (phase change) |
| **Mixing** | $m_1 c_1 (T_f - T_1) + m_2 c_2 (T_f - T_2) = 0$ (no loss) |
| **Phase Change** | $L_f$ (fusion), $L_v$ (vaporization); $Q = m L$ |
| **Ice-Water-Steam** | Ice $\to$ Water: $L_f = 80$ cal/g = 334 J/g; Water $\to$ Steam: $L_v = 540$ cal/g = 2260 J/g |

---

## 📐 Simple Harmonic Motion (SHM)

| Quantity | Formula |
|----------|---------|
| **Definition** | $F = -kx$; $a = -\omega^2 x$; $\omega = \sqrt{\frac{k}{m}}$ |
| **Displacement** | $x = A \sin(\omega t + \phi)$ or $A \cos(\omega t + \phi)$ |
| **Velocity** | $v = \omega \sqrt{A^2 - x^2}$; $v_{max} = A\omega$ at $x=0$ |
| **Acceleration** | $a = -\omega^2 x$; $a_{max} = A\omega^2$ at $x = \pm A$ |
| **Period & Frequency** | $T = \frac{2\pi}{\omega} = 2\pi \sqrt{\frac{m}{k}}$; $f = \frac{1}{T} = \frac{\omega}{2\pi}$ |
| **Energy** | $E = \frac{1}{2} k A^2 = \frac{1}{2} m \omega^2 A^2$ |
| | $K = \frac{1}{2} m v^2 = \frac{1}{2} m \omega^2 (A^2 - x^2)$ |
| | $U = \frac{1}{2} k x^2 = \frac{1}{2} m \omega^2 x^2$ |
| **Spring Combinations** | Series: $\frac{1}{k_{eq}} = \sum \frac{1}{k_i}$; Parallel: $k_{eq} = \sum k_i$ |
| **Pendulums** | |
| Simple | $T = 2\pi \sqrt{\frac{L}{g}}$; $\omega = \sqrt{\frac{g}{L}}$ (small $\theta$) |
| Physical | $T = 2\pi \sqrt{\frac{I}{mgd}}$; $d$ = distance from pivot to COM |
| Torsional | $T = 2\pi \sqrt{\frac{I}{\kappa}}$; $\kappa$ = torsion constant |
| **Superposition** | Same freq: $x = A_1 \sin(\omega t) + A_2 \sin(\omega t + \phi)$ |
| **Damped Oscillations** | $m\ddot{x} + b\dot{x} + kx = 0$ |
| Underdamped | $x = A_0 e^{-bt/2m} \sin(\omega' t + \phi)$; $\omega' = \sqrt{\omega_0^2 - (b/2m)^2}$ |
| Critical | $b = 2\sqrt{mk}$; $x = (A + Bt) e^{-bt/2m}$ |
| Overdamped | $x = A_1 e^{-\gamma_1 t} + A_2 e^{-\gamma_2 t}$ |
| **Forced Oscillations** | $m\ddot{x} + b\dot{x} + kx = F_0 \sin(\omega t)$ |
| Steady State | $x = A \sin(\omega t - \delta)$; $A = \frac{F_0/m}{\sqrt{(\omega_0^2 - \omega^2)^2 + (b\omega/m)^2}}$ |
| Resonance | $\omega_{res} = \sqrt{\omega_0^2 - \frac{b^2}{2m^2}}$ (amplitude); $\omega_0$ (velocity) |
| Quality Factor | $Q = \frac{\omega_0 m}{b} = \frac{\omega_0}{\Delta\omega}$ |

---

## 📐 Wave Motion

| Quantity | Formula |
|----------|---------|
| **Progressive Wave** | $y = A \sin(kx - \omega t + \phi)$ or $A \sin(\omega t - kx + \phi)$ |
| Wave Number | $k = \frac{2\pi}{\lambda}$ |
| Angular Frequency | $\omega = 2\pi f = \frac{2\pi}{T}$ |
| Wave Speed | $v = f\lambda = \frac{\omega}{k} = \sqrt{\frac{T}{\mu}}$ (string) |
| **Particle Velocity** | $v_p = \frac{\partial y}{\partial t} = -A\omega \cos(kx - \omega t + \phi)$ |
| **Intensity & Power** | $P = \frac{1}{2} \mu \omega^2 A^2 v$; $I = \frac{P}{A} = \frac{1}{2} \rho v \omega^2 A^2$ |
| **Superposition** | $y = y_1 + y_2$ |
| **Interference** | Constructive: $\Delta = n\lambda$; Destructive: $\Delta = (2n-1)\frac{\lambda}{2}$ |
| **Standing Waves** | $y = 2A \sin(kx) \cos(\omega t)$ |
| Nodes | $kx = n\pi \implies x = n\frac{\lambda}{2}$ |
| Antinodes | $kx = (2n+1)\frac{\pi}{2} \implies x = (2n+1)\frac{\lambda}{4}$ |
| **Reflection** | Fixed end: phase change $\pi$ (node); Free end: no phase change (antinode) |
| **String Fixed Both Ends** | $\lambda_n = \frac{2L}{n}$; $f_n = \frac{nv}{2L} = n f_1$ |
| **Pipes** | |
| Open Both Ends | $f_n = \frac{nv}{2L}$; $n = 1,2,3...$ |
| Closed One End | $f_n = \frac{(2n-1)v}{4L}$; $n = 1,2,3...$ |
| End Correction | $L_{eff} = L + 0.6r$ (open end) |

---

## 📐 Sound Waves

| Quantity | Formula |
|----------|---------|
| **Speed** | $v = \sqrt{\frac{B}{\rho}} = \sqrt{\frac{\gamma P}{\rho}} = \sqrt{\frac{\gamma RT}{M}}$ |
| | $v_{gas} \approx 331 \sqrt{1 + \frac{T}{273}}$ m/s ($T$ in °C) |
| **Intensity** | $I = \frac{P}{A} = \frac{1}{2} \rho v \omega^2 A^2$ |
| **Intensity Level** | $\beta = 10 \log_{10} \frac{I}{I_0}$ dB; $I_0 = 10^{-12}$ W/m² |
| **Beats** | $f_{beat} = |f_1 - f_2|$; $y = 2A \cos(2\pi \frac{f_1-f_2}{2}t) \sin(2\pi \frac{f_1+f_2}{2}t)$ |
| **Doppler Effect** | |
| Source Moving | $f' = f \frac{v}{v \mp v_s}$ ($-$ approaching, $+$ receding) |
| Observer Moving | $f' = f \frac{v \pm v_o}{v}$ ($+$ approaching, $-$ receding) |
| General | $f' = f \frac{v \pm v_o}{v \mp v_s}$ |
| **Shock Waves** | Mach Number: $M = \frac{v_s}{v}$; $M > 1$ supersonic |

---

*Thermal & Waves formula sheet — sign conventions: $W$ positive if done on system, $Q$ positive if added to system, $T$ in Kelvin, $\gamma = C_p/C_v$. Cross-reference with topic-wise notes for derivations.*