# PDF Pipeline Guide

How the HTML guides become PDFs, and how to keep them in sync.

## Architecture

```
HTML file  ──→  Playwright/Chromium (screen mode)  ──→  PDF
                    │
                    └── Injected stylesheet (convert_pdfs.js lines 44-187)
                         with !important overrides
```

The PDF is **not** generated from `@media print` CSS. The converter
(`scripts/convert_pdfs.js`) does this:

1. Opens the HTML in headless Chromium via Playwright
2. Calls `page.emulateMedia({ media: 'screen' })` — **screen mode, not print**
3. Injects its own `<style>` tag loaded with `!important` CSS overrides
4. Calls `page.pdf({ printBackground: true, preferCSSPageSize: true })`

Because of step 2: `@media print {}` rules in your HTML are **dead code for
the PDF**. They only affect the browser's own Ctrl+P dialog. The converter's
injected stylesheet is the sole source of PDF-specific CSS.

Because of step 3: **any `!important` rule in the converter will silently
override inline styles on your HTML elements.** If something looks right in
the browser but wrong in the PDF, the converter is the culprit.

## Critical Trap: Converter Overrides Win

The converter's injected stylesheet uses `!important` on everything. If a
per-guide rule targets an element you styled inline, **the converter wins**.

**Example**: The body-care guide had textareas with `min-height: 3.7in` inline,
but the converter had:

```css
.body-care .note-block textarea { min-height: 1.5rem !important; }
```

Result: fields looked 3.7 inches in the browser, ~0.2 inches in the PDF.
Fix: removed the conflicting converter rules.

## Global Overrides (Apply to All Guides)

```css
body          { padding: 0 !important; margin: 0 !important; }
.toolbar      { display: none !important; }
.interactive-only { display: none !important; }
textarea::placeholder { color: transparent !important; }
input::placeholder   { color: transparent !important; }
textarea      { border: 1px dashed #D9D0C1 !important; }
.page {
  margin-bottom: 0 !important;
  box-shadow: none !important;
  padding-top: 0.6in !important;
  padding-bottom: 0.6in !important;
  break-after: page !important;
  page-break-after: always !important;
}
```

Implications:
- All textareas get a dashed border on the PDF. Match it in HTML with
  `border: 1px dashed var(--line)`.
- All placeholders are hidden on the PDF. Add clay-colored placeholders
  in HTML for the browser experience; they vanish automatically.
- Every `.page` div becomes exactly one PDF page (unless content overflows).

## Workflow

```
1. Edit HTML         → patch the .html file
2. Check converter   → read scripts/convert_pdfs.js
                        verify no per-guide !important rule targets
                        the elements you just changed
3. Rebuild PDF       → node scripts/convert_pdfs.js <guide-name>
4. Check heights     → node scripts/check_all_heights.js <guide-name>
                        .page divs must equal PDF pages
                        all pages ≤ 11in, no blanks
5. Git commit        → commit after every successful cycle
```

## Text Fields for Handwriting

When the PDF is meant to be printed and hand-written in:

```html
<textarea placeholder="Hint text…"
  style="width:100%; min-height:3.7in; resize:vertical;
  font-size:12pt; font-family:'Crimson Pro',Georgia,serif;
  line-height:1.5;
  border:1px dashed var(--line);    /* matches converter's global rule */
  outline:none;
  background:var(--light);          /* subtle paper tint for visibility */
  padding:0.3rem"></textarea>
```

Also add to the `<style>` block:
```css
input::placeholder, textarea::placeholder { color: var(--clay); opacity: 1; }
```

The converter hides placeholders automatically — no `@media print` rule needed.

## Standard Notes Page (2×2 Grid)

```html
<div class="page prose-page">
  <div class="section-header">
    <h2>My Notes</h2>
  </div>
  <div class="notes-grid" style="margin-top:0.3rem; gap:0.3rem;">
    <div class="note-block" style="min-height:4.3in;">
      <h4>Field Title</h4>
      <textarea data-key="notes-..." placeholder="Hint…"
        style="...as above..."></textarea>
    </div>
    <!-- repeat for 4 total blocks in 2×2 grid -->
  </div>
</div>
```

`.notes-grid` uses `grid-template-columns: 1fr 1fr` — two columns
automatically. Four blocks = 2×2. Two blocks = single row, half-width each.

## Per-Guide Override Sections

The converter has targeted overrides for each guide (e.g., `.body-care`,
`.chicken-guide`, `.cast-iron-guide`). These compress spacing, reduce padding,
and sometimes constrain element sizes to keep pages under 11 inches.

When adding new elements or changing layouts, you may need to:
- Remove converter overrides that fight your new styles
- Add new converter overrides if your content overflows 11 inches

Never reduce fonts below 12pt. Never use `overflow: hidden` to fix overflow.

## Files

| File | Purpose |
|------|---------|
| `digital-products/<guide>/<guide>.html` | Source HTML |
| `digital-products/<guide>/<guide>.pdf`  | Generated PDF |
| `digital-products/scripts/convert_pdfs.js` | PDF converter + overrides |
| `digital-products/scripts/check_all_heights.js` | Page height validator |
| `shop-info/brand-style-guide/style-guide.html` | Brand colors, fonts, rules |

## Common Failures

| Symptom | Cause | Fix |
|---------|-------|-----|
| Field tiny in PDF, fine in browser | Converter !important overrides inline size | Remove the converter override |
| PDF page count ≠ .page div count | Content overflows to extra pages | Check heights, trim content or split pages |
| Placeholder text showing on PDF | Missing converter placeholder rule | Should be auto-hidden; check convert_pdfs.js |
| Background colors missing in PDF | (Should not happen — printBackground:true is set) | Check if converter strips the element's bg |
