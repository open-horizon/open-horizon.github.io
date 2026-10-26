"""
tests/test_build_nav.py — Unit tests for scripts/build_nav.py
"""
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import yaml

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

import build_nav  # noqa: E402


SAMPLE_SOURCES = [
    {
        "repo": "anax",
        "branch": "master",
        "src_path": "docs",
        "dest_name": "anax",
        "nav_label": "Agent (anax)",
        "section": "Reference",
        "extras": [{"src": "agent-install/README.md", "dest": "overview.md"}],
    },
    {
        "repo": "devops",
        "branch": "master",
        "src_path": "docs",
        "dest_name": "mgmt-hub",
        "nav_label": "Management Hub",
        "section": "Reference",
    },
]


class TestLoadDocSources:
    def test_reads_sources_from_mkdocs(self, tmp_path):
        cfg = {"extra": {"doc_sources": SAMPLE_SOURCES}}
        path = tmp_path / "mkdocs.yml"
        path.write_text(yaml.dump(cfg))
        result = build_nav.load_doc_sources(str(path))
        assert len(result) == 2
        assert result[0]["repo"] == "anax"
        assert result[1]["dest_name"] == "mgmt-hub"

    def test_skips_entries_without_repo(self, tmp_path):
        cfg = {"extra": {"doc_sources": [{"nav_label": "orphan"}, {"repo": "anax"}]}}
        path = tmp_path / "mkdocs.yml"
        path.write_text(yaml.dump(cfg))
        result = build_nav.load_doc_sources(str(path))
        assert len(result) == 1
        assert result[0]["repo"] == "anax"

    def test_empty_when_missing(self, tmp_path):
        path = tmp_path / "mkdocs.yml"
        path.write_text(yaml.dump({"site_name": "x"}))
        assert build_nav.load_doc_sources(str(path)) == []


class TestLoadStaticNav:
    def test_reads_nav(self, tmp_path):
        cfg = {"nav": [{"Home": "index.md"}, {"Quick Start": "quick-start.md"}]}
        path = tmp_path / "mkdocs.yml"
        path.write_text(yaml.dump(cfg))
        assert build_nav.load_static_nav(str(path))[0] == {"Home": "index.md"}

    def test_fallback_home(self, tmp_path):
        path = tmp_path / "mkdocs.yml"
        path.write_text(yaml.dump({"site_name": "x"}))
        assert build_nav.load_static_nav(str(path)) == [{"Home": "index.md"}]


class TestLinkedMdFiles:
    def test_finds_relative_md_links(self):
        text = "See [setup](SETUP.md) and [guide](docs/guide.md) for details."
        assert build_nav._linked_md_files(text) == ["SETUP.md", "docs/guide.md"]

    def test_ignores_http_links(self):
        text = "[external](https://example.com/README.md)"
        assert build_nav._linked_md_files(text) == []

    def test_ignores_absolute_paths(self):
        text = "[abs](/docs/README.md)"
        assert build_nav._linked_md_files(text) == []

    def test_strips_anchors(self):
        text = "[section](CONTRIBUTING.md#setup)"
        assert build_nav._linked_md_files(text) == ["CONTRIBUTING.md"]


class TestLinkedImageFiles:
    def test_finds_markdown_image(self):
        assert "imgs/arch.png" in build_nav._linked_image_files("![diagram](imgs/arch.png)")

    def test_finds_html_img(self):
        assert "imgs/oh.png" in build_nav._linked_image_files('<img src="imgs/oh.png">')

    def test_ignores_http_images(self):
        assert build_nav._linked_image_files("![remote](https://example.com/image.png)") == []


class TestRenameReadmes:
    def test_renames_readme_to_index(self, tmp_path):
        (tmp_path / "README.md").write_text("# hello")
        build_nav._rename_readmes(tmp_path)
        assert (tmp_path / "index.md").exists()
        assert not (tmp_path / "README.md").exists()

    def test_does_not_overwrite_existing_index(self, tmp_path):
        (tmp_path / "index.md").write_text("# existing")
        (tmp_path / "README.md").write_text("# readme")
        build_nav._rename_readmes(tmp_path)
        assert (tmp_path / "index.md").read_text() == "# existing"
        assert (tmp_path / "README.md").exists()


class TestInjectRepoFrontMatter:
    def test_injects_front_matter(self, tmp_path):
        (tmp_path / "index.md").write_text("# Hello\n")
        build_nav._inject_repo_front_matter(
            tmp_path, "anax", "https://github.com/open-horizon/anax", org="open-horizon"
        )
        content = (tmp_path / "index.md").read_text()
        assert content.startswith("---\n")
        assert "repo_url: https://github.com/open-horizon/anax\n" in content
        assert "repo_name: open-horizon/anax\n" in content

    def test_merges_into_existing_front_matter(self, tmp_path):
        (tmp_path / "index.md").write_text("---\ntitle: Existing\n---\n\n# Hello\n")
        (tmp_path / "api.md").write_text("---\ntitle: API\n---\n\n# API\n")
        build_nav._inject_repo_front_matter(
            tmp_path, "anax", "https://github.com/open-horizon/anax",
            org="open-horizon", stars=10, forks=2,
        )
        for name in ("index.md", "api.md"):
            content = (tmp_path / name).read_text()
            assert "title:" in content
            assert "repo_url: https://github.com/open-horizon/anax" in content
            assert "repo_name: open-horizon/anax" in content
            assert "repo_stars: 10" in content


class TestAppendReferenceNav:
    def test_appends_repo_sections(self, tmp_path):
        staged_dir = tmp_path / "anax" / "docs"
        staged_dir.mkdir(parents=True)
        (staged_dir / "index.md").write_text("# Agent\n")
        (staged_dir / "api.md").write_text("# API\n")

        static_nav = [{"Home": "index.md"}]
        staged = [
            (
                {
                    "repo": "anax",
                    "dest_name": "anax",
                    "nav_label": "Agent (anax)",
                    "section": "Reference",
                },
                str(staged_dir),
            )
        ]

        original = build_nav.SECTIONS_DIR
        build_nav.SECTIONS_DIR = str(tmp_path / "reference")
        try:
            nav = build_nav.append_reference_nav(static_nav, staged)
        finally:
            build_nav.SECTIONS_DIR = original

        assert nav[0] == {"Home": "index.md"}
        assert any("Agent (anax)" in item for item in nav if isinstance(item, dict))


class TestJekyllStyleNav:
    def test_builds_tree_from_parent_titles(self, tmp_path, monkeypatch):
        docs = tmp_path / "docs" / "docs"
        docs.mkdir(parents=True)
        (docs / "parent.md").write_text(
            "---\ntitle: Parent Section\nnav_order: 1\nhas_children: true\n---\n# Parent\n"
        )
        (docs / "child.md").write_text(
            "---\ntitle: Child Page\nparent: Parent Section\nnav_order: 1\n---\n# Child\n"
        )
        monkeypatch.setattr(build_nav, "DOCS_CONTENT_ROOT", str(docs))
        # Isolate from repo common-requests / quick-start
        monkeypatch.chdir(tmp_path)
        (tmp_path / "docs").mkdir(exist_ok=True)
        nav = build_nav.build_jekyll_style_nav()
        assert len(nav) >= 1
        top = nav[0]
        assert "Parent Section" in top
        children = top["Parent Section"]
        assert isinstance(children, list)
        titles = []
        for item in children:
            titles.extend(item.keys())
        assert "Child Page" in titles


class TestPreprocessMarkdown:
    def test_substitutes_keywords(self):
        keywords = {"edge_notm": "Open Horizon", "edge_abbr": "OH"}
        text = "Welcome to {{site.data.keyword.edge_notm}} ({{site.data.keyword.edge_abbr}})."
        assert build_nav.preprocess_markdown(text, keywords) == "Welcome to Open Horizon (OH)."

    def test_strips_attribute_lines(self):
        text = "# Title\n{: #title}\n\nBody\n{:codeblock}\n"
        result = build_nav.preprocess_markdown(text, {})
        assert "{:" not in result
        assert "Title" in result
        assert "Body" in result

    def test_strips_inline_attributes(self):
        text = "[Kubernetes](https://k8s.io/){:target=\"_blank\"}{: .externalLink}"
        result = build_nav.preprocess_markdown(text, {})
        assert result == "[Kubernetes](https://k8s.io/)"

    def test_leaves_unknown_keywords(self):
        text = "{{site.data.keyword.unknown_key}}"
        assert build_nav.preprocess_markdown(text, {}) == text

    def test_preprocess_staged_tree(self, tmp_path):
        md = tmp_path / "page.md"
        md.write_text("# {{site.data.keyword.edge_notm}}\n{: #x}\n")
        changed = build_nav.preprocess_staged_tree(tmp_path, {"edge_notm": "Open Horizon"})
        assert changed == 1
        assert md.read_text() == "# Open Horizon\n"


class TestDocsDirExists:
    def test_true_on_200(self):
        with patch("build_nav.requests.get") as mock_get:
            mock_get.return_value = MagicMock(status_code=200)
            assert build_nav.docs_dir_exists("anax") is True

    def test_false_on_404(self):
        with patch("build_nav.requests.get") as mock_get:
            mock_get.return_value = MagicMock(status_code=404)
            assert build_nav.docs_dir_exists("missing") is False


class TestGetRepoMetadata:
    def test_returns_json(self):
        with patch("build_nav.requests.get") as mock_get:
            resp = MagicMock(status_code=200)
            resp.json.return_value = {"name": "anax", "clone_url": "https://x"}
            resp.raise_for_status = MagicMock()
            mock_get.return_value = resp
            assert build_nav.get_repo_metadata("anax")["name"] == "anax"

    def test_returns_none_on_404(self):
        with patch("build_nav.requests.get") as mock_get:
            mock_get.return_value = MagicMock(status_code=404)
            assert build_nav.get_repo_metadata("nope") is None
