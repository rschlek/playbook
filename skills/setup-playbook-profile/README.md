# setup-playbook-profile

- Maintainer: the playbook plugin maintainers
- Origin: written for this plugin (first released in project-guide as `profile`; renamed `setup-playbook-profile` in playbook 1.0.1)

Sets up playbook for the user, once per machine. Creates, shows, or changes the user's profile: the one file per machine holding the projects root, the worktrees folder, scopes with their hosts, and the default tracker, plus an optional free-form `metadata` mapping the plugin never reads. It asks only what the user's request needs. It also sets up the user's tracker doc for the default tracker, `trackers/<kind>.md` beside the profile, by the shared procedure in `references/tracker-setup.md`. The other setup skills invoke it when no profile exists.

## Maintainer notes

- The profile is found through `PLAYBOOK_PROFILE` or the `.playbook` pointer, falling back to the older `PROJECT_GUIDE_PROFILE` or `.project-guide`; when only an old pointer exists, the skill offers to write the new one.
- The tracker setup steps live in `references/tracker-setup.md`, shared with new and adopt; change them there, not here.
- Shared files are named by their path from the plugin root; the SKILL.md says so once.
