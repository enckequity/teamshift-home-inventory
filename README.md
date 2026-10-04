# TeamShift Home Inventory

TeamShift-branded shared home inventory and QR labels, based on the maintained open-source engine.

Upstream baseline: `b31d6d41326fce44b7fce1c3e424b1d1714e8c4a` from sysadminsmedia/homebox. This baseline includes collection-owner enforcement and tenant-scoped entities; deployment-specific isolation must still be tested.

The fork changes presentation (titles, logo, icons, translated application name and printed label defaults) while retaining native inventory, QR, import/export and authentication contracts. Technical identifiers and the upstream license remain intact. See [source provenance](TEAMSHIFT-SOURCE.md) and [upstream documentation](UPSTREAM-README.md).

This component is under local acceptance testing; it is not deployed in canonical TeamShift production. The canonical worker workflow belongs in enckequity/teamshift-monorepo/services/fleet. Do not expose the app or import private inventories without the intended authenticated household access boundary.

Licensed under the retained [AGPL-3.0 license](LICENSE). Source for this modified version is available from this repository.

## Verification

Run `node --experimental-strip-types teamshift/test-branding.mjs` for presentation checks. Build the official Dockerfile, start a disposable database on `127.0.0.1:8770`, and run `python3 teamshift/test-http.py` for two-household access, member permissions and repeat-import acceptance. The HTTP fixture creates synthetic accounts and data; never point it at a live household database.
