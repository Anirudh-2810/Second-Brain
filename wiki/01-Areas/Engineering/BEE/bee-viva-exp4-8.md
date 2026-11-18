---
course_code: "BEE"
course_name: "Basic Electrical Engineering"
unit: "BEEL Viva — Expts 4–8"
date: 2026-11-19
tags: [btech, bee, beel-lab, viva, superposition, maximum-power-transfer, power-factor, two-wattmeter, dc-motor]
last_updated: "2026-11-19"
confidence: high
description: "Viva Q&A bank for BEE lab Expts 4–8: superposition, maximum power transfer, PF improvement, two-wattmeter 3-phase power, DC-motor armature speed control — with trap questions and one-line answers."
---

## For future agent

Viva-prep companion to the bench guides [[lab-dc-theorems-expts-2-5]] (Expts 4–5) and [[lab-ac-pf-three-phase-motor-expts-6-8]] (Expts 6–8). Answers are one-liners meant to be said out loud, not essays. Theory depth lives in [[module-1-dc-circuits]], [[module-2-ac-circuits]], [[module-3b-three-phase-ac-circuits]], [[module-4-dc-machines-and-induction-motors]]; formulas in [[formula-sheet-bee]]. If the uploaded lab manual contradicts a statement here, correct this page and log it.

# BEE Viva — Expts 4 to 8

## Expt 4 — Superposition theorem

**Say the statement first:** *In any linear bilateral network with multiple sources, the current/voltage in any branch is the algebraic sum of the responses caused by each source acting alone, all other sources replaced by their internal resistances.*

| Q | A (say it in one breath) |
|---|---|
| How do you "kill" a voltage source? | Replace with a **short circuit** — keeps its internal resistance in the circuit. |
| How do you kill a current source? | Replace with an **open circuit**. |
| Why is internal resistance kept when killing a source? | The short/open only removes the *ideal* source; the real source's resistance is part of the network. |
| Superposition applies to… ? | Current and voltage only — **never power** ($P=I^2R$ is nonlinear, $P'+P''\neq P$). |
| Why must the network be linear? | Superposition = homogeneity + additivity; only R, L, C, and linear amplifiers obey it — not diodes/transistors at large signal. |
| Sign convention in the sum? | Take one reference direction; a source pushing opposite to it contributes negative — sum with signs. |
| Can you superpose dependent sources? | No — dependent sources stay active (they depend on a branch quantity that itself changes). |
| What if the two sources are equal and opposing? | Branch currents from each case are equal and opposite → net zero in that branch (classic check). |

**Trap:** *"Can you verify superposition with a bulb?"* — No: filament resistance changes with temperature → nonlinear → the theorem doesn't apply, and $P'\neq P''$ anyway.

## Expt 5 — Maximum power transfer

**Say the statement first:** *A source delivers maximum power to the load when $R_L = R_S$ (the source/Thevenin resistance), and then $P_{max} = V_S^2 / 4R_S$.*

| Q | A |
|---|---|
| Condition for max power? | $R_L = R_{th}$ (matched load). |
| Value of $P_{max}$? | $V_S^2/(4R_S)$ — half the voltage drops across $R_S$. |
| Efficiency at max power? | **50%** exactly — $\eta = R_L/(R_L+R_S) = 1/2$ when matched. |
| So why use it at all? | Signal/audio/RF transfer where *power delivered* matters more than *wasting* it — speaker, antenna, antenna-to-receiver matching. |
| Why NOT in power systems? | 50% waste is unacceptable — utilities run $R_L \gg R_S$ for high efficiency instead. |
| Plot $P_L$ vs $R_L$ — shape? | Rises, **peaks at $R_L = R_S$**, falls off on both sides (asymmetric: →0 as $R_L→0$, →0 as $R_L→∞$). |
| What if $R_L < R_S$? | Current is high but $V_L$ collapses → power falls. |
| Real-world dynamic example? | Solar **MPPT** — the converter continuously retunes the effective load so the panel always sees its matched operating point. |
| Difference from Thevenin's aim? | Thevenin *models* the network; max-power *chooses the load* for it. |

## Expt 6 — Power-factor improvement (parallel capacitor)

**Aim in one line:** *Raise the PF of an R–L load by connecting a capacitor in parallel, so the same real power needs less line current.*

| Q | A |
|---|---|
| Why is a motor's PF lagging? | Magnetising current is reactive — it must be drawn from the supply to build the field (wasted VAR). |
| Why does a parallel C improve PF? | Capacitor supplies the reactive VAR *locally* → supply no longer carries it → $I_{line}$ drops, $\phi$ shrinks. |
| Why **parallel**, not series? | Parallel keeps the **load voltage undisturbed**; series C would change voltage/current division and could overvolt the load. |
| Design equation? | $Q_C = P(\tan\phi_1 - \tan\phi_2)$, $\;C = Q_C/(2\pi f V^2)$ |
| Benefits? | Lower $I^2R$ losses, thinner cables, released feeder capacity, avoids utility PF-penalty. |
| What happens if you over-compensate? | PF goes **leading** — risk of resonance with system inductance and voltage rise; stay near unity, slightly lagging is safest. |
| Define PF. | $\cos\phi = P/S$ — ratio of real power (W) to apparent power (VA); $\phi$ = angle between V and I. |
| Units? | P in watts, Q in VAR, S in VA; $S^2 = P^2 + Q^2$. |
| Can a capacitor change real power P? | No — P is set by the load; only Q (and hence S and I) changes. |
| Why 50 V / 50 Hz autotransformer? | Variable-voltage supply to set the operating point safely; 50 Hz is the Indian mains frequency the formula assumes. |

## Expt 7 — Three-phase power by two wattmeters

**Aim in one line:** *Measure balanced 3-φ power with two wattmeters and verify $P = W_1 + W_2 = \sqrt{3}V_LI_L\cos\phi$.*

| Q | A |
|---|---|
| Why does two-wattmeter work at all? | **Blondel's theorem:** n conductors need n−1 wattmeters — 3-φ, 3-wire → 2. |
| Reading formulas? | $W_1 = V_LI_L\cos(30°+\phi)$, $\quad W_2 = V_LI_L\cos(30°-\phi)$ |
| Total power? | $W_1 + W_2 = \sqrt{3}V_LI_L\cos\phi$ (independent of $\phi$) |
| Reactive power from readings? | $Q = \sqrt{3}(W_1 - W_2)$ |
| PF from readings? | $\tan\phi = \sqrt{3}\,(W_1-W_2)/(W_1+W_2)$ |
| At $\phi = 0$ (resistive)? | $W_1 = W_2$ — the lamp-bank check ($\cos\phi=1$, count × 100 W). |
| At $\phi = 60°$? | One reading = **zero** ($\cos 90° = 0$). |
| Beyond $60°$? | That reading goes **negative** — reverse the current-coil terminals and *subtract*. |
| What does the lamp bank give you? | A known resistive load: theoretical $P$ = lamps × 100 W to compare against $W_1+W_2$. |
| Can you use one wattmeter? | Only for a *balanced* load with neutral access (per-phase measurement) — two is the general method. |
| Why verify against $\sqrt{3}V_LI_L$? | Two independent checks: sum-of-readings vs formula vs lamp rating — disagreement means wiring/connection error. |

## Expt 8 — DC-motor speed control (armature resistance)

**Aim in one line:** *Control DC-motor speed below base speed by adding resistance in the armature circuit, keeping field flux constant.*

| Q | A |
|---|---|
| Speed equation? | $E_b = V - I_a(R_a + R_{ext}) = k\phi n \;\Rightarrow\; n = \dfrac{V - I_a(R_a+R_{ext})}{k\phi}$ |
| Why does speed fall when $R_{ext}$ rises? | More drop across $R_{ext}$ → smaller $E_b$ → and $n \propto E_b$ at constant $\phi$. |
| Why is the field left straight across the supply? | Keeps $\phi$ constant so speed changes come *only* from armature voltage — smooth, controllable. |
| Constant-torque drive? | Yes — load torque constant keeps $I_a$ rated while $n$ steps down: **constant-torque, below-base-speed** control. |
| Why not use field resistance to slow it down? | Field control gives **above**-base speed (weaker $\phi$ → higher $n$) — wrong direction, and weak field risks runaway. |
| Main drawback? | $I_a^2R_{ext}$ heat — **poor efficiency**; that's why it's for lab/virtual demonstration, not industry. |
| Industrial alternative? | Ward–Leonard (armature-voltage control, smooth, efficient) or chopper/DRV-driven armature control. |
| Operating points on the $n$–$I_a$ family? | $R_{ext}=0→$ point C, then D, E as resistance steps up — each step a new straight line, load line picks the point. |
| What happens at $R_{ext}$ very large? | $n → 0$ — motor can stall while drawing full armature current (dangerous: motor at standstill = back-EMF 0). |
| What is back-EMF? | Generated opposition voltage $k\phi n$ — the motor's own "speed sensor"; it limits armature current. |

## Cross-experiment traps (asked regardless of experiment)

- **"Which experiment did you actually do?"** — answer honestly, then explain the theory as above; Expts 4 and 6 were VLab, Expts 5 and 8 (and 2) hardware, Expt 7 lamp-bank bench.
- **"Thevenin vs Norton vs superposition — one line each?"** — Thevenin: $V_{th}+R_{th}$ series; Norton: $I_N \parallel R_N$ ($V_{th}=I_NR_N$); superposition: sum per-source responses (V and I only).
- **"Why is max-power efficiency only 50%?"** — matched divider splits voltage equally across $R_S$ and $R_L$, so half the power is lost in the source.
- **"PF lagging or leading for a motor? Why?"** — lagging: inductive magnetising branch needs VAR from the supply.

## See also

- Bench procedures + observation tables: [[lab-dc-theorems-expts-2-5]] · [[lab-ac-pf-three-phase-motor-expts-6-8]]
- Full IA1 viva bank (Expts 1–3): [[bee-ia1-2026-solutions-and-viva]]
- Formulas: [[formula-sheet-bee]] · Theory: [[module-1-dc-circuits]] · [[module-2-ac-circuits]] · [[module-3b-three-phase-ac-circuits]] · [[module-4-dc-machines-and-induction-motors]]
