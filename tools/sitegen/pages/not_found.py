"""404 page. GitHub Pages serves /404.html for missing pages at any depth, so its shared links are made absolute."""
from ..page import Page

# Relative link starts in the shared shell and what they become on the 404 page.
_ABSOLUTE = [
    ('href="./"', 'href="/"'), ('href="assets/', 'href="/assets/'), ('src="assets/', 'src="/assets/'),
    ('href="favicon', 'href="/favicon'), ('href="apple-', 'href="/apple-'), ('href="site.web', 'href="/site.web'),
    ('href="games/', 'href="/games/'), ('href="press/', 'href="/press/'), ('href="about/', 'href="/about/'),
]


def absolute_links(doc):
    for old, new in _ABSOLUTE:
        doc = doc.replace(old, new)
    return doc


PAGE = Page("404.html", "Page not found", "This page does not exist.",
    """<section class="studio-hero">
  <div class="wrap">
    <img class="emblem" src="/assets/img/studio/highmarch_logo_emblem.svg" alt="" width="164" height="192">
    <h1>The road ends here</h1>
    <p class="lede">This page does not exist – or it has wandered off the map.</p>
    <div class="btns"><a class="btn primary" href="/">Back to the start</a></div>
  </div>
</section>""",
    post=absolute_links)
