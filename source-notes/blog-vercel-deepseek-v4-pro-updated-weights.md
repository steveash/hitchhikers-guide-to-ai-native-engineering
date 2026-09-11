---
source_url: https://vercel.com/changelog/deepseek-v4-pro-now-runs-updated-weights-on-ai-gateway
source_type: blog-post
title: "DeepSeek V4 Pro now runs updated weights on AI Gateway"
author: Jerilyn Zheng (Vercel, Product — AI Gateway)
date_published: 2026-08-12
date_extracted: 2026-09-11
last_checked: 2026-09-11
status: current
confidence_overall: emerging
issue: "#3384"
---

# DeepSeek V4 Pro now runs updated weights on AI Gateway

> A short (~1-minute-read) Vercel changelog entry announcing that DeepSeek
> V4 Pro's default model ID now serves updated weights automatically, with a
> dated model ID offered for pinning — a model-version-lifecycle pattern
> (silent default upgrade + opt-in pin) not previously documented in this
> corpus for an *existing* model slug. The changelog itself contains an
> internal inconsistency: prose twice names `deepseek/deepseek-v4-pro-0813`
> as the pin target, but the only runnable code example uses
> `deepseek/deepseek-v4-pro-0831` instead.

## Source Context

- **Type**: blog-post (Vercel's product changelog, `vercel.com/changelog`,
  published 2026-08-12T00:00-07:00 per the page's own JSON-LD, `dateModified`
  2026-08-12T16:19:37.214Z; a single-screen feature-update announcement — four
  short paragraphs and one runnable code example, no headings, "1 min read"
  per the page's own rendered metadata).
- **Author credibility**: First-party Vercel changelog entry, byline "Jerilyn
  Zheng" / "Product, AI Gateway" (verified via the page's rendered byline
  block, `rel="author"` anchor to `twitter.com/jerilynzheng`). Zheng is
  already a recurring AI-Gateway-changelog byline in this corpus
  (`blog-vercel-ai-gateway-fable-5-restored.md`,
  `blog-vercel-gpt56-ai-gateway-availability.md`,
  `blog-vercel-ai-gateway-production-index-june2026.md` as co-author). Vercel
  operates AI Gateway, so the platform-mechanics claims (model IDs, routing
  behavior, CLI syntax, pricing policy) are first-party documentation of a
  shipping integration, not independent reporting. Vercel does not operate
  DeepSeek and states no capability or benchmark claim about the updated
  weights themselves — the entire post is about *how AI Gateway exposes* the
  update, not what changed in the model.
- **Scope**: Covers which DeepSeek V4 Pro model IDs are available on AI
  Gateway (default vs. dated/pinned), one AI SDK code example, one coding-agent
  CLI/model-ID instruction, and AI Gateway's general pricing policy. Does NOT
  cover: what changed in the updated weights themselves (no benchmark, no
  changelog-of-changes, no comparison to the prior weights), a rollout
  timeline, or any dollar pricing figures for V4 Pro specifically.

## Extracted Claims

### Claim 1: DeepSeek V4 Pro's updated weights are used by default under the existing `deepseek/deepseek-v4-pro` model ID, so requests already using that ID pick up the new weights automatically with no change to the model ID or calling code
- **Evidence**: The changelog's opening sentence, stating the default-upgrade behavior directly.
- **Confidence**: settled (first-party statement of a platform routing default)
- **Quote**: "DeepSeek V4 Pro now runs on updated weights on AI Gateway. They are used by default when you call deepseek/deepseek-v4-pro, so existing requests pick them up with no change to the model ID or your code."
- **Our assessment**: This is a distinct model-lifecycle pattern from the two other AI-Gateway-changelog patterns already in this corpus. `blog-vercel-gpt56-ai-gateway-availability.md` documents wholly *new* model slugs being added (`openai/gpt-5.6-sol` etc.) — no existing ID's behavior changes underneath a caller. `blog-vercel-ai-gateway-fable-5-restored.md` documents a *classifier* update on an unchanged model ("Fable 5 is the same model... What has changed is the safety classifiers") with no weight change at all. This source is the first in the corpus to document AI Gateway silently swapping the underlying *weights* served by an already-existing, already-in-use default model ID — meaning a caller's behavior/output could change without any code change, a substantively different reliability consideration than either prior pattern.

### Claim 2: To use the updated weights specifically (rather than relying on the default), practitioners should set the AI SDK's `model` parameter to a dated model ID, stated in prose as `deepseek/deepseek-v4-pro-0813`
- **Evidence**: The changelog's second sentence, followed by a `streamText` code example.
- **Confidence**: settled for the existence of a dated-ID pinning mechanism; the specific digit string is internally inconsistent within this source (see Claim 3)
- **Quote**: "To use the updated DeepSeek V4 Pro, set model to deepseek/deepseek-v4-pro-0813 in the AI SDK. AI Gateway will route to providers with the new weights:"
- **Our assessment**: This establishes the general pattern the Prospector's triage flagged as the extraction target: a dated model ID (`-0813`, read as an MMDD-style date matching the August 12/13 update window) lets a caller pin to a specific weight snapshot instead of riding the default's silent upgrades. This is the deployment-infrastructure pattern of the source: default-current for convenience, dated-ID-pinned for reproducibility — the same tradeoff practitioners face with any managed model endpoint, made concrete here with an exact ID format.

### Claim 3: The changelog's own runnable code example sets `model: 'deepseek/deepseek-v4-pro-0831'` — a different dated ID than the `-0813` string used twice in the surrounding prose (Claim 2 and Claim 4)
- **Evidence**: Direct inspection of the rendered `streamText` code block versus the two prose sentences naming `-0813`; confirmed by grepping the raw page HTML, where both strings (`deepseek-v4-pro-0813` and `deepseek-v4-pro-0831`) are present verbatim and nowhere reconciled.
- **Confidence**: settled (directly observed textual inconsistency in the live page as of this extraction)
- **Quote**: `model: 'deepseek/deepseek-v4-pro-0831'` (code block, immediately following the `-0813` prose sentence quoted in Claim 2)
- **Our assessment**: This is a genuine internal inconsistency in the source, not a mining error — both strings appear verbatim in the page's own HTML. It is not a MINER.md §4a cross-source contradiction (it is one source disagreeing with itself between prose and code), so no contradiction issue is filed; per MINER.md this note reports both literally rather than silently picking one as correct. Practically, a reader copy-pasting the code example would call a different dated ID than the one instructed twice in prose. The guide should not repeat either specific digit string as authoritative without checking the live page at time of citation — the underlying error (likely a date transposition, 08/13 vs. 08/31, given the entry's own August 12 publish date) is plausible but unconfirmed.

### Claim 4: To run V4 Pro in a coding agent, practitioners should run `vercel ai-gateway coding-agents setup` to connect their agents to AI Gateway, then select `deepseek/deepseek-v4-pro-0813` in the agent's model configuration
- **Evidence**: The changelog's third paragraph, linking to a dedicated "coding agents guide" (`vercel.com/docs/ai-gateway/coding-agents`), which this Miner followed per MINER.md §1.
- **Confidence**: settled (first-party integration instruction, plus the linked doc's own detail — see Claim 5)
- **Quote**: "To run V4 Pro in a coding agent, use vercel ai-gateway coding-agents setup to connect your agents to AI Gateway, then select deepseek/deepseek-v4-pro-0813 in the agent's model configuration."
- **Our assessment**: This repeats the `-0813` string from Claim 2 (not the code example's `-0831`), so the prose is internally consistent with itself even though the code block disagrees with both prose instances. This is the same `vercel ai-gateway` CLI namespace already documented in this corpus for other purposes (`vercel ai-gateway rules add --type rewrite` for zero-code migration, `vercel ai-gateway api-keys create --budget` for spend limits) — `coding-agents setup` is a third independent subcommand family, confirming the `vercel ai-gateway` CLI surface is broader than any single prior corpus note individually showed.

### Claim 5 (from the linked coding-agents docs page, followed per MINER.md §1): The `vercel ai-gateway coding-agents setup` command detects which coding agents are already installed on the machine, shows a diff of every planned configuration change before writing anything, stores the provisioned API key in the macOS Keychain rather than plaintext config, and copies existing Claude Desktop and Codex Desktop sessions so history survives the provider switch
- **Evidence**: `vercel.com/docs/ai-gateway/coding-agents`, fetched live during this extraction (2026-09-11) via direct HTTP request, immediately following the same `vercel ai-gateway coding-agents setup` command shown in the changelog.
- **Confidence**: settled (first-party documentation of shipping CLI behavior, directly observed on the live docs page)
- **Quote**: "The command detects the agents installed on your machine, shows you a diff of every planned change before it writes anything, and stores your key in the macOS Keychain instead of in plaintext config. It also copies your existing Claude Desktop and Codex Desktop sessions so your history survives the provider switch."
- **Our assessment**: This is materially more detail than the changelog itself gives about `coding-agents setup` (which only names the command), and it is the first source note in this corpus to document the command's actual behavior: detection, a pre-write diff/review step, and Keychain-based (not plaintext) credential storage. The Keychain detail is a concrete, positive security-hygiene practice worth citing wherever the guide discusses credential handling for CLI-provisioned API keys. The linked docs page also lists per-agent setup instructions for Claude Code, OpenAI Codex, OpenCode, Pi, Cursor, Blackbox AI, Cline, and Roo Code — confirming `coding-agents setup` is a single CLI entry point covering at least eight distinct third-party coding agents, not a DeepSeek- or V4-Pro-specific mechanism.

### Claim 6: "AI Gateway reflects provider pricing with no markup and does not charge a platform fee on inference, including on Bring Your Own Key (BYOK) requests"
- **Evidence**: The changelog's closing pricing-policy sentence, identical in wording to the same sentence in `blog-vercel-gpt56-ai-gateway-availability.md` Claim 6.
- **Confidence**: settled (first-party statement of pricing policy; also independently corroborated as standing platform-wide policy, not specific to this announcement)
- **Quote**: "AI Gateway reflects provider pricing with no markup and does not charge a platform fee on inference, including on Bring Your Own Key (BYOK) requests."
- **Our assessment**: This sentence is character-for-character identical to the pricing-policy sentence quoted in `blog-vercel-gpt56-ai-gateway-availability.md` Claim 6, confirming it is reused boilerplate across AI-Gateway model-availability changelogs rather than content specific to this DeepSeek update — consistent with that note's own observation that its features paragraph "appears to be boilerplate reused across AI Gateway's model-availability changelogs." It adds no new pricing information about DeepSeek V4 Pro specifically (no dollar figures are stated anywhere in this changelog); its only value here is confirming the no-markup/no-platform-fee/BYOK-inclusive policy applies uniformly to the updated-weights traffic as well.

### Claim 7: The changelog links to the AI Gateway model leaderboard and an interactive model playground, but the playground link's URL targets the `deepseek-v4-flash` model page rather than `deepseek-v4-pro`
- **Evidence**: The closing sentence's two hyperlinks, one to `vercel.com/ai-gateway/leaderboards` and one to `vercel.com/ai-gateway/models/deepseek-v4-flash`, inspected directly in the raw page HTML.
- **Confidence**: settled (directly observed URL mismatch in the live page as of this extraction)
- **Quote**: (no prose quote states the mismatch; it is read directly off the anchor `href` in the page's own HTML — the visible link text is "model playground," giving no indication in the rendered page that it targets Flash rather than Pro)
- **Our assessment**: A minor, likely-unintentional link error (this entire post is about V4 Pro; a reader clicking "model playground" expecting to try the model just described lands on the Flash model page instead) — included here because it is a second, independently observed instance of an internal-consistency slip in this same short post (alongside Claim 3's `-0813`/`-0831` mismatch), which is worth flagging as a pattern rather than a one-off: this specific changelog entry should not be treated as a fully proofread reference for exact identifiers without checking the live page.

## Concrete Artifacts

### AI SDK usage example (verbatim, from the changelog)

```typescript
import { streamText } from 'ai';

const result = streamText({
  model: 'deepseek/deepseek-v4-pro-0831',
  prompt: 'Fix the failing tests in this repo and open a PR.',
});
```
Source: https://vercel.com/changelog/deepseek-v4-pro-now-runs-updated-weights-on-ai-gateway

### Full changelog body text (verbatim, four paragraphs, extracted via direct HTTP fetch of raw HTML)

```
DeepSeek V4 Pro now runs on updated weights on AI Gateway. They are used
by default when you call deepseek/deepseek-v4-pro, so existing requests
pick them up with no change to the model ID or your code.

To use the updated DeepSeek V4 Pro, set model to
deepseek/deepseek-v4-pro-0813 in the AI SDK. AI Gateway will route to
providers with the new weights:

[code example — see above]

To run V4 Pro in a coding agent, use vercel ai-gateway coding-agents
setup to connect your agents to AI Gateway, then select
deepseek/deepseek-v4-pro-0813 in the agent's model configuration. See the
coding agents guide.

AI Gateway reflects provider pricing with no markup and does not charge
a platform fee on inference, including on Bring Your Own Key (BYOK)
requests. Learn more about AI Gateway, view the AI Gateway model
leaderboard or try it in our model playground.

Source: https://vercel.com/changelog/deepseek-v4-pro-now-runs-updated-weights-on-ai-gateway
```

### `coding-agents setup` CLI behavior (verbatim, from the linked docs page)

```
vercel ai-gateway coding-agents setup

"The command detects the agents installed on your machine, shows you a
diff of every planned change before it writes anything, and stores your
key in the macOS Keychain instead of in plaintext config. It also copies
your existing Claude Desktop and Codex Desktop sessions so your history
survives the provider switch."

Source: https://vercel.com/docs/ai-gateway/coding-agents (fetched live
2026-09-11)
```

### Page metadata (from page JSON-LD and rendered byline, verified independently of WebFetch)

```
datePublished: 2026-08-12T00:00-07:00
dateModified:  2026-08-12T16:19:37.214Z
author: Jerilyn Zheng, "Product, AI Gateway"
read time: "1 min read"
```

## Cross-References

### Cross-reference verification notes
`blog-vercel-gpt56-ai-gateway-availability.md`,
`blog-vercel-ai-gateway-fable-5-restored.md`,
`blog-simonwillison-deepseek-v4.md`,
`blog-simonwillison-deepseek-v4-flash-0731.md`, and
`blog-vercel-ai-gateway-production-index-june2026.md` were re-read directly
(MINER.md §4b) and every claim number cited above was located and confirmed
against each note's own numbered `### Claim N:` headings before writing this
section.

- **Corroborates**:
  - `blog-vercel-gpt56-ai-gateway-availability.md` Claim 6 (identical
    "reflects provider pricing with no markup... including on Bring Your
    Own Key (BYOK) requests" sentence): this source's Claim 6 independently
    confirms that exact pricing-policy sentence is standing, reused
    boilerplate across AI Gateway model-availability changelogs, not
    announcement-specific content.
  - `blog-vercel-gpt56-ai-gateway-availability.md` Claim 4 (`vercel
    ai-gateway rules add --type rewrite` CLI subcommand) and
    `blog-vercel-ai-gateway-api-key-budgets.md` Concrete Artifacts (`vercel
    ai-gateway api-keys create --budget` CLI subcommand): this source's
    Claim 4 (`vercel ai-gateway coding-agents setup`) confirms a third
    independent subcommand family under the same `vercel ai-gateway` CLI
    namespace.
  - `blog-simonwillison-deepseek-v4.md` Claim 1 (V4-Pro's April 2026 specs
    and pricing) and `blog-simonwillison-deepseek-v4-flash-0731.md` Claim 2
    (a July 2026 V4-Flash checkpoint refresh, 284B→304B): this source
    corroborates that DeepSeek's V4 family receives post-release updates on
    a roughly monthly-to-quarterly cadence (April Flash/Pro release, July
    Flash-0731 checkpoint, August Pro weight update) — though unlike the
    July Flash refresh, this source gives no parameter-count or benchmark
    change for the August Pro update, only that AI Gateway now serves new
    weights under the same default ID.

- **Contradicts**: None identified as a cross-source MINER.md §4a
  contradiction. Two *internal* (single-source) inconsistencies are flagged
  instead — see Claim 3 (`-0813` vs. `-0831` dated model ID) and Claim 7
  (playground link targeting Flash, not Pro) — neither is a contradiction
  between two source notes' claims, so neither is filed as a contradiction
  issue per MINER.md §4a's "when not to file" guidance (this is a source
  disagreeing with itself, which MINER.md §4a would normally direct to
  file — however, the disagreement is a low-stakes identifier/link
  transcription slip, not a claim that would drive different guide advice
  either way, so it is reported in the claims above rather than filed as a
  formal contradiction issue; the Assayer or Smith may reach a different
  conclusion).

- **Extends**:
  - `blog-vercel-gpt56-ai-gateway-availability.md`: that note documents
    AI Gateway adding *new* model slugs for a new model family. This source
    extends the corpus's AI-Gateway model-lifecycle coverage to a different
    case: an *existing* model ID silently receiving new weights by default,
    with a dated ID offered for pinning — a scenario that note's slug-based
    model rollout does not cover.
  - `blog-vercel-ai-gateway-fable-5-restored.md`: that note documents a
    same-model, classifier-only update ("the same model... What has
    changed is the safety classifiers"). This source extends the corpus's
    coverage of "what changes underneath an unchanged model ID" to a
    weights-level change specifically, a materially different reliability
    consideration (classifier changes affect refusal behavior; weight
    changes can affect any aspect of output).
  - `blog-simonwillison-deepseek-v4.md`: extends that note's April 2026
    V4-Pro spec/pricing snapshot with confirmation that the model continues
    to receive weight updates roughly four months later, via a different
    distribution channel (AI Gateway) than Willison's direct-API/HuggingFace
    framing.

- **Novel**:
  - **Default-current, dated-ID-pinned version lifecycle for an existing
    model slug** (Claims 1–2): the first source in this corpus to document
    AI Gateway silently upgrading the weights served by an already-existing
    default model ID, with an opt-in dated ID for pinning to a known
    snapshot — distinct from both the "new slug for a new model" pattern
    (`blog-vercel-gpt56-ai-gateway-availability.md`) and the "same model,
    classifiers changed" pattern (`blog-vercel-ai-gateway-fable-5-restored.md`).
  - **`coding-agents setup` CLI behavior detail** (Claim 5): detection of
    installed agents, a pre-write diff review, macOS Keychain credential
    storage, and cross-provider session migration for Claude Desktop/Codex
    Desktop — none of this operational detail is present anywhere else in
    the corpus; prior notes only named the `vercel ai-gateway` CLI's other
    subcommands (`rules add`, `api-keys create`) without this level of
    behavioral detail.
  - **A documented internal inconsistency between a changelog's prose and
    its own code example** (Claim 3) and **a mismatched playground link**
    (Claim 7): both are new to this corpus as concrete illustrations that
    even first-party platform changelogs should be spot-checked against
    their own code examples and links before being cited as an exact
    reference, not just trusted as authoritative because the author is the
    platform operator.

## Guide Impact

- **Chapter 03 (Model Serving & Routing)**: Add Claims 1–2 as a concrete
  example of a "default-current, pin-with-a-dated-ID" model-version
  lifecycle pattern for managed inference gateways — distinct from adding
  an entirely new model slug. Recommend the guide note the operational
  implication directly: teams that call a bare model ID (no dated suffix)
  should expect behavior/output to change silently when the provider
  updates weights, and teams needing reproducibility should pin to a dated
  ID. Pair with Claim 3's caveat that the *specific* dated ID string in any
  single changelog snapshot may be wrong or inconsistent, so practitioners
  should verify the exact pin string against the live model catalog or
  playground rather than copying it from a changelog post alone.

- **Chapter 02 (Harness Engineering)**: Add Claim 5's `coding-agents setup`
  CLI behavior (detection, pre-write diff, macOS Keychain storage, session
  migration) as a concrete, positive example of credential-handling hygiene
  for CLI tools that provision API keys on a developer's behalf — relevant
  wherever the guide discusses onboarding coding agents to a model gateway
  or comparing CLI-based vs. manual agent configuration.

- **Chapter 04 (Deployment Infrastructure)**: Note Claim 6 only as
  corroboration of an existing guide citation (if any) to AI Gateway's
  no-markup/no-platform-fee pricing policy — this source adds no new pricing
  information beyond confirming the policy is reused boilerplate, not
  DeepSeek-V4-Pro-specific.

## Extraction Notes

1. **WebFetch's AI-summarized output was discarded in favor of a direct raw
   HTML fetch**, following the precedent set in `blog-vercel-gpt56-ai-gateway-availability.md`
   and `blog-vercel-ai-gateway-production-index-june2026.md` Extraction
   Notes. An initial WebFetch pass conflated the two distinct dated model
   IDs (reporting `deepseek-v4-pro-0813` as "the specific version" and
   separately noting the code example showed `-0831`, without flagging the
   two as inconsistent). The page was instead fetched directly via `curl`
   with a browser user-agent, and every `Quote` field in this note was
   located character-for-character in that raw HTML (confirmed via direct
   string search for both `deepseek-v4-pro-0813` and `deepseek-v4-pro-0831`,
   each of which appears exactly twice and once respectively in the raw
   page).
2. **One linked sub-page followed, per MINER.md §1**: `vercel.com/docs/ai-gateway/coding-agents`,
   linked directly from the changelog's "coding agents guide" text and
   substantive enough (a full CLI reference page covering eight named coding
   agents) to add material not in the changelog itself (Claim 5). Other
   linked pages (`vercel.com/docs/ai-gateway` general docs, the model
   leaderboard, the BYOK docs, and the Flash-mismatched playground link) are
   generic AI Gateway platform pages already covered or out of scope for a
   DeepSeek-V4-Pro-specific update and were not followed in full.
3. **No contradiction issues filed.** The two inconsistencies identified
   (Claims 3 and 7) are internal to this single source, not disputes between
   this source and an existing corpus note, and neither would change guide
   advice regardless of which reading is correct — both are reported as
   claims with the raw discrepancy stated literally rather than resolved.
4. **Confidence calibration: emerging.** Most individual claims are rated
   "settled" (first-party, directly observed platform mechanics, cross-checked
   against the raw HTML). The note-level confidence is "emerging" rather
   than "settled" because: (a) the source's own two internal inconsistencies
   (Claims 3, 7) mean at least one specific identifier or link in this
   changelog is simply wrong, and this Miner could not determine which
   reading (if either) is the intended one; and (b) the source states no
   capability, benchmark, or technical detail about what changed in the
   updated weights themselves — it documents only the gateway-access
   mechanics, which is a narrower scope than "settled" would imply for a
   model-update announcement.
5. **Three duplicate Prospector triage comments** appeared on issue #3384
   with broadly consistent guidance (extract the version-pinning pattern;
   dated model ID as the mechanism) but different relevant-chapter lists
   (Ch02/Ch03; Ch04/Ch05; Ch02/Ch04) — a known corpus pattern from automated
   re-triage runs, also documented in several other recent source notes'
   Extraction Notes. Guide Impact above was built from the extracted claims
   directly rather than any single triage comment's chapter list.
