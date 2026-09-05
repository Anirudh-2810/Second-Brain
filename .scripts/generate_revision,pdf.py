#!/usr/bin/env python3
"""Revision PDF - Basic Python + LLM + 2 Repos + ML (print-ready)"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
from reportlab.lib import colors

OUT = r"C:\Users\Vijaykumar\Second-Brain\Second-Brain\raw-sources\Interview_Revision_Sheet_Basic.pdf"

NAVY = HexColor("#0F2A44")
ACCENT = HexColor("#1F4E78")
BLUE = HexColor("#2E75B6")
GREEN = HexColor("#385723")
DARK = HexColor("#404040")
GOLD = HexColor("#7F6000")
GREY = HexColor("#333333")
LGREY = HexColor("#F2F2F2")
BORDER = HexColor("#B4C6E7")
MUTED = HexColor("#666666")

styles = getSampleStyleSheet()
s_title = ParagraphStyle("title", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=16, textColor=NAVY, alignment=TA_CENTER, spaceAfter=2, leading=18)
s_sub = ParagraphStyle("sub", parent=styles["Normal"], fontName="Helvetica", fontSize=7.5, textColor=HexColor("#555555"), alignment=TA_CENTER, leading=9, spaceAfter=6)
s_h1 = ParagraphStyle("h1", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=10, textColor=colors.white, leading=11)
s_h2 = ParagraphStyle("h2", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=7.8, textColor=NAVY, leading=10, spaceBefore=6, spaceAfter=2)
s_cell = ParagraphStyle("cell", parent=styles["Normal"], fontName="Helvetica", fontSize=6.2, textColor=GREY, leading=7.2, alignment=TA_LEFT, spaceAfter=0)
s_cell_b = ParagraphStyle("cell_b", parent=s_cell, fontName="Helvetica-Bold", fontSize=6.3, textColor=HexColor("#1A1A1A"))
s_cell_small = ParagraphStyle("cell_small", parent=s_cell, fontSize=6.0, leading=6.8)
s_header_cell = ParagraphStyle("header_cell", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=6.2, textColor=colors.white, leading=7, alignment=TA_CENTER)
s_footer = ParagraphStyle("footer", parent=styles["Normal"], fontName="Helvetica", fontSize=6, textColor=HexColor("#777777"), alignment=TA_CENTER)

def hr(color):
    return HRFlowable(width="100%", thickness=1.2, color=color, spaceAfter=4, spaceBefore=2)

def make_table(rows, col_widths, header_fill):
    # rows: list of lists with Paragraph objects already, first row is header
    t = Table(rows, colWidths=col_widths, repeatRows=1)
    style = [
        ("BACKGROUND", (0,0), (-1,0), header_fill),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,0), 6.2),
        ("ALIGN", (0,0), (-1,0), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("GRID", (0,0), (-1,-1), 0.4, BORDER),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, HexColor("#F7F9FC")]),
        ("LEFTPADDING", (0,0), (-1,-1), 3),
        ("RIGHTPADDING", (0,0), (-1,-1), 3),
        ("TOPPADDING", (0,0), (-1,-1), 2),
        ("BOTTOMPADDING", (0,0), (-1,-1), 2),
    ]
    t.setStyle(TableStyle(style))
    return t

def P(text, style=s_cell):
    # escape minimal
    text = text.replace("&", "&amp;")
    return Paragraph(text, style)

# Data reused from sheet generator (kept in sync)
python_rows = [
    ["1","What is Python? Key features?","Interpreted, high-level, dynamically typed, indentation-based. Portable, large stdlib, GC.","python --version; print('hi')","Must"],
    ["2","Data types?","int, float, str, bool, list, tuple, dict, set, None. type(x).","type([1,2]) -> list","Must"],
    ["3","List vs Tuple vs Set vs Dict?","List [] ordered+mutable+dup, Tuple () ordered+immutable, Set {} unordered+unique, Dict {k:v}.","set([1,1])->{1}","Must"],
    ["4","Mutable vs Immutable?","Mutable changes after creation (list/dict/set). Immutable not (str/tuple/int).","s[0]='H' error","Must"],
    ["5","== vs is?","== value, is identity. Use is only for None.","x is None","Must"],
    ["6","Slicing?","seq[start:stop:step]. s[::-1] reverse.","s[::-1]","Must"],
    ["7","List comprehension vs loop?","[x*2 for x in a if x>0]. Gen (x*2 for x in a) lazy."," [x*x for x in range(5)]","Should"],
    ["8","dict.get vs d[key]?","d[key] crashes if missing. get(k,default) safe.","d.get('x',0)","Must"],
    ["9","Function + *args, **kwargs?","def f(a,b=0): *args tuple, **kwargs dict.","f(1,2,x=3)","Must"],
    ["10","Mutable default bug?","def f(a,l=[]) shares list. Fix l=None.","f(1)->[1] bug","Must"],
    ["11","Scope LEGB?","Local>Enclosing>Global>Builtin. global/nonlocal.","x=1; def f(): x=2","Should"],
    ["12","self and __init__?","self=this object. __init__ on obj=Cls().","class Dog: __init__","Must"],
    ["13","Generator vs Iterator?","Iterator __next__, generator yield lazy.","yield 1; yield 2","Should"],
    ["14","with open? try/except?","with auto-closes. try/except/finally.","with open('a.txt')","Must"],
    ["15","Decorator (basic)?","Func wrapping func. @timer is f=timer(f).","@decorator","Should"],
    ["16","Shallow vs Deep copy?","a=b alias. b=a[:] shallow. deepcopy recurses.","copy.deepcopy","Should"],
    ["17","GIL? Thread vs Process?","GIL=one thread at a time. CPU->Process, IO->Thread.","CPU->multiprocess","Should"],
    ["18","venv + pip?","venv per project isolated.","python -m venv .venv","Should"],
    ["19","Where are variables stored?","Name->object in private heap. id() shows addr.","a=5; b=a; id same","Must"],
    ["20","Stack vs Heap?","Stack=frames/refs, Heap=objects. Refcount+GC.","x=[1,2] on heap","Must"],
    ["21","id() and refcount?","id/type/value/refcount. 0->freed.","sys.getrefcount(a)","Must"],
    ["22","Why a is b for small ints?","Cache -5..256 interned. Don't use is.","256 is True, 257 maybe False","Must"],
    ["23","Dynamic typing?","Type on object not name. Rebind any type.","a=5; a='hi'","Must"],
    ["24","a=[1,2]; b=a; b.append?","Alias same heap list. Copy need a[:] .","a->[1,2,3]","Must"],
    ["25","How GC frees?","Refcount 0 now. Cycles need gc.collect().","del a; gc.collect()","Must"],
    ["26","Namespaces? Where?","Name->dict. Locals frame, globals dict, LEGB.","locals()","Should"],
    ["27","Why everything is object?","Even int/func are heap objects.","(5).__class__","Should"],
]

ml_rows = [
    ["1","What is ML? Types?","ML learns pattern to predict. Supervised/ Unsupervised/ RL.","spam = supervised","Must"],
    ["2","Classification vs Regression?","Classification=category, Regression=number.","cat/dog vs price","Must"],
    ["3","Features vs Label?","Features inputs X, Label output y.","X=[age], y=buy","Must"],
    ["4","Train/Test split? Why?","Train 80 learn, Test 20 unseen. Never test on train.","test_size=0.2","Must"],
    ["5","Overfit vs Underfit?","Overfit memorizes fail test. Underfit too simple.","train99/test70 overfit","Must"],
    ["6","Accuracy vs Prec/Rec?","Accuracy fails imbalance. Prec=trust, Rec=coverage.","95/5 fraud 95% useless","Must"],
    ["7","Confusion Matrix?","Table TP,TN,FP,FN.","TP hit FP alarm","Must"],
    ["8","Cross-validation?","k folds rotate validation. Honest.","k=5","Should"],
    ["9","Scaling? When?","Same range 0-1. Need for KNN/grad not trees.","StandardScaler","Should"],
    ["10","Basic algorithms?","Linear/Logistic, Tree(flowchart), Forest(vote), KNN, KMeans.","Forest votes","Must"],
    ["11","Bias-Variance?","Error=bias2+var+noise. Simple high bias.","learning curves","Should"],
    ["12","When accuracy misleads?","On imbalance use PR-AUC/F1.","fraud ex","Should"],
]

llm_rows = [
    ["1","What is LLM? Examples?","LLM predicts next token. ex ChatGPT/Gemini/Claude. Transformer.","ChatGPT decoder","Must"],
    ["2","Transformer core?","Every word looks at every other via Attention, parallel.","which words matter","Must"],
    ["3","Self-Attention formula?","Attention=softmax(QK^T/sqrt(dk))V Q=XWq...","write on board","Must"],
    ["4","Multi-head?","h heads parallel different relation, concat+project.","h=8","Should"],
    ["5","Positional encoding?","Attention no order. Add sin/cos.","PE sin","Should"],
    ["6","Token? Embedding?","Token piece (BPE). Embedding word->vector.","Chat+GPT","Must"],
    ["7","Training 3 steps?","1) Pretrain next-token 2) SFT 3) RLHF.","Pretrain->SFT->RLHF","Must"],
    ["8","Temperature / Top-p?","Temp 0 determin, >1 creative. Top-p smallest set sum p.","temp 0.7","Must"],
    ["9","Context window? O(n2)?","Max tokens seen. Attn O(T2) 2x->4x.","4K vs 128K","Should"],
    ["10","Hallucination? RAG?","Fluent false. RAG search docs feed LLM.","Docs+LLM","Must"],
    ["11","Prompt vs Fine-tune?","Prompt better instructions. LoRA <1% params.","LoRA","Should"],
    ["12","Encoder vs Decoder?","Encoder bidir BERT, Decoder causal GPT. LLMs decoder-only.","GPT decoder","Should"],
]

pomodoro_rows = [
    ["1","Quote Pomodoro? Stack?","Tkinter Pomodoro 25/5,50/10,15/3, quotes, beeps, plyer.","flightproductivity.py 198","Must"],
    ["2","Threading model?","Main UI mainloop. Daemon sleep(1)->remaining--. root.after thread-safe.","daemon=True","Must"],
    ["3","Why root.after?","Tkinter not thread-safe. after schedules on main.","after(0,tick_ui)","Must"],
    ["4","Pause/Resume?","Flag is_paused. continue skip decrement.","toggle flag","Must"],
    ["5","Presets + progress?","PRESETS dict. Progress max=total value=total-remain.","PRESETS[\"25/5\"]","Should"],
    ["6","Sounds cross-platform?","winsound.Beep 800/600+450 else \\a.","HAS_WINSOUND","Should"],
    ["7","Quotes rotation?","10 quotes inc every 300s modulo.","QUOTES[(i+1)%len]","Should"],
    ["8","Hardest part?","Thread-safety + pause + mm:ss parse.","STAR","Must"],
    ["9","Improve?","CSV log, task field, auto-break, stats.","TODOs","Should"],
]

handsens_rows = [
    ["1","handsens101? Stack?","Webcam mouse Python OpenCV MediaPipe pyautogui.","github Anirudh-2810","Must"],
    ["2","Pipeline?","Cap0->MediaPipe 0.85->21 landmarks->map->smooth5.0->pyautogui.","detect-filter-map","Must"],
    ["3","Gestures?","Pinch click, index+middle scroll, move cursor.","pinch->click","Must"],
    ["4","Why 0.85 conf?","Cut false positives noise.","conf 0.85","Should"],
    ["5","Why smoothing 5.0?","Jitter. Exponential smooth stabilize.","filter","Must"],
    ["6","PAUSE=0 failsafe off?","Low latency. Tradeoff safety.","PAUSE=0","Should"],
    ["7","Hardest part?","Jitter/lighting. Fixed via smoothing.","good light","Must"],
    ["8","Extend?","ROS2 teleop, 2-hand, calibration.","robotics stack","Should"],
]
frontend_rows = [
    ["1","HTML vs CSS vs JS roles?","HTML structure, CSS presentation, JS behavior.","button + color + onclick","Must"],
    ["2","Semantic HTML? Why?","header/nav/main not div soup - SEO+a11y.","nav ul","Should"],
    ["3","Box model?","content+padding+border+margin. border-box.","box-sizing:border-box","Must"],
    ["4","Flex vs Grid?","Flex 1D row/col, Grid 2D layout. Responsive.","display:flex","Must"],
    ["5","Specificity?","inline>id>class>tag. !important breaks.","#id .class tag","Should"],
    ["6","let vs const vs var?","var hoisted avoid. let mutable, const binding immutable.","const a=[1] push ok","Must"],
    ["7","DOM + event handling?","DOM tree JS manipulates. listeners.","querySelector addEventListener","Must"],
    ["8","fetch + async/await?","fetch Promise. await fetch .json() CORS.","await fetch('/api')","Must"],
    ["9","Responsive design?","viewport + fluid rem/% + media queries.","@media 600px","Should"],
    ["10","Basic accessibility?","alt, label for, focus, contrast.","img alt","Should"],
]

story=[]
story.append(Paragraph("Interview Revision Sheet - Basic (Python | ML | LLM | 2 Repos)", s_title))
story.append(Paragraph("Anirudh Vijaykumar  |  1st Year B.Tech RAI, KJSCE  |  Odyssey Prep &nbsp;|&nbsp; English only  |  1 row = 30-sec answer: Definition - Why - When breaks", s_sub))
story.append(Paragraph(
    "How to use: Tonight filter <b>Must</b> only (about 30 rows). Speak each aloud &lt;60s. Set Status Done. Use skeleton not verbatim. For reports: explain via STAR: what you built - choice - rejected alternative + why - metric - failure fixed.",
    ParagraphStyle("tip", parent=s_cell, fontSize=6.5, textColor=HexColor("#444444"), leading=7.5, alignment=TA_LEFT, borderPadding=(4,4,4), backColor=HexColor("#FFF2CC"))
))
story.append(Spacer(1,4))

def section(title, subtitle, rows, widths, fill):
    story.append(Paragraph(title, ParagraphStyle("sec", parent=s_h2, textColor=fill, fontSize=9, leading=10)))
    story.append(Paragraph(subtitle, ParagraphStyle("secsub", parent=s_cell, fontSize=6.2, textColor=MUTED, leading=7)))
    story.append(hr(fill))
    # build header + data with Paragraphs
    header = [P("<b>#</b>", s_header_cell), P("<b>Question</b>", s_header_cell), P("<b>30-sec Answer (Memorize)</b>", s_header_cell), P("<b>Example / Code</b>", s_header_cell), P("<b>Pri</b>", s_header_cell)]
    data = [header]
    for r in rows:
        # r has 5 cols: #, Q, Answer, Example, Pri ; Status omitted for print
        data.append([
            P(r[0], ParagraphStyle("c", parent=s_cell, alignment=TA_CENTER)),
            P(f"<b>{r[1]}</b>", s_cell_b),
            P(r[2], s_cell),
            P(f"<font face=\"Courier\" size=\"5.5\">{r[3]}</font>", s_cell_small),
            P(r[4], ParagraphStyle("pri", parent=s_cell, alignment=TA_CENTER, textColor=HexColor("#9C0006") if r[4]=="Must" else HexColor("#375623"), fontName="Helvetica-Bold")),
        ])
    t = make_table(data, widths, fill)
    story.append(t)
    story.append(Spacer(1,6))

# Widths tuned for A4 landscape: total ~277mm, margins 10mm each => 190mm usable landscape? Actually A4 landscape 297-20=277. Split: # 10, Q 55, Ans 85, Ex 50, Pri 14
# Use portrait: 210-24=186. So landscape better. We'll use landscape via pagesize A4 landscape? Keep portrait but narrower. Let's do portrait widths sum 186
portrait_widths = [10*mm, 44*mm, 72*mm, 42*mm, 14*mm]
# Actually use landscape for tables: set pagesize to A4 landscape via doc
# We'll build doc landscape

section("01 - PYTHON BASIC  (27 Qs)  -  Must-know + where variables live", "Types, mutability, slicing, comprehension, dict, args, copy, GIL, venv + 9 new: private heap, stack vs heap, id/refcount, cache, dynamic typing, alias, GC, namespaces, everything is object.", python_rows, portrait_widths, ACCENT)
section("02 - ML BASIC  (12 Qs)", "Types, classification vs regression, train/test, overfit, prec/rec, confusion matrix, CV, scaling.", ml_rows, portrait_widths, BLUE)
section("03 - LLM BASIC  (12 Qs)", "Transformer idea, attention formula, multi-head, positional, token/embedding, training SFT/RLHF, temp/top-p, RAG, hallucination.", llm_rows, portrait_widths, GREEN)
section("04 - REPO: Quote Pomodoro  (9 Qs)  -  flightproductivity.py", "Tkinter + daemon thread + root.after pattern. Be ready to whiteboard threading diagram.", pomodoro_rows, portrait_widths, DARK)
section("05 - REPO: handsens101  (8 Qs)  -  github.com/Anirudh-2810/handsens101", "OpenCV + MediaPipe 0.85 + smooth 5.0 + pyautogui. Perception -> filter -> map -> actuate.", handsens_rows, portrait_widths, GOLD)
FRONTEND = HexColor("#9E4D2E")
section("06 - FRONTEND BASIC  (10 Qs)", "HTML/CSS/JS roles, semantic, box model, flex vs grid, specificity, let/const/var, DOM/events, fetch/async, responsive, a11y.", frontend_rows, portrait_widths, FRONTEND)

story.append(Spacer(1,6))
story.append(Paragraph(
    "Last page tip for Odyssey: When asked 'Tell me about your project' use 60-sec STAR for each repo: (S) Problem you solved for yourself, (T) Stack, (A) Hardest part + fix (thread-safety / jitter), (R) What you shipped + 1 improvement you would do next (CSV log for Pomodoro, ROS2 for handsens). Keep demo ready: video 20s screen-record on phone.",
    ParagraphStyle("tip2", parent=s_cell, fontSize=6.5, leading=7.5, backColor=HexColor("#E2EFDA"), borderPadding=(5,5,5), textColor=HexColor("#375623"))
))

doc = SimpleDocTemplate(
    OUT,
    pagesize=A4,  # portrait fits better for printing; tables still fit with widths above
    leftMargin=9*mm,
    rightMargin=9*mm,
    topMargin=8*mm,
    bottomMargin=10*mm,
    title="Interview Revision Sheet - Basic - Python LLM ML + 2 Repos",
    author="Anirudh Vijaykumar",
)

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 6)
    canvas.setFillColor(HexColor("#888888"))
    canvas.drawCentredString(A4[0]/2, 8*mm, f"Anirudh Vijaykumar  |  First-Year B.Tech RAI, KJSCE  |  Odyssey Prep  |  Page {doc.page}  |  github.com/Anirudh-2810")
    canvas.setStrokeColor(BORDER)
    canvas.line(9*mm, 9*mm, A4[0]-9*mm, 9*mm)
    canvas.restoreState()

doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(f"SAVED -> {OUT}")
import pathlib, pymupdf
p = pathlib.Path(OUT)
print("size", p.stat().st_size)
d = pymupdf.open(str(p))
print("pages", len(d))
print(d[0].get_text()[:600].replace("\n"," | "))
# Verify key needles
txt = "".join([pg.get_text() for pg in d])
for needle in ["PYTHON BASIC","LLM BASIC","Quote Pomodoro","handsens101","Odyssey"]:
    print(needle, needle in txt)

