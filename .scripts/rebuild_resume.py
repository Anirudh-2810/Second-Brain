#!/usr/bin/env python3
"""Rebuild Anirudhcv101.pdf with updated education percentages - English only, no additions beyond 85% / 65%"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors

OUT = r"C:\Users\Vijaykumar\Second-Brain\Second-Brain\raw-sources\Anirudhcv101.pdf"
# Use millimeter margins to fit 1 page exactly like original
PAGE_W, PAGE_H = A4

# Colors matching original - dark navy headings
NAVY = HexColor("#0F2A44")
ACCENT = HexColor("#1F4E78")
LIGHT_BG = HexColor("#F2F2F2")
GREY_TEXT = HexColor("#333333")
LIGHT_GREY = HexColor("#666666")

def make_styles():
    s = {}
    s["name"] = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=16, textColor=NAVY, alignment=TA_CENTER, spaceAfter=2, leading=18)
    s["contact"] = ParagraphStyle("contact", fontName="Helvetica", fontSize=7.2, textColor=HexColor("#444444"), alignment=TA_CENTER, spaceAfter=6, leading=9)
    s["contact_link"] = ParagraphStyle("contact_link", fontName="Helvetica", fontSize=7.2, textColor=ACCENT, alignment=TA_CENTER, leading=9)
    s["heading"] = ParagraphStyle("heading", fontName="Helvetica-Bold", fontSize=8.5, textColor=NAVY, spaceBefore=7, spaceAfter=3, leading=10, borderPadding=(0,0,2))
    s["subheading"] = ParagraphStyle("subheading", fontName="Helvetica-Bold", fontSize=7.8, textColor=HexColor("#222222"), spaceBefore=3, spaceAfter=1, leading=9.5)
    s["body"] = ParagraphStyle("body", fontName="Helvetica", fontSize=7.3, textColor=GREY_TEXT, alignment=TA_JUSTIFY, spaceAfter=1.2, leading=9.2)
    s["bullet"] = ParagraphStyle("bullet", fontName="Helvetica", fontSize=7.3, textColor=GREY_TEXT, leftIndent=10, bulletIndent=3, spaceAfter=1, leading=9.2)
    s["small"] = ParagraphStyle("small", fontName="Helvetica", fontSize=7.1, textColor=GREY_TEXT, leading=9)
    s["edu_line"] = ParagraphStyle("edu_line", fontName="Helvetica-Bold", fontSize=7.4, textColor=HexColor("#1A1A1A"), leading=9.2, spaceAfter=0.5)
    s["edu_detail"] = ParagraphStyle("edu_detail", fontName="Helvetica", fontSize=7.1, textColor=LIGHT_GREY, leading=9, leftIndent=0, spaceAfter=1)
    return s

def hr():
    return HRFlowable(width="100%", thickness=0.6, color=ACCENT, spaceAfter=2, spaceBefore=0)

def section_heading(text, styles):
    return [Paragraph(f'<font color="#0F2A44">{text}</font>', styles["heading"]), hr()]

def bullet(text, styles):
    return Paragraph(f'<bullet>-</bullet>{text}', styles["bullet"])

styles = make_styles()

story = []
# Name
story.append(Paragraph("ANIRUDH VIJAYKUMAR", styles["name"]))
# Contact line - single centered line with separators
contact_html = (
    'Location: Mumbai, Maharashtra, India &nbsp;|&nbsp; Phone: +91-8828029983 &nbsp;|&nbsp; Email: vkanirudh28@gmail.com<br/>'
    'LinkedIn: linkedin.com/in/anirudh-vijay-kumar-1264803b9 &nbsp;|&nbsp; GitHub: github.com/Anirudh-2810'
)
story.append(Paragraph(contact_html, styles["contact"]))
story.append(Spacer(1, 1))

# PROFESSIONAL SUMMARY
story.extend(section_heading("PROFESSIONAL SUMMARY", styles))
story.append(Paragraph(
    "Incoming First-Year B.Tech student with hands-on experience in delivering user-driven solutions, a strong understanding of the Apple "
    "ecosystem, and solid grounding in computer science fundamentals. Strong active listener with a talent for simplifying technical concepts "
    "and helping peers navigate new technology. Eager to leverage strong interpersonal skills, a fast learning curve, and an inclusive mindset "
    "to deliver exceptional customer service, build brand loyalty, and create lasting owners of Apple products and services as a Part-Time Specialist.",
    styles["body"]
))

# CORE COMPETENCIES
story.extend(section_heading("CORE COMPETENCIES &amp; SKILLS", styles))
story.append(Paragraph(
    '<b>Customer Engagement &amp; Service:</b> Active Listening, Needs Assessment, Clear Technical Explanation, Problem Solving, Relationship Building, Multitasking, Handling Sensitive Customer Data, Product Demonstrations.',
    styles["body"]
))
story.append(Paragraph(
    '<b>Apple Ecosystem Knowledge:</b> macOS, iOS, iPadOS, watchOS, iCloud, Apple Services Integration.',
    styles["body"]
))
story.append(Paragraph(
    '<b>Technical Foundation:</b> Python, C++, Artificial Intelligence Fundamentals, Machine Learning Concepts, Data Structures.',
    styles["body"]
))
story.append(Paragraph(
    '<b>Personal Attributes:</b> Adaptability, Team Collaboration, Inclusive Mindset, Fast Learner, High Energy, Communication.',
    styles["body"]
))

# CERTIFICATIONS
story.extend(section_heading("CERTIFICATIONS &amp; CREDENTIALS", styles))
story.append(bullet("CS50's Introduction to Programming with Python (CS50P) | HarvardX / edX", styles))
story.append(bullet("Artificial Intelligence Fundamentals | IBM SkillsBuild", styles))
story.append(bullet("Fundamentals of Machine Learning and Artificial Intelligence | Coursera", styles))

# ACADEMIC & PEER LEADERSHIP
story.extend(section_heading("ACADEMIC &amp; PEER LEADERSHIP", styles))
story.append(Paragraph("Engineering Student &amp; Peer Collaborator | 2025 - Present", styles["subheading"]))
story.append(bullet(
    "<b>Technical Guidance:</b> Frequently assist classmates in understanding introductory programming logic (Python/C++) and coursework concepts by breaking them down into simple, step-by-step explanations.",
    styles
))
story.append(bullet(
    "<b>Collaborative Problem Solving:</b> Work effectively in study groups to solve technical problems, encouraging input from all team members and fostering an inclusive learning environment.",
    styles
))
story.append(bullet(
    "<b>Continuous Self-Learning:</b> Independently completed online certifications from HarvardX, IBM, and Coursera to broaden understanding of software and modern technology ecosystems.",
    styles
))

# EDUCATION - UPDATED with percentages only (English, no additions per approval)
story.extend(section_heading("EDUCATION", styles))
# KJ Somaiya
story.append(Paragraph("K. J. Somaiya College of Engineering, Mumbai", styles["edu_line"]))
story.append(Paragraph(
    "Bachelor of Technology (B.Tech) in Robotics and Artificial Intelligence (RAI) | First Year (Starting August 17, 2026)<br/>"
    "<i>Relevant Coursework &amp; Projects: Programming in Python &amp; C++, Data Structures, Technical Communication, Human-Computer Interaction (Class Projects).</i>",
    styles["edu_detail"]
))
story.append(Spacer(1, 3))
# Ryan - 11th-12th with 65% in 12th
story.append(Paragraph("Ryan International School, Mumbai | Higher Secondary Education (Grades 11-12)", styles["edu_line"]))
story.append(Paragraph(
    "2024 - 2026 &nbsp;|&nbsp; <b>65% in Grade 12</b>",
    styles["edu_detail"]
))
story.append(Spacer(1, 3))
# OLPS - till 10th with 85% in 10th
story.append(Paragraph("Our Lady of Perpetual Succour (OLPS) High School, Mumbai | Primary &amp; Secondary Education (Sr. KG - Grade 10)", styles["edu_line"]))
story.append(Paragraph(
    "Till 2024 &nbsp;|&nbsp; <b>85% in Grade 10</b>",
    styles["edu_detail"]
))

# AVAILABILITY
story.extend(section_heading("AVAILABILITY &amp; COMMITMENT", styles))
story.append(Paragraph(
    "<b>Part-Time Retail Roster:</b> Fully available for evening shifts (post-college hours), weekends, public holidays, and peak retail periods as required by store needs.",
    styles["body"]
))

# Build with tight margins to keep 1 page
doc = SimpleDocTemplate(
    OUT,
    pagesize=A4,
    leftMargin=14*mm,
    rightMargin=14*mm,
    topMargin=10*mm,
    bottomMargin=10*mm,
    title="Anirudh Vijaykumar - CV",
    author="Anirudh Vijaykumar",
)

# Footer function for page number if needed (kept minimal)
def add_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 6)
    canvas.setFillColor(LIGHT_GREY)
    # no footer text to keep clean like original
    canvas.restoreState()

doc.build(story, onFirstPage=add_footer, onLaterPages=add_footer)
print(f"SAVED -> {OUT}")

# Verify extract
import pymupdf
d = pymupdf.open(OUT)
print("pages", len(d))
txt = d[0].get_text()
print(txt[:2500])
# Check education block present
for needle in ["85% in Grade 10", "65% in Grade 12", "OLPS", "Ryan International"]:
    print(f"check '{needle}':", needle in txt)
# Check file size
import pathlib
print("size", pathlib.Path(OUT).stat().st_size)
