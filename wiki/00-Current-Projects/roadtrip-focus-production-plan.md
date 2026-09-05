---
date: 2026-09-06
description: "Open plan (no timing): take Roadtrip Focus to production-level — the full endless-road experience (not the stripped pomodoro-web timer) hardened like pomodoro-web: auth, Supabase/RLS/persist, Vercel, landings. Serves North Star builds goal."
tags: [builds, plan, roadtrip, production, nextjs, supabase, vercel, focus, open-plan]
last_updated: "2026-09-06"
confidence: medium
relations:
  depends_on: "[[roadtrip-focus]]"
  relates_to: "[[pomodoro-web/overview]]"
  relates_to: "[[stock-agent/improvement-roadmap]]"
---

## For future agent
**OPEN PLAN** — created 2026-09-06, to be executed next session. Scope: take **Roadtrip Focus** (the full winding-road endless-cruise web experience) to production-level, matching the hardening pomodoro-web got but WITHOUT stripping the road/canvas. pomodoro-web is the reference for the production stack (Next.js 16 + Supabase + Resend + Vercel) — reuse its patterns and migrations, don't reinvent. Close this plan when its steps complete.

# Roadtrip Focus — Production-Level Build (Plan)

> **North Star alignment:** serves the **builds** goal (portfolio + deployed production app). Roadtrip is the user's favourite build; taking it to real production is a strong portfolio + about-the-user story.
> **Reference:** [[pomodoro-web/overview]] shows the exact production stack/suite already shipped. The gap: pomodoro-web is a *simple* timer; user explicitly wants the **full road experience** (winding canvas, biome hills, sound bed, cover, trip log) at that production bar.

## Context / why now
- pomodoro-web proved the stack works (Next 16 + Supabase + Resend + Vercel, `9494111`).
- Roadtrip web currently = single-file `RoadtripFocus/index.html` (React+motion+Pixi inline, localStorage only) on GitHub Pages (`docs/roadtrip.html`). Read-only, per-user-browser, no auth, no server persistence, no email, no dashboard.
- Production target = same durability + auth + cloud persistence + deploy, while keeping the road visual.

## Open decisions to confirm first (do NOT guess)
1. **New repo vs reuse `roadtrip-pomodoro`?** Roadtrip-Pomodoro already lives at `Anirudh-2810/roadtrip-pomodoro`. Options: (a) evolve that repo's timer toward full road, or (b) new repo `roadtrip-focus-pro`. Recommend (a) reuse — same stack, no new migrations/deploy. Confirm.
2. **Preserve the React single-file visuals?** Can render canvas inline in Next without the `esm.sh` importmap; or keep Pixi via npm. TBD with user.
3. **Auth required?** Mirror pomodoro-web (signup/login + guest-claim) — assume yes, confirm.
4. **Email?** Mirror (per-session + digest) or skip for v1? Confirm scope.

## Scope (order only, no timing estimates)
- [ ] **P0 — Migrate road experience into Next.js** (from single-file `index.html`): winding-road canvas (dist/3-hill parallax/pt-facing math from `[[roadtrip-focus]]` §5), sound bed (Web Audio white/pink/brown/rain + hum), cover, completion popup, trip log. Keep 60fps RAF.
- [ ] **P0 — Persistence + auth**: Supabase `sessions` (RLS `auth.uid()=user_id`) + guest localStorage-claim flow, mirroring `pomodoro-web/lib/guest.ts` + `/api/guest/claim`. Reuse `supabase/migrations/001_init.sql` style.
- [ ] **P0 — Deploy on Vercel**: import repo, env vars (Supabase URL/anon/service, RESEND, AUTH_SECRET, APP_URL), health route.
- [ ] **P1 — Email**: per-completed-trip Resend a+b + daily/weekly digest via pg_cron (reuse pomodoro-web templates/migrations) — only if user says yes.
- [ ] **P1 — Dashboard**: today/7d/30d totals + trip history from `sessions` RLS (mirror pomodoro-web dashboard).
- [ ] **P1 — Landing/cover**: keep the `READY TO ROLL` cover + a marketing hero for the production URL.
- [ ] **P2 — Security pass**: headers, CSRF, rate limiting, Zod (reuse pomodoro-web `lib/rate-limit.ts`, `next.config.ts`).

## Definitions of done (per pomodoro-web bar)
- [ ] Runs `npm run dev` + `npm run build -- --webpack` on win32 clean
- [ ] Supabase tables + RLS applied; guest claim + auth both work
- [ ] Deployed on Vercel; `GET /api/health` OK
- [ ] Road visual + sound preserved at 60fps (manual eyeball — agent cannot see rendered)
- [ ] Vault page + `wiki/log.md` updated; commit + push

## Link back
- Vault page home: [[roadtrip-focus]] · production reference: [[pomodoro-web/overview]] · this plan in Builds domain: [[00-Current-Projects/INDEX|Builds INDEX]]
- Roadmaps hub: [[01-Areas/Roadmaps/INDEX]]

> **Anti-drift check (AGENTS.md):** this maps to the **builds** North-Star goal → proceed. Not a stale open plan if worked next session; if deferred >2 sessions, revisit scope.
