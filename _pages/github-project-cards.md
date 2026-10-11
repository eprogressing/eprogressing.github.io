---
permalink: /github-project-cards/
title: "GitHub Project Cards"
author_profile: true
---

# GitHub Project Cards

GitHub Project Cards keeps the selected open-source projects on my personal website up to date. It reads public repository metadata from the GitHub REST API and generates accessible cards with descriptions, stars, forks, primary language and license.

[View the cards]({{ '/' | relative_url }}#open-source-title){:target="_self"} or [browse the source](https://github.com/eprogressing/eprogressing.github.io/tree/main/scripts).

## How it works

Only repositories explicitly listed in `_data/github_repositories.json` are included. The generator runs during the GitHub Pages build and on a daily schedule. It produces a static snapshot, so visitors can see the cards without JavaScript, sign-in or an API request from their browser. The snapshot date is displayed alongside the cards.

The integration reads repository metadata without modifying repositories. Responses marked private are rejected before publishing. Temporary API failures retain the last successful snapshot; changing the selected repository list requires a successful refresh before the new list is published.

## Use it on a Jekyll website

1. Add the repositories and display titles to `_data/github_repositories.json`.
2. Run `python3 scripts/refresh_github_projects.py` before building Jekyll.
3. Include `github-project-cards.html` and import the card stylesheet.

Local refreshes work without authentication for public repositories. GitHub Actions supplies its read-only token during builds; tokens are never included in the generated page or data file.

## Support

Questions or feedback: [2312632@mail.nankai.edu.cn](mailto:2312632@mail.nankai.edu.cn).
