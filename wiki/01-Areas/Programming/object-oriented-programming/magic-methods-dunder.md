---
module: "object-oriented-programming"
topic: "Dunder / Magic Methods — Complete Reference for Python Special Methods"
tags: [oop, python, dunder, magic-methods, special-methods, protocols, operator-overloading, reference]
last_updated: "2026-08-15"
---

# Dunder (Magic) Methods — Complete Reference

> Dunder = **d**ouble **under**score: methods like `__init__`, `__str__`, `__eq__`. Python calls them **automatically in response to operations** — `str(x)` triggers `x.__str__()`, `x == y` triggers `x.__eq__(y)`. Implementing dunders is how your objects *speak Python fluently*.
> Source: [Python Data Model](https://docs.python.org/3/reference/datamodel.html), [Real Python Magic Methods](https://realpython.com/python-magic-methods/).

---

## 1. The Core Insight

Every operator and built-in is sugar for a special method call:

```
x + y        →  type(x).__add__(x, y)
str(x)       →  type(x).__str__(x)
repr(x)      →  type(x).__repr__(x)
len(x)       →  type(x).__len__(x)
x[i]         →  type(x).__getitem__(x, i)
x == y       →  type(x).__eq__(x, y)
for v in x:  →  type(x).__iter__(x)  then __next__
with x:      →  __enter__(x) / __exit__(x, exc_type, exc, tb)
x(args)      →  type(x).__call__(x, args)
```

**Golden rule:** these are looked up on the **type**, not the instance (so `__slots__` classes, frozen dataclasses, and even `__getattr__`-hiding all still honor them).

---

## 2. The "Big 5" you'll implement every day

```python
class BankAccount:
    def __init__(self, owner, balance=0):          # 1. initialization
        self.owner = owner
        self.balance = balance

    def __repr__(self):                            # 2. unambiguous, dev-facing
        return f"BankAccount({self.owner!r}, {self.balance!r})"

    def __str__(self):                             # 3. readable, user-facing
        return f"Account of {self.owner}: ${self.balance}"

    def __eq__(self, other):                       # 4. value equality
        if isinstance(other, BankAccount):
            return (self.owner, self.balance) == (other.owner, other.balance)
        return NotImplemented

    def __hash__(self):                            # 5. usable as dict key / in set
        return hash((self.owner, self.balance))
```

**`__repr__` vs `__str__`:** `repr()`/`!r` should be *unambiguous* (ideally round-trippable code); `str()`/`print()` should be *pretty*. If you implement only one, do `__repr__` — `str()` falls back to it.

**`__eq__` + `__hash__` law:** defining `__eq__` sets `__hash__` to `None` (unhashable) *unless* you define `__hash__` too. Mutable objects shouldn't be hashable anyway. Dataclasses handle all this automatically ([[modern-oop-dataclasses-typing]]).

---

## 3. Full Reference Table (by category)

### A. Object lifecycle

| Method | Trigger | Purpose |
|---|---|---|
| `__new__(cls, ...)` | `Cls(...)` | create the raw object (first step) |
| `__init__(self, ...)` | `Cls(...)` | initialize the object (second step) |
| `__del__(self)` | GC collects object | finalize (rarely reliable — avoid) |

### B. Representation & formatting

| Method | Trigger | Purpose |
|---|---|---|
| `__repr__(self)` | `repr(x)`, `!r` | unambiguous representation |
| `__str__(self)` | `str(x)`, `print(x)` | pretty representation (falls back to `__repr__`) |
| `__bytes__(self)` | `bytes(x)` | byte representation |
| `__format__(self, spec)` | `f"{x:spec}"` | custom format spec |

### C. Comparison & ordering

| Method | Trigger |
|---|---|
| `__eq__` | `==` |
| `__ne__` | `!=` (defaults to `not __eq__`) |
| `__lt__` / `__le__` | `<` / `<=` |
| `__gt__` / `__ge__` | `>` / `>=` |

`functools.total_ordering` fills in the missing ones from `__eq__` + one ordering method.

### D. Arithmetic (binary operators)

| Method | Trigger | Method | Trigger |
|---|---|---|---|
| `__add__` / `__radd__` | `+` / `+` (reflected) | `__mul__` / `__rmul__` | `*` |
| `__sub__` | `-` | `__truediv__` | `/` |
| `__floordiv__` | `//` | `__mod__` | `%` |
| `__pow__` | `**` | `__matmul__` | `@` |
| `__neg__`/`__pos__`/`__abs__` | unary `-`,`+`,`abs()` | `__round__` | `round()` |

**Reflected (r) methods:** when `x + y` fails (`x.__add__` returns `NotImplemented`), Python tries `y.__radd__(x)`. Return `NotImplemented` to hand off gracefully.

### E. Containers & sequences

| Method | Purpose |
|---|---|
| `__len__` | `len(x)` — enables `bool(x)` fallback too |
| `__getitem__(self, key)` | `x[key]`, slices, iteration fallback |
| `__setitem__` / `__delitem__` | `x[key] = v` / `del x[key]` |
| `__contains__` | `v in x` |
| `__iter__` / `__next__` | `for`, `iter()`, `next()` |
| `__reversed__` | `reversed(x)` |

```python
class Range2D:
    def __init__(self, lo, hi):
        self._vals = list(range(lo, hi))
    def __len__(self): return len(self._vals)
    def __getitem__(self, i): return self._vals[i]
    def __contains__(self, v): return v in self._vals
    def __iter__(self): return iter(self._vals)
```

### F. Callable & context managers

| Method | Purpose |
|---|---|
| `__call__(self, *a, **k)` | make instances callable: `x(...)` |
| `__enter__(self)` / `__exit__(self, exc_type, exc, tb)` | `with x:` — setup/teardown |

```python
class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - self.start
        return False                 # False → propagate exceptions

with Timer() as t:
    do_work()
print(t.elapsed)
```

### G. Attribute access (advanced)

| Method | Purpose |
|---|---|
| `__getattr__(self, name)` | called **only when** normal lookup fails |
| `__getattribute__(self, name)` | called for **every** attribute access |
| `__setattr__` / `__delattr__` | intercept writes/deletes |
| `__dir__` | customize `dir(x)` |

*(Descriptors — `__get__`/`__set__`/`__delete__`/`__set_name__` — are their own page: [[properties-and-descriptors]].)*

### H. `__slots__` (memory optimization)

`__slots__` tells Python the exact attribute names → no per-instance `__dict__` → ~30–50% less memory + faster access. Trade-off: no dynamic attributes, no weakrefs by default. *(Details: [[properties-and-descriptors]] §4.)*

```python
class Point:
    __slots__ = ("x", "y")
    def __init__(self, x, y): self.x, self.y = x, y

p = Point(1, 2)
p.z = 3   # AttributeError: 'Point' object has no attribute 'z'
```

---

## 4. Protocols (bundles of dunders)

A **protocol** is a family of special methods that unlock a language feature. The Big Three:

| Protocol | Requires | Unlocks |
|---|---|---|
| **Iterable/Iterator** | `__iter__` (+ `__next__`) | `for`, unpacking, `in`, `sum()`, `sorted()` |
| **Context manager** | `__enter__` + `__exit__` | `with` |
| **Descriptor** | `__get__` (+`__set__`/`__delete__`) | managed attributes, properties, methods |

Plus: Sequence (`__getitem__`+`__len__`), Mapping, Number, Callable (`__call__`).

---

## 5. Idioms Worth Knowing

```python
# 1. Return NotImplemented to let the other operand try (reflected ops)
class Money:
    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.amount + other.amount)
        return NotImplemented          # → Python tries other.__radd__

# 2. __bool__: empty = falsy, like containers
class ShoppingCart:
    def __bool__(self):
        return bool(self.items)        # then `if cart:` works naturally

# 3. f-string formatting via __format__
class Money:
    def __format__(self, spec):
        return f"${self.amount:{spec}}"

f"{Money(12.345):.2f}"   # "$12.35"

# 4. __iter__ as generator → one method, both __iter__ and __next__
class Countdown:
    def __init__(self, n): self.n = n
    def __iter__(self):
        while self.n > 0:
            yield self.n
            self.n -= 1
```

---

## 6. Pitfalls

1. **`__eq__` without `__hash__`** → objects become unhashable silently.
2. **`__init__` and `__new__` confusion** — `__init__` is for state, not allocation.
3. **`__getattr__` vs `__getattribute__`** — one fires only on failure; the other always. Confusing them causes infinite recursion.
4. **Returning `None` from `__eq__`/`__lt__`** — comparisons must return `bool` (or `NotImplemented`).
5. **Mutating `self` inside `__hash__`** — catastrophic (object changes hash while in a dict).
6. **`__del__` guarantees** — don't rely on it; use context managers / `finally` for cleanup.
7. **Infinite recursion with `__setattr__`** — use `object.__setattr__(self, ...)` inside it.

---

## 7. Navigation

- Operator overloading context: [[polymorphism]] §4 · lifecycle in [[advanced-metaprogramming]] §2
- Managed attributes: [[properties-and-descriptors]] · automatic dunders: [[modern-oop-dataclasses-typing]]
- Quick-reference version: [[cheatsheet]] · back to [[overview]]
