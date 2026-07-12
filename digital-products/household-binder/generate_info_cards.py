"""Generate info card listing images for Household Binder."""

from PIL import Image, ImageDraw, ImageFont

H = 2000
W = 2000
PAPER = (245, 240, 232)
INK = (44, 36, 22)
CLAY = (160, 133, 94)
SAGE = (125, 139, 111)

F_SERIF = '/usr/share/fonts/liberation/LiberationSerif-Regular.ttf'
F_SANS_REG = '/usr/share/fonts/liberation/LiberationSans-Regular.ttf'

OUT_DIR = '/home/chels/test/digital-products/household-binder'


def make_info_card(filename, title, subtitle, bullets, page_note):
    img = Image.new('RGB', (W, H), PAPER)
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

    start_y = (H - total_h) // 2
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


# IMAGE 2 — What's Inside
make_info_card(
    OUT_DIR + '/household-binder-image.png',
    "What's Inside",
    "Six tabbed sections, no starting from scratch",
    [
        '\u2022  Home Information \u2014 contacts, utilities,',
        '   password hints, pet info',
        '\u2022  Cleaning System \u2014 daily, weekly, monthly,',
        '   and seasonal checklists with checkboxes',
        '\u2022  Home Maintenance \u2014 appliance logs, repair',
        '   tracker, warranty tracker, paint records',
        '\u2022  Financial Organization \u2014 bill tracker,',
        '   subscriptions, budget worksheet, savings goals',
        '\u2022  Food & Kitchen \u2014 pantry and freezer',
        '   inventory, meal planner, grocery lists',
        '\u2022  Family Organization \u2014 important dates,',
        '   gift planning, holiday and vacation planning',
    ],
    '38 pages \u00b7 printable PDF',
)

# IMAGE 3 — No Guesswork
make_info_card(
    OUT_DIR + '/household-binder-image-2.png',
    "No Guesswork",
    "Pre-filled checklists you can actually use",
    [
        '\u2022  Stop wondering what to clean and when \u2014',
        '   the daily, weekly, monthly, and seasonal',
        '   checklists have you covered',
        '',
        '\u2022  Stop digging through email for account',
        '   numbers, vet records, or the plumber\u2019s number',
        '',
        '\u2022  Stop forgetting when you last changed the',
        '   furnace filter, pumped the septic tank, or',
        '   cleaned the chimney',
        '',
        '\u2022  Everything saves automatically. Export a',
        '   backup file so your data survives any',
        '   browser reset.',
    ],
    'Household Binder \u00b7 Kitchen & Kettle',
)
