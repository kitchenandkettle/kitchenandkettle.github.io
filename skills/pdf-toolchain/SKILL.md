---
name: pdf-toolchain
description: Use when reading, editing, or generating PDFs.
---

# PDF Toolchain

Rule zero: keep a renderable source (HTML). Edit the source, re-render the PDF. Binary PDF edits are last resort.

## Reading (in order)

1. read_file on the PDF — extracts the text layer, enough for most checks.
2. Poppler binaries for ground truth: `pdfinfo file.pdf | grep -E "Pages|Page size"`, `pdftotext -layout file.pdf - | head`, `pdffonts file.pdf` for embedded fonts.
3. URL PDFs: web_extract first, before any local tool.
4. Scanned or image-only PDFs (no text layer): marker-pdf, which needs ~5GB of models (`uv pip install marker-pdf`). Not installed by default.

## Generating (Playwright, source-first)

- Render HTML to PDF with the project .venv python (system python lacks Playwright): `pg.pdf(path, width, height, print_background=True, prefer_css_page_size=True)` with zero margins.
- Use exact trim sizes (grimoire interior 6x9in; cover = 2x trim + spine + bleed). Confirm the built HTML's `@page` size before rendering.
- Preview HTML via `python3 -m http.server <port>` in the file dir; confirm with curl expecting 200; bypass browser cache with `?v=N` links.

## Editing

- With source: edit the source, rebuild, re-verify. This is how the grimoire books work.
- Without source, text swaps: pymupdf (`uv pip install pymupdf`), redaction plus insert or search-and-replace scripts.
- Without source, structural work (merge, split, rotate): pymupdf or qpdf.
- One-off natural-language text edits: nano-pdf skill (LLM-backed, needs an API key; page numbers may be 0- or 1-based, always verify after).

## Before starting PDF work on a new machine

- Check binaries: `command -v pdfinfo pdftotext qpdf gs`. Check python packages: pymupdf, playwright.
- A struggling agent usually misses libraries, not method. Run this check first.

## Verify after every PDF build

- Page count and size via pdfinfo, fonts embedded via pdffonts.
- For HTML-rendered books: zero clipped content, checked by comparing each page div's scrollHeight against its clientHeight (overflow:hidden hides overflow silently, the PDF alone will not reveal it).
