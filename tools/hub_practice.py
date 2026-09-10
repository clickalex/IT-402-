"""Shared unit-hub navigation, using the same chapter IDs as the question bank."""
from html import escape
from tpl import CHAPTERS
from quiz import PYQ_ANCHOR
from practice import chapter_picker

# Chapter membership, titles and destinations come from tpl.CHAPTERS, not copies.
HUBS = {
    'part-a.html': ('part-a-unit', 'Part A', 'Employability unit', 'pa-u'),
    'unit1-writer.html': ('unit1-chapter', 'Unit 1 · Writer', 'Writer chapter', 'u1-ch'),
    'unit2-calc.html': ('unit2-chapter', 'Unit 2 · Calc', 'Calc chapter', 'u2-ch'),
    'unit3-dbms.html': ('unit3-chapter', 'Unit 3 · DBMS', 'DBMS chapter', 'u3-ch'),
    'unit4-safety.html': ('unit4-chapter', 'Unit 4 · Safety', 'Safety chapter', 'u4-ch'),
}

PRIORITIES = {
    'unit1-writer.html': 'Choose styles instead of repeated direct formatting; distinguish image anchor from wrap and embedding from linking; build a ToC from headings; reuse templates and review tracked edits.',
    'unit2-calc.html': 'Choose Consolidate, Subtotals, Scenarios, Goal Seek or Solver for the task; record and run trusted macros; distinguish cell references from hyperlinks; share and review changes.',
    'unit3-dbms.html': 'Explain keys and table structure; choose field types; model relationships and referential integrity; apply query criteria; distinguish forms for input from reports for presentation.',
    'unit4-safety.html': 'Identify and report hazards; suggest ergonomic improvements; explain safe evacuation, electrical precautions and when to call trained help. Current safety practice uses recent SQPs, not the old Web Applications unit.',
}


def hub_chapters(hub):
    return [c for c in CHAPTERS if c[4] == hub]


def practice_links(cid):
    return (f'<p class="hub-practice-links"><a href="practice/{cid}.html">'
            f'All chapter questions + MCQs →</a><br><a href="pyq.html#{PYQ_ANCHOR[cid]}">'
            'Official SQP questions →</a></p>')


def practice_panel(hub):
    select_id, title, label, prefix = HUBS[hub]
    chapters = hub_chapters(hub)
    count = len(chapters)
    heading = 'Choose a Part A unit to practise' if hub == 'part-a.html' else f'Choose a {escape(title)} chapter to practise'
    priorities = ''
    if hub in PRIORITIES:
        priorities = (f'<div class="card hub-priorities"><b>Practice priorities:</b> {PRIORITIES[hub]}'
                      '<p>Use the <a href="pyq.html">2019–26 official SQP review</a> as topic evidence, '
                      'not main-board frequency or a prediction. Study every current chapter. '
                      'Older Web Applications and mail-merge questions are not current-syllabus priorities. '
                      'The unit total is not a guaranteed chapter-wise marks split.</p></div>')
    return f'''<section class="card hub-practice" aria-labelledby="hub-practice-title">
<h2 id="hub-practice-title">{heading}</h2>
{chapter_picker(chapters=chapters, select_id=select_id)}
<p id="hub-practice-help">Opens a separate page for the selected chapter/unit, with exactly 220 questions: 60 MCQs and 40 each of short, long, application and competitive-style questions. Answers stay hidden until you choose Show answer. These are original exercises, not official PYQs. Each card below also links directly to its question page, without JavaScript.</p>
<div class="unitbar" data-unit="{prefix}" data-total="{count}"><b>{escape(title)} progress</b>
<div class="progress"><i data-unit-bar></i></div><small data-unit-label>0/{count} chapters</small>
<p><small>Mark complete on the detailed chapter pages. Progress is saved in this browser; the revision checklist below is separate.</small></p></div>
<p><b>Study → practise → review:</b> Read the notes, answer without looking, then compare model points and official SQP answers. Revisit mistakes before marking a chapter complete.</p>
</section>{priorities}'''


def render_hub(body, hub):
    """Expand explicit slots; fail on missing or stale navigation at build time."""
    assert body.count('{{unit_practice}}') == 1, hub
    body = body.replace('{{unit_practice}}', practice_panel(hub))
    for c in hub_chapters(hub):
        token = '{{practice:' + c[0] + '}}'
        assert body.count(token) == 1, (hub, token)
        body = body.replace(token, practice_links(c[0]))
    assert '{{practice:' not in body, hub
    return body
