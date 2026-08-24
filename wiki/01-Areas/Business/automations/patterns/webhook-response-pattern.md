# Pattern: Webhook Responder

> The fastest pattern to build, demo, and sell. An external event hits your unique URL; the workflow answers. Powers lead bots, chatbots, payment flows, API glue — and it's the pattern clients "get" instantly when you show a live demo.

## Anatomy

```
External app ──POST──► https://your-n8n/webhook/<private-path>
                          │
                     [Webhook node]
                          │
                 validate → transform → act
                          │
              respond fast (or acknowledge + process async)
```

Two webhook modes you must choose deliberately:
- **Respond Immediately** (`responseMode: onReceived`): replies 200 instantly, workflow continues in background. Use for anything slow (>1–2 s) or where the caller won't wait.
- **Using Respond-to-Webhook node** (`responseMode: responseNode`): YOU craft the final response body/status. Required for chatbots and API endpoints that need real answers.

## Build Checklist (every webhook workflow)

### 1. Private path
Never `/webhook/lead`. Use `/webhook/lc-7f3k9x2a` — unguessable by default. Production vs test URLs differ; activate workflow before sharing prod URL.

### 2. Validate the caller
Minimum one of:
- Header auth: `X-Webhook-Token` equals secret (IF node first thing)
- HMAC signature check when source supports it (Stripe, GitHub): verify signature against raw body with Code node + crypto
- Source IP allowlist via header/origin checks where available

Reject early → `418`/`403`, log the attempt.

### 3. Normalize input immediately
First Set node maps `body.*` into clean fields, applies defaults, trims strings. Downstream nodes never touch raw `$json.body`.

### 4. Idempotency key
Callers retry. Derive a key (their event ID, or hash of timestamp+email+amount), check state store:
```
IF seen(key) → return {"status":"duplicate"} (200)
ELSE mark(key) → continue
```
Prevents double-charges, double-leads, double-messages.

### 5. Fast ack for slow work
If processing takes seconds (AI calls, loops):
1. Webhook (respond immediately) → 2. Queue-ish branch → do work → notify separately.
The sender gets instant 200; nothing times out.

### 6. Structured success/error responses
Success: `{ "ok": true, ...useful }`.
Errors: meaningful status codes — `400` bad payload, `403` bad token, `429` throttled, `500` broke. Attach Error Workflow so failures page you (see templates #3).

### 7. Log every hit
Append minimal row per call (ts, source, key, outcome). This is your debugging lifeline AND client-facing proof of activity ("see, 43 leads processed this week").

## Reference Flow — Lead Bot

```json path=webhook
{ "httpMethod": "POST", "path": "lc-7f3k9x2a", "responseMode": "onReceived" }
```
→ IF header token valid?
   no → Respond 403 (stop)
   yes ↓
→ Set: {name, email, phone, message, source:"leadform", received_at}
→ Google Sheets append (idempotency row)
→ Telegram alert to owner
→ IF message contains urgent keywords → SMS/priority ping

Full importable JSON: `templates/starter-workflows.md` (#1).

## Reference Flow — Chatbot (respond-node style)

Telegram/Webhook message in → load user context (state sheet by chat id) → AI node generates reply → **Respond to Webhook** with text → save context.
Latency budget: keep under ~8 s or move to async + follow-up message.

## Testing Protocol

```powershell
# happy path
curl.exe -X POST "http://localhost:5678/webhook/lc-7f3k9x2a" `
  -H "Content-Type: application/json" -H "X-Webhook-Token: SECRET" `
  -d '{\"name\":\"A\",\"email\":\"a@b.c\",\"message\":\"hi\"}'

# missing token → expect 403
# duplicate send ×2 → expect second returns duplicate
# malformed JSON → expect 400 not 500-crash
```

Then test from the public internet via tunnel (`cloudflared tunnel --url http://localhost:5678`) because firewall behavior differs.

## Security Notes (non-negotiable for client work)

- Secrets in n8n credentials/env, never in URL query params
- Rate-limit guard (simple counter per IP in Redis/sheet) on public endpoints
- Don't echo full payloads back in error responses (leakage)
- Per-client isolated n8n instance for regulated data

## Why Clients Buy This Pattern Fast

You can demo live in 60 seconds on a sales call: open their form → type → their phone buzzes. That moment closes deals better than any slide deck. Anchor: $297–497 per responder, often same-week delivery.
