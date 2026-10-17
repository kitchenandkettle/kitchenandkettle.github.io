#!/usr/bin/env python3
"""Old Norse Grimoire generator — 6x9 KDP interior, 145 pages, black ink, no bleed.
Content: Vol I, Norse system mirroring Celtic. 40% reading / 60% doing.
Voice: plain, 2nd-person. Every lore page carries a Lore Root line.
"""
import html as H
import re
import sys
sys.path.insert(0, "/home/chels/test/grimoires/norse")
from content_a import CH1, CH2
from content_b import CH3, CH3B, CH4B, CH4C
from content_c import CH5, CH6
from content_d import CH7, CH8, CH9, CH10
from content_e import CH_ED


def lore_page(num, kicker, title, paras, prompt):
    ps = "\n".join(f"<p>{p}</p>" for p in paras)
    return f"""<div class="page">
<div class="inner">
<div class="kicker">{H.escape(kicker)}</div>
<h2>{H.escape(title)}</h2>
<div class="rule"></div>
{ps}
<div class="prompt"><div class="prompt-label">Grimoire prompt</div><div class="prompt-text">{H.escape(prompt)}</div></div>
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


def valknut_inline(prefix, size, color="#1A1512"):
    from pathlib import Path
    svg = (Path(__file__).parent / "valknut.svg").read_text(encoding="utf-8")
    svg = re.sub(r"<title>.*?</title>\s*", "", svg)
    svg = svg.replace("#1A1512", color)
    svg = svg.replace('id="m', f'id="{prefix}m').replace("url(#m", f"url(#{prefix}m")
    svg = svg.replace('width="200" height="200"', f'width="{size}" height="{size}" style="display:block;margin:0 auto 0.2in auto;" role="img" aria-label="Valknut"', 1)
    return svg.strip()


def title_pages():
    p1 = f"""<div class="page"><div class="inner center">
{valknut_inline("t", 60)}
<div class="kicker">A Grimoire of the Old Religions &middot; Vol. I</div>
<h1>The Old Norse<br>Grimoire</h1>
<div class="rule"></div>
<p class="subtitle">A window to the old world, gods,<br>oath &amp; craft</p>
<div class="folio">1</div>
</div></div>"""
    p2 = """<div class="page"><div class="inner center">
<div class="kicker">Dedication</div>
<div class="rule"></div>
<p class="subtitle">For Huginn and Muninn.<br>While they return to Óðinn each night, may they also return to us as well.</p>
<div class="folio">2</div>
</div></div>"""
    p3 = """<div class="page"><div class="inner">
<div class="kicker">The Path We Will Walk Together</div>
<h2>Contents</h2>
<div class="rule"></div>
<div class="toc">
<p><b>1. Welcome</b>: Working with the Old Ways &middot; 4&ndash;5</p>
<p><b>2. Threshold</b>: Who Were the Old Norse &middot; 6&ndash;11</p>
<p><b>3. Nine Realms</b>: The Gods and Their Kingdoms &middot; 12&ndash;22</p>
<p><b>4. Rǫgn</b>: Gods &amp; Ruling Powers &middot; 23&ndash;44</p>
<p><b>5. Völva &amp; Seiðr</b>: seeress and fate-work &middot; 45&ndash;48</p>
<p><b>6. Hamingja</b>: your luck &middot; 49&ndash;52</p>
<p><b>7. Vitki</b>: rune-reader &middot; 53&ndash;54</p>
<p><b>8. Elves &amp; Dwarfs</b>: neighbors and smiths &middot; 55&ndash;65</p>
<p><b>9. Norse Wheel of the Year</b>: Winter Nights to Midsummer &middot; 66&ndash;87</p>
<p><b>10. Plants &amp; Trees</b>: herbs and ash &middot; 88&ndash;106</p>
<p><b>11. Liminal Places</b>: wells that remember &middot; 107&ndash;115</p>
<p><b>12. Runes</b>: stones with staves &middot; 116&ndash;118</p>
<p><b>13. Staves</b>: use them honestly &middot; 119&ndash;124</p>
<p><b>14. Galdr: Charms</b>: words in old books &middot; 125&ndash;135</p>
<p><b>15. Ancestors</b>: mound-neighbors &middot; 136&ndash;141</p>
<p><b>16. Oath</b>: go on reading &middot; 142&ndash;145</p>
</div>
<div class="folio">3</div>
</div></div>"""
    p4 = """<div class="page"><div class="inner center">
<h1 style="font-size:30pt">Welcome</h1>
<div class="rule"></div>
<p class="subtitle">Working with the Old Ways</p>
<div class="folio">4</div>
</div></div>"""
    p5 = """<div class="page"><div class="inner">
<div class="kicker">Welcome</div>
<h2>Working with the Old Ways</h2>
<div class="rule"></div>
<p>Rest your tired bones and troubled mind. This book shares the old Norse ways, which were about keeping good company with the living, the dead, and the land. It is meant to bring you comfort and a sense of connection with your ancestors. If parts of it do not fit your life or beliefs, leave them behind and keep what helps. I have tried to present these old ways as accurately as the sources allow, and I mark each claim with where it comes from. Use the lines on each page to write, reflect, and build your own practice in whatever way works best for you.</p>
<p>This book covers medicinal plants, but it does not replace a doctor. Never eat, drink, or apply any plant from these pages based on this book alone. If you forage, go with an experienced guide, check each plant against at least three trusted sources, and take only what you need, leaving most of it behind. For medicinal herbs, I buy from Mountain Rose Herbs: https://mountainroseherbs.com/</p>
<p><b>How to read the labels.</b> Every lore page ends with a Lore Root line that says how each claim is known. <i>Attested</i> means it comes from old stones, medieval poems or sagas (named on each page), or law. <i>Folk</i> means custom that survived in farm and village life, often long after the Viking Age. <i>Reconstructed</i> means a practice this book builds from old patterns. <i>Modern</i> means written today for your home. The main sources are the Poetic Edda, Snorri Sturluson’s Prose Edda, the medieval rune poems, and the sagas listed in Resources.</p>
<div class="prompt"><div class="prompt-label">Grimoire prompt</div><div class="prompt-text">What season is it today, outside your actual window? Name three signs.</div></div>
<div class="folio">5</div>
</div></div>"""
    return [p1, p2, p3, p4, p5]


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
    if kind == "resources":
        _, kicker, title = entry
        return resources_page(num, kicker, title)
    raise ValueError(f"unknown page kind {kind}")


RESOURCES = [
    ("Primary sources, in translation", [
        "The Poetic Edda — trans. Carolyne Larrington, or trans. Jackson Crawford (Hackett, 2015).",
        "Snorri Sturluson, The Prose Edda — trans. Anthony Faulkes.",
        "Völsunga Saga (The Saga of the Völsungs) — trans. Jesse Byock; trans. Jackson Crawford.",
        "Egils saga — in translation.",
        "The rune poems: Norwegian, Icelandic, Anglo-Saxon — in translation.",
    ]),
    ("Witnesses, histories, law", [
        "Tacitus, Germania.",
        "Ibn Fadlan, account of the Rus burial on the Volga.",
        "Adam of Bremen, Gesta Hammaburgensis Ecclesiae Pontificum.",
        "Landnámabók.",
        "Grágás (the Grey Goose Laws).",
        "Sigvatr Þórðarson, Austrfararvísur.",
        "Ynglinga Saga.",
        "The Merseburg Charms.",
        "Old English leechbooks.",
    ]),
    ("Scholarship and teaching", [
        "Jackson Crawford — YouTube channel: Norse mythology, language, sagas, and culture.",
        "Luthien Cangemi — The Art of Healing in Medieval Iceland, PhD thesis, UCL, 2024.",
        "Carl-Herman Tillhagen — Swedish folk custom records.",
    ]),
]


def resources_page(num, kicker, title):
    parts = []
    for group, items in RESOURCES:
        parts.append(f"<p><b>{H.escape(group)}</b></p>")
        parts.extend(f"<p>{H.escape(it)}</p>" for it in items)
    return f"""<div class="page">
<div class="inner">
<div class="kicker">{H.escape(kicker)}</div>
<h2>{H.escape(title)}</h2>
<div class="rule"></div>
<div class="toc">{''.join(parts)}</div>
<div class="folio">{num}</div>
</div>
</div>"""


def divider_page(num, kicker, title, sub):
    return f"""<div class="page"><div class="inner center">
<h1 style="font-size:30pt">{H.escape(title)}</h1>
<div class="rule"></div>
<p class="subtitle">{H.escape(sub)}</p>
<div class="folio">{num}</div>
</div></div>"""


def blank_page(num):
    return f"""<div class="page"><div class="inner">
<div class="folio">{num}</div>
</div></div>"""


def build():
    pages = []
    pages += title_pages()  # 1-5
    n = 6
    sections = [
        ("Threshold", "Threshold", "Who were the Old Norse", CH1),
        ("Nine Realms", "Nine Realms", "The Gods and Their Kingdoms", CH2),
        ("Gods & Ruling Powers", "Rǫgn: Gods & Ruling Powers", "Aesir & Vanir", CH3),
        ("Völva & Seiðr", "Völva & Seiðr", "seeress and fate-work", CH3B),
        ("Hamingja", "Hamingja", "your luck", CH4C),
        ("Vitki", "Vitki", "rune-reader", CH4B),
        ("Elves & Dwarfs", "Elves & Dwarfs", "neighbors and smiths", CH_ED),
        ("Norse Wheel of the Year", "Norse Wheel of the Year", "Winter Nights to Midsummer", CH5),
        ("Plants & Trees", "Plants & Trees", "Herbs and ash", CH6),
        ("Liminal Places", "Liminal Places", "Wells that remember", [e for e in CH7 if e[1] == "Liminal Places"]),
        ("Runes", "Runes", "Stones with staves", [e for e in CH7 if e[1] == "Runes"]),
        ("Staves", "Staves", "use them honestly", [e for e in CH7 if e[1] != "Liminal Places" and e[1] != "Runes"]),
        ("Galdr: Charms", "Galdr: Charms", "Words in old books", CH8),
        ("Ancestors", "Ancestors", "Mound-neighbors", CH9),
        ("Oath", "Oath", "Go on reading", CH10),
    ]
    for kicker, title, sub, ch in sections:
        pages.append(divider_page(n, kicker, title, sub))
        n += 1
        for entry in ch:
            pages.append(render(entry, n))
            n += 1
        if kicker == "Staves":
            pages.append(blank_page(n))
            n += 1
    assert len(pages) == 145, f"got {len(pages)} pages, need 145"
    assert n - 1 == 145, f"last folio {n - 1}, need 145"
    return pages


CSS = """
@page { size: 6in 9in; margin: 0; }
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; background: #fff; color: #1A1512; }
body { font-family: 'EB Garamond', Georgia, 'Times New Roman', serif; }
@media screen {
  html, body { background: #2b2721; }
  body { padding: 24px 0; }
  .page { margin: 0 auto 24px auto; box-shadow: 0 4px 24px rgba(0,0,0,.45); }
}
.page { width: 6in; height: 9in; page-break-after: always; break-after: page; overflow: hidden; background: #fff; }
.page:last-child { page-break-after: auto; break-after: auto; }
.inner { position: relative; height: 100%; padding-top: 0.42in; padding-bottom: 0.37in; }
.page:nth-child(odd) .inner { padding-left: 0.65in; padding-right: 0.5in; }
.page:nth-child(even) .inner { padding-left: 0.5in; padding-right: 0.65in; }
.kicker { font-size: 12pt; letter-spacing: 0.14em; text-transform: uppercase; color: #9C958E; margin-bottom: 0.12in; }
h1 { font-size: 34pt; line-height: 1.05; margin: 0.1in 0 0.15in 0; font-weight: 700; }
h2 { font-size: 16pt; line-height: 1.25; margin: 0 0 0.12in 0; }
.rule { border-top: 2px solid #1A1512; border-bottom: 1px solid #8A7D6B; height: 5px; margin: 0.1in 0 0.14in 0; }
p { font-size: 12pt; line-height: 1.35; margin: 0 0 0.1in 0; text-align: justify; hyphens: auto; }
.subtitle { font-size: 12pt; text-align: center; line-height: 1.5; }
.edition { font-size: 12pt; color: #5A4F43; text-align: center; margin-top: 0.2in; }
.center { text-align: center; display: flex; flex-direction: column; justify-content: center; }
.center p { text-align: center; }
.toc p { font-size: 12pt; text-align: left; margin-bottom: 0.08in; }
.prompt { background: #F4EFE6; border: 1px solid #8A7D6B; border-left: 4px solid #1A1512; padding: 0.07in 0.1in; margin: 0.1in 0; }
.prompt-label { font-size: 12pt; letter-spacing: 0.14em; text-transform: uppercase; color: #5A4F43; margin-bottom: 0.06in; }
.prompt-text { font-size: 12pt; font-style: italic; line-height: 1.35; }
.jprompt { font-size: 12pt; font-style: italic; line-height: 1.4; margin-bottom: 0.05in; }
.lines span { display: block; height: 0.22in; border-bottom: 1px solid #B9AE9E; }
.lines.tall span { height: 0.28in; }
.track .trow { display: flex; gap: 0.08in; align-items: baseline; min-height: 0.28in; border-bottom: 1px solid #B9AE9E; font-size: 12pt; line-height: 1.35; padding: 0.02in 0; }
.track .box { font-size: 12pt; }
.folio { position: absolute; bottom: 0.3in; left: 0; right: 0; text-align: center; font-size: 12pt; color: #5A4F43; }
"""


def main():
    pages = build()
    doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>The Old Norse Grimoire — KDP interior</title>
<style>{CSS}</style></head>
<body>
{''.join(pages)}
</body></html>"""
    with open("norse-grimoire.html", "w") as f:
        f.write(doc)
    print(f"wrote norse-grimoire.html with {len(pages)} .page divs")


if __name__ == "__main__":
    main()
