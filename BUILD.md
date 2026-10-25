# Build a community personal agent

This is a proposed implementation based on the evidence in [STUDY.md](STUDY.md).
The accompanying Python reference executes the coordination semantics without
network access. It does not include a live model, account connectors, UI, browser,
or a security sandbox. Those integrations have explicit contracts below.

## Start with the runnable core

```sh
python3 reference/demo.py
python3 -m unittest discover -s reference -p 'test_*.py' -v
```

The core stores state in SQLite and has no dependencies beyond Python's standard
library. For persistent state use `Engine("state.db")`; the demo uses `:memory:`.
Keep it behind trusted application code. It is not an authenticated HTTP service.

The [tool manifest](config/community-tools.json) defines five model actions and
their Python bindings. The [runtime config](config/community-runtime.json) clearly
separates implemented reference behavior from a production target. The
[model-request template](requests/community-model-request.template.json) is an
invented provider-neutral adapter contract, not a vendor request format.

### Connect the model

Implement a host-side adapter around this loop:

1. Claim a wake with a lease. Bind agent identity, origin chat, parent, authority
   reference, tool-call nonce and remaining budget in trusted host context.
2. Load the coordinator or worker prompt, then assemble a bounded conversation
   snapshot, source references and the wake. Include the background addition
   for a scheduled check or private completion.
3. Filter tools by role and host grants. Translate their `inputSchema` objects
   into the chosen provider's function/tool format. Do not let model arguments
   choose their own identity, permission version, or delivery destination.
4. Validate arguments and semantic conditions, then validate the run lease and
   permission scope again before dispatch. Persist the tool intent and receipt.
5. Return the tool result to the model. A spawn returns acceptance, not its result.
   A child completion is persisted and enqueues a private parent wake.
6. End through `turn.finish(message=...)`, or finish silently without a message.
   Commit local message creation and run completion atomically.

In the reference `task.complete` calls an internal completion callback. A real
distributed adapter must authenticate the worker and fence its completion with
the current lease/generation. Never expose an arbitrary `worker_id` callback to
untrusted clients. `task.cancel` must verify parent/child ownership before calling
the engine. `schedule.once` is absent unless the host grants that specific future
action. These required adapter checks are listed in the tool manifest; the model
prompt is not their enforcement.

## Durable entities and invariants

| Entity | Minimum durable fields | Invariant |
|---|---|---|
| Agent | account, identity, role, parent, origin chat, allowed capabilities | An identity is not an isolation boundary |
| Conversation | channel binding, transcript sequence, compaction epoch | A UI projection is not the complete model context |
| Accepted event | source, source ID, digest, target, ordering, authority reference | Same key + different input is rejected |
| Run | event, status, lease owner/expiry, generation, budget, input snapshot | Only the current lease/generation may commit |
| Child task | parent, spawn nonce, scope, context policy, result reference | Duplicate spawn/completion does not duplicate work |
| Schedule | version, owner, timezone, recurrence, next due, misfire policy | Definition changes do not rewrite a running snapshot |
| Watch | source cursor/fingerprint, revision, last check, next check | Cursor advancement and wake enqueue are atomic |
| External action | intent, canonical arguments hash, permission, idempotency key, receipt | Unknown outcome is reconciled before retry |
| Delivery | message ID, origin target, payload hash, outbox attempts, provider receipt | Execution completion and delivery completion differ |

Serialize coordinator turns per conversation or agent, then allow independent
workers to run in parallel within a bounded task tree. Give user work priority
when claiming queued work. To support active-turn interruption, implement a
separate steering/cancellation protocol at safe boundaries; the small reference
only prioritizes queued work. Do not claim that a `deliveryMode` field alone proves
preemption semantics.

Persist task cancellation before stopping workers. Fence late callbacks and
delivery commits. A cancelled parent must not be revived into doing new work by
an old child result. Recovery should preserve completed stages, pending approvals,
unknown external outcomes, denials and rate-limit stops.

## Scheduling and event triggers

Support three independently testable ingress paths:

- **Clock:** calculate a due occurrence outside the model, enqueue it once using
  `(job_id, definition_version, scheduled_occurrence)`, then run the saved body.
- **Push:** authenticate a webhook or stream event, record its source ID, and
  enqueue a bounded run. An HTTP acceptance is not a completed run.
- **Poll:** use a cheap deterministic detector first. Persist its cursor and
  enqueue a wake only when a relevant observation changes. No model call on a
  no-change result. The awakened model still decides whether to notify the user.

For recurring jobs, record an IANA timezone, DST behavior, overlap policy,
catch-up/skip/coalesce policy, retry limits, deadline, lifecycle owner and delivery
destination. A one-off request does not automatically authorize recurrence.
The reference implements one-off UTC epoch schedules only.

A continuous collector is a supervised service, not a loop inside a conversational
turn. Separate desired state from current process state. After environment
replacement, restore prerequisites and reconcile each collector from checkpoints.
An active PID does not establish useful progress. A worker waiting for a user's
approval must not be restarted as a failed collector.

## Keep the chat clean

Use explicit typed presentation events. Two viable model interfaces were found:
Grok's historical message tool and Muse's parser for selected final output.
The proposed reference chooses an explicit `turn.finish` action, committing at
most one bubble per turn. Extend it to typed message lists if multiple bubbles,
attachments or cards are required; do not indiscriminately stream internal model
text into the public transcript.

Maintain separate projections for:

- permanent chat messages and attachments;
- transient deltas, typing, status and progress;
- approval requests and secure credential entry;
- private worker logs/results and coordinator handoffs;
- sidebar preview, unread/read state and notifications.

Use one canonical message ID for transient-to-durable replacement and later
metadata updates. Cue's observed sequence illustrates why appending a new bubble
for every event creates duplicates. A delayed sidebar update can describe a
previous message; correlate IDs and sequence numbers instead of treating every
preview as a newly delivered answer.

Commit a durable outbox with user-message creation. A separate channel worker
performs external delivery and records provider receipts. Retries need provider
idempotency or reconciliation; SQLite uniqueness alone cannot give exactly-once
email, SMS or arbitrary external writes. A quiet completed check has no outbox
entry. A result the user explicitly requested must not disappear merely because
the worker finished while the coordinator was idle.

## Tool discovery and account integrations

Keep a compact capability catalog with names, descriptions, schema hashes,
read/write classes and grant requirements. Load detailed definitions only through
the host registry. Freeze a tool/schema snapshot per run so a model retry does
not silently acquire different semantics.

Use [Muse's recovered namespace schemas](evidence/muse/runtime-export/schemas/)
and [connector definitions](evidence/muse/runtime-export/connectors/) as interface
research. They depend on vendor CLIs, auth services and lifecycle code that are
not included. They are not drop-in working MCP servers. The installed Cue addon
manifests show a different local MCP path; preserve this distinction.

Manus's historical context-engineering article describes stable prompt prefixes
and action masking. It does not prove today's Cue tool routing, and hosted model
APIs do not all expose decoder-level masking. Use the provider's supported tool
selection controls and benchmark your own catalog strategy.
[Historical engineering article](https://manus.im/uk/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus).

## Sandbox and policy implementation

Implement these in host services, outside all agent-modifiable environments:

1. Per-account VM or comparably enforced tenant boundary, with an explicit
   decision about shared versus isolated agent workspaces.
2. Disposable execution cells, an immutable image, narrowly scoped persistent
   mounts, resource limits, restricted capabilities and broker-only egress.
3. A policy/approval broker binding authorization to the actor, task, tool,
   canonical arguments, destination, data classes, expiry and permission version.
4. A credential broker inserting secrets after approval. Agents receive opaque
   references or surrogates, not provider tokens in environment variables.
5. A browser broker owning automation sessions, task leases and takeover state.
   Decide whether it permits only accessibility actions or richer script APIs;
   that is a security and capability choice, not a UI detail.

The reference exposes no shell executor. Adding `subprocess.run` with a timeout
would not implement this security architecture. Neither the reference prompts nor
the proposed JSON config enforce network isolation, secret separation or tenant
security by themselves.

## Acceptance criteria for the next implementation phase

The eight included tests cover the small reference's implemented invariants.
Before attaching real accounts, add integration tests for the production
components you actually build:

- crash after external acceptance but before local receipt persistence;
- duplicate source events, reconnect replay and transient/durable message updates;
- expired lease or cancelled generation trying to write or send;
- worker completes while the parent is offline, busy, or being compacted;
- scheduled occurrence across DST, missed execution and overlapping runs;
- source unchanged, model wakes but decides silence, expected result fails;
- approval expires or is revoked while a task is suspended;
- environment replacement restores work without reviving cancelled tasks;
- connector is available for read/write but has no configured event subscription;
- browser takeover pauses automation and cannot leak credentials to the model.

Use synthetic fixtures first. Measure acceptance-to-start, execution time,
completion-to-parent-wake, and message-commit-to-provider-delivery separately.
That decomposition makes a clean, responsive personal agent easier to diagnose
than one end-to-end latency metric.
