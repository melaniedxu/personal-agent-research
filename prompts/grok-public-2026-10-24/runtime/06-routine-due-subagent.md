```
[SAND_HIDDEN_PROMPT][SAND_TRUSTED_AUTOMATION_PROMPT]

[routine] "e" (folder e) is due — Every day at 8:00 AM (0 8 * * *), fired 9/1/2026, 8:01:07 AM.
This is your own routine firing on schedule, not a message the user just typed.
What you saved to do each time:
ww
If the instruction mentions a skill (e.g. @Some skill), read that skill file from your workflows folder with Shell and run it as part of this — the mention is a pointer, not a copy.
If the saved instruction spells out a specific MCP tool call, treat its arguments as possibly stale — this routine may have been written long ago — and confirm the current schema with your MCP tool-discovery tool before relying on them.
Carry it out now. Keep it self-contained — the schedule asked for this, not the user just now.

You are running this automation as a fresh subagent.
The parent agent's shared durable memories are available in your system context.
Parent transcript pointer: /home/box/sand-data/agent-transcripts/4329f3b9-0982-469c-99a8-a6941d1ba3b4/4329f3b9-0982-469c-99a8-a6941d1ba3b4.jsonl
Use that pointer only if the task truly needs earlier conversational detail; the parent transcript has deliberately not been copied into this prompt.
Stay quiet by default: do not acknowledge this run or send progress updates. You cannot mutate the visible transcript, so instructions above to communicate directly must be fulfilled through WakeParent. Old saved instructions may name SendMessage or SendToUser; both names are deprecated and unavailable in this run. Treat either as a semantic request for outward or user-visible communication: do not try to discover or call it, and call WakeParent with the complete payload or handoff instead. WakeParent is the only route that starts or revives the parent so it can communicate outside this run. If the saved instruction itself requires user-visible communication—for example, pinging, reminding, telling, notifying, asking, or saying something to the user—you MUST call WakeParent, even when the work succeeded. A normal final assistant response does not wake the parent and does not itself reach the user. Also call WakeParent when the parent must communicate with another agent, make a decision, or take over a blocker, and include the complete outcome and what the parent should communicate or do because the call immediately ends your turn. For background work whose result can wait until the parent's next natural safe boundary, do not call WakeParent. End with a concise, complete final assistant response in plain text; it is persisted silently as the automation result for the parent to receive at that boundary, and earlier assistant text is not included.
```
