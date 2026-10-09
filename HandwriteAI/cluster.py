"""
HandwriteAI - CLUSTER LABELING: turn the unlabeled shape-bucket harvest into a
labeled letter library with ZERO paper: cluster crops by shape, human labels
each cluster once (~10 min), clusters sharing a letter merge into variant sets.

Why this instead of only enroll.py: the harvest already holds THOUSANDS of the
user's real letterforms with natural variation. Labeling clusters (not single
crops) amortizes one decision over dozens of variants.

Pipeline:
  python cluster.py build --lib styles/user_001.glyphs --k 64
    -> styles/user_001.clusters/{clusters.json, contact sheets}
  (label in Gradio tab 6, or see clusters.json)
  -> styles/user_001.labeled/manifest.json (0.2-labeled format, same as enroll.py)

KMeans is implemented in numpy (no sklearn dependency).
"""
from __future__ import annotations
import os, json, argparse, string
import numpy as np
from PIL import Image

ALPHABET = (list(string.ascii_lowercase) + list(string.ascii_uppercase)
            + list(string.digits) + list(".,!?;:'\"()-+=/&"))


def thumb_features(arr: np.ndarray) -> np.ndarray:
    """16x16 thumbnail + aspect + relative-size + density -> 259-dim vector."""
    img = Image.fromarray(arr).resize((16, 16), Image.LANCZOS)
    t = np.array(img).astype(np.float32) / 255.0
    h, w = arr.shape[:2]
    aspect = w / max(1, h)
    density = float((arr < 200).mean())
    return np.concatenate([t.ravel(), [aspect, density]])


def collect_crops(lib_dir: str):
    """Only single-letter-plausible crops: skip 'wide' (joined pairs)."""
    manifest = json.load(open(os.path.join(lib_dir, "manifest.json")))
    med_w = float(manifest.get("width_mean", 25) or 25)
    items = []
    for bucket, files in manifest.get("files", {}).items():
        if bucket == "wide":
            continue
        for fn in files:
            p = os.path.join(lib_dir, fn)
            if not os.path.exists(p):
                continue
            try:
                arr = np.array(Image.open(p).convert("L"))
            except Exception:
                continue
            gh, gw = arr.shape[:2]
            if gw > 4 * med_w or gh > 3.5 * (manifest.get("height_mean", 25) or 25):
                continue
            if gw < 6 or gh < 10:
                continue
            items.append((fn, bucket, arr))
    return items, manifest


def kmeans(X: np.ndarray, k: int, iters: int = 25, seed: int = 0):
    rng = np.random.default_rng(seed)
    n = len(X)
    k = max(2, min(k, n))
    # kmeans++ init
    centers = [X[int(rng.integers(0, n))]]
    for _ in range(1, k):
        d2 = np.min(((X[:, None, :] - np.array(centers)[None, :, :]) ** 2).sum(-1), axis=1)
        probs = d2 / (d2.sum() + 1e-9)
        cum = np.cumsum(probs)
        centers.append(X[int(np.searchsorted(cum, rng.random()))])
    C = np.array(centers)
    assign = np.zeros(n, dtype=int)
    for _ in range(iters):
        d2 = ((X[:, None, :] - C[None, :, :]) ** 2).sum(-1)
        new = d2.argmin(axis=1)
        if (new == assign).all():
            assign = new
            break
        assign = new
        for j in range(k):
            pts = X[assign == j]
            if len(pts):
                C[j] = pts.mean(axis=0)
    # drop empty clusters, remap
    remap, out, nxt = {}, np.zeros(n, dtype=int), 0
    for j in range(k):
        if (assign == j).any():
            remap[j] = nxt
            nxt += 1
    for j, nj in remap.items():
        out[assign == j] = nj
    return out, nxt


def guess_letters(clusters: dict, thumbs: dict) -> dict:
    """Template-match cluster medoids vs font alphabet -> suggested labels.
    Suggestions only (often wrong on handwriting); human confirms in UI."""
    try:
        import sys
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from inference import _font
        from PIL import ImageDraw
    except Exception:
        return {}
    refs = {}
    for ch in ALPHABET:
        cell = Image.new("L", (48, 48), 255)
        d = ImageDraw.Draw(cell)
        fnt = _font(34)
        try:
            d.text((24, 30), ch, font=fnt, fill=0, anchor="ms")
        except TypeError:
            d.text((8, 4), ch, font=fnt, fill=0)
        a = np.array(cell.resize((16, 16), Image.LANCZOS)).astype(np.float32)
        a = a.ravel()
        refs[ch] = (a - a.mean()) / (a.std() + 1e-6)
    guesses = {}
    for cid, members in clusters.items():
        vecs = []
        for fn in members[:12]:
            t = thumbs.get(fn)
            if t is not None:
                vecs.append(t[:256])
        if not vecs:
            continue
        med = np.median(np.array(vecs), axis=0)
        med = (med - med.mean()) / (med.std() + 1e-6)
        best, bs = "?", -2.0
        for ch, r in refs.items():
            s = float((med * r).mean())
            if s > bs:
                best, bs = ch, s
        guesses[str(cid)] = {"guess": best, "score": round(bs, 3)}
    return guesses


def build(lib_dir: str, k: int = 64, out_dir: str = "") -> dict:
    out_dir = out_dir or (os.path.splitext(lib_dir)[0] + ".clusters")
    os.makedirs(out_dir, exist_ok=True)
    items, _ = collect_crops(lib_dir)
    if len(items) < 30:
        raise RuntimeError(f"only {len(items)} labelable crops in {lib_dir}")
    feats = []
    thumbs = {}
    for fn, bucket, arr in items:
        v = thumb_features(arr)
        feats.append(v)
        thumbs[fn] = v
    X = np.array(feats)
    mu, sd = X.mean(axis=0), X.std(axis=0) + 1e-9
    Xn = (X - mu) / sd
    assign, nk = kmeans(Xn, min(k, max(8, len(items) // 25)))
    clusters = {}
    for idx, (fn, bucket, arr) in enumerate(items):
        clusters.setdefault(str(int(assign[idx])), []).append(fn)
    # contact sheets (12 samples each) for fast human scanning
    for cid, members in clusters.items():
        n = min(12, len(members))
        sheet = Image.new("RGB", (64 * 6, 64 * 2), "white")
        for i, fn in enumerate(members[:n]):
            try:
                im = Image.open(os.path.join(lib_dir, fn)).convert("RGB")
                im.thumbnail((60, 60))
                sheet.paste(im, ((i % 6) * 64 + 2, (i // 6) * 64 + 2))
            except Exception:
                pass
        sheet.save(os.path.join(out_dir, f"cluster_{int(cid):03d}.png"))
    guesses = guess_letters(clusters, thumbs)
    payload = {"lib": lib_dir, "k": nk,
               "sizes": {c: len(m) for c, m in clusters.items()},
               "clusters": clusters, "guesses": guesses, "labels": {}}
    with open(os.path.join(out_dir, "clusters.json"), "w", encoding="utf-8") as f:
        json.dump(payload, f)
    print(f"clusters: {nk} from {len(items)} crops -> {out_dir} "
          f"(label in UI tab 6, or edit clusters.json labels)")
    return payload


def apply_labels(cluster_dir: str, labels: dict, out_dir: str) -> dict:
    """labels: {cluster_id: char}. Merges same-letter clusters into variants."""
    payload = json.load(open(os.path.join(cluster_dir, "clusters.json")))
    payload["labels"] = labels
    with open(os.path.join(cluster_dir, "clusters.json"), "w", encoding="utf-8") as f:
        json.dump(payload, f)
    lib_dir = payload["lib"]
    chars: dict = {}
    for cid, ch in labels.items():
        if not ch or len(ch) != 1:
            continue
        for fn in payload["clusters"].get(str(cid), []):
            src = os.path.join(lib_dir, fn)
            if os.path.exists(src):
                chars.setdefault(ch, []).append((cid, fn))
    os.makedirs(out_dir, exist_ok=True)
    out_chars: dict = {}
    for ch, pairs in chars.items():
        out_chars[ch] = []
        for i, (cid, fn) in enumerate(pairs):
            safe = ch.replace("/", "slash").replace("\\", "back").replace(
                '"', "dquot").replace("'", "squot").replace(":", "colon").replace(
                "?", "qmark").replace("*", "star").replace("|", "pipe")
            dst = f"c{cid}_{safe}_{i:03d}.png"
            data = open(os.path.join(lib_dir, fn), "rb").read()
            open(os.path.join(out_dir, dst), "wb").write(data)
            out_chars[ch].append(dst)
    manifest = {"version": "0.2-labeled", "chars": out_chars,
                "missing": [], "n_pages": 0,
                "n_glyphs": sum(len(v) for v in out_chars.values()),
                "source": f"clusters:{cluster_dir}"}
    with open(os.path.join(out_dir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)
    print(f"labeled library: {manifest['n_glyphs']} glyphs, "
          f"{len(out_chars)} letters -> {out_dir}")
    return manifest


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("--lib", required=True)
    b.add_argument("--k", type=int, default=64)
    b.add_argument("--out", default="")
    args = ap.parse_args()
    if args.cmd == "build":
        build(args.lib, args.k, args.out)


if __name__ == "__main__":
    main()
