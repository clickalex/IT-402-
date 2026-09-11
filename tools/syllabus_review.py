"""Reviewed curriculum traceability. A changed source needs an explicit new review.

Fingerprint checks prevent silent content drift; they are NOT an automated proof
of educational correctness. Outcome mapping was made against the cited curricula.
"""
import csv
import hashlib
import io
import json
import math
import re
from functools import lru_cache
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


@lru_cache(maxsize=1)
def registry():
    return json.loads((ROOT / 'content/practice/syllabus-review.json').read_text(encoding='utf-8'))


def validate_expansion_engine():
    expected = registry()['expansion_engine_sha256']
    actual = hashlib.sha256((ROOT / 'tools/practice_expansion.py').read_bytes()).hexdigest()
    if actual != expected:
        raise ValueError('Question expansion templates changed after syllabus review; review the new task/answer formats before updating the recorded engine fingerprint.')


def approve(key, fields):
    data = registry()
    item = data['reviews'].get(key)
    if not item or item.get('decision') != 'in-scope' or item['sha256'] != fingerprint(fields):
        raise ValueError(f'Syllabus review missing or stale for {key}; review the changed prompt/options/answer before updating its fingerprint.')
    if not item['outcomes'] or any(ref not in data['outcomes'] for ref in item['outcomes']):
        raise ValueError(f'Invalid curriculum outcome mapping: {key}')
    return {'syllabus': item['outcomes'], 'review_keys': [key]}


def syllabus_links(question, prefix='../'):
    refs = question.get('syllabus', [])
    if not refs:
        raise ValueError('Question has no reviewed syllabus mapping')
    return '<p class="syllabus-reference"><small>Syllabus topic: ' + ' · '.join(
        f'<a href="{prefix}syllabus-audit.html#{ref}">{escape(ref)}</a>' for ref in refs) + '</small></p>'


def pyq_map():
    """Map each chapter id to its canonical PYQ anchor (C-U1..C-U5, C-Ch1..C-Ch15)."""
    from tpl import CHAPTERS
    anchors = {}
    for c in CHAPTERS:
        cid = c[0]
        if cid.startswith('pa-u'):
            anchors[cid] = 'C-U' + cid.rsplit('-', 1)[1][1:]  # pa-u1 -> C-U1
        else:
            anchors[cid] = 'C-Ch' + cid.rsplit('-ch', 1)[1]    # u3-ch8 -> C-Ch8
    return anchors


PYQ_STOPWORDS = frozenset((
    'a an the is are was were be been being of in on at to for with by from as and or '
    'but if then else this that these those it its which what who whom whose how when '
    'where why can could should would may might must shall will do does did done not no '
    'yes so such more most some any all each every both few several many much own same '
    'other another new old good bad into about over under above below between among '
    'during before after against through'
).split())

PYQ_MATCH_THRESHOLD = 0.6


def _pyq_norm(text):
    text = text.lower().replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    text = re.sub(r'[^a-z0-9]+', ' ', text)
    return re.sub(r'\s+', ' ', text).strip()


def _pyq_tokens(text):
    # Single-character tokens (option/fill-in letters like "A" or "T") are kept,
    # even when they coincide with an English stopword such as "a".
    return [token for token in _pyq_norm(text).split() if len(token) == 1 or token not in PYQ_STOPWORDS]


@lru_cache(maxsize=1)
def _pyq_idf():
    """Inverse document frequency of tokens across the solved PYQ bank.

    Topic-generic words (e.g. "key", "primary", "data") that recur throughout a
    chapter's PYQs get low weight, so two different questions sharing only common
    vocabulary do not look "closely matched"; distinctive words get high weight.
    """
    entries = pyq_entries()
    document_frequency = {}
    for entry in entries:
        for token in set(entry[2]):
            document_frequency[token] = document_frequency.get(token, 0) + 1
    total = len(entries)
    return {token: math.log((total + 1) / (count + 1)) + 1 for token, count in document_frequency.items()}


def _pyq_similarity(tokens_a, tokens_b):
    if not tokens_a or not tokens_b:
        return 0.0
    set_a, set_b = set(tokens_a), set(tokens_b)
    overlap = set_a & set_b
    if not overlap:
        return 0.0
    idf = _pyq_idf()
    unseen = math.log(len(pyq_entries()) + 1) + 1  # rarest possible token
    numerator = 2 * sum(idf.get(token, unseen) for token in overlap)
    denominator = sum(idf.get(token, unseen) for token in set_a) + sum(idf.get(token, unseen) for token in set_b)
    return numerator / denominator


@lru_cache(maxsize=1)
def pyq_entries():
    """Solved PYQ bank as (chapter, session, tokens, single-letters) entries.

    Only in-syllabus entries are kept; ``⛔`` skip-list lines are excluded so an
    authored question never matches a removed topic.
    """
    md = (ROOT / 'content' / 'pyq' / 'chapterwise.md').read_text(encoding='utf-8')
    anchors = pyq_map()
    reverse = {tag: cid for cid, tag in anchors.items()}
    entries = []
    current = None
    for line in md.splitlines():
        stripped = line.strip()
        if stripped.startswith('#'):
            match = re.match(r'^###\s+(C-U\d|C-Ch\d+)\b', stripped)
            current = reverse.get(match.group(1)) if match else None
            continue
        if not current:
            continue
        question = None
        match = re.match(r'^- \[SQP (\d\d-\d\d) [^\]]*\] (.+?) → .+$', stripped)
        if match:
            question = match.group(2)
        else:
            match = re.match(r'^\*\*Q \(SQP (\d\d-\d\d) [^)]*\):\*\* (.+)$', stripped)
            if match:
                question = match.group(2)
        if question is None:
            continue
        tokens = _pyq_tokens(question)
        letters = frozenset(token for token in tokens if len(token) == 1 and token.isalpha())
        entries.append((current, match.group(1), tuple(tokens), letters))
    return entries


def pyq_reference(question, prefix='../'):
    """Render the PYQ session reference for questions that closely match a real PYQ.

    An authored question only shows a PYQ year when an in-syllabus official SQP
    question on the same chapter is a close token match (Dice similarity on content
    words); otherwise no PYQ reference is shown. Single-letter tokens (option or
    fill-in letters such as “T” vs “A”) must agree, so near-identical questions
    with different answers are not cross-tagged.
    """
    refs = question.get('syllabus', [])
    if not refs:
        raise ValueError('Question has no reviewed syllabus mapping')
    outcomes = registry()['outcomes']
    chapters = list(dict.fromkeys(outcomes.get(ref, {}).get('chapter') for ref in refs if outcomes.get(ref, {}).get('chapter')))
    if not chapters:
        raise ValueError('Question has no reviewed syllabus mapping')
    anchors = pyq_map()
    tokens = _pyq_tokens(question['question'])
    letters = frozenset(token for token in tokens if len(token) == 1 and token.isalpha())
    sessions = []
    if len(tokens) >= 2:
        for chapter in chapters:
            for entry_chapter, session, pyq_tokens, pyq_letters in pyq_entries():
                if entry_chapter != chapter:
                    continue
                if len(pyq_tokens) < 2:
                    continue
                if _pyq_similarity(tokens, pyq_tokens) < PYQ_MATCH_THRESHOLD:
                    continue
                if letters and pyq_letters and letters != pyq_letters:
                    continue
                if session not in sessions:
                    sessions.append(session)
    if not sessions:
        return ''
    sessions.sort()
    anchor = anchors[chapters[0]]
    return ('<p class="pyq-reference"><small>PYQ: '
            + ' · '.join(f'<a href="{prefix}pyq.html#{anchor}">{escape(session)}</a>' for session in sessions)
            + '</small></p>')


def audit_csv(bank):
    stream = io.StringIO(newline='')
    # Keep the generated CSV consistent with the repository's LF text files.
    writer = csv.writer(stream, lineterminator='\n')
    writer.writerow(['question_id', 'chapter', 'type', 'outcomes', 'reviewed_sources', 'content_sha256', 'review_date', 'question'])
    for cid, groups in bank.items():
        for kind, questions in groups.items():
            for n, q in enumerate(questions, 1):
                if not q.get('syllabus') or not q.get('review_keys'):
                    raise ValueError(f'Unmapped question: {cid}/{kind}/{n}')
                writer.writerow([f'{cid}/{kind}-{n}', cid, kind, ';'.join(q['syllabus']), ';'.join(q['review_keys']), fingerprint(q), registry()['review_date'], q['question']])
    return stream.getvalue()


def render_audit(bank):
    from tpl import CHAPTERS, page
    data = registry()
    total = sum(len(qs) for groups in bank.values() for qs in groups.values())
    body = [
        '<div class="crumbs"><a href="index.html">Home</a> / <a href="question-bank.html">Question directory</a> / Syllabus audit</div>',
        '<h1>Question-bank syllabus audit · 2026–27</h1>',
        f'<p class="card"><b>{total:,} current chapter-bank questions mapped to published Class X learning outcomes.</b> Each of 20 chapters has 60 MCQs and 40 each of short, long, application and competitive-style questions. Answers are authored practice, not copied official questions or a CBSE endorsement.</p>',
        '<h2>Official sources checked</h2><ul>']
    for source in data['sources'].values():
        body.append(f'<li><a href="{source["url"]}">{escape(source["title"])}</a> — {escape(source["used"])}</li>')
    body.extend(['</ul>',
        '<p>Reviewed on ' + data['review_date'] + '. The Class X Employability Skills PDF supplies Part A detail; the IT-402 PDF supplies the 15 subject-specific chapters. The detailed current safety chapters and unit table take precedence over the stale “Web Applications” overview label in the IT PDF. The Part A ICT-I typo in that overview is resolved using the separate Class X ICT-II syllabus.</p>',
        '<h2>What was changed</h2><p>Replaced standalone break-even, electricity-consumption arithmetic, advanced SQL/null-count semantics, standalone mixed-cell-reference drills and unsupported cyber-protocol trivia. Added explicitly listed coverage such as writing skills, Writer style families and templates, macro cell access/sorting, registered data, Base wizards and workplace monitoring. Safety answers keep assistance within training and authority.</p>',
        '<p>The published Part A allocation of 2/3/1/3/1 marks is restored in the syllabus guide. Earlier audit wording had incorrectly treated that published allocation as unsupported. It is still not a promise of particular recurring questions.</p>',
        '<h2>How the review works</h2><p>Reviewed source questions and scenario packs carry explicit outcome references and content fingerprints. Reference IDs such as B1 are local labels for the cited official topics, not codes published by CBSE. Generated variants inherit the references for their assessed topics and any paired cases or distractors. Every rendered item is listed in the downloadable manifest. A changed prompt, option, answer or source pack fails the build until its review record is deliberately updated.</p>',
        '<p><a class="button" href="docs/question-syllabus-audit.csv" download>Download every-question audit (CSV)</a> <a href="content/practice/audit-changes.json">Inspect source replacements</a></p>',
        '<p class="warning">A fingerprint check detects changes; it does not independently judge educational correctness. Long Part A answers practise the same prescribed topics in a longer format, not a claimed four-mark board-paper pattern. Competitive-style means syllabus-based reasoning, not an external competition syllabus. The historical SQP library, legacy notes and mixed-revision archive are separate resources and are not included in this 4,400-item mapping review.</p>',
        '<h2>Chapter coverage</h2><table><tr><th>Chapter</th><th>MCQ</th><th>Short</th><th>Long</th><th>Application</th><th>Competitive</th></tr>'])
    for c in CHAPTERS:
        body.append(f'<tr><td><a href="practice/{c[0]}.html">{escape(c[2])}</a></td>' + ''.join(f'<td>{len(qs)}</td>' for qs in bank[c[0]].values()) + '</tr>')
    body.append('</table><h2>Published topic references</h2>')
    for ref, item in data['outcomes'].items():
        source = data['sources'][item['source']]
        body.append(f'<section class="card syllabus-topic" id="{ref}"><h3>{escape(ref)} · {escape(item["title"])}</h3><p>{escape(item["scope"])}</p><p><a href="{source["url"]}#page={item["page"]}">{escape(source["short"])} · page {item["page"]}</a></p></section>')
    return page('Syllabus audit · Class X IT-402', 'Question-level traceability to the official 2026-27 CBSE Class X IT-402 and Employability Skills curricula', 'question-bank.html', '\n'.join(body))


def write_audit(bank):
    (ROOT / 'docs/question-syllabus-audit.csv').write_text(audit_csv(bank), encoding='utf-8')
    (ROOT / 'syllabus-audit.html').write_text(render_audit(bank), encoding='utf-8')
