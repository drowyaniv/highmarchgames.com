"""The shared page shell: head, header with the main menu, footer."""
import html

from .config import EMAIL, NAV, SITE, YEAR

OG_IMAGE = "assets/img/nexus/og-nexus.jpg"  # link-preview image for every page


def render_page(path, title, description, body, active=None):
    """Wraps a page body in the shared head, header and footer."""
    depth = path.count("/")
    r = "../" * depth  # relative prefix back to the site root
    canonical = SITE + "/" + path.replace("index.html", "")
    nav = "".join(
        f'<a href="{r}{href}"{" aria-current=\"page\"" if label == active else ""}>{label}</a>' for label, href in NAV
    )
    full_title = title if title.endswith("Highmarch Games") else f"{title} | Highmarch Games"
    doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Highmarch Games">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/{OG_IMAGE}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#121014">
<link rel="icon" href="{r}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{r}favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="{r}apple-touch-icon.png">
<link rel="manifest" href="{r}site.webmanifest">
<link rel="preload" href="{r}assets/fonts/IMFellEnglishSC-Regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{r}assets/site.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{r or './'}" aria-label="Highmarch Games – home"><img src="{r}assets/img/studio/highmarch_logo_horizontal_on_dark.svg" alt="Highmarch Games" width="455" height="192"></a>
    <nav class="nav" aria-label="Main">{nav}</nav>
  </div>
</header>
<main id="main">
{body.replace("{r}", r)}
</main>
<footer class="site-footer">
  <div class="wrap">
    <img src="{r}assets/img/studio/highmarch_logo_horizontal_on_dark.svg" alt="" width="455" height="192">
    <nav aria-label="Footer"><a href="{r}games/nexus-of-dragons/">Nexus of Dragons</a><a href="{r}press/">Press kit</a><a href="{r}about/">About</a><a href="mailto:{EMAIL}">{EMAIL}</a></nav>
    <div>&copy; {YEAR} Highmarch Games. All rights reserved. Highmarch&trade; and the Highmarch logo are trademarks of Highmarch Games.</div>
  </div>
</footer>
</body>
</html>
"""
    return doc
