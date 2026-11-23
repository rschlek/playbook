# A tracker doc describes a tracker as it is, and never requires it to change

Question: What does playbook define about a tracker, what does a tracker doc add, and what may it require of the tracker?

Playbook says what a tracker must be able to do. A tracker doc, in plain speech a recipe, says how one tracker does it. The tracker stays as it is: no tracker doc may require it to be set up differently. The design covers a team's shared tracker as fully as one person's.

## What was decided

1. Three layers. Playbook says what a tracker must be able to do. A tracker doc says how one tracker does each of those things, and holds the habits of the people who use it. The tracker itself stays as it is.
2. The list is written down once. What a tracker must be able to do is stated in one place, and every tracker doc answers it. The basics: hold a ticket with a title and a line saying what done means, show whether it is not started, started, or done, and show who has taken it. The rest: say that one ticket waits on another, group tickets under a plan or a map, tell kinds of ticket apart, and, for a personal tracker, hold a link to a project ticket and find an item by it.
3. Never required to change. A tracker doc works with what the tracker already has. For each item beyond the basics it gives one of three answers: built in, kept as a line of text in the ticket, or not kept here. What is not kept here is kept in the personal tracker or in a file in the project. A tracker may be set up more richly. That is allowed and never required.
4. On a tracker other people share, the team's habits come first. A line of text playbook adds has to read as something a person would write.
5. One tracker, one doc. A tracker has one tracker doc, kept in one place, and every project that uses the tracker points at it. A personal tracker has its own. The decision on where a personal tracker is declared already says this.
6. The tracker docs playbook ships are options: for a person or a team with no tracker yet, and for those who want to adopt the pattern playbook uses. For anyone else, setup builds a tracker doc around the tracker they have.
7. Proved at setup. Setup tries each item on the list once against the real tracker before the doc is written, with reads where it can, and with one throwaway item, on the user's yes, where it must. When an operation fails later, the agent says so and offers to correct the doc.
8. Playbook does not connect tools. It says in plain words what it cannot reach, and checks that the tracker answers once the person has connected it. It carries no connecting steps of its own.
9. For teams as well. The remaining design is worked out for a team's shared tracker, not only for one person's use.

## Options considered

- A tracker doc may require ticket types, fields, or statuses to be set up first: not taken. Most people cannot change their team's tracker, and nobody should have to before they can start.
- No tracker doc, with the skills left generic: not taken. The agent would work the tracker out again in every session, slowly and differently each time.
- Step-by-step connecting instructions carried by playbook: not taken. They differ for every tool and every harness, and they change often.
- Designing for one person's use first: not taken. Playbook is meant to be offered to a team, and to people who are not technical.

## What settled it

- The skills collection playbook adapts from, read on 2026-11-21: it keeps a description of the tracker written at setup, needs only labels that it creates by itself, and falls back to a line of text where a tracker lacks a feature.
- A test on the four shipped trackers: where a link can be found differs for each, so a tracker doc has to say it for its own tracker.
- The person's view: the shipped tracker docs are options, and people use whatever tracker they have.

## Not settled here

- Where a team's tracker doc is kept when it is not in a repository, and how a project points at it. A separate question on the map holds these.
- What the Link label in a tracker doc says. A separate question holds it.
- Whether a tracker doc is called a recipe in what the user reads.
- Which tracker docs playbook ships. A ticket outside this map holds it.

## Replaces

In part, the decision that setup starts from how the person tracks their work (`2026-11-20-setup-starts-from-how-the-person-works.md`): its point on helping to connect. Setup says what it cannot reach and checks afterwards. It does not walk the person through connecting.
