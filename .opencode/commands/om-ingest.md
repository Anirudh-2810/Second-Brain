---
description: "Ingest raw sources into the wiki. Map a raw-sources file to its syllabus module and distill it into linked concept pages."
---

Ingest from raw sources: $ARGUMENTS

(No argument = list unprocessed candidates in `raw-sources/` and propose what to ingest next.)

Workflow:
1. **Locate & read** the raw document in `raw-sources/` (never modify it)
2. **Map** it to the relevant module under `wiki/01-Areas/<Domain>/<module>/` — check the domain's INDEX.md; if no module fits, create one + run update-graph-colors.py & generate-index.py
3. **Extract** definitions, key algorithms, mathematical proofs, formulas, and core implementations
4. **Create/update concept pages** — atomic (one concept per page when substantial), full YAML frontmatter (`course_code`, `course_name`, `unit`, `tags: [btech, kjsce, concept]`, `last_updated`), LaTeX for math, language-tagged code blocks
5. **Cross-link** related concepts and prerequisites with `[[wikilinks]]`; link back from parent topic pages
6. **Update** `wiki/index.md` under the right subject/module and append to `wiki/log.md`
7. Suggest exam-prep follow-up if the material covers assessable units
