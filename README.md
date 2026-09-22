![Workflow Status](https://github.com/joaomlourenco/joaomlourenco.github.io/actions/workflows/gh-pages.yml/badge.svg)

# João Lourenço — personal academic page

Source for my personal academic website, built with [Hugo](https://gohugo.io/) and the
[wowchemy / starter-hugo-academic](https://wowchemy.com/) theme. You can find the
[live version here](https://joaomlourenco.github.io/).

Looking for the **NOVAthesis** LaTeX template instead? Head to its own
[repository](https://github.com/joaomlourenco/novathesis).

## Content

- `content/authors/admin/` — profile (bio, interests, social links)
- `content/home/` — homepage sections (about, news, software, teaching, projects,
  advisees, publications), toggled and ordered via `active`/`weight` in each file
- `content/publications/` — one folder per paper
- `content/software/` — LaTeX packages and other tools I maintain
- `content/news/`, `content/teaching/`, `content/projects/`, `content/advisees/` —
  simple markdown entries, one per item

## Updating the publication list

Publications are populated from my [Google Scholar profile](https://scholar.google.com/citations?user=8aN-HtMAAAAJ&hl=en)
using the script in [scripts/](scripts/), adapted from Simon Gravelle's
[scholar-collector](https://github.com/simongravelle/scholar-collector). To refresh:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install scholarly "bibtexparser<2"
python3 scripts/collect_publications.py content/publications/
```

It only adds publications that aren't already present, so it's safe to re-run.

## How to build locally

```bash
hugo server
```

## How to deploy

Pushing to `master` triggers the `gh-pages.yml` GitHub Action, which builds the site
with Hugo and publishes it to the `gh-pages` branch. In the repository Settings → Pages,
set the source to deploy from the `gh-pages` branch, `/(root)`.

## Credit

This site is based on the personal page template built by
[Simon Gravelle](https://github.com/simongravelle/simongravelle.github.io), itself
based on [wowchemy](https://wowchemy.com/).
