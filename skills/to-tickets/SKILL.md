---
name: to-tickets
description: >-
  Turn a finished plan into tickets: write the plan into its own parent
  ticket, then create the work tickets under it in order, linked by what
  blocks what, from a settled decision map or a plan agreed in the
  conversation. Use when the user says "to-tickets", "turn this plan into
  tickets", "break the plan into tickets", "file the plan", or "make tickets
  for this", or when the last question on a decision map has been answered
  and the user agrees to create the tickets. Nothing is created before the
  user's yes. Do NOT use for one ticket (that is capture), for charting or
  answering open questions (that is wayfinder; this skill stops while a map
  has any), or for doing a ticket (that is tackle).
---

# To tickets

Write the plan once, in the tracker, then create the tickets that carry it
out. The plan lives in the body of its own parent ticket; the work tickets sit
under that parent, never under a map.

## The tracker doc

Paths such as `references/conventions.md` are relative to the plugin's root
folder, two levels above this skill's folder; "The decision map" there
defines the map. Find and read the tracker doc as
`references/tracker-lookup.md` says, before the first tracker call: it
covers where the doc is, empty roles, House rules (they can narrow this
skill, never remove a confirmation), two trackers, and what to do when no
doc is found. The plan's parent ticket goes in the primary tracker; each
work ticket goes in the tracker the doc assigns its kind to.

## 1. Find the input and guard it

- **A map**, when the user names one or the conversation is about one:
  recognise and fetch it as the Wayfinding operations and Mechanics say,
  children included. If any child question ticket is still open (claimed or
  blocked ones too), stop: list them by name with links, say the plan waits
  on them, and point the user to the `wayfinder` skill. What is left under
  Not yet specified is settled as `skills/wayfinder/MAP.md` says: plain
  work goes into the plan as work items; anything still a question goes
  back to `wayfinder`.
  If the body already links a plan ticket, show it and ask whether this
  replaces it, or whether only closing the map is left (then close it as in
  step 3 on a yes); never create a second plan silently.
- **Otherwise the plan agreed in this conversation.** Name any open question
  (an option not chosen, an "it depends", a fact still to find) and ask
  whether to map it first with the `wayfinder` skill or go ahead.

## 2. Write the plan

- What is being done and why: the destination in a sentence or two.
- The pieces of work in order, one line each, with what each waits on. Size
  each for one sitting: one person finishes it in one working session. Split
  anything bigger; fold a piece too small for its own ticket into a
  neighbour. Example: "Gather three years of receipts into one folder".
  Look for an existing ticket for each piece, as the `capture` skill's
  duplicate check does; mark matches in the list and offer to move them
  under the plan instead of creating new ones.
- What "done" means for the whole.
- The decisions it rests on, each a link to its file in `docs/decisions/`,
  never restated. A decision from the conversation with no file yet is first
  written as one, per "Documents" in `references/conventions.md`: always in a
  shared project, on the user's yes in their own (if no, the plan states it
  in one line, as it does with no repository unless the user asks for a
  project to keep the records, which is the `new` skill).
- A link to the map, when there is one.

The plan carries no progress and no statuses. Write it and any decision file
by the record rule in "Documents" of `references/conventions.md`.

Show the user the exact plan text, any decision file text, and the ticket
list (title, done line, tracker, what it waits on), and say that the map, if
there is one, closes once the plan is linked. Wait for a yes; that one yes
covers every step below. On changes, show it again.

## 3. Create, after the yes

1. **The plan's parent ticket**: titled `Plan: <the destination>`, placed
   and given fields as the Layout's New ticket says, the plan as its body.
   It is not a child of the map; fill the map body's `Plan:` line with it
   (Mechanics' Edit).
2. **Work tickets, first pass**: create each in plan order (or move the
   existing ticket the user agreed to reuse) as a child of the
   plan's parent ticket (Link parent and child), with a title stating the
   outcome, a description someone could pick up cold, a last line
   `Done when: <the result anyone could check>`, and fields as New ticket
   says. When Parent and children is empty, or the ticket belongs in the
   secondary tracker, it carries a `Plan: <title and link>` line in its
   description instead, and the plan's body lists it with its link
   (Mechanics' Edit). Links, never copies.
3. **Second pass, blocking**: link each ticket to what it waits on, using
   the real ids, as the Layout's Blocking says: the tracker's native blocking
   where it has one, else what Mechanics' Link blocking describes.
4. **Close the map**, when there is one, as the Layout's Done says.

If a create fails partway, stop, say what already exists, and do not start
over: a rerun would duplicate tickets.

## 4. Report

List the tickets created, in order, by name with id or link, each with what
it waits on. Say which are ready to start now (nothing open blocks them) and
that the `tackle` skill picks them up.
