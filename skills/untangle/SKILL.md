---
name: untangle
description: >-
  For when the user is lost: says it plainly, then turns the agent's own
  pile (findings, options, jargon, a multi-part recommendation, a status
  dump) into a short sequence of small plain-language decisions, walked one
  at a time, each with a recommendation, with what is already decided
  separated from what is still open. A point that needs understanding first
  is explained plainly on the way. Use when the user says "I'm lost", "I'm
  overwhelmed", "I don't understand", "plain English", "explain this
  simply", "break this down", "simplify this", "one decision at a time",
  "walk me through them", "too much to review at once", or "I don't
  remember my open decisions". Also use unprompted when a reply would hand
  the user more than three open decisions at once. Do NOT use for
  stress-testing a plan the user already has (that is grill-me), for asking
  where the project stands or which skill comes next (that is next), or for
  editing the work itself to make it simpler.
---

# Untangle

The user is not confused because the work is wrong. They are confused because it
arrived as a pile. Hand it back as decisions they can answer in a word.

## Procedure

1. **Change register, out loud.** One line that says so ("Let me back up and say
   this plainly, then we take one decision at a time"). If a mix-up was the
   agent's, name it in that line.
2. **Give the whole picture in plain words.** Three short paragraphs at most:
   what this thing is, what was found or proposed, why it matters to the user.
   Every term is translated or dropped. One everyday comparison is worth more
   than a second paragraph of detail.
3. **Sort the pile into three buckets, with counts.**
   - *Already decided:* each with a status word (done, decided but not built,
     blocked). These are not reopened.
   - *Open, and the user's:* the real decisions.
   - *Not a decision:* things the agent will simply do, or facts for reference.
   Anything the agent can settle by looking it up leaves the open bucket now.
4. **Order the open ones.** A decision that others depend on goes first, then by
   size of consequence. Say how many there are ("4 open, starting with 1").
5. **Walk them one per turn.** Each decision carries:
   - the question in one plain sentence;
   - what changes for the user either way;
   - one recommendation and the single reason that decides it;
   - how to answer in a word ("yes", "A", "you pick").
   Then stop. Do not preview the next one.
6. **Take the answer and move.** "Noted: X. Next." and the next decision.
   Settled items are never shown again in full. "You pick" is a valid answer:
   take the recommendation and mark it as delegated.
7. **If an answer shows the question did not land, make it smaller.** Split the
   decision, define the one term in the way, or give a concrete example. Never
   repeat the same explanation at greater length.
8. **Close with a ledger and one question.** A short list of what was decided
   (delegated ones marked), what the agent will now do in order, and a single
   closing question asking for the go. Nothing is changed until the user says
   yes; agreeing to each piece is not agreeing to the sum.

## Never

- Ask a question before the plain picture and the decided/open split exist. A
  narrow question with no recap under it is the pile in another form.
- Stack questions, or offer a menu with no recommendation.
- Explain with shorthand: bare dates, ticket or decision numbers, acronyms, or
  labels coined earlier in the session. Restate the thing itself.
- Slide back into bulk delivery. Once the user asks for one at a time, that
  holds for the rest of the pile and for the next pile in the session.
- Reopen a settled decision unless new evidence changes it, and then say what
  changed.

## Notes

- Works the same in plain chat and in a structured question prompt, where the
  harness offers one. If a prompt is used, the plain explanation goes inside the
  question itself, never only in the text above it, and it is still one
  decision per prompt.
- The same walk fits reviewing long material: one section per turn, with what
  that section is for stated in plain words directly above it.
- Status requests about the pile in this conversation ("where do we stand on
  these") are steps 2, 3 and 8 without the walk: the picture, the three
  buckets, and one closing question. Start the walk only if the user wants to
  settle the open ones now. Where the project as a whole stands is the `next`
  skill.
- When nothing is waiting to be decided, steps 1 and 2 are the whole job:
  the plain picture, then follow the user's questions, making it smaller
  (step 7) when it does not land. Change nothing.
- Direction is the difference from `grill-me`: grill-me pulls answers out of
  the user about their plan; this hands the agent's pile to the user in pieces.
  When one decision needs something understood before it can be asked,
  explain that one point plainly (a few plain sentences, one everyday
  comparison), then return to the walk.
