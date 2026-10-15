---
course_code: "216U06C101"
course_name: "Applied Mathematics-I"
unit: "MSE Flashcards — Modules 1–3"
date: "2026-10-16"
tags: [engineering-math, btech, exam-prep, mse, flashcards, matrices, partial-differentiation, homogeneous-functions, revision]
last_updated: "2026-10-16"
confidence: high
description: "Flashcard deck for Applied Mathematics-I MSE (Modules 1-3): rank/normal form, systems consistency, eigen/Cayley-Hamilton/orthogonal, Gauss-Seidel, Jacobian, maxima-minima, Laplacian, Euler homogeneous functions. Each card is a collapsible callout — read the question, click to reveal the answer. Companion to the recall test and revision pack."
relations:
  depends_on: "[[mse-revision-am1]]"
  relates_to: "[[mse-recall-test-am1]]"
---

## For future agent

Flashcards for the **Applied Mathematics-I MSE** (Modules 1–3). Format = one card per fact, the *question always visible*, the answer in a **collapsed callout** `> [!success]- Answer` (click to reveal). No spaced-repetition plugin is installed in this vault, so this works with vanilla Obsidian. Answers are condensed recall surfaces — the **deep module pages are the source of truth** ([[module-1-matrices]], [[module-2-partial-differentiation]], [[module-3-homogeneous-functions]]); if a card disagrees, fix the card. Paper pattern + worked solutions: [[ise-exam-prep-am1]]. Run the drill per [[mse-study-method]]: cover the answer, say it, then click. Cards tagged `#mse #flashcards` so a future SR plugin can ingest them.

# MSE Flashcards — Applied Mathematics-I

Pack: [[mse-revision-am1]] · Test: [[mse-recall-test-am1]] · Plan: [[mse-2026-10-26-5-day-plan]]

## Module 1 — Matrices

**M‑01.** Normal form — which elementary operations are allowed, and what does the rank equal?

> [!success]- Answer
> Reduce $A$ to $\begin{bmatrix}I_r & 0\\0 & 0\end{bmatrix}$ using **row AND column** elementary operations. Then **rank $=r$**. ⚠️ Row-ops alone will *not* finish the normal form — column ops are legal for this method only.

**M‑02.** Two quick rank facts?

> [!success]- Answer
> $\operatorname{rank}(A)=\operatorname{rank}(A^{T})$; rank is unchanged by elementary row/column operations.

**M‑03.** Consistency of $AX=B$ — state the three cases in terms of $r, r', n$.

> [!success]- Answer
> $r=\operatorname{rank}(A)$, $r'=\operatorname{rank}([A\mid B])$, $n=\#$unknowns:
> $r'\ne r$ → **inconsistent**; $r=r'=n$ → **unique**; $r=r'<n$ → **infinitely many**, with $(n-r)$ free parameters.

**M‑04.** Rouché–Capelli consistency condition (one line)?

> [!success]- Answer
> $AX=B$ is consistent $\iff \operatorname{rank}(A)=\operatorname{rank}([A\mid B])$.

**M‑05.** A homogeneous system $AX=0$ — always consistent? When is a *nontrivial* solution possible?

> [!success]- Answer
> Always consistent (it has $\mathbf{0}$). Nontrivial solutions $\iff \operatorname{rank}(A)<n$.

**M‑06.** Eigenvalues — equation, and two sum/product facts.

> [!success]- Answer
> Solve $\det(A-\lambda I)=0$. Then $\sum\lambda_i=\operatorname{tr}(A)$ and $\prod\lambda_i=|A|$.

**M‑07.** Eigenvector for eigenvalue $\lambda_i$?

> [!success]- Answer
> Solve $(A-\lambda_i I)X=0$ for a **nonzero** solution $X$.

**M‑08.** Cayley–Hamilton — statement and the two things you use it for?

> [!success]- Answer
> Every square matrix satisfies its own characteristic equation $|A-\lambda I|=0$. Use it to find $A^{-1}$ (rearrange for $A^{-1}$) and higher powers $\left(A^{2}=\operatorname{tr}(A)A-\dots\right)$.

**M‑09.** Orthogonal matrix — relation, and what to *state* in the cipher question?

> [!success]- Answer
> $Q^{T}Q=I \Rightarrow Q^{-1}=Q^{T}$. State this explicitly to earn the method mark (orthogonal cipher).

**M‑10.** When is $A$ diagonalizable, and the formula for $A^{k}$?

> [!success]- Answer
> $n$ distinct eigenvalues $\Rightarrow$ diagonalizable. $A=PDP^{-1}\Rightarrow A^{k}=PD^{k}P^{-1}$.

**M‑11.** Gauss–Seidel — two conditions, and how it differs from Jacobi?

> [!success]- Answer
> Requires a **diagonally dominant** system; iterate from $(0,0,0)$. Unlike Jacobi, it **reuses the latest value immediately** in the same sweep.

**M‑12.** Eigenvalue transformations: $A^{T}, A^{2}, A^{-1}, kA, A+kI$?

> [!success]- Answer
> $A^{T}\to\lambda$ (same); $A^{2}\to\lambda^{2}$; $A^{-1}\to1/\lambda$; $kA\to k\lambda$; $A+kI\to\lambda+k$.

## Module 2 — Partial Differentiation

**M‑13.** Definition of $\dfrac{\partial f}{\partial x}$?

> [!success]- Answer
> Differentiate w.r.t. $x$ **holding $y$ constant**.

**M‑14.** Chain rule for $u=f(x,y)$ with $x=x(t),\,y=y(t)$?

> [!success]- Answer
> $\dfrac{du}{dt}=\dfrac{\partial u}{\partial x}\dfrac{dx}{dt}+\dfrac{\partial u}{\partial y}\dfrac{dy}{dt}$. (Composite: one term per intermediate variable.)

**M‑15.** Mixed partials — the equality and its condition?

> [!success]- Answer
> $f_{xy}=f_{yx}$ (Clairaut), **when the second partials are continuous**.

**M‑16.** Jacobian of $u,v$ w.r.t. $x,y$ (definition)?

> [!success]- Answer
> $J=\dfrac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}u_x & u_y\\ v_x & v_y\end{vmatrix}=u_xv_y-u_yv_x$. Three variables → $3\times3$ determinant of first partials.

**M‑17.** Two Jacobian manipulation rules — inverse and product?

> [!success]- Answer
> Inverse: $\dfrac{\partial(u,v)}{\partial(x,y)}=1\Big/\dfrac{\partial(x,y)}{\partial(u,v)}$. Product: $\dfrac{\partial(u,v)}{\partial(x,y)}=\dfrac{\partial(u,v)}{\partial(r,s)}\cdot\dfrac{\partial(r,s)}{\partial(x,y)}$.

**M‑18.** Jacobian trap — is $\partial(u,v,w)/\partial(x,y,z)$ a chain-rule product?

> [!success]- Answer
> **No** — it is a **straight determinant** (expand along the sparsest row). Never apply the chain rule across it.

**M‑19.** Maxima/minima test — define $r,s,t$ and give all four outcomes.

> [!success]- Answer
> $r=f_{xx},\ s=f_{xy},\ t=f_{yy}$ at points solving $f_x=f_y=0$:
> $rt-s^{2}>0,\ r<0$ → **max**; $rt-s^{2}>0,\ r>0$ → **min**; $rt-s^{2}<0$ → **saddle**; $rt-s^{2}=0$ → **inconclusive**.

**M‑20.** Method for constrained extrema of $f$ subject to $g=0$?

> [!success]- Answer
> **Lagrange multipliers:** solve $\nabla f=\lambda\nabla g$ together with $g=0$.

**M‑21.** Laplacian-identity pattern — e.g. $u=x^{2}y+y^{2}z+z^{2}x$, find $u_{xx}+u_{yy}+u_{zz}$.

> [!success]- Answer
> Differentiate each term in its own variable and add: $u_{xx}=2y,\ u_{yy}=2z,\ u_{zz}=2x \Rightarrow$ sum $=2(x+y+z)$.

## Module 3 — Homogeneous Functions

**M‑22.** Definition — $f$ is homogeneous of degree $n$ if…?

> [!success]- Answer
> $f(tx,ty)=t^{n}f(x,y)$ (all terms share the same total degree).

**M‑23.** Euler's theorem (first order)?

> [!success]- Answer
> $x\,u_{x}+y\,u_{y}=n\,u$.

**M‑24.** Euler's theorem (second order)?

> [!success]- Answer
> $x^{2}u_{xx}+2xyu_{xy}+y^{2}u_{yy}=n(n-1)\,u$.

**M‑25.** Degree trap — for $u=\sin^{-1}\!\left(\dfrac{x+y}{x-y}\right)$, what is $n$?

> [!success]- Answer
> The ratio is degree $0$; $\sin^{-1}(\cdot)$ of a degree-0 argument contributes degree $0$, so the **outer power sets $n$** — here $n=1$.

## Paper pattern

**M‑26.** Paper structure for the Maths MSE?

> [!success]- Answer
> **30 marks, 1 h 15 min.** Q1 **compulsory** (6M) + Q2/Q3 "attempt any TWO of three" (6M each). Modules M1/M2/M3.

**M‑27.** What is Q1 almost always, and what rotates in Q2/Q3?

> [!success]- Answer
> Q1 $\approx$ **normal form → rank**. Q2/Q3 rotate through Jacobian, orthogonal ciphers, Laplacian identities, Gauss–Seidel, $\lambda$-consistency, Euler's theorem.

## See also

- [[mse-revision-am1]] — the revision pack (source for these cards)
- [[mse-recall-test-am1]] — exam-style test with worked key
- [[module-1-matrices]] · [[module-2-partial-differentiation]] · [[module-3-homogeneous-functions]] — deep pages (source of truth)
- [[quiz-2026-09-22-systems-consistency-rank]] — 9-question consistency drill
- [[formula-sheet-am]] · [[ise-exam-prep-am1]] · [[prerequisite-toolkit]]
- [[mse-study-method]] — how to run the deck
