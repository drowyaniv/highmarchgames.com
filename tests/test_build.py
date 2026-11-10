"""Checks the site generator: run from the repository root with  python -m unittest discover -s tests"""
import re
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from sitegen.build import build_site  # noqa: E402

LINK = re.compile(r'(?:href|src)="([^"]+)"')
EXTERNAL = ("http://", "https://", "mailto:", "#")


class BuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.out = Path(cls.tmp.name)
        cls.built = build_site(cls.out)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_builds_every_page(self):
        self.assertEqual(self.built, ["index.html", "games/index.html", "games/nexus-of-dragons/index.html",
                                      "press/index.html", "about/index.html", "404.html"])

    def test_committed_pages_are_up_to_date(self):
        # The published .html files must be exactly what the generator writes: run tools/build.py after editing.
        for rel in self.built + ["sitemap.xml"]:
            with self.subTest(rel):
                built = (self.out / rel).read_text(encoding="utf-8")
                committed = (ROOT / rel).read_text(encoding="utf-8")
                self.assertEqual(built, committed)

    def test_every_local_link_exists(self):
        for rel in self.built:
            page_dir = (ROOT / rel).parent
            for link in LINK.findall((self.out / rel).read_text(encoding="utf-8")):
                if link.startswith(EXTERNAL):
                    continue
                path = link.split("#")[0].split("?")[0]
                target = ROOT / path.lstrip("/") if path.startswith("/") else page_dir / path
                with self.subTest(page=rel, link=link):
                    self.assertTrue(target.exists(), f"{link} -> {target}")

    def test_404_uses_only_absolute_links(self):
        doc = (self.out / "404.html").read_text(encoding="utf-8")
        relative = [l for l in LINK.findall(doc) if not l.startswith(EXTERNAL + ("/",))]
        self.assertEqual(relative, [])

    def test_no_double_escaped_entities(self):
        for rel in self.built:
            with self.subTest(rel):
                self.assertNotRegex((self.out / rel).read_text(encoding="utf-8"), r"&amp;[a-z]+;")

    def test_sitemap_lists_pages_but_not_404(self):
        sitemap = (self.out / "sitemap.xml").read_text(encoding="utf-8")
        self.assertIn("<loc>https://highmarchgames.com/press/</loc>", sitemap)
        self.assertNotIn("404", sitemap)

    def test_logo_tm_is_an_outline(self):
        # The TM must not depend on the visitor's fonts.
        for name in ("highmarch_logo_horizontal_on_dark.svg", "highmarch_logo_horizontal_on_light.svg"):
            svg = (ROOT / "assets/img/studio" / name).read_text(encoding="utf-8")
            with self.subTest(name):
                self.assertTrue('id="trademark"' in svg and "<text" not in svg, name)


if __name__ == "__main__":
    unittest.main()
