"""Minimal Markdown-subset to HTML converter for IT-402 notes."""
import re, html as ihtml

def slug(t):
    t = re.sub(r"<[^>]+>", "", t)
    t = re.sub(r"[^\w\s-]", "", t).strip().lower()
    return re.sub(r"[\s_]+", "-", t)[:60]

def inline(md):
    esc = ihtml.escape(md)
    def code_repl(m):
        c = m.group(1)
        if re.search(r"Ctrl|Alt|Shift|Win|F\d|Del|Esc|Enter|Tab|Insert|Home|End|Backspace", c) and len(c) < 40:
            return "+".join(f"<kbd>{p.strip()}</kbd>" for p in c.split("+"))
        return f"<code>{c}</code>"
    esc = re.sub(r"`([^`]+)`", code_repl, esc)
    esc = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", esc)
    esc = re.sub(r"(?<!\w)\*(?!\*)([^*\n]+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", esc)
    esc = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', esc)
    return esc

LIST_RE = re.compile(r"^(\s*)(?:(-|\*)|(\d+)\.)\s+(.*)$")

def render_list_block(lines):
    items = []
    for ln in lines:
        m = LIST_RE.match(ln)
        ind = len(m.group(1).replace("\t", "    "))
        items.append((ind, bool(m.group(3)), m.group(4)))
    base = min(i[0] for i in items)
    tag = "ol" if items[0][1] else "ul"
    cls = ' class="steps"' if items[0][1] else ""
    out = [f"<{tag}{cls}>"]
    i = 0
    while i < len(items):
        ind, _, text = items[i]
        if ind > base:
            i += 1; continue
        kids, j = [], i + 1
        while j < len(items) and items[j][0] > base:
            kids.append(items[j]); j += 1
        # checklist items
        if text.strip().startswith("[ ]"):
            out.append(f'<label class="check"><input type="checkbox">{inline(text.strip()[3:].strip())}</label>')
        else:
            out.append(f"<li>{inline(text)}")
            if kids:
                ktag = "ol" if kids[0][1] else "ul"
                out.append(f"<{ktag}>" + "".join(f"<li>{inline(k[2])}</li>" for k in kids) + f"</{ktag}>")
            out.append("</li>")
        i = j
    out.append(f"</{tag}>")
    return "\n".join(out)

def render_table_block(lines):
    rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in lines]
    rows = [r for r in rows if not all(re.match(r"^:?-{2,}:?$", c or "--") for c in r)]
    if not rows: return ""
    out = ["<table>", "<tr>" + "".join(f"<th>{inline(c)}</th>" for c in rows[0]) + "</tr>"]
    for r in rows[1:]:
        out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
    out.append("</table>")
    return "\n".join(out)

def _slurp_plain(lines, j):
    """Collect plain paragraph lines until a structural line. Returns (html_list, new_j)."""
    inner, buf = [], []
    n = len(lines)
    def flush():
        if buf:
            inner.append("<p>" + "<br>".join(inline(b) for b in buf) + "</p>")
            buf.clear()
    while j < n:
        t = lines[j].strip()
        if not t:
            flush(); j += 1; continue
        if re.match(r"^#{1,4}\s+", t) or t == "---" or t.startswith("```") or t.startswith("|") or LIST_RE.match(lines[j]) or t.startswith(">"):
            break
        buf.append(t); j += 1
    flush()
    return inner, j

def md_blocks(text):
    lines = text.split("\n")
    out, toc = [], []
    section = ""
    i, n = 0, len(lines)
    while i < n:
        ln = lines[i]; s = ln.strip()
        if not s:
            i += 1; continue
        if s.startswith("```"):
            buf = []; i += 1
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i]); i += 1
            i += 1
            out.append("<pre><code>" + ihtml.escape("\n".join(buf)) + "</code></pre>")
            continue
        if s == "---":
            out.append("<hr>"); i += 1; continue
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            raw = m.group(2).strip()
            title = inline(raw)
            section = raw
            lvl = 2 if len(m.group(1)) <= 2 else 3
            if raw.startswith(("🎯", "📖", "🖱️", "🧠", "⚠️", "❓", "💻", "✅")):
                lvl = 2
            toc.append((lvl, slug(raw), title))
            out.append(f'<h{lvl} class="section-title" id="{slug(raw)}">{title}</h{lvl}>')
            i += 1; continue
        if s.startswith("|"):
            buf = []
            while i < n and lines[i].strip().startswith("|"):
                buf.append(lines[i]); i += 1
            out.append(render_table_block(buf)); continue
        if LIST_RE.match(ln):
            buf = []
            while i < n and LIST_RE.match(lines[i]):
                buf.append(lines[i]); i += 1
            out.append(render_list_block(buf)); continue
        if s.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip()); i += 1
            txt = "<br>".join(inline(b) for b in buf)
            cls = "ans" if "Ans:" in txt[:60] else "tip"
            out.append(f'<div class="{cls}">{txt}</div>'); continue
        buf = []
        while i < n:
            t = lines[i].strip()
            if not t or re.match(r"^#{1,4}\s+", t) or t in ("---",) or t.startswith(("```", "|", ">")) or LIST_RE.match(lines[i]):
                break
            buf.append(t); i += 1
        if not buf:
            i += 1; continue
        if section.startswith("❓") and buf[0].startswith("**"):
            for b in buf:
                mm = re.match(r"^\*\*(.+?)\*\*\s*(.*)$", b)
                if mm:
                    out.append(f'<div class="qa"><strong>{inline(mm.group(1))}</strong><br>{inline(mm.group(2))}</div>')
                else:
                    out.append(f"<p>{inline(b)}</p>")
        else:
            out.append("<p>" + "<br>".join(inline(b) for b in buf) + "</p>")
    return "\n".join(out), toc