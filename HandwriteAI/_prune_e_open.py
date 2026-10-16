"""One-shot: suppress open (c-like) e variants + render A/B probes.

Rule: e-crops with mid-right closure < 0.10 get q capped at 0.10
(q^4: 0.54^4=0.085 -> 1e-4, ~850x suppression). Files stay, manifest
metrics change only; backup at manifest.json.bak-e-prune (reversible).

Probes rendered BEFORE (backup manifest) and AFTER at target_h=32:
  condimentum commodo consectetur / adipiscing ver fermentum from /
  Pulvinar suspendisse + stacked line
"""
import os, json, shutil
import numpy as np
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(BASE, "styles", "profile_001.labeled")
MAN = os.path.join(LIB, "manifest.json")
BAK = os.path.join(LIB, "manifest.json.bak-e-prune")
PROBES = os.path.join(BASE, "Test_input", "pdf1_work", "probes")
os.makedirs(PROBES, exist_ok=True)

THRESH, QCAP = 0.10, 0.10


def closure(arr):
    h, w = arr.shape[:2]
    ink = arr < 200
    band = ink[int(h * 0.35):int(h * 0.65), int(w * 0.60):int(w * 0.92)]
    return float(band.mean()) if band.size else 0.0


manifest = json.load(open(MAN, encoding="utf-8"))
if not os.path.exists(BAK):
    shutil.copy(MAN, BAK)
    print("backup:", os.path.basename(BAK))
mets = manifest.setdefault("metrics", {})
hit, tot = 0, 0
for fn in manifest["chars"].get("e", []):
    p = os.path.join(LIB, fn)
    if not os.path.exists(p):
        continue
    tot += 1
    arr = np.array(Image.open(p).convert("L"))
    if closure(arr) < THRESH:
        entry = mets.setdefault(fn, {})
        entry["q"] = min(float(entry.get("q", 1.0)), QCAP)
        hit += 1
json.dump(manifest, open(MAN, "w", encoding="utf-8"), indent=2)
qs = np.array([float((mets.get(fn) or {}).get("q", 1.0))
               for fn in manifest["chars"]["e"]])
w = np.array([max(q, 0.02) ** 4 for q in qs])
print(f"capped {hit}/{tot} e-crops; pick-weight now: min-q share "
      f"{(w[qs <= QCAP + 1e-9].sum() / w.sum() * 100):.2f}%")

import profiles
from inference import load_style, render_labeled

PROBE_TEXTS = {
    "p1_fence_e": "condimentum commodo consectetur",
    "p2_r_e": "adipiscing ver fermentum from",
    "p3_stack": "Pulvinar suspendisse\nlittle tittle lull",
}


def render_all(tag):
    info = profiles.resolve("Profile 1")
    style = load_style(info["style"])
    for name, text in PROBE_TEXTS.items():
        img = render_labeled(text, style, info["labeled"], width=1600,
                             seed=7, target_h=32, page_h=None)[0]
        out = os.path.join(PROBES, f"{tag}_{name}.png")
        img.save(out, dpi=(300, 300))
        print(f"  {tag}/{name}: {img.size[0]}x{img.size[1]}")


shutil.copy(MAN, MAN + ".new")
shutil.copy(BAK, MAN)  # restore pre-prune for BEFORE probes
print("BEFORE probes:")
render_all("before")
shutil.copy(MAN + ".new", MAN)  # re-apply pruned manifest
os.remove(MAN + ".new")
print("AFTER probes:")
render_all("after")
print("OK prune+probes (active manifest = pruned)")
