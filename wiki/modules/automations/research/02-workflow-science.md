# Research 02 — Workflow Science: Anatomy, Taxonomy, Quality Signals

> Everything the repository teaches about what n8n workflows *are* — their JSON anatomy, the classification system, naming conventions, size distributions, and how to judge quality before you import. Derived from `workflow_db.py` analysis logic plus corpus-wide statistics.

## 1. The Workflow JSON Format

Every file in the library is a standard n8n export. The essential structure:

```json
{
  "id": "...",                    // original instance id (often stripped)
  "name": "My workflow 5",        // often meaningless -> repo regenerates titles
  "active": false,                // exported state; most are false
  "nodes": [                      // THE core: array of node objects
    {
      "parameters": { ... },      // node-specific config
      "name": "Webhook",          // human label, unique within workflow
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [250, 300],     // canvas coordinates
      "webhookId": "...",         // only on webhook nodes
      "credentials": { ... }      // sometimes present but non-functional post-export
    }
  ],
  "connections": {                // adjacency map: source node -> outputs -> targets
    "Webhook": {
      "main": [
        [ { "node": "Set Fields", "type": "main", "index": 0 } ]
      ]
    }
  },
  "settings": { },                // execution order, timezone, error workflow ref
  "createdAt": "...", "updatedAt": "..."
}
```

Key facts with money consequences:

- **Credentials do not survive export as usable secrets** — files may reference credential names/ids, but you must reconnect every node after import. This is why "100% import success rate" is possible: structure always imports; secrets never transfer.
- **`connections` is a directed graph** keyed by node name strings. Renaming a node without updating connections breaks the graph — the #1 beginner mistake after import.
- **`position` arrays mean nothing functionally** but everything visually; tidy layouts signal professionally maintained workflows.
- **Multiple outputs per node** (IF true/false branches, Switch cases) appear as multiple arrays under `main`. Reading branch semantics from raw JSON is how you understand complex workflows fast.

## 2. The Classification System

The repo's indexer assigns every workflow exactly two class labels plus counts. Internalize these buckets because they're your search vocabulary.

### 2.1 Trigger taxonomy

| Class | Detection rule | Typical shape | Count tendency |
|---|---|---|---|
| Manual | No auto-trigger found | Utility/data-fix scripts run by hand | Common |
| Webhook | Node type/name contains "webhook", or any non-manual trigger type present | Event-driven APIs: forms, bots, payment callbacks | Very common |
| Scheduled | Type contains "cron" or "schedule" | Digests, syncs, monitors, backups | Very common |
| Complex | >10 nodes AND >3 distinct integrations | Multi-system orchestrations, AI agents | Rarest, highest study value |

Note the subtlety: trigger detection is name-based heuristics, so a Telegram trigger counts toward Webhook (any non-manual trigger defaults there). "Complex" is not a trigger at all — it's an override flag for ambition.

### 2.2 Complexity bands

| Band | Node count | What it means for you |
|---|---|---|
| Low | ≤ 5 nodes | Learn from these first; also your fastest client deliverables |
| Medium | 6–15 nodes | The commercial sweet spot — enough logic to charge real money, still explainable in one screen |
| High | 16+ nodes | Study material for architecture ideas; rarely sell as-is |

Corpus average ≈ 6.8 nodes/workflow ⇒ **medium is the center of gravity**. When clients imagine "automation" they're usually picturing a medium workflow. Price accordingly: a well-built 10-node pipeline is a legitimate $500+ deliverable.

### 2.3 Integration counting rules
Only service nodes count. The utility exclusion list (Set, Code, IF, Switch, Merge, Split, Sticky Note, Wait, Schedule/Cron/Manual triggers, Stop And Error, NoOp, Limit, Aggregate, Summarize, Filter, Sort, Remove Duplicates, Date & Time, file read/write/extract/convert, Execution Data, Execute Workflow/Command, Respond to Webhook) is effectively **the standard toolbox of every n8n build**. Memorizing this list = knowing 80% of n8n's core vocabulary. A workflow's real-world complexity lives in its service nodes; its robustness lives in its utility nodes.

## 3. Naming Conventions — The Hidden Search Engine

Files follow `{number}_{Service}_{Action}_{Qualifiers}.json`, e.g.:

- `0251_HTTP_Webhook_Triggered_Automation.json`
- Patterns visible across the tree: `Telegram_Bot_Create_Update_Automation`, `Scheduled_*`, `*_Triggered_*`, `*_Automation_Webhook`

Because the search index includes filenames, FTS queries hit them directly — including exact-field syntax visible in the API code (`filename:"..."`). Practical grep strategies against a local clone:

```
# find every scheduled telegram digest
rg -l "telegramTrigger" workflows/Telegram --glob "*.json"
rg -c '"type": "n8n-nodes-base.openAi"' -g "*.json"   # count AI usage repo-wide
rg -l "respondToWebhook" workflows/                    # chatbot-style responders
```

Title generation strips the numeric prefix and title-cases the rest, special-casing HTTP/API/Webhook/Automation/etc. Embedded JSON names win when meaningful — so cards show clean titles even when filenames are numeric.

## 4. Corpus Statistics & What They Imply

From README + stats endpoint design:

- **4,343 workflows**, of which the `active` boolean distinguishes exports saved in active vs paused state (the UI exposes an Active-only filter; most community exports are inactive).
- **29,445 total nodes → ~6.8 avg**, implying a long tail of small workflows plus a thin band of 30–50+ node monsters.
- **365 unique integrations** across 188 primary-integration folders (some folders are core-node groupings like `Code`, `Filter`, `Webhook`, `Schedule` rather than third-party brands).
- **16 categories** (15 organized + Uncategorized): AI Agent Development; Business Process Automation; CRM & Sales; Cloud Storage & File Management; Communication & Messaging; Creative Content & Video Automation; Creative Design Automation; Data Processing & Analysis; E-commerce & Retail; Financial & Accounting; Marketing & Advertising Automation; Project Management; Social Media Management; Technical Infrastructure & DevOps; Web Scraping & Data Extraction.
- Category assignments live in `context/search_categories.json` (filename→category), served via `/api/category-mappings` for instant client-side filtering.

## 5. Description Auto-Generation — Reusable Copywriting Logic

When metadata lacks descriptions, the indexer writes one deterministically:

1. Trigger opener: "Webhook-triggered automation that…" / "Scheduled automation that…" / "Complex multi-step automation that…" / "Manual workflow that…"
2. Integration sentence: single ("integrates with X"), pair ("connects X and Y"), or list ("orchestrates X, Y, and Z")
3. Purpose keyword scan on the title: create→"to create new records"; update→"to update existing data"; sync→"to synchronize data"; notification/alert→"for notifications and alerts"; backup→"for data backup operations"; monitor→"for monitoring and reporting"; fallback→"for data processing"
4. Suffix: ". Uses N nodes" (+ "and integrates with M services" if M>3)

This is a miniature template-based NLG system. Steal the pattern for your own portfolio: describe every workflow you ship in exactly this structure — trigger + systems + purpose + scale — and clients instantly parse what they bought.

## 6. Quality Signals — Judging Before Importing

Rank any candidate workflow in 60 seconds:

| Signal | Green | Red |
|---|---|---|
| Node count vs promise | Matches task scale | 40 nodes for a "simple alert" |
| Sticky notes present | Documents intent | None in high-complexity flow |
| Error handling | StopAndError / error branch / retry settings | Bare happy path on paid APIs |
| Credential references | Named cleanly (`gmail-main`) | Missing entirely mid-chain |
| typeVersion values | Recent versions | Ancient versions (import warnings) |
| Hardcoded data | Expressions reference prior nodes | Literal emails/IDs baked into Set nodes |
| Loop safety | SplitInBatches with clear exit | Unbounded loops over large lists |

Also note what the repo itself optimizes for — its own quality bar is *importability*: valid JSON, resolvable node types, coherent connection graph. It does NOT guarantee credentials, sub-workflow dependencies, or external files exist. Always budget 15–45 minutes of re-linking and environment fixing per import; that labor is precisely what clients pay you to remove.

## 7. Versioning & Drift Risks

Node `typeVersion` fields evolve; a workflow built for `typeVersion 1` of the OpenAI node may import with deprecation warnings on current n8n. The library's November 2025 security pass resolved CVEs in the tooling, but individual workflow compatibility tracks n8n releases. Mitigation ritual after any import: check every node for yellow/orange warning banners, update typeVersions where offered, test-run manually before activating schedules or exposing webhooks.

## 8. Meta-Observation — Why This Dataset Matters Strategically

Four thousand real automations are a fossil record of what businesses actually ask for. Frequency analysis of the tree tells you demand: Telegram dominates delivery channels, OpenAI saturates new builds, Sheets/Gmail/Airtable anchor small business stacks, and webhook+scheduled triggers split roughly evenly between reactive and proactive automation. Every product decision you make — which niche to serve, which template pack to publish next, which retainer to pitch — can be grounded in this distribution instead of guesswork. The dataset is MIT-licensed: the fossils are yours to monetize.
