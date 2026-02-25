# Open Horizon Documentation - Agent Guidelines

This is the primary AGENTS file for the Open Horizon documentation repository. This repository contains the documentation site for Open Horizon, built with Jekyll and hosted on GitHub Pages.

## Build/Lint/Test Commands

### Local Development Commands

Use the provided Makefile for all local development tasks:

- **`make init`**: Install and update all Ruby dependencies. Run this once before using other tools each day.
- **`make build`**: Build the Jekyll site locally using `jekyll build`. This generates the static site in the `_site` directory.
- **`make test`**: Run Jekyll's built-in tests using `jekyll doctor` to check for configuration issues.
- **`make dev`**: Complete development workflow - builds, serves, and tests the site (`jekyll build && jekyll serve && jekyll doctor`).
- **`make run`**: Start the local development server with live reload using `jekyll serve`. Access at http://localhost:4000.

### Testing Individual Components

- **Single page validation**: Run `jekyll build` and check the `_site` directory for the specific page
- **Link validation**: GitHub Actions automatically check for broken links monthly
- **Orphan page detection**: Automated workflow identifies pages not linked in navigation
- **Performance testing**: Lighthouse CI runs weekly performance audits
- **Security scanning**: CodeQL security analysis runs on pushes to master

### Prose and Content Quality

The repository uses write-good for prose quality checking:
- **writeGood**: Checks for passive voice, wordy phrases, and common writing issues
- **alex**: Checks for insensitive or inconsiderate language
- **spellchecker**: Validates spelling across documentation

Configuration is in `.github/write-good.yml`.

## Content and Writing Guidelines

### Grammar and Style

- **Voice and tone**: Write in third-person, active voice
- **Avoid compound phrases**: Replace "and/or" and similar compound joining word/phrases with clearer alternatives
- **Replace Latin phrases**: Use plain English instead of Latin abbreviations:
  - "i.e." → "that is"
  - "e.g." → "for example"
  - "etc." → "and so on"
- **Capitalization**: Headlines and titles should only capitalize the first word and proper nouns
- **Sequences**: Use numbered lists for sequential steps, bullet points for non-sequential items
- **Accessibility**: Avoid directional content ("above", "below") and visual cues ("click the blue button")

### Terminology Conventions

- **User references**: When referring to persons or groups who use Open Horizon, use "adopter" instead of "customer" or "user"
- **Jargon**: Identify and replace technical jargon and cultural references with clearer alternatives
- **Proper names**: All proper names and trademarks should be inserted via variables for consistency

### Formatting Standards

#### External Links
Mark up all external links with target and externalLink class:
```markdown
[Kubernetes debugging](https://kubernetes.io/){:target="_blank"}{: .externalLink}
```
Leave a space in the linked text after the last character so the external link glyph doesn't butt against the hyperlink.

#### Code Blocks
End all code blocks with `{: codeblock}` on a new line at the same indent level:
```bash
make build
{: codeblock}
```

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

### Information Architecture

- **Personas**: Content should be created with specific user personas in mind (app developer, model developer, admin, DevSecNetOps, architect)
- **User journeys**: Structure content around identified user journey paths
- **Navigation**: Use breadcrumbs for section identification and navigation
- **Page titles**: Titles should accurately reflect page content
- **SEO**: Use og-meta tags for social media sharing, SEO optimization, and machine-readability
- **Responsive design**: Ensure content works across devices with proper responsive web design principles

### Content Re-usability

- **Variables**: Use variables for proper names, trademarks, and repeated content
- **Conditional rendering**: Surround environment- and feature-specific sections with conditional rendering tags
- **Includes**: Headers, footers, and navigation should be included at page generation, not embedded directly

### Performance and Optimization

- **Image optimization**: All images should be optimized for web (72 dpi) with proper compression
- **Asset minification**: All text-based markup (JS, CSS, SVG) should be minified for production
- **Caching**: Leverage browser caching for static assets
- **Lazy loading**: Implement lazy loading for images and non-critical content

## Code Style Guidelines

### Markdown and Content Structure

#### Front Matter Requirements

All Markdown files must include proper Jekyll front matter:

```yaml
---
copyright:
  years: 2021 - 2024
lastupdated: "2024-09-27"
layout: page
title: "Page Title"
description: "Brief description for SEO and navigation"
nav_order: 2
has_children: true  # if this page has child pages
has_toc: false     # enable/disable table of contents
---
```

- **copyright.years**: Must be updated annually to reflect current year
- **lastupdated**: ISO date format (YYYY-MM-DD) - update when modifying content
- **title**: Use sentence case, quoted
- **description**: Keep under 160 characters for SEO
- **nav_order**: Numeric ordering for navigation (lower numbers appear first)

#### Content Organization

- Use H2 (`##`) and H3 (`###`) headers for main sections
- Avoid H1 headers (reserved for page title from front matter)
- Include table of contents for pages with multiple sections (`has_toc: true`)
- Use numbered lists for sequential steps, bullet points for non-sequential items

#### Code Examples

- Use fenced code blocks with language specification:
  ```bash
  # Correct
  ```bash
  make build
  ```

  ```javascript
  // Incorrect - missing language
  make build
  ```
- Enable syntax highlighting for all code blocks
- Include comments in code examples for clarity
- Use `$` prefix for command examples to indicate shell prompts

#### Links and References

- Use relative links within the documentation: `[link text](relative/path)`
- Use absolute URLs for external references: `[Open Horizon](https://github.com/open-horizon)`
- Reference files with proper extensions: `file.md`, `image.png`
- Cross-reference other documentation pages using Jekyll collections

### Jekyll Configuration

#### Site Structure

- **Root pages**: Place in repository root (e.g., `quick-start.md`)
- **Documentation pages**: Place in `_docs/` directory
- **Includes**: Custom components in `_includes/`
- **Layouts**: Page templates in `_layouts/`
- **Assets**: CSS in `css/`, JavaScript in `js/`, images in `img/`

#### Theme and Styling

- **Theme**: Just the Docs (configured in `_config.yml`)
- **Custom styling**: Add to `css/style.scss` or `css/colorscheme.scss`
- **Color scheme**: Uses `open-horizon-theme` defined in theme configuration
- **Mermaid diagrams**: Enabled for architecture and flow diagrams
- **Syntax highlighting**: Kramdown with Rouge, line numbers disabled

#### Configuration Conventions

- **HTML compression**: Enabled for production builds
- **Search**: Enabled with custom tokenization for hyphenated terms
- **Analytics**: Google Analytics configured (GDPR compliant)
- **SEO**: Jekyll SEO tag plugin enabled

### CSS/SCSS Guidelines

#### File Organization

- **style.scss**: Main stylesheet importing Jekyll theme
- **colorscheme.scss**: Custom color variables and overrides
- **Individual styles**: Component-specific styles in separate files

#### Naming Conventions

- Use BEM methodology: `block__element--modifier`
- CSS variables for theme colors: `--header-color`, `--accent-color`
- Class names: kebab-case (e.g., `.site-header`, `.nav-link`)

#### Best Practices

- Minimize custom CSS - prefer theme defaults
- Use theme variables for colors and spacing
- Ensure responsive design with mobile-first approach
- Test styles across different browsers

### JavaScript Guidelines

#### File Organization

- **js/**: Directory for all JavaScript files
- **Vendor scripts**: Third-party libraries (e.g., `lunr.min.js`, `reveal.min.js`)
- **Custom scripts**: Site-specific functionality (e.g., `search.js`, `clean-blog.js`)

#### Code Style

- Use modern ES6+ syntax where supported
- Include JSDoc comments for functions
- Minify production assets
- Ensure cross-browser compatibility

### Image and Asset Guidelines

#### File Naming

- **Logos**: `open-horizon.png`, `open-horizon-color.png`, `open-horizon-white.svg`
- **Screenshots**: Descriptive names with hyphens: `git-signoff-vscode.png`
- **Icons**: Semantic names: `launch-glyph.svg`, `favicon.png`

#### Optimization

- Use appropriate formats: SVG for logos/icons, PNG/JPG for photos
- Compress images for web delivery
- Provide multiple sizes for responsive images
- Include alt text for accessibility

### Git and Contribution Guidelines

#### Commit Standards

- **Signed commits**: All commits must use `git commit -s` (signed-off)
- **Commit messages**: Descriptive but concise, focus on "what" and "why"
- **Atomic commits**: One logical change per commit
- **Branch naming**: `issue-###`

#### Pull Request Process

- Always open an issue before beginning to contribute. No bare PRs, please.
- Try to use the appropriate issue template. If unsure, just ask in the chat room.
- Make issues as atomic as possible. Do not put unrelated bugs into a single issue.
- Create PRs from feature branches to `master`
- Include description of changes and testing performed
- Ensure all CI checks pass before merging
- Update front matter `lastupdated` dates on content changes
- Follow the standard process:
  - Fork the repo
  - Create a local branch with the issue in the format `issue-###`
  - Commit often, each time with the `-s` or `--sign-off` flag
  - Test your committed code before creating a PR. If unsure how to test, ask in the chat room.
  - Create the PR by prefixing the title with `Issue: ## - <title of PR less than 72 characters>`
  - Label the PR with the same labels as the issue
  - "@" mention one or more Maintainers in a PR comment, and assign it to them if you can.
  - Link the PR to the issue.
  - Be prepared to answer any questions and make any changes.

### Documentation Source Management

#### Multi-Repository Sources
Some of the documentation content in this repository is copied from other Open Horizon repositories by using automated workflows. The following directory listing shows the directories that receive content in this way, and the other Open Horizon repositories from which the content is copied:

docs/
├── anax/
│   ├─ docs/                  # Copied from `open-horizon/anax`
├── mgmt-hub/
│   ├─ docs/                  # Copied from `open-horizon/devops`
├── kubearmor-integration/
│   ├─ docs/                  # Copied from `open-horizon/kubearmor-integration`
├── fdo/
│   ├─ docs/                  # Copied from `open-horizon/FDO-support`
├── exchange-api/
│   ├─ docs/                  # Copied from `open-horizon/exchange-api`
├── release/
│   ├─ docs/                  # Copied from `open-horizon/open-horizon-release`

**Important**: Never modify markdown files in the directories in this repository that receive content from other Open Horizon repositories. Make changes only in the repositories from which the content is copied.  This will ensure that the content is kept in sync with the source repositories.  Instead, to make changes to the content in this repository, you must make the changes in the source repositories, and then wait for the automated workflows to copy the changes to this repository.

#### File Exclusion

The following files are excluded from Jekyll builds (defined in `_config.yml`):
- Development files: `Gemfile*`, `Makefile`, `README.md`
- Maintenance files: `MAINTAINERS.md`, `LICENSE`, `AGENTS.md`
- Build artifacts: `vendor/`, `node_modules/`, `.sass-cache/`

### Testing and Validation

#### Automated Checks

- **GitHub Actions**: Run on push to master and scheduled intervals
- **Link checking**: Monthly validation of all hyperlinks
- **Orphan detection**: Identifies unlinked documentation pages
- **Performance**: Weekly Lighthouse audits
- **Security**: CodeQL analysis for vulnerabilities

#### Manual Testing

- **Local build**: Always test with `make dev` before committing
- **Cross-browser**: Test in Chrome, Firefox, Safari, Edge
- **Mobile responsive**: Verify layout on mobile devices
- **Accessibility**: Check with screen readers and keyboard navigation

### Performance Optimization

#### Build Optimization

- **HTML compression**: Enabled in production builds
- **Asset minification**: CSS and JavaScript are minified
- **Image optimization**: Use appropriate formats and compression
- **Caching**: Leverage browser caching for static assets

#### Content Optimization

- **Lazy loading**: Images and non-critical content
- **Minimal JavaScript**: Only load necessary scripts
- **Efficient CSS**: Minimize unused styles
- **Fast search**: Lunr.js provides client-side search

This guidelines document should be updated whenever new tools, workflows, or conventions are introduced to the repository.
