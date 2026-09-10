#!/usr/bin/env python3
"""Generate chapters/*.html + question-bank.html + practical.html from Markdown."""
import re, pathlib
from md import md_blocks, inline
from tpl import CHAPTERS, BY_ID, SHORT, sidebar, page
from extras import DIAGRAMS, EXTRA_QA
from quiz import QUIZZES, CHAPTER_IMG, HUB_IMG, PYQ_ANCHOR

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "content" / "source"

def split_source(fname, markers):
    text = (SRC / fname).read_text(encoding="utf-8")
    lines = text.split("\n")
    chunks, cur, cur_key = {}, [], None
    for ln in lines:
        hit = next((m for m in markers if ln.strip().startswith(m)), None)
        if hit:
            if cur_key: chunks[cur_key] = "\n".join(cur).strip()
            cur_key, cur = hit, []
        elif cur_key:
            cur.append(ln)
    if cur_key: chunks[cur_key] = "\n".join(cur).strip()
    return chunks

UNIT_FILES = {}
def unit_chunks(fname):
    if fname not in UNIT_FILES:
        ms = [c[7] for c in CHAPTERS if c[6] == fname]
        UNIT_FILES[fname] = split_source(fname, ms)
    return UNIT_FILES[fname]

def build_chapter(idx):
    cid, fname, h1, unit_label, unit_file, theme, src_md, marker = CHAPTERS[idx]
    raw = unit_chunks(src_md)[marker]
    body, toc = md_blocks(raw)
    # insert diagram before first section heading
    if cid in DIAGRAMS:
        diag = f'<h2 class="section-title" id="visual">🖼️ Visual summary</h2>\n{DIAGRAMS[cid]}'
        body = body.replace("<h2", diag + "\n<h2", 1) if "<h2" in body else diag + "\n" + body
    if cid in EXTRA_QA:
        body += "\n" + EXTRA_QA[cid]
    # toc box
    toc_html = '<div class="toc"><b>On this page:</b> ' + " ".join(
        f'<a href="#{a}">{t}</a>' for _, a, t in toc[:14]) + "</div>"
    # prev / next across chain
    if idx > 0:
        p = CHAPTERS[idx - 1]
        prev = f'<a href="{p[1]}">← Previous: {SHORT[p[0]]}</a>'
    else:
        prev = f'<a href="../{unit_file}">← Back: {unit_label}</a>'
    if idx < len(CHAPTERS) - 1:
        nx = CHAPTERS[idx + 1]
        nxt = f'<a href="{nx[1]}">Next: {SHORT[nx[0]]} →</a>'
    else:
        nxt = '<a href="../question-bank.html">Next: Question Bank →</a>'
    num = idx + 1
    img, alt, cap = CHAPTER_IMG[cid]
    pyq_anchor = PYQ_ANCHOR[cid]
    fig = f'<figure class="shot"><img src="../assets/img/{img}" alt="{alt}" loading="lazy"><figcaption>{cap}</figcaption></figure>'
    main = f"""<div class="crumbs"><a href="../index.html">Home</a> / <a href="../{unit_file}">{unit_label}</a> / {SHORT[cid]}</div>
<h1>{h1}</h1>
<p class="card {theme}"><b>Chapter {num} of 20.</b> Deep study page: concepts, exact LibreOffice steps, memory tricks, mistakes to avoid, exam Q&amp;A and a hands-on task. Finish it and tick the box at the bottom.</p>
{fig}
{toc_html}
<article class="chapter {theme}">
{body}
<h2 class="section-title">✅ Done? Mark it complete</h2>
<label class="complete"><input type="checkbox" data-complete="{cid}"> Mark “{SHORT[cid]}” complete</label>
</article>
<p class="pyqlink">📝 <a href="../pyq.html#{pyq_anchor}">Practise board PYQs from this chapter →</a></p>
<nav class="card prevnext">{prev}<span style="float:right">{nxt}</span></nav>"""
    out = ROOT / "chapters" / fname
    out.write_text(page(f"{SHORT[cid]} · IT 402", f"CBSE Class 10 IT 402 2026-27: {h1}", fname, main, prefix="../"), encoding="utf-8")
    return fname

def build_quiz_html():
    parts = []
    for qi, (title, qs) in enumerate(QUIZZES):
        parts.append(f'<div class="quiz"><h3>{title}</h3><p class="quiz-score"><b>Score: 0/0 answered</b> — click an option for instant feedback.</p>')
        for n, (q, opts, ans) in enumerate(qs, 1):
            parts.append(f'<div class="quiz-question" data-answer="{ans}"><b>{n}. {q}</b>')
            for o in opts:
                parts.append(f'<label><input type="radio" name="q{qi}_{n}" value="{o}"> {o}</label>')
            parts.append('<p class="feedback"></p></div>')
        parts.append("</div>")
    return "\n".join(parts)

def build_question_bank():
    text = (SRC / "IT-402-Question-Bank-and-Sample-Paper.md").read_text(encoding="utf-8")
    text = re.sub(r"^# .*$", "", text, count=1, flags=re.M)
    # convert numbered objective lines "1. Q → A" into QA blocks
    def obj_repl(m):
        q, a = m.group(1).strip(), m.group(2).strip()
        return f"@@QA@@{q}|||{a}@@END@@"
    text = re.sub(r"(?m)^\d+\.\s+(.+?)\s+→\s+(.+)$", obj_repl, text)
    # pair Q/S/L-lines with following > Ans quotes
    text = re.sub(r"(?m)^((?:Q|S|L)\d+\..+)$\n> \*\*Ans:\*\* (.+)$",
                  lambda m: f"@@QA@@{m.group(1).strip()}|||{m.group(2).strip()}@@END@@", text)
    body, qb_toc = md_blocks(text)
    def qa_html(m):
        return f'<div class="qa"><strong>{m.group(1)}</strong><br>{m.group(2)}</div>'
    body = re.sub(r"@@QA@@(.+?)\|\|\|(.+?)@@END@@", qa_html, body, flags=re.S)
    timer = """<h2 class="section-title" id="timer">⏱️ Timed sample-paper mode (2 hours)</h2>
<div class="timer card"><p>Open a sample paper below, start the timer, and write answers on paper. 30 min Section A + 80 min Section B + 10 min revision.</p>
<p class="timer-display">02:00:00</p>
<p><button class="button" id="startTimer">Start</button> <button class="button" id="pauseTimer">Pause</button> <button class="button" id="resetTimer">Reset</button></p></div>"""
    quiz = f'<h2 class="section-title" id="quiz">🎯 Interactive MCQ quizzes (30 questions · 5 unit quizzes)</h2>\n{build_quiz_html()}'
    qb_img, qb_alt, qb_cap = HUB_IMG["question-bank.html"]
    qb_fig = f'<figure class="shot"><img src="assets/img/{qb_img}" alt="{qb_alt}" loading="lazy"><figcaption>{qb_cap}</figcaption></figure>'
    qb_toc_html = '<div class="toc"><b>On this page:</b> <a href="#quiz">Quizzes</a> <a href="#timer">Timer</a> ' + " ".join(f'<a href="#{a}">{t}</a>' for lvl, a, t in qb_toc if lvl == 2) + "</div>"
    main = f"""<div class="crumbs"><a href="index.html">Home</a> / Question Bank</div>
<h1>Question bank &amp; sample papers</h1>
<p class="card"><b>100 one-markers + rapid-fire + 25 short + 14 long answers with models + TWO full 50-mark sample papers.</b> Attempt without notes first. Subjective frame: definition → steps/example → benefit or precaution.</p>
{qb_fig}
{qb_toc_html}
{quiz}
{timer}
{body}"""
    (ROOT / "question-bank.html").write_text(
        page("Question Bank · IT 402", "IT 402 question bank, quiz and 50-mark sample paper", "question-bank.html", main), encoding="utf-8")

def build_practical():
    text = (SRC / "IT-402-Practical-File-and-Project-Guide.md").read_text(encoding="utf-8")
    text = re.sub(r"^# .*$", "", text, count=1, flags=re.M)
    # bold-lead practical lines **W1. ...:** ... → QA cards
    text = re.sub(r"(?m)^(\*\*(?:W\d|C\d|D\d|M\d)\..+)$", r"@@P@@\1@@END@@", text)
    body, pr_toc = md_blocks(text)
    body = re.sub(r"@@P@@(.+?)@@END@@",
                  lambda m: f'<div class="qa">{m.group(1)}</div>', body, flags=re.S)
    pr_img, pr_alt, pr_cap = HUB_IMG["practical.html"]
    pr_fig = f'<figure class="shot"><img src="assets/img/{pr_img}" alt="{pr_alt}" loading="lazy"><figcaption>{pr_cap}</figcaption></figure>'
    pr_toc_html = '<div class="toc"><b>On this page:</b> ' + " ".join(f'<a href="#{a}">{t}</a>' for lvl, a, t in pr_toc if lvl == 2) + "</div>"
    main = f"""<div class="crumbs"><a href="index.html">Home</a> / Practical Guide</div>
<h1>Practical file, project &amp; viva guide</h1>
<p class="card"><b>Practical 50:</b> Writer 5 + Calc 5 + Base 10 + Viva 10 + Project 10 + File 10. Create folder <code>IT402_YourName</code>; keep editable files and PDFs separately. LibreOffice only. Now with <b>25 tasks + mock exam + troubleshooting + 50 viva Qs</b>.</p>
{pr_fig}
{pr_toc_html}
{body}"""
    (ROOT / "practical.html").write_text(
        page("Practical Guide · IT 402", "IT 402 practicals, project structure and viva questions", "practical.html", main), encoding="utf-8")

if __name__ == "__main__":
    (ROOT / "chapters").mkdir(exist_ok=True)
    for i in range(len(CHAPTERS)):
        print("chapter", build_chapter(i))
    build_question_bank(); print("question-bank.html")
    build_practical(); print("practical.html")
