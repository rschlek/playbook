# A linked pair is two tickets kept in step, and the one-tracker rule stands

Question: How does the rule that lets a linked pair move together read in the conventions?

Replaced in part by: 2026-11-25-the-tracker-work-is-built-in-two-releases.md. The standard version moves at each of the two releases, not once.

The sentence "Every ticket lives in exactly one tracker, and its status lives only there" stays as it is. A personal item and the project ticket it links are two tickets, each with its own status. One new rule in "Trackers" says how the pair is kept in step. The standard version moves with the release that carries it.

## What was decided

1. The existing rule is unchanged. In `references/conventions.md`, "Trackers", this stays word for word: "Every ticket lives in exactly one tracker, and its status lives only there. Trackers are linked, never mirrored into each other."
2. One rule is added directly after it:

   "A person may keep a personal tracker beside a project tracker. A personal item that serves a project ticket carries a link to it, on the personal side only. The two are separate tickets, each with its own status in its own tracker: no text is copied, and nothing personal is written to the project tracker. The skills keep the pair in step and never mirror it. They compare the two states, and at start and at done they propose the change to the project ticket, which is made on the user's yes and only when the ticket is the person's. Nothing moves a ticket backwards, and nothing runs between sessions."

3. `references/tracker-lookup.md`, "Two trackers". The sentence "Links, never copies: no ticket's text or status is repeated in the other tracker" stays. One sentence follows it: "A personal item linked to a project ticket is a separate ticket, not a copy, and the shared reference on linked pairs says how the two are kept in step."
4. The base block. Its sentence "A ticket's status lives only in its tracker; never copy tickets between trackers" stays true and is not changed by this rule.
5. The changelog entry, dated when it is released:

   "A person may keep a personal tracker beside a project tracker. A personal item that serves a project ticket links to it from the personal side only, and the two are separate tickets, each with its own status. Skills keep a linked pair in step by comparing states and proposing the change at start and at done, made on the user's yes. Nothing is mirrored, and nothing runs between sessions. The rule that every ticket lives in exactly one tracker is unchanged."

6. The standard version moves. The conventions change, and every project carries a copy of them, so the release that carries this rule gives the standard a new version and sync replaces the copy in each project. The number is set at that release, once, for all the changes this map makes to the conventions.

## Options considered

- Rewording "its status lives only there" to allow two places: not taken. It would loosen the rule for every pair of trackers, and a linked pair does not need it.
- Calling the personal item a copy of the project ticket with an exception: not taken. It holds no text of the ticket and has its own state.
- Keeping the rule only in the shared reference, with nothing in the conventions: not taken. A reader of the conventions alone would take the behaviour for a breach of them.

## What settled it

- The decision on keeping a linked pair in step, which compares states and writes on the user's yes.
- The decision that nothing runs between sessions.
- The glossary's definitions of project tracker, personal tracker, and link.

## Not settled here

- The name of the shared reference on linked pairs, and the other sentences in the conventions that this map changes. They are written with the work that follows the map.

## Replaces

Nothing.
