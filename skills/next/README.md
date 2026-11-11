# next

- Maintainer: the playbook plugin maintainers
- Origin: written for this plugin in playbook 1.0.0

Tells the user where the current project stands in the playbook flow and which one skill to use next. It reads only: whether a profile, a `project.yaml`, and a tracker doc exist; any decision map and its open question tickets; any plan's parent ticket and its open work tickets; what is started or blocked. It answers in a few plain lines (where it stands, what is open, the one skill to use next and why) and changes nothing.

## Maintainer notes

- Read-only by design. It never starts work, picks a ticket (`tackle`), or walks decisions (`untangle`).
- The tracker doc is found through `references/tracker-lookup.md`, like every tracker-using skill.
- Its idea of the flow must match `docs/flow.md` and the flow lines in the base block of `template/AGENTS.md`.
- Model-invocable on purpose: "what's next" and "which skill do I use" are asked mid-conversation.
