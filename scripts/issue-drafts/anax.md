### Context

The Open Horizon documentation site is moving from Jekyll + Just the Docs to **MkDocs Material**, with docs pulled from this repository at build time (see [open-horizon/open-horizon.github.io#729](https://github.com/open-horizon/open-horizon.github.io/issues/729)). The new portal follows the same approach as [open-horizon-services.github.io](https://github.com/open-horizon-services/open-horizon-services.github.io).

Until source markdown is cleaned up, the docs build substitutes `{{site.data.keyword.*}}` and strips `{: …}` markers as a temporary compatibility layer. That should not remain the long-term contract for this repo’s `docs/`.

### Problem

A large share of files under `docs/` still use Jekyll Liquid keyword placeholders and Just-the-Docs attribute syntax, for example:

- `{{site.data.keyword.edge_notm}}`, `{{site.data.keyword.horizon}}`, and related keys
- Standalone or trailing `{:codeblock}`, `{: #anchor}`, `{:target="_blank"}` markers

Rough scan of current `docs/`: **~27 of 34** Markdown files contain `site.data.keyword`, and **~29** contain `{:` attribute markers. Heaviest examples include `docs/api.md`, `docs/properties_and_constraints.md`, `docs/model_policy.md`, and `docs/agreement_bot_api.md`.

The repo still **pushes** docs into `open-horizon.github.io` via CopyDocs GitHub Actions. That model is replaced by **pull-at-build-time** on the portal, so those workflows (and the agent guidance that documents them) are obsolete once the new site is the publishing path.

### Ask

#### 1. Clean up Markdown for MkDocs Material

1. Replace every `{{site.data.keyword.<key>}}` with the plain text term adopters should see (prefer **Open Horizon** / **OH** rather than legacy IBM Edge Application Manager wording unless a sentence is intentionally about IBM products).
2. Remove Just-the-Docs / Jekyll attribute markers (`{: …}`).
3. Prefer relative links that work inside this repo’s `docs/` tree (the portal stages that tree as-is). `agent-install/README.md` continues to be staged as `overview.md` by the portal.

#### 2. Adjust YAML front matter (do not strip nav keys)

The portal builds the left nav from Just-the-Docs–compatible front matter across first-party **and** staged child-repo pages. For files under `docs/`:

| Keep | Drop (unused by MkDocs / portal) |
| --- | --- |
| `title` (nav label) | `layout` |
| `parent` (nav hierarchy) | `has_children` |
| `nav_order` (nav order) | `has_toc` |
| Optional: `description`, `copyright`, `years`, `lastupdated` | |

Do **not** add `repo_url` / `repo_name` / `repo_stars` / `repo_forks` in source — the portal injects those at build time for the header source widget.

#### 3. Remove CopyDocs GitHub Actions

Delete the push-based docs sync workflow(s); the portal clones this repo’s `docs/` (and `agent-install/README.md`) at build time instead:

- Remove [`.github/workflows/copydocs.yml`](../.github/workflows/copydocs.yml) (Copy Docs + agent-install README copy jobs).
- Remove any other leftover CopyDocs / copycat workflows if present (older docs mentioned `copyagentreadme.yml`; confirm and delete if it still exists).
- After removal, `PERSONAL_TOKEN` (or equivalent) secrets used only for CopyDocs can be retired from this repo’s settings.

Coordinate cutover with [open-horizon.github.io#729](https://github.com/open-horizon/open-horizon.github.io/issues/729) so the portal is already pulling docs before (or as) CopyDocs stops pushing.

#### 4. Update `docs/AGENTS.md` for pull-at-build

Rewrite [`docs/AGENTS.md`](../docs/AGENTS.md) so agents and contributors are not told to rely on CopyDocs. It should describe:

1. **Source of truth:** edit Markdown only in this repository (`docs/`, plus `agent-install/README.md` for the agent install overview).
2. **Publishing:** `open-horizon.github.io` **pulls** this tree at docs build time into `/docs/anax/docs/` (no push from this repo).
3. **Front matter rules** from section 2 above (keep `title` / `parent` / `nav_order`; drop `layout` / `has_children` / `has_toc`).
4. **No Liquid / `{: …}` markers**; write plain Markdown.
5. **Do not** document or reintroduce CopyDocs / `andstor/copycat-action` workflows.

### Why it matters

- Source docs should be correct when read on GitHub, not only after a portal preprocess step.
- Stops conflicting push/pull publishing and removes unused Actions + tokens.
- Keeps sidebar structure working via `title` / `parent` / `nav_order` under MkDocs Material.

### References

- Tracking: https://github.com/open-horizon/open-horizon.github.io/issues/729
- Keyword map formerly used by the Jekyll site: `_data/keyword.yml` in `open-horizon.github.io` (legacy)
- Temporary preprocess + staging: `scripts/build_nav.py` on the new docs site
- Destination: **Reference → Edge node agents (anax)** → `/docs/anax/docs/`
