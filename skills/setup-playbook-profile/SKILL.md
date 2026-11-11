---
name: setup-playbook-profile
description: >-
  Set up playbook for the user, once per user on each machine: create, show,
  or change the user's profile (the default tracker, and the projects root
  and scopes when a project needs them), and connect the tracker by writing
  its tracker doc, checked against the live tracker. Use when the user says
  "set up playbook", "connect my tracker", "set up my tracker", "change my
  tracker", "show my profile", "change my projects root", on first use of
  the plugin with no tracker doc, and when another skill finds no profile or
  no tracker doc. Do NOT use to create a project (that is new), to bring an
  existing repository to the standard or change its project.yaml or own
  tracker doc (that is adopt), or to store credentials.
---

# Setup playbook profile

This skill creates, shows, and changes the profile; the profile file itself
keeps its name and lookup.

Paths such as `references/conventions.md` are relative to the plugin's root
folder, two levels above this skill's folder.

## Procedure

1. Read "The profile" and "Trackers" in `references/conventions.md`, and
   `references/profile.example.yaml` for the shape.
2. Locate the profile: the path in the environment variable
   `PLAYBOOK_PROFILE` when it is set; else the path written in the one-line
   file `.playbook` in the user's home folder; else, from the earlier
   project-guide standard, the path in `PROJECT_GUIDE_PROFILE` or in
   `.project-guide`. When it was found only through an older pointer, offer
   to write `.playbook` holding the same path; write it on a yes and leave
   the old pointer in place. Then do what the user asked: create the profile
   when it is missing, show it, change one value, or set up the tracker.
3. Create. Ask only what the user's request needs, in one batch, offering
   the example's defaults: for tracker setup alone, only `tracker`; the
   rest when a skill that needs it (new, adopt, sync) asks.
   - `projects_root`: the one flat folder holding every project.
   - `worktrees_dir`: where worktrees nest inside a project (default
     `.claude/worktrees`).
   - `scopes`: for each, a name, its meaning, whether it is a name prefix,
     and the remote host and namespace its projects go to.
   - `tracker`: the default tracker's kind (a shipped template in
     `references/trackers/`, or any other name for a tracker without one)
     and its URL pattern with `{key}`.
   - `shared_namespaces`, optional: remote namespaces of repos other people
     use, so sync sends their updates through review.
   Ask where to keep the file when the environment variable does not name
   one (suggest `.config/playbook/profile.yaml` in the home folder, since
   the tracker docs go in a `trackers` folder beside it). Write it in the
   example's shape and order, with only the user's answers (and any
   `metadata` mapping the user gives, never read by the plugin), then write the
   one-line `.playbook` pointer holding its path, unless the environment
   variable already names it. Show the result, then set up the tracker
   (step 6).
4. Show. Print the profile's values grouped as in the example, say which
   file they came from and how it was found, and list the tracker docs in
   the `trackers` folder beside it.
5. Change one value. Show the current value and the new one, write only that
   key, and leave every other line, comment, and the file's line endings as
   they are. A changed `projects_root` or `worktrees_dir` moves nothing on
   disk: say so, and that existing projects and worktrees stay where they
   are until the user moves them. A changed `tracker.kind` goes on to
   step 6 when no doc exists for the new kind.
6. Set up the tracker. Follow `references/tracker-setup.md` for the
   default tracker's kind, writing `trackers/<kind>.md` in the folder that
   holds the profile. Running it again updates that doc in place. When
   there is no profile and the user wants none, and the work is in a
   repository, write `docs/tracker.md` there instead.
7. When another skill called this one, return to that skill's next step
   with the profile's path.

## Notes

- One profile per user on each machine. It and the tracker docs beside it
  hold locations, names, and rules, never credentials, tokens, or
  passwords; for a tracker that needs a key, it names the location only.
- An older profile's `memory` section is left as it is; nothing reads it.
- Never create the profile or a user-level tracker doc inside a project's
  repository, and never commit either.
- Writing the profile, the pointer file, or a user-level tracker doc
  changes only those files; nothing under the projects root is touched.
