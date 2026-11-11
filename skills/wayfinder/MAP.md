# The map in detail

Reference for the `wayfinder` skill: the map body, the question tickets, the ticket types, and the fog and scope rules. How each of these is held in a given tracker is in the tracker doc's `## Wayfinding operations`.

## The map is an index

The map is one ticket in the primary tracker, made with the Map operation. Its question tickets are its children. The map is an **index**, not a store: it lists the answers reached and points at the decision files that hold them. A decision lives in exactly one place, its file in `docs/decisions/`, so the map never restates it; it gives the gist in a line and links the file.

## The map body

The whole map at low resolution, loaded once per session. Open questions are **never** listed here: they are the map's open child tickets, found with the Frontier query, and their status lives only in the tracker.

```markdown
## Destination

<what reaching the end of this map looks like: the spec, choice, or settled process this effort is finding its way to. One or two lines; every session orients to it before choosing a ticket.>

Plan: <added by to-tickets once the plan exists: the plan ticket's title and link>

## Notes

<the domain; skills of this plugin every session should be offered (a suggestion the agent confirms with the user); standing preferences for this effort>

## Answers so far

<!-- one line per resolved question, enough to judge relevance; follow the link for the detail. The name links the decision file; a research finding with no choice to record links its research document, a task links its ticket. -->

- [<question ticket title>](<path to docs/decisions/YYYY-MM-DD-short-name.md>): <one-line gist of the answer>

## Not yet specified

<!-- in-scope fog you cannot ticket yet; graduates as the frontier advances -->

## Out of scope

<!-- work ruled beyond the destination; never graduates -->
```

When the map is done, the `to-tickets` skill writes the plan into a parent ticket of its own, titled `Plan: <the destination>`, links it from the map body, and closes the map. Work tickets never sit under the map. A map whose answers leave no work closes on the user's yes.

## Question tickets

Each question is a child ticket of the map, made with the Child ticket operation; the tracker's id is its identity. Its body is the question, sized to one agent session:

```markdown
## Question

<the decision or investigation this ticket resolves>

## Options

<the options known so far, when there are any; leave the section out otherwise>
```

Each carries exactly one type marker (Type marker operation): research, prototype, grilling, or task. A map and its questions carry no other workflow markers: they are decisions, not work. The answer is never added to the body; it is recorded on resolution. Anything made while resolving a ticket (a research document, a prototype) is linked from the ticket, not pasted in.

Blocking uses the tracker's own link where it has one, because it shows the frontier in the tracker itself; the tracker doc gives the fallback where it has none. A ticket is **unblocked** when every ticket blocking it is closed. The **frontier** is the open, unblocked, unclaimed children: the edge of the known.

## Ticket types

Every ticket is either **human in the loop** (worked with the user, who speaks for themselves) or **agent alone**. A human-in-the-loop ticket resolves only through that live exchange; the agent never stands in for the user's side of it (a grilling agent that answers its own questions has broken this).

- **Research** (agent alone): reading documentation, standards, regulations, third-party services, or local material to surface a fact a decision waits on. Resolved by invoking the `research` skill, in a fresh-context subagent where the harness has one, otherwise inline. Use when knowledge from outside the project is needed. Its output is a dated document under `docs/`, linked from the ticket; when its finding settles a choice, that choice is written as a decision file too.
- **Prototype** (human in the loop): raise the fidelity of the discussion with a cheap, rough, concrete thing to react to (an outline, a draft, a mock-up, a stub, or code), by invoking the `prototype` skill. The prototype is linked from the ticket. Use when the key question is how something should look, read, behave, or go.
- **Grilling** (human in the loop): conversation, the default case. Invoke the `grill-me` skill and the `glossary` skill.
- **Task** (human in the loop or agent alone): work that must happen before a decision can be made. Nothing to decide, prototype, or research, but the discussion is blocked until it is done: signing up for a service so its interface can be judged, requesting a copy of a policy so its terms can be read, gathering last year's figures so their shape can be seen. It is the one type that does rather than decides, and it earns its place by unblocking a decision, not by delivering the destination. The agent drives it alone where it can; otherwise it hands the user a precise checklist. It is resolved when the work is done: the resolve comment records what was done and the facts later tickets depend on (where something now lives, new links, counts), never a secret.

## Decision files

One file per resolved question that settles a choice, `docs/decisions/YYYY-MM-DD-<short-name>.md`, lowercase with hyphens, written under the record-writing rule in `references/conventions.md`. Keep it short; a line or two per section is often enough.

```markdown
# <Short title of the decision>

Question: <the question ticket's title, with its link>

<What was decided, in one to three sentences.>

## Options considered

- <option>: <why it was or was not taken>

## What settled it

<the facts and figures that decided it, linking any research document or prototype>

## Replaces

<the earlier decision file this replaces, or "Nothing.">
```

A decision file is not edited afterwards, except that a later decision replacing it adds one line, `Replaced by: <new file name>`.

## Fog of war

The map is deliberately incomplete: do not chart what you cannot yet see. Beyond the live tickets lies the **fog of war**: the dim view of questions you can tell are coming but cannot pin down, because they hang on questions still open. Resolving a ticket clears the fog ahead of it, graduating whatever is now specific into fresh tickets, until the way to the destination is clear and no tickets remain.

**Not yet specified** is where that dim view is written down: the suspected question, the area to revisit later. Everything in it is in scope, just not sharp enough to ticket. Write as loosely or as fully as the view allows; it also tells collaborators where the effort is headed.

**Fog or ticket?** The test is whether you can state the question precisely now, not whether you can answer it now.

- **Ticket** when the question is already sharp, even if it is blocked and cannot be worked yet.
- **Not yet specified** when you cannot phrase it that sharply. Do not pre-slice the fog into ticket-sized pieces: one patch may graduate into several tickets, or none.

Not yet specified excludes what is already answered, what is already a live ticket, and what is out of scope.

**When the frontier is empty**, settle each patch still in Not yet specified with the user, one way or another: a real question becomes a question ticket and the map goes on; work that needs no decision (a step to do, not a choice to make) is marked `(plain work)` and goes into the plan as a work item; anything beyond the destination moves to Out of scope. The map is done when Not yet specified holds nothing but plain work.

## Out of scope

Fog only gathers toward the destination. The destination fixes the scope, so work beyond it is **out of scope**: not fog, and not part of Not yet specified. It gets its own section: work consciously ruled out of this effort. Scope, not sharpness, lands it here. It never graduates; it returns only if the destination is redrawn, and then as a fresh effort.

Ruling something out of scope is a scoping act agreed with the user, not a step on the route. When an existing ticket turns out to sit past the destination, close it with the Resolve operation's not-planned close (a closed ticket is off the frontier) and add one line to Out of scope: the gist and why it is out, naming the closed ticket. It stays out of Answers so far, which records the route actually walked, and it gets no decision file unless the user wants the scope boundary recorded as a decision.
