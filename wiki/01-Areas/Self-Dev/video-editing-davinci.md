---
date: 2026-10-03
description: "Video editing starter with DaVinci Resolve Free (India-safe, CapCut banned) tuned for an ASUS Vivobook RTX 2050 — Cut to Deliver workflow, phone-audio sync for dead laptop mic, guitar leveling, and 5 showable projects from record-only clips."
tags: [video-editing, davinci-resolve, vlogging, guitar, self-dev, showable, india-safe]
last_updated: "2026-10-03"
source: "user request 2026-10-03 (record-only guitar + vlog, CapCut banned in India)"
confidence: medium
relations:
  relates_to: "[[01-Areas/Self-Dev/INDEX|Self-Dev Domain Index]]"
---

## For future agent
Editing starter for a user who records (guitar + vlog) but never edits. Uses **DaVinci Resolve Free** because CapCut is banned in India. Tuned for ASUS Vivobook K3405VF (i5-13500H, RTX 2050, 16 GB) with dead built-in mic — earphones + phone mic, sync in post. Use for Cut→Deliver basics, audio leveling, and showable clip ladder. Interface paths `medium` — Resolve moves between versions.

# Video Editing with DaVinci Resolve Free (India-safe starter)

Companions: [[01-Areas/Self-Dev/INDEX]] · learning loop: [[01-Areas/Self-Dev/productivity/how-to-self-teach]] · output-over-hours: [[01-Areas/Self-Dev/comparing-the-wrong-number-practice]]

> Why Resolve and not CapCut: CapCut is ByteDance and banned in India. Resolve Free is full-featured, no ban, and your RTX 2050 accelerates it. Start in **Clipchamp** (preinstalled) only if Resolve feels heavy week one — same workflow, migrate after 3 exports.

## 1. One-time setup (15 min, do once)

- Download **DaVinci Resolve Free** (blackmagicdesign.com), new Project → Timeline **1080p30**
- Preferences → Memory: leave ~4 GB for system; enable **Optimized Media** on import (Playback → Generate Optimized Media) — this stops 4K stutter on the Vivobook
- Project Settings → Save stills/cache to D: or second partition if C: is tight
- Media Storage: one folder per shoot `YYYY-MM-DD-guitar/` — raw stays immutable, exports go to `exports/`

## 2. The only workflow (Cut → Deliver)

| Page | Do | Keys |
|---|---|---|
| **Media** | Import clip(s), generate optimized media | — |
| **Cut** | Blade dead start/end, ripple-delete mistakes | `B` blade, `J/K/L` shuttle, `Shift+Delete` ripple |
| **Edit** | One title, max one cross-dissolve | `Ctrl+T` title |
| **Fairlight** | Select dialogue/music clip → Normalize to **-14 LUFS**, add 5-frame fades in/out | Effects → Normalize; `Alt+T` trim |
| **Color** | Auto white-balance + exposure nudge only (skip Look LUTs for now) | — |
| **Deliver** | Preset **YouTube 1080p**, H.264, upload or save to `exports/` | — |

**Audio matters more than video for you.** Laptop mic is dead — record audio on phone/earphones alongside video, then select both → right-click **Auto Align Clips → Based on Waveform**. Then normalize. A leveled guitar take beats a graded one every time.

## 3. Guitar-specific chain (your case)

1. Trim silence before first strum and after ring-out
2. Cut flubbed bars with ripple delete — keep tempo honest, no time-stretch yet
3. Fairlight: normalize -14 LUFS → light EQ cut below 80 Hz (rumble) → 5-frame fades
4. Title: song + date only. No animated anything.
5. Export 1080p30, watch once on phone speaker — if it sounds fine there, it ships

## 4. Showable projects (in order — each is postable)

| # | Clip | Forces | Show as |
|---|---|---|---|
| 1 | **60-s guitar take, trimmed + leveled** | import, blade, normalize, export | unlisted YouTube link |
| 2 | **Before/after audio** (raw vs leveled, 15 s each) | Fairlight normalize + fades | split video proving ear difference |
| 3 | **Practice loop** (one bar ×4, clean cuts on beat) | ripple rhythm cutting | loopable short |
| 4 | **Two-angle cover** (phone + webcam synced via waveform) | multicam sync, angle switching | 60-s cover |
| 5 | **Day vlog cut** (≤90 s, 5 shots, 1 title) | story selection, pacing | portfolio vlog |

**Done per project:** exported mp4 + 1-line note (what was cut/leveled). No effects reel.

## 5. Rules till MSE

- 20 min alt-days max — exams outrank editing (North Star: FE RAI first)
- One tool only (Resolve). No Premiere/Filmora parallel.
- No LUT packs, no plugin shopping — cuts + level audio ship more than looks

## Next

- After 5 projects: Color quick-grade + keyframed audio dips under voice
- Cross-skill: fitted hardware + edited demo clip together make one portfolio post (Fusion part + this page's export)
