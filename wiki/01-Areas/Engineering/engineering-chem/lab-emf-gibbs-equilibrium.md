---
course_code: "ENG-CHEM"
course_name: "Engineering Chemistry"
unit: "Chem Lab Expt 2 — EMF, Gibbs Energy & Equilibrium"
tags: [btech, engineering-chemistry, chem-lab, emf, nernst, gibbs-energy, electrochemical-series]
last_updated: "2026-09-09"
description: "Chem Lab Expt 2 write-up: cell EMF from the electrochemical series, Nernst equation, Gibbs free energy, equilibrium constant and spontaneity prediction."
---

## For future agent

Full ingest of `Chem Lab/EMF.docx` (Expt 2, VLab). Theory companion is [[module-3-electrochemistry-corrosion]] (cells, reference electrodes, Nernst derivation). This page keeps the bench objectives + series table + result chain.

# Expt 2 — EMF of a Cell & Spontaneity

**Objectives**: (i) find cell EMF, (ii) compute $\Delta G$, (iii) compute equilibrium constant, (iv) predict spontaneity.

## 1. Cell construction logic

Anode = oxidation (metal with **lower** reduction potential); cathode = reduction (higher $E^\circ$). Compartments joined by a salt bridge (concentrated electrolyte in agar jelly — completes circuit, maintains neutrality). Daniel-cell notation: $\mathrm{Zn\,|\,Zn^{2+}\,||\,Cu^{2+}\,|\,Cu}$.

Standard EMF:

$$E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode}\quad\text{(both as reduction potentials)}$$

Non-standard concentrations via Nernst ($n$ = electrons transferred):

$$E = E^\circ - \frac{0.0591}{n}\log Q\qquad (25^\circ\mathrm{C})$$

## 2. Result chain (memorize order)

$$\Delta G = -nFE\qquad \Delta G^\circ = -nFE^\circ_{cell}\qquad \log K = \frac{nE^\circ}{0.0591}$$

(via van 't Hoff / $\Delta G^\circ = -RT\ln K$). $E_{cell} > 0 \Rightarrow \Delta G < 0 \Rightarrow$ spontaneous as written.

## 3. Electrochemical series (abridged, V vs SHE — from source)

$\mathrm{F_2}}$ +2.87 · $\mathrm{Au^+}$ +1.68 · $\mathrm{Cl_2}$ +1.36 · $\mathrm{O_2}$(acid) +1.23 · $\mathrm{Ag^+}$ +0.80 · $\mathrm{Fe^{3+}/Fe^{2+}}$ +0.77 · $\mathrm{Cu^{2+}}$ +0.34 · $\mathrm{2H^+/H_2}$ 0.00 · $\mathrm{Pb^{2+}}$ −0.13 · $\mathrm{Ni^{2+}}$ −0.23 · $\mathrm{Fe^{2+}}$ −0.44 · $\mathrm{Zn^{2+}}$ −0.76 · $\mathrm{Al^{3+}}$ −1.67 · $\mathrm{Mg^{2+}}$ −2.34 · $\mathrm{Na^+}$ −2.71 · $\mathrm{K^+}$ −2.93 · $\mathrm{Li^+}$ −3.02.

Worked check (Daniel cell): $E^\circ = 0.34 - (-0.76) = +1.10\ \mathrm{V}$, $n = 2$ → $\Delta G^\circ = -2(96500)(1.10) \approx -212\ \mathrm{kJ/mol}$, $\log K = 2(1.10)/0.0591 \approx 37.2$ — strongly product-favoured.

## 4. Viva points

- SHE as reference: Pt|$\mathrm{H_2}$(1 atm)|$\mathrm{H^+}$(1 M), defined 0.000 V; practical labs use calomel (see [[module-3-electrochemistry-corrosion]]).
- Salt-bridge function vs wire: ions migrate to balance charge; electrons go through the external circuit.
- Any pair of half-cells makes a galvanic cell — higher $E^\circ$ always becomes the cathode.
