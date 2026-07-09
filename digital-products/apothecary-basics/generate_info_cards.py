"""Generate 3 listing images for Apothecary Basics Etsy listing."""
from PIL import Image, ImageDraw, ImageFont

SERIF = '/usr/share/fonts/liberation/LiberationSerif-Regular.ttf'
SERIF_BOLD = '/usr/share/fonts/liberation/LiberationSerif-Bold.ttf'
SANS = '/usr/share/fonts/liberation/LiberationSans-Regular.ttf'

PAPER = (245, 240, 232)
INK = (44, 36, 22)
CLAY = (160, 133, 94)
SAGE = (125, 139, 111)


def make_info_card(filename, title, subtitle, bullets, page_note):
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
    draw.text((100, 1920), "Kitchen & Kettle", font=brand_font, fill=CLAY)
    img.save(filename, 'PNG', optimize=True)
    print(f"Saved {filename}")


def make_title_card(filename, title_lines, tagline):
    img = Image.new('RGB', (2000, 2000), PAPER)
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype(SERIF_BOLD, 140)
    tag_font = ImageFont.truetype(SERIF, 56)
    brand_font = ImageFont.truetype(SANS, 36)
    note_font = ImageFont.truetype(SANS, 28)

    line_data = []
    total_title_h = 0
    remaining = list(title_lines)
    for line in remaining:
        bb = title_font.getbbox(line)
        tw = bb[2] - bb[0]
        if tw > 1800:
            f = ImageFont.truetype(SERIF_BOLD, 110)
            bb = f.getbbox(line)
        else:
            f = title_font
        line_data.append((f, bb, line))
        total_title_h += bb[3] - bb[1] + 14

    brand_text = "KITCHEN & KETTLE"
    bb = brand_font.getbbox(brand_text)
    brand_h = bb[3] - bb[1]
    tag_h = tag_font.getbbox(tagline)[3] - tag_font.getbbox(tagline)[1]
    note_h = note_font.getbbox("17 pages  ·  printable PDF")[3] - note_font.getbbox("17 pages  ·  printable PDF")[1]

    total_h = brand_h + 30 + total_title_h + 50 + tag_h + 80 + note_h
    start_y = (2000 - total_h) // 2
    y = start_y

    bw = brand_font.getbbox(brand_text)[2] - brand_font.getbbox(brand_text)[0]
    draw.text((1000 - bw // 2, y), brand_text, font=brand_font, fill=CLAY)
    y += brand_h + 30

    for font, bb, line in line_data:
        tw = bb[2] - bb[0]
        draw.text((1000 - tw // 2, y), line, font=font, fill=INK)
        y += bb[3] - bb[1] + 14

    y += 50
    tw = tag_font.getbbox(tagline)[2] - tag_font.getbbox(tagline)[0]
    draw.text((1000 - tw // 2, y), tagline, font=tag_font, fill=SAGE)
    y += tag_h + 80

    note = "17 pages  ·  printable PDF"
    nw = note_font.getbbox(note)[2] - note_font.getbbox(note)[0]
    draw.text((1000 - nw // 2, y), note, font=note_font, fill=SAGE)

    img.save(filename, 'JPEG', quality=92, optimize=True)
    print(f"Saved {filename}")


# === IMAGE 1: Title Card (primary) ===
make_title_card(
    'primary-product-image.jpg',
    ['Apothecary', 'Basics'],
    'Works because it works.',
)

# === IMAGE 2: What's Inside ===
make_info_card(
    'apothecary-basics-image.png',
    "What's Inside",
    'A beginner\u2019s guide to herbal preparations',
    [
        '\u2022  10 preparation methods with full instructions',
        '\u2022  Teas, tinctures, oxymels, infused oils,',
        '   salves, poultices, compresses, steams,',
        '   decoctions, and witch hazel',
        '\u2022  What each method is best for \u2014',
        '   and when to pick one over another',
        '\u2022  Exact supplies, ratios, and timing',
        '\u2022  Troubleshooting \u2014 what to do when',
        '   something goes wrong',
        '\u2022  Supplies checklist with clickable boxes',
    ],
    '17 pages \u00b7 printable & interactive',
)

# === IMAGE 3: What Sets It Apart ===
make_info_card(
    'apothecary-basics-image-2.png',
    'Slow Medicine',
    'For Real Kitchens',
    [
        '\u2022  Not a course in herbalism \u2014 a practical',
        '   reference for making useful things at home.',
        '',
        '\u2022  Every method tells you what it\u2019s for,',
        '   not just how to do it. You\u2019ll know whether',
        '   a tea or a tincture is the right call.',
        '',
        '\u2022  Honest about what\u2019s worth making and',
        '   what\u2019s better bought. No purity tests.',
        '',
        '\u2022  Start with one thing. Calendula salve or',
        '   elderberry oxymel. In six months you\u2019ll',
        '   have a shelf full of things you made.',
    ],
    'Interactive HTML + printable PDF',
)
