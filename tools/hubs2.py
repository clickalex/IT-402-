#!/usr/bin/env python3
"""Generate part-a.html and unit1-4 hub pages."""
import pathlib
from tpl import page

ROOT = pathlib.Path(__file__).resolve().parent.parent

PARTA = """<div class="crumbs"><a href="index.html">Home</a> / Part A · Employability Skills</div>
<h1>Part A · Employability Skills (10 marks)</h1>
<p class="card part-a">Workplace skills for a Domestic Data Entry Operator. Paper: <b>Q1 objective (any 4/6 = 4)</b> + <b>short answers (any 3/5 × 2 = 6)</b>. Each unit below has its own detailed page — open it, study, tick complete.</p>
<figure class="shot"><img src="assets/img/part-a-team.jpg" alt="Team communicating in an office" loading="lazy"><figcaption>Part A — the human skills behind every data operator.</figcaption></figure>
<section class="card" aria-label="Part A unit selection">
<h2>Choose a Part A unit to practise</h2>
<form action="question-bank.html#quiz" method="get">
<label for="part-a-unit"><b>Employability unit</b></label>
<select id="part-a-unit" name="chapter">
<option value="pa-u1">U1 · Communication Skills-II</option>
<option value="pa-u2">U2 · Self-Management Skills-II</option>
<option value="pa-u3">U3 · ICT Skills-II</option>
<option value="pa-u4">U4 · Entrepreneurial Skills-II</option>
<option value="pa-u5">U5 · Green Skills-II</option>
</select>
<button class="button" type="submit">Open selected practice →</button>
</form>
<p>Opens the question bank filtered to your selected unit: interactive MCQs and a written question with model marking points. The bank’s general questions and full papers remain unfiltered.</p>
</section>
<div class="card"><b>Trend-informed priorities:</b> communication barriers and feedback; stress and SMART goals; OS, maintenance and data protection; entrepreneurial qualities, myths and functions; sustainability and practical green actions.
<p>These priorities come from the <a href="pyq.html">2019–26 official SQP review</a>, not predictions. Practise all five units. Individual unit marks vary across papers; the 10-mark Part A total is not a fixed per-unit split. New practice questions are authored exercises, not official PYQs.</p></div>
<div class="cards">
<div class="card"><h3>U1 · Communication-II</h3>
<p>Cycle, methods, 7 Cs, barriers, feedback, active listening.</p>
<p><b>Practice focus:</b> 7 Cs match · linguistic barrier · feedback.</p><a href="chapters/pa-u1-communication.html">Study U1 →</a><p><a href="question-bank.html?chapter=pa-u1#quiz">Unit-wise MCQs + written practice →</a> · <a href="pyq.html#C-U1">Official SQP questions →</a></p></div>
<div class="card"><h3>U2 · Self-Management-II</h3>
<p>Stress, SMART goals, time management, OCEAN, grooming.</p>
<p><b>Practice focus:</b> expand SMART · stress techniques · case-study.</p><a href="chapters/pa-u2-self-management.html">Study U2 →</a><p><a href="question-bank.html?chapter=pa-u2#quiz">Unit-wise MCQs + written practice →</a> · <a href="pyq.html#C-U2">Official SQP questions →</a></p></div>
<div class="card"><h3>U3 · ICT Skills-II</h3>
<p>OS, files &amp; extensions, maintenance, cyber safety, email.</p>
<p><b>Practice focus:</b> OS role · maintenance · backup · safe access.</p><a href="chapters/pa-u3-ict.html">Study U3 →</a><p><a href="question-bank.html?chapter=pa-u3#quiz">Unit-wise MCQs + written practice →</a> · <a href="pyq.html#C-U3">Official SQP questions →</a></p></div>
<div class="card"><h3>U4 · Entrepreneurial-II</h3>
<p>Entrepreneur vs employee, qualities, myths, business plan.</p>
<p><b>Practice focus:</b> difference table · qualities · myths vs facts.</p><a href="chapters/pa-u4-entrepreneurial.html">Study U4 →</a><p><a href="question-bank.html?chapter=pa-u4#quiz">Unit-wise MCQs + written practice →</a> · <a href="pyq.html#C-U4">Official SQP questions →</a></p></div>
<div class="card"><h3>U5 · Green Skills-II</h3>
<p>Sustainable development, green economy, green jobs, 4 Rs.</p>
<p><b>Practice focus:</b> sustainable development · SDGs · practical resource-saving actions.</p><a href="chapters/pa-u5-green.html">Study U5 →</a><p><a href="question-bank.html?chapter=pa-u5#quiz">Unit-wise MCQs + written practice →</a> · <a href="pyq.html#C-U5">Official SQP questions →</a></p></div>
</div>
<h2>Part A at a glance</h2>
<table><tr><th>Unit</th><th>Memorise cold</th><th>Trick</th></tr>
<tr><td>U1 Communication</td><td>7 steps cycle + 7 Cs + 5 barriers</td><td>SEMC-DRF · “Can Cows Chew…”</td></tr>
<tr><td>U2 Self-Management</td><td>SMART × 5 + 4 stress techniques + OCEAN</td><td>“Smart Monkeys Achieve…”</td></tr>
<tr><td>U3 ICT</td><td>OS def + 4 maintenance + 4 safety habits</td><td>PAF-BL</td></tr>
<tr><td>U4 Entrepreneurial</td><td>Difference table + 6 qualities + 3 myths</td><td>RLD-HIC · I-M-P-F-S-L</td></tr>
<tr><td>U5 Green</td><td>Brundtland line + 3 pillars + 4 green jobs</td><td>ESE · 4 Rs</td></tr></table>
<h2>Part A final checklist</h2>
<label class="check"><input type="checkbox"> Cycle 7 steps in order + 7 Cs with 2 examples</label>
<label class="check"><input type="checkbox"> SMART expanded + 4 stress techniques + OCEAN</label>
<label class="check"><input type="checkbox"> OS + extensions + backup + password rules</label>
<label class="check"><input type="checkbox"> Entrepreneur vs employee table + myths vs facts</label>
<label class="check"><input type="checkbox"> Explain sustainable development + pillars + two practical green actions</label>
<nav class="card prevnext"><a href="syllabus.html">← Previous: Syllabus</a><span style="float:right"><a href="unit1-writer.html">Next: Unit 1 Writer →</a></span></nav>"""

UNIT1 = """<div class="crumbs"><a href="index.html">Home</a> / Unit 1 · Writer</div>
<h1>Unit 1 · Digital Documentation — Writer (8 marks)</h1>
<p class="card u1">Advanced LibreOffice Writer: maintainable long documents with styles, labelled images, automatic ToC, reusable templates and tracked reviews. Every chapter is a full page — open, practise on a computer, tick complete.</p>
<figure class="shot"><img src="assets/img/writer-docs.jpg" alt="Styled document illustration" loading="lazy"><figcaption>Unit 1 — professional documents with Writer.</figcaption></figure>
<div class="cards">
<div class="card"><h3>Ch 1 · Introduction to Styles</h3>
<p>6 categories, F11, Fill Format, 2 creation methods, update, load.</p>
<p><b>Hot Qs:</b> categories · Fill Format · new-style methods.</p><a href="chapters/u1-ch1-styles.html">Study Ch 1 →</a></div>
<div class="card"><h3>Ch 2 · Working with Images</h3>
<p>4 insert methods, resize/crop, drawing + group, anchor, arrange, wrap.</p>
<p><b>Hot Qs:</b> embed vs link · 4 anchors · wraps.</p><a href="chapters/u1-ch2-images.html">Study Ch 2 →</a></div>
<div class="card"><h3>Ch 3 · ToC + Templates + Track Changes</h3>
<p>Heading hierarchy → ToC lifecycle; .ott verbs; 5-step review cycle.</p>
<p><b>Hot Qs:</b> ToC steps · template verbs · Manage path.</p><a href="chapters/u1-ch3-toc-templates-track.html">Study Ch 3 →</a></div>
</div>
<h2>Writer quick paths</h2>
<table><tr><th>Task</th><th>Path</th><th>Remember</th></tr>
<tr><td>Styles</td><td><kbd>F11</kbd> → double-click</td><td>Paragraph: click in para; Character: select letters</td></tr>
<tr><td>Fill Format</td><td>Paint icon in F11</td><td><kbd>Esc</kbd> exits</td></tr>
<tr><td>New style</td><td>From Selection (A+) / Drag-Drop</td><td>Name it; Update changes all</td></tr>
<tr><td>Image link</td><td>Insert → Image → tick Link</td><td>Small file; breaks if source moves</td></tr>
<tr><td>Anchor</td><td>Right-click → Anchor</td><td>To Page fixed; To Paragraph moves</td></tr>
<tr><td>Wrap</td><td>Right-click → Wrap</td><td>Contour follows shape edge</td></tr>
<tr><td>ToC</td><td>Insert → Table of Contents and Index</td><td>Headings first, Update always</td></tr>
<tr><td>Template</td><td>File → Templates → Save as Template</td><td>.ott, not .odt</td></tr>
<tr><td>Review</td><td>Edit → Track Changes → Record/Manage</td><td>Comment = <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>C</kbd></td></tr></table>
<h2>Unit 1 final checklist</h2>
<label class="check"><input type="checkbox"> 6 categories + F11 + Fill Format + 2 creation methods + Update + Load</label>
<label class="check"><input type="checkbox"> 4 image methods + Embed vs Link + Group</label>
<label class="check"><input type="checkbox"> 4 anchors + Arrange + 7 wraps with uses</label>
<label class="check"><input type="checkbox"> ToC: hierarchy → Insert → customise → Update/Delete</label>
<label class="check"><input type="checkbox"> Templates: 7 verbs + .ott · Track cycle P-R-R-A-F + Compare</label>
<p class="banner">📖 Prefer one long page? The legacy <a href="book-ch1-5.html">printable Chapters 1–5 book</a> is still available.</p>
<nav class="card prevnext"><a href="part-a.html">← Previous: Part A</a><span style="float:right"><a href="unit2-calc.html">Next: Unit 2 Calc →</a></span></nav>"""

UNIT2 = """<div class="crumbs"><a href="index.html">Home</a> / Unit 2 · Calc</div>
<h1>Unit 2 · Electronic Spreadsheet — Calc (10 marks)</h1>
<p class="card u2">Advanced LibreOffice Calc: analyse data, automate with macros, link sheets and collaborate safely. Most practical unit — learn every path by <b>doing</b> on a computer, then theory becomes easy.</p>
<figure class="shot"><img src="assets/img/calc-sheets.jpg" alt="Spreadsheet with charts illustration" loading="lazy"><figcaption>Unit 2 — analyse and automate with Calc.</figcaption></figure>
<div class="cards">
<div class="card"><h3>Ch 4 · Scenarios &amp; Goal Seek</h3>
<p>Consolidate, subtotals (sort first!), scenarios, Goal Seek F-T-V, Solver.</p>
<p><b>Hot Qs:</b> sort rule · Scenario vs Goal Seek · F-T-V.</p><a href="chapters/u2-ch4-scenarios-goal-seek.html">Study Ch 4 →</a></div>
<div class="card"><h3>Ch 5 · Macros</h3>
<p>Record/Run/Organise, My Macros, Function, arguments, security.</p>
<p><b>Hot Qs:</b> record path · storage · macro-as-function.</p><a href="chapters/u2-ch5-macros.html">Study Ch 5 →</a></div>
<div class="card"><h3>Ch 6 · Linking Data</h3>
<p>Sheet refs, external refs, hyperlinks, relative/absolute, F4.</p>
<p><b>Hot Qs:</b> syntax · Ctrl+K · relative vs absolute.</p><a href="chapters/u2-ch6-linking.html">Study Ch 6 →</a></div>
<div class="card"><h3>Ch 7 · Share &amp; Review</h3>
<p>Share ON, conflicts, record, comments, Manage, merge vs compare.</p>
<p><b>Hot Qs:</b> share path · (shared) · merge vs compare.</p><a href="chapters/u2-ch7-share-review.html">Study Ch 7 →</a></div>
</div>
<h2>Calc quick paths</h2>
<table><tr><th>Task</th><th>Path</th><th>Remember</th></tr>
<tr><td>Consolidate</td><td>Data → Consolidate</td><td>Merges dispersed ranges (SUM)</td></tr>
<tr><td>Subtotals</td><td>Sort → Data → Subtotals</td><td>IRON RULE: sort first; Remove to clear</td></tr>
<tr><td>Scenarios</td><td>Tools → Scenarios</td><td>Forward: inputs → outputs</td></tr>
<tr><td>Goal Seek</td><td>Tools → Goal Seek</td><td>Backward: F-T-V, ONE variable</td></tr>
<tr><td>Solver</td><td>Tools → Solver</td><td>Many variables + constraints</td></tr>
<tr><td>Macro</td><td>Tools → Macros → Record/Run</td><td>My Macros; Medium security</td></tr>
<tr><td>Hyperlink</td><td><kbd>Ctrl</kbd>+<kbd>K</kbd></td><td>Right-click to edit; relative moves safely</td></tr>
<tr><td>Data sources</td><td><kbd>F4</kbd></td><td>Drag registered Base data in</td></tr>
<tr><td>Share / Track</td><td>Tools → Share · Edit → Track Changes</td><td>(shared) · Manage accepts/rejects</td></tr></table>
<h2>Unit 2 final checklist</h2>
<label class="check"><input type="checkbox"> Consolidate steps · SORT-before-Subtotal + Remove + 3 levels</label>
<label class="check"><input type="checkbox"> Scenario create/switch · Goal Seek F-T-V + 1-variable rule · Solver</label>
<label class="check"><input type="checkbox"> Macro Record/Run/Organise + My Macros + Function + Security</label>
<label class="check"><input type="checkbox"> Sheet + external ref syntax · Ctrl+K + Relative/Absolute · F4</label>
<label class="check"><input type="checkbox"> Tools→Share + conflicts + Record/Manage + Merge vs Compare</label>
<nav class="card prevnext"><a href="unit1-writer.html">← Previous: Unit 1 Writer</a><span style="float:right"><a href="unit3-dbms.html">Next: Unit 3 DBMS →</a></span></nav>"""

UNIT3 = """<div class="crumbs"><a href="index.html">Home</a> / Unit 3 · DBMS</div>
<h1>Unit 3 · Database Management System — Base (12 marks ⭐)</h1>
<p class="card u3">Biggest unit, most scoring if concepts are clear. Keep the running example through all five chapters: <b>STUDENT(RollNo*, Name, ClassID, Marks) + CLASS(ClassID*, ClassName, Teacher)</b> (* = primary key).</p>
<figure class="shot"><img src="assets/img/dbms-base.jpg" alt="Connected database tables illustration" loading="lazy"><figcaption>Unit 3 — real databases with Base.</figcaption></figure>
<div class="cards">
<div class="card"><h3>Ch 8 · DBMS Intro</h3>
<p>Data vs information, 6 advantages, 3 models, keys table, 4 objects.</p>
<p><b>Hot Qs:</b> data vs info · degree/cardinality · PK.</p><a href="chapters/u3-ch8-dbms-intro.html">Study Ch 8 →</a></div>
<div class="card"><h3>Ch 9 · Base Tables</h3>
<p>.odb, 7 data types, Wizard vs Design View, PK rules, sort/delete.</p>
<p><b>Hot Qs:</b> types · 2 methods · AutoValue.</p><a href="chapters/u3-ch9-base-tables.html">Study Ch 9 →</a></div>
<div class="card"><h3>Ch 10 · Relationships</h3>
<p>1:1 / 1:N / M:N + junction, Tools→Relationships, RI + cascades.</p>
<p><b>Hot Qs:</b> types + example · FK side · RI.</p><a href="chapters/u3-ch10-relationships.html">Study Ch 10 →</a></div>
<div class="card"><h3>Ch 11 · Queries</h3>
<p>Wizard vs grid FATSVC, AND/OR rows, wildcards, SUM/AVG/COUNT.</p>
<p><b>Hot Qs:</b> grid rows · wildcards · functions.</p><a href="chapters/u3-ch11-queries.html">Study Ch 11 →</a></div>
<div class="card"><h3>Ch 12 · Forms &amp; Reports</h3>
<p>7 controls, form wizard + ops, report wizard + Title/Date.</p>
<p><b>Hot Qs:</b> Label vs Text Box · form vs report.</p><a href="chapters/u3-ch12-forms-reports.html">Study Ch 12 →</a></div>
</div>
<h2>DBMS quick paths</h2>
<table><tr><th>Task</th><th>Path</th><th>Remember</th></tr>
<tr><td>New database</td><td>File → New → Database</td><td>.odb holds everything</td></tr>
<tr><td>Table (fast)</td><td>Tables → Use Wizard</td><td>Standard fields, guided</td></tr>
<tr><td>Table (control)</td><td>Tables → Create Table in Design View</td><td>Name + type + properties + 🔑</td></tr>
<tr><td>Relationship</td><td>Tools → Relationships</td><td>Drag PK→FK, tick RI, 1—∞</td></tr>
<tr><td>Query</td><td>Queries → Create Query in Design View</td><td>FATSVC grid, <kbd>F5</kbd> runs</td></tr>
<tr><td>Form</td><td>Forms → Use Wizard</td><td>Columnar; subform for 1:N</td></tr>
<tr><td>Report</td><td>Reports → Use Wizard</td><td>Group by Class, sort, Title + Date</td></tr></table>
<h2>Unit 3 final checklist</h2>
<label class="check"><input type="checkbox"> Data vs Info · 6 advantages · 3 models · Degree/Cardinality · 5 keys · 4 objects</label>
<label class="check"><input type="checkbox"> 7 data types · Wizard vs Design · PK rules · Sort/Delete/Navigate</label>
<label class="check"><input type="checkbox"> 1:1/1:N/M:N + junction line · Tools→Relationships · RI + cascades</label>
<label class="check"><input type="checkbox"> Query grid FATSVC · AND/OR rows · wildcards · SUM/AVG/COUNT + GROUP BY</label>
<label class="check"><input type="checkbox"> 7 form controls (Label vs Text Box!) · wizards · Form vs Report</label>
<nav class="card prevnext"><a href="unit2-calc.html">← Previous: Unit 2 Calc</a><span style="float:right"><a href="unit4-safety.html">Next: Unit 4 Safety →</a></span></nav>"""

UNIT4 = """<div class="crumbs"><a href="index.html">Home</a> / Unit 4 · Safety</div>
<h1>Unit 4 · Healthy, Safe &amp; Secure Environment (10 marks)</h1>
<p class="card u4">Easiest 10 marks in the paper — pure reading + logic. Target full marks: hazard <b>types</b>, ergonomics <b>numbers</b>, evacuation <b>steps</b>, fire <b>triangle</b>, electrical first-aid <b>order</b>.</p>
<figure class="shot"><img src="assets/img/safety-lab.jpg" alt="Safe computer lab illustration" loading="lazy"><figcaption>Unit 4 — healthy, safe and secure work.</figcaption></figure>
<div class="cards">
<div class="card"><h3>Ch 13 · HSS at Workplace</h3>
<p>Health/safety/security, policies, 6 reasons, hazard gallery, lifting, hierarchy.</p>
<p><b>Hot Qs:</b> defs · reasons · hazard types.</p><a href="chapters/u4-ch13-hss.html">Study Ch 13 →</a></div>
<div class="card"><h3>Ch 14 · Quality + Ergonomics</h3>
<p>Air/water/cleanliness, ergonomics numbers, 8 problem→remedy pairs, cautions.</p>
<p><b>Hot Qs:</b> 50–70 · 20-20-20 · case-study.</p><a href="chapters/u4-ch14-quality-ergonomics.html">Study Ch 14 →</a></div>
<div class="card"><h3>Ch 15 · Accidents &amp; Emergencies</h3>
<p>5 golden rules, accident types, evacuation ×7, fire + PASS, electrical ×6.</p>
<p><b>Hot Qs:</b> evacuation order · PASS · shock first step.</p><a href="chapters/u4-ch15-accidents-emergencies.html">Study Ch 15 →</a></div>
</div>
<h2>Safety numbers &amp; orders</h2>
<table><tr><th>Topic</th><th>Learn exactly</th><th>Trick</th></tr>
<tr><td>Ergonomics</td><td>50–70 cm · eye level · 90° knees · feet flat · elbow keyboard</td><td>Chant thrice</td></tr>
<tr><td>Eyes</td><td>20-20-20: every 20 min → 20 ft away → 20 sec</td><td>—</td></tr>
<tr><td>Golden rules ×5</td><td>Identify → Help → Policy → Limits → Obey</td><td>I-Help-Policy-Limits-Obey</td></tr>
<tr><td>Evacuation ×7</td><td>Calm+Alarm → Switch off → Exit (no lift) → Assemble → Count → Wait</td><td>CALm-Switch-Exit-Assemble-Count-Wait</td></tr>
<tr><td>Fire</td><td>Triangle F-H-O · PASS · STOP-DROP-ROLL</td><td>FoHO</td></tr>
<tr><td>Electrical ×6</td><td>Don't touch → Power OFF → Dry stick → Call → Burns → Hospital</td><td>Don't-Switch-Stick-Send</td></tr>
<tr><td>Helplines</td><td>101 fire · 100 police · 102/108 ambulance</td><td>Write in every emergency answer</td></tr></table>
<h2>Unit 4 final checklist</h2>
<label class="check"><input type="checkbox"> Defs · 6 policy items · 6 reasons · 7 hazard types + examples</label>
<label class="check"><input type="checkbox"> Computer 6 · lifting knees-rule · control 5 levels</label>
<label class="check"><input type="checkbox"> Air/water/cleanliness · ergonomics numbers · 20-20-20 · 8 pairs · 8 cautions</label>
<label class="check"><input type="checkbox"> Accident vs Emergency · 5 rules · 5 accident types · 3 handling steps</label>
<label class="check"><input type="checkbox"> Evacuation ×7 · Triangle + PASS + STOP-DROP-ROLL · electrical ×6 · helplines</label>
<nav class="card prevnext"><a href="unit3-dbms.html">← Previous: Unit 3 DBMS</a><span style="float:right"><a href="question-bank.html">Next: Question Bank →</a></span></nav>"""

if __name__ == "__main__":
    jobs = [("part-a.html", "Part A · Employability Skills · IT 402",
             "Part A employability skills overview with links to 5 detailed units", PARTA, "part-a.html"),
            ("unit1-writer.html", "Unit 1 · Writer · IT 402",
             "Unit 1 Writer overview with links to 3 detailed chapters", UNIT1, "unit1-writer.html"),
            ("unit2-calc.html", "Unit 2 · Calc · IT 402",
             "Unit 2 Calc overview with links to 4 detailed chapters", UNIT2, "unit2-calc.html"),
            ("unit3-dbms.html", "Unit 3 · DBMS · IT 402",
             "Unit 3 DBMS overview with links to 5 detailed chapters", UNIT3, "unit3-dbms.html"),
            ("unit4-safety.html", "Unit 4 · Safety · IT 402",
             "Unit 4 safety overview with links to 3 detailed chapters", UNIT4, "unit4-safety.html")]
    for fname, title, desc, body, active in jobs:
        (ROOT / fname).write_text(page(title, desc, active, body), encoding="utf-8")
    print("part-a + unit1-4 hubs written")