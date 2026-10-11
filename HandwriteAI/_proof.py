import sys, json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
style = json.load(open('styles/user_001.style'))
from inference import render_labeled
tests = [
    ('abcdefghijklmnopqrstuvwxyz', 'Az-lower'),
    ('ABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789', 'Az-up-digits'),
    ('.,!?;:\'\"()-+=/&', 'punct'),
    ('were you u it in have to check', 'words'),
    ('you were maybe over your old dream purple gold', 'words2'),
]
for text, stem in tests:
    img = render_labeled(text, style, 'styles/user_001.labeled', seed=7, style_strength=1.0)
    out = f'outputs/Proof-{stem}-seed7.png'
    img.save(out)
    print('saved', out, img.size)
