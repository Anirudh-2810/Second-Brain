---
module: "physics"
topic: "Physics Formula Sheet — Mechanics (JEE Advanced)"
tags: [physics, mechanics, formulas, jee, kinematics, dynamics, rotational, gravitation]
last_updated: "2026-08-11"
source: "Kota notes, standard references"
---

# Physics Formula Sheet — Mechanics (JEE Advanced)

> Complete mechanics formula compendium. Every formula with conditions and sign conventions.

---

## 📐 Kinematics

| Quantity | Formula | Conditions |
|----------|---------|------------|
| **1D Constant Acceleration** | | |
| $v$ | $u + at$ | |
| $s$ | $ut + \frac{1}{2}at^2$ | |
| $v^2$ | $u^2 + 2as$ | |
| $s_{nth}$ | $u + \frac{a}{2}(2n-1)$ | Displacement in $n$-th second |
| **Projectile Motion** | | |
| Range $R$ | $\frac{u^2 \sin 2\theta}{g}$ | Same level |
| Max Height $H$ | $\frac{u^2 \sin^2 \theta}{2g}$ | |
| Time of Flight $T$ | $\frac{2u \sin \theta}{g}$ | |
| Trajectory | $y = x \tan \theta - \frac{g x^2}{2 u^2 \cos^2 \theta}$ | Origin at launch |
| Range on Inclined Plane | $\frac{u^2}{g \cos^2 \beta}[\sin(2\alpha - \beta) \mp \sin \beta]$ | $\pm$ for up/down plane |
| **Relative Motion** | | |
| $\vec{v}_{AB}$ | $\vec{v}_A - \vec{v}_B$ | |
| $\vec{a}_{AB}$ | $\vec{a}_A - \vec{a}_B$ | |
| **Variable Acceleration** | | |
| $a = f(t)$ | $v = u + \int_0^t f(t) dt$; $s = \int v dt$ | |
| $a = f(v)$ | $t = \int \frac{dv}{f(v)}$; $s = \int \frac{v dv}{f(v)}$ | |
| $a = f(x)$ | $v^2 = u^2 + 2 \int f(x) dx$ | |
| **Graphs** | | |
| $x-t$ slope | $v$ | |
| $v-t$ slope | $a$; area = $s$ | |
| $a-t$ area | $\Delta v$ | |

---

## 📐 Laws of Motion & Friction

| Quantity | Formula |
|----------|---------|
| **Newton's 2nd** | $\vec{F}_{net} = m \vec{a} = \frac{d\vec{p}}{dt}$ |
| **Impulse** | $\vec{J} = \int \vec{F} dt = \Delta \vec{p}$ |
| **Static Friction** | $f_s \le \mu_s N$; max $= \mu_s N$ |
| **Kinetic Friction** | $f_k = \mu_k N$ |
| **Rolling Friction** | $f_r = \mu_r N$ (very small) |
| **Angle of Repose** | $\theta_r = \tan^{-1} \mu_s$ |
| **System of Particles** | $\vec{F}_{ext} = M \vec{a}_{cm}$; $\vec{a}_{cm} = \frac{\sum m_i \vec{a}_i}{\sum m_i}$ |

---

## 📐 Work, Energy, Power

| Quantity | Formula |
|----------|---------|
| **Work** | $W = \int \vec{F} \cdot d\vec{s}$; $W = F s \cos\theta$ (const $F$) |
| **Work-Energy Theorem** | $W_{net} = \Delta K = K_f - K_i$ |
| **Conservative Force** | $W_{cons} = -\Delta U$; $\vec{F} = -\nabla U = -\frac{dU}{dx} \hat{i}$ |
| **Potential Energy** | Spring: $U = \frac{1}{2} k x^2$; Gravitational: $U = mgh$ (near Earth) |
| **Total Mechanical Energy** | $E = K + U$ (conserved if only conservative forces) |
| **Power** | $P = \frac{dW}{dt} = \vec{F} \cdot \vec{v}$; $P_{avg} = \frac{W}{t}$ |
| **Collisions** | |
| Coefficient of Restitution | $e = \frac{v_2' - v_1'}{v_1 - v_2}$ ($0 \le e \le 1$) |
| Elastic ($e=1$) | $K$ conserved, $v_{sep} = v_{app}$ |
| Inelastic ($e<1$) | $K$ not conserved; perfectly inelastic ($e=0$): stick together |
| 1D Elastic | $v_1' = \frac{m_1 - m_2}{m_1 + m_2} v_1 + \frac{2m_2}{m_1 + m_2} v_2$ |
| 1D Inelastic | $v_1' = \frac{m_1 - e m_2}{m_1 + m_2} v_1 + \frac{(1+e)m_2}{m_1 + m_2} v_2$ |
| 2D Elastic | Momentum conserved in both axes; $K$ conserved |

---

## 📐 Rotational Motion

| Quantity | Formula |
|----------|---------|
| **Angular Kinematics** | $\omega = \omega_0 + \alpha t$; $\theta = \omega_0 t + \frac{1}{2} \alpha t^2$; $\omega^2 = \omega_0^2 + 2\alpha\theta$ |
| **Moment of Inertia** | $I = \sum m_i r_i^2 = \int r^2 dm$ |
| Parallel Axis | $I = I_{cm} + M d^2$ |
| Perpendicular Axis (lamina) | $I_z = I_x + I_y$ |
| **Common $I$ Values** | |
| Ring (axis ⟂ plane) | $MR^2$ |
| Disc (axis ⟂ plane) | $\frac{1}{2} MR^2$ |
| Solid Sphere | $\frac{2}{5} MR^2$ |
| Hollow Sphere | $\frac{2}{3} MR^2$ |
| Rod (about center ⟂) | $\frac{1}{12} ML^2$ |
| Rod (about end ⟂) | $\frac{1}{3} ML^2$ |
| **Torque & Angular Momentum** | $\vec{\tau} = \vec{r} \times \vec{F}$; $\tau = I \alpha$; $\vec{L} = \vec{r} \times \vec{p} = I \vec{\omega}$ |
| **Rotational Work-Energy** | $W = \int \tau d\theta = \Delta K_{rot}$; $K_{rot} = \frac{1}{2} I \omega^2$ |
| **Rolling Without Slipping** | $v = \omega R$; $a = \alpha R$; $K_{total} = \frac{1}{2} I_{cm} \omega^2 + \frac{1}{2} M v^2 = \frac{1}{2} M v^2 (1 + \frac{K^2}{R^2})$ |
| Acceleration down incline | $a = \frac{g \sin \theta}{1 + K^2/R^2}$; $f = \frac{Mg \sin \theta}{1 + R^2/K^2}$ |
| **Conservation Laws** | $\tau_{ext} = 0 \implies L = \text{const}$; $F_{ext} = 0 \implies P = \text{const}$ |
| **Instantaneous Axis of Rotation (IAR)** | For rolling body: IAR at contact point; $\omega_{IAR} = \omega_{cm}$; $v_P = \omega_{IAR} \times r_{P/IAR}$ |

---

## 📐 Gravitation

| Quantity | Formula |
|----------|---------|
| **Universal Law** | $F = \frac{G m_1 m_2}{r^2}$; $G = 6.67 \times 10^{-11}$ N·m²/kg² |
| **Field & Potential** | $E = \frac{GM}{r^2}$ (toward center); $V = -\frac{GM}{r}$ (zero at $\infty$) |
| **Shell Theorem** | Outside: $E = \frac{GM}{r^2}$, $V = -\frac{GM}{r}$; Inside: $E = 0$, $V = -\frac{GM}{R}$ (const) |
| **Solid Sphere** | $E = \frac{GM r}{R^3}$ (inside); $V = -\frac{GM}{2R}(3 - \frac{r^2}{R^2})$ (inside) |
| **$g$ Variations** | Height: $g_h = g(1 - \frac{2h}{R})$; Depth: $g_d = g(1 - \frac{d}{R})$; Latitude: $g_\lambda = g - \omega^2 R \cos^2 \lambda$ |
| **Escape Velocity** | $v_{esc} = \sqrt{\frac{2GM}{R}} = \sqrt{2gR} \approx 11.2$ km/s |
| **Orbital Velocity** | $v_{orb} = \sqrt{\frac{GM}{r}}$; $v_{orb} = \sqrt{g(R+h)}$ near surface |
| **Time Period** | $T = 2\pi \sqrt{\frac{r^3}{GM}}$; $T^2 \propto r^3$ (Kepler's 3rd) |
| **Satellite Energy** | $K = \frac{GMm}{2r}$; $U = -\frac{GMm}{r}$; $E = K + U = -\frac{GMm}{2r}$ |
| **Geostationary** | $T = 24$ h; $h \approx 36000$ km; $r \approx 6.6 R_E$ |
| **Binding Energy** | $BE = \frac{GMm}{2r}$ (energy to escape to $\infty$) |

---

## 📐 Fluid Mechanics

| Quantity | Formula |
|----------|---------|
| **Pressure** | $P = P_0 + \rho gh$; $P = \frac{F}{A}$ |
| **Pascal's Law** | $\Delta P$ transmitted undiminished |
| **Buoyancy (Archimedes)** | $F_b = \rho_{fluid} V_{sub} g = \text{weight of displaced fluid}$ |
| **Floatation** | $\frac{V_{sub}}{V_{body}} = \frac{\rho_{body}}{\rho_{fluid}}$ |
| **Continuity** | $A_1 v_1 = A_2 v_2$ (incompressible) |
| **Bernoulli** | $P + \frac{1}{2} \rho v^2 + \rho gh = \text{const}$ (streamline, steady, incompressible, non-viscous) |
| **Torricelli** | $v = \sqrt{2gh}$ (efflux speed) |
| **Viscosity (Newtonian)** | $F = \eta A \frac{dv}{dy}$; $\eta$ = coefficient of viscosity |
| **Stokes' Law** | $F = 6\pi \eta r v$ (sphere, low Re); Terminal: $v_T = \frac{2}{9} \frac{r^2 (\rho - \sigma) g}{\eta}$ |
| **Surface Tension** | $F = T l$; $T$ = force per unit length |
| **Excess Pressure** | Liquid drop: $\frac{2T}{R}$; Soap bubble: $\frac{4T}{R}$; Air bubble in liquid: $\frac{2T}{R}$ |
| **Capillary Rise** | $h = \frac{2T \cos\theta}{\rho g r}$; $h = \frac{2T}{\rho g r}$ ($\theta=0$) |

---

## 📐 Properties of Matter

| Quantity | Formula |
|----------|---------|
| **Stress** | $\frac{F}{A}$ |
| **Strain** | $\frac{\Delta L}{L}$ (longitudinal); $\frac{\Delta V}{V}$ (volumetric); $\frac{\Delta x}{L}$ (shear) |
| **Young's Modulus** | $Y = \frac{\text{Stress}}{\text{Strain}} = \frac{F/A}{\Delta L/L}$ |
| **Bulk Modulus** | $B = -\frac{V \Delta P}{\Delta V} = -\frac{\Delta P}{\Delta V/V}$ |
| **Shear Modulus** | $\eta = \frac{\text{Shear stress}}{\text{Shear strain}} = \frac{F/A}{\Delta x/L}$ |
| **Poisson's Ratio** | $\sigma = -\frac{\text{Lateral strain}}{\text{Longitudinal strain}}$ |
| **Relations** | $Y = 3B(1-2\sigma)$; $Y = 2\eta(1+\sigma)$; $\frac{9}{Y} = \frac{3}{B} + \frac{1}{\eta}$ |
| **Thermal Stress** | $\frac{F}{A} = Y \alpha \Delta T$ (fully constrained) |
| **Thermal Expansion** | $\Delta L = L \alpha \Delta T$; $\Delta A = 2A \alpha \Delta T$; $\Delta V = 3V \alpha \Delta T$ |
| **Elastic Energy** | $U = \frac{1}{2} \text{Stress} \times \text{Strain} \times \text{Volume} = \frac{1}{2} \frac{Y A}{L} (\Delta L)^2 = \frac{F^2 L}{2 A Y}$ |

---

## 📐 Center of Mass & Collisions

| Quantity | Formula |
|----------|---------|
| **COM (Discrete)** | $\vec{r}_{cm} = \frac{\sum m_i \vec{r}_i}{\sum m_i}$ |
| **COM (Continuous)** | $\vec{r}_{cm} = \frac{\int \vec{r} dm}{\int dm}$ |
| **Velocity of COM** | $\vec{v}_{cm} = \frac{\sum m_i \vec{v}_i}{\sum m_i}$ |
| **Momentum of System** | $\vec{P}_{total} = M \vec{v}_{cm}$ |
| **Rocket Equation** | $v = u \ln\frac{M_0}{M} - gt$ (vertical, no external force except gravity) |
| **Common COM** | Semicircular ring: $2R/\pi$; Semicircular disc: $4R/3\pi$; Solid hemisphere: $3R/8$; Hollow hemisphere: $R/2$; Solid cone: $h/4$; Hollow cone: $h/3$ |

---

*Mechanics formula sheet — sign conventions: $g$ downward, $\theta$ from horizontal, torque positive CCW. Cross-reference with topic-wise notes for derivations.*