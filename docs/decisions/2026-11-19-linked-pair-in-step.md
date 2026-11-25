# Keeping a linked pair in step is part of the work skills

Question: What does keeping a linked pair in step look like when it is built into the work loop?

Replaced in part by: 2026-11-25-the-tracker-work-is-built-in-two-releases.md. Starting an unassigned project ticket through `tackle` assigns it and adds the linked personal item.

A personal item and the project ticket it links move together through the skills a person already uses. There is no skill for it. The skills compare what the linked items say now with what the project ticket says now, and offer the difference. The walk-through also settled where planning lives when a person has a personal tracker.

## What was decided

1. Where it lives. One shared reference holds the rules, and `guide-me`, `tackle`, `wayfinder`, and `to-tickets` follow it. `capture` does not run it, so that adding one ticket stays quick.
2. Compare states, not moments. For a project ticket that the person's items link: when no linked item is started, leave it; when any linked item is started or finished, it should be started; when every linked item is finished, propose done with a short note. A ticket is never moved backwards.
3. Whose tickets. A write goes only to a project ticket assigned to the person, or to an agent working for the person. In a tracker with no assignees, and in a project whose tickets are not the person's to move, nothing is written: the difference is reported and left.
4. At start. One yes covers the personal item and the project ticket together.
5. At done. Closing the project ticket gets its own yes, with the note shown. The person may edit the note.
6. The check for pairs out of step. It runs by itself, once per session, at the first tracker use by one of those skills, and says nothing when every pair is in step. Inside a project it looks at that project only, and at everything only when asked.
7. A budget. The check reads the linked items in one query and their project tickets in one batch. It never reads items one by one. When it cannot check within a few calls, or the project tracker cannot be reached, it says so and goes on.
8. A plan in the personal tracker carries one link, on its parent. Its steps carry none, unless a step answers a different project ticket. The plan counts as started when its first step starts, and as finished when it is closed. Filing a plan moves nothing.
9. A complete personal list. Every project ticket assigned to the person has a personal item that links it. When one has none, the check offers to add the missing items, on one yes.

## Where planning lives

1. Maps, plans, and their steps are work the project needs, and someone else may do them. They go in the project tracker by default, also for a person who uses a personal tracker.
2. The project tracker's doc is where a project says planning does not go there. Then the map, the plan, and its steps go in the personal tracker, linked to the project ticket they serve.
3. When the project tracker takes no planning and one person does most of the work, the plan stays in the personal tracker. Decisions and research are in the repository either way.

## What it does not cover

- Between a change made with no agent involved and the person's next session, the project ticket is out of date.
- A session on a machine that cannot reach the project tracker cannot check.
- A conversation that uses none of those skills does not check.

## Options considered

- A skill of its own that the work skills hand off to: not taken. It is one more name to remember, and the comparing belongs where the work happens.
- Built in, plus a name to call it by: not taken. `guide-me` already answers where things stand and runs the check.
- Built into the work skills through one shared reference: taken.
- A separate yes for the project ticket at start: not taken. Starting is easy to undo.
- Closing the project ticket with no question: not taken. Other people read it, and the note goes out in the person's name.
- A link on every step of a plan: not taken. Every step added or dropped is another link to keep right.
- The check only when asked: not taken. Its purpose is the times the person forgot.
- A personal item only for the project tickets the person chooses: not taken. The personal tracker is meant to be the person's whole list.
- All planning in the personal tracker once a person has one: not taken. It hides work the project needs from the people who might do it.
- A second copy of the plan in the repository when the project tracker takes no planning: not taken. It is one more thing to keep current.

## What settled it

- A walk-through of three processes, which the person reacted to: doing one ticket with an agent, planning and then filing a plan, and finishing work with no agent involved.
- Comparing states handles the case that reacting to moments missed: one of several linked items started and finished with no agent involved while the others are still open.
- The person's model: the personal tracker answers "what do I need to do today", and the project tracker answers "what is the state of the project, and who is working on what".

## Not settled here

- What catches a pair that drifted while no session was open. A separate question on the map holds it.
- How the rule that lets a linked pair move together reads in the conventions. A separate question holds it.
- Where a project's rule for what goes to its tracker is written, and its form. A separate question holds it.
- How a person later shares planning kept in the personal tracker with the project. A new question holds it.

## Replaces

Nothing.
