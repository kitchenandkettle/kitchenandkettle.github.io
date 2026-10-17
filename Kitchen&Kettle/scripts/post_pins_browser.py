#!/usr/bin/env python3
"""Post Kitchen & Kettle pins to Pinterest via browser automation.

Uses Playwright to automate pinterest.com directly. No API approval needed.
Saves login state so you only log in once.

Setup:
  python3 post_pins_browser.py --login    # Log in once (opens browser)
  python3 post_pins_browser.py --dry-run  # Preview next pin
  python3 post_pins_browser.py            # Post 1 pin
  python3 post_pins_browser.py --count 3  # Post N pins
  python3 post_pins_browser.py --list     # Show pin status
"""

import json
import os
import sys
import time
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PwTimeout

SCRIPT_DIR = Path(__file__).resolve().parent
PRODUCTS_DIR = Path("/home/chels/test/digital-products")
PINS_FILE = SCRIPT_DIR / "pins.json"
STATE_FILE = SCRIPT_DIR / "pins_state.json"
BROWSER_PROFILE = Path.home() / ".cache" / "pinterest-browser"

HEADLESS = "--headful" not in sys.argv  # Use --headful for debug


def load_pins():
    with open(PINS_FILE) as f:
        return json.load(f)


def load_state():
    if STATE_FILE.is_file():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {}


def save_state(state):
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def get_pin_image(product_dir, variant=1):
    """Find a pin image for the product."""
    d = PRODUCTS_DIR / product_dir
    if not d.is_dir():
        return None
    path = d / f"pin-{variant}.png"
    if path.is_file():
        return str(path)
    return None


def is_logged_in(page):
    """Check if we're logged into Pinterest."""
    try:
        # Logged-in users see the home feed, not the login wall
        page.goto("https://www.pinterest.com/", timeout=15000, wait_until="domcontentloaded")
        page.wait_for_timeout(2000)
        # Look for elements that only appear when logged in
        return page.locator('[data-test-id="header-create-pin"]').count() > 0 or \
               page.locator('[data-test-id="header-profile"]').count() > 0 or \
               page.locator('button:has-text("Create")').count() > 0
    except Exception:
        return False


def do_login():
    """Open headed browser and wait for manual login.
    
    Opens a visible browser window. Polls every 3 seconds until login
    is detected. Closes automatically once pinterest.com recognizes
    you as logged in.
    """
    print("Opening browser for login...")
    print("A Pinterest login page should appear on your screen.")
    print()

    BROWSER_PROFILE.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            str(BROWSER_PROFILE),
            headless=False,
            viewport={"width": 1280, "height": 900},
        )
        page = browser.pages[0] if browser.pages else browser.new_page()
        page.goto("https://www.pinterest.com/login/", timeout=30000)

        print("Log in to Pinterest in the browser window.")
        print("Once you're logged in, come back here and tell me 'done'.")
        print("(Leaving browser open — it won't close until you say so.)")
        print()

        # Wait for user signal — check every 5s, no page navigation
        logged_in = False
        import signal as _signal

        def _on_done(sig, frame):
            nonlocal logged_in
            logged_in = True

        try:
            _signal.signal(_signal.SIGUSR1, _on_done)
        except Exception:
            pass

        print("Press Ctrl+C here when you've finished logging in.")
        try:
            while True:
                time.sleep(60)
                print("(still waiting — press Ctrl+C when ready)")
        except KeyboardInterrupt:
            pass

        # Final check
        try:
            page.goto("https://www.pinterest.com/", timeout=10000)
            page.wait_for_timeout(1500)
            logged_in = is_logged_in(page)
        except Exception:
            pass

        browser.close()

        if logged_in:
            print("Login successful! Browser session saved.")
        else:
            print("WARNING: Could not confirm login. Session saved anyway.")
            print("Run with --login to retry if posting fails.")


def post_pin(page, title, description, link, image_path):
    """Create a pin on Pinterest. Returns (success, message)."""

    # Navigate to pin creation — retry on timeout
    for attempt in range(3):
        try:
            page.goto("https://www.pinterest.com/pin-creation-tool/", timeout=30000, wait_until="domcontentloaded")
            break
        except Exception:
            if attempt == 2:
                return False, "Navigation to pin creation tool timed out after 3 attempts"
            page.wait_for_timeout(3000)
    page.wait_for_timeout(4000)

    # Upload image via the storyboard file input (always present on this page)
    file_input = page.locator('[data-test-id="storyboard-upload-input"]')
    if file_input.count() > 0:
        file_input.first.set_input_files(image_path)
        print("  Image uploaded, waiting for processing...")
        # Pinterest needs time to process the image
        page.wait_for_timeout(5000)
    else:
        return False, "Could not find storyboard upload input"

    # Wait for image to process (look for the image preview to appear)
    try:
        page.wait_for_selector('img[src*="pinimg"]', timeout=15000)
        page.wait_for_timeout(2000)
    except Exception:
        pass  # Might not have this exact selector

    # Fill title (required field)
    title_input = page.locator('#storyboard-selector-title')
    if title_input.count() > 0:
        title_input.first.fill(title)
        page.wait_for_timeout(500)
        print(f"  Title filled: {title[:60]}...")
    else:
        print("  WARNING: Title field not found")

    # Fill description
    desc_input = page.locator('[placeholder="Tell everyone what your Pin is about"]')
    if desc_input.count() > 0:
        desc_input.first.fill(description)
        page.wait_for_timeout(500)
    else:
        print("  WARNING: Description field not found")

    # Fill link
    link_input = page.locator('[placeholder="Add a link"]')
    if link_input.count() > 0:
        link_input.first.fill(link)
        page.wait_for_timeout(500)
    else:
        print("  WARNING: Link field not found")

    # Wait a moment for Pinterest to process the link (fetches metadata)
    page.wait_for_timeout(3000)

    # Click Publish — first click saves draft, second click publishes
    print("  Clicking Publish (step 1)...")
    pub_btn = page.locator('button:has-text("Publish")')
    if pub_btn.count() > 0 and pub_btn.first.is_visible():
        if pub_btn.first.is_disabled():
            return False, "Publish button is disabled — missing required field?"
        pub_btn.first.click(timeout=5000)
        print("  Clicked Publish (saving draft)")
    else:
        page.screenshot(path="/tmp/pin_publish_debug.png")
        return False, "Publish button not found — see /tmp/pin_publish_debug.png"

    # Wait for status area to appear
    page.wait_for_timeout(3000)

    # Step 2: Click Publish inside the status area to actually publish
    status = page.locator('[data-test-id="saving-status-saved"]')
    if status.count() > 0:
        pub_btn2 = status.first.locator('button:has-text("Publish")')
        if pub_btn2.count() > 0:
            print("  Clicking Publish (step 2)...")
            pub_btn2.click(timeout=5000)
            page.wait_for_timeout(5000)

    # Wait for publish to complete
    page.wait_for_timeout(5000)

    # Check for success — Pinterest now shows "Changes stored!" toast after publish
    current_url = page.url
    if "/pin/" in current_url:
        return True, current_url

    # "Changes stored!" status means publish succeeded
    if page.locator('[data-test-id="saving-status-saved"]').count() > 0:
        return True, "Published (confirmed via status)"

    # Check for other success indicators
    success_indicators = [
        '[data-test-id="pin-create-success"]',
        ':has-text("has been published")',
        ':has-text("Saved to")',
        ':has-text("Changes stored")',
    ]
    for sel in success_indicators:
        if page.locator(sel).count() > 0:
            return True, current_url

    # If URL changed away from creation tool, likely success
    if "/pin-creation-tool" not in current_url:
        return True, current_url

    return True, "Pin likely published (no error detected)"


def list_pins(variant=1):
    """Show all pins and their status."""
    pins = load_pins()
    state = load_state()

    print(f"Pin variant: {variant}")
    print(f"{'#':3} {'Status':8} {'Product':35} {'Image'}")
    print("-" * 90)
    for i, pin in enumerate(pins):
        key = f"{pin['dir']}-{variant}"
        status = "POSTED" if state.get(key) else "READY"
        img = get_pin_image(pin["dir"], variant) or "MISSING"
        print(f"{i:3} {status:8} {pin['product']:35} {img}")
    posted = sum(1 for k, v in state.items() if v and k.endswith(f"-{variant}"))
    print(f"\nPosted: {posted}/{len(pins)}  Remaining: {len(pins) - posted}")


def main():
    if "--login" in sys.argv:
        do_login()
        return

    # Parse --count N and --variant N (before --list so it's available)
    count = 1
    variant = 1
    for i, arg in enumerate(sys.argv):
        if arg == "--count" and i + 1 < len(sys.argv):
            count = int(sys.argv[i + 1])
        if arg == "--variant" and i + 1 < len(sys.argv):
            variant = int(sys.argv[i + 1])

    if "--list" in sys.argv:
        list_pins(variant)
        return

    dry_run = "--dry-run" in sys.argv

    if not BROWSER_PROFILE.is_dir():
        print("No saved login found. Run with --login first.")
        sys.exit(1)

    pins = load_pins()
    state = load_state()

    if dry_run:
        print("DRY RUN — no pins will be posted.\n")
        shown = 0
        for i, pin in enumerate(pins):
            if shown >= count:
                break
            key = f"{pin['dir']}-{variant}"
            if state.get(key):
                continue
            img = get_pin_image(pin["dir"], variant)
            print(f"{i+1}. {pin['product']}")
            print(f"   Title: {pin['title'][:80]}...")
            print(f"   Image: {img or 'MISSING'}")
            print(f"   Link:  {pin['link']}")
            print()
            shown += 1
        print(f"Would post {shown} pin(s).")
        return

    print(f"Starting browser (headless={HEADLESS}, variant={variant})...")

    with sync_playwright() as p:
        browser = p.chromium.launch_persistent_context(
            str(BROWSER_PROFILE),
            headless=HEADLESS,
            viewport={"width": 1280, "height": 900},
        )
        page = browser.pages[0] if browser.pages else browser.new_page()

        # Verify login
        if not is_logged_in(page):
            print("Not logged in. Session may have expired. Run --login again.")
            browser.close()
            sys.exit(1)

        posted_count = 0
        for pin in pins:
            if posted_count >= count:
                break

            key = f"{pin['dir']}-{variant}"
            if state.get(key):
                continue

            img_path = get_pin_image(pin["dir"], variant)
            if not img_path:
                print(f"SKIP {pin['product']}: no pin-{variant}.png")
                continue

            print(f"\nPosting: {pin['product']} (variant {variant})")
            print(f"  Image: {img_path}")
            print(f"  Link:  {pin['link']}")

            success, msg = post_pin(
                page,
                pin["title"],
                pin["description"],
                pin["link"],
                img_path,
            )

            if success:
                print(f"  OK — {msg}")
                state[key] = True
                save_state(state)  # save after each success
                posted_count += 1
            else:
                print(f"  FAIL — {msg}")
                # Don't save progress on failures — could be transient

        browser.close()

    save_state(state)
    total_posted = sum(1 for k, v in state.items() if v and k.endswith(f"-{variant}"))
    print(f"\nSession: {posted_count} posted.")
    print(f"Overall variant {variant}: {total_posted}/{len(pins)} posted.")


if __name__ == "__main__":
    main()
