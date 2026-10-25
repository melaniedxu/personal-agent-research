# Prompt provenance

`coordinator.md`, `worker.md`, and `background-wake.md` are new, MIT-licensed
community prompts written for this package's model-neutral reference. They are
not claimed to be any vendor's system prompt. Pair them with the role-filtered
tool contract in `../config/community-tools.json` and host-side policy checks.

The actual downloaded Muse startup snapshot is
`../evidence/muse/system_prompt.md`. It is preserved as research evidence, with
separate provenance. It is not a capture of a complete inference request: live
developer messages, memory injections, tools, compaction, and run-specific
context may be added elsewhere. The Muse export describes ordinary final-text
delivery, so do not substitute its prompt for the tool-only delivery contract
of the community reference.

The follow-up found two substantial public Grok collections:

- [October 24 collection](grok-public-2026-10-24/README.md): main prompt, eight
  worker/run/group variants and six runtime injection templates. Its separate
  catalog has 43 tool definitions and its evidence directory has 54 skills.
- [August 21 archive](grok-public-2026-08-21/README.md): main prompt, ten worker
  type sections and a separate 51-tool catalog.

Both are public transcriptions with pinned commits, not authenticated snapshots
of the installed Grok 0.75.8 service. Internal inconsistencies and source fixture
values are documented in [the follow-up](../PROMPT-FOLLOWUP.md). They are research
evidence, excluded from the MIT grant for this package's original community work.

No current Cue prompt was recovered. Its ordinary documentation follow-up also
declined to export installed skill files. The [historical Manus prompts and
29-tool catalog](../evidence/manus-historical-2025-07-20/README.md) predate Cue and
must not be labelled as Cue's current prompt. Historical Grok reconstruction
code is mapped in [grok-historical-prompt-map.md](grok-historical-prompt-map.md).
