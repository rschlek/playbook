# How work moves through a project

This page is for anyone opening the playbook plugin for the first time, whether or not they write software. It shows the path a piece of work takes, which skill handles each step, and what each step leaves behind.

## The flow

```
an idea
  -> grill-me      sharpen it until you can say where it ends
  -> wayfinder     only if it is still foggy: a map ticket, one child ticket
                   per open question, answered with research, prototype,
                   and grill-me
  -> to-tickets    the plan in a parent ticket, the work tickets under it,
                   in order, with what blocks what
  -> tackle        do one ticket at a time and close each honestly
  -> close the parent, offered when its last ticket closes

at any time:  capture  a stray item becomes one ticket
              untangle when you are lost in a pile of findings or options
              next     when you are not sure which step you are on
```

Skip what you do not need:

- Work you already understand skips `wayfinder`: go straight to `to-tickets`.
- A single small job skips the plan too: `capture` it, then `tackle` it. It needs no project or repository, and it closes with an ordinary closing note.
- An idea that is already sharp skips `grill-me`.

## Where things live

- **The repository** holds the work and the project's own context: one file per decision in `docs/decisions/`, dated research documents under `docs/`.
- **The tracker** holds the work: maps, question tickets, the plan (in its parent ticket's body), and work tickets, each with its status.
- **Agent memory** is outside this plugin: nothing here reads or writes it.

## Worked example: approval for a new data pipeline

A team wants to copy customer records into a reporting store every night. Nobody is sure what approval that needs.

**The loose idea.** "We need the reporting pipeline approved." `grill-me` sharpens it into a destination: *the review board has signed off the pipeline, and every control it asks for is in place.*

**The map.** That is still foggy, so `wayfinder` makes a map ticket, "Get the reporting pipeline approved", and four question tickets under it:

| Question ticket | Type | How it was answered |
|---|---|---|
| Which rules apply to copying customer records into a reporting store? | research | `research` read the regulation and the internal data policy and wrote `docs/research/2026-03-02-rules-for-customer-data-copies.md`. It found facts (an impact assessment is required; copies may be kept at most two years), so the ticket links that document and no decision file is written. |
| Do we copy full records or masked records? | grilling | A conversation with the user, using `grill-me`. Masked won: the reports never need names, and masking shrinks the assessment. |
| How long do we keep the copies? | grilling, blocked by the first | Settled once the rules were known: two years, the maximum, because yearly comparisons need it. |
| Who reviews pipelines, and how is a request made? | task | The agent found the intake page. The resolve comment records what was done: the board meets monthly, requests go through the intake form, the next deadline is the 20th. |

The map body's **Not yet specified** held "what monitoring the board will ask for" until the intake page answered it. **Out of scope**: moving old reports onto the new store.

**Decision files left behind**, one per choice:

- `docs/decisions/2026-03-04-copy-masked-records-only.md`
- `docs/decisions/2026-03-05-keep-copies-two-years.md`

**The plan.** With no question left, `wayfinder` asks whether to create the tickets now; on a yes, `to-tickets` writes a parent ticket, "Plan: approval for the reporting pipeline", linked from the map. Its body:

```
Get the nightly reporting pipeline approved by the review board.
1. Write the masking rule for each customer field.
2. Write the impact assessment (waits on 1).
3. Set up the job that deletes copies after two years.
4. Submit the approval request with the assessment (waits on 2 and 3).
Done when: the board's sign-off is linked here.
Rests on: copy-masked-records-only, keep-copies-two-years.
```

**The work tickets**, created under that parent in order: "Write the masking rules", "Write the impact assessment", "Set up the two-year deletion job", "Submit the approval request". In a second pass, "Write the impact assessment" is marked blocked by "Write the masking rules".

**Doing the work with `tackle`.**

- "Write the masking rules" is done: the rules are in `docs/masking-rules.md`, the ticket closes with the note *Rules for 14 fields; 3 fields dropped entirely.* That unblocks the assessment.
- "Write the impact assessment" stops partway. It stays open with the note *Sections 1 to 4 drafted in docs/impact-assessment.md. Next: section 5, the risks, taken from the two decision files.* It is never marked done.

Later sessions finish the assessment and the deletion job. When "Submit the approval request" closes with the sign-off linked, `tackle` says it was the last open ticket under "Plan: approval for the reporting pipeline" and offers to close the parent. The user says yes, and the parent closes.

**What is left behind:** a research document, two decision files, the masking rules and the assessment in `docs/`, and in the tracker a closed map (to-tickets closed it once the plan was linked), a closed plan, and four closed work tickets that say what was done.

## A small example: one person, no map

Someone wants their household paperwork in one filing system before tax season. They already know what that means, so there is nothing to map. They need no project or repository for this: they `capture` three tickets in their own tracker: "Scan last year's receipts", "Sort the scans into folders by year", "Shred the paper originals", the third blocked by the first.

Over a few evenings they `tackle` one at a time. The receipts ticket stops partway one night, with the note *January to June scanned; the July to December box is in the hall cupboard*, and finishes the next. No decision files and no research: nothing was decided that a future reader would wonder about. If the work had grown into a real choice (which filing system to buy, say), `grill-me` would sharpen it and the choice would get a decision file.

## Which skill when

| Skill | Use it when | Do not use it when | What it leaves behind |
|---|---|---|---|
| **Set up a project** | | | |
| `profile` | First time on a machine, or changing the default tracker | Changing one project's settings (`adopt`) | The profile file and the user's tracker doc beside it |
| `new` | Starting a project from nothing | The repository already exists (`adopt`) | A project folder with its standard files, a repository, and its tracker doc when it needs one |
| `adopt` | Bringing an existing repository to the standard | Creating a project (`new`) | The missing standard files, `project.yaml` filled in, a list of gaps |
| `sync` | The standard has a new version, or repos came from project-guide | One repository that was never adopted (`adopt`) | Updated base blocks and conventions copies, review branches for shared repos |
| **The work loop** | | | |
| `wayfinder` | The way to the goal is unclear and too big for one session | The way is already clear (`to-tickets`) | A map ticket, question tickets, decision files, research documents |
| `to-tickets` | A plan is settled and needs to become work | Questions are still open on the map (`wayfinder`) | A parent ticket holding the plan, work tickets under it with blocking |
| `capture` | One new thing needs to be a ticket | A whole plan (`to-tickets`) | One well-formed ticket in the right place |
| `tackle` | Doing a ticket, or asking what to work on | Adding a ticket (`capture`) | The work done, and the ticket closed, noted, or marked blocked |
| `next` | Unsure which step the project is on or which skill comes next | Choosing a specific ticket (`tackle`) | Nothing: it only looks and points |
| **Thinking** | | | |
| `grill-me` | Testing a plan or sharpening an idea by being questioned | You are lost in the agent's findings (`untangle`) | A shared understanding; decisions are recorded by the skill that called it |
| `research` | A decision waits on facts from outside the project | Deciding with the user (`grill-me`) | A dated, cited document under `docs/` |
| `prototype` | Seeing a rough version would settle a design question | Building the real thing (`tackle`) | A decision file; the throwaway is deleted or kept by choice |
| `untangle` | Lost, overwhelmed, or wanting something said plainly | Testing your own plan (`grill-me`) | Small decisions taken one at a time, then a short ledger |
| `glossary` | Naming and defining the project's terms | Testing a whole plan (`grill-me`) | `docs/glossary.md` and decision files for hard-to-reverse choices |

## Setting up

- **Once per machine:** run `profile`. For everyday tickets it needs only your tracker; it asks for your projects folder and scopes when you first start a project.
- **Once per tracker kind:** the tracker setup inside `profile` (or `new` or `adopt` for a project with its own) writes a tracker doc from a shipped template. With no tracker yet, pick `markdown`: tickets become files in the project's repository. It proposes the steps, runs the query for pickable work so you can see what would be offered, and creates nothing in the tracker without your yes.
- **Once per project:** only for an initiative with records to keep, `new` for fresh work or `adopt` for a repository that already exists. After that, `next` tells you where you are.
