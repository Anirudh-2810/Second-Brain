---
description: "Things that have bitten before and will bite again — pitfalls, edge cases, and testing traps"
tags:
  - brain
---

# Gotchas

Things that have bitten before and will bite again.

## Tools & Environment

- **2026-08-23 — Gemini share links are JS-rendered.** `share.gemini.google/<id>` redirects to `gemini.google.com/share/<id>`, but the HTML is an ~820KB empty shell — conversation data loads via client-side RPC. Plain `webfetch`/`Invoke-WebRequest` gets nothing; needs a headless browser (Browserless/Firecrawl) or a manual paste.
- **2026-08-23 — PowerShell flags git's stderr progress as errors.** `git clone` writes progress to stderr, which PowerShell 5.1 surfaces as `NativeCommandError`. Harmless noise — verify success by checking the result (`Test-Path .git`), not by absence of red text.
- **2026-08-23 — opencode directories are plural.** `.opencode/commands/`, `.opencode/agents/`, `.opencode/plugins/` (confirmed against docs). Claude Code conventions are singular (`.claude/commands`) — don't mix them when porting templates.
- **2026-08-23 — obsidian-mind hook scripts are Claude-Code-shaped** (stdin JSON events: SessionStart, PostToolUse…). They don't run under opencode; equivalent logic must be reimplemented as an opencode plugin (`tool.execute.after`, `experimental.session.compacting`).

## Retrieval Agent / Business Brain

- **2026-08-24 — Tool error = "not in brain" confusion.** If the Edge Function is down (DNS, 401, 500, timeout) and the agent *doesn't* have the "tool errors ≠ empty results" rule, it will confidently say "That's not in the brain yet" when the real problem is the database is unreachable. The user cannot distinguish "fact missing" from "system down." Fix: Enforce Rule 5 in system prompt; test by killing Edge Function.
- **2026-08-24 — n8n HTTP Request tool swallows 5xx as "empty" if not configured.** Default n8n tool behavior: non-2xx responses may not throw; check "Throw on Error" in tool settings or handle in agent logic. Without this, a 500 from Edge Function looks like empty results → agent refuses with "not in brain" instead of "system problem."
- **2026-08-24 — OpenAI embedding dimension mismatch.** `text-embedding-3-small` defaults to 1536 dims; must explicitly request `dimensions: 384` in API call. If you create the table with `VECTOR(384)` but embed at 1536, upserts fail silently or with cryptic pgvector errors. Verify: `SELECT vector_dims(embedding) FROM brain_chunks LIMIT 1;` must return 384.
- **2026-08-24 — IVFFLAT index staleness after bulk ingestion.** IVFFLAT is an ANN index — it doesn't auto-update perfectly for new vectors. After ingesting >1000 new chunks, similarity search recall drops. Fix: `DROP INDEX ...; CREATE INDEX ... WITH (lists = <new_sqrt_rows>);` or `REINDEX INDEX brain_chunks_embedding_idx;` (less effective). Monitor `idx_scan` in `pg_stat_user_indexes`.
- **2026-08-24 — Cosine similarity threshold too high = false negatives.** Default `match_threshold: 0.7` in RPC. For technical/financial content with precise terminology, 0.75+ may miss relevant chunks. For general queries, 0.65 may work better. Tune per domain; expose as parameter in Edge Function.
- **2026-08-24 — Heading-aware chunking loses context at boundaries.** A chunk ending mid-sentence or starting mid-paragraph loses flow. Mitigation: overlap chunks by 50-100 chars, or use semantic chunking (by paragraph + heading) instead of fixed-size. Current implementation: heading-aware only — verify chunk boundaries manually for critical docs.
- **2026-08-24 — Confidence/status not enforced at ingestion.** If ingestion script doesn't extract/propagate `confidence` and `status` from frontmatter, all chunks default to `medium`/`published` → agent can't weight answers, can't filter draft/archived. Fix: Ingestion must parse frontmatter `confidence:` and `status:` fields (or infer from tags/path) and write to chunk row.
- **2026-08-24 — n8n Chat Trigger memory persists across sessions unexpectedly.** Simple Memory (10 turns) is per-session, but if webhook URL is hit without session ID, it may create new memory or share memory. Verify: each chat session gets isolated 10-turn window. For production, consider Redis-backed memory or explicit session IDs.
- **2026-08-24 — Edge Function cold start adds 2-5s latency on first request.** Deno Edge Functions spin down after inactivity. First request after idle pays cold start. Mitigation: Keep-warm cron (ping every 5 min) or accept latency. For user-facing chat, this is visible as "thinking..." delay.
- **2026-08-24 — Supabase Service Role Key in Edge Function = full DB access.** The Edge Function uses `SUPABASE_SERVICE_ROLE_KEY` (bypasses RLS). If Edge Function code has a bug (e.g., SQL injection via query param), attacker gets full DB. Mitigation: Validate all inputs, use RPC functions (not raw SQL), rotate keys periodically, monitor function logs for anomalies.
- **2026-08-24 — Brain key in n8n credentials = plaintext if n8n not secured.** n8n stores credentials encrypted at rest, but if n8n instance is compromised (no auth, exposed port), brain key leaks. Mitigation: n8n behind auth (basic auth / OAuth), rotate brain key quarterly, use separate key per environment (dev/staging/prod).
