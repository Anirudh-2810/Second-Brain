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

## Part 3.5 — R&D Extension: D3 Layout Math + bpy Operator Anatomy

### D3 tree layout intuition
`d3.tree()` solves: given a hierarchy, assign x (position among leaves) and y (depth) so subtrees don't overlap. Nodes post-layout carry x,y — you draw links as bezier curves between parent-child coordinates. Your family twist: spouses are dual-node units (render couple card; children link to COUPLE midpoint, not one parent). Generational alignment breaks with marrying-cousins (DAG!) — detect cycles, fall back to force layout for weird subgraphs.

```javascript
const root = d3.hierarchy(familyData, d => d.children);
d3.tree().nodeSize([cardW+gap, depthH])(root);
svg.selectAll('g.node').data(root.descendants()).join(...) // cards
svg.selectAll('path.link').data(root.links()).join(...)     // curves
```

### Blender add-on skeleton (the universal triad)
```python
bl_info = {"name":"MyTools","version":(0,1,0),"category":"Object"}
import bpy
class MYTOOLS_OT_rename(bpy.types.Operator):
    bl_idname = "mytools.rename"; bl_label = "Prefix Rename"
    prefix: bpy.props.StringProperty(default="obj_")
    def execute(self, context):
        for i, ob in enumerate(context.selected_objects):
            ob.name = f"{self.prefix}{i:03d}"
        return {'FINISHED'}
class MYTOOLS_PT_panel(bpy.types.Panel):
    bl_label = "MyTools"; bl_space_type='VIEW_3D'; bl_region_type='UI'
    def draw(self, ctx):
        self.layout.operator(MYTOOLS_OT_rename.bl_idname)
classes = (MYTOOLS_OT_rename, MYTOOLS_PT_panel)
def register():
    for c in classes: bpy.utils.register_class(c)
def unregister():
    for c in reversed(classes): bpy.utils.unregister_class(c)
```
The triad transfers: VSCode/Obsidian/Figma plugins share register/action/UI DNA.


## Part 4 — Life Integration

- Build A = genuine family artifact (gift potential!) + portfolio viz piece
- Build B unlocks the entire plugin-economy skill (Blender/Obsidian/VSCode/Figma plugins share the registration-operator-panel DNA)
- Metrics: artifacts used by real humans · add-on skeleton reusable

## Part 6 — Internals Push: GEDCOM Format + bpy Registration Deep

### GEDCOM in five lines
Genealogy interchange format: lines of LEVEL TAG VALUE — `0 @I1@ INDI` starts an individual; `1 BIRT` birth event; `2 DATE 1969`; `1 FAMC @F1@` child-to-family link. Hierarchy purely by level numbers. TreeMaker-class tools ingest GEDCOM or simplified JSON. Lesson: ancient line-level formats persist because diff-friendly and stream-parseable.

### bpy registration deep — why classes, not functions
Blender maintains a live type system: registered Operators become undo-pushable, hotkey-mappable, callable via bpy.ops, searchable in F3. Panels introspect poll() for context-sensitivity; PropertyGroups persist inside .blend files and participate in undo. The ceremony enrolls your code into Blender's undo/menu/persistence subsystems — unregistered functions run but integrate with nothing.

### Version-churn strategy
Blender breaks the Python API across major releases (2.8x, 3.x, 4.x each moved things). Sustainable add-ons pin supported versions in bl_info and gate version-specific imports — maintenance burden of platform-adjacent tools is structural, not accidental.

## Checkpoint Questions

1. In your D3 tree, what breaks when two siblings marry into the same family (DAG vs tree)?
2. Why does Blender route everything through Operators — what do undo/hotkeys gain?
3. Which YOUR-workflow pain is one panel+operator away from solved?

## Cross-Vault Links

[[modules/case-studies/index|Field Index]] · [[build-project-playbook]] · [[modules/automations/money/earn-with-n8n]]