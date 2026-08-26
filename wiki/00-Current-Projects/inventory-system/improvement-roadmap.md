---
module: "current-projects"
topic: "StockOffline — Improvement Roadmap"
tags: [builds, inventory, roadmap, improvements, priorities, bugs, security, features]
last_updated: "2026-08-27"
confidence: "high"
source: "C:\Users\Vijaykumar\inventory-system"
description: "Priority-ordered improvement roadmap for StockOffline: P0 critical bug fixes, P1 security hardening, P2 architecture improvements, P3 feature additions. Each item has impact, effort, and specific implementation guidance."
---

# StockOffline — Improvement Roadmap

> **Source:** Deep review analysis of `C:\Users\Vijaykumar\inventory-system`
> **Related:** [[wiki/00-Current-Projects/inventory-system/deep-review-report]]
> **Priority Scale:** P0 (critical, fix now) → P1 (high, fix soon) → P2 (medium, plan) → P3 (low, backlog)

---

## For future agent
This is the **improvement roadmap** for the StockOffline inventory system — priority-ordered fixes and enhancements derived from the deep review report. P0 = critical bugs, P1 = security hardening, P2 = architecture improvements, P3 = feature additions. Cross-links: [[wiki/00-Current-Projects/inventory-system/deep-review-report]], [[wiki/00-Current-Projects/inventory-system]], [[brain/Patterns/agent-pipeline-patterns]].

---

## P0 — Critical (Fix Immediately)

### P0-1: Fix `main.py` — `logger` used before definition
**Bug:** `fail()` references `logger` but is called before `logger` is defined
**Impact:** CLI crashes with `NameError` when `INVENTORY_DB_PATH` not set
**Effort:** 5 minutes
**Fix:**
```python
# src/main.py — move logger definition to line 37 (before fail())
import logging
logger = logging.getLogger(__name__)

def fail(message):
    logger.error(message)
    print(f"Error: {message}", file=sys.stderr)
    sys.exit(1)

# ... rest of code
```

### P0-2: Fix `utils.py` — Missing type imports
**Bug:** `validate_upload()` references `Dict[str, Any]` but only `List` imported
**Impact:** `validate_upload()` crashes with `NameError` at runtime
**Effort:** 2 minutes
**Fix:**
```python
# src/utils.py line 3
from typing import List, Dict, Any  # Add Dict, Any
```

### P0-3: Fix `utils.py` — `max_size` parameter ignored
**Bug:** `validate_upload()` accepts `max_size` but uses `MAX_FILE_SIZE` constant
**Impact:** Parameter is accepted but never used
**Effort:** 2 minutes
**Fix:**
```python
# src/utils.py line 75
if len(file_data) > max_size:  # Change MAX_FILE_SIZE to max_size
```

---

## P1 — High Priority (Fix Before Production)

### P1-1: Add request body size limit
**Risk:** Attacker sends large `Content-Length` → OOM crash
**Impact:** Denial of service
**Effort:** 30 minutes
**Implementation:**
```python
# src/web/server.py — in _Handler._dispatch()
MAX_BODY_SIZE = 1 * 1024 * 1024  # 1MB

length = int(self.headers.get("Content-Length", 0))
if length > MAX_BODY_SIZE:
    self.send_error(413, "Request body too large")
    return
body = self.rfile.read(length)
```

### P1-2: Enable SQLite WAL mode
**Risk:** "database is locked" under concurrent writes
**Impact:** Intermittent failures with multiple gunicorn workers
**Effort:** 15 minutes
**Implementation:**
```python
# src/inventory_system/services/database.py — in _get_connection()
conn = sqlite3.connect(self.db_path)
conn.execute("PRAGMA journal_mode=WAL")  # Add this line
conn.execute("PRAGMA foreign_keys=ON")   # Also enable FK enforcement
return conn
```

### P1-3: Enable SQLite foreign key enforcement
**Risk:** FK constraints not enforced — orphaned transactions possible
**Impact:** Data integrity not guaranteed at database level
**Effort:** 5 minutes
**Implementation:**
```python
# Already included in P1-2 above
conn.execute("PRAGMA foreign_keys=ON")
```

### P1-4: Fix `datetime.now` to use UTC
**Risk:** Local time used — inconsistent in distributed deployments
**Impact:** Timestamps may be wrong across time zones
**Effort:** 15 minutes
**Implementation:**
```python
# src/inventory_system/models/product.py
from datetime import datetime, timezone

# Change:
created_at: datetime = field(default_factory=datetime.now)
updated_at: datetime = field(default_factory=datetime.now)

# To:
created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
```

### P1-5: Add input validation at service layer
**Risk:** Negative prices, empty names allowed through
**Impact:** Invalid data in database
**Effort:** 45 minutes
**Implementation:**
```python
# src/inventory_system/services/inventory_service.py
def _validate_product(data: dict):
    if not data.get("name"):
        raise ValueError("Product name is required")
    if data.get("unit_price", 0) < 0:
        raise ValueError("Unit price cannot be negative")
    if data.get("cost_price", 0) < 0:
        raise ValueError("Cost price cannot be negative")
    if data.get("quantity", 0) < 0:
        raise ValueError("Quantity cannot be negative")
    if data.get("reorder_level", 0) < 0:
        raise ValueError("Reorder level cannot be negative")

# Call in add_product() and update_product()
```

### P1-6: Verify payment prices against database
**Risk:** Client can manipulate `unit_price` in payment calculation
**Impact:** Revenue loss if prices are tampered
**Effort:** 1 hour
**Implementation:**
```python
# src/payments.py — in calculate_order_total()
def calculate_order_total(items, tax_rate=0.18, inventory_service=None):
    total = Decimal("0")
    for item in items:
        if inventory_service:
            # Verify price against database
            product = inventory_service.get_product(item["sku"])
            if product and product.unit_price != Decimal(str(item["unit_price"])):
                raise ValueError(f"Price mismatch for {item['sku']}")
        # ... rest of calculation
```

---

## P2 — Medium Priority (Plan for Next Sprint)

### P2-1: Add pytest + CI/CD
**Risk:** Manual test scripts, no automated testing on commit
**Impact:** Bugs slip through, no regression testing
**Effort:** 2-3 hours
**Implementation:**
1. Add `pytest` to `requirements-dev.txt`
2. Convert `run_tests.py` and `test_web.py` to pytest format
3. Add `conftest.py` with fixtures
4. Add GitHub Actions workflow:
```yaml
# .github/workflows/test.yml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"
      - run: pip install -r requirements.txt -r requirements-dev.txt
      - run: pytest --cov=src tests/
```

### P2-2: Add type checking (mypy)
**Risk:** No static type analysis
**Impact:** Type errors caught at runtime instead of compile time
**Effort:** 1-2 hours
**Implementation:**
1. Add `mypy` to `requirements-dev.txt`
2. Add `mypy.ini`:
```ini
[mypy]
python_version = 3.12
warn_return_any = True
warn_unused_configs = True
disallow_untyped_defs = True
```
3. Fix type errors iteratively

### P2-3: Add linter (ruff)
**Risk:** No code style enforcement
**Impact:** Inconsistent code style over time
**Effort:** 30 minutes
**Implementation:**
1. Add `ruff` to `requirements-dev.txt`
2. Add `ruff.toml`:
```toml
line-length = 100
target-version = "py312"
select = ["E", "F", "I", "N", "W", "UP"]
```
3. Run `ruff check --fix src/`

### P2-4: Consolidate schema into single file
**Risk:** Schema split between `database.py` and `store.py`
**Impact:** Maintenance confusion, migration complexity
**Effort:** 1 hour
**Implementation:**
1. Create `src/schema.py` with all table definitions
2. Import in both `database.py` and `store.py`
3. Single source of truth for schema

### P2-5: Add database migration system
**Risk:** Inline migrations in `_initialize_db()` — fragile
**Impact:** Schema changes could break existing databases
**Effort:** 2-3 hours
**Implementation:**
1. Add `alembic` to `requirements.txt`
2. Create initial migration from current schema
3. Future changes via `alembic revision --autogenerate`

### P2-6: Add Redis for shared state (optional)
**Risk:** In-memory rate limiting/blacklist not shared across workers
**Impact:** Rate limiting bypassed, logout incomplete
**Effort:** 3-4 hours
**Implementation:**
1. Add `redis` to `requirements.txt`
2. Create `src/redis_store.py` for rate limiting + token blacklist
3. Fall back to in-memory if Redis unavailable

---

## P3 — Low Priority (Backlog)

### P3-1: Add email service for password reset
**Risk:** Reset tokens generated but never delivered
**Impact:** Password reset unusable in production
**Effort:** 2-3 hours
**Implementation:**
1. Add `sendgrid` or `resend` to `requirements.txt`
2. Create `src/email.py` with send functions
3. Update `reset_request` handler to send email

### P3-2: Add product images
**Risk:** Products are text-only
**Impact:** Less useful for visual inventory
**Effort:** 4-6 hours
**Implementation:**
1. Add `image_data BLOB` column to products table
2. Update GUI to display images
3. Update API to accept base64 images

### P3-3: Add barcode generation
**Risk:** Relies on keyboard-emulating scanners only
**Impact:** Cannot print barcode labels
**Effort:** 2-3 hours
**Implementation:**
1. Add `python-barcode` to `requirements.txt`
2. Create `src/barcode_gen.py`
3. Add "Print Label" button to GUI

### P3-4: Add multi-device sync
**Risk:** Single database, no sync
**Impact:** Cannot use on multiple devices
**Effort:** 1-2 weeks
**Implementation:**
1. Add sync endpoint to API
2. Implement conflict resolution (last-write-wins or CRDT)
3. Add sync indicator to GUI

### P3-5: Add audit trail
**Risk:** No change history
**Impact:** Cannot track who changed what and when
**Effort:** 2-3 hours
**Implementation:**
1. Add `audit_log` table: id, user_id, action, entity_type, entity_id, old_value, new_value, timestamp
2. Update service layer to log all mutations
3. Add audit report to API/GUI

### P3-6: Add i18n (internationalization)
**Risk:** English only
**Impact:** Limited market reach
**Effort:** 1-2 weeks
**Implementation:**
1. Add `gettext` support
2. Extract all user-facing strings
3. Create translation files for Hindi, Marathi, etc.

---

## Implementation Order

### Phase 1: Critical Fixes (1-2 hours)
1. P0-1: Fix `main.py` logger bug
2. P0-2: Fix `utils.py` import bug
3. P0-3: Fix `utils.py` max_size bug

### Phase 2: Security Hardening (2-3 hours)
4. P1-1: Add request body size limit
5. P1-2: Enable SQLite WAL mode
6. P1-3: Enable FK enforcement
7. P1-4: Fix datetime to UTC
8. P1-5: Add input validation
9. P1-6: Verify payment prices

### Phase 3: Tooling (3-4 hours)
10. P2-1: Add pytest + CI/CD
11. P2-2: Add type checking
12. P2-3: Add linter

### Phase 4: Architecture (4-6 hours)
13. P2-4: Consolidate schema
14. P2-5: Add migration system
15. P2-6: Add Redis (optional)

### Phase 5: Features (ongoing)
16. P3-1: Email service
17. P3-2: Product images
18. P3-3: Barcode generation
19. P3-4: Multi-device sync
20. P3-5: Audit trail
21. P3-6: i18n

---

## Metrics to Track

| Metric | Current | Target | How to Measure |
|--------|---------|--------|----------------|
| **Bug Count** | 2 critical, 1 moderate | 0 critical, 0 moderate | Manual review |
| **Test Coverage** | ~60% (estimated) | 80%+ | `pytest --cov` |
| **Type Coverage** | 0% | 90%+ | `mypy --strict` |
| **Lint Score** | Unknown | 0 errors | `ruff check` |
| **API Response Time** | <100ms (SQLite) | <50ms | Load testing |
| **Concurrent Users** | 1-5 (SQLite) | 20+ (with WAL/Redis) | Load testing |

---

## Cross-References
- [[wiki/00-Current-Projects/inventory-system/deep-review-report]] — Full review with bug details
- [[wiki/00-Current-Projects/inventory-system]] — System overview and architecture
- [[wiki/00-Current-Projects/stock-agent/improvement-roadmap]] — Similar roadmap for stock-agent
- [[brain/Patterns/agent-pipeline-patterns]] — Improvement roadmap patterns