"""Press kit for Nexus of Dragons: fact sheet, descriptions, downloads."""
import html

from ..config import EMAIL
from ..content.nexus import FEATURES_HTML, GAME_SHORT, SHOTS
from ..page import Page

PAGE = Page("press/index.html", "Press kit",
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
      Players choose from a wide cast of heroes, each with a story and a personal quest, and journey inward across the
      three rings of Thandrys. Along the way they fight monsters with dice on the table, rest and trade in towns, buy
      mounts, hire companions and take on contracts, while the lich's four lieutenants roam the board. The first hero to
      reach the Nexus Temple, defeat the dragon that guards it and take mastery of the Nexus Crystal wins. Matches come
      in two lengths: Classic and Quick.</p>
    </div>
  </div>
</section>
<section id="features">
  <div class="wrap">
    <h2>Features</h2>
    <ul class="features">""" + FEATURES_HTML + """</ul>
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
</section>""", active="Press")
