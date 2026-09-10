"""Static generated-site audit: python3 tests/audit_site.py."""
import sys
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
from collections import Counter
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from quiz import QUIZZES, QUIZ_CHAPTERS
from trend_practice import PRACTICE
from tpl import CHAPTERS

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids, self.links, self.questions = [], [], []
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if 'id' in d: self.ids.append(d['id'])
        for key in ('href', 'src'):
            if key in d: self.links.append(d[key])
        if 'quiz-question' in d.get('class', '').split():
            self.questions.append(d.get('data-answer'))

files = sorted(ROOT.glob('*.html')) + sorted((ROOT / 'chapters').glob('*.html'))
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
        if not target.exists(): errors.append(f'{path.name}: missing {link}')
        elif u.fragment and target in pages and unquote(u.fragment) not in pages[target].ids:
            errors.append(f'{path.name}: missing fragment {link}')
assert set(PRACTICE) == {c[0] for c in CHAPTERS}
assert len(QUIZ_CHAPTERS) == len(QUIZZES)
assert set(cid for group in QUIZ_CHAPTERS for cid in group) == set(PRACTICE)
for (_, qs), chapter_ids in zip(QUIZZES, QUIZ_CHAPTERS):
    assert len(qs) == len(chapter_ids)
bank_text = (ROOT / 'question-bank.html').read_text()
assert bank_text.count('data-chapter=') == 70
assert bank_text.count('<option value=') == 21
assert 'id="chapter-select"' in bank_text
assert len(QUIZZES) == 5 and sum(len(q) for _, q in QUIZZES) == 50
for title, questions in QUIZZES:
    assert len(questions) == 10, title
    for q, opts, ans in questions:
        assert len(opts) == len(set(opts)) == 4 and opts.count(ans) == 1, q
bank = pages[(ROOT / 'question-bank.html').resolve()]
assert len(bank.questions) == 50
assert bank.questions == [ans for _, qs in QUIZZES for _, _, ans in qs]
for c in CHAPTERS:
    assert 'trend-practice' in pages[(ROOT / 'chapters' / c[1]).resolve()].ids
assert (ROOT / 'question-bank.html').read_text().count('Model marking points') == 20
pyq = (ROOT / 'pyq.html').read_text()
assert pyq.count('class="qa"') == 101 and pyq.count('class="ans"') == 57
for e in errors: print(e)
print(f'{len(pages)} pages; {links} local references; {len(errors)} errors; 50 MCQs and 20 chapter prompts checked')

# Part A selector must reach all five valid question-bank filters.
part_a = (ROOT / 'part-a.html').read_text()
assert 'action="question-bank.html#quiz" method="get"' in part_a
assert 'id="part-a-unit" name="chapter"' in part_a
for i in range(1, 6):
    assert f'<option value="pa-u{i}">' in part_a
    assert f'question-bank.html?chapter=pa-u{i}#quiz' in part_a
    assert f'pyq.html#C-U{i}' in part_a
print('Part A: five selector options and practice/SQP links checked')

sys.exit(bool(errors))
