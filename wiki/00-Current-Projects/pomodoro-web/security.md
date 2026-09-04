---
course_code: "BUILDS"
course_name: "Roadtrip Pomodoro — Security"
unit: "Security"
tags: [builds, pomodoro, security, rls, headers, owasp]
last_updated: "2026-09-05"
confidence: high
description: "Production securities for Pomodoro web: headers, cookies, RLS, Zod, rate limits, secrets, checklist."
---

## For future agent
Production hardening applied and what remains. Check `architecture.md` for file map.

# Security

## Done in this commit `9494111`

| Layer | Implementation |
|-------|----------------|
| Headers | `next.config.ts:1` `X-Frame-Options DENY`, `X-Content-Type-Options nosniff`, `Referrer-Policy strict-origin-when-cross-origin`, `Permissions-Policy` empty, `HSTS 63072000` |
| Cookies | Supabase SSR sets `__Host-` style via `lib/supabase/server.ts:1` + `middleware.ts:1`, `httpOnly` `Secure` `SameSite=Lax`, refresh via `auth.getUser()` |
| RLS | `supabase/migrations/001_init.sql:1` — `sessions`, `email_preferences`, `email_logs` all `enable RLS` + `auth.uid()=user_id` policies for select/insert/delete/all |
| Validation | `lib/validation.ts:1` Zod on client (rhf) + server (route handlers), `parsePreset` 1–180m, `sessionSchema`, `guestClaimSchema 500 max` |
| Rate limit | `lib/rate-limit.ts:1` in-mem Map (5/h signup, 10/15m login, 60/m sessions, 1/5m claim, 5/m email/session) — swap to Upstash Redis for multi-instance |
| Password | `lib/auth.ts:1` `bcryptjs` 12 rounds (Supabase Auth also hashes, double layer if custom), password regex upper+lower+number 8–128 |
| Secrets | `.gitignore:1` `.env*` with `!.env.example`, `.env.example:1` template, never `NEXT_PUBLIC` for `SUPABASE_SERVICE_ROLE_KEY/RESEND_API_KEY` |
| Email | Enforces `to` == own verified email, `List-Unsubscribe`, no open relay, `email_logs` audit |
| Build | `npx tsc --noEmit` clean, `next build --webpack` 24.4s on win32, warnings only for Edge `process.cwd` in middleware |

## TODO before public

- Migrate `src/middleware.ts` → `src/proxy.ts` (Next 16 deprecation) via `npx @next/codemod middleware-to-proxy`
- Add `Content-Security-Policy` with nonce (strict), `XSS` via React escape already
- Upstash Redis for rate limit, Sentry, `npm audit` + Dependabot, `playwright` e2e (timer→email mock, guest claim), add `CAPTCHA` on signup if abuse
- Verify Resend domain DKIM/SPF/DMARC, set `RESEND_FROM` to verified domain
