# How a guide-me session goes

Question: How does a guide-me session go: what it looks at, the one sentence it says, and what it does on yes, on skip, and when nothing fits?

Replaced in part by: 2026-11-24-define-is-offered-whenever-the-problem-is-not-written-down.md. `define` is offered whenever new work has no problem definition, not only for a loose want.

`guide-me` looks without changing anything, says in about five lines where the work stands, names the one skill that fits, and asks a yes-or-no question. Version 1.0.3 ships this. Five changes follow from decisions made since.

## What was decided

As released in version 1.0.3:

1. Who starts it. Plain words start it, such as "guide me", "where are we", "what's next", and "I have an idea and don't know where to begin". The agent may start it. A bare "I want to..." does not.
2. Look. It reads the tracker doc, whether there is a project, the open maps and how many of their questions can be taken now, the open plans and their work tickets, and loose work that is ready. One narrow query for each, about five tracker calls in all. It never reads tickets one by one, never hands the look to a subagent, and changes nothing.
3. Point. About five short lines of plain prose: where the work stands, what is open as counts with at most three tickets named by title, and the one skill that fits and why. It never says what it did not check.
4. The ladder. It takes the first row that fits: no tracker doc or profile leads to `setup-playbook-profile`, or to `new` or `adopt` when a project is needed; a loose want leads to `grill-me`; a way that is unclear and too big for one session leads to `wayfinder`, to chart a map; a map with open questions leads to `wayfinder`, to take the next one; a finished map or an agreed plan with no work tickets leads to `to-tickets`; work that is ready leads to `tackle`; nothing open leads to `capture`. A user who says they are lost gets `untangle`, whatever the look found.
5. Offer. One yes-or-no question that names only the skill. Nothing starts before the yes.
6. Skip. It names the next row that fits and asks again. When none fits, it stops.
7. Nothing fits. It says so, says what it found, and asks what the user is trying to get done. It never invents a stage.
8. Picking a ticket, as in "what can we work on today", belongs to `tackle`.

To change, with the work that follows this map:

9. A loose want leads to `define` once that skill exists.
10. A settled problem definition with no map and no plan is a state it recognises. Which skill it offers then is a separate question on the map.
11. The check for linked pairs out of step runs during the look, inside the same small budget, as the decision on keeping a linked pair in step says.
12. A questionnaire that was sent and has no answers is mentioned in one line, and `to-questionnaire` is offered when bringing the answers back is what fits. Finding it is one look at the project's questionnaires folder.
13. After a map question is answered, it says where the map stands and offers the next question in the same session. It suggests a fresh session only when the session has grown long. Version 1.0.3 suggests a fresh session every time. The rule in `wayfinder` of one question for each session changes with it: one question at a time, and the next one is offered, not started.

## Known gaps in version 1.0.3

- A session sometimes opens with a line about what it is checking.
- One test run named six tickets where the limit is three.

## Options considered

- Started only by its name: not taken. A newcomer does not know the name.
- A menu of skills to choose from: not taken. It names one.
- A fresh session after every answered question: not taken. Used on this map, question after question was answered in one session, and it worked.

## What settled it

- Test runs of the build before its release.
- Its use on the map this question belongs to.
- The release of version 1.0.3.

## Not settled here

- What it offers once a problem definition is settled. A separate question on the map holds it.

## Replaces

Nothing.
