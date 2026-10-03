---
date: 2026-10-04
description: "Part 1 of the Marcus Jones 4-hour editing course dump — Resolve Free install, UI tour, import, cutting, transitions, link/unlink, keyboard shortcuts, keyframe animation. Beginner-friendly with examples and drills."
tags: [video-editing, davinci-resolve, marcus-jones, course, cutting, keyframes, beginners]
last_updated: "2026-10-04"
source: "https://www.youtube.com/watch?v=sNjyOSADDxE (Full Video Editing Course for YouTube, Marcus Jones, ~3h49m)"
confidence: high
relations:
  relates_to: "[[01-Areas/Self-Dev/video-editing-davinci|Video Editing with DaVinci Resolve Free]]"
---

## For future agent
Part 1 of a 4-part distillation of Marcus Jones's free 4-hour YouTube editing masterclass (Resolve 19-era, version-proof per the video itself). Covers 00:00–00:44: install, UI tour, cutting, transitions, save discipline, link/unlink, shortcuts, keyframes. Verbatim transcript lives in `raw-sources/youtube-transcript-full-video-editing-course-marcus-jones.txt` (7,007 captions). Timestamps like (12:32) point into the video. Continues in [[01-Areas/Self-Dev/video-editing-course-part2-visuals|part 2 (visuals)]] · [[01-Areas/Self-Dev/video-editing-course-part3-audio-deliver|part 3 (audio + deliver)]] · [[01-Areas/Self-Dev/video-editing-course-part4-retention-shorts|part 4 (retention + shorts)]].

# Editing Course Dump 1/4 — Foundations, Cutting, Keyframes

> Source course: **Full Video Editing Course for YouTube (4+ Hours), Marcus Jones** — free, no upsell, Discord feedback community linked under the video. His framing: knowledge without reps is useless, like knowing gym technique but never lifting (00:01). Commit to reps.
> Starter companion: [[01-Areas/Self-Dev/video-editing-davinci|Video Editing with DaVinci Resolve Free]] (your Vivobook setup + 5-clip ladder).

## 0. How to use these 4 pages

Each part maps to a course span with timestamps so you can jump between note and video: part 1 = 00:00–00:44 (hands on keys), part 2 = 00:44–01:03 (eyes), part 3 = 01:03–02:40 (ears + export + live edit), part 4 = 02:40–03:49 (strategy + Shorts). Read a part, do its Reps section the same evening on a real clip, then move on. One part per sitting is the intended dose — four sittings finish the course with a edited video to show for each. Guitar/vlog examples are tuned to record-only footage like yours.

## 1. The master pipeline (the whole course on one flowchart)

```
SHOOT (separate tracks: facecam + screen + mic + room)
  → IMPORT + ORGANIZE (media pool, timeline fps match → Change)
  → ROUGH CUT (watch once, delete silences/mistakes, punchy intro)
  → SECOND PASS (overlays, punch-ins, slides timed to words)
  → SOUND (EQ voice → level rides → duck music → SFX on moments)
  → POLISH (text readable? eye directed? one focus per shot?)
  → DELIVER (range → MP4/H.264 → queue → upload)
  → REPACKAGE (best moments → Shorts/Reels, captions on)
```

Editing order matters: story/cuts first, sound second, looks last. Never grade color on an uncut timeline.

## 2. Install Resolve Free (00:02)

- Google **DaVinci Resolve — Blackmagic Design** → **Free Download** → left option → fill form → Register and Download. He demos Resolve 19; versions move yearly but buttons barely move since v15, so future versions follow along fine (00:03).
- Windows: unzip (7-Zip fine) → run installer → leave everything **default** (don't tick extras) → Next → accept → Install → Finish.
- Launch → Continue → Start. Pick **not-quick-start**, open manually → Allow access. Project manager opens: existing projects listed, or one blank **Untitled Project**. **New Project → name it → Create.**
- Go to the **Edit tab** (bottom icons) — that's home base for 90% of this course.

## 3. UI tour in 60 seconds (00:06)

Reset anytime: **Workspace → Reset UI Layout** (do this now so your screen matches his clicks).

| Zone | What it is | Example use |
|---|---|---|
| **Media pool** (left) | Bin for footage, audio, images | Drag folder contents in; hover scrubs preview |
| **Source preview** (mid-left) | Previews pool clips | Double-click clip → play → pick what to use |
| **Program preview** (right) | Shows your actual edit | This is the video; left is just ingredients |
| **Timeline** (bottom) | Where edits live | 90% of your hours go here |
| **Playhead** (red line) | "You are here" marker | Click ruler to jump (e.g. 1:30); drag to scrub |

Zoom timeline: **+ / – buttons**, or hold **Alt/Option + scroll** (fastest). Play: **Spacebar**. Frame-step: **arrow keys** (his are remapped to W/E — same thing). Resize any panel by dragging its edge; toggle panels (media pool, Effects, Inspector, Index) by clicking their icons — hide them for room once media is on the timeline.

## 4. Import without lag (00:07)

Drag files from a folder straight into the media pool, then drag the main clip to the timeline. On the first drop Resolve asks about matching timeline settings — click **Change** so timeline fps/resolution match your footage (prevents black bars and judder later).

Slow PC fix (do this on day one): **Playback → Timeline Playback Resolution → Half or Quarter**. Preview looks blurry, but **render/export restores full quality** (00:08). Pair with Optimized Media per the starter page.

## 5. Cutting — the fundamental skill (00:11)

Everything is removing boring bits. Recipe for a silence:

1. Zoom the audio track tall (drag its edge) — **waveforms show talking vs silence**.
2. Move playhead to where talking stops → toolbar → **Razor** → click (mini-playhead appears) → click where talking resumes → back to **Arrow/Selection** tool.
3. Click the dead middle → right-click → **Delete Selected** → drag the right-hand remainder left till it snaps shut.

Two more cuts you'll use constantly: **opening silence** (delete first 2 frames so talking starts instantly on click) and **mid-sentence stalls** ("I forgot what I was saying" gaps). Faster edge-trim: with the Arrow tool, hover a clip edge till the trim icon appears, **drag inward/outward** — no razor needed for heads and tails (00:15).

**Example (guitar):** trim the 3 s of chair noise before your first strum and the ring-out tail. Viewer hears music in second one.

**Save discipline (00:21):** **File → Save Project**, constantly. His crash story: closed laptop, lost hours. Reopen via the project manager — timeline, cuts, transitions all reload exactly.

## 6. Transitions — smoothing cuts (00:16)

Hover any clip corner: a white handle appears. Drag it inward on both neighbors → crossfade-style **fade in/out** between them. Essential on **audio** cuts — naked audio cuts sound janky.

Effects-library transitions (left → **Effects → Toolbox**):

- **Dip to Color Dissolve** — dips through black/white; fine but plain.
- **Cross Iris** — obvious circle wipe; he demos it only because it's visible, and says never actually use it.
- **Blur Dissolve** — his recommended workhorse: soft, modern, invisible-ish.
- Audio: **Crossfade 0/3 dB** dragged onto the audio cut — blends waveforms seamlessly.

Drag a transition's edge to lengthen/shorten it: long = dreamy/slow, short (4–8 frames) = crisp. Rule: talking-head silence cuts usually want **no video transition** (a fade screams "I cut here") but almost always want the **audio crossfade**.

## 7. Link / unlink — invisible edits (00:23)

Default: video + audio move together (linked). His Minecraft demo: mining tree → silence → "alright, forward". A video cut teleports the player (harsh). Instead:

1. Select both clips → right-click → **Link Clips → uncheck**.
2. Razor **only the audio**, delete the silence, drag audio shut, trim video tail to match.
3. Playback: talking flows continuously, picture never jumps — viewer can't tell audio was touched.

Why record separate tracks (facecam / desktop / mic / friend audio): unlinking lets you fix one layer without touching the others. Re-link after (select all → Link Clips) so later drags stay in sync. Shortcut version: hold **Alt/Option and click** a clip to select just its video or just its audio — same result, no menu (00:29).

## 8. Speed shortcuts (00:25) — learn these on day two

| Key | Does | Why it matters |
|---|---|---|
| `Space` | Play / stop | Hundreds of times per session |
| `Alt + scroll` | Zoom timeline | Faster than +/– buttons |
| `← / →` (or W/E) | One frame step | Land cuts on exact waveform edges |
| `S` | Split at playhead | No razor-tool round-trips |
| `D` / Backspace | Delete selected | No right-click menu |
| Click gap + `D` | Ripple-delete gap, joins footage | Closes holes in one keystroke |
| `Alt + click` | Select video-only / audio-only | Instant unlink behavior |
| `Ctrl+Z` | Undo | You will live here while learning |
| `I` / `O` | Mark in/out range (render) | Covered in part 3 deliver |
| `M` | Marker | Flag spots to return to (used heavily in his live edit) |
| `Alt + drag` | Duplicate clip | Reuse overlays/slides in one gesture |

Basic clicks-first is fine; graduate to shortcuts as they stick — he uses them throughout the later lessons without explaining again.

## 9. Keyframes — ~40% of editing (00:29)

His claim: understand keyframes and you understand nearly half of video editing. Analogy: a flipbook where you draw page 1 and page 100 and **magic fills pages 2–99**. Two keyframes of different values → software animates everything between.

Concrete recipe (moving logo left → right):

1. Click clip → viewer **Transform** box on → position roughly at start (drag, or drag handles to scale).
2. **Inspector → Position → diamond icon** (turns keyframing on) — keyframe 1 set.
3. Move playhead to end → drag logo right — keyframe 2 auto-creates; red interpolation line appears.
4. Play: smooth glide. **Closer keyframes = faster; farther = slower.** Drag keyframes on the graph, or delete (click red diamond) and re-place.

Stacking: same clip can keyframe **position + zoom + rotation** simultaneously (his logo glides right, grows 0.2→0.4, spins). Also pitch/yaw for tilt-warp. Practical drill he demos: **zoom-to-highlight** — footage with a small thumbnail to emphasize: keyframe zoom-out full → zoom-in + X-position shift to center the target → play → it glides onto the detail (00:38).

Three traps and fixes:

- **Drift-out:** zoom in, then later "zoom out" with only one more keyframe → footage slowly deflates the whole time. Fix: add a **hold keyframe** (same values) where the zoom should persist, then the zoom-out keyframe after it (00:41).
- **Wrong zoom center:** zoom lands off-target. Fix: keyframe **position together with zoom**; reset either by **double-clicking the parameter name** (snaps to default).
- **Pan across stills:** hold position → move playhead → shift X — slow Ken-Burns pan for slides/screenshots (00:43).

## 10. Reps before part 2

1. Razor out 3 silences + edge-trim head/tail, close all gaps.
2. Add fade handles on one audio join; add one Blur Dissolve + one audio crossfade.
3. Unlink once: delete an audio-only "um" without moving video.
4. Animate a PNG/text: left → right in 3 s, then again in 1 s (feel the speed difference).
5. Save, close Resolve, reopen from project manager — confirm everything survived.

## 11. First-evening checklist (30 minutes, end to end)

1. New Project → Edit tab → Reset UI Layout (2 min).
2. Drag one phone clip to media pool → drag to timeline → Change settings (3 min).
3. Playback → Half resolution (30 s).
4. Razor out head silence + one mid "um" → ripple shut (10 min).
5. Fade handles on the join, save, Deliver MP4/H.264/Best of a 15-s range (10 min).
6. Watch the export on your phone. If it plays clean, the loop is learned — everything after is decoration.

## 12. Dense extras (supplements marked)

- **Marker workflow (video, 02:26):** he hits `M` mid-edit to flag spots (applause to steal, fix-later cuts). System: first watch = drop markers only (`M` + rename: "sneeze", "good line", "cover image here"), second pass = execute. Markers turn a 40-minute scrub into a todo list.
- **Optimized media (supplement, pairs with 00:08):** Playback resolution fixes *preview* lag; **Generate Optimized Media** (right-click clips in media pool) fixes *scrub/codec* lag on phone H.264/H.265 footage — the actual Vivobook bottleneck. Proxy quarter-res for edit, full-res at Deliver automatically.
- **Trim modes in one line (supplement):** you know ripple (close gap). **Roll** = move the cut point (both sides change, duration same). **Slip** = slide content inside fixed in/out (timing same, moment changes). Ripple fixes structure; roll fixes timing; slip fixes moments. Learn ripple cold, others on demand.
- **Common part-1 mistakes:** cutting video without checking audio underneath (always glance at waveforms); transitions on every cut (fade-everything screams beginner); editing at full timeline zoom (zoom out for structure, in for precision); no save for 30+ min.

## 13. Tasks (graded — do in order)

1. **Tonight (20 min):** run §11 end to end on one phone clip. Done = MP4 on your phone that starts mid-speech with zero head silence.
2. **This week:** cut a 3-minute ramble to 90 seconds using markers-first method + only S/D/Alt-click keys (no toolbar). Done = ≤2 audible cuts, everything crossfaded.
3. **Portfolio:** keyframed 10-s intro bump (logo/text glides in, holds 3 s, eases out) built once, reused as template. Done = `.drp` project + exported bump you can prepend to any video.

Next: [[01-Areas/Self-Dev/video-editing-course-part2-visuals|Part 2 — tracks, overlays, text that stands out, blur/shake, adjustment + compound clips, green screen]].
