# MANIFEST — personal-agent architecture research export

This manifest is the researcher's commentary. It is NOT source material.
Everything under `prompt/`, `notes/`, `docs/`, `muse-db/`, `connectors/`, and
`inventory/` is a verbatim copy of the inspected source listed beside it, except
where a file's own header or a `transcription_note` field says otherwise.
Everything under `schemas/` is a transcription of in-session tool definitions into
valid JSON: function names, parameter names, types, enums, patterns, defaults, and
required fields are exact; long prose descriptions are in some cases summarized, and
each such file says so in its own `transcription_note`. Nothing in `schemas/` is a
captured wire payload.

## Labeling used throughout this export

- **[Inspected]** — read directly from a file, doc, or tool definition in this session.
- **[Prompt-described]** — vendor self-report: the session prompt or a namespace
  description asserting how a subsystem behaves. Not independently measured.
- **[Inference]** — the researcher's reconstruction or best guess. Labeled as such
  wherever it appears, and never presented as an observed fact.

## What was NOT done (per the requester's constraints)

- No connected account API was invoked; no memory or profile data was read.
- No database user records were queried; muse-db material is schema/docs text only.
- No permission was changed, no external message was sent, no real schedule was created.
- No credential, account ID, or secret value is included; a secret-pattern scan over
  the staged tree (private-key headers, sk-*, AKIA*, xox*, ghp_*, gho_*) found no hits.
- The prompt snapshot was scanned for personal identifiers (<USER_IDENTIFIER>, <USER_IDENTIFIER>, <USER_IDENTIFIER>,
  <USER_IDENTIFIER>, <USER_IDENTIFIER>, case-insensitive) with 0 matches before copying.

## File inventory: export path, inspected source path, SHA-256

| Export path | Inspected source | SHA-256 |
|---|---|---|
| `all-tools.json` | `Generated from schemas/*.json in this export` | `5440a0b3c51f588996735c52096938af2cfaaa1432f2b5e0438a07a3c0f1ab5b` |
| `connectors/apple_healthkit/CONNECTOR.md` | `/opt/hatch/connectors/apple_healthkit/CONNECTOR.md` | `f214e0fbb26fa5b7b110af84588cf76f7757cea35868f3fd1e16f57f5526cb52` |
| `connectors/apple_healthkit/connector.yaml` | `/opt/hatch/connectors/apple_healthkit/connector.yaml` | `6b6f6eb7ee803ac0e855f79474bebdc90fe529e7fc98ccd5a2a29777713ed84e` |
| `connectors/apple_healthkit/manifest.yaml` | `/opt/hatch/connectors/apple_healthkit/manifest.yaml` | `1751fc300a041d2d2fc974baa8480bc2dd109b8693eec758738c7ba61cc7a8f0` |
| `connectors/asana/CONNECTOR.md` | `/opt/hatch/connectors/asana/CONNECTOR.md` | `9092cf560dabc08c3a20104a3badf8029c1a0b4735c3f7ae86347402ac957c8f` |
| `connectors/asana/connector.yaml` | `/opt/hatch/connectors/asana/connector.yaml` | `2191da1209320ca06a5f2a4d2b8ee228c924ede6a50bb0af88e5f519c8f8ec74` |
| `connectors/asana/manifest.yaml` | `/opt/hatch/connectors/asana/manifest.yaml` | `bc3d067cc01cc9a8e68cca522f38d14577a5db16713f150915838dd73fa60236` |
| `connectors/box/CONNECTOR.md` | `/opt/hatch/connectors/box/CONNECTOR.md` | `bf3788acb521c6437bd5683189308d0797a85aff5084e4f1d17afe8053633188` |
| `connectors/box/connector.yaml` | `/opt/hatch/connectors/box/connector.yaml` | `24f0df255309c26b98773fe08492a2325ac13e01a5f2a379b37e15623684b4b7` |
| `connectors/box/manifest.yaml` | `/opt/hatch/connectors/box/manifest.yaml` | `f57584cd7ba3403f911a93a65da85fb067201521a16484003e18c9a4d9386888` |
| `connectors/calendly/CONNECTOR.md` | `/opt/hatch/connectors/calendly/CONNECTOR.md` | `04f3cb511a735b565e5efc44c9a9b8411990fa8bbbe1944c6f902002cb4abfc0` |
| `connectors/calendly/connector.yaml` | `/opt/hatch/connectors/calendly/connector.yaml` | `1c7dd9f8ab46141bc0092ba9d00731578fb6b4ba2a0e888a8535531416906b51` |
| `connectors/calendly/manifest.yaml` | `/opt/hatch/connectors/calendly/manifest.yaml` | `f08f283ec932cb6712b41e8633c3bf757d4d848d9eab7655df3366ddd166656e` |
| `connectors/canva/CONNECTOR.md` | `/opt/hatch/connectors/canva/CONNECTOR.md` | `788f9b9fc997e13948ee415b1bf1c0cbda4898544cadb4ccb90c4a7e7175d417` |
| `connectors/canva/connector.yaml` | `/opt/hatch/connectors/canva/connector.yaml` | `6a3dc8a7104888f20f17ec71aa96102291304423b0ea9f42e88c4a82c9312057` |
| `connectors/canva/manifest.yaml` | `/opt/hatch/connectors/canva/manifest.yaml` | `11efc79bbd27b6d2c4f879b8198f0e13a9a6ab08d729f85e22ee941656bd3b68` |
| `connectors/dropbox/CONNECTOR.md` | `/opt/hatch/connectors/dropbox/CONNECTOR.md` | `40bf6b3c86e370393249052c03914e964988e31dc0e2d062826db4826fc48101` |
| `connectors/dropbox/connector.yaml` | `/opt/hatch/connectors/dropbox/connector.yaml` | `32f2103797d14e79833061026f78f19d57140437218550bf3d2664ec9106c6e2` |
| `connectors/dropbox/manifest.yaml` | `/opt/hatch/connectors/dropbox/manifest.yaml` | `90e7dc3c5a2ba83c554b1c20946787318d24fd8012e204681227fab21cc82107` |
| `connectors/duffel/CONNECTOR.md` | `/opt/hatch/connectors/duffel/CONNECTOR.md` | `60ce309c709dbc6d8904cc7128e0af4f8721273b5e9ec683b43dbbdb432e6e05` |
| `connectors/duffel/connector.yaml` | `/opt/hatch/connectors/duffel/connector.yaml` | `789fb99200379a69b8cdd2ef465bab1351782642566c29cc03fc9fa051734685` |
| `connectors/duffel/manifest.yaml` | `/opt/hatch/connectors/duffel/manifest.yaml` | `811c16091914cd37cd21d229793356c3c507c85b86cb1f98b41f1e5a4b97d6f6` |
| `connectors/evernote/CONNECTOR.md` | `/opt/hatch/connectors/evernote/CONNECTOR.md` | `8e2ea1fa5a836def05c701ac9cb0f03b05870cb9f8d82fdfabe77bf6e7f51fe8` |
| `connectors/evernote/connector.yaml` | `/opt/hatch/connectors/evernote/connector.yaml` | `726b0689374f46e9d99b4a0b8c3e4ab1b92dafe8364199b10503670ca705fa40` |
| `connectors/evernote/manifest.yaml` | `/opt/hatch/connectors/evernote/manifest.yaml` | `bfb057394c4ff788fb93b0621b68014ba4d5c70c78302a8aafd6a61371cd1e89` |
| `connectors/facebook_cli/CONNECTOR.md` | `/opt/hatch/connectors/facebook_cli/CONNECTOR.md` | `9d31afbb530aabc43464c3a141cbbb8de19f6a204d519ee1dca8c2523fda73ed` |
| `connectors/facebook_cli/connector.yaml` | `/opt/hatch/connectors/facebook_cli/connector.yaml` | `48c9ec2c6cb25b4ffc3de2eda4c4e4fe9c45fd82c5c46233c1d36a42335a9f95` |
| `connectors/facebook_cli/manifest.yaml` | `/opt/hatch/connectors/facebook_cli/manifest.yaml` | `dd888a51870bcc62989dec3bc36158d68f1defcda439bedaaca6ace2e449b0bb` |
| `connectors/figma/CONNECTOR.md` | `/opt/hatch/connectors/figma/CONNECTOR.md` | `1fef4e35c9fbe7932ee6abad5e18d61dd9d6aa3d8193db8effbf790c8bd2ec66` |
| `connectors/figma/connector.yaml` | `/opt/hatch/connectors/figma/connector.yaml` | `43c0cd353b0804f0262ba073022ab1479f4a956441e0d799c48847182110fe21` |
| `connectors/figma/manifest.yaml` | `/opt/hatch/connectors/figma/manifest.yaml` | `0fdbb3227e1b6d58263b1ebdccf41475339498a8beac9c9ff48146a683cc5f94` |
| `connectors/flightaware/CONNECTOR.md` | `/opt/hatch/connectors/flightaware/CONNECTOR.md` | `4e0c73ac0631a9dda3bf5cd883ff180f7da0debd786f5ac2e256fcd3cfdaab71` |
| `connectors/flightaware/connector.yaml` | `/opt/hatch/connectors/flightaware/connector.yaml` | `47ca9e8ccfaeff1f1291f0879dba8535a7d9c9305611807e8507ced538594168` |
| `connectors/flightaware/manifest.yaml` | `/opt/hatch/connectors/flightaware/manifest.yaml` | `93d3ced5232aa1edc52c59ac001e98b2fd492f90f4fd72766690f7caedc81277` |
| `connectors/function_health/CONNECTOR.md` | `/opt/hatch/connectors/function_health/CONNECTOR.md` | `6d282401ae28e97b374ca697ecc71aefad1057ca43c0d58743b2211a9d588427` |
| `connectors/function_health/connector.yaml` | `/opt/hatch/connectors/function_health/connector.yaml` | `11d7305ca9c95fca68f005e52d20a2e57fcaecb7a7ac88ee74a24f8f98b437d9` |
| `connectors/function_health/manifest.yaml` | `/opt/hatch/connectors/function_health/manifest.yaml` | `d10ec57f30c14c8378b0999ad1ce4d56423ee0a5802e086a2bd5c0f5dad5d219` |
| `connectors/ghl/CONNECTOR.md` | `/opt/hatch/connectors/ghl/CONNECTOR.md` | `5ef948a6b1ed0148fcbcd99044e0c4c8cfdae2b80a44ce6e9f6e5131151ff83b` |
| `connectors/ghl/connector.yaml` | `/opt/hatch/connectors/ghl/connector.yaml` | `0703cb7347ecab98f71cf7cce32f4444ecb6bd560b59fb9f3d2b3bfad7a130e5` |
| `connectors/ghl/manifest.yaml` | `/opt/hatch/connectors/ghl/manifest.yaml` | `adcfa079783382d76f3f162f3fecb93b4ae5e5b7cdcf0e59eb827ab9ff5a35c2` |
| `connectors/github/CONNECTOR.md` | `/opt/hatch/connectors/github/CONNECTOR.md` | `84fab490b60bb24b0a2557789d7e7f9b9275d724675163cc21b82c84fcd62f83` |
| `connectors/github/connector.yaml` | `/opt/hatch/connectors/github/connector.yaml` | `f586e454faf4347628b3f875c4279268b43b62e75bb7b3ee997052c3706e97e5` |
| `connectors/github/manifest.yaml` | `/opt/hatch/connectors/github/manifest.yaml` | `a695503baa16635bedd9adf900769b35d0adff96edc7d7da24a6281e577b1b0e` |
| `connectors/gmail/CONNECTOR.md` | `/opt/hatch/connectors/gmail/CONNECTOR.md` | `997e3611e9fd9a8169f787761289d4100e78370b6b77d86ece892f806a8e232c` |
| `connectors/gmail/connector.yaml` | `/opt/hatch/connectors/gmail/connector.yaml` | `efa8cedcaa5ee65d6ca86ce6ad022e83481972b3e80ac54936798df200a85048` |
| `connectors/gmail/manifest.yaml` | `/opt/hatch/connectors/gmail/manifest.yaml` | `961ce43669f5d95cb6d72ebc29175c972d88de99abc1be92fdc02ab1c95a1627` |
| `connectors/google_calendar/CONNECTOR.md` | `/opt/hatch/connectors/google_calendar/CONNECTOR.md` | `6a7b41ec0f191559278208dea83e6305458666f791f22c7ba4934472e812bd90` |
| `connectors/google_calendar/connector.yaml` | `/opt/hatch/connectors/google_calendar/connector.yaml` | `20383ff03d424401dda97b7e975a036657aec777483a2b05a2a7223dce5f9898` |
| `connectors/google_calendar/manifest.yaml` | `/opt/hatch/connectors/google_calendar/manifest.yaml` | `7d6259e64dbd6fa0792d866d774e07b6931efe235427450bece86f3c6c4b1c97` |
| `connectors/google_contacts/CONNECTOR.md` | `/opt/hatch/connectors/google_contacts/CONNECTOR.md` | `5b3577bc99dc093534fdce74bcf21c8b614738793c51b02dfb300f978b50d290` |
| `connectors/google_contacts/connector.yaml` | `/opt/hatch/connectors/google_contacts/connector.yaml` | `370a41e5e991bf18dd8ea0154184c228aa52a8aa163edac09ac93e3acb32d360` |
| `connectors/google_contacts/manifest.yaml` | `/opt/hatch/connectors/google_contacts/manifest.yaml` | `1611f95202a910fa4c3ff74bba3811eaa252af1a9448807612d2823c3cc2c1aa` |
| `connectors/google_docs/CONNECTOR.md` | `/opt/hatch/connectors/google_docs/CONNECTOR.md` | `9f47487c0912403278de511bfc22e04724d372c5acfbf7b6b3d60ad1222faadd` |
| `connectors/google_docs/connector.yaml` | `/opt/hatch/connectors/google_docs/connector.yaml` | `6647dd87b4136e1ef756b5c88c0eadb5b1a628d94f28edf210f8243214443e78` |
| `connectors/google_docs/manifest.yaml` | `/opt/hatch/connectors/google_docs/manifest.yaml` | `b47bd43ff51babfa031bee4e4571e4d2545594e86dba61c980f9091dd82c84db` |
| `connectors/google_drive/CONNECTOR.md` | `/opt/hatch/connectors/google_drive/CONNECTOR.md` | `d39badabb1324c19a91542799dc3b8b4847fcc2cccd34a71c46b115eaf0414da` |
| `connectors/google_drive/connector.yaml` | `/opt/hatch/connectors/google_drive/connector.yaml` | `191d63a40be3ad1cfc20f803c9e80a19516aa9511d816a8532a95b78fc4d441b` |
| `connectors/google_drive/manifest.yaml` | `/opt/hatch/connectors/google_drive/manifest.yaml` | `0062b3c1c6beb39044be595c1193f44bea5191f6e303e7b557c7f477ba9e0326` |
| `connectors/google_forms/CONNECTOR.md` | `/opt/hatch/connectors/google_forms/CONNECTOR.md` | `2c69ba0afaa59bab8ae975f2638a547a54b06f7437fbfa9842c3b4a7d0566e3a` |
| `connectors/google_forms/connector.yaml` | `/opt/hatch/connectors/google_forms/connector.yaml` | `90cd52d3311af1fc331be93a7f323cd375b247c9279c352092d0129a42afad4b` |
| `connectors/google_forms/manifest.yaml` | `/opt/hatch/connectors/google_forms/manifest.yaml` | `55195ef22f5a956b56ef7bc2c3023408af78b2e3d70e709d84b5e9c1907e0265` |
| `connectors/google_health_connect/CONNECTOR.md` | `/opt/hatch/connectors/google_health_connect/CONNECTOR.md` | `43d852677f147f1c65fe110fcb30733b16e5954681d6ab71f3c089d58fd8a522` |
| `connectors/google_health_connect/connector.yaml` | `/opt/hatch/connectors/google_health_connect/connector.yaml` | `282e935bc5051ecd985247f912e8956ef90c714e7355ef81855add08dd18cc54` |
| `connectors/google_health_connect/manifest.yaml` | `/opt/hatch/connectors/google_health_connect/manifest.yaml` | `e02cea73aa0fb4f495338b6c82feec7a1f0da4cba20658292aad265a6bce6eb6` |
| `connectors/google_sheets/CONNECTOR.md` | `/opt/hatch/connectors/google_sheets/CONNECTOR.md` | `649fe934391171385d4949880baa1160e4abefafb9d742e4902d5b3373789028` |
| `connectors/google_sheets/connector.yaml` | `/opt/hatch/connectors/google_sheets/connector.yaml` | `1b1df97371c44569fd95a6b5e13b635f3b3b0b2bf9bc97860c03935a90e2b1af` |
| `connectors/google_sheets/manifest.yaml` | `/opt/hatch/connectors/google_sheets/manifest.yaml` | `131f7d87ce5713ce478278429bd6bec469309e03fef2df46619a72815706f306` |
| `connectors/google_slides/CONNECTOR.md` | `/opt/hatch/connectors/google_slides/CONNECTOR.md` | `753d136aacbbe4a3e5b037c6428601f8c0534d0167c073c593c841b1318d5e44` |
| `connectors/google_slides/connector.yaml` | `/opt/hatch/connectors/google_slides/connector.yaml` | `943519ae612236bd9f8e8bb19a6d46f2369fb5fd027157ca92964aa888f9de2f` |
| `connectors/google_slides/manifest.yaml` | `/opt/hatch/connectors/google_slides/manifest.yaml` | `51f8be12a8535f43e698e61a1900cd02291aad3ea05863749cf1ce30710ac646` |
| `connectors/google_tasks/CONNECTOR.md` | `/opt/hatch/connectors/google_tasks/CONNECTOR.md` | `8a5d75cf2298cd6b5227cc515587330b3b741621d2b0a87b5959bb13c182f632` |
| `connectors/google_tasks/connector.yaml` | `/opt/hatch/connectors/google_tasks/connector.yaml` | `3562042076ccbeb4095b9960cd8f56f9389676a9cb2948e1184e6caec7aa2679` |
| `connectors/google_tasks/manifest.yaml` | `/opt/hatch/connectors/google_tasks/manifest.yaml` | `f50a99a319f44f8f0d54f442a43315f4f5ccf23f26e741d699e19d780d5e4d52` |
| `connectors/granola/CONNECTOR.md` | `/opt/hatch/connectors/granola/CONNECTOR.md` | `5a14f67e5139ce0752069a37d4f7868afcad692fe576ec6231b69c640174896f` |
| `connectors/granola/connector.yaml` | `/opt/hatch/connectors/granola/connector.yaml` | `7aab6c8a53766ff011e29257c7685ea4584662b89e18fdf348ad12c8e213be0c` |
| `connectors/granola/manifest.yaml` | `/opt/hatch/connectors/granola/manifest.yaml` | `d1d7dd62381203fd058338735037179da095903b57b8eec960d5edf5f666ff55` |
| `connectors/healthex/CONNECTOR.md` | `/opt/hatch/connectors/healthex/CONNECTOR.md` | `b91004077404c8d427afaef74146f8dc5baa0b0df6454785b63015b594698564` |
| `connectors/healthex/connector.yaml` | `/opt/hatch/connectors/healthex/connector.yaml` | `705ec7cc699c96cf0375bb088470bdb3239e4d76919557999cf10ff3b4c737a7` |
| `connectors/healthex/manifest.yaml` | `/opt/hatch/connectors/healthex/manifest.yaml` | `a2a3c0b0f260094568c4ae7ea7a5204ee61023e778b1e4dae5f56e5e083b78d1` |
| `connectors/instagram/CONNECTOR.md` | `/opt/hatch/connectors/instagram/CONNECTOR.md` | `a5a0afca1186817a2ad0ddbbcce0bd3a90334b6049998c5ed7efef2a303b1579` |
| `connectors/instagram/connector.yaml` | `/opt/hatch/connectors/instagram/connector.yaml` | `31b7fd285386a18656ed3123e3abcf016ff89ed721289cbb5b559c94241c44a8` |
| `connectors/instagram/manifest.yaml` | `/opt/hatch/connectors/instagram/manifest.yaml` | `3f340655d0b7a2592cf7a60ff54142c10200fd8eef7cb90b73fb524ec9aa960f` |
| `connectors/instagram_messages/CONNECTOR.md` | `/opt/hatch/connectors/instagram_messages/CONNECTOR.md` | `2dc7321efc6c37a93500f99da100ad7ba8f393ce606ed45aa2f2962ed9107ce0` |
| `connectors/instagram_messages/connector.yaml` | `/opt/hatch/connectors/instagram_messages/connector.yaml` | `0be624a67c35071121664659a34cd054ee4cd534d275f3189051d9b5b4a379e5` |
| `connectors/instagram_messages/manifest.yaml` | `/opt/hatch/connectors/instagram_messages/manifest.yaml` | `cfa537214394ed58a90a88ce3ef0408c82821d42ec01bec5178dad166bb36fa4` |
| `connectors/klaviyo/CONNECTOR.md` | `/opt/hatch/connectors/klaviyo/CONNECTOR.md` | `633e7ee37213a64b611e59e553f615e6c91e4f28106344c7e7b6e5e400648ad3` |
| `connectors/klaviyo/connector.yaml` | `/opt/hatch/connectors/klaviyo/connector.yaml` | `9df681b00293e9264d5e1d77c6e5ed53f49a710cdeb60dc210d0d4dc11e37eb8` |
| `connectors/klaviyo/manifest.yaml` | `/opt/hatch/connectors/klaviyo/manifest.yaml` | `bbe06353a2149d0ec50269154f636daa42e3e7905ddebc076b18c80cef42015d` |
| `connectors/linear/CONNECTOR.md` | `/opt/hatch/connectors/linear/CONNECTOR.md` | `2dd316cafb1fd540f9fe6b19cd1866a11cd4bb590a339e8278ee5274653f25fd` |
| `connectors/linear/connector.yaml` | `/opt/hatch/connectors/linear/connector.yaml` | `72c6b85915b2fc6452dff1e2c8b2d3aabcfb0101983fadf7e60db8a2d3756d8d` |
| `connectors/linear/manifest.yaml` | `/opt/hatch/connectors/linear/manifest.yaml` | `620dab63c920fa4548b1336e676b465e676fdc2747b9a0be3fdbf8d046aecf2c` |
| `connectors/lovable/CONNECTOR.md` | `/opt/hatch/connectors/lovable/CONNECTOR.md` | `c467446b655ae75b895c6c4b509b6bdc8a886843bee2388943cd06970dc5108d` |
| `connectors/lovable/connector.yaml` | `/opt/hatch/connectors/lovable/connector.yaml` | `a9c79939207710b8f231aeb2e8c77b07eeb0f51f53ec34c97bc308199271e96e` |
| `connectors/lovable/manifest.yaml` | `/opt/hatch/connectors/lovable/manifest.yaml` | `c959dcb6038a13a7b47a7d75a77ab819aace5bbe2a584074102eca274abc5ae0` |
| `connectors/messenger_read/CONNECTOR.md` | `/opt/hatch/connectors/messenger_read/CONNECTOR.md` | `dc7bce529690a025a2311fcdafda514d678ecbf1be0a3522e525c91bbb8d13a6` |
| `connectors/messenger_read/connector.yaml` | `/opt/hatch/connectors/messenger_read/connector.yaml` | `a502c2d481a58c18237cfc85800d558c004dea9eb067bfccd5e98e21a12e4dc0` |
| `connectors/messenger_read/manifest.yaml` | `/opt/hatch/connectors/messenger_read/manifest.yaml` | `bde4cddeb6de200599a7d03010dc23e8060c915a2fcab71c00946c04a831b8bd` |
| `connectors/meta_ads/CONNECTOR.md` | `/opt/hatch/connectors/meta_ads/CONNECTOR.md` | `6077006674d191956d22635e26cbc0f76acdec985e6fe330c33498eda94e677a` |
| `connectors/meta_ads/connector.yaml` | `/opt/hatch/connectors/meta_ads/connector.yaml` | `d0582c031c6cfc4fd7b21f63e7841494849eeee2005d09d0a7c7d40ae9d324d6` |
| `connectors/meta_ads/manifest.yaml` | `/opt/hatch/connectors/meta_ads/manifest.yaml` | `bc024dd749e62abfc8829a9f2e04a773ad34bdc3bcd02c00b63277569deaa59d` |
| `connectors/meta_catalog_search/CONNECTOR.md` | `/opt/hatch/connectors/meta_catalog_search/CONNECTOR.md` | `b4b5a3adb86fe2ef473f4afa88dfe7baa2b96d448d0f8da9123e327242655890` |
| `connectors/meta_catalog_search/connector.yaml` | `/opt/hatch/connectors/meta_catalog_search/connector.yaml` | `84ea3722a52a7a5b68b26597cd90f0eceb46a42eaf2cb4a34ecedb136248a45a` |
| `connectors/meta_catalog_search/manifest.yaml` | `/opt/hatch/connectors/meta_catalog_search/manifest.yaml` | `2db30f95d8c7a6150ef2ff8ddd143dafa98a9e756693523cd4b829e588d2af40` |
| `connectors/moneyforward_me/CONNECTOR.md` | `/opt/hatch/connectors/moneyforward_me/CONNECTOR.md` | `d155d1b4d933f3c7483a330105393bfc8e029900fe2d8b30ca902f8669e481b8` |
| `connectors/moneyforward_me/connector.yaml` | `/opt/hatch/connectors/moneyforward_me/connector.yaml` | `2482e9eec5c0e89780479d82b1bf29b67ded792e71df723a2d23b3874f7a194d` |
| `connectors/moneyforward_me/manifest.yaml` | `/opt/hatch/connectors/moneyforward_me/manifest.yaml` | `3da4247b5738dd706d758af888b6b6dc9e705176ddac3a1b35533253ba16cff3` |
| `connectors/notion/CONNECTOR.md` | `/opt/hatch/connectors/notion/CONNECTOR.md` | `e6260435e0d7852d1012ecfb0625bcd63c62d4cb2ec185f2a202554540910dab` |
| `connectors/notion/connector.yaml` | `/opt/hatch/connectors/notion/connector.yaml` | `d1265a28b3e172c8cff7f4d3456920034773263e35e8d937796174db242505a7` |
| `connectors/notion/manifest.yaml` | `/opt/hatch/connectors/notion/manifest.yaml` | `0f12281df4f304dccdf2687ce777fbce3a72d3ef5fdc124ca145c9cbea213946` |
| `connectors/onepassword/CONNECTOR.md` | `/opt/hatch/connectors/onepassword/CONNECTOR.md` | `a4eed66553f1b1210abcc562543772afd69f2395ab018f1295d876ff5b56f64a` |
| `connectors/onepassword/connector.yaml` | `/opt/hatch/connectors/onepassword/connector.yaml` | `4420f9b5f7c2348e7b9f4b3dde30b778a602dbd3eede46e6aea56d8473a8f636` |
| `connectors/onepassword/manifest.yaml` | `/opt/hatch/connectors/onepassword/manifest.yaml` | `5d27c6a46066615cef9b24662122256e0e96cdfb52ef0b62ebb6738ff8e9d9e9` |
| `connectors/opentable/CONNECTOR.md` | `/opt/hatch/connectors/opentable/CONNECTOR.md` | `81cefe8e3d5a3719643f6b0a494c2b5187ec6bf6d4e443bef9b15bb2f68ac44e` |
| `connectors/opentable/connector.yaml` | `/opt/hatch/connectors/opentable/connector.yaml` | `91ee0c039de8f9c32de204be8c2ad4485925d0e9e11e229f4cbfa60a8dabbd14` |
| `connectors/opentable/manifest.yaml` | `/opt/hatch/connectors/opentable/manifest.yaml` | `f198654bfec686330496aba0661a487b4b2e2f0eaa68e68c5ecec290361985ce` |
| `connectors/outlook_calendar/CONNECTOR.md` | `/opt/hatch/connectors/outlook_calendar/CONNECTOR.md` | `3f4030c1e71050e79ce8824e354305e7a92c846fdf46612d966e0e2757c0e6ff` |
| `connectors/outlook_calendar/connector.yaml` | `/opt/hatch/connectors/outlook_calendar/connector.yaml` | `d76b68cb0178455d29838e7b90fa487e16d431bd361af7e99c49a5df75ead617` |
| `connectors/outlook_calendar/manifest.yaml` | `/opt/hatch/connectors/outlook_calendar/manifest.yaml` | `e25d0022917432fd5dea2a5597d20e7c7221c93f07c617b79d2d0d975d71b7f5` |
| `connectors/outlook_contacts/CONNECTOR.md` | `/opt/hatch/connectors/outlook_contacts/CONNECTOR.md` | `f4c04a37bcb01832ab1cbaebccaae84be28cbc3b9261beeb4662d01060d66f0a` |
| `connectors/outlook_contacts/connector.yaml` | `/opt/hatch/connectors/outlook_contacts/connector.yaml` | `d1fd460ce4f4dbe15318607869e1050feb760466b345eee732466e60f2217652` |
| `connectors/outlook_contacts/manifest.yaml` | `/opt/hatch/connectors/outlook_contacts/manifest.yaml` | `6a38484b528a41b99c48fe8837606ccb17346a5f4567fc11f1c0776127b078a8` |
| `connectors/outlook_mail/CONNECTOR.md` | `/opt/hatch/connectors/outlook_mail/CONNECTOR.md` | `097c5ef591b4e5200a414562e167e2c97dfd0af8aa1b7b528664a337c5768503` |
| `connectors/outlook_mail/connector.yaml` | `/opt/hatch/connectors/outlook_mail/connector.yaml` | `0ae701716681dc4109df1658f63373b7bba34770c629353744a5a5a0df146e3a` |
| `connectors/outlook_mail/manifest.yaml` | `/opt/hatch/connectors/outlook_mail/manifest.yaml` | `f17b04f213dc25052b263890e68d3d94372fdebcbef2111b438493825627c97d` |
| `connectors/peloton/CONNECTOR.md` | `/opt/hatch/connectors/peloton/CONNECTOR.md` | `4eeb74d24273c5dee9411fab208bb4c81f99172d081e78d503ef87c8e5668963` |
| `connectors/peloton/connector.yaml` | `/opt/hatch/connectors/peloton/connector.yaml` | `19cf0f0c0030b5b4bcd4361100a65b4b23e5481c6ebce96628a2bf3a6f7910af` |
| `connectors/peloton/manifest.yaml` | `/opt/hatch/connectors/peloton/manifest.yaml` | `6bbf7a374c71711374b6d48ac35395082775e996a7c810a829b56a711b7234eb` |
| `connectors/philips_hue/CONNECTOR.md` | `/opt/hatch/connectors/philips_hue/CONNECTOR.md` | `098e563e05ae2f3cb9d69dc3c9d9a6c4ec053f3a1f2b2ea83d7c4f55c37140ae` |
| `connectors/philips_hue/connector.yaml` | `/opt/hatch/connectors/philips_hue/connector.yaml` | `849da8df912215222f1292a49c96ca8560eada2b6671900278fd2d998582db4b` |
| `connectors/philips_hue/manifest.yaml` | `/opt/hatch/connectors/philips_hue/manifest.yaml` | `ae981a6383bbeda0c5ccd0b0e939e5f2d262b811e8939723bc3fda09ebb8f7bd` |
| `connectors/places/CONNECTOR.md` | `/opt/hatch/connectors/places/CONNECTOR.md` | `54dff8294151417b17facc66822ffc0ef41248472eafe616d299871af8534cbc` |
| `connectors/places/connector.yaml` | `/opt/hatch/connectors/places/connector.yaml` | `2b9d56b65b08aedadbb85174055ae12c06190ab5b63421d8856b5ecfd7521420` |
| `connectors/plaid/CONNECTOR.md` | `/opt/hatch/connectors/plaid/CONNECTOR.md` | `bae9459c1ca2909a5e57bd7baa344cd8321c4eb668b462f06eaae2b2efe7762d` |
| `connectors/plaid/connector.yaml` | `/opt/hatch/connectors/plaid/connector.yaml` | `c6fc8b389300db83b683b3380b8d364b4b307a0df0e9bd62221fca51a908eac4` |
| `connectors/plaid/manifest.yaml` | `/opt/hatch/connectors/plaid/manifest.yaml` | `697674ad97d5874607ec6d05d5e39cc529a51ff677656c3229075abf95c7d64a` |
| `connectors/printify/CONNECTOR.md` | `/opt/hatch/connectors/printify/CONNECTOR.md` | `a6c93129029db281d73dc180e55d602bcc2a1b508454514aeb185c4abdddfa1a` |
| `connectors/printify/connector.yaml` | `/opt/hatch/connectors/printify/connector.yaml` | `8106e4d4bcf4a87209e7e7547ebea07b6e3362c4de29b4bf509d12e6c7416150` |
| `connectors/printify/manifest.yaml` | `/opt/hatch/connectors/printify/manifest.yaml` | `c59008818b015b1f7d6e9339171167e1394f30f898442acfbe7918784c3acbc4` |
| `connectors/quickbooks/CONNECTOR.md` | `/opt/hatch/connectors/quickbooks/CONNECTOR.md` | `c18b15c93e058fd11b7723eda538b4940e0769a8fa0867b6274b3f1de0919ffc` |
| `connectors/quickbooks/connector.yaml` | `/opt/hatch/connectors/quickbooks/connector.yaml` | `10a7fe9ff31cb93e8c3b6243a10b74dd43579a91cb928994ef418bec40461f8b` |
| `connectors/quickbooks/manifest.yaml` | `/opt/hatch/connectors/quickbooks/manifest.yaml` | `c5cea901efed9a29f154040f9d9edb114b8bf3e2f86ac84ecd9461092a85ea69` |
| `connectors/replit/CONNECTOR.md` | `/opt/hatch/connectors/replit/CONNECTOR.md` | `1607507f6e83a54f2bb62c9fab3ebb7338733315f323f8e4a329ce983a8d4ccf` |
| `connectors/replit/connector.yaml` | `/opt/hatch/connectors/replit/connector.yaml` | `0c742c67a61136cd4de590a15ec794921e110c323d752eff875d827b59dad908` |
| `connectors/replit/manifest.yaml` | `/opt/hatch/connectors/replit/manifest.yaml` | `073c7a8d05bef72dc2f2bb449fec171e6e3a83d7ff720f7d83f9d507f3e36ac9` |
| `connectors/shop-pay/CONNECTOR.md` | `/opt/hatch/connectors/shop-pay/CONNECTOR.md` | `eb9163a377a85ee17bd24c3eb16945cf24a02a506e1d31f9ed97c2509e257205` |
| `connectors/shop-pay/connector.yaml` | `/opt/hatch/connectors/shop-pay/connector.yaml` | `580ae1ff3f5a5b5d4651b5a8b23d2cdbf102158fe9923400b118fabf3b484ea7` |
| `connectors/shop-pay/manifest.yaml` | `/opt/hatch/connectors/shop-pay/manifest.yaml` | `7d714947f67db59bb3d1cfcd56d68c6ad7003ef6ec2f8b0a123deb7be9352874` |
| `connectors/shopify/CONNECTOR.md` | `/opt/hatch/connectors/shopify/CONNECTOR.md` | `710561ad9b059290ec79b2fb1db84b28c49807490d7bbb501f83816dd4d69d63` |
| `connectors/shopify/connector.yaml` | `/opt/hatch/connectors/shopify/connector.yaml` | `b238806d18649b828758825fea00db847d426333123a86f5ebe25f90b2066c97` |
| `connectors/shopify/manifest.yaml` | `/opt/hatch/connectors/shopify/manifest.yaml` | `3313eb6ca6f53afeae631d8c201c4ad9925bfa6433f31b75beb83bc99e1b5f17` |
| `connectors/shopify-ucp/CONNECTOR.md` | `/opt/hatch/connectors/shopify-ucp/CONNECTOR.md` | `90d454cbf59e0982342b61bb413753b939dbc2dfbefb92e7913ff8f4b201c143` |
| `connectors/shopify-ucp/connector.yaml` | `/opt/hatch/connectors/shopify-ucp/connector.yaml` | `1e327bc16f5e1eb1b075695066e53171cede30266f51406e6fb3688704225850` |
| `connectors/shopify-ucp/manifest.yaml` | `/opt/hatch/connectors/shopify-ucp/manifest.yaml` | `6cd976d87e77c6597b2f0d845383ac05d7038668877045647bfd343d4c1bb7c3` |
| `connectors/slack/CONNECTOR.md` | `/opt/hatch/connectors/slack/CONNECTOR.md` | `32d1ff8857e8f51964ff12e04eb2a88213dfdb642d4c89b1d4d994af20b13641` |
| `connectors/slack/connector.yaml` | `/opt/hatch/connectors/slack/connector.yaml` | `abc2ce2995bc3dff3b18ffddacd2107ffbaa04b6a5d774f1b9c8b37196cf73dc` |
| `connectors/slack/manifest.yaml` | `/opt/hatch/connectors/slack/manifest.yaml` | `2b3930b8bfafe78ed05b33e2143f12c9c796af7378ec252a71ea5321af58f129` |
| `connectors/spotify/CONNECTOR.md` | `/opt/hatch/connectors/spotify/CONNECTOR.md` | `54ad1cd4047456629e10e08a673e5e68b416e91f54421df2dddd289fa0082bf2` |
| `connectors/spotify/connector.yaml` | `/opt/hatch/connectors/spotify/connector.yaml` | `16b7516e874c7bf0d580a7beb281917d13f11d2a3ab7a831249c0289aa7bebf7` |
| `connectors/spotify/manifest.yaml` | `/opt/hatch/connectors/spotify/manifest.yaml` | `baf534fa9c13b1400ae07610d1bc0a55f752b981b83e71dc0eeb98a6e66de366` |
| `connectors/stripe/CONNECTOR.md` | `/opt/hatch/connectors/stripe/CONNECTOR.md` | `0f415085031e3c84456ac4993427f19f075d7cbda6050e667005dd7a36d4cb7c` |
| `connectors/stripe/connector.yaml` | `/opt/hatch/connectors/stripe/connector.yaml` | `4ca7d04f1e615ba49293b4b2efe3728a6607f8589ba2072b82b4b90581759df0` |
| `connectors/stripe/manifest.yaml` | `/opt/hatch/connectors/stripe/manifest.yaml` | `4a612518c332b3027d493f6b6dab0ad67f46224c9bd68783b060050e893ab8e2` |
| `connectors/stripe-link/CONNECTOR.md` | `/opt/hatch/connectors/stripe-link/CONNECTOR.md` | `6e575130d733a6bb0289ab96772d5e916a16d385046335dfbc7c0d2d10cefb09` |
| `connectors/stripe-link/connector.yaml` | `/opt/hatch/connectors/stripe-link/connector.yaml` | `20f2b0a31d2c31fc0e735c2ef4f90eade3de430554357e31d61bdc16dd7e3920` |
| `connectors/stripe-link/manifest.yaml` | `/opt/hatch/connectors/stripe-link/manifest.yaml` | `c31623fbe5d65fa6d84e80728166c65ee32c9b933fe1a81a7350434d0b3283bc` |
| `connectors/tailscale/CONNECTOR.md` | `/opt/hatch/connectors/tailscale/CONNECTOR.md` | `5b04038e8dddb1ebc5d2bd336e6e246a8abd246b4e617a51ba25eccbb6bb89c8` |
| `connectors/tailscale/connector.yaml` | `/opt/hatch/connectors/tailscale/connector.yaml` | `d289794e409d8ee9014c8f571c064d397ba697cb2c1e51e19771f24be5b0f297` |
| `connectors/tessie/CONNECTOR.md` | `/opt/hatch/connectors/tessie/CONNECTOR.md` | `b06956a11a4e9d07b0a146b2ca9447a881b573948fbcc6d28fd61dad1a64fc9f` |
| `connectors/tessie/connector.yaml` | `/opt/hatch/connectors/tessie/connector.yaml` | `e1cb7814b99e69ed7d342fe21b17fa1558b99613ecf05c5d2f0718069754e7ca` |
| `connectors/tessie/manifest.yaml` | `/opt/hatch/connectors/tessie/manifest.yaml` | `e4644f578d24e184b175366bf85656bf4609ffdf3e5c1eec955331a76713a218` |
| `connectors/threads/CONNECTOR.md` | `/opt/hatch/connectors/threads/CONNECTOR.md` | `dc0d904c578be18237cb316b1dced1c943861ed3b971902aae8d4d3e896a13e8` |
| `connectors/threads/connector.yaml` | `/opt/hatch/connectors/threads/connector.yaml` | `21735f1c8c454ea0a6c7fb40545d9e3d402a338ecc764ffac20c4f0dcfff3a92` |
| `connectors/threads/manifest.yaml` | `/opt/hatch/connectors/threads/manifest.yaml` | `6d230010126d01dac64605c8a45128b5c6f38dcedfbecf7c160fab685e568be1` |
| `connectors/threads_messages/CONNECTOR.md` | `/opt/hatch/connectors/threads_messages/CONNECTOR.md` | `ab934470d84bbb22740a417239e92d6a0628d1ce229d02bf071c313fbbe679d3` |
| `connectors/threads_messages/connector.yaml` | `/opt/hatch/connectors/threads_messages/connector.yaml` | `7035ea1e74a32f8c6dd434b84218b198d9b6b80adb54fcb779d3575860882f51` |
| `connectors/threads_messages/manifest.yaml` | `/opt/hatch/connectors/threads_messages/manifest.yaml` | `b900c53f992dec3a13e0f854507fb7c2c9a353625f0f526daa122117c136fcd8` |
| `connectors/ticketmaster/CONNECTOR.md` | `/opt/hatch/connectors/ticketmaster/CONNECTOR.md` | `76c2b01cecf9d30aa9c15c31538dec7f67ef7da066859933f649c920781b25fa` |
| `connectors/ticketmaster/connector.yaml` | `/opt/hatch/connectors/ticketmaster/connector.yaml` | `1336cccfe371f80940876a5be63266aea5c4d4e871a94a594b2ba15f6dd885b6` |
| `connectors/ticketmaster/manifest.yaml` | `/opt/hatch/connectors/ticketmaster/manifest.yaml` | `5bda5daf48f7d0f0c01e8409b62daa1963973797c0f50d632da9bc12f504dc3d` |
| `connectors/todoist/CONNECTOR.md` | `/opt/hatch/connectors/todoist/CONNECTOR.md` | `ee4ea20203e58b1ab02cf183f9d840e18c6887fd190910d7fcb818d2221025c6` |
| `connectors/todoist/connector.yaml` | `/opt/hatch/connectors/todoist/connector.yaml` | `541e74f8f824234a0f0bfda998ee4a2ebabf2e13ed6b20a6a5e101fd7dedb151` |
| `connectors/todoist/manifest.yaml` | `/opt/hatch/connectors/todoist/manifest.yaml` | `806196291310dba602031410120796d28f7e9a09275d657f3fe8cfb0ec79b278` |
| `connectors/vercel/CONNECTOR.md` | `/opt/hatch/connectors/vercel/CONNECTOR.md` | `dcbf45fd181890dc51caa29b66b1803d99d80eb54ec74f78b1b5bcadde7d73a8` |
| `connectors/vercel/connector.yaml` | `/opt/hatch/connectors/vercel/connector.yaml` | `a231c6cc073fd8401670e9b36250fd3410e4408f7b8127b4f62c8f9d80143231` |
| `connectors/vercel/manifest.yaml` | `/opt/hatch/connectors/vercel/manifest.yaml` | `268a4ae00f4a8e5578b60369360bdd6e2968dd1c2791c8eb6ad1c9fe2d8832ad` |
| `connectors/withings/CONNECTOR.md` | `/opt/hatch/connectors/withings/CONNECTOR.md` | `1f9a27996fc2d87178f53acf6ef986714cf8549e1a8f25c96272528437efeb87` |
| `connectors/withings/connector.yaml` | `/opt/hatch/connectors/withings/connector.yaml` | `592cc57490710fa311af8020dc182fed7d6975c704621ae41988ca0fdb6fa109` |
| `connectors/withings/manifest.yaml` | `/opt/hatch/connectors/withings/manifest.yaml` | `190aa8a67cd492a0949b0470eca937c1f79183e767d9b4f785d854100d256d6a` |
| `connectors/zapier/CONNECTOR.md` | `/opt/hatch/connectors/zapier/CONNECTOR.md` | `190b2c9375cceabee1f7b0862efc3d0fa1c830a1b83c46e2d559d064fb8df63b` |
| `connectors/zapier/connector.yaml` | `/opt/hatch/connectors/zapier/connector.yaml` | `c06aea04bbee152f8b10b30d0621e5d18b414b5b3939584f0016aaa0a2db6eeb` |
| `connectors/zapier/manifest.yaml` | `/opt/hatch/connectors/zapier/manifest.yaml` | `aea56a9940b4181e66ae5a34154a6c928ca3bbfce25e26b1d53fb9b597575523` |
| `connectors/zoom/CONNECTOR.md` | `/opt/hatch/connectors/zoom/CONNECTOR.md` | `125f0a809b715d7b19ebfa1fb97ebb561fae0dd668eb2f6c6aaa45096f733350` |
| `connectors/zoom/connector.yaml` | `/opt/hatch/connectors/zoom/connector.yaml` | `676dce31ebabcd5f3a19eda764e6635d7cf9fe7af6ebcd7e3cd88f44068325d6` |
| `connectors/zoom/manifest.yaml` | `/opt/hatch/connectors/zoom/manifest.yaml` | `f3bd9f476c18b7cc9ffdbc8e453e5c0626fd49d6d12e436d382531dd643c4280` |
| `docs/HEARTBEAT.md` | `~/HEARTBEAT.md` | `55acc18c4867cf74151fdb2962a5d9be756cda277a329e65ad3bd3a29e3eb62b` |
| `docs/artifacts.md` | `~/docs/artifacts.md` | `4243dd4e55acc8e22aad66a10c260300ea98eeba907b3690424eb511280df979` |
| `docs/browser.md` | `~/docs/browser.md` | `f8a7b97a541a1d40cb0eddb06df00b4337bb075c597244e061c90fe54920b913` |
| `docs/calls-texts-notifications.md` | `~/docs/calls-texts-notifications.md` | `44813f1d71a95610c9a1fb5e318169e9ed1499fdebabfe3fcb04125beccab9c1` |
| `docs/chat-connections.md` | `~/docs/chat-connections.md` | `66a379453cf0d3648f2b478c10335298908f69fb7ea3505ffa788af576c6e3b0` |
| `docs/client-surfaces.md` | `~/docs/client-surfaces.md` | `b993915ba64fde1b09d012de2885946bfe4fcfe55a7a87db22c1fe6ee7503e3e` |
| `docs/connectors.md` | `~/docs/connectors.md` | `06b58b010b8b809700f61f116cde627708f1b9f030ef4fbc42b3aeedcb2d877e` |
| `docs/data-handling.md` | `~/docs/data-handling.md` | `fd15f933405407333fda8199aa731af5fc3f8f9295bb25ed8a4425504119c3e6` |
| `docs/feed.md` | `~/docs/feed.md` | `85c6962fdf27243d87f87ec48426d2712631877a16ca6dfe7b388f98c5933568` |
| `docs/files-and-library.md` | `~/docs/files-and-library.md` | `7d2f8401cd0fa55c07a33173e626ac8a24e38ff8e22df0ca08db10a13b33287c` |
| `docs/goals.md` | `~/docs/goals.md` | `7754700194935890313ac9e63797e15e74ceea834e6b04fce28dccd3f57afc5e` |
| `docs/ideas.md` | `~/docs/ideas.md` | `668d9dae6ef64c649b9a601bd7257eaa16172d43d1ee2abd4fad5f7aa30146b3` |
| `docs/memory.md` | `~/docs/memory.md` | `3aa1197e55b80a60af927595417226232187f290279d8f2e0e24a5b8b946656e` |
| `docs/muse.md` | `~/docs/muse.md` | `6406c2f204fa46d1197c0bcd56103e82ec419756b2974ba7557c20670c6f9793` |
| `docs/privacy-and-credentials.md` | `~/docs/privacy-and-credentials.md` | `92fc0e41fbc1ec206ae584cd445c548966d1f4ebbc991b01a1e44190cca87f53` |
| `docs/scheduling-and-watching.md` | `~/docs/scheduling-and-watching.md` | `7940ef38be47495a3e275052853a1f87932c5a2830492a5ee0112d3be0f43811` |
| `docs/self_improvement.md` | `~/docs/self_improvement.md` | `595a36bb46050a0e390ec4aaa4da95b16ff2a0710302468fbad23e9012f7ce44` |
| `docs/chat/scheduling-and-watching.md` | `~/docs/chat/scheduling-and-watching.md` | `c00d4c4e147e72ed7ba74868b673f83f283d1984c9f6367af71ee0971b932e74` |
| `docs/chat-connections/whatsapp.md` | `~/docs/chat-connections/whatsapp.md` | `827333a356122fda3b2338c3c92615623eb6edfbef2e7bbc904897eadf40ddf5` |
| `inventory/connectors.txt` | `Directory listing of /opt/hatch/connectors/` | `e6a32b39ddd91096ff5f965e4a49b110f5c30f7e40b27f410edad81e1c09407d` |
| `inventory/skills.txt` | `Directory listing of /opt/muse/skills/` | `6d6b94dbb944d7f8b11c7dcf6de22d29d9d92011844e024f9ac0fffa7a3a281c` |
| `inventory/skills.yaml` | `~/config/skills.yaml` | `d1438a0080f1fa59ad4eb9a096da5f04994686e66e3d4e468b272c8f34905630` |
| `muse-db/identifiers.md` | `/opt/muse/skills/muse_db/references/identifiers.md` | `5be4b0f4e73184428e56eea4b8b95481f96c867805fb242799aba762dcbd1e65` |
| `muse-db/querying.md` | `/opt/muse/skills/muse_db/references/querying.md` | `6f6bc7289778871ceb5aa821ca385a1efd5125bc23f425c80c6e06fd9702db9c` |
| `muse-db/schema.md` | `/opt/muse/skills/muse_db/references/schema.md` | `ee48a5575b786176a5c6e46ead221726e45e46f2c7ec1a9eeaee209a2b3f1f9f` |
| `muse-db/tables/activity.activity_monitor_agent_threads.md` | `/opt/muse/skills/muse_db/references/tables/activity.activity_monitor_agent_threads.md` | `fad7c69cae432209d42069cab64953854f6b9760d9e90b41f610cdbe22f6d440` |
| `muse-db/tables/activity.activity_monitor_carrier_user_messages.md` | `/opt/muse/skills/muse_db/references/tables/activity.activity_monitor_carrier_user_messages.md` | `e3806ded4f8eb2555091424240e45b54b4c0b7b73affce56d23edf98a459396f` |
| `muse-db/tables/activity.activity_monitor_message_threads.md` | `/opt/muse/skills/muse_db/references/tables/activity.activity_monitor_message_threads.md` | `d5153361981910b1414a976b9df6d17d4ac6fd70f34f5a7741debfc4ce90c16d` |
| `muse-db/tables/activity.activity_monitor_runtime_work_threads.md` | `/opt/muse/skills/muse_db/references/tables/activity.activity_monitor_runtime_work_threads.md` | `36fa8c3d31f652dc9c92395021b3468c1cbf945c1b1a10e1e815877b414ae776` |
| `muse-db/tables/activity.activity_monitor_thread_actions.md` | `/opt/muse/skills/muse_db/references/tables/activity.activity_monitor_thread_actions.md` | `d91f4f18db9f42159ef1e3aa3e1a46eda35c57db5e30b3dd038f08086c020184` |
| `muse-db/tables/activity.activity_monitor_thread_sections.md` | `/opt/muse/skills/muse_db/references/tables/activity.activity_monitor_thread_sections.md` | `c95880eca107044a28f267e64bb56b8fbc8ab8840f5bcb8185c92c0842ac0b3b` |
| `muse-db/tables/activity.activity_monitor_threads.md` | `/opt/muse/skills/muse_db/references/tables/activity.activity_monitor_threads.md` | `7bb043c98821d463183213bc8892887c877cccc4a86736571728d0f8e6c7e8d1` |
| `muse-db/tables/activity.feed_entries.md` | `/opt/muse/skills/muse_db/references/tables/activity.feed_entries.md` | `4506f13e88a86c4a70ab265bca85b733875633c5fe7e9111bc53aecb77bd2356` |
| `muse-db/tables/agent.agent_ancestors.md` | `/opt/muse/skills/muse_db/references/tables/agent.agent_ancestors.md` | `0084dcd5753e14eaaec083fb94dab75304ffbd4e1d6dd2df523b43b7ff10adab` |
| `muse-db/tables/agent.agent_compactions.md` | `/opt/muse/skills/muse_db/references/tables/agent.agent_compactions.md` | `cb28e6a6ea3b12bc24c015d37912b5afd99755c73d730e65486b0a3b6c18269a` |
| `muse-db/tables/agent.agent_message_token_usage.md` | `/opt/muse/skills/muse_db/references/tables/agent.agent_message_token_usage.md` | `44889215ea67507cc7cb4b3c5d9b9988263da5b9359a0f302c6b76d04728c29d` |
| `muse-db/tables/agent.agents.md` | `/opt/muse/skills/muse_db/references/tables/agent.agents.md` | `bb39c09978c96441f507b26dd4b5ceafe174c6c49635bf434085520893cd7886` |
| `muse-db/tables/agent.chat_preferences.md` | `/opt/muse/skills/muse_db/references/tables/agent.chat_preferences.md` | `b01dad7049a699743e39ca14e94c5e4003eac813836bcb2f1128e81730f3ebf8` |
| `muse-db/tables/agent.compactions.md` | `/opt/muse/skills/muse_db/references/tables/agent.compactions.md` | `dbb66d9058edf4844d1a448bd37ccae2ce5c946045e7a8470cc439b97562fc0d` |
| `muse-db/tables/agent.context_item_derived_write_backlog.md` | `/opt/muse/skills/muse_db/references/tables/agent.context_item_derived_write_backlog.md` | `a4c070596efde25e44c117bb183f85880ffa8202eb02c21b849c6812a8f8a966` |
| `muse-db/tables/agent.context_item_fields.md` | `/opt/muse/skills/muse_db/references/tables/agent.context_item_fields.md` | `6bf19a0d46af842e5f2d7f5b9be1c74868a9e41b053f18695edbf8b1a35bf5b2` |
| `muse-db/tables/agent.context_item_resume_projection.md` | `/opt/muse/skills/muse_db/references/tables/agent.context_item_resume_projection.md` | `e747e8178bd077d93d2d0b542223f0b5ff209760bc37755d5c7e38699a914935` |
| `muse-db/tables/agent.context_items.md` | `/opt/muse/skills/muse_db/references/tables/agent.context_items.md` | `322d146e36518e5843068a78743edbe544b2aad094882252d8f49e9187a06a03` |
| `muse-db/tables/agent.context_text_segments.md` | `/opt/muse/skills/muse_db/references/tables/agent.context_text_segments.md` | `05fe3faea7b9f93b1729853efcb467781e0158a9ee44d36e3c718784b4217e4f` |
| `muse-db/tables/agent.message_mailbox.md` | `/opt/muse/skills/muse_db/references/tables/agent.message_mailbox.md` | `2e7ef4822cdeac3529d54dd017ed198f3d6436ae35cb4349722ac142ce6b1212` |
| `muse-db/tables/agent.recovery_owner_terminal_events.md` | `/opt/muse/skills/muse_db/references/tables/agent.recovery_owner_terminal_events.md` | `e306f816215c928114c73fdd9e0163f0e49b4cc1aa971b9fb81d919a835324f3` |
| `muse-db/tables/agent.recovery_owners.md` | `/opt/muse/skills/muse_db/references/tables/agent.recovery_owners.md` | `d723fb7a12b1daf4c55ce80c7598cc1a6403c935074ed10be66b24d45c11fdb8` |
| `muse-db/tables/agent.runtime_restart_checkpoints.md` | `/opt/muse/skills/muse_db/references/tables/agent.runtime_restart_checkpoints.md` | `a70db4ad4ee4f885c87d2ef3ac91f9da12390ab1e11580c9c091864c1cd3bddf` |
| `muse-db/tables/agent.runtime_state.md` | `/opt/muse/skills/muse_db/references/tables/agent.runtime_state.md` | `ca2901239f0483957b24e8b85a4533fd319f319b148fd48eda23213be0e95950` |
| `muse-db/tables/agent.session_memory_capture_deadlines.md` | `/opt/muse/skills/muse_db/references/tables/agent.session_memory_capture_deadlines.md` | `d7c4225334cf6aa44ba000c7780b458f2dafa7a275ffe807bdbc71df5c4da5ef` |
| `muse-db/tables/agent.sessions.md` | `/opt/muse/skills/muse_db/references/tables/agent.sessions.md` | `9f98a730b032d294b78efc8563ac107bdfa0ed09957a49167fe2ff778542c452` |
| `muse-db/tables/agent.subagent_monitor_decisions.md` | `/opt/muse/skills/muse_db/references/tables/agent.subagent_monitor_decisions.md` | `828e7619502b52c1201fb76861ff3485e6d379ebef5748996086718cb3e24005` |
| `muse-db/tables/agent.subagent_progress.md` | `/opt/muse/skills/muse_db/references/tables/agent.subagent_progress.md` | `9776999ee0418e1fceb7ae4c8e98f4beaa6764786866ea58225fa6f833f326a5` |
| `muse-db/tables/agent.subagent_progress_message_events.md` | `/opt/muse/skills/muse_db/references/tables/agent.subagent_progress_message_events.md` | `32cfb7e8d4454981f2bc3a4c864cc8b67ab70669705a0b99a7b449bce73d13dc` |
| `muse-db/tables/agent.subagent_progress_tool_events.md` | `/opt/muse/skills/muse_db/references/tables/agent.subagent_progress_tool_events.md` | `e7a83475e790ed6296eb1802159fc68e81d0a3e3a1defe332a8e0d65aacf85c9` |
| `muse-db/tables/agent.subagent_spawns.md` | `/opt/muse/skills/muse_db/references/tables/agent.subagent_spawns.md` | `3ac99ea5b160716b65d756bb8932bcc7e4a4053462d8482ce2e85eb081762308` |
| `muse-db/tables/agent.token_usage.md` | `/opt/muse/skills/muse_db/references/tables/agent.token_usage.md` | `0bfcc59c63fe0fc69f43dfc0daa3e171c175aadae24267dfce07665a0b96ac79` |
| `muse-db/tables/agent.volatile_context_pins.md` | `/opt/muse/skills/muse_db/references/tables/agent.volatile_context_pins.md` | `e4cee6ca2be23faf964eed26f0c42d085234d561823bcf8131857d0518d703ab` |
| `muse-db/tables/chat.chats.md` | `/opt/muse/skills/muse_db/references/tables/chat.chats.md` | `41c4c35b9901cf0ab05badeb771c09aa378fd93c8d25fd7fb3790d3277681270` |
| `muse-db/tables/chat.event_transports.md` | `/opt/muse/skills/muse_db/references/tables/chat.event_transports.md` | `fd3d68fa5c429bbfd048049b58805d79d47804383deebe75ddc1e29aa5023ec6` |
| `muse-db/tables/chat.message_bindings.md` | `/opt/muse/skills/muse_db/references/tables/chat.message_bindings.md` | `35294637fdac39b9e0c13e803b30d26bb4266e7fe119b6dad865bdfd8cc99e97` |
| `muse-db/tables/device.calendar_events.md` | `/opt/muse/skills/muse_db/references/tables/device.calendar_events.md` | `ede0e61e908b6049e32139ea2c412fe1d2f6f907908ba93be9fd3047938a04b6` |
| `muse-db/tables/device.call_log.md` | `/opt/muse/skills/muse_db/references/tables/device.call_log.md` | `b7a744da8613892ef394aa41f8be9445062e3296d27d9c0f1233a652468830d9` |
| `muse-db/tables/device.client_contexts.md` | `/opt/muse/skills/muse_db/references/tables/device.client_contexts.md` | `800c858634c9e5a3308e4efb737cf8b9f68479f0781b578c70435e72b6b268e4` |
| `muse-db/tables/device.contact_addresses.md` | `/opt/muse/skills/muse_db/references/tables/device.contact_addresses.md` | `ce514a9a4da0942dcb9690d1f8c7c5b5cf772bb68c83835f229b55eb2ba19bf2` |
| `muse-db/tables/device.contact_emails.md` | `/opt/muse/skills/muse_db/references/tables/device.contact_emails.md` | `2fe81892d5af11b46d018af792657b2bfee23cfadfa591023ad0b21e982947c3` |
| `muse-db/tables/device.contact_phones.md` | `/opt/muse/skills/muse_db/references/tables/device.contact_phones.md` | `437f1400c81ee3cce6193081fb55bf11fefabc55b1dec91d7bbba0ac1fcefae1` |
| `muse-db/tables/device.contacts.md` | `/opt/muse/skills/muse_db/references/tables/device.contacts.md` | `6cd28c656d06b2c4b245a30339db825a13df758c000988a8025a53f1ecddd602` |
| `muse-db/tables/device.data_sync_state.md` | `/opt/muse/skills/muse_db/references/tables/device.data_sync_state.md` | `753783eddb053bfd033657ded67ccfc1f0c6822b400bbede0ed6c003eb273777` |
| `muse-db/tables/device.media_upload_batches.md` | `/opt/muse/skills/muse_db/references/tables/device.media_upload_batches.md` | `e8abc14833afdd1ba0b667624cc014e082bb448ff2cd55707df0d40ffdf27bf4` |
| `muse-db/tables/device.media_upload_events.md` | `/opt/muse/skills/muse_db/references/tables/device.media_upload_events.md` | `8485f2693df849572ca5fe8d5202acf2fba60ffe11847afdd67695d74f22d14b` |
| `muse-db/tables/device.nodes.md` | `/opt/muse/skills/muse_db/references/tables/device.nodes.md` | `bc72cdb990e7d3f7f0bee4745213352f8c7cac0678d13eeb556d6b992720b0d4` |
| `muse-db/tables/device.upload_chunks.md` | `/opt/muse/skills/muse_db/references/tables/device.upload_chunks.md` | `ba152a9d974582e050af37311bbb1402da18be4bf421f623729fb6223b09ceff` |
| `muse-db/tables/device.upload_sessions.md` | `/opt/muse/skills/muse_db/references/tables/device.upload_sessions.md` | `82c389fcc0b9fd9d49f444e998b8b7d7db9f31342fb294515f376b7c08195cf8` |
| `muse-db/tables/feed.fleet_engagement_contributions.md` | `/opt/muse/skills/muse_db/references/tables/feed.fleet_engagement_contributions.md` | `9fb74807e4e9dcffa2a8d4f36f8f2d9ab64c7d83e37b44ded105c0c48de54713` |
| `muse-db/tables/feed.fleet_engagement_outbox.md` | `/opt/muse/skills/muse_db/references/tables/feed.fleet_engagement_outbox.md` | `8f91c4b5f981dc3438d6c058664f4d41484720b65ee454accbd6416e4e03e695` |
| `muse-db/tables/feed.fleet_fetch_receipts.md` | `/opt/muse/skills/muse_db/references/tables/feed.fleet_fetch_receipts.md` | `831a4961fd412394ce742b98e0abfe90a0e3e360c5aa7ae8ef5275b6e5da8e0c` |
| `muse-db/tables/feed.fleet_publish_state.md` | `/opt/muse/skills/muse_db/references/tables/feed.fleet_publish_state.md` | `99c05910042f2c0a51af7fa72d9a9629d9492ea3aa50878ccaaaa32dc1ca9efb` |
| `muse-db/tables/feed.fleet_reaction_outbox.md` | `/opt/muse/skills/muse_db/references/tables/feed.fleet_reaction_outbox.md` | `7e700375610230eeafa839d9c3a3d08ab2a4b2c5c9b32b7d75f7d4adc4446030` |
| `muse-db/tables/feed.interactions.md` | `/opt/muse/skills/muse_db/references/tables/feed.interactions.md` | `2bf638b1890809442d02dc4320e9f8081985126aa3ad3947ea719fc3a48bdb79` |
| `muse-db/tables/feed.null_state_seed.md` | `/opt/muse/skills/muse_db/references/tables/feed.null_state_seed.md` | `652abd4112046728c11e2292c94a1934bf4b7f783959a6e0d5763b3877fbb3bf` |
| `muse-db/tables/feed.preferences_projection.md` | `/opt/muse/skills/muse_db/references/tables/feed.preferences_projection.md` | `5d2f389f86131541c6a72d02306f2cf373a6e92aa9f5ef5168fc3b35792ac9d7` |
| `muse-db/tables/feed.prompt_scope_verdict.md` | `/opt/muse/skills/muse_db/references/tables/feed.prompt_scope_verdict.md` | `757c78e3a2052285f4499e526949f776709665afe16c2c495ead874e46123882` |
| `muse-db/tables/feed.prompt_seed.md` | `/opt/muse/skills/muse_db/references/tables/feed.prompt_seed.md` | `6f27ad3781afba23d51b770a8f59ed98894197b2303538971d034c3a561ace6d` |
| `muse-db/tables/feed.promptless_unit_orders.md` | `/opt/muse/skills/muse_db/references/tables/feed.promptless_unit_orders.md` | `3956d47b0c857ecee04a44c2f74b7f724cd51aab017a918bddf13c5b0b15f274` |
| `muse-db/tables/feed.prompts.md` | `/opt/muse/skills/muse_db/references/tables/feed.prompts.md` | `a78ba0c4a38766a418dfd5d0927a3b7bda797852baa632399771a8a8aa8f18c2` |
| `muse-db/tables/feed.run_steps.md` | `/opt/muse/skills/muse_db/references/tables/feed.run_steps.md` | `46ef0278a8cba4938cd377f199606d4f129b446785feb3957b5e9618858ccfad` |
| `muse-db/tables/feed.runs.md` | `/opt/muse/skills/muse_db/references/tables/feed.runs.md` | `c7e168818732cff27de54640158803df294a76ccd98cf0cca6d38ee3adeb39a2` |
| `muse-db/tables/feed.surface_state.md` | `/opt/muse/skills/muse_db/references/tables/feed.surface_state.md` | `8742585f55328947b7dd5d6ca891083441e6325c4ec184eedfd8b26026f0442b` |
| `muse-db/tables/feed.units.md` | `/opt/muse/skills/muse_db/references/tables/feed.units.md` | `8138c145a090b6a95e5e8539c3907d2403c0984603f1e2b6889334b5a8cbe41f` |
| `muse-db/tables/goals.actions.md` | `/opt/muse/skills/muse_db/references/tables/goals.actions.md` | `c6a6d5673d422bff043f9dcef2b6a64df90a50b2af24b4822550a94e388a8a23` |
| `muse-db/tables/goals.associations.md` | `/opt/muse/skills/muse_db/references/tables/goals.associations.md` | `1845aab865667bdfcf5363f86c53beda30e13732d9d439b7d4de58eb12a36e53` |
| `muse-db/tables/goals.briefings.md` | `/opt/muse/skills/muse_db/references/tables/goals.briefings.md` | `698c31ed6f3ea276a6a0a4fd810705f0422fbd50f8f52c80f1270b88d7af3897` |
| `muse-db/tables/goals.engagement_events.md` | `/opt/muse/skills/muse_db/references/tables/goals.engagement_events.md` | `aa70f1df8ef505df018ae5b8987d3e72664a6a133b604c352fca9405a7f0a4a2` |
| `muse-db/tables/goals.goals.md` | `/opt/muse/skills/muse_db/references/tables/goals.goals.md` | `495234fbddfecbc62661d3a6f63b2a9097a5ae7b80b08a7c26fcbf6d4be9458d` |
| `muse-db/tables/goals.learning_state.md` | `/opt/muse/skills/muse_db/references/tables/goals.learning_state.md` | `5c4f167554066cb56a6e494f9600c8b85746bb7e54e77c3512804cf6e2db4f06` |
| `muse-db/tables/goals.momentum_history.md` | `/opt/muse/skills/muse_db/references/tables/goals.momentum_history.md` | `4c1bc2ae8c66a086721240273d51233bff049dda550cfb1dea26c249c47e4dd7` |
| `muse-db/tables/goals.sessions.md` | `/opt/muse/skills/muse_db/references/tables/goals.sessions.md` | `afa1b3184dfce4ad2c24791ec029e737fea2fbb356aeb2fdc9933c0f230dfbe8` |
| `muse-db/tables/goals.suggestions.md` | `/opt/muse/skills/muse_db/references/tables/goals.suggestions.md` | `452b39a289766e3ff825f39aff3a4d942a6e85bedfba1c2c0780f03392cbee15` |
| `muse-db/tables/goals.thread_actions.md` | `/opt/muse/skills/muse_db/references/tables/goals.thread_actions.md` | `b8d84d7dd4d55908f12472db9f6cc206b459a06ac12e59257fb2b3747a9f6f38` |
| `muse-db/tables/goals.threads.md` | `/opt/muse/skills/muse_db/references/tables/goals.threads.md` | `b1e96a3126be862a9bf8c322f5f220b2c66b91393da63f6a9712991ec7bbda5b` |
| `muse-db/tables/goals.updates.md` | `/opt/muse/skills/muse_db/references/tables/goals.updates.md` | `adcd5288e0654cef86bc5e11ac27c3bb0a1890c7f88bcd6a814303292c460162` |
| `muse-db/tables/health.aggregates.md` | `/opt/muse/skills/muse_db/references/tables/health.aggregates.md` | `051461d4717db5867bc9b81bf2f7847dffe73b14af04169d92bdde0ac10b6015` |
| `muse-db/tables/health.events.md` | `/opt/muse/skills/muse_db/references/tables/health.events.md` | `7cdcd781af7186efb78fe2f3f59bab9687888bfa22465e82a525764ffa204e2f` |
| `muse-db/tables/health.record_values.md` | `/opt/muse/skills/muse_db/references/tables/health.record_values.md` | `703105f25a986cecb8f533e6c9e26c3480a329299f4fb9332d9781b746e8c679` |
| `muse-db/tables/health.sample_values.md` | `/opt/muse/skills/muse_db/references/tables/health.sample_values.md` | `582f86e31f623a8222f312156d1674044de3780eb34fe4cc9bc8de2c42452807` |
| `muse-db/tables/health.samples.md` | `/opt/muse/skills/muse_db/references/tables/health.samples.md` | `3b95b686314c02aaf695e1e420d0a98b679528521aad8f5f58369e6deb20df47` |
| `muse-db/tables/health.sleep_sessions.md` | `/opt/muse/skills/muse_db/references/tables/health.sleep_sessions.md` | `eff9bf620ad45835a542c500ab25cf1d6c6d2207c0f4d600893b9e45ca7b0f81` |
| `muse-db/tables/health.synced_ranges.md` | `/opt/muse/skills/muse_db/references/tables/health.synced_ranges.md` | `09c67e6b4b55d40f14dea82564e9233bf1667843925b48a8dfd8c38444482c9e` |
| `muse-db/tables/health.workouts.md` | `/opt/muse/skills/muse_db/references/tables/health.workouts.md` | `be475da5c603c5ac0d0d30ce3659edeb6823a102a331493b1addaa7d22b7f761` |
| `muse-db/tables/ideas.bandit_arm_state.md` | `/opt/muse/skills/muse_db/references/tables/ideas.bandit_arm_state.md` | `be5b30b3e0744591df20089d264c17b7f674f243bad2af3d1e8ae7d98def56fa` |
| `muse-db/tables/ideas.bandit_fold_state.md` | `/opt/muse/skills/muse_db/references/tables/ideas.bandit_fold_state.md` | `a813e576f75c6d343314106e4ff139c4d5f359598238628428473860cfb4f456` |
| `muse-db/tables/ideas.bandit_folded_events.md` | `/opt/muse/skills/muse_db/references/tables/ideas.bandit_folded_events.md` | `0da9b760101ae9fb24b5acaf0790ee61cc27cef767a5a820fb205789f483f1ad` |
| `muse-db/tables/ideas.discovery_pool_history.md` | `/opt/muse/skills/muse_db/references/tables/ideas.discovery_pool_history.md` | `e9079f6a205272e9def6e638b9c3c7e604eece7fa6b90a2eec0279a4d1c3e71c` |
| `muse-db/tables/ideas.discovery_pool_meta.md` | `/opt/muse/skills/muse_db/references/tables/ideas.discovery_pool_meta.md` | `793d5cc1b3a80f7d6113dc364d95224ff37ec3cc201e1abe95bfe1bd64a1e4fa` |
| `muse-db/tables/ideas.explore_policy.md` | `/opt/muse/skills/muse_db/references/tables/ideas.explore_policy.md` | `947676c8aa382d4b9cbfdc5a12327c07f8aa42ec51abee0eaa0a316a66f0a61c` |
| `muse-db/tables/ideas.feed_snapshot_cards.md` | `/opt/muse/skills/muse_db/references/tables/ideas.feed_snapshot_cards.md` | `1a6243f61d27f14725e7341873b745207eae56500fe1fbc08283036f0f33e449` |
| `muse-db/tables/ideas.feed_snapshot_sections.md` | `/opt/muse/skills/muse_db/references/tables/ideas.feed_snapshot_sections.md` | `16de38bcd076e3ed8af93e0381e9ef9f3de68ef55d9cb384ce3bf13f913c3929` |
| `muse-db/tables/ideas.feed_snapshots.md` | `/opt/muse/skills/muse_db/references/tables/ideas.feed_snapshots.md` | `7ff99fe438f5e3e88317d3072faf244e2ba39dfeafc3b2d2f061b7b3e2a25129` |
| `muse-db/tables/ideas.icon_embeddings.md` | `/opt/muse/skills/muse_db/references/tables/ideas.icon_embeddings.md` | `0305826ac0518053715bb7362daeb61005f09a26de2b104e4ea899e6e780487f` |
| `muse-db/tables/ideas.idea_anchors.md` | `/opt/muse/skills/muse_db/references/tables/ideas.idea_anchors.md` | `ee6e3603367721dc6f5071ffb8830e9eec536c6bd67138bf02b77b8f31569328` |
| `muse-db/tables/ideas.idea_build_status.md` | `/opt/muse/skills/muse_db/references/tables/ideas.idea_build_status.md` | `a52a4c5a0aa5ea582e7f304f429959ff2057b07e5e3d636a1f1a9569db97f7bf` |
| `muse-db/tables/ideas.idea_card_feeds.md` | `/opt/muse/skills/muse_db/references/tables/ideas.idea_card_feeds.md` | `ca8a9c3952a0e06a8b7f0de14208e71be4c2e0cbf2aa8693c1ddc9a2a0f170a8` |
| `muse-db/tables/ideas.idea_dedup.md` | `/opt/muse/skills/muse_db/references/tables/ideas.idea_dedup.md` | `dd60afe6c4f67b287c077fd5d853d50c1e6085c4bc861256dc91f894ffa44cd3` |
| `muse-db/tables/ideas.idea_events.md` | `/opt/muse/skills/muse_db/references/tables/ideas.idea_events.md` | `1763df55e98e70789676dd601b4cbe4dce18cb82ccd6536762c383786745fe64` |
| `muse-db/tables/ideas.idea_feedback_state.md` | `/opt/muse/skills/muse_db/references/tables/ideas.idea_feedback_state.md` | `d989cac36dcbd9e4b85488dff5dd3ace80fb00b50e8f794b534134039d0de1b2` |
| `muse-db/tables/ideas.idea_install_assets.md` | `/opt/muse/skills/muse_db/references/tables/ideas.idea_install_assets.md` | `10ae880777ff67418e0e4d18199696c5ef55f6fe81c716657f3fa22db3bd9bf5` |
| `muse-db/tables/ideas.idea_items.md` | `/opt/muse/skills/muse_db/references/tables/ideas.idea_items.md` | `db54ff489737199ec4794dd614d4b35888a588348b2a4ab4e5a693c13b716109` |
| `muse-db/tables/ideas.idea_quality.md` | `/opt/muse/skills/muse_db/references/tables/ideas.idea_quality.md` | `81521d7424b374480073a47276e26a4e2ca63cb719e31898b90bbc482a30d50b` |
| `muse-db/tables/ideas.idea_sources.md` | `/opt/muse/skills/muse_db/references/tables/ideas.idea_sources.md` | `8716b9284d3214f9b9c45a1f7c97a8f5941818443b94e703d0dede1d8aaf34ec` |
| `muse-db/tables/ideas.idea_tags.md` | `/opt/muse/skills/muse_db/references/tables/ideas.idea_tags.md` | `24a28b7a4bd7edaf743fe01ca6eb707c897c0a088637f2c5f915d5a7c804caa3` |
| `muse-db/tables/ideas.ideas.md` | `/opt/muse/skills/muse_db/references/tables/ideas.ideas.md` | `651238ff502efa82b205a400fbb355255b504e2da777c7076e384d6202aad4c2` |
| `muse-db/tables/ingest.data_source_events.md` | `/opt/muse/skills/muse_db/references/tables/ingest.data_source_events.md` | `c7fbffb1f633efc4bdc85d3c049f01ca7f0a5a80f7975df5558e1e7b659b0cca` |
| `muse-db/tables/media.descriptions.md` | `/opt/muse/skills/muse_db/references/tables/media.descriptions.md` | `9ba7772d7fee81cda6ffd4329034708710f3fcf5044eb9d4b0754133cfe31202` |
| `muse-db/tables/media.exif_values.md` | `/opt/muse/skills/muse_db/references/tables/media.exif_values.md` | `49f7f4ce6a31f551d2423ee5326e7041a55661e0df9d9bb92df596d77faf844a` |
| `muse-db/tables/media.items.md` | `/opt/muse/skills/muse_db/references/tables/media.items.md` | `a4e1b9a8f0e3897d6b54c06645781b3d5b193243ceab85e9266168783e30e0c0` |
| `muse-db/tables/media.locations.md` | `/opt/muse/skills/muse_db/references/tables/media.locations.md` | `bc69ba2c581f45853f57b66b218a098e2ecb6721451bf224a06197764be80333` |
| `muse-db/tables/memory.claims.md` | `/opt/muse/skills/muse_db/references/tables/memory.claims.md` | `eb39f930ba59ecb2dee80444e4c54550dbc1a483deac69dd388dad80e825972c` |
| `muse-db/tables/memory.embedding_models.md` | `/opt/muse/skills/muse_db/references/tables/memory.embedding_models.md` | `107cc5ff523b282ee658cf4c01f31dcd28b055b6895a389ff9c83aeb9574ddb2` |
| `muse-db/tables/memory.embeddings.md` | `/opt/muse/skills/muse_db/references/tables/memory.embeddings.md` | `b4d2ab9d0d1d47b0cd194e5e88713dd20ea82362935a6ea52d60c199560333e1` |
| `muse-db/tables/memory.entries.md` | `/opt/muse/skills/muse_db/references/tables/memory.entries.md` | `7b95fc16557c6765ff483a32d777958d2ca68c483e654f2bb6f55c5c1c2d9c5d` |
| `muse-db/tables/memory.entry_attributes.md` | `/opt/muse/skills/muse_db/references/tables/memory.entry_attributes.md` | `d320b2ffc52d06e4a2c733e3bc69f66b7c9cb85b36c90b9309458245b8f2e31c` |
| `muse-db/tables/memory.metadata.md` | `/opt/muse/skills/muse_db/references/tables/memory.metadata.md` | `be473b52b7655494e8d2661cf21d8226db4699e59331af5b71028bd7ab44688b` |
| `muse-db/tables/podcasts.episodes.md` | `/opt/muse/skills/muse_db/references/tables/podcasts.episodes.md` | `87aca670ac3fc777b04a3ffbf2b9a8de0d29d310e7a8c097f2b0e48d09324b6f` |
| `muse-db/tables/podcasts.feed.md` | `/opt/muse/skills/muse_db/references/tables/podcasts.feed.md` | `ab57317bab7a4e03b208001ad1bc651a84a35d41eee8ae8395877bced845600c` |
| `muse-db/tables/podcasts.feeds.md` | `/opt/muse/skills/muse_db/references/tables/podcasts.feeds.md` | `a6a6b6f05846e3be5f9c25016e6a3afc520024e61eaa7861da740bf9f55e9b38` |
| `muse-db/tables/runtime.agent_todo_snapshots.md` | `/opt/muse/skills/muse_db/references/tables/runtime.agent_todo_snapshots.md` | `36f41e0130e6ddc151d025efee8bbe57b91d658fe4fc249d594b158170a66632` |
| `muse-db/tables/runtime.avatar_state.md` | `/opt/muse/skills/muse_db/references/tables/runtime.avatar_state.md` | `1a1e9bfa5fbfad9ce4545385786a1257a373113c99ed05c1070d4f397be6395b` |
| `muse-db/tables/runtime.browser_tasks.md` | `/opt/muse/skills/muse_db/references/tables/runtime.browser_tasks.md` | `9a63b9f0505e5c7166a165620d1e57d66eb8f4c016ce709e855aee192738357c` |
| `muse-db/tables/runtime.chat_event_derived_write_backlog.md` | `/opt/muse/skills/muse_db/references/tables/runtime.chat_event_derived_write_backlog.md` | `cd379aa442e3f6d7442ca1c83e8a07f82d9b7149c0dd5e2d249386847e2af1f8` |
| `muse-db/tables/runtime.checkout_spend_checkpoints.md` | `/opt/muse/skills/muse_db/references/tables/runtime.checkout_spend_checkpoints.md` | `0c595ecafe7f7f7353f36dafeec06729287bd1bb6de68f103ce5b770e54ddf52` |
| `muse-db/tables/runtime.checkout_spend_operations.md` | `/opt/muse/skills/muse_db/references/tables/runtime.checkout_spend_operations.md` | `160d170a46788c1d38677b4d3a83fc72f8234eff217aeee10e3f03e6a7949eb5` |
| `muse-db/tables/runtime.client_rendering_capabilities.md` | `/opt/muse/skills/muse_db/references/tables/runtime.client_rendering_capabilities.md` | `77c764c301b19dec6bb5c353999ea2d7f75ae1fb2b2abb5cdba5a4f83d033804` |
| `muse-db/tables/runtime.context_snapshots.md` | `/opt/muse/skills/muse_db/references/tables/runtime.context_snapshots.md` | `7f57f579cf52676ca231b77e4302e00e4b3c8ed98693a8822d1ef585955a8e26` |
| `muse-db/tables/runtime.dev_notice_watermark.md` | `/opt/muse/skills/muse_db/references/tables/runtime.dev_notice_watermark.md` | `d89a9e15318e66bae9e04d949849288de053edd642b6eab7d3a57f795dfd8d46` |
| `muse-db/tables/runtime.event_hook_space_owners.md` | `/opt/muse/skills/muse_db/references/tables/runtime.event_hook_space_owners.md` | `c488b15ad0ecd32193ea48caac3b13e6aa4d5a5b8c5573d7243a0423916d6cac` |
| `muse-db/tables/runtime.event_payload_fields.md` | `/opt/muse/skills/muse_db/references/tables/runtime.event_payload_fields.md` | `7148c846b1301535e9c90f1493aa7222381306a401744c9fcf549ba5f980c8c6` |
| `muse-db/tables/runtime.events.md` | `/opt/muse/skills/muse_db/references/tables/runtime.events.md` | `90f5549515892bdfd4220e14e3ea9812f8e72c8e7900e7e97689fde9189afdf9` |
| `muse-db/tables/runtime.execute_resolve_runs.md` | `/opt/muse/skills/muse_db/references/tables/runtime.execute_resolve_runs.md` | `2b2492749d0289539b0450d21f43ee9dc4fc2482def18891c90b11c77394ab37` |
| `muse-db/tables/runtime.idea_execution_pending.md` | `/opt/muse/skills/muse_db/references/tables/runtime.idea_execution_pending.md` | `80ca3d03411f38e0f650fc3b141372566e2b22c3af93b09aecd8915f1062a4ca` |
| `muse-db/tables/runtime.invite_badge_seen_state.md` | `/opt/muse/skills/muse_db/references/tables/runtime.invite_badge_seen_state.md` | `e879408af369b687efe9a579466845fa1613b86fd0d7adfd1b8f74c2d7b24f2b` |
| `muse-db/tables/runtime.maintenance_markers.md` | `/opt/muse/skills/muse_db/references/tables/runtime.maintenance_markers.md` | `ca6ecbe195e24d04e9722236ac52dc42ecfd77eefb5c42b656bc68ee90a4db47` |
| `muse-db/tables/runtime.message_attachments.md` | `/opt/muse/skills/muse_db/references/tables/runtime.message_attachments.md` | `46e170a4695e88745e8362477b644e1dad7a11c1f62cb2393e32442334751e5d` |
| `muse-db/tables/runtime.message_reactions.md` | `/opt/muse/skills/muse_db/references/tables/runtime.message_reactions.md` | `29f1c4851bf7aade59e736f957b195d5582a79c38e47d0831c3c33636946e4e0` |
| `muse-db/tables/runtime.messages.md` | `/opt/muse/skills/muse_db/references/tables/runtime.messages.md` | `2ba487342ce9ab3ed98c49421b032f120dcbade9d318c0fc4261b1d558ec596c` |
| `muse-db/tables/runtime.product_improvements_preference.md` | `/opt/muse/skills/muse_db/references/tables/runtime.product_improvements_preference.md` | `6a89a8666bc67c649fc361ab3b4a77742f9a0535a6440d413fba66669934a2b2` |
| `muse-db/tables/runtime.raw_signal_collections.md` | `/opt/muse/skills/muse_db/references/tables/runtime.raw_signal_collections.md` | `bd9d7afcb9b10bc4099e40d71e0a370ee3335293aca8aceabe733d4f57fde239` |
| `muse-db/tables/runtime.raw_signal_entries.md` | `/opt/muse/skills/muse_db/references/tables/runtime.raw_signal_entries.md` | `b50bf6eb4621e0f6410274aee754bb9755fdf401cac5ae3043d2dcb8ad83d787` |
| `muse-db/tables/runtime.requests.md` | `/opt/muse/skills/muse_db/references/tables/runtime.requests.md` | `3a4fb87b93292bea05ace89532dea9957bcb01c3f738e8432dcf0ade4958c766` |
| `muse-db/tables/runtime.resources.md` | `/opt/muse/skills/muse_db/references/tables/runtime.resources.md` | `4ec27dfcd1281a638f015825b2461511442c3a2feb6975f7464c6b6994d9523a` |
| `muse-db/tables/runtime.search_documents.md` | `/opt/muse/skills/muse_db/references/tables/runtime.search_documents.md` | `ca6557ba90132210d4bdbeb873bbcef0148642436d3d3f722401b993dd371272` |
| `muse-db/tables/runtime.skill_invalidation_state.md` | `/opt/muse/skills/muse_db/references/tables/runtime.skill_invalidation_state.md` | `cece563b29ec7b606187fe36768fd7aae8b26d892a8db79916a8a43abc4294d2` |
| `muse-db/tables/runtime.stripe_link_spend_requests.md` | `/opt/muse/skills/muse_db/references/tables/runtime.stripe_link_spend_requests.md` | `ab545836ddd4509e29c7763dd92a61605b51215854d01c0eddb6c754984823e6` |
| `muse-db/tables/runtime.summaries.md` | `/opt/muse/skills/muse_db/references/tables/runtime.summaries.md` | `07b770fdba2e86fc9737463bcf498ee1d13e4642ec888ffefaf180341ad5cbb7` |
| `muse-db/tables/runtime.tool_calls.md` | `/opt/muse/skills/muse_db/references/tables/runtime.tool_calls.md` | `d2626036b40133725d93c1c8899836f8ef1e14150a6dd619d62865f9fe20b6ff` |
| `muse-db/tables/runtime.tool_outputs.md` | `/opt/muse/skills/muse_db/references/tables/runtime.tool_outputs.md` | `e62e1702fef6221185d47d919f9f3cc6a1259fe2d5200e299ca4dded36c289a2` |
| `muse-db/tables/runtime.widgets.md` | `/opt/muse/skills/muse_db/references/tables/runtime.widgets.md` | `7d70cbd5a2c2c7caa9a075a384afcea7c4f4e31fa45cea72e84950ede140b5ac` |
| `muse-db/tables/runtime.work_items.md` | `/opt/muse/skills/muse_db/references/tables/runtime.work_items.md` | `7806869345c6f3ff364ec4947b6c70beaa117aed6aac1122eb679bd7a4ac56c2` |
| `muse-db/tables/runtime.workflow_agent_calls.md` | `/opt/muse/skills/muse_db/references/tables/runtime.workflow_agent_calls.md` | `c29e0903f0c259512c6a229ad6d3cd15e6443ed07f60d0148ebbd05d6183227d` |
| `muse-db/tables/runtime.workflow_launch_occurrence_aliases.md` | `/opt/muse/skills/muse_db/references/tables/runtime.workflow_launch_occurrence_aliases.md` | `078a367cb299c24ac100567cc336cdbbe171a19fb95d08ee86449d4e55f17a48` |
| `muse-db/tables/runtime.workflow_legacy_launch_occurrence_blocks.md` | `/opt/muse/skills/muse_db/references/tables/runtime.workflow_legacy_launch_occurrence_blocks.md` | `8b01a5c0b720bb9e0324fa25531550a5e6cfefc45e749698e21ded2243c48e07` |
| `muse-db/tables/runtime.workflow_phase_runs.md` | `/opt/muse/skills/muse_db/references/tables/runtime.workflow_phase_runs.md` | `b23a86a1a61b58fd78213a90ead9bde903f863f5f3142ea80b1990ab61836f4b` |
| `muse-db/tables/runtime.workflow_runs.md` | `/opt/muse/skills/muse_db/references/tables/runtime.workflow_runs.md` | `a14e15d650591678a0c0fdae4bbd4113f62e4cababa880999662f560acb1693f` |
| `muse-db/tables/runtime.writer_epoch.md` | `/opt/muse/skills/muse_db/references/tables/runtime.writer_epoch.md` | `7d5d4030fd439f8c763e8d7b4ba9d3cb17f1263ef158391924811e4099db59e7` |
| `muse-db/tables/saved.item_links.md` | `/opt/muse/skills/muse_db/references/tables/saved.item_links.md` | `448061a7bed8e1c8bd22b007997ece2116630049c31a8f319d03e68607cd143e` |
| `muse-db/tables/saved.items.md` | `/opt/muse/skills/muse_db/references/tables/saved.items.md` | `21bd898d3a5792b6b9d22369caf5e50ce98f65b96fa8e8083bd73421a984e439` |
| `muse-db/tables/saved.lists.md` | `/opt/muse/skills/muse_db/references/tables/saved.lists.md` | `d7f7b6d2ecbb497b33dc86fa919df687ac252148491f97f503ee611aa0917f1b` |
| `muse-db/tables/scheduler.cron_mutations.md` | `/opt/muse/skills/muse_db/references/tables/scheduler.cron_mutations.md` | `202e3c9f69b03a7e75cd5943e217fc423063eb909058977349ca26ae31e2977e` |
| `muse-db/tables/scheduler.delivery_outbox.md` | `/opt/muse/skills/muse_db/references/tables/scheduler.delivery_outbox.md` | `aa5b585ae2fdbd4e9fca2b4582204a1ada9c1b719115e29baea4c13e6c53f59c` |
| `muse-db/tables/scheduler.doctor_run_plans.md` | `/opt/muse/skills/muse_db/references/tables/scheduler.doctor_run_plans.md` | `050b9673f482228b3d0bbf9fe9525c130e5c1fcf4caed82cdf691fabe5bcf9b1` |
| `muse-db/tables/scheduler.doctor_task_state.md` | `/opt/muse/skills/muse_db/references/tables/scheduler.doctor_task_state.md` | `6f531833071594a4547582f1d9c4a63dc8f5351255811ca95503ea9f4915433d` |
| `muse-db/tables/scheduler.events.md` | `/opt/muse/skills/muse_db/references/tables/scheduler.events.md` | `b3b97d2147cc59df573cb96390031042c83b121fc6202a6f26eaea9c61b6f1b9` |
| `muse-db/tables/scheduler.job_definitions.md` | `/opt/muse/skills/muse_db/references/tables/scheduler.job_definitions.md` | `c77015ef526b56de89ab38b8c3072b38f44915b796106a7aba0278953d3bb65b` |
| `muse-db/tables/scheduler.job_idea_scope.md` | `/opt/muse/skills/muse_db/references/tables/scheduler.job_idea_scope.md` | `45d69085e884c3541c886e22db8b4e9d3d7a84c7e834a9aa54ac3702216bfb0e` |
| `muse-db/tables/scheduler.job_runs.md` | `/opt/muse/skills/muse_db/references/tables/scheduler.job_runs.md` | `43a1def2e28feb925335aa1321b22df4c631e9e0ff57dbf7466fc0f76033ea63` |
| `muse-db/tables/scheduler.jobs.md` | `/opt/muse/skills/muse_db/references/tables/scheduler.jobs.md` | `476a45b14ea53a204e7b3dcf7cc16d17a774dee3d215989fb59799bfce22aac1` |
| `muse-db/tables/scheduler.scheduled_resume_registrations.md` | `/opt/muse/skills/muse_db/references/tables/scheduler.scheduled_resume_registrations.md` | `dffbd24e2fa21d68f368c2b7ef2d1395287d92ca10d6cf524aee0df711e4c7fc` |
| `muse-db/tables/scheduler.scheduled_resume_state.md` | `/opt/muse/skills/muse_db/references/tables/scheduler.scheduled_resume_state.md` | `edb0d70ba8390eae42a1c22edbcf72c7f33e9b2721abfebf77accb6d5bf8185d` |
| `muse-db/tables/scheduler.terminal_signals.md` | `/opt/muse/skills/muse_db/references/tables/scheduler.terminal_signals.md` | `c1158a825dfeef057d24e4cc0774009e433307e7a90650464c34b9960c3c5fa4` |
| `muse-db/tables/self_improvement.backfill_day_runs.md` | `/opt/muse/skills/muse_db/references/tables/self_improvement.backfill_day_runs.md` | `a93ef896a377dbb692433b6a15044e94af97b87d8f49ea86f2b7d0bbaf32b85e` |
| `muse-db/tables/self_improvement.calculation_records.md` | `/opt/muse/skills/muse_db/references/tables/self_improvement.calculation_records.md` | `a2751cc7cd9e89ec0883a3e91cea8df0be0ea7be6cdeae2f6a6f9979ec2b5e39` |
| `muse-db/tables/self_improvement.calibration_records.md` | `/opt/muse/skills/muse_db/references/tables/self_improvement.calibration_records.md` | `ce923303337e2a5bc14bd70cb6b68008244a689682a559b8ca3997aca80d6692` |
| `muse-db/tables/self_improvement.connector_read_audit.md` | `/opt/muse/skills/muse_db/references/tables/self_improvement.connector_read_audit.md` | `b127e8df003eee8e70ae110fe80db644ab7926abf66155532e265194a1054bdd` |
| `muse-db/tables/self_improvement.conversation_follow_up_attempts.md` | `/opt/muse/skills/muse_db/references/tables/self_improvement.conversation_follow_up_attempts.md` | `cc2e84f14a58ebdc0b3c66d9b8d25b4ada9b16c0c2bc9f31db5f284e7dc0db04` |
| `muse-db/tables/self_improvement.handoff_dedupe.md` | `/opt/muse/skills/muse_db/references/tables/self_improvement.handoff_dedupe.md` | `6b0811594c105afc9f325e73df9b7c41e57fe39aa1ee1c70d1f76775d4fd14ed` |
| `muse-db/tables/self_improvement.learning_adoption_events.md` | `/opt/muse/skills/muse_db/references/tables/self_improvement.learning_adoption_events.md` | `9bfaae8cb6b183925097201a5568faa621dd3b8a2325e344941c8041d087349d` |
| `muse-db/tables/self_improvement.leases.md` | `/opt/muse/skills/muse_db/references/tables/self_improvement.leases.md` | `73c86a261ac3a86e517cf0feb8323a5b06158a51ba817fa0e93acc178f2134a1` |
| `muse-db/tables/self_improvement.objective_markers.md` | `/opt/muse/skills/muse_db/references/tables/self_improvement.objective_markers.md` | `538932f10e129d96612345cbc60cc6e8983b87b160bfbf5d541978f209f17e31` |
| `muse-db/tables/self_improvement.objective_state.md` | `/opt/muse/skills/muse_db/references/tables/self_improvement.objective_state.md` | `8adb098882e3ecd198bb2b3b17880cf20e40fc0bb2e5233431b48c5d645649c1` |
| `muse-db/tables/self_improvement.proactivity_changes.md` | `/opt/muse/skills/muse_db/references/tables/self_improvement.proactivity_changes.md` | `065d042a67ae30bb16b2a71952983b8c35955422558e3171b07987db05811789` |
| `muse-db/tables/self_improvement.relationship_briefs.md` | `/opt/muse/skills/muse_db/references/tables/self_improvement.relationship_briefs.md` | `90aa9a46cc0ccb5b7d4bc7feca4c771db22d9393d451262c6a3f2e8f4a3d5795` |
| `muse-db/tables/self_improvement.runs.md` | `/opt/muse/skills/muse_db/references/tables/self_improvement.runs.md` | `8d38a556c010c7fc987aae66c6af537a65193b47dc5bc476fb4ec37431263ba2` |
| `muse-db/tables/shell.user_state.md` | `/opt/muse/skills/muse_db/references/tables/shell.user_state.md` | `729ef007ee39024a618f5c6212319ecced86626e7f30c45b75597dc7e5753ef4` |
| `muse-db/tables/spaces.action_arguments.md` | `/opt/muse/skills/muse_db/references/tables/spaces.action_arguments.md` | `bdbf13d5ff9dd19fa18c9b7d14880212a0985758a8703e18114ef952ae197f93` |
| `muse-db/tables/spaces.action_invocations.md` | `/opt/muse/skills/muse_db/references/tables/spaces.action_invocations.md` | `ab4a3e577251a9d1ea25d15a4f5b01a88b9e055b064f14c589a82d96042b5a82` |
| `muse-db/tables/spaces.action_results.md` | `/opt/muse/skills/muse_db/references/tables/spaces.action_results.md` | `e23683d124728954ad94195a8f039ff61cb0b208f9726a9fa47c7ddb744448d4` |
| `muse-db/tables/spaces.backfill_markers.md` | `/opt/muse/skills/muse_db/references/tables/spaces.backfill_markers.md` | `d973d521d973f2ca630d309fcf9044eaaaab57e590c9b9ea7246808b7fff6444` |
| `muse-db/tables/spaces.file_artifact_identities.md` | `/opt/muse/skills/muse_db/references/tables/spaces.file_artifact_identities.md` | `d8effde740ebf8c0d6024f41a47eefdffc3578f99700a3c5ac92f54f8a36c661` |
| `muse-db/tables/spaces.proposals.md` | `/opt/muse/skills/muse_db/references/tables/spaces.proposals.md` | `3c5018ec4460977ce118d69eee78b5c2a2ad3c35683b660fe062773da9feaa0b` |
| `muse-db/tables/spaces.shares.md` | `/opt/muse/skills/muse_db/references/tables/spaces.shares.md` | `7d754ad8056d5ecf0eec71e8e7ba2156c3972e360f86f8ca1d0f1d9b016df8b6` |
| `muse-db/tables/spaces.spaces.md` | `/opt/muse/skills/muse_db/references/tables/spaces.spaces.md` | `08b76c74655b50b19c3d204e4c73f7f2d0b769f0611b75aded8209db47850c25` |
| `muse-db/tables/spaces.user_state.md` | `/opt/muse/skills/muse_db/references/tables/spaces.user_state.md` | `b3d4f0589eb0834ace402697c5c23820e886c7b10db14900ef68537fdd5089b0` |
| `notes/architecture-notes.md` | `~/workspace/your_files/personal-agent-architecture/architecture-notes.md` | `3eb7119f25f29ab02b523d46fa660a2acd1b641b7318cc75d444bcc29b2b5b7f` |
| `notes/tool-schemas.md` | `~/workspace/your_files/personal-agent-architecture/tool-schemas.md` | `3890aacc1974119a524ff9bed4ff820264fb1f3d5c837265ff9cfc05f09f6b14` |
| `prompt/system_prompt.md` | `~/workspace/system/system_prompt.md` | `d383ea401c01a4115be03844b0f37ff29e4281e25fdbb38986e9df2172922308` |
| `schemas/ads.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `665254a38318d0e6704b86426d400e6ee2449779802945331cfa333883bb8e09` |
| `schemas/artifact.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `706c4c63464ca84b174b8ac2b650369bab5ea8de6a569461b518ce106a22df2c` |
| `schemas/avatar.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `f9a79bbb5638b4c4d03afe34d83f3845ee139a375601a05c6f2ecf0116c9161c` |
| `schemas/browser.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `7b2f5ad514a97c98b88f53614191d3c66c6f970dfbbbe3ef8a3714ef8b392e44` |
| `schemas/chat.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `21dc64eb946cdad1a0d9fcc3ce5dedff36ed11d0173e8a961f121a79777d8c7e` |
| `schemas/credentials.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `9d4c09427eae1b30001b9d8915ebddb49012875e5fa421841f2feef09a636ff9` |
| `schemas/cron.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `27240dac0f127a2a94a64a9f194851e691e012e934dd65e9982255cc8e952038` |
| `schemas/device.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `8280e807b1f88c748ff1581e24ec1bd587b61d5fd03b8c6e4c55e0692b4d64f9` |
| `schemas/feed.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `995479d87a8eaa107f7f3eb849c158845c74650bf0849fad5dcb6a835ea84bcf` |
| `schemas/forget.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `062d31ec0b4e6748925c11e1020bcb4f1ee7a0a933be0151b7acfed80062638b` |
| `schemas/hooks.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `e3ae64c9fab7a8d02024f5679d662aa295cd577b2eba1047aa79d852c43144e6` |
| `schemas/idea.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `a87d6734cfe41f04d5ae315ffbbcc64fafc7228f3300915b38015288ffe52c43` |
| `schemas/map.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `b36b71df1b3569088091c12a48bd8f43b1cc357c3b5215cead5fc309541b2c5e` |
| `schemas/media.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `f4f28b6042ea6fab3a4e0d54fa84cd7b5fd778834e71e7a0f792fe40b4f84b2e` |
| `schemas/muse.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `3c30878ae92634aedcd62cb0d5cca24a543644474708c0e42d639f86cffe00bc` |
| `schemas/onboarding.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `f00ebe85c32f1010315ec7ee7ee527a47c7d2a753182447015e60f8a28f426e5` |
| `schemas/permissions.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `2ae43a3324dab8e25ab489d63990b1bdb077e18008d6576b3b624e7f0f1bb247` |
| `schemas/proactivity.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `4f4b53726cbd0e119e6096dc6a5a77fbc92553520e8db4051e2ddff26afa8fd5` |
| `schemas/process.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `bdd19c944d18edee37b985ff07608402eff22cf1207c50400f0aedc1b7bd97fb` |
| `schemas/shopping.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `836a21cd588e8dbbbbde3f362b1a637f0e64895ac860a9d2f4b0cd8caeb61faf` |
| `schemas/social.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `544786e7d1abb81f2ca156e6730b1efa50b4f6d559e59721489e5b0159a49a31` |
| `schemas/subagent.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `c99ea16f162caf0cb067adbb20fded4b3a6c0f1b463bd414ade20b76e30e9837` |
| `schemas/todo.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `d21e4effe27f335c317bcc79971855ed109f488c2df11f673e114653d9e50590` |
| `schemas/tool_search.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `ba29b3e27d0566c1883faf7147c7b57b7e3795630141c9018778af392698056f` |
| `schemas/tracking.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `4f06684617e429b2d246ac54a9ccd9b43007e58bfb61d0747de47b61dd0661cc` |
| `schemas/trash.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `7bd7d617ec56b28397ea62a25dc1ebc329b24368a494c2f381df9c4033a389e0` |
| `schemas/travel.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `0f2c65f44d88ffd953e879691db9d1f30dacb88e4b45c72f67481541fddcaace` |
| `schemas/ui.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `719b4f2358cb46085750bc4ea5f941a18bca0ec6e439e05b11fac03ac26b4b50` |
| `schemas/user_goal.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `bcfb585e2215641e376b16290f900095d1d5d47568efe168364328c7fd7134f5` |
| `schemas/wallet.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `2e7309bb80bd15211ccd9f4abac59001d8e72728b98fc268a1289a0864659edb` |
| `schemas/widget.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `fab55f5f144161b15fc53647bbe35a74e24270d466266ed47514a7d7a56f896f` |
| `schemas/worker.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `fa7ee5f15cd4ceec972fbbf8716efc4c7a6013533b5580b6e30ac70586ad33db` |
| `schemas/workflow.json` | `In-session tool definitions (namespace load or session prompt; see per-file transcription_note)` | `54a9575b8cb4b5d5feb865f2747087b00572284b770358d9239a7e54daf87a85` |

## Exact gaps (what this export does NOT contain or prove)

1. **Server-side internals are vendor self-report only.** Model hosting, the scheduler,
   handoff transport, push delivery, and the message index were never measured; the
   architecture notes label these [Prompt-described] or [Inference].
2. **No runtime version stamp exists** in any definition or doc read, so schemas cannot
   be pinned to a release. Tool catalogs are session-scoped and may differ by client.
3. **Summarized prose.** Several schema files summarize long prose descriptions
   (browser, cron, social, widget, workflow, chat, device, hooks); each such file flags
   this in `transcription_note`. Parameter names/types/required fields are exact.
4. **Typed-as-unspecified.** In `artifact.json`, `artifact.create_file` / `artifact.edit`
   `slide_count_target` had no type in the source definition and is typed `"unspecified"`.
5. **Functions named but not exposed.** `idea.share` and `widget.create_image_picker_widget`
   appear in namespace descriptions but were not returned by the namespace loads in this
   session; both are recorded in their files' `missing` arrays, not invented.
6. **No wire captures.** Example payloads in `notes/architecture-notes.md` are
   reconstructions of field shapes, not captured network payloads.
7. **Prompt snapshot is a startup snapshot** (`~/workspace/system/system_prompt.md`,
   72,867 bytes, Oct 24, 21:40), not the live session prompt with injected context.
8. **Docs with no dedicated file.** Subagent/worker/workflow behavior is documented
   through tool schemas and the architecture notes; no standalone runtime doc for those
   topics was found under `~/docs/`. Permissions/sandbox/storage wording lives in
   `privacy-and-credentials.md`, `data-handling.md`, `files-and-library.md`, and
   `client-surfaces.md` (all included).
9. **Connector CLIs are docs, not binaries.** `connectors/` holds `CONNECTOR.md` plus
   `connector.yaml`/`manifest.yaml` per connector; the executable CLIs under
   `/opt/hatch/bin/` were not copied (they are runtime-owned and replaced on deploy).
10. **Tool discovery configs.** `inventory/skills.yaml` is the user's skill config;
    no other tool-discovery config file was found in the inspected locations.
