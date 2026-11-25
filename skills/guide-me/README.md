# guide-me

- Maintainer: the playbook plugin maintainers
- Origin: grew from this plugin's `next` skill, written for playbook 1.0.0; renamed `guide-me` in playbook 1.0.3

Tells the user where the current work stands in the playbook flow, names the one skill that fits next and why, and on the user's yes starts it. It looks first, reading only: whether a profile, a `project.yaml`, and a tracker doc exist; any decision map and its open question tickets; any plan's parent ticket and its open work tickets; what is started or blocked. It answers in about five plain lines, not a list (where it stands, what is open as counts with at most three tickets named by title, the one skill that fits and why), then asks one yes-or-no question: start that skill now? On a skip it names the next skill that fits. When the started skill ends in the same session, it looks again and offers the following one.

It is the `next` skill with an offer and a start added: the look is the same, and so is the rule of one skill, not a menu.

## Maintainer notes

- The promise: it changes nothing until the user's yes, and after the yes the started skill does the changing, not this one. The yes covers starting the skill only; every confirmation inside that skill stays with it.
- New work with no problem definition is offered `define` first, whether the user has a loose want or a specific build in mind. Before `define` existed, that row sent a loose want to `grill-me`, which stays the skill for testing a plan the user already has. Whether a problem definition exists is one listing of the project's `docs/problems/` folder and no more. It is offered, never forced: a skip moves to the next row, as for every row.
- The trigger list deliberately excludes a bare "I want to ...": it would fire on ordinary requests. Only phrases about being unsure where to start or what comes next are listed.
- It never picks a ticket (`tackle`) or walks decisions (`untangle`); it offers those skills. It does not choose which question on a map comes next either: that is `wayfinder`'s Frontier query.
- The Look is kept to about five tracker calls with no subagent and no per-ticket fetches: a first real use spent four list calls, a search, a get, and a subagent on it, and later test runs fetched each question's links one by one. The map's Frontier query is one of those calls and is never skipped: without it the Point cannot say how many questions can be taken now. When a tracker's Frontier query needs links read ticket by ticket and the tool cannot list them in one call, the Point gives open and claimed counts only.
- A map whose Frontier query returns nothing is waiting on its claimed questions, so `wayfinder` is not offered for it; the next row that fits is.
- It never calls a claim stale: a ticket started under the user's own name may be another session's live work.
- The tracker doc is found through `references/tracker-lookup.md`, like every tracker-using skill.
- Its idea of the flow must match `docs/flow.md` and the flow lines in the base block of `template/AGENTS.md`.
- Model-invocable on purpose: "what's next" and "which skill do I use" are asked mid-conversation, in plain words.
