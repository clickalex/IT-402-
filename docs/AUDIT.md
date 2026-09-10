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
