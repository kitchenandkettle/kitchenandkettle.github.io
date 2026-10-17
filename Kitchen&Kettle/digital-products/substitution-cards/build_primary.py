"""Build split-panel primary listing image for Substitution Cards."""
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

SRC = '/home/chels/test/digital-products/substitution-cards/primary.jpg'
DST = '/home/chels/test/digital-products/substitution-cards/primary-product-image.jpg'

# Photo fills entire canvas
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

# Brand
draw.text((50, 740), "KITCHEN & KETTLE", font=brand_font, fill=CLAY)

# Title
title = "Substitution Cards"
draw.text((50, 800), title, font=title_font, fill=INK)

# Tagline — measure to ensure fit
tagline = "The answer, before you Google it."
tw = tag_font.getbbox(tagline)[2] - tag_font.getbbox(tagline)[0]
print(f"Tagline width: {tw}px (max 860)")
if tw > 860:
    tag_font = ImageFont.truetype(F_SERIF, 44)
    tw = tag_font.getbbox(tagline)[2] - tag_font.getbbox(tagline)[0]
    print(f"Reduced to 44pt: {tw}px")
draw.text((50, 940), tagline, font=tag_font, fill=SAGE)

# Features
features = [
    "For the moment you reach for buttermilk",
    "Exact ratios \u2014 not suggestions",
    "Six categories, twenty-six swaps",
    "Print, cut, keep where you cook",
]
y = 1060
for feat in features:
    text = "\u2022  " + feat
    bb = feat_font.getbbox(text)
    w = bb[2] - bb[0]
    if w > 860:
        ff_sm = ImageFont.truetype(F_SERIF, 40)
        draw.text((50, y), text, font=ff_sm, fill=INK)
        y += 70
        print(f"  Feature overflow ({w}px), reduced to 40pt: {feat}")
    else:
        draw.text((50, y), text, font=feat_font, fill=INK)
        y += 76
        print(f"  Feature OK ({w}px): {feat}")

canvas.save(DST, 'JPEG', quality=92, optimize=True)
print(f"Saved {DST}")
