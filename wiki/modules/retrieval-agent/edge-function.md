---
course_code: "RETRIEVAL-AGENT"
course_name: "Business Brain Retrieval Agent"
unit: "Module 3 — Supabase Edge Function"
tags: [retrieval-agent, supabase, edge-function, deno, pgvector, embedding, semantic-search, api]
last_updated: "2026-08-24"
confidence: "high"
---

## For future agent
This page documents the Supabase Edge Function that powers vector search for the retrieval agent. It handles two modes: `embed` (for ingestion) and `search` (for query-time retrieval). Written in Deno/TypeScript, deployed to Supabase Edge Runtime.

---

# Supabase Edge Function — Vector Search API

## Endpoint

```
POST https://<project-ref>.supabase.co/functions/v1/search_brain
Authorization: Bearer <brain-key>
Content-Type: application/json
```

## Request Modes

### Mode: `embed` (Ingestion)

```json
{
  "mode": "embed",
  "inputs": ["chunk text 1", "chunk text 2", "..."]
}
```

**Response**: Array of 384-dim embedding vectors (one per input)

```json
[
  [0.0123, -0.0456, ...],  // 384 numbers
  [0.0234, -0.0567, ...]
]
```

### Mode: `search` (Query)

```json
{
  "mode": "search",
  "query": "What is our pricing model?"
}
```

**Response**: Top-k matching chunks with metadata

```json
{
  "results": [
    {
      "path": "wiki/modules/business/pricing.md",
      "heading": "Enterprise Pricing",
      "content": "Enterprise plans start at $2,000/mo...",
      "confidence": "high",
      "status": "published",
      "similarity": 0.87
    },
    ...
  ],
  "count": 5
}
```

## Edge Function Code (Deno/TypeScript)

```typescript
// supabase/functions/search_brain/index.ts
import { serve } from "https://deno.land/std@0.177.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
};

serve(async (req) => {
  // Handle CORS preflight
  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: corsHeaders });
  }

  // Verify brain key
  const authHeader = req.headers.get("Authorization");
  const brainKey = Deno.env.get("BRAIN_KEY");
  if (!authHeader || authHeader !== `Bearer ${brainKey}`) {
    return new Response(JSON.stringify({ error: "Unauthorized" }), {
      status: 401,
      headers: { ...corsHeaders, "Content-Type": "application/json" },
    });
  }

  const { mode, inputs, query } = await req.json();

  // Initialize Supabase client
  const supabase = createClient(
    Deno.env.get("SUPABASE_URL")!,
    Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!
  );

  try {
    if (mode === "embed") {
      return await handleEmbed(supabase, inputs);
    } else if (mode === "search") {
      return await handleSearch(supabase, query);
    } else {
      return new Response(JSON.stringify({ error: "Invalid mode" }), {
        status: 400,
        headers: { ...corsHeaders, "Content-Type": "application/json" },
      });
    }
  } catch (err) {
    console.error("Edge Function error:", err);
    return new Response(JSON.stringify({ error: err.message }), {
      status: 500,
      headers: { ...corsHeaders, "Content-Type": "application/json" },
    });
  }
});

async function handleEmbed(supabase: any, inputs: string[]) {
  const openaiKey = Deno.env.get("OPENAI_API_KEY");
  if (!openaiKey) throw new Error("OPENAI_API_KEY not set");

  const embeddings = [];
  for (const input of inputs) {
    const res = await fetch("https://api.openai.com/v1/embeddings", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${openaiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        model: "text-embedding-3-small",
        input: input,
        dimensions: 384,
      }),
    });
    const data = await res.json();
    if (data.error) throw new Error(data.error.message);
    embeddings.push(data.data[0].embedding);
  }

  return new Response(JSON.stringify(embeddings), {
    headers: { ...corsHeaders, "Content-Type": "application/json" },
  });
}

async function handleSearch(supabase: any, query: string) {
  const openaiKey = Deno.env.get("OPENAI_API_KEY");
  if (!openaiKey) throw new Error("OPENAI_API_KEY not set");

  // 1. Embed the query
  const embedRes = await fetch("https://api.openai.com/v1/embeddings", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${openaiKey}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model: "text-embedding-3-small",
      input: query,
      dimensions: 384,
    }),
  });
  const embedData = await embedRes.json();
  if (embedData.error) throw new Error(embedData.error.message);
  const queryEmbedding = embedData.data[0].embedding;

  // 2. Vector search via RPC (cosine similarity)
  const { data: results, error } = await supabase.rpc("match_brain_chunks", {
    query_embedding: queryEmbedding,
    match_threshold: 0.7,      // Cosine similarity threshold
    match_count: 10,           // Top-k
    filter_confidence: "high", // Optional: filter by confidence
  });

  if (error) throw error;

  return new Response(JSON.stringify({ results, count: results.length }), {
    headers: { ...corsHeaders, "Content-Type": "application/json" },
  });
}
```

## Required Database RPC Function

```sql
-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- RPC for cosine similarity search
CREATE OR REPLACE FUNCTION match_brain_chunks(
  query_embedding vector(384),
  match_threshold float DEFAULT 0.7,
  match_count int DEFAULT 10,
  filter_confidence text DEFAULT NULL
)
RETURNS TABLE (
  id uuid,
  path text,
  heading text,
  content text,
  confidence text,
  status text,
  metadata jsonb,
  similarity float
)
LANGUAGE sql STABLE
AS $$
  SELECT
    bc.id,
    bc.path,
    bc.heading,
    bc.content,
    bc.confidence,
    bc.status,
    bc.metadata,
    1 - (bc.embedding <=> query_embedding) AS similarity
  FROM brain_chunks bc
  WHERE 1 - (bc.embedding <=> query_embedding) > match_threshold
    AND (filter_confidence IS NULL OR bc.confidence = filter_confidence)
  ORDER BY bc.embedding <=> query_embedding
  LIMIT match_count;
$$;
```

## Environment Variables (Supabase Dashboard → Edge Functions → Settings)

| Variable | Description |
|----------|-------------|
| `BRAIN_KEY` | Secret key for n8n → Edge Function auth (generate: `openssl rand -hex 32`) |
| `OPENAI_API_KEY` | OpenAI API key for embeddings |
| `SUPABASE_URL` | Auto-injected by Supabase |
| `SUPABASE_SERVICE_ROLE_KEY` | Auto-injected by Supabase |

## Deployment

```bash
# Install Supabase CLI
npm install -g supabase

# Login & link project
supabase login
supabase link --project-ref <your-project-ref>

# Deploy function
supabase functions deploy search_brain --no-verify-jwt

# Set secrets
supabase secrets set BRAIN_KEY=<your-key> OPENAI_API_KEY=<your-key>
```

## Local Development

```bash
supabase start
supabase functions serve search_brain --env-file .env.local
```

## Ingestion Script (Run Once / Periodically)

```typescript
// scripts/ingest-brain.ts
import { createClient } from "@supabase/supabase-js";
import fs from "fs";
import path from "path";

const supabase = createClient(process.env.SUPABASE_URL!, process.env.SUPABASE_SERVICE_ROLE_KEY!);

async function ingest() {
  // 1. Walk wiki/modules, read .md files
  // 2. Chunk by heading (preserve heading path)
  // 3. Call Edge Function mode=embed for batches
  // 4. Upsert to brain_chunks with path, heading, content, embedding, confidence, status, metadata
}

ingest();
```

## Performance Tuning

| Parameter | Recommendation |
|-----------|----------------|
| `match_threshold` | 0.7 (cosine); lower = more recall, higher = more precision |
| `match_count` | 10 for agent (fits in context); 20 for human review |
| IVFFLAT `lists` | 100 for ~10k chunks; scale with `sqrt(rows)` |
| Embedding model | `text-embedding-3-small` (384 dim, fast, cheap) |
| Batch embed size | 20-50 inputs per Edge Function call |

## Related Pages

- [[overview]] — System architecture
- [[n8n-setup]] — n8n HTTP Request tool config
- [[database-schema]] — brain_chunks table, indexes, RLS
- [[wiki/modules/programming/SAAS_BUILD_NOTES|SaaS Build Notes]] — Supabase Edge Function patterns (E3, E8, E13)