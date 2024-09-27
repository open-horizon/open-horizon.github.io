<p style="text-align:center;" align="center">
  <img align="center" src="https://github.com/open-horizon/open-horizon.github.io/blob/master/img/logos/open-horizon-color.png" width="45%"/>
</p>

<p align="center">
<a href="https://github.com/open-horizon/open-horizon.github.io" alt="GitHub contributors">
<img src="https://img.shields.io/github/contributors/open-horizon/open-horizon.github.io.svg"/></a>
<a href="https://github.com/open-horizon/open-horizon.github.io" alt="Check_broken_link.yml">
<img src="https://github.com/open-horizon/open-horizon.github.io/actions/workflows/Check_broken_link.yml/badge.svg"/></a>
<a href="https://github.com/open-horizon/open-horizon.github.io" alt="Twitter Follow">
<img src="https://github.com/open-horizon/open-horizon.github.io/actions/workflows/orphan_pages_checker.yml/badge.svg"/></a>
<a href="https://matrix.to/#/#open-horizon-docs:chat.lfx.linuxfoundation.org" alt="chat on matrix">
<img src="https://matrix.to/img/matrix-badge.svg"/></a>
</p>

# Contributing to Open Horizon pages

To visit the Open Horizon documentation site, go to [open-horizon.github.io](https://open-horizon.github.io/)

If you would like to contribute to the project, read the following documentation for helpful information and guidelines.

## How to contribute to Open Horizon

All content, artwork, and code is contained in GitHub repositories.  To see what assistance we need, look for open GitHub issues that have not been assigned to someone already.  If you see one that you would like to work on, please add a comment to that issue and try to `@mention` the person who opened the issue to let them know of your interest.  Do not begin working on an issue unless and until it has been assigned to you.  Likewise, do not submit a Pull Request (code fix or submission) unless it is tied to an existing open issue.

More details can be found on the following pages:

* [Contribution Guidelines](https://github.com/open-horizon/.github/blob/master/CONTRIBUTING.md)
* [The mechanics of working on an issue](https://open-horizon.github.io/common-requests/contribute/)
* [Chat with the project team and ask any questions](https://chat.lfx.linuxfoundation.org/#/welcome)
* [List all unassigned and open issues labelled "Good First Issue"](https://github.com/search?type=issues&q=org%3Aopen-horizon+org%3Aopen-horizon-services+label%3A%22good+first+issue%22+is%3Aopen+no%3Aassignee)

We appreciate and recognize all Contributors.

# Table of Contents

- [Contributing to Open Horizon Pages](#contributing-to-open-horizon-pages)
- [Table of Contents](#table-of-contents)
- [Fork the Repository](#fork-the-repository)
- [Make Necessary Changes](#make-necessary-changes)
  - [Clone the repository](#clone-the-repository)
  - [Create a branch](#create-a-branch)
  - [Make necessary changes](#make-necessary-changes-1)
  - [Identifying Documentation Source](#identifying-documentation-source)
- [Test in Local and Push Changes to GitHub](#test-in-local-and-push-changes-to-github)
  - [Prerequisites](#prerequisites)
  - [Test your changes locally](#test-your-changes-locally)
  - [Commit changes](#commit-changes)
  - [Push changes to GitHub](#push-changes-to-github)
  - [Possible errors](#possible-errors)
- [Submit a Pull Request for Review](#submit-a-pull-request-for-review)
- [Clean Up](#clean-up)
  - [Delete the branch](#delete-the-branch)
  - [Syncing a fork](#syncing-a-fork)

# Fork the Repository

Fork this repository by clicking on the fork button on the top of this page. This will create a copy of this repository in your account.

# Make Necessary Changes

To make changes, clone the forked repository to your machine.

## Clone the repository

<img align="right" width="300" src="img/clone.jpg" alt="clone this repository"/>

Go to your GitHub account, open the forked repository, click **Code**, and then **copy to clipboard**.

Open a terminal and run the following git command:

```bash
git clone "url you just copied"
```

where "url you just copied" (without the quotation marks) is the url to this repository (your fork of this project).

## Create a branch

Change to the repository directory on your computer:

```bash
cd open-horizon.github.io
```

Now create a branch using the `git checkout` command:

```bash
git checkout -b <name-your-new-branch-name-after-your-issue>
```

For example:

```bash
git checkout -b issue-329
```

## Make necessary changes

Now, you can suggest contributions, make necessary changes to existing files, or add new files.

## Identifying Documentation Source

Some markdown pages under [open-horizon.github.io/docs](https://github.com/open-horizon/open-horizon.github.io/tree/master/docs) can have their source markdown in other repositories in the Open Horizon GitHub organization.

Use the URL path to identify if the source is [open-horizon.github.io/docs](https://github.com/open-horizon/open-horizon.github.io/tree/master/docs) or another repository. If the source is in different repository then sourced repo name is used `open-horizon.github.io/docs/<SOURCE_REPO_NAME>/docs`.

- [`/docs/anax/docs/`](https://github.com/open-horizon/open-horizon.github.io/tree/master/docs/anax/docs) markdown pages are sourced from https://github.com/open-horizon/anax/tree/master/docs/
- [`/docs/mgmt-hub/docs/`](https://github.com/open-horizon/open-horizon.github.io/tree/master/docs/mgmt-hub/docs/) markdown pages are sourced from https://github.com/open-horizon/devops/blob/master/docs/
- [`/docs/kubearmor-integration/docs/`](https://github.com/open-horizon/open-horizon.github.io/tree/master/docs/kubearmor-integration/docs/) markdown pages are sourced from https://github.com/open-horizon/kubearmor-integration/tree/main/docs/

It is important that any changes to docs sourced from another repository be made in the corresponding repository and not in the `open-horizon.github.io` repository.

CopyDocs GitHub Actions, in each of the respective repos, will trigger on a PR merge and the source markdown files will be copied.

# Test in local and push changes to GitHub

Before you push changes to GitHub, build this GitHub pages site locally to preview and test the changes.

## Prerequisites

This GitHub Pages site is built with Jekyll. Before you can use Jekyll to test a site, you must [install Jekyll](https://jekyllrb.com/docs/installation/).

## Test your changes locally

> NOTE: Ruby 3.2.0 is [incompatible at the moment](https://www.miskatonic.org/2023/01/02/ruby-jekyll/).  Recommend using `rbenv` and installing and using `rbenv local 3.1.1` as a workaround.  On MacOS, `brew install rbenv` then `rbenv install 3.1.1` first.

Change to the repository directory on your computer and execute the following command to run the Jekyll site locally.

1. To install and update all dependencies.

   ```bash
   make init
   ```

   **Note**: Run the above command one time before using the tools each day.

2. Start the local web server, do not build the site first

   ```bash
   make run
   ```

   **Note**: This runs a local web server with live reload enabled. When running the make command on Windows, an error might occur that identifies the installed command as unrecognized. This can happen when the binary path is set incorrectly.

   To preview the site in your web browser navigate to [http://localhost:4000](http://localhost:4000).

3. To build and test the local documentation site:

   ```bash
   make dev
   ```

4. To Build the local documentation site:

   ```bash
   make build
   ```

5. Test the local documentation site locally:

   ```bash
   make test
   ```

   **Note**: This is typically done before `make run`

## Commit changes

After you have a successful testing in local with your changes, you are ready to commit those changes.

If you go to the project directory and execute the command `git status`, you'll see your changes.

Add those changes to the branch you just created using the `git add` command:

```bash
git add <file>
```

All commits should be signed off (`-s` flag on `git commit`). To use the `-s` option, follow the [guidance](common-requests/contribute.md#how-to-attest) to make sure you configure your git name (user.name) and email address (user.email).

Now commit those changes using the git commit command:

```bash
git commit -s -m "Add README.md"
```

## Push changes to GitHub

Push your changes using the command `git push`:

```bash
git push origin <add-your-branch-name>
```

replacing `<add-your-branch-name>` with the name of the branch you created earlier.

## Possible Errors

When setting up a project locally, some errors can occur. Some of those are listed below.

- Missing `webrick` and `wdm` in `Gemfile`

Change to:

Some users use the latest version of `ruby`, which is `>2.7` that does not have pre-added `webrick` support. If they are using `ruby` versions `>= 3.0.0`, they might see the error listed below.

```text
  Add the following to your Gemfile to avoid polling for changes:
    gem 'wdm', '>= 0.1.0' if Gem.win_platform?
 Auto-regeneration: enabled for 'C:/Users/yourUserName/Desktop/open-horizon/open-horizon.github.io'
C:/Ruby30-x64/lib/ruby/gems/3.0.0/gems/jekyll-3.9.0/lib/jekyll/commands/serve/servlet.rb:3:in `require': cannot load such file -- webrick (LoadError)
        from C:/Ruby30-x64/lib/ruby/gems/3.0.0/gems/jekyll-3.9.0/lib/jekyll/commands/serve/servlet.rb:3:in `<top (required)>'
        from C:/Ruby30-x64/lib/ruby/gems/3.0.0/gems/jekyll-3.9.0/lib/jekyll/commands/serve.rb:184:in `require_relative'
        from C:/Ruby30-x64/lib/ruby/gems/3.0.0/gems/jekyll-3.9.0/lib/jekyll/commands/serve.rb:184:in `setup'
        from C:/Ruby30-x64/lib/ruby/gems/3.0.0/gems/jekyll-3.9.0/lib/jekyll/commands/serve.rb:102:in `process'
        from C:/Ruby30-x64/lib/ruby/gems/3.0.0/gems/jekyll-3.9.0/lib/jekyll/commands/serve.rb:93:in `block in start'
        from C:/Ruby30-x64/lib/ruby/gems/3.0.0/gems/jekyll-3.9.0/lib/jekyll/commands/serve.rb:93:in `each'
        from C:/Ruby30-x64/lib/ruby/gems/3.0.0/gems/jekyll-3.9.0/lib/jekyll/commands/serve.rb:93:in `start'
        from C:/Ruby30-x64/lib/ruby/gems/3.0.0/gems/jekyll-3.9.0/lib/jekyll/commands/serve.rb:75:in `block (2 levels) in init_with_program'
        from C:/Ruby30-x64/lib/ruby/gems/3.0.0/gems/mercenary-0.3.6/lib/mercenary/command.rb:220:in `block in execute'
        from C:/Ruby30-x64/lib/ruby/gems/3.0.0/gems/mercenary-0.3.6/lib/mercenary/command.rb:220:in `each'
        from C:/Ruby30-x64/lib/ruby/gems/3.0.0/gems/mercenary-0.3.6/lib/mercenary/command.rb:220:in `execute'
        from C:/Ruby30-x64/lib/ruby/gems/3.0.0/gems/mercenary-0.3.6/lib/mercenary/program.rb:42:in `go'
        from C:/Ruby30-x64/lib/ruby/gems/3.0.0/gems/mercenary-0.3.6/lib/mercenary.rb:19:in `program'
        from C:/Ruby30-x64/lib/ruby/gems/3.0.0/gems/jekyll-3.9.0/exe/jekyll:15:in `<top (required)>'
        from C:/Ruby30-x64/bin/jekyll:25:in `load'
        from C:/Ruby30-x64/bin/jekyll:25:in `<main>'
```

To solve this error, add `webrick` and `wdm` to your local `Gemfile` by using the commands listed below and re-run the serve.

add webrick:

```bash
bundle add webrick
```

add wdm:

```bash
gem install wdm
```

# Submit a Pull Request for Review

If you go to your repository on GitHub, you'll see a `Compare & pull request button`. Click on that button.

<img style="float: right;" src="img/compare-and-pull.jpg" alt="create a pull request"/>

Now submit the pull request by clicking `Create pull request`.

<img style="float: right;" src="img/submit-pull-request.jpg" alt="submit pull request"/>

You will get a notification email after the changes have been merged.

# Clean Up

## Delete the branch

After your Pull Request has been approved/merged, you are safe to delete the branch created earlier. Change to the repository directory on your computer and execute the following commands to delete the branch:

Delete the local branch:

```bash
git branch -d <branch-name>
```

Delete remote branch:

```bash
git push origin :<branch-name>
```

## Syncing a fork

Connect your local repository to the original, upstream repository by adding it as a remote. You should pull in changes from upstream often, so that you stay up-to-date. This helps avoid merge conflicts when you submit pull requests.

For more information, see [Sync a fork of a repository to keep it up-to-date with the upstream repository.](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)

## 📌 Our valuable contributors👩‍💻👨‍💻

<table>
  <tr>
    <a href="https://github.com/open-horizon/open-horizon.github.io/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=open-horizon/open-horizon.github.io" />
    </a>
  </tr>
</table>
