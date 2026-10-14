---
course_code: "216U06C101"
course_name: "Applied Mathematics-I"
unit: "MSE Revision — Modules 1–3"
date: "2026-10-15"
tags: [engineering-math, btech, exam-prep, mse, matrices, partial-differentiation, homogeneous-functions, revision]
last_updated: "2026-10-15"
description: "MSE revision pack for Applied Mathematics-I: exam-facing consolidation of Modules 1-3 (matrices/rank, partial differentiation/Jacobian, Euler homogeneous functions). Formula recall + traps + worked patterns, linking the deep module pages."
confidence: high
---

## For future agent

Exam-facing consolidation of Applied Mathematics-I for the **MSE (in-semester exam)**, 30 marks / 75 min. This is NOT a re-teach — it is the condensed recall surface (formulas, decision rules, traps, pattern of the real paper) that links to the deep pages [[module-1-matrices]], [[module-2-partial-differentiation]], [[module-3-homogeneous-functions]]. Paper pattern and worked solutions live in [[ise-exam-prep-am1]]. If any formula here disagrees with a module page, the module page is the single source of truth — fix this page. As of 2026-10-15; syllabus weightings can change per term.

# MSE Revision — Applied Mathematics-I

## Paper pattern (recurring)

- **30 marks, 1 hr 15 min.** Q1 **compulsory** (6M) + Q2/Q3 "attempt any TWO of three" (6M each).
- Modules: **M1 Matrices**, **M2 Partial Differentiation (incl. Jacobian)**, **M3 Homogeneous Functions**.
- Q1 is almost always **normal form → rank**. Q2/Q3 rotate through Jacobian, orthogonal ciphers, Laplacian identities, Gauss-Seidel, λ-consistency, Euler theorem.
- Verified pattern + full worked solutions: [[ise-exam-prep-am1]].

## Module 1 — Matrices (deep: [[module-1-matrices]])

### Rank & normal form
- **Normal form** = reduce $A$ to $\begin{bmatrix} I_r & 0 \\ 0 & 0 \end{bmatrix}$ using **row AND column** elementary operations. **rank = r**.
- ⚠️ **Trap:** row-ops only will not finish the normal form — column ops are legal *for this method only*.
- Useful: $\text{rank}(A) = \text{rank}(A^T)$; rank unchanged by elementary ops.

### Systems of linear equations
- $[A|B]$ → row-reduce. Let $r = \text{rank}(A)$, $r' = \text{rank}([A|B])$, $n$ = number of unknowns:
  - $r' \ne r$ → **inconsistent** (no solution)
  - $r = r' = n$ → **unique** solution
  - $r = r' < n$ → **infinitely many**, with $(n-r)$ free parameters
- **Eigenvalues:** solve $\det(A - \lambda I) = 0$; eigenvector: $(A-\lambda I)x = 0$.
- **Cayley–Hamilton:** every matrix satisfies its own characteristic equation → use to find $A^{-1}$ and powers.
- **Orthogonal matrix:** $Q^TQ = I \Rightarrow Q^{-1} = Q^T$ (used in the cipher question — state it to earn the method mark).
- **Gauss–Seidel:** requires diagonally dominant system; **reuse the latest value immediately** (unlike Jacobi). Iterate from $(0,0,0)$.

## Module 2 — Partial Differentiation (deep: [[module-2-partial-differentiation]])

### Core rules
- **Chain rule:** $u = f(x,y)$, $x,y$ functions of $t$: $\dfrac{du}{dt} = \dfrac{\partial u}{\partial x}\dfrac{dx}{dt} + \dfrac{\partial u}{\partial y}\dfrac{dy}{dt}$.
- **Composite/partial:** extend with one term per intermediate variable.

### Jacobian
- $J = \dfrac{\partial(u,v)}{\partial(x,y)} = \begin{vmatrix} u_x & u_y \\ v_x & v_y \end{vmatrix}$; 3-var: $3\times3$ determinant of first partials.
- **Chain/product:** $\dfrac{\partial(u,v)}{\partial(x,y)} = \dfrac{\partial(u,v)}{\partial(r,s)}\cdot\dfrac{\partial(r,s)}{\partial(x,y)}$.
- **Inverse:** $\dfrac{\partial(u,v)}{\partial(x,y)} = 1 \big/ \dfrac{\partial(x,y)}{\partial(u,v)}$.
- ⚠️ **Trap:** $\partial(u,v,w)/\partial(x,y,z)$ is a **straight determinant**, not the chain-rule Jacobian. Expand along the sparsest row.

### Maxima / minima
- $r = f_{xx}$, $s = f_{xy}$, $t = f_{yy}$; solve $f_x = f_y = 0$ for stationary points.
  - $rt - s^2 > 0,\ r<0$ → **max**; $rt-s^2>0,\ r>0$ → **min**; $rt-s^2<0$ → saddle; $rt-s^2=0$ → inconclusive.
- Lagrange multipliers for constrained extrema.

### Laplacian-type identities
- Pattern: $u_{xx}+u_{yy}+u_{zz}$ of a polynomial → differentiate each term in its own variable, add. E.g. $u = x^2y+y^2z+z^2x \Rightarrow u_{xx}+u_{yy}+u_{zz} = 2(x+y+z)$.

## Module 3 — Homogeneous Functions (deep: [[module-3-homogeneous-functions]])

- $f$ homogeneous of degree $n$ if $f(tx,ty) = t^n f(x,y)$.
- **Euler's theorem:** $x u_x + y u_y = n\,u$.
- **Second order:** $x^2u_{xx} + 2xyu_{xy} + y^2u_{yy} = n(n-1)u$.
- ⚠️ **Trap:** find the degree of the **whole** function; a $\sin^{-1}(\cdot)$ or $\tan^{-1}(\cdot)$ of a degree-0 ratio contributes degree 0, so the outer power sets $n$.

## Formula recall (rapid)

| Concept | Formula |
|---|---|
| Normal form rank | $(I_r \mid 0; 0 \mid 0) \Rightarrow$ rank $= r$ |
| Consistency | $r' \ne r$ inconsistent · $r=r'=n$ unique · $r=r'<n$ infinite |
| Eigen | $\det(A-\lambda I)=0$ |
| Orthogonal | $Q^{-1}=Q^T$ |
| Jacobian 2-var | $J = u_xv_y - u_yv_x$ |
| Jacobian inverse | $\partial(u,v)/\partial(x,y) = [\partial(x,y)/\partial(u,v)]^{-1}$ |
| Extrema test | $rt-s^2$ sign + sign of $r$ |
| Euler degree $n$ | $xu_x+yu_y = nu$ |
| Euler 2nd order | $x^2u_{xx}+2xyu_{xy}+y^2u_{yy} = n(n-1)u$ |

## See also

- [[module-1-matrices]] · [[module-2-partial-differentiation]] · [[module-3-homogeneous-functions]] — deep pages (source of truth)
- [[formula-sheet-am]] — full AM formula sheet by module
- [[ise-exam-prep-am1]] — real paper pattern + worked solutions
- [[quiz-2026-09-22-systems-consistency-rank]] — consistency/rank drill
- [[prerequisite-toolkit]] — algebra basics if a rule slips
- [[mse-2026-10-26-5-day-plan]] — the day-by-day plan this pack feeds
