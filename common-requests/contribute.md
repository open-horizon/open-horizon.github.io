---
layout: page
title: "Contribute"
description: "Contribution process to help newcomers get started with Open Horizon"
---

Contributions will only be considered when linked to an open issue, aligned with the project goals, and attested to by the Contributor (ex. signing off on a commit, accepting the [Developer Certificate of Origin](https://developercertificate.org/)).

#### Get assigned
To get assigned to an issue, start with an open issue labelled `Good First Issue` in one of the repositories and submit a comment on the issue requesting that it be assigned to you.  

#### Discuss
- To get a quick response, try "at" mentioning a Maintainer or Working Group lead in your comment as mentioned in the following repositories: 
    - [anax](https://github.com/open-horizon/anax) repo - [Agent](https://wiki.lfedge.org/display/OH/Agent+Working+Group) Working Group
    - [exchange-api](https://github.com/open-horizon/exchange-api) repo - [Management Hub](https://wiki.lfedge.org/display/OH/Management+Hub+Working+Group) Working Group
    - [open-horizon.github.io](https://github.com/open-horizon/open-horizon.github.io) repo - [Documentation](https://wiki.lfedge.org/display/OH/Documentation+Working+Group) Working Group
- For a more live interaction, participating in [regular meetings conducted by respective working groups](https://wiki.lfedge.org/display/OH/Community+Membership) is encouraged.
- Join channel #open-horizon in [LF Edge slack work space](https://slack.lfedge.org/). 
  

#### Attest
All commits should be signed off (-s flag on git commit).

The -s option used for both alternatives causes a committer signed-off-by line to be appended to the end of the commit message body.  It certifies that committer has the rights to submit this work under the same license and agrees to our [Developer Certificate of Origin](https://developercertificate.org/). E.g.
`signed-off-by: John Doe johndoe@example.com`

In order to use the -s option, you need to make sure you configure your git name (user.name) and email address (user.email):

{% capture code %}git config --global user.name "John Doe"{% endcapture %}
{% include code_snippet.md code=code language='shell' now='now' %}
{% capture code %}git config --global user.email "johndoe@example.com"{% endcapture %}
{% include code_snippet.md code=code language='shell' now='now' %}

In most cases, git automatically adds the signoff to your commit with the use of `-s` or `--signoff` flag to `git commit`. You must use your real name and a reachable email address (sorry, no pseudonyms or anonymous contributions).

To ensure all your commits are signed, you may choose to add this alias to your global `.gitconfig` :

*~/.gitconfig*

{% capture code %}
[alias]
  amend = commit -s --amend
  cm = commit -s -m
  commit = commit -s
{% endcapture %}

{% include code_snippet.md code=code language='shell' now='now' %}

Or you may configure your IDE, for example, Visual Studio Code to automatically sign-off commits for you:

<img src="../../img/git-signoff-vscode.png" style="width:60%" alt="git-signoff-vscode">

**To check** 
{% capture code %}git config --list{% endcapture %}
{% include code_snippet.md code=code language='shell' now='now' %}