# capture

- Maintainer: the playbook plugin maintainers
- Origin: written for this plugin in playbook 1.0.0

Adds one new, well-formed ticket to the right tracker and place: a title that states the outcome, a description someone else could pick up cold, a `Done when:` line, the place and fields the tracker doc's Layout gives for a new ticket, and parent and blocking links when it belongs to something. It checks for an existing ticket first, shows the draft before creating it, and confirms the result with its id or link.

## Maintainer notes

- The skill names no tracker product; it reads the tracker doc. Placement and required fields come only from the Layout's New ticket role.
- In a shared project the ticket text follows the record-writing rule in `references/conventions.md`: project facts only.
- One ticket per run. A whole plan is the `to-tickets` skill; sorting an inbox is out of scope.
- The tracker doc lookup lives once in `references/tracker-lookup.md`, shared by every tracker-using skill; change it there, in step with "Trackers" in `references/conventions.md`.
