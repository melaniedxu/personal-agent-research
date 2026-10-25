# Muse evidence

`runtime-export/` is the fuller native export, imported after the initial
`system_prompt.md` and `tool-schemas.md` downloads. Prefer the fuller export's
schema files. It contains copied runtime documentation and connector manifests,
plus **agent-transcribed** tool definitions and attributed architecture notes.

Local checks verified 452 manifest-listed hashes, all exported JSON files, 33
namespace files and 193 function definitions. The received archive had 453 files
including its manifest. We retained 449 source files, excluding account-specific
inventory and the personal heartbeat file, and added an audit and portable DB
index. See `runtime-export/EXPORT-AUDIT.json` for exact transformations.

The 197 table files describe schema, relationships and restrictions. They contain
no database rows. Their original absolute links refer to the VM; use the portable
`runtime-export/DB-INDEX.md` when browsing this package locally.

`runtime-export/MANIFEST.md` is the exporting agent's commentary. Its claim that
tool parameter shapes are exact is a transcription claim; it is not independently
authenticated by captured inference traffic. Long descriptions with summaries
are flagged. Two named-but-unreturned functions remain missing.

The architecture notes contain an oversimplified statement placing runtime
services outside the VM. The study corrects this using the vendor security
architecture and independent teardown: outside the **runtime cell** does not
necessarily mean outside the VM. Preserve that distinction when interpreting
these source notes.

`client-route-catalog.json` is separately derived from the installed Mac client's
shipped HTML/JS. Route presence does not prove that a route is enabled, callable
by the model, or implemented exactly as its name suggests.

This evidence is not covered by the MIT grant for the package's original code.
The vendor's CLI binaries, auth brokers, inference services and other required
implementation components are not included. Register your own OAuth applications
and implement your own account integrations for a community product.
