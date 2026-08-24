---
module: "physics"
topic: "Physics Formula Sheet — Optics (JEE Advanced)"
tags: [physics, optics, formulas, jee, ray, wave, instruments]
last_updated: "2026-08-11"
source: "Kota notes, standard references"
---

# Physics Formula Sheet — Optics (JEE Advanced)

> Complete optics formula compendium. Ray, wave, and instruments formulas with sign conventions.

---

## 📐 Ray Optics (Geometrical)

| Quantity | Formula | Sign Convention |
|----------|---------|-----------------|
| **Mirror Formula** | $\frac{1}{v} + \frac{1}{u} = \frac{1}{f} = \frac{2}{R}$ | $u$ negative (real object), $v$ positive (real image), $f$ positive (concave), $R$ positive (concave) |
| **Magnification** | $m = -\frac{v}{u} = \frac{h'}{h}$ | $m$ negative = inverted, positive = erect |
| **Mirror Types** | Concave: $f>0$, $R>0$; Convex: $f<0$, $R<0$ | |
| **Refraction (Plane)** | $\frac{\sin i}{\sin r} = \mu_{21} = \frac{\mu_2}{\mu_1} = \frac{v_1}{v_2} = \frac{\lambda_1}{\lambda_2}$ | |
| **Apparent Depth** | $d_{app} = \frac{d_{real}}{\mu}$ (normal view); $d_{app} = d_{real} \frac{\mu_1}{\mu_2}$ | |
| **Refraction (Spherical)** | $\frac{\mu_2}{v} - \frac{\mu_1}{u} = \frac{\mu_2 - \mu_1}{R}$ | $u$ negative, $v$ positive if real, $R$ positive if center right of surface |
| **Lens Maker Formula** | $\frac{1}{f} = (\mu - 1)(\frac{1}{R_1} - \frac{1}{R_2})$ | $R_1$ first surface, $R_2$ second; $R>0$ if center right |
| **Lens Formula** | $\frac{1}{v} - \frac{1}{u} = \frac{1}{f}$ | $u$ negative, $v$ positive (real), $f$ positive (convex) |
| **Lens Magnification** | $m = \frac{v}{u} = \frac{h'}{h}$ | $m$ positive = erect (virtual), negative = inverted (real) |
| **Lens Types** | Convex (converging): $f>0$; Concave (diverging): $f<0$ | |
| **Power** | $P = \frac{1}{f(m)} = \frac{100}{f(cm)}$ (Diopter) | |
| **Combination (Contact)** | $P_{eq} = \sum P_i$; $\frac{1}{f_{eq}} = \sum \frac{1}{f_i}$ | |
| **Separated Lenses** | $\frac{1}{F} = \frac{1}{f_1} + \frac{1}{f_2} - \frac{d}{f_1 f_2}$ | $d$ = separation |
| **Prism** | $\delta = i + e - A$ | $i$ = incidence, $e$ = emergence, $A$ = prism angle |
| **Min Deviation** | $\mu = \frac{\sin\frac{A+\delta_m}{2}}{\sin\frac{A}{2}}$ | $\delta_m = 2i - A$; $i = e$, $r_1 = r_2 = A/2$ |
| **Dispersion** | $\delta_v - \delta_r = (\mu_v - \mu_r)A$ | |
| **Dispersive Power** | $\omega = \frac{\mu_v - \mu_r}{\mu - 1}$ | $\mu = \frac{\mu_v + \mu_r}{2}$ (mean) |
| **Achromatic Combination** | $\omega_1 f_1 + \omega_2 f_2 = 0$ (contact); $\frac{\omega_1}{f_1} + \frac{\omega_2}{f_2} = 0$ (separated) | |

---

## 📐 Wave Optics

| Quantity | Formula | Notes |
|----------|---------|-------|
| **Young's Double Slit (YDS)** | | |
| Fringe Width | $\beta = \frac{\lambda D}{d}$ | $D$ = slit-screen, $d$ = slit separation |
| Bright Fringes | $y_n = \frac{n\lambda D}{d}$ | $n = 0, \pm 1, \pm 2...$ |
| Dark Fringes | $y_n = \frac{(2n-1)\lambda D}{2d}$ | $n = 1, 2, 3...$ |
| Path Difference | $\Delta = d \sin\theta \approx \frac{dy}{D}$ | |
| Constructive | $\Delta = n\lambda$ | |
| Destructive | $\Delta = (2n-1)\frac{\lambda}{2}$ | |
| **Coherence** | Temporal: $\Delta \lambda / \lambda \ll 1$; Spatial: source size $\ll \lambda D/d$ | |
| **Intensity Distribution** | $I = I_{max} \cos^2(\frac{\pi d \sin\theta}{\lambda})$ | $I_{max} = 4I_0$ (equal slits) |
| **Thin Film** | | |
| Reflected | $2\mu t \cos r = n\lambda$ (phase change $\pi$ at denser) | $r$ = angle in film |
| Transmitted | $2\mu t \cos r = (2n-1)\frac{\lambda}{2}$ | |
| Normal Incidence | $2\mu t = n\lambda$ (reflected); $= (2n-1)\frac{\lambda}{2}$ (transmitted) | |
| **Diffraction (Single Slit)** | | |
| Minima | $a \sin\theta = n\lambda$ ($n = \pm 1, \pm 2...$) | |
| Maxima (approx) | $a \sin\theta = (2n+1)\frac{\lambda}{2}$ | |
| Central Max Width | $\frac{2\lambda D}{a}$ (linear); $\frac{2\lambda}{a}$ (angular) | |
| **Resolving Power** | | |
| Telescope | $R.P. = \frac{D}{1.22\lambda}$ | $D$ = objective diameter |
| Microscope | $R.P. = \frac{2\mu \sin\theta}{\lambda}$ | $\mu \sin\theta$ = numerical aperture |
| **Polarization** | | |
| Malus' Law | $I = I_0 \cos^2\theta$ | $\theta$ = angle between polarizer & analyzer |
| Brewster's Angle | $\tan\theta_p = \mu$ | $\theta_p + r = 90^\circ$ |
| Polaroid | Transmits component $\parallel$ to pass axis | |

---

## 📐 Optical Instruments

| Instrument | Formula | Notes |
|------------|---------|-------|
| **Simple Microscope** | | |
| Normal Adjustment | $M = \frac{D}{f}$ | Image at $\infty$, $D=25$ cm |
| Near Point | $M = 1 + \frac{D}{f}$ | Image at $D$ (max magnification) |
| **Compound Microscope** | | |
| Normal Adjustment | $M = \frac{v_0}{u_0} \cdot \frac{D}{f_e} \approx \frac{L}{f_0} \cdot \frac{D}{f_e}$ | $L$ = tube length ($v_0 + f_e$) |
| Near Point | $M = \frac{v_0}{u_0}(1 + \frac{D}{f_e})$ | |
| **Telescope (Astronomical)** | | |
| Normal Adjustment | $M = \frac{f_0}{f_e}$ | Image at $\infty$, length $= f_0 + f_e$ |
| Near Point | $M = \frac{f_0}{f_e}(1 + \frac{f_e}{D})$ | Length $= f_0 + \frac{f_e D}{f_e + D}$ |
| **Terrestrial Telescope** | $M = \frac{f_0}{f_e}$ (with erecting lens) | Length $= f_0 + 4f + f_e$ |
| **Galilean Telescope** | $M = \frac{f_0}{f_e}$ | $f_e$ negative (concave eye lens) |
| **Resolving Power** | | |
| Microscope | $R.P. = \frac{2\mu \sin\theta}{\lambda} = \frac{2 \text{NA}}{\lambda}$ | NA = numerical aperture |
| Telescope | $R.P. = \frac{D}{1.22\lambda}$ | Dawes' limit: $\theta_{min} = \frac{116}{D(\text{mm})}$ arcsec |

---

## 📐 Sign Conventions (Cartesian)

| Quantity | Sign |
|----------|------|
| Object distance ($u$) | Negative (real object on left) |
| Image distance ($v$) | Positive (real, right), Negative (virtual, left) |
| Focal length ($f$) | Positive (convex lens, concave mirror), Negative (concave lens, convex mirror) |
| Radius ($R$) | Positive (center right of surface), Negative (center left) |
| Height ($h, h'$) | Positive (upward), Negative (downward) |
| Magnification ($m$) | Positive (erect), Negative (inverted) |

---

*Optics formula sheet — use Cartesian sign convention consistently. Cross-reference with topic-wise notes for derivations and ray diagrams.*