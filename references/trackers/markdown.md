# Tracker: Markdown files in the repository

## Mechanics

- Tool: the agent's own file tools, in the project's repository. A ticket is one Markdown file in `docs/tickets/`; the folder is the tracker. Ticket files are the tracker, not documents, so they carry a status.
  - File name: `docs/tickets/<id>-<short-name>.md`. The id is a whole number, one more than the highest id in the folder; the short name is lowercase with hyphens. A ticket file is never renamed, moved, or deleted.
  - File shape: the title, then the header lines directly under it, one per line and in this order, leaving out any that is empty; then the body; then the log of dated notes.

    ```markdown
    # <title>

    Status: open
    Type: <a kind of ticket, when Layout or a map uses one>
    Assignee: <the person working it>
    Parent: <the parent ticket's id>
    Blocked by: <ids of blocking tickets, comma separated>
    Due: <YYYY-MM-DD, only when something must happen by then>
    Created: YYYY-MM-DD

    <what the ticket asks; for a parent, the plan; for a map, the map body>

    ## Log

    - YYYY-MM-DD: <note>
    ```

  - Statuses: `open`, `started`, `paused`, `waiting`, `done`, `dropped`. A ticket is closed when it is `done` or `dropped`.
  - Queries: there is no query language. Read the header lines of every file in `docs/tickets/` and filter on them. A ticket is blocked while any id in its `Blocked by` line names a ticket that is not closed.
- Find by name: list `docs/tickets/` and match file names and titles by meaning; search the files' text for one distinctive word when that is not enough.
- Fetch: read the whole file, the files its `Parent` and `Blocked by` lines name, and its children (the files whose `Parent` line names its id).
- Comment: add a dated bullet under `## Log`, adding the heading when it is missing. (A map's body has its own `## Notes` section; the log is separate.)
- Change status: edit the `Status` line.
- Assign: set the `Assignee` line to the user's own handle: the one the user gives, else the git user name (`git config user.name`). Never the project's `owner` unless that is the user.
- Create: write a new file with the next id, `Status: open`, and `Created` set to today.
- Edit: change the title line or the body text in the file; leave the header lines to the operations that own them.
- Link parent and child: a `Parent` line in the child.
- Link blocking: add the blocker's id to the blocked ticket's `Blocked by` line.
- Quirks:
  - A ticket change is a file change: commit it by path, with the work it belongs to or on its own with a message naming the ticket. In a repo other people use, it goes through review like any change.
  - Two branches can take the same id. Before committing a new ticket on a branch, check the main branch for that id and take the next free one.

## Layout

- Where: `docs/tickets/` in this repository
- Pickable work: tickets with `Status: open` or `started` that are not blocked<, narrowed further if you like, such as by Assignee>
- Ranking: `started` before `open`, then the earliest `Due` (tickets without one after), then the lowest id first
- Excluded: <what is never offered, such as tickets of Type map and the question tickets under a map, which the wayfinder skill works>
- New ticket: a new file with the next id and `Status: open`<, plus the Type and Parent it needs>
- Start: `Status: started`, and the `Assignee` line set to the user
- Note: a dated bullet under `## Log`
- Done: `Status: done`, with a note saying what was done
- Stopped partway: leave `Status: started` with a note saying where it stands; `paused` when it is set aside
- Cannot proceed: `Status: waiting`, with a note naming the blocker
- Not worth doing: propose `Status: dropped`; the user decides
- Parent and children: a `Parent` line in each child
- Blocking: a `Blocked by` line in the blocked ticket
- Close the parent: `Status: done` on the parent once every child is closed

## House rules

<!-- Example: A ticket of Type idea is never offered as work. -->

## Wayfinding operations

- Map: a ticket file titled with the destination, with `Type: map` and no `Parent` line, its body holding the map body. Find maps by reading the header lines for `Type: map` and a status that is not closed. Read the file again just before editing its body.
- Child ticket: a new ticket file titled with the question, with a `Parent` line naming the map's id and a `Type` line, its body holding the question and any options. Questions never name each other as `Parent`. Blocking between questions is the `Blocked by` line, added in a second pass once every new ticket has its id.
- Type marker: the `Type` line, exactly one of `research`, `prototype`, `grilling`, or `task`.
- Claim: read the file and skip it if its status is `started` or its `Assignee` names someone else. Otherwise set `Assignee` to the user and `Status: started` before any work. In a shared project, commit the file by path at once so other people see the claim; in a project only the user works on, the claim needs no commit of its own and goes in with the resolve. To release a claim when a session stops without resolving the question, set `Status: open` again and clear `Assignee` if the claim set it.
- Frontier query: the ticket files whose `Parent` line names the map's id, with `Status: open`, an `Assignee` that is empty or the user, and not blocked (every id in `Blocked by` names a `done` or `dropped` ticket), lowest id first.
- Resolve: add a dated note with the answer's gist and a link to where it is recorded: its decision file for a choice, its research document for a fact, or, for a task, the note itself saying what was done and the facts later questions need. Set `Status: done`, clear the `Assignee` the claim set, add the one-line pointer under `## Answers so far` in the map's body, and commit the ticket, the map, and any decision file or research document together. A question ruled out of scope gets `Status: dropped` with a note starting `Out of scope:`, and its line goes under `## Out of scope` instead.
