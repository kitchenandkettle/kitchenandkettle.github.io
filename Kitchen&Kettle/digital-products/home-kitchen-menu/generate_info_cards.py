"""Generate Etsy info cards for the Home Kitchen Menu."""
from PIL import Image, ImageDraw, ImageFont

SERIF = "/usr/share/fonts/liberation/LiberationSerif-Regular.ttf"
SANS = "/usr/share/fonts/liberation/LiberationSans-Regular.ttf"

PAPER = (245, 240, 232)
INK = (44, 36, 22)
CLAY = (160, 133, 94)
SAGE = (125, 139, 111)


def make_card(filename, title, subtitle, bullets, page_note):
    img = Image.new("RGB", (2000, 2000), PAPER)
    draw = ImageDraw.Draw(img)

    title_font = ImageFont.truetype(SERIF, 140)
    if title_font.getbbox(title)[2] - title_font.getbbox(title)[0] > 1800:
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
    total_h += sum(bullet_h + gap_between_bullets for _ in bullets)
    total_h += gap_before_note + note_h

    x = 530
    y = (2000 - total_h) // 2
    draw.text((x, y), title, font=title_font, fill=INK)
    y += title_h + gap_title_sub
    draw.text((x, y), subtitle, font=subtitle_font, fill=SAGE)
    y += subtitle_h + gap_sub_bullets

    for line in bullets:
        if line:
            draw.text((x, y), line, font=bullet_font, fill=INK)
        y += bullet_h + gap_between_bullets

    y += gap_before_note
    draw.text((x, y), page_note, font=note_font, fill=SAGE)
    draw.text((100, 1920), "Kitchen & Kettle", font=brand_font, fill=CLAY)
    img.save(filename, "PNG", optimize=True)
    print(f"Saved {filename}")


make_card(
    "home-kitchen-menu-image.png",
    "Three Ways",
    "to plan dinner",
    [
        "•  The Full Spread — for the whole restaurant",
        "   experience, from starters to dessert",
        "",
        "•  The Simple Board — for weeknight reality",
        "   when dinner just needs to happen",
        "",
        "•  The Greatest Hits — your own categories",
        "   for the meals your household actually makes",
    ],
    "Three fillable styles · interactive HTML + printable PDF",
)

make_card(
    "home-kitchen-menu-image-2.png",
    "Your Kitchen",
    "your rules",
    [
        "•  Type directly in your browser, or print a",
        "   blank menu and fill it in by hand",
        "",
        "•  Entries save automatically on your device",
        "   with no account and no cloud storage",
        "",
        "•  Put the menu where everyone can see it",
        "   and retire the what's-for-dinner question",
    ],
    "Letter-size · private local saving · made for home printing",
)
