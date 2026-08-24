---
module: "programming"
course: "CS50x — Introduction to Computer Science"
week: 8
topic: "The Internet, HTTP & Web Front-Ends — HTML, CSS, JavaScript"
tags: [programming, computer-science, cs50, harvard, html, css, javascript, http, internet, dom, web]
last_updated: "2026-08-11"
---

# Week 8 — HTML, CSS, JavaScript

> **Goal of the week:** the Internet's *layers* (TCP/IP → DNS → HTTP), then the three web front-end languages: **HTML** (content), **CSS** (style), **JavaScript** (behavior). First taste of building real webpages.
> **PSet 8:** *Homepage* (a personal site) and *Trivia* (JavaScript interactive questions).

---

## 1. The Internet — Layers Under a Website

- **IP** addresses devices; **TCP** packages data into packets, orders, and re-sends lost ones (reliability). **DNS** translates `www.google.com` → IP (a hash-table lookup, Week 5-style).
- **HTTP** = the request/response protocol browsers speak.

```
You (browser) --GET /index.html HTTP/1.1-->  server
                  Host: www.example.com
server --HTTP/1.1 200 OK ... <html>...-->  you
```

- **Status codes:** `2xx` success · `200 OK` · `301/302` redirects · `403`/`404` forbidden/not found · `500` server error.
- `GET` (fetch, visible in URL, ~no side effects) vs `POST` (send data in the body, for mutations) — the distinction Week 9's Flask uses heavily.

---

## 2. HTML — Structure / Content Only

- Markup = **tags** wrapping content. A `<tag attribute="value">content</tag>` document is a *tree* (Malan folds pages — **DOM tree**).

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="initial-scale=1, width=device-width">
    <title>hello</title>
  </head>
  <body>
    <h1>Hello, world</h1>
    <form action="/submit" method="get">
      <input autocomplete="off" autofocus name="q" placeholder="Search">
      <button type="submit">Go</button>
    </form>
  </body>
</html>
```

- Block vs inline: `<h1..h6>`, `<p>`, `<ul>/<ol>/<li>` vs `<b>`, `<i>`, `<img>`, `<a href>`. Semantics matter for accessibility.
- **Forms** (`<form>`, `<input>`, `<button>`, `<select>`) are *the* input mechanism → they hand data to the backend (Week 9). `name=`, `action=`, `method=` are the contract.

---

## 3. CSS — Appearance / Style

- Selector → `property: value;`. Three insertion points: inline `style=`, `<style>` block, or **external** `href="styles.css"` (best — separation of concerns).
- **Selectors:** element (`p`), class (`.class`), id (`#unique`), attributes, pseudo-classes (`:hover`); specificity + the `:hover` label.

```css
body { font-family: sans-serif; }
p { color: purple; }
.highlight { background-color: yellow; }
```

- **Box model** (`margin`/`border`/`padding`/`content`), **flexbox/grid** for layout, **media queries** for responsiveness:
```css
@media (min-width: 600px)
{
    body { background-color: teal; }
}
```

---

## 4. JavaScript — Behavior / Interactivity

- JavaScript runs **in the browser** (client-side), manipulating the **DOM** — Week 5's tree structure, revisited — and letting pages react without reloading.

Variables, conditions, loops, functions — *same ideas, new syntax*:
```javascript
const name = "David";     // const (fixed) vs let (changeable)
let counter = 0;
counter++;                // hi again, Week 1
function greet(name) { return `Hello, ${name}`; }
if (counter > 0) { /* ... */ }
for (let i = 0; i < 10; i++) { /* ... */ }
```

**Events + DOM manipulation — interactivity's engine:**
```javascript
document.querySelector("#submit").addEventListener('click', function() {
    let name = document.querySelector("#name").value;
    document.querySelector("#greeting").innerHTML = `Hello, ${name}!`;
});
```
- `document.querySelector(...)` walks the DOM (that's Week 7's search, client-side).
- **_Practice note (Trivia):** buttons → click events → `innerHTML` swap = the classic interactive-quiz skeleton.

---

## 5. The Three-Language Division of Labor (don't conflate!)

| Layer | Language | Responsibility |
|---|---|---|
| Content | **HTML** | what's *on* the page |
| Style | **CSS** | how it *looks* |
| Behavior | **JavaScript** | what it *does* |

> Cross-link the big-picture lesson: **separation of concerns** (independent, single-purpose abstractions) is the identical instinct behind modules, libraries, and clean functions — see [[pkm-code-framework]] and [[programming-cs-fundamentals]] §14.

---

## 6. Vocabulary to Master

- IP · TCP · DNS · HTTP(verbs/status codes) · client/server · request/response · URL · HTML (tag/attribute/element) · DOM · form (`GET`/`POST`) · CSS (selector, property-value, box model, media query) · JS (`let/const`, functions, events, `document.querySelector`) · responsive design

## 7. Cross-Links

- [[cs50/week-7-sql]] — forms will POST to a backend that SQLifies the data.
- [[cs50/week-9-flask]] — server-side Python meets these templates next week.
- [[cs50/week-10-cybersecurity]] — trusting client input is *exactly* what Week 10's passwords/cookies harden.
- [[cs50/problem-sets]] — PSet 8 (Homepage / Trivia).
- [[winning-in-tech-art-of-winning]] — a visible homepage/PetProject is the "build visibly" play, now real.