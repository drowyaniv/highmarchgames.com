"""Builds the static pages of highmarchgames.com: python tools/build.py

Writes plain .html files (and sitemap.xml) into the repository root, where GitHub Pages serves them as they are.
Page texts live in tools/sitegen/pages/; see Docs/ARCHITECTURE.md.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sitegen.build import build_site  # noqa: E402
from sitegen.config import ROOT  # noqa: E402

if __name__ == "__main__":
    print("built:", ", ".join(build_site(ROOT)))
