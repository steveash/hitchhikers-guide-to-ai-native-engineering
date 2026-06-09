---
source_url: https://claude.com/blog/observability-for-developers-building-connectors
source_type: blog-post
title: "Observability for developers building connectors"
author: Anthropic (no individual byline)
date_published: 2026-06-08
date_extracted: 2026-06-09
last_checked: 2026-06-09
status: current
confidence_overall: settled
issue: "#1124"
---

# Observability for developers building connectors

> First-party Anthropic announcement of production observability tooling for
> MCP connector developers — a performance dashboard covering adoption metrics,
> error/latency diagnostics, and cross-product surface breakdowns, plus
> in-app directory submission — filling the operational monitoring gap that
> existing MCP coverage (blog-anthropic-mcp-production-agents.md) explicitly
> did not address.

## Source Context

- **Type**: blog-post (official claude.com/blog, June 8, 2026; no individual
  byline — published as Anthropic)
- **Author credibility**: First-party Anthropic content on claude.com — the
  same publishing channel as "Building agents that reach production systems
  with MCP" and other Anthropic practitioner guidance. Represents Anthropic's
  first-party documentation of new tooling released into public beta. The
  "over 300 connectors, millions of users daily" scale claim is an
  Anthropic-verified adoption signal from their own directory.
- **Scope**: Covers operator-side observability for MCP connectors that have
  been published to the Anthropic connector directory — specifically what
  metrics are available, how to access them, and how to submit new connectors
  in-app. Does NOT cover: how to build an MCP server (see
  `blog-anthropic-mcp-production-agents.md`), connector performance on
  self-hosted or private MCP deployments, observability for connectors not
  in the public directory, or observability for Claude Code harnesses
  (agent-level observability vs. connector-level observability).

## Extracted Claims

### Claim 1: Published MCP connectors now have a production dashboard showing performance across all Claude product surfaces, in public beta as of June 8, 2026

- **Evidence**: First-party product announcement. The feature is described as
  already live ("now have a dashboard"), available through Organization
  settings, and explicitly in public beta.
- **Confidence**: settled (first-party release announcement)
- **Quote**: "Published connectors in the directory now have a dashboard showing how they're performing across Claude product surfaces."
- **Our assessment**: This is the headline claim — the observability gap that
  existed for MCP connector developers before this release. Prior to this,
  developers building connectors had no structured way to see aggregate
  performance signals across the Claude user base. This dashboard changes
  the operational posture for connector development: it converts connector
  deployment from a "ship and hope" model into a monitored production system.
  The "across Claude product surfaces" framing is significant — metrics
  aggregate across all Claude access points (Claude.ai, Claude Code, Cowork,
  and future surfaces), not just one client.

### Claim 2: The dashboard exposes three adoption metrics — active users, total tool calls, and directory rank over time

- **Evidence**: First-party feature documentation with specific metric names.
- **Confidence**: settled (first-party release documentation)
- **Quote**: "Track adoption. Monitor active users, total tool calls, and directory rank over time."
- **Our assessment**: These three metrics give connector developers the same
  signals a SaaS product team would use to assess adoption health. Active
  users (stickiness), tool calls (engagement depth), and directory rank
  (relative position in the discovery surface) together allow
  developers to distinguish growing connectors from stagnating ones, and
  widely-discovered connectors from deeply-used ones. Directory rank over
  time is particularly useful: it tells developers whether their connector
  is gaining or losing visibility in the distribution channel.

### Claim 3: The dashboard provides a health score, per-tool error breakdowns, and latency metrics enabling precise debugging of connector failures

- **Evidence**: First-party feature documentation with specific signal names.
- **Confidence**: settled (first-party release documentation)
- **Quote**: "Diagnose errors and latency. See health score, error rates, and latency at a glance, with per-tool error breakdowns to pinpoint what's failing."
- **Our assessment**: The per-tool error breakdown is the most operationally
  valuable diagnostic signal described. Without it, a developer seeing a
  rising error rate would need to manually triage which of their connector's
  tools is failing. With per-tool breakdown, the failing tool is immediately
  identifiable. The "health score" is a roll-up signal that presumably
  aggregates error rate and latency into a single indicator — useful for
  quick triage ("is something wrong?") before drilling into the per-tool
  breakdown. The article does not define how health score is calculated,
  which is a gap for practitioners who need to understand its thresholds.

### Claim 4: Usage can be broken down by Claude product surface — specifically Claude, Claude Code, Cowork, and more

- **Evidence**: First-party feature documentation listing specific products.
- **Confidence**: settled (first-party enumeration of product surfaces)
- **Quote**: "Break down usage by product. Compare tool calls across Claude, Claude Code, Cowork, and more to understand where users are engaging."
- **Our assessment**: The multi-surface breakdown reveals something important
  about the MCP ecosystem structure: a single connector can be consumed by
  users on different Claude products, and usage patterns may differ
  substantially across surfaces. A connector optimized for Claude.ai
  conversational use may behave differently when called from Claude Code
  or Cowork automation contexts. The "and more" qualifier implies the
  product surface list is extensible — new Claude product surfaces will
  appear in this breakdown as they launch. For connector developers, this
  breakdown should inform how they prioritize tool design and which user
  journeys to optimize for.

### Claim 5: The Anthropic connector directory contains over 300 third-party connectors used by millions of people daily, establishing the scale of the MCP ecosystem

- **Evidence**: First-party Anthropic ecosystem scale claim.
- **Confidence**: settled (first-party verified count from Anthropic's own
  directory; the "millions of users daily" figure is a usage statistic
  Anthropic can verify from their own telemetry)
- **Quote**: "Connectors are built on the Model Context Protocol (MCP). There are over 300 third-party connectors in the directory, used by millions of people every day."
- **Our assessment**: The "millions of people every day" claim is the most
  striking signal in the post. It means the MCP connector ecosystem has
  reached mass-consumer scale, not just developer-preview scale. For connector
  developers, this scale creates both an opportunity (large potential user base
  for new connectors) and a reliability requirement (at millions-of-users scale,
  a connector with poor error handling will fail at volume and surface in the
  new error diagnostics dashboard). This claim corroborates and extends the
  `blog-anthropic-mcp-production-agents.md` Claim 4 adoption signal (300M SDK
  downloads/month) — both point to rapid MCP ecosystem growth, now confirmed
  at the user-facing level.

### Claim 6: In-app directory submission is now available — developers can submit MCP servers to the Anthropic connector directory directly within Claude, without an external process

- **Evidence**: First-party product announcement.
- **Confidence**: settled (first-party release announcement)
- **Quote**: "If you wish to submit your MCP server to the directory, you can now do so directly in Claude."
- **Our assessment**: Before this feature, the submission flow required
  navigating an external process outside of Claude. The in-app submission
  removes a workflow friction point for developers going from "building a
  connector" to "distributing a connector." The practical impact: the
  development, testing, and distribution cycle for MCP connectors can now
  be completed within the Claude product surface, reducing context-switching.
  This is a UX improvement for the connector ecosystem's supply side —
  it lowers the activation energy for developers to publish their work.

### Claim 7: The observability dashboard and in-app submission are available only to Team or Enterprise accounts with Admin/Owner access, or custom roles with Libraries permission on Enterprise plans

- **Evidence**: First-party access documentation.
- **Confidence**: settled (first-party release documentation)
- **Quote**: "a Team or Enterprise account with Admin or Owner access, or a custom role with the Libraries permission on Enterprise"
- **Our assessment**: The access gate is enterprise-oriented. This is expected
  given that the feature is aimed at connector *developers* rather than
  connector *users* — and connector developers who have published to the
  directory are likely operating at team or enterprise scale. The "Libraries
  permission" custom role is the most granular access path, allowing
  organizations to delegate connector management to a specific team without
  granting broader admin access. For practitioners: the observability features
  are not available on free or Pro plans, and require organization-level
  setup, not just individual user setup.

## Concrete Artifacts

### Dashboard Features Summary

```
# Connector Performance Dashboard (Public Beta, June 8, 2026)
# Source: "Observability for developers building connectors," Anthropic

ACCESS:
  Path: Organization settings → Directory section (public beta)
  Requires: Team or Enterprise account + Admin/Owner access
            OR Enterprise plan + custom role with Libraries permission

ADOPTION METRICS:
  "Track adoption. Monitor active users, total tool calls, and directory rank over time."

ERROR / LATENCY DIAGNOSTICS:
  "Diagnose errors and latency. See health score, error rates, and latency at a glance,
   with per-tool error breakdowns to pinpoint what's failing."

CROSS-PRODUCT SURFACE BREAKDOWN:
  "Break down usage by product. Compare tool calls across Claude, Claude Code,
   Cowork, and more to understand where users are engaging."

SCOPE:
  Applies to connectors published in the Anthropic connector directory.
  Directory: "over 300 third-party connectors...used by millions of people every day."
```

### In-App Submission Feature

```
# In-App MCP Directory Submission (Public Beta, June 8, 2026)
# Source: "Observability for developers building connectors," Anthropic

WHERE: Organization settings → Directory section
HOW:   "If you wish to submit your MCP server to the directory, you can now do so directly in Claude."
CONTEXT: Previously required external submission process.
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-mcp-production-agents.md` Claim 4 (MCP ecosystem adoption
    — 300M SDK downloads/month as of April 2026): This source adds a
    user-facing scale confirmation from June 2026: "millions of people every
    day" using connectors from the directory. The two signals together — SDK
    download volume and active user count — present a consistent picture of
    rapid MCP ecosystem growth. SDK downloads measure developer adoption;
    daily active users measure end-user adoption.
  - `blog-ghaw-agent-observability.md` Claim 1 ("Observability isn't optional
    when you're running dozens of AI agents"): The GitHub Agentic Workflows
    team's principle applies here at the connector level. Anthropic's
    dashboard launch reflects the same recognition: at millions-of-users scale,
    connector developers need structured observability to manage reliability.
    The gh-aw note covers agent-fleet observability; this source covers
    connector-level observability. Both document the same underlying imperative
    — instrument production AI systems — at different layers of the stack.

- **Extends**:
  - `blog-anthropic-mcp-production-agents.md`: That note (April 2026) covers
    how to *build* production MCP servers — design principles, token efficiency,
    auth patterns. It does NOT cover how to *monitor* them once deployed.
    This source fills the operational monitoring gap explicitly: it documents
    the signals available to connector developers after publishing. Together,
    the two sources give a complete picture: build a good connector
    (`blog-anthropic-mcp-production-agents.md`) then monitor it in production
    (this source).
  - `blog-ghaw-agent-observability.md`: The gh-aw note covers a three-tier
    observatory architecture (Metrics Collector, Portfolio Analyst, Audit
    Workflows) for internal agent fleets using the GitHub Actions platform.
    This source covers a different observability layer: Anthropic-managed
    dashboards for published connectors, accessed by connector developers
    through Organization settings. The two complement each other: gh-aw
    observability is DIY and fleet-internal; Anthropic's connector observability
    is managed and connector-external (you observe how the outside world uses
    your connector, not how your internal agent processes run).

- **Contradicts**: None identified. No existing source note makes claims
  about MCP connector observability that this source would oppose. The scope
  of this source (Anthropic-managed dashboard for published connectors) does
  not overlap with gh-aw's DIY observability pattern enough to create
  a contradiction.

- **Novel**:
  - **Connector-level observability as a first-class Anthropic product
    feature**: No prior source note documents Anthropic providing managed
    observability tooling for connector developers. This is new infrastructure
    in the MCP ecosystem — a monitoring layer that didn't exist before June
    2026.
  - **Per-tool error breakdowns as a debugging primitive**: The granularity of
    per-tool error diagnostics (vs. aggregate connector-level errors) is a
    novel debugging signal not described in any prior MCP-related source note.
  - **Cross-product surface usage breakdown (Claude, Claude Code, Cowork)**:
    No prior source documents tools for understanding how connector usage
    distributes across Claude product surfaces. This is the first corpus entry
    acknowledging that a single MCP connector may serve meaningfully different
    user populations across Claude products.
  - **Directory rank as an adoption metric**: Tracking directory rank over time
    as a connector health signal is not described in any prior source.
  - **In-app directory submission**: Streamlining the connector submission
    workflow into the Claude product surface is new to the corpus.
  - **Scale confirmation ("millions of people every day")**: This is the first
    user-facing scale figure for the MCP connector ecosystem in our corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering — production reliability)**: Add a
  section on MCP connector observability as a production concern. Currently
  the guide covers MCP server design (`blog-anthropic-mcp-production-agents.md`)
  but lacks guidance on monitoring deployed connectors. The dashboard features
  documented here — error rates, per-tool breakdowns, health score, latency —
  define the operational baseline connector developers should track.
  Recommend: once a connector is published to the directory, treat the
  health score and per-tool error breakdown as the primary reliability
  signals. Pair with the design principles from `blog-anthropic-mcp-production-agents.md`.

- **Chapter 04 (Context Engineering — extends MCP coverage)**: The
  cross-product surface breakdown (Claim 4) is relevant to context engineering
  because usage patterns on Claude.ai (conversational), Claude Code (agentic),
  and Cowork (automation) will differ. Connector developers should examine
  the product-surface breakdown to understand which tool calls dominate on
  which surface, then tune tool descriptions and response structures
  accordingly. A connector with high tool call volume on Claude Code should
  be optimized for programmatic consumption patterns; one with high volume
  on Claude.ai should be optimized for human-conversational contexts.

- **Chapter 05 (Team Adoption — operational governance)**: The access
  model (Claim 7) is governance-relevant. Organizations adopting MCP connectors
  should assign the Libraries permission custom role to their connector owners
  rather than granting Admin access broadly. The directory rank and adoption
  metrics can feed into team-level AI tooling investment decisions — connectors
  with low directory rank and low active users may not warrant continued
  maintenance investment.

## Extraction Notes

1. **Short feature-announcement article**: The source is a concise feature
   announcement (~5 min read) rather than a long-form tutorial or analysis post.
   It documents what features exist and how to access them, not deep rationale
   or design tradeoffs. Claims were fully exhausted at 7 extractions — the
   article is intentionally compact.

2. **Public beta caveat**: All features described are in public beta as of
   June 8, 2026. Feature scope, access requirements, and available metrics
   may change as the features move toward general availability.

3. **Health score calculation undocumented**: Claim 3 notes that the article
   does not define how the health score is computed. Practitioners who need to
   understand health score thresholds should consult Anthropic's support
   documentation or connector developer resources.

4. **WebFetch returns AI-summarized content**: The claude.com blog renders as
   a JavaScript SPA; WebFetch AI-summarizes rendered content. Three separate
   fetches were performed with targeted verbatim-extraction prompts to maximize
   quote fidelity. All quoted passages were verified across fetches for
   consistency. The direct quotes used in this note appeared consistently
   across all fetches.

5. **No contradictions to file**: Reviewed all existing MCP-related source
   notes (`blog-anthropic-mcp-production-agents.md`, `blog-bswen-mcp-token-cost.md`,
   `blog-ghaw-agent-observability.md`, `docs-ghaw-mcps.md`). No contradictions
   meeting the MINER.md §4a filing threshold were found. This source fills a gap
   in the corpus (connector-level observability) without conflicting with
   existing claims about MCP server design or agent-fleet observability.
