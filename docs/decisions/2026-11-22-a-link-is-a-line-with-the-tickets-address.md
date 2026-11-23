# A link is one line holding the project ticket's web address

Question: What does the Link label in a tracker doc say: where a link is stored, how it is found, and from which side?

A personal item links a project ticket with one line, `Link:` followed by the ticket's full web address, at the start of the item's description. Each tracker doc's Link label says where that line goes in its tracker and how items are found by it.

## What was decided

1. The form. One line: `Link:` and the project ticket's full web address. A person can follow it, and it can mean only one ticket.
2. Where it is stored. By default, the first line of the item's description. A tracker doc may name a field of the tracker's own where its tool can search that field. Where the tool can search only titles, the address goes at the end of the title. It never goes in a comment.
3. One side only. The link is on the personal item. Nothing is written to the project ticket. Several personal items may carry a link to the same ticket.
4. What the Link label says. Each tracker doc's Mechanics has one label, `Link`, with three parts:
   - Stored: the place in this tracker where the line is kept.
   - Find by ticket: the one search that returns every item whose link is a given address.
   - Find all: the one search that returns every item that carries a link into a given project tracker. This is the one query the check for pairs out of step uses.
5. A project ticket with no linked item is found by comparing. The project tickets assigned to the person are read in one batch and set against the items that Find all returns. A ticket none of them points at has no personal item.
6. An empty label. With no Link label in the personal tracker's doc, the skills do not link, and they say so. Setup fills the label for a personal tracker.
7. Proved at setup. Setup stores the line on a throwaway item, on the user's yes, and searches for it, as the decision on what a tracker doc may require says.

## Options considered

- A short ticket id with the name of its tracker: not taken. It cannot be followed, and two trackers can hold the same id.
- A line in the description as the only place: not taken. In the test, one shipped tracker's tool could search titles and ids only.
- The tracker's own field wherever it has one: allowed, not required.
- A comment on the item: not taken. In the test, only one tracker's search found a link there.

## What settled it

- The test on the four shipped trackers, in the closing comment of the map question on it: a link in the description or body was found in three of four, a link in the title in all four, a link in a comment in one, and the full address and the short id were both found wherever the place was searchable.
- The research in `docs/research/2026-11-19-cross-tracker-link-storage.md`.
- The person's choice of the full address.
- The decision that a tracker doc never requires the tracker to change.

## Not settled here

- The exact Link label in each shipped tracker doc. It is written with the work that follows this map, from the test results.
- How the rule that lets a linked pair move together reads in the conventions. A separate question on the map holds it.

## Replaces

Nothing.
