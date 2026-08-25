# 🏠 Home

> Everything on this page pulls live from your notes — nothing to maintain manually.
> The agent reads `AGENTS.md` and [[North Star]] every session.

| | |
|---|---|
| **🎯 Goals** | [[North Star]] · [[North Star#Shifts Log\|Shifts Log]] |
| **🧠 Memory** | [[Memories]] · [[Key Decisions]] · [[Patterns]] · [[Gotchas]] · [[Wins]] · [[Profile]] |
| **📚 Knowledge** | [[wiki/index\|Wiki Index]] · [[wiki/log\|Wiki Log]] · `raw-sources/` → `/om-ingest` |
| **📅 Days** | [[daily/index\|Daily Index]] · today's note via Daily Notes plugin |
| **👁 Views** | [[Recently Touched.base\|Recently Touched]] · [[Wiki.base\|Wiki Pages]] · [[Daily.base\|Daily Table]] · [[Brain.base\|Memory Topics]] · [[Templates.base\|Templates]] |
| **⚡ Commands** | `/om-standup` `/om-dump` `/om-wrap-up` `/om-weekly` — full catalog: [[Skills]] |

---

## 🗂 Domain Map (scoped retrieval — agent scans the matching folder only)

| Ask about… | Scan | Hub |
|---|---|---|
| 💼 Business / career / market / trading | `wiki/01-Areas/Business/` | [[01-Areas/Business/INDEX\|Business INDEX]] |
| 💻 Coding / DSA / frameworks / case studies | `wiki/01-Areas/Programming/` | [[01-Areas/Programming/INDEX\|Programming INDEX]] |
| 🤖 AI / ML / data science | `wiki/01-Areas/AI-Data/` | [[01-Areas/AI-Data/INDEX\|AI-Data INDEX]] |
| ⚙️ College engineering / coursework | `wiki/01-Areas/Engineering/` | [[01-Areas/Engineering/INDEX\|Engineering INDEX]] |
| 🧠 Mind / habits / discipline / German | `wiki/01-Areas/Self-Dev/` | [[01-Areas/Self-Dev/INDEX\|Self-Dev INDEX]] |
| 🔨 My own builds (stock-agent, RAG brain) | `wiki/00-Current-Projects/` | [[00-Current-Projects/INDEX\|Builds INDEX]] |
| 🗺 All roadmaps in one place | [[01-Areas/Roadmaps/INDEX]] | — |

Browser dashboard: open `index.html` at vault root.

---

## 🎯 North Star Alignment

_The first block is what you committed to (live from [[North Star]]); the second scores it against what your vault says you actually did this week._

![[North Star#Current Focus]]

### Should vs Aim — automatic audit

```dataviewjs
// Each North Star focus maps to the folder where its evidence lives.
// Edit FOCUS_MAP when goals move or new domains appear.
const FOCUS_MAP = [
    [/robotics|\brai\b|kjsce/i,                    ["wiki/01-Areas/Engineering"]],
    [/quant/i,                                     ["wiki/01-Areas/Business"]],
    [/stock[- ]?agent/i,                           ["wiki/00-Current-Projects/stock-agent"]],
    [/retrieval|\brag\b|second.?brain/i,           ["wiki/00-Current-Projects/retrieval-agent"]],
    [/freelanc|n8n|client|automation business/i,   ["wiki/01-Areas/Business/automations", "wiki/01-Areas/Business/careers"]],
    [/habit|streak/i,                              "HABIT"],
];
const NOISE = /(\/INDEX\.md$|\/log\.md$|^wiki\/index\.md$|^Home\.md$|^docs\/)/;

const ns = dv.page("brain/North Star");
if (!ns) {
    dv.paragraph("`brain/North Star.md` missing — create it.");
} else {
    const cutoff = dv.date("today").startOf("day").minus({ days: 7 });

    const focuses = ns.file.lists
        .where(l => l.section && /^current focus/i.test(l.section.subpath ?? ""))
        .map(l => String(l.text)).array();

    const touched = dv.pages("")
        .where(p => p.file.mday && p.file.mday >= cutoff)
        .where(p => { const f = p.file.path;
            return f.startsWith("wiki/") && !NOISE.test(f); }).array();

    const dailies = dv.pages('"daily"')
        .where(p => p.file.day && p.file.day >= cutoff).array();
    const studyH = dailies.reduce((s, p) => s + (Number(p.Study) || 0), 0);

    const badge = n => n >= 3 ? "🟢 on track" : n >= 1 ? "🟡 quiet" : "🔴 stalled";

    if (!focuses.length) {
        dv.paragraph("No `## Current Focus` bullets found in North Star — add some.");
    } else {
        let rows = [];
        for (const raw of focuses) {
            const m = String(raw).match(/\*\*(.+?)\*\*/);
            const title = (m ? m[1] : String(raw).split(/[—-]/)[0]).trim();

            // Habit-style focus → judged by daily logging
            if (/habit|streak/i.test(title)) {
                const v = dailies.length >= 5 ? "🟢 on track"
                        : dailies.length >= 3 ? "🟡 quiet" : "🔴 stalled";
                rows.push([title,
                    `${dailies.length}/7 days logged · ${studyH}h study`, v]);
                continue;
            }

            // Goal → scoped-domain evidence (pages meaningfully touched this week)
            const entry = FOCUS_MAP.find(([re]) => re.test(title));
            let hits;
            if (entry) {
                hits = touched.filter(p => entry[1].some(f =>
                    p.file.path.startsWith(f + "/")));
            } else {
                // unmapped goal: fall back to keyword search over wiki paths+tags
                const kw = title.toLowerCase().replace(/[^a-z0-9 ]/g, " ").split(/\s+/)
                    .filter(w => w.length > 2);
                hits = touched.filter(p => {
                    const tagStr = p.tags ? p.tags.array().join(" ") : "";
                    const hay = (p.file.path + " " + tagStr).toLowerCase();
                    return kw.some(k => hay.includes(k));
                });
                if (hits.length)
                    rows.push([title + " ⚠️ unmapped — add to FOCUS_MAP",
                        `${hits.length} generic hit${hits.length === 1 ? "" : "s"}`, "🟡"]);
                else
                    rows.push([title + " ⚠️ unmapped — add to FOCUS_MAP",
                        "no vault activity this week", "🔴 stalled"]);
                continue;
            }

            const ev = hits.sort((a, b) => b.file.mday.toMillis() - a.file.mday.toMillis())
                .slice(0, 3).map(p => p.file.link).array().join(" · ");
            rows.push([title,
                hits.length ? `${hits.length} page${hits.length === 1 ? "" : "s"} touched: ${ev}` : "no activity in its domain this week",
                badge(hits.length)]);
        }
        dv.table(["North Star says…", "…but the vault saw (7 days)", "Verdict"], rows);
        dv.el("small", "🟢 ≥3 meaningful touches · 🟡 1–2 · 🔴 untouched. Counts real page edits inside each goal's domain folder — INDEX/log/dashboard churn excluded.");
    }
}
```

---

## ✅ What's On Today & Tomorrow

```dataviewjs
const fmt = d => d.toFormat("yyyy-MM-dd");
const today = dv.date("today");

// --- Today's to-dos ---
const tp = dv.page(`daily/${fmt(today)}`);
dv.header(4, "Today's To-Dos");
if (tp) {
    const tt = tp.file.tasks.where(t => !t.completed);
    tt.length ? dv.taskList(tt, false) : dv.paragraph("Nothing pending from today's note ✓");
} else {
    dv.paragraph(`No daily note yet — create \`daily/${fmt(today)}.md\``);
}

// --- Carried over: yesterday's "Tomorrow" plan ---
const yest = dv.pages('"daily"')
    .where(p => p.file.day && p.file.day < today)
    .sort(p => p.file.name, "desc").first();
if (yest) {
    const items = yest.file.lists.where(l => l.section && /tomorrow/i.test(l.section.subpath ?? ""));
    if (items.length) {
        dv.header(4, `Carried Over — ${yest.file.link}'s plan`);
        dv.list(items.map(i => i.text));
    }
}
```

## 📌 Open Tasks — last 2 weeks

```dataviewjs
const today = dv.date("today").startOf("day");
const cutoff = today.minus({ days: 14 });
const pages = dv.pages('"daily"').where(p => p.file.day && p.file.day >= cutoff && p.file.day < today);
let open = [];
for (const p of pages)
    for (const t of p.file.tasks)
        if (!t.completed && t.text.trim())
            open.push({ text: t.text, link: p.file.link, day: p.file.day });
open.sort((a, b) => b.day.toMillis() - a.day.toMillis());
if (!open.length) dv.paragraph("No open threads 🎉");
else {
    dv.table(["Task", "From"], open.slice(0, 20).map(o => [o.text, o.link]));
    if (open.length > 20) dv.paragraph(`…and ${open.length - 20} more`);
}
```

---

## 📅 Your Last 7 Days

```dataviewjs
const days = dv.pages('"daily"').where(p => p.file.day)
    .sort(p => p.file.name, "desc").limit(7);
const yesno = v => v === true || v === "true" ? "✔" : "·";
const totalStudy = days.where(p => p.Study).array().reduce((s, p) => s + Number(p.Study), 0);
if (totalStudy) dv.paragraph(`**${totalStudy}h total study** this stretch`);
dv.table(["Day", "Study h", "Exercise", "Mood", "Vlog", "Guitar"],
    days.map(p => [p.file.link, p.Study ?? "–", yesno(p.Exercise), p.Mood ?? "–", yesno(p.Vlogging), yesno(p.Guitar)]));
```

---

# 🔥 Habit Heatmaps

> GitHub-style activity + habit tracker. Data is read from your `daily/` notes.
> **Click any square** to open the note for that day (or create it). Requires the **Dataview** + **Heatmap Tracker** plugins.

## Vault Activity — notes edited per day

```dataviewjs
const trackerData = {
    entries: [],
    separateMonths: true,
    heatmapTitle: "Vault Activity",
    heatmapSubtitle: "Notes edited each day",
    colorScheme: { paletteName: "default" },
    intensityConfig: { defaultIntensity: 1 },
};

const counts = new Map();
for (const p of dv.pages("")) {
    if (!p.file.mday) continue;
    const day = p.file.mday.toFormat("yyyy-MM-dd");
    counts.set(day, (counts.get(day) ?? 0) + 1);
}
for (const [date, count] of counts) {
    trackerData.entries.push({
        date,
        intensity: Number(count),
        content: `${count} note${count === 1 ? "" : "s"} edited`,
    });
}

renderHeatmapTracker(this.container, trackerData);
```

---

## Study — hours of focused study

```dataviewjs
const trackerData = {
    entries: [],
    separateMonths: true,
    heatmapTitle: "Study",
    heatmapSubtitle: "Hours of focused study",
    colorScheme: { paletteName: "default" },
    intensityConfig: { defaultIntensity: 1 },
};

for (const p of dv.pages('"daily"').where(p => p.Study)) {
    trackerData.entries.push({
        date: p.file.name,
        filePath: p.file.path,
        intensity: Number(p.Study),
        content: `${p.Study}h of study`,
    });
}

renderHeatmapTracker(this.container, trackerData);
```

## Exercise — yes/no

```dataviewjs
const trackerData = {
    entries: [],
    separateMonths: true,
    heatmapTitle: "Exercise",
    heatmapSubtitle: "Did I exercise today?",
    colorScheme: { paletteName: "default" },
    intensityConfig: { defaultIntensity: 1 },
};

for (const p of dv.pages('"daily"').where(p => p.Exercise)) {
    trackerData.entries.push({
        date: p.file.name,
        filePath: p.file.path,
        intensity: 1,
        content: "Exercised",
    });
}

renderHeatmapTracker(this.container, trackerData);
```

## Mood — 1 to 5

```dataviewjs
const trackerData = {
    entries: [],
    separateMonths: true,
    heatmapTitle: "Mood",
    heatmapSubtitle: "1 (rough) to 5 (great)",
    colorScheme: { paletteName: "default" },
    intensityConfig: { defaultIntensity: 1, scaleStart: 1, scaleEnd: 5 },
};

for (const p of dv.pages('"daily"').where(p => p.Mood)) {
    trackerData.entries.push({
        date: p.file.name,
        filePath: p.file.path,
        intensity: Number(p.Mood),
        content: `Mood ${p.Mood}/5`,
    });
}

renderHeatmapTracker(this.container, trackerData);
```

## Vlogging — yes/no

```dataviewjs
const trackerData = {
    entries: [],
    separateMonths: true,
    heatmapTitle: "Vlogging",
    heatmapSubtitle: "Did I vlog today?",
    colorScheme: { paletteName: "default" },
    intensityConfig: { defaultIntensity: 1 },
};

for (const p of dv.pages('"daily"').where(p => p.Vlogging)) {
    trackerData.entries.push({
        date: p.file.name,
        filePath: p.file.path,
        intensity: 1,
        content: "Vlogged",
    });
}

renderHeatmapTracker(this.container, trackerData);
```

## Guitar — yes/no

```dataviewjs
const trackerData = {
    entries: [],
    separateMonths: true,
    heatmapTitle: "Guitar",
    heatmapSubtitle: "Did I practice guitar today?",
    colorScheme: { paletteName: "default" },
    intensityConfig: { defaultIntensity: 1 },
};

for (const p of dv.pages('"daily"').where(p => p.Guitar)) {
    trackerData.entries.push({
        date: p.file.name,
        filePath: p.file.path,
        intensity: 1,
        content: "Practiced guitar",
    });
}

renderHeatmapTracker(this.container, trackerData);
```

---

## How to use

1. **Create a daily note** — command palette → "Daily notes". It opens `daily/YYYY-MM-DD.md` with the tracker fields.
2. **Fill in frontmatter**: `Study` (hours), `Exercise`, `Mood` (1–5), `Vlogging`, `Guitar`. Write `- [ ]` checkboxes for anything to do.
3. **Everything above updates itself** — plans carry over from each note's `## Tomorrow`, tasks roll into Open Tasks until checked.

> Adding a metric? Edit `templates/daily-note-template.md` to add a field, then copy a matching block above.
