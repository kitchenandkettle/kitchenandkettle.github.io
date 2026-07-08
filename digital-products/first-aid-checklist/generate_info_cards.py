"""Generate info card images for First Aid Checklist Etsy listing."""
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
    'first-aid-checklist-image.png',
    'First Aid',
    'Checklist',
    [
        '\u2022  11 injury scenarios with clear steps',
        '\u2022  Cuts, burns, splinters, bites & stings',
        '\u2022  Choking, nosebleeds, eye injuries & more',
        '\u2022  Folk remedies that actually work',
        '\u2022  22-item first aid kit checklist',
        '\u2022  Fillable emergency contacts page',
        '\u2022  Clear line between \u201chandle at home\u201d',
        '   and \u201cget to a doctor\u201d',
    ],
    '16 pages \u00b7 printable & interactive',
)

# --- Card 2: What Sets It Apart ---
make_card(
    'first-aid-checklist-image-2.png',
    'Not a Medical',
    'Textbook',
    [
        '\u2022  Written for real kitchens and households \u2014',
        '   not a first-aid certification manual.',
        '',
        '\u2022  Folk remedies that actually work: duct tape',
        '   for splinters, baking soda for stings,',
        '   plantain poultices, and more.',
        '',
        '\u2022  Interactive checkboxes on every scenario \u2014',
        '   track what you\u2019ve done as you go.',
        '',
        '\u2022  Designed to grab with one hand while the',
        '   other hand is under cold water.',
    ],
    'Interactive HTML + printable PDF',
)
