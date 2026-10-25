# Capture method and lab record

Local research date: 24 October 2026, America/Los_Angeles. UTC timestamps in
payloads can therefore show 25 October. The client's timezone, not the execution
host's date, defines the study date.

## Installed artifacts

The version/build/hash inventory is in
[installed-versions.json](evidence/installed-versions.json). Grok Bot and Cue were
inspected as Electron ASAR archives. Muse's installed client exposes a bundled
HTML/JavaScript application, from which a route catalog was extracted. The bundles
were read and copied to scratch space; installed application files were not edited.

Static presence is not availability. Shared generated protocol modules include
types for features outside the personal-agent surface. The Grok descriptor catalog
is deliberately labelled as a shipped protocol inventory, not a callable tool list.

## Serialization observations

The initial observers enabled the Chromium Network domain and filtered synthetic
marker requests. HTTP-only observation did not reveal the relevant messages.
Targeted observers then wrapped transport serialization methods in memory while
forwarding their original arguments unchanged. They did not replay requests,
invoke hidden account APIs or copy credential stores.

The two Electron clients were temporarily launched with debugger access bound
to loopback, using separate ports. The observers were attached only to their own
app contexts. They filtered data containing synthetic `RESEARCH_PROBE_20261024`
markers. Relevant boundaries were:

- Cue `WebSocket.send` and incoming WebSocket events; Socket.IO `42` framing was
  decoded before sanitizing the payload object.
- Grok `MessagePort.postMessage` and incoming MessagePort events in the Electron
  isolated context; these expose renderer/coordinator traffic, not remote LLM API
  bytes.

The research probes requested fixed acknowledgement strings and no account/file/
schedule work. Grok's activity projection nevertheless reported `SetStatus` as
internal activity. The study does not infer a tool definition from that label.

After the captures, both apps were restarted with normal arguments. This removed
the in-memory observer wrappers. The temporary debugger ports were checked closed.
No proxy CA, macOS certificate trust change or disabled TLS validation was used.

## Sanitization

The final JSON files preserve synthetic message content and field structure.
Identifiers, UUIDs, nonces, trace values and replica keys are replaced with
consistent placeholders. Duplicate records caused by overlapping observer
wrappers were removed; they are not counted as duplicate server deliveries.
The Grok trace selects the fourth probe, and the Cue trace selects the request
whose reply was `RESEARCH_PROBE_20261024_CUE_ACK`.

The captured Cue notifications and metadata updates are retained because they
demonstrate separate UI projections. A transient delta and a later permanent
message are different lifecycle events, not evidence of multiple model calls.

## Agent requests and direct exports

Each product received an architecture-export request through its normal chat UI.
It asked for inspectable prompt/tool/runtime documentation, source distinctions,
sanitized examples, and no personal connected-account reads or external effects.
Grok declined the protected prompt/schema request. Cue supplied a public-evidence
report and stated its protected internals were unavailable. Muse supplied files.

A subsequent ordinary Cue request narrowed the scope to readable runtime/skill/API
documentation, excluding personal data and any new workers or schedules. Cue said
it found installed Skill files but declined their contents and paths; it supplied
no download. The [saved reply](evidence/cue/documentation-followup.json) is an
agent self-report, not verified filesystem evidence. Public Grok archives added
in the [follow-up](PROMPT-FOLLOWUP.md) were downloaded from pinned repository
commits, not captured from either live app. A field-scoped local Grok override
cache check returned no prompt value. This follow-up made no new debugger or
certificate changes.

The Muse follow-up explicitly allowed reading connector documentation and schema
metadata while excluding account API calls, user records, credentials and personal
memory/profile files. The archive was downloaded through native Library controls.
The [local export audit](evidence/muse/runtime-export/EXPORT-AUDIT.json) records
hash verification, JSON counts, exclusions and transformations. The exporting
agent's self-report of its actions is attributed, not treated as a network audit.

The ZIP had 453 files including its manifest; 452 manifest-listed source hashes
matched. Account-specific inventory and the personal heartbeat file were excluded.
Known personal identifier literals in exporter commentary were redacted. A scoped
text scan checked known user identifiers and common credential-value formats.
Such a scan cannot recognize every possible sensitive value; it is paired with
the narrow source selection, not presented as a universal privacy guarantee.

## Unintended action

A stale Grok UI control briefly opened a voice chat. It was closed, and the UI
record showed approximately twelve seconds. No research relied on voice. That
action is recorded here so the lab record does not imply that every interaction
was part of the controlled text protocol.

## What this method cannot establish

Client interception cannot ordinarily observe a cloud harness's separate model
request. Muse's startup snapshot does not include all dynamic developer/context/
memory/tool additions. Schema documentation establishes shapes and relationships,
not transaction implementations or running database contents. Shell-accessible
runtime files do not expose privileged services outside their assigned boundary.

The observed files must therefore retain their provenance labels. A separately
labelled synthetic request template is provided for the community implementation;
it must never be described as a captured vendor inference request.
