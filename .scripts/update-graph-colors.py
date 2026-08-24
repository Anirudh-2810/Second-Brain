"""Graph color scheme — curated dark-theme domain coding (canonical).

Run anytime (idempotent):  python .scripts/update-graph-colors.py

Design:
  - Domain-level colors only (sub-modules inherit parent) = readable legend
  - Jewel tones, s~0.68 l~0.56: vivid on near-black, zero glare
  - Builds = amber (active work pops warm), AI = violet, coding = emerald
  - Archive/Unsorted fade to near-invisible gray
"""
import os, json

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GP = os.path.join(VAULT, '.obsidian', 'graph.json')

SCHEME = [
    # (query, hex, meaning)
    ('path:"wiki/00-Current-Projects"',       0xf5a623, 'builds — amber: active work pops'),
    ('path:"wiki/01-Areas/Programming"',      0x2ec4a0, 'programming — emerald'),
    ('path:"wiki/01-Areas/AI-Data"',          0x9d6ff3, 'AI/data — violet'),
    ('path:"wiki/01-Areas/Business"',         0x4a90d9, 'business — steel blue'),
    ('path:"wiki/01-Areas/Engineering"',      0x7a8ba3, 'engineering — slate steel'),
    ('path:"wiki/01-Areas/Self-Dev"',         0xe8637c, 'self-dev — coral'),
    ('path:"wiki/01-Areas/Roadmaps"',         0x3fd4d4, 'roadmaps hub — bright cyan'),
    ('path:"wiki/02-Resources"',              0x8fa663, 'resources — muted sage'),
    ('path:"wiki/98-Archive"',                0x4a4a55, 'archive — fade out'),
    ('path:"wiki/99-Unsorted"',               0x4a4a55, 'unsorted — fade out'),
]

cfg = {}
if os.path.exists(GP):
    try:
        cfg = json.load(open(GP, encoding='utf-8'))
    except Exception:
        cfg = {}

cfg['colorGroups'] = [
    {'query': q, 'color': {'a': 1, 'rgb': rgb}} for q, rgb, _ in SCHEME
]
json.dump(cfg, open(GP, 'w', encoding='utf-8'), indent=2, ensure_ascii=False)

print('graph.json — curated dark-theme domain scheme applied:\n')
for q, rgb, note in SCHEME:
    print(f'  #{rgb:06x}  {q:38s} {note}')
