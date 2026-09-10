"""Expand curated, chapter-specific scenario packs into different assessment tasks.

The source supplies the substance: definition, situation, action, misconception,
correction, verification evidence and limitation. Rendering varies the assessed
skill, not names/numbers in otherwise identical questions. Existing questions are
retained first; round-robin MCQ selection distributes additions across all topics.
"""
from dataclasses import dataclass
from hashlib import sha256

TARGETS = {'mcq': 60, 'short': 40, 'long': 40, 'application': 40, 'competitive': 40}


@dataclass(frozen=True)
class Scenario:
    topic: str
    definition: str
    case: str
    action: str
    misconception: str
    correction: str
    evidence: str
    limitation: str


def mcq_candidates(scenarios):
    # Each format assesses a different skill. Distractors come from the same
    # chapter, but address other topics/situations rather than this prompt.
    formats = [
        ('topic', lambda s: f'Which term matches this definition: “{s.definition}”?', lambda s: s.definition),
        ('action', lambda s: f'{s.case} Which response most directly addresses this case?', lambda s: s.correction + ' ' + s.limitation),
        ('correction', lambda s: f'Which explanation corrects this claim about {s.topic.lower()}: “{s.misconception}”?', lambda s: s.definition + '. ' + s.action),
        ('evidence', lambda s: f'A reviewer checks {s.topic.lower()} in this situation: {s.case} Which observation is the most relevant verification?', lambda s: s.action + ' ' + s.limitation),
        ('definition', lambda s: f'Which principle most directly explains the appropriate response to this situation? {s.case}', lambda s: s.action + ' ' + s.correction),
        ('limitation', lambda s: f'Which caution specifically qualifies this description of {s.topic.lower()}: “{s.definition}”?', lambda s: s.correction + ' ' + s.evidence),
    ]
    for field, prompt, explain in formats:
        for i, scenario in enumerate(scenarios):
            answer = getattr(scenario, field)
            options = [answer] + [getattr(scenarios[(i + offset) % len(scenarios)], field) for offset in (2, 4, 6)]
            question = prompt(scenario)
            offset = int(sha256(question.encode()).hexdigest()[:8], 16) % 4
            options = options[offset:] + options[:offset]
            yield dict(question=question, options=options, answer=answer, explanation=explain(scenario), marks=1, review_indices=[i] + [(i + offset) % len(scenarios) for offset in (2, 4, 6)])


def written_candidate(kind, scenario, index):
    s = scenario
    if kind == 'short':
        question = f'Define {s.topic.lower()} and recommend one relevant action for this case: {s.case}'
        answer = f'{s.definition} (1). {s.action} (1).'
    elif kind == 'long':
        question = (f'Explain a reasoned approach to {s.topic.lower()} using this case: {s.case} '
                    'State the principle, recommend an action, describe how to check the result and explain one limitation.')
        answer = (f'Principle: {s.definition} (1).\nAction: {s.action} (1).\n'
                  f'Verification: {s.evidence} (1).\nLimitation: {s.limitation} (1).')
    elif kind == 'application':
        question = (f'Case review — {s.case} A classmate claims: “{s.misconception}” '
                    'Correct the misconception, choose a better action, specify a check and state a remaining precaution.')
        answer = (f'Correction: {s.correction} (1).\nBetter action: {s.action} (1).\n'
                  f'Check: {s.evidence} (1).\nPrecaution: {s.limitation} (1).')
    else:
        # Higher-order tasks distinguish observed evidence from overclaims,
        # evaluate conflicting advice and identify the limits of a conclusion.
        if index % 4 == 0:
            question = (f'Evidence challenge — {s.case} A check finds: “{s.evidence}” '
                        f'A learner concludes: “{s.misconception}” Does that evidence justify the conclusion? '
                        'Explain the logical error and a remaining limit on what can be concluded.')
            answer = f'No. {s.correction} The observation verifies a specific aspect, not the learner’s broader claim. {s.limitation}'
        elif index % 4 == 1:
            question = (f'Compare two reviewers in this case: {s.case} Reviewer A says: “{s.misconception}” '
                        f'Reviewer B says: “{s.correction}” Whose reasoning is defensible? '
                        'Give an action and an observable check that would support your decision.')
            answer = f'Reviewer B addresses the misconception correctly. {s.action} Check: {s.evidence} Qualification: {s.limitation}'
        elif index % 4 == 2:
            question = (f'Necessary or sufficient? In this case, {s.case} the proposed action is: “{s.action}” '
                        'Would performing that action alone establish that every relevant issue is solved? '
                        'Explain what evidence and qualification your judgement requires.')
            answer = f'Not by itself. An action must be implemented correctly and its effect checked: {s.evidence} Also, {s.limitation} {s.correction}'
        else:
            question = (f'Decision audit — {s.case} A team reports success but provides no supporting observations. '
                        f'Using {s.topic.lower()}, specify a useful test, explain the consequence of overlooking it '
                        f'and evaluate the claim “{s.misconception}”.')
            answer = (f'Test the relevant result: {s.evidence} Without that check, the claimed success is unsupported. '
                      f'The quoted claim is not justified: {s.correction} A remaining boundary is that {s.limitation[0].lower() + s.limitation[1:]}')
    return dict(question=question, answer=answer, marks=0 if kind == 'competitive' else 2 if kind == 'short' else 4)


def additional_written(kind, s, peer, variant):
    if kind == 'short':
        if variant == 1:
            question = f'Correct this misconception about {s.topic.lower()}: “{s.misconception}” Then state one suitable action for this situation: {s.case}'
            answer = f'{s.correction} (1). {s.action} (1).'
        else:
            question = f'Distinguish {s.topic.lower()} from {peer.topic.lower()}. Give the essential meaning of each rather than treating them as interchangeable.'
            answer = f'{s.topic}: {s.definition} (1). {peer.topic}: {peer.definition} (1).'
    elif kind == 'long':
        if variant == 1:
            question = (f'Prepare a four-point checking plan for this case: {s.case} '
                        f'Address the claim “{s.misconception}”, the required response, evidence of its effect and a limit on the conclusion.')
            answer = f'Correct the claim: {s.correction} (1).\nRespond: {s.action} (1).\nCheck: {s.evidence} (1).\nQualify: {s.limitation} (1).'
        else:
            question = (f'Compare the principles and responses needed in two situations. Case A: {s.case} Case B: {peer.case} '
                        'For each case identify its relevant principle and a specific suitable action.')
            answer = f'A — {s.definition} (1). {s.action} (1).\nB — {peer.definition} (1). {peer.action} (1).'
    elif kind == 'application':
        if variant == 1:
            question = (f'An operator proposes the following response: “{s.action}” The situation is: {s.case} '
                        'Explain why the response fits, a misconception to avoid, a result to verify and one precaution still needed.')
            answer = f'Fit: {s.definition} (1).\nAvoid the misconception: {s.correction} (1).\nVerify: {s.evidence} (1).\nPrecaution: {s.limitation} (1).'
        else:
            question = (f'Choose actions and checks for both cases rather than copying one response indiscriminately. '
                        f'Case A: {s.case} Case B: {peer.case} Give one targeted action and one verification for each.')
            answer = f'A action: {s.action} (1). A check: {s.evidence} (1).\nB action: {peer.action} (1). B check: {peer.evidence} (1).'
    else:
        if variant == 1:
            question = (f'Evidence transfer challenge: Case A concerns {s.topic.lower()}: {s.case} '
                        f'Case B concerns {peer.topic.lower()}: {peer.case} A team checks only this observation from B: “{peer.evidence}” '
                        'Can it certify A as correctly resolved? Explain what additional evidence and qualification A needs.')
            answer = f'No; evidence about B is not sufficient proof that A was addressed. For A, check: {s.evidence} The relevant action is: {s.action} Also, {s.limitation}'
        else:
            question = (f'Claim versus demonstration: {s.case} A learner accurately states “{s.correction}” but has not checked the actual result. '
                        'Distinguish knowing the principle from demonstrating success. State a suitable observation and explain what it cannot prove.')
            answer = f'Correctly stating the principle does not prove correct execution. Appropriate action: {s.action} Evidence: {s.evidence} The conclusion remains limited: {s.limitation}'
    return dict(question=question, answer=answer, marks=0 if kind == 'competitive' else 2 if kind == 'short' else 4)


def written_candidates(kind, scenarios):
    for variant in range(3):
        for i, scenario in enumerate(scenarios):
            peer = (i + 5) % len(scenarios)
            if variant == 0:
                q = written_candidate(kind, scenario, i)
            else:
                q = additional_written(kind, scenario, scenarios[peer], variant)
            uses_peer = (variant == 2 and kind != 'competitive') or (variant == 1 and kind == 'competitive')
            q['review_indices'] = [i, peer] if uses_peer else [i]
            yield q


def expand_bank(bank, rows, reviewer):
    seen = {q['question'].strip().casefold() for chapter in bank.values() for group in chapter.values() for q in group}
    for cid, groups in bank.items():
        scenarios = [Scenario(*row) for row in rows[cid]]
        if len(scenarios) != 14 or len({s.topic for s in scenarios}) != 14:
            raise ValueError(f'{cid}: expected fourteen distinct syllabus-reviewed topics')
        approvals = [reviewer(f'scenario:{cid}:{i}', row) for i, row in enumerate(rows[cid], 1)]
        for kind, target in TARGETS.items():
            if len(groups[kind]) > target:
                raise ValueError(f'{cid}/{kind}: existing questions exceed the agreed allocation')
            # Keep the existing 60-MCQ sequence; the five added topic packs expand written practice.
            candidates = mcq_candidates(scenarios[:9]) if kind == 'mcq' else written_candidates(kind, scenarios)
            for q in candidates:
                if len(groups[kind]) == target:
                    break
                key = q['question'].strip().casefold()
                if key in seen:
                    raise ValueError(f'Duplicate expansion prompt: {q["question"]}')
                if kind == 'mcq' and (len(set(q['options'])) != 4 or q['options'].count(q['answer']) != 1):
                    raise ValueError(f'{cid}: repeated MCQ options')
                approval_items = [approvals[i] for i in q.pop('review_indices')]
                q['syllabus'] = list(dict.fromkeys(ref for item in approval_items for ref in item['syllabus']))
                q['review_keys'] = list(dict.fromkeys(ref for item in approval_items for ref in item['review_keys']))
                seen.add(key)
                groups[kind].append(q)
            if len(groups[kind]) != target:
                raise ValueError(f'{cid}/{kind}: insufficient curated questions')
    return bank
