---
name: new
description: >-
  Create a new project to the playbook standard, for any kind of work: a
  named folder under the projects root from the template, the standard files
  including a local copy of the conventions, project.yaml filled, the
  project's tracker set up, git initialized, worktrees ignored, a remote
  created (private unless the user decides it is internal or public), and a
  first commit pushed. Use when the user says "new project", "start a
  project", "create a repo for X", "set up a project for X", "scaffold a
  project to the standard", or when work that needs records has no
  repository yet. Do NOT use for an existing repository (that is adopt), for
  adding a worktree to a project, or for adding a ticket (that is capture).
---

# New project

Paths such as `references/conventions.md` are relative to the plugin's root
folder, two levels above this skill's folder.

## Procedure

1. Read `references/conventions.md` for the rules.
2. Locate the profile: the path in the environment variable
   `PLAYBOOK_PROFILE` when it is set and the file exists; else the path in
   the one-line file `.playbook` in the user's home folder; else the older
   `PROJECT_GUIDE_PROFILE` or `.project-guide`. If none exists, invoke the
   `profile` skill to create one, then continue with it.
3. Ask for the scope (from the profile's list), the subject, a human-readable
   title, a one-sentence summary saying what it is and who it is for, and
   whether it is private, internal, or public (private unless the user
   decides otherwise). Unless the user chose internal or public, which
   already counts as shared, ask once whether other people work on the
   project. For a project that will run as a service, ask for its owner.
   Ask which tracker holds its work (the profile's default unless the user
   names another) and the project's location in it. Build the name per the
   naming rule. Stop if a folder of that name already exists under the
   projects root.
4. Copy the plugin's `template` folder to `<projects_root>/<name>`.
5. In `project.yaml`, set `project` to the name, and `title`, `summary`, and
   `scope`, `owner` when the user named one, plus `visibility: internal` or
   `visibility: public` for an internal or public project. For a private
   project, add `shared: true` when other people work on it; otherwise leave
   that line out. Set `tracking` when the tracker is not the
   profile's default or its location is known; else leave it empty. Put the
   title and the summary in `README.md`.
6. Fill the base block and write the conventions copy with Python 3.9 or
   later: `python scripts/sync.py --repo <projects_root>/<name> --add
   --worktrees-dir <worktrees_dir>` (the script's path is from the plugin
   root), with the profile's worktrees folder (default `.claude/worktrees`).
   It sets the worktrees folder in the `AGENTS.md` block and writes
   `docs/project-conventions.md` at the standard version.
7. Set up the tracker by following `references/tracker-setup.md`: write
   `docs/tracker.md` when the project is shared or its tracker or layout
   differs from the user's default; otherwise make sure the user's doc for
   its kind exists.
8. Check that no `<...>` placeholder remains in `README.md`, `project.yaml`,
   `AGENTS.md`, `docs/tracker.md`, or the copy's first line (the rules and
   the tracker templates use `<...>` in examples).
9. Initialize git on `main`. Add to the `.gitignore` copied from the
   template a line that ignores the profile's worktrees folder.
10. For a public project, first run the cleaning pass from the conventions:
    nothing identifying in the files, the commit identity the user wants
    published, and a license the user picks. For an internal project, check
    the files against the internal rule. Then confirm with the user and
    create the remote, with the visibility the user chose, named after the
    folder, on the host and namespace the profile gives for the scope, and
    add it as `origin`.
11. Make the first commit, whether or not a remote exists. Push only when
    `origin` exists and the user confirms.
12. When another skill sent the user here because its work had no
    repository, return to that skill with the new project's path.

## Notes

- Creating the remote and pushing are outward-facing; each needs the user's
  go, for a public project too, after the cleaning pass. If the user
  declines the remote, leave the project local and say that it has no remote
  yet, which the standard requires.
- Never write credentials or data extracts into the new project.
