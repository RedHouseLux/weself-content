"""Combine carousel PNGs into one PDF for LinkedIn document posts.

Usage: python3 tools/pdf.py <carousel dir> <png prefix> <out.pdf>
Example: python3 tools/pdf.py linkedin/leadership weself-li-leadership linkedin/leadership/weself-li-leadership.pdf
Pages keep the PNG size (1080x1350 or 1080x1080) and are written in name order.
"""
import glob
import os
import sys

from PIL import Image

d, prefix, out = sys.argv[1:4]
files = sorted(glob.glob(os.path.join(d, prefix + "-*.png")))
if not files:
    sys.exit("no PNG found for " + prefix)
pages = [Image.open(f).convert("RGB") for f in files]
pages[0].save(out, save_all=True, append_images=pages[1:], resolution=144)
print("ok", len(pages), "pages ->", out)
