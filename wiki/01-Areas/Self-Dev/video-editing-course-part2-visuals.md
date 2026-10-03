---
date: 2026-10-04
description: "Part 2 of the Marcus Jones editing course dump — tracks, transparent overlays, text that stands out, background blur and darken, camera shake, adjustment clips, compound clips, green screen keying in Fusion."
tags: [video-editing, davinci-resolve, marcus-jones, course, overlays, text, effects, green-screen]
last_updated: "2026-10-04"
source: "https://www.youtube.com/watch?v=sNjyOSADDxE (Full Video Editing Course for YouTube, Marcus Jones, ~3h49m)"
confidence: high
relations:
  relates_to: "[[01-Areas/Self-Dev/video-editing-davinci|Video Editing with DaVinci Resolve Free]]"
---

## For future agent
Part 2 of 4, covering 00:44–01:03 of the course: tracks as layers, overlays, legibility effects, background suppression, shake, adjustment layers, compound clips, chroma key. Assumes [[01-Areas/Self-Dev/video-editing-course-part1-foundations-cutting|part 1 (cutting + keyframes)]]. Continues in [[01-Areas/Self-Dev/video-editing-course-part3-audio-deliver|part 3]] · [[01-Areas/Self-Dev/video-editing-course-part4-retention-shorts|part 4]]. Transcript: `raw-sources/youtube-transcript-full-video-editing-course-marcus-jones.txt`.

# Editing Course Dump 2/4 — Layers, Text, Effects, Green Screen

> One-line thesis of this part (00:54): **editing is directing the viewer's eye** — every overlay exists so the eye lands on the right thing at the right second.

## 1. Tracks are stacked Lego (00:44)

Right-click timeline → **Add Track**. Higher track = on top, always: drag a clip above and it covers what's below; drag it down and it sinks behind. New **Text+** (Effects → Titles) auto-creates its own fresh track (V3).

**Example:** gameplay on V1, facecam picture-in-picture on V2, arrow PNG on V3, title text on V4. Mute/hide any layer to inspect what's underneath. His rule of thumb: one track per *job* (base / visuals / callouts / titles) so nothing gets lost in a Tetris pile.

## 2. Transparent overlays in 2 minutes (00:45)

Need an arrow/circle pointing at something (his demo: arrow at a health bar)?

1. Google `red arrow transparent` → **Tools → Color → Transparent** (filters to true PNGs) → save.
2. Drag onto an upper track, position over target, rotate slightly.
3. Keyframe it (part 1 skills): drift + rotate across the moment — his arrow slowly sweeps like a clock hand.

Anything can be an overlay — photos, screenshots, memes — and anything overlayed can be keyframed. Overlays that *move* feel alive; static ones feel pasted.

## 3. Making things stand out, ranked (00:47–00:53)

Light-on-light is the classic failure (white text on clouds = invisible). Three fixes, weakest to strongest:

**a) Drop shadow** — Effects → OpenFX → Filters → type `shadow` → drag **Drop Shadow** onto the clip. Inspector → Effects tab: tune **strength, angle, distance**. Subtle separation, keeps the design clean. His default for arrows.

**b) Stroke (outline)** — Text+ → Inspector → Title → **Shading → slot 2 → enable** → color **black**, crank **thickness**. White text + thick black stroke survives any background — the meme-caption look. Ugly at max thickness on dark footage, perfect on bright footage; judge per shot.

**c) Suppress the background** — two moves, often stacked:
- **Darken:** cut the background segment under the title (razor both sides) → Inspector → Video → **Composite → Opacity** down. Text stays full-bright, footage sinks. Perfect for intro cards.
- **Blur:** Effects → Filters → **Gaussian Blur** onto the background segment. Blurry + darker = zero competition; the eye has nowhere to go but your text (00:53).

Soften every overlay's entry/exit: **Cross Dissolve** + manual fade handles (part 1). Harsh pops read as amateur; 6–10 frame fades read as pro.

## 4. Camera shake for loud moments (00:54)

Screaming, bass drop, comedic mic-peak? Effects → Filters → **`Camera Shake`** onto the text/clip. Play, then tune **speed** (faster = funnier), **motion scale** (aggression), **motion blur** (smear while shaking). Use sparingly — one shake per video is a punchline; ten is motion sickness.

Browse don't hoard: Effects → Filters holds dozens of toys. Learn the five in this part deeply; window-shop the rest only when a video *needs* a look.

## 5. Adjustment clips — one effect, many clips (00:56)

Problem: 7 clips all need the same blur. Dragging it 7 times + tuning 7 times is slow. Fix:

1. Effects → **Adjustment Clip** → drag onto a new track **above** everything it should affect → stretch it across the span.
2. Drop Gaussian Blur (or any effect) **onto the adjustment clip**. Everything beneath inherits it; raw clips stay untouched.

Think of it as sunglasses over the timeline: put on, take off, one place to tune. Color grades, letterbox bars, and whole-section blurs all live here.

## 6. Compound clips — many clips, one behavior (00:58)

Inverse problem: 5 separate clips need **one** smooth zoom across all of them (keyframing each = fiddly seam-matching hell). Fix: select all → right-click → **New Compound Clip → Create**. Now it's one clip: one zoom keyframe at the head, one at the tail, perfect glide. Same trick for a single long fade across a montage, or one volume ride over a whole scene (he leans on this again in the live edit at 02:15).

Compound = "treat this pile as one thing." Unpack anytime by decomposing (right-click) if you need the pieces back.

## 7. Green screen in Fusion, no fear (01:00)

Two overlay philosophies: **opacity blends** (rainbow pulse at 30% over gameplay — pretty but washes the subject) vs **keying** (remove exactly one color, keep the subject pixel-perfect). For a Travolta-style meme over gameplay, keying wins:

1. Clip selected → **Fusion page** (bottom icons — new tool, same app).
2. Click the **MediaIn node** → press **Shift+Space** → type `key` → **Delta Keyer → Add**.
3. **Eyedropper**: click-hold-drag **over the green** (never over the face — it'll key out skin). Back on Edit page: background gone.
4. Green halo/fringe on edges? Drag the **Gain** slider till the outline dies without eating the subject (too far = purple ghosting).

Free material: search `<anything> green screen` on YouTube/Google — one site he shows hosts 2,500+ downloadable keys. Position/scale with part-1 transform skills afterward.

## 8. His homework list (00:59, verbatim spirit)

- New tracks; transparent PNGs animated around screen.
- Shadow vs stroke on the same text — compare on dark AND light footage.
- Blur/darken backgrounds under titles; stack both.
- Same effect via base clip vs adjustment layer — feel the speed difference.
- Compound-clip zoom across 4+ cuts; fade a whole montage as one.

## 9. Templates vs hand-built (his honest trade)

At 02:33 he admits the alternative openly: his lower-third name card *could* be multi-layer text with manual keyframes — 20 more minutes — or a **pre-built template** dragged on in seconds. Rule: hand-build twice to learn the mechanics, then template it forever. Templates aren't cheating; they're the asset library (part 4 §4) paying rent. Your first lower-third: build manually once (Text+ + stroke + fade), save as preset, never rebuild.

## 10. Worked examples for your footage

- **Guitar chord label:** song section starts → Text+ "Am – F – C – G" bottom-center → white + black stroke → 8-frame fade in/out. Viewer learns while listening; nothing else on screen competes.
- **Vlog location card:** arriving somewhere new → gaussian-blurred freeze of first frame + darkened to 60% + place name center. Two seconds, then dissolve back to motion.
- **Mistake callout:** flubbed chord → red circle PNG pops with camera-click SFX (part 3 §5), holds 1 s, fades. Self-deprecation + eye direction in one move.

## 11. Reps

1. Same sentence, three treatments: shadow-only, stroke-only, blur+darken — screenshot all three, pick a house style.
2. Animate one arrow across a screen recording with position + rotation keyframes.
3. Key one green-screen meme over gameplay; kill the halo with gain.
4. One adjustment clip carrying blur over a 5-clip span; then the same job via compound zoom — note which felt faster.

## 12. Standard track stack (copy this layout every project)

```
V4  titles / lower-thirds (Text+, faded 8 frames each side)
V3  callouts (arrows, circles, memes, keyed green screens)
V2  B-roll / slides / screenshots (timed to nouns)
V1  base footage (facecam / gameplay / vlog)
A1  voice (EQ preset, rides, normalized)
A2  music (ducked, mood-swapped per section)
A3  SFX (whooshes, clicks, ambience — all faded)
```

New project, same stack, zero decisions. When a layer misbehaves you know exactly which lane to open. This is the asset-library habit (part 4 §4) expressed as timeline hygiene.

## 13. Dense extras (supplements marked)

- **Save Text+ as preset (supplement):** style one lower-third (font, stroke, fade) → right-click in Effects Library → **Save As Preset / Power Bin still**. Every future name card = one drag. This is how JV's asset-library advice (part 4 §4) looks inside Resolve.
- **Safe-area discipline (supplement):** Shorts UI covers edges — keep text inside center 80% (View → Safe Area overlays). Robert's readability rant (part 4 §4) applies double on vertical.
- **Overlay timing rule (video spirit):** overlays land *on the noun* (part 3 §7) and leave *before* the sentence ends — lingering callouts after the topic moved on split attention. Default lifespan: 2–4 s, faded both ends.
- **Common part-2 mistakes:** 5 stacked effects when 1 darkened bg would do; keyframing every overlay (static is fine for labels); green-screen fringe ignored at export size (check at 100%, not 25%); adjustment clip left stretched over unrelated scenes (trim it to the span).

## 14. Tasks (graded)

1. **Tonight (25 min):** style one Text+ lower-third (white, black stroke, fade in/out), save as preset, stamp it on 3 clips. Done = preset reusable tomorrow.
2. **This week:** 30-s screen recording with 3 keyframed callouts (arrow + zoom + blurred secret), one focus at a time. Done = viewer test: a friend names all 3 callouts in order.
3. **Portfolio:** keyed meme over gameplay, halo-free at 100%, with whoosh + fade. Done = exported 10-s clip that looks native, not pasted.

Next: [[01-Areas/Self-Dev/video-editing-course-part3-audio-deliver|Part 3 — voice cleanup EQ, the full audio system, music/SFX, Deliver settings, and the 70-minute live edit with you over his shoulder]].
