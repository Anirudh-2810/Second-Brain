---
course_code: "CASESTUDY"
course_name: "Open-Source Case Studies"
unit: "Case Study 11 — Riot.js + ActionScript4 [Deep R&D + Build Edition]"
tags: [javascript, frameworks, language-design, lifecycle, case-study, build-plan]
last_updated: "2026-08-24"
confidence: "high"
source: "https://github.com/riot/riot + https://github.com/adobe-research/ActionScript4"
---

## For future agent
Deep-dive on both lifecycle studies with code-level inventories (Riot's compiler+observable runtime; AS4's spec/prototype structure) and buildable versions — **micro-riot: a ~100-line component framework** (the famous build-your-own-framework exercise) and **mini-spec: a language spec + tokenizer/parser skeleton**. These builds teach how frameworks and languages WORK from the inside.

# Riot.js + ActionScript 4 — Deep R&D

## Part 1A — Riot.js Code Inventory

| Piece | Tech | Mechanism |
|-------|------|-----------|
| **Compiler** | JS | `.riot` files: HTML-ish templates with `<script>` + `style` per component → compiled into JS factory functions |
| **Runtime core** | Vanilla JS (~few KB) | `mount()`: instantiate component → build DOM from template → wire expressions |
| **Reactivity** | Observer pattern (`observable`) | Component state changes → `update()` re-evaluates bound expressions → targeted DOM patches |
| **Scoped styles** | CSS + generated attribute selectors | Per-component style isolation without shadow DOM |
| **No VDOM** | Direct DOM updates | The design thesis: bindings can patch precisely without diffing |

## Part 1B — ActionScript4 Inventory

| Piece | What Existed |
|-------|--------------|
| **Spec documents** | Language proposal: static types, modern runtime model, package system evolution beyond AS3 |
| **Prototype toolchain** | Research compiler/playground experiments under adobe-research |
| **The missing piece** | A shipped RUNTIME + browser/plugin distribution — Flash Player EOL (2020) removed the host platform entirely |

## Part 2 — Why Each Design/Decision Existed

| Decision | Rationale |
|----------|-----------|
| Riot: compiler-in-userland vs JSX-build-step | 2014 era: no-build-page simplicity was a feature; tags looked like HTML |
| Riot: observable + direct DOM | Size budget; simplicity; anti-VDOM stance ("diffing is a workaround for bad APIs") |
| Riot lost anyway | React's ecosystem (devtools, patterns, hiring pool) outweighed elegance — **ecosystem > design** is the era's verdict |
| AS4 as research-spec only | Flash platform EOL made shipping pointless; Adobe studied "what would modern AS look like" for institutional knowledge |
| Spec-driven language death | Languages need RUNTIMES + communities; specs alone are museum artifacts |

**Second-order insight**: both are answers to "what happens to good technical work when its platform/ecosystem context dies?" Riot survives as maintained niche; AS4 as pure case study.

## Part 3 — Can I Build My Own Versions?

### Version A: **micro-riot** ✅ (flagship — ~100 lines)

```
Spec (vanilla JS):
state = {count:0}
template = '<button onclick="inc">Clicked {{count}} times</button>'

1. compile(template): replace {{expr}} with data-bind spans
2. mount(el, template, state): render once; attach event listeners
   by scanning onclick= etc.
3. update(): re-render ONLY bound spans from current state
4. makeReactive(state): Proxy that calls update() on any set
Demo: counter app in <100 lines total, then a todo list
```

| Milestone | Deliverable |
|-----------|-------------|
| M1 | Template interpolation renders |
| M2 | Reactive state auto-updates DOM |
| M3 | Event binding works (counter) |
| M4 | Todo-list on your framework; README comparing to Riot/React mechanics |

### Version B: **mini-spec + parser skeleton** ✅
Write a SPEC (2 pages) for a tiny expression language (numbers, + - *, variables, let): grammar in EBNF → tokenizer (~80 lines) → recursive-descent parser producing AST printer. This is the honest way to touch "language design" without compiler-bootstrapping madness.

### Failure modes while building

| Failure | Counter |
|---------|---------|
| Framework scope explosion (routing? components? lists?) | v0.1 = interpolation + events ONLY; list rendering via manual re-call of mount |
| Parser rabbit hole | Stop at AST-printer; evaluation optional stretch |
| Comparing to React mid-build | You're learning MECHANISMS, not competing |

## Part 3.5 — R&D Extension: micro-riot Implementation + Parser Sketch

### micro-riot in ~100 lines (actual implementation shape)
```javascript
function compile(template) {
  const el = document.createElement('div'); el.innerHTML = template;
  const exprs = [];
  const walk = (node) => {
    [...node.attributes].forEach(a => {
      if (a.name.startsWith('on')) {
        const ev = a.name.slice(2), fn = a.value;
        node.removeAttribute(a.name);
        node.addEventListener(ev, e => exprScope[fn](e));
      }
    });
    [...node.childNodes].forEach(n => {
      if (n.nodeType === 3 && n.textContent.includes('{{')) {
        const expr = n.textContent.match(/{{(.+?)}}/)[1];
        exprs.push({ node: n, expr });
      } else walk(n);
    });
  };
  walk(el);
  return { el, render(state){
    window.exprScope = state;                    // demo-scope; sandbox later
    exprs.forEach(({node,expr}) =>
      node.textContent = Function('with(this)return '+expr).call(state));
  }};
}
function mount(sel, template, state) {
  const c = compile(template);
  document.querySelector(sel).append(c.el);
  const reactive = new Proxy(state, {
    set(t,k,v){ t[k]=v; c.render(reactive); return true; }
  });
  c.render(reactive); return reactive;
}
// Usage: mount('#app', '<button onclick="inc">{{count}}</button>', {count:0,
//        inc(){ this.count++ }})
```
Building this once permanently demystifies: templates, reactivity proxies, declarative events. Then read Riot/React sources comparatively.

### mini-spec parser sketch (expression language)
```
Grammar (EBNF):
  expr   := term (('+'|'-') term)*
  term   := factor (('*'|'/') factor)*
  factor := NUMBER | IDENT | '(' expr ')'
Tokenizer: regex scan -> [{type:'NUM',v:3},{type:'OP',v:'+'},...]
Parser: recursive descent per rule -> AST nodes {type,val,left,right}
Stretch: evaluator walking AST; 'let' bindings = env dict
```
This skeleton + spec page IS the deliverable — languages start exactly here.


## Part 4 — Life Integration

- micro-riot doubles as interview prep: "explain React's core loop" becomes trivial after building one
- Metrics: LOC of your framework · todo-app working on it · spec+parser committed
- Ecosystem-wisdom metrics applied forward: every future stack choice runs through activity/health checklist ([[market-analysis-tech-2026]] lens)

## Checkpoint Questions

1. In YOUR framework, where exactly does reactivity live — and what does Riot's observer share with it?
2. Why did Riot's direct-DOM thesis lose to VDOM commercially, even if partially vindicated by signals-based libs later?
3. Which platform-dependency does YOUR favorite stack have that could become its Flash moment?

## Cross-Vault Links

[[modules/case-studies/index|Field Index]] · [[web-development-resources]] · [[lr-build-your-own-x]] · [[languages-polyglot]]