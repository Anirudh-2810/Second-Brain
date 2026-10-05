---
course_code: "PROJECT"
course_name: "Portfolio Projects"
unit: "index"
tags: [project, github, index]
last_updated: "2026-08-23"
---

## For future agent
Hub page for the owner's GitHub portfolio repos ([Anirudh-2810](https://github.com/Anirudh-2810)), cataloged 2026-08-23 from live repo inspection. Start here for anything about the owner's shipped code projects.

# Projects — GitHub Portfolio

| Project | Stack | One-liner | Wiki |
|---|---|---|---|
| **StockOffline** (`inventory-system`) | Python, Tkinter, SQLite, stdlib web tier | Offline-first shop inventory with secured multi-user web option | [[inventory-system]] |
| **AURA** (`Algorithm101`) | React 19, FastAPI, MongoDB, YouTube API v3 | Music-trend intelligence: genre classification + viral prediction | [[algorithm101-aura]] |
| **handsens101** | Python, MediaPipe, OpenCV, pyautogui | Hand-gesture mouse control via webcam | [[handsens101]] · explained: [[handsens101-explained]] |
| **roadtrip-pomodoro** | Python/Tkinter → Next.js 16, Supabase, Vercel | Focus timer themed as an endless night drive; writes sessions into this vault | [[wiki/00-Current-Projects/roadtrip-focus|Roadtrip Focus]] · explained: [[roadtrip-pomodoro-explained]] |

## Skill signals across the three
- **Product thinking** — offline constraint honored, packaging (.exe), marketing collateral (StockOffline)
- **Security maturity** — PBKDF2/JWT/rate-limiting/tenant isolation well beyond typical student code (StockOffline)
- **Async data engineering** — parallel API windows, Motor/MongoDB persistence (AURA)
- **CV pipeline basics** — detection → smoothing → actuation loop (handsens101)
- **Real-time + concurrency** — daemon-thread timer loop with `root.after` thread hand-off, unified 60fps `requestAnimationFrame` clock, spring physics (roadtrip-pomodoro)

## Interview framing

The two **explained** pages carry a 60–90 second script plus likely follow-ups: [[handsens101-explained]] · [[roadtrip-pomodoro-explained]]. Both builds are **AI-assisted** (provenance recorded per owner 2026-09-24 in [[01-Areas/Business/careers/team-onyx-application]]) — say so if asked, then lead with what *you* decided: the constraint, the architecture, and how you verified it.

Cross-links: [[stock-agent/overview|stock-agent]] is the flagship in-progress platform; AURA's scoring patterns feed it ([[momentum-jegadeesh-titman]]).
