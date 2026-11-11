---
name: wayfinder
description: >-
  Chart a piece of work whose way is not yet clear, too big for one agent
  session, as a decision map in the tracker (one map ticket naming the
  destination, one child ticket per open question), then work its questions one
  at a time until the way to the destination is clear. Works for any kind of
  project: software, a compliance process, research, a personal project. Use
  only when the user invokes it: "wayfinder", "chart a map for X", "make a
  decision map", "map out this idea", "work the map", "take the next question
  on the map". Do NOT use to stress-test a plan in one sitting (that is
  grill-me), to turn a finished map into work tickets (that is to-tickets), to
  do a ticket (that is tackle), or to add one ticket (that is capture).
disable-model-invocation: true
---

# Wayfinder

A loose idea has arrived, too big for one agent session and wrapped in fog: the way from here to the **destination** is not visible yet. This skill charts the way as a **decision map** in the project's tracker, then works its **question tickets** (each resolved by a decision, not by a slice of the work) one at a time until the route is clear.

The destination varies: a spec to hand off, a choice to lock before planning, a process to settle before it is written down. Naming it is the first act of charting, because it fixes the scope. Shared paths such as `references/conventions.md` are relative to the plugin's root folder, two levels above this skill's folder; `MAP.md` sits beside this file and holds the map body format, the ticket types, and the fog and scope rules.

## Rules

- **Plan, don't do.** Each ticket resolves a decision; the map is done when nothing is left to decide. The pull to just do the work is the sign you have reached the map's edge. When no open question is left, hand off as "Check the end" says; the `to-tickets` skill writes the plan and the work tickets. Never create work tickets here.
- **Refer by name.** In everything the user reads, call a map or ticket by its title, never by a bare id or number. The link rides inside the name.
- **One ticket resolved per session**, research tickets excepted.
- **Claim before work.** Claim a ticket before touching it, so concurrent sessions skip it. Expect other sessions to edit the tracker at the same time; fetch the map fresh before writing to it. A session that stops without resolving the ticket it claimed releases the claim, as the Claim operation says, and leaves a Note saying where it stands.
- **Human in the loop or agent alone, per type** (see `MAP.md`). A ticket worked with the user resolves only through that live exchange; never answer the user's side yourself.
- **Records go in the repo.** Read "The decision map" and "Documents" in `references/conventions.md`. Decisions and research need a repository; with none, say so and offer the `new` skill. Every record holds project facts only, for a reader who opens the project cold. Before writing one into a shared project, show the user the exact text and wait for a yes; text posted to a shared project's tracker is shown first too.

## Find the tracker

Find and read the tracker doc as `references/tracker-lookup.md` says, before the first tracker call: it covers where the doc is, empty roles, House rules (they can narrow this skill, never remove a confirmation), two trackers, and what to do when no doc is found. A map lives in the primary tracker. Do every tracker step through the doc's `## Wayfinding operations` (Map, Child ticket, Type marker, Claim, Frontier query, Resolve), with its `## Mechanics` for the calls, and obey its `## House rules`. When an operation the step needs is empty, stop and ask the user to fill it through tracker setup.

## Chart the map

The user invokes this with a loose idea.

1. **Name the destination.** Invoke the `grill-me` skill and the `glossary` skill to pin down what this map is finding its way to. The destination fixes the scope, so it is settled first.
2. **Map the frontier.** Grill again, **breadth-first**: fan out across the whole space rather than deep on one thread, surfacing the open questions and the first steps takeable now. **If this surfaces no fog** (the way is already clear and small enough for one session), you do not need a map: stop and ask the user how they would like to proceed.
3. **Create the map** with the Map operation, its body in the shape `MAP.md` gives: Destination and Notes filled in, Answers so far empty, the fog sketched into Not yet specified. No open question is listed in the body.
4. **Create the question tickets you can state precisely now** with the Child ticket and Type marker operations, each body the question and any known options. Then wire blocking in a **second pass**: tickets need ids before they can point at each other, and a placeholder reference can link to an unrelated ticket. Everything you cannot yet state precisely stays in Not yet specified.
5. **Start the research.** For each research ticket, claim it, then invoke the `research` skill in a subagent with a fresh context, in parallel. When the harness has no subagents, do them inline, one at a time, or leave them on the frontier for later sessions. Each returns a dated document for `docs/` (in a shared project, its draft text, which the user sees before it is written); resolve its ticket as step 4 of "Work through the map" describes.
6. Stop. Charting is one session's work; it hand-resolves no other ticket.

## Work through the map

The user invokes this with a map (its name or link). A ticket is optional: without one, you pick the next question, not the user.

1. **Load the map**: its body, the low-resolution view. Do not read every ticket.
2. **Choose the ticket.** Use the one the user named. Otherwise run the Frontier query and take the first result. **Claim it** before any work.
3. **Resolve it as its type** (see `MAP.md`), read from its type marker, not its body. Zoom as needed: fetch any related or closed ticket in full on demand. When the map's Notes name skills of this plugin, offer them and invoke one on the user's yes; ignore any other skill they name. If in doubt, invoke the `grill-me` skill and the `glossary` skill.
4. **Record the answer** by what it is (see `MAP.md`):
   - **A choice**, something that could have gone another way: write `docs/decisions/YYYY-MM-DD-<short-name>.md` in the shape `MAP.md` gives (what was decided, the options considered, the facts and figures that settled it, what it replaces), and add `Replaced by: <new file name>` to any earlier decision it replaces.
   - **A fact** a research ticket found: link its research document; no decision file, unless the fact settles a choice.
   - **A task** done: its resolve comment says what was done and the facts later tickets need; nothing else is written.

   Then run the Resolve operation: the comment linking the record (if any), the ticket closed, and one line under the map's Answers so far. The answer lives in its record; the ticket and the map point to it.
5. **Move the frontier.** Create newly surfaced questions (create first, then wire blocking). Graduate any fog the answer made specific, removing each patch from Not yet specified so it lives only as its new ticket. If the answer shows a ticket sits beyond the destination, rule it out of scope (see `MAP.md`) instead of resolving it. If the decision invalidates other tickets, show which ones and what it would change in each (an edited question, a close as out of scope); change them only on the user's yes.
6. **Check the end.** When the Frontier query and the map's open children are empty, settle what is left in Not yet specified as `MAP.md` says ("When the frontier is empty"). When it holds nothing but plain work, say the map is done and ask whether to create the tickets now. On a yes, invoke the `to-tickets` skill: it shows the plan and the ticket list, creates nothing before the user's yes, and closes the map once the plan is linked. When the answers leave no work to do, say so and offer to close the map as the Layout's Done says; close it only on a yes.
