"""Builds the static HTML pages of highmarchgames.com.

The pages share one header and footer, so they are written from this script.
Run it after editing any text below:  python tools/build.py
It writes plain .html files that GitHub Pages serves as they are (no build on the server).
Links are relative, so the site also works when opened from a local folder or a test server.
"""
from pathlib import Path
import html

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://highmarchgames.com"
EMAIL = "yaniv@highmarchgames.com"
YEAR = 2026

NAV = [("Games", "games/"), ("Press", "press/"), ("About", "about/")]


def page(path, title, description, body, *, active=None, og_image="assets/img/nexus/og-nexus.jpg", extra_head=""):
    """path: output path relative to the site root, e.g. 'games/index.html'."""
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
<meta property="og:image" content="{SITE}/{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#121014">
<link rel="icon" href="{r}favicon.svg" type="image/svg+xml">
<link rel="icon" href="{r}favicon.ico" sizes="32x32">
<link rel="apple-touch-icon" href="{r}apple-touch-icon.png">
<link rel="manifest" href="{r}site.webmanifest">
<link rel="preload" href="{r}assets/fonts/IMFellEnglishSC-Regular.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{r}assets/site.css">
{extra_head}</head>
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
    out = ROOT / path
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")
    return path


# ---------- shared pieces ----------
GAME_SHORT = ("A fantasy adventure board game for one to six players. Choose a hero, journey inward across three "
              "rings of a painted land, and face the Shadow Dragon at the heart of the Nexus.")



GAME_CARD = """<a class="feature-game" href="{r}games/nexus-of-dragons/">
  <img class="bg" src="{r}assets/img/nexus/keyart-1920.webp" srcset="{r}assets/img/nexus/keyart-960.webp 960w, {r}assets/img/nexus/keyart-1920.webp 1920w" sizes="(max-width: 1120px) 100vw, 1120px" alt="" width="1920" height="1072" loading="lazy">
  <div class="inner">
    <img class="game-logo" src="{r}assets/img/nexus/nexus-logo-994.webp" alt="Nexus of Dragons" width="994" height="416" loading="lazy">
    <div><span class="tag">In development</span><span class="tag">PC</span><span class="tag">1–6 players</span></div>
    <p>""" + GAME_SHORT + """</p>
    <span class="btn">Explore the game &rarr;</span>
  </div>
</a>"""

# ---------- pages ----------
built = []

built.append(page("index.html", "Highmarch Games",
    "Highmarch Games is an independent game studio. Its first game, Nexus of Dragons, a fantasy adventure board game for PC, is in development.",
    """<section class="studio-hero">
  <div class="wrap">
    <img class="emblem" src="{r}assets/img/studio/highmarch_logo_emblem.svg" alt="" width="164" height="192">
    <p class="eyebrow">Independent game studio</p>
    <h1>Worlds worth the journey</h1>
    <p class="lede">Highmarch Games is an independent studio. Different worlds, one promise: games worth coming back to –
    each with its own rules, its own story, and evenings you look up from hours later.</p>
    <div class="btns"><a class="btn primary" href="{r}games/nexus-of-dragons/">Nexus of Dragons</a></div>
  </div>
</section>
<section>
  <div class="wrap">
    <p class="eyebrow">My first game</p>
    """ + GAME_CARD + """
  </div>
</section>
"""))

built.append(page("games/index.html", "Games",
    "Games by Highmarch Games: Nexus of Dragons, a fantasy adventure board game in development for PC.",
    """<section>
  <div class="wrap">
    <p class="eyebrow">Games</p>
    <h1>Our games</h1>
    <hr class="rule">
    """ + GAME_CARD + """
    <div class="cards" style="margin-top:22px">
      <div class="card placeholder"><div><h3>More in the forge</h3><p class="mt0">Nexus of Dragons is our first world. It will not be the last.</p></div></div>
    </div>
  </div>
</section>
""", active="Games"))

SHOTS = [
    ("board", "The painted board: three rings of lands around the Nexus Temple."),
    ("hero", "Every step is a choice – where to go, and what waits there."),
    ("lieutenant", "The Shadow Dragon's lieutenants roam the land."),
    ("dragon", "At the heart of the Nexus waits the Shadow Dragon."),
    ("town", "Towns to rest, trade, train and take on contracts."),
    ("tavern", "Taverns along the road, and companions to hire in them."),
]
gallery = "\n".join(
    f'<button type="button" data-full="{{r}}assets/img/nexus/shots/{k}-1600.webp" data-caption="{html.escape(c)}">'
    f'<img src="{{r}}assets/img/nexus/shots/{k}-800.webp" alt="{html.escape(c)}" width="800" height="343" loading="lazy"></button>'
    for k, c in SHOTS)
HEROES = ["warrior_gareth_m", "mage_eldrin_f", "priest_corvin_f", "rogue_varis_f", "ranger_fenn_m", "hilldwarf_warrior_f",
          "dragonborn_mage_m", "tiefling_ranger_f", "highelf_cleric_m", "halforc_rogue_f", "lightfoothalfling_ranger_m", "rockgnome_mage_f"]
heroes = "".join(f'<img src="{{r}}assets/img/nexus/heroes/{h}.webp" alt="" width="200" height="300" loading="lazy">' for h in HEROES)

FEATURES = [
    ("Journey to the heart", "Three rings of land – the Outer, the Middle and the Inner – each harder than the last. "
     "Find the crossings, earn your way inward and reach the Nexus Temple."),
    ("Ninety heroes", "Nine peoples and five callings: warriors, mages, clerics, rogues and rangers, each hero with a story "
     "and a personal quest of their own. Or make your own hero."),
    ("Dice on the table", "Every blow, spell and saving throw is rolled out in front of you, from the d4 to the d20. "
     "Classic tabletop rules decide every fight."),
    ("Towns and the road", "Rest at inns, trade in markets, buy a mount at the stables, hire companions in taverns, "
     "take guild contracts – and perhaps raise a dragon of your own."),
    ("The Shadow Dragon's lieutenants", "Four of the dragon's servants walk the land. Beat them for their treasures – "
     "or run when you must."),
    ("Your table, your length", "Up to six players in any mix of friends at one screen and computer heroes. "
     "Play a Classic match for the long road or a Quick one for an evening."),
]
features = "\n".join(f"<li><h3>{t}</h3><p>{html.escape(d)}</p></li>" for t, d in FEATURES)

LIGHTBOX_JS = """<dialog class="lightbox" id="lightbox" aria-label="Screenshot">
  <form method="dialog"><button class="close" aria-label="Close">Close &times;</button></form>
  <img alt="" id="lightbox-img"><p id="lightbox-cap"></p>
</dialog>
<script>
(() => {
  const dlg = document.getElementById('lightbox'), img = document.getElementById('lightbox-img'), cap = document.getElementById('lightbox-cap');
  if (!dlg || !dlg.showModal) return;
  document.querySelectorAll('.gallery button').forEach(b => b.addEventListener('click', () => {
    img.src = b.dataset.full; img.alt = b.dataset.caption; cap.textContent = b.dataset.caption; dlg.showModal();
  }));
  dlg.addEventListener('click', e => { if (e.target === dlg) dlg.close(); });
})();
</script>"""

built.append(page("games/nexus-of-dragons/index.html", "Nexus of Dragons",
    "Nexus of Dragons is a fantasy adventure board game for one to six players, in development for PC by Highmarch Games.",
    """<div class="game-hero">
  <picture>
    <source media="(max-width: 900px)" srcset="{r}assets/img/nexus/keyart-night-960.webp">
    <img src="{r}assets/img/nexus/keyart-night-1920.webp" alt="" width="1920" height="1072">
  </picture>
  <div class="wrap">
    <h1 class="skip">Nexus of Dragons</h1>
    <img class="game-logo" src="{r}assets/img/nexus/nexus-logo-994.webp" alt="Nexus of Dragons" width="994" height="416">
    <div><span class="tag">In development</span><span class="tag">PC (Windows)</span><span class="tag">1–6 players</span></div>
    <p class="lede">""" + GAME_SHORT + """</p>
    <div class="btns"><a class="btn primary" href="#screens">Screenshots</a></div>
  </div>
</div>
<section>
  <div class="wrap split">
    <div>
      <p class="eyebrow">The game</p>
      <h2>A board game you can lose yourself in</h2>
      <hr class="rule">
      <p>Nexus of Dragons is played on a painted board of three rings. Each turn you roll, choose your road and face
      what you find there: a monster to fight, a stranger with an offer, a town to rest in, a gate that will only open
      for the strong.</p>
      <p>Your hero grows with every step – levels, spells, gear, a horse, a few loyal companions. The other heroes on the
      board are racing you to the same prize. Only one of you will take mastery of the Nexus Crystal.</p>
    </div>
    <div class="card"><img src="{r}assets/img/nexus/shots/board-800.webp" alt="The board of Nexus of Dragons, seen from above" width="800" height="343" loading="lazy">
      <div class="body"><p class="mt0 muted" style="margin:0">To win, reach the Nexus Temple, defeat the Shadow Dragon and take mastery of the Crystal.</p></div></div>
  </div>
</section>
<section class="band">
  <div class="wrap">
    <p class="eyebrow">Features</p>
    <h2>What waits on the road</h2>
    <ul class="features">""" + features + """</ul>
  </div>
</section>
<section id="screens">
  <div class="wrap">
    <p class="eyebrow">Screenshots</p>
    <h2>From the table</h2>
    <div class="gallery">""" + gallery + """</div>
    <p class="note">Work in progress. Everything shown may change before release.</p>
  </div>
</section>
<section class="story">
  <img class="bg" src="{r}assets/img/nexus/keyart-960.webp" alt="" width="960" height="536" loading="lazy">
  <div class="wrap">
    <p class="eyebrow">The Waking of the Nexus</p>
    <h2>This spring, the Crystal flared</h2>
    <blockquote>Beasts no one had seen in a lifetime came down onto the roads. The dead began to march in step.
    And at the heart of the Nexus, coiled around the Crystal, the Shadow Dragon woke.</blockquote>
  </div>
</section>
<section>
  <div class="wrap">
    <p class="eyebrow">Heroes</p>
    <h2>Ninety heroes, ninety stories</h2>
    <p class="lede">A gate captain searching for the man who raised him. A glassblower's daughter who taught herself fire.
    A hunter tracking a corrupted dragon through the marshes. Every hero comes with a story and a quest of their own.</p>
    <div class="heroes">""" + heroes + """</div>
  </div>
</section>
""" + LIGHTBOX_JS, active="Games"))

PRESS_FILES = [
    # (file in press/, title, size note, thumb, thumb class)
    ("nexus-of-dragons-presskit.zip", "Everything", "Screenshots, art and logos (ZIP)", None, ""),
]
built.append(page("press/index.html", "Press kit",
    "Press kit for Nexus of Dragons and Highmarch Games: fact sheet, description, screenshots, logos and contact.",
    """<section>
  <div class="wrap">
    <p class="eyebrow">Press kit</p>
    <h1>Nexus of Dragons</h1>
    <p class="lede">Everything you need to write about the game. All images may be used in coverage of Nexus of Dragons.</p>
    <div class="btns"><a class="btn primary" href="nexus-of-dragons-presskit.zip" download>Download everything (ZIP)</a><a class="btn" href="mailto:""" + EMAIL + """?subject=Press%20enquiry">Press enquiries</a></div>
    <nav class="toc" aria-label="On this page"><a href="#facts">Fact sheet</a><a href="#about">Description</a><a href="#features">Features</a><a href="#screens">Screenshots</a><a href="#art">Logos &amp; art</a><a href="#studio">Studio</a></nav>
  </div>
</section>
<section id="facts" class="band">
  <div class="wrap split">
    <div>
      <h2>Fact sheet</h2>
      <table class="facts">
        <tr><th>Game</th><td>Nexus of Dragons</td></tr>
        <tr><th>Developer &amp; publisher</th><td>Highmarch Games</td></tr>
        <tr><th>Genre</th><td>Fantasy adventure board game</td></tr>
        <tr><th>Players</th><td>1–6, local (one screen); any mix of people and computer heroes</td></tr>
        <tr><th>Platform</th><td>PC (Windows)</td></tr>
        <tr><th>Release date</th><td>To be announced</td></tr>
        <tr><th>Price</th><td>To be announced</td></tr>
        <tr><th>Language</th><td>English</td></tr>
        <tr><th>Website</th><td><a href="https://highmarchgames.com/games/nexus-of-dragons/">highmarchgames.com</a></td></tr>
        <tr><th>Press contact</th><td><a href="mailto:""" + EMAIL + """">""" + EMAIL + """</a></td></tr>
      </table>
    </div>
    <div id="about">
      <h2>Description</h2>
      <p><b>Short:</b> """ + GAME_SHORT + """</p>
      <p><b>Long:</b> Nexus of Dragons is a fantasy adventure board game for one to six players, in development for PC.
      Players choose from ninety heroes – nine peoples, five classes, each with a story and a personal quest – and journey
      inward across three rings of a painted land. Along the way they fight monsters with dice on the table, rest and
      trade in towns, buy mounts, hire companions and take on contracts, while four lieutenants of the Shadow Dragon roam
      the board. The first hero to reach the Nexus Temple, defeat the Shadow Dragon and take mastery of the Nexus Crystal
      wins. Matches come in two lengths: Classic and Quick.</p>
    </div>
  </div>
</section>
<section id="features">
  <div class="wrap">
    <h2>Features</h2>
    <ul class="features">""" + features + """</ul>
  </div>
</section>
<section id="screens" class="band">
  <div class="wrap">
    <h2>Screenshots</h2>
    <p class="muted">Click an image for the full-size file. Work in progress – everything shown may change before release.</p>
    <div class="downloads">""" + "\n".join(
        f'<a href="screens/{k}.jpg" download><div class="thumb"><img class="cover" src="{{r}}assets/img/nexus/shots/{k}-800.webp" alt="{html.escape(c)}" loading="lazy"></div>'
        f'<div class="meta"><b>{html.escape(c)}</b><span>JPG</span></div></a>' for k, c in SHOTS) + """</div>
  </div>
</section>
<section id="art">
  <div class="wrap">
    <h2>Logos &amp; art</h2>
    <div class="downloads">
      <a href="art/nexus-of-dragons-logo.png" download><div class="thumb"><img src="{r}assets/img/nexus/nexus-logo-994.webp" alt="Nexus of Dragons logo" loading="lazy"></div><div class="meta"><b>Game logo</b><span>PNG, transparent</span></div></a>
      <a href="art/nexus-of-dragons-icon.png" download><div class="thumb"><img src="{r}assets/img/nexus/nexus-icon-256.webp" alt="Nexus of Dragons icon" loading="lazy"></div><div class="meta"><b>Game icon</b><span>PNG, 1024 x 1024</span></div></a>
      <a href="art/nexus-of-dragons-key-art.jpg" download><div class="thumb"><img class="cover" src="{r}assets/img/nexus/keyart-960.webp" alt="Key art" loading="lazy"></div><div class="meta"><b>Key art – dusk</b><span>JPG, 1920 x 1072</span></div></a>
      <a href="art/nexus-of-dragons-key-art-night.jpg" download><div class="thumb"><img class="cover" src="{r}assets/img/nexus/keyart-night-960.webp" alt="Key art at night" loading="lazy"></div><div class="meta"><b>Key art – night</b><span>JPG, 1920 x 1072</span></div></a>
      <a href="art/highmarch-games-logo-dark.png" download><div class="thumb"><img src="{r}assets/img/studio/highmarch_logo_horizontal_on_dark.svg" alt="Highmarch Games logo for dark backgrounds" loading="lazy"></div><div class="meta"><b>Studio logo – dark backgrounds</b><span>PNG, transparent (SVG in the ZIP)</span></div></a>
      <a href="art/highmarch-games-logo-light.png" download><div class="thumb light"><img src="{r}assets/img/studio/highmarch_logo_horizontal_on_light.svg" alt="Highmarch Games logo for light backgrounds" loading="lazy"></div><div class="meta"><b>Studio logo – light backgrounds</b><span>PNG, transparent (SVG in the ZIP)</span></div></a>
    </div>
  </div>
</section>
<section id="studio" class="band">
  <div class="wrap">
    <h2>About Highmarch Games</h2>
    <p class="lede">Highmarch Games is an independent studio making fantasy games. Nexus of Dragons is its first game.
    <a href="{r}about/">More about the studio</a>.</p>
  </div>
</section>""", active="Press"))

built.append(page("about/index.html", "About",
    "About Highmarch Games, an independent studio making fantasy games, and how to get in touch.",
    """<section>
  <div class="wrap split">
    <div>
      <p class="eyebrow">About</p>
      <h1>Highmarch Games</h1>
      <hr class="rule">
      <p class="lede">An independent studio making fantasy games – the kind you sit down to for an evening and look up
      from hours later.</p>
      <p>We care about worlds that feel painted rather than generated in bulk, rules that are easy to learn and hard to
      master, and heroes who are more than a set of numbers. Our first game, <a href="{r}games/nexus-of-dragons/">Nexus of Dragons</a>,
      is a fantasy adventure board game for one to six players, in development for PC.</p>
    </div>
    <div class="card" id="contact"><div class="body">
      <h2 class="mt0">Contact</h2>
      <p>Questions, press, or just a hello – write to us at</p>
      <p><a class="btn" href="mailto:""" + EMAIL + """">""" + EMAIL + """</a></p>
      <p class="muted" style="margin:0">Press can find screenshots, logos and the fact sheet in the <a href="{r}press/">press kit</a>.</p>
    </div></div>
  </div>
</section>
""", active="About"))

# 404 - GitHub Pages serves /404.html for missing pages at any depth, so its links are absolute.
built.append(page("404.html", "Page not found", "This page does not exist.",
    """<section class="studio-hero">
  <div class="wrap">
    <img class="emblem" src="/assets/img/studio/highmarch_logo_emblem.svg" alt="" width="164" height="192">
    <h1>The road ends here</h1>
    <p class="lede">This page does not exist – or it has wandered off the map.</p>
    <div class="btns"><a class="btn primary" href="/">Back to the start</a></div>
  </div>
</section>"""))
# The 404 page is served from any depth: make its shared links absolute.
p404 = ROOT / "404.html"
p404.write_text(p404.read_text(encoding="utf-8").replace('href="./"', 'href="/"').replace('href="assets/', 'href="/assets/')
                .replace('src="assets/', 'src="/assets/').replace('href="favicon', 'href="/favicon').replace('href="apple-', 'href="/apple-')
                .replace('href="site.web', 'href="/site.web').replace('href="games/', 'href="/games/').replace('href="press/', 'href="/press/')
                .replace('href="about/', 'href="/about/'), encoding="utf-8")

# sitemap
urls = [p.replace("index.html", "") for p in built if p != "404.html"]
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + "".join(f"  <url><loc>{SITE}/{u}</loc></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
print("built:", ", ".join(built))
