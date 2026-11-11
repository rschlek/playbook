# adopt

- Maintainer: the playbook plugin maintainers
- Origin: written for this plugin (first released in project-guide, renamed in playbook 1.0.0)

Brings an existing repository up to the standard without moving or renaming anything: adds the missing standard files, places the base block and conventions copy (through `scripts/sync.py --add`, which also replaces a block or copy from the earlier project-guide standard), fills `project.yaml` from what the repo shows, sets up the project's tracker, and reports every remaining gap.

## Maintainer notes

- Tracker setup follows `references/tracker-setup.md`, shared with profile and new.
- In a repo someone else owns, everything added stays local in the exclude file.
- Shared files are named by their path from the plugin root; the SKILL.md says so once.
