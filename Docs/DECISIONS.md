# highmarchgames.com — technical decisions

Why the site is built the way it is. Newest first; add an entry when a choice is made or changed.

## Headings use IM Fell English SC, served from the site
The heading font is self-hosted in `assets/fonts/` with its SIL Open Font License file, so pages make no requests to font services.
The logo does not depend on it: its lettering and the ™ are outlines inside the SVG.

## No newsletter block for now
A mail-to "keep me posted" box asks visitors to write an e-mail by hand and needs a list to be kept by hand.
It returns as social links once the accounts exist and as a Steam wishlist button once the store page exists.

## Literal characters instead of HTML entities in texts
Captions and feature texts are passed through `html.escape`; an entity such as `&ndash;` would be shown as text.

## Generated static HTML, committed to the repository
A small Python generator (`tools/sitegen/`) writes plain HTML so every page shares one header and footer without a framework or a build on the server.
The generated pages are committed because GitHub Pages serves the repository as it is. A test fails when they are out of date.

## Relative links, except on the 404 page
Relative links let the site work from a local folder or any test server. GitHub Pages serves `404.html` at any depth, so that page uses absolute links.

## Hosting: GitHub Pages, domain at Porkbun
Free static hosting with HTTPS; the domain and the e-mail forwarding stay at the registrar.
