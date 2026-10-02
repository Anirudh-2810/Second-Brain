---
course_code: "ENG-PHY"
course_name: "Engineering Physics"
unit: "Domain hub — all modules"
date: "2026-10-02"
description: "Engineering Physics module hub — the four course modules (optics/wave, optoelectronics/lasers, quantum mechanics, semiconductors/EM) with the revision-first entry point for each, plus the Sem-1 source map and open-ingest gaps."
tags: [engineering-physics, index, domain-hub, optics, lasers, quantum-mechanics, semiconductors, btech, exam-prep]
last_updated: "2026-10-02"
confidence: high
---

## For future agent

Landing page for `wiki/01-Areas/Engineering/engineering-physics/`. **This page did not exist until 2026-10-02** even though `Engineering/INDEX.md` had been linking to `[[engineering-physics/overview]]` since the domain was created — a broken link that went unnoticed. It exists now purely to close that gap, so treat it as a **router, not a content page**: every topic lives in a child page.

**Two sizes worth knowing before you open anything.** Three module pages are very large and are *not* revision surfaces — `module-1-optics-interference-diffraction` (81.5 KB), `module-2-optoelectronics-lasers-fiber-optics` (73.2 KB), `module-3-quantum-mechanics` (73.9 KB), `module-4-semiconductors-electromagnetism` (60.6 KB). **Route the user to the short revision page first** and only send them into the deep page for derivation detail. Do not paste deep-page content into an answer when a short page covers it.

**Only Module 2 has a revision sheet so far.** Modules 1, 3 and 4 have no short cut — the closest thing is `thin-film-interference-revision` (4.6 KB, M1 topic only). If a Physics-B revision sheet is wanted for another module, that is a known gap, not an oversight.

---

# Engineering Physics — Module Hub

> BTech coursework, Engineering Physics. Four modules. **Scan this folder for physics exam questions**, then route to the right child page.

---

## Start here — pick your revision surface

| If you need | Go to | Size |
|---|---|---|
| **Lasers quick revision** (Einstein coefficients, inversion, threshold gain, laser types, cavity modes) | **[[lasers-quick-ref]]** | 19 KB ✓ |
| **Optical fibres** (TIR, NA derivation, V-number, modes, attenuation, dispersion, bit rate) | **[[module-2-fiber-optics]]** | 24 KB ✓ |
| **Module 2 exam practice** — 30 theory questions + 40 numericals, laser *and* fibre, with worked solutions | **[[module-2-laser-fibre-question-bank]]** | 26 KB ✓ |
| Thin-film interference, focused | [[thin-film-interference-revision]] | 4.6 KB ✓ |
| Full derivations + numericals for any module | the module page below | 60–82 KB |

**Module 2 is now fully faculty-sourced.** Dr. Suren Patwardhan's official papers (*SVU R-2023*) were opened on 2026-10-02 after sitting unread: `2.1 Laser/` and `2.2 Optical Fibre/` each hold a Notes, Formulas, Numericals and Questions paper. Where the faculty notes disagree with the deep module page, **the faculty win** — three corrections are recorded on [[lasers-quick-ref]] (threshold uses `L` not `l`; Ne⁺ metastable is 18.7 eV not 19.78 eV; He-Ne coherence is ≈2 km not 200 m) and one on [[module-2-fiber-optics]] (`Δ = (n₁−n₂)/n₁`, plus the GRIN mode count `V²/4` and `B ≈ 0.7/τ`).

---

## The four modules

| Module | Topic | Page | Deep page size |
|---|---|---|---|
| **1** | Optics — interference, diffraction, polarization | [[module-1-optics-interference-diffraction]] | 81.5 KB |
| **2** | Optoelectronics — lasers & fiber optics | [[module-2-optoelectronics-lasers-fiber-optics]] | 73.2 KB |
| **3** | Quantum Mechanics | [[module-3-quantum-mechanics]] | 73.9 KB |
| **4** | Semiconductors & Electromagnetism | [[module-4-semiconductors-electromagnetism]] | 60.6 KB |

### What each module actually covers

**Module 1 — Optics: interference, diffraction & polarization** (deep page §1+)
Three-process radiation interaction → interference (YDSE, thin films, Newton's rings) → diffraction (single/double slit, grating, resolving power) → polarization. Companions: [[module-1-addendum-sem1-numericals-derivations]] (thin-film derivation + 12 solved numericals) and [[thin-film-interference-revision]] (short revision cut).

**Module 2 — Optoelectronics: lasers & fiber optics** (deep page §1+)
Einstein coefficients → population inversion → laser types → resonators & modes → fiber structure/propagation → attenuation & dispersion → optoelectronic devices (LED, photodiode, solar cell) → nonlinear optics.
- **Revision surface:** [[lasers-quick-ref]] — lasers only, 13 sections, 4 worked numericals, formula card, common-mistakes table
- **Deep page** carries a "use the quick-ref for exams" banner; it remains the owner of **fiber optics, NA/V-number, dispersion, EDFA/Raman, photodiodes, solar cells, nonlinear optics** — topics the quick-ref deliberately omits.

**Module 3 — Quantum Mechanics** (deep page §1+)
Historical foundations → wave-particle duality → wave function & Schrödinger equation → and onward. Note this is the foundation for the photon-energy relation that Module 2 lasers depends on ($E_2 - E_1 = h\nu$).

**Module 4 — Semiconductors & Electromagnetism** (deep page §1+)
Energy bands in solids → intrinsic semiconductors → extrinsic (doping) → and onward. Provides the p-n junction and band-gap background behind the Module 2 semiconductor laser ($\lambda = 1240/E_g$).

---

## Cross-module bridges

- **Module 3 → Module 2:** quantized energy levels are *why* lasers emit at discrete frequencies — `$E_2 - E_1 = h\nu$`.
- **Module 4 → Module 2:** the band gap `$E_g$` sets a semiconductor laser's wavelength via `$\lambda = 1240/E_g$` (eV·nm).
- **Module 1 → Module 2:** coherence length `$l_c = c/\Delta\nu$` explains the "coherent" property of laser light; Young's double-slit measures spatial coherence.
- **Module 2 ↔ Programming:** the fiber/laser stack is what runs long-haul links — see `Business/quant-finance/` only for market relevance, not physics.

---

## Source coverage

[[source-map-physics-sem1]] catalogues roughly **75 Sem-1 physics source files** across two raw-source trees. As of 2026-09-09 only **7 had ever been opened**; everything else is filename-level with topic guesses marked `speculation`. Known un-ingested material worth picking up next:

| Priority | Folder | Files | Topic |
|---|---|---|---|
| ~~3~~ | ~~`Module 2 Photonics/2.1 Laser/`~~ | ~~8~~ | **DONE 2026-10-02** — 4 text-rich papers opened and ingested → [[module-2-laser-fibre-question-bank]] + [[lasers-quick-ref]]. Remaining 4 are image-only slide decks, see below |
| ~~4~~ | ~~`Module 2 Photonics/2.2 Optical Fibre/`~~ | ~~6~~ | **DONE 2026-10-02** — 4 text-rich papers opened and ingested → [[module-2-fiber-optics]] + the question bank |
| 1 | `Semester 1/Physics/Physics Lab/` | 2 | `Physics Lab Manual 2025-26 SEM I final.pdf` (1.2 MB, unopened) — **prime candidate, one experiment at a time** |
| 2 | `Semester 1/Physics/` | 3 | `Syllabus_EP_Sem I.pdf` — would fix official module boundaries |
| 3 | `Module 2 Photonics/` image-only decks | 4 | `PPT on Laser.pdf` (28 pp), `PPT Optical Fibre.pdf` (22 pp), `PPT_Optical fiber .pdf` (49 pp), `Numericals on Laser PPT.pdf` (19 pp), `Laser-fundamentals-Slides.pdf` (14 pp) — **132 of 167 pages are images.** No OCR available (no tesseract/pytesseract/PIL), so these are blocked without installing OCR |
| 4 | `Module 3 Quantum Mechanics/` | 10 | incl. `Prof. Surens Notes` and solved numerical sets |
| 5 | `Module 4 Semiconductors/` | 9 | `Formula sheet`/`Notes`/`Numerical problems` by Dr. Suren Patwardhan |
| 6 | `Derivations/` | 3 remaining | thin-film pair only; the `Einstein_s Coefficients` + `Lasing Threshold` + `Numerical Aperture` files are now **superseded** by the faculty notes |

That file also notes: `Physics Lab Experiment Format.pdf` extracts **no text** (image-only) — do not quote it as text; it needs OCR.

---

## Open gaps in this domain

1. **No revision sheets for Modules 1, 3, 4** — only Module 2 has one. Modules 3 and 4 deep pages are 60–74 KB with no short cut.
2. **Physics lab has no write-up page** — the lab manual has never been opened, so there is no `lab-*` page for physics (unlike the SPM/chem/BEE labs).
3. **No `description:` frontmatter on three deep pages** — `module-2`, `module-3`, `module-4` lack the `description` field that the vault's Definition of Done requires. The mind plugin may warn on these; they are large hand-built pages, so a short description was never added.

---

## Cross-references

- Domain: [[01-Areas/Engineering/INDEX|Engineering domain hub]]
- **Revision first:** [[lasers-quick-ref]] · [[thin-film-interference-revision]] · [[module-1-addendum-sem1-numericals-derivations]]
- Source inventory: [[source-map-physics-sem1]]
- Course context: [[syllabus-316U06C107|SPM syllabus]] (the C course, for contrast) · [[assessment-guide-ese-ost-quiz]] (SPM exam patterns — note: no equivalent physics exam-pattern page exists yet)
