const { chromium } = require('playwright');
const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

// --- CONFIG: must match BASE and FILES from convert_pdfs.js ---
const BASE = '/home/chels/test/digital-products';
const FILES = [
  'seasonal-preservation-calendar/calendar.html',
  'egg-preservation-guide/egg-guide.html',
  'recipe-cards/recipe-cards-static.html',
  'homekeeping-guide/homekeeping-guide-interactive.html',
  'preservation-logbook/preservation-logbook.html',
  'kitchen-planner-bundle/kitchen-planner-bundle.html',
  'chicken-keeping-guide/chicken-keeping-guide.html',
  'cast-iron-guide/cast-iron-guide.html',
  'body-care-guide/body-care-guide.html',
  'survival-garden-basics/survival-garden-basics.html',
  'honey-handbook/honey-handbook.html',
  'beeswax-wraps/beeswax-wraps.html',
  'apothecary-journal/apothecary-journal.html',
  'egg-handling-card/egg-handling-card.html',
  'Moon-Journal/moon-journal-static.html',
  'substitution-cards/substitution-cards.html',
  'recipe-book-dividers/recipe-book-dividers.html',
  'first-aid-checklist/first-aid-checklist.html',
  'apothecary-basics/apothecary-basics.html',
  'root-cellaring-guide/root-cellaring-guide.html',
  'simple-life-guide/simple-life-guide.html',
  'ancestral-living-guide/ancestral-living-guide.html',
  'household-binder/household-binder.html',
];

// --- Must match EXACTLY the injected CSS in convert_pdfs.js ---
const INJECT_CSS = `
        body { padding: 0 !important; margin: 0 !important; }
        .toolbar { display: none !important; }
        .interactive-only { display: none !important; }
        .pdf-only { display: block !important; }
        textarea::placeholder { color: transparent !important; }
        input::placeholder { color: transparent !important; }
        textarea { border: 1px dashed #D9D0C1 !important; }
        .page {
          margin-bottom: 0 !important;
          box-shadow: none !important;
          padding-top: 0.6in !important;
          padding-bottom: 0.6in !important;
          break-after: page !important;
          page-break-after: always !important;
        }

        /* --- Calendar: reference page (+0.6in) & closing page (+0.1in) --- */
        .ref-card { padding: 0.35rem !important; }
        .ref-card p { font-size: 8.5pt !important; line-height: 1.35 !important; }
        .ref-grid { gap: 0.4rem 1.2rem !important; margin: 0.5rem 0 !important; }
        .closing { padding: 1.2in 1in 0.6in 1in !important; align-items: center !important; }
        .closing .notes-block { margin-top: 1rem !important; }
        .closing p { margin-bottom: 0.5rem !important; }
        .month-spread p { font-size: 8pt !important; line-height: 1.35 !important; margin-bottom: 0.2rem !important; }
        .month-spread .action-box { padding: 0.3rem !important; }
        .month-spread .action-box p { font-size: 8pt !important; }
        .month-spread .method-tags { margin-top: 0.25rem !important; }
        .month-spread .honest-box { padding: 0.3rem !important; margin-top: 0.3rem !important; }
        .month-spread .honest-box p { font-size: 7.5pt !important; }
        .month-spread .honest-box h4 { font-size: 8pt !important; }
        .month-spread h3 { font-size: 13pt !important; margin-bottom: 0.2rem !important; }
        .month-spread hr { margin: 0.3rem 0 !important; }

        /* --- Homekeeping Guide: increased compression --- */
        .homekeeping-guide .ingredient-card { padding: 0.2rem !important; }
        .homekeeping-guide .ingredient-card p { line-height: 1.2 !important; margin-bottom: 0.05rem !important; }
        .homekeeping-guide .ingredient-card h4 { margin-bottom: 0.1rem !important; padding-bottom: 0.08rem !important; }
        .homekeeping-guide .ingredient-card .use-for { font-size: 10pt !important; }
        .homekeeping-guide .ingredient-grid { gap: 0.2rem !important; }
        .homekeeping-guide .honest-box { padding: 0.2rem !important; margin: 0.2rem 0 !important; }
        .homekeeping-guide .honest-box h4 { margin-bottom: 0.08rem !important; }
        .homekeeping-guide .honest-box p { margin-bottom: 0.05rem !important; line-height: 1.2 !important; }
        .homekeeping-guide .prose-page .lede { margin-bottom: 0.3rem !important; }
        .homekeeping-guide .prose-page hr { margin: 0.25rem 0 !important; }
        .homekeeping-guide .recipe-card { margin-bottom: 0.2rem !important; padding: 0.2rem 0 !important; }
        .homekeeping-guide .recipe-card h3 { margin-bottom: 0.08rem !important; }
        .homekeeping-guide .recipe-card .uses { margin-bottom: 0.08rem !important; }
        .homekeeping-guide .recipe-card .ingredients { margin-bottom: 0.12rem !important; }
        .homekeeping-guide .recipe-card .steps { line-height: 1.25 !important; margin: 0.12rem 0 !important; }
        .homekeeping-guide .recipe-card .steps li { margin-bottom: 0.08rem !important; }
        .homekeeping-guide .page { padding-top: 0.4in !important; padding-bottom: 0.4in !important; }
        .homekeeping-guide .prose-page p { line-height: 1.3 !important; margin-bottom: 0.12rem !important; }
        .homekeeping-guide .prose-page h2 { margin-bottom: 0.15rem !important; margin-top: 0.15rem !important; }
        .homekeeping-guide .prose-page h3 { margin-bottom: 0.1rem !important; margin-top: 0.15rem !important; }
        .homekeeping-guide .prose-page ul { margin: 0.15rem 0 0.2rem 1rem !important; }
        .homekeeping-guide .prose-page ul li { margin-bottom: 0.05rem !important; line-height: 1.35 !important; }
        .homekeeping-guide .prose-page ol { margin: 0.15rem 0 0.2rem 1rem !important; }
        .homekeeping-guide .routine-table { break-inside: avoid !important; page-break-inside: avoid !important; }
        .homekeeping-guide .prose-page ol li { margin-bottom: 0.05rem !important; line-height: 1.35 !important; }

        /* --- Ancestral Living Guide: prose-heavy reading guide compression --- */
        .ancestral-living .prose-page { display: block !important; }
        .ancestral-living .notes-area { min-height: 2.5rem !important; }
        .ancestral-living .notes-area textarea { min-height: 2rem !important; height: 2rem !important; }
        .ancestral-living .prose-page p { margin-bottom: 0.25rem !important; line-height: 1.3 !important; font-size: 12pt !important; }
        .ancestral-living .prose-page .lede { margin-bottom: 0.3rem !important; font-size: 12pt !important; }
        .ancestral-living .prose-page h2 { font-size: 16pt !important; margin-bottom: 0.15rem !important; padding-bottom: 0.1rem !important; }
        .ancestral-living .prose-page h3 { margin-top: 0.2rem !important; margin-bottom: 0.08rem !important; font-size: 12pt !important; }
        .ancestral-living .prose-page hr { margin: 0.2rem 0 !important; }
        .ancestral-living .honest-box { padding: 0.18rem 0.35rem !important; margin: 0.2rem 0 !important; font-size: 12pt !important; }
        .ancestral-living .tip-box { padding: 0.18rem 0.35rem !important; margin: 0.2rem 0 !important; font-size: 12pt !important; }
        .ancestral-living .page { padding-top: 0.35in !important; padding-bottom: 0.35in !important; }
        .ancestral-living .closing { padding: 0.7in 0.7in !important; }
        .ancestral-living .closing p { margin-bottom: 0.35rem !important; }
        .ancestral-living .cover { padding: 1.2in 0.7in !important; }
        .ancestral-living .page-footer { margin-top: 0.3rem !important; }

        /* --- Chicken Guide: breed page (+0.6in) --- */
        .breed-card { padding: 0.3rem !important; }
        .breed-card p { font-size: 8.8pt !important; line-height: 1.35 !important; }
        .breed-card .traits { font-size: 8pt !important; margin-bottom: 0.1rem !important; }
        .breed-grid { gap: 0.35rem !important; margin: 0.35rem 0 !important; }

        /* --- Chicken Guide: coop setup page (step-card compression) --- */
        .step-card { padding: 0.3rem !important; margin-bottom: 0.3rem !important; }
        .step-card .note { font-size: 8.5pt !important; margin-bottom: 0.15rem !important; }
        .step-card .materials { font-size: 8.5pt !important; margin-bottom: 0.15rem !important; }
        .step-card .steps { font-size: 8.8pt !important; }
        .step-card .steps li { margin-bottom: 0.08rem !important; line-height: 1.35 !important; }

        /* --- Chicken Guide: tighten prose spacing --- */
        .chicken-guide .prose-page p { font-size: 7.5pt !important; margin-bottom: 0.15rem !important; line-height: 1.3 !important; }
        .chicken-guide .prose-page .lede { font-size: 9pt !important; }
        .chicken-guide .prose-page hr { margin: 0.15rem 0 !important; }
        .chicken-guide .prose-page h3 { font-size: 7.5pt !important; margin-bottom: 0.08rem !important; margin-top: 0.15rem !important; }
        .chicken-guide .prose-page .tip { font-size: 7pt !important; margin: 0.15rem 0 !important; padding-left: 0.35rem !important; }
        .chicken-guide .prose-page h2 { font-size: 13pt !important; margin-bottom: 0.15rem !important; }

        /* --- Cast Iron Guide: compress prose, step-cards, tables --- */
        .cast-iron-guide .prose-page p { font-size: 8.5pt !important; margin-bottom: 0.15rem !important; line-height: 1.35 !important; }
        .cast-iron-guide .prose-page .lede { font-size: 10pt !important; margin-bottom: 0.4rem !important; }
        .cast-iron-guide .prose-page h2 { font-size: 13pt !important; margin-bottom: 0.2rem !important; }
        .cast-iron-guide .prose-page h3 { font-size: 8pt !important; margin-bottom: 0.1rem !important; margin-top: 0.2rem !important; }
        .cast-iron-guide .prose-page hr { margin: 0.3rem 0 !important; }
        .cast-iron-guide .prose-page .tip { font-size: 7.5pt !important; margin: 0.15rem 0 !important; padding-left: 0.35rem !important; }
        .cast-iron-guide .step-card { padding: 0.3rem !important; margin-bottom: 0.3rem !important; }
        .cast-iron-guide .step-card h3 { font-size: 10pt !important; }
        .cast-iron-guide .step-card p, .cast-iron-guide .step-card li { font-size: 8.5pt !important; line-height: 1.35 !important; }
        .cast-iron-guide .step-card .materials { font-size: 8pt !important; margin-bottom: 0.15rem !important; }
        .cast-iron-guide .ref-card { padding: 0.3rem !important; }
        .cast-iron-guide .ref-card h3 { font-size: 10pt !important; }
        .cast-iron-guide .ref-card p, .cast-iron-guide .ref-card li { font-size: 8.5pt !important; line-height: 1.35 !important; }
        .cast-iron-guide .trouble-table td, .cast-iron-guide .trouble-table th { font-size: 8pt !important; padding: 0.15rem 0.25rem !important; }
        .cast-iron-guide .trouble-table td:first-child { font-size: 7.5pt !important; }
        .cast-iron-guide .notes-grid { gap: 0.35rem !important; margin-top: 0.35rem !important; }
        .cast-iron-guide .note-block { padding: 0.3rem !important; min-height: 2.5rem !important; }
        .cast-iron-guide .note-block h4 { font-size: 8pt !important; margin-bottom: 0.1rem !important; }

        /* --- Egg Guide: 12pt font bump compression --- */
        .egg-guide .page { padding-top: 0.35in !important; padding-bottom: 0.35in !important; }
        .egg-guide .method-card { padding: 0.35rem !important; }
        .egg-guide .method-card p { line-height: 1.3 !important; margin-bottom: 0.15rem !important; }
        .egg-guide .method-grid { gap: 0.35rem 1rem !important; margin: 0.4rem 0 !important; }
        .egg-guide .steps { margin: 0.3rem 0 !important; padding-left: 1rem !important; }
        .egg-guide .steps li { margin-bottom: 0.08rem !important; line-height: 1.3 !important; }
        .egg-guide .ratio-box { padding: 0.35rem 0.5rem !important; margin: 0.4rem 0 !important; }
        .egg-guide .caution-box { padding: 0.35rem 0.5rem !important; margin: 0.4rem 0 !important; }
        .egg-guide .honest-box { padding: 0.35rem !important; margin: 0.4rem 0 !important; }
        .egg-guide .honest-box p { line-height: 1.3 !important; }
        .egg-guide .system-table { margin: 0.5rem 0 !important; }
        .egg-guide .system-table td { padding: 0.2rem 0.35rem !important; line-height: 1.3 !important; }
        .egg-guide .system-table th { padding: 0.2rem 0.35rem !important; }
        .egg-guide .variation-grid { gap: 0.35rem !important; margin: 0.3rem 0 0.5rem !important; }
        .egg-guide .var-card { padding: 0.3rem 0.4rem !important; }
        .egg-guide h2 { margin-bottom: 0.25rem !important; }
        .egg-guide p { margin-bottom: 0.35rem !important; line-height: 1.4 !important; }
        .egg-guide h3 { margin-bottom: 0.2rem !important; margin-top: 0.4rem !important; }
        .egg-guide .notes-block { margin-top: 1rem !important; min-height: 2in !important; }

        /* --- Chicken Guide: notes page (+0.6in) --- */
        .chicken-guide .notes-grid { gap: 0.25rem !important; margin-top: 0.25rem !important; }
        .chicken-guide .note-block { padding: 0.2rem !important; min-height: 2.3rem !important; }
        .chicken-guide .note-block h4 { font-size: 12pt !important; margin-bottom: 0.1rem !important; }
        .chicken-guide .note-block textarea { font-size: 12pt !important; min-height: 1.6rem !important; }
        .chicken-guide .prose-page hr { margin: 0.3rem 0 !important; }
        .chicken-guide .prose-page h3 { margin-top: 0.2rem !important; margin-bottom: 0.15rem !important; }
        .chicken-guide .page { padding-top: 0.55in !important; padding-bottom: 0.55in !important; }

        /* --- Apothecary Basics: teas page (+0.8in) & poultices page (+1.3in) --- */
        .apothecary-basics .method-card { padding: 0.22rem 0.35rem !important; margin-bottom: 0.18rem !important; }
        .apothecary-basics .method-card p { margin-bottom: 0.1rem !important; line-height: 1.3 !important; }
        .apothecary-basics .method-card .label { margin-bottom: 0.04rem !important; }
        .apothecary-basics .prose-page p { margin-bottom: 0.25rem !important; line-height: 1.35 !important; }
        .apothecary-basics .prose-page h3 { margin-top: 0.3rem !important; margin-bottom: 0.15rem !important; }
        .apothecary-basics .prose-page h2 { margin-bottom: 0.2rem !important; }
        .apothecary-basics .section-header h2 { margin-top: 0.3rem !important; }
        .apothecary-basics .honest-box { padding: 0.2rem 0.35rem !important; margin: 0.2rem 0 !important; }
        .apothecary-basics .tip-box { padding: 0.2rem 0.35rem !important; margin: 0.2rem 0 !important; }
        .apothecary-basics .lede { margin-bottom: 0.35rem !important; }
        .apothecary-basics .page { padding-top: 0.5in !important; padding-bottom: 0.5in !important; }

        /* --- Root Cellaring Guide: crop grid (+0.3in) & troubleshooting (+0.1in) --- */
        .root-cellaring .crop-card { padding: 0.22rem !important; }
        .root-cellaring .crop-card p { margin-bottom: 0.05rem !important; line-height: 1.3 !important; }
        .root-cellaring .crop-card .specs { font-size: 7.5pt !important; }
        .root-cellaring .crop-grid { gap: 0.18rem !important; margin: 0.2rem 0 !important; }
        .root-cellaring .alt-card { padding: 0.22rem !important; }
        .root-cellaring .alt-card p { margin-bottom: 0.05rem !important; line-height: 1.3 !important; }
        .root-cellaring .alt-card .rating { font-size: 7.5pt !important; }
        .root-cellaring .alt-grid { gap: 0.18rem !important; margin: 0.2rem 0 !important; }
        .root-cellaring .ref-table td { padding: 0.1rem 0.2rem !important; line-height: 1.25 !important; }
        .root-cellaring .ref-table th { padding: 0.1rem 0.2rem !important; }
        .root-cellaring .method-card { padding: 0.22rem 0.3rem !important; margin-bottom: 0.18rem !important; }
        .root-cellaring .method-card p { margin-bottom: 0.05rem !important; line-height: 1.3 !important; }
        .root-cellaring .method-card .label { margin-bottom: 0.04rem !important; }
        .root-cellaring .prose-page p { margin-bottom: 0.2rem !important; line-height: 1.35 !important; }
        .root-cellaring .prose-page h3 { margin-top: 0.25rem !important; margin-bottom: 0.12rem !important; }
        .root-cellaring .prose-page .lede { margin-bottom: 0.3rem !important; }
        .root-cellaring .prose-page hr { margin: 0.2rem 0 !important; }
        .root-cellaring .honest-box { padding: 0.2rem 0.3rem !important; margin: 0.2rem 0 !important; }
        .root-cellaring .tip-box { padding: 0.2rem 0.3rem !important; margin: 0.2rem 0 !important; }
        .root-cellaring .page { padding-top: 0.5in !important; padding-bottom: 0.5in !important; }
      `;
// ----------------------------------------------------------------

(async () => {
  const browser = await chromium.launch({ headless: true });

  for (const rel of FILES) {
    const htmlPath = path.join(BASE, rel);
    const pdfRel = rel.replace('.html', '.pdf');
    if (!fs.existsSync(htmlPath)) continue;

    const page = await browser.newPage();
    await page.emulateMedia({ media: 'screen' });
    await page.goto(`file://${htmlPath}`, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(500);
    await page.addStyleTag({ content: INJECT_CSS });

    const info = await page.evaluate(() => {
      const pageDivs = document.querySelectorAll('.page:not(.page-footer)');
      const pages = Array.from(pageDivs).map((p, i) => {
        const h2 = p.querySelector('h2');
        let title = 'untitled';
        if (p.classList.contains('cover')) title = 'COVER';
        else if (p.classList.contains('closing')) title = 'CLOSING';
        else if (h2) title = h2.textContent.trim().substring(0, 45);
        else title = p.className.replace('page', '').trim().substring(0, 25);

        const heightIn = p.scrollHeight / 96;
        return { n: i + 1, title, height: heightIn.toFixed(1), overflows: heightIn > 11.05 };
      });
      const overflowers = pages.filter(p => p.overflows);
      return { total: pages.length, pages, overflowers };
    });

    let pdfPages = '?';
    try {
      const out = execSync(`pdfinfo "${path.join(BASE, pdfRel)}" 2>/dev/null | grep Pages`, { encoding: 'utf8' });
      pdfPages = out.match(/\d+/)[0];
    } catch(e) {}

    console.log(`\n${rel}`);
    console.log(`  .page divs: ${info.total}  |  PDF pages: ${pdfPages}`);
    if (info.overflowers.length === 0) {
      console.log(`  ✓ All pages ≤ 11in — no blanks`);
    } else {
      console.log(`  ✗ ${info.overflowers.length} overflow:`);
      info.overflowers.forEach(p => console.log(`     #${p.n} "${p.title}" — ${p.height}in`));
    }
    await page.close();
  }
  await browser.close();
})();