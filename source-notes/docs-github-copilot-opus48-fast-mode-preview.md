---
source_url: https://github.blog/changelog/2026-06-29-claude-opus-4-8-fast-mode-is-now-in-preview-for-github-copilot
source_type: docs
title: "Claude Opus 4.8 (fast mode) is now in preview for GitHub Copilot"
author: GitHub (official changelog)
date_published: 2026-06-29
date_extracted: 2026-06-30
last_checked: 2026-06-30
status: current
confidence_overall: settled
issue: "#1354"
---

# Claude Opus 4.8 (Fast Mode) Is Now in Preview for GitHub Copilot

> GitHub's June 29, 2026 changelog announcing Claude Opus 4.8 fast mode as a
> preview option in GitHub Copilot, extending fast mode access beyond the direct
> Anthropic API to a major IDE-integrated platform — covering 9 Copilot surfaces,
> gated to Pro+/Max/Business/Enterprise plans with an admin-policy opt-in for
> Business and Enterprise, and priced under Usage Based Billing at a cost below
> prior fast-mode generations but above standard Opus 4.8.

## Source Context

- **Type**: docs (GitHub official product changelog, June 29, 2026; approximately
  200–300 words of primary announcement text)
- **Author credibility**: GitHub engineering team announcing a production preview
  feature. Authoritative for: the fact that fast mode is now available in Copilot,
  the list of supported surfaces, plan eligibility, admin policy requirements, and
  the stated pricing tier. Not a credible source for: specific throughput
  measurements (no numbers given), task-type performance comparisons, latency
  differences vs. standard Opus 4.8, or the specific cost per token in Copilot's
  Usage Based Billing context (the source refers to "provider list pricing" without
  quoting exact figures).
- **Scope**: The availability of Claude Opus 4.8 fast mode as a new model option
  within GitHub Copilot, covering supported surfaces, plan access, admin policy
  setup for B/E plans, billing, and general rollout status. Does NOT cover: specific
  performance metrics (OTPS numbers), comparison to standard Opus 4.8 latency in
  Copilot, how fast mode interacts with Copilot's auto model selection routing, the
  prompt cache invalidation behavior documented in the Anthropic fast mode docs, or
  platform availability on Vertex AI/Bedrock/Foundry (those remain excluded per the
  prior Anthropic launch documentation).

## Extracted Claims

### Claim 1: Claude Opus 4.8 fast mode is now in preview in GitHub Copilot as of June 29, 2026

- **Evidence**: Official GitHub product changelog announcing the feature as a named
  preview. The announcement date is June 29, 2026, with a gradual rollout underway.
- **Confidence**: settled (product fact — the feature exists, is documented by
  GitHub engineering, and is actively rolling out)
- **Quote**: (no direct title quote available verbatim; announcement stated as
  "Claude Opus 4.8 (fast mode) is now in preview for GitHub Copilot")
- **Our assessment**: This is a significant platform-expansion event for fast mode.
  The Anthropic fast mode launch (documented in `blog-simonwillison-llm-anthropic-0251.md`
  Claim 7) initially scoped fast mode to "the Claude API, including Claude Managed
  Agents, only" — explicitly excluding "third-party platforms." GitHub Copilot's
  inclusion as of June 29 represents the first documented expansion of fast mode to
  a third-party hosting platform. Practitioners who could not use fast mode because
  they route through GitHub Copilot (not the direct Anthropic API) now have access
  via the model picker on supported plan tiers.

### Claim 2: Fast mode delivers significantly faster output token speeds while maintaining the same intelligence as Claude Opus 4.8

- **Evidence**: Official changelog product description. Both independent WebFetch
  calls returned this phrasing consistently.
- **Confidence**: settled (stated in official GitHub changelog, consistent with
  Anthropic's first-party fast mode documentation)
- **Quote**: "delivers significantly faster output token speeds while maintaining
  the same intelligence as Claude Opus 4.8"
- **Our assessment**: This is the canonical fast mode value proposition as stated
  by GitHub — same weights, faster output throughput. The Willison note (Claim 4)
  quantifies this from Anthropic's own docs: "Up to 2.5x higher output tokens per
  second compared to standard speed." GitHub's changelog uses qualitative language
  ("significantly faster") rather than the 2.5x number. The two claims are
  consistent; the Anthropic fast mode documentation provides the quantitative grounding
  that this changelog elides. For the guide: cite the 2.5x figure from
  `blog-simonwillison-llm-anthropic-0251.md` Claim 4 when precision is needed;
  use this changelog as the authoritative source for Copilot availability.
  Importantly: "significantly faster output token speeds" — not time-to-first-token.
  Fast mode improves throughput (tokens/second), not perceived responsiveness at
  the start of a response. This distinction matters for interactive use cases.

### Claim 3: Fast mode is positioned as well suited for interactive coding and agentic workflows where responsiveness matters

- **Evidence**: Official changelog's use-case framing — the stated rationale for
  when practitioners should choose fast mode over standard Opus 4.8.
- **Confidence**: settled (vendor framing stated in official changelog)
- **Quote**: "well suited for interactive coding and agentic workflows where
  responsiveness matters"
- **Our assessment**: The "interactive coding and agentic workflows" framing maps
  directly to the primary use-case context for GitHub Copilot (IDE chat, cloud
  agent tasks). The "responsiveness" qualifier connects to the throughput improvement:
  faster token output makes streaming responses feel more responsive even if
  time-to-first-token is unchanged. For practitioners deciding when to use fast mode
  in Copilot: the use case signals (interactive, agentic) align with exactly the
  Copilot surfaces where fast mode is now available (VS Code, CLI, cloud agent). For
  batch or non-interactive workloads where throughput matters less than cost, standard
  Opus 4.8 remains the appropriate choice.

### Claim 4: Fast mode in Copilot is available across 9 named surfaces: VS Code, Visual Studio, Copilot CLI, GitHub Copilot cloud agent, the Copilot app, github.com, GitHub Mobile (iOS/Android), JetBrains, Xcode, and Eclipse

- **Evidence**: Official changelog lists supported surfaces. This is the broadest
  cross-surface fast-mode availability announced for any platform to date.
- **Confidence**: settled (surface list stated in official changelog)
- **Quote**: (surface list returned by WebFetch; specific formatting unclear — quote
  fields are paraphrased from WebFetch output; Assayer should verify exact surface
  list wording against the live source URL)
- **Our assessment**: The surface coverage is striking: VS Code, JetBrains, Xcode,
  Eclipse, Visual Studio, the web UI, mobile (iOS/Android), the dedicated Copilot
  app, and the CLI. This means fast mode is available wherever Copilot is available
  for the eligible plan tiers — it is not a subset feature limited to specific IDE
  plugins. Practitioners on Pro+/Max/Business/Enterprise can access fast mode from
  their preferred development environment without switching tools. For Ch04: document
  that fast mode model selection follows the same surface availability as the model
  picker generally. There is no surface-specific configuration needed beyond plan
  eligibility and (for B/E) admin policy enablement.

### Claim 5: Fast mode is available to Copilot Pro+, Max, Business, and Enterprise subscribers — not to Free or Student plans

- **Evidence**: Official changelog access eligibility statement. Consistent with
  plan-tier restrictions documented across prior Copilot changelog entries.
- **Confidence**: settled (plan eligibility stated in official changelog)
- **Quote**: (plan tier list returned by WebFetch; exact phrasing uncertain — Assayer
  should verify against live source; paraphrase: "accessible to Copilot Pro+, Max,
  Business, and Enterprise users")
- **Our assessment**: Free and Student plan exclusion is consistent with the
  trajectory documented in `docs-github-copilot-free-student-auto-only-model-selection.md`
  (Claim 1): those plans already lost manual model selection as of June 24, 2026.
  Fast mode is a premium capability that is appropriately gated above the free tier.
  Pro and Pro+ subscription tiers are NOT listed — the eligible tiers are Pro+, Max,
  Business, and Enterprise. Practitioners on the standard Pro plan ($10/month) cannot
  access fast mode in Copilot; they would need Pro+ or higher. This plan-tier
  boundary is notable and aligns with fast mode being positioned as an "interactive
  and agentic" premium offering.

### Claim 6: Fast mode in Copilot is billed under Usage Based Billing at a reduced cost compared to previous fast mode generations, but still at a premium over standard Claude Opus 4.8

- **Evidence**: Official changelog pricing statement. Consistent with the pricing
  trajectory documented in `blog-simonwillison-llm-anthropic-0251.md` (Claim 5),
  which shows Opus 4.8 fast mode at $10/$50 per MTok (vs. $30/$150 for Opus 4.6/4.7
  fast mode) through the direct Anthropic API.
- **Confidence**: settled for the directional claim (premium over standard, below
  prior fast modes); the exact multiplier in Copilot's UBB system is not quoted in
  the source
- **Quote**: "at a reduced cost compared to previous fast modes, though it still
  costs more than standard Claude Opus 4.8" (paraphrase from WebFetch — Assayer
  should verify exact wording; the substance — premium over standard, below prior
  fast mode — is consistent across both WebFetch calls)
- **Our assessment**: In Copilot's Usage Based Billing model, models are priced at
  provider list pricing. For Opus 4.8 fast mode, the Anthropic list price is $10/$50
  per MTok input/output (vs. $5/$25 for standard Opus 4.8) — a 2x input premium.
  The "reduced cost compared to previous fast modes" refers to the 3x reduction
  versus Opus 4.6/4.7 fast mode ($30/$150). The guide should cite the specific API
  pricing from `blog-simonwillison-llm-anthropic-0251.md` (Claim 5 pricing table)
  when practitioners need exact numbers; this changelog provides the directional
  framing. For cost-sensitive agentic workloads, fast mode in Copilot doubles the
  input token cost vs. standard Opus 4.8 — the throughput benefit must justify the
  premium on a per-use-case basis.

### Claim 7: Enterprise and Business plan administrators must explicitly enable a policy for fast mode in Copilot settings; the policy is off by default

- **Evidence**: Official changelog admin configuration requirement. This follows the
  standard Copilot admin policy pattern for new model capabilities.
- **Confidence**: settled (stated in official changelog)
- **Quote**: (paraphrase from WebFetch: "administrators must enable the policy for
  fast mode for Claude Opus 4.8 in Copilot settings. The policy is off by default."
  — Assayer should verify exact phrasing against live source)
- **Our assessment**: The off-by-default admin policy requirement for B/E plans is
  consistent with the governance pattern established for third-party AI model access
  in Copilot (documented in `docs-github-copilot-agent-model-selection.md`, Claim 5).
  Enterprise organizations that want developers to access fast mode must take an
  explicit admin action — it will not appear automatically. For Ch05 (enterprise
  governance): document fast mode as a capability requiring admin policy enablement in
  B/E organizations, distinct from standard model availability. Orgs with existing
  Anthropic Claude policies enabled will still need a separate policy action for fast
  mode if it is gated behind its own policy toggle (not clear from the source whether
  it is a sub-toggle of the existing Anthropic policy or a new top-level toggle).

### Claim 8: The rollout of fast mode in Copilot is described as gradual

- **Evidence**: Official changelog rollout status statement.
- **Confidence**: settled (stated in official changelog)
- **Quote**: (paraphrase from WebFetch: rollout described as "gradual" — Assayer
  should verify exact phrasing)
- **Our assessment**: A gradual rollout means practitioners on eligible plan tiers
  may not see the fast mode option in the model picker immediately after June 29.
  This is operationally relevant: if fast mode doesn't appear in the picker for a
  Pro+/Max subscriber, the most likely explanation is that the rollout has not yet
  reached their account. For Ch03: note that new Copilot capabilities described as
  "gradual rollout" may require waiting for account eligibility to propagate —
  absence from the picker is not evidence of plan ineligibility.

### Claim 9: Users select fast mode through the Copilot model picker interface across supported surfaces

- **Evidence**: Official changelog UX description. Model picker is already the
  standard selection mechanism for Copilot model selection across surfaces (documented
  in `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` Claim 6 and
  `docs-github-copilot-cca-auto-model-selection.md` Claim 5).
- **Confidence**: settled (described in official changelog; consistent with existing
  model picker UX documentation)
- **Quote**: (no direct quote; described via model picker selection UX throughout
  changelog)
- **Our assessment**: Fast mode selection is per-request (at the time of model
  selection in the picker), not a session-level or account-level toggle. Practitioners
  can switch between standard Opus 4.8 and Opus 4.8 fast mode by changing their
  picker selection. However, per the Willison note (Claim 6): switching between fast
  and standard speed invalidates the prompt cache — requests at different speeds do
  not share cached prefixes. In Copilot's context, where system prompt caching
  behavior is managed by the platform, this may not be visible to users — but
  practitioners using fast mode for automated/repeated tasks should be aware of this
  underlying constraint.

## Concrete Artifacts

### Feature Availability Matrix (June 29, 2026)

```
Claude Opus 4.8 Fast Mode — GitHub Copilot Preview

SURFACES (eligible plan tiers):
  VS Code
  Visual Studio
  JetBrains IDEs
  Xcode
  Eclipse
  Copilot CLI
  GitHub Copilot cloud agent
  Copilot app
  github.com
  GitHub Mobile (iOS, Android)

PLAN ELIGIBILITY:
  Pro+:          ✓ Eligible
  Max:           ✓ Eligible
  Business:      ✓ Eligible (admin policy enablement required; off by default)
  Enterprise:    ✓ Eligible (admin policy enablement required; off by default)
  Pro:           ✗ Not listed
  Free:          ✗ Not eligible
  Student:       ✗ Not eligible

SELECTION:      Model picker on each supported surface

ROLLOUT STATUS: Gradual (as of June 29, 2026)
```

*Source: GitHub Copilot official changelog, June 29, 2026*

### Fast Mode Cost Comparison (Direct API — from cross-referenced sources)

```
Model                         Input        Output    Notes
──────────────────────────────────────────────────────────────────
Claude Opus 4.6/4.7 (fast)   $30 / MTok   $150/MTok  3x more expensive
Claude Opus 4.8 (standard)    $5 / MTok    $25 / MTok  baseline
Claude Opus 4.8 (fast)       $10 / MTok   $50 / MTok  2x standard
```

*Source: Anthropic fast mode documentation and Opus 4.8 announcement,
as documented in `blog-simonwillison-llm-anthropic-0251.md` (Claim 5 pricing table).*

*Note: Copilot Usage Based Billing uses "provider list pricing" per this changelog.
The above API prices reflect direct Anthropic pricing; Copilot may apply multipliers
or credits on top. Practitioners should consult the Copilot UBB documentation for
exact Copilot-context token costs.*

### Enterprise Admin Enablement (June 29, 2026)

```
For Business and Enterprise plans:

Policy:  "Enable fast mode for Claude Opus 4.8"
Default: Off (must be explicitly enabled)
Path:    Copilot settings → [fast mode policy for Opus 4.8]
         (exact navigation path not specified in changelog)

Effect when enabled:   Developers on the org can select Opus 4.8 fast
                       mode from the model picker across all supported surfaces.
Effect when disabled:  Opus 4.8 fast mode does not appear in the model picker
                       even for eligible plan subscribers.
```

*Source: GitHub Copilot official changelog, June 29, 2026*

## Cross-References

- **Corroborates** `blog-simonwillison-llm-anthropic-0251.md` (Claims 4, 5):
  The Willison note documented "Up to 2.5x higher output tokens per second" as the
  fast mode performance claim (Claim 4) and Opus 4.8 fast mode pricing at $10/$50
  per MTok vs. $30/$150 for prior generations (Claim 5). This changelog uses
  qualitative framing ("significantly faster," "reduced cost compared to previous fast
  modes") that is fully consistent with those quantitative claims. The two sources
  are complementary: the Willison note provides the technical depth; this changelog
  provides the Copilot-platform availability context.

- **Extends** `blog-simonwillison-llm-anthropic-0251.md` (Claim 7): The Willison
  note (dated May 28, 2026) documented that fast mode "launches as a research preview
  on the Claude API, including Claude Managed Agents, only. It is not available on
  third-party platforms, including Vertex AI, Amazon Bedrock, and Microsoft Foundry."
  This June 29, 2026 announcement represents the first documented expansion of fast
  mode beyond the direct Anthropic API to a third-party hosting platform (GitHub
  Copilot). This does not contradict the Willison note — it documents a subsequent
  platform expansion approximately one month after initial launch. GitHub Copilot is
  distinct from the three excluded platforms (Vertex AI, Bedrock, Foundry); its
  addition is an expansion of the initial "Claude API + Managed Agents only" scope.
  The Willison Claim 7 remains accurate for its stated date (May 28); this source
  establishes a new access path as of June 29. Guide content citing Willison Claim 7
  should add a qualifier: "as of June 29, 2026, GitHub Copilot was added as an
  additional access path for fast mode."

- **Extends** `docs-github-copilot-agent-model-selection.md` (Claims 1, 5): That
  April 2026 source documented model selection for Claude and Codex agents on GitHub,
  with a two-layer governance model (subscription + admin policy). This source adds
  fast mode as a new model variant within the same governance architecture — admin
  policy enablement for B/E, plan-tier gating, model picker selection. The governance
  pattern is identical; fast mode is a new option within the existing framework.

- **Extends** `docs-github-copilot-cca-auto-model-selection.md` (Claim 1): That May
  2026 source documented auto model selection for the Copilot cloud agent surface.
  This source adds fast mode as an explicit pinned-model option on the same surface.
  Practitioners using CCA now have three selection modes: auto (routes by system
  health/performance), standard Opus 4.8 (pinned), or Opus 4.8 fast mode (pinned,
  fast). The guide should present these three options together as the full CCA model
  selection surface.

- **Extends** `docs-github-copilot-free-student-auto-only-model-selection.md`
  (Claim 1): That June 24 source established that Free and Student plans have
  auto-only model selection with no manual picker. Fast mode is therefore
  inaccessible to those plan tiers on two independent grounds: (1) plan ineligibility
  (explicitly excluded from fast mode access), and (2) no manual picker to select it.
  These constraints compound: even if plan eligibility were extended, Free/Student
  users would need a picker restore before they could access fast mode.

- **Corroborates** `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md`
  (Claim 6): That June 22 source documented the model picker gaining `/models` slash
  command support for both Copilot CLI and the Claude agent in JetBrains. Fast mode
  as a new model picker option on the same surface is consistent with and directly
  accessible via that `/models` picker enhancement. The two announcements are 7 days
  apart and together define the current JetBrains model picker landscape.

- **Novel**:
  - **First documentation of fast mode availability on a GitHub-integrated Copilot
    surface**: No prior corpus source documents fast mode within GitHub Copilot
    (across VS Code, JetBrains, Xcode, Eclipse, Visual Studio, CLI, cloud agent, app,
    web, and mobile). The `blog-simonwillison-llm-anthropic-0251.md` note documented
    fast mode only for direct Anthropic API and `llm` CLI access.
  - **First corpus documentation of the plan-tier boundary for fast mode in a
    third-party platform**: The plan-tier restriction (Pro+/Max/Business/Enterprise;
    Pro/Free/Student excluded) is specific to GitHub Copilot's pricing model and is
    not previously documented for any platform hosting fast mode.
  - **First corpus documentation of the admin policy requirement for fast mode in
    enterprise Copilot deployments**: The off-by-default policy for B/E plan
    organizations is a new governance data point not covered by any prior source.
  - **First corpus documentation of the breadth of Copilot surfaces supporting fast
    mode**: The 9+ surface list (including mobile, Eclipse, Xcode) establishes that
    fast mode is platform-wide, not surface-specific — a claim that no prior corpus
    source could make.

## Guide Impact

- **Chapter 03 (Tools & Infrastructure for AI-Native Work)**: Add Claude Opus 4.8
  fast mode as a model option for GitHub Copilot users on Pro+/Max/Business/Enterprise
  plans. Distinguish from standard Opus 4.8: faster output throughput (up to 2.5x
  OTPS per `blog-simonwillison-llm-anthropic-0251.md` Claim 4); same intelligence;
  2x input cost premium; best for interactive coding and agentic workflows. Note the
  gradual rollout and admin policy requirement for B/E. Do NOT cite the 2.5x figure
  from this changelog — it doesn't contain it; cite the Willison note for the metric.

- **Chapter 04 (Build-time Patterns — IDE Tooling and Integrations)**: Document fast
  mode as a picker-selectable option alongside standard Opus 4.8 across all supported
  Copilot surfaces. Key practitioner guidance: (1) eligibility is plan-gated (Pro+ and
  above), (2) B/E orgs need admin policy enablement, (3) gradual rollout means the
  picker option may not appear immediately, (4) switching between fast and standard mode
  invalidates the prompt cache (per `blog-simonwillison-llm-anthropic-0251.md` Claim 6
  — this is a critical operational constraint for cost management). Recommend fast mode
  for: streaming-heavy interactive workflows, real-time agentic tasks where lower latency
  is visible to users. Recommend standard Opus 4.8 for: cost-sensitive batch tasks,
  workloads where total throughput is not the bottleneck.

- **Chapter 01 (Daily Workflows)**: Update model selection guidance for Copilot users to
  include fast mode as an option. Practical heuristic: start with standard Opus 4.8;
  switch to fast mode when streaming latency is causing friction in interactive sessions.
  The 2x cost premium should be justified by the use case — don't default to fast mode
  for all tasks just because it's available. The plan-tier gate means free/student users
  don't need to consider it.

- **Chapter 05 (Team Adoption / Enterprise Governance)**: For organizations on Business
  or Enterprise plans considering fast mode: (1) the feature is off by default — admins
  must make a deliberate choice to enable it; (2) enabling fast mode for developers
  increases per-request Copilot cost on UBB (2x input token cost vs. standard); (3)
  organizations should define a policy on when developers are authorized to use fast mode
  vs. standard Opus. Reference the broader fast mode admin policy pattern alongside the
  Anthropic Claude policy enablement already documented in
  `docs-github-copilot-agent-model-selection.md` (Claim 5).

## Extraction Notes

1. **Source is a short changelog (~200–300 words)**: All substantive claims are
   captured above. The source is intentionally brief as a GitHub changelog entry.
   All key facts (surfaces, plan tiers, pricing direction, admin policy, rollout
   status) are exhausted in the 9 claims.
2. **Quote fidelity caveat**: Both WebFetch calls returned AI-processed content,
   not raw HTML. The most critical quote — "delivers significantly faster output
   token speeds while maintaining the same intelligence as Claude Opus 4.8" — was
   returned consistently across both independent WebFetch calls and is likely
   verbatim. Quotes marked as "paraphrase from WebFetch" in the claim bodies should
   be verified by the Assayer against the live source URL before the PR is merged.
3. **Cross-reference verification performed**:
   - `blog-simonwillison-llm-anthropic-0251.md` Claims 4, 5, 6, 7 confirmed by
     reading the full note (lines 50–80): Claim 4 = 2.5x OTPS; Claim 5 = $10/$50
     Opus 4.8 fast mode pricing; Claim 6 = cache invalidation on speed switch;
     Claim 7 = "not available on third-party platforms."
   - `docs-github-copilot-agent-model-selection.md` Claim 5 confirmed (lines 100–116):
     two-layer governance model, admin policy enablement, stated in official changelog.
   - `docs-github-copilot-free-student-auto-only-model-selection.md` Claim 1 confirmed
     (lines 41–57): "Copilot Free and Student plans will now use Copilot auto model
     selection as the default and only model selection experience."
   - `docs-github-copilot-cca-auto-model-selection.md` Claim 1 confirmed (lines 43–58):
     CCA auto mode documented as of May 14, 2026.
   - `docs-github-copilot-jetbrains-claude-agent-provider-june2026.md` Claim 6
     confirmed (lines 153–169): /models picker command supporting both Copilot CLI and
     Claude agent.
4. **No contradictions to file**: The Willison note's Claim 7 ("not available on
   third-party platforms") is superseded in a sequential/timeline sense by this
   announcement, not contradicted. Both claims are true at their respective dates;
   the availability scope expanded. The guide should note this timeline in any section
   that cites Willison Claim 7. No contradiction issue is warranted.
5. **Fast mode cache behavior in Copilot**: The Anthropic fast mode documentation
   (cited in the Willison note) documents that switching speeds invalidates the prompt
   cache. In GitHub Copilot, prompt caching behavior is managed by the platform. The
   impact of this constraint in Copilot's managed context is not addressed by this
   source. The guide should note this uncertainty: the cache invalidation caveat from
   the direct API may or may not apply identically to how Copilot manages caching
   internally.
6. **Pro vs. Pro+**: The source lists eligible plans as Pro+, Max, Business, and
   Enterprise. Standard Copilot Pro ($10/month) is NOT listed. This is a meaningful
   distinction that could trip up practitioners who assume "I have Copilot" means they
   have fast mode access.
