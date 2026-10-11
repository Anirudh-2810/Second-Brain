import os, sys, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw
manifest = json.load(open('styles/user_001.labeled/manifest.json'))
# e suspects + o suspects + g lined crops
fns = ['c61_e_259.png','c61_e_184.png','c25_e_070.png','c62_e_299.png',
       'c53_e_133.png','c53_e_158.png','c61_e_182.png',
       'c55_o_038.png','c59_o_050.png','c55_o_021.png',
       'c45_g_003.png','c45_g_004.png','c45_g_001.png']
sheet = Image.new('RGB', (120*7, 160*2), 'white')
d = ImageDraw.Draw(sheet)
for j, fn in enumerate(fns):
    p = os.path.join('styles/user_001.labeled', fn)
    if not os.path.exists(p): print('missing', fn); continue
    im = Image.open(p).convert('RGB').resize((100,100), Image.NEAREST)
    x, y = (j%7)*120+10, (j//7)*160+40
    sheet.paste(im, (x, y))
    d.text((x-6, y-22), fn.replace('.png',''), fill='red')
sheet.save('Test_input/suspects2.png')
print('ok')
