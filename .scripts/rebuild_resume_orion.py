#!/usr/bin/env python3
"""Orion Coding Club resume - 1st Year B.Tech, no Apple, professional, English only"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether
from reportlab.lib.styles import ParagraphStyle

OUT_MAIN = r"C:\Users\Vijaykumar\Second-Brain\Second-Brain\raw-sources\Anirudhcv101.pdf"
OUT_ORION = r"C:\Users\Vijaykumar\Second-Brain\Second-Brain\raw-sources\Anirudhcv101_Orion.pdf"
OUT_BACKUP_RETAIL = r"C:\Users\Vijaykumar\Second-Brain\Second-Brain\raw-sources\Anirudhcv101_Retail_Apple.pdf"

NAVY = HexColor("#0F2A44")
ACCENT = HexColor("#1F4E78")
GREY = HexColor("#2B2B2B")
LGREY = HexColor("#5A5A5A")
MUTED = HexColor("#666666")

def styles():
    s={}
    s["name"] = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=17, textColor=NAVY, alignment=TA_CENTER, leading=18, spaceAfter=2)
    s["contact"] = ParagraphStyle("contact", fontName="Helvetica", fontSize=7.2, textColor=HexColor("#444444"), alignment=TA_CENTER, leading=9, spaceAfter=4)
    s["heading"] = ParagraphStyle("heading", fontName="Helvetica-Bold", fontSize=8.2, textColor=NAVY, spaceBefore=5, spaceAfter=1, leading=10)
    s["body"] = ParagraphStyle("body", fontName="Helvetica", fontSize=7.25, textColor=GREY, alignment=TA_JUSTIFY, leading=9.1, spaceAfter=1)
    s["bullet"] = ParagraphStyle("bullet", fontName="Helvetica", fontSize=7.25, textColor=GREY, leftIndent=10, bulletIndent=3, leading=9.1, spaceAfter=1)
    s["bullet_small"] = ParagraphStyle("bullet_small", fontName="Helvetica", fontSize=7.0, textColor=GREY, leftIndent=14, bulletIndent=6, leading=8.8, spaceAfter=0.7)
    s["sub"] = ParagraphStyle("sub", fontName="Helvetica-Bold", fontSize=7.7, textColor=HexColor("#1A1A1A"), leading=9.5, spaceAfter=0.5, spaceBefore=2)
    s["sub_detail"] = ParagraphStyle("sub_detail", fontName="Helvetica", fontSize=7.0, textColor=MUTED, leading=8.6, spaceAfter=0.8)
    s["edu_line"] = ParagraphStyle("edu_line", fontName="Helvetica-Bold", fontSize=7.4, textColor=HexColor("#1A1A1A"), leading=9, spaceAfter=0.3)
    s["edu_detail"] = ParagraphStyle("edu_detail", fontName="Helvetica", fontSize=7.0, textColor=MUTED, leading=8.6, spaceAfter=1)
    return s

def hr():
    return HRFlowable(width="100%", thickness=0.6, color=ACCENT, spaceAfter=2, spaceBefore=0)

def heading(text, st):
    return [Paragraph(f'<font color="#0F2A44">{text}</font>', st["heading"]), hr()]

def bullet(text, st):
    return Paragraph(f'<bullet>-</bullet>{text}', st["bullet"])

def bullet_small(text, st):
    return Paragraph(f'<bullet>-</bullet>{text}', st["bullet_small"])

S = styles()
story=[]

# Header
story.append(Paragraph("ANIRUDH VIJAYKUMAR", S["name"]))
story.append(Paragraph(
    'First-Year B.Tech - Robotics and Artificial Intelligence | K. J. Somaiya College of Engineering, Mumbai<br/>'
    'Mumbai, Maharashtra &nbsp;|&nbsp; +91-8828029983 &nbsp;|&nbsp; vkanirudh28@gmail.com &nbsp;|&nbsp; linkedin.com/in/anirudh-vijay-kumar-1264803b9 &nbsp;|&nbsp; github.com/Anirudh-2810',
    S["contact"]
))

# Objective / Summary - Orion focused
story.extend(heading("OBJECTIVE", S))
story.append(Paragraph(
    "First-year B.Tech (Robotics and Artificial Intelligence) student seeking to join <b>Orion Coding Club</b> as an active builder and collaborator. "
    "Hands-on Python developer with two shipped personal projects spanning human-computer interaction and productivity tooling, and a strong foundation in programming logic, object-oriented design, and data structures. "
    "Active peer mentor who breaks down technical concepts into simple steps and contributes consistently to team problem-solving. Eager to learn, build, and contribute to Orion's hackathons, open-source sprints, and peer-learning culture.",
    S["body"]
))

# Technical Skills - replaces Apple/Core Competencies
story.extend(heading("TECHNICAL SKILLS", S))
story.append(Paragraph(
    "<b>Languages:</b> Python (proficient), C++ (foundations), SQL (basics) &nbsp;|&nbsp; <b>Libraries:</b> OpenCV, MediaPipe, Tkinter, pyautogui, threading",
    S["body"]
))
story.append(Paragraph(
    "<b>CS Fundamentals:</b> Data Structures, OOP (classes, inheritance, dunders), File I/O, Error Handling, Git/GitHub, venv/pip, Debugging with breakpoint()",
    S["body"]
))
story.append(Paragraph(
    "<b>Tools:</b> VS Code, Git, GitHub, Windows, SQLite (basics), plyer notifications &nbsp;|&nbsp; <b>Strengths:</b> Clear technical explanation, active listening, team collaboration, fast learner, inclusive mindset",
    S["body"]
))

# Projects - critical for coding club
story.extend(heading("PROJECTS", S))

# handsens101
story.append(Paragraph("handsens101 - Hand-Gesture Mouse Control | Python, OpenCV, MediaPipe, pyautogui", S["sub"]))
story.append(Paragraph("<i>GitHub: github.com/Anirudh-2810/handsens101</i> &nbsp;|&nbsp; Webcam-based HCI controller replacing the mouse", S["sub_detail"]))
story.append(bullet_small("Built perception-to-action loop: OpenCV capture -> MediaPipe HandLandmarker (1 hand, confidence 0.85) -> 21 landmarks mapped to screen -> exponential smoothing (factor 5.0) -> pyautogui actuation.", S))
story.append(bullet_small("Implemented 3 gestures: pinch (index+thumb) = click, index+middle = scroll, hand movement = cursor; state machine tracks drag and scroll state.", S))
story.append(bullet_small("Solved sensor noise and jitter via confidence tuning and smoothing before actuation - same filtering intuition as robotics state estimation; extensible to ROS2 teleoperation.", S))

# Quote Pomodoro
story.append(Paragraph("Quote Pomodoro - Dark-Mode Focus Timer | Python, Tkinter, threading, winsound", S["sub"]))
story.append(Paragraph("<i>Source: flightproductivity.py (198 lines) &nbsp;|&nbsp; Personal productivity desktop app</i>", S["sub_detail"]))
story.append(bullet_small("Built distraction-free Pomodoro timer with editable mm:ss input, presets 25/5, 50/10, 15/3, progress bar, rotating motivational quotes, and Windows beeps/toast notifications.", S))
story.append(bullet_small("Solved Tkinter thread-safety (Tkinter is not thread-safe) using daemon timer thread + root.after() for UI updates; pause/resume preserves remaining time, reset restores preset.", S))

# Certifications
story.extend(heading("CERTIFICATIONS", S))
story.append(bullet("CS50's Introduction to Programming with Python (CS50P) - HarvardX / edX", S))
story.append(bullet("Artificial Intelligence Fundamentals - IBM SkillsBuild", S))
story.append(bullet("Fundamentals of Machine Learning and Artificial Intelligence - Coursera", S))

# Academic & Peer Leadership - keep but reframe
story.extend(heading("LEADERSHIP &amp; COLLABORATION", S))
story.append(Paragraph("Peer Mentor &amp; Collaborator | 2025 - Present", S["sub"]))
story.append(bullet("Mentor classmates in Python/C++ logic and coursework by breaking concepts into step-by-step explanations; run informal peer debug sessions.", S))
story.append(bullet("Collaborate in study groups and build sessions, encouraging inclusive input and shared problem-solving; independently completed online certifications to broaden software depth.", S))

# Education - with percentages as requested
story.extend(heading("EDUCATION", S))
story.append(Paragraph("K. J. Somaiya College of Engineering, Mumbai", S["edu_line"]))
story.append(Paragraph(
    "Bachelor of Technology (B.Tech) in Robotics and Artificial Intelligence (RAI) - First Year (from August 2026)<br/>"
    "<i>Coursework: Programming in Python &amp; C++, Data Structures, Technical Communication, Human-Computer Interaction.</i>",
    S["edu_detail"]
))
story.append(Spacer(1,2))
story.append(Paragraph("Ryan International School, Sanpada - Higher Secondary Education (Grades 11-12)", S["edu_line"]))
story.append(Paragraph("2024 - 2026 &nbsp;|&nbsp; <b>65% in Grade 12</b>", S["edu_detail"]))
story.append(Spacer(1,2))
story.append(Paragraph("Our Lady of Perpetual Succour (OLPS) High School, Mumbai - Primary &amp; Secondary Education (Sr. KG - Grade 10)", S["edu_line"]))
story.append(Paragraph("Till 2024 &nbsp;|&nbsp; <b>85% in Grade 10</b>", S["edu_detail"]))

# Commitment - club appropriate
story.extend(heading("COMMITMENT", S))
story.append(Paragraph(
    "Available for regular Orion meetings, weekend build sprints, hackathons, and peer-learning sessions. Committed to consistent contribution, code reviews, and collaborative projects; aligns with Orion's build-and-learn culture.",
    S["body"]
))

def build_pdf(path):
    doc = SimpleDocTemplate(
        path,
        pagesize=A4,
        leftMargin=12*mm,
        rightMargin=12*mm,
        topMargin=9*mm,
        bottomMargin=9*mm,
        title="Anirudh Vijaykumar - Resume - Orion Coding Club",
        author="Anirudh Vijaykumar",
    )
    def footer(c, d):
        c.saveState()
        c.setFont("Helvetica", 6)
        c.setFillColor(MUTED)
        c.drawCentredString(A4[0]/2, 10*mm, "Anirudh Vijaykumar  |  github.com/Anirudh-2810  |  vkanirudh28@gmail.com")
        c.restoreState()
    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    print(f"SAVED -> {path}")

# Backup current retail version if not already
import pathlib, shutil
src = pathlib.Path(OUT_MAIN)
if src.exists():
    # Only backup once - don't overwrite retail backup if exists
    retail_backup = pathlib.Path(OUT_BACKUP_RETAIL)
    if not retail_backup.exists():
        shutil.copy2(src, retail_backup)
        print(f"retail backup -> {retail_backup}")
    else:
        print(f"retail backup already exists -> {retail_backup}")

# Build both outputs (club version as main + distinct Orion file)
build_pdf(OUT_ORION)
# Also update main CV to Orion version (so default CV is club-ready)
shutil.copy2(OUT_ORION, OUT_MAIN)
print(f"copied Orion -> main CV {OUT_MAIN}")

# Verify
import pymupdf
for p in [OUT_MAIN, OUT_ORION]:
    d = pymupdf.open(p)
    txt = d[0].get_text()
    print("---", p)
    print("pages", len(d), "size", pathlib.Path(p).stat().st_size)
    for needle in ["Orion", "handsens101", "Pomodoro", "85% in Grade 10", "65% in Grade 12", "Apple"]:
        print(f"  {needle}: {needle in txt}")
    # check no weird char
    print("  bad char:", "�" in txt)
    print(txt[:500].replace("\n"," | "))
