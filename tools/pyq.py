#!/usr/bin/env python3
"""Generate pyq.html — official-Paper library + chapter-wise PYQ bank + trends."""
import re, pathlib
from md import md_blocks
from tpl import page

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "content" / "pyq"


def prep(text):
    # root page: fix relative links written for chapters/
    text = text.replace("](../", "]( ")
    text = text.replace("]( ", "](")
    # "- [TAG] question → answer" lines into QA cards
    text = re.sub(r"(?m)^- \[(.+?)\] (.+?)\s+→\s+(.+)$",
                  lambda m: f"@@QA@@[{m.group(1)}] {m.group(2).strip()}|||{m.group(3).strip()}@@END@@",
                  text)
    # chapter headings: strip parenthetical link, add chapter-link line after
    def head_repl(m):
        tag, title, url = m.group(1), m.group(2), m.group(3)
        return f"### {tag} · {title}\n\n*📖 [Open the full chapter →]({url})*"
    text = re.sub(r"(?m)^### (C-[A-Za-z0-9]+) · (.+?) \(\[Chapter →\]\((.+?)\)\)$",
                  head_repl, text)
    return text


def qa_html(m):
    return f'<div class="qa"><strong>{m.group(1)}</strong><br>{m.group(2)}</div>'


def section(fname):
    text = (SRC / fname).read_text(encoding="utf-8")
    text = re.sub(r"^# (.*)$", r"## \1", text, count=1, flags=re.M)
    body, toc = md_blocks(prep(text))
    body = re.sub(r"@@QA@@(.+?)\|\|\|(.+?)@@END@@", qa_html, body, flags=re.S)
    # canonical chapter anchors: C-U1..C-U5, C-Ch1..C-Ch15
    def _canon(m):
        g = m.group(2)
        tag = "U" + g[1:] if g[0] == "u" else "Ch" + g[2:]
        return m.group(1) + f'id="C-{tag}"'
    body = re.sub(r'(<h3[^>]*?)id="c-(u\d+|ch\d+)[^"]*"', _canon, body)
    return body, [t for t in toc if t[0] == 2]


def main():
    lib, lib_toc = section("papers.md")
    bank, bank_toc = section("chapterwise.md")
    trends, trends_toc = section("trends.md")
    toc_html = ('<div class="toc"><b>On this page:</b> <a href="#timer">Timer</a> '
                + " ".join(f'<a href="#{a}">{t}</a>'
                           for _, a, t in lib_toc + bank_toc + trends_toc) + "</div>")
    timer = """<h2 class="section-title" id="timer">⏱️ Timed PYQ mode (2 hours)</h2>
<div class="timer card"><p>Open an official SQP from the library, start the timer, and write answers on paper. 30 min Section A + 80 min Section B + 10 min revision — then mark yourself with the MS.</p>
<p class="timer-display">02:00:00</p>
<p><button class="button" id="startTimer">Start</button> <button class="button" id="pauseTimer">Pause</button> <button class="button" id="resetTimer">Reset</button></p></div>"""
    fig = ('<figure class="shot"><img src="assets/img/pyq-papers.jpg" '
           'alt="Stack of previous year question papers with timer" loading="lazy">'
           '<figcaption>PYQ Practice — real CBSE papers, chapter-wise.</figcaption></figure>')
    main_html = f"""<div class="crumbs"><a href="index.html">Home</a> / PYQ Practice</div>
<h1>PYQ practice — official papers, solved</h1>
<p class="card"><b>4 official CBSE Sample Papers (2022-23 → 2025-26) with marking schemes, 158 chapter-wise questions with answers, trend tables and a 2-hour timer.</b> Your session's paper is first. Pre-2024 papers: practise Part A + Units 1–3 only (old Unit 4 skipped).</p>
{fig}
{toc_html}
{timer}
{lib}
{bank}
{trends}
<nav class="card prevnext"><a href="question-bank.html">← Previous: Question Bank</a><span style="float:right"><a href="practical.html">Next: Practical →</a></span></nav>"""
    (ROOT / "pyq.html").write_text(
        page("PYQ Practice · IT 402", "Official CBSE IT 402 previous year questions chapter-wise with answers, trends and timer", "pyq.html", main_html),
        encoding="utf-8")
    print("pyq.html")


if __name__ == "__main__":
    main()
