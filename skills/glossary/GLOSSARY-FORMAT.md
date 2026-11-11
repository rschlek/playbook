# Glossary format

The glossary is `docs/glossary.md` in the project's repository.

## Structure

```md
# {Context Name}

{One or two sentence description of what this context is and why it exists.}

## Language

**Order**:
{A one or two sentence description of the term}
_Avoid_: Purchase, transaction

**Invoice**:
A request for payment sent to a customer after delivery.
_Avoid_: Bill, payment request

**Customer**:
A person or organization that places orders.
_Avoid_: Client, buyer, account
```

The same shape holds outside software. For a compliance process:

```md
**Control**:
A check that must pass before a change is accepted.
_Avoid_: Gate, rule

**Exception**:
A recorded, time-limited permission to skip one control for one change.
_Avoid_: Waiver, override
```

## Rules

- **Be opinionated.** When multiple words exist for the same concept, pick the best one and list the others under `_Avoid_`.
- **Keep definitions tight.** One or two sentences max. Define what it IS, not what it does.
- **Only include terms specific to this project's context.** General concepts of the field (for software, timeouts or error types; for a compliance process, deadlines or approvals in general) don't belong even if the project uses them extensively. Before adding a term, ask: is this a concept unique to this context, or a general concept of the field? Only the former belongs.
- **Group terms under subheadings** when natural clusters emerge. If all terms belong to a single cohesive area, a flat list is fine.

## Single and multi-context projects

**Single context (most projects):** one `docs/glossary.md`, in the structure above.

**Multiple contexts:** `docs/glossary.md` becomes a map. It lists the contexts, where each one's glossary lives under `docs/glossary/`, and how they relate:

```md
# Glossary map

## Contexts

- [Ordering](./glossary/ordering.md): receives and tracks customer orders
- [Billing](./glossary/billing.md): generates invoices and processes payments
- [Fulfillment](./glossary/fulfillment.md): manages warehouse picking and shipping

## Relationships

- **Ordering → Fulfillment**: Ordering emits `OrderPlaced` events; Fulfillment consumes them to start picking
- **Fulfillment → Billing**: Fulfillment emits `ShipmentDispatched` events; Billing consumes them to generate invoices
- **Ordering ↔ Billing**: Shared types for `CustomerId` and `Money`
```

The skill infers which structure applies:

- If `docs/glossary.md` is a map of contexts, read it to find them
- If it is a plain glossary, single context
- If neither exists, create `docs/glossary.md` lazily when the first term is resolved
- If the project already keeps a glossary somewhere else, use that file and leave it where it is

When multiple contexts exist, infer which one the current topic relates to. If unclear, ask.
