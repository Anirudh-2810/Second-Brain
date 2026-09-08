---
course_code: "ENG-BIO"
course_name: "Engineering Biology"
unit: "Unit 1 — Biomolecules & Enzymes"
tags: [btech, engineering-biology, biomolecules, carbohydrates, proteins, nucleic-acids, enzymes, michaelis-menten]
last_updated: "2026-09-09"
description: "Unit 1 notes: carbohydrate/protein/nucleic-acid structure-function, enzyme catalysis, Michaelis–Menten kinetics and competitive/non-competitive/uncompetitive inhibition with engineering uses."
---

## For future agent

Ingest of `Bio/Unit 1 Biomolecules and Enzymes/Lecture 1.pptx` (carbs, amino acids, proteins + eng. applications), `Lecture 2 - 3.pptx` (nucleic acids, enzyme intro), `Lecture 4.pptx` (kinetics, inhibition, IA1 industrial-enzyme brief). Central dogma continues in [[unit-2-cell-biology-central-dogma]]. Chemistry depth: [[../chemistry/overview|Chemistry overview]] § Biomolecules.

# Unit 1 — Biomolecules & Enzymes

## 1. Carbohydrates

Roles: chief energy source; glycogen (animal) / starch (plant) storage; biosynthesis intermediates; nerve-tissue regulation (brain fuel); structural (cellulose cell walls); cell–cell signalling. Engineering uses: **glucose biosensors** (glucose oxidase → electrical signal ∝ [glucose]; enzyme immobilisation + microelectronics), **starch bioplastics** (cheap, film-forming, compostable packaging), **cellulose** in paper/textiles/biocomposites ($\beta$-glucose chains → H-bonded tensile strength).

## 2. Amino acids & proteins

Amino acid = $-\mathrm{NH_2}$ + $-\mathrm{COOH}$ + R-group (R sets charge/solubility). Essential (Val, Met, Ile, Lys, Leu, Trp, Thr, Phe — body cannot make), semi-essential (Arg, His — insufficient in children), non-essential (Gly, Ala, Cys, Tyr, Pro, Ser, Asn, Gln, Asp, Glu). Peptide bond (amide) links residues: di-/tri-/polypeptide; protein ≈ 50+ residues (>5000 Da). Structure ladder: **primary** (sequence) → **secondary** ($\alpha$-helix, $\beta$-sheet) → tertiary → quaternary.

## 3. Nucleic acids

DNA→RNA→protein (central dogma). mRNA (message + eukaryotic 5′-cap/poly-A tail), tRNA (anticodon + 3′ amino-acid acceptor; charged by aminoacyl-tRNA synthetase), rRNA (ribosome core; 70S prokaryote / 80S eukaryote; A/P/E sites), miRNA (RISC-guided silencing). Backbone: **phosphodiester** 3′→5′ links; strands held by **H-bonds** (A–T/U, C–G) — weak enough to unzip for replication/transcription.

## 4. Enzyme kinetics

E + S ⇌ ES → E + P at the active site. Michaelis–Menten:

$$v_0 = \frac{V_{max}\,[S]}{K_m + [S]}$$

$K_m$ = [S] at $v_0 = V_{max}/2$ (inverse affinity). Urease drill (source): $[S] = 0.03$, $K_m = 0.06$, $v_0 = 1.5\times10^{-3}$ → $V_{max} = v_0(K_m+[S])/[S] = 4.5\times10^{-3}\ \mathrm{mmol\,L^{-1}\,min^{-1}}$.

## 5. Reversible inhibition (memorize table)

| Type | Binds | $V_{max}$ | $K_m$ | Overcome by [S]? |
|------|-------|-----------|-------|------------------|
| Competitive | Active site (vs S) | unchanged | ↑ apparent | Yes |
| Non-competitive | Elsewhere (E or ES) | ↓ | unchanged | No |
| Uncompetitive | ES complex only | ↓ | ↓ apparent | No (worsens) |

Drug-design relevance: inhibitor class is read straight off the Lineweaver–Burk pattern. IA1 brief (industrial enzyme, e.g. amylase/protease/lactase): report enzyme role + process conditions + product with referenced picture.
