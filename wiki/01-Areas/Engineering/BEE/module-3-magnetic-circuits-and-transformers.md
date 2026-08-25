---
course_code: "BEE"
course_name: "Basic Electrical Engineering"
unit: "Module 3 — Magnetic Circuits & Single-Phase Transformer"
tags: [bee, magnetic-circuit, transformer, emf-equation, efficiency, regulation]
last_updated: "2026-08-25"
confidence: "high"
---

## For future agent
Module 3 of BEE (MU pattern): magnetic circuits and the single-phase transformer. The EMF equation derivation, losses split, and efficiency/regulation numericals are guaranteed paper questions. All formulas in [[formula-sheet-bee]]; physics foundation in [[modules/../01-Areas/Engineering/physics/overview|Engineering Physics]].

# Magnetic Circuits & Single-Phase Transformer

## 1. Magnetic Circuit Concepts

| Electric circuit | Magnetic circuit |
|------------------|------------------|
| EMF (V) | **MMF** $\mathcal{F} = NI$ (ampere-turns, At) |
| Current I | **Flux** $\Phi$ (weber, Wb) |
| Resistance R | **Reluctance** $\mathcal{S} = \dfrac{l}{\mu_0\mu_r a}$ (At/Wb) |
| $I = EMF/R$ | $\Phi = \dfrac{\mathcal{F}}{\mathcal{S}}$ (Hopkinson's law) |

- **Flux density** $B = \dfrac{\Phi}{a}$ (tesla); **field intensity** $H = \dfrac{NI}{l}$ (At/m)
- **Permeability**: $B = \mu_0\mu_r H$; air: $\mu_r = 1$; iron: $\mu_r = 1000\text{–}5000$
- **Air gap dominance**: even a 1 mm air gap has reluctance ≈ thousands of times an equal iron path — magnetic circuits in SERIES add reluctances exactly like resistors

### B-H Curve & Losses
- **B-H curve**: saturation knee — beyond it, $\mu_r$ collapses (why transformers aren't designed at saturation)
- **Hysteresis loss** $P_h = \eta B_m^{1.6} f V$ (W) — area of the loop; minimized by silicon steel (narrow loop)
- **Eddy current loss** $P_e = K B_m^2 f^2 t^2 V$ — minimized by laminating the core (thin sheets insulated from each other break the eddy paths)
- Together = **core (iron) losses** — constant at constant voltage & frequency, independent of load

## 2. Single-Phase Transformer — Principle

Two windings on a laminated iron core. AC on the **primary** creates alternating flux $\Phi_m$ in the core; this flux links the **secondary** and induces EMF by **mutual induction**. No electrical connection — power transfers through the magnetic field. Works ONLY on AC (DC gives steady flux → zero induced EMF → primary burns out on its own resistance drop).

### EMF Equation (derive this — guaranteed question)
Flux varies sinusoidally: $\Phi = \Phi_m \sin\omega t$.
By Faraday: $e = -N\dfrac{d\Phi}{dt} = -N\omega\Phi_m\cos\omega t$
Peak EMF: $E_m = N\,\omega\Phi_m = 2\pi f N \Phi_m$
RMS (divide by $\sqrt2$):
$$\boxed{E = 4.44\, f\, N\, \Phi_m \;\text{volts}}$$
(4.44 = $2\pi/\sqrt2$). Per-turn equality: $\dfrac{E_1}{N_1} = \dfrac{E_2}{N_2}$ → **transformation ratio**
$$K = \frac{E_2}{E_1} = \frac{N_2}{N_1} \approx \frac{I_1}{I_2}$$
Step-up: $K>1$; step-down: $K<1$. Current transforms inversely — power in ≈ power out.

## 3. Losses, Efficiency & Regulation

### Losses
| Loss | Source | Dependence | Measured by |
|------|--------|-----------|-------------|
| **Iron (core)** $P_i$ | Hysteresis + eddy in core | Constant (V, f fixed) | **Open-circuit test** (measures $P_i$ + magnetizing current) |
| **Copper** $P_{cu} = I_1^2R_1 + I_2^2R_2$ | Winding resistance | Varies as load² | **Short-circuit test** (measures full-load $P_{cu}$) |

### Efficiency
$$\eta = \frac{P_{out}}{P_{out}+P_i+P_{cu}} = \frac{x\cdot S\cos\phi}{x\cdot S\cos\phi + P_i + x^2 P_{cu,fl}}$$
where $x$ = fraction of full load. **Maximum efficiency** when:
$$P_{cu}(x) = P_i \quad\Rightarrow\quad x = \sqrt{\frac{P_i}{P_{cu,fl}}}$$
Transformers are designed so this peak lands at the typical load (~60–70% of full load) — they run near peak all day.

### Voltage Regulation
$$\%Reg = \frac{V_{no\text{-}load} - V_{full\text{-}load}}{V_{full\text{-}load}} \times 100$$
Lower is better (output voltage stays constant from no-load to full-load). Zero at unity PF with capacitive load compensation; worst at low leading/lagging PF.

## 4. Autotransformer

Single winding, part shared between primary and secondary. 
- **Saving in copper** ∝ fraction of winding shared: $ saving = 1 - \dfrac{N_2}{N_1}$ (for $K$ near 1)
- Uses: motor starting, interconnecting nearly-equal voltages (220↔200 V)
- Risk: electrically NOT isolated — a primary fault appears on the secondary

## 5. Worked Example (exam pattern)

*1-φ transformer, 50 Hz, core area 0.02 m², $B_m = 1.2$ T, N₁ = 400, N₂ = 20. Find EMFs; if $P_i$ = 80 W, $P_{cu,fl}$ = 200 W, S = 5 kVA, find max-efficiency load and η at that load.*

1. $\Phi_m = B_m \cdot a = 1.2 \times 0.02 = 0.024$ Wb
2. $E_1 = 4.44(50)(400)(0.024) = 2131$ V; $E_2 = 4.44(50)(20)(0.024) = 106.6$ V
3. Max η at $x = \sqrt{80/200} = 0.632$ → load = 3.16 kVA
4. $\eta_{max} = \dfrac{0.632 \times 5000 \times 0.8}{0.632 \times 5000 \times 0.8 + 80 + 80} = \dfrac{2528}{2688} = 94.05\%$ (at PF 0.8)

## 6. Failure Modes (exam)

| Trap | Fix |
|------|-----|
| Forgetting $\sqrt2$ in EMF equation | $E_m = 2\pi f N \Phi_m$; RMS = 4.44 — quote both |
| Max-η condition misremembered | Variable losses = constant losses, i.e. $x^2 P_{cu,fl} = P_i$ |
| Regulation sign confusion | Lagging PF → regulation positive; leading can be negative (voltage RISES on load) |
| DC on transformer | Steady flux → no secondary EMF, no back-EMF → primary draws huge current → burns |

## Related

[[module-2-ac-circuits]] (the sinusoid feeding the core) · [[module-4-dc-machines-and-induction-motors]] (same flux principles in rotating machines) · [[formula-sheet-bee]]