# Configuration and tool interfaces

These files have different purposes. A recovered schema is interface evidence;
it does not implement a tool or supply vendor authentication.

| File | Purpose | Status |
|---|---|---|
| [community-tools.json](community-tools.json) | Five model actions, role filters, Python bindings and required host checks | Original community contract |
| [community-runtime.json](community-runtime.json) | Implemented reference properties and a separately labelled production target | Original implementation/design map |
| [muse-tools.normalized.json](muse-tools.normalized.json) | 193 agent-transcribed functions in 33 namespaces wrapped as input schemas | Research interface; omissions and summaries remain documented |
| [Grok October tools](grok-tools.public-2026-10-24.json) | 43 public definitions, source hash and 41 quoting-repair receipts | Public transcription; exact live role availability unknown |
| [Grok August tools](grok-tools.public-2026-08-21.json) | Earlier public 51-tool catalog | Historical transcription |
| [Grok comparison](grok-tool-diff.public-2026-08-21_to_2026-10-24.json) | Names and root-property/required-field changes | Archive comparison, not a vendor release changelog |

For a community build, start with the two `community-*` files and
[BUILD.md](../BUILD.md). Bind identity, origin, grants and leases in the trusted
host, then translate the selected role's `inputSchema` to your model provider.
Do not expose the whole vendor catalog to every role or treat prose constraints
as enforced validation. Preserve source snapshots when revising normalization.
