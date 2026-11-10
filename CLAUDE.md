# highmarchgames.com — working notes

- Follow the **organized-codebase** skill (`anthropic-skills:organized-codebase`) for every change in this repository.
- Structure and how a build runs: `Docs/ARCHITECTURE.md`. Reasons behind choices: `Docs/DECISIONS.md`.
- Page texts live in `tools/sitegen/pages/`; never edit the generated `.html` by hand.
- After a change: `python tools/build.py`, then `python -m unittest discover -s tests`, and commit the source with the regenerated pages.
- This repository is published as the website: keep private notes out of it.
