---
module: "object-oriented-programming"
topic: "OOP Python — Master Flowcharts (Class Design, Inheritance Decision, Dunder Selection)"
tags: [oop, python, flowchart, state-machine, design, decision-tree, class-design, reference]
last_updated: "2026-08-15"
---

# Object-Oriented Python — Master Flowcharts

> All the OOP decision procedures as diagrams (Mermaid + ASCII): how to design a class, when to inherit vs compose, which method kind to use, which dunder you need, and how to pick a pattern. Each box = an action, each diamond = a decision.
> Companion to [[cheatsheet]] (reference) and [[design-principles-solid]] (the "why").

---

## 1. The Class-Design Loop (from problem to shipped class)

```mermaid
flowchart TD
    START["Start: what real-world thing<br/>must I model?"] --> A{"Does it hold<br/>state + behavior?"}
    A -->|"Only data"| D["@dataclass + methods<br/>([[modern-oop-dataclasses-typing]])"]
    A -->|"Only behavior"| F["Function / mixin —<br/>skip the class (YAGNI)"]
    A -->|"State + behavior"| B["Write the blueprint:<br/>1) state 2) behavior 3) invariants"]
    B --> C{"Is-a relationship<br/>with existing class?"}
    C -->|yes| E["class Child(Parent) + super()<br/>([[inheritance]])"]
    C -->|no| G["Standalone class + composition<br/>([[design-principles-solid]] §7)"]
    E --> H["Protect state? → @property / _name<br/>([[properties-and-descriptors]])"]
    G --> H
    H --> I["Fit the language? → dunders<br/>repr/eq/hash/iter/with... ([[magic-methods-dunder]])"]
    I --> J["Quality gate (SOLID):<br/>SRP? OCP? LSP? ISP? DIP? ([[design-principles-solid]])"]
    J -->|"pass"| K["Ship + type-check (mypy)"]
    J -->|"fail"| B
    D --> J
    F --> J
```

**ASCII version:**
```
 real-world thing ─► data-only? ──► @dataclass ──┐
                   │ behavior-only? ─► function ─┤
                   └ state+behavior ─► blueprint ─┴─► SOLID gate ─► ship
                                          ▲              │ fail
                                          └──────────────┘ (redesign)
```

---

## 2. Inheritance vs Composition Decision Tree

```mermaid
flowchart TD
    A["Two classes need<br/>shared behavior"] --> B{"Real is-a?<br/>(Engineer IS-A Employee)"}
    B -->|yes| C{"Mostly reuse parent<br/>implementation?"}
    C -->|yes| D["INHERIT<br/>class Child(Parent)<br/>shallow, flat, super()"]
    C -->|no| E["Interface only →<br/>ABC / Protocol<br/>([[inheritance]] §7, [[polymorphism]] §5)"]
    B -->|no| F{"has-a?<br/>(Car HAS-A Engine)"}
    F -->|yes| G["COMPOSE<br/>store the object, delegate<br/>(loose coupling, swappable)"]
    F -->|no| H["Unrelated classes —<br/>duck typing suffices<br/>([[polymorphism]] §2)"]
    D --> I["Will subclasses override<br/>the contract? (LSP check)"]
    E --> I
    I -->|"break LSP"| G
    I -->|"preserve contract"| J["OK — document the hierarchy"]
```

```
   shared behavior?
   ├─ true is-a + reuse parent impl ─► INHERITANCE (shallow, super(), MRO-aware)
   ├─ interface contract only       ─► ABC or Protocol
   ├─ has-a                        ─► COMPOSITION (inject + delegate)
   └─ otherwise                    ─► duck typing ([[polymorphism]])
```

---

## 3. Which Method Kind Do I Need?

```mermaid
flowchart TD
    A["Writing a method..."] --> B{"Needs the<br/>instance?"}
    B -->|yes| C["instance method (self)<br/>read/write state"]
    B -->|no| D{"Needs the class?<br/>(polymorphic factory / class state)"}
    D -->|yes| E["@classmethod (cls)<br/>alt constructor, e.g. from_iso(...)"]
    D -->|no| F{"Touches class at all?"}
    F -->|"just a helper"| G["@staticmethod<br/>utility grouped with class"]
    F -->|"expose data w/ logic"| H["@property<br/>managed attribute"]
```

---

## 4. Which Dunder Do I Need? (behavior you want → method)

```mermaid
flowchart TD
    A["I want my object to..."] --> B["print nicely → __repr__ / __str__"]
    A --> C["compare == → __eq__ (+__hash__)<br/>orderable → __lt__.. or @total_ordering"]
    A --> D["len(x) / x[i] / for-in → __len__/__getitem__/__iter__"]
    A --> E["use with: → __enter__ / __exit__"]
    A --> F["callable x(...) → __call__"]
    A --> G["support + - * / → __add__/__radd__ ..."]
    A --> H["hidden internal → _name / __name (convention)"]
```

---

## 5. Design-Pattern Picker

```mermaid
flowchart TD
    A["Need..."] --> B["exactly one shared instance → Singleton / module-level ([[design-patterns]] §3.1)"]
    A --> C["create objects without naming classes → Factory / dict registry (§3.2)"]
    A --> D["swap algorithm at runtime → Strategy = inject callable/object (§5.1)"]
    A --> E["one change notifies many → Observer / event bus (§5.2)"]
    A --> F["fixed skeleton, subclasses fill steps → Template Method (§5.3)"]
    A --> G["behavior depends on internal state → State (§5.4)"]
    A --> H["add behavior to existing objects → Decorator @ (§4.2)"]
```

---

## 6. The OOP Learning Loop (zero → fluent)

```mermaid
flowchart TD
    S["FOUNDATIONS<br/>class, object, self, __init__<br/>([[oop-foundations]])"] --> P["PILLARS<br/>encapsulation·abstraction·<br/>inheritance·polymorphism<br/>([[the-four-pillars]])"]
    P --> D["DEEP DIVES<br/>MRO · super() · duck typing<br/>dunders · properties<br/>([[inheritance]] [[polymorphism]]<br/>[[magic-methods-dunder]]<br/>[[properties-and-descriptors]])"]
    D --> M["MODERN + DESIGN<br/>dataclasses · SOLID · patterns<br/>([[modern-oop-dataclasses-typing]]<br/>[[design-principles-solid]] [[design-patterns]])"]
    M --> A["ADVANCED<br/>metaclasses · __new__ ·<br/>lookup chain (understanding)<br/>([[advanced-metaprogramming]])"]
    A --> C["CONSOLIDATE<br/>[[cheatsheet]] · [[interview-questions]]"]
    C -->|"build real things<br/>(OOP in projects)"| P
```

---

## 7. Navigation

- Reference companion: [[cheatsheet]] · decision "why": [[design-principles-solid]] · [[design-patterns]]
- Concepts: [[oop-foundations]] · [[the-four-pillars]] · [[inheritance]] · [[polymorphism]]
- Back to [[overview]]
