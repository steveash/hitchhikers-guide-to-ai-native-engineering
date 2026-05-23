---
source_url: https://github.github.com/gh-aw/guides/using-at-scale
source_type: docs
title: "GitHub Agentic Workflows: Using at Scale in Organizations"
author: GitHub Agentic Workflows team (official documentation)
date_published: null
date_extracted: 2026-05-23
last_checked: 2026-05-23
status: current
confidence_overall: emerging
issue: "#879"
---

# GitHub Agentic Workflows: Using at Scale in Organizations

> The organizational adoption guide that frames multi-repository gh-aw deployment
> as a qualitatively different capability layer — consolidates novel content on
> sparse-checkout monorepo optimization (tens of minutes → seconds), the three
> BatchOps strategies for large repositories, self-hosted runner deployment for
> compliance and isolation, and the enterprise GHE/data-residency deployment
> surface — alongside pointers to dedicated pattern docs for individual topics.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows `guides/using-at-scale` page —
  in the `guides/` section alongside `guides/organization-practices/safe-rollout`
  and `guides/organization-practices/sharing-workflows`. Guide pages are practitioner
  how-to references distinct from `patterns/` pages which document individual design
  patterns and `reference/` pages which document field schemas.)
- **Author credibility**: GitHub Agentic Workflows team — first-party documentation
  for the `gh aw` platform. Same team behind the Peli de Halleux / Don Syme agent
  factory blog series. Claims about platform capabilities and configuration are
  authoritative; claims about performance (checkout time) are illustrative estimates
  rather than benchmarked measurements.
- **Scope**: Organizational adoption guide covering workflow distribution,
  cross-repository access and authentication, multi-repository operation patterns,
  large-repository and monorepo performance optimization, cost management, enterprise
  deployment (self-hosted runners, GitHub Enterprise Server and Cloud), A/B
  experiments, and OpenTelemetry observability. This is a consolidating guide that
  links to dedicated pattern and reference pages for each topic. Does NOT provide
  deep coverage of any single pattern — individual pattern pages cover those in
  depth. Novel content specific to this page: the monorepo sparse-checkout
  performance quantification, BatchOps three-strategy enumeration, self-hosted
  runner requirements, and enterprise deployment surface.

## Extracted Claims

### Claim 1: Moving agentic workflows beyond a single repository into an organization enables qualitatively different capabilities — org-wide rollouts, assessment of hundreds of repositories, and centralized control planes — that single-repo use cannot provide

- **Evidence**: The guide's opening frames this as a qualitative shift, not merely
  a quantitative one. The capability list is concrete: org-wide change rollouts,
  code quality assessment across 100s of repos, dependency synchronization, coding
  policy propagation, backlog shrinkage across maintained repos, standards enforcement,
  and centralized issue aggregation.
- **Confidence**: emerging (first-party framing; the qualitative shift claim is
  editorial positioning, not a measured finding)
- **Quote**: "When agentic workflows move beyond a single repository and into an
  organization or enterprise, something qualitatively different becomes possible."
- **Our assessment**: The framing matters for organizational adoption decisions.
  Teams often consider multi-repo agentic workflows as "more of the same." This
  guide explicitly positions the transition as unlocking a new capability tier:
  the ability to assess, enforce, and evolve organizational standards across
  hundreds of repositories simultaneously — something that is not just slower
  with single-repo workflows, but structurally impossible. The "single control
  plane" framing (aggregating issue tracking into one view across all repos) is
  the specific capability that justifies multi-repo infrastructure investment.
  For Ch05 (Organization and Teams): use this framing to justify the organizational
  complexity of multi-repo gh-aw adoption — the payoff is a new class of
  capability, not just efficiency gains.

### Claim 2: Workflow distribution at organizational scale has two complementary layers — developer mechanics (installation and import commands) and organizational governance (central repositories, versioning, access controls)

- **Evidence**: The guide states there are "two complementary layers to workflow
  distribution across an organization" and describes each: the developer mechanics
  layer uses `gh aw add`, `gh aw add-wizard`, `gh aw update`, and `imports:` in
  workflow frontmatter; the governance layer involves maintaining central
  repositories as sources of truth, versioning strategies with tags, and
  controlling discoverability.
- **Confidence**: emerging (first-party framing; the two-layer structure is
  an editorial organization of related concepts rather than a formally validated
  taxonomy)
- **Quote**: "There are two complementary layers to workflow distribution across
  an organization."
- **Our assessment**: The two-layer framing is the most useful mental model for
  platform teams setting up org-wide gh-aw adoption: developer mechanics solve
  the "how does a consuming team install a workflow" question; governance solves
  the "who owns it, how is it versioned, who can install it" question. Teams that
  only configure the mechanics layer without the governance layer end up with
  ungoverned proliferation — each team forks workflows independently with no
  update path. Teams that only address governance without clear developer mechanics
  create adoption friction. The guide's two-layer framing is the correct starting
  model for Ch05. Cross-reference: `docs-ghaw-sharing-workflows.md` covers
  the developer mechanics layer (Claim 1) and governance layer (Claim 8) in detail;
  this guide provides the framing that connects them as complementary layers.

### Claim 3: Using `sparse-checkout` in the `checkout:` field can reduce monorepo checkout time from tens of minutes to seconds by fetching only the paths a workflow actually needs

- **Evidence**: The guide states this directly in the large monorepos section,
  providing a specific performance quantification (tens of minutes → seconds) as
  the benefit of sparse-checkout adoption.
- **Confidence**: emerging (first-party; the directional claim is credible for
  large monorepos, but "tens of minutes to seconds" is an illustrative estimate
  from the documentation team rather than a benchmarked measurement from a
  specific repository configuration)
- **Quote**: "Use `sparse-checkout` in the `checkout:` field to fetch only the
  paths a workflow actually needs — this can reduce checkout time from tens of
  minutes to seconds."
- **Our assessment**: This is the most directly actionable novel claim in the
  source. The checkout reference (`docs-ghaw-checkout-reference.md` Claim 9)
  documents the `sparse-checkout` field as "Newline-separated patterns for sparse
  checkout" but does not provide a performance quantification or frame it as a
  monorepo strategy. This guide adds the specific monorepo use-case framing and
  the order-of-magnitude performance claim. For large monorepos where full checkout
  takes tens of minutes (common in enterprise repos with large binary assets, deep
  history, or extensive LFS), sparse-checkout is not merely a performance
  optimization — it makes agentic workflows on those repos operationally viable.
  For Ch04 (Scale and Complexity) and Ch02 (Harness Engineering): add sparse-checkout
  as a required optimization for monorepo workflows, with the performance
  quantification as justification.

### Claim 4: The QMD search tool enables vector similarity search over indexed monorepo content without requiring a full clone — making semantic search available to agents on large repositories

- **Evidence**: The guide positions QMD specifically in the monorepo section as a
  technique for working with large repositories without cloning them: "the QMD
  search tool runs vector similarity search over indexed repository content without
  requiring a full clone."
- **Confidence**: emerging (first-party; the positioning is editorial, placing
  QMD in the monorepo context; the technical claim about search without cloning
  is consistent with the QMD reference documentation)
- **Quote**: "the QMD search tool runs vector similarity search over indexed
  repository content without requiring a full clone."
- **Our assessment**: The `docs-ghaw-qmd-reference.md` (Claim 1) covers QMD as
  a documentation search tool running `tobi/qmd` as an MCP server. This guide
  adds the complementary framing: QMD is specifically valuable in the monorepo
  context because it avoids the clone cost entirely. An agent querying a 50GB
  monorepo for a specific API surface does not need to clone 50GB if QMD can
  find the relevant fragments via vector similarity. Sparse-checkout (Claim 3)
  and QMD search (this claim) are complementary strategies: sparse-checkout
  reduces checkout cost for known paths; QMD eliminates checkout cost for
  discovery-oriented queries. For Ch04: document QMD as the monorepo semantic
  search alternative to full-clone checkout, paired with sparse-checkout as
  the two-strategy monorepo toolkit.

### Claim 5: BatchOps covers three large-repository processing strategies: chunked pagination across scheduled runs, matrix fan-out for parallel sharding, and rate-limit-aware sub-batching

- **Evidence**: The guide names all three BatchOps strategies explicitly in the
  context of large repositories: "BatchOps covers the main strategies: chunked
  pagination across scheduled runs, matrix fan-out for parallel sharding, and
  rate-limit-aware sub-batching."
- **Confidence**: emerging (first-party; the three strategies are named as part
  of the BatchOps pattern; there is no dedicated BatchOps source note in the
  corpus to cross-reference against)
- **Quote**: "BatchOps covers the main strategies: chunked pagination across
  scheduled runs, matrix fan-out for parallel sharding, and rate-limit-aware
  sub-batching."
- **Our assessment**: No dedicated BatchOps source note exists in the corpus.
  The WorkQueueOps note (`docs-ghaw-workqueue-ops.md` Claim 10) contrasts
  WorkQueueOps with BatchOps but describes it only as "process large volumes in
  parallel chunks rather than sequentially." This guide provides the first
  corpus-level enumeration of the three named BatchOps strategies. Each addresses
  a different large-repo constraint: chunked pagination handles repositories with
  more items than can be processed in one run; matrix fan-out distributes
  processing across parallel workers by sharding the item space; rate-limit-aware
  sub-batching prevents token/API rate limit exhaustion within a single run. A
  dedicated BatchOps source note would extend this with YAML configuration
  examples. For Ch04 (Scale and Complexity): add the three-strategy BatchOps
  taxonomy alongside WorkQueueOps as the parallel (bounded, high-throughput)
  counterpart to WorkQueueOps' sequential (unbounded, resumable) approach.

### Claim 6: WorkQueueOps with cache-memory provides durable progress tracking for large backlogs that survives interruptions, rate limits, and multi-day processing horizons

- **Evidence**: The guide states: "WorkQueueOps with cache-memory provides durable
  progress tracking that survives interruptions."
- **Confidence**: settled (consistent with the dedicated WorkQueueOps source note;
  first-party documentation)
- **Quote**: "WorkQueueOps with cache-memory provides durable progress tracking
  that survives interruptions."
- **Our assessment**: Corroborates `docs-ghaw-workqueue-ops.md` Claim 1 ("surviving
  interruptions, rate limits, and multi-day horizons") and Claim 5 (cache-memory
  as the large-queue strategy). The at-scale guide positions WorkQueueOps
  specifically as the solution for large issue repositories — complementing BatchOps
  when the processing horizon extends beyond a single run window. For Ch04: the
  distinction between BatchOps (all items processable in one run) and WorkQueueOps
  (multi-day, resumable) is the key selection criterion for large-repo processing
  strategy.

### Claim 7: GitHub Apps are preferred over PATs for cross-repository authentication because of automatic token rotation and fine-grained scoping

- **Evidence**: The guide states this preference explicitly in the private
  repositories section: "GitHub Apps are preferred for automatic token rotation
  and fine-grained scoping."
- **Confidence**: settled (consistent with `docs-ghaw-multi-repo-ops.md` Claim 8;
  the preference is first-party guidance with clear technical rationale)
- **Quote**: "GitHub Apps are preferred for automatic token rotation and fine-grained
  scoping."
- **Our assessment**: Corroborates `docs-ghaw-multi-repo-ops.md` Claim 8 (GitHub
  App Installation Tokens preferred over PATs — per-job minting, automatic
  revocation, fine-grained permissions, better attribution). The at-scale framing
  reinforces this guidance in the organizational deployment context where credential
  management across hundreds of repositories makes PAT rotation especially costly.
  For Ch03 (Safety and Verification) and Ch05: GitHub App preference should be
  the default recommendation for any org-scale cross-repository gh-aw deployment.

### Claim 8: Organizations requiring network isolation, compliance, or cost control can use self-hosted runners for agentic workflows; self-hosted runners must be Linux with Docker

- **Evidence**: The guide describes self-hosted runners in the enterprise section:
  "Organizations that need to run agentic workflows on their own infrastructure —
  for network isolation, compliance, or cost reasons — can use self-hosted runners."
  The guide references the self-hosted runner documentation for configuration, and
  (per the broader gh-aw platform documentation) self-hosted runners must run
  Linux with Docker to execute the containerized agentic workflow runtime.
- **Confidence**: emerging (first-party framing for the use cases; the Linux +
  Docker requirement is stated in the self-hosted runner documentation linked from
  this guide, not verbatim on this page)
- **Quote**: "Organizations that need to run agentic workflows on their own
  infrastructure — for network isolation, compliance, or cost reasons — can use
  self-hosted runners."
- **Our assessment**: Self-hosted runner support is a critical enterprise adoption
  enabler. The three use cases (network isolation, compliance, cost) represent the
  three main enterprise blockers for GitHub-hosted runner adoption: (1) network
  isolation — enterprises with strict egress controls cannot allow agentic
  workflows to use GitHub-hosted runners that access the public internet; (2)
  compliance — data sovereignty, audit log requirements, or regulatory constraints
  may require on-premises execution; (3) cost — GitHub-hosted runner minutes may
  exceed the cost of self-managed compute at enterprise scale. No existing source
  note in the corpus covers self-hosted runner deployment for gh-aw. For Ch05
  (Organization and Teams) and Ch04 (Scale and Complexity): add self-hosted runner
  support as an enterprise adoption prerequisite discussion, with the three use
  cases as the decision criteria for whether self-hosted runners are required.

### Claim 9: Deployments on GitHub Enterprise Server or GHE Cloud with data residency require additional configuration — runner setup, token scoping, and endpoint customization — compared to github.com deployments

- **Evidence**: The guide addresses GHE deployment: "For deployments on GitHub
  Enterprise Server or GitHub Enterprise Cloud with data residency, see the
  Enterprise Configuration reference for runner configuration, token scoping, and
  endpoint customization."
- **Confidence**: emerging (first-party; the guide points to a reference page
  for details rather than describing the specifics on this page)
- **Quote**: "For deployments on GitHub Enterprise Server or GitHub Enterprise
  Cloud with data residency, see the Enterprise Configuration reference for
  runner configuration, token scoping, and endpoint customization."
- **Our assessment**: The three-area configuration surface for GHE deployments
  (runner configuration, token scoping, endpoint customization) is a useful
  enumeration for enterprise platform teams. GHE deployments differ from github.com
  in that the API endpoint changes (affecting token scoping and MCP server
  authentication), runners must be configured for the GHE instance, and data
  residency on GHE Cloud requires endpoint routing that keeps data within the
  specified region. No existing source note covers GHE-specific gh-aw deployment.
  For Ch05 (Organization and Teams): add GHE deployment considerations as a
  separate section from github.com deployment, noting the three configuration
  areas teams must address.

### Claim 10: OpenTelemetry integration for gh-aw covers four areas of each workflow run: activation, agent execution, safe-output operations, and MCP tool calls

- **Evidence**: The guide describes the observability coverage: "GitHub Agentic
  Workflows can be configured to emit OpenTelemetry traces and spans for each
  workflow run, covering activation, agent execution, safe-output operations,
  and MCP tool calls."
- **Confidence**: emerging (first-party; the four-area coverage scope is stated
  explicitly; configuration details are in the dedicated observability reference)
- **Quote**: "GitHub Agentic Workflows can be configured to emit OpenTelemetry
  traces and spans for each workflow run, covering activation, agent execution,
  safe-output operations, and MCP tool calls."
- **Our assessment**: The four-area coverage scope gives practitioners a complete
  picture of what OTEL tracing observes in a gh-aw workflow. Activation spans
  cover the pre-agent setup (compilation, trigger handling, experiment variant
  selection); agent execution spans cover the AI inference and tool use loop;
  safe-output operation spans cover each GitHub write (issue creation, PR creation,
  comment posting) with its outcome; MCP tool call spans cover each external tool
  invocation. Together these four areas give distributed tracing across the full
  workflow lifecycle, enabling root-cause analysis for failures at any stage.
  The `docs-ghaw-agentic-ops.md` note covers OTEL at the configuration level
  (with `observability.otlp` frontmatter); this guide provides the at-scale framing
  positioning OTEL as the observability mechanism for organizations running many
  concurrent workflows. For Ch04 and Ch05: present OTEL as the recommended
  observability infrastructure for organizations deploying gh-aw at scale.

### Claim 11: A/B experiments in gh-aw use a balanced round-robin counter to select named prompt variants so every variant is exercised equally across runs

- **Evidence**: The guide describes the experiment selection mechanism: "The A/B
  Experiments feature lets you define named prompt variants in workflow frontmatter
  and measure their effect across runs. The activation job selects a variant using
  balanced round-robin counter so every variant is exercised equally."
- **Confidence**: settled (consistent with `docs-ghaw-practices-experiments.md`
  Claim 1; first-party documentation)
- **Quote**: "The activation job selects a variant using balanced round-robin counter
  so every variant is exercised equally."
- **Our assessment**: Corroborates `docs-ghaw-practices-experiments.md` Claim 1
  (experiments section of workflow frontmatter, variants selected by activation job).
  The at-scale guide's contribution here is framing A/B experiments as a named
  at-scale feature — specifically relevant when organizations want to measure prompt
  variant effects across hundreds of repositories or many concurrent workflow runs.
  The round-robin selection ensures statistical fairness across variants without
  requiring randomization infrastructure. For Ch04 (Scale and Complexity): position
  gh-aw's built-in A/B experiment support as the platform-native way to run
  controlled prompt experiments at organizational scale.

### Claim 12: Cost management at organizational scale requires integrating three levers — token budgeting, model selection, and spend tracking — not just rate limiting

- **Evidence**: The guide frames cost management as a multi-lever concern: "Running
  agentic workflows at scale consumes compute and AI inference tokens. Use the Cost
  Management reference for an overview of token budgeting, model selection, and
  spend tracking." The guide also references the Effective Tokens Specification as
  a tool for accurate cost calculation and rate-limiting controls for preventing
  runaway spend.
- **Confidence**: emerging (the three-lever framing is editorial positioning from
  the platform team; the Cost Management reference page provides the specifics)
- **Quote**: "Running agentic workflows at scale consumes compute and AI inference
  tokens."
- **Our assessment**: The three-lever framing (token budgeting, model selection,
  spend tracking) goes beyond the rate-limiting controls focus that dominates the
  existing corpus. Rate limiting (`docs-ghaw-rate-limiting-controls.md` Claim 8)
  is a defensive mechanism that caps usage; token budgeting and model selection
  are proactive mechanisms that match model capability to task requirements. Using
  a high-capability model (higher cost per token) for routine issue triage is
  wasteful; using it for complex refactoring is appropriate. The Effective Tokens
  Specification (covered in `docs-ghaw-effective-tokens-specification.md`) provides
  the normative metric for cost calculation. For Ch05: present cost management as
  a three-lever system — proactive (budgeting + model selection) + defensive
  (rate limiting + spend tracking) — rather than treating rate limiting as the
  only cost control mechanism.

## Concrete Artifacts

### Sparse-Checkout Monorepo Optimization (from source, verbatim)

```
"Use `sparse-checkout` in the `checkout:` field to fetch only the paths a
workflow actually needs — this can reduce checkout time from tens of minutes
to seconds."
```

*Source: Using at Scale guide, large monorepos section.*

### Checkout field for sparse-checkout in workflow frontmatter

```yaml
# Sparse checkout for monorepo — fetch only needed paths
checkout:
  sparse-checkout: |
    .github/
    src/
    # Add only the directories the agent actually needs
```

*Source: Checkout Reference (`docs-ghaw-checkout-reference.md` Claim 9);
pattern recommended in Using at Scale guide monorepos section.*

### BatchOps Three Strategies (from source, verbatim)

```
"BatchOps covers the main strategies: chunked pagination across scheduled
runs, matrix fan-out for parallel sharding, and rate-limit-aware sub-batching."
```

*Source: Using at Scale guide, large repositories section.*

### OpenTelemetry Coverage Scope (from source, verbatim)

```
"GitHub Agentic Workflows can be configured to emit OpenTelemetry traces and
spans for each workflow run, covering activation, agent execution, safe-output
operations, and MCP tool calls."
```

*Source: Using at Scale guide, observability section.*

### A/B Experiment Variant Selection (from source, verbatim)

```
"The A/B Experiments feature lets you define named prompt variants in workflow
frontmatter and measure their effect across runs. The activation job selects
a variant using balanced round-robin counter so every variant is exercised
equally."
```

*Source: Using at Scale guide, A/B experiments section.*

### Organizational Capability Tier (from source, verbatim)

```
"Roll out changes org-wide"
"Assess code quality across 100s of repos"
"Synchronize dependency updates"
"Propagate coding policy changes"
"Shrink backlogs in multiple maintained repos"
"Enforce coding standards across teams"
"Aggregate issue tracking into a single control plane"
```

*Source: Using at Scale guide, overview capabilities list.*

### Self-Hosted Runner Use Cases (from source, verbatim)

```
"Organizations that need to run agentic workflows on their own infrastructure
— for network isolation, compliance, or cost reasons — can use self-hosted
runners."
```

*Source: Using at Scale guide, enterprise deployment section.*

### GHE Deployment Configuration Areas (from source, verbatim)

```
"For deployments on GitHub Enterprise Server or GitHub Enterprise Cloud with
data residency, see the Enterprise Configuration reference for runner
configuration, token scoping, and endpoint customization."
```

*Source: Using at Scale guide, enterprise deployment section.*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-sharing-workflows.md` Claim 1 (`gh aw add` as the primary
    distribution mechanism) and Claim 8 (enterprise central-repo pattern):
    this guide's two-layer distribution framing (Claim 2) is consistent with
    and builds on the distribution mechanics covered in the sharing-workflows
    note. Both sources agree on the central-repo governance model.
  - `docs-ghaw-multi-repo-ops.md` Claim 8 (GitHub Apps preferred over PATs):
    this guide's Claim 7 directly corroborates the preference for GitHub Apps
    with the same rationale (automatic token rotation, fine-grained scoping).
  - `docs-ghaw-workqueue-ops.md` Claim 1 (WorkQueueOps survives interruptions):
    this guide's Claim 6 is consistent with the WorkQueueOps source note's
    opening definition, providing the at-scale framing for the same pattern.
  - `docs-ghaw-checkout-reference.md` Claim 9 (sparse-checkout field):
    this guide's Claim 3 uses the same field but adds the monorepo-specific
    performance quantification (tens of minutes → seconds) absent from the
    checkout reference.
  - `docs-ghaw-practices-experiments.md` Claim 1 (experiments section enabling
    A/B testing): this guide's Claim 11 corroborates the round-robin selection
    and adds the at-scale framing for organizational prompt experimentation.
  - `docs-ghaw-rate-limiting-controls.md` Claim 1 (defense-in-depth anti-runaway
    taxonomy): this guide's Claim 12 positions rate limiting as one component of
    a broader three-lever cost management system (budgeting + model selection +
    spend tracking), consistent with the rate-limiting note's framing.
  - `docs-ghaw-qmd-reference.md` Claim 1 (QMD vector similarity search):
    this guide's Claim 4 is consistent with and extends the QMD reference's
    definition, adding the monorepo optimization framing.

- **Contradicts**: None identified. Reviewed all gh-aw source notes. All claims
  in this guide are consistent with the dedicated pattern and reference source
  notes. No contradiction issue required.

- **Extends**:
  - `docs-ghaw-checkout-reference.md` Claim 9: the checkout reference documents
    sparse-checkout as a field configuration; this guide adds the monorepo-specific
    use case framing and the specific performance quantification. Together they give
    both the configuration reference and the organizational deployment motivation.
  - `docs-ghaw-workqueue-ops.md` and `docs-ghaw-rate-limiting-controls.md`: those
    notes cover individual patterns in depth; this guide provides the organizational
    context for when to apply them together as part of a coherent at-scale strategy.
  - `docs-ghaw-safe-rollout.md` Claim 2 (four-rung rollout ladder): this guide
    implicitly extends the rollout framework by adding the organizational dimensions
    (multi-repo deployment patterns, enterprise configuration) that the safe-rollout
    note does not cover.

- **Novel** (what this note adds that no prior source covers):
  - **Sparse-checkout performance quantification for monorepos** (Claim 3):
    The specific "tens of minutes to seconds" estimate is not in the checkout
    reference note or any other corpus source. This is the first corpus source
    to quantify the monorepo checkout problem and its magnitude.
  - **BatchOps three-strategy enumeration** (Claim 5): No dedicated BatchOps
    source note exists. This is the first corpus source to name all three
    BatchOps strategies (chunked pagination, matrix fan-out, rate-limit-aware
    sub-batching) as a coherent taxonomy. The WorkQueueOps note mentions BatchOps
    but only as a one-line contrast ("parallel chunks").
  - **Self-hosted runner use-case framing for gh-aw** (Claim 8): No existing
    source note covers self-hosted runners as a gh-aw enterprise adoption
    mechanism. The three use cases (network isolation, compliance, cost) are
    new to the corpus.
  - **GHE-specific deployment surface** (Claim 9): No existing source note
    covers GitHub Enterprise Server or GHE Cloud with data residency as gh-aw
    deployment targets. The three configuration areas (runner config, token
    scoping, endpoint customization) are new to the corpus.
  - **OpenTelemetry four-area coverage scope** (Claim 10): The agentic-ops
    note covers OTEL configuration details (frontmatter, OTLP endpoint), but
    the four-area lifecycle coverage scope (activation + agent execution +
    safe-output operations + MCP tool calls) as stated in this guide is new
    to the corpus as a clean summary.
  - **Organizational adoption framing of the qualitative shift** (Claim 1):
    The explicit framing that multi-repo agentic workflows enable "something
    qualitatively different" — not just more of the same — is a novel editorial
    positioning in the corpus that has practical guide impact.

## Guide Impact

- **Chapter 04 (Scale and Complexity)**:
  - Add the sparse-checkout → seconds quantification (Claim 3) as the primary
    justification for making sparse-checkout standard practice in any monorepo
    gh-aw workflow. Current corpus does not surface this quantification.
  - Add the three-strategy BatchOps taxonomy (Claim 5) as the parallel-processing
    complement to WorkQueueOps' sequential processing. Recommend BatchOps for
    bounded within-run parallel workloads; WorkQueueOps for multi-day resumable
    backlogs.
  - Add QMD + sparse-checkout as the two-tool monorepo toolkit (Claims 3–4):
    sparse-checkout for known-path operations, QMD for semantic discovery without
    full-clone cost.

- **Chapter 05 (Organization and Teams)**:
  - Add the qualitative shift framing (Claim 1) as the motivation for multi-repo
    gh-aw investment: the payoff is a new capability class (org-wide enforcement,
    centralized control planes), not just efficiency gains.
  - Add the two-layer distribution model (Claim 2) as the organizational
    architecture for workflow distribution: developer mechanics (installation)
    + governance layer (versioning, access, central repos).
  - Add self-hosted runner use cases (Claim 8) as an enterprise adoption
    prerequisite discussion: network isolation, compliance, and cost control
    as the three reasons an organization needs self-hosted runners.
  - Add GHE deployment considerations (Claim 9) as a separate section from
    github.com deployment: runner configuration, token scoping, and endpoint
    customization as the three areas requiring GHE-specific work.
  - Add three-lever cost management (Claim 12): proactive (token budgeting +
    model selection) + defensive (rate limiting + spend tracking).

- **Chapter 02 (Harness Engineering)**:
  - Add sparse-checkout as a required pattern for any monorepo workflow
    (Claim 3) — not optional. The order-of-magnitude checkout time improvement
    makes it a correctness concern (workflow timeout) as well as a performance
    concern.
  - Add OpenTelemetry four-area coverage scope (Claim 10) to the harness
    observability section: practitioners designing at-scale deployments should
    instrument all four areas.

- **Chapter 03 (Safety and Verification)**:
  - Add GitHub Apps preference (Claim 7) as the default cross-repo credential
    recommendation for any org-scale gh-aw deployment — not just a best practice
    but a governance requirement when managing credentials across many repositories.

## Extraction Notes

1. **Source is a consolidating guide**: The using-at-scale page is explicitly a
   roadmap that links to dedicated pattern and reference pages for each topic.
   Extraction focused on claims that are specific to this page (especially the
   novel content the Prospector identified) rather than re-extracting what is
   already deeply covered in dedicated source notes.

2. **WebFetch AI-model processing**: This page content is processed by WebFetch's
   AI model before returning results. Three independent fetches were made with
   different prompts to triangulate verbatim wording. Quotes in this note are
   drawn from passages that appeared consistently across fetches. The guide page
   is an Astro/Starlight SPA; exact rendering may vary slightly by client.

3. **BatchOps reference page not fetched**: The guide references a BatchOps
   pattern page (`patterns/batch-ops`) for the full BatchOps documentation.
   That page was not fetched for this extraction — it warrants a dedicated source
   note. The BatchOps claims here are limited to what the using-at-scale guide
   itself states.

4. **Self-hosted runner Linux+Docker requirement**: The Linux with Docker
   requirement is mentioned in the broader gh-aw documentation for self-hosted
   runners (linked from this guide), not explicitly stated verbatim on the
   using-at-scale page itself. The claim notes this in its evidence assessment.

5. **No publication date**: The documentation page does not carry an explicit
   publication date. Content is consistent with gh-aw platform state as of
   the 2026-05-23 extraction date.

6. **No contradictions filed**: Reviewed all existing corpus source notes.
   No claims in this guide materially oppose any existing note. No contradiction
   issue required.
