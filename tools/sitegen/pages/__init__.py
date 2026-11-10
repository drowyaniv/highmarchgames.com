"""One module per page; PAGES is the build order."""
from . import about, games, home, nexus_of_dragons, not_found, press

PAGES = [home.PAGE, games.PAGE, nexus_of_dragons.PAGE, press.PAGE, about.PAGE, not_found.PAGE]
