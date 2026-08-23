# Pattern: Two-Way Data Sync

> Keep two systems consistent (CRM ↔ Sheets, store ↔ inventory, form tool ↔ database). One of the highest-value patterns because "our data doesn't match" is a universal, expensive pain.

## Architecture

```
System A ──(change event/poll)──► [Sync Workflow] ──upsert──► System B
System B ──(change event/poll)──► [Mirror Workflow] ──upsert──► System A
```

Two separate workflows (A→B and B→A) beat one bidirectional monster: easier testing, no infinite loops.

## The 7 Rules (checklist before writing any sync)

### 1. Golden record & field map
Table mapping every field: `A.name ← → B.full_name`, types, required, transform (e.g., date format). Write it down first; half of sync bugs are mapping bugs.

### 2. Stable external ID (dedupe key)
Every synced record carries both IDs:
`{ a_id, b_id, last_synced_hash }` in a sync-state sheet.
Never match on name/email alone — they change.

### 3. Idempotent writes
Re-running must be safe. Upsert by external ID, never blind insert. Test: run the same input twice → still exactly one record.

### 4. Change detection
Options in order of cost:
- Webhook from source (best — real-time)
- Updated_at timestamp > last-run watermark (good)
- Full compare via row hash (fallback for dumb sources)
Store watermark in n8n static data or state sheet.

### 5. Loop prevention
A→B write will look like a B-change. Guard:
- Tag records you wrote (`synced_by=n8n`) and skip them inbound
- Or ignore changes where new hash == last_synced_hash
- Or per-system watermarks with small overlap window

### 6. Conflict rule (write it in the client proposal)
Default: **last-write-wins** using updated_at. Special fields (e.g., billing) may be single-master. Clients sign off on this BEFORE build.

### 7. Failure handling
- Retry node (3×, exponential) on API errors
- Dead-letter row in sync-state sheet (`status=failed, reason`) 
- Nightly digest workflow emails the failed list — silent failures destroy trust
- Rate limits: batch + respect 429 `Retry-After`

## Reference Flow (A→B direction)

```
Trigger (webhook or schedule 5 min)
→ Get changed rows since watermark
→ Split batches (50)
→ Loop items:
    → lookup sync-state by a_id
    → IF exists → update B by b_id
      ELSE   → create in B → save {a_id,b_id} pair
    → store new hash + timestamp
→ Update watermark
→ IF any failures → append dead-letter + notify Telegram
```

## Testing Protocol

1. **Fresh pair:** create in A → appears in B ✓
2. **Update:** edit in A → B reflects change, no duplicate ✓
3. **Round-trip:** same record edited in B → A updates, no ping-pong loop ✓
4. **Idempotency:** re-run whole workflow manually ×2 → counts stable ✓
5. **Chaos:** wrong API key mid-run → failed rows logged, digest sent, rerun heals them ✓
6. **Volume:** 500-row backfill completes without rate-limit deaths ✓

## Sellable Variants

| Variant | Client example | Anchor |
|---|---|---|
| Form tool → CRM | Typeform leads into HubSpot | $497 |
| Store ↔ inventory | Shopify stock ↔ supplier sheet | $997 |
| Sheet ↔ Notion wiki | ops data to client portal | $697 |
| Billing ↔ accounting | Stripe invoices ↔ bookkeeping sheet | $797 |

## Common Failures Seen in the Wild

- Timezone mismatch makes everything look "changed" every run → normalize to UTC at ingestion
- Trailing whitespace / case differences breaking dedupe → normalize keys before lookup
- Deleted records never propagate → decide policy: soft-delete flag syncs, hard deletes logged for review
- API pagination ignored → only first 100 rows ever synced ("works in test" syndrome)
