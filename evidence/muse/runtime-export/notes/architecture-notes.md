# Personal-agent architecture notes (research reconstruction)

**What this is.** A reconstruction of how this personal-agent runtime appears to
work, built only from documents and tool definitions inspectable from inside a
session. It is written for someone building a community implementation. It is
NOT vendor source code, and it does not claim server-side internals that could
not be observed from here.

## Labeling — read this first

- **[Inspected]** — the author read this directly with a tool in this session
  (file path given). You can re-verify it the same way.
- **[Prompt-described]** — stated in the runtime's own prompt or docs, but the
  behavior happens outside the observable session (server-side routing, model
  hosting, push delivery). It is the vendor's self-report, not an independent
  measurement.
- **[Inference]** — the author's synthesis from inspected + prompt-described
  material. Treat it as a design hypothesis, not a fact.

No personal data was used. No connected account was read, no credential was
touched, no permission was changed, no external message was sent, and no real
automation was scheduled while producing these notes. The one temporary child
agent the request permitted was NOT spawned: direct inspection sufficed, so
there was nothing to close.

## 1. System at a glance

```
User surfaces: Muse app (iOS / Android / web / Mac) + provider side chats (e.g. WhatsApp)
        │  chat UUID + binding authority captured by the runtime per message [Prompt-described]
        ▼
Main agent (model + system prompt) ── tools ──► Linux VM (guest compute)
        │                                        ├─ home dir (persists) + workspace files
        │                                        ├─ Chromium browser (shared default profile)
        │                                        ├─ shell, filesystem, systemd (guest)
        │                                        └─ paired devices (via device.* tools)
        ├──► subagents (children inherit context; results return as handoffs)
        ├──► workflows (VM-local JS daemon coordinating child agents)
        ├──► browser tasks (windows with task_id; results return as handoffs)
        └──► scheduled work (crons, hooks, background self-improvement runs)
Runtime (outside the VM, [Prompt-described]):
  scheduler + delivery router + approval/permission store + connector OAuth +
  message index + push notifications + model inference
```

## 2. Local vs. cloud split

| Piece | Where it appears to live | Evidence |
|---|---|---|
| Agent working files, memory notes, goal workspaces, hook scripts/state, cron definition copies | VM home directory, which persists across VM replacements | [Inspected] `~/docs/chat/scheduling-and-watching.md` ("Keep the canonical unit, program, dependencies, and state under persistent home storage"); system prompt: "`~` survives VM restarts and replacements" |
| Live browser, shell, file tools | Same VM (guest) | [Inspected] system prompt "Your computer" section; `~/docs/browser.md` exists (not read in full — see Gaps) |
| Model inference (Muse Spark family) | Runtime/cloud side; the VM is not the model host | [Inference] from the prompt's split between "your computer" and "the runtime: the machinery around you"; no host address was observable |
| Scheduler, handoff delivery, approval cards, push | Runtime/cloud side | [Prompt-described] system prompt ("the runtime delivers", "approval cards"); [Inspected] `~/docs/scheduling-and-watching.md` ("Jobs run whether the user's app is closed or their phone is off. Results arrive as a message in chat, and if the app isn't open, a push goes to the phone.") |
| Message transcripts + full-text index | Server side | [Inspected] `~/docs/client-surfaces.md` ("the server keeps a full-text index of every visible message … across the main chat and all side chats, including archived ones"; "hidden system and background messages are never in the index") |
| Connector OAuth tokens / Secure Vault | Provider-side secure storage, not in chat, memory, or ordinary files | [Prompt-described] system prompt "Secure Vault" section; [Inspected] `~/docs/client-surfaces.md` Settings panes (Secure credentials store; per-login Agent permissions) |
| Deployments | Frequent runtime updates, often hourly, can replace the VM and stop its processes | [Prompt-described] system prompt "Deployments" section |
| Recovery | Runtime-managed for saved jobs, subagents, crons, artifacts, resumable agent work; custom programs must supply their own startup path | [Inspected] `~/docs/chat/scheduling-and-watching.md` "Recovery after replacement" |

**Design takeaway [Inference].** The durable unit is not the VM process but the
record: a saved job, a chat UUID, a memory file, a workflow run id. Anything
that must survive a VM replacement has to be re-derivable from those records.
That is why the docs obsess over "check run history, not the schedule" and
"a successful run does not prove delivery."

## 3. Persistence map (all paths [Inspected] from prompt + docs)

| What | Where | Notes |
|---|---|---|
| Agent identity/persona | `~/IDENTITY.md`, `~/SOUL.md`, `~/AGENTS.md`, `~/TOOLS.md` | Agent-owned, user-editable |
| Curated long-term memory | `~/MEMORY.md` | Promoted facts/preferences/commitments; not a transcript |
| Dated memory trail | `~/memory/YYYY-MM-DD.md`, `~/memory/bank/`, `~/memory/index/` | Runtime owns `bank/` and `index/`; agent reads, never edits directly |
| People / groups | `~/memory/people/`, `~/memory/groups/` (+ `INDEX.md` each) | One page per person/group, ordered by closeness |
| User-facing deliverables | `~/workspace/your_files/` | Only files the user is meant to see |
| Goal workspaces | `~/workspace/goals/<goal-slug>/` with `GOAL.md`, `files/` (user documents), `hidden_files/` (run logs, watermarks, snapshots) | Goal-owned cron output stays here |
| Cron definition copies | `workspace/cron.d/`, `workspace/goals/<goal-slug>/crons/`, `workspace/system-cron.d/` | READ-ONLY projections; editing them changes nothing — use `cron.view`/`cron.update` |
| Hook scripts / state | `~/hooks/scripts/*.sh`, `~/hooks/state/` | Scripts run without secrets or connector credentials |
| Saved workflows | Workspace saved-workflows directory (launched by name) | Script snapshots; runs keep the snapshot they launched with |
| System prompt snapshot | `~/workspace/system/system_prompt.md` | Saved by the runtime at startup; attached separately with this research |
| Chat transcripts | Server-side index + per-chat history | Agent reads via `chat.read_messages`; hidden system/background messages excluded |
| Run/step/decision records | `muse.db` (PostgreSQL-backed records) | Tracing via `muse.db` after reading `/opt/muse/skills/muse_db/references/schema.md` |
| Ephemeral scratch | `/tmp` | Deleted automatically or lost on restart; never hand a user a `/tmp` path |
| Outside-home paths (`/usr/local/bin`, `/etc`, …) | Ephemeral | Treated as lost on reboot/replacement |

## 4. Coordinator / worker context

**Main agent + subagents [Prompt-described + tool schemas].**

- A subagent spawned with `subagent.spawn` inherits the parent's current
  context. The spawn call is async: its response only confirms the spawn and
  returns an agent id. Results arrive later through the runtime as handoffs;
  the parent must not poll in a loop (`subagent.list` only to act on status).
- A coordinator pattern is explicit: when a task needs several subagents, spawn
  ONE coordinator and let it fan out; nesting stops there (a coordinator's
  subagents cannot spawn their own).
- A failed report does not prove nothing happened. Before repeating an
  irreversible action, establish its actual outcome. Closing a browser-task
  owner stops the whole browser task.
- Generic subagents may NOT do live-browser work, artifacts, or accepted Idea
  builds — those have dedicated routes (browser tasks, artifact tools).

**Workflows [Inspected: workflow tool definitions].**

- A separate, deterministic orchestration layer: VM-local JavaScript executed
  by a daemon, with globals `args`, `phase(...)`, `agent(...)`,
  `parallel(...)`, `pipeline(...)`, `log(...)`. No Node/fs/shell/browser APIs
  inside workflow code; real work is delegated to `agent()` calls with stable
  unique keys and optional JSON `options.schema` contracts.
- One pre-created shared working directory per execution. Final top-level
  return is the curated user-facing handback only — no child outputs, logs,
  or build debris.
- Recovery is status-specific: `resume` for paused runs; relaunch with
  `resumeFromRunId` for terminal failed runs (reuses completed stable-key
  child results); stopped/cancelled runs are terminal and must never be
  resumed or relaunched.

**Side-chat workers (the DM pattern) [Inspected: chat-connections docs +
messaging skill + chat tool definitions].**

- Every conversation has a chat UUID. A connected messaging app is a transport
  for a side chat; the transport never creates a second transcript and never
  chooses the recipient of another chat's reply.
- Main agent → worker: `chat.send_message` with the target `chat_id` and an
  instruction. For a group chat, the group's worker receives it as a private
  task; the instruction itself is never posted to the conversation.
- Worker → user: the worker sends private messages through the main agent.
  The main agent rewrites them as its OWN message to the user (with
  attribution when a specific person said/decided something), never a
  verbatim forward. Worker questions are never answered on the user's behalf,
  even when the answer seems known from memory.
- Discretion rules per chat live in `~/side-chats/<chat-id>/DISCRETION.md`:
  a default section plus a user-rules section replaced via
  `worker.update_discretion`. The worker applies that chat's discretion
  policy, which protects the user's own information.

## 5. Wakeups — how background work starts

| Mechanism | Trigger | Agent involvement per firing | Key constraints |
|---|---|---|---|
| `cron` (clock) | runonce / interval / daily / weekly / monthly / yearly | Full agent run with tools + judgment | Body injected verbatim; no start/end date, no fire-only-when condition (conditions go in the body); one-off vs recurring; `delivery` chat ids; owner required for reminders (`goal:<slug>` or a tracked item); blocked jobs pause themselves and retry at the next scheduled time |
| `hooks` (event-ish) | Bash poll script on an interval (5s–7d) ending in exactly one `silent` or `wake` | None unless `wake` fires, then one worker agent | No secrets/connector credentials in scripts; state under `~/hooks/state/`; new hooks start DISABLED; `dry_run` before `enable`; `disable_after_run` for terminal conditions |
| `systemd` services (guest) | Process supervision | None (program runs) | Guest boots minimal `default.target`, not `multi-user.target`; units + state must live under persistent home; no inherited tool credentials; foreground process, absolute paths, `Restart` policy |
| Background self-improvement | Hourly/daily/nightly cadence | Same agent, between conversations | Memory upkeep (hourly, new signal), relationships (hourly), idea curation (daily), studying (daily, overnight), dreaming (nightly), skill review (daily), quiet-moment pass (a few times/day max). The foreground agent never schedules these |
| Device data sources | Device push (per `device.describe` data_sources) | Handoff into the conversation | Some sources emit proactively; capabilities/permissions come from `device.describe`, never assumed |
| Browser tasks / subagents | Completion | Completion handoff to the parent | Use these instead of adding a monitor on top |

**Polling, not watching [Inspected].** Both crons and hooks poll. A change is
caught at the next check; a change that happens and reverses between checks is
missed entirely. Timing is loose (minutes early/late). Never promise detection
"the moment it happens." A watch also cannot block or reject a source event —
only tools on the source service can; a watch can only message afterward with
a link to act.

**Run vs. delivery [Inspected].** A succeeded run means the work finished, not
that anything reached the user. The worker's report arrives as a hidden handoff
to the main agent, which decides what the user sees (including silence via
`muse.nothing_to_do`). If a run fails or times out, it may end with no chat
message at all — the failure shows only in `cron.runs`. "Check the run history,
not the schedule."

## 6. How replies become clean DMs

This is the pipeline that turns an internal worker result into a message the
user actually sees in the right chat, without leaking other chats' content:

1. **Ownership is captured, not chosen [Inspected].** "A reply belongs to the
   chat that admitted the user message. The runtime captures that UUID and
   the current binding authority before execution; the model does not choose
   the reply surface." (`~/docs/chat-connections.md`)
2. **Scheduled results stay in their origin chat [Inspected].** A task created
   in a provider side chat delivers there; a main-chat task stays in main
   chat. `chat.send_message` cannot push a one-off message into a provider
   conversation from another chat. Reconnection cannot redirect queued work
   to a replacement account.
3. **Worker output is private until rewritten [Inspected].** The worker writes
   to the user, not to the main agent — so the main agent must not answer the
   worker's questions, approve its requests, or decide for the user. It
   passes the important context on in full (details, thanks, personal notes,
   image/file/page links) as its own message, attributing statements to the
   person who said them.
4. **Discretion is per-chat and explicit [Inspected].** The user's rules for
   a chat are recorded with `worker.update_discretion` whenever they state
   what may be shared/offered/discussed/done there — even in passing, even
   when answering a single question. A second approval of the same kind of
   share for the same contact/room becomes a standing rule for that room
   only. The main agent never filters the user's own messages for the
   worker; the worker applies the chat's policy.
5. **Provider specifics [Inspected].** WhatsApp side chat: one durable side
   chat titled `WhatsApp`; its history is not copied into main chat; replies
   and tasks scheduled from it return there; inbound polling runs on the
   paired-connection cadence; cursors, encryption material, link identity,
   and media state remain private to the runtime; there are no editable
   WhatsApp connection preferences; status never returns a pairing bearer.
   The connection is one-to-one and does not expose the user's other
   messages or personal sending identity.
6. **Outbound-to-people messages are a different path [Inspected].** A message
   sent through a connected account goes out as the user, under their name.
   It requires the user having asked for that specific person/group with
   settled content; the exact text and recipient are shown before sending
   unless the connector's approval card already shows them. Muse's own
   reminders/monitoring/status updates never go out through the user's
   accounts. Sends are once-only: a timeout does not prove failure, so the
   conversation is re-read before any retry, and retries never happen in
   the background.
7. **Approvals are a separate surface [Prompt-described + Inspected].**
   Permission prompts can arrive as push notifications with Allow/Deny
   (Android decides in the background; on Android, swiping away counts as
   Deny; iOS requires unlock + foreground). `permissions.list_pending`,
   `permissions.list_active`, and `permissions.history` are the read-only
   record. Approval applies to exactly what was approved; settings cannot
   grant a standing Allow for sending.

**Clean-DM recipe for a community implementation [Inference].** Bind every
inbound message to (chat_id, binding authority) at intake and thread that
binding through execution to delivery; never let the model pick a
destination. Keep worker output in a private channel and have a separate
rewrite step produce the user-visible message. Store per-room disclosure
rules as data, not as prompt folklore. Treat "run succeeded" and "user saw
it" as two different events with separate records.

## 7. Sanitized example payloads (RECONSTRUCTED shapes — not real payloads)

Every value below is a placeholder. Field names follow the shapes described in
the inspected docs and tool definitions; no real IDs, timestamps, or content
from any actual run are included.

### 7a. Scheduled-task handoff (cron run → main agent)

```json
{
  "job_id": "example-weekly-check",
  "run_id": "00000000-0000-0000-0000-000000000000",
  "mode": "task",
  "scheduled_for_local": "2026-01-05T09:30:00 America/Los_Angeles",
  "task_context": "One-off reminder: <the job body, injected verbatim>",
  "delivery_targets": [{"chat_id": "00000000-0000-0000-0000-000000000001"}],
  "worker_report": "<worker's internal report; written for the agent, not the user>",
  "recovery_snapshot": {"status": "running", "delivery_recovery": null}
}
```

Reading note [Prompt-described]: the handoff is internal. The main agent
decides delivery (send, or `muse.nothing_to_do`) and must check the current
conversation for a user-visible message that actually conveyed the result
before treating anything as delivered.

### 7b. Side-chat worker task → clean DM

```json
// Main agent → worker (private task, never posted to the room)
{"tool": "chat.send_message",
 "chat_id": "00000000-0000-0000-0000-000000000002",
 "message": "<instruction for the worker: what to do in the room>"}

// Worker → main agent (private handoff, not user-visible)
{"from_worker": true, "room": "Example Room",
 "report": "<what happened, who said/decided what, links/files if any>"}

// Main agent → user (own message in the originating chat)
"<rewritten message in the agent's voice, attributing statements to the
  person who said them, with the details and links that matter>"
```

### 7c. Hook wake payload

```bash
# ~/hooks/scripts/example-watch.sh (shape only)
#!/usr/bin/env bash
set -euo pipefail
source "$HATCH_HOOK_RUNTIME"
# ... bounded fetch, jq parse, state in ~/hooks/state/ ...
# Exactly one terminal decision:
wake "example-condition-met" '{"changed_field": "example-value"}'
# or: silent "no-change" '{}'
```

The worker launched after `wake` receives the reason + payload as event data
alongside the hook's `prompt` instruction, then decides whether the main
agent should be notified.

### 7d. Cron creation shape (fields only)

```json
{"id": "example-reminder", "title": "Example reminder",
 "mode": "task", "enabled": true, "owner": "goal:example-goal",
 "schedule": {"kind": "daily", "time": "09:30", "timezone": "America/Los_Angeles"},
 "body": "<full task intent, injected verbatim at fire time>",
 "delivery": [{"chat_id": "00000000-0000-0000-0000-000000000001"}],
 "predicted_connector_permissions": [],
 "timeout_secs": 3600}
```

## 8. Exact gaps — what this research does NOT establish

1. **Server-side internals are unobserved.** Model hosting, the scheduler's
   implementation, the handoff transport, push infrastructure, and the
   message index are described only by the vendor's prompt/docs. Nothing
   here was measured against a server.
2. **No version stamp.** No tool definition, doc, or file read in this
   session carried a runtime version number, so the schemas cannot be pinned
   to a release. Re-check with `tool_search.load_tool_namespace` on the
   target system before building against them.
3. **Connector command shapes are missing by design.** The request forbade
   touching connected accounts, so no connector CLI (Gmail, Calendar,
   Drive, Spotify, Messenger, etc.) was read or transcribed. Those docs live
   at `/opt/hatch/connectors/<connector>/CONNECTOR.md`.
4. **Browser internals are prompt-described only.** The browser login agent,
   approval-card rendering, CAPTCHA handling, and profile cookie behavior
   were not inspected (no browser task was run for this research).
5. **`~/docs/browser.md`, `~/docs/artifacts.md`, `~/docs/feed.md`,
   `~/docs/goals.md`, `~/docs/ideas.md`, and the `muse.db` schema reference
   were not read.** They may add detail on browser behavior, artifacts,
   Feed/Ideas pipelines, goals, and run tracing. The `muse.db` schema path
   is `/opt/muse/skills/muse_db/references/schema.md`.
6. **Widget, artifact, feed, idea, goal, tracking, shopping, social, map,
   media, avatar, and UI namespaces are not in the schema file.** They were
   outside the requested scope and were not loaded.
7. **WhatsApp is the only provider guide read.** Other provider guides under
   `~/docs/chat-connections/` (if any exist on a given system) were not
   enumerated beyond the directory listing, and provider behavior varies by
   account.
8. **The attached system prompt is a startup snapshot.** The live prompt in
   a session also carries injected context files, conversation state, and
   compaction summaries that are not in that file. It was scanned for the
   user's name and email addresses (zero matches) but was not line-edited;
   if your build needs a redacted variant, say so and one can be produced
   from it with redactions marked.
9. **No child agent was used.** The permitted one temporary
   architecture-only child agent was not spawned because direct inspection
   answered every question; there is therefore no independent second-pass
   verification in this package. An independent pass can be run on request.
10. **Example payloads are reconstructions.** Section 7 shows field shapes
    inferred from docs and tool definitions, not captured wire payloads.
    Real payloads may carry additional fields (delivery receipts, retry
    metadata, approval ids) that are only named in prose here.

## 9. Sources inspected in this session

- `~/workspace/system/system_prompt.md` (72,867 bytes; scanned: zero matches
  for the user's name/email identifiers — attached separately, unedited)
- `~/docs/chat-connections.md`, `~/docs/chat-connections/whatsapp.md`
- `~/docs/scheduling-and-watching.md`, `~/docs/chat/scheduling-and-watching.md`
- `~/docs/self_improvement.md`, `~/docs/memory.md`, `~/docs/client-surfaces.md`
- `/opt/muse/skills/messaging/SKILL.md`
- Tool definitions: `muse`, `subagent`, `permissions`, `worker` (session tool
  list); `chat`, `cron`, `hooks`, `workflow`, `device` (loaded in-session);
  `browser` (loaded earlier in-session)
- Deliberately NOT read: any connected account, credential store, mailbox,
  calendar, personal memory file, or personal chat transcript.
