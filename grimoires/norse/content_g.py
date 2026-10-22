"""Content G: the Runes, Staves, and Seiðr rebuild. Raw HTML blocks start with '<'.
Tokens replaced in gen_norse.py: {{AEGIS}}, {{VALKNUT}}.
"""

def _tbl(rows, cls="rt"):
    out = [f'<table class="{cls}">']
    for g, n, s, m in rows:
        out.append(f'<tr><td class="g">{g}</td><td class="n">{n}</td><td class="s">{s}</td><td>{m}</td></tr>')
    out.append('</table>')
    return "".join(out)

ELDER_1 = [("ᚠ","fehu","f","cattle, wealth"),("ᚢ","uruz","u","the aurochs, a wild ox"),("ᚦ","þurisaz","th","a giant, or a thorn"),("ᚨ","ansuz","a","a god; the mouth of Óðinn"),("ᚱ","raidō","r","riding, a journey"),("ᚲ","kenaz","k","a torch, or a sore"),("ᚷ","gebō","g","a gift"),("ᚹ","wunjō","w","joy")]
ELDER_2 = [("ᚺ","hagalaz","h","hail"),("ᚾ","nauðiz","n","need, hardship"),("ᛁ","īsaz","i","ice"),("ᛃ","jēra","j","the year, a good harvest"),("ᛇ","eihwaz","ei","the yew"),("ᛈ","perþō","p","uncertain; no agreed meaning"),("ᛉ","algiz","z","uncertain; often read “elk” or “protection”"),("ᛊ","sōwilō","s","the sun")]
ELDER_3 = [("ᛏ","tīwaz","t","the god Týr"),("ᛒ","berkanan","b","the birch"),("ᛖ","ehwaz","e","a horse"),("ᛗ","mannaz","m","a man, a person"),("ᛚ","laguz","l","water; the same rune is also read as laukaz, the leek"),("ᛜ","ingwaz","ng","the god Ing, a name of Freyr"),("ᛞ","dagaz","d","day"),("ᛟ","ōþala","o","an inherited estate, heritage")]
YOUNGER = [("ᚠ","fé","f","wealth, which stirs up strife among kin"),("ᚢ","úr","u, o, v","drizzle or slag"),("ᚦ","þurs","th","a giant"),("ᚬ","óss","o, a","a god, “aged Gautr,” Óðinn; also a river mouth"),("ᚱ","reið","r","riding"),("ᚴ","kaun","k, g","an ulcer, a sore"),("ᚼ","hagall","h","hail"),("ᚾ","nauð","n","need, hardship"),("ᛁ","ís","i, e","ice"),("ᛅ","ár","a, æ","a good harvest, plenty"),("ᛋ","sól","s","the sun"),("ᛏ","týr","t, d","the one-handed god"),("ᛒ","bjarkan","b, p","the birch"),("ᛘ","maðr","m","a man"),("ᛚ","lǫgr","l","water"),("ᛦ","ýr","R","the yew, a bent bow")]

def _kv(pairs):
    return "".join(f'<span class="kv"><span class="g">{g}</span>{l}</span>' for l, g in pairs)

LATIN = [("a","ᚨ"),("b","ᛒ"),("d","ᛞ"),("e","ᛖ"),("f","ᚠ"),("g","ᚷ"),("h","ᚺ"),("i","ᛁ"),("j","ᛃ"),("k","ᚲ"),("l","ᛚ"),("m","ᛗ"),("n","ᚾ"),("o","ᛟ"),("p","ᛈ"),("r","ᚱ"),("s","ᛊ"),("t","ᛏ"),("u","ᚢ"),("w","ᚹ"),("z","ᛉ"),("th","ᚦ"),("ng","ᛜ"),("ei","ᛇ")]

RUNE_PAGES = [
("lore", "Runes", "What runes are",
 ["Runes are the letters the early Germanic peoples carved in wood, stone, bone, and metal. The oldest inscriptions date from about the second century CE. The alphabet is called the futhark, named for its first six letters: f, u, th, a, r, k. It came in three main forms. The Elder Futhark has 24 runes and was used from about the 2nd to the 8th century. The Younger Futhark has 16 and was used in Viking Age Scandinavia, from about the 9th to the 12th century. The Anglo-Saxon futhorc grew to as many as 33 and was used in England.",
  "Each rune has a name, a sound, and a meaning from the rune poems. Fehu is the sound f and also the word for cattle and wealth. On some inscriptions a single rune stands for the whole word it names, as scholars think the l-rune stands for laukaz, “leek.”",
  "The row below is cut on the Kylver stone, a grave slab from Gotland in Sweden, about the year 400. It is the oldest complete futhark we have.",
  '<div class="rrow">ᚠᚢᚦᚨᚱᚲᚷᚹ &nbsp; ᚺᚾᛁᛃᛇᛈᛉᛊ &nbsp; ᛏᛒᛖᛗᛚᛜᛞᛟ</div>',
  "<b>Where this comes from:</b> The Kylver stone and the three futharks are known from archaeology. The rune names come from the rune poems."],
 "Copy the 24 runes of the Kylver row by hand, once, slowly."),
("lore", "Runes", "The Elder Futhark: Freyr’s eight",
 ["The 24 runes are grouped in three families of eight, called ættir (singular ætt). Later books name each family after the rune that begins it: Freyr’s ætt, Hagal’s ætt, and Týr’s ætt. The first is Freyr’s.",
  _tbl(ELDER_1),
  "These names are reconstructed. No Elder Futhark inscription records them, so scholars rebuild them from the Anglo-Saxon, Norwegian, and Icelandic rune poems.",
  "<b>Where this comes from:</b> The runes are known from inscriptions. Their names are reconstructed from the rune poems."],
 "Say the eight names aloud, then copy the eight runes."),
("lore", "Runes", "The Elder Futhark: Hagal’s eight",
 ["The second family of eight is called Hagal’s ætt, after the hail rune that begins it. Two of its runes, perþō and algiz, have names no one can agree on.",
  _tbl(ELDER_2),
  "<b>Where this comes from:</b> The runes are known from inscriptions. Their names are reconstructed from the rune poems."],
 "Say the eight names aloud, then copy the eight runes."),
("lore", "Runes", "The Elder Futhark: Týr’s eight",
 ["The third family is Týr’s ætt, named for the god’s rune, tīwaz. It ends with ōþala, the rune of heritage and home.",
  _tbl(ELDER_3),
  "<b>Where this comes from:</b> The runes are known from inscriptions. Their names are reconstructed from the rune poems."],
 "Say the eight names aloud, then copy the eight runes."),
("lore", "Runes", "The Younger Futhark: sixteen runes",
 ["In the Viking Age the row shrank to 16 runes, so each rune had to serve for several sounds. The Icelandic and Norwegian rune poems give each one a short verse. This is the gist of each, in long-branch form.",
  _tbl(YOUNGER, 'rt rt2'),
  "<b>Where this comes from:</b> Viking Age stones. The meanings are paraphrased from the Icelandic and Norwegian rune poems (Dickins, 1915)."],
 "Choose three runes and copy each with its name and its poem line."),
("lore", "Runes", "Runes in use: seven examples",
 ["<b>Kylver stone</b>: the whole futhark, cut on a grave slab on Gotland, about 400.<br><b>Bracteates</b>: gold medallions from about 500 carry the words alu and laukaz. Nobody is sure what they meant, but they repeat.<br><b>Björketorp stone</b>: a 7th-century stone in Sweden that curses anyone who breaks it.<br><b>Rök stone</b>: the longest Viking Age inscription, with some secret runes among the ordinary ones.<br><b>Egill’s horn</b>: in Egils saga, Egill carves runes on a drinking horn and rubs them with blood. The horn bursts, and the poisoned drink spills.<br><b>Egill’s whalebone</b>: in the same saga, a girl is sick because someone carved the wrong runes on a whalebone. Egill scrapes them off, burns the shavings, carves new runes, and she recovers.<br><b>Sigrdrífumál</b>: the valkyrie Sigrdrífa lists runes for victory, for ale, for birth, for the sea, for healing, for speech, and for wisdom, each cut on a named object.",
  "Egill’s verse in the saga sums it up: a man should not carve runes unless he can read them well. Many are confounded by a dark rune.",
  "<b>Where this comes from:</b> The inscriptions are known from archaeology. Egill’s runes are in Egils saga, and Sigrdrífa’s are in the Sigrdrífumál."],
 "Which of these seven would you most like to see in person? Name it and where it is."),
("lore", "Runes", "Writing in runes",
 ["To write in runes, spell by sound, not by spelling. The Elder Futhark has no capitals and no rules for spaces. Inscriptions mark the end of a word with a dot or two, and may run left to right or right to left.",
  '<div class="kvgrid">' + _kv(LATIN) + '</div>',
  "There is no c, v, or y: use ᚲ for c, ᚹ for v, and ᛃ for y. Four examples:",
  '<div class="rrow" style="font-size:15pt">ᛖᚷᛁᛚᛚ &nbsp; ᚦᛟᚱ &nbsp; ᚨᛊᚲ &nbsp; ᛖᛗᛒᛚᚨ</div><div style="text-align:center;font-size:10.5pt;margin-top:-0.05in">egill &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; thor &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ask &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; embla</div>',
  "Notice that the runes are all straight lines. Wood has a grain, and a cut along the grain tends to split, so rune strokes run across it. That is one reason runes avoid curves and flat horizontal lines.",
  "<b>Where this comes from:</b> The rune values are standard. The grain explanation is the usual scholarly account, not a statement in any source."],
 "Write your own name in Elder Futhark, by sound."),
("lore", "Runes", "Carving runes",
 ["The old sources say how runes were made. Sigrdrífa tells Sigurðr to carve them on the thing they are for: a sword’s hilt, a horn, the palm, a ship’s prow. In Egils saga, Egill carves runes and then reddens them with blood. The Hávamál asks the same questions in stanza 146: do you know how to carve a rune, how to read it, how to color it, and how to test it?",
  "To make a simple carved rune, you need a smooth, dry piece of wood and a sharp knife, used carefully and always cutting away from your hand. Draw the runes in pencil first. Cut each stroke across the grain, with two cuts that meet in a V. Then fill the cuts with red ink or paint. This book does not ask for blood.",
  "Egill’s rule is the one that matters most: do not carve runes you cannot read. Before you cut a rune, know its name and the sound or word it stands for.",
  "<b>Where this comes from:</b> Sigrdrífumál stanzas 6 to 19, Hávamál stanza 146, and Egils saga. The wood and ink steps are practical, not from a source."],
 "Carve one rune you know the name of on a scrap of wood. Fill the cuts with red ink."),
("lore", "Runes", "Bindrunes and secret runes",
 ["A bindrune joins two or more runes by sharing one stave, the vertical line. Bindrunes appear on many early and Viking Age inscriptions, to save space or to make a name look like one sign.",
  '<div style="text-align:center"><span class="bind"><span>ᚠ</span><span>ᚱ</span></span><span class="bind"><span>ᚨ</span><span>ᛏ</span></span></div><div style="text-align:center;font-size:10.5pt;margin-top:-0.05in">fr &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; at</div>',
  "The two signs above join fehu and raidō (fr) and ansuz and tīwaz (at). To make one, pick runes that share a stave, and draw the shared stave once.",
  "Secret runes are older than they sound. The Rök stone uses cipher runes. One old cipher counts the family of eight and the place in the row, so each rune becomes two numbers shown as strokes: fehu is the first rune of the first family, so it is 1 and 1.",
  "<b>Where this comes from:</b> Bindrunes and cipher runes are known from Viking Age inscriptions, including the Rök stone."],
 "Join two runes from your own name as a bindrune. Draw it, and write the two runes beside it."),
("lore", "Runes", "Carve your name",
 ["The oldest runic sentence formula is a maker’s mark. The Golden Horn of Gallehus, made in Denmark about the year 400, carries this line:",
  '<div class="rrow" style="font-size:15pt">ᛖᚲ ᚺᛚᛖᚹᚨᚷᚨᛊᛏᛁᛉ ᚺᛟᛚᛏᛁᛃᚨᛉ ᚺᛟᚱᚾᚨ ᛏᚨᚹᛁᛞᛟ</div>',
  "It reads “ek Hlewagastiz Holtijaz horna tawido,” which means “I, Hlewagastiz, son of Holt, made the horn.” The golden horns were stolen and melted in 1802, but drawings of the inscription survive.",
  "Use the same pattern on something you have made. Write ek, then your name, then tawido, which means “made.” Spell by sound, and carve it as you learned on the last pages.",
  "<b>Where this comes from:</b> The Gallehus inscription is known from early drawings. The formula ek … tawido recurs on other early inscriptions."],
 "Carve ek, your name, and tawido on something you have made."),
("lore", "Runes", "A rune a day",
 ["The oldest complete rune row we have is on the Kylver stone from Gotland, carved about the year 400. It lists the whole Elder Futhark in order, and it is the earliest full row we have. You can use that order as a month-long practice, one rune a day for twenty-four days.",
  "Each day, take the next rune from the three groups of eight on the earlier pages. Say its name aloud. Read its line in the rune poems. Draw it three times in your notebook, then carve it once if you have wood and a knife. Spend one more minute looking for the thing it names: cattle, water, ice, a gift, a day. Five minutes is enough.",
  "At the end of the twenty-four days, write your name in the runes you have learned, and say which three felt most like yours. Egill’s rule still holds. Do not use a rune you cannot name.",
  "<b>Where this comes from:</b> The order of the Elder Futhark comes from the Kylver stone, about 400 CE. The daily practice was built for this book."],
 "Pick the day you will start. Write the first rune, its name, and one thing you noticed about it."),
("lore", "Runes", "Casting lots",
 ["The Roman writer Tacitus, writing about 98 CE, describes how Germanic peoples took omens. They cut a branch from a fruit tree into small slips and cut a mark on each one. The slips were scattered on a white cloth. A priest, or in a private matter the father of the household, prayed to the gods, looked up at the sky, and lifted three slips one at a time. He read them by the marks. If the lots forbade a plan, it was dropped for that day.",
  "Tacitus says marks, not runes, so we cannot say these were runes. What this shows is that drawing marked slips for a yes-or-no answer was an old habit. Rune casting as it is practiced now, with named meanings and layouts, is modern.",
  "To try the old shape, gather ten or more small pieces of wood from fallen twigs, and cut a rune you know on each. Lay out a light cloth. Ask a question about something you can actually do. Pull three slips, one at a time, without looking. Read each by its name and its poem line. Then decide what you will do. The runes give you something to think with, not an order.",
  "<b>Where this comes from:</b> Tacitus, Germania, chapter 10. The runes, the question, and the reading method are modern."],
 "Draw three slips for a choice you face this week. Write each rune, its name, and what you decided."),
]

STAVE_PAGES = [
("lore", "Staves", "Runes and staves are not the same",
 ["Runes are an alphabet. They were cut from about the 2nd to the 12th century, for writing and for magic, and their names and meanings are in the rune poems.",
  "Galdrastafir, usually called staves, are magic signs. They come from Iceland, mostly from the 15th to the 19th centuries, and they were drawn in charm books beside Latin, runes, and Christian prayers. A stave is not a letter. It is a sign made for a purpose.",
  "That difference matters because many modern sellers call staves Viking symbols. They are not. The staves in this chapter are medieval and early modern, and the pages say when each one is from.",
  "<b>Where this comes from:</b> The dating is from the Icelandic manuscripts described on the next page."],
 "Say in one sentence how a rune differs from a stave."),
("lore", "Staves", "The stave books: a timeline",
 ["<b>About 1500, AM 434 a 12mo</b>: an Icelandic book of medicine and magic. Its staves are drawn beside remedies, and its rituals are for finding a thief, frightening an enemy, and avoiding a ruler’s anger.<br><b>1600s, Galdrabók</b>: a collection of Icelandic spells that mixes Latin, runes, and staves with Christian prayers.<br><b>1670, Galdrakver</b>: “the little magic book,” a small skin-bound book. Its drawings include the sign called the Helm of Awe.<br><b>1860s, the Huld manuscript</b>: a 19th-century collection that holds the way-pointer, Vegvísir.",
  "Dates are approximate, and scholars disagree on some of them. The oldest manuscript is already two to three centuries after the Viking Age.",
  "<b>Where this comes from:</b> Luthien Cangemi’s The Art of Healing in Medieval Iceland (UCL, 2024) for AM 434 a 12mo, and standard descriptions of the other books."],
 "Which of these four books would you most like to see? Name it and why."),
("lore", "Staves", "Three rituals from the oldest stave book",
 ["<b>To see a thief.</b> Carve a sign on the bottom of a box. Grind yarrow as fine as you can in clean water, and say: “I desire, by the nature of the herb and the power of the sign, that I may see the shadow of the one who has stolen from me.” End with the Latin words In nomine domini, amen.<br><b>To frighten an enemy.</b> Pick yarrow on the feast of Bishop John. Keep the sun off it, take it with all its roots, and speak over it when the sun is in the south-east. Carry the sign in your left hand.<br><b>To avoid a ruler’s anger.</b> Go out before sunrise and speak to no one. Take yarrow and let your blood fall on it, then draw a cross on your forehead with the herb, and go before your lord.",
  "Notice the pattern: a sign, a herb, spoken words, and a Christian closing. These rituals are quoted as history. This book does not ask you to draw blood or to try them.",
  "<b>Where this comes from:</b> AM 434 a 12mo, as quoted in Luthien Cangemi’s thesis, from Ben Waggoner’s translation."],
 "Which of the three rituals is the strangest to you, and why?"),
("lore", "Staves", "Two famous staves",
 ["<b>Ægishjálmr</b>, the Helm of Awe, takes its name from the Fáfnismál, where the dragon Fáfnir says: “An Oegis-helm I bore among the sons of men, while I o’er the treasures lay.” (Stanza 16, translated by Benjamin Thorpe, 1866.) Sigurðr answers that it is no protection when angry men fight. One 17th-century stave book describes the Helm of Awe as a sign to carve in lead and press between the brows to overcome foes. The drawing below is a simplified modern version; the manuscripts vary.",
  '<div style="text-align:center">{{AEGIS}}</div>',
  "<b>Vegvísir</b>, the way-pointer, is from the 19th-century Huld manuscript. It says that a person who carries the sign will not lose their way in storms or bad weather, even on an unknown road. It is not a Viking Age sign.",
  "<b>Where this comes from:</b> The Fáfnismál is in the Poetic Edda. The Helm of Awe instructions are in 17th-century Icelandic stave books, and Vegvísir is in the Huld manuscript."],
 "Which of these two staves would you want on a journey? Say why."),
("lore", "Symbols", "Valknútr (Valknut) is old; the rest is newer",
 ["{{VALKNUT}}",
  "The valknútr (knot of the slain) is three triangles locked together. It is cut on Viking Age picture stones beside riders and ships. Its link to Óðinn is only suggested, by the scenes it appears in, not by a written label.",
  "Of the signs in this chapter, only the valknútr is Viking Age. The staves are later. The triquetra, a knot of three pointed loops, belongs to Early Christian and medieval art, and most tangled knotwork sold as a Viking badge is medieval or modern craft.",
  "Study it where it was found. Find photographs of Viking Age picture stones that show a valknútr, and sketch the knot. Beside each sketch, note the scene around it: riders, ships, or fallen warriors.",
  "<b>Where this comes from:</b> The valknútr is cut on Viking Age picture stones. The triquetra comes from Christian and medieval art."],
 "Sketch a valknútr from a photograph of a picture stone. Note the scene around it."),
]

SEIDR_PAGES = [
("lore", "Seeress and Fate-Work", "Seiðr in the sources",
 ["The sources that describe seiðr are few. Here they are.",
  "<b>Vǫluspá</b>: Heiðr, a seeress who practiced seiðr, is burned three times and born again.<br><b>Lokasenna</b>: Loki mocks Óðinn for beating a drum and going about as a witch among men.<br><b>Ynglinga saga, chapter 4</b>: Freyja is a priestess of the sacrifices, and she teaches seiðr to the Æsir.<br><b>Ynglinga saga, chapter 7</b>: Óðinn can change shape while his body lies as if asleep. Snorri says seiðr could bring harm, and that men who practiced it were shamed, so priestesses taught it.<br><b>Eiríks saga rauða, chapter 4</b>: a seeress named Þorbjǫrg comes to a Greenland farm in a famine winter. The next page describes her.",
  "What they share: women are the practitioners, a staff is carried, there is a high seat or platform, chanting is involved, and the aim is knowledge of fate. The sources describe seiðr far more than they teach it.",
  "<b>Where this comes from:</b> The Vǫluspá and Lokasenna are in the Poetic Edda. Ynglinga saga is in Snorri’s Heimskringla. Eiríks saga rauða is an Icelandic saga."],
 "Which of the five sources would you most like to read in full? Name it and why."),
("lore", "Seeress and Fate-Work", "A seeress at work: Eiríks saga rauða",
 ["In a famine winter in Greenland, a seeress named Þorbjǫrg is invited to a farm to foretell when the hunger will end. The saga describes her in detail.",
  "<b>Dress</b>: a blue-black mantle set with stones to the hem, a necklace of glass beads, a black lambskin hood lined with white catskin, calfskin shoes with tin knobs, and catskin gloves white inside.<br><b>Tools</b>: a staff with a brass knob set with stones, and a belt of touchwood with a large pouch for her charms.<br><b>Seat</b>: a high seat with a cushion stuffed with hen feathers.<br><b>Food</b>: porridge of kid’s milk, and the hearts of every kind of animal on the farm.<br><b>Chants</b>: she needs women who know the chants called varðlokur. Only Guðríðr, a young Christian at the farm, knows them, and she sings them reluctantly.<br><b>Result</b>: the spirits are drawn by the song, and Þorbjǫrg says the famine will end and tells Guðríðr her own future.",
  "The saga was written in the 1200s, by a Christian author, about events around the year 1000. It is the most detailed account of a seeress that survives.",
  "<b>Where this comes from:</b> Eiríks saga rauða, chapter 4."],
 "Which part of this scene would be hardest to recreate honestly, and why?"),
]

RUNE_NOTEBOOK = [
("journal", "Runes", "Rune notebook: write each rune you carve, its name, its poem line, and where you used it.", 12),
]
