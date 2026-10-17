# Celtic Grimoire — Prose Pass

> **For Hermes:** Rewrite directly — all lore paras in `grimoires/celtic/content_a.py`, `content_b.py`, `content_c.py`, `content_d.py`. Keep tuple format, page count, prompts. Single session.

**Goal:** Beef up lore text. Current draft is shallow and choppy: 2 short paras, every sentence hinged on because/so, no scene, no texture. Make it well-rounded and readable aloud, without adding new lore claims or breaking 6x9 fit.

**Directory:** `/home/chels/test/grimoires/celtic/`
**Generator:** `gen_celtic.py` — `lore_page(num,kicker,title,paras,prompt)`, `journal_page`, `tracker_page`. Build must stay 150 pages. Test with `python3 gen_celtic.py`.

---

## Why it feels choppy

- Same openers: When/You will/Since/Because/So on nearly every page.
- Two paras only: claim, then instruction. No middle where the image lands.
- No sensory detail: no sound, season, hands, house. All summary.
- Practice bridge is abrupt. Needs one sentence linking old to your flat/field.

## Target voice

- Plain 2nd-person, kitchen-table smart. Warm, flat affect. No guru language.
- Varied rhythm: one longer scene sentence, then a short plain one. Read aloud test.
- Keep Chels constraints: cultures kept separate (Gaul / Ireland / Wales never blended), every claim labeled, safety verbatim, no curses/hexes, no druid-manual claims.

## Hard constraints

1. Do not change: kicker, title, prompt text, Lore Root line, folio order, journal/trackers.
2. Lore pages: 3 paras + Lore Root (Root is para 4, keep verbatim). Body budget 1300-1750 chars total incl. spaces. Current avg 600-900, headroom to ~2300 before `.page{overflow:hidden}` clips at `grimoires/celtic/gen_celtic.py:158`.
3. No new deities, dates, or uses without label. If unsure, label Reconstructed/Modern.
4. Safety pages pp4,99 must keep exact safety sentences. Toxic list: yew, mistletoe, selago, samolus = eyes/notebook only. Bought teas only, expert ID only, check meds/pregnancy, never leave flame. Fix `content_c.py:93` "store bought" -> "store-bought" to match p4.
5. `content_c.py:165` yew aril exception: keep fact but close loophole. Change to: every part is poison, take no teas, no berries, no experiments. No aril detail.
6. After rewrite: run `python3 gen_celtic.py`, confirm `wrote celtic-grimoire.html with 150 .page divs`, folios 1-150 sequential, rebuild interior PDF at 432x648pts.

## Rewrite shape per lore page

- P1 scene/story: where we know it from, one concrete image.
- P2 what it means: translate to household terms, keep distinction Attested vs folk vs modern.
- P3 practice bridge: what to do in under an hour, in a flat, with hands.
- Keep prompts as-is.

## Examples — do all pages like this

### 1. Threshold p7 — Who we mean here, part one
BEFORE: 2 paras, cousins/twins summary.
AFTER:
- P1: When this book says Celtic, picture a language family scattered across hillforts and salt mines and river towns, not a single tribe. The earliest kin gather around Hallstatt's salt workings, then La Tene metalworkers winding their art across central Europe, then Gaulish farmers carving short prayers to local gods in stone, then Irish and Welsh scribes copying old stories into Christian manuscripts centuries later.
- P2: Hold Gaul, Ireland, and Wales as three windows on related but separate houses. In one you get Epona named by soldiers from Britain to Bulgaria with almost no story attached. In another Rhiannon riding a white horse no one can catch. In another the Dagda with club and cauldron, generous and crude in the same hour. Kin, not copies.
- P3: You do not need to choose blood or belief to begin. You need to know which window you are looking through on a given page, and greet that household on its own terms.

### 2. Cernunnos p32
BEFORE: image + name only.
AFTER:
- P1: You meet Cernunnos mostly in silence. On the Gundestrup cauldron he sits cross-legged and antlered, holding a neck-ring, ringed by stag and bull and lion. On the Pillar of the Boatmen at Paris his name is carved by river-merchants doing business under Rome. No tale tells what he says or wants.
- P2: Treat that silence as the teaching. He reads as wild plenty that does not negotiate and cannot be owned, the deer path and the weed lot going on without you. Later stories about him as horned god of witches are modern make; leave them out here.
- P3: Honor him with attention rather than requests. Stand a minute where trees and weeds do as they please, name what lives there, carry litter home. Watching can be worship.

### 3. Samhain story p79
BEFORE: harvest ends, mounds open.
AFTER:
- P1: At Samhain the harvest is in and winter opens. Its old Irish name means summer's end. In the tales herds come down from summer pasture, debts are settled, hearth fires are put out to be kindled fresh, and the mounds — the old burial hills — stand open so the dead walk near. It is a hinge for audit and divination, because winter asks hard questions and you want counsel before the dark.
- P2: Folk custom keeps the shape: quiet house, names spoken aloud, one thing finished before dark. You do not need a crowd or a costume. You need a swept hearth and a clear table.
- P3: Keep it plain and Irish at home. Still the rooms, say the old names, close one account. That small kept shape will carry you through.

### 4. Yarrow p105
BEFORE: feathery leaf, soldier's woundwort.
AFTER:
- P1: Yarrow is easy to know once you learn it: feathery leaves, flat white heads along hedges and verges through summer. Old books call it soldier's woundwort and lend it Achilles' name, because the folk use across countries is staunching — a pinched leaf for nosebleeds, a clean field plaster where permitted.
- P2: Respect runs ahead of use. Skin can sensitize, so wear gloves, try a patch first, keep use outside the body to tiny cuts only or bought tea in the cup. Never as substitute for prescribed medicine.
- P3: Learn it by counting first. On your next walk note how many stands you pass and where the ground is damp or trodden. The notebook teaches what the old herbals cannot: where it lives near you.

---

## Tasks

### Task 1: Rewrite CH1-CH2 in `content_a.py`
All 10 lore entries to 3 paras each. Keep prompts, Roots. Verify char budget per entry <1750.

### Task 2: Rewrite CH3-CH4 in `content_b.py`
All 33 lore entries. Keep Gaul/Ireland/Wales separate. Keep Cerridwen to one honestly-small page, Brigid three-women distinction, Morrigan stark. Keep practice pages practical.

### Task 3: Rewrite CH5-CH6 in `content_c.py`
All 30 lore entries. Keep four-fires honesty (Irish ground only, 8-spoke wheel labeled modern, Coligny as sidebar only). Keep plant safety verbatim + fixes above. Trees: oak/hazel/rowan/hawthorn/yew distinct uses.

### Task 4: Rewrite CH7-CH10 in `content_d.py`
All 21 lore entries. Keep wells leave-no-trace, fords, doorway rite 4-min, ogham 7-fews labeled modern, triskele honesty, charms only ward/bless, ancestors gentle, oath reading list.

### Task 5: Build + verify
Run `python3 gen_celtic.py`, `python3 -c` folio check 1-150, open `http://localhost:8091/celtic-grimoire.html` and spot-check pp7,32,79,105 for clipping. Rebuild interior PDF, confirm 150p 432x648pts.

Accept: prose reads aloud without choppiness, no new unattributed claims, no overflow clipping, 150 pages intact.
