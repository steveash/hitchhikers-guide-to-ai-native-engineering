---
source_url: https://vercel.com/changelog/claude-fable-5-access-restored-on-ai-gateway
source_type: blog-post
title: "Claude Fable 5 Access Restored on AI Gateway"
author: Jerilyn Zheng (Vercel, Product — AI Gateway)
date_published: 2026-07-01
date_extracted: 2026-07-31
last_checked: 2026-07-31
status: current
confidence_overall: emerging
issue: "#2364"
---

# Claude Fable 5 Access Restored on AI Gateway

> A short Vercel changelog entry confirming Claude Fable 5's access was
> restored on AI Gateway after the US Government lifted the export control
> directive that suspended it on June 12, 2026 — the first source in this
> corpus to document the restoration from a platform-integration angle,
> with a concrete model-fallback code example (Fable 5 → Opus 4.8 → Sonnet 5)
> and the model's data retention terms.

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`,
  published 2026-07-01T00:01-07:00 per the page's own JSON-LD, `dateModified`
  2026-07-02T06:14:39Z; a single-screen feature/status announcement with one
  runnable code example and no prose beyond a few short paragraphs).
- **Author credibility**: First-party Vercel changelog entry, author
  verified against the page's JSON-LD (`Jerilyn Zheng`, jobTitle "Product,
  AI Gateway") and byline anchor tag (`x.com/jerilynzheng`). Zheng is also a
  credited co-author on `blog-vercel-ai-gateway-realtime-voice-speech.md`
  and `blog-vercel-ai-gateway-xai-grok-audio-models.md` — a recurring
  AI-Gateway product-team byline in this corpus. Vercel operates AI Gateway,
  so this is first-party documentation of a platform integration status
  change, not independent reporting on Anthropic's restoration decision
  itself. No customer, production deployment, or independent verification of
  the underlying export-control lift is cited — Vercel is reporting the
  practical downstream effect (the model is callable again) and giving
  integration guidance, not confirming the policy mechanics.
- **Scope**: Covers AI Gateway's model identifier for Fable 5, the
  recommended model-fallback pattern and a runnable code example for it, and
  Fable 5's data retention terms as they apply to AI Gateway traffic. Does
  NOT cover: the export-control lift itself (dates, government process,
  legal basis), pricing for Fable 5 on AI Gateway, a list of which specific
  request types trigger safety classifiers beyond "coding and debugging,"
  or how the "updated and more robust" safety classifiers differ technically
  from the classifiers in place before the June 12 suspension.

## Extracted Claims

### Claim 1: Access to Claude Fable 5 has been restored on AI Gateway following the US Government's decision to lift the export control directive
- **Evidence**: The changelog's opening sentence and its JSON-LD `description` field, both stating the same fact independently.
- **Confidence**: settled (first-party statement of a platform-level access change, corroborated by the page's own structured metadata)
- **Quote**: "Access to Claude Fable 5, the Mythos-class model, has now been restored on AI Gateway following the US Government's decision to lift the export controls."
- **Our assessment**: This is the first source in this corpus to document Fable 5's restoration explicitly as the reversal of the export control directive, rather than inferring the connection. `blog-latentspace-ainews-fable-relaunch-orchestration.md` Claim 2 reported a July 1 relaunch ("Anthropic re-enabled Claude Fable 5... After a day of pent-up demand") but only inferred the export-control link and explicitly flagged that inference as unconfirmed, recommending "a future Miner should locate and mine Anthropic's own restoration announcement (if one exists) to convert this from an inferred connection to a documented one." This source is not Anthropic's own announcement, but it is a first-party platform statement that makes the same causal claim explicitly, which meaningfully strengthens (though does not fully settle, absent Anthropic's own statement) that inferred link.

### Claim 2: Fable 5 on AI Gateway is the same model that was available between June 9 and June 12, 2026, with only the safety classifiers changed — described as "now updated and more robust"
- **Evidence**: The changelog's second sentence, directly following Claim 1's restoration statement.
- **Confidence**: settled (first-party statement about what changed vs. what stayed the same in the restored model)
- **Quote**: "Fable 5 is the same model that was available between June 9 and June 12. What has changed is the safety classifiers, which are now updated and more robust."
- **Our assessment**: This corroborates the June 9 launch date and June 12 suspension date already established across this corpus (`blog-simonwillison-claude-fable-5.md`, `blog-simonwillison-fable-mythos-access-directive.md`) and directly matches the "updated cybersecurity safeguards" framing `blog-latentspace-ainews-fable-relaunch-orchestration.md` Claim 1 attributed to `@claudeai`'s July 1 announcement. Two independent sources (a social-media-relay digest and a first-party Vercel platform changelog) now agree the restored model is unchanged except for classifier updates — this is stronger corroboration than either source alone.

### Claim 3: In the near term, some routine tasks such as coding and debugging may trigger Fable 5's safety classifiers, and developers should use model fallbacks to ensure requests are still serviced when that happens
- **Evidence**: The changelog's "Usage Guidance" content, presented as a direct operational recommendation to developers integrating Fable 5.
- **Confidence**: settled (first-party operational guidance directly tied to a named, expected failure mode)
- **Quote**: "In the near term, some routine tasks such as coding and debugging may trigger safety classifiers. To ensure requests are still serviced when the safety classifiers are triggered, use model fallbacks."
- **Our assessment**: This is the most actionable claim in the source and a direct, concrete instance of the pattern already surfaced in `blog-simonwillison-fable-silent-interventions.md` Claim 6 (Anthropic "changing to visible safeguards that fall back to Opus 4.8") and `blog-latentspace-ainews-fable-relaunch-orchestration.md` Claim 1 ("updated cybersecurity safeguards may route some requests to Opus 4.8, with biology/chemistry classifiers still overly broad for now"). Naming "coding and debugging" specifically as trigger-prone routine tasks is new and practically significant: it means practitioners building coding agents or debugging assistants on Fable 5 should expect classifier false-positives as a normal operating condition, not an edge case, and should architect for it rather than treat it as an occasional failure.

### Claim 4: AI Gateway will try each model in a configured fallback list, in order, if Anthropic refuses the request to Fable 5 — demonstrated with a runnable example that falls back from Fable 5 to Opus 4.8, then to Sonnet 5
- **Evidence**: A complete TypeScript code example using the AI SDK's `streamText` with `providerOptions.gateway.models` set to `['anthropic/claude-opus-4.8', 'anthropic/claude-sonnet-5']`.
- **Confidence**: settled (first-party runnable code example naming the exact configuration mechanism and specific fallback model IDs)
- **Quote**: "AI Gateway will try each model in models in the stated order if Anthropic refuses the request to Fable 5." / "Call Fable 5 with model fallbacks. This request will fall back to Opus 4.8, then Sonnet 5, if the safety classifier is triggered."
- **Our assessment**: This is the first source in this corpus to show the exact AI Gateway configuration syntax (`providerOptions.gateway.models`) for a safety-classifier-triggered fallback specifically, as opposed to the general-purpose fallback/reliability configuration documented for other purposes elsewhere in the corpus. It gives practitioners a concrete, copyable pattern rather than only a policy description. The specific ordered chain (Fable 5 primary, Opus 4.8 first fallback, Sonnet 5 second fallback) is a specific model-tiering recommendation from the platform vendor, not just an abstract "have a fallback" recommendation.

### Claim 5: Model fallbacks work on every API format on AI Gateway, not just the AI SDK example shown
- **Evidence**: A single sentence following the code example, pointing to the docs for configuring fallbacks across API formats.
- **Confidence**: settled (first-party statement of a platform-wide capability, though this source does not itself demonstrate the other API formats)
- **Quote**: "Model fallbacks work on every API format: for more information on how to configure these, see the docs."
- **Our assessment**: This broadens Claim 4's applicability — teams calling AI Gateway via a format other than the AI SDK's `streamText` (e.g., a raw OpenAI-compatible or Anthropic-compatible request) should not need to change frameworks just to get fallback behavior for Fable 5. This source does not itself show those other formats' syntax, so practitioners still need the linked docs page for anything beyond the AI SDK.

### Claim 6: Anthropic does not support Zero Data Retention for Fable 5 on AI Gateway because some misuse patterns are only visible across cumulative requests, which real-time filters cannot catch on their own; prompts and completions are instead retained for 30 days and not used to train Claude
- **Evidence**: The changelog's "Data Retention Policy" section, giving both the retention terms and Vercel/Anthropic's stated rationale for why ZDR is unavailable.
- **Confidence**: settled (first-party statement of a concrete compliance-relevant policy and its stated rationale)
- **Quote**: "Anthropic does not support Zero Data Retention for the model, because some misuse patterns are only visible across cumulative requests, which real-time filters cannot catch on their own. Prompts and completions are retained for 30 days and are not used to train Claude."
- **Our assessment**: This confirms and extends the 30-day retention policy `blog-latentspace-fable-5-mythos-launch.md` documented at launch for "Mythos-class models" generally ("We will require 30-day retention for all traffic on Mythos-class models" — Anthropic, June 10, 2026) — this source shows the same policy still applies to Fable 5 specifically after restoration, and adds a rationale not present in the launch-day note: retention exists because cumulative, cross-request misuse patterns can't be caught by real-time filtering alone. For practitioners in regulated environments who need ZDR, this is a hard architectural constraint: Fable 5 on AI Gateway cannot be used with a no-retention compliance posture, regardless of fallback configuration, since the retention policy applies independently of which model in the fallback chain actually serves the request.

## Concrete Artifacts

### Verbatim article text (extracted via direct HTML fetch + BeautifulSoup `<article>` isolation, not WebFetch summarization)

```
Access to Claude Fable 5, the Mythos-class model, has now been restored
on AI Gateway following the US Government's decision to lift the export
controls.

Fable 5 is the same model that was available between June 9 and June 12.
What has changed is the safety classifiers, which are now updated and
more robust.

In the near term, some routine tasks such as coding and debugging may
trigger safety classifiers. To ensure requests are still serviced when
the safety classifiers are triggered, use model fallbacks. AI Gateway
will try each model in models in the stated order if Anthropic refuses
the request to Fable 5.

To call Fable 5, use model name anthropic/claude-fable-5:

[code example — see below]

Call Fable 5 with model fallbacks. This request will fall back to
Opus 4.8, then Sonnet 5, if the safety classifier is triggered.

Model fallbacks work on every API format: for more information on how
to configure these, see the docs.

Anthropic does not support Zero Data Retention for the model, because
some misuse patterns are only visible across cumulative requests, which
real-time filters cannot catch on their own. Prompts and completions
are retained for 30 days and are not used to train Claude. Read more in
the data retention whitepaper.

Source: https://vercel.com/changelog/claude-fable-5-access-restored-on-ai-gateway
```

### Fable 5 with model fallbacks (verbatim code example)

```typescript
import { streamText } from 'ai';

const result = streamText({
  model: 'anthropic/claude-fable-5',
  prompt: 'Summarize this quarterly report and list the key risks.',
  providerOptions: {
    gateway: {
      models: ['anthropic/claude-opus-4.8', 'anthropic/claude-sonnet-5'],
    },
  },
});
```
Source: https://vercel.com/changelog/claude-fable-5-access-restored-on-ai-gateway

### Page metadata (from page JSON-LD, verified independently of WebFetch)

```
datePublished: 2026-07-01T00:01-07:00
dateModified:  2026-07-02T06:14:39.210Z
author: Jerilyn Zheng, jobTitle "Product, AI Gateway"
description: "Access to Claude Fable 5, the Mythos-class model, has now
  been restored on AI Gateway following the US Government's decision to
  lift the export control directive."
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-claude-fable-5.md` and `blog-simonwillison-fable-mythos-access-directive.md`: this source's Claim 2 independently confirms the June 9 launch / June 12 suspension dates already established in this corpus's Fable 5 timeline.
  - `blog-latentspace-ainews-fable-relaunch-orchestration.md` Claim 1: this source's Claims 2 and 3 corroborate that note's "updated cybersecurity safeguards may route some requests to Opus 4.8" framing, independently confirming the Opus 4.8 fallback mechanism and adding the specific "coding and debugging" trigger detail that note did not have.
  - `blog-simonwillison-fable-silent-interventions.md` Claim 6 ("Anthropic reversed the silent intervention policy... changing to visible safeguards that fall back to Opus 4.8"): this source's Claim 4 is the first concrete, runnable configuration example of exactly that visible-fallback-to-Opus-4.8 mechanism the earlier note only described in prose.
  - `blog-latentspace-fable-5-mythos-launch.md` ("We will require 30-day retention for all traffic on Mythos-class models"): this source's Claim 6 confirms the same 30-day, no-training retention policy still applies to Fable 5 after restoration, and adds Anthropic's stated rationale (cumulative misuse-pattern detection).

- **Contradicts**: None identified. All claims here are consistent with, and add detail to, the existing Fable 5 export-control/restoration timeline in this corpus.

- **Extends**:
  - `blog-latentspace-ainews-fable-relaunch-orchestration.md` Claim 2, which explicitly flagged the causal link between the July 1 relaunch and the June 12 export-control directive as an unconfirmed Miner inference and recommended a future Miner locate a more direct restoration announcement. This source's Claim 1 is the closest documentation in the corpus so far to that recommendation — a first-party platform statement making the same causal claim explicitly — though it is Vercel's statement about AI Gateway access, not Anthropic's own restoration announcement, so the gap that note flagged is narrowed but not fully closed.
  - `blog-vercel-ai-gateway-api-key-budgets.md`, `blog-vercel-ai-gateway-realtime-voice-speech.md`, and `blog-vercel-ai-gateway-xai-grok-audio-models.md`: extends this corpus's documentation of AI Gateway's model-fallback and reliability configuration surface to a safety-classifier-triggered use case specifically, rather than a capacity/outage/modality-availability one.

- **Novel**:
  - **The exact `providerOptions.gateway.models` fallback chain for Fable 5** (Claim 4): no prior corpus source shows the specific AI SDK configuration syntax for routing around Fable 5 safety-classifier refusals.
  - **"Coding and debugging" named explicitly as a routine-task category expected to trigger safety classifiers** (Claim 3): more specific than the "biology/chemistry classifiers still overly broad" framing in `blog-latentspace-ainews-fable-relaunch-orchestration.md`, which named a different trigger-prone domain.
  - **Stated rationale for withholding Zero Data Retention** (Claim 6): "some misuse patterns are only visible across cumulative requests, which real-time filters cannot catch on their own" is not present in any prior Fable 5/Mythos data-retention source note in this corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the `providerOptions.gateway.models` fallback pattern (Claim 4, Concrete Artifacts) as a concrete reference implementation for teams building coding/debugging agents on Fable 5 — the guide should recommend configuring an explicit fallback chain (e.g., Opus 4.8, then Sonnet 5) as standard practice for this model given Vercel's own guidance that routine coding and debugging tasks may trigger safety-classifier refusals (Claim 3), not as a defensive measure for rare edge cases.

- **Chapter 06 (Security & Threat Model)**: Add Claim 6's Zero Data Retention gap as a compliance constraint: teams with a no-retention requirement cannot use Fable 5 on AI Gateway (or, by extension, its fallback chain when Fable 5 itself is used) — the 30-day, no-training retention applies regardless of which model in the chain serves the request. Cite alongside `blog-latentspace-fable-5-mythos-launch.md`'s launch-day retention statement as two independent confirmations of the same durable constraint.

## Extraction Notes

1. **WebFetch quotes did not match verbatim on first two passes.** Two separate WebFetch calls against this URL returned paraphrased text that differed from each other in exact wording for the same passages (e.g., "routine tasks such as coding and debugging may trigger safety classifiers" vs. "some routine tasks such as coding and debugging may trigger safety classifiers"; differing renderings of the data-retention rationale sentence). Per MINER.md §2a and the precedent in `blog-vercel-ai-gateway-xai-grok-audio-models.md` Extraction Notes, the page was instead fetched directly via `curl` with a browser user-agent, the `<article>` element isolated with BeautifulSoup, and every `Quote` field above located character-for-character in that locally-parsed text.
2. **Author and dates verified against the page's own JSON-LD**, not inferred from a WebFetch summary — `datePublished`, `dateModified`, and the `author` object were extracted directly from a `<script type="application/ld+json">` embedded in the fetched HTML.
3. **No linked pages followed beyond the primary changelog.** The changelog links to a general "docs" page for fallback configuration and a "data retention whitepaper," both referenced generically rather than as substantive sub-pages central to understanding this changelog's own claims; per MINER.md §1, this short, self-contained entry did not require following them.
4. **Three duplicate Prospector triage comments** appeared on issue #2364 with inconsistent novelty assessments (high, then low, then low) and different relevant-chapter lists — a known corpus pattern from automated re-triage runs, also documented in `blog-vercel-ai-gateway-xai-grok-audio-models.md` and `blog-simonwillison-fable-5-permanent.md` Extraction Notes. Following the precedent set in those notes, I treated the third (most detailed) comment as the most informative for chapter targeting but formed my own chapter recommendations (Guide Impact, above) from the actual extracted claims rather than any single triage comment's chapter list, since none of the three fully matched the content once read.
5. **Confidence calibration: emerging.** Individual claims are largely "settled" (first-party platform statements and runnable code), but overall confidence is "emerging" because: (a) this is a single vendor-adjacent platform's brief changelog, not Anthropic's own restoration announcement, so Claim 1's causal link between this restoration and the export-control lift — while now stated explicitly by a first party — is still not confirmed by Anthropic directly; (b) the source is narrow in scope (no pricing, no full trigger taxonomy, no technical detail on what changed in the "more robust" classifiers); (c) this matches both the Prospector's own "thin evidence" characterization and my own reading of the source.
