---
name: define
description: >-
  Get to the root of a problem by interviewing the user, one plain question
  at a time, and write it down as a problem definition in the project: what
  the problem is, who has it, what it costs, what solved looks like, and what
  is still unknown, with no solution in it. For anyone starting new work:
  someone with a loose want, and someone who already has a way of solving it
  in mind. Works for any kind of work. Use when the user says "define the
  problem", "let's define the problem we are trying to solve", "what is the real
  problem here", "write down the problem", "I want something but I'm not
  sure what", "I don't know what I need yet", "should we build this", or "is
  this worth doing", or agrees when the guide-me skill offers it. Do NOT use
  to test a plan the user already has (that is grill-me), to gather facts
  from sources (that is research), to chart work too big for one session
  (that is wayfinder), or to lay out or choose ways of solving a problem.
---

# Define

The problem is the user's; the agent's job is to find its root by asking, then write it down before anyone picks a way to solve it. The result is a **problem definition**: a short document in the project that says what the problem is, who has it, what it costs, what solved looks like, and what is still unknown.

## Rules

- **Started on the user's yes.** Never start this skill on your own initiative: it writes a document into the project and may start a project. When you think the problem should be written down first, offer it and wait for the user's yes. When another skill offered it and the user said yes, do not ask again whether to begin: ask the first question.
- **Problem only.** Lay out no ways of solving the problem, compare none, and record no pick. A person who arrives with a way of solving it in mind is asked what problem that way is meant to solve. The idea stays in the conversation for the next step and is not written into the problem definition, and it is not judged.
- **Plain words.** Use the user's own names for their things. Say "problem definition" once, explained, when it first matters (the written result, kept in the project); use no other playbook word unless the user will need it later.
- **Nothing guessed.** A fact you cannot reach, or one only another person holds, is not filled in. It goes under what is still unknown, with who could answer it, named by role.

## Interview

1. **Start from what the user said.** When it names a way of solving something ("we need a new form", "let's buy X"), the first question is what problem that is meant to solve. When the user wants a plan they already have tested, not the problem written down, say so and offer the `grill-me` skill instead.
2. **Ask one question at a time**, in plain words: one idea per question. When you have a fair guess at the answer, offer it so the user can answer in a word.
3. **Follow the branches that matter.** There is no fixed list. The ground to cover: who has the problem and who else is affected, what happens today, what it costs (time, money, risk, frustration), how anyone would know it is solved, limits such as budget, deadline, and approvals, and what is out of scope.
4. **Look before asking.** If the project itself can answer (its files, documents, records, or code), look instead of asking. Look in `docs/problems/` too: an earlier problem definition may already cover this, or a draft may be waiting for answers.
5. **When a word turns out to be used two ways**, or conflicts with the project's glossary, pin it down with the `glossary` skill, then carry on. With no repository, settle the word in the conversation.
6. **When facts are missing**, propose research before looking anything up: say what you would look up and where, and mark which sources are internal to the user's organization. Invoke the `research` skill only on the user's yes. On a no, the item goes under what is still unknown.
7. **When someone else holds the answer**, say so plainly, and add the question to what is still unknown with who could answer it.
8. **Stop asking** when the user and you understand the problem the same way, and say so.

## The problem definition

It is a file `docs/problems/YYYY-MM-DD-<short-name>.md`, dated the day it is first written, in this shape:

```
# <the problem, in a few words>

Status: draft, <n> questions open
(or: Status: settled)

## The problem        a few plain sentences
## Who has it         and who else is affected
## What happens today
## What it costs
## What solved looks like   so that someone could check it
## Limits             budget, deadline, approvals
## Out of scope
## Still unknown      each question, with who could answer it
```

Leave a section out when the interview found nothing for it, except Still unknown, which says "Nothing" when empty. It holds project facts only, for a reader who opens it cold: people are named by their role, and there is no solution, no list of options, no pick, and no record of the idea the user arrived with. A problem definition that replaces an earlier one says so under the title: `Replaces: <file name>`.

## Write it

1. **Show the whole text** in the conversation and correct it until the user says it is the problem. Nothing is written before that yes. Ask only that in this turn: where the file goes (step 2 or 3) is asked after that yes, in a turn of its own, one question per turn.
2. **No repository for this work:** offer to start a project for it with the `new` skill, private unless the user decides otherwise, with the problem definition as its first document. On a yes, invoke `new`, then write the file there. On a no, nothing is kept: the text stays in the conversation for the user to copy.
3. **A shared or public project** (`project.yaml` says `shared: true`, or a `visibility` other than private): before writing, say who will be able to read the file (the people the repository is shared with, everyone in the organization that hosts it, or anyone), show the exact text, and wait for the user's yes. When the user says it cannot go there, treat the work as having no repository (step 2).
4. **Otherwise**, write the file on the yes from step 1.
5. **Draft or settled.** While any question under Still unknown is open, the status is draft with the count. A draft is updated in place when answers come back: show the changes, write on the user's yes, and recount. When nothing is open, ask whether it is settled. A settled problem definition is never edited: a problem that has changed gets a new one that names the one it replaces.

## Finish

Say in a line or two where the problem definition is and whether it is settled, or a draft with its open questions and who could answer each. Then say that the `guide-me` skill can say what fits next, and offer it; invoke it on the user's yes. Do not start any next step yourself.
