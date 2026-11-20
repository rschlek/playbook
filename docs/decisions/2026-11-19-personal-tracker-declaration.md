# Where a personal tracker is declared and when it is used

Question: Where is a personal tracker declared, and what switches it on over a project's tracker?

A person declares a personal tracker by marking the profile's one `tracker` entry with `personal: true`. The same entry holds, per project, where that project's items sit in the personal tracker. Once marked, the personal tracker is used with every project whose tracker is not the personal tracker itself. Two trackers of one kind are told apart by where their tracker docs live, never by kind.

## What was decided

1. Declared on the existing entry. The profile keeps one `tracker` entry, still the default for a project that declares no tracker. The line `personal: true` says this tracker is the person's own list and may sit on top of a project tracker. Without the line, nothing changes from before this decision.
2. The per-project location is in the profile. The entry carries a `projects` mapping keyed by project slug. A project's `ref` is where its items sit in the personal tracker. A project with no entry has no place of its own: its items go where the personal tracker doc's New ticket role puts them.
3. Used with every project. With `personal: true` set, the personal tracker is used with every project whose tracker is not the personal tracker itself. A project is left out by `personal: false` on its entry. A project that declares no tracker uses the profile's tracker directly, as before, and nothing is layered.
4. Told apart by where the tracker doc lives. The doc beside the profile for the profile's tracker kind always describes the personal tracker. A project tracker's doc has one home, a project: a team with one project keeps it in that project's `docs/tracker.md`, and a team with several keeps it in one project, which the others point at without carrying a copy. A project whose tracker resolves to the person's own doc for the profile's tracker is using the personal tracker itself. Docs filed beside the profile by kind, and repositories that already carry `docs/tracker.md`, keep working.

```yaml
tracker:
  kind: example-tracker
  url: https://tracker.example.com/browse/{key}
  personal: true              # this tracker is the person's own list
  projects:                   # keyed by project slug
    example-project:
      ref: EXAMPLE            # where this project's items sit in the personal tracker
    another-project:
      personal: false         # the personal tracker is not used with this project
```

The profile is one file per person on each machine, so all of this is set per machine.

## Options considered

- The default tracker doubles as the personal tracker with no marker: not taken. A person who only wanted a fallback would get two-tracker behaviour without asking, and their default may be a tracker other people see.
- A separate personal tracker entry in the profile: not taken. In the common case it repeats the default's kind and URL, and it leaves open what the default is for.
- One entry with an explicit marker: taken.
- The per-project location in `project.local.yaml`: not taken. Git ignores the file, so a fresh worktree does not have it.
- The per-project location in the profile: taken.
- The personal tracker used only with projects that have an entry: not taken. Until the entry exists, work goes straight to the project tracker, where it cannot be taken back.
- The personal tracker used with every project, with a per-project opt-out: taken. A forgotten setup keeps items personal, and sharing later is cheap.
- A copy of the project tracker's doc in every repository of a team: not taken. The copies drift, and almost nothing in a tracker doc differs between a team's projects except the project's location, which `ref` already holds.
- Tracker docs filed under a name the person chooses: not taken. It changes how every existing doc is found, and where a doc lives already tells two of one kind apart.
- A project of its own required for every tracker doc: not taken. A person with one project would need a second repository only to hold the doc, and a team may already have a shared project the doc fits in. A dedicated project is allowed.
- One home per tracker doc, told apart by where it lives: taken.

## What settled it

- The glossary defines a personal tracker as one person's list across every project they work on. The profile's default tracker already does that job, so one entry serves both.
- A person with no personal tracker must see no change. An explicit marker gives that.
- `project.local.yaml` is ignored by git, and a new worktree holds only tracked files.
- The conventions already say code has one home and is referenced, never copied. The same rule fits a tracker doc.

## Not settled here

- How a project points at the project holding its tracker doc, what a person does when a team's projects cannot carry that pointer, and how the doc is kept current on each machine. A separate question on the map holds these.
- With "every project", a project that is one person's alone and declares its own tracker gets the personal tracker on top unless its entry says `personal: false`.

## Replaces

Nothing.
