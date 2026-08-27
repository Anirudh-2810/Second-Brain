"""Generate index.html — browser dashboard of the whole vault, grouped by PARA domain.

Run:  python .scripts/generate-index.py
"""
import os, html, datetime

VAULT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI = os.path.join(VAULT, 'wiki')
VAULT_NAME = os.path.basename(VAULT)

DOMAINS = [
    ('🔨 Current Projects', '00-Current-Projects', None),
    ('💼 Business', '01-Areas/Business', ['careers', 'automations', 'quant-finance']),
    ('💻 Programming & Coding', '01-Areas/Programming', None),
    ('🤖 AI & Data Science', '01-Areas/AI-Data', ['data-science', 'ai', 'ai-ml']),
    ('⚙️ Engineering', '01-Areas/Engineering', None),
    ('🧠 Self-Development', '01-Areas/Self-Dev', ['self-mastery', 'productivity', 'german']),
    ('📚 Resources', '02-Resources', ['case-studies', 'learning-resources', 'academic-databases']),
    ('🗺 Roadmaps Hub', '01-Areas/Roadmaps', None),
]

def title_of(path):
    with open(path, encoding='utf-8') as f:
        for line in f:
            if line.startswith('# '):
                return html.escape(line[2:].strip())
    return html.escape(os.path.splitext(os.path.basename(path))[0])

def obsidian_uri(rel):
    from urllib.parse import quote
    return f"obsidian://open?vault={quote(VAULT_NAME)}&file={quote(rel.replace(os.sep, '/'))}"

def list_pages(folder):
    pages = []
    for root, dirs, files in os.walk(folder):
        for fn in files:
            if fn.endswith('.md'):
                full = os.path.join(root, fn)
                rel_dom = os.path.relpath(full, folder).replace(os.sep, '/')
                rel_vault = os.path.relpath(full, VAULT).replace(os.sep, '/')
                pages.append((rel_vault, fn[:-3], rel_dom.count('/')))
    return sorted(pages)

rows = []
total = 0
for label, folder, subs in DOMAINS:
    dom_path = os.path.join(WIKI, folder)
    if not os.path.isdir(dom_path):
        continue
    all_pages = list_pages(dom_path)
    rows.append(f'<h2>{html.escape(label)}</h2>')
    rows.append(f'<p class="path">wiki/{folder}/</p>')
    blocks = []
    if subs is None:
        blocks.append(('— root —', [p for p in all_pages if p[2] == 0]))
        for sub in sorted(d for d in os.listdir(dom_path) if os.path.isdir(os.path.join(dom_path, d))):
            sp = [p for p in all_pages if p[0].startswith(f'wiki/{folder}/{sub}/')]
            if sp:
                blocks.append((sub, sp))
    else:
        blocks.append(('— root —', [p for p in all_pages if p[2] == 0]))
        for sub in subs:
            sp = [p for p in all_pages if p[0].startswith(f'wiki/{folder}/{sub}/')]
            if sp:
                blocks.append((sub, sp))
    for bname, pages in blocks:
        if not pages:
            continue
        if bname != '— root —':
            rows.append(f'<h3>{html.escape(bname)}/</h3>')
        rows.append('<ul>')
        for rel, base, _ in sorted(pages, key=lambda x: (x[1].lower() != 'index', x[1].lower())):
            name = 'INDEX' if base == 'INDEX' else base
            cls = ' class="idx"' if base == 'INDEX' else ''
            rows.append(f'<li{cls}><a href="{obsidian_uri(rel)}">{html.escape(name)}</a></li>')
            total += 1
        rows.append('</ul>')

now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
out = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>Second Brain — Vault Index</title>
<style>
 body{{font-family:system-ui,-apple-system,sans-serif;max-width:960px;margin:2rem auto;padding:0 1rem;
      background:#1e1e2e;color:#cdd6f4;line-height:1.5}}
 h1{{color:#cba6f7}} h2{{color:#89b4fa;border-bottom:1px solid #45475a;padding-bottom:.2rem;margin-top:2rem}}
 h3{{color:#a6adc8}} .path{{font-family:monospace;color:#6c7086;font-size:.85em}}
 a{{color:#89dceb;text-decoration:none}} a:hover{{text-decoration:underline}}
 li.idx a{{color:#a6e3a1;font-weight:600}}
 ul{{columns:2;gap:2rem}} @media(max-width:700px){{ul{{columns:1}}}}
 .meta{{color:#6c7086;font-size:.85em}}
</style></head><body>
<h1>🧠 Second Brain — Vault Index</h1>
<p class="meta">Generated {now} · {total} pages · regenerate: <code>python .scripts/generate-index.py</code> · colors: <code>python .scripts/update-graph-colors.py</code><br>
Click any link to open in Obsidian.</p>
{chr(10).join(rows)}
</body></html>"""

with open(os.path.join(VAULT, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(out)
# GitHub Pages copy (served from /docs via Pages settings)
docs = os.path.join(VAULT, 'docs')
os.makedirs(docs, exist_ok=True)
with open(os.path.join(docs, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(out)
print(f'index.html regenerated (root + docs/): {total} pages')
