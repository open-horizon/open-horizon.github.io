# Contributing to Open Horizon Documentation

Thank you for contributing. This guide covers local preview, Dev Containers, and how documentation is assembled from source repositories.

---

## Prerequisites

- Python 3.9 or later
- `git`
- (Optional) `make`

---

## Local setup

```bash
git clone https://github.com/open-horizon/open-horizon.github.io
cd open-horizon.github.io

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
export ORG_READ_TOKEN=ghp_...   # optional but recommended

make serve
```

Preview: <http://127.0.0.1:8765>

| Command        | Description |
|----------------|-------------|
| `make stage`   | Fetch source-repo docs into `docs/docs/<name>/docs/` |
| `make serve`   | Stage then start MkDocs |
| `make dry-run` | List configured sources without cloning |
| `make test`    | Run unit tests |
| `make clean`   | Remove generated artifacts |

---

## Environment variables

| Variable | Required | Description |
| --- | --- | --- |
| `ORG_READ_TOKEN` | Recommended | Classic GitHub PAT with `public_repo` scope for API + clone rate limits |

Copy `.env.example` to `.env` for local use. Never commit `.env`.

---

## Generated paths (do not commit)

| Path | Description |
| --- | --- |
| `docs/docs/<name>/docs/` | Staged documentation from source repositories |
| `docs/docs/reference/` | Generated Reference overview page |
| `site/` | MkDocs HTML output |
| `mkdocs_build.yml` | Resolved MkDocs config with dynamic Reference nav |

---

## Where to edit content

- **First-party guides** (Getting started, Installing, Developing, Administering): edit Markdown under `docs/docs/` in this repository (URLs under `/docs/`).
- **Reference docs** (agent, hub, exchange, FDO, Kubearmor, release): edit the **source repository** listed in `mkdocs.yml` → `extra.doc_sources`. Do not edit generated `docs/docs/<name>/docs/` trees.

### Adding or changing a source repository

1. Open `mkdocs.yml`.
2. Add or update an entry under `extra.doc_sources`:

   ```yaml
   - repo: my-repo
     branch: main
     src_path: docs
     dest_name: my-repo
     nav_label: My docs
     section: Reference
   ```

3. Run `make dry-run` then `make serve` to verify.

Once this pull-at-build model is live, the CopyDocs workflows in child repositories (`copydocs.yml` / `copy-docs.yml`) can be removed so they no longer push into this repo.

---

## Dev Container / Codespaces

1. Open the repo in VS Code and reopen in the Dev Container, or start a Codespace.
2. Ensure `ORG_READ_TOKEN` is available (host env or Codespaces secret).
3. Run `make serve` and open the forwarded port **8765**.

---

## Tests

```bash
make test
```

Tests live in `tests/test_build_nav.py` and use mocked HTTP where needed.

---

## Pull requests

- Open an issue before a large change when possible.
- Use a focused branch and descriptive commits (`git commit -s` for DCO sign-off when contributing upstream).
- Link the PR to the related issue (for example [#729](https://github.com/open-horizon/open-horizon.github.io/issues/729)).
