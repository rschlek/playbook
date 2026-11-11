# new

- Maintainer: the playbook plugin maintainers
- Origin: written for this plugin (first released in project-guide, renamed in playbook 1.0.0)

Creates a new project under the projects root from the plugin's `template` folder: the standard files, a filled `project.yaml`, the base block and conventions copy (through `scripts/sync.py --add`), the project's tracker doc when it needs its own, git, a remote with the visibility the user chose, and a first commit. Works for any kind of project, code or not.

## Maintainer notes

- Tracker setup follows `references/tracker-setup.md`, shared with profile and adopt.
- Creating a remote and pushing always wait for the user's go.
- Shared files are named by their path from the plugin root; the SKILL.md says so once.
