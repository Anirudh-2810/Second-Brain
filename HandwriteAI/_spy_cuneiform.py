import os, sys, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
import inference as inf
import profiles

info = profiles.resolve("")
style = json.load(open(info["style"]))
manifest, cache = inf.load_labeled(info["labeled"])
files_by_ch = manifest['chars']
picks = []


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
inf.load_labeled = lambda lib_dir: (manifest, cache)

para = (
    "Cuneiform is one of the earliest writing systems, developed "
    "in southern mesopotamia around 3400 BCE. Scribes pressed "
    "wedge-shaped marks into wet clay tablets using a cut reed "
    "stylus. Most surviving tablets come from iraq and syria, "
    "where thousands remain legible after five thousand years. "
    "The script recorded laws, contracts, receipts, myths, and "
    "astronomical tables. Rate of decipherment improved sharply "
    "once bilingual inscriptions surfaced. Organ builders even "
    "reused clay tokens as tallies. Texts written in the late "
    "period show tremendous variety in ductus and spacing. "
    "Testing the script against monumental inscriptions reveals "
    "surprising consistency in sign structure. What survives is "
    "fragmented, yet the wedges still speak."
)
inf.render_labeled(para, style, info["labeled"], seed=7)

# align with retry repair: the aspect check may sample twice for one char
# (try1 discarded on aspect fail, try2 renders). Find the extra pick index
# to drop so the ch-sequence matches the text exactly; when the retry pair
# is (ch,a),(ch,b) both drop positions align — keep the LATER pick (the
# final try that actually rendered) by dropping the earlier index.
T = [ch for line in para.split('\n') for ch in line if ch != ' ' and ch in cache]
Pch = [p[0] for p in picks]
valid_d = [d for d in range(len(Pch)) if Pch[:d] + Pch[d + 1:] == T]
if len(picks) != len(T):
    print('retry repair: drop candidates', valid_d[:10],
          '(%d total)' % len(valid_d))
if not valid_d:
    raise SystemExit('cannot align picks to text')
d = min(valid_d) if len(valid_d) > 1 else valid_d[0]
picks = picks[:d] + picks[d + 1:]
assert [p[0] for p in picks] == T, 'alignment still broken'

pi = 0
aligned = []
for cline in para.split('\n'):
    row = []
    for ch in cline:
        if ch == ' ':
            row.append(' ')
        elif ch in cache:
            cpi = picks[pi][1]
            pi += 1
            row.append('%s[%s]' % (ch, files_by_ch[ch][cpi].replace('.png', '')))
        else:
            row.append('%s[FB]' % ch)
    aligned.append(''.join(row))
for row in aligned:
    print('ROW:', row)
