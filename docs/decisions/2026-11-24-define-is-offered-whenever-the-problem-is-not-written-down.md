# Define is offered whenever the problem is not written down

Question: When is `define` the step that fits, and does it look at ways to solve the problem?

`define` is the step for writing down the problem, whoever arrives: a person with a loose want, or a person with a specific way of solving it already in mind. It ends at the problem and looks at no ways to solve it.

## What was decided

1. When it fits. When new work has no problem definition yet, `guide-me` offers `define` first, whether the person has a loose want or a specific build in mind. It is offered and never forced: on a skip, `guide-me` names the next step that fits.
2. What starts it. Plain words such as "let's define the problem we are trying to solve" start it, as well as the words of a person who does not yet know what they want.
3. A person who arrives with a way of solving it. `define` asks what problem that way is meant to solve. The idea stays in the conversation for the next step and is not written into the problem definition.
4. Problem only. `define` lays out no ways of solving the problem and records no pick. This was looked at again and kept.
5. How `guide-me` knows. In a project, one look at `docs/problems/`, and no more.
6. `wayfinder` is not changed with the release that adds `define`. Its changes from this map are made together and tested once.

## Options considered

- `define` only for a loose want: not taken. A written problem is useful also to a person who already has a way of solving it in mind.
- `define` in two parts, the problem and then ways to solve it: not taken. Each skill keeps one job, and a second part would pull people through the first.
- `define` required before any planning: not taken. It is offered, and a person may skip it.

## What settled it

- The person's view: the need is "define the problem we are trying to solve", and the way of solving it belongs to a later step.
- `guide-me` is the entry point and offers the next step, so a separate step costs the person no name to remember.

## Not settled here

- Which step lays out ways to solve a defined problem. A separate question on the map holds it. The person's rule for it: `wayfinder` changes as little as possible.

## Replaces

In part, the decision on how a `guide-me` session goes (`2026-11-20-how-a-guide-me-session-goes.md`): its point that a loose want leads to `define`. `define` is offered whenever new work has no problem definition.
