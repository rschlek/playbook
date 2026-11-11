# Decision format

Decisions live in `docs/decisions/`, one file per decision, named `YYYY-MM-DD-<short-name>.md` (the date it was decided, then a short name, lowercase with hyphens). This is the shape "Documents" in `references/conventions.md` gives, and the `wayfinder` skill writes the same files.

Create the `docs/decisions/` folder lazily: only when the first decision is recorded.

## Template

```md
# {Short title of the decision}

{1-3 sentences: what's the context, what did we decide, and why.}

## Options considered

- {option}: {why it was or was not taken}

## What settled it

{The facts and figures that decided it.}

## Replaces

{The earlier decision file this replaces, or "Nothing."}
```

Keep it short. A decision can be a single paragraph and a line under each heading. The value is in recording *that* a decision was made and *why*, not in filling out sections. Add a **Consequences** section only when non-obvious downstream effects need to be called out.

## Records rule

A decision holds project facts only, written for a reader who opens the project cold: no personal details, no discussion of people beyond their role in the work, no record of who said what, no personal reasoning. In a shared project, show the user the exact text and wait for a yes before writing it. A decision that cannot be written this way stays out of the project.

## Replacing a decision

A decision file is not edited after it is written. When a later decision replaces it, the new file says so under Replaces, and the old file gets one added line: `Replaced by: <new file name>`.

## When to offer a decision

All three of these must be true:

1. **Hard to reverse**: the cost of changing your mind later is meaningful
2. **Surprising without context**: a future reader will look at the work and wonder "why on earth did they do it this way?"
3. **The result of a real trade-off**: there were genuine alternatives and you picked one for specific reasons

If a decision is easy to reverse, skip it: you'll just reverse it. If it's not surprising, nobody will wonder why. If there was no real alternative, there's nothing to record beyond "we did the obvious thing."

### What qualifies

- **The shape of the work.** "We're using one repository for all services." "Every request goes through intake before triage, never straight to a reviewer."
- **How the parts meet.** "Ordering and Billing communicate via events, not direct calls." "Legal signs off on the policy, not on each procedure under it."
- **Choices that carry lock-in.** Database, auth provider, hosting; a vendor, a filing system, a standard to certify against. Not every small choice: just the ones that would take a quarter to undo.
- **Boundary and scope decisions.** "Customer data is owned by the Customer context; others reference it by ID only." "This audit covers the payments team only." The explicit no-s are as valuable as the yes-s.
- **Deliberate deviations from the obvious path.** "We write SQL by hand instead of using an ORM because X." "We file quarterly though monthly is the norm, because X." Anything where a reasonable reader would assume the opposite. These stop the next person from "fixing" something that was deliberate.
- **Constraints not visible in the work itself.** "We can't use that cloud provider because of compliance requirements." "Records must be kept seven years because of the regulator's rule."
- **Rejected alternatives when the rejection is non-obvious.** If you considered one approach and picked another for subtle reasons, record it; otherwise someone will suggest the first again in six months.
