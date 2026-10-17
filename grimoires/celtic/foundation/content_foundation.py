"""Celtic Grimoire content: the chapter plan plus pages written in full.
Rules: every claim sourced, no invented rites, 'Where this comes from' on every lore page,
list pages for parallel facts, modern material labelled.
"""
W = "<b>Where this comes from:</b>"

def L(*pairs):
    """list-style block: pairs of (bold lead, text)"""
    return "<br>".join(f"<b>{a}</b>: {b}" for a, b in pairs)

# ---------------- sample pages ----------------
S_WELCOME = ("lore", "Welcome", "Working with the Old Ways", [
 "Rest your tired bones and troubled mind. This book shares the old Celtic ways, which were about keeping good company with the living, the dead, the land, and the Otherworld next door. If parts of it do not fit your life or beliefs, leave them behind and keep what helps. I have tried to present these old ways as accurately as the sources allow, and I say where each claim comes from. Use the prompt at the end of each page, and the lined pages, to write, reflect, and build your own practice. Write your answers on a lined page or in a notebook of your own, and date them.",
 "“Celtic” is a modern word for peoples who spoke related languages: Gaulish, Irish, Welsh, and their kin. They never shared one religion or one government, so this book keeps Ireland, Wales, and Gaul apart, and says which one it means on every page.",
 "This book mentions plants from medieval medical books and folk custom, but it does not replace a doctor. Never eat, drink, or apply any plant from these pages based on this book alone.",
 W + " Every lore page ends with a short note that says where its ideas come from: a poem, a tale, a stone, a custom, or this book. If a source is late, or scholars disagree, the note says so. Anything described as modern or rebuilt was written for your home and is not an old practice."],
 "What season is it today, outside your actual window? Name three signs.")

S_NAMES = ("lore", "Welcome", "How to say the names", [
 "Irish and Welsh names look hard, but a few rules cover most of them. In Irish, <i>bh</i> and <i>mh</i> sound like v or w, <i>dh</i> and <i>gh</i> are soft or silent, and <i>ch</i> is like the end of “loch.” An accent mark lengthens a vowel. In Welsh, <i>dd</i> is the “th” in this, <i>f</i> is v, <i>w</i> is often “oo,” and <i>ll</i> is a breathy l. Every name below has more than one accepted way to say it.",
 L(("Samhain","SOW-in or SAH-win"),("Imbolc","IM-ulk"),("Beltaine","BYEL-tin-eh"),("Lughnasadh","LOO-na-sa"),("Dagda","DAG-da"),("Lugh","LOO"),("Brigid","BREE-id"),("Morrígan","MOR-ree-gan"),("Tuatha Dé Danann","TOO-a-ha day DAN-an"),("Cú Chulainn","koo KHUL-in"),("Fionn","FYUN"),("Oisín","UH-sheen"),("Rhiannon","hree-AN-on"),("Annwn","AN-oon"),("Taliesin","tal-YES-in"),("Cerridwen","keh-RID-wen"),("ogham","OH-um")),
 "These are English-friendly approximations. Say them aloud once, and they will stay with you.",
 W + " Standard Irish and Welsh pronunciation guides, simplified for English readers."], "")

S_SOURCES = ("lore", "The Sources", "Who wrote about the Celts", [
 "No Celtic priest left a book. What we know comes from Roman and Greek writers, from medieval monks, and from the ground. Here is who is who.",
 L(("Caesar, 50s BCE","<i>The Gallic War</i>, book 6: druids, Gaulish society, and gods named by Roman names."),
   ("Diodorus and Strabo, around the turn of the era","Gaulish feasts, bards, and severed heads, passed down from an earlier Greek traveler, Posidonius."),
   ("Pliny the Elder, 77 CE","Mistletoe, oak, and the herbs the druids gathered."),
   ("Tacitus, about 116 CE","The Roman attack on the druids’ island of Mona in 60 CE."),
   ("Irish manuscripts, 1100s","The Book of Leinster and others keep older tales, written down by Christian monks."),
   ("Welsh manuscripts, 1300s","The Mabinogi and the poems of Taliesin, in the White Book of Rhydderch and the Red Book of Hergest."),
   ("The ground","The Coligny calendar from Gaul, the Gundestrup cauldron, the Llyn Cerrig Bach hoard on Anglesey, and 400 ogham stones.")),
 "Ask who wrote each source and why. The Romans wrote about enemies, and the monks wrote after the old religion had faded.",
 W + " The authors and works named here. Dates are approximate."], 
 "Which source would you most like to read first? Name it and why.")

S_WHO = ("lore", "Who Were the Celts", "Who were the Celts", [
 "The Celts are peoples who spoke Celtic languages, one branch of the Indo-European family. By about 400 BCE, Celtic speakers lived from Spain to Turkey. The best known are the Gauls in what is now France, the Britons in Britain, and the Gaels in Ireland, later Scotland and the Isle of Man.",
 "They never formed one nation, and “Celtic” was not their own name for themselves. Greek writers called the Gauls <i>Keltoi</i>. The word is now a label for a language family. The evidence differs by place: the Gauls are known from Roman writers and archaeology, while Ireland and Wales are known from medieval manuscripts, written by Christians after the old religions had faded.",
 "That is why this book keeps its places apart. When a page says “Irish,” it means Irish. When it says “Gaulish,” it means Gaul.",
 W + " Celtic languages are known from inscriptions and manuscripts. The names Keltoi and Galatai are from Greek writers."],
 "Find Gaul, Britain, and Ireland on a map. Write one thing each place is known for in the sources.")

S_APART = ("lore", "Who Were the Celts", "Keep the places apart", [
 L(("Gaul","Known from Roman writers and archaeology. The gods have Roman names in the writers, and Gaulish names on altars: Cernunnos, Epona, Taranis."),
   ("Ireland","Known from tales written by Christian monks from about 1100, which keep older material: the Tuatha Dé Danann, the Ulster heroes, the four fires, and the Brehon laws."),
   ("Wales","Known from the Mabinogi and the poems of Taliesin, copied in the 1300s: Rhiannon, Bran, Cerridwen, and the deep land of Annwn."),
   ("Scotland and Man","Known mostly from folk prayers and charms collected in the 1800s, the Carmina Gadelica, which are late.")),
 "Do not blend them. A god in an Irish tale is not the same as a god on a Gaulish altar, even when the names look alike.",
 W + " The sources named on the previous page. The Carmina Gadelica was collected by Alexander Carmichael and published in 1900."],
 "")

S_OTHER = ("lore", "The Otherworld", "The Otherworld at a glance", [
 "The Celts did not describe one afterlife. Each place told it differently. Here are the main names.",
 L(("Tír na nÓg (Ireland)","the land of the young, from the later tale of Oisín."),
   ("Mag Mell (Ireland)","the plain of delight, a happy land across the sea."),
   ("Emain Ablach (Ireland)","the isle of apples, home of Manannán."),
   ("Tech Duinn (Ireland)","the house of Donn, where the dead gather."),
   ("The sídhe (Ireland)","the hills and mounds where the Tuatha Dé went."),
   ("Annwn (Wales)","the deep, ruled by Arawn, whom Pwyll visits in the Mabinogi."),
   ("Caer Sidi (Wales)","the turning fortress, in the poems of Taliesin."),
   ("Gaul","no land is named, but Caesar says the druids taught that the soul passes from one body to another.")),
 W + " The Irish tales, the Mabinogi, the Book of Taliesin, and Caesar’s <i>Gallic War</i>. Tír na nÓg is from a late tale."],
 "Which Otherworld would you most like to read about? Name it and why.")

S_CULTURES = ("lore", "Gods and Powers", "The Tuatha Dé Danann at a glance", [
 "The Irish tales name a divine people, the Tuatha Dé Danann, “the people of the goddess Danu.” They fight the Fomorians and later go into the hills. Here are the best known.",
 L(("The Dagda","the great father, with a club and a bottomless cauldron."),
   ("Lugh","the many-skilled, who kills the giant Balor."),
   ("Nuada","the king with the silver arm."),
   ("Brigit","poetry, healing, and smithcraft."),
   ("Dian Cécht","the healer."),
   ("Goibniu","the smith."),
   ("Ogma","the warrior-poet, said to have invented ogham."),
   ("The Morrígan","battle and sovereignty, with Badb and Macha."),
   ("Manannán mac Lir","the sea, with a cloak of mist."),
   ("Aengus Óg","love and youth, at Brú na Bóinne."),
   ("Boann","the river Boyne.")),
 W + " Cath Maige Tuired (The Second Battle of Mag Tuired) and the other Irish tales, written down about 1100 and later. Danu is named in few sources."],
 "Which of these would you most like to meet? Name them and why.")

S_BRIGIT = ("lore", "Gods and Powers", "Brigit: goddess and saint", [
 "Brigit is a goddess of poetry, healing, and smithcraft. Cormac’s Glossary, an Irish word-book from about 900, calls her “the woman of wisdom” and “the goddess whom poets adored.” It says she had two sisters, also named Brigit: one a healer and one a smith.",
 "Saint Brigid of Kildare has the same name. Tradition places her in the 5th or 6th century, with a feast on 1 February, the day of Imbolc. The saint cares for cattle, milk, and healing, and around 1185 Gerald of Wales described a fire kept burning at Kildare. Scholars still argue about how much of the saint belongs to the goddess.",
 "This book tells the two apart. The goddess is in Cormac’s Glossary and the Irish tales. The saint is in the lives written by monks.",
 W + " Cormac’s Glossary (about 900) and the lives of Saint Brigid. The link between the two is debated."],
 "Which of Brigit’s three crafts is nearest to yours? Name one, and why.")

S_SALMON = ("lore", "Tales", "The salmon of knowledge", [
 "A young man named Fionn goes to study with the poet Finnegas, who has spent seven years beside the Boyne waiting for one fish. The salmon had eaten the nuts of the nine hazels that grow around the well of wisdom, and whoever eats it will know everything.",
 "Finnegas catches the salmon and tells Fionn to cook it, but not to eat any. As Fionn turns the fish, its skin blisters his thumb, and he sticks the thumb in his mouth. From that day, whenever Fionn puts his thumb in his mouth, he knows what is hidden.",
 "The tale links wisdom with water, hazel, and patience, and it says wisdom may come by accident. It is told in the Irish tales of Fionn’s boyhood.",
 W + " The medieval Irish tale of Fionn’s boyhood deeds, Macgnímartha Find."],
 "Where did you learn something by accident? Write it in one sentence.")

S_IMBAS = ("lore", "Druids, Poets, and Seers", "Imbas forosnai: the poet’s vision", [
 "<i>Imbas forosnai</i> means roughly “knowledge that illuminates.” Cormac’s Glossary, written by a Christian about 900, describes it as a rite of the Irish poets, the filid. The poet chews a piece of raw flesh, puts it on a flat stone behind the door, chants over it, and calls on gods whose names the glossator does not give. Then he sleeps with his palms on his cheeks, while others watch over him, until the answer is revealed.",
 "A related rite, the <i>tarbfeis</i>, is described in another tale. A man eats his fill of a bull killed for a feast and drinks its broth while a spell is chanted over him. Then he sleeps, and the man he sees in his dream is the next king.",
 "Notice what we have: a hostile description by a monk, not a manual. We do not know how the poets said it, or what the words were. This book gives no instructions, because the sources give none.",
 W + " Cormac’s Glossary (Sanas Chormaic) and the Irish tale Togail Bruidne Da Derga. Both were written by Christians."],
 "What would you want a vision to tell you? Write the question, and leave it unanswered.")

S_GEIS = ("lore", "Truth and Oath", "What a geis is", [
 "A <i>geis</i> is a taboo laid on a person in Irish tales. Keep it, and you are safe. Break it, and your doom follows. The best known belong to heroes.",
 L(("Cú Chulainn","forbidden to eat dog, and forbidden to refuse hospitality. A hag offers him dog meat and he eats, and he dies."),
   ("Conaire Mór","a king bound by many taboos, who breaks them one by one and is killed in a hostel."),
   ("Diarmuid","forbidden to hunt a boar, and killed by one.")),
 "Notice the pattern: a geis binds the best of the people, and fate finds the gap between two of them.",
 W + " Aided Con Culainn (Cú Chulainn’s Death), Togail Bruidne Da Derga, and the tale of Diarmuid and Gráinne."],
 "Which of these taboos would be hardest to keep? Name it, and say why.")

S_HONEST = ("lore", "The Four Fires", "An honest wheel", [
 "The Irish year had four great feasts: Samhain on 1 November, Imbolc on 1 February, Beltaine on 1 May, and Lughnasadh on 1 August. They are named in Irish texts from about 900 to 1200, and in Cormac’s Glossary. The Coligny calendar from Gaul, of the 2nd century CE, shows month names and a cycle of years. One month, Samonios, may be related to Samhain.",
 "The eight-spoke Wheel of the Year, with solstices and equinoxes, was put together in the 20th century. It is a modern tool, not an old Celtic one. There is no evidence that the solstices and equinoxes were Celtic feasts, even though older monuments like Newgrange line up with the sun.",
 "This book follows the four fires. It marks thin evidence as thin.",
 W + " The four feasts are named in Irish texts and Cormac’s Glossary. The Coligny calendar is a bronze tablet from France. The eight-spoke wheel is modern."],
 "Find which of the four fires comes next, and mark its date in ink.")

S_BELT = ("lore", "The Four Fires", "Beltaine: the two fires", [
 "Beltaine, on 1 May, opens the summer half of the year. Cormac’s Glossary says the name has to do with two fires, or a “lucky fire.” It says the druids lit two fires with incantations and drove the cattle between them each year, as protection against disease.",
 "Scholars still argue over the exact meaning of the glossary entry. Later Irish and Scottish folk custom, recorded in the 1700s and 1800s, kept bonfires and cattle-driving at the start of May, and the Carmina Gadelica records prayers for the cattle and the dairy.",
 "The old purpose is plain: protect the herd as it goes out to summer pasture. [Practice to be written from the sources.]",
 W + " Cormac’s Glossary (about 900). The later customs are from folk records."],
 "What would you protect as you go into summer? Name it.")

S_PLANTS = ("lore", "Plants and Trees", "Healing plants in the sources", [
 "No Celtic herbal survives from the Iron Age. What we have is scattered. Pliny the Elder says Gaulish druids cut mistletoe from an oak on the sixth day of the moon, with a golden sickle, and caught it in a white cloth. He also names selago, a plant gathered without iron, and samolus, a marsh plant gathered by a fasting person with the left hand.",
 "Irish myth says that after the healer Dian Cécht kills his son Miach, 365 herbs grow from the grave, one for each joint and sinew of the body, and Miach’s sister Airmed gathers them. In Wales, the Physicians of Myddfai were a family of healers whose remedies were written down from about the 1300s.",
 "Pliny was a Roman writing about another people, and the Irish tale is a myth. This book records them as history. It does not recommend any plant. If you are unwell, see a clinician.",
 W + " Pliny’s <i>Natural History</i> (77 CE), Cath Maige Tuired, and the Red Book of Hergest."],
 "Which of these plants have you seen growing near you? Note where. Do not pick it.")

S_OGHAM1 = ("lore", "Ogham", "What ogham is", [
 "Ogham (OH-um) is an alphabet of straight strokes cut along the edge of a standing stone. About 400 stones survive, most in southern Ireland and Wales, from about the 4th to the 6th century CE. The tallest, the Ballycrovane stone in County Cork, stands about 4.7 meters high.",
 "Its twenty letters fall in four groups of five, called <i>aicmí</i> (families). The strokes sit on, across, or below a central line, which is the stone’s edge. Most inscriptions are names in the form “of X, son of Y.” Scholars think ogham was made by Irish speakers who knew the Latin alphabet, so it grew out of contact with Rome. Medieval writers credit the god Ogma.",
 '<div class="ogrow">᚛ᚁᚂᚃᚄᚅ᚜</div><div class="ogrow">᚛ᚆᚇᚈᚉᚊ᚜</div><div class="ogrow">᚛ᚋᚌᚍᚎᚏ᚜</div><div class="ogrow">᚛ᚐᚑᚒᚓᚔ᚜</div>',
 "Above is the whole alphabet, one family to a line.",
 W + " The ogham stones themselves, and the medieval Irish texts that name the letters. The Latin link is the usual scholarly view."],
 "Copy the twenty letters once, slowly.")

S_OGHAM2 = ("lore", "Ogham", "The first family: Beithe", [
 "The first family is named for its first letter, Beithe (birch). Its five letters are cut as strokes to the right of the line.",
 '<table class="rt"><tr><td class="g og">ᚁ</td><td class="n">Beithe</td><td class="s">b</td><td>birch</td></tr><tr><td class="g og">ᚂ</td><td class="n">Luis</td><td class="s">l</td><td>flame or herb; later glossed as rowan</td></tr><tr><td class="g og">ᚃ</td><td class="n">Fern</td><td class="s">f or v</td><td>alder</td></tr><tr><td class="g og">ᚄ</td><td class="n">Sail</td><td class="s">s</td><td>willow</td></tr><tr><td class="g og">ᚅ</td><td class="n">Nin</td><td class="s">n</td><td>uncertain; later glossed as ash</td></tr></table>',
 "Only about five of the twenty letter names are certainly trees. The others have uncertain meanings, and the tree readings come from medieval glosses. The “tree calendar” sold today was invented in the 20th century.",
 W + " The medieval ogham treatises and the stones. The modern tree calendar is not old."],
 "Say the five names aloud, then copy the five letters.")

S_SYMBOLS = ("lore", "Symbols", "Old signs and newer ones", [
 L(("Spiral and triple spiral","carved at Newgrange in Ireland about 3200 BCE, long before the Celts. Later Celtic metalwork reused spirals."),
   ("Triskele","three-armed spirals on Celtic metalwork from about the 5th century BCE."),
   ("Torc","a neck ring, found in Gaulish graves and worn by gods and heroes in art."),
   ("Knotwork","from Insular Christian art, as in the Book of Kells, about 800 CE. It is not pre-Christian."),
   ("Celtic cross","Christian, from the high crosses of the 8th to 10th centuries."),
   ("Awen","three rays, said to be a bardic sign, but invented in the 1790s by Iolo Morganwg.")),
 '<div style="text-align:center"><img src="../triple-spiral-light.png" alt="triple spiral" style="width:1.2in"></div>',
 "Only the first three are old. The rest are later, and the pages say when.",
 W + " Newgrange and La Tène metalwork are known from archaeology. The Book of Kells is a Christian manuscript. The awen is a modern invention."],
 "Sketch a triple spiral from a photograph of a carving. Note where it was found.")

S_CHARMS = ("lore", "Charms and Prayers", "Gaulish words in Latin books", [
 "Marcellus of Bordeaux, a Gaulish official, wrote a Latin book of remedies about 400 CE, <i>De medicamentis</i>. It includes spoken charms, some of them in words scholars read as Gaulish. One is for the eye.",
 "Gaulish also survives on lead. The Larzac tablet, from about 100 CE, is the longest known Gaulish text, and it is a spell written by women. Scholars can read only part of it.",
 "So the oldest real Celtic charms are a few phrases in a Latin book and a few lead tablets. This book gives no instructions, because we cannot read enough to give them.",
 W + " Marcellus’s <i>De medicamentis</i> and the Larzac lead tablet. Both are partly understood."],
 "Which of these two would you most like to see? Name it, and why.")

SAMPLES = {
 "Welcome": [S_WELCOME, S_NAMES],
 "The Sources": [S_SOURCES],
 "Who Were the Celts": [S_WHO, S_APART],
 "The Otherworld and the Land": [S_OTHER],
 "Gods and Powers": [S_CULTURES, S_BRIGIT],
 "Tales": [S_SALMON],
 "Druids, Poets, and Seers": [S_IMBAS],
 "Truth and Oath": [S_GEIS],
 "The Four Fires": [S_HONEST, S_BELT],
 "Plants and Trees": [S_PLANTS],
 "Ogham": [S_OGHAM1, S_OGHAM2],
 "Symbols": [S_SYMBOLS],
 "Charms and Prayers": [S_CHARMS],
}

# ---------------- chapter plan ----------------
# (chapter, subtitle, total pages including divider, unused, [(page, scope, source)])
CHAPTERS = [
 ("Welcome", "Working with the Old Ways", 3, "", []),
 ("The Sources", "what we know and how", 7, "", [
   ("Who wrote about the Celts","the sources at a glance","[written]"),
   ("Roman and Greek writers","Caesar, Strabo, Diodorus, Pliny, Tacitus, and why each is hostile or second-hand","the writers themselves"),
   ("Irish manuscripts","the Book of Leinster, Lebor na hUidre, the tale lists","medieval manuscripts"),
   ("Welsh manuscripts","the White Book of Rhydderch, Red Book of Hergest, Book of Taliesin","medieval manuscripts"),
   ("What the ground gives us","Coligny calendar, Gundestrup cauldron, Llyn Cerrig Bach, La Tène, ogham stones","archaeology"),
   ("Folk collections, and what they are","Carmina Gadelica (1900) and the Physicians of Myddfai: late, and labeled so","Carmichael; Myddfai")]),
 ("Who Were the Celts", "peoples, places, and a hard truth", 7, "", [
   ("Who were the Celts","a language family, not a nation","[written]"),
   ("Keep the places apart","Gaul, Ireland, Wales, Scotland and Man","[written]"),
   ("Peoples at a glance","Gauls, Britons, Gaels, Galatians (list)","Greek and Roman writers"),
   ("Society at a glance","kings, druids, filid, warriors, farmers, Brehon law (list)","Caesar; Irish law texts"),
   ("The door and the guest","hospitality as law: the hostel, the host’s duty","Togail Bruidne Da Derga; Irish law"),
   ("Fosterage and kin","raising other people’s children; the bond that followed","Irish and Welsh law and tales")]),
 ("The Otherworld and the Land", "land, sea, sky, and the place beside them", 7, "", [
   ("Land, sea, and sky","the three divisions of the Irish world","Irish texts"),
   ("The Otherworld at a glance","every named Otherworld (list)","[written]"),
   ("The sídhe","where the Tuatha Dé went underground","Irish tales"),
   ("Journeys across","Bran, Oisín, and Pwyll","Immram Brain; Oisín; the Mabinogi"),
   ("Tara and Uisneach","the centres of Ireland","Irish tales; archaeology"),
   ("Doors and edges","shores, mounds, and Samhain night as crossing times","Irish tales")]),
 ("Gods and Powers", "Ireland, Wales, and Gaul, kept apart", 19, "", [
   ("How the three groups differ","the divine peoples of each place","[summary]"),
   ("The Tuatha Dé Danann at a glance","list","[written]"),
   ("The Dagda","club and cauldron","Cath Maige Tuired"),
   ("Lugh","the many-skilled","Cath Maige Tuired"),
   ("Brigit: goddess and saint","the goddess and the saint, kept apart","[written]"),
   ("The Morrígan and her kin","Badb, Macha, Nemain","Irish tales"),
   ("Manannán mac Lir","the sea","Irish tales"),
   ("The craft gods","Dian Cécht, Goibniu, Credne, Luchta","Cath Maige Tuired"),
   ("The Welsh gods at a glance","list","the Mabinogi; Welsh poems"),
   ("Rhiannon","horse, birds, and a hard bargain","the Mabinogi"),
   ("Bran the Blessed","the head that spoke","the Mabinogi"),
   ("Cerridwen","the cauldron","the tale of Taliesin"),
   ("Arawn","the king of Annwn","the Mabinogi"),
   ("The Gaulish gods at a glance","list","altars and Roman writers"),
   ("Cernunnos","the antlered one","Pillar of the Boatmen; Gundestrup"),
   ("Epona","the horse goddess","altars across the Roman world"),
   ("Sulis and the water goddesses","Bath, the Seine, the Boyne","altars; Irish tales"),
   ("The Mothers","triple goddesses on Gaulish-Roman reliefs","reliefs"),
   ("Battle goddesses","Morrígan, Badb, Macha, taken together","Irish tales")]),
 ("Tales", "stories from the old books", 12, "", [
   ("The Second Battle of Mag Tuired","Lugh, Balor, the end of the Fomorians","Irish tales"),
   ("Cú Chulainn takes arms","the boy who guarded Ulster","the Táin"),
   ("Cú Chulainn at the ford","the single combat with Ferdiad","the Táin"),
   ("The salmon of knowledge","Fionn’s thumb","[written]"),
   ("The Children of Lir","four swans, nine hundred years","Irish tales"),
   ("Oisín in Tír na nÓg","three hundred years in a night","Irish tales"),
   ("Pwyll and Arawn","a year in another man’s place","the Mabinogi"),
   ("Branwen and the head of Bran","war, and the head that spoke","the Mabinogi"),
   ("Blodeuwedd","the woman made of flowers","the Mabinogi"),
   ("Taliesin","the boy who stirred the cauldron","the tale of Taliesin"),
   ("Welsh Triads","three of this, three of that (list)","the Triads of the Island of Britain")]),
 ("Druids, Poets, and Seers", "the learned class", 8, "", [
   ("Who were the druids","what Caesar and Pliny say, and don’t","Caesar; Pliny"),
   ("The attack on Mona","the Roman assault of 60 CE","Tacitus"),
   ("The filid and the bards","the Irish poets, their training and rank","Irish law texts"),
   ("Imbas forosnai","the poet’s vision","[written]"),
   ("Women seers","Fedelm in the Táin and others","the Táin"),
   ("Taliesin and Myrddin","poet and wild prophet in Wales","Welsh poems"),
   ("Sitting out and sleeping on it","the tarbfeis and the wild madman’s year","Togail Bruidne Da Derga; Buile Suibhne")]),
 ("Truth and Oath", "the Celtic form of luck", 5, "", [
   ("What a geis is","taboos of the heroes (list)","[written]"),
   ("The ruler’s truth","fír flathemon: a true king brings a good year","Irish law and tales"),
   ("Oaths by the elements","swearing by sky, sea, and earth","Irish tales; Caesar"),
   ("Your vow","a lined page, built on oath-taking","lined page")]),
 ("The Other People", "the aos sí, in sources and in folklore", 5, "", [
   ("Who the aos sí are","medieval tales versus 19th-century folklore, kept apart","Irish tales; folklore"),
   ("Fairy hills and thorns","places people leave alone","folklore, labeled late"),
   ("Changelings and folk rules","what folklore says, labeled as such","folklore"),
   ("Leaving things alone","a practice built on documented custom","folklore")]),
 ("The Four Fires", "Samhain, Imbolc, Beltaine, Lughnasadh", 15, "", [
   ("An honest wheel","four fires, not eight spokes","[written]"),
   ("How each fire works here","the pattern for the chapter","[summary]"),
   ("The Coligny sidebar","the calendar from Gaul","the Coligny bronze"),
   ("Samhain, two pages","the dead, the Mag Tuired battle, a feast","Irish tales"),
   ("Imbolc, two pages","Brigit, ewes’ milk, a first stir of spring","Cormac’s Glossary; later custom"),
   ("Beltaine, two pages","the two fires, the herd","[written] and Cormac’s Glossary"),
   ("Lughnasadh, two pages","Tailtiu’s fair, games, and marriages","Irish tales"),
   ("The champion’s portion","feasting rank and the gift of meat","Fled Bricrenn"),
   ("Moon tracker","two months of looking up","calendar sticks and the Coligny calendar"),
   ("Gift log","what you gave and to whom","built on the feast pages")]),
 ("Plants and Trees", "what the sources say", 10, "", [
   ("Healing plants in the sources","Pliny, Airmed, Myddfai","[written]"),
   ("Mistletoe and oak","Pliny’s rite, with its doubts","Pliny"),
   ("Selago, samolus, and vervain","Pliny’s herbs and the rules for gathering","Pliny"),
   ("Airmed’s 365 herbs","the myth","Cath Maige Tuired"),
   ("The Physicians of Myddfai","remedies from a Welsh family of healers","Myddfai manuscripts"),
   ("Hazel and the well of wisdom","nine hazels, the salmon","Irish tales"),
   ("The Battle of the Trees","alder, rowan, and the poem","the Book of Taliesin"),
   ("Oak, yew, and apple","the sacred trees of the tales","Irish and Welsh tales"),
   ("Safety page","read first","plain fact")]),
 ("Sacred Places", "water, hills, and groves", 8, "", [
   ("Wells and springs","Sulis at Bath, Coventina, the well of Segais","altars and tablets; Irish tales"),
   ("Rivers and their goddesses","the Boyne, the Seine","Irish tales; altars"),
   ("Fords","where combats and laws were held","the Táin"),
   ("Hills and royal sites","Tara, Uisneach, Emain Macha","tales; archaeology"),
   ("Caves and doors","Oweynagat, the cave of Cruachan","Irish tales"),
   ("Groves","the nemeton: a word in place names","Roman writers; place names"),
   ("Gifts in water","La Tène, Llyn Cerrig Bach, Flag Fen","archaeology")]),
 ("Ogham", "the letters of the old Irish", 12, "", [
   ("What ogham is","","[written]"),
   ("The first family: Beithe","","[written]"),
   ("The second family: hÚath","","ogham treatises and stones"),
   ("The third family: Muin","","ogham treatises and stones"),
   ("The fourth family: Ailm","","ogham treatises and stones"),
   ("The extra letters","the forfeda, added later","ogham treatises"),
   ("Reading a stone","the “of X, son of Y” formula, with examples","the stones"),
   ("Ogham in the tales","Cú Chulainn cuts ogham on a withy","the Táin"),
   ("Writing your name","a worked example and a chart","the chart"),
   ("Carving ogham","wood, a central line, and the strokes","practical"),
   ("The tree alphabet: old and modern","what is medieval, and what Robert Graves invented in 1948","the treatises; Graves")]),
 ("Symbols", "what is old and what is newer", 4, "", [
   ("Old signs and newer ones","list with a drawing","[written]"),
   ("The spiral and the triskele","what the carvings show","archaeology"),
   ("The torc and the cauldron","gold at the neck, a pot at the feast","graves; Gundestrup; the Irish tales")]),
 ("Charms and Prayers", "what words survive", 6, "", [
   ("Gaulish words in Latin books","Marcellus of Bordeaux","[written]"),
   ("Lead tablets","Larzac and Chamalières","the tablets"),
   ("The Deer’s Cry","an Irish prayer that names the elements","a medieval text"),
   ("The caim","the encircling prayer","Carmina Gadelica, labeled late"),
   ("Learn a prayer","a practice built on the Deer’s Cry","the Deer’s Cry")]),
 ("The Dead and the Ancestors", "mounds, feasts, and names", 5, "", [
   ("Mounds and tombs","Newgrange, passage tombs, barrows","archaeology"),
   ("Feasts for the dead","Samhain and the funeral feast","Irish tales"),
   ("Names and pedigrees","reciting your descent, as the Irish did","Irish genealogies"),
   ("Tech Duinn","the house where the dead gather","Irish tales")]),
 ("Reference", "resources, reading, and a glossary", 14, "", [
   ("Resources","books behind this book","list"),
   ("Go on reading","primary texts in translation","list"),
   ("Words in this book","Irish and Welsh terms, two pages","list"),
   ("Lined pages","ten, placed after the practice chapters","lined")]),
]
