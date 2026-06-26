---
source_url: https://github.blog/changelog/2026-06-25-copilot-code-review-analysis-depth-and-efficiency-updates
source_type: docs
title: "Copilot code review: Analysis depth and efficiency updates"
author: GitHub (official changelog)
date_published: 2026-06-25
date_extracted: 2026-06-26
last_checked: 2026-06-26
status: current
confidence_overall: settled
issue: "#1319"
---

# Copilot Code Review: Analysis Depth and Efficiency Updates

> GitHub's June 25, 2026 changelog announcing two improvements to Copilot code review:
> a switch to CLI-based file exploration tools (grep, rg, glob, view) that yields a
> claimed ~20% cost reduction while maintaining review quality, and new org-level
> configurability for the Medium analysis depth tier with PR comment attribution —
> extending the per-repo Low/Medium configuration model with organizational governance
> and a quantified efficiency gain.

## Source Context

- **Type**: docs (GitHub official product changelog, June 25, 2026; approximately 250–350 words)
- **Author credibility**: GitHub engineering team announcing production feature updates.
  Authoritative for the existence of these features, the architectural change described, and
  the stated cost efficiency metric. The ~20% figure is a vendor claim validated internally
  ("both offline and online evaluation") — not independently verified by a third party.
- **Scope**: Two specific updates: (1) architectural shift to CLI-based file exploration tools
  with a quantified efficiency result, and (2) org-level Medium analysis depth defaults with
  PR comment attribution for organizations in the Medium public preview. Does NOT cover: which
  specific code review agent model changed behavior; whether the ~20% reduction applies
  uniformly across Low and Medium tiers or primarily to one; concrete latency improvements;
  or how the org-level depth default interacts with the runner lock introduced in the June 12
  changelog.

## Extracted Claims

### Claim 1: Copilot code review now uses CLI-based file tools — specifically grep, rg, glob, and view — from the Copilot CLI and SDK instead of prior custom file exploration utilities

- **Evidence**: Official GitHub product changelog describing the architectural change as the
  causal mechanism behind the efficiency gains.
- **Confidence**: settled (architectural fact stated in official changelog)
- **Quote**: (no direct quote; WebFetch returned AI-processed summaries — see Our assessment
  and Extraction Notes)
- **Our assessment**: WebFetch rendered this as: "The system now utilizes `grep`, `rg`, `glob`
  and `view` tools from the Copilot CLI and SDK instead of custom file exploration utilities."
  This represents a meaningful architectural convergence: code review now uses the same file
  exploration primitives available in the Copilot CLI/SDK rather than a bespoke implementation.
  For Ch02 (Harness Engineering): the code review pipeline shares file-tool primitives with
  the CLI agent — a design choice that simplifies maintenance and enables future CLI capability
  improvements to propagate to code review automatically.

### Claim 2: The switch to CLI-based file tools achieved approximately 20% reduction in Copilot code review costs while maintaining the same standard of review quality

- **Evidence**: Quantified vendor metric stated in the changelog, attributed to validation
  through offline and online evaluation.
- **Confidence**: emerging (vendor-provided metric stated as "approximately 20%"; no
  independent verification; quality measurement methodology not disclosed)
- **Quote**: "20% reduction in Copilot code review costs while maintaining the same standard
  of review quality"
- **Our assessment**: This is the first quantified efficiency metric for any architectural
  improvement to Copilot code review in the corpus. "Approximately 20%" signals an empirical
  estimate, not a theoretical bound. The qualifier "while maintaining the same standard of
  review quality" is a vendor assertion — the changelog does not define what quality standard
  is being maintained or how it was measured. Cost denominator is not specified: given that
  the change is to file exploration (the agentic tool-calling portion running on Actions), the
  reduction most plausibly refers primarily to GitHub Actions minutes consumed per review, not
  AI Credits. For Ch05 (Team Adoption): this figure provides a concrete data point for TCO
  recalculations, though teams cannot assume the 20% applies identically to their specific
  review workloads.

### Claim 3: The efficiency improvement was validated through both offline and online evaluation

- **Evidence**: Stated validation methodology in the changelog.
- **Confidence**: settled (validation approach stated in official changelog; specific
  methodology and metrics not disclosed)
- **Quote**: "both offline and online evaluation"
- **Our assessment**: "Offline evaluation" typically refers to benchmark testing against
  held-out data; "online evaluation" typically refers to production A/B testing or staged
  rollout monitoring. The dual-validation approach increases credibility of the ~20% figure
  (Claim 2) compared to offline-only claims. However, the specific evaluation design — what
  quality metrics were tracked, what baseline was used, what statistical significance was
  established — is not disclosed. For the guide: cite the dual-validation as evidence that
  GitHub tested the change before shipping, while noting specific methodology details are not
  public.

### Claim 4: The CLI tool integration enables a more focused code review where Copilot finds the code that matters more quickly

- **Evidence**: Changelog framing of why the architectural change produces efficiency gains.
- **Confidence**: anecdotal (vendor framing — plausible mechanism but causal attribution is
  not independently verified)
- **Quote**: "a more focused review where Copilot finds the code that matters, quickly"
- **Our assessment**: The efficiency gain is attributed to better file discovery. grep and rg
  are highly optimized, widely tested tools for finding relevant code in large repos; using
  them directly is more efficient than reimplementing file search logic in a custom utility.
  The "quickly" framing suggests latency improvement alongside cost reduction — though no
  specific latency metric is provided. For Ch02: this is the expected outcome of reusing
  proven Unix tools rather than custom implementations — a software engineering best practice
  applied at the AI agent architecture level.

### Claim 5: Organization administrators can now configure a default analysis depth (Medium or Low) for repositories within their organization, applying to repositories that have not set their own level

- **Evidence**: Official changelog announcing org-level analysis depth configuration for
  organizations in the Medium analysis depth public preview.
- **Confidence**: settled (product fact stated in official changelog)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: This extends the per-repository analysis depth configuration documented
  in `docs-github-copilot-code-review-skills-mcp-tier.md` (Claim 14: "Navigate to repository
  settings → Copilot → Code review → Review effort level") with an organizational-level default
  for unconfigured repositories. Prior to this, each repository required individual configuration —
  admins managing large repository fleets had to configure analysis depth per-repo or leave all
  repos at the default (Low). The org-level default enables fleet-wide analysis depth policy
  without per-repo admin overhead. For Ch02 (Harness Engineering): the analysis depth
  configuration surface now parallels the runner configuration surface from
  `docs-github-copilot-code-review-config-controls.md` Claims 1–2, where org-level defaults
  were introduced for runner type in June 12.

### Claim 6: Individual repositories can override the organizational default for analysis depth, retaining per-repo autonomy

- **Evidence**: Official changelog stating that repositories can override org-level defaults.
- **Confidence**: settled (product fact stated in official changelog)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The override capability maintains per-repository autonomy established in
  `docs-github-copilot-code-review-skills-mcp-tier.md` (Claim 14) while adding the org-level
  default layer. The resulting hierarchy is: org default (Low or Medium) → per-repo override.
  This is a less restrictive governance model than the runner lock documented in
  `docs-github-copilot-code-review-config-controls.md` (Claim 2), which allows org admins to
  prevent repository-level overrides entirely. The distinction is meaningful: runner type may
  have compliance implications (air-gap, network boundary) warranting lock enforcement; analysis
  depth is a cost/quality tradeoff that benefits from per-repo flexibility. For governance
  decisions: set the org default to match most repositories' needs, then override selectively
  for repositories with different complexity profiles.

### Claim 7: PR overview comments for Medium-depth reviews now display "Medium" attribution, enabling teams to verify at a glance which analysis level generated the review

- **Evidence**: Changelog announcing PR comment attribution as a new visibility feature for
  organizations in the Medium public preview.
- **Confidence**: settled (product fact stated in official changelog)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Prior to this, a PR reviewer looking at Copilot code review comments had
  no inline indication of whether the review was generated by Low or Medium tier. The "Medium"
  attribution in the PR overview comment closes that visibility gap. Important distinction:
  this is a tier-level attribution in the PR overview comment, distinct from the per-comment
  severity labels (High/Medium/Low) documented in `docs-github-copilot-code-review-comment-ux.md`
  (Claim 1). The existing severity labels apply to individual comments; this new attribution
  applies to the review as a whole and identifies the analysis depth tier used. For Ch01 (Daily
  Workflows): practitioners can now determine the analysis depth from within the PR UI without
  checking repository settings. For Ch05 (Team Adoption): the attribution supports rollout
  monitoring — teams gradually enabling Medium tier for repositories can confirm, at the PR
  level, that Medium is active.

## Concrete Artifacts

### Feature Summary (from changelog, June 25, 2026)

```
Copilot Code Review — Analysis Depth and Efficiency Updates (June 25, 2026)
Source: https://github.blog/changelog/2026-06-25-copilot-code-review-analysis-depth-and-efficiency-updates

Feature 1: CLI-Based File Tool Integration (all code review users)
  Tools:     grep, rg, glob, view (from Copilot CLI and SDK)
  Replaces:  Custom file exploration utilities
  Result:    ~20% reduction in code review costs (vendor claim)
  Quality:   "Maintaining the same standard of review quality" (vendor claim)
  Validated: "Both offline and online evaluation"

Feature 2: Org-Level Analysis Depth Configuration (Medium public preview only)
  Capability: Org admins set default analysis depth (Low or Medium) fleet-wide
  Scope:      Applies to repositories without an explicit per-repo setting
  Override:   Individual repositories can override the org default

Feature 3: Medium Attribution in PR Overview Comments (Medium public preview only)
  Location:  PR overview comment generated by Copilot code review
  Content:   Displays "Medium" when Medium analysis depth generated the review
  Purpose:   Quick verification at PR level of which analysis tier is active
  Distinct from: Per-comment severity labels (High/Medium/Low) from May 12 changelog
```

### Updated Code Review Configuration Surface (as of June 25, 2026)

```
# Copilot code review configuration surface — compiled from June 2, 12, and 25 changelogs

AGENT CONTEXT (what the agent reads during review):
  .github/skills/code-review/SKILL.md        → agent skill context (June 2)
  MCP servers (repo settings → Copilot)      → external context (June 2)
  .github/copilot-instructions.md            → general instructions, unlimited (June 12)
  *.instructions.md                          → additional instructions, unlimited (June 12)

CONTENT GOVERNANCE (what the agent can access):
  Content exclusion settings                 → repo / org / enterprise levels (June 12)

COMPUTE CONFIGURATION (where the agent runs):
  Org-level runner default + lock            → org settings → Copilot → Runner type (June 12)
  Per-repo Actions workflow                  → configurable compute environment (June 2)

ANALYSIS DEPTH (how thoroughly the agent reviews):
  Review tier (Low / Medium)                 → repo settings → Copilot → Code review (June 2)
  Org-level tier default (no lock)           → NEW: applies to unconfigured repos (June 25)
  PR overview attribution                    → NEW: "Medium" label in PR comment (June 25)

UNDERLYING ENGINE (new June 25 — transparent to user configuration):
  File exploration: grep, rg, glob, view (Copilot CLI/SDK)
  Cost efficiency: ~20% reduction per review (validated offline + online)
```

### Copilot Code Review Feature Evolution Arc (updated to June 25, 2026)

```
Date        Source Note                                           What Changed
----------  ----------------------------------------------------- -------------------------
2026-04-08  docs-github-copilot-pr-review-metrics                 Measurement: code review
                                                                  API fields
2026-04-27  docs-github-copilot-code-review-actions-billing       Billing: AI Credits +
                                                                  Actions minutes
2026-05-12  docs-github-copilot-code-review-comment-ux            UX: severity labels +
                                                                  comment grouping
2026-05-19  docs-github-copilot-cca-apply-review-feedback         Action: Fix with Copilot
2026-06-02  docs-github-copilot-code-review-skills-mcp-tier       Customization: skills +
                                                                  MCP + Low/Medium tier
2026-06-12  docs-github-copilot-code-review-config-controls       Governance: org runner +
                                                                  content exclusion +
                                                                  unlimited instructions
2026-06-25  THIS NOTE                                             Efficiency: CLI tools
(code-review-analysis-depth-efficiency)                           (~20% cost reduction);
                                                                  Governance: org-level
                                                                  tier default (no lock);
                                                                  Visibility: "Medium"
                                                                  PR attribution
```

## Cross-References

- **Extends** `docs-github-copilot-code-review-skills-mcp-tier.md` (issue #1052):
  - Claim 14: "Navigate to repository settings → Copilot → Code review → Review effort level."
    This source (Claim 5) adds an org-level default for that same tier setting — teams no
    longer need to configure each repository individually for a fleet-wide default. The per-repo
    override capability (Claim 6 of this note) means Claim 14 remains valid as the per-repo
    configuration path.
  - Claims 8–11 document the Medium tier's higher-reasoning model, cost difference, and quality
    claims. This source's ~20% cost reduction (Claim 2) is an architectural efficiency gain at
    the implementation level — distinct from the AI Credit cost increase of Medium tier vs. Low.
    The two cost dimensions layer: the architectural efficiency reduces resource consumption per
    review for both tiers; Medium tier still costs more AI Credits than Low tier even after the
    efficiency improvement.
  - Claim 9: "Low remains a fast, cost-efficient default for straightforward work like docs and
    small repositories." The ~20% efficiency gain makes both tiers more cost-efficient, though
    the source does not specify whether the gain applies identically to Low and Medium.

- **Extends** `docs-github-copilot-code-review-config-controls.md` (issue #1168):
  - Claim 6 documents the seven-layer configuration surface as of June 12. This source adds an
    eighth layer: org-level analysis depth default. The updated eight-layer surface is captured
    in the Concrete Artifacts section of this note.
  - Claims 1–2 document org-level runner configuration with lock enforcement. This source
    (Claims 5–6) adds org-level analysis depth configuration but WITHOUT a lock — repositories
    can override the depth default. This creates a meaningful governance distinction: runner type
    (compliance-relevant — air-gap, network boundary) has a lock mechanism; analysis depth
    (cost/quality tradeoff) retains per-repo flexibility.

- **Extends** `docs-github-copilot-code-review-actions-billing.md` (issue #445):
  - Claim 2: "That agentic architecture runs on GitHub Actions using GitHub-hosted runners."
    The CLI tool integration (Claim 1 of this note) refines that architectural picture: the
    file exploration component now uses shared Copilot CLI/SDK primitives rather than custom
    utilities, reducing the compute footprint per review. The billing model (AI Credits +
    Actions minutes) is unchanged; the ~20% efficiency gain means fewer Actions minutes are
    consumed per review.
  - Claim 6: "GitHub Copilot code review supports self-hosted runners and larger GitHub-hosted
    runners which are billed at different rates." The efficiency gain (Claim 2 of this note)
    applies on top of runner type — teams already using self-hosted runners for cost optimization
    get an additional ~20% reduction in review compute consumption.

- **Corroborates** `docs-github-copilot-code-review-comment-ux.md` (issue #723):
  - Claim 1 documents per-comment severity labels (High/Medium/Low). This source (Claim 7)
    adds a tier-level attribution ("Medium") in the PR overview comment. The two features are
    complementary, not duplicative: severity labels classify individual suggestions by importance;
    tier attribution identifies the depth level of the entire review. Teams should understand
    both as distinct UI elements in the PR review interface.

- **Contradicts**: None found. No existing source note claims that code review uses non-CLI file
  exploration utilities that cannot be changed, or that org-level analysis depth configuration
  is unavailable, or that there is no PR-level visibility into which analysis tier produced a
  review. This source extends prior notes without opposing existing claims. No contradiction
  issue to file.

- **Novel**:
  - **Quantified cost efficiency metric (~20%)**: No prior corpus source documents a specific
    cost efficiency improvement for any Copilot code review architectural component. This is
    the first numeric efficiency claim for the code review pipeline.
  - **CLI tool primitives in code review pipeline**: No prior source identifies the specific
    file exploration tools used by the code review agent. The switch from custom utilities to
    grep/rg/glob/view (Copilot CLI/SDK) is new architectural information.
  - **Org-level analysis depth default (no lock)**: Prior sources documented analysis depth as
    a per-repository setting only. Org-level defaults without a lock are documented here for
    the first time.
  - **"Medium" PR overview attribution**: No prior source documents any PR-level visibility
    indicator for which analysis tier generated a review. This is the first corpus documentation
    of inline tier attribution in the PR interface.

## Guide Impact

### Chapter 02: Harness Engineering

- **Update the configuration surface to eight layers**: The June 25 changelog adds an eighth
  layer: org-level analysis depth default. Any guide section referencing the June 12 seven-layer
  surface (citing `docs-github-copilot-code-review-config-controls.md` Claim 6) should be
  updated to include this new layer and note the lock/no-lock distinction: runner type has a
  lock enforcement mechanism; analysis depth defaults allow per-repo override.
- **CLI tool convergence as an architectural principle**: The reuse of grep/rg/glob/view from
  the Copilot CLI in code review confirms a platform decision to converge agent surfaces on
  shared file-tool primitives. For guide readers building custom agentic workflows: reusing
  proven, widely-tested tools rather than reimplementing file exploration is the pattern
  GitHub is following in its own products.
- **Org-level analysis depth default as a fleet governance pattern**: For teams deploying code
  review across many repositories, recommend: set org default to Low (cost-efficient baseline),
  then explicitly configure Medium per-repo for high-criticality code. This produces the same
  outcome as the per-repo strategy in `docs-github-copilot-code-review-skills-mcp-tier.md`
  (Claim 14) with significantly less administrative overhead.

### Chapter 05: Team Adoption

- **Update the TCO model with the ~20% cost reduction**: The code review cost model from
  `docs-github-copilot-code-review-actions-billing.md` can be revised: the architectural
  efficiency improvement reduces per-review resource consumption by approximately 20%. This is
  separate from the AI Credit cost difference between Low and Medium tiers — it applies at the
  infrastructure level for both tiers. Teams should recalculate their Copilot code review
  Actions minute projections downward by ~20%.
- **"Medium" PR attribution enables rollout validation**: Teams gradually enabling Medium tier
  can use the PR overview attribution to confirm at the PR level that Medium is active. Include
  in the adoption monitoring workflow: after enabling Medium for a repository, verify that PR
  overview comments display "Medium" attribution.
- **Org-level default simplifies fleet deployment checklist**: Update the deployment checklist
  from `docs-github-copilot-code-review-config-controls.md` Guide Impact: before fleet-wide
  enablement, set the org-level analysis depth default in addition to org runner defaults.
  Then identify repositories that warrant per-repo overrides (either for cost-saving downgrade
  to Low or quality-seeking upgrade to Medium).

### Chapter 01: Daily Workflows

- **Practitioners can now see analysis depth in the PR interface**: The "Medium" attribution
  in PR overview comments is a practitioner-visible signal. Engineers can now determine from
  the PR UI whether their review was generated by Medium or Low analysis depth without checking
  repository settings. Note the distinction from per-comment severity labels (H/M/L): severity
  labels classify individual suggestions; tier attribution identifies the overall review depth.

## Extraction Notes

1. **WebFetch returned AI-processed summaries, not verbatim text**: Both WebFetch attempts
   returned content processed through a small model. The second fetch explicitly refused to
   reproduce verbatim text citing copyright. Phrases that appeared inside double quotes in the
   first WebFetch output — specifically the ~20% cost reduction claim (Claim 2), the evaluation
   methodology phrase (Claim 3), and the "focused review" framing (Claim 4) — are used as
   verbatim quotes here. All other claims are marked `(no direct quote; see paraphrase in Our
   assessment)`. The Assayer should verify all quotes against the source URL directly.
2. **Medium public preview scope**: Features 2 and 3 (org-level depth default and PR attribution)
   apply only to organizations in the public preview for Medium analysis depth. Feature 1 (CLI
   tool efficiency) appears to apply to all code review users, not just those in the Medium
   preview. This scope distinction is preserved in the Concrete Artifacts section.
3. **Cost reduction denominator not specified**: The ~20% cost reduction does not specify whether
   it refers to Actions minutes, AI Credits, or both. Given the architectural change is to file
   exploration (the agentic tool-calling portion that runs on Actions), the reduction most likely
   refers to Actions minutes consumed per review. This is inferred, not stated.
4. **No sub-pages followed**: The changelog likely links to documentation for org-level depth
   configuration and PR attribution. These were not fetched.
5. **No contradictions to file**: All features extend prior corpus capabilities without opposing
   existing claims. No contradiction issue required.
