---
source_url: https://vercel.com/blog/vercel-flags-platform-native-feature-flags
source_type: blog-post
title: "Vercel Flags: Platform-native feature flags"
author: Malavika Tadeusz, Dominik Ferber (Vercel)
date_published: 2026-06-22
date_extracted: 2026-07-22
last_checked: 2026-07-22
status: current
confidence_overall: emerging
issue: "#2137"
---

# Vercel Flags: Platform-native feature flags

> Vercel's product announcement for Vercel Flags — server-side-evaluated,
> framework-native feature flags with an open-source Flags SDK, automatic
> flag registration/unreferenced-flag detection, a "Precompute" pattern for
> keeping flagged pages static, and an agent-native `vercel flags` CLI —
> framed around Vercel's own year-plus internal dogfooding, most concretely
> v0's staged 5/10/25/50%-over-six-hours rollout process and a production
> database migration executed as a flag flip.

## Source Context

- **Type**: blog-post (official Vercel Blog, `vercel.com/blog`, published
  June 22, 2026; product-announcement/how-it-works post, two named authors,
  auto-discovered from Vercel's trusted Atom feed). The post links out to
  the Vercel Flags documentation, a "Precompute" docs page, a GA changelog
  entry (`/changelog/vercel-flags-ga`), and a Flags SDK "skill" for coding
  agents — none of these linked pages were fetched for this note; per
  MINER.md §1 they are peripheral (docs cross-links and a changelog stub)
  rather than substantive companion posts the way, e.g., the Vercel Connect
  companion post was for `blog-vercel-enterprise-apps-and-agents.md`, and
  the announcement post itself is self-contained enough to extract in full
  without them.
- **Author credibility**: First-party Vercel product announcement authored
  by two named individuals (Malavika Tadeusz, Dominik Ferber). Vercel
  operates the platform and product being described, so feature mechanics,
  GA timing, and the internal v0 dogfooding narrative are first-party
  vendor description — not independently verified by a third party. No
  named customer (outside Vercel's own v0 team) or independent audit is
  cited.
- **Scope**: Covers what Vercel Flags is (targeting rules, progressive
  rollouts, kill switches), the Flags SDK's server-side evaluation model,
  automatic flag registration/dashboard sync, the Precompute pattern for
  static pages, the `vercel flags` CLI for agents, the Flags Explorer
  browser-override tool, and Vercel's own internal usage (the v0 team's
  hundreds of flags, a staged rollout process, AI model-routing flags, and
  a database-migration cutover). Does NOT cover: pricing (the post only
  says "Vercel Flags is available on every plan," no dollar figures);
  targeting-rule syntax or dashboard UI details beyond one screenshot
  caption; competitive comparison to LaunchDarkly, GrowthBook, Statsig, or
  other third-party flag providers by name; or any customer other than
  Vercel's own v0 product.

## Extracted Claims

### Claim 1: The Flags SDK evaluates flags server-side, so React Server Components can read a flag with `await` during render and the browser renders the correct view directly, with no separate client-side flag request or layout shift
- **Evidence**: Direct product-mechanism description with an explicit before/after framing (client-side evaluation causes a loader/flicker/layout-shift; server-side evaluation avoids it), plus a worked Next.js code example.
- **Confidence**: settled (first-party description of a named, GA product mechanism, with a runnable code example)
- **Quote**: "When a flag is evaluated on the client, users see a loader, a flicker, or a layout shift. The browser can't render the correct view until the flag value comes back. The Flags SDK evaluates on the server instead. With Next.js React Server Components, you read the flag with await during render. The correct view is determined server-side and the browser renders it directly, with no separate flag request. That value comes from Vercel Flags, where a configuration change propagates to every region within milliseconds."
- **Our assessment**: The "propagates to every region within milliseconds" claim is a specific, falsifiable latency assertion but is given no supporting number or methodology (contrast with `blog-vercel-ai-gateway-api-key-budgets.md`, which gives specific propagation-delay ranges like "tens of seconds to five minutes" for a different Vercel feature) — treat the milliseconds figure as a marketing assertion, not a measured SLA, unless independently confirmed. The underlying architectural point (server-side evaluation eliminates the client-request round trip that causes flicker) is a well-understood, uncontroversial mechanism.

### Claim 2: Flags defined in code register automatically in the dashboard as drafts on deploy, and removing a flag from code marks it "unreferenced" in the dashboard, so there is no separate flag list to keep in sync by hand
- **Evidence**: Direct product-mechanism description with a worked `flags.ts` code example.
- **Confidence**: settled (first-party description of a named, GA product mechanism)
- **Quote**: "Vercel Flags registers flags automatically. Define one in code, deploy, and it appears in the dashboard as a draft. Promote the draft when you're ready to configure targeting and roll out. Remove the flag from your code and the dashboard marks it as unreferenced, so you always know what's safe to archive. The flags you write are the flags you manage, with no separate list to keep in sync by hand."
- **Our assessment**: This is a concrete, product-level answer to the exact "flags accumulate faster than they get removed" hygiene problem documented in `blog-pragmaticengineer-erez-cicd.md` Claim 5 ("the ease with which feature flags are added can create a hygiene crisis if they're continuously added, but not removed"). Where Erez's post treats flag cleanup as a manual, ongoing gardening discipline the team must maintain, Vercel Flags' code-as-source-of-truth model automates *detection* of stale flags (unreferenced-in-code -> flagged in dashboard) even though it does not automate *removal* — the team still has to act on the "unreferenced" signal. This is a meaningful but partial answer to the hygiene problem, not a full solution (see Cross-References and Guide Impact).

### Claim 3: Precompute lets teams keep a page fully static (served from the CDN, no layout shift) even though it contains a feature flag, by building all flag variants at build time and using Routing Middleware to route each user to the correct pre-built variant
- **Evidence**: Direct product-mechanism description, framed as solving a named tradeoff (dynamic-rendering-for-flags vs. static-CDN-delivery) that the SDK's default server-side evaluation does not solve on its own.
- **Confidence**: settled (first-party description of a named, documented SDK pattern, explicitly flagged by the source itself as advanced)
- **Quote**: "Static pages are fast and consistent because they are served from the CDN regions closest to you and your users. But adding a flag makes a page dynamic. Either you render server-side and lose CDN delivery, or you fetch the flag client-side and get layout shift back. However, Flags SDK comes with an optional, advanced pattern that solves this. Precompute lets you build all variants at build time, distribute them through the CDN, and have Routing Middleware (the proxy.ts file in Next.js) route each user to the right one. Every page stays static and loads with no layout shift."
- **Our assessment**: The source itself caveats this as an advanced pattern ("Precompute is an advanced but powerful pattern. Read the docs to learn more.") and does not explain how many variants are practical to precompute before build-time and CDN-storage costs become prohibitive (e.g., a flag with many possible target-segment combinations). This is a real architectural tradeoff worth flagging for the guide rather than treating Precompute as a universally-applicable solution to the static-vs-dynamic flag tension.

### Claim 4: The `vercel flags` CLI exposes the same flag-management operations (create, configure targeting, run rollouts, archive) from the terminal that the dashboard exposes, explicitly framed as usable by both humans and coding agents
- **Evidence**: Direct product description, repeated in two places in the post (once under "Agent-native flag management," once in the closing "Get started" section).
- **Confidence**: settled (first-party description of a named, GA CLI feature)
- **Quote**: "The vercel flags CLI exposes the same flag management from your terminal, so you and your coding agents can create flags, configure targeting, run rollouts, and archive them."
- **Our assessment**: This is a concrete, named instance of a platform vendor explicitly designing a management surface for coding-agent use rather than treating agent access as an incidental side effect of having a CLI at all — the phrasing "you and your coding agents" puts agent operators on equal footing with human operators for a production-safety-relevant action (rollout control, kill switches). No prior corpus source documents an agent-addressable feature-flag CLI specifically; this extends the "agent-native CLI as a first-class management interface" pattern already seen for Vercel Connect's `vercel connect revoke-tokens`/`vercel connect create` CLI (`blog-vercel-enterprise-apps-and-agents.md`, Concrete Artifacts) into the feature-flag domain.

### Claim 5: Flags Explorer, built into the Vercel Toolbar, lets a developer override any flag's value for their own browser session to test a variant, without changing the shared configuration or redeploying
- **Evidence**: Direct product-mechanism description.
- **Confidence**: settled (first-party description of a named, GA feature)
- **Quote**: "Flags Explorer, built into the Vercel Toolbar, lets you override any flag in your browser session to test a variant. The shared configuration stays untouched and you do not redeploy."
- **Our assessment**: This is a session-scoped, non-destructive override mechanism — useful for the guide's testing/verification material as a concrete example of "test a flagged variant without affecting other users or committing to the change," distinct from and complementary to the staged-percentage rollout mechanism in Claim 8.

### Claim 6: The v0 team runs hundreds of flags active at any given moment, cited as Vercel's example of what flag usage "looks like at scale" internally
- **Evidence**: First-party statement about Vercel's own internal usage of its own product, stated twice in the post (once in the introduction, once in the "Vercel ships on Vercel Flags" section) with identical wording.
- **Confidence**: anecdotal (single named internal team, no external verification, no time-series data — just a snapshot claim repeated twice)
- **Quote**: "The v0 team alone runs hundreds at any given moment."
- **Our assessment**: This is a vendor's own dogfooding claim about a single internal team, not a customer case study or independently measured usage pattern — treat as illustrative of intended scale, not as evidence that "hundreds of flags" is a typical or recommended number for other teams. It does, however, sharpen the stakes of Claim 2's hygiene-automation point: at "hundreds" of active flags, a code-as-source-of-truth registration/unreferenced-detection system stops being a nice-to-have and becomes load-bearing for the flag list to stay legible at all.

### Claim 7: Because every new feature at Vercel is built behind a flag, developers merge to `main` continuously without releasing unfinished work, eliminating long-lived branches and the merge conflicts that come with them
- **Evidence**: First-party statement about Vercel's own internal engineering practice, presented as a direct consequence of flag-based feature gating rather than a separate initiative.
- **Confidence**: anecdotal (internal practice description, no metrics on branch lifetime, conflict rate, or merge frequency given)
- **Quote**: "Because every new feature is built behind a flag, developers can merge to main continuously without releasing unfinished work. There are no long-lived branches and no painful merge conflicts to resolve. Deploying code and releasing a feature become two separate decisions."
- **Our assessment**: "Deploying code and releasing a feature become two separate decisions" is the single most reusable framing sentence in this source — it names the core architectural benefit of flag-gated development (decoupling the deploy event from the release event) in one clause, independent of any Vercel-specific product mechanics. This directly corroborates the trunk-based-development argument implicit in `blog-pragmaticengineer-erez-cicd.md`'s roll-forward-preferred stance (Claim 1 there), though that source addresses deployment rollback risk rather than branch-lifetime/merge-conflict risk specifically — the two sources approach flag-gated development from different angles (incident response vs. day-to-day merge hygiene) that reinforce, rather than duplicate, each other.

### Claim 8: v0's feature releases move through a fixed staged rollout — developer, then internal team, then 5%, 10%, 25%, and 50% of users for six hours each, before reaching everyone — with the ability to kill the feature at any stage without a code change or redeploy
- **Evidence**: First-party description of Vercel's own internal rollout process for the v0 product, given as a specific numeric sequence rather than a general description of "gradual rollout."
- **Confidence**: settled (specific, named internal process with exact percentages and timing given, though for a single internal team/product, not validated across other Vercel teams or customers)
- **Quote**: "A release moves through a controlled progression. The developer who built the feature sees it first, then the internal team. After that, the flag steps up through 5%, 10%, 25%, and 50% of users for six hours each, before going to everyone. If something goes wrong at any stage, the team can kill the feature without making a code change or redeploying."
- **Our assessment**: This is the most concrete, reusable operational artifact in the source — a specific staged-percentage/dwell-time rollout schedule (5/10/25/50%, six hours per stage) that a guide could cite as a worked example of "what a real progressive rollout schedule looks like in practice," rather than the generic advice to "roll out gradually." It directly corroborates `blog-pragmaticengineer-erez-cicd.md` Claim 4's "toggle off, don't redeploy" incident-response preference — the "kill the feature without making a code change or redeploying" clause here is functionally identical to Erez's "reaching for a toggle... is less nerve-jangling than scrambling to force a redeployment" — two independent sources agreeing that flag-based kill switches are strictly faster and lower-risk than deployment rollback for incident mitigation.

### Claim 9: Vercel Flags controls v0's AI model traffic, shifting users to a new model gradually rather than cutting over all at once when a new model launches
- **Evidence**: A single-sentence first-party statement, given without the staged-percentage detail provided for the general rollout process in Claim 8.
- **Confidence**: anecdotal (asserted without the specific percentage/timing breakdown given for Claim 8; unclear whether it reuses the same 5/10/25/50% schedule or a different one)
- **Quote**: "Flags also control v0's AI model traffic, shifting gradually when a new model launches rather than cutting over all at once."
- **Our assessment**: This is a specific, named application of feature-flag-based gradual rollout to *AI model routing/migration* specifically, distinct from generic feature rollout — a directly relevant pattern for guide material on model-migration risk management (e.g., switching a production coding agent from one model to a newer one). However, the claim is thin: no percentage schedule, no rollback trigger criteria, and no outcome/incident data are given, unlike Claim 8's fully specified schedule for feature rollouts generally.

### Claim 10: v0 executed a production database migration using a flag as the literal cutover mechanism — keeping old and new databases in sync, then flipping the flag to switch which database was live, after repeated staging rehearsals
- **Evidence**: First-party narrative description of a specific internal engineering event, presented as Vercel's most extreme example of what "putting infrastructure behind a flag" can mean.
- **Confidence**: anecdotal (single narrated internal event, no date given, no metrics on sync lag, rehearsal count, or post-migration validation beyond "without degrading traffic")
- **Quote**: "v0 even ran a production database migration with a flag. We kept the old and new databases in sync, and the flag controlled which database was in use. Flipping the flag was the cutover itself. We rehearsed it in staging repeatedly, then ran it in production without degrading traffic. The flag turned a high-stakes infrastructure change into something the team could practice, schedule, and ship with confidence."
- **Our assessment**: "The flag turned a high-stakes infrastructure change into something the team could practice, schedule, and ship with confidence" is a strong, quotable framing for extending feature-flag thinking beyond UI/feature gating into infrastructure cutover risk management generally (database migrations, provider swaps — also listed as a category in Claim 6's bullet list: "Database migrations and provider swaps"). The claim is thin on verification detail (no sync-lag figures, no explicit rollback-if-inconsistent mechanism described), so treat the *pattern* (flag-as-cutover-switch, rehearsed repeatedly in staging first) as the reusable takeaway rather than the specific v0 migration as a fully-documented case study.

### Claim 11: Flags SDK is an open-source, provider-agnostic library with first-class adapters for Next.js and SvelteKit, plus a built-in OpenFeature provider for other frameworks — positioned explicitly against vendor lock-in to Vercel Flags specifically
- **Evidence**: Direct product-positioning statement distinguishing the open-source SDK layer from the Vercel Flags dashboard/backend product.
- **Confidence**: settled (first-party description of a named, open-source project and its interoperability mechanism)
- **Quote**: "From your code, you read flags through Flags SDK, an open-source, provider-agnostic library we maintain with first-class adapters for Next.js and SvelteKit. If you are using another framework, you can consume Vercel Flags using the built-in OpenFeature provider."
- **Our assessment**: OpenFeature is the CNCF-backed vendor-neutral feature-flag standard; supporting it as an escape hatch is a meaningful anti-lock-in signal distinct from most of Vercel's other platform-native products in this corpus (Passport, Connect, Enterprise Managed Users — see `blog-vercel-enterprise-apps-and-agents.md` — are all Vercel-platform-specific with no stated open-standard interop path). This is the first corpus source to document a Vercel product explicitly interoperating with a vendor-neutral open standard as a stated design choice, worth noting as a partial counterexample to a "Vercel platform-native means Vercel-only" generalization.

### Claim 12: Vercel Flags became generally available in April 2026, after being used internally at Vercel for over a year before that
- **Evidence**: First-party GA-date and pre-GA-usage-duration statement.
- **Confidence**: settled (first-party, specific, unambiguous factual claim about the vendor's own product timeline)
- **Quote**: "While we made Vercel Flags generally available in April 2026, we've been using it internally for over a year."
- **Our assessment**: Useful for dating this source's claims relative to other Vercel product timelines in the corpus — e.g., `blog-vercel-enterprise-apps-and-agents.md` (announced June 16, 2026, three of its four products still Beta/Private Beta) and `blog-vercel-ai-gateway-production-index-may2026.md` (May 2026 production data) both post-date Vercel Flags' April 2026 GA, so Vercel Flags is a comparatively mature (GA, not Beta) product relative to those other announcements at the time this post was published.

## Concrete Artifacts

### Server-side flag read in a React Server Component (verbatim, `app/page.tsx`)

```tsx
import { showNewFeature } from "@/flags"

export default async function Page() {
  const isEnabled = await showNewFeature()
  return isEnabled ? <NewDashboard /> : <OldDashboard />
}

Source: https://vercel.com/blog/vercel-flags-platform-native-feature-flags
```

### Flag definition with the Vercel adapter (verbatim, `flags.ts`)

```typescript
import { flag } from "flags/next"
import { vercelAdapter } from "@flags-sdk/vercel"

export const showNewFeature = flag({
  key: "show-new-feature",
  adapter: vercelAdapter()
})

Source: https://vercel.com/blog/vercel-flags-platform-native-feature-flags
```

### v0's staged rollout schedule (verbatim)

```
"The developer who built the feature sees it first, then the internal
team. After that, the flag steps up through 5%, 10%, 25%, and 50% of
users for six hours each, before going to everyone."

Source: https://vercel.com/blog/vercel-flags-platform-native-feature-flags,
"Vercel ships on Vercel Flags" section
```

### What Vercel teams put behind flags (verbatim list)

```
- New features under development
- AI model routing per user or segment
- Operational kill switches
- Database migrations and provider swaps
- Beta access for early customers or internal teams

Source: https://vercel.com/blog/vercel-flags-platform-native-feature-flags,
"Vercel ships on Vercel Flags" section
```

## Cross-References

### Cross-reference verification notes
`blog-pragmaticengineer-erez-cicd.md`, `blog-cursor-app-stability.md`, and
`blog-vercel-enterprise-apps-and-agents.md` were re-read in full during this
extraction (MINER.md §4b), and every claim number cited above and below was
located and confirmed against that note's own numbered `### Claim N:`
headings in document order before writing this section.

- **Corroborates**:
  - `blog-pragmaticengineer-erez-cicd.md` Claim 4 ("Feature toggles are a
    faster, calmer incident-response mechanism than rolling back a
    deployment," quoting "reaching for a toggle... is less nerve-jangling
    than scrambling to force a redeployment"): this source's Claim 8 ("the
    team can kill the feature without making a code change or redeploying")
    is the identical operational claim from an independent vendor
    describing its own internal practice — two independent sources agree
    that flag-based kill switches are faster and lower-risk than deployment
    rollback for incident mitigation.
  - `blog-vercel-enterprise-apps-and-agents.md` Concrete Artifacts (the
    `vercel connect revoke-tokens` / `vercel connect create` CLI examples):
    this source's Claim 4 (`vercel flags` CLI, explicitly usable by "you and
    your coding agents") extends the same agent-native-CLI design pattern
    Vercel already applies to credential management into the feature-flag
    domain — the same vendor is consistently building CLI-first, agent-
    addressable management surfaces across multiple product lines.

- **Contradicts**: None identified as a MINER.md §4a contradiction. This
  source's Claim 2 (automatic unreferenced-flag detection) could be read as
  in tension with `blog-pragmaticengineer-erez-cicd.md` Claim 5's framing of
  flag cleanup as an ongoing manual "gardening" discipline, but this is not
  a factual disagreement — Erez's post describes the general industry
  problem and a manual remediation practice; this source describes a
  product feature that automates *detection* of the same problem (not full
  removal). The two are complementary, not opposed (see Extends, below). No
  contradiction issue filed.

- **Extends**:
  - `blog-pragmaticengineer-erez-cicd.md` Claim 5 ("flags accumulate faster
    than they get removed... treat feature-toggle cleanups like a form of
    gardening"): this source's Claim 2 (automatic dashboard-level
    unreferenced-flag marking, tied to the flag's presence in code) is a
    concrete, vendor-shipped partial automation of the detection half of
    the hygiene problem Erez's post identifies — narrowing, though not
    eliminating, the manual-discipline burden Erez describes. Removal
    itself is still a human/team decision in Vercel's model.
  - `blog-cursor-app-stability.md` Claim 4 (Statsig-based feature-flag A/B
    testing for crash attribution, "crash events must carry feature-flag
    state at the time of the crash, not just at session start"): that note
    documents flags as an *analytics/attribution* dimension (linking a
    flag's on/off state to a crash-rate outcome via a third-party flag
    provider, Statsig), a different use case from this source's rollout/
    kill-switch/precompute mechanics. Read together, the two sources cover
    complementary flag use cases — Vercel Flags for evaluation/rollout
    mechanics, Statsig (per the Cursor note) for outcome attribution — and
    a mature flag-based safety pipeline plausibly needs both: a flag-state-
    aware crash/metric pipeline (Cursor/Statsig pattern) layered on top of
    whatever evaluates and serves the flags (Vercel Flags, LaunchDarkly, or
    similar).
  - `blog-vercel-enterprise-apps-and-agents.md`: that source documents
    Vercel's access/governance product bundle (Passport, Connect,
    Enterprise Managed Users, BYOC) as a separate June 16, 2026 announcement
    from the same vendor. This source is a fourth, functionally distinct
    Vercel platform-native product line (feature flagging vs. identity/
    access governance) sharing the same "agent-native CLI" design
    philosophy (Claim 4 here vs. that note's Connect CLI) but addressing a
    different operational concern (safe progressive release vs. access
    control).

- **Novel**:
  - **Agent-addressable feature-flag CLI** (Claim 4): no prior corpus
    source documents a feature-flag management surface explicitly designed
    for coding-agent use ("you and your coding agents").
  - **Automatic unreferenced-flag detection tied to code presence**
    (Claim 2): a specific, concrete mechanism (not just a stated best
    practice) for partially automating stale-flag detection, new to this
    corpus.
  - **Precompute pattern for static-CDN delivery of flagged pages**
    (Claim 3): the corpus's first documentation of a build-time-variant/
    routing-middleware approach to reconciling feature flags with static
    site delivery.
  - **Named staged-rollout schedule with exact percentages and dwell time**
    (Claim 8: 5/10/25/50% over six hours per stage): a concrete, reusable
    worked example, more specific than any general "roll out gradually"
    guidance previously in the corpus.
  - **Feature flag as a database-migration cutover mechanism** (Claim 10):
    no prior corpus source documents using a feature flag as the literal
    dual-database cutover switch for a production data-layer migration.
  - **OpenFeature interoperability as an explicit anti-lock-in design
    choice** (Claim 11): the corpus's first example of a Vercel
    platform-native product explicitly supporting a vendor-neutral open
    standard as an escape hatch, in contrast to other Vercel products in
    the corpus that have no stated open-standard interop path.

## Guide Impact

- **Chapter 05 (Team Adoption / Systems & Operations) — flag hygiene**: Add
  Claim 2 (automatic unreferenced-flag detection in the dashboard, tied to
  the flag's presence in code) as a concrete example of *partial* tooling
  automation for the flag-hygiene problem already flagged in
  `blog-pragmaticengineer-erez-cicd.md` Claim 5. Frame it precisely: this
  automates *detection* of stale flags, not *removal* — the guide should
  not overstate this as "solving" flag hygiene, only as narrowing the
  detection half of the manual-discipline burden.

- **Chapter 05 (Systems & Operations) — incident response / rollback
  authority for agents**: Add Claim 8's specific staged-rollout schedule
  (developer -> internal team -> 5% -> 10% -> 25% -> 50%, six hours per
  stage -> everyone, kill at any stage without redeploy) as a worked,
  concrete example of a progressive-rollout policy, corroborating and
  giving numeric specificity to `blog-pragmaticengineer-erez-cicd.md`
  Claim 4's general "toggle, don't redeploy" incident-response preference.
  This also strengthens the existing "toggle-off authority as a narrow,
  low-risk autonomous agent action" argument from that note's Guide Impact
  section with a concrete schedule an agent-driven rollout system could
  implement or reference.

- **Chapter 02 (Harness Engineering) — agent-addressable operational
  tooling**: Add Claim 4 (`vercel flags` CLI explicitly designed for "you
  and your coding agents") as a second, independent example (alongside
  Vercel Connect's CLI in `blog-vercel-enterprise-apps-and-agents.md`) of a
  vendor building CLI-first management surfaces with coding-agent use as a
  first-class design consideration, not an incidental side effect of having
  a CLI at all. Useful for a guide argument that production-safety-relevant
  controls (rollout percentage, kill switches) should be scriptable/
  agent-callable, not locked behind a GUI-only dashboard.

- **Chapter 04 (Cost/Risk Engineering at Scale) — model migration risk**:
  Add Claim 9 (flags controlling v0's AI model traffic during model
  launches, "shifting gradually... rather than cutting over all at once")
  as a named pattern for de-risking a production AI model migration —
  flag-gated gradual model cutover, not a single atomic switch. Flag this
  claim's thinness explicitly in guide text: no percentage schedule or
  rollback trigger is given for the model-routing case, unlike the fully
  specified feature-rollout schedule in Claim 8.

- **Chapter 05 (Systems & Operations) — infrastructure cutover risk**: Add
  Claim 10 (database migration executed as a flag flip between synced old/
  new databases, rehearsed repeatedly in staging first) as a named pattern
  for extending feature-flag thinking to infrastructure/data-layer cutovers
  generally, not just UI feature gating. Note in guide text that this is a
  single narrated internal event with no sync-lag or consistency-validation
  detail given — cite as an illustrative pattern, not a fully specified
  procedure.

## Extraction Notes

1. **Verified against raw HTML, not WebFetch summarization alone.** Per
   MINER.md §2a, an initial WebFetch pass was cross-checked by fetching the
   page's raw HTML directly via `curl` (the site is a Next.js app; article
   text is present in escaped form inside the server-rendered page markup)
   and locating every quoted phrase used in this note character-for-
   character in that raw HTML before use. Every `Quote` field above,
   including the code examples and the staged-rollout schedule, was located
   in the raw HTML, not taken from WebFetch's paraphrased output alone.
2. **No sub-pages followed.** The post links to the Vercel Flags
   documentation, a Precompute-specific docs page, a GA changelog entry, and
   a Flags SDK "skill" for agents. None were fetched: per MINER.md §1, these
   are peripheral docs/changelog links rather than a substantive companion
   article the way, e.g., `/blog/introducing-vercel-connect` was for
   `blog-vercel-enterprise-apps-and-agents.md`. The announcement post itself
   is self-contained and was read in full.
3. **No named customer beyond Vercel's own v0 team.** All internal-usage
   claims (Claims 6-10) describe Vercel's own product, v0, not an
   independent customer — this is reflected in the "anecdotal" confidence
   rating for those claims and the overall "emerging" confidence rating for
   the note, despite several individual product-mechanism claims (Claims
   1-5, 11-12) being rated "settled" as unambiguous first-party descriptions
   of named, GA features.
4. **No contradiction issues filed.** The one near-tension considered
   (automatic unreferenced-flag detection here vs. the manual "gardening"
   framing in `blog-pragmaticengineer-erez-cicd.md` Claim 5) was evaluated
   against MINER.md §4a and judged complementary, not contradictory — see
   Cross-References → Contradicts.
5. **Confidence calibration: emerging.** Individual product-mechanism
   claims (server-side evaluation, automatic registration, Precompute, the
   CLI, Flags Explorer, OpenFeature support, GA timing) are rated "settled"
   as unambiguous first-party descriptions of named, shipping (GA, not
   Beta) features. The note's overall confidence is "emerging" rather than
   "settled" because the most concrete, guide-relevant operational claims
   (the staged-rollout schedule, the AI-model-routing use, and the
   database-migration cutover) are all single-team internal anecdotes from
   Vercel's own v0 product, with no metrics, no external customer
   validation, and — for the model-routing and database-migration claims
   specifically — no supporting detail beyond one or two sentences each.
