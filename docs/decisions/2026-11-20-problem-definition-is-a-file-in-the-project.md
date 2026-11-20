# A problem definition is a file in the project

Question: Where is define's result recorded, and how does it reach wayfinder as the destination?

`define` writes its result, the problem definition, as a file in the project's repository. With no project, it offers to start one. `wayfinder` reads the problem definition to name its destination.

## What was decided

1. The name. The document `define` writes is a problem definition. The earlier working name, problem brief, is dropped.
2. A file in the project. It is written to `docs/problems/YYYY-MM-DD-<short-name>.md`, dated the day it is first written. A ticket may link it. It is not kept in a ticket.
3. Draft or settled. A status line at the top says draft, with the number of questions still open, or settled. A draft is updated in place when answers come back. Once the user says it is settled, it is not edited: a problem that has changed gets a new problem definition that names the one it replaces.
4. No project. `define` shows the finished problem definition in the conversation and asks whether to start a project for it, private by default, with the problem definition as its first document. On a yes it invokes the `new` skill. On a no, nothing is kept, and the text is the user's to copy.
5. Who can read it. A problem definition can hold facts internal to an organization. Before writing one into a shared or public project, `define` says who will be able to read it and waits for the user's yes, as for every record in a shared project. When the user says it cannot go there, the work is treated as having no project.
6. How it reaches `wayfinder`. When `wayfinder` is started on work that has a problem definition, it reads it, proposes the destination from it, and the user confirms or corrects that. It does not interview from the start. The map's Notes link the problem definition. A draft can still be charted: its open questions that matter go on the map.

## Options considered

- In a ticket: not taken. A tracker is a poor place for a long document, and the document would be tied to one tool.
- A decision file: not taken. A problem definition records a problem, not a choice.
- A folder of drafts outside any project: not taken. It is one more place to look in and keep tidy, and every other record lives in a project or is not kept.
- A file in the project, and an offer to start a project when there is none: taken.
- Other names: problem brief, problem statement, requirements document, problem frame. Not taken. A problem statement is usually a sentence or two, and a requirements document says what a solution must do.

## What settled it

- Playbook keeps every record of a project in its repository. Research with no repository is already given in the conversation and not kept.
- The name matches the skill: `define` produces a definition.
- The folder is `docs/problems`, so that it is not confused with the glossary, which defines words.

## Not settled here

- What `guide-me` offers once a problem definition is settled, and which step lays out the ways to solve it. A separate question on the map holds these.
- What the questionnaire skill is called and how its answers come back. A separate question holds it.

## Replaces

In part, the decision that define is an open interview that ends with a problem brief (`2026-11-20-define-ends-with-a-problem-brief.md`): the name only. Where that record says problem brief, read problem definition.
