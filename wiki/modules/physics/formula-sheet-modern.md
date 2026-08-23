---
module: "physics"
topic: "Physics Formula Sheet — Modern Physics (JEE Advanced)"
tags: [physics, modern, formulas, jee, photoelectric, atomic, nuclear, semiconductor]
last_updated: "2026-08-11"
source: "Kota notes, standard references"
---

# Physics Formula Sheet — Modern Physics (JEE Advanced)

> Complete modern physics formula compendium. Photoelectric, atomic, nuclear, semiconductor, communication.

---

## 📐 Dual Nature (Photoelectric & Matter Waves)

| Quantity | Formula |
|----------|---------|
| **Photon** | |
| Energy | $E = h\nu = \frac{hc}{\lambda}$; $h = 6.626 \times 10^{-34}$ J·s; $hc = 1240$ eV·nm |
| Momentum | $p = \frac{h}{\lambda} = \frac{E}{c}$ |
| **Photoelectric Effect** | |
| Einstein Equation | $h\nu = \phi + K_{max}$; $K_{max} = eV_s$ |
| Work Function | $\phi = h\nu_0$ ($\nu_0$ = threshold frequency) |
| Stopping Potential | $eV_s = h\nu - \phi$; $V_s = \frac{h}{e}\nu - \frac{\phi}{e}$ |
| Intensity Effect | $I \propto$ number of photons; $K_{max}$ independent of $I$ |
| **de Broglie Wavelength** | |
| General | $\lambda = \frac{h}{p} = \frac{h}{mv} = \frac{h}{\sqrt{2mK}}$ |
| Accelerated by $V$ | $\lambda = \frac{h}{\sqrt{2meV}}$ (non-relativistic) |
| Electron (approx) | $\lambda (\text{nm}) = \frac{1.227}{\sqrt{V(\text{volts})}}$ |
| **Davisson-Germer** | $n\lambda = 2d \sin\theta$ (Bragg's law) |
| **Heisenberg Uncertainty** | $\Delta x \cdot \Delta p \ge \frac{h}{4\pi}$; $\Delta E \cdot \Delta t \ge \frac{h}{4\pi}$ |

---

## 📐 Atomic Physics (Bohr Model & Spectra)

| Quantity | Formula |
|----------|---------|
| **Bohr Model (Hydrogen-like)** | |
| Radius | $r_n = \frac{n^2}{Z} a_0$; $a_0 = 0.529$ Å |
| Velocity | $v_n = \frac{Z e^2}{2\epsilon_0 h n} = \frac{Z \alpha c}{n}$; $\alpha = \frac{1}{137}$ |
| Energy | $E_n = -\frac{13.6 Z^2}{n^2}$ eV; $E_n = -\frac{m e^4}{8\epsilon_0^2 h^2} \frac{Z^2}{n^2}$ |
| Angular Momentum | $L_n = n \frac{h}{2\pi} = n \hbar$ |
| **Transitions** | |
| Wavelength | $\frac{1}{\lambda} = R Z^2 (\frac{1}{n_1^2} - \frac{1}{n_2^2})$; $R = 1.097 \times 10^7$ m⁻¹ |
| Energy | $\Delta E = 13.6 Z^2 (\frac{1}{n_1^2} - \frac{1}{n_2^2})$ eV |
| Photon Energy | $E_{photon} = E_i - E_f$ |
| **Spectral Series** | |
| Lyman | $n_1 = 1$ (UV) |
| Balmer | $n_1 = 2$ (Visible) |
| Paschen | $n_1 = 3$ (IR) |
| Brackett | $n_1 = 4$ (IR) |
| Pfund | $n_1 = 5$ (IR) |
| **Reduced Mass Correction** | $R_M = \frac{R_\infty}{1 + m_e/M_{nuc}}$ |

---

## 📐 Nuclear Physics

| Quantity | Formula |
|----------|---------|
| **Nuclear Radius** | $R = R_0 A^{1/3}$; $R_0 \approx 1.2$ fm |
| **Mass Defect** | $\Delta m = [Z m_p + (A-Z) m_n] - M_{nuc}$ |
| **Binding Energy** | $B = \Delta m c^2$; $B/A$ = binding energy per nucleon |
| **Radioactivity** | |
| Decay Law | $N = N_0 e^{-\lambda t}$; $\frac{dN}{dt} = -\lambda N$ |
| Activity | $A = -\frac{dN}{dt} = \lambda N = A_0 e^{-\lambda t}$ |
| Half-Life | $T_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.693}{\lambda}$ |
| Mean Life | $\tau = \frac{1}{\lambda} = 1.44 T_{1/2}$ |
| **Decay Modes** | |
| $\alpha$-decay | $^A_Z X \to ^{A-4}_{Z-2} Y + ^4_2 \alpha$; $Q = (M_X - M_Y - M_\alpha)c^2$ |
| $\beta^-$-decay | $n \to p + e^- + \bar{\nu}_e$; $^A_Z X \to ^A_{Z+1} Y + e^- + \bar{\nu}_e$ |
| $\beta^+$-decay | $p \to n + e^+ + \nu_e$; $^A_Z X \to ^A_{Z-1} Y + e^+ + \nu_e$ |
| Electron Capture | $p + e^- \to n + \nu_e$; $^A_Z X + e^- \to ^A_{Z-1} Y + \nu_e$ |
| $\gamma$-decay | $^A_Z X^* \to ^A_Z X + \gamma$ |
| **Nuclear Reactions** | |
| Fission | $^{235}_{92}U + n \to$ fragments + $2-3 n$ + $\sim 200$ MeV |
| Fusion | Light nuclei $\to$ heavier + energy (e.g., $4p \to ^4He + 2e^+ + 2\nu_e + 26.7$ MeV) |

---

## 📐 Semiconductor Devices

| Quantity | Formula |
|----------|---------|
| **Energy Bands** | |
| Intrinsic Carrier | $n_i^2 = n_e n_h$; $n_i \propto T^{3/2} e^{-E_g/2kT}$ |
| Doping | $n$-type: $n_e \approx N_D$, $n_h = n_i^2/N_D$; $p$-type: $n_h \approx N_A$, $n_e = n_i^2/N_A$ |
| Mass Action | $n_e n_h = n_i^2$ (thermal equilibrium) |
| **p-n Junction** | |
| Built-in Potential | $V_{bi} = \frac{kT}{e} \ln\frac{N_A N_D}{n_i^2}$ |
| Depletion Width | $W = \sqrt{\frac{2\epsilon}{e}(\frac{1}{N_A} + \frac{1}{N_D})(V_{bi} + V_R)}$ |
| **Diode Equation** | $I = I_0(e^{eV/kT} - 1)$; $I_0 = A e n_i^2 (\frac{D_n}{L_n N_A} + \frac{D_p}{L_p N_D})$ |
| Forward Bias ($V \gg kT/e$) | $I \approx I_0 e^{eV/kT}$ |
| Reverse Bias | $I \approx -I_0$ (saturation current) |
| **Zener Diode** | Breakdown at $V_Z$ (Zener < 5V: tunneling; > 5V: avalanche) |
| **Rectifiers** | |
| Half-Wave | $V_{dc} = \frac{V_m}{\pi}$; $\eta = 40.6\%$; Ripple factor $= 1.21$ |
| Full-Wave (Center-tap) | $V_{dc} = \frac{2V_m}{\pi}$; $\eta = 81.2\%$; Ripple factor $= 0.48$ |
| Bridge | Same as full-wave; no center-tap needed |
| **Transistor (BJT)** | |
| $\alpha = \frac{I_C}{I_E}$; $\beta = \frac{I_C}{I_B} = \frac{\alpha}{1-\alpha}$ |
| $I_C = \beta I_B + (1+\beta)I_{CBO}$; $I_E = I_C + I_B$ |
| **MOSFET** | $I_D = K(V_{GS} - V_{th})^2$ (saturation); $g_m = \frac{\partial I_D}{\partial V_{GS}} = 2K(V_{GS} - V_{th})$ |
| **Logic Gates** | |
| NOT | $\overline{A}$ |
| AND | $A \cdot B$ |
| OR | $A + B$ |
| NAND | $\overline{A \cdot B}$ (universal) |
| NOR | $\overline{A + B}$ (universal) |
| XOR | $A \oplus B = A\overline{B} + \overline{A}B$ |
| XNOR | $\overline{A \oplus B} = AB + \overline{A}\overline{B}$ |

---

## 📐 Communication Systems

| Quantity | Formula |
|----------|---------|
| **Modulation** | |
| AM Signal | $s(t) = A_c[1 + m \cos(\omega_m t)] \cos(\omega_c t)$ |
| Modulation Index | $m = \frac{A_m}{A_c}$ ($0 \le m \le 1$) |
| AM Spectrum | $\omega_c$, $\omega_c \pm \omega_m$; Bandwidth $= 2 f_m$ |
| FM Signal | $s(t) = A_c \cos(\omega_c t + \beta \sin \omega_m t)$ |
| FM Index | $\beta = \frac{\Delta f}{f_m}$ |
| FM Bandwidth (Carson) | $BW \approx 2(\Delta f + f_m) = 2 f_m(\beta + 1)$ |
| **Propagation** | |
| Ground Wave | $< 2$ MHz; follows Earth curvature |
| Sky Wave | $2-30$ MHz; ionospheric reflection; critical freq $f_c = 9\sqrt{N_{max}}$ |
| Space Wave | $> 30$ MHz; LOS; $d = \sqrt{2Rh_t} + \sqrt{2Rh_r}$ |
| Satellite | Geostationary: $h \approx 36000$ km |

---

*Modern Physics formula sheet — constants: $h=6.626\times10^{-34}$ J·s, $c=3\times10^8$ m/s, $e=1.6\times10^{-19}$ C, $m_e=9.1\times10^{-31}$ kg, $k=1.38\times10^{-23}$ J/K. Cross-reference with topic-wise notes for derivations.*