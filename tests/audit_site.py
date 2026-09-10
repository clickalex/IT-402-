"""Static generated-site audit: python3 tests/audit_site.py."""
import sys
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote, parse_qs
from collections import Counter
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from quiz import QUIZZES, QUIZ_CHAPTERS
from trend_practice import PRACTICE
from tpl import CHAPTERS
from quiz import PYQ_ANCHOR
from hub_practice import HUBS, hub_chapters, render_hub

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.questions, self.tags = [], [], [], []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        self.tags.append((tag, d))
        if 'id' in d: self.ids.append(d['id'])
        for key in ('href', 'src', 'action', 'data-page'):
            if key in d: self.links.append(d[key])
        if 'quiz-question' in d.get('class', '').split():
            self.questions.append(d.get('data-answer'))

files = sorted(ROOT.glob('*.html')) + sorted((ROOT / 'chapters').glob('*.html')) + sorted((ROOT / 'practice').glob('*.html'))
pages = {p.resolve(): Page(p.read_text()) for p in files}
errors, links = [], 0
for path, page in pages.items():
    for ident, count in Counter(page.ids).items():
        if count > 1: errors.append(f'{path.name}: duplicate id {ident}')
    for link in page.links:
        u = urlsplit(link)
        if u.scheme or u.netloc: continue
        links += 1
        target = (path.parent / unquote(u.path)).resolve() if u.path else path
        if target.name == 'question-bank.html' and u.query:
            values = parse_qs(u.query).get('chapter', [])
            if len(values) != 1 or values[0] not in set(PRACTICE) | {'all'}:
                errors.append(f'{path.name}: invalid chapter filter {link}')
        if not target.exists(): errors.append(f'{path.name}: missing {link}')
        elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:
            errors.append(f'{path.name}: missing fragment {link}')
assert set(PRACTICE) == {c[0] for c in CHAPTERS}
assert len(QUIZ_CHAPTERS) == len(QUIZZES)
assert set(cid for group in QUIZ_CHAPTERS for cid in group) == set(PRACTICE)
for (_, qs), chapter_ids in zip(QUIZZES, QUIZ_CHAPTERS):
    assert len(qs) == len(chapter_ids)
bank_text = (ROOT / 'mixed-practice.html').read_text()
assert bank_text.count('data-chapter=') == 70
assert bank_text.count('<option value=') == 21
assert 'id="chapter-select"' in bank_text
assert len(QUIZZES) == 5 and sum(len(q) for _, q in QUIZZES) == 50
for title, questions in QUIZZES:
    assert len(questions) == 10, title
    for q, opts, ans in questions:
        assert len(opts) == len(set(opts)) == 4 and opts.count(ans) == 1, q
bank = pages[(ROOT / 'mixed-practice.html').resolve()]
assert len(bank.questions) == 50
assert bank.questions == [ans for _, qs in QUIZZES for _, _, ans in qs]
for c in CHAPTERS:
    assert 'trend-practice' in pages[(ROOT / 'chapters' / c[1]).resolve()].ids
assert (ROOT / 'mixed-practice.html').read_text().count('Model marking points') == 20
pyq = (ROOT / 'pyq.html').read_text()
assert pyq.count('class="qa"') == 101 and pyq.count('class="ans"') == 57
for e in errors: print(e)
print(f'{len(pages)} pages; {links} local references; {len(errors)} errors; 50 MCQs and 20 chapter prompts checked')

# Every hub must expose exactly its own chapters, with accessible GET selectors.
from hubs2 import PARTA, UNIT1, UNIT2, UNIT3, UNIT4
covered = []
for (hub, (select_id, _, _, prefix)), body in zip(HUBS.items(), [PARTA, UNIT1, UNIT2, UNIT3, UNIT4]):
    text = (ROOT / hub).read_text()
    parsed = pages[(ROOT / hub).resolve()]
    chapters = hub_chapters(hub)
    ids = [c[0] for c in chapters]
    covered.extend(ids)
    assert render_hub(body, hub) in text, f'{hub}: generated body is stale'
    assert '{{practice:' not in text and '{{unit_practice}}' not in text
    forms = [d for tag, d in parsed.tags if tag == 'form']
    assert len(forms) == 1 and forms[0]['action'] == 'question-bank.html'
    assert forms[0]['method'] == 'get'
    selects = [d for tag, d in parsed.tags if tag == 'select']
    assert len(selects) == 1 and selects[0]['id'] == select_id
    assert selects[0]['name'] == 'chapter'
    assert 'required' in selects[0]
    assert any(tag == 'label' and d.get('for') == select_id for tag, d in parsed.tags)
    assert any(tag == 'button' and d.get('type') == 'submit' for tag, d in parsed.tags)
    assert [d['value'] for tag, d in parsed.tags if tag == 'option' and d.get('value')] == ids
    progress = [d for tag, d in parsed.tags if 'data-unit' in d]
    assert len(progress) == 1 and progress[0]['data-unit'] == prefix
    assert int(progress[0]['data-total']) == len(ids)
    practice = [link for link in parsed.links if link.startswith('practice/')]
    sqps = [link for link in parsed.links if link.startswith('pyq.html#C-')]
    assert Counter(practice) == Counter({f'practice/{cid}.html': 2 for cid in ids})
    assert sqps == [f'pyq.html#{PYQ_ANCHOR[cid]}' for cid in ids]
    for c in chapters:
        assert f'chapters/{c[1]}' in parsed.links
    assert any(tag == 'noscript' for tag, _ in parsed.tags)
    assert 'without JavaScript' in text and 'separate page' in text
    assert 'Hot Qs:' not in text
assert covered == [c[0] for c in CHAPTERS]
print('All five hubs: 20 options, study/practice/SQP links, progress, accessibility and regeneration checked')

# Guard against the unsupported fixed Part A allocations removed in this pass.
source = (ROOT / 'content/source/Part-A-Deep-Chapters.md').read_text()
for claim in ('Fixed 1–2 questions every year', 'highest in Part A', '1 fixed marker', 'Only 1 mark'):
    assert claim not in source
assert 'publishes the Part A allocation as 2/3/1/3/1' in (ROOT / 'syllabus.html').read_text()

# The new bank is a directory, not an all-chapters quiz dump.
from practice import load_bank, counts, TYPES, render_chapter, render_directory
expanded = load_bank()
original = load_bank(expand=False)
totals = counts(expanded)
assert totals == {'mcq': 1200, 'short': 800, 'long': 800, 'application': 800, 'competitive': 800}
assert sum(totals.values()) == 4400
directory = (ROOT / 'question-bank.html').read_text()
assert directory == render_directory(expanded)
assert 'class="practice-question"' not in directory
assert len(list((ROOT / 'practice').glob('*.html'))) == 20
answer_positions = set()
for c in CHAPTERS:
    cid = c[0]
    text = (ROOT / 'practice' / f'{cid}.html').read_text()
    assert text == render_chapter(c, expanded), f'{cid}: stale generated page'
    parsed = pages[(ROOT / 'practice' / f'{cid}.html').resolve()]
    questions = expanded[cid]
    question_tags = [d for tag, d in parsed.tags if 'data-question-type' in d]
    assert Counter(d['data-question-type'] for d in question_tags) == {kind: len(questions[kind]) for kind, _ in TYPES}
    reveals = [d for tag, d in parsed.tags if tag == 'details' and 'answer-reveal' in d.get('class', '').split()]
    assert len(reveals) == sum(len(group) for group in questions.values())
    assert all('open' not in d for d in reveals), f'{cid}: answer exposed by default'
    options = [d for tag, d in parsed.tags if tag == 'option' and d.get('data-page')]
    assert [d['value'] for d in options] == [chapter[0] for chapter in CHAPTERS]
    assert [d['value'] for d in options if 'selected' in d] == [cid]
    assert all(d['data-page'] == f'../practice/{d["value"]}.html' for d in options)
    assert f'../chapters/{c[1]}' in parsed.links
    assert f'../pyq.html#{PYQ_ANCHOR[cid]}' in parsed.links
    assert f'../practice/{cid}.html' in pages[(ROOT / 'chapters' / c[1]).resolve()].links
    for kind, _ in TYPES:
        assert kind in parsed.ids and len(questions[kind]) == (60 if kind == 'mcq' else 40)
        assert questions[kind][:len(original[cid][kind])] == original[cid][kind]
    assert sum(map(len, questions.values())) == 220
    assert len({q['question'].casefold().strip() for group in questions.values() for q in group}) == 220
    for start in range(1, 61, 10):
        assert f'#mcq-{start}' in parsed.links
    assert 'question-type' in parsed.ids
    assert 'All questions (220)' in text and '{total}' not in text
    for q in questions['mcq']:
        assert len(set(q['options'])) == 4 and q['options'].count(q['answer']) == 1
        answer_positions.add(q['options'].index(q['answer']))
    radios = [d for tag, d in parsed.tags if tag == 'input' and d.get('type') == 'radio']
    assert len(radios) == len(questions['mcq']) * 4
    assert set(Counter(d['name'] for d in radios).values()) == {4}
    assert all('checked' not in d for d in radios)
assert answer_positions == {0, 1, 2, 3}
print(f'20 separate question pages: {dict(totals)}; directory, chapter routes, radio groups and closed answers checked')

# Every current item is traceable to reviewed source content and an official scope.
import csv, io, re
from syllabus_review import registry, approve, audit_csv, render_audit, fingerprint, validate_expansion_engine
review = registry()
assert len(review['reviews']) == 710
assert review['session'] == '2026-2027'
assert b'\r' not in (ROOT / 'docs/question-syllabus-audit.csv').read_bytes(), 'Generated CSV must use LF line endings'
manifest = (ROOT / 'docs/question-syllabus-audit.csv').read_text()
# CSV newline conventions are normalised by read_text.
assert manifest == audit_csv(expanded).replace('\r\n', '\n')
rows = list(csv.DictReader(io.StringIO(manifest)))
assert len(rows) == 4400 and len({r['question_id'] for r in rows}) == 4400
assert (ROOT / 'syllabus-audit.html').read_text() == render_audit(expanded)
by_id = {row['question_id']: row for row in rows}
for cid, groups in expanded.items():
    for kind, questions in groups.items():
        for n, q in enumerate(questions, 1):
            row = by_id[f'{cid}/{kind}-{n}']
            assert row['content_sha256'] == fingerprint(q)
            assert row['outcomes'].split(';') == q['syllabus']
            assert all(ref in review['outcomes'] for ref in q['syllabus'])
            assert all(key in review['reviews'] for key in q['review_keys'])
            inherited = list(dict.fromkeys(ref for key in q['review_keys'] for ref in review['reviews'][key]['outcomes']))
            assert q['syllabus'] == inherited
            text = ' '.join([q['question'], q['answer']] + q.get('options', []))
            assert not re.search(r'\bSQL\b|\bHTTPS\b|\bMFA\b|break.even|cash.flow|\bkWh\b|\bphishing\b|\$[A-Z]\$?\d', text, re.I), (cid, kind, n)
            for ref in q['syllabus']:
                assert ref in pages[(ROOT / 'syllabus-audit.html').resolve()].ids
# Negative checks: unknown or altered sources must not silently self-approve.
from practice import read_rows
sample = read_rows('mcqs.txt', 6)['pa-u1'][0]
assert approve('mcq:pa-u1:1', sample)['syllabus']
for key, fields in [('mcq:pa-u1:unknown', sample), ('mcq:pa-u1:1', sample[:-1] + ['Unreviewed replacement answer'])]:
    try:
        approve(key, fields)
    except ValueError:
        pass
    else:
        raise AssertionError('Syllabus review gate accepted missing/stale evidence')
from unittest.mock import patch
with patch.dict(review, {'expansion_engine_sha256': '0' * 64}):
    try:
        validate_expansion_engine()
    except ValueError:
        pass
    else:
        raise AssertionError('Unreviewed expansion-engine change was accepted')
with patch.dict(review['reviews']['mcq:pa-u1:1'], {'decision': 'pending'}):
    try:
        approve('mcq:pa-u1:1', sample)
    except ValueError:
        pass
    else:
        raise AssertionError('Pending source review was accepted')
print('Syllabus traceability: 710 reviewed sources; 4,400 manifest rows; all mappings and fingerprints checked; stale-source negative tests passed')

sys.exit(bool(errors))
