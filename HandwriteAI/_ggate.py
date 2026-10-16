"""g-gate + smoking paragraph after g restore."""
import os, sys, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
import inference as inf
import profiles

info = profiles.resolve("")
style = json.load(open(info["style"]))
lab = info["labeled"]
gate = "go get going laughing right away again, g g g"
img = inf.render_labeled(gate, style, lab, seed=7)[0]
img.save('outputs/ggate-seed7.png')
print('ggate', img.size)
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
img = inf.render_labeled(smoke, style, lab, seed=7)[0]
img.save('outputs/smoke-seed7.png')
print('smoke', img.size)
