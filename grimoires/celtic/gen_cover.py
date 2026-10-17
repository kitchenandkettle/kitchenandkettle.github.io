#!/usr/bin/env python3
"""Celtic Grimoire cover generator — KDP paperback, 6x9, 150 pages, cream paper."""
PAGE_COUNT = 150
TRIM_W = 6.0
TRIM_H = 9.0
BLEED = 0.125
SPINE = PAGE_COUNT * 0.0025  # cream paper
TOTAL_W = TRIM_W * 2 + SPINE + BLEED * 2
TOTAL_H = TRIM_H + BLEED * 2

BLACK = "#14110D"
PAPER = "#E8E0D0"
MUTED = "#A89A7E"
GOLD = "#C4A882"
RULE = "#4A4335"

KNOT = """<img src="triple-spiral-light.png" width="64" height="64" alt="Triple spiral" style="display:block;margin:0 auto;" />"""

HTML = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>The Celtic Grimoire — cover</title>
<style>
@page {{ size: {TOTAL_W}in {TOTAL_H}in; margin: 0; }}
* {{ box-sizing: border-box; }}
html, body {{ margin: 0; padding: 0; background: {BLACK}; color: {PAPER}; }}
body {{ font-family: Georgia, 'Times New Roman', serif; }}
@media screen {{
  html, body {{ background: #2b2721; }}
  body {{ padding: 24px 0; }}
  .cover {{ margin: 0 auto; box-shadow: 0 4px 24px rgba(0,0,0,.5); }}
}}
.cover {{
  width: {TOTAL_W}in; height: {TOTAL_H}in;
  display: flex; flex-direction: row;
  background: {BLACK}; color: {PAPER};
  overflow: hidden; page-break-after: avoid;
}}
.bleed-note {{ display: none; }}
.back, .front {{
  width: {TRIM_W}in; height: {TOTAL_H}in;
  padding: 0.75in 0.6in;
  display: flex; flex-direction: column;
}}
.spine {{
  width: {SPINE}in; height: {TOTAL_H}in;
  display: flex; align-items: center; justify-content: center;
  border-left: 1px solid {RULE}; border-right: 1px solid {RULE};
}}
.spine-text {{
  writing-mode: vertical-rl;
  font-size: 11pt; letter-spacing: 0.18em; text-transform: uppercase;
  color: {PAPER}; white-space: nowrap;
}}
.kicker {{ font-size: 8pt; letter-spacing: 0.16em; text-transform: uppercase; color: {MUTED}; margin-bottom: 0.15in; }}
.back h2 {{ font-size: 16pt; font-weight: 400; margin: 0 0 0.12in 0; line-height: 1.3; }}
.back p {{ font-size: 9.5pt; line-height: 1.55; margin: 0 0 0.1in 0; color: {PAPER}; }}
.back .bullets {{ margin: 0.12in 0; padding: 0; list-style: none; }}
.back .bullets li {{ font-size: 9.5pt; line-height: 1.5; margin-bottom: 0.05in; padding-left: 0.18in; position: relative; }}
.back .bullets li::before {{ content: "—"; position: absolute; left: 0; color: {GOLD}; }}
.back .foot {{ margin-top: auto; font-size: 8pt; letter-spacing: 0.12em; text-transform: uppercase; color: {MUTED}; }}
.tri {{ font-size: 26pt; color: {GOLD}; margin-bottom: 0.15in; }}
.front {{ text-align: center; align-items: center; justify-content: center; }}
.front .series {{ font-size: 8.5pt; letter-spacing: 0.2em; text-transform: uppercase; color: {MUTED}; margin-bottom: 0.38in; }}
.front .tri {{ margin-top: 0; margin-bottom: 0.12in; }}
.front h1 {{ font-size: 38pt; line-height: 1.05; margin: 0 0 0.15in 0; font-weight: 700; color: {PAPER}; }}
.front .rule {{ width: 1.5in; border-top: 1px solid {GOLD}; border-bottom: 1px solid {RULE}; height: 4px; margin: 0.12in auto 0.15in auto; }}
.front .sub {{ font-size: 11pt; font-style: italic; color: {PAPER}; line-height: 1.5; }}
.front .ed {{ margin-top: 0.25in; font-size: 8.5pt; letter-spacing: 0.14em; text-transform: uppercase; color: {MUTED}; }}
</style></head>
<body>
<div class="cover">
  <div class="back">
    <div class="tri">{KNOT}</div>
    <div class="kicker">A Grimoire of the Old Religions &middot; Vol. II</div>
    <h2>A working journal of land, season, ancestor &amp; craft.</h2>
    <p>Short passages open each section. Prompts and lined pages do the rest. Write in it. Date your entries. Cross things out.</p>
    <ul class="bullets">
      <li>The Four Fires, kept the Irish way</li>
      <li>Twelve gods, heroes, and your own geis</li>
      <li>Plants, wells, ogham, and the triskele</li>
      <li>Charms, ancestors, and your oath</li>
    </ul>
    <p>Honest about sources. Nothing here claims a closed lineage. Take what fits a full modern life. Leave the rest.</p>
    <div class="foot">Black-ink edition &middot; 6 x 9 in &middot; 150 pages</div>
  </div>
  <div class="spine"><div class="spine-text">The Celtic Grimoire &middot; Vol. II</div></div>
  <div class="front">
    <div class="series">A Grimoire of the Old Religions &middot; Vol. II</div>
    <div class="tri">{KNOT}</div>
    <h1>The Celtic<br>Grimoire</h1>
    <div class="rule"></div>
    <div class="sub">A journal of land, season,<br>ancestor &amp; craft</div>
    <div class="ed">Black-ink edition</div>
  </div>
</div>
</body></html>
"""

with open("celtic-grimoire-cover.html", "w") as f:
    f.write(HTML)
print(f"wrote cover {TOTAL_W:.3f} x {TOTAL_H:.3f} in, spine {SPINE:.4f} in (cream, {PAGE_COUNT} pp)")
