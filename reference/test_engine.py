import os
import tempfile
import unittest
from engine import Engine


class CoordinationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.tmp.name, "state.db")
        self.e = Engine(self.path)
        self.e.agent("chief", "side-chat")

    def tearDown(self):
        self.e.close()
        self.tmp.cleanup()

    def reopen(self):
        self.e.close()
        self.e = Engine(self.path)

    def test_acceptance_survives_restart_and_rejects_nonce_mismatch(self):
        self.e.receive("u1", "chief", "user", {"text": "hello"})
        self.reopen()
        self.assertTrue(self.e.receive("u1", "chief", "user", {"text": "hello"})["duplicate"])
        with self.assertRaises(ValueError):
            self.e.receive("u1", "chief", "user", {"text": "different"})
        self.assertEqual(self.e.messages("side-chat"), [])

    def test_priority_exclusivity_and_expired_lease_fencing(self):
        self.e.receive("bg", "chief", "schedule", {})
        self.e.receive("user", "chief", "user", {})
        first = self.e.claim("chief", now=100, lease_seconds=10)
        self.assertEqual(first["event_id"], "user")
        self.assertIsNone(self.e.claim("chief", now=105))
        recovered = self.e.claim("chief", now=111)
        self.assertNotEqual(first["lease"], recovered["lease"])
        with self.assertRaises(ValueError):
            self.e.finish(first, "late duplicate", now=112)
        self.e.finish(recovered, "one result", now=112)
        self.assertEqual(len(self.e.messages("side-chat")), 1)
        self.assertEqual(self.e.claim("chief", now=113)["event_id"], "bg")

    def test_completion_is_private_and_returns_to_origin_chat(self):
        child = self.e.spawn("chief", "s1", "read sample")
        self.e.complete_worker(child["worker_id"], {"finding": 7})
        self.assertEqual(self.e.messages("side-chat"), [])
        self.assertTrue(self.e.complete_worker(child["worker_id"], {"finding": 7})["duplicate"])
        wake = self.e.claim("chief")
        self.assertEqual(wake["kind"], "child.completed")
        self.e.finish(wake, "Finding: 7")
        self.assertEqual(self.e.messages("side-chat")[0]["content"], "Finding: 7")
        self.assertEqual(self.e.messages("main-chat"), [])
        self.assertIsNone(self.e.claim("chief"))

    def test_worker_cannot_write_to_user_chat(self):
        child = self.e.spawn("chief", "s1", "sample")
        run = self.e.claim(child["worker_id"])
        with self.assertRaises(PermissionError):
            self.e.finish(run, "unauthorized direct worker message")
        self.assertEqual(self.e.messages("side-chat"), [])

    def test_unchanged_watch_is_quiet_after_restart(self):
        self.assertTrue(self.e.observe("w1", "chief", "v1", {"value": 1})["wake"])
        self.e.finish(self.e.claim("chief"))
        self.reopen()
        self.assertFalse(self.e.observe("w1", "chief", "v1", {"value": 1})["wake"])
        self.assertIsNone(self.e.claim("chief"))
        self.assertEqual(self.e.messages("side-chat"), [])
        self.assertTrue(self.e.observe("w1", "chief", "v2", {"value": 2})["wake"])

    def test_one_off_schedule_survives_restart_and_dispatches_once(self):
        self.e.schedule_once("j1", "chief", 100, "check sample")
        self.reopen()
        self.assertEqual(self.e.tick(99), 0)
        self.assertEqual(self.e.tick(101), 1)
        self.assertEqual(self.e.tick(102), 0)
        self.e.finish(self.e.claim("chief"))
        self.assertEqual(self.e.messages("side-chat"), [])

    def test_cancellation_propagates_and_drops_late_completion(self):
        child = self.e.spawn("chief", "s1", "sample")
        grandchild = self.e.spawn(child["worker_id"], "s2", "nested sample")
        self.e.schedule_once("j1", "chief", 100, "sample")
        self.e.cancel("chief")
        for aid in ["chief", child["worker_id"], grandchild["worker_id"]]:
            self.assertIsNone(self.e.claim(aid))
        self.assertFalse(self.e.complete_worker(child["worker_id"], {"late": True})["completed"])
        self.assertEqual(self.e.tick(101), 0)
        self.assertEqual(self.e.messages("side-chat"), [])

    def test_conflicting_spawn_and_completion_are_rejected(self):
        child = self.e.spawn("chief", "s1", "sample")
        self.assertTrue(self.e.spawn("chief", "s1", "sample")["duplicate"])
        with self.assertRaises(ValueError):
            self.e.spawn("chief", "s1", "different")
        self.e.complete_worker(child["worker_id"], {"value": 1})
        with self.assertRaises(ValueError):
            self.e.complete_worker(child["worker_id"], {"value": 2})


if __name__ == "__main__":
    unittest.main(verbosity=2)
