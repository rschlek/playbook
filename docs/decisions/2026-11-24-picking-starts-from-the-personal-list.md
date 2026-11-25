# Each skill uses the tracker the work belongs to, and picking starts from the personal list

Question: From inside a repository, how does tracker lookup find both trackers, and which one does each skill read and write?

From inside a repository, lookup finds the project tracker and, for a person who has one, the personal tracker. Work someone else could pick up goes in the project tracker. A person's own breakdown of a ticket they hold goes in the personal tracker, linked to that ticket. Picking work starts from the personal tracker and checks the project tickets behind its linked items before it offers anything.

## What was decided

1. Finding both. Lookup finds the project tracker's doc as the decision on pointing at a tracker doc says. When the profile's tracker is marked as personal and the project is not left out, lookup also reads the personal tracker's doc beside the profile. The skills hold the two apart by name, each with its own Mechanics and Layout. When the project's tracker is the personal tracker itself, there is one tracker and nothing is layered.
2. What goes where. Work that someone else on the project could pick up goes in the project tracker. A person's own breakdown of a ticket they already hold goes in the personal tracker. So does what is only the person's own, and anything the agent cannot place.
3. Project work in the personal tracker always carries a link. Every personal item that serves the project links the project ticket it serves. An item with no link is the person's own, or an idea not yet shared.
4. Picking starts from the personal tracker. With no ticket named, `tackle` reads the person's items for this project. Before it offers any, it reads the project tickets behind the linked items in one batch, the same read the check for pairs out of step makes. A linked item whose project ticket is now assigned to someone else, or closed, is not offered: the skill says so, names who holds the ticket, and offers to close the personal item.
5. Work nobody has taken. Pickable work in the project tracker that is assigned to nobody is shown when the personal tracker has nothing ready, or when the person asks for it.
6. Which tracker each skill uses, for a person with a personal tracker:

| Skill | Reads | Writes |
|---|---|---|
| `tackle`, picking | The personal tracker, then the project tickets behind its linked items | Nothing until a ticket is chosen |
| `tackle`, a named ticket | The tracker the ticket is in | That ticket. For a project ticket that is the person's, the personal item and the project ticket start under one yes, and closing the project ticket has its own yes |
| `capture` | Neither | One ticket in one tracker, by point 2, and it says which |
| `wayfinder` | The tracker the map is in | The map and its questions in the project tracker, or in the personal tracker when the project tracker's doc keeps planning out |
| `to-tickets` | The tracker the map or plan is in | The plan and its work tickets in the project tracker, or as the project tracker's doc says |
| `guide-me` | Both: maps, plans, and the state of the project from the project tracker, the person's ready work from the personal tracker | Nothing |

7. A ticket held by someone else. A skill writes nothing to a project ticket that is assigned to another person. It says who holds it.
8. A person with no personal tracker. Lookup finds one tracker, and every skill reads and writes it exactly as before this decision.
9. A repository someone else owns, or a team that does not use playbook. The project tracker comes from the project's entry in the profile. Skills write there only to tickets that are the person's, in words a person would write. What planning goes there is what that tracker's doc says.
10. A split project tracker. Everything said here about the project tracker holds for each part of a split one. A ticket goes to the part that holds its kind, a link may point into any part, and the read before picking makes one batch for each part.

## Options considered

- Picking from both trackers at once, merged: not taken. The personal tracker is meant to answer what the person needs to do today without a second place to look.
- Picking from the personal tracker with no look at the project tracker: not taken. Nothing keeps the two in step between sessions, so a ticket someone else took would still be offered.
- Every breakdown of a ticket in the project tracker: not taken. Much of it is too small to matter to the rest of the team.
- Project work in the personal tracker with no link: not taken. Nobody could tell what it serves, and the check could not see it.

## What settled it

- The person's model: the project tracker holds everything the project needs to move forward and lets people share the work, and the personal tracker holds what one person needs to do.
- The person's case: two people plan together, one takes a ticket the other also has on their own list, and nothing runs between sessions to say so.
- The decision that every project ticket assigned to a person has a personal item, so the personal tracker is complete for the person's own work.

## Not settled here

- How a claim tells this session from another session of the same person. A ticket outside this map holds it. Here a ticket counts as taken when it is assigned to another person.
- Where a project tracker's doc says what planning it takes, and its form. A separate question on the map holds it.
- How a person later shares something kept in the personal tracker. A separate question holds it.
- The text that changes in each skill. A separate question holds it.

## Replaces

Nothing. It adds to two earlier decisions. To the decision that project work goes to the project tracker: a person's own breakdown of a ticket they hold stays in the personal tracker. To the decision on keeping a linked pair in step: a project ticket that is now someone else's, or closed, is one more state the check reports.
