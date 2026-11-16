"""Studio home page: the studio hero and the current game."""
from ..content.nexus import GAME_CARD
from ..page import Page

PAGE = Page("index.html", "Highmarch Games",
    "Highmarch Games is an independent game studio. Its first game, Nexus of Dragons, a fantasy adventure board game for PC, is in development.",
    """<section class="studio-hero">
  <div class="wrap">
    <img class="emblem" src="{r}assets/img/studio/highmarch_logo_emblem.svg" alt="" width="164" height="192">
    <p class="eyebrow">Independent game studio</p>
    <h1>Worlds worth the journey</h1>
    <p class="lede">Highmarch Games is an independent studio. Different worlds, one promise: games worth coming back to –
    each with its own rules and its own story.</p>
    <div class="btns"><a class="btn primary" href="{r}games/nexus-of-dragons/">Nexus of Dragons</a></div>
  </div>
</section>
<section>
  <div class="wrap">
    <p class="eyebrow">My first game</p>
    """ + GAME_CARD + """
  </div>
</section>
""")
