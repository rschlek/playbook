# Draft Prototype

Two or three **radically different rough drafts** of the thing itself, side by side in one file, so the user can react to how it reads or how it goes instead of imagining it. Use this when the answer will be words, a layout on paper, or a plan of steps: a policy, a form, a letter, a report's outline, a course, a checklist, a schedule, a process with no real states to click through.

If the question is about rules or states a case moves through (what is legal when), use `LOGIC.md`. If it is about a software screen, use `UI.md`.

## When this is the right shape

- "How should this policy read?"
- "What should the intake form ask, and in what order?"
- "How should the onboarding week go?"
- "Should the report lead with the findings or the method?"
- Any time the user would otherwise argue about a document or a plan in the abstract.

## Process

### 1. State the question and pick N

Default to **3 drafts**; 2 is fine when there are truly only two directions. More than 4 stops being radically different and starts being noise.

Write the question at the top of the file in one line: "Three outlines for the vendor review policy, to settle how it should be organised."

### 2. Draft radically different versions

Each draft is rough and short: an outline with one section written out, a sample page, a mock schedule as a table, a walkthrough of the steps as a numbered list with who does what. Enough to react to, never finished.

Drafts must be **structurally different**: a different order, a different organising idea, a different length or audience, not the same outline reworded. If two come out too similar, redo one with an explicit instruction not to use the first one's structure. Name each by its idea: "A: by risk level", "B: by team", "C: one page, checklist only".

### 3. Put them side by side

One Markdown file under `docs/`, named with `prototype` in it (for example `docs/prototype-vendor-review-policy.md`), holding the question, then each draft under its own heading, then a short "What differs" list so the user sees the choice at a glance. For a schedule or a process, a table per draft (step, who, when, what it needs) is often clearer than prose.

Placeholder text is fine where the exact words do not matter to the question; mark it clearly.

### 4. Hand it over

Open it for the user or give them the path. The useful reactions are "B's order with C's length" or "nobody would read A past the first page": those are the real answer. Mix and redraft when they ask.

### 5. Capture the answer and clear it away

Capture the answer as the `SKILL.md` describes: a decision file naming the chosen direction (or the mix), what it was chosen over, and why. Then delete the drafts file, or keep it under `docs/` if the user wants the comparison kept. Writing the real document or running the real process is a work ticket of its own.

## Anti-patterns

- **Polishing.** Final wording, formatting, and references belong to the real thing, not the prototype.
- **Drafts that differ only in wording.** That's an edit, not a prototype.
- **Writing the whole thing.** One section written out shows how it reads; ten sections waste the time the prototype was meant to save.
- **Using real personal details.** Use made-up names and figures; the drafts may be shared.
