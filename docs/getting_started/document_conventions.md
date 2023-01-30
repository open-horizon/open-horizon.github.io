---

copyright:
years: 2020 - 2022
lastupdated: "2022-06-14"
title: "Conventions used in this document"

parent: Release notes
nav_order: 3
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Conventions used in this document

{: #document_conventions}

This document uses content conventions to convey specific meaning.

## Command conventions

Replace the variable content that is shown in < > with values specific to your needs. Do not include  < > characters in the command.

### Example

  ```bash
  hzn key create "<companyname>" "<youremailaddress>"
  ```
  {: codeblock}

## Literal strings

Content that you see on the management hub or in code is a literal string. This content is shown as **bold** text.

### Example

If you examine the `service.sh` code, you see that it uses these, and other configuration variables to control its behavior. **PUBLISH** controls if the code attempts to send messages to IBM Event Streams. **MOCK** controls if service.sh attempts to contact the REST APIs and its dependent services (cpu and gps) or if `service.sh` creates fake data.
