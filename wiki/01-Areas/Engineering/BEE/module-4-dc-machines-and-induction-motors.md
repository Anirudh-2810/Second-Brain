---
course_code: "BEE"
course_name: "Basic Electrical Engineering"
unit: "Module 4 — DC Machines & Three-Phase Induction Motors"
tags: [bee, dc-generator, dc-motor, induction-motor, emf-equation, torque, slip]
last_updated: "2026-08-25"
confidence: "high"
---

## For future agent
Module 4 of BEE (MU pattern): DC generator/motor principles and the three-phase induction motor. Derivations (EMF, back-EMF, torque) + slip numericals are the guaranteed questions. Motors reappear in [[modules/../01-Areas/Engineering/robotics/robotics-fundamentals|robotics fundamentals]] — same physics driving actuators. All formulas in [[formula-sheet-bee]].

# DC Machines & Three-Phase Induction Motors

## 1. Construction (common to generator & motor)

- **Yoke** (frame), **poles + field windings** (produce flux Φ), **armature** (rotating core carrying conductors), **commutator** (mechanical rectifier — converts internal AC to external DC), **brushes** (carbon contacts)

**Two governing laws**:
- Generator: **Faraday** — conductor moves in flux → EMF induced: $e = Blv$
- Motor: **Lorentz force** — current-carrying conductor in flux → force $F = BIl$
- Both: $e$ and $F$ directions by **Fleming's Right/Left-hand rules** respectively

## 2. DC Generator

### EMF Equation (derive — guaranteed)
Average EMF per conductor: $e_{avg} = \dfrac{\Phi P}{60/A}\cdot Z$ … combining flux cut per second:

$$\boxed{E_g = \frac{P\,\Phi\,Z\,N}{60\,A}} \quad \text{volts}$$

- $P$ = poles, $\Phi$ = flux per pole (Wb), $Z$ = total armature conductors, $N$ = speed (RPM), $A$ = parallel paths
- **Wave winding**: $A = 2$ (high voltage, low current) · **Lap winding**: $A = P$ (high current, low voltage)

### Types & characteristics
| Type | Field connection | Behavior | Use |
|------|-----------------|----------|-----|
| Separately excited | Independent source | Full control | Ward-Leonard drives, testing |
| Shunt | Parallel with armature | ~Constant voltage | Battery charging, lighting |
| Series | In series with armature | $E \propto \Phi \propto I_a$ → rises with load | Traction, cranes (never open-load — runs away) |
| Compound | Both | Compromise | Welding, elevators |

## 3. DC Motor

Same machine, reversed energy flow: supply current + flux → torque. Back-EMF $E_b$ opposes supply (Lenz):
$$E_b = \frac{P\Phi Z N}{60A}, \qquad V = E_b + I_aR_a$$

**Back-EMF is self-regulation**: load ↑ → N ↓ → $E_b$ ↓ → $I_a = \dfrac{V-E_b}{R_a}$ ↑ → torque ↑ until balance. This is why DC motors self-adjust without a controller.

### Torque equation
$$T_a = \frac{1}{2\pi}\cdot\frac{P\Phi Z I_a}{A} \quad \text{N·m} \qquad\text{or}\qquad T_a = 0.159\,\frac{P Z \Phi I_a}{A}$$
Mechanical power developed: $P_{dev} = E_b I_a = T_a\,\omega$ → $T_a = \dfrac{E_b I_a}{2\pi N/60} = 9.55\,\dfrac{E_b I_a}{N}$

### Speed equation (the workhorse)
$$N \propto \frac{E_b}{\Phi} = \frac{V - I_aR_a}{\Phi}$$
**Speed control falls out directly**: field control (↓Φ → ↑N), armature control (↓V → ↓N), or chopper/PWM in modern drives.

### Starting problem
At standstill $E_b = 0$ → $I_{start} = V/R_a$ with tiny $R_a$ → **10–20× full-load current**. Fix: starter (series starting resistance, cut out progressively) or soft-start electronics.

## 4. Three-Phase Induction Motor

### Construction
- **Stator**: 3-φ winding on laminated core — fed with 3-phase AC
- **Rotor**: squirrel cage (bars + end rings — rugged, 90% of industry) or wound (slip rings, external resistance for starting torque)

### Rotating Magnetic Field (the magic)
Three coils 120° apart, fed 120°-apart currents → resultant flux of CONSTANT magnitude $\dfrac{3}{2}\Phi_m$ rotating at **synchronous speed**:
$$N_s = \frac{120 f}{P} \quad \text{RPM}$$
(50 Hz, 4 poles → 1500 RPM). The rotor conductors see this rotating field → relative motion → induced EMF → rotor current → Lorentz force → rotor chases the field. It can NEVER catch it (no relative motion = no induction = no torque).

### Slip
$$s = \frac{N_s - N}{N_s} \times 100\%$$
- At start: $N = 0$ → $s = 1$ (max torque conditions)
- At full load: 2–5% (4-pole motor ≈ 1440–1470 RPM)
- Rotor frequency: $f_r = s f$

### Torque & starting
Torque ∝ $s E_2^2 R_2 / (R_2^2 + (sX_2)^2)$ — starting torque is modest for squirrel cage (low $R_2$). Starting methods: **DOL** (small motors), **star-delta starter** (reduces starting current to 1/3, torque to 1/3), **rotor resistance** (wound rotor only — raises starting torque).

### Losses & efficiency chain
Input → stator Cu+Fe losses → air-gap power → rotor Cu loss ($= s \times$ air-gap power!) → mechanical → friction. So efficiency ceiling ≈ $1 - s$: a 5% slip motor wastes 5% in the rotor.

## 5. Worked Example (exam pattern)

*4-pole, 3-φ induction motor, 50 Hz, runs at 1440 RPM. Find $N_s$, slip, rotor frequency. If air-gap power = 10 kW, find rotor copper loss.*

1. $N_s = \dfrac{120 \times 50}{4} = 1500$ RPM
2. $s = \dfrac{1500-1440}{1500} = 0.04 = 4\%$
3. $f_r = 0.04 \times 50 = 2$ Hz
4. Rotor Cu loss = $s \times P_{airgap} = 0.04 \times 10\,000 = 400$ W → mechanical power = 9600 W

## 6. Failure Modes (exam)

| Trap | Fix |
|------|-----|
| A = P vs A = 2 confusion | Lap → A = P (parallel paths per pole pair pair); Wave → A = 2 |
| Slip stated without % or fraction | Be explicit; rotor frequency uses the fraction |
| "Induction motor runs at synchronous speed" | Never — s = 0 kills induction; it always slips |
| DC motor started without starter | Quote $I_a = V/R_a$ arithmetic — the examiner wants the 10–20× number |

## Related

[[module-3-magnetic-circuits-and-transformers]] (flux + EMF machinery shared) · [[formula-sheet-bee]] · [[modules/../01-Areas/Engineering/robotics/robotics-fundamentals|robotics fundamentals]] (actuators) · [[module-5-installations-safety-energy]] (motors in installations)