"""Pick-spy: render smoke text, log every glyph pick -> labeled filename."""
import os, sys, json, hashlib
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
import numpy as np
from PIL import Image
import inference as inf

style = json.load(open('styles/user_001.style'))
manifest, cache = inf.load_labeled('styles/user_001.labeled')
files_by_ch = manifest['chars']
log = []

_real_rng = np.random.default_rng
class SpyRng:
    def __init__(self, real, tag):
        object.__setattr__(self, '_r', real)
        object.__setattr__(self, '_tag', tag)
    def __getattr__(self, name):
        return getattr(object.__getattribute__(self, '_r'), name)
    def choice(self, n, p=None, **kw):
        r = object.__getattribute__(self, '_r').choice(n, p=p, **kw)
        object.__getattribute__(self, '_log').append((object.__getattribute__(self, '_tag'), int(r)))
        return r
    def __setattr__(self, k, v):
        object.__setattr__(self, k, v)

# attach log list after class def
SpyRng._log = []

def patched_rng(*a, **k):
    r = _real_rng(*a, **k)
    s = SpyRng(r, tuple(a))
    return s
np.random.default_rng = patched_rng

smoke = (
    "Smoking is deeply injurious to health because it introduces "
    "dangerous toxic chemicals like nicotine, tar, and carbon "
    "monoxide directly into the body.\n\n"
    "The Dangers of Smoking\n\n"
    "Severe Organ Damage: Inhaling "
    "tobacco smoke harms nearly "
    "every organ, damaging the lungs, "
    "heart, and blood vessels"
)
img = inf.render_labeled(smoke, style, 'styles/user_001.labeled', seed=7)

# Replay the pick sequence per line: we know lrng seeds; instead of replaying,
# re-walk: for each line, rng = default_rng(seed*1000+li*77+11) — choices are
# interleaved with normal/uniform calls, so reconstructing order is fragile.
# Simpler: monkeypatch at a higher level. We already logged (seedtuple, idx)
# per choice call IN ORDER. Map order -> (line, char) by re-simulating which
# chars have variants in each line.
seed = 7
log = SpyRng._log
li = 0
ci_in_line_choice = 0
mapped = []
for cline in smoke.split('\n'):
    ch_choice_seq = []
    for ch in cline:
        if ch == ' ':
            continue
        if ch in cache:
            ch_choice_seq.append(ch)
    # not exact: retries (up to 3 choices per char) break 1:1 mapping.
    # So instead print raw log length and do a looser analysis.
    mapped.append((li, ch_choice_seq))
    li += 1
print('total choice calls:', len(log))
print('chars-with-variants per line:', [len(s) for _, s in mapped])
