# Tracker: <product name>

<!--
A tracker doc for a tracker that has no template yet. Fill each line with
what an agent needs to operate this tracker with only this file in hand.
Name the tool (the connected <product> tool, or a command line), never a
secret. Leave a Layout or Wayfinding line empty when the step does not exist
in this tracker; an agent skips an empty step and never invents one.
-->

## Mechanics

- Tool: <the connected tool or command line used, and what a ticket and a place are called in this tracker>
- Find by name: <how to search for a ticket by its title, and how the search matches (whole phrase or words)>
- Fetch: <how to load a ticket in full: body, comments, children, relations, and anything left out unless asked for>
- Comment: <how to add a comment or note>
- Change status: <how to change a ticket's status, and what limits which statuses are allowed>
- Assign: <how to assign a ticket to the user, if the tracker has assignees>
- Create: <how to create a ticket, and the fields a create needs>
- Edit: <how to change a ticket's title or body, and whether the body is replaced whole>
- Link parent and child: <how a child is attached to its parent, and how children are listed>
- Link blocking: <the tracker's native blocking link, or the line written in the body when it has none>
- Quirks: <anything that surprises: writes that need confirming, deletion that cannot be undone, fields that wipe others, limits, transient errors>

## Layout

- Where: <the tracker locations this doc covers>
- Pickable work: <the query for tickets that may be offered as work now, in the tracker's own query language; then any later source, saying whether it is a fallback or merged>
- Ranking: <how to order candidates>
- Excluded: <what is never offered, and how to recognise it; with title-prefix wayfinding markers, the tickets whose title starts with one>
- New ticket: <where a captured ticket goes, and the fields it needs>
- Start: <what marks a ticket as started, including assigning it to the user where the tracker has assignees>
- Note: <how a note is left on a ticket>
- Done: <how a finished ticket is closed>
- Stopped partway: <what happens to a ticket left unfinished>
- Cannot proceed: <how a stuck ticket is marked, with its blocker named>
- Not worth doing: <what is proposed for a ticket not worth doing; the user decides>
- Parent and children: <how a ticket holds child tickets>
- Blocking: <how one ticket blocks another>
- Close the parent: <what closes a parent once its last open child closes>

## House rules

<!-- Example: Never offer a ticket that is waiting on someone else. -->

## Wayfinding operations

- Map: <where maps live (a place for committed work, never an inbox), how a map ticket is made (titled with the destination) and recognised (a label, category, type, or title prefix such as `[map]`), where the map body goes (its description or body), how to find open maps, and how to edit the body safely when other sessions may have changed it>
- Child ticket: <how a question ticket is made under the map, titled with the question, its body holding the question and any options; how blocking between questions is wired once both exist. With no native child link, write a `Map: <map title and link>` line at the top of the question's body; with no native blocking link, a `Blocked by: <ticket title and link>` line>
- Type marker: <how exactly one type, research, prototype, grilling, or task, is marked on each question: one label or category per type (`wayfinder-research`, `wayfinder-prototype`, `wayfinder-grilling`, `wayfinder-task`), or a title prefix such as `[research]` where the tracker has neither, and whether each must be created once first>
- Claim: <how a session claims a question before working it, after checking no one else holds it: a `wayfinder-claimed` label, a `[claimed]` title prefix, or a started status, plus assigning it to the user where the tracker has assignees; and how the claim is released when a session stops without resolving it (the marker removed, the status set back, the assignee removed if the claim set it)>
- Frontier query: <the query, in the tracker's own language, for the map's children that are open, carry no claim, are assigned to no one or to the user, and are not blocked by an open ticket, and the order to take them in. With the fallbacks above: search for the `Map:` line, then drop any whose `Blocked by:` lines name an open ticket>
- Resolve: <how an answered question is closed: a comment with the answer's gist linking its decision file (or research document), the closed status, then the one-line pointer added under `## Answers so far` in the map body; and how a question ruled out of scope is closed (a not-planned or dropped status, a comment starting `Out of scope:`) with its line under `## Out of scope` instead>
