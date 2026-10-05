---
course_code: "BEE"
course_name: "Basic Electrical Engineering"
unit: "IA1 2026-27 — Mesh + Thevenin solutions and viva bank"
date: "2026-10-05"
tags: [btech, bee, beel-lab, thevenin, vth, rth, mesh-analysis, lt-spice, viva, exam-prep]
last_updated: "2026-10-05"
confidence: high
description: "Fully solved BEE IA1 2026-27 simulation assignment (Q1 mesh on the 25V network, Q2 Thevenin on the 8V network) with R1-from-roll-number tables, plus the viva bank for Expt 1 components/instruments, Expt 2 battery level indicator and finding unknown resistance by Thevenin."
source: "raw-sources/BEE IA1_SemI_ 2026.pdf (3 pp) + Downloads Expt_1_Components_Intruments_26-27.docx + Expt_2_Battery_Voltage_level_indicator_26-27.docx"
---

## For future agent
Solved from the actual IA1 paper. **The two figures are swapped relative to their captions' surroundings** — the image on PDF page 2 (labelled *Figure 1*, the circuit with 4Ω/7Ω/2Ω/3Ω/2Ω and 25V+12V) is the **Q1 mesh** circuit, and the image on page 3 (*Figure 2*, 1Ω/2Ω/3Ω/5Ω with 8V/10V/12V) is the **Q2 Thevenin** circuit. Each figure's element list matches its own question's required outputs (Q1 asks for I_4Ω/I_7Ω/I_3Ω; Q2 asks for the 5Ω load), so the pairing is certain. Battery polarities were read from plate lengths at 14× zoom: **8V + on top, 10V + on left, 12V + on left, 25V + on top (explicit), 12V in Fig 1 − on top (explicit)**. Theory home: [[module-1-dc-circuits]]; worked-slide examples: [[thevenin-vth-rth-worked-examples]]; bench records: [[lab-dc-theorems-expts-2-5]]. Staleness caveat: R1 depends on the student's roll number — pick your own row. Solutions were cross-checked (KCL at all nodes + KVL on all three meshes = exact), so the topology and polarities are self-consistent; **LT Spice simulated values may differ slightly** and that is expected, not an error.

# BEE IA1 2026-27 — Solutions + Viva Bank

## 0. The assignment in one line

`R1 = last two digits of roll no.` If those digits are 01–10, **add 10** (so 01→11, 05→15). R1 is in **Ω**. Odd roll numbers attempt **Q1**, even roll numbers attempt **Q2**. Both need: simulate in LT Spice, then solve theoretically, then tabulate theoretical vs simulated.

| Q | Odd/Even | Circuit | Method | Report |
|---|----------|---------|--------|--------|
| Q1 | **Odd** | Fig 1: 25V + 12V, 4Ω/7Ω/2Ω/3Ω/2Ω + R1 | Mesh analysis | I_R1, I_4Ω, I_7Ω, I_3Ω |
| Q2 | **Even** | Fig 2: 8V + 10V + 12V, 1Ω/2Ω/3Ω/5Ω + R1 | Thevenin | V_th, R_th, I_L through 5Ω |

## 1. Q1 — Mesh analysis (Fig 1, odd roll)

### Topology (as read from the figure)

- Left branch: **25V** source, **+ on top**. Its top node `L1` also feeds the top wire (→ R1) and the left end of the **4Ω**.
- Its bottom node `L2` feeds the left end of the bottom **2Ω**.
- Middle horizontal wire: `L1` —**4Ω**— `M` —**2Ω**— `Rn`.
- **7Ω** drops from `M` to `M2`.
- Bottom wire: `L2` —**2Ω**— `M2` —**3Ω**— `R2`.
- **R1** drops from the top wire down to `Rn` (it sits on the right vertical).
- Right branch: **12V** source between `Rn` (**− on top**) and `R2` (**+ on bottom**).

### Mesh currents (all clockwise)

| Mesh | Region | Owns |
|------|--------|------|
| $I_A$ | top | R1, mid 2Ω, 4Ω |
| $I_B$ | left | 25V, bottom 2Ω, 7Ω, 4Ω |
| $I_C$ | bottom-right | mid 2Ω, 12V, 3Ω, 7Ω |

Branch currents (directions as written):
$$I_{R1} = I_A \quad(\text{L1}\to\text{Rn}) \qquad I_{4\Omega} = I_B - I_A \quad(\text{L1}\to M)$$
$$I_{7\Omega} = I_B - I_C \quad(M\to M2) \qquad I_{3\Omega} = I_C \quad(\text{R2}\to M2)$$

### The three equations

$$\boxed{(R_1 + 6)\,I_A - 4 I_B - 2 I_C = 0} \tag{A}$$
$$\boxed{-4 I_A + 13 I_B - 7 I_C = 25} \tag{B}$$
$$\boxed{-2 I_A - 7 I_B + 12 I_C = 12} \tag{C}$$

Where the numbers come from: (A) R1 + 4 + 2; (B) 4 + 7 + 2 with the 25V rise; (C) 2 + 7 + 3 with the 12V rise.

### Answers — pick your R1 row

| R1 (Ω) | I_R1 (A) | I_4Ω (A) | I_7Ω (A) | I_3Ω (A) |
|---------|----------|----------|----------|----------|
| 11 | 1.5024 | 2.9569 | 0.6077 | 3.8517 |
| 12 | 1.4000 | 3.0000 | 0.6000 | 3.8000 |
| 13 | 1.3107 | 3.0376 | 0.5933 | 3.7549 |
| 20 | 0.9060 | 3.2077 | 0.5631 | 3.5507 |
| 25 | 0.7423 | 3.2766 | 0.5508 | 3.4681 |
| 45 | 0.4309 | 3.4076 | 0.5275 | 3.3109 |
| 56 | 0.3501 | 3.4415 | 0.5215 | 3.2701 |
| 99 | 0.2020 | 3.5038 | 0.5104 | 3.1954 |

*(Recompute for any other roll number by solving (A)–(C); the R1 row is the only thing that changes.)*

**Sanity checks an examiner can watch you do:** current in = current out at `M` and `M2`; and adding (A)+(B)+(C) reproduces the outer-loop KVL $R_1 I_A + 2 I_B + 3 I_C = 37$.

## 2. Q2 — Thevenin's theorem (Fig 2, even roll)

### Topology (as read from the figure)

- Left branch: **8V**, **+ on top** → node `X` (top) to `W` (below it).
- `X` = top wire = top of the **1Ω** = **+ plate of the 10V**.
- **10V** runs in the top wire, **+ on the left** (− faces R1). Its right node `Y` is the top of **R1**.
- **R1** drops on the right vertical from `Y` to `Z`.
- `Z` = right of the mid **3Ω** = right end of the bottom wire.
- Middle wire: `W` —**2Ω**— `M` —**3Ω**— `Z`. The **1Ω** drops from `X` to `M`.
- Bottom wire: `W` —**5Ω**— `B` —**12V**— `Z`, with the **12V + plate on the left** (facing `B`).

**The load is the 5Ω resistor** — that is what "current through the 5 Ω load resistor $I_L$" means. Remove it; the Thevenin terminals are `W` and `B`.

### Step 1 — V_th (open circuit at W–B)

With the 5Ω gone, node `B` touches only the 12V source, so **no current flows in the 12V branch** and $V_B = V_Z + 12$.

Take $V_W = 0$. Then $V_X = 8$ and $V_Y = V_X - 10 = -2$.

KCL at `M` and at `Z`:
$$\frac{V_M - 8}{1} + \frac{V_M}{2} + \frac{V_M - V_Z}{3} = 0 \;\Longrightarrow\; 11 V_M - 2 V_Z = 48$$
$$\frac{V_Z + 2}{R_1} + \frac{V_Z - V_M}{3} = 0$$

$$\boxed{V_{th} = V_B - V_W = V_Z + 12}$$

### Step 2 — R_th (sources killed)

Kill sources: 8V short → `X`=`W`; 10V short → `X`=`Y`; 12V short → `B`=`Z`. Now the 1Ω and 2Ω are **in parallel** from the terminal node to `M`, in series with the 3Ω to the far terminal, and that whole path is **in parallel with R1**:

$$R_{th} = R_1 \parallel \left(3 + (1 \parallel 2)\right) = R_1 \parallel \frac{11}{3} = \frac{11 R_1}{3 R_1 + 11}$$

### Step 3 — load current

$$I_L = \frac{V_{th}}{R_{th} + 5} \qquad V_{5\Omega} = 5 I_L$$

### Answers — pick your R1 row

| R1 (Ω) | V_th (V) | R_th (Ω) | I_L through 5Ω (A) | V across 5Ω (V) |
|---------|----------|----------|--------------------|-----------------|
| 11 | 13.2353 | 2.7500 | 1.7078 | 8.5389 |
| 12 | 13.2593 | 2.8085 | 1.6981 | 8.4903 |
| 13 | 13.2798 | 2.8600 | 1.6895 | 8.4477 |
| 20 | 13.3691 | 3.0986 | 1.6508 | 8.2539 |
| 25 | 13.4035 | 3.1977 | 1.6350 | 8.1752 |
| 45 | 13.4664 | 3.3904 | 1.6050 | 8.0249 |
| 56 | 13.4822 | 3.4413 | 1.5972 | 7.9858 |
| 99 | 13.5106 | 3.5357 | 1.5828 | 7.9142 |

**Note the structure worth saying out loud in the viva:** $V_{th}$ depends only on the *sources*, $R_{th}$ only on the *resistors*. If a load resistor is also part of the network, changing it changes nothing about $V_{th}$ — only $I_L$ moves.

## 3. Viva bank — Thevenin experiment

### 3.1 The two questions the record asks

**"State what is meant by a linear network."**
A network is linear if its output obeys **homogeneity** (scaling every input by $k$ scales every output by $k$) **and superposition / additivity** (the response to several sources acting together equals the sum of the responses to each acting alone). For a resistor this shows up as a straight-line V–I characteristic through the origin; for any linear network the Thevenin/Norton equivalent exists.

**"State the different applications of a linear network."**
Replacing a complex multi-source block by a single $V_{th}$–$R_{th}$ pair so analysis continues at one terminal pair: simplifying two-port stages, source/signal matching, sensor and transducer interfacing, amplifier input/output design, power-supply analysis, and any network where the load is one element among many. In short — it turns "many loops and many sources" into one division.

### 3.2 Finding an unknown resistance by Thevenin — the classic viva follow-up

This is the reason the theorem is taught. Method:

1. **Measure $V_{th}$** across the open terminals (unknown resistor removed).
2. **Measure $R_{th}$** looking back into the terminals with sources killed (voltage sources shorted, current sources opened).
3. Insert the unknown $R$ and measure the **loaded voltage $V$** across it (or the current $I$).
4. From the divider: $V = V_{th}\dfrac{R}{R + R_{th}}$ → solve
$$\boxed{R = \frac{V\,R_{th}}{V_{th} - V} = \frac{R_{th}}{V_{th}/V - 1}}$$

Why it is worth doing: you measure only voltages and one resistance you already know — **no ammeter, and the unknown resistor never has to be trusted as a reference**. $R_{th}$ can also be obtained without sources by the **open-circuit / short-circuit method**: $R_{th} = V_{oc}/I_{sc}$.

### 3.3 Trap questions

| Question | Answer |
|----------|--------|
| Why must the network be *linear*? | Superposition is the step that fails for non-linear elements; $V_{th}$, $R_{th}$ are not single-valued for diodes/transistors. |
| Active or passive? | Must be **active** — a passive network has $V_{th}=0$ and $R_{th}=R_N$. |
| How do you kill an ideal source? | Voltage source → **short** (0 Ω); current source → **open** (∞ Ω). |
| Is $R_{th} = R_N$? | Yes, same looking-in resistance; they are duals, $V_{th} = I_N R_{th}$. |
| Does superposition work for power? | **No.** $P = I^2R$ is non-linear, so $P' + P'' \ne P$. |
| Efficiency at max power transfer? | Only **50%** — all of $V_s^2/(4R_s)$ is delivered but half is burned in $R_{th}$. Hence matching is for *signal transfer*, not power distribution. |

## 4. Viva bank — Expt 1, Components & Instruments

Post-lab question in the record: **"State the functions of C.R.O."**

**CRO functions:** displays the **instantaneous value of a voltage vs time** as a waveform, so you can read **amplitude, peak-to-peak voltage, period, frequency, time interval, rise/fall time, phase shift and distortion**. Because the vertical deflection is proportional to voltage and horizontal to time, it *measures* time (period, phase delay between two channels) as well as voltage. A built-in **component tester** measures passive and active parts **in-circuit**. The lab unit is a 30 MHz colour-LCD scope with digital readout.

Follow-ups:

| Question | Answer |
|----------|--------|
| Why a CRO and not a DMM? | A DMM gives one number; a CRO gives the *shape* of the signal — peak, RMS, frequency, phase, distortion — and the time relationship between two signals. |
| What is the function generator? | A **multi-waveform signal source** — sine, square, triangle, ramp, pulse, TTL/sync and DC over roughly 0.01 Hz–1 MHz, with amplitude, DC offset and 80 dB attenuation. Used to test amplifiers, filters and attenuators, and to inject a known signal. |
| How does a breadboard work? | Internally it is **sets of five metal clips**: each group of five holes in a half-row (A–E or F–J) is one node. So A1–E1 are all connected; A1 is **not** connected to A2, nor to F1–J1. The centre channel is the power rail. |
| What is a resistor's two main ratings? | Its **resistance value in Ω** and its **power rating in W**. Tolerance runs from ±20% down to ±0.001%. |
| Fixed vs variable? | Fixed = carbon composition, metalized film, wire-wound (constantan/manganin). Variable = **potentiometer**, 3 terminals (2 fixed + wiper), for adjustment while connected. |
| Colour code? | First two bands = significant digits, **third = multiplier (number of zeros)**, fourth = **tolerance %**, fifth = failure rate. Gold = ±5%. |
| Four capacitor types? | **Ceramic** (small, cheap, low loss, pF→0.1 µF), **electrolytic** (polarized, >1 µF, low frequency ~100 kHz), **tantalum** (polarized, high capacitance density, explodes if reverse biased), **polystyrene/polyester film** (close tolerance, rolled plate/dielectric so inductance limits them to a few hundred kHz). |
| Inductor core types? | **Air** (RF, lossless core, high Q), **iron** (high power/high L audio chokes), **ferrite** (Fe₂O₃ with Mn-Zn or Ni-Zn — the common RF core), **iron powder** (distributed air gap → saturates late, good for high DC current). |
| Name four switch types. | By poles/throws: **SPST** (basic on/off), **SPDT** (changeover), **DPST**, **DPDT**; also by actuation: push-button (momentary), toggle, rotary, joystick. |

## 5. Viva bank — Expt 2, Battery Voltage-Level Indicator

The experiment teaches **voltage division**, **current division** and **LED turn-on voltage**, then assembles them into a 4-LED bar-graph battery gauge.

### 5.1 The three post-lab questions

**Q1 — Applications of a battery level indicator.**
Fuel gauge in vehicles · battery/backup health on UPS and inverter units · charge-level display on laptops, phones, power banks, drones and RC aircraft · verifying a new cell before use · solar-panel charge monitoring · any device where a user must know "how much is left" without opening it. The car dashboard fuel gauge is the direct commercial example.

**Q2 — Practical use of the voltage-division concept.**
Whenever one source must be split into two or more voltages that **sum to $V_S$**: resistor **voltage dividers** for biasing and reference voltages in amplifiers, **sensor signal conditioning** (thermistor/LDR/photoresistor divider feeding an ADC), **potentiometers and potentiometric position sensors**, **attenuating a signal to a measurable ADC range**, and **multi-LED bar graphs** as in this experiment. The rule that makes it work: in a series chain, the same current flows, so each drop is proportional to its resistance:
$$V_k = V_S\frac{R_k}{\sum R_i} \qquad \text{and} \qquad \sum V_k = V_S$$

**Q3 — How the battery level indicator works, in your own words.**
Four LEDs with series resistors are hung off successive taps of a resistor chain across the supply. Each resistor drops part of $V_S$, so the tap voltages rise as you go up the chain. At a high battery voltage the later taps sit above the ~1.8–2.2 V LED turn-on threshold, so LED 1, 2, 3, 4 light in turn. As the battery discharges the whole chain's voltage scales down; each tap falls below the LED threshold one after another and **LEDs go out one by one from the top of the bar downward** — LED 1 stays lit longest, so the number of lit LEDs *is* the state of charge. The series resistors set each LED's current and, just as importantly, isolate the already-lit LEDs so they do not load the higher taps and collapse the ladder.

### 5.2 Follow-ups

| Question | Answer |
|----------|--------|
| Why must each LED have its own series resistor? | To limit its current to a safe value ($R = (V_S - V_{LED})/I_{LED}$), and to prevent the conducting LEDs from loading the higher taps and breaking the ladder. |
| What is the LED turn-on voltage? | About **1.8–2.2 V** for a standard red/green LED (silicon). Task 3 in the record is exactly this measurement: Case 1 = just glowing (dimmest), Case 2 = glowing brightly. |
| Why does Task 3 need two cases? | An LED does not have a sharp threshold — it conducts from about 1 V and its brightness rises with forward current. "Just ON" ≈ first visible glow, "bright" ≈ higher forward current. Case 1 isolates the *turn-on* point, Case 2 checks the resistor is setting a sensible working current. |
| Why does the LED need a **forward-biased** junction? | A diode conducts only when its p-anode is positive relative to its n-cathode; reverse-bias it and it blocks (and may exceed its PIV and break). |
| Current division vs voltage division — which is it here? | The **task-1 ladder is voltage division** (series chain, same current, taps sum to $V_S$). **Task 2's parallel branches are current division**: $I_1=V_S/R_1$, and $I_S = I_1+I_2+I_3$. |
| In Task 2, why must $I_S$ equal the sum? | Kirchhoff's **current law**: charge is conserved, so total current entering the node equals total leaving it. |
| What is a non-load-bearing trap here? | A voltmeter has finite input resistance (≈10 MΩ for a DMM) and *loads* the tap it measures. Always note that a measured tap voltage is slightly lower than the ideal divider value. |

## Self-check before you walk in

1. Recompute your Q1 row for your own R1 from (A)–(C) without looking.
2. Recompute your Q2 row: $V_{th}$ from the two node equations, then $R_{th} = \frac{11R_1}{3R_1+11}$, then $I_L$.
3. One-line each: why sources short/open; why superposition fails for power; why efficiency is 50% at max power.
4. Derive $R = \dfrac{V R_{th}}{V_{th} - V}$ for the unknown-resistance case from the divider alone.
5. Explain why the LED count maps to state of charge without re-deriving the whole circuit.
6. Be ready to say **"V_th depends only on sources, R_th only on resistors"** — it is the cleanest one-sentence summary of the theorem.

## See also

- [[module-1-dc-circuits]] — mesh/nodal method, star–delta, all four network theorems
- [[thevenin-vth-rth-worked-examples]] — three solved slide examples (5.2 V/1.2 Ω, 10.93 V/8.33 Ω, 81 V/8 Ω)
- [[lab-dc-theorems-expts-2-5]] — Expts 2–5 bench procedure and observation tables
- [[formula-sheet-bee]] — every formula on one page
- [[source-map-bee-sem1]] — which raw file fed which page
- [[modules/../01-Areas/Engineering/engineering-math/module-1-matrices|eng-math M1]] — solving the mesh set by matrices
