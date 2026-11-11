# research

- Maintainer: the playbook plugin maintainers
- Origin: adapted from Matt Pocock's skills repository
  (https://github.com/mattpocock/skills, `skills/engineering/research`),
  at commit 4ae2317ddb22b046e26455e4f9c9b3aaaf62212d (main, 2026-10-31),
  MIT licensed, copyright (c) 2026 Matt Pocock. Reworded for any kind
  of work.

Spins up a background agent with a fresh context (or works inline when the harness has none) that investigates one question against primary sources, writes the findings to one Markdown document with each claim cited, and saves it as a dated document under the project's `docs/` folder, linked from the ticket it serves.

## What changed from the original

- Any kind of project: primary sources include regulations, standards, issuing bodies' guidance, original papers, and vendors' terms, not only docs and code.
- Where the findings go follows `references/conventions.md`: a dated file under `docs/` (the project's research folder, else `docs/research/`), written under the record-writing rule, never edited afterwards. The original saved it wherever the repo kept notes; an earlier version also allowed a store outside the project when there was no repository. Here there is no such fallback: with no repository the skill offers `new`.
- An inline fallback when the harness has no background agents.
- A description with trigger phrases and sibling pointers; the original's was too thin to trigger on.

## Maintainer notes

- The `wayfinder` skill invokes this skill for research tickets, in parallel subagents, and resolves the tickets itself; keep the return (path plus a few lines) short so the caller can do that.

## Prerequisites

A project repository. A background agent facility in the harness is used when present.
