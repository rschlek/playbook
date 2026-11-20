# wayfinder

- Maintainer: the playbook plugin maintainers
- Origin: adapted from Matt Pocock's skills repository
  (https://github.com/mattpocock/skills, `skills/engineering/wayfinder`),
  at commit 4ae2317ddb22b046e26455e4f9c9b3aaaf62212d (main, 2026-10-31),
  MIT licensed, copyright (c) 2026 Matt Pocock. Reworded for any kind
  of work.

Charts a piece of work too big for one agent session as the standard's decision map: one map ticket in the primary tracker naming the destination, one child ticket per open question (research, prototype, grilling, or task), the tracker's own blocking between them, and a Not yet specified section for what cannot be ticketed yet. Sessions then work the map one question at a time until the way is clear, and hand the finished map to `to-tickets`. Started when the user asks for it in plain words or agrees when `guide-me` offers it, never on the agent's own initiative.

## What changed from the original

- Any kind of project, not only software; the examples pair software with non-software work.
- The map follows `references/conventions.md`: the body holds Destination, Notes, Answers so far, Not yet specified, and Out of scope, and never lists open questions.
- A resolved question becomes a decision file in `docs/decisions/`, written under the record-writing rule; the ticket's resolve comment and the map's Answers so far point at it. The original kept the decision in a ticket comment.
- Research output is a dated document under `docs/`, linked from its ticket, instead of a never-merged branch.
- Every tracker step goes through the tracker doc's `## Wayfinding operations` (Map, Child ticket, Type marker, Claim, Frontier query, Resolve); the skill names no tracker product, label syntax, or command line.
- The option to carry execution into the map was dropped: the skill plans only, and when no question is left asks whether to create the tickets now, invoking `to-tickets` on a yes. A decision that invalidates other tickets changes them only on the user's yes, and a skill named in the map's Notes is offered, not invoked unasked.
- Harness-neutral: sibling skills are invoked by name (`grill-me`, `glossary`, `research`, `prototype`, `to-tickets`, `new`, `setup-playbook-profile`), with an inline fallback where a fresh-context subagent is wanted.
- The original is started only by the user typing its name. Here the agent may also start it when the user asks in plain words or agrees to `guide-me`'s offer, never on its own initiative.
- Reference detail (map body, ticket types, fog and scope, decision file shape) moved to `MAP.md` to keep `SKILL.md` near 100 lines.

## Maintainer notes

- The six operation names must match the `## Wayfinding operations` lines in every template under `references/trackers/`.
- The decision file shape in `MAP.md` must agree with `skills/glossary/DECISION-FORMAT.md` and with "Documents" in `references/conventions.md`.
- After the claim, "Work through the map" step 2 names the question in one sentence and asks the first interview question in the same reply. In tests and in real use the hand-over was a wall of bullets about the ticket followed by a second yes to start, and the first question was too dense.
