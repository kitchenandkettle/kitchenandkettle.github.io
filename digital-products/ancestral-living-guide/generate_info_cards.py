"""Generate info card images for Ancestral Living Guide Etsy listing."""
from PIL import Image, ImageDraw, ImageFont

SERIF = '/usr/share/fonts/liberation/LiberationSerif-Regular.ttf'
SERIF_BOLD = '/usr/share/fonts/liberation/LiberationSerif-Bold.ttf'
SANS = '/usr/share/fonts/liberation/LiberationSans-Regular.ttf'
SANS_BOLD = '/usr/share/fonts/liberation/LiberationSans-Bold.ttf'

PAPER = (245, 240, 232)
INK = (44, 36, 22)
CLAY = (160, 133, 94)
SAGE = (125, 139, 111)

def make_card(filename, title, subtitle, bullets, page_note):
    img = Image.new('RGB', (2000, 2000), PAPER)
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype(SERIF, 140)
    tw = title_font.getbbox(title)[2] - title_font.getbbox(title)[0]
    if tw > 1800:
        title_font = ImageFont.truetype(SERIF, 110)

    subtitle_font = ImageFont.truetype(SERIF, 52)
    bullet_font = ImageFont.truetype(SERIF, 48)
    note_font = ImageFont.truetype(SANS, 28)
    brand_font = ImageFont.truetype(SANS, 28)

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

    brand = "Kitchen & Kettle"
    draw.text((100, 1920), brand, font=brand_font, fill=CLAY)

    img.save(filename, 'PNG', optimize=True)
    print(f"Saved {filename}")


# --- Card 1: What's Inside ---
make_card(
    'ancestral-living-image.png',
    "A Different Kind",
    'of Guide',
    [
        '\u2022  The kitchen skills that earn their keep \u2014',
        '   sauerkraut, sourdough, cooking with real fats',
        '',
        '\u2022  Two crops anyone can grow, even if you\u2019ve',
        '   never touched dirt in your life',
        '',
        '\u2022  Body and household \u2014 what to make,',
        '   what to buy, and how to know the difference',
        '',
        '\u2022  Old words, old healing, old ways of seeing',
        '   the world \u2014 the stuff that still matters',
    ],
    '15 pages \u00b7 printable PDF \u00b7 $8',
)

# --- Card 2: What Sets It Apart ---
make_card(
    'ancestral-living-image-2.png',
    'No Soap',
    'Making Required',
    [
        '\u2022  This isn\u2019t a manual for becoming a',
        '   one-woman homestead. It\u2019s permission to',
        '   stop trying so hard.',
        '',
        '\u2022  Our ancestors didn\u2019t do everything',
        '   themselves. They supported the craftspeople',
        '   around them. You can too.',
        '',
        '\u2022  Twelve years of chasing the wrong version',
        '   of this \u2014 and what finally made it click.',
        '',
        '\u2022  If a skill exhausts you instead of settling',
        '   you, it\u2019s not ancestral. It\u2019s just guilt in',
        '   a mason jar.',
    ],
    'Interactive PDF \u00b7 write in your notes \u00b7 printable',
)
