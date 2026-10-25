"""Run: python3 reference/demo.py. Uses synthetic data and a deterministic model stub."""
import json
from engine import Engine

e = Engine()
e.agent("chief", "research-chat")
print("accept", e.receive("user-1", "chief", "user", {"text": "Check the sample release"}))
run = e.claim("chief")
child = e.spawn("chief", "spawn-1", "Inspect synthetic release notes; no external access")
e.finish(run, "I’m checking the sample release.")
print("spawn", child)
print("worker_done", e.complete_worker(child["worker_id"], {"version": "2.0", "changed": True}))
print("visible_before_parent_wake", len(e.messages("research-chat")))
revival = e.claim("chief")
print("private_wake", revival["kind"], revival["payload"])
e.finish(revival, "The sample release is now version 2.0.")
print("watch_initial", e.observe("release-watch", "chief", "v2", {"version": "2.0"}))
e.finish(e.claim("chief"))  # baseline observed; intentionally no user message
print("watch_unchanged", e.observe("release-watch", "chief", "v2", {"version": "2.0"}))
e.schedule_once("test-once", "chief", 100, "Check the synthetic release")
print("schedule_tick", e.tick(101))
e.finish(e.claim("chief"))  # scheduled check completed quietly
print(json.dumps(e.messages("research-chat"), indent=2))
e.close()
