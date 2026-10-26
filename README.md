# Open Horizon Documentation

Documentation site for [Open Horizon](https://github.com/open-horizon) — autonomous management of containerized workloads and machine learning assets across fleets of edge devices.

**Stack:** MkDocs + Material theme (same approach as [open-horizon-services.github.io](https://github.com/open-horizon-services/open-horizon-services.github.io)). Reference docs from child repositories are **pulled at build time**, replacing the former CopyDocs GitHub Actions that pushed markdown into this repo.

**Live site (after Pages is configured):** <https://open-horizon.github.io>

---

## Local development

### Prerequisites

- Python 3.9+
- Git

### Setup

```bash
git clone https://github.com/open-horizon/open-horizon.github.io
cd open-horizon.github.io

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

# Optional: avoid GitHub API rate limits when staging source repos
export ORG_READ_TOKEN=ghp_...

make serve
```

Preview: <http://127.0.0.1:8765>

### Make targets

| Command        | Description                                      |
|----------------|--------------------------------------------------|
| `make stage`   | Fetch source-repo docs and write `mkdocs_build.yml` |
| `make serve`   | Stage then start the preview server              |
| `make build`   | Stage then build static HTML into `site/`        |
| `make dry-run` | Show configured sources without cloning          |
| `make test`    | Run unit tests                                   |
| `make clean`   | Remove staged docs and build output              |

### Dev Container / Codespaces

Open this repository in VS Code with the Dev Containers extension or in GitHub Codespaces. Dependencies install automatically. See [CONTRIBUTING.md](CONTRIBUTING.md).

---

## Documentation sources

| Path / nav | Source |
| --- | --- |
| `/`, `/quick-start/` | This repository (`docs/index.md`, `docs/quick-start.md`) |
| `/docs/...` guides | This repository (`docs/docs/`) |
| `/docs/anax/docs/` | [`open-horizon/anax`](https://github.com/open-horizon/anax) `docs/` (+ `agent-install/README.md`) |
| `/docs/mgmt-hub/docs/` | [`open-horizon/devops`](https://github.com/open-horizon/devops) `docs/` |
| `/docs/kubearmor-integration/docs/` | [`open-horizon/kubearmor-integration`](https://github.com/open-horizon/kubearmor-integration) `docs/` |
| `/docs/fdo/docs/` | [`open-horizon/FDO-support`](https://github.com/open-horizon/FDO-support) `docs/` |
| `/docs/exchange-api/docs/` | [`open-horizon/exchange-api`](https://github.com/open-horizon/exchange-api) `docs/` |
| `/docs/release/docs/` | [`open-horizon/open-horizon-release`](https://github.com/open-horizon/open-horizon-release) `docs/` |

Configure sources in `mkdocs.yml` under `extra.doc_sources`.

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md).
