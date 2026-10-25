# Repository maintenance

Run from the repository root, using Python 3.9+:

```sh
python3 tools/validate.py
```

The command runs the reference tests and demo, parses JSON, checks normalized
schema roots, verifies source hashes and prompt splits, checks authored links,
scans selected credential formats, and compares repository contents against
`FILE-HASHES.json`. It uses Git's candidate file list when this is a Git checkout;
otherwise it skips standard local/runtime directories. It does not contact
vendors, invoke models, read credentials or change app/debugger settings.

After deliberate changes:

```sh
python3 tools/validate.py --refresh-manifest
python3 tools/validate.py
```

The refresh happens only after content checks pass. Review the inventory diff.
It checks integrity, not the truth of a public prompt or completeness of a schema.
The credential scan is scoped; source selection and manual review are still
required. Original research checks are recorded in [VALIDATION.md](../VALIDATION.md).
