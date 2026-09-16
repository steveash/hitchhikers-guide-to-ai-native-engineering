---
source_url: https://github.blog/changelog/2026-09-15-github-copilot-suggests-custom-properties-definitions
source_type: docs
title: "GitHub Copilot suggests custom properties definitions"
author: GitHub (official changelog)
date_published: 2026-09-15
date_extracted: 2026-09-16
last_checked: 2026-09-16
status: current
confidence_overall: emerging
issue: "#3472"
---

# GitHub Copilot Suggests Custom Property Definitions (GitHub Changelog)

> GitHub's September 15, 2026 changelog announces a public-preview Copilot
> feature that suggests allowed values when an admin creates a custom
> property definition for repository governance metadata, gated behind a
> new "Repository custom property suggestions" Copilot policy — an
> AI-assist layer bolted onto the existing custom-properties/rulesets
> governance mechanism rather than new governance infrastructure.

## Source Context

- **Type**: docs (GitHub official product changelog, ~185 words, tagged
  `copilot` and `platform governance`, "1 minute read"). One linked page
  followed per MINER.md §1: the docs page "Managing custom properties for
  repositories in your organization"
  (`docs.github.com/organizations/managing-organization-settings/
  managing-custom-properties-for-repositories-in-your-organization`).
- **Author credibility**: GitHub product/engineering team announcing a
  shipped (public preview) feature. Authoritative for the fact that the
  feature exists, what triggers it, and the policy that gates it. Not a
  credible source for whether the suggestions are actually good, whether
  admins adopt the one-click accept, or whether resulting metadata is more
  consistent than before — no usage data or outcome evidence is included.
- **Scope**: Covers only the value-suggestion feature at custom-property
  *creation* time and the policy toggle that controls it. Does NOT cover:
  what data or model powers the suggestions, suggestion accuracy/quality,
  whether suggestions appear when *editing* an existing property
  definition, rollout timeline to GA, or any usage metrics. The linked
  docs page (fetched directly, not just via changelog) describes custom
  properties generally (types, permissions, visibility, requirements) but,
  as of this extraction, contains **no mention at all** of the Copilot
  suggestion feature or the new policy — the docs have not yet been
  updated to reflect this changelog entry.

## Extracted Claims

### Claim 1: Copilot now suggests allowed values when an admin creates a new custom property definition, in public preview for Copilot Business and Enterprise

- **Evidence**: Stated directly in the changelog's opening sentence.
- **Confidence**: settled (a public-preview product fact, officially
  announced)
- **Quote**: "GitHub Copilot can now suggest allowed values when you
  create a custom property for repositories in your organization. This
  feature is in public preview for GitHub Copilot Business and Copilot
  Enterprise plans."
- **Our assessment**: A narrow, concrete capability — not a general "AI
  governance assistant," but a specific autocomplete-style suggestion at
  one UI step (defining allowed values for a new property). Availability
  is plan-gated (Business/Enterprise only), consistent with GitHub's
  pattern of shipping new Copilot capabilities to paid tiers first.

### Claim 2: The feature targets a specific, named adoption problem — admins don't know which properties or values to define, and inconsistent metadata undermines governance at scale

- **Evidence**: Changelog's problem-statement paragraph, framed as the
  rationale for the feature.
- **Confidence**: anecdotal (vendor's own framing of the problem; no
  independent data cited on how common this failure mode is)
- **Quote**: "Custom properties are one of the most popular ways to scope
  rulesets, but getting started has been a challenge. Admins often aren't
  sure which properties to define or what allowed values to use, and
  inconsistent metadata makes it harder to apply governance consistently
  across a large fleet of repositories."
- **Our assessment**: This is a plausible and specific failure mode —
  free-text or inconsistently-cased custom property values (e.g.
  `internet-facing: Yes` vs `true` vs `y` across different repos) would
  silently break ruleset targeting that depends on exact value matches.
  The claim that this is a *common* problem is vendor framing, but the
  underlying mechanism (schema drift in admin-entered taxonomy values) is
  a real and well-known class of governance-metadata failure, independent
  of this source.

### Claim 3: Suggestions are property-type-aware — multi-select properties surface domain-specific value sets, single-select properties surface canonical binary-style choices

- **Evidence**: The changelog gives two worked examples tied to the two
  property types it names.
- **Confidence**: settled (stated directly, with concrete examples)
- **Quote**: "Creating a multi-select property like FedRAMP surfaces
  suggested compliance-related values." / "Creating a single-select
  property like internet-facing surfaces suggested values such as yes and
  no."
- **Our assessment**: The `FedRAMP` example implies the suggestion engine
  has some domain knowledge of compliance frameworks (i.e., it doesn't
  just look at the property name syntactically — it infers a relevant
  value taxonomy, e.g., FedRAMP impact levels). The `internet-facing`
  example is a much lower bar (any boolean-shaped property name plausibly
  maps to yes/no). The two examples together suggest the feature spans a
  range from "trivial pattern match" to "actual domain knowledge," but the
  source gives no detail on how the suggestion is generated (LLM prompt,
  fixed taxonomy library, or a hybrid), so we can't assess how far the
  domain knowledge actually extends beyond these two illustrative cases.

### Claim 4: Suggested values are applied via one-click accept, framed as accelerating taxonomy setup

- **Evidence**: Stated directly in the changelog.
- **Confidence**: settled (a described UI interaction)
- **Quote**: "You can accept a suggestion in one click, helping you stand
  up a meaningful custom property taxonomy faster."
- **Our assessment**: Low-friction acceptance is a double-edged pattern
  common to AI-suggestion UIs: it lowers the cost of adopting a
  higher-quality taxonomy, but it also lowers the cost of accepting a
  suggestion without evaluating whether it actually fits the org's
  compliance/governance needs — the same "of course, why not" acceptance
  risk documented for AI code-review suggestions elsewhere in the corpus,
  just applied to governance metadata instead of code.

### Claim 5: The feature is scoped to *creating* a new custom property definition, not to editing existing ones

- **Evidence**: The changelog's mechanism sentence specifies the trigger
  condition.
- **Confidence**: settled (as stated) but the absence of edit-time
  suggestions is an inference from what the source does *not* say, not an
  explicit statement
- **Quote**: "With this release, when you create a new custom property
  definition at the enterprise or organization level, Copilot will
  suggest relevant allowed values based on the property you're defining."
- **Our assessment**: If suggestions genuinely don't extend to editing
  existing definitions, this leaves a gap: organizations that already have
  a sprawling, inconsistent set of custom properties (the exact failure
  mode Claim 2 describes) get no AI assistance cleaning up what already
  exists — the feature only helps prevent the problem from getting worse
  going forward, via new properties. This is a plausible but unconfirmed
  reading; the source simply never mentions an edit-time path.

### Claim 6: The feature is gated behind a new, distinct Copilot policy — "Repository custom property suggestions" — controllable by enterprise and organization owners

- **Evidence**: Stated directly in the changelog's closing paragraph.
- **Confidence**: settled (a named, documented policy control)
- **Quote**: "Enterprise and organization owners can now configure the
  Repository custom property suggestions Copilot policy to control
  feature availability."
- **Our assessment**: This follows GitHub's established pattern (seen
  elsewhere in the corpus, e.g. `docs-github-copilot-global-model-policy-ga.md`
  and `docs-github-copilot-cca-custom-properties.md`) of shipping new
  Copilot capabilities with a dedicated, independently toggleable policy
  rather than bundling them under a single "Copilot on/off" switch. For
  enterprises with strict AI-governance review processes, this means
  reviewing and explicitly approving each new Copilot capability
  individually is both required and feasible — but also means policy
  sprawl: the number of independently-gated Copilot policies keeps
  growing with each release.

## Concrete Artifacts

### Changelog text (verbatim, full body — fetched directly via HTTP, not AI-summarized)

```
GitHub Copilot suggests custom properties definitions
September 15, 2026 • 1 minute read

GitHub Copilot can now suggest allowed values when you create a custom
property for repositories in your organization. This feature is in
public preview for GitHub Copilot Business and Copilot Enterprise plans.

Custom properties let enterprise and organization admins attach
governance metadata to repositories, which you can then use to target
repositories with rulesets. Custom properties are one of the most
popular ways to scope rulesets, but getting started has been a
challenge. Admins often aren't sure which properties to define or what
allowed values to use, and inconsistent metadata makes it harder to
apply governance consistently across a large fleet of repositories.

With this release, when you create a new custom property definition at
the enterprise or organization level, Copilot will suggest relevant
allowed values based on the property you're defining. For example:

  - Creating a multi-select property like FedRAMP surfaces suggested
    compliance-related values.
  - Creating a single-select property like internet-facing surfaces
    suggested values such as yes and no.

You can accept a suggestion in one click, helping you stand up a
meaningful custom property taxonomy faster.

Enterprise and organization owners can now configure the Repository
custom property suggestions Copilot policy to control feature
availability.

Learn more in our docs about managing custom properties for
repositories in your organization.

Tags: copilot, platform governance
```

### Custom properties background (from linked docs page, for context — not new to this feature)

```
Custom properties are structured metadata fields attached to
repositories/organizations. Created in org settings under
Repository > Custom properties, admins define:
  - Name: up to 75 chars, [a-zA-Z0-9_\-$#]
  - Description: optional
  - Type: text string, single select, multi select, or boolean
  - Permissions: whether repository actors can set values
  - Requirements: required-for-all-repos, with defaults and
    explicit-value requirements

Visibility of a custom property's values matches repository visibility
(public repo properties are publicly viewable; internal/private repo
properties require read access).

As of 2026-09-16, this docs page contains NO reference to the Copilot
suggestion feature or the "Repository custom property suggestions"
policy — the changelog has not yet been reflected in the linked docs.
```

## Cross-References

- **Extends** `docs-github-copilot-cca-custom-properties.md`: that note
  documents custom properties as a *targeting/selection* mechanism (which
  orgs get Copilot Cloud Agent access, via `custom_properties` filters on
  the enterprise CCA API). This source documents an earlier stage of the
  same pipeline — *defining* the custom property taxonomy in the first
  place, now with Copilot assistance. Read together, the two notes cover
  most of a custom-property-driven governance lifecycle: define taxonomy
  (this source, AI-assisted) → attach values to repos → use values to
  scope rulesets or CCA policy (`docs-github-copilot-cca-custom-properties.md`).
  Notably, that note's Claim 2 documents a footgun where custom-property
  matching is evaluated once at configuration time and does not track
  later property changes — a sharp reminder that even AI-assisted,
  higher-quality taxonomy values (this source) feed into a downstream
  system that treats them as a one-time snapshot, not a live filter. An
  admin who uses this feature to clean up/standardize a property's
  allowed values after CCA policy was already configured against that
  property should not assume CCA org selection updates automatically.
- **Corroborates** `docs-github-copilot-global-model-policy-ga.md`: both
  sources document GitHub's pattern of gating a specific new Copilot
  capability behind its own dedicated, independently-configurable policy
  (there: per-model enablement policy; here: "Repository custom property
  suggestions" policy) rather than a single blanket Copilot toggle.
- **Novel**:
  - First source in corpus to document Copilot being used to assist
    *governance metadata schema design* itself (suggesting allowed values
    for custom properties), as distinct from using custom properties to
    gate or target other Copilot features (which is what
    `docs-github-copilot-cca-custom-properties.md` covers).
  - First source to note the specific failure mode this feature targets:
    inconsistent, admin-entered taxonomy values silently degrading
    ruleset-targeting accuracy at fleet scale.
  - No existing source note discusses AI-suggested values for
    compliance-taxonomy fields (e.g., FedRAMP-related values) — this is a
    new example of AI touching compliance-adjacent configuration, distinct
    from AI touching code or PRs.

## Guide Impact

- **Chapter 02 (AI-Augmented Development / Copilot)**: If the guide has a
  section on Copilot's governance/admin-facing features (as opposed to
  its code-authoring features), add this as an example of Copilot
  assisting with *metadata schema design* — a distinct capability class
  from code suggestions or PR review. Flag it as public preview,
  Business/Enterprise only, and policy-gated.
- **Chapter 05/07 (Organizations & Adoption / Enterprise Governance)**: If
  the guide discusses the growing surface area of independently-toggleable
  Copilot policies (per the pattern noted in
  `docs-github-copilot-global-model-policy-ga.md`), add this as another
  data point: "Repository custom property suggestions" is at least the
  Nth distinct Copilot policy an enterprise admin must now individually
  review. Also worth flagging as a caution: this note's cross-reference
  to the CCA custom-properties footgun (evaluated-once-at-configuration
  semantics) means that AI-standardized taxonomy values do not
  automatically propagate into already-configured downstream policies —
  a practitioner cleaning up custom property values with this feature
  should re-audit any policy (like CCA org selection) that was configured
  against the old values.

## Extraction Notes

1. The changelog page was fetched twice: once via the AI-summarizing
   WebFetch tool, and once via direct HTTP + HTML-tag-stripping to get
   character-verified raw text (saved to confirm every quote above is
   verbatim, not AI-paraphrased). Both fetches agreed on content; the raw
   fetch is what the quotes in this note are copied from. The one linked
   docs page (custom properties management guide) was also fetched both
   ways. It contains general custom-properties documentation but, as of
   2026-09-16, no mention whatsoever of the Copilot suggestion feature or
   its policy — this gap between changelog and docs update timing is
   noted explicitly in Source Context and the Concrete Artifacts section
   rather than glossed over.
2. **Thin source**: the changelog itself is ~185 words. This is a
   genuinely small feature announcement, not a deeply-linked multi-page
   topic. Six claims were extracted, fully exhausting the source's
   substantive content; padding to a higher claim count would have meant
   restating the same two example sentences in different words, which
   MINER.md explicitly warns against (paraphrase-as-new-claim).
3. **No contradictions found**: no existing source note makes a claim
   about custom-property taxonomy design or AI-assisted governance
   metadata that this source disagrees with. No contradiction issue filed.
4. **Overall confidence set to "emerging"**: the feature itself is a
   settled product fact (it shipped, it's documented), but it is public
   preview, has no usage/outcome data, and its problem-statement framing
   (Claim 2) is vendor-asserted rather than independently evidenced —
   "emerging" reflects a real-but-unproven-in-practice feature rather than
   "settled" (established, if the note graded the whole entry that
   generously) or "anecdotal" (which would undersell the concrete,
   documented, shipping nature of the feature).
