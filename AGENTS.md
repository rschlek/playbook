# Working in this repo

- This repo is a plugin for Claude Code and Codex. Consumers install it from its remote on the `stable` ref. Work lands on `main`; promote `main` to `stable` deliberately, never as a side effect. A release bumps `version` in both manifests.
- Everything here is public and generic: no person, company, team, host, machine, absolute path, private tool, or real URL. Say "the user", "the tracker", "the memory system", "the profile". Machine-specific values belong in a profile, not in this repo. The exceptions are the `author` field in the plugin manifests and this repository's own public URL (https://github.com/rschlek/playbook), which the template and the sync script write into every project. A public tool the standard recommends, or a skill adapted from one, may be credited by its author's public name and its repository link, and an adapted skill's README keeps its MIT attribution.
- Tracker products are named only in the tracker templates under `references/trackers/` and in lists of the shipped templates. Skills name no tracker product; they read the tracker doc.
- Skills never tell the agent to read, write, or update agent memory. Memory is a separate workflow that this plugin does not direct.
- This repository is the source of the standard, so it carries no `docs/project-conventions.md` copy of its own.
- Any change to the rules in `references/conventions.md` gets a dated entry in `references/changelog.md`.
- The version in the base block's start marker in `template/AGENTS.md` is the standard version, and the skills and `scripts/sync.py` read it from there. In a release, set it (in the marker and in the sentence below it) to the release version only when that release changes the base block text or `references/conventions.md`; otherwise leave it, so adopted repos need no update.
- No em dashes. Plain sentences.

## Skills

Each skill is a folder `skills/<name>/` holding:

- `SKILL.md`: frontmatter `name` equal to the folder name, and a `description` rich in the phrases a user says, which also says what the skill is NOT for, pointing at sibling skills by bare name. Keep the body under about 100 lines; move detail into a file beside it.
- `README.md`: what the skill is, its source and credit when it was adapted, and maintainer notes.
- `agents/openai.yaml`: Codex metadata, an `interface` with `display_name`, `short_description`, and optionally `default_prompt`. A skill only the user may start sets `policy.allow_implicit_invocation: false` there and `disable-model-invocation: true` in its frontmatter.

Every skill works in both harnesses from the same `SKILL.md`:

- Name another skill as "invoke the `<name>` skill", never by a harness tool or a slash command.
- Name a shared file by its path from the plugin root, such as `references/conventions.md`, and say once per skill that such paths are relative to the plugin's root folder, two levels above the skill's own folder. Name a file bundled beside the skill by its path relative to the skill's folder. Never use a harness-specific variable for the plugin root.
- Where a step wants a fresh-context subagent, say what to do when the harness has none: do it inline, one item at a time.
- Add no hooks.
