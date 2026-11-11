# Tracker: Todoist

## Mechanics

- Tool: the connected Todoist tool (Doist's official Todoist MCP server, hosted or as an app connector). A ticket is a task; a project or section is a place. The tool names below are that server's; another Todoist tool names them differently, and tracker setup checks each read operation against the connected tool and corrects these lines in the user's copy.
- Find by name: search tasks with one distinctive keyword (`find-tasks` with `searchText`). Search is phrase matching, not word matching, so a longer query misses a reworded task; when a search comes back empty, list the likely project or section without a search term and compare titles by meaning.
- Fetch: load the task (`fetch-object`, with its children), its comments (`find-comments`), and the description of the project and section it sits in. The title is rarely the whole story. Searches return a section's id, not its name: read the project's sections (`find-sections`), or the project overview, which names them.
- Comment: add a comment on the task (`add-comments`).
- Change status: a task is open or complete. Complete it (`complete-tasks`); reopen it (`uncomplete-tasks`). Completing a recurring task rolls it to its next date and keeps the recurrence.
- Assign: assignees exist only in a shared project (`manage-assignments`, after checking the person collaborates on that project). A personal project has no assignee.
- Create: add a task (`add-tasks`) with its project or section, content, description, labels, priority, and date as Layout's New ticket says. A section id implies its project.
- Edit: change a task's title or description with `update-tasks` (`content`, `description`), sending only the fields that change. A description is replaced whole: to add a line, read it, add the line, and send it all back.
- Link parent and child: a child is a subtask, created with the parent's id or moved under it (`update-tasks` with `parentId`).
- Link blocking: Todoist has no native dependency. Write one line in the blocked task's description, `Blocked by: <task title> (<task link>)`, and remove it when the blocker completes.
- Quirks:
  - Dates: move a date with `reschedule-tasks`, which keeps a recurrence; setting `dueString` through `update-tasks` wipes it. `reschedule-tasks` errors on a task with no date, so a dateless task gets its first date through `update-tasks` `dueString`. Clear a date with `update-tasks` `dueString: "remove"` (a deadline with `deadlineDate: "remove"`).
  - Moving a task: `update-tasks` takes exactly one of `projectId`, `sectionId`, or `parentId` per call. Never send a task's existing place back in an update; it counts as a move.
  - A rejected field fails that whole task's update in the call; re-send the other fields without it. A set duration cannot be cleared through the tool.
  - An empty description is left out of listings: a missing field means no description. A project's description is read with `find-projects` or `fetch-object`, not from the overview.
  - Completing a parent task completes its open subtasks too: never complete a parent or a map while a child is open.
  - A filter query cannot be combined with a project or section id in the same call: put the place into the query itself (`#Project`, `##Project` with its sub-projects, `/Section`).
  - Activity for one task cannot be read; age a task from its creation date and dated comments.
  - Transient errors are common; retry a failed call two or three times before treating it as real.

## Layout

- Where: <the projects (and sections) this doc covers, or "all projects">
- Pickable work: <a Todoist filter query, such as `(today | overdue)`; then any fallback source, saying whether it is a fallback or merged>
- Ranking: <how to order candidates, such as overdue first, then priority p1 to p4, then date>
- Excluded: <what is never offered, such as a section or label that holds ideas rather than work; the map and question labels, or with the fallback markers, titles starting with a wayfinding prefix>
- New ticket: <the project or section a captured task goes to, and the fields it needs (labels, priority, date or none)>
- Start: none; Todoist has no started state
- Note: add a comment on the task
- Done: complete the task; a recurring task rolls forward and keeps its recurrence
- Stopped partway: leave the task open with a comment saying where it stands; move its date only when the user agrees
- Cannot proceed: leave the task open with a comment naming the blocker
- Not worth doing: say so; the user decides whether to complete it or change its date. Never delete it to close it
- Parent and children: subtasks
- Blocking: a `Blocked by:` line in the blocked task's description
- Close the parent: complete the parent task once its last open subtask completes

## House rules

<!-- Example: Never offer anything in a section named Ideation as work. -->

## Wayfinding operations

- Map: a task titled with the destination, with the label `wayfinder-map`, in `<the project or section for maps: a place for committed work, never the Inbox or another capture place>`. The map body is the task's description. Find maps with `find-tasks` filtered on the label `wayfinder-map`. Fallback that creates nothing, where the user does not want the labels made: the title starts with `[map]`, and maps are found by searching `[map]` (`find-tasks` `searchText`, with a limit) and keeping the open tasks whose title starts with it. Tracker setup records which form is in use. Before writing the description, fetch the task again (other sessions edit it too) and send the whole new description through `update-tasks` with no project, section, or parent field.
- Child ticket: a subtask of the map task (`add-tasks` with the map's id as `parentId`), titled with the question, its description holding the question and any options. Questions are never subtasks of each other. Blocking between questions is a `Blocked by: <task title> (<task link>)` line in the blocked question's description, written in a second pass once both tasks exist; Todoist has no native dependency.
- Type marker: exactly one label per question: `wayfinder-research`, `wayfinder-prototype`, `wayfinder-grilling`, or `wayfinder-task`. Create each label once (`add-labels`) before first use; label names are matched exactly. Fallback that creates nothing: the title starts with `[research]`, `[prototype]`, `[grilling]`, or `[task]`.
- Claim: re-fetch the task and skip it if it already carries the claim marker or is assigned to someone else. Then add the label `wayfinder-claimed`, or, in the fallback, put `[claimed]` at the front of the title (`update-tasks` `content`); in a shared project, also assign it to the user (`manage-assignments`). To release a claim when a session stops without resolving the question, remove the marker, and the assignee if the claim set it.
- Frontier query: fetch the map task with its children (`fetch-object` with children); keep the subtasks that are open, carry no `wayfinder-claimed` label and no `[claimed]` title prefix, are assigned to no one or to the user, and whose `Blocked by:` lines name only completed tasks (fetch each named blocker to check). Keep the order the subtasks have in the map.
- Resolve: add a comment on the question task with the answer's gist and a link to its decision file (or research document); remove `wayfinder-claimed` or the `[claimed]` prefix; complete the task (`complete-tasks`); then add the one-line pointer under `## Answers so far` in the map's description. A question ruled out of scope is completed the same way with a comment starting `Out of scope:`, and its line goes under `## Out of scope` instead. Never complete the map task while a question under it is open: completing a parent completes its open subtasks.
