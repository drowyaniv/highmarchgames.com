"""One generated page: where it is written and what goes in it."""
from typing import Callable, NamedTuple, Optional


class Page(NamedTuple):
    path: str  # output path from the site root, e.g. "games/index.html"
    title: str
    description: str
    body: str  # HTML inside <main>; "{r}" becomes the relative path back to the site root
    active: Optional[str] = None  # main-menu label to mark as the current page
    post: Optional[Callable[[str], str]] = None  # rewrites the finished document (used by the 404 page)
