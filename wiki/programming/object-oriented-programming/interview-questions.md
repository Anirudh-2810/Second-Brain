---
module: "object-oriented-programming"
topic: "OOP Python — Interview Questions & Answers (curated Q&A bank)"
tags: [oop, python, interview, questions, answers, qa, job-prep, revision]
last_updated: "2026-08-15"
---

# Object-Oriented Python — Interview Q&A Bank

> Curated questions with crisp answers + a code snippet each. Use the reveal-style format: answer first, code second. Answers link back to the node pages for depth.
> Scope: fundamentals → inheritance internals → dunders → design → modern Python.

---

## Level 1 — Fundamentals

**Q1. What is OOP, and how does Python support it?**
OOP is a programming paradigm that structures programs by bundling related data (attributes) and behaviors (methods) into objects. Python is multiparadigm and supports OOP via the `class` keyword with minimal ceremony: classes are objects, all methods are virtually dispatched, and there is no enforced privacy. ([[overview]] §1)

**Q2. Class vs object vs instance — define each.**
A class is a blueprint + a type + a namespace. An object is a thing created from a blueprint; an instance is an object of a specific class. `Dog` is the class; `d = Dog("Miles")` creates an instance. ([[oop-foundations]] §1)

**Q3. What is `self`? Why is it explicit in Python?**
`self` is the instance, passed explicitly as the first parameter of instance methods (by convention). `x.f()` ≡ `C.f(x)` — Python inserts the instance when you use dot-notation. It's explicit because Python is "explicit is better than implicit." ([[oop-foundations]] §4)

**Q4. Class attributes vs instance attributes.**
Class attributes are declared in the class body and shared by all instances (looked up on the class). Instance attributes are set via `self.x = ...` and live in each object's `__dict__`. Reading checks instance first, then the class. ([[oop-foundations]] §5)

**Q5. What is `__init__`, and is it a constructor?**
`__init__` is the *initializer* — it sets instance state. The *constructor* is `__new__`, which creates the object. `__new__` → `__init__` → object. You virtually always write only `__init__`. ([[advanced-metaprogramming]] §2)

**Q6. `@classmethod` vs `@staticmethod` vs instance method.**
Instance methods get `self`; class methods get `cls` (use for alternative constructors, respect subclasses); static methods get neither (utility functions). ([[oop-foundations]] §6)

**Q7. How is privacy handled in Python?**
By convention: `name` public, `_name` "protected" (internal), `__name` name-mangled to `_ClassName__name` (mainly to avoid accidental overrides). Nothing is enforced — "Python trusts you." ([[the-four-pillars]] §2)

**Q8. What is `__dict__`?**
A dict storing an object's writable attributes; also the class namespace (as a mappingproxy). `vars(obj)` returns it. Instances with `__slots__` don't have one. ([[oop-foundations]] §5, [[properties-and-descriptors]] §4)

---

## Level 2 — Inheritance

**Q9. What is MRO, and how is it computed?**
Method Resolution Order = the linear order used for attribute lookup and `super()`. It preserves base-class left-to-right order, visits each ancestor once, and is monotonic (C3 linearization). Check with `Class.__mro__`. ([[inheritance]] §4)

**Q10. The diamond problem — how does Python solve it?**
With multiple inheritance, a class may reach one ancestor via several paths. Python's MRO linearization visits each ancestor exactly once, so cooperative `super()` chains run each `__init__` once (`D → B → C → A → object`). ([[inheritance]] §4)

**Q11. What does `super()` actually do?**
It returns a proxy that delegates lookups to the *next class in the MRO* — not literally "the parent." That's why it works in diamonds. Use keyword args in `__init__` chains. ([[inheritance]] §3)

**Q12. When should I use multiple inheritance?**
For **mixins** — small, single-responsibility classes adding one capability (logging, JSON, permissions). Otherwise prefer composition. ([[inheritance]] §5)

**Q13. ABC vs Protocol.**
ABCs (`abc.ABC` + `@abstractmethod`) define contracts that must be inherited and are enforced at runtime instantiation. Protocols (`typing.Protocol`) are structural — any class with the right methods satisfies them; enforced by type checkers. ([[inheritance]] §7, [[polymorphism]] §5)

**Q14. Overriding vs overloading in Python.**
Overriding = child redefines a parent method (supported, natural; all methods virtual). Overloading = same name, different signatures — Python doesn't support it; use defaults, `*args`, `isinstance` dispatch, or `functools.singledispatch`. ([[inheritance]] §6)

**Q15. Inheritance vs composition — how do you choose?**
Inheritance for a true **is-a** relationship + genuine implementation reuse (but keep shallow). Composition for **has-a** or just needing behavior — it's loosely coupled and swappable. Interface-only needs → Protocol/ABC. ([[design-principles-solid]] §7)

---

## Level 3 — Dunders & protocols

**Q16. What are dunder methods? Name the most important five.**
Special methods auto-invoked by operators/built-ins. Big five: `__init__`, `__repr__`, `__str__`, `__eq__`(+`__hash__`), `__len__`. Others: `__iter__`/`__next__`, `__call__`, `__enter__`/`__exit__`, `__getitem__`, arithmetic ops. ([[magic-methods-dunder]])

**Q17. `__repr__` vs `__str__`.**
`__repr__` → unambiguous, dev-facing, ideally round-trippable; `__str__` → readable, user-facing. `str(x)` falls back to `__repr__`. Use `!r` in f-strings for repr. ([[magic-methods-dunder]] §2)

**Q18. Why do `__eq__` and `__hash__` need to be consistent?**
Dicts/sets use the hash first, then equality. If two objects are equal but hash differently (or `__eq__` is defined without `__hash__`, making objects unhashable), lookups break. Define both or use `@dataclass(frozen=True)`. ([[magic-methods-dunder]] §2)

**Q19. What is a context manager? How do you implement one?**
An object with `__enter__`/`__exit__` enabling `with`. Use for resource setup/teardown. Alternatively `@contextlib.contextmanager` on a generator. ([[magic-methods-dunder]] §2)

**Q20. What is the descriptor protocol?**
`__get__`(+`__set__`/`__delete__`) on a class attribute intercepts access. Data descriptors (with `__set__`) beat instance `__dict__`; non-data descriptors lose to it. Properties, methods, `classmethod`, `staticmethod` are all descriptors. ([[properties-and-descriptors]] §2)

**Q21. What does `__slots__` do, and when is it worth it?**
Declares a fixed attribute set, removing the per-instance `__dict__` → ~30–50% less memory, faster access. Costs: no dynamic attributes, no default weakrefs, and subclasses must redeclare slots. Use for many small fixed-shape objects. ([[properties-and-descriptors]] §4)

---

## Level 4 — Design

**Q22. State SOLID in one sentence each.**
S — one reason to change. O — open for extension, closed for modification. L — subtypes substitutable for base types. I — no fat interfaces. D — depend on abstractions, not concretions. ([[design-principles-solid]])

**Q23. Give a violation of OCP and the fix.**
A `Shape.area()` full of `if kind == ...` branches → adding a shape means editing. Fix: abstract `Shape` with polymorphic `area()` per subclass; `total_area()` never changes. ([[design-principles-solid]] §3)

**Q24. What does LSP protect against? Give a classic Python violation.**
Subclasses that break the base contract. Classic: `Penguin(Bird)` whose `fly()` raises. Fix: separate `FlyingBird`/`SwimmingBird` capabilities. `Square(Rectangle)` also fails LSP. ([[design-principles-solid]] §4)

**Q25. How do you implement DIP in Python?**
High-level code depends on an abstraction (Protocol/ABC), concrete implementations are *injected* (constructor/function args). Example: `OrderService(repo: OrderRepository)` with MySQL vs InMemory repos. ([[design-principles-solid]] §6)

**Q26. How do you implement a Singleton in Python — and what's the Pythonic alternative?**
A module-level instance (modules are singletons) is the idiomatic way. Class-based: `__new__` guard or decorator. Warning: Singleton is global state; prefer dependency injection. ([[design-patterns]] §3.1)

**Q27. Implement the Strategy pattern. When would you simplify it?**
Context holds a strategy (callable/object) injected at runtime. Simplify when the strategy is stateless → just pass a function. ([[design-patterns]] §5.1)

**Q28. When is a design pattern overkill in Python?**
When a language feature already does it: functions → Strategy; dicts of classes → Factory; module → Singleton; `@decorator` → Decorator; generators → Iterator. ([[design-patterns]] §1)

---

## Level 5 — Modern Python

**Q29. What does `@dataclass` generate?**
`__init__`, `__repr__`, `__eq__` (+`__ne__`) from annotated fields; optionally `__lt__/__le__/__gt__/__ge__` (`order=True`), `__hash__` (`frozen=True`), `__slots__` (`slots=True`), `__match_args__`. ([[modern-oop-dataclasses-typing]] §1-2)

**Q30. Why `field(default_factory=list)` and not `= []`?**
A bare mutable default would be created once at class definition and shared by every instance (dataclass rejects it with `ValueError`). `default_factory` calls the callable fresh per instance. ([[modern-oop-dataclasses-typing]] §3)

**Q31. Dataclass vs NamedTuple.**
Dataclass: mutable (unless `frozen`), generated dunders, rich field config. NamedTuple: immutable, tuple-like unpacking, naturally hashable, light. Pick by whether you need mutability/custom fields. ([[modern-oop-dataclasses-typing]] §5)

**Q32. What is `Protocol`, and how is it different from an ABC?**
`Protocol` declares a structural interface — any object implementing its methods satisfies it (duck typing, checked by mypy), no inheritance required. ABC requires explicit inheritance and enforces at runtime. ([[polymorphism]] §5)

**Q33. What are metaclasses? When would you use one?**
The class of a class — a factory that customizes class creation (`class C(Base, metaclass=Meta)`). Rarely justified: auto-registries, conventions, namespace transforms. Tim Peters: "metaclasses are deeper magic than 99% of users should ever worry about." ([[advanced-metaprogramming]] §4)

**Q34. `__getattr__` vs `__getattribute__`.**
`__getattr__` fires only when normal lookup *fails* (nice for proxies/virtual attrs). `__getattribute__` fires on *every* access (dangerous, recursion-prone). ([[advanced-metaprogramming]] §3)

---

## Practice prompts (mini coding challenges)

1. Write `BankAccount` with `deposit`/`withdraw`, validation, read-only `balance`. *(Answer shape: [[oop-foundations]] §9.)*
2. Build `class Shape(ABC)` with `Circle`/`Square`; make a polymorphic `total_area(shapes)`. *([[design-principles-solid]] §3.)*
3. Model `Employee → Engineer/Manager` with `super()`; add a `LogMixin`. *([[inheritance]] §2/§5.)*
4. Make a `Money` class supporting `+`, `==`, `<`, `str`, and use it in `sorted()`. *([[polymorphism]] §4.)*
5. Write a `Timer` context manager and an iterator class. *([[magic-methods-dunder]] §2.)*
6. Convert a hand-written data class to `@dataclass(frozen=True, slots=True)` and add validation in `__post_init__`. *([[modern-oop-dataclasses-typing]] §3.)*

---

## Navigation

- Reference: [[cheatsheet]] · process maps: [[flowcharts]] · back to [[overview]]
