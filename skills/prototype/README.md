# prototype

- Maintainer: the playbook plugin maintainers
- Origin: adapted from Matt Pocock's skills repository
  (https://github.com/mattpocock/skills, `skills/engineering/prototype`),
  at commit 4ae2317ddb22b046e26455e4f9c9b3aaaf62212d (main, 2026-10-31),
  MIT licensed, copyright (c) 2026 Matt Pocock. Reworded for any kind
  of work.

Makes a cheap, rough throwaway that answers one design question: a single-file HTML demo that pushes a state model or process through hard cases (`LOGIC.md`), several radically different screen variants on one page of an app (`UI.md`), or two or three radically different rough drafts of a document, form, schedule, or plan of steps side by side (`DRAFT.md`). Throwaway from day one, trivial to open, no persistence, state surfaced, linked from its ticket, and cleared away once its answer is a decision file.

## What changed from the original

- Any kind of project. A third branch, `DRAFT.md`, covers "how should it read" and "how should the process go" for work that is not a screen or a state model; the original covered that in one sentence.
- Capture follows `references/conventions.md`: what the prototype showed becomes a decision file in `docs/decisions/` under the record-writing rule, the prototype is linked from its ticket, and afterwards it is deleted or kept where the project's layout puts it. The original folded the winner into the real code and kept the prototype on a throwaway branch; there are no throwaway branches here, and the real work is its own work ticket.
- The logic branch keeps its pure module so the rules can be stated exactly in the decision, rather than so it can be lifted into production.

## Maintainer notes

- The `wayfinder` skill invokes this skill for prototype tickets.
- `UI.md` is the one software-only branch; keep its code examples, which are what make it useful.

## Prerequisites

A project repository the prototype can sit in. The UI branch needs the project's own task runner.
