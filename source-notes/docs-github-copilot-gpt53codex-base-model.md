---
source_url: https://github.blog/changelog/2026-05-17-gpt-5-3-codex-is-now-the-base-model-for-copilot-business-and-enterprise
source_type: docs
title: "GPT-5.3-Codex is now the base model for Copilot Business and Enterprise"
author: GitHub (official changelog)
date_published: 2026-05-17
date_extracted: 2026-05-18
last_checked: 2026-05-18
status: current
confidence_overall: settled
issue: "#797"
---

# GPT-5.3-Codex is Now the Base Model for Copilot Business and Enterprise

> GitHub's May 17, 2026 changelog establishing GPT-5.3-Codex as the default
> fallback model for all Copilot Business and Enterprise organizations — replacing
> GPT-4.1, introducing the first-ever LTS (long-term support) model designation
> with a 12-month availability guarantee, and signalling GPT-4.1's deprecation
> alongside usage-based billing on June 1, 2026.

## Source Context

- **Type**: docs (GitHub official product changelog, May 17, 2026; approximately
  250 words)
- **Author credibility**: GitHub engineering team announcing a production change
  to the Copilot Business and Enterprise model baseline. Authoritative for: which
  model is now the base, which plan tiers are affected, LTS status and dates, and
  billing multiplier. Not a credible source for: capability comparison between
  GPT-5.3-Codex and GPT-4.1, the specific methodology behind the cited "code
  survival rate" metric, or when GPT-5.3-Codex itself will eventually be deprecated
  beyond the LTS window.
- **Scope**: Base model change for Copilot Business and Enterprise only. Covers:
  the new base model identity, the definition of "base model" in the enterprise
  context, LTS designation and 12-month window, premium request multiplier (1x),
  GPT-4.1 deprecation timeline, and plan scope. Does NOT cover: changes to Copilot
  Pro, Pro+, or Free; capability differences between the old and new base model; any
  required administrator actions; or what happens to organizations that have already
  approved specific models via their internal review process.

## Extracted Claims

### Claim 1: GPT-5.3-Codex replaced GPT-4.1 as the base model for all Copilot Business and Copilot Enterprise organizations on May 17, 2026

- **Evidence**: Official GitHub Copilot changelog, effective date is the publication
  date of the announcement.
- **Confidence**: settled (authoritative product fact stated directly in official changelog)
- **Quote**: "GPT-5.3-Codex is now the base model for all Copilot Business and
  Copilot Enterprise organizations, replacing GPT-4.1."
- **Our assessment**: This is the first corpus source to designate GPT-5.3-Codex as
  a default/baseline for any Copilot plan tier — prior notes documented it as
  "available" for explicit selection (`docs-github-copilot-agent-model-selection.md`
  Claim 3) and as the "suggested alternative" for GPT-5.2-Codex deprecation
  (`docs-github-copilot-gpt52-deprecation.md` Claim 2). The shift from "available
  option" to "default base model" is a meaningful governance event: organizations
  that have not yet configured an explicit model policy will now receive GPT-5.3-Codex
  as their fallback. For Ch02: this anchors the model selection landscape for
  Business/Enterprise practitioners who defer to vendor defaults.

### Claim 2: The base model is the model an organization receives when no other models have been approved through its internal security review process

- **Evidence**: Official changelog definition provided directly in the announcement.
- **Confidence**: settled (definitional; stated directly in official changelog)
- **Quote**: "The base model is used when your organization hasn't yet approved other
  models through its internal review process."
- **Our assessment**: This definition reveals an important governance dynamic. Enterprise
  Copilot model access depends on completing an internal security/safety review for
  each model an organization wants to use. Organizations mid-review — or that have not
  begun reviewing GPT-5.3-Codex — will now fall back to GPT-5.3-Codex as the base
  even if they have not reviewed it themselves. The implicit assumption is that the LTS
  designation and GitHub/OpenAI partnership backstop provides sufficient confidence for
  Business/Enterprise as a baseline. For Ch05: enterprise teams that maintain rigorous
  AI model approval processes should be aware their base model changed automatically on
  May 17 regardless of their review status.

### Claim 3: GPT-5.3-Codex is the first long-term support (LTS) model in GitHub Copilot, developed in partnership with OpenAI

- **Evidence**: Official changelog states this designation explicitly. No prior LTS
  designation exists in the corpus for any Copilot model.
- **Confidence**: settled (product designation stated directly in official changelog)
- **Quote**: "GPT-5.3-Codex is also the first long-term support (LTS) model, in
  partnership with OpenAI."
- **Our assessment**: This is the most significant novel claim in the source. The LTS
  designation addresses the concern raised in `docs-github-copilot-gpt52-deprecation.md`
  Claim 7 — that model lifecycle cadence in Copilot is measurable in weeks, making
  hardcoded model identifiers risky. An LTS model breaks from that pattern: practitioners
  and enterprise teams can now rely on a 12-month availability guarantee when building
  configurations referencing GPT-5.3-Codex. For Ch02 and Ch05: document that Copilot's
  model landscape now has at least two lifecycle categories — standard (rapid deprecation,
  weeks to months) and LTS (12-month guarantee). This bifurcation matters for
  practitioners deciding whether to pin a specific model identifier or prefer auto-routing.

### Claim 4: GPT-5.3-Codex will remain available through February 4, 2027 for Copilot Business and Enterprise users — a full 12 months from its February 5, 2026 launch

- **Evidence**: Launch date and end-of-LTS date stated explicitly in the changelog.
- **Confidence**: settled (authoritative dates stated in official changelog)
- **Quote**: "GPT-5.3-Codex launched on February 5, 2026 and will remain available
  through February 4, 2027 for Copilot Business and Copilot Enterprise users."
- **Our assessment**: The 12-month window gives enterprise teams a concrete planning
  horizon. This is the first explicit model stability commitment in the corpus. For
  teams building harnesses or integrations that reference GPT-5.3-Codex explicitly,
  this guarantee means the configuration is defensible until at least February 2027
  — a marked contrast with GPT-5.2-Codex (available in Copilot agent selection from
  approximately April 14, 2026 per `docs-github-copilot-agent-model-selection.md`;
  deprecated June 1, 2026 — roughly 7 weeks). For Ch02: when advising on whether to
  pin a model vs. use auto-routing, LTS status is a key conditioning variable.

### Claim 5: GitHub cites a "significantly high code survival rate among enterprise customers" for GPT-5.3-Codex as justification for the base model selection, without specifying the metric value

- **Evidence**: GitHub Copilot data cited in the changelog; no percentage, baseline,
  or comparison model provided.
- **Confidence**: anecdotal (vendor metric referenced without specifics; no methodology
  or baseline for comparison)
- **Quote**: "GPT-5.3-Codex has a significantly high code survival rate among
  enterprise customers."
- **Our assessment**: "Code survival rate" — presumably the fraction of AI-assisted
  code that passes review and is retained rather than immediately discarded — is an
  interesting quality signal. However, the claim is unverifiable without the specific
  percentage, the comparison baseline (vs. GPT-4.1? vs. other models?), or the
  methodology. The guide should note this metric exists as a quality dimension worth
  tracking, while flagging that this instance of it is a vendor assertion without
  supporting data. For Ch02: code survival rate is a practitioner-useful quality
  metric distinct from benchmark scores — worth tracking in internal harnesses even
  if GitHub has not published its methodology.

### Claim 6: GPT-5.3-Codex carries a 1x premium request unit multiplier as the new base model

- **Evidence**: Official changelog, billing multiplier stated directly.
- **Confidence**: settled (billing fact stated directly in official changelog)
- **Quote**: "GPT-5.3-Codex carries a 1x premium request unit multiplier."
- **Our assessment**: The previous base model, GPT-4.1, was and remains force-enabled
  at a 0x multiplier until June 1, 2026. This means the shift from GPT-4.1 to
  GPT-5.3-Codex as the base model represents a cost change for organizations that
  were implicitly relying on GPT-4.1's 0x fallback. After June 1, GPT-4.1 disappears
  and organizations are left with GPT-5.3-Codex (1x) as their baseline. For Ch04/Ch05:
  enterprise finance and procurement teams reviewing Copilot budgets should account for
  this transition — the effective floor cost for model usage rises from 0x to 1x after
  the usage-based billing launch on June 1, 2026.

### Claim 7: GPT-4.1 will remain force-enabled at a 0x premium request multiplier temporarily but will deprecate alongside the usage-based billing launch on June 1, 2026

- **Evidence**: Official changelog; timeline stated directly.
- **Confidence**: settled (deprecation timeline and billing coupling stated in official changelog)
- **Quote**: "GPT-4.1 will remain force-enabled at a 0x multiplier for the time being,
  though it will deprecate alongside the launch of usage-based billing on June 1, 2026."
- **Our assessment**: This creates a May 17–June 1 transition window where both
  GPT-4.1 (0x, force-enabled) and GPT-5.3-Codex (1x, new base) are available. After
  June 1, GPT-4.1 disappears and usage-based billing activates simultaneously. The
  coupling of a model deprecation with a billing model launch is notable — organizations
  should treat June 1 as a joint governance event requiring both model-policy review
  and billing-configuration review. Corroborates `docs-github-copilot-gpt52-deprecation.md`
  Claim 5 (enterprise administrators must proactively enable replacement models before
  June 1 or face silent workflow failures).

### Claim 8: The base model change applies exclusively to Copilot Business and Enterprise plans; Copilot Pro, Pro+, and Free are unaffected

- **Evidence**: Official changelog, explicit plan scope stated.
- **Confidence**: settled (scope stated directly in official changelog)
- **Quote**: "These changes apply to Copilot Business and Copilot Enterprise plans
  only. They don't apply to Copilot Pro, Copilot Pro+, or Copilot Free."
- **Our assessment**: Consistent with the pattern that model-selection governance
  features are gated on Business/Enterprise tiers
  (`docs-github-copilot-agent-model-selection.md` Claim 5). Individual plans (Pro,
  Pro+, Free, Student) continue to operate under separate model access rules — see
  `docs-github-copilot-individual-plan-changes.md` and
  `docs-github-copilot-student-gpt53codex-picker-removal.md` for those tiers.
  For Ch05: enterprise governance documentation should explicitly note that base model
  configuration is a Business/Enterprise-tier concern and does not apply to
  individual-tier Copilot subscriptions.

### Claim 9: The LTS and base model changes were announced on March 18, 2026 — nearly two months before the May 17, 2026 effective date

- **Evidence**: Key dates section of the changelog states both dates explicitly.
- **Confidence**: settled (dates stated directly in official changelog)
- **Quote**: (from the Key dates section) "March 18, 2026: LTS and base model changes
  announced" and "May 17, 2026: GPT-5.3-Codex becomes the base model for all Copilot
  Business and Copilot Enterprise organizations"
- **Our assessment**: The approximately 60-day lead time between announcement and
  effective date is notably longer than other Copilot model changes in the corpus.
  The GPT-5.2-Codex deprecation (`docs-github-copilot-gpt52-deprecation.md`, May 1
  announcement, June 1 effective date) gave approximately 30 days. This longer runway
  aligns with the enterprise governance context: a base model change that affects all
  Business/Enterprise organizations requires more preparation time than a single model
  deprecation. For Ch05: document the 60-day announcement window as evidence that
  GitHub is calibrating lead times to enterprise operational reality for base model
  changes.

## Concrete Artifacts

### Key Dates for GPT-5.3-Codex Base Model Transition (from changelog)

```
GitHub Copilot — GPT-5.3-Codex Base Model Timeline

February 5, 2026:   GPT-5.3-Codex launched
March 18, 2026:     LTS designation and base model change announced
May 17, 2026:       GPT-5.3-Codex becomes base model for Business/Enterprise
                    (GPT-4.1 force-enabled at 0x as fallback during transition)
June 1, 2026:       GPT-4.1 deprecates; usage-based billing launches
                    (GPT-5.3-Codex at 1x becomes the effective cost floor)
February 4, 2027:   End of GPT-5.3-Codex LTS availability window

Applies to: Copilot Business, Copilot Enterprise
Does NOT apply to: Copilot Pro, Pro+, Free
```

*Source: GitHub Copilot official changelog, May 17, 2026*

### GPT-5.3-Codex LTS Model Summary

```
Model:          GPT-5.3-Codex (OpenAI)
LTS status:     First LTS model for GitHub Copilot
Partnership:    In partnership with OpenAI
Launch date:    February 5, 2026
LTS end:        February 4, 2027 (12-month guarantee)
Multiplier:     1x premium request unit

Base model definition:
  Used when an organization has not yet approved other models
  through its internal security/safety review process.

Quality signal:
  "Significantly high code survival rate among enterprise customers"
  (no specific percentage or methodology published)

Prior base model:
  GPT-4.1 (0x multiplier) — deprecates June 1, 2026
```

*Source: GitHub Copilot official changelog, May 17, 2026*

### Copilot Model Lifecycle Categories (derived from corpus)

```
GitHub Copilot model lifecycle (as of May 2026):

STANDARD lifecycle:
  Typical availability: weeks to months after introduction before deprecation
  Example: GPT-5.2-Codex — available ~April 14, deprecated June 1 (~7 weeks)
  Harness advice: prefer auto-routing or admin-policy-managed selection;
                  avoid pinning specific model version strings

LTS (Long-Term Support) lifecycle:
  Guarantee: available for 12 months from model launch date
  Example: GPT-5.3-Codex — Feb 5, 2026 to Feb 4, 2027
  Harness advice: safe to pin in configurations for the LTS window;
                  still monitor GitHub changelog for any policy changes

AUTO-ONLY (picker-removed but auto-retained):
  Access: via auto model selection only (no explicit picker)
  Example: GPT-5.3-Codex on Copilot Student (as of April 27, 2026)
  Harness advice: cannot be explicitly pinned; auto routing may or may
                  not select it depending on plan/policy/rate-limit state
```

*Derived from this source and corpus cross-references*

## Cross-References

- **Corroborates** `docs-github-copilot-gpt52-deprecation.md` Claim 2: That source
  designated GPT-5.3-Codex as the suggested replacement for GPT-5.2-Codex (deprecated
  June 1, 2026). This source confirms GPT-5.3-Codex is now the official base model for
  Business/Enterprise — the two notes together complete the picture of how GPT-5.3-Codex
  came to occupy the primary slot in the Copilot Business/Enterprise model hierarchy.

- **Corroborates** `docs-github-copilot-gpt52-deprecation.md` Claim 5: That source
  warned that Enterprise admins who do not proactively enable replacement models before
  June 1 will face silent workflow failures. This source adds: GPT-5.3-Codex is already
  the base model as of May 17, and GPT-4.1 (the prior fallback) disappears June 1 —
  organizations that have been implicitly relying on GPT-4.1 as their zero-cost fallback
  should treat June 1 as a forced migration date even without explicit action.

- **Corroborates** `docs-github-copilot-cli-auto-model-selection.md` Claim 3: The CLI
  auto model pool (as of April 17, 2026) already included GPT-5.3-Codex. The base model
  elevation is consistent with GPT-5.3-Codex's positioning as the primary OpenAI Codex
  model in Copilot's auto routing infrastructure.

- **Extends** `docs-github-copilot-agent-model-selection.md` Claim 3 and Claim 5:
  That source (April 14, 2026) documented GPT-5.3-Codex as an available selection option
  for Business/Enterprise cloud coding agents, and described the two-layer admin governance
  model. This source adds a new dimension: GPT-5.3-Codex is now the model organizations
  receive if they have not completed model approval. The governance implication shifts —
  the base model is what fills the gap before enterprise security review completes, making
  model approval timelines more operationally urgent.

- **Extends** `docs-github-copilot-gpt52-deprecation.md` Claim 7: That note inferred
  "hardcoded model identifiers in Copilot workflows have a shelf life measurable in weeks,
  not months or years." The LTS designation for GPT-5.3-Codex refines this inference:
  the rapid-deprecation pattern applies to standard-lifecycle models; LTS models are an
  explicit exception with a 12-month guarantee. The guide advice to "prefer auto-routing
  over pinning" remains sound for standard-lifecycle models, but LTS status is the
  conditioning variable that makes explicit pinning of GPT-5.3-Codex defensible for
  configurations targeting Business/Enterprise. This is a nuance, not a true
  contradiction — see Extraction Notes.

- **Extends** `docs-github-copilot-student-gpt53codex-picker-removal.md`: That source
  (April 27, 2026) documented GPT-5.3-Codex being removed from the explicit picker for
  the Student plan (free educational tier) while remaining in the auto pool. This source
  (May 17, 2026) documents GPT-5.3-Codex simultaneously elevated to the base model for
  paid Business/Enterprise tiers. The juxtaposition is striking: on the same timeline,
  GitHub is narrowing GPT-5.3-Codex access for the free educational tier while expanding
  it to default status for paid tiers. This is the clearest evidence yet that Copilot's
  model access strategy is deliberately tiered: premium tiers receive broader and more
  stable access, while free tiers receive constrained and less predictable access.

- **Novel**:
  - First source in corpus to document the LTS (long-term support) model designation
    for any Copilot or GitHub AI product. This concept — a vendor-committed 12-month
    availability guarantee for a specific model — is not documented elsewhere in the
    corpus and directly addresses the rapid-deprecation concern raised by practitioners.
  - First source to define the "base model" concept in the Copilot context: the model
    used before organizational security review completes. This is a distinct governance
    construct not previously named in the corpus.
  - First explicit 12-month model stability commitment in the corpus from a cloud AI
    coding platform vendor.
  - First source to document "code survival rate" as a quality metric cited by GitHub
    when justifying model selection decisions — a practitioner-useful metric concept
    not yet named in the guide.

## Guide Impact

### Chapter 02: Harness Engineering / Tooling Landscape

- **LTS status as a model-pinning decision variable**: Add explicit guidance that
  GPT-5.3-Codex is the first LTS model in Copilot, guaranteed available through
  February 4, 2027. For practitioners building configurations on Copilot Business/Enterprise
  that need to reference a specific model identifier, GPT-5.3-Codex is the defensible
  choice — it is the only Codex-family model with an explicit 12-month commitment.
  Contrast with the standard-lifecycle guidance (prefer auto-routing) from
  `docs-github-copilot-cli-auto-model-selection.md` and `docs-github-copilot-gpt52-deprecation.md`.
- **Model lifecycle taxonomy**: The corpus now has evidence for three Copilot model
  lifecycle states: standard (weeks to months), LTS (12-month guarantee), and
  auto-only (picker-removed, auto-accessible). The guide should explain this taxonomy
  when advising on model selection and configuration strategy.
- **Code survival rate as a quality metric**: Name "code survival rate" as an
  AI-assisted coding quality metric worth tracking internally — the fraction of AI-suggested
  code that survives code review and is retained. GitHub has begun citing it as a model
  selection signal, making it a useful benchmarking dimension for teams building internal
  AI coding metrics programs.

### Chapter 05: Team Adoption / Enterprise Governance

- **Base model as a governance gap-filler**: Enterprise teams should understand that the
  base model activates when internal model review has not been completed. This makes
  model approval timelines operationally consequential: delays in review mean teams use
  the base model (GPT-5.3-Codex) rather than a model they have reviewed and explicitly
  approved. Governance frameworks should account for the base model as a distinct
  operational state, not just an edge case.
- **June 1, 2026 as a joint governance event**: Two changes land simultaneously —
  GPT-4.1 deprecates and usage-based billing launches. Enterprise teams should treat
  this as a single coordinated planning item: (1) audit whether any workflows rely on
  GPT-4.1 or the 0x fallback cost assumption; (2) confirm GPT-5.3-Codex is enabled in
  model policy settings; (3) update billing projections to reflect the 1x floor cost
  replacing the 0x fallback.
- **Tiered access as a model access philosophy**: The contrast between Student plan
  (GPT-5.3-Codex removed from picker) and Business/Enterprise (GPT-5.3-Codex elevated
  to base model) on approximately the same timeline reveals GitHub's access philosophy:
  stability and breadth scale with subscription tier. Teams advising mixed-tier
  developer populations (some on Student, some on Business) should document that the
  same model name implies very different access semantics depending on the plan tier.

## Extraction Notes

1. **Source is short by design**: The changelog is approximately 250 words. All
   substantive claims are exhausted in nine claims above. The source does not
   provide: capability comparison between GPT-5.3-Codex and GPT-4.1, details on
   the internal review process that determines when the base model applies, specific
   code survival rate metrics, or guidance for organizations mid-review on May 17.
2. **LTS qualification scope**: The changelog specifies the LTS availability window
   applies to "Copilot Business and Copilot Enterprise users." It does not address
   whether the LTS guarantee extends to direct OpenAI API access to GPT-5.3-Codex
   outside of Copilot, or to other Copilot plan tiers.
3. **No contradiction filed**: The LTS claim refines rather than contradicts the
   inference in `docs-github-copilot-gpt52-deprecation.md` Claim 7 (rapid lifecycle
   cadence). That claim was tagged "emerging" and explicitly framed as an inference
   from a single deprecation event. The LTS designation adds a category exception —
   the general principle (prefer auto or admin-managed selection for standard models)
   remains sound; LTS status is the condition under which explicit pinning becomes
   defensible. The two claims are complementary, not contradictory. No contradiction
   issue required.
4. **"Announced March 18, 2026" reference**: The changelog refers to an earlier
   announcement. This note does not speculate about what that earlier announcement
   contained; the May 17 changelog is treated as the operative effective-date source.
5. **WebFetch returned structured content with high fidelity**: The verbatim
   quotes in Claims 1–8 were confirmed across two fetches of the source URL and are
   presented with high confidence as verbatim excerpts from the page.
