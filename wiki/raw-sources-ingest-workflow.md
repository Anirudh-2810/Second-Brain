---
date: "2026-10-02"
last_updated: "2026-10-02"
description: "Working procedure for ingesting raw-sources into the wiki — extraction recipes per file type (PDF/DOCX/PPTX/PPTX-slides), the duplicate-academic-year deck check, deck-to-deck text diffing, and the correctness traps that caused a whole-session date error."
tags: [raw-sources, ingest, workflow, extraction, pymupdf, pptx, docx, pdf, gotcha-worthy, method]
confidence: high
prerequisites: []
---

## For future agent

The repeatable procedure for turning files in `raw-sources/` into linked wiki pages. Written 2026-10-02 after the SPM ingest, where the naive approach failed twice and a third mistake cost a whole sweep of corrections.

**Why this exists:** the `read` tool **cannot read PDFs** — it returns *"Cannot read pdf (this model does not support pdf input)"*. Every PDF in this vault therefore needs a text-extraction step first. This note is the recipe. It is the procedure behind [[Gotchas]] entries dated 2026-10-02, and it exists partly because that gotcha originally linked here as a dead link.

**Hard rule from AGENTS.md:** `raw-sources/` is **immutable**. Extract to `Temp/opencode/`, never write into `raw-sources/`. Scratch scripts are disposable — write them to the temp directory, not the vault.

---

## 0. Before you touch anything — the duplicate-source check

`raw-sources/` can hold **the same material in more than one folder, from different academic years.** Blindly ingesting the newer-looking folder can overwrite good content with a dead edition.

**Check before ingesting any deck/slide set:**

```python
import zipfile, re, glob, os
for p in sorted(glob.glob(r"E:\Brain\Second-Brain\raw-sources\<folder>\*.pptx")):
    z = zipfile.ZipFile(p)
    sl = sorted([x for x in z.namelist() if re.match(r"ppt/slides/slide[0-9]+\.xml$", x)])
    txt = ""
    for s in sl[:4]:
        txt += " ".join(re.findall(r"<a:t>(.*?)</a:t>", z.read(s).decode("utf8","ignore"), re.S))
    z.close()
    topic = re.findall(r"TOPIC\s*[0-9.]+", txt)
    ay    = sorted(set(re.findall(r"20\d\d\s*-\s*\d\d", txt)))
    print(os.path.basename(p), topic[:1], ay)
```

**How to read the output:**

- `Topic N.N` + `AY 2026-27` → **current cohort family.**
- `First Year -AY 2025-26` and **no** `Topic` marker → **superseded.** Do not let it overwrite current content.

Verified case: `raw-sources/SPM SEM1 work/PPT/Module 1/` (AY 2026-27, used to build [[01-Areas/Engineering/SPM/spm-module1-faculty-companion]]) vs `raw-sources/SPM Lecture/`, where 7 of 8 decks were 2026-27 but `SPM_Module1_1.1_PPT.pptx` alone was 2025-26. Salvaging only its additive content, into companion §6b, was the right move.

---

## 1. Extraction recipes

### PDF — PyMuPDF or pypdf (both installed)

```python
import fitz                      # pymupdf; prints a deprecation warning, still works
doc = fitz.open(path)
text = "".join(f"\n===== PAGE {i+1} =====\n" + p.get_text() for i, p in enumerate(doc))
doc.close()
```

Import as `import pymupdf` in future — `fitz` is the deprecated alias and warns.

### DOCX — stdlib only, no install

```python
import zipfile, re
with zipfile.ZipFile(path) as z:
    xml = z.read("word/document.xml").decode("utf8", "ignore")
xml = re.sub(r"</w:p>", "\n", xml)
xml = re.sub(r"</w:tr>", "\n", xml)
xml = re.sub(r"</w:tc>", " | ", xml)
xml = re.sub(r"<w:tab[^>]*/>", "\t", xml)
xml = re.sub(r"<[^>]+>", "", xml)          # strip all remaining tags
xml = xml.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
```

**Expect OCR garbage** in lab records — duplicated blocks like `873912329668# include <stdio .h>` are scanner noise, not content. Logic is trustworthy; formatting is not. Hand-clean and note it.

### PPTX — stdlib only; **PyMuPDF cannot open it**

A `.pptx` is a **ZIP archive**, not a PDF. `python-pptx` is **not installed** in this environment and is unnecessary:

```python
import zipfile, re
z = zipfile.ZipFile(path)
sl = sorted([x for x in z.namelist() if re.match(r"ppt/slides/slide[0-9]+\.xml$", x)],
            key=lambda s: int(re.findall(r"[0-9]+", s)[0]))
for s in sl:
    xml = z.read(s).decode("utf8", "ignore")
    for p in re.findall(r"<a:p>(.*?)</a:p>", xml, re.S):     # each <a:p> is a paragraph
        line = "".join(re.findall(r"<a:t>(.*?)</a:t>", p, re.S)).strip()
        if line:
            print(line)
z.close()
```

**Speaker notes:** `ppt/notesSlides/notesSlideN.xml`. On the SPM decks these were pure slide-number boilerplate (`‹#›`), adding only ~0.3 KB/deck — **check once, then skip.**

### PPTX exported to PDF, and image-only decks

Some decks are exported as PDF where the content is images. **Detect with chars-per-page:**

```python
doc = fitz.open(path)
n = len(doc); c = sum(len(p.get_text().strip()) for p in doc); doc.close()
avg = c / max(n, 1)
# avg > 250 -> text is usable;  40-250 -> thin;  < 40 -> image-only, needs OCR
```

**OCR is NOT available here** — no `tesseract`, no `pytesseract`, no `PIL`. For image-only pages the fallback is **spot-rendering the highest-value pages to PNG and reading them as images** (a prior session did this for slide answers; it works but is token-expensive — a few pages, not a whole deck). In the SPM/Physics case: 129 of 167 physics pages were image-only slide decks.

---

## 2. Diffing two versions of the same deck

When a second copy of a deck exists, **do not overwrite — diff it first.** This found 2 identical decks, 2 cosmetic-only, and 1 real content change across 6 M1 decks.

```python
import zipfile, re, difflib

def lines(path):
    z = zipfile.ZipFile(path)
    sl = sorted([x for x in z.namelist() if re.match(r"ppt/slides/slide[0-9]+\.xml$", x)],
                key=lambda s: int(re.findall(r"[0-9]+", s)[0]))
    out = []
    for s in sl:
        out.append(f"=== SLIDE {int(re.findall(r'[0-9]+', s)[0])} ===")
        for p in re.findall(r"<a:p>(.*?)</a:p>", z.read(s).decode("utf8","ignore"), re.S):
            line = "".join(re.findall(r"<a:t>(.*?)</a:t>", p, re.S)).strip()
            if line and line != "‹#›":
                out.append(line)
    z.close()
    return out

d = list(difflib.unified_diff(lines(old), lines(new), fromfile="OLD", tofile="NEW", lineterm="", n=1))
changed = [x for x in d[2:] if x[:1] in "+-"]
```

**Triage the result — most diffs are noise:**

| Diff signature | Meaning |
|---|---|
| `&quot;` ↔ `"`, `&apos;` ↔ `'` | HTML-entity encoding difference. **Zero content change.** |
| only `=== SLIDE n ===` renumbering | slides were dropped/added. Check *what*, then ignore numbering. |
| line-join changes (`Step 1: Start` → `Step 1: Start\n\nStep 2:`) | re-wrapped text. Cosmetic. |
| **zero changed lines** | decks are equivalent — nothing to do |
| whole section removed/added | **real** — investigate and record |

---

## 3. Correctness traps that have actually bitten

1. **Confirm the system date at wrap-up, not just at session start.** A session that crosses midnight means a date inferred at the start is wrong. This stamped **44 wrong dates across 12 files** and needed a full correction sweep. Run `Get-Date -Format "yyyy-MM-dd"` at *both* ends.
2. **Source-file dates use a different format** (`10/1/2026` from the filesystem, `dated 10/1/2026` in prose) than work-date stamps (`2026-10-01`). A targeted ISO replace is safe — **verify that before running a blanket replace.**
3. **In this PowerShell 5.1 environment, never use `Set-Content -Encoding UTF8` on vault files** — it silently writes a UTF-8 BOM, which makes frontmatter invisible to regex-based checkers and to Obsidian's parser. Use:
   ```powershell
   [System.IO.File]::WriteAllText($p, $t, (New-Object System.Text.UTF8Encoding($false)))
   ```
4. **Don't report a broken-link count from a naive scanner.** Wikilinks inside code fences (`` `[[a, b]]` ``, `` `[[{ "node": "Alert Me" }]]` ``, `` `[[:title:]]` ``) get scraped as links. A scanner that skips frontmatter but **not** code fences reported **607** broken links where the true count was **68** — and most of those 68 were still false positives. Minimum bar: skip frontmatter, resolve relative paths against the linking note's folder (walking up), and match bare basenames.
5. **Verbose ≠ done.** Extracting 8 files is not ingesting them. Read what you extracted and confirm it reached a page before claiming the folder is closed.
6. **Run the correction sweep on EVERY page that restates the value, not just the ones you revised.** When a newly-opened source supersedes a previously-synthesised page, the *deep* page is usually where the stale number still lives — it holds the long derivations, so it is what a confused student actually opens, and it is what they trust. Correcting only the short revision sheet leaves the trap in place. Real case (2026-10-02): four faculty discrepancies were fixed on the laser quick-ref and the new fibre page while `module-2-optoelectronics-lasers-fiber-optics.md` still said `19.78 eV` in two places. Grep the whole vault for the old value before calling it done: `Select-String -Path "wiki/**/*.md" -Pattern "<old value>"`.

---

## 4. Definition of Done for an ingest

Per AGENTS.md, every new page needs: frontmatter (`date`, `description`, `tags`, + type-specific), ≥1 outbound wikilink, ideally ≥1 inbound, listed in its module INDEX, a `wiki/log.md` entry, scripts run, committed **and** pushed.

**Verify it — do not assume.** A scripted check over frontmatter + link counts + size caught 4 real gaps on a session that felt complete (two pages missing `description`, one missing `date`, one daily note with zero wikilinks). Then run `.scripts/update-graph-colors.py` and `.scripts/generate-index.py`.

**Flag, never fake, manual checks:** graph colors, Dataview/Bases output, `<details>` rendering, and heading-anchor link resolution all depend on Obsidian's renderer. You cannot see them. Say so explicitly.

---

## Cross-references

- [[Gotchas]] — the condensed version of §1 and §3
- [[01-Areas/Engineering/SPM/spm-module1-faculty-companion]] — worked example of a deck-verification log (§0 + §2)
- [[syllabus-316U06C107]] — the ingest whose lessons this note records
- [[lab-ca-and-experiments]] — the rubric write-ups are graded against
- [[assessment-guide-ese-ost-quiz]] — why the question banks matter

*Created 2026-10-02 to close a dead `raw-sources-ingest-workflow` link in [[Gotchas]] and to make the SPM/Physics ingest procedure reusable.*
