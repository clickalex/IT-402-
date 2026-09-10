"""Optional real-browser regression suite.

Install Playwright and Chromium in a development environment, start the static
site server, then run: python3 tests/browser_practice.py
BASE_URL defaults to http://127.0.0.1:8000. CHROMIUM_EXECUTABLE optionally selects
an existing browser. No browser or Python dependency is shipped to students.
"""
import os
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright, expect

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from tpl import CHAPTERS
from practice import load_bank, TYPES
from hub_practice import HUBS, hub_chapters

BASE = os.environ.get('BASE_URL', 'http://127.0.0.1:8000').rstrip('/')
BANK = load_bank()

with sync_playwright() as p:
    launch = dict(headless=True)
    if os.environ.get('CHROMIUM_EXECUTABLE'):
        launch['executable_path'] = os.environ['CHROMIUM_EXECUTABLE']
        launch['args'] = ['--no-sandbox', '--disable-dev-shm-usage', '--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader']
    browser = p.chromium.launch(**launch)
    context = browser.new_context(viewport={'width': 1280, 'height': 900}, reduced_motion='reduce')
    page = context.new_page()
    failures = []
    page.on('pageerror', lambda error: failures.append(str(error)))
    page.on('response', lambda response: failures.append(f'HTTP {response.status}: {response.url}') if response.status >= 400 else None)
    for c in CHAPTERS:
        cid = c[0]
        # Every directory choice must open a distinct real page, not a filter.
        page.goto(BASE + '/question-bank.html')
        page.locator('#practice-chapter').select_option(cid)
        page.locator('[data-practice-navigation] button').click()
        expect(page).to_have_url(BASE + f'/practice/{cid}.html')
        expect(page.locator('.practice-question')).to_have_count(220)
        expect(page.locator('.practice-question:visible')).to_have_count(220)
        expect(page.locator('[data-question-filter] option[value="all"]')).to_have_text('All questions (220)')
        expect(page.locator('.syllabus-reference')).to_have_count(220)
        expect(page.locator('[data-question-status]')).to_contain_text('220 of 220')
        expect(page.locator('.answer-reveal[open]')).to_have_count(0)
        radio = page.locator('.practice-question input[type=radio]').first
        radio.check()
        expect(radio).to_be_checked()
        expect(page.locator('.answer-reveal[open]')).to_have_count(0)
        for kind, _ in TYPES:
            page.locator('[data-question-filter]').select_option(kind)
            expect(page.locator('.practice-question:visible')).to_have_count(60 if kind == 'mcq' else 40)
            expect(page.locator('[data-question-status]')).to_contain_text(f'{60 if kind == "mcq" else 40} of 220')
            question = page.locator(f'#{kind}-1')
            answer = question.locator('.model-answer')
            expect(answer).to_be_hidden()
            summary = question.locator('summary')
            summary.focus()
            summary.press('Enter')
            expect(answer).to_be_visible()
            expect(summary).to_contain_text('Hide answer')
            summary.press('Enter')
            expect(answer).to_be_hidden()
            # Include a newly expanded item, not only the preserved originals.
            last = page.locator(f'#{kind}-{60 if kind == "mcq" else 40}')
            last.locator('summary').click()
            expect(last.locator('.model-answer')).to_be_visible()
            expect(last.locator('.model-answer')).to_contain_text(BANK[cid][kind][-1]['answer'])
            last.locator('summary').click()
        page.locator('[data-question-filter]').select_option('all')
        expect(page.locator('.practice-question:visible')).to_have_count(220)
        page.locator('.mcq-batches a[href="#mcq-51"]').click()
        expect(page.locator('#mcq-51')).to_be_visible()
        expect(page.locator('.practice-question:visible')).to_have_count(60)
        page.locator('.practice-types a[href="#short"]').click()
        expect(page.locator('.practice-question:visible')).to_have_count(40)
        expect(page.locator('#short-1')).to_be_visible()
        page.locator('[data-question-filter]').select_option('all')
        page.locator('#mcq-1 summary').click()
        page.locator('[data-hide-answers]').click()
        expect(page.locator('.answer-reveal[open]')).to_have_count(0)
        # Legacy bookmarked query URLs must be routed too.
        page.goto(BASE + f'/question-bank.html?chapter={cid}#quiz')
        expect(page).to_have_url(BASE + f'/practice/{cid}.html')
    # Hash URLs must reveal a destination even when only one type is displayed.
    page.goto(BASE + '/practice/u1-ch1.html#competitive-40')
    expect(page.locator('[data-question-filter]')).to_have_value('competitive')
    expect(page.locator('#competitive-40')).to_be_visible()
    expect(page.locator('.practice-question:visible')).to_have_count(40)
    page.locator('#competitive-40 summary').click()
    page.locator('[data-question-filter]').select_option('mcq')
    page.locator('[data-hide-answers]').click()
    expect(page.locator('.answer-reveal[open]')).to_have_count(0)
    # Picker on a practice page must resolve from the nested folder.
    page.locator('#practice-chapter').select_option('u1-ch1')
    page.locator('[data-practice-navigation] button').click()
    expect(page).to_have_url(BASE + '/practice/u1-ch1.html')
    page.locator('#siteSearch').fill('Goal Seek')
    expect(page.locator('#searchResults a[href="../chapters/u2-ch4-scenarios-goal-seek.html"]')).to_be_visible()
    page.goto(BASE + '/question-bank.html?chapter=not-a-chapter')
    expect(page.locator('#practice-navigation-status')).to_contain_text('Choose a valid chapter')
    for hub in HUBS:
        page.goto(BASE + '/' + hub)
        cid = hub_chapters(hub)[-1][0]
        page.locator('[data-practice-navigation] select').select_option(cid)
        page.locator('[data-practice-navigation] button').click()
        expect(page).to_have_url(BASE + f'/practice/{cid}.html')
    # Published question references lead to real topic evidence, not an empty audit.
    page.goto(BASE + '/practice/pa-u1.html')
    page.locator('#mcq-1 .syllabus-reference a').first.click()
    expect(page).to_have_url(BASE + '/syllabus-audit.html#A1-feedback')
    expect(page.locator('#A1-feedback')).to_be_visible()
    expect(page.locator('table tr')).to_have_count(21)
    with page.expect_download() as info:
        page.locator('a[download]').click()
    assert info.value.suggested_filename == 'question-syllabus-audit.csv'
    assert info.value.failure() is None
    # Narrow-screen and dark-theme overflow checks for every question page.
    page.set_viewport_size({'width': 360, 'height': 800})
    for c in CHAPTERS:
        page.goto(BASE + f'/practice/{c[0]}.html')
        if not page.locator('body').evaluate("e=>e.classList.contains('dark')"):
            page.locator('.theme-btn').click()
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), c[0]
        page.locator('#mcq-60 summary').click()
        expect(page.locator('#mcq-60 .model-answer')).to_be_visible()
        assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'), c[0]
    page.goto(BASE + '/question-bank.html')
    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
    page.goto(BASE + '/syllabus-audit.html')
    assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
    # No-JS + file:// proves answers and direct links work without a server/network.
    offline = browser.new_context(java_script_enabled=False, viewport={'width': 360, 'height': 800}, reduced_motion='reduce')
    off = offline.new_page()
    for c in CHAPTERS:
        off.goto((ROOT / 'practice' / f'{c[0]}.html').as_uri())
        expect(off.locator('.answer-reveal[open]')).to_have_count(0)
        expect(off.locator('.practice-question:visible')).to_have_count(220)
        expect(off.locator('[data-question-controls]')).to_be_hidden()
        off.locator('#long-1 summary').click()
        expect(off.locator('#long-1 .model-answer')).to_be_visible()
        off.locator('#long-1 summary').click()
        expect(off.locator('#long-1 .model-answer')).to_be_hidden()
    off.goto((ROOT / 'question-bank.html').as_uri())
    off.locator('a.button[href="practice/u1-ch1.html"]').click()
    expect(off).to_have_url((ROOT / 'practice/u1-ch1.html').as_uri())
    assert not failures, failures
    browser.close()
print('PASS: 20 chapters × 220 questions; 60/40/40/40/40 filtering; new and original hidden answers; keyboard toggles; batch/type jumps; hash routes; hide-all; hub selection; nested search; mobile/dark layout; 220 offline no-JS questions per chapter.')
