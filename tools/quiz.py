# Unit-wise interactive quizzes + chapter/hub illustration mapping.

# [(quiz title, [(question, [4 options], correct answer), ...]), ...]
QUIZZES = [
("Quiz 1 · Part A — Employability", [
("Which of the 7 Cs means “to the point, no extra words”?", ["Clear", "Concise", "Concrete", "Courteous"], "Concise"),
("In SMART goals, T stands for…", ["Total", "Tough", "Time-bound", "Tested"], "Time-bound"),
("A file named marks.ods belongs to…", ["LibreOffice Writer", "LibreOffice Calc", "LibreOffice Base", "LibreOffice Draw"], "LibreOffice Calc"),
("An entrepreneur's income is…", ["Fixed salary", "Daily wage", "Uncertain profit or loss", "Monthly pension"], "Uncertain profit or loss"),
("The Brundtland Commission defined…", ["Green jobs", "Sustainable development", "E-waste", "ICT safety"], "Sustainable development"),
("Pressing Win+L on a shared PC will…", ["Open the browser", "Lock the screen", "Shut down", "Refresh"], "Lock the screen"),
]),
("Quiz 2 · Unit 1 — Writer", [
("Which Writer feature supplies structure for an automatic ToC?", ["Bold text", "Heading styles", "Font colour", "Page numbers"], "Heading styles"),
("Which shortcut opens the Styles window?", ["F4", "F11", "Ctrl+K", "Ctrl+S"], "F11"),
("How do you exit Fill Format mode?", ["Press Esc", "Press Enter", "Click Save", "Press F5"], "Press Esc"),
("Which image method keeps the .odt file small?", ["Embed", "Link (stores path only)", "Copy-paste", "Drag-drop"], "Link (stores path only)"),
("A LibreOffice Writer template uses the extension…", [".odt", ".ott", ".ods", ".odb"], ".ott"),
("The shortcut to insert a comment is…", ["Ctrl+K", "Ctrl+Alt+C", "Ctrl+Shift+E", "F4"], "Ctrl+Alt+C"),
]),
("Quiz 3 · Unit 2 — Calc", [
("Which Calc tool finds the input needed for a desired formula result?", ["Sort", "Scenarios", "Goal Seek", "Consolidate"], "Goal Seek"),
("How many variable cells can Goal Seek change?", ["Only one", "Two", "Up to ten", "Unlimited"], "Only one"),
("Before applying Subtotals, data must first be…", ["Filtered", "Sorted by the grouping column", "Printed", "Shared"], "Sorted by the grouping column"),
("Recorded macros are stored under…", ["My Documents", "My Macros", "Templates", "Recycle Bin"], "My Macros"),
("Ctrl+K in Calc inserts a…", ["Function", "Hyperlink", "Comment", "Scenario"], "Hyperlink"),
("Multi-user editing is enabled via…", ["Edit → Track Changes", "Tools → Share Spreadsheet", "Insert → Sheet", "Data → Sort"], "Tools → Share Spreadsheet"),
]),
("Quiz 4 · Unit 3 — DBMS", [
("Which key uniquely identifies each record and cannot be NULL?", ["Foreign key", "Primary key", "Caption", "Index"], "Primary key"),
("Degree and cardinality of a table mean…", ["Rows / Columns", "Columns / Rows", "Keys / Queries", "Forms / Reports"], "Columns / Rows"),
("CLASS–STUDENTS is which relationship type?", ["One-to-One", "One-to-Many", "Many-to-Many", "No relation"], "One-to-Many"),
("A school.odb file is a…", ["Writer document", "Calc sheet", "LibreOffice Base database", "PDF report"], "LibreOffice Base database"),
("In Base criteria, wildcards * and ? match…", ["* one char, ? many", "* many chars, ? exactly one", "Both exactly one", "Both everything"], "* many chars, ? exactly one"),
("On a Base form, Label vs Text Box…", ["Both store data", "Label shows fixed text, Text Box stores input", "Both print only", "Label stores, Text Box shows"], "Label shows fixed text, Text Box stores input"),
]),
("Quiz 5 · Unit 4 — Safety + Mixed", [
("What is the eye-break rule for computer users?", ["50–70", "20-20-20", "90-90-90", "101/102/108"], "20-20-20"),
("In a fire evacuation you should use…", ["The lift (fastest)", "Nearest safe stairs", "Locked exits", "The balcony"], "Nearest safe stairs"),
("First step in an electrical rescue?", ["Touch the victim", "Throw water", "Switch OFF power", "Call a friend"], "Switch OFF power"),
("The screen should be placed…", ["20–30 cm away", "50–70 cm away at eye level", "2 metres away", "Below the desk"], "50–70 cm away at eye level"),
("PASS for fire extinguishers means…", ["Push-Alert-Shout-Save", "Pull-Aim(base)-Squeeze-Sweep", "Phone-Alarm-Switch-Stairs", "Protect-Attend-Send-Stay"], "Pull-Aim(base)-Squeeze-Sweep"),
("Relative hyperlinks are better when…", ["Files never move", "Folders move together", "Using the internet", "Printing"], "Folders move together"),
]),
]

# chapter_id -> (image file, alt text, caption)
CHAPTER_IMG = {
"pa-u1": ("part-a-team.jpg", "Illustration of an office team communicating around a laptop", "Employability in action — clear communication at work."),
"pa-u2": ("part-a-team.jpg", "Illustration of an office team planning work together", "Self-management — plan goals, time and habits."),
"pa-u3": ("part-a-team.jpg", "Illustration of colleagues using computers safely", "ICT skills — organised files and safe computing."),
"pa-u4": ("part-a-team.jpg", "Illustration of a small business team shaking hands", "Entrepreneurship — ideas, plans and customers."),
"pa-u5": ("part-a-team.jpg", "Illustration of a team keeping the workplace green", "Green skills — reduce, reuse, recycle."),
"u1-ch1": ("writer-docs.jpg", "Illustration of a styled document with headings and an image frame", "Writer styles keep long documents consistent."),
"u1-ch2": ("writer-docs.jpg", "Illustration of a document page with an anchored image", "Images + captions + wrap = professional pages."),
"u1-ch3": ("writer-docs.jpg", "Illustration of a long document with a contents list", "ToC, templates and tracked reviews for long reports."),
"u2-ch4": ("calc-sheets.jpg", "Illustration of a spreadsheet with charts and a magnifier", "Calc analysis — compare scenarios, seek goals."),
"u2-ch5": ("calc-sheets.jpg", "Illustration of spreadsheet cells being automated", "Macros replay repetitive work in one click."),
"u2-ch6": ("calc-sheets.jpg", "Illustration of linked spreadsheet sheets", "Link sheets, files and live data together."),
"u2-ch7": ("calc-sheets.jpg", "Illustration of a shared spreadsheet with comments", "Share, comment and merge — teamwork in Calc."),
"u3-ch8": ("dbms-base.jpg", "Illustration of a database connected to three tables", "DBMS — organised data instead of scattered files."),
"u3-ch9": ("dbms-base.jpg", "Illustration of database tables with key icons", "Tables store data; keys identify every row."),
"u3-ch10": ("dbms-base.jpg", "Illustration of three linked database tables", "Relationships connect tables without duplication."),
"u3-ch11": ("dbms-base.jpg", "Illustration of querying connected tables", "Queries ask questions; tables stay unchanged."),
"u3-ch12": ("dbms-base.jpg", "Illustration of data entry screens and printed reports", "Forms enter data; reports present it."),
"u4-ch13": ("safety-lab.jpg", "Illustration of a safe tidy computer lab", "A safe lab — extinguisher, first aid, tidy cables."),
"u4-ch14": ("ergonomics.jpg", "Illustration of perfect sitting posture at a desk", "Ergonomics — eye-level screen, flat feet, straight wrists."),
"u4-ch15": ("fire-safety.jpg", "Illustration of a fire extinguisher and fire triangle", "Fire safety — know the triangle and PASS."),
}

HUB_IMG = {
"part-a.html": ("part-a-team.jpg", "Team communicating in an office", "Part A — the human skills behind every data operator."),
"unit1-writer.html": ("writer-docs.jpg", "Styled document illustration", "Unit 1 — professional documents with Writer."),
"unit2-calc.html": ("calc-sheets.jpg", "Spreadsheet with charts illustration", "Unit 2 — analyse and automate with Calc."),
"unit3-dbms.html": ("dbms-base.jpg", "Connected database tables illustration", "Unit 3 — real databases with Base."),
"unit4-safety.html": ("safety-lab.jpg", "Safe computer lab illustration", "Unit 4 — healthy, safe and secure work."),
"question-bank.html": ("quiz-exam.jpg", "Exam sheet with checkmarks and a timer", "Practise under exam conditions — then check answers."),
"practical.html": ("practical-lab.jpg", "Hands typing on a laptop with files", "Learn by doing — every task on a real computer."),
}
