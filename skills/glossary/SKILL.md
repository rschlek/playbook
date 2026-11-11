---
name: glossary
description: >-
  Keep the project's glossary: pin down the words the project uses in
  docs/glossary.md, one precise meaning each, as they are settled. Challenge
  a word used two ways or against the glossary, sharpen fuzzy terms, and
  test the boundaries between concepts with concrete scenarios; offer to
  record a hard-to-reverse decision (docs/decisions/) only when one comes up.
  Works for any kind of project: a software system, a compliance process, a
  research field, a household. Use when the user is naming or defining
  things, says "what do we call this", "define our terms", "update the
  glossary", "these two words mean the same thing", or when grill-me or
  wayfinder finds a word used two ways. Do NOT use for merely reading the
  glossary to use its words, for stress-testing a whole plan (that is
  grill-me), or for charting work too big for one session (that is
  wayfinder).
---

# Glossary

Pin down the project's words in its glossary as the work is designed. This is the *active* discipline: challenging terms, inventing edge-case scenarios, and writing each settled word down the moment it crystallises, with a decision recorded only when one truly comes up. (Merely *reading* `docs/glossary.md` for vocabulary is not this skill: that's a one-line habit any skill can do. This skill is for when the words are changing, not just being used.)

Shared paths such as `references/conventions.md` are relative to the plugin's root folder, two levels above this skill's folder. `GLOSSARY-FORMAT.md` and `DECISION-FORMAT.md` sit beside this file.

## File structure

The glossary and the decisions are records in the project's repository. With no repository, say so and offer the `new` skill; do not keep them anywhere else.

Most projects have a single context:

```
/
└── docs/
    ├── glossary.md
    └── decisions/
        ├── 2026-03-02-orders-are-event-sourced.md
        └── 2026-04-11-retain-records-seven-years.md
```

If `docs/glossary.md` is a map of contexts (see `GLOSSARY-FORMAT.md`), the project has several, each with its own file under `docs/glossary/`. Decisions stay in the one `docs/decisions/` folder for every context; the title names the context when it matters.

Create files lazily: only when you have something to write. If no glossary exists, create `docs/glossary.md` when the first term is resolved. If no `docs/decisions/` exists, create it when the first decision is recorded. A project that already keeps its glossary or its decisions in another place keeps them there until the user decides to convert it, as "Documents" in `references/conventions.md` says; an older single decisions file stays as history and new decisions go in the folder.

## During the session

### Challenge against the glossary

When the user uses a term that conflicts with the existing language in the glossary, call it out immediately. "Your glossary defines 'cancellation' as X, but you seem to mean Y. Which is it?"

### Sharpen fuzzy language

When the user uses vague or overloaded terms, propose a precise canonical term. "You're saying 'account': do you mean the Customer or the User? Those are different things." Or: "You're saying 'review': do you mean the annual Audit or the Sign-off on each change?"

### Discuss concrete scenarios

When domain relationships are being discussed, stress-test them with specific scenarios. Invent scenarios that probe edge cases and force the user to be precise about the boundaries between concepts.

### Cross-reference with the project

When the user states how something works, check whether the project agrees: its code, procedures, forms, or records. If you find a contradiction, surface it: "Your code cancels entire Orders, but you just said partial cancellation is possible. Which is right?" Or: "Your retention procedure deletes records after five years, but you just said seven. Which is right?"

### Update the glossary inline

When a term is resolved, propose its glossary entry right there. Don't batch these up: capture them as they happen. Use the format in `GLOSSARY-FORMAT.md`. In a shared project (`project.yaml` says `shared: true`, or a `visibility` other than private), show the exact text and write it only on the user's yes. In a project that is the user's alone, write it when a glossary already exists or the user asked for one; otherwise ask once whether to start one ("Documents" in `references/conventions.md`: other documents are written only when asked). A no holds for the rest of the session: settle words in the conversation and do not ask again. Never write a file to record the no.

The glossary should be totally devoid of how-it-is-done details. Do not treat it as a spec, a scratch pad, or a store for decisions. It is a glossary and nothing else.

### Offer decisions sparingly

Only offer to record a decision when all three are true:

1. **Hard to reverse**: the cost of changing your mind later is meaningful
2. **Surprising without context**: a future reader will wonder "why did they do it this way?"
3. **The result of a real trade-off**: there were genuine alternatives and you picked one for specific reasons

If any of the three is missing, skip it. Use the format in `DECISION-FORMAT.md`: one file per decision, `docs/decisions/YYYY-MM-DD-<short-name>.md`, project facts only, written for a reader who opens the project cold. Before writing one into a shared project, show the user the exact text and wait for a yes. A question on a decision map is the exception: when its answer settles a choice (something that could have gone another way), the `wayfinder` skill writes it as a decision file whether or not these three hold; a fact found or a task done gets no decision file.
