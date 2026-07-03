---
source_url: https://github.blog/changelog/2026-06-30-claude-sonnet-5-is-generally-available-for-github-copilot
source_type: docs
title: "Claude Sonnet 5 is generally available for GitHub Copilot"
author: GitHub (official changelog)
date_published: 2026-06-30
date_extracted: 2026-07-02
last_checked: 2026-07-02
status: current
confidence_overall: settled
issue: "#1432"
---

# Claude Sonnet 5 Is Generally Available for GitHub Copilot

> GitHub's June 30, 2026 changelog announcing general availability of Claude
> Sonnet 5 across ten GitHub Copilot surfaces — the first corpus documentation
> of Sonnet 5 in Copilot, published one day after Claude Opus 4.8 fast mode
> entered preview, reusing the identical surface list and administration
> pattern from that announcement while adding a first-in-corpus mention of
> Zero Data Retention (ZDR) for a specific Copilot model.

## Source Context

- **Type**: docs (GitHub official product changelog, June 30, 2026; approximately
  150 words of primary announcement text, "1 minute read")
- **Author credibility**: GitHub engineering team announcing a production GA
  feature. Authoritative for: the fact that Claude Sonnet 5 is now GA in
  Copilot, the list of supported surfaces, plan eligibility, the billing model,
  and the ZDR operating claim. Not a credible source for: specific benchmark
  scores or quantitative performance numbers (the changelog uses qualitative
  language — "strong results," "particularly strong performance" — with no
  numbers), comparison to Claude Sonnet 4.6's performance, exact pricing figures
  (the source says "provider list pricing" without quoting a rate card), or how
  Sonnet 5 fits into GitHub Copilot's auto model selection routing pool.
- **Scope**: GA availability of Claude Sonnet 5 within GitHub Copilot — supported
  plans, supported platforms, billing treatment, admin enablement for
  Business/Enterprise, and the ZDR operating condition. Does NOT cover:
  quantitative benchmark results, direct-API pricing for Sonnet 5, whether
  Sonnet 5 replaces or coexists with Sonnet 4.6 in the model picker, auto model
  selection pool membership, or the reasoning-effort-level mechanics referenced
  by the "lower effort levels" phrase.

## Extracted Claims

### Claim 1: Claude Sonnet 5 is now generally available in GitHub Copilot as of June 30, 2026, positioned as Anthropic's latest Sonnet-class model for everyday development and agentic workflows

- **Evidence**: Official GitHub product changelog announcing GA status directly
  in the title and opening paragraph.
- **Confidence**: settled (product fact — the feature is released and documented
  by GitHub engineering)
- **Quote**: "Claude Sonnet 5 is Anthropic's latest Sonnet-class model, now
  available in GitHub Copilot. It brings strong coding performance to everyday
  development and agentic workflows, giving developers a new Sonnet-class option
  for tasks across the IDE and CLI."
- **Our assessment**: This is the first corpus documentation of Claude Sonnet 5
  in GitHub Copilot. The prior current-generation Sonnet in the roster was
  Sonnet 4.6 (established GA in `docs-github-copilot-agent-model-selection.md`
  Claim 2 and confirmed as the deprecation successor to the base Sonnet 4 in
  `docs-github-copilot-claude-sonnet4-deprecation.md` Claim 1). Sonnet 5's GA
  arrival supersedes Sonnet 4.6 as the current Sonnet-class option, though the
  changelog does not state whether Sonnet 4.6 remains selectable alongside it or
  is being phased out. For Ch02: update the model roster to add Claude Sonnet 5
  as the current-generation Sonnet option as of June 30, 2026; flag Sonnet 4.6's
  status as unconfirmed pending a future deprecation notice or roster update.

### Claim 2: In GitHub's internal testing, Claude Sonnet 5 showed strong results across coding scenarios, with particularly strong performance on CLI-style tasks

- **Evidence**: Official changelog performance framing, stated as GitHub's own
  internal testing conclusion rather than a third-party benchmark citation.
- **Confidence**: anecdotal (vendor-reported internal testing result; no
  benchmark name, task set, or numeric score is disclosed)
- **Quote**: "In our internal testing, Claude Sonnet 5 showed strong results
  across a range of coding scenarios, including particularly strong performance
  on CLI-style tasks."
- **Our assessment**: The "CLI-style tasks" emphasis is notable because it
  aligns with GitHub's own CLI-first agent tooling emphasis (Copilot CLI, `gh`
  extensions) documented across `docs-github-copilot-cli-auto-model-selection.md`
  and `docs-github-copilot-agent-skills-cli.md`. However, "internal testing" with
  no disclosed methodology is the weakest evidentiary tier the guide accepts —
  it should not be cited as a capability claim without qualification. For Ch04:
  if the guide adds Sonnet 5 to a model comparison table, mark the CLI-task
  performance claim as vendor-asserted, not independently verified.

### Claim 3: Claude Sonnet 5 shows excellent prompt-cache utilization and competitive latency at lower effort levels

- **Evidence**: Official changelog technical framing, presented as a
  differentiator for "developers seeking fast, capable Sonnet-class performance."
- **Confidence**: anecdotal (vendor-reported characteristic; no cache hit-rate
  numbers or latency figures given)
- **Quote**: "excellent prompt-cache utilization and competitive latency at
  lower effort levels"
- **Our assessment**: The phrase "lower effort levels" implies Sonnet 5 supports
  a configurable reasoning-effort parameter, consistent with the "configurable
  reasoning levels" capability GitHub documented for Copilot models in
  `docs-github-copilot-1m-context-reasoning-levels.md` (Claim 2 area) roughly
  four weeks earlier (June 4, 2026). This changelog does not itself explain what
  effort levels are available for Sonnet 5 or how to configure them — it assumes
  the reader already understands the mechanism from the June 4 announcement. For
  Ch04: cross-reference the reasoning-level configuration guidance from that
  earlier note when documenting Sonnet 5's effort-level behavior; this changelog
  only confirms that Sonnet 5 participates in that mechanism and that lower
  effort settings retain competitive latency and cache efficiency.

### Claim 4: Claude Sonnet 5 is billed at provider list pricing under Usage Based Billing, with no promotional or discounted rate

- **Evidence**: Official changelog billing statement, given as a standalone
  sentence with no further detail.
- **Confidence**: settled (billing treatment stated directly in official
  changelog)
- **Quote**: "This model is billed at provider list pricing under Usage Based
  Billing."
- **Our assessment**: No specific per-token rate is disclosed in this source,
  unlike the Opus 4.8 fast mode announcement which at least gestured at relative
  pricing tiers (documented in `docs-github-copilot-opus48-fast-mode-preview.md`
  Claim 6). Practitioners need to consult GitHub's models-and-pricing
  documentation (linked from this changelog) for the actual UBB multiplier. For
  Ch04: do not assume Sonnet 5 carries any launch discount — "provider list
  pricing" signals standard-rate billing from day one of GA, unlike some prior
  Copilot model introductions that included promotional periods.

### Claim 5: Claude Sonnet 5 is available on Copilot Pro, Pro+, Max, Business, and Enterprise plans — notably including the standard Pro tier, unlike the Opus 4.8 fast mode preview which excluded Pro

- **Evidence**: Official changelog plan eligibility list, compared against the
  plan list in `docs-github-copilot-opus48-fast-mode-preview.md` Claim 5
  (Pro+, Max, Business, Enterprise — Pro explicitly excluded).
- **Confidence**: settled (plan list stated directly in official changelog)
- **Quote**: "Claude Sonnet 5 will be available to Copilot Pro, Pro+, Max,
  Business, and Enterprise users."
- **Our assessment**: This is a meaningful contrast with the immediately
  preceding Opus 4.8 fast mode announcement (one day earlier), which gated
  access above standard Pro. Sonnet 5 GA reaches the full paid tier ladder
  including the $10/month Pro plan, consistent with Sonnet-class models
  historically being positioned as the broadly-accessible tier (vs. Opus-class
  models as the premium tier) — a distinction also visible in the CLI auto pool
  (`docs-github-copilot-cli-auto-model-selection.md` Claim 3: Sonnet 4.6 and
  Haiku 4.5 included in the cost-bounded auto pool; no Opus tier included). Free
  and Student plans are not listed and are therefore excluded, consistent with
  the auto-only restriction already documented for those tiers in
  `docs-github-copilot-free-student-auto-only-model-selection.md`.

### Claim 6: Claude Sonnet 5 rolls out across ten platforms — VS Code, Visual Studio, Copilot CLI, GitHub Copilot cloud agent, the Copilot App, github.com, GitHub Mobile (iOS and Android), JetBrains, Xcode, and Eclipse — an identical surface list to the Opus 4.8 fast mode preview announced one day earlier

- **Evidence**: Official changelog platform list, compared directly against the
  surface list in `docs-github-copilot-opus48-fast-mode-preview.md` Claim 4 (VS
  Code, Visual Studio, Copilot CLI, GitHub Copilot cloud agent, Copilot app,
  github.com, GitHub Mobile iOS/Android, JetBrains, Xcode, Eclipse).
- **Confidence**: settled (platform list stated directly in official changelog)
- **Quote**: "Visual Studio Code, Visual Studio, Copilot CLI, GitHub Copilot
  cloud agent, GitHub Copilot App, github.com, GitHub Mobile (iOS and Android),
  JetBrains, Xcode, Eclipse"
- **Our assessment**: The surface list is a verbatim match to the Opus 4.8 fast
  mode preview list from June 29. This is strong evidence that GitHub now
  maintains a single, standardized "full Copilot surface" rollout template that
  new model announcements plug into, rather than negotiating surface coverage
  per model. For Ch02: practitioners can now expect that any new frontier model
  GitHub adds to Copilot will appear across this same ten-surface set roughly
  simultaneously, rather than rolling out to IDEs first and other surfaces
  later — a operational planning simplification versus the surface-by-surface
  rollout patterns documented in earlier 2026 changelogs (e.g., the JetBrains-
  specific and Eclipse-specific model announcements catalogued elsewhere in this
  corpus).

### Claim 7: The Sonnet 5 rollout is described as gradual, meaning eligible-plan practitioners may not see it immediately

- **Evidence**: Official changelog rollout status statement.
- **Confidence**: settled (stated in official changelog)
- **Quote**: "Rollout will be gradual."
- **Our assessment**: Identical rollout framing to the Opus 4.8 fast mode
  announcement (`docs-github-copilot-opus48-fast-mode-preview.md` Claim 8:
  "gradual"). This confirms gradual rollout is GitHub's standard practice for
  new model introductions in Copilot, not a one-off caveat. For Ch03: absence of
  Sonnet 5 from a practitioner's model picker immediately after June 30, 2026
  should be read as normal rollout lag, not plan ineligibility — consistent with
  the guidance already established for the Opus 4.8 fast mode rollout.

### Claim 8: Copilot Enterprise and Business plan administrators can enable Claude Sonnet 5 through model policy settings

- **Evidence**: Official changelog administration statement.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Copilot Enterprise and Copilot Business plan administrators can
  enable Claude Sonnet 5 for their organization through the model policy
  settings in Copilot."
- **Our assessment**: The changelog does not state whether the policy is off by
  default (as it explicitly was for Opus 4.8 fast mode, per
  `docs-github-copilot-opus48-fast-mode-preview.md` Claim 7) or on by default.
  This is a gap relative to the fast mode announcement's explicit "off by
  default" language. For Ch05: flag this ambiguity — enterprise admins should
  verify Sonnet 5's policy state directly in Copilot settings rather than
  assuming parity with the fast mode default-off pattern, since GitHub did not
  repeat that qualifier here. This is consistent with the general governance
  pattern (admin policy enablement required for Business/Enterprise; see also
  `docs-github-copilot-agent-model-selection.md` Claim 5) but less precisely
  specified than in the immediately preceding fast mode announcement.

### Claim 9: Claude Sonnet 5 operates under Zero Data Retention (ZDR) in GitHub Copilot

- **Evidence**: Official changelog administration section statement, stated as a
  standalone operating condition alongside the admin enablement claim.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Like other Sonnet models in GitHub Copilot, Claude Sonnet 5
  operates under Zero Data Retention (ZDR)."
- **Our assessment**: This is the first corpus source to state a ZDR operating
  condition for a specific named model within GitHub Copilot. No other Copilot
  model-availability changelog in this corpus (including the Opus 4.8 fast mode
  preview, the Sonnet 4 deprecation notice, or the April 2026 Claude/Codex model
  selection announcement) mentions ZDR as an explicit per-model claim. The source
  does clarify the scope: the leading clause "Like other Sonnet models in GitHub
  Copilot" establishes that ZDR is a pre-existing property of the Sonnet tier in
  Copilot, not a new condition specific to Sonnet 5 — Sonnet 5 inherits it rather
  than introducing it. What the source does *not* address is whether the same ZDR
  condition applies to Opus-tier Claude models in Copilot; it speaks only to
  "other Sonnet models." For Ch05 (enterprise governance / data handling): this is
  a concrete, citable data point for compliance-conscious teams evaluating whether
  Copilot's Claude Sonnet 5 integration meets data retention requirements, and it
  can be generalized to the Sonnet tier as a whole. The open question that remains
  is narrower than parity across all Claude models: does ZDR also cover Opus-class
  models in Copilot, or is it stated here only for the Sonnet tier?

## Concrete Artifacts

### Feature Availability Summary (June 30, 2026)

```
Claude Sonnet 5 — GitHub Copilot General Availability

PLANS:
  Pro:           Eligible
  Pro+:          Eligible
  Max:           Eligible
  Business:      Eligible (admin enablement via model policy settings)
  Enterprise:    Eligible (admin enablement via model policy settings)
  Free:          Not listed / not eligible
  Student:       Not listed / not eligible

PLATFORMS (10):
  Visual Studio Code
  Visual Studio
  Copilot CLI
  GitHub Copilot cloud agent
  GitHub Copilot App
  github.com
  GitHub Mobile (iOS and Android)
  JetBrains
  Xcode
  Eclipse

BILLING:      Provider list pricing under Usage Based Billing
DATA HANDLING: Operates under Zero Data Retention (ZDR)
ROLLOUT:       Gradual
```

*Source: GitHub Copilot official changelog, June 30, 2026*

### Plan Eligibility Contrast: Sonnet 5 GA vs. Opus 4.8 Fast Mode Preview (one day apart)

```
                        Opus 4.8 fast mode      Claude Sonnet 5
                        (June 29, 2026)          (June 30, 2026)
                        ------------------       ------------------
Pro                     NOT listed               Eligible
Pro+                    Eligible                 Eligible
Max                     Eligible                 Eligible
Business                Eligible (admin gate)    Eligible (admin gate)
Enterprise              Eligible (admin gate)    Eligible (admin gate)
Free / Student          Not eligible             Not listed / not eligible
Admin policy default    Off by default (stated)  Not stated
Platforms               10 surfaces              Identical 10 surfaces
Rollout                 Gradual                  Gradual
ZDR mentioned            No                       Yes
```

*Derived from this source and
`docs-github-copilot-opus48-fast-mode-preview.md`*

## Cross-References

- **Corroborates** `docs-github-copilot-opus48-fast-mode-preview.md` (Claims 4,
  7): the identical ten-surface platform list and identical "gradual" rollout
  language, published one day apart, confirm GitHub now uses a standardized
  full-surface rollout template for new Claude model introductions in Copilot
  rather than negotiating platform coverage per announcement.

- **Extends** `docs-github-copilot-agent-model-selection.md` (Claim 2): that
  April 14, 2026 source documented the Claude model roster on github.com as
  Sonnet 4.5, Sonnet 4.6, Opus 4.5, Opus 4.6. This source adds Claude Sonnet 5
  as a new current-generation Sonnet-class entry as of June 30, 2026 — the
  roster from that note is now stale for the Sonnet tier and should be updated.

- **Extends** `docs-github-copilot-claude-sonnet4-deprecation.md` (Claim 1):
  that May 7, 2026 source established Claude Sonnet 4.6 as the GA successor to
  the deprecated base Claude Sonnet 4. This source documents Sonnet 4.6 being
  superseded in turn by Sonnet 5 as the current Sonnet-class GA option, roughly
  seven weeks later — evidence of a fast Sonnet-tier release cadence in Copilot
  (Sonnet 4 → deprecated May 6; Sonnet 4.6 → current as of May 7; Sonnet 5 → GA
  June 30, all within an eight-week window).

- **Extends** `docs-github-copilot-1m-context-reasoning-levels.md`: that June 4,
  2026 source documented configurable reasoning/effort levels as a Copilot
  capability without naming which models support it. This source's "competitive
  latency at lower effort levels" phrase confirms Sonnet 5 participates in that
  reasoning-level mechanism, providing the first named-model confirmation for
  that feature in this corpus.

- **Extends** `docs-github-copilot-cli-auto-model-selection.md` (Claim 3): that
  April 17, 2026 source documented the CLI auto pool as GPT-5.4, GPT-5.3-Codex,
  Sonnet 4.6, and Haiku 4.5, bounded to 0x–1x multiplier models. This source
  does not state whether Sonnet 5 joins the auto pool or at what multiplier —
  a gap the guide should flag rather than assume; the auto pool note itself
  cautioned that "the available models will evolve over time."

- **Corroborates** `docs-github-copilot-free-student-auto-only-model-selection.md`
  (Claim 1): Free and Student plans' absence from the Sonnet 5 plan list is
  consistent with those plans already being restricted to auto-only model
  selection with no manual picker as of June 24, 2026.

- **Novel**:
  - First corpus documentation of Claude Sonnet 5 anywhere in GitHub Copilot.
  - First corpus confirmation that Zero Data Retention (ZDR) applies to the
    Claude Sonnet tier in GitHub Copilot generally — the source states Sonnet 5
    operates under ZDR "like other Sonnet models," so this is a pre-existing
    tier property surfaced explicitly for the first time in the corpus, not a
    Sonnet-5-specific novelty. No prior Copilot model-availability note in the
    corpus states a ZDR condition at all.
  - First evidence that GitHub is reusing an identical ten-surface rollout
    template across consecutive model announcements (Opus 4.8 fast mode, June
    29; Sonnet 5 GA, June 30), suggesting a standardized release process rather
    than per-model surface negotiation.

## Guide Impact

- **Chapter 02 (Harness Engineering / Tooling Landscape)**: Update the GitHub
  Copilot model roster to add Claude Sonnet 5 as the current-generation
  Sonnet-class GA option as of June 30, 2026, available on Pro and above (unlike
  Opus 4.8 fast mode, which requires Pro+ or higher). Note that Sonnet 4.6's
  continued availability alongside Sonnet 5 is not confirmed by this source —
  do not assume Sonnet 4.6 is deprecated without a separate deprecation notice.
  Add the ten-surface rollout list as the current "full Copilot surface"
  baseline practitioners should expect for future model announcements.

- **Chapter 04 (Context Engineering / Model Selection)**: Cross-reference the
  "lower effort levels" claim with the configurable reasoning-level guidance in
  `docs-github-copilot-1m-context-reasoning-levels.md` when documenting how to
  tune Sonnet 5's latency/reasoning-depth tradeoff in Copilot. Flag GitHub's
  internal-testing performance claims (strong on CLI-style tasks) as
  vendor-asserted rather than independently benchmarked — do not cite the
  "particularly strong performance on CLI-style tasks" claim as settled
  capability evidence without an independent source.

- **Chapter 05 (Team Adoption / Enterprise Governance)**: Add Zero Data
  Retention (ZDR) as a documented data-handling property of the Claude Sonnet
  tier in Copilot — a new, citable compliance data point. The source states
  Sonnet 5 operates under ZDR "like other Sonnet models in GitHub Copilot," so
  the guide can document ZDR as a Sonnet-tier property, not a Sonnet-5-specific
  disclosure; no follow-up check on whether ZDR applies to other *Sonnet* models
  is needed — the source already answers that. The narrower open question that
  remains is whether ZDR extends to Opus-class Claude models in Copilot, which
  this source does not address. Also note the ambiguity around whether the
  Business/Enterprise admin policy for Sonnet 5 is on or off by default (unlike
  the explicit "off by default" statement for Opus 4.8 fast mode) — recommend
  enterprise admins verify current policy state directly rather than assuming a
  default.

## Extraction Notes

1. **Source is short (~150 words, "1 minute read")**: All substantive claims are
   captured in the nine claims above. The changelog covers availability,
   billing, administration, and a brief performance framing — it does not
   include benchmark data, exact pricing, or migration guidance from Sonnet 4.6.
2. **"Additional Resources" links not separately extracted as claims**: The
   changelog links to GitHub's models-and-pricing documentation, the supported
   models documentation, and the Community feedback discussion category. These
   are navigational references, not substantive content, and were not followed
   as sub-pages per MINER.md guidance (they are general reference docs rather
   than content specific to this announcement).
3. **No admin-policy-default statement**: Unlike the Opus 4.8 fast mode
   announcement (which explicitly stated the policy is "off by default"), this
   changelog states only that admins "can enable" Sonnet 5 — it does not specify
   the default state. This ambiguity is called out explicitly in Claim 8 rather
   than assumed either way.
4. **ZDR scope — Sonnet tier confirmed, Opus tier open**: The changelog states
   Sonnet 5 operates under ZDR "like other Sonnet models in GitHub Copilot,"
   which establishes ZDR as a pre-existing property of the Sonnet tier that
   Sonnet 5 inherits — not a Sonnet-5-specific condition. This is reflected in
   Claim 9 and Guide Impact. The only ZDR scope question the source leaves open
   is whether the condition also covers Opus-class Claude models in Copilot,
   which it does not address.
5. **No contradictions to file**: No existing corpus source claims Sonnet 4.6
   is the permanent or final Claude Sonnet-class model in Copilot, or that
   Copilot models never carry ZDR. This source documents an expected model-tier
   progression and a new (not contradictory) data-handling disclosure. No
   contradiction issue required.
6. **Two Prospector triage comments on the source issue**: Issue #1432 carries
   two separate triage assessments (novelty: medium, then novelty: high) with
   slightly different chapter recommendations (Ch02/Ch04 vs. Ch02/Ch05). This
   note treats both as valid signal and addresses Ch02, Ch04, and Ch05 in Guide
   Impact rather than picking one triage comment over the other.
