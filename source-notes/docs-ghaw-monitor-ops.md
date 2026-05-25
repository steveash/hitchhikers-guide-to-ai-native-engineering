---
source_url: https://github.github.com/gh-aw/patterns/monitor-ops
source_type: docs
title: "GitHub Agentic Workflows: MonitorOps Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-25
last_checked: 2026-05-25
status: current
confidence_overall: emerging
issue: "#769"
---

# GitHub Agentic Workflows: MonitorOps Pattern

> Canonical URL and updated text for the pattern previously documented as
> "Agentic Ops" — the page at `patterns/agentic-ops` now redirects here;
> the pattern is officially named "MonitorOps," the pattern description
> explicitly names "workflow logs and auditing" as the inspection mechanism,
> and the "When to use it" section adds the multi-team applicability condition
> as integrated prose (not a separate bullet); the page also adds BatchOps,
> Cache Memory, and Concurrency as related patterns.

## Source Context

- **Type**: docs (GitHub Agentic Workflows `patterns/monitor-ops` page — a
  practitioner implementation reference in the `patterns/` section, between
  MemoryOps and MultiRepoOps in the sidebar navigation. This is the canonical
  successor to the `patterns/agentic-ops` page documented in
  `docs-ghaw-agentic-ops.md`; the old URL now issues an HTTP redirect to this
  location.)
- **Author credibility**: First-party from the GitHub Agentic Workflows team
  (GitHub Next / Microsoft Research — the same team behind Peli de Halleux's
  "Agent Factory" blog series, the `gh aw` CLI, and all other `patterns/`
  pages in the corpus). YAML configs, CLI commands, and field schemas are
  authoritative for the `gh aw` platform. Claims about the MonitorOps design
  (scope, when to use, applicability conditions) do not automatically
  generalize to non-`gh-aw` monitoring systems without qualification.
- **Scope**: Covers the MonitorOps design pattern — its purpose, what it does,
  the four-step typical workflow, when to use it, and links to related
  documentation including a reference implementation. Does NOT contain YAML
  workflow frontmatter, CLI command tables, or workflow specs — those are in
  the reference implementation repository (`githubnext/agentic-ops`, documented
  in depth in `docs-ghaw-agentic-ops.md`). The pattern page is concise (~300
  words); all reference-implementation depth lives in the prior extraction.

## Extracted Claims

### Claim 1: The pattern is officially renamed "MonitorOps"; the old `patterns/agentic-ops` URL now redirects to `patterns/monitor-ops`

- **Evidence**: The page title is "MonitorOps | GitHub Agentic Workflows";
  sidebar navigation shows "MonitorOps" between MemoryOps and MultiRepoOps.
  A direct fetch of `https://github.github.com/gh-aw/patterns/agentic-ops`
  returns a redirect notice: "Redirecting from `/gh-aw/patterns/agentic-ops/`
  to `/gh-aw/patterns/monitor-ops/`."
- **Confidence**: settled (first-party page title and verified redirect)
- **Quote**: (no prose quote; the evidence is the page title and redirect
  behavior, both confirmed)
- **Our assessment**: The rename matters for guide maintenance: any guide
  chapters or source notes that link to or cite `patterns/agentic-ops` should
  be updated to the canonical `patterns/monitor-ops` URL. The reference
  implementation at `githubnext/agentic-ops` keeps the old name — only the
  pattern page was renamed. `docs-ghaw-agentic-ops.md`'s `source_url` field
  should be updated to reflect the current canonical URL.

### Claim 2: MonitorOps enables scheduled workflows to inspect other agentic workflows using workflow logs and auditing — the "using workflow logs and auditing" phrase is new vs the prior agentic-ops extraction

- **Evidence**: Opening paragraph of the MonitorOps pattern page.
- **Confidence**: settled (first-party, verbatim from the page)
- **Quote**: "Use this pattern when you want a scheduled workflow to inspect
  other agentic workflows using workflow logs and auditing, summarize what
  happened, and escalate unusual cost or failure patterns."
- **Our assessment**: The phrase "using workflow logs and auditing" is the
  notable addition vs the prior extraction in `docs-ghaw-agentic-ops.md`
  Claim 1 (which quoted the same sentence without those words). This
  makes the inspection mechanism explicit: MonitorOps agents consume
  `gh aw logs` output and `gh aw audit` output, not arbitrary telemetry
  sources. The addition is consistent with the reference implementation
  which uses `gh aw logs --engine copilot --start-date -1d --json` as its
  primary data source. The old quote is still accurate to the old page
  text; this quote reflects the current canonical wording.

### Claim 3: MonitorOps reviews workflow logs, classifies notable behavior, publishes structured reports, escalates findings into issues, and creates a "durable operational record"

- **Evidence**: "What this pattern does" section of the page, full paragraph.
- **Confidence**: settled (first-party documentation)
- **Quote**: "This pattern reviews workflow logs across a repository, classifies
  notable behavior, and publishes a structured report. When it detects repeated
  failures, abnormal token consumption, or other unhealthy patterns, it can
  escalate those findings into issues for follow-up. This pattern is useful for
  repository-wide monitoring because it creates a durable operational record
  instead of relying on ad hoc inspection of individual workflow runs."
- **Our assessment**: This is an expanded version of `docs-ghaw-agentic-ops.md`
  Claim 2's quote ("This pattern reviews workflow logs across a repository,
  classifies notable behavior, and publishes a structured report."). The two
  new sentences are now verbatim on the page: the escalation mechanism (findings
  → issues for follow-up) and the rationale (durable operational record vs ad
  hoc inspection). The phrase "durable operational record" was previously cited
  in `docs-ghaw-agentic-ops.md` Claim 4 but only as a two-word fragment;
  here it appears in its full explanatory context. For Ch02 (Harness
  Engineering): this full paragraph is the authoritative definition of
  MonitorOps and should be cited in preference to the shorter prior quote.

### Claim 4: Detection targets remain unchanged: repeated failures, abnormal token consumption, and other unhealthy patterns

- **Evidence**: Second sentence of "What this pattern does" section.
- **Confidence**: settled (first-party; consistent with `docs-ghaw-agentic-ops.md`
  Claim 3)
- **Quote**: "repeated failures, abnormal token consumption, or other unhealthy
  patterns"
- **Our assessment**: The three detection signal classes are unchanged from the
  prior extraction. This corroborates `docs-ghaw-agentic-ops.md` Claim 3
  verbatim.

### Claim 5: The typical workflow is a four-step sequence: collect → analyze → post report → escalate to issues

- **Evidence**: "Typical workflow" numbered list on the pattern page.
- **Confidence**: settled (first-party)
- **Quote**: (no single sentence; see Concrete Artifacts for the full
  four-step list)
- **Our assessment**: The four-step workflow is identical to the four steps
  documented in `docs-ghaw-agentic-ops.md` Concrete Artifacts section.
  The steps have not changed with the rename. This corroborates the prior
  extraction.

### Claim 6: Two distinct applicability conditions: volume condition (enough workflow activity) AND multi-team condition (failures need shared visibility across teams)

- **Evidence**: "When to use it" section of the pattern page, full paragraph.
- **Confidence**: settled (first-party; both conditions stated explicitly in
  the same paragraph)
- **Quote**: "Use this pattern when a repository has enough workflow activity
  that maintainers need a regular summary instead of checking each run
  manually. It also helps when workflows span multiple teams and failures or
  waste need to be surfaced in a shared location."
- **Our assessment**: The first sentence matches `docs-ghaw-agentic-ops.md`
  Claim 5's quote exactly. The second sentence — "It also helps when workflows
  span multiple teams and failures or waste need to be surfaced in a shared
  location" — is now confirmed verbatim from the page. In the prior extraction,
  the multi-team condition was captured in the Our Assessment of Claim 5 but
  not as a direct quote. This source note provides the verbatim confirmation.
  The phrase "failures or waste" is the specific phrasing — "waste" (token
  overconsumption) joins "failures" as the co-equal second dimension of what
  MonitorOps surfaces in multi-team environments. For Ch05 (Team Adoption):
  document both conditions as the adoption decision criteria, using this
  two-sentence paragraph as the authoritative guidance.

### Claim 7: The MonitorOps page links to BatchOps and Concurrency as related patterns — additions not present in the prior agentic-ops extraction

- **Evidence**: "Related Documentation" section of the pattern page.
- **Confidence**: settled (page content)
- **Quote**: (Related documentation entries verbatim)
  - BatchOps — "Process large volumes in parallel chunks"
  - Concurrency — "Prevent overlapping workflow runs"
  - Cache Memory — "Persistent state across runs"
  - Audit Commands — "Investigate individual runs and regressions"
  - OpenTelemetry — "Workflow telemetry and spans"
  - Monitoring with Projects — "Durable tracking with Projects"
- **Our assessment**: BatchOps and Concurrency are new related-pattern links
  not listed in the old agentic-ops extraction. Their presence is informative:
  — **BatchOps**: MonitorOps may benefit from processing large volumes of
    workflow logs in parallel chunks, linking the pattern to the batch
    processing primitives.
  — **Concurrency**: MonitorOps workflows should prevent overlapping runs
    (a monitoring run for day N should not start while day N-1 is still
    running). The Concurrency link confirms this is a practical concern.
  — **Cache Memory**: Persistent state across runs (for rolling baselines
    and trend data); this is the per-workflow mechanism vs. the `repo-memory`
    used in the reference implementation for cross-workflow shared state.
  For Ch02: the Concurrency link for MonitorOps should be documented as a
  recommended config addition to any monitoring workflow, preventing the
  overlapping-run scenario that could produce duplicate reports or corrupt
  rolling baselines.

### Claim 8: The reference implementation for MonitorOps remains at `https://github.com/githubnext/agentic-ops`

- **Evidence**: Reference implementation callout on the pattern page.
- **Confidence**: settled (direct URL on the page)
- **Quote**: "The [agentic-ops repository](https://github.com/githubnext/agentic-ops)
  provides the reference implementation for this approach."
- **Our assessment**: The reference implementation repository has not been
  renamed (only the pattern page was renamed). The two production workflows
  (`copilot-token-audit` and `copilot-token-optimizer`) are installed via
  `gh aw add githubnext/agentic-ops/copilot-token-audit
  githubnext/agentic-ops/copilot-token-optimizer`. The full reference
  implementation is documented in depth in `docs-ghaw-agentic-ops.md`
  Claims 6–13 and Concrete Artifacts.

## Concrete Artifacts

### Pattern Page: Canonical Definition and Four-Step Workflow

From `https://github.github.com/gh-aw/patterns/monitor-ops` (fetched 2026-05-25):

```
Opening (trigger condition):
  "Use this pattern when you want a scheduled workflow to inspect other agentic
  workflows using workflow logs and auditing, summarize what happened, and
  escalate unusual cost or failure patterns."

What this pattern does (full paragraph):
  "This pattern reviews workflow logs across a repository, classifies notable
  behavior, and publishes a structured report. When it detects repeated
  failures, abnormal token consumption, or other unhealthy patterns, it can
  escalate those findings into issues for follow-up. This pattern is useful
  for repository-wide monitoring because it creates a durable operational
  record instead of relying on ad hoc inspection of individual workflow runs."

Typical workflow (numbered steps):
  1. Run on a schedule to collect recent workflow activity.
  2. Analyze logs, costs, and failure signals across runs.
  3. Post a summary report to a GitHub Discussion or another durable
     destination.
  4. Open or update issues when the same problem crosses a threshold.

When to use it (full paragraph):
  "Use this pattern when a repository has enough workflow activity that
  maintainers need a regular summary instead of checking each run manually.
  It also helps when workflows span multiple teams and failures or waste need
  to be surfaced in a shared location."

Reference implementation:
  "The [agentic-ops repository](https://github.com/githubnext/agentic-ops)
  provides the reference implementation for this approach."
```

### Redirect Evidence

```
Fetch of https://github.github.com/gh-aw/patterns/agentic-ops returns:
  "Redirecting from `/gh-aw/patterns/agentic-ops/` to
   `/gh-aw/patterns/monitor-ops/`"
```

### Related Documentation (verbatim link text and descriptions)

```
- BatchOps — "Process large volumes in parallel chunks"
- Audit Commands — "Investigate individual runs and regressions"
- OpenTelemetry — "Workflow telemetry and spans"
- Cache Memory — "Persistent state across runs"
- Concurrency — "Prevent overlapping workflow runs"
- Monitoring with Projects — "Durable tracking with Projects"
```

## Cross-References

- **Corroborates**:
  - `docs-ghaw-agentic-ops.md` Claim 3 (detection targets: repeated failures,
    abnormal token consumption, other unhealthy patterns): The MonitorOps page
    uses identical wording — the three detection classes are confirmed unchanged
    across the URL rename.
  - `docs-ghaw-agentic-ops.md` Claim 5 (applicability: "enough workflow
    activity that maintainers need a regular summary instead of checking each
    run manually"): The volume condition quote is verbatim identical to the
    MonitorOps page's first sentence in "When to use it."
  - `docs-ghaw-monitoring-patterns.md` Claim 9 (`gh aw logs` inside a
    scheduled workflow for automated trend monitoring): The MonitorOps opening
    now explicitly names "workflow logs and auditing" as the inspection
    mechanism, confirming that `gh aw logs` and `gh aw audit` are the canonical
    tools for MonitorOps agents.

- **Extends**:
  - `docs-ghaw-agentic-ops.md`: That note is the deep extraction of the same
    page's prior form (URL: `patterns/agentic-ops`). This note documents the
    canonical URL change, the updated pattern description text, and the expanded
    "When to use it" paragraph. The prior extraction's 13 claims and Concrete
    Artifacts (YAML frontmatter, token-efficiency anti-patterns, cost anomaly
    thresholds, OTLP integration) are all from the reference implementation —
    not the pattern page itself — and remain valid. This note covers what
    changed on the pattern page; that note covers what the reference
    implementation specifies.
  - `blog-ghaw-agent-observability.md`: That post describes the observatory
    architecture at scale. MonitorOps is the formalized, installable pattern
    that operationalizes the observatory concept described in the blog.

- **Contradicts**: None. The MonitorOps page is an updated/renamed version of
  the agentic-ops page. All claims are consistent with or extend the prior
  extraction. No material opposition with any existing source note.

- **Novel**:
  - **Verbatim confirmation of the multi-team applicability sentence** (Claim 6):
    "It also helps when workflows span multiple teams and failures or waste need
    to be surfaced in a shared location." The prior extraction noted the
    multi-team condition in its assessment but did not have it as a direct
    quote; this note provides the verbatim text.
  - **"Failures or waste" as the co-equal dual dimension of multi-team
    visibility** (Claim 6): The word "waste" (token overconsumption) is
    explicitly named alongside "failures" as what needs to be surfaced across
    teams. No existing source note uses this phrasing.
  - **Canonical name "MonitorOps" confirmed** (Claim 1): Prior corpus sources
    referenced the pattern as "Agentic Ops." This note establishes "MonitorOps"
    as the canonical name, with `patterns/agentic-ops` confirmed as a redirect.
  - **"Using workflow logs and auditing" addition** (Claim 2): The updated
    opening paragraph explicitly names the inspection tools. No prior source
    note included this phrase in the trigger condition.
  - **BatchOps and Concurrency as related patterns** (Claim 7): Neither
    BatchOps nor Concurrency appeared in the related-docs section of the old
    agentic-ops page. Their addition suggests the platform team views MonitorOps
    as needing parallel-chunk log processing (BatchOps) and overlap prevention
    (Concurrency) as companion patterns.
  - **"Durable operational record" in full sentence context** (Claim 3):
    "This pattern is useful for repository-wide monitoring because it creates a
    durable operational record instead of relying on ad hoc inspection of
    individual workflow runs." Prior extraction cited only "a durable
    operational record" as a two-word fragment (Claim 4). This note provides
    the complete explanatory sentence.

## Guide Impact

- **Chapter 02 (Harness Engineering)**:
  - Update the canonical URL for the MonitorOps/Agentic Ops pattern from
    `patterns/agentic-ops` to `patterns/monitor-ops` in any guide text.
  - Update the pattern's official name to "MonitorOps" where cited.
  - Add the full "What this pattern does" paragraph (Claim 3 quote) as the
    authoritative definition of MonitorOps, replacing the shorter one-sentence
    definition from the prior extraction.
  - Add Concurrency as a recommended companion config for MonitorOps workflows
    to prevent overlapping monitoring runs (per Claim 7 — the pattern page
    explicitly links to Concurrency as a related concern).

- **Chapter 04 (Multi-agent orchestration patterns)**:
  - Document MonitorOps as the canonical fleet-monitoring orchestrator pattern.
    The updated page text makes explicit that MonitorOps is a "repository-wide
    monitoring" mechanism — scope is the repository, not a single workflow.
    This positions it as the repository-level meta-agent that oversees all
    other agent workflows.

- **Chapter 05 (Team Adoption)**:
  - Use the two-sentence "When to use it" paragraph (Claim 6) as the
    adoption decision guide: volume condition (maintainers need regular
    summaries) OR multi-team condition (failures or waste need shared
    visibility). Document both as legitimate triggers; prior guide drafts
    may only reflect the volume condition.

## Extraction Notes

1. **WebFetch processes through AI model**: The `WebFetch` tool processes page
   content through an AI model before returning results. Two fetch passes were
   performed with different prompts to maximize verbatim coverage. Quotes are
   cross-validated for consistency across passes before being cited. Where a
   passage appeared consistently across passes in the same form, it is cited
   as a direct quote.

2. **Redirect confirmed independently**: The redirect from `patterns/agentic-ops`
   to `patterns/monitor-ops` was confirmed by a separate WebFetch of the old
   URL, which returned the redirect notice verbatim.

3. **Pattern page is concise**: The MonitorOps pattern page is approximately
   300 words (consistent with other `patterns/` pages in the corpus). The
   detailed workflow specifications and YAML artifacts are in the reference
   implementation (`githubnext/agentic-ops`), which was thoroughly extracted
   in `docs-ghaw-agentic-ops.md`. This note focuses on the pattern page text
   only; the reference implementation extraction remains valid and complete.

4. **No contradictions filed**: Reviewed all claims against MINER.md §4a
   criteria. No claim in this source materially opposes any existing source
   note. All differences from the prior extraction are additive (new sentences,
   new related-pattern links, name change) rather than opposing.
