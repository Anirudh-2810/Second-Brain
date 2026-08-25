---
course_code: "BEE"
course_name: "Basic Electrical Engineering"
unit: "Master Formula Sheet"
tags: [bee, formula-sheet, exam-prep, revision]
last_updated: "2026-08-25"
confidence: "high"
---

## For future agent
Every BEE formula on one page for CA/MSE/ESE revision. Organized by module; pairs with the module pages for derivations and worked examples. Print-friendly.

# BEE — Master Formula Sheet

## M1 — DC Circuits

| Quantity | Formula |
|----------|---------|
| Charge / Power / Energy | $Q = It$ · $P = VI = I^2R = V^2/R$ · $W_{kWh} = Pt/1000$ |
| Resistance | $R = \rho l/a$ · $R_2 = R_1[1+\alpha_1(T_2-T_1)]$ |
| Series / Parallel | $\Sigma R$ · $\dfrac{1}{R_{eq}} = \Sigma\dfrac{1}{R_i}$ · product-over-sum (2) |
| Divider rules | $V_1 = V\frac{R_1}{R_1+R_2}$ · $I_1 = I\frac{R_2}{R_1+R_2}$ |
| Star→Delta | $R_{12} = R_A+R_B+\dfrac{R_AR_B}{R_C}$ (cyclic) |
| Delta→Star | $R_A = \dfrac{R_{12}R_{31}}{R_{12}+R_{23}+R_{31}}$ (cyclic) |
| Balanced | $R_\Delta = 3R_Y$ |
| Thevenin | $I_L = \dfrac{V_{th}}{R_{th}+R_L}$ |
| Norton ↔ Thevenin | $I_N = V_{th}/R_{th}$, same $R_{th}$ |
| Max power transfer | $R_L = R_{th}$, $P_{max} = \dfrac{V_{th}^2}{4R_{th}}$, η = 50% |

## M2 — AC Circuits

| Quantity | Formula |
|----------|---------|
| RMS / Avg / Form / Peak | $\dfrac{V_m}{\sqrt2}$ · $\dfrac{2V_m}{\pi}$ · 1.11 · 1.414 (sine) |
| $\omega$, f | $\omega = 2\pi f$ |
| Reactances | $X_L = \omega L$ · $X_C = \dfrac{1}{\omega C}$ |
| Series impedance | $|Z| = \sqrt{R^2+(X_L-X_C)^2}$, $\theta = \tan^{-1}\dfrac{X_L-X_C}{R}$ |
| Current | $I = \dfrac{V}{|Z|}$ |
| Powers | $P = VI\cos\theta$ · $Q = VI\sin\theta$ · $S = VI$ · $S^2 = P^2+Q^2$ |
| PF | $\cos\theta = R/|Z| = P/S$ |
| Admittance | $Y = 1/Z = G - jB$ |
| Resonance | $f_0 = \dfrac{1}{2\pi\sqrt{LC}}$ · $Z=R$ · $I_{max}$ · PF = 1 |
| Q factor / BW | $Q = \dfrac{\omega_0L}{R} = \dfrac{1}{R}\sqrt{\dfrac{L}{C}}$ · $BW = \dfrac{f_0}{Q} = \dfrac{R}{2\pi L}$ |
| Voltage magnification | $V_L = V_C = QV$ |

## M3 — Magnetic Circuits & Transformer

| Quantity | Formula |
|----------|---------|
| MMF / Flux / Reluctance | $\mathcal{F} = NI$ · $\Phi = \dfrac{\mathcal{F}}{\mathcal{S}}$ · $\mathcal{S} = \dfrac{l}{\mu_0\mu_r a}$ |
| B, H | $B = \Phi/a = \mu_0\mu_rH$ · $H = NI/l$ |
| Core losses | $P_h = \eta B_m^{1.6}fV$ · $P_e = KB_m^2f^2t^2V$ |
| **EMF equation** | $E = 4.44\,f\,N\,\Phi_m$ |
| Transformation | $K = \dfrac{E_2}{E_1} = \dfrac{N_2}{N_1} \approx \dfrac{I_1}{I_2}$ |
| Efficiency | $\eta = \dfrac{xS\cos\phi}{xS\cos\phi + P_i + x^2P_{cu,fl}}$ |
| Max efficiency at | $x = \sqrt{P_i/P_{cu,fl}}$ (i.e., $P_{cu} = P_i$) |
| Regulation | $\%\,Reg = \dfrac{V_{nl}-V_{fl}}{V_{fl}}\times100$ |
| Autotransformer Cu saving | $1 - \dfrac{N_2}{N_1}$ |

## M4 — DC Machines & Induction Motor

| Quantity | Formula |
|----------|---------|
| Generator EMF | $E_g = \dfrac{P\Phi ZN}{60A}$ (Lap: A=P; Wave: A=2) |
| Motor back-EMF | $E_b = V - I_aR_a = \dfrac{P\Phi ZN}{60A}$ |
| Armature torque | $T_a = 0.159\dfrac{PZ\Phi I_a}{A}$ N·m · $= 9.55\dfrac{E_bI_a}{N}$ |
| Speed | $N \propto \dfrac{E_b}{\Phi} = \dfrac{V-I_aR_a}{\Phi}$ |
| Starting current | $I_{st} = V/R_a$ (10–20× FL — hence starter) |
| Synchronous speed | $N_s = \dfrac{120f}{P}$ |
| Slip | $s = \dfrac{N_s-N}{N_s}$ · $f_r = sf$ |
| Rotor Cu loss | $= s \times P_{airgap}$ · mech power $= (1-s)P_{airgap}$ |

## M5 — Installations, Safety & Energy

| Quantity | Rule |
|----------|------|
| Energy | kWh = kW × h ("units") |
| Load factor | avg demand / peak demand (↑ = cheaper/unit) |
| Wire ratings | Lights 5 A / 1.5 mm² · Power 15 A / 2.5–4 mm² |
| Switch position | Always in PHASE wire |
| RCCB sensitivity | 30 mA human protection · 100/300 mA fire |
| Earth pit resistance | < 1–5 Ω |
| Cell voltages | Lead-acid 2.0 · Li-ion 3.7 · LiFePO₄ 3.2 V/cell |
| Pack building | Series → voltage adds · parallel → Ah adds |
| Solar panel | ~15–22% conversion · wind Betz limit 59.3% |

## Exam-Day Checklist

1. Thevenin: kill sources correctly (V→short, I→open)
2. AC: draw the impedance triangle, then power triangle — same shape
3. PF answer: always "0.XX lagging/leading"
4. Transformer max-η: set $x^2P_{cu,fl} = P_i$
5. Induction motor: compute $N_s$ FIRST, then slip
6. M5: draw wiring/earthing diagrams — half the marks

## Related

[[INDEX|BEE Module Index]] · [[module-1-dc-circuits]] · [[module-2-ac-circuits]] · [[module-3-magnetic-circuits-and-transformers]] · [[module-4-dc-machines-and-induction-motors]] · [[module-5-installations-safety-energy]]