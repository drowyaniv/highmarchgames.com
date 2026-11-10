# highmarchgames.com

The website of Highmarch Games: a plain static site (HTML + CSS, a few lines of JavaScript for the screenshot viewer).
No build step is needed on the server: GitHub Pages serves the files as they are.

## Pages

| Address | File |
|---|---|
| `/` | `index.html` - the studio home |
| `/games/` | `games/index.html` - all games |
| `/games/nexus-of-dragons/` | the Nexus of Dragons page |
| `/press/` | press kit (fact sheet, screenshots, logos, ZIP) |
| `/about/` | about the studio and contact |
| any missing page | `404.html` |

## Editing

The pages share one header and footer, so they are generated. Page texts are in `tools/sitegen/pages/`
(one file per page); the structure is described in `Docs/ARCHITECTURE.md`. After a change run:

```
python tools/build.py
python -m unittest discover -s tests
```

and commit the changed source together with the regenerated `.html` files. Styles are in `assets/site.css`.

## Hosting (GitHub Pages + Porkbun)

1. Create a **public** GitHub repository (for example `highmarchgames.com`) and push this folder to it.
2. Repository **Settings -> Pages**: Source "Deploy from a branch", branch `main`, folder `/ (root)`.
   The `CNAME` file already holds `highmarchgames.com`.
3. At **Porkbun -> Domain -> DNS**, remove the default parking records and add:
   - `A` records for `highmarchgames.com` (host empty) to `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - `CNAME` record `www` to `<your-github-user>.github.io`
4. Back in **Settings -> Pages**, wait for the DNS check, then tick **Enforce HTTPS**.
5. **E-mail:** the public address is `yaniv@highmarchgames.com` (Porkbun Email Forwarding to the owner's mailbox, already set up). It is set as `EMAIL` in `tools/sitegen/config.py`.

Check the current values in GitHub's documentation ("Managing a custom domain for your GitHub Pages site") before entering them.

## Fonts and art

- IM Fell English SC (headings) - SIL Open Font License, `assets/fonts/OFL-IMFellEnglishSC.txt`.
- Game art and screenshots are from Nexus of Dragons (see `Docs/AI_CONTENT_REGISTER.md` in the game project).
