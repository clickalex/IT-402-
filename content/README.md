# Content map

The HTML pages are the publishable layer. Sources and generators:

- `content/source/*.md` — imported deep notes (source of truth for chapter bodies,
  question bank and practical guide; originally from `IT-402-Complete-Package.zip`).
- `content/part-a.md`, `unit1-writer.md`, `unit2-calc.md`, `unit3-dbms.md`,
  `unit4-safety.md`, `assessment.md` — short curriculum outlines per area.
- `tools/extras.py` — per-chapter diagrams, extra Q&A banks, quiz data.
- `tools/md.py`, `tools/tpl.py` — Markdown converter + shared page templates.
- `tools/build.py` — generates `chapters/*.html`, `question-bank.html`, `practical.html`.
- `tools/hubs1.py`, `tools/hubs2.py` — generate index, syllabus, revision,
  part-a and unit hub pages.

Regenerate everything:

```bash
python3 tools/build.py && python3 tools/hubs1.py && python3 tools/hubs2.py
```

Keep procedures aligned to LibreOffice Writer, Calc and Base. Shared appearance is
in `assets/css/styles.css`; interactions are in `assets/js/app.js`.
