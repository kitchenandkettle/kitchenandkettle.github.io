"""Generate two 2000x2000 info card images for the Recipe Cards Etsy listing."""
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

    # Fonts — match the cast iron card sizes
    title_font = ImageFont.truetype(SERIF, 140)
    # Check if title fits at 140; fall back to 110
    tw = title_font.getbbox(title)[2] - title_font.getbbox(title)[0]
    if tw > 1800:
        title_font = ImageFont.truetype(SERIF, 110)

    subtitle_font = ImageFont.truetype(SERIF, 52)
    bullet_font = ImageFont.truetype(SERIF, 48)
    note_font = ImageFont.truetype(SANS, 28)
    brand_font = ImageFont.truetype(SANS, 28)

    # --- Measure everything for vertical centering ---
    title_h = title_font.getbbox(title)[3] - title_font.getbbox(title)[1]
    subtitle_h = subtitle_font.getbbox(subtitle)[3] - subtitle_font.getbbox(subtitle)[1]
    bullet_h = bullet_font.getbbox("Test")[3] - bullet_font.getbbox("Test")[1]
    note_h = note_font.getbbox(page_note)[3] - note_font.getbbox(page_note)[1]

    gap_title_sub = 12
    gap_sub_bullets = 40
    gap_between_bullets = 18
    gap_before_note = 50

    total_h = title_h + gap_title_sub + subtitle_h + gap_sub_bullets
    for _ in bullets:
        total_h += bullet_h + gap_between_bullets
    total_h += gap_before_note + note_h

    start_y = (2000 - total_h) // 2
    y = start_y

    # --- Title (centered) ---
    tw = title_font.getbbox(title)[2] - title_font.getbbox(title)[0]
    draw.text((1000 - tw // 2, y), title, font=title_font, fill=INK)
    y += title_h + gap_title_sub

    # --- Subtitle (centered, sage) ---
    sw = subtitle_font.getbbox(subtitle)[2] - subtitle_font.getbbox(subtitle)[0]
    draw.text((1000 - sw // 2, y), subtitle, font=subtitle_font, fill=SAGE)
    y += subtitle_h + gap_sub_bullets

    # --- Bullets (left-aligned within a centered block) ---
    # The block is left-aligned at a fixed X for all bullets
    block_x = 530  # left edge of bullet text block (matches cast iron card)
    for line in bullets:
        if line == '':
            y += bullet_h  # blank line spacer
        else:
            draw.text((block_x, y), line, font=bullet_font, fill=INK)
            y += bullet_h + gap_between_bullets
    y += gap_before_note

    # --- Page note (centered, sage) ---
    nw = note_font.getbbox(page_note)[2] - note_font.getbbox(page_note)[0]
    draw.text((1000 - nw // 2, y), page_note, font=note_font, fill=SAGE)

    # --- Brand label (bottom-left) ---
    brand = "Kitchen & Kettle"
    draw.text((100, 1920), brand, font=brand_font, fill=CLAY)

    img.save(filename, 'PNG', optimize=True)
    print(f"Saved {filename}")

# --- Card 1: What's Inside ---
make_card(
    'recipe-cards-image.png',
    'Recipe Card',
    'Binder Inserts',
    [
        '\u2022  Type your recipes in your browser',
        '\u2022  No Canva, no account, no signup',
        '\u2022  13 ingredient slots per recipe',
        '\u2022  Instructions, notes, and time fields',
        '\u2022  Save a Copy keeps edits persistent',
        '\u2022  Print blank or filled \u2014 one click',
    ],
    'Interactive HTML + printable PDF  \u00b7  $4',
)

# --- Card 2: What Sets It Apart ---
make_card(
    'recipe-cards-image-2.png',
    'No Canva',
    'No Signup. No Cloud.',
    [
        '\u2022  Most printable recipe cards on Etsy',
        '   require a Canva account. These don\u2019t.',
        '',
        '\u2022  Edits save locally to your device \u2014',
        '   private, instant, and free.',
        '',
        '\u2022  Designed as binder inserts with room',
        '   for hole-punching. Standard letter paper.',
        '',
        '\u2022  Save filled pages as PDFs anytime.',
    ],
    'Letter-size  \u00b7  printable PDF  \u00b7  $4',
)
