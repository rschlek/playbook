# Nothing runs between sessions to catch a linked pair out of step

Question: What catches a linked pair that drifted while no session was looking?

Playbook ships nothing that runs outside a session. A pair that drifted is caught by the check the work skills run at the first tracker use in the person's next session. Until then the project ticket may be out of date, and that is accepted.

## What was decided

1. Nothing ships that runs on a schedule or in the background. Playbook adds no hook, no job, and no service for this.
2. The next session catches it. The check for pairs out of step runs by itself, once per session, as the decision on keeping a linked pair in step says. A person can also ask for it at any time: `guide-me` runs it.
3. A person may run the check on a schedule of their own. That is their setup on their machine, not part of playbook. Run with no person present, the check may read both trackers and prepare a list of differences. It writes to neither tracker: every change still waits for the person's yes.

## Options considered

- A check on a schedule, shipped with playbook, that notices and prepares a list for one approval: not taken. A schedule belongs to one machine and one harness, so one plugin cannot ship it for everyone, and it would only prepare a list, so the project ticket waits for the person either way.
- A check of its own that the person runs by name: not taken. `guide-me` already runs the check when asked.
- Nothing more than the next session's check: taken.

## What settled it

- The person's view: when they are doing the work, tickets that drift a little are not a problem, and whoever wants a schedule can set one up.
- Playbook ships no hooks, and a schedule is specific to a machine and a harness.
- An earlier ruling said no background sync job is built. The case that reopened it, a project ticket left unstarted after one of its linked items was finished with no agent involved, is now caught by comparing states at the next session.

## Not settled here

- How a person sets up a schedule of their own, if they want one. Playbook does not describe it.

## Replaces

Nothing. It confirms the earlier ruling that no background sync job is built.
