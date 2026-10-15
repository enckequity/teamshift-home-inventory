# Direct Mobbin foundation

This is the direct-layout follow-up under `teamshift-monorepo#8092`, separate from the release preparation owned by the parent task. Branch `codex/inventory-direct-mobbin-8092` starts at canonical fork merge `1e18c484d4bf74d0afcb2056e72fac51c39c744a`. Owner: `/root/account_final_review`, `codex-account-final-review@DAKOTAENCK`. The existing `codex-teamshift-home-inventory-8092` release worktree is outside this task.

The first adaptation retained the upstream permanent sidebar and warm palette. This revision uses the cloned Mobbin product shell as the visual foundation: a 72px minimum header, 48px search, horizontal underline navigation, white canvas, `#141414` text, `#efefef` inset surfaces, 32px desktop spacing, 24px card corners and pill controls. The measured source is `src/components/sites/mobbin/product-library/product-shell.tsx` and its CSS in `C:/Users/dakot/worktrees/codex-mobbin-exact-refinement`, inspected at `d906d9d12991e9b49a74821dfd434d177fc6b209`. Home Inventory retains its own brand, self-hosted licensed fonts, translations, content and actions.

The work covers the existing layout, shared cards and page containers. Default desktop navigation becomes horizontal. The upstream sidebar becomes an initially closed drawer that still opens through its existing trigger and keyboard shortcut. Mobile retains the upstream modal drawer, and the legacy preference retains the sidebar layout. The collection picker, create menu and search move into the header. Compact layouts show their existing icons and accessible names. Search, collection selection, creation, scanner, sign-out, route guards, uploads, edits, data tables, permissions and household boundaries keep their existing implementations. The existing VueUse resize observer measures header height for the item edit toolbar's existing offset variables. Source catalog data, clone account simulations and third-party runtime bundles are excluded.

Acceptance covers 320/390/768/769/1440 widths, enlarged text, alternate palette, header/search/navigation, collection menu, create dialog/drawer focus and scroll, item editing/upload affordances and original route coverage. Local synthetic fixtures do not prove live household isolation, camera/print or production writes. Heavy Windows checks wait for the shared runtime slot. Required release checks still include the official candidate image and disposable two-household HTTP suite. The existing private backup belongs to the parent task and is untouched.

## Resources

- Worktree: `C:/Users/dakot/worktrees/codex-inventory-direct-mobbin-8092`, branch `codex/inventory-direct-mobbin-8092`, created 2026-10-15 UTC. Active until reviewed and integrated, then remove with normal `git worktree remove` after checking status and processes.
- Scope lease: `enckequity-teamshift-home-inventory-direct-8092`, owner `codex-account-final-review@DAKOTAENCK`, expires `2026-10-15T04:41:15.382Z`. Release after integration or accepted handoff.
- Evidence: `C:/Users/dakot/artifacts/mobbin-exact-20261014/inventory-direct-8092`, retained for review and release provenance. Process and tab identities will be recorded before runtime checks.

No build, server or browser has been started for this revision. Verification is pending.
