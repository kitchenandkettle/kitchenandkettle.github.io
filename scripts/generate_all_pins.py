#!/usr/bin/env python3
"""Generate ALL Pinterest pins for every product, numbered pin-1 pin-2 pin-3.
pin-1 = dark overlay (primary) — already exists as pin.png for most products
pin-2 = tip card — "DID YOU KNOW?" style
pin-3 = list card — "Inside this guide" bullets
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os, shutil

W, H = 1000, 1500
PAPER = (245, 240, 232, 166)
INK = "#2C2416"
INK_RGB = (44, 36, 22)
CLAY = "#A0855E"
CLAY_RGB = (160, 133, 94)
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
    img = Image.open(photo_path).convert("RGB")
    pw, ph = img.size
    target_ratio = W / H
    if pw / ph > target_ratio:
        new_w = int(ph * target_ratio)
        left = (pw - new_w) // 2
        img = img.crop((left, 0, left + new_w, ph))
    else:
        new_h = int(pw / target_ratio)
        top = (ph - new_h) // 2
        img = img.crop((0, top, pw, top + new_h))
    return img.resize((W, H), Image.LANCZOS)


def generate_tip_pin(photo_path, tip_text, product_name, outpath):
    base = fit_photo(photo_path)
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 80))
    base_rgba = base.convert("RGBA")
    base_rgba = Image.alpha_composite(base_rgba, overlay)

    draw_panel = ImageDraw.Draw(Image.new("RGBA", (W, H)))
    tip_font = ImageFont.truetype(FONT_SERIF_BOLD, 48)
    tip_lines = wrap_text(draw_panel, tip_text, tip_font, 650)
    name_font = ImageFont.truetype(FONT_SANS, 24)

    line_height = 62
    panel_pad_top = 70
    panel_pad_bottom = 60
    panel_content_h = len(tip_lines) * line_height + 20 + 28
    panel_h = panel_content_h + panel_pad_top + panel_pad_bottom
    panel_w = 760
    panel_x = (W - panel_w) // 2
    panel_y = (H - panel_h) // 2

    panel = Image.new("RGBA", (panel_w, panel_h), PAPER)
    shadow = Image.new("RGBA", (panel_w, panel_h), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle([4, 4, panel_w - 4, panel_h - 4], radius=12, fill=(0, 0, 0, 60))
    shadow = shadow.filter(ImageFilter.GaussianBlur(8))
    shadow_full = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    shadow_full.paste(shadow, (panel_x, panel_y), shadow)
    base_rgba = Image.alpha_composite(base_rgba, shadow_full)

    panel_draw = ImageDraw.Draw(panel)
    panel_draw.rounded_rectangle([0, 0, panel_w - 1, panel_h - 1], radius=12, fill=PAPER)

    label_font = ImageFont.truetype(FONT_SANS, 18)
    label = "DID YOU KNOW?"
    lw = textbbox(panel_draw, label, label_font)
    panel_draw.text(((panel_w - lw) // 2, 30), label, fill=CLAY, font=label_font)

    tip_y = 60
    for i, line in enumerate(tip_lines):
        lw = textbbox(panel_draw, line, tip_font)
        panel_draw.text(((panel_w - lw) // 2, tip_y + i * line_height), line, fill=INK, font=tip_font)

    name_text = f"— {product_name}"
    nw = textbbox(panel_draw, name_text, name_font)
    panel_draw.text(((panel_w - nw) // 2, tip_y + len(tip_lines) * line_height + 18), name_text, fill=CLAY, font=name_font)

    base_rgba.paste(panel, (panel_x, panel_y), panel)
    final = base_rgba.convert("RGB")
    draw = ImageDraw.Draw(final)

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
    print(f"  pin-2 -> {outpath}")


def generate_list_pin(photo_path, product_name, bullets, outpath):
    base = fit_photo(photo_path)
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 90))
    base_rgba = base.convert("RGBA")
    base_rgba = Image.alpha_composite(base_rgba, overlay)

    draw_measure = ImageDraw.Draw(Image.new("RGBA", (W, H)))
    title_font = ImageFont.truetype(FONT_SERIF_BOLD, 52)
    title_lines = wrap_text(draw_measure, product_name, title_font, 650)

    bullet_font = ImageFont.truetype(FONT_SERIF, 34)
    bullet_max_w = 620
    all_bullet_lines = []
    for bullet in bullets:
        all_bullet_lines.append(wrap_text(draw_measure, bullet, bullet_font, bullet_max_w))

    sub_font = ImageFont.truetype(FONT_SANS, 22)
    sub = "Inside this guide:"

    title_h = len(title_lines) * 62
    sub_h = 30
    bullet_spacing = 48
    bullet_gap = 22
    bullet_lines_total = sum(len(bl) for bl in all_bullet_lines)
    bullets_h = bullet_lines_total * bullet_spacing + (len(all_bullet_lines) - 1) * bullet_gap

    panel_pad_top = 55
    panel_pad_bottom = 50
    panel_content_h = title_h + 16 + sub_h + 14 + bullets_h
    panel_h = panel_content_h + panel_pad_top + panel_pad_bottom
    panel_w = 740
    panel_x = (W - panel_w) // 2
    panel_y = (H - panel_h) // 2

    panel = Image.new("RGBA", (panel_w, panel_h), (0, 0, 0, 0))
    panel_draw = ImageDraw.Draw(panel)
    panel_draw.rounded_rectangle([0, 0, panel_w - 1, panel_h - 1], radius=12, fill=PAPER)

    shadow = Image.new("RGBA", (panel_w, panel_h), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle([4, 4, panel_w - 4, panel_h - 4], radius=12, fill=(0, 0, 0, 60))
    shadow = shadow.filter(ImageFilter.GaussianBlur(8))
    shadow_full = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    shadow_full.paste(shadow, (panel_x, panel_y), shadow)
    base_rgba = Image.alpha_composite(base_rgba, shadow_full)

    y = panel_pad_top
    for line in title_lines:
        lw = textbbox(panel_draw, line, title_font)
        panel_draw.text(((panel_w - lw) // 2, y), line, fill=INK, font=title_font)
        y += 62

    y += 16
    sw = textbbox(panel_draw, sub, sub_font)
    panel_draw.text(((panel_w - sw) // 2, y), sub, fill=CLAY, font=sub_font)
    y += sub_h + 14

    for blines in all_bullet_lines:
        panel_draw.text((60, y), "—", fill=CLAY_RGB, font=bullet_font)
        for j, bline in enumerate(blines):
            panel_draw.text((100, y + j * bullet_spacing), bline, fill=INK, font=bullet_font)
        y += len(blines) * bullet_spacing + bullet_gap

    base_rgba.paste(panel, (panel_x, panel_y), panel)
    final = base_rgba.convert("RGB")
    draw = ImageDraw.Draw(final)

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
    print(f"  pin-3 -> {outpath}")


# ── FULL PRODUCT CONFIG (all 22 products) ────────────────────

PRODUCTS = [
    # ── Already have all 3 pins, just need rename ──
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
        "tip": "The crops that feed you reliably need no greenhouse, no seed starting, and no daily attention. Beans, potatoes, and winter squash grow themselves.",
        "bullets": [
            "Crops that grow without a greenhouse or daily care",
            "Simple direct-sow instructions for each crop",
            "Storage guidance so food lasts through winter"
        ]
    },
    # ── Need pin-2 and pin-3 generated ──
    {
        "name": "Moon Journal",
        "dir": "Moon-Journal",
        "photo": "product-image.png",
        "tip": "The old moon names came from what was happening on the ground. The Worm Moon meant thawing soil. The Strawberry Moon meant it was time to pick. Track all twelve in one journal.",
        "bullets": [
            "All 12 full moons with folk meanings and reflection prompts",
            "Cycle pages: New Moon intentions, Full Moon reflection",
            "68 pages, interactive — entries save to your device"
        ]
    },
    {
        "name": "Apothecary Basics",
        "dir": "apothecary-basics",
        "photo": "apothecary-basics-image.png",
        "tip": "Thirteen herbal preparation methods, from teas to tinctures to salves. The kitchen skills of a home apothecary — no herbalism background required.",
        "bullets": [
            "13 methods: teas, tinctures, oxymels, salves, and more",
            "Which method for what — quick-reference table",
            "Troubleshooting: rancid oils, salves that won't set, off smells"
        ]
    },
    {
        "name": "Egg Handling Cards",
        "dir": "egg-handling-card",
        "photo": "annie-spratt-6B9706lqxSo-unsplash.jpg",
        "tip": "The bloom is a nearly invisible coating that keeps eggs fresh on the counter for weeks. Wash it off and the egg becomes porous — it must go in the fridge immediately.",
        "bullets": [
            "Six cards per sheet — cut and tuck into every carton",
            "Covers the bloom, washing, storage, and the float test",
            "Print as many as you need — the file is yours forever"
        ]
    },
    {
        "name": "First Aid Checklist",
        "dir": "first-aid-checklist",
        "photo": "jonathan-kemper-FAqt8dbkwio-unsplash.jpg",
        "tip": "Duct tape removes splinters better than tweezers. Press firmly, pull in the direction the splinter entered, and it comes out clean. No digging, no tears.",
        "bullets": [
            "11 injury scenarios with clear numbered steps",
            "Folk remedies that actually work: duct tape, baking soda, plantain",
            "Interactive — check off steps as you go, entries save to your device"
        ]
    },
    {
        "name": "Household Binder",
        "dir": "household-binder",
        "photo": "corinne-kutz-oqCT1SnKcRY-unsplash.jpg",
        "tip": "Your phone dies. Apps log you out. Cloud services go down. A binder on a shelf still works when the power is out — that's the whole argument for paper.",
        "bullets": [
            "6 tabbed sections: home info, cleaning, maintenance, finances, kitchen, family",
            "Interactive checkboxes and fillable fields save to your device",
            "38 pages — pre-filled checklists so you're never starting from scratch"
        ]
    },
    {
        "name": "Recipe Book Dividers",
        "dir": "recipe-book-dividers",
        "photo": "recipe-book-dividers-image.png",
        "tip": "Most recipe collections grow haphazardly — a screenshot here, a torn-out page there. Ten pre-made category dividers give your recipes a proper home in any binder.",
        "bullets": [
            "10 pre-made category dividers plus 2 write-in custom tabs",
            "Fillable cover page and 2 recipe insert cards",
            "Designed to pair with Recipe Cards — same warm paper feel"
        ]
    },
    {
        "name": "Recipe Cards",
        "dir": "recipe-cards",
        "photo": "stockphoto.jpg",
        "tip": "Most printable recipe cards on Etsy require a Canva account. These don't. Open in your browser, type your recipe, print — no signups, no subscriptions.",
        "bullets": [
            "Editable in your browser — no Canva, no account, no cloud",
            "13 ingredient slots, instructions, notes, and time fields",
            "Save a Copy button — download a standalone backup anytime"
        ]
    },
    {
        "name": "Root Cellaring Guide",
        "dir": "root-cellaring-guide",
        "photo": "robert-zunikoff-2iL4Xqmxocs-unsplash.jpg",
        "tip": "Carrots stored in damp sand at 35°F stay crisp for six months. No root cellar needed — a basement corner, cold garage, or buried cooler does the job.",
        "bullets": [
            "6 modern storage methods — no construction required",
            "14 crops with exact temperature, humidity, and storage life",
            "Sand storage method that keeps carrots crisp through winter"
        ]
    },
    {
        "name": "A Simple Life Guide",
        "dir": "simple-life-guide",
        "photo": "church-of-the-king-e6ZlCzBnGWI-unsplash.jpg",
        "tip": "The Diaper Bag Rule: one good thing that does many jobs beats five specialized ones. Mason jars, bar soap, shop cloths — use what already works.",
        "bullets": [
            "Kitchen swaps: mason jars, fewer oils, one brewer, no disposables",
            "Bath & body: bar soap over pumps, free & clear, one moisturizer",
            "The DIY trap: why you don't have to make everything yourself"
        ]
    },
    {
        "name": "Ingredient Substitution Cards",
        "dir": "substitution-cards",
        "photo": "product-image.png",
        "tip": "26 common kitchen substitutions across 6 categories. When you're mid-recipe and out of buttermilk, the answer is already on your cabinet door — exact ratios, not suggestions.",
        "bullets": [
            "26 substitutions: dairy, eggs, baking, sweeteners, fats, pantry",
            "Six cards per sheet — cut, tape inside a cabinet, or hole-punch for a binder",
            "Covers what people actually Google: buttermilk, eggs, brown sugar, heavy cream"
        ]
    },
]

# ── MAIN ──────────────────────────────────────────────────────

BASE = "/home/chels/test/digital-products"
needs_rename = []
needs_tip = []
needs_list = []

for p in PRODUCTS:
    d = os.path.join(BASE, p["dir"])
    pin1 = os.path.join(d, "pin-1.png")
    pin2 = os.path.join(d, "pin-2.png")
    pin3 = os.path.join(d, "pin-3.png")
    old_pin = os.path.join(d, "pin.png")
    old_tip = os.path.join(d, "pin-tip.png")
    old_list = os.path.join(d, "pin-list.png")

    print(f"\n{p['name']}:")

    # Pin 1: rename pin.png -> pin-1.png if it exists and pin-1 doesn't
    if os.path.isfile(old_pin) and not os.path.isfile(pin1):
        shutil.copy2(old_pin, pin1)
        print(f"  pin-1.png (copied from pin.png)")

    # Pin 2: rename pin-tip.png or generate
    if os.path.isfile(old_tip) and not os.path.isfile(pin2):
        shutil.copy2(old_tip, pin2)
        print(f"  pin-2.png (copied from pin-tip.png)")
    elif os.path.isfile(pin2):
        print(f"  pin-2.png (exists)")
    else:
        photo = os.path.join(d, p["photo"])
        if os.path.isfile(photo):
            generate_tip_pin(photo, p["tip"], p["name"], pin2)
        else:
            print(f"  SKIP pin-2 — photo not found: {photo}")

    # Pin 3: rename pin-list.png or generate
    if os.path.isfile(old_list) and not os.path.isfile(pin3):
        shutil.copy2(old_list, pin3)
        print(f"  pin-3.png (copied from pin-list.png)")
    elif os.path.isfile(pin3):
        print(f"  pin-3.png (exists)")
    else:
        photo = os.path.join(d, p["photo"])
        if os.path.isfile(photo):
            generate_list_pin(photo, p["name"], p["bullets"], pin3)
        else:
            print(f"  SKIP pin-3 — photo not found: {photo}")

print("\nDone. All products should have pin-1.png, pin-2.png, pin-3.png")
