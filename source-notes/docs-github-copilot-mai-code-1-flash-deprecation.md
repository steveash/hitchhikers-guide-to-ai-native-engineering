---
source_url: https://github.blog/changelog/2026-08-11-upcoming-deprecation-of-mai-code-1-flash
source_type: docs
title: "Upcoming deprecation of MAI-Code-1-Flash"
author: GitHub (official changelog; byline "Allison")
date_published: 2026-08-11
date_extracted: 2026-08-12
last_checked: 2026-08-12
status: current
confidence_overall: settled
issue: "#2637"
---

# Upcoming Deprecation of MAI-Code-1-Flash

> GitHub's August 11, 2026 changelog deprecating MAI-Code-1-Flash itself —
> the model just designated on July 31 as Raptor Mini's Copilot replacement
> — in favor of MAI-Code-1.1-Flash, effective September 10, 2026 (a 30-day
> notice). Published the same day as a companion changelog entry announcing
> MAI-Code-1.1-Flash's GitHub Copilot availability (73% lower list price,
> native vision support) and the same day as Microsoft's own MAI-Code-1.1-Flash
> announcement (22% Terminal-Bench 2.1 improvement, 25% token efficiency
> gain, "a quarter of the cost" of the prior model).

## Source Context

- **Type**: docs (GitHub official product changelog, August 11, 2026;
  approximately 110 words of primary announcement text, "1 minute read,"
  category-tagged "Retired" — confirmed via direct raw-HTML `curl` fetch, not
  a WebFetch summary alone). Two directly linked companion sources were also
  fetched and read in full: GitHub's own same-day changelog entry "MAI-Code-1.1-Flash
  available in GitHub Copilot" and Microsoft's own same-day announcement
  "MAI-Code-1.1-Flash: Better, faster, at a quarter of the cost" on
  microsoft.ai (reached via the `aka.ms/mai-code-1.1-flash` link in GitHub's
  companion post).
- **Author credibility**: GitHub engineering team (changelog) and Microsoft
  AI team (microsoft.ai blog). Both are primary sources for their own product
  facts — deprecation date, successor designation, pricing, and rollout
  scope from GitHub; benchmark and efficiency claims from Microsoft. Neither
  source is independently verified: Microsoft's benchmark improvements
  (Terminal-Bench 2.1, .NET tasks, token efficiency) are self-reported with
  no disclosed comparison methodology beyond "hundreds of thousands of
  reinforcement-learning environments."
- **Scope**: Covers the deprecation date, successor model, and standard
  enable-then-verify admin procedure for MAI-Code-1-Flash specifically. Does
  NOT cover: why the model is being deprecated only ~40 days after being
  named Raptor Mini's replacement, in-flight session behavior at cutover, or
  independent verification of Microsoft's performance claims for the
  successor.

## Extracted Claims

### Claim 1: GitHub will deprecate MAI-Code-1-Flash across all Copilot experiences on September 10, 2026, with MAI-Code-1.1-Flash as the sole named successor

- **Evidence**: Official GitHub Copilot changelog table, published August 11, 2026, fetched directly from raw page HTML.
- **Confidence**: settled (authoritative product fact stated directly in a structured table)
- **Quote**: "With the launch of MAI-Code-1.1-Flash, we will deprecate MAI-Code-1-Flash across all GitHub Copilot experiences on September 10, 2026:" followed by the table row "MAI-Code-1-Flash | 9-10-2026 | MAI-Code-1.1-Flash"
- **Our assessment**: This directly resolves the Prospector's triage question for this issue — whether the notice is a distinct new deprecation event or a duplicate reference to the July 31, 2026 notice that designated MAI-Code-1-Flash as Raptor Mini's successor. It is a distinct event: the July 31 notice deprecated Raptor Mini and named MAI-Code-1-Flash as its replacement (`docs-github-copilot-aug2026-model-deprecations.md` Claim 1); this notice deprecates MAI-Code-1-Flash itself, eleven days later, naming MAI-Code-1.1-Flash as its replacement. No overlap in subject model between the two notices.

### Claim 2: MAI-Code-1-Flash's own deprecation was announced just 11 days after it was named Raptor Mini's official Copilot successor, and its September 10 cutoff falls only 9 days after the Raptor Mini migration deadline it was named to satisfy

- **Evidence**: Cross-referencing this source's publish date (August 11, 2026) and deprecation date (September 10, 2026) against `docs-github-copilot-aug2026-model-deprecations.md`, which documents MAI-Code-1-Flash being named Raptor Mini's successor on July 31, 2026, effective September 1, 2026.
- **Confidence**: emerging (each date is individually settled; the "rapid churn" characterization is our cross-source synthesis, not a claim either source makes)
- **Quote**: (no direct quote; timeline comparison across this source and `docs-github-copilot-aug2026-model-deprecations.md`)
- **Our assessment**: This is the fastest successor-to-deprecation turnaround documented in the corpus's Copilot deprecation-notice family. An organization that migrated from Raptor Mini to MAI-Code-1-Flash on the September 1 deadline would need to migrate again to MAI-Code-1.1-Flash just nine days later, on September 10. Practitioners who read the July 31 notice and enabled MAI-Code-1-Flash as instructed are now facing a second required migration within the same month, for the same functional role (the Copilot Business/Enterprise cost-efficient coding model slot). This is a materially different pattern from the "regular scheduled deprecation" cadence documented in earlier corpus notices — a named successor being retired before the predecessor's own migration deadline has even passed.

### Claim 3: The notice-to-cutoff window is 30 days (published August 11, 2026; effective September 10, 2026)

- **Evidence**: Changelog publish date/time (`datetime="2026-08-11"`, "August 11, 2026" per the page header) and the stated deprecation date ("9-10-2026") in the table.
- **Confidence**: settled (both dates stated directly in the official source; the day-count is a derived calculation)
- **Quote**: "August 11, 2026" (page publish date); "9-10-2026" (deprecation date, table)
- **Our assessment**: Sits within the range already documented across the corpus (31, 25, -1, 29, 32 days for the five prior notices in `docs-github-copilot-aug2026-model-deprecations.md`'s cross-notice timeline). This sixth data point (30 days) does not extend the range but reinforces that lead time clusters in the high-20s-to-low-30s range for genuinely "upcoming" (non-retroactive) notices, distinct from the one -1 day retroactive outlier.

### Claim 4: This notice omits the enumerated "affected surfaces" boilerplate present in every prior corpus deprecation notice, stating only "across all GitHub Copilot experiences" with no parenthetical surface list

- **Evidence**: Full-text comparison of this notice's deprecation sentence against the equivalent sentence in five prior corpus notices, verified via raw HTML fetch.
- **Confidence**: settled (the absence is directly observable in the raw HTML; verified against the page's meta-description abstract and body text, which match)
- **Quote**: "With the launch of MAI-Code-1.1-Flash, we will deprecate MAI-Code-1-Flash across all GitHub Copilot experiences on September 10, 2026:"
- **Our assessment**: `docs-github-copilot-aug2026-model-deprecations.md` Claim 2 asserted the phrase "all GitHub Copilot experiences (including Copilot Chat, inline edits, ask and agent modes, and code completions)" was "fixed boilerplate GitHub reuses regardless of provider or model count," based on five-for-five verbatim matches. This notice breaks that pattern — the parenthetical enumeration is absent entirely, leaving only the unqualified "across all GitHub Copilot experiences." This directly contradicts the "fixed regardless of ... model count" framing of the prior claim. **Contradiction filed: see issue #2650** and Cross-References below. We do not resolve which framing is correct here; a human resolver will assign the verdict.

### Claim 5: The enable-then-verify enterprise admin procedure and the "no action required to remove the older model" boilerplate both repeat near-verbatim from every prior corpus notice

- **Evidence**: Required-actions paragraph, changelog body.
- **Confidence**: settled (stated directly in official changelog; near-verbatim text match against five prior notices)
- **Quote**: "Please update your workflows and integrations to use the new model before September 10. Copilot Enterprise administrators may need to enable access to the alternative model through their model policies in Copilot settings. As an administrator, you can verify availability by checking your individual Copilot settings and confirming that the policy is enabled for the specific model. Once enabled, you'll see the model in the Copilot Chat model selector in VS Code and on github.com. No action is required to remove the older model once it has been deprecated."
- **Our assessment**: Near-identical to the corresponding paragraph in `docs-github-copilot-aug2026-model-deprecations.md` Claims 5-6 (only "these dates"/"the models" is singularized to "September 10"/"the older model," consistent with this notice covering one model rather than six). This is now a sixth consecutive notice confirming the enable-then-verify procedure and auto-removal-with-no-cleanup as GitHub's fixed enterprise governance mechanism — unlike the surface-enumeration sentence (Claim 4), this part of the boilerplate did survive intact into a single-model notice.

### Claim 6: GitHub Enterprise customers with questions are directed to their account manager — the same support channel named in every prior corpus notice

- **Evidence**: Closing sentence of the changelog body.
- **Confidence**: settled (stated directly in official changelog)
- **Quote**: "GitHub Enterprise customers with questions or concerns are encouraged to reach out to their account manager for further assistance."
- **Our assessment**: Word-for-word identical to the equivalent sentence in every prior corpus deprecation notice, including `docs-github-copilot-aug2026-model-deprecations.md` Claim 7. A sixth consecutive confirmation that this exact sentence, unlike the surface enumeration, is genuinely fixed.

### Claim 7: A same-day companion changelog entry announces MAI-Code-1.1-Flash's availability, claiming native vision support and improvements "across coding quality, instruction following, tool use, and performance" over MAI-Code-1-Flash

- **Evidence**: GitHub Copilot changelog, "MAI-Code-1.1-Flash available in GitHub Copilot," published August 11, 2026 (same day, linked directly from the deprecation notice's related-posts section).
- **Confidence**: settled (stated directly in GitHub's own companion changelog); the underlying quality claims themselves are anecdotal (no benchmark cited in this specific sentence)
- **Quote**: "MAI-Code-1.1-Flash, Microsoft's latest small-tier coding model, is now rolling out in GitHub Copilot. Building on MAI-Code-1-Flash, it adds native vision support for image understanding and delivers improvements across coding quality, instruction following, tool use, and performance."
- **Our assessment**: The vision-support claim is notable and specifically attributable to GitHub's own changelog wording — it does not appear anywhere in Microsoft's own microsoft.ai announcement for the same model (verified by full-text search of that page's raw HTML), which is worth flagging: the two companies' own-channel announcements for the identical model release do not describe identical feature sets in their own words, though they are not necessarily in conflict (Microsoft's post may simply have omitted the vision feature rather than denied it).

### Claim 8: MAI-Code-1.1-Flash carries a 73% lower list price than MAI-Code-1-Flash and is billed at a 0.25× premium request multiplier for annual GitHub Copilot subscribers

- **Evidence**: Same companion changelog, "MAI-Code-1.1-Flash available in GitHub Copilot," August 11, 2026.
- **Confidence**: settled (stated directly as a specific numeric figure in official changelog)
- **Quote**: "Alongside these model enhancements, continued advances in model and serving efficiency have enabled a 73% lower list price than MAI-Code-1-Flash, making it a cost-effective option for lightweight coding workflows that require a balance of capability and cost efficiency. For annual GitHub Copilot subscribers, the model is charged at a 0.25× premium request multiplier."
- **Our assessment**: This is a precise, falsifiable pricing claim (73% lower list price; 0.25× multiplier), a step up in specificity from the qualitative "improvements" language in Claim 7. Combined with Microsoft's own "a quarter of the cost" framing (Claim 11 below), the two companies' cost claims are directionally consistent (roughly 73-75% reduction), though GitHub's figure is Copilot-specific list pricing and Microsoft's is a general framing — the two are not necessarily measuring identical things, but they do not conflict.

### Claim 9: MAI-Code-1.1-Flash's plan-tier rollout is broader at launch than MAI-Code-1-Flash's was at its own June 2 launch — Free and Student get it via auto-selection only, while Pro, Pro+, Max, Business, and Enterprise can manually select it in addition to auto-selection, across ten named Copilot surfaces

- **Evidence**: Same companion changelog, "Availability in GitHub Copilot" section.
- **Confidence**: settled (explicit plan-tier and surface breakdown stated directly)
- **Quote**: "MAI-Code-1.1-Flash will be available to Copilot Free and Student users through auto model selection. Copilot Pro, Pro+, Max, Business, and Enterprise SKUs will be able to manually select this model in addition to having auto model select it."
- **Our assessment**: `docs-github-copilot-mai-code-1-flash-more-surfaces.md` Claim 2 and Claim 7 documented MAI-Code-1-Flash's June 18, 2026 expansion as excluding Business and Enterprise tiers entirely ("forthcoming," not yet available), creating a documented individual-before-enterprise rollout gap. MAI-Code-1.1-Flash's launch reverses that sequencing: Business and Enterprise are included from day one (manual selection, gated by an admin policy per Claim 10 below), while Free and Student are restricted to auto-selection only rather than manual choice. This is a different rollout shape than its predecessor's, not a strict superset.

### Claim 10: Copilot Enterprise and Business plan administrators must enable a MAI-Code-1.1-Flash policy that is off by default

- **Evidence**: Same companion changelog, "Enabling access" section.
- **Confidence**: settled (stated directly as an administrative requirement)
- **Quote**: "Copilot Enterprise and Copilot Business plan administrators must enable the MAI-Code-1.1-Flash policy in Copilot settings. The policy is off by default."
- **Our assessment**: Consistent with the standard enable-then-verify pattern documented across the corpus's deprecation-notice family (Claim 5 above), extended here to a new-model-availability announcement rather than a deprecation. Enterprise/Business admins who do nothing after this announcement will not have MAI-Code-1.1-Flash available to their users, mirroring the same "no automatic enablement" governance posture GitHub applies to deprecation successor models.

### Claim 11: Microsoft's own announcement claims a 22% improvement on Terminal-Bench 2.1 (measured in GitHub Copilot CLI), a 15% improvement on .NET tasks, 25% greater token efficiency, and "a quarter of the cost" relative to the prior model — plus production metrics of 4% higher code survival and 9% more return visits

- **Evidence**: Microsoft's own microsoft.ai announcement, "MAI-Code-1.1-Flash: Better, faster, at a quarter of the cost," published August 11, 2026, fetched directly from raw page HTML (reached via the `aka.ms/mai-code-1.1-flash` redirect linked from GitHub's companion changelog).
- **Confidence**: anecdotal (vendor self-reported figures; no third-party benchmark verification, no disclosed comparison baseline beyond "the model we launched in June at Microsoft Build," and "code survival"/"return visits" are undefined internal metrics)
- **Quote**: "We learned from developer feedback that CLI tasks and .NET performance mattered, so that's where we focused. The result: a 22% improvement on Terminal-Bench 2.1 in GitHub Copilot CLI and a 15% improvement on .NET tasks." / "Benchmarks are useful guides but production is where the rubber meets the road. Most importantly, code survival rose 4% and return visits increased 9%." / "1.1 is also dramatically more efficient. In GitHub Copilot tokens stream 25% faster and the model uses 25% fewer tokens to complete a task." / "Better training and serving efficiency let us offer a stronger, faster model at one quarter of the price of 1.0—and pass those savings reliably to customers. We achieved this by optimizing for real-world use across more than hundreds of thousands of reinforcement-learning environments in GitHub Copilot."
- **Our assessment**: This continues the pattern documented in `blog-simonwillison-microsoft-mai-models.md` Claims 3-6 and `docs-github-copilot-mai-code-1-flash-more-surfaces.md` Claim 4 of Microsoft self-reporting favorable performance figures for MAI-family models without disclosing comparison methodology, evaluator identity, or raw benchmark scores — only percentage deltas. "Code survival" and "return visits" in particular are undefined proprietary metrics with no stated definition, making them impossible for practitioners to independently verify or contextualize. The specificity is higher here than prior MAI announcements (named benchmark: Terminal-Bench 2.1; named domain: .NET tasks) but still falls short of disclosed methodology.

### Claim 12: Microsoft's own blog refers to the predecessor model as "1.0" and "the model we launched in June at Microsoft Build," while GitHub's official deprecation table names it "MAI-Code-1-Flash" (no ".0" suffix)

- **Evidence**: Direct comparison of naming in this source's deprecation table ("MAI-Code-1-Flash") against Microsoft's own announcement text ("compared to the model we launched in June at Microsoft Build" and "at one quarter of the price of 1.0").
- **Confidence**: emerging (both namings are directly quoted; the significance we assign — that this is an informal/formal naming mismatch rather than a different model — is our interpretation)
- **Quote**: "MAI-Code-1.1-Flash produces higher quality code, at 25% greater token efficiency, and at a quarter of the cost compared to the model we launched in June at Microsoft Build." / "Better training and serving efficiency let us offer a stronger, faster model at one quarter of the price of 1.0" (both Microsoft's own announcement); "MAI-Code-1-Flash" (GitHub's deprecation table, this source)
- **Our assessment**: This is a minor but real naming inconsistency across the two companies' own official channels for the same model transition — GitHub's product surfaces and changelog consistently use "MAI-Code-1-Flash" (no version-point suffix) while Microsoft's own blog treats "1.0" as the implicit version number the "1.1" in the successor's name refers back to. Practitioners searching for "MAI-Code-1.0-Flash" in GitHub's own documentation or model picker will not find that exact string; "MAI-Code-1-Flash" is the only form that appears in GitHub's product surfaces per this and prior corpus notices.

## Concrete Artifacts

### Deprecation Notice (verbatim, from raw HTML — github.blog, August 11, 2026)

```
Upcoming deprecation of MAI-Code-1-Flash
Tag: Retired
Published: August 11, 2026 · 1 minute read

With the launch of MAI-Code-1.1-Flash, we will deprecate MAI-Code-1-Flash
across all GitHub Copilot experiences on September 10, 2026:

Model               Deprecation date    Suggested alternative
MAI-Code-1-Flash     9-10-2026           MAI-Code-1.1-Flash

Please update your workflows and integrations to use the new model before
September 10. Copilot Enterprise administrators may need to enable access
to the alternative model through their model policies in Copilot settings.
As an administrator, you can verify availability by checking your
individual Copilot settings and confirming that the policy is enabled for
the specific model. Once enabled, you'll see the model in the Copilot Chat
model selector in VS Code and on github.com. No action is required to
remove the older model once it has been deprecated.

GitHub Enterprise customers with questions or concerns are encouraged to
reach out to their account manager for further assistance.

To learn more about the models available in Copilot, see our documentation
on models and get started with Copilot today.
```

*Source: raw HTML of
https://github.blog/changelog/2026-08-11-upcoming-deprecation-of-mai-code-1-flash/,
fetched via `curl --compressed` on 2026-08-12. JSON-LD metadata: author
"Allison"; `datePublished` 2026-08-11T18:50:42+00:00; `dateModified`
2026-08-11T19:02:14+00:00; category "copilot."*

### Companion Availability Announcement (verbatim excerpt — github.blog, same day)

```
MAI-Code-1.1-Flash available in GitHub Copilot
Published: August 11, 2026 · 1 minute read

MAI-Code-1.1-Flash, Microsoft's latest small-tier coding model, is now
rolling out in GitHub Copilot. Building on MAI-Code-1-Flash, it adds native
vision support for image understanding and delivers improvements across
coding quality, instruction following, tool use, and performance.

Alongside these model enhancements, continued advances in model and serving
efficiency have enabled a 73% lower list price than MAI-Code-1-Flash, making
it a cost-effective option for lightweight coding workflows that require a
balance of capability and cost efficiency. For annual GitHub Copilot
subscribers, the model is charged at a 0.25x premium request multiplier.

This model is billed at provider list pricing under usage-based billing.

Availability in GitHub Copilot
MAI-Code-1.1-Flash will be available to Copilot Free and Student users
through auto model selection. Copilot Pro, Pro+, Max, Business, and
Enterprise SKUs will be able to manually select this model in addition to
having auto model select it.

Selectable in: Copilot CLI, Copilot cloud agent, GitHub Copilot app,
Copilot Chat on GitHub, Visual Studio Code, Visual Studio, GitHub Mobile,
JetBrains IDEs, Eclipse, Xcode.

Enabling access
Copilot Enterprise and Copilot Business plan administrators must enable the
MAI-Code-1.1-Flash policy in Copilot settings. The policy is off by default.
```

*Source: raw HTML of
https://github.blog/changelog/2026-08-11-mai-code-1-1-flash-available-in-github-copilot/,
fetched via `curl --compressed` on 2026-08-12.*

### Microsoft's Own Announcement (verbatim excerpt — microsoft.ai, same day)

```
MAI-Code-1.1-Flash: Better, faster, at a quarter of the cost
Published: August 11, 2026

MAI-Code-1.1-Flash produces higher quality code, at 25% greater token
efficiency, and at a quarter of the cost compared to the model we launched
in June at Microsoft Build. This small, efficient, coding workhorse is now
in production in GitHub Copilot.

We learned from developer feedback that CLI tasks and .NET performance
mattered, so that's where we focused. The result: a 22% improvement on
Terminal-Bench 2.1 in GitHub Copilot CLI and a 15% improvement on .NET
tasks.

Benchmarks are useful guides but production is where the rubber meets the
road. Most importantly, code survival rose 4% and return visits increased
9%.

1.1 is also dramatically more efficient. In GitHub Copilot tokens stream
25% faster and the model uses 25% fewer tokens to complete a task. That
means faster answers, less waiting, and more useful work from every
token-not simply a bigger model with a bigger bill.

Better training and serving efficiency let us offer a stronger, faster
model at one quarter of the price of 1.0-and pass those savings reliably to
customers. We achieved this by optimizing for real-world use across more
than hundreds of thousands of reinforcement-learning environments in
GitHub Copilot.

The loop is simple: ship, learn, improve, repeat. That's the MAI hill
climbing machine.
```

*Source: raw HTML of
https://microsoft.ai/news/mai-code-1-1-flash-br-better-faster-at-a-quarter-of-the-cost/,
fetched via `curl --compressed` with a browser user-agent on 2026-08-12
(the default curl UA was blocked with HTTP 403). Note: "vision support" is
NOT mentioned anywhere in this Microsoft page — that claim comes only from
GitHub's companion changelog (see Claim 7).*

### Updated Cross-Notice Deprecation Timeline (sixth corpus data point)

```
GitHub Copilot Model Deprecations — Corpus Timeline (as of August 11, 2026)

Notice   | Model(s)                        | Notice Date | Effective Date | Lead Time | Providers
---------|-----------------------------------|-------------|-----------------|-----------|---------------------
May 1    | GPT-5.2 / GPT-5.2-Codex*         | 2026-05-01  | 2026-06-01      | 31 days   | OpenAI
May 7    | GPT-4.1                          | 2026-05-07  | 2026-06-01      | 25 days   | OpenAI
May 7    | Claude Sonnet 4                  | 2026-05-07  | 2026-05-06      | -1 day    | Anthropic
Jul 2    | Gemini 2.5 Pro / Gemini 3 Flash  | 2026-07-02  | 2026-07-31      | 29 days   | Google
Jul 31   | Gemini 3.1 Pro / Opus 4.5-4.6 /  | 2026-07-31  | 2026-09-01      | 32 days   | Google, Anthropic,
         | Sonnet 4.5-4.6 / Raptor Mini     |             |                 |           | Microsoft
Aug 11   | MAI-Code-1-Flash                 | 2026-08-11  | 2026-09-10      | 30 days   | Microsoft

* GPT-5.2-Codex in Copilot Code Review carved out (see docs-github-copilot-gpt52-deprecation.md)

Successor chain for the Copilot cost-efficient coding-model slot:
  Raptor Mini        → MAI-Code-1-Flash    (named 2026-07-31, effective 2026-09-01)
  MAI-Code-1-Flash    → MAI-Code-1.1-Flash  (named 2026-08-11, effective 2026-09-10)
  Two forced migrations for this model slot within 41 days.
```

*Derived from this source and `docs-github-copilot-aug2026-model-deprecations.md`*

## Cross-References

- **Corroborates** `docs-github-copilot-aug2026-model-deprecations.md`
  Claims 5-7 (enable-then-verify admin procedure, no-action-required
  auto-removal, account-manager support channel): all three recur
  near-verbatim in this notice, extending the confirmed cross-provider
  standardized playbook to a sixth notice.
- **Corroborates** `blog-simonwillison-microsoft-mai-models.md` Claims 3-6
  and `docs-github-copilot-mai-code-1-flash-more-surfaces.md` Claim 4
  (Microsoft self-reports favorable performance figures for MAI-family
  models without disclosing methodology): Claim 11 of this note extends
  that pattern to MAI-Code-1.1-Flash's Terminal-Bench 2.1, .NET, and
  token-efficiency figures.
- **Contradicts** `docs-github-copilot-aug2026-model-deprecations.md`
  Claim 2 (affected-surfaces sentence is "fixed boilerplate GitHub reuses
  regardless of provider or model count"): this notice's deprecation
  sentence omits the enumerated surface list entirely (Claim 4 above).
  **Contradiction issue filed: #2650.** Do not treat either framing as
  settled until that issue resolves.
- **Extends** `docs-github-copilot-aug2026-model-deprecations.md` (which
  established MAI-Code-1-Flash as Raptor Mini's named Copilot successor on
  July 31, 2026) with the immediate follow-on event: MAI-Code-1-Flash's own
  deprecation, 11 days later (Claim 2). Together the two notices document a
  successor-model chain (Raptor Mini → MAI-Code-1-Flash → MAI-Code-1.1-Flash)
  compressed into a 41-day window.
- **Extends** `docs-github-copilot-mai-code-1-flash-more-surfaces.md` Claims
  2 and 7 (MAI-Code-1-Flash's June 18, 2026 expansion excluded Business and
  Enterprise tiers, "forthcoming"): MAI-Code-1.1-Flash's launch (Claim 9)
  reverses that sequencing, including Business/Enterprise from day one
  (behind an admin policy, per Claim 10) while restricting Free/Student to
  auto-selection only — a materially different rollout shape than its
  predecessor's individual-tier-first pattern.
- **Extends** `blog-simonwillison-microsoft-mai-models.md` Claims 1-2 (the
  original MAI-Code-1-Flash launch, 137B total / 5B active parameter MoE,
  purpose-built for Copilot/VS Code): this source documents that same model
  reaching end-of-life roughly 70 days after Claim 1's June 2 initial launch
  date, one of the shorter model lifespans in the corpus.
- **Novel**:
  - **First corpus documentation of a named deprecation successor itself
    being deprecated within days of taking on that role** (Claim 2) — no
    prior corpus notice shows a chain this compressed.
  - **First corpus example of the affected-surfaces boilerplate sentence
    being omitted** (Claim 4) — see contradiction issue #2650.
  - **First corpus source pairing a GitHub product changelog with the
    underlying vendor's own technical announcement for the same model
    release**, surfacing a wording discrepancy (vision-support claim
    present only in GitHub's text, Claim 7) and a naming discrepancy
    ("MAI-Code-1-Flash" vs. Microsoft's informal "1.0," Claim 12) between
    the two companies' own official channels.
  - **First corpus deprecation notice with concrete, itemized replacement
    pricing** (73% lower list price, 0.25× premium multiplier, Claim 8) —
    prior notices named a successor but never quantified the pricing
    delta.

## Guide Impact

### Chapter 02: Harness Engineering / Tooling Landscape

- **Model roster update**: MAI-Code-1-Flash should be marked deprecated
  (effective September 10, 2026) with MAI-Code-1.1-Flash as the confirmed
  replacement, in any model roster the guide maintains for GitHub Copilot.
  Note the compressed timeline explicitly: teams that just migrated from
  Raptor Mini to MAI-Code-1-Flash for the September 1 cutover face a second,
  unrelated migration nine days later.
- **New caution — successor-of-a-successor churn**: The guide's existing
  "avoid hardcoding model identifiers" recommendation
  (`docs-github-copilot-gpt52-deprecation.md` Guide Impact §Ch02;
  reinforced by `docs-github-copilot-aug2026-model-deprecations.md` Guide
  Impact §Ch02) should add this as its sharpest data point yet: even a
  model named as an official migration target in one notice can itself be
  deprecated before that migration's own deadline arrives. Auto-routing or
  admin-policy-managed model selection is now demonstrably more resilient
  than pinning to *either* the deprecated model *or* its just-announced
  successor.
- **Changelog-reading caution, refined**: Per Claim 4 and issue #2650, the
  guide should not assert that GitHub's deprecation-notice surface
  enumeration is always present — the fifth notice reviewed by this corpus
  omitted it. Practitioners parsing changelogs programmatically should not
  rely on that parenthetical list being present to identify a deprecation's
  scope; the deprecation table itself is the reliable structured signal.

### Chapter 05: Team Adoption / Enterprise Governance

- **Migration-cadence tracking needs to account for successor-model
  volatility, not just original-model deprecation dates**: Governance
  processes that track "when does Model X get deprecated" should also track
  "is Model X's *replacement* itself newly launched and therefore at
  elevated near-term deprecation risk." A replacement announced within the
  last few weeks (as MAI-Code-1-Flash was on July 31) should be flagged as
  higher churn risk than a replacement that has been stable for months.
- **Vendor performance claims remain unverifiable without independent
  evaluation**: Claim 11's Terminal-Bench 2.1 and .NET figures are more
  specific than earlier MAI announcements but still lack disclosed
  methodology. The guide's existing recommendation to require independent
  evaluation before model-selection decisions
  (`docs-github-copilot-mai-code-1-flash-more-surfaces.md` Guide Impact
  §Ch05) applies unchanged to MAI-Code-1.1-Flash.

## Extraction Notes

1. **Three companion sources read in full, not just the triage-linked
   page**: Per MINER.md §1's "follow substantive linked pages" guidance,
   this note reads (a) the deprecation notice itself, (b) GitHub's same-day
   companion changelog announcing MAI-Code-1.1-Flash's availability (linked
   directly in the deprecation page's related-posts section), and (c)
   Microsoft's own microsoft.ai announcement for the same model (reached via
   the `aka.ms/mai-code-1.1-flash` redirect embedded in source (b)). All
   three were fetched as raw HTML via `curl`, not WebFetch summaries alone,
   specifically to support verbatim quote verification.
2. **WebFetch vs. raw-HTML discrepancy caught and corrected**: An initial
   WebFetch pass against the Microsoft microsoft.ai page reported a "vision
   support" claim as part of Microsoft's own announcement. Direct raw-HTML
   inspection of that page found no mention of "vision" anywhere in the
   article text — the vision-support claim originates only in GitHub's
   companion changelog (source (b) above), not Microsoft's own post. This
   is documented explicitly in Claim 7 and the Concrete Artifacts section
   rather than silently corrected, since it is itself a notable finding
   about the two companies' announcements not being identical in content.
3. **Triage comments were duplicated three times** on the source issue,
   all independently concluding the source was likely a distinct new
   deprecation event (high novelty) rather than a duplicate of the July 31
   notice. This extraction confirms that conclusion directly (Claim 1).
4. **Contradiction filed**: Issue #2650, covering whether the
   "affected surfaces" enumeration sentence is genuinely fixed GitHub
   boilerplate (per `docs-github-copilot-aug2026-model-deprecations.md`
   Claim 2) or variable per-notice (per this note's Claim 4). No verdict is
   asserted in this note; see the issue for resolution status.
5. **Cross-reference verification performed**: All `Claim N` citations to
   `docs-github-copilot-aug2026-model-deprecations.md`,
   `docs-github-copilot-mai-code-1-flash-more-surfaces.md`, and
   `blog-simonwillison-microsoft-mai-models.md` were checked against those
   notes' actual claim numbering (each note re-read in full before citing);
   none were guessed.
