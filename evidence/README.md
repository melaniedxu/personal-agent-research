# Evidence index

Source material is kept separate from the study's conclusions and original code.
Each source has a different observation boundary.

| Location | What it contains | Boundary |
|---|---|---|
| [Installed versions](installed-versions.json) | App versions, bundle IDs and artifact hashes | Client artifacts, not cloud releases |
| [Grok](grok/README.md) | Public prompt archives, skills, provenance and static client metadata | Published text and installed-client observations |
| [Muse](muse/README.md) | Direct runtime documents, transcribed schemas, connectors and DB metadata | An authenticated export, not an inference capture |
| [Cue](cue/README.md) | Local addon manifests and an attributed documentation refusal | No current private prompt or model-tool catalog recovered |
| [Historical Manus](manus-historical-2025-07-20/README.md) | Older prompt/module/loop material and 29 tools | Predates Cue; not current Cascade evidence |

Actual sanitized client messages are in [requests/](../requests/README.md).
[CAPTURE.md](../CAPTURE.md) describes collection and exclusions;
[sources.json](../sources.json) pins public references and commits.

Retain source bytes and provenance. Add dated snapshots for new research and
record transformations outside the raw source. Agent commentary remains
self-report; client schemas can be unused; a worker ID does not establish a VM.
Vendor evidence is excluded from the MIT grant for original community work.
