"""One-shot: apply agent labels for Profile 2 (prune + apply_labels).

Reads Test_input/p2_sheets/_p2_labels.json:
  labels {cid: char} -> cluster labels (conservative: unanimous sheets only)
  prune  {cid: [member indices]} -> removed from clusters.json (files stay)
  skip   [cids] -> left unlabeled (font fallback at render)
Writes styles/profile_002.labeled/ via cluster.apply_labels.
"""
import os, json

BASE = os.path.dirname(os.path.abspath(__file__))
CDIR = os.path.join(BASE, "styles", "profile_002.clusters")

import profiles
from cluster import apply_labels

dec = json.load(open(os.path.join(BASE, "Test_input", "p2_sheets",
                                  "_p2_labels.json"), encoding="utf-8"))
labels = dec["labels"]
prune = dec.get("prune", {})
skip = dec.get("skip", [])

payload_path = os.path.join(CDIR, "clusters.json")
payload = json.load(open(payload_path, encoding="utf-8"))
n_pruned = 0
for cid, idxs in prune.items():
    members = payload["clusters"].get(str(cid), [])
    keep = [fn for i, fn in enumerate(members) if i not in set(idxs)]
    n_pruned += len(members) - len(keep)
    payload["clusters"][str(cid)] = keep
json.dump(payload, open(payload_path, "w", encoding="utf-8"))
print(f"pruned {n_pruned} members across {len(prune)} clusters (files kept)")

info = profiles.resolve("Profile 2")
man = apply_labels(CDIR, labels, info["labeled"])
chars = man.get("chars", {})
print(f"labeled: {man.get('n_glyphs')} glyphs / {len(chars)} letters")
for ch in sorted(chars):
    print(f"  {ch!r}: {len(chars[ch])}")
missing = sorted(set("abcdefghijklmnopqrstuvwxyz0123456789.,!?;:'\"()-") - set(chars))
print("fallback (font):", "".join(missing))
print("OK p2 apply")
