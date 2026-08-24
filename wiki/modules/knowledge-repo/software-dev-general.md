---
course_code: "KNOWLEDGE-REPO"
course_name: "Knowledge Repository — Curated Learning Resources (niderhoff)"
unit: "Module 6 — Software Development (General)"
tags: [software-development, algorithms, data-structures, big-o, interview-prep, software-architecture, cli, git, code-review]
last_updated: "2026-08-24"
confidence: "high"
source: "https://github.com/niderhoff/knowledge-repository#in-general"
---

## For future agent
Language-agnostic software engineering resources: CS fundamentals, DS&A study systems, architecture thinking, engineering practices (code review, git, CLI). The algorithms/interview section is the strongest part. Use when leveling up general engineering skill or preparing for technical interviews.

# Software Development — General

## Learning Tools
- [Learn Anything](https://learn-anything.xyz/) — visual knowledge-map search engine
- **[learnXinYminutes](https://learnxinyminutes.com/)** — syntax tour of any language in minutes; first stop in a new language
- [devhints](https://devhints.io/) — cheatsheet collection

## CS Fundamentals & Knowledge
- **[Teach Yourself Computer Science](https://teachyourselfcs.com/)** — the 9-subject self-taught curriculum with one book + one course each; the canonical answer to "how do I learn CS properly"
- [Things Every Programmer Should Know](https://github.com/mr-mig/every-programmer-should-know)
- [Naming Conventions (wikiwand)](https://www.wikiwand.com/en/Naming_convention_(programming))
- [Functional Programming Jargon](https://functional.works-hub.com/blog/Functional-Programming-Jargon)
- [Computer Science for Engineers (Robert Elder)](https://blog.robertelder.org/computer-science-for-engineers/)
- Books: [Must-reads for devs without CS degree (HN thread)](https://news.ycombinator.com/item?id=22803780); [TAOCP (Knuth)](https://www.amazon.com/Computer-Programming-Volumes-1-4A-Boxed/dp/0321751043/) — reference, not reading
- **[Big-O Cheat Sheet](https://www.bigocheatsheet.com/)** — complexity tables for all structures/algorithms

## Algorithms & Data Structures / Interview Prep

### Study Systems
| Resource | Type |
|----------|------|
| **[Coding Interview University (jwasham)](https://github.com/jwasham/coding-interview-university)** | Multi-month checklist: self-taught → big-tech SWE |
| [geeksforgeeks DS section](https://www.geeksforgeeks.org/data-structures/) | Theory + practice + examples |
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | Every algorithm, implemented |
| [javascript-algorithms (trekhleb)](https://github.com/trekhleb/javascript-algorithms) | Same, JS, excellent docs |

### Visualizations (build intuition)
- **[visualgo](https://visualgo.net/)** — animated data structure operations
- [algorithm-visualizer.org](https://algorithm-visualizer.org/)
- [USF Data Structure Visualizations](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)

### Books
- [Algorithms in C (Sedgewick, 5-part)](https://www.amazon.com/Algorithms-Parts-1-5-Bundle-Fundamentals/dp/0201756080/)
- [Data Structures and Abstractions with Java (4th ed.)](https://www.amazon.com/Data-Structures-Abstractions-Java-4th/dp/0133744051)
- [Problem Solving with Algorithms and DS using Python (2nd ed.)](https://www.amazon.com/Problem-Solving-Algorithms-Structures-Python/dp/1590282574)
- Advanced: **[CLRS Introduction to Algorithms (3rd ed.)](https://www.amazon.com/Introduction-Algorithms-3rd-MIT-Press/dp/0262033844/)** — the reference; algorithmic-reasoning sections praised

### Practice Platforms
- [LeetCode](https://leetcode.com/) · [HackerRank](https://www.hackerrank.com/)

### Components & Internals
- [What is a Lambda Function? (SO deep-dive)](https://stackoverflow.com/questions/16501/what-is-a-lambda-function)
- [An Intro to Compilers (nicoleorchard)](https://nicoleorchard.com/blog/compilers)

## Software Architecture
- **[Software Architecture Guide (Martin Fowler)](https://martinfowler.com/architecture/)** — start here
- [The Architecture of Open Source Applications](http://aosabook.org/en/index.html) — real architects explain real systems
- [Software Architecture Patterns (free O'Reilly PDF)](https://www.oreilly.com/programming/free/files/software-architecture-patterns.pdf) — layered/event-driven/microkernel/space-based/CQRS
- **[C4 Model](https://c4model.com/)** — Context/Containers/Components/Code diagramming standard
- [SoftwareArchitect roadmap (justinamiller)](https://github.com/justinamiller/SoftwareArchitect)
- Design patterns origin: [GoF on Wikipedia](https://en.wikipedia.org/wiki/Design_Patterns) → vault impl: [[modules/object-oriented-programming/design-patterns]]

## Engineering Practices
- **[How to do a code review (Google eng-practices)](https://google.github.io/eng-practices/review/reviewer/)** — Google's official reviewer guide
- Git: [Interactive tutorial](https://try.github.io/)
- CI/CD mindset: ["I am a mediocre developer" (sobolevn)](https://dev.to/sobolevn/i-am-a-mediocre-developer--30hn) — automation over heroics

## Command Line Mastery
- **[The Art of Command Line](https://github.com/jlevy/the-art-of-command-line)** — the definitive interactive-shell fluency guide
- [htop explained (peteris.rocks)](https://peteris.rocks/blog/htop/) — read every column
- [tldr pages](https://tldr.ostera.io/) · **[explainshell](https://www.explainshell.com/)** — paste any command, get it explained token-by-token
- Bash: [Wooledge BashGuide](http://mywiki.wooledge.org/BashGuide) · [bash-hackers wiki](https://wiki.bash-hackers.org/) · [conditional constructs (GNU manual)](https://www.gnu.org/software/bash/manual/html_node/Conditional-Constructs.html)
- [Mastering jq (codefaster)](https://codefaster.substack.com/p/mastering-jq-part-1-59c) — JSON parsing in shell
- Text processing by example: [Command-line text processing (learnbyexample)](https://github.com/learnbyexample/Command-line-text-processing)

## Tooling
- [analysis-tools.dev](https://analysis-tools.dev/) — compare 483+ static analysis tools across languages

## Related Pages

- [[overview]] · [[languages-python-advanced]] · [[language-rust]] · [[languages-polyglot]]
- [[modules/programming/cs50/index|CS50x]] — vault's practiced fundamentals (this page extends it)
- [[modules/programming/cs50/problem-sets|CS50 PSet catalog]] — practice problems pairing with LeetCode
- [[roadmaps-and-study-guides]] — where interview prep fits a full plan