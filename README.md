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
├── question-bank.html, practical.html          # quiz + sample paper, lab + viva
├── revision.html, book-ch1-5.html              # cheat sheet, legacy printable book
├── assets/css/styles.css                       # shared responsive + print styling
├── assets/js/app.js                            # theme, search, progress, quiz, timer
├── content/*.md                                # editable curriculum outlines
├── content/source/*.md                         # imported deep-note sources
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
- **Hubs:** edit `tools/hubs1.py` / `tools/hubs2.py`, then run them.
- **Styling/behaviour:** `assets/css/styles.css`, `assets/js/app.js`.
- Keep relative links and avoid external dependencies. Progress and theme are
  stored only in the browser (localStorage). See `docs/AUDIT.md` for the
  content audit and quality checks.
