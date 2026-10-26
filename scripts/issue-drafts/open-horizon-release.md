### Context

Open Horizon docs are migrating from Jekyll + Just the Docs to **MkDocs Material**, with this repo’s `docs/` staged at build time ([open-horizon/open-horizon.github.io#729](https://github.com/open-horizon/open-horizon.github.io/issues/729)).

### Problem

`docs/index.md` still uses Jekyll Liquid (`{{site.data.keyword.edge_notm}}`) and related Just-the-Docs markers. The new portal substitutes keywords temporarily; source content should stand alone. This repo also still **pushes** docs via CopyDocs; the portal now **pulls** at build time instead.

### Ask

#### 1. Clean up Markdown for MkDocs Material

1. Replace `{{site.data.keyword.*}}` with plain text (typically **Open Horizon**).
2. Remove `{: …}` attribute markers.
3. Prefer relative links within `docs/`.

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

Delete the push-based docs sync workflow; the portal clones this repo’s `docs/` at build time into `/docs/release/docs/`:

- Remove [`.github/workflows/copydocs.yml`](../.github/workflows/copydocs.yml).
- Retire `PERSONAL_TOKEN` (or equivalent) secrets used only for CopyDocs.

Coordinate cutover with [open-horizon.github.io#729](https://github.com/open-horizon/open-horizon.github.io/issues/729).

#### 4. Add or update `docs/AGENTS.md` for pull-at-build

If `docs/AGENTS.md` is missing, create it; otherwise rewrite it so it does not describe CopyDocs push publishing. It should cover:

1. Edit docs only in this repository’s `docs/` tree.
2. The portal **pulls** that tree at build time (destination `/docs/release/docs/`).
3. Front matter rules from section 2 (`title` / `parent` / `nav_order` kept; `layout` / `has_children` / `has_toc` dropped).
4. No Liquid / `{: …}` markers.
5. Do not reintroduce CopyDocs / `andstor/copycat-action`.

### References

- https://github.com/open-horizon/open-horizon.github.io/issues/729
- Nav label: **Reference → Release** → `/docs/release/docs/`
