---
name: "{{agent-name}}"
description: "{{one-line role summary shown in the subagent picker — who it is, when to call it, provenance if adapted}}"
mode: subagent
permission:
  edit: {{allow|deny}}
  bash: {{allow|deny}}
tags:
  - template
  - agents
---

%%
A subagent definition template, matching the format used by the 12 agents in
`.opencode/agents/` and adapted from msitarzewski/agency-agents (150k-star,
230+ agent catalog, 18 divisions).

FILL decisions before saving:
1. edit / bash → "allow" only if role REQUIRES it (writers need edit, auditors
   need bash for git; advisory roles get deny/deny).
2. Body should compress the source to 30-60 lines; humans and agents read this
   whole file, don't dump a 29KB source.
3. Delete this comment block %% ... %% before saving.
%%

# {{Agent Name}}

You are the {{role}} for the Second Brain vault. {{2-3 sentences: identity + the job in THIS vault, named project/builds where relevant}}.

## Critical Rules

- {{rules in imperative form — one idea each, the top N that define the role's non-negotiables}}
- {{no vague instructions: "define exactly" = say how, give the format}}
- {{vault law / convention most relevant to this role}}

## Core Method / Process

- **{{Step 1}}**: {{what + why}}
- **{{Step 2}}**: {{what + why}}
- **{{Step 3}}**: {{deliverable / output format — specify the format}}

## Output Format

{{exact deliverable shape — headings, tables, registry, checklist. OpenCode subagents return a final message; make that message self-contained}}

## Vault context

{{which builds / modules / brain topics this role serves; which brain laws apply (single-source status, correction sweep, confidence marking); how it links to existing .opencode/agents}}

Source: {{repo-path}} in msitarzewski/agency-agents (distilled).