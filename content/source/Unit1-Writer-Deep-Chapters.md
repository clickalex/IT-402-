# UNIT 1 – Digital Documentation (Advanced) | Deep Chapters (8 marks)
### LibreOffice Writer | Ch1 Styles • Ch2 Images • Ch3 ToC + Templates + Track Changes

---

# Chapter 1: Introduction to Styles

## 🎯 Marks lens
2–3 marks here. Style categories + Fill Format + new-style methods are the top 3 questions.

## 📖 Deep concepts

**1. What is a Style?** A named, saved bundle of formatting. Apply once → same look everywhere.
*Without styles:* 50 headings formatted by hand = 2 hours + mismatch. *With styles:* change Heading 1 once → all 50 update in 2 seconds. That's **consistency + speed**.

**2. Six categories (with what each controls + example):**
| Category | Controls | Example |
|---|---|---|
| **Page** | Size, margins, orientation, header/footer, background, columns | “First Page” (no header) vs “Left/Right pages” |
| **Paragraph** | Font + alignment + spacing + bullets + tabs for whole para (MOST USED) | Heading 1, Heading 2, Text Body, Caption |
| **Character** | Only selected characters inside a para | Red-bold keyword, hyperlink blue |
| **Frame** | Boxes holding images/text (border, wrap, position) | Photo frame with caption |
| **List** | Bullets/numbering design + levels | Bullet • →, Number 1. 1.1 1.2 |
| **Table** | Borders, shading, header row repeat | Blue-header marks table |

**3. Styles and Formatting window (F11):** Sidebar deck listing all styles. Top icons filter by category. **Double-click = apply.** Right-click = New/Edit/Delete/Hide. Bottom dropdown filters (All/Automatic/Applied…).

**4. Fill Format Mode (paintbrush icon 🎨):** 
- Click style (e.g. Heading 2) → click Fill Format (paint can icon) → cursor becomes bucket → click/drag each para to paint style → **Esc to exit**.
- *Use:* apply one style to 20 scattered paras fast.
- *Don't confuse with Clone Formatting (paintbrush on toolbar)* — Clone copies direct formatting once; Fill Format applies a named style repeatedly.

**5. Creating a new style — 2 methods (full steps):**
- **Method A – From Selection:** (1) Format a para exactly as wanted. (2) F11 → click **New Style from Selection** icon (A+). (3) Type name (`MyChapHead`) → OK. Style appears in list.
- **Method B – Drag and Drop:** (1) Select formatted text. (2) Drag it into F11 window → drop. (3) Name prompt → type name → OK.
- *Right-click → New* is the third manual way (dialog with all tabs) — mention only if asked “any other”.

**6. Updating a style:** (1) Edit any para using that style (e.g. make Heading 1 green + 18pt). (2) In F11, right-click `Heading 1` → **Update Selected Style** (or click update icon). (3) Every Heading 1 in document changes instantly.

**7. Load Styles from Template/Document:** F11 → New Style dropdown (top-right) → **Load Styles from Template** → From File → pick `.ott`/`.odt` → tick categories (Text/Frame/Pages/Numbering) → OK. *Use:* copy school's official styles into your file.

**8. Applying – precise rules:** Paragraph style → click anywhere in para → double-click style. Character style → **select exact letters first** → double-click. Page style → place cursor on that page → double-click (applies from there; use manual page break for clean switch).

## 🖱️ Key paths (memorise)
- F11 • Fill Format = paint icon in F11 • New from Selection = A+ icon • Update = circular-arrow icon • Load = F11 menu → Load Styles

## 🧠 Trick
Categories → **"Pretty Parrots Chirp For Loud Tunes"** (Page Paragraph Character Frame List Table).

## ⚠️ Mistakes
- Saying “6 styles are Heading1…” — those are *examples*, categories are Page/Para/Char/Frame/List/Table.
- Forgetting Esc exits Fill Format.
- Updating style vs editing text: updating changes ALL instances; students often describe retyping.

## ❓ Exam Q&A
**1-mark:** “Margins+header controlled by?” → Page style. “F11?” → Styles window. “Bucket tool?” → Fill Format.
**2-mark:** *Two methods to create new style.* → From Selection (format→A+→name) + Drag-Drop (drag text into F11→name).
**4-mark:** *What are styles? Explain categories + updating.* → Def (1) + 6 categories one line each (2) + update steps (1).

## 💻 Practical (W1)
“Styles Demo”: 2 pages, apply H1/H2/Text Body, create `MyQuote` character style (italic+blue), Fill-Format it on 5 quotes, update H1 colour → screenshot before/after.

---

# Chapter 2: Working with Images

## 🎯 Marks lens
2–3 marks. Insert methods + anchoring + wrapping = guaranteed questions.

## 📖 Deep concepts

**1. Four insertion methods (detail + when to use):**
| Method | Steps | Best when |
|---|---|---|
| **Insert Image** | Insert → Image → From File → select → Open | Normal, reliable; embeds copy |
| **Drag and Drop** | Drag file from folder into Writer | Quick rough layout |
| **Copy-Paste** | Ctrl+C on image, Ctrl+V in doc | From browser/another doc |
| **Link** | Insert → Image → tick **Link** → Open | 100+ photos / shared logo; keeps `.odt` small; ⚠️ breaks if source moves |

*Embed vs Link:* Embed stores image INSIDE file (big file, always visible). Link stores only PATH (small file, needs source present). Check links: Edit → Links to External Files.

**2. Image toolbar modifications:** Select image → toolbar/drag handles appear:
- **Resize:** drag corner handle (Shift+drag = keep ratio; exact: right-click → Position and Size → Width/Height + Keep ratio).
- **Crop:** Crop tool → drag edges inward (cuts margins); right-click → Crop → set cm values.
- **Delete:** select → Delete key.
- Extras: Brightness/Contrast, Colour mode (grayscale), Flip, Border, Shadow, Filters (blur/sharpen), Compression (reduce file size).

**3. Drawing Objects:** Vector shapes (rectangle, ellipse, line, arrows, stars, flowchart, callouts). Insert: View → Toolbars → Drawing → click shape → drag on page. Or Insert → Shape.
- **Properties:** Line (colour/style/width/arrow), Area/Fill (colour/gradient/hatching), Shadow, Transparency, Font (for text inside), Position/Size, Rotation.
- **Resize:** select → drag handles. **Group:** Shift+click multiple → right-click → **Group** (moves/scales as one; essential for diagrams). **Ungroup** to edit parts. **Combine/Arrange** orders overlaps.

**4. Positioning — the big trio (ANCHOR + ARRANGE + WRAP):**

**(a) Anchoring — what image sticks to (4 options, right-click → Anchor):**
| Anchor | Behaviour | Use |
|---|---|---|
| **To Page** | Locked to page number; text edits don't move it | Cover-page logo, watermark |
| **To Paragraph** | Moves with that para | Most figures in reports |
| **To Character** | Glued to a character | Icon inside a line |
| **As Character** | Treated AS a text character (in-line, affects line height) | Small symbols, emoji-like art |

**(b) Arrangement — stack order when overlapping:** Right-click → Arrange → Bring to Front / Forward / Backward / Send to Back (or To Background/To Foreground). *Example:* caption box in front of photo; watermark behind text.

**(c) Alignment — horizontal position:** Left / Center / Right / Justified (Format → Align or toolbar). Works with anchor+wrap.

**(d) Text Wrapping — how text flows (right-click → Wrap):**
| Wrap | Effect |
|---|---|
| **Page Wrap / Optimal Page Wrap** | Text flows both sides (Optimal avoids narrow gaps) |
| **Wrap Left / Wrap Right** | Text only on left / only on right |
| **Wrap Through** | Text flows OVER image (set transparency for watermark) |
| **In Background** | Image behind text (classic watermark) |
| **Contour** | Text follows image shape edge (needs contour line set; great for round logos) |
| **No Wrap** | Image on its own lines; text above/below only |

**Spacing + contour:** Wrap → Edit Contour / Spacing sets gap between image and text (e.g. 0.2 cm each side).

## 🧠 Tricks
- Anchors → **"Page Para Char As"** (big → small attachment). Wraps → **"POL TIB CN"**: Page/Optimal, Left, Through, In-Background, Contour, No-wrap.
- Link memory: **"Link is Light"** (small file) but **"Link is Breakable"**.

## ⚠️ Mistakes
- Mixing Anchor (WHAT it sticks to) with Wrap (HOW text flows) — write both terms correctly.
- Saying To Page “moves with text” — opposite! To Page is FIXED; To Paragraph MOVES.
- Forgetting Group for multi-shape diagrams.

## ❓ Exam Q&A
**1-mark:** “Small file, path only?” → Link. “Behaves like a letter?” → As Character. “Text follows round edge?” → Contour.
**2-mark:** *Embed vs Link.* → Embed stores copy inside (big, safe); Link stores path (small, breaks if source moves/deleted).
**4-mark:** *Explain anchoring options with use.* → 4 anchors × (behaviour + 1 example).

## 💻 Practical (W3+W4)
“Image Lab”: 4 pages (one method each) + grouped logo diagram + same photo shown with 4 anchors and 4 wraps, each labelled with one-line behaviour note.

---

# Chapter 3: Advanced Features of Writer

## 🎯 Marks lens
3–4 marks. ToC steps + Templates + Track Changes = the classic 4-markers of Unit 1.

## 📖 Deep concepts

### A. Table of Contents (ToC)

**1. Idea:** Auto-built list of headings + page numbers that updates itself. Built from **paragraph styles** (Heading 1/2/3…), NOT from big-bold manual text.

**2. Hierarchy of headings (set BEFORE ToC):**
- Heading 1 = chapter (largest)
- Heading 2 = section
- Heading 3 = sub-section … up to 10 levels.
- Apply via F11 double-click or Navigator. Check with View → Navigator (F5) — shows tree.

**3. Creating (exact steps):** (1) Apply heading styles throughout. (2) Click where ToC goes (usually page 2). (3) Insert → Table of Contents and Index → **Table of Contents, Index or Bibliography** → (4) Title “Contents”, tick *Protect against manual changes* → OK. Entries + page numbers + hyperlinks appear.

**4. Customisation (ToC dialog tabs):** Type (title, up to level N), Entries (tab stops, leader dots ……, page-number position), Styles (font per level), Columns, Background, Borders. *Example:* Level 1 bold 14pt, Level 2 normal 12pt, dotted leaders.

**5. Maintaining:** After adding/deleting pages → right-click ToC → **Update Index** (refresh entries + numbers). **Delete Index** removes ToC (headings stay). **Edit Index** reopens dialog. ⚠️ Never type inside ToC manually — updates will wipe it (that's why “Protect” is ticked).

### B. Templates (.ott)

**1. Idea:** Reusable master design (styles + layout + header/footer + placeholder text). Create once → unlimited identical docs (report cards, letters, resumes).

**2. Full lifecycle (learn all 7 verbs — exam loves these):**
| Action | Path |
|---|---|
| **Create/Save** | Design doc → File → Templates → **Save as Template** → name + category → Save (.ott) |
| **Use In-built/Saved** | File → New → **Templates** → pick → Open |
| **Use Online** | Templates dialog → Online search / extensions.libreoffice.org templates |
| **Import** | Manage Templates → **Import** → select .ott |
| **Edit** | Manage Templates → right-click → **Edit** → change → Save (future docs get new look) |
| **Move** | Manage Templates → right-click → Move to folder/category |
| **Export** | Manage Templates → right-click → **Export** (share .ott file with others) |
| **Apply to blank doc** | Open blank → File → Templates → Manage → double-click template (styles pour in) |

**3. Template vs Document:** Template = master mould (.ott, reusable, listed in gallery); Document = one baked copy (.odt, editable freely). Editing template ≠ editing old documents.

### C. Track Changes + Comments + Compare

**1. Track Changes =** Records every insertion (underline/colour), deletion (strikethrough), formatting change with author + timestamp in margins. For teacher-student / team review.

**2. Full workflow (write as 5 steps in 4-marker):**
1. **Prepare:** File → Save As copy (`Report-Review.odt`); keep original safe.
2. **Record:** Edit → Track Changes → **Record** (Ctrl+Shift+E) ON → share file.
3. **Review:** Reviewer edits; changes auto-marked. Insert → **Comment** (Ctrl+Alt+C) for suggestions without altering text.
4. **Accept/Reject:** Author reopens → Edit → Track Changes → **Manage** → click each change → Accept / Reject (or Accept All). 
5. **Finalise:** Turn Record OFF → resolve/delete comments (right-click → Delete) → Save final.

**3. Comments:** Select text → Ctrl+Alt+C → type → Esc. Right-click comment → Reply/Delete/Delete All. Show/Hide via View → Comments.

**4. Compare Documents:** Edit → Track Changes → **Compare Document** → pick original → Writer merges → differences shown as tracked changes. *Use:* “What changed between draft1 and draft2?” without manual reading.

## 🧠 Tricks
- ToC mantra: **"Headings first, Insert second, Update always."**
- Template verbs: **C-U-I-E-M-E-A** (“CUI EMEA”): Create, Use, Import, Edit, Move, Export, Apply.
- Review flow: **P-R-R-A-F** (Prepare, Record, Review, Accept, Finalise).

## ⚠️ Mistakes
- Creating ToC with manual bold text instead of Heading styles → empty ToC.
- Typing inside ToC manually → lost on update.
- Saying “template extension .odt” → it's **.ott**.
- Accept/Reject path: Edit → Track Changes → **Manage** (not “Review tab” — that's MS Word language; avoid in CBSE answer).

## ❓ Exam Q&A
**1-mark:** “ToC built from?” → Heading styles. “.ott?” → Template. “Ctrl+Alt+C?” → Comment. “Ctrl+Shift+E?” → Track Changes Record.
**2-mark:** *Update vs Delete Index.* → Update refreshes entries/numbers after edits; Delete removes the whole ToC block (headings untouched).
**4-mark:** *Explain Track Changes review cycle.* → 5-step P-R-R-A-F with paths + comment use.
**4-mark:** *Template lifecycle.* → Create→Use→Import→Edit→Move→Export→Apply, one line each.

## 💻 Practical (W5+W6)
“Report Project”: 4-page report → ToC + custom leaders → Save as Template → new doc from template → Record ON → 5 edits + 2 comments → Manage (accept 3/reject 2) → Compare with original → print Manage-dialog screenshot.

---

## ✅ Unit 1 Final Checklist
- [ ] 6 style categories + F11 + Fill Format + 2 creation methods + Update + Load
- [ ] 4 image methods + Embed vs Link + Resize/Crop/Delete + Group
- [ ] 4 anchors + Arrange + Align + 7 wraps (with uses)
- [ ] ToC: hierarchy → Insert → customise → Update/Delete
- [ ] Templates: 7 verbs + .ott + vs document
- [ ] Track Changes: 5-step cycle + Manage + Comments + Compare
