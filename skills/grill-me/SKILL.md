---
name: grill-me
description: >-
  Interview the user relentlessly about a plan or design until reaching shared
  understanding, resolving each branch of the decision tree one question at a
  time, each with a recommended answer. Works for any plan: a software design, a
  compliance process, a research approach, a move or a trip. Use when the user
  wants to stress-test a plan, get grilled on their design, poke holes in an
  idea, or says "grill me", "challenge this plan", or "what am I missing". Do
  NOT use for explaining something plainly or handing the agent's own pile
  back to the user as small decisions (that is untangle), for keeping the
  project's glossary (that is glossary, which this skill calls when a word
  is used two ways), or for charting work too big for one session (that is
  wayfinder).
---

# Grill Me

The plan is the user's; the agent's job is to test it by asking. Keep asking
until both sides understand the plan the same way.

## Procedure

1. **Interview the user relentlessly** about every aspect of the plan, until
   reaching a shared understanding of it.
2. **Walk down each branch of the design tree**, resolving dependencies between
   decisions one by one.
3. **Give a recommended answer with each question.**
4. **Ask the questions one at a time.**
5. **If a question can be answered by looking at the project itself (its
   files, documents, records, or code), look instead of asking.**
6. **When a word in the plan turns out to be used two ways, or conflicts with
   the project's glossary, pause and pin it down with the `glossary` skill**
   (it records the word, with its own confirmation in a shared project), then
   carry on with the interview. With no repository, do not invoke it: settle
   the word in the conversation and carry on.
