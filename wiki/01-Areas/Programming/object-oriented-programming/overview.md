---
module: "object-oriented-programming"
topic: "Object-Oriented Programming in Python — Module Overview & Synthesis"
tags: [oop, object-oriented-programming, python, classes, overview, synthesis, meta, learning-path, design, pillars]
last_updated: "2026-08-15"
---

# Object-Oriented Programming in Python — Module Overview & Synthesis

> Everything needed about **writing, designing, and reasoning about object-oriented Python** — from the mental model of classes/objects up through the Four Pillars, inheritance internals, dunder protocols, SOLID design, GoF design patterns, modern idioms (dataclasses / typing / protocols), and the metaprogramming under the hood.
> Start here → then branch into the node pages below.

---

## 1. What Is OOP (and why Python does it differently)

**Definition.** *Object-oriented programming is a method of structuring a program by bundling related **properties** (data) and **behaviors** (operations) into individual **objects** — then letting those objects communicate.*

OOP models real-world entities as software objects: a `Car` has state (`speed`, `fuel`) and behavior (`start()`, `accelerate()`). The data and the code that operates on it live in the same box.

**Key difference from other languages** (from the official Python tutorial): *Python's class mechanism adds classes with a minimum of new syntax and semantics.* Concretely:

| Property | Python | Java / C++ |
|---|---|---|
| Everything is an object (functions, classes, modules) | ✅ | ❌ (mostly) |
| Data hiding enforced by language | ❌ — by **convention** (`_name`) | ✅ `private` keyword |
| Method visibility | All public / effectively `virtual` | `public/private/protected`, `final` |
| Multiple inheritance | ✅ native | ❌ (interfaces instead) |
| Abstraction mechanism | ABCs + duck typing + `Protocol` | `abstract class` / `interface` |
| Constructor story | `__new__` (create) + `__init__` (initialize) | constructor |
| Methods are `virtual` by default | ✅ | ❌ (need keyword) |
| Operator overloading | ✅ via dunder methods | partial (operators) |
| Formal interfaces | Optional (duck typing makes them unneeded) | Required |

**The mental frame:** a **class** is a blueprint; an **object/instance** is a thing built from the blueprint. One `Dog` class → many `Dog` instances, each with its own `name` and `age` but the same set of behaviors.

---

## 2. The Four Pillars (the whole module in one table)

| Pillar | One-liner | Python vehicle | Where in module |
|---|---|---|---|
| **Encapsulation** | Bundle data + behavior; hide internal state behind an interface | Attributes, methods, `_`/`__` convention, `@property` | [[the-four-pillars]], [[properties-and-descriptors]] |
| **Abstraction** | Hide implementation; expose only the essential interface | ABCs (`abc`), `Protocol`, duck typing | [[the-four-pillars]], [[inheritance]] |
| **Inheritance** | Define a hierarchy; child classes reuse & override parent behavior | `class Child(Base)`, `super()`, MRO | [[inheritance]] |
| **Polymorphism** | Different types, same interface — interchangeable objects | Method overriding, duck typing, operator overloading | [[polymorphism]] |

```
        ┌────────────────────────────────────────────────────┐
        │              OBJECT-ORIENTED PYTHON               │
        └────────────────────────────────────────────────────┘
        │            │              │              │
   [Encapsulation] [Abstraction] [Inheritance] [Polymorphism]
        │            │              │              │
    data + method  hide details  is-a reuse     same call,
    under one roof (interface)   + override     many behaviors
```

---

## 3. Concept Map (Obsidian graph)

```
                          [[overview]]  ← YOU ARE HERE
                                │
          ┌───────────┬─────────┴──────────┬────────────┐
          ▼           ▼                    ▼            ▼
   [[oop-foundations]]   [[the-four-pillars]]   [[cheatsheet]]   [[flowcharts]]
    class · object ·      4 pillars as a        one-page          design &
    self · __init__       single system         reference         class flows
          │                    │
          ├──────────┬─────────┼──────────┬──────────────────┐
          ▼          ▼         ▼          ▼                  ▼
   [[inheritance]]  [[polymorphism]]  [[magic-methods-dunder]]  [[properties-and-descriptors]]
    MRO · super()   duck typing ·     __init__/__str__/__eq__   @property · descriptor
    multiple ·      overriding ·      operator overloading     protocol · __slots__
    mixins          protocols                                   │
          │                    │                                 ▼
          ▼                    ▼                          [[advanced-metaprogramming]]
   [[design-principles-solid]]  [[design-patterns]]        metaclasses · __new__ ·
    SRP/OCP/LSP/ISP/DIP        Singleton · Factory ·      introspection
    composition-over-inher.    Strategy · Observer ...
          │
          ▼
   [[modern-oop-dataclasses-typing]]
    @dataclass · Protocol · NamedTuple · typing
```

**Cross-module links:**
- The general CS/base syntax this module builds on: [[programming-cs-fundamentals]] and the Python week of [[programming/cs50/index|CS50x]].
- The 6-step Python fast-track that prescribes *practice* for these exact skills: [[programming/learn-python-fast-system]].
- OOP is the backbone of the quant modules' Python: [[01-Areas/Business/quant-finance/quant-toolkit-and-skills]], [[ai-ml/event-driven-backtesting]] (event objects, backtest engine classes).

---

## 4. Reading Order for a Newcomer

1. **[[oop-foundations]]** — build the mental model: classes, objects, `self`, `__init__`, attribute lookup. Run every snippet.
2. **[[the-four-pillars]]** — see how encapsulation/abstraction/inheritance/polymorphism hang together as one system.
3. **[[inheritance]]** — the deepest Python-specific machinery (MRO, `super()`, multiple inheritance, mixins).
4. **[[polymorphism]]** — duck typing, overriding, operator overloading, protocols.
5. **[[magic-methods-dunder]]** — the language's "API hooks" — make your objects behave like built-ins.
6. **[[properties-and-descriptors]]** — managed attributes: `@property`, descriptors, `__slots__`.
7. **[[modern-oop-dataclasses-typing]]** — how serious Python code actually writes data classes today.
8. **[[design-principles-solid]]** then **[[design-patterns]]** — design quality (the "why").
9. **[[advanced-metaprogramming]]** — the engine room (metaclasses, `__new__`), for understanding not everyday use.
10. When exam/quick-review time comes: **[[cheatsheet]]** and **[[flowcharts]]**; for interview prep: **[[interview-questions]]**.

**Reuse decision shortcut** (inheritance vs composition) is in [[design-principles-solid]] §7; the class-design workflow is in [[flowcharts]].

---

## 5. Source Registry

| Source | Type | Used for |
|---|---|---|
| [Python Docs — The Tutorial, §9 Classes](https://docs.python.org/3/tutorial/classes.html) | Official | Foundations, method objects, inheritance, private vars |
| [Python Docs — Data Model](https://docs.python.org/3/reference/datamodel.html) | Official | Dunder methods, descriptors, `__slots__`, lookup chain |
| [PEP 557 — Data Classes](https://peps.python.org/pep-0557/) + `dataclasses` docs | Official | [[modern-oop-dataclasses-typing]] |
| [Real Python — OOP in Python](https://realpython.com/python3-object-oriented-programming/) | Tutorial | Foundations, 4 pillars, instantiation |
| [Real Python — Python Classes](https://realpython.com/python-classes/) | Tutorial | Attributes vs methods, `__dict__`, descriptors, `__slots__` |
| [Real Python — Inheritance & Composition](https://realpython.com/inheritance-composition-python/) | Tutorial | is-a vs has-a, multiple inheritance, ABCs |
| [Real Python — SOLID Principles](https://realpython.com/solid-principles-python/) | Tutorial | [[design-principles-solid]] |
| [Real Python — Magic Methods](https://realpython.com/python-magic-methods/) · [Descriptors](https://realpython.com/python-descriptors/) · [Metaclasses](https://realpython.com/python-metaclasses/) · [Data Classes](https://realpython.com/python-data-classes/) | Tutorial | Deep-dive node pages |
| [Refactoring Guru — Design Patterns (Python)](https://refactoring.guru/design-patterns/python) | Reference | [[design-patterns]] |
| *Fluent Python* (L. Ramalho) · *Python Cookbook* (Beazley & Jones) | Books | Advanced idioms, metaprogramming |

---

## 6. The Golden Rules (distilled)

1. **Everything is an object** — functions, classes, modules. Understanding this unlocks Python's flexibility (classes are first-class: pass them, store them, call them).
2. **`self` is just the instance** — `x.f()` ≡ `X.f(x)`. Nothing magical.
3. **Python trusts you** — no enforced private; naming conventions (`_`, `__`) + `@property` are the discipline.
4. **Prefer composition over inheritance** — reach for inheritance only for a real **is-a** relationship + genuine code reuse.
5. **Make objects speak Python** — implement dunders so objects fit the language (iterate, compare, print, `with`, `+`, `len()`...).
6. **Design for change** — SOLID keeps classes small, open to extension, and dependent on abstractions.
7. **Use modern idioms** — `@dataclass`, `Protocol`, type hints make intent explicit without ceremony.
8. **Don't over-engineer** — classes for everything is an anti-pattern; simple data → dataclass, one-off logic → functions.

---

## 7. Module Navigation

- **Foundations:** [[oop-foundations]] · [[the-four-pillars]]
- **Deep dives:** [[inheritance]] · [[polymorphism]] · [[magic-methods-dunder]] · [[properties-and-descriptors]]
- **Design:** [[design-principles-solid]] · [[design-patterns]]
- **Modern / advanced:** [[modern-oop-dataclasses-typing]] · [[advanced-metaprogramming]]
- **Reference:** [[cheatsheet]] · [[flowcharts]] · [[interview-questions]]
- Back to the catalog: [[wiki/index]] · [[programming/overview|Programming module]]
