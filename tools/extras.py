# Chapter extras: SVG/CSS diagrams + extra exam Q&A bank + quiz data.
# Used by tools/build.py to enrich every chapter page.

DIAGRAMS = {
"pa-u1": """<div class="diagram" role="img" aria-label="Communication cycle: sender encodes message, sends via channel, receiver decodes, feedback returns">
<div class="node">📤<br><b>Sender</b><br><small>encodes idea</small></div><span class="arrow">→</span>
<div class="node">💬<br><b>Message</b><br><small>via channel</small></div><span class="arrow">→</span>
<div class="node">📥<br><b>Receiver</b><br><small>decodes</small></div><span class="arrow">→</span>
<div class="node">↩️<br><b>Feedback</b><br><small>confirms</small></div></div>
<p class="cap">Draw this 7-step loop in 2-mark answers: Sender → Encoding → Message → Channel → Decoding → Receiver → Feedback.</p>""",
"pa-u2": """<div class="diagram" role="img" aria-label="SMART goals: Specific Measurable Achievable Relevant Time-bound">
<div class="node"><b>S</b><br><small>Specific</small></div><div class="node"><b>M</b><br><small>Measurable</small></div><div class="node"><b>A</b><br><small>Achievable</small></div><div class="node"><b>R</b><br><small>Relevant</small></div><div class="node"><b>T</b><br><small>Time-bound</small></div></div>
<p class="cap">Example: “Finish DBMS Ch8–9 + 20 MCQs by Sunday 6 pm” — specific, countable, possible, relevant, dated.</p>""",
"pa-u3": """<div class="diagram" role="img" aria-label="Computer system tree: hardware and software, system software and application software">
<div class="node"><b>🖥️ Computer System</b></div></div>
<div class="diagram"><div class="node"><b>Hardware</b><br><small>keyboard · CPU · monitor · printer</small></div>
<div class="node"><b>Software</b><br><small>System: OS · antivirus · drivers</small><br><small>Application: Writer · Calc · browser</small></div></div>
<p class="cap">LibreOffice Writer is <b>application</b> software. The OS (Windows / Ubuntu) is <b>system</b> software.</p>""",
"pa-u4": """<div class="diagram" role="img" aria-label="Steps to start a business: idea, market survey, plan, finance, setup, launch">
<div class="node">💡<br><small>Idea</small></div><span class="arrow">→</span><div class="node">🔍<br><small>Market survey</small></div><span class="arrow">→</span>
<div class="node">📋<br><small>Business plan</small></div><span class="arrow">→</span><div class="node">💰<br><small>Finance</small></div><span class="arrow">→</span>
<div class="node">🏪<br><small>Set up</small></div><span class="arrow">→</span><div class="node">🚀<br><small>Launch</small></div></div>""",
"pa-u5": """<div class="diagram" role="img" aria-label="Three pillars of sustainable development: environment, society, economy">
<div class="node">🌳<br><b>Environment</b><br><small>protect nature</small></div><span class="arrow">+</span>
<div class="node">🧑‍🤝‍🧑<br><b>Society</b><br><small>health · equity</small></div><span class="arrow">+</span>
<div class="node">💼<br><b>Economy</b><br><small>jobs · growth</small></div></div>
<p class="cap">Sustainable development needs <b>all three</b> pillars together — “ESE” (Easy).</p>""",
"u1-ch1": """<div class="diagram" role="img" aria-label="Six style categories in Writer">
<div class="node">📄<br><small>Page</small></div><div class="node">¶<br><small>Paragraph</small></div><div class="node">A<br><small>Character</small></div>
<div class="node">🖼️<br><small>Frame</small></div><div class="node">•≡<br><small>List</small></div><div class="node">▦<br><small>Table</small></div></div>
<p class="cap">Mnemonic: <b>“Pretty Parrots Chirp For Loud Tunes.”</b> Paragraph styles are used most (Heading 1, Text Body).</p>""",
"u1-ch2": """<div class="diagram" role="img" aria-label="Four anchoring options from biggest to smallest attachment">
<div class="node"><b>To Page</b><br><small>📌 fixed on page</small></div><span class="arrow">→</span>
<div class="node"><b>To Paragraph</b><br><small>moves with para</small></div><span class="arrow">→</span>
<div class="node"><b>To Character</b><br><small>glued to a letter</small></div><span class="arrow">→</span>
<div class="node"><b>As Character</b><br><small>behaves as text</small></div></div>
<p class="cap">Anchor = <b>WHAT</b> the image sticks to. Wrap = <b>HOW</b> text flows around it. Examiners test this pair.</p>""",
"u1-ch3": """<div class="diagram" role="img" aria-label="Table of contents workflow: headings first, insert second, update always">
<div class="node"><b>1. Headings</b><br><small>apply H1/H2/H3 (F11)</small></div><span class="arrow">→</span>
<div class="node"><b>2. Insert</b><br><small>Insert → ToC/Index</small></div><span class="arrow">→</span>
<div class="node"><b>3. Update</b><br><small>right-click → Update</small></div></div>
<p class="cap">Mantra: <b>“Headings first, Insert second, Update always.”</b> Never type inside the ToC manually.</p>""",
"u2-ch4": """<div class="diagram" role="img" aria-label="Scenario goes forward from many inputs to outputs; Goal Seek goes backward from output to input">
<div class="node">📈<br><b>Scenario</b><br><small>many inputs → see outputs</small><br><small><i>forward</i></small></div>
<div class="node">📉<br><b>Goal Seek</b><br><small>1 output → find input</small><br><small><i>backward, 1 variable</i></small></div>
<div class="node">🧩<br><b>Solver</b><br><small>many variables + constraints</small></div></div>""",
"u2-ch5": """<div class="diagram" role="img" aria-label="Macro workflow: record, stop and save, run">
<div class="node">🔴<br><b>Record</b><br><small>Tools → Macros → Record</small></div><span class="arrow">→</span>
<div class="node">💾<br><b>Stop + Save</b><br><small>My Macros · name it</small></div><span class="arrow">→</span>
<div class="node">▶️<br><b>Run</b><br><small>Run Macro / button</small></div></div>
<p class="cap"><b>My Macros</b> = all files. Current document = this file only.</p>""",
"u2-ch6": """<div class="diagram" role="img" aria-label="Reference syntax examples">
<div class="node"><code>Sheet2.A1</code><br><small>same file</small></div>
<div class="node"><code>'file…'#$Sheet1.A1</code><br><small>other file (# = sheet)</small></div>
<div class="node"><kbd>Ctrl</kbd>+<kbd>K</kbd><br><small>hyperlink</small></div>
<div class="node"><kbd>F4</kbd><br><small>data sources</small></div></div>
<p class="cap">Chant: <b>“Sheet-Dot-Cell; File-Hash-Sheet-Dot-Cell.”</b> Right-click (never left-click) to edit a link.</p>""",
"u2-ch7": """<div class="diagram" role="img" aria-label="Collaboration flow: share, edit, record, comment, review, merge">
<div class="node"><small>Share ON</small></div><span class="arrow">→</span><div class="node"><small>Edit + Save</small></div><span class="arrow">→</span>
<div class="node"><small>Record changes</small></div><span class="arrow">→</span><div class="node"><small>Comment</small></div><span class="arrow">→</span>
<div class="node"><small>Manage accept/reject</small></div><span class="arrow">→</span><div class="node"><small>Merge</small></div></div>
<p class="cap">Shared title bar shows <b>(shared)</b>. Same-cell clash on save → <b>Resolve Conflicts</b> dialog.</p>""",
"u3-ch8": """<div class="diagram" role="img" aria-label="Data processed into information; RDBMS objects: tables, queries, forms, reports">
<div class="node">🧱<br><b>Data</b><br><small>raw facts</small></div><span class="arrow">→ process →</span>
<div class="node">💡<br><b>Information</b><br><small>meaningful</small></div></div>
<div class="diagram"><div class="node"><small>Tables<br><b>store</b></small></div><div class="node"><small>Queries<br><b>ask</b></small></div>
<div class="node"><small>Forms<br><b>enter</b></small></div><div class="node"><small>Reports<br><b>print</b></small></div></div>
<p class="cap">Objects trick: <b>“The Quick Fox Runs.”</b> PK = “mine”; FK = “Xerox of neighbour's PK”.</p>""",
"u3-ch9": """<div class="diagram" role="img" aria-label="Table design row: field name, field type, properties, primary key">
<div class="node"><small>Field Name<br><b>RollNo</b></small></div><span class="arrow">+</span>
<div class="node"><small>Field Type<br><b>INTEGER</b></small></div><span class="arrow">+</span>
<div class="node"><small>Properties<br><b>Required · AutoValue</b></small></div><span class="arrow">+</span>
<div class="node">🔑<br><small>Primary Key</small></div></div>
<p class="cap">Wizard = fast guided tables. Design View = full control (name + type + properties + key).</p>""",
"u3-ch10": """<div class="diagram" role="img" aria-label="Relationship types: one-to-one, one-to-many, many-to-many via junction table">
<div class="node"><b>1 — 1</b><br><small>PERSON ↔ PASSPORT</small></div>
<div class="node"><b>1 — ∞</b><br><small>CLASS ↔ STUDENTS</small><br><small>FK on MANY side</small></div>
<div class="node"><b>∞ — ∞</b><br><small>via JUNCTION table</small><br><small>ENROLMENT</small></div></div>
<p class="cap">Referential integrity: <b>“No fake foreign keys”</b> — every FK must match a real PK.</p>""",
"u3-ch11": """<div class="diagram" role="img" aria-label="Query Design View grid rows: field, alias, table, sort, visible, criterion">
<div class="node"><small>Field</small></div><div class="node"><small>Alias</small></div><div class="node"><small>Table</small></div>
<div class="node"><small>Sort</small></div><div class="node"><small>Visible</small></div><div class="node"><small>Criterion</small></div></div>
<p class="cap">Grid chant: <b>FATSVC</b>. AND = same criterion row · OR = next row · Run = <kbd>F5</kbd> · Wildcards <code>*</code> (many) <code>?</code> (one).</p>""",
"u3-ch12": """<div class="diagram" role="img" aria-label="Form for entry versus report for printing">
<div class="node">🖥️<br><b>Form</b><br><small>screen · read-write</small><br><small>Label · Text Box · Button · Combo</small></div>
<div class="node">🖨️<br><b>Report</b><br><small>print · read-only</small><br><small>Titles · Groups · Totals · Date</small></div></div>
<p class="cap">Tables = godown · Forms = shop counter · Reports = printed bill. <b>Label shows, Text Box stores.</b></p>""",
"u4-ch13": """<div class="diagram" role="img" aria-label="Hazard types with icons">
<div class="node">🔊<br><small>Physical</small></div><div class="node">🪜<br><small>Fall</small></div><div class="node">🧽<br><small>Slip/Trip</small></div>
<div class="node">⚡<br><small>Electrical</small></div><div class="node">🔥<br><small>Fire</small></div><div class="node">🤧<br><small>Health</small></div>
<div class="node">🧪<br><small>Chemical</small></div></div>
<p class="cap">Control hierarchy: <b>Eliminate → Substitute → Engineering → Administrative → PPE</b> (last shield).</p>""",
"u4-ch14": """<svg class="fig" viewBox="0 0 420 190" role="img" aria-label="Ergonomic desk: monitor 50 to 70 cm away at eye level, keyboard at elbow height, feet flat, back supported">
<rect x="8" y="8" width="404" height="174" rx="10" class="figbox"/>
<rect x="250" y="40" width="90" height="60" rx="4" class="figscreen"/><rect x="285" y="100" width="8" height="22" class="figstand"/>
<rect x="230" y="122" width="130" height="8" rx="2" class="figdesk"/>
<circle cx="120" cy="70" r="16" class="fighead"/><rect x="104" y="90" width="34" height="52" rx="10" class="figbody"/>
<rect x="98" y="142" width="12" height="30" class="figleg"/><rect x="126" y="142" width="12" height="30" class="figleg"/>
<line x1="138" y1="70" x2="252" y2="60" class="figline"/><text x="150" y="58" class="figtext">50–70 cm · eye level</text>
<text x="60" y="120" class="figtext">90° knees · feet flat</text><text x="230" y="145" class="figtext">keyboard @ elbow</text></svg>
<p class="cap"><b>20-20-20:</b> every 20 min → look 20 feet away → for 20 seconds.</p>""",
"u4-ch15": """<svg class="fig" viewBox="0 0 420 170" role="img" aria-label="Fire triangle: fuel, heat, oxygen; PASS extinguisher steps">
<rect x="8" y="8" width="404" height="154" rx="10" class="figbox"/>
<polygon points="105,130 45,35 165,35" class="figtri"/>
<text x="80" y="60" class="figtext">HEAT</text><text x="52" y="120" class="figtext">FUEL</text><text x="118" y="120" class="figtext">OXYGEN</text>
<text x="210" y="45" class="figtext"><b>PASS:</b> Pull · Aim (base) · Squeeze · Sweep</text>
<text x="210" y="75" class="figtext">⚡ shock → DON'T touch → power OFF → dry stick</text>
<text x="210" y="105" class="figtext">🔥 fire → stairs, NEVER lift → assemble → count</text>
<text x="210" y="135" class="figtext">📞 101 fire · 102/108 ambulance</text></svg>""",
}

# Extra Q&A bank per chapter: 3 one-mark + 1 two-mark + 1 four-mark (with answers).
EXTRA_QA = {
"pa-u1": """<h3>➕ Extra exam Q&amp;A bank</h3>
<div class="qa"><strong>1-mark: Expand the 7 Cs (any four).</strong><br>Clear, Concise, Concrete, Correct, Coherent, Complete, Courteous.</div>
<div class="qa"><strong>1-mark: Encoding happens on whose side — sender or receiver?</strong><br>Sender's side (converting thought into words/gestures); decoding is on the receiver's side.</div>
<div class="qa"><strong>1-mark: Give one example each of oral and written communication.</strong><br>Oral: phone call / meeting. Written: email / report.</div>
<div class="qa"><strong>2-mark: Explain two barriers to communication with one example each.</strong><br>(1) Linguistic barrier — people use different languages, e.g. a client cannot read a French manual. (2) Physical barrier — noise or distance blocks the message, e.g. a faulty phone line during an order call.</div>
<div class="qa"><strong>4-mark (practice): Describe the communication cycle with a data-entry example and the role of feedback.</strong><br>Sender encodes an idea into a message and sends it through a channel; the receiver decodes it and returns feedback. Example: a supervisor dictates a customer record (sender/encoding) over phone (channel); the operator repeats the spelling (decoding + feedback). Feedback confirms understanding, corrects errors early and improves accuracy. Good feedback is descriptive, specific, timely and constructive — e.g. “Row 4's phone number has 9 digits; please recheck” instead of “wrong data”.</div>""",
"pa-u2": """<h3>➕ Extra exam Q&amp;A bank</h3>
<div class="qa"><strong>1-mark: Expand SMART with one example.</strong><br>Specific, Measurable, Achievable, Relevant, Time-bound — e.g. “Finish DBMS Ch8–9 + 20 MCQs by Sunday 6 pm”.</div>
<div class="qa"><strong>1-mark: Name the Big Five (OCEAN) traits.</strong><br>Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism.</div>
<div class="qa"><strong>1-mark: State one physical and one mental effect of unmanaged stress.</strong><br>Physical: headache / poor sleep. Mental: anxiety / poor concentration.</div>
<div class="qa"><strong>2-mark: Two benefits of goal setting for a student.</strong><br>(1) Gives clear direction and measurable targets, so effort stays focused. (2) Builds motivation and time control — small wins tracked daily reduce exam stress.</div>
<div class="qa"><strong>4-mark (practice): You have 10 days before the IT exam and feel stressed. Write a self-management plan.</strong><br>(1) Set SMART targets: e.g. Unit 3 in 4 days, 20 MCQs/day. (2) Make a daily to-do list; prioritise urgent + important first; use 25-min study + 5-min break cycles. (3) Manage stress: 7–8 hrs sleep, exercise/yoga, short walks, talk to family. (4) Track progress on a chart and reward small wins; say no politely to distractions. Review nightly and adjust — planned work finishes on time with less stress.</div>""",
"pa-u3": """<h3>➕ Extra exam Q&amp;A bank</h3>
<div class="qa"><strong>1-mark: What is an operating system? Give two examples.</strong><br>Master software that links user and hardware and manages files, memory and devices — e.g. Windows, Ubuntu/Linux.</div>
<div class="qa"><strong>1-mark: Match: .odt / .ods / .odb.</strong><br>.odt = Writer document, .ods = Calc spreadsheet, .odb = Base database.</div>
<div class="qa"><strong>1-mark: What does Win+L do? Why is it good practice?</strong><br>Locks the screen instantly; protects data on shared PCs.</div>
<div class="qa"><strong>2-mark: Two tips for file organisation on a computer.</strong><br>(1) Use subject-wise folders with meaningful names (IT-Ch8-Notes.odt) instead of dumping on the desktop. (2) Rename (F2), sort by date, delete temp files and keep a dated backup copy.</div>
<div class="qa"><strong>4-mark (practice): Design a weekly computer-care routine for your school lab PC.</strong><br>(1) Daily: proper shutdown, lock screen when leaving, save + backup classwork. (2) Weekly: update OS/antivirus and run a full scan, delete temp files, empty recycle bin. (3) Security: strong unique passwords, firewall on, never click unknown links or share OTPs, verify https sites. (4) Monthly: uninstall unused apps, check backup restore, clean keyboard/screen when switched off. This keeps the PC fast, safe and exam-ready.</div>""",
"pa-u4": """<h3>➕ Extra exam Q&amp;A bank</h3>
<div class="qa"><strong>1-mark: Who is an entrepreneur?</strong><br>A person who starts and runs a business, takes risk and innovates for profit.</div>
<div class="qa"><strong>1-mark: Name any two contents of a business plan.</strong><br>Product/service, target customers, pricing, marketing, finance (any two).</div>
<div class="qa"><strong>1-mark: State one myth and its fact about entrepreneurship.</strong><br>Myth: entrepreneurs are born. Fact: entrepreneurial skills can be learned and practised.</div>
<div class="qa"><strong>2-mark: Differentiate entrepreneur and employee (2 points).</strong><br>(1) Risk/income — entrepreneur bears risk for uncertain profit; employee gets a fixed salary. (2) Decisions — entrepreneur decides independently; employee follows instructions.</div>
<div class="qa"><strong>4-mark (practice): Plan a small data-entry service for local shops.</strong><br>Idea: digitise paper registers into searchable Calc/Base files with weekly backup. Market survey: visit 5 shops, note record problems, check competitors' prices. Business plan: service list, pricing per 100 records, promotion via pamphlets. Finance: start small with home PC (low cost); track profit = price − cost. Risks: data privacy (take consent, restrict access), errors (double-check + checklist). Qualities used: hard work, communication, honesty, persistence. Start with one shop, collect feedback, then grow.</div>""",
"pa-u5": """<h3>➕ Extra exam Q&amp;A bank</h3>
<div class="qa"><strong>1-mark: Define sustainable development (Brundtland).</strong><br>Development that meets present needs without compromising future generations' ability to meet theirs.</div>
<div class="qa"><strong>1-mark: Name the three pillars of sustainable development.</strong><br>Environment, Society, Economy (“ESE”).</div>
<div class="qa"><strong>1-mark: Give two examples of green jobs.</strong><br>Solar panel technician and e-waste manager (also: energy auditor, organic farmer).</div>
<div class="qa"><strong>2-mark: Two ways your school can go green.</strong><br>(1) Switch to LED bulbs, switch off unused lights/fans and use natural light. (2) Segregate wet/dry/e-waste bins, compost leaves, print double-sided and plant trees.</div>
<div class="qa"><strong>4-mark (practice): What is a green economy? How can an IT student support it?</strong><br>A green economy is low-carbon, resource-efficient and socially inclusive growth (solar energy, e-vehicles, recycling). An IT student can: use power-saving settings and shut down labs PCs; proofread on screen and print double-sided only when needed; send e-waste (batteries, keyboards) to authorised recyclers; make e-notes instead of photocopies; spread awareness on World Environment Day (5 June). Small daily habits protect the environment while keeping productivity high.</div>""",
"u1-ch1": """<h3>➕ Extra exam Q&amp;A bank</h3>
<div class="qa"><strong>1-mark: Which style category controls margins and headers?</strong><br>Page style.</div>
<div class="qa"><strong>1-mark: What is the shortcut for the Styles window and how do you apply a style?</strong><br>F11; double-click the style (click in the paragraph first for paragraph styles).</div>
<div class="qa"><strong>1-mark: How is Fill Format different from Clone Formatting?</strong><br>Fill Format applies a named style repeatedly (Esc exits); Clone copies direct formatting once.</div>
<div class="qa"><strong>2-mark: Two advantages of styles over direct formatting.</strong><br>(1) Consistency — one update changes every matching paragraph instantly. (2) Speed + structure — fast formatting and automatic ToC from heading styles.</div>
<div class="qa"><strong>4-mark (practice): Explain style categories and how to create and update a style.</strong><br>A style is a saved bundle of formatting. Six categories: Page (margins/headers), Paragraph (whole para, e.g. Heading 1), Character (selected letters), Frame (image/text boxes), List (bullets/numbers), Table. Create — Method A: format a para → F11 → New Style from Selection (A+) → name → OK; Method B: drag formatted text into F11 → name → OK. Update: edit one instance → right-click style → Update Selected Style → all instances change. Load school styles via F11 → Load Styles from Template.</div>""",
"u1-ch2": """<h3>➕ Extra exam Q&amp;A bank</h3>
<div class="qa"><strong>1-mark: Which image method stores only the path? What is its risk?</strong><br>Linking; the image breaks if the source file moves or is deleted.</div>
<div class="qa"><strong>1-mark: “As Character” anchoring behaves like what?</strong><br>Like a text character inside the line (affects line height, flows with text).</div>
<div class="qa"><strong>1-mark: Which wrap follows a round logo's edge?</strong><br>Contour wrap (after setting the contour line).</div>
<div class="qa"><strong>2-mark: Embed vs Link for images.</strong><br>Embed stores a copy inside the document — bigger file but always visible. Link stores only the path — small file but breaks if the source moves. Check links via Edit → Links to External Files.</div>
<div class="qa"><strong>4-mark (practice): Explain image anchoring options with one use each.</strong><br>Anchoring decides what the image sticks to (right-click → Anchor). To Page: locked to a page number — cover logo/watermark. To Paragraph: moves with that paragraph — most report figures. To Character: glued to one character — inline icon. As Character: treated as a text character — small symbols. Combine with Wrap (how text flows) and Arrange (stack order: bring to front/send to back) for full control. Group multi-shape diagrams (Shift+click → Group) so they move as one.</div>""",
"u1-ch3": """<h3>➕ Extra exam Q&amp;A bank</h3>
<div class="qa"><strong>1-mark: ToC is built from what — bold text or heading styles?</strong><br>Heading paragraph styles (Heading 1/2/3), never manual bold text.</div>
<div class="qa"><strong>1-mark: Template extension? How do you create one?</strong><br>.ott — File → Templates → Save as Template.</div>
<div class="qa"><strong>1-mark: Shortcuts: comment? Track Changes record?</strong><br>Comment = Ctrl+Alt+C; Record = Ctrl+Shift+E.</div>
<div class="qa"><strong>2-mark: Update Index vs Delete Index.</strong><br>Update Index refreshes entries and page numbers after edits. Delete Index removes the whole ToC block (headings stay). Never type inside the ToC — updates wipe manual typing.</div>
<div class="qa"><strong>4-mark (practice): Describe the full Track Changes review cycle.</strong><br>(1) Prepare: save a review copy. (2) Record: Edit → Track Changes → Record ON, then share. (3) Review: edits appear coloured with author names; add suggestions via Insert → Comment (Ctrl+Alt+C). (4) Accept/Reject: reopen → Edit → Track Changes → Manage → accept/reject each change. (5) Finalise: switch Record OFF, delete resolved comments, save final. Use Edit → Track Changes → Compare Document to see differences between two drafts. Remember: Manage (not “Review tab” — that is MS Word language).</div>""",
"u2-ch4": """<h3>➕ Extra exam Q&amp;A bank</h3>
<div class="qa"><strong>1-mark: What must you do before applying Subtotals?</strong><br>Sort the data by the grouping column first — unsorted data gives garbage groups.</div>
<div class="qa"><strong>1-mark: Scenario vs Goal Seek direction?</strong><br>Scenario: forward (inputs → outputs). Goal Seek: backward (output → input).</div>
<div class="qa"><strong>1-mark: How many variable cells does Goal Seek change? What must the formula cell contain?</strong><br>Exactly one variable cell; the formula cell must contain a formula.</div>
<div class="qa"><strong>2-mark: When would you use Solver instead of Goal Seek?</strong><br>When there are multiple variable cells plus constraints — e.g. maximise profit by adjusting price AND quantity with budget ≤ ₹50,000 and stock ≤ 500.</div>
<div class="qa"><strong>4-mark (practice): Explain Goal Seek with an example and steps.</strong><br>Goal Seek finds the input needed for a desired output (works backwards, one variable). Example: Total = Term1 (85) + Term2 (?) and you want 180 — Goal Seek finds Term2 = 95. Steps: (1) build the formula cell (C1 =A1+B1). (2) Tools → Goal Seek → Formula cell C1, Target value 180, Variable cell B1 → OK (memorise F-T-V). (3) Accept the result. Contrast: Scenarios save input sets to compare outputs (forward, many inputs); Consolidate merges dispersed ranges; Subtotals summarise grouped data (sort first!).</div>""",
"u2-ch5": """<h3>➕ Extra exam Q&amp;A bank</h3>
<div class="qa"><strong>1-mark: Record-macro path and storage location?</strong><br>Tools → Macros → Record Macro; stored under My Macros (Standard library).</div>
<div class="qa"><strong>1-mark: Macro security path? Which level asks before running?</strong><br>Tools → Options → Security → Macro Security; Medium asks before running unsigned macros.</div>
<div class="qa"><strong>1-mark: Sub vs Function in Basic?</strong><br>Sub runs actions; Function returns a value so it can be used as a formula (e.g. =BONUS(B2)).</div>
<div class="qa"><strong>2-mark: Two benefits of macros + one precaution.</strong><br>Benefits: speed (one click replays many steps) and consistency (zero repeated errors). Precaution: never enable macros from unknown files — virus risk; keep security at Medium/High.</div>
<div class="qa"><strong>4-mark (practice): Recording steps + macro as a function with example.</strong><br>Record: Tools → Macros → Record Macro → perform planned actions (bold headers, fill, sort) → Stop Recording → save under My Macros as FormatDaily. Run: Tools → Macros → Run Macro (or assign to a button/shortcut). Macro as Function: written with Function in LibreOffice Basic, used like built-in formulas — e.g. Function BONUS(salary) = salary*0.10, called as =BONUS(B2). Passing arguments as values (DISCOUNT(1000, 0.1)) makes one macro handle many cases; order matters.</div>""",
"u2-ch6": """<h3>➕ Extra exam Q&amp;A bank</h3>
<div class="qa"><strong>1-mark: Write a reference to cell B5 of sheet “Branch A”.</strong><br>='Branch A'.B5 (quote names with spaces).</div>
<div class="qa"><strong>1-mark: In an external reference, what does # separate?</strong><br>The file path from the sheet: 'file…'#$Sheet1.A1.</div>
<div class="qa"><strong>1-mark: How do you follow vs edit a hyperlink in Calc?</strong><br>Ctrl+Click follows; right-click → Edit/Remove Hyperlink edits (left-click alone follows it!).</div>
<div class="qa"><strong>2-mark: Relative vs absolute hyperlink.</strong><br>Relative stores a short portable path from the current file (../data/sales.ods) — moves safely with the folder. Absolute stores the full URL/path (https://… or C:\\…) — breaks if the file moves.</div>
<div class="qa"><strong>4-mark (practice): Explain sheet references, external references and hyperlinks.</strong><br>Same file, by mouse: type = → click the sheet tab → click the cell → Enter (Calc writes ='Sheet2'.A1); by keyboard: type SheetName.Cell manually. Other file: open both → = → switch window → click source cell → Enter (full path with # inserted); manage via Edit → Links to External Files. Hyperlinks (Ctrl+K): jump to cell/sheet/file/webpage/email — Internet, Document, Mail tabs; blue + underlined. Live imports differ: Sheet → Link to External Data refreshes tables from URL/file; View → Data Sources (F4) drags registered Base data into Calc.</div>""",
"u2-ch7": """<h3>➕ Extra exam Q&amp;A bank</h3>
<div class="qa"><strong>1-mark: Share path? How do you know a file is shared?</strong><br>Tools → Share Spreadsheet; the title bar shows (shared).</div>
<div class="qa"><strong>1-mark: When does the Resolve Conflicts dialog appear?</strong><br>On save, when two users changed the same cell — pick Mine/Theirs per conflict.</div>
<div class="qa"><strong>1-mark: Comment vs recorded change?</strong><br>Comment discusses without altering the value; a recorded change alters the value with a coloured border + author note.</div>
<div class="qa"><strong>2-mark: Merge vs Compare in Calc.</strong><br>Merge combines many edited copies into one master (Edit → Track Changes → Merge). Compare diffs two versions and inserts differences as tracked changes. (Writer has Compare; Calc has Merge + Compare + Share.)</div>
<div class="qa"><strong>4-mark (practice): Describe the full Calc collaboration cycle.</strong><br>(1) Save in a shared location → Tools → Share Spreadsheet → tick multi-user → OK. (2) Users open, edit and save often; clashes raise Resolve Conflicts. (3) Switch Edit → Track Changes → Record ON so edits get coloured borders + author notes. (4) Discuss via Insert → Comment (Ctrl+Alt+C) without touching values. (5) Leader opens Edit → Track Changes → Manage, filters by author/date and Accepts/Rejects each change. (6) Combine copies via Merge Document. Shared mode limits (no images/charts/merged cells) prove you know the details.</div>""",
"u3-ch8": """<h3>➕ Extra exam Q&amp;A bank</h3>
<div class="qa"><strong>1-mark: Data vs Information in one line each.</strong><br>Data = raw unorganised facts. Information = processed, meaningful, decision-useful.</div>
<div class="qa"><strong>1-mark: Table with 4 columns and 50 rows — degree? cardinality?</strong><br>Degree = 4 (columns); cardinality = 50 (rows).</div>
<div class="qa"><strong>1-mark: Candidate vs alternate vs composite key?</strong><br>Candidate = could be PK; alternate = candidate not chosen; composite = PK of 2+ columns together.</div>
<div class="qa"><strong>2-mark: Two advantages of DBMS over flat files.</strong><br>(1) No redundancy + consistency — store once (teacher name), one update reflects everywhere. (2) Integrity + security — rules reject bad data (marks &gt; 100 blocked) and passwords control who edits.</div>
<div class="qa"><strong>4-mark (practice): Advantages of DBMS (any six, one line each).</strong><br>(1) No redundancy — store once, link everywhere. (2) Consistency — one update reflects everywhere. (3) Integrity — rules block duplicates/bad values. (4) Security — passwords + user rights. (5) Sharing + concurrency — many users together safely. (6) Quick search — queries answer in seconds. Bonus: backup/recovery and standards. CBSE uses the Relational model (tables + keys); Hierarchical is a rigid tree, Network is a complex graph.</div>""",
"u3-ch9": """<h3>➕ Extra exam Q&amp;A bank</h3>
<div class="qa"><strong>1-mark: Base file extension? What does it contain?</strong><br>.odb — tables + queries + forms + reports together.</div>
<div class="qa"><strong>1-mark: Which type for Name? For Marks with decimals? For Passed?</strong><br>Name = TEXT/VARCHAR; Marks = DECIMAL; Passed = BOOLEAN.</div>
<div class="qa"><strong>1-mark: AutoValue = Yes does what?</strong><br>Auto-numbers IDs (1, 2, 3…) so every row gets a unique key.</div>
<div class="qa"><strong>2-mark: Wizard vs Design View for creating tables.</strong><br>Wizard: guided, fast, standard fields — best for beginners. Design View: manual field name + type + properties (Length, Default, Required, AutoValue) + primary key — full control.</div>
<div class="qa"><strong>4-mark (practice): Create a CLASS table in Design View and explain the primary key.</strong><br>Tables → Create Table in Design View → rows: ClassID INTEGER (AutoValue Yes, Required Yes), ClassName VARCHAR(30), Teacher VARCHAR(40) → right-click ClassID → Primary Key (🔑) → Ctrl+S → name CLASS. Primary key rules: one per table, unique, NOT NULL, stable (RollNo, not Name), short numbers best. Datasheet ops: double-click table → type rows (auto-save), navigate with First/Prev/Next/Last bar, sort via column header, delete via row header (permanent!). Composite key: Ctrl+click 2 fields → Primary Key.</div>""",
"u3-ch10": """<h3>➕ Extra exam Q&amp;A bank</h3>
<div class="qa"><strong>1-mark: CLASS–STUDENTS is which type? Where does the FK sit?</strong><br>One-to-Many; the FK sits in the MANY-side table (STUDENT.ClassID).</div>
<div class="qa"><strong>1-mark: PERSON–PASSPORT is which type?</strong><br>One-to-One (one row ↔ exactly one row).</div>
<div class="qa"><strong>1-mark: What is an orphan record?</strong><br>An FK value pointing to a non-existent PK — referential integrity prevents these.</div>
<div class="qa"><strong>2-mark: What is referential integrity? Give one blocked action.</strong><br>Rule that every FK must match an existing PK (or NULL). It blocks entering a student with ClassID “ZZZ” and deleting a class that still has students (unless cascade).</div>
<div class="qa"><strong>4-mark (practice): Relationship types + creation steps.</strong><br>1:1 — one ↔ one (PERSON–PASSPORT). 1:N — one ↔ many, most common (CLASS–STUDENTS, FK on many side). M:N — many ↔ many (STUDENTS–SUBJECTS) built physically as two 1:N via a junction table ENROLMENT(StudentID, SubjectID) whose composite PK = both FKs. Create: close tables → Tools → Relationships → add tables → drag CLASS.ClassID onto STUDENT.ClassID → tick Enforce referential integrity (+ Update/Delete cascade only if needed) → save. Line 1—∞ appears. Deleting a table with enforced relations is blocked — remove the relation first.</div>""",
"u3-ch11": """<h3>➕ Extra exam Q&amp;A bank</h3>
<div class="qa"><strong>1-mark: Run query shortcut? Hide a column how?</strong><br>F5 runs; untick Visible to use-but-hide a column.</div>
<div class="qa"><strong>1-mark: LIKE 'A*' finds what? LIKE 'An?'?</strong><br>'A*' = names starting with A (many chars). 'An?' = 3-letter names starting An (one char).</div>
<div class="qa"><strong>1-mark: AND vs OR in the criterion rows?</strong><br>AND = same criterion row; OR = next (different) row.</div>
<div class="qa"><strong>2-mark: Wizard vs Design View query.</strong><br>Wizard: guided, simple AND conditions only — no wildcards/calculations. Design View: full grid power — Field/Alias/Table/Sort/Visible/Criterion + Function row (SUM/AVG/COUNT) + SQL view.</div>
<div class="qa"><strong>4-mark (practice): Build a topper query in Design View.</strong><br>Queries → Create Query in Design View → add STUDENT → drag Name, ClassID, Marks to the grid (FATSVC order). Sort: Desc on Marks. Visible: untick ClassID (filter, don't show). Criterion: Marks &gt;80 AND ClassID='X-A' (same row = AND). Wildcard variant: Name LIKE 'A*'. Calculation: Function row → AVG(Marks), grouped by ClassID (SELECT ClassID, AVG(Marks) … GROUP BY ClassID). Save → F5 to run → tables unchanged, view is live. Toggle View → SQL View to see the statement.</div>""",
"u3-ch12": """<h3>➕ Extra exam Q&amp;A bank</h3>
<div class="qa"><strong>1-mark: Label vs Text Box?</strong><br>Label shows fixed text (not stored); Text Box types/stores field data. (#1 viva trap!)</div>
<div class="qa"><strong>1-mark: Radio button vs check box?</strong><br>Radio = one-of-many choice (gender); check box = yes/no tick (passed?).</div>
<div class="qa"><strong>1-mark: Name three things you insert to polish a report.</strong><br>Title/Heading, Date and Time, Page Number (+ logo image).</div>
<div class="qa"><strong>2-mark: Form vs Report (2 points).</strong><br>(1) Form = screen for entry/edit (read-write, one record focus); Report = print for reading (read-only, many records + groups + totals). (2) Form uses Text Box/Button/Combo controls; Report uses Titles/Headings/Date/Page numbers.</div>
<div class="qa"><strong>4-mark (practice): Form controls + report wizard steps.</strong><br>Form: Forms → Use Wizard → table/query → fields → subform for 1:N (CLASS + STUDENTS) → layout (columnar) → mode → style → Finish. Controls: Label (fixed text), Text Box (input), Button (save/next), Check Box (yes/no), Radio (one-of-many), List/Combo (dropdown), Date/Formatted (validated). Daily ops: ➕ new → type → save → find (binoculars). Report: Reports → Wizard → fields → GROUP by Class → sort Marks desc → tabular layout → title → Finish → Edit: Insert Title + Date & Time → Print Preview/PDF.</div>""",
"u4-ch13": """<h3>➕ Extra exam Q&amp;A bank</h3>
<div class="qa"><strong>1-mark: Health vs Safety vs Security (one line each)?</strong><br>Health = well-being (no illness/stress). Safety = freedom from accidents. Security = protection of people/data/property.</div>
<div class="qa"><strong>1-mark: Wet floor? Loose cable across path?</strong><br>Wet floor = slip hazard; loose cable = trip hazard.</div>
<div class="qa"><strong>1-mark: Correct lifting posture?</strong><br>Bend KNEES (not back), straight back, firm grip, load close, no twisting — trolley/help for heavy loads.</div>
<div class="qa"><strong>2-mark: Two reasons every organisation needs an HSS policy.</strong><br>(1) Legal + fewer accidents — complies with law and cuts injury leave. (2) Higher productivity + lower costs — safe workers focus better; fewer medical/damage bills (also: motivation, good image).</div>
<div class="qa"><strong>4-mark (practice): Hazard types with two examples each (any five).</strong><br>Physical: loud noise, poor lighting. Fall: ladder without grip, stair with no railing. Slip/Trip: wet floor, loose wires. Electrical: overloaded socket, cut wire. Fire: paper near heater, blocked exit. Health: dust → asthma, long sitting → back pain. Chemical: toner, cleaning acid. Controls follow the hierarchy: Eliminate → Substitute → Engineering (guards) → Administrative (training/signs) → PPE (gloves/masks) as the last shield.</div>""",
"u4-ch14": """<h3>➕ Extra exam Q&amp;A bank</h3>
<div class="qa"><strong>1-mark: Monitor distance? Knees angle? Feet?</strong><br>50–70 cm away, top at/below eye level; knees ~90°; feet flat on floor/footrest.</div>
<div class="qa"><strong>1-mark: Expand 20-20-20.</strong><br>Every 20 minutes → look 20 feet away → for 20 seconds (prevents eye strain).</div>
<div class="qa"><strong>1-mark: Green / blue / red bins?</strong><br>Green = wet waste, blue = dry waste, red = e-waste/biomedical.</div>
<div class="qa"><strong>2-mark: Two ergonomic sitting tips.</strong><br>(1) Straight back with lumbar support, feet flat, knees ~90°. (2) Monitor at eye level 50–70 cm, keyboard + mouse at elbow height, wrists straight.</div>
<div class="qa"><strong>4-mark (practice): Riya uses a computer 8 hours daily and has eye + back pain. Suggest four measures.</strong><br>(1) Ergonomics: back-supported chair, feet flat; monitor eye-level 50–70 cm; keyboard at elbow height; document holder to avoid neck twist. (2) Eyes: 20-20-20 + blink often; anti-glare, bigger fonts, clean screen, brightness matching room. (3) Breaks: micro-break every 30–60 min — stand, stretch, walk, drink water. (4) Habits: no eating over keyboard, laptop on stand + external KB/mouse, eye test + correct specs, fixed sleep (no screens 1 hr before bed).</div>""",
"u4-ch15": """<h3>➕ Extra exam Q&amp;A bank</h3>
<div class="qa"><strong>1-mark: Fire triangle? PASS?</strong><br>Fuel + Heat + Oxygen. PASS = Pull pin, Aim at base, Squeeze, Sweep.</div>
<div class="qa"><strong>1-mark: Lift or stairs in a fire? Why?</strong><br>Stairs — lifts can trap you in a power cut and shafts spread smoke.</div>
<div class="qa"><strong>1-mark: Clothes on fire — what do you do?</strong><br>STOP-DROP-ROLL, smother with a blanket, cool burns under water 10 min.</div>
<div class="qa"><strong>2-mark: Three steps of handling an accident.</strong><br>(1) Attend the injured — reassure, stop bleeding, don't move spinal injuries. (2) Inform the supervisor + call first-aider/ambulance with exact location. (3) Assist — fetch kit, guide ambulance, note witnesses, file the incident report.</div>
<div class="qa"><strong>4-mark (practice): First aid for an electrical emergency (order matters!).</strong><br>(1) DON'T touch the victim with bare hands. (2) Switch OFF power (MCB/main) FIRST. (3) Separate with a DRY non-conductor (wooden stick) while standing on dry insulation. (4) Call supervisor + 102/108. (5) If trained: check breathing/pulse → CPR/recovery position; cover burns with clean DRY cloth (no ointment/ice); keep victim warm + still. (6) Shift to hospital even if they “feel fine” (delayed heart effects). Never throw water on electrical fire — use CO₂/dry powder. Know your MAIN switch locations!</div>""",
}

# Interactive quiz: (question, [4 options], correct answer)
QUIZ = [
("Which Writer feature supplies structure for an automatic ToC?", ["Bold text", "Heading styles", "Font colour", "Page numbers"], "Heading styles"),
("Which Calc tool finds the input needed for a desired formula result?", ["Sort", "Scenarios", "Goal Seek", "Consolidate"], "Goal Seek"),
("Which key uniquely identifies each Base record and cannot be NULL?", ["Foreign key", "Primary key", "Caption", "Index"], "Primary key"),
("What is the eye-break rule for computer users?", ["50–70", "20-20-20", "90-90-90", "101/102/108"], "20-20-20"),
("Which shortcut opens the Styles window in Writer?", ["F4", "F11", "Ctrl+K", "Ctrl+S"], "F11"),
("How many variable cells can Goal Seek change?", ["Only one", "Two", "Up to ten", "Unlimited"], "Only one"),
("Degree and cardinality of a table mean…", ["Rows / Columns", "Columns / Rows", "Keys / Queries", "Forms / Reports"], "Columns / Rows"),
("CLASS–STUDENTS is which relationship type?", ["One-to-One", "One-to-Many", "Many-to-Many", "No relation"], "One-to-Many"),
("In a fire evacuation you should use…", ["The lift (fastest)", "Nearest safe stairs", "Locked exits", "The balcony"], "Nearest safe stairs"),
("First step in an electrical rescue?", ["Touch the victim", "Throw water", "Switch OFF power", "Call a friend"], "Switch OFF power"),
("Relative hyperlinks are better when…", ["Files never move", "Folders move together", "Using the internet", "Printing"], "Folders move together"),
("SMART goals: T stands for…", ["Total", "Tough", "Time-bound", "Tested"], "Time-bound"),
]
