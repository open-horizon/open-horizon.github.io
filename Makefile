.PHONY: stage serve clean test help dry-run build

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'

PYTHON ?= python3

stage: ## Fetch source-repo docs into docs/docs/<name>/docs/ and write mkdocs_build.yml
	$(PYTHON) scripts/build_nav.py

serve: stage ## Stage docs then start the MkDocs preview server
	mkdocs serve -f mkdocs_build.yml -a 127.0.0.1:8765

build: stage ## Stage docs then build the static site into site/
	mkdocs build -f mkdocs_build.yml

dry-run: ## Show which repositories would be included without cloning
	$(PYTHON) scripts/build_nav.py --dry-run

test: ## Run unit tests
	$(PYTHON) -m pytest tests/ -v

clean: ## Remove staged docs, build output, and generated config
	rm -rf docs/docs/*/docs/ docs/docs/reference/ docs/docs/_clone_*/ docs/_repos/ docs/_sections/ site/ mkdocs_build.yml __pycache__ .pytest_cache
	# Remove empty staged repo parent dirs left after deleting .../docs/
	-find docs/docs -mindepth 1 -maxdepth 1 -type d -empty -delete
