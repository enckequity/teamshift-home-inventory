# TeamShift presentation adaptation

Tracker: teamshift-monorepo#8092, parent#8085. Baseline462751a retains fork PR4 and the upstream Homebox components. Production currently runs earlier source dc8a314; this document does not claim a deployment.

The shared presentation adapts the Mobbin study's quieter navigation, card hierarchy and typography to TeamShift. Default-theme colors use TeamShift's warm canvas, slate ink and sky accent. User-selected upstream themes retain their palettes. Figtree and Gabarito are self-hosted copies from TeamShift's design system at monorepo4e328b040. Their notices and full SIL Open Font License texts ship beside them. The sign-in root has a presentation class for its quieter default-theme header. No vendor component, permission boundary, login/session store, household/collection selector, scanner, form handler or API path changes.

The shared styles cover the existing layout and every route listed below. This is source coverage, not a claim that every nested signed-in interaction has browser acceptance. Wrappers and redirects remain distinct in the inventory. Camera permissions, physical scanning/print, attachments, collection membership and actual household isolation need their existing installed/runtime acceptance. Local fixture screenshots only establish the exercised presentations.

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

