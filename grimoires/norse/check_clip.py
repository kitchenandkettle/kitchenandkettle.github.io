#!/usr/bin/env python3
"""Check each .page div for clipped overflow (scrollHeight vs clientHeight)."""
import pathlib
from playwright.sync_api import sync_playwright

HERE = pathlib.Path(__file__).resolve().parent
HTML = HERE / "norse-grimoire.html"

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 800, "height": 1200})
    pg.goto(HTML.resolve().as_uri())
    pg.wait_for_timeout(1200)
    result = pg.evaluate(
        """() => {
        const pages = Array.from(document.querySelectorAll('.page'));
        return pages.map((el, i) => ({
            n: i + 1,
            client: el.clientHeight,
            scroll: el.scrollHeight,
            clipped: el.scrollHeight - el.clientHeight,
        }));
    }"""
    )
    bad = [r for r in result if r["clipped"] > 1]
    print("pages checked:", len(result))
    print("clipped pages:", len(bad))
    for r in bad:
        print("CLIP page", r["n"], "over by", r["clipped"], "px")
    b.close()
