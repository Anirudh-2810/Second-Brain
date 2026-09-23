from docx import Document
from docx.shared import Pt

SRC = "raw-sources/Team Onyx India Resume (1).docx"
DST = "raw-sources/Team Onyx India Resume - Anirudh.docx"

ANS = {
    "name_top": "NAME: Anirudh [FILL: full name]",
    "contact": "EMAIL ID: [FILL: email]\t\tMOBILE NUMBER: [FILL: mobile]",
    "pd_name": "Name: Anirudh",
    "pd_branch": "Branch: FE Robotics & AI @ KJSCE",
    "pd_div": "Division: [FILL: division]",
    "pd_addr": "Address: [FILL: address]",
    "q1": ("I want to write code where it flies. I am FE Robotics & AI, and my builds so far are software — "
           "a ROS2 odometry diagnostic spec with live covariance and Q/R tuning (aerofuse), and a stock-agent data loop. "
           "Onyx is the first place where my scripts meet a real airframe and real flight logs. I cleared Round-1 on theory; "
           "now I want to earn the bench by automating the boring parts — prop-match math, CSV log parsing, checklists — "
           "so seniors get clean data instead of manual readings."),
    "q2": ("College term: strong Python/C + DSA fluency, ship aerofuse MVP and a working stock-agent prototype, keep the daily study streak alive. "
           "Career direction: builder-researcher toward robotics + quant foundations — internship-ready portfolio first, "
           "then decide CQF vs MSc vs job route by exposure. Onyx fits the robotics half directly."),
    "q3": ("Three things I cannot get alone: real test data to code against, review from seniors who have crashed and fixed, "
           "and a team loop that forces shipping. My dashboard spec and backtest loop were solo; Onyx gives me thrust-test CSVs, "
           "build-flow discipline from the workshop PPTs, and flight-test debriefs that turn scripts into tools people use."),
    "q4": ("Python + Arduino-basics for software-only bench tooling. I will own: (1) prop-matcher script — kV x volts = RPM, 8x5 reading, "
           "3S voltage bands, ESC headroom rule; (2) CSV log parser — max thrust row, mean amps, undervoltage flags; (3) pre-flight checklist "
           "generator from the workshop flow. Beginner hardware, honest about it — one ASL LED lab — but I can whiteboard delay() vs millis() "
           "and I learn bench procedure fast."),
    "q5": ("Cleared Team Onyx Round-1 written 2026-09-23, through to interview. aerofuse ROS2 diagnostic dashboard — full design spec, EKF covariance plan. "
           "Stock-agent data-signal-backtest loop in progress; Second-Brain vault with generated dashboard. ASL Arduino LED patterns lab — first embedded exposure."),
}

SKILLS_ROWS = [
    ("Python 3.x (NumPy, matplotlib)", "CPython 3.x", "stock-agent loop; prop-matcher + CSV log parser scripts"),
    ("C (GCC)", "CS50 / DSA practice", "vault DSA pages, memory/flowchart notes"),
    ("Arduino beginner (Uno, IDE)", "setup/loop, digitalWrite", "one ASL lab: LED patterns; delay() vs millis() explainable"),
    ("ROS2 concept + Git/GitHub", "Humble/Jazzy spec; GitHub", "aerofuse dashboard spec; Second-Brain vault + Pages"),
]

EDU_ROWS = [
    ("SSC (10th)", "[FILL: month & year]", "[FILL: school/board]", "[FILL: %/CGPA]"),
    ("FE Robotics & AI, KJSCE (pursuing 2026-30)", "[FILL]", "KJSCE", "[FILL: CGPA]"),
]

d = Document(SRC)
paras = d.paragraphs
paras[2].text = ANS["name_top"]
paras[4].text = ANS["contact"]
paras[8].text = ANS["pd_name"]
paras[9].text = ANS["pd_branch"]
paras[10].text = ANS["pd_div"]
paras[11].text = ANS["pd_addr"]
paras[17].text = "CO-CURRICULAR ACTIVITIES"
paras[18].text = "2026: Cleared Team Onyx Round-1 written, through to interview. Building Second-Brain vault + stock-agent + aerofuse spec. [FILL: add clubs/sports if wanted]"
paras[33].text = ANS["q1"]
paras[41].text = ANS["q2"]
paras[49].text = ANS["q3"]
paras[57].text = ANS["q4"]
paras[66].text = ANS["q5"]

# Table0 education: keep header rows 0-1, fill rows 2-3
t0 = d.tables[0]
for i, row in enumerate(EDU_ROWS):
    r = t0.rows[2 + i]
    for j, val in enumerate(row):
        r.cells[j].text = val

# Table1 skills: keep header, fill rows 1-5
t1 = d.tables[1]
for i, row in enumerate(SKILLS_ROWS):
    r = t1.rows[1 + i]
    for j, val in enumerate(row):
        r.cells[j].text = val

# Table2 preferences: Design > Propulsion > Aerodynamics > Marketing and Finance
prefs = ["Design — CAD + scripting (software-only fit)",
         "Propulsion — theory + data tooling",
         "Aerodynamics — Round-1 depth",
         "Marketing and Finance"]
t2 = d.tables[2]
for i, p in enumerate(prefs):
    t2.rows[i].cells[0].text = ["First Preference", "Second Preference", "Third Preference", "Fourth Preference"][i]
    t2.rows[i].cells[1].text = p

d.save(DST)
print("saved " + DST)
