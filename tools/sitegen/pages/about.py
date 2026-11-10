"""About the studio and contact."""
from ..config import EMAIL
from ..page import Page

PAGE = Page("about/index.html", "About",
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
""", active="About")
