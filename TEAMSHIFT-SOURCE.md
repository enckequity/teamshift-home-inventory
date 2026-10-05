# Source and upgrade record

Modified by TeamShift on 2026-10-04: presentation branding, the native QR icon, immutable item URLs for existing-item labels, a build-worker-compatible compile instruction and local acceptance checks. Upstream copyright and AGPL notices are retained.

Upstream: https://github.com/sysadminsmedia/homebox
Baseline: b31d6d41326fce44b7fce1c3e424b1d1714e8c4a
TeamShift fork: https://github.com/enckequity/teamshift-home-inventory

Keep the upstream remote and periodically compare supported releases against the baseline. Rebase or merge upstream into an isolated branch, resolve only TeamShift branding and label patches, and rerun frontend build, branding and HTTP household-isolation acceptance before release. Do not carry compiled hashed-chunk substitutions.

Original copyright/license notices and third-party licenses are retained. Network deployments of this modified AGPL application must make its corresponding source available; the visible Source link points to this fork. Do not remove notices or imply TeamShift authored upstream code. Canonical TeamShift icon assets were copied from apps/web/public in enckequity/teamshift-monorepo.

Modified on 2026-10-05: authenticated TeamShift wordmark and logo background; footer links to the displayed build's fork commit; upstream help is identified as upstream; upstream social channels and the upstream-only upgrade banner are removed from the customer shell. Technical identifiers, AGPL notices, authentication, data and QR contracts remain unchanged. The backend upstream release checker remains intact; operators may disable it with HBOX_OPTIONS_GITHUB_RELEASE_CHECK=false.
