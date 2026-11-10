"""sitemap.xml for search engines."""
from .config import SITE


def sitemap_xml(paths):
    """paths: built page paths; the 404 page is left out."""
    urls = [p.replace("index.html", "") for p in paths if p != "404.html"]
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "".join(f"  <url><loc>{SITE}/{u}</loc></url>\n" for u in urls) + "</urlset>\n")
