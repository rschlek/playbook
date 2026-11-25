# define

- Maintainer: the playbook plugin maintainers
- Origin: written for playbook 1.0.4

Interviews the user about a problem, one plain question at a time, until both understand it the same way, then writes it down as a problem definition: a file `docs/problems/YYYY-MM-DD-<short-name>.md` in the project, with a status line (draft with its open questions, or settled), saying what the problem is, who has it, what happens today, what it costs, what solved looks like, its limits, what is out of scope, and what is still unknown. It holds no solution. Questions the project itself can answer are answered by looking instead of asking. Where facts are missing it proposes research and starts the `research` skill only on the user's yes. With no repository it offers the `new` skill, private by default, and on a no nothing is kept. In a shared or public project it says who can read the file and shows the exact text before writing it. It ends by pointing at `guide-me` for what fits next.

## Maintainer notes

- It is the step for writing down the problem, whoever arrives: a person with a loose want, and a person with a way of solving it already in mind. The second is asked what problem that way is meant to solve; the idea stays in the conversation for the next step and is never written into the problem definition.
- Problem only: it lays out no ways of solving the problem and records no pick. A problem written beside a recommended solution gets bent to fit the solution, and one without can be handed to someone else or sent out for comment. Which step lays out ways to solve a defined problem is still open, so the skill names none: its last step points at `guide-me`.
- It is its own skill, not a mode of `grill-me`: `grill-me` starts from a plan and tests it, writes nothing, and looks for no alternatives; `define` starts from a want or an idea and leaves a record.
- Started on the user's yes, by a rule in its body, like `wayfinder`. It carries none of the settings that mark a skill as started only by the user, so `guide-me` can start it after the user's yes. That yes covers starting it; every confirmation inside it still stands.
- `guide-me` offers it first whenever new work has no problem definition, and knows by one look at the project's `docs/problems/` folder. Keep the folder name, or change both skills together.
- A settled problem definition is never edited; a changed problem gets a new one with a `Replaces:` line. A draft is updated in place as answers come back.
- Answers only another person holds go under Still unknown, with who could answer each. A skill for sending those questions out is planned but not part of this plugin yet; until it is, the skill only lists them.
- Model-invocable on purpose, with the guard in its body: "define the problem" is said mid-conversation, in plain words.

## Prerequisites

None beyond the agent. A project repository is needed to keep the result; without one, the text is given in the conversation.
