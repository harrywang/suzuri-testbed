---
related: "[[only-in-code]]"
---

# Centre

The note the local graph check starts from. Every link shape the graph counts is here once, followed by the shapes it must ignore.

## Counted

- A plain wikilink: [[outgoing]]
- A wikilink with an alias: [[aliased|a different label]]
- A wikilink to a heading: [[outgoing#Details]]
- An embed: ![[embedded]]
- A markdown link to a note: [the linked note](markdown-linked.md)
- A name two notes share: [[twin]]

## Ignored

- A link to a note that does not exist: [[no-such-note]]
- A web link: [Suzuri](https://suzuri.ai)
- A heading in this note: [Counted](#counted)
- A code span: `[[only-in-code]]`

```markdown
[[only-in-code]]
```
