"""About the studio and contact."""
from ..config import EMAIL
from ..page import Page

PAGE = Page("about/index.html", "About",
    "About Highmarch Games, a one-person independent game studio, and how to get in touch.",
    """<section>
  <div class="wrap split">
    <div>
      <p class="eyebrow">About</p>
      <h1>Highmarch Games</h1>
      <hr class="rule">
      <p class="lede">A one-person independent game studio, making games worth coming back to.</p>
      <p>I care about rules that are easy to learn and hard to master, worlds with a history behind them, and heroes who
      are more than a set of numbers. My first game, <a href="{r}games/nexus-of-dragons/">Nexus of Dragons</a>, is a
      fantasy adventure board game for one to six players, in development for PC. I make my games with the help of AI
      tools – for the artwork, the music, some of the sound and the game text – and I direct, review and rework every
      piece until it fits.</p>
    </div>
    <div class="card" id="contact"><div class="body">
      <h2 class="mt0">Contact</h2>
      <p>Questions, press, or just a hello – write to me at</p>
      <p><a class="btn" href="mailto:""" + EMAIL + """">""" + EMAIL + """</a></p>
      <p class="muted" style="margin:0">Press can find screenshots, logos and the fact sheet in the <a href="{r}press/">press kit</a>.</p>
    </div></div>
  </div>
</section>
""", active="About")
