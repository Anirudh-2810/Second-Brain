---
course_code: "ENG-NEXUS"
course_name: "Nexus Robotics — Hardware Viva"
unit: "Component Sheet Level 1 + Datasheet Parts"
date: 2026-11-19
tags: [btech, kjsce, nexus-robotics, viva, components, electronics, power-electronics, motors]
last_updated: "2026-11-19"
confidence: high
description: "Viva answers for every Level-1 row of the Nexus component sheet — passives, actives, LDO/78xx/79xx, BJT/MOSFET, motors, drivers, 555, protection, pull-ups, dividers, PWM — plus the 7 datasheet parts (7805, 7905, IRLZ44N, IRFZ44n, IRF4905, LM741, MG995) and MCB."
---

## For future agent

Viva Q&A over the **Level 1** half of the Nexus component sheet (the image in the interview-prep request), plus its datasheet column (7805, 7905, IRLZ44N, IRFZ44n, IRF4905, LM741, MG995) and MCB/fuse/varistor protection. Level 2 (comms, sensors, MCUs, op-amps, encoders…) lives in [[nexus-components-viva-level2]]. Companion theory bank: [[nexus-theory-rapidfire]]. Each entry = *what it does* (one line) + *viva traps*. Say answers out loud.

# Nexus Hardware Viva — Level 1 Components

## 1. Passive components

### Resistors
- **Does:** limits current / divides voltage; $V = IR$, $P = V^2/R$.
- **Types:** carbon-composition (cheap, noisy, hot), wire-wound (constantan/manganin — stable, high power), metal-film (low noise, 1% tol), potentiometer (variable — 3-terminal voltage divider).
- **Specs =** resistance + power rating (¼ W typical) + tolerance (gold 5%, silver 10%).
- **Color code (4-band):** band1 = 1st digit, band2 = 2nd digit, band3 = multiplier, band4 = tolerance. *Black 0 Brown 1 Red 2 Orange 3 Yellow 4 Green 5 Blue 6 Violet 7 Gray 8 White 9*; gold ×0.1. Example: red-red-brown-gold = 22 × 10 = **220 Ω ±5%**.
- **Viva traps:** *Which is more accurate — film or composition?* → metal-film (1%). *Why not use resistor as heater?* → power rating exceeded. *Series adds, parallel?* → $1/R_p = \sum 1/R_i$; two equal R in parallel = R/2.

### Capacitors
- **Does:** stores charge in electric field; blocks DC, passes AC ($X_C = 1/2\pi fC$); filters, couples, timing, decoupling.
- **Types:** ceramic (small, RF, unstable with temp), electrolytic (**polarised — +/−, can explode reversed**), tantalum (compact, low ESR, pricey), film (stable, timing).
- **Units:** 1 F = 10⁶ µF = 10⁹ nF = 10¹² pF.
- **Viva traps:** *Why DC blocked?* → charges fully, then no current flows in steady state. *Polarity matters?* → electrolytic only; ceramic/film non-polar. *Where is a cap used in your Arduino?* → 100 nF decoupling cap across VCC–GND (shunts IC switching noise). *Value code "104"?* → 10 × 10⁴ pF = **100 nF**.

### Diodes
- **Does:** one-way valve (PN junction); rectifier, protection (flyback), Zener regulation, LED emission.
- **Forward drop:** Si ≈ 0.7 V, Ge ≈ 0.3 V, LED ≈ 1.8–3.3 V (needs series resistor: $R=(V_s-V_f)/I$).
- **Viva traps:** *What happens reverse-biased?* → only tiny leakage until breakdown (Zener designed to work there). *Why a diode across a relay coil?* → flyback: collapses the inductive kick, protects the transistor.

### Inductors
- **Does:** stores energy in magnetic field; opposes *change* in current ($v = L\,di/dt$); filters ripple ($X_L = 2\pi fL$).
- **Viva traps:** *Inductor in DC steady state?* → short circuit (zero voltage drop). *Why in a buck converter?* → smooths the chopped current into the load. *Why does opening an inductive circuit spark?* → $di/dt$ huge → high voltage kick.

### Potentiometers
- **Does:** variable voltage divider (3 terminals) — volume knobs, sensor-position, calibration trim.
- **Viva trap:** *Rheostat vs potentiometer?* → rheostat = 2-terminal current limiter; pot = 3-terminal divider.

## 2. Active components

### LEDs
- **Does:** emits light when forward-biased; indicator, RGB via 3 dies, optocoupler's internal light source.
- **Trap:** never connect directly across supply — always series current-limiting resistor.

### ICs
- **Does:** entire circuit (transistors + resistors) on one silicon die; fixed function (555) or programmable (MCU).
- **Trap:** *IC vs MCU?* → MCU is an IC that runs *your* program; 555 is an IC with one hardwired job.

### Comparators
- **Does:** compares two voltages, outputs HIGH/LOW (open-loop op-amp behaviour); threshold detection, zero-crossing, level sensor.
- **Trap:** *Comparator vs op-amp?* → comparator = saturated digital output (rail or ground), designed for speed; op-amp = linear amplification. *Why hysteresis (Schmitt trigger)?* → noisy input near threshold otherwise chatters.

## 3. Power electronics

### LDO (low-dropout regulator)
- **Does:** linear regulator that works with tiny input–output difference (dropout ~0.2–1 V, vs ~2 V for 7805); quiet output, no switching noise, but burns $(V_{in}-V_{out})\times I$ as heat.
- **Trap:** *LDO vs buck?* → LDO: simple/quiet/wasteful; buck: efficient (>85%) but noisy and needs inductor.

### Switching regulator
- **Does:** chops input at high freq, filters → efficient voltage conversion; topologies: **buck** (step-down, $V_o = D\cdot V_{in}$), boost (step-up), buck-boost.
- **Trap:** *Efficiency vs linear?* → 80–95% vs 30–60%; *why noisy?* → PWM ripple needs LC filtering.

### 78xx / 79xx
- **78xx:** positive fixed linear regulators (7805 = +5 V, 7812 = +12 V); needs $V_{in} \ge V_{out} + 2$ V; 3 pins (in, gnd, out), ~1–1.5 A with heatsink.
- **79xx:** the negative-rail twins (7905 = −5 V).
- **Trap:** *Why is 7805 hot?* → dropout × load current wasted as heat. *7805 with 6 V input?* → marginal — below dropout + ripple → drops out.

## 4. Power supply

- **Battery:** DC source; chemistry sets voltage (Li-ion 3.7 V/cell, 9 V block, 12 V lead-acid — *lead-acid banned in Robocon robots, rule 11.16.1*).
- **SMPS:** AC→DC supply using high-freq switching + transformer isolation; compact, efficient, mains-isolated (your bench supply/charger).
- **Buck:** step-down DC-DC switcher (covered above); the standard 12 V→5 V/3.3 V on robots.

## 5. Transistors

### BJT (NPN/PNP)
- **Does:** **current-controlled** amplifier/switch; base current controls collector: $I_C = \beta I_B$ (β ≈ 100–300).
- **Regions:** cutoff (off), active (amplifying, $V_{CE}$ mid), saturation (fully on, $V_{CE(sat)}$ ≈ 0.2 V — the "switch" region).
- **Trap:** *Why base resistor?* → base-emitter is a diode; without R it burns out. *NPN sinking vs PNP sourcing?* → NPN low-side switch, PNP high-side.

### MOSFET (IRLZ44N, IRFZ44N, IRF4905 — see §7)
- **Does:** **voltage-controlled** switch; gate draws ~no DC current → driven straight from MCU pin; low $R_{DS(on)}$ → little heat.
- **N vs P channel:** N-channel conducts when gate HIGH (low-side, common); P-channel conducts when gate LOW (high-side).
- **Logic-level vs standard:** *logic-level* (IRLZ44N) fully ON at $V_{GS}$ = 4.5–5 V (MCU-friendly); *standard* (IRFZ44N) needs $V_{GS}$ ≈ 10 V — a 5 V pin only half-switches it → hot.
- **Trap:** *BJT or MOSFET for motor switching?* → MOSFET (faster, lower loss, voltage-driven). *Why gate driver IC for big MOSFETs?* → gate charge must be pumped fast; MCU pin can't supply the transient current.

## 6. Motors

| Motor | Does | Key viva line |
|---|---|---|
| **DC brushed** | Commutator + brushes switch coil current as rotor turns | Speed ∝ voltage, torque ∝ current; simple but brushes wear |
| **BLDC** | Electronically commutated 3-phase DC; rotor = permanent magnet | Sensorless (BEMF) or sensor-based; needs **ESC**; efficient, no brushes |
| **Stepper** | Moves in discrete steps (1.8°/step = 200/rev) | Open-loop positioning, holding torque; misses steps if overloaded |
| **Servo (MG995)** | Closed-loop: motor + gear + pot feedback → holds commanded angle | PWM (50 Hz, 1–2 ms pulse) commands angle; MG995 = metal-gear ~10 kg·cm |

**Trap:** *How do you know a stepper's position without a sensor?* → you don't lose it if you never skip steps — that's the open-loop assumption; stall = position error forever.

## 7. Motor drivers

- **H-bridge:** 4 switches in H config; diagonal pairs conduct → **bidirectional** control of one motor; PWM on the high side sets speed. **Trap:** *shoot-through?* → both switches in one leg on simultaneously = dead short — fix with dead-time/complementary driving.
- **L293D:** quadruple half-bridge = **2 motors**, ~0.6 A/ch, built-in flyback diodes, TTL-compatible inputs, 4.5–36 V.
- **L298N:** dual H-bridge, **2 A/ch** but a *bipolar* chip → ~2 V internal drop (runs hot, needs heatsink); EN pins for PWM.
- **Trap:** *Why doesn't the MCU drive the motor directly?* → motor amps (1–10 A) and noise vs MCU's mA-level 5 V pins — driver isolates control from power.

## 8. Controller

- **Arduino (UNO = ATmega328P, Mega = 2560):** 5 V, 16 MHz, easy GPIO/ADC/PWM; 328P = 14 DIO/6 PWM/6 ADC; 2560 = 54 DIO/15 PWM/16 ADC/4 serial.
- **ESP series (ESP8266/ESP32):** 3.3 V (**not 5 V tolerant!**), Wi-Fi (+BT on ESP32), dual-core 240 MHz on ESP32 — the cheap robot-comms choice.
- **Trap:** *ESP32 with 5 V sensor?* → level-shifter or divider required (see [[nexus-components-viva-level2]]). *When a real project needs STM32?* → more peripherals, faster ADC/timers, CAN, RTOS-grade work.

## 9. Connectors

- **FRC (crimp, e.g. Anderson/Molex KK):** keyed, latchable, rated for robot motor currents; standard in FTC/FRC-style wiring.
- **"Relimates" = JST (likely transcription):** polarized 2/3/4-pin housings for sensors/servos — can't be plugged backwards.
- **Screw terminals:** field-wireable, thick-gauge power distribution.
- **Header:** 0.1″ pins for breadboard/prototyping.
- **Viva line:** *Why polarized connectors?* → reversed power = dead MCU; keys make it impossible.

## 10. IC — Timer 555

- **Does:** precision timer/oscillator; two comparators + RS flip-flop + discharge transistor in one 8-pin package.
- **Modes:** **astable** (free-running square wave, $f = 1.44/[(R_1+2R_2)C]$), **monostable** (one pulse of width $1.1RC$ on trigger), bistable (Schmitt trigger).
- **Pins:** 1 GND, 2 trig, 3 out, 4 reset, 5 ctrl, 6 thr, 7 dis, 8 Vcc.
- **Traps:** *555 as PWM?* → astable + diode steering varies duty; *what does pin 5 do?* → control voltage — filter it with 10 nF.

## 11. Switches

- **Limit switch:** lever arm hit by mechanism → position end-stop (the "has the arm reached home" sensor).
- **Reed switch:** glass tube, contacts closed by a **magnetic field** (no physical contact — magnet on moving part).
- **Toggle / push:** manual; push = momentary (NO or NC contacts).
- **Trap:** *Why debounce?* → mechanical contacts bounce ms-scale → MCU counts multiple edges; fix: 10–20 ms timer or RC.

## 12. Protection & display

- **Relay:** coil + contact — MCU pin drives transistor → coil → **galvanically isolated** high-power switch (AC mains, big loads). Needs flyback diode across coil.
- **Fuse:** $I^2t$ element melts on overcurrent — **one-time**, never resettable; rating must sit above normal current but below wire rating.
- **MCB (miniature circuit breaker):** the resettable fuse+switch combo for mains circuits:
  - **Thermal trip:** bimetallic strip bends on sustained overload → trips.
  - **Magnetic trip:** solenoid yanks the latch instantly on short-circuit (high $di/dt$).
  - **Curve types:** B (domestic, 3–5× In), C (inductive/motor, 5–10× In), D (transformer/inrush, 10–20× In).
  - **Trap:** *Fuse vs MCB?* → fuse = cheaper, single-use, faster clearing; MCB = reusable, detects both overload and short, gives isolation. *ELCB/RCD?* → those trip on earth leakage (mA), not overcurrent.
- **Varistor (MOV):** voltage-dependent resistor — clamps voltage spikes (lightning/switching) to a safe level, degrades after repeated surges; placed across mains input.
- **4-bit / 7-segment display:** 7 LEDs in an 8-figure pattern; driven as **common-cathode** (all cathodes grounded, pin HIGH = lit) or **common-anode** (reverse); 4-digit = multiplexing (scan digits fast, human sees all lit). *Why multiplex?* → 4 digits × 7 segments = 28 lines vs 12 with scanning.

## 13. Circuit building blocks

- **Pull-up / pull-down:** a button pin must never float — pull-up (10 kΩ to VCC, button to GND → resting HIGH, press reads LOW) or pull-down (to GND, resting LOW). *Internal vs external?* → MCU internal ≈ 20–50 kΩ, fine for buttons; external needed for precision/noisy lines. *Active-low why?* → shorter path to ground, matches most input structures.
- **Voltage divider:** $V_{out} = V_{in}\cdot R_2/(R_1+R_2)$. Uses: measure high voltage with ADC, bias signals, logic-level shift (one-way). **Trap:** *Can a divider power a motor?* → no — it wastes current, sags under load; use a regulator. *Load effect?* → attaching a load changes the ratio — mind $R_2 \parallel R_{load}$.
- **Analog vs digital:** analog = continuous (sensor voltages, audio), digital = discrete levels (0/1); MCU's **ADC** converts analog→counts (10-bit: 0–1023 → $V = raw/1023 \times V_{ref}$), **DAC**/PWM converts back.
- **PWM:** digital square wave whose *duty cycle* = average power: $V_{avg} = duty \times V_{cc}$; motor speed, LED brightness, servo angle. *Why not analog voltage for motor?* → linear region of a transistor burns power as heat; PWM + switch = efficient.

## 14. Datasheet column (the 7 named parts)

| Part | One-line what | Datasheet facts they may probe |
|---|---|---|
| **7805** | +5 V 1.5 A linear regulator (TO-220) | $V_{in}$ max 35 V; needs ≥7 V in for 5 V out (2 V dropout); pinout in–gnd–out; heat = $(V_{in}-5)I$ |
| **7905** | −5 V linear regulator (the negative twin) | Same package/pinout *mirrored*; used for ± supplies around op-amps |
| **IRLZ44N** | Logic-level N-MOSFET, 47 V, ~47 A | $R_{DS(on)}$ specified **at $V_{GS}$ = 4.5 V** → driven straight from 5 V MCU; TO-220 |
| **IRFZ44N** | Standard N-MOSFET, 47 V, ~47 A | Same die class but $R_{DS(on)}$ rated at $V_{GS}$ = 10 V → **needs 10 V gate drive**; 5 V = half-on = hot |
| **IRF4905** | **P-channel** MOSFET, −55 V, −74 A | High-side switch (source to +V, gate pulled LOW to turn on); used for reverse-polarity protection and high-side load switching |
| **LM741** | Classic op-amp (1968) | Needs **± supplies** (not rail-to-rail), GBW ~1 MHz, offset ~1–6 mV, output can't reach rails; fine for labs, obsolete for modern design |
| **MG995** | Metal-gear servo, ~10 kg·cm @ 6 V | 50 Hz PWM, 1–2 ms pulse = 0–180°, 4.8–7.2 V, 3-wire (power/GND/信号); metal gears = can stall without stripping |

**One comparison they love:** *IRLZ44N vs IRFZ44N?* — identical package, **different gate-drive spec**: logic-level vs standard; that single letter (L) decides whether a 5 V pin can turn it fully on.

## 15. Rapid-fire round (say answer, then stop)

1. 7805 vs LDO? → dropout spec: 7805 ~2 V, LDO <1 V.
2. BJT vs MOSFET control? → current vs voltage.
3. Fuse vs MCB vs varistor? → overcurrent one-shot / resettable overload+short / voltage-spike clamp.
4. Why pull-up? → no floating pins; defined rest state.
5. Divider vs regulator? → passive ratio (wastes current) vs active hold (efficient, stiff).
6. Why H-bridge? → reverse current through motor → both directions.
7. Why a flyback diode? → inductor kick on switch-off.
8. Servo vs stepper? → closed-loop absolute angle vs open-loop steps.
9. PWM frequency too low for motor? → audible whine + torque ripple; too high → switching losses.
10. 4-bit 7-seg multiplexing? → scan digits, save IO pins.

## See also

- Level 2 (comms, sensors, MCUs, op-amps, encoders, mux): [[nexus-components-viva-level2]]
- Interview theory bank: [[nexus-theory-rapidfire]] · Morning sheet: [[nexus-master-cheatsheet]] · INDEX: [[01-Areas/Engineering/nexus-robotics/INDEX]]
- Rulebook viva: [[nexus-robocon-rulebook-viva]]
- BEE protection/fuses theory: [[01-Areas/Engineering/BEE/module-5-installations-safety-energy]]
