# Contributing to Open Horizon Pages

If you would like to contribute, please read the following contents. This document contains a lot of tips and guidelines to help keep things organized. 

We appreciate and recognize all contributors.

# Table of Contents

- [Fork the Repository](#fork-the-repository)
- [Make Necessary Changes](#make-necessary-changes)
- [Test in Local and Push Changes to GitHub](#test-in-local-and-push-changes-to-gitHub)
- [Submit a Pull Request for Review](#submit-a-pull-request-for-review)
- [Clean Up](#clean-up)

# Fork the Repository

Fork this repository by clicking on the fork button on the top of this page. This will create a copy of this repository in your account.

# Make Necessary Changes

To make necessary changes, you need to clone the forked repository to your machine and set up the development environment in local.

## Clone the repository

<img align="right" width="300" src="img/clone.jpg" alt="clone this repository" />

Go to your GitHub account, open the forked repository, click on the Code button and then click the *copy to clipboard* icon.

Open a terminal and run the following git command:

```
git clone "url you just copied"
```

where "url you just copied" (without the quotation marks) is the url to this repository (your fork of this project).

## Create a branch

Change to the repository directory on your computer:

```
cd open-horizon.github.io
```

Now create a branch using the `git checkout` command:

```
git checkout -b <add-your-new-branch-name>
```

For example:

```
git checkout -b add-readme
```

(The name of the branch does not need to have the word add in it, but it's a reasonable thing to include because the purpose of this branch is to add README to this repository.)

## Make necessary changes

Now do whatever you want to contribute to this project and make necessary changes on existing files or add new files. 

# Test in Local and Push Changes to GitHub

Before pushing changes to GitHub, please make sure you build this GitHub Pages site locally to preview and test changes to this site. 

## Prerequisites

This GitHub Pages site is built with Jekyll. Before you can use Jekyll to test a site, you must [install Jekyll](https://jekyllrb.com/docs/installation/).

## Test your changes locally

Change to the repository directory on your computer and execute the following command to run the Jekyll site locally.

NOTE: The first time you run locally, and any time the `Gemfile.lock` file is updated, run `bundle install` before the step below to install or update any required Jekyll modules.

```
bundle install
bundle exec jekyll serve
```

To preview the site, in your web browser, navigate to [http://localhost:4000](http://localhost:4000)

## Commit changes

Once you have a successful testing in local with your changes, you are ready to commit those changes.

If you go to the project directory and execute the command `git status`, you'll see your changes.

Add those changes to the branch you just created using the `git add` command:

```
git add <file> 
```

All commits should be signed off(`-s` flag on `git commit`). To use `-s` option, follow the [guidance](common-requests/contribute.md#how-to-attest) to make sure you configure your git name (user.name) and email address (user.email).

Now commit those changes using the git commit command:

```
git commit -s -m "Add README.md"
```

## Push changes to GitHub

Push your changes using the command `git push`:

```
git push origin <add-your-branch-name>
```

replacing `<add-your-branch-name>` with the name of the branch you created earlier.

# Submit a Pull Request for Review

If you go to your repository on GitHub, you'll see a `Compare & pull request button`. Click on that button.

<img style="float: right;" src="img/compare-and-pull.jpg" alt="create a pull request" />

Now submit the pull request by clicking `Create pull request`.

<img style="float: right;" src="img/submit-pull-request.jpg" alt="submit pull request" />

You will get a notification email once the changes have been merged.

# Clean Up

## Delete the branch

Once your Pull Request has been approved/merged, you are safe to delete the branch created ealier. Change to the repository directory on your computer and execute the following commands to delete the branch:

Delete the local branch:

```
git branch -d <branch-name>
```

Delete remote branch:

```
git push origin :<branch-name>
```

## Syncing a fork

Connect your local repository to the original “upstream” repository by adding it as a remote. Pull in changes from “upstream” often so that you stay up to date so that when you submit your pull request, merge conflicts will be less likely. 

Refer to [Sync a fork of a repository to keep it up-to-date with the upstream repository.](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork)

