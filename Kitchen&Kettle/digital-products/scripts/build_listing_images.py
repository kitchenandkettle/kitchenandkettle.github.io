#!/usr/bin/env python3
"""Composite listing image for First Aid Checklist"""
from PIL import Image, ImageDraw, ImageFont
import subprocess, os

SIZE = 2000
PANEL = 820
OPACITY = 220
MARGIN = 80
PAPER = (245, 240, 232, 220)
TEXT = (44, 36, 22)
CLAY = (160, 133, 94)
INK = (61, 54, 45)
SAGE = (125, 139, 111)

def find_font(pattern, style='Regular'):
    fps = subprocess.run(['fc-list', ':lang=en', '--format=%{file}\\n'],
                         capture_output=True, text=True).stdout.strip().split('\n')
    for f in fps:
        if pattern in f and style in f:
            return f
    raise FileNotFoundError(f"No font matching '{pattern}' '{style}'")

SERIF = find_font('LiberationSerif', 'Regular')
SANS = find_font('NotoSans', 'Regular')

def build(photo_path, out_path, title_lines, tagline, features):
    photo = Image.open(photo_path).convert('RGBA')
    pw, ph = photo.size
    if pw > ph:
        photo = photo.crop(((pw-ph)//2, 0, (pw-ph)//2+ph, ph))
    elif ph > pw:
        photo = photo.crop((0, (ph-pw)//2, pw, (ph-pw)//2+pw))
    photo = photo.resize((SIZE, SIZE), Image.LANCZOS)

    panel = Image.new('RGBA', (SIZE, SIZE), (0, 0, 0, 0))
    d = ImageDraw.Draw(panel)
    d.rectangle([(0, 0), (PANEL, SIZE)], fill=PAPER)

    shadow = Image.new('RGBA', (40, SIZE), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    for i in range(40):
        sd.line([(i, 0), (i, SIZE)], fill=(0, 0, 0, int(35 * (1 - i/40))))
    panel.paste(shadow, (PANEL, 0), shadow)

    bf = ImageFont.truetype(SANS, 20)
    tf = ImageFont.truetype(SERIF, 68)
    tf2 = ImageFont.truetype(SERIF, 52)
    gf = ImageFont.truetype(SERIF, 28)
    ff = ImageFont.truetype(SERIF, 24)

    total_h = 0
    bb = d.textbbox((0, 0), 'KITCHEN & KETTLE', font=bf)
    total_h += bb[3] - bb[1] + 10
    for line in title_lines:
        bb = d.textbbox((0, 0), line, font=tf)
        f = tf if bb[2] - bb[0] <= PANEL - MARGIN * 2 else tf2
        bb = d.textbbox((0, 0), line, font=f)
        total_h += bb[3] - bb[1] + 8
    total_h += 20 + 3 + 25
    bb = d.textbbox((0, 0), tagline, font=gf)
    total_h += bb[3] - bb[1] + 30
    for feat in features:
        bb = d.textbbox((0, 0), feat, font=ff)
        total_h += bb[3] - bb[1] + 12
    total_h += 100

    y = max(40, (SIZE - total_h) // 2)

    txt = 'KITCHEN & KETTLE'
    bb = d.textbbox((0, 0), txt, font=bf)
    d.text((MARGIN, y), txt, fill=CLAY, font=bf)
    y += bb[3] - bb[1] + 10

    for line in title_lines:
        bb = d.textbbox((0, 0), line, font=tf)
        f = tf if bb[2] - bb[0] <= PANEL - MARGIN * 2 else tf2
        bb = d.textbbox((0, 0), line, font=f)
        d.text((MARGIN, y), line, fill=TEXT, font=f)
        y += bb[3] - bb[1] + 8

    y += 20
    d.rectangle([(MARGIN, y), (MARGIN + 80, y + 3)], fill=CLAY)
    y += 3 + 25

    bb = d.textbbox((0, 0), tagline, font=gf)
    d.text((MARGIN, y), tagline, fill=INK, font=gf)
    y += bb[3] - bb[1] + 30

    for feat in features:
        bb = d.textbbox((0, 0), feat, font=ff)
        d.text((MARGIN, y), feat, fill=INK, font=ff)
        y += bb[3] - bb[1] + 12

    y += 30
    d.rectangle([(MARGIN, y), (MARGIN + 80, y + 3)], fill=SAGE)

    result = Image.alpha_composite(photo, panel).convert('RGB')
    result.save(out_path, 'PNG', quality=95)
    return os.path.getsize(out_path)

# ----- FIRST AID CHECKLIST -----
kb = build(
    '/home/chels/test/digital-products/first-aid-checklist/primary.jpg',
    '/home/chels/test/digital-products/first-aid-checklist/primary-product-image.jpg',
    ['First Aid', 'Checklist'],
    'Works because it works.',
    ['Cuts, burns, bites & splinters',
     'Folk remedies that actually work',
     'Emergency contacts & kit checklist',
     '16 pages  |  printable & interactive']
)
print(f'First Aid: {kb} bytes')

# ----- RECIPE BOOK DIVIDERS (typography only, no photo) -----
# Create a warm paper-background square with centered text
div = Image.new('RGB', (SIZE, SIZE), (245, 240, 232))
dd = ImageDraw.Draw(div)

# Decorative border
dd.rectangle([(60, 60), (SIZE-60, SIZE-60)], outline=(196, 168, 130), width=3)
dd.rectangle([(70, 70), (SIZE-70, SIZE-70)], outline=(217, 208, 193), width=1)

tf68 = ImageFont.truetype(SERIF, 68)
tf48 = ImageFont.truetype(SERIF, 48)
bf20 = ImageFont.truetype(SANS, 20)
sf24 = ImageFont.truetype(SERIF, 26)

# Brand
bb = dd.textbbox((0, 0), 'KITCHEN & KETTLE', font=bf20)
dd.text(((SIZE - (bb[2]-bb[0]))//2, 200), 'KITCHEN & KETTLE', fill=CLAY, font=bf20)

# Title
title1 = 'Recipe Book'
bb = dd.textbbox((0, 0), title1, font=tf68)
dd.text(((SIZE - (bb[2]-bb[0]))//2, 300), title1, fill=TEXT, font=tf68)

title2 = 'Cover & Title Dividers'
bb = dd.textbbox((0, 0), title2, font=tf48)
dd.text(((SIZE - (bb[2]-bb[0]))//2, 390), title2, fill=TEXT, font=tf48)

# Tagline
tag = 'Works because it works.'
bb = dd.textbbox((0, 0), tag, font=sf24)
dd.text(((SIZE - (bb[2]-bb[0]))//2, 510), tag, fill=INK, font=sf24)

# Features
features = [
    '10 pre-made category dividers',
    '2 fillable custom category pages',
    'Matching cover page with name field',
    'Designed to pair with Recipe Cards',
]
y = 650
for feat in features:
    bb = dd.textbbox((0, 0), feat, font=sf24)
    dd.text(((SIZE - (bb[2]-bb[0]))//2, y), feat, fill=INK, font=sf24)
    y += 45

# Bottom ornament
dd.rectangle([(SIZE//2 - 40, y + 30), (SIZE//2 + 40, y + 33)], fill=CLAY)

div.save('/home/chels/test/digital-products/recipe-book-dividers/primary-product-image.jpg', 'JPEG', quality=95)
print(f'Dividers: {os.path.getsize("/home/chels/test/digital-products/recipe-book-dividers/primary-product-image.jpg")} bytes')
