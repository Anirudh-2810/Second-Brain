"""One-shot: render pdf1_work text segments with Profile 1 (labeled engine).

Same engine/policy as convert.py --mode auto (labeled lib exists -> render_labeled).
In-process renders (one style load) -> Test_input/pdf1_work/seg_<name>.png
"""
import os, time

BASE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(BASE, "Test_input", "pdf1_work")

import profiles
from inference import load_style, render_labeled

info = profiles.resolve("Profile 1")
print("profile: %s (%s)" % (info["id"], info["display_name"]))
style = load_style(info["style"])
lib_dir = info["labeled"]

SEGS = ["seg_chart", "seg_table_pre", "seg_table_post", "seg_p3", "seg_p4", "seg_p5"]
for name in SEGS:
    with open(os.path.join(WORK, name + ".txt"), encoding="utf-8") as f:
        text = f.read()
    t0 = time.time()
    img = render_labeled(text, style, lib_dir, width=1600, seed=7,
                         target_h=32, page_h=None)[0]  # single strip (composer slices it)
    out = os.path.join(WORK, name + ".png")
    img.save(out, dpi=(300, 300))
    print(f"{name}: {len(text)} chars -> {img.size[0]}x{img.size[1]} "
          f"in {time.time()-t0:.1f}s -> {os.path.basename(out)}")
print("OK render")
