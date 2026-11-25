# What goes on a project tracker is set once, in its tracker doc

Question: Where does the rule for what goes to the project tracker live, what form does it take, and how do to-tickets and capture apply it under one yes?

The rule is one role in the Layout of the project tracker's doc. Setup asks for it once, when the doc is built. The skills that create tickets show which tracker each ticket goes to in the review they already give, and one yes covers both trackers.

## What was decided

1. Its home. The rule is in the project tracker's doc, since it is the team's choice about its own tracker. Every project that points at the doc follows it.
2. Its form. One new role in `## Layout`, `What goes here`, holding a level and two optional lists:

```markdown
- What goes here: outcomes. Always: bugs. Never: research questions.
```

   - `everything`: the project's work goes here, planning included. This is what an empty or missing role means, so a doc written before this decision behaves as before.
   - `outcomes`: one ticket for each outcome of a plan goes here, or a link to a ticket that already exists. The map, the plan, and its steps go in the personal tracker, linked to the outcome they serve.
   - `Always` and `Never` name kinds of ticket in plain words. They win over the level for the kinds they name.
3. How an agent applies it. The level first, then `Always` and `Never`. Within what the level allows, the rule from the decision on which tracker each skill uses decides: work someone else could pick up goes here, a person's own breakdown does not. When still unsure, the personal tracker.
4. Asked once, at setup. When setup builds a project tracker's doc, it asks whether plans and open questions show on this tracker, or only outcomes. It suggests `everything` when the project's shared files carry playbook's files, and `outcomes` when the tracker is reached through the person's profile because the team does not use playbook. The answer is written into the role. Running setup again keeps it. A personal tracker's doc has no such role.
5. No standing personal override. The profile holds no setting that changes the team's rule for one person. In the review, before the yes, a person may move any item to their own list. An item is not moved onto the project tracker against a `Never` line: the skill says what the line is.
6. What `to-tickets` shows. Its one review groups the tickets under the tracker each goes to, with a count for each group. An item for the personal tracker shows the project ticket it links. An outcome that already exists is shown as linked, not created. One yes covers every ticket in both trackers.
7. What `capture` shows. Its draft carries one line naming the tracker the ticket goes to, with the title and the line saying what done means. One yes creates it. The person may say to put it on their own list.
8. `wayfinder` shows the same line when it charts a map.
9. The record rule still holds. In a shared project, text posted to the project tracker is shown in full first and holds project facts only. The role can keep more off the tracker. It cannot put on it what the record rule keeps off.
10. `outcomes` and no personal tracker. The skill says the tracker takes only outcomes and that the person has no tracker of their own to hold the plan, and offers to set one up. It creates nothing on the project tracker beyond the outcomes.
11. A person with no personal tracker, on a tracker at `everything`, sees one group and no change from before this decision.

## Options considered

- The rule in the profile only: not taken. It is the team's choice about its tracker, and two people on one team could then differ without knowing.
- The rule under House rules: not taken. House rules narrow what a skill may do, and this says where a ticket goes.
- A personal override kept in the profile: not taken. It is a second setting to keep right, and moving an item in the review does the same job when it is needed.
- Never asked, with `everything` unless someone edits the doc: not taken. On a tracker whose team does not use playbook, planning tickets that appear unannounced cannot be taken back.
- A second question for the split when tickets are created: not taken. The review already shows every ticket, and asking ticket by ticket was ruled out before the map was charted.

## What settled it

- The person's choice that setup asks once, when the tracker doc is built.
- The decision that project work goes to the project tracker by default and that the level is set once.
- `to-tickets` already shows one review and takes one yes.

## Not settled here

- How a person later shares something kept in the personal tracker. A separate question on the map holds it.
- The text that changes in each skill and in each shipped tracker doc. A separate question holds it.

## Replaces

Nothing.
