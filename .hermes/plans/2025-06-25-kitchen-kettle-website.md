# Kitchen & Kettle Website — Implementation Plan

> **For Hermes:** Build directly — single-session, all HTML/CSS. No subagents needed.

**Goal:** A quiet, static website for Kitchen & Kettle — home base for the brand beyond Etsy.

**Architecture:** Flat static HTML files with one shared CSS file. No framework, no build step, no JavaScript except what's necessary for basic behavior. Self-contained — open from disk or serve with any static server.

**Tech Stack:** HTML5, CSS3 (custom properties, grid, no preprocessor), zero JavaScript dependencies. Fonts: Crimson Pro + Work Sans via Google Fonts CDN.

**Directory:** `/home/chels/test/site/`

---

## Design System (from brand strategy)

- **Colors:** Paper #F5F0E8 (bg), Ink #2C2416 (text), Clay #C4A882 (accent), Sage #7D8B6F (secondary accent)
- **Typography:** Crimson Pro (headings/body), Work Sans (UI/labels/nav)
- **No:** pure white, pure black, carousels, popups, comment sections, newsletter bait, blog chronology
- **Yes:** warm, calm, reference-shelf feel. Organized by topic, not date.

---

## Pages to Build

### Task 1: Shared stylesheet (`site/css/style.css`)

**Objective:** Single CSS file with the full design system — variables, typography, layout, navigation, article template, responsive breakpoints.

**What it covers:**
- CSS custom properties (colors, fonts, spacing, radii)
- Typography scale (h1-h3, body, caption, nav)
- Layout: max-width content column (680px), centered
- Navigation: top bar, simple links, no hamburger on desktop
- Article template: clean, readable, print-friendly
- Footer: minimal — brand name, tagline, no social icons
- Responsive: stacks at 600px, keeps it simple

### Task 2: Home page (`site/index.html`)

**Objective:** Statement of philosophy, entry points to major sections, seasonal anchor.

**Content (from brand strategy §11):**
- Hero: "A quieter way to run a kitchen." + subhead
- Three-column "This is / This is not / This is for"
- Entry point cards: Recipes, Preservation, Household, Body & Care
- Seasonal anchor section (placeholder for now — "What's in season: summer")
- Footer

### Task 3: About page (`site/about.html`)

**Objective:** Who this is for, what this is not, why it exists. Reader knows within 30 seconds.

**Content (from brand strategy §11):**
- Why Kitchen & Kettle exists
- The philosophy: "Works because it works"
- Who this is for (the Quietly Overwhelmed + the Seekers)
- What this is not (wellness brand, lifestyle aspiration, perfection)
- Footer

### Task 4: Start Here page (`site/start-here.html`)

**Objective:** Guided entry path for someone new. "Start with these five things."

**Content:**
- "If you feel overwhelmed, start here"
- Five low-pressure entry points (e.g. "Get one pan right" → cast iron, "Clean with three things" → vinegar/soap/baking soda, "Cook one thing that keeps" → preserved lemons, "Read one label" → soap ingredients, "Plant one thing" → survival garden basics)
- Each entry point: 2-3 sentences + link to relevant reference article
- Gentle reassurance throughout

### Task 5: Reference article — Cast Iron Care (`site/library/cast-iron.html`)

**Objective:** Free web version of the core cast iron knowledge. Teaches the method. Natural link to Etsy for the printable guide.

**Content:** Adapted from the Cast Iron Care Guide product HTML — the core instructions (seasoning, cleaning, what to cook), but as a web article, not a PDF layout. No "buy the guide" pressure — just a quiet link at the bottom.

### Task 6: Reference article — Simple Cleaning (`site/library/simple-cleaning.html`)

**Objective:** The baking-soda-and-vinegar myth, the three-ingredient cleaning pantry, what actually works. Free web reference.

**Content:** Adapted from the Homekeeping Guide — the philosophy, the core ingredients (vinegar, soap, baking soda), what each does, the myth bust, the basic recipes.

### Task 7: Reference article — Honey Primer (`site/library/honey.html`)

**Objective:** What honey is, types, how to use it, why it crystallizes. Reference material that stands alone.

**Content:** Adapted from the Honey Handbook — how bees make it, varietal guide, storage/crystallization, a couple recipes.

---

## Anti-Slop Checklist (from claude-design skill)

- [ ] No gradients
- [ ] No glassmorphism
- [ ] No emoji
- [ ] No generic SaaS cards with icons
- [ ] No fake metrics or decorative stats
- [ ] No "Insights / Growth / Scale / Optimize" language
- [ ] No stock-photo hero
- [ ] No oversized rounded rectangles as layout crutch

---

## Verification

After all pages built:
1. Open index.html in browser, check no console errors
2. Navigate all links between pages
3. Resize to mobile width, verify readability
4. Print one article page, verify it looks clean
5. Commit everything

---

## Task Order

1. CSS stylesheet → foundation for everything
2. Home page → anchor page, all others link from it
3. About page → linked from home
4. Start Here → linked from home
5. Library pages (3) → linked from Start Here and home
6. Verification pass
