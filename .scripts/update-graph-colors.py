"""Graph color scheme — user-selected 5-color palette (canonical).

Run anytime (idempotent):  python .scripts/update-graph-colors.py

Palette: #16335B navy / #A5ABBD light / #717788 slate / #58202D maroon / #8D4F5B rose
First match wins — specific paths before the 01-Areas catch-all.
"""
import os, json

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GP = os.path.join(VAULT, ".obsidian", "graph.json")

SCHEME = [
    ('path:"wiki/00-Current-Projects"', 0x16335B, "builds — navy"),
    ("path:'wiki/01-Areas/Roadmaps'",   0x717788, "roadmaps hub — slate"),
    ("path:'wiki/02-Resources'",        0x8D4F5B, "resources — rose"),
    ("path:'wiki/98-Archive'",          0xA5ABBD, "archive — light"),
    ("path:'wiki/99-Unsorted'",         0xA5ABBD, "unsorted — light"),
    ("path:'wiki/01-Areas'",            0x58202D, "core areas — maroon"),
]

cfg = {}
if os.path.exists(GP):
    try:
        cfg = json.load(open(GP, encoding="utf-8"))
    except Exception:
        cfg = {}

cfg["colorGroups"] = [
    {"query": q.replace("'", '"'), "color": {"a": 1, "rgb": rgb}} for q, rgb, _ in SCHEME
]
json.dump(cfg, open(GP, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

print("graph.json — 5-color palette applied:")
for q, rgb, note in SCHEME:
    print(f"  #{rgb:06x}  {note}")