# Chapter question sources

These are original authored exercises, not official CBSE or competition questions.
The 20 chapter IDs must match `tools/tpl.py`.

## Format

The UTF-8 text files use `[chapter-id]` section headings. Blank lines and lines
beginning with `#` are ignored. Each question occupies one line; separate fields
with ` | `. Do not use a literal `|` inside a field. HTML is escaped by the renderer.

`mcqs.txt` (six fields):

```text
[chapter-id]
Question | Correct option | Wrong option 1 | Wrong option 2 | Wrong option 3 | Explanation
```

The correct option is deliberately explicit in the source. The generator rotates
options deterministically so the displayed correct answer does not always occupy
the same position. Four distinct nonempty options are required.

`written.txt` (four fields):

```text
[chapter-id]
short | Question | 2 | Model answer with marking points
long | Question | 4 | Model answer with marking points
application | Case or task | 4 | Worked response with marking points
competitive | Reasoning challenge | 0 | Worked explanation
```

A zero means ungraded reasoning practice, not a zero-value exam question. All
content stays within the prescribed topics. Longer Part A questions extend the
response format, not the syllabus or claimed board-paper mark allocation.

## Scenario expansion format

`scenarios.txt` contains nine existing topic packs per chapter;
`scenarios-extra.txt` adds five more. Together: 14 per chapter, 280 overall.
Each pipe-separated line has eight nonempty fields:

```text
topic | definition | situation | appropriate action | misconception | correction | evidence to check | limitation
```

The misconception must be a claim that the correction directly addresses. Evidence
must describe an observable check specific to the situation, not generic “it works”
text. The limitation prevents the result being overgeneralised. Peer topics within
the same chapter supply distractors; review them for relevance and a single best
answer whenever editing a pack.

`tools/practice_expansion.py` renders these packs into skill-specific exercises:
concept identification, choosing a response, correcting a misconception, selecting
verification evidence and reasoning about principles/limitations. Written variants
ask for a definition/action, a four-point approach, a case correction, or evaluation
of evidence and competing claims. These share the topic deliberately, but assess
different tasks. They are not represented as independently sourced exam questions.

## Coverage and generation

- The reviewed base comprises 200 MCQs and 160 written items here, plus 50 mapped
  MCQs in `tools/quiz.py` and 20 written prompts in `tools/trend_practice.py`.
- 3,970 scenario-derived items bring the total to **4,400**. Each chapter has
  **60 MCQs + 40 short + 40 long + 40 application + 40 competitive-style = 220**.
- This adds 30 of EACH written type per chapter (2,400 written questions total)
  relative to the earlier 100-item version. Preserve in-scope questions, but replace
  unsupported or inaccurate content; the 430-item reviewed base stays at the start
  of its respective categories. Changes are documented in `audit-changes.json`.
- MCQs retain their original nine-topic traversal, with audited scope corrections.
  Written variants traverse all 14 topics. Three formats per type assess a single
  concept, a misconception/checking task, or a paired-case/distinction task.
  Paired questions inherit references from both topic packs. The target determines
  how many candidates are needed; the last traversal need not use every candidate.
- Generation rejects missing chapters, malformed packs, duplicate new prompts,
  repeated options, insufficient candidates and base sets larger than the target.
- All answers use initially closed native `<details>`. Selecting an MCQ option does
  not reveal the answer; no scoring, submission or answer persistence is implied.
- All 220 questions remain accessible offline without JavaScript. Type selectors
  and sets-of-ten MCQ links enhance navigation. Legacy mixed practice remains
  separately labelled and is not covered by this review.

## Mandatory syllabus review

`syllabus-review.json` is a deliberately reviewed ledger, **not** automatically
inferred keyword approval. It records the official 2026–27 IT-402 and Employability
Skills Class X URLs, page references, detailed scope, 710 source fingerprints and
the expansion-engine fingerprint. Sources are keyed by chapter and one-based row:
`mcq:`, `written:`, `scenario:` (rows 1–9 original, 10–14 extra), `legacy-mcq:` and
`trend:`. Review whole prompts, every distractor, correct answers and explanations;
for packs, inspect all eight fields and their generated task/answer combinations.

After editing content:

1. Read the relevant original official table and check that the assessed knowledge
   is prescribed at Class X, rather than merely related to computing in general.
2. Review correctness and ambiguity, including paired cases and distractors from
   the same chapter. Prefer a clearly listed topic when the scope is uncertain.
3. Record appropriate outcome IDs and document substantive replacements in the
   change log. Update only the deliberately reviewed entry's SHA-256 using
   `tools.syllabus_review.fingerprint(fields)` with the exact parsed source fields.
4. If expansion templates change, inspect the affected generated questions and
   update `expansion_engine_sha256` only after reviewing those formats.
5. Regenerate, inspect the manifest diff and run static/browser tests. A fingerprint
   proves that content has not changed since review, not that it is educationally
   correct or endorsed by CBSE. Do not blindly refresh all hashes to make tests pass.

Build using `python3 tools/practice.py` (or the full build in the root README).
It writes the directory, 20 pages, `syllabus-audit.html` and
`docs/question-syllabus-audit.csv` with one row per question, exact prompts and
fingerprints covering answers/options as well as prompts.

`python3 tests/audit_site.py` checks counts, reviewed-base retention, answer keys,
closed answers, all local links and mappings, manifest regeneration and negative
missing/stale-review cases. `tests/browser_practice.py` checks actual filtering,
keyboard answers, routes, narrow/dark layouts and all 220 offline/no-JS questions.
