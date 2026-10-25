```
<timestamp>Friday, Aug 14, 2026, 8:03 AM (UTC)</timestamp>
<user_query>
[SAND_HIDDEN_PROMPT][SAND_TRUSTED_AUTOMATION_PROMPT]

[routine] "e" (folder e) is due — Every day at 8:00 AM (0 8 * * *), fired 8/14/2026, 8:03:46 AM.
This is your own standing order firing on schedule, not a message the user just typed.
What you saved to do each time:
ww
If the instruction mentions a workflow (e.g. @Some workflow), read that workflow file from your workflows folder with Shell and run it as part of this — the mention is a pointer, not a copy.
If the saved instruction spells out a specific MCP tool call, treat its arguments as possibly stale — this standing order may have been written long ago — and confirm the current schema with GetMcpTools before relying on them.
Carry it out now. If there's something worth surfacing, tell the user how it went with SendMessage — casually, the way you'd mention something you remembered to handle, not by announcing a routine. If the saved instruction above says to stay quiet when there's nothing to report and there's nothing new, just end the run with no SendMessage rather than sending filler like "(no change.)"; nobody is waiting on this. If it can't be done, SendMessage to say why. If you're already mid-task with them, don't stop: finish that first, then slip this in as a "btw …" aside. Keep it self-contained — the schedule asked for this, not the user just now.
</user_query>
```
