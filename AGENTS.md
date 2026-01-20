# Open Horizon project documentation

This is the primary AGENTS file for the documentation repository.  There are at least six sub-AGENTS in subdirectories under this directory.  Those indicate files that have been source from other Open Horizon repositories.  The Markdown files in those folders should not be modified in this repository.

## Building the documentation

The documentation is intended to be built in production from this repository using GitHub Actions and GitHub pages using Jekyll, so that the documentation is available at https://open-horizon.github.io/ .  The build process is triggered by a push to the master branch of this repository.  The template is based on the [Just the Docs](https://pmarsceill.github.io/just-the-docs/) theme.

Further, we use GitHub Actions for validating hyperlinks and checking for orphaned pages.

Every time we edit a page, we update the last modified date in the front matter.

All Markdown and HTML files are turned into web pages except for AGENTS.md files.
