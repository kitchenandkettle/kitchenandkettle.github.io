#!/usr/bin/env python3
"""Generate 2 additional pin variants per product.
Variant B: tip card (one useful fact)
Variant C: list card (3 things inside)
Dimensions: 1000x1500 PNG
"""

from PIL import Image, ImageDraw, ImageFont
import json
import os

W, H = 1000, 1500
PAPER = "#F5F0E8"
INK = "#2C2416"
CLAY = "#A0855E"
SAGE = "#7D8B6F"
FONT_SERIF = "/usr/share/fonts/liberation/LiberationSerif-Regular.ttf"
FONT_SERIF_BOLD = "/usr/share/fonts/liberation/LiberationSerif-Bold.ttf"
FONT_SERIF_ITALIC = "/usr/share/fonts/liberation/LiberationSerif-Italic.ttf"
FONT_SANS = "/usr/share/fonts/liberation/LiberationSans-Regular.ttf"
FONT_SANS_BOLD = "/usr/share/fonts/liberation/LiberationSans-Bold.ttf"

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def textbbox(draw, text, font):
    """Get pixel-accurate text width using new PIL textbbox."""
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]

def wrap_text(draw, text, font, max_w):
    """Wrap text to fit within max_w pixels."""
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

def generate_tip_pin(product_name, tip_text, tagline, outpath):
    """Variant B: Single practical tip on paper background."""
    img = Image.new("RGB", (W, H), hex_to_rgb(PAPER))
    draw = ImageDraw.Draw(img)

    # Decorative top line
    draw.rectangle([100, 60, 900, 62], fill=hex_to_rgb(CLAY))

    # Brand label at top
    brand_font = ImageFont.truetype(FONT_SANS, 28)
    brand_text = "Kitchen & Kettle"
    bw = textbbox(draw, brand_text, brand_font)
    draw.text(((W - bw) // 2, 85), brand_text, fill=hex_to_rgb(CLAY), font=brand_font)

    # "Did you know?" header
    header_font = ImageFont.truetype(FONT_SANS, 22)
    header_text = "DID YOU KNOW?"
    hw = textbbox(draw, header_text, header_font)
    draw.text(((W - hw) // 2, 140), header_text, fill=hex_to_rgb(SAGE), font=header_font)

    # Tip text - large, centered, wrapped
    tip_font = ImageFont.truetype(FONT_SERIF, 52)
    lines = wrap_text(draw, tip_text, tip_font, 780)
    
    total_h = len(lines) * 72
    start_y = 500 if len(lines) <= 3 else 400
    
    for i, line in enumerate(lines):
        lw = textbbox(draw, line, tip_font)
        draw.text(((W - lw) // 2, start_y + i * 72), line, fill=hex_to_rgb(INK), font=tip_font)

    # Product name below tip
    name_font = ImageFont.truetype(FONT_SANS_BOLD, 24)
    name_text = f"— from {product_name}"
    nw = textbbox(draw, name_text, name_font)
    tip_end_y = start_y + len(lines) * 72 + 60
    draw.text(((W - nw) // 2, tip_end_y), name_text, fill=hex_to_rgb(CLAY), font=name_font)

    # Bottom: tagline
    tag_font = ImageFont.truetype(FONT_SERIF_ITALIC, 28)
    tag_text = f'"{tagline}"'
    tw = textbbox(draw, tag_text, tag_font)
    draw.text(((W - tw) // 2, tip_end_y + 80), tag_text, fill=hex_to_rgb(SAGE), font=tag_font)

    # Bottom brand
    bottom_font = ImageFont.truetype(FONT_SANS, 20)
    bottom_text = "kitchenandkettle.etsy.com"
    bw2 = textbbox(draw, bottom_text, bottom_font)
    draw.text(((W - bw2) // 2, H - 80), bottom_text, fill=hex_to_rgb(CLAY), font=bottom_font)

    # Decorative bottom line
    draw.rectangle([100, H - 62, 900, H - 60], fill=hex_to_rgb(CLAY))

    img.save(outpath, "PNG", optimize=True)
    print(f"  -> {outpath}")


def generate_list_pin(product_name, bullets, outpath):
    """Variant C: 'Inside this guide' with bullet points."""
    img = Image.new("RGB", (W, H), hex_to_rgb(PAPER))
    draw = ImageDraw.Draw(img)

    # Decorative top line
    draw.rectangle([100, 60, 900, 62], fill=hex_to_rgb(CLAY))

    # Title
    title_font = ImageFont.truetype(FONT_SERIF_BOLD, 64)
    title_lines = wrap_text(draw, product_name, title_font, 800)
    ty = 120
    for line in title_lines:
        lw = textbbox(draw, line, title_font)
        draw.text(((W - lw) // 2, ty), line, fill=hex_to_rgb(INK), font=title_font)
        ty += 80

    # Subtitle
    sub_font = ImageFont.truetype(FONT_SANS, 26)
    sub_text = "Inside this guide:"
    sw = textbbox(draw, sub_text, sub_font)
    draw.text(((W - sw) // 2, ty + 30), sub_text, fill=hex_to_rgb(SAGE), font=sub_font)

    # Bullet points — wrap long lines
    bullet_font = ImageFont.truetype(FONT_SERIF, 38)
    bullet_y = ty + 120
    bullet_max_w = 730  # leaves room for dash + left margin
    
    for bullet in bullets:
        b_lines = wrap_text(draw, bullet, bullet_font, bullet_max_w)
        # Dash on first line only
        draw.text((140, bullet_y), "—", fill=hex_to_rgb(CLAY), font=bullet_font)
        for j, bline in enumerate(b_lines):
            draw.text((190, bullet_y + j * 50), bline, fill=hex_to_rgb(INK), font=bullet_font)
        bullet_y += len(b_lines) * 50 + 30  # gap between bullets

    # Bottom: printable guide callout
    callout_font = ImageFont.truetype(FONT_SANS_BOLD, 24)
    callout = "Printable PDF"
    cw = textbbox(draw, callout, callout_font)
    draw.text(((W - cw) // 2, H - 140), callout, fill=hex_to_rgb(INK), font=callout_font)

    # URL
    url_font = ImageFont.truetype(FONT_SANS, 20)
    url = "kitchenandkettle.etsy.com"
    uw = textbbox(draw, url, url_font)
    draw.text(((W - uw) // 2, H - 100), url, fill=hex_to_rgb(CLAY), font=url_font)

    # Decorative bottom line
    draw.rectangle([100, H - 62, 900, H - 60], fill=hex_to_rgb(CLAY))

    img.save(outpath, "PNG", optimize=True)
    print(f"  -> {outpath}")


# ── Product config ────────────────────────────────────────────

PRODUCTS = [
    {
        "name": "Apothecary Journal",
        "dir": "apothecary-journal",
        "tip": "Steep 2 tsp dried herb in 1 cup boiled water for 10 minutes, strain, and you have real herbal tea. No special equipment needed.",
        "tagline": "Make it. Record it. Remember it.",
        "bullets": [
            "How to make herbal tea, salves, tinctures, and infused oils",
            "Step-by-step methods with room for your own experiments",
            "No dosage charts or medical claims — just practical recipes"
        ]
    },
    {
        "name": "DIY Beeswax Wraps",
        "dir": "beeswax-wraps",
        "tip": "Three ingredients, an oven, and 20 minutes. Cotton + beeswax + pine resin + jojoba oil makes a washable wrap that replaces plastic for up to a year.",
        "tagline": "Plastic wrap, retired.",
        "bullets": [
            "The 3-ingredient recipe with exact ratios",
            "Oven method — no double boiler, no mess",
            "Care and refresh instructions for a full year of use"
        ]
    },
    {
        "name": "Body Care Guide",
        "dir": "body-care-guide",
        "tip": "Most 'natural' soaps use essential oils that can trigger skin reactions. The gentlest option is often the shortest ingredient list — fragrance-free and dye-free.",
        "tagline": "Clean soap. Simple routine.",
        "bullets": [
            "How to read soap labels and spot irritants",
            "Building a simple routine without 10 steps",
            "Tallow balm, infused oils, and salve recipes"
        ]
    },
    {
        "name": "Cast Iron Guide",
        "dir": "cast-iron-guide",
        "tip": "Skip the salt scrub and chain mail. After cooking, hot water and a stiff brush is all you need. Dry it on the stove for 2 minutes and it's done.",
        "tagline": "Season it. Clean it. Keep it forever.",
        "bullets": [
            "Oven seasoning step by step, no flaky layers",
            "Daily care that takes 2 minutes",
            "Thrift store restoration and troubleshooting table"
        ]
    },
    {
        "name": "Chicken Keeping Guide",
        "dir": "chicken-keeping-guide",
        "tip": "The daily chicken routine takes 5 minutes: food, water, eggs, and a quick coop check. Predator-proofing matters more than fancy feeders.",
        "tagline": "Simple setup. Happy birds. Real eggs.",
        "bullets": [
            "Breed guide for cold-hardy, friendly layers",
            "Coop setup with predator protection that works",
            "The 5-minute daily routine and winter care"
        ]
    },
    {
        "name": "Egg Preservation Guide",
        "dir": "egg-preservation-guide",
        "tip": "Water glassing keeps fresh eggs at room temperature for 6-8 months using just pickling lime and water. Only unwashed, clean eggs work — don't wash the bloom off.",
        "tagline": "When the hens outproduce you.",
        "bullets": [
            "Freezing for baking, water glassing for backup, pickling for snacks",
            "Clear brine ratios with no guesswork",
            "How to tell if preserved eggs are still good"
        ]
    },
    {
        "name": "Homekeeping Guide",
        "dir": "homekeeping-guide",
        "tip": "You don't need a different spray bottle for every surface. Five DIY recipes from a seven-ingredient pantry clean an entire house — and they actually work.",
        "tagline": "A clean house, not a cabinet full of products.",
        "bullets": [
            "Seven-ingredient cleaning pantry with real alternatives",
            "Five DIY recipes including glass cleaner and scrub",
            "Daily rhythms, weekly reset, and the twice-a-year deep clean"
        ]
    },
    {
        "name": "Honey Handbook",
        "dir": "honey-handbook",
        "tip": "Honey never spoils. Archaeologists found 3,000-year-old honey in Egyptian tombs — still edible. Store it sealed at room temperature and it lasts forever.",
        "tagline": "The original pantry staple.",
        "bullets": [
            "How bees make honey and why it lasts forever",
            "6 kitchen recipes including Hot Honey and Honey Butter",
            "Varietal guide from clover to manuka, storage and traditional uses"
        ]
    },
    {
        "name": "Kitchen Planner Bundle",
        "dir": "kitchen-planner-bundle",
        "tip": "A grocery list organized by store section — produce, dairy, pantry, frozen — cuts shopping time in half. No more backtracking through aisles.",
        "tagline": "Run your kitchen like it owes you money.",
        "bullets": [
            "Weekly meal planner and grocery list by store section",
            "Pantry and freezer inventory so you stop overbuying",
            "Prep checklist for smooth cooking days"
        ]
    },
    {
        "name": "Preservation Logbook",
        "dir": "preservation-logbook",
        "tip": "The best preservation method is the one you'll actually eat. Track what you made, when it's ready, and what got used — so next year you preserve smarter.",
        "tagline": "Preserve it. Track it. Actually eat it.",
        "bullets": [
            "Canning, fermenting, dehydrating, and freezing logs",
            "Seasonal produce guide so you know what's in season",
            "Year-end review to plan next year's batches"
        ]
    },
    {
        "name": "Recipe Cards",
        "dir": "recipe-cards",
        "tip": "Recipe cards that feel like they belong in a working kitchen. Two cards per page, print as many as you need — no fancy binder required.",
        "tagline": "Recipes that earn their stains.",
        "bullets": [
            "Five themes: Classic, Garden, Baker's, Hearth, Farmhouse",
            "Warm notebook-paper feel, two cards per page",
            "Print and reprint — the file is yours forever"
        ]
    },
    {
        "name": "Seasonal Preservation Calendar",
        "dir": "seasonal-preservation-calendar",
        "tip": "June strawberries don't wait. The calendar tells you what's in season each month and the best way to preserve it — freeze, can, ferment, dehydrate, or root cellar.",
        "tagline": "What's in season, and what to do with it.",
        "bullets": [
            "Month-by-month produce guide with preservation methods",
            "Honest notes on what's worth the effort",
            "Recipes for marmalade and preserved lemons included"
        ]
    },
    {
        "name": "Survival Garden Basics",
        "dir": "survival-garden-basics",
        "tip": "The crops that feed you reliably need no greenhouse, no seed starting, and no daily attention. Beans, potatoes, and winter squash grow themselves — just add dirt, sun, and water.",
        "tagline": "Throw it in the ground. It grows.",
        "bullets": [
            "Crops that grow without a greenhouse or daily care",
            "Simple direct-sow instructions for each crop",
            "Storage guidance so food lasts through winter"
        ]
    }
]

BASE = "/home/chels/test/digital-products"

for p in PRODUCTS:
    d = os.path.join(BASE, p["dir"])
    print(f"\n{p['name']}:")
    
    generate_tip_pin(
        p["name"],
        p["tip"],
        p["tagline"],
        os.path.join(d, "pin-tip.png")
    )
    
    generate_list_pin(
        p["name"],
        p["bullets"],
        os.path.join(d, "pin-list.png")
    )

print(f"\nDone. Generated {len(PRODUCTS) * 2} pin variants.")
