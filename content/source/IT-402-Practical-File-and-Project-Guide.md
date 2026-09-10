# IT 402 – Practical File + Project + Viva Guide (50 marks)
### Class 10 | Practical Exam 30 + Project 10 + Portfolio/File 10

## Marks split (remember this!)

| Component | Marks | What happens |
|---|---|---|
| Writer practical | 5 | 1 task on computer (styles / images / ToC / template / track changes) |
| Calc practical | 5 | 1 task (consolidate / subtotal / scenario / goal seek / macro / linking / sharing) |
| Base practical | 10 | 1–2 tasks (table + relationship + query + form/report) |
| Viva Voce | 10 | Oral questions from all units (see list below) |
| Project / Field Visit | 10 | Real-world case study: form entry + report output in Base + documentation in Writer |
| Portfolio / Practical File | 10 | Neat file with printouts: min. 5 Writer + 5 Calc + 5 Base practicals |

---

## 1. Practical File – 15 must-do practicals (do these exactly)

### A. Writer – Digital Documentation (any 5+)

**W1. Styles:** Create 2-page document “My School” → open Styles (F11) → list the 6 categories → apply Heading 1, Heading 2, Text Body → create a new style “MyHeading” using From Selection → update it (change colour) → show whole doc updates.
**W2. Fill Format + Load Style:** Type 5 paragraphs → use Fill Format to paint Heading 2 on alternate paras → Load a style from another document (Load Styles from Template) → apply it.
**W3. Images:** Insert one image by each method (Insert Image / Drag-Drop / Copy-Paste / Link) on 4 pages → resize one, crop one → add 2 drawing objects (rectangle + arrow) → set fill/line colour → Group them.
**W4. Anchoring + Wrapping:** Insert 1 image 4 times → set anchors To Page / To Paragraph / To Character / As Character → apply Page Wrap / Wrap Left / Wrap Right / No Wrap → write one line under each explaining behaviour.
**W5. ToC:** Create 4-page report with Heading 1 (chapters) + Heading 2 (sections) → Insert → ToC and Index → Table of Contents → customise title + levels → then add a new section → Update Index → take before/after printouts.
**W6. Templates + Track Changes:** Save W5 as Template (.ott) via File → Templates → Save as Template → create new doc from it → turn ON Track Changes (Record) → make 5 edits + add 2 comments (Ctrl+Alt+C) → Accept 3, Reject 2 via Manage → Compare with original via Compare Document.

### B. Calc – Spreadsheet (any 5+)

**C1. Consolidate:** Make 3 sheets (Branch A/B/C monthly sales) → on Summary sheet use Data → Consolidate → Function SUM → add 3 ranges → OK → verify totals.
**C2. Subtotals:** Student marks sheet (Class, Name, Marks) → Sort by Class → Data → Subtotals → Group by Class → Function AVERAGE on Marks → OK → show Collapse/Expand (+/−) → then Remove subtotals.
**C3. Scenario + Goal Seek:** Fees model: Total = Students × Fee. Create 3 Scenarios (Low 100, Expected 150, High 200 students) via Tools → Scenarios → switch and note totals. Then Goal Seek: set Total = 500000 → variable cell = Fee → find required fee. Screenshot both.
**C4. Macro:** Record a macro (Tools → Macros → Record) that bolds headers + adds background + autosizes columns → Stop → save in My Macros as “FormatSheet” → run it on a fresh unformatted sheet. Also write one Function-macro e.g. `BONUS(salary)` returning 10%.
**C5. Linking:** Create Book1 (summary) + Book2 (data) → in Book1 type `=` → click Book2 cell → Enter (external reference created) → Insert → Hyperlink (Ctrl+K) from summary to detail sheet → edit then remove one hyperlink → note relative vs absolute path difference.
**C6. Sharing + Comments:** Tools → Share Spreadsheet → ON → save copy → Edit → Track Changes → Record → two “users” edit different cells → Insert → Comment on one cell → Manage → Accept/Reject → Merge a second copy via Merge Document.

### C. Base – Database (any 5+)

**D1. Tables (both methods):** Create `school.odb` → Table 1 STUDENT via Wizard (RollNo, Name, Class, Marks) → Table 2 CLASS via Design View (ClassID, ClassName, Teacher + set ClassID as Primary Key with AutoValue) → set both primary keys → save.
**D2. Data + Sort:** Enter 10 records in STUDENT → practise First/Prev/Next/Last navigation → Sort by Marks Descending → delete 1 record → show record count.
**D3. Relationships:** Tools → Relationships → add STUDENT + CLASS → drag CLASS.ClassID → drop on STUDENT.ClassID → tick Enforce referential integrity → save. Try entering invalid ClassID → note the error (proves integrity works).
**D4. Queries:** Query 1 (Wizard): names + marks of Class X. Query 2 (Design View): `Marks > 80` sorted descending, hide Class column (untick Visible). Query 3: `LIKE 'A*'` names + `AVG(Marks)` calculation. Run each (F5) + screenshot output.
**D5. Form:** Forms → Wizard on STUDENT → all fields → columnar layout → finish → open form → add 2 records via form → Find one record (binoculars) → Edit mode: change a Label text + background colour → save.
**D6. Report:** Reports → Wizard on topper query → group by Class → sort by Marks desc → tabular layout → title “Class X Toppers” → finish → Edit: insert Title + Date & Time → print preview → export/print 1 page.

> **File presentation tips (fetch full 10):** Index page + dated certificate + one practical per 2 pages (left = steps/objective, right = screenshot/printout) → spiral bind → every page signed. Examiners reward neatness + correct menu paths written under screenshots.

---

## 2. Project Work / Field Visit (10 marks) – do ONE case study

**Requirement:** Interdisciplinary real-world case study → input via **Forms**, output via **Reports** in Base → documentation in **Writer**. (~8–12 pages.)

**Easiest high-scoring topics (pick one):**
1. School Library Management (Books, Members, Issue/Return)
2. Canteen Sales Tracker (Items, Daily Sales, Monthly Report)
3. Class Attendance & Marks Register
4. Sports Day / Annual Fest Event Management

**Recommended structure (copy this):**
1. Cover + Certificate + Acknowledgement (1 page)
2. Introduction / Objective of study (why this system? problem with registers?) (1 page)
3. Requirement / Tables planned (list tables + fields + keys) (1 page)
4. Database design: table structures + relationship diagram screenshot (2 pages)
5. Data entry screenshots via **Form** (2 pages, 5+ records)
6. Query + **Report** output screenshots (1–2 pages, e.g. “Defaulters list”, “Top sellers”)
7. Conclusion + Learning + Future scope (1 page)
8. Bibliography (NCERT/CBSE book, LibreOffice help)

**Field-visit alternative (if school asks):** Visit a data-entry centre/cyber café/bank back-office → note location, computers, printers/scanners, software, sitting posture/ergonomics, manpower, costs/income if shared → 2-page report + photos (with permission) + learnings. Attach visit proof (letter/photo).

---

## 3. Viva Voce – 30 most-asked questions (10 marks)

**Writer:** 1) What is a style? Name categories. 2) F11 does what? 3) Fill Format use? 4) Two ways to create a style? 5) Link vs embed image? 6) Anchoring options? 7) Wrapping options? 8) Steps to create ToC? 9) What is a template (.ott)? 10) Track Changes + comment shortcut?
**Calc:** 11) Consolidate vs Subtotal? 12) Why sort before subtotal? 13) Scenario vs Goal Seek? 14) Goal Seek needs what 3 inputs? (formula cell, target, variable cell) 15) Solver advantage? 16) What is a macro? Where stored? 17) Record macro path? 18) Relative vs absolute hyperlink? 19) F4 in Calc? 20) Share + Merge paths?
**Base:** 21) Data vs Information? 22) DBMS advantages (any 3)? 23) Three data models? 24) Primary vs foreign key? 25) Degree vs cardinality? 26) .odb file? Table creation methods? 27) Relationship types + example? 28) Referential integrity? 29) Wizard vs Design View query? 30) Form vs Report + two form controls?

> **Viva tips:** Answer in 2–3 lines + one example. If asked “show me”, do it on screen confidently. Say menu paths aloud (“Tools → Scenarios”) – examiners love that. Never say “MS Word/Excel” – always **LibreOffice Writer/Calc/Base**.

---

## 4. One-week practical prep plan

| Day | Task (2 hrs) |
|---|---|
| 1 | W1–W3 on computer + write file pages |
| 2 | W4–W6 + ToC/template revision |
| 3 | C1–C3 (consolidate/subtotal/scenario/goal seek) |
| 4 | C4–C6 (macro/linking/sharing) |
| 5 | D1–D3 (tables + relationships) |
| 6 | D4–D6 (query + form + report) + print file |
| 7 | Project screenshots + viva Qs aloud + 1 timed sample paper |

You’re set! Practicals are the easiest 50/100 – neat file + confident viva = full marks.

---

## 5. ADVANCED PRACTICE SET — 10 more tasks (for 95%+ scorers)

**W7. Newsletter with columns + drop cap:** Create a 2-page newsletter → Format → Page → Columns (2) → insert a drop cap via Format → Paragraph → Drop Caps → add header/footer with page numbers → export PDF. *Shows page styles + layout control.*

**W8. Mail-merge-style labels (manual):** Build a table of 10 addresses → use Tools → Mail Merge concepts via Base-registered addresses (View → Data Sources, F4) → drag fields into label frames → print one sheet. *Links Writer + Base (impresses examiners).*

**C7. Grade calculator with IF + charts:** Marks sheet → add Grade column using `=IF(B2>=90,"A",IF(B2>=75,"B","C"))` → Data → Subtotals per Class → Insert → Chart (column) → title + axis labels → print. *Formulas + analysis + presentation in one file.*

**C8. Attendance dashboard with linking:** One file per month (Jan/Feb/Mar sheets) → summary sheet pulls `=Jan.B2+Feb.B2+Mar.B2` → hyperlinked index (Ctrl+K) → conditional formatting for <75% (Format → Conditional) → protect summary (Tools → Protect Sheet). *Linking + protection.*

**C9. Macro button panel:** Record 3 macros (FormatSheet, SortByMarks, AddDate) → View → Toolbars → Form Controls → insert 3 push Buttons → assign each macro (right-click → Control → Events) → one-click panel. *Macros + controls together.*

**D7. Library mini-system (3 tables + junction):** BOOKS(BookID*, Title) + MEMBERS(MemberID*, Name) + ISSUE(IssueID*, BookID, MemberID, Date) with two 1:N relations + RI → enter 8 issues → query “books issued this month” → report grouped by member. *Full M:N via junction — project-ready.*

**D8. Parameter-style queries:** Build 3 Design-View queries on STUDENT — toppers (`Marks>80` desc), failures (`Marks<40`), name search (`LIKE '*a*'`) → add `COUNT(*)` and `AVG(Marks)` row → save as Q-Top/Q-Fail/Q-Find. *Criteria + wildcards + aggregates.*

**D9. Form with list box + report with totals:** Form on STUDENT with Class as List Box (typed values X-A/X-B) → add 3 records via form → report on topper query grouped by Class with `SUM`/`AVG` in footer + Title + Date + page numbers → export PDF. *Controls + grouped totals.*

**M1. Mixed mini-project (all 3 apps):** Pick “Canteen Sales” → Base: ITEMS + SALES tables + bill report → Calc: import sales via F4 + monthly chart + Goal Seek (price for ₹50,000 target) → Writer: 3-page report (styles + ToC + chart image + template). *Exactly what the 10-mark project wants.*

> **File tip:** Advanced tasks go on coloured separator pages in your file — examiners notice effort organisation instantly.

---

## 6. MOCK PRACTICAL EXAM (90 minutes · 30 marks — simulate for real!)

**Rules:** No notes. One folder `Mock_YourName/`. Save every 10 minutes. Say menu paths aloud (viva habit).

| Time | Task | Marks |
|---|---|---|
| 0–20 min | **Writer:** 2-page report — Title + Heading 1/2 styles, 1 captioned image (To Paragraph, Optimal wrap), automatic ToC on page 1, footer page numbers. Save `report.odt` + export PDF. | 10 |
| 20–45 min | **Calc:** Branch sales (2 sheets) → Consolidate SUM on Summary → class-marks Subtotal AVERAGE → 2 Scenarios (Low/High) + 1 Goal Seek (find fee for target). Save `analysis.ods`. | 10 |
| 45–75 min | **Base:** `shop.odb` — ITEMS(ItemID* AutoValue, Name, Price) + SALES(SaleID*, ItemID, Qty) with 1:N + RI → 6 rows → query `Qty>10` sorted desc → columnar form + 1 record via form → grouped report PDF. | 10 |
| 75–90 min | Reopen every file, fix errors, rename neatly, write 5-line “what I did” note. | — |

**Marking (self-check):** File opens + requested features visible (60%) · correct menu paths used (20%) · neat naming + PDF evidence (20%). Score ≥25/30 twice → exam-ready.

---

## 7. TROUBLESHOOTING CLINIC (fixes that save marks)

| Problem | Likely cause | Fix |
|---|---|---|
| ToC is empty | Titles are manual bold, not Heading styles | Apply Heading 1/2 (F11) → right-click ToC → Update Index |
| ToC typing vanished | You typed inside the ToC | Retype in body text; “Protect against manual changes” stays ticked |
| Image jumps while typing | Wrong anchor | Right-click → Anchor → To Paragraph (or As Character for inline) |
| Linked image shows red X | Source moved/renamed | Keep images in the same folder; Edit → Links to External Files → relink |
| Subtotals look wrong | Forgot to sort first | Sort by grouping column → Data → Subtotals again |
| Goal Seek says error | Formula cell has no formula / wrong variable | Check `=` formula exists; variable cell must feed the formula |
| Macro won't run | Security High / wrong library | Tools → Options → Security → Medium; save under My Macros |
| Hyperlink follows instead of editing | Left-clicked the link | Right-click → Edit/Remove Hyperlink |
| Query returns zero rows | Criteria too strict / AND-OR row mix-up | Loosen criteria; AND = same row, OR = next row |
| FK entry rejected | No matching PK (or tables unrelated) | Add the parent row first; check Tools → Relationships + RI |
| Report shows no groups | Grouping level not set | Report Wizard → Grouping → pick field (e.g. Class) |
| File lost after power cut | No backup / never saved | Save often (Ctrl+S); keep dated copies + cloud backup |

---

## 8. MORE VIVA — Q31 to Q50 (one-line answers)

| # | Question | Answer |
|---|---|---|
| 31 | Page style vs paragraph style? | Page = margins/headers for the page; paragraph = formatting for one para (Heading 1). |
| 32 | Clone Formatting vs Fill Format? | Clone copies direct formatting once; Fill Format paints a named style repeatedly (Esc exits). |
| 33 | Embed vs link image? | Embed stores copy inside (big, safe); link stores path (small, breaks if moved). |
| 34 | Contour wrap use? | Text follows the image's shaped edge — best for round logos. |
| 35 | .ott vs .odt? | .ott = reusable template master; .odt = one editable document. |
| 36 | Compare Document use? | Shows differences between two drafts as tracked changes. |
| 37 | Consolidate vs Subtotal? | Consolidate merges dispersed ranges; Subtotal groups totals in place (sort first). |
| 38 | Scenario vs Goal Seek direction? | Scenario forward (inputs→outputs); Goal Seek backward (output→input, 1 variable). |
| 39 | Solver vs Goal Seek? | Solver = many variables + constraints; Goal Seek = one variable, none. |
| 40 | My Macros vs document macros? | My Macros work in all files; document macros only in that file. |
| 41 | Relative hyperlink benefit? | Portable — survives when the folder moves together. |
| 42 | F4 in Calc? | Opens Data Sources to drag registered Base data into sheets. |
| 43 | (shared) in title bar? | File is in multi-user shared mode (Tools → Share Spreadsheet). |
| 44 | Degree vs cardinality? | Degree = columns; cardinality = rows. |
| 45 | Candidate vs alternate key? | Candidate could be PK; alternate = candidate not chosen. |
| 46 | Composite key example? | (ClassID, RollNo) together as PK in marks-history. |
| 47 | Junction table purpose? | Implements M:N as two 1:N relations (e.g. ENROLMENT). |
| 48 | Cascade delete danger? | Deleting a parent auto-deletes linked rows — use rarely. |
| 49 | Combo box vs list box? | Combo allows typing new values; list box only offers fixed choices. |
| 50 | PASS + fire triangle? | PASS = Pull-Aim-Squeeze-Sweep; triangle = Fuel + Heat + Oxygen. |

> **Viva habit:** Answer in 2–3 lines + one example + the menu path aloud. Do all 50 aloud twice before the exam.
