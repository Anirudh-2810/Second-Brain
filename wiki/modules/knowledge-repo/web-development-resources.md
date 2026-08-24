---
course_code: "KNOWLEDGE-REPO"
course_name: "Knowledge Repository — Curated Learning Resources (niderhoff)"
unit: "Module 11 — Web Development"
tags: [web-development, css, ux, devtools, event-loop, frontend, learning-resources]
last_updated: "2026-08-24"
confidence: "high"
source: "https://github.com/niderhoff/knowledge-repository#web-development"
---

## For future agent
Frontend resources from the knowledge repo: browser fundamentals (event loop, DevTools), CSS architecture conventions, UX/usability references, and inspiration sources. Thin-but-curated section; pairs with the JS language books in [[languages-polyglot]].

# Web Development Resources

## Fundamentals & References
- **[MDN Web Docs](https://developer.mozilla.org/en-US/)** — THE web platform reference; start every lookup here
- **[What the Heck is the Event Loop Anyway? (Philip Roberts, JSConf)](https://www.youtube.com/watch?v=8aGhZQkoFbQ)** — the talk that makes async JS click; call stack → task queue → microtasks
- [Chrome DevTools overview](https://developer.chrome.com/devtools) + tips collection: [cool DevTools tricks (flaviocopes)](https://flaviocopes.com/chrome-devtools-tips/)
- Browser support lookup: **[caniuse.com](https://caniuse.com/)** — feature compatibility tables before using any API
- Schema sketching: [QuickDBD](https://www.quickdatabasediagrams.com/) — text-to-diagram database design
- Playground: [JSFiddle](https://jsfiddle.net/)

## CSS Architecture
| Convention | Idea | Link |
|-----------|------|------|
| **BEM** | Block-Element-Modifier naming | [smacss.com/book](https://smacss.com/book/) *(source listed BEM but linked SMACSS)* |
| **SMACSS** | Scalable Modular Architecture for CSS: base/layout/module/state/theme rules | [smacss.com/book](https://smacss.com/book/) |
| **CSS Grid** | Native layout replacing framework grids | [spec (csswg drafts)](https://drafts.csswg.org/css-grid/) |
| Grid vs Bootstrap essay | Why native grid wins for layout | [hackernoon](https://hackernoon.com/how-css-grid-beats-bootstrap-85d5881cf163) |

Modern CSS explainer from reading list: ["Modern CSS Explained for Dinosaurs"](https://medium.com/actualize-network/modern-css-explained-for-dinosaurs-5226febe3525) — CSS evolution: inline → `<style>` → frameworks → preprocessor → postprocessor → CSS-in-JS → utility classes.

Common mistakes checklist: [12 common CSS mistakes (webpagefx)](https://www.webpagefx.com/blog/web-design/12-common-css-mistakes-web-developers-make/)

## UI / Design Tools
- [Adobe Color wheel](https://color.adobe.com/create/color-wheel/) — palette construction

## UX & Usability
- [What is User Experience Design? (Smashing overview + tools)](https://www.smashingmagazine.com/2010/10/what-is-user-experience-design-overview-tools-and-resources/)
- **[Usability 101 (Nielsen Norman Group)](https://www.nngroup.com/articles/usability-101-introduction-to-usability/**)** — the authority on usability testing basics
- No-code regression testing: [Reflect](https://reflect.run/)

## Frameworks
- [Bootstrap](http://getbootstrap.com/) · [Foundation](http://foundation.zurb.com/) — the two classic component frameworks
- 2026 note `(TBC)`: Tailwind has largely displaced both in new projects; concepts still transfer

## Get Inspired
- [Dribbble](https://dribbble.com/) · [Behance](https://www.behance.net/) · [awesome-inspire (curated screenshots)](https://github.com/NoahBuscher/Inspire)

## Related Pages

- [[overview]] · [[languages-polyglot]] (JS core books) · [[software-dev-general]]
- [[modules/programming/cs50/week-8-html-css-javascript|CS50 Week 8 — HTML/CSS/JS]] — vault's first-contact notes
- [[modules/projects/algorithm101-aura|AURA project]] — React dashboard applying this layer