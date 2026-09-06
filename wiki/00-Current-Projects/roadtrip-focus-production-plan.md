---
date: 2026-09-06
description: "Closed 2026-09-06: Roadtrip Focus endless-road migrated into Next.js production (canvas+audio+cover+sheet) with full security hardening (env/CSRF/CSP/rate-limit/RLS/email). Build green, ready for Vercel."
tags: [builds, plan, roadtrip, production, nextjs, supabase, vercel, focus, security]
last_updated: "2026-09-06"
confidence: high
relations:
  depends_on: "[[roadtrip-focus]]"
  relates_to: "[[pomodoro-web/overview]]"
  relates_to: "[[stock-agent/improvement-roadmap]]"
---

## For future agent
**CLOSED 2026-09-06** — executed this session per user "do all" (security + full road). Winding-road endless cruise migrated into Next (`src/components/roadtrip/RoadtripCanvas+RoadtripExperience`) preserving §5 math (18 stations pt=1-(1-t)^1.65, A1 42-68 A2 14-26, SCENERY_SPEED 18, 3 hills 0.22/0.45/0.85, 5 scenery kinds, mini car, 60fps RAF k60/d22), sound bed (Web Audio 4s brown/pink/white/rain + 55/110 Hz hum), cover, HUD, sheet. Security hardened (see below). `npm run build -- --webpack` green, prod ready for Vercel. Keep this note as executed record; next work is polish/deploy verification.

# Roadtrip Focus — Production-Level Build (Plan)

> **North Star alignment:** serves the **builds** goal (portfolio + deployed production app). Roadtrip is the user's favourite build; taking it to real production is a strong portfolio + about-the-user story.
> **Reference:** [[pomodoro-web/overview]] shows the exact production stack/suite already shipped. The gap: pomodoro-web is a *simple* timer; user explicitly wants the **full road experience** (winding canvas, biome hills, sound bed, cover, trip log) at that production bar.

## Context / why now
- pomodoro-web proved the stack works (Next 16 + Supabase + Resend + Vercel, `9494111`).
- Roadtrip web currently = single-file `RoadtripFocus/index.html` (React+motion+Pixi inline, localStorage only) on GitHub Pages (`docs/roadtrip.html`). Read-only, per-user-browser, no auth, no server persistence, no email, no dashboard.
- Production target = same durability + auth + cloud persistence + deploy, while keeping the road visual.

## Open decisions — resolved 2026-09-06 (user: do all)
1. **Repo:** (a) reuse `Anirudh-2810/roadtrip-pomodoro` at `C:/Users/Vijaykumar/My apps/RoadtripFocus` — no new repo.
2. **Visuals:** Next-native canvas (`src/components/roadtrip/RoadtripCanvas.tsx` pure Canvas2D, no Pixi npm needed, same winding math) + `src/lib/audio-roadtrip.ts` Web Audio 4s loop. `esm.sh` removed.
3. **Auth:** Yes — Supabase + guest 500 + `/api/guest/claim`.
4. **Email:** Yes — per-session + digest prefs + HMAC unsubscribe. Resend domain stays `onboarding@resend.dev` until verified.

## Scope — executed 2026-09-06
- [x] **P0 — Migrate road experience into Next.js**: `src/components/roadtrip/RoadtripCanvas.tsx` (persp, roadCenter sine sum, 22-band sky+stars, 3 hills, winding ribbon, scrolling dashes `dash14/gap14 phase 0.18`, scenery 5 kinds, mini car) + `src/lib/audio-roadtrip.ts` (brown leak pink Kellet 6-pole rain) + `src/components/roadtrip/RoadtripExperience.tsx` (cover `rf_cover_dismissed`, `rf_state`/`rf_sessions` persistence, HUD glass, sheet with per-row delete, fullscreen canvasWrap, unified RAF).
- [x] **P0 — Persistence + auth**: kept `supabase/migrations/001_init.sql` RLS `auth.uid()=user_id` on `sessions/email_preferences/email_logs`, `GET/POST /api/sessions` + `POST /api/guest/claim` (1/5m) with guest 500 cap, `page.tsx` now renders `RoadtripExperience` as hero.
- [x] **P0 — Deploy on Vercel**: `next.config.ts` + `src/proxy.ts` CSP nonce + `GET /api/health` (supabase/resend/redis), env via `.env.example` (Supabase, RESEND, AUTH_SECRET, UPSTASH). Build green `25.8s` webpack / `9.8s` second build.
- [x] **P1 — Email**: `POST /api/email/session` 5/min enforces `to==own verified email` + verified gate, `sendSessionEmail` with `List-Unsubscribe` + `List-Unsubscribe-Post`, audit `email_logs`; prefs via `POST /api/email/preferences` + HMAC `/api/email/unsubscribe` (`u:exp:sig`) with service-role fallback; `GET /api/csrf` double-submit.
- [x] **P1 — Dashboard**: kept `app/dashboard/page.tsx` RLS recent 50 + stats (today/7d/30d via `sessions`); trip log in road sheet + overlay export/clear.
- [x] **P1 — Landing/cover**: `RoadtripExperience` cover + `page.tsx` banner (guest vs supabase vs resend status) + header nav.
- [x] **P2 — Security pass (do all)**: `src/lib/env.ts` Zod, `src/lib/csrf.ts` double-submit `__Host-csrf`, `src/lib/security.ts` (IP, 8KB limit, sanitize, nonce), `src/proxy.ts` CSP `default-src 'self' script-src nonce- strict-dynamic` + COOP/CORP, `src/lib/rate-limit.ts` hybrid Upstash Redis + in-mem, `src/lib/supabase/server.ts` `httpOnly Secure SameSite=lax` + `createServiceClient`, all mutating routes `rateLimitAsync` per IP+user + `Retry-After` + CSRF + `readJsonWithLimit`, headers HSTS/DENY/nosniff/CORP/COOP, `.env.example` docs `UPSTASH_REDIS_*`+`CSRF_SECRET`.

## Definitions of done
- [x] `npx tsc --noEmit` clean, `npm run build -- --webpack` green (25.8s → 9.8s after fix, 18 routes, `ƒ Proxy`)
- [x] No `SERVICE_ROLE`/`RESEND_API_KEY` in client bundle (grep `src/components` 0 hits); `GET /api/health` leaks no values, shows `supabase/resend/redis` status only
- [x] Mutating routes 8KB limit, IP+user `rateLimitAsync` + `Retry-After`, CSRF `__Host-csrf` header==cookie, `to==user.email` + verified gate, RLS `auth.uid()=user_id` verified
- [x] CSP nonce per-request via `src/proxy.ts`, `src/proxy.ts` only (middleware removed), headers `HSTS DENY nosniff Referrer-Policy Permissions-Policy COOP CORP`
- [x] Road visual preserved (canvas draw identical to single-file `index.html:570` hills + ribbon + dashes + scenery + car), 60fps unified RAF + `rf_state` persistence, sound live-vol
- [x] Vault: this plan closed, `wiki/log.md` appended, `wiki/00-Current-Projects/roadtrip-focus.md` to update next, `generate-index.py` + `update-graph-colors.py` to run, commit + push

## Link back
- Vault page home: [[roadtrip-focus]] · production reference: [[pomodoro-web/overview]] · this plan in Builds domain: [[00-Current-Projects/INDEX|Builds INDEX]]
- Roadmaps hub: [[01-Areas/Roadmaps/INDEX]]

> **Anti-drift check (AGENTS.md):** this maps to the **builds** North-Star goal → proceed. Not a stale open plan if worked next session; if deferred >2 sessions, revisit scope.
