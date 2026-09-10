"""Original practice inspired by the SQP topic review, not official PYQ text."""
from html import escape

# chapter id: (prompt, marks, model marking points)
PRACTICE = {
'pa-u1': ('A manager uses unfamiliar abbreviations in instructions. Identify the barrier and suggest a remedy.', 2, 'Linguistic/language barrier (1). Replace abbreviations with familiar words or explain their meaning (1).'),
'pa-u2': ('Turn “I will study Calc” into a SMART goal and explain how progress is measured.', 2, 'Example: Complete 15 Calc questions by Saturday at 6 pm, allowing 30 minutes daily (1). Count completed and checked questions against the target of 15 (1).'),
'pa-u3': ('Give two measures to protect a computer against data loss.', 2, 'Keep regular backups on a separate device or trusted backup service (1). Use updated antivirus software and security updates to reduce malware risk (1).'),
'pa-u4': ('Respond to the claim “Entrepreneurs are born, not made” with two points.', 2, 'Entrepreneurial skills can be learned through education and training (1). Experience and practice develop planning, decision-making and risk-management skills (1).'),
'pa-u5': ('Suggest two school actions supporting sustainable development.', 2, 'Reduce paper use through digital notices or double-sided printing (1). Conserve energy by switching off unused lights and computers (1). Accept other valid actions with a clear benefit.'),
'u1-ch1': ('A report has 40 headings formatted manually. Explain a better method and its benefits.', 4, 'Apply the appropriate heading paragraph styles (1). Modify the style to change all matching headings consistently (1). Use character styles for selected text rather than whole paragraphs (1). Heading structure supports an automatic table of contents (1).'),
'u1-ch2': ('Explain anchor versus wrap, then explain cropping and one risk of linked images.', 4, 'Anchor determines what an image is attached to (1). Wrap determines how surrounding text flows (1). Cropping removes unwanted outer portions from view (1). Moving or deleting a linked source image can break its display (1).'),
'u1-ch3': ('An automatic ToC is empty although titles look bold. Give a fix and a later maintenance step.', 2, 'Apply heading paragraph styles to titles so the ToC can detect their outline structure (1). Update the ToC after changing headings or pagination (1).'),
'u2-ch4': ('Choose and explain tools for finding one required input, comparing input sets, optimising with constraints and combining sheet totals.', 4, 'Goal Seek finds one input for a target formula result (1). Scenarios compare saved sets of inputs (1). Solver optimises an objective using variables and constraints (1). Consolidate combines data from ranges or sheets (1).'),
'u2-ch5': ('A clerk repeats the same spreadsheet formatting daily. Suggest a feature and one security precaution.', 2, 'Use a macro to automate the repeated sequence (1). Run macros only from trusted sources; do not enable an unknown document macro (1).'),
'u2-ch6': ('Distinguish relative and absolute hyperlinks and explain what happens when a project folder moves.', 4, 'A relative link specifies the target relative to the source location (1). An absolute link specifies the full destination address (1). Moving source and target together while preserving their relative layout can keep a relative link working (1). An absolute file link can break when its target moves away from its stored path (1).'),
'u2-ch7': ('Distinguish spreadsheet sharing from recording changes.', 2, 'Sharing allows multiple users to collaborate on a spreadsheet (1). Recording changes logs supported edits for review and acceptance or rejection; it is not the same as enabling sharing (1).'),
'u3-ch8': ('In a school database, define primary key and foreign key with examples.', 2, 'StudentID uniquely identifies each student in STUDENT, so it can be its primary key (1). ClassID in STUDENT references the key in CLASS and can be a foreign key (1).'),
'u3-ch9': ('Contrast Entry Required and Default Value using a student table.', 2, 'Entry Required set to Yes prevents a missing value, e.g. for StudentName (1). Default Value supplies an initial value, e.g. City set to Delhi, which can be changed (1).'),
'u3-ch10': ('Explain a class-to-students relationship, referential integrity and two cascade actions.', 4, 'One class can have many students: one-to-many (1). Referential integrity prevents a non-null student ClassID from referring to a nonexistent class key (1). Update cascade propagates changes to referenced keys (1). Delete cascade removes related child records when the parent is deleted; use cautiously (1).'),
'u3-ch11': ('For STUDENT(StudentID, Name, Marks), write SQL to show names and marks of students scoring at least 75, highest score first.', 2, 'SELECT Name, Marks FROM STUDENT WHERE Marks >= 75 ORDER BY Marks DESC; Award 1 for correct selected columns and filter, 1 for descending order.'),
'u3-ch12': ('Choose a database object for entering student records and another for a printable summary. Explain each.', 2, 'A form provides a user-friendly interface for entering or editing records (1). A report formats retrieved data into a structured presentation suitable for printing (1).'),
'u4-ch13': ('A corridor has a spill beside a damaged power cable. Give two safe actions.', 2, 'Keep people away and report or secure the hazardous area according to workplace procedure (1). Have the electrical supply isolated safely by an authorised person; do not touch exposed conductors or approach with water (1).'),
'u4-ch14': ('Suggest four ways to reduce strain during computer work.', 4, 'Use an adjustable supportive chair and neutral posture (1). Position the screen at a comfortable distance and height (1). Reduce glare and ensure suitable lighting (1). Take regular breaks, including looking away from the screen (1).'),
'u4-ch15': ('Give two safe actions after a workplace fire alarm.', 2, 'Follow the evacuation plan using a safe exit or stairs, not lifts (1). Go to the assembly point for headcount and do not re-enter until authorised (1).'),
}

NOTICE = ('Original trend-informed practice, not official CBSE questions or predictions. '
          'Based on the 2019–26 SQP review; older syllabuses are filtered. '
          'Safety priorities use the recent papers. Study every current chapter.')

def chapter_practice(cid):
    q, marks, answer = PRACTICE[cid]
    return (f'<h2 class="section-title" id="trend-practice">Trend-informed practice</h2>'
            f'<p>{NOTICE} <a href="../pyq.html">Review source evidence →</a></p>'
            f'<div class="qa"><strong>{escape(q)} ({marks} marks)</strong>'
            f'<details><summary>Model marking points</summary><p>{escape(answer)}</p></details></div>')

def bank_practice():
    rows = ['<h2 class="section-title" id="trend-practice">Trend-informed written practice — 20 questions</h2>',
            f'<p>{NOTICE} <a href="pyq.html">Review source evidence →</a></p>']
    for i, (cid, (q, marks, ans)) in enumerate(PRACTICE.items(), 1):
        rows.append(f'<div class="qa" data-chapter="{cid}"><strong>T{i}. {escape(q)} ({marks} marks)</strong>'
                    f'<details><summary>Model marking points</summary><p>{escape(ans)}</p></details></div>')
    return '\n'.join(rows)

# Four additional original case/concept MCQs per unit. Existing quizzes remain intact.
MCQS = [
[
('Instructions contain unexplained technical abbreviations. Which barrier is most relevant?', ['Physical', 'Linguistic', 'Financial', 'Environmental'], 'Linguistic'),
('Which goal has a measurable target and deadline?', ['Study harder', 'Become successful', 'Complete 12 checked questions by Friday', 'Read when free'], 'Complete 12 checked questions by Friday'),
('Which statement about entrepreneurship is a myth?', ['Skills can be learned', 'Planning helps', 'All entrepreneurs are born with every necessary skill', 'Risk can be managed'], 'All entrepreneurs are born with every necessary skill'),
('Which school action best conserves resources?', ['Print every email', 'Leave idle PCs running', 'Replace working devices weekly', 'Reuse paper and switch off unused equipment'], 'Reuse paper and switch off unused equipment'),
], [
('A publisher must change every chapter heading consistently. What should be modified?', ['Each space', 'The shared heading style', 'Every image', 'The status bar'], 'The shared heading style'),
('An image must lose unwanted outer edges. Choose the operation.', ['Crop', 'Anchor', 'Wrap', 'Arrange'], 'Crop'),
('Which setting determines how text flows beside a picture?', ['Image filename', 'Page count', 'Text wrapping', 'Spellcheck'], 'Text wrapping'),
('A reusable starting document containing standard formatting is a…', ['Comment', 'Template', 'Database key', 'Query'], 'Template'),
], [
('Which tool compares saved sets of spreadsheet input values?', ['Scenarios', 'Spellcheck', 'Track Changes', 'AutoCorrect'], 'Scenarios'),
('An objective must be maximised with several adjustable cells and constraints. Use…', ['Goal Seek', 'Sort', 'Solver', 'Find'], 'Solver'),
('A clerk repeats the same sequence of spreadsheet operations daily. Use…', ['A footer', 'A macro', 'A report', 'An anchor'], 'A macro'),
('A reviewer needs to inspect logged spreadsheet edits. Which feature is relevant?', ['Consolidate', 'Page style', 'Track Changes', 'Crop'], 'Track Changes'),
], [
('Which field property prevents a missing entry?', ['Default Value alone', 'Font Size', 'Entry Required set to Yes', 'Column Width'], 'Entry Required set to Yes'),
('A child record refers to a nonexistent parent key. Which rule should prevent this?', ['Text wrapping', 'Referential integrity', 'Page numbering', 'Image transparency'], 'Referential integrity'),
('Which SQL clause filters rows to Marks >= 75?', ['ORDER BY Name', 'WHERE Marks >= 75', 'SELECT ALL TABLES', 'GROUP EVERY ROW'], 'WHERE Marks >= 75'),
('Which database object is intended for a formatted printable summary?', ['Report', 'Macro recorder', 'Cell style', 'Slide transition'], 'Report'),
], [
('Which is an ergonomic risk?', ['Neutral posture', 'Supported back', 'Repeated work with a bent wrist', 'Regular breaks'], 'Repeated work with a bent wrist'),
('You notice exposed electrical wiring. What is the safe response?', ['Touch it to test', 'Pour water', 'Ignore it', 'Keep clear and report for safe isolation'], 'Keep clear and report for safe isolation'),
('After evacuating, where should employees go?', ['Back to their desks', 'The designated assembly point', 'A lift', 'A locked storeroom'], 'The designated assembly point'),
('Which action helps reduce screen-related eye strain?', ['Remove all lighting', 'Stare without breaks', 'Increase glare', 'Take regular breaks and reduce glare'], 'Take regular breaks and reduce glare'),
],
]
