#!/usr/bin/env python3
"""Generate index.html, syllabus.html, revision.html (hub pages)."""
import pathlib
from tpl import page

ROOT = pathlib.Path(__file__).resolve().parent.parent

INDEX = """<div class="crumbs"><a href="index.html">Home</a> / Home</div>
<section class="hero hero-grid"><div><p><b>CBSE • CLASS 10 • SESSION 2026–27</b></p>
<h1>Information Technology<br><span style="color:#a7f3d0">Subject Code 402</span></h1>
<p>A practical-first study hub for the Domestic Data Entry Operator job role. <b>20 chapters, one detailed page each</b> — concept, LibreOffice steps, memory tricks, exam Q&amp;A and a hands-on task.</p>
<a class="button" href="syllabus.html">View syllabus</a> <a class="button" href="chapters/u3-ch8-dbms-intro.html">Start DBMS (12 marks) →</a> <a class="button alt" href="revision.html">Quick revision</a></div><img class="hero-img" src="assets/img/hero-study.jpg" alt="Two students studying Information Technology at a computer desk"></section>
<h2>Study dashboard</h2>
<div class="card"><b>Your 20-chapter progress</b><div class="progress"><i data-progress></i></div>
<p data-progress-label>0 of 20 chapters marked complete</p><small>Saved on this device with localStorage. Tick “Mark complete” at the bottom of each chapter.</small></div>
<h2>Five study areas · 20 chapters</h2>
<div class="cards">
<div class="card part-a" data-unit="pa-u" data-total="5"><h3>Part A · Employability (10)</h3>
<p>Workplace behaviour and green skills.</p>
<ul><li><a href="chapters/pa-u1-communication.html">U1 · Communication-II</a> <small>(2)</small></li>
<li><a href="chapters/pa-u2-self-management.html">U2 · Self-Management-II</a> <small>(3 ⭐)</small></li>
<li><a href="chapters/pa-u3-ict.html">U3 · ICT Skills-II</a> <small>(1)</small></li>
<li><a href="chapters/pa-u4-entrepreneurial.html">U4 · Entrepreneurial-II</a> <small>(3 ⭐)</small></li>
<li><a href="chapters/pa-u5-green.html">U5 · Green Skills-II</a> <small>(1)</small></li></ul>
<div class="unitbar"><div class="progress"><i data-unit-bar></i></div><small data-unit-label>0/5 chapters</small></div>
<p><a href="part-a.html">Unit overview →</a></p></div>
<div class="card u1" data-unit="u1-ch" data-total="3"><h3>Unit 1 · Writer (8)</h3>
<p>Styles, images, ToC, templates and review.</p>
<ul><li><a href="chapters/u1-ch1-styles.html">Ch 1 · Styles</a></li>
<li><a href="chapters/u1-ch2-images.html">Ch 2 · Images</a></li>
<li><a href="chapters/u1-ch3-toc-templates-track.html">Ch 3 · ToC + Templates + Track</a></li></ul>
<div class="unitbar"><div class="progress"><i data-unit-bar></i></div><small data-unit-label>0/3 chapters</small></div>
<p><a href="unit1-writer.html">Unit overview →</a></p></div>
<div class="card u2" data-unit="u2-ch" data-total="4"><h3>Unit 2 · Calc (10)</h3>
<p>Analysis, macros, links and collaboration.</p>
<ul><li><a href="chapters/u2-ch4-scenarios-goal-seek.html">Ch 4 · Scenarios + Goal Seek</a></li>
<li><a href="chapters/u2-ch5-macros.html">Ch 5 · Macros</a></li>
<li><a href="chapters/u2-ch6-linking.html">Ch 6 · Linking Data</a></li>
<li><a href="chapters/u2-ch7-share-review.html">Ch 7 · Share &amp; Review</a></li></ul>
<div class="unitbar"><div class="progress"><i data-unit-bar></i></div><small data-unit-label>0/4 chapters</small></div>
<p><a href="unit2-calc.html">Unit overview →</a></p></div>
<div class="card u3" data-unit="u3-ch" data-total="5"><h3>Unit 3 · DBMS (12 ⭐)</h3>
<p>Base tables, relationships, queries, forms, reports.</p>
<ul><li><a href="chapters/u3-ch8-dbms-intro.html">Ch 8 · DBMS Intro</a></li>
<li><a href="chapters/u3-ch9-base-tables.html">Ch 9 · Base Tables</a></li>
<li><a href="chapters/u3-ch10-relationships.html">Ch 10 · Relationships</a></li>
<li><a href="chapters/u3-ch11-queries.html">Ch 11 · Queries</a></li>
<li><a href="chapters/u3-ch12-forms-reports.html">Ch 12 · Forms &amp; Reports</a></li></ul>
<div class="unitbar"><div class="progress"><i data-unit-bar></i></div><small data-unit-label>0/5 chapters</small></div>
<p><a href="unit3-dbms.html">Unit overview →</a></p></div>
<div class="card u4" data-unit="u4-ch" data-total="3"><h3>Unit 4 · Safety (10)</h3>
<p>Health, safety, quality, ergonomics, emergencies.</p>
<ul><li><a href="chapters/u4-ch13-hss.html">Ch 13 · HSS at Workplace</a></li>
<li><a href="chapters/u4-ch14-quality-ergonomics.html">Ch 14 · Quality + Ergonomics</a></li>
<li><a href="chapters/u4-ch15-accidents-emergencies.html">Ch 15 · Accidents &amp; Emergencies</a></li></ul>
<div class="unitbar"><div class="progress"><i data-unit-bar></i></div><small data-unit-label>0/3 chapters</small></div>
<p><a href="unit4-safety.html">Unit overview →</a></p></div>
</div>
<h2>Assessment at a glance</h2>
<table><tr><th>Component</th><th>Marks</th><th>Preparation</th></tr>
<tr><td>Theory (Section A objective 24 + Section B subjective 26)</td><td><b>50</b></td><td>Menu paths, shortcuts, definitions, steps and safety reasoning.</td></tr>
<tr><td>Practical: Writer 5 + Calc 5 + Base 10 + Viva 10 + Project 10 + File 10</td><td><b>50</b></td><td>Repeat 15 tasks, explain choices aloud, keep a neat file.</td></tr>
<tr><th>Total</th><th>100</th><td>Accuracy and presentation matter.</td></tr></table>
<h2>Topper's study order (15 days)</h2>
<ol class="steps"><li><b>Unit 3 DBMS first</b> (12 marks, most scoring) → 4 days.</li>
<li><b>Unit 2 Calc</b> on a computer (10) → 3 days.</li>
<li><b>Unit 4 Safety</b> (10, easiest theory) → 2 days.</li>
<li><b>Unit 1 Writer</b> (8, steps-based) → 2 days.</li>
<li><b>Part A</b> (10, lists + examples) → 2 days.</li>
<li><b>Timed sample paper + practical file + viva</b> → 2 days.</li></ol>
<div class="callout tip"><b>Exam countdown:</b> Target February 2027 boards; verify the official CBSE date sheet when published.</div>
<h2>Jump in</h2>
<div class="cards"><a class="card" href="practical.html"><h3>💻 Practical lab</h3><p>25 tasks, mock exam, troubleshooting, 50 viva Qs.</p></a>
<a class="card" href="question-bank.html"><h3>❓ Test yourself</h3><p>30-question quizzes, 100 objectives, 2 sample papers + timer.</p></a>
<a class="card" href="revision.html"><h3>🧠 Exam morning</h3><p>Paths, shortcuts, numbers and answer frames.</p></a></div>"""

SYLLABUS = """<div class="crumbs"><a href="index.html">Home</a> / Syllabus</div>
<h1>CBSE IT-402 syllabus · 2026–27</h1>
<p class="card">Study map for the Domestic Data Entry Operator role. Compare your school's latest official curriculum if a circular changes the paper. All procedures use <b>LibreOffice Writer / Calc / Base</b> — never write MS Office names in answers.</p>
<h2>Theory marks distribution (50)</h2>
<table><tr><th>Part</th><th>Unit / Chapter</th><th>Marks</th><th>Study link</th></tr>
<tr><td rowspan="5"><b>Part A (10)</b></td><td>U1 · Communication Skills-II</td><td>2</td><td><a href="chapters/pa-u1-communication.html">Study →</a></td></tr>
<tr><td>U2 · Self-Management Skills-II</td><td>3</td><td><a href="chapters/pa-u2-self-management.html">Study →</a></td></tr>
<tr><td>U3 · ICT Skills-II</td><td>1</td><td><a href="chapters/pa-u3-ict.html">Study →</a></td></tr>
<tr><td>U4 · Entrepreneurial Skills-II</td><td>3</td><td><a href="chapters/pa-u4-entrepreneurial.html">Study →</a></td></tr>
<tr><td>U5 · Green Skills-II</td><td>1</td><td><a href="chapters/pa-u5-green.html">Study →</a></td></tr>
<tr><td rowspan="4"><b>Part B (40)</b></td><td>Unit 1 · Digital Documentation — Ch 1–3</td><td>8</td><td><a href="unit1-writer.html">Study →</a></td></tr>
<tr><td>Unit 2 · Electronic Spreadsheet — Ch 4–7</td><td>10</td><td><a href="unit2-calc.html">Study →</a></td></tr>
<tr><td>Unit 3 · DBMS — Ch 8–12</td><td><b>12</b></td><td><a href="unit3-dbms.html">Study →</a></td></tr>
<tr><td>Unit 4 · Safe working environment — Ch 13–15</td><td>10</td><td><a href="unit4-safety.html">Study →</a></td></tr></table>
<h2>Theory paper pattern (50 marks, 2 hours)</h2>
<div class="cards"><div class="card"><h3>Section A · Objective · 24</h3>
<p><b>Q1:</b> Employability — 6 sub-Qs, attempt any 4 = 4.<br><b>Q2–Q5:</b> Subject skills — 24 sub-Qs, attempt any 20 = 20.</p>
<p>MCQ, fill-in, True/False, match. No negative marking — attempt all allowed. Watch for “<b>not</b>”.</p></div>
<div class="card"><h3>Section B · Subjective · 26</h3>
<p><b>Employability:</b> 5 × 2-mark, attempt any 3 = 6 (20–30 words).<br><b>Subject short:</b> 6 × 2-mark, attempt any 4 = 8.<br><b>Subject long:</b> 5 × 4-mark, attempt any 3 = 12 (50–80 words, steps/case-study).</p></div></div>
<h2>School-based 50 marks</h2>
<table><tr><th>Evidence</th><th>Marks</th><th>Prepare</th></tr>
<tr><td>Writer practical</td><td>5</td><td>Styles / images / ToC / template / track changes file that opens.</td></tr>
<tr><td>Calc practical</td><td>5</td><td>Consolidate / subtotal / scenario / goal seek / macro / linking file.</td></tr>
<tr><td>Base practical</td><td>10</td><td>Table + relationship + query + form/report in one .odb.</td></tr>
<tr><td>Viva</td><td>10</td><td>Explain <i>why</i> you chose a field type, formula, style or safety action.</td></tr>
<tr><td>Project / field visit</td><td>10</td><td>Real-world case study: Base forms + reports, documented in Writer.</td></tr>
<tr><td>Practical file / portfolio</td><td>10</td><td>Neat file: 5 Writer + 5 Calc + 5 Base printouts with steps.</td></tr></table>
<div class="warning"><b>Weightage note:</b> Chapter-wise marks can shift in the official paper design. Treat this as a preparation lens, not a promise.</div>
<h2>Golden rules to score 45+/50</h2>
<ol class="steps"><li>Learn every <b>menu path + shortcut</b> (Tools → Macros → Record Macro, <kbd>F11</kbd>, <kbd>Ctrl</kbd>+<kbd>K</kbd>).</li>
<li>For 2- and 4-markers, write <b>numbered steps</b> with one example.</li>
<li>Master <b>DBMS (12) + Calc (10)</b> first — 22 of 40 Part B marks.</li>
<li>Attempt all allowed objectives — <b>no negative marking</b>.</li></ol>
<h2>Study route per chapter</h2>
<ol class="steps"><li>Read the concept + comparison table + diagram.</li>
<li>Perform the numbered LibreOffice steps on a computer.</li>
<li>Answer the Q&amp;A without looking; then check.</li>
<li>Mark complete and revisit weekly via <a href="revision.html">Revision</a>.</li></ol>"""

REVISION = """<div class="crumbs"><a href="index.html">Home</a> / Revision</div>
<h1>Exam morning · quick revision</h1>
<p class="card">One glance before you enter the hall: every menu path, shortcut, number and key. Print this page after checking your school's latest instructions.</p>
<div class="cards">
<div class="card"><h2>Writer paths</h2>
<p><b>Styles:</b> <kbd>F11</kbd> → double-click → Edit/Update<br><b>Fill Format:</b> paint icon → click paras → <kbd>Esc</kbd><br>
<b>Image:</b> Insert → Image → Anchor / Wrap / Caption<br><b>ToC:</b> Headings first → Insert → Table of Contents and Index → Update<br>
<b>Template:</b> File → Templates → Save as Template (.ott)<br><b>Changes:</b> Edit → Track Changes → Record (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>E</kbd>) / Manage<br>
<b>Comment:</b> <kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>C</kbd></p></div>
<div class="card"><h2>Calc paths</h2>
<p><b>Consolidate:</b> Data → Consolidate (SUM)<br><b>Subtotal:</b> SORT first → Data → Subtotals<br>
<b>Scenario:</b> Tools → Scenarios (forward)<br><b>Goal Seek:</b> Tools → Goal Seek — F-T-V (backward, 1 variable)<br>
<b>Solver:</b> Tools → Solver (many + constraints)<br><b>Macro:</b> Tools → Macros → Record/Run (My Macros)<br>
<b>Comment:</b> Insert → Comment · <b>Protect:</b> Tools → Protect Sheet<br><b>Link:</b> Insert → Hyperlink (<kbd>Ctrl</kbd>+<kbd>K</kbd>) · <b>Sources:</b> <kbd>F4</kbd><br>
<b>Share:</b> Tools → Share Spreadsheet</p></div>
<div class="card"><h2>Base paths</h2>
<p><b>New DB:</b> File → New → Database (.odb)<br><b>Tables:</b> Tables → Create Table in Design View (🔑 PK)<br>
<b>Relationship:</b> Tools → Relationships → drag PK→FK → RI tick<br><b>Query:</b> Queries → Create Query in Design View → <kbd>F5</kbd><br>
<b>Grid:</b> FATSVC · AND same row / OR next row · <code>*</code> many, <code>?</code> one<br>
<b>Form/Report:</b> panels → Use Wizard · Label shows, Text Box stores</p></div>
<div class="card"><h2>Numbers &amp; helplines</h2>
<p><b>50–70 cm:</b> screen distance · <b>20-20-20:</b> eye break<br><b>90°:</b> knees · feet flat · keyboard @ elbow<br>
<b>101:</b> fire · <b>100:</b> police · <b>102/108:</b> ambulance<br><b>PASS:</b> Pull-Aim(base)-Squeeze-Sweep<br><b>Fire triangle:</b> Fuel + Heat + Oxygen<br><b>Shock:</b> DON'T touch → power OFF → dry stick</p></div>
</div>
<h2>DBMS keys in 30 seconds</h2>
<table><tr><th>Key</th><th>Meaning</th><th>Example</th></tr>
<tr><td>Primary</td><td>Unique + NOT NULL, one/table</td><td>RollNo</td></tr>
<tr><td>Foreign</td><td>Copy of parent's PK</td><td>STUDENT.ClassID</td></tr>
<tr><td>Candidate</td><td>Could be PK</td><td>RollNo, AdmissionNo</td></tr>
<tr><td>Alternate</td><td>Candidate not chosen</td><td>AdmissionNo</td></tr>
<tr><td>Composite</td><td>PK of 2+ columns</td><td>(ClassID, RollNo)</td></tr>
<tr><td>Degree / Cardinality</td><td>#columns / #rows</td><td>4 / 50</td></tr></table>
<h2>Shortcut strip</h2>
<table><tr><th>Shortcut</th><th>Use</th><th>Shortcut</th><th>Use</th></tr>
<tr><td><kbd>Ctrl</kbd>+<kbd>S</kbd></td><td>Save</td><td><kbd>Ctrl</kbd>+<kbd>K</kbd></td><td>Hyperlink</td></tr>
<tr><td><kbd>F11</kbd></td><td>Styles</td><td><kbd>F4</kbd></td><td>Data Sources</td></tr>
<tr><td><kbd>F5</kbd></td><td>Run query / Navigator</td><td><kbd>Ctrl</kbd>+<kbd>P</kbd></td><td>Print</td></tr>
<tr><td><kbd>Ctrl</kbd>+<kbd>Z</kbd></td><td>Undo</td><td><kbd>Ctrl</kbd>+<kbd>F</kbd></td><td>Find</td></tr>
<tr><td><kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>C</kbd></td><td>Comment</td><td><kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>E</kbd></td><td>Track Changes</td></tr>
<tr><td><kbd>Win</kbd>+<kbd>L</kbd></td><td>Lock PC</td><td><kbd>F2</kbd></td><td>Rename file</td></tr></table>
<h2>Answer frames that fetch full marks</h2>
<ol class="steps"><li><b>1-mark:</b> one exact term + one example.</li>
<li><b>2-mark:</b> define in one line → 2 points/compare → 1 example (20–30 words).</li>
<li><b>4-mark:</b> define → numbered steps with menu paths → example → benefit/precaution (50–80 words).</li>
<li><b>Safety case-study:</b> hazard → prevention → response order → report + helpline.</li></ol>
<h2>Night-before checklist</h2>
<label class="check"><input type="checkbox"> 7 Cs + SMART expansion + Brundtland line by heart</label>
<label class="check"><input type="checkbox"> F11 / Ctrl+K / F4 / F5 / Ctrl+Alt+C recalled</label>
<label class="check"><input type="checkbox"> ToC, Goal Seek F-T-V, macro record, query grid steps revised</label>
<label class="check"><input type="checkbox"> Keys table + 1:N + RI + wildcards revised</label>
<label class="check"><input type="checkbox"> 50–70, 20-20-20, PASS, evacuation order, 101/102/108 revised</label>
<label class="check"><input type="checkbox"> One timed sample paper attempted (30 + 80 + 10 min)</label>
<div class="warning"><b>Last check:</b> LibreOffice names (not MS), labelled diagrams, units on numbers, saved work, privacy, official board instructions.</div>"""

if __name__ == "__main__":
    (ROOT / "index.html").write_text(page("Home · IT 402", "CBSE Class 10 IT 402 2026-27 study guide — 20 detailed chapters", "index.html", INDEX), encoding="utf-8")
    (ROOT / "syllabus.html").write_text(page("Syllabus · IT 402", "CBSE Class 10 IT 402 2026-27 syllabus and paper pattern", "syllabus.html", SYLLABUS), encoding="utf-8")
    (ROOT / "revision.html").write_text(page("Revision · IT 402", "IT 402 exam-morning cheat sheet", "revision.html", REVISION), encoding="utf-8")
    print("index, syllabus, revision written")
