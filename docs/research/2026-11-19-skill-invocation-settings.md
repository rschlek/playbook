# Skill invocation settings in Claude Code and Codex

Date written: 2026-11-19. All documentation pages were read on that date.

## Question

The playbook plugin marks a skill that only the user may start with `disable-model-invocation: true` in the skill's `SKILL.md` frontmatter (read by Claude Code) and `policy.allow_implicit_invocation: false` in the skill's `agents/openai.yaml` (read by Codex). What does each setting do in its own harness, and can one skill start another skill that carries it? In particular: is there a way to say "the model may start this, but only after the user agrees"?

## Side by side

| Point | Claude Code: `disable-model-invocation: true` | Codex: `policy.allow_implicit_invocation: false` |
| --- | --- | --- |
| What it blocks | Claude cannot invoke the skill "on its own". The skill's description is not put in Claude's context. The skill is also not preloaded into subagents and does not run when a session-scoped scheduled task fires with it as the prompt. | Codex "won't implicitly invoke the skill based on user prompt", meaning it will not pick the skill because the task matches its description. |
| What it leaves possible | The user can still start it with `/name` (at the start of a message). The skill loads in full when invoked. Naming `/name` as a separate word later in a message counts as the user's permission for that message. | Explicit `$skill` invocation "still works". |
| Default when absent | `false`: both the user and Claude can invoke the skill; the description is in context. | `true`: Codex may select the skill implicitly from its description. |
| Skill-to-skill (A tells the agent to start B, B is user-only) | Not documented. See notes below. | Not documented. |
| Confirm-first mode ("model may start it, only after the user agrees") | No dedicated frontmatter value. A permission `ask` rule on the Skill tool is the nearest documented mechanism (see below, not verified for the Skill tool). | No documented confirm mode. Only two states: implicit allowed or not. |
| Related settings | `user-invocable: false`, `skillOverrides` in settings, `Skill(...)` permission rules. | `[[skills.config]]` with `enabled = false` in `config.toml`, `[skills.bundled]`. |

## Claude Code

Sources: https://code.claude.com/docs/en/skills (sections "Frontmatter reference", "Control who invokes a skill", "Restrict Claude's skill access", "Override skill visibility from settings", "Where you write the skill's name") and https://code.claude.com/docs/en/permissions (rule evaluation order, and `Tool(param:value)` matching). Read 2026-11-19. The last 19,715 characters of the skills page were not read in the first pass; a second pass over that range found only the troubleshooting and related-resources text.

Field names and values:

- `disable-model-invocation`: boolean, default `false`. Documented text: "Set to `true` to prevent Claude from automatically loading this skill. Use for workflows you want to trigger manually with `/name`. Also prevents the skill from being preloaded into subagents and from running when a session-scoped scheduled task fires with the skill as its prompt."
- `user-invocable`: boolean, default `true`. "Set to `false` when only Claude should invoke the skill: Claude Code hides it from the `/` menu and doesn't run it when you type `/name`."
- `allowed-tools`: tools Claude can use without asking during the turn that invokes the skill; the grant clears at the next user message.

Who can invoke, from the documentation's table:

| Frontmatter | User can invoke | Claude can invoke | Context |
| --- | --- | --- | --- |
| (default) | Yes | Yes | Description in context, full skill loads when invoked |
| `disable-model-invocation: true` | Yes | "Not on its own" | Description not in context, full skill loads when invoked |
| `user-invocable: false` | No | Yes | Description in context, full skill loads when invoked |

Blocking behaviour. The page says: "Hide individual skills by adding `disable-model-invocation: true` to their frontmatter. This removes the skill from Claude's context entirely." It also says that with `user-invocable: false` "Claude still can" invoke the skill, and that to keep Claude from invoking it "through the Skill tool" the flag `disable-model-invocation: true` is needed. So the Skill tool is Claude's route, and the flag closes it. The page also says: "If Claude tries when your message doesn't include `/deploy` as a separate word with no punctuation attached, Claude Code blocks the call. Expect Claude to suggest running `/deploy` yourself." (`/deploy` is the page's own example of a skill with the flag set.)

Where the user writes the name: at the start of a message, `/deploy staging` runs the skill directly. After plain text as a separate word with no punctuation, "Nothing runs directly. The name counts as your permission for that message: Claude can run the skill while it responds, and judges from your wording whether you asked it to." Leaving off the slash writes about the skill without permitting a run.

Permission rules for the Skill tool (skills page, "Restrict Claude's skill access"):

- Deny every skill: add `Skill` to the deny rules.
- `Skill(name)` is an exact match; `Skill(name *)` is a prefix match with any arguments. The page shows `Skill(commit)` and `Skill(review-pr *)` as allow rules ("skip the prompt") and `Skill(deploy *)` as a deny rule.
- "When you add allow rules, Claude isn't limited to the skills they name."
- `Skill(skill:<name>)` is the parameter form; a deny rule in that form matches the skill under any of its names (permissions page).
- Evaluation order (permissions page): "Rules are evaluated in order: deny, then ask, then allow. The first match in that order determines the outcome." "A matching ask rule prompts even when a more specific allow rule also matches the same call." The permissions page says deny and ask rules can match `Tool(param:value)` on "any built-in tool". The pages read show no worked example of an `ask` rule on `Skill(...)`, so using one as a confirm-first guard is an application of the general rule, not a documented recipe. Unverified for the Skill tool specifically. Permission rules live in the user's or project's settings, not in the skill, so a plugin cannot ship one inside a skill file (the pages read do not say a plugin can set them either).

`skillOverrides` (skills page, "Override skill visibility from settings"): a settings key mapping skill name to one of four values.

| Value | Listed to Claude | In `/` menu |
| --- | --- | --- |
| `"on"` | Name and description | Yes |
| `"name-only"` | Name only | Yes |
| `"user-invocable-only"` | Hidden | Yes |
| `"off"` | Hidden | Hidden |

A skill absent from `skillOverrides` is treated as `"on"`. "Invoking a hidden skill by its full name returns the `skillOverrides` error instead of running it." And: "Plugin skills are not affected by `skillOverrides`. Manage those through `/plugin` instead." So this setting does not apply to playbook's own skills.

Skill-to-skill. The pages read contain no statement about what happens when a skill's instructions tell Claude to invoke another skill, with or without the flag on the target. What is documented is narrower: the flag stops Claude invoking a skill "on its own", and a Skill-tool call is blocked when the user's message does not name the skill as `/name`. Whether text inside skill A counts as the user naming skill B is not documented. Skill text enters the conversation as content ("the rendered `SKILL.md` content enters the conversation as a single message"), but the page does not classify it as a user message or as Claude's own act for this purpose.

## Codex

Source: https://developers.openai.com/codex/skills, which on 2026-11-19 answered with a 308 permanent redirect to https://learn.chatgpt.com/docs/build-skills (sections "How ChatGPT and Codex use skills", the optional `agents/openai.yaml` metadata section, and "Enable or disable local Codex skills"). Read 2026-11-19. It is a first-party OpenAI page. The page text was returned through a summarising fetch tool, so quoted phrases are as reported by that tool.

- Explicit invocation: "Include the skill directly in your prompt." In the Codex CLI or IDE extension the user runs `/skills` or types `$` to mention a skill.
- Implicit invocation: "ChatGPT or Codex can choose a skill when your task matches the skill `description`."
- `agents/openai.yaml` is optional metadata: "to configure UI metadata in the ChatGPT desktop app, to set invocation policy, and to declare tool dependencies". Fields: `interface` (`display_name`, `short_description`, `icon_small`, `icon_large`, `brand_color`, `default_prompt`), `policy`, `dependencies`.
- `policy.allow_implicit_invocation`: "(default: `true`): When `false`, Codex won't implicitly invoke the skill based on user prompt; explicit `$skill` invocation still works." The page gives only `true` and `false` as values. No third value or confirm mode is shown.
- `dependencies.tools` entries: `type` (the example shows `mcp`), `value`, `description`, `transport` (the example shows `streamable_http`), `url`. Other types and transports are not defined on the page.
- Disabling a skill outright: in `~/.codex/config.toml`, a `[[skills.config]]` entry with `enabled = false` and exactly one selector, `path` (one `SKILL.md` file) or `name` (every skill with that name). The last matching entry wins. `[skills.bundled]` with `enabled = false` turns off bundled system skills for a project. Restart Codex after changing configuration. This disables the skill for the user too, so it is not a confirm mode.
- Skill-to-skill: the page does not say whether one skill can invoke another, nor whether a skill's text naming another skill counts as explicit invocation. Not documented.
- The page does not say whether the policy affects invocation from a skill's own instructions, from a subagent, or in ChatGPT.

## Current settings in the playbook plugin

Read from the plugin files, version 1.0.2, on 2026-11-19.

- `wayfinder`: `disable-model-invocation: true` in `SKILL.md` and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`.
- `to-tickets`: `policy.allow_implicit_invocation: true` in `agents/openai.yaml`; no `disable-model-invocation` in its frontmatter.
- The other twelve skills (`adopt`, `capture`, `glossary`, `grill-me`, `new`, `next`, `prototype`, `research`, `setup-playbook-profile`, `sync`, `tackle`, `untangle`) set neither flag (a search of all `SKILL.md` and `openai.yaml` files for the two setting names found only the three hits above).
- The plugin's `AGENTS.md` states: "A skill only the user may start sets `policy.allow_implicit_invocation: false` there and `disable-model-invocation: true` in its frontmatter." It also says to name another skill as "invoke the `<name>` skill", never by a harness tool or slash command.

## Not documented or not verified

- Skill-to-skill invocation into a user-only skill, in either harness: not documented in the pages read. What happens when skill A's text asks for user-only skill B would have to be tested; it was not tested here.
- Whether a Claude Code `ask` rule on `Skill(name)` gives a confirm prompt for a skill: implied by the general rule text, no Skill-specific example found.
- Whether a plugin can ship permission rules: not found in the pages read.
- Claude Code mid-sentence `/name`: the documented outcome is that Claude "judges from your wording whether you asked it to"; no firmer rule exists.
- Codex: any confirm-before-use mode, any permission-rule system for skills, and any effect on subagents: not found.
- The Codex `config.toml` reference page was not read.
- Codex quotes come through a summarising fetch tool, not a raw page copy.
