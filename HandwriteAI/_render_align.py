import sys
sys.path.insert(0, '.')
from profiles import resolve
import inference as inf

p = resolve('')
style = inf.load_style(p['style'])
para = (
    'Cuneiform script is one of the earliest systems of writing,\n'
    'distinguished from the mostly pictographic logs of other\n'
    'ancient scripts by using a combination of logophonetic,\n'
    'cuneiform syllabary and alphabetic signs. The direction of\n'
    'writing was varied over time in a rather complex evolution\n'
    'and was written in boxes. This script was written on\n'
    'tablets of clay that were dried in the sun or, especially\n'
    'in later periods, tablets were baked in a kiln, making them\n'
    'durable. Scribes would use a reed stylus to press the signs\n'
    'into soft clay. After drying, the tablets could be stored\n'
    'in archive rooms in temples or palaces. Cuneiform tablets\n'
    'have been unearthed in sites across the Middle East, from\n'
    'Egypt to Anatolia and Iran. The language of the tablets is\n'
    'not a single language but includes Sumerian, Akkadian,\n'
    'Eblaite, Elamite, Hittite, Hurrian and Urartian.'
)
img = inf.render_labeled(para, style, p['labeled'], seed=7)
img.save('outputs/align-fix-cuneiform.png')
print('saved outputs/align-fix-cuneiform.png', img.size)
img2 = inf.render_labeled(
    'The quick brown fox jumps over the lazy dog. '
    'We hold these truths to be self-evident, that all men are created equal. '
    'Again and again the wr band struck, but the firm ridge held.',
    style, p['labeled'], seed=7)
img2.save('outputs/align-fix-smoke.png')
print('saved outputs/align-fix-smoke.png', img2.size)
