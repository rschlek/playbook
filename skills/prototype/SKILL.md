---
name: prototype
description: >-
  Make a cheap, rough, throwaway thing to react to, so one design question
  gets answered by seeing it rather than by arguing about it: an outline, a
  draft page, a mock-up, a mock schedule, a clickable walkthrough of a process
  or state model, a stub, or a few radically different screen variants. Works
  for any kind of project. Use when the user asks "how should it read", "how
  should the process go", "how should it look", "how should it behave", "does
  this logic feel right", "show me a few options", "sketch it out", or "mock
  it up", and for prototype tickets on a decision map. Do NOT use to build the
  real thing (that is tackle on a work ticket), to gather facts from sources
  (that is research), or to settle a choice by talking it through (that is
  grill-me).
---

# Prototype

A prototype is **a throwaway that answers a question**. The question decides the shape. Shared paths such as `references/conventions.md` are relative to the plugin's root folder, two levels above this skill's folder; `LOGIC.md`, `UI.md`, and `DRAFT.md` sit beside this file.

## Pick a branch

Identify which question is being answered, using the user's prompt, the surrounding project, or by asking if the user is around:

- **"Does this logic / state model / process behave right?"** → `LOGIC.md`. Build a single shareable HTML file (free-play buttons plus tabbed guided walkthroughs) that pushes the states and steps through cases that are hard to reason about on paper, and that someone who never reads code can drive. It suits an order's lifecycle as well as an approval process or a case moving through review.
- **"What should this screen look like?"** → `UI.md`. Generate several radically different variations on a single page of an existing app, switchable via a URL search param and a floating bottom bar.
- **"How should it read?" or "How should it go?"** for a document, form, message, schedule, or a process with no real states to click through → `DRAFT.md`. Write two or three radically different rough drafts of the thing itself (an outline, a sample page, a mock schedule, a walkthrough table) side by side in one file.

The branches produce very different artifacts, so getting this wrong wastes the whole prototype. If the question is genuinely ambiguous and the user isn't reachable, default to whichever branch better matches what the answer will become (code with states → logic; a page or component → UI; a document or a plan of steps → draft) and state the assumption at the top of the prototype.

## Rules that apply to every branch

1. **Throwaway from day one, and clearly marked as such.** Put it close to where the answer will be used so context is obvious, but name it so a casual reader can see it's a prototype (include the word `prototype` in its name). Written material goes under `docs/`. For throwaway screens, obey whatever routing convention the project already uses; don't invent a new top-level structure.
2. **Trivial to open.** A logic demo or a draft is a single file the user double-clicks or opens. A screen prototype starts from one command in the project's task runner. Either way, no thinking required to start it.
3. **No persistence by default.** State lives in memory. Persistence is the thing the prototype is _checking_, not something it should depend on. If the question explicitly involves stored data, use a scratch store or a local file with a clear "PROTOTYPE, wipe me" name.
4. **Skip the polish.** No tests, no error handling beyond what makes it _usable_, no abstractions, no final wording. The point is to learn something fast.
5. **Surface the state.** After every action (logic), on every variant switch (UI), or beside every draft (draft), show the full relevant state or what differs, so the user can see what changed.
6. **Link it from its ticket.** When the prototype serves a ticket, link it from that ticket by its path in the project. The skill that invoked this one (such as `wayfinder`) does it; when the user named a ticket directly, find the tracker doc as `references/tracker-lookup.md` says and leave the link as its Layout's Note says. It lives in the project's working tree on the branch the work is on; never push a separate throwaway branch for it.
7. **Capture the answer, then clear it away.** Read "Documents" in `references/conventions.md`. A prototype settles a choice, something that could have gone another way, so what it showed becomes a decision file, `docs/decisions/YYYY-MM-DD-<short-name>.md`: what was decided, the options the prototype put side by side, what settled it, what it replaces. It holds project facts only; in a shared project, show the user the exact text and wait for a yes. Then delete the prototype, or, if the user wants it kept, leave it where the project's layout puts it (written material under `docs/`) and say where. The real work the decision calls for is its own work ticket (the `to-tickets` and `tackle` skills), never the prototype promoted as is.

Records exist only inside projects: with no repository, give the answer in the conversation and write no decision file; offer the `new` skill only when the user asks to keep it as a record.
