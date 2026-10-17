#!/usr/bin/env python3
"""Old Norse Grimoire generator — 6x9 KDP interior, 150 pages, black ink, no bleed.
Content: Vol I, Norse system mirroring Celtic. 40% reading / 60% doing.
Voice: plain, 2nd-person. Every lore page carries a Where-this-comes-from line.
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
from content_g import RUNE_PAGES, STAVE_PAGES, SEIDR_PAGES, RUNE_NOTEBOOK
from content_f import CH_POEMS, CH_WELCOME, GODS_GLANCE, NEW_SONGS, NEW_VITKI, NEW_COUNSEL, VOLUSPA_PAGE, FRIENDS_PAGE, TALES, NEW_PLANTS, TREES_RUNE, GIANTS_PAGE, GLOSSARY_PAGE


def aegis_svg():
    import math
    parts = ['<svg viewBox="-100 -100 200 200" width="130" height="130" xmlns="http://www.w3.org/2000/svg" style="display:inline-block" role="img" aria-label="Helm of Awe, simplified"><g fill="none" stroke="#1A1512" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">']
    parts.append('<circle r="6"/>')
    for k in range(8):
        a = math.radians(k * 45)
        def pt(r, da=0.0):
            return (r * math.cos(a + da), r * math.sin(a + da))
        x0, y0 = pt(10)
        x1, y1 = pt(62)
        parts.append(f'<line x1="{x0:.1f}" y1="{y0:.1f}" x2="{x1:.1f}" y2="{y1:.1f}"/>')
        # trident at the end: centre prong plus two angled prongs
        xe, ye = pt(86)
        parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{xe:.1f}" y2="{ye:.1f}"/>')
        for sgn in (-1, 1):
            xb, yb = pt(70, sgn * 0.0)
            xt, yt = pt(88, sgn * 0.19)
            parts.append(f'<line x1="{xb:.1f}" y1="{yb:.1f}" x2="{xt:.1f}" y2="{yt:.1f}"/>')
        # crossbar
        xa, ya = pt(40, -0.12)
        xb2, yb2 = pt(40, 0.12)
        parts.append(f'<line x1="{xa:.1f}" y1="{ya:.1f}" x2="{xb2:.1f}" y2="{yb2:.1f}"/>')
    parts.append('</g></svg>')
    return "".join(parts)


def lore_page(num, kicker, title, paras, prompt):
    ps = "\n".join(p if p.lstrip().startswith(("<table", "<div", "<svg")) else f"<p>{p}</p>" for p in paras)
    ps = ps.replace("{{AEGIS}}", aegis_svg()).replace("{{VALKNUT}}", '<div style="text-align:center">' + valknut_inline("vk", 70) + "</div>")
    prompt_box = (f'<div class="prompt"><div class="prompt-label">Grimoire prompt</div><div class="prompt-text">{H.escape(prompt)}</div></div>'
                  if prompt else "")
    return f"""<div class="page">
<div class="inner">
<div class="kicker">{H.escape(kicker)}</div>
<h2>{H.escape(title)}</h2>
<div class="rule"></div>
{ps}
{prompt_box}
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


def title_pages(toc_html):
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
    p3 = f"""<div class="page"><div class="inner">
<div class="kicker">The Path We Will Walk Together</div>
<h2>Contents</h2>
<div class="rule"></div>
<div class="toc">
{toc_html}
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
<p>This book mentions plants from folk custom and from medieval medical books, but it does not replace a doctor. Never eat, drink, or apply any plant from these pages based on this book alone. If you forage, go with an experienced guide, check each plant against at least three trusted sources, and take only what you need, leaving most of it behind. For medicinal herbs, I buy from Mountain Rose Herbs: https://mountainroseherbs.com/</p>
<p><b>Where this comes from.</b> Every lore page ends with a short note that says where its ideas come from: a poem, a saga, a stone, a custom, or this book. If a source is late, or scholars disagree, the note says so. Anything described as modern or rebuilt was written for your home and is not an old practice. The main sources are the Poetic Edda, Snorri Sturluson’s Prose Edda, the medieval rune poems, and the sagas listed in Resources.</p>
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
        "Benjamin Thorpe, Edda of Sæmund the Learned (1866) — public domain, quoted on several pages.",
        "Völsunga Saga (The Saga of the Völsungs) — trans. Jesse Byock; trans. Jackson Crawford.",
        "Egils saga — in translation.",
        "The rune poems: Norwegian, Icelandic, Anglo-Saxon — in translation.",
    ]),
    ("Witnesses, histories, law", [
        "Tacitus, Germania; Ibn Fadlan, account of the Rus burial on the Volga.",
        "Adam of Bremen, Gesta Hammaburgensis Ecclesiae Pontificum.",
        "Landnámabók; Grágás (the Grey Goose Laws).",
        "Sigvatr Þórðarson, Austrfararvísur.",
        "Ynglinga Saga; the Merseburg Charms; Old English leechbooks.",
    ]),
    ("Scholarship and teaching", [
        "Jackson Crawford — YouTube channel: Norse mythology, language, sagas, and culture.",
        "Luthien Cangemi — The Art of Healing in Medieval Iceland, PhD thesis, UCL, 2024.",
        "Ben Waggoner — Norse Magical and Herbal Healing: A Medical Book from Medieval Iceland (The Troth, 2011).",
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
    body = []
    toc = []
    n = 6
    start = 4
    for entry in CH_WELCOME:
        body.append(render(entry, n))
        n += 1
    toc.append(("Welcome", "Working with the Old Ways", start, n - 1))
    start = n
    body.append(divider_page(n, "The Poems", "The Poems", "What the old sources are"))
    n += 1
    for entry in CH_POEMS[:-1] + VOLUSPA_PAGE + CH_POEMS[-1:]:
        body.append(render(entry, n))
        n += 1
    toc.append(("The Poems", "what the sources are", start, n - 1))
    ch3 = list(CH3)
    moved = [e for e in ch3 if e[2] == "Blot: simply" or (e[0] == "tracker" and e[2].startswith("Gift log"))]
    ch3 = [e for e in ch3 if e not in moved]
    moved = [(e[0], "Norse Wheel of the Year") + tuple(e[2:]) for e in moved]
    ch5 = list(CH5)
    i_blot = next(i for i, e in enumerate(ch5) if e[2] == "How each turning works here") + 1
    ch5[i_blot:i_blot] = moved
    idx = next(i for i, e in enumerate(ch3) if e[2] == "The Æsir–Vanir war") + 1
    ch3[idx:idx] = GODS_GLANCE
    oath = FRIENDS_PAGE + NEW_COUNSEL + list(CH10)
    oath += GLOSSARY_PAGE
    vitki = [(e[0], "Runes") + tuple(e[2:]) for e in CH4B + NEW_VITKI]
    rune_all = [RUNE_PAGES[0]] + vitki + list(RUNE_PAGES[1:]) + RUNE_NOTEBOOK
    ch3b = list(CH3B)
    i_seidr = next(i for i, e in enumerate(ch3b) if e[2].startswith("Seiðr")) + 1
    ch3b[i_seidr:i_seidr] = SEIDR_PAGES
    ch2 = list(CH2)
    i_realms = next(i for i, e in enumerate(ch2) if e[2] == "The nine realms at a glance") + 1
    ch2[i_realms:i_realms] = GIANTS_PAGE
    ch6 = list(CH6)
    i_herbs = next(i for i, e in enumerate(ch6) if e[2] == "More herbs in the leechbooks") + 1
    ch6[i_herbs:i_herbs] = NEW_PLANTS
    i_trees = next(i for i, e in enumerate(ch6) if e[2].startswith("Ash")) 
    ch6[i_trees:i_trees] = TREES_RUNE
    sections = [
        ("Threshold", "Threshold", "Who were the Old Norse", CH1, "Who Were the Old Norse"),
        ("Nine Realms", "Nine Realms", "The Gods and Their Kingdoms", ch2, "The Gods and Their Kingdoms"),
        ("Gods & Ruling Powers", "Rǫgn: Gods & Ruling Powers", "Aesir & Vanir", ch3, "Gods & Ruling Powers"),
        ("Tales", "Tales", "Stories from the old books", TALES, "stories from the old books"),
        ("Völva & Seiðr", "Völva & Seiðr", "seeress and fate-work", ch3b, "seeress and fate-work"),
        ("Hamingja", "Hamingja", "your luck", CH4C, "your luck"),
        ("Elves & Dwarfs", "Elves & Dwarfs", "neighbors and smiths", CH_ED, "neighbors and smiths"),
        ("Norse Wheel of the Year", "Norse Wheel of the Year", "Winter Nights to Midsummer", ch5, "Winter Nights to Midsummer"),
        ("Plants & Trees", "Plants & Trees", "Herbs and ash", ch6, "herbs and ash"),
        ("Liminal Places", "Liminal Places", "Wells that remember", [e for e in CH7 if e[1] == "Liminal Places"], "wells that remember"),
        ("Runes", "Runes", "Stones with staves", rune_all, "stones with staves"),
        ("Staves", "Staves", "use them honestly", STAVE_PAGES, "use them honestly"),
        ("Galdr: Charms", "Galdr: Charms", "Words in old books", CH8[:1] + NEW_SONGS + CH8[1:], "words in old books"),
        ("Ancestors", "Ancestors", "Mound-neighbors", CH9, "mound-neighbors"),
        ("Oath", "Oath", "Go on reading", oath, "go on reading"),
    ]
    toc_names = {"Gods & Ruling Powers": "Rǫgn", "Elves & Dwarfs": "Elves &amp; Dwarfs"}
    for kicker, title, sub, ch, toc_sub in sections:
        start = n
        body.append(divider_page(n, kicker, title, sub))
        n += 1
        for entry in ch:
            body.append(render(entry, n))
            n += 1
        label = {"Gods & Ruling Powers": "Rǫgn"}.get(kicker, kicker)
        toc.append((label, toc_sub, start, n - 1))
    rows = []
    for i, (label, sub, a, b) in enumerate(toc, 1):
        rows.append(f"<p><b>{i}. {H.escape(label)}</b>: {H.escape(sub)} &middot; {a}&ndash;{b}</p>")
    pages = title_pages("\n".join(rows)) + body
    assert len(pages) == 150, f"got {len(pages)} pages, need 150"
    
    assert n - 1 == 150, f"last folio {n - 1}, need 150"
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

.rt { width: 100%; border-collapse: collapse; margin: 0.06in 0 0.1in 0; }
.rt td { font-size: 11pt; line-height: 1.25; padding: 0.04in 0.06in; border-bottom: 1px solid #B9AE9E; vertical-align: middle; }
.rt td.g { font-family: 'Noto Sans Runic', serif; font-size: 19pt; width: 0.5in; text-align: center; padding: 0; }
.rt td.n { font-weight: 700; width: 0.95in; }
.rt td.s { width: 0.55in; font-style: italic; }
.rt2 td { padding: 0.012in 0.06in; font-size: 10.5pt; }
.rt2 td.g { font-size: 16pt; }
.rrow { font-family: 'Noto Sans Runic', serif; font-size: 16pt; letter-spacing: 0.06em; line-height: 1.6; text-align: center; margin: 0.06in 0; }
.kvgrid { text-align: center; margin: 0.05in 0; }
.kv { display: inline-block; width: 0.62in; text-align: center; margin: 0.02in 0; font-size: 11pt; }
.kv .g { display: block; font-family: 'Noto Sans Runic', serif; font-size: 17pt; line-height: 1.15; }
.bind { position: relative; display: inline-block; font-family: 'Noto Sans Runic', serif; font-size: 44pt; width: 0.9em; height: 1.25em; margin: 0 0.12in; }
.bind span { position: absolute; left: 0; top: 0; }
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
