# IT-402 Study Hub

Static, offline-friendly CBSE Class 10 Information Technology (402), 2026–27
study website for the Domestic Data Entry Operator job role. Plain HTML, CSS and
vanilla JavaScript with LibreOffice Writer, Calc and Base procedures.

**20 chapters, one detailed page each** — every chapter has a marks lens, visual
summary, concepts with comparison tables, exact menu paths, memory tricks,
mistakes to avoid, an exam Q&A bank (one/two/four-mark) and a hands-on task.

## Folder structure

```text
.
├── index.html, syllabus.html, part-a.html      # hubs
├── unit1-writer.html … unit4-safety.html       # unit hubs (link to chapters)
├── chapters/*.html                             # 20 detailed chapter pages
├── question-bank.html                         # chapter question directory
├── practice/*.html                            # 20 standalone question pages
├── mixed-practice.html, practical.html         # mixed quizzes + papers, lab + viva
├── revision.html, book-ch1-5.html              # cheat sheet, legacy printable book
├── assets/css/styles.css                       # shared responsive + print styling
├── assets/js/app.js                            # theme, search, progress, quiz, timer
├── content/*.md                                # editable curriculum outlines
├── content/source/*.md                         # imported deep-note sources
├── content/practice/*.txt                      # editable chapter question sources
├── tools/*.py                                  # static site generators
└── docs/AUDIT.md, docs/PROJECT.md              # audit report, project structure
```

## Run locally

Open `index.html` directly, or run `python3 -m http.server 8000` in this folder
and visit `http://localhost:8000`.

## Deploy free

For GitHub Pages, enable **Settings → Pages → Deploy from branch** with the
repository root as the publishing directory. Netlify and Vercel need no build
command; publish directory is `.`.

## Edit content later

- **Chapter bodies:** edit the matching file in `content/source/`, then run
  `python3 tools/build.py` to regenerate `chapters/*.html` (+ question bank,
  practical). Diagrams/extra Q&A live in `tools/extras.py`.
- **Hubs:** edit `tools/hubs1.py` / `tools/hubs2.py`, then run them. Shared
  selectors, progress and practice links live in `tools/hub_practice.py`; chapter
  membership comes from `tools/tpl.py`. All five hubs link to separate chapter
  question pages and official SQP sections. Run `python3 tests/audit_site.py` after rebuilding.
- **Styling/behaviour:** `assets/css/styles.css`, `assets/js/app.js`.
- Keep relative links and avoid external dependencies. Progress and theme are
  stored only in the browser (localStorage). See `docs/AUDIT.md` for the
  content audit and quality checks.

## Chapter-wise question bank

Open `question-bank.html` and choose a chapter. Each of the 20 chapters has its
own URL (for example, `practice/u1-ch1.html`) and **220 questions**:

| Type | Per chapter | All 20 chapters |
| --- | ---: | ---: |
| MCQ | 60 | 1,200 |
| Short | 40 | 800 |
| Long | 40 | 800 |
| Application | 40 | 800 |
| Competitive-style | 40 | 800 |
| **Total** | **220** | **4,400** |

This adds 30 of **each** written type per chapter: 2,400 additional written
questions. In-scope existing questions are retained; scope-sensitive sources were
corrected rather than kept just to preserve their wording. The reviewed 430-item
base is supplemented by 3,970 scenario-derived items using 280 topic packs.
Related variants revisit a topic through different assessment tasks; they are not
4,400 independently sourced official exam questions.

Answers stay hidden in native `<details>` until opened, including offline without
JavaScript. MCQ choices are self-study, not scored or saved. Type filtering and six
sets-of-ten MCQ jump links remain available; no-JS users see all 220 questions.

Every question shows its **syllabus topic reference** (e.g. `Syllabus topic: B8`).
A question additionally shows a **PYQ year reference** (`PYQ: 24-25`, linking to the
official SQP questions for that chapter) only when it closely matches an official
PYQ on the same topic. The match is a weighted token-overlap check against
`content/pyq/chapterwise.md` (content words, rare terms weighted up, fill-in/option
letters required to agree). Original questions that do not mirror a real PYQ show
no year.

### Official syllabus review

- Open **`syllabus-audit.html`** for sources, learning-outcome references, scope and
  methodology. Every question links to its mapped curriculum topic.
- **`docs/question-syllabus-audit.csv`** lists every current question ID, topic
  references, source lineage, exact prompt and content fingerprint.
- The review uses both official **2026–27 Class X IT-402** and **Class X
  Employability Skills** curricula, not just existing website notes.
- `content/practice/syllabus-review.json` records 710 reviewed source entries and
  the reviewed expansion-engine fingerprint. Builds reject unreviewed edits.
  Fingerprints detect changes, not semantic correctness; review against the
  original curriculum is still required before updating an approval.
- `content/practice/audit-changes.json` records source corrections. Longer Part A
  questions change the practice format, not the syllabus. Competitive-style means
  reasoning within the prescribed topics, not a named competition's syllabus.
- The preserved mixed-revision and historical SQP archives are separate from this
  4,400-item review and are labelled accordingly; the review does not certify all
  older parallel study notes or archive questions.

### Maintain and test

Edit the source files under `content/practice/`; see their README for authoring
formats and mandatory review updates. Never bulk-approve changed hashes without
checking the source content and affected generated variants.

```bash
python3 tools/build.py && python3 tools/hubs1.py && python3 tools/hubs2.py && python3 tools/pyq.py
python3 tests/audit_site.py
node --check assets/js/app.js
```

`python3 tools/practice.py` rebuilds just chapter practice and its audit artifacts.
Optional browser tests use Playwright/Chromium and a local static server:
`python3 tests/browser_practice.py`. `BASE_URL` and `CHROMIUM_EXECUTABLE` override
its server and browser. No browser dependency is shipped with the study website.

## Hindi / Hinglish language switching

A language picker sits in the top bar (English · हिंदी · Hinglish) and works on
every page; the choice is remembered in `localStorage`.

- **Offline:** navigation, buttons, labels and common phrases translate from a
  local dictionary in `assets/js/i18n.js` — this part needs no internet.
- **Online:** body text (questions, answers, notes) is translated on demand with
  the free Google Translate endpoint and cached in `localStorage`, so a page
  translated once opens instantly next time. Offline, untranslated text simply
  stays in English — the site never breaks.
- **Technical terms** (`Fill Format`, `Goal Seek`, `SQL`, `Ctrl+Shift+N`, menu
  paths, …) are protected so they stay intact in both Hindi and Hinglish; Hinglish
  is the Hindi translation re-rendered in Latin script.

Dynamic labels (progress, quiz score, filters) go through the same dictionary, so
the whole interface switches language together. Validate scripts with
`node --check assets/js/app.js && node --check assets/js/i18n.js`.
