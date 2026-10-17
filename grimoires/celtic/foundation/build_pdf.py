import pathlib
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).resolve().parent
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.goto((HERE / "celtic-grimoire-foundation.html").as_uri()); pg.wait_for_timeout(1500)
    pg.pdf(path=str(HERE / "celtic-grimoire-foundation.pdf"), width="6in", height="9in", print_background=True, prefer_css_page_size=True)
    pg.evaluate("1"); b.close()
print("pdf written")
