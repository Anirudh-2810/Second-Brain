---
module: "engineering-physics"
topic: "Module 1: Optics — Interference, Diffraction & Polarization"
tags: [optics, interference, diffraction, polarization, wave-optics, ydse, fresnel, fraunhofer, thin-film, newtons-rings, grating, malus-law, brewster]
last_updated: "2026-08-17"
prerequisites: ["Wave Motion", "SHM", "Basic Trigonometry", "Trigonometric Identities"]
---

# Module 1: Optics — Interference, Diffraction & Polarization

> A comprehensive deep dive into wave optics: the phenomena that prove light is a wave. Covers every major topic from Huygens' principle through polarization, with full derivations, 12+ worked numerical problems, ASCII flowcharts, and a complete formula reference.

---

## Table of Contents

1. [Wave Nature of Light — Foundation](#1-wave-nature-of-light--foundation)
2. [Interference of Light](#2-interference-of-light)
3. [Interference in Thin Films](#3-interference-in-thin-films)
4. [Newton's Rings](#4-newtons-rings)
5. [Diffraction of Light](#5-diffraction-of-light)
6. [Diffraction Grating](#6-diffraction-grating)
7. [Resolving Power & Rayleigh Criterion](#7-resolving-power--rayleigh-criterion)
8. [Polarization of Light](#8-polarization-of-light)
9. [Advanced Topics](#9-advanced-topics)
10. [ASCII Flowcharts](#10-ascii-flowcharts)
11. [Common Mistakes](#11-common-mistakes)
12. [Worked Numerical Examples](#12-worked-numerical-examples)
13. [Complete Formula Reference Table](#13-complete-formula-reference-table)

---

## 1. Wave Nature of Light — Foundation

### 1.1 Huygens' Principle

Every point on a wavefront acts as a secondary source of spherical wavelets. The new wavefront is the **envelope** (tangent surface) of these wavelets after a time interval $\Delta t$.

**Postulates:**
1. Each point on a primary wavefront serves as a source of secondary spherical wavelets.
2. The secondary wavelets spread out in all directions with the speed of the wave.
3. The new wavefront at a later time is the forward envelope of all secondary wavelets.
4. The backward envelope is not considered (no backward propagation).

**Key consequences and derivations:**

**a) Rectilinear propagation:** In a homogeneous medium, the wavefronts remain the same shape. The envelope of spherical wavelets from a plane wavefront is another plane wavefront shifted forward.

**b) Laws of reflection:**

Consider a plane wavefront AB incident on a reflecting surface at angle $i$. By the time point B reaches the surface (travels distance BC), point A has generated a spherical wavelet of radius AD = BC. From the geometry:

```
    A ________________ B
     \               /
      \    i    r   /
       \    \  /   /
        \    \/   /
         \   /\  /
          \ /  \/
           O----C
```

In triangles OAD and OBC:
- AD = BC (same time, same speed)
- OA = OC (hypotenuse of equal right triangles... not quite)

More carefully: The normal at O bisects angle DOC. Triangles AOD and COB are congruent (RHS: AD = BC, OD = OB). Therefore angle AOD = angle COB, which means $i = r$.

**c) Snell's Law of refraction:**

When the wavefront passes from medium 1 (speed $v_1$) to medium 2 (speed $v_2$):

$$\frac{\sin i}{\sin r} = \frac{v_1}{v_2} = \mu_{21}$$

where $\mu_{21}$ is the refractive index of medium 2 relative to medium 1.

**Derivation:** When point B travels distance BC in medium 2 while A generates wavelet of radius AD in medium 1:

- BC / $v_2$ = AD / $v_1$ = time
- From geometry: $\sin i$ = AD/OA, $\sin r$ = BC/OA (approximately, for small prism angles near the point of incidence)

Actually more precisely: AD = OA sin i, BC = OC sin r, and OA ≈ OC (for the limit as the wavefront approaches the surface). Therefore:

$$\frac{\sin i}{\sin r} = \frac{AD}{BC} = \frac{v_1}{v_2}$$

**Limitations of Huygens' principle:**
- Does not explain intensity distribution in diffraction patterns
- Does not explain polarization
- Does not explain why diffraction effects are not noticeable for large obstacles
- The principle of backward wavelets requires further justification

### 1.2 Superposition Principle

When two or more waves overlap in the same region of space, the resultant displacement at any point is the **vector sum** of individual displacements at that point.

$$\vec{E}_{net} = \vec{E}_1 + \vec{E}_2 + \vec{E}_3 + \cdots$$

This holds for **linear waves** (small amplitudes, linear medium). For electromagnetic waves, this is a direct consequence of the linearity of Maxwell's equations.

**Important:** Superposition applies to displacements (electric fields), NOT to intensities directly. Intensity must be computed from the resultant amplitude.

### 1.3 Coherence

Two sources are **coherent** if they maintain a constant phase difference over time.

**Detailed comparison:**

| Property | Coherent Sources | Incoherent Sources |
|----------|------------------|--------------------|
| Phase relation | Constant $\Delta\phi$ | Randomly varying |
| Same frequency | Yes | Not required |
| Same wavelength | Yes | Not required |
| Same amplitude | Not required | Not required |
| Example | Split single source (YDSE) | Two independent bulbs |
| Fringe visibility | High | Zero |

**Why coherence matters:** Interference fringes are only visible with coherent sources. Independent sources produce rapidly changing phase differences that average out over any detection time → time-averaged intensity = sum of individual intensities (no fringes visible).

**Temporal coherence:** Related to the monochromaticity of the source. A perfectly monochromatic source has infinite temporal coherence. Real sources have a finite coherence length $l_c = c \cdot \tau_c$ where $\tau_c$ is the coherence time.

**Spatial coherence:** Related to the finite size of the source. Two points separated by more than the spatial coherence width cannot produce visible interference.

### 1.4 Intensity from Superposition — Complete Derivation

Consider two waves with the same amplitude and frequency but different phases:

$$E_1 = E_0 \sin(\omega t)$$
$$E_2 = E_0 \sin(\omega t + \phi)$$

Using the superposition principle:

$$E_{net} = E_0 \sin(\omega t) + E_0 \sin(\omega t + \phi)$$

Apply the sum-to-product identity: $\sin A + \sin B = 2\cos\!\left(\frac{A-B}{2}\right)\sin\!\left(\frac{A+B}{2}\right)$

Let $A = \omega t + \phi$, $B = \omega t$:

$$E_{net} = 2E_0 \cos\!\left(\frac{\phi}{2}\right) \sin\!\left(\omega t + \frac{\phi}{2}\right)$$

This shows:
- **Amplitude:** $A_{net} = 2E_0 \cos(\phi/2)$
- **Phase:** The resultant wave has a phase that is the average of the two original phases.
- The wave oscillates at the same frequency $\omega$.

**Intensity** is proportional to the square of the amplitude:

$$I = I_{net} \propto A_{net}^2 = 4E_0^2 \cos^2\!\left(\frac{\phi}{2}\right)$$

If each individual wave has intensity $I_0 \propto E_0^2$:

$$\boxed{I = 4I_0 \cos^2\!\left(\frac{\phi}{2}\right)}$$

**Special cases:**

| Phase difference $\phi$ | $\cos^2(\phi/2)$ | Intensity $I$ | Type |
|------------------------|-------------------|----------------|------|
| $0, 2\pi, 4\pi, \ldots$ ($2n\pi$) | 1 | $4I_0$ | Maximum (constructive) |
| $\pi, 3\pi, 5\pi, \ldots$ ($(2n+1)\pi$) | 0 | 0 | Minimum (destructive) |
| $\pi/2, 3\pi/2, \ldots$ | 1/2 | $2I_0$ | Half-maximum |

**Key insight:** The total energy is conserved. Energy is redistributed from the dark regions to the bright regions. The average intensity over the entire pattern is $2I_0$ (the sum of individual intensities).

**For unequal amplitudes:** If $E_1 = A_1 \sin(\omega t)$ and $E_2 = A_2 \sin(\omega t + \phi)$:

$$I = I_1 + I_2 + 2\sqrt{I_1 I_2}\cos\phi$$

- $I_{max} = (\sqrt{I_1} + \sqrt{I_2})^2$ when $\phi = 0$
- $I_{min} = (\sqrt{I_1} - \sqrt{I_2})^2$ when $\phi = \pi$

**Fringe visibility:**

$$V = \frac{I_{max} - I_{min}}{I_{max} + I_{min}} = \frac{2\sqrt{I_1 I_2}}{I_1 + I_2}$$

For equal intensities, $V = 1$ (perfect contrast). For very unequal intensities, $V \approx 0$.

### 1.5 Beats (Temporal Interference)

When two waves of slightly different frequencies $f_1$ and $f_2$ interfere:

$$I = 4I_0 \cos^2\!\left[2\pi \cdot \frac{f_1 - f_2}{2} \cdot t\right] \cos^2\!\left[2\pi \cdot \frac{f_1 + f_2}{2} \cdot t\right]$$

The intensity oscillates at the **beat frequency:**

$$f_{beat} = |f_1 - f_2|$$

---

## 2. Interference of Light

### 2.1 Young's Double Slit Experiment (YDSE)

**Setup:** A monochromatic source $S$ illuminates a barrier with two narrow slits $S_1$ and $S_2$ separated by distance $d$. A screen at distance $D$ ($D \gg d$) shows interference fringes.

```
                   Screen
    S              |  P (at height y)
    *              |
     \             |
      \   D'       |     D
       \           |
    S1  *----------*--------
    S2  *----------*--------
         \         |
          d        |
```

**Geometric path difference at point P:**

Point P is at height $y$ above the central axis.

Distance from $S_1$ to P: $r_1 = \sqrt{D^2 + (y - d/2)^2}$

Distance from $S_2$ to P: $r_2 = \sqrt{D^2 + (y + d/2)^2}$

**Path difference:**

$$\Delta = r_2 - r_1$$

**Derivation using the approximation:**

For $D \gg d$ and $D \gg y$:

$$r_1 = D\sqrt{1 + \frac{(y - d/2)^2}{D^2}} \approx D\left[1 + \frac{(y - d/2)^2}{2D^2}\right]$$

$$r_2 = D\sqrt{1 + \frac{(y + d/2)^2}{D^2}} \approx D\left[1 + \frac{(y + d/2)^2}{2D^2}\right]$$

$$\Delta = r_2 - r_1 \approx \frac{(y + d/2)^2 - (y - d/2)^2}{2D} = \frac{2yd}{2D} = \frac{yd}{D}$$

Also, $\Delta = d\sin\theta$ where $\theta$ is the angle subtended at the midpoint of the slits.

For small $\theta$: $\sin\theta \approx \theta \approx \tan\theta = y/D$, so $\Delta \approx yd/D$.

**Phase difference:**

$$\phi = \frac{2\pi}{\lambda} \cdot \Delta = \frac{2\pi yd}{\lambda D}$$

**Conditions for interference:**

**Constructive interference (bright fringes):**

$$\Delta = n\lambda \quad (n = 0, \pm 1, \pm 2, \ldots)$$

$$\phi = 2n\pi$$

$$\boxed{y_n = \frac{n\lambda D}{d}}$$

**Destructive interference (dark fringes):**

$$\Delta = (2n - 1)\frac{\lambda}{2} \quad (n = \pm 1, \pm 2, \ldots)$$

$$\phi = (2n - 1)\pi$$

$$\boxed{y_n = \frac{(2n-1)\lambda D}{2d}}$$

**Fringe width (spacing between consecutive bright or dark fringes):**

$$\boxed{\beta = \frac{\lambda D}{d}}$$

**Derivation:** $y_{n+1} - y_n = \frac{(n+1)\lambda D}{d} - \frac{n\lambda D}{d} = \frac{\lambda D}{d}$

**Key observations:**
- Fringes are equally spaced (for small angles where $\sin\theta \approx \theta$)
- Central fringe ($n = 0$) is always bright
- Increasing $D$ → wider fringes
- Increasing $d$ → narrower fringes
- Increasing $\lambda$ → wider fringes (red fringes wider than blue)
- Total number of fringes visible: roughly $2D/d$ (within $|\theta| < 90°$)

### 2.2 Intensity Distribution in YDSE

$$I(\theta) = 4I_0 \cos^2\!\left(\frac{\pi d \sin\theta}{\lambda}\right)$$

**Derivation:** The phase difference is $\phi = \frac{2\pi}{\lambda} d\sin\theta$. Substituting into $I = 4I_0 \cos^2(\phi/2)$:

$$I = 4I_0 \cos^2\!\left(\frac{\pi d \sin\theta}{\lambda}\right)$$

**Normalized intensity:** $I/I_{max} = \cos^2(\pi d\sin\theta/\lambda)$

- Bright fringes have $I_{max} = 4I_0$
- Dark fringes have $I_{min} = 0$
- Average intensity = $2I_0$ (energy conservation)
- The $\cos^2$ profile means bright fringes are broad and dark fringes are narrow.

### 2.3 Modifications of YDSE

#### Case 1: Source Displaced Perpendicular to Slits

If source $S$ is moved up by distance $x$ from the central axis:

```
           S (displaced up by x)
           *
          /|
         / |
        /  | x
       /   |
      /    |
     S1 *--*--------
     S2 *--------
```

The path difference from the displaced source to the two slits:

$$\Delta_{extra} = S S_2 - S S_1 \approx \frac{xd}{D'}$$

where $D'$ is the distance from the source plane to the slit plane.

**The entire fringe pattern shifts** so that the new central maximum is at:

$$\boxed{y_0 = -\frac{xD}{D'}}$$

(negative sign means shift is opposite to the source displacement)

**Physical reason:** The source displacement introduces a fixed path difference at the slits. The pattern shifts to compensate, so the point where total path difference = 0 becomes the new center.

#### Case 2: Thin Transparent Sheet in Front of One Slit

A sheet of thickness $t$ and refractive index $\mu$ is placed in front of slit $S_1$.

**Extra optical path introduced:**

In the sheet, light travels slower: $v = c/\mu$. For physical thickness $t$:
- Optical path in sheet = $\mu t$
- Optical path if air were there = $t$
- Extra optical path = $(\mu - 1)t$

**Fringe shift:**

$$\boxed{\Delta y = \frac{(\mu - 1)tD}{d}}$$

**Entire pattern shifts toward the slit with the sheet** (the sheet "delays" light through that slit, so the central maximum moves toward that slit to equalize the optical paths).

#### Case 3: Immersed in Liquid

If the entire setup is in a liquid of refractive index $\mu$:

$$\lambda_{liquid} = \frac{\lambda_0}{\mu}$$

$$\boxed{\beta_{liquid} = \frac{\lambda_0 D}{\mu d} = \frac{\beta_{air}}{\mu}}$$

Finges become narrower by factor $\mu$.

#### Case 4: White Light Illumination

- Central fringe ($n = 0$): **White** (all wavelengths constructively interfere at $\theta = 0$)
- Colored fringes: Red ($\lambda \approx 700$ nm) fringes are wider → appear farther from center
- Violet ($\lambda \approx 400$ nm) fringes are narrower → appear closer to center
- After a few fringes (around $n = 5$ to $7$), colors overlap → fringes become washed out
- No white light fringes beyond a certain order because different color maxima overlap

#### Case 5: Asymmetric Slit Widths

If the two slits have different widths $a_1$ and $a_2$, the intensities $I_1 \propto a_1^2$ and $I_2 \propto a_2^2$ are unequal. The fringe visibility decreases:

$$V = \frac{2\sqrt{I_1 I_2}}{I_1 + I_2} = \frac{2a_1 a_2}{a_1^2 + a_2^2}$$

The positions of maxima and minima remain the same.

### 2.4 Fresnel Biprism

Two coherent virtual sources $S_1, S_2$ are created by refraction through a thin prism with a very small refracting angle $\alpha$. The interference pattern is identical to YDSE.

**Effective slit separation:**

$$d = 2a(\mu - 1)\alpha$$

where $a$ is the distance from the source to the biprism, and $\mu$ is the refractive index of the prism.

The fringe width and all YDSE formulas apply with this effective $d$.

### 2.5 Lloyd's Mirror

A single plane mirror creates a virtual image $S'$ of the real source $S$. Interference occurs between the direct ray from $S$ and the reflected ray (which appears to come from $S'$).

```
    S (real source)
    |
    |   * S' (virtual image)
    |  /
    | / angle θ
    |/
    *----------- Mirror edge
    |           Screen
    |           |
```

**Critical feature:** The reflected ray undergoes a $\pi$ phase change (equivalent to $\lambda/2$ path difference) upon reflection at the dense medium (the mirror). This means:

- The condition for bright/dark fringes is **reversed** compared to YDSE
- **Bright:** $\Delta + \lambda/2 = (2n+1)\lambda/2$ → $\Delta = n\lambda$ (same as YDSE dark condition)
- **Dark:** $\Delta + \lambda/2 = n\lambda$ → $\Delta = (2n-1)\lambda/2$ (same as YDSE bright condition)
- The fringe at the point where the mirror meets the screen is always **dark** (the path difference approaches zero, but the reflection phase change makes it destructive)

### 2.6 Billet's Split Lens

A convex lens is split into two halves and slightly separated. A single point source $S$ produces two real images $S_1$ and $S_2$ that act as coherent sources. The interference pattern is again identical to YDSE.

---

## 3. Interference in Thin Films

### 3.1 Theory of Thin Film Interference

When light strikes a thin film, reflections occur at both the top and bottom surfaces. The two reflected rays interfere with each other.

```
    Incident ray
         \
          \ θ_i
           \
    --------*---------- Top surface (air → film)
            /\
           /  \ r (refracted angle)
          /    \
         / film  \
        /  μ, t   \
       /____________\ Bottom surface (film → air)
      / θ_r'
     /
    / Reflected ray 2
```

### 3.2 Phase Changes on Reflection — The Critical Concept

**Stokes' rule:** When light reflects from an optically denser medium (higher $\mu$), it undergoes a phase change of $\pi$ (equivalent to a path difference of $\lambda/2$). When reflecting from a rarer medium, there is no phase change.

| Reflection interface | Phase change |
|---------------------|-------------|
| Rare → Dense (e.g., air → glass) | $\pi$ (or $\lambda/2$) |
| Dense → Rare (e.g., glass → air) | 0 |
| Dense → Dense (same $\mu$) | 0 or $\pi$ (depends on context) |

### 3.3 Counting Phase Changes

**For a film of refractive index $\mu$ in air:**

1. **Ray 1 (reflected from top surface):** Air ($\mu = 1$) → Film ($\mu > 1$). Since $1 < \mu$, this is rare → dense → **phase change of $\pi$.**

2. **Ray 2 (reflected from bottom surface, then transmitted back through top):** Film ($\mu$) → Air ($\mu = 1$). Since $\mu > 1$, this is dense → rare → **no phase change.**

**Total phase change count: 1**

This is the most common scenario in exam problems.

### 3.4 Reflected Light Interference — Complete Conditions

The total optical path difference between the two reflected rays (for near-normal incidence, $r \approx 0$):

$$\Delta = 2\mu t + \frac{\lambda}{2}$$

where $2\mu t$ is the extra path length traveled inside the film, and $\lambda/2$ accounts for the single phase change.

**For general angle of refraction $r$:**

$$\Delta = 2\mu t \cos r + \frac{\lambda}{2}$$

**Constructive interference (bright in reflected light) — ONE phase change:**

$$2\mu t \cos r + \frac{\lambda}{2} = n\lambda$$

$$\boxed{2\mu t \cos r = \left(n - \frac{1}{2}\right)\lambda = \frac{(2n-1)\lambda}{2}}$$

For normal incidence ($r = 0$):

$$\boxed{2\mu t = \frac{(2n-1)\lambda}{2}} \quad n = 1, 2, 3, \ldots$$

**Destructive interference (dark in reflected light) — ONE phase change:**

$$2\mu t \cos r + \frac{\lambda}{2} = \left(n + \frac{1}{2}\right)\lambda$$

$$\boxed{2\mu t \cos r = n\lambda}$$

For normal incidence:

$$\boxed{2\mu t = n\lambda} \quad n = 0, 1, 2, \ldots$$

**Note:** $n = 0$ gives $t = 0$ which is physically trivial (no film).

### 3.5 Zero or Two Phase Changes

If both reflections are rare→dense or both are dense→rare (total phase changes = 0 or 2), the conditions flip:

**Constructive (bright):** $2\mu t \cos r = n\lambda$

**Destructive (dark):** $2\mu t \cos r = (2n-1)\lambda/2$

### 3.6 Transmitted Light Interference

The transmitted interference pattern is **complementary** to the reflected one (conservation of energy):

$$\text{Bright in reflected} \iff \text{Dark in transmitted}$$

For normal incidence with ONE phase change at top surface:

**Transmitted bright:** $2\mu t = n\lambda$ (the phase changes for the transmitted rays differ from reflected)

**Transmitted dark:** $2\mu t = (2n-1)\lambda/2$

**Why complementary?** The two reflected rays and the two transmitted rays together account for all the energy. If the reflected rays interfere destructively (all energy transmitted), then the transmitted rays must interfere constructively.

### 3.7 Colored Thin Films

**Soap bubbles and oil films** show colors because different wavelengths satisfy the constructive interference condition at different thicknesses. White light produces a range of colors as the film thickness varies.

- A film of uniform thickness shows a single color (the wavelength that constructively interferes)
- A film of varying thickness (like a soap bubble hanging down) shows bands of color
- The colors change as the film drains (thickness changes with time)

---

## 4. Newton's Rings

### 4.1 Setup

A plano-convex lens of radius of curvature $R$ is placed on a flat glass plate. An air film of varying thickness is formed between them.

```
         plano-convex lens
        _______________
       /               \
      /     R           \
     /                   \
    /                     \
   *-------+-------+------*  Contact point (center)
   |   t   |       |  t   |
   *-------*-------*------*  Flat glass plate
```

At distance $r$ from the contact point, the thickness of the air film is:

$$t = \frac{r^2}{2R}$$

**Derivation:** For the circular cross-section of the lens:

$$R^2 = r^2 + (R - t)^2 = r^2 + R^2 - 2Rt + t^2$$

$$r^2 = 2Rt - t^2 \approx 2Rt \quad (\text{since } t \ll R)$$

$$t = \frac{r^2}{2R}$$

### 4.2 Phase Changes

- **Ray 1 (reflected from bottom of lens):** Glass → Air (dense → rare) → **no phase change**
- **Ray 2 (reflected from top of plate):** Air → Glass (rare → dense) → **phase change of $\pi$**

**Total: 1 phase change** → The standard "one phase change" formulas apply.

### 4.3 Reflected Light (Standard Case)

**Dark rings (destructive):**

$$2t = n\lambda \quad \text{(normal incidence, using the 1 phase change condition)}$$

Substituting $t = r^2/(2R)$:

$$\frac{r^2}{R} = n\lambda$$

$$\boxed{r_n = \sqrt{n\lambda R}} \quad n = 0, 1, 2, \ldots$$

- $n = 0$: $r = 0$ → **Central dark spot** (due to the $\pi$ phase change at the bottom surface)

**Bright rings (constructive):**

$$2t = \left(n + \frac{1}{2}\right)\lambda$$

$$\boxed{r_n = \sqrt{\left(n + \frac{1}{2}\right)\lambda R}} \quad n = 0, 1, 2, \ldots$$

### 4.4 Transmitted Light

The pattern is complementary:

**Bright rings:** $r_n = \sqrt{n\lambda R}$

**Dark rings:** $r_n = \sqrt{\left(n + \frac{1}{2}\right)\lambda R}$

**Central spot is bright** in transmitted light.

### 4.5 Ring Spacing Analysis

**Radius of $n$th dark ring:** $r_n = \sqrt{n\lambda R}$

**Width of $n$th ring (radial width):**

$$\Delta r_n = r_n - r_{n-1} = \sqrt{n\lambda R} - \sqrt{(n-1)\lambda R}$$

$$= \sqrt{\lambda R}\left(\sqrt{n} - \sqrt{n-1}\right)$$

Since $\sqrt{n} - \sqrt{n-1} \approx \frac{1}{2\sqrt{n}}$ for large $n$:

$$\Delta r_n \approx \frac{1}{2}\sqrt{\frac{\lambda R}{n}} = \frac{\lambda R}{2r_n}$$

**Ring spacing decreases** as we go outward (since $r_n \propto \sqrt{n}$, the rings get closer together farther from center).

### 4.6 Measuring Wavelength and Radius of Curvature

**Measurement of wavelength:**

$$\lambda = \frac{r_n^2}{nR}$$

Using two rings: $\lambda = \frac{r_{n+p}^2 - r_n^2}{pR}$ (eliminates zero-error)

**Measurement of radius of curvature:**

$$R = \frac{r_{n+p}^2 - r_n^2}{p\lambda}$$

**Measurement of refractive index of a liquid:**

If the space between the lens and plate is filled with a liquid of refractive index $\mu$:

$$r_n' = \frac{r_n}{\sqrt{\mu}}$$

$$\mu = \left(\frac{r_n}{r_n'}\right)^2 = \frac{r_n^2}{r_n'^2}$$

---

## 5. Diffraction of Light

### 5.1 What is Diffraction?

Diffraction is the bending of light around obstacles and through apertures, with the wavefront being **distorted** in the process. It is the failure of light to travel in straight lines when encountering obstacles comparable in size to its wavelength.

**Fresnel vs Fraunhofer diffraction:**

| Property | Fresnel | Fraunhofer |
|----------|---------|------------|
| Source distance | Finite | Infinite (parallel rays) |
| Screen distance | Finite | Infinite (or at focal plane of lens) |
| Wavefront | Spherical/cylindrical | Plane |
| Mathematical treatment | Complex integrals | Simpler Fourier analysis |
| Obstacle size | ~ $\sqrt{\lambda d}$ | Much larger than $\lambda$ |

### 5.2 Single Slit Diffraction (Fraunhofer)

**Setup:** Parallel (collimated) monochromatic light passes through a slit of width $a$. A converging lens of focal length $f$ focuses the diffracted light on a screen at its focal plane.

```
    Parallel light
    |||||||||  →  |← a →|  →  Lens  →  Screen (at focal plane)
    |||||||||     Slit
```

**Analysis by division of wavefront:**

Consider the slit as divided into $N$ equal strips, each of width $a/N$. The path difference between rays from adjacent strips at angle $\theta$ is $\Delta = (a/N)\sin\theta$.

For the **first minimum:** Each strip's contribution cancels with an adjacent strip. This happens when the path difference between the top and bottom of the slit equals $\lambda$:

$$a\sin\theta = \lambda$$

**General minima:**

$$\boxed{a\sin\theta = n\lambda} \quad n = \pm 1, \pm 2, \pm 3, \ldots$$

**Note:** $n = 0$ is NOT a minimum — it's the central maximum.

### 5.3 Single Slit Intensity — Complete Derivation

Consider the slit divided into infinitesimal strips. At angle $\theta$, the path difference between rays from position $x$ (measured from one edge) and the edge is $(x/a) \cdot a\sin\theta = x\sin\theta$.

The total amplitude is the integral:

$$E = E_0 \int_0^1 \cos(\beta u) \, du$$

where $\beta = \frac{\pi a \sin\theta}{\lambda}$ and $u = x/a$.

Actually, more carefully, if each infinitesimal element contributes amplitude $dE_0$ with phase $\phi = \frac{2\pi}{\lambda} x \sin\theta$:

$$E = \int_0^a \frac{E_0}{a} e^{i(2\pi/\lambda)x\sin\theta} dx$$

Let $\alpha = \frac{\pi a \sin\theta}{\lambda}$:

$$E = \frac{E_0}{a} \cdot \frac{a}{i(2\alpha)} \left[e^{2i\alpha} - 1\right] = E_0 \cdot \frac{e^{i\alpha}}{i\alpha} \cdot \frac{e^{i\alpha} - e^{-i\alpha}}{2i/2i}$$

Wait, let me redo this more carefully.

Each point in the slit contributes a wavelet. If the slit extends from $x = 0$ to $x = a$, and the field from element $dx$ at angle $\theta$ has phase $kx\sin\theta$ (where $k = 2\pi/\lambda$):

$$E(\theta) \propto \int_0^a e^{ikx\sin\theta} dx = \frac{e^{ika\sin\theta} - 1}{ik\sin\theta} = a \cdot \frac{e^{i\alpha} - 1}{2i\alpha}$$

where $\alpha = \frac{ka\sin\theta}{2} = \frac{\pi a \sin\theta}{\lambda}$.

$$E(\theta) \propto a \cdot \frac{e^{i\alpha}}{i\alpha} \cdot \frac{e^{i\alpha} - e^{-i\alpha}}{2i} \cdot \frac{1}{1} = a \cdot e^{i\alpha/2} \cdot \frac{\sin\alpha}{\alpha}$$

Hmm, let me just use the standard result:

$$E(\theta) = E_0 \cdot \frac{\sin\alpha}{\alpha}$$

where $E_0$ is the amplitude at the center ($\theta = 0$), and $\alpha = \frac{\pi a \sin\theta}{\lambda}$.

**Intensity:**

$$\boxed{I(\theta) = I_0 \left(\frac{\sin\alpha}{\alpha}\right)^2}$$

where $I_0$ is the intensity at the center and $\alpha = \frac{\pi a \sin\theta}{\lambda}$.

**Properties of $\text{sinc}^2$ function:**

- At $\alpha = 0$: $(\sin\alpha/\alpha)^2 \to 1$ → Central maximum
- At $\alpha = n\pi$ ($n = \pm 1, \pm 2, \ldots$): $\sin\alpha = 0$ → Minima → $a\sin\theta = n\lambda$ ✓
- First secondary maximum near $\alpha \approx 1.43\pi$: $I_1 \approx 0.0472 I_0$ (about 4.7% of central)
- Second secondary maximum near $\alpha \approx 2.46\pi$: $I_2 \approx 0.0165 I_0$ (about 1.7% of central)

### 5.4 Width of Central Maximum

The central maximum extends from the first minimum on one side to the first minimum on the other side.

First minimum: $a\sin\theta_1 = \lambda$ → $\sin\theta_1 = \lambda/a$ → $\theta_1 \approx \lambda/a$ (small angle)

**Angular width of central maximum:**

$$\boxed{2\theta_1 = \frac{2\lambda}{a}}$$

**Linear width on screen (distance from slit to screen = $D$, or focal length $f$):**

$$\boxed{W = \frac{2\lambda D}{a}}$$

**Key point:** The central maximum is **twice as wide** as any other maximum (other maxima have width $\lambda D/a$).

### 5.5 Comparison: Diffraction vs Interference

| Feature | Interference (YDSE) | Diffraction (Single Slit) |
|---------|--------------------|-----------------------------|
| Source | Two coherent sources | One extended source (wavefront) |
| Number of waves | Two | Infinite (continuous) |
| Fringe spacing | Equal ($\beta = \lambda D/d$) | Unequal |
| Intensity of maxima | All equal ($4I_0$) | Rapidly decreasing |
| Central maximum | Same as others | Twice as wide, much brighter |
| Condition for max | $d\sin\theta = n\lambda$ | $a\sin\theta = (2n+1)\lambda/2$ (approx) |
| Condition for min | $d\sin\theta = (2n-1)\lambda/2$ | $a\sin\theta = n\lambda$ |
| Pattern | Equally spaced, equal intensity | Unequally spaced, decreasing intensity |

### 5.6 Double Slit Diffraction

Both interference and diffraction occur simultaneously when light passes through two slits, each of width $a$, separated by center-to-center distance $d$.

$$I = 4I_0 \cos^2\!\left(\frac{\pi d \sin\theta}{\lambda}\right) \cdot \left(\frac{\sin\alpha}{\alpha}\right)^2$$

where $\alpha = \frac{\pi a \sin\theta}{\lambda}$.

The first factor is the YDSE interference pattern; the second is the single-slit diffraction envelope.

**Missing orders:** When a diffraction minimum coincides with an interference maximum, that fringe disappears. This happens when:

$$\frac{d}{a} = m \quad \text{(integer)}$$

The $m$th interference maximum is suppressed by the diffraction minimum. For example, if $d = 3a$, orders $n = 3, 6, 9, \ldots$ are missing.

---

## 6. Diffraction Grating

### 6.1 Structure and Theory

A diffraction grating has a large number of equally spaced, parallel slits (or lines). If there are $N$ slits per unit length, the slit spacing (grating element) is:

$$d = \frac{1}{N}$$

**Example:** 5000 lines/cm → $d = 1/5000$ cm $= 2 \times 10^{-4}$ cm $= 2000$ nm.

### 6.2 Principal Maxima

For $N$ slits, the interference condition for principal maxima:

$$\boxed{d\sin\theta = n\lambda} \quad n = 0, \pm 1, \pm 2, \ldots$$

**Why is the grating equation the same as YDSE?** The path difference between adjacent slits is $d\sin\theta$. For constructive interference: $d\sin\theta = n\lambda$. This condition is the same regardless of the number of slits — but having many slits makes the maxima much sharper.

### 6.3 Secondary Maxima and Minima

Between two adjacent principal maxima:

- **$N - 1$ minima** (zero intensity points)
- **$N - 2$ secondary maxima** (small but nonzero intensity)

As $N$ increases, the secondary maxima become negligible and the principal maxima become very sharp spikes.

**Angular width of a principal maximum:**

$$\Delta\theta = \frac{\lambda}{Nd\cos\theta} = \frac{\lambda}{N \cdot d \cos\theta}$$

This is inversely proportional to $N$: more slits → sharper peaks.

### 6.4 Grating Equation for Oblique Incidence

For light incident at angle $\theta_i$ on the grating:

$$d(\sin\theta_i + \sin\theta_d) = n\lambda$$

where $\theta_d$ is the diffraction angle (both angles measured from the normal, same side of normal if both sines have the same sign).

### 6.5 Number of Visible Orders

The maximum order visible is limited by $\sin\theta \leq 1$:

$$n_{max} = \left\lfloor\frac{d}{\lambda}\right\rfloor$$

**Example:** $d = 2000$ nm, $\lambda = 500$ nm → $n_{max} = \lfloor 2000/500 \rfloor = 4$.

So orders $n = 0, \pm 1, \pm 2, \pm 3, \pm 4$ are visible (9 principal maxima total).

### 6.6 Blazed Grating

A blazed grating has its grooves cut at a specific angle (blaze angle $\theta_B$) to concentrate most of the diffracted energy into a particular order. The blaze condition:

$$2d\sin\theta_B\cos(\theta_i - \theta_B) = n\lambda$$

---

## 7. Resolving Power & Rayleigh Criterion

### 7.1 Rayleigh Criterion

Two point sources are **just resolvable** when the central maximum of the diffraction pattern of one source falls exactly on the first minimum of the diffraction pattern of the other.

**For a circular aperture (telescope/microscope):**

$$\theta_{min} = 1.22\frac{\lambda}{D}$$

where $D$ is the aperture diameter.

**For a slit (spectrometer):**

$$\theta_{min} = \frac{\lambda}{a}$$

### 7.2 Resolving Power of a Grating

The **resolving power** (or chromatic resolving power) of a grating:

$$\boxed{R = \frac{\lambda}{\Delta\lambda} = nN}$$

where:
- $\lambda$ is the mean wavelength
- $\Delta\lambda$ is the smallest wavelength difference that can be resolved
- $n$ is the diffraction order
- $N$ is the total number of slits illuminated

**Derivation:** Two wavelengths $\lambda$ and $\lambda + \Delta\lambda$ produce maxima at slightly different angles in order $n$:

$$d\sin\theta = n\lambda$$
$$d\sin(\theta + \Delta\theta) = n(\lambda + \Delta\lambda)$$

By the Rayleigh criterion, the first minimum of the $\lambda$ pattern falls at:

$$d\sin(\theta + \delta\theta) = n\lambda + \lambda$$

where $\delta\theta$ is the angular distance to the first minimum. For the grating, this corresponds to the path difference being $\lambda$ less — which happens at a specific angular offset.

The minimum resolvable wavelength difference is: $\Delta\lambda = \lambda/(nN)$, giving $R = \lambda/\Delta\lambda = nN$.

**Key insight:** Higher orders and more slits give better resolution.

### 7.3 Resolving Power of a Prism

$$R = \frac{\lambda}{\Delta\lambda} = b\frac{dn}{d\lambda}$$

where $b$ is the base length of the prism and $dn/d\lambda$ is the dispersion of the prism material.

### 7.4 Resolving Power of a Telescope

$$R = \frac{D}{1.22\lambda}$$

where $D$ is the aperture diameter.

### 7.5 Numerical Aperture and Microscope Resolution

**Numerical Aperture:** $NA = n\sin\alpha$ where $n$ is the refractive index of the medium and $\alpha$ is the half-angle of the cone of light collected.

**Minimum resolvable distance:**

$$d_{min} = \frac{1.22\lambda}{2 \cdot NA} = \frac{0.61\lambda}{NA}$$

---

## 8. Polarization of Light

### 8.1 What is Polarization?

Light is a **transverse** wave — the electric field oscillates perpendicular to the direction of propagation. Polarization restricts this oscillation to a single plane or pattern.

**Unpolarized light:** E-field oscillates randomly in all planes perpendicular to propagation. Time-averaged intensity is the same in all directions.

**Linearly polarized light:** E-field oscillates in one fixed plane.

**Circularly polarized light:** E-field rotates uniformly in a circle perpendicular to propagation.

**Elliptically polarized light:** E-field traces an ellipse.

### 8.2 Unpolarized Light → Polarizer

When unpolarized light of intensity $I_0$ passes through an ideal linear polarizer:

$$\boxed{I = \frac{I_0}{2}}$$

This is **not** Malus' law — it's a consequence of averaging over all orientations. The unpolarized light can be thought of as an equal mixture of two orthogonal polarization states, each carrying $I_0/2$. The polarizer transmits only one component.

### 8.3 Malus' Law

When **linearly polarized** light of intensity $I_0$ passes through an analyzer (second polarizer) whose transmission axis makes angle $\theta$ with the polarization direction:

$$\boxed{I = I_0 \cos^2\theta}$$

**Derivation:** The electric field $E_0$ (polarized along one direction) is projected onto the analyzer axis: $E = E_0 \cos\theta$. Since $I \propto E^2$:

$$I = I_0 \cos^2\theta$$

**Special cases:**

| Angle $\theta$ | $\cos^2\theta$ | Intensity $I$ |
|-----------------|-----------------|----------------|
| $0°$ | 1 | $I_0$ (maximum) |
| $30°$ | 3/4 | $3I_0/4$ |
| $45°$ | 1/2 | $I_0/2$ |
| $60°$ | 1/4 | $I_0/4$ |
| $90°$ | 0 | 0 (crossed polarizers) |

### 8.4 Multiple Polarizers

**Three polarizers (P1, P2, P3):**

If P1 and P3 are crossed ($90°$ to each other), no light passes through P1 + P3 alone. But inserting P2 at $45°$ between them allows light through:

1. After P1: $I_1 = I_0/2$, polarized along P1 axis
2. After P2 (at $45°$ to P1): $I_2 = I_1 \cos^2(45°) = (I_0/2)(1/2) = I_0/4$, polarized along P2 axis
3. After P3 (at $45°$ to P2, hence $90°$ to P1): $I_3 = I_2 \cos^2(45°) = (I_0/4)(1/2) = I_0/8$

**Result:** $I_3 = I_0/8$

**General formula for $n$ polarizers each at angle $\theta$ to the previous:**

$$I_n = \frac{I_0}{2} \cos^{2(n-1)}\theta$$

### 8.5 Brewster's Law

At the **polarizing angle** (Brewster angle) $\theta_B$, reflected light is completely linearly polarized perpendicular to the plane of incidence.

$$\boxed{\tan\theta_B = \mu = \frac{n_2}{n_1}}$$

**Derivation:** At Brewster's angle, the reflected ray and refracted ray are perpendicular ($\theta_B + r = 90°$). From Snell's law:

$$n_1 \sin\theta_B = n_2 \sin r = n_2 \sin(90° - \theta_B) = n_2 \cos\theta_B$$

$$\tan\theta_B = \frac{n_2}{n_1} = \mu$$

**Properties at Brewster's angle:**
- Reflected light is 100% polarized perpendicular to the plane of incidence
- Reflected and refracted rays are perpendicular to each other
- The refracted ray is partially polarized in the plane of incidence
- There is no reflected light polarized in the plane of incidence

**Numerical example:** For glass ($\mu = 1.5$): $\theta_B = \arctan(1.5) = 56.3°$

### 8.6 Double Refraction (Birefringence)

Some crystals (calcite, quartz, rutile) are birefringent — they have two different refractive indices depending on the polarization direction of the light.

- **Ordinary ray (o-ray):** Obeys Snell's law normally. Refractive index $n_o$.
- **Extraordinary ray (e-ray):** Does not obey Snell's law in general. Refractive index $n_e$ varies with direction.

**Optic axis:** The direction in which both rays travel at the same speed ($n_o = n_e$). This is NOT a unique line but a direction in the crystal.

**Negative crystal:** $n_e < n_o$ (e.g., calcite). The extraordinary ray travels faster.

**Positive crystal:** $n_e > n_o$ (e.g., quartz). The ordinary ray travels faster.

### 8.7 Quarter-Wave and Half-Wave Plates

**Quarter-wave plate (QWP):** Introduces a phase difference of $\pi/2$ (quarter wavelength) between two orthogonal polarization components.

- **Application:** Converts linearly polarized light to circularly polarized (when input polarization is at $45°$ to the optic axis)
- **Thickness:** $t = \frac{\lambda}{4|n_e - n_o|}$

**Half-wave plate (HWP):** Introduces a phase difference of $\pi$ (half wavelength) between two orthogonal components.

- **Application:** Rotates the plane of polarization by $2\theta$ (where $\theta$ is the angle between the input polarization and the optic axis)
- **Thickness:** $t = \frac{\lambda}{2|n_e - n_o|}$

### 8.8 Optical Activity

Certain materials (sugar solution, quartz) rotate the plane of polarization of linearly polarized light passing through them. The rotation angle:

$$\theta = \alpha \cdot l \cdot C$$

where $\alpha$ is the specific rotation, $l$ is the path length, and $C$ is the concentration (for solutions).

---

## 9. Advanced Topics

### 9.1 Fabry-Pérot Interferometer (Etalon)

A Fabry-Pérot etalon consists of two parallel partially reflecting mirrors separated by distance $t$.

**Multiple beam interference:** Unlike YDSE (two beams), the Fabry-Pérot uses many successive reflections.

**Transmission maxima (constructive):**

$$2\mu t \cos\theta = n\lambda$$

**Airy function for transmitted intensity:**

$$I_T = \frac{I_{max}}{1 + F\sin^2(\delta/2)}$$

where $\delta = \frac{4\pi\mu t\cos\theta}{\lambda}$ and $F = \frac{4R}{(1-R)^2}$ is the coefficient of finesse.

**Finesse:**

$$\boxed{\mathcal{F} = \frac{\pi\sqrt{R}}{1-R}}$$

where $R$ is the reflectivity of each mirror.

**Free spectral range (FSR):**

$$\boxed{\Delta\lambda_{FSR} = \frac{\lambda^2}{2\mu t}}$$

or in frequency: $\Delta\nu_{FSR} = c/(2\mu t)$.

**Key advantage:** Very high resolving power. For a Fabry-Pérot etalon:

$$R_{FP} = \frac{\lambda}{\Delta\lambda} = n \cdot \mathcal{F}$$

### 9.2 Michelson Interferometer

Splits a beam into two perpendicular paths using a beam splitter, reflects each beam back, and recombines them. Moving one mirror changes the path difference.

```
                    Mirror M1 (movable)
                         |
                         |
    Source →  Beam Splitter → Mirror M2 (fixed)
                         |
                    Detector
```

**Fringe shift for mirror displacement $d$:**

$$\boxed{n = \frac{2d}{\lambda}}$$

The mirror moves $d$, but the round-trip path changes by $2d$.

**Applications:**
- Measuring wavelength of light: $\lambda = 2d/n$
- Measuring refractive index: insert thin film, count fringes shifted
- Measuring coherence length
- LIGO gravitational wave detector is a giant Michelson interferometer

### 9.3 Coherence Length and Time

**Coherence length:** $l_c = c \cdot \tau_c$

| Source | Coherence length |
|--------|-----------------|
| Sodium lamp | ~0.6 mm |
| Mercury lamp | ~0.03 mm |
| Tungsten lamp | ~0.001 mm |
| Laser (good quality) | meters to km |

**Condition for observable fringes:** Path difference $\Delta < l_c$

If the path difference exceeds the coherence length, the fringes disappear (the waves from the two paths are no longer correlated).

### 9.4 Interference Filters

A thin film structure designed to transmit a narrow band of wavelengths. Uses multiple thin film layers to create constructive interference for the desired wavelength and destructive for others.

**Peak wavelength:** $\lambda_0 = 2\mu t$ (for a single layer at normal incidence)

**Bandwidth:** Depends on the number of layers and their reflectivities.

---

## 10. ASCII Flowcharts

### 10.1 Phase Change Counting Flowchart

Use this flowchart for every thin-film and reflection problem. Count the total number of $\pi$ phase changes (equivalent to $\lambda/2$ path differences) in the two interfering rays.

```
╔══════════════════════════════════════════════════════════════════╗
║              PHASE CHANGE COUNTING FLOWCHART                    ║
╚══════════════════════════════════════════════════════════════════╝

  Start: Identify the TWO interfering rays
  ┌─────────────────────────────────────┐
  │  RAY 1: Reflected at TOP surface    │
  │  RAY 2: Reflected at BOTTOM surface │
  └──────────────┬──────────────────────┘
                 │
                 ▼
  ┌──────────────────────────────────────┐
  │  RAY 1: What is the reflection?      │
  │  Rare→Dense  or  Dense→Rare ?        │
  └───────┬──────────────┬───────────────┘
          │              │
     Rare→Dense     Dense→Rare
          │              │
          ▼              ▼
   ┌────────────┐  ┌──────────────┐
   │ Phase       │  │ No phase     │
   │ change = π  │  │ change = 0   │
   │ (count=1)   │  │ (count=0)    │
   └──────┬─────┘  └──────┬───────┘
          │               │
          ▼               ▼
  ┌──────────────────────────────────────┐
  │  RAY 2: What is the reflection?      │
  │  Rare→Dense  or  Dense→Rare ?        │
  └───────┬──────────────┬───────────────┘
          │              │
     Rare→Dense     Dense→Rare
          │              │
          ▼              ▼
   ┌────────────┐  ┌──────────────┐
   │ Phase       │  │ No phase     │
   │ change = π  │  │ change = 0   │
   │ (count=+1)  │  │ (count=+0)   │
   └──────┬─────┘  └──────┬───────┘
          │               │
          ▼               ▼
  ┌──────────────────────────────────────┐
  │     TOTAL PHASE CHANGES = COUNT      │
  └───────┬──────────────┬───────────────┘
          │              │
    COUNT = 1       COUNT = 0 or 2
          │              │
          ▼              ▼
  ┌────────────────┐  ┌────────────────────┐
  │ USE THESE       │  │ USE THESE           │
  │ CONDITIONS:     │  │ CONDITIONS:         │
  │                 │  │                     │
  │ Bright:         │  │ Bright:             │
  │ 2μt = (2n-1)λ/2│  │ 2μt = nλ            │
  │                 │  │                     │
  │ Dark:           │  │ Dark:               │
  │ 2μt = nλ        │  │ 2μt = (2n-1)λ/2     │
  └────────────────┘  └────────────────────┘

  EXAMPLES:
  ┌─────────────────────────────────────────────┐
  │ Soap film in air:                            │
  │   Ray1: air→film (Rare→Dense) → π change    │
  │   Ray2: film→air (Dense→Rare) → no change   │
  │   Total = 1 phase change                    │
  │                                              │
  │ Glass plate (coated) in air:                 │
  │   Ray1: air→coating (Rare→Dense) → π        │
  │   Ray2: coating→glass (Dense→Denser) → π    │
  │   Total = 2 phase changes                   │
  │                                              │
  │ Air wedge between glass plates:              │
  │   Ray1: glass→air (Dense→Rare) → no change  │
  │   Ray2: air→glass (Rare→Dense) → π change   │
  │   Total = 1 phase change                    │
  └─────────────────────────────────────────────┘
```

### 10.2 Which Interference Formula to Use?

```
╔══════════════════════════════════════════════════════════════════════╗
║          WHICH INTERFERENCE FORMULA SHOULD I USE?                   ║
╚══════════════════════════════════════════════════════════════════════╝

  What is the physical setup?
  ┌──────────────────────┐
  │   Identify the setup  │
  └──────┬───────────────┘
         │
    ┌────┴────┬──────────────┬───────────────┬──────────────┐
    │         │              │               │              │
    ▼         ▼              ▼               ▼              ▼
  ┌──────┐ ┌────────┐ ┌───────────┐ ┌───────────┐ ┌──────────┐
  │ YDSE │ │THIN    │ │ NEWTON'S  │ │ SINGLE    │ │ GRATING  │
  │      │ │FILM    │ │ RINGS     │ │ SLIT      │ │          │
  └──┬───┘ └───┬────┘ └─────┬─────┘ └─────┬─────┘ └────┬─────┘
     │         │            │              │             │
     ▼         ▼            ▼              ▼             ▼

  ┌─────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌───────────┐
  │Count     │ │Count     │ │Count     │ │This is   │ │Same as    │
  │phase     │ │phase     │ │phase     │ │diffraction│ │YDSE with  │
  │changes   │ │changes   │ │changes   │ │not       │ │N slits:   │
  │from      │ │from      │ │from      │ │interfer- │ │           │
  │source    │ │reflec-   │ │reflec-   │ │ence.    │ │d sinθ     │
  │displace- │ │tions at  │ │tions:    │ │          │ │  = nλ     │
  │ment,     │ │top and   │ │1 total   │ │Minima:  │ │           │
  │sheets,   │ │bottom    │ │          │ │a sinθ   │ │NOT d sinθ │
  │etc.      │ │surfaces  │ │Dark at   │ │  = nλ   │ │  = nλ/2   │
  │          │ │          │ │center    │ │          │ │           │
  │Fringe    │ │          │ │          │ │Central  │ │Max orders:│
  │shift:    │ │Then use  │ │Dark:     │ │max is   │ │n_max =    │
  │Δy=       │ │table     │ │r=√(nλR) │ │twice as │ │⌊d/λ⌋     │
  │(μ-1)tD/d │ │below     │ │Bright:   │ │wide     │ │           │
  │          │ │          │ │r=√((n+½) │ │          │ │R = nN     │
  │Fringe    │ │Bright:   │ │  λR)    │ │Central  │ │           │
  │width:    │ │2μt cos r │ │          │ │width:   │ │           │
  │β=λD/d    │ │= (2n-1)λ/│ │          │ │W=2λD/a  │ │           │
  │          │ │  2       │ │          │ │          │ │           │
  │          │ │(1 phase) │ │          │ │          │ │           │
  │          │ │          │ │          │ │          │ │           │
  │          │ │Dark:     │ │          │ │          │ │           │
  │          │ │2μt cos r │ │          │ │          │ │           │
  │          │ │= nλ      │ │          │ │          │ │           │
  │          │ │(1 phase) │ │          │ │          │ │           │
  └─────────┘ └──────────┘ └──────────┘ └──────────┘ └───────────┘

  ┌─────────────────────────────────────────────────────────────────┐
  │                    QUICK DECISION TABLE                          │
  ├─────────────────────────────────────────────────────────────────┤
  │ Setup              │ Bright condition         │ Dark condition  │
  ├────────────────────┼──────────────────────────┼─────────────────┤
  │ YDSE               │ Δ = nλ                   │ Δ = (2n-1)λ/2  │
  │                    │ → y_n = nλD/d            │ → y_n=(2n-1)λD/ │
  │                    │                          │        2d       │
  ├────────────────────┼──────────────────────────┼─────────────────┤
  │ Thin film (1 phase │ 2μt cos r = (2n-1)λ/2   │ 2μt cos r = nλ │
  │ change)            │                          │                 │
  ├────────────────────┼──────────────────────────┼─────────────────┤
  │ Thin film (0 or 2  │ 2μt cos r = nλ           │ 2μt cos r =    │
  │ phase changes)     │                          │ (2n-1)λ/2      │
  ├────────────────────┼──────────────────────────┼─────────────────┤
  │ Newton's rings     │ r_n = √((n+½)λR)        │ r_n = √(nλR)  │
  │ (reflected, 1      │                          │                 │
  │ phase change)      │                          │                 │
  ├────────────────────┼──────────────────────────┼─────────────────┤
  │ Single slit        │ a sinθ = (2n+1)λ/2      │ a sinθ = nλ    │
  │                    │ (approx, weaker)         │ (exact)         │
  ├────────────────────┼──────────────────────────┼─────────────────┤
  │ Grating            │ d sinθ = nλ              │ N/A (use minima │
  │                    │ (principal max)          │ between maxima) │
  └────────────────────┴──────────────────────────┴─────────────────┘
```

### 10.3 Diffraction vs Interference Decision Flowchart

```
╔══════════════════════════════════════════════════════════════════╗
║           DIFFRACTION vs INTERFERENCE DECISION FLOWCHART        ║
╚══════════════════════════════════════════════════════════════════╝

  Question: How many slits/openings are there?
  ┌────────────────────────────────────────┐
  │                                        │
  └───────┬────────────────┬───────────────┘
          │                │
      2 slits          ≥ 3 slits (grating)
          │                │
          ▼                ▼
  ┌──────────────┐   ┌──────────────────┐
  │ YDSE         │   │ GRATING          │
  │ INTERFERENCE │   │ (Use grating eq.)│
  │              │   │ d sinθ = nλ      │
  │ β = λD/d    │   │                  │
  │              │   │ R = nN           │
  │ Equal        │   │                  │
  │ spacing      │   │ Very sharp       │
  │ Equal        │   │ principal maxima │
  │ intensity    │   │                  │
  └──────────────┘   └──────────────────┘

  Question: Is there ONE slit of width a?
  ┌────────────────────────────────────────┐
  │                                        │
  └───────┬────────────────────────────────┘
          │
          ▼
  ┌──────────────────────────────────────┐
  │ SINGLE SLIT DIFFRACTION              │
  │                                      │
  │ Minima: a sinθ = nλ                  │
  │ Central max width = 2λD/a           │
  │                                      │
  │ Central max is TWICE as wide         │
  │ Secondary maxima are much weaker     │
  │ Pattern is NOT equally spaced        │
  └──────────────────────────────────────┘

  Question: Are there TWO slits, each of width a, separated by d?
  ┌────────────────────────────────────────────────────────┐
  │                                                        │
  └───────┬────────────────────────────────────────────────┘
          │
          ▼
  ┌──────────────────────────────────────────────────────────┐
  │  DOUBLE SLIT DIFFRACTION + INTERFERENCE                  │
  │                                                          │
  │  I = 4I₀ cos²(πd sinθ/λ) × (sin α/α)²                 │
  │                                                          │
  │  INTERFERENCE modulates DIFFRACTION envelope             │
  │                                                          │
  │  Missing orders when d/a = integer:                      │
  │  The n-th interference max vanishes under the            │
  │  diffraction minimum.                                    │
  └──────────────────────────────────────────────────────────┘

  ┌──────────────────────────────────────────────────────────┐
  │              KEY DISTINCTIONS                             │
  ├──────────────────────────────────────────────────────────┤
  │                                                          │
  │  INTERFERENCE:     DIFFRACTION:                          │
  │  ─────────────     ────────────                          │
  │  • 2 coherent      • 1 extended source                   │
  │    sources         • (Huygens wavelets)                  │
  │  • Equal spacing   • Unequal spacing                     │
  │  • Equal intensity • Decreasing intensity                │
  │  • Central max     • Central max is TWICE                │
  │    same as others    as wide                              │
  │                                                          │
  │  IN REALITY: Both always occur together!                 │
  │  Double slit = interference + diffraction                │
  │  The slit width a determines the diffraction envelope.   │
  │  The slit separation d determines the interference fringes│
  │                                                          │
  └──────────────────────────────────────────────────────────┘
```

---

## 11. Common Mistakes

### 11.1 Phase Change Errors

1. **Forgetting phase change on reflection** — the single most common error. Always check: is the reflection at a denser medium? If yes, add $\pi$ phase change ($\lambda/2$ path difference).

2. **Applying phase change to transmitted light incorrectly.** Remember: reflected and transmitted patterns are complementary. If you count phase changes for reflection, the transmitted pattern has the opposite conditions.

3. **Assuming both reflections have phase changes** when the film has different media on each side. Always trace each ray individually.

### 11.2 YDSE Mistakes

4. **Confusing the slit width $a$ with the slit separation $d$.** In YDSE, $d$ is the center-to-center distance between slits. In single-slit diffraction, $a$ is the width of the single slit. In double-slit diffraction, both $a$ (slit width) and $d$ (slit separation) appear.

5. **Using $y = n\lambda D/d$ for dark fringes.** The correct formula for dark fringes is $y = (2n-1)\lambda D/(2d)$.

6. **Forgetting that fringe width changes in liquid.** $\beta_{liquid} = \beta_{air}/\mu$.

7. **Wrong sign for fringe shift direction.** The pattern shifts TOWARD the slit with the glass sheet (because the sheet adds optical path, so the path-equalizing point moves toward that slit).

### 11.3 Thin Film Mistakes

8. **Using $\cos r$ when the problem says normal incidence.** At normal incidence, $r = 0$, so $\cos r = 1$. Don't leave $\cos r$ in the answer.

9. **Confusing reflected and transmitted conditions.** They are complementary. If you get the reflected condition wrong, you'll get the transmitted one wrong too (but sometimes in the right direction by accident).

10. **Using the wrong value of $n$.** For minimum thickness, use $n = 1$ for constructive with 1 phase change, and $n = 0$ for destructive with 1 phase change (but $n = 0$ gives zero thickness, so use the next meaningful value).

### 11.4 Diffraction Mistakes

11. **Confusing interference maxima conditions with diffraction minima.** For single slit: MINIMA at $a\sin\theta = n\lambda$. For YDSE: MAXIMA at $d\sin\theta = n\lambda$. The formulas look the same but apply to opposite conditions!

12. **Forgetting that the central maximum in diffraction is twice as wide.** Students often write the width of the central maximum as $\lambda D/a$ instead of $2\lambda D/a$.

13. **Assuming secondary maxima in diffraction are at $\theta = (2n+1)\lambda/(2a)$.** This is only approximately true. The exact positions are solutions of $\tan\alpha = \alpha$, which are slightly shifted.

### 11.5 Grating Mistakes

14. **Using $N$ (slits per unit length) instead of total number of slits $N_{total}$ in resolving power.** $R = nN_{total}$, where $N_{total}$ is the total number of illuminated slits, not the lines per unit length.

15. **Not checking that $n_{max} = \lfloor d/\lambda \rfloor$.** Always verify that the order you're computing actually exists.

### 11.6 Polarization Mistakes

16. **Applying Malus' law to unpolarized light.** For unpolarized → polarizer: $I = I_0/2$. Malus' law ($I = I_0\cos^2\theta$) only applies when the INPUT is already polarized.

17. **Forgetting the factor of $1/2$ after the first polarizer.** When unpolarized light passes through the first polarizer, intensity becomes $I_0/2$, not $I_0$.

18. **Using Brewster's angle for total internal reflection.** Brewster's angle ($\tan\theta_B = \mu$) is for reflection at the surface of a denser medium from outside. Total internal reflection occurs when going from dense to rare at angle $>\theta_c$ where $\sin\theta_c = 1/\mu$.

### 11.7 General Mistakes

19. **Units:** Always convert to SI units (meters, not mm or cm). Wavelengths are in nanometers: $1$ nm $= 10^{-9}$ m.

20. **Small angle approximation:** $\sin\theta \approx \theta \approx \tan\theta$ is valid only for $\theta < 10°$ approximately. Check the problem for large angles.

---

## 12. Worked Numerical Examples

### Example 1: YDSE with Glass Sheet — Fringe Shift

**Problem:** In a Young's double slit experiment, the slit separation is $d = 1.0$ mm, the screen distance is $D = 1.0$ m, and the wavelength is $\lambda = 589$ nm. A glass sheet of refractive index $\mu = 1.50$ and thickness $t = 0.010$ mm is placed in front of one of the slits. Find:
(a) the fringe shift
(b) the new position of the central maximum

**Solution:**

**(a) Fringe shift:**

The extra optical path introduced by the glass sheet:

$$\Delta_{optical} = (\mu - 1)t = (1.50 - 1)(0.010 \times 10^{-3}) = 0.5 \times 10^{-5} \text{ m} = 5.0 \times 10^{-6} \text{ m}$$

The fringe shift:

$$\Delta y = \frac{(\mu - 1)tD}{d} = \frac{5.0 \times 10^{-6} \times 1.0}{1.0 \times 10^{-3}} = 5.0 \times 10^{-3} \text{ m} = \boxed{5.0 \text{ mm}}$$

**(b) Position of central maximum:**

The central maximum shifts toward the slit with the glass sheet. If the sheet is in front of $S_1$ (above the axis), the central maximum shifts upward (toward $S_1$):

$$y_0 = +\Delta y = +5.0 \text{ mm above the original center}$$

The shift is toward the slit with the sheet because that slit's light is "delayed" — the pattern moves so that the geometrical path difference compensates for the optical path added by the sheet.

---

### Example 2: YDSE with Source Displacement

**Problem:** In a YDSE setup, $d = 0.5$ mm, $D = 1.0$ m (screen distance), $D' = 0.5$ m (source-to-slits distance), and $\lambda = 600$ nm. The source is displaced upward by $x = 0.20$ mm from the central axis. Find the position of the central maximum on the screen.

**Solution:**

The extra path difference from the displaced source to the two slits:

$$\Delta_{source} = \frac{xd}{D'} = \frac{(0.20 \times 10^{-3})(0.5 \times 10^{-3})}{0.5} = 2.0 \times 10^{-7} \text{ m}$$

The central maximum shifts to compensate:

$$y_0 = -\frac{xD}{D'} = -\frac{(0.20 \times 10^{-3})(1.0)}{0.5} = -4.0 \times 10^{-4} \text{ m} = \boxed{-0.40 \text{ mm}}$$

The negative sign indicates the central maximum shifts **downward** (opposite to the source displacement).

**Verification:** The fringe width is $\beta = \lambda D/d = (600 \times 10^{-9})(1.0)/(0.5 \times 10^{-3}) = 1.2$ mm. The shift is 0.40 mm, which is less than one fringe width. This makes physical sense.

---

### Example 3: Thin Film — Constructive Interference

**Problem:** What is the minimum thickness of a soap film ($\mu = 1.33$) that appears bright in reflected light when illuminated with sodium light ($\lambda = 589$ nm) at normal incidence?

**Solution:**

**Step 1: Count phase changes.**
- Ray 1 (reflected at top): air → soap ($1 < 1.33$): Rare → Dense → **Phase change of $\pi$**
- Ray 2 (reflected at bottom): soap → air ($1.33 > 1$): Dense → Rare → **No phase change**
- Total: **1 phase change**

**Step 2: Apply constructive condition for 1 phase change:**

$$2\mu t = \left(n - \frac{1}{2}\right)\lambda$$

For **minimum** thickness, use $n = 1$:

$$t_{min} = \frac{\lambda}{4\mu} = \frac{589 \times 10^{-9}}{4 \times 1.33} = \frac{589 \times 10^{-9}}{5.32}$$

$$t_{min} = 110.7 \times 10^{-9} \text{ m} = \boxed{111 \text{ nm}}$$

**Check:** $2\mu t = 2(1.33)(111 \times 10^{-9}) = 295 \times 10^{-9}$ m $= \lambda/2$. This matches $(2n-1)\lambda/2$ for $n=1$. ✓

---

### Example 4: Newton's Rings — Radius Calculation

**Problem:** In a Newton's rings experiment, the radius of curvature of the plano-convex lens is $R = 5.0$ m and the wavelength is $\lambda = 589$ nm. Find:
(a) the radius of the 5th dark ring in reflected light
(b) the radius of the 5th bright ring in reflected light
(c) the spacing between the 5th and 6th dark rings

**Solution:**

**(a) Radius of 5th dark ring (reflected light):**

For dark rings in reflected light (1 phase change):

$$r_n = \sqrt{n\lambda R}$$

$$r_5 = \sqrt{5 \times 589 \times 10^{-9} \times 5.0} = \sqrt{1.4725 \times 10^{-5}}$$

$$r_5 = 3.84 \times 10^{-3} \text{ m} = \boxed{3.84 \text{ mm}}$$

**(b) Radius of 5th bright ring (reflected light):**

$$r_n = \sqrt{\left(n + \frac{1}{2}\right)\lambda R}$$

$$r_5 = \sqrt{5.5 \times 589 \times 10^{-9} \times 5.0} = \sqrt{1.620 \times 10^{-5}}$$

$$r_5 = 4.02 \times 10^{-3} \text{ m} = \boxed{4.02 \text{ mm}}$$

**(c) Spacing between 5th and 6th dark rings:**

$$\Delta r = r_6 - r_5 = \sqrt{6\lambda R} - \sqrt{5\lambda R} = \sqrt{\lambda R}(\sqrt{6} - \sqrt{5})$$

$$= \sqrt{589 \times 10^{-9} \times 5.0} \times (2.449 - 2.236)$$

$$= (1.716 \times 10^{-3}) \times 0.213 = \boxed{0.365 \text{ mm}}$$

**Note:** As we go to higher orders, the ring spacing decreases ($\Delta r \approx \lambda R / (2r_n)$).

---

### Example 5: Single Slit Diffraction — Minima Position

**Problem:** Monochromatic light of wavelength $\lambda = 632.8$ nm passes through a single slit of width $a = 0.20$ mm. A lens of focal length $f = 50$ cm focuses the pattern on a screen. Find:
(a) the angular position of the first three minima
(b) the linear positions of the first three minima on the screen
(c) the width of the central maximum

**Solution:**

**(a) Angular positions of minima:**

Condition: $a\sin\theta = n\lambda$

$$\sin\theta_n = \frac{n\lambda}{a} = \frac{n \times 632.8 \times 10^{-9}}{0.20 \times 10^{-3}} = n \times 3.164 \times 10^{-3}$$

For small angles, $\theta_n \approx \sin\theta_n$:

- $n = 1$: $\theta_1 = 3.164 \times 10^{-3}$ rad $= \boxed{0.181°}$
- $n = 2$: $\theta_2 = 6.328 \times 10^{-3}$ rad $= \boxed{0.363°}$
- $n = 3$: $\theta_3 = 9.492 \times 10^{-3}$ rad $= \boxed{0.544°}$

**(b) Linear positions on screen:**

$y_n = f \tan\theta_n \approx f\theta_n$

- $y_1 = 0.50 \times 3.164 \times 10^{-3} = 1.58 \times 10^{-3}$ m $= \boxed{1.58 \text{ mm}}$
- $y_2 = 0.50 \times 6.328 \times 10^{-3} = 3.16 \times 10^{-3}$ m $= \boxed{3.16 \text{ mm}}$
- $y_3 = 0.50 \times 9.492 \times 10^{-3} = 4.75 \times 10^{-3}$ m $= \boxed{4.75 \text{ mm}}$

**(c) Width of central maximum:**

$$W = 2y_1 = 2 \times 1.58 = \boxed{3.16 \text{ mm}}$$

Or: $W = \frac{2\lambda f}{a} = \frac{2 \times 632.8 \times 10^{-9} \times 0.50}{0.20 \times 10^{-3}} = 3.16 \times 10^{-3}$ m $= 3.16$ mm ✓

---

### Example 6: Diffraction Grating — Maximum Orders

**Problem:** A diffraction grating has 6000 lines/cm. White light ($\lambda$ ranging from 400 nm to 700 nm) is incident normally. Find:
(a) the grating spacing
(b) the maximum order visible for each extreme wavelength
(c) the angular separation between the violet (400 nm) and red (700 nm) ends of the first-order spectrum

**Solution:**

**(a) Grating spacing:**

$$d = \frac{1}{N} = \frac{1}{6000} \text{ cm} = 1.667 \times 10^{-4} \text{ cm} = \boxed{1667 \text{ nm}}$$

**(b) Maximum orders:**

$$n_{max} = \left\lfloor\frac{d}{\lambda}\right\rfloor$$

- For $\lambda = 400$ nm: $n_{max} = \lfloor 1667/400 \rfloor = \lfloor 4.17 \rfloor = \boxed{4}$
- For $\lambda = 700$ nm: $n_{max} = \lfloor 1667/700 \rfloor = \lfloor 2.38 \rfloor = \boxed{2}$

So the violet end shows 4 orders while the red end shows only 2. Higher-order spectra overlap.

**(c) Angular separation in first order:**

For $\lambda = 400$ nm:
$$\sin\theta_v = \frac{\lambda_v}{d} = \frac{400}{1667} = 0.2400$$
$$\theta_v = 13.88°$$

For $\lambda = 700$ nm:
$$\sin\theta_r = \frac{\lambda_r}{d} = \frac{700}{1667} = 0.4199$$
$$\theta_r = 24.83°$$

$$\Delta\theta = \theta_r - \theta_v = 24.83° - 13.88° = \boxed{10.95°}$$

---

### Example 7: Malus' Law with Three Polarizers

**Problem:** Unpolarized light of intensity $I_0 = 100$ W/m² passes through three polarizers. P1 is vertical, P2 is at $60°$ to P1, and P3 is at $90°$ to P1 (horizontal). Find the intensity after each polarizer.

**Solution:**

**After P1 (vertical):**

Unpolarized light → polarizer:

$$I_1 = \frac{I_0}{2} = \frac{100}{2} = \boxed{50 \text{ W/m}^2}$$

Light is now vertically polarized.

**After P2 (at $60°$ to vertical):**

Apply Malus' law: $\theta = 60°$ between P1 and P2.

$$I_2 = I_1 \cos^2(60°) = 50 \times (0.5)^2 = 50 \times 0.25 = \boxed{12.5 \text{ W/m}^2}$$

Light is now polarized at $60°$ to vertical.

**After P3 (horizontal, $90°$ to vertical):**

The angle between P2's axis ($60°$ to vertical) and P3's axis ($90°$ to vertical) is $\theta = 90° - 60° = 30°$.

$$I_3 = I_2 \cos^2(30°) = 12.5 \times (\sqrt{3}/2)^2 = 12.5 \times 0.75 = \boxed{9.375 \text{ W/m}^2}$$

**Summary:**

| Polarizer | Intensity | Polarization |
|-----------|-----------|--------------|
| After P1 | 50 W/m² | Vertical ($0°$) |
| After P2 | 12.5 W/m² | At $60°$ |
| After P3 | 9.375 W/m² | Horizontal ($90°$) |

**Check:** Without P2, $I_3 = 0$ (crossed polarizers). Adding P2 "rotates" the polarization, allowing some light through. The intermediate polarizer increases transmission!

---

### Example 8: Brewster Angle

**Problem:** Light is incident from air ($\mu_1 = 1.00$) onto glass ($\mu_2 = 1.52$).
(a) Find the Brewster angle.
(b) Find the angle of refraction at Brewster's angle.
(c) Verify that the reflected and refracted rays are perpendicular.

**Solution:**

**(a) Brewster angle:**

$$\tan\theta_B = \frac{\mu_2}{\mu_1} = \frac{1.52}{1.00} = 1.52$$

$$\theta_B = \arctan(1.52) = \boxed{56.7°}$$

**(b) Angle of refraction:**

From Snell's law:

$$\mu_1 \sin\theta_B = \mu_2 \sin r$$

$$\sin r = \frac{\mu_1 \sin\theta_B}{\mu_2} = \frac{1.00 \times \sin(56.7°)}{1.52} = \frac{0.8360}{1.52} = 0.5499$$

$$r = \arcsin(0.5499) = \boxed{33.4°}$$

**(c) Verification:**

$$\theta_B + r = 56.7° + 33.4° = 90.1° \approx 90° \checkmark$$

(Small discrepancy due to rounding.) The reflected and refracted rays are indeed perpendicular at Brewster's angle.

**Note:** At this angle, the reflected light is 100% polarized perpendicular to the plane of incidence.

---

### Example 9: Michelson Interferometer — Wavelength Measurement

**Problem:** In a Michelson interferometer, a mirror is moved by a distance of $0.322$ mm, and 1024 fringes are observed to pass across the reference point. Find the wavelength of the light used.

**Solution:**

When the mirror moves by distance $d$, the optical path difference changes by $2d$ (round trip). The number of fringes that shift:

$$n = \frac{2d}{\lambda}$$

Solving for $\lambda$:

$$\lambda = \frac{2d}{n} = \frac{2 \times 0.322 \times 10^{-3}}{1024}$$

$$\lambda = \frac{6.44 \times 10^{-4}}{1024} = 6.289 \times 10^{-7} \text{ m}$$

$$\boxed{\lambda = 628.9 \text{ nm}}$$

This is in the orange-red region of visible light.

**Verification:** The fringe width in the interferometer pattern is $\beta = \lambda/2 = 314$ nm, which is the path difference change per fringe. For 1024 fringes: $1024 \times 314$ nm $= 321{,}536$ nm $= 0.322$ mm ✓

---

### Example 10: Resolving Power of a Grating

**Problem:** A grating has 5000 lines and is illuminated with light centered at $\lambda = 500$ nm in the second order.
(a) Find the resolving power.
(b) What is the minimum wavelength difference $\Delta\lambda$ that can be resolved?
(c) Can this grating resolve the sodium D lines ($\lambda_1 = 589.0$ nm, $\lambda_2 = 589.6$ nm) in the first order?

**Solution:**

**(a) Resolving power:**

$$R = nN = 2 \times 5000 = \boxed{10{,}000}$$

**(b) Minimum resolvable wavelength difference:**

$$\Delta\lambda = \frac{\lambda}{R} = \frac{500}{10{,}000} = \boxed{0.050 \text{ nm}}$$

**(c) Sodium D lines in first order:**

First order: $R = nN = 1 \times 5000 = 5000$

Required resolution: $\Delta\lambda_{needed} = 589.6 - 589.0 = 0.6$ nm

Required resolving power: $R_{needed} = \frac{\lambda}{\Delta\lambda} = \frac{589.3}{0.6} = 982$

Since $R = 5000 > R_{needed} = 982$:

$$\boxed{\text{Yes, the grating can easily resolve the sodium D lines in first order.}}$$

**Check:** $R = 5000$ means $\Delta\lambda_{min} = 589.3/5000 = 0.118$ nm. Since $0.6$ nm $> 0.118$ nm, the lines are well resolved. ✓

---

### Example 11: Thin Film — Multiple Wavelengths

**Problem:** White light is incident normally on a thin soap film ($\mu = 1.33$) in air. The film is 300 nm thick.
(a) Which wavelengths are maximally reflected?
(b) Which wavelengths are minimized in reflection (appear dark)?
(c) What color does the film appear in reflected light?

**Solution:**

**Phase changes:** 1 total (air→film at top: rare→dense → π; film→air at bottom: dense→Rare → 0).

**Condition for constructive interference (bright reflection):**

$$2\mu t = \left(n - \frac{1}{2}\right)\lambda$$

$$\lambda = \frac{2\mu t}{n - 1/2} = \frac{2(1.33)(300)}{n - 0.5} = \frac{798}{n - 0.5} \text{ nm}$$

For various $n$:

| $n$ | $\lambda$ (nm) | Visible? | Color |
|-----|----------------|----------|-------|
| 1 | 1596 | No (IR) | — |
| 2 | 532 | Yes | Green |
| 3 | 319 | No (UV) | — |

Only $n = 2$ gives a visible wavelength: $\lambda = 532$ nm (green).

**(b) Condition for destructive interference (dark reflection):**

$$2\mu t = n\lambda$$

$$\lambda = \frac{2\mu t}{n} = \frac{798}{n} \text{ nm}$$

| $n$ | $\lambda$ (nm) | Visible? | Color |
|-----|----------------|----------|-------|
| 1 | 798 | Marginal (deep red) | Red |
| 2 | 399 | Marginal (deep violet) | Violet |
| 3 | 266 | No (UV) | — |

**(c) Color of reflected light:**

The film strongly reflects green (532 nm) and partially reflects red and violet. The dominant reflected color is:

$$\boxed{\text{Green (with some reddish and bluish tints)}}$$

---

### Example 12: Resolving Power — Telescope

**Problem:** Two stars are separated by an angular distance of $2.5 \times 10^{-6}$ rad. What minimum aperture diameter is needed to resolve them using light of wavelength $\lambda = 550$ nm?

**Solution:**

**Rayleigh criterion for a circular aperture:**

$$\theta_{min} = 1.22\frac{\lambda}{D}$$

Setting $\theta_{min} = 2.5 \times 10^{-6}$ rad:

$$D = 1.22\frac{\lambda}{\theta_{min}} = 1.22 \times \frac{550 \times 10^{-9}}{2.5 \times 10^{-6}}$$

$$D = 1.22 \times 0.220 = 0.2684 \text{ m}$$

$$\boxed{D \geq 26.8 \text{ cm}}$$

A telescope with aperture diameter of at least 26.8 cm is needed.

**Resolving power of this telescope:**

$$R = \frac{D}{1.22\lambda} = \frac{0.268}{1.22 \times 550 \times 10^{-9}} = \frac{0.268}{6.71 \times 10^{-7}} = 3.99 \times 10^5$$

This means the telescope can resolve two wavelengths differing by:

$$\Delta\lambda = \frac{\lambda}{R} = \frac{550}{3.99 \times 10^5} = 1.38 \times 10^{-3} \text{ nm} = 0.00138 \text{ nm}$$

---

## 13. Complete Formula Reference Table

### Interference Formulas

| Formula | Description | Variables |
|---------|-------------|-----------|
| $\Delta = d\sin\theta \approx yd/D$ | YDSE path difference | $d$ = slit separation, $D$ = screen distance, $y$ = position |
| $y_n = n\lambda D/d$ | YDSE bright fringe position | $n$ = order ($0, \pm 1, \pm 2, \ldots$) |
| $y_n = (2n-1)\lambda D/(2d)$ | YDSE dark fringe position | $n$ = $\pm 1, \pm 2, \ldots$ |
| $\beta = \lambda D/d$ | YDSE fringe width | $\lambda$ = wavelength |
| $I = 4I_0\cos^2(\phi/2)$ | Two-beam interference intensity | $\phi$ = phase difference |
| $\phi = 2\pi\Delta/\lambda$ | Phase from path difference | |
| $\Delta y = (\mu-1)tD/d$ | Fringe shift (glass sheet) | $\mu$ = refractive index, $t$ = thickness |
| $y_0 = -xD/D'$ | Shift from source displacement | $x$ = source displacement, $D'$ = source-to-slit distance |
| $\beta_{liq} = \lambda_0 D/(\mu d)$ | Fringe width in liquid | $\mu$ = liquid refractive index |

### Thin Film Formulas

| Formula | Description | Condition |
|---------|-------------|-----------|
| $2\mu t\cos r = (2n-1)\lambda/2$ | Constructive (reflected) | 1 phase change |
| $2\mu t\cos r = n\lambda$ | Destructive (reflected) | 1 phase change |
| $2\mu t\cos r = n\lambda$ | Constructive (reflected) | 0 or 2 phase changes |
| $2\mu t\cos r = (2n-1)\lambda/2$ | Destructive (reflected) | 0 or 2 phase changes |
| $\Delta_{optical} = (\mu-1)t$ | Extra path from thin film | Normal incidence |

### Newton's Rings Formulas

| Formula | Description | Notes |
|---------|-------------|-------|
| $t = r^2/(2R)$ | Air film thickness | $R$ = radius of curvature |
| $r_n = \sqrt{n\lambda R}$ | Dark ring radius (reflected) | $n = 0, 1, 2, \ldots$ |
| $r_n = \sqrt{(n+1/2)\lambda R}$ | Bright ring radius (reflected) | $n = 0, 1, 2, \ldots$ |
| $r_n = \sqrt{n\lambda R}$ | Bright ring radius (transmitted) | Complementary pattern |
| $\Delta r_n \approx \lambda R/(2r_n)$ | Ring spacing (large $n$) | Spacing decreases outward |

### Diffraction Formulas

| Formula | Description | Notes |
|---------|-------------|-------|
| $a\sin\theta = n\lambda$ | Single slit minima | $n = \pm 1, \pm 2, \ldots$ (NOT $n = 0$) |
| $W = 2\lambda D/a$ | Central maximum width | Twice as wide as other maxima |
| $I = I_0(\sin\alpha/\alpha)^2$ | Single slit intensity | $\alpha = \pi a\sin\theta/\lambda$ |
| $I = 4I_0\cos^2(\pi d\sin\theta/\lambda) \cdot (\sin\alpha/\alpha)^2$ | Double slit (interference + diffraction) | $d$ = slit separation, $a$ = slit width |

### Grating Formulas

| Formula | Description | Notes |
|---------|-------------|-------|
| $d = 1/N$ | Grating spacing | $N$ = lines per unit length |
| $d\sin\theta = n\lambda$ | Principal maxima | $n = 0, \pm 1, \pm 2, \ldots$ |
| $n_{max} = \lfloor d/\lambda \rfloor$ | Maximum visible order | |
| $R = nN$ | Resolving power | $n$ = order, $N$ = total slits illuminated |
| $\Delta\lambda_{min} = \lambda/R$ | Minimum resolvable wavelength | |
| $d(\sin\theta_i + \sin\theta_d) = n\lambda$ | Grating equation (oblique) | |

### Polarization Formulas

| Formula | Description | Notes |
|---------|-------------|-------|
| $I = I_0/2$ | After polarizer (from unpolarized) | |
| $I = I_0\cos^2\theta$ | Malus' law | $\theta$ = angle between polarizer and analyzer |
| $I_n = (I_0/2)\cos^{2(n-1)}\theta$ | $n$ polarizers, each at $\theta$ to previous | First polarizer on unpolarized light |
| $\tan\theta_B = \mu$ | Brewster's angle | Reflected light fully polarized |
| $\theta_B + r = 90°$ | At Brewster's angle | Reflected ⊥ refracted |

### Advanced Formulas

| Formula | Description | Notes |
|---------|-------------|-------|
| $n = 2d/\lambda$ | Michelson fringe shift | $d$ = mirror displacement |
| $R_{FP} = n\mathcal{F}$ | Fabry-Pérot resolving power | $\mathcal{F}$ = finesse |
| $\mathcal{F} = \pi\sqrt{R}/(1-R)$ | Finesse | $R$ = mirror reflectivity |
| $\Delta\lambda_{FSR} = \lambda^2/(2\mu t)$ | Free spectral range | $t$ = etalon spacing |
| $\theta_{min} = 1.22\lambda/D$ | Rayleigh criterion (circular) | $D$ = aperture diameter |
| $l_c = c\tau_c$ | Coherence length | $\tau_c$ = coherence time |

---

## Cross-References

- [[engineering-physics/module-2-optoelectronics-lasers-fiber-optics|Module 2: Optoelectronics]] — Fabry-Pérot resonators in laser cavities, diffraction limits on beam quality, fiber mode analysis
- [[engineering-physics/module-3-quantum-mechanics|Module 3: Quantum Mechanics]] — Wave-particle duality, electron diffraction (Davisson-Germer), de Broglie wavelength
- [[engineering-physics/module-4-semiconductors-electromagnetism|Module 4: Semiconductors & Electromagnetism]] — Maxwell's equations → wave equation → light as EM wave → polarization

---

*Module 1 of 4 — [[engineering-physics/module-2-optoelectronics-lasers-fiber-optics|Module 2 →]] | [[engineering-physics/module-3-quantum-mechanics|Module 3 →]] | [[engineering-physics/module-4-semiconductors-electromagnetism|Module 4 →]]*
*Total formulas: 30+ | Worked examples: 12 | ASCII flowcharts: 3*
