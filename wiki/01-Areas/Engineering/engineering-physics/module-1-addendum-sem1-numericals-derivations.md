---
course_code: "EP-SEM1"
course_name: "Engineering Physics Sem 1"
unit: "Module 1 — Wave Optics (addendum)"
tags: [engineering-physics, btech, optics, interference, thin-film, diffraction, grating, numericals]
last_updated: "2026-09-09"
description: "Module 1 addendum: thin-film reflected-light derivation transcribed from Sem-1 scans plus 12 fully solved interference and grating numericals."
---

# Module 1 Addendum — Thin-Film Derivation + Solved Source Numericals

## For future agent

This note holds Sem-1 Module-1 material transcribed 2026-09-09 from `raw-sources/SEM I-20260908T193519Z-1-001/SEM I/MODULE 1/` (two PDFs read for structure, three images transcribed verbatim into LaTeX). Parent theory lives in [[module-1-optics-interference-diffraction]]; filename catalog of all ~70 unread sources in [[source-map-physics-sem1]]. Confidence: derivation `high` (direct transcription); Q2 dark-band wavelength `medium` (order-numbering ambiguous, flagged inline).

## 1. Thin-film reflected-light derivation (from textbook scans WA0014 + WA0016)

Setup: transparent film, uniform thickness $t$, refractive index $\mu$, surrounded by air. Monochromatic ray $AB$ incident at angle $i$, refracted at angle $r$. Ray 1 reflects at top ($BR$); ray 2 refracts along $BC$, reflects at $C$, emerges along $DR_1 \parallel BR$. Drop normal $DE$ on $BR$ and $BF$ on $CD$; produce $DC$ back to meet $BQ$ produced at $P$. Geometry gives $\angle BDE = i$, $\angle QPC = r$, $BC = PC$.

Optical path difference (film path minus air path):

$$\Delta = \mu(BC + CD) - BE \tag{1}$$

Snell's law via the figure ($\mu = \sin i / \sin r = (BE/BD)/(FD/BD) = BE/FD$):

$$BE = \mu(FD) \tag{2}$$

Substitute (2) into (1), using $CD = CF + FD$:

$$\Delta = \mu(BC + CD) - \mu(FD) = \mu(BC + CF) = \mu(PF) \tag{3}$$

From $\triangle BPF$: $\cos r = PF/BP$, $BP = 2t$, so $PF = 2t\cos r$:

$$\boxed{\Delta = 2\mu t\cos r} \tag{5}$$

**Stokes $\pi$ correction:** the top-surface reflection (rarer $\to$ denser) suffers an abrupt phase change $\pi \equiv \lambda/2$. Effective path difference:

$$\boxed{\Delta_{\mathrm{eff}} = 2\mu t\cos r \pm \lambda/2}$$

- Bright (maxima, $\Delta_{\mathrm{eff}} = n\lambda$): $\boxed{2\mu t\cos r = (2n \pm 1)\lambda/2}$
- Dark (minima, $\Delta_{\mathrm{eff}} = (2n\pm1)\lambda/2$): $\boxed{2\mu t\cos r \pm \lambda/2 = (2n\pm1)\lambda/2 \Rightarrow 2\mu t\cos r = n\lambda}$ (normal-incidence form; see [[module-1-optics-interference-diffraction]] §3 for the $\cos r$ general case and transmitted complement $2\mu t = n\lambda$ bright / $(2n-1)\lambda/2$ dark).

Related revision: [[thin-film-interference-revision]].

## 2. Interference numericals (from `Interference Numerical.jpeg`, fully solved)

Formula key: reflected system, one $\pi$ change, angle $r$ from $\sin i = \mu\sin r$. Bright: $2\mu t\cos r = (2n-1)\lambda/2$; dark: $2\mu t\cos r = n\lambda$.

**Q1.** $\lambda = 600\,\mathrm{nm}$, $\mu = \sqrt{3/2}$, $i = 45^\circ$, bright reflected, minimum $t$.
$\sin r = \sin45^\circ/\mu = 0.7071/1.2247 = 1/\sqrt{3}$, $r \approx 35.26^\circ$, $\cos r = \sqrt{2/3} \approx 0.8165$, and $\mu\cos r = 1$ exactly. $n=1$: $2(1)t = \lambda/2 \Rightarrow \boxed{t_{\min} = \lambda/4 = 150\,\mathrm{nm}}$.

**Q2.** Soap $\mu = 1.33$, $t = 1.5\times10^{-5}\,\mathrm{cm} = 150\,\mathrm{nm}$, $i = 30^\circ$, dark 2nd order.
$\sin r = 0.5/1.33 \approx 0.3759$, $\cos r \approx 0.9267$. $2\mu t\cos r \approx 369.7\,\mathrm{nm} = n\lambda$, $n = 2 \Rightarrow \boxed{\lambda \approx 185\,\mathrm{nm}}$ (deep UV — physically suspicious for a visible-light setup; if orders are counted from $n=0/1$ so "2nd order" means $n=1$, then $\lambda \approx 370\,\mathrm{nm}$). Confidence `medium` — order convention unverified (TBC against course convention).

**Q3.** Oil $\mu = 1.25$, normal incidence, destructive at $5000\,\mathrm{\AA}$ and $6000\,\mathrm{\AA}$, none between.
Dark: $2\mu t = n\lambda$. Consecutive orders: $n(6000) = (n+1)(5000) \Rightarrow n = 5$. $\boxed{t = 5\times6000/(2\times1.25) = 12000\,\mathrm{\AA} = 1.2\,\mu\mathrm{m}}$ (checks against 6th order of $5000\,\mathrm{\AA}$).

**Q4.** White light normal on soap $\mu = 1.33$, $t = 380\,\mathrm{nm}$; visible $4000$–$7000\,\mathrm{\AA}$ intensified?
Bright: $\lambda = 4\mu t/(2n-1) = 2021.6/(2n-1)\,\mathrm{nm}$. $n=2 \Rightarrow 673.9\,\mathrm{nm} \approx \boxed{6740\,\mathrm{\AA}}$ (red); $n=3 \Rightarrow 404.3\,\mathrm{nm} \approx \boxed{4040\,\mathrm{\AA}}$ (violet); $n=1,4$ fall outside visible.

**Q5.** White at $50^\circ$ on film $\mu = 1.25$, bright yellow $\lambda = 5893\,\mathrm{\AA}$ in **transmitted**, minimum $t$.
Transmitted bright: $2\mu t\cos r = n\lambda$, $n=1$. $\sin r = \sin50^\circ/1.25 \approx 0.6128$, $\cos r \approx 0.7903$. $\boxed{t = 5893/(2\times1.25\times0.7903) \approx 2980\,\mathrm{\AA} \approx 298\,\mathrm{nm}}$.

**Q6.** Oil $\mu = 1.20$ on glass ($\mu_{\mathrm{glass}} \approx 1.5$), edge thinnest.
(i) Top reflection air$\to$oil: $\pi$; bottom oil$\to$glass (denser): $\pi$ — two changes cancel, so $t\to0$ gives constructive $\Rightarrow$ outer thin region appears **bright** (white-light wash at the very edge). (ii) Bright green $\lambda = 540\,\mathrm{nm}$, 2nd order, reflected: with 0/2-change condition $2\mu t = n\lambda$, $n=2 \Rightarrow \boxed{t = 2\times540/(2\times1.20) = 450\,\mathrm{nm}}$ at normal incidence (assumes order counted $n=2$; state convention in exams).

## 3. Grating numericals (from `1.2 Diffraction.pdf`, fully solved)

Grating law: $\boxed{(a+b)\sin\theta = n\lambda}$, $N = 1/(a+b)$; resolving power $\boxed{R = \lambda/\Delta\lambda = nN}$.

**G1.** $n=2$, $\lambda = 5\times10^{-5}\,\mathrm{cm}$, $\theta = 30^\circ$: $(a+b) = 2\lambda/\sin\theta = 2\times10^{-4}\,\mathrm{cm} \Rightarrow \boxed{N = 5000\,\mathrm{lines/cm}}$.

**G2.** $\lambda = 6000\,\mathrm{\AA} = 6\times10^{-5}\,\mathrm{cm}$, $N = 6000/\mathrm{cm}$: $d = 1.667\times10^{-4}\,\mathrm{cm}$, $n_{\max} = \lfloor d/\lambda \rfloor = \lfloor 2.78 \rfloor \Rightarrow \boxed{n_{\max} = 2}$.

**G3.** $5400\,\mathrm{\AA}$ (order $n$) overlaps $4050\,\mathrm{\AA}$ (order $n+1$), $\theta = 30^\circ$: $5400n = 4050(n+1) \Rightarrow n = 3$; $d\sin\theta = 3\times5400\,\mathrm{\AA} = 1.62\times10^{-4}\,\mathrm{cm} \Rightarrow d = 3.24\times10^{-4}\,\mathrm{cm} \Rightarrow \boxed{N \approx 3086/\mathrm{cm}}$.

**G4.** 3rd order of $\lambda$ = 4th order of $4992\,\mathrm{\AA}$: $3\lambda = 4\times4992 \Rightarrow \boxed{\lambda = 6656\,\mathrm{\AA}}$.

**G5.** $620\,\mathrm{rulings/mm}$, width $0.5\,\mathrm{mm}$ ($N_{\mathrm{tot}} = 310$), 3rd order $\lambda = 481\,\mathrm{nm}$: $\boxed{\Delta\lambda = \lambda/(nN) = 481/(3\times310) \approx 0.52\,\mathrm{nm}}$.

**G6.** Grating $2\,\mathrm{cm} \times 6000/\mathrm{cm}$ ($N = 12000$), $\lambda = 5890\,\mathrm{\AA}$: $d = 1.667\times10^{-4}\,\mathrm{cm}$, $n_{\max} = \lfloor d/\lambda \rfloor = 2 \Rightarrow \boxed{R_{\max} = nN = 24000}$ (first order $R = 12000$).
