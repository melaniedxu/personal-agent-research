# Validation

For reproducible repository checks, run `python3 tools/validate.py`. After an
intentional edit, `--refresh-manifest` updates the repository integrity inventory
once content checks pass. The script additionally verifies the 449 retained Muse
import files against their audit hashes. The recorded results below describe the
research baseline; current repository checks print their results when run.

The coordination reference passed eight tests and its synthetic end-to-end demo.
Tests cover durable duplicate acceptance and digest mismatch, queued priority and
exclusive leases, stale-lease fencing, private parent completion, origin-chat
delivery, worker delivery restrictions, quiet unchanged watches, persistent
one-off schedules, recursive cancellation and conflicting completion rejection.

All JSON files parsed successfully. The normalized Muse manifest contains 193
function definitions from 33 namespaces; required root fields were checked against
their property maps. This is structural validation, not authentication of the
agent's transcription or a complete JSON Schema semantic audit.

The imported export audit verified all 452 hashes listed by its source manifest.
It records the exclusions and the one redaction in exporter commentary. The
runtime export includes 65 connector directories and 197 database table documents.

Authored relative links were checked. Verbatim vendor docs retain VM-absolute
links; a portable database index is provided. A scoped scan found no known user
identifier literals or selected common credential-value formats. Source selection
and the stated scan limits remain part of the privacy boundary.

The temporary debugger ports were checked closed. No live model, connector,
external-channel delivery, security sandbox or production database migration was
tested by the reference. Those components are not implemented in it.

The two public Grok archives passed source-hash and split-integrity checks.
Their 43 and 51 normalized tool schemas parsed and passed root-required-field
checks. The newer archive has 54 skill files; 41 JSON quoting repairs are logged.
The historical Manus source files matched their import hashes and its 29-tool
catalog parsed. These are integrity/structure checks, not authentication of the
public text against either vendor's current inference service. Verbatim public
prompt bodies retain their source links; authored indexes use portable links.

Machine-readable results:

```json
{
  "reference_tests": 8,
  "demo": "passed",
  "json_files_parsed": 60,
  "muse_namespaces": 33,
  "muse_functions": 193,
  "muse_connector_directories": 65,
  "muse_table_documents": 197,
  "public_grok_prompt_archives": {
    "2026-10-24": {
      "tools": 43,
      "variants": 8,
      "runtime_templates": 6,
      "quote_repairs": 41,
      "split_integrity": "passed"
    },
    "2026-08-21": {
      "tools": 51,
      "variants": 10,
      "runtime_templates": 0,
      "quote_repairs": 0,
      "split_integrity": "passed"
    }
  },
  "public_grok_skills": 54,
  "historical_manus_tools": 29,
  "authored_relative_links": "passed",
  "scoped_privacy_scan": "passed; no known user identifier or selected common secret-value format found",
  "temporary_debug_ports": "closed"
}
```
