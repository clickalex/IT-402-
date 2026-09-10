"""Shared chapter metadata, sidebar and page templates."""

CHAPTERS = [
("pa-u1","pa-u1-communication.html","Unit 1 · Communication Skills-II","Part A · Employability Skills","part-a.html","part-a","Part-A-Deep-Chapters.md","# Unit 1:"),
("pa-u2","pa-u2-self-management.html","Unit 2 · Self-Management Skills-II","Part A · Employability Skills","part-a.html","part-a","Part-A-Deep-Chapters.md","# Unit 2:"),
("pa-u3","pa-u3-ict.html","Unit 3 · ICT Skills-II","Part A · Employability Skills","part-a.html","part-a","Part-A-Deep-Chapters.md","# Unit 3:"),
("pa-u4","pa-u4-entrepreneurial.html","Unit 4 · Entrepreneurial Skills-II","Part A · Employability Skills","part-a.html","part-a","Part-A-Deep-Chapters.md","# Unit 4:"),
("pa-u5","pa-u5-green.html","Unit 5 · Green Skills-II","Part A · Employability Skills","part-a.html","part-a","Part-A-Deep-Chapters.md","# Unit 5:"),
("u1-ch1","u1-ch1-styles.html","Chapter 1 · Introduction to Styles","Unit 1 · Digital Documentation (Writer)","unit1-writer.html","u1","Unit1-Writer-Deep-Chapters.md","# Chapter 1:"),
("u1-ch2","u1-ch2-images.html","Chapter 2 · Working with Images","Unit 1 · Digital Documentation (Writer)","unit1-writer.html","u1","Unit1-Writer-Deep-Chapters.md","# Chapter 2:"),
("u1-ch3","u1-ch3-toc-templates-track.html","Chapter 3 · ToC, Templates & Track Changes","Unit 1 · Digital Documentation (Writer)","unit1-writer.html","u1","Unit1-Writer-Deep-Chapters.md","# Chapter 3:"),
("u2-ch4","u2-ch4-scenarios-goal-seek.html","Chapter 4 · Scenarios & Goal Seek","Unit 2 · Electronic Spreadsheet (Calc)","unit2-calc.html","u2","Unit2-Calc-Deep-Chapters.md","# Chapter 4:"),
("u2-ch5","u2-ch5-macros.html","Chapter 5 · Macros in Spreadsheet","Unit 2 · Electronic Spreadsheet (Calc)","unit2-calc.html","u2","Unit2-Calc-Deep-Chapters.md","# Chapter 5:"),
("u2-ch6","u2-ch6-linking.html","Chapter 6 · Linking Spreadsheet Data","Unit 2 · Electronic Spreadsheet (Calc)","unit2-calc.html","u2","Unit2-Calc-Deep-Chapters.md","# Chapter 6:"),
("u2-ch7","u2-ch7-share-review.html","Chapter 7 · Share & Review Spreadsheet","Unit 2 · Electronic Spreadsheet (Calc)","unit2-calc.html","u2","Unit2-Calc-Deep-Chapters.md","# Chapter 7:"),
("u3-ch8","u3-ch8-dbms-intro.html","Chapter 8 · Introduction to DBMS","Unit 3 · Database Management System (Base)","unit3-dbms.html","u3","Unit3-DBMS-Deep-Chapters.md","# Chapter 8:"),
("u3-ch9","u3-ch9-base-tables.html","Chapter 9 · Starting with LibreOffice Base","Unit 3 · Database Management System (Base)","unit3-dbms.html","u3","Unit3-DBMS-Deep-Chapters.md","# Chapter 9:"),
("u3-ch10","u3-ch10-relationships.html","Chapter 10 · Working with Multiple Tables","Unit 3 · Database Management System (Base)","unit3-dbms.html","u3","Unit3-DBMS-Deep-Chapters.md","# Chapter 10:"),
("u3-ch11","u3-ch11-queries.html","Chapter 11 · Queries in Base","Unit 3 · Database Management System (Base)","unit3-dbms.html","u3","Unit3-DBMS-Deep-Chapters.md","# Chapter 11:"),
("u3-ch12","u3-ch12-forms-reports.html","Chapter 12 · Forms & Reports","Unit 3 · Database Management System (Base)","unit3-dbms.html","u3","Unit3-DBMS-Deep-Chapters.md","# Chapter 12:"),
("u4-ch13","u4-ch13-hss.html","Chapter 13 · Health, Safety & Security","Unit 4 · Safe & Secure Environment","unit4-safety.html","u4","Unit4-Safety-Deep-Chapters.md","# Chapter 13:"),
("u4-ch14","u4-ch14-quality-ergonomics.html","Chapter 14 · Workplace Quality Measures","Unit 4 · Safe & Secure Environment","unit4-safety.html","u4","Unit4-Safety-Deep-Chapters.md","# Chapter 14:"),
("u4-ch15","u4-ch15-accidents-emergencies.html","Chapter 15 · Prevent Accidents & Emergencies","Unit 4 · Safe & Secure Environment","unit4-safety.html","u4","Unit4-Safety-Deep-Chapters.md","# Chapter 15:"),
]

GROUPS = [
("Part A · Employability (10)", ["pa-u1","pa-u2","pa-u3","pa-u4","pa-u5"]),
("Unit 1 · Writer (8)", ["u1-ch1","u1-ch2","u1-ch3"]),
("Unit 2 · Calc (10)", ["u2-ch4","u2-ch5","u2-ch6","u2-ch7"]),
("Unit 3 · DBMS (12)", ["u3-ch8","u3-ch9","u3-ch10","u3-ch11","u3-ch12"]),
("Unit 4 · Safety (10)", ["u4-ch13","u4-ch14","u4-ch15"]),
]
BY_ID = {c[0]: c for c in CHAPTERS}
SHORT = {"pa-u1":"U1 · Communication-II","pa-u2":"U2 · Self-Management-II","pa-u3":"U3 · ICT Skills-II",
"pa-u4":"U4 · Entrepreneurial-II","pa-u5":"U5 · Green Skills-II","u1-ch1":"Ch 1 · Styles",
"u1-ch2":"Ch 2 · Images","u1-ch3":"Ch 3 · ToC + Templates + Track","u2-ch4":"Ch 4 · Scenarios + Goal Seek",
"u2-ch5":"Ch 5 · Macros","u2-ch6":"Ch 6 · Linking Data","u2-ch7":"Ch 7 · Share & Review",
"u3-ch8":"Ch 8 · DBMS Intro","u3-ch9":"Ch 9 · Base Tables","u3-ch10":"Ch 10 · Relationships",
"u3-ch11":"Ch 11 · Queries","u3-ch12":"Ch 12 · Forms & Reports","u4-ch13":"Ch 13 · HSS at Workplace",
"u4-ch14":"Ch 14 · Quality + Ergonomics","u4-ch15":"Ch 15 · Accidents & Emergencies"}

def sidebar(active, prefix=""):
    ch = "chapters/" if prefix == "" else ""
    parts = ['<aside class="sidebar">', "<h3>Navigate</h3>"]
    for href, label in [("index.html", "🏠 Home"), ("syllabus.html", "🗺️ Syllabus & Pattern")]:
        cls = ' class="active"' if href == active else ""
        parts.append(f'<a href="{prefix}{href}"{cls}>{label}</a>')
    for gtitle, ids in GROUPS:
        is_open = " open" if any(BY_ID[i][1] == active for i in ids) else ""
        parts.append(f'<details class="navgroup"{is_open}><summary>{gtitle}</summary>')
        for i in ids:
            f = BY_ID[i][1]
            cls = ' class="active"' if f == active else ""
            parts.append(f'<a href="{ch}{f}"{cls}>{SHORT[i]}</a>')
        parts.append("</details>")
    for href, label in [("question-bank.html", "❓ Question Bank"), ("pyq.html", "📝 PYQ Practice"), ("practical.html", "💻 Practical Lab"), ("revision.html", "🧠 Revision")]:
        cls = ' class="active"' if href == active else ""
        parts.append(f'<a href="{prefix}{href}"{cls}>{label}</a>')
    parts.append('<h3>Progress</h3><div class="progress"><i data-progress></i></div>')
    parts.append("<small data-progress-label>0 of 20 chapters marked complete</small></aside>")
    return "\n".join(parts)

def page(title, desc, active, body_html, prefix=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="{desc}">
<title>{title}</title>
<link rel="stylesheet" href="{prefix}assets/css/styles.css">
</head>
<body>
<header class="topbar">
<button class="menu-btn" aria-label="Open navigation">☰</button>
<a class="brand" href="{prefix}index.html">IT<span>402</span> Study Hub</a>
<div class="search"><input id="siteSearch" type="search" placeholder="Search 20 chapters…  ( / )" aria-label="Search">
<div id="searchResults"></div></div>
<button class="theme-btn" aria-label="Toggle dark mode">☼</button>
</header>
<div class="layout">
{sidebar(active, prefix)}
<main class="main">
{body_html}
</main>
</div>
<button class="backtop" aria-label="Back to top">↑</button>
<footer class="footer">CBSE Class 10 Information Technology · Subject Code 402 · Session 2026–27<br>LibreOffice-only study hub · 20 chapters · works offline</footer>
<script src="{prefix}assets/js/app.js"></script>
</body>
</html>
"""
