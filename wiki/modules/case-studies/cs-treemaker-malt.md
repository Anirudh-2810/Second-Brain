---
course_code: "CASESTUDY"
course_name: "Open-Source Case Studies"
unit: "Case Study 13 — wesen/TreeMaker + bnpr/Malt [Deep R&D + Build Edition]"
tags: [d3, visualization, blender, python, creative-coding, niche-tools, case-study, build-plan]
last_updated: "2026-08-24"
confidence: "medium"
source: "https://github.com/wesen/TreeMaker + https://github.com/bnpr/Malt (partial fetches; analysis from project knowledge — verify specifics in-repo)"
---

## For future agent
Deep-dive on both creative tools with code-level inventories (TreeMaker: D3 layouts over genealogy data; Malt: Blender bpy add-on architecture) and buildable versions — **your own family-tree D3 page** and **a first Blender add-on skeleton**. Both are weekend-scale and teach plugin/data-viz patterns transferable everywhere.

# Niche Creative Tools — Deep R&D

## Part 1A — TreeMaker Code Inventory

| Piece | Tech | Mechanism |
|-------|------|-----------|
| Data loader | JS | Parses genealogy data (GEDCOM-derived/JSON) into person nodes + parent links |
| **Layout engine** | **D3.js** tree/cluster layout | Computes x/y positions across generations; handles pan/zoom viewport |
| Renderer | D3 + SVG | Nodes as cards (photo/name/dates), links as curved paths |
| Interaction | D3 behaviors | Zoom-to-subtree, click-for-details |

**Why D3**: family trees are graph-layout problems where control matters more than convenience — D3 gives primitives (scales, shapes, zoom behavior) instead of a fixed chart.

## Part 1B — Malt Code Inventory (Blender add-on pattern)

| Piece | Tech | Mechanism |
|-------|------|-----------|
| `bl_info` manifest | Python dict | Add-on identity/version shown in Blender prefs |
| **Operator classes** | `bpy.types.Operator` | The actions (bake material, export textures) with `execute()` |
| **Panel classes** | `bpy.types.Panel` | UI sections in the sidebar via `layout` API |
| **Property groups** | `bpy.props.*` | Persisted settings per scene |
| Registration trio | `register()/unregister()` | Classes enrolled into Blender's type system on enable |

This triad (**Operator / Panel / PropertyGroup + register**) is the universal shape of EVERY Blender add-on — learn it once, read any add-on.

## Part 2 — Why These Designs

| Choice | Rationale |
|--------|-----------|
| TreeMaker: D3 not a chart library | Family trees need custom orientation/generational spacing; D3 = layout primitives you compose |
| TreeMaker: client-side only | Genealogy data is private; zero-server tool respects that |
| Malt: bpy Operator pattern | Blender's core is operator-centric (undo, scripting, hotkeys all route through operators) — add-ons inherit consistency for free |
| Malt: panel-in-sidebar | Lives where artists already work — adoption through placement |

**Niche-tool thesis**: both succeed by serving ONE acute workflow deeply. Small audience × acute pain × deep fit > broad shallow tools.

## Part 3 — Can I Build My Own Versions? ✅ BOTH weekend-scale

### Build A: **Your Family Tree in D3** ✅
```
M1: CSV of 15+ relatives (id, name, birth, parents)
M2: Parse → D3.tree layout → SVG render with names/dates
M3: Pan/zoom; click node → detail card
M4: Add spouse handling OR photos; deploy GitHub Pages
Failure modes: cycles in bad data (validate DAG), huge trees
(clip to descendants-of-root), privacy (use initials if publishing).
```

### Build B: **First Blender Add-On Skeleton** ✅
```
M1: Installable empty add-on (manifest + register) showing panel "MyTools"
M2: One operator: batch-rename selected objects with prefix input
M3: One PropertyGroup setting persisted per scene
M4: Real utility: e.g., auto-setup render settings for your vlogs
Failure modes: Blender version API churn (pin version), UI-layout
API verbosity (copy official template add-on shape).
```

## Part 4 — Life Integration

- Build A = genuine family artifact (gift potential!) + portfolio viz piece
- Build B unlocks the entire plugin-economy skill (Blender/Obsidian/VSCode/Figma plugins share the registration-operator-panel DNA)
- Metrics: artifacts used by real humans · add-on skeleton reusable

## Checkpoint Questions

1. In your D3 tree, what breaks when two siblings marry into the same family (DAG vs tree)?
2. Why does Blender route everything through Operators — what do undo/hotkeys gain?
3. Which YOUR-workflow pain is one panel+operator away from solved?

## Cross-Vault Links

[[modules/case-studies/index|Field Index]] · [[build-project-playbook]] · [[modules/automations/money/earn-with-n8n]]