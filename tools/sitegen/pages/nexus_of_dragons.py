"""The Nexus of Dragons game page."""
from ..content.nexus import FEATURES_HTML, GALLERY_HTML, GAME_SHORT, HEROES_HTML
from ..page import Page
from ..widgets import LIGHTBOX_JS

PAGE = Page("games/nexus-of-dragons/index.html", "Nexus of Dragons",
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
      <p>Nexus of Dragons is played on a board of three rings, across the land of Thandrys. Each turn you roll, choose
      your road and face what you find there: a monster to fight, a stranger with an offer, a town to rest in, a gate
      that will only open for the strong.</p>
      <p>Your hero grows with every step – levels, spells, gear, a horse, a few loyal companions. The other heroes on the
      board are racing you to the same prize. Only one of you will take mastery of the Nexus Crystal.</p>
    </div>
    <div class="card"><img src="{r}assets/img/nexus/shots/table-800.webp" alt="The board of Nexus of Dragons on the table, seen from above" width="800" height="450" loading="lazy">
      <div class="body"><p class="mt0 muted" style="margin:0">To win, reach the Nexus Temple, defeat the dragon that guards it and take mastery of the Crystal.</p></div></div>
  </div>
</section>
<section class="band">
  <div class="wrap">
    <p class="eyebrow">Features</p>
    <h2>What waits on the road</h2>
    <ul class="features">""" + FEATURES_HTML + """</ul>
  </div>
</section>
<section id="screens">
  <div class="wrap">
    <p class="eyebrow">Screenshots</p>
    <h2>From the table</h2>
    <div class="gallery">""" + GALLERY_HTML + """</div>
    <p class="note">Work in progress. Everything shown may change before release.</p>
  </div>
</section>
<section class="story">
  <img class="bg" src="{r}assets/img/nexus/keyart-960.webp" alt="" width="960" height="536" loading="lazy">
  <div class="wrap">
    <p class="eyebrow">The Waking of the Nexus</p>
    <h2>Now the dead march again</h2>
    <blockquote>For eight hundred years the Crystal has burned half-open, corrupted by the souls the lich Vael Morrath
    poured into it. Every few decades it flares: the monsters come, the dead walk, and its guardian rises to burn the
    land. Now the dead march again, and someone is leading them. Whoever finishes the ritual will hold the Nexus.</blockquote>
  </div>
</section>
<section>
  <div class="wrap">
    <p class="eyebrow">Heroes</p>
    <h2>Dozens of heroes, each with a story</h2>
    <p class="lede">A gate captain searching for the man who raised him. A library guard who has kept her lady's last
    order for eight hundred years. A hunter tracking a corrupted dragon through the marshes. Choose one of them – or
    make your own.</p>
    <div class="heroes">""" + HEROES_HTML + """</div>
  </div>
</section>
""" + LIGHTBOX_JS, active="Games")
