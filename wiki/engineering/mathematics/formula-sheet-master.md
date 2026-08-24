---
module: "mathematics"
topic: "Mathematics Formula Sheet — Master Reference (JEE Advanced)"
tags: [mathematics, formulas, jee, reference, quick-revision]
last_updated: "2026-08-11"
source: "/raw-sources/math/MATHS FORMULA SHEET.pdf, /raw-sources/math/TRIGNOMETRIC-Formulas.pdf, Kota notes"
---

# Mathematics Formula Sheet — Master Reference

> Complete formula compendium for JEE Advanced. Every formula, identity, and shortcut in one place.

---

## 📐 Algebra

### Complex Numbers
| Formula | Expression |
|---------|------------|
| Modulus | $|z| = \sqrt{a^2 + b^2}$ |
| Argument | $\arg(z) = \tan^{-1}(b/a) \in (-\pi, \pi]$ |
| Polar Form | $z = r(\cos\theta + i\sin\theta) = re^{i\theta}$ |
| Conjugate | $\bar{z} = a - ib$, $z\bar{z} = |z|^2$ |
| Inverse | $z^{-1} = \bar{z}/|z|^2$ |
| Euler's Formula | $e^{i\theta} = \cos\theta + i\sin\theta$ |
| De Moivre | $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$ |
| Cube Roots of Unity | $1, \omega, \omega^2$; $\omega = -\frac{1}{2} + i\frac{\sqrt{3}}{2}$, $1+\omega+\omega^2=0$, $\omega^3=1$ |
| $n$-th Roots of Unity | $z_k = e^{2\pi i k/n}$, $k=0,1,\dots,n-1$; sum $=0$, product $=(-1)^{n-1}$ |
| Rotation | $\frac{z_2 - z_1}{z_3 - z_1} = \frac{|z_2 - z_1|}{|z_3 - z_1|} e^{i\theta}$ |
| Parallelogram Law | $|z_1+z_2|^2 + |z_1-z_2|^2 = 2(|z_1|^2 + |z_2|^2)$ |

### Quadratic Equations
| Formula | Expression |
|---------|------------|
| Roots | $\alpha,\beta = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$ |
| Sum/Product | $\alpha+\beta = -b/a$, $\alpha\beta = c/a$ |
| Discriminant | $D = b^2 - 4ac$; $D>0$: real distinct, $D=0$: equal, $D<0$: complex |
| Symmetric Sums | $\alpha^2+\beta^2 = (\alpha+\beta)^2 - 2\alpha\beta$, $\alpha^3+\beta^3 = (\alpha+\beta)^3 - 3\alpha\beta(\alpha+\beta)$ |
| Recurrence | $S_n = \alpha^n+\beta^n = -\frac{b}{a}S_{n-1} - \frac{c}{a}S_{n-2}$ |
| Common Root | $(c_1a_2-c_2a_1)^2 = (a_1b_2-a_2b_1)(b_1c_2-b_2c_1)$ |
| Location: Both in $(\alpha,\beta)$ | $f(\alpha)f(\beta)>0$, $af(\alpha)>0$, $af(\beta)>0$, $\alpha < -b/2a < \beta$ |

### Sequences & Series
| Formula | Expression |
|---------|------------|
| AP $n$-th term | $a_n = a + (n-1)d$ |
| AP Sum | $S_n = \frac{n}{2}[2a + (n-1)d]$ |
| GP $n$-th term | $a_n = ar^{n-1}$ |
| GP Sum | $S_n = a\frac{r^n-1}{r-1}$ ($r \neq 1$), $S_\infty = \frac{a}{1-r}$ ($|r|<1$) |
| $\sum k$ | $\frac{n(n+1)}{2}$ |
| $\sum k^2$ | $\frac{n(n+1)(2n+1)}{6}$ |
| $\sum k^3$ | $[\frac{n(n+1)}{2}]^2$ |
| AM $\ge$ GM $\ge$ HM | $\frac{\sum a_i}{n} \ge (\prod a_i)^{1/n} \ge \frac{n}{\sum 1/a_i}$ |
| AGP Sum | $S_n = \frac{a}{1-r} + \frac{dr(1-r^{n-1})}{(1-r)^2} - \frac{[a+(n-1)d]r^n}{1-r}$ |

### Binomial Theorem
| Formula | Expression |
|---------|------------|
| Expansion | $(x+y)^n = \sum_{r=0}^n \binom{n}{r} x^{n-r} y^r$ |
| General Term | $T_{r+1} = \binom{n}{r} x^{n-r} y^r$ |
| Middle Term | $n$ even: $T_{n/2+1}$; $n$ odd: $T_{(n+1)/2}, T_{(n+3)/2}$ |
| Greatest Term | $\frac{T_{r+1}}{T_r} = \frac{n-r+1}{r}|x/y| \ge 1$ |
| Sum of Coeffs | $2^n$ |
| Sum of Odd/Even | $2^{n-1}$ |
| $\sum \binom{n}{r}^2$ | $\binom{2n}{n}$ |
| $\sum r\binom{n}{r}$ | $n2^{n-1}$ |
| $\sum r^2\binom{n}{r}$ | $n(n+1)2^{n-2}$ |

### Permutations & Combinations
| Formula | Expression |
|---------|------------|
| $^nP_r$ | $n!/(n-r)!$ |
| $^nC_r$ | $n!/[r!(n-r)!]$ |
| $^nC_r = ^nC_{n-r}$ | |
| $^nC_r + ^nC_{r-1}$ | $^{n+1}C_r$ |
| Circular Permutations | $(n-1)!$ (if direction matters), $(n-1)!/2$ (if not) |
| Derangements | $D_n = n! \sum_{k=0}^n \frac{(-1)^k}{k!} \approx n!/e$ |
| Distribution (distinct to distinct) | $r^n$ |
| Distribution (identical to distinct) | $^{n+r-1}C_{r-1}$ |
| Onto Functions | $\sum_{k=0}^n (-1)^k \binom{n}{k} (n-k)^m$ |

### Probability
| Formula | Expression |
|---------|------------|
| Conditional | $P(A|B) = P(A \cap B)/P(B)$ |
| Bayes | $P(A_i|B) = \frac{P(B|A_i)P(A_i)}{\sum P(B|A_j)P(A_j)}$ |
| Total Probability | $P(B) = \sum P(B|A_i)P(A_i)$ (partition $\{A_i\}$) |
| Independence | $P(A \cap B) = P(A)P(B)$ |
| Binomial Distribution | $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$ |
| Mean/Variance | $\mu = np$, $\sigma^2 = np(1-p)$ |
| Poisson (approx) | $P(X=k) = e^{-\lambda}\lambda^k/k!$, $\lambda = np$ |

### Matrices & Determinants
| Formula | Expression |
|---------|------------|
| Determinant Properties | $|A^T|=|A|$, $|kA|=k^n|A|$, $|AB|=|A||B|$, $|A^{-1}|=1/|A|$ |
| Adjoint | $A(\text{adj }A) = (\text{adj }A)A = |A|I$ |
| Inverse | $A^{-1} = \text{adj }A / |A|$ |
| $(AB)^{-1}$ | $B^{-1}A^{-1}$ |
| $(A^T)^{-1}$ | $(A^{-1})^T$ |
| Cramer's Rule | $x_i = \Delta_i/\Delta$ |
| Rank | Max order of non-zero minor; $\le \min(m,n)$ |
| Consistency | $AX=B$: consistent iff $\text{rank}(A) = \text{rank}([A|B])$ |
| Eigenvalues | $|A-\lambda I|=0$; sum $=$ trace, product $=$ det |

---

## 📐 Calculus

### Limits & Standard Limits
| Limit | Value |
|-------|-------|
| $\lim_{x\to0} \frac{\sin x}{x}$ | $1$ |
| $\lim_{x\to0} \frac{\tan x}{x}$ | $1$ |
| $\lim_{x\to0} \frac{e^x-1}{x}$ | $1$ |
| $\lim_{x\to0} \frac{\ln(1+x)}{x}$ | $1$ |
| $\lim_{x\to0} \frac{a^x-1}{x}$ | $\ln a$ |
| $\lim_{x\to0} \frac{\log_a(1+x)}{x}$ | $\log_a e$ |
| $\lim_{x\to0} (1+x)^{1/x}$ | $e$ |
| $\lim_{x\to\infty} (1+\frac{1}{x})^x$ | $e$ |

### Derivatives
| Function | Derivative |
|----------|------------|
| $x^n$ | $nx^{n-1}$ |
| $e^x$ | $e^x$ |
| $a^x$ | $a^x \ln a$ |
| $\ln x$ | $1/x$ |
| $\log_a x$ | $1/(x\ln a)$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2 x$ |
| $\sin^{-1} x$ | $1/\sqrt{1-x^2}$ |
| $\cos^{-1} x$ | $-1/\sqrt{1-x^2}$ |
| $\tan^{-1} x$ | $1/(1+x^2)$ |

**Rules:**
- Chain: $\frac{d}{dx} f(g(x)) = f'(g(x)) g'(x)$
- Product: $(uv)' = u'v + uv'$
- Quotient: $(\frac{u}{v})' = \frac{u'v - uv'}{v^2}$
- Parametric: $\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$
- Implicit: Differentiate both sides w.r.t. $x$

### Indefinite Integrals
| Integral | Result |
|----------|--------|
| $\int x^n dx$ | $\frac{x^{n+1}}{n+1} + C$ ($n \neq -1$) |
| $\int \frac{1}{x} dx$ | $\ln|x| + C$ |
| $\int e^x dx$ | $e^x + C$ |
| $\int a^x dx$ | $\frac{a^x}{\ln a} + C$ |
| $\int \sin x dx$ | $-\cos x + C$ |
| $\int \cos x dx$ | $\sin x + C$ |
| $\int \sec^2 x dx$ | $\tan x + C$ |
| $\int \csc^2 x dx$ | $-\cot x + C$ |
| $\int \sec x \tan x dx$ | $\sec x + C$ |
| $\int \csc x \cot x dx$ | $-\csc x + C$ |
| $\int \frac{1}{\sqrt{1-x^2}} dx$ | $\sin^{-1} x + C$ |
| $\int \frac{1}{1+x^2} dx$ | $\tan^{-1} x + C$ |
| $\int \frac{1}{x\sqrt{x^2-1}} dx$ | $\sec^{-1} x + C$ |
| $\int \tan x dx$ | $-\ln|\cos x| + C = \ln|\sec x| + C$ |
| $\int \cot x dx$ | $\ln|\sin x| + C$ |
| $\int \sec x dx$ | $\ln|\sec x + \tan x| + C$ |
| $\int \csc x dx$ | $\ln|\csc x - \cot x| + C$ |

**Special Forms:**
- $\int \frac{f'(x)}{f(x)} dx = \ln|f(x)| + C$
- $\int [f(x)]^n f'(x) dx = \frac{[f(x)]^{n+1}}{n+1} + C$
- $\int e^x [f(x) + f'(x)] dx = e^x f(x) + C$
- By Parts: $\int u dv = uv - \int v du$ (ILATE)

### Definite Integrals Properties
| Property | Formula |
|----------|---------|
| $\int_a^b f(x) dx$ | $F(b) - F(a)$ |
| $\int_a^b f(x) dx$ | $-\int_b^a f(x) dx$ |
| $\int_a^b f(x) dx$ | $\int_a^c f(x) dx + \int_c^b f(x) dx$ |
| Symmetry | $\int_a^b f(x) dx = \int_a^b f(a+b-x) dx$ |
| $\int_{-a}^a f(x) dx$ | $2\int_0^a f(x) dx$ (even), $=0$ (odd) |
| $\int_0^{nT} f(x) dx$ | $n \int_0^T f(x) dx$ (periodic $T$) |
| King's Property | $\int_a^b f(x) dx = \int_a^b f(a+b-x) dx$ |
| Walli's Formula | $\int_0^{\pi/2} \sin^n x dx = \int_0^{\pi/2} \cos^n x dx = \frac{(n-1)!!}{n!!} \cdot K$<br>$K = \pi/2$ if $n$ even, $1$ if $n$ odd |
| Leibniz Rule | $\frac{d}{dx} \int_{\phi(x)}^{\psi(x)} f(t) dt = f(\psi(x))\psi'(x) - f(\phi(x))\phi'(x)$ |

---

## 📐 Coordinate Geometry

### Straight Lines
| Formula | Expression |
|---------|------------|
| Slope | $m = \tan\theta = \frac{y_2-y_1}{x_2-x_1}$ |
| Point-Slope | $y - y_1 = m(x - x_1)$ |
| Two-Point | $\frac{y-y_1}{y_2-y_1} = \frac{x-x_1}{x_2-x_1}$ |
| Intercept | $\frac{x}{a} + \frac{y}{b} = 1$ |
| Normal/Perpendicular | $x\cos\alpha + y\sin\alpha = p$ |
| General | $ax + by + c = 0$; slope $= -a/b$ |
| Distance Point-Line | $\frac{|ax_1+by_1+c|}{\sqrt{a^2+b^2}}$ |
| Distance Parallel Lines | $\frac{|c_1-c_2|}{\sqrt{a^2+b^2}}$ |
| Angle Between Lines | $\tan\theta = \left|\frac{m_1-m_2}{1+m_1m_2}\right|$ |
| Reflection of $(x_1,y_1)$ | $\frac{x-x_1}{a} = \frac{y-y_1}{b} = -\frac{2(ax_1+by_1+c)}{a^2+b^2}$ |
| Family through Intersection | $L_1 + \lambda L_2 = 0$ |

### Circles
| Formula | Expression |
|---------|------------|
| Center-Radius | $(x-h)^2 + (y-k)^2 = r^2$ |
| General | $x^2+y^2+2gx+2fy+c=0$; center $(-g,-f)$, $r=\sqrt{g^2+f^2-c}$ |
| Diameter Form | $(x-x_1)(x-x_2) + (y-y_1)(y-y_2) = 0$ |
| Parametric | $x = h + r\cos\theta$, $y = k + r\sin\theta$ |
| Tangent at $(x_1,y_1)$ | $xx_1+yy_1+g(x+x_1)+f(y+y_1)+c=0$ |
| Tangent $y=mx+c$ | $c = \pm r\sqrt{1+m^2}$ (center at origin) |
| Normal at $(x_1,y_1)$ | $\frac{x-x_1}{x_1+g} = \frac{y-y_1}{y_1+f}$ |
| Chord of Contact | $T = 0$ (same as tangent form with $(x_1,y_1)$ external) |
| Power of Point | $S_1 = x_1^2+y_1^2+2gx_1+2fy_1+c$ |
| Radical Axis | $S_1 - S_2 = 0$ |
| Family of Circles | $S_1 + \lambda S_2 = 0$ |
| Orthogonal Circles | $2g_1g_2 + 2f_1f_2 = c_1 + c_2$ |

### Parabola ($y^2 = 4ax$)
| Formula | Expression |
|---------|------------|
| Focus | $(a,0)$ |
| Directrix | $x = -a$ |
| Vertex | $(0,0)$ |
| Latus Rectum | $4a$ (ends: $(a, \pm 2a)$) |
| Parametric | $(at^2, 2at)$ |
| Tangent at $t$ | $ty = x + at^2$ |
| Tangent at $(x_1,y_1)$ | $yy_1 = 2a(x+x_1)$ |
| Normal at $t$ | $y = -tx + 2at + at^3$ |
| Normal at $(x_1,y_1)$ | $y-y_1 = -\frac{y_1}{2a}(x-x_1)$ |
| Focal Chord | $t_1 t_2 = -1$; length $= a(t_1-t_2)^2$ |
| Chord of Contact | $yy_1 = 2a(x+x_1)$ |
| Pole-Polar | $T=0$ |

### Ellipse ($\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$, $a>b$)
| Formula | Expression |
|---------|------------|
| Eccentricity | $e = \sqrt{1-b^2/a^2}$ |
| Foci | $(\pm ae, 0)$ |
| Directrices | $x = \pm a/e$ |
| Latus Rectum | $2b^2/a$ |
| Parametric | $(a\cos\theta, b\sin\theta)$ |
| Tangent at $\theta$ | $\frac{x\cos\theta}{a} + \frac{y\sin\theta}{b} = 1$ |
| Normal at $\theta$ | $\frac{ax}{\cos\theta} - \frac{by}{\sin\theta} = a^2-b^2$ |
| Director Circle | $x^2 + y^2 = a^2 + b^2$ |
| Auxiliary Circle | $x^2 + y^2 = a^2$ |

### Hyperbola ($\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$)
| Formula | Expression |
|---------|------------|
| Eccentricity | $e = \sqrt{1+b^2/a^2}$ |
| Foci | $(\pm ae, 0)$ |
| Directrices | $x = \pm a/e$ |
| Asymptotes | $y = \pm \frac{b}{a}x$ |
| Conjugate | $\frac{x^2}{a^2} - \frac{y^2}{b^2} = -1$ |
| Rectangular ($xy=c^2$) | $e=\sqrt{2}$, param $(ct, c/t)$ |

---

## 📐 Trigonometry

### Compound Angles
| Formula | Expression |
|---------|------------|
| $\sin(A\pm B)$ | $\sin A\cos B \pm \cos A\sin B$ |
| $\cos(A\pm B)$ | $\cos A\cos B \mp \sin A\sin B$ |
| $\tan(A\pm B)$ | $\frac{\tan A \pm \tan B}{1 \mp \tan A\tan B}$ |
| $\cot(A\pm B)$ | $\frac{\cot A\cot B \mp 1}{\cot B \pm \cot A}$ |

### Multiple Angles
| Formula | Expression |
|---------|------------|
| $\sin 2A$ | $2\sin A\cos A = \frac{2\tan A}{1+\tan^2 A}$ |
| $\cos 2A$ | $\cos^2 A-\sin^2 A = 2\cos^2 A-1 = 1-2\sin^2 A = \frac{1-\tan^2 A}{1+\tan^2 A}$ |
| $\tan 2A$ | $\frac{2\tan A}{1-\tan^2 A}$ |
| $\sin 3A$ | $3\sin A - 4\sin^3 A$ |
| $\cos 3A$ | $4\cos^3 A - 3\cos A$ |
| $\tan 3A$ | $\frac{3\tan A - \tan^3 A}{1-3\tan^2 A}$ |
| $\sin A$ | $2\sin\frac{A}{2}\cos\frac{A}{2} = \frac{2\tan\frac{A}{2}}{1+\tan^2\frac{A}{2}}$ |
| $\cos A$ | $2\cos^2\frac{A}{2}-1 = 1-2\sin^2\frac{A}{2} = \frac{1-\tan^2\frac{A}{2}}{1+\tan^2\frac{A}{2}}$ |
| $\tan A$ | $\frac{2\tan\frac{A}{2}}{1-\tan^2\frac{A}{2}}$ |

### Sum-to-Product / Product-to-Sum
| Formula | Expression |
|---------|------------|
| $\sin C + \sin D$ | $2\sin\frac{C+D}{2}\cos\frac{C-D}{2}$ |
| $\sin C - \sin D$ | $2\cos\frac{C+D}{2}\sin\frac{C-D}{2}$ |
| $\cos C + \cos D$ | $2\cos\frac{C+D}{2}\cos\frac{C-D}{2}$ |
| $\cos C - \cos D$ | $-2\sin\frac{C+D}{2}\sin\frac{C-D}{2}$ |
| $2\sin A\cos B$ | $\sin(A+B) + \sin(A-B)$ |
| $2\cos A\sin B$ | $\sin(A+B) - \sin(A-B)$ |
| $2\cos A\cos B$ | $\cos(A+B) + \cos(A-B)$ |
| $2\sin A\sin B$ | $\cos(A-B) - \cos(A+B)$ |

### Trigonometric Equations (General Solutions)
| Equation | Solution |
|----------|----------|
| $\sin x = \sin \alpha$ | $x = n\pi + (-1)^n \alpha$ |
| $\cos x = \cos \alpha$ | $x = 2n\pi \pm \alpha$ |
| $\tan x = \tan \alpha$ | $x = n\pi + \alpha$ |
| $\sin^2 x = \sin^2 \alpha$ | $x = n\pi \pm \alpha$ |
| $\cos^2 x = \cos^2 \alpha$ | $x = n\pi \pm \alpha$ |
| $\tan^2 x = \tan^2 \alpha$ | $x = n\pi \pm \alpha$ |

### Properties of Triangle
| Formula | Expression |
|---------|------------|
| Sine Rule | $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R$ |
| Cosine Rule | $a^2 = b^2+c^2-2bc\cos A$ |
| Projection | $a = b\cos C + c\cos B$ |
| Napier's | $\tan\frac{B-C}{2} = \frac{b-c}{b+c}\cot\frac{A}{2}$ |
| Area | $\Delta = \frac{1}{2}bc\sin A = \sqrt{s(s-a)(s-b)(s-c)}$ |
| $R$ (Circumradius) | $R = \frac{abc}{4\Delta}$ |
| $r$ (Inradius) | $r = \frac{\Delta}{s}$ |
| $r_1$ (Exradius) | $r_1 = \frac{\Delta}{s-a}$ |
| $\tan\frac{A}{2}$ | $\sqrt{\frac{(s-b)(s-c)}{s(s-a)}}$ |
| $r = 4R\sin\frac{A}{2}\sin\frac{B}{2}\sin\frac{C}{2}$ | |

---

## 📐 Vector & 3D Geometry

### Vectors
| Formula | Expression |
|---------|------------|
| Dot Product | $\vec{a}\cdot\vec{b} = |\vec{a}||\vec{b}|\cos\theta = a_1b_1+a_2b_2+a_3b_3$ |
| Cross Product | $\vec{a}\times\vec{b} = |\vec{a}||\vec{b}|\sin\theta \hat{n}$ |
| $|\vec{a}\times\vec{b}|^2$ | $|\vec{a}|^2|\vec{b}|^2 - (\vec{a}\cdot\vec{b})^2$ |
| Scalar Triple | $[\vec{a}\vec{b}\vec{c}] = \vec{a}\cdot(\vec{b}\times\vec{c})$ |
| Vector Triple | $\vec{a}\times(\vec{b}\times\vec{c}) = (\vec{a}\cdot\vec{c})\vec{b} - (\vec{a}\cdot\vec{b})\vec{c}$ |
| Reciprocal | $\vec{a}^* = \frac{\vec{b}\times\vec{c}}{[\vec{a}\vec{b}\vec{c}]}$ etc. |
| Projection | $\frac{\vec{a}\cdot\vec{b}}{|\vec{b}|}$ |

### 3D Geometry
| Formula | Expression |
|---------|------------|
| Direction Cosines | $l^2+m^2+n^2=1$; $l,m,n = \frac{a,b,c}{\sqrt{a^2+b^2+c^2}}$ |
| Line (Symmetric) | $\frac{x-x_1}{a} = \frac{y-y_1}{b} = \frac{z-z_1}{c}$ |
| Line (Vector) | $\vec{r} = \vec{a} + \lambda \vec{b}$ |
| Plane (General) | $ax+by+cz+d=0$ |
| Plane (Normal) | $\vec{r}\cdot\vec{n} = d$ |
| Plane (Intercept) | $\frac{x}{a}+\frac{y}{b}+\frac{z}{c}=1$ |
| Distance Point-Plane | $\frac{|ax_1+by_1+cz_1+d|}{\sqrt{a^2+b^2+c^2}}$ |
| Distance Point-Line | $\frac{|(\vec{a}-\vec{r}_1)\times\vec{b}|}{|\vec{b}|}$ |
| Angle Line-Plane | $\sin\theta = \frac{|\vec{b}\cdot\vec{n}|}{|\vec{b}||\vec{n}|}$ |
| Angle Plane-Plane | $\cos\theta = \frac{|a_1a_2+b_1b_2+c_1c_2|}{\sqrt{a_1^2+b_1^2+c_1^2}\sqrt{a_2^2+b_2^2+c_2^2}}$ |
| Shortest Distance (Skew) | $\frac{|(\vec{a}_2-\vec{a}_1)\cdot(\vec{b}_1\times\vec{b}_2)|}{|\vec{b}_1\times\vec{b}_2|}$ |
| Image in Plane | $\frac{x-x_1}{a} = \frac{y-y_1}{b} = \frac{z-z_1}{c} = -\frac{2(ax_1+by_1+cz_1+d)}{a^2+b^2+c^2}$ |

---

## 📐 Differential Equations

| Type | Form | Solution Method |
|------|------|-----------------|
| Variable Separable | $f(y)dy = g(x)dx$ | Integrate both sides |
| Homogeneous | $\frac{dy}{dx} = F(\frac{y}{x})$ | Substitute $y = vx$ |
| Linear | $\frac{dy}{dx} + Py = Q$ | IF $= e^{\int P dx}$; $y \cdot IF = \int Q \cdot IF dx + C$ |
| Bernoulli | $\frac{dy}{dx} + Py = Qy^n$ | Divide by $y^n$, substitute $v = y^{1-n}$ |
| Exact | $M dx + N dy = 0$, $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$ | $\int M dx + \int N_{\text{independent}} dy = C$ |
| Clairaut | $y = xp + f(p)$ | Differentiate: $p = p + xp' + f'(p)p' \implies p' = 0$ or $x + f'(p) = 0$ |

---

*Master formula sheet — keep for quick revision before exams. Cross-reference with topic-wise notes for derivations and problem-solving strategies.*