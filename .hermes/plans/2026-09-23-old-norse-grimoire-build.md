# Old Norse Grimoire — Build

> **For Hermes:** Build directly — mirror `grimoires/celtic/` into `grimoires/norse/`. Single session, no subagents. Ship 150p 6x9 interior HTML + PDF.

**Goal:** A second volume matching Celtic Grimoire's system: 150 pages, 6x9 KDP interior, black ink, no bleed, 40% reading / 60% doing. Plain 2nd-person, kitchen-table smart. Every lore page carries a Lore Root. Honest about sources throughout.

**Directory:** `/home/chels/test/grimoires/norse/`
**Reference:** `/home/chels/test/grimoires/celtic/gen_celtic.py`, `content_a.py`, `content_b.py`, `content_c.py`, `content_d.py`, `celtic-grimoire.html`

---

## System to copy exactly

- Tuple formats: `("lore", kicker, title, [p1,p2,p3, root], prompt)`, `("journal", kicker, prompt, lines)`, `("tracker", kicker, prompt, [rows])`
- 3 paras + Root per lore page. Body 1300-1750 chars total. Root verbatim last para.
- Title pp1-6 same shape: title, dedication, Contents, How to use + safety, Map/Three windows, Yours belongs-to page.
- CSS: copy from `gen_celtic.py:148-182`. `.page{width:6in;height:9in;overflow:hidden}`, `.inner` paddings, `.folio` absolute, odd/even inside margins. `@page{size:6in 9in;margin:0}`.
- Build assert: 150 `.page` divs, folios 1-150 sequential. Output `norse-grimoire.html`, PDF 432x648pts via Chromium.
- Serve check: `http://localhost:8091/norse-grimoire.html`

## Voice / rules — same as Celtic

- Warm flat affect. Varied rhythm, read-aloud test. No guru language, no curses/hexes to send out — ward/bless only.
- Cultures kept separate: Norse (Viking Age Scandinavia/Iceland) is not Celtic, not Anglo-Saxon, not modern Asatru synthesis. Say which window each page looks through.
- Labels: Attested / Folk survival / Reconstructed / Modern on every Root. No druid-manual-style claims here either: no unbroken lineage, Eddas are Christian-era manuscripts.
- Safety verbatim on pp4 + plant chapter: bought teas only, expert ID only, check meds/pregnancy, no flame unattended, no wild-water drinking, leave-no-trace outdoors.
- Shape per lore: P1 scene/story with one concrete image, P2 what it means in household terms, P3 practice bridge under an hour in a flat.

## 10-chapter map — 144 content pages + 6 title = 150

1. Threshold pp7-14: what Norse means (language family, Viking Age, runestones/burials vs Eddas/sagas), what this book is not, Three-part check-in (use attested frame, e.g. land/sea/sky equivalent only if sourced — else build plain breath/count practice and label Modern).
2. Worlds Next Door pp15-30: Yggdrasil, Nine Worlds as places sideways not upstairs, Valhalla/Hel/strand, time crooked, doors (mounds, sea-mist, crossroads, Yule), guest manners, veil walk, dawn/dusk, dream-log 7 nights.
3. Gods & Neighbors pp31-60: keep Aesir/Vanir/other distinct. Odin, Thor, Freyja, Freyr, Frigg, Loki plainly, Baldr one page honestly small, plus landvaettir/dis. No flattening into one family. Altar page, offering log.
4. Heroes & Your Oath pp61-74: Sigurd, Brynhildr, Egil as ballast (historical/saga), hamingja/luck, oath-formula explained, breaking/repair, 30-day vow, geis-equivalent tracker 1-14 + 15-30.
5. Wheel of Year pp75-98: honest wheel — Yule, Winter Nights, Sigrblot/Summer finding have thin/varied ground, Midsummer mostly folk/modern. No 8-spoke import without label. Same 5-pages-per-fire shape as Celtic: story, old practice, modern rite, table, reflections. Moon/runestone sidebar strictly separate.
6. Plants & Trees pp99-118: Safety box first. Classics (mugwort, yarrow, juniper, birch, pine — Eisenherb lore only if sourced), folk & field 5, trees 5 (ash, birch, rowan, juniper/yew-careful, oak). Journal-only for toxic/protected. No dosing.
7. Wells, Sea, Doorways, Dawn/Dusk + Runes/Symbols pp119-132: holy wells/springs, sea roads, doorways, neither-times. Runes: Elder/Younger Futhark stones 2nd-8th c attested, medieval rune-poems attested, oracle spreads modern. Valknut/triquetra honesty — Iron Age vs Christian/medieval vs modern, same as triskele rule.
8. Charms & Workings pp133-142: Merseburg-type charms and Sigrdrifa-type counsel as Attested literary charms only, caim-equivalent circling/saining labeled by culture, 3 workings (knot/thread, doorway bundle, water blessing), uncrossing/repair, 2-week tracker.
9. Ancestors & Dead pp143-147: haugr/mound-neighbors, disir/alfar carefully, dumb-supper equivalent labeled by culture, 2 ancestor cards, grief letter + roll-call.
10. Your Oath pp148-150: vow page, 30-day integration tracker, go-on-reading list (Poetic Edda, Prose Edda, Volsunga Saga, Egil's Saga).

## Sources to use first-hand — do not invent beyond these

Poetic Edda (Larrington trans., plus CELT/Codex Regius text), Prose Edda (Faulkes), Volsunga Saga (Byock), Egil's Saga, Havamal/Sigrdrifumal for counsel verses only, Tacitus Germania for outsider-frame, Ibn Fadlan for burial account labeled outsider, runestone corpus (Samnordisk rundatabas overview), Auraicept-equivalent: rune-poems (Norwegian/Icelandic/Anglo-Saxon), Brehon-equivalent: Grey Goose Laws for price/custom only. Folk: Tillhagen/saining custom labeled folk. Modern: 8-spoke wheel, rune-oracle sets, valknut-as-Odin-badge — label Modern, cut where Celtic book cut triquetra.

## Tasks

### Task 1: Scaffold `grimoires/norse/`
Copy `gen_celtic.py` → `gen_norse.py`, retitle. Copy CSS verbatim. Stub `content_a.py`–`content_d.py` with CH1–CH10 lists matching page map above.

### Task 2: CH1-CH2 + CH3-CH4 (`content_a.py`, `content_b.py`)
3-paras each lore, prompts in same voice as Celtic examples (Threshold p7, Cernunnos p32). Keep Aesir/Vanir separate, Loki plainly trickster-not-devil, Baldr small.

### Task 3: CH5-CH6 (`content_c.py`)
Honest year-wheel, Coligny-equivalent sidebar (Rök stone or calendar-stick controversy, strictly sidebar). Plant safety verbatim + yew/juniper no-ingest fix.

### Task 4: CH7-CH10 (`content_d.py`)
Runes 7-rune working set for journal (label modern), symbols honesty page, 3 charms ward/bless only, ancestors gentle, oath close.

### Task 5: Build + verify
`python3 gen_norse.py` → 150 divs, folios 1-150, no `overflow` clipping on pp7,32,79,105 equivalents. Build PDF 150p 432x648pts. List remaining lore-root doubts at top of output.

Accept: reads aloud without choppiness, no new unattributed claims, 150 pages intact, matches Celtic system page-for-page.
