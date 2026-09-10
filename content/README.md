# Content map

The HTML pages are the publishable layer. Sources and generators:

- `content/source/*.md` — imported deep notes (source of truth for chapter bodies,
  question bank and practical guide; originally from `IT-402-Complete-Package.zip`).
- `content/part-a.md`, `unit1-writer.md`, `unit2-calc.md`, `unit3-dbms.md`,
  `unit4-safety.md`, `assessment.md` — short curriculum outlines per area.
- `tools/extras.py` — per-chapter diagrams, extra Q&A banks, quiz data.
- `tools/md.py`, `tools/tpl.py` — Markdown converter + shared page templates.
- `content/practice/*.txt` — base questions and 14 reviewed scenario packs per
  chapter; see its README. `tools/practice_expansion.py` fills each chapter to
  exactly 60 MCQs and 40 each of the four written types (220 questions total).
- `content/practice/syllabus-review.json` and `tools/syllabus_review.py` — official
  scope references and mandatory source/template review fingerprints; generate
  `syllabus-audit.html` and the 4,400-row `docs/question-syllabus-audit.csv`.
- `tools/practice.py` — chapter directory and 20 separate question pages; merges
  earlier mapped quizzes and written practice without changing the official SQP bank.
- `tools/build.py` — generates `chapters/*.html`, `practice/*.html`,
  `question-bank.html`, `mixed-practice.html` and `practical.html`.
- `tools/hubs1.py`, `tools/hubs2.py` — generate index, syllabus, revision,
  part-a and unit hub pages.

Regenerate everything:

```bash
python3 tools/build.py && python3 tools/hubs1.py && python3 tools/hubs2.py && python3 tools/pyq.py
```

Keep procedures aligned to LibreOffice Writer, Calc and Base. Shared appearance is
in `assets/css/styles.css`; interactions are in `assets/js/app.js`.
