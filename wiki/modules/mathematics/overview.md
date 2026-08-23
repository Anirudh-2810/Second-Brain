---
module: "mathematics"
topic: "Mathematics — JEE Advanced / IIT Level Complete Reference"
tags: [mathematics, jee, iit, algebra, calculus, coordinate, trigonometry, vectors, formulas]
last_updated: "2026-08-11"
source: "/raw-sources/math/ (Algebra, Calculus, Coordinate, Trigonometry, Vector 3D, Math IIT Kota notes, Formula sheets)"
---

# Mathematics — JEE Advanced / IIT Level Complete Reference

> Comprehensive topic-wise notes distilled from Kota classroom notes, formula sheets, and practice materials. Covers entire JEE Advanced syllabus with proofs, derivations, shortcuts, and problem-solving strategies.

---

## 📚 Module Structure

| Section | Topics | Pages |
|---------|--------|-------|
| **Algebra** | Complex Numbers, Quadratic Equations, Sequences & Series, Binomial Theorem, Permutations & Combinations, Probability, Matrices & Determinants | 8 |
| **Calculus** | Functions, Limits & Continuity, Differentiability, Application of Derivatives, Indefinite Integration, Definite Integration, Area Under Curves, Differential Equations | 8 |
| **Coordinate Geometry** | Straight Lines, Circles, Parabola, Ellipse, Hyperbola | 5 |
| **Trigonometry** | Ratios & Identities, Trigonometric Equations, Properties of Triangles | 3 |
| **Vector & 3D Geometry** | Vectors, 3D Geometry | 2 |
| **Formula Sheets** | Complete formula reference, Trigonometric formulas, Quick revision cards | 3 |

---

## 🎯 Algebra

### 1. Complex Numbers
**Key Concepts:** Argand plane, modulus-argument form, Euler's form $z = re^{i\theta}$, De Moivre's theorem, roots of unity, rotation, geometry of complex numbers.

**Critical Formulas:**
- $|z| = \sqrt{a^2 + b^2}$, $\arg(z) = \tan^{-1}(b/a)$
- $z_1 z_2 = r_1 r_2 e^{i(\theta_1 + \theta_2)}$, $z_1/z_2 = (r_1/r_2) e^{i(\theta_1 - \theta_2)}$
- Cube roots of unity: $1, \omega, \omega^2$ where $\omega = e^{2\pi i/3}$, $1+\omega+\omega^2=0$, $\omega^3=1$
- Rotation: $z_2 - z_1 = |z_2 - z_1| e^{i\theta}$ rotates $z_1$ to $z_2$ by $\theta$

**JEE Traps:** Principal argument range $(-\pi, \pi]$, $|z_1 + z_2|^2 + |z_1 - z_2|^2 = 2(|z_1|^2 + |z_2|^2)$ (parallelogram law)

### 2. Quadratic Equations
**Key Concepts:** Nature of roots (discriminant $D = b^2 - 4ac$), relation between roots and coefficients ($\alpha+\beta = -b/a$, $\alpha\beta = c/a$), symmetric functions, common roots, location of roots.

**Critical Formulas:**
- $\alpha^n + \beta^n$ recurrence: $S_n = -b S_{n-1}/a - c S_{n-2}/a$
- Common root condition: $(c_1 a_2 - c_2 a_1)^2 = (a_1 b_2 - a_2 b_1)(b_1 c_2 - b_2 c_1)$
- Location: Both roots in $(\alpha, \beta)$ iff $f(\alpha)f(\beta) > 0$, $af(\alpha) > 0$, $af(\beta) > 0$, $\alpha < -b/2a < \beta$

### 3. Sequences & Series
**Key Concepts:** AP, GP, HP, AGP, summation of series ($\sum n, \sum n^2, \sum n^3$), special series, AM-GM-HM inequality.

**Critical Formulas:**
- $S_n^{AP} = \frac{n}{2}[2a + (n-1)d]$, $S_n^{GP} = a\frac{r^n - 1}{r - 1}$
- $\sum_{k=1}^n k = \frac{n(n+1)}{2}$, $\sum k^2 = \frac{n(n+1)(2n+1)}{6}$, $\sum k^3 = [\frac{n(n+1)}{2}]^2$
- AM $\ge$ GM $\ge$ HM: $\frac{a_1 + \dots + a_n}{n} \ge \sqrt[n]{a_1 \dots a_n} \ge \frac{n}{\frac{1}{a_1} + \dots + \frac{1}{a_n}}$

### 4. Binomial Theorem
**Key Concepts:** General term $T_{r+1} = \binom{n}{r} x^{n-r} y^r$, middle term, greatest coefficient/term, binomial coefficients properties, multinomial theorem.

**Critical Formulas:**
- $(1+x)^n = \sum_{r=0}^n \binom{n}{r} x^r$
- Sum of coefficients: $2^n$, sum of odd/even: $2^{n-1}$
- Greatest term: $\frac{T_{r+1}}{T_r} = \frac{n-r+1}{r} |x| \ge 1$
- $\binom{n}{0}^2 + \binom{n}{1}^2 + \dots + \binom{n}{n}^2 = \binom{2n}{n}$

### 5. Permutations & Combinations
**Key Concepts:** Fundamental principle, circular permutations, derangements, inclusion-exclusion, distribution of identical/distinct objects.

**Critical Formulas:**
- $^nP_r = \frac{n!}{(n-r)!}$, $^nC_r = \frac{n!}{r!(n-r)!}$
- Circular: $(n-1)!$ (clockwise ≠ anticlockwise)
- Derangement: $D_n = n! \sum_{k=0}^n \frac{(-1)^k}{k!}$
- Number of onto functions: $n^m - \binom{n}{1}(n-1)^m + \binom{n}{2}(n-2)^m - \dots$

### 6. Probability
**Key Concepts:** Conditional probability, Bayes' theorem, independent events, total probability, binomial distribution, random variables, expectation, variance.

**Critical Formulas:**
- $P(A|B) = \frac{P(A \cap B)}{P(B)}$, Bayes: $P(A_i|B) = \frac{P(B|A_i)P(A_i)}{\sum P(B|A_j)P(A_j)}$
- $P(A \cup B) = P(A) + P(B) - P(A \cap B)$
- Binomial: $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$, $E[X] = np$, $Var[X] = np(1-p)$

### 7. Matrices & Determinants
**Key Concepts:** Matrix operations, inverse, rank, system of equations (Cramer's rule, matrix method), eigenvalues/eigenvectors (intro), determinant properties.

**Critical Formulas:**
- $|AB| = |A||B|$, $|A^T| = |A|$, $|kA| = k^n |A|$
- $A^{-1} = \frac{\text{adj } A}{|A|}$, $(AB)^{-1} = B^{-1}A^{-1}$
- Cramer's rule: $x_i = \frac{\Delta_i}{\Delta}$ where $\Delta_i$ replaces $i$-th column with constants
- Rank: Number of non-zero rows in row-echelon form

---

## 🎯 Calculus

### 1. Functions
**Key Concepts:** Domain, range, types (polynomial, rational, trigonometric, exponential, logarithmic, piecewise), composite, inverse, even/odd, periodic, boundedness, monotonicity.

**Critical Formulas:**
- $f \circ g (x) = f(g(x))$, $(f \circ g)^{-1} = g^{-1} \circ f^{-1}$
- Even: $f(-x) = f(x)$, Odd: $f(-x) = -f(x)$
- Period of $a \sin(bx+c)$ or $a \cos(bx+c)$ is $\frac{2\pi}{|b|}$

### 2. Limits, Continuity & Differentiability
**Key Concepts:** Limit algebra, indeterminate forms (L'Hôpital's rule), standard limits, continuity at a point/interval, differentiability, left/right derivatives.

**Critical Formulas:**
- $\lim_{x \to 0} \frac{\sin x}{x} = 1$, $\lim_{x \to 0} \frac{\tan x}{x} = 1$, $\lim_{x \to 0} \frac{e^x - 1}{x} = 1$, $\lim_{x \to 0} \frac{\ln(1+x)}{x} = 1$
- L'Hôpital: $\lim \frac{f}{g} = \lim \frac{f'}{g'}$ for $0/0$ or $\infty/\infty$
- Continuity: $\lim_{x \to c} f(x) = f(c)$
- Differentiability $\implies$ Continuity (converse false)

### 3. Application of Derivatives (AOD)
**Key Concepts:** Rate of change, tangents/normals, monotonicity, maxima/minima (first/second derivative test), Rolle's theorem, LMVT, approximations.

**Critical Formulas:**
- Tangent: $y - y_1 = f'(x_1)(x - x_1)$, Normal: $y - y_1 = -\frac{1}{f'(x_1)}(x - x_1)$
- Monotonic: $f'(x) > 0$ increasing, $f'(x) < 0$ decreasing
- Max/Min: $f'(c) = 0$, $f''(c) < 0 \to$ max, $f''(c) > 0 \to$ min
- Rolle's: $f(a)=f(b) \implies \exists c \in (a,b): f'(c)=0$
- LMVT: $\exists c \in (a,b): f'(c) = \frac{f(b)-f(a)}{b-a}$

### 4. Indefinite Integration
**Key Concepts:** Standard integrals, substitution, integration by parts ($\int uv = u\int v - \int u'(\int v)$), partial fractions, trigonometric integrals, special forms.

**Critical Formulas:**
- $\int x^n = \frac{x^{n+1}}{n+1} + C$, $\int e^x = e^x + C$, $\int \frac{1}{x} = \ln|x| + C$
- $\int \sin x = -\cos x + C$, $\int \cos x = \sin x + C$, $\int \sec^2 x = \tan x + C$
- By parts: ILATE rule (Inverse, Log, Algebraic, Trig, Exponential)
- $\int \frac{f'(x)}{f(x)} = \ln|f(x)| + C$, $\int [f(x)]^n f'(x) = \frac{[f(x)]^{n+1}}{n+1} + C$

### 5. Definite Integration
**Key Concepts:** Fundamental theorem, properties (symmetry, periodicity, King's property $\int_a^b f(x) dx = \int_a^b f(a+b-x) dx$), Leibniz rule, reduction formulas.

**Critical Formulas:**
- $\int_a^b f(x) dx = F(b) - F(a)$ where $F' = f$
- $\int_a^b f(x) dx = \int_a^b f(a+b-x) dx$
- $\int_{-a}^a f(x) dx = 2\int_0^a f(x) dx$ (even), $=0$ (odd)
- $\int_0^{\pi/2} \sin^n x dx = \int_0^{\pi/2} \cos^n x dx = \frac{(n-1)!!}{n!!} \times \begin{cases} \pi/2 & n \text{ even} \\ 1 & n \text{ odd} \end{cases}$
- Leibniz: $\frac{d}{dx} \int_{\phi(x)}^{\psi(x)} f(t) dt = f(\psi(x))\psi'(x) - f(\phi(x))\phi'(x)$

### 6. Area Under Curves
**Key Concepts:** Area between curve and axis, area between two curves, area bounded by closed curves, area with inequalities.

**Critical Formulas:**
- Area = $\int_a^b |f(x)| dx$ (above x-axis: $\int f(x) dx$, below: $-\int f(x) dx$)
- Between $y=f(x)$ and $y=g(x)$: $\int_a^b |f(x) - g(x)| dx$
- With $x = f(y)$: $\int_c^d |f(y)| dy$

### 7. Differential Equations
**Key Concepts:** Order, degree, formation, variable separable, homogeneous, linear ($\frac{dy}{dx} + Py = Q$), exact, Bernoulli, Clairaut.

**Critical Formulas:**
- Variable separable: $\int f(y) dy = \int g(x) dx + C$
- Homogeneous: substitute $y = vx$
- Linear: IF $= e^{\int P dx}$, solution: $y \cdot IF = \int Q \cdot IF dx + C$
- Exact: $M dx + N dy = 0$ exact if $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$

---

## 🎯 Coordinate Geometry

### 1. Straight Lines
**Key Concepts:** Slope, intercepts, general form, distance from point to line, angle between lines, family of lines, concurrency, image/reflection.

**Critical Formulas:**
- Slope: $m = \tan \theta = \frac{y_2 - y_1}{x_2 - x_1}$
- Distance: $d = \frac{|ax_1 + by_1 + c|}{\sqrt{a^2 + b^2}}$
- Angle: $\tan \theta = \left|\frac{m_1 - m_2}{1 + m_1 m_2}\right|$
- Family: $L_1 + \lambda L_2 = 0$ (lines through intersection)
- Reflection of $(x_1, y_1)$ about $ax+by+c=0$:
  $\frac{x - x_1}{a} = \frac{y - y_1}{b} = -\frac{2(ax_1 + by_1 + c)}{a^2 + b^2}$

### 2. Circles
**Key Concepts:** Standard/central/parametric forms, chord, tangent, normal, power of point, radical axis, family of circles, orthogonal circles.

**Critical Formulas:**
- Center-radius: $(x-h)^2 + (y-k)^2 = r^2$
- General: $x^2 + y^2 + 2gx + 2fy + c = 0$, center $(-g, -f)$, $r = \sqrt{g^2 + f^2 - c}$
- Tangent at $(x_1, y_1)$: $xx_1 + yy_1 + g(x+x_1) + f(y+y_1) + c = 0$
- Power of point $P(x_1, y_1)$: $S_1 = x_1^2 + y_1^2 + 2gx_1 + 2fy_1 + c$
- Radical axis: $S_1 - S_2 = 0$

### 3. Parabola
**Key Concepts:** Standard forms ($y^2=4ax$, $x^2=4ay$, etc.), parametric $(at^2, 2at)$, tangent, normal, chord, focal chord, latus rectum, pole-polar.

**Critical Formulas:**
- Tangent at $t$: $ty = x + at^2$; at $(x_1, y_1)$: $yy_1 = 2a(x+x_1)$
- Normal at $t$: $y = -tx + 2at + at^3$; at $(x_1, y_1)$: $y - y_1 = -\frac{y_1}{2a}(x - x_1)$
- Focal chord: $t_1 t_2 = -1$; length $= a(t_2 - t_1)^2$
- Chord of contact from $(x_1, y_1)$: $yy_1 = 2a(x+x_1)$

### 4. Ellipse
**Key Concepts:** Standard form $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$, parametric $(a\cos\theta, b\sin\theta)$, tangent, normal, chord, auxiliary circle, director circle.

**Critical Formulas:**
- Eccentricity: $e = \sqrt{1 - \frac{b^2}{a^2}}$ ($a > b$)
- Foci: $(\pm ae, 0)$, Directrices: $x = \pm a/e$
- Tangent at $\theta$: $\frac{x\cos\theta}{a} + \frac{y\sin\theta}{b} = 1$
- Normal at $\theta$: $\frac{ax}{\cos\theta} - \frac{by}{\sin\theta} = a^2 - b^2$
- Director circle: $x^2 + y^2 = a^2 + b^2$

### 5. Hyperbola
**Key Concepts:** Standard form $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$, parametric $(a\sec\theta, b\tan\theta)$, rectangular hyperbola $xy = c^2$, asymptotes, conjugate hyperbola.

**Critical Formulas:**
- Eccentricity: $e = \sqrt{1 + \frac{b^2}{a^2}}$
- Foci: $(\pm ae, 0)$, Directrices: $x = \pm a/e$
- Asymptotes: $y = \pm \frac{b}{a}x$; combined: $\frac{x^2}{a^2} - \frac{y^2}{b^2} = 0$
- Rectangular hyperbola $xy = c^2$: parametric $(ct, c/t)$, $e = \sqrt{2}$

---

## 🎯 Trigonometry

### 1. Ratios & Identities
**Key Concepts:** Compound angles, multiple/sub-multiple angles, sum-to-product, product-to-sum, conditional identities, trigonometric inequalities.

**Critical Formulas:**
- $\sin(A \pm B) = \sin A \cos B \pm \cos A \sin B$
- $\cos(A \pm B) = \cos A \cos B \mp \sin A \sin B$
- $\tan(A \pm B) = \frac{\tan A \pm \tan B}{1 \mp \tan A \tan B}$
- $\sin 2A = 2\sin A \cos A$, $\cos 2A = \cos^2 A - \sin^2 A = 2\cos^2 A - 1 = 1 - 2\sin^2 A$
- $\sin 3A = 3\sin A - 4\sin^3 A$, $\cos 3A = 4\cos^3 A - 3\cos A$
- $\sin C + \sin D = 2 \sin\frac{C+D}{2} \cos\frac{C-D}{2}$

### 2. Trigonometric Equations
**Key Concepts:** Principal/general solutions, standard equations ($\sin x = a$, $\cos x = a$, $\tan x = a$), quadratic in trig functions, factorizable equations.

**Critical Formulas:**
- General solutions: $\sin x = \sin \alpha \implies x = n\pi + (-1)^n \alpha$
- $\cos x = \cos \alpha \implies x = 2n\pi \pm \alpha$
- $\tan x = \tan \alpha \implies x = n\pi + \alpha$

### 3. Properties of Triangles
**Key Concepts:** Sine rule, cosine rule, projection rule, half-angle formulas, area, circumcircle/incircle/excircles, Napier's analogy, Apollonius theorem.

**Critical Formulas:**
- Sine rule: $\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R$
- Cosine rule: $a^2 = b^2 + c^2 - 2bc\cos A$
- Area: $\Delta = \frac{1}{2}bc\sin A = \sqrt{s(s-a)(s-b)(s-c)}$ (Heron)
- $r = \frac{\Delta}{s}$, $R = \frac{abc}{4\Delta}$, $r_1 = \frac{\Delta}{s-a}$ (exradius)
- $\tan \frac{A}{2} = \sqrt{\frac{(s-b)(s-c)}{s(s-a)}}$

---

## 🎯 Vector & 3D Geometry

### 1. Vectors
**Key Concepts:** Types, addition, scalar/dot product, vector/cross product, scalar triple product, vector triple product, reciprocal basis, vector equations of line/plane.

**Critical Formulas:**
- Dot: $\vec{a} \cdot \vec{b} = |\vec{a}||\vec{b}|\cos\theta = a_1b_1 + a_2b_2 + a_3b_3$
- Cross: $\vec{a} \times \vec{b} = |\vec{a}||\vec{b}|\sin\theta \hat{n}$; $|\vec{a} \times \vec{b}|^2 = |\vec{a}|^2|\vec{b}|^2 - (\vec{a} \cdot \vec{b})^2$
- Scalar triple: $[\vec{a} \vec{b} \vec{c}] = \vec{a} \cdot (\vec{b} \times \vec{c})$ = volume of parallelepiped
- Vector triple: $\vec{a} \times (\vec{b} \times \vec{c}) = (\vec{a} \cdot \vec{c})\vec{b} - (\vec{a} \cdot \vec{b})\vec{c}$
- Projection of $\vec{a}$ on $\vec{b}$: $\frac{\vec{a} \cdot \vec{b}}{|\vec{b}|}$

### 2. 3D Geometry
**Key Concepts:** Direction cosines/ratios, line equations (vector/cartesian/symmetric), plane equations, angle between line/plane, distance point-to-plane/line, intersection, image/reflection.

**Critical Formulas:**
- Direction cosines: $l^2 + m^2 + n^2 = 1$; $l,m,n = \frac{a,b,c}{\sqrt{a^2+b^2+c^2}}$
- Line through $(x_1,y_1,z_1)$ with direction $(a,b,c)$: $\frac{x-x_1}{a} = \frac{y-y_1}{b} = \frac{z-z_1}{c}$
- Plane: $ax + by + cz + d = 0$ or $\vec{r} \cdot \vec{n} = d$
- Distance point $(x_1,y_1,z_1)$ to plane: $\frac{|ax_1 + by_1 + cz_1 + d|}{\sqrt{a^2+b^2+c^2}}$
- Angle between planes: $\cos \theta = \frac{|a_1a_2 + b_1b_2 + c_1c_2|}{\sqrt{a_1^2+b_1^2+c_1^2}\sqrt{a_2^2+b_2^2+c_2^2}}$
- Shortest distance between skew lines: $\frac{|(\vec{a}_2 - \vec{a}_1) \cdot (\vec{b}_1 \times \vec{b}_2)|}{|\vec{b}_1 \times \vec{b}_2|}$

---

## 📐 Formula Sheets

### Complete Formula Sheet (Master)
See: [[mathematics/formula-sheet-master]]

### Trigonometric Formula Sheet
See: [[mathematics/formula-sheet-trigonometry]]

### Quick Revision Cards (Last Minute)
See: [[mathematics/quick-revision-cards]]

---

## 🔗 Cross-References

- **Physics**: Vectors (mechanics), Calculus (kinematics, EM), Complex numbers (AC circuits)
- **Chemistry**: Logarithms (kinetics, pH), Matrices (quantum), Probability (statistical mechanics)
- **Quant Finance**: Calculus (stochastic), Linear algebra (portfolio), Probability (risk)

---

## 📖 Source Registry

| Source File | Type | Topics Covered |
|-------------|------|----------------|
| `/raw-sources/math/Algebra-.../Algebra/*.pdf` | Notes | Basic Maths, Binomial, Complex, Matrices, P&C, Probability, Quadratic, Sequence |
| `/raw-sources/math/Calculus-.../Calculus/*.pdf` | Notes | AOD, Area, Definite/Indefinite Integration, DE, Functions, Inverse Trig, LCD |
| `/raw-sources/math/Coordinate-.../Coordinate/*.pdf` | Notes | Circles, Ellipse, Hyperbola, Parabola, Straight Lines |
| `/raw-sources/math/Trigonometry-.../Trigonometry/*.pdf` | Notes | Triangle Properties, Trig Ratios/Identities, Trig Equations |
| `/raw-sources/math/Vector 3D-.../Vector 3D/*.pdf` | Notes | 3D, Vector |
| `/raw-sources/math/Math IIT/*.pdf` | Kota Notes | 17 chapters: AOD, AUC, Binomial, Circle, Complex, Compound Angle, Conic, DE, Determinant, Integration, ITF, LCD, P&C, Probability, Quadratic, Relations/Functions, Sequence/Series, Straight Line |
| [[raw-sources/math/MATHS FORMULA SHEET.pdf]] | Formula Sheet | Complete |
| [[raw-sources/math/TRIGNOMETRIC-Formulas.pdf]] | Formula Sheet | Trigonometry |
| [[raw-sources/math/Maths hacked.pdf]] | Shortcuts | Quick tricks |
| [[raw-sources/math/MATHS MODULE.pdf]] | Module | Comprehensive |

---

## 🎯 Study Strategy

1. **Phase 1 (Concepts):** Read theory + Kota notes for each topic → derive formulas yourself
2. **Phase 2 (Practice):** Solve 50-100 problems per topic (use PYQs + Kota modules)
3. **Phase 3 (Integration):** Mixed practice, timed tests, formula sheet memorization
4. **Phase 4 (Mock):** Full syllabus tests, error analysis, weak topic revisit

**High-Yield Topics (JEE Advanced 2020-2024 frequency):**
- Definite Integration + Properties + Area
- Application of Derivatives (Max/Min, Tangent/Normal)
- Conic Sections (Parabola, Ellipse, Hyperbola combined)
- Complex Numbers (Geometry + Roots of Unity)
- Probability (Bayes, Binomial, Conditional)
- Vector & 3D (Scalar triple, Line/Plane intersections)
- Matrices & Determinants (System of equations, Eigenvalues)

---

*Generated from raw-sources/math/ — Kota classroom notes, formula sheets, and practice modules.*