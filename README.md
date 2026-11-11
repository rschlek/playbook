# Playbook

How a project is set up and how work moves through it, packaged as a plugin for agent harnesses (Claude Code and Codex). It works for any kind of project, not only software: a compliance process, life admin, or a research question gets the same home and the same loop as a code base.

## Install

Playbook needs git and Python 3.9 or later on the machine (the setup skills run `scripts/sync.py`), and the `gh` command line where a project uses GitHub Issues or a GitHub remote.

```bash
# Claude Code
claude plugin marketplace add https://github.com/rschlek/playbook.git
claude plugin install playbook@playbook

# Codex
codex plugin marketplace add https://github.com/rschlek/playbook.git
codex plugin add playbook@playbook
```

A local checkout works the same way: pass its folder to `marketplace add`. Start a new session afterwards.

## First run

1. Invoke the `setup-playbook-profile` skill. It asks which tracker you use and sets up a tracker doc for it; that is all everyday work needs. No tracker yet? Choose `markdown`: tickets are files in a repository, and nothing else is needed.
2. Everyday tickets (an errand, a chore, a one-off task) need no repository and no project: `capture` and `tackle` work with the tracker doc alone.
3. When you start an initiative that produces something and has decisions worth recording, invoke `new` for it, or `adopt` in a repository you already have. Its records (decisions, glossary, research) live in that repository.
4. Invoke `next` whenever you are unsure what to do: it says where things stand and which skill comes next.

## The flow in short

```
an idea -> grill-me (sharpen it) -> wayfinder (map it, only if foggy)
        -> to-tickets (plan and work tickets) -> tackle (do each one)
        -> close the parent
at any time: capture a stray item, untangle when lost, next when unsure
```

Work you already understand skips the map; a single small job is just `capture` and `tackle`. [docs/flow.md](docs/flow.md) walks the whole flow with a worked example, a table of every skill, and how to set up.

A project keeps three things apart (a standalone ticket lives only in the tracker):

- **The repository** holds the work itself and the project's own context: its documents, its decisions (one file each), and its research.
- **The tracker** holds the items of work, including the plan for a piece of work, which lives in the parent ticket. A **tracker doc** tells an agent how to read and write tickets in that tracker and what each step of the loop means there.
- **Agent memory** is outside this plugin's scope.

## What is here

- `references/conventions.md`: the standard. Every adopted project carries a copy.
- `references/trackers/`: tracker doc templates for Todoist, OpenProject, GitHub Issues, tickets kept as Markdown files in the repository, and a blank one for any other tracker.
- `references/tracker-setup.md`: how a tracker doc is set up, shared by the setup skills.
- `references/tracker-lookup.md`: how every tracker-using skill finds and reads the tracker doc.
- `references/profile.example.yaml`: the shape of the profile, one per user on each machine, that holds the projects root, the worktrees folder, scopes and their hosts, and the default tracker.
- `references/changelog.md`: changes to the standard.
- `template/`: the files a new project starts from.
- `scripts/sync.py`: places, compares, and updates the base block and the conventions copy; the setup skills run it. It also migrates a repository adopted under the earlier project-guide standard.
- `docs/flow.md`: the flow, a worked example, and which skill to use when.
- `agents/standards.md`: an agent that runs the heavy phases of the setup skills across many repositories, for harnesses that load agents from a plugin; elsewhere the skills do the same work inline.

## Skills

Set up a project:

- `setup-playbook-profile`: set up playbook for the user, once per machine: create, show, or change the profile, and connect the tracker through a tracker doc checked against the live tracker.
- `new`: create a new project to the standard, its tracker doc included.
- `adopt`: bring an existing repository up to the standard in place, and set up its tracker.
- `sync`: bring every adopted project's base block and conventions copy up to date in one run, migrating project-guide repositories.

The work loop:

- `wayfinder`: chart a large or foggy piece of work as a decision map in the tracker, one question ticket per open question, and resolve them one at a time. Started by the user only. When the last question is answered it asks whether to create the tickets now.
- `to-tickets`: turn a finished plan into a parent ticket holding the plan and the work tickets under it, in order, with blocking, then close the map. It shows everything first and creates nothing before the user's yes.
- `capture`: add one well-formed ticket to the right tracker and place.
- `tackle`: do a ticket the user names, or pick one worth doing now, and close it out honestly.
- `next`: say where the project stands in the flow and which one skill to use next, changing nothing.

Thinking:

- `grill-me`: stress-test a plan by being asked about it, one question at a time.
- `glossary`: pin down the project's words in its glossary, and record a hard-to-reverse decision when one comes up.
- `research`: investigate one question from primary sources and write the findings, cited, as a dated document under `docs/`.
- `prototype`: build something rough and throwaway to react to, so one design question gets answered.
- `untangle`: when the user is lost, say it plainly and turn a pile of findings into small decisions, one at a time.

## Profile

The skills find the user's profile on this machine through the environment variable `PLAYBOOK_PROFILE`, or else a one-line file `.playbook` in the home folder containing the profile's path. When neither exists they fall back to the older `PROJECT_GUIDE_PROFILE` and `.project-guide`, so a profile written for project-guide keeps working; the `setup-playbook-profile` skill offers to write the new pointer. The `setup-playbook-profile` skill creates the profile from a few questions; or start from `references/profile.example.yaml`. The user's tracker docs sit beside the profile file, in `trackers/<kind>.md`.

## Upgrading from project-guide

Playbook replaces the project-guide plugin. Run the `sync` skill once: it replaces each adopted repository's `project-guide:base` block and project-guide conventions copy with the playbook ones. Existing `docs/plan/` files and a single `docs/decisions.md` stay as history.

## Credit

The `wayfinder`, `grill-me`, `glossary` (upstream `domain-modeling`), `research`, `prototype`, and `to-tickets` skills are adapted from Matt Pocock's skills (https://github.com/mattpocock/skills), MIT licensed. Each adapted skill's README names its source, and [LICENSE](LICENSE) reproduces the upstream copyright and permission notice.
