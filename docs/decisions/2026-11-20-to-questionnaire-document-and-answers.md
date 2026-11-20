# to-questionnaire writes a document for someone else and brings the answers back

Question: What is the questionnaire skill called, and how do its answers come back?

The skill is `to-questionnaire`, adapted from the skill of that name in Matt Pocock's skills collection, which playbook already adapts other skills from. It writes a questionnaire document for one other person, sends it on the user's approval, and has a step that brings the answers back to where the questions came from.

## What was decided

1. The name is `to-questionnaire`.
2. It interviews the user about the send, not the subject: who the questionnaire goes to, and what the user needs back.
3. It writes a document, in the pattern of the skill it is adapted from: the purpose, who it is from and to, how the answers will be used, a paragraph of background, how to answer, the questions in themed sections with the most important first, and a closing question for anything else. Each question holds one idea, with an optional line on why it matters and an empty place for the answer. There is no fixed length.
4. Two ways to use it. The other person fills it in on their own time, or the user goes through it with them in a meeting.
5. A short message for a small ask. When the user needs one to three quick facts, the skill writes a short message in place of the document and says so.
6. Where it is kept. The questionnaire is a file in the project, `docs/questionnaires/YYYY-MM-DD-<short-name>.md`, with a status line: draft, sent, or answered. It names the other person by their role. Their name goes only in what is sent. With no project, the text is given in the conversation and nothing is kept.
7. How it is sent. The user approves the exact text. It then goes out through a connected tool that can deliver it, written in the user's voice. With no such tool, the file is handed to the user to send.
8. How the answers come back. The step starts when the user says the answers are in. The skill reads the reply through the connected tool when it can reach it. Otherwise the user pastes the reply or gives their notes from the meeting. Each answer is written under its question in the questionnaire file, and then carried to where the question came from: into the problem definition's list of what is still unknown, or onto the map question it answers, which `wayfinder` then resolves in its own steps. The user sees every change before it is written.
9. When it starts. On the user's ask, or on the user's yes to an offer from `define`, `wayfinder`, or `guide-me`. Never on the agent's initiative. It stands on its own and is not reachable only from `define`.

## What it adds to the skill it is adapted from

- The file is kept in the project, not in the current folder.
- A sending step, on the user's approval.
- The step that brings the answers back.
- It may be started on the user's yes to an offer, where the original starts only when the user calls it by name.

## Options considered

- Always a short message of a few questions: not taken. Written questions get thin answers unless the other person has the background and room to answer, and a short message cannot serve as the script for a meeting.
- A form with its own place to live: not taken. The other person would have to open something new, and it would need a place they can reach.
- Answers come back only into `define`, or only into a map: not taken. They go back to wherever the questions came from.
- The name `questionnaire`: not taken. `to-questionnaire` keeps the link to the skill it is adapted from and matches `to-tickets`.

## What settled it

- The person's doubt that a few short questions would bring back enough.
- The text of the skill it is adapted from, read on the day of this decision.
- The decision on how a define interview goes, which gives this skill the unknowns that only other people can answer.

## Not settled here

- Whether `guide-me` notices a questionnaire that was sent and not answered. It belongs with the question on how a `guide-me` session goes.

## Replaces

Nothing.
