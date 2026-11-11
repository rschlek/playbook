# glossary

- Maintainer: the playbook plugin maintainers
- Origin: adapted from the `domain-modeling` skill in Matt Pocock's skills repository
  (https://github.com/mattpocock/skills, `skills/engineering/domain-modeling`),
  at commit 4ae2317ddb22b046e26455e4f9c9b3aaaf62212d (main, 2026-10-31),
  MIT licensed, copyright (c) 2026 Matt Pocock. Renamed `glossary` in
  playbook 1.0.0 and reworded for any kind of work.

Keeps the project's glossary while the work is designed: pins down the project's words in `docs/glossary.md`, challenges terms against it, sharpens fuzzy language, stress-tests relationships with concrete scenarios, cross-checks claims against the project (its code, procedures, forms, or records), updates `docs/glossary.md` the moment a term is resolved (`GLOSSARY-FORMAT.md`), and offers a decision record only for hard-to-reverse, surprising, real trade-offs (`DECISION-FORMAT.md`).

## What changed from the original

- Named for what it leaves behind, the glossary, rather than for the discipline.
- Any kind of project: the project's own vocabulary, not only code terms; examples pair software with non-software work.
- Where things go follows `references/conventions.md`: the glossary is `docs/glossary.md` (a multi-context project keeps a map there and one file per context under `docs/glossary/`), and decisions are dated files in `docs/decisions/`, one per decision, in the conventions' shape, with a `Replaced by:` line instead of a status field. The original kept the glossary at the repository root and numbered decision records in their own folder.
- Decision records follow the record-writing rule: project facts only, and in a shared project the user sees the exact text first.
- A project that already keeps its glossary or decisions elsewhere keeps them there until the user converts it.

## Maintainer notes

- `DECISION-FORMAT.md` must agree with "Documents" in `references/conventions.md` and with the decision file shape in `skills/wayfinder/MAP.md`.
- The `wayfinder` skill invokes this skill, with `grill-me`, for grilling tickets, and `grill-me` invokes it when a word turns out to be used two ways.

## Prerequisites

A project repository to hold `docs/glossary.md` and `docs/decisions/`. Nothing else beyond the agent.
