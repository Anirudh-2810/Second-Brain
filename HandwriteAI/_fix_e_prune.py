"""Recover from letter-wide/local index mixup, then apply CORRECT e-prune.
Sheet verdicts (E-worst48, q<=0.10): stems/hooks/C-shapes/theta = junk;
blurry-but-e reads = keep."""
import json, os, sys, hashlib
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
from cluster import _resolve_lib

cdir = 'styles/user_001.clusters'
lab_dir = 'styles/user_001.labeled'
p = json.load(open(os.path.join(cdir, 'clusters.json')))
lib = _resolve_lib(cdir, p['lib'])

# 1) restore wrongly-dropped members via byte match (labeled copy == source bytes)
def md5(path):
    return hashlib.md5(open(path, 'rb').read()).hexdigest()

lib_hashes = {}
for fn in os.listdir(lib):
    if fn.lower().endswith('.png'):
        lib_hashes.setdefault(md5(os.path.join(lib, fn)), fn)

for lab_name, cid, expected_count in [('c53_e_184.png', '53', 110),
                                      ('c25_e_052.png', '25', 74)]:
    src_fn = lib_hashes.get(md5(os.path.join(lab_dir, lab_name)))
    if src_fn is None:
        print('RESTORE FAILED for', lab_name)
        sys.exit(1)
    p['clusters'][cid].append(src_fn)
    print(f'restored {src_fn} -> c{cid} (now {len(p["clusters"][cid])})')

# 2) correct drops. c25 already has exactly the right 4 removed (bad pass
# removed {0,9,23,52,65}, we restored 52). c53's list is mutated: original
# 105 was removed then re-appended at the end, so originals 108,109,110
# now sit at positions 107,108,109; originals <105 keep their positions.
drops = {
    '53': [21, 51, 63, 67, 100, 107, 108, 109],
    '61': [18, 56],
    '62': [8, 14, 21, 23, 39, 51, 59, 67, 70, 71],
}
for cid, idxs in drops.items():
    mem = p['clusters'][cid]
    s = set(idxs)
    keep = [m for i, m in enumerate(mem) if i not in s]
    print(f'c{cid}: {len(mem)} -> {len(keep)}')
    p['clusters'][cid] = keep

json.dump(p, open(os.path.join(cdir, 'clusters.json'), 'w'), indent=1)
total = sum(len(p['clusters'][c]) for c in ('25', '53', '61', '62'))
print('e total now:', total)

from cluster import apply_labels
man = apply_labels(cdir, p['labels'], 'styles/user_001.labeled')
print('labeled glyphs:', man['n_glyphs'])
