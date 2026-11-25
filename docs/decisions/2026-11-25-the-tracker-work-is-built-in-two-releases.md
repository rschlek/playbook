# The tracker work is built in two releases

Question: How is the work on project and personal trackers released, and what is left out of it?

It ships in two releases: first one tracker doc for a team, then the personal tracker. The standard version moves at each. The defaults taken while planning are listed here so the plan rests on a record.

## What was decided

1. Release 1: a team keeps its tracker doc once, in one shared project, and other projects point at it in one line, which `new` and `adopt` write. `to-tickets` marks a ticket unattended only when its `Check:` line names a check a machine can run.
2. Release 2: a person may keep a personal tracker over the project tracker. Each project tracker's doc says what goes on it, and the work skills place, pick, and keep linked pairs in step.
3. The standard version moves at each release. Adopted repositories are synced once, after release 2.
4. Defaults taken while planning:
   - A link to a ticket in a markdown project tracker is its file's web address on the code host, else the repository name and file path.
   - A team that does not use playbook has its tracker doc beside the profile, named for the tracker entry, not its kind.
   - The duplicate check in `capture` and `to-tickets` searches only the tracker the new ticket goes to.
   - A project's personal items are those in its place in the personal tracker, plus any linked to its tickets.
   - `guide-me` adds only one search of the personal tracker and one batch read per part of the project tracker. It reports pairs out of step and offers `tackle`, which applies the difference.
   - Starting an unassigned project ticket through `tackle` assigns it and adds the linked personal item, under one yes.
   - The link labels rest on a dated research note. The check that a checkout is behind its remote may fetch, and changes no working file.
   - The base block's tracker sentence changes at most once, in release 2. Skill text says "tracker doc", never "recipe".
   - "Outcome" means a result someone outside the work would notice is finished; a step is tracked only by the person doing it.
5. Left out: the questionnaire skill, not built; offering the next map question in the same session, a `wayfinder` change this work does not need; a pointer from the old skill name `next`, since the rename shipped without one; how a person schedules the check, which is their own setup; telling one session's claim from another of the same person, which has its own ticket.

## Options considered

- One release: not taken. Everything untried would land at once.
- Two releases, the team's shared doc first: taken.

## What settled it

- The aim to offer playbook to a team soon, in a form friendly to people who are not technical.

## Not settled here

- The version numbers, set at each release.

## Replaces

In part: 2026-11-24-a-linked-pair-is-two-tickets-kept-in-step.md (point 6), 2026-11-24-picking-starts-from-the-personal-list.md (point 4 and the `capture` row of its table), 2026-11-22-a-project-points-at-the-project-that-holds-its-tracker-doc.md (points 4 and 6), 2026-11-19-linked-pair-in-step.md (point 3), and 2026-11-20-how-a-guide-me-session-goes.md (point 2).
