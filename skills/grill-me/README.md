# grill-me

- Maintainer: the playbook plugin maintainers
- Origin: adapted from the upstream skill of the same name in Matt Pocock's
  skills repository (https://github.com/mattpocock/skills), MIT licensed,
  copyright (c) 2026 Matt Pocock. Reworded for any kind of work.

Interviews the user relentlessly about a plan or design, one question at a
time and each with a recommended answer, walking every branch of the decision
tree until both sides understand the plan the same way. Questions the project
itself can answer (its files, documents, records, or code) are answered by
looking instead of asking.

## Maintainer notes

- The `wayfinder` skill invokes this skill, together with `glossary`,
  for grilling tickets and to name a map's destination. Keep the name.
- The changes from the earlier version are step 5, which looked only at
  code, step 6, which hands a word used two ways to the `glossary` skill,
  and a description that names its siblings.

## Prerequisites

None beyond the agent.
