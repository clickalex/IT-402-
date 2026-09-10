# UNIT 3 – Database Management System | Deep Chapters (12 marks ⭐ BIGGEST)
### LibreOffice Base (.odb) | Ch8 Intro • Ch9 Tables • Ch10 Relations • Ch11 Queries • Ch12 Forms & Reports

> Read slowly with examples. Master keys + relationships + queries = 8+ marks fixed. Keep the STUDENT/CLASS example running through all chapters.

**Running example (refer everywhere):**
STUDENT(RollNo*, Name, ClassID, Marks) + CLASS(ClassID*, ClassName, Teacher). `*` = primary key.

---

# Chapter 8: Introduction to DBMS

## 🎯 Marks lens
2–3 marks. Data vs Information + advantages + models + keys terminology.

## 📖 Deep concepts

**1. Data vs Information (always asked):**
| Data | Information |
|---|---|
| Raw, unorganised facts | Processed, meaningful, useful |
| “Amit, 92, X” | “Amit (X) scored 92% – Grade A, Rank 2” |
| No decision value alone | Supports decisions |
*Process:* Data → (sorting/calculating/filtering) → Information.

**2. Database & DBMS:** **Database** = organised collection of related data (e.g. school records). **DBMS** = software to create/store/manage/retrieve it (Base, MySQL, Oracle, Access, SQLite). DBMS sits between user and raw files, handling safety/search/sharing.

**3. Advantages over flat files (learn 6 + 1 line):**
1. **No redundancy** – store once, link everywhere (class name once, not in every student row)
2. **Consistency** – one update reflects everywhere (change teacher once)
3. **Integrity/Accuracy** – rules reject bad data (marks > 100 blocked, duplicate RollNo blocked)
4. **Security** – passwords + user rights (teacher edits, student views)
5. **Sharing + concurrency** – many users together, no conflicts
6. **Quick search/query** – “toppers > 90 in 1 sec” vs manual register hunt
7. Bonus: Backup/recovery, standards, less space.

**4. Data Models (3 — with diagram words):**
| Model | Structure | Links | Example | Limitation |
|---|---|---|---|---|
| **Hierarchical** | Tree (root → children), one parent each | 1:N only | Company org-chart, file folders | Rigid; child can't have 2 parents |
| **Network** | Graph (many links) | M:N via pointers | Old telecom routes | Powerful but complex to design |
| **Relational** | TABLES + keys | 1:1, 1:N, M:N (via junction) | Base/MySQL school DB | Needs key planning (easiest overall) |

*Exam line:* “CBSE syllabus uses the Relational model (RDBMS).”

**5. RDBMS Terminology (THE table — memorise cold):**
| Term | Also called | Meaning | In STUDENT example |
|---|---|---|---|
| Table | Relation | Rows + columns grid | STUDENT |
| Row | Tuple / Record | One full entry | (101, Amit, X-A, 92) |
| Column | Attribute / Field | One property | Name |
| Cell value | Data item | Single fact | “Amit” |
| **Degree** | — | No. of COLUMNS | 4 |
| **Cardinality** | — | No. of ROWS | e.g. 50 |
| **Primary Key** | PK | Unique + NOT NULL, one per table | RollNo |
| **Foreign Key** | FK | Copies another table's PK to link | ClassID → CLASS |
| **Candidate Key** | — | All columns that COULD be PK | RollNo, AdmissionNo |
| **Alternate Key** | — | Candidate NOT chosen as PK | AdmissionNo |
| **Composite Key** | — | PK of 2+ columns together | (ClassID + RollNo) in marks-history |

**6. Objects of RDBMS (4):** **Tables** (store), **Queries** (ask/filter/calculate), **Forms** (friendly entry screens), **Reports** (formatted printouts). *Trick: “The Quick Fox Runs”.*

## 🧠 Tricks
- Degree = **D**own? No! Degree = **columns** (think “Degree of table width”). Cardinality = **count of rows**.
- PK vs FK: **“PK is mine; FK is a Xerox of neighbour's PK.”**

## ❓ Exam Q&A
**1-mark:** “Row = ?” → Tuple/Record. “4 cols, 50 rows → degree/cardinality?” → 4 / 50. “Unique+not null?” → Primary key.
**2-mark:** *Data vs Information with example.* → table row + Amit example.
**4-mark:** *Advantages of DBMS (any 4–6).* → 6 points × 1 line each.

---

# Chapter 9: Starting with LibreOffice Base

## 🎯 Marks lens
2–3 marks. Data types + 2 creation methods + primary key + sort/delete.

## 📖 Deep concepts

**1. Base basics:** Free RDBMS; file = **.odb** (contains tables+queries+forms+reports together). Panes: left = Database objects; Tasks = Create…; main = work area. Open: File → Open → `.odb`. New: File → New → Database → *Create new* (wizard: register? yes for F4 use).

**2. Data Types (match carefully — 1-mark MCQ bank):**
| Type | Stores | Example field |
|---|---|---|
| TEXT / VARCHAR(n) | Variable text | Name VARCHAR(50) |
| CHAR(n) | Fixed-length text | Gender CHAR(1) |
| INTEGER / INT | Whole numbers | RollNo |
| DECIMAL(p,s) / NUMERIC | Decimals exact | Marks DECIMAL(5,2), Price |
| DATE / TIME / TIMESTAMP | Calendar/clock | DOB, JoinTime |
| BOOLEAN / YES-NO | True/False | Passed? |
| MEMO / LONGVARCHAR | Long text | Remarks, Address |

**3. Create Table — Method 1: Wizard (fast):** Tables → **Use Wizard to Create Table** → Category (Business/Personal) → Sample table (e.g. Students) → move fields with `>` → set field types/lengths → **Set primary key** (auto or pick field) → name table → Finish. *Best for beginners/standard tables.*

**4. Create Table — Method 2: Design View (full control):** Tables → **Create Table in Design View** → grid: Field Name + Field Type per row → bottom: Field Properties (Length, Default value, Required=Yes/No, AutoValue) → right-click field → **Primary Key** (🔑 icon) → Ctrl+S → name → OK.
*Properties decoded:* Length (max chars), Default (auto-fill if blank), Required=Yes (NOT NULL — must enter), AutoValue=Yes (auto-number IDs 1,2,3…).

**5. Primary key rules:** One per table • unique • NOT NULL • stable (never changes, e.g. RollNo not Name) • short numbers best. Composite: Ctrl+click 2 fields → right-click → Primary Key.

**6. Data operations in datasheet (double-click table):**
- **Enter:** type row-wise, Tab/Enter moves; new empty row auto-adds; close = auto-save.
- **Navigate bar:** ⏮ First ◀ Prev ▶ Next ⏭ Last ➕ New | “Record 3 of 50”.
- **Edit:** click cell → change → leave row (Enter) to commit.
- **Delete record:** select row header (grey box) → Delete key/right-click Delete → confirm (permanent!).
- **Sort:** click column header → Sort Ascending (A→Z, 0→9, oldest→newest) / Descending button; or right-click → Sort. (Multi-col sort → use query instead.)

## ❓ Exam Q&A
**1-mark:** “.odb?” → Base DB. “Auto-number IDs?” → AutoValue. “Record 3 of 50 bar = ?” → Navigation.
**2-mark:** *Wizard vs Design View.* → Wizard: guided, fast, standard fields. Design View: manual field+type+properties+PK, full control.
**2-mark:** *Primary key + 2 rules.* → Unique+NOT NULL identifier, one per table; e.g. RollNo; stable + short.

## 💻 Practical (D1–D2)
`school.odb`: STUDENT via Wizard (10 rows) + CLASS via Design View (PK+AutoValue) → sort Marks desc → delete 1 row → screenshot nav bar.

---

# Chapter 10: Working with Multiple Tables

## 🎯 Marks lens
2–3 marks. 3 relationship types + referential integrity = classic 4-marker material.

## 📖 Deep concepts

**1. Edit/Delete tables:** Right-click table → **Edit** (Design View: add/drop fields, change type ⚠️ may truncate data — backup first) → Save. Right-click → **Delete** (structure + ALL rows gone forever; blocked if enforced relationships exist — delete relation first).

**2. Why relate? (Advantages — 5):** No duplication (teacher name once) • Consistency (one update) • Integrity (no orphan rows) • Saves space • Enables combined queries/reports (student + class + teacher in one output).

**3. Three types (examples = marks):**
| Type | Symbol | Meaning | Example | Implementation |
|---|---|---|---|---|
| **1:1 One-to-One** | 1—1 | One row ↔ exactly one row | PERSON ↔ PASSPORT (one person, one passport) | PK shared or unique FK |
| **1:N One-to-Many** | 1—∞ | One ↔ many (MOST COMMON) | CLASS ↔ STUDENTS | FK on “many” side (STUDENT.ClassID) |
| **M:N Many-to-Many** | ∞—∞ | Many ↔ many | STUDENTS ↔ SUBJECTS | **Junction table** ENROLMENT(StudentID, SubjectID, Marks) splitting into two 1:N |

*Junction table deep-line:* “M:N is physically built as two 1:N relations via a third linking table whose composite PK = both FKs.” (Write this → impress examiner.)

**4. Creating relationships (exact steps):** (1) Both tables saved with PKs; close them. (2) Tools → **Relationships** → Add tables (drag STUDENT + CLASS in). (3) Drag PK field (`CLASS.ClassID`) → drop on FK (`STUDENT.ClassID`) → Relation dialog opens. (4) Tick **Enforce referential integrity** (+ optionally *Update cascade / Delete cascade*) → OK. (5) Line with 1—∞ appears → Save (Ctrl+S).

**5. Referential Integrity (RI) — the guardian rule:** *“Every FK value must match an existing PK (or be NULL).”*
- **Blocks:** entering STUDENT with ClassID `ZZZ` (no such class); deleting CLASS `X-A` while students linked (unless cascade).
- **Cascade options:** Update cascade (change PK → FKs auto-update); Delete cascade (delete PK row → linked rows auto-delete ⚠️ dangerous, use rarely).
- *Orphan record* = FK pointing nowhere — RI prevents these.

## 🧠 Tricks
- “1:N lives on MANY” (FK sits in the many-side table).
- RI mantra: **"No fake foreign keys."**

## ❓ Exam Q&A
**1-mark:** “CLASS–STUDENTS?” → 1:N. “M:N needs?” → Junction table. “Tools→?” → Relationships.
**2-mark:** *What is referential integrity?* → FK must match real PK; blocks invalid entries + unsafe deletes; e.g. no marks for RollNo 999.
**4-mark:** *Three relationship types + example + creation steps.* → table (3) + Tools→Relationships drag + RI tick (1).

## 💻 Practical (D3)
Relate STUDENT–CLASS with RI → try invalid ClassID (screenshot error = proof) → draw 1—∞ line diagram in file.

---

# Chapter 11: Queries in Base

## 🎯 Marks lens
2–3 marks. Wizard vs Design View + criteria + wildcards + functions.

## 📖 Deep concepts

**1. What is a Query?** Saved question producing a live filtered/sorted/calculated VIEW of data. Tables unchanged; re-run anytime (F5). E.g. “Class X students with Marks > 80, sorted desc, showing avg.”

**2. Wizard method (simple):** Queries → **Use Wizard to Create Query** → table → fields (`>`) → sorting → search conditions → grouping/alias → name → Finish. Limits: basic AND conditions, no wildcards/calculations.

**3. Design View method (powerful) — GRID ROWS (memorise order!):**
| Grid row | Purpose | Example |
|---|---|---|
| Field | Column to use | Name |
| Alias | Rename in output | `Topper` instead of Name |
| Table | Source table | STUDENT |
| Sort | Asc/Desc/(not sorted) | Desc on Marks |
| Visible | Tick = show; untick = use-but-hide | Hide ClassID |
| Criterion | Filter rule (AND = same row; OR = next row) | `>80` |
| (Function row*) | Aggregate | AVG, SUM, COUNT |

*Show Function row: View → Functions (or Σ icon).*
**Steps:** Queries → Create Query in Design View → Add table(s) → close dialog → drag fields to grid (or dropdown) → set Sort/Visible/Criterion → Save → **Run F5** → Datasheet view shows answer. Switch views: Design ↔ SQL (View → SQL View shows `SELECT … WHERE …`).

**4. Criteria patterns (with examples on Marks/Class/Name):**
- Single: `>80` (above 80), `='X-A'` (exact class), `>=60 AND <=80`? In grid: `>=60` with second column, or SQL BETWEEN.
- Multiple AND (same Criterion row): Class `='X-A'` AND Marks `>60` → toppers of X-A.
- OR (different rows): Name `='Amit'` on row1, `='Anu'` on row2 → either.
- Date: `>#2026-01-01#`? (Base/HSQL uses `'2026-01-01'` in quotes — write `> '2026-01-01'`.)

**5. Wildcards (LIKE queries):**
| Symbol | Matches | Example | Finds |
|---|---|---|---|
| `*` | Zero/many chars | `LIKE 'A*'` | Amit, Anu, A |
| `?` | Exactly one char | `LIKE 'An?'` | Anu, Ani (not Amit) |
| combos | — | `LIKE '*sh*'` | Asha, Rishi |

**6. Numerical calculations (aggregates):** `SUM(Marks)` total, `AVG(Marks)` average, `COUNT(*)` rows, `MAX/MIN` extremes. In grid: Function row pick + Field `Marks`. Grouping: e.g. AVG per Class → Group By Class + AVG Marks. SQL: `SELECT ClassID, AVG(Marks) FROM STUDENT GROUP BY ClassID;`

## 🧠 Tricks
- Grid chant: **"Field-Alias-Table-Sort-Visible-Criterion"** (FATSVC).
- Wildcards: **Star=Sky (many), Question=one Quiz answer.**

## ❓ Exam Q&A
**1-mark:** “Run query?” → F5. “Hide column?” → untick Visible. “`A*` finds?” → names starting A.
**2-mark:** *Wizard vs Design View.* → Wizard guided/simple; Design grid full power (sort/visible/criteria/functions/SQL).
**4-mark:** *Design-View query with criteria + wildcard + calculation.* → steps + grid rows + `>80` + `LIKE 'A*'` + `AVG(Marks)` example.

## 💻 Practical (D4)
Q1 Wizard (Class X list) • Q2 Design (`Marks>80` desc, hide ID) • Q3 `LIKE 'A*'` + AVG → screenshot outputs.

---

# Chapter 12: Forms and Reports

## 🎯 Marks lens
2 marks. Form controls + Wizard steps + Form vs Report.

## 📖 Deep concepts

**1. Form =** Pretty, one-record-at-a-time screen for entry/view/edit. Hides table complexity; adds logos, buttons, dropdowns, validation. Tables = godown; Forms = shop counter.

**2. Create via Wizard:** Forms → **Use Wizard to Create Form** → table/query → fields → **subform?** (e.g. CLASS master + STUDENT details — yes if 1:N display wanted) → arrange (Columnar/Tabular/Datasheet/Block) → data-entry mode (all records / new-only / no-delete) → style + name → Finish.

**3. Modify:** Right-click form → **Edit** → drag/resize controls, change fonts/colours, add logo (Insert → Image), align via grid → Save. Test in normal (non-edit) mode.

**4. Form Controls Toolbar (View → Toolbars → Form Controls) — know 7:**
| Control | Job | Example |
|---|---|---|
| **Label** | Fixed display text (not stored) | “Name:” heading |
| **Text Box** | Type/edit field data | Name input |
| **Button** | Click action | Save / Next / Close |
| **Check Box** | Yes/No tick | “Passed?” |
| **Radio Button** | One-of-many choice | Gender M/F/O |
| **List/Combo Box** | Dropdown choices | Class list (Combo allows typing new) |
| **Date/Formatted Field** | Validated date/number | DOB picker, Marks (2 decimals) |

*Label vs Text Box is the #1 viva trap: Label shows, Text Box stores.*

**5. Daily form ops:** Open form → navigator (⏮◀▶⏭➕🗑🔍💾): **New record** ➕ → type → Save → Next. **Find:** binoculars → value → search (e.g. Name=`Amit`). **Delete:** 🗑 → confirm.
**Change label/background:** Edit mode → right-click control → Properties → Text/Font/Background colour/Image → OK.

**6. Report =** Formatted PRINT output (marksheet, pay-slip, topper list). Read-only; from table/query; with titles, grouping, totals, page numbers, date.
**Create via Wizard:** Reports → **Use Wizard to Create Report** → table/query → fields → labels → **grouping levels** (e.g. Group by Class — creates section headers + optional subtotals) → sort (Marks desc) → layout (Tabular/Columnar/Stepped/Block) + style → title (`Class X Toppers`) → Finish/Create.
**Polish in Edit mode:** Insert → **Title/Heading** (report name, section heads), Insert → **Date and Time** (fixed print date or auto field), Insert → Page Number, Image (logo), Line/Box controls, background. Print Preview → Print/Export PDF.

**7. Form vs Report (2-marker table):**
| Form | Report |
|---|---|
| Screen for entry/edit (read-write) | Print for reading (read-only) |
| One record focus + navigation | Many records + grouping + totals |
| Controls: Text Box/Button/Combo | Elements: Titles/Headings/Date/Page No. |

## ❓ Exam Q&A
**1-mark:** “Fixed text control?” → Label. “Dropdown?” → List/Combo Box. “Report grouping example?” → by Class.
**2-mark:** *Form vs Report (2 pts).* → table rows above.
**4-mark:** *Form controls + Report wizard.* → 5 controls × 1 line + report 6-step wizard + Title/Date insertion.

## 💻 Practical (D5–D6)
Form on STUDENT (add 2 rows via form, Find 1, recolour Label) + Report “Toppers” (group Class, sort Marks, Title + Date) → print 1 page each.

---

## ✅ Unit 3 Final Checklist
- [ ] Data vs Info • 6 advantages • 3 models • Degree/Cardinality • 5 keys • 4 objects
- [ ] 7 data types • Wizard vs Design table • PK rules • Sort/Delete/Navigate
- [ ] 1:1/1:N/M:N + junction line • Tools→Relationships • RI + cascade meanings
- [ ] Query grid FATSVC • AND/OR rows • `*` `?` + LIKE • SUM/AVG/COUNT + GROUP BY
- [ ] 7 form controls (Label vs Text Box!) • Form wizard + ops • Report wizard + Title/Date • Form vs Report
