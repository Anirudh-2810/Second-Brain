"""Assign a DISTINCT graph color to every module folder (full-depth discovery).

Run after creating any new module:  python .scripts/update-graph-colors.py
"""
import os, json, colorsys

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GP = os.path.join(VAULT, '.obsidian', 'graph.json')
WIKI = os.path.join(VAULT, 'wiki')

modules = []
for root, dirs, files in os.walk(WIKI):
    dirs[:] = [d for d in dirs if d != '.obsidian']
    md_files = [f for f in files if f.endswith('.md') and f != 'log.md']
    if not md_files:
        continue
    rel = os.path.relpath(root, VAULT).replace(os.sep, '/')
    if rel == 'wiki':          # vault-level index/log — not a module
        continue
    name = os.path.basename(rel)
    modules.append((rel, name))

modules.sort()

def rgb_int(hue_deg, s=0.65, l=0.6):
    r, g, b = colorsys.hls_to_rgb((hue_deg % 360) / 360, l, s)
    return (int(r * 255) << 16) + (int(g * 255) << 8) + int(b * 255)

groups = []
for i, (rel, name) in enumerate(modules):
    hue = i * 137.508
    groups.append({
        'query': f'path:"{rel}"',
        'color': {'a': 1, 'rgb': rgb_int(hue)},
    })

cfg = {}
if os.path.exists(GP):
    try:
        cfg = json.load(open(GP, encoding='utf-8'))
    except Exception:
        cfg = {}
cfg['colorGroups'] = groups
json.dump(cfg, open(GP, 'w', encoding='utf-8'), indent=2, ensure_ascii=False)
print(f'graph.json: {len(groups)} module color groups written\n')
for g in groups:
    print(f"  {g['query']:55s} {hex(g['color']['rgb'])}")
