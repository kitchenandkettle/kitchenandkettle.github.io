#!/usr/bin/env python3
"""Generate 2 Pinterest pin variants per product with full-bleed photo backgrounds.
Variant B: tip card — photo + centered overlay panel with one practical tip
Variant C: list card — photo + overlay panel with 3 bullet points
Dimensions: 1000x1500 PNG
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

W, H = 1000, 1500
PAPER = (245, 240, 232, 166)  # RGBA — 65% opacity
INK = "#2C2416"
INK_RGB = (44, 36, 22)
CLAY = "#A0855E"
CLAY_RGB = (160, 133, 94)
SAGE = "#7D8B6F"
WHITE = (255, 255, 255)

FONT_SERIF = "/usr/share/fonts/liberation/LiberationSerif-Regular.ttf"
FONT_SERIF_BOLD = "/usr/share/fonts/liberation/LiberationSerif-Bold.ttf"
FONT_SERIF_ITALIC = "/usr/share/fonts/liberation/LiberationSerif-Italic.ttf"
FONT_SANS = "/usr/share/fonts/liberation/LiberationSans-Regular.ttf"
FONT_SANS_BOLD = "/usr/share/fonts/liberation/LiberationSans-Bold.ttf"


def textbbox(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]


def wrap_text(draw, text, font, max_w):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = f"{current} {word}".strip()
        if textbbox(draw, test, font) <= max_w:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def fit_photo(photo_path):
    """Load photo and crop to 1000x1500 cover."""
    img = Image.open(photo_path).convert("RGB")
    pw, ph = img.size
    target_ratio = W / H  # 2/3
    
    if pw / ph > target_ratio:
        # Photo is wider — crop sides
        new_w = int(ph * target_ratio)
        left = (pw - new_w) // 2
        img = img.crop((left, 0, left + new_w, ph))
    else:
        # Photo is taller — crop top/bottom
        new_h = int(pw / target_ratio)
        top = (ph - new_h) // 2
        img = img.crop((0, top, pw, top + new_h))
    
    return img.resize((W, H), Image.LANCZOS)


def generate_tip_pin(photo_path, tip_text, product_name, outpath):
    """Variant B: Photo background + centered overlay card with tip."""
    base = fit_photo(photo_path)
    
    # Darken photo slightly for text readability
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 80))
    base_rgba = base.convert("RGBA")
    base_rgba = Image.alpha_composite(base_rgba, overlay)
    
    # Cream panel — centered, auto-sized to content
    draw_panel = ImageDraw.Draw(Image.new("RGBA", (W, H)))
    
    # Measure tip text
    tip_font = ImageFont.truetype(FONT_SERIF_BOLD, 48)
    tip_lines = wrap_text(draw_panel, tip_text, tip_font, 650)
    
    # Measure product name
    name_font = ImageFont.truetype(FONT_SANS, 24)
    
    # Panel dimensions
    line_height = 62
    panel_pad_top = 70
    panel_pad_bottom = 60
    panel_content_h = len(tip_lines) * line_height + 20 + 28  # tip lines + gap + name
    panel_h = panel_content_h + panel_pad_top + panel_pad_bottom
    panel_w = 760
    panel_x = (W - panel_w) // 2
    panel_y = (H - panel_h) // 2
    
    # Draw cream panel
    panel = Image.new("RGBA", (panel_w, panel_h), PAPER)
    
    # Add subtle shadow by drawing a slightly offset darker panel behind
    shadow = Image.new("RGBA", (panel_w, panel_h), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle(
        [4, 4, panel_w - 4, panel_h - 4], radius=12,
        fill=(0, 0, 0, 60)
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(8))
    
    # Composite shadow behind panel
    shadow_full = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    shadow_full.paste(shadow, (panel_x, panel_y), shadow)
    base_rgba = Image.alpha_composite(base_rgba, shadow_full)
    
    # Draw panel
    panel_draw = ImageDraw.Draw(panel)
    panel_draw.rounded_rectangle(
        [0, 0, panel_w - 1, panel_h - 1], radius=12,
        fill=PAPER
    )
    
    # "DID YOU KNOW?" label at top of panel
    label_font = ImageFont.truetype(FONT_SANS, 18)
    label = "DID YOU KNOW?"
    lw = textbbox(panel_draw, label, label_font)
    panel_draw.text(((panel_w - lw) // 2, 30), label, fill=CLAY, font=label_font)
    
    # Tip text
    tip_y = 60
    for i, line in enumerate(tip_lines):
        lw = textbbox(panel_draw, line, tip_font)
        panel_draw.text(((panel_w - lw) // 2, tip_y + i * line_height), line, fill=INK, font=tip_font)
    
    # Product name at bottom
    name_text = f"— {product_name}"
    nw = textbbox(panel_draw, name_text, name_font)
    panel_draw.text(
        ((panel_w - nw) // 2, tip_y + len(tip_lines) * line_height + 18),
        name_text, fill=CLAY, font=name_font
    )
    
    # Composite panel onto photo
    base_rgba.paste(panel, (panel_x, panel_y), panel)
    
    # Brand at top
    final = base_rgba.convert("RGB")
    draw = ImageDraw.Draw(final)
    brand_font = ImageFont.truetype(FONT_SANS_BOLD, 22)
    brand = "KITCHEN & KETTLE"
    
    # Semi-transparent top bar for brand
    top_bar = Image.new("RGBA", (W, 50), (0, 0, 0, 120))
    base_rgba2 = final.convert("RGBA")
    base_rgba2.paste(top_bar, (0, 0), top_bar)
    final = base_rgba2.convert("RGB")
    draw = ImageDraw.Draw(final)
    
    bw = textbbox(draw, brand, brand_font)
    draw.text(((W - bw) // 2, 10), brand, fill="#F5F0E8", font=brand_font)
    
    final.save(outpath, "PNG", optimize=True)
    print(f"  -> {outpath}")


def generate_list_pin(photo_path, product_name, bullets, outpath):
    """Variant C: Photo background + overlay panel with bullets."""
    base = fit_photo(photo_path)
    
    # Darken photo
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 90))
    base_rgba = base.convert("RGBA")
    base_rgba = Image.alpha_composite(base_rgba, overlay)
    
    draw_measure = ImageDraw.Draw(Image.new("RGBA", (W, H)))
    
    # Measure title
    title_font = ImageFont.truetype(FONT_SERIF_BOLD, 52)
    title_lines = wrap_text(draw_measure, product_name, title_font, 650)
    
    # Measure bullets
    bullet_font = ImageFont.truetype(FONT_SERIF, 34)
    bullet_max_w = 620
    all_bullet_lines = []
    for bullet in bullets:
        all_bullet_lines.append(wrap_text(draw_measure, bullet, bullet_font, bullet_max_w))
    
    # Measure subtitle
    sub_font = ImageFont.truetype(FONT_SANS, 22)
    sub = "Inside this guide:"
    
    # Panel dimensions
    title_h = len(title_lines) * 62
    sub_h = 30
    bullet_spacing = 48
    bullet_gap = 22  # gap between bullet items
    bullet_lines_total = sum(len(bl) for bl in all_bullet_lines)
    bullets_h = bullet_lines_total * bullet_spacing + (len(all_bullet_lines) - 1) * bullet_gap
    
    panel_pad_top = 55
    panel_pad_bottom = 50
    panel_content_h = title_h + 16 + sub_h + 14 + bullets_h
    panel_h = panel_content_h + panel_pad_top + panel_pad_bottom
    panel_w = 740
    panel_x = (W - panel_w) // 2
    panel_y = (H - panel_h) // 2
    
    # Draw cream panel
    panel = Image.new("RGBA", (panel_w, panel_h), (0, 0, 0, 0))
    panel_draw = ImageDraw.Draw(panel)
    panel_draw.rounded_rectangle(
        [0, 0, panel_w - 1, panel_h - 1], radius=12,
        fill=PAPER
    )
    
    # Shadow
    shadow = Image.new("RGBA", (panel_w, panel_h), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle(
        [4, 4, panel_w - 4, panel_h - 4], radius=12,
        fill=(0, 0, 0, 60)
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(8))
    shadow_full = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    shadow_full.paste(shadow, (panel_x, panel_y), shadow)
    base_rgba = Image.alpha_composite(base_rgba, shadow_full)
    
    # Render panel content
    y = panel_pad_top
    
    # Title
    for line in title_lines:
        lw = textbbox(panel_draw, line, title_font)
        panel_draw.text(((panel_w - lw) // 2, y), line, fill=INK, font=title_font)
        y += 62
    
    y += 16
    sw = textbbox(panel_draw, sub, sub_font)
    panel_draw.text(((panel_w - sw) // 2, y), sub, fill=CLAY, font=sub_font)
    y += sub_h + 14
    
    # Bullets
    for blines in all_bullet_lines:
        # Dash on first line
        panel_draw.text((60, y), "—", fill=CLAY_RGB, font=bullet_font)
        for j, bline in enumerate(blines):
            panel_draw.text((100, y + j * bullet_spacing), bline, fill=INK, font=bullet_font)
        y += len(blines) * bullet_spacing + bullet_gap
    
    # Composite
    base_rgba.paste(panel, (panel_x, panel_y), panel)
    final = base_rgba.convert("RGB")
    draw = ImageDraw.Draw(final)
    
    # Top bar with brand
    top_bar = Image.new("RGBA", (W, 50), (0, 0, 0, 120))
    base_rgba2 = final.convert("RGBA")
    base_rgba2.paste(top_bar, (0, 0), top_bar)
    final = base_rgba2.convert("RGB")
    draw = ImageDraw.Draw(final)
    
    brand_font = ImageFont.truetype(FONT_SANS_BOLD, 22)
    brand = "KITCHEN & KETTLE"
    bw = textbbox(draw, brand, brand_font)
    draw.text(((W - bw) // 2, 10), brand, fill="#F5F0E8", font=brand_font)
    
    final.save(outpath, "PNG", optimize=True)
    print(f"  -> {outpath}")


# ── Product config ────────────────────────────────────────────
# photo: filename relative to product dir, or None if missing

PRODUCTS = [
    {
        "name": "Apothecary Journal",
        "dir": "apothecary-journal",
        "photo": "bottle.jpg",
        "tip": "Steep 2 tsp dried herb in 1 cup boiled water for 10 minutes, strain, and you have real herbal tea. No special equipment needed.",
        "bullets": [
            "How to make herbal tea, salves, tinctures, and infused oils",
            "Step-by-step methods with room for your own experiments",
            "No dosage charts or medical claims — just practical recipes"
        ]
    },
    {
        "name": "DIY Beeswax Wraps",
        "dir": "beeswax-wraps",
        "photo": "beeswax.jpg",
        "tip": "Three ingredients, an oven, and 20 minutes. Cotton + beeswax + pine resin + jojoba oil makes a wrap that replaces plastic for up to a year.",
        "bullets": [
            "The 3-ingredient recipe with exact ratios",
            "Oven method — no double boiler, no mess",
            "Care and refresh instructions for a full year of use"
        ]
    },
    {
        "name": "Body Care Guide",
        "dir": "body-care-guide",
        "photo": "croppedpexels-karola-g-4735910.jpg",
        "tip": "Most 'natural' soaps use essential oils that can trigger skin reactions. The gentlest option is often the shortest ingredient list — fragrance-free and dye-free.",
        "bullets": [
            "How to read soap labels and spot irritants",
            "Building a simple routine without 10 steps",
            "Tallow balm, infused oils, and salve recipes"
        ]
    },
    {
        "name": "Cast Iron Guide",
        "dir": "cast-iron-guide",
        "photo": "Cast-Iron.jpg",
        "tip": "Skip the salt scrub and chain mail. After cooking, hot water and a stiff brush is all you need. Dry it on the stove for 2 minutes and it's done.",
        "bullets": [
            "Oven seasoning step by step, no flaky layers",
            "Daily care that takes 2 minutes",
            "Thrift store restoration and troubleshooting table"
        ]
    },
    {
        "name": "Chicken Keeping Guide",
        "dir": "chicken-keeping-guide",
        "photo": "Chicken.jpg",
        "tip": "The daily routine takes 5 minutes: food, water, eggs, and a quick coop check. Predator-proofing matters more than fancy feeders.",
        "bullets": [
            "Breed guide for cold-hardy, friendly layers",
            "Coop setup with predator protection that works",
            "The 5-minute daily routine and winter care"
        ]
    },
    {
        "name": "Egg Preservation Guide",
        "dir": "egg-preservation-guide",
        "photo": "eggs.jpg",
        "tip": "Water glassing keeps fresh eggs at room temperature for 6-8 months using just pickling lime and water. Only unwashed, clean eggs work — don't wash the bloom off.",
        "bullets": [
            "Freezing for baking, water glassing for backup, pickling for snacks",
            "Clear brine ratios with no guesswork",
            "How to tell if preserved eggs are still good"
        ]
    },
    {
        "name": "Homekeeping Guide",
        "dir": "homekeeping-guide",
        "photo": "natural-home-guide.jpg",
        "tip": "You don't need a different spray bottle for every surface. Five DIY recipes from a seven-ingredient pantry clean an entire house — and they actually work.",
        "bullets": [
            "Seven-ingredient cleaning pantry with real alternatives",
            "Five DIY recipes including glass cleaner and scrub",
            "Daily rhythms, weekly reset, and twice-a-year deep clean"
        ]
    },
    {
        "name": "Honey Handbook",
        "dir": "honey-handbook",
        "photo": "honey.jpg",
        "tip": "Honey never spoils. Archaeologists found 3,000-year-old honey in Egyptian tombs — still edible. Store it sealed at room temperature and it lasts forever.",
        "bullets": [
            "How bees make honey and why it lasts forever",
            "6 kitchen recipes including Hot Honey and Honey Butter",
            "Varietal guide from clover to manuka, storage and traditional uses"
        ]
    },
    {
        "name": "Kitchen Planner Bundle",
        "dir": "kitchen-planner-bundle",
        "photo": "kitchen.jpg",
        "tip": "A grocery list organized by store section — produce, dairy, pantry, frozen — cuts shopping time in half. No more backtracking through aisles.",
        "bullets": [
            "Weekly meal planner and grocery list by store section",
            "Pantry and freezer inventory so you stop overbuying",
            "Prep checklist for smooth cooking days"
        ]
    },
    {
        "name": "Preservation Logbook",
        "dir": "preservation-logbook",
        "photo": "food-preserve.jpg",
        "tip": "The best preservation method is the one you'll actually eat. Track what you made, when it's ready, and what got used — so next year you preserve smarter.",
        "bullets": [
            "Canning, fermenting, dehydrating, and freezing logs",
            "Seasonal produce guide so you know what's in season",
            "Year-end review to plan next year's batches"
        ]
    },
    {
        "name": "Recipe Cards",
        "dir": "recipe-cards",
        "photo": None,  # needs photo
        "tip": "Recipe cards that feel like they belong in a working kitchen. Two cards per page, print as many as you need — no fancy binder required.",
        "bullets": [
            "Five themes: Classic, Garden, Baker's, Hearth, Farmhouse",
            "Warm notebook-paper feel, two cards per page",
            "Print and reprint — the file is yours forever"
        ]
    },
    {
        "name": "Seasonal Preservation Calendar",
        "dir": "seasonal-preservation-calendar",
        "photo": "pickle.jpg",
        "tip": "June strawberries don't wait. The calendar tells you what's in season each month and the best way to preserve it — freeze, can, ferment, dehydrate, or root cellar.",
        "bullets": [
            "Month-by-month produce guide with preservation methods",
            "Honest notes on what's worth the effort",
            "Recipes for marmalade and preserved lemons included"
        ]
    },
    {
        "name": "Survival Garden Basics",
        "dir": "survival-garden-basics",
        "photo": "pumpkin.jpg",
        "tip": "The crops that feed you reliably need no greenhouse, no seed starting, and no daily attention. Beans, potatoes, and winter squash grow themselves — just add dirt, sun, and water.",
        "bullets": [
            "Crops that grow without a greenhouse or daily care",
            "Simple direct-sow instructions for each crop",
            "Storage guidance so food lasts through winter"
        ]
    }
]


BASE = "/home/chels/test/digital-products"
missing_photos = []

for p in PRODUCTS:
    d = os.path.join(BASE, p["dir"])
    
    if p["photo"] is None:
        missing_photos.append(p["name"])
        print(f"\n{p['name']}: SKIP — no photo available")
        continue
    
    photo = os.path.join(d, p["photo"])
    if not os.path.isfile(photo):
        missing_photos.append(p["name"])
        print(f"\n{p['name']}: SKIP — photo not found: {photo}")
        continue
    
    print(f"\n{p['name']}:")
    generate_tip_pin(photo, p["tip"], p["name"], os.path.join(d, "pin-tip.png"))
    generate_list_pin(photo, p["name"], p["bullets"], os.path.join(d, "pin-list.png"))

if missing_photos:
    print(f"\n⚠ Missing photos for: {', '.join(missing_photos)}")

print(f"\nDone.")
