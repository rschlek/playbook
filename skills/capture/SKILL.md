---
name: capture
description: >-
  Add one new, well-formed ticket to the user's tracker, in the right tracker
  and place, with a title that states the outcome and a line saying what done
  means. Use when the user says "add a ticket", "capture this", "put this on
  my list", "add this to my to-dos", "remind me to ...", "file a follow-up",
  "make a ticket for that", or when something in the conversation clearly
  needs to become a ticket. Works with any tracker that has a tracker doc. Do
  NOT use to sort or clear an inbox, to turn a whole plan into tickets (that
  is to-tickets), to do an existing ticket (that is tackle), or to add a
  question to a decision map (that is wayfinder).
---

# Capture

Turn one thing to do into one well-formed ticket. The conversation usually
holds more than the words given: use it to propose a real description, not a
copy of the title.

## The tracker doc

Paths such as `references/tracker-lookup.md` are relative to the plugin's
root folder, two levels above this skill's folder. Find and read the tracker
doc as `references/tracker-lookup.md` says, before the first tracker call:
it covers where the doc is, empty roles, House rules (they can narrow this
skill, never remove a confirmation), two trackers, and what to do when no
doc is found. The doc is all this skill needs: no `project.yaml`, and for a
repository's own `docs/tracker.md`, no profile.

## Procedure

1. **Take the input**: what the user said and the context around it. When it
   holds several independent outcomes, say so and capture each as its own
   ticket, one at a time. A whole plan with ordered pieces is for the
   `to-tickets` skill; say so and offer it. When you could simply do the
   thing now in this session, say so and offer that instead.
2. **Pick the tracker.** With two trackers, use the one the doc assigns this
   kind of ticket to; ask only when the doc does not settle it.
3. **Check for an existing ticket** that already covers it, with Mechanics'
   Find by name and its quirks. When a search matches whole phrases, search
   one distinctive word; when it comes back empty, list the likely place
   (titles only, within the tool's limit) and compare titles by meaning. A recurring ticket or the same outcome in other
   words counts. On a match, show it and ask: add a Note to it, skip, or
   create anyway.
4. **Draft the ticket.**
   - Title: the outcome as a short action ("Renew the car registration",
     not "registration").
   - Description: enough for someone else to pick it up cold: why it
     matters, what is already known, where the materials are, what it waits
     on. Nothing the title already says.
   - A last line `Done when: <the result anyone could check>`.
   - Place and fields exactly as the Layout's New ticket says. When New
     ticket is empty, ask the user where in the doc's Where it goes. A field
     the input does not settle (a date, a priority) is a question for the
     user, never an invented value; give a date only when something must
     happen by then.
   - Links: when it belongs to a larger piece of work, it is a child of that
     work's parent ticket (Layout's Parent and children); when the parent is
     in the other tracker, the ticket carries a link to the parent in its
     description instead and the parent's body gets a line listing it with
     its link (Mechanics' Edit), never a copy. When it cannot start until
     another ticket closes, it is blocked by that ticket (Layout's Blocking).
5. **Keep shared text clean.** In a shared project (`project.yaml` has
   `shared: true`, or a `visibility` other than private), the ticket
   holds project facts only: no personal details, nothing about people
   beyond their role in the work, no record of who said what, and no
   personal reasoning.
6. **Show the draft**: tracker, place, title, description, done line,
   fields, links, and any near-duplicate, marking what you inferred. Wait
   for a yes or changes. Skip this only when the user dictated the ticket
   word for word, and never in a shared project.
7. **Create it** with Mechanics' Create, then add the links with Link parent
   and child (or the parent's listing line) and Link blocking, using the new
   ticket's real id.
8. **Confirm** what was created: its title, its id or link, and where it
   sits.

## Notes

- One capture, one ticket. Never re-shape other tickets while capturing
  (a parent's listing line aside); a near-duplicate is reported, not merged.
- Capture files work; it does not start it. Doing a ticket is the `tackle`
  skill.
