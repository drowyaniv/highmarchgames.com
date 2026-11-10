# highmarchgames.com — architecture

A static website. A small Python generator writes the HTML pages; GitHub Pages serves the repository root as it is.
Everything in this repository is published, so it holds no private notes.

## Where things are

| Folder | What lives there | Start reading |
|---|---|---|
| `/` (root) | The published site: generated `index.html`, `404.html`, `sitemap.xml`; icons, `CNAME`, `robots.txt` | — (generated, never edit by hand) |
| `games/`, `about/` | Generated pages | — |
| `press/` | Generated press page, plus the downloads: `art/`, `screens/`, the press-kit ZIP | `press/index.html` |
| `assets/` | `site.css`, `fonts/` (with their licences), `img/studio/` (logo), `img/nexus/` (game art) | `assets/site.css` |
| `tools/build.py` | Entry point: builds every page | `tools/build.py` |
| `tools/sitegen/` | Generator core: settings, page shell, sitemap | `sitegen/build.py` |
| `tools/sitegen/pages/` | One module per page — **page texts are edited here** | `pages/__init__.py` |
| `tools/sitegen/content/` | Game data used on several pages (texts, image lists) | `content/nexus.py` |
| `tests/` | Generator tests | `tests/test_build.py` |
| `Docs/` | This guide and `DECISIONS.md` | — |

## How a build runs

1. `python tools/build.py` puts `tools/` on the import path and calls `sitegen.build.build_site(ROOT)`.
2. `build_site` walks `PAGES` (`sitegen/pages/__init__.py`) in order: home, games, Nexus of Dragons, press, about, 404.
3. Each `Page` body goes through `layout.render_page`, which adds the shared head, header and footer and turns `{r}` into the relative path back to the root.
4. A page may rewrite its finished document (`Page.post`): the 404 page makes its links absolute, because it is served at any depth.
5. The pages and `sitemap.xml` are written into the repository root.
6. `python -m unittest discover -s tests` checks the result; commit the source together with the regenerated `.html`.

## Conventions

- **A new page:** a module in `sitegen/pages/` with a `PAGE = Page(...)`, added to `PAGES`.
- **A new game:** its data in `sitegen/content/<game>.py`, its images in `assets/img/<game>/`, a page module, and a card on the games page.
- **Shared page parts** that belong to no single game go in `sitegen/widgets.py`; site-wide settings (domain, e-mail, menu) in `sitegen/config.py`.
- **Texts:** use the real characters (`–`, `’`), not HTML entities. Image captions and feature texts are passed through `html.escape`, which would show an entity as text.
- **Size:** no source file over ~500 lines; split a growing page into a module plus content.
- **Comments:** one to three lines on what a thing is for; history goes in commit messages, reasons in `Docs/DECISIONS.md`.
