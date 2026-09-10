# Static Website Builder — Copy-Paste Prompt for IT 402

> How to use: open any AI website builder (v0, Lovable, Bolt, ChatGPT, Arena, etc.), **attach/upload all the IT-402 .md notes files**, then paste the MASTER PROMPT below.

---

## MASTER PROMPT (paste this) 👇

```text
ROLE: You are an expert front-end developer AND a CBSE Class 10 IT teacher.

GOAL: Build a complete STATIC educational website for CBSE Class 10 Information
Technology (Subject Code 402), session 2026-27. Students will use it to study
every chapter in MORE detail than the notes, prepare for theory (50 marks),
practicals (50 marks), viva and project work.

SOURCE OF TRUTH: I have attached/uploaded my study notes (markdown files for
Part A, Unit 1 Writer, Unit 2 Calc, Unit 3 DBMS, Unit 4 Safety, question bank
and practical guide). Use them as the base content, then EXPAND each topic with
deeper explanations, more examples, simple diagrams and exam tips. All content
must match the CBSE 2026-27 syllabus for IT-402 (Job Role: Domestic Data Entry
Operator). All software procedures must use LibreOffice Writer / Calc / Base
menu paths and shortcuts — NEVER MS Word/Excel/Access.

TECH CONSTRAINTS (strict):
- 100% STATIC: plain HTML + CSS + vanilla JavaScript only. No backend, no
  database, no build step, no framework.
- Must work when opened directly (file://) AND when hosted on GitHub Pages /
  Netlify / Vercel.
- Prefer ZERO external dependencies (no CDN) so the site works offline. Use
  system font stack. All diagrams must be pure CSS/SVG (no external images).

SITE MAP (multi-page site with shared navbar + sidebar):
1. index.html — Home: hero, subject overview, marks table (Theory 50 +
   Practical 50), unit cards with progress bars, "Start Studying" + "Quick
   Revision" buttons, exam countdown to Feb 2027 boards.
2. syllabus.html — Full syllabus, chapter-wise weightage, theory paper pattern
   (Section A objective 24 + Section B subjective 26), practical marks split.
3. part-a.html — Employability Skills: Units 1-5 (Communication-II,
   Self-Management-II, ICT-II, Entrepreneurial-II, Green Skills-II).
4. unit1-writer.html — Ch1 Styles, Ch2 Images, Ch3 ToC + Templates + Track Changes.
5. unit2-calc.html — Ch4 Scenarios + Goal Seek, Ch5 Macros, Ch6 Linking,
   Ch7 Share & Review.
6. unit3-dbms.html — Ch8 DBMS Intro, Ch9 Base Tables, Ch10 Relationships,
   Ch11 Queries, Ch12 Forms & Reports.
7. unit4-safety.html — Ch13 Health/Safety/Security, Ch14 Workplace Quality +
   Ergonomics, Ch15 Accidents & Emergencies.
8. question-bank.html — Objective practice (1-mark), short answers (2-mark) and
   long answers (4-mark) with model answers + a timed 50-mark sample paper.
9. practical.html — 15 practicals with steps (5 Writer + 5 Calc + 5 Base),
   project/file structure, 30 viva questions with answers.
10. revision.html — 2-page "exam morning" cheat sheet: all menu paths,
    shortcuts, keys, numbers (50-70 cm, 20-20-20, 101/102/108) oningat-a-glance cards.

EVERY CHAPTER section must follow this template:
a) 🎯 Marks lens (what gets asked, weightage)
b) 📖 Concepts explained simply, with comparison tables + a real-life example
c) 🖱️ Exact steps / menu paths in numbered styled boxes (copyable), with
   shortcuts highlighted as <kbd> chips
d) 🧠 Memory trick + ⚠️ Common mistakes box
e) ❓ Exam Q&A: at least 5 one-markers, 3 two-markers with answers, 1-2
   four-markers with full model answers
f) 💻 "Try on computer" practical mini-task
g) Prev/Next chapter links at the bottom

FEATURES (all client-side JS):
- Sticky top navbar + collapsible sidebar chapter navigation with active link
  highlighting; breadcrumbs on every page.
- Client-side SEARCH box that finds text across all chapters and jumps to it.
- Dark / Light mode toggle (saved in localStorage).
- "Mark as complete" checkbox per chapter with progress bars on Home
  (localStorage).
- Interactive MCQ quiz on question-bank page: click option → instant
  correct/wrong feedback + final score.
- Sample-paper timer (2-hour countdown with start/pause/reset).
- Fully responsive (mobile-first), print-friendly stylesheet for revision page,
  back-to-top button, smooth scrolling, accessible (semantic tags, alt text,
  good contrast).

DESIGN:
- Clean study-theme: white/soft background in light mode, proper dark mode
  palette. Colour-code the 5 parts (A=teal, U1=blue, U2=green, U3=purple,
  U4=orange). Card layout, styled tables, timeline/step components, sticky
  "On this page" mini-TOC on desktop.
- No lorem ipsum — every page must be filled with REAL study content from my
  notes, expanded.

OUTPUT:
1. Show the file tree first.
2. Then give COMPLETE code for every file (index.html, other pages, styles.css,
   app.js), ready to save and open.
3. End with a short README: how to run locally + how to deploy free on GitHub
   Pages / Netlify, and how I can edit content later.

QUALITY CHECK before finishing: all links work, no empty pages, no external
dependencies, LibreOffice-only procedures, valid HTML, JS has no errors.
```

---

## If you want SEPARATE mini-website per unit instead

Use the MASTER PROMPT above, but replace the SITE MAP section with just one line,
e.g. `Only build: index.html (Unit 3 home) + ch8.html + ch9.html + ch10.html +
ch11.html + ch12.html + quiz.html`. Repeat for each unit:

- Mini-site 1: Part A (U1–U5) — teal theme
- Mini-site 2: Unit 1 Writer (Ch1–Ch3) — blue theme
- Mini-site 3: Unit 2 Calc (Ch4–Ch7) — green theme
- Mini-site 4: Unit 3 DBMS (Ch8–Ch12) — purple theme
- Mini-site 5: Unit 4 Safety (Ch13–Ch15) — orange theme

## Handy follow-up prompts (paste after the first result)

1. `Now expand Chapter [X] further: add 2 solved examples, a labelled SVG diagram, and 10 more MCQs with answers.`
2. `Add 20 more viva questions with one-line answers to practical.html`
3. `Make a single-file version (all-in-one .html) of the revision page for offline phone use.`
4. `Check all pages: fix broken links, validate the JS, and list what you changed.`
