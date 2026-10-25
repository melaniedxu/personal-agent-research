"""Original, model-neutral coordination reference. Python 3.9+, standard library.

This is a coordination engine, not a security sandbox or a vendor clone.
All visible messages are committed explicitly. Worker completions are private wakes.
"""
import hashlib
import json
import sqlite3
import time
import uuid


def encode(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


class Engine:
    def __init__(self, path=":memory:"):
        self.db = sqlite3.connect(path, isolation_level=None)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys=ON")
        self.db.execute("PRAGMA journal_mode=WAL")
        self.db.executescript("""
        CREATE TABLE IF NOT EXISTS agents(
          id TEXT PRIMARY KEY, role TEXT NOT NULL, chat_id TEXT NOT NULL,
          parent_id TEXT REFERENCES agents(id), cancelled INTEGER NOT NULL DEFAULT 0);
        CREATE TABLE IF NOT EXISTS wakes(
          id TEXT PRIMARY KEY, agent_id TEXT NOT NULL REFERENCES agents(id),
          kind TEXT NOT NULL, priority INTEGER NOT NULL, payload TEXT NOT NULL,
          digest TEXT NOT NULL, state TEXT NOT NULL DEFAULT 'queued',
          lease TEXT, lease_until REAL, created REAL NOT NULL);
        CREATE TABLE IF NOT EXISTS messages(
          id TEXT PRIMARY KEY, agent_id TEXT NOT NULL, chat_id TEXT NOT NULL,
          nonce TEXT NOT NULL UNIQUE, content TEXT NOT NULL, created REAL NOT NULL);
        CREATE TABLE IF NOT EXISTS workers(
          id TEXT PRIMARY KEY REFERENCES agents(id), parent_id TEXT NOT NULL,
          spawn_nonce TEXT NOT NULL UNIQUE, input TEXT NOT NULL,
          state TEXT NOT NULL, result TEXT);
        CREATE TABLE IF NOT EXISTS schedules(
          id TEXT PRIMARY KEY, agent_id TEXT NOT NULL, due REAL NOT NULL,
          body TEXT NOT NULL, enabled INTEGER NOT NULL DEFAULT 1);
        CREATE TABLE IF NOT EXISTS watches(
          id TEXT PRIMARY KEY, agent_id TEXT NOT NULL, fingerprint TEXT NOT NULL,
          revision INTEGER NOT NULL);
        """)

    def atomic(self, fn):
        self.db.execute("BEGIN IMMEDIATE")
        try:
            value = fn()
            self.db.execute("COMMIT")
            return value
        except BaseException:
            self.db.execute("ROLLBACK")
            raise

    def agent(self, agent_id, chat_id, role="coordinator", parent_id=None):
        if role not in ("coordinator", "worker"):
            raise ValueError("unknown role")
        self.db.execute("INSERT INTO agents(id,role,chat_id,parent_id) VALUES(?,?,?,?)",
                        (agent_id, role, chat_id, parent_id))

    def _agent(self, agent_id):
        row = self.db.execute("SELECT * FROM agents WHERE id=?", (agent_id,)).fetchone()
        if row is None:
            raise KeyError(agent_id)
        return row

    def _enqueue(self, event_id, agent_id, kind, payload, priority):
        if self._agent(agent_id)["cancelled"]:
            raise ValueError("agent cancelled")
        body = encode(payload)
        digest = hashlib.sha256(encode([agent_id, kind, priority, payload]).encode()).hexdigest()
        old = self.db.execute("SELECT digest FROM wakes WHERE id=?", (event_id,)).fetchone()
        if old:
            if old["digest"] != digest:
                raise ValueError("same event id with different input")
            return {"event_id": event_id, "accepted": True, "duplicate": True}
        self.db.execute("INSERT INTO wakes(id,agent_id,kind,priority,payload,digest,created) VALUES(?,?,?,?,?,?,?)",
                        (event_id, agent_id, kind, priority, body, digest, time.time()))
        return {"event_id": event_id, "accepted": True, "duplicate": False}

    def receive(self, event_id, agent_id, kind, payload):
        # Acceptance means durable enqueue, never completion or user delivery.
        priority = {"user": 0, "child.completed": 1}.get(kind, 2)
        return self.atomic(lambda: self._enqueue(event_id, agent_id, kind, payload, priority))

    def claim(self, agent_id, now=None, lease_seconds=60):
        now = time.time() if now is None else now
        def op():
            if self._agent(agent_id)["cancelled"]:
                return None
            # A coordinator is serial. Expired leases allow recovery; an old lease
            # can no longer commit, even if its old model/tool request finishes late.
            self.db.execute("UPDATE wakes SET state='queued',lease=NULL,lease_until=NULL WHERE agent_id=? AND state='running' AND lease_until<=?",
                            (agent_id, now))
            if self.db.execute("SELECT 1 FROM wakes WHERE agent_id=? AND state='running'", (agent_id,)).fetchone():
                return None
            row = self.db.execute("SELECT * FROM wakes WHERE agent_id=? AND state='queued' ORDER BY priority,created,id LIMIT 1", (agent_id,)).fetchone()
            if row is None:
                return None
            lease = str(uuid.uuid4())
            self.db.execute("UPDATE wakes SET state='running',lease=?,lease_until=? WHERE id=?",
                            (lease, now + lease_seconds, row["id"]))
            return {"event_id": row["id"], "agent_id": agent_id,
                    "kind": row["kind"], "payload": json.loads(row["payload"]),
                    "lease": lease, "lease_until": now + lease_seconds}
        return self.atomic(op)

    def _valid_lease(self, run, now):
        row = self.db.execute("SELECT * FROM wakes WHERE id=?", (run["event_id"],)).fetchone()
        if (row is None or row["agent_id"] != run["agent_id"] or row["state"] != "running"
                or row["lease"] != run["lease"] or row["lease_until"] <= now):
            raise ValueError("stale or expired run lease")
        if self._agent(run["agent_id"])["cancelled"]:
            raise ValueError("agent cancelled")

    def finish(self, run, visible_message=None, now=None):
        now = time.time() if now is None else now
        def op():
            self._valid_lease(run, now)
            agent = self._agent(run["agent_id"])
            if visible_message is not None:
                if agent["role"] != "coordinator":
                    raise PermissionError("workers cannot send directly to the user")
                if not isinstance(visible_message, str) or not visible_message.strip():
                    raise ValueError("visible message must have content")
                self.db.execute("INSERT INTO messages(id,agent_id,chat_id,nonce,content,created) VALUES(?,?,?,?,?,?)",
                                (str(uuid.uuid4()), run["agent_id"], agent["chat_id"],
                                 run["event_id"], visible_message, now))
            self.db.execute("UPDATE wakes SET state='completed',lease=NULL,lease_until=NULL WHERE id=?", (run["event_id"],))
        self.atomic(op)

    def spawn(self, parent_id, nonce, instructions, now=None):
        now = time.time() if now is None else now
        def op():
            parent = self._agent(parent_id)
            if parent["cancelled"]:
                raise ValueError("parent cancelled")
            old = self.db.execute("SELECT * FROM workers WHERE spawn_nonce=?", (nonce,)).fetchone()
            if old:
                if old["input"] != instructions or old["parent_id"] != parent_id:
                    raise ValueError("spawn nonce reused with different input")
                return {"worker_id": old["id"], "accepted": True, "duplicate": True}
            wid = "worker-" + str(uuid.uuid4())
            self.db.execute("INSERT INTO agents(id,role,chat_id,parent_id) VALUES(?,?,?,?)",
                            (wid, "worker", parent["chat_id"], parent_id))
            self.db.execute("INSERT INTO workers(id,parent_id,spawn_nonce,input,state) VALUES(?,?,?,?,?)",
                            (wid, parent_id, nonce, instructions, "running"))
            self._enqueue("start:" + wid, wid, "worker.start", {"instructions": instructions}, 1)
            return {"worker_id": wid, "accepted": True, "duplicate": False}
        return self.atomic(op)

    def complete_worker(self, worker_id, result):
        def op():
            row = self.db.execute("SELECT * FROM workers WHERE id=?", (worker_id,)).fetchone()
            if row is None:
                raise KeyError(worker_id)
            encoded = encode(result)
            if row["state"] == "completed":
                if row["result"] != encoded:
                    raise ValueError("conflicting worker completion")
                return {"completed": True, "duplicate": True}
            if row["state"] == "cancelled" or self._agent(row["parent_id"])["cancelled"]:
                return {"completed": False, "reason": "cancelled"}
            self.db.execute("UPDATE workers SET state='completed',result=? WHERE id=?", (encoded, worker_id))
            self.db.execute("UPDATE wakes SET state='completed',lease=NULL,lease_until=NULL WHERE agent_id=? AND state IN ('running','queued')", (worker_id,))
            self._enqueue("complete:" + worker_id, row["parent_id"], "child.completed",
                          {"worker_id": worker_id, "result": result, "visibility": "private"}, 1)
            return {"completed": True, "duplicate": False}
        return self.atomic(op)

    def cancel(self, agent_id):
        def op():
            self._agent(agent_id)
            rows = self.db.execute("""WITH RECURSIVE children(id) AS (
              SELECT id FROM agents WHERE id=? UNION ALL
              SELECT a.id FROM agents a JOIN children c ON a.parent_id=c.id)
              SELECT id FROM children""", (agent_id,)).fetchall()
            for row in rows:
                aid = row["id"]
                self.db.execute("UPDATE agents SET cancelled=1 WHERE id=?", (aid,))
                self.db.execute("UPDATE wakes SET state='cancelled',lease=NULL,lease_until=NULL WHERE agent_id=? AND state IN ('queued','running')", (aid,))
                self.db.execute("UPDATE workers SET state='cancelled' WHERE id=? AND state!='completed'", (aid,))
                self.db.execute("UPDATE schedules SET enabled=0 WHERE agent_id=?", (aid,))
        self.atomic(op)

    def schedule_once(self, schedule_id, agent_id, due, body):
        self._agent(agent_id)
        self.db.execute("""INSERT INTO schedules(id,agent_id,due,body,enabled) VALUES(?,?,?,?,1)
          ON CONFLICT(id) DO UPDATE SET agent_id=excluded.agent_id,due=excluded.due,body=excluded.body,enabled=1""",
                        (schedule_id, agent_id, due, body))

    def tick(self, now=None):
        now = time.time() if now is None else now
        def op():
            rows = self.db.execute("SELECT * FROM schedules WHERE enabled=1 AND due<=?", (now,)).fetchall()
            for row in rows:
                self._enqueue("schedule:" + row["id"] + ":" + str(row["due"]), row["agent_id"],
                              "schedule", {"schedule_id": row["id"], "instruction": row["body"]}, 2)
                self.db.execute("UPDATE schedules SET enabled=0 WHERE id=?", (row["id"],))
            return len(rows)
        return self.atomic(op)

    def observe(self, watch_id, agent_id, fingerprint, payload):
        # Deterministic cheap gate: no model call on an unchanged observation.
        def op():
            row = self.db.execute("SELECT * FROM watches WHERE id=?", (watch_id,)).fetchone()
            if row and row["agent_id"] != agent_id:
                raise ValueError("watch belongs to another agent")
            if row and row["fingerprint"] == fingerprint:
                return {"wake": False}
            revision = row["revision"] + 1 if row else 1
            self.db.execute("""INSERT INTO watches VALUES(?,?,?,?) ON CONFLICT(id)
              DO UPDATE SET fingerprint=excluded.fingerprint,revision=excluded.revision""",
                            (watch_id, agent_id, fingerprint, revision))
            self._enqueue("watch:" + watch_id + ":" + str(revision), agent_id, "watch.changed", payload, 2)
            return {"wake": True, "revision": revision}
        return self.atomic(op)

    def messages(self, chat_id):
        return [dict(r) for r in self.db.execute("SELECT * FROM messages WHERE chat_id=? ORDER BY created,id", (chat_id,))]

    def close(self):
        self.db.close()
