#!/usr/bin/env python3
"""Composite household binder primary image."""
import sys, os
sys.path.insert(0, '/home/chels/test/digital-products')
# Reuse the composite_etsy_mockup.py template directly via import
import importlib.util
spec = importlib.util.spec_from_file_location("composite", "/home/chels/.hermes/skills/creative/digital-product-design/scripts/composite_etsy_mockup.py")
composite = importlib.util.module_from_spec(spec)
spec.loader.exec_module(composite)

title = "Household Binder"
tagline = "Works because it works."
features = [
    "Six tabbed sections \u2014 cleaning, maintenance,",
    "finances, food & family",
    "Pre-filled checklists \u2014 no starting from scratch",
    "Everything saves automatically as you type",
    "Save a backup file \u2014 your data stays safe",
]
brand = "Kitchen & Kettle"

photo = "/home/chels/test/digital-products/household-binder/katja-rooke-qjgZqBzg5H8-unsplash.jpg"
out = "/home/chels/test/digital-products/household-binder/primary-product-image-2.png"

kb = composite.build(photo, out, [title], tagline, features, brand)
print(f"Done: {out} ({kb} bytes)")
