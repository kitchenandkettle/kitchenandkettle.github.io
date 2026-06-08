const { chromium } = require('playwright');
const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

// --- CONFIG: must match BASE and FILES from convert_pdfs.js ---
const BASE = '/home/chels/test/digital-products';
const FILES = [
  'seasonal-preservation-calendar/calendar.html',
  'egg-preservation-guide/egg-guide.html',
  'recipe-cards/recipe-cards.html',
  'homekeeping-guide/homekeeping-guide.html',
  'preservation-logbook/preservation-logbook.html',
  'kitchen-systems-bundle/kitchen-systems-bundle.html',
  'chicken-keeping-guide/chicken-keeping-guide.html',
  'cast-iron-guide/cast-iron-guide.html',
  'body-care-guide/body-care-guide.html',
  'survival-garden-basics/survival-garden-basics.html',
  'honey-handbook/honey-handbook.html',
];

// --- Must match EXACTLY the injected CSS in convert_pdfs.js ---
const INJECT_CSS = `
  body { padding: 0 !important; margin: 0 !important; }
  .toolbar { display: none !important; }
  .interactive-only { display: none !important; }
  .page {
    margin-bottom: 0 !important;
    box-shadow: none !important;
    padding-top: 0.6in !important;
    padding-bottom: 0.6in !important;
  }

  .ref-card { padding: 0.45rem !important; }
  .ref-card p { font-size: 8.8pt !important; line-height: 1.45 !important; }
  .ref-grid { gap: 0.5rem 1.5rem !important; margin: 0.8rem 0 !important; }
  .closing { padding: 1.2in 1in 0.6in 1in !important; }
  .closing .notes-block { margin-top: 1rem !important; }
  .closing p { margin-bottom: 0.5rem !important; }

  .ingredient-card { padding: 0.35rem !important; }
  .ingredient-card p { font-size: 8.5pt !important; line-height: 1.35 !important; }
  .ingredient-card .use-for { font-size: 8pt !important; }
  .ingredient-grid { gap: 0.35rem !important; }
  .prose-page .lede { font-size: 11pt !important; margin-bottom: 0.5rem !important; }
  .prose-page hr { margin: 0.4rem 0 !important; }

  .recipe-card { margin-bottom: 0.25rem !important; padding: 0.25rem 0 !important; }
  .recipe-card h3 { font-size: 8pt !important; margin-bottom: 0.1rem !important; }
  .recipe-card .uses { font-size: 8pt !important; margin-bottom: 0.1rem !important; }
  .recipe-card .ingredients { font-size: 8.5pt !important; margin-bottom: 0.15rem !important; }
  .recipe-card .steps { font-size: 8.5pt !important; line-height: 1.3 !important; margin: 0.15rem 0 !important; }
  .recipe-card .steps li { margin-bottom: 0.1rem !important; }

  .breed-card { padding: 0.3rem !important; }
  .breed-card p { font-size: 8.8pt !important; line-height: 1.35 !important; }
  .breed-card .traits { font-size: 8pt !important; margin-bottom: 0.1rem !important; }
  .breed-grid { gap: 0.35rem !important; margin: 0.35rem 0 !important; }

  .step-card { padding: 0.3rem !important; margin-bottom: 0.3rem !important; }
  .step-card .note { font-size: 8.5pt !important; margin-bottom: 0.15rem !important; }
  .step-card .materials { font-size: 8.5pt !important; margin-bottom: 0.15rem !important; }
  .step-card .steps { font-size: 8.8pt !important; }
  .step-card .steps li { margin-bottom: 0.08rem !important; line-height: 1.35 !important; }

  .chicken-guide .prose-page p { font-size: 7.5pt !important; margin-bottom: 0.15rem !important; line-height: 1.3 !important; }
  .chicken-guide .prose-page .lede { font-size: 9pt !important; }
  .chicken-guide .prose-page hr { margin: 0.15rem 0 !important; }
  .chicken-guide .prose-page h3 { font-size: 7.5pt !important; margin-bottom: 0.08rem !important; margin-top: 0.15rem !important; }
  .chicken-guide .prose-page .tip { font-size: 7pt !important; margin: 0.15rem 0 !important; padding-left: 0.35rem !important; }
  .chicken-guide .prose-page h2 { font-size: 13pt !important; margin-bottom: 0.15rem !important; }

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
  .cast-iron-guide .note-block h4 { font-size: 8pt !important; margin-bottom: 0.15rem !important; }
  .cast-iron-guide .note-block textarea { font-size: 8pt !important; min-height: 1.5rem !important; }

  .body-care .page { padding-top: 0.5in !important; padding-bottom: 0.5in !important; }

  .body-care .prose-page p { font-size: 8.5pt !important; margin-bottom: 0.15rem !important; line-height: 1.35 !important; }
  .body-care .prose-page .lede { font-size: 10pt !important; margin-bottom: 0.4rem !important; }
  .body-care .prose-page h2 { font-size: 13pt !important; margin-bottom: 0.2rem !important; }
  .body-care .prose-page h3 { font-size: 8pt !important; margin-bottom: 0.1rem !important; margin-top: 0.2rem !important; }
  .body-care .prose-page hr { margin: 0.3rem 0 !important; }
  .body-care .prose-page .tip { font-size: 7.5pt !important; margin: 0.15rem 0 !important; padding-left: 0.35rem !important; }
  .body-care .prose-page ol, .body-care .prose-page ul { font-size: 8.5pt !important; margin: 0.2rem 0 0.3rem 1rem !important; }
  .body-care .prose-page li { margin-bottom: 0.12rem !important; line-height: 1.35 !important; }
  .body-care .label-table td, .body-care .label-table th { font-size: 7.5pt !important; padding: 0.12rem 0.2rem !important; }
  .body-care .label-table td:first-child { font-size: 7.5pt !important; }
  .body-care .label-table th { font-size: 7pt !important; }
  .body-care .honest-box { padding: 0.3rem !important; }
  .body-care .honest-box h4 { font-size: 7.5pt !important; margin-bottom: 0.1rem !important; }
  .body-care .honest-box p { font-size: 8pt !important; }
  .body-care .ingredient-card { padding: 0.25rem !important; }
  .body-care .ingredient-card h4 { font-size: 10pt !important; }
  .body-care .ingredient-card p { font-size: 8pt !important; line-height: 1.3 !important; }
  .body-care .ingredient-card .role { font-size: 7.5pt !important; }
  .body-care .ingredient-grid { gap: 0.3rem !important; }
  .body-care .do-dont { gap: 0.5rem !important; margin: 0.3rem 0 !important; }
  .body-care .do, .body-care .dont { padding: 0.3rem !important; }
  .body-care .do h4, .body-care .dont h4 { font-size: 7.5pt !important; margin-bottom: 0.15rem !important; }
  .body-care .do li, .body-care .dont li { font-size: 8pt !important; line-height: 1.35 !important; }
  .body-care .ref-card { padding: 0.25rem !important; margin-bottom: 0.2rem !important; }
  .body-care .ref-card h3 { font-size: 10pt !important; margin-bottom: 0.15rem !important; }
  .body-care .ref-card li { font-size: 8.5pt !important; line-height: 1.3 !important; }
  .body-care .notes-grid { gap: 0.3rem !important; margin-top: 0.35rem !important; }
  .body-care .note-block { padding: 0.25rem !important; min-height: 2.5rem !important; }
  .body-care .note-block h4 { font-size: 7.5pt !important; margin-bottom: 0.15rem !important; }
  .body-care .note-block textarea { font-size: 8pt !important; min-height: 1.5rem !important; }

  /* --- Chicken Guide: notes page (+0.6in) --- */
  .chicken-guide .notes-grid { gap: 0.25rem !important; margin-top: 0.25rem !important; }
  .chicken-guide .note-block { padding: 0.2rem !important; min-height: 2.3rem !important; }
  .chicken-guide .note-block h4 { font-size: 12pt !important; margin-bottom: 0.1rem !important; }
  .chicken-guide .note-block textarea { font-size: 12pt !important; min-height: 1.6rem !important; }
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
