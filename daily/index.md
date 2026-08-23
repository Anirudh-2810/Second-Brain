---
tags: [daily, index]
---

# Daily Notes Index

> Auto-updating list of every daily note. **Any new daily note you create in `daily/` appears here automatically** (via Dataview) — newest first.

---

## All daily notes (newest first)

```dataview
TABLE
    dateformat(file.mtime, "yyyy-MM-dd HH:mm") AS "Last edited"
FROM "daily"
WHERE file.name != this.file.name
SORT file.name DESC
```

---

## Related

- [[Home]] — the heatmap dashboard (vault activity, study, exercise, mood)
- [[templates/daily-note-template|Daily Note Template]] — the template used for new daily notes