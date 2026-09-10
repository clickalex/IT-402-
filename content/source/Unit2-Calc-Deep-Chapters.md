# UNIT 2 – Electronic Spreadsheet (Advanced) | Deep Chapters (10 marks)
### LibreOffice Calc | Ch4 Analyse • Ch5 Macros • Ch6 Linking • Ch7 Share & Review

> Most practical unit. Learn paths by DOING on computer — then theory becomes easy. Calculator + rough sheet recommended while studying Ch4.

---

# Chapter 4: Analyse Data using Scenarios and Goal Seek

## 🎯 Marks lens
3–4 marks. Subtotals rule + Scenario vs Goal Seek + Goal Seek steps = top questions.

## 📖 Deep concepts

### 1. Consolidating Data (Data → Consolidate)
**Idea:** Merge numbers from many ranges/sheets/files into ONE summary table using a function (SUM/AVERAGE/COUNT/MAX/MIN).
**Example:** Branch A, B, C sheets each have Jan–Mar sales → Summary sheet shows total per month.
**Steps:** (1) Click target cell in summary sheet. (2) Data → **Consolidate** → pick Function (SUM). (3) Click each Source range (drag or type, e.g. `$BranchA.$B$2:$D$5`) → Add (repeat for all). (4) Options: tick *Link to source* if auto-update wanted → OK.
**Exam line:** “Consolidate aggregates dispersed data; Subtotal summarises grouped data in place.”

### 2. Groups and Subtotals
**Group (Data → Group):** Collapses rows/columns with **+/− outline buttons** for tidy viewing (e.g. hide Jan–Nov, show Dec). Ungroup to restore. Purely visual — values unchanged.
**Subtotals (Data → Subtotals):** Auto-inserts total rows per group using SUBTOTAL().
**⚠️ IRON RULE: SORT FIRST by the grouping column.** (Unsorted → garbage groups.)
**Steps:** (1) Sort by group col (e.g. Class: A→Z). (2) Data → Subtotals → *Group by:* Class → *Calculate subtotals for:* Marks → *Use function:* AVERAGE/SUM/COUNT → OK. (3) Outline levels 1/2/3 appear: 1=grand total, 2=group totals, 3=full detail. (4) Remove: Data → Subtotals → **Remove**. Max 3 nested groups (e.g. Class → Section → Gender).
**Functions choice:** SUM (total sales), AVERAGE (class average), COUNT (students per class), MAX/MIN (topper/lowest).

### 3. What-if Analysis & Scenarios (Tools → Scenarios)
**What-if =** “What happens to OUTPUT if I change INPUTS?” (Forward thinking.)
**Scenario =** A NAMED saved set of inputs you can switch instantly.
**Example:** Profit = (Price − Cost) × Students. Scenarios: Pessimistic (100 students, ₹500), Expected (150, ₹600), Optimistic (200, ₹700). Switch → profit recalculates → compare side by side.
**Steps:** (1) Build model with formulas. (2) Tools → **Scenarios** → Add → name (`Expected`) → select Changing cells (inputs) → OK → enter values → OK. (3) Repeat for others. (4) Switch via Tools → Scenarios → Show, or Navigator → Scenarios. Changing cells get coloured border. Optionally tick *Prevent changes / Copy back* protections.
**Show in report:** Scenario summary can be pasted as table for comparison.

### 4. Goal Seek (Tools → Goal Seek) — BACKWARDS
**Idea:** “What INPUT gives my dream OUTPUT?” Only **ONE variable cell**, and result cell MUST contain a formula.
**Example:** Total = Term1 (85) + Term2 (?) → want Total 180 → Goal Seek finds Term2 = 95.
**Steps:** (1) Build formula cell (e.g. C1 `=A1+B1`). (2) Tools → **Goal Seek** → *Formula cell:* C1 → *Target value:* 180 → *Variable cell:* B1 → OK. (3) Dialog shows result → Yes to keep. 
**Inputs trio to memorise: Formula cell + Target value + Variable cell.**

### 5. Solver (Tools → Solver) — Goal Seek's big brother
**Use when:** MULTIPLE variable cells + constraints. *Example:* Maximise profit by adjusting price AND quantity, subject to budget ≤ ₹50,000 and stock ≤ 500 units.
**Needs:** Objective cell (formula to maximise/minimise/match), Variable cells (many), Constraints (e.g. B2 ≤ 50000). Harder; just know “Solver = multi-variable + constraints; Goal Seek = single variable, no constraints.”

## 🧠 Tricks
- **“Sort-Subtotal-Scenario-Seek”** (4 S's in Ch4 order).
- Scenario = **Many inputs → see outputs** (forward 📈). Goal Seek = **One output → find input** (backward 📉). Draw arrows in answer!
- Goal Seek trio: **F-T-V** (Formula, Target, Variable).

## ⚠️ Mistakes
- Subtotal without sorting (0 marks for steps).
- Saying Goal Seek changes many cells (it changes ONE).
- Swapping Scenario/Goal Seek directions.

## ❓ Exam Q&A
**1-mark:** “Sort before?” → Subtotals. “F-T-V belongs to?” → Goal Seek. “Multi-variable tool?” → Solver.
**2-mark:** *Scenario vs Goal Seek.* → Scenario saves input sets to compare outputs (forward, many inputs); Goal Seek finds input for fixed output (backward, one variable).
**4-mark:** *Explain Goal Seek with example + steps.* → Def + example (marks/fees) + 3-step F-T-V + one-variable rule.

## 💻 Practical (C1–C3)
“Sales Analysis”: 3 branch sheets → Consolidate SUM → Class-marks Subtotal AVERAGE → Fee-model 3 Scenarios + 1 Goal Seek (target total). Screenshot each dialog + result.

---

# Chapter 5: Using Macros in Spreadsheet

## 🎯 Marks lens
2–3 marks. Record path + storage + macro-as-function = the trio.

## 📖 Deep concepts

**1. What is a Macro?** Saved sequence of actions (or LibreOffice Basic code) replayed in one click. *Example:* Daily attendance sheet needs bold headers + date + border + sort — record once, run daily. Benefits: speed, zero errors, consistency.

**2. Recording (exact path):** Tools → Macros → **Record Macro** → red recording indicator → perform actions (format/sort/filter — avoid mouse-only selections where possible) → **Stop Recording** → dialog → save under **My Macros** (Standard library) → name (`FormatDaily`) → Save.
*Stored where?* **My Macros & Dialogs → Standard** (global, all files) vs *Current Document* (only this file). Mention this line for full marks.

**3. Running:** Tools → Macros → **Run Macro** → expand My Macros → select → Run. Faster: assign to toolbar icon / menu / shortcut key / button (Tools → Customise) or to an event (file open).

**4. Creating & Organising (manual coding):** Tools → Macros → **Organise Macros → LibreOffice Basic** → My Macros → New Module → type/edit code → Compile → Save. Organiser buttons: New/Edit/Delete/Rename libraries & modules. *Use:* fix recorded code, add logic (loops, IF).

**5. Macro as a Function:** Write macro as `Function` → use like built-in formula in cells.
```basic
Function BONUS(salary)
    BONUS = salary * 0.10
End Function
```
Cell: `=BONUS(B2)` → returns 10% of B2. Reusable across sheet like SUM().

**6. Passing Arguments:** Values in brackets customise behaviour: `DISCOUNT(price, rate)`. **Arguments as values** = passing actual data (`DISCOUNT(1000, 0.1)`, or cell refs) so one macro handles many cases dynamically. Order matters: 1st value → 1st parameter.

**7. Accessing cells directly (code peek — know the idea):**
```basic
ThisComponent.Sheets(0).getCellByPosition(0,0).Value = 100  ' writes 100 into A1
```
`getCellByPosition(col,row)` — 0-based (0,0)=A1. `.Value` for numbers, `.String` for text.

**8. Sort columns using macro:** Record: select data range → Data → Sort → key(s) + Asc/Desc + *Range contains column labels* → OK → Stop. Run on next month's data → same sort instantly. (Mention “record sort steps once, replay on similar data”.)

**9. Macro Security (1-mark favourite):** Tools → Options → Security → **Macro Security** → Very High/High/Medium/Low. Medium = asks before running unsigned macros (recommended). Never enable macros from unknown files (virus risk).

## 🧠 Tricks
- Path chant: **"Tools-Macros-Record-Run-Organise"**.
- Storage: **"My Macros = Mine for all files; Document = for this file only."**

## ⚠️ Mistakes
- Saying macros stored “in Excel” / forgetting **My Macros** name.
- Recording with absolute chaos (random clicks) — plan steps BEFORE recording.
- Forgetting macro-as-function needs `Function`, not `Sub`.

## ❓ Exam Q&A
**1-mark:** “Record path?” → Tools→Macros→Record. “Storage?” → My Macros. “Security path?” → Tools→Options→Security.
**2-mark:** *What is macro? One use.* → Recorded action-sequence automating repetitive tasks; e.g. one-click daily formatting/sorting.
**4-mark:** *Recording steps + macro as function.* → Record 5 steps + storage (2) + Function idea + BONUS example + arguments-as-values line (2).

## 💻 Practical (C4)
“Macro Magic”: Record `FormatSheet` (bold header + yellow fill + autosize + sort by Marks desc) → run on 3 raw sheets → write BONUS function → demo `=BONUS(B2:B11)` → screenshot macro organiser.

---

# Chapter 6: Linking Spreadsheet Data

## 🎯 Marks lens
2–3 marks. Reference syntax + hyperlink types + F4 = favourites.

## 📖 Deep concepts

**1. Multiple sheets:** Insert: Insert → Sheet / `+` tab / right-click tab → Insert Sheet. Rename: double-click tab. Move/Copy: right-click → Move or Copy Sheet (tick *Copy* for duplicate, even to another file). Colour tabs (right-click → Tab Colour) for clarity. Reference same-file cell: `Sheet2.A1` or with spaces `'Branch A'.B2`.

**2. Reference to other SHEETS (same file):**
- **By mouse:** type `=` in target → click source sheet tab → click cell → Enter. (Calc writes `='Sheet2'.A1` automatically.)
- **By keyboard:** type manually: `=SUM(Sheet2.A1:A10)` or `='Summary'.B2*0.1`.
- Syntax rule: `SheetName.CellAddress`; quote names with spaces/special chars.

**3. Reference to another DOCUMENT (external):**
- **By mouse:** open both files → `=` in target → switch window → click source cell → Enter. Calc inserts full path: `='file:///home/user/data.ods'#$Sheet1.A1` (`#` = sheet separator, `$` = absolute).
- **By keyboard:** type the path manually (error-prone; prefer mouse).
- Update: Edit → Links to External Files → Update/Manage/Break. Broken if source moved/renamed → keep files in same folder.

**4. Hyperlinks (Ctrl+K):** Click-to-jump to cell/sheet/file/webpage/email.
- **Create:** Insert → Hyperlink (or Ctrl+K) → left tabs: Internet (URL `https://…`), Document (sheet/cell/bookmark in file), Mail (email+subject), New Document → set Target + Text → Apply. Link shows blue+underlined; **Ctrl+Click to follow** in Calc.
- **Relative vs Absolute (classic 2-marker):**
  | Type | Stores | Example | Moves well? |
  |---|---|---|---|
  | Relative | Path from current file | `../data/sales.ods` | ✅ Yes (folder moved together) |
  | Absolute | Full path/URL | `https://site.com/f.ods`, `C:\docs\f.ods` | ❌ Breaks if file moves |
  Default: Tools → Options → Load/Save → General → *Save URLs relative…*.
- **Edit/Remove:** Right-click → **Edit Hyperlink** (change target) / **Remove Hyperlink** (keeps text, kills link) / Open Link. (Don't left-click — it follows the link!)

**5. Link to External Data (Sheet → Link to External Data):** Imports LIVE table/range from URL/file (e.g. daily gold price, school notice table). Steps: Sheet → Link to External Data → enter URL/file → pick Available range/table → OK → set refresh (every N minutes on open). Data updates without retyping.

**6. Link to Registered Data Sources (F4):** LibreOffice can register databases (Base `.odb`) as global sources. View → Data Sources (**F4**) → left pane pick registered DB → table/query → drag into Calc (or use Data → Define Range linking). Register new: Tools → Options → LibreOffice Base → Databases → New → point to `.odb`. *Use:* payroll DB → salary sheet auto-linked.

## 🧠 Tricks
- Syntax chant: **"Sheet-Dot-Cell; File-Hash-Sheet-Dot-Cell"**.
- Ctrl+K = linK. F4 = Four = “Find From database”.
- Relative = **Relative moves with Relatives** (folder family moves together safely).

## ⚠️ Mistakes
- Forgetting quotes around sheet names with spaces.
- Left-clicking hyperlink to edit (follows it!) — must RIGHT-click.
- Confusing Link to External Data (live import) with plain hyperlink (jump only).

## ❓ Exam Q&A
**1-mark:** “Ctrl+K?” → Hyperlink. “F4?” → Data Sources. “`Sheet2.A1` is?” → Inter-sheet reference.
**2-mark:** *Relative vs absolute hyperlink.* → Relative = short portable path (moves safely); Absolute = full URL/path (breaks on move). One example each.
**4-mark:** *References + hyperlinks.* → Same-sheet (mouse/keyboard + syntax) + external doc reference + hyperlink create/edit/remove + relative/absolute.

## 💻 Practical (C5)
“Linked Workbooks”: `data.ods` (raw) + `summary.ods` (`=` click-across reference + SUM) → Ctrl+K index sheet → Edit one link, Remove another → F4 drag a Base table → screenshot formulas showing paths.

---

# Chapter 7: Share and Review Spreadsheet

## 🎯 Marks lens
2 marks. Share path + Record/Accept + Merge = quick scoring.

## 📖 Deep concepts

**1. Sharing (Tools → Share Spreadsheet):** Allows **simultaneous multi-user editing** (same network/shared folder).
- Steps: Save file in shared location → Tools → **Share Spreadsheet** → tick *Allow changes by more than one user…* → OK → Save. Title bar shows **(shared)**.
- Limits in shared mode: can't insert images/charts, merge cells, or change some settings (mention as intelligent extra).
- Disable: untick the same box (only when no other user has it open).

**2. Open & Save shared workbook:** Open normally → edit → Save (Ctrl+S). If same cell changed by two users → **Resolve Conflicts** dialog lists Mine vs Theirs → pick per conflict → OK. Save often to see others' changes (or set auto-update interval in Share dialog).

**3. Record Changes (Edit → Track Changes → Record):** Every edit gets **coloured cell border + hover note** (author, date, old→new value). Must be ON before reviewing. Show/Hide via Edit → Track Changes → Show.

**4. Comments (discuss without changing values):**
- Add: Insert → Comment (**Ctrl+Alt+C**). Edit/Delete/Show: right-click cell → respective option. Format: right-click comment box → font/colour/size. Navigate: Navigator or Next/Previous comment buttons.
- *Comment vs Change:* Comment = discussion note (value untouched); Change = actual edit (value altered).

**5. Reviewing (Edit → Track Changes → Manage):** Lists all changes (author/date/cell/old/new) with filters (by author/date/range) → select → **Accept** (keep) / **Reject** (revert) / Accept All / Reject All. Add your own remark in Description.

**6. Merging & Comparing:**
- **Merge:** Combine MANY edited copies into one: open master → Edit → Track Changes → **Merge Document** → select copies → OK → conflicts resolved → all changes appear tracked.
- **Compare:** Diff two versions: Edit → Track Changes → **Compare Document** → pick file → differences inserted as tracked changes.
- *Writer has Compare only; Calc has Merge + Compare + Share* — favourite examiner trap!

## 🧠 Tricks
- Flow: **S-O-R-C-R-M** (“Sir, Our Revision Can Require Merging”): Share, Open/Save, Record, Comment, Review, Merge.
- Shared title bar shows **(shared)** — write this detail, examiners smile.

## ⚠️ Mistakes
- Saying Share path is Edit menu (it's **Tools → Share**; Track Changes is **Edit** menu).
- Mixing Manage (accept/reject list) with Record (tracking ON/OFF).
- Forgetting Ctrl+Click vs right-click rules from Ch6 still apply.

## ❓ Exam Q&A
**1-mark:** “Share path?” → Tools→Share. “Comment?” → Ctrl+Alt+C. “Conflict dialog appears on?” → Save with same-cell edits.
**2-mark:** *Comment vs Recorded change.* → Comment discusses (value same); change alters value with coloured border + author note.
**4-mark:** *Collaboration cycle in Calc.* → Share ON → users edit → Record tracks → Comments discuss → Manage accept/reject → Merge copies → conflicts resolved.

## 💻 Practical (C6)
“Team Sheet”: Share ON → User A edits prices, User B edits qty (simulate via two copies) → Comments on 2 cells → Manage accept/reject → Merge copies → screenshot Manage dialog + Resolve Conflicts.

---

## ✅ Unit 2 Final Checklist
- [ ] Consolidate steps • [ ] SORT-before-Subtotal + Remove + 3 levels
- [ ] Scenario create/switch • [ ] Goal Seek F-T-V + 1-variable rule • [ ] Solver = multi + constraints
- [ ] Macro Record/Run/Organise + My Macros + Function + Security
- [ ] Sheet refs + external refs syntax • [ ] Ctrl+K + Relative/Absolute + Edit/Remove • [ ] F4 + Sheet→Link External Data
- [ ] Tools→Share + (shared) + Resolve Conflicts + Record/Manage + Merge vs Compare
