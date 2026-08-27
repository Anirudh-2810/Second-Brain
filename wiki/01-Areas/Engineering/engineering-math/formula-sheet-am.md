---
course_code: "AM"
course_name: "Applied Mathematics (Engineering Mathematics)"
unit: "Master Formula Sheet"
tags: [applied-mathematics, engineering-math, formula-sheet, exam-prep, matrices, partial-differentiation, differential-equations, complex-numbers]
last_updated: "2026-08-25"
confidence: "high"
---

## For future agent
Every AM (Engineering Mathematics F.E.) formula on one page, organized by the five module pages in this folder. Pairs with the module pages for derivations and worked examples; JEE-level recall lives separately in [[modules/../01-Areas/Engineering/mathematics/formula-sheet-master|mathematics formula-sheet-master]].

# Applied Mathematics — Master Formula Sheet

## M1 — Matrices ([[module-1-matrices]])

| Concept | Formula / Rule |
|---------|----------------|
| Inverse | $A^{-1} = \dfrac{1}{|A|}\,\text{adj}(A)$; $A^{-1}$ exists ⟺ $|A| \neq 0$ |
| Properties | $(AB)^{-1} = B^{-1}A^{-1}$ · $(A^T)^{-1} = (A^{-1})^T$ · $|AB| = |A||B|$ |
| System $AX = B$ | Consistent ⟺ $\text{rank}(A) = \text{rank}(A|B)$; unique if rank $= n$, infinite if $< n$; inconsistent if ranks differ |
| **Rank via normal form** | Reduce $A$ to $\begin{bmatrix}I_r & 0 \\ 0 & 0\end{bmatrix}$ using **row AND column** operations → rank = number of 1s = $r$ (only method that uses column ops) |
| **Cayley–Hamilton** | Every square matrix satisfies its own characteristic equation $|A - \lambda I| = 0$ → use to compute $A^{-1}$ and higher powers ($A^2 = \text{tr}(A)A - \ldots$ from the equation) |
| Eigenvalues | $|A - \lambda I| = 0$; $\sum\lambda_i = \text{tr}(A)$; $\prod\lambda_i = |A|$ |
| Eigenvector | $(A - \lambda_i I)X = 0$ → nonzero solution |
| Diagonalizable | $n$ distinct eigenvalues ⇒ diagonalizable; $A = PDP^{-1}$ ⇒ $A^k = PD^kP^{-1}$ |
| Properties of eigenvalues of $A$ | $A^2 \to \lambda^2$; $A^{-1} \to 1/\lambda$; $kA \to k\lambda$; $A^T$ same; $A+kI \to \lambda+k$ |

## M2 — Partial Differentiation ([[module-2-partial-differentiation]])

| Concept | Formula / Rule |
|---------|----------------|
| Definition | $\dfrac{\partial f}{\partial x}$: differentiate w.r.t. $x$, hold $y$ constant |
| Total differential | $df = \dfrac{\partial f}{\partial x}dx + \dfrac{\partial f}{\partial y}dy$ |
| Chain rule | $\dfrac{df}{dt} = \dfrac{\partial f}{\partial x}\dfrac{dx}{dt} + \dfrac{\partial f}{\partial y}\dfrac{dy}{dt}$ |
| Mixed partials | $f_{xy} = f_{yx}$ (when continuous — Clairaut) |
| **Euler's theorem** (homogeneous $f$, degree $n$) | $x f_x + y f_y = n f$; differentiate again: $x^2f_{xx} + 2xyf_{xy} + y^2f_{yy} = n(n-1)f$ |
| **Maxima/Minima** of $f(x,y)$ | Solve $f_x = 0, f_y = 0$; then $r = f_{xx}, s = f_{xy}, t = f_{yy}$: $rt - s^2 > 0, r<0$ → max; $rt-s^2>0, r>0$ → min; $rt-s^2<0$ → saddle; $=0$ → doubtful |
| Jacobians | $J = \dfrac{\partial(u,v)}{\partial(x,y)} = \begin{vmatrix} u_x & u_y \\ v_x & v_y\end{vmatrix}$; $\dfrac{\partial(u,v)}{\partial(x,y)} \cdot \dfrac{\partial(x,y)}{\partial(u,v)} = 1$; two-variable transformation dependence: $J = 0$ |
| Errors | $\dfrac{\delta f}{f} \approx \dfrac{x}{f}f_x\dfrac{\delta x}{x} + \dfrac{y}{f}f_y\dfrac{\delta y}{y}$ (relative error propagation) |
| Taylor (two variables) | $f(x+h,y+k) = f + hf_x + kf_y + \dfrac{1}{2!}(h^2f_{xx} + 2hkf_{xy} + k^2f_{yy}) + \dots$ |

## M3 — Homogeneous Functions ([[module-3-homogeneous-functions]])

| Concept | Formula / Rule |
|---------|----------------|
| Homogeneous test | All terms same total degree: $f(tx, ty) = t^n f(x,y)$ |
| Euler's theorem | $xf_x + yf_y = nf$ |
| Euler (second order) | $x^2f_{xx} + 2xyf_{xy} + y^2f_{yy} = n(n-1)f$ |
| With third variable constraint | If $u = f(x,y)$ and $x,y$ homogeneous of degree $p,q$: $x^2u_{xx} + 2xyu_{xy} + y^2u_{yy} = n(n-1)u$ style deductions — substitute $x = X t$ and compare degrees |
| Deduction pattern | Differentiate Euler's relation partially w.r.t. $x$ and $y$, then multiply by $x$/$y$ and add |

## M4 — Linear Differential Equations ([[module-4-linear-differential-equations]])

### First order
| Type | Form | Solution |
|------|------|----------|
| Variable separable | $\dfrac{dy}{dx} = f(x)g(y)$ | $\int\dfrac{dy}{g(y)} = \int f(x)dx$ |
| Homogeneous | $\dfrac{dy}{dx} = F(y/x)$ | substitute $y = vx$ |
| Linear | $\dfrac{dy}{dx} + Py = Q$ | $y \cdot IF = \int Q\,IF\,dx$, $IF = e^{\int P dx}$ |
| Bernoulli | $\dfrac{dy}{dx} + Py = Qy^n$ | divide by $y^n$, substitute $v = y^{1-n}$ → linear |
| Exact | $Mdx + Ndy = 0$, $\dfrac{\partial M}{\partial y} = \dfrac{\partial N}{\partial x}$ | $\int M\,dx_{(y const)} + \int(\text{N} - \partial_x\!\int\!M)dy = c$ |
| Reducible to linear (x) | $\dfrac{dx}{dy} + P(y)x = Q(y)$ | swap variables, same IF method |

### Higher order — linear with constant coefficients
$a_0\dfrac{d^ny}{dx^n} + \dots + a_ny = X$; symbolic: $F(D)y = X$

**Complementary function (CF)** — roots $m$ of $F(m) = 0$:
| Roots | CF terms |
|-------|----------|
| Real distinct $m_1, m_2$ | $c_1e^{m_1x} + c_2e^{m_2x}$ |
| Real repeated $m$ (r times) | $(c_1 + c_2x + \dots + c_rx^{r-1})e^{mx}$ |
| Complex $\alpha \pm i\beta$ | $e^{\alpha x}(c_1\cos\beta x + c_2\sin\beta x)$ |

**Particular integral (PI) shortcuts**:
| For $X$ = | PI |
|-----------|-----|
| $e^{ax}$ | $\dfrac{1}{F(a)}e^{ax}$ (if $F(a) \neq 0$; else differentiate denominator) |
| $\sin ax$ / $\cos ax$ | Replace $D^2 \to -a^2$: $\dfrac{1}{F(-a^2)}\sin ax$ (if $F(-a^2)\neq0$) |
| $x^m$ | Expand $\dfrac{1}{F(D)}$ in powers of $D$ (binomial), apply to $x^m$ |
| $x\,V$ | $x\dfrac{1}{F(D)}V - \dfrac{F'(D)}{[F(D)]^2}V$ |

**General solution** $y = CF + PI$. Variation of parameters as backup for any linear DE.

## M5 — Complex Numbers ([[module-5-complex-numbers]])

| Concept | Formula / Rule |
|---------|----------------|
| Modulus / argument | $r = \sqrt{x^2+y^2}$, $\theta = \tan^{-1}\dfrac{y}{x}$ (quadrant-aware) |
| Polar / Euler | $z = r(\cos\theta + i\sin\theta) = re^{i\theta}$ |
| De Moivre | $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$ |
| Roots of $z^n = 1$ | $e^{i2k\pi/n}$, $k = 0..n-1$ — equally spaced on unit circle |
| Cube roots of unity | $1, \omega = \dfrac{-1+i\sqrt3}{2}, \omega^2$; $1 + \omega + \omega^2 = 0$, $\omega^3 = 1$ |
| $n$th roots of $re^{i\theta}$ | $r^{1/n}e^{i(\theta + 2k\pi)/n}$ |
| Euler identities | $\cos\theta = \dfrac{e^{i\theta}+e^{-i\theta}}{2}$ · $\sin\theta = \dfrac{e^{i\theta}-e^{-i\theta}}{2i}$ |
| log of complex | $\log z = \log r + i\theta$ |

## Exam-Day Checklist

1. Matrices: state Cayley–Hamilton before using it; verify $\sum\lambda = $ trace
2. Maxima/minima: NEVER skip the $rt - s^2$ discriminant test
3. Linear DE: IF formula + one worked line of $\int Q \cdot IF$
4. PI table: check $F(a) = 0$ / $F(-a^2) = 0$ case BEFORE dividing
5. De Moivre: quote the theorem statement when first used

## Related

[[module-1-matrices]] · [[module-2-partial-differentiation]] · [[module-3-homogeneous-functions]] · [[module-4-linear-differential-equations]] · [[module-5-complex-numbers]] · [[modules/../01-Areas/Engineering/mathematics/formula-sheet-master|JEE-level master sheet]]