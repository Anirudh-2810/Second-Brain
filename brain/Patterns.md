---
date: "2026-08-23"
type: "pattern"
tags: [freelancing, pricing, psychology, business]
confidence: stated
---

## For future agent
Captured from live interview 2026-08-23. The user's actual pricing behavior around micro-freelancing (slide decks), revealing anchoring language, a "don't feel like it" floor at ₹250, and a hypothetical ₹500 "worth it" threshold never tested. Negative knowledge: they walked away from a second ₹250 gig due to friction + low pay, not inability.

# Freelancing Pricing — Micro-gig Psychology

**Anchor phrase used:** *"it seems difficult but for you ill do it at 250rs"*

- Deliberate anchoring: "difficult" frames effort → justifies price → makes ₹250 feel like a favor
- Actual work: Canva deck, ~10-15 slides, smooth transitions (morph-style), malware prevention topic for CS project
- Time cost: ~2-3 hours (user's estimate)
- Client returned for second deck (Python functions explainer) → user **refused at same ₹250**

**The refusal trigger:** Not the topic. "Too tired" = "already had one to do + ₹250 is kinda less." Friction + low pay = walk away.

**Stated "worth it" floor:** ₹500 — but **never asked for it**. Hypothetical only.

**Negative knowledge (what doesn't work):**
- ₹250 with any friction (competing work, low motivation) → refusal, not negotiation
- Anchoring works to *get* the gig but doesn't protect against resentment at that price point
- No data on ₹500+ — untested hypothesis

**Open question:** Why not quote ₹500 next time? Fear of "no"? Imposter? Habit?

## Acquisition Model: Pure Inbound Only

- **First (and only) gig:** Classmate *walked up* — zero outbound, zero need-spotting
- **User's words:** *"they just came up to me"* / *"i cant identify ones req adn weakness by looking at them so i never knew what to offer"*
- **Result:** One gig at ₹250, one refusal at same price, zero proactive pitches since
- **Negative knowledge:** Without inbound trigger → no offer made → no revenue. The skill (deck building) exists; the *sales motion* does not.

**Implication:** ₹500 is untested because the *only* activation path is "someone asks." No ask = no quote = no data.

## Stock-Agent as Credential: The Deflection Pattern

- User knows the gaps (inverted kill-switch, disabled scheduler, NULL features, zero tests, unhosted)
- **But** when asked how they'd handle a recruiter questioning the kill-switch bug: *"ill say it that we came across it while testing, one of our testor came across it; we'll be fixing it we're working out solutions on it"*
- **Translation:** Deflect ownership ("tester found it"), imply a team ("we"), vague future fix ("working out solutions") — instead of *"I introduced it, here's why, here's the fix"*
- **Implication:** The project is a **prop**, not a portfolio piece. The goal is the *appearance* of a complex system, not the ability to defend it.
- **Negative knowledge:** Without line-by-line ownership, any technical interviewer will probe → deflection detected → credibility collapses.

## Spatial Visualization Gap (Engineering Drawing)

- **Topic:** Orthographic projections — 90° rotation between planar views (front → top/side)
- **Mental block:** Viewpoint visualization — can't mentally rotate the object; "glass box" projector method doesn't translate to intuition
- **What helped marginally:** Physical model (holding a box) — but *didn't fully click*
- **What didn't work:** Diagrams, textbook explanations, quadrant method, mental rotation
- **Implication:** User needs **kinesthetic / embodied** spatial reasoning, not 2D diagrams. Traditional ED teaching (projections on paper) mismatches their cognitive style.
- **Actionable:** 3D CAD (Onshape/Fusion) with live view manipulation > paper sketches. Or physical foam models for every new projection type.

## Learning Loop: Project-Driven → Just-in-Time

- **Trigger:** Project idea (Gemini-suggested habit tracker) → need specific tools (`re`, `datetime`)
- **Source:** YouTube (search-driven, not curriculum-driven)
- **Pattern:** Learn *only what the project demands*; no systematic coverage
- **Evidence:** CS50 `datetime` + `re` for habit tracker; skipped unrelated stdlib modules
- **Negative knowledge:** Gaps accumulate silently — you don't know what you don't know until a project needs it
- **Implication:** Efficient for shipping, risky for interviews (can't answer "how does X work?" if no project needed X)

## Quant Study: Read-Only Illusion

- **Wiki has 18 quant pages** (momentum, pairs trading, VaR, BS, portfolio opt, etc.)
- **User read:** Full momentum (Jegadeesh-Titman) + pairs trading (Gatev) pages
- **Code written:** **Zero** — no ranker, no cointegration test, no backtest snippet
- **Negative knowledge:** Reading ≠ understanding. Without implementation, you can't explain *why* skip=1 month matters, or how Gatev's 6-month formation / 6-month holding actually works on noisy NSE data.
- **Implication:** Quant knowledge is currently **decorative** — looks good in wiki, collapses under "show me the code."

## Vlogging Friction: Over-Tooling

- **Yesterday:** Raw college vlog footage on phone (auto travel → class)
- **Planned workflow:** After Effects + Lightroom edit → post
- **Blocker:** Pro-tool chain for daily content = **perfectionism trap**. AE + LR = 30-60 min per minute of footage. Daily vlog = unsustainable.
- **Negative knowledge:** High-friction tooling kills consistency. Phone-native (CapCut/InShot) or one-take posting beats "perfect edit never posted."

## Habit Stacking: Energy Budgeting (Not Time)

- **Five tracked:** Study, Exercise, Mood, Vlogging, Guitar
- **Reality:** "Exhausted — either study or gym, clogging" (schedule conflict)
- **Guitar:** Broken → repair → paused
- **Pattern:** User treats habits as *additive* (5 × daily) but energy is *subtractive* — each high-effort habit drains the pool for others
- **Negative knowledge:** Tracking 5 habits ≠ doing 5 habits. The tracker becomes a guilt ledger.
- **Actionable:** Pick **one anchor habit** (Study? Exercise?) → others become "bonus." Or rotate: Mon/Wed/Fri = Study + Exercise; Tue/Thu/Sat = Vlog + Guitar. Energy-aware scheduling > streak-chasing.

## Stated Priority Order (Energy Allocation)

1. **Gym** — non-negotiable anchor
2. **Study** — academic survival + quant prep
3. **Vlog** — creative outlet / future asset
4. **Guitar** — paused (repair)
5. **Mood** — measurement, not activity

## Gym Anchor: Concrete Protocol

- **Good day:** Dumbbells 30 reps (compound: press/row/squat variations) → Legs (squats, lunges, calf raises)
- **Bad-day minimum:** *Not yet defined* — "streak doesn't break" needs a floor (e.g., 1 set pushups + 1 set bodyweight squats = 5 min)
- **Negative knowledge:** Without a defined minimum, "exhausted" days become zero days → streak breaks → guilt spiral.

## Retrieval Agent Patterns (Business Brain)

### Pattern: Search-First, Never Generalize
- **Rule**: Every user question → tool call first. No exceptions.
- **Enforcement**: System prompt Rule 1 + temperature 0.2 + tool attached to agent.
- **Failure mode**: Agent answers without searching → system prompt not enforced or tool not connected.
- **Detection**: Check n8n execution log — tool call must precede final answer.

### Pattern: Multi-Search on Thin Results
- **Rule**: If first search returns < 3 chunks OR max similarity < 0.75 → rephrase and search again.
- **Rephrase strategies**: Synonyms (ICP → "ideal customer profile"), broader ("pricing" → "enterprise pricing model"), narrower ("refund" → "refund policy enterprise"), different angle ("how" → "process steps").
- **Max attempts**: 2-3 before refusing.

### Pattern: Refusal Over Hallucination
- **Rule**: Search succeeds (200 OK) but chunks don't answer → "That's not in the brain yet. I searched for '[query]'."
- **Never**: "I don't know", "Probably X", "Based on general knowledge..."
- **Why**: In business contexts, a confident wrong answer destroys trust; explicit refusal preserves it.

### Pattern: Tool Error ≠ Missing Fact
- **Rule**: Any tool error (DNS, timeout, 401, 500) → "I can't reach the brain right now — that's a system problem, not a missing note." Then STOP.
- **Critical distinction**: Without this, downtime = "fact not documented" in agent's language — same words, opposite meaning.
- **Test**: Kill Edge Function → ask question → verify agent says system problem, not "not in brain."

### Pattern: Confidence-Weighted Answers
- **high**: State as fact ("Our pricing is $X/mo.")
- **medium**: Hedge ("Our pricing appears to be $X/mo (source notes medium confidence).")
- **low/speculation**: Explicit ("One note speculates pricing might be $X/mo, but this is unproven.")
- **draft**: "This is from a draft note and may change."
- **archived**: "This is from an archived note and may be outdated."
- **Implementation**: Edge Function RPC filters by confidence; agent reads confidence from chunk metadata.

### Pattern: Verbatim Quoting for Scripts/Rebuttals
- **Rule**: For cold emails, objection handling, exact promises → quote source note word-for-word.
- **Paraphrase only**: Summaries, context, process descriptions.
- **Why**: Owner's exact phrasing carries authority; paraphrasing loses nuance.

### Pattern: No Invented Metrics
- **Rule**: Never state leads, CPL, conversion, ROI, revenue, churn, CAC, LTV unless explicitly in brain chunks.
- **Response**: "That's not in the brain yet. I searched for 'conversion rate Q3'."
- **Why**: Made-up numbers in business contexts are liability.

### Pattern: Heading-Aware Chunking with Metadata
- **Ingestion**: Chunk Markdown by heading (preserve heading path), embed each chunk.
- **Storage**: Each chunk stores `path`, `heading`, `confidence`, `status`, `frontmatter` in `metadata` JSONB.
- **Benefits**: Filtered search (by confidence/status), human-readable citations (file path + heading), context preservation.

### Pattern: n8n as Orchestration, Edge Function as Logic
- **n8n role**: Chat Trigger → AI Agent (model, memory, system prompt) → HTTP Request tool.
- **Edge Function role**: Embedding (OpenAI), vector search (pgvector), RPC, auth.
- **Why**: n8n workflows stay portable; heavy logic in version-controlled TypeScript; scaling independent.

### Pattern: IVFFLAT Index Maintenance
- **Lists parameter**: `lists ≈ sqrt(row_count)` — rebuild after bulk ingestion.
- **Monitor**: `pg_stat_user_indexes` for `idx_scan` — if dropping, rebuild.
- **Threshold**: For >50k rows, consider HNSW (`vector_hnsw_ops`) for better recall/latency.