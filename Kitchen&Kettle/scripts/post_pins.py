#!/usr/bin/env python3
"""Post Kitchen & Kettle pins to Pinterest via the v5 API.

Uses only stdlib. Reads pins from pins.json, posts using urllib.
Tracks posted pins in pins_state.json to avoid duplicates.

Requires a Pinterest access token in .pinterest_token file.
Get one at: https://developers.pinterest.com/apps/

Usage:
  python3 post_pins.py           # Post next unposted pin
  python3 post_pins.py --dry-run # Show what would be posted
  python3 post_pins.py --count 3 # Post up to 3 pins
  python3 post_pins.py --list    # Show all pins and their status
"""

import json
import os
import sys
import base64
import urllib.request
import urllib.error

API_URL = "https://api.pinterest.com/v5/pins"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PRODUCTS_DIR = "/home/chels/test/digital-products"
PINS_FILE = os.path.join(SCRIPT_DIR, "pins.json")
STATE_FILE = os.path.join(SCRIPT_DIR, "pins_state.json")
TOKEN_FILE = os.path.join(SCRIPT_DIR, ".pinterest_token")


def load_token():
    """Read access token from file."""
    if not os.path.isfile(TOKEN_FILE):
        print("ERROR: No token file found at", TOKEN_FILE)
        print()
        print("To get a token:")
        print("1. Go to https://developers.pinterest.com/apps/")
        print("2. Create an app (or use existing)")
        print("3. Under 'OAuth', generate an access token with scopes:")
        print("   pins:read, pins:write, boards:read")
        print("4. Paste the token into:", TOKEN_FILE)
        print()
        print("Token must be the only content in that file.")
        sys.exit(1)
    with open(TOKEN_FILE) as f:
        return f.read().strip()


def load_pins():
    """Load all pin data from pins.json."""
    with open(PINS_FILE) as f:
        return json.load(f)


def load_state():
    """Load posting state. Returns dict of {pin_key: True/False}."""
    if os.path.isfile(STATE_FILE):
        with open(STATE_FILE) as f:
            return json.load(f)
    return {}


def save_state(state):
    """Save posting state."""
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


def get_pin_images(product_dir, pin_variant=1):
    """Get pin image path for a product. Falls back to any pin image."""
    img_path = os.path.join(PRODUCTS_DIR, product_dir, f"pin-{pin_variant}.png")
    if os.path.isfile(img_path):
        return img_path
    # Fallback: find any pin image
    d = os.path.join(PRODUCTS_DIR, product_dir)
    if os.path.isdir(d):
        for f in sorted(os.listdir(d)):
            if f.startswith("pin") and f.endswith(".png"):
                return os.path.join(d, f)
    return None


def image_to_base64(path):
    """Read image file and return base64 string."""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")


def post_pin(token, title, description, link, image_path, board_id=None):
    """Post a pin to Pinterest using base64 image upload.
    
    Returns (success, response_data) tuple.
    """
    img_b64 = image_to_base64(image_path)
    
    body = {
        "title": title,
        "description": description,
        "link": link,
        "media_source": {
            "source_type": "image_base64",
            "content_type": "image/png",
            "data": img_b64
        }
    }
    
    if board_id:
        body["board_id"] = board_id
    
    data = json.dumps(body).encode("utf-8")
    
    req = urllib.request.Request(
        API_URL,
        data=data,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            result = json.loads(resp.read())
            return True, result
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace")
        try:
            error_json = json.loads(error_body)
            return False, error_json
        except json.JSONDecodeError:
            return False, {"message": error_body}
    except Exception as e:
        return False, {"message": str(e)}


def list_boards(token):
    """List user's boards (for finding board IDs)."""
    url = "https://api.pinterest.com/v5/boards?page_size=50"
    req = urllib.request.Request(
        url,
        headers={"Authorization": f"Bearer {token}"}
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
            boards = data.get("items", [])
            for b in boards:
                print(f"  {b['name']:30s}  id: {b['id']}")
            return boards
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace")
        print(f"Error listing boards: {error_body}")
        return []


def main():
    dry_run = "--dry-run" in sys.argv
    list_mode = "--list" in sys.argv
    list_boards_mode = "--boards" in sys.argv
    
    # How many pins to post
    count = 1
    for i, arg in enumerate(sys.argv):
        if arg == "--count" and i + 1 < len(sys.argv):
            count = int(sys.argv[i + 1])
    
    pins = load_pins()
    state = load_state()
    
    # Modes that don't need a token
    if list_mode:
        print(f"{'#':3} {'Status':8} {'Product':30} Pin")
        print("-" * 80)
        for i, pin in enumerate(pins):
            key = f"{pin['dir']}-1"
            status = "POSTED" if state.get(key) else "READY"
            print(f"{i:3} {status:8} {pin['product']:30} pin-1.png")
        print()
        posted = sum(1 for v in state.values() if v)
        print(f"Posted: {posted}/{len(pins)}  Remaining: {len(pins) - posted}")
        return
    
    if dry_run:
        print("DRY RUN — no pins will actually be posted.\n")
        for i, pin in enumerate(pins):
            if i >= count:
                break
            key = f"{pin['dir']}-1"
            img_path = get_pin_images(pin["dir"], 1)
            print(f"{i+1}. {pin['product']}")
            print(f"   Image: {img_path}")
            print(f"   Link:  {pin['link']}")
            print(f"   Board: {pin['board']}")
            print()
        print(f"Would post {min(count, len(pins))} pin(s).")
        return
    
    token = load_token()
    
    if list_boards_mode:
        print("Your Pinterest boards:")
        list_boards(token)
        return
    
    posted_count = 0
    for pin in pins:
        if posted_count >= count:
            break
        
        key = f"{pin['dir']}-1"
        if state.get(key):
            continue
        
        img_path = get_pin_images(pin["dir"], 1)
        if not img_path:
            print(f"SKIP {pin['product']}: no pin image found")
            continue
        
        print(f"\nPosting: {pin['product']}")
        print(f"  Image: {img_path}")
        
        success, result = post_pin(
            token,
            pin["title"],
            pin["description"],
            pin["link"],
            img_path
        )
        
        if success:
            pin_id = result.get("id", "unknown")
            print(f"  OK - Pin ID: {pin_id}")
            state[key] = True
            posted_count += 1
        else:
            error_msg = result.get("message", str(result))
            print(f"  FAIL - {error_msg}")
    
    save_state(state)
    total_posted = sum(1 for v in state.values() if v)
    total = len(pins)
    print(f"\nSession: {posted_count} pin(s) posted.")
    print(f"Overall: {total_posted}/{total} pins posted ({total - total_posted} remaining).")


if __name__ == "__main__":
    main()
