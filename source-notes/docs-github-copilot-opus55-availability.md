---
source_url: https://github.blog/changelog/2026-09-22-claude-opus-5-5-is-now-available-in-github-copilot
source_type: docs
title: "Claude Opus 5.5 is now available in GitHub Copilot"
author: GitHub (official changelog)
date_published: 2026-09-22
date_extracted: 2026-09-23
last_checked: 2026-09-23
status: current
confidence_overall: settled
issue: "#3627"
---

# Claude Opus 5.5 Is Now Available in GitHub Copilot

> GitHub's September 22, 2026 changelog announcing Claude Opus 5.5 in Copilot's
> model picker across ten surfaces (Pro+/Max/Business/Enterprise only), framed
> around an efficiency claim — comparable task resolution to Claude Opus 5 using
> "significantly fewer steps and tokens" — plus output watermarking, and the
> first Opus-tier changelog in this corpus to state the new default-on GA model
> enablement behavior explicitly.

## Source Context

- **Type**: docs (GitHub official product changelog, September 22, 2026; tagged
  "Release," a "1 minute read." Raw HTML fetched directly via `curl` to
  character-verify quotes, in addition to an AI-summarizing WebFetch pass — both
  returned consistent substance.)
- **Author credibility**: GitHub engineering/product team announcing a
  production model-availability change. Authoritative for: the fact that Opus
  5.5 is now selectable in Copilot, the surface list, plan eligibility, billing
  treatment, watermarking behavior, and the admin-enablement mechanism. Not a
  credible source for: the methodology behind the "resolved tasks comparably...
  while using significantly fewer steps and tokens" claim (no benchmark name,
  task set, or numeric figures are disclosed), or any comparison to non-Anthropic
  models in Copilot's roster.
- **Scope**: Availability of Claude Opus 5.5 within GitHub Copilot — supported
  plans, supported platforms, billing, watermarking, admin enablement, and
  rollout status. Does NOT cover: quantitative efficiency numbers (no
  step-count or token-count figures given), pricing figures (only "provider
  list pricing" is stated), whether Opus 5.5 supersedes or coexists with base
  Opus 5 in the model picker, or Opus 5.5's participation in Copilot's auto
  model selection routing pool.

## Extracted Claims

### Claim 1: Claude Opus 5.5, described as "Anthropic's newest Opus model," is now available in GitHub Copilot for agentic coding, long-running agentic tasks, and knowledge work

- **Evidence**: Official GitHub changelog, opening paragraph.
- **Confidence**: settled (product fact — the model is released and documented
  by GitHub engineering)
- **Quote**: "Claude Opus 5.5, Anthropic's newest Opus model, is now available
  in GitHub Copilot. You can use it for agentic coding, long-running agentic
  tasks, and knowledge work."
- **Our assessment**: This is the first dedicated Copilot-availability
  changelog for an Opus 5-generation model documented in this corpus. Base
  Claude Opus 5 (launched July 24, 2026, per
  `blog-simonwillison-introducing-opus-5.md`) appears in the corpus only as a
  *suggested deprecation successor* for Opus 4.5/4.6 in
  `docs-github-copilot-aug2026-model-deprecations.md` (Claim 11) and
  `docs-github-copilot-selected-models-deprecated-sept2026.md` — no prior
  source note documents a standalone "Claude Opus 5 is now available in GitHub
  Copilot" changelog. This note therefore fills part of that gap by
  documenting the point-release successor's arrival, though the base Opus 5
  Copilot-availability announcement itself remains unmined.

### Claim 2: In GitHub's early testing, Opus 5.5 resolved tasks comparably to Claude Opus 5 while using significantly fewer steps and tokens

- **Evidence**: Official changelog performance framing, stated as GitHub's own
  "early testing" conclusion with no benchmark name, task set, or numeric
  score disclosed.
- **Confidence**: anecdotal (vendor-reported internal testing result; no
  disclosed methodology, consistent with the evidentiary weight the guide
  already assigns to this class of claim)
- **Quote**: "In early testing, Opus 5.5 resolved tasks comparably to Claude
  Opus 5 while using significantly fewer steps and tokens."
- **Our assessment**: This is an efficiency claim rather than a raw capability
  claim — it does not assert Opus 5.5 is more capable than Opus 5, only that it
  reaches comparable outcomes more cheaply (fewer steps, fewer tokens). That
  framing is distinct from the leaderboard-position and anecdote-driven
  capability claims Willison relayed for the Opus 5 launch itself
  (`blog-simonwillison-introducing-opus-5.md` Claims 2, 4-5), and closer in
  spirit to the cost/quality efficiency framing GitHub used for its own
  HydraFusion routing feature benchmarked against an Opus 5 baseline
  (`docs-github-copilot-weekly-releases-sept7-2026.md` Claim 4: "matched or
  exceeded Claude Opus 5's verified task quality at substantially lower
  estimated cost"). Neither source discloses whether "fewer steps and tokens"
  for Opus 5.5 was measured on the same benchmark suite GitHub used for that
  HydraFusion comparison. For Ch04 (Model Selection and Cost Management): if
  the guide cites this claim, it should flag it as vendor-asserted with no
  disclosed methodology, and should not conflate the "fewer steps/tokens"
  efficiency framing with an independently verified cost reduction figure.

### Claim 3: Opus 5.5 quickly recovered from errors in multistep tasks

- **Evidence**: Official changelog, same paragraph as Claim 2.
- **Confidence**: anecdotal (vendor-reported, no example or reproducible
  artifact given)
- **Quote**: "It also quickly recovered from errors in multistep tasks."
- **Our assessment**: This is a bare assertion with no anecdote or artifact
  attached — contrast with the FreeCAD/computer-vision anecdote Anthropic
  supplied for the base Opus 5 launch, which Willison at least quoted in
  detail (`blog-simonwillison-introducing-opus-5.md` Claims 4-5). This
  changelog gives no comparable illustrative example for error recovery,
  making it the weakest-evidenced claim in this source. Not recommended for
  citation beyond noting that GitHub's own framing emphasizes error recovery
  as a stated improvement axis for Opus 5.5.

### Claim 4: Claude Opus 5.5 watermarks its text outputs, and the watermark does not change the meaning, quality, or readability of outputs, nor does it add any tokens or cost

- **Evidence**: Official changelog, dedicated paragraph linking to Anthropic's
  "How Claude's text watermark works" documentation.
- **Confidence**: settled (a specific, checkable operating characteristic
  stated directly in the changelog)
- **Quote**: "Claude Opus 5.5 watermarks its text outputs. The watermark
  doesn't change the meaning, quality, or readability of outputs, nor does it
  add any tokens or cost."
- **Our assessment**: This is the first mention of output watermarking for any
  Claude model in this corpus's GitHub Copilot changelog family (the
  Opus 4.8 fast mode preview, Sonnet 5 GA, and prior Opus/Sonnet deprecation
  notes do not mention watermarking). The explicit "no added tokens or cost"
  qualifier addresses the most likely practitioner objection (that a
  watermarking mechanism might carry a hidden cost or context-window
  overhead) directly in the announcement. For Ch05 (Team Adoption /
  Enterprise Governance): this is a citable, vendor-stated data point for
  compliance-conscious teams asking whether AI-generated code or text
  produced via Opus 5.5 in Copilot carries a detectable provenance signal —
  though the guide should note that the mechanism's technical details live in
  Anthropic's linked documentation, not in this changelog, and were not
  extracted here since this source only points to it.

### Claim 5: Claude Opus 5.5 is billed at provider list pricing under usage-based billing, with no specific rate disclosed in the changelog

- **Evidence**: Official changelog, standalone sentence linking to GitHub's
  models-and-pricing documentation.
- **Confidence**: settled (billing treatment stated directly; no rate
  disclosed)
- **Quote**: "This model is billed at provider list pricing under
  usage-based billing. See Models and pricing for GitHub Copilot for details."
- **Our assessment**: Identical billing framing to Claude Sonnet 5's GA
  announcement (`docs-github-copilot-sonnet5-ga.md` Claim 4: "billed at
  provider list pricing under Usage Based Billing," also with no rate
  disclosed) and consistent with the "provider list pricing" phrasing used for
  the Opus 4.8 fast mode preview (`docs-github-copilot-opus48-fast-mode-preview.md`
  Claim 6, which at least gestured at relative pricing tiers). This changelog
  gives even less pricing detail than the fast mode preview did — practitioners
  must consult GitHub's separate pricing documentation for the actual
  usage-based-billing multiplier. No discount or promotional period is implied.

### Claim 6: Claude Opus 5.5 is available only to Copilot Pro+, Max, Business, and Enterprise users — not Pro, Free, or Student plans

- **Evidence**: Official changelog, "Availability in GitHub Copilot" section.
- **Confidence**: settled (plan eligibility stated directly in changelog)
- **Quote**: "Claude Opus 5.5 is available to Copilot Pro+, Max, Business, and
  Enterprise users."
- **Our assessment**: This matches the exact plan-tier gate documented for the
  Opus 4.8 fast mode preview (`docs-github-copilot-opus48-fast-mode-preview.md`
  Claim 5: Pro+/Max/Business/Enterprise, standard Pro excluded) and stands in
  contrast to Claude Sonnet 5's broader GA rollout, which explicitly included
  the standard Pro tier (`docs-github-copilot-sonnet5-ga.md` Claim 5: "Pro,
  Pro+, Max, Business, and Enterprise"). This reconfirms the pattern already
  observed across two prior sources: Opus-class Claude models in Copilot are
  gated above standard Pro, while Sonnet-class models reach the full paid
  tier ladder. For Ch04: practitioners on the $10/month Copilot Pro plan
  cannot access Opus 5.5 regardless of this changelog's "now available"
  framing — they would need Pro+ or higher, exactly as for Opus 4.8 fast mode.

### Claim 7: Opus 5.5 rolls out across ten platforms, listed by the changelog as Visual Studio Code, Visual Studio, Copilot CLI, GitHub Copilot coding agent, GitHub Copilot app, github.com, GitHub Mobile on iOS and Android, JetBrains IDEs, Xcode, and Eclipse

- **Evidence**: Official changelog, "Availability in GitHub Copilot" section,
  bulleted platform list.
- **Confidence**: settled (platform list stated directly), with an **emerging**
  terminology note (see assessment)
- **Quote**: "You can select the model in the model picker in: Visual Studio
  Code, Visual Studio, Copilot CLI, GitHub Copilot coding agent, GitHub
  Copilot app, github.com, GitHub Mobile on iOS and Android, JetBrains IDEs,
  Xcode, Eclipse"
- **Our assessment**: This is the same ten-surface set used for the Opus 4.8
  fast mode preview and the Sonnet 5 GA announcement
  (`docs-github-copilot-opus48-fast-mode-preview.md` Claim 4;
  `docs-github-copilot-sonnet5-ga.md` Claim 6), reconfirming GitHub's
  standardized "full Copilot surface" rollout template for new Claude model
  introductions. One naming drift worth flagging: this changelog names the
  fifth surface "GitHub Copilot coding agent," whereas both of those prior
  changelogs (June 29 and June 30, 2026) named the equivalent surface "GitHub
  Copilot cloud agent." No other Copilot changelog note in this corpus records
  when or whether this rename happened; it may be a straightforward product
  rebrand between June and September 2026, or an inconsistency in GitHub's own
  changelog copy. For Ch02: treat "GitHub Copilot coding agent" and "GitHub
  Copilot cloud agent" as referring to the same surface (the asynchronous
  cloud-hosted Copilot agent, as opposed to the interactive IDE/CLI agent)
  until a dedicated source resolves the naming history.

### Claim 8: The rollout of Opus 5.5 in Copilot is gradual, and users who don't see it in the picker yet should check back soon

- **Evidence**: Official changelog, "Availability in GitHub Copilot" section.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "Rollout will be gradual. Check back soon if you don't see it
  yet."
- **Our assessment**: Identical rollout framing to every prior Claude model
  introduction changelog in this corpus (Opus 4.8 fast mode: "gradual," per
  `docs-github-copilot-opus48-fast-mode-preview.md` Claim 8; Sonnet 5 GA:
  "Rollout will be gradual," per `docs-github-copilot-sonnet5-ga.md` Claim 7,
  verbatim identical wording). This is now a four-for-four pattern across
  every Claude-model Copilot availability changelog mined in this corpus,
  reinforcing that gradual rollout is GitHub's standing practice, not a
  one-off caveat — absence from the picker immediately after September 22,
  2026 should be read as normal rollout lag.

### Claim 9: Copilot Enterprise and Business plan administrators manage access to Opus 5.5 through the model policy in Copilot settings, and under default model enablement, new models are automatically enabled unless an administrator has turned off the global default or explicitly disabled this specific model

- **Evidence**: Official changelog, "Enabling access" section.
- **Confidence**: settled (stated directly in official changelog; corroborated
  by a distinct, already-mined source describing the same mechanism — see
  assessment)
- **Quote**: "Copilot Enterprise and Copilot Business plan administrators can
  manage access to Claude Opus 5.5 through the model policy in Copilot
  settings. Under default model enablement, new models are automatically
  enabled unless an administrator has turned off the global default or
  explicitly disables this model."
- **Our assessment**: This is the first Opus-tier Copilot changelog in this
  corpus to state the default-on GA model enablement behavior explicitly, and
  it directly corroborates `docs-github-copilot-global-model-policy-ga.md`
  (Claim 2: "Models you haven't previously configured will change their state
  to 'Delegate to default policy'... If your policy is enabled — which is the
  default — those models will become available to your users," enforced
  enterprise-by-enterprise through September 1, 2026). Opus 5.5, launching
  three weeks after that enforcement window closed, is a live instance of a
  GA model inheriting the now-fully-enforced default-on policy: it becomes
  available to Business/Enterprise users automatically unless an admin has
  disabled either the global policy or Opus 5.5 specifically. This is a
  notable contrast with the *opt-in, off-by-default* admin policy GitHub
  used for the Opus 4.8 fast mode **preview**
  (`docs-github-copilot-opus48-fast-mode-preview.md` Claim 7: "administrators
  must enable the policy for fast mode... The policy is off by default").
  The difference is not a contradiction — fast mode was a preview feature
  gated by its own opt-in policy toggle, while Opus 5.5 is a GA model
  governed by the global default-enablement policy documented in the August
  26 note. For Ch05: the guide should distinguish these two governance
  tracks explicitly — preview features may still default to off pending their
  own policy, while GA model releases from September 2026 onward default to
  on for Business/Enterprise unless an admin has opted out globally or
  per-model.

## Concrete Artifacts

### Changelog full text (verbatim, raw HTML, September 22, 2026)

```
Title: Claude Opus 5.5 is now available in GitHub Copilot
Published: September 22, 2026 (Release, 1 minute read)
Source: https://github.blog/changelog/2026-09-22-claude-opus-5-5-is-now-available-in-github-copilot

Claude Opus 5.5, Anthropic's newest Opus model, is now available in GitHub
Copilot. You can use it for agentic coding, long-running agentic tasks, and
knowledge work. In early testing, Opus 5.5 resolved tasks comparably to
Claude Opus 5 while using significantly fewer steps and tokens. It also
quickly recovered from errors in multistep tasks.

Claude Opus 5.5 watermarks its text outputs. The watermark doesn't change the
meaning, quality, or readability of outputs, nor does it add any tokens or
cost. To learn more visit Anthropic's How Claude's text watermark works.

This model is billed at provider list pricing under usage-based billing. See
Models and pricing for GitHub Copilot for details.

[Availability in GitHub Copilot]
Claude Opus 5.5 is available to Copilot Pro+, Max, Business, and Enterprise
users. You can select the model in the model picker in:
- Visual Studio Code
- Visual Studio
- Copilot CLI
- GitHub Copilot coding agent
- GitHub Copilot app
- github.com
- GitHub Mobile on iOS and Android
- JetBrains IDEs
- Xcode
- Eclipse

Rollout will be gradual. Check back soon if you don't see it yet.

[Enabling access]
Copilot Enterprise and Copilot Business plan administrators can manage
access to Claude Opus 5.5 through the model policy in Copilot settings.
Under default model enablement, new models are automatically enabled unless
an administrator has turned off the global default or explicitly disables
this model.

[Learn more]
To explore all models available in GitHub Copilot, see our documentation on
models and get started with Copilot.

[Share your feedback]
Join the GitHub Community to share your feedback.
```

### Feature Availability Summary (September 22, 2026)

```
Claude Opus 5.5 — GitHub Copilot Availability

PLANS:
  Pro:           Not listed / not eligible
  Pro+:          Eligible
  Max:           Eligible
  Business:      Eligible (default-on per global model policy; admin can disable)
  Enterprise:    Eligible (default-on per global model policy; admin can disable)
  Free:          Not listed / not eligible
  Student:       Not listed / not eligible

PLATFORMS (10):
  Visual Studio Code
  Visual Studio
  Copilot CLI
  GitHub Copilot coding agent   <- named "cloud agent" in June 2026 changelogs
  GitHub Copilot app
  github.com
  GitHub Mobile (iOS and Android)
  JetBrains IDEs
  Xcode
  Eclipse

BILLING:       Provider list pricing under usage-based billing (rate not disclosed)
WATERMARKING:  Text outputs watermarked; no meaning/quality/readability/token/cost impact
ROLLOUT:       Gradual
```

*Source: GitHub Copilot official changelog, September 22, 2026.*

## Cross-References

- **Corroborates** `docs-github-copilot-global-model-policy-ga.md` (Claim 2):
  that August 26, 2026 source documented the enforcement rollout (through
  September 1) of a default-on GA model enablement policy for
  Business/Enterprise plans. This changelog's Claim 9 language ("new models
  are automatically enabled unless an administrator has turned off the
  global default or explicitly disables this model") is a direct, live
  instance of that policy applying to a specific newly-GA model three weeks
  after the enforcement window closed — the first Opus-tier changelog in the
  corpus to describe this mechanism in these terms.

- **Corroborates** `docs-github-copilot-opus48-fast-mode-preview.md` (Claims
  4, 5, 8) and `docs-github-copilot-sonnet5-ga.md` (Claims 6, 7): identical
  or near-identical ten-surface platform list and "gradual" rollout language,
  continuing the standardized full-Copilot-surface rollout template for
  Claude model introductions (three-for-three plus this note, four-for-four
  on rollout language).

- **Extends** `docs-github-copilot-opus48-fast-mode-preview.md` (Claim 5):
  Opus 5.5 repeats the same Pro+/Max/Business/Enterprise plan gate documented
  for Opus 4.8 fast mode (standard Pro excluded), confirming this is a
  standing pattern for Opus-class models rather than a one-off restriction —
  in contrast to Sonnet 5's broader Pro-and-above availability
  (`docs-github-copilot-sonnet5-ga.md` Claim 5).

- **Extends** `blog-simonwillison-introducing-opus-5.md` (Claims 2, 4-5): that
  July 24, 2026 source documented base Opus 5's launch via a leaderboard
  ranking and a vendor-supplied autonomous-workaround anecdote (the FreeCAD/
  computer-vision task). This changelog's efficiency claim (Claim 2 of this
  note: comparable task resolution to Opus 5 using fewer steps and tokens) is
  a different kind of claim — relative efficiency versus the immediate
  predecessor, not absolute capability or leaderboard position — and comes
  with no comparable illustrative anecdote or reproducible artifact.

- **Extends** `docs-github-copilot-aug2026-model-deprecations.md` (Claim 11)
  and `docs-github-copilot-selected-models-deprecated-sept2026.md`: both
  sources list base Claude Opus 5 as a suggested successor for deprecated
  Opus 4.5/4.6 models but do not document a dedicated Copilot-availability
  changelog for Opus 5 itself. This note documents the next point release
  (5.5) arriving with its own dedicated changelog, but leaves the base Opus 5
  Copilot-availability announcement itself unmined — a gap for a future
  source-note pass if that changelog is ever submitted.

- **Contradicts**: None identified. The default-on admin-enablement framing
  in Claim 9 might look, at first glance, like it conflicts with the
  off-by-default policy documented for Opus 4.8 fast mode
  (`docs-github-copilot-opus48-fast-mode-preview.md` Claim 7), but the two
  describe different governance tracks (preview-feature opt-in policy vs.
  GA-model global default-enablement policy) that were already documented as
  distinct as of the August 26, 2026 global model policy changelog. No
  contradiction issue filed per MINER.md §4a.

- **Novel**:
  - First dedicated GitHub Copilot availability changelog for an Opus
    5-generation point release (5.5) in this corpus.
  - First Opus-tier Copilot changelog to explicitly invoke the default-on GA
    model enablement policy language established in
    `docs-github-copilot-global-model-policy-ga.md`.
  - First mention of Claude output watermarking in this corpus's GitHub
    Copilot changelog family.
  - First observed instance of "GitHub Copilot coding agent" as a surface
    name, where prior corpus sources (June 2026) used "GitHub Copilot cloud
    agent" for the apparently equivalent surface.

## Guide Impact

- **Chapter 04 (Model Selection and Cost Management)**: Add Claude Opus 5.5
  to the GitHub Copilot model roster as of September 22, 2026, gated to
  Pro+/Max/Business/Enterprise (same tier boundary as Opus 4.8 fast mode; wider
  than Sonnet 5's Pro-and-above availability). Cite the "fewer steps and
  tokens" efficiency claim only as vendor-asserted, undisclosed-methodology
  evidence — do not present it as a quantified cost-reduction figure. Do not
  treat this changelog as evidence that Opus 5.5 outperforms Opus 5 in raw
  capability; it claims comparable task resolution at lower operating cost,
  which is a narrower claim.

- **Chapter 05 (Team Adoption & Tooling)**: Note that as of this changelog,
  new GA Claude models in Copilot (including Opus 5.5) inherit the
  default-on global model enablement policy documented in
  `docs-github-copilot-global-model-policy-ga.md` — Business/Enterprise admins
  who have not reviewed their global model policy setting should expect
  Opus 5.5 to become available to their users automatically as the gradual
  rollout reaches them, absent an explicit opt-out. Recommend pairing this
  guidance with the existing recommendation (from that note's Guide Impact)
  that governance-conscious teams review each new model via the changelog
  rather than relying on the passive default.

## Extraction Notes

1. **Source is a short changelog (~130 words of primary text, "1 minute
   read")**: this is consistent with the Prospector's second triage comment
   flagging this as a "thin changelog entry" and with the pre-screen
   rejection comment on the issue ("no engineering substance"). In practice
   the source does contain several extractable, specific claims (an
   efficiency framing versus the immediate predecessor, a watermarking
   disclosure, an explicit statement of the default-on GA enablement
   mechanism, and a surface-naming drift) — thin in word count, but not
   contentless. All substantive claims are captured in the 9 claims above;
   this is not a case of under-reading a longer source.
2. **Raw HTML fetched directly via `curl`**: quotes in this note are
   character-verified against the raw page HTML (tags stripped, entities
   decoded), not solely against WebFetch's AI-summarized paraphrase. Both
   methods returned consistent substance.
3. **Two contradictory Prospector triage comments on this issue**: the first
   comment rated novelty "high" and pointed to Ch02/Ch05; the second rated
   novelty "low," questioned whether this warrants separate coverage beyond
   existing Opus 5 documentation, and pointed to Ch04. This note treats both
   as valid signal: it extracts the source at moderate depth (9 claims, not
   the 12-13 seen in some longer changelog notes in this family) and
   addresses Ch04 and Ch05 in Guide Impact, consistent with the union of both
   triage comments' chapter recommendations.
4. **No contradictions filed**: see Cross-References → Contradicts. The
   apparent tension between this note's default-on admin enablement and the
   Opus 4.8 fast mode preview's default-off policy is resolved by the two
   sources describing different governance tracks (GA global policy vs.
   preview-specific opt-in), not a disagreement about the same mechanism.
5. **Anthropic's own watermarking documentation and Copilot's
   models-and-pricing page were not followed as sub-pages**: per MINER.md
   §1, up to 5 substantive linked pages may be followed. The two links in
   this changelog (Anthropic's "How Claude's text watermark works" and
   GitHub's "Models and pricing for GitHub Copilot") are general reference
   documentation not specific to this announcement, consistent with how
   prior notes in this family (e.g.
   `docs-github-copilot-sonnet5-ga.md` Extraction Notes #2) treated similar
   "Additional Resources"-style links as navigational rather than
   substantive. They are candidates for separate future source-note issues
   if submitted independently.
