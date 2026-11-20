# A split project tracker stays, and a personal tracker sits over the whole of it

Question: How do split-by-kind trackers (primary and secondary) and a personal tracker sit together?

Splitting a project's tickets by kind between a primary and a secondary tracker stays as it is. It is a property of the project tracker. A personal tracker sits over the whole project tracker, whichever shape it has. The setup is named a split project tracker, and the phrase "two trackers" is no longer used for either idea.

## What was decided

1. Split by kind stays. A project tracker is one tracker, or a primary with a secondary for each kind of ticket filed elsewhere. Everyone on the project sees every part. Nothing about how a split project tracker works changes.
2. A personal tracker sits over the whole. A person may use a personal tracker with a project whose tracker is split, and a personal item's link may point at a ticket in any part.
3. A personal tracker is never split. The profile holds one tracker entry, so a person's own list is one place.
4. The name. The setup is called a split project tracker, with a primary and a secondary. "Two trackers" is not used for it, and not for a personal tracker over a project tracker either.

## Sentences that change

In `references/tracker-lookup.md`:

- The heading "Two trackers" becomes "A split project tracker".
- "A doc may describe a primary and a secondary tracker, each holding one kind of ticket." becomes "A project tracker may be split: its doc describes a primary and a secondary tracker, each holding one kind of ticket."

In `references/conventions.md`:

- "One doc may describe two trackers, a primary and a secondary, each holding one kind of ticket" becomes "One doc may describe a split project tracker, a primary and a secondary, each holding one kind of ticket". It is a rename with no change of behaviour, and it still gets a dated changelog entry.

In the skills `capture`, `tackle`, `to-tickets`, and `wayfinder`: each mention of "two trackers" that points at that section of the tracker lookup becomes "a split project tracker".

Sentences that stay, and why:

- "A ticket in one tracker cannot sit under a parent in the other" and "no ticket's text or status is repeated in the other tracker" stay. Both speak only of the parts of a split project tracker. What crosses between a personal item and the project ticket it links is a separate rule with its own question on the map.
- "Maps, and the parent tickets that hold plans, live in the primary tracker" stays for a project with no personal tracker. Where they live when a personal tracker is used belongs to the question of how tracker lookup finds both trackers.
- "never fall back to another tracker" stays. A personal tracker is declared, never a fallback.

## Options considered

- Split by kind and the personal tracker become one mechanism: not taken. Everyone sees every part of a split and only one person sees a personal tracker, so one mechanism would need a visibility switch on every rule.
- Split by kind is retired: not taken. It is a shipped feature, and a team that keeps code tickets in its code host would lose it.
- Split by kind stays, a property of the project tracker: taken.
- The phrase "two trackers" kept for the split: not taken. A personal tracker over a project tracker is also two trackers, so the phrase would name two different setups.
- The name "split project tracker": taken.

## What settled it

- The glossary already says a project tracker "may be split by ticket kind into a primary and a secondary".
- The two ideas answer different questions: a split says what kind of ticket goes where, and a personal tracker says who sees an item.
- The earlier decision on where a personal tracker is declared keeps one tracker entry in the profile.
- The proposal this map started from called the personal setup "two trackers" while the rules used the phrase for the split.

## Not settled here

- From inside a repository, which tracker each skill reads and writes when a personal tracker is used, including where maps and plans live and how picking merges. A separate question on the map holds these.
- Whether the link a secondary ticket carries to its parent and the link a personal item carries are stored the same way. The question on the Link label holds this.

## Replaces

Nothing.
