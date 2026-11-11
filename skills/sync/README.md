# sync

- Maintainer: the playbook plugin maintainers
- Origin: written for this plugin (first released in project-guide, renamed in playbook 1.0.0)

Runs `scripts/sync.py` across the projects root: plans first, shows the user, then writes, commits by path, and pushes on the user's go. A repo other people use gets a review branch, `standard/playbook-<version>`, and a pull request. Repos adopted under the earlier project-guide standard are migrated: their old block and copy are replaced, never duplicated.

## Maintainer notes

- The script recognises both `project-guide:base` and `playbook:base` markers and both copy headers.
- Behaviour beyond the rename and migration is unchanged from project-guide 0.9.0.
- Shared files are named by their path from the plugin root; the SKILL.md says so once.
