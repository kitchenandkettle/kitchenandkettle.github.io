"""Build Dark Overlay Pin for Substitution Cards — 1000x1500."""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

# ── Dimensions ──────────────────────────────────────────
W, H = 1000, 1500

# ── Colors ──────────────────────────────────────────────
PAPER   = (245, 240, 232)   # #F5F0E8 — text color
ACCENT  = (212, 196, 168)   # #D4C4A8 — warm gold/clay
SHADOW  = (0, 0, 0)         # black for text shadow

# ── Fonts ───────────────────────────────────────────────
F_SANS   = '/usr/share/fonts/liberation/LiberationSans-Bold.ttf'
F_SERIF  = '/usr/share/fonts/liberation/LiberationSerif-Regular.ttf'
F_SERIF_BOLD = '/usr/share/fonts/liberation/LiberationSerif-Bold.ttf'
F_SERIF_ITALIC = '/usr/share/fonts/liberation/LiberationSerif-Italic.ttf'

# ── Paths ───────────────────────────────────────────────
SRC = '/home/chels/test/digital-products/substitution-cards/primary.jpg'
DST = '/home/chels/test/digital-products/substitution-cards/pin.png'


def load_cover(src, w, h):
    """Load image and crop/scale to cover w×h."""
    photo = Image.open(src).convert('RGB')
    pw, ph = photo.size
    ratio = max(w / pw, h / ph)
    nw = int(pw * ratio)
    nh = int(ph * ratio)
    photo = photo.resize((nw, nh), Image.LANCZOS)
    left = (nw - w) // 2
    top = (nh - h) // 2
    return photo.crop((left, top, left + w, top + h))


def dark_gradient_overlay(w, h, top_alpha=0.45, bot_alpha=0.70):
    """Linear gradient from top_alpha to bot_alpha, black."""
    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    pixels = overlay.load()
    for y in range(h):
        t = y / (h - 1)  # 0 at top, 1 at bottom
        alpha = int(255 * (top_alpha + t * (bot_alpha - top_alpha)))
        for x in range(w):
            pixels[x, y] = (0, 0, 0, alpha)
    return overlay


def text_shadow(draw, xy, text, font, blur=2, color=SHADOW, opacity=128):
    """Draw a blurred text shadow by compositing multiple offset copies."""
    r, g, b = color
    offsets = []
    steps = blur * 2 + 1
    for dx in range(-blur, blur + 1):
        for dy in range(-blur, blur + 1):
            dist = math.sqrt(dx*dx + dy*dy)
            if dist <= blur:
                offsets.append((dx, dy, dist))

    # Sort by distance so closer offsets are drawn last (on top)
    offsets.sort(key=lambda x: -x[2])

    for dx, dy, dist in offsets:
        alpha = int(opacity * (1.0 - dist / (blur + 1)) / len(offsets) * 3)
        if alpha > 0:
            fill = (r, g, b, max(1, min(255, alpha)))
            draw.text((xy[0] + dx, xy[1] + dy), text, font=font, fill=fill)


# ── Build ───────────────────────────────────────────────

# 1. Load photo
canvas = load_cover(SRC, W, H)

# 2. Apply dark gradient overlay
gradient = dark_gradient_overlay(W, H, top_alpha=0.45, bot_alpha=0.70)
canvas_rgba = canvas.convert('RGBA')
canvas_rgba.paste(gradient, (0, 0), gradient)

# 3. Set up drawing layer for text
text_layer = Image.new('RGBA', (W, H), (0, 0, 0, 0))
draw = ImageDraw.Draw(text_layer)

# 4. Layout constants
cx = W // 2  # center x

# 5. Label — 24px sans, uppercase, centered, ACCENT
label = "PRINTABLE CARDS"
label_font = ImageFont.truetype(F_SANS, 24)
label_bbox = label_font.getbbox(label)
label_w = label_bbox[2] - label_bbox[0]
label_y = 180
draw.text((cx - label_w // 2, label_y), label, font=label_font, fill=ACCENT)

# 6. Title — 100px serif bold, 3 lines, centered, PAPER, text shadow
title_lines = ["Ingredient", "Substitution", "Cards"]
title_font = ImageFont.truetype(F_SERIF_BOLD, 100)
title_y = 250
line_spacing = 110
for i, line in enumerate(title_lines):
    bbox = title_font.getbbox(line)
    tw = bbox[2] - bbox[0]
    tx = cx - tw // 2
    ty = title_y + i * line_spacing
    # Shadow
    text_shadow(draw, (tx, ty), line, font=title_font, blur=2, opacity=120)
    # Main text
    draw.text((tx, ty), line, font=title_font, fill=PAPER)

# 7. Hook — 42px serif italic, centered, ACCENT, 1px shadow
hook = "The answer, before you Google it."
hook_font = ImageFont.truetype(F_SERIF_ITALIC, 42)
hook_bbox = hook_font.getbbox(hook)
hook_w = hook_bbox[2] - hook_bbox[0]
hook_y = title_y + 3 * line_spacing + 30
hook_x = cx - hook_w // 2
text_shadow(draw, (hook_x, hook_y), hook, font=hook_font, blur=1, opacity=100)
draw.text((hook_x, hook_y), hook, font=hook_font, fill=ACCENT)

# 8. Divider — 60px accent line, centered
div_y = hook_y + 80
div_w = 60
draw.line([(cx - div_w // 2, div_y), (cx + div_w // 2, div_y)],
          fill=ACCENT, width=2)

# 9. Features — 4 bullet points, 34px serif, centered, ACCENT
features = [
    "26 common kitchen swaps",
    "Exact ratios, not suggestions",
    "Six categories, two printable pages",
    "Print, cut, keep where you cook",
]
feat_font = ImageFont.truetype(F_SERIF, 34)
feat_start_y = div_y + 50
feat_spacing = 52
for i, feat in enumerate(features):
    bbox = feat_font.getbbox(feat)
    fw = bbox[2] - bbox[0]
    fy = feat_start_y + i * feat_spacing
    draw.text((cx - fw // 2, fy), feat, font=feat_font, fill=ACCENT)

# 10. Brand bar — 22px sans, bottom-50px, centered, ACCENT
brand = "KITCHEN & KETTLE"
brand_font = ImageFont.truetype(F_SANS, 22)
brand_bbox = brand_font.getbbox(brand)
brand_w = brand_bbox[2] - brand_bbox[0]
brand_y = H - 70
draw.text((cx - brand_w // 2, brand_y), brand, font=brand_font, fill=ACCENT)

# 11. Composite text layer onto canvas
canvas_rgba = Image.alpha_composite(canvas_rgba, text_layer)

# 12. Save
canvas_rgba.convert('RGB').save(DST, 'PNG', optimize=True)
print(f"Saved {DST}")
print(f"Size: {W}x{H}")
