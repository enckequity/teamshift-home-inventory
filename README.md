# TeamShift Home Inventory

TeamShift-branded shared home inventory and QR labels, based on the maintained open-source engine.

Upstream baseline: `b31d6d41326fce44b7fce1c3e424b1d1714e8c4a` from sysadminsmedia/homebox. This baseline includes collection-owner enforcement and tenant-scoped entities; deployment-specific isolation must still be tested.

The fork changes presentation (titles, logo, icons, translated application name and printed label defaults). Printed labels for existing items use their immutable item URL; blank labels retain native asset lookup. Native inventory, QR, import/export and authentication contracts remain intact. Technical identifiers and the upstream license remain intact. See [source provenance](TEAMSHIFT-SOURCE.md) and [upstream documentation](UPSTREAM-README.md).

The initial authenticated household runtime is released through the opt-in canonical TeamShift deployment overlay (monorepo PRs5107/5109). Its pinned image passed disposable isolation/import/QR acceptance and actual browser login with QR deep-link resume for both authorized household identities. Native logins remain separate from TeamShift Supabase login; automatic customer onboarding is not certified. The canonical worker workflow belongs in enckequity/teamshift-monorepo/services/fleet. Do not expose the app or import private inventories without the intended authenticated household access boundary.

Licensed under the retained [AGPL-3.0 license](LICENSE). Source for this modified version is available from this repository.

## Verification

Run `node --experimental-strip-types teamshift/test-branding.mjs` for presentation checks and `node --experimental-strip-types teamshift/test-labels.mjs` for stable label destinations. Build the official Dockerfile, start a disposable database on `127.0.0.1:8770`, and run `uv run --with-requirements teamshift/test-requirements.txt --python 3.12 teamshift/test-http.py` for two-household access, member permissions and repeat-import updates with retained item IDs and native QR decoding. The HTTP fixture creates synthetic accounts and data; never point it at a live household database.
