"""Build dark overlay banner from cropped-kitcchen.jpg."""

from PIL import Image, ImageDraw, ImageFont
import math

# ── Paths ───────────────────────────────────────────────
SRC = '/home/chels/test/cropped-kitcchen.jpg'
DST = '/home/chels/test/banner-kitchen.jpg'

# ── Colors ──────────────────────────────────────────────
PAPER  = (245, 240, 232)   # #F5F0E8
ACCENT = (212, 196, 168)   # #D4C4A8
SHADOW = (0, 0, 0)

# ── Fonts ───────────────────────────────────────────────
F_SANS  = '/usr/share/fonts/liberation/LiberationSans-Bold.ttf'
F_SERIF = '/usr/share/fonts/liberation/LiberationSerif-Bold.ttf'
F_SERIF_ITALIC = '/usr/share/fonts/liberation/LiberationSerif-Italic.ttf'


def dark_gradient_overlay(w, h, top_alpha=0.30, bot_alpha=0.55):
    """Linear gradient overlay — gentler than the pin version."""
    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    pixels = overlay.load()
    for y in range(h):
        t = y / (h - 1)
        alpha = int(255 * (top_alpha + t * (bot_alpha - top_alpha)))
        for x in range(w):
            pixels[x, y] = (0, 0, 0, alpha)
    return overlay


def text_shadow(draw, xy, text, font, blur=2, color=SHADOW, opacity=100):
    """Blurred text shadow via offset copies."""
    r, g, b = color
    offsets = []
    for dx in range(-blur, blur + 1):
        for dy in range(-blur, blur + 1):
            dist = math.sqrt(dx*dx + dy*dy)
            if dist <= blur:
                offsets.append((dx, dy, dist))
    offsets.sort(key=lambda x: -x[2])
    for dx, dy, dist in offsets:
        alpha = int(opacity * (1.0 - dist / (blur + 1)) / len(offsets) * 3)
        if alpha > 0:
            fill = (r, g, b, max(1, min(255, alpha)))
            draw.text((xy[0] + dx, xy[1] + dy), text, font=font, fill=fill)


# ── Load & overlay ──────────────────────────────────────
photo = Image.open(SRC).convert('RGB')
W, H = photo.size
print(f"Source: {W}x{H}")

gradient = dark_gradient_overlay(W, H, top_alpha=0.30, bot_alpha=0.55)
canvas = photo.convert('RGBA')
canvas.paste(gradient, (0, 0), gradient)

# ── Text layer ──────────────────────────────────────────
text_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
draw = ImageDraw.Draw(text_layer)
cx, cy = W // 2, H // 2

# Title — "Kitchen & Kettle"
title = "Kitchen & Kettle"
title_font = ImageFont.truetype(F_SERIF, 160)
bbox = title_font.getbbox(title)
tw = bbox[2] - bbox[0]
th = bbox[3] - bbox[1]
tx = cx - tw // 2
ty = cy - th // 2 - 20

text_shadow(draw, (tx, ty), title, font=title_font, blur=3, opacity=120)
draw.text((tx, ty), title, font=title_font, fill=PAPER)

# Tagline
tagline = "Works because it works."
tag_font = ImageFont.truetype(F_SERIF_ITALIC, 52)
tbbox = tag_font.getbbox(tagline)
ttw = tbbox[2] - tbbox[0]
ttx = cx - ttw // 2
tty = ty + th + 30

text_shadow(draw, (ttx, tty), tagline, font=tag_font, blur=1, opacity=80)
draw.text((ttx, tty), tagline, font=tag_font, fill=ACCENT)

# Composite
canvas = Image.alpha_composite(canvas, text_layer)
canvas.convert('RGB').save(DST, 'JPEG', quality=92, optimize=True)
print(f"Saved {DST} ({W}x{H})")
