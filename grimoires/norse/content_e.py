"""Content E: Elves & Dwarfs chapter.
Tuple formats:
  ("lore", kicker, title, [paras], prompt)
  ("journal", kicker, prompt, lines)
  ("tracker", kicker, prompt, [row labels])
Every lore page's last para is its Where-this-comes-from line.
Voice: plain, 2nd-person. Plain voice; sources named, modern and rebuilt practices said so.
Cut: Elfshots (duplicates Liminal Places sickness para), Svartálfaheimr
standalone (folded into Bright/dark page), extra journals + edge/forge
tracker held in cuttings.py. CH_ED is the 8 lore pages that ship.
"""

CH_ELVES = [
("lore", "Elves", "Bright elves and dark elves",
 ["Elves (álfar) are shy neighbors in the old poems. You mostly glimpse them at the edge of lamplight. The Grímnismál names Álfheimr as their home. The poems often pair them with the gods in the phrase “Æsir and elves,” and the Lokasenna seats them at Ægir’s feast. They are beautiful and dangerous outsiders, tied to mounds and fields, and they are neither angels nor demons.",
  "Snorri Sturluson’s Prose Edda splits them into two groups: light-elves, bright as the sun to look at, and dark-elves, black as pitch, who live down in the earth. That split is late and tidy. The Poetic Edda names elves often but never draws the line cleanly. Some scholars think Snorri may be sorting dwarfs under another name, calling them the smiths of Svartálfaheimr, the dark-elf world. Treat the boundary as blurred.",
  "Think of the elves as unseen neighbors who watch from the edge. You can honor them by stepping softly, keeping paths clear, and leaving one quiet place alone. Practice this in one corner of your week, not in all of it.",
  "<b>Where this comes from:</b> Álfheimr is in Grímnismál, and the light and dark split is in Snorri’s Prose Edda, which is late and tidy."],
 "Name one spot near your home that feels quietly watched over. Name how you will keep it. Give it two dated lines."),
("lore", "Elves", "Freyr: lord of Álfheimr",
 ["Álfheimr, the home of the elves, was given to Freyr. The Grímnismál says it was a tooth-gift, a gift marking a child’s first tooth. The god was young and of the Vanir. No verse in the Poetic Edda explains what lordship over the elves meant in practice.",
  "Lordship here means something like neighborliness, not rule. The gift binds the elves to him the way two farms share a fence. Read the verse itself before you build any practice on it. This book builds no rite that treats Freyr as king of the elves.",
  "Freyr is linked to fair weather and good harvests on tame ground, and the elves are linked to beauty and danger at the wild edge. The poems never explain how the two meet.",
  "<b>Where this comes from:</b> The tooth-gift is in Grímnismál. This book adds no elf-king rites."],
 "Read the Grímnismál stanza that gives Álfheimr to Freyr. Write what it says and what it leaves out. Give it two dated lines."),
("lore", "Elves", "Álfablót (Alfablot): the closed door",
 ["Álfablót (alfablot) means “elf sacrifice.” It was an autumn rite, and almost everything we know comes from one traveler. Sigvatr Þórðarson (Thordarson), a skald, or court poet, of King Óláfr (Olaf), went from farm to farm in Norway seeking a bed and was turned away. In his poem Austrfararvísur (Austrfararvisur), he says each farm was holding an álfablót, which was holy and closed to strangers. The doors were barred and no guest was taken in.",
  "That closed door is nearly all outsiders saw of the rite. Sigvatr’s poem is from the early eleventh century, written at about the time. It describes being shut out, not the ritual itself. No prayer, altar plan, or list of offerings survives. The sources support only a few plain points: autumn, closed doors, and family only. Later farm custom leaves food and drink at mounds and keeps certain hills alone, but that is folk custom and not the same rite.",
  "You can keep the same spirit at home. Pick one evening, close the door to noise, eat quietly, and speak one thank-you aloud. This is one skald’s account of farms, not a rule for every farm.",
  "<b>Where this comes from:</b> The álfablót is in Sigvatr’s Austrfararvísur, a poem from the time. No account of the rite itself survives."],
 "When will you bar your door early for one quiet meal with thanks? Name the date, the meal, and the people you will thank. Give it three dated lines."),
("lore", "Elves", "Elves in the ground",
 ["Elves are still present in place names long after the Poetic Edda falls quiet. Farms and fields across Norway and Sweden carry elf-names, and Álfheimr was even the name of a region. Some stones and mounds were left alone by plows, while the plows cut straight through everything else. Icelandic sagas describe mounds honored with toasts poured at the door-stone and paths swept clean. The dead inside were called mound-dwellers, and they were not always clearly separate from elves.",
  "This is about the land, not about formal teachings. Place names last longer than the books that record them. Elf-names are shown on stones and in farm-names recorded in Landnámabók, and folk custom still shows farmers leaving certain mounds and hills alone. Iceland’s huldufolk, the hidden people, kept the same courtesy the longest.",
  "Your street may keep a version of this too, perhaps the corner no one builds on, or the tree no one cuts. You can do the same on your block: leave one tree, one patch of ground, or one corner alone. Leave it be, and do not take what is not yours.",
  "<b>Where this comes from:</b> Elf place-names and mound-honor are in old records and folk custom."],
 "Walk your block once this week and look for places people leave alone. Mark two spots. Give each one dated line."),
("lore", "Elves", "Honoring without summoning",
 ["Elves were not worshipped the way the gods were. No temple to elves has been found, and no priest is named for them. The one sign of honor on record is the closed autumn door. Offerings at mounds and hills in Icelandic sagas were small. They were poured or laid down and left alone, with no attempt to call anything up. The Lokasenna seats the elves among the gods at Ægir’s feast. They are guests and witnesses, not servants.",
  "The old practice was courtesy without command. People cleaned up edges and lowered noise near nesting ground. They asked leave before taking, and they gave thanks after. Nothing was summoned, bound, or bought. The mound toasts are a pattern in Icelandic sagas, and the quiet-edge practice is rebuilt from that pattern. It is good manners, not control.",
  "Keep one edge this way: choose one patch of ground or one shared space. Ask before you take from it, give thanks after, and leave it quieter than you found it. That is all this practice asks.",
  "<b>Where this comes from:</b> Mound offerings are in Icelandic sagas. This book offers no summoning rites."],
 "Which edge will you keep this month, using only good manners? Name place, act, and date in three lines."),
]

CH_DWARFS = [
("lore", "Dwarfs", "Born from earth and sea",
 ["Dwarfs (dvergar) are the smiths and craftsmen of the old stories, and they live in the earth and rock. The Völuspá gives them the longest list of names in the Poetic Edda but almost no description. After the gods shape the world, the dwarfs come to life in the earth, like maggots that grow in flesh, according to Snorri’s Prose Edda. In the Völuspá they are shaped from Ymir’s bones and from the blood of the sea-giant Brimir, and the gods give them mind and shape.",
  "The long list holds names like Northri and Southri, Austri and Vestri, Gandalf and Thorin. Many of the names point to stone, staff, or advice. Think of dwarfs first as powers of the earth, and only second as people. They avoid daylight and work metal. Later books make them short, comic miners with axes, and that picture is modern. The Poetic Edda shows skill, advice, and cost, and no comedy.",
  "The dwarf list was made to be said aloud. Start with four names: Northri, Southri, Austri, and Vestri. In Snorri’s Prose Edda they hold up the four corners of the sky. Say them once each day for a week.",
  "<b>Where this comes from:</b> The dwarf origins and name lists are in the Völuspá and Snorri’s Prose Edda, which is late."],
 "Which three dwarf-names will you learn first? Name them and say them aloud. Give it three dated lines."),
("lore", "Dwarfs", "Treasures from the forge",
 ["The gods could not have their finest tools without dwarfs to make them, and every gift had a cost. In Snorri Sturluson’s Skáldskaparmál (Skaldskaparmal), Loki cut the hair of Sif, Þórr’s wife, for sport, and had to pay for it. He got new hair of gold from the dwarfs called the sons of Ívaldi (Ivaldi), who also made Skíðblaðnir, a ship that folds up, and Gungnir, a spear that never misses. Then Loki bet his head against the dwarfs Brokkr and Sindri that they could not do better. They made Draupnir, a gold ring that drips more gold, Gullinbursti, a golden boar, and Mjölnir, a hammer with a short handle.",
  "Loki’s head was on the line, and only his wordplay saved him. The hammer’s handle is short because Loki, as a fly, stung the smith’s brow while he worked. The cost matters more than the shine. Every treasure costs something, good work costs effort, and careless tricks with other people’s goods bring trouble.",
  "Sif’s gold hair shows the pattern: a careless wrong is repaired by fine work, and the repair is paid for. Use that lesson in your own life. Fine work deserves to be honored, not just owned.",
  "<b>Where this comes from:</b> The Ívaldi and Brokkr treasures are in Skáldskaparmál, a late prose work."],
 "Which fine-made thing of yours needs mending? Name it, name its maker, and log the price and date in four lines."),
("lore", "Dwarfs", "Völundr (Volund) the smith",
 ["Völundr (Volund) is the greatest of the elven-smiths, a master of metal who ends up crippled and captive. The Völundarkviða (Volundarkvida) tells his story. King Níðuðr (Nidud) hamstrung him, cutting the tendons in his legs so he could not walk well, and made him forge on the king’s island. Völundr killed the king’s sons in revenge for what was done to him and made cups from their skulls. Then he flew away on wings of his own making, and the king was left grieving.",
  "Völundr is a warning, not a patron. The poem does not make him gentle. The tale is in the Poetic Edda, and it reads as stark and early. Honoring Völundr with a hammer and forge is a modern craft practice, honest only when called so. The lesson is plain: skilled people who serve a household should not be held against their will.",
  "Pay the people who make things for you fairly, and thank them by name. Work freely given and fairly paid is the everyday opposite of Völundr’s chains.",
  "<b>Where this comes from:</b> Völundr’s story is in the Völundarkviða in the Poetic Edda. Smith-patron rites are modern."],
 "Whose skilled work do you rely on without thanks? Name that person, what you owe, and one way you will thank them. Give three dated lines."),
("lore", "Dwarfs", "Alvíss (Alvis): all-wise till dawn",
 ["Alvíss (Alvis) is a dwarf who stayed talking until dawn, and that was his undoing. In the Alvíssmál (Alvissmal), Alvíss comes to claim Þórr’s daughter as his bride, saying she was promised to him. Þórr does not refuse him outright. He asks the dwarf riddles about what each world calls earth, sky, and ale, and he keeps him talking until sunrise.",
  "The poem ends with the sun in the hall. In a later telling, daylight turns dwarfs to stone, and that is how Alvíss ends. Þórr wins with talk and delay, and no magic. The lesson still applies. Answer a hard bargain with questions, not force. Sleep on a deal, and it may look different in daylight.",
  "You can use the same tactic on a hard bargain: wait for daylight, and make the other side answer your questions in writing.",
  "<b>Where this comes from:</b> The Alvíssmál is a poem in the Poetic Edda. Daylight turning dwarfs to stone is a later telling."],
 "What pressure wants you to sign now? Name it, write its three questions, and sleep before signing. Give dated lines tonight."),
]

CH_ED = CH_ELVES + CH_DWARFS
