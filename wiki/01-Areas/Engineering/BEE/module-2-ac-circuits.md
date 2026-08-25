---
course_code: "BEE"
course_name: "Basic Electrical Engineering"
unit: "Module 2 — AC Circuits"
tags: [bee, ac-circuits, phasor, impedance, resonance, power-factor]
last_updated: "2026-08-25"
confidence: "high"
---

## For future agent
Module 2 of BEE (MU pattern): single-phase AC circuits — sinusoids, phasors, R-L-C combinations, power and resonance. Complex-number fluency is assumed from [[modules/../01-Areas/Engineering/engineering-math/module-5-complex-numbers|eng-math M5]]. All formulas duplicated in [[formula-sheet-bee]].

# AC Circuits

## 1. The Sinusoid

$$v(t) = V_m \sin(\omega t \pm \phi), \quad \omega = 2\pi f \;\text{rad/s}, \quad f = \frac{1}{T}$$

| Quantity | Formula | Meaning |
|----------|---------|---------|
| **RMS value** | $V_{rms} = \dfrac{V_m}{\sqrt{2}} = 0.707 V_m$ | DC equivalent that produces same heating — what voltmeters read (230 V mains = 230 V RMS, peak ≈ 325 V) |
| **Average value** | $V_{avg} = \dfrac{2V_m}{\pi} = 0.637 V_m$ (half-cycle) | Zero over a full symmetric cycle |
| **Form factor** | $k_f = \dfrac{V_{rms}}{V_{avg}} = 1.11$ (sine) | Shape quality |
| **Peak (crest) factor** | $k_p = \dfrac{V_m}{V_{rms}} = 1.414$ (sine) | Insulation sizing |

## 2. Phasor Representation

A sinusoid ↔ a rotating vector (phasor). Use RMS phasors with reference at $0°$:
$$v = V_m\sin(\omega t + \phi) \;\Longleftrightarrow\; \bar{V} = V_{rms}\angle\phi$$

**Why phasors kill trigonometry**: adding sinusoids of the same frequency = adding complex numbers. Rectangular ↔ polar fluently:
$$\bar{Z} = R + jX = |Z|\angle\theta, \quad |Z| = \sqrt{R^2+X^2}, \quad \theta = \tan^{-1}\frac{X}{R}$$

## 3. Pure R, L, C Behavior

| Element | Impedance | Phase | Key fact |
|---------|-----------|-------|----------|
| R | $R$ | $0°$ (V, I in phase) | Consumes only real power |
| L | $jX_L = j\omega L$ | $+90°$ (I lags V) | $X_L \propto f$ — chokes high frequency |
| C | $-jX_C = \dfrac{1}{j\omega C}$ | $-90°$ (I leads V) | $X_C \propto 1/f$ — passes high frequency, blocks DC |

Memory hook: **"ELI the ICE man"** — E(L) before I: inductor lags; I before E(C): capacitor leads.

## 4. Series R-L-C Circuit

$$\bar{Z} = R + j(X_L - X_C), \quad |Z| = \sqrt{R^2 + (X_L - X_C)^2}$$

**Impedance triangle** (draw it every time):
- Base = R, perpendicular = $X = X_L - X_C$, hypotenuse = |Z|
- Same triangle scaled by I gives the voltage triangle ($V_R$, $V_X$, V)
- Same triangle scaled by I² gives the power triangle (P, Q, S)

**Nature of circuit**: $X_L > X_C$ → inductive (I lags, PF lagging); $X_L < X_C$ → capacitive (I leads, PF leading); equal → resonance.

## 5. Power in AC

| Power | Formula | Unit |
|-------|---------|------|
| Active (real) | $P = VI\cos\theta = I^2R$ | W |
| Reactive | $Q = VI\sin\theta = I^2X$ | VAR |
| Apparent | $S = VI = I^2|Z|$ | VA |

**Power factor**: $\cos\theta = \dfrac{R}{|Z|} = \dfrac{P}{S}$ — the fraction of apparent power doing useful work. Industrial penalty below ~0.9 → capacitors added in parallel (they supply lagging reactive power locally).

## 6. Parallel R-L-C & Admittance

$$\bar{Y} = \frac{1}{\bar{Z}} = G - jB, \quad G = \frac{1}{R} \text{(conductance)}, \; B = \text{susceptance}$$
Branch currents add as phasors; use admittance when branches share voltage (household wiring = parallel).

## 7. Series Resonance

At $X_L = X_C$ → $\omega_0 = \dfrac{1}{\sqrt{LC}}$, $f_0 = \dfrac{1}{2\pi\sqrt{LC}}$:

- $\bar{Z}_{min} = R$ (purely resistive), $I_{max} = V/R$
- Power factor = 1 (unity)
- **Voltage magnification**: $V_L = V_C = QV$ where **quality factor**
$$Q = \frac{\omega_0 L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}}$$
High Q → sharp selectivity, narrow bandwidth: $BW = \dfrac{f_0}{Q} = \dfrac{R}{2\pi L}$
- Application: radio tuning (select one station's frequency, reject others)

## 8. Worked Example (exam pattern)

*R = 8 Ω, L = 0.1 H, C = 200 μF in series across 230 V, 50 Hz.*

1. $X_L = 2\pi(50)(0.1) = 31.42$ Ω
2. $X_C = \dfrac{1}{2\pi(50)(200\times10^{-6})} = 15.92$ Ω
3. $X = 31.42 - 15.92 = 15.5$ Ω (inductive)
4. $|Z| = \sqrt{8^2 + 15.5^2} = 17.43$ Ω; $I = \dfrac{230}{17.43} = 13.2$ A
5. $\theta = \tan^{-1}\dfrac{15.5}{8} = 62.7°$ → **PF = cos 62.7° = 0.459 lagging**
6. $P = VI\cos\theta = 230 \times 13.2 \times 0.459 = 1393$ W; $Q = VI\sin\theta = 2698$ VAR

**Checker**: $S^2 = P^2 + Q^2$ → $3060^2 \approx 1393^2 + 2698^2$ ✓

## 9. Failure Modes (exam)

| Trap | Fix |
|------|-----|
| Mixing RMS and peak | All phasor math in RMS; convert at the end only |
| Sign of X_C | Impedance of C is $-jX_C$ — capacitive branch REDUCES net reactance |
| PF stated without lead/lag | Always write "0.46 lagging" — the nature is half the answer |
| Resonance without Q | Quote $f_0$, Q, BW, and $Z=R$ — the four-piece answer scores full |

## Related

[[module-1-dc-circuits]] · [[module-3-magnetic-circuits-and-transformers]] · [[formula-sheet-bee]] · [[modules/../01-Areas/Engineering/engineering-math/module-5-complex-numbers|complex numbers]]