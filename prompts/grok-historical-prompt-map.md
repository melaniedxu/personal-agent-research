# Historical Grok prompt assembly map

Source: [b-nnett/grok-bot-0.18-reconstructed](https://github.com/b-nnett/grok-bot-0.18-reconstructed),
the archived reconstruction of desktop version 0.18.0. The local installed app
was 0.75.8. This file is an original summary, not a current vendor prompt dump.

The reconstruction's `source/host/runner/system-prompt.ts` builds a base prompt
using feature flags. `system-prompt-assembly.ts` adds runtime sections. The
assembly dependencies explicitly include:

1. agent identity/profile and profile updates;
2. agent, user, and project memory, including compaction-epoch snapshots;
3. automation records and workflow definitions;
4. connected messaging channels and connector manifests;
5. agent/group directory and current execution/computer context;
6. timezone and user identity;
7. feature-specific sections, such as cloud-agent availability and MCP accounts.

The base prompt teaches explicit `SendMessage` delivery, acknowledging user work,
private child results, background work that may finish silently, and approval
checks. Completion revival code constructs a later parent prompt from finished
worker results and carries the originating job's quiet-delivery rule.

Read these pinned-repository paths together; a single base prompt is incomplete:

- `source/host/runner/system-prompt.ts`
- `source/host/runner/system-prompt-assembly.ts`
- `source/host/runner/sand-agent-profile-prompt.ts`
- `source/host/runner/tools/turn-toolset.ts`
- `source/host/runner/tools/send-message-schema.ts`
- `source/host/extensions/transcript/completion-revivals.ts`
- `source/host/extensions/transcript/automation-run-path.ts`

The exact repository commit and reuse status are recorded in `../sources.json`.
The project states that it reconstructs and extends the shipped product; its
module names and changed behavior must not be treated as upstream source truth.
