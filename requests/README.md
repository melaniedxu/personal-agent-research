# Request and event JSON

`grok-client-observed.json` and `cue-client-observed.json` contain real records
from synthetic probes against the installed desktop apps. Identifiers and trace
values are pseudonymized; duplicated observer records were removed. Their
`capture_method` fields identify the exact boundary observed.

- Grok: renderer/coordinator MessagePort request and received transcript/activity
  events. The answer is represented by a `send-message` transcript entry.
- Cue: Socket.IO `42` event packets over WebSocket, decoded into JSON. The trace
  includes the user submission, streaming delta, permanent message, updates and
  notification projection.

These are not TLS MITM exports and not cloud harness-to-model inference requests.
No current provider request body, full serialized model prompt, or model sampling
configuration was obtained. The initial HTTP-only observer did not show the
relevant data; targeted serialization observation did.

`community-model-request.template.json` is separately marked synthetic. It is
an original provider-neutral model-adapter contract for the included reference.
Its shape must be translated to the model provider you choose.

The example JSON snippets in the main study abbreviate editor content and IDs
for readability. The files here preserve the observed field structure and the
synthetic probe text, subject to their stated redactions.
