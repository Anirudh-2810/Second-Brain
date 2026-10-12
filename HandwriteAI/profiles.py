"""HandwriteAI - PROFILES: named handwriting styles, each a family of files.

A profile on disk is four siblings under styles/ sharing one stem:
  styles/<id>.style       encoder latent + features (the .style JSON)
  styles/<id>.labeled/    render library: manifest.json + glyph PNGs
  styles/<id>.glyphs/     source harvest (pages/crops; used to re-cluster)
  styles/<id>.clusters/   cluster-labeling state

Only <id>.style and <id>.labeled/ are required to render; glyphs/clusters
are enrollment-side. The shared fine-tuned encoder (styles/encoder_finetuned.pth)
is NOT per-profile.

Registry: styles/profiles.json
  {"version": 0.1, "active": "profile_001",
   "profiles": {"profile_001": {"display_name": "Profile 1", "created": "...", "note": "..."}}}

Lookup accepts a profile id ("profile_001"), a display name ("Profile 1"),
or a bare number ("001" / "1"). Missing registry self-heals by registering
any unregistered styles/*.style found on disk (legacy migration).
"""
from __future__ import annotations
import os, json, datetime, glob, re

STYLES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "styles")
REGISTRY = os.path.join(STYLES_DIR, "profiles.json")
_VERSION = 0.1


def _load() -> dict:
    if os.path.exists(REGISTRY):
        try:
            with open(REGISTRY, encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, dict) and "profiles" in data:
                return data
        except Exception:
            pass
    data = {"version": _VERSION, "active": "", "profiles": {}}
    _heal(data)
    return data


def _heal(data: dict) -> None:
    """Register any styles/*.style not yet in the registry (self-heal /
    first-run after a rename). Sets active when unset."""
    changed = False
    for p in sorted(glob.glob(os.path.join(STYLES_DIR, "*.style"))):
        stem = os.path.splitext(os.path.basename(p))[0]
        if stem.startswith("_"):
            continue  # temp files like _pending.style
        if stem not in data["profiles"]:
            n = len(data["profiles"]) + 1
            data["profiles"][stem] = {
                "display_name": "Profile %d" % n,
                "created": datetime.date.today().isoformat(),
                "note": "auto-registered from %s" % os.path.basename(p),
            }
            changed = True
    if not data.get("active") and data["profiles"]:
        data["active"] = sorted(data["profiles"])[0]
        changed = True
    if changed:
        _save(data)


def _save(data: dict) -> None:
    os.makedirs(STYLES_DIR, exist_ok=True)
    data["version"] = _VERSION
    with open(REGISTRY, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def list_profiles():
    """[(id, display_name, meta)] sorted by id."""
    data = _load()
    return [(pid, meta.get("display_name", pid), meta)
            for pid, meta in sorted(data["profiles"].items())]


def active_id() -> str:
    data = _load()
    return data.get("active", "")


def resolve(name_or_id: str = "") -> dict:
    """Resolve a profile reference to its paths.

    Accepts id / display name / bare number; empty string -> active profile.
    Returns {id, display_name, style, labeled, glyphs, clusters}.
    Raises KeyError when not found."""
    data = _load()
    if not name_or_id:
        name_or_id = data.get("active", "")
    if not name_or_id:
        raise KeyError("no active profile (run enrollment or set one in Settings)")
    q = str(name_or_id).strip().lower()
    profiles = data["profiles"]
    pid = None
    if q in profiles:
        pid = q
    else:
        for cand, meta in profiles.items():
            if meta.get("display_name", "").strip().lower() == q:
                pid = cand
                break
        if pid is None:
            m = re.fullmatch(r"(?:profile[_\s-]*)?0*(\d+)", q)
            if m:
                guess = "profile_%03d" % int(m.group(1))
                if guess in profiles:
                    pid = guess
    if pid is None:
        raise KeyError("profile %r not found (have: %s)"
                       % (name_or_id, ", ".join(sorted(profiles)) or "none"))
    base = os.path.join(STYLES_DIR, pid)
    return {"id": pid,
            "display_name": profiles[pid].get("display_name", pid),
            "style": base + ".style",
            "labeled": base + ".labeled",
            "glyphs": base + ".glyphs",
            "clusters": base + ".clusters"}


def set_active(name_or_id: str) -> dict:
    info = resolve(name_or_id)
    data = _load()
    data["active"] = info["id"]
    _save(data)
    return info


def create_profile(display_name: str, copy_from: str = "") -> dict:
    """New profile with a fresh (or copied) style + empty-sidecar family.
    copy_from: existing profile id/display to duplicate style+labeled+glyphs+clusters."""
    import shutil
    data = _load()
    n = 1
    while ("profile_%03d" % n) in data["profiles"]:
        n += 1
    pid = "profile_%03d" % n
    base = os.path.join(STYLES_DIR, pid)
    if copy_from:
        src = resolve(copy_from)
        for ext in (".style",):
            if os.path.exists(src["style"]):
                shutil.copy(src["style"], base + ext)
        for sub in ("labeled", "glyphs", "clusters"):
            dst = base + "." + sub
            if os.path.isdir(dst):
                shutil.rmtree(dst, ignore_errors=True)  # stale partial copy
            if os.path.isdir(src[sub]):
                shutil.copytree(src[sub], dst)
    else:
        # minimal fresh style: neutral features, zero latent
        with open(base + ".style", "w", encoding="utf-8") as f:
            json.dump({"version": "0.1", "style_dim": 128, "z": [0.0] * 128,
                       "features": {"slant_deg": 8.0, "thickness_px": 3.0,
                                    "baseline_sag_px": 2.0, "ligature_pct": 25.0,
                                    "n_lines": 0}}, f)
    data["profiles"][pid] = {
        "display_name": display_name.strip() or ("Profile %d" % (len(data["profiles"]) + 1)),
        "created": datetime.date.today().isoformat(),
        "note": "copied from %s" % copy_from if copy_from else "fresh profile",
    }
    _save(data)
    return resolve(pid)


def rename_profile(name_or_id: str, new_display: str) -> dict:
    """Change a profile's display name only (disk stem stays)."""
    info = resolve(name_or_id)
    data = _load()
    data["profiles"][info["id"]]["display_name"] = new_display.strip() or info["id"]
    _save(data)
    return resolve(info["id"])


def default_paths(name_or_id: str = "") -> tuple:
    """(style_path, labeled_dir) for the active (or named) profile.
    Drop-in replacement for hard-coded 'styles/user_001.style' strings."""
    info = resolve(name_or_id)
    return info["style"], info["labeled"]
