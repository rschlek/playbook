# to-tickets

- Maintainer: the playbook plugin maintainers
- Origin: written for this plugin in playbook 1.0.0 as one generic skill doing the work of the to-spec and to-tickets skills in Matt Pocock's skills repository (https://github.com/mattpocock/skills, at commit 4ae2317, 2026-10-31), MIT licensed, copyright (c) 2026 Matt Pocock. No text is copied; the shape (write the plan, then create ordered tickets with blocking) follows those skills.

Turns a finished plan into tickets. The input is a settled decision map or a plan agreed in the conversation. It writes the plan (what and why, the pieces in order, what done means, links to the decisions in `docs/decisions/`) into a parent ticket of its own, linked from the map, shows it, and after the user's yes creates the work tickets under that parent in order, then links blocking in a second pass. Once the plan is linked it closes the map. It reports which tickets are ready to start. The model may invoke it, for example when the `wayfinder` skill hands off a finished map, but it shows the plan and the ticket list and creates nothing before the user's yes.

## Maintainer notes

- Guard: while a map has open question tickets, the skill stops, lists them, and points back to the `wayfinder` skill.
- Work tickets sit under the plan's parent ticket, never under the map, so the map's frontier query only ever returns question tickets.
- Linking the plan from the map body uses the Mechanics' Edit operation in the tracker templates.
- The tracker doc lookup lives once in `references/tracker-lookup.md`, shared by every tracker-using skill; change it there, in step with "Trackers" in `references/conventions.md`.
