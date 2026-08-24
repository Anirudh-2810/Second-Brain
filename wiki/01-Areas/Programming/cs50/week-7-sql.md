---
module: "programming"
course: "CS50x — Introduction to Computer Science"
week: 7
topic: "SQL — Regular vs Relational Data, Queries, JOINs, Design & Injection"
tags: [programming, computer-science, cs50, harvard, sql, database, sqlite, joins, primary-key, foreign-key, sql-injection]
last_updated: "2026-08-11"
---

# Week 7 — SQL

> **Goal of the week:** upgrade from *flat files* (CSV) to **relational databases**, and write `SELECT/INSERT/UPDATE/DELETE` in **SQL** — the same language powering banks, apps, and quant back-offices.
> **PSet 7:** *Movies* (many `SELECT` workouts), *Fiftyville* (a detective game — SQL as forensics).

---

## 1. From Flat Files to Databases

- **Flat file** = one table (e.g. `favorites.csv`). Re-scanning the whole file for every question is $O(n)$ and it chokes on relationships (same user, many shows …).
- **Database (EDB: SQLite in CS50)** stores tables *with structure* and lets the engine search fast via **indexes** — Week 5's hash/B-tree ideas, now SQL's job.
- Open in class:

```
$ sqlite3 favorites.db
sqlite> .mode csv
sqlite> .import favorites.csv favorites
$ sqlite3 favorites.db
sqlite> SELECT * FROM favorites;
```

---

## 2. The Four Core Operations (CRUD)

| Operation | SQL | Notes |
|---|---|---|
| Create table | `CREATE TABLE favorites (id INTEGER, name TEXT);` | define columns + types |
| Insert | `INSERT INTO favorites (name, genre) VALUES ('Office', 'Comedy');` | add rows |
| Read | `SELECT name, genre FROM favorites;` | query columns |
| Update | `UPDATE favorites SET genre = 'Reality' WHERE title = 'Love Island';` | change rows |
| Delete | `DELETE FROM favorites WHERE title = '...';` | remove rows |

**Filtering & shaping — the workhorses:**
```sql
SELECT * FROM shows
WHERE title LIKE '%game%'    -- pattern match (case-insensitive-ish)
ORDER BY year DESC LIMIT 10; -- sort + cap rows

SELECT genre, COUNT(*) AS cnt FROM shows GROUP BY genre;   -- aggregate
```

**Aggregates:** `COUNT`, `AVG`, `SUM`, `MAX`, `MIN`; `GROUP BY` splits rows into buckets. This becomes the "SQL as analytics" step later in quant work.

---

## 3. Relational Design — Normalizing, Keys, and JOIN

**Problems a single table hides:** duplicated data ("The Office" repeated per genre), inconsistency, wasted storage, and painful updates. Solution: **separate concerns into multiple tables and JOIN them**.

- **Primary key** — unique per row (`id INTEGER PRIMARY KEY AUTOINCREMENT`).
- **Foreign key** — a column referencing another table's primary key (`show_id` in `genres` → `id` in `shows`).

```sql
CREATE TABLE shows (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    year INTEGER
);

CREATE TABLE genres (
    show_id INTEGER,
    genre TEXT,
    FOREIGN KEY(show_id) REFERENCES shows(id)
);

-- Reconstruct the "one big table" view:
SELECT title, genre FROM genres JOIN shows ON genres.show_id = shows.id;
```

| JOIN type | Result |
|---|---|
| `JOIN` / `INNER JOIN` | only rows that match on both sides |
| `LEFT JOIN` | all left rows (NULLs where nothing matched) |
| `RIGHT/FULL JOIN` | mirrors / both (SQLite lacks FULL) |

> **Design principle:** one table per *entity*; link with foreign keys; **query by joining** instead of duplicating. (The same normalization instinct applies to note-taking/PM — cross-link [[pkm-code-framework]].)

---

## 4. Indexes — Make Queries Fast

```sql
CREATE INDEX title_index ON shows (title);
```
- The database builds a search structure (hash or B-tree) on the column → `WHERE title = …` drops from full scans to ~$O(\log n)$.
- **The Week 5 lesson, relocated:** indexes trade *write speed + storage* for *read speed* — pick columns you actually filter/sort/join on.

---

## 5. SQL Injection — Malicious Input as a *Query*

SQL queries in app code are often built by **string concatenation**, so user input can leak into the SQL:

```
WHERE username = "" OR "1"="1"      -- always true → login bypassed
```

- `OR '1'='1'` (or `'; DROP TABLE users; --`) exploits *untrusted input merged into a command*.
- **Defense = parameterized queries** (bind values, never splice text):

```python
db.execute("SELECT * FROM users WHERE username = ? AND password = ?", username, password)
```
- **The deeper lesson (echoes Week 4):** *never trust input; always validate/sanitize the boundary between your code and the outside world.* Week 10's cybersecurity amplifies this.

---

## 6. CS50's SQL Metaphor to Keep

"Moves" — a SQL statement is a *question about the data*; `JOIN` is the relational pulse; indexes are the engine's shortcuts. And everything we simulated in C (memory layout, arrays, searching, structures) now happens *inside the database engine* — the abstraction stack closes the loop. Famous CS50 takeaway: because SQL is "so powerful," **design carefully** — a bad query touches every user.

---

## 7. Vocabulary to Master

- flat file · database/DBMS (SQLite) · table · column type · CRUD · `SELECT ... FROM ... WHERE` · `LIKE`, `ORDER BY`, `LIMIT`, `GROUP BY` · aggregate (`COUNT/AVG/SUM`) · primary key · foreign key · normalization · `JOIN` (inner/left) · index · transaction (flavor) · SQL injection · parameterized query

## 8. Cross-Links

- [[cs50/week-5-data-structures]] — indexes implement hash tables/B-trees.
- [[cs50/week-6-python]] — `import csv`, flat files, and `import sqlite3` sit right next door.
- [[cs50/week-9-flask]] — SQL becomes the *backend* of web apps (`db.execute` + Jinja).
- [[cs50/week-10-cybersecurity]] — injection returns as a full security concern.
- [[cs50/problem-sets]] — PSet 7 (Movies / Fiftyville).
- [[quant-toolkit-and-skills]] · [[predictive-return-models]] — SQL/`GROUP BY` aggregates are the analytics backbone of quant data work.