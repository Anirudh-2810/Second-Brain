---
date: 2026-10-04
description: "Part 3 of the Marcus Jones editing course dump — voice EQ cleanup and presets, the complete audio system, music and sound effects, Deliver export settings, and the full live start-to-finish edit with decision commentary."
tags: [video-editing, davinci-resolve, marcus-jones, course, audio, fairlight, music, export, live-edit]
last_updated: "2026-10-04"
source: "https://www.youtube.com/watch?v=sNjyOSADDxE (Full Video Editing Course for YouTube, Marcus Jones, ~3h49m)"
confidence: high
relations:
  relates_to: "[[01-Areas/Self-Dev/video-editing-davinci|Video Editing with DaVinci Resolve Free]]"
---

## For future agent
Part 3 of 4, covering 01:03–02:40: the entire audio curriculum plus Deliver plus the 70-minute over-the-shoulder live edit. Follows [[01-Areas/Self-Dev/video-editing-course-part2-visuals|part 2]]. Ends with [[01-Areas/Self-Dev/video-editing-course-part4-retention-shorts|part 4 (retention + shorts)]]. Transcript: `raw-sources/youtube-transcript-full-video-editing-course-marcus-jones.txt`.

# Editing Course Dump 3/4 — Audio, Export, Live Edit

> His most repeated claim (01:09): **audio matters more than video** — viewers forgive 720p, nobody forgives harsh/muddy/uneven voice. Budget your learning accordingly.

## 1. Voice cleanup EQ recipe (01:03)

Raw chain first: drop the voice clip on the timeline, drag the white volume line up till clearly audible. Then **Fairlight tab → Mixer on → select the voice track → EQ → double-click** to open the curve:

| Band | Shape | Move | Fixes |
|---|---|---|---|
| **5** | Bell | Sweep to presence (~2–5 kHz), lift slightly | "Crisp/clean" — his before/after test line: *"the quick brown fox…"* |
| **6** | Cut highs | Drag left/down | Harsh sibilance, fizzy top end |
| **1** | Cut lows | Pull down | "Mud" — messy low rumble |

No universal numbers — male/female voices, rooms, and mics differ, so sweep while looping playback and trust ears. Save the winner: **+ → Add Preset → Create New Preset → name it** (his: *"Marcus' voice"*). Next video: dropdown → preset → curve snaps back. One-time work, lifetime dividends.

**Example (you):** phone-recorded guitar voiceover with room hum — band-1 low cut + gentle band-5 lift is 80% of "studio sound" before any plugin.

## 2. The volume system (01:09)

Three levels, smallest to biggest:

- **Clip line:** drag the white line on a clip up/down (dB). Loud = big waveforms; watch it doesn't sound blown out.
- **Keyframe rides:** talking loud then trailing quiet? Hover line → **Alt+click** adds ride points (red dots, same diamonds in Inspector → Audio). Anchor a baseline point, add a second, drag up the quiet tail — volume climbs gradually between them. His daily use-case: excited starts, mumbled endings, one consistent level so viewers never touch their volume knob.
- **Track fader:** Fairlight **Mixer** slider per track moves *every* clip on it. Three dialogue clips all quiet? One fader, not three drags.

Ceiling rule: peaks should sit under **–3 dB**; meters flashing **red** = crackly clipping. Occasional red on a scream is a comedic choice; constant red is ear damage and click-away.

**Normalize shortcut:** select several clips → right-click → **Normalize Audio Levels** → target dB (he uses –6). Waveforms rebalance toward each other — imperfect but instant across a whole timeline.

## 3. Tracks: mono, separated, named (01:16)

Add audio track → choose **Mono** always (stereo lets left/right ears differ — fiddly, pointless for YouTube; mono = identical both ears). Run three lanes minimum: **voice / music / SFX**, because the mixer then rides each family with one fader and you can *find* effects months later.

## 4. Music that serves the story (01:16)

Free source first: **YouTube Studio → Audio Library** — 100% copyright-free, monetizable, preview in browser, Download → drag into the music track. It'll arrive too loud (meters red) — drag the line down till voice sits clearly on top.

Three laws:

1. **Duck it ruthlessly.** Music is wallpaper; if one word gets masked, it's too loud. Keyframe gentle builds (quiet → louder) under montages.
2. **Score the emotion, per section.** Epic moment = epic track; suspense = suspense; silly = silly. One generic bed across 10 minutes flattens everything — swap tracks as the story turns.
3. **Match energy, don't fake it.** Upbeat track under monotone delivery (or vice versa) feels disjointed to viewers even if they can't say why.

## 5. Sound effects, three species (01:19)

- **Foley/exaggeration:** real moments made bigger — smack on a game-character landing, crash synced to impact frame, **whoosh** as arrows/photos slide in, **camera click** as pictures pop. Rule: land exactly on the visual frame.
- **Meme/jingle bits:** standalone comedy (voice lines, jingles) — genre-dependent, use where your audience speaks meme.
- **Ambience beds:** long spooky/cozy room tones under whole scenes.

Placement > library: the *right-frame* free whoosh beats the *perfect* mistimed premium one. Same transitions as video apply — fade handles and **audio crossfades** on every join, plus one-off toys like **Echo (Large Hall preset)** on a sarcastic line for emphasis.

Starter SFX shopping list (10 files cover 90% of YouTube): 3 whooshes (soft/medium/hard), 1 camera click, 1 pop, 1 smack/impact, 1 riser, 1 applause bed, 1 room-tone loop, 1 notification ding. Collect once into the asset library, rotate the whooshes per Ed's law, never download mid-edit again.

## 6. Deliver without fear (01:25)

Edited? **Deliver tab** (bottom rocket icon):

1. Select range: drag the in/out markers (or `I`/`O` keys) around what ships — exclude test junk.
2. Left panel → **Custom Export** → name + **Location** (Desktop is fine).
3. **Format MP4, codec H.264, resolution = timeline, framerate = timeline** (auto-matched when you clicked Change at import). **Quality → Automatic → Best.** Files too fat? Drop to High/Medium — slightly softer, far smaller.
4. Ignore Audio/File tabs → **Add to Render Queue → Start Render** (or Render All for batches). Finished = one MP4 ready to upload.

## 7. Live edit: 70 minutes over his shoulder (01:28–02:40)

He edits a real talk ("green dot theory" — start messy, pivot by revealed opportunity) start to finish. Steal the *method*, not the slides:

- **Rough cut first.** One full watch: delete silences, kill the weak prelude ("she's just talking about me" — cut; open on *"I wanted to share something today"*), drag main beats in order. Goal: know your footage intimately. Result: long talk → 7:40.
- **Punchy intro or death.** If the first 15 s rambles, it goes. No exceptions.
- **Overlays hide cuts.** Every harsh join gets a slide/screenshot laid over the seam — mouth-closed→mid-sentence teleport vanishes under a well-timed visual.
- **Punch in/out on key lines** (zoom 1.0→1.15 + recenter). Keep the punch value **consistent** across the video; align **eyes** between cuts or it feels jarring; fix drift with position keyframes.
- **Time reveals to words.** New dot appears *exactly* when he says "red dot opportunity" — slide transitions land on the noun, never early.
- **Audio-visual sync principle (01:48):** show it the second you say it. Mention a channel? It's on screen. Hard-to-imagine thing? Screenshot it. Described object without visual = confused viewer.
- **White-rectangle cover-ups:** stray slide text ("suck") hidden with a white Solid Color generator sized over the word — invisible on white decks.
- **Alt+drag duplicates** reuse slides/overlays in one gesture.
- **Frankenstein room tone:** applause too short? Copy tail → paste → crossfade the seam → compound-clip the pile → one clean fade. Same move rescues any crowd/guitar-room moment.
- **Ride every mumble:** trailer-off line gets 2–3 volume keyframes till intelligible; sniffs get dipped, not deleted (keeps it human).
- **Kill filler honestly:** redundant clause ("or to succeed as a YouTuber" ×2) → cut + crossfade; keep one deliberate dramatic pause per point (his "to succeed, you first have to BE" beat).
- **Eye-line surgery:** looking at script? Cut to the frame where eyes lift — reads as "talking off the top of my head."
- **80/20 ship rule (02:38):** not the most meticulous edit possible — *engaging enough*, then export. Watch each edit twice; the second watch always finds the cut you swore was clean.

## 8. Reps

1. EQ your voice, save the preset, apply to a second project from the dropdown.
2. Ride one trailing-quiet sentence with 3 Alt+click keyframes.
3. Score a 60-s clip with 2 mood-swapped tracks + 1 whoosh + 1 click, all faded.
4. Deliver MP4/H.264/Best via queue; note file size, re-render Medium, compare.

## 9. Worked examples for your footage

- **Guitar take rescue:** room hum + trailing-quiet final chord → band-1 low cut, band-5 lift, save preset → ride the last chord up with two keyframes → normalize whole track → Deliver Best. This single chain is 90% of "why do his covers sound pro."
- **Vlog street noise:** traffic bed under talking → cut ambience to its own lane → duck to –20 dB under voice via track fader, keyframe swells up in walking-only gaps. Voice never fights the street.
- **Cover intro:** 2 s of song hook *before* any greeting (punchy-intro rule), title card over darkened freeze, music dips as you say "hey I'm Anirudh" — hook + name + smile inside 15 s (part 4 §7 applies here too).

## 10. Reps

1. EQ your voice, save the preset, apply to a second project from the dropdown.
2. Ride one trailing-quiet sentence with 3 Alt+click keyframes.
3. Score a 60-s clip with 2 mood-swapped tracks + 1 whoosh + 1 click, all faded.
4. Deliver MP4/H.264/Best via queue; note file size, re-render Medium, compare.

## 12. Dense extras (supplements marked)

- **YouTube loudness target (supplement):** YouTube normalizes to **–14 LUFS**. Mix voice to peak –3 dB (video §2), then check integrated loudness in Fairlight meters (Loudness panel) — near –14 means no platform re-compression surprises. Quiet uploads get turned *up* (noise floor rises); hot uploads get turned *down* (your punch flattens).
- **De-ess and de-noise order (supplement):** chain order matters — **noise reduction → EQ → de-esser → normalize**. Cutting hiss *after* lifting presence bakes the hiss in. Resolve Fairlight FX in that top-to-bottom order.
- **Room-tone glue (video spirit):** Frankensteined applause works because continuous bed + crossfades hide seams. Same for vlogs: loop 10 s of street/room tone under the whole scene at –30 dB — cuts stop "popping" against digital silence.
- **Common part-3 mistakes:** EQ before fixing levels (garbage in, polished garbage out); music ducked once globally instead of per-section; SFX library auditioned mid-edit (collect the 10-file starter list first); exporting the whole timeline instead of I/O-ranged selection.

## 13. Tasks (graded)

1. **Tonight (25 min):** full voice chain on one guitar voiceover — EQ preset → rides → normalize → –14 LUFS check → export. Done = before/after pair where the after is clearly crisper at phone-speaker volume.
2. **This week:** score a 90-s vlog with mood-swapped music (2 tracks), room-tone bed, 3 exact-frame SFX. Done = a deaf-to-detail friend can't spot a single cut.
3. **Portfolio:** 60-s cover with intro hook (2 s song first), leveled vocal + guitar, faded ends, MP4/Best. Done = upload-ready file + loudness screenshot.

## 11. Mix order (never fight all lanes at once)

1. Voice first: EQ preset → rides → normalize → ceiling check.
2. Music second: duck under voice, swap per mood, fade heads/tails.
3. SFX last: exact frames, one layer, crossfaded.
4. Full pass at low volume on phone speaker — if every word survives there, the mix ships.

Next: [[01-Areas/Self-Dev/video-editing-course-part4-retention-shorts|Part 4 — hooks, frontloading, J/L cuts, asset libraries, directing the eye, roast lessons, Shorts/AI repurposing, and the master tips bank]].
