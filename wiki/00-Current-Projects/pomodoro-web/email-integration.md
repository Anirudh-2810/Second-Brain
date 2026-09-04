---
course_code: "BUILDS"
course_name: "Roadtrip Pomodoro — Email Integration"
unit: "Email"
tags: [builds, pomodoro, email, resend, digest, supabase]
last_updated: "2026-09-05"
confidence: high
description: "Email a+b implementation: Resend templates, rate limits, idempotency, unsubscribe, pg_cron digest, email_logs audit."
---

## For future agent
How save-to-email works and what to wire in Supabase/Resend/Vercel. Pair with `architecture.md`.

# Email Integration — Save to Email (a+b)

## Provider

Resend `resend@4.0.1` with `RESEND_API_KEY` + `RESEND_FROM` (default `onboarding@resend.dev` until domain verified with SPF/DKIM/DMARC). Templates are React Email inline HTML in `src/lib/email.ts:1` (no extra dep needed, renders server-side).

## a) Auto per Pomodoro

- **Trigger**: `PomodoroTimer.tsx:handleFinish` when `!isBreak` and `userEmail` present → `POST /api/email/session` with `to=userEmail`.
- **Route** `src/app/api/email/session/route.ts:1`: validates `to` case-insensitive equals `user.email` (prevents open relay), `rateLimit 5/min`, calls `sendSessionEmail()` → Resend `emails.send` with `from`, `subject`, `html` (midnight card), `text`, `List-Unsubscribe` header. On success inserts `email_logs {user_id, type:'session', to_email, provider_msg_id}`. Returns `{ok:true, id}`.
- **Idempotency**: client key `session_id` not yet — currently rate limit + `started_at` dedupe on claim; add `Idempotency-Key: userId:startedAt` if Resend duplicates appear.
- **Guest**: no email while guest; after claim, *next* sessions email, past guest sessions not backfilled.

## b) Digest

- **Prefs**: `supabase/migrations/001_init.sql:email_preferences` (`daily_enabled`, `daily_time default 22:00`, `weekly_enabled`, `weekly_dow`, `timezone Asia/Kolkata`). UI `src/app/settings/page.tsx:1` + `POST /api/email/preferences` upsert.
- **Cron**: `pg_cron` + `pg_net` example in migration comment — `30 16 * * *` daily, `30 3 * * 0` weekly — HTTP POST to `functions/v1/send-digest` with `period`. Edge Function not yet deployed; stub `sendDigestEmail()` in `lib/email.ts:1` ready.
- **Content**: aggregates `sessions` per user where `created_at` in period, renders summary + 10-row table, link to `/dashboard`.
- **Audit**: `email_logs` type `daily`/`weekly` with `provider_msg_id`.

## Security / deliverability

- SPF `include:amazonses.com`, DKIM, DMARC `p=quarantine` after domain verify.
- `From` verified, `Reply-To` not user-controlled, plaintext alternative always.
- Queue: synchronous now, add retry (3× exponential) if `resend` 5xx; Vercel `maxDuration` 10s.
- Unsubscribe: `List-Unsubscribe` header + `/api/email/unsubscribe` (HMAC `user_id:exp` TODO) + settings toggle; never email if `Resend.suppressions` bounced.
