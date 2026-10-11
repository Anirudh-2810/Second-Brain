"""Align picks 1:1 to text; print word-by-word for problem words."""
import os, sys, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
import numpy as np
from PIL import Image
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

# 1:1 align
pi = 0
out = []
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
    out.append(''.join(row))
for row in out:
    print(row[:400])
print('consumed', pi, 'of', len(picks))

# Build zoom sheet of suspects
suspects = []
for cline in smoke.split('\n'):
    pass
# extract from aligned strings: problem crops
import re
for row in out:
    for m in re.finditer(r'\w\[(c\d+_[a-z]+_\d+)\]', row):
        fn = m.group(1)
        if fn in ('c43_l_034','c43_l_017','c0_v_017','c0_v_002','c42_b_021',
                  'c53_e_170','c55_o_038','c25_e_070','c43_l_045','c43_l_042',
                  'c55_o_021','c42_b_057','c42_b_020'):
            suspects.append(fn)
# also add all w picks and all v picks and c45 g picks for context
for ch, idx in picks:
    fn = files_by_ch[ch][idx].replace('.png','')
    if ch in 'wv' and fn not in suspects:
        suspects.append(fn)
suspects = sorted(set(suspects))
sheet = Image.new('RGB', (120*7, 160*((len(suspects)+6)//7)), 'white')
from PIL import ImageDraw
d = ImageDraw.Draw(sheet)
lab = 'styles/user_001.labeled'
for j, fn in enumerate(suspects):
    im = Image.open(os.path.join(lab, fn + '.png')).convert('RGB')
    im = im.resize((100, 100), Image.NEAREST)
    x, y = (j%7)*120+10, (j//7)*160+40
    sheet.paste(im, (x, y))
    d.text((x-6, y-22), fn, fill='red')
sheet.save('Test_input/suspects-smoke.png')
print('suspects sheet:', suspects)
