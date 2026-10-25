# Additional Grok and Cue prompt research

Second pass, 24 October 2026. The first package missed a substantial public Grok
collection. This update adds it, an older public archive, and historical Manus
material. **Neither Grok archive is authenticated against the installed 0.75.8
inference service. No current Cue system prompt was recovered.**

## What was found

| Material | Clean files | Scope and provenance |
|---|---|---|
| Grok collection updated 2026-10-24 | [Main prompt and variants](prompts/grok-public-2026-10-24/README.md), [43 tool definitions](config/grok-tools.public-2026-10-24.json) | 211,184-byte public transcription; eight variant sections, six runtime-context templates, 54 skill files and two reference files |
| Earlier Grok archive first committed 2026-08-21 | [Main prompt and variants](prompts/grok-public-2026-08-21/README.md), [51 tool definitions](config/grok-tools.public-2026-08-21.json) | 305,973-byte public transcription; ten worker-type sections; pinned to the parent commit before the October replacement |
| Historical Manus archive labelled 2025-07-20 | [Module/loop/environment prompts and 29 tools](evidence/manus-historical-2025-07-20/README.md) | Manus material predating Cue; useful comparison, not Cue/Cascade internals |
| Current local Grok prompt-override lead | [Field-scoped result](evidence/grok/local-prompt-override-check.json) | Installed client declares a string override, but the targeted cache check recovered no value |
| Current Cue documentation request | [Observed reply](evidence/cue/documentation-followup.json) | Agent says installed skills exist but declines their contents/paths; no export received |

The [October source](https://github.com/asgeirtj/system_prompts_leaks/blob/be9efc3ce7f31a79b698d95b4a93fee6178ce88b/xAI/grok-bot/grok-bot.md)
is pinned at `be9efc3ce7f31a79b698d95b4a93fee6178ce88b`, committed
2026-10-24T05:25:04Z. The
[earlier file](https://github.com/asgeirtj/system_prompts_leaks/blob/2c2d038d6ce4b20a101a99c9eea4f3952b24c1bd/xAI/grok-bot.md)
was first committed on August 21 and removed in the October update. These dates
are repository dates, not verified capture dates or product release identifiers.
The repository describes its files as verbatim prompts but supplies no original
request trace or reproducible extraction method for these snapshots.

The exact combined files, per-source SHA-256, repository license text and
provenance manifests are under `evidence/grok/public-prompt-*`. Clean prompt
files strip only their outer numbered heading and boundary whitespace. The
October [skills directory](evidence/grok/public-prompt-2026-10-24/skills/) and
[references directory](evidence/grok/public-prompt-2026-10-24/reference/) preserve
the public files. No downloaded code was executed.

## What the newer Grok prompt says

These are claims in the public text, not newly observed behavior of this account.

**Delivery is a model action with explicit completion.** `SendToUser` is the
only visible output of the main agent; ordinary assistant prose is private.
The source requires an opening text acknowledgement for user-opened work, then
milestone updates, then a final send. A successful `end_turn: true` ends the
turn; the agent must not race that send against unfinished work. Hidden routine
wakes and stale worker results may end silently. `ReactToMessage` can also end
a turn. This directly answers how a DM-like UI can hide internal work.

The schema includes text, standalone attachment, question widget, cloud-agent
card and masked secret-request variants. Fields route text to a connected
`channel`, thread under `reply_to`, or privately DM the owner from a group turn
with `to: "dm"`. Voice memos use another text-send option. A masked request
suspends the agent until submission and describes delivering a secret reference
rather than the value into chat. This is a functional contract, not proof of
the implementation of secret storage or its security.

**Workers have a different completion channel.** `Task` starts a worker with a
self-contained prompt and no inherited conversation. Its final assistant
message becomes the parent's result, and intermediate assistant prose is not
relayed. The parent receives a completion wake and decides what the user needs.
`Task.resume` continues a finished worker; `MessageSubagent` steers one that is
still running; `CheckSubagent` inspects status; `StopSubagent` aborts it. The
new catalog's task types are executor, computerUse, watchVideo and videoReview.
Executor is headless, has no user-delivery tool or browser, and cannot dispatch
more workers according to its description. Most substantial work is delegated
so the main conversation remains responsive.

**Peer agents are distinct from workers.** `SendToAgent` addresses another
persistent agent or group. `priority: true` wakes a direct recipient; false
queues information until its next turn. Group posts arrive immediately.
The source says a priority peer message appears to the user while held messages
do not. This differs from a private Task completion and needs its own transcript
projection and authority rules in a community implementation.

**A shared computer and separate desktops are explicit.** The main prompt says
one persistent Linux box is shared by the user's agents, with shared files,
installed tools and logins; each named agent gets its own desktop/browser
window. Within one agent, only one computerUse worker runs at a time. The parent
has a read-only screenshot tool and delegates input. `Read`, `Shell` and
`AwaitShell` target the box unless passed a registered `machineId`; copy tools
move files across the boundary. These are routing and concurrency contracts.
They do not establish per-worker VM/process provisioning or prove that a model
instruction alone enforces the restrictions.

**Routines combine triggers, saved intent and hidden input.** `UpdateRoutine`
supports create/update/pause/resume/delete and either a schedule or trigger.
Its schema names Slack, GitHub, Origin, Teams, Linear, Sentry, PagerDuty, email,
webhook, cron and group types. The
[routines skill](evidence/grok/public-prompt-2026-10-24/skills/routines.md)
contains the richer event filters absent from the shallow tool schema, along
with finite-watch cleanup, repeated-auth-failure pausing and quiet unchanged
results. The time schedule is described as a local-time five-field cron with
at least five minutes between firings. This is not evidence of the server's
actual deduplication, retry or transaction code.

**MCP tools are discovered separately from execution.** `GetDynamicTools`
retrieves descriptors; `CallDynamicTool` carries namespace, tool name, arguments
and optional MCP details. Plugin discovery/install/auth tools form another
layer. The collection does not enumerate every connected account's live tools,
nor establish a complete role-specific allowlist.

**Memory has a distinct interface.** `RecallMemory` retrieves older facts;
`UpdateMemory` writes or forgets facts with agent/user scope. The example
identity, timezone, teammate and `/tmp/sand-prompt-capture/memory` path in the
published main prompt are source fixture values. They should be replaced during
assembly, not copied as deployment defaults.

## Differences and inconsistencies that matter when building

The [machine-readable comparison](config/grok-tool-diff.public-2026-08-21_to_2026-10-24.json)
records names and root-property/required-field changes. It is a comparison of
two archives, not a vendor release changelog.

| Area | August archive | October archive |
|---|---|---|
| Main visible-delivery name | SendMessage | SendToUser, with explicit end_turn |
| Dynamic tool access | GetMcpTools | GetDynamicTools plus CallDynamicTool |
| General task type | generalPurpose among ten listed variants | executor among four Task enum values |
| User computer routing | Earlier tool surfaces | machineId on Read/Shell/AwaitShell/copy tools, plus ListMachines |
| State management | update_state | Separate routine, memory, profile and skill tools |
| Browser tools in published catalog | Many browser_* schemas and Computer | Not in the 43-entry catalog; browser operation delegated to computerUse |

Do not concatenate every file and expose every tool to every role:

- The October event and routine injection examples still say `SendMessage` and
  `GetMcpTools`, although its main prompt/catalog use the newer names. They also
  contain August example timestamps. Preserve them as evidence, then deliberately
  adapt names for a community implementation.
- Executor/automation variants reference `WakeParent` or `DraftExternalMessage`,
  neither present in the 43-entry catalog. A `userComputerUse` variant appears
  in the text but not the `Task.subagent_type` enum. These can be role-specific
  omissions or material from different runtime states; the source does not
  establish which explanation is correct.
- The October parameter blocks are labelled YAML but written largely as JSON.
  Forty-one lines contain JSON-incompatible quoting. The normalized file escapes
  internal quotation marks or converts a single-quoted regex string; it records
  every before/after line. No properties, required fields, enums or missing
  definitions were invented. All 51 August schemas parse without such repairs.
- Several requirements live only in descriptions: for example, choosing the
  right message payload fields or providing exactly one of schedule/trigger.
  JSON parsing and root-field validation do not enforce these cross-field
  rules. Implement host-side validation and durable delivery acknowledgements.
- Prompt text about approvals and isolation describes expected behavior. It
  does not substitute for capability filtering, approvals bound to exact
  operations, desktop locks or sandbox enforcement.

For implementation, use the original prompts/configuration in this package as
the coherent baseline. Use these recovered sections to add features and tests:
explicit successful-send completion; separate private worker and peer-message
paths; resumable workers; fresh-worker dispatch context; per-agent desktop
locking on a shared account computer; and typed schedule/event inputs. The
Python reference remains a coordination reference and does not implement all
these vendor features.

## Cue: what the second pass establishes

Targeted searches across public prompt collections, the installed Cue client
assets, and a narrower direct documentation question did not yield a verified
current Cue prompt or private tool catalog.

The ordinary Cue chat follow-up requested readable runtime/skill/API docs only,
excluded connected accounts and personal records, and asked for no workers or
schedules. The agent replied that it found installed Skill instruction files
but could not disclose their contents or exact paths, and said it found no
separate exportable references. It created no download. This is an attributed
self-report/refusal, not independent filesystem verification.

The archived **Cue 2023-09-20** entry in EliFuzz's collection is explicitly
Naver's Korean search product in its text. It is not Manus Cue. Similarly,
`xai-org/grok-prompts` documents Grok chat/X prompts, not this Grok Bot desktop
runtime. Product-name collisions are excluded from recovered Cue evidence.

Historical Manus has concrete `message_notify_user`, `message_ask_user` and
`idle` schemas and an event stream containing user messages, actions,
observations, plans, knowledge and data-source documentation. The
[historical files](evidence/manus-historical-2025-07-20/README.md) are included
for comparison, with their archive label and source commit. The file literally
named `prompt.txt` is a general capability essay, so its filename is not evidence
of prompt recovery. A second public repository has identical parsed 29-tool
content; that duplication is not independent authentication.

Official [Manus 2.0 documentation](https://manus.im/blog/introducing-manus-2-0)
connects Cue to Manus infrastructure, but does not establish that those 2025
tools or instructions survive in Cue's Cascade harness. The real client event
JSON in [requests](requests/README.md) remains the stronger current observation.

## What remains unrecovered

There is still no authenticated current Grok/Cue inference request, complete
live prompt stack, role-conditioned tool allowlist, model routing or production
approval implementation. The public Grok collection materially narrows the
functional design gaps. It does not convert a renderer serialization capture
into a server-to-model request. No TLS interception or new credential access
was performed during this follow-up.
