#!/usr/bin/env python3
"""Simple Words Interview Cheat Sheet - Odyssey Prep - plain English, no big terms"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
from reportlab.lib import colors

OUT = r"C:\Users\Vijaykumar\Second-Brain\Second-Brain\raw-sources\Simple_Cheatsheet_Odyssey.pdf"

NAVY = HexColor("#0F2A44")
ACCENT = HexColor("#1F4E78")
TEAL = HexColor("#0B6B4A")
DARK = HexColor("#333333")
MUTED = HexColor("#666666")
LGREY = HexColor("#F2F2F2")
BORDER = HexColor("#B4C6E7")
YELLOW_BG = HexColor("#FFF2CC")
GREEN_BG = HexColor("#E2EFDA")
BLUE_BG = HexColor("#D9E1F2")
ORANGE_BG = HexColor("#FCE4D6")

styles = getSampleStyleSheet()
s_title = ParagraphStyle("title", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=15, textColor=NAVY, alignment=TA_CENTER, leading=16, spaceAfter=2)
s_sub = ParagraphStyle("sub", parent=styles["Normal"], fontName="Helvetica", fontSize=7.2, textColor=HexColor("#555555"), alignment=TA_CENTER, leading=8, spaceAfter=4)
s_h1 = ParagraphStyle("h1", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=10, textColor=colors.white, leading=11)
s_h2 = ParagraphStyle("h2", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=8.5, textColor=NAVY, leading=10, spaceBefore=5, spaceAfter=2)
s_h3 = ParagraphStyle("h3", parent=styles["Heading3"], fontName="Helvetica-Bold", fontSize=7.5, textColor=ACCENT, leading=9, spaceBefore=4, spaceAfter=1)
s_body = ParagraphStyle("body", parent=styles["Normal"], fontName="Helvetica", fontSize=7.0, textColor=DARK, leading=8.5, alignment=TA_JUSTIFY, spaceAfter=1.5)
s_bullet = ParagraphStyle("bullet", parent=s_body, leftIndent=10, bulletIndent=3, leading=8.5, spaceAfter=0.8)
s_cell = ParagraphStyle("cell", parent=styles["Normal"], fontName="Helvetica", fontSize=6.2, textColor=DARK, leading=7.0, alignment=TA_LEFT, spaceAfter=0)
s_cell_b = ParagraphStyle("cell_b", parent=s_cell, fontName="Helvetica-Bold", fontSize=6.2, textColor=HexColor("#1A1A1A"))
s_cell_small = ParagraphStyle("cell_small", parent=s_cell, fontSize=6.0, leading=6.6)
s_header_cell = ParagraphStyle("header_cell", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=6.1, textColor=colors.white, leading=6.8, alignment=TA_CENTER)
s_tip = ParagraphStyle("tip", parent=s_body, fontSize=6.4, textColor=HexColor("#444444"), leading=7.2, alignment=TA_LEFT, borderPadding=(4,4,4), backColor=YELLOW_BG, spaceAfter=3)
s_green = ParagraphStyle("tipg", parent=s_tip, backColor=GREEN_BG, textColor=HexColor("#375623"))
s_blue = ParagraphStyle("tipb", parent=s_tip, backColor=BLUE_BG, textColor=NAVY)

def hr(color):
    return HRFlowable(width="100%", thickness=1.0, color=color, spaceAfter=3, spaceBefore=1)

def P(text, style=s_cell):
    text = text.replace("&", "&amp;")
    return Paragraph(text, style)

def make_table(rows, col_widths, header_fill):
    t = Table(rows, colWidths=col_widths, repeatRows=1)
    style = [
        ("BACKGROUND", (0,0), (-1,0), header_fill),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,0), 6.1),
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

story=[]
story.append(Paragraph("Simple Interview Cheat Sheet — Odyssey Prep", s_title))
story.append(Paragraph("Anirudh Vijaykumar  |  1st Year B.Tech RAI, KJSCE  |  Odyssey  |  Plain English — no big terms — say in your own words", s_sub))
story.append(Paragraph(
    "How to use: Read yellow boxes aloud once. Each table row = 30-sec answer. Say <b>Simple Definition → Why useful → What goes wrong</b>. Don’t memorise word-for-word — use skeleton. For projects, use 60-sec STAR at bottom.",
    s_tip
))

# Section 0 - Resume quick
story.append(Paragraph("0 — YOUR RESUME IN 30 SEC (what it says)", s_h2))
story.append(hr(ACCENT))
story.append(Paragraph(
    "<b>Top:</b> 1st Year B.Tech RAI, KJSCE Mumbai — wants to join <b>Odyssey</b> coding club as builder + learner. "
    "<b>Skills:</b> Python (good), C++ (basic), SQL (basic) — Libraries: OpenCV, MediaPipe, Tkinter, pyautogui, threading — Basics: Data Structures, OOP (classes), File handling, <b>Error Handling (try/except)</b>, Git/GitHub, debugging with breakpoint() — "
    "<b>Strengths:</b> Eager to Learn, Growth Mindset, Fast Learner, explains clearly, listens, teamwork, adaptable. "
    "<b>Projects:</b> handsens101 (hand mouse) + Quote Pomodoro (focus timer). "
    "<b>Certs:</b> CS50P Harvard, IBM AI, Coursera ML. "
    "<b>Education:</b> KJSCE RAI (Aug 2026), Ryan 65% in 12th, OLPS 85% in 10th. "
    "<b>Commitment:</b> Free for regular Odyssey meets, weekend builds, hackathons.",
    s_body
))
story.append(Paragraph(
    "<b>30-sec self-intro to say:</b> “I’m 1st year RAI at KJSCE. I know Python well, made 2 small projects — a hand mouse and a focus timer. I’m eager to learn, I pick up new tools fast, I like explaining and helping friends. I want to join Odyssey to learn from seniors and build in hackathons.”",
    s_green
))

# Section 1 - handsens101 simple
story.append(Paragraph("1 — PROJECT: handsens101 — Hand Mouse (say simply)", s_h2))
story.append(Paragraph("GitHub: github.com/Anirudh-2810/handsens101 — Replaces mouse with hand in front of webcam", ParagraphStyle("sub2", parent=s_body, fontSize=6.5, textColor=MUTED, leading=7)))
story.append(hr(ACCENT))
story.append(Paragraph("5 steps — like story:", s_h3))
story.append(Paragraph("<b>1. Camera on</b> — cv2 opens webcam (camera 0), gets frames ~30 per sec.", s_bullet))
story.append(Paragraph("<b>2. Find hand</b> — MediaPipe (Google tool) finds hand, gives 21 points (fingertip joints). We set 1 hand only, 85% sure → so it ignores random background.", s_bullet))
story.append(Paragraph("<b>3. Hand position → screen position</b> — tiny numbers 0-1 become full screen: hand_x * screen_width. Full frame = full screen.", s_bullet))
story.append(Paragraph("<b>4. Make it smooth (5.0)</b> — Real hand shakes → cursor shakes. Smoothing = don’t jump, glide slowly. Like: new cursor = old * some + new * some (heavy smooth 5.0). Same idea as filtering noise in robotics.", s_bullet))
story.append(Paragraph("<b>5. Move real mouse</b> — pyautogui moves real cursor, does click/scroll. PAUSE=0 means no delay → fast.", s_bullet))
story.append(Paragraph("<b>3 gestures:</b> Thumb + index pinch close = click | Index + middle together = scroll | Just move hand = cursor moves. Code remembers drag/scroll so it doesn’t click again and again.", s_body))
story.append(Paragraph("<b>Simple error handling (what can go wrong):</b> No hand / bad light → do nothing, wait next frame (no crash). Wrong detection → 85% blocks it. Shaking → smoothing fixes. Missing hand_landmarker.task file → auto-downloads first time. Fast movement → may be too sensitive (trade-off of PAUSE=0).", s_blue))

# handsens Q table simple
handsens_simple = [
    ["1","What is handsens101?","Small webcam mouse. Python + OpenCV + MediaPipe + pyautogui. My GitHub.","Runs from src/main.py","Must"],
    ["2","5 steps?","Camera → find hand (0.85) → 21 points → map to screen → smooth 5.0 → move mouse","detect→filter→map→act","Must"],
    ["3","3 gestures?","Pinch = click, 2 fingers = scroll, move = cursor","pinch close","Must"],
    ["4","Why 85%?","Default 0.5 detects anything. 85 means only when really sure → less mistakes","less false","Should"],
    ["5","Why 5.0 smooth?","Without it shakes. With it glides slowly → stable","like filter","Must"],
    ["6","Hardest?","Shaking + light. Fixed via 85 + smooth. Needs good light.","good light demo","Must"],
    ["7","PAUSE=0?","No delay → fast. Safety off → faster but less safe","trade-off","Should"],
    ["8","Next?","Add 2 hands, ROS2 robot control, calibrate for screen","robotics mini","Should"],
]
header = [P("<b>#</b>", s_header_cell), P("<b>Question</b>", s_header_cell), P("<b>Say this (simple)</b>", s_header_cell), P("<b>Hint</b>", s_header_cell), P("<b>Pri</b>", s_header_cell)]
data = [header]
for r in handsens_simple:
    data.append([
        P(r[0], ParagraphStyle("c", parent=s_cell, alignment=TA_CENTER)),
        P(f"<b>{r[1]}</b>", s_cell_b),
        P(r[2], s_cell),
        P(f"<font face=\"Courier\" size=\"5.5\">{r[3]}</font>", s_cell_small),
        P(r[4], ParagraphStyle("pri", parent=s_cell, alignment=TA_CENTER, textColor=HexColor("#9C0006") if r[4]=="Must" else HexColor("#375623"), fontName="Helvetica-Bold")),
    ])
story.append(make_table(data, [10*mm, 42*mm, 74*mm, 42*mm, 14*mm], ACCENT))
story.append(Spacer(1,2))
story.append(Paragraph("<b>60-sec STAR to say:</b> “I wanted mouse without touching. Used Python OpenCV MediaPipe pyautogui. Hard was shaking — fixed via 85 + smooth 5.0. Shipped 3 gestures on GitHub; next would do ROS2 teleop.”", s_green))

# Section 2 - Pomodoro simple
story.append(Paragraph("2 — PROJECT: Quote Pomodoro — Focus Timer (say simply)", s_h2))
story.append(Paragraph("Source: flightproductivity.py (198 lines) — Black + green timer with quotes + beep", ParagraphStyle("sub2", parent=s_body, fontSize=6.5, textColor=MUTED, leading=7)))
story.append(hr(TEAL))
story.append(Paragraph("How it works — 2 workers story:", s_h3))
story.append(Paragraph("<b>Worker 1 = UI worker:</b> Shows window (Tkinter). Has time box 25:00, 3 preset buttons (25/5, 50/10, 15/3), progress bar, quotes.", s_bullet))
story.append(Paragraph("<b>Worker 2 = Timer worker:</b> Sleeps 1 sec, does remaining -=1. Runs in background with daemon=True (so it dies if you close window).", s_bullet))
story.append(Paragraph("<b>Why root.after?</b> Simple: only Worker 1 can change window. If Worker 2 touches window directly, it crashes. So Worker 2 passes chit: root.after(0, tick_ui) → Worker 1 updates label/progress. Like passing note.", s_bullet))
story.append(Paragraph("<b>Pause simple:</b> Flag is_paused. Pause → True → timer does ‘continue’ (skip counting, keep remaining). Resume → False → counting resumes.", s_bullet))
story.append(Paragraph("<b>Reset:</b> Goes back to last preset. <b>Presets:</b> dictionary like 25*60 sec. <b>Progress:</b> value = total - remaining. <b>Quotes:</b> 10 quotes, change every 5 min with % wrap so never error.", s_bullet))
story.append(Paragraph("<b>Sounds:</b> Windows beep 800Hz start, 600+450 end. Other laptops just ‘ding’. Wrapped in try/except so no crash if no sound.", s_bullet))
story.append(Paragraph("<b>Simple error handling:</b> Wrong time like ‘abc’ → try split by ‘:’ fails → except sets back to 25:00 (no crash). Click Start twice → if running: return (no double timer). Close window → daemon dies (no stuck thread). No plyer → try/except skip popup. No winsound → bell fallback.", s_blue))

pomodoro_simple = [
    ["1","What is Pomodoro?","Black-green focus timer. 25/5 etc, quotes, beeps. Python Tkinter.","198 lines","Must"],
    ["2","2 workers?","Worker1 UI, Worker2 sleep 1 sec + count. Pass chit via root.after","daemon True","Must"],
    ["3","Why root.after?","Only UI worker can touch window. Else crash. After passes note safely.","after(0,tick)","Must"],
    ["4","Pause?","Flag is_paused. If True → continue (skip count). Keep remaining.","toggle flag","Must"],
    ["5","Presets?","Dict 25*60 etc. Progress = total - remaining","PRESETS","Should"],
    ["6","Sound?","Windows Beep 800/600 else ding. In try.","try check","Should"],
    ["7","Hardest?","Window freezing when timer touched UI → fixed via after + flags + try parse","STAR","Must"],
    ["8","Next?","Add CSV log, task name, auto-break, stats, tray","TODOs","Should"],
]
data = [header]
for r in pomodoro_simple:
    data.append([
        P(r[0], ParagraphStyle("c", parent=s_cell, alignment=TA_CENTER)),
        P(f"<b>{r[1]}</b>", s_cell_b),
        P(r[2], s_cell),
        P(f"<font face=\"Courier\" size=\"5.5\">{r[3]}</font>", s_cell_small),
        P(r[4], ParagraphStyle("pri", parent=s_cell, alignment=TA_CENTER, textColor=HexColor("#9C0006") if r[4]=="Must" else HexColor("#375623"), fontName="Helvetica-Bold")),
    ])
story.append(make_table(data, [10*mm, 42*mm, 74*mm, 42*mm, 14*mm], TEAL))
story.append(Spacer(1,2))
story.append(Paragraph("<b>60-sec STAR:</b> “I needed focus timer for study. Made with Tkinter+threading. Hard was window crash when timer updated — fixed via root.after chit + flags. Shipped 3 presets + quotes; next add CSV log + stats.”", s_green))

# Section 3 - Error handling overall
story.append(Paragraph("3 — ERROR HANDLING — simple (what they want to hear)", s_h2))
story.append(hr(HexColor("#7F6000")))
story.append(Paragraph("Error handling = think ‘what can go wrong’ and make code not crash.", s_body))
story.append(Paragraph("<b>handsens:</b> No hand → wait, don’t crash | Wrong light → 85 blocks | Shake → smooth fixes | Missing file → auto-download", s_bullet))
story.append(Paragraph("<b>Pomodoro:</b> Wrong time ‘abc’ → reset to 25:00 | Double Start → block | Close → daemon dies | No sound lib → fallback ding | No plyer → skip popup (try/except)", s_bullet))
story.append(Paragraph("<b>Frontend (JS):</b> fetch fails → try/catch + show fallback. Same idea.", s_bullet))
story.append(Paragraph("<b>Say if asked ‘what is error handling?’:</b> “I think what can go wrong — wrong input, no file, no net — and I write try/except or checks so it handles gently, not crash, shows fallback.”", s_green))

# Section 4 - Frontend simple
story.append(Paragraph("4 — FRONTEND QUICK — simple (for Odyssey web Qs)", s_h2))
story.append(Paragraph("HTML = structure (walls) | CSS = paint (color) | JS = behavior (on click do)", s_body))
story.append(hr(HexColor("#9E4D2E")))
frontend_simple = [
    ["1","What?","HTML walls, CSS paint, JS behavior. Together make page","button + color + onclick","Must"],
    ["2","Semantic?","Use &lt;nav&gt; &lt;header&gt; not just &lt;div&gt; — good for Google + screen readers","nav ul","Should"],
    ["3","Box?","Content + padding + border + margin. Use border-box to fix size","box-sizing","Must"],
    ["4","Flex vs Grid?","Flex = one line row/col (nav). Grid = rows+cols both (page). Both for phone","display:flex","Must"],
    ["5","let vs const?","var old don’t use. let can change, const box can’t change (but inside list push ok)","const a=[1] push","Must"],
    ["6","DOM?","Tree of page. JS finds with querySelector and listens click","addEventListener","Must"],
    ["7","fetch?","Call server for data. await fetch + try/catch if net fails","try fetch","Must"],
    ["8","Responsive?","Make phone friendly: viewport + % + @media 600px","@media","Should"],
    ["9","Error?","try fetch { if !ok throw } catch show fallback — same as Python","fallback","Should"],
]
data = [header]
for r in frontend_simple:
    data.append([
        P(r[0], ParagraphStyle("c", parent=s_cell, alignment=TA_CENTER)),
        P(f"<b>{r[1]}</b>", s_cell_b),
        P(r[2], s_cell),
        P(f"<font face=\"Courier\" size=\"5.5\">{r[3]}</font>", s_cell_small),
        P(r[4], ParagraphStyle("pri", parent=s_cell, alignment=TA_CENTER, textColor=HexColor("#9C0006") if r[4]=="Must" else HexColor("#375623"), fontName="Helvetica-Bold")),
    ])
story.append(make_table(data, [10*mm, 42*mm, 74*mm, 42*mm, 14*mm], HexColor("#9E4D2E")))
story.append(Spacer(1,3))
story.append(Paragraph("Tip for any Q: say 1 line definition → 1 why useful → 1 when breaks. Keep it simple, not big words. Example: “Flex is for arranging in one line — useful for nav bar — breaks if you need 2D then use Grid.”", s_tip))
story.append(Spacer(1,2))
story.append(Paragraph("Final tip for Odyssey: When they ask ‘tell me about project’, use STAR (S problem you solved for yourself, T tools, A hard + fix, R what you shipped + 1 next improvement). Keep 20-sec demo video ready on phone. And say eager to learn: ‘I’m quick to ramp, I take feedback, I help peers.’", ParagraphStyle("tipf", parent=s_tip, backColor=GREEN_BG, textColor=HexColor("#375623"))))

doc = SimpleDocTemplate(
    OUT,
    pagesize=A4,
    leftMargin=9*mm,
    rightMargin=9*mm,
    topMargin=8*mm,
    bottomMargin=10*mm,
    title="Simple Interview Cheat Sheet - Odyssey - Plain English",
    author="Anirudh Vijaykumar",
)
def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 6)
    canvas.setFillColor(HexColor("#888888"))
    canvas.drawCentredString(A4[0]/2, 8*mm, f"Anirudh Vijaykumar  |  1st Year B.Tech RAI, KJSCE  |  Odyssey — Simple Words Prep  |  Page {doc.page}  |  github.com/Anirudh-2810")
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
txt0 = d[0].get_text()[:800].replace("\n"," | ")
try:
    print(txt0)
except UnicodeEncodeError:
    print(txt0.encode("ascii","ignore").decode())
txt = "".join([pg.get_text() for pg in d])
for needle in ["handsens101", "Pomodoro", "Error handling", "FRONTEND", "Odyssey"]:
    print(needle, needle in txt)
# check no odyssey missing
if len(d) > 3:
    print("WARNING pages", len(d))
