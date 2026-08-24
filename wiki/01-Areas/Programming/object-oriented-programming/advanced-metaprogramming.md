---
module: "object-oriented-programming"
topic: "Advanced OOP & Metaprogramming — __new__, Metaclasses, Attribute Lookup, Introspection"
tags: [oop, python, metaclasses, new, metaprogramming, introspection, type, lookup-chain, advanced]
last_updated: "2026-08-15"
---

# Advanced OOP & Metaprogramming — the Engine Room

> Classes are objects. Classes are created by other classes (metaclasses). Attribute access is a protocol you can intercept. This page explains **how Python's machinery actually works** — mostly for *understanding*, because "metaclasses are deeper magic than 99% of users should ever worry about." (Tim Peters)
> Sources: [Python Data Model](https://docs.python.org/3/reference/datamodel.html), [Real Python — Metaclasses](https://realpython.com/python-metaclasses/), [Real Python — Descriptors](https://realpython.com/python-descriptors/).

---

## 1. The Big Picture: everything is an object; classes are objects too

```
object   (root class of the class hierarchy)
   │  instances: everything except classes
   ▼
   │  instances of ─────────────────────┐
   ▼                                    ▼
instances (d1, d2)   ┌──────────────── type (the metaclass)
                     │ instances: every class
                     ▼
                  class Dog
                     │ instances
                     ▼
                    d1, d2
```

- `type(1)` → `int`; `type(int)` → `type`. **`type` is the metaclass of most classes.**
- A **metaclass** = "a class of a class" = a factory for classes (like a class is a factory for objects).

```python
type(object)        # type
type(type)          # type   (type is its own metaclass)
Dog.__class__       # type
isinstance(Dog, type)  # True — classes are instances of type
```

---

## 2. `__new__` vs `__init__` — the two-step birth of an object

| Step | Method | Returns | Typical use |
|---|---|---|---|
| 1. create | `__new__(cls, ...)` | the (empty) object | immutable types, singletons, subclassing built-ins |
| 2. initialize | `__init__(self, ...)` | `None` | set up instance state |

`Dog("Miles")` ⇒ `Dog.__new__(Dog, "Miles")` → empty object → `Dog.__init__(obj, "Miles")` → returned to you.

**`__new__` is a classmethod** (even without decorator) and is called **before** `__init__`.

```python
class ImmutablePoint(tuple):
    def __new__(cls, x, y):
        return super().__new__(cls, (x, y))   # tuple.__new__ builds it

    def __init__(self, x, y):                 # cannot set attrs — it's a tuple
        pass

ImmutablePoint(1, 2)   # (1, 2)  — works, immutable
```

**Singleton via `__new__`** (the class-based version; usually a module is better — see [[design-patterns]] §3.1):
```python
class Logger:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

**Rule of thumb:** define `__new__` only when the object's *type* must be customized (immutables, singletons, subclassing built-ins). For everything else, `__init__` suffices.

---

## 3. The Attribute Lookup Chain (the complete picture)

When you read `obj.attr` — this is what `object.__getattribute__` does:

```
obj.attr
  1. data descriptor named 'attr' on type(obj) or its MRO?  → __get__(obj, type)
  2. 'attr' in obj.__dict__?                                 → return value
  3. non-data descriptor 'attr' on type/MRO?                 → __get__(obj, type)
  4. plain class attribute on type/MRO?                      → return it
  5. obj.__getattr__('attr') defined?                        → call it
  6. raise AttributeError
```

```python
class Descriptor:
    def __get__(self, obj, objtype=None): return "descriptor value"
class C:
    d = Descriptor()     # non-data descriptor
c = C(); c.d             # "descriptor value"   (step 3)
c.d = 1; c.d             # 1  (step 2 — instance __dict__ wins over NON-data descriptor)
```

**Data descriptor wins over `__dict__`** (step 1 beats step 2) — that's why `@property` can't be shadowed by instance assignment but a method can. *(Full diagram: [[properties-and-descriptors]] §3.)*

**Customizing access:**
- `__getattr__` — fallback hook, fires only when normal lookup fails (great for lazy proxies, virtual attributes).
- `__getattribute__` — fires on *every* access (dangerous; recursion risk).
- `__setattr__` / `__delattr__` — intercept writes/deletes (frozen dataclasses use this).

```python
class LazyDict:
    def __init__(self, d): object.__setattr__(self, "_d", d)
    def __getattr__(self, name):          # only called when _d lookup fails
        if name in self._d: return self._d[name]
        raise AttributeError(name)
    def __setattr__(self, name, value):
        if name == "_d": object.__setattr__(self, name, value)
        else: self._d[name] = value
```

---

## 4. Metaclasses — classes that build classes

`class C(Base, metaclass=Meta):` tells Python: *"when creating the class object C, use Meta's machinery, not type's."*

```python
class Meta(type):                       # Meta IS-A type → it's a metaclass
    def __new__(mcs, name, bases, namespace):
        namespace["created_by"] = "Meta"
        return super().__new__(mcs, name, bases, namespace)

    def __call__(cls, *args, **kwargs): # intercepts "cls(...)" → instantiation
        print(f"creating {cls.__name__}")
        return super().__call__(*args, **kwargs)

class Foo(metaclass=Meta): ...
Foo.created_by          # "Meta"  (injected at class-creation time)
Foo()                   # prints "creating Foo"
```

**What `type(name, bases, namespace)` is:** the same thing, called directly — classes created dynamically:
```python
Dynamic = type("Dynamic", (Base,), {"attr": 42})
```

**When metaclasses are (rarely) worth it:**
- Class-level registries (auto-register subclasses).
- Enforcing conventions (validate method names, forbid attributes).
- Modifying the namespace at class-creation time (like `@dataclass` does — dataclass uses the decorator, not a metaclass).

**When they're not:** almost always. "If it isn't pretty obvious that a problem calls for them, then it will probably be cleaner and more readable if solved in a simpler way." (Tim Peters)

```python
# Registry via metaclass — the classic justified use
class RegistryMeta(type):
    _registry = {}
    def __new__(mcs, name, bases, ns):
        cls = super().__new__(mcs, name, bases, ns)
        if getattr(cls, "auto_register", False):
            mcs._registry[cls.__name__] = cls
        return cls

class Plugin(metaclass=RegistryMeta):
    auto_register = True

class MyPlugin(Plugin): ...          # auto-added to RegistryMeta._registry
```

---

## 5. Descriptors power *everything* (a recap)

- **`property`** → a data descriptor (getter/setter/deleter).
- **Functions** → non-data descriptors: `obj.method` binds via `__get__` → bound method.
- **`staticmethod`/`classmethod`** → descriptors that change what's bound.
- **Your own descriptors** → reusable managed attributes ([[properties-and-descriptors]] §2).

```python
class classmethod_lite:               # how @classmethod roughly works
    def __init__(self, fn): self.fn = fn
    def __get__(self, obj, objtype=None):
        return self.fn.__get__(objtype)   # bind to the CLASS, not the instance
```

---

## 6. Introspection & utilities

| Tool | Purpose |
|---|---|
| `type(x)`, `x.__class__` | object's type |
| `isinstance(x, C)`, `issubclass(C, P)` | relationship checks |
| `C.__mro__`, `C.mro()`, `C.__bases__` | resolution order |
| `C.__dict__`, `vars(obj)`, `dir(obj)` | namespaces |
| `hasattr/getattr/setattr/delattr` | dynamic access (safe with slots) |
| `inspect.getmembers`, `inspect.signature`, `inspect.getmro` | deep inspection |
| `dataclasses.fields`, `dataclasses.asdict` | dataclass metadata |

```python
import inspect
inspect.getmro(D)                  # same as D.__mro__
inspect.signature(BankAccount)     # (owner: str, balance: int = 0)
dir(Dog)                           # all reachable attributes incl. inherited
```

---

## 7. Pitfalls

1. **Metaclass conflicts** — two bases with different metaclasses raise `TypeError` (unify with a common metaclass).
2. **`__getattribute__` recursion** — any `self.x` inside it re-enters itself; use `object.__getattribute__`.
3. **`__new__` forgetting `super().__new__(cls, ...)`** — objects never get built.
4. **Metaclass for everything** — decorators/class decorators solve most "metaclass problems" more simply.
5. **`type()` confusion** — `type(x)` (one arg, returns type) vs `type(name, bases, ns)` (three args, *creates* a class).

---

## 8. Navigation

- The machinery behind: [[oop-foundations]] §2-5 · [[properties-and-descriptors]] §2-3
- Dunder reference: [[magic-methods-dunder]] · dataclass implementation notes: [[modern-oop-dataclasses-typing]]
- Reference: [[cheatsheet]] · back to [[overview]]
