"""Phase 1: strip mislabeled crops from Profile 2 manifest + disk.

Removes (verified by visual audit):
  multi-letter : p_001(PQR) f_001(FG) r_028/r_029(rst) Y_001(YZ) 1_001/1_003(10)
  wrong digits : 0_000(=2) 6_000/6_001(curves) 7_000/7_001(=6) 8_000/8_001(=7)
  wrong punct  : ._000 ._001 ,_000 -_000 -_001 =_000 =_001
Keeps the one real comma (_001) and the + signs.
Case-insensitive pairs (p/P, f/F) drop BOTH manifest refs; files deleted once.
"""
import os, json

BASE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(BASE, "styles", "profile_002.labeled")
MPATH = os.path.join(LIB, "manifest.json")

# filenames to purge (exact disk names)
PURGE = [
    "enr_p_001.png", "enr_f_001.png", "enr_r_028.png", "enr_r_029.png",
    "enr_Y_001.png", "enr_1_001.png", "enr_1_003.png",
    "enr_0_000.png", "enr_6_000.png", "enr_6_001.png",
    "enr_7_000.png", "enr_7_001.png", "enr_8_000.png", "enr_8_001.png",
    "enr_._000.png", "enr_._001.png", "enr_,_000.png",
    "enr_-_000.png", "enr_-_001.png", "enr_=_000.png", "enr_=_001.png",
]
# manifest refs that resolve to the same files via case-insensitive FS
PURGE_REFS = PURGE + ["enr_P_001.png", "enr_F_001.png"]

man = json.load(open(MPATH, encoding="utf-8"))
removed = []
for ch, files in man["chars"].items():
    keep = [f for f in files if f not in PURGE_REFS]
    if len(keep) != len(files):
        removed.append((ch, len(files) - len(keep)))
        man["chars"][ch] = keep
for fn in PURGE:
    if fn in man["metrics"]:
        del man["metrics"][fn]
man["n_glyphs"] = sum(len(v) for v in man["chars"].values())
man["missing"] = sorted(c for c, v in man["chars"].items() if not v)

with open(MPATH, "w", encoding="utf-8") as f:
    json.dump(man, f, indent=2)

deleted = 0
for fn in PURGE:
    p = os.path.join(LIB, fn)
    if os.path.exists(p):
        os.remove(p)
        deleted += 1

print("removed refs from pools:", removed)
print("files deleted:", deleted)
print("new n_glyphs:", man["n_glyphs"], "chars:", len(man["chars"]),
      "empty:", man["missing"])
