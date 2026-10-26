# Open Horizon Documentation — Agent Guidelines

This repository is the Open Horizon documentation site. It is built with **MkDocs** and the **Material** theme (same stack as [open-horizon-services.github.io](https://github.com/open-horizon-services/open-horizon-services.github.io)), and is intended for GitHub Pages.

It replaces the previous Jekyll + Just the Docs + Ruby toolchain.

---

## Prerequisites and first-time setup

### Required software

- **Python 3.9+**
- **Git**
- (Optional) **Make**

### Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
export ORG_READ_TOKEN=ghp_...   # optional; avoids GitHub API rate limits
make serve
```

Preview: <http://127.0.0.1:8765>

| Make target | Purpose |
| --- | --- |
| `make stage` | Run `scripts/build_nav.py` to clone source-repo docs and write `mkdocs_build.yml` |
| `make serve` | Stage, then `mkdocs serve` on port 8765 |
| `make build` | Stage, then `mkdocs build` into `site/` |
| `make dry-run` | Print configured sources without cloning |
| `make test` | Run `pytest` |
| `make clean` | Remove generated staged trees under `docs/docs/*/docs/`, `site/`, `mkdocs_build.yml` |

---

## Architecture

### First-party docs

Markdown under `docs/docs/` (getting started, installing, developing, administering) is authored in this repository and publishes at `/docs/...`. Root pages `docs/index.md` and `docs/quick-start.md` publish at `/` and `/quick-start/`. Navigation is declared in `mkdocs.yml` under `nav:`.

### Reference docs from child repositories

Previously, child repositories used CopyDocs GitHub Actions (`andstor/copycat-action`) to **push** their `docs/` trees into this repo on every merge. That model is replaced by **pull-at-build-time**:

1. `extra.doc_sources` in `mkdocs.yml` lists each source repository, branch, source path, destination name, and nav label.
2. `scripts/build_nav.py` clones those trees into `docs/docs/<dest_name>/docs/`, injects per-repo front matter, and appends a **Reference** section to `mkdocs_build.yml`. Published URLs match the legacy shape `/docs/<dest_name>/docs/`.
3. CI (`.github/workflows/deploy.yml`) runs the script before `mkdocs build` and deploys `site/` to `gh-pages`.

| Destination (URL) | Source repository |
| --- | --- |
| `/docs/anax/docs/` | `open-horizon/anax` (`docs/` + `agent-install/README.md` → `overview.md`) |
| `/docs/mgmt-hub/docs/` | `open-horizon/devops` (`docs/`) |
| `/docs/kubearmor-integration/docs/` | `open-horizon/kubearmor-integration` (`docs/`) |
| `/docs/fdo/docs/` | `open-horizon/FDO-support` (`docs/`) |
| `/docs/exchange-api/docs/` | `open-horizon/exchange-api` (`docs/`) |
| `/docs/release/docs/` | `open-horizon/open-horizon-release` (`docs/`) |

**Important:** Never edit generated files under `docs/docs/<name>/docs/`. Change content only in the source repositories. After this site is the production docs host, remove the CopyDocs workflows from those child repositories so they stop pushing into this repo, and update each child repo’s `docs/AGENTS.md` so it describes pull-at-build (not CopyDocs push). Tracking issues for that cleanup live in the child repos and reference [#729](https://github.com/open-horizon/open-horizon.github.io/issues/729).

---

## Content style

- Prefer third-person, active voice.
- Use "adopter" rather than "customer" when referring to people who use Open Horizon.
- Headings: sentence case (capitalize the first word and proper nouns only).
- Numbered lists for sequences; bullets for unordered items.
- Avoid directional or visual-only instructions ("click the blue button above").
- Prefer plain English over Latin abbreviations (for example, "for example" instead of "e.g.").

### Front matter

MkDocs Material uses optional YAML front matter. Left-nav contents are built from Just-the-Docs–compatible keys on **first-party and staged** pages:

| Keep in source `docs/` | Drop (Just-the-Docs only) |
| --- | --- |
| `title`, `parent`, `nav_order` | `layout`, `has_children`, `has_toc` |
| Optional: `description`, `copyright`, `years`, `lastupdated` | |

During staging, `build_nav.py` merges `repo_url`, `repo_name`, `repo_stars`, and `repo_forks` into every staged reference markdown page so the header source widget (`overrides/partials/source.html`) links to that page’s origin repository. Authors must not add those `repo_*` keys in child repos. First-party pages fall back to `repo_url` / `repo_name` in `mkdocs.yml`.

---

## Code and project conventions

- Python: keep `scripts/build_nav.py` testable; add coverage in `tests/test_build_nav.py` for new helpers.
- Do not commit secrets. Use `ORG_READ_TOKEN` via environment or GitHub Actions secrets.
- Generated artifacts are gitignored: `docs/docs/*/docs/`, `docs/docs/reference/`, `site/`, `mkdocs_build.yml`, `.env`.

### Git / contribution notes for upstream Open Horizon

- Prefer signed-off commits (`git commit -s`) when contributing to the upstream project.
- Open an issue before large changes; link PRs to issues.
- Branch naming in the upstream project often follows `issue-###`.

---

## Updating these guidelines

Update this file whenever the build toolchain, source-repo list, or contribution workflow changes.
