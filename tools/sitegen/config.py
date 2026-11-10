"""Site-wide settings shared by every page."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # repository root = the published site
SITE = "https://highmarchgames.com"
EMAIL = "yaniv@highmarchgames.com"
YEAR = 2026

NAV = [("Games", "games/"), ("Press", "press/"), ("About", "about/")]
