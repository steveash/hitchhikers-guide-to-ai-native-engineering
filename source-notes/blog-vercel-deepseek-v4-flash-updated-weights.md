---
source_url: https://vercel.com/changelog/deepseek-v4-flash-now-runs-updated-weights-on-ai-gateway
source_type: blog-post
title: "DeepSeek V4 Flash now runs updated weights on AI Gateway"
author: Jerilyn Zheng (Vercel, Product — AI Gateway)
date_published: 2026-07-31
date_extracted: 2026-08-30
last_checked: 2026-08-30
status: current
confidence_overall: emerging
issue: "#3103"
---

# DeepSeek V4 Flash now runs updated weights on AI Gateway

> A short Vercel changelog entry announcing that the stable `deepseek/deepseek-v4-flash`
> model ID on AI Gateway now silently serves updated weights, with a
> Terminal-Bench score of 82.7 (up 25.8 points from 56.9 in the "April
> preview") — the first concrete agentic-benchmark figure in this corpus's
> DeepSeek V4 Flash coverage — but the changelog never names this update
> "0731," and Vercel's own leaderboard tracks "DeepSeek V4 Flash" and
> "DeepSeek V4 Flash 0731" as two distinct, simultaneously-active model
> entries, so this update's identity relative to Simon Willison's
> July 31 V4-Flash-0731 post is a same-day correlation, not a confirmed match.

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`,
  published 2026-07-31T00:00-07:00 per the page's own embedded JSON-LD,
  `dateModified` 2026-07-31T17:05:09.064Z; a single-screen feature-update
  announcement — one headline paragraph, one code example, one CLI-onboarding
  pointer, and one pricing-policy paragraph).
- **Author credibility**: First-party Vercel changelog entry, author verified
  against the page's embedded JSON-LD (`"author":[{"@type":"Person","name":"Jerilyn
  Zheng","jobTitle":"Product, AI Gateway"...}]`) and the byline anchor tag
  (`href="https://twitter.com/jerilynzheng" rel="author"`). Zheng is the same
  recurring AI-Gateway product-team byline already documented in
  `blog-vercel-ai-gateway-fable-5-restored.md`,
  `blog-vercel-ai-gateway-realtime-voice-speech.md`, and
  `blog-vercel-ai-gateway-xai-grok-audio-models.md`. Vercel operates AI
  Gateway, so this is first-party documentation of a platform-side weight
  update and its downstream Terminal-Bench score — not independent
  benchmarking, and not DeepSeek's own announcement of the update.
- **Scope**: Covers the Terminal-Bench score delta for the updated weights,
  the model-ID stability of the update (no code change required), a
  coding-agent CLI onboarding path, provider rollout status (DeepSeek-only
  for now, others including ZDR providers "coming next week"), and AI
  Gateway's general no-markup pricing policy. Does NOT cover: which specific
  checkpoint/version name the updated weights correspond to, Terminal-Bench's
  version number or task suite, DeepSeek's own announcement of the update (if
  any), per-token pricing for the updated weights specifically, or any
  benchmark besides Terminal-Bench.

## Extracted Claims

### Claim 1: The updated DeepSeek V4 Flash weights score 82.7 on Terminal-Bench, up 25.8 points from 56.9 in "the April preview"
- **Evidence**: The changelog's opening/headline sentence, stating both the new score and the delta against a named prior baseline.
- **Confidence**: emerging (a specific, first-party numeric benchmark result — but Terminal-Bench's version/suite is unnamed, and the "April preview" baseline is not independently dated or sourced within this changelog)
- **Quote**: "DeepSeek V4 Flash now runs on updated weights by default on AI Gateway, with notably stronger agentic capabilities. On Terminal-Bench, it scores 82.7, up 25.8 points from 56.9 in the April preview."
- **Our assessment**: This is exactly the evidence gap the Prospector's triage flagged: `blog-simonwillison-deepseek-v4-flash-0731.md` Claim 1 documented DeepSeek's "substantially enhanced agentic capabilities" framing as asserted but unbenchmarked in that source, and its "Our assessment" explicitly named "an agentic-specific benchmark (SWE-bench Verified, Terminal-Bench, or similar)" as what would be needed to substantiate it. This changelog supplies a named Terminal-Bench score and a concrete delta. However, it does not state a Terminal-Bench version number (the rest of this corpus's Terminal-Bench figures are all versioned "Terminal-Bench 2.1," per `blog-cognition-swe17.md` and `blog-openai-gpt56-ga-announcement.md`), so the 82.7/56.9 pair cannot be confirmed as directly comparable to those other in-corpus scores on methodological grounds — only that they use the same benchmark name and 0-100-ish scale. Treat as strong but not fully reconciled evidence.

### Claim 2: Requests to the model ID `deepseek/deepseek-v4-flash` pick up the new weights automatically, with no change to the model ID or calling code required
- **Evidence**: The changelog's second sentence, immediately following the benchmark claim.
- **Confidence**: settled (first-party statement of the update mechanism)
- **Quote**: "Requests to deepseek/deepseek-v4-flash pick up the new weights automatically, with no change to the model ID or your code."
- **Our assessment**: This is a distinct update mechanism from the version-suffixed checkpoint releases documented elsewhere in this corpus (e.g., `blog-simonwillison-deepseek-v4-flash-0731.md`'s "deepseek-v4-flash-0731" as a separate, newly-named checkpoint). Here, the same stable model ID silently changes behavior underneath a pinned string. No existing source note in this corpus documents this "same ID, swapped weights" update pattern for any provider — it is a genuinely novel reproducibility concern: a team that benchmarked or evaluated `deepseek/deepseek-v4-flash` before July 31, 2026 and pins that exact model string could see materially different results after this date without any visible signal in their own code or config, since 56.9 → 82.7 is a very large single-update swing.

### Claim 3: The changelog does not name this update "0731" anywhere, and Vercel's own AI Gateway leaderboard tracks "DeepSeek V4 Flash" and "DeepSeek V4 Flash 0731" as two separate, simultaneously-active model entries with independent token-volume and request shares
- **Evidence**: Direct text search of the fetched changelog page found zero occurrences of the string "0731"; the linked AI Gateway leaderboard (`vercel.com/ai-gateway/leaderboards`, followed per MINER.md §1) lists "DeepSeek V4 Flash" at 27.6% token volume / 19.4% of requests and "DeepSeek V4 Flash 0731" separately at 4.4% token volume / 6.8% of requests, for the same Jun 1 – Aug 29, 2026 window.
- **Confidence**: settled (both facts — the absence of "0731" in the changelog HTML, and the leaderboard's two separate rows — are directly, independently verifiable)
- **Quote**: (no single quote states this distinction explicitly; it is established by the absence of "0731" in the changelog's own text combined with the leaderboard's two separate line items — see Concrete Artifacts for the leaderboard rows)
- **Our assessment**: This directly complicates the Prospector's triage assumption (repeated across all three triage comments on this issue) that this changelog documents the same checkpoint as `blog-simonwillison-deepseek-v4-flash-0731.md`. Same-day publication (both July 31, 2026) and matching thematic framing ("substantially enhanced agentic capabilities" / "notably stronger agentic capabilities") make a connection plausible, but Vercel's own product surface treats "DeepSeek V4 Flash" (the ID this changelog is about) and "DeepSeek V4 Flash 0731" (a separately cataloged, separately tracked model) as two different things, at least for gateway-routing and leaderboard-accounting purposes. This note does not resolve whether the *weights themselves* are identical (Vercel's `deepseek/deepseek-v4-flash` update could plausibly still be, under the hood, the same weights DeepSeek shipped as its named "0731" release, routed through a different gateway-facing ID) — it flags the gap so the guide does not silently merge these two sources into a single unambiguous checkpoint story. Not filed as a MINER.md §4a contradiction, since neither source makes a claim the other directly disputes; this is an identity/scope ambiguity, not a factual disagreement.

### Claim 4: For now, DeepSeek is the only provider serving the updated weights on AI Gateway; other providers, including ones offering Zero Data Retention, are coming next week
- **Evidence**: The changelog's third sentence, a direct rollout-status statement.
- **Confidence**: settled (first-party statement of current rollout scope and near-term timeline)
- **Quote**: "For now, DeepSeek is the only provider serving the updated weights. Other providers, including ones with Zero Data Retention, are coming next week."
- **Our assessment**: This is an explicit, actionable compliance caveat: as of this changelog's July 31, 2026 publication, a team on AI Gateway requiring Zero Data Retention cannot get it while also getting the updated (82.7 Terminal-Bench) weights — they must currently route through DeepSeek's own provider slot, which this source does not state offers ZDR. The model page for the base `deepseek/deepseek-v4-flash` ID (followed per MINER.md §1) states generically that "Zero Data Retention is available for this model... offered on a per-provider and model basis" without confirming DeepSeek's own provider row supports it at the time of this changelog. Teams with a hard ZDR requirement should verify provider-level ZDR support before assuming the updated weights are available to them without a retention trade-off.

### Claim 5: To run the updated V4 Flash in a coding agent, developers should run `vercel ai-gateway coding-agents setup` to connect their agents to AI Gateway, then select `deepseek/deepseek-v4-flash` in the agent's model configuration
- **Evidence**: A dedicated paragraph and CLI command, distinct from the AI SDK code example, specifically addressed to coding-agent integration.
- **Confidence**: settled (first-party runnable CLI command, named and quoted directly)
- **Quote**: "To run V4 Flash in a coding agent, use vercel ai-gateway coding-agents setup to connect your agents to AI Gateway, then select deepseek/deepseek-v4-flash in the agent's model configuration."
- **Our assessment**: This is the first source note in this corpus to document a `vercel ai-gateway coding-agents setup` CLI subcommand specifically for coding-agent onboarding, distinct from the `vercel ai-gateway api-keys create` (budgets, per `blog-vercel-ai-gateway-api-key-budgets.md`) and `vercel ai-gateway rules add --type rewrite` (routing rewrites, per `blog-vercel-gpt56-ai-gateway-availability.md` Claim 4) subcommands already documented — a third independent subcommand family under the `vercel ai-gateway` CLI namespace, suggesting a broader dedicated CLI surface than any single prior note showed. The changelog does not describe what the setup command actually configures (credentials, config files, agent-specific adapters), so practitioners still need the linked "coding agents guide" (`vercel.com/docs/ai-gateway/coding-agents`) for the mechanics.

### Claim 6: AI Gateway reflects provider pricing with no markup and does not charge a platform fee on inference, including on Bring Your Own Key (BYOK) requests
- **Evidence**: A single closing pricing-policy sentence, identical in wording to the same policy statement documented elsewhere in this corpus.
- **Confidence**: settled (first-party pricing-policy statement, and this exact sentence is now independently confirmed verbatim across at least two separate AI Gateway changelogs)
- **Quote**: "AI Gateway reflects provider pricing with no markup and does not charge a platform fee on inference, including on Bring Your Own Key (BYOK) requests."
- **Our assessment**: This sentence is word-for-word identical to `blog-vercel-gpt56-ai-gateway-availability.md` Claim 6's quoted text, confirming it is standardized boilerplate reused across AI Gateway model-update changelogs rather than DeepSeek-specific content. Its presence here adds no new information beyond re-confirming the policy applies uniformly to this update; its main value is corroboration (a second, independently-fetched instance of the identical sentence, strengthening confidence that this is genuinely platform-wide policy language rather than a one-off claim). Per that note's own Claim 9, however, "no markup" is scoped to whichever upstream provider actually serves a request — this changelog's Claim 4 (DeepSeek-only for now) means that scoping question is currently moot for the updated weights specifically, since only one provider route exists.

### Claim 7: On Vercel's AI Gateway leaderboard (Jun 1 – Aug 29, 2026 window), "DeepSeek V4 Flash" is the single largest model by both token volume (27.6%) and request share (19.4%) of all AI Gateway traffic, ahead of every named competitor including Claude Opus 4.8, GPT 5.6 Luna, and MiniMax M3
- **Evidence**: The AI Gateway leaderboard page's "Token Volume" and "Requests" ranked lists, followed per MINER.md §1 as a substantive linked page.
- **Confidence**: settled (a specific, directly-observed, checkable ranked list on a live first-party analytics page, though it is anonymized aggregate telemetry with no per-workload breakdown)
- **Quote**: (no prose quote; read directly from the ranked list — see Concrete Artifacts for the full top-10 reproduction)
- **Our assessment**: This is independent evidence of real-world adoption scale behind the Terminal-Bench improvement claim (Claim 1): whatever weight update this changelog describes affects the single most heavily-used model on one of the larger third-party inference gateways, not a niche or low-traffic route. This strengthens the practical stakes of Claim 2's reproducibility concern — a silent weights swap under a stable ID matters more when that ID already carries the largest share of a major gateway's traffic. The leaderboard does not break down usage by workload type (agentic vs. simple completion), so this cannot itself confirm how much of that 27.6%/19.4% share is agentic/coding-agent traffic specifically.

### Claim 8: A live, separately-maintained "About Deepseek V4 Flash" product page still recommends escalating to "DeepSeek V4 Pro" for "complex agent orchestration" and "multi-step reasoning and tool planning," without mentioning the July 31 weights update or its Terminal-Bench improvement
- **Evidence**: The `vercel.com/ai-gateway/models/deepseek-v4-flash` model catalog page (followed per MINER.md §1, fetched live on 2026-08-30 — one month after this changelog's publication), which describes the model as released "April 23, 2026" and positions it as unsuited for complex agentic work.
- **Confidence**: emerging (a specific, directly observed live-page finding, but its cause — stale marketing copy vs. a genuine ongoing capability gap for orchestration-heavy tasks specifically — is not something this Miner can resolve from the pages alone)
- **Quote**: "Deepseek V4 Flash is tuned for speed and cost on shorter tasks. If your workload involves multi-step reasoning, complex agentic flows, or long synthesis chains, DeepSeek V4 Pro is the better fit within the same generation." / "Complex agent orchestration: Use DeepSeek V4 Pro within the same generation for multi-step reasoning and tool planning."
- **Our assessment**: This is a live-page tension of the same shape already flagged in `blog-vercel-gpt56-ai-gateway-availability.md` Claim 1 (a same-surface internal inconsistency between a changelog's capability framing and another page's positioning), though here the two pages are a month apart rather than same-day. The changelog's headline claim is "notably stronger agentic capabilities" backed by a 25.8-point Terminal-Bench gain, yet the model's own persistent catalog description (as of this extraction, 2026-08-30) still frames it as the wrong choice for "complex agent orchestration" and recommends stepping up to V4 Pro for exactly that use case. This may simply be marketing copy that lags a weights update rather than a substantive capability claim, but the guide should not cite the changelog's "stronger agentic capabilities" framing as meaning V4 Flash is now Vercel's own recommended choice for complex agentic orchestration — the vendor's own current positioning copy says otherwise. Not filed as a MINER.md §4a contradiction: this is two statements from the same vendor about the same model family that are in tension due to apparent copy staleness, not a factual dispute between independent sources.

## Concrete Artifacts

### Changelog article body (verbatim, extracted via direct `curl` fetch + BeautifulSoup `<article>` isolation, not WebFetch summarization)

```
DeepSeek V4 Flash now runs on updated weights by default on AI Gateway,
with notably stronger agentic capabilities. On Terminal-Bench, it scores
82.7, up 25.8 points from 56.9 in the April preview.

Requests to deepseek/deepseek-v4-flash pick up the new weights
automatically, with no change to the model ID or your code.

For now, DeepSeek is the only provider serving the updated weights. Other
providers, including ones with Zero Data Retention, are coming next week.

To use the updated DeepSeek V4 Flash, set model to deepseek/deepseek-v4-flash
in the AI SDK. AI Gateway will route to providers with the new weights by
default:

[code example — see below]

To run V4 Flash in a coding agent, use vercel ai-gateway coding-agents setup
to connect your agents to AI Gateway, then select deepseek/deepseek-v4-flash
in the agent's model configuration. See the coding agents guide.

AI Gateway reflects provider pricing with no markup and does not charge a
platform fee on inference, including on Bring Your Own Key (BYOK) requests.
Learn more about AI Gateway, view the AI Gateway model leaderboard or try
it in our model playground.

Source: https://vercel.com/changelog/deepseek-v4-flash-now-runs-updated-weights-on-ai-gateway
```

### AI SDK usage example (verbatim, from the changelog)

```typescript
import { streamText } from 'ai';

const result = streamText({
  model: 'deepseek/deepseek-v4-flash',
  prompt: 'Fix the failing tests in this repo and open a PR.',
});
```
Source: https://vercel.com/changelog/deepseek-v4-flash-now-runs-updated-weights-on-ai-gateway

### Page metadata (from embedded JSON-LD, verified independently of WebFetch)

```
datePublished: 2026-07-31T00:00-07:00
dateModified:  2026-07-31T17:05:09.064Z
author: Jerilyn Zheng, jobTitle "Product, AI Gateway"
description: "DeepSeek V4 Flash now runs on updated weights on AI Gateway,
  served by DeepSeek by default, with stronger agentic capabilities."
```

### AI Gateway leaderboard, Top Models by Token Volume and Requests (Jun 1 – Aug 29, 2026 window; fetched live 2026-08-30 from vercel.com/ai-gateway/leaderboards, followed per MINER.md §1)

```
Token Volume share (top 10):
1. DeepSeek V4 Flash        27.6%
2. Step 3.7 Flash           12.3%
3. MiniMax M3                8.4%
4. GLM 5.3 Flash             5.6%
5. GPT 5.6 Luna              4.6%
6. DeepSeek V4 Flash 0731    4.4%
7. Claude Opus 4.8           4.2%
8. Claude Opus 5             3.5%
9. Claude Sonnet 5           3.0%
10. Other                   26.4%

Requests share (top 10):
1. DeepSeek V4 Flash        19.4%
2. GPT-5 nano                7.2%
3. DeepSeek V4 Flash 0731    6.8%
4. GPT 5.6 Luna              5.4%
5. Step 3.7 Flash            4.6%
6. text-embedding-3-small    4.1%
7. Gemini 3.1 Flash Lite     3.6%
8. MiniMax M3                3.3%
9. Claude Sonnet 5           2.7%
10. Other                   42.9%

Source: vercel.com/ai-gateway/leaderboards, fetched live via curl 2026-08-30.
Note: "DeepSeek V4 Flash" and "DeepSeek V4 Flash 0731" appear as two
separate, independently-ranked entries in both lists.
```

### "About Deepseek V4 Flash" catalog-page positioning copy (verbatim; fetched live 2026-08-30 from vercel.com/ai-gateway/models/deepseek-v4-flash)

```
"Deepseek V4 Flash was released April 23, 2026 as part of DeepSeek's V4
generation. ... Deepseek V4 Flash positions as the efficiency tier of the
V4 lineup. It handles instruction following, classification, short-form
Q&A, and other tasks where latency and per-token cost matter more than
maximum reasoning depth."

"Configuration: Deepseek V4 Flash is tuned for speed and cost on shorter
tasks. If your workload involves multi-step reasoning, complex agentic
flows, or long synthesis chains, DeepSeek V4 Pro is the better fit within
the same generation."

"Consider alternatives when — Complex agent orchestration: Use DeepSeek
V4 Pro within the same generation for multi-step reasoning and tool
planning."

Source: vercel.com/ai-gateway/models/deepseek-v4-flash, fetched live 2026-08-30.
```

## Cross-References

### Cross-reference verification notes
`blog-simonwillison-deepseek-v4-flash-0731.md`, `blog-vercel-ai-gateway-fable-5-restored.md`,
`blog-vercel-gpt56-ai-gateway-availability.md`, `blog-vercel-ai-gateway-api-key-budgets.md`,
and `blog-cognition-swe17.md` were re-read in full during this extraction
(MINER.md §4b), and every claim number cited above was located and confirmed
against each note's own numbered `### Claim` headings before writing this
section.

- **Corroborates**:
  - `blog-vercel-gpt56-ai-gateway-availability.md` Claim 6 ("AI Gateway
    reflects provider pricing with no markup and does not charge a platform
    fee on inference, including on Bring Your Own Key (BYOK) requests."):
    this source's Claim 6 reproduces the identical sentence verbatim,
    confirming it as standardized cross-changelog policy boilerplate rather
    than a one-off statement.
  - `blog-vercel-gpt56-ai-gateway-availability.md` Claim 4 (`vercel ai-gateway
    rules add --type rewrite`) and `blog-vercel-ai-gateway-api-key-budgets.md`
    Concrete Artifacts (`vercel ai-gateway api-keys create --budget ...`):
    this source's Claim 5 (`vercel ai-gateway coding-agents setup`) confirms
    the `vercel ai-gateway` CLI has at least three independent subcommand
    families (`api-keys`, `rules`, `coding-agents`), extending the CLI
    surface documented across these two prior notes.
  - `blog-cognition-swe17.md` Concrete Artifacts (Terminal-Bench 2.1 scores:
    GLM-5.2 81.0%, SWE-1.7 81.5%, GPT-5.5 84.2%, Opus 4.8 86.9%) and
    `blog-openai-gpt56-ga-announcement.md` Concrete Artifacts (Terminal-Bench
    2.1 scores ranging 70.7%–91.9% across a different model set): this
    source's Claim 1 places the updated DeepSeek V4 Flash's 82.7 score
    within the same numeric band as these frontier coding-agent models —
    directionally corroborating that the update brings V4 Flash's agentic
    coding performance close to frontier tier, though (per Claim 1's Our
    assessment) the Terminal-Bench version is unconfirmed, so this is
    directional corroboration, not a verified apples-to-apples comparison.

- **Contradicts**: None filed as a formal MINER.md §4a contradiction issue.
  Two tensions are flagged explicitly rather than silently resolved (see
  Claims 3 and 8 above):
  1. **Claim 3** — this changelog's silence on "0731" versus the leaderboard's
     treatment of "DeepSeek V4 Flash" and "DeepSeek V4 Flash 0731" as
     separate entries, which complicates (without directly contradicting)
     the Prospector's triage assumption that this source fills the benchmark
     gap in `blog-simonwillison-deepseek-v4-flash-0731.md` for the *same*
     checkpoint. Not filed because no source makes a claim the other
     disputes — this is an identity-scope ambiguity between two sources
     about closely related but not confirmed-identical model releases.
  2. **Claim 8** — the changelog's "notably stronger agentic capabilities"
     framing versus the live catalog page's persistent "use V4 Pro for
     complex agent orchestration" guidance for the same model family. Not
     filed because both statements come from the same vendor (Vercel) about
     the same underlying model, and the more likely explanation is
     copy staleness rather than a substantive factual dispute.

- **Extends**:
  - `blog-simonwillison-deepseek-v4-flash-0731.md` Claim 1: that note
    documented DeepSeek's "substantially enhanced agentic capabilities"
    framing as an unverified vendor claim and named Terminal-Bench as an
    example of the missing evidence type. This source's Claim 1 supplies
    exactly that missing benchmark category (Terminal-Bench, 82.7 vs. 56.9)
    — though, per Claim 3, whether it applies to the identical checkpoint
    Willison covered is not confirmed by this source.
  - `blog-vercel-gpt56-ai-gateway-availability.md` and
    `blog-vercel-ai-gateway-api-key-budgets.md`: extends the documented
    `vercel ai-gateway` CLI surface with a third subcommand family
    (`coding-agents setup`, Claim 5) specifically for coding-agent
    onboarding, not present in either prior note.

- **Novel**:
  - **A "same model ID, silently swapped weights" update mechanism**
    (Claim 2): no prior source note in this corpus documents a provider
    changing a model's underlying weights behind a stable, pinned model
    string, as opposed to shipping a new version-suffixed checkpoint. This
    has direct evaluation-reproducibility implications not previously
    surfaced in this corpus.
  - **A dedicated CLI onboarding path for coding agents** (Claim 5,
    `vercel ai-gateway coding-agents setup`): the first documented AI
    Gateway CLI subcommand specifically targeting coding-agent integration
    rather than general API-key or routing configuration.
  - **Leaderboard-level adoption-scale evidence for a single model update**
    (Claim 7): the first source note in this corpus to pair a specific
    weights-update announcement with the model's actual share of aggregate
    third-party gateway traffic.

## Guide Impact

- **Chapter 06 (Evaluation & Benchmarking)**: Add Claim 2 (silent weight
  updates behind a stable model ID) as a concrete, named risk for any guide
  section on benchmark reproducibility or model-version pinning: pinning a
  model string (e.g., `deepseek/deepseek-v4-flash`) does not guarantee pinning
  behavior, when a gateway or provider can swap weights underneath that ID
  without a version bump. Recommend the guide advise teams doing longitudinal
  evaluation to snapshot or re-verify a model's benchmark scores periodically
  even when their own configuration hasn't changed, and to prefer explicitly
  version-suffixed model IDs (e.g., `deepseek-v4-flash-0731`) when
  reproducibility matters more than automatically receiving improvements.

- **Chapter 03 (Model Selection)**: Cite Claim 1 (82.7 Terminal-Bench, +25.8
  from 56.9) as the concrete benchmark evidence that was missing from
  `blog-simonwillison-deepseek-v4-flash-0731.md`'s coverage of DeepSeek's
  "substantially enhanced agentic capabilities" claim — but pair it with
  Claim 3's caveat that this update's identity relative to the "0731"
  checkpoint documented there is not confirmed, so the guide should not
  present the two sources as describing one unambiguous release. Also cite
  Claim 8 as a caution against over-reading the "stronger agentic
  capabilities" headline: Vercel's own current model-catalog copy still
  recommends V4 Pro over V4 Flash for complex agent orchestration.

- **Chapter 05 (Infrastructure / Multi-Provider Routing)**: Add Claim 4 (only
  DeepSeek serves the updated weights initially; ZDR-capable providers are
  "coming next week") as a concrete example of a capability/compliance
  trade-off during a provider rollout window — teams needing both the
  improved weights and Zero Data Retention could not get both simultaneously
  at the time of this changelog. Add Claim 5's `vercel ai-gateway
  coding-agents setup` command as a reference onboarding step for connecting
  coding agents to AI Gateway models generally, not just this DeepSeek
  update.

## Extraction Notes

1. **Raw HTML fetched directly via `curl` with a browser user-agent**, not
   through WebFetch, following the precedent in
   `blog-vercel-ai-gateway-fable-5-restored.md` and
   `blog-vercel-gpt56-ai-gateway-availability.md` Extraction Notes that
   WebFetch has produced inconsistent paraphrases of Vercel changelog text
   across repeated calls. The article body was isolated via BeautifulSoup's
   `<article>` tag; author, `datePublished`, and `dateModified` were read
   directly from the page's embedded `application/ld+json` script rather
   than inferred from rendered text. All `Quote` fields above were located
   character-for-character in that fetched HTML/JSON.
2. **Three linked pages followed, per MINER.md §1** ("follow up to 5 linked
   pages that seem substantive"): the changelog's own "model playground" /
   `DeepSeek V4 Flash` links go to `vercel.com/ai-gateway/models/deepseek-v4-flash`
   (fetched live, source for Claims 4 and 8); the "AI Gateway model
   leaderboard" link goes to `vercel.com/ai-gateway/leaderboards` (fetched
   live via curl with `-L` to follow a 307 redirect, source for Claim 7).
   The "coding agents guide" (`vercel.com/docs/ai-gateway/coding-agents`) and
   generic "AI Gateway" docs links were not followed — they are general
   platform documentation not specific to this weights update, consistent
   with the "generic platform-feature pages... not specific to [this
   announcement]" judgment call already made in
   `blog-vercel-gpt56-ai-gateway-availability.md` Extraction Notes for
   analogous generic links.
3. **The `vercel.com/ai-gateway/models/deepseek-v4-flash` catalog page and
   the leaderboard were both fetched live on 2026-08-30**, one month after
   this changelog's July 31, 2026 publication date. Claims 7 and 8 are
   explicitly timestamped to that later fetch date and are not attributed to
   the changelog's original publication-day state, since the changelog itself
   contains neither the leaderboard percentages nor the catalog page's
   positioning copy.
4. **No contradiction issue filed.** Two tensions were identified and
   evaluated against MINER.md §4a (see Cross-References → Contradicts): the
   "0731"-identity ambiguity (Claim 3) and the "stronger agentic
   capabilities" vs. "use V4 Pro for complex orchestration" tension (Claim
   8). Both were judged to be scope/staleness ambiguities within the same
   vendor's own documentation, not material factual disputes between
   independent sources that would drive different guide advice. The Assayer
   or Smith may reach a different conclusion on Claim 3 in particular, given
   how directly the Prospector's triage comments assumed a match with the
   Willison "0731" post.
5. **Three duplicate Prospector triage comments** appeared on issue #3103,
   each asserting (with varying confidence: "medium," "high," then "medium"
   again) that this source fills the agentic-benchmark gap in
   `blog-simonwillison-deepseek-v4-flash-0731.md` for the *same* checkpoint —
   a known corpus pattern from automated re-triage runs, also documented in
   `blog-vercel-ai-gateway-fable-5-restored.md` and
   `blog-vercel-ai-gateway-xai-grok-audio-models.md` Extraction Notes. This
   Miner independently verified the "0731" identity assumption against the
   actual page text (Claim 3) rather than accepting any triage comment's
   framing at face value, and found the assumption unconfirmed by this
   source — the changelog and the leaderboard both point to "DeepSeek V4
   Flash" and "DeepSeek V4 Flash 0731" being tracked as distinct entities on
   Vercel's own platform.
6. **Confidence calibration: emerging.** Individual platform-mechanics claims
   (Claims 2, 4, 5, 6) are "settled" — first-party, directly quoted
   statements about shipping behavior. The note's overall confidence is
   "emerging" rather than "settled" because: (a) Claim 1, the headline
   benchmark claim, lacks a stated Terminal-Bench version and an independently
   sourced "April preview" baseline; (b) Claim 3 leaves a real, unresolved
   ambiguity about which checkpoint this update actually corresponds to,
   which affects how confidently this source can be said to extend
   `blog-simonwillison-deepseek-v4-flash-0731.md`; and (c) Claim 8 shows the
   vendor's own current documentation is not fully internally consistent
   with the changelog's capability framing a month later.
