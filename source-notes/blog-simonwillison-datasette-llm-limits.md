---
source_url: https://simonwillison.net/2026/May/15/datasette-llm-limits/
source_type: blog-post
title: "datasette-llm-limits 0.1a0"
author: Simon Willison
date_published: 2026-05-15
date_extracted: 2026-05-24
last_checked: 2026-05-24
status: current
confidence_overall: emerging
issue: "#890"
---

# datasette-llm-limits 0.1a0

> A one-paragraph release announcement for datasette-llm-limits, a Datasette
> plugin enabling per-user and global USD spending limits on LLM usage — notable
> for demonstrating actor-scoped, rolling-window cost governance as a composable
> plugin-layer architectural pattern.

## Source Context

- **Type**: blog-post (release announcement — a "beat" post in Simon Willison's
  format; fewer than 100 words of prose plus one YAML configuration example)
- **Author credibility**: Simon Willison is the creator of Datasette and the
  `llm` CLI. As the plugin's author, this is first-party release documentation.
  The YAML configuration example is authoritative for how the plugin accepts
  configuration. The post contains no practitioner analysis or production
  validation — it is a release announcement, not an experience report. The
  `0.1a0` alpha designation signals early-stage development.
- **Scope**: The announcement describes one specific feature: per-user
  (actor-scoped) spending limits with a rolling 24-hour window denominated in
  USD. Also mentions global (non-actor) limits. Does NOT include: metrics on
  cost savings, production deployment experience, multi-window configuration,
  rate-limit-exceeded behavior, or comparison to alternative approaches.

## Extracted Claims

### Claim 1: datasette-llm-limits is a Datasette plugin that configures periodic spending limits on LLM usage within Datasette

- **Evidence**: Plugin description from the release announcement, authored by
  the tool's creator. The phrase "periodic limits" is precise — it implies
  limits that reset over time windows (recurring budgets) rather than one-time
  caps.
- **Confidence**: settled (first-party release documentation from the tool's
  author; the description and YAML are authoritative for what the plugin does)
- **Quote**: "Plugin for configuring periodic limits on LLM usage in Datasette"
- **Our assessment**: The plugin fills a specific operational gap in the
  Datasette LLM ecosystem: cost governance. Prior to this plugin, Datasette-
  based LLM deployments lacked a native mechanism for enforcing spending limits
  on individual users. The "periodic" framing is architecturally significant —
  rolling-window limits are a different class of control from one-time caps or
  aggregate quotas.

### Claim 2: datasette-llm-limits operates as the third component of a three-package stack — datasette-llm (LLM execution) + datasette-llm-accountant (usage tracking) + datasette-llm-limits (spending enforcement)

- **Evidence**: The release announcement explicitly states the plugin "works in
  conjunction with datasette-llm and datasette-llm-accountant."
- **Confidence**: settled (stated by the tool's author in the release
  announcement)
- **Quote**: "This plugin works in conjunction with datasette-llm and
  datasette-llm-accountant to let you configure a per-user (or global) spending
  limit for LLM usage inside of Datasette."
- **Our assessment**: This three-package stack is an important architectural
  claim: cost governance here requires execution (datasette-llm), accounting
  (datasette-llm-accountant), and enforcement (datasette-llm-limits) as
  separate, composable layers. The accountant component is the data layer that
  tracks usage; the limits plugin acts on that data. This separation of metering
  and enforcement is a design pattern reusable beyond Datasette. Importantly,
  datasette-llm-limits alone is not sufficient for cost governance — all three
  components must be deployed together.

### Claim 3: The plugin supports both per-user (actor-scoped) and global spending limits, selectable via the `scope` configuration field

- **Evidence**: The release announcement states the plugin allows users to
  configure "a per-user (or global) spending limit." The YAML example
  demonstrates the per-user pattern with `scope: actor`.
- **Confidence**: settled (stated by the tool's author in the release
  announcement; per-user and global are both named explicitly)
- **Quote**: "to let you configure a per-user (or global) spending limit for
  LLM usage inside of Datasette"
- **Our assessment**: The distinction between actor-scoped and global limits
  enables different governance models. Actor-scoped limits prevent individual
  users from over-consuming (fairness model); global limits cap the entire
  Datasette instance's LLM spending (organizational budget model). Both are
  stated as supported, though only the actor-scoped configuration is shown in
  the example. For multi-tenant Datasette deployments, actor-scoped limits are
  the primary governance mechanism.

### Claim 4: Spending limits are specified in USD via the `amount_usd` field, making cost governance denominated in dollars rather than token counts

- **Evidence**: The YAML configuration example shows `amount_usd: 1.00` as the
  limit value.
- **Confidence**: settled (YAML example from the tool's author is authoritative
  for the configuration schema)
- **Quote**: (no direct prose quote; the YAML shows `amount_usd: 1.00`)
- **Our assessment**: USD denomination is a significant design choice: it
  abstracts away the token-per-model complexity. A $1.00/day budget applies
  regardless of which model is used — different models consume different
  fractions of that dollar, but the administrator does not need to set per-model
  token limits. This makes cost governance more maintainable in multi-model
  deployments because the dollar budget is stable even as underlying model
  prices change. The trade-off: USD limits require a cost-per-token mapping
  that must stay current as model pricing changes, and the accountant must
  translate tokens to dollars accurately.

### Claim 5: Limits use a rolling window (`rolling-24h`) rather than a calendar-day or fixed-period reset, providing smoother cost control

- **Evidence**: The YAML configuration example shows `window: rolling-24h`.
- **Confidence**: settled (YAML example from the tool's author)
- **Quote**: (no direct prose quote; the YAML shows `window: rolling-24h`)
- **Our assessment**: Rolling windows provide smoother rate control than
  calendar-day resets. A calendar-day limit resets at midnight, creating a
  predictable burst window at the start of each day. A rolling-24h window means
  the available budget at any moment reflects spending in the preceding 24
  hours — preventing both end-of-day exhaustion and start-of-day bursting. This
  is the same rolling-window design used in API rate limiting (see
  `docs-ghaw-rate-limiting-controls.md` Claim 8 for the gh-aw per-user `window`
  field), applied here to dollar-denominated spending rather than request counts.

### Claim 6: Limit rules are defined under a named key within `limits:`, implying the schema supports multiple simultaneous limit rules per deployment

- **Evidence**: The YAML configuration shows `per-user-daily` as a named rule
  under `limits:`. The nesting implies additional named rules could coexist
  (e.g., both `per-user-daily` and `global-monthly`).
- **Confidence**: emerging (structural inference from the YAML schema; the
  announcement shows only one rule, so simultaneous multi-rule capability is
  inferred rather than demonstrated)
- **Quote**: (no direct prose quote; see YAML artifact in Concrete Artifacts)
- **Our assessment**: The name (`per-user-daily`) is a user-defined label, not
  a reserved keyword — it is a descriptive identifier chosen by the
  administrator. The structure is consistent with other multi-rule configuration
  patterns (Nginx location blocks, GitHub Actions job steps, gh-aw `rate-limit`
  configs). However, the announcement does not confirm multiple simultaneous
  limits work — this is an inference from the schema structure, not a stated
  feature.

### Claim 7: datasette-llm-limits is at version 0.1a0 (early alpha), with no stated production validation in the release announcement

- **Evidence**: The release announcement title contains the version string
  `0.1a0`, which follows Python's pre-release versioning convention (alpha 0).
- **Confidence**: settled (version string is unambiguous; alpha status is a
  standard Python packaging convention)
- **Quote**: "datasette-llm-limits 0.1a0"
- **Our assessment**: Alpha status means the configuration schema may change
  before a stable release. The `amount_usd` field, `scope`, `window`, and
  named-limit structure documented here may not be stable. Practitioners
  building on this plugin in production should treat the configuration schema
  as provisional. The pattern (actor-scoped, rolling-window, USD-denominated
  limits) is architecturally sound regardless of API stability.

## Concrete Artifacts

### Full Configuration Example (verbatim from blog post)

```yaml
plugins:
  datasette-llm-limits:
    limits:
      per-user-daily:
        scope: actor
        window: rolling-24h
        amount_usd: 1.00
```

*Source: Simon Willison, simonwillison.net/2026/May/15/datasette-llm-limits/,
2026-05-15*

Field reference (inferred from structure and names):
- `per-user-daily` — user-defined label for this limit rule
- `scope: actor` — apply limit per authenticated Datasette user
- `window: rolling-24h` — rolling 24-hour window (not a calendar-day reset)
- `amount_usd: 1.00` — USD spending limit per actor per window period

### Complete Prose Content of the Post (verbatim)

The full prose body of the announcement (the post is a "beat" — a short-form
release note):

> "Plugin for configuring periodic limits on LLM usage in Datasette"

> "This plugin works in conjunction with datasette-llm and
> datasette-llm-accountant to let you configure a per-user (or global) spending
> limit for LLM usage inside of Datasette. Configuration looks something like
> this:"

*Source: Simon Willison, simonwillison.net/2026/May/15/datasette-llm-limits/,
2026-05-15. This is the complete prose content — the source is intentionally
thin (two sentences + YAML configuration example).*

## Cross-References

- **Corroborates** `failure-cursor-ultra-billing-cache-explosion.md` (Lesson 4:
  "Cache breakpoints are vendor-controlled, not user-controlled"): That lesson
  documents the failure mode where users cannot inspect, cap, or reduce the
  billable prompt-cache state in Cursor — vendor controls the billing, user is
  blind to the mechanism. datasette-llm-limits addresses the inverse pattern:
  it gives the deployment administrator explicit, configurable control over
  per-user spending limits at the application layer. The two notes bracket the
  design space: closed-system billing opacity (Cursor failure) vs. open-system
  billing governance (datasette-llm-limits).

- **Corroborates** `failure-cursor-ultra-billing-cache-explosion.md` (Lesson 6:
  "Billing transparency requires exporting CSV, not reading the product UI"):
  That lesson documents that Cursor's only diagnostic path for billing anomalies
  is CSV export after the fact — purely reactive. datasette-llm-limits
  represents the proactive alternative: enforce hard limits before costs
  accumulate, rather than detect them after. Both notes address LLM billing
  governance; one documents the reactive diagnosis failure pattern, the other
  demonstrates a preventive enforcement pattern.

- **Corroborates** `docs-github-copilot-code-review-actions-billing.md`
  (Claim 7: "Teams and Enterprise organizations can use spending limit budgets
  to manage GitHub Actions overage from Copilot code reviews"): Both sources
  demonstrate spending-limit governance for AI tooling — GitHub Copilot at the
  platform level (GitHub's built-in spending limits on Actions minutes) and
  datasette-llm-limits at the application framework level (plugin-enforced USD
  limits on LLM calls). The parallel confirms that spending limits are an
  emerging standard pattern for AI cost governance across different deployment
  contexts and scales.

- **Extends** `docs-ghaw-rate-limiting-controls.md` (Claim 8: "The `rate-limit`
  frontmatter field provides per-user request throttling — `max` (1–10 runs per
  window) and `window` (up to 180 minutes) — with `ignored-roles` defaulting to
  `[admin, maintain]` and `events` to filter which trigger types count"): gh-aw
  rate limiting governs request *count* per user per window; datasette-llm-limits
  governs USD *spending* per user per window. Both use actor-scoped + named-window
  semantics. datasette-llm-limits extends the per-user rate limiting pattern into
  the cost dimension: it is what request-count rate limiting looks like when the
  variable of concern is money rather than throughput.

- **Extends** `blog-simonwillison-llm031.md` (overall): That note documents
  `llm 0.31`, another Simon Willison tool release from the same datasette-llm
  ecosystem. Both are thin release announcements from the same author in the
  same tooling family. This note adds the cost-governance layer to the tooling
  stack documented in prior llm notes. Together these notes document Willison's
  Datasette LLM ecosystem as an incrementally composable stack: model access
  (`datasette-llm`, `llm`), accounting (`datasette-llm-accountant`), and
  enforcement (`datasette-llm-limits`).

- **Novel**:
  - First corpus source to document actor-scoped, USD-denominated, rolling-window
    spending limits as a Datasette plugin configuration pattern.
  - First corpus source to describe a three-layer LLM governance stack (execution /
    accounting / enforcement) as a composable plugin architecture — the pattern is
    stated as a general principle, not Datasette-specific.
  - The `amount_usd` field is the first corpus example of dollar-denominated limit
    configuration for LLM governance (prior corpus sources on rate limiting use
    request-count or token-count windows, not dollar amounts).
  - Rolling-window design (`rolling-24h`) for LLM *cost* governance is first
    documented here — prior corpus rate-limiting sources apply rolling windows to
    request counts, not dollar-denominated spending.

## Guide Impact

- **Chapter 04 (Context as budget / cost control)**: Add datasette-llm-limits
  as a concrete implementation of per-user LLM cost governance at the application
  layer. The `amount_usd: 1.00` per rolling-24h example is the first corpus
  artifact showing dollar-denominated, rolling-window budget enforcement. Pair
  with `failure-cursor-ultra-billing-cache-explosion.md` Lessons 4 and 6 for the
  motivating failure context: the Cursor failure shows what happens without
  proactive governance; datasette-llm-limits shows one architectural response.
  The three-layer stack pattern (execution + accounting + enforcement) is
  generalizable beyond Datasette and should be presented as a reusable governance
  architecture.

- **Chapter 05 (Team adoption at scale)**: Add the three-package stack
  (datasette-llm + datasette-llm-accountant + datasette-llm-limits) as a
  reference architecture for rolling out LLM tooling to teams with cost
  governance built in from day one. The actor-scoped daily limit ($1.00/user/
  rolling-24h in the example) is a concrete starting point for teams evaluating
  LLM governance policies before wider rollout. Note the alpha status: the
  specific API may change, but the pattern (enforce limits at the application
  layer, denominated in USD, scoped per actor) is architecturally reusable and
  worth establishing as a governance principle regardless of the specific tool.

- **Chapter 01 (Daily workflows)**: If the guide covers Datasette-based LLM
  workflows (following `blog-simonwillison-llm031.md` and related notes),
  datasette-llm-limits should be cited as the cost governance plugin in that
  ecosystem. Individual practitioners running team-shared Datasette LLM instances
  should deploy datasette-llm-limits alongside datasette-llm-accountant as
  standard operational practice — the three-package stack is the complete
  deployment unit.

## Extraction Notes

- **Very thin source**: The blog post is a "beat" in Simon Willison's format —
  a short release announcement, not an analysis or experience report. Total prose
  is two sentences plus a YAML configuration block. The Prospector triage
  correctly identifies high novelty (the cost governance pattern is new to the
  corpus) despite the source's brevity.
- **Verbatim content confirmed**: Full page text was extracted via curl + HTML
  parsing (Python HTMLParser). The verbatim prose and YAML are confirmed from
  the raw HTML. The post's recent-articles sidebar references "Datasette Agent"
  (21st May 2026) — that post is a separate source from 6 days later and was
  not followed.
- **GitHub and PyPI inaccessible**: `simonw/datasette-llm-limits` GitHub
  repository and its PyPI page returned 404 or JS-load errors at extraction
  time. Claims are based solely on the blog post content and YAML configuration
  example. The Assayer should verify the configuration schema against the
  package repository if available at review time. The `simonw/datasette-llm`
  repository is confirmed archived (2026-01-22), so the ecosystem has been in
  transition; datasette-llm-limits may live in a different namespace.
- **datasette-llm-accountant not independently mined**: The blog post references
  datasette-llm-accountant as a dependency but provides no description of its
  internals. The accounting layer is mentioned as a fact about the plugin stack;
  if it is mined separately, Claim 2 should be updated with that note's reference.
- **No contradictions filed**: No existing source note makes claims about
  datasette-llm-limits or its architectural pattern that conflict with this
  source. The actor-scoped, rolling-window, USD-denominated cost governance
  pattern is entirely new to the corpus. No contradiction issue required.
