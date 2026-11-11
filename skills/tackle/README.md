# tackle

- Maintainer: the playbook plugin maintainers
- Origin: written for this plugin in playbook 1.0.0, replacing an earlier version tied to one tracker product

Helps the user do one existing ticket and close it out honestly, or picks a few worth doing now. It works with any tracker that has a tracker doc: it finds the doc by the standard's resolution order, operates the tracker only through the doc's Mechanics, and reads every step (pickable work, ranking, start, done, stopped partway, cannot proceed, not worth doing, close the parent) from the doc's Layout. House rules in the doc override the skill.

## Maintainer notes

- The skill names no tracker product. Anything tracker-specific belongs in a template under `references/trackers/`, not here.
- Picking never offers excluded, house-ruled, blocked, map, or question tickets, and says what it left out. A user may still name any ticket; the skill says which rule it breaks and asks.
- Closing out never deletes a ticket. Follow-ups go through the `capture` skill.
- When the closed ticket was the last open child of its parent, the skill offers to close the parent and waits for a yes.
- The tracker doc lookup lives once in `references/tracker-lookup.md`, shared by every tracker-using skill; change it there, in step with "Trackers" in `references/conventions.md`.
