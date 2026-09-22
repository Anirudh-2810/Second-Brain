---
date: 2026-09-22
description: "9-question drill on rank, REF, Rouche-Capelli consistency, homogeneous vs non-homogeneous systems — all solutions verified step-by-step."
course_code: "AM1"
course_name: "Applied Mathematics I"
unit: "Module 1 - Matrices"
tags: [btech, kjsce, matrices, rank, consistency, linear-systems, quiz]
last_updated: "2026-09-22"
confidence: high
---

## For future agent

9-question tutorial drill (2026-09-22) for [[module-1-matrices]]: consistency via augmented-matrix rank, unique/infinite/no-solution classification, REF check, homogeneous parametric solve. All 9 answers verified by re-derivation. Stable exam reference — link, don't duplicate.

# 2026-09-22 Quiz — System Consistency, Rank, REF (9 Qs)

Parent: [[module-1-matrices]] · Formula sheet: [[formula-sheet-am]] · Prereqs: [[prerequisite-toolkit]]

Core theorem used throughout ([[module-1-matrices#2.3 Systems of Linear Equations]]):

> $AX=B$ consistent $\iff \mathrm{rank}(A)=\mathrm{rank}([A\mid B])$. If $=r$: $r=n$ unique, $r<n$ infinite ($n-r$ free vars). Else no solution. Homogeneous $AX=0$ always consistent.

## Q1 — Consistency of $[A:B]$ in $a$ → $a=-3,4$

$$\begin{bmatrix} 1 & 2 & 3 & : & 4 \\ 2 & -1 & -2 & : & a^2 \\ -1 & -7 & -11 & : & a \end{bmatrix}$$

$R_2\to R_2-2R_1=[0,-5,-8\mid a^2-8]$; $R_3\to R_3+R_1=[0,-5,-8\mid a+4]$; $R_3\to R_3-R_2=[0,0,0\mid -a^2+a+12]$. $\mathrm{rank}(A)=2$, so need $-a^2+a+12=0\implies a^2-a-12=0\implies (a-4)(a+3)=0$. **$a=4$ or $a=-3$.**

## Q2 — Unique solution condition on $k$ → $k\neq 1,-2$

$$A=\begin{bmatrix} k & -2 & 1 \\ 1 & -2k & 1 \\ 1 & -2 & k \end{bmatrix},\quad \det(A)=-2k^3+6k-4$$

$\det(A)=0\iff k^3-3k+2=0\iff (k-1)^2(k+2)=0$. Unique $\iff \det\neq 0$: **$k\neq 1,\;k\neq -2$.**

## Q3 — $AX=B$, $\det(A)=0$ → never unique

$\det=0\implies \mathrm{rank}(A)<n$, so unique impossible. Either infinite ($\mathrm{rank}(A)=\mathrm{rank}([A\mid B])<n$) or none ($\mathrm{rank}(A)<\mathrm{rank}([A\mid B])$).

## Q4 — General consistency condition

**$\mathrm{rank}(A)=\mathrm{rank}([A\mid B])$** (Rouché–Capelli).

## Q5 — Infinite solutions → $\alpha=2,\;\beta=7$

$[A\mid B]=\begin{bmatrix}1&1&1&: &5\\1&3&3&: &9\\1&2&\alpha&: &\beta\end{bmatrix}$; $R_2-R_1\to[0,1,1\mid2]$; $R_3-R_1\to[0,1,\alpha-1\mid\beta-5]$; minus $R_2\to[0,0,\alpha-2\mid\beta-7]$. Zero row needs **$\alpha=2,\;\beta=7$**.

## Q6 — Which matrix is in REF? → (c)

$$\begin{bmatrix} 1&0&5&7\\0&0&1&3\\0&0&0&2\\0&0&0&0\end{bmatrix}$$

Pivots at cols 1,3,4 stepping right, zeros below, zero row bottom. REF yes (not RREF — nonzeros above pivots allowed in REF).

## Q7 — Rank of $A$ → 2

$$A=\begin{pmatrix}1&1&1\\1&-1&0\\1&1&1\end{pmatrix}$$

$R_1=R_3\implies\det=0$. $R_2-R_1=[0,-2,-1]$, $R_3-R_1=[0,0,0]$ → 2 nonzero rows. **Rank 2.**

## Q8 — Homogeneous solve → rank 2, $(t,2t,-t)$

$\det=3(-51)-2(102)+7(51)=0$; minor $\begin{vmatrix}3&2\\4&-3\end{vmatrix}=-17\neq0\implies r=2$, 1 free var. Set $z=-t$: $3x+2y=7t$, $4x-3y=-2t\implies x=t,\;y=2t$. **$(t,2t,-t),\;t\in\mathbb{R}$.**

## Q9 — Consistency test → no solution

$R_2-2R_1\to[0,1,0\mid2]$; $R_3-R_1=[0,-1,0\mid-1]$; $+[0,1,0\mid2]\to[0,0,0\mid1]$. $\mathrm{rank}(A)=2\neq3=\mathrm{rank}([A\mid B])$. **Inconsistent.**

## Exam traps

- $0=0$ row → free var (infinite if $r<n$); $0=b\neq0$ row → stop, no solution.
- Square unique $\iff\det\neq0$; $\det=0$ never gives unique (Q2 vs Q3 pair).
- REF $\neq$ RREF: pivots need not be 1, entries above pivots may be nonzero (Q6).
- Homogeneous always has $\mathbf{0}$; nontrivial $\iff r<n$.
