# Documentation Publishing Workflow for the exchange-api repository

> **Last Updated:** January 2026

## Overview

This document describes how documentation from the exchange-api repository is automatically published to the Open Horizon website.

## Source Locations

- **docs/** folder → Published to: https://open-horizon.github.io/docs/exchange-api/docs/

## Automation Process

The documentation publishing workflow follows these steps:

1. Changes are pushed to the master branch in the exchange-api repository
2. GitHub Actions trigger automatically:
   - `copydocs.yml` - Copies docs folder content
3. Files are copied to the open-horizon.github.io repository
4. A rebuild is triggered in the open-horizon.github.io repository
5. Updated documentation is published to the website

## GitHub Actions

The following GitHub Actions automate the documentation publishing process:

- [copydocs.yml](../.github/workflows/copydocs.yml)

## Troubleshooting

If documentation updates don't appear on the website:

- Check GitHub Actions status in both repositories (exchange-api and open-horizon.github.io)
- Verify changes were merged to the master branch
- Allow 5-10 minutes for the full publishing pipeline to complete
- Review the GitHub Actions logs for any error messages

## Content and Writing Guidelines

### Formatting Standards

#### Front Matter Updates

**CRITICAL**: When modifying any file with front matter, you MUST:

1. Update the `lastupdated` field to today's date in ISO format (YYYY-MM-DD)
2. Update the `years` field to include the current year if not already present
   - If years is a single year (e.g., `2024`), change to range: `2024 - 2026`
   - If years is already a range (e.g., `2021 - 2024`), update end year: `2021 - 2026`

Example front matter updates:

```yaml
# Before modification
copyright:
  years: 2021 - 2024
lastupdated: "2024-09-27"

# After modification (in 2026)
copyright:
  years: 2021 - 2026
lastupdated: "2026-01-30"
```

#### Copyright Notices
Copyright notices should span from start year through current year and be updated annually in January:

- First year: `Copyright Foo, 2020`
- Second year: `Copyright Foo, 2020 - 2021`