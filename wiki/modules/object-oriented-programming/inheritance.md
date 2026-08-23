---
module: "object-oriented-programming"
topic: "Inheritance in Python — Single, Multiple, MRO, super(), Diamond Problem, Mixins, ABCs"
tags: [oop, python, inheritance, mro, super, multiple-inheritance, diamond, mixins, abc, abstract-base-class]
last_updated: "2026-08-15"
---

# Inheritance in Python — Deep Dive

> Inheritance is the pillar with the most Python-specific machinery: the **MRO** (method resolution order), cooperative `super()`, multiple inheritance (rare among mainstream languages), the diamond problem, and mixins. Master this page and inheritance stops being "magic."
> Sources: [Python tutorial §9.5](https://docs.python.org/3/tutorial/classes.html), [Real Python inheritance & composition](https://realpython.com/inheritance-composition-python/).

---

## 1. The Core Rule (from the official tutorial)

> "Method references are resolved as follows: the corresponding class attribute is searched, descending down the chain of base classes if necessary, and the method reference is valid if this yields a function object."

And the killer consequence for Python:

> "Because methods have no special privileges when calling other methods of the same object, a method of a base class that calls another method defined in the same base class may end up calling a method of a derived class that overrides it. (For C++ programmers: **all methods in Python are effectively virtual.**)"

```python
class Base:
    def greet(self):
        return f"hi from {self.name()}"   # self.name() dispatches dynamically!
    def name(self):
        return "Base"

class Derived(Base):
    def name(self):
        return "Derived"

Derived().greet()   # "hi from Derived"   ← Base.greet called Derived.name
```

This dynamic dispatch is what makes overriding and the Template Method pattern work.

---

## 2. Basic Single Inheritance

```python
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id, self.name = emp_id, name

    def work(self):
        return f"{self.name} works"

class Engineer(Employee):                 # Engineer IS-A Employee
    def __init__(self, emp_id, name, language):
        super().__init__(emp_id, name)    # 1) run parent init
        self.language = language          # 2) add own state

    def work(self):                       # override: extend, not replace
        return super().work() + f" on {self.language}"

    def debug(self):                      # brand-new method
        return f"{self.name} is debugging"
```

**Vocabulary:** `Employee` = parent / base / superclass; `Engineer` = child / derived / subclass.

**Checks:**
```python
isinstance(e, Engineer)  # True
isinstance(e, Employee)  # True (Engineer is-a Employee)
issubclass(Engineer, Employee)  # True
Engineer.__bases__       # (Employee,)
Engineer.__mro__         # (Engineer, Employee, object)
```

---

## 3. `super()` — cooperative delegation

`super()` returns a **proxy that delegates attribute lookups to the next class in the MRO** — it is *not* "the parent class." In single inheritance it behaves like the parent; in multiple inheritance it drives cooperative `__init__` chains.

**The design rule for constructors in a hierarchy:**
- Every class that has an `__init__` calls `super().__init__(...)`.
- Every `__init__` uses **keyword arguments**, so each class can pick what it needs from the forwarded kwargs and pass the rest up.

```python
class A:
    def __init__(self, a, **kwargs):
        super().__init__(**kwargs)   # pass everything we don't use onward
        self.a = a

class B:
    def __init__(self, b, **kwargs):
        super().__init__(**kwargs)
        self.b = b

class C(A, B):
    def __init__(self, a, b):
        super().__init__(a=a, b=b)   # super() walks A → B → object

c = C(1, 2); c.a, c.b   # (1, 2)
```

**Why not `Parent.__init__(self, ...)`?** Hard-coding the parent name breaks under multiple inheritance and renames. `super()` follows the MRO automatically.

---

## 4. The MRO and the Diamond Problem

**MRO** = the linear order Python uses to resolve attribute lookups and `super()` chains. Compute it with `ClassName.mro()` or `ClassName.__mro__`.

**Rules** (from the tutorial): the MRO algorithm
1. preserves the left-to-right order of base classes as written,
2. calls each parent only once,
3. is **monotonic** (subclassing never reorders a parent's precedence).

```python
class A:  pass
class B(A): pass
class C(A): pass
class D(B, C): pass

D.__mro__   # D → B → C → A → object
```

```
            A
           / \
          B   C
           \ /
            D        diamond: A reachable two ways → visited once
```

**Diamond problem:** `A` is an ancestor via both `B` and `C`. Naive inheritance would call `A.__init__` twice. The MRO linearization *guarantees each ancestor runs exactly once*, and `super()` walks that single linear chain — this is why cooperative `super()` matters.

```python
class A:
    def __init__(self):
        print("A"); super().__init__()
class B(A):
    def __init__(self):
        print("B"); super().__init__()
class C(A):
    def __init__(self):
        print("C"); super().__init__()
class D(B, C):
    def __init__(self):
        print("D"); super().__init__()

D()   # prints D B C A  — exactly once each, following D→B→C→A→object
```

**MRO debugging tools:** `D.mro()`, `D.__mro__`, `D.__bases__`, `inspect.getmro(D)`.

---

## 5. Multiple Inheritance — when it's a good idea

Python is *"one of the few modern programming languages that supports multiple inheritance"* (Real Python). Use it for **mixins** — small, focused classes that contribute a single capability:

```python
class LogMixin:
    def log(self, msg):
        print(f"[{type(self).__name__}] {msg}")

class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class Task(LogMixin, JsonMixin):
    def __init__(self, title):
        self.title = title
        self.log("task created")

t = Task("ship feature")
t.to_json()      # '{"title": "ship feature"}'
```

**Mixins as flags of good design:** each mixin has exactly one responsibility, adds no `__init__` state (or uses cooperative `super()`), and reads only through `self`/`type(self)`. See [[design-principles-solid]] (SRP, ISP) — mixins are the multiple-inheritance embodiment of those principles.

---

## 6. Overriding vs Overloading (Python has no overloading)

| Concept | Meaning | In Python |
|---|---|---|
| **Override** | Child redefines a parent method (same signature intent) | ✅ common, natural |
| **Overload** | Same method name, *different signatures* selected by arg types | ❌ not supported; use defaults / `*args` / `isinstance` dispatch or `functools.singledispatch` |

```python
# Pythonic "overload by type":
import functools

@functools.singledispatch
def fmt(x):
    return str(x)

@fmt.register
def _(x: int):
    return f"int:{x}"

@fmt.register
def _(x: list):
    return f"list:{len(x)}"
```

Also `@typing.overload` exists — but it's *only for type-checkers*, the runtime still uses one function.

---

## 7. Abstract Base Classes — enforcing the contract

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): ...                    # must be implemented

    @abstractmethod
    def perimeter(self): ...

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side ** 2
    # forgot perimeter() → Square stays abstract

Shape()          # TypeError: Can't instantiate abstract class Shape
Square(2).area() # 9  (perimeter still missing → error at instantiation)

Square.__abstractmethods__  # frozenset({'perimeter'})
```

- **ABCs exist to be inherited, never instantiated.**
- `ABC` can also use `@abstractmethod` together with `@classmethod`, `@staticmethod`, `@property` for richer contracts.
- **Concrete default implementations** are allowed — a subclass may override or inherit them.
- **`register()`** (virtual subclassing) lets unrelated classes be *declared* as implementing an ABC without inheriting — rarely needed; prefer `Protocol` ([[polymorphism]] §4).

**ABC vs Protocol (pick one):**

| | `abc.ABC` | `typing.Protocol` |
|---|---|---|
| Relationship | explicit inheritance | structural (duck typing) |
| Enforced at | runtime (instantiation) | mypy/static check time |
| Subclass must | inherit and implement | just implement methods |
| Use when | you own the hierarchy | you don't control the classes |

---

## 8. Inheritance vs Composition — a decision tool

> "Use inheritance to reuse an implementation; implement an interface to be reused." — Real Python

```
Need to reuse behavior between two classes?
      │
      ├─ Is it a true "is-a" relationship? (a Dog IS-A Animal)
      │     └─ YES → inheritance (but keep hierarchy shallow)
      │
      ├─ Is it "has-a"? (a Car HAS-A Engine)
      │     └─ YES → composition
      │
      └─ Do classes just need a common interface?
            └─ Protocol / ABC, not necessarily inheritance
```

| | Inheritance | Composition |
|---|---|---|
| Relation | is-a | has-a |
| Reuse | interface + implementation | implementation only |
| Coupling | tight (child depends on parent) | loose (component is a field) |
| Change cost | parent change ripples down | component change rarely affects composite |
| Flexibility | fixed at class definition | swappable at runtime |
| Multiple reuse | multiple inheritance (fragile) | unlimited, clean |

```python
# Composition: a HashtagFormatter HAS-A Strategy
class Formatter:
    def __init__(self, strategy):   # inject behavior
        self.strategy = strategy
    def format(self, text):
        return self.strategy(text)

uppercase = Formatter(lambda t: t.upper())
hashtag = Formatter(lambda t: "#" + t.replace(" ", ""))
```
*(This is the Strategy pattern — see [[design-patterns]] §6.)*

---

## 9. Inheritance Pitfalls (top 8)

1. **Deep hierarchies** — prefer flat (composition or mixins).
2. **Non-cooperative `super()`** — hard-coding `Parent.__init__(self)` in a MI diamond runs the parent twice / skips MRO.
3. **Mutable class attributes inherited and mutated** — shared list strikes again (see [[oop-foundations]] §10).
4. **`__slots__` + inheritance** — child must repeat parent's slots or it grows a `__dict__` anyway ([[properties-and-descriptors]] §4).
5. **Forgetting `super().__init__()`** → parent state missing, subtle bugs.
6. **Overriding everything** — if a child overrides 90% of a parent, the hierarchy is wrong ([[design-principles-solid]] LSP).
7. **LSP violations** — child that can't do what the parent promised (e.g. `Penguin(Bird)` raising on `fly()`). Fix with better interfaces.
8. **Name mangling surprise** — `__x` inside a class is renamed to `_ClassName__x`; inheritors can't "see" it, and `super().__x` won't reach the parent's `__x`. Use it only to avoid collisions, or use `_x`.

---

## 10. Quick-Reference Table

| Task | Code |
|---|---|
| Subclass | `class Child(Parent):` |
| Call next-in-MRO | `super().method(...)` |
| Cooperative init | `super().__init__(**kwargs)` |
| List ancestors | `Child.__mro__` / `Child.mro()` |
| Abstract contract | `from abc import ABC, abstractmethod` |
| Enforce interface (static) | `typing.Protocol` |
| Check relation | `isinstance(o, P)`, `issubclass(C, P)` |
| Multiple mixins | `class C(Mixin1, Mixin2, Base):` |

---

## 11. Navigation

- Pillars view: [[the-four-pillars]] · foundations: [[oop-foundations]]
- Related: [[polymorphism]] (overriding & protocols) · [[design-principles-solid]] (LSP, composition-vs-inheritance) · [[design-patterns]] (Template Method, Strategy, Adapter all lean on inheritance)
- Reference: [[cheatsheet]] · [[flowcharts]] · back to [[overview]]
