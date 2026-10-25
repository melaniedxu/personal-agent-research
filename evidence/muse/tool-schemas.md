# Tool schemas — personal-agent runtime (transcribed in-session)

**Provenance and honesty label.** [Inspected] Every function name, parameter name,
parameter type, enum, pattern, and `required` list below was transcribed from the
tool definitions visible to the agent in this session on 2026-10-24: the `muse`,
`subagent`, `permissions`, and `worker` definitions shipped in the session tool list,
plus the `chat`, `cron`, `hooks`, `workflow`, and `device` definitions returned by
`tool_search.load_tool_namespace`, and the `browser` definitions returned by an
earlier load in this same session. Descriptions are quoted verbatim where short.
Two long prose blocks are flagged `[summary]` instead of quoted: the `cron`
schedule-field description and the `workflow` authoring contract — their parameter
structures are still given in full. No version number was observed in any
definition, so these schemas may drift across runtime releases; treat the live
runtime as canonical.

**Scope note.** This file covers only the namespaces the research request named:
messaging (`chat`, `worker`), subagents (`subagent`), scheduled work (`cron`),
event hooks (`hooks`), workflows (`workflow`), permissions (`permissions`),
browser (`browser`), memory (`muse.memory_*`), and devices (`device`). The `muse`
core helpers used alongside them are included for completeness. Connector CLIs
(Gmail, Calendar, Spotify, etc.) are intentionally NOT included: reading them
would have meant touching connected accounts, which the request forbade.
No personal data, account IDs, or real chat/message IDs appear anywhere below;
all IDs in examples are placeholders.

---

## 1. `muse` — core agent tools

### `muse.connector_search`
Find connectors by name, alias or the action you need. Searches their names,
aliases and descriptions; returns each match's name, docs path and description.
Does not connect accounts or perform actions.
```json
{"properties": {"maxResults": {"type": "integer", "minimum": 1, "default": 8},
  "queries": {"type": "array", "items": {"type": "string"}, "minItems": 1, "maxItems": 5}},
 "required": ["queries"]}
```

### `muse.create_options`
For a known, bounded choice, returns an `embed_token` to place unchanged in the
reply. Tapping an option sends its exact text as the user's next message.
```json
{"properties": {"button_style": {"type": "string", "enum": ["dotted_lines", "center_aligned_filled"], "default": "dotted_lines"},
  "options": {"type": "array", "items": {"type": "string"}, "minItems": 1, "uniqueItems": true}},
 "required": ["options"]}
```

### `muse.db`
Run bounded, read-only SQL SELECT queries against database-backed Muse records
(transcripts, messages, agent executions, tool calls, goals, memories, scheduled
work, Feed/Ideas records, artifacts, device-sync data). Requires reading
`/opt/muse/skills/muse_db/references/schema.md` first.
```json
{"properties": {"sql": {"type": "string"}},
 "required": ["sql"]}
```

### `muse.edit`
Edit a file by replacing exact text. `old_text` must match exactly, including
whitespace. First occurrence is replaced.
```json
{"properties": {"path": {"type": "string"}, "old_text": {"type": "string"}, "new_text": {"type": "string"}},
 "required": ["path", "old_text", "new_text"]}
```

### `muse.exec`
Execute a shell command. Backgrounds after `yield_ms` (default 10000) and the
runtime delivers the terminal result automatically.
```json
{"properties": {"command": {"type": "string"}, "background": {"type": "boolean"},
  "env": {"type": "object"}, "pty": {"type": "boolean"}, "stdin": {"type": "string"},
  "workdir": {"type": "string"}, "yield_ms": {"type": "integer"}},
 "required": ["command"]}
```

### `muse.memory_explain`
Show where one memory came from and what replaced what. Accepts a claim id, a
`memory://` URI, or a citation like `MEMORY.md#L7`.
```json
{"properties": {"target": {"type": "string"}}, "required": ["target"]}
```

### `muse.memory_get`
Read a snippet from `~/MEMORY.md`, `~/memory/**/*.md`, or side-chat memory files.
```json
{"properties": {"path": {"type": "string"}, "from": {"type": "number"}, "lines": {"type": "number"}},
 "required": ["path"]}
```

### `muse.memory_search`
Search saved memory and past conversations. Results have separate sections
(Memories; Past conversations). `maxResults` limits each source separately.
```json
{"properties": {"queries": {"type": "array", "items": {"type": "string"}, "minItems": 1, "maxItems": 3},
  "maxResults": {"type": "number", "default": 6},
  "minScore": {"type": "number"}},
 "required": ["queries"]}
```

### `muse.nothing_to_do`
Signal that an internal handoff should produce no user-visible reply because the
content is stale, duplicate, or not worth surfacing. Takes no input arguments.
```json
{"properties": {}, "required": []}
```

### `muse.offer_preference`
After a connector completes a task, check whether to ask about making it the
preferred connector for that task category. Returns `should_offer` at most once
per category.
```json
{"properties": {"name": {"type": "string"}, "category": {"type": "string", "minLength": 1, "maxLength": 80}},
 "required": ["name", "category"]}
```

### `muse.react_to_user_message`
Attach one emoji reaction to the user's current message.
```json
{"properties": {"emoji": {"type": "string"}}, "required": ["emoji"]}
```

### `muse.read`
Read file contents or list directory contents. Text files are returned whole-line
with optional offset/limit; images are injected into model context; documents
(PDF/Word/Excel/PowerPoint/ODF/EPUB/RTF) are converted to Markdown and paged.
```json
{"properties": {"path": {"type": "string"}, "offset": {"type": "integer", "minimum": 1}, "limit": {"type": "integer", "minimum": 1}},
 "required": ["path"]}
```

### `muse.session_status`
Report how much of the conversation's context window is filled and remains, in
tokens, plus the model serving the conversation and the user's local time.
```json
{"properties": {}, "required": []}
```

### `muse.set_preferred`
Save or clear the skill or connector the user prefers for a kind of task.
```json
{"properties": {"name": {"type": "string"}, "preferred": {"type": "boolean"}, "for": {"type": "string"}},
 "required": ["name", "preferred"]}
```

### `muse.skill_search`
Search the full skill catalog (bundled skills in `/opt/muse/skills` and custom
skills in `~/workspace/custom-skills`). `bm25` (default) ranks by keyword;
`regex` matches a case-insensitive pattern over names and descriptors.
```json
{"properties": {"queries": {"type": "array", "items": {"type": "string"}, "minItems": 1, "maxItems": 5},
  "maxResults": {"type": "number", "default": 8, "maximum": 25},
  "mode": {"type": "string", "enum": ["bm25", "regex"]}},
 "required": ["queries"]}
```

### `muse.visual_grounding`
Locate, label, or count objects in an image, returning normalized 0–1000
coordinates. `format_type`: `bbox`, `point`, or `count`.
```json
{"properties": {"image_path": {"type": "string"}, "object_names": {"type": "array", "items": {"type": "string"}},
  "title": {"type": "string"}, "format_type": {"type": "string", "enum": ["bbox", "point", "count"]}},
 "required": ["object_names", "image_path"]}
```

### `muse.write`
Write content to a file. Default mode overwrites; `append` adds to the end.
Overwriting a file that already has content fails unless it was read earlier
in the conversation.
```json
{"properties": {"path": {"type": "string"}, "content": {"type": "string"},
  "mode": {"type": "string", "enum": ["overwrite", "append"], "default": "overwrite"}},
 "required": ["path", "content"]}
```

---

## 2. `subagent` — child agents (coordinator / worker pattern)

Namespace rule (from the tool definitions): a spawned child inherits the
parent's current context; results arrive later through the runtime; never poll
or treat the spawn receipt as completion. Browser work, artifacts, and accepted
Idea builds must NOT be spawned as generic children.

### `subagent.spawn`
Delegate a self-contained task to a new child agent running in the background.
Async: the response only confirms the spawn and returns the new agent id.
```json
{"properties": {"message": {"type": "string"},
  "items": {"type": "array", "items": {"type": "object", "properties": {
    "type": {"type": "string", "enum": ["text", "image", "file"]},
    "text": {"type": "string"}, "mime_type": {"type": "string"},
    "data_base64": {"type": "string"}, "filename": {"type": "string"}, "caption": {"type": "string"}},
    "required": ["type"]}}},
 "required": []}
```

### `subagent.list`
List child agents (direct, or full subtree with `scope: descendants`), grouped
into active and recent, with normalized status (running, done, interrupted,
failed), timing, and whether a finished result was already seen.
```json
{"properties": {"limit": {"type": "integer", "default": 20, "maximum": 200},
  "scope": {"type": "string", "enum": ["direct", "descendants"], "default": "direct"}},
 "required": []}
```

### `subagent.send`
Deliver follow-up input to a running child agent. Async: success means the
message was submitted, not applied. `interrupt: true` cuts off current work
first. Browser task owners cannot be steered by agent id.
```json
{"properties": {"id": {"type": "string"}, "message": {"type": "string"},
  "items": {"type": "array", "items": {"type": "object"}},
  "interrupt": {"type": "boolean"},
  "scope": {"type": "string", "enum": ["direct", "descendants"], "default": "direct"}},
 "required": ["id"]}
```

### `subagent.resume`
Resume an interrupted child agent so it continues its existing task. Only a
paused/interrupted agent can be resumed; terminal agents cannot.
```json
{"properties": {"id": {"type": "string"},
  "scope": {"type": "string", "enum": ["direct", "descendants"], "default": "direct"}},
 "required": ["id"]}
```

### `subagent.close`
Stop a child agent by id and end its work. Closing a browser task owner stops
the whole browser task.
```json
{"properties": {"id": {"type": "string"},
  "scope": {"type": "string", "enum": ["direct", "descendants"], "default": "direct"}},
 "required": ["id"]}
```

---

## 3. `permissions` — approval records (read-only)

### `permissions.history`
Read resolved permission requests as Markdown, newest first, or look up one
pending/resolved request by `approval_id`.
```json
{"properties": {"approval_id": {"type": "string", "maxLength": 128}, "cursor": {"type": "string", "maxLength": 1024}},
 "required": []}
```

### `permissions.list_active`
List current permission settings and grants, including scope and expiry.
```json
{"properties": {"cursor": {"type": "string", "maxLength": 1024}}, "required": []}
```

### `permissions.list_pending`
List permission requests currently waiting for the user (newest first, max 20
per page). `remaining_count` reports older requests remaining.
```json
{"properties": {"cursor": {"type": "string", "maxLength": 1024}}, "required": []}
```

---

## 4. `worker` — side-chat discretion rules

### `worker.update_discretion`
Replace the user's own rules in a side chat's `~/side-chats/<chat-id>/DISCRETION.md`.
`guidance` becomes everything after the `default-discretion:end` marker; the
runtime keeps the default section. Works only on the user's own turn; otherwise
the user approves it on a card first.
```json
{"properties": {"chat_id": {"type": "string"}, "guidance": {"type": "string"}},
 "required": ["chat_id", "guidance"]}
```

---

## 5. `chat` — messaging: chats, side chats, and worker tasks

Namespace rule (from the tool definitions): `chat.list` resolves chats by name;
a group's entry has its room name and people, a contact's entry has the contact's
name. `chat.send_message` to a group reaches the group's worker as a private task;
the worker's reply comes back privately to the main agent, which rewrites it as
its own message to the user (never a verbatim forward).

### `chat.archive`
Archive a side chat so it leaves the active chat list. History is kept; it still
appears in `chat.list` with `include_archived: true`. The main chat cannot be
archived. For permanent removal use `chat.delete`, only when explicitly asked.
```json
{"properties": {"chat_id": {"type": "string"}}, "required": ["chat_id"]}
```

### `chat.configure_connection`
Read or update a connected provider's preferences. Omit `settings` to read;
supply a partial settings object to update. Requires the user's own Muse chat.
Linking/disconnecting use separate flows. Provider guides live in
`~/docs/chat-connections/<provider>.md`.
```json
{"properties": {"provider": {"type": "string", "enum": ["whatsapp"]}, "settings": {"type": "object", "additionalProperties": true}},
 "required": ["provider"]}
```

### `chat.connection_status`
Check a connection that supplies side chats (providers: whatsapp). Call before
`chat.disconnect`. Connecting uses a secure in-app link.
```json
{"properties": {"provider": {"type": "string", "enum": ["whatsapp"]}}, "required": ["provider"]}
```

### `chat.create`
Create a new side chat: a separate persistent 1:1 Muse conversation alongside
the main chat. Never a group chat; no way to add people. `context_mode` is
required: `fork` (starts with the main chat's history; only from the main chat)
or `fresh` (no prior context). The optional `message` seeds context/title only
and is NOT delivered as a message; use `chat.send_message` to give the new
chat's agent something to do.
```json
{"properties": {"context_mode": {"type": "string", "enum": ["fork", "fresh"]},
  "message": {"type": "string"}, "name": {"type": "string", "maxLength": 120}},
 "required": ["context_mode"]}
```

### `chat.delete`
Permanently delete a side chat, including its history. Irreversible; only when
the user explicitly asks. The main chat cannot be deleted.
```json
{"properties": {"chat_id": {"type": "string"}}, "required": ["chat_id"]}
```

### `chat.disconnect`
Disconnect a side-chat provider (providers: whatsapp). Call
`chat.connection_status` first. Requires the user's own Muse chat. History
remains available.
```json
{"properties": {"provider": {"type": "string", "enum": ["whatsapp"]}}, "required": ["provider"]}
```

### `chat.list`
List the user's Muse chats: one entry per chat with `chat_id` UUID, name,
whether it is the Main chat, archived/pinned flags, and status. A chat
connected to an external messaging service also includes `provider`. A group
chat is named after its room and includes `group` (room name, display names of
people in it, when its latest message was sent). Default: active chats only.
```json
{"properties": {"include_archived": {"type": "boolean", "default": false}}, "required": []}
```

### `chat.read_messages`
Read an existing main or side chat. With `message_id`, returns that message plus
surrounding messages (defaults: 2 before, 2 after; capped at 20 each). Do not
combine `message_id` with `cursor` or `limit`. Without `message_id`, supply
`chat_id` to browse turns newest first (`limit` default 5, max 20; `cursor`
pages older). Private worker handoffs are excluded from group transcripts.
Reading does not contact the other agent or change the chat.
```json
{"properties": {"message_id": {"type": "string", "minLength": 1},
  "chat_id": {"type": "string"}, "before": {"type": "integer", "minimum": 0, "maximum": 20, "default": 2},
  "after": {"type": "integer", "minimum": 0, "maximum": 20, "default": 2},
  "limit": {"type": "integer", "minimum": 1, "maximum": 20, "default": 5},
  "cursor": {"type": "string"}},
 "required": []}
```

### `chat.rename`
Rename an existing chat (display title, at most 120 characters; extra
whitespace is collapsed).
```json
{"properties": {"chat_id": {"type": "string"}, "name": {"type": "string", "maxLength": 120}},
 "required": ["chat_id", "name"]}
```

### `chat.send_message`
Send an instruction to another chat by `chat_id`. For a native chat, that
chat's agent gets the instruction and responds in that chat. For a group chat,
the group's worker gets it as a private task. Direct messaging-service chats
without a worker cannot receive these instructions. Returns immediately with
`submission_message_id`; the receipt does not confirm delivery or completion.
```json
{"properties": {"chat_id": {"type": "string"}, "message": {"type": "string"}},
 "required": ["chat_id", "message"]}
```

### `chat.unarchive`
Restore an archived side chat to the active list. Use an exact `chat_id` from
`chat.list` with `include_archived: true`. The main chat is always active.
```json
{"properties": {"chat_id": {"type": "string"}}, "required": ["chat_id"]}
```

---

## 6. `cron` — scheduled work (clock-driven agent tasks)

Namespace rules (from the tool definitions, condensed): definition files under
`workspace/cron.d/`, `workspace/goals/<goal-slug>/crons/`, and
`workspace/system-cron.d/` are READ-ONLY copies; editing them does not change
the saved job — use `view` + `update` with the same id and the complete revised
body. System cron jobs cannot be added, updated, disabled, or removed here.
A reminder cron with no owner is a routing error: goal-owned jobs use
`owner: "goal:<goal-slug>"`, otherwise create/log a tracked item first. Job
bodies are injected verbatim when the job fires. `mode` must be `task`.
Recurring kinds have no start/end date and no fire-only-when condition;
conditions belong in the job body. `timeout_secs`: 1–86400; recurring jobs get
at least the interval between runs, up to 86400; one-offs default to 86400.
Quarter-hour-aligned runs may dispatch up to five minutes early.

Shared parameter shapes (identical in `add` and `update` unless noted):

```json
{"schedule": {"type": "object", "properties": {
  "kind": {"type": "string", "enum": ["runonce", "interval", "daily", "weekly", "monthly", "yearly"]},
  "at": {"type": "string", "pattern": "^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}(:\\d{2})?$"},
  "every": {"type": "string", "pattern": "^\\d+\\s*[smh]$"},
  "time": {"type": "string", "pattern": "^\\d{2}:\\d{2}(:\\d{2})?$"},
  "dow": {"type": "array", "items": {"type": "string"}},
  "dom": {"type": "array", "items": {"type": "integer"}},
  "month": {"type": "array", "items": {"type": "integer"}},
  "timezone": {"type": "string"},
  "flexible_time": {"type": "boolean"}},
  "required-by-kind": {
    "runonce": ["at"], "interval": ["every"], "daily": ["time"],
    "weekly": ["time", "dow"], "monthly": ["time", "dom"], "yearly": ["time", "dom", "month"]}},
 "execution": {"type": "object", "properties": {
  "kind": {"type": "string", "enum": ["agent", "space_action"]},
  "slug": {"type": "string"}, "action": {"type": "string"}, "args": {"type": "object"}},
  "required": ["kind"]},
 "delivery": {"type": "array", "items": {"type": "object", "properties": {
  "chat_id": {"type": "string", "format": "uuid"}}, "required": ["chat_id"]}},
 "retry": {"type": "object", "properties": {
  "max_retries": {"type": "integer", "default": 0}, "on_failure": {"type": "boolean", "default": false}}},
 "predicted_connector_permissions": {"type": "array", "maxItems": 32, "uniqueItems": true,
  "items": {"type": "object", "properties": {
    "connector": {"type": "string", "pattern": "^[a-z0-9_.-]+$", "maxLength": 64},
    "method": {"type": "string", "pattern": "^[a-z0-9_.-]+$", "maxLength": 64}},
    "required": ["connector", "method"]}},
 "title": {"type": "string", "maxLength": 120, "pattern": "^[^\\r\\n]*$"},
 "timeout_secs": {"type": "integer", "minimum": 1, "maximum": 86400},
 "body": {"type": "string"}, "text": {"type": "string"},
 "owner": {"type": "string"},
 "enabled": {"type": "boolean"}, "mode": {"type": "string", "enum": ["task"]}}
```

Notes on the schedule field [summary, not verbatim]: `timezone` may be omitted
on add and defaults to the user's current timezone; recurring kinds may store
`@user.current`, `@user.home`, or `@user.work` (the latter two require matching
keys in `user/timezones.yaml`); runonce/interval need a literal IANA zone.
`dow` values are `Mon..Sun` and are honored only for `weekly`. There is no
nth-weekday-of-month kind. For `interval`, omitting `at` phases the cadence
from authoring time. A past `at` on runonce is accepted and fires an immediate
catch-up run. The `body` must not name the terminal tools `nothing_to_do`,
`nothing_to_report`, or `notify_main_agent` (validation rejects those names).

### `cron.add`
Add a new scheduled cron job. Check `list` first and reuse/update instead of
creating overlapping schedules.
```json
{"properties": {"id": {"type": "string"}, "schedule": {"$ref": "#schedule"}, "enabled": {"type": "boolean"},
  "mode": {"type": "string", "enum": ["task"]}, "body": {"type": "string"}, "text": {"type": "string"},
  "title": {"type": "string"}, "owner": {"type": "string"}, "delivery": {"$ref": "#delivery"},
  "execution": {"$ref": "#execution"}, "retry": {"$ref": "#retry"},
  "predicted_connector_permissions": {"$ref": "#predicted_connector_permissions"},
  "timeout_secs": {"type": "integer"}},
 "required": ["id", "predicted_connector_permissions", "enabled", "mode", "schedule"]}
```

### `cron.list`
List schedule summaries with lifecycle owners.
```json
{"properties": {"include_disabled": {"type": "boolean"}}, "required": []}
```

### `cron.view`
View one schedule's details by id.
```json
{"properties": {"id": {"type": "string"}}, "required": ["id"]}
```

### `cron.update`
Update an existing schedule. Omitted fields stay the same, except: leaving out
`at` when switching to an interval lets the runtime choose a start, and a body
change clears old `predicted_connector_permissions` unless a refreshed set is
supplied. On update, do not pass `slug`/`action`/`args` with `kind: agent`.
```json
{"properties": {"id": {"type": "string"}, "schedule": {"$ref": "#schedule"}, "enabled": {"type": "boolean"},
  "mode": {"type": "string", "enum": ["task"]}, "body": {"type": "string"}, "text": {"type": "string"},
  "title": {"type": "string"}, "owner": {"type": "string"}, "delivery": {"$ref": "#delivery"},
  "execution": {"$ref": "#execution"}, "retry": {"$ref": "#retry"},
  "predicted_connector_permissions": {"$ref": "#predicted_connector_permissions"},
  "timeout_secs": {"type": "integer"}},
 "required": ["id"]}
```

### `cron.remove`
Remove a schedule by `id`. Removing revokes its scoped permissions.
```json
{"properties": {"id": {"type": "string"}}, "required": ["id"]}
```

### `cron.run`
Enqueue an immediate manual run of a schedule by `id`.
```json
{"properties": {"id": {"type": "string"}, "reason": {"type": "string"}}, "required": ["id"]}
```

### `cron.runs`
Recent run records (status, timing, attempt, error text), optionally scoped to
one schedule by `id`.
```json
{"properties": {"id": {"type": "string"}, "limit": {"type": "number"}}, "required": []}
```

### `cron.status`
Scheduler-wide counts of enabled jobs, queued runs, and running runs. Scoped
by `id` it reports that job's state: enabled, schedule, last run time/status,
queued/running runs, next run time.
```json
{"properties": {"id": {"type": "string"}}, "required": []}
```

### `cron.stop`
Stop a schedule's in-flight run by `id` (its worker, subagents, and browser
windows included); records it as cancelled by the user and notifies the job's
chat. When nothing is running, pending queued occurrences are cancelled
silently. The schedule itself is unchanged and still fires next time; use
`update` with `enabled: false` to pause, `remove` to delete.
```json
{"properties": {"id": {"type": "string"}, "run": {"type": "string"}},
 "required": ["id"]}
```

---

## 7. `hooks` — event-driven automations (polling scripts that wake an agent)

Namespace rules (from the tool definitions): a hook has two parts — (1) a Bash
polling script ending in `.sh` under `~/hooks/scripts/`, written with
`#!/usr/bin/env bash`, `set -euo pipefail`, and `source "$HATCH_HOOK_RUNTIME"`;
it runs through the normal tracked shell executor WITHOUT secrets or connector
credentials; it must end with exactly one `silent "reason" '{...}'` or
`wake "reason" '{...}'`; state lives under `~/hooks/state/`; `HATCH_HOOK_DRY_RUN`
is `1` for dry runs, `0` otherwise; `disable_after_run` marks a terminal
condition. (2) A worker instruction launched after `wake`; wake reason and
payload arrive automatically as event data. A new hook starts DISABLED; test
with `dry_run`, inspect the result, then `enable`. Poll intervals: 5–604800
seconds (default 60). Script timeout: 1–600 seconds (default 600).

### `hooks.add`
Add an event hook definition. Write the script first, then register it. A new
hook starts disabled.
```json
{"properties": {"id": {"type": "string", "pattern": "^[a-z0-9][a-z0-9_-]{0,63}$"},
  "script_path": {"type": "string"}, "prompt": {"type": "string"},
  "poll_interval_secs": {"type": "integer", "minimum": 5, "maximum": 604800, "default": 60},
  "script_timeout_secs": {"type": "integer", "minimum": 1, "maximum": 600, "default": 600},
  "delivery": {"type": "array", "maxItems": 1, "minItems": 1, "items": {"type": "object",
    "properties": {"surface": {"type": "string", "enum": ["main", "side_chat"]},
      "to": {"type": "string"}}, "required": ["surface"]}}},
 "required": ["id", "script_path", "prompt"]}
```

### `hooks.view` / `hooks.list` / `hooks.enable` / `hooks.disable` / `hooks.remove`
```json
{"hooks.view": {"properties": {"id": {"type": "string", "pattern": "^[a-z0-9][a-z0-9_-]{0,63}$"}}, "required": ["id"]},
 "hooks.list": {"properties": {"include_disabled": {"type": "boolean"}}, "required": []},
 "hooks.enable": {"properties": {"id": {"type": "string", "pattern": "^[a-z0-9][a-z0-9_-]{0,63}$"}}, "required": ["id"]},
 "hooks.disable": {"properties": {"id": {"type": "string", "pattern": "^[a-z0-9][a-z0-9_-]{0,63}$"}}, "required": ["id"]},
 "hooks.remove": {"properties": {"id": {"type": "string", "pattern": "^[a-z0-9][a-z0-9_-]{0,63}$"}}, "required": ["id"]}}
```

### `hooks.dry_run`
Synchronously test only the script with `HATCH_HOOK_DRY_RUN=1` and no
wake/disable side effects; it does not isolate script-managed state.
```json
{"properties": {"id": {"type": "string", "pattern": "^[a-z0-9][a-z0-9_-]{0,63}$"}}, "required": ["id"]}
```

### `hooks.run`
Live run with `HATCH_HOOK_DRY_RUN=0`: a wake starts the asynchronous agent
lifecycle.
```json
{"properties": {"id": {"type": "string", "pattern": "^[a-z0-9][a-z0-9_-]{0,63}$"}}, "required": ["id"]}
```

### `hooks.logs`
Recent entries from the hook's append-only JSONL invocation log.
```json
{"properties": {"id": {"type": "string", "pattern": "^[a-z0-9][a-z0-9_-]{0,63}$"},
  "limit": {"type": "integer", "minimum": 1, "maximum": 200}}, "required": ["id"]}
```

### `hooks.update`
Update an event hook definition in place. The hook's current enabled state is
preserved; after updating, test with `dry_run`.
```json
{"properties": {"id": {"type": "string", "pattern": "^[a-z0-9][a-z0-9_-]{0,63}$"},
  "script_path": {"type": "string"}, "prompt": {"type": "string"},
  "poll_interval_secs": {"type": "integer", "minimum": 5, "maximum": 604800},
  "script_timeout_secs": {"type": "integer", "minimum": 1, "maximum": 600},
  "delivery": {"type": "array", "maxItems": 1, "minItems": 1, "items": {"type": "object",
    "properties": {"surface": {"type": "string", "enum": ["main", "side_chat"]},
      "to": {"type": "string"}}, "required": ["surface"]}}},
 "required": ["id"]}
```

---

## 8. `workflow` — VM-local JavaScript workflows (deterministic multi-agent orchestration)

Authoring contract [summary — full contract text lives in the live tool
definition]: scripts are self-contained, begin with exactly one literal
`export const meta = { name, description, phases }` object, then top-level
statements calling the runtime globals `args`, `phase(...)`, `agent(...)`,
`parallel(...)`, `pipeline(...)`, `log(...)`. No metadata shorthand, no
`export default`, no exported `run()`, no CommonJS, no imports/`require`. No
Node/filesystem/shell/browser APIs, no `Date.now()`, argless `new Date()`, or
`Math.random()` in workflow code — delegate real work to `agent()` calls.
`agent(prompt, options)` requires a stable unique `key`; with `options.schema`
the child must return a JSON envelope with `status` and `result`, and the
runtime unwraps `result`. `parallel()` runs independent work concurrently and
returns results in input order (non-fatal item failure → `null`). `pipeline()`
runs every item through stages independently with no barrier. Each execution
gets one pre-created shared working directory under the hidden workflow run
directory. Final top-level return is the curated user-facing handback only.
Blocked control result: `{ __hatchWorkflowControl: "blocked", result: {...} }`.
Run recovery: `resume` for paused runs; relaunch with `resumeFromRunId` for
terminal failed runs (reuses completed stable-key child results); stopped or
cancelled runs are terminal and must never be resumed or relaunched.

### `workflow.create` / `workflow.update` / `workflow.delete` / `workflow.view`
Saved workflows live in the workspace's saved-workflows directory and are
launched by name. Creating only stores the script and never runs it. `create`
fails if the name exists (use `update`); `update` fails if it does not exist.
`view` returns script source plus metadata (declared name, description,
phases, script path, hash, last-updated time).
```json
{"workflow.create": {"properties": {"name": {"type": "string"}, "script": {"type": "string"}}, "required": ["name", "script"]},
 "workflow.update": {"properties": {"name": {"type": "string"}, "script": {"type": "string"}}, "required": ["name", "script"]},
 "workflow.delete": {"properties": {"name": {"type": "string"}}, "required": ["name"]},
 "workflow.view": {"properties": {"name": {"type": "string"}}, "required": ["name"]}}
```

### `workflow.launch` / `workflow.launch_async`
Launch a workflow and wait for it to resolve (`launch`), or return immediately
with the run id (`launch_async`). Exactly one script source: `scriptPath`
(highest precedence), `script`, or `name`. `args` is a structured object
exposed verbatim as the global `args`.
```json
{"properties": {"scriptPath": {"type": "string"}, "script": {"type": "string"}, "name": {"type": "string"},
  "args": {"type": "object"}, "resumeFromRunId": {"type": "string"}},
 "required": []}
```

### `workflow.list` / `workflow.list_runs`
`list`: saved scripts only (name, declared name, description, phases, path,
hash, last-updated; default limit 100, max 200). `list_runs`: runs from this
root session (id, workflow name, status, timing; default limit 100, max 200).
```json
{"workflow.list": {"properties": {"limit": {"type": "integer", "minimum": 1, "maximum": 200, "default": 100}}, "required": []},
 "workflow.list_runs": {"properties": {"limit": {"type": "integer", "minimum": 1, "maximum": 200}}, "required": []}}
```

### `workflow.view_run`
View one run: status, phase progress, child agent calls with call ids, timing,
final result or error. Only runs belonging to this root session are visible.
```json
{"properties": {"runId": {"type": "string"}}, "required": ["runId"]}
```

### `workflow.pause` / `workflow.resume` / `workflow.stop` / `workflow.stop_agent` / `workflow.save_run`
`pause`: only a queued/running run changes state; terminal runs cannot pause.
`resume`: only a paused run that can continue without new user input.
`stop`: terminal — a stopped run must never be resumed or relaunched.
`stop_agent`: stops one child call inside a running run (needs `callId`).
`save_run`: saves a run's verified script snapshot as a saved workflow (name
defaults to the run's workflow name; overwrites same-name scripts).
```json
{"workflow.pause": {"properties": {"runId": {"type": "string"}}, "required": ["runId"]},
 "workflow.resume": {"properties": {"runId": {"type": "string"}}, "required": ["runId"]},
 "workflow.stop": {"properties": {"runId": {"type": "string"}}, "required": ["runId"]},
 "workflow.stop_agent": {"properties": {"runId": {"type": "string"}, "callId": {"type": "string"}}, "required": ["runId", "callId"]},
 "workflow.save_run": {"properties": {"runId": {"type": "string"}, "name": {"type": "string"}}, "required": ["runId"]}}
```

---

## 9. `device` — paired devices

Namespace rules (from the tool definitions): call `device.list` first — it is
the source of device ids and reachability. Call `device.describe` before
`device.invoke` to get a command's argument schema. Invoking needs the device
online or wakeable. To use an ungranted command, just invoke it; the device
prompts the user and runs only on approval. `contacts.search` and
`calendar.search` are live reads, never silent substitutes for cached data.
Files the device returns are saved into the workspace under `saved_files`.
A result may include an `embed_token` to include verbatim to render a card.

### `device.list`
List paired devices with live state. Takes no parameters, changes nothing.
Each entry: `device_id`, `display_name`, `is_request_origin`,
`connection_state` (`online`, `wakeable`, `disconnected`, `offline`),
`command_count`, data source names, `platform`, `last_seen_at`. Registered
sessions that expose nothing to invoke or read (e.g. plain web browser logins)
are NOT listed here.
```json
{"properties": {}, "required": []}
```

### `device.describe`
Show everything one paired device can do: runnable commands with per-command
argument schemas, data sources, permission state. Read-only. `device` is the
device id or display name (case-insensitive; ambiguous names error with ids).
Result carries `connection_state`, `commands` (description,
`permission_required`, required/optional argument specs), `data_sources`
(proactive emission, permission granted), `enabled_permissions`, contacts
cache freshness under `stored_data`, and platform metadata.
```json
{"properties": {"device": {"type": "string"}}, "required": ["device"]}
```

### `device.invoke`
Run one command on one paired device. `command` is the command id exactly as
`device.describe` lists it. `params_json` is the command's arguments as a JSON
object (omit for no-arg commands). `health.backfill` is accepted
asynchronously (completion arrives automatically; do not poll). `geofence.set`
accepts one extra daemon-kept field the phone never sees: `payload`
(`{"kind": "act" | "notify", "text": "..."}`); `persistent: true` makes it
standing, `false` one-off; it needs background location
(`location.set_sharing_mode` with `always`, only when the user asks).
```json
{"properties": {"device": {"type": "string"}, "command": {"type": "string"},
  "params_json": {"type": "object"}},
 "required": ["device", "command"]}
```

### `device.unpair`
Remove one device's pairing. The device disconnects, its commands stop, and it
leaves the paired list; only the user can undo this by pairing again from the
device itself. Confirm the user means to remove the pairing before calling.
```json
{"properties": {"device": {"type": "string"}}, "required": ["device"]}
```

---

## 10. `browser` — web search, page fetch, live browser tasks, deep research

Namespace rules (from the tool definitions): `browser.search` finds
information; it does not open a website in the user's live browser or act
there. `browser.open` fetches page text only; it cannot click, sign in, fill
forms, or buy. Live website visits and actions belong to `browser.browse`.
A new window uses the default profile unless a named profile is given; every
window shares the default profile, so one sign-in covers every chat and
scheduled job. A failed/incomplete text fetch does not establish a login
barrier, a live-browser failure, or absence of an option.

### `browser.search`
Search the web from a text query (question, topic, or keywords — never a URL,
pasted link, or bare address). `verticals` accepts at most ONE of: `news`,
`sports`, `weather`, `finance`, `datetime`. General results may be stale and
do not establish current inventory, prices, booking availability, or account
state. The output ends with `Full URLs for search results` when available;
copy those URLs verbatim, never guess from domains.
```json
{"properties": {"primary_query": {"type": "object", "properties": {
    "query": {"type": "string"},
    "language_code": {"type": ["string", "null"]}}, "required": ["query"]},
  "verticals": {"type": "array", "items": {"type": "string",
    "enum": ["news", "sports", "weather", "finance", "datetime"]}}},
 "required": ["primary_query"]}
```

### `browser.open`
Fetch page text to read/summarize/answer. Prefer a returned integer
search-session or page id as `url_id`, with `outlink_idx` to select a result
or real link. A literal URL must be copied verbatim from a prior tool result
or a user-supplied link — never guessed or built from a domain. `line_start`
continues reading a fetched page's text.
```json
{"properties": {"url_id": {"type": ["integer", "string"]},
  "outlink_idx": {"type": ["integer", "null"], "minimum": 0},
  "line_start": {"type": ["integer", "null"], "minimum": 0}},
 "required": ["url_id"]}
```

### `browser.find`
Find exact (case-insensitive) matches of `pattern` in a page already opened
with `browser.open`.
```json
{"properties": {"url_id": {"type": "integer"}, "pattern": {"type": "string"},
  "line_start": {"type": ["integer", "null"], "minimum": 0}},
 "required": ["pattern", "url_id"]}
```

### `browser.lookup_citation_url`
Resolve search-result URLs from a prior `browser.search` call without fetching.
Pass `outlink_indices` (0-based, max 30) or omit for all results. Never use a
URL for a result whose mapping is absent from the search output's full-URL
section. Use returned URLs verbatim.
```json
{"properties": {"url_id": {"type": "integer", "format": "uint64", "minimum": 0},
  "outlink_indices": {"type": "array", "items": {"type": "integer", "format": "uint", "minimum": 0}, "default": []}},
 "required": ["url_id"]}
```

### `browser.windows`
List, open, and close browser windows/tabs and see profiles. A window is one
browser task with its own tabs; its id is the `task_id` shared with
`browser.browse`. `list` also includes scheduled jobs' windows (with owner).
`open` without `task_id` opens a new window (no browser agent starts; send
work with `browser.browse` + `task_id`). `open` with `task_id` opens a new tab
in that window. `close` with `task_id` + `tab` closes the tab; with only
`task_id` it closes the window and stops its browser task. An idle window
closes after about two hours. A named profile is a separate cookie jar.
```json
{"properties": {"action": {"type": "string", "enum": ["list", "open", "close"]},
  "task_id": {"type": "string"}, "tab": {"type": "string"},
  "profile": {"type": "string"}, "url": {"type": "string", "format": "uri"},
  "cursor": {"type": "string", "pattern": "^[A-Za-z][A-Za-z0-9:_-]*$"}},
 "required": ["action"]}
```

### `browser.profiles`
Create or delete a named browser profile (a separate cookie jar for signing
in to a second account on the same site). `create` takes a short `label` and
returns the profile id. `delete` erases the profile's cookies and sign-ins
and is refused while a window still uses it. The default profile cannot be
deleted. Create a profile when a task needs a second account on the same site;
delete one only when the user asks.
```json
{"properties": {"action": {"type": "string", "enum": ["create", "delete"]},
  "label": {"type": "string", "maxLength": 64, "minLength": 1},
  "profile": {"type": "string", "minLength": 1}},
 "required": ["action"]}
```

### `browser.browse`
Give website work to a browser agent, or continue an existing window's work.
`task_id: "new"` starts a new window; an existing window's `task_id` continues
it (send only what changed — a restated assignment can make it repeat work).
The browser cannot read the conversation or memory, so a new task must be a
self-contained assignment: outcome in the user's terms, choices already made,
limits the user set, only the context the work needs. `url` only for an
address the user gave, one from a tool result, or a well-known site whose
address is certain — never build a domain from a business name. `files`
grants workspace files with purposes. Acceptance is not completion; results
arrive as handoffs; do not poll or resend. A new task is not a retry for an
unresolved purchase. For purchases, the checkout shows the user the payment
approval before anything is paid. `account_hint` names the account to sign in
with. `verification_code` carries a one-time-code reference (`credential_id`
UUID + site HTTPS `origin`) from a protected read — never the code itself;
a code the user sent in chat goes in the answer as text. `wallet` selects a
wallet card (`provider`: `stripe-link` | `shop-pay`, plus exact
`payment_method_id`), or `{"action": "keep"}`, or `null` to switch payment
method. The browser signs in when a site needs it: its login agent uses a
saved login or shows the user a secure entry card when none fits.
```json
{"properties": {"task_id": {"type": "string"}, "task": {"type": "string", "minLength": 1},
  "url": {"type": "string", "format": "uri", "pattern": "^https?://", "minLength": 1},
  "profile": {"type": "string", "minLength": 1}, "tab": {"type": "string", "minLength": 1},
  "account_hint": {"type": "string", "minLength": 1},
  "answer_to": {"type": "string", "pattern": "^question_[0-9a-f]{16}$"},
  "files": {"type": "array", "items": {"type": "object", "properties": {
    "file": {"type": "string", "minLength": 1}, "purpose": {"type": "string", "minLength": 1}},
    "required": ["file", "purpose"]}},
  "verification_code": {"type": "object", "properties": {
    "credential_id": {"type": "string", "format": "uuid"},
    "origin": {"type": "string", "pattern": "^https://"}}, "required": ["credential_id", "origin"]},
  "wallet": {"type": ["object", "null"], "properties": {
    "action": {"type": "string", "enum": ["keep"]},
    "provider": {"type": "string", "enum": ["stripe-link", "shop-pay"]},
    "payment_method_id": {"type": "string", "minLength": 1}}}},
 "required": ["task_id", "task"]}
```

### `browser.deep_research`
Send an isolated research agent to the live web in a signed-out browser;
findings return as a handoff with sources, notes, and a report. Only for
explicit user research asks (deep dive, investigation, sourced analysis).
The researcher is isolated: no conversation, memory, files, or accounts;
never signs in; never enters personal data. One call per ask; the mission
must be self-contained. Returns immediately with `agent_id` and a research
folder; findings arrive as a handoff.
```json
{"properties": {"mission": {"type": "string"}, "slug": {"type": "string"}},
 "required": ["mission", "slug"]}
```

---

## Appendix — what was deliberately NOT captured here

- Connector command shapes (Gmail/Calendar/Drive/Spotify/etc.): excluded because
  reading them would have meant touching connected accounts, which the research
  request forbade. Each connector's doc lives at
  `/opt/hatch/connectors/<connector>/CONNECTOR.md` (system, read-only) or
  `~/workspace/custom-connectors/` (custom).
- Artifact, widget, feed, idea, goal, tracking, shopping, social, map, media,
  avatar, and UI namespaces: outside the requested scope; their schemas were
  not loaded or transcribed.
- Approval-card UI, push-notification rendering, and model-side prompt text:
  not exposed as tool schemas; see the architecture notes for what is
  prompt-described vs. inspected.
