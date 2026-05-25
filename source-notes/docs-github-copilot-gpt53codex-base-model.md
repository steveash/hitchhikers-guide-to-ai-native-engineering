---
source_url: https://github.blog/changelog/2026-05-17-gpt-5-3-codex-is-now-the-base-model-for-copilot-business-and-enterprise
source_type: docs
title: "GPT-5.3-Codex is now the base model for Copilot Business and Enterprise"
author: GitHub (official changelog)
date_published: 2026-05-17
date_extracted: 2026-05-25
last_checked: 2026-05-25
status: current
confidence_overall: settled
issue: "#797"
---

# GPT-5.3-Codex Is Now the Base Model for Copilot Business and Enterprise

> GitHub's May 17, 2026 changelog documenting the transition of GPT-5.3-Codex from
> an available model to the default base model for all Copilot Business and Enterprise
> organizations, replacing GPT-4.1 — and announcing GitHub's first LTS model designation,
> with a 12-month availability guarantee through February 2027.

## Source Context

- **Type**: docs (GitHub official product changelog, approximately 250 words)
- **Author credibility**: GitHub engineering team announcing a production product change.
  Authoritative for the fact of the base-model switch, the LTS designation, the pricing
  structure during transition, the plan scope, and the rollout timeline. Not a source for
  why GPT-5.3-Codex was selected over alternatives, how "code survival rate" is measured,
  or whether practitioners will observe quality improvements relative to GPT-4.1.
- **Scope**: The default model change for Copilot Business and Copilot Enterprise plans,
  effective May 17, 2026. Covers: new base model identity (GPT-5.3-Codex), prior base model
  (GPT-4.1), LTS designation details, pricing during transition (GPT-4.1 at 0x, GPT-5.3-Codex
  at 1x), plan scope (Business/Enterprise only), performance claim ("code survival rate"),
  and the June 1 deadline for usage-based billing launch and GPT-4.1 full deprecation. Does
  NOT cover: how GPT-5.3-Codex was selected over GPT-5.4 or GPT-5.5 as the base model,
  what "code survival rate" means or how it is measured, whether there is a UI change in
  the model picker, capability differences between GPT-5.3-Codex and GPT-4.1, or how
  organizations can pin an alternative model if they prefer not to use the new default.

## Extracted Claims

### Claim 1: GPT-5.3-Codex is now the default base model for all Copilot Business and Copilot Enterprise organizations, replacing GPT-4.1, effective May 17, 2026

- **Evidence**: Official GitHub Copilot changelog, stated as a completed product change
  effective the publication date.
- **Confidence**: settled (authoritative product fact — both the new model and the replaced
  model are stated directly in the official changelog)
- **Quote**: "GPT-5.3-Codex is now the base model for all Copilot Business and Copilot
  Enterprise organizations"
- **Our assessment**: This is the central operational fact of the source. Business and
  Enterprise organizations that have not pinned a specific model are now running GPT-5.3-Codex
  as their default. This is a significant shift from GPT-4.1 and represents GitHub's
  deliberate choice to move to a Codex-family model as the foundation for paid enterprise
  tiers. For Ch02: the guide's model selection guidance for Business/Enterprise Copilot
  users should note that GPT-5.3-Codex is the new default and that practitioners who
  previously relied on GPT-4.1 defaults now have a different model without any configuration
  action required. Organizations that need to control which model runs as default must
  explicitly pin an alternative through admin model policies.

### Claim 2: GPT-5.3-Codex is GitHub's first long-term support (LTS) model, in partnership with OpenAI, with a 12-month availability guarantee

- **Evidence**: Official changelog explicitly designates this as the first LTS model.
  The 12-month window is stated via specific dates: launched February 5, 2026, available
  through February 4, 2027.
- **Confidence**: settled (LTS designation and availability dates stated directly in
  official changelog)
- **Quote**: "GPT-5.3-Codex is also our first long-term support (LTS) model, in partnership
  with OpenAI."
- **Our assessment**: This is the most novel and strategically significant claim in the
  source. No prior source in the corpus documents a vendor-committed availability guarantee
  for a specific Copilot model. The LTS designation addresses a major governance concern
  documented across multiple prior deprecation notices: that model identifiers in GitHub
  Copilot configurations have a shelf life measurable in weeks (see
  `docs-github-copilot-gpt52-deprecation.md` Claim 7 and `docs-github-copilot-gpt41-deprecation.md`
  Claim 5 for the rapid lifecycle cadence evidence). An LTS model inverts this problem:
  practitioners who build automation, harness configurations, or team workflows around
  GPT-5.3-Codex can rely on it being available until at least February 4, 2027. For Ch02
  and Ch05: the LTS designation should be prominently noted as a practical design signal —
  practitioners who want stable, predictable model availability should prefer LTS-designated
  models when building configurations that will not be actively maintained.

### Claim 3: The LTS availability window for GPT-5.3-Codex runs from February 5, 2026 through February 4, 2027 — 12 months

- **Evidence**: Specific dates stated in the official changelog.
- **Confidence**: settled (dates stated directly)
- **Quote**: "GPT-5.3-Codex launched on February 5, 2026 and will remain available through
  February 4, 2027"
- **Our assessment**: The LTS window started at model launch (February 5, 2026) and runs for
  exactly 12 months. As of the May 17, 2026 announcement, approximately 8.5 months of LTS
  availability remain. Practitioners making technology decisions in mid-2026 should factor
  in the February 2027 boundary — configurations built around GPT-5.3-Codex will require
  review by Q4 2026 for the post-LTS transition. For Ch05: include the LTS end date in any
  enterprise Copilot governance calendar. No successor LTS model is named in this source.

### Claim 4: GPT-5.3-Codex carries a 1x premium request unit multiplier; GPT-4.1 is temporarily force-enabled at 0x during the transition period

- **Evidence**: Pricing structure stated in official changelog with specific multiplier values.
- **Confidence**: settled (multiplier values stated directly in official changelog)
- **Quote**: "GPT-5.3-Codex carries a 1x premium request unit multiplier"
- **Our assessment**: The 1x multiplier for GPT-5.3-Codex means that Business/Enterprise
  organizations switching from GPT-4.1 as default will see their premium request consumption
  increase — GPT-4.1 at 0x was effectively free in premium request terms. GitHub is softening
  this transition by force-enabling GPT-4.1 at 0x temporarily, giving organizations time to
  adjust their usage patterns and budgets before June 1. The June 1, 2026 date (when usage-
  based billing launches and GPT-4.1 is fully deprecated) is the hard transition point at
  which this subsidy ends. For Ch05: enterprise billing teams should plan for an increase in
  premium request consumption after June 1 if their organizations were previously on GPT-4.1
  defaults. The gap between GPT-4.1's 0x and GPT-5.3-Codex's 1x is the most concrete
  financial impact of this change.

### Claim 5: The base model change applies exclusively to Copilot Business and Copilot Enterprise — Copilot Pro, Pro+, and Free are unaffected

- **Evidence**: Official changelog explicitly scopes the change to Business and Enterprise
  plans and explicitly excludes individual plans.
- **Confidence**: settled (plan scope stated directly and explicitly)
- **Quote**: "These changes apply to Copilot Business and Copilot Enterprise plans only.
  They don't apply to Copilot Pro, Copilot Pro+, or Copilot Free."
- **Our assessment**: This is a clear governance boundary. Individual plan users (Pro, Pro+,
  Free) on Copilot are not affected by this default switch and should not see a change in
  their default model behavior from this announcement. For Ch05: enterprise governance
  teams managing Copilot Business or Enterprise rollouts should communicate this change
  to their engineering teams — developers who rely on the Copilot default without explicitly
  selecting a model have a different model as of May 17. Individual plan users on the same
  team using personal Copilot subscriptions may have a different default, creating a
  surface-level inconsistency within the same development team's tooling.

### Claim 6: GitHub cites "significantly high code survival rate among enterprise customers" as the performance basis for choosing GPT-5.3-Codex as the base model

- **Evidence**: Official changelog quotes a performance metric without specifying measurement
  methodology, comparison baseline, or the magnitude of "significantly high."
- **Confidence**: anecdotal (metric name stated in official source; no measurement definition,
  comparative baseline, or sample size provided)
- **Quote**: "GPT-5.3-Codex has a significantly high code survival rate among enterprise
  customers"
- **Our assessment**: "Code survival rate" is a product metric not previously defined in
  the corpus. It likely refers to the proportion of AI-generated code that persists in
  production rather than being reverted or immediately modified — a proxy for code acceptance
  and durability. However, GitHub does not define the metric, provide baseline comparison
  to GPT-4.1 or other models, cite the sample size, or specify measurement period. The
  claim is therefore taken as vendor marketing support for the choice, not as independently
  verifiable evidence. For the guide: this is worth noting as an instance of a code-quality
  metric (survival rate) that practitioners should consider tracking internally, even though
  GitHub does not expose it as a self-serve metric. If teams track which AI-generated code
  blocks survive code review and production deployment, they can build their own model
  quality signal independent of vendor claims.

### Claim 7: June 1, 2026 is the date both usage-based billing launches and GPT-4.1 is fully deprecated

- **Evidence**: Official changelog states the June 1 date as the convergence point for two
  events: usage-based billing activation and GPT-4.1 deprecation. This is corroborated by
  `docs-github-copilot-gpt41-deprecation.md` Claim 1, which documented June 1 as the
  GPT-4.1 deprecation date.
- **Confidence**: settled (date stated directly; cross-corroborated by existing source note)
- **Quote**: (no single verbatim quote; the June 1 date appears in the source timeline
  section referencing both billing launch and GPT-4.1 deprecation)
- **Our assessment**: June 1, 2026 is now a compound governance event for Business/Enterprise
  Copilot administrators: (1) GPT-4.1 is removed, ending the 0x force-enabled subsidy, and
  (2) usage-based billing activates, changing the cost model. Organizations that have not
  prepared for both changes before June 1 face a simultaneous budget and model availability
  disruption. The March 18, 2026 announcement date (when the change was first announced)
  gave organizations roughly 75 days of preparation time before the May 17 effective date,
  and approximately 105 days before the June 1 billing/deprecation cutover. For Ch05:
  document June 1 as a compound event requiring coordinated action from both model admins
  (ensure alternative models are enabled) and finance/billing teams (budget for premium
  request consumption from the new 1x default model).

### Claim 8: Organizations with concerns or needing more time on the transition can contact their account team

- **Evidence**: Official changelog provides this as the stated escalation path.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "If your team has questions or needs more time, contact your account team."
- **Our assessment**: The existence of an account-team escalation path implies GitHub
  may offer transition accommodations (timeline extensions, billing adjustments) for
  enterprise customers on a case-by-case basis. This is notable because prior deprecation
  notices (`docs-github-copilot-gpt52-deprecation.md` and `docs-github-copilot-gpt41-deprecation.md`)
  offered the same account-team contact without specifying what accommodations were
  available. For Ch05: enterprise AI governance teams should treat account-team outreach
  as a legitimate governance option when platform changes create compliance or budget
  challenges. This is not a public opt-out mechanism, but it suggests flexibility exists
  for enterprise relationships.

## Concrete Artifacts

### Timeline of Key Events (from changelog)

```
GitHub Copilot GPT-5.3-Codex Base Model Transition

February 5, 2026:  GPT-5.3-Codex launched (LTS window begins)

March 18, 2026:    Base model change announced (75 days before effective date)

May 17, 2026:      BASE MODEL CHANGE EFFECTIVE
                   - GPT-5.3-Codex becomes default for all Business and Enterprise orgs
                   - GPT-4.1 force-enabled at 0x multiplier (temporary subsidy)
                   - GPT-5.3-Codex at 1x premium request multiplier

June 1, 2026:      TWO SIMULTANEOUS EVENTS
                   - Usage-based billing activates for Copilot
                   - GPT-4.1 deprecated (0x force-enable ends)

February 4, 2027:  LTS window closes for GPT-5.3-Codex

Source: GitHub Copilot official changelog, May 17, 2026
```

### Plan Scope Summary

```
Who is affected by the base model change:

  Copilot Business:    YES — GPT-5.3-Codex is now the default base model
  Copilot Enterprise:  YES — GPT-5.3-Codex is now the default base model

  Copilot Pro:         NO — not affected
  Copilot Pro+:        NO — not affected
  Copilot Free:        NO — not affected

Source: "These changes apply to Copilot Business and Copilot Enterprise plans only.
         They don't apply to Copilot Pro, Copilot Pro+, or Copilot Free."
```

### Pricing Structure During Transition

```
GitHub Copilot Premium Request Multipliers (May 17 – June 1, 2026 transition)

  GPT-5.3-Codex (new base model):  1x premium request multiplier
  GPT-4.1 (prior base model):      0x — force-enabled temporarily
                                   (available at no premium cost during transition)

After June 1, 2026:
  GPT-4.1 deprecated — 0x force-enable removed
  GPT-5.3-Codex remains at 1x
  Usage-based billing activates

Enterprise action required before June 1:
  [ ] Ensure model policies include GPT-5.3-Codex or a preferred alternative
  [ ] Budget for 1x multiplier consumption replacing 0x GPT-4.1 default
  [ ] Contact account team if more transition time is needed

Source: GitHub Copilot official changelog, May 17, 2026
```

### LTS Designation Details

```
GitHub Copilot First LTS Model

Model:             GPT-5.3-Codex
Partner:           OpenAI
LTS Window:        February 5, 2026 – February 4, 2027 (12 months)
Applicable plans:  Copilot Business, Copilot Enterprise (as base model)
                   (model is available on other surfaces too, per prior notes)

LTS guarantee:     Model availability guaranteed for duration of LTS window
                   (GitHub's stated commitment; mechanism for post-LTS transition
                    not specified in this announcement)

Successor LTS:     Not announced

Source: GitHub Copilot official changelog, May 17, 2026
        "GPT-5.3-Codex is also our first long-term support (LTS) model,
         in partnership with OpenAI."
        "GPT-5.3-Codex launched on February 5, 2026 and will remain
         available through February 4, 2027"
```

## Cross-References

- **Extends** `docs-github-copilot-agent-model-selection.md` Claim 3: That April 14, 2026
  source documented GPT-5.3-Codex as *available* for selection on GitHub cloud coding agents
  alongside GPT-5.2-Codex and GPT-5.4. This source (May 17, 2026) establishes it as the
  *default base model* for Business/Enterprise organizations — a materially different
  designation. The guide's model selection advice for B/E Copilot users should now reflect
  that GPT-5.3-Codex is not just an option but the default for those tiers.

- **Corroborates** `docs-github-copilot-gpt41-deprecation.md` Claim 1: That May 7, 2026
  source documented GPT-4.1 as scheduled for deprecation on June 1, 2026. This source
  confirms GPT-4.1 was the prior base model for Business/Enterprise (what GPT-5.3-Codex is
  "replacing"). The two sources together complete the GPT-4.1 picture: it was the default
  for B/E, then deprecated June 1 with GPT-5.5 as the official migration target for any
  workflows that explicitly pinned it. No contradiction: GPT-5.3-Codex replaces GPT-4.1 as
  the *default*; GPT-5.5 is the recommended *explicit pinning target* for workflows that
  referenced GPT-4.1 by name. Different contexts, not contradictory.

- **Extends** `docs-github-copilot-gpt52-deprecation.md` Claim 2: That May 1, 2026 source
  designated GPT-5.3-Codex as the replacement for GPT-5.2-Codex in deprecation terms. This
  source now adds a second role for GPT-5.3-Codex: it is also the designated base model for
  B/E tiers. GPT-5.3-Codex is simultaneously the replacement path for GPT-5.2-Codex and the
  default for B/E organizations — a convergent designation reinforcing GPT-5.3-Codex as
  GitHub's primary Codex-family workhorse for enterprise use in 2026.

- **Corroborates** `docs-github-copilot-cli-auto-model-selection.md` Claim 3: The CLI auto
  pool already included GPT-5.3-Codex (as of April 17, 2026) alongside GPT-5.4, Sonnet 4.6,
  and Haiku 4.5. This source's LTS designation for GPT-5.3-Codex provides a retrospective
  rationale for its inclusion in the auto pool: GitHub likely prioritized the LTS model for
  auto routing to provide stability. The 12-month LTS window also suggests the auto pool
  will not need to replace GPT-5.3-Codex until at least February 2027.

- **Extends** `docs-github-copilot-student-gpt53codex-picker-removal.md` Claim 1: The
  April 27, 2026 source documented removal of GPT-5.3-Codex from the Student plan picker
  (retaining it only via auto). This source, three weeks later, designates GPT-5.3-Codex
  as the Business/Enterprise base model. The two together reveal a deliberate product-tier
  strategy: constrain GPT-5.3-Codex on the Student (free educational) tier while elevating
  it as the default on paid enterprise tiers. GPT-5.3-Codex is simultaneously more
  restricted for free users and more prominent for paying organizations.

- **Complements** `docs-github-copilot-web-model-consolidation.md`: That May 20, 2026
  source (three days after this one) documented removal of Gemini models and other variants
  from Copilot web chat, retaining only OpenAI and Claude families. Together, the two sources
  characterize a May 2026 Copilot model consolidation strategy: designate a single stable
  Codex model as the enterprise default (this source) while simultaneously narrowing the
  web interface to recommended models (that source). GitHub is reducing option complexity
  for enterprise and web users simultaneously, trading breadth for stability and clarity.

- **Contradicts**: None. The claim that GPT-5.3-Codex replaces GPT-4.1 as base model is
  not contradicted by any prior corpus note. The LTS designation is novel with no
  conflicting claim. No contradiction issue required.

- **Novel**:
  - **First LTS model designation in GitHub Copilot history**: No prior source in the corpus
    documents a vendor-committed availability guarantee for any Copilot model. The LTS concept
    is entirely new to this corpus and addresses the fragility concern documented repeatedly
    in deprecation notes.
  - **First explicit base-model designation per paid tier**: Prior corpus sources document
    model options, auto pools, and deprecation targets — but none document which model is the
    designated *default* for a specific subscription tier. This is the first source to name
    the base model for B/E Copilot explicitly.
  - **Code survival rate as a quality metric**: This is the first mention of "code survival
    rate" as a performance signal in the corpus. Even as an undefined vendor claim, it
    introduces a metric concept worth documenting.
  - **0x force-enable mechanism during transition**: No prior source documents a "force-enable
    at 0x" mechanism for a deprecated model during a transition period. This is a novel
    product mechanism where the old model remains accessible at no premium cost while
    practitioners migrate.

## Guide Impact

### Chapter 02: Harness Engineering / Tooling Landscape

- **GPT-5.3-Codex as the Copilot B/E default**: Update any model roster or model selection
  guidance for GitHub Copilot Business/Enterprise users. As of May 17, 2026, the default is
  GPT-5.3-Codex (1x multiplier), not GPT-4.1. Teams that have not pinned a specific model
  should verify their actual default behavior matches expectations. Document the transition
  from a 0x (GPT-4.1) to a 1x (GPT-5.3-Codex) default as a budget-relevant change
  effective June 1 when usage-based billing activates.
- **LTS as a design primitive for harness configurations**: Add guidance that practitioners
  building Copilot-dependent configurations (scripts, CI integrations, harness tooling) should
  prefer LTS-designated models when stability matters more than accessing the latest capability.
  GPT-5.3-Codex (LTS through February 2027) is the only current LTS model. Organizations
  can reference it as a stable configuration target through at least Q4 2026.

### Chapter 05: Team Adoption / Enterprise Governance

- **Default model change as a governance event**: Teams managing Copilot for Business or
  Enterprise should treat default model changes as governance-relevant events. Developers
  who relied on GPT-4.1 defaults without realizing it are now on GPT-5.3-Codex. Governance
  processes should include a mechanism to notify development teams when the platform changes
  their default model — this is a silent behavioral change at the practitioner level.
- **June 1, 2026 compound deadline**: Frame June 1 as a compound event for B/E Copilot
  administrators: GPT-4.1 deprecation (remove 0x force-enable) + usage-based billing
  activation. Both require coordinated preparation: model admin enables replacement models;
  finance teams adjust premium request budgets; teams using automated workflows that
  reference GPT-4.1 by name update their configurations before the cutover.
- **LTS planning horizon**: Recommend enterprise Copilot governance calendars include the
  LTS boundary date (February 4, 2027 for GPT-5.3-Codex). Organizations that adopt
  GPT-5.3-Codex as their pinned model based on the LTS guarantee should begin successor
  planning by November 2026 to avoid a reactive migration in early 2027.
- **Tier-specific model defaults create team inconsistency**: Individual developers on
  Copilot Pro or Free subscriptions have a different default than their B/E colleagues.
  Teams mixing subscription tiers (enterprise org with some Pro+ individual users, or
  contractors on individual plans) should document that model defaults are not uniform
  across plans and ensure that any quality or reproducibility expectations account for
  this inconsistency.

## Extraction Notes

1. **WebFetch returned structured summaries, not raw HTML**: Two separate WebFetch calls
   to the source URL returned structured markdown summaries of the page content. Verbatim
   quotes in Claims 1, 2, 3, 4, 5, 6, and 8 are reproduced as they appeared in the
   WebFetch output in quotation marks attributed to the source. The Assayer should verify
   key quotes against the live source URL before treating them as character-for-character
   verbatim. Claims 7's June 1 date and the multiplier for GPT-4.1 (0x) are drawn from
   structured summary content and may be paraphrased in the WebFetch output.
2. **Source is short by design**: The changelog is approximately 250 words. All substantive
   claims are exhausted in the eight claims above. The source provides no methodology for
   the "code survival rate" metric, no comparison between GPT-5.3-Codex and GPT-4.1
   quality, and no mechanism for organizations to opt out of the base model change.
3. **No successor LTS model announced**: This source does not name what follows GPT-5.3-Codex
   as LTS. The February 2027 boundary is the only forward-looking date provided.
4. **"Force-enabled at 0x" mechanism**: The GPT-4.1 force-enable at 0x during transition
   is inferred from the WebFetch summary stating "GPT-4.1 remains force-enabled at 0x
   multiplier temporarily." This phrasing appeared in one WebFetch call; the mechanism is
   consistent with the overall transition design described in the source.
5. **No contradictions filed**: No existing corpus source claims that GPT-4.1 was not the
   prior base model, that GPT-5.3-Codex was not available, or that LTS models do not exist
   in Copilot. No contradiction issue required.
