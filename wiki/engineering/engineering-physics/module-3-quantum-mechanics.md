---
module: "engineering-physics"
topic: "Module 3: Quantum Mechanics (Deep Dive)"
tags: [quantum-mechanics, wave-particle-duality, schrodinger, hydrogen-atom, uncertainty-principle, tunneling, photoelectric-effect, compton-scattering, harmonic-oscillator, particle-in-a-box]
last_updated: "2026-08-17"
prerequisites: ["Wave Motion", "Photoelectric Effect", "Bohr Model", "Basic Linear Algebra", "Calculus"]
---

# Module 3: Quantum Mechanics (Deep Dive)

> The revolutionary framework that describes nature at the atomic scale — where particles are waves, measurements change reality, and certainty gives way to probability.

**Target Audience:** Engineering Physics students (B.Tech / B.E.)
**Estimated Study Time:** 25–30 hours for complete mastery

---

## Table of Contents

1. [Historical Foundations](#1-historical-foundations)
2. [Wave-Particle Duality](#2-wave-particle-duality)
3. [Wave Function and Schrödinger Equation](#3-wave-function-and-schrodinger-equation)
4. [Particle in a Box (Infinite Square Well)](#4-particle-in-a-box-infinite-square-well)
5. [Quantum Harmonic Oscillator](#5-quantum-harmonic-oscillator)
6. [Hydrogen Atom](#6-hydrogen-atom)
7. [Spin and Angular Momentum](#7-spin-and-angular-momentum)
8. [Identical Particles and Exclusion Principle](#8-identical-particles-and-exclusion-principle)
9. [Quantum Tunneling](#9-quantum-tunneling)
10. [Quantum Measurement](#10-quantum-measurement)
11. [Advanced Topics](#11-advanced-topics)
12. [Worked Examples (10–15 Complete Solutions)](#12-worked-examples)
13. [Common Mistakes and Traps](#13-common-mistakes-and-traps)
14. [Quick-Reference Formula Tables](#14-quick-reference-formula-tables)
15. [Cross-References](#15-cross-references)

---

## 1. Historical Foundations

### 1.1 Failures of Classical Physics

Classical mechanics and electromagnetism, despite their enormous success at the macroscopic scale, failed spectacularly when applied to atomic and subatomic phenomena. Four key experimental observations defied classical explanation:

**Blackbody radiation:**
- Classical prediction (Rayleigh-Jeans): $u(\nu, T) = \frac{8\pi\nu^2}{c^3} kT$
- This diverges at high frequencies → the **ultraviolet catastrophe**
- Experiment: intensity peaks at a finite frequency that shifts with temperature (Wien's law)
- Classical physics predicts infinite total radiated power: $U = \int_0^\infty u \, d\nu \to \infty$

**Photoelectric effect:**
- Classical expectation: light intensity should determine the kinetic energy of ejected electrons
- Observation: frequency determines kinetic energy; a threshold frequency exists below which no electrons are emitted regardless of intensity
- Intensity only affects the number (current) of emitted electrons, not their energy
- Emission is instantaneous (< 10⁻⁹ s) even at very low intensity — classical wave would need time to accumulate energy

**Atomic stability:**
- Classical electrodynamics: an accelerating charge (orbiting electron) must radiate energy
- Predicted: electron spirals into nucleus in ~10⁻¹¹ s
- Observed: atoms are stable; electrons occupy well-defined orbits
- Classical atoms should not emit discrete spectral lines

**Specific heats of solids:**
- Classical (Dulong-Petit): $C_V = 3R$ for all temperatures
- Experiment: $C_V \to 0$ as $T \to 0$
- Classical theory cannot explain the temperature dependence

```
 CLASSICAL vs QUANTUM: Summary of Failures
 ===========================================

 Phenomenon        Classical Prediction       Quantum Result
 -----------------------------------------------------------------
 Blackbody         UV catastrophe (infinite    Planck's law matches
                   energy at high freq)        experiment exactly

 Photoelectric     Intensity determines KE     Frequency determines KE
 effect            of ejected electrons        threshold frequency exists

 Atomic            Electron radiates and       Stable orbits with
 stability         collapses into nucleus      quantized energy levels

 Specific Heat     C_V = 3R at all T          C_V → 0 as T → 0
 -----------------------------------------------------------------
```

### 1.2 Planck's Quantum Hypothesis (1900)

Max Planck resolved the blackbody problem by postulating that energy exchange between matter and radiation occurs in discrete packets called **quanta**:

$$E = nh\nu \quad n = 0, 1, 2, \ldots$$

**Derivation of Planck's radiation law:**

Starting from the average energy of a quantum oscillator at temperature $T$:

$$\langle E \rangle = \frac{\sum_{n=0}^{\infty} nh\nu \, e^{-nh\nu/kT}}{\sum_{n=0}^{\infty} e^{-nh\nu/kT}}$$

Let $x = h\nu / kT$. Then:

$$\langle E \rangle = h\nu \frac{\sum_{n=0}^{\infty} n \, e^{-nx}}{\sum_{n=0}^{\infty} e^{-nx}} = h\nu \frac{-d/dx \sum e^{-nx}}{\sum e^{-nx}} = h\nu \frac{-d/dx \left(\frac{1}{1-e^{-x}}\right)}{\frac{1}{1-e^{-x}}}$$

$$\langle E \rangle = h\nu \frac{e^{-x}}{(1-e^{-x})} = \frac{h\nu}{e^{h\nu/kT} - 1}$$

Multiplying by the density of electromagnetic modes $g(\nu) = \frac{8\pi\nu^2}{c^3}$:

$$\boxed{u(\nu, T) = \frac{8\pi h\nu^3}{c^3} \cdot \frac{1}{e^{h\nu/kT} - 1}}$$

**Planck's constant:** $h = 6.626 \times 10^{-34}$ J·s $= 4.136 \times 10^{-15}$ eV·s

**Reduced Planck's constant:** $\hbar = \frac{h}{2\pi} = 1.055 \times 10^{-34}$ J·s $= 6.582 \times 10^{-16}$ eV·s

**Limits of Planck's law:**
- Low frequency ($h\nu \ll kT$): $u \to \frac{8\pi\nu^2}{c^3} kT$ (Rayleigh-Jeans, classical)
- High frequency ($h\nu \gg kT$): $u \to \frac{8\pi h\nu^3}{c^3} e^{-h\nu/kT}$ (Wien's law)

### 1.3 Einstein's Photon Theory (1905)

Einstein extended Planck's idea: light itself consists of discrete energy packets called **photons** (not just matter):

$$\boxed{E_{\text{photon}} = h\nu = \frac{hc}{\lambda}}$$

**Photon momentum:**

$$p_{\text{photon}} = \frac{E}{c} = \frac{h\nu}{c} = \frac{h}{\lambda}$$

**Photoelectric equation (derivation):**

A photon of energy $h\nu$ strikes a metal surface. The electron must overcome the work function $\phi$ (minimum energy to escape). By conservation of energy:

$$h\nu = \phi + K_{\max}$$

$$\boxed{K_{\max} = h\nu - \phi = eV_s}$$

where $V_s$ is the stopping potential.

**Key relationships:**
- Threshold frequency: $\nu_0 = \phi/h$
- Threshold wavelength: $\lambda_0 = hc/\phi$
- No emission below $\nu_0$ regardless of intensity
- $K_{\max}$ depends linearly on $\nu$ (not on intensity)
- Intensity determines the photocurrent (number of photoelectrons per second)
- Emission is instantaneous (< 10⁻⁹ s)

### 1.4 Compton Effect (1923)

When X-rays scatter off electrons, the scattered radiation has a longer wavelength than the incident radiation — a shift that depends on the scattering angle. This cannot be explained by classical wave theory (which predicts no frequency change).

**Derivation of Compton shift:**

Consider a photon with initial energy $E = h\nu$ and momentum $\vec{p} = h\vec{\nu}/c$ scattering off a stationary free electron.

Conservation of energy:

$$h\nu + m_e c^2 = h\nu' + \sqrt{m_e^2 c^4 + (h\nu')^2 c^2 - 2h\nu' m_e c^3 \cos\theta + h^2\nu'^2}$$

Wait — let's write this more carefully using 4-vector notation.

Conservation of energy and momentum give us:

$$h\nu = h\nu' + K_e$$

$$\frac{h\nu}{c} = \frac{h\nu'}{c}\cos\theta + p_e \cos\phi$$

$$0 = \frac{h\nu'}{c}\sin\theta - p_e \sin\phi$$

Eliminating the electron momentum $p_e$ and using $K_e = p_e^2/(2m_e)$ (non-relativistic) or the relativistic relation, after algebra:

$$\boxed{\Delta\lambda = \lambda' - \lambda = \frac{h}{m_e c}(1 - \cos\theta)}$$

**Compton wavelength:** $\lambda_C = \frac{h}{m_e c} = 2.426 \times 10^{-12}$ m $= 0.00243$ nm

**Key features:**
- Shift is independent of the incident wavelength
- Maximum shift at $\theta = 180°$: $\Delta\lambda_{\max} = 2\lambda_C = 0.00486$ nm
- Confirms photons carry momentum: $p = h/\lambda = E/c$
- At small angles: shift is negligible (classical scattering recovered)

```
 COMPTON SCATTERING DIAGRAM
 ===========================

                    Scattered photon
                    (lower energy)
                   \  θ
                    \|
     Photon    ======>O-------->  Scattered photon
     hν              /|
                    / |
                   /  φ
              Electron
            (recoil)

     θ = scattering angle of photon
     φ = recoil angle of electron

     λ' - λ = (h/m_ec)(1 - cos θ)
```

### 1.5 De Broglie's Unification (1924)

Louis de Broglie proposed the bold hypothesis that **all matter** has wave properties, not just light:

$$\boxed{\lambda_{\text{matter}} = \frac{h}{p}}$$

This was confirmed experimentally by Davisson and Germer (1927) using electron diffraction from nickel crystals, and independently by G.P. Thomson using thin metal foils.

---

## 2. Wave-Particle Duality

### 2.1 de Broglie Hypothesis (1924)

**Matter waves:** Every particle with momentum $p$ has an associated wavelength:

$$\boxed{\lambda = \frac{h}{p} = \frac{h}{mv}}$$

**For a non-relativistic particle accelerated through potential $V$:**

Starting from $K = eV = \frac{1}{2}mv^2$:

$$p = mv = \sqrt{2mK} = \sqrt{2meV}$$

$$\boxed{\lambda = \frac{h}{\sqrt{2meV}}}$$

**Numerical values:**

| Particle | Condition | de Broglie Wavelength | Comparable to... |
|----------|-----------|----------------------|------------------|
| Electron | 100 V | 0.123 nm | Atomic spacing (~0.1 nm) |
| Electron | 10 kV | 0.012 nm | X-ray wavelength |
| Electron | 100 kV | 0.0037 nm | Nuclear size |
| Proton | 100 V | 2.86 × 10⁻³ nm | — |
| Neutron | Thermal (0.025 eV) | 0.18 nm | Crystal spacing |
| Baseball | 30 m/s | 1.5 × 10⁻³⁴ m | ~10⁻⁶ of proton radius |

**Key insight:** The wave nature of matter is significant only when $\lambda$ is comparable to the size of the system. For macroscopic objects, $\lambda$ is absurdly small and quantum effects are unobservable.

### 2.2 Davisson-Germer Experiment (1927)

Electrons fired at a nickel crystal surface produce a diffraction pattern — just like X-rays diffracting from crystal planes.

**Bragg's law:** $n\lambda = 2d\sin\theta$

For 54 eV electrons and nickel ($d = 0.091$ nm), the predicted first-order diffraction angle matches experiment exactly when using the de Broglie wavelength.

### 2.3 The Wave Packet and Group Velocity

A free particle is not described by a single plane wave $e^{i(kx-\omega t)}$ (which extends over all space), but by a **wave packet** — a superposition of plane waves:

$$\Psi(x,t) = \int_{-\infty}^{\infty} A(k) e^{i(kx - \omega t)} dk$$

**Group velocity** (velocity of the packet, i.e., the particle):

$$v_g = \frac{d\omega}{dk} = \frac{dE}{dp} = v_{\text{particle}}$$

**Phase velocity** (velocity of the carrier wave):

$$v_p = \frac{\omega}{k} = \frac{E}{p} = \frac{pc^2}{pc} = \frac{c^2}{v_g}$$

Note: $v_p \times v_g = c^2$, and $v_p > c$ for massive particles. This does not violate relativity because no information travels at $v_p$.

### 2.4 Heisenberg Uncertainty Principle

$$\boxed{\Delta x \cdot \Delta p \geq \frac{\hbar}{2}}$$

where $\hbar = h/(2\pi) = 1.055 \times 10^{-34}$ J·s

**Derivation (simplified):**

Consider a wave packet constructed from plane waves with wave number spread $\Delta k$:

$$\Delta x \sim \frac{1}{\Delta k}, \quad \Delta p = \hbar \Delta k$$

$$\Delta x \cdot \Delta p \sim \hbar$$

Rigorous proof using the Cauchy-Schwarz inequality gives the exact result $\hbar/2$.

**Other conjugate uncertainty relations:**
- Energy-time: $\Delta E \cdot \Delta t \geq \hbar/2$
- Angular momentum-angle: $\Delta L \cdot \Delta\phi \geq \hbar/2$

**General form for any two observables:**

$$\Delta A \cdot \Delta B \geq \frac{1}{2}\left|[\hat{A}, \hat{B}]\right|$$

where $[\hat{A}, \hat{B}] = \hat{A}\hat{B} - \hat{B}\hat{A}$ is the commutator.

**Physical meaning:**
- NOT a limitation of measurement technology — a fundamental property of nature
- Conjugate variables cannot both have precise values simultaneously
- For position-momentum: $[\hat{x}, \hat{p}] = i\hbar$
- Explains zero-point energy: a confined particle cannot be at rest (that would require $\Delta p = 0$ and $\Delta x = 0$, violating HUP)

**Numerical applications:**
- Electron in atom ($\Delta x \sim 10^{-10}$ m): $\Delta p \sim 10^{-24}$ kg·m/s → $\Delta v \sim 10^6$ m/s
- Proton in nucleus ($\Delta x \sim 10^{-15}$ m): $\Delta p \sim 10^{-19}$ kg·m/s → very high momentum → explains nuclear binding energy scale

```
 HEISENBERG UNCERTAINTY PRINCIPLE: Decision Tree
 =================================================

 Is the question about position-momentum?
 |
 YES ──> Use: Δx · Δp ≥ ℏ/2
 |
 NO
 |
 Is it about energy-time?
 |
 YES ──> Use: ΔE · Δt ≥ ℏ/2
 |
 NO
 |
 Is it about angular momentum-angle?
 |
 YES ──> Use: ΔL · Δφ ≥ ℏ/2
 |
 NO
 |
 Use the general form:
 ΔA · ΔB ≥ |[A,B]| / 2
```

---

## 3. Wave Function and Schrödinger Equation

### 3.1 Wave Function $\Psi(x,t)$

The wave function contains **all information** about a quantum system. It is a complex-valued function of space and time.

**Born's interpretation (1926):** $|\Psi(x,t)|^2$ is the **probability density** for finding the particle at position $x$ at time $t$.

$$P(a \leq x \leq b) = \int_a^b |\Psi(x,t)|^2 dx$$

**Properties of the wave function:**
1. Single-valued (probability must be unique at each point)
2. Continuous (probability cannot have abrupt jumps)
3. Square-integrable ($\int_{-\infty}^{\infty} |\Psi|^2 dx < \infty$)
4. Goes to zero at infinity (particle must be somewhere)

**Normalization:**

$$\boxed{\int_{-\infty}^{\infty} |\Psi(x,t)|^2 dx = 1}$$

If $\Psi$ is not normalized, we normalize by dividing by $\sqrt{N}$ where $N = \int |\Psi|^2 dx$.

### 3.2 Time-Dependent Schrödinger Equation

$$\boxed{i\hbar \frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m} \frac{\partial^2 \Psi}{\partial x^2} + V(x)\Psi}$$

**For 3D:**

$$i\hbar \frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m} \nabla^2 \Psi + V(\vec{r})\Psi$$

**Derivation (heuristic):**

Starting from a plane wave $\Psi = Ae^{i(kx - \omega t)}$:

$$\frac{\partial \Psi}{\partial t} = -i\omega \Psi \quad \Rightarrow \quad i\hbar\frac{\partial \Psi}{\partial t} = \hbar\omega \Psi = E\Psi$$

$$\frac{\partial^2 \Psi}{\partial x^2} = -k^2 \Psi \quad \Rightarrow \quad -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} = \frac{\hbar^2 k^2}{2m}\Psi = \frac{p^2}{2m}\Psi$$

Adding potential energy: $E = \frac{p^2}{2m} + V(x)$, so:

$$E\Psi = \frac{p^2}{2m}\Psi + V\Psi \quad \Rightarrow \quad i\hbar\frac{\partial \Psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2 \Psi}{\partial x^2} + V\Psi$$

### 3.3 Time-Independent Schrödinger Equation

For stationary states where the potential does not depend on time, we use **separation of variables**:

$$\Psi(x,t) = \psi(x) \cdot T(t) = \psi(x) \cdot e^{-iEt/\hbar}$$

Substituting into the TDSE:

$$\boxed{-\frac{\hbar^2}{2m} \frac{d^2\psi}{dx^2} + V(x)\psi = E\psi}$$

This is an **eigenvalue equation**: $\hat{H}\psi = E\psi$

**Hamiltonian operator:** $\hat{H} = -\frac{\hbar^2}{2m}\nabla^2 + V(\vec{r})$

**Key points:**
- $E$ is the total energy (eigenvalue)
- $\psi(x)$ is the spatial part of the wave function (eigenfunction)
- Only certain values of $E$ give valid (normalizable) solutions → energy quantization
- The time dependence $e^{-iEt/\hbar}$ gives $|\Psi|^2 = |\psi(x)|^2$ which is time-independent for stationary states

---

## 4. Particle in a Box (Infinite Square Well)

### 4.1 One-Dimensional Box

**Potential:**

$$V(x) = \begin{cases} 0 & 0 < x < L \\ \infty & \text{otherwise} \end{cases}$$

```
    INFINITE SQUARE WELL
    =====================

    V(x)
    |          
 ∞  |█         █
    |█         █
    |█         █
    |█         █
    |█  V = 0  █
    |█         █
    |█_________█
    0    L/2    L ──> x
         ψ₁(x) ∝ sin(πx/L)

    █ = impenetrable walls
```

**Solution:**

Inside the box ($V = 0$), the TISE becomes:

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi \quad \Rightarrow \quad \frac{d^2\psi}{dx^2} = -k^2\psi$$

where $k = \sqrt{2mE}/\hbar$.

General solution: $\psi(x) = A\sin(kx) + B\cos(kx)$

**Boundary conditions:**
- $\psi(0) = 0 \Rightarrow B = 0$
- $\psi(L) = 0 \Rightarrow A\sin(kL) = 0 \Rightarrow kL = n\pi$, $n = 1, 2, 3, \ldots$

**Wave function (after normalization):**

$$\boxed{\psi_n(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{n\pi x}{L}\right) \quad n = 1, 2, 3, \ldots}$$

**Energy levels:**

$$k_n = \frac{n\pi}{L} = \frac{\sqrt{2mE_n}}{\hbar}$$

$$\boxed{E_n = \frac{n^2 \pi^2 \hbar^2}{2mL^2} = \frac{n^2 h^2}{8mL^2} \quad n = 1, 2, 3, \ldots}$$

**Normalization derivation:**

$$\int_0^L |\psi_n|^2 dx = \frac{2}{L}\int_0^L \sin^2\left(\frac{n\pi x}{L}\right) dx = \frac{2}{L} \cdot \frac{L}{2} = 1 \quad \checkmark$$

**Key features:**
- Energy is **quantized** — only discrete values allowed
- **Zero-point energy** ($n=1$): $E_1 = \frac{h^2}{8mL^2} \neq 0$ (consequence of uncertainty principle)
- Energy spacing increases with $n$: $E_{n+1} - E_n = (2n+1)\frac{h^2}{8mL^2}$
- Number of nodes (zero crossings): $n - 1$
- Wave functions are **orthogonal**: $\int_0^L \psi_m^* \psi_n dx = \delta_{mn}$
- Wave functions form a **complete set** — any function in $[0, L]$ can be expanded as a Fourier sine series of these $\psi_n$

```
    ENERGY LEVELS AND WAVE FUNCTIONS
    ==================================

    E₄ = 16 E₁  ─────  ψ₄: 3 nodes

    E₃ = 9 E₁   ─────  ψ₃: 2 nodes

    E₂ = 4 E₁   ─────  ψ₂: 1 node

    E₁           ─────  ψ₁: 0 nodes

    |  sin(πx/L) |  sin(2πx/L) |  sin(3πx/L) |  sin(4πx/L)
    |    /\      |    /\  /\   |   /\ /\     |  /\  /\
    |   /  \     |   /  \/  \  |  /  X  \    | /  \/  \
    |--/----\----|--/--------\-|-/---|---\---|-/--------\-
    | /      \   | /          \|/    |    \  |/          \
    0          L 0            L 0           L 0           L
```

### 4.2 Three-Dimensional Box (Rectangular)

$$E_{n_x, n_y, n_z} = \frac{h^2}{8m}\left(\frac{n_x^2}{L_x^2} + \frac{n_y^2}{L_y^2} + \frac{n_z^2}{L_z^2}\right)$$

**For a cubic box** ($L_x = L_y = L_z = L$):

$$E_{n_x, n_y, n_z} = \frac{h^2}{8mL^2}(n_x^2 + n_y^2 + n_z^2)$$

**Degeneracy:** Multiple quantum states can have the same energy.

Example: $E_{211} = E_{121} = E_{112}$ → 3-fold degenerate (ignoring spin).

### 4.3 Probability and Expectation Values in the Box

**Probability of finding the particle in $[a, b]$:**

$$P(a \leq x \leq b) = \frac{2}{L}\int_a^b \sin^2\left(\frac{n\pi x}{L}\right) dx$$

**Expectation value of position:**

$$\langle x \rangle = \frac{2}{L}\int_0^L x\sin^2\left(\frac{n\pi x}{L}\right) dx = \frac{L}{2}$$

(This makes sense by symmetry — the average position is always the center.)

**Expectation value of $x^2$:**

$$\langle x^2 \rangle = \frac{2}{L}\int_0^L x^2\sin^2\left(\frac{n\pi x}{L}\right) dx = L^2\left(\frac{1}{3} - \frac{1}{2n^2\pi^2}\right)$$

**Position uncertainty:**

$$\Delta x = \sqrt{\langle x^2\rangle - \langle x\rangle^2} = L\sqrt{\frac{1}{12} - \frac{1}{2n^2\pi^2}}$$

For $n = 1$: $\Delta x = L\sqrt{\frac{1}{12} - \frac{1}{2\pi^2}} \approx 0.183L$

**Expectation value of momentum:**

$$\langle p \rangle = 0$$

(This makes sense — the particle is equally likely to move left or right.)

**Expectation value of $p^2$:**

$$\langle p^2 \rangle = 2mE_n = \frac{n^2\pi^2\hbar^2}{L^2}$$

**Momentum uncertainty:**

$$\Delta p = \frac{n\pi\hbar}{L}$$

**Verification of uncertainty principle:**

$$\Delta x \cdot \Delta p = L\sqrt{\frac{1}{12} - \frac{1}{2n^2\pi^2}} \cdot \frac{n\pi\hbar}{L} = n\pi\hbar\sqrt{\frac{1}{12} - \frac{1}{2n^2\pi^2}} \geq \frac{\hbar}{2}$$

For $n = 1$: $\Delta x \cdot \Delta p = \pi\hbar\sqrt{1/12 - 1/(2\pi^2)} \approx 0.569\hbar > \hbar/2$ ✓

### 4.4 Transitions Between Energy Levels

When a particle transitions from state $n_i$ to state $n_f$ ($n_f < n_i$), the energy difference is emitted as a photon:

$$\Delta E = E_{n_i} - E_{n_f} = \frac{h^2}{8mL^2}(n_i^2 - n_f^2)$$

The emitted photon has wavelength:

$$\lambda = \frac{hc}{\Delta E} = \frac{8mcL^2}{h(n_i^2 - n_f^2)}$$

---

## 5. Quantum Harmonic Oscillator

### 5.1 Classical vs Quantum

**Classical potential:** $V(x) = \frac{1}{2}m\omega^2 x^2$

A mass on a spring oscillates with angular frequency $\omega = \sqrt{k/m}$. Classically, the energy can take any value from 0 to $\infty$.

**Quantum result:** Energy is quantized:

$$\boxed{E_n = \left(n + \frac{1}{2}\right)\hbar\omega \quad n = 0, 1, 2, \ldots}$$

```
    QUANTUM HARMONIC OSCILLATOR: Energy Levels
    =============================================

    E
    ^
    |
 6ℏω|          ───── n=5
    |
 5ℏω|       ───── n=4
    |
 4ℏω|    ───── n=3
    |
 3ℏω| ───── n=2
    |
 2ℏω|─── n=1
    |
 ½ℏω|─── n=0  ← Zero-point energy
    |
    |      V(x) = ½mω²x²
    |     /
    |    /
    |   /
    |  /
    | /
    |/_____________ x
```

**Key features:**
- Equally spaced energy levels: $\Delta E = \hbar\omega$
- Zero-point energy: $E_0 = \frac{1}{2}\hbar\omega \neq 0$
- Wave functions involve Hermite polynomials $H_n(\xi)$:

$$\psi_n(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4} \frac{1}{\sqrt{2^n n!}} H_n\left(\sqrt{\frac{m\omega}{\hbar}}x\right) e^{-m\omega x^2/(2\hbar)}$$

**First few Hermite polynomials:**
- $H_0(\xi) = 1$
- $H_1(\xi) = 2\xi$
- $H_2(\xi) = 4\xi^2 - 2$
- $H_3(\xi) = 8\xi^3 - 12\xi$

### 5.2 Raising and Lowering Operators (Algebraic Method)

The Schrödinger equation for the harmonic oscillator can be solved elegantly without calculus, using **ladder operators**:

**Annihilation (lowering) operator:**

$$\hat{a} = \sqrt{\frac{m\omega}{2\hbar}}\left(\hat{x} + \frac{i\hat{p}}{m\omega}\right)$$

**Creation (raising) operator:**

$$\hat{a}^\dagger = \sqrt{\frac{m\omega}{2\hbar}}\left(\hat{x} - \frac{i\hat{p}}{m\omega}\right)$$

**Commutation relation:** $[\hat{a}, \hat{a}^\dagger] = 1$

**Number operator:** $\hat{n} = \hat{a}^\dagger \hat{a}$

The Hamiltonian can be rewritten as:

$$\hat{H} = \hbar\omega\left(\hat{a}^\dagger \hat{a} + \frac{1}{2}\right) = \hbar\omega\left(\hat{n} + \frac{1}{2}\right)$$

**Action of ladder operators:**
- $\hat{a}|n\rangle = \sqrt{n}|n-1\rangle$ (lowers energy by $\hbar\omega$)
- $\hat{a}^\dagger|n\rangle = \sqrt{n+1}|n+1\rangle$ (raises energy by $\hbar\omega$)

**Why the energy is quantized:** The state $|0\rangle$ (ground state) satisfies $\hat{a}|0\rangle = 0$. Applying $\hat{a}$ to $|0\rangle$ must give zero (there's no $|-1\rangle$ state), which forces $E_0 = \frac{1}{2}\hbar\omega$.

**Expectation values in the ground state:**

$$\langle x \rangle_0 = 0, \quad \langle x^2 \rangle_0 = \frac{\hbar}{2m\omega}$$

$$\langle p \rangle_0 = 0, \quad \langle p^2 \rangle_0 = \frac{m\omega\hbar}{2}$$

$$\Delta x_0 = \sqrt{\frac{\hbar}{2m\omega}}, \quad \Delta p_0 = \sqrt{\frac{m\omega\hbar}{2}}$$

$$\Delta x_0 \cdot \Delta p_0 = \frac{\hbar}{2} \quad \text{(minimum uncertainty state!)}$$

The ground state of the harmonic oscillator is a **minimum uncertainty state** (also called a **coherent state** when generalized).

### 5.3 Classical Limit

At high quantum numbers ($n \gg 1$), the probability density $|\psi_n(x)|^2$ oscillates rapidly and its average approaches the classical probability distribution, which is higher near the turning points (where the classical particle spends more time). This is an illustration of the **correspondence principle**.

---

## 6. Hydrogen Atom

### 6.1 The Hydrogen Atom Problem

The hydrogen atom consists of a proton and an electron interacting via the Coulomb potential:

$$V(r) = -\frac{e^2}{4\pi\epsilon_0 r}$$

In spherical coordinates $(r, \theta, \phi)$, the Schrödinger equation separates into radial and angular parts.

### 6.2 Separation of Variables

$$\psi_{nlm}(r, \theta, \phi) = R_{nl}(r) \cdot Y_l^m(\theta, \phi)$$

**Radial part:** $R_{nl}(r)$ involves associated Laguerre polynomials:

$$R_{nl}(r) = N_{nl} \left(\frac{2r}{na_0}\right)^l e^{-r/(na_0)} L_{n-l-1}^{2l+1}\left(\frac{2r}{na_0}\right)$$

**Angular part:** $Y_l^m(\theta, \phi)$ are spherical harmonics:

$$Y_l^m(\theta, \phi) = \sqrt{\frac{(2l+1)}{4\pi}\frac{(l-m)!}{(l+m)!}} P_l^m(\cos\theta) e^{im\phi}$$

where $P_l^m$ are associated Legendre polynomials.

### 6.3 Energy Levels

$$\boxed{E_n = -\frac{13.6 \text{ eV}}{n^2} = -\frac{me^4}{8\epsilon_0^2 h^2 n^2}}$$

**Bohr radius:** $a_0 = \frac{4\pi\epsilon_0 \hbar^2}{me^2} = 0.529$ Å $= 5.29 \times 10^{-11}$ m

**Derivation sketch of energy levels:**

The radial Schrödinger equation for hydrogen:

$$-\frac{\hbar^2}{2m_e}\frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{dR}{dr}\right) + \left[\frac{l(l+1)\hbar^2}{2m_e r^2} - \frac{e^2}{4\pi\epsilon_0 r}\right]R = ER$$

The effective potential is:

$$V_{\text{eff}}(r) = -\frac{e^2}{4\pi\epsilon_0 r} + \frac{l(l+1)\hbar^2}{2m_e r^2}$$

The centrifugal term $\frac{l(l+1)\hbar^2}{2m_e r^2}$ prevents the electron from reaching $r = 0$ (except for $l = 0$).

Solving with the boundary condition $R(r) \to 0$ as $r \to \infty$ gives quantized energies:

$$E_n = -\frac{m_e e^4}{2(4\pi\epsilon_0)^2\hbar^2 n^2} = -\frac{13.6 \text{ eV}}{n^2}$$

```
    HYDROGEN ATOM ENERGY LEVELS
    ============================

    E (eV)
    ^
  0 ──────────────────────── n = ∞  (ionization)
    |
 -0.54 ───────────────────── n = 5
    |
 -0.85 ───────────────────── n = 4
    |
 -1.51 ───────────────────── n = 3
    |
 -3.4  ───────────────────── n = 2
    |
    |
 -13.6 ───────────────────── n = 1  (ground state)

    Series:
    Lyman  (n₁=1): UV   (n₂ = 2,3,4,...)
    Balmer (n₁=2): Visible (n₂ = 3,4,5,...)
    Paschen (n₁=3): IR   (n₂ = 4,5,6,...)
    Brackett (n₁=4): Far IR (n₂ = 5,6,...)
    Pfund  (n₁=5): Far IR (n₂ = 6,7,...)
```

### 6.4 Quantum Numbers

| Quantum Number | Symbol | Values | Physical Meaning |
|---------------|--------|--------|------------------|
| Principal | $n$ | $1, 2, 3, \ldots$ | Energy, size of orbital |
| Orbital angular momentum | $l$ | $0, 1, \ldots, n-1$ | Shape of orbital |
| Magnetic | $m_l$ | $-l, -l+1, \ldots, +l$ | Orientation in space |
| Spin | $m_s$ | $+1/2$ or $-1/2$ | Intrinsic angular momentum |

**Angular momentum quantization:**

$$L = \sqrt{l(l+1)}\hbar \quad \text{(total orbital angular momentum)}$$

$$L_z = m_l\hbar \quad \text{(z-component only is quantized)}$$

Note: $L$ is never zero (even for $l = 0$, $L = 0$), and we cannot simultaneously know $L_z$ and $L_x$ (or $L_y$) due to the uncertainty principle.

### 6.5 Orbital Shapes and Quantum Numbers

| $l$ | Letter | Number of Orbitals | Shape | Radial Nodes | Angular Nodes |
|-----|--------|-------------------|-------|-------------|---------------|
| 0 | s | 1 | Spherical | $n - 1$ | 0 |
| 1 | p | 3 | Dumbbell | $n - 2$ | 1 |
| 2 | d | 5 | Cloverleaf | $n - 3$ | 2 |
| 3 | f | 7 | Complex | $n - 4$ | 3 |

**Total nodes** in orbital $nl$: $n - 1$
**Radial nodes:** $n - l - 1$
**Angular nodes:** $l$

```
    ORBITAL SHAPES
    ===============

    s orbital:       p orbital:       d orbital (d_z²):
       ___              |
      /   \          ---|---            ___
     |  •  |            |            / |   | \
      \___/             |           |  | • |  |
                         |            \ |___| /
    (spherical)     (dumbbell)    (cloverleaf-like)
```

### 6.6 Degeneracy

**Hydrogen atom:** Energy depends only on $n$ → high degeneracy:

**Without spin:** $g_n = \sum_{l=0}^{n-1}(2l+1) = n^2$

**With spin:** $g_n = 2n^2$

| $n$ | $l$ values | $m_l$ values | States (no spin) | States (with spin) |
|-----|-----------|-------------|-----------------|-------------------|
| 1 | 0 | 0 | 1 | 2 |
| 2 | 0, 1 | 0; -1, 0, 1 | 4 | 8 |
| 3 | 0, 1, 2 | 0; -1,0,1; -2,-1,0,1,2 | 9 | 18 |
| 4 | 0,1,2,3 | 0; -1,0,1; -2,-1,0,1,2; -3,-2,-1,0,1,2,3 | 16 | 32 |

**Important:** This high degeneracy is special to the $1/r$ potential. Perturbations (external fields, relativistic corrections, spin-orbit coupling) **lift the degeneracy** — this is why spectral lines split in magnetic (Zeeman) and electric (Stark) fields.

### 6.7 Selection Rules

Electric dipole transitions between states must satisfy:

$$\boxed{\Delta l = \pm 1, \quad \Delta m_l = 0, \pm 1}$$

There is **no restriction on $\Delta n$**.

**Why $\Delta l = \pm 1$?** The electric dipole operator $\hat{d} = -e\hat{x}$ (or equivalently $\hat{y}$, $\hat{z}$) has odd parity. The matrix element $\langle n'l'm'|\hat{z}|nlm\rangle$ vanishes unless the parity of the initial and final states are different, which requires $\Delta l = \text{odd}$. The angular momentum integral gives $\Delta l = \pm 1$.

### 6.8 Hydrogen Spectrum

$$\boxed{\frac{1}{\lambda} = R_H \left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)}$$

where $R_H = 1.097 \times 10^7$ m⁻¹ is the Rydberg constant.

**Derivation:**

$$E_{n_2} - E_{n_1} = 13.6\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right) \text{ eV}$$

$$\frac{hc}{\lambda} = 13.6\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)$$

$$\frac{1}{\lambda} = \frac{13.6}{hc}\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right) = R_H\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)$$

**Spectral series:**

| Series | $n_1$ | $n_2$ | Region | Notable Lines |
|--------|-------|-------|--------|--------------|
| Lyman | 1 | 2, 3, 4, ... | Ultraviolet | Lα: 121.6 nm, Lβ: 102.6 nm |
| Balmer | 2 | 3, 4, 5, ... | Visible | Hα: 656.3 nm, Hβ: 486.1 nm |
| Paschen | 3 | 4, 5, 6, ... | Near infrared | Pα: 1875 nm |
| Brackett | 4 | 5, 6, 7, ... | Infrared | Brα: 4051 nm |
| Pfund | 5 | 6, 7, 8, ... | Far infrared | Pfα: 7460 nm |

**Convergence limit** (as $n_2 \to \infty$):

$$\frac{1}{\lambda_\infty} = \frac{R_H}{n_1^2}$$

For Lyman: $\lambda_\infty = 91.2$ nm (ionization wavelength from ground state)

---

## 7. Spin and Angular Momentum

### 7.1 Electron Spin

Electrons possess an intrinsic angular momentum called **spin**, which has no classical analogue:

**Spin quantum number:** $s = 1/2$ (always, for electrons)

$$S = \sqrt{s(s+1)}\hbar = \frac{\sqrt{3}}{2}\hbar$$

$$S_z = m_s\hbar = \pm\frac{\hbar}{2}$$

**Spin operators (Pauli matrices):**

$$\hat{S}_x = \frac{\hbar}{2}\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \hat{S}_y = \frac{\hbar}{2}\begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \hat{S}_z = \frac{\hbar}{2}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

**Spin states:**

$$|+\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \text{spin up}, \quad |-\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix} = \text{spin down}$$

**Commutation relations:**
- $[\hat{S}_x, \hat{S}_y] = i\hbar\hat{S}_z$ (and cyclic permutations)
- $\hat{S}^2|s, m_s\rangle = s(s+1)\hbar^2|s, m_s\rangle$
- $\hat{S}_z|s, m_s\rangle = m_s\hbar|s, m_s\rangle$

### 7.2 Stern-Gerlach Experiment

Silver atoms passing through an inhomogeneous magnetic field split into **two** discrete beams, not a continuous distribution.

**Key observations:**
- Angular momentum is quantized (only two values of $S_z$)
- Electrons have spin $s = 1/2$ (giving $2s + 1 = 2$ beams)
- The magnetic moment is $\vec{\mu} = -g_s\frac{e}{2m_e}\vec{S}$ where $g_s \approx 2$

### 7.3 Total Angular Momentum

$$\vec{J} = \vec{L} + \vec{S}$$

**Addition rules:**
- $j$ ranges from $|l - s|$ to $l + s$ in integer steps
- For single electron ($s = 1/2$): $j = l + 1/2$ or $j = l - 1/2$ (except $l = 0$ → $j = 1/2$ only)

**Fine structure:** Spin-orbit coupling splits each energy level (except $l = 0$) into two closely-spaced levels:

$$E_{\text{SO}} \propto \vec{L} \cdot \vec{S} = \frac{\hbar^2}{2}[j(j+1) - l(l+1) - s(s+1)]$$

---

## 8. Identical Particles and Exclusion Principle

### 8.1 Identical Particles

For $N$ identical particles, the wave function must be either:
- **Symmetric** (under exchange of any two particles): $\Psi(\ldots, i, \ldots, j, \ldots) = +\Psi(\ldots, j, \ldots, i, \ldots)$ → **Bosons** (integer spin)
- **Antisymmetric** (under exchange): $\Psi(\ldots, i, \ldots, j, \ldots) = -\Psi(\ldots, j, \ldots, i, \ldots)$ → **Fermions** (half-integer spin)

### 8.2 Pauli Exclusion Principle

No two identical fermions can occupy the **same quantum state** simultaneously.

**Mathematical statement:** The total wave function must be antisymmetric under exchange of any two fermions. If two fermions are in the same state, swapping them gives $-\Psi = \Psi$, which requires $\Psi = 0$.

**Consequences:**
- Explains the electron shell structure of atoms → periodic table
- Explains the stability of matter (electrons can't all fall into the ground state)
- Explains white dwarf stability (electron degeneracy pressure)
- Explains neutron star stability (neutron degeneracy pressure)

### 8.3 Fermions vs Bosons

| Property | Fermions | Bosons |
|----------|----------|--------|
| Spin | Half-integer (1/2, 3/2, ...) | Integer (0, 1, 2, ...) |
| Examples | Electrons, protons, neutrons, quarks | Photons, gluons, W/Z bosons, He-4 atoms |
| Statistics | Fermi-Dirac | Bose-Einstein |
| Multiple in same state? | **No** (exclusion principle) | **Yes** (unlimited) |
| Low-T behavior | Forms Fermi sea | Forms Bose-Einstein condensate |
| Wave function symmetry | Antisymmetric | Symmetric |

**Composite particles:** Protons (3 quarks) are fermions; neutrons (3 quarks) are fermions; He-4 atoms (2p + 2n + 2e = 6 fermions) are bosons (even number of fermions → integer total spin).

---

## 9. Quantum Tunneling

### 9.1 The Phenomenon

A particle can penetrate and pass through a potential barrier even when its energy is **less** than the barrier height. This has no classical analogue.

```
    QUANTUM TUNNELING THROUGH A RECTANGULAR BARRIER
    =================================================

    V(x)
    ^
    |
 V₀ |     _______________
    |    |               |
    |    |    BARRIER    |
 E ─|────|─ ─ ─ ─ ─ ─ ─ ─|────────  (Classical turning points)
    |    |               |
    |    |               |
  0 |____|_______________|____________ x
         0       L

    Region I    Region II   Region III
    (x < 0)    (0 < x < L)  (x > L)

    Classical: T = 0 if E < V₀ (particle bounces back)
    Quantum:   T > 0 even if E < V₀ (particle tunnels through!)
```

### 9.2 Rectangular Barrier

**Potential:**

$$V(x) = \begin{cases} 0 & x < 0 \\ V_0 & 0 \leq x \leq L \\ 0 & x > L \end{cases}$$

For $E < V_0$:

**Region II wave function:** $\psi_{II} = Ae^{-\kappa x} + Be^{\kappa x}$

where $\kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar}$

**Transmission coefficient (approximate for thick barriers, $\kappa L \gg 1$):**

$$\boxed{T \approx e^{-2\kappa L} = \exp\left(-\frac{2L\sqrt{2m(V_0-E)}}{\hbar}\right)}$$

**Reflection coefficient:** $R = 1 - T \approx 1$ (most of the wave is reflected)

**Exact transmission coefficient:**

$$T = \left[1 + \frac{V_0^2 \sinh^2(\kappa L)}{4E(V_0 - E)}\right]^{-1}$$

For thin barriers ($\kappa L \ll 1$): $\sinh(\kappa L) \approx \kappa L$, so $T$ can be appreciable.

### 9.3 Applications

**Radioactive α-decay:**
- α-particle (E ≈ 5 MeV) tunnels through the nuclear Coulomb barrier (~30 MeV)
- Explains the Geiger-Nuttall law: $\log\lambda = a + b/\sqrt{E_\alpha}$
- Barrier width depends on nuclear charge → explains why heavy nuclei decay

**Scanning Tunneling Microscope (STM):**
- Electron tunnels between a sharp metal tip and a conducting surface
- Current: $I \propto e^{-2\kappa d}$ where $d$ is the tip-surface distance
- Extreme sensitivity to distance: changing $d$ by 0.1 nm changes $I$ by an order of magnitude
- Resolution: atomic scale (~0.01 nm laterally, ~0.001 nm vertically)

**Semiconductor devices:**
- Tunnel diodes (Esaki diodes): negative differential resistance region
- Flash memory: Fowler-Nordheim tunneling for programming/erasing
- Josephson junctions: superconducting tunnel junctions

**Biological systems:**
- Enzyme catalysis: proton tunneling can enhance reaction rates
- DNA mutations: proton tunneling between base pairs can cause tautomeric shifts

### 9.4 Tunneling Probability Calculations

**Formula summary:**

For a rectangular barrier of height $V_0$ and width $L$, with particle energy $E < V_0$:

$$\kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar}$$

$$T \approx e^{-2\kappa L}$$

**For a triangular barrier** (WKB approximation):

$$T \approx \exp\left(-\frac{2}{\hbar}\int_{x_1}^{x_2} \sqrt{2m(V(x)-E)}\, dx\right)$$

**General observation:** $T$ is exponentially sensitive to:
1. Barrier width $L$ (doubling $L$ squares $T$)
2. $\sqrt{V_0 - E}$ (energy deficit)
3. Particle mass $m$ (heavy particles tunnel much less)

---

## 10. Quantum Measurement

### 10.1 Measurement and Collapse

Before measurement, a system exists in a **superposition** of eigenstates:

$$|\psi\rangle = \sum_n c_n |n\rangle$$

where $|n\rangle$ are eigenstates of the observable $\hat{A}$ with eigenvalues $a_n$: $\hat{A}|n\rangle = a_n|n\rangle$.

**Upon measurement of $\hat{A}$:**
1. The result is one of the eigenvalues $a_n$ (random)
2. The probability of getting $a_n$ is $|c_n|^2$
3. The state **collapses** to $|n\rangle$

**Example:** If $\hat{S}_z$ is measured on $|\psi\rangle = \frac{1}{\sqrt{2}}(|+\rangle + |-\rangle)$:
- 50% chance of getting $+\hbar/2$ (spin up)
- 50% chance of getting $-\hbar/2$ (spin down)
- After measurement, state is either $|+\rangle$ or $|-\rangle$

### 10.2 Expectation Values

For observable $\hat{A}$:

$$\boxed{\langle A \rangle = \int \psi^* \hat{A} \psi \, dx = \sum_n |c_n|^2 a_n}$$

**Variance:**

$$\langle(\Delta A)^2\rangle = \langle A^2\rangle - \langle A\rangle^2$$

$$\Delta A = \sqrt{\langle A^2\rangle - \langle A\rangle^2}$$

### 10.3 Ehrenfest's Theorem

Quantum expectation values obey classical equations of motion:

$$m\frac{d\langle x \rangle}{dt} = \langle p \rangle$$

$$\frac{d\langle p \rangle}{dt} = -\left\langle \frac{dV}{dx} \right\rangle$$

**Note:** For linear potentials (constant force), $\langle dV/dx \rangle = dV/dx|_{x=\langle x\rangle}$, recovering classical equations exactly. For non-linear potentials (e.g., Coulomb), there is a discrepancy, leading to quantum corrections.

**Correspondence principle:** Quantum mechanics agrees with classical mechanics in the limit of large quantum numbers ($n \to \infty$) or equivalently $\hbar \to 0$.

---

## 11. Advanced Topics

### 11.1 Dirac Notation

**Ket:** $|\psi\rangle$ (state vector in Hilbert space)
**Bra:** $\langle\psi|$ (dual vector, complex conjugate transpose)

**Inner product:** $\langle\phi|\psi\rangle$ = complex number (probability amplitude)

**Outer product:** $|\psi\rangle\langle\phi|$ = operator (projection if $\psi = \phi$)

**Completeness (resolution of identity):**

$$\sum_n |n\rangle\langle n| = \hat{I}$$

**Insert identity to calculate matrix elements:**

$$\langle\phi|\hat{A}|\psi\rangle = \sum_{m,n} \langle\phi|m\rangle\langle m|\hat{A}|n\rangle\langle n|\psi\rangle = \sum_{m,n} \phi_m^* A_{mn} \psi_n$$

### 11.2 Operators and Observables

| Operator | Symbol | Action |
|----------|--------|--------|
| Position | $\hat{x}$ | Multiplies by $x$ |
| Momentum | $\hat{p} = -i\hbar\frac{\partial}{\partial x}$ | Differentiates |
| Energy | $\hat{H} = -\frac{\hbar^2}{2m}\nabla^2 + V$ | TISE eigenvalue |
| Angular momentum | $\hat{L}_z = -i\hbar\frac{\partial}{\partial\phi}$ | Differentiates |

**Key commutators:**
- $[\hat{x}, \hat{p}] = i\hbar$
- $[\hat{L}_x, \hat{L}_y] = i\hbar\hat{L}_z$ (and cyclic)
- $[\hat{H}, \hat{t}] \neq 0$ (energy and time are not both operators)

**General uncertainty relation:**

$$\boxed{\Delta A \cdot \Delta B \geq \frac{1}{2}|[\hat{A}, \hat{B}]|}$$

### 11.3 Perturbation Theory

**Time-independent (non-degenerate):**

When $\hat{H} = \hat{H}_0 + \lambda\hat{H}'$ where $\hat{H}'$ is a small perturbation:

**Zeroth order:** $\hat{H}_0|n^{(0)}\rangle = E_n^{(0)}|n^{(0)}\rangle$

**First-order energy correction:**

$$E_n^{(1)} = \langle n^{(0)} | \hat{H}' | n^{(0)} \rangle$$

**First-order state correction:**

$$|n^{(1)}\rangle = \sum_{m \neq n} \frac{\langle m^{(0)} | \hat{H}' | n^{(0)} \rangle}{E_n^{(0)} - E_m^{(0)}} |m^{(0)}\rangle$$

**Second-order energy correction:**

$$E_n^{(2)} = \sum_{m \neq n} \frac{|\langle m^{(0)} | \hat{H}' | n^{(0)} \rangle|^2}{E_n^{(0)} - E_m^{(0)}}$$

**Applications:**
- **Stark effect:** $\hat{H}' = eEz$ (electric field splits levels)
- **Zeeman effect:** $\hat{H}' = \frac{e}{2m}B(\hat{L}_z + 2\hat{S}_z)$ (magnetic field splits levels)
- **Fine structure:** relativistic kinetic energy + spin-orbit coupling + Darwin term

### 11.4 Variational Principle

The ground state energy satisfies:

$$\boxed{E_0 \leq \frac{\langle \psi_{\text{trial}} | \hat{H} | \psi_{\text{trial}} \rangle}{\langle \psi_{\text{trial}} | \psi_{\text{trial}} \rangle}}$$

for **any** trial wave function $|\psi_{\text{trial}}\rangle$.

**Algorithm:**
1. Choose a trial wave function with adjustable parameters
2. Calculate $\langle \hat{H} \rangle$ as a function of those parameters
3. Minimize with respect to the parameters
4. The minimum gives the best approximation to $E_0$

### 11.5 WKB Approximation

For slowly-varying potentials, the wave function is approximately:

$$\psi(x) \approx \frac{C}{\sqrt{p(x)}} \exp\left(\pm\frac{i}{\hbar}\int p(x)\, dx\right)$$

where $p(x) = \sqrt{2m(E - V(x))}$.

**Connection formulas** at classical turning points give the quantization condition:

$$\int_{x_1}^{x_2} p(x)\, dx = \left(n + \frac{1}{2}\right)\pi\hbar$$

This works well for large $n$ and gives the correct qualitative behavior of energy levels.

---

## 12. Worked Examples

### Example 1: Photoelectric Effect — Finding Work Function and Stopping Potential

**Problem:** Ultraviolet light of wavelength 200 nm shines on a metal surface. The stopping potential is found to be 2.22 V. Find (a) the work function of the metal, (b) the threshold frequency, and (c) the maximum kinetic energy of the emitted electrons.

**Solution:**

**Given:** $\lambda = 200$ nm $= 200 \times 10^{-9}$ m, $V_s = 2.22$ V

**(a) Work function:**

The photoelectric equation: $h\nu = \phi + K_{\max}$

$$K_{\max} = eV_s = 1 \text{ eV} \times 2.22 = 2.22 \text{ eV}$$

Photon energy:

$$E_{\text{photon}} = \frac{hc}{\lambda} = \frac{6.626 \times 10^{-34} \times 3 \times 10^8}{200 \times 10^{-9}} = \frac{1.988 \times 10^{-25}}{2 \times 10^{-7}} = 9.94 \times 10^{-19} \text{ J}$$

Convert to eV: $E_{\text{photon}} = \frac{9.94 \times 10^{-19}}{1.602 \times 10^{-19}} = 6.20$ eV

$$\phi = E_{\text{photon}} - K_{\max} = 6.20 - 2.22 = \boxed{3.98 \text{ eV}}$$

**(b) Threshold frequency:**

$$\nu_0 = \frac{\phi}{h} = \frac{3.98 \times 1.602 \times 10^{-19}}{6.626 \times 10^{-34}} = \frac{6.376 \times 10^{-19}}{6.626 \times 10^{-34}} = 9.62 \times 10^{14} \text{ Hz}$$

**(c) Maximum kinetic energy:**

$$K_{\max} = eV_s = \boxed{2.22 \text{ eV}}$$

(Already used above.)

**Quick method using hc = 1240 eV·nm:**

$$E_{\text{photon}} = \frac{1240}{200} = 6.20 \text{ eV}$$

$$\phi = 6.20 - 2.22 = 3.98 \text{ eV}$$

---

### Example 2: de Broglie Wavelength of Electron Accelerated Through Voltage

**Problem:** An electron is accelerated from rest through a potential difference of 100 V. Find its de Broglie wavelength.

**Solution:**

**Given:** $V = 100$ V, $m_e = 9.109 \times 10^{-31}$ kg, $e = 1.602 \times 10^{-19}$ C

**Step 1: Find the kinetic energy**

$$K = eV = 1.602 \times 10^{-19} \times 100 = 1.602 \times 10^{-17} \text{ J}$$

**Step 2: Find the momentum**

$$p = \sqrt{2m_e K} = \sqrt{2 \times 9.109 \times 10^{-31} \times 1.602 \times 10^{-17}}$$

$$p = \sqrt{2.919 \times 10^{-47}} = 5.403 \times 10^{-24} \text{ kg·m/s}$$

**Step 3: Find the de Broglie wavelength**

$$\lambda = \frac{h}{p} = \frac{6.626 \times 10^{-34}}{5.403 \times 10^{-24}} = 1.226 \times 10^{-10} \text{ m} = \boxed{0.123 \text{ nm}}$$

**Shortcut formula:**

$$\lambda = \frac{h}{\sqrt{2m_e eV}} = \frac{6.626 \times 10^{-34}}{\sqrt{2 \times 9.109 \times 10^{-31} \times 1.602 \times 10^{-19} \times V}}$$

$$\boxed{\lambda(\text{nm}) = \frac{1.226}{\sqrt{V(\text{volts})}}}$$

For $V = 100$ V: $\lambda = 1.226/\sqrt{100} = 1.226/10 = 0.123$ nm ✓

---

### Example 3: Particle in a Box — Energy Levels and Transition Wavelengths

**Problem:** An electron is confined in a one-dimensional box of width $L = 0.20$ nm (approximately the size of an atom). Find (a) the ground state energy, (b) the first three energy levels, (c) the wavelength of light emitted in the $n = 2 \to n = 1$ transition.

**Solution:**

**Given:** $L = 0.20$ nm $= 2.0 \times 10^{-10}$ m, $m_e = 9.109 \times 10^{-31}$ kg

**Formula:** $E_n = \frac{n^2 h^2}{8mL^2}$

**Step 1: Calculate the energy constant**

$$E_1 = \frac{h^2}{8mL^2} = \frac{(6.626 \times 10^{-34})^2}{8 \times 9.109 \times 10^{-31} \times (2.0 \times 10^{-10})^2}$$

Numerator: $(6.626 \times 10^{-34})^2 = 4.390 \times 10^{-67}$

Denominator: $8 \times 9.109 \times 10^{-31} \times 4.0 \times 10^{-20} = 2.915 \times 10^{-49}$

$$E_1 = \frac{4.390 \times 10^{-67}}{2.915 \times 10^{-49}} = 1.506 \times 10^{-18} \text{ J}$$

Convert to eV: $E_1 = \frac{1.506 \times 10^{-18}}{1.602 \times 10^{-19}} = \boxed{9.40 \text{ eV}}$

**(a) Ground state energy:** $E_1 = 9.40$ eV

**(b) First three levels:**
- $E_1 = 1^2 \times 9.40 = 9.40$ eV
- $E_2 = 2^2 \times 9.40 = 4 \times 9.40 = 37.6$ eV
- $E_3 = 3^2 \times 9.40 = 9 \times 9.40 = 84.6$ eV

**(c) Transition $n = 2 \to n = 1$:**

$$\Delta E = E_2 - E_1 = 37.6 - 9.40 = 28.2 \text{ eV}$$

$$\lambda = \frac{hc}{\Delta E} = \frac{1240 \text{ eV·nm}}{28.2 \text{ eV}} = \boxed{44.0 \text{ nm}}$$

This is in the ultraviolet region.

---

### Example 4: Harmonic Oscillator — Energy Calculations

**Problem:** A quantum harmonic oscillator has a natural frequency of $\nu = 3.0 \times 10^{14}$ Hz. Find (a) the zero-point energy in eV, (b) the energy of the $n = 3$ state, (c) the frequency of light emitted in the $n = 3 \to n = 2$ transition, and (d) the energy spacing between adjacent levels.

**Solution:**

**Given:** $\nu = 3.0 \times 10^{14}$ Hz, $\omega = 2\pi\nu = 2\pi \times 3.0 \times 10^{14} = 1.885 \times 10^{15}$ rad/s

**(a) Zero-point energy:**

$$E_0 = \frac{1}{2}\hbar\omega = \frac{1}{2} \times 1.055 \times 10^{-34} \times 1.885 \times 10^{15}$$

$$E_0 = \frac{1}{2} \times 1.989 \times 10^{-19} = 9.94 \times 10^{-20} \text{ J}$$

Convert to eV: $E_0 = \frac{9.94 \times 10^{-20}}{1.602 \times 10^{-19}} = \boxed{0.62 \text{ eV}}$

**(b) Energy of $n = 3$:**

$$E_3 = \left(3 + \frac{1}{2}\right)\hbar\omega = \frac{7}{2}\hbar\omega = 7 \times E_0 = 7 \times 0.62 = \boxed{4.34 \text{ eV}}$$

**(c) Frequency of $n = 3 \to n = 2$ transition:**

$$\Delta E = E_3 - E_2 = \left(\frac{7}{2} - \frac{5}{2}\right)\hbar\omega = \hbar\omega = h\nu$$

$$\nu_{\text{emitted}} = \nu = \boxed{3.0 \times 10^{14} \text{ Hz}}$$

This is the remarkable feature of the harmonic oscillator: **all transitions have the same frequency!**

**(d) Energy spacing:**

$$\Delta E = \hbar\omega = h\nu = 6.626 \times 10^{-34} \times 3.0 \times 10^{14} = 1.99 \times 10^{-19} \text{ J} = \boxed{1.24 \text{ eV}}$$

---

### Example 5: Hydrogen Atom — Energy Levels and Spectral Lines

**Problem:** A hydrogen atom is in the $n = 4$ state. Find (a) all possible energies, (b) the number of spectral lines that can be emitted, (c) the wavelength of the $n = 4 \to n = 2$ transition (Balmer series), and (d) the ionization energy from the $n = 2$ state.

**Solution:**

**(a) Energy of the $n = 4$ state:**

$$E_4 = -\frac{13.6}{4^2} = -\frac{13.6}{16} = -0.85 \text{ eV}$$

**(b) Number of spectral lines:**

From $n = 4$, the atom can transition to:
- $n = 3$, then $n = 2$, then $n = 1$
- $n = 2$, then $n = 1$
- $n = 1$

Total distinct transitions: $\binom{4}{2} = \frac{4 \times 3}{2} = \boxed{6}$ lines

The lines are: 4→3, 4→2, 4→1, 3→2, 3→1, 2→1

**(c) $n = 4 \to n = 2$ transition:**

$$E_4 - E_2 = -0.85 - (-3.40) = 2.55 \text{ eV}$$

$$\lambda = \frac{hc}{\Delta E} = \frac{1240}{2.55} = \boxed{486 \text{ nm}}$$

This is the Hβ (Balmer-beta) line — blue-green in color.

**(d) Ionization energy from $n = 2$:**

$$E_{\text{ionization}} = 0 - E_2 = 0 - (-3.40) = \boxed{3.40 \text{ eV}}$$

**Complete energy level calculation for hydrogen:**

| $n$ | $E_n$ (eV) | $\Delta E$ from $n=4$ (eV) | $\lambda$ (nm) | Series |
|-----|-----------|---------------------------|----------------|--------|
| 4 | -0.85 | 0 | — | — |
| 3 | -1.51 | 0.66 | 1879 | Paschen |
| 2 | -3.40 | 2.55 | 486 | Balmer |
| 1 | -13.60 | 12.75 | 97.3 | Lyman |

---

### Example 6: Uncertainty Principle Applications

**Problem:** An electron is confined within an atom (approximate size $\Delta x \approx 10^{-10}$ m). Find (a) the minimum uncertainty in its momentum, (b) the minimum uncertainty in its speed, and (c) estimate the kinetic energy. Compare with the hydrogen atom ground state energy.

**Solution:**

**(a) Minimum momentum uncertainty:**

$$\Delta x \cdot \Delta p \geq \frac{\hbar}{2}$$

$$\Delta p \geq \frac{\hbar}{2\Delta x} = \frac{1.055 \times 10^{-34}}{2 \times 10^{-10}} = \boxed{5.28 \times 10^{-25} \text{ kg·m/s}}$$

**(b) Minimum speed uncertainty:**

$$\Delta v \geq \frac{\Delta p}{m_e} = \frac{5.28 \times 10^{-25}}{9.109 \times 10^{-31}} = \boxed{5.80 \times 10^5 \text{ m/s}}$$

This is about 0.2% of the speed of light — significant but non-relativistic.

**(c) Kinetic energy estimate:**

$$K \sim \frac{(\Delta p)^2}{2m_e} = \frac{(5.28 \times 10^{-25})^2}{2 \times 9.109 \times 10^{-31}}$$

$$K = \frac{2.788 \times 10^{-49}}{1.822 \times 10^{-30}} = 1.53 \times 10^{-19} \text{ J} = \boxed{0.96 \text{ eV}}$$

The hydrogen ground state energy is $E_1 = -13.6$ eV, and the kinetic energy is $|K| = 13.6$ eV (by the virial theorem). Our rough estimate of ~1 eV is within an order of magnitude, which is reasonable for such a crude estimate.

---

### Example 7: Quantum Tunneling Probability

**Problem:** An alpha particle ($m = 6.64 \times 10^{-27}$ kg, $E = 5.0$ MeV) encounters a nuclear potential barrier of height $V_0 = 30$ MeV and width $L = 2.0 \times 10^{-15}$ m. Estimate (a) the tunneling probability and (b) the mean lifetime if the particle attempts to escape $10^{21}$ times per second.

**Solution:**

**(a) Tunneling probability:**

**Step 1: Calculate $\kappa$**

$$\kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar}$$

$$V_0 - E = 30 - 5 = 25 \text{ MeV} = 25 \times 1.602 \times 10^{-13} \text{ J} = 4.005 \times 10^{-12} \text{ J}$$

$$2m(V_0 - E) = 2 \times 6.64 \times 10^{-27} \times 4.005 \times 10^{-12} = 5.319 \times 10^{-38}$$

$$\sqrt{2m(V_0 - E)} = 2.306 \times 10^{-19} \text{ kg·m/s}$$

$$\kappa = \frac{2.306 \times 10^{-19}}{1.055 \times 10^{-34}} = 2.186 \times 10^{15} \text{ m}^{-1}$$

**Step 2: Calculate $2\kappa L$**

$$2\kappa L = 2 \times 2.186 \times 10^{15} \times 2.0 \times 10^{-15} = \boxed{8.74}$$

**Step 3: Calculate $T$**

$$T = e^{-2\kappa L} = e^{-8.74} = \boxed{1.6 \times 10^{-4}}$$

The alpha particle has about a 0.016% chance of tunneling through on each attempt.

**(b) Mean lifetime:**

$$\tau = \frac{1}{\nu \cdot T} = \frac{1}{10^{21} \times 1.6 \times 10^{-4}} = \boxed{6.3 \times 10^{18} \text{ s}}$$

Wait — that's about $2 \times 10^{11}$ years! For actual alpha decay, the attempt frequency and barrier parameters are different (the Coulomb barrier is not rectangular), but the exponential sensitivity of tunneling explains the enormous range of observed half-lives (from microseconds to billions of years).

---

### Example 8: Expectation Values in Particle in a Box

**Problem:** For an electron in a 1D box of width $L = 0.10$ nm in the $n = 1$ state, find (a) $\langle x \rangle$, (b) $\langle x^2 \rangle$, (c) $\Delta x$, (d) $\langle p \rangle$, (e) $\langle p^2 \rangle$, (f) $\Delta p$, and verify the uncertainty principle.

**Solution:**

**Given:** $L = 0.10$ nm $= 1.0 \times 10^{-10}$ m, $n = 1$, $\psi_1(x) = \sqrt{2/L}\sin(\pi x/L)$

**(a) $\langle x \rangle$:**

$$\langle x \rangle = \frac{2}{L}\int_0^L x\sin^2\left(\frac{\pi x}{L}\right) dx = \frac{L}{2} = \boxed{0.050 \text{ nm}}$$

(Midpoint, by symmetry.)

**(b) $\langle x^2 \rangle$:**

$$\langle x^2 \rangle = \frac{2}{L}\int_0^L x^2\sin^2\left(\frac{\pi x}{L}\right) dx = L^2\left(\frac{1}{3} - \frac{1}{2\pi^2}\right)$$

$$= (0.10)^2\left(0.3333 - 0.0507\right) = 0.01 \times 0.2826 = \boxed{2.83 \times 10^{-3} \text{ nm}^2}$$

**(c) $\Delta x$:**

$$\Delta x = \sqrt{\langle x^2\rangle - \langle x\rangle^2} = \sqrt{2.83 \times 10^{-3} - (0.05)^2} = \sqrt{2.83 \times 10^{-3} - 2.5 \times 10^{-3}}$$

$$= \sqrt{3.3 \times 10^{-4}} = \boxed{0.018 \text{ nm}}$$

**(d) $\langle p \rangle$:**

By symmetry (the particle is equally likely to go left or right):

$$\langle p \rangle = \boxed{0}$$

**(e) $\langle p^2 \rangle$:**

$$\langle p^2 \rangle = 2mE_1 = \frac{\pi^2\hbar^2}{L^2}$$

$$= \frac{\pi^2 \times (1.055 \times 10^{-34})^2}{(1.0 \times 10^{-10})^2} = \frac{9.87 \times 1.113 \times 10^{-68}}{1.0 \times 10^{-20}} = 1.099 \times 10^{-47} \text{ kg}^2\text{·m}^2\text{/s}^2$$

**(f) $\Delta p$:**

$$\Delta p = \sqrt{\langle p^2\rangle - \langle p\rangle^2} = \sqrt{1.099 \times 10^{-47}} = 3.32 \times 10^{-24} \text{ kg·m/s}$$

**Verification of uncertainty principle:**

$$\Delta x \cdot \Delta p = 1.8 \times 10^{-11} \times 3.32 \times 10^{-24} = 5.97 \times 10^{-35} \text{ J·s}$$

$$\frac{\hbar}{2} = \frac{1.055 \times 10^{-34}}{2} = 5.28 \times 10^{-35} \text{ J·s}$$

$$\Delta x \cdot \Delta p = 5.97 \times 10^{-35} > 5.28 \times 10^{-35} = \frac{\hbar}{2} \quad \checkmark$$

---

### Example 9: Quantum Number Problems — Degeneracy and Selection Rules

**Problem:** (a) How many distinct quantum states does the $n = 3$ shell of hydrogen have (including spin)? (b) Which of the following transitions are allowed: 2s → 1s, 2p → 1s, 3d → 2p, 3s → 2p, 3p → 2s? (c) How many spectral lines would be observed from hydrogen in the $n = 3$ excited state?

**Solution:**

**(a) Number of states in $n = 3$ shell:**

For $n = 3$:
- $l = 0$: $m_l = 0$ (1 orbital) × 2 spins = 2 states
- $l = 1$: $m_l = -1, 0, 1$ (3 orbitals) × 2 spins = 6 states
- $l = 2$: $m_l = -2, -1, 0, 1, 2$ (5 orbitals) × 2 spins = 10 states

Total: $2 + 6 + 10 = \boxed{18}$ states

Or simply: $2n^2 = 2 \times 9 = 18$ ✓

**(b) Selection rules:** $\Delta l = \pm 1$

| Transition | $l_i$ | $l_f$ | $\Delta l$ | Allowed? |
|-----------|-------|-------|-----------|----------|
| 2s → 1s | 0 | 0 | 0 | **No** (Δl = 0) |
| 2p → 1s | 1 | 0 | -1 | **Yes** |
| 3d → 2p | 2 | 1 | -1 | **Yes** |
| 3s → 2p | 0 | 1 | +1 | **Yes** |
| 3p → 2s | 1 | 0 | -1 | **Yes** |

**(c) Spectral lines from $n = 3$:**

Possible transitions: 3→2, 3→1, 2→1 = $\boxed{3}$ spectral lines

---

### Example 10: Compton Scattering Wavelength Shift

**Problem:** An X-ray photon with wavelength 0.100 nm scatters off a free electron at an angle of 90°. Find (a) the wavelength of the scattered photon, (b) the kinetic energy of the recoil electron, and (c) the scattering angle at which the wavelength shift is maximum.

**Solution:**

**Given:** $\lambda = 0.100$ nm $= 1.00 \times 10^{-10}$ m, $\theta = 90°$

**(a) Scattered wavelength:**

$$\Delta\lambda = \frac{h}{m_e c}(1 - \cos\theta) = \lambda_C(1 - \cos 90°)$$

$$\Delta\lambda = 2.426 \times 10^{-12} \times (1 - 0) = 2.426 \times 10^{-12} \text{ m} = 0.00243 \text{ nm}$$

$$\lambda' = \lambda + \Delta\lambda = 0.100 + 0.00243 = \boxed{0.1024 \text{ nm}}$$

**(b) Kinetic energy of recoil electron:**

$$K_e = hc\left(\frac{1}{\lambda} - \frac{1}{\lambda'}\right) = hc \cdot \frac{\lambda' - \lambda}{\lambda\lambda'}$$

$$K_e = \frac{1240 \text{ eV·nm} \times 0.00243 \text{ nm}}{0.100 \times 0.1024 \text{ nm}^2}$$

$$K_e = \frac{3.013}{0.01024} = \boxed{294 \text{ eV}}$$

Alternatively:

$$K_e = E_{\text{photon}} - E_{\text{scattered}} = \frac{hc}{\lambda} - \frac{hc}{\lambda'}$$

$$= \frac{1240}{0.100} - \frac{1240}{0.1024} = 12400 - 12109 = 291 \text{ eV} \approx 294 \text{ eV}$$

(Small difference due to rounding.)

**(c) Maximum shift:**

$$\Delta\lambda_{\max} = 2\lambda_C = 2 \times 2.426 \times 10^{-12} = 0.00485 \text{ nm}$$

This occurs at $\theta = 180°$ (backscattering).

---

### Example 11: Tunneling Through a Triangular Barrier (STM Application)

**Problem:** In a scanning tunneling microscope, the tip-to-surface distance is 0.50 nm. If the work function (effective barrier height) is 4.5 eV and the tunneling voltage is small, estimate the tunneling current. If the distance changes to 0.55 nm, what happens to the current?

**Solution:**

The tunneling current in an STM is proportional to $e^{-2\kappa d}$ where $d$ is the tip-surface distance.

$$\kappa = \frac{\sqrt{2m_e\phi}}{\hbar}$$

where $\phi = 4.5$ eV is the effective barrier height.

**Step 1: Calculate $\kappa$**

$$\kappa = \frac{\sqrt{2 \times 9.109 \times 10^{-31} \times 4.5 \times 1.602 \times 10^{-19}}}{1.055 \times 10^{-34}}$$

$$= \frac{\sqrt{1.313 \times 10^{-48}}}{1.055 \times 10^{-34}} = \frac{1.146 \times 10^{-24}}{1.055 \times 10^{-34}} = 1.086 \times 10^{10} \text{ m}^{-1} = 10.86 \text{ nm}^{-1}$$

**Step 2: Tunneling factor at $d_1 = 0.50$ nm**

$$2\kappa d_1 = 2 \times 10.86 \times 0.50 = 10.86$$

$$e^{-2\kappa d_1} = e^{-10.86} = 1.93 \times 10^{-5}$$

**Step 3: Tunneling factor at $d_2 = 0.55$ nm**

$$2\kappa d_2 = 2 \times 10.86 \times 0.55 = 11.95$$

$$e^{-2\kappa d_2} = e^{-11.95} = 6.57 \times 10^{-6}$$

**Step 4: Current ratio**

$$\frac{I_2}{I_1} = \frac{e^{-2\kappa d_2}}{e^{-2\kappa d_1}} = e^{-2\kappa(d_2 - d_1)} = e^{-2 \times 10.86 \times 0.05} = e^{-1.086} = \boxed{0.337}$$

Increasing the distance by just 0.05 nm (0.5 Å) reduces the current to about **one-third** of its original value. This extreme sensitivity is what makes STM capable of atomic-resolution imaging.

---

### Example 12: Hydrogen Atom — Degeneracy and Orbital Angular Momentum

**Problem:** For a hydrogen atom in the $n = 3$ state, find (a) the allowed values of $l$, (b) the allowed values of $m_l$ for each $l$, (c) the magnitude of the orbital angular momentum for $l = 2$, (d) the maximum $z$-component of angular momentum, and (e) the angle between $\vec{L}$ and the $z$-axis for the state with maximum $m_l$.

**Solution:**

**(a) Allowed $l$ for $n = 3$:**

$$l = 0, 1, 2$$

**(b) Allowed $m_l$ for each $l$:**

| $l$ | $m_l$ values | Number of states |
|-----|-------------|-----------------|
| 0 | 0 | 1 |
| 1 | -1, 0, 1 | 3 |
| 2 | -2, -1, 0, 1, 2 | 5 |

Total: 9 states (without spin), 18 with spin.

**(c) Magnitude for $l = 2$:**

$$L = \sqrt{l(l+1)}\hbar = \sqrt{2 \times 3}\hbar = \sqrt{6}\hbar = \boxed{2.449\hbar}$$

**(d) Maximum $L_z$:**

$$L_{z,\max} = m_{l,\max}\hbar = 2\hbar$$

Note that $L_{z,\max} = 2\hbar < L = \sqrt{6}\hbar = 2.449\hbar$. This is consistent — the $z$-component can never equal the total magnitude because the vector precesses around the $z$-axis.

**(e) Angle for $m_l = 2$:**

$$\cos\theta = \frac{L_z}{L} = \frac{2\hbar}{\sqrt{6}\hbar} = \frac{2}{\sqrt{6}} = 0.8165$$

$$\theta = \cos^{-1}(0.8165) = \boxed{35.3°}$$

The angular momentum vector makes an angle of 35.3° with the $z$-axis, precessing around it while maintaining a constant angle.

---

### Example 13: Compton Effect with Full Kinematics

**Problem:** A 0.100 nm X-ray photon scatters off a free electron at an angle of 60°. Find (a) the scattered photon wavelength, (b) the scattered photon energy, (c) the kinetic energy of the recoil electron, and (d) the scattering angle of the electron.

**Solution:**

**Given:** $\lambda = 0.100$ nm, $\theta = 60°$

**(a) Scattered wavelength:**

$$\Delta\lambda = \lambda_C(1 - \cos\theta) = 2.426 \times 10^{-3} \text{ nm} \times (1 - \cos 60°)$$

$$= 2.426 \times 10^{-3} \times (1 - 0.5) = 2.426 \times 10^{-3} \times 0.5 = 1.213 \times 10^{-3} \text{ nm}$$

$$\lambda' = 0.100 + 0.001213 = \boxed{0.10121 \text{ nm}}$$

**(b) Scattered photon energy:**

$$E' = \frac{hc}{\lambda'} = \frac{1240}{0.10121} = \boxed{12252 \text{ eV} = 12.25 \text{ keV}}$$

**(c) Kinetic energy of recoil electron:**

$$K_e = E - E' = \frac{1240}{0.100} - \frac{1240}{0.10121} = 12400 - 12252 = \boxed{148 \text{ eV}}$$

**(d) Electron scattering angle:**

From momentum conservation:

$$\tan\phi = \frac{\sin\theta}{(E/E') - \cos\theta} = \frac{\sin 60°}{(0.10121/0.100) - \cos 60°}$$

Wait — let me use the correct formula. From momentum conservation:

$$\cot\phi = \left(1 + \frac{h\nu}{m_e c^2}\right)\tan\frac{\theta}{2}$$

$$\frac{h\nu}{m_e c^2} = \frac{12400}{511000} = 0.02427$$

$$\cot\phi = (1 + 0.02427)\tan 30° = 1.02427 \times 0.5774 = 0.5915$$

$$\phi = \cot^{-1}(0.5915) = \boxed{59.3°}$$

---

### Example 14: Harmonic Oscillator — Ladder Operator Application

**Problem:** A quantum harmonic oscillator is in the state $|\psi\rangle = \frac{1}{2}|0\rangle + \frac{1}{2}|1\rangle + \frac{1}{\sqrt{2}}|2\rangle$. Find (a) verify normalization, (b) $\langle E \rangle$, (c) $\langle n \rangle$, and (d) the probability of measuring $E_1$.

**Solution:**

**(a) Verify normalization:**

$$\langle\psi|\psi\rangle = \left(\frac{1}{2}\right)^2 + \left(\frac{1}{2}\right)^2 + \left(\frac{1}{\sqrt{2}}\right)^2 = \frac{1}{4} + \frac{1}{4} + \frac{1}{2} = 1 \quad \checkmark$$

**(b) Expectation value of energy:**

$$\langle E \rangle = \sum_n |c_n|^2 E_n = \frac{1}{4}E_0 + \frac{1}{4}E_1 + \frac{1}{2}E_2$$

$$= \frac{1}{4}\left(\frac{1}{2}\hbar\omega\right) + \frac{1}{4}\left(\frac{3}{2}\hbar\omega\right) + \frac{1}{2}\left(\frac{5}{2}\hbar\omega\right)$$

$$= \frac{\hbar\omega}{8} + \frac{3\hbar\omega}{8} + \frac{5\hbar\omega}{4} = \frac{\hbar\omega + 3\hbar\omega + 10\hbar\omega}{8} = \boxed{\frac{14\hbar\omega}{8} = \frac{7}{4}\hbar\omega}$$

**(c) Expectation value of $n$:**

$$\langle n \rangle = \sum_n |c_n|^2 n = \frac{1}{4}(0) + \frac{1}{4}(1) + \frac{1}{2}(2) = 0 + \frac{1}{4} + 1 = \boxed{1.25}$$

Check: $\langle E \rangle = (\langle n \rangle + 1/2)\hbar\omega = (1.25 + 0.5)\hbar\omega = 1.75\hbar\omega = \frac{7}{4}\hbar\omega$ ✓

**(d) Probability of measuring $E_1$:**

$$P(E_1) = |c_1|^2 = \left(\frac{1}{2}\right)^2 = \boxed{\frac{1}{4} = 25\%}$$

---

### Example 15: Particle in a Box — Probability Calculations

**Problem:** For a particle in a 1D box of width $L$ in the $n = 2$ state, find (a) the probability of finding the particle in the left half of the box ($0 \leq x \leq L/2$), (b) the probability of finding it in the middle third ($L/3 \leq x \leq 2L/3$), and (c) the most probable position.

**Solution:**

**Wave function:** $\psi_2(x) = \sqrt{2/L}\sin(2\pi x/L)$

**Probability density:** $|\psi_2(x)|^2 = \frac{2}{L}\sin^2\left(\frac{2\pi x}{L}\right)$

**(a) Probability in left half:**

$$P = \frac{2}{L}\int_0^{L/2} \sin^2\left(\frac{2\pi x}{L}\right) dx$$

Using $\sin^2(\theta) = \frac{1 - \cos(2\theta)}{2}$:

$$P = \frac{2}{L}\int_0^{L/2} \frac{1 - \cos(4\pi x/L)}{2} dx = \frac{1}{L}\left[x - \frac{L}{4\pi}\sin\left(\frac{4\pi x}{L}\right)\right]_0^{L/2}$$

$$= \frac{1}{L}\left[\frac{L}{2} - \frac{L}{4\pi}\sin(2\pi) - 0 + 0\right] = \frac{1}{L}\left[\frac{L}{2} - 0\right] = \boxed{\frac{1}{2}}$$

This makes sense — the $n = 2$ wave function has equal probability in the left and right halves (the node at $L/2$ divides the box symmetrically).

**(b) Probability in middle third:**

$$P = \frac{2}{L}\int_{L/3}^{2L/3} \sin^2\left(\frac{2\pi x}{L}\right) dx$$

$$= \frac{1}{L}\left[x - \frac{L}{4\pi}\sin\left(\frac{4\pi x}{L}\right)\right]_{L/3}^{2L/3}$$

$$= \frac{1}{L}\left[\frac{2L}{3} - \frac{L}{4\pi}\sin\left(\frac{8\pi}{3}\right) - \frac{L}{3} + \frac{L}{4\pi}\sin\left(\frac{4\pi}{3}\right)\right]$$

$$\sin\left(\frac{8\pi}{3}\right) = \sin\left(\frac{2\pi}{3}\right) = \frac{\sqrt{3}}{2}, \quad \sin\left(\frac{4\pi}{3}\right) = -\frac{\sqrt{3}}{2}$$

$$P = \frac{1}{3} - \frac{1}{4\pi}\cdot\frac{\sqrt{3}}{2} - \frac{1}{4\pi}\cdot\frac{\sqrt{3}}{2} = \frac{1}{3} - \frac{\sqrt{3}}{4\pi}$$

$$= 0.3333 - 0.1378 = \boxed{0.196}$$

**(c) Most probable position:**

The most probable position maximizes $|\psi_2|^2 = \frac{2}{L}\sin^2(2\pi x/L)$.

$\sin^2(2\pi x/L)$ is maximized when $\sin(2\pi x/L) = \pm 1$:

$$\frac{2\pi x}{L} = \frac{\pi}{2}, \frac{3\pi}{2}$$

$$x = \frac{L}{4} \text{ and } x = \frac{3L}{4}$$

The most probable positions are at $\boxed{x = L/4}$ and $\boxed{x = 3L/4}$ (the two peaks of the probability density).

---

## 13. Common Mistakes and Traps

### 13.1 Formula Confusion

| Mistake | Correct Version | Why It Matters |
|---------|----------------|----------------|
| Using $\lambda = h/mv$ when relativistic | Must use $p = \gamma mv$ for $v > 0.1c$ | de Broglie wavelength becomes much smaller |
| Forgetting $\hbar = h/(2\pi)$ | Always check: is the formula using $h$ or $\hbar$? | Factor of $2\pi$ error |
| Using $E_n = n^2$ for harmonic oscillator | HO: $E_n = (n+1/2)\hbar\omega$; Box: $E_n \propto n^2$ | Completely different energy spectra |
| Writing $\Delta x \cdot \Delta p \geq \hbar$ | It's $\hbar/2$, not $\hbar$ | Factor of 2 error |
| Confusing $\omega$ and $\nu$ | $\omega = 2\pi\nu$; use $\hbar\omega$ or $h\nu$ | Factor of $2\pi$ error |

### 13.2 Conceptual Errors

**1. Zero-point energy:**
- WRONG: "The ground state has zero energy"
- RIGHT: $E_0 > 0$ for box ($E_1 = h^2/8mL^2$) and harmonic oscillator ($E_0 = \hbar\omega/2$)
- Only the hydrogen atom has $E_1 = -13.6$ eV (but the kinetic energy is positive!)

**2. Normalization:**
- WRONG: Writing $\psi_n(x) = \sin(n\pi x/L)$ without the normalization factor
- RIGHT: $\psi_n(x) = \sqrt{2/L}\sin(n\pi x/L)$
- If you forget normalization, probabilities will be wrong

**3. Boundary conditions:**
- WRONG: Applying $\psi = 0$ at a finite potential wall
- RIGHT: $\psi = 0$ only at infinite potential walls. At finite walls, $\psi$ decays exponentially into the forbidden region

**4. Selection rules:**
- WRONG: "$\Delta n = \pm 1$" (this is for harmonic oscillator only!)
- RIGHT: For hydrogen, $\Delta l = \pm 1$ with no restriction on $\Delta n$

**5. Probability vs probability amplitude:**
- WRONG: "The probability is $\psi$"
- RIGHT: The probability density is $|\psi|^2$, and probability is $\int|\psi|^2 dx$

**6. Measurement:**
- WRONG: "The measurement disturbs the system and causes the collapse"
- RIGHT: In the Copenhagen interpretation, collapse is a fundamental postulate — not caused by any physical disturbance. The system literally has no definite value before measurement.

### 13.3 Calculation Errors

**1. Compton wavelength vs Compton shift:**
- $\lambda_C = h/(m_e c) = 0.00243$ nm (a constant)
- $\Delta\lambda = \lambda_C(1 - \cos\theta)$ (depends on angle)

**2. Tunneling:**
- WRONG: $T = e^{-\kappa L}$ (missing factor of 2)
- RIGHT: $T = e^{-2\kappa L}$

**3. Hydrogen energy:**
- WRONG: $E_n = -13.6/n$ (missing square)
- RIGHT: $E_n = -13.6/n^2$ eV

**4. Angular momentum:**
- WRONG: $L_z = \sqrt{l(l+1)}\hbar$ (this is $L$, the total)
- RIGHT: $L_z = m_l\hbar$ (the $z$-component), and $|m_l| \leq l$, so $L_z < L$

**5. Photoelectric effect:**
- WRONG: $h\nu = \phi - K_{\max}$
- RIGHT: $h\nu = \phi + K_{\max}$ (photon energy goes to both work function AND kinetic energy)

**6. Harmonic oscillator quantum number:**
- WRONG: $E_n = n\hbar\omega$ for $n = 0, 1, 2, \ldots$
- RIGHT: $E_n = (n + 1/2)\hbar\omega$ (don't forget the 1/2!)

### 13.4 Conceptual Traps on Exams

**Trap 1: "Does the electron orbit the nucleus?"**
No. The electron exists as a probability cloud (orbital). It does not follow a classical trajectory.

**Trap 2: "Can we know both position and momentum exactly?"**
No. The uncertainty principle is a fundamental limit, not a measurement limitation.

**Trap 3: "Why doesn't the electron fall into the nucleus?"**
The uncertainty principle prevents it. Confining the electron to the nuclear size would require such a large momentum uncertainty that the kinetic energy would far exceed the binding energy.

**Trap 4: "What is the wavelength of a baseball?"**
Mathematically, $\lambda = h/(mv) \approx 10^{-34}$ m. Practically, this is meaningless — wave effects are undetectable for macroscopic objects.

**Trap 5: "Does tunneling violate energy conservation?"**
No. The particle has the same energy before and after tunneling. It's the position that changes, not the energy. The kinetic energy inside the barrier becomes imaginary ($E < V_0$), but the particle appears on the other side with its original energy.

**Trap 6: "How many electrons can fit in the $n = 2$ shell?"**
8 (not 4!). The $n = 2$ shell has $l = 0$ (2 electrons) and $l = 1$ (6 electrons) = 8 total. The subshell structure matters!

---

## 14. Quick-Reference Formula Tables

### Table 1: Fundamental Constants

| Constant | Symbol | Value |
|----------|--------|-------|
| Planck's constant | $h$ | $6.626 \times 10^{-34}$ J·s |
| Reduced Planck's constant | $\hbar$ | $1.055 \times 10^{-34}$ J·s |
| Electron mass | $m_e$ | $9.109 \times 10^{-31}$ kg |
| Proton mass | $m_p$ | $1.673 \times 10^{-27}$ kg |
| Elementary charge | $e$ | $1.602 \times 10^{-19}$ C |
| Speed of light | $c$ | $3.00 \times 10^8$ m/s |
| Boltzmann constant | $k$ | $1.381 \times 10^{-23}$ J/K |
| Bohr radius | $a_0$ | $5.29 \times 10^{-11}$ m |
| Rydberg energy | $R_E$ | 13.6 eV |
| Rydberg constant | $R_H$ | $1.097 \times 10^7$ m⁻¹ |
| Compton wavelength | $\lambda_C$ | $2.426 \times 10^{-12}$ m |
| Useful product | $hc$ | 1240 eV·nm |

### Table 2: Key Formulas by Topic

| Topic | Formula | Notes |
|-------|---------|-------|
| **Photoelectric effect** | $h\nu = \phi + K_{\max}$ | $K_{\max} = eV_s$ |
| | $\nu_0 = \phi/h$ | Threshold frequency |
| **de Broglie wavelength** | $\lambda = h/p$ | Universal |
| | $\lambda = h/\sqrt{2meV}$ | For electrons accelerated through $V$ |
| **Compton scattering** | $\Delta\lambda = \lambda_C(1-\cos\theta)$ | $\lambda_C = h/(m_e c)$ |
| **Uncertainty principle** | $\Delta x \cdot \Delta p \geq \hbar/2$ | Fundamental limit |
| **Particle in box** | $E_n = n^2h^2/(8mL^2)$ | $n = 1, 2, 3, \ldots$ |
| | $\psi_n = \sqrt{2/L}\sin(n\pi x/L)$ | Normalized |
| **Harmonic oscillator** | $E_n = (n+1/2)\hbar\omega$ | $n = 0, 1, 2, \ldots$ |
| | $\Delta E = \hbar\omega$ | Equal spacing |
| **Hydrogen atom** | $E_n = -13.6/n^2$ eV | Only depends on $n$ |
| | $a_0 = 0.529$ Å | Most probable distance (1s) |
| | $R = \sqrt{l(l+1)}\hbar$ | Orbital angular momentum |
| | $L_z = m_l\hbar$ | z-component |
| **Hydrogen spectrum** | $1/\lambda = R_H(1/n_1^2 - 1/n_2^2)$ | Rydberg formula |
| **Tunneling** | $T \approx e^{-2\kappa L}$ | Thick barrier approximation |
| | $\kappa = \sqrt{2m(V_0-E)}/\hbar$ | Decay constant |
| **Selection rules** | $\Delta l = \pm 1$ | Electric dipole |
| | $\Delta m_l = 0, \pm 1$ | Electric dipole |

### Table 3: Hydrogen Atom Quantum Numbers and Degeneracy

| $n$ | $l$ values | Total states (no spin) | Total states (with spin) | Energy (eV) |
|-----|-----------|----------------------|------------------------|-------------|
| 1 | 0 | 1 | 2 | -13.60 |
| 2 | 0, 1 | 4 | 8 | -3.40 |
| 3 | 0, 1, 2 | 9 | 18 | -1.51 |
| 4 | 0, 1, 2, 3 | 16 | 32 | -0.85 |
| 5 | 0, 1, 2, 3, 4 | 25 | 50 | -0.54 |

### Table 4: Hydrogen Spectral Series

| Series | Lower Level $n_1$ | Upper Level $n_2$ | Wavelength Range | Region |
|--------|-------------------|-------------------|-----------------|--------|
| Lyman | 1 | 2, 3, 4, ... | 91–122 nm | Ultraviolet |
| Balmer | 2 | 3, 4, 5, ... | 365–656 nm | Visible |
| Paschen | 3 | 4, 5, 6, ... | 820–1875 nm | Near infrared |
| Brackett | 4 | 5, 6, 7, ... | 1458–4051 nm | Infrared |
| Pfund | 5 | 6, 7, 8, ... | 2279–7460 nm | Far infrared |

### Table 5: Comparison of Quantum Models

| Model | Potential | Energy Levels | Wave Function | Key Application |
|-------|-----------|--------------|---------------|-----------------|
| Free particle | $V = 0$ | Continuous ($E > 0$) | Plane wave $e^{ikx}$ | Scattering |
| Particle in box | $V = 0$ inside, $\infty$ outside | $E_n \propto n^2$ | $\sin(n\pi x/L)$ | Confinement, quantum dots |
| Harmonic oscillator | $V = \frac{1}{2}m\omega^2 x^2$ | $E_n = (n+\frac{1}{2})\hbar\omega$ | Hermite × Gaussian | Molecular vibrations, phonons |
| Hydrogen atom | $V = -e^2/(4\pi\epsilon_0 r)$ | $E_n \propto 1/n^2$ | Laguerre × spherical harmonics | Atomic physics |
| Finite square well | $V = V_0$ inside, 0 outside | Few bound states | Oscillatory + exponential decay | Quantum wells, nuclei |
| Morse potential | $V = D_e(1-e^{-a(r-r_e)})^2$ | Anharmonic | — | Diatomic molecules |

### Table 6: Useful Integrals

| Integral | Result |
|----------|--------|
| $\int_0^L \sin^2(n\pi x/L)\, dx$ | $L/2$ |
| $\int_0^L \sin(m\pi x/L)\sin(n\pi x/L)\, dx$ | $(L/2)\delta_{mn}$ |
| $\int_{-\infty}^{\infty} e^{-ax^2}\, dx$ | $\sqrt{\pi/a}$ |
| $\int_{-\infty}^{\infty} x^2 e^{-ax^2}\, dx$ | $\frac{1}{2a}\sqrt{\pi/a}$ |
| $\int_0^\infty x^n e^{-ax}\, dx$ | $n!/a^{n+1}$ |

---

## 15. Cross-References

- [[engineering-physics/module-1-optics-interference-diffraction|Module 1: Interference & Diffraction]] — Wave nature of light → wave-particle duality; Davisson-Germer experiment confirms de Broglie hypothesis
- [[engineering-physics/module-2-optoelectronics-lasers-fiber-optics|Module 2: Optoelectronics]] — Stimulated emission, laser physics, semiconductor lasers — all rely on quantum energy levels and transitions
- [[engineering-physics/module-4-semiconductors-electromagnetism|Module 4: Semiconductors & Electromagnetism]] — Energy bands from quantum mechanics, Fermi-Dirac statistics, quantum tunneling in tunnel diodes and STM

**Connections to other fields:**
- **Quantum Chemistry:** Molecular orbitals, chemical bonding, spectroscopy
- **Quantum Computing:** Qubits, superposition, entanglement
- **Nuclear Physics:** Alpha decay (tunneling), nuclear energy levels
- **Particle Physics:** Fundamental particles as excitations of quantum fields

---

*Module 3 of 4 — [[engineering-physics/module-1-optics-interference-diffraction|← Module 1]] | [[engineering-physics/module-2-optoelectronics-lasers-fiber-optics|← Module 2]] | [[engineering-physics/module-4-semiconductors-electromagnetism|Module 4 →]]*

---

## 16. Exam Preparation Checklist

- [ ] Can derive the photoelectric equation and calculate work function, stopping potential, threshold frequency
- [ ] Can calculate de Broglie wavelength for particles accelerated through voltage
- [ ] Can solve the particle-in-a-box problem (energy levels, wave functions, normalization)
- [ ] Can calculate expectation values ($\langle x \rangle$, $\langle p \rangle$, $\Delta x$, $\Delta p$)
- [ ] Can verify the uncertainty principle for specific states
- [ ] Can apply harmonic oscillator energy formula and use ladder operators
- [ ] Can identify hydrogen quantum numbers and count degeneracies
- [ ] Can apply selection rules to determine allowed/forbidden transitions
- [ ] Can calculate hydrogen spectral line wavelengths (Rydberg formula)
- [ ] Can solve Compton scattering problems (wavelength shift, kinetic energy)
- [ ] Can estimate tunneling probabilities
- [ ] Can interpret probability density plots
- [ ] Can distinguish between fermions and bosons and apply Pauli exclusion principle
- [ ] Can use Dirac notation for inner products and expectation values
- [ ] Can apply perturbation theory for first-order energy corrections

---

*Last updated: 2026-08-17*
