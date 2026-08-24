---
module: "object-oriented-programming"
topic: "OOP Python — Master Cheat Sheet (one-page reference)"
tags: [oop, python, cheatsheet, reference, quick-reference, exam-prep, formula]
last_updated: "2026-08-15"
---

# Object-Oriented Python — Master Cheat Sheet

> The compressed, exam/CRAM version of the whole module. Deep links on every row.

---

## 1. Vocabulary

| Term | Meaning | Example |
|---|---|---|
| class | blueprint + new type + namespace | `class Dog:` |
| object/instance | thing built from the class | `d = Dog()` |
| attribute | data attached to an object | `d.name` |
| method | function belonging to an object | `d.speak()` |
| `self` | the instance, passed explicitly | `def speak(self)` |
| class attr | shared across instances | `species = "dog"` |
| instance attr | per-object state | `self.name = name` |
| instantiation | calling the class | `Dog("Miles")` |
| dunder | special method, auto-called | `__init__`, `__eq__` |

---

## 2. Class Skeleton (and what each piece is)

```python
class MyClass(Parent):                 # inheritance
    class_attr = 0                     # class attribute (shared)

    def __init__(self, arg):           # initializer (NOT constructor)
        self.attr = arg                # instance attribute

    def method(self, x):               # instance method → self
        return self.attr + x

    @classmethod
    def make(cls, arg):                # class method → cls
        return cls(arg)                # builds the RIGHT subclass

    @staticmethod
    def helper(): ...                  # static method → nothing

    @property
    def computed(self):                # read-only managed attribute
        return self._attr

    def __repr__(self):                # unambiguous (dev)
        return f"MyClass({self.attr!r})"

    def __str__(self):                 # pretty (user); falls back to __repr__
        return f"MyClass({self.attr})"

    def __eq__(self, other):           # value equality
        return isinstance(other, MyClass) and self.attr == other.attr
```

---

## 3. Method / attribute matrix

| Kind | Decorator | First arg | Can access | Use for |
|---|---|---|---|---|
| instance | — | `self` | instance + class | default behavior |
| class | `@classmethod` | `cls` | class only | alt constructors |
| static | `@staticmethod` | — | neither | utility |
| property | `@property` | `self` | instance | managed/read-only attrs |

---

## 4. The Four Pillars (one line each)

| Pillar | One-liner | Mechanism |
|---|---|---|
| Encapsulation | bundle + hide state | class, `_`/`__`, `@property` |
| Abstraction | expose what, hide how | ABC, Protocol, duck typing |
| Inheritance | is-a reuse + override | `class B(A)`, `super()`, MRO |
| Polymorphism | same interface, many forms | overriding, duck typing, dunders |

---

## 5. Inheritance cheat codes

```python
class Child(Parent): ...                        # subclass
super().__init__(**kwargs)                      # cooperative init
Child.__mro__                                   # resolution order
isinstance(x, Parent)                           # True for child instances
issubclass(Child, Parent)                       # True

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): ...
```

**MRO rules:** left-to-right as written, each parent once, monotonic. Diamond ⇒ each ancestor runs once (`D → B → C → A → object`).

**Inheritance vs composition:** true is-a → inherit; has-a / just need behavior → compose.

---

## 6. Top dunders to remember

| Dunder | Trigger | Purpose |
|---|---|---|
| `__new__` | `C(...)` | create object (rare) |
| `__init__` | `C(...)` | initialize (always) |
| `__repr__` / `__str__` | `repr()` / `str()` | representation |
| `__eq__` / `__hash__` | `==` / `hash()` | value equality + hashability |
| `__lt__` / `__le__` ... | `<` `<=` ... | ordering (or `@total_ordering`) |
| `__add__` / `__radd__` | `+` | arithmetic (reflected) |
| `__len__` / `__getitem__` | `len()` / `x[i]` | container behavior |
| `__iter__` / `__next__` | `for` | iteration |
| `__call__` | `x(...)` | callable instances |
| `__enter__` / `__exit__` | `with` | context manager |
| `__getattr__` / `__setattr__` | missing / any write | intercept access |

**`__eq__` + `__hash__`:** define `__eq__` → hash becomes `None` (unhashable). Define both, or use `@dataclass(frozen=True)`.

---

## 7. Dataclasses (modern default for data classes)

```python
from dataclasses import dataclass, field

@dataclass(frozen=True, order=True, slots=True, kw_only=True)
class User:
    name: str
    age: int = field(default=18, repr=False)
    tags: list[str] = field(default_factory=list)   # mutable default!

    def __post_init__(self):                        # validation/derived
        if self.age < 0: raise ValueError("negative age")

User(name="Ada", age=36)     # kw_only → keyword required
```

| Flag | Effect |
|---|---|
| `frozen=True` | immutable + hashable |
| `order=True` | `==`, `<`, `<=`, ... from fields |
| `slots=True` | `__slots__` (memory) |
| `kw_only=True` | keyword-only args |

Helpers: `asdict(obj)` · `astuple(obj)` · `replace(obj, field=v)` · `fields(cls)` · `is_dataclass(x)`.

**NamedTuple:** immutable, hashable, unpackable — `class Coord(NamedTuple): lat: float; lon: float`.

---

## 8. SOLID one-liners

| | Principle | Reminder |
|---|---|---|
| S | Single Responsibility | one reason to change |
| O | Open/Closed | extend by adding, not editing |
| L | Liskov Substitution | subtypes keep the contract |
| I | Interface Segregation | no fat interfaces |
| D | Dependency Inversion | depend on abstractions |

---

## 9. Pattern cheat codes (Pythonic forms)

| Pattern | Pythonic implementation |
|---|---|
| Singleton | module-level instance (`db = _DB()`) |
| Factory | `REGISTRY = {"dog": Dog}; REGISTRY[k]()` |
| Strategy | pass a callable / inject an object |
| Observer | `EventBus` with callback lists |
| Template Method | abstract hooks + concrete skeleton |
| Adapter | duck typing (any object with right methods) |
| Decorator | `@decorator` (native) |

---

## 10. Two-minute checklist before you ship a class

- [ ] Fields set once in `__init__` (or dataclass) — no mutable class attr bugs (`default_factory`).
- [ ] `__repr__` implemented; `__eq__` + `__hash__` consistent.
- [ ] State hidden behind `_`/`@property` where mutation would break invariants.
- [ ] Is-a vs has-a decided; hierarchy flat; `super()` cooperative.
- [ ] One responsibility (SRP); interface small (ISP); no hard-coded concretions (DIP).
- [ ] Dataclass used for pure data; methods kept meaningful.
- [ ] Types annotated; `Protocol`/ABC chosen deliberately.

---

## 11. Navigation

- Full reference: [[magic-methods-dunder]] · [[properties-and-descriptors]] · [[modern-oop-dataclasses-typing]]
- Concepts: [[oop-foundations]] · [[the-four-pillars]] · [[inheritance]] · [[polymorphism]]
- Design: [[design-principles-solid]] · [[design-patterns]] · advanced: [[advanced-metaprogramming]]
- Process maps: [[flowcharts]] · interview prep: [[interview-questions]] · back to [[overview]]
