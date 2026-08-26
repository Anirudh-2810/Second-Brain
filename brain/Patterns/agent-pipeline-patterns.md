---
module: "self-dev"
topic: "Agent Pipeline Patterns — From Understand-Anything"
tags: [patterns, agent-pipeline, deterministic-llm, skill-agent, tree-sitter, knowledge-graph, design-system]
last_updated: "2026-08-26"
confidence: "high"
source: "C:\Users\Vijaykumar\Understand-Anything"
description: "Key design patterns learned from Understand-Anything: deterministic + LLM hybrid analysis, skill/agent file structure, graph-first UI, dark luxury design system. Applicable to vault workflows, codebase analysis, and agent-driven tools."
---

# Agent Pipeline Patterns — From Understand-Anything

> **Source:** Analyzed from `C:\Users\Vijaykumar\Understand-Anything`
> **Purpose:** Extract reusable patterns for vault workflows and agent-driven tools

---

## For future agent
Key design patterns extracted from Understand-Anything codebase analysis tool. These patterns apply to vault workflows, codebase analysis, and any agent-driven automation. Cross-links: [[wiki/01-Areas/AI-Data/agent-systems]], [[brain/Patterns]], [[wiki/00-Current-Projects/understand-anything]].

---

## Pattern 1: Deterministic + LLM Hybrid Analysis

### Core Insight
**Don't send raw code to LLMs — extract structure first, then analyze semantics.**

### Two-Phase Pipeline
```
Phase 1 (Deterministic): Fast, cheap, no API costs
  - tree-sitter AST parsing
  - Regex pattern matching
  - File structure extraction
  - Dependency graph building

Phase 2 (LLM): Rich semantic analysis
  - Code understanding
  - Pattern detection
  - Architecture analysis
  - Documentation generation
```

### Benefits
- **Cost reduction**: 80% less LLM API calls
- **Speed**: Deterministic phase is 10-100x faster
- **Accuracy**: Structural facts are always correct
- **Reliability**: No hallucinations in Phase 1

### Application to Vault
```
Phase 1 (Deterministic): 
  - Scan markdown files for wikilinks
  - Extract frontmatter fields
  - Count headings, words, code blocks
  - Build link graph

Phase 2 (LLM):
  - Analyze note quality
  - Suggest cross-links
  - Generate summaries
  - Detect orphan notes
```

---

## Pattern 2: Skill/Agent File Structure

### Skills (SKILL.md)
Skills define **what to do** — structured prompts with clear inputs/outputs:

```markdown
# Skill Name

Brief description of what this skill does.

## Inputs
- `param1`: Description
- `param2`: Description

## Process
1. Step 1
2. Step 2
3. Step 3

## Output
- Description of output format
```

### Agents (.md files)
Agents define **how to do it** — phase-based execution with explicit steps:

```markdown
# Agent Name

## Phase 1: Discovery
1. Step 1.1
2. Step 1.2

## Phase 2: Analysis
1. Step 2.1
2. Step 2.2

## Phase 3: Output
1. Step 3.1
```

### Benefits
- **Version control**: Skills/agents are plain markdown
- **Composability**: Agents can use skills
- **Clarity**: Explicit steps, no ambiguity
- **Iteration**: Easy to refine prompts

### Application to Vault
```
Skills:
  - om-ingest: How to ingest content
  - om-wrap-up: How to end a session
  - om-dump: How to capture freeform input

Agents:
  - context-loader: Load vault context
  - cross-linker: Find missing links
  - vault-librarian: Deep maintenance
```

---

## Pattern 3: Graph-First UI

### Layout Strategy
```
75% Canvas — Interactive visualization
360px Sidebar — Entity details
```

### Why 75/25 Split?
- **Graph is primary**: Users want to see relationships
- **Sidebar is secondary**: Details on demand
- **Responsive**: Sidebar collapses on mobile

### State Management (Zustand)
```typescript
interface GraphStore {
  nodes: Node[];
  edges: Edge[];
  selectedNode: Node | null;
  filters: FilterState;
  
  // Actions
  setGraph: (nodes, edges) => void;
  selectNode: (node) => void;
  applyFilters: (filters) => void;
}
```

### Application to Vault
- **75%**: Obsidian graph view (native)
- **360px**: Note preview sidebar
- **Filters**: Tags, domains, date ranges

---

## Pattern 4: Dark Luxury Design System

### Color Palette
```css
:root {
  --bg-primary: #0a0a0a;      /* Near-black */
  --bg-secondary: #111111;     /* Card backgrounds */
  --bg-tertiary: #1a1a1a;      /* Elevated surfaces */
  
  --accent-primary: #d4a574;   /* Gold/Amber */
  --accent-secondary: #b8956a; /* Muted gold */
  
  --text-primary: #ffffff;
  --text-secondary: #a0a0a0;
  
  --border-subtle: #1f1f1f;
  --border-default: #333333;
}
```

### Design Principles
1. **High contrast**: White text on near-black
2. **Gold accents**: Luxury feel, not flashy
3. **Subtle borders**: Don't compete with content
4. **Consistent spacing**: 4px grid system

### Application to Vault
- **Dark theme**: Obsidian dark mode
- **Accent colors**: Domain-specific (blue=programming, green=ai-data)
- **Consistent typography**: Inter font family

---

## Pattern 5: Plugin Architecture

### Plugin Types
1. **Skills**: Self-contained prompts
2. **Agents**: Phase-based execution
3. **Dashboard**: Visualization components

### Extension Points
- Add new skill: Create SKILL.md
- Add new agent: Create .md with phases
- Add new visualization: React component

### Benefits
- **Modularity**: Each plugin is independent
- **Testability**: Test skills/agents in isolation
- **Reusability**: Skills can be shared across agents

### Application to Vault
```
Plugin Types:
  - Commands: Slash commands (/om-*)
  - Subagents: Task-specific agents
  - Skills: Workflow templates

Extension Points:
  - Add command: .opencode/commands/
  - Add agent: .opencode/agents/
  - Add skill: .opencode/skills/
```

---

## Key Takeaways

| Pattern | Core Idea | Vault Application |
|---------|-----------|-------------------|
| **Deterministic + LLM** | Structure first, semantics second | Link graph before quality analysis |
| **Skill/Agent Structure** | What vs How | Commands vs Subagents |
| **Graph-First UI** | 75% canvas, 360px sidebar | Obsidian graph + preview |
| **Dark Luxury Theme** | Near-black + gold accents | Consistent vault styling |
| **Plugin Architecture** | Modular, composable | Commands + Agents + Skills |

---

## See Also
- [[brain/Patterns]] — All vault patterns
- [[wiki/01-Areas/AI-Data/agent-systems]] — Multi-agent systems
- [[wiki/00-Current-Projects/understand-anything]] — Source project