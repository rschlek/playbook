# untangle

- Maintainer: the playbook plugin maintainers
- Origin: written by the plugin's maintainers, part of playbook since 1.0.0

Turns the agent's own pile of findings, options, jargon, or status into a short sequence of small plain-language decisions. It gives the whole picture first, sorts the pile into already decided, open, and not a decision, then walks the open ones one per turn, each with a recommendation, and closes with a ledger and a single question asking for the go. A point that has to be understood before a decision can be asked is explained plainly on the way; when nothing is waiting to be decided, the plain picture and the user's follow-up questions are the whole job.

## When it fires

- The user is lost: "I'm lost", "I'm overwhelmed", "I don't understand", "plain English", "explain this simply", "break this down", "simplify this", "one decision at a time", "walk me through them", "too much to review at once", "I don't remember my open decisions".
- Unprompted, when a reply would hand the user more than three open decisions at once.

Not for stress-testing the user's own plan (`grill-me`) or for where the project stands and which skill comes next (`next`).

## Prerequisites

None beyond the agent.

## Maintainer notes

- The procedure is unchanged from the earlier version, except that a point needing explanation is now explained inline: in playbook 1.0.0 the separate plain-explanation skill was retired and untangle took over its phrases. The code-specific "not for" was made general, and the structured question prompt is named without naming any harness's tool.
- "Where do we stand" about the pile in the conversation stays here; where the project as a whole stands is `next`. Keep the two descriptions from competing for the same phrases.
- Model-invocable on purpose: it should fire unprompted when a reply would carry more than three open decisions.
