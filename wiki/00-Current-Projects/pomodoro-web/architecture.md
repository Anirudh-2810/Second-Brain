---
course_code: "BUILDS"
course_name: "Roadtrip Pomodoro — Architecture"
unit: "Architecture"
tags: [builds, pomodoro, architecture, nextjs, supabase, rls, security]
last_updated: "2026-09-05"
confidence: high
description: "Architecture of production Pomodoro web: Next.js App Router SSR, Supabase RLS tables, Resend queue, rate limiting, guest claim flow, headers."
---

## For future agent
Covers file map, request flow, and why each choice was made for the production Pomodoro. Read `overview.md` first for context.

# Architecture

## File map

```
RoadtripFocus/
  src/app/page.tsx            # timer landing (server getUser, PomodoroTimer client)
  src/app/layout.tsx          # header + Geist fonts + footer
  src/app/globals.css         # Tailwind 4 + midnight tokens (#09090B, #10b981)
  src/app/signup/page.tsx     # rhf+zod, guest claim after signup
  src/app/login/page.tsx      # rhf+zod
  src/app/dashboard/page.tsx  # RLS sessions fetch, stats
  src/app/settings/page.tsx   # email_preferences toggle
  src/app/api/auth/{signup,login,logout}/route.ts
  src/app/api/sessions/route.ts          # POST insert + GET list (RLS)
  src/app/api/guest/claim/route.ts       # 1/5m, 500 max, chunk 100
  src/app/api/email/session/route.ts     # 5/min, enforce to=own email
  src/app/api/email/preferences/route.ts # form POST upsert
  src/app/api/health/route.ts
  src/components/timer/PomodoroTimer.tsx # presets, intent, Worker fallback, guest save, POST /api/sessions + /api/email/session
  src/components/ui/{button,input}.tsx
  src/lib/{validation,guest,rate-limit,email,auth}.ts
  src/lib/supabase/{client,server,middleware}.ts
  src/middleware.ts           # updateSession (Next 16 deprecated name, keep until proxy migration)
  supabase/migrations/001_init.sql
  legacy/{index.html,roadtrip.py}
  next.config.ts              # security headers
```

## Flows

- **Guest**: `PomodoroTimer.tsx:handleFinish` → `saveGuestSession()` (localStorage 500) → `guestStats()`. No email. Banner `Sync to save →` links to `/signup`.
- **Claim**: `GET guestSessions()` → `POST /api/guest/claim {sessions}` → server `guestClaimSchema` validates, chunked insert into `sessions` with `user_id=auth.uid()`. Then `clearGuestSessions()`. No backfill of per-session emails (avoids spam), next completions trigger Email a.
- **Authed finish**: `saveGuestSession` + `POST /api/sessions` (RLS) + fire-and-forget `POST /api/email/session {to, duration_sec, preset, intent, completed}` → `lib/email.ts:sendSessionEmail` via Resend + `email_logs` insert. Idempotency via `rateLimit` + client not re-sending same `started_at`.
- **Digest**: `pg_cron` at `30 16 * * *` (22:00 IST = 16:30 UTC) + `30 3 * * 0` → `supabase/functions/send-digest` (TODO stub, template in `lib/email.ts:sendDigestEmail`) reads `email_preferences` where `daily_enabled/weekly_enabled`, aggregates `sessions`, bulk Resend.
