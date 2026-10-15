---
course_code: "216U06C101"
course_name: "Applied Mathematics-I"
unit: "MSE Recall Test — Modules 1–3"
date: "2026-10-16"
tags: [engineering-math, btech, exam-prep, mse, recall-test, self-test, matrices, partial-differentiation, homogeneous-functions]
last_updated: "2026-10-16"
confidence: high
description: "Exam-style self-test for Applied Mathematics-I MSE (Modules 1-3): normal form/rank, consistency, eigen/Cayley-Hamilton, orthogonal, Jacobian, maxima-minima, Laplacian, Euler. Questions first, worked answer key in collapsible callouts — attempt cold before revealing."
relations:
  depends_on: "[[mse-revision-am1]]"
  relates_to: "[[mse-flashcards-am1]]"
---

## For future agent

Cold **self-test** for the Applied Mathematics-I MSE (Modules 1–3). Attempt every question **on paper with no notes** first; then open the collapsed `> [!success]- Answer` under each question to mark it. A unit counts as *passed* only if you reproduce the method unaided (see [[mse-study-method]]). The 9-question rank/consistency drill already lives in [[quiz-2026-09-22-systems-consistency-rank]] — run that separately as the M1 consistency block rather than duplicating it here. Deep pages are the source of truth: [[module-1-matrices]], [[module-2-partial-differentiation]], [[module-3-homogeneous-functions]]. Worked paper solutions: [[ise-exam-prep-am1]].

# MSE Recall Test — Applied Mathematics-I

Pack: [[mse-revision-am1]] · Cards: [[mse-flashcards-am1]] · Consistency drill: [[quiz-2026-09-22-systems-consistency-rank]]

> **How to use:** answer all questions cold, then reveal. Score by unit, not by marks. Anything wrong → flag it and repair from the pack.

## Q1 — Normal form → rank

Reduce $A=\begin{bmatrix}1&2&3\\2&4&6\\1&2&3\end{bmatrix}$ to normal form and state the rank. Name the operations.

> [!success]- Answer
> $R_2\to R_2-2R_1$, $R_3\to R_3-R_1$ leave one nonzero row. Column ops kill the 2nd/3rd columns. Normal form $=\begin{bmatrix}1&0&0\\0&0&0\\0&0&0\end{bmatrix}\Rightarrow \operatorname{rank}=1$. (Trap: row-ops alone cannot finish the normal form — you need column ops.)

## Q2 — Eigenvalues + Cayley–Hamilton

For $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$: (a) find the eigenvalues, (b) use Cayley–Hamilton to write $A^{-1}$.

> [!success]- Answer
> (a) $|A-\lambda I|=(1-\lambda)(4-\lambda)-6=\lambda^{2}-5\lambda-2=0\Rightarrow \lambda=\dfrac{5\pm\sqrt{33}}{2}$. $\operatorname{tr}=5$, $|A|=-2$ ✓.
> (b) C–H: $A^{2}-5A-2I=0\Rightarrow A^{-1}=\dfrac{1}{2}(A-5I)=\dfrac{1}{2}\begin{bmatrix}-4&2\\3&-1\end{bmatrix}$.

## Q3 — Orthogonal cipher

State the property that lets you invert an orthogonal $Q$ without computing an inverse, and why it is valid.

> [!success]- Answer
> $Q^{T}Q=I\Rightarrow Q^{-1}=Q^{T}$ (the transpose *is* the inverse). State it explicitly to earn the method mark.

## Q4 — Gauss–Seidel

Which of these is suitable for Gauss–Seidel, and why?
(a) $\begin{cases}x+4y=5\\ 5x+y=6\end{cases}$ (b) $\begin{cases}5x+y=6\\ x+4y=5\end{cases}$

> [!success]- Answer
> **(b)** — rows are **diagonally dominant** ($|5|>|1|$, $|4|>|1|$). (a) is not. Seidel also **reuses the latest value immediately** and starts from $(0,0,0)$.

## Q5 — Jacobian (definition)

Find $\dfrac{\partial(u,v)}{\partial(x,y)}$ for $u=x^{2}-y^{2},\ v=2xy$.

> [!success]- Answer
> $u_x=2x,\ u_y=-2y,\ v_x=2y,\ v_y=2x$. $J=u_xv_y-u_yv_x=4x^{2}+4y^{2}=4(x^{2}+y^{2})$.

## Q6 — Jacobian inverse / product rule

If $\dfrac{\partial(x,y)}{\partial(u,v)}=e^{u}\!,$ what is $\dfrac{\partial(u,v)}{\partial(x,y)}$, and state the product rule connecting two Jacobians.

> [!success]- Answer
> $\dfrac{\partial(u,v)}{\partial(x,y)}=1/e^{u}=e^{-u}$. Product rule: $\dfrac{\partial(u,v)}{\partial(x,y)}=\dfrac{\partial(u,v)}{\partial(r,s)}\cdot\dfrac{\partial(r,s)}{\partial(x,y)}$.

## Q7 — Maxima / minima

Locate and classify the stationary points of $f(x,y)=x^{3}+y^{3}-3xy$.

> [!success]- Answer
> $f_x=3x^{2}-3y=0,\ f_y=3y^{2}-3x=0\Rightarrow (0,0)$ and $(1,1)$. $r=6x,\ s=-3,\ t=6y$. At $(1,1)$: $rt-s^{2}=36-9>0,\ r>0$ → **min**. At $(0,0)$: $rt-s^{2}=-9<0$ → **saddle**.

## Q8 — Laplacian-type identity

For $u=x^{3}+y^{3}+z^{3}-3xyz$, find $u_{xx}+u_{yy}+u_{zz}$.

> [!success]- Answer
> $u_{xx}=6x,\ u_{yy}=6y,\ u_{zz}=6z \Rightarrow$ sum $=6(x+y+z)$.

## Q9 — Euler's theorem

Show $u=\dfrac{x^{3}+y^{3}}{x+y}$ is homogeneous, find its degree, and verify $xu_x+yu_y=nu$ at a point.

> [!success]- Answer
> $u(tx,ty)=t^{3}\dfrac{x^{3}+y^{3}}{tx+ty}=t^{2}u \Rightarrow n=2$. Euler gives $xu_x+yu_y=2u$; check numerically (e.g. $x=y=1$, $u=1$).

## Q10 — Degree trap

Find the degree $n$ of $u=\tan^{-1}\!\left(\dfrac{x^{3}+y^{3}}{x^{3}-y^{3}}\right)$.

> [!success]- Answer
> Argument is degree $0$; the inverse-trig outer contributes $0$, so the ratio's inner content is degree $0$ → **$n=0$**. (If it were $\sin^{-1}(x/y)$ with $x,y$ degree-1, the ratio is degree 0 → $n=0$; an outer *power* like $\left(\frac{x+y}{x-y}\right)^{k}$ sets $n=k$.)

## Q11 — Lagrange multipliers

Find the extreme value of $xy$ subject to $x+y=10$.

> [!success]- Answer
> $\nabla f=\lambda\nabla g:\ y=\lambda,\ x=\lambda\Rightarrow x=y=5$. Value $xy=25$ (**max** on the line). Method mark: set up $\nabla f=\lambda\nabla g$ plus the constraint.

## Q12 — Consistency in a parameter

For which $\lambda$ is $\begin{bmatrix}1&1&1\\1&2&3\\1&3&\lambda\end{bmatrix}X=\begin{bmatrix}1\\2\\3\end{bmatrix}$ inconsistent / unique / infinite?

> [!success]- Answer
> $R_3-R_2=[0,1,\lambda-3\mid1]$, $R_2-R_1=[0,1,2\mid1]$; subtract → $[0,0,\lambda-5\mid0]$.
> $\lambda=5$ → rank$(A)=$rank$([A|B])=2<3$ → **infinite**; $\lambda\ne5$ → full rank → **unique**; **never inconsistent** here.

## Score sheet

| Unit | Pass? | Flag |
|---|---|---|
| M1 normal form/rank (Q1) | | |
| M1 eigen + C–H (Q2) | | |
| M1 orthogonal (Q3) | | |
| M1 Gauss–Seidel (Q4) | | |
| M2 Jacobian (Q5, Q6) | | |
| M2 extrema (Q7) | | |
| M2 Laplacian (Q8) | | |
| M3 Euler + trap (Q9, Q10) | | |
| M2 Lagrange (Q11) | | |
| M1 consistency (Q12) | | |

## See also

- [[mse-revision-am1]] · [[mse-flashcards-am1]] · [[mse-study-method]]
- [[quiz-2026-09-22-systems-consistency-rank]] — the 9-Q consistency block
- [[ise-exam-prep-am1]] — real paper + worked solutions
- [[module-1-matrices]] · [[module-2-partial-differentiation]] · [[module-3-homogeneous-functions]]
