"""Nexus of Dragons: the texts and image lists used on the home, games, game and press pages."""
import html

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

SHOTS = [
    ("table", "The table: a painted board of three rings, with the decks and the gold beside it."),
    ("lieutenant", "One of the Shadow Dragon's lieutenants stands in a hero's way."),
    ("fight", "A fight with a manticore: keep the roll, or spend Luck on a second throw."),
    ("town", "Highcrest, the fortress-city every road eventually leads back to."),
    ("heroes", "Ninety heroes to choose from – or make your own."),
    ("market", "Weapons, armour and potions in Highcrest's marketplace."),
    ("hero-card", "Every hero comes with a story and a personal quest of their own."),
    ("dice-move", "Roll the d6 and choose your road."),
    ("dice-attack", "Every attack is a d20 thrown on the table."),
]
GALLERY_HTML = "\n".join(
    f'<button type="button" data-full="{{r}}assets/img/nexus/shots/{k}-1400.webp" data-caption="{html.escape(c)}">'
    f'<img src="{{r}}assets/img/nexus/shots/{k}-800.webp" alt="{html.escape(c)}" width="800" height="450" loading="lazy"></button>'
    for k, c in SHOTS)
HEROES = ["warrior_gareth_m", "mage_eldrin_f", "priest_corvin_f", "rogue_varis_f", "ranger_fenn_m", "hilldwarf_warrior_f",
          "dragonborn_mage_m", "tiefling_ranger_f", "highelf_cleric_m", "halforc_rogue_f", "lightfoothalfling_ranger_m", "rockgnome_mage_f"]
HEROES_HTML = "".join(f'<img src="{{r}}assets/img/nexus/heroes/{h}.webp" alt="" width="200" height="300" loading="lazy">' for h in HEROES)

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
FEATURES_HTML = "\n".join(f"<li><h3>{t}</h3><p>{html.escape(d)}</p></li>" for t, d in FEATURES)
