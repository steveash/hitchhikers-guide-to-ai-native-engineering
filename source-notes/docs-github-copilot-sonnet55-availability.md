---
source_url: https://github.blog/changelog/2026-09-28-claude-sonnet-5-5-in-github-copilot
source_type: docs
title: "Claude Sonnet 5.5 in GitHub Copilot"
author: GitHub (official changelog, byline "Allison")
date_published: 2026-09-28
date_extracted: 2026-09-29
last_checked: 2026-09-29
status: current
confidence_overall: settled
issue: "#3781"
---

# Claude Sonnet 5.5 in GitHub Copilot

> GitHub's September 28, 2026 changelog announcing GA of Claude Sonnet 5.5 across ten Copilot surfaces on Pro, Pro+, Max, Business and Enterprise, with a qualitative efficiency claim (parity with Sonnet 5 on coding using fewer steps, tokens and tool calls) and the same admin default-enablement pattern as prior Claude releases.

## Source Context

- **Type**: docs (GitHub official product changelog; short announcement, roughly 200 words)
- **Author credibility**: GitHub's Copilot team announcing a shipped feature. Authoritative for availability, plan eligibility, surfaces, billing model and admin behavior. Not a credible source for quantitative performance: "early testing" is qualitative, with no benchmarks, numbers or methodology.
- **Scope**: Availability of Sonnet 5.5 in Copilot: efficiency claim, billing, plans, surfaces, rollout, admin enablement. Does NOT cover: pricing figures, benchmark scores, Auto model selection pool membership, context window, ZDR status, or deprecation of Sonnet 5.

## Extracted Claims

### Claim 1: Claude Sonnet 5.5 is generally available in GitHub Copilot, positioned for well-scoped everyday work
- **Evidence**: Official changelog opening paragraph (published 2026-09-28).
- **Confidence**: settled
- **Quote**: "Claude Sonnet 5.5, Anthropic’s newest Sonnet model, is now generally available in GitHub Copilot."
- **Our assessment**: Product fact. Unlike the Opus 5.5 announcement (which says "now available"), this says "generally available". The positioning ("well-scoped everyday work like building features and fixing bugs") frames Sonnet as the routine-work tier rather than the long-running-agent tier.

### Claim 2: In GitHub's early testing, Sonnet 5.5 matched Sonnet 5 on coding tasks with significantly fewer steps, tokens and tool calls
- **Evidence**: GitHub's own early testing; no numbers, benchmarks or methodology.
- **Confidence**: emerging (vendor-reported, qualitative, unquantified)
- **Quote**: "In our early testing, Sonnet 5.5 stood out for its efficiency, matching Claude Sonnet 5 on coding tasks while using significantly fewer steps, tokens, and tool calls."
- **Our assessment**: Plausible, and consistent with the identical efficiency framing GitHub used for Opus 5.5 vs Opus 5. The point-release pattern seems to be "same quality, lower cost per task" rather than higher capability. Practitioners should validate on their own workloads before assuming per-task savings, since the changelog gives no magnitude.

### Claim 3: Sonnet 5.5 also finishes tasks noticeably faster
- **Evidence**: Same early testing; no latency figures.
- **Confidence**: anecdotal
- **Quote**: "It also finished tasks noticeably faster."
- **Our assessment**: Fewer steps and tool calls would plausibly cut wall-clock time, so this is coherent with Claim 2. It is unquantified, and the source doesn't say whether the speedup is per-token or per-task.

### Claim 4: Sonnet 5.5 is billed at provider list pricing under usage-based billing
- **Evidence**: Changelog statement; points to "Models and pricing for GitHub Copilot" without quoting a rate.
- **Confidence**: settled
- **Quote**: "This model is billed at provider list pricing under usage-based billing."
- **Our assessment**: Combined with Claim 2, the cost effect of fewer tokens flows directly to the user under list-price billing. No discount or promotional rate is mentioned.

### Claim 5: Sonnet 5.5 is available on Copilot Pro, Pro+, Max, Business and Enterprise, so the Pro tier is included
- **Evidence**: Plan list in changelog "Availability in GitHub Copilot" section.
- **Confidence**: settled
- **Quote**: "Claude Sonnet 5.5 is available to Copilot Pro, Pro+, Max, Business, and Enterprise users."
- **Our assessment**: The plan list matches Sonnet 5 GA and, unlike Opus 5.5 (Pro+, Max, Business, Enterprise), includes Pro. This supports a pattern: Sonnet-class models reach Pro, Opus-class models are gated to higher tiers. Free and Student are not listed, so they are presumably excluded.

### Claim 6: Sonnet 5.5 is selectable in the model picker on ten surfaces
- **Evidence**: Bulleted surface list in the changelog.
- **Confidence**: settled
- **Quote**: "You can select the model in the model picker in:"
- **Our assessment**: The list is: Visual Studio Code, Visual Studio, Copilot CLI, GitHub Copilot coding agent, GitHub Copilot app, github.com, GitHub Mobile on iOS and Android, JetBrains IDEs, Xcode, Eclipse. This is the same ten-surface set as Sonnet 5 GA and Opus 5.5. Listing Copilot CLI and coding agent means Sonnet 5.5 is manually selectable there. The changelog says nothing about whether it joins Auto selection.

### Claim 7: Rollout is gradual
- **Evidence**: Changelog statement.
- **Confidence**: settled
- **Quote**: "Rollout will be gradual. Check back soon if you don’t see it yet."
- **Our assessment**: Standard staged rollout. Teams should not treat a missing picker entry on day one as a policy problem.

### Claim 8: Business and Enterprise admins manage Sonnet 5.5 through model policy, and new models are enabled by default unless the global default is off or the model is explicitly disabled
- **Evidence**: Changelog "Enabling access" section.
- **Confidence**: settled
- **Quote**: "Under default model enablement, new models are automatically enabled unless an administrator has turned off the global default or explicitly disables this model."
- **Our assessment**: This is the governance-relevant claim. Organizations that want to vet new models must either turn off the global default or disable each model proactively. The source lists an "explicitly disables this model" path and a global-default toggle, so blanket opt-in requires acting before release, not after.

## Concrete Artifacts

```
Availability (verbatim from source): "Claude Sonnet 5.5 is available to Copilot Pro, Pro+, Max, Business, and Enterprise users."
Surfaces (verbatim list from source): Visual Studio Code; Visual Studio; Copilot CLI; GitHub Copilot coding agent; GitHub Copilot app; github.com; GitHub Mobile on iOS and Android; JetBrains IDEs; Xcode; Eclipse
Admin control (source): model policy in Copilot settings; "default model enablement" with a global default toggle.
Source: https://github.blog/changelog/2026-09-28-claude-sonnet-5-5-in-github-copilot
```

## Cross-References

- **Corroborates**: `docs-github-copilot-sonnet5-ga.md` Claim 5 (same plan list, including Pro), Claim 6 (same ten surfaces), Claim 7 (gradual rollout), Claim 4 (provider list pricing); `docs-github-copilot-opus55-availability.md` Claim 2 (same "matches predecessor with fewer steps and tokens" framing), Claim 5 (provider list pricing), Claim 7 (ten surfaces), Claim 8 (gradual rollout).
- **Contradicts**: None found. Sonnet 5.5's plan list differs from `docs-github-copilot-opus55-availability.md` Claim 6 (Opus excludes Pro), but that is a tier difference between models, not a conflict.
- **Extends**: `docs-github-copilot-sonnet5-ga.md` by documenting its point-release successor about three months later (Sonnet 5 GA 2026-06-30). Also extends `docs-github-copilot-opus55-availability.md`, showing the same 5.5 release template applied to Sonnet six days later.
- **Novel**: (a) The Sonnet 5.5 release itself in Copilot; (b) explicit wording of the two-level admin default-enablement mechanism ("global default" vs. per-model disable), which is worth comparing to `docs-github-copilot-global-model-policy-ga.md`; (c) unlike Sonnet 5, no ZDR claim appears, and unlike Opus 5.5, no watermarking claim appears. The absence is not evidence about either property.

## Guide Impact

- **Chapter 02 / Chapter 04**: Add Sonnet 5.5 to the Copilot model-availability roster. The recurring pattern across Sonnet 5 → 5.5 and Opus 5 → 5.5 is "point release matches predecessor quality with fewer steps/tokens", cited to this note Claim 2 and `docs-github-copilot-opus55-availability.md` Claim 2. Under provider-list billing (Claim 4) that becomes a cost lever, but it is vendor-reported and unquantified, so present it as a hypothesis to verify.
- **Chapter 04**: The Sonnet-includes-Pro versus Opus-excludes-Pro tier split (Claim 5) is a practical selection factor for mixed-plan teams.
- **Chapter 05**: The default-enablement wording (Claim 8) supports advice that enterprises decide up front whether new models auto-enable, since each release would otherwise reach all users by default.

## Extraction Notes

- Read the full changelog page (fetched directly, HTML stripped); it is a single short page with no sub-pages worth following beyond links to Copilot models/pricing docs, which were not fetched.
- Quotes were copied from the page text. The changelog is thin on evidence: no numbers, benchmarks or dates beyond publication.
- Triage questions not answered by the source: whether Sonnet 5.5 supersedes or coexists with Sonnet 5 (no deprecation stated) and whether it joins the CLI Auto pool (not stated).
- No contradiction issue filed.
