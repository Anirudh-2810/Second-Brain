import os, sys, json, re
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
import numpy as np
from PIL import Image, ImageDraw
import inference as inf

style = json.load(open('styles/user_001.style'))
manifest, cache = inf.load_labeled('styles/user_001.labeled')
files_by_ch = manifest['chars']
picks = []
class SpyList(list):
    def __init__(self, ch, *a):
        super().__init__(*a); self._ch = ch
    def __getitem__(self, i):
        if isinstance(i, int): picks.append((self._ch, i))
        return super().__getitem__(i)
for ch in list(cache): cache[ch] = SpyList(ch, cache[ch])
inf.load_labeled = lambda lib_dir: (manifest, cache)

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
inf.render_labeled(smoke, style, 'styles/user_001.labeled', seed=7)
pi = 0
aligned = []
for cline in smoke.split('\n'):
    row = []
    for ch in cline:
        if ch == ' ':
            row.append(' ')
        elif ch in cache:
            cpi = picks[pi][1]; pi += 1
            row.append('%s[%s]' % (ch, files_by_ch[ch][cpi].replace('.png','')))
        else:
            row.append('%s[FB]' % ch)
    aligned.append(''.join(row))
# print words of interest with full alignment
for row in aligned:
    print('ROW:', row)
    print()
