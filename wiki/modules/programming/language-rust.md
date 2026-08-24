---
course_code: "PROGRAMMING"
course_name: "Programming & Software Engineering Field"
unit: "Module 8 — Rust"
tags: [rust, systems-programming, memory-safety, concurrency, learning-resources]
last_updated: "2026-08-24"
confidence: "high"
source: "https://github.com/niderhoff/knowledge-repository#rust"
---

## For future agent
The Rust learning path from the knowledge repo, ordered from first contact to unsafe internals. Gets its own page because the repo's Rust section was unusually well curated. Use when starting Rust or going deeper than the Book.

# Rust — Learning Path

## The Official Path (in order)
1. **[The Rust Programming Language ("the Book")](https://doc.rust-lang.org/stable/book/)** — the canonical text; read cover-to-cover
2. **[Rustlings](https://github.com/rust-lang/rust-lang/rustlings)** *(correct: [rust-lang/rustlings](https://github.com/rust-lang/rustlings))* — small exercises drilling reading/writing Rust; do alongside the Book
3. **[Rust By Example](https://doc.rust-lang.org/stable/rust-by-example/)** — companion examples when the Book's prose is dense
4. **[The Rust Reference](https://doc.rust-lang.org/stable/reference/index.html)** — precise language semantics lookup

## Going Deeper
| Resource | What You Learn |
|----------|---------------|
| **[Learning Rust with Entirely Too Many Linked Lists](https://rust-unofficial.github.io/too-many-lists/)** | Ownership/borrowing *through failure* — the best intermediate text on why Rust fights you |
| **[Programming Rust (Blandy & Orendorff)](https://www.goodreads.com/book/show/25550614-programming-rust)** | ⭐ per source: best book for experienced developers; systems depth |
| **[The Rustonomicon](https://doc.rust-lang.org/stable/nomicon/index.html)** | "The Dark Arts of Unsafe Rust" — only after ownership is instinct |
| [Hands-On Concurrency with Rust](https://www.amazon.com/dp/1788399978) | Memory-safe parallel design |
| [Hands-On Data Structures & Algorithms with Rust](https://www.amazon.com/dp/178899552X) | Classic structures in a borrow-checker world |

## Alternative On-Ramps
- **[Easy Rust (Dhghomon)](https://github.com/Dhghomon/easy_rust)** — plain-English rewrite; great for non-native speakers or quick orientation
- **[tl;dr Rust (christine.website)](https://christine.website/blog/TLDR-rust-2020-09-19)** — pattern overview with Go comparisons
- [OMG WTF RS resources roundup (Ferrous Systems, archived)](https://web.archive.org/web/20200923111823/https://ferrous-systems.com/blog/omg-wtf-rs-resources-to-help-you-get-started-with-rust/)
- **[Stanford CS110L: Safety in Systems Programming](https://reberhardt.com/cs110l/spring-2020/)** — full undergrad course using Rust to teach systems safety

## Web Frameworks
- [Choosing a Rust Web Framework: 2020 Edition (lpalmieri)](https://www.lpalmieri.com/posts/2020-07-04-choosing-a-rust-web-framework-2020-edition/) — actix vs warp vs rocket decision analysis
- 2026 note `(TBC)`: ecosystem has since consolidated around axum; verify current state before choosing

## Perspective
- [Scala Developer's Journey into Rust (madhukaraphatak)](http://blog.madhukaraphatak.com/rust-scala-part-1/) — JVM-dev migration lens

## Why Rust for This Vault

- [[modules/quant-finance/quant-toolkit-and-skills]] lists C++ as the quant-industry language — Rust is the modern alternative gaining HFT/market-infrastructure adoption `(TBC)`
- Memory-safety-without-GC maps to matching-engine latency work: see [[modules/ai-ml/matching-engine-cpp]] for the C++ version of the same problem

## Related Pages

- [[modules/programming/overview|Programming Hub]] · [[software-dev-general]] · [[languages-polyglot]]
- [[modules/programming/cs50/week-4-memory|CS50 Week 4 — Memory]] — pointers/stack/heap intuition that Rust formalizes