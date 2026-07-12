"""Generate listing images for A Simple Life."""

from PIL import Image, ImageDraw, ImageFont

W, H = 2000, 2000
SPLIT = 961
PAPER = (245, 240, 232)
INK = (44, 36, 22)
CLAY = (160, 133, 94)
SAGE = (125, 139, 111)
OVERLAY_ALPHA = 225

F_SERIF = '/usr/share/fonts/liberation/LiberationSerif-Regular.ttf'
F_SERIF_BOLD = '/usr/share/fonts/liberation/LiberationSerif-Bold.ttf'
F_SANS = '/usr/share/fonts/liberation/LiberationSans-Bold.ttf'
F_SANS_REG = '/usr/share/fonts/liberation/LiberationSans-Regular.ttf'

SRC = '/home/chels/test/digital-products/simple-life-guide/church-of-the-king-e6ZlCzBnGWI-unsplash.jpg'
OUT_DIR = '/home/chels/test/digital-products/simple-life-guide'


# ============================================================
# PRIMARY IMAGE — Split panel with photo
# ============================================================

photo = Image.open(SRC).convert('RGB')
pw, ph = photo.size
ratio = max(W / pw, H / ph)
nw = int(pw * ratio)
nh = int(ph * ratio)
photo = photo.resize((nw, nh), Image.LANCZOS)
left = (nw - W) // 2
top = (nh - H) // 2
photo = photo.crop((left, top, left + W, top + H))

canvas = photo.copy()
draw = ImageDraw.Draw(canvas)

# Semi-transparent cream overlay on left panel
overlay = Image.new('RGBA', (SPLIT, H), (*PAPER, OVERLAY_ALPHA))
canvas.paste(overlay, (0, 0), overlay)

# Fonts
brand_font = ImageFont.truetype(F_SANS, 36)
title_font = ImageFont.truetype(F_SERIF_BOLD, 100)
tag_font = ImageFont.truetype(F_SERIF, 48)
feat_font = ImageFont.truetype(F_SERIF, 46)

# Text positions
draw.text((50, 740), "KITCHEN & KETTLE", font=brand_font, fill=CLAY)
draw.text((50, 810), "A Simple Life", font=title_font, fill=INK)

# Tagline
tagline = "A guide to doing less, with more intention."
tag_bb = tag_font.getbbox(tagline)
tag_w = tag_bb[2] - tag_bb[0]
if tag_w > 860:
    tag_font = ImageFont.truetype(F_SERIF, 40)
draw.text((50, 950), tagline, font=tag_font, fill=SAGE)

# Features
features = [
    "Practical swaps for kitchen, bath & home",
    "The Diaper Bag Rule explained",
    "How to cut the noise of social media",
    "Permission to stop making everything from scratch",
]
y = 1080
for feat in features:
    text = "\u2022  " + feat
    bb = feat_font.getbbox(text)
    fw = bb[2] - bb[0]
    if fw > 860:
        fs = ImageFont.truetype(F_SERIF, 40)
        draw.text((50, y), text, font=fs, fill=INK)
        y += 70
    else:
        draw.text((50, y), text, font=feat_font, fill=INK)
        y += 76

primary_path = OUT_DIR + '/primary-listing.png'
canvas.save(primary_path, 'PNG', optimize=True)
print(f"Saved {primary_path}")


# ============================================================
# INFO CARD HELPER
# ============================================================

def make_info_card(filename, title, subtitle, bullets, page_note):
    img = Image.new('RGB', (2000, 2000), PAPER)
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype(F_SERIF, 140)
    tw = title_font.getbbox(title)[2] - title_font.getbbox(title)[0]
    if tw > 1800:
        title_font = ImageFont.truetype(F_SERIF, 110)

    subtitle_font = ImageFont.truetype(F_SERIF, 52)
    bullet_font = ImageFont.truetype(F_SERIF, 48)
    note_font = ImageFont.truetype(F_SANS_REG, 28)
    brand_font = ImageFont.truetype(F_SANS_REG, 28)

    title_h = title_font.getbbox(title)[3] - title_font.getbbox(title)[1]
    subtitle_h = subtitle_font.getbbox(subtitle)[3] - subtitle_font.getbbox(subtitle)[1]
    bullet_h = bullet_font.getbbox("Test")[3] - bullet_font.getbbox("Test")[1]
    note_h = note_font.getbbox(page_note)[3] - note_font.getbbox(page_note)[1]

    gap_title_sub = 40
    gap_sub_bullets = 40
    gap_between_bullets = 18
    gap_before_note = 50

    total_h = title_h + gap_title_sub + subtitle_h + gap_sub_bullets
    for _ in bullets:
        total_h += bullet_h + gap_between_bullets
    total_h += gap_before_note + note_h

    start_y = (2000 - total_h) // 2
    y = start_y
    block_x = 530

    draw.text((block_x, y), title, font=title_font, fill=INK)
    y += title_h + gap_title_sub
    draw.text((block_x, y), subtitle, font=subtitle_font, fill=SAGE)
    y += subtitle_h + gap_sub_bullets
    for line in bullets:
        if line == '':
            y += bullet_h
        else:
            draw.text((block_x, y), line, font=bullet_font, fill=INK)
            y += bullet_h + gap_between_bullets
    y += gap_before_note
    draw.text((block_x, y), page_note, font=note_font, fill=SAGE)
    draw.text((100, 1920), "Kitchen & Kettle", font=brand_font, fill=CLAY)
    img.save(filename, 'PNG', optimize=True)
    print(f"Saved {filename}")


# ============================================================
# IMAGE 2 — What's Inside
# ============================================================

make_info_card(
    OUT_DIR + '/listing-2.png',
    "What's Inside",
    "A practical guide to doing less",
    [
        '\u2022  Kitchen swaps that actually work \u2014 mason',
        '   jars, fewer oils, one brewer that does both',
        '\u2022  Bath & body simplified \u2014 bar soap,',
        '   free & clear, one moisturizer, one oil',
        '\u2022  The Diaper Bag Rule \u2014 why one good',
        '   thing beats five specialized ones',
        '\u2022  How to cut the noise and keep only',
        '   the voices that actually serve you',
    ],
    '9 pages \u00b7 printable PDF',
)


# ============================================================
# IMAGE 3 — The Diaper Bag Rule
# ============================================================

make_info_card(
    OUT_DIR + '/listing-3.png',
    "The Diaper Bag",
    "Rule",
    [
        '\u2022  One good thing that does many jobs beats',
        '   five specialized things that each do one.',
        '',
        '\u2022  The mason jar. The french press. The shop',
        '   cloth. The simple bar of soap. Each replaces',
        '   a drawer full of products you don\u2019t need.',
        '',
        '\u2022  Before you buy something new, ask: does',
        '   something I already own do this job?',
        '   Most of the time, the answer is yes.',
    ],
    'A Simple Life \u00b7 Kitchen & Kettle',
)
