---
course_code: "PROGRAMMING"
course_name: "Programming & Software Engineering Field"
unit: "Module 7 — Advanced Python (Non-Data-Science)"
tags: [python, async, concurrency, django, databases, type-checking, webscraping, telegram-bot, tooling]
last_updated: "2026-08-24"
confidence: "high"
source: "https://github.com/niderhoff/knowledge-repository#python-non-datascience"
---

## For future agent
Production Python beyond notebooks: idioms and anti-patterns, typing, async/concurrency trade-offs, Django patterns, database tooling/DevOps, bot building, scraping. Complements the vault's [[modules/object-oriented-programming/overview|OOP module]] (which covers classes/patterns) by covering the ecosystem around the language.

# Advanced Python — Ecosystem & Craft

## Courses / Books
- **[The Hitchhiker's Guide to Python](https://docs.python-guide.org/)** — opinionated best-practices guide (envs, structure, style)
- **[Automate the Boring Stuff](https://automatetheboringstuff.com/)** — practical scripting; free online
- [Full Stack Python](https://www.fullstackpython.com/table-of-contents.html) — everything-Python deployment encyclopedia
- [Fluent Python (Ramalho)](https://github.com/fluentpython) · [Effective Python](https://effectivepython.com/) — the two mastery books
- [Python Programming & Numerical Methods (Berkeley)](https://pythonnumericalmethods.berkeley.edu/notebooks/Index.html) — for engineers/scientists
- [Dave Beazley courses](https://www.dabeaz.com/courses.html) — legendary advanced Python training

## Idioms, Paradigms, Deep Features
- [Python 3 Patterns, Recipes and Idioms (incl. Singleton)](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html)
- [Functional Programming in Python (free O'Reilly)](https://www.oreilly.com/programming/free/files/functional-programming-python.pdf)
- **[Composing Programs (Berkeley CS61A text)](https://www.composingprograms.com/** — programming-as-abstraction, SICP-in-Python
- [OOP basics (swaroopch)](https://python.swaroopch.com/oop.html) → deep version: [[modules/object-oriented-programming/overview]]
- **[wtfpython](https://github.com/satwikkansal/wtfpython)** — surprising snippets explaining interpreter internals
- [Little Book of Python Anti-Patterns](https://docs.quantifiedcode.com/python-anti-patterns/)
- **[pytudes (Peter Norvig)](https://github.com/norvig/pytudes)** — short programs for perfecting skill; study-quality code
- [pysanity](https://github.com/rednafi/pysanity/) — opinionated guidelines

## Basics Reference
- Config files: [YAML/JSON/etc. in Python](https://martin-thoma.com/configuration-files-in-python/)
- [String formatting cookbook](https://mkaz.blog/code/python-string-format-cookbook/)
- [Google-style docstrings (Napoleon)](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

## Tooling: Testing / Linting / Performance / Typing
- **[Numba](http://numba.pydata.org/)** — JIT compiler for numeric Python
- [Hypermodern Python dev environment (cjolowicz)](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/) — series: modern project setup
- Type checking:
  - **[Dropbox's journey to typing 4M lines](https://dropbox.tech/application/our-journey-to-type-checking-4-million-lines-of-python)** — case study at scale
  - [Type hints explained (kunigami)](https://kunigami.blog/2019/12/26/python-type-hints/)
  - [MonkeyType (Instagram)](https://github.com/instagram/MonkeyType) — generates hints from runtime types
- Dev resources gist: [AlmasM's collection](https://gist.github.com/AlmasM/8a05355dbd84029eae03f92c5c61038f)

## Async / Concurrency (decision-critical)
| Resource | Takeaway |
|----------|----------|
| **[Async Python is not faster (Cal Paterson)](http://calpaterson.com/async-python-is-not-faster.html)** | HTTP benchmarks: asyncio often loses to threads+gunicorn |
| [Sync vs Async: what's the difference (Grinberg)](https://blog.miguelgrinberg.com/post/sync-vs-async-python-what-is-the-difference) | Clear conceptual split |
| [Async IO complete walkthrough (realpython)](https://realpython.com/async-io-python/) | The full tutorial |
| [Concurrency: the tricky bits](https://archive.ph/RQSfH) | Threads vs processes vs coroutines |
| HN discussion | [23289563](https://news.ycombinator.com/item?id=23289563) |

**Decision rule** (distilled): CPU-bound → multiprocessing; I/O-bound modest scale → threads; I/O-bound high-concurrency + async-native stack → asyncio.

## CLI Apps
- **[Building Rich Terminal Dashboards (Will McGugan)](https://www.willmcgugan.com/blog/tech/post/building-rich-terminal-dashboards/)** — by the Rich/Textual author

## Django Patterns
- [GraphQL in Django overview](https://medium.com/swlh/graphql-in-django-an-overview-51d27e7fceb3)
- Concurrency control: [managing concurrency in Django models (hakibenita)](https://medium.com/@hakibenita/how-to-manage-concurrency-in-django-models-b240fed4ee2) · [SO thread](https://stackoverflow.com/questions/1645269/concurrency-control-in-django-model)
- Background jobs: [django-celery](https://pypi.org/project/django-celery/) · [django-rq (Redis Queue)](https://github.com/rq/django-rq)

## Databases & DB DevOps
- [Introduction to Databases (Stanford self-paced)](https://lagunita.stanford.edu/courses/DB/2014/SelfPaced/about)
- Testing: [pytest-postgresql](https://pypi.org/project/pytest-postgresql/) · [pgmock announcement](https://technology.cloverhealth.com/better-postgresql-testing-with-python-announcing-pytest-pgsql-and-pgmock-d0c569d0602a) · [SO: DB testing in python/postgres](https://stackoverflow.com/questions/2723406/database-testing-in-python-postgresql)
- [Databases chapter (Full Stack Python)](https://www.fullstackpython.com/databases.html)
- Migrations tooling: [Alembic (SQLAlchemy)](https://alembic.sqlalchemy.org/en/latest/) · [Flyway](https://flywaydb.org/) · [Roundhouse](https://github.com/chucknorris/roundhouse) · driver: [psycopg](https://www.psycopg.org/)

## Telegram Bots (Telethon)
- [Telethon docs](https://lonamiwebs.github.io/Telethon/) · [API introduction](https://towardsdatascience.com/introduction-to-the-telegram-api-b0cd220dbed2) · [create + deploy a bot](https://djangostars.com/blog/how-to-create-and-deploy-a-telegram-bot/)
- Vault link: n8n Telegram nodes cover no-code variant → [[modules/automations/quick-start-guide]]

## Web Scraping
- **[Web Scraping 101 with Python (ScrapingBee)](https://www.scrapingbee.com/blog/web-scraping-101-with-python/)** — requests→BeautifulSoup→Selenium ladder

## Related Pages

- [[modules/programming/overview|Programming Hub]] · [[software-dev-general]] · [[languages-polyglot]] (JavaScript section pairs with web work)
- [[modules/object-oriented-programming/overview|OOP module]] · [[modules/object-oriented-programming/modern-oop-dataclasses-typing|dataclasses & typing]] — deeper on typing
- [[modules/programming/cs50/week-9-flask|CS50 Flask week]] — lighter-weight alternative to Django