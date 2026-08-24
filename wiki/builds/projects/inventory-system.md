---
course_code: "PROJECT"
course_name: "Portfolio Projects"
unit: "inventory-system"
tags: [project, github, python, sqlite, security, portfolio]
last_updated: "2026-08-23"
confidence: stated
relations:
  applies_concepts_from: "[[the-four-pillars]]"
  relates_to: "[[automations-catalog]]"
---

## For future agent
This note catalogs the owner's GitHub repo **StockOffline** (offline inventory manager), extracted from its README on 2026-08-23. Use it to answer questions about the project's architecture, security posture, and deployment story; all facts below were stated in the repo itself.

# StockOffline — Secure Offline Inventory System

**Repo:** https://github.com/Anirudh-2810/inventory-system · Python · updated Jul 2026

Offline-first inventory manager for small shops: desktop GUI + CLI run with **zero third-party dependencies** (SQLite local file); optional web/API tier for multi-user access. Ships as a packaged Windows `.exe` (`marketing/dist/StockOffline.exe`).

## Architecture
| Tier | Stack | Notes |
|---|---|---|
| Offline GUI | Python Tkinter (dark theme) | DB next to app/exe; barcode scanners work as keyboard input |
| CLI | stdlib only | `add / list / sale / status / report / export`, `INVENTORY_DB_PATH` env |
| Core domain | `inventory_system/` package — dataclass models (`Product`, `Transaction`) + services + SQLite layer | Parameterized queries throughout |
| Web/API tier | stdlib server or gunicorn WSGI | JWT auth, per-tenant isolation, rate limiting |

## Security posture (stated in repo)
- PBKDF2-HMAC-SHA256 passwords (100k iters, per-user salt, constant-time compare)
- JWT with expiry + logout blacklist; refuses to start without real `JWT_SECRET_KEY`
- Per-tenant scoping server-side (anti-IDOR), strict CORS, security headers, generic errors + correlation IDs
- Rate limits: login 5/min, signup 3/hr, reset 3/hr
- Razorpay webhook signature verification; Stripe reserved
- `DELETE /api/account` cascades full data deletion

## Distribution
PyInstaller spec → standalone exe (relative paths, no dev info baked in, UPX off to dodge AV false positives); not code-signed → SmartScreen warning expected. Includes marketing kit (leaflet, price sheet, shopkeeper guide).

## Why it matters (my read)
Strongest portfolio piece of the three — real product thinking (offline-first constraint, packaging, marketing collateral) plus genuinely serious web security for a solo project. Demonstrates [[the-four-pillars|OOP]] dataclass/service-layer design and could seed the freelancing offer playbook in [[automations-catalog]].
