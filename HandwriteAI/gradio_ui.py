"""
HandwriteAI - Gradio desktop UI (5-screen flow).
Screens: 1 Upload -> 2 Style analysis -> 3 Generate -> 4 Output/Download -> 5 Profiles & Settings
Runs offline at localhost:7860. CPU-only.

Each saved handwriting is a named profile (styles/profiles.json); the active
profile drives Generate / fine-tune / cluster-labeling. Profile 1 = the
original user_001 hand (renamed 2026-10-10).

  python gradio_ui.py
"""
from __future__ import annotations
import os, json, shutil, glob
import numpy as np
from PIL import Image

BASE = os.path.dirname(os.path.abspath(__file__))
STYLES = os.path.join(BASE, "styles")
OUTPUTS = os.path.join(BASE, "outputs")
os.makedirs(STYLES, exist_ok=True)
os.makedirs(OUTPUTS, exist_ok=True)

from features import load_sample_images, analyze_pages  # noqa: E402
from inference import load_style, render_text_image, export_outputs  # noqa: E402
import profiles as profmod  # noqa: E402

try:
    from train_fine_tune import finetune_on_user
    HAS_TRAIN = True
except Exception:
    HAS_TRAIN = False


def _active_style_path() -> str:
    try:
        return profmod.resolve("")["style"]
    except KeyError:
        return ""


STATE = {"style_path": _active_style_path(), "features": None}


def _prof_choices():
    return [disp for _pid, disp, _meta in profmod.list_profiles()]


def _prof_active_display():
    try:
        return profmod.resolve("")["display_name"]
    except KeyError:
        return "(none)"


def ui_extract(files):
    if not files:
        return [], "Upload 2-4 pages first.", "{}"
    paths = [f.name if hasattr(f, "name") else f for f in files]
    try:
        images = load_sample_images(paths)
    except Exception as e:
        return [], f"Load failed: {e}", "{}"
    feats = analyze_pages(images)
    STATE["features"] = feats.to_dict()
    previews = [Image.fromarray(im if isinstance(im, np.ndarray) else np.array(im)).convert("RGB")
                for im in images[:4]]
    summary = (f"Slant: {feats.slant_deg:.1f} deg right [{feats.slant_confidence} confidence"
               f"{'' if feats.slant_confidence != 'low' else ' - use the slider on Screen 3'}] | "
               f"Thickness: {feats.thickness_px:.2f}px"
               f"{(' (ratio %.3f)' % (feats.thickness_px / feats.glyph_h_median)) if feats.glyph_h_median > 4 else ''} | "
               f"Baseline sag: {feats.baseline_sag_px:.1f}px | "
               f"Ligatures: {feats.ligature_pct:.1f}% | "
               f"Lines: {feats.n_lines}")
    # persist pending features so Generate works even before fine-tune
    pending = os.path.join(STYLES, "_pending.style")
    with open(pending, "w", encoding="utf-8") as f:
        json.dump({"z": [0.0]*128, "features": feats.to_dict(),
                   "meta": {"pending": True}}, f)
    STATE["style_path"] = pending
    return previews, summary, json.dumps(feats.to_dict(), indent=2)


def ui_finetune(files, epochs):
    if not files:
        return "Upload samples first (Screen 1)."
    if not HAS_TRAIN:
        return "train module unavailable."
    paths = [f.name if hasattr(f, "name") else f for f in files]
    try:
        out = finetune_on_user(paths, _active_style_path(), epochs=int(epochs))
        STATE["style_path"] = out
        return f"Fine-tuned OK -> {out}. Proceed to Generate."
    except Exception as e:
        return f"Fine-tune failed: {e}"


def _has_manifest(d: str) -> bool:
    return bool(d) and os.path.exists(os.path.join(d, "manifest.json"))


def ui_generate(text, slant_adj, strength, lined, fmts, mode, seed):
    if not text or not text.strip():
        return None, "Type some text first.", ""
    if not fmts:
        fmts = ["PNG"]
    style = load_style(STATE.get("style_path", ""))
    style_path = STATE.get("style_path", "")
    stem = os.path.splitext(style_path)[0] if style_path else ""
    labeled_dir = (stem + ".labeled") if stem else ""
    buckets_dir = (stem + ".glyphs") if stem else ""
    pages, used = None, "font"
    # POLICY (user override 2026-10-10): look-first. auto = labeled, else
    # buckets ink, else font.
    if mode in ("labeled", "auto") and _has_manifest(labeled_dir):
        try:
            from inference import render_labeled
            pages = render_labeled(text, style, labeled_dir, lined=lined,
                                   seed=int(seed), style_strength=strength)
            used = "labeled (your letters, your ink)"
        except Exception as e:
            used = f"labeled failed ({e}), falling back; "
    if pages is None and mode in ("glyphs", "auto") and _has_manifest(buckets_dir):
        try:
            from inference import render_with_glyphs
            pages = render_with_glyphs(text, style, buckets_dir, lined=lined,
                                       seed=int(seed), style_strength=strength)
            used += "glyphs/buckets (real ink, letters may be wrong)"
        except Exception as e:
            used += f"buckets failed ({e}); "
    if pages is None:
        if mode == "labeled":
            used += ("font (no enrollment yet: run python enroll.py sheet, "
                     "fill it, then enroll.py build)")
        elif mode == "glyphs":
            used += "font (no bucket library)"
        pages = render_text_image(text, style, slant_adj=slant_adj,
                                  style_strength=strength, lined=lined, seed=int(seed))
        if used == "font":
            used = "font (correct letters, font skeleton)"
    # low-res preview return; full-res saved on Download
    preview = pages[0].copy()
    preview.thumbnail((900, 900))
    STATE["_last_pages"] = pages
    STATE["_last_fmt"] = list(fmts)
    fmt_show = "+".join(fmts)
    return (preview,
            f"Preview ready ({len(pages)} page(s) {pages[0].size[0]}x{pages[0].size[1]}, "
            f"page 1 shown, mode={used}, "
            f"profile={_prof_active_display()}). Hit Download for full 300-DPI {fmt_show}.",
            "")


def _safe_stem(name: str) -> str:
    import re as _re
    return _re.sub(r"[^\w\-]+", "_", name.strip()).strip("_") or "Handwriting"


def ui_download():
    pages = STATE.get("_last_pages")
    if not pages:
        return [], "Generate first (Screen 3)."
    fmts = STATE.get("_last_fmt", ["PNG"])
    try:
        info = profmod.resolve("")
        stem = _safe_stem(info["display_name"])
    except KeyError:
        stem = "Handwriting"
    paths = export_outputs(pages, OUTPUTS, stem=stem, formats=fmts)
    files = [p for ps in paths.values() for p in ps]
    return files, f"Saved: {'; '.join(files)}"


def ui_export_profile():
    """Full-profile bundle zip: style + labeled + glyphs + clusters."""
    import zipfile
    try:
        info = profmod.resolve("")
    except KeyError:
        return None, "No profile yet - extract + fine-tune first."
    zpath = os.path.join(OUTPUTS, info["id"] + "-bundle.zip")
    n = 0
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(info["style"], os.path.basename(info["style"]))
        n += 1
        for sub in ("labeled", "glyphs", "clusters"):
            if not os.path.isdir(info[sub]):
                continue
            for root, _dirs, files in os.walk(info[sub]):
                for f in files:
                    fp = os.path.join(root, f)
                    z.write(fp, os.path.relpath(fp, STYLES))
                    n += 1
    return zpath, f"Exported {zpath} ({n} files, full profile bundle)"


def ui_import_profile(f):
    """Bundle .zip (full family) or legacy .style file (style only)."""
    if not f:
        return "Choose a profile bundle (.zip) or a .style file."
    src = f.name if hasattr(f, "name") else f
    try:
        if src.lower().endswith(".zip"):
            import zipfile
            with zipfile.ZipFile(src) as z:
                z.extractall(STYLES)
            # self-heal registers the extracted <id>.style
            data = profmod._load()
            profmod._heal(data)
            profmod._save(data)
            # activate the newest extracted profile
            stems = set()
            for name in os.listdir(STYLES):
                if name.endswith(".style") and not name.startswith("_"):
                    stems.add(os.path.splitext(name)[0])
            newest = sorted(stems)[-1] if stems else ""
            if newest:
                profmod.set_active(newest)
            STATE["style_path"] = _active_style_path()
            return (f"Imported bundle -> {newest} "
                    f"({len(stems)} profile(s) on disk). Ready to generate.")
        dst = os.path.join(STYLES, os.path.basename(src))
        shutil.copy(src, dst)
        data = profmod._load()
        profmod._heal(data)
        profmod._save(data)
        STATE["style_path"] = dst
        return f"Imported {dst} - ready to generate (labeled library not bundled; label in Tab 6)."
    except Exception as e:
        return f"Import failed: {e}"


def ui_delete():
    """Delete the ACTIVE profile's family + registry entry."""
    try:
        info = profmod.resolve("")
    except KeyError:
        return "No profile to delete."
    removed = []
    for p in (info["style"],):
        if os.path.exists(p):
            os.remove(p)
            removed.append(p)
    for sub in ("labeled", "glyphs", "clusters"):
        if os.path.isdir(info[sub]):
            shutil.rmtree(info[sub], ignore_errors=True)
            removed.append(info[sub])
    data = profmod._load()
    data["profiles"].pop(info["id"], None)
    if data.get("active") == info["id"]:
        data["active"] = sorted(data["profiles"])[0] if data["profiles"] else ""
    profmod._save(data)
    STATE["style_path"] = _active_style_path()
    return (f"Deleted profile {info['display_name']} ({len(removed)} items). "
            f"Active is now: {_prof_active_display()}.")


def ui_prof_select(name):
    import gradio as gr
    try:
        info = profmod.set_active(name)
        STATE["style_path"] = info["style"]
        status = (f"Active: {info['display_name']} ({info['id']}). "
                  f"Style {'found' if os.path.exists(info['style']) else 'MISSING'}, "
                  f"library {'enrolled' if _has_manifest(info['labeled']) else 'not enrolled yet'}.")
        return gr.update(choices=_prof_choices(), value=info["display_name"]), status
    except KeyError as e:
        return gr.update(choices=_prof_choices(), value=_prof_active_display()), f"Select failed: {e}"


def ui_prof_create(name, copy_from):
    import gradio as gr
    try:
        src = "" if copy_from in ("(fresh - no copy)", "") else copy_from
        info = profmod.create_profile(name or "", src)
        profmod.set_active(info["id"])
        STATE["style_path"] = info["style"]
        status = (f"Created {info['display_name']} ({info['id']})"
                  + (f" as a copy of {src}." if src else
                     " fresh - enroll in Tabs 1+6 to fill its library."))
        return gr.update(choices=_prof_choices(), value=info["display_name"]), status
    except Exception as e:
        return gr.update(choices=_prof_choices(), value=_prof_active_display()), f"Create failed: {e}"


def ui_prof_rename(new_name):
    import gradio as gr
    try:
        info = profmod.rename_profile("", new_name)
        return (gr.update(choices=_prof_choices(), value=info["display_name"]),
                f"Renamed -> {info['display_name']}.")
    except Exception as e:
        return gr.update(choices=_prof_choices(), value=_prof_active_display()), f"Rename failed: {e}"


def _label_state():
    st = STATE.setdefault("label", {})
    style_path = STATE.get("style_path", "") or _active_style_path()
    stem = os.path.splitext(style_path)[0] if style_path else ""
    st["cluster_dir"] = stem + ".clusters"
    st["labeled_dir"] = stem + ".labeled"
    return st


def _label_order(payload):
    """Labeling queue: biggest clusters first (coverage per minute).
    Falls back to id order when sizes are missing (legacy payloads)."""
    sizes = payload.get("sizes", {}) or {}
    order = list(payload["clusters"].keys())
    if sizes:
        order.sort(key=lambda c: (-sizes.get(str(c), 0), int(c)))
    else:
        order.sort(key=int)
    return order


def _load_clusters():
    import json as _json
    st = _label_state()
    p = os.path.join(st["cluster_dir"], "clusters.json")
    if not os.path.exists(p):
        return None, st
    payload = _json.load(open(p))
    st["payload"] = payload
    st["order"] = _label_order(payload)
    if "idx" not in st:
        st["idx"] = 0
    return payload, st


def ui_label_build():
    try:
        import sys as _sys
        _sys.path.insert(0, BASE)
        from cluster import build as _build
        st = _label_state()
        lib = os.path.splitext(STATE.get("style_path", "") or _active_style_path())[0] + ".glyphs"
        payload = _build(lib, 64, st["cluster_dir"])
        st["payload"] = payload
        st["order"] = _label_order(payload)
        st["idx"] = 0
        return f"Built {payload['k']} clusters. Start labeling below.", *_label_show()
    except Exception as e:
        return f"Cluster build failed: {e}", None, "", ""


def _label_show():
    payload, st = _load_clusters()
    if payload is None:
        return None, "", "Press Build clusters first."
    order = st["order"]
    st["idx"] = max(0, min(st.get("idx", 0), len(order) - 1))
    cid = order[st["idx"]]
    sheet = os.path.join(st["cluster_dir"], f"cluster_{int(cid):03d}.png")
    guess = payload.get("guesses", {}).get(str(cid), {})
    done = len(payload.get("labels", {}))
    # suspect-sheet flag: wide and/or wildly varying members usually mean
    # joined pairs or junk — a hint, never a verdict. Absent on legacy
    # payloads built before shape stats existed.
    flag = ""
    shp = (payload.get("shape", {}) or {}).get(str(cid), {})
    if shp and (shp.get("med_aspect", 0) > 1.2 or shp.get("w_cv", 0) > 0.45):
        flag = (f" | SUSPECT (aspect {shp.get('med_aspect')}, "
                f"width-cv {shp.get('w_cv')}) — probably joined, consider Skip")
    status = (f"Cluster {st['idx'] + 1}/{len(order)} (id {cid}, "
              f"{payload['sizes'].get(str(cid), '?')} samples) | "
              f"labeled {done}/{len(order)} | "
              f"guess: '{guess.get('guess', '?')}' ({guess.get('score', '?')})"
              f"{flag}")
    return sheet, "", status


def _label_save(letter, advance=True):
    import json as _json
    payload, st = _load_clusters()
    if payload is None:
        return None, "", "Press Build clusters first."
    order = st["order"]
    cid = order[st["idx"]]
    letter = (letter or "").strip()
    if letter:
        if len(letter) != 1:
            _, _, status = _label_show()
            return _label_show()[0], "", status + " | type ONE character (or Skip)"
        payload["labels"][str(cid)] = letter
        _json.dump(payload, open(os.path.join(st["cluster_dir"], "clusters.json"), "w"))
    if advance:
        st["idx"] = min(st["idx"] + 1, len(order) - 1)
    return _label_show()


def ui_label_save_next(letter):
    sheet, _, status = _label_save(letter, True)
    return sheet, "", status


def ui_label_skip():
    payload, st = _load_clusters()
    if payload is None:
        return None, "", "Press Build clusters first."
    st["idx"] = min(st["idx"] + 1, len(st["order"]) - 1)
    return _label_show()


def ui_label_back():
    payload, st = _load_clusters()
    if payload is None:
        return None, "", "Press Build clusters first."
    st["idx"] = max(st["idx"] - 1, 0)
    return _label_show()


def ui_label_confirm_guess():
    payload, st = _load_clusters()
    if payload is None:
        return None, "", "Press Build clusters first."
    order = st["order"]
    cid = order[st["idx"]]
    g = payload.get("guesses", {}).get(str(cid), {}).get("guess", "")
    return _label_save(g, True)


def ui_label_finish():
    try:
        import sys as _sys
        _sys.path.insert(0, BASE)
        from cluster import apply_labels
        st = _label_state()
        payload, _ = _load_clusters()
        if payload is None:
            return "Press Build clusters first."
        labels = payload.get("labels", {})
        if not labels:
            return "No labels yet - label at least a few clusters above."
        man = apply_labels(st["cluster_dir"], labels, st["labeled_dir"])
        warn = (" Library missing (font fallback at render): %s" % "".join(man.get("missing", []))
                if man.get("missing") else " Full common-letter coverage.")
        return (f"Built labeled library: {man['n_glyphs']} glyphs, "
                f"{len(man['chars'])} letters -> {st['labeled_dir']}. "
                f"Generate tab now uses it on auto." + warn)
    except Exception as e:
        return f"Finish failed: {e}"


def build_app():
    import gradio as gr
    with gr.Blocks(title="HandwriteAI") as app:
        gr.Markdown("# HandwriteAI - Your Handwriting Synthesis Tool")
        gr.Markdown("*For personal note digitization only. Offline - no data leaves this computer.*")

        with gr.Tab("1 - Upload Samples"):
            samples = gr.File(file_types=[".pdf", ".jpg", ".jpeg", ".png"],
                              file_count="multiple", label="2-4 pages of YOUR handwriting")
            gallery = gr.Gallery(label="Preview", columns=2)
            extract_btn = gr.Button("Extract Features")
            analysis = gr.Textbox(label="Auto-detected style")
            feats_json = gr.Code(label="Feature JSON", language="json")
            epochs = gr.Slider(1, 5, value=2, step=1, label="Fine-tune epochs")
            tune_btn = gr.Button("Fine-tune my style (1-2 epochs, CPU)")
            tune_status = gr.Textbox(label="Training status")
            extract_btn.click(ui_extract, [samples], [gallery, analysis, feats_json])
            tune_btn.click(ui_finetune, [samples, epochs], [tune_status])

        with gr.Tab("2 - Style Analysis"):
            gr.Markdown("Run **Extract Features** on Screen 1, then review the readouts here. "
                        "Fine-tune the slant on Screen 3 with the slider (-5..+5 deg).")
            gr.Markdown("- Slant angle (deg right) | Thickness profile (px) | "
                        "Baseline sag (px) | Ligature %")

        with gr.Tab("3 - Generate"):
            text_in = gr.Textbox(lines=6, label="Text to render",
                                 placeholder="Type anything - letters, numbers, punctuation...")
            with gr.Row():
                slant = gr.Slider(-5.0, 5.0, value=0.0, label="Slant adjust (deg)")
                strength = gr.Slider(0.0, 1.0, value=1.0, label="Style strength")
            with gr.Row():
                lined = gr.Checkbox(value=False, label="Lined paper background")
                fmts = gr.CheckboxGroup(["PNG", "PDF", "SVG"], value=["PNG"],
                                        label="Output format(s) - pick any combination")
            with gr.Row():
                mode = gr.Radio(["auto", "labeled", "font", "glyphs"], value="auto",
                                label="Render mode (auto=labeled, else your-ink buckets, else font)")
                seed = gr.Number(value=7, precision=0, label="Seed (change for a fresh take)")
            gen_btn = gr.Button("Generate", variant="primary")
            preview = gr.Image(label="Preview (thumbnail)")
            gen_status = gr.Textbox(label="Status")

        with gr.Tab("4 - Output & Download"):
            dl_btn = gr.Button("Download full-quality file(s)")
            dl_files = gr.File(file_count="multiple", label="Your files")
            dl_status = gr.Textbox(label="Saved paths")
            gen_btn.click(ui_generate, [text_in, slant, strength, lined, fmts, mode, seed],
                          [preview, gen_status, dl_status])
            dl_btn.click(ui_download, None, [dl_files, dl_status])

        with gr.Tab("5 - Profiles & Settings"):
            gr.Markdown("**Disclaimer:** for personal note digitization only. "
                        "Not for reproducing others' coursework, bypassing handwritten "
                        "submission requirements, or any deceptive use. "
                        "All processing is local; network needed only once for IAM weights (~150MB).")
            gr.Markdown("A **profile** = one saved handwriting (style + letter library). "
                        "Profile 1 is your main hand; add more for other people/styles.")
            with gr.Row():
                prof_sel = gr.Dropdown(choices=_prof_choices(), value=_prof_active_display(),
                                       label="Active profile")
                prof_apply = gr.Button("Switch to selected")
            with gr.Row():
                new_name = gr.Textbox(label="New profile name", placeholder="e.g. Profile 2")
                copy_from = gr.Dropdown(choices=["(fresh - no copy)"] + _prof_choices(),
                                        value="(fresh - no copy)", label="Copy from")
                new_btn = gr.Button("Create profile", variant="primary")
            with gr.Row():
                rename_to = gr.Textbox(label="Rename active profile")
                rename_btn = gr.Button("Rename")
            prof_status = gr.Textbox(label="Profile status", value=f"Active: {_prof_active_display()}")
            with gr.Row():
                exp_btn = gr.Button("Export full profile bundle (.zip)")
                imp = gr.File(file_types=[".zip", ".style"], label="Import bundle (.zip) or .style")
            exp_file = gr.File(label="Exported bundle")
            exp_status = gr.Textbox(label="Export status")
            imp_status = gr.Textbox(label="Import status")
            del_btn = gr.Button("Delete ACTIVE profile from this device")
            del_status = gr.Textbox(label="Delete status")
            gr.Markdown("Version 0.1 - offline only - CPU inference ~2-3s / 100 chars")
            prof_apply.click(ui_prof_select, [prof_sel], [prof_sel, prof_status])
            new_btn.click(ui_prof_create, [new_name, copy_from], [prof_sel, prof_status])
            rename_btn.click(ui_prof_rename, [rename_to], [prof_sel, prof_status])
            exp_btn.click(ui_export_profile, None, [exp_file, exp_status])
            imp.change(ui_import_profile, [imp], [imp_status])
            del_btn.click(ui_delete, None, [del_status])

        with gr.Tab("6 - Label letters (no paper needed)"):
            gr.Markdown("Teach the system YOUR letters from ink you already uploaded. "
                        "Each cluster = one pile of same-looking crops. Type the letter "
                        "it shows (or Confirm the guess, or Skip junk). Same letter on "
                        "many clusters just merges into more variants - good. "
                        "Finish builds the labeled library; Generate tab uses it on auto. "
                        "Labeling applies to the ACTIVE profile.")
            with gr.Row():
                build_btn = gr.Button("Build clusters from my uploads")
                build_status = gr.Textbox(label="Build status")
            lab_sheet = gr.Image(label="Cluster samples (all should be the SAME letter)")
            with gr.Row():
                lab_letter = gr.Textbox(label="This cluster is the letter… (one character)",
                                        max_lines=1)
                lab_confirm = gr.Button("Confirm guess")
            with gr.Row():
                lab_save = gr.Button("Save & Next", variant="primary")
                lab_skip = gr.Button("Skip cluster")
                lab_back = gr.Button("Back")
            lab_status = gr.Textbox(label="Progress")
            with gr.Row():
                lab_finish = gr.Button("Finish: build labeled library")
                lab_done = gr.Textbox(label="Library status")
            build_btn.click(ui_label_build, None, [build_status, lab_sheet, lab_letter, lab_status])
            lab_save.click(ui_label_save_next, [lab_letter], [lab_sheet, lab_letter, lab_status])
            lab_skip.click(ui_label_skip, None, [lab_sheet, lab_letter, lab_status])
            lab_back.click(ui_label_back, None, [lab_sheet, lab_letter, lab_status])
            lab_confirm.click(ui_label_confirm_guess, None, [lab_sheet, lab_letter, lab_status])
            lab_finish.click(ui_label_finish, None, [lab_done])
    return app


if __name__ == "__main__":
    build_app().launch(server_name="127.0.0.1", server_port=7860)
