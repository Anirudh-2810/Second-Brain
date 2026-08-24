---
course_code: "LEARNRES"
course_name: "Learning Resource Catalogs"
unit: "Resource 3 — EbookFoundation/free-programming-books"
tags: [books, free-resources, catalogs, learning-resources, multilingual]
last_updated: "2026-08-24"
confidence: "high"
source: "https://github.com/EbookFoundation/free-programming-books"
---

## For future agent
The canonical free programming books index (350k+ stars): thousands of free legal books/courses by language and topic, including multilingual editions. This page adds selection discipline — book-hoarding is the classic failure. Feeds [[software-dev-general]], [[01-Areas/Programming/cs50/index]].

# Free Programming Books — The Library Index

## What It Contains

Organized by: language-specific resources · free online courses · interactive programming resources · problem sets & competitive programming · **multilingual sections** (Hindi and other non-English lists exist) · podcast/screencast series.

## Selection Protocol

```mermaid
flowchart TD
    N["Need a book for<br/>CURRENT topic"] --> S{"Topic has a vault<br/>canonical pick already?"}
    S -->|"yes"| U["Use the vault pick<br/>(e.g., DL Book, Fluent Python)"]
    S -->|"no"| P["Pick ONE from list by:<br/>recency + exercises included"]
    P --> R["30-page rule: if still unclear<br/>after 30 pages, swap - once"]
    U & R --> B["Book serves the build"]
```

## Failure Modes

| Failure | Mechanism | Counter |
|---------|-----------|---------|
| Library hoarding | Downloading 40 PDFs = dopamine of preparedness | Downloads allowed only when the book is CURRENT |
| Book-switching at chapter 3 | Hard chapters trigger better-feeling alternatives | 30-page rule + one-swap limit per topic |
| Tutorial-book mismatch | Reading reference texts linearly | Reference books are LOOKED UP, not read through |

**Premortem**: *Hard drive full of PDFs; none finished.* The library grew as identity ([[how-to-self-teach]] Engine 2). Books enter reading-status only with a start date + target chapters in daily notes.

## Life Integration

- One active technical book max; slot = commute/low-energy hours
- Vault note per finished book: 5-line summary + what changed in your code
- Metrics: books-finished per quarter (≥1), downloads-without-starting (target 0)

## Example Checkpoint Questions

1. Which book am I actually mid-way through right now?
2. Of my downloaded books, how many have notes? (Notes = read; no notes = hoarded.)

## Cross-Vault Links

[[02-Resources/learning-resources/index|Field Index]] · [[repo-teachyourselfcs]] · [[curated-reading-list]]