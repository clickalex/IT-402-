/* IT 402 Study Hub — Hindi / Hinglish language switching.
   · Navigation, labels and common phrases translate offline from a local dictionary.
   · Body content is translated on demand via the free Google Translate endpoint and
     cached in localStorage, so a page translated once opens instantly next time.
   · Technical terms (LibreOffice feature names, SQL, menu paths) are protected so
     they stay intact in both Hindi and Hinglish.
   · Offline, content simply stays in English — the site never breaks.
   Choose: English → हिंदी → Hinglish, persisted in localStorage. */
(function (global) {
  'use strict';

  var STORE = 'it402-lang';
  var CACHE = 'it402-tr-cache';
  var SEP = '\n\n@@@@\n\n';

  /* ------------------------------------------------------------------ *
   * Local dictionary (authored, works offline). Key = English text.
   * ------------------------------------------------------------------ */
  var DICT = {
    'Navigate': { hi: 'नेविगेट करें', hinglish: 'Navigate karein' },
    '🏠 Home': { hi: '🏠 होम', hinglish: '🏠 Home' },
    '🗺️ Syllabus & Pattern': { hi: '🗺️ पाठ्यक्रम व पैटर्न', hinglish: '🗺️ Syllabus aur Pattern' },
    'Part A · Employability (10)': { hi: 'भाग A · रोज़गार कौशल (10)', hinglish: 'Part A · Employability (10)' },
    'Unit 1 · Writer (8)': { hi: 'यूनिट 1 · राइटर (8)', hinglish: 'Unit 1 · Writer (8)' },
    'Unit 2 · Calc (10)': { hi: 'यूनिट 2 · कैल्क (10)', hinglish: 'Unit 2 · Calc (10)' },
    'Unit 3 · DBMS (12)': { hi: 'यूनिट 3 · DBMS (12)', hinglish: 'Unit 3 · DBMS (12)' },
    'Unit 4 · Safety (10)': { hi: 'यूनिट 4 · सुरक्षा (10)', hinglish: 'Unit 4 · Safety (10)' },
    'U1 · Communication-II': { hi: 'U1 · संचार-II', hinglish: 'U1 · Communication-II' },
    'U2 · Self-Management-II': { hi: 'U2 · स्व-प्रबंधन-II', hinglish: 'U2 · Self-Management-II' },
    'U3 · ICT Skills-II': { hi: 'U3 · ICT कौशल-II', hinglish: 'U3 · ICT Skills-II' },
    'U4 · Entrepreneurial-II': { hi: 'U4 · उद्यमिता-II', hinglish: 'U4 · Entrepreneurial-II' },
    'U5 · Green Skills-II': { hi: 'U5 · हरित कौशल-II', hinglish: 'U5 · Green Skills-II' },
    'Ch 1 · Styles': { hi: 'अध्याय 1 · स्टाइल्स', hinglish: 'Ch 1 · Styles' },
    'Ch 2 · Images': { hi: 'अध्याय 2 · चित्र', hinglish: 'Ch 2 · Images' },
    'Ch 3 · ToC + Templates + Track': { hi: 'अध्याय 3 · ToC + टेम्पलेट + ट्रैक', hinglish: 'Ch 3 · ToC + Templates + Track' },
    'Ch 4 · Scenarios + Goal Seek': { hi: 'अध्याय 4 · परिदृश्य + Goal Seek', hinglish: 'Ch 4 · Scenarios + Goal Seek' },
    'Ch 5 · Macros': { hi: 'अध्याय 5 · मैक्रोज़', hinglish: 'Ch 5 · Macros' },
    'Ch 6 · Linking Data': { hi: 'अध्याय 6 · डेटा लिंक करना', hinglish: 'Ch 6 · Linking Data' },
    'Ch 7 · Share & Review': { hi: 'अध्याय 7 · साझा करना व समीक्षा', hinglish: 'Ch 7 · Share & Review' },
    'Ch 8 · DBMS Intro': { hi: 'अध्याय 8 · DBMS परिचय', hinglish: 'Ch 8 · DBMS Intro' },
    'Ch 9 · Base Tables': { hi: 'अध्याय 9 · Base टेबल', hinglish: 'Ch 9 · Base Tables' },
    'Ch 10 · Relationships': { hi: 'अध्याय 10 · संबंध', hinglish: 'Ch 10 · Relationships' },
    'Ch 11 · Queries': { hi: 'अध्याय 11 · क्वेरीज़', hinglish: 'Ch 11 · Queries' },
    'Ch 12 · Forms & Reports': { hi: 'अध्याय 12 · फ़ॉर्म व रिपोर्ट', hinglish: 'Ch 12 · Forms & Reports' },
    'Ch 13 · HSS at Workplace': { hi: 'अध्याय 13 · कार्यस्थल पर HSS', hinglish: 'Ch 13 · HSS at Workplace' },
    'Ch 14 · Quality + Ergonomics': { hi: 'अध्याय 14 · गुणवत्ता + एर्गोनॉमिक्स', hinglish: 'Ch 14 · Quality + Ergonomics' },
    'Ch 15 · Accidents & Emergencies': { hi: 'अध्याय 15 · दुर्घटनाएँ व आपातस्थितियाँ', hinglish: 'Ch 15 · Accidents & Emergencies' },
    '❓ Question Bank': { hi: '❓ प्रश्न बैंक', hinglish: '❓ Question Bank' },
    '📝 PYQ Practice': { hi: '📝 PYQ अभ्यास', hinglish: '📝 PYQ Practice' },
    '💻 Practical Lab': { hi: '💻 प्रैक्टिकल लैब', hinglish: '💻 Practical Lab' },
    '🧠 Revision': { hi: '🧠 रिवीज़न', hinglish: '🧠 Revision' },
    'Progress': { hi: 'प्रगति', hinglish: 'Progress' },
    'Show answer': { hi: 'उत्तर दिखाएँ', hinglish: 'Answer dikhayein' },
    'Hide answer': { hi: 'उत्तर छिपाएँ', hinglish: 'Answer chhupayein' },
    'Choose your chapter': { hi: 'अपना अध्याय चुनें', hinglish: 'Apna chapter chunein' },
    'Open chapter questions →': { hi: 'अध्याय के प्रश्न खोलें →', hinglish: 'Chapter ke questions kholen →' },
    'Open this chapter’s questions + MCQs →': { hi: 'इस अध्याय के प्रश्न + MCQ खोलें →', hinglish: 'Is chapter ke questions + MCQs kholen →' },
    'Hide all answers': { hi: 'सभी उत्तर छिपाएँ', hinglish: 'Saare answers chhupayein' },
    'Read chapter notes →': { hi: 'अध्याय के नोट्स पढ़ें →', hinglish: 'Chapter notes padhein →' },
    'Unit overview →': { hi: 'यूनिट अवलोकन →', hinglish: 'Unit overview →' },
    'Official SQP questions →': { hi: 'आधिकारिक SQP प्रश्न →', hinglish: 'Official SQP questions →' },
    'Open the full chapter →': { hi: 'पूरा अध्याय खोलें →', hinglish: 'Poora chapter kholen →' },
    'Syllabus topic:': { hi: 'पाठ्यक्रम विषय:', hinglish: 'Syllabus topic:' },
    'PYQ:': { hi: 'PYQ:', hinglish: 'PYQ:' },
    'Ungraded extension': { hi: 'अनग्रेडेड विस्तार', hinglish: 'Ungraded extension' },
    'Show question type': { hi: 'प्रश्न का प्रकार दिखाएँ', hinglish: 'Question ka type dikhayein' },
    'Start': { hi: 'शुरू करें', hinglish: 'Shuru karein' },
    'Pause': { hi: 'रोकें', hinglish: 'Rokein' },
    'Reset': { hi: 'रीसेट', hinglish: 'Reset' },
    'On this page:': { hi: 'इस पृष्ठ पर:', hinglish: 'Is page par:' },
    'Search 20 chapters…  ( / )': { hi: '20 अध्याय खोजें…  ( / )', hinglish: '20 chapters khojein…  ( / )' },
    'Open navigation': { hi: 'नेविगेशन खोलें', hinglish: 'Navigation kholen' },
    'Toggle dark mode': { hi: 'डार्क मोड बदलें', hinglish: 'Dark mode badlein' },
    'Back to top': { hi: 'ऊपर जाएँ', hinglish: 'Upar jaayein' },
    'Language': { hi: 'भाषा', hinglish: 'Bhasha' },
    'CBSE Class 10 Information Technology · Subject Code 402 · Session 2026–27':
      { hi: 'CBSE कक्षा 10 सूचना प्रौद्योगिकी · विषय कोड 402 · सत्र 2026–27', hinglish: 'CBSE Class 10 Information Technology · Subject Code 402 · Session 2026–27' },
    'LibreOffice-only study hub · 20 chapters · works offline':
      { hi: 'केवल LibreOffice अध्ययन हब · 20 अध्याय · ऑफ़लाइन चलता है', hinglish: 'Sirf LibreOffice study hub · 20 chapters · offline chalta hai' },
    'No page found — try “macros”, “viva” or “ergonomics”.':
      { hi: 'कोई पृष्ठ नहीं मिला — “macros”, “viva” या “ergonomics” आज़माएँ।', hinglish: 'Koi page nahi mila — “macros”, “viva” ya “ergonomics” try karein.' },
    '✓ Correct': { hi: '✓ सही', hinglish: '✓ Sahi' },
    '✗ Correct answer: {a}': { hi: '✗ सही उत्तर: {a}', hinglish: '✗ Sahi answer: {a}' },
    'Score: {c}/{a} answered (of {v} shown)':
      { hi: 'स्कोर: {c}/{a} उत्तर दिए ({v} में से)', hinglish: 'Score: {c}/{a} answered ({v} mein se)' },
    'progress_label': { hi: '{total} में से {done} अध्याय पूर्ण', hinglish: '{done} of {total} chapters complete' },
    'unit_label': { hi: '{d}/{tot} अध्याय', hinglish: '{d}/{tot} chapters' },
    'q_status': { hi: '{total} में से {count} प्रश्न दिख रहे हैं। उत्तर वैसे ही हैं जैसे आपने छोड़े थे; सभी बंद करने के लिए “सभी उत्तर छिपाएँ” दबाएँ।', hinglish: '{count} of {total} questions shown. Answers waise hi hain; sab band karne ke liye “Hide all answers” dabayein.' },
    'chapter_status': { hi: '{mcqs} MCQ और {written} लिखित प्रश्न दिख रहे हैं। अध्याय बदलने पर उत्तर सुरक्षित रहते हैं।', hinglish: '{mcqs} MCQs aur {written} written questions shown. Chapter badalne par answers safe rehte hain.' },
    'choose_valid_chapter': { hi: 'अपने प्रश्न पृष्ठ को खोलने के लिए नीचे एक मान्य अध्याय चुनें।', hinglish: 'Question page kholne ke liye neeche sahi chapter chunein.' },
    'translating': { hi: 'अनुवाद हो रहा है… {p}%', hinglish: 'Translate ho raha hai… {p}%' },
    'offline_notice': { hi: 'ऑफ़लाइन — अंग्रेज़ी दिखाई जा रही है', hinglish: 'Offline — English dikhaya ja raha hai' }
  };

  /* ------------------------------------------------------------------ *
   * Technical terms kept in English. [term, caseInsensitive?]
   * ------------------------------------------------------------------ */
  var TERMS = [
    ['Microsoft Word', 1], ['Styles and Formatting', 1], ['Update Selected Style', 1],
    ['Referential Integrity', 1], ['Table of Contents', 1], ['Data Consolidation', 1],
    ['Text Wrapping', 1], ['Bring to Front', 1], ['Send to Back', 1], ['Primary Key', 1],
    ['Foreign Key', 1], ['Composite Key', 1], ['Candidate Key', 1], ['Fill Format', 1],
    ['Goal Seek', 1], ['Ctrl+Shift+N', 1], ['Keep ratio', 1], ['Wrap text', 1],
    ['As Character', 1], ['To Paragraph', 1], ['Page Wrap', 1], ['Design view', 1],
    ['Basic IDE', 1], ['Mail Merge', 1], ['Smart Goals', 1], ['Default Value', 1],
    ['LibreOffice', 1], ['OpenOffice', 1], ['Subtotal', 1], ['Consolidate', 1],
    ['Hyperlink', 1], ['Anchoring', 1], ['Solver', 1], ['Macro', 1], ['MySQL', 1],
    ['MS Word', 1], ['MS Excel', 1], ['MS Access', 1], ['20-20-20', 1], ['Win+R', 1],
    ['Ctrl+K', 1], ['Wi-Fi', 1], ['Sub … End Sub', 1], ['End Sub', 1], ['VARCHAR', 1],
    ['PDF', 1], ['CSV', 1], ['HTML', 1], ['HTTP', 1], ['HTTPS', 1], ['FTP', 1],
    ['URL', 1], ['USB', 1], ['CPU', 1], ['WiFi', 1], ['F5', 1],
    ['CREATE TABLE', 0], ['ORDER BY', 0], ['GROUP BY', 0], ['SELECT', 0], ['INSERT', 0],
    ['UPDATE', 0], ['DELETE', 0], ['WHERE', 0], ['LIKE', 0], ['DBMS', 0], ['RDBMS', 0],
    ['SQL', 0], ['SDG', 0], ['SMART', 0], ['OOS', 0], ['RSI', 0], ['PPE', 0], ['CCTV', 0],
    ['RAM', 0], ['LAN', 0], ['WAN', 0], ['ISP', 0], ['OS', 0], ['PASS', 0], ['MS', 0], ['IP', 0]
  ].sort(function (a, b) { return b[0].length - a[0].length; });

  function esc(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }

  function protectTerms(text) {
    var out = text, map = {}, n = 0;
    for (var i = 0; i < TERMS.length; i++) {
      var term = TERMS[i][0], flags = TERMS[i][1] ? 'gi' : 'g';
      var re = new RegExp('\\b' + esc(term) + '\\b', flags);
      out = out.replace(re, function (m) {
        var tok = '[{t' + (n++) + '}]';
        map[tok] = m;
        return tok;
      });
    }
    return { text: out, map: map };
  }

  function restoreTerms(text, map) {
    var out = text;
    for (var tok in map) {
      if (out.indexOf(tok) === -1) return null; // token was altered by the translator
      out = out.split(tok).join(map[tok]);
    }
    return out;
  }

  /* ------------------------------------------------------------------ *
   * Devanagari → Latin (informal Hinglish transliteration).
   * ------------------------------------------------------------------ */
  var VOWELS = { 'अ': 'a', 'आ': 'aa', 'इ': 'i', 'ई': 'ee', 'उ': 'u', 'ऊ': 'oo', 'ऋ': 'ri', 'ए': 'e', 'ऐ': 'ai', 'ओ': 'o', 'औ': 'au' };
  var MATRA = { 'ा': 'aa', 'ि': 'i', 'ी': 'ee', 'ु': 'u', 'ू': 'oo', 'ृ': 'ri', 'े': 'e', 'ै': 'ai', 'ो': 'o', 'ौ': 'au', 'ं': 'n', 'ँ': 'n', 'ः': 'h' };
  var CONSONANTS = { 'क': 'k', 'ख': 'kh', 'ग': 'g', 'घ': 'gh', 'ङ': 'ng', 'च': 'ch', 'छ': 'chh', 'ज': 'j', 'झ': 'jh', 'ञ': 'ny', 'ट': 't', 'ठ': 'th', 'ड': 'd', 'ढ': 'dh', 'ण': 'n', 'त': 't', 'थ': 'th', 'द': 'd', 'ध': 'dh', 'न': 'n', 'प': 'p', 'फ': 'ph', 'ब': 'b', 'भ': 'bh', 'म': 'm', 'य': 'y', 'र': 'r', 'ल': 'l', 'व': 'v', 'श': 'sh', 'ष': 'sh', 'स': 's', 'ह': 'h', 'ड़': 'r', 'ढ़': 'rh', 'फ़': 'f', 'ज़': 'z', 'क़': 'q', 'ग़': 'gh', 'ख़': 'kh' };
  var LIGATURES = { 'क्ष': 'ksh', 'त्र': 'tr', 'ज्ञ': 'gy', 'श्र': 'shr' };
  var DIGITS = { '०': '0', '१': '1', '२': '2', '३': '3', '४': '4', '५': '5', '६': '6', '७': '7', '८': '8', '९': '9' };
  var VOWEL_CHARS = Object.keys(VOWELS).join('');
  var MATRA_CHARS = Object.keys(MATRA).join('');
  var CONS_CHARS = Object.keys(CONSONANTS).join('');

  function transliterateDeva(t) {
    var out = '';
    for (var i = 0; i < t.length; i++) {
      var c = t[i], nxt = t[i + 1];
      if (LIGATURES[c + nxt]) { out += LIGATURES[c + nxt]; i++; continue; }
      if (CONSONANTS[c] !== undefined) {
        out += CONSONANTS[c];
        if (nxt === '्') { continue; }                 // virama: no vowel, form a conjunct
        if (nxt === undefined || /[\s.,;:!?।॥…'"”’)\]}»>-]/.test(nxt)) { continue; } // end of word: drop schwa
        if (MATRA_CHARS.indexOf(nxt) !== -1) { continue; }                          // matra supplies the vowel
        if (VOWEL_CHARS.indexOf(nxt) !== -1) { out += 'a'; continue; }              // ka + independent vowel
        if (CONS_CHARS.indexOf(nxt) !== -1) { out += 'a'; continue; }               // consonant cluster keeps schwa
        continue;
      }
      if (c === '्') { continue; }
      if (MATRA[c] !== undefined) {
        if (c === 'े' && nxt === 'ं') { out += 'ein'; i++; continue; }
        if (c === 'ै' && nxt === 'ं') { out += 'ain'; i++; continue; }
        out += MATRA[c]; continue;
      }
      if (VOWELS[c] !== undefined) { out += VOWELS[c]; continue; }
      if (DIGITS[c] !== undefined) { out += DIGITS[c]; continue; }
      out += c; // Latin text, punctuation, emoji — pass through
    }
    return out;
  }

  /* ------------------------------------------------------------------ *
   * Phrase lookup: exact dictionary hit, then small patterns.
   * ------------------------------------------------------------------ */
  function localPhrase(text, lang) {
    var e = DICT[text];
    if (e && e[lang]) return e[lang];
    var m;
    if ((m = /^(\d+) suggested marks?$/.exec(text))) return (lang === 'hi' ? m[1] + ' सुझाए गए अंक' : m[1] + ' suggested marks');
    if ((m = /^MCQs \((\d+)\)$/.exec(text))) return 'MCQs (' + m[1] + ')';
    if ((m = /^Short questions \((\d+)\)$/.exec(text))) return (lang === 'hi' ? 'लघु प्रश्न (' + m[1] + ')' : 'Short questions (' + m[1] + ')');
    if ((m = /^Long questions \((\d+)\)$/.exec(text))) return (lang === 'hi' ? 'दीर्घ प्रश्न (' + m[1] + ')' : 'Long questions (' + m[1] + ')');
    if ((m = /^Application questions \((\d+)\)$/.exec(text))) return (lang === 'hi' ? 'अनुप्रयोग प्रश्न (' + m[1] + ')' : 'Application questions (' + m[1] + ')');
    if ((m = /^Competitive-style challenges \((\d+)\)$/.exec(text))) return (lang === 'hi' ? 'प्रतियोगी-शैली चुनौतियाँ (' + m[1] + ')' : 'Competitive-style challenges (' + m[1] + ')');
    if ((m = /^All questions \((\d+)\)$/.exec(text))) return (lang === 'hi' ? 'सभी प्रश्न (' + m[1] + ')' : 'All questions (' + m[1] + ')');
    if ((m = /^MCQs (\d+)–(\d+)$/.exec(text))) return 'MCQs ' + m[1] + '–' + m[2];
    if ((m = /^MCQs · (\d+)$/.exec(text))) return 'MCQs · ' + m[1];
    if ((m = /^Short questions · (\d+)$/.exec(text))) return (lang === 'hi' ? 'लघु प्रश्न · ' + m[1] : 'Short questions · ' + m[1]);
    if ((m = /^Long questions · (\d+)$/.exec(text))) return (lang === 'hi' ? 'दीर्घ प्रश्न · ' + m[1] : 'Long questions · ' + m[1]);
    if ((m = /^Application questions · (\d+)$/.exec(text))) return (lang === 'hi' ? 'अनुप्रयोग प्रश्न · ' + m[1] : 'Application questions · ' + m[1]);
    if ((m = /^Competitive-style challenges · (\d+)$/.exec(text))) return (lang === 'hi' ? 'प्रतियोगी-शैली चुनौतियाँ · ' + m[1] : 'Competitive-style challenges · ' + m[1]);
    if ((m = /^MCQs (\d+)–(\d+)$/.exec(text))) return 'MCQs ' + m[1] + '–' + m[2];
    return null;
  }

  /* ------------------------------------------------------------------ *
   * Translation cache (localStorage, best effort).
   * ------------------------------------------------------------------ */
  var cache = null;
  function loadCache() {
    if (cache) return cache;
    try {
      cache = JSON.parse(localStorage.getItem(CACHE) || '{}');
    } catch (e) { cache = {}; }
    return cache;
  }
  function cacheGet(lang, text) {
    var c = loadCache()[lang + '\u0000' + text];
    return c === undefined ? null : c;
  }
  function cacheSet(lang, text, value) {
    loadCache()[lang + '\u0000' + text] = value;
    try {
      var s = JSON.stringify(cache);
      if (s.length < 2500000) localStorage.setItem(CACHE, s);
    } catch (e) { /* quota exceeded — keep in-memory only */ }
  }

  /* ------------------------------------------------------------------ *
   * Google Translate (free, keyless endpoint) → Hindi string or null.
   * ------------------------------------------------------------------ */
  function googleHi(text) {
    var p = protectTerms(text);
    var attempt = function (src) {
      var url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=hi&dt=t&q=' + encodeURIComponent(src);
      return fetch(url).then(function (res) {
        if (!res.ok) throw new Error('bad status');
        return res.json();
      }).then(function (data) {
        return (data && data[0]) ? data[0].map(function (s) { return s[0]; }).join('') : '';
      });
    };
    return attempt(p.text).then(function (out) {
      var restored = restoreTerms(out, p.map);
      if (restored != null) return restored;
      return attempt(text); // protection tokens were altered — retry unprotected
    }).catch(function () { return null; });
  }

  /* ------------------------------------------------------------------ *
   * DOM helpers.
   * ------------------------------------------------------------------ */
  function getLang() {
    var v = null;
    try { v = localStorage.getItem(STORE); } catch (e) {}
    return (v === 'hi' || v === 'hinglish') ? v : 'en';
  }

  var SKIP_TAGS = { SCRIPT: 1, STYLE: 1, NOSCRIPT: 1, PRE: 1, CODE: 1, KBD: 1, INPUT: 1, TEXTAREA: 1, SELECT: 1, OPTION: 1, IFRAME: 1, SVG: 1 };
  var SKIP_SELECTOR = '.brand, .lang-wrap, .sr-only, .timer-display, #searchResults, [data-no-translate], [data-progress-label], [data-question-status], [data-unit-label], .quiz-score, .feedback, #chapter-status, #practice-navigation-status';

  function collectTextNodes() {
    var nodes = [];
    var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
      acceptNode: function (node) {
        var p = node.parentElement;
        if (!p) return NodeFilter.FILTER_REJECT;
        if (SKIP_TAGS[p.tagName]) return NodeFilter.FILTER_REJECT;
        if (p.closest && p.closest(SKIP_SELECTOR)) return NodeFilter.FILTER_REJECT;
        var t = node.nodeValue.replace(/\s+/g, ' ').trim();
        if (!t || !/[A-Za-z\u0900-\u097F]/.test(t)) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    while (walker.nextNode()) nodes.push(walker.currentNode);
    return nodes;
  }

  function wrapNode(node) {
    var raw = node.nodeValue;
    var span = document.createElement('span');
    span.className = 'i18n-node';
    span.dataset.en = raw;                                   // original, for restoring English
    span.dataset.padL = (raw.match(/^\s*/) || [''])[0];
    span.dataset.padR = (raw.match(/\s*$/) || [''])[0];
    span.textContent = raw;
    node.parentNode.replaceChild(span, node);
    return span;
  }

  function keyOf(span) {
    return span.dataset.en.replace(/\s+/g, ' ').trim();
  }

  function setSpan(span, value, lang) {
    span.textContent = (span.dataset.padL || '') + value + (span.dataset.padR || '');
    span.dataset.lang = lang;
    cacheSet(lang, keyOf(span), value);
  }

  function translateSpan(span, lang) {
    return googleHi(keyOf(span)).then(function (hi) {
      if (hi == null) return;
      setSpan(span, lang === 'hinglish' ? transliterateDeva(hi) : hi, lang);
    });
  }

  function translateBatch(batch, lang) {
    return googleHi(batch.text).then(function (hi) {
      if (hi == null) return; // offline — keep English
      var parts = hi.split('@@@@');
      if (parts.length === batch.spans.length) {
        for (var j = 0; j < parts.length; j++) {
          var val = parts[j].trim();
          setSpan(batch.spans[j], lang === 'hinglish' ? transliterateDeva(val) : val, lang);
        }
      } else {
        var jobs = batch.spans.map(function (s) { return translateSpan(s, lang); });
        return Promise.all(jobs);
      }
    });
  }

  function runQueue(batches, lang, onProgress) {
    var next = 0, done = 0;
    var worker = function () {
      return new Promise(function (resolve) {
        var step = function () {
          if (next >= batches.length) return resolve();
          var b = batches[next++];
          translateBatch(b, lang).then(function () {
            done++;
            if (onProgress) onProgress(Math.round(done / batches.length * 100));
            step();
          }, function () { done++; step(); });
        };
        step();
      });
    };
    var pool = [];
    for (var i = 0; i < 4; i++) pool.push(worker());
    return Promise.all(pool);
  }

  function translateAll(nodes, lang, onProgress) {
    var todo = [];
    var spans = [];
    nodes.forEach(function (node) {
      var span = (node.parentElement.className === 'i18n-node') ? node.parentElement : wrapNode(node);
      spans.push(span);
      if (span.dataset.lang === lang) return;
      var key = keyOf(span);
      var local = localPhrase(key, lang);
      if (local != null) { setSpan(span, local, lang); return; }
      var cached = cacheGet(lang, key);
      if (cached != null) { setSpan(span, cached, lang); return; }
      todo.push(span);
    });
    if (!todo.length) return Promise.resolve();
    var batches = [];
    for (var i = 0; i < todo.length;) {
      var list = [], len = 0, text = [];
      while (i < todo.length && list.length < 10 && len < 1400) {
        var t = keyOf(todo[i]);
        list.push(todo[i]); text.push(t); len += t.length + SEP.length; i++;
      }
      batches.push({ spans: list, text: text.join(SEP) });
    }
    return runQueue(batches, lang, onProgress);
  }

  /* ------------------------------------------------------------------ *
   * Attributes (placeholder / aria-label) — offline, from the dictionary.
   * ------------------------------------------------------------------ */
  function translateAttributes(lang) {
    var map = [
      ['#siteSearch', 'placeholder', 'Search 20 chapters…  ( / )'],
      ['.menu-btn', 'aria-label', 'Open navigation'],
      ['.theme-btn', 'aria-label', 'Toggle dark mode'],
      ['.backtop', 'aria-label', 'Back to top']
    ];
    map.forEach(function (item) {
      var el = document.querySelector(item[0]);
      if (!el) return;
      if (lang === 'en') {
        if (el.dataset.enAttr) el.setAttribute(item[1], el.dataset.enAttr);
      } else {
        if (!el.dataset.enAttr) el.dataset.enAttr = el.getAttribute(item[1]) || '';
        el.setAttribute(item[1], DICT[item[2]] ? DICT[item[2]][lang] : item[2]);
      }
    });
  }

  function restoreEnglish() {
    document.querySelectorAll('.i18n-node').forEach(function (span) {
      span.textContent = span.dataset.en;
      delete span.dataset.lang;
    });
    translateAttributes('en');
    document.documentElement.lang = 'en';
  }

  /* ------------------------------------------------------------------ *
   * Switcher UI + orchestration.
   * ------------------------------------------------------------------ */
  function buildSwitcher() {
    var bar = document.querySelector('.topbar');
    if (!bar || bar.querySelector('.lang-wrap')) return;
    var wrap = document.createElement('span');
    wrap.className = 'lang-wrap';
    wrap.setAttribute('data-no-translate', '');
    var select = document.createElement('select');
    select.className = 'lang-select';
    select.setAttribute('aria-label', 'Language / भाषा');
    select.title = 'Language / भाषा';
    [['en', 'English'], ['hi', 'हिंदी'], ['hinglish', 'Hinglish']].forEach(function (pair) {
      var o = document.createElement('option');
      o.value = pair[0]; o.textContent = pair[1];
      select.appendChild(o);
    });
    var status = document.createElement('span');
    status.className = 'tr-status';
    status.setAttribute('aria-live', 'polite');
    status.hidden = true;
    wrap.appendChild(select);
    wrap.appendChild(status);
    var theme = bar.querySelector('.theme-btn');
    if (theme) bar.insertBefore(wrap, theme); else bar.appendChild(wrap);
    return { select: select, status: status };
  }

  function setLang(lang, ui) {
    if (!ui) ui = { select: document.querySelector('.lang-select'), status: document.querySelector('.tr-status') };
    try { localStorage.setItem(STORE, lang); } catch (e) {}
    if (ui && ui.select) ui.select.value = lang;
    if (lang === 'en') { restoreEnglish(); return; }
    var nodes = collectTextNodes();
    translateAttributes(lang);
    document.documentElement.lang = lang;
    if (ui && ui.status) {
      ui.status.hidden = false;
      ui.status.textContent = (DICT.translating[lang] || '').replace('{p}', '0');
    }
    translateAll(nodes, lang, function (pct) {
      if (ui && ui.status) {
        if (pct >= 100) { ui.status.hidden = true; }
        else ui.status.textContent = (DICT.translating[lang] || '').replace('{p}', pct);
      }
    }).then(function () {
      if (ui && ui.status) ui.status.hidden = true;
    });
  }

  function mount() {
    var ui = buildSwitcher();
    var lang = getLang();
    if (lang !== 'en') {
      setLang(lang, ui);
    } else if (ui && ui.select) {
      ui.select.value = 'en';
    }
    if (ui && ui.select) {
      ui.select.addEventListener('change', function () { setLang(ui.select.value, ui); });
    }
  }

  /* ------------------------------------------------------------------ *
   * Template helper used by app.js for dynamic labels.
   * ------------------------------------------------------------------ */
  function tr(key, fallback, replacements) {
    var entry = DICT[key];
    var lang = getLang();
    var s = (lang !== 'en' && entry && entry[lang]) ? entry[lang] : fallback;
    if (replacements) {
      s = s.replace(/\{(\w+)\}/g, function (m, k) {
        return (replacements[k] !== undefined && replacements[k] !== null) ? replacements[k] : m;
      });
    }
    return s;
  }

  var API = {
    mount: mount,
    setLang: setLang,
    getLang: getLang,
    tr: tr,
    localPhrase: localPhrase,
    protectTerms: protectTerms,
    restoreTerms: restoreTerms,
    transliterateDeva: transliterateDeva,
    DICT: DICT,
    TERMS: TERMS
  };

  if (typeof module !== 'undefined' && module.exports) {
    module.exports = API;
  } else {
    global.I18N = API;
    if (document.readyState !== 'loading') mount();
    else document.addEventListener('DOMContentLoaded', mount);
  }
})(typeof window !== 'undefined' ? window : globalThis);
