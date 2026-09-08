---
course_code: "ENG-BIO"
course_name: "Engineering Biology"
unit: "Unit 2B — Bioinformatics (FASTA & BLAST)"
tags: [btech, engineering-biology, bioinformatics, fasta, blast, sequence-alignment, databases]
last_updated: "2026-09-09"
description: "Unit 2B notes: bioinformatics scope, sequence databases, FASTA vs BLAST algorithms and variants, E-values, and the data-to-discovery pipeline with applications."
---

## For future agent

Ingest of `Bio/Unit 2 .../Introduction-to-Bioinformatics.pptx`. Wet-lab companion: [[unit-2-cell-biology-central-dogma]] (the sequences being searched). Pathway databases (KEGG/Reactome) continue in [[unit-5-systems-biology]].

# Unit 2B — Bioinformatics

## 1. Scope

Biology + CS + maths + IT: store, analyse, interpret DNA/RNA/protein sequences with computational tools. Pipeline: **Databases → Alignment → Analysis → Research → Submit new data** (cycle back into databases).

## 2. FASTA (Lipman & Pearson, 1985; FAST-All)

Word-search short fragments → score → extend → optimise best alignments. Output: alignment score. Strength: accurate on small datasets, DNA + protein; weakness: slow on huge databases.

## 3. BLAST (Altschul et al., NCBI, 1990; local alignment)

Query → short words (3 aa proteins / 11 nt DNA) → database word-match → extend → score + **E-value** statistics. Variants (memorize): **blastn** (nt vs nt) · **blastp** (protein vs protein) · **blastx** (translated nt vs protein) · **tblastn** (protein vs translated nt) · **tblastx** (translated vs translated).

## 4. FASTA vs BLAST (exam table)

| | FASTA | BLAST |
|---|---|---|
| Alignment | Global or local | Local |
| Speed | Slower | Faster (large DBs) |
| Output | Score only | Score + E-value + stats |
| Best for | Small datasets | Large database search |
| Misses | — | Weak similarities possible |

E-value = expected random hits at that score — lower is more significant. Uses: homology/evolution, gene-function prediction, conserved domains/mutations, genome annotation, drug discovery/functional genomics.
