---
name: research
description: >-
  Investigate one question against high-trust primary sources and write the
  findings, every claim cited, as a dated document under the project's docs/
  folder, handing the reading to a background agent where the harness has
  one. Works for any kind of project: an API's limits, what a regulation
  requires, what a standard says, the state of a field, the options for a
  purchase. Use when the user says "research X", "look into X", "find out
  what the docs say about X", "what does the rule actually say", "gather the
  facts on X", or wants reading legwork done in the background, and for the
  research tickets on a decision map. Do NOT use to explain something already
  understood (that is untangle), to decide between options with the user (that
  is grill-me), or to chart a large effort (that is wayfinder).
---

# Research

Shared paths such as `references/conventions.md` are relative to the plugin's root folder, two levels above this skill's folder.

Spin up a **background agent** to do the research, so you keep working while it reads. Start it with a fresh context window. When the harness has no background agents, do the research inline, one question at a time, following the same steps.

Its job:

1. Investigate the question against **primary sources**, not a secondary write-up of them: for software, official docs, source code, specs, and first-party APIs; elsewhere, the regulation or standard itself, the issuing body's guidance, the original paper or dataset, the vendor's own terms. Follow every claim back to the source that owns it.
2. Write the findings to a single Markdown document, citing each claim's source. It holds project facts only, written for a reader who opens the project cold: no personal details, no discussion of people beyond their role in the work, no personal reasoning.
3. Name it `YYYY-MM-DD-<short-name>.md`, dated the day it is written, under `docs/`: in the folder the project already uses for research, else `docs/research/`. A research document records a moment: it is never edited afterwards, and new findings go in a new file.
4. Return the document's path and a few lines of findings to the session that started it.

## Where it goes

- Read "Documents" in `references/conventions.md`. Research is a record, and records live only in the project's repository. When the work has no repository, give the findings in the conversation and say they are not kept; offer the `new` skill only when the user wants them kept as a record. Never save them anywhere else in its place.
- In a shared project (`project.yaml` says `shared: true`, or sets `visibility`), show the user the exact text and wait for a yes before writing it. A background agent returns its draft for that check instead of writing it.
- The document is never kept on a branch that will not merge.
- When the research serves a ticket, link the document from that ticket. The skill that invoked this one (such as `wayfinder`) does it; when the user named a ticket directly, find the tracker doc as `references/tracker-lookup.md` says and leave the link as its Layout's Note says.
- The document holds facts, and a fact needs no decision file. When a finding settles a choice (something that could have gone another way), that choice also gets a decision file in `docs/decisions/`: the invoking skill writes it, or, when the user asked directly, offer to.
