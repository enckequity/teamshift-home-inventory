# TeamShift presentation adaptation

Tracker: teamshift-monorepo#8092, parent#8085. Baseline462751a retains fork PR4 and the upstream Homebox components. Production currently runs earlier source dc8a314; this document does not claim a deployment.

The shared presentation adapts the Mobbin study's quieter navigation, card hierarchy and typography to TeamShift. Default-theme colors use TeamShift's warm canvas, slate ink and sky accent. User-selected upstream themes retain their palettes. Default-theme links use a darker blue for readable contrast on the warm canvas and selected rows. Figtree and Gabarito are self-hosted copies from TeamShift's design system at monorepo4e328b040. Their notices and full SIL Open Font License texts ship beside them. The sign-in root has a presentation class for its quieter default-theme header. No vendor component, permission boundary, login/session store, household/collection selector, scanner, form handler or API path changes.

The shared styles cover the existing layout and every route listed below. This is source coverage, not a claim that every nested signed-in interaction has browser acceptance. Wrappers and redirects remain distinct in the inventory. Camera permissions, physical scanning/print, attachments, collection membership and actual household isolation need their existing installed/runtime acceptance. Local fixture screenshots only establish the exercised presentations.

## Verification

Shipping presentation code: `91719d6`. The frozen pnpm 10.28.0 install and Nuxt production generate passed on the isolated Mac worktree. The lockfile SHA256 remained `a6aca891bf539f6dc1e73962396874eece61161e57b4891a07ca833c544dbf86`. Branding/source-link and immutable-label checks passed. Fork PR4 remains an ancestor.

Typecheck reports 191 diagnostics. The exact base `462751a3` produces the same 191 diagnostic lines, including the Ref/ComputedRef errors in unchanged upstream files. This patch adds no typecheck diagnostic.

A local Chromium fixture visited all 32 route source entries at 1440px desktop and 390px phone widths, recording 64 attempts with no page errors or horizontal overflow at `84b43f5`. Wrappers and redirects are recorded by their resolved URLs. After the final text-reflow adjustments, 30 focused attempts at `91719d6` repeated login, home, profile, search, collection settings and item detail at normal desktop/phone, 200% text desktop/phone and the upstream black theme. Those checks also had no page errors or horizontal overflow. The collapsed desktop rail remains 56px with 40px header/footer controls, scaling to 112px/80px at 200% text. The Create Tag dialog/drawer opened and closed in all five variants without submitting. Its enlarged phone body requires the existing internal scroll area; footer reachability was not separately exercised.

Every API read used synthetic data or an explicit local unavailable response. Non-GET requests were intercepted, including automatic preference PUTs. No backend or customer writes occurred. The first full-matrix wrapper returned exit1 because it treated those blocked preference writes as failures; its page-error and overflow results remain clear. The final focused harness allows only that known intercepted preference path and passed. The source, result JSON and screenshots are retained under `C:/Users/dakot/artifacts/mobbin-exact-20261014/inventory-browser/` and `inventory-browser-final/`, with Mac receipts under `/Users/dakotaenck/agent/evidence/home-inventory-mobbin-8092`.

These checks establish local presentation, not household isolation or production workflow acceptance. Existing production release requirements still include the SQLite/attachment backup and disposable two-household restore checks described in the monorepo customer-completion QA report. Nothing was deployed by this patch.
## Route sources
- `frontend/pages/forgot-password.vue`
- `frontend/pages/index.vue`
- `frontend/pages/items.vue`
- `frontend/pages/locations.vue`
- `frontend/pages/maintenance.vue`
- `frontend/pages/no-collections.vue`
- `frontend/pages/profile.vue`
- `frontend/pages/reset-password.vue`
- `frontend/pages/scanner-ar.vue`
- `frontend/pages/search.vue`
- `frontend/pages/tags.vue`
- `frontend/pages/templates.vue`
- `frontend/pages/a/[id].vue`
- `frontend/pages/assets/[id].vue`
- `frontend/pages/collection/index.vue`
- `frontend/pages/collection/index/entity-types.vue`
- `frontend/pages/collection/index/invites.vue`
- `frontend/pages/collection/index/members.vue`
- `frontend/pages/collection/index/notifiers.vue`
- `frontend/pages/collection/index/settings.vue`
- `frontend/pages/collection/index/tools.vue`
- `frontend/pages/home/index.vue`
- `frontend/pages/item/[id]/index.vue`
- `frontend/pages/item/[id]/index/edit.vue`
- `frontend/pages/item/[id]/index/maintenance.vue`
- `frontend/pages/label/[id].vue`
- `frontend/pages/location/[id]/index.vue`
- `frontend/pages/location/[id]/index/edit.vue`
- `frontend/pages/location/[id]/index/index.vue`
- `frontend/pages/reports/label-generator.vue`
- `frontend/pages/tag/[id].vue`
- `frontend/pages/template/[id].vue`

