#!/usr/bin/env python3
"""
build_nav.py — Stages docs from configured Open Horizon source repositories
and writes mkdocs_build.yml ready for `mkdocs build -f mkdocs_build.yml`.

Usage:
    python scripts/build_nav.py [--dry-run]

Environment:
    ORG_READ_TOKEN   GitHub PAT with public_repo scope (optional but recommended)

Source repositories are read from mkdocs.yml `extra.doc_sources`. Each entry
replaces a former CopyDocs GitHub Action that pushed markdown into this repo.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any, Optional

import requests
import yaml

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

GITHUB_API = "https://api.github.com"
ORG = "open-horizon"
MKDOCS_TEMPLATE = "mkdocs.yml"
MKDOCS_BUILD = "mkdocs_build.yml"
# First-party guides and staged reference trees live under docs/docs/ so published
# URLs match the legacy site: /docs/... and /docs/<name>/docs/...
DOCS_CONTENT_ROOT = "docs/docs"
SECTIONS_DIR = "docs/docs/reference"
KEYWORD_FILE = "data/keyword.yml"

# Back-compat alias used by older tests / callers
DOCS_STAGING_DIR = DOCS_CONTENT_ROOT


def staged_docs_dir(dest_name: str) -> Path:
    """Filesystem path for a staged repo: docs/docs/<dest_name>/docs/."""
    return Path(DOCS_CONTENT_ROOT) / dest_name / "docs"


def staged_nav_prefix(dest_name: str) -> str:
    """Nav path prefix relative to docs_dir: docs/<dest_name>/docs."""
    return f"docs/{dest_name}/docs"

# Jekyll Liquid / Just-the-Docs artifacts commonly left in source-repo markdown
_LIQUID_KEYWORD_RE = re.compile(r"\{\{\s*site\.data\.keyword\.([A-Za-z0-9_-]+)\s*\}\}")
_JEKYLL_ATTR_LINE_RE = re.compile(r"^\{:.*?\}\s*$", re.MULTILINE)
_JEKYLL_INLINE_ATTR_RE = re.compile(r"\s*\{:[^}]+\}")

# ---------------------------------------------------------------------------
# GitHub API helpers
# ---------------------------------------------------------------------------


def load_keywords(path: str = KEYWORD_FILE) -> dict[str, str]:
    """Load Jekyll keyword substitutions from data/keyword.yml."""
    try:
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        if not isinstance(data, dict):
            return {}
        return {str(k): str(v).strip() for k, v in data.items() if v is not None}
    except OSError:
        return {}


def preprocess_markdown(text: str, keywords: Optional[dict[str, str]] = None) -> str:
    """
    Convert common Jekyll / Just-the-Docs markdown into MkDocs-friendly text.

    - Substitute {{site.data.keyword.*}} using data/keyword.yml
    - Strip {: attribute} lines and trailing inline attribute lists
    """
    keywords = keywords if keywords is not None else load_keywords()

    def _replace(match: re.Match) -> str:
        key = match.group(1)
        return keywords.get(key, match.group(0))

    text = _LIQUID_KEYWORD_RE.sub(_replace, text)
    text = _JEKYLL_ATTR_LINE_RE.sub("", text)
    text = _JEKYLL_INLINE_ATTR_RE.sub("", text)
    # Collapse runs of blank lines left by stripped attribute lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def preprocess_staged_tree(root: Path, keywords: Optional[dict[str, str]] = None) -> int:
    """Run preprocess_markdown on every .md file under *root*. Returns file count."""
    keywords = keywords if keywords is not None else load_keywords()
    count = 0
    for md in root.rglob("*.md"):
        original = md.read_text(encoding="utf-8", errors="replace")
        updated = preprocess_markdown(original, keywords)
        if updated != original:
            md.write_text(updated, encoding="utf-8")
            count += 1
    return count


def _headers() -> dict:
    token = (
        os.environ.get("ORG_READ_TOKEN")
        or os.environ.get("GH_TOKEN")
        or os.environ.get("GITHUB_TOKEN")
        or ""
    )
    h = {"Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        h["Authorization"] = f"Bearer {token}"
    return h


def get_repo_metadata(repo_name: str, org: str = ORG) -> Optional[dict]:
    """Return GitHub repo metadata, or None if the repo is missing."""
    url = f"{GITHUB_API}/repos/{org}/{repo_name}"
    resp = requests.get(url, headers=_headers(), timeout=30)
    if resp.status_code == 404:
        return None
    resp.raise_for_status()
    return resp.json()


def docs_dir_exists(repo_name: str, src_path: str = "docs", org: str = ORG) -> bool:
    """Return True if the given path exists in the repo."""
    url = f"{GITHUB_API}/repos/{org}/{repo_name}/contents/{src_path}"
    resp = requests.get(url, headers=_headers(), timeout=30)
    return resp.status_code == 200


# ---------------------------------------------------------------------------
# Config loading
# ---------------------------------------------------------------------------


def load_doc_sources(mkdocs_path: str = MKDOCS_TEMPLATE) -> list[dict[str, Any]]:
    """Read explicit doc source list from mkdocs.yml extra.doc_sources."""
    with open(mkdocs_path) as f:
        cfg = yaml.safe_load(f)
    sources = cfg.get("extra", {}).get("doc_sources", [])
    if not isinstance(sources, list):
        return []
    return [s for s in sources if isinstance(s, dict) and s.get("repo")]


def load_static_nav(mkdocs_path: str = MKDOCS_TEMPLATE) -> list:
    """Return the committed static nav from mkdocs.yml (or a Home fallback)."""
    with open(mkdocs_path) as f:
        cfg = yaml.safe_load(f)
    nav = cfg.get("nav")
    if isinstance(nav, list) and nav:
        return nav
    return [{"Home": "index.md"}]


# ---------------------------------------------------------------------------
# Staging helpers
# ---------------------------------------------------------------------------

_IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".ico"}


def _linked_md_files(readme_text: str) -> list[str]:
    """Parse relative .md links from markdown text."""
    linked = []
    for path in re.findall(r"\[(?:[^\]]*)\]\(([^)]+)\)", readme_text):
        path = path.split("#")[0].strip()
        if (
            path
            and not path.startswith(("http://", "https://", "/"))
            and path.lower().endswith(".md")
            and not any(part.startswith(".") for part in Path(path).parts)
        ):
            linked.append(path)
    return linked


def _linked_image_files(text: str) -> list[str]:
    """Parse relative image paths from markdown/HTML text."""
    candidates: list[str] = []
    candidates += re.findall(r"!\[[^\]]*\]\(([^)]+)\)", text)
    candidates += re.findall(r'<img\b[^>]*\bsrc=["\']([^"\']+)["\']', text, re.IGNORECASE)
    result = []
    for raw in candidates:
        path = raw.split("?")[0].split("#")[0].strip()
        if (
            path
            and not path.startswith(("http://", "https://", "/"))
            and Path(path).suffix.lower() in _IMAGE_EXTS
            and not any(part.startswith(".") for part in Path(path).parts)
        ):
            result.append(path)
    return result


def _clone_sparse(clone_url: str, dest: Path, paths: list[str], branch: Optional[str] = None) -> bool:
    """Shallow sparse-clone and check out the given path list."""
    try:
        cmd = ["git", "clone", "--depth", "1", "--filter=blob:none", "--sparse", "--no-local"]
        if branch:
            cmd += ["--branch", branch]
        cmd += [clone_url, str(dest)]
        subprocess.run(cmd, check=True, capture_output=True)
        subprocess.run(
            ["git", "sparse-checkout", "set"] + paths,
            cwd=str(dest),
            check=True,
            capture_output=True,
        )
        return True
    except subprocess.CalledProcessError as exc:
        err = exc.stderr.decode().strip() if exc.stderr else str(exc)
        print(f"  ⚠ clone failed for {dest.name}: {err}", file=sys.stderr)
        return False


def _rename_readmes(root: Path) -> None:
    """Rename every readme.md (case-insensitive) to index.md within *root*."""
    for md in list(root.rglob("*.md")):
        if md.name.lower() == "readme.md":
            target = md.parent / "index.md"
            if not target.exists():
                md.rename(target)


def _merge_repo_meta_into_markdown(
    path: Path,
    repo_html_url: str,
    repo_name: str,
    stars: int = 0,
    forks: int = 0,
) -> None:
    """
    Ensure a markdown file's front matter includes repo_* keys for the Material
    header source widget. Merges into existing YAML front matter when present.
    """
    content = path.read_text(encoding="utf-8", errors="replace")
    meta = {
        "repo_url": repo_html_url,
        "repo_name": repo_name,
        "repo_stars": stars,
        "repo_forks": forks,
    }
    if content.startswith("---"):
        m = _FM_RE.match(content)
        if m:
            try:
                existing = yaml.safe_load(m.group(1)) or {}
            except yaml.YAMLError:
                existing = {}
            if not isinstance(existing, dict):
                existing = {}
            existing.update(meta)
            body = content[m.end() :]
            dumped = yaml.dump(existing, default_flow_style=False, allow_unicode=True, sort_keys=False).rstrip()
            path.write_text(f"---\n{dumped}\n---\n{body}", encoding="utf-8")
            return
    front = (
        f"---\n"
        f"repo_url: {repo_html_url}\n"
        f"repo_name: {repo_name}\n"
        f"repo_stars: {stars}\n"
        f"repo_forks: {forks}\n"
        f"---\n\n"
    )
    path.write_text(front + content, encoding="utf-8")


def _inject_repo_front_matter(
    root: Path,
    repo_name: str,
    repo_html_url: str,
    org: str = ORG,
    stars: int = 0,
    forks: int = 0,
) -> None:
    """Stamp every staged markdown page with source-repo metadata for the header widget."""
    short_name = f"{org}/{repo_name}"
    for md in root.rglob("*.md"):
        _merge_repo_meta_into_markdown(md, repo_html_url, short_name, stars, forks)


def _apply_extras(clone_root: Path, dest: Path, extras: list[dict[str, str]]) -> None:
    """
    Copy extra files from the sparse clone into the staged dest.

    Each extra is {src: path-in-repo, dest: filename-under-dest}.
    Used for anax agent-install/README.md → overview.md.
    """
    for extra in extras:
        src_rel = extra.get("src")
        dest_rel = extra.get("dest")
        if not src_rel or not dest_rel:
            continue
        src = clone_root / src_rel
        if not src.exists():
            print(f"  ⚠ extra source missing: {src_rel}", file=sys.stderr)
            continue
        target = dest / dest_rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, target)
        print(f"  + extra {src_rel} → {dest_rel}")


def stage_source(
    source: dict[str, Any],
    repo_meta: dict,
    staging_root: str = DOCS_CONTENT_ROOT,
    dry_run: bool = False,
    org: str = ORG,
) -> Optional[str]:
    """
    Stage one configured doc source into docs/docs/<dest_name>/docs/.

    That layout publishes at /docs/<dest_name>/docs/, matching the legacy
    CopyDocs destination URLs on open-horizon.github.io.

    Returns the staging path on success, None on failure.
    """
    repo_name = source["repo"]
    dest_name = source.get("dest_name") or repo_name
    src_path = source.get("src_path") or "docs"
    branch = source.get("branch")
    extras = source.get("extras") or []
    repo_root = Path(staging_root) / dest_name
    dest = repo_root / "docs"

    if dry_run:
        print(f"  [dry-run] would clone {repo_name} ({src_path}) → {dest}/")
        return str(dest)

    if repo_root.exists():
        shutil.rmtree(repo_root)
    dest.mkdir(parents=True, exist_ok=True)

    # Sparse paths: docs tree plus any extra file parents
    sparse_paths = [src_path]
    for extra in extras:
        src_rel = extra.get("src", "")
        if src_rel:
            # Include the parent directory so sparse checkout can fetch the file
            parent = str(Path(src_rel).parent)
            if parent and parent != "." and parent not in sparse_paths:
                sparse_paths.append(parent)
            elif parent == ".":
                sparse_paths.append(src_rel)

    clone_tmp = Path(staging_root) / f"_clone_{dest_name}"
    if clone_tmp.exists():
        shutil.rmtree(clone_tmp)

    clone_url = repo_meta["clone_url"]
    if not _clone_sparse(clone_url, clone_tmp, sparse_paths, branch=branch):
        shutil.rmtree(repo_root, ignore_errors=True)
        shutil.rmtree(clone_tmp, ignore_errors=True)
        return None

    docs_sub = clone_tmp / src_path
    if not docs_sub.is_dir():
        print(f"  ⚠ no {src_path}/ found after clone for {repo_name}", file=sys.stderr)
        shutil.rmtree(repo_root, ignore_errors=True)
        shutil.rmtree(clone_tmp, ignore_errors=True)
        return None

    # Copy docs contents into docs/docs/<dest_name>/docs/
    for item in docs_sub.iterdir():
        target = dest / item.name
        if item.is_dir():
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)

    if extras:
        _apply_extras(clone_tmp, dest, extras)

    shutil.rmtree(clone_tmp, ignore_errors=True)

    if not list(dest.rglob("*.md")):
        print(f"  ⚠ no .md files in {src_path}/ for {repo_name}, skipping", file=sys.stderr)
        shutil.rmtree(repo_root, ignore_errors=True)
        return None

    _rename_readmes(dest)
    preprocess_staged_tree(dest)
    _inject_repo_front_matter(
        dest,
        repo_name,
        repo_meta["html_url"],
        org=org,
        stars=repo_meta.get("stargazers_count", 0),
        forks=repo_meta.get("forks_count", 0),
    )
    return str(dest)


# ---------------------------------------------------------------------------
# Navigation generation
# ---------------------------------------------------------------------------


_NAV_SKIP_NAMES = {"agents.md"}


def _nav_label_for_md(path: Path) -> str:
    """Humanize a markdown filename for sidebar labels."""
    stem = path.stem
    if stem.lower() in ("index", "readme"):
        return "Overview"
    return stem.replace("_", " ").replace("-", " ").strip().capitalize()


def _get_repo_entry_doc(repo_path: Path, dest_name: str) -> Optional[str]:
    """Find the primary documentation entry point for a staged repository."""
    md_files = sorted(repo_path.rglob("*.md"))
    if not md_files:
        return None

    prefix = staged_nav_prefix(dest_name)

    for filename in ("index.md", "readme.md"):
        for md in md_files:
            if md.parent == repo_path and md.name.lower() == filename:
                return f"{prefix}/{md.relative_to(repo_path)}"

    for filename in ("index.md", "readme.md"):
        for md in md_files:
            if md.name.lower() == filename:
                return f"{prefix}/{md.relative_to(repo_path)}"

    return f"{prefix}/{md_files[0].relative_to(repo_path)}"


def build_repo_nav_tree(repo_path: Path, dest_name: str) -> list:
    """
    Build a nested MkDocs nav list for all markdown files under a staged repo.

    Mirrors Just the Docs' expandable left-nav sections for each source repo.
    """
    prefix = staged_nav_prefix(dest_name)
    md_files = sorted(
        p for p in repo_path.rglob("*.md")
        if p.name.lower() not in _NAV_SKIP_NAMES
    )
    if not md_files:
        return []

    # Group by immediate parent directory relative to repo_path
    root_pages: list[dict] = []
    children_by_dir: dict[str, list[dict]] = {}

    for md in md_files:
        rel = md.relative_to(repo_path)
        nav_path = f"{prefix}/{rel.as_posix()}"
        label = _nav_label_for_md(md)
        if rel.parent == Path("."):
            # Prefer Overview first
            entry = {label: nav_path}
            if label == "Overview":
                root_pages.insert(0, entry)
            else:
                root_pages.append(entry)
        else:
            top = rel.parts[0]
            children_by_dir.setdefault(top, []).append({label: nav_path})

    nav_entries: list = list(root_pages)
    for dirname, entries in sorted(children_by_dir.items()):
        section_label = dirname.replace("_", " ").replace("-", " ").capitalize()
        nav_entries.append({section_label: entries})
    return nav_entries


def _write_section_index(
    label: str,
    entries: list[tuple[str, str, str]],
    dry_run: bool = False,
) -> str:
    """
    Create docs/docs/reference/index.md listing staged sources.

    entries: list of (nav_label, dest_name, doc_path)
    """
    out_path = Path(SECTIONS_DIR) / "index.md"
    nav_path = "docs/reference/index.md"

    lines = [f"# {label}", ""]
    lines.append(
        "Documentation staged at build time from Open Horizon source repositories. "
        "Edit content in the source repository — do not edit generated trees under "
        "`docs/docs/<name>/docs/`."
    )
    lines.append("")
    for nav_label, dest_name, doc_path in entries:
        # doc_path is relative to docs_dir, e.g. docs/anax/docs/index.md.
        # This page lives at docs/reference/index.md → link via ../<dest>/docs/...
        rel = doc_path[5:] if doc_path.startswith("docs/") else doc_path
        lines.append(f"- [{nav_label}](../{rel})")
    lines.append("")

    if dry_run:
        return nav_path

    Path(SECTIONS_DIR).mkdir(parents=True, exist_ok=True)
    out_path.write_text("\n".join(lines), encoding="utf-8")
    return nav_path


def append_reference_nav(
    static_nav: list,
    staged: list[tuple[dict[str, Any], str]],
    dry_run: bool = False,
) -> list:
    """
    Append each staged source repo as a top-level left-nav section.

    Prefer build_jekyll_style_nav() for a unified Just-the-Docs tree; this
    helper remains for tests and fallbacks.
    """
    nav = list(static_nav)

    overview_entries: list[tuple[str, str, str]] = []
    for source, path in staged:
        dest_name = source.get("dest_name") or source["repo"]
        nav_label = source.get("nav_label") or dest_name
        repo_path = Path(path)
        doc_path = _get_repo_entry_doc(repo_path, dest_name)
        if not doc_path and dry_run:
            doc_path = f"{staged_nav_prefix(dest_name)}/index.md"
        if not doc_path:
            continue
        overview_entries.append((nav_label, dest_name, doc_path))

        if dry_run:
            nav.append({nav_label: doc_path})
            continue

        tree = build_repo_nav_tree(repo_path, dest_name)
        if not tree:
            nav.append({nav_label: doc_path})
        else:
            nav.append({nav_label: tree})

    if overview_entries:
        section_index = _write_section_index("Reference", overview_entries, dry_run=dry_run)
        if not any(isinstance(item, dict) and "Reference" in item for item in nav):
            nav.append({"Reference index": section_index})

    return nav


# ---------------------------------------------------------------------------
# Just-the-Docs–compatible nav (title / parent / nav_order)
# ---------------------------------------------------------------------------

_STAGED_DEST_DIRS = {
    "anax",
    "mgmt-hub",
    "kubearmor-integration",
    "fdo",
    "exchange-api",
    "release",
    "reference",
}

_FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)


def _parse_front_matter(text: str) -> dict[str, Any]:
    m = _FM_RE.match(text)
    if not m:
        return {}
    try:
        data = yaml.safe_load(m.group(1)) or {}
        return data if isinstance(data, dict) else {}
    except yaml.YAMLError:
        return {}


def _collect_nav_pages() -> list[dict[str, Any]]:
    """
    Collect pages that participate in the Just-the-Docs-style sidebar.

    Includes first-party docs under docs/docs/, common-requests/, quick-start.md,
    and staged reference trees (so parent links across repo boundaries work).
    """
    pages: list[dict[str, Any]] = []
    scan_roots = [
        (Path(DOCS_CONTENT_ROOT), "docs"),
        (Path("docs/common-requests"), "common-requests"),
    ]
    quick = Path("docs/quick-start.md")
    if quick.exists():
        fm = _parse_front_matter(quick.read_text(encoding="utf-8", errors="replace"))
        title = str(fm.get("title") or "Quick Start").strip('"').strip("'")
        pages.append(
            {
                "title": title,
                "parent": (str(fm["parent"]).strip('"').strip("'") if fm.get("parent") else None),
                "order": int(fm["nav_order"]) if str(fm.get("nav_order", "")).isdigit() else 50,
                "path": "quick-start.md",
            }
        )

    for root, url_prefix in scan_roots:
        if not root.exists():
            continue
        for md in sorted(root.rglob("*.md")):
            rel = md.relative_to(root)
            # skip generated reference index only at docs/docs/reference/
            if url_prefix == "docs" and rel.parts and rel.parts[0] == "reference":
                continue
            if md.name.lower() in _NAV_SKIP_NAMES:
                continue
            if md.name == "index.md" and rel == Path("index.md") and url_prefix == "docs":
                # docs/docs/index.md is the Documentation landing; linked from Home
                continue
            text = md.read_text(encoding="utf-8", errors="replace")
            fm = _parse_front_matter(text)
            title = fm.get("title") or _nav_label_for_md(md)
            title = str(title).strip().strip('"').strip("'")
            parent = fm.get("parent")
            parent = str(parent).strip().strip('"').strip("'") if parent else None
            order_raw = fm.get("nav_order")
            try:
                order = int(order_raw)
            except (TypeError, ValueError):
                order = 999
            nav_path = f"{url_prefix}/{rel.as_posix()}"
            pages.append(
                {"title": title, "parent": parent, "order": order, "path": nav_path}
            )
    return pages


def build_jekyll_style_nav() -> list:
    """
    Build left-nav contents from title/parent/nav_order front matter.

    This reproduces the Just the Docs information architecture so the sidebar
    lists the same sections and pages as the legacy Jekyll site.
    """
    pages = _collect_nav_pages()
    by_title: dict[str, dict[str, Any]] = {}
    for p in pages:
        # Last write wins on duplicate titles (rare); prefer lower path length
        existing = by_title.get(p["title"])
        if existing and len(existing["path"]) <= len(p["path"]):
            continue
        by_title[p["title"]] = {**p, "children": []}

    roots: list[dict[str, Any]] = []
    for p in by_title.values():
        parent = p.get("parent")
        if parent and parent in by_title and parent != p["title"]:
            by_title[parent]["children"].append(p)
        else:
            roots.append(p)

    def sort_key(node: dict[str, Any]) -> tuple:
        return (node.get("order", 999), node.get("title", "").lower())

    def emit(node: dict[str, Any]) -> dict:
        children = sorted(node.get("children") or [], key=sort_key)
        if not children:
            return {node["title"]: node["path"]}
        items: list = [{node["title"]: node["path"]}]
        items.extend(emit(child) for child in children)
        return {node["title"]: items}

    return [emit(r) for r in sorted(roots, key=sort_key)]


# ---------------------------------------------------------------------------
# mkdocs_build.yml generation
# ---------------------------------------------------------------------------


def write_build_config(
    nav: list,
    template_path: str = MKDOCS_TEMPLATE,
    output_path: str = MKDOCS_BUILD,
    dry_run: bool = False,
) -> None:
    """Merge nav into the template mkdocs.yml and write mkdocs_build.yml."""
    with open(template_path) as f:
        cfg = yaml.safe_load(f)

    cfg["nav"] = nav
    cfg["docs_dir"] = "docs"

    if dry_run:
        print("\n--- Generated nav (dry-run) ---")
        print(yaml.dump({"nav": nav}, default_flow_style=False, allow_unicode=True))
        return

    with open(output_path, "w") as f:
        yaml.dump(cfg, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    print(f"✓ Written {output_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Stage Open Horizon source-repo docs and generate mkdocs_build.yml"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print configured sources and nav without cloning or writing files",
    )
    parser.add_argument(
        "--org",
        default=ORG,
        help=f"GitHub organization name (default: {ORG})",
    )
    args = parser.parse_args()

    sources = load_doc_sources()
    print(f"Configured doc sources: {len(sources)}")

    staged: list[tuple[dict[str, Any], str]] = []

    if not args.dry_run:
        Path(DOCS_CONTENT_ROOT).mkdir(parents=True, exist_ok=True)

    print("\nStaging source repositories…")
    for source in sources:
        repo_name = source["repo"]
        dest_name = source.get("dest_name") or repo_name

        if args.dry_run:
            print(f"  [dry-run] {repo_name} → {staged_docs_dir(dest_name)}/")
            staged.append((source, str(staged_docs_dir(dest_name))))
            continue

        try:
            meta = get_repo_metadata(repo_name, args.org)
        except requests.HTTPError as exc:
            print(f"  ⚠ failed to fetch metadata for {repo_name}: {exc}", file=sys.stderr)
            continue

        if meta is None:
            print(f"  – {repo_name} not found, skipping")
            continue

        src_path = source.get("src_path") or "docs"
        if not docs_dir_exists(repo_name, src_path, args.org):
            print(f"  – {repo_name} has no {src_path}/, skipping")
            continue

        path = stage_source(source, meta, dry_run=False, org=args.org)
        if path:
            staged.append((source, path))
            print(f"  ✓ staged {repo_name} → {dest_name}")
        else:
            print(f"  – {repo_name} skipped")

    # Unified left-nav from Just-the-Docs title/parent/nav_order across first-party
    # and staged pages (so cross-folder parents resolve like the legacy site).
    print("\nBuilding sidebar from page front matter…")
    content_nav = build_jekyll_style_nav()
    nav: list = [
        {"Home": "index.md"},
        {"Documentation": "docs/index.md"},
    ] + content_nav
    print(f"  {len(content_nav)} top-level sidebar sections")

    write_build_config(nav, dry_run=args.dry_run)

    if not args.dry_run:
        print(f"\nDone. Run: mkdocs serve -f {MKDOCS_BUILD} -a 127.0.0.1:8765")


if __name__ == "__main__":
    main()
