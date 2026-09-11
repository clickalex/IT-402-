#!/usr/bin/env python3
"""Build the chapter question directory and 20 standalone, offline practice pages."""
from collections import Counter
from hashlib import sha256
from html import escape
from pathlib import Path

from tpl import CHAPTERS, GROUPS, BY_ID, page
from quiz import QUIZZES, QUIZ_CHAPTERS, PYQ_ANCHOR
from trend_practice import PRACTICE
from practice_expansion import expand_bank
from syllabus_review import approve, syllabus_links, pyq_reference, write_audit, validate_expansion_engine

ROOT = Path(__file__).resolve().parents[1]
TYPES = [('mcq', 'MCQs'), ('short', 'Short questions'), ('long', 'Long questions'),
         ('application', 'Application questions'), ('competitive', 'Competitive-style challenges')]


def read_rows(filename, width):
    result, chapter = {}, None
    for number, line in enumerate((ROOT / 'content/practice' / filename).read_text(encoding='utf-8').splitlines(), 1):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if line.startswith('[') and line.endswith(']'):
            chapter = line[1:-1]
            if chapter not in BY_ID or chapter in result:
                raise ValueError(f'{filename}:{number}: unknown or repeated chapter')
            result[chapter] = []
            continue
        fields = [part.strip() for part in line.split('|')]
        if chapter is None or len(fields) != width or not all(fields):
            raise ValueError(f'{filename}:{number}: expected {width} nonempty fields inside a chapter')
        result[chapter].append(fields)
    if set(result) != set(BY_ID):
        raise ValueError(f'{filename}: missing chapter coverage')
    return result


def load_bank(expand=True):
    mcqs, written = read_rows('mcqs.txt', 6), read_rows('written.txt', 4)
    bank = {cid: {kind: [] for kind, _ in TYPES} for cid in BY_ID}
    seen = set()
    for cid in BY_ID:
        for row_number, fields in enumerate(mcqs[cid], 1):
            question, answer, wrong1, wrong2, wrong3, explanation = fields
            reviewed = approve(f'mcq:{cid}:{row_number}', fields)
            options = [answer, wrong1, wrong2, wrong3]
            if len(set(options)) != 4:
                raise ValueError(f'{cid}: repeated MCQ option: {question}')
            key = question.casefold().strip()
            if key in seen:
                raise ValueError(f'duplicate authored prompt: {question}')
            seen.add(key)
            # Stable distribution of answer positions without changing the source key.
            offset = int(sha256(question.encode()).hexdigest()[:8], 16) % 4
            options = options[offset:] + options[:offset]
            bank[cid]['mcq'].append(dict(question=question, answer=answer, options=options, explanation=explanation, marks=1, **reviewed))
        for row_number, fields in enumerate(written[cid], 1):
            kind, question, marks, answer = fields
            reviewed = approve(f'written:{cid}:{row_number}', fields)
            if kind not in {'short', 'long', 'application', 'competitive'}:
                raise ValueError(f'{cid}: unknown question type {kind}')
            key = question.casefold().strip()
            if key in seen:
                raise ValueError(f'duplicate authored prompt: {question}')
            seen.add(key)
            mark_value = int(marks)
            if mark_value != {'short': 2, 'long': 4, 'application': 4, 'competitive': 0}[kind]:
                raise ValueError(f'{cid}: unexpected suggested marks for {kind}')
            bank[cid][kind].append(dict(question=question, answer=answer, marks=mark_value, **reviewed))
        if len(bank[cid]['mcq']) < 10 or any(len(bank[cid][kind]) < 2 for kind, _ in TYPES[1:]):
            raise ValueError(f'{cid}: insufficient new questions')
    # Keep all earlier chapter-mapped MCQs and written practice available here too.
    legacy_numbers = Counter()
    for (_, questions), chapters in zip(QUIZZES, QUIZ_CHAPTERS):
        for (question, options, answer), cid in zip(questions, chapters):
            legacy_numbers[cid] += 1
            reviewed = approve(f'legacy-mcq:{cid}:{legacy_numbers[cid]}', [question, options, answer])
            if question.casefold().strip() not in seen:
                bank[cid]['mcq'].append(dict(question=question, options=options, answer=answer, explanation='', marks=1, **reviewed))
                seen.add(question.casefold().strip())
    for cid, (question, marks, answer) in PRACTICE.items():
        reviewed = approve(f'trend:{cid}', [question, marks, answer])
        if question.casefold().strip() not in seen:
            bank[cid]['application'].append(dict(question=question, answer=answer, marks=marks, **reviewed))
            seen.add(question.casefold().strip())
    if not expand:
        return bank
    validate_expansion_engine()
    scenarios = read_rows('scenarios.txt', 8)
    extra = read_rows('scenarios-extra.txt', 8)
    return expand_bank(bank, {cid: scenarios[cid] + extra[cid] for cid in bank}, approve)


def counts(bank):
    return Counter({kind: sum(len(chapter[kind]) for chapter in bank.values()) for kind, _ in TYPES})


def chapter_picker(chapters=CHAPTERS, current='', prefix='', select_id='practice-chapter'):
    """Normal GET fallback to the directory, enhanced to direct page navigation."""
    options = ['<option value="" disabled' + (' selected' if not current else '') + '>Choose a chapter…</option>']
    for c in chapters:
        selected = ' selected' if c[0] == current else ''
        options.append(f'<option value="{c[0]}" data-page="{prefix}practice/{c[0]}.html"{selected}>{escape(c[2])}</option>')
    return (f'<form class="practice-picker" data-practice-navigation action="{prefix}question-bank.html" method="get">'
            f'<label for="{select_id}"><b>Choose your chapter</b></label>'
            f'<div class="hub-practice-controls"><select class="hub-chapter-select" id="{select_id}" name="chapter" required>'
            + ''.join(options) + '</select><button class="button" type="submit">Open chapter questions →</button></div></form>'
            '<noscript><p>Use the chapter links below or the question directory to open a page without JavaScript. All Show answer controls work without JavaScript.</p></noscript>')


def render_question(cid, kind, number, q):
    ident = f'{kind}-{number}'
    prompt = escape(q['question'])
    marks = f'{q["marks"]} suggested mark' + ('s' if q['marks'] != 1 else '') if q['marks'] else 'Ungraded extension'
    if kind == 'mcq':
        options = ''.join(f'<label class="practice-option"><input type="radio" name="{cid}-{ident}" value="{i}"> '
                          f'<span>{chr(65+i)}. {escape(option)}</span></label>' for i, option in enumerate(q['options']))
        question = f'<fieldset><legend><b>{number}. {prompt}</b></legend>{options}</fieldset>'
        answer = f'<p><b>{chr(65+q["options"].index(q["answer"]))}. {escape(q["answer"])}</b></p>'
        if q['explanation']:
            answer += f'<p>{escape(q["explanation"])}</p>'
    else:
        question = f'<h3>{number}. {prompt}</h3>'
        answer = f'<p>{escape(q["answer"])}</p>'
    return (f'<article class="practice-question" id="{ident}" data-question-type="{kind}">'
            f'<p class="question-meta">{marks}</p>{question}{syllabus_links(q)}{pyq_reference(q)}'
            f'<details class="answer-reveal"><summary><span class="answer-show">Show answer</span>'
            f'<span class="answer-hide">Hide answer</span><span class="sr-only"> for {kind} question {number}</span></summary>'
            f'<div class="model-answer">{answer}</div></details></article>')


def render_chapter(c, bank):
    cid, filename, title = c[:3]
    questions = bank[cid]
    total = sum(len(items) for items in questions.values())
    body = [f'<div class="crumbs"><a href="../index.html">Home</a> / <a href="../question-bank.html">Question directory</a> / {escape(title)}</div>',
            f'<h1>{escape(title)} · {total} questions</h1>',
            f'<p class="card {c[5]}"><b>{total} questions for this chapter only.</b> Select an MCQ option or write your own response, then choose Show answer to self-check. Selecting an option does not reveal the answer. Choices are not scored or saved.</p>',
            chapter_picker(current=cid, prefix='../'),
            f'<p><a href="../chapters/{filename}">Read chapter notes →</a> · <a href="../{c[4]}">Unit overview →</a> · <a href="../pyq.html#{PYQ_ANCHOR[cid]}">Official SQP questions →</a></p>',
            '<p class="warning">Syllabus-mapped authored practice for CBSE Class X IT-402 (2026–27), not official questions or predictions. Competitive-style tasks use the same prescribed topics for higher-order reasoning, not an external competition syllabus. Part A long responses use a longer practice format, not a claim about four-mark board questions. <a href="../syllabus-audit.html">Read the source-based audit →</a></p>',
            '<nav class="toc practice-types" aria-label="Question types">' + ''.join(f'<a href="#{kind}">{label} ({len(questions[kind])})</a>' for kind, label in TYPES) + '</nav>',
            f'<div class="practice-controls" data-question-controls hidden><label for="question-type"><b>Show question type</b></label>'
            f'<select class="hub-chapter-select" id="question-type" data-question-filter><option value="all">All questions ({total})</option>'
            + ''.join(f'<option value="{kind}">{label} ({len(questions[kind])})</option>' for kind, label in TYPES)
            + f'</select><p data-question-status role="status" aria-live="polite">{total} questions shown</p></div>',
            '<button type="button" class="button" data-hide-answers hidden>Hide all answers</button>']
    for kind, label in TYPES:
        body.append(f'<section class="practice-section" data-practice-section="{kind}" aria-labelledby="{kind}"><h2 id="{kind}">{label} · {len(questions[kind])}</h2>')
        if kind == 'mcq':
            body.append('<nav class="toc mcq-batches" aria-label="MCQ sets of ten">' + ''.join(
                f'<a href="#mcq-{start}">MCQs {start}–{min(start+9, len(questions[kind]))}</a>'
                for start in range(1, len(questions[kind])+1, 10)) + '</nav>')
        body.extend(render_question(cid, kind, n, q) for n, q in enumerate(questions[kind], 1))
        body.append('</section>')
    index = CHAPTERS.index(c)
    prev = f'<a href="{CHAPTERS[index-1][0]}.html">← Previous chapter questions</a>' if index else '<a href="../question-bank.html">← Question directory</a>'
    nxt = f'<a href="{CHAPTERS[index+1][0]}.html">Next chapter questions →</a>' if index < len(CHAPTERS)-1 else '<a href="../mixed-practice.html">Mixed revision &amp; sample papers →</a>'
    body.append(f'<nav class="pager" aria-label="Question page navigation">{prev}{nxt}</nav>')
    return page(f'{escape(title)} · Questions · IT 402', 'Chapter-specific MCQs, short, long, application and competitive-style questions with hidden answers', filename, '\n'.join(body), prefix='../')


def render_directory(bank):
    totals = counts(bank)
    body = ['<div class="crumbs"><a href="index.html">Home</a> / Question directory</div>',
            '<h1>Choose a chapter. Practise at your pace.</h1>',
            f'<p class="card"><b>{sum(totals.values())} questions across 20 separate chapter pages.</b> '
            + ' · '.join(f'{totals[kind]} {label.lower()}' for kind, label in TYPES)
            + '. Every answer stays hidden until you choose Show answer.</p>',
            '<p>No need to scroll through every chapter’s MCQs. Select your chapter to open its own question page, or use a chapter card below. Each page includes all five question types.</p>',
            '<section class="card" id="quiz"><h2>Select a chapter</h2>', chapter_picker(),
            '<p id="practice-navigation-status" role="status"></p></section>',
            '<p>These are original learning exercises, not official exam questions or predictions. All four written types practise prescribed topics; longer responses do not imply the official board paper uses that answer length. Study notes and official SQP links are available on every chapter page.</p>']
    for title, ids in GROUPS:
        body.append(f'<section><h2>{escape(title)}</h2><div class="cards">')
        for cid in ids:
            chapter = BY_ID[cid]
            items = bank[cid]
            body.append(f'<article class="card {chapter[5]}"><h3><a href="practice/{cid}.html">{escape(chapter[2])}</a></h3>'
                        f'<p><b>{sum(map(len, items.values()))} questions</b><br>{len(items["mcq"])} MCQs · {len(items["short"])} short · {len(items["long"])} long · '
                        f'{len(items["application"])} application · {len(items["competitive"])} challenges</p>'
                        f'<a class="button" href="practice/{cid}.html">Open chapter questions →</a></article>')
        body.append('</div></section>')
    body.append('<p class="card"><a href="syllabus-audit.html">Official curriculum references and every-question audit →</a></p>')
    body.append('<section class="card" id="trend-practice"><h2>Looking for full-paper revision?</h2><p>The earlier mixed quizzes and sample papers are a separate legacy revision archive, not part of the current question-level syllabus audit. Use the chapter pages for the audited question sets.</p><a href="mixed-practice.html">Mixed revision &amp; sample papers →</a> · <a href="pyq.html">Official SQP library →</a></section>')
    return page('Chapter question directory · IT 402', f'{totals["mcq"]} MCQs and chapter-wise written practice on 20 separate pages with hidden answers', 'question-bank.html', '\n'.join(body))


def build_practice():
    bank = load_bank()
    (ROOT / 'practice').mkdir(exist_ok=True)
    for chapter in CHAPTERS:
        (ROOT / 'practice' / f'{chapter[0]}.html').write_text(render_chapter(chapter, bank), encoding='utf-8')
    (ROOT / 'question-bank.html').write_text(render_directory(bank), encoding='utf-8')
    write_audit(bank)
    print('Chapter practice:', dict(counts(bank)))


if __name__ == '__main__':
    build_practice()
