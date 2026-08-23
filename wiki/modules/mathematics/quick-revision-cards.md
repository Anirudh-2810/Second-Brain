---
module: "mathematics"
topic: "Mathematics Quick Revision Cards — Last Minute JEE Advanced"
tags: [mathematics, revision, quick-reference, jee, last-minute]
last_updated: "2026-08-11"
source: "Kota notes, formula sheets, PYQ analysis"
---

# Mathematics Quick Revision Cards — Last Minute JEE Advanced

> Ultra-condensed revision cards for final 48 hours. One card per high-yield topic. Memorize triggers, not derivations.

---

## 🔴 CARD 1: Complex Numbers — Triggers

| See This | Do This |
|----------|---------|
| $|z_1+z_2| = |z_1|+|z_2|$ | Vectors aligned $\implies \arg(z_1) = \arg(z_2)$ |
| $|z_1+z_2| = \||z_1|-|z_2|\|$ | Vectors anti-aligned $\implies \arg(z_1) = \arg(z_2) \pm \pi$ |
| $|z-1| = |z+1|$ | Perpendicular bisector of $(-1,0)$ and $(1,0)$ $\implies$ imaginary axis |
| $|z-z_1| = k|z-z_2|$ ($k>0, k\neq 1$) | Circle (Apollonius) |
| $\arg(z) = \theta$ | Ray from origin (excl. origin) |
| $\arg(\frac{z-z_1}{z-z_2}) = \theta$ | Arc of circle through $z_1, z_2$ subtending $\theta$ |
| $z + \bar{z}$ | $2\Re(z)$ (real) |
| $z - \bar{z}$ | $2i\Im(z)$ (imaginary) |
| Roots of unity $\omega$ | $1+\omega+\omega^2=0$, $\omega^3=1$, $\omega^2 = \bar{\omega}$ |

**Memorize:** Rotation formula: $\frac{z_2-z_1}{z_3-z_1} = \frac{|z_2-z_1|}{|z_3-z_1|} e^{i\theta}$

---

## 🔴 CARD 2: Quadratic Equations — Triggers

| See This | Do This |
|----------|---------|
| "Roots are $\alpha, \beta$" | Write $\alpha+\beta = -b/a$, $\alpha\beta = c/a$ immediately |
| $\alpha^2+\beta^2$ | $(\alpha+\beta)^2 - 2\alpha\beta$ |
| $\alpha^3+\beta^3$ | $(\alpha+\beta)^3 - 3\alpha\beta(\alpha+\beta)$ |
| $\alpha^n+\beta^n$ | Recurrence $S_n = -b/a S_{n-1} - c/a S_{n-2}$ |
| "Common root" | Use $(c_1a_2-c_2a_1)^2 = (a_1b_2-a_2b_1)(b_1c_2-b_2c_1)$ |
| "Both roots in $(\alpha,\beta)$" | Check: $f(\alpha)f(\beta)>0$, $af(\alpha)>0$, $af(\beta)>0$, $\alpha < -b/2a < \beta$ |
| "Exactly one root in $(\alpha,\beta)$" | $f(\alpha)f(\beta) < 0$ |
| "Roots of opposite signs" | $\alpha\beta < 0 \implies c/a < 0$ |
| "Both roots positive" | $\alpha+\beta > 0$, $\alpha\beta > 0$, $D \ge 0$ |

---

## 🔴 CARD 3: Sequences & Series — Triggers

| See This | Do This |
|----------|---------|
| $\sum n$ | $n(n+1)/2$ |
| $\sum n^2$ | $n(n+1)(2n+1)/6$ |
| $\sum n^3$ | $[n(n+1)/2]^2$ |
| AP sum | $n/2 \times (\text{first} + \text{last})$ |
| GP sum | $a(r^n-1)/(r-1)$ |
| "Find $n$ from sum" | Solve quadratic |
| AM-GM | $(\sum a_i)/n \ge (\prod a_i)^{1/n}$ — equality when all equal |
| HP | Reciprocals form AP |
| AGP | $S_n = \frac{a}{1-r} + \frac{dr(1-r^{n-1})}{(1-r)^2} - \frac{[a+(n-1)d]r^n}{1-r}$ |

---

## 🔴 CARD 4: Binomial Theorem — Triggers

| See This | Do This |
|----------|---------|
| General term | $T_{r+1} = \binom{n}{r} x^{n-r} y^r$ |
| Middle term | $n$ even: 1 middle; $n$ odd: 2 middle |
| Greatest term | Compare $T_{r+1}/T_r = \frac{n-r+1}{r}|x/y|$ with 1 |
| Coefficient sum | Put $x=1$ |
| Odd/Even sum | $(f(1) \pm f(-1))/2$ |
| $\sum \binom{n}{r}^2$ | $\binom{2n}{n}$ |
| $\sum r\binom{n}{r}$ | $n2^{n-1}$ |
| $\sum r(r-1)\binom{n}{r}$ | $n(n-1)2^{n-2}$ |

---

## 🔴 CARD 5: P&C / Probability — Triggers

| See This | Do This |
|----------|---------|
| "Arrange in circle" | $(n-1)!$ (or $(n-1)!/2$ if necklace) |
| "No two together" | Gap method: arrange others, choose gaps |
| Derangements | $D_n = n! \sum (-1)^k/k! \approx n!/e$ |
| Inclusion-Exclusion | $n(A \cup B) = n(A) + n(B) - n(A \cap B)$ |
| Bayes | $P(A|B) = \frac{P(B|A)P(A)}{P(B|A)P(A) + P(B|\bar{A})P(\bar{A})}$ |
| Total Probability | $P(B) = \sum P(B|A_i)P(A_i)$ |
| Binomial | $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$ |
| Mean/Var (Binomial) | $\mu = np$, $\sigma^2 = np(1-p)$ |
| "At least one" | $1 - P(\text{none})$ |

---

## 🔴 CARD 6: Matrices & Determinants — Triggers

| See This | Do This |
|----------|---------|
| $|AB|$ | $|A||B|$ |
| $|kA|$ | $k^n|A|$ |
| $|\text{adj }A|$ | $|A|^{n-1}$ |
| $A^{-1}$ | $\text{adj }A / |A|$ (only if $|A| \neq 0$) |
| $(AB)^{-1}$ | $B^{-1}A^{-1}$ |
| $(A^T)^{-1}$ | $(A^{-1})^T$ |
| Cramer's Rule | $x_i = \Delta_i/\Delta$ |
| System $AX=B$ | Consistent iff $\text{rank}(A) = \text{rank}([A|B])$ |
| Eigenvalues | $|A-\lambda I|=0$; sum = trace, product = det |

---

## 🔴 CARD 7: Limits & Continuity — Triggers

| See This | Do This |
|----------|---------|
| $0/0$ or $\infty/\infty$ | L'Hôpital: $\lim f/g = \lim f'/g'$ |
| $\lim \frac{\sin x}{x}$ | $1$ (x in radians) |
| $\lim \frac{\tan x}{x}$ | $1$ |
| $\lim \frac{e^x-1}{x}$ | $1$ |
| $\lim \frac{\ln(1+x)}{x}$ | $1$ |
| $\lim \frac{a^x-1}{x}$ | $\ln a$ |
| $\lim (1+x)^{1/x}$ | $e$ |
| $\lim_{x\to0} \frac{\sin^{-1}x}{x}$ | $1$ |
| $\lim_{x\to0} \frac{\tan^{-1}x}{x}$ | $1$ |

---

## 🔴 CARD 8: Application of Derivatives — Triggers

| See This | Do This |
|----------|---------|
| Tangent at $(x_1,y_1)$ | $y - y_1 = f'(x_1)(x - x_1)$ |
| Normal at $(x_1,y_1)$ | $y - y_1 = -\frac{1}{f'(x_1)}(x - x_1)$ |
| Max/Min | $f'(c)=0$; $f''(c)<0 \to$ max, $f''(c)>0 \to$ min |
| Monotonic | $f'(x)>0$ inc, $f'(x)<0$ dec |
| Point of Inflection | $f''(c)=0$ and sign change |
| Rolle's Theorem | $f(a)=f(b) \implies \exists c: f'(c)=0$ |
| LMVT | $\exists c: f'(c) = \frac{f(b)-f(a)}{b-a}$ |
| Approximation | $f(x+\Delta x) \approx f(x) + f'(x)\Delta x$ |

---

## 🔴 CARD 9: Indefinite Integration — Triggers

| See This | Do This |
|----------|---------|
| $\int \frac{f'(x)}{f(x)} dx$ | $\ln|f(x)| + C$ |
| $\int [f(x)]^n f'(x) dx$ | $\frac{[f(x)]^{n+1}}{n+1} + C$ |
| $\int e^x[f(x)+f'(x)] dx$ | $e^x f(x) + C$ |
| $\int \tan x dx$ | $\ln|\sec x| + C$ |
| $\int \sec x dx$ | $\ln|\sec x + \tan x| + C$ |
| By Parts (ILATE) | Inverse → Log → Algebraic → Trig → Exponential |
| Substitution | $\int f(g(x))g'(x) dx = \int f(u) du$ |

---

## 🔴 CARD 10: Definite Integration — Triggers

| See This | Do This |
|----------|---------|
| King's Property | $\int_a^b f(x) dx = \int_a^b f(a+b-x) dx$ |
| Even Function | $\int_{-a}^a f(x) dx = 2\int_0^a f(x) dx$ |
| Odd Function | $\int_{-a}^a f(x) dx = 0$ |
| Periodic $T$ | $\int_0^{nT} f(x) dx = n\int_0^T f(x) dx$ |
| Walli's Formula | $\int_0^{\pi/2} \sin^n x dx = \int_0^{\pi/2} \cos^n x dx = \frac{(n-1)!!}{n!!} \times K$ |
| Leibniz Rule | $\frac{d}{dx}\int_{\phi(x)}^{\psi(x)} f(t) dt = f(\psi(x))\psi'(x) - f(\phi(x))\phi'(x)$ |

---

## 🔴 CARD 11: Area Under Curves — Triggers

| See This | Do This |
|----------|---------|
| Area above x-axis | $\int f(x) dx$ |
| Area below x-axis | $-\int f(x) dx$ |
| Between $y=f(x)$ and $y=g(x)$ | $\int |f(x)-g(x)| dx$ |
| Symmetric about y-axis | $2 \times$ (right half) |
| Symmetric about origin | $0$ |

---

## 🔴 CARD 12: Differential Equations — Triggers

| See This | Do This |
|----------|---------|
| $f(y)dy = g(x)dx$ | Variable separable: integrate both sides |
| $\frac{dy}{dx} = F(y/x)$ | Homogeneous: put $y = vx$ |
| $\frac{dy}{dx} + Py = Q$ | Linear: IF $= e^{\int P dx}$ |
| $\frac{dy}{dx} + Py = Qy^n$ | Bernoulli: divide by $y^n$, put $v = y^{1-n}$ |
| $M dx + N dy = 0$, $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$ | Exact: $\int M dx + \int N_{\text{ind}} dy = C$ |
| $y = xp + f(p)$ | Clairaut: differentiate w.r.t. x |

---

## 🔴 CARD 13: Straight Lines — Triggers

| See This | Do This |
|----------|---------|
| Distance from $(x_1,y_1)$ to $ax+by+c=0$ | $\frac{|ax_1+by_1+c|}{\sqrt{a^2+b^2}}$ |
| Angle between lines | $\tan\theta = \left|\frac{m_1-m_2}{1+m_1m_2}\right|$ |
| Family through intersection | $L_1 + \lambda L_2 = 0$ |
| Reflection of point | $\frac{x-x_1}{a} = \frac{y-y_1}{b} = -\frac{2(ax_1+by_1+c)}{a^2+b^2}$ |
| Distance between parallels | $\frac{|c_1-c_2|}{\sqrt{a^2+b^2}}$ |

---

## 🔴 CARD 14: Circles — Triggers

| See This | Do This |
|----------|---------|
| Center from $x^2+y^2+2gx+2fy+c=0$ | $(-g, -f)$ |
| Radius | $\sqrt{g^2+f^2-c}$ |
| Tangent at $(x_1,y_1)$ | $xx_1+yy_1+g(x+x_1)+f(y+y_1)+c=0$ |
| Power of Point | $S_1 = x_1^2+y_1^2+2gx_1+2fy_1+c$ |
| Radical Axis | $S_1 - S_2 = 0$ |
| Family of Circles | $S_1 + \lambda S_2 = 0$ |
| Orthogonal Circles | $2g_1g_2 + 2f_1f_2 = c_1 + c_2$ |

---

## 🔴 CARD 15: Conic Sections — Triggers

### Parabola ($y^2=4ax$)
| See This | Do This |
|----------|---------|
| Focus | $(a,0)$ |
| Tangent at $t$ | $ty = x + at^2$ |
| Normal at $t$ | $y = -tx + 2at + at^3$ |
| Focal Chord | $t_1 t_2 = -1$ |
| Latus Rectum | $4a$ |

### Ellipse ($x^2/a^2 + y^2/b^2 = 1$)
| See This | Do This |
|----------|---------|
| Eccentricity | $e = \sqrt{1-b^2/a^2}$ |
| Tangent at $\theta$ | $\frac{x\cos\theta}{a} + \frac{y\sin\theta}{b} = 1$ |
| Director Circle | $x^2 + y^2 = a^2 + b^2$ |

### Hyperbola ($x^2/a^2 - y^2/b^2 = 1$)
| See This | Do This |
|----------|---------|
| Eccentricity | $e = \sqrt{1+b^2/a^2}$ |
| Asymptotes | $y = \pm \frac{b}{a}x$ |
| Rectangular ($xy=c^2$) | $e = \sqrt{2}$, param $(ct, c/t)$ |

---

## 🔴 CARD 16: Trigonometry — Triggers

| See This | Do This |
|----------|---------|
| $\sin(A\pm B)$, $\cos(A\pm B)$ | Use compound angle formulas |
| $\sin 2A$, $\cos 2A$, $\tan 2A$ | Double angle |
| $\sin C + \sin D$ | $2\sin\frac{C+D}{2}\cos\frac{C-D}{2}$ |
| $\sin x = \sin \alpha$ | $x = n\pi + (-1)^n\alpha$ |
| $\cos x = \cos \alpha$ | $x = 2n\pi \pm \alpha$ |
| $\tan x = \tan \alpha$ | $x = n\pi + \alpha$ |
| $A+B+C=\pi$ | $\tan A+\tan B+\tan C = \tan A\tan B\tan C$ |
| $\tan^{-1} x + \tan^{-1} y$ | $\tan^{-1}\frac{x+y}{1-xy}$ |

---

## 🔴 CARD 17: Vectors & 3D — Triggers

| See This | Do This |
|----------|---------|
| $[\vec{a}\vec{b}\vec{c}]$ | Volume of parallelepiped |
| $\vec{a}\times(\vec{b}\times\vec{c})$ | $(\vec{a}\cdot\vec{c})\vec{b} - (\vec{a}\cdot\vec{b})\vec{c}$ |
| Shortest distance (skew) | $\frac{|(\vec{a}_2-\vec{a}_1)\cdot(\vec{b}_1\times\vec{b}_2)|}{|\vec{b}_1\times\vec{b}_2|}$ |
| Distance point-plane | $\frac{|ax_1+by_1+cz_1+d|}{\sqrt{a^2+b^2+c^2}}$ |
| Angle line-plane | $\sin\theta = \frac{|\vec{b}\cdot\vec{n}|}{|\vec{b}||\vec{n}|}$ |
| Line $\frac{x-x_1}{a}=\frac{y-y_1}{b}=\frac{z-z_1}{c}$ | Direction $(a,b,c)$ |
| Plane $ax+by+cz+d=0$ | Normal $(a,b,c)$ |

---

## 🔴 CARD 18: Last 24 Hours Checklist

### Must Memorize (Write Once)
- [ ] Walli's Formula ($n$ even/odd cases)
- [ ] King's Property + Even/Odd symmetry
- [ ] Complex number rotation formula
- [ ] Quadratic recurrence $S_n = -b/a S_{n-1} - c/a S_{n-2}$
- [ ] $\tan A+\tan B+\tan C = \tan A\tan B\tan C$
- [ ] Derangements $D_n = n!/e$
- [ ] Eigenvalue sum = trace, product = det
- [ ] $\int_0^{\pi/2} \sin^n x dx$ formula
- [ ] Binomial greatest term comparison
- [ ] Conic section: focus, directrix, tangent, normal for all 3

### Must Practice (1 Problem Each)
- [ ] Area between curves (2 curves)
- [ ] Differential equation (linear, homogeneous, exact)
- [ ] Bayes theorem word problem
- [ ] Complex number geometry (circle/line)
- [ ] Vector triple product
- [ ] Shortest distance skew lines
- [ ] Tangent/normal to conics
- [ ] Definite integral with King's property

### Quick Scan (5 min each)
- [ ] Formula sheet master
- [ ] Trigonometry formula sheet
- [ ] Standard limits
- [ ] Standard derivatives/integrals

---

*Keep this file open during final revision. One card per topic = complete coverage.*