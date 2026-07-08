---
source_url: https://vercel.com/changelog/budgets-for-api-keys-on-ai-gateway
source_type: blog-post
title: "Budgets for API keys on AI Gateway"
author: Mark Roberts, Kevin Dawkins, Walter Korman, Jeremy Philemon, Jerilyn Zheng (Vercel)
date_published: 2026-06-09
date_extracted: 2026-07-08
last_checked: 2026-07-08
status: current
confidence_overall: settled
issue: "#1645"
---

# Budgets for API keys on AI Gateway

> Vercel AI Gateway API keys can now carry an optional, dollar-denominated
> spend budget with a configurable UTC-aligned refresh period; the gateway
> checks the budget before each request and rejects further requests on
> that key once exceeded — but the linked technical reference clarifies
> this is a soft cap (checked at request start, so an in-flight request can
> still push spend slightly over) rather than a hard, mid-request cutoff.

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`,
  published June 9, 2026; a short feature-announcement entry, roughly a
  2-minute read per the page's own read-time estimate). This note also
  follows the changelog's own "Read the API keys documentation for more
  information about setting and using budgets for API keys" link to the
  dedicated reference page (`/docs/ai-gateway/observability-and-spend/api-key-budgets`,
  last updated June 20, 2026 — eleven days after the changelog entry), per
  MINER.md §1's "follow up to 5 linked pages that seem substantive."
- **Author credibility**: First-party Vercel product announcement, listing
  five named authors with public profile links (Mark Roberts, Kevin
  Dawkins, Walter Korman, Jeremy Philemon, Jerilyn Zheng), consistent with
  Vercel's changelog byline convention. Vercel operates the AI Gateway
  product being described, so feature mechanics, CLI syntax, and API
  behavior are authoritative first-party documentation of a shipping
  capability — not third-party reporting or a customer anecdote. Jerilyn
  Zheng is also a listed author on `blog-vercel-ai-gateway-production-index-may2026.md`,
  Vercel's monthly AI Gateway usage report already in this corpus.
- **Scope**: Covers the API-key budget feature specifically — what it does,
  why Vercel built it (three named risk scenarios), and how to configure it
  via Dashboard or CLI. Does NOT cover: pricing of the AI Gateway product
  itself, budgets at any scope other than a single API key (e.g.
  team-level or project-level spend limits), historical spend analytics, or
  alerting/notification on approaching a budget limit — no threshold-alert
  mechanism (of the kind documented in `blog-anthropic-admin-analytics-cost-controls.md`
  Claim 7) is described in either the changelog or the linked reference
  page. The changelog itself is ~250 words; most of the granular mechanism
  detail in this note comes from the linked reference page, which is
  substantially longer and is treated here as part of the same source
  family (the changelog explicitly directs readers to it for "more
  information about setting and using budgets").

## Extracted Claims

### Claim 1: A budget on an AI Gateway API key blocks further requests on that key once the dollar limit is exceeded, until the budget resets on its refresh period or is manually raised
- **Evidence**: Direct statement in the changelog's opening paragraph, restated with the same "checks before each request" framing on the linked reference page.
- **Confidence**: settled (first-party description of a shipping platform feature, corroborated verbatim in substance across two pages of the same source)
- **Quote**: "Set a spend cap on any key, and AI Gateway rejects further requests on that key once the limit is exceeded, until the budget resets or you raise it."
- **Our assessment**: This is the feature's headline behavior and the plainest statement of the mechanism. Read on its own, it implies a hard stop at the exact dollar limit. Claim 2 below, from the linked reference page, adds a load-bearing nuance the changelog omits: the check happens before a request starts, not continuously during it, so the boundary is not exact. Practitioners relying on this as a strict circuit breaker (e.g., to bound a runaway agent's spend to an exact dollar figure) should read Claim 2 before treating "$10 budget" as "never more than $10 spent."

### Claim 2: The budget is a soft cap, not a hard limit — because the check runs at the start of each request, a request that crosses the limit still completes in full, so total spend can end up slightly over the configured budget
- **Evidence**: Explicit callout box on the linked reference page (`/docs/ai-gateway/observability-and-spend/api-key-budgets`), presented as a clarifying note directly under the page's opening definition of what a budget does.
- **Confidence**: settled (first-party technical reference; the mechanism described — check-then-request rather than continuous metering — is a specific, falsifiable design detail, not a hedge)
- **Quote**: "A budget is a soft cap, not a hard limit. The check runs at the start of each request, so the request that crosses the limit still completes and total spend can end up slightly over the budget."
- **Our assessment**: This is the single most important operational detail in the source and the one most likely to be missed by a reader who only sees the changelog (which does not mention it at all — see Claim 1). It does not contradict Claim 1's "rejects further requests... once exceeded" framing (the *next* request after the crossing one is in fact rejected), but it does mean a budget cannot be relied on as an exact ceiling for a single expensive request — a key with a $10 budget that is one $50 request away from its limit will complete that $50 request, landing spend at up to $60 before the next request is blocked. For any guide advice framing API-key budgets as a blast-radius-limiting control (see Guide Impact), this soft-cap behavior should be stated explicitly rather than assumed away.

### Claim 3: A budget's cap applies across every provider and model routed through that one key, not per-model or per-provider
- **Evidence**: Direct statement in the changelog, immediately following the budget-enforcement sentence.
- **Confidence**: settled (first-party description of a shipping feature's scope)
- **Quote**: "The cap applies to all AI Gateway providers and models running through the key, making it easier to consolidate and govern AI costs."
- **Our assessment**: This is a deliberate design choice with a direct tradeoff against Uber's documented governance pattern (`blog-simonwillison-uber-caps-usage.md` Claim 2): Uber caps spend *per tool* ($1,500/month per AI coding tool per employee, with separate budgets per tool so tools don't compete for the same pool). Vercel's key-scoped budget is the opposite structure — a single pool shared across every provider and model that traffic through that key touches. The practical implication: if a team wants Uber-style per-tool isolation on AI Gateway, they need one budgeted key per tool/workload, not one shared key with a single budget, because a single key's budget cannot be further subdivided by provider or model.

### Claim 4: Vercel frames the feature as a response to three specific cost-risk scenarios: autonomous agent workflows that loop or fan out unsupervised, demos/prototypes that could catch unexpected traffic if shared or shipped, and developers experimenting without a sense of per-model cost
- **Evidence**: The changelog's framing paragraph and its three-item bulleted list, presented before the feature description as the motivation for building it.
- **Confidence**: settled (first-party statement of the vendor's own stated rationale for shipping the feature — the scenarios themselves are asserted, not measured or sourced to an incident)
- **Quote**: "AI costs are getting harder to forecast. As teams lean more on coding agents and other token-heavy workflows, a key can burn cost faster than anyone notices:" followed by the list items "Autonomous workflows that can loop or fan out without supervision", "Demos and prototypes that could catch unexpected traffic if shared or shipped", and "Developers exploring or experimenting without a sense of per-model cost"
- **Our assessment**: The first named scenario ("autonomous workflows that can loop or fan out without supervision") is the same failure mode `docs-ghaw-cost-management.md` addresses with `skip-if-match` deterministic pre-checks and per-user rate limiting (Claims 5 and 8 there), and that O'Mahony's five-practice checklist addresses with "circuit breakers... so a runaway agent will be caught in minutes" (`blog-thoughtworks-omahony-feature-token-budgets.md` Claim 8). This is a third, independent vendor converging on the same problem statement — unsupervised agentic loops as a primary AI cost-overrun risk — but Vercel's mitigation is a platform-level dollar cap on the credential itself, rather than a workflow-level deterministic skip condition (gh-aw) or a per-user usage-spike cutoff (Shopify, per `blog-thoughtworks-omahony-feature-token-budgets.md` Claim 8a). These are complementary, not competing, controls: a `skip-if-match` condition prevents wasted runs before they start, while a key budget bounds the damage of runs that do start and go wrong.

### Claim 5: Budgets are configured through the Dashboard (a toggle on key creation or via an existing key's "Edit key" menu) or the CLI, with a `--budget` dollar amount and a `--refresh-period` of daily, weekly, monthly, or none
- **Evidence**: The changelog's two configuration sections — "API key budgets in the Vercel Dashboard" and "API key budgets in the Vercel CLI" (flat sibling headings, not a single "Configuration Options" section) — and its CLI command example, corroborated and extended with parameter constraints on the linked reference page.
- **Confidence**: settled (first-party documentation of shipping UI and CLI surfaces)
- **Quote**: "On the AI Gateway API Keys page, click Create Key, enable the Spend Quota option, enter a limit in dollars, and choose a refresh period." (changelog); the linked reference page adds the constraint "Spending limit in dollars (minimum $1)" for the `--budget` CLI flag.
- **Our assessment**: The $1 minimum (from the reference page, not stated in the changelog) is a small but concrete detail worth preserving — it rules out symbolic $0 "kill switch" keys; a budget always permits at least some spend once active. The changelog and reference page are consistent on the mechanism (dashboard toggle or CLI flag, four refresh-period choices) but the reference page is the more complete source for exact constraints; see Concrete Artifacts for the full CLI/API field tables.

### Claim 6: Each refresh period resets at a fixed UTC calendar boundary, not a rolling window from key creation — daily resets at 12:00 AM UTC every day, weekly at 12:00 AM UTC every Monday, monthly at 12:00 AM UTC on the 1st, and "none" never resets (the limit accumulates forever)
- **Evidence**: A dedicated reset-schedule table on the linked reference page, expanding on the changelog's briefer "Each period resets at the start of its window in UTC" line.
- **Confidence**: settled (first-party documentation of a specific, deterministic scheduling behavior)
- **Quote**: (table data extracted verbatim — see Concrete Artifacts; the changelog's own summary sentence is: "Pair a key with an optional refresh period (`daily`, `weekly`, `monthly`, or `none`) to scope the limit to a window. Each period resets at the start of its window in UTC.")
- **Our assessment**: The fixed-calendar-boundary design (as opposed to a rolling 24-hour/7-day/30-day window measured from key creation) means two keys created at different times but with the same refresh period reset in lockstep — both a key created Monday morning and one created Sunday night on a `weekly` refresh reset at the same Monday 12:00 AM UTC boundary, not seven days after their respective creation times. This is a useful, previously-undocumented-in-corpus scheduling detail for teams trying to reason about exactly when a budgeted key regains headroom.

### Claim 7: A newly-created budget is not enforced instantly — for up to a minute or two after key creation, requests may not be counted against it — and once active, recorded spend appears in the dashboard/API within about 20 seconds; edits to an existing budget also take a short delay (typically tens of seconds, up to about 5 minutes for a key in active use) to take effect
- **Evidence**: Two explicit timing callouts on the linked reference page, one in the "Add a budget when creating a key" section and one at the end of the "Add or change a budget" section. Neither timing detail appears in the changelog.
- **Confidence**: settled (first-party documentation of specific propagation-delay behavior)
- **Quote**: "A new budget is not enforced instantly. For up to a minute or two after the key is created, requests may not be counted against the budget. Once active, spend appears within about 20 seconds." / "Budget changes take effect after a short delay, typically tens of seconds and up to about 5 minutes for a key in active use. If a change doesn't appear right away, wait and retry rather than re-applying it."
- **Our assessment**: This compounds the soft-cap nuance from Claim 2: not only can a single in-flight request push spend over budget, but a freshly-created or freshly-edited budget has its own propagation window during which requests may not be counted against the (old or new) limit at all. Combined, these two timing behaviors mean a budget should be treated as a same-day-effective cost-governance control, not a real-time, sub-minute one — relevant for anyone reasoning about how quickly a budget change would actually stop spend after, say, discovering a leaked key.

### Claim 8: A key's budget is exposed and managed through a separate Quotas API (`/v1/quotas`), distinct from the API Keys endpoint — GET returns `limitAmount`, `currentSpend`, `refreshPeriod`, and `active` fields for a budgeted key, and 404s with `{"error": "Quota not found"}` for a key with no budget; the dashboard shows budgeted keys as e.g. "$1.04 / $10 spent" and unbudgeted keys as "Unlimited quota"
- **Evidence**: The linked reference page's "Check a budget and spend" section, with Dashboard/CLI/API tabs and a full example API response.
- **Confidence**: settled (first-party API reference with a concrete example payload)
- **Quote**: "On the API Keys page, a budgeted key shows its spend against the limit (for example, $1.04 / $10 spent) with the refresh period. A key without a budget shows Unlimited quota." / example response: `{"quotaEntityId": "api_key_id_<your_key_id>", "apiKeyName": "my-api-key", "limitAmount": 10, "currentSpend": 1.04, "refreshPeriod": "monthly", "active": true}`
- **Our assessment**: The API-level detail here (a dedicated Quotas API with its own entity-ID scheme, `api_key_id_<id>`) is new, concrete information not present anywhere in the changelog itself, and is the kind of implementation detail an Assayer or Smith would need to verify a guide claim like "you can programmatically check a key's remaining budget" — this note supplies the exact endpoint and response shape rather than a general description.

### Claim 9: A key's budget is its only editable property; removing a budget does not delete the underlying record but archives it, so restoring a previously-removed budget requires a PATCH (which would otherwise 409 via POST because the record still exists)
- **Evidence**: The linked reference page's "Add or change a budget" and "Remove a budget" sections.
- **Confidence**: settled (first-party API/behavior documentation, including a specific error-code detail — a 409 on POST against an archived record — that reflects internal implementation behavior, not just a UI description)
- **Quote**: "A key's budget is its only editable property." / "Removing a budget archives it rather than deleting it, so you restore it with PATCH, not POST (a POST would return 409 because the record still exists)."
- **Our assessment**: This is a specific, easy-to-get-wrong operational detail: a team that removes a budget and later wants to reinstate the exact same one might reasonably try re-creating it via the same POST call used the first time, and would hit an unexplained 409 without this documentation. It also confirms (consistent with the changelog's "You can also edit existing keys and add, change, or remove budgets... and Edit Key") that budget is deliberately the *only* mutable field on an API key — renaming or otherwise modifying a key requires deleting and recreating it, which the changelog alludes to but the reference page states explicitly.

## Concrete Artifacts

### Changelog CLI example (verbatim)

```bash
vercel ai-gateway api-keys create --name <NAME> --budget <DOLLARS> --refresh-period <PERIOD>
```
*Source: https://vercel.com/changelog/budgets-for-api-keys-on-ai-gateway*

### Refresh period reset schedule (verbatim table, from the linked reference page)

| Period | Resets at |
|---|---|
| `daily` | 12:00 AM UTC every day |
| `weekly` | 12:00 AM UTC every Monday |
| `monthly` | 12:00 AM UTC on the 1st of each month |
| `none` | Never; the limit accumulates forever |

*Source: https://vercel.com/docs/ai-gateway/observability-and-spend/api-key-budgets, table under "Add a budget when creating a key"*

### CLI flags and API fields for creating a budgeted key (verbatim, from the linked reference page)

```
CLI:
  --budget <AMOUNT>          Spending limit in dollars (minimum $1).
  --refresh-period <PERIOD>  daily, weekly, monthly, or none (default).

curl -X POST "https://api.vercel.com/v1/api-keys?teamId=$VERCEL_TEAM_ID" \
  -H "Authorization: Bearer $VERCEL_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "purpose": "ai-gateway",
    "name": "my-api-key",
    "aiGatewayQuota": { "limitAmount": 10, "refreshPeriod": "monthly" }
  }'

API fields:
  aiGatewayQuota.limitAmount    number  Budget limit in dollars (minimum 1).
  aiGatewayQuota.refreshPeriod  string  daily, weekly, monthly, or none.
```
*Source: https://vercel.com/docs/ai-gateway/observability-and-spend/api-key-budgets, "Add a budget when creating a key" section*

### Quotas API — check, add/change, and remove a budget (verbatim, from the linked reference page)

```
# Check a key's quota (quotaEntityId = api_key_id_<key id>)
curl "https://ai-gateway.vercel.sh/v1/quotas?quotaEntityId=api_key_id_<your_key_id>" \
  -H "Authorization: Bearer $AI_GATEWAY_API_KEY"

# Budgeted key -> 200 OK
{
  "quotaEntityId": "api_key_id_<your_key_id>",
  "apiKeyName": "my-api-key",
  "limitAmount": 10,
  "currentSpend": 1.04,
  "refreshPeriod": "monthly",
  "active": true
}

# Key without a budget -> 404 Not Found
{ "error": "Quota not found" }

# Add a budget to a key that doesn't have one
curl -X POST "https://ai-gateway.vercel.sh/v1/quotas" \
  -H "Authorization: Bearer $AI_GATEWAY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "quotaEntityId": "api_key_id_<your_key_id>", "limitAmount": 50, "refreshPeriod": "weekly" }'

# Change the limit or refresh period (send only what changes)
curl -X PATCH "https://ai-gateway.vercel.sh/v1/quotas?quotaEntityId=api_key_id_<your_key_id>" \
  -H "Authorization: Bearer $AI_GATEWAY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "limitAmount": 100, "refreshPeriod": "monthly" }'

# Remove a budget (reverts key to unlimited; archives rather than deletes)
curl -X DELETE "https://ai-gateway.vercel.sh/v1/quotas?quotaEntityId=api_key_id_<your_key_id>" \
  -H "Authorization: Bearer $AI_GATEWAY_API_KEY"

# Restore a removed (archived) budget — must PATCH, not POST
# PATCH body: { "archived": false, "active": true, "limitAmount": 50 }
```
*Source: https://vercel.com/docs/ai-gateway/observability-and-spend/api-key-budgets, "Check a budget and spend", "Add or change a budget", and "Remove a budget" sections*

### Risk scenarios motivating the feature (verbatim list, from the changelog)

```
"AI costs are getting harder to forecast. As teams lean more on coding
agents and other token-heavy workflows, a key can burn cost faster than
anyone notices:

- Autonomous workflows that can loop or fan out without supervision
- Demos and prototypes that could catch unexpected traffic if shared or shipped
- Developers exploring or experimenting without a sense of per-model cost"

Source: https://vercel.com/changelog/budgets-for-api-keys-on-ai-gateway
```

## Cross-References

### Cross-reference verification notes
`blog-vercel-ai-gateway-production-index-may2026.md`, `blog-thoughtworks-omahony-feature-token-budgets.md`,
`docs-ghaw-cost-management.md`, `blog-simonwillison-uber-caps-usage.md`,
`blog-anthropic-admin-analytics-cost-controls.md`, and
`blog-cursor-wayfair-ml-cost-reduction.md` were re-read in full during this
extraction (MINER.md §4b), and every claim number cited below was located
and confirmed against that note's own numbered `### Claim N:` headings in
document order before writing this section.

- **Corroborates**:
  - `docs-ghaw-cost-management.md` Claim 5 (`skip-if-match` as the
    highest-leverage cost control) and Claim 8 (`user-rate-limit`
    frontmatter field): both are workflow-level mechanisms addressing the
    same "unsupervised agent burns cost" risk this source names as its
    first motivating scenario (Claim 4 here). Vercel's key budget is a
    credential-level analog of the same governance intent, implemented at
    the network-gateway layer rather than the CI-workflow layer.
  - `blog-thoughtworks-omahony-feature-token-budgets.md` Claim 8 (the
    five-practice checklist including "circuit breakers... so a runaway
    agent will be caught in minutes") and Claim 8a (Shopify's per-user
    spend-spike cutoff, sourced from the followed Pragmatic Engineer
    link): a third independent source describing automatic cutoff on
    anomalous spend as a named best practice, now shown here as a
    productized, vendor-native feature rather than something a team must
    build itself (as Shopify did).
  - `blog-simonwillison-uber-caps-usage.md` Claim 2 (Uber's $1,500/month
    per-tool per-employee cap): both describe a dollar-denominated
    spending ceiling on an AI-tool credential as the governance mechanism.
    See **Contradicts** below for where the two diverge structurally.

- **Contradicts**: None filed as a formal MINER.md §4a contradiction issue.
  Two tensions are worth flagging explicitly, both judged to be differences
  in governance layer/design philosophy rather than opposing factual claims
  about the same mechanism:
  1. **Scope structure vs. Uber** (`blog-simonwillison-uber-caps-usage.md`
     Claim 2): Uber's cap is deliberately *per tool* — separate budgets for
     Cursor and Claude Code so the two don't compete for one pool. Vercel's
     key budget is deliberately *pooled across every provider and model*
     running through one key (Claim 3 here). These are opposite structural
     choices for the same governance goal, not a factual disagreement — a
     team wanting Uber-style per-tool isolation on AI Gateway would need
     one budgeted key per tool, since a single key's budget cannot be
     subdivided further.
  2. **Enforcement philosophy vs. Anthropic** (`blog-anthropic-admin-analytics-cost-controls.md`
     Claim 7): Anthropic's Claude Enterprise spend controls are graduated
     alerts (75%/90% admin, 75%/95% user) explicitly designed "to raise the
     cap before anyone gets blocked mid-task," with no hard reject
     described. Vercel's key budget is the opposite default: a reject-once-exceeded
     mechanism (Claim 1) with no alerting or warning threshold described
     anywhere in this source. Per the precedent set in
     `blog-anthropic-admin-analytics-cost-controls.md`'s own Cross-References
     section (which considered and declined to file a contradiction for
     the same Uber-vs-Anthropic tension), this is treated here as two
     vendors shipping different points on a hard-cap/soft-warning spectrum
     for the same underlying problem, not a contradiction about the same
     fact. The Assayer or Smith may reach a different conclusion.

- **Extends**:
  - `blog-vercel-ai-gateway-production-index-may2026.md`: that note
    documents aggregate AI Gateway usage/spend-share telemetry (which
    models and providers are consuming Gateway traffic and dollars) but
    says nothing about per-key spend controls. This source extends the
    same product's documentation into the cost-*governance* surface,
    complementing that note's cost-*observation* surface — together they
    cover both what AI Gateway usage looks like in aggregate and what
    tools exist to cap it at the credential level.
  - `blog-cursor-wayfair-ml-cost-reduction.md` Claim 12 (a Wayfair
    researcher: "I define the spec, set the cost guardrails, and feed in
    the ideas worth trying"): that source describes a researcher
    self-imposing "cost guardrails" on an agentic workflow without
    specifying what mechanism enforces them. This source supplies a
    concrete, generally-available implementation a team in that position
    could actually use — a budgeted API key scoped to that researcher's
    or workflow's traffic — giving the abstract "cost guardrail" concept
    a specific, off-the-shelf mechanism.

- **Novel**:
  - **A platform-native, dollar-denominated, per-credential spend cap with
    a documented reset schedule** (Claims 1, 3, 6): no prior corpus source
    documents an AI-provider-gateway product shipping this as a built-in,
    self-service feature — prior cost-governance examples in the corpus
    (Uber, Shopify) are organizational policies or custom-built internal
    tooling layered on top of a platform that does not natively support
    per-key budgets.
  - **The soft-cap/check-at-request-start enforcement detail** (Claim 2):
    genuinely new and non-obvious information for this corpus — every
    other spend-cap mechanism documented so far (Uber's per-tool cap,
    Shopify's spike-cutoff, Anthropic's threshold alerts) is described at
    a policy level without this kind of implementation-level precision
    about exactly when the check runs relative to the request it's
    checking.
  - **Explicit propagation-delay behavior for new/edited budgets** (Claim
    7) and **the archive-not-delete semantics for removed budgets** (Claim
    9): both are specific, previously-undocumented-in-corpus operational
    details about how a cost-governance control actually behaves at the
    edges (creation, editing, removal) rather than in steady state.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add AI Gateway API-key budgets as a
  platform-level, provider-agnostic cost-governance primitive that sits
  below/alongside workflow-level controls like `docs-ghaw-cost-management.md`'s
  `skip-if-match` and `user-rate-limit` — a team using AI Gateway can cap
  total dollar spend on a credential regardless of which workflow or tool
  routes traffic through it. Explicitly carry forward the soft-cap nuance
  (Claim 2): the guide should not describe this as an exact, hard ceiling —
  a single expensive request can still push spend over the configured
  limit before the next request is blocked.

- **Chapter 06 (Security Threat Model)**: Add API-key budgets as a
  blast-radius-limiting control for the specific risk scenarios Vercel
  itself names (Claim 4): a leaked or over-shared key, an unsupervised
  agent loop, or a demo that catches unexpected traffic. Frame this
  alongside the propagation-delay behavior (Claim 7) — a newly-created or
  newly-edited budget takes up to a few minutes to fully take effect, so
  it should be treated as a same-session-effective control, not an
  instant one, when reasoning about incident response timelines (e.g. "we
  just capped the leaked key's budget" is not equivalent to "the leaked
  key can no longer spend anything, right now").

- **Chapter 05 (Team Adoption)**: Add the three-way contrast between this
  source's platform-enforced pooled-key reject cap, Uber's org-policy
  per-tool cap (`blog-simonwillison-uber-caps-usage.md`), and Anthropic's
  graduated self-service alerting (`blog-anthropic-admin-analytics-cost-controls.md`)
  as concrete, named examples of different points on the same
  hard-cap/soft-warning design spectrum — useful for a team choosing which
  governance posture fits their risk tolerance, rather than presenting any
  one of the three as the correct default.

## Extraction Notes

1. **Fetched via direct HTTP, not WebFetch's summarized output.** An
   initial WebFetch pass on the changelog URL returned a "reproduction"
   that included at least one fabricated sentence not present in the
   actual page — a claim that the feature addresses "autonomous workflows
   that can loop or fan out without supervision" and "shared demos" in a
   single fused sentence structure, with wording ("consuming tokens
   rapidly") that does not appear anywhere in the real page. The real page
   does discuss looping/fan-out workflows and shared demos, but as three
   separate bullet-point list items with different wording (see Claim 4),
   not the WebFetch paraphrase's fused sentence. This note discarded the
   WebFetch output entirely and instead retrieved both the changelog and
   its linked reference page via direct `curl` requests, located the
   article body inside the page's embedded Next.js RSC/richtext JSON
   payload (the canonical source for the rendered HTML), and read that
   text directly. Every `Quote` field in this note was verified against
   that raw HTML/JSON, not against any WebFetch output.
2. **One linked page followed, per MINER.md §1.** The changelog's only
   substantive outbound link relevant to this issue is "Read the API keys
   documentation for more information about setting and using budgets for
   API keys," pointing to `/docs/ai-gateway/authentication-and-byok/api-keys`,
   which itself points to a more specific page,
   `/docs/ai-gateway/observability-and-spend/api-key-budgets` — the page
   actually fetched and extracted from for this note, since it is the one
   that contains the budget-specific content (the intermediate API-keys
   page only cross-references it). No other substantive linked pages were
   found from the changelog entry itself.
3. **No contradiction issues filed.** Two structural/philosophical tensions
   were identified and evaluated against MINER.md §4a (see
   Cross-References → Contradicts) — the per-tool-vs-pooled cap structure
   versus Uber, and the hard-reject-vs-graduated-alert philosophy versus
   Anthropic. Both were judged to be governance-layer/vendor-design
   differences rather than factual disagreements about the same claim,
   consistent with how `blog-anthropic-admin-analytics-cost-controls.md`
   handled the analogous Uber-vs-Anthropic tension in its own extraction.
   The Assayer or Smith may reach a different conclusion on either.
4. **Confidence calibration: settled.** Nearly every claim in this note is
   a first-party, non-interpretive description of a shipping product
   feature's exact mechanics (enforcement timing, reset schedule, API
   field names, error codes), verified verbatim against directly-fetched
   raw HTML/JSON rather than an AI-summarized intermediate. The two pages
   (changelog and reference doc) are internally consistent everywhere they
   overlap and the reference page (updated June 20, 2026, eleven days
   after the changelog) is treated as the more authoritative and current
   statement of behavior where it adds detail the changelog omits (Claims
   2, 6, 7, 8, 9).
