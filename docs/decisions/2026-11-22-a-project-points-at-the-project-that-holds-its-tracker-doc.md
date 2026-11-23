# A project points at the project that holds its tracker doc

Question: How does a project point at the project that holds its tracker doc, and where does a person record that when the project's shared files cannot?

A project tracker's doc is a file in a repository the team shares. A project that does not hold the doc names the project that does, in one line of its `project.yaml`. When the project's shared files cannot carry that line, the person's profile carries it. The doc is read from the named project's checkout and never copied.

## What was decided

1. The home is a repository. A project tracker's doc is `docs/tracker.md` in one project the team shares: one of its working projects, or a project kept only for this. It is not kept in a shared folder outside a repository, or on a web page.
2. The pointer. In `project.yaml`, a tracker entry under `tracking` may carry `doc`, the slug of the project whose `docs/tracker.md` describes that tracker. `ref` stays the project's own location in the tracker. A project that points carries no `docs/tracker.md` of its own.

```yaml
tracking:
  primary:
    kind: example-tracker
    ref: EXAMPLE              # this project's location in that tracker
    doc: team-handbook        # the project whose docs/tracker.md describes the tracker
```

3. When the shared files cannot carry it. Where the team does not use playbook, or the repository is someone else's, the project's entry in the profile's `projects` mapping carries a `tracking` block of the same shape. It is read only when the project's `project.yaml` has no `tracking`.

```yaml
tracker:
  kind: example-list
  personal: true
  projects:
    example-project:
      ref: EXAMPLE            # where this project's items sit in the personal tracker
      tracking:               # the project tracker, when the project's shared files cannot say
        primary:
          kind: example-tracker
          ref: EXAMPLE
          doc: team-handbook
```

4. The order a skill finds the doc in:
   1. the repository's own `docs/tracker.md`;
   2. else `tracking` in `project.yaml`, else `tracking` on the project's entry in the profile: for an entry with `doc`, the named project's `docs/tracker.md`, and for an entry without it, the person's doc for that kind beside the profile, as today;
   3. else the profile's default tracker, as today;
   4. else it stops and asks for tracker setup. It never guesses.
5. Reached on a machine. The named project is a checkout under the projects root, like any other project. The doc is read from there each time. No copy is made in the pointing project or beside the profile.
6. Kept current. Once in a session, at the first lookup, the skill checks whether that checkout is behind its remote. The check changes no file. When it is behind, the skill says so in one line and updates the checkout on the user's yes. When the check cannot run, it reads the checkout as it is and says so once.
7. Missing or out of reach. When the named project is not on the machine, the skill says which project is needed and offers to get it, asking for the repository's address when it does not know it. When the person has no access, it says so and stops. It never falls back to another tracker's doc.
8. Changing the doc. The doc changes in its home project, through that project's normal review. A skill working in another project that finds a line of it wrong shows the corrected text and makes the change in the home project on the user's yes.
9. Setup. When a project's tracker is defined, setup asks whether a doc for that tracker already exists in another project. On a yes it writes the pointer and no doc.

## Text that changes

With the work that follows this map:

- The conventions: the sentence that a shared project carries `docs/tracker.md` gains "or points at the project that holds it", the sentence on where docs live says the same, the order for finding a doc reads as point 4, and the rule for a repository someone else owns says the pointer goes on the project's entry in the profile.
- `references/tracker-lookup.md`, "Find the doc": the order in point 4, with points 5 to 7.
- The template `project.yaml`: a commented `doc` line under each tracker entry.
- Setup: point 9, and the `tracking` block on a project's entry in the profile.

## Options considered

- A shared folder that syncs to each computer, or a web page: not taken. Every other playbook document is a file in a repository, and a repository shows what changed.
- A link under `links` in `project.yaml`: not taken. `links` joins related projects for a reader, and the lookup needs one fixed place.
- A local `docs/tracker.md` kept out of git, where the shared files cannot carry a pointer: not taken. A fresh worktree does not have it, and it is a copy.
- The doc copied at a pinned version: not taken. Copies drift, and the earlier decision ruled out carrying one.
- Updating the checkout without asking: not taken. It changes files the person may be working in.

## What settled it

- The person's view: a repository fits the pattern playbook follows everywhere else.
- The decision on where a personal tracker is declared: one home for a tracker doc, pointed at and never copied.
- The profile is present in every worktree, and a file git ignores is not.

## Not settled here

- How a team that does not work with repositories gets one for a project and shares it. A ticket outside this map holds it.
- Whether the tracker docs playbook ships move to a repository of their own. They stay in playbook for now. A ticket outside this map holds when to look again.

## Replaces

Nothing.
