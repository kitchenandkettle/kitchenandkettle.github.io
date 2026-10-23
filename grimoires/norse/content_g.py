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

LATIN = [("a","ᛅ"),("b, p","ᛒ"),("d, t","ᛏ"),("e, i","ᛁ"),("f","ᚠ"),("g, k","ᚴ"),("h","ᚼ"),("l","ᛚ"),("m","ᛘ"),("n","ᚾ"),("o, u, v","ᚢ"),("r","ᚱ"),("s","ᛋ"),("th","ᚦ"),("end r","ᛦ")]

RUNE_PAGES = [
("lore", "Runes", "What runes are",
 ["Runes are the letters the early Germanic peoples carved in wood, stone, bone, and metal. The oldest inscriptions date from about the second century CE. The alphabet is called the futhark, named for its first six letters: f, u, th, a, r, k. It came in three main forms. The Elder Futhark has 24 runes and was used from about the 2nd to the 8th century, to write Proto-Norse, the early Northern Germanic language. The Younger Futhark has 16 and was used from about the 9th to the 12th century, to write Old Norse in Viking Age Scandinavia. The Anglo-Saxon futhorc grew to as many as 33 and was used in England.",
  "What the inscriptions prove is that runes were an alphabet. Most carry short, plain messages: a name on a grave marker, an owner’s or maker’s name on a sword or tool. The Vǫluspá gives them one more job. There the Norns carve the fates of people on wooden slips, the way runes are cut.",
  "Each rune has a name, a sound, and a meaning from the rune poems. Fehu is the sound f and also the word for cattle and wealth. On some inscriptions a single rune stands for the whole word it names, as scholars think the l-rune stands for laukaz, “leek.”",
  "The row below is cut on the Kylver stone, a grave slab from Gotland in Sweden, about the year 400. It is the oldest complete futhark we have.",
  '<div class="rrow">ᚠᚢᚦᚨᚱᚲᚷᚹ &nbsp; ᚺᚾᛁᛃᛇᛈᛉᛊ &nbsp; ᛏᛒᛖᛗᛚᛜᛞᛟ</div>',
  "<b>Where this comes from:</b> The Kylver stone and the three futharks are known from archaeology. The rune names come from the rune poems."],
 "Copy the 24 runes of the Kylver row by hand, once, slowly."),
("lore", "Runes", "The Elder Futhark: 24 runes",
 ["The Elder Futhark wrote Proto-Norse, the early language of the north, before the Viking Age. Its 24 runes fall into three families of eight, called ættir (singular ætt): Freyr’s, Hagal’s, and Týr’s, each named for the rune that begins it.",
  _tbl(ELDER_1 + ELDER_2 + ELDER_3, 'rt rt3'),
  "<b>Where this comes from:</b> The runes are known from inscriptions. Their names are reconstructed from the rune poems, and no one agrees on the names of perþō and algiz."],
 "Say the eight names of one family aloud, then copy their runes."),
("lore", "Runes", "The Younger Futhark: sixteen runes",
 ["Old Norse was written in this row. In the Viking Age the Elder row shrank to 16 runes, so each rune had to serve for several sounds. The Icelandic and Norwegian rune poems give each one a short verse. This is the gist of each, in long-branch form.",
  _tbl(YOUNGER, 'rt rt2'),
  "<b>Where this comes from:</b> Viking Age stones. The meanings are paraphrased from the Icelandic and Norwegian rune poems (Dickins, 1915)."],
 "Choose three runes and copy each with its name and its poem line."),
("lore", "Runes", "Two forms of the row",
 ["The sixteen Younger Futhark runes were drawn in two forms. Long-branch runes, also called Danish runes, have full-length strokes and appear on many carved stones. Short-twig runes, also called Swedish-Norwegian runes, are cut short, with a stave and a small twig, and suited quick, everyday carving. It is the same row with the same sounds. The table on the last page shows the long-branch form.",
  "Carvers with a knife and a stick of wood had a problem: sixteen runes for more than sixteen sounds. Around the eleventh century they began to add a dot to some runes to tell the sounds apart. A dotted i stood for e, a dotted k for g, a dotted t for d, and a dotted b for p.",
  "You do not need the dots here. The writing pages in this book use the plain sixteen, and the reader works out the word from the whole line, as Viking Age readers did.",
  "<b>Where this comes from:</b> The two forms and the dotted runes are known from Viking Age stones and wooden sticks. The rune poems give the meanings."],
 "Choose a rune that stands for two sounds, and write two words that use it."),
("lore", "Runes", "Runes in use: seven examples",
 ["<b>Kylver stone</b>: the whole futhark, cut on a grave slab on Gotland, about 400.<br><b>Bracteates</b>: gold medallions from about 500 carry the words alu and laukaz. Nobody is sure what they meant, but they repeat.<br><b>Björketorp stone</b>: a 7th-century stone in Sweden that curses anyone who breaks it.<br><b>Rök stone</b>: the longest Viking Age inscription, with some secret runes among the ordinary ones.<br><b>Egill’s horn</b>: in Egils saga, Egill carves runes on a drinking horn and rubs them with blood. The horn bursts, and the poisoned drink spills.<br><b>Egill’s whalebone</b>: in the same saga, a girl is sick because someone carved the wrong runes on a whalebone. Egill scrapes them off, burns the shavings, carves new runes, and she recovers.<br><b>Sigrdrífumál</b>: the valkyrie Sigrdrífa lists runes for victory, for ale, for birth, for the sea, for healing, for speech, and for wisdom, each cut on a named object.",
  "Egill’s verse in the saga sums it up: a man should not carve runes unless he can read them well. Many are confounded by a dark rune.",
  "<b>Where this comes from:</b> The inscriptions are known from archaeology. Egill’s runes are in Egils saga, and Sigrdrífa’s are in the Sigrdrífumál."],
 "Which of these seven would you most like to see in person? Name it and where it is."),
("lore", "Runes", "Writing in runes",
 ["To write in runes, spell by sound, not by spelling. Old Norse runes have no capitals and no rules for spaces. Inscriptions mark the end of a word with a dot or two, and may run left to right or right to left.",
  '<div class="kvgrid">' + _kv(LATIN) + '</div>',
  "Sixteen runes cover every sound, so some letters share one: e and i, o and u and v, b and p, d and t, g and k. Use plain spelling: c is k, y is i, z is s. Four examples:",
  '<div class="rrow" style="font-size:15pt">ᛁᚴᛁᛚᛚ &nbsp; ᚦᚢᚱ &nbsp; ᛅᛋᚴ &nbsp; ᛁᛘᛒᛚᛅ</div><div style="text-align:center;font-size:10.5pt;margin-top:-0.05in">egill &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; thor &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ask &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; embla</div>',
  "Notice that the runes are all straight lines. Wood has a grain, and a cut along the grain tends to split, so rune strokes run across it. That is one reason runes avoid curves and flat horizontal lines.",
  "<b>Where this comes from:</b> The rune values are standard. The grain explanation is the usual scholarly account, not a statement in any source."],
 "Write your own name in the Younger Futhark, by sound."),
("lore", "Runes", "Reading a stone",
 ["Reading runes goes the other way from writing them. Each rune gives you a sound, and you choose the word. Because one rune can stand for several sounds, you read the whole line and let the language settle it.",
  "The most common sentence on Viking Age stones is a memorial: so-and-so raised this stone after so-and-so. A carver cut it like this:",
  '<div class="rrow" style="font-size:15pt">ᚱᛅᛁᛋᛏᛁ &nbsp; ᛋᛏᛅᛁᚾ &nbsp; ᚦᛅᚾᛋᛁ &nbsp; ᛅᚠᛏᛁᛦ</div><div style="text-align:center;font-size:10.5pt;margin-top:-0.05in">raisti &nbsp;&nbsp;&nbsp; stain &nbsp;&nbsp;&nbsp; þansi &nbsp;&nbsp;&nbsp; aftiR</div><div style="text-align:center;font-size:10.5pt">raised &nbsp;&nbsp;&nbsp; stone &nbsp;&nbsp;&nbsp; this &nbsp;&nbsp;&nbsp; after</div>',
  "Carvers often wrote the ei sound as ᛅᛁ, a and i together, and used ᛦ for the r at the end of a word. Put the raiser’s name before the sentence and the name of the one remembered after it, and you have a stone.",
  "To practice, read these three words from stones, then say what each one means: ᛋᚢᚾ, ᚠᛅᚦᛁᛦ, ᛒᚱᚢᚦᛁᛦ.",
  "<b>Where this comes from:</b> The memorial formula is found on a great many Viking Age rune stones. The spellings are the usual ones, simplified."],
 "Write a stone line for someone you remember: your name, then raisti stain þansi aftiR, then theirs."),
("lore", "Runes", "Carving runes",
 ["The old sources say how runes were made. Sigrdrífa tells Sigurðr to carve them on the thing they are for: a sword’s hilt, a horn, the palm, a ship’s prow. In Egils saga, Egill carves runes and then reddens them with blood. The Hávamál asks the same questions in stanza 146: do you know how to carve a rune, how to read it, how to color it, and how to test it?",
  "To make a simple carved rune, you need a smooth, dry piece of wood and a sharp knife, used carefully and always cutting away from your hand. Draw the runes in pencil first. Cut each stroke across the grain, with two cuts that meet in a V. Then fill the cuts with red ink or paint. This book does not ask for blood.",
  "Egill’s rule is the one that matters most: do not carve runes you cannot read. Before you cut a rune, know its name and the sound or word it stands for.",
  "<b>Where this comes from:</b> Sigrdrífumál stanzas 6 to 19, Hávamál stanza 146, and Egils saga. The wood and ink steps are practical, not from a source."],
 "Carve one rune you know the name of on a scrap of wood. Fill the cuts with red ink."),
("lore", "Runes", "Bindrunes and secret runes",
 ["A bindrune joins two or more runes by sharing one stave, the vertical line. Bindrunes appear on many early and Viking Age inscriptions, to save space or to make a name look like one sign.",
  '<div style="text-align:center"><span class="bind"><span>ᚠ</span><span>ᚱ</span></span><span class="bind"><span>ᛅ</span><span>ᛏ</span></span></div><div style="text-align:center;font-size:10.5pt;margin-top:-0.05in">fr &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; at</div>',
  "The two signs above join fé and reið (fr) and ár and týr (at). To make one, pick runes that share a stave, and draw the shared stave once.",
  "Secret runes are older than they sound. The Rök stone uses cipher runes. One old cipher counts the family (ætt) and the place in the row, so each rune becomes two numbers shown as strokes: fé is the first rune of the first family, so it is 1 and 1.",
  "<b>Where this comes from:</b> Bindrunes and cipher runes are known from Viking Age inscriptions, including the Rök stone."],
 "Join two runes from your own name as a bindrune. Draw it, and write the two runes beside it."),
("lore", "Runes", "Carve your name",
 ["The oldest runic sentence formula is a maker’s mark. The Golden Horn of Gallehus, made in Denmark about the year 400, carries this line in Elder Futhark and Proto-Norse:",
  '<div class="rrow" style="font-size:15pt">ᛖᚲ ᚺᛚᛖᚹᚨᚷᚨᛊᛏᛁᛉ ᚺᛟᛚᛏᛁᛃᚨᛉ ᚺᛟᚱᚾᚨ ᛏᚨᚹᛁᛞᛟ</div>',
  "It reads “ek Hlewagastiz Holtijaz horna tawido,” which means “I, Hlewagastiz, son of Holt, made the horn.” The golden horns were stolen and melted in 1802, but drawings of the inscription survive.",
  "Old Norse keeps the same pattern. Write ek, then your name, then gerði, which means “made.” Spell by sound in the Younger Futhark, and carve it as you learned on the last pages.",
  "<b>Where this comes from:</b> The Gallehus inscription is known from early drawings. The formula ek … tawido recurs on other early inscriptions. The Old Norse wording is the same pattern in later speech."],
 "Carve ek, your name, and gerði on something you have made."),
("lore", "Runes", "A rune a day",
 ["The Younger Futhark has a fixed order, f, u, th, o, r, k, and the rune poems give it in that order. You can use it as a practice of sixteen days, one rune a day.",
  "Each day, take the next rune from the Younger Futhark page. Say its name aloud. Read its line in the rune poems. Draw it three times in your notebook, then carve it once if you have wood and a knife. Spend one more minute looking for the thing it names: wealth, water, ice, hail, the sun. Five minutes is enough.",
  "At the end of the sixteen days, write your name in the runes you have learned, and say which three felt most like yours. Egill’s rule still holds. Do not use a rune you cannot name.",
  "<b>Where this comes from:</b> The order of the Younger Futhark comes from the rune poems. The daily practice was built for this book."],
 "Pick the day you will start. Write the first rune, its name, and one thing you noticed about it."),
("lore", "Runes", "Casting lots",
 ["The Roman writer Tacitus, writing about 98 CE, describes how Germanic peoples took omens. They cut a branch from a fruit tree into small slips and cut a mark on each one. The slips were scattered on a white cloth. A priest, or in a private matter the father of the household, prayed to the gods, looked up at the sky, and lifted three slips one at a time. He read them by the marks. If the lots forbade a plan, it was dropped for that day.",
  "Tacitus says marks, not runes, so we cannot say these were runes. What this shows is that drawing marked slips for a yes-or-no answer was an old habit. Rune casting as it is practiced now, with named meanings and layouts, is modern.",
  "To try the old shape, gather ten or more small pieces of wood from fallen twigs, and cut a rune you know on each. Lay out a light cloth. Ask a question about something you can actually do. Pull three slips, one at a time, without looking. Read each by its name and its poem line. Then decide what you will do. The runes give you something to think with, not an order.",
  "<b>Where this comes from:</b> Tacitus, Germania, chapter 10. The runes, the question, and the reading method are modern."],
 "Draw three slips for a choice you face this week. Write each rune, its name, and what you decided."),
]

STAVE_PAGES = [
("lore", "Staves", "Two famous staves",
 ["Galdrastafir, usually called staves, are magic signs from Iceland, mostly from the 15th to the 19th centuries. They were drawn in charm books beside Latin, runes, and Christian prayers. A stave is a sign made for a purpose, not a letter. Many sellers call staves Viking symbols, but they are later than the Viking Age. These two are the best known.",
  "<b>Ægishjálmr</b>, the Helm of Awe, takes its name from the Fáfnismál, where the dragon Fáfnir says: “An Oegis-helm I bore among the sons of men, while I o’er the treasures lay.” (Stanza 16, translated by Benjamin Thorpe, 1866.) Sigurðr answers that it is no protection when angry men fight. One 17th-century stave book describes the Helm of Awe as a sign to carve in lead and press between the brows to overcome foes. The drawing below is a simplified modern version; the manuscripts vary.",
  '<div style="text-align:center">{{AEGIS}}</div>',
  "<b>Vegvísir</b>, the way-pointer, is from the 19th-century Huld manuscript. It says that a person who carries the sign will not lose their way in storms or bad weather, even on an unknown road. It is not a Viking Age sign.",
  "<b>Where this comes from:</b> The Fáfnismál is in the Poetic Edda. The Helm of Awe instructions are in 17th-century Icelandic stave books such as the Galdrabók and Galdrakver, and Vegvísir is in the 1800s Huld manuscript."],
 "Which of these two staves would you want on a journey? Say why."),
("lore", "Symbols", "Valknútr (Valknut): a Viking Age sign",
 ["{{VALKNUT}}",
  "The valknútr (knot of the slain) is three triangles locked together. It is cut on Viking Age picture stones beside riders and ships. Its link to Óðinn is only suggested, by the scenes it appears in, not by a written label.",
  "The valknútr is not a stave. It is older than the staves by many centuries. The triquetra, a knot of three pointed loops, belongs to Early Christian and medieval art, and most tangled knotwork sold as a Viking badge is medieval or modern craft.",
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
