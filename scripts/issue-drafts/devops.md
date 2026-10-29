### Context

The Open Horizon documentation site is moving from Jekyll + Just the Docs to **MkDocs Material**, pulling this repository’s `docs/` at build time into the Management Hub reference section ([open-horizon/open-horizon.github.io#729](https://github.com/open-horizon/open-horizon.github.io/issues/729)). Pattern reference: [open-horizon-services.github.io](https://github.com/open-horizon-services/open-horizon-services.github.io).

Until source markdown is cleaned up, the portal may substitute Liquid keywords and strip `{: …}` markers temporarily. Source content should not depend on that.

### Problem

`docs/` still contains Jekyll Liquid keyword usage (for example `{{site.data.keyword.macOS_notm}}` in `docs/index.md`) and Just-the-Docs-oriented front matter / markers. This repo also still **pushes** docs via CopyDocs; the portal now **pulls** at build time instead.

### Ask

#### 1. Clean up Markdown for MkDocs Material

1. Replace `{{site.data.keyword.*}}` with plain text (for example macOS, Open Horizon).
2. Remove any Just-the-Docs `{: …}` markers if present.
3. Keep links valid relative to this repo’s `docs/` tree.

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

Delete the push-based docs sync workflow; the portal clones this repo’s `docs/` at build time into `/docs/mgmt-hub/docs/`:

- Remove [`.github/workflows/copy-docs.yml`](../.github/workflows/copy-docs.yml).
- Retire `PERSONAL_TOKEN` (or equivalent) secrets used only for CopyDocs.

Coordinate cutover with [open-horizon.github.io#729](https://github.com/open-horizon/open-horizon.github.io/issues/729).

#### 4. Update `docs/AGENTS.md` for pull-at-build

Rewrite [`docs/AGENTS.md`](../docs/AGENTS.md) so it no longer describes CopyDocs push publishing. It should cover:

1. Edit docs only in this repository’s `docs/` tree.
2. The portal **pulls** that tree at build time (destination `/docs/mgmt-hub/docs/`).
3. Front matter rules from section 2 (`title` / `parent` / `nav_order` kept; `layout` / `has_children` / `has_toc` dropped).
4. No Liquid / `{: …}` markers.
5. Do not reintroduce CopyDocs / `andstor/copycat-action`.

### References

- https://github.com/open-horizon/open-horizon.github.io/issues/729
- Destination nav label: **Reference → Management Hub** (`dest_name: mgmt-hub`) → `/docs/mgmt-hub/docs/`
