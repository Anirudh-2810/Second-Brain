---
module: "chemistry"
topic: "Organic Chemistry Reaction Map — Mechanisms & Named Reactions (JEE Advanced)"
tags: [chemistry, organic, reactions, mechanisms, jee, named-reactions]
last_updated: "2026-08-11"
source: "/raw-sources/Chem/Organic chemistry brahmastra handbook!.pdf, Kota notes"
---

# Organic Chemistry Reaction Map — Mechanisms & Named Reactions

> Complete reaction roadmap with mechanisms, conditions, and stereochemistry. Focus on arrow-pushing logic.

---

## 🎯 General Organic Chemistry (GOC) — Effect Hierarchy

| Effect | Order | Key Application |
|--------|-------|-----------------|
| **-I (Inductive)** | $NO_2 > CN > F > COOH > Cl > Br > I > OH > C_6H_5 > CH_3$ | Acid strength, carbocation stability |
| **+I (Inductive)** | $(CH_3)_3C^- > (CH_3)_2CH^- > CH_3CH_2^- > CH_3^-$ | Electron donation |
| **-R/-M (Resonance)** | $NO_2, CN, COOH, SO_3H, CHO, COR, COOR, CONH_2, X, OH, OR, NH_2, NHR, NR_2, SH, SR$ | Delocalization |
| **+R/+M (Resonance)** | $OH, OR, NH_2, NHR, NR_2, SH, SR$ | Electron donation |
| **Hyperconjugation** | $CH_3^- > 1^\circ > 2^\circ > 3^\circ$ (opposite of carbocation) | Alkene stability, carbocation stability |
| **Electromeric** | Temporary, reagent-induced | Addition reactions |

**Stability Orders:**
- Carbocation: $3^\circ \approx \text{allyl/benzyl} > 2^\circ > 1^\circ > CH_3^+$ (allyl/benzyl resonance stabilized)
- Carbanion: $CH_3^- > 1^\circ > 2^\circ > 3^\circ$ (opposite)
- Free Radical: $3^\circ > 2^\circ > 1^\circ > CH_3^\bullet$ (allyl/benzyl > 3°)
- Alkene: Tetrasubstituted > Tri > Di > Mono > Unsubstituted

---

## 🎯 Hydrocarbons — Reaction Map

### Alkanes
| Reaction | Reagent | Condition | Mechanism |
|----------|---------|-----------|-----------|
| Free Radical Substitution | $X_2$ ($Cl_2$, $Br_2$) | $h\nu$ or $\Delta$ | Radical chain (initiation, propagation, termination) |
| Combustion | $O_2$ | $\Delta$ | Radical |
| Pyrolysis | - | $500-600^\circ C$ | Radical (C-C cleavage) |

### Alkenes
| Reaction | Reagent | Condition | Regioselectivity | Stereochemistry |
|----------|---------|-----------|------------------|-----------------|
| **Electrophilic Addition** | | | | |
| $HX$ addition | $HCl, HBr, HI$ | - | Markovnikov (H to less sub. C) | Anti (via carbocation) |
| $HX$ + peroxide | $HBr + ROOR$ | - | **Anti-Markovnikov** (only HBr) | Anti |
| Hydration | $H_2O/H^+$ | Dil. $H_2SO_4$ | Markovnikov | - |
| Oxymercuration | $Hg(OAc)_2, H_2O$ then $NaBH_4$ | - | Markovnikov | Anti (no rearrangement) |
| Hydroboration | $B_2H_6$ then $H_2O_2/NaOH$ | - | **Anti-Markovnikov** | **Syn** |
| Halogenation | $Br_2/CCl_4$, $Cl_2$ | - | - | **Anti** (halonium ion) |
| Hypohalous acid | $HOCl, HOBr$ | $H_2O$ | OH to more sub. C | Anti |
| Epoxidation | $mCPBA$ or $H_2O_2/OH^-$ | - | - | **Syn** |
| Dihydroxylation | $OsO_4$ or $KMnO_4$ (cold, dil.) | - | - | **Syn** |
| Oxidative Cleavage | $O_3$ then $Zn/H_2O$ or $Me_2S$ | -78°C then RT | C=O products | - |
| $KMnO_4$ (hot, conc.) | - | Cleavage to acids/ketones | - | - |
| **Reduction** | | | | |
| Hydrogenation | $H_2/Pd-C, Pt, Ni$ | - | - | **Syn** |
| $Na/NH_3$ (Birch) | Aromatic rings | - | - | Trans (non-conjugated) |
| **Addition of Carbenes** | $CH_2I_2/Zn(Cu)$ | Simmons-Smith | - | Cyclopropanation (syn) |

### Alkynes
| Reaction | Reagent | Condition | Product |
|----------|---------|-----------|---------|
| Acidic H | $NaNH_2$, $AgNO_3/NH_3$ | - | Acetylide ($RC≡C^-Na^+$) |
| $H_2$ (1 eq) | Lindlar's cat. | - | **cis**-alkene |
| $H_2$ (excess) | $Pd-C$ | - | Alkane |
| $Na/NH_3$ | - | - | **trans**-alkene |
| Hydration | $HgSO_4/H_2SO_4$ | - | Methyl ketone (Markovnikov) |
| Hydroboration | $B_2H_6$ then $H_2O_2/NaOH$ | - | Aldehyde (Anti-Markovnikov) |
| Ozonolysis | $O_3$ then $Zn/H_2O$ | - | Carboxylic acids |

---

## 🎯 Alkyl Halides — Substitution & Elimination

### $S_N2$ (Bimolecular Nucleophilic Substitution)
| Feature | Detail |
|---------|--------|
| **Rate** | $k[R-X][Nu^-]$ |
| **Substrate** | $CH_3X > 1^\circ > 2^\circ \gg 3^\circ$ (no $3^\circ$) |
| **Nucleophile** | Strong ($I^-, CN^-, OH^-, RO^-, N_3^-, RS^-$) |
| **Solvent** | Polar **aprotic** (DMSO, DMF, acetone, $CH_3CN$) |
| **Stereochemistry** | **Inversion** (Walden) |
| **Rearrangement** | **No** |

### $S_N1$ (Unimolecular Nucleophilic Substitution)
| Feature | Detail |
|---------|--------|
| **Rate** | $k[R-X]$ |
| **Substrate** | $3^\circ > 2^\circ \gg 1^\circ$ (carbocation stability) |
| **Nucleophile** | Weak ($H_2O, ROH, CH_3COOH$) |
| **Solvent** | Polar **protic** ($H_2O, ROH$) |
| **Stereochemistry** | **Racemization** (planar carbocation) |
| **Rearrangement** | **Yes** (hydride/alkyl shift) |

### $E_2$ (Bimolecular Elimination)
| Feature | Detail |
|---------|--------|
| **Rate** | $k[R-X][Base]$ |
| **Base** | Strong, bulky ($t-BuOK, LDA, NaNH_2$) |
| **Geometry** | **Anti-periplanar** required |
| **Product** | Zaitsev (more substituted) normally; **Hofmann** with bulky base |
| **Rearrangement** | **No** |

### $E_1$ (Unimolecular Elimination)
| Feature | Detail |
|---------|--------|
| **Rate** | $k[R-X]$ |
| **Base** | Weak ($H_2O, ROH$) |
| **Substrate** | $3^\circ > 2^\circ$ |
| **Product** | Zaitsev (more substituted) |
| **Rearrangement** | **Yes** |

**Competition Guide:**
- $1^\circ$ halide + strong Nu$^-$ $\to$ $S_N2$
- $1^\circ$ halide + strong bulky base $\to$ $E_2$
- $3^\circ$ halide + weak Nu$^-$ $\to$ $S_N1/E_1$ mix
- $3^\circ$ halide + strong base $\to$ $E_2$

---

## 🎯 Alcohols, Phenols, Ethers

| Reaction | Reagent | Product | Notes |
|----------|---------|---------|-------|
| **Oxidation** | | | |
| $1^\circ$ alcohol | $PCC/CH_2Cl_2$ | Aldehyde | Stops at aldehyde |
| $1^\circ$ alcohol | $KMnO_4, K_2Cr_2O_7/H^+$ | Carboxylic acid | Over-oxidation |
| $2^\circ$ alcohol | $PCC, KMnO_4$ | Ketone | |
| $3^\circ$ alcohol | Strong oxidant | No reaction / cleavage | |
| **Dehydration** | Conc. $H_2SO_4$, $170^\circ C$ | Alkene | $E_1$, Zaitsev, rearrangement possible |
| **Esterification** | $RCOOH + R'OH \xrightleftharpoons{H^+}$ | Ester | Equilibrium, remove $H_2O$ |
| **Lucas Test** | $ZnCl_2/HCl$ | $3^\circ$: immediate; $2^\circ$: 5-10 min; $1^\circ$: no rxn | |
| **Phenol Acidity** | $pK_a \approx 10$ | - | e⁻ withdrawing $\uparrow$ acidity |
| **Ether Cleavage** | $HX$ (excess) | $R-X + R'-OH$ | $3^\circ$ alkyl $\to$ $S_N1$ |
| **Williamson Synthesis** | $RO^- + R'X$ | $R-O-R'$ | $S_N2$, works best for $1^\circ$ |

---

## 🎯 Carbonyl Compounds (Aldehydes & Ketones)

### Nucleophilic Addition
| Reaction | Reagent | Product | Notes |
|----------|---------|---------|-------|
| $HCN$ | $HCN + \text{trace } NaCN$ | Cyanohydrin | Base catalyzed |
| $NaHSO_3$ | $NaHSO_3$ | Bisulfite adduct | Separation/purification |
| $ROH$ | $ROH + H^+$ | Acetal/Ketal | Protect carbonyl |
| $NH_2OH$ | $NH_2OH$ | Oxime | |
| $PhNHNH_2$ | Phenylhydrazine | Phenylhydrazone | |
| $2,4-DNP$ | Brady's reagent | Yellow/orange ppt | Test for carbonyl |
| $RMgX$ (Grignard) | $RMgX$ then $H_3O^+$ | Alcohol ($1^\circ/2^\circ/3^\circ$) | $2$ eq for esters |
| $RLi$ (Organolithium) | $RLi$ then $H_3O^+$ | Alcohol | More reactive |
| $LiAlH_4$ | $LiAlH_4$ then $H_3O^+$ | $1^\circ$ alcohol (aldehyde), $2^\circ$ (ketone) | Strong |
| $NaBH_4$ | $NaBH_4$ | Alcohol | Mild, selective |
| $H_2/Ni$ | Catalytic hydrogenation | Alcohol | |

### Special Reactions
| Reaction | Substrate | Reagent | Product | Key Point |
|----------|-----------|---------|---------|-----------|
| **Aldol Condensation** | $\alpha$-H aldehyde/ketone | Dil. $NaOH$, $\Delta$ | $\beta$-hydroxy carbonyl $\to$ $\alpha,\beta$-unsaturated | Enolate formation |
| **Cross Aldol** | Two different | Controlled | Mixed | Use non-enolizable (formaldehyde, benzaldehyde) |
| **Cannizzaro** | No $\alpha$-H aldehyde | Conc. $NaOH$ | Alcohol + Acid | Disproportionation |
| **Haloform** | $CH_3CO-$ or $CH_3CH(OH)-$ | $X_2/OH^-$ ($Cl_2, Br_2, I_2$) | $CHX_3 + RCOO^-$ | $I_2/NaOH$ = iodoform test (yellow ppt) |
| **Tollen's Test** | Aldehyde | $Ag(NH_3)_2^+$ | Ag mirror | Aldehyde +ve |
| **Fehling's** | Aldehyde | $Cu^{2+}$ tartrate | Red $Cu_2O$ ppt | Aldehyde +ve |
| **Benedict's** | Aldehyde | $Cu^{2+}$ citrate | Red $Cu_2O$ ppt | Aldehyde +ve |
| **Schiff's Test** | Aldehyde | Fuchsin + $SO_2$ | Pink color | Aldehyde +ve |

---

## 🎯 Carboxylic Acids & Derivatives

### Reactivity Order: Acid Chloride > Anhydride > Ester > Amide > Carboxylate

| Conversion | Reagent | Notes |
|------------|---------|-------|
| Acid $\to$ Acid Chloride | $SOCl_2$, $PCl_5$, $(COCl)_2$ | |
| Acid $\to$ Ester | $R'OH + H^+$ (Fischer) | Equilibrium |
| Acid $\to$ Amide | $NH_3$ or $R_2NH$ (heat) | Via ammonium salt |
| Acid $\to$ Acid Chloride $\to$ Ester/Amide | $SOCl_2$ then $R'OH/R_2NH$ | Best route |
| Ester $\to$ Acid | $H_3O^+$ or $OH^-$ (saponification) | Hydrolysis |
| Ester $\to$ Alcohol | $LiAlH_4$ (2 eq) | $NaBH_4$ doesn't reduce esters |
| Amide $\to$ Amine | $LiAlH_4$ | Hofmann rearrangement also possible |
| Acid Chloride $\to$ Ketone | $R_2CuLi$ (Gilman) | Stops at ketone |
| Acid Chloride $\to$ Aldehyde | $LiAlH(OtBu)_3$ (Rosenmund) | Rosenmund-von Braun |

### Named Rearrangements
| Name | Substrate | Reagent | Product | Mechanism |
|------|-----------|---------|---------|-----------|
| **Hofmann** | Primary amide | $Br_2/NaOH$ | $1^\circ$ amine (1 C less) | Nitrene |
| **Curtius** | Acyl azide | $\Delta$ | $1^\circ$ amine (1 C less) | Nitrene |
| **Lossen** | Hydroxamic acid | Base/heat | $1^\circ$ amine | Nitrene |
| **Schmidt** | Carboxylic acid/ketone | $HN_3$ | Amine/amide | Nitrene |
| **Beckmann** | Oxime | $H_2SO_4/PCl_5$ | Amide (anti-migration) | Nitrenium |
| **Baeyer-Villiger** | Ketone | $mCPBA$ | Ester (more sub. migrates) | Criegee |
| **Favorskii** | $\alpha$-halo ketone | Base | Ester (ring contraction if cyclic) | Cyclopropanone |

---

## 🎯 Aromatic Compounds

### Electrophilic Aromatic Substitution (EAS)
| Reaction | Electrophile | Catalyst | Product | Director |
|----------|--------------|----------|---------|----------|
| Nitration | $NO_2^+$ | $HNO_3/H_2SO_4$ | Nitrobenzene | Meta (deactivating) |
| Sulfonation | $SO_3$ | $H_2SO_4$ (fuming) | Benzenesulfonic acid | Meta (deactivating) |
| Halogenation | $X^+$ | $FeX_3/AlX_3$ | Halobenzene | Ortho/Para (activating) |
| Friedel-Crafts Alkylation | $R^+$ | $AlCl_3$ | Alkylbenzene | Ortho/Para (activating) |
| Friedel-Crafts Acylation | $RCO^+$ | $AlCl_3$ | Acylbenzene | Meta (deactivating) |

**Directing Effects:**
| Activating (o/p) | Deactivating (o/p) | Deactivating (m) |
|------------------|-------------------|------------------|
| $-OH, -OR, -NH_2, -NHR, -NR_2, -SH, -SR$ | $-X, -CH=CH_2, -C≡CH$ | $-NO_2, -CN, -SO_3H, -CHO, -COR, -COOH, -COOR, -CONH_2, -CF_3, -NH_3^+$ |

**Reactivity:** Phenol > Aniline > Benzene > Chlorobenzene > Nitrobenzene

### Nucleophilic Aromatic Substitution (NAS)
| Type | Condition | Mechanism |
|------|-----------|-----------|
| **Addition-Elimination** | Strong e⁻ withdrawing ortho/para to leaving group | Meisenheimer complex |
| **Benzyne** | $NaNH_2$, $NH_3$, strong base | Elimination-Addition |

---

## 🎯 Named Reactions — Quick Index

| Reaction | Key Transformation | Key Reagent |
|----------|-------------------|-------------|
| **Aldol** | $\alpha$-H carbonyl $\to$ $\beta$-hydroxy carbonyl | $NaOH$ |
| **Claisen** | Ester $\to$ $\beta$-keto ester | $NaOEt$ |
| **Dieckmann** | Diester $\to$ cyclic $\beta$-keto ester | $NaOEt$ |
| **Michael** | Enolate + $\alpha,\beta$-unsaturated | $NaOH/EtOH$ |
| **Robinson Annulation** | Michael + Aldol | $\to$ cyclohexenone |
| **Mannich** | Carbonyl + $HCHO$ + $2^\circ$ amine | $\to$ $\beta$-amino carbonyl |
| **Knövenagel** | Active methylene + aldehyde | $\to$ $\alpha,\beta$-unsaturated |
| **Perkin** | Aromatic aldehyde + acid anhydride | $\to$ cinnamic acid |
| **Knoevenagel-Doebner** | + malonic acid | $\to$ acid |
| **Reformatsky** | $\alpha$-bromo ester + Zn + aldehyde | $\to$ $\beta$-hydroxy ester |
| **Wittig** | Phosphonium ylide + carbonyl | $\to$ alkene |
| **Horner-Wadsworth-Emmons** | Phosphonate + carbonyl | $\to$ $(E)$-alkene |
| **Julia** | Phenyl sulfone + carbonyl | $\to$ alkene |
| **McMurry** | $TiCl_4/Zn$ + carbonyl | $\to$ alkene (coupling) |
| **Pinacol** | Diol + $H^+$ | $\to$ ketone (rearrangement) |
| **Benzilic Acid** | Benzil + $OH^-$ | $\to$ benzilic acid |
| **Favorskii** | $\alpha$-halo ketone + base | $\to$ ester (ring contraction) |
| **Barton** | Nitrite ester + $hv$ | $\to$ $\delta$-nitro alcohol |

---

*Organic Chemistry reaction map — mechanisms first, memorize conditions second. Cross-reference with GOC effects for regioselectivity.*