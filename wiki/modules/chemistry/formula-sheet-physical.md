---
module: "chemistry"
topic: "Physical Chemistry Formula Sheet — Complete Reference (JEE Advanced)"
tags: [chemistry, physical, formulas, jee, thermodynamics, kinetics, electrochemistry]
last_updated: "2026-08-11"
source: "Kota notes, standard references"
---

# Physical Chemistry Formula Sheet — Complete Reference

> Every formula for Physical Chemistry JEE Advanced in one place. Memorize derivations for key formulas, results for others.

---

## 📐 Thermodynamics

| Quantity | Formula | Conditions |
|----------|---------|------------|
| **Work** | $w = -\int P_{ext} dV$ | General |
| **Reversible Isothermal** | $w = -nRT \ln\frac{V_2}{V_1} = -nRT \ln\frac{P_1}{P_2}$ | Ideal gas, isothermal |
| **Reversible Adiabatic** | $w = \frac{nR(T_2-T_1)}{1-\gamma}$; $TV^{\gamma-1} = \text{const}$ | $\gamma = C_p/C_v$ |
| **1st Law** | $\Delta U = q + w$ | Always |
| **Enthalpy** | $H = U + PV$; $\Delta H = \Delta U + \Delta n_g RT$ | |
| **Heat Capacity** | $C = \frac{q}{\Delta T}$; $C_p - C_v = R$ (ideal gas) | |
| **Hess's Law** | $\Delta H_{rxn} = \sum \Delta H_f(products) - \sum \Delta H_f(reactants)$ | |
| **Kirchhoff** | $\Delta H_2 - \Delta H_1 = \int_{T_1}^{T_2} \Delta C_p dT$ | |
| **Entropy** | $\Delta S = \int \frac{dq_{rev}}{T}$; $\Delta S = nC_p \ln\frac{T_2}{T_1} - nR \ln\frac{P_2}{P_1}$ | |
| **Gibbs Free Energy** | $G = H - TS$; $\Delta G = \Delta H - T\Delta S$ | |
| **Spontaneity** | $\Delta G < 0$ spontaneous; $\Delta G = 0$ equilibrium; $\Delta G > 0$ non-spontaneous | |
| $\Delta G^\circ$ | $\Delta G^\circ = -RT \ln K = -2.303 RT \log K$ | |
| **van't Hoff** | $\ln\frac{K_2}{K_1} = -\frac{\Delta H^\circ}{R}(\frac{1}{T_2} - \frac{1}{T_1})$ | |
| **Clapeyron** | $\frac{dP}{dT} = \frac{\Delta H}{T \Delta V}$ | Phase equilibrium |
| **Clausius-Clapeyron** | $\ln\frac{P_2}{P_1} = \frac{\Delta H_{vap}}{R}(\frac{1}{T_1} - \frac{1}{T_2})$ | Liquid-vapor |

---

## 📐 Chemical Equilibrium

| Quantity | Formula |
|----------|---------|
| $K_c$ | $\frac{[C]^c[D]^d}{[A]^a[B]^b}$ |
| $K_p$ | $K_c (RT)^{\Delta n_g}$ |
| $K_x$ | $K_p P^{\Delta n_g}$ (mole fraction) |
| Reaction Quotient | $Q = \frac{[C]^c[D]^d}{[A]^a[B]^b}$ (same form, initial conc) |
| Direction | $Q < K$: forward; $Q > K$: reverse; $Q = K$: equilibrium |
| Le Chatelier | $\Delta n_g > 0$: $\uparrow P \to$ reverse; $\Delta H > 0$: $\uparrow T \to$ forward |

---

## 📐 Ionic Equilibrium

| Quantity | Formula |
|----------|---------|
| $pH$ | $-\log[H^+]$ |
| $pOH$ | $-\log[OH^-]$ |
| $K_w$ | $[H^+][OH^-] = 10^{-14}$ (25°C) |
| $pH + pOH$ | $14$ |
| Weak Acid | $[H^+] = \sqrt{K_a C}$ ($C/K_a > 400$) |
| Weak Base | $[OH^-] = \sqrt{K_b C}$ |
| $K_a \times K_b$ | $K_w$ (conjugate pair) |
| Buffer (Acidic) | $pH = pK_a + \log\frac{[Salt]}{[Acid]}$ |
| Buffer (Basic) | $pOH = pK_b + \log\frac{[Salt]}{[Base]}$ |
| Hydrolysis | $K_h = K_w/K_a$ (salt of WA+SB), $K_h = K_w/K_b$ (SA+WB) |
| $K_{sp}$ | $[M^{n+}]^m [X^{m-}]^n$ |
| Precipitation | Ionic Product $> K_{sp} \to$ ppt forms |
| Common Ion | $[H^+] = \sqrt{K_a \frac{C_{acid}}{C_{salt}}}$ (approx) |

---

## 📐 Electrochemistry

| Quantity | Formula |
|----------|---------|
| Conductivity | $\kappa = \frac{1}{\rho} = \frac{G \cdot l}{A}$ (S cm⁻¹) |
| Molar Conductivity | $\Lambda_m = \frac{\kappa \times 1000}{C}$ (S cm² mol⁻¹) |
| Kohlrausch | $\Lambda_m = \Lambda_m^\circ - K\sqrt{C}$ (strong); $\Lambda_m = \alpha \Lambda_m^\circ$ (weak) |
| $\Lambda_m^\circ$ | $\Lambda_m^\circ = \nu_+ \lambda_+^\circ + \nu_- \lambda_-^\circ$ |
| Degree of Dissoc. | $\alpha = \frac{\Lambda_m}{\Lambda_m^\circ}$ (weak electrolyte) |
| $E_{cell}$ | $E_{cathode} - E_{anode} = E_{RP} - E_{RP}$ (both reduction) |
| Nernst (25°C) | $E = E^\circ - \frac{0.0591}{n} \log Q$ |
| $E^\circ_{cell}$ | $E^\circ_{cathode} - E^\circ_{anode}$ |
| $\Delta G$ | $\Delta G = -nFE_{cell}$; $\Delta G^\circ = -nFE^\circ_{cell}$ |
| $\Delta G^\circ$ | $-RT \ln K = -2.303 RT \log K$ |
| Faraday's Laws | $m = ZIt$; $Z = \frac{M}{nF}$; $F = 96485$ C mol⁻¹ |
| Concentration Cell | $E = \frac{0.0591}{n} \log\frac{C_2}{C_1}$ |

---

## 📐 Chemical Kinetics

| Quantity | Formula |
|----------|---------|
| Rate | $-\frac{1}{a}\frac{d[A]}{dt} = \frac{1}{b}\frac{d[B]}{dt} = k[A]^x[B]^y$ |
| Order | $n = x + y$ |
| Zero Order | $[A] = [A]_0 - kt$; $t_{1/2} = \frac{[A]_0}{2k}$ |
| 1st Order | $\ln\frac{[A]_0}{[A]} = kt$; $t_{1/2} = \frac{0.693}{k}$ |
| 2nd Order (1 reactant) | $\frac{1}{[A]} - \frac{1}{[A]_0} = kt$; $t_{1/2} = \frac{1}{k[A]_0}$ |
| n-th Order | $\frac{1}{[A]^{n-1}} - \frac{1}{[A]_0^{n-1}} = (n-1)kt$ |
| Arrhenius | $k = A e^{-E_a/RT}$; $\ln\frac{k_2}{k_1} = \frac{E_a}{R}(\frac{1}{T_1} - \frac{1}{T_2})$ |
| Activation Energy | $E_a = RT^2 \frac{d\ln k}{dT}$ |
| Catalyst | Lowers $E_a$; increases $k$; doesn't change $\Delta G$ or $K$ |

---

## 📐 States of Matter

| Quantity | Formula |
|----------|---------|
| Ideal Gas | $PV = nRT$ |
| Dalton's Law | $P_{total} = \sum P_i$; $P_i = x_i P_{total}$ |
| Graham's Law | $\frac{r_1}{r_2} = \sqrt{\frac{M_2}{M_1}}$ |
| Kinetic Theory | $PV = \frac{1}{3} m n \bar{c}^2$; $KE_{avg} = \frac{3}{2} RT$ |
| rms Speed | $u_{rms} = \sqrt{\frac{3RT}{M}}$ |
| Average Speed | $u_{avg} = \sqrt{\frac{8RT}{\pi M}}$ |
| Most Probable | $u_{mp} = \sqrt{\frac{2RT}{M}}$ |
| van der Waals | $(P + \frac{an^2}{V^2})(V - nb) = nRT$ |
| Critical Constants | $V_c = 3b$; $P_c = \frac{a}{27b^2}$; $T_c = \frac{8a}{27Rb}$ |
| Compressibility | $Z = \frac{PV}{nRT}$; $Z=1$ (ideal), $Z<1$ (attractive), $Z>1$ (repulsive) |

---

## 📐 Solid State

| Quantity | Formula |
|----------|---------|
| Density | $\rho = \frac{Z \cdot M}{N_A \cdot a^3}$ |
| Packing Efficiency | FCC/CCP/HCP = 74%; BCC = 68%; SC = 52.4% |
| Coordination Number | FCC = 12; BCC = 8; SC = 6 |
| Octahedral Void | $r_{void} = 0.414 r_{atom}$ |
| Tetrahedral Void | $r_{void} = 0.225 r_{atom}$ |
| Radius Ratio Rules | CN=3: 0.155-0.225; CN=4: 0.225-0.414; CN=6: 0.414-0.732; CN=8: 0.732-1.0 |
| Bragg's Law | $n\lambda = 2d\sin\theta$ |

---

## 📐 Solutions

| Quantity | Formula |
|----------|---------|
| Molality ($m$) | $\frac{n_{solute}}{kg_{solvent}}$ |
| Molarity ($M$) | $\frac{n_{solute}}{L_{solution}}$ |
| Mole Fraction ($x$) | $\frac{n_i}{n_{total}}$ |
| Normality ($N$) | $\frac{eq_{solute}}{L_{solution}}$ |
| Raoult's Law | $P_A = x_A P_A^\circ$ |
| $\Delta P/P^\circ$ | $x_B$ (solute mole fraction) |
| $\Delta T_b$ | $i K_b m$ |
| $\Delta T_f$ | $i K_f m$ |
| Osmotic Pressure ($\Pi$) | $i CRT$ |
| van't Hoff ($i$) | $i = \frac{\text{observed}}{\text{theoretical (no dissociation)}}$ |
| $i = 1 + \alpha(n-1)$ | Dissociation: $AB \to A^+ + B^-$ ($n=2$) |
| $i = 1 - \alpha(1-1/n)$ | Association: $n A \to A_n$ |

---

## 📐 Surface Chemistry

| Quantity | Formula |
|----------|---------|
| Langmuir | $\frac{x}{m} = \frac{a k P}{1 + k P}$ or $\frac{P}{x/m} = \frac{1}{ak} + \frac{P}{a}$ |
| Freundlich | $\frac{x}{m} = k P^{1/n}$; $\log\frac{x}{m} = \log k + \frac{1}{n}\log P$ |
| BET (Multilayer) | $\frac{P}{V(P_0-P)} = \frac{1}{V_m C} + \frac{C-1}{V_m C}\frac{P}{P_0}$ |

---

## 📐 Atomic Structure

| Quantity | Formula |
|----------|---------|
| de Broglie | $\lambda = \frac{h}{p} = \frac{h}{mv}$ |
| Heisenberg | $\Delta x \cdot \Delta p \ge \frac{h}{4\pi}$ |
| Bohr Model | $r_n = n^2 a_0$ ($a_0 = 0.529$ Å) |
| Energy | $E_n = -\frac{13.6 Z^2}{n^2}$ eV |
| Rydberg | $\frac{1}{\lambda} = R Z^2 (\frac{1}{n_1^2} - \frac{1}{n_2^2})$ |
| Quantum Numbers | $n=1,2,...$; $l=0...n-1$; $m=-l...+l$; $s=\pm 1/2$ |
| Nodes | Radial: $n-l-1$; Angular: $l$; Total: $n-1$ |
| Magnetic Moment | $\mu = \sqrt{n(n+2)}$ BM |

---

## 📐 Chemical Bonding

| Quantity | Formula |
|----------|---------|
| Bond Order (MOT) | $\frac{N_b - N_a}{2}$ |
| Dipole Moment | $\mu = q \times d$ (Debye); $1 D = 3.33 \times 10^{-30}$ C m |
| % Ionic Character | $16|\chi_A - \chi_B| + 3.5|\chi_A - \chi_B|^2$ (Hannay-Smith) |
| Fajan's Rules | High charge + small cation + large anion $\to$ covalent |

---

*Physical Chemistry formula sheet — keep for quick revision. Cross-reference with topic-wise notes for derivations.*