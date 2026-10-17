"""Build split-panel Etsy primary: stock photo right, paper panel left."""
from PIL import Image, ImageDraw, ImageFont

SERIF_BOLD = '/usr/share/fonts/liberation/LiberationSerif-Bold.ttf'
SERIF = '/usr/share/fonts/liberation/LiberationSerif-Regular.ttf'
SANS = '/usr/share/fonts/liberation/LiberationSans-Regular.ttf'

PAPER = (245, 240, 232)
INK = (44, 36, 22)
CLAY = (160, 133, 94)
SAGE = (125, 139, 111)

SIZE = 2000
PANEL_W = 820
PANEL_ALPHA = 220


def build(photo_path, out_path, brand, title_lines, tagline, note):
    photo = Image.open(photo_path).convert('RGB')
    w, h = photo.size
    side = min(w, h)
    left = (w - side) // 2
    top = (h - side) // 2
    photo = photo.crop((left, top, left + side, top + side)).resize((SIZE, SIZE), Image.LANCZOS)

    canvas = photo.copy()
    panel = Image.new('RGBA', (PANEL_W, SIZE), PAPER + (PANEL_ALPHA,))
    canvas.paste(panel, (0, 0), panel)
    draw = ImageDraw.Draw(canvas)

    brand_font = ImageFont.truetype(SANS, 34)
    title_font = ImageFont.truetype(SERIF_BOLD, 118)
    tag_font = ImageFont.truetype(SERIF, 46)
    note_font = ImageFont.truetype(SANS, 30)

    pad = 70
    max_w = PANEL_W - pad * 2

    def fit(font_path, size, text):
        f = ImageFont.truetype(font_path, size)
        while f.getbbox(text)[2] - f.getbbox(text)[0] > max_w and size > 20:
            size -= 4
            f = ImageFont.truetype(font_path, size)
        return f

    brand_f = fit(SANS, 34, brand)
    title_fs = [fit(SERIF_BOLD, 118, t) for t in title_lines]
    tag_f = fit(SERIF, 46, tagline)
    note_f = fit(SANS, 30, note)

    def h(f, t):
        bb = f.getbbox(t)
        return bb[3] - bb[1]

    blocks = [(brand_f, brand, CLAY, 0)]
    for f, t in zip(title_fs, title_lines):
        blocks.append((f, t, INK, 6))
    blocks.append((tag_f, tagline, SAGE, 26))
    blocks.append((note_f, note, SAGE, 40))

    total = sum(h(f, t) + gap for f, t, _, gap in blocks)
    y = (SIZE - total) // 2
    for f, t, color, gap in blocks:
        y += gap
        draw.text((pad, y), t, font=f, fill=color)
        y += h(f, t)

    canvas.save(out_path, 'JPEG', quality=92, optimize=True)
    print(f"Saved {out_path}")


build(
    "laura-olsen-lg9QrSa8VaQ-unsplash.jpg",
    "primary-natural-bodycare-split.jpg",
    "KITCHEN & KETTLE",
    ["Natural Body", "Care Guide"],
    "Simple ingredients. Honest tradeoffs.",
    "19 pages · printable PDF",
)
