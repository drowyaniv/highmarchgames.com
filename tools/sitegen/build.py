"""Renders every page and the sitemap into a folder."""
from .layout import render_page
from .pages import PAGES
from .sitemap import sitemap_xml


def build_site(out_root):
    """Writes all pages under out_root; returns their paths in build order."""
    built = []
    for page in PAGES:
        doc = render_page(page.path, page.title, page.description, page.body, active=page.active)
        if page.post:
            doc = page.post(doc)
        out = out_root / page.path
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(doc, encoding="utf-8")
        built.append(page.path)
    (out_root / "sitemap.xml").write_text(sitemap_xml(built), encoding="utf-8")
    return built
