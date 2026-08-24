---
course_code: "PROGRAMMING"
course_name: "Programming & Software Engineering Field"
unit: "Module 9 — Other Languages (C/C++, Go, Haskell, Java/Scala, JavaScript)"
tags: [cpp, go, golang, haskell, java, scala, javascript, functional-programming, learning-resources]
last_updated: "2026-08-24"
confidence: "high"
source: "https://github.com/niderhoff/knowledge-repository#others"
---

## For future agent
Multi-language resource catalog from the knowledge repo. Each section is a self-contained mini-path: one canonical book + exercises + one deep-dive. Use when picking up a new language or finding the canonical text for one you know. JS section is the deepest (core-mechanics books).

# C/C++

### Learning the Language
- **[The C Programming Language (K&R)](https://www.amazon.com/Programming-Language-2nd-Brian-Kernighan/dp/0131103628)** — the classic; still the reference
- [Learn C the Hard Way](https://learncodethehardway.org/c/)
- [Modern C (Gustedt)](https://modernc.gforge.inria.fr/) — free, standards-tracked
- Quick tours: [C in Y minutes](https://learnxinyminutes.com/docs/c/) · [C++ in Y minutes](https://learnxinyminutes.com/docs/c++/)
- Video: [Learn C++ by Building a Crossword Puzzle (YouTube series)](https://www.youtube.com/playlist?list=PLg4AoophFZWZ7Llifowo-1WGMVICq-mfw)

### Ecosystem
- Algorithms in C++: [priyankchheda/algorithms](https://github.com/priyankchheda/algorithms)
- Testing: [GoogleTest](https://github.com/google/googletest/)
- Jupyter kernel: [xeus-cling](https://github.com/jupyter-xeus/xeus-cling)
- Safety-critical practices: [awesome-safety-critical](https://github.com/stanislaw/awesome-safety-critical/blob/master/README.md#coding-guidelines)
- Vault link: [[modules/ai-ml/matching-engine-cpp]] · [[modules/SPM/c-programming-master-study-guide|SPM C module]]

# Go

- **[Practical Go Lessons](https://www.practical-go-lessons.com/)** — in-depth free book covering Go + CS basics
- [The ecosystem of Go (henvic)](https://henvic.dev/posts/go/) — full orientation map
- Project-based: **[Learn Go by porting a web backend from Python (benhoyt)](http://benhoyt.com/writings/learning-go/)**
- Test-driven: **[Learn Go with Tests](https://quii.gitbook.io/learn-go-with-tests/)** — TDD as the teaching vehicle
- Reference: **[Go by Example](https://gobyexample.com/** · [Using Go modules (official)](https://blog.golang.org/using-go-modules)
- Practice: [1000+ hand-crafted examples & quizzes (learngo)](https://github.com/inancgumus/learngo)
- Craft essay: [How I write Go HTTP services after seven years](http://archive.today/G0JDY)

# Haskell

- **[Learn You a Haskell for Great Good](http://learnyouahaskell.com/**) — the friendly classic
- **[Write Yourself a Scheme in 48 Hours](https://en.wikibooks.org/wiki/Write_Yourself_a_Scheme_in_48_Hours)** — learn-by-building-an-interpreter
- **[Graham Hutton's lectures (YouTube)](https://www.youtube.com/channel/UCBDp7ydYTHi1dh4Gnf3VTPA)** · [Nottingham course page](http://www.cs.nott.ac.uk/~pszgmh/) — from the *Programming in Haskell* author

# Java / Scala

- [Awesome Java](https://github.com/akullpp/awesome-java) — everything catalog
- **[Helsinki MOOC Object-Oriented Programming with Java](http://mooc.fi/courses/2013/programming-part-1/)** — the recommended structured course
- Jackson JSON library:
  - [Swagger & polymorphic type handling](http://yysource.com/2016/05/swagger-and-polymorphic-type-handling-with-jackson/)
  - [Polymorphic serialization/deserialization example (SO)](https://stackoverflow.com/questions/17135166/looking-for-a-good-example-of-polymorphic-serialization-deserialization-using-ja/26720380#26720380)

# JavaScript (deepest section)

## Learn (canonical order)
1. **[Eloquent JavaScript](https://eloquentjavascript.net/)** — the recommended book (free online, interactive)
2. [JavaScript for Impatient Programmers (ES2020, Dr. Axel)](https://exploringjs.com/impatient-js/)
3. **[You Don't Know JS (getify)](https://github.com/getify/You-Dont-Know-JS)** — core mechanisms deep-dive series (free)
4. [Exploring JS (Dr. Axel's book site)](https://exploringjs.com)
5. Spec: [ECMAScript 2020 Language Specification](https://www.ecma-international.org/publications/standards/Ecma-262.htm)

## Beyond Basics
- **[Build Your Own React (pomb.us)](https://pomb.us/build-your-own-react/**)** — build a React clone from scratch; best way to actually understand React
- **[Mostly Adequate Guide to FP](https://mostly-adequate.gitbook.io/mostly-adequate-guide/)** — functional programming in JS
- Trends: [State of JS survey](https://stateofjs.com/) — 20k+ developers' tool usage data
- Algorithms: [javascript-algorithms (trekhleb)](https://github.com/trekhleb/javascript-algorithms)
- d3.js: [Hitchhiker's Guide to d3.js](https://medium.com/@enjalot/the-hitchhikers-guide-to-d3-js-a8552174733a)

Vault link: [[modules/programming/cs50/week-8-html-css-javascript|CS50 Week 8]] — first contact; this section extends it.

## Related Pages

- [[modules/programming/overview|Programming Hub]] · [[software-dev-general]] · [[languages-python-advanced]] · [[language-rust]]
- [[web-development-resources]] — the frontend layer above JS
- [[modules/object-oriented-programming/design-principles-solid|SOLID principles]] — language-agnostic design