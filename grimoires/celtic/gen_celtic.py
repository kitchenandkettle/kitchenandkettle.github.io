#!/usr/bin/env python3
"""Celtic Grimoire generator — 6x9 KDP interior, 150 pages, black ink, no bleed.
Content: Opencode draft v3 structure (10 chapters), fleshed out. 40% reading / 60% doing.
Voice: plain, 2nd-person. Every lore page carries a Lore Root line.
"""
import html as H
import sys
sys.path.insert(0, "/home/chels/test/grimoires/celtic")
from content_a import CH1, CH2
from content_b import CH3, CH4
from content_c import CH5, CH6
from content_d import CH7, CH8, CH9, CH10


def lore_page(num, kicker, title, paras, prompt):
    ps = "\n".join(f"<p>{p}</p>" for p in paras)
    return f"""<div class="page">
<div class="inner">
<div class="kicker">{H.escape(kicker)}</div>
<h2>{H.escape(title)}</h2>
<div class="rule"></div>
{ps}
<div class="prompt"><div class="prompt-label">Grimoire prompt</div><div class="prompt-text">{H.escape(prompt)}</div></div>
<div class="lines"><span></span><span></span><span></span></div>
<div class="folio">{num}</div>
</div>
</div>"""


def journal_page(num, kicker, prompt_text, lines=14):
    ls = "".join("<span></span>" for _ in range(lines))
    return f"""<div class="page">
<div class="inner">
<div class="kicker">{H.escape(kicker)}</div>
<div class="jprompt">{H.escape(prompt_text)}</div>
<div class="rule"></div>
<div class="lines tall">{ls}</div>
<div class="folio">{num}</div>
</div>
</div>"""


def tracker_page(num, kicker, prompt_text, rows):
    rs = "".join(f"<div class=\"trow\"><span class=\"box\">&#9744;</span><span>{H.escape(r)}</span></div>" for r in rows)
    return f"""<div class="page">
<div class="inner">
<div class="kicker">{H.escape(kicker)}</div>
<div class="jprompt">{H.escape(prompt_text)}</div>
<div class="rule"></div>
<div class="track">{rs}</div>
<div class="folio">{num}</div>
</div>
</div>"""


def title_pages():
    p1 = """<div class="page"><div class="inner center">
<div class="kicker">A Grimoire of the Old Religions &middot; Vol. II</div>
<h1>The Celtic<br>Grimoire</h1>
<div class="rule"></div>
<p class="subtitle">A journal of land, season,<br>ancestor &amp; craft</p>
<p class="edition">Black-ink edition &middot; 6 &times; 9 in &middot; 150 pages</p>
<div class="folio">1</div>
</div></div>"""
    p2 = """<div class="page"><div class="inner center">
<div class="kicker">Dedication</div>
<div class="rule"></div>
<p class="subtitle">For the ones who kept the wells clean<br>and the doors open.</p>
<p class="edition">Write your own dedication below.</p>
<div class="lines"><span></span><span></span><span></span><span></span></div>
<div class="folio">2</div>
</div></div>"""
    p3 = """<div class="page"><div class="inner">
<div class="kicker">Contents</div>
<h2>Contents</h2>
<div class="rule"></div>
<div class="toc">
<p><b>1. Threshold</b> &middot; 7&ndash;14</p>
<p><b>2. Otherworld Next Door</b> &middot; 15&ndash;30</p>
<p><b>3. Gods &amp; Neighbors</b> &middot; 31&ndash;60</p>
<p><b>4. Heroes &amp; Your Geis</b> &middot; 61&ndash;74</p>
<p><b>5. Wheel of Four Fires</b> &middot; 75&ndash;98</p>
<p><b>6. Plants of Medicine &amp; Ritual</b> &middot; 99&ndash;118</p>
<p><b>7. Wells, Fords, Doorways, Dawn &amp; Dusk</b> &middot; 119&ndash;132</p>
<p><b>8. Charms &amp; Protective Workings</b> &middot; 133&ndash;142</p>
<p><b>9. Ancestors &amp; the Dead</b> &middot; 143&ndash;147</p>
<p><b>10. Your Oath</b> &middot; 148&ndash;150</p>
</div>
<div class="folio">3</div>
</div></div>"""
    p4 = """<div class="page"><div class="inner">
<div class="kicker">How to use</div>
<h2>How to use this book</h2>
<div class="rule"></div>
<p>Come in and make yourself at home, because this book works the way a good visit does. You read a little and then you do a little, and then you write a little, and that rhythm carries the whole book. Short passages open each part while the practices fit inside an hour, and the lined pages take the rest, so date every entry and watch your year turn in your own hand.</p>
<p>Take safety as part of the welcome and keep it always. Safety first, always. Never ingest yew, mistletoe, or selago in any form. No wild plant identification without an expert beside you — store-bought teas only. Check every herb against your medicines and, if relevant, pregnancy with a clinician. Never leave flame unattended.</p>
<div class="prompt"><div class="prompt-label">Grimoire prompt</div><div class="prompt-text">What season is it today, outside your actual window? Name three signs.</div></div>
<div class="lines"><span></span><span></span><span></span></div>
<div class="folio">4</div>
</div></div>"""
    p5 = """<div class="page"><div class="inner">
<div class="kicker">Map</div>
<h2>Three windows</h2>
<div class="rule"></div>
<p><b>Gaul</b> — roughly today's France and beyond: hillforts, the Coligny bronze, short votive inscriptions in a Celtic tongue, gods known mostly by name and image.</p>
<p><b>Ireland</b> — the four fires, the Tuatha De Danann, the Ulster heroes, Brehon laws, wells still visited: stories written down by Christians, customs kept by families.</p>
<p><b>Wales</b> — the Mabinogi's four branches, Annwn the deep place, Rhiannon's birds: a smaller window, and no less strange for it.</p>
<div class="prompt"><div class="prompt-label">Grimoire prompt</div><div class="prompt-text">Mark your own spot on the map in words. Where do you stand, reading this?</div></div>
<div class="lines"><span></span><span></span><span></span></div>
<div class="folio">5</div>
</div></div>"""
    p6 = """<div class="page"><div class="inner">
<div class="kicker">Yours</div>
<div class="jprompt">This grimoire belongs to ___ . I open it on ___ , intending ___ .</div>
<div class="rule"></div>
<div class="lines tall"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>
<div class="folio">6</div>
</div></div>"""
    return [p1, p2, p3, p4, p5, p6]


def render(entry, num):
    kind = entry[0]
    if kind == "lore":
        _, kicker, title, paras, prompt = entry
        return lore_page(num, kicker, title, paras, prompt)
    if kind == "journal":
        _, kicker, prompt, lines = entry
        return journal_page(num, kicker, prompt, lines)
    if kind == "tracker":
        _, kicker, prompt, rows = entry
        return tracker_page(num, kicker, prompt, rows)
    raise ValueError(f"unknown page kind {kind}")


def build():
    pages = []
    pages += title_pages()  # 1-6
    n = 7
    for entry in CH1 + CH2 + CH3 + CH4 + CH5 + CH6 + CH7 + CH8 + CH9 + CH10:
        pages.append(render(entry, n))
        n += 1
    assert len(pages) == 150, f"got {len(pages)} pages, need 150"
    assert n - 1 == 150, f"last folio {n - 1}, need 150"
    return pages


CSS = """
@page { size: 6in 9in; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: #fff; color: #1A1512; }
body { font-family: Georgia, 'Times New Roman', serif; }
@media screen {
  html, body { background: #2b2721; }
  body { padding: 24px 0; }
  .page { margin: 0 auto 24px auto; box-shadow: 0 4px 24px rgba(0,0,0,.45); }
}
.page { width: 6in; height: 9in; page-break-after: always; break-after: page; overflow: hidden; background: #fff; }
.page:last-child { page-break-after: auto; break-after: auto; }
.inner { position: relative; height: 100%; padding-top: 0.6in; padding-bottom: 0.55in; }
.page:nth-child(odd) .inner { padding-left: 0.65in; padding-right: 0.5in; }
.page:nth-child(even) .inner { padding-left: 0.5in; padding-right: 0.65in; }
.kicker { font-size: 8pt; letter-spacing: 0.14em; text-transform: uppercase; color: #5A4F43; margin-bottom: 0.12in; }
h1 { font-size: 34pt; line-height: 1.05; margin: 0.1in 0 0.15in 0; font-weight: 700; }
h2 { font-size: 16pt; line-height: 1.2; margin: 0 0 0.1in 0; }
.rule { border-top: 2px solid #1A1512; border-bottom: 1px solid #8A7D6B; height: 5px; margin: 0.1in 0 0.14in 0; }
p { font-size: 9.5pt; line-height: 1.45; margin: 0 0 0.09in 0; text-align: justify; }
.subtitle { font-size: 11pt; text-align: center; line-height: 1.5; }
.edition { font-size: 8.5pt; color: #5A4F43; text-align: center; margin-top: 0.2in; }
.center { text-align: center; display: flex; flex-direction: column; justify-content: center; }
.center p { text-align: center; }
.toc p { font-size: 9.5pt; text-align: left; margin-bottom: 0.06in; }
.prompt { background: #F4EFE6; border: 1px solid #8A7D6B; border-left: 4px solid #1A1512; padding: 0.1in 0.12in; margin: 0.12in 0; }
.prompt-label { font-size: 7.5pt; letter-spacing: 0.14em; text-transform: uppercase; color: #5A4F43; margin-bottom: 0.04in; }
.prompt-text { font-size: 9.5pt; font-style: italic; line-height: 1.4; }
.jprompt { font-size: 12pt; font-style: italic; line-height: 1.4; margin-bottom: 0.05in; }
.lines span { display: block; height: 0.26in; border-bottom: 1px solid #B9AE9E; }
.lines.tall span { height: 0.30in; }
.track .trow { display: flex; gap: 0.08in; align-items: baseline; min-height: 0.30in; border-bottom: 1px solid #B9AE9E; font-size: 9.5pt; line-height: 1.4; padding: 0.02in 0; }
.track .box { font-size: 11pt; }
.folio { position: absolute; bottom: 0.3in; left: 0; right: 0; text-align: center; font-size: 8.5pt; color: #5A4F43; }
"""


def main():
    pages = build()
    doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>The Celtic Grimoire — 6x9 KDP interior</title>
<style>{CSS}</style></head>
<body>
{''.join(pages)}
</body></html>"""
    with open("celtic-grimoire.html", "w") as f:
        f.write(doc)
    print(f"wrote celtic-grimoire.html with {len(pages)} .page divs")


if __name__ == "__main__":
    main()
