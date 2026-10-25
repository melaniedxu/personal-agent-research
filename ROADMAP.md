# Roadmap

An ordered plan for evolving the research bundle into a community agent.
Unchecked work is not implemented. The current reference runs locally in one
process behind trusted application code.

## Baseline available

- [x] Versioned Grok public prompts, variants, templates, tools and comparisons.
- [x] Muse export with prompt, schema, connector and database documentation.
- [x] Sanitized Grok/Cue client events with explicit observation boundaries.
- [x] Original community prompts and five action contracts.
- [x] Durable coordination core with eight failure/recovery tests.
- [x] Source provenance, integrity inventory and portable validation.

## 1. Connect a model to the host

- [ ] Implement one provider adapter around the original community prompts.
- [ ] Bind tools, identity, origin chat, grants and budgets in trusted host context.
- [ ] Persist tool intents/receipts and bounded context snapshots.
- [ ] Exercise user work and private worker completion through the durable loop.

Acceptance: dispatch, private result, parent revival, delivery and silence work
through an adapter; recovery does not repeat completed external work. Use a fake
provider for repeatable failure cases and an explicitly configured live provider.

## 2. Add conversation UI and delivery

- [ ] Separate permanent messages, progress, approvals and private logs.
- [ ] Add an external-delivery outbox with reconciliation.
- [ ] Bind approvals to exact operations and durable user decisions.

Acceptance: reconnects preserve message IDs, repeated deltas do not duplicate
bubbles, unknown sends reconcile before retry, quiet wakes send nothing, and
requested results reach the original chat.

## 3. Extend scheduling and task lifecycle

- [ ] Recurrence with timezone, DST, misfire/overlap policies and finite-watch cleanup.
- [ ] Authenticated event ingress, source deduplication and cheap polling gates.
- [ ] Worker lease/generation fencing, bounded retries and budgets.
- [ ] Safe-boundary steering/cancellation and desktop resource leases.

Acceptance: duplicate events and recovery do not duplicate execution, cancelled
jobs do not revive, late callbacks are fenced and unchanged polls invoke no model.

## 4. Implement execution isolation and account integrations

- [ ] Enforce tenant/cell isolation, resource limits and brokered egress.
- [ ] Add a credential broker and one read-only connector behind host grants.
- [ ] Add brokered browser sessions with ownership and takeover.

Acceptance: workers cannot widen grants, reach another account, read broker
credentials or commit unapproved actions. Document and test the actual isolation
and shared-state choices outside the model prompt.

## Open research

- [ ] Authenticate which public Grok sections match a measured runtime release.
- [ ] Resolve stale names and absent role-specific schemas in the October archive.
- [ ] Recover current Cue docs through an authorized, reproducible source.
- [ ] Observe cancellation, revival and delivery under controlled failures.
- [ ] Measure context assembly, compaction and worker-context inheritance separately.

Keep dated sources and reproducible probes. The community implementation can
choose explicit contracts without waiting for a complete vendor replica.
