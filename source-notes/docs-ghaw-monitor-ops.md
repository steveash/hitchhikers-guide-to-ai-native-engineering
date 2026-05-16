---
source_url: https://github.github.com/gh-aw/patterns/monitor-ops
source_type: docs
title: "GitHub Agentic Workflows: MonitorOps Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-16
last_checked: 2026-05-16
status: current
confidence_overall: settled
issue: "#769"
---

# GitHub Agentic Workflows: MonitorOps Pattern

> Canonical design-patterns page for the MonitorOps pattern — a scheduled
> workflow that inspects other agentic workflows, publishes observability
> reports, and escalates recurring failures or waste; the page at
> `patterns/agentic-ops` now redirects here, confirming this as the current
> authoritative URL; the dense implementation details (reference implementation
> YAML, token anti-patterns, cost thresholds) were captured in
> `docs-ghaw-agentic-ops.md` (issue #552) when the page was at its prior URL.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `patterns/` section —
  specifically the `patterns/monitor-ops` page, which as of 2026-05-16 is the
  canonical URL; the prior URL `patterns/agentic-ops` issues an HTTP redirect
  to this location. The page appears in the site's "Design Patterns" sidebar
  under the official name "MonitorOps". Patterns pages are practitioner
  implementation references, distinct from the conceptual `introduction/` pages
  and the practitioner `guides/` section.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team
  (GitHub Next / Microsoft Research — the same team behind Peli de Halleux's
  "Agent Factory" blog series, the `gh aw` CLI, and all other `patterns/`
  pages in the corpus). The pattern description is authoritative for the
  `gh aw` platform. Claims do not automatically generalize to non-`gh-aw`
  monitoring systems without qualification.
- **Scope**: Covers the MonitorOps design pattern at the conceptual level:
  trigger condition, what the pattern does, four-step typical workflow,
  applicability criteria, and related documentation links. Does NOT contain
  YAML configuration blocks, CLI command examples, or reference implementation
  code (those are in the `githubnext/agentic-ops` repository, documented in
  `docs-ghaw-agentic-ops.md`). The page is concise (~350 words of content)
  and refers readers to `githubnext/agentic-ops` for the reference
  implementation.

## Extracted Claims

### Claim 1: MonitorOps is a formally named gh-aw design pattern for scheduled workflows that inspect other agentic workflows, summarize what happened, and escalate unusual cost or failure patterns

- **Evidence**: Opening trigger sentence on the pattern page — the canonical
  definition of the pattern as it appears in the current sidebar-listed
  "MonitorOps" entry.
- **Confidence**: settled (first-party documentation; the pattern is formally
  named, defined, and listed in the `patterns/` sidebar under "MonitorOps")
- **Quote**: "Use this pattern when you want a scheduled workflow to inspect
  other agentic workflows, summarize what happened, and escalate unusual cost
  or failure patterns."
- **Our assessment**: The renaming from "Agentic Ops" to "MonitorOps" is an
  editorial decision by the gh-aw team that signals how they want practitioners
  to think about the pattern: the name emphasizes *monitoring operations* (the
  intent) rather than *agentic operations* (the mechanism). The pattern is
  positioned in the sidebar alongside BatchOps, DailyOps, IssueOps, and other
  named operational patterns — it is a peer in the pattern taxonomy, not a
  subcategory of observability tooling. For Ch02 (Harness Engineering): refer
  to this pattern by its current official name "MonitorOps" rather than
  "Agentic Ops."

### Claim 2: The pattern reviews workflow logs across a repository, classifies notable behavior, and publishes a structured report — the observatory concept made installable

- **Evidence**: "What this pattern does" section of the page. Consistently
  appears on the current page at the canonical URL.
- **Confidence**: settled (first-party documentation)
- **Quote**: "This pattern reviews workflow logs across a repository, classifies
  notable behavior, and publishes a structured report."
- **Our assessment**: The "classifies notable behavior" language is architecturally
  important: this is not a passive log aggregator but a classification agent
  that applies qualitative assessment to fleet activity. The "structured report"
  framing positions it alongside DataOps-style patterns. For Ch02: document
  MonitorOps as a classification + publication pattern, not just a monitoring
  script — the agent reads, judges, and reports, rather than simply forwarding
  raw logs.

### Claim 3: The pattern creates a durable operational record for repository-wide monitoring, replacing ad hoc inspection of individual workflow runs

- **Evidence**: "What this pattern does" section, second paragraph.
- **Confidence**: settled (first-party documentation)
- **Quote**: "This pattern is useful for repository-wide monitoring because it
  creates a durable operational record instead of relying on ad hoc inspection
  of individual workflow runs."
- **Our assessment**: The "durable operational record" framing is the key
  design principle: MonitorOps exists to replace the manual practice of
  individually reviewing each workflow run in the GitHub Actions UI. At low
  volume (a repository with two workflows) this is practical; at high volume
  (50+ workflows across multiple teams) it is not. The durable record makes
  trends visible that would be invisible from individual run inspection. For
  Ch02: position MonitorOps as the operational maturity step that teams take
  when ad hoc run inspection becomes impractical.

### Claim 4: Detection targets are repeated failures, abnormal token consumption, and other unhealthy patterns — with escalation into GitHub issues for follow-up

- **Evidence**: "What this pattern does" section, first paragraph continuation.
- **Confidence**: settled (first-party documentation)
- **Quote**: "When it detects repeated failures, abnormal token consumption, or
  other unhealthy patterns, it can escalate those findings into issues for
  follow-up."
- **Our assessment**: The three detection classes (failures, token consumption,
  "other unhealthy patterns") correspond to distinct monitoring concerns:
  reliability, cost/efficiency, and open-ended anomaly detection. The escalation
  path (findings → GitHub issues) is the canonical escalation mechanism across
  the gh-aw pattern library. For Ch03 (Safety and Verification): the three
  detection classes should map to distinct thresholds and escalation paths —
  repeated failures need immediate attention; abnormal token consumption is a
  cost concern that can be addressed on a slower cadence.

### Claim 5: The MonitorOps workflow follows four sequential steps: schedule → analyze → report to durable destination → open/update issues at threshold

- **Evidence**: "Typical workflow" section, four bullet points.
- **Confidence**: settled (first-party documentation)
- **Quote**: "Run on a schedule to collect recent workflow activity." /
  "Analyze logs, costs, and failure signals across runs." / "Post a summary
  report to a GitHub Discussion or another durable destination." / "Open or
  update issues when the same problem crosses a threshold."
- **Our assessment**: The four-step structure is a general-purpose observability
  loop applicable beyond gh-aw: collect → analyze → report → escalate. The
  "when the same problem crosses a threshold" qualifier on the escalation step
  is important: routine anomalies should not generate issues every run;
  only persistent or threshold-crossing problems warrant issue creation. This
  prevents the issue tracker from filling with transient noise. For Ch04
  (Multi-agent orchestration): the four-step loop is the standard template
  for any meta-agent workflow in a fleet.

### Claim 6: The applicability condition is repositories with sufficient workflow activity to justify automated summaries, or multi-team repositories requiring shared visibility into failures and waste

- **Evidence**: "When to use it" section, two sentences.
- **Confidence**: settled (first-party documentation)
- **Quote**: "Use this pattern when a repository has enough workflow activity
  that maintainers need a regular summary instead of checking each run
  manually. It also helps when workflows span multiple teams and failures or
  waste need to be surfaced in a shared location."
- **Our assessment**: The two applicability conditions address different
  motivations: (1) volume — when individual run inspection becomes impractical,
  (2) coordination — when failures need to be visible across team boundaries.
  The second condition is subtly important: even a small repository with few
  workflows may benefit from MonitorOps if failures in one team's workflows
  affect another team. "Failures or waste" is the framing — cost waste is
  treated as an equally valid trigger for shared visibility as reliability
  failures. For Ch05 (Team Adoption): document both applicability conditions
  as adoption triggers; the multi-team condition may fire earlier than the
  volume condition for cross-functional organizations.

### Claim 7: The `patterns/agentic-ops` URL now redirects to `patterns/monitor-ops`, confirming the pattern was renamed from "Agentic Ops" to "MonitorOps"

- **Evidence**: HTTP redirect observed when fetching
  `https://github.github.com/gh-aw/patterns/agentic-ops` — the response
  includes `Redirecting to: /gh-aw/patterns/monitor-ops/` and the canonical
  URL meta tag is `https://github.github.com/gh-aw/patterns/monitor-ops/`.
  The design patterns sidebar lists the entry as "MonitorOps", not "Agentic Ops".
- **Confidence**: settled (HTTP redirect is authoritative; sidebar listing
  is the current official name)
- **Quote**: (no direct quote; HTTP redirect response is the evidence)
- **Our assessment**: This rename has a practical implication for the corpus:
  `docs-ghaw-agentic-ops.md` (issue #552) was extracted from the old URL
  `patterns/agentic-ops` and the source_url in that note reflects the old
  name. The quotes in that note are confirmed verbatim matches to the current
  page content, so the extraction remains accurate — only the URL needs
  updating. For the guide and future source notes: use "MonitorOps" as the
  official name for this pattern. Any guide chapter that cites
  `docs-ghaw-agentic-ops.md` should reference the pattern as "MonitorOps"
  and note the current URL.

## Concrete Artifacts

### Full Page Content (verbatim, as of 2026-05-16)

From `https://github.github.com/gh-aw/patterns/monitor-ops`:

```
# MonitorOps

Use this pattern when you want a scheduled workflow to inspect other agentic
workflows, summarize what happened, and escalate unusual cost or failure patterns.

The agentic-ops repository provides the reference implementation for this approach.

## What this pattern does

This pattern reviews workflow logs across a repository, classifies notable
behavior, and publishes a structured report. When it detects repeated failures,
abnormal token consumption, or other unhealthy patterns, it can escalate those
findings into issues for follow-up.

This pattern is useful for repository-wide monitoring because it creates a durable
operational record instead of relying on ad hoc inspection of individual workflow runs.

## Typical workflow

- Run on a schedule to collect recent workflow activity.
- Analyze logs, costs, and failure signals across runs.
- Post a summary report to a GitHub Discussion or another durable destination.
- Open or update issues when the same problem crosses a threshold.

## When to use it

Use this pattern when a repository has enough workflow activity that maintainers
need a regular summary instead of checking each run manually. It also helps when
workflows span multiple teams and failures or waste need to be surfaced in a
shared location.

## Related documentation

- Monitoring with Projects: for durable tracking with Projects and safe outputs
- OpenTelemetry: for enriching workflow telemetry
- Audit Commands: for investigating individual runs and regressions
```

Reference implementation: https://github.com/githubnext/agentic-ops

### URL Redirect Evidence

```
Request:  GET https://github.github.com/gh-aw/patterns/agentic-ops
Response: Redirecting to: /gh-aw/patterns/monitor-ops/
Canonical: https://github.github.com/gh-aw/patterns/monitor-ops/
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-agentic-ops.md` Claims 1–5: All five quotes in those claims
    appear verbatim on the current `patterns/monitor-ops` page, confirming
    that `docs-ghaw-agentic-ops.md` (extracted 2026-05-07 from
    `patterns/agentic-ops`) was documenting the same page content that now
    lives at `patterns/monitor-ops`. The redirect proves the equivalence.
    Specifically:
    - Claim 1 here (Claim 1 there): both quote the opening trigger sentence
      exactly
    - Claim 2 here (Claim 2 there): "This pattern reviews workflow logs across
      a repository, classifies notable behavior, and publishes a structured
      report." — verbatim match
    - Claim 4 here (Claim 3 there): "repeated failures, abnormal token
      consumption, or other unhealthy patterns" — verbatim match
    - Claim 3 here (Claim 4 there): "a durable operational record" fragment —
      verbatim match (this note adds the full surrounding sentence)
    - Claim 6 here (Claim 5 there): "Use this pattern when a repository has
      enough workflow activity that maintainers need a regular summary instead
      of checking each run manually." — verbatim match; this note adds the
      second sentence from the same section that Claim 5 did not capture.
  - `blog-ghaw-agent-observability.md` Claim 1 ("Observability isn't optional
    when you're running dozens of AI agents"): MonitorOps is the gh-aw
    pattern that operationalizes this principle — it is the installable form
    of the observatory architecture. Claim 8 ("The observatory represents a
    named, first-class architectural component of an agent factory, not an
    afterthought") is also corroborated: the MonitorOps entry in the official
    "Design Patterns" sidebar confirms observability is a first-class named
    pattern, not an afterthought.
  - `docs-ghaw-monitoring-patterns.md` Claim 9 (`gh aw logs --format markdown`
    inside a scheduled workflow for automated trend monitoring): the four-step
    typical workflow here (Claim 5) is the orchestration wrapper around the
    specific CLI command documented in Claim 9 there. MonitorOps is the pattern;
    `gh aw logs` is the tool.

- **Extends**:
  - `docs-ghaw-agentic-ops.md`: That note captured the same page content
    PLUS the full reference implementation from `githubnext/agentic-ops`
    (YAML frontmatter, token anti-patterns, cost thresholds, OTLP integration).
    This note confirms the current canonical URL and official name; `docs-ghaw-agentic-ops.md`
    remains the authoritative deep-extraction note for this pattern.
  - `blog-ghaw-agent-observability.md`: That post established the observatory
    as a named architectural layer with production metrics. MonitorOps is the
    installable, distributable form of that architecture — the patterns page
    formalizes it into a pattern that teams can adopt without building from
    scratch.
  - `docs-ghaw-monitoring-patterns.md`: That note covers the configuration-
    layer primitives (safe-outputs: `update-project`, `create-project-status-update`,
    `group-reports`, CLI commands). MonitorOps is the orchestration pattern
    that wraps those primitives into a fleet-monitoring workflow.

- **Contradicts**: None. No existing source note makes claims that conflict with
  the MonitorOps pattern description. The rename from "Agentic Ops" to
  "MonitorOps" is a naming change, not a design change — the underlying
  pattern is the same as what `docs-ghaw-agentic-ops.md` documented.

- **Novel**:
  - **Official rename to "MonitorOps"** (Claim 7): No existing source note
    documents the rename from "Agentic Ops" to "MonitorOps". The sidebar
    listing and the HTTP redirect are new information not present in
    `docs-ghaw-agentic-ops.md`. This is the first corpus entry that uses
    the current official name.
  - **Multi-team applicability condition** (Claim 6, second sentence): The
    "It also helps when workflows span multiple teams and failures or waste
    need to be surfaced in a shared location." sentence was not captured in
    `docs-ghaw-agentic-ops.md` Claim 5, which only quoted the first sentence
    of the "When to use it" section. The multi-team + waste visibility framing
    is a distinct and actionable criterion not previously documented.
  - **"Failures or waste" framing** (Claim 6): The word "waste" in "failures
    or waste need to be surfaced" treats cost waste as a first-class
    operational concern alongside reliability failures. No prior source note
    uses this framing explicitly.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Rename all references from "Agentic Ops" to "MonitorOps" — this is the
    current official name for the pattern. Any guide chapter that mentions the
    fleet-monitoring pattern should use "MonitorOps" per the current sidebar.
  - Document MonitorOps as the recommended operational pattern when manual
    per-run inspection becomes impractical. Add the two applicability
    conditions (volume threshold and multi-team visibility) as concrete
    adoption triggers. The "multi-team" condition should be highlighted — it
    can apply even to small repositories.

- **Chapter 04 (Multi-agent orchestration)**:
  - The MonitorOps four-step loop (collect → analyze → report → escalate at
    threshold) is the canonical orchestration template for any fleet-monitoring
    meta-agent. Add it as the standard pattern template for workflows that
    observe other workflows — regardless of whether teams use the gh-aw
    reference implementation.

- **Chapter 05 (Team Adoption)**:
  - The "failures or waste need to be surfaced in a shared location" language
    addresses the multi-team coordination case. Document this as a distinct
    adoption trigger: even teams with low workflow volume may benefit from
    MonitorOps if failures in one team's workflows are invisible to other teams.

- **Corpus maintenance**:
  - Update `docs-ghaw-agentic-ops.md` frontmatter `source_url` from
    `https://github.github.com/gh-aw/patterns/agentic-ops` to
    `https://github.github.com/gh-aw/patterns/monitor-ops` to reflect the
    current canonical URL. The old URL still redirects, so this is editorial
    rather than critical, but it should be corrected for accuracy.

## Extraction Notes

1. **URL redirect confirmed**: `patterns/agentic-ops` issues an HTTP redirect
   to `patterns/monitor-ops`. The canonical meta tag on both the redirect
   response and the destination page confirms the current URL is
   `https://github.github.com/gh-aw/patterns/monitor-ops/`.

2. **Page is very brief**: The substantive content is approximately 350 words
   (five sections). There are no YAML code blocks, CLI commands, or embedded
   examples on the pattern page itself. All implementation details (reference
   workflows, token anti-patterns, cost thresholds) are in the `githubnext/agentic-ops`
   repository, which was extracted in `docs-ghaw-agentic-ops.md`.

3. **All quotes verified against raw page content**: The HTML was fetched via
   `curl` and the text was extracted directly from the page's `<article>` element.
   All quotes in this note are verbatim from that extraction. The quotes in
   `docs-ghaw-agentic-ops.md` Claims 1–5 were also verified against the same
   raw content and confirmed as exact matches.

4. **`docs-ghaw-agentic-ops.md` overlap is comprehensive**: That note
   documented the pattern page content (Claims 1–5) plus the full reference
   implementation (Claims 6–13). This note adds the URL rename evidence
   (Claim 7) and the second sentence of the "When to use it" section (part
   of Claim 6) — the only content not captured in the prior extraction.

5. **No contradictions filed**: No claims in this source materially oppose
   existing source notes at the MINER.md §4a filing threshold. The rename
   does not change the pattern's design.

6. **Related documentation links**: The page links to "Monitoring with Projects"
   (→ `docs-ghaw-monitoring-patterns.md`), "OpenTelemetry" (→ not yet
   documented in detail in the corpus), and "Audit Commands" (→
   `docs-ghaw-audit-with-agents.md`). These links corroborate the
   cross-references noted above.
