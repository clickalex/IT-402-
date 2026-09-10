"""Reviewed curriculum traceability. A changed source needs an explicit new review.

Fingerprint checks prevent silent content drift; they are NOT an automated proof
of educational correctness. Outcome mapping was made against the cited curricula.
"""
import csv
import hashlib
import io
import json
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
