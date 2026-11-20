# "Started on the user's yes" is a rule in the skill, not a setting

Question: How does the guard read that lets guide-me start wayfinder and grill-me only on the user's yes, in both harnesses?

Neither harness has a setting that means "only after the user agrees", so the guard is wording in the skills. `guide-me` asks one yes-or-no question and starts nothing before the yes. `wayfinder` carries a rule of its own and no longer carries the settings that let only the user start it. Version 1.0.3 was built and released this way.

## What was decided

1. Settings. No shipped skill carries the settings that mark a skill as started only by the user: `disable-model-invocation: true` in the frontmatter and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`. `wayfinder` was the only skill that had them, and they came off. `guide-me` and `grill-me` never had them.
2. The guard in `guide-me`: "Ask one yes-or-no question that names only the skill, such as "Start wayfinder now?", and end the turn on it. Start nothing before the user's yes, and never on your own initiative."
3. The guard in `wayfinder`: "Started on the user's yes. Never start this skill on your own initiative: charting creates tickets and commits an effort to several sessions. When you think a map is needed, offer it and wait for the user's yes."
4. `grill-me` carries no guard of its own. It asks questions and writes nothing. When `guide-me` offers it, the guard in `guide-me` applies.
5. What the yes covers. The yes given to `guide-me` covers starting the skill, as if the user had started it by name, so the started skill does not ask a second time whether to begin. It covers nothing inside that skill: every confirmation the skill has of its own still stands.
6. The rule in the repository's `AGENTS.md`. The sentence on a skill only the user may start stays, for a future skill that needs it. One sentence is added: a skill that changes things and may be offered by another skill carries a "started on the user's yes" rule in its body, and none of the settings for a skill only the user may start. This sentence is not in version 1.0.3. It is added with the work that follows this map.
7. Skills still to be built that another skill may offer, such as `define` and `to-questionnaire`, follow the same pattern.

## Options considered

- Keep the settings on `wayfinder`, and have `guide-me` tell the user to type its name: not taken. In one harness that setting blocks every start the user's own message does not name, so the entry point could point at the next skill and never start it.
- A setting that means "only after the user agrees": there is none in either harness.
- `guide-me` started only by the user: not taken. The agent may start it, and its triggers are kept narrow.
- A guard in the skills, with the settings removed: taken.

## What settled it

- The research in `docs/research/2026-11-19-skill-invocation-settings.md`.
- Test runs of the build before its release, in which `guide-me` ended on its question and started nothing.
- The release of version 1.0.3 with this wording.

## Not settled here

- How a `guide-me` session goes: what it looks at, what it says, and what it does on skip and when nothing fits. A separate question on the map holds it.

## Replaces

Nothing.
