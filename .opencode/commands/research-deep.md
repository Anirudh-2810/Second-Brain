\---

description: Execute vault-gated deep research with gap identification and external search delta report

\---



Target: $ARG1



Execute Deep Research using the following pipeline:



1\. VAULT SCAN:

&#x20;  - Perform a local workspace scan using `ripgrep` (`rg`) to locate existing notes, technical specs, and references related to "$ARG1".

&#x20;  - Collect file paths and relevant excerpts.



2\. GAP IDENTIFICATION:

&#x20;  - Compare local workspace context against the objective requirements for "$ARG1".

&#x20;  - Highlight missing sub-topics, unverified technical assumptions, deprecated APIs, or missing architectural details.



3\. EXTERNAL SEARCH:

&#x20;  - Query external sources (via web search / Tavily / Perplexity tools) explicitly targeting the missing gaps identified in Step 2.



4\. DELTA REPORT GENERATION:

&#x20;  - Output a clean Markdown report with the following structure:

&#x20;    - \*\*Vault Knowledge Base\*\*: Existing local references (with relative file paths).

&#x20;    - \*\*Confirmed External Additions\*\*: New verified facts and syntax specifications (with sources).

&#x20;    - \*\*Discrepancies \& Contradictions\*\*: Conflict resolutions between existing workspace notes and updated external documentation.

&#x20;    - \*\*Recommended Action Items\*\*: Specific edits or new files to add to the workspace.

