#!/usr/bin/env bash
# Open issues in Open Horizon source repos for the docs migration
# (see open-horizon.github.io issue #729):
#   - replace Jekyll Liquid / Just-the-Docs markers with MkDocs-friendly markdown
#   - adjust docs front matter (keep title/parent/nav_order; drop layout/has_*)
#   - remove CopyDocs GitHub Actions
#   - rewrite docs/AGENTS.md for pull-at-build publishing
#
# Requires: GH_TOKEN (or gh auth) with Issues: Write on each target repo.
# Usage:  GH_TOKEN=ghp_... ./scripts/open-liquid-migration-issues.sh
#
# Prefer editing existing issues over re-running if issues are already open.

set -euo pipefail

if ! command -v gh >/dev/null; then
  echo "gh CLI is required" >&2
  exit 1
fi

if [[ -z "${GH_TOKEN:-${GITHUB_TOKEN:-}}" ]]; then
  echo "Set GH_TOKEN (classic PAT or fine-grained token with Issues: Write)." >&2
  exit 1
fi
export GH_TOKEN="${GH_TOKEN:-$GITHUB_TOKEN}"

PARENT_ISSUE="https://github.com/open-horizon/open-horizon.github.io/issues/729"
SERVICES_REF="https://github.com/open-horizon-services/open-horizon-services.github.io"

create_issue() {
  local repo="$1"
  local title="$2"
  local body_file="$3"
  echo "Creating issue in open-horizon/${repo}…"
  gh issue create \
    --repo "open-horizon/${repo}" \
    --title "${title}" \
    --body-file "${body_file}"
}

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DRAFT_DIR="${SCRIPT_DIR}/issue-drafts"

create_issue anax \
  "Docs: replace Jekyll Liquid keywords with MkDocs-friendly markdown" \
  "${DRAFT_DIR}/anax.md"

create_issue devops \
  "Docs: replace Jekyll Liquid keywords with MkDocs-friendly markdown" \
  "${DRAFT_DIR}/devops.md"

create_issue kubearmor-integration \
  "Docs: remove Jekyll/Just-the-Docs markers; target MkDocs Material" \
  "${DRAFT_DIR}/kubearmor-integration.md"

create_issue FDO-support \
  "Docs: remove Jekyll/Just-the-Docs markers; target MkDocs Material" \
  "${DRAFT_DIR}/FDO-support.md"

create_issue exchange-api \
  "Docs: remove Jekyll/Just-the-Docs markers; target MkDocs Material" \
  "${DRAFT_DIR}/exchange-api.md"

create_issue open-horizon-release \
  "Docs: replace Jekyll Liquid keywords with MkDocs-friendly markdown" \
  "${DRAFT_DIR}/open-horizon-release.md"

echo "Done. Parent tracking issue: ${PARENT_ISSUE}"
echo "Services docs reference site: ${SERVICES_REF}"
