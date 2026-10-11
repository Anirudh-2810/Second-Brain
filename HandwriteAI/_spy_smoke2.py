"""Pick-spy v2: wrap cache lists so variants[pi] logs (char, pi)."""
import os, sys, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
import numpy as np
from PIL import Image
import inference as inf

style = json.load(open('styles/user_001.style'))
manifest, cache = inf.load_labeled('styles/user_001.labeled')
files_by_ch = manifest['chars']

picks = []  # (char, pi)

class SpyList(list):
    def __init__(self, ch, *a):
        super().__init__(*a)
        self._ch = ch
    def __getitem__(self, i):
        if isinstance(i, int):
            picks.append((self._ch, i))
        return super().__getitem__(i)

for ch in list(cache):
    cache[ch] = SpyList(ch, cache[ch])

# Patch load_labeled to return our spied cache
_orig = inf.load_labeled
def fake_load(lib_dir):
    return manifest, cache
inf.load_labeled = fake_load

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

# Replay walk: for each line, walk chars; every char WITH variants consumes
# >=1 picks (retries consume more). Align greedily: for a char, the LAST pick
# before the next char's first pick (or first pick if no retries) is used.
# Easier: for each char, the picks list slice until picks stop increasing for
# that char — but we don't have char boundaries in picks. Use position order:
# chars-with-variants appear in order; each char consumes >=1 picks; a char
# is done when the next pick belongs to the next variant-char. Since retries
# all belong to same char, we group: consecutive picks where grouping is
# determined by walking the text and consuming 1 pick per char first, then
# extra picks are retries attached to the PREVIOUS char.
flat = []
for cline in smoke.split('\n'):
    for ch in cline:
        if ch != ' ' and ch in cache:
            flat.append(ch)
# each variant-char consumes at least 1; extras are retries. Greedy: assign
# first len(flat) picks 1:1; extra picks beyond that go to retries of some
# char — but actual order interleaves retries inline. Proper replay: we know
# for each char exactly how many choices happened IF we instrument retries.
# Re-render with per-char pick counts instead.
picks.clear()
img = inf.render_labeled(smoke, style, 'styles/user_001.labeled', seed=7)
# group picks by char sequence alignment (dynamic): walk flat, for char c
# consume picks until we've consumed >=1 and the counts-so-far match... 
# Ambiguous. Print raw picks with char order for manual alignment instead.
print('total picks:', len(picks), 'variant-chars in text:', len(flat))
# Show picks only for problem letters
for i, (ch, pi) in enumerate(picks):
    if ch in 'ovebyl':
        fn = files_by_ch[ch][pi]
        print('%3d %s #%3d -> %s' % (i, ch, pi, fn))
