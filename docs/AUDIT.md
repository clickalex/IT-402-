# IT-402 Content & Site Audit — September 2026

Scope: full static study hub for CBSE Class 10 IT-402 (2026–27), LibreOffice-only.
Goal of this pass: **more detail everywhere + one page per chapter (20 pages).**

## 1. What the audit found (before)

| # | Finding | Severity |
|---|---|---|
| 1 | Theory chapters were ~200–400 words each with generic filler Q&A repeated verbatim across chapters (“What is one benefit? It improves consistency…”) | High |
| 2 | Progress counter said “15 chapters” but the syllabus has 20 examinable units (Part A ×5 + Ch 1–15) | Medium |
| 3 | `question-bank.html` had only 4 MCQs / 4 short / ~2 long answers — far below a usable bank | High |
| 4 | `practical.html` listed 15 tasks as one-liners; viva answers were 2–4 words | Medium |
| 5 | `revision.html` / `syllabus.html` were minimal (~250 words each), no paper pattern detail | Medium |
| 6 | `book-ch1-5.html` duplicated Chapters 1–5 with no cross-links (two sources of truth) | Low |
| 7 | Search index covered only 11 pages + a few anchors; links would break from subfolders | Low |
| 8 | `content/*.md` outlines were ~80-word stubs; deep notes existed only inside the ZIP | Low |

Total site content before: **~12,400 words** across 11 HTML pages.

## 2. What changed (after)

- **20 chapter pages** in `chapters/` (Part A U1–U5 + Ch 1–15), each ~800–1,400
  words with: marks lens, visual summary diagram (CSS/SVG), deep concepts with
  comparison tables, exact LibreOffice menu paths + `<kbd>` shortcuts, memory
  tricks, mistakes to avoid, exam Q&A (5+ one-mark, 3+ two-mark, 1–2 four-mark
  with models), hands-on task, prev/next links, and a completion checkbox.
- **Unit hubs** (`part-a.html`, `unit1-4`) rebuilt as navigators: chapter cards,
  quick-path tables, interactive final checklists, prev/next unit flow.
- **`question-bank.html`**: 12-question interactive MCQ quiz with instant feedback,
  60 unit-wise objectives with answers, 13 short + 7 long model answers, full
  50-mark sample paper with answer key, 2-hour timer.
- **`practical.html`**: full W1–W6 / C1–C6 / D1–D6 practicals with steps,
  file-presentation tips, project structure, 30 viva Qs, 1-week prep plan.
- **`syllabus.html`**: complete marks table (2/3/1/3/1 + 8/10/12/10), Section A/B
  pattern, school-based 50 split, golden rules, study route.
- **`revision.html`**: expanded cheat sheet — all paths, shortcuts, DBMS keys,
  numbers (50–70, 20-20-20, PASS, 101/102/108), answer frames, checklists.
- **`index.html`**: 20-chapter dashboard with per-unit progress bars + chapter links.
- **Search/theme/progress JS**: 31-entry index (works from root and `chapters/`
  via relative prefix), 20-chapter progress, per-unit bars, persistent checklists,
  `/` keyboard shortcut, mobile sidebar auto-close.
- **CSS**: chapter nav groups, SVG figure theme, answer/checklist/banner styles,
  themed chapter rails, print-friendly (existing print rules kept).
- **Sources preserved**: ZIP notes imported to `content/source/`; generators in
  `tools/` (`build.py`, `hubs1.py`, `hubs2.py`) reproduce all pages.
- **Legacy book** kept for printing, clearly badged with links to detailed chapters.

Total site content after: **~31,600 words** across 31 HTML pages (2.5×).

## 3. Verification (this pass)

- [x] Internal link audit: **1,018 links, 0 broken** (script in history)
- [x] Same-page anchor audit: **0 dangling anchors**
- [x] `node --check assets/js/app.js`: **valid**
- [x] No external dependencies (offline-friendly); no MS Office paths in procedures
- [x] Every chapter page has: diagram, Q&A bank, practical task, prev/next, checkbox
- [x] Print stylesheet hides nav/chrome; revision page prints as cheat sheet

## 4. Known limitations / next steps

- Diagrams are lightweight CSS/SVG by design (offline, no image assets).
- Quiz distractors are original simplifications — teachers should sanity-check
  wording against the latest CBSE sample paper.
- If CBSE issues a curriculum circular, update `content/source/` + `tools/extras.py`
  and regenerate; then refresh `syllabus.html` weightage.

## 5. Pass 2 — More bank, more practice, illustrations (September 2026)

- **Question bank:** 12 → **30 interactive MCQs** (5 unit quizzes with per-quiz
  scoring), 60 → **100 objectives**, +15 rapid-fire True/False, short 13 → **25**,
  long 7 → **14** model answers, + **second full 50-mark sample paper** with key.
- **Practical:** 15 → **25 tasks** (W7–W8, C7–C9, D7–D9, M1 mixed project),
  + **90-minute mock practical exam** with marking scheme, + **troubleshooting
  clinic** (12 fixes), viva 30 → **50 Qs**.
- **Images:** 10 original flat illustrations in `assets/img/` (~836 KB total,
  offline, lazy-loaded, alt text) — hero, 5 unit/hub banners, ergonomics, fire
  safety, quiz and lab art — embedded on 28 of 31 pages.
- Re-verified: **1,052 links, 0 broken**; anchors clean; JS valid; ~35,500 words.

## §6 Pass 3 — official PYQ practice page (2026-09-10)
- Added `pyq.html`: library of 4 official CBSE SQPs (2022-23→2025-26) with SQP+MS PDF links,
  158 chapter-wise PYQs (101 one-markers + 57 answered subjective, MS-gist/model labeled),
  trend tables, 4-marker analysis, 4-week plan, self-marking guide, 2-hour timer, print-ready.
- Sources: content/pyq/{papers,chapterwise,trends}.md → tools/pyq.py generator (mirrors build.py QA pipeline).
- Wiring: sidebar 📝 link (tpl.py), index jump card (hubs1.py), search index (app.js),
  per-chapter "Practise board PYQs" deep links (20 canonical anchors C-U1..C-Ch15, verified, 0 dangling).
- Suitability flags: 2022-23/2023-24 Unit 4 (Web Applications) + mail merge marked ⛔ skip (old syllabus).
- Note: sandbox has no outbound net, so official PDFs are linked (not vendored); bank works offline.
- Verify: 32 pages, 1152 links 0 problems, ~42.4k words; node --check app.js OK.

## Historical SQP evidence extension — 2026-09-10
- Read four additional official Class X SQPs: 2019–20, 2020–21, 2021–22 T1/T2 (all web-reader chunks).
- Added historical.md: question-topic evidence and parsing/syllabus caveats, rendered on pyq.html.
- Coverage now eight documents / seven sessions. Comparable broad-topic window: six sessions; 2019–20 kept separate. Terms counted as one session.
- Removed misleading “Asked every single year” heading. Explicitly distinguish SQP recurrence from main-board frequency/predictions; solved bank unchanged.
- Original PDF downloads attempted over HTTPS, HTTP and www host; failed (TLS/empty response). No PDF binaries saved, no claim of completed downloads. Historical MS not verified. 2015–18 not covered.
- Verified generated local links, fragment targets, unique IDs, 101 QA cards + 57 answer blocks; node syntax check passed.

## Trend-informed practice update and site audit — 2026-09-10

### Changes
- Expanded interactive question-bank quizzes from 30 to 50 MCQs: 10 in each of five unit quizzes. New items target recurring concepts and case-based feature selection; current safety remains covered.
- Added 20 original written prompts (one per chapter) with suggested 2M/4M marking points. The same source renders the central bank and all 20 chapter pages to avoid answer drift.
- Clearly labelled authored practice as original, not official PYQ text, official marking schemes or predictions. No legacy presentation/mail-merge/networking questions added.
- Updated revision guidance, homepage historical-paper count and assessment summary. Corrected chapter links from “board PYQs” to “official SQP questions”. The official solved bank remains 158 items.
- Added `tools/trend_practice.py` as shared practice source; MCQ heading counts now computed from quiz data rather than hardcoded.

### Audit performed
- Rebuilt with tools/build.py, hubs1.py, hubs2.py and pyq.py successfully.
- `python3 tests/audit_site.py`: PASS — 32 generated pages, 1,367 local references, zero missing files/fragments or duplicate IDs; all 20 chapters contain practice.
- Validated 50 rendered MCQ answer keys against source, four distinct options and exactly one correct option per question; five quizzes of ten questions.
- Validated 20 central written prompts and unchanged 101 official QA cards + 57 answer blocks.
- `node --check assets/js/app.js`, Python compileall and `git diff --check`: PASS.
- Static/content audit only: no browser interaction or visual-layout test performed. External PDF availability is not asserted; original binary downloads remain blocked as documented above. Historical topic evidence is SQP-based, not main-board exam frequency.

Repeatable audit: `python3 tests/audit_site.py` from repository root after rebuilding.

## Chapter-wise practice selection — 2026-09-10
- Added a labelled 20-chapter selector plus All chapters on the question bank. Filters 50 MCQs and 20 written trend-practice prompts; full papers/general bank remain visibly labelled as unfiltered.
- Explicit chapter mapping covers every MCQ (including the linking question inside the mixed safety quiz). Every chapter has at least one MCQ and its written prompt.
- Hides empty quiz groups, updates visible-question score/counts, retains answers across chapter changes, and locks answered radio groups to prevent answer/score disagreement.
- Supports shareable `?chapter=<short-id>` URLs, chapter-note/SQP links and direct practice links from all chapter pages. Invalid chapter values fall back to All chapters.
- Static audit PASS: 32 pages, 1,387 local references, zero errors; 70 tagged questions, 21 selector options, valid chapter mappings. JavaScript syntax and diff whitespace checks PASS. Browser interaction/visual testing not performed.

## Part A unit-wise entry point — 2026-09-10
- Updated the Employability Skills hub with an accessible five-unit GET-form selector opening the corresponding question-bank filter. Selection submission does not require JavaScript; filtering uses the existing bank script.
- Added MCQ/written-practice and official SQP deep links to all five cards; updated topic guidance to match the historical review without predicting marks.
- Removed unexplained unit-level numbers from this hub to avoid implying a guaranteed marks split; retained the 10-mark Part A pattern and all five study/checklist sections.
- Audit PASS: 32 pages, 1,398 local references, no broken local targets; verified all five selector options and practice/SQP links. JS syntax and diff checks pass. No browser visual test performed.

## Consistent unit hubs and Part A follow-up — 2026-09-10

### Scope and findings
- Audited all five unit hubs and their routes into the existing chapter-filtered bank. Writer, Calc, DBMS and Safety had no selectors or card-level practice/SQP links, unlike Part A.
- Baseline static audit: **37 HTML pages, 1,619 local references, zero errors**. Earlier entries reporting 32 pages predate the five standalone root-level Part A pages.
- Part A's hub already disclaimed fixed individual marks, but the homepage, syllabus table and canonical deep-note source still presented 2/3/1/3/1 as fixed and claimed guaranteed questions.
- Found “Hot Qs” / easy-marks promises, a blanket Medium macro-security reminder, an oversimplified `.odb` description and unsafe shorthand in the Safety hub.

### Changes
- Added a labelled chapter/unit GET selector to every hub (5 + 3 + 4 + 5 + 3 options), direct authored MCQ/written practice and official SQP links on all 20 chapter cards, and per-hub progress using the existing browser storage.
- Centralised selectors, progress and practice links in `tools/hub_practice.py`; chapter membership comes from `tpl.CHAPTERS`, official anchors from `quiz.PYQ_ANCHOR`. Build-time slot checks prevent silently missing navigation.
- Added consistent study/practise/review guidance, original-vs-official question labels, unfiltered-bank notice and explicit no-JavaScript limitations. Selectors have labels, help text, theme-aware styling and narrow-screen wrapping.
- Added unit-specific practice priorities without claiming exam predictions; Safety explicitly excludes historical Web Applications material.
- Part A: replaced opaque mnemonic fragments in the hub table with recall/application guidance and added a two-mark answer checklist. Removed unsupported fixed unit allocations/guaranteed-frequency wording in canonical notes, homepage and syllabus. Updated ICT password/MFA and HTTPS guidance.
- Corrected Calc macro-security advice and Share Spreadsheet naming; clarified Base external storage and relationship rules. Safety now prioritises safe evacuation, trained help, no improvised electrical rescue and India's integrated emergency number 112.
- Corrected the homepage's stale 30-question quiz count to 50. Existing bank content remains **50 MCQs + 20 written prompts**, with the official solved bank unchanged at 101 objective + 57 subjective items.

### Verification
- Rebuilt `tools/build.py`, `tools/hubs1.py`, `tools/hubs2.py` successfully.
- `python3 tests/audit_site.py`: **37 pages, 1,653 local references, zero errors**. Audit now includes form actions and chapter query values, all five selectors' exact membership, labels/help/submit controls, progress totals, all 20 card link sets, no-JS notices and generated-body consistency.
- `node --check assets/js/app.js`, Python compileall and `git diff --check`: pass.
- Browser interaction/visual testing **not completed**: Playwright installed in an external virtual environment, but Chromium download failed with TLS connection resets. No runtime dependency was added to the site.

### Limits / follow-up
- This is a hub/navigation and targeted content audit, not a fresh verification of the complete 2026–27 official curriculum, every LibreOffice version or external PDF availability.
- The ZIP, legacy printable book, standalone `part-a-ch*.html` pages and other imported source summaries remain historical/parallel content and were not rewritten in this pass. Canonical study links point to `chapters/`; reconcile or retire legacy copies in a separate content migration.
- The Safety hub's revised precautions should also be propagated through a dedicated safety review of older deep notes, revision material and question answers. No claim of a complete medical/safety audit is made here.

## Separate chapter question pages and expanded bank — 2026-09-10

### Delivery
- Replaced the primary `question-bank.html` experience with a labelled chapter
  picker and 20 chapter cards. Each choice opens an actual `practice/<id>.html`
  page containing only that chapter's questions, not a filter over one long page.
- Added **360 new authored questions**: 200 MCQs, 40 short, 40 long, 40 application
  and 40 competitive-style challenges. Included the earlier 50 chapter-mapped
  MCQs and 20 written prompts, yielding **430 questions** on the new pages:
  **250 MCQs + 40 short + 40 long + 60 application + 40 competitive**.
- Every chapter has all five question types and at least ten newly authored MCQs.
  New MCQs include explanations; written answers include model reasoning or
  suggested marking points. Exact new prompt duplicates are rejected at build time.
- All 430 answers are closed native `<details>` controls, styled as Show answer /
  Hide answer. Selecting an MCQ option does not reveal its answer. Added keyboard
  support through native controls and a JavaScript-enhanced Hide all answers button.
  Choices on these learning pages are explicitly not scored or saved.
- Added category jump links, a chapter picker, notes/unit/SQP links and previous /
  next question-page navigation. Direct links appear on all five hubs and at both
  the top and bottom of every canonical study chapter.
- Preserved the former general bank, quizzes and two sample papers in
  `mixed-practice.html`, linked from the new directory. Existing
  `question-bank.html?chapter=<id>` URLs route to the corresponding chapter page
  with JavaScript; invalid values remain in the directory with guidance.
- Static links and answer controls work without JavaScript or a server. The
  selector is an enhancement: no-JS learners use chapter cards/direct links.
- Fixed shared sidebar and search prefixes for the new `practice/` folder.
  Added responsive, dark-theme, focus and reduced-motion styling.
- Content lives in `content/practice/{mcqs,written}.txt`, documented by its README;
  `tools/practice.py` renders the pages and is invoked by `tools/build.py`.

### Verification
- Rebuilt build.py, hubs1.py, hubs2.py and pyq.py. Existing official SQP bank remains
  101 objective + 57 subjective items; new competitive exercises are not called PYQs.
- Static audit: **58 pages, 3,027 local references, zero missing files/fragments or
  duplicate IDs**. Added checks for standalone page membership, question counts,
  answer-key validity, four distinct MCQ options, radio grouping, closed answers,
  selector destinations, direct study links and deterministic generated output.
- Real Chromium / Playwright suite (`tests/browser_practice.py`): **PASS** across
  every chapter route, all five answer types, keyboard open/close, MCQ selection
  without reveal, Hide all, legacy query routes, invalid IDs, five hub selectors,
  nested-folder search, 360px dark-theme overflow and file:// no-JavaScript answers.
- Inspected desktop and mobile screenshots. Screenshots and browser binaries are
  external test artifacts, not shipped with the repository.
- The earlier Playwright CDN download limitation was worked around using a
  Chromium binary from an npm distribution in the sandbox's external cache.
  No browser library or runtime dependency was added to the study website.
- `node --check assets/js/app.js`, Python compileall and `git diff --check`: PASS.

### Content boundaries
- Competitive-style tasks are original reasoning extensions, not a claim of
  alignment to a named competitive examination. Part A long questions are clearly
  labelled extensions rather than the usual board-paper two-mark format.
- The primary chapter pages hide all answers. The preserved mixed-revision resource
  keeps its original quiz feedback and sample-paper conventions; it is not the new
  chapter-learning interface. Official SQP answers remain in their separate library.
- This expansion does not assert fresh verification of every official syllabus,
  historical PDF or older parallel note page. New safety questions emphasise trained
  help, safe isolation and evacuation rather than improvised rescue techniques.

## Exactly 100 questions in every chapter — 2026-09-11

### Confirmed scope and delivery
- User selected **100 total questions per chapter**, with **60 MCQs + 10 short +
  10 long + 10 application + 10 competitive-style**. All 20 chapters now meet
  that exact allocation: **2,000 total (1,200 MCQs + 800 written)**.
- Retained all 430 existing chapter-page questions in their existing category
  order. Added 1,570 assessment items (950 MCQs and 620 written questions).
- Added nine authored scenario packs per chapter in `content/practice/scenarios.txt`.
  Each specifies a topic, definition, case, action, misconception, correction,
  verification evidence and limitation. `tools/practice_expansion.py` renders
  different assessment skills from these packs. Related exercises intentionally
  revisit concepts through different tasks; they are not claimed to be 2,000
  independently sourced official questions.
- Expansion uses deterministic balanced traversal across the chapter's topics.
  It rejects duplicate prompts/options, malformed or incomplete coverage and
  insufficient content rather than silently padding or truncating existing items.
- Existing separate chapter URLs, chapter selectors and hidden answers remain.
  Added an accessible question-type filter (All / MCQ / four written types), live
  visible counts and six MCQ jump links covering 1–10 through 51–60.
- Native section/deep links reveal the relevant filtered section; Hide all answers
  also closes answers in currently hidden sections. No-JS users retain all 100
  questions, jump links and native answer controls. No runtime dependency added.
- Updated directory, homepage, hub guidance, search and content-maintenance docs.

### Verification
- Static audit: **58 pages, 3,147 local references, zero link/fragment/ID errors**.
  Exact per-chapter/category counts and retained original prefixes are checked,
  along with MCQ keys, four distinct options, duplicate prompts, chapter routes,
  sets-of-ten anchors and all 2,000 answers closed in generated markup.
- Playwright/Chromium: **PASS** for all 20 chapters: 100 loaded questions,
  60/10/10/10/10 type filtering, original and newly added answers, keyboard
  toggles, MCQ batch jumps, type jumps, hash links, closing filtered-out answers,
  chapter and hub selectors, legacy query routes, nested search, 360px dark-mode
  overflow and no-JS file:// access to all 100 questions per chapter.
- JavaScript syntax, Python compilation and diff whitespace checks pass.
- Content remains authored self-study practice with suggested marks. Competitive
  variants are reasoning extensions; Part A long questions are not a claim about
  the official board format. This is not a fresh official-syllabus or medical audit.

## 220 questions per chapter + official-syllabus review — 2026-09-11

This section supersedes the earlier 100-item allocation and its explicit limitation
that no fresh official-syllabus audit had been performed. Historical sections above
remain a record of earlier deliveries, not the current bank's counts or scope.

### Confirmed allocation and delivery
- User selected **30 additional questions of EACH written type per chapter**.
  All 20 chapters now contain **60 MCQs + 40 short + 40 long + 40 application +
  40 competitive-style = 220** questions. Overall: **4,400** (1,200 MCQs and
  800 of each written type), adding **2,400 written questions**.
- Added five substantive syllabus-topic packs per chapter, bringing the source to
  280 packs / 14 per chapter. Written expansion uses distinct concept, correction,
  evidence and paired-case formats. These are deliberate practice variants, not
  4,400 independent official exam sources or 4,400 different concepts.
- Retained the in-scope base and original nine-topic MCQ traversal; corrected
  scope-sensitive wording rather than preserving it uncritically. The reviewed
  430-item base remains at the front of its categories. Native closed answers,
  separate chapter URLs, chapter choice, filters and six MCQ batches remain.

### Official references and scope decisions
- Read the current CBSE **2026–27 Class X IT-402 curriculum** (17 pages):
  <https://cbseacademic.nic.in/web_material/Curriculum27/Sec/402-IT-X.pdf>.
- Read the separate **Class X Employability Skills curriculum** (all 3 pages):
  <https://cbseacademic.nic.in/web_material/Curriculum27/Sec/EmployabilitySkills-X.pdf>.
- Mapped the assessed knowledge to the actual theory/practical tables and course
  outcomes, not just existing notes or keyword lists. The detailed workplace-safety
  chapters resolve the stale Web Applications overview label; the separate Class X
  document resolves the ICT-I/II overview inconsistency.
- Replaced standalone break-even and electricity-unit calculations, unsupported
  advanced cyber-protocol trivia, mixed-cell-reference drills, and raw/advanced SQL
  examples with explicitly listed activities. This is a conservative scope choice,
  not a claim that all financial arithmetic or ICT safety is forbidden: the main
  curriculum includes business fundamentals/financial literacy and safe ICT use,
  and the field-visit section includes income, expenditure and profit/loss.
- Kept **Solver**, macro functions/arguments/direct cell access/sorting, query
  numerical calculations and graphical criteria, because they are explicitly in
  the prescribed theory/practical outcomes. Questions do not require advanced
  programming, formal normal forms or complex SQL/NULL aggregation semantics.
- Corrected remaining query distractors and misconceptions to use graphical query
  terminology. Qualified shared questions on image links, bound form controls,
  subtotal grouping and typical monitor positioning. Safety scenarios prioritise
  safe isolation, trained assistance, evacuation and limits of authority.
- **Correction to the earlier audit:** official page 3 DOES publish Part A marks
  **2/3/1/3/1**. Restored this allocation while distinguishing it from a guarantee of
  particular questions appearing in a paper. Green employment has its own direct
  reference to the main curriculum's page 2 learning outcome.

### Review artifacts and drift protection
- `syllabus-audit.html`: readable report, official sources, all chapter counts and
  27 detailed topic references (local reference labels, not official CBSE codes).
- `docs/question-syllabus-audit.csv`: **4,400 rows**, one for every current question,
  with exact prompt, ID, type, topic references, reviewed source keys and a digest
  covering its prompt, answer, options and metadata.
- `content/practice/syllabus-review.json`: **710 source reviews** (200 base MCQs,
  160 written rows, 280 packs, 50 shared MCQs and 20 shared written prompts).
  Each maps source content to cited outcomes with a SHA-256 fingerprint. Paired
  tasks and MCQ distractors inherit references from their actual source packs.
- `content/practice/audit-changes.json`: before/after replacement and clarification
  records. Some entries are successive changes to one source, not distinct questions.
- Builds reject absent, pending or changed source reviews and changed expansion
  templates. The expansion engine itself is fingerprinted. No automatic bulk
  “approve” step is included in the build.
- Review was semantic at source/assessment-template level, with exhaustive
  question-level lineage and generation checks. A checksum or keyword test is NOT
  independent proof of correctness or CBSE approval. A changed question still needs
  substantive curriculum/correctness review before its approval is refreshed.
- Long Part A answers extend the **response format**, not the prescribed content.
  Competitive-style means syllabus-based reasoning, not an external competition.
- The audit boundary is the current **4,400 standalone chapter-bank questions**.
  The legacy mixed resource is clearly labelled; historical SQPs and older parallel
  note banks are preserved separately and are not included in this review claim.

### Final verification
- Static audit: **59 HTML pages, 7,939 local references, zero link/fragment/ID errors**.
- Exact 60/40/40/40/40 counts in all 20 chapters; all 4,400 answer blocks initially
  closed; distinct MCQ options, answer keys, reviewed-base prefixes and prompt
  uniqueness checked. All manifest IDs, fingerprints and inherited topic references
  checked against generated content and the source ledger.
- Negative tests: missing source, changed source, pending review and changed
  expansion-engine fingerprint are all rejected.
- Real Chromium/Playwright: **PASS** for all chapter selectors and routes, all five
  filters, first/last written and MCQ answers, keyboard toggles, batch/type/hash
  navigation, hide-all including filtered-out answers, hub routing, nested search,
  360px/dark overflow and **220 file:// no-JavaScript questions per chapter**.
  Also checked a question-to-syllabus link, the audit's 20-row coverage table,
  successful CSV download and mobile audit-page layout.
- Full regeneration is **byte-identical for all 60 deliverables** (59 HTML pages
  plus the CSV). JavaScript syntax, Python compilation and diff whitespace pass.
- Browser dependencies, screenshots and scratch review scripts remain outside the
  repository; the website still has no runtime framework or network dependency.

## Pre-PR verification — 2026-09-11

Fresh audit requested before PR creation and merge:
- Re-ran `tests/audit_site.py`: 59 pages, 7,939 local references, zero errors;
  exact 220-item chapter allocations and all 4,400 syllabus manifest rows pass.
- Confirmed all 4,400 prompts are globally distinct and every one of the 710
  source-review records is used by the bank (no missing or orphan approvals).
- Re-ran the full Chromium suite: all 20 routes, type filtering, hidden answers,
  keyboard controls, syllabus links/download, mobile/dark and offline/no-JS pass.
- Full rebuild remains byte-identical across 60 deliverables. JavaScript syntax,
  Python compilation and whitespace checks pass.
- The final staged-file check caught CRLF line endings in the newly added CSV.
  Changed the CSV writer to explicit LF and added a regression assertion; staged
  whitespace checks now pass. No unresolved blocking findings remain.
- Syllabus review remains source/template-based with exhaustive question lineage;
  preserved legacy archives are outside its scope.
