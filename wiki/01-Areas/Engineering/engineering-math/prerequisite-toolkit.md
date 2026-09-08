---
course_code: "216U06C101"
course_name: "Applied Mathematics-I"
unit: "Prerequisite Toolkit"
tags: [engineering-math, btech, prerequisites, trigonometry, differentiation, integration, formula-sheet]
last_updated: "2026-09-09"
description: "Zero-th week toolkit for AM-I: trig identities, standard derivatives with tricks, integration formulae plus substitution map — distilled from the dump's prerequisite folder."
---

## For future agent

The dump's `Prerequisite Topics, (rules & formulae)/` folder (4 PDFs) is assumed knowledge the modules build on — this note makes it explicit so [[module-4-linear-differential-equations]] (IF/integration) and [[module-5-complex-numbers]] (trig/hyperbolic) never have to re-derive basics. OCR of the sources is noisy; identities below are the standard syllabus set cross-checked against the extracted headings (confidence: high on identities, medium on matching exact file order).

# Prerequisite Toolkit — Trig, Differentiation, Integration

## 1. Trigonometry (from `Basics of Trigonometry.pdf`)

$$\sin^2\theta + \cos^2\theta = 1, \qquad 1 + \tan^2\theta = \sec^2\theta, \qquad 1 + \cot^2\theta = \csc^2\theta$$

Double/half angle: $\sin 2\theta = 2\sin\theta\cos\theta$, $\cos 2\theta = 2\cos^2\theta - 1 = 1 - 2\sin^2\theta$, $\tan 2\theta = \tfrac{2t}{1-t^2}$. Products: $2\sin A\cos B = \sin(A+B) + \sin(A-B)$, $2\cos A\cos B = \cos(A-B) + \cos(A+B)$, $2\sin A\sin B = \cos(A-B) - \cos(A+B)$. Needed for: De Moivre expansions ([[module-5-complex-numbers]] §9), PI trig operators ($D^2 \to -a^2$).

## 2. Differentiation rules (from `Differential formula rules and tricks.pdf`)

$$\frac{d}{dx}x^n = nx^{n-1}, \quad \frac{d}{dx}e^{ax} = ae^{ax}, \quad \frac{d}{dx}a^x = a^x\ln a, \quad \frac{d}{dx}\ln x = \frac{1}{x}$$

$$\frac{d}{dx}\sin ax = a\cos ax, \quad \frac{d}{dx}\tan x = \sec^2 x, \quad \frac{d}{dx}\sin^{-1}x = \frac{1}{\sqrt{1-x^2}}, \quad \frac{d}{dx}\tan^{-1}x = \frac{1}{1+x^2}$$

Product/quotient/chain: $(uv)' = u'v + uv'$, $\left(\tfrac{u}{v}\right)' = \tfrac{u'v-uv'}{v^2}$, $\tfrac{dy}{dx} = \tfrac{dy}{du}\tfrac{du}{dx}$. Tricks file emphasis: differentiate $e^{ax}V$ and $\sin^{-1}$/$\tan^{-1}$ forms blind-fast — they recur in IF problems and Euler deductions ([[module-3-homogeneous-functions]] deduction 2).

## 3. Integration formulae + substitutions (from `Integral formulae substitutions and tricks.pdf`, `Integration Formula List 2.pdf`, DE `Integration Formula List.pdf`)

$$\int x^n dx = \frac{x^{n+1}}{n+1},\quad \int e^{ax}dx = \frac{e^{ax}}{a},\quad \int \frac{dx}{x^2+a^2} = \frac{1}{a}\tan^{-1}\!\frac{x}{a},\quad \int \frac{dx}{\sqrt{a^2-x^2}} = \sin^{-1}\!\frac{x}{a}$$

$$\int \frac{dx}{x^2-a^2} = \frac{1}{2a}\ln\left|\frac{x-a}{x+a}\right|,\quad \int \sqrt{a^2-x^2}\,dx = \frac{x}{2}\sqrt{a^2-x^2} + \frac{a^2}{2}\sin^{-1}\!\frac{x}{a}$$

By parts: $\int u\,dv = uv - \int v\,du$ (ILATE order). Substitution map: $\sqrt{a^2-x^2} \to x = a\sin t$; $\sqrt{a^2+x^2} \to x = a\tan t$; $\sqrt{x^2-a^2} \to x = a\sec t$; $e^x$-rich integrands $\to t = e^x$. Partial fractions for $\tfrac{P(x)}{(x-a)(x-b)\cdots}$. Direct use: every IF integral $\int Q \cdot e^{\int P dx}dx$ in [[module-4-linear-differential-equations]] §2.1.

## Source map — `Prerequisite Topics, (rules & formulae)/`

| Dump file | Use |
|-----------|-----|
| `Basics of Trigonometry.pdf` | §1 above |
| `Differential formula rules and tricks.pdf` | §2 above |
| `Integral formulae substitutions and tricks.pdf` + `Integration Formula List 2.pdf` | §3 above (two overlapping lists — consolidated, duplicates dropped) |

## Related

[[formula-sheet-am]] · [[ise-exam-prep-am1]] · [[module-4-linear-differential-equations]] · [[module-5-complex-numbers]]
