---
name: adopt
description: >-
  Bring an existing repository up to the playbook standard in place: add the
  missing standard files, fill project.yaml from what the repo already shows,
  set up the project's tracker, and report every gap against the standard
  without moving or renaming anything. Use when the user says "adopt this
  repo", "bring this project up to the standard", "add a project.yaml",
  "make this repo conform", "set up the tracker for this project", or "check
  this repo against the standard". Do NOT use for creating a new project
  (that is new), for updating the base block across many repos (that is
  sync), or for moving or renaming a repository.
---

# Adopt a repository

Paths such as `references/conventions.md` are relative to the plugin's root
folder, two levels above this skill's folder.

## Procedure

1. Read `references/conventions.md` for the rules.
2. Locate the profile: the path in the environment variable
   `PLAYBOOK_PROFILE` when it is set and the file exists; else the path in
   the one-line file `.playbook` in the user's home folder; else the older
   `PROJECT_GUIDE_PROFILE` or `.project-guide`. If none exists, invoke the
   `profile` skill to create one, then continue with it.
3. Look at the repo: folder name, the `origin` remote, README, existing agent
   files, `.gitignore`, any existing `project.yaml`, and any existing tracker
   doc (`docs/tracker.md`, or a doc another tool left describing the issue
   tracker). The tree is clean when no tracked file is modified or staged;
   untracked files do not block. If it is not clean or another session
   appears to be working in the repo, stop and report before writing.
4. Decide ownership from the namespace of `origin`: the user's own repo, a
   shared repo the user leads, or a repo someone else owns (see "Repos shared
   with other people" in the conventions). When it is not evident, ask.
5. Add whichever of `README.md`, `CLAUDE.md`, and `project.yaml` are missing,
   from the plugin's `template` folder. Never overwrite an existing README
   or agent file. A `CLAUDE.md` whose only content is `@AGENTS.md`, blank
   lines aside, already conforms. If a long `CLAUDE.md` exists with no
   `AGENTS.md`, propose moving its content into `AGENTS.md` and ask first.
6. Place the base block and the conventions copy with Python 3.9 or later:
   `python scripts/sync.py --repo <path> --add --worktrees-dir
   <worktrees_dir>` with the profile's worktrees folder (default
   `.claude/worktrees`). In a repo someone else owns whose `AGENTS.md` is
   tracked, add `--copy-only` so that file stays untouched, and report the
   missing block instead. The script creates a missing `AGENTS.md`, inserts
   a missing block, replaces an older block or copy (or one from the earlier
   project-guide standard) whole, keeps line endings, and reports a newer
   one, malformed markers, or a copy without the standard header. Relay
   what it reports.
7. Fill `project.yaml` from what the repo shows: `project` from the repo
   name (of `origin`, else the folder name); `title` from the README's first
   heading, left out when there is none or it only repeats the slug; `scope`
   from a scope the profile marks as a prefix when the folder name starts
   with it, else the one scope whose host and namespace match `origin` (when
   several or none match, or there is no `origin`, leave it empty and ask,
   offering any matches); `summary` drafted from the README and confirmed
   (unconfirmed drafts are written and listed as such). Ask if the repo is
   private, internal, or public, and record `visibility: internal` or
   `public` as confirmed. Unless `visibility` already counts as shared or
   someone else owns the repo, ask once whether other people work on it and
   on a yes set `shared: true`. For a service, ask for `owner`. Leave
   unknown fields empty. In an existing `project.yaml`, fill only empty
   fields and propose changes: `parent` and `links` for `repo_role` and
   `repos`, and `paused` for `parked`. Leave `metadata`, and any older
   field such as `memory`, untouched.
8. Set up the tracker. Ask which tracker holds this project's work, offering
   what `tracking`, an existing tracker doc, or the remote suggests, and the
   project's location in it. Then follow `references/tracker-setup.md`:
   write `docs/tracker.md` when the project is shared or its tracker or
   layout differs from the user's default; otherwise make sure the user's
   doc for its kind exists. An existing tracker doc is a starting point:
   propose carrying its content over, and leave the old file as it is.
9. If the profile's worktrees folder or `project.local.yaml` is not
   ignored, add the ignore line: in `.gitignore` in the user's own repo, in
   the local exclude file in a shared repo. In a repo someone else owns,
   also list the added standard files, the conventions copy and any
   `docs/tracker.md` included, in the local exclude file.
10. Check that no `<...>` placeholder remains in an added or changed
    `README.md`, `project.yaml`, `AGENTS.md`, `docs/tracker.md`, or the
    copy's header line.
11. Report the gaps against the standard: no remote, a name off the naming
    rule, a repo not directly under the projects root or nested in another,
    committed credentials, or, in a public repo, no license or an unwanted
    commit identity. Report `docs/plan/` files or a single
    `docs/decisions.md` as history that stays; never rename, move, or
    convert documents. Say which files were added or updated and their fate:
    uncommitted in the user's own repo; uncommitted for review, with only
    fields true for everyone, in a shared repo the user leads; excluded and
    never committed in a repo someone else owns.

## Notes

- Change nothing beyond adding files, the base block, the conventions copy,
  the tracker doc, `tracking`, and ignore lines unless the user agrees.
- Never move or rename the repository, or change its visibility. Added
  files follow the repo's own line-ending and formatting rules. In a shared
  repo, ignore lines go in the local exclude file, never `.gitignore`.
