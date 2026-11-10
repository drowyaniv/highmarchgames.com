"""All games: one card per game and a placeholder for the next."""
from ..content.nexus import GAME_CARD
from ..page import Page

PAGE = Page("games/index.html", "Games",
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
""", active="Games")
