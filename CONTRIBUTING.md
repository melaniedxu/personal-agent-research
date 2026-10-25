# Contributing

This project maintains research evidence and an original implementation. Keep
them distinguishable so readers can reproduce a finding and understand what
the code actually implements.

## Adding research

1. State the question and the smallest observation that could answer it.
2. Add a dated/versioned directory under the product in `evidence/`. Preserve
   earlier snapshots. Keep raw personal captures outside this repository.
3. Record source URL or method, product/build, timestamps, source commit/hash,
   transformations, exclusions and confidence limits. Distinguish observations,
   static metadata, direct exports, self-report, public transcription and inference.
4. Sanitize identifiers consistently. Remove credentials, account inventories,
   personal memory and unrelated records. A pattern scan supports narrow source
   selection and manual review; it cannot replace them.
5. Preserve source text. Put clean splits in `prompts/`, normalized schemas or
   comparisons in `config/`, and log transformations instead of silently fixing
   or completing a vendor definition.
6. Add sources to `sources.json` and explain the finding in a linked study. Change
   confidence only when the new evidence supports it.
7. Update navigation and `CHANGELOG.md`, then validate.

A prompt filename does not authenticate its origin. A tool mentioned in text
does not establish a role's access. A client message is not an inference request.
Duplicated public dumps do not independently authenticate one another.

## Changing the implementation

- Work from `BUILD.md` and the implemented/proposed distinction in
  `config/community-runtime.json`.
- Bind authority, identity, leases, origin chat and approvals in trusted host code.
- Update original prompts, action contracts and bindings together when behavior
  changes; keep recovered vendor snapshots separate.
- Add meaningful tests for new failure, recovery, permission or delivery semantics.
  Documentation edits normally need link/integrity validation.
- Describe what is implemented and proposed. A subprocess is not a sandbox;
  successful local delivery is not proof of external delivery.

## Validation and review

From the repository root:

```sh
# After intentional edits, validate and refresh the integrity inventory.
python3 tools/validate.py --refresh-manifest

# Verify the candidate snapshot before committing.
python3 tools/validate.py
git diff --stat
git diff --check
```

Review `FILE-HASHES.json` changes with the edited files. Refreshing it does not
rewrite imported provenance or authenticate a source's claims.

Keep a change focused on evidence, normalization or implementation. Use branches
and pull requests for ongoing collaboration, with a concrete problem, resulting
behavior, source/provenance impact and relevant validation. No CI workflow is
installed initially; the portable validation command runs locally.

## Sharing and licenses

Invite intended collaborators through private repository access controls. Do not
commit credentials to make an integration work. The MIT grant covers original
work only; preserve imported attribution, source licenses and provenance.
Changing visibility or redistributing evidence is separate from routine updates.
