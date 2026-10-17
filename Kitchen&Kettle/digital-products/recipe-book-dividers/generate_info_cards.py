"""Generate 3 listing images for Recipe Book Dividers Etsy listing.
Image 1: Title card (typography-only primary)
Image 2: What's Inside
Image 3: What Sets It Apart
"""
from PIL import Image, ImageDraw, ImageFont

SERIF = '/usr/share/fonts/liberation/LiberationSerif-Regular.ttf'
SERIF_BOLD = '/usr/share/fonts/liberation/LiberationSerif-Bold.ttf'
SANS = '/usr/share/fonts/liberation/LiberationSans-Regular.ttf'

PAPER = (245, 240, 232)
INK = (44, 36, 22)
CLAY = (160, 133, 94)
SAGE = (125, 139, 111)


def make_info_card(filename, title, subtitle, bullets, page_note):
    """Standard left-aligned info card (for images 2 and 3)."""
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
    """Typography-only title card — centered, no bullets."""
    img = Image.new('RGB', (2000, 2000), PAPER)
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype(SERIF_BOLD, 140)
    tag_font = ImageFont.truetype(SERIF, 56)
    brand_font = ImageFont.truetype(SANS, 36)
    note_font = ImageFont.truetype(SANS, 28)

    # Measure title lines
    line_heights = []
    total_title_h = 0
    for line in title_lines:
        bb = title_font.getbbox(line)
        tw = bb[2] - bb[0]
        if tw > 1800:
            f = ImageFont.truetype(SERIF_BOLD, 110)
            bb = f.getbbox(line)
            line_heights.append((f, bb))
        else:
            line_heights.append((title_font, bb))
        total_title_h += bb[3] - bb[1] + 14

    tag_h = tag_font.getbbox(tagline)[3] - tag_font.getbbox(tagline)[1]

    # Total height: brand + title + gap + tagline + note
    brand_h = brand_font.getbbox("KITCHEN & KETTLE")[3] - brand_font.getbbox("KITCHEN & KETTLE")[1]
    note_h = note_font.getbbox("13 pages  ·  printable PDF")[3] - note_font.getbbox("13 pages  ·  printable PDF")[1]

    total_h = brand_h + 30 + total_title_h + 50 + tag_h + 80 + note_h
    start_y = (2000 - total_h) // 2
    y = start_y

    # Brand label
    brand_text = "KITCHEN & KETTLE"
    bw = brand_font.getbbox(brand_text)[2] - brand_font.getbbox(brand_text)[0]
    draw.text((1000 - bw // 2, y), brand_text, font=brand_font, fill=CLAY)
    y += brand_h + 30

    # Title lines (centered)
    for font, bb in line_heights:
        tw = bb[2] - bb[0]
        draw.text((1000 - tw // 2, y), title_lines.pop(0) if title_lines else "", font=font, fill=INK)
        y += bb[3] - bb[1] + 14

    y += 50

    # Tagline (centered)
    tw = tag_font.getbbox(tagline)[2] - tag_font.getbbox(tagline)[0]
    draw.text((1000 - tw // 2, y), tagline, font=tag_font, fill=SAGE)
    y += tag_h + 80

    # Page note
    note = "15 pages  ·  printable PDF"
    nw = note_font.getbbox(note)[2] - note_font.getbbox(note)[0]
    draw.text((1000 - nw // 2, y), note, font=note_font, fill=SAGE)

    img.save(filename, 'JPEG', quality=92, optimize=True)
    print(f"Saved {filename}")


# === IMAGE 1: Title Card (primary) ===
make_title_card(
    'primary-product-image.jpg',
    ['Recipe Book', 'Cover & Title Dividers'],
    'Works because it works.',
)

# === IMAGE 2: What's Inside ===
make_info_card(
    'recipe-book-dividers-image.png',
    "What's Inside",
    'Organize your recipe collection by category',
    [
        '\u2022  Fillable cover page with your name',
        '\u2022  10 pre-made category dividers:',
        '   Breakfast, Soups & Stews, Salads & Sides,',
        '   Main Dishes, Breads & Baking, Desserts,',
        '   Preserves & Pickles, Drinks,',
        '   Snacks & Appetizers, Holiday',
        '\u2022  2 write-in custom category pages',
        '\u2022  2 recipe insert cards \u2014 fill in your own',
        '   recipes and slip behind the dividers',
        '\u2022  Interactive \u2014 type your categories and',
        '   recipes, they save to your device',
    ],
    '15 pages \u00b7 printable & interactive',
)

# === IMAGE 3: What Sets It Apart ===
make_info_card(
    'recipe-book-dividers-image-2.png',
    'Designed to Pair',
    'With the Recipe Cards',
    [
        '\u2022  Same letter-size format — print, cut tabs,',
        '   and slip into your recipe binder.',
        '',
        '\u2022  Clay kettle logo on every divider page',
        '   ties the whole collection together.',
        '',
        '\u2022  Clean, simple design — nothing fussy,',
        '   nothing you don\u2019t need.',
        '',
        '\u2022  Two blank custom dividers so your system',
        '   grows with your recipe collection.',
    ],
    'Interactive HTML + printable PDF',
)
