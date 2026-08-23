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

## 🎯 North Star Alignment

_The first block is what you committed to (live from [[North Star]]); the second scores it against what your vault says you actually did this week._

![[North Star#Current Focus]]

### Should vs Am — automatic audit

```dataviewjs
const ns = dv.page("brain/North Star");
if (!ns) {
    dv.paragraph("`brain/North Star.md` missing — create it.");
} else {
    const today = dv.date("today").startOf("day");
    const cutoff = today.minus({ days: 7 });

    const STOP = new Set(["the","and","for","with","this","that","your","from","into",
        "start","keep","build","building","work","toward","track","project","focus",
        "area","path","self","study"]);

    const focuses = ns.file.lists
        .where(l => l.section && /^current focus/i.test(l.section.subpath ?? ""))
        .map(l => String(l.text)).array();

    const recent = dv.pages("")
        .where(p => p.file.mday && p.file.mday >= cutoff)
        .where(p => { const f = p.file.folder;
            return !f.startsWith("templates") && !f.startsWith("raw-sources"); })
        .array();

    const dailies = dv.pages('"daily"')
        .where(p => p.file.day && p.file.day >= cutoff).array();
    const studyH = dailies.reduce((s, p) => s + (p.Study ? Number(p.Study) : 0), 0);

    const badge = n => n >= 3 ? "🟢 on track" : n >= 1 ? "🟡 quiet" : "🔴 stalled";

    if (!focuses.length) {
        dv.paragraph("No `## Current Focus` bullets found in North Star — add some.");
    } else {
        let rows = [];
        for (const raw of focuses) {
            const m = String(raw).match(/\*\*(.+?)\*\*/);
            const title = (m ? m[1] : String(raw).split(/[—-]/)[0]).trim();

            // Habit-style focus → judge by daily logging
            if (/habit|streak/i.test(title)) {
                const v = dailies.length >= 5 ? "🟢 on track"
                        : dailies.length >= 3 ? "🟡 quiet" : "🔴 stalled";
                rows.push([title,
                    `${dailies.length}/7 days logged · ${studyH}h study`, v]);
                continue;
            }

            // Knowledge/project focus → match keywords against touched notes
            const kw = title.toLowerCase().replace(/[^a-z0-9 ]/g, " ").split(/\s+/)
                .filter(w => w.length > 2 && !STOP.has(w));
            const hits = [];
            for (const p of recent) {
                const tagStr = p.tags ? p.tags.array().join(" ") : "";
                const hay = (p.file.path + " " + tagStr).toLowerCase();
                if (kw.some(k => hay.includes(k))) hits.push(p);
            }
            const ev = hits.slice(0, 3).map(p => p.file.link).array().join(" · ");
            rows.push([title,
                hits.length ? `${hits.length} note${hits.length === 1 ? "" : "s"} touched: ${ev}` : "no vault activity this week",
                badge(hits.length)]);
        }
        dv.table(["North Star says…", "…but the vault saw (7 days)", "Verdict"], rows);
        dv.el("small", "🟢 ≥3 touches · 🟡 1–2 · 🔴 untouched. Heuristic — it reads note paths & tags; do work where it lives (wiki modules, brain notes) so it sees you.");
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

## 🧠 Mental Health

```dataviewjs
const logged = dv.pages('"daily"').where(p => p.Mood != null && Number(p.Mood) > 0)
    .sort(p => p.file.name, "desc");
const arr = logged.array();
if (!arr.length) {
    dv.paragraph("Log `Mood` in your daily notes to see trends here.");
} else {
    const moods = arr.map(p => Number(p.Mood));
    const avg = a => a.length ? a.reduce((x, y) => x + y, 0) / a.length : null;
    const week = moods.slice(0, Math.min(7, moods.length));
    const prev = moods.slice(7, 14);
    const w = avg(week), pv = avg(prev);
    let trend = "";
    if (w != null && pv != null)
        trend = w > pv + 0.1 ? " 📈 better than prior week" : (w < pv - 0.1 ? " 📉 worse than prior week" : " ➖ steady vs prior week");
    const exDays = arr.filter(p => p.Exercise === true || p.Exercise === "true").length;
    const low = arr.filter(p => Number(p.Mood) <= 2);
    const streak = (() => { // consecutive logged days with Mood >= 4 ending at most recent
        let s = 0;
        for (const m of moods) { if (m >= 4) s++; else break; }
        return s;
    })();
    dv.table(["Signal", "Reading"], [
        [`Avg mood — last ${week.length} logged`, w != null ? `${w.toFixed(1)} / 5${trend}` : "–"],
        ["Good-day streak (mood ≥ 4)", streak ? `${streak} day${streak === 1 ? "" : "s"}` : "—"],
        ["Exercise", `${exDays} of last ${arr.length} logged days`],
        ["Rough days (mood ≤ 2)", low.length ? low.map(p => p.file.link).array().join(" · ") : "none recently 💪"],
    ]);
    if (low.length >= 3)
        dv.paragraph("> ⚠️ Several rough days lately — worth a check-in with yourself. Sleep, sunlight, movement, someone to talk to.");
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
