#!/usr/bin/env python3
"""Render norse-grimoire.html to norse-grimoire-interior.pdf at exact 6x9 trim."""
import pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
HTML = HERE / "norse-grimoire.html"
PDF = HERE / "norse-grimoire-interior.pdf"

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page()
    pg.goto(HTML.resolve().as_uri())
    pg.wait_for_timeout(1500)
    pg.pdf(
        path=str(PDF),
        width="6in",
        height="9in",
        print_background=True,
        prefer_css_page_size=True,
        margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
    )
    print("pdf written:", PDF.name)
    b.close()
