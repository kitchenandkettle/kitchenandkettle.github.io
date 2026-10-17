# Early Modern English Grimoire — Build

> **For Hermes:** Build directly — mirror `grimoires/celtic/` into `grimoires/english/`. Single session. Ship 150p 6x9 interior HTML + PDF.

**Goal:** Cunning-folk England 1500s-1600s. 150 pages, 6x9 KDP, black ink, no bleed, 40% reading / 60% doing. Plain 2nd-person. Every lore page carries Lore Root. Honest about Christian frame throughout.

**Directory:** `/home/chels/test/grimoires/english/`
**Reference:** `grimoires/celtic/gen_celtic.py`, `content_a.py`–`content_d.py`

## System to copy

- Tuples: `("lore", kicker, title, [p1,p2,p3, root], prompt)`, `("journal", kicker, prompt, lines)`, `("tracker", kicker, prompt, [rows])`
- 3 paras + Root per lore. Body 1300-1750 chars. Title pp1-6 same shape.
- CSS copy from `gen_celtic.py:148-182`. `.page{6in 9in overflow:hidden}`, folio 1-150 sequential. Output `english-grimoire.html`, PDF 432x648pts.

## Rules

- Labels Attested / Folk / Reconstructed / Modern every Root. No unbroken lineage. Trial pamphlets are hostile sources, label so.
- Christian frame stays. Charms name Christ/saints/psalms. Give adaptation note: keep line or swap witness, record swap. No pagan-wash.
- Safety verbatim pp4 + ch6: bought herbs only, expert ID, check meds/pregnancy, no poisons, no flame unattended.
- Ward/bless only. Refusal rules: no harm, no coerced love, no theft-finding that accuses.
- Shape per lore: P1 scene from record/herbal, P2 household meaning, P3 under-an-hour doing with modern hands.

## Spines — do not drop

- Danger/reputation ch4: rates, client book, church attendance, what you refuse. Fear of accusation is the engine.
- Women's work: birth/aftercare, breasts, sick children in ch6; churching grief in ch9.
- Nine Herbs Old Roots x3 in ch6 only: Lacnunga 10th c Attested, Gerard/Culpeper 1600s bridge, your cup Modern. Never imply continuous use.
- Modern bridges: hands (garden/cook/sweep), words (copy/speak), neighbor-work (help/log/charge). No pretending to be 1600s.

## Map — 144 + 6 = 150

1. Threshold 7-14. 2. Seen/Unseen 15-30 + veil walk, dream x7. 3. God/Saints/Neighbors 31-60 + altar, log. 4. Trials/Name 61-74 + client book, refusal drill, tracker 1-14/15-30. 5. Parish Year 75-98 + attendance, seasonal calendar. 6. Herbs/Physic 99-118 + Nine Herbs x3, garden, birth bag, dose book. 7. Wells/Roads/Doors/Night 119-132 + keeping log, 3-day sit, almanac. 8. Charms 133-142 + copy-book, 3 makings, 2-week tracker. 9. Dead/Ghosts 143-147 + cards x2, letter/roll. 10. Oath 148-150 + vow, 30-day tracker, reading list.

## Sources first-hand

Lacnunga (Nine Herbs, Wið færstice — CELT/early English text), Bald's Leechbook, Gerard Herball 1597, Culpeper English Physitian 1652, Essex/Somerset trial pamphlets (hostile), church court records overview, parish calendar. Rune/ogham equivalents: almanacprognostications. Modern: circle-casting, crystal correspondences — label Modern, cut.

## Tasks

1. Scaffold `grimoires/english/` from celtic pattern. 2. CH1-CH4. 3. CH5-CH6 with Nine Herbs + women's work. 4. CH7-CH10. 5. Build: `python3 gen_english.py` → 150 divs, folios sequential, no clip, PDF 150p.

Accept: reads aloud clean, labels intact, interactive > informative, 150p intact.
