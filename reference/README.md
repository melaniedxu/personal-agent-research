# Runnable coordination reference

This original code demonstrates the control plane described in the study. It uses
Python 3.9+ and SQLite from the standard library. No API keys or network are needed.

From the `agent-study` directory:

```sh
python3 reference/demo.py
python3 -m unittest discover -s reference -p 'test_*.py' -v
```

The demo uses a deterministic stand-in for model decisions. It accepts a user
message, dispatches a worker, records a private completion, wakes the coordinator,
and commits a user message to the originating side chat. An unchanged watch and a
scheduled check finish silently. Pass a filesystem path to `Engine(path)` to keep
the state across restarts. The demo itself uses an in-memory database.

`engine.py` implements:

- durable event acceptance with input-digest validation;
- one active leased run per agent, user-first claim priority, and stale-lease fencing;
- idempotent child creation and completion, private parent wakeups, explicit delivery;
- recursive cancellation, one-off schedules, persistent change-detection cursors;
- atomic local message commit plus run completion.

The API is **trusted in-process code**, not an authenticated public service.
Bind agent identity and permissions in a host-side adapter before exposing tools.
`complete_worker` is an internal completion callback; authenticate its caller and
bind it to the worker's run in a distributed system. `finish` validates its run
lease. Keep lease renewal/recovery in the host, outside agent-controlled code.

To connect a model, construct a context from the claimed wake and the appropriate
prompt in `../prompts/`, expose the matching actions in
`../config/community-tools.json`, and dispatch validated calls to the engine.
Use a provider adapter to translate that model-neutral schema to the provider's
request format. The model must not choose its own agent ID, permission scope, or
delivery chat. Persist tool receipts before continuing the model loop.

This is deliberately a small executable reference, with explicit limits:

- It is not a VM, container sandbox, credential broker, browser implementation,
  external messaging bridge, live LLM client, or multi-user auth service.
- Priorities apply when claiming work; active model/tool calls are not preempted.
- Schedules are one-off UTC epoch times. Recurrence, timezone/DST rules, budgets,
  dead-letter handling, leases for external workers, and wake coalescing belong in
  the production implementation described in `../BUILD.md`.
- `cancel` stops future local work and delivery. It cannot undo an external action.
- Atomic SQLite delivery prevents duplicate local bubbles. An external channel
  requires a durable outbox and the provider's idempotency or reconciliation API.
- No shell or arbitrary-code executor is exposed. A subprocess with a timeout is
  not a security sandbox.

The eight tests exercise failure and recovery semantics, not only happy-path
method calls. The original reference code and community prompts are MIT licensed;
the vendor evidence directory has separate provenance and is not covered by that
grant. See `../LICENSE-ORIGINAL.txt`.
