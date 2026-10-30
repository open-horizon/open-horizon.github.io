# Conventions used in this document

This document uses content conventions to convey specific meaning.

## Command conventions

Replace the variable content that is shown in < > with values specific to your needs. Do not include < > characters in the command.

### Example

```
hzn key create "<companyname>" "<youremailaddress>"
```

## Literal strings

Content that you see on the management hub or in code is a literal string. This content is shown as **bold** text.

### Example

If you examine the `service.sh` code, you see that it uses these, and other configuration variables to control its behavior. **PUBLISH** controls if the code attempts to send messages to IBM Event Streams. **MOCK** controls if service.sh attempts to contact the REST APIs and its dependent services (cpu and gps) or if `service.sh` creates fake data.

## Heading anchors

Authors put an explicit anchor on a heading when other pages link to it. Use the Material `attr_list` syntax at the end of the heading line:

```
## Install the agent {: #install-agent }

See [Install the agent](installing.md#install-agent).
```

Do not use the Kramdown form from the earlier Jekyll site, which puts the id on the next line:

```
## Install the agent
{: #install-agent}
```

- The Markdown processor only reads the attribute list on the same line as the heading, so the Kramdown form is ignored.
- During the site build, a Kramdown heading id in a source repository is converted into the Material form. Other Kramdown attributes, such as `{:target="_blank"}` and `{: .externalLink}`, are dropped. New content should not rely on this conversion.
- Without an explicit id, MkDocs generates one from the heading text: lowercase, punctuation removed, and runs of spaces collapsed into one hyphen. Kramdown kept the double hyphen in headings such as `### **API:** POST /attribute`, so a link to `#api-post--attribute` breaks. Link to `#api-post-attribute` or add an explicit id.
- An explicit id replaces the generated one. Update links that used the generated id.
- Use lowercase letters, digits, hyphens, and underscores in ids.
