---
course_code: "RETRIEVAL-AGENT"
course_name: "Business Brain Retrieval Agent"
unit: "Module 2 — n8n Configuration"
tags: [retrieval-agent, n8n, chat-trigger, ai-agent, http-request-tool, langchain, workflow-automation]
last_updated: "2026-08-24"
confidence: "high"
---

## For future agent
This page documents the n8n side of the retrieval agent: the Chat Trigger, AI Agent node configuration, and the HTTP Request tool that calls the Supabase Edge Function. This is a reusable pattern for any grounded Q&A agent over a private knowledge base.

---

# n8n Setup — Chat Trigger + AI Agent + Search Tool

## Workflow Overview

```
Chat Trigger (Webhook) 
    → AI Agent (Model + Memory + Tool)
    → HTTP Request Tool (search_business_brain)
    → Supabase Edge Function
```

## 1. Chat Trigger Node

| Setting | Value |
|---------|-------|
| **Node Type** | `n8n-nodes-base.chatTrigger` |
| **Webhook URL** | `/webhook/brain-chat` (or your path) |
| **Authentication** | None (or n8n auth if exposed publicly) |
| **Response Mode** | "Reply to Webhook" |

> **Note**: The Chat Trigger receives the user message and passes it to the AI Agent as the initial prompt.

## 2. AI Agent Node

| Setting | Value |
|---------|-------|
| **Node Type** | `@n8n/n8n-nodes-langchain.agent` |
| **Model** | OpenRouter / OpenAI / Gemini (e.g., `openrouter/anthropic/claude-3.5-sonnet`) |
| **Temperature** | `0.2` (low for factual grounding) |
| **Memory** | Simple Memory, **10 turns** (window buffer) |
| **System Prompt** | See [[retrieval-agent#system-prompt-rules-non-negotiable]] |
| **Tools Attached** | 1 × HTTP Request Tool (`search_business_brain`) |

### System Prompt (Full)

```
You answer questions about this business using ONLY the business brain.

## How to answer
1. ALWAYS call search_business_brain first. Never answer from your own knowledge, even if the question seems general.
2. If the first search is thin, search again with different wording.
3. Answer from the returned chunks only.
4. Cite the file path of every note you used, at the end.

## Tool errors are NOT empty results
If the tool returns an error of any kind — DNS failure, timeout, 401, 500 — the brain is UNREACHABLE. That does not mean the answer is missing. Say: "I can't reach the brain right now — that's a system problem, not a missing note." Then stop. Do not answer from your own knowledge.

## Refusing — this matters more than answering
If the search succeeds but the chunks don't contain the answer, say "That's not in the brain yet" and state what you searched for. Do NOT fill gaps from general knowledge. A wrong answer about this business is worse than no answer.

## Never state a performance number
If asked for results, leads, cost per lead, conversion rates or ROI and the brain has no figures, do not produce one under any circumstances.

## Weighting
- confidence: high — may be stated as fact
- confidence: medium — don't overclaim
- confidence: low — say explicitly you're relying on something unproven
- status: draft is unfinished; archived is retired and may be wrong

## Style
Quote the owner's phrasing verbatim for rebuttals and scripts rather than paraphrasing. Be direct and brief.
```

## 3. HTTP Request Tool — `search_business_brain`

| Field | Value |
|-------|-------|
| **Name** | `search_business_brain` |
| **Method** | `POST` |
| **URL** | `https://<your-project-ref>.supabase.co/functions/v1/search_brain` |
| **Authentication** | Generic → Header Auth → `Authorization: Bearer <brain-key>` |
| **Headers** | `Content-Type: application/json` |
| **Body** | JSON keypair: `mode` = `search`, `query` = *(let the AI fill this)* |

### Tool Schema (for the AI)

```json
{
  "name": "search_business_brain",
  "description": "Search the business brain for relevant knowledge chunks. Use this for ANY question about the business.",
  "parameters": {
    "type": "object",
    "properties": {
      "mode": { "type": "string", "enum": ["search"], "description": "Always 'search'" },
      "query": { "type": "string", "description": "Natural language search query. Rephrase if first attempt returns thin results." }
    },
    "required": ["mode", "query"]
  }
}
```

### Example Tool Call (AI-generated)

```json
{
  "mode": "search",
  "query": "What is our pricing model for enterprise clients?"
}
```

## 4. Edge Function Credentials in n8n

1. **Create Credential**: n8n → Credentials → New → "Header Auth"
2. **Name**: `Brain Key`
3. **Header Name**: `Authorization`
4. **Header Value**: `Bearer <your-brain-key>`
4. **Assign** to HTTP Request Tool → Authentication → "Brain Key"

## 5. Testing the Workflow

1. **Activate** the workflow
2. **Open Chat**: Click "Chat" in n8n workflow editor (or hit the webhook URL)
3. **Ask**: "What is our refund policy?"
4. **Verify**:
   - Tool fires → Edge Function returns chunks
   - Agent answers with citations like `wiki/01-Areas/Business/refund-policy.md`
   - If no result: "That's not in the brain yet. I searched for 'refund policy enterprise'."

## Troubleshooting

| Symptom | Check |
|---------|-------|
| Tool returns 401 | Brain key credential valid? Edge Function `Authorization` header matches? |
| Tool returns 500 | Edge Function logs (Supabase Dashboard → Functions → Logs) |
| Tool times out | Edge Function cold start? Increase n8n tool timeout (default 300s) |
| Agent answers without searching | System prompt not attached? Tool not connected to agent? |
| Agent hallucinates | System prompt rules 5 & 6 not enforced? Temperature too high? |

## Related Pages

- [[overview]] — System architecture overview
- [[edge-function]] — Edge Function implementation
- [[retrieval-agent]] — Agent behavior deep-dive
- [[wiki/01-Areas/Business/automations/patterns/webhook-response-pattern|Webhook Response Pattern]] — n8n webhook best practices
- [[wiki/01-Areas/Programming/SAAS_BUILD_NOTES|SaaS Build Notes]] — Supabase Edge Function patterns