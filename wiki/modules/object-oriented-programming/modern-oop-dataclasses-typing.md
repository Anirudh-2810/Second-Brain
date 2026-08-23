---
module: "object-oriented-programming"
topic: "Modern Python OOP — Dataclasses, NamedTuple, typing, Protocol, Pattern Matching"
tags: [oop, python, dataclasses, namedtuple, typing, type-hints, protocol, structural-typing, pattern-matching, modern]
last_updated: "2026-08-15"
---

# Modern Python OOP — Dataclasses, Typing, Protocols

> 2026-era Python (3.9–3.14) has erased most OOP boilerplate. **`@dataclass`** generates `__init__/__repr__/__eq__` from annotated fields; **`typing.Protocol`** gives structural interfaces; **`match`/`case`** destructures objects. This page is how *production Python* actually writes classes today.
> Sources: [PEP 557](https://peps.python.org/pep-0557/) + [`dataclasses` docs](https://docs.python.org/3/library/dataclasses.html), [Real Python — Data Classes](https://realpython.com/python-data-classes/).

---

## 1. Why dataclasses (PEP 557)

Writing a data-carrying class by hand means ~25 lines of `__init__` + `__repr__` + `__eq__` boilerplate with **zero business logic**. The `@dataclass` decorator inspects your type-annotated fields and generates those methods for you — staying in sync when you add/rename fields.

```python
from dataclasses import dataclass

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0           # default value

# ✅ __init__ generated:  InventoryItem(name, unit_price, quantity_on_hand=0)
# ✅ __repr__ generated:  InventoryItem(name='widget', unit_price=3.0, quantity_on_hand=10)
# ✅ __eq__  generated:   field-by-field equality
```

"A data class is a regular Python class. The only thing that sets it apart is that it has basic data model methods implemented for you."

---

## 2. `@dataclass` parameters (the full dial board)

| Parameter | Default | Effect |
|---|---|---|
| `init=True` | generate `__init__` | |
| `repr=True` | generate `__repr__` | |
| `eq=True` | generate `__eq__` (+`__ne__`) | |
| `order=False` | generate `__lt__/__le__/__gt__/__ge__` (requires `eq=True`) | |
| `unsafe_hash=False` | force a `__hash__` even when risky | |
| `frozen=False` | `True` → immutable instances (`FrozenInstanceError` on write) | |
| `match_args=True` | generate `__match_args__` for `match`/`case` | |
| `kw_only=False` | `True` → all fields keyword-only | |
| `slots=False` | `True` → generate `__slots__` (3.10+) | |

**Hash law (from PEP 557):** `eq=True, frozen=False` → `__hash__ = None` (unhashable). `eq=True, frozen=True` → `__hash__` auto-generated. Use `unsafe_hash=True` only when you know what you're doing.

```python
@dataclass(frozen=True, order=True, slots=True)
class Point:
    x: float
    y: float

p1, p2 = Point(1, 2), Point(1, 2)
p1 == p2          # True (eq)
p1 < Point(3, 0)  # True (order — compares like a tuple (x, y))
hash(p1)          # works (frozen → hashable)
p1.x = 5          # FrozenInstanceError
```

---

## 3. `field()` — per-field control

| Argument | Purpose |
|---|---|
| `default=` | immutable scalar default |
| `default_factory=` | zero-arg callable → **fresh** mutable default per instance |
| `init=False` | exclude from `__init__` (set in `__post_init__`) |
| `repr=False` | hide from `__repr__` (secrets, noisy fields) |
| `compare=False` | exclude from `==`/ordering |
| `hash=False` | exclude from `__hash__` |
| `metadata=` | read-only info for third-party tools |
| `kw_only=True` | keyword-only for this field (3.10+) |

**The #1 dataclass bug — mutable defaults:**
```python
@dataclass
class Bad:
    items: list = []                    # ValueError! (dataclass rejects this)

@dataclass
class Good:
    items: list = field(default_factory=list)   # fresh list per instance
```

**`__post_init__` — validation & derived fields:**
```python
@dataclass(order=True)
class PlayingCard:
    sort_index: int = field(init=False, repr=False)   # computed, hidden
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = RANKS.index(self.rank) * len(SUITS) + SUITS.index(self.suit)

@dataclass(frozen=True)
class Temperature:
    value: float
    unit: str = "C"

    def __post_init__(self):
        if self.unit not in {"C", "F", "K"}:
            object.__setattr__(self, "unit", "C")   # frozen → use object.__setattr__
```

**Module-level helpers:** `asdict(obj)` (deep dict for JSON), `astuple(obj)`, `replace(obj, **changes)` (new instance with changes — essential for frozen), `fields(cls)`, `is_dataclass(obj)`, `make_dataclass(...)`.

---

## 4. Dataclass inheritance (the gotcha)

Non-defaulted fields in a subclass cannot follow defaulted base-class fields:

```python
@dataclass
class Base:
    name: str
    meta: str = ""          # defaulted

@dataclass
class Child(Base):
    age: int                # ❌ TypeError: non-default argument after default
```

Fix: reorder, give `age` a default, or use `kw_only=True`:
```python
@dataclass
class Child(Base):
    age: int = 0            # ✅
```

---

## 5. Dataclass vs NamedTuple vs Protocol

| Tool | Immutable? | Boilerplate | Hashable | Use for |
|---|---|---|---|---|
| `@dataclass` | no (unless `frozen=True`) | low (generated) | if frozen | app models, mutable records, behavior + data |
| `NamedTuple` | ✅ | low | ✅ | small fixed records, unpacking, hashable values |
| `Protocol` | — | none (interface only) | — | structural interfaces / duck typing contracts |

```python
from typing import NamedTuple

class Coordinate(NamedTuple):
    lat: float
    lon: float

c = Coordinate(19.07, 72.87)
c.lat                      # 19.07
lat, lon = c               # unpacking works
{c: "Mumbai"}              # hashable → dict key
```

---

## 6. Type hints: the OOP contract layer

Hints document intent and let mypy/pyright catch errors — but **aren't enforced at runtime** (that's duck typing's freedom, and why Protocols exist).

```python
from typing import Protocol

class Readable(Protocol):
    def read(self, key: str) -> bytes: ...

class Cache:
    def read(self, key: str) -> bytes: ...   # structurally matches Readable

def fetch(store: Readable, key: str) -> bytes:   # any Readable works
    return store.read(key)
```

**Key `typing` vocabulary:**
- `Protocol` — structural interfaces (the modern "interface keyword")
- `TypeVar` / generics — `class Repository[T]:` (PEP 695, 3.12) for type-parameterized classes
- `Type[T]` — the class object itself (used in factories)
- `Self` — return the same subclass (`def clone(self) -> Self`)
- `@typing.overload` — declare multiple signatures for the *type checker only*
- `@final` — mark a class/method as not-for-overriding (mypy enforces)

```python
class BaseModel[T]:          # 3.12+ generic dataclass-style class
    def __init__(self, value: T): self.value = value
    def get(self) -> T: return self.value
```

---

## 7. Pattern matching over objects (3.10+)

`match`/`case` destructures *attributes* of objects, so classes plug into the syntax:

```python
@dataclass
class Point:
    x: int
    y: int

@dataclass
class Color:
    r: int
    g: int
    b: int

def describe(obj):
    match obj:
        case Point(x=0, y=0):      return "origin"
        case Point(x, y):          return f"point at ({x},{y})"
        case Color(r, g, b):       return f"rgb({r},{g},{b})"
        case _:                    return "something else"
```
Works because dataclasses generate `__match_args__` (positional) and have the right attribute names.

---

## 8. Modern class style guide (how production Python looks)

```python
from dataclasses import dataclass, field

@dataclass(slots=True, order=True)
class OrderLine:
    sku: str
    qty: int
    price: float = 0.0
    _discounts: list[str] = field(default_factory=list, repr=False, compare=False)

    @property
    def total(self) -> float:
        return self.qty * self.price * (1 - sum(map(float, self._discounts)))
```

Rules of thumb:
1. Data-only class → `@dataclass` (not hand-written dunders).
2. Behavior + data → still `@dataclass` + methods, or a regular class with `@property`.
3. Interface to implement → `Protocol` (structural) or `ABC` (inheritance-based).
4. Huge class → reconsider SRP ([[design-principles-solid]]).
5. Hot inner loops → `slots=True` for memory/CPU ([[properties-and-descriptors]] §4).

---

## 9. Navigation

- Dunders these replace/automate: [[magic-methods-dunder]] · slots & properties: [[properties-and-descriptors]]
- Structural typing in action: [[polymorphism]] §5 · design quality: [[design-principles-solid]]
- Reference: [[cheatsheet]] · back to [[overview]]
