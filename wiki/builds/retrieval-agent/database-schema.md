---
course_code: "RETRIEVAL-AGENT"
course_name: "Business Brain Retrieval Agent"
unit: "Module 5 — Database Schema & Maintenance"
tags: [retrieval-agent, supabase, postgresql, pgvector, database-schema, rls, indexing, maintenance, vector-search]
last_updated: "2026-08-24"
confidence: "high"
---

## For future agent
This page documents the `brain_chunks` table schema, indexes, RLS policies, and maintenance operations. The schema is designed for cosine similarity search via pgvector with metadata filtering (confidence, status).

---

# Database Schema — `brain_chunks` Table

## Table Definition

```sql
-- Enable pgvector extension (run once)
CREATE EXTENSION IF NOT EXISTS vector;

-- Main chunks table
CREATE TABLE brain_chunks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  
  -- Source identification
  path TEXT NOT NULL,                    -- e.g., "wiki/modules/quant-finance/momentum-jegadeesh-titman.md"
  heading TEXT,                          -- Nearest heading: "## 3.1 Canonical Momentum Strategy"
  
  -- Content
  content TEXT NOT NULL,                 -- Chunk text (target 500-1000 chars)
  
  -- Vector embedding
  embedding VECTOR(384),                 -- OpenAI text-embedding-3-small (384 dims)
  
  -- Quality metadata
  confidence TEXT CHECK (confidence IN ('high', 'medium', 'low', 'speculation')) DEFAULT 'medium',
  status TEXT CHECK (status IN ('draft', 'published', 'archived')) DEFAULT 'published',
  
  -- Extracted frontmatter + custom fields
  metadata JSONB DEFAULT '{}',
  
  -- Timestamps
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Updated_at trigger
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER LANGUAGE plpgsql AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END $$;

CREATE TRIGGER brain_chunks_updated_at
  BEFORE UPDATE ON brain_chunks
  FOR EACH ROW EXECUTE FUNCTION update_updated_at();
```

## Indexes

```sql
-- IVFFLAT index for cosine similarity (ANN)
-- lists = sqrt(row_count) ~ 100 for 10k rows
CREATE INDEX brain_chunks_embedding_idx 
  ON brain_chunks USING ivfflat (embedding vector_cosine_ops) 
  WITH (lists = 100);

-- Path prefix for listing/navigation
CREATE INDEX brain_chunks_path_idx ON brain_chunks (path);

-- Filter indexes
CREATE INDEX brain_chunks_confidence_idx ON brain_chunks (confidence);
CREATE INDEX brain_chunks_status_idx ON brain_chunks (status);

-- Composite for common query: filter by confidence + vector search
-- (PostgreSQL doesn't support composite vector + btree, but planner uses both)
```

## RPC Function for Search

```sql
CREATE OR REPLACE FUNCTION match_brain_chunks(
  query_embedding vector(384),
  match_threshold float DEFAULT 0.7,
  match_count int DEFAULT 10,
  filter_confidence text DEFAULT NULL,
  filter_status text DEFAULT NULL
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
    AND (filter_status IS NULL OR bc.status = filter_status)
  ORDER BY bc.embedding <=> query_embedding
  LIMIT match_count;
$$;
```

## Row Level Security (RLS)

```sql
-- Enable RLS
ALTER TABLE brain_chunks ENABLE ROW LEVEL SECURITY;

-- Policy: Service role (Edge Function) has full access
CREATE POLICY "Service role full access" ON brain_chunks
  FOR ALL TO service_role USING (true) WITH CHECK (true);

-- Policy: Anon read access (if you want direct browser queries)
-- CREATE POLICY "Anon read published" ON brain_chunks
--   FOR SELECT TO anon USING (status = 'published');
```

## Metadata JSONB Structure

The `metadata` column stores extracted frontmatter and computed fields:

```json
{
  "course_code": "QUANT-FINANCE",
  "course_name": "Quantitative Finance",
  "unit": "Module 3 — Momentum Strategies",
  "tags": ["quant-finance", "momentum", "jegadeesh-titman"],
  "last_updated": "2026-08-15",
  "source": "raw-sources/quant-finance/momentum-jegadeesh-titman.pdf",
  "chunk_index": 3,
  "total_chunks": 12,
  "word_count": 847,
  "has_math": true,
  "has_code": false,
  "confidence_reason": "Primary source: Jegadeesh & Titman (1993) paper"
}
```

## Ingestion: Chunking Strategy

```python
# Pseudocode for heading-aware chunking
def chunk_markdown(file_path: Path) -> list[Chunk]:
    content = file_path.read_text()
    frontmatter, body = parse_frontmatter(content)
    
    chunks = []
    current_heading = ""
    current_text = []
    
    for line in body.split("\n"):
        if line.startswith("#"):
            # Save previous chunk
            if current_text:
                chunks.append(Chunk(
                    path=str(file_path.relative_to("wiki")),
                    heading=current_heading,
                    content="\n".join(current_text),
                    metadata=frontmatter
                ))
            current_heading = line.lstrip("#").strip()
            current_text = [line]
        else:
            current_text.append(line)
    
    # Don't forget last chunk
    if current_text:
        chunks.append(Chunk(...))
    
    # Merge small chunks (< 200 chars) with neighbors
    return merge_small_chunks(chunks, min_chars=200, max_chars=1500)
```

## Maintenance Operations

### Refresh IVFFLAT Index (Run After Bulk Ingestion)

```sql
-- Rebuild index with updated lists parameter
-- lists ≈ sqrt(row_count)
DROP INDEX brain_chunks_embedding_idx;
CREATE INDEX brain_chunks_embedding_idx 
  ON brain_chunks USING ivfflat (embedding vector_cosine_ops) 
  WITH (lists = 100);  -- Adjust based on row count
```

### Analyze Table Statistics

```sql
ANALYZE brain_chunks;
```

### Monitor Index Usage

```sql
SELECT 
  schemaname,
  tablename,
  indexname,
  idx_scan,
  idx_tup_read,
  idx_tup_fetch
FROM pg_stat_user_indexes
WHERE tablename = 'brain_chunks';
```

### Check Embedding Coverage

```sql
SELECT 
  COUNT(*) AS total_chunks,
  COUNT(embedding) AS with_embedding,
  COUNT(*) - COUNT(embedding) AS missing_embedding,
  ROUND(100.0 * COUNT(embedding) / COUNT(*), 1) AS coverage_pct
FROM brain_chunks;
```

### Cleanup Old/Archived Chunks

```sql
-- Soft delete: mark archived
UPDATE brain_chunks SET status = 'archived' WHERE path LIKE 'wiki/modules/old/%';

-- Hard delete (if needed)
DELETE FROM brain_chunks WHERE status = 'archived' AND updated_at < NOW() - INTERVAL '1 year';
```

## Performance Benchmarks (Reference)

| Rows | IVFFLAT lists | Query Latency (p95) | Recall@10 |
|------|---------------|---------------------|-----------|
| 1,000 | 30 | ~15ms | 0.98 |
| 10,000 | 100 | ~25ms | 0.95 |
| 50,000 | 220 | ~45ms | 0.92 |
| 100,000 | 316 | ~65ms | 0.90 |

> **Note**: For >50k rows, consider HNSW index (`vector_hnsw_ops`) for better recall/latency tradeoff.

## Related Pages

- [[overview]] — System architecture
- [[edge-function]] — Edge Function uses this schema
- [[retrieval-agent]] — Agent expects this data shape
- [[wiki/modules/programming/SAAS_BUILD_NOTES|SaaS Build Notes]] — Supabase patterns (RLS, RPC, migrations)