# Setup starts from how the person tracks their work

Question: How does a person set up a personal tracker: in the existing setup skill or one of its own, and what do they define for themselves?

Replaced in part by: 2026-11-22-a-tracker-doc-never-requires-the-tracker-to-change.md. Setup does not walk the person through connecting a tool; it says what it cannot reach and checks afterwards.

In the existing setup skill. Setup opens by asking the person how they keep track of their work, in plain words, and what it learns sets up their personal tracker. A project tracker is not set up there: it is defined in each project.

## What was decided

1. One skill. A personal tracker is set up in `setup-playbook-profile`. There is no skill of its own for it.
2. It opens with an open question, such as "How do you usually keep track of your work?", and listens. It does not open by asking which tracker the person uses.
3. What the person says sets up their personal tracker, the place where their own tasks live. When they keep a list of their own, setup marks the profile's tracker as the person's own, as the decision on where a personal tracker is declared says. A person who keeps no list is not pushed toward a tool: setup offers the simplest tracker playbook ships a template for, and a no is accepted.
4. The project tracker is defined in each project, not in setup. A project says which tracker it uses, and that tracker's doc has its home in a project. A person who works in a project gets its tracker from the project. When they cannot reach it yet, the agent says so in plain words the first time they work there, and helps them connect.
5. Helping to connect. When a tool the person uses is not connected, setup walks them through connecting it and checks that it works by reading from it. The person does every sign-in. Playbook stores no password and no key. Exact steps exist for the trackers playbook ships templates for. For another tool, setup says what kind of connection is needed.
6. A tool with no shipped template. Setup looks at what the tool can do, tries it with reads that change nothing, and builds the tracker doc with the person.
7. What the person defines for themselves: where items for a project go, where an item with no project goes, how an item shows it is started, and any rules of their own. Setup suggests an answer for each. The template gives the rest: how the tool is operated.
8. Plain words. Setup uses the person's own names for their things and asks about habits, not settings. A playbook word appears only when the person will need it later, and it is explained once. Setup shows back what it understood in plain sentences and writes on the person's yes. The tracker doc it writes is shown when the person asks.
9. A person who is already set up and later wants a personal tracker is asked only what is new.
10. The plain-words rule also holds for `guide-me`, the other place a newcomer lands. It is checked when that skill is next changed.

## Options considered

- A skill of its own: not taken. A personal tracker is the profile's tracker with a mark on it, so most of its steps would repeat setup's, and a newcomer would have to know a second name.
- One added question in setup, "Is this your own list?": not taken. It asks the person to think in playbook's terms.
- Setup also sets up the team's tracker: not taken. A project tracker belongs to its project.
- Setup opens with how the person works: taken.

## What settled it

- The person's view: asking how someone tracks their work sets up the personal tracker, the project tracker is defined per project, and a new user does not know playbook's words.
- The decision on where a personal tracker is declared, which made it the profile's one tracker with a mark.

## Not settled here

- How a project points at the project that holds its tracker doc. A separate question on the map holds it.
- What the Link label in a tracker doc says. A separate question holds it.
- Which templates and connection steps playbook ships for trackers. A ticket outside this map holds it.

## Replaces

Nothing.
