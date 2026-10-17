#!/usr/bin/env python3
"""Build the Celtic Grimoire foundation (6x9). Self-contained."""
import html as H
import pathlib
from content_foundation import CHAPTERS, SAMPLES

HERE = pathlib.Path(__file__).resolve().parent


def lore_page(num, kicker, title, paras, prompt):
    ps = "\n".join(p if p.lstrip().startswith(("<table", "<div")) else f"<p>{p}</p>" for p in paras)
    box = (f'<div class="prompt"><div class="prompt-label">Grimoire prompt</div><div class="prompt-text">{H.escape(prompt)}</div></div>' if prompt else "")
    return f"""<div class="page"><div class="inner"><div class="kicker">{H.escape(kicker)}</div><h2>{H.escape(title)}</h2><div class="rule"></div>
{ps}
{box}
<div class="folio">{num}</div></div></div>"""


def divider_page(num, title, sub):
    return f"""<div class="page"><div class="inner center"><h1 style="font-size:30pt">{H.escape(title)}</h1><div class="rule"></div><p class="subtitle">{H.escape(sub)}</p><div class="folio">{num}</div></div></div>"""


def plan_page(num, kicker, title, rows, note):
    items = "".join(
        f'<p class="pl"><b>{H.escape(t)}</b>{(" — " + H.escape(s)) if s else ""}<br><span class="src">{H.escape(src)}</span></p>'
        for t, s, src in rows)
    return f"""<div class="page"><div class="inner"><div class="kicker">{H.escape(kicker)}</div><h2>{H.escape(title)}</h2><div class="rule"></div>
{items}
<p class="note">{note}</p>
<div class="folio">{num}</div></div></div>"""


def build():
    body, toc = [], []
    n = 3
    book = 3  # page in the planned 150-page book where chapters start (after 3 front pages)
    for name, sub, count, replaces, plan in CHAPTERS:
        start = n
        body.append(divider_page(n, name, sub)); n += 1
        if plan:
            per = 12
            chunks = [plan[i:i + per] for i in range(0, len(plan), per)]
            for ci, ch in enumerate(chunks):
                label = "Planned pages" + (f" ({ci + 1} of {len(chunks)})" if len(chunks) > 1 else "")
                note = f"This chapter is planned at {count} pages, including its divider. Entries marked [written] appear in full later in this chapter."
                body.append(plan_page(n, name, label, ch, note)); n += 1
        for entry in SAMPLES.get(name, []):
            _, kicker, title, paras, prompt = entry
            body.append(lore_page(n, kicker, title, paras, prompt)); n += 1
        toc.append((name, sub, book, book + count - 1, start, n - 1))
        book += count
    return body, toc


CSS = """
@page { size: 6in 9in; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: #fff; color: #1A1512; }
body { font-family: 'EB Garamond', Georgia, serif; }
@media screen { html, body { background: #2b2721; } body { padding: 24px 0; } .page { margin: 0 auto 24px auto; box-shadow: 0 4px 24px rgba(0,0,0,.45); } }
.page { position: relative; width: 6in; height: 9in; page-break-after: always; break-after: page; overflow: hidden; background: #fff; }
.inner { position: relative; height: 100%; padding-top: 0.42in; padding-bottom: 0.37in; }
.page:nth-child(odd) .inner { padding-left: 0.65in; padding-right: 0.5in; }
.page:nth-child(even) .inner { padding-left: 0.5in; padding-right: 0.65in; }
.kicker { font-size: 12pt; letter-spacing: 0.14em; text-transform: uppercase; color: #9C958E; margin-bottom: 0.12in; }
h1 { font-size: 34pt; line-height: 1.05; margin: 0.1in 0 0.15in 0; font-weight: 700; }
h2 { font-size: 16pt; line-height: 1.25; margin: 0 0 0.12in 0; }
.rule { border-top: 2px solid #1A1512; border-bottom: 1px solid #8A7D6B; height: 5px; margin: 0.1in 0 0.14in 0; }
p { font-size: 12pt; line-height: 1.35; margin: 0 0 0.1in 0; text-align: justify; hyphens: auto; }
.subtitle { font-size: 12pt; text-align: center; line-height: 1.5; }
.center { text-align: center; display: flex; flex-direction: column; justify-content: center; }
.center p { text-align: center; }
.toc p { font-size: 11pt; text-align: left; margin-bottom: 0.06in; }
.prompt { background: #F4EFE6; border: 1px solid #8A7D6B; border-left: 4px solid #1A1512; padding: 0.07in 0.1in; margin: 0.1in 0; }
.prompt-label { font-size: 12pt; letter-spacing: 0.14em; text-transform: uppercase; color: #5A4F43; margin-bottom: 0.06in; }
.prompt-text { font-size: 12pt; font-style: italic; line-height: 1.35; }
.pl { font-size: 10.5pt; line-height: 1.25; margin: 0 0 0.07in 0; text-align: left; }
.pl .src { font-size: 9.5pt; color: #5A4F43; font-style: italic; }
.note { font-size: 9.5pt; color: #5A4F43; font-style: italic; text-align: left; margin-top: 0.1in; }
.rt { width: 100%; border-collapse: collapse; margin: 0.06in 0 0.1in 0; }
.rt td { font-size: 11pt; line-height: 1.25; padding: 0.04in 0.06in; border-bottom: 1px solid #B9AE9E; vertical-align: middle; }
.rt td.g { width: 0.5in; text-align: center; padding: 0; }
.rt td.og { font-family: 'Noto Sans Ogham', serif; font-size: 20pt; }
.rt td.n { font-weight: 700; width: 0.95in; }
.rt td.s { width: 0.55in; font-style: italic; }
.ogrow { font-family: 'Noto Sans Ogham', serif; font-size: 20pt; text-align: center; margin: 0.03in 0; white-space: nowrap; }
.folio { position: absolute; bottom: 0.3in; left: 0; right: 0; text-align: center; font-size: 12pt; color: #5A4F43; }
"""


def front(toc, total):
    title = """<div class="page"><div class="inner center"><div class="kicker">A Grimoire of the Old Religions · Vol. II</div><h1>The Celtic<br>Grimoire</h1><div class="rule"></div><p class="subtitle">The old ways of Ireland, Wales, and Gaul</p><div class="folio">1</div></div></div>"""
    rows = "".join(
        f'<p><b>{i}. {H.escape(name)}</b> &middot; {b - a + 1} pages &middot; begins on page {s}</p>'
        for i, (name, sub, a, b, s, e) in enumerate(toc, 1))
    contents = f"""<div class="page"><div class="inner"><div class="kicker">What is inside</div><h2>Contents</h2><div class="rule"></div><div class="toc">{rows}</div>
<p class="note">The book is planned at 150 pages, and page counts are the planned lengths. Chapters with a plan page list what each page will cover, and the pages written so far follow it.</p><div class="folio">2</div></div></div>"""
    return [title, contents]


if __name__ == "__main__":
    body, toc = build()
    total = 2 + len(body)
    pages = front(toc, total) + body
    doc = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>The Celtic Grimoire</title><style>{CSS}</style></head><body>{''.join(pages)}</body></html>"""
    (HERE / "celtic-grimoire-foundation.html").write_text(doc, encoding="utf-8")
    print("pages:", len(pages))
