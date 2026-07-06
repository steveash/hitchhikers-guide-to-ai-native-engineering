---
source_url: https://simonwillison.net/2026/Jun/30/claude-sonnet-5/
source_type: blog-post
title: "What's new in Claude Sonnet 5"
author: Simon Willison
date_published: 2026-06-30
date_extracted: 2026-07-06
last_checked: 2026-07-06
status: current
confidence_overall: settled
issue: "#1573"
---

# What's new in Claude Sonnet 5

> Simon Willison's launch-day link-post on Claude Sonnet 5 relays Anthropic's official "what's new" developer docs and system card, and adds first-party token-count measurements showing the new tokenizer produces roughly 1.4x more tokens for English text — turning a nominally unchanged price list into an effective ~30-40% cost increase depending on content language.

## Source Context

- **Type**: blog-post (Simon Willison link-blog format, June 30, 2026; ~350 words
  of original commentary plus a blockquote from Anthropic's system card and a
  results table from Willison's own tokenizer testing). This is a "link post" —
  Willison's stated practice, per the post itself, is to go "straight to the
  'what's new' developer docs because they tend to have more actionable
  information than the official announcement post." The primary technical
  content of the post is drawn from and quotes Anthropic's official "What's new
  in Claude Sonnet 5" docs page
  (`https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5`),
  which this Miner also fetched directly and treats as part of the source per
  MINER.md §1 (a linked page that is substantive and central to the post's own
  content).
- **Author credibility**: Simon Willison is the creator of Django and the `llm`
  CLI, and one of the most widely-cited practitioner commentators on LLM
  tooling; a `trusted-feed` source in this repo's scanning configuration. He is
  authoritative for: relaying and correctly summarizing Anthropic's own
  published documentation, and for his own first-party tokenizer measurements
  (produced with his own publicly available Claude Token Counter tool). He is
  not an Anthropic employee and the capability/pricing claims he relays
  originate from Anthropic, not from independent benchmarking by Willison.
- **Scope**: Covers Sonnet 5's API-visible changes (removed sampling
  parameters, adaptive thinking default, new tokenizer, context window,
  pricing), a system-card excerpt on cybersecurity safeguards relative to
  Mythos 5, and Willison's own tokenizer-inflation measurements across four
  documents in four languages/formats. Does NOT cover: independent capability
  benchmarks (no benchmark scores are given, only Anthropic's qualitative
  "close to Opus 4.8" framing), enterprise/platform availability details
  (covered instead by the official docs page, which this note also draws on),
  or third-party reception/discussion (the post links an HN thread but does not
  discuss its contents).

## Extracted Claims

### Claim 1: Claude Sonnet 5 is a drop-in upgrade for Claude Sonnet 4.6 with exactly three behavior changes: adaptive thinking on by default, manual extended thinking now returns a 400 error, and setting sampling parameters to non-default values returns a 400 error
- **Evidence**: Anthropic's official "What's new in Claude Sonnet 5" docs page, opening summary paragraph, fetched directly by this Miner.
- **Confidence**: settled (official vendor documentation, primary source for the model's own migration contract)
- **Quote**: "Claude Sonnet 5 is the next generation of Anthropic's Sonnet model family. It is a drop-in upgrade for Claude Sonnet 4.6 with three behavior changes: adaptive thinking is on by default, manual extended thinking now returns a 400 error (it was deprecated on Claude Sonnet 4.6), and setting sampling parameters (temperature, top_p, top_k) to non-default values returns a 400 error."
- **Our assessment**: This is the single most load-bearing sentence for migration planning — it explicitly scopes the *entire* set of behavior changes to three items, which practitioners can treat as a complete checklist rather than needing to hunt for undocumented differences. The docs page frames these as "behavior changes" distinct from the tokenizer change (Claim 2), which it explicitly says is "not an API change."

### Claim 2: Claude Sonnet 5 uses a new tokenizer that produces approximately 30% more tokens than Sonnet 4.6 for the same input text, and this is explicitly not an API change (same request/response shapes, no code changes required)
- **Evidence**: Official docs page, "New tokenizer" section, fetched directly.
- **Confidence**: settled (official vendor documentation, stated as a direct product fact)
- **Quote**: "Claude Sonnet 5 uses a new tokenizer. The same input text produces approximately 30% more tokens than on Claude Sonnet 4.6. The exact increase depends on the content. This is not an API change: requests, responses, and streaming events keep the same shape, and no code changes are required."
- **Our assessment**: The "not an API change" framing is important and easy to miss: nothing breaks mechanically, so a migration could appear to succeed with no errors while silently costing more per request and truncating outputs closer to `max_tokens` limits than before. This is a "silent" cost/behavior change rather than a "loud" one — the API changes in Claim 1 are loud (they 400 immediately); the tokenizer change is not. Practitioners relying on error-driven migration testing will not catch this change; they must proactively recount tokens.

### Claim 3: Willison's own tokenizer testing (via his Claude Token Counter tool) found the new tokenizer produces roughly 1.4x more tokens for English text, 1.33x for Spanish, 1.27–1.28x for Python code, and effectively no change (1.01x) for Simplified Mandarin
- **Evidence**: Willison's first-party measurement using his own publicly available tool, tested against four documents: the Universal Declaration of Human Rights in English, Spanish, and Simplified Mandarin, and the Python source file `sqlite_utils/db.py` (4,279 lines).
- **Confidence**: settled (first-party, reproducible measurement against named documents with exact token counts given)
- **Quote**: "So the new token is roughly 1.4x times more expensive for English, 1.33x for Spanish, 1.28x for Python code and effectively the same cost for Simplified Mandarin."
- **Our assessment**: This is the most practically important data point in the post for cost modeling, and it directly refines Claim 2's generic "~30%" figure into a per-language/per-format multiplier table. It shows the effective price increase is not uniform: English-heavy prompts and codebases see the largest token inflation (and thus the largest effective cost increase), while Mandarin content is barely affected. Practitioners with multilingual or non-English-dominant workloads should not assume the ~30% headline figure applies uniformly to their own token budgets — they should re-measure against their own representative content, exactly as Willison did.

### Claim 4: Setting sampling parameters (`temperature`, `top_p`, `top_k`) to a non-default value on Claude Sonnet 5 returns a 400 error; this constraint is new for Sonnet-class models but was already introduced on Claude Opus 4.7
- **Evidence**: Official docs page, "Sampling parameters not accepted" section, fetched directly.
- **Confidence**: settled (official vendor documentation)
- **Quote**: "Setting temperature, top_p, or top_k to a non-default value returns a 400 error. Remove these parameters when migrating; the default value (or omitting the parameter) is accepted. Use system-prompt instructions to guide model behavior. This is new for Sonnet-class models; the same constraint was previously introduced on Claude Opus 4.7."
- **Our assessment**: The docs page's own framing ("new for Sonnet-class models... previously introduced on Claude Opus 4.7") establishes this as a cross-tier rollout pattern, not a Sonnet-5-specific decision — Anthropic is progressively removing sampling-parameter control across its model lineup, tier by tier. Practitioners with harnesses that set `temperature` for determinism or creativity tuning across multiple Claude tiers should expect this same 400-error behavior to eventually reach any remaining tier still accepting these parameters.

### Claim 5: Manual extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) is removed on Claude Sonnet 5 and returns a 400 error; practitioners should migrate to adaptive thinking with the effort parameter instead
- **Evidence**: Official docs page, "Manual extended thinking removed" section, including a Python code comparison, fetched directly.
- **Confidence**: settled (official vendor documentation, with a direct migration code example)
- **Quote**: "Manual extended thinking (thinking: {type: \"enabled\", budget_tokens: N}) was deprecated on Claude Sonnet 4.6; on Claude Sonnet 5 it is removed and returns a 400 error, the same as on Claude Opus 4.8 and Claude Opus 4.7."
- **Our assessment**: This confirms manual `budget_tokens`-style thinking control is now removed across Sonnet 5, Opus 4.8, and Opus 4.7 — i.e., across Anthropic's current frontier and mid-tier lineup as of this post. Any harness still setting `budget_tokens` explicitly (rather than relying on adaptive thinking or the effort parameter) will now fail hard with a 400 on Sonnet 5, not silently degrade.

### Claim 6: Claude Sonnet 5 supports a 1 million token context window as both the default and the maximum (there is no smaller context variant) and 128,000 maximum output tokens
- **Evidence**: Official docs page, model summary table and "New model" section, fetched directly; corroborated by Willison's blog post restating the same figures.
- **Confidence**: settled (official vendor documentation, specific numeric specs)
- **Quote**: "It has a 1 million token context window and 128,000 maximum output tokens."
- **Our assessment**: The docs page's clarification that "1M tokens is both the default and the maximum; there is no smaller context variant" is a meaningful simplification relative to prior Claude releases that offered separate smaller-context and 1M-context variants or tiers — practitioners no longer need to select a context-window size for Sonnet 5. Combined with Claim 2 (tokenizer inflation), the *effective* text capacity of that 1M-token window is smaller than Sonnet 4.6's 1M-token window for the same content, even though the token count itself is unchanged.

### Claim 7: Claude Sonnet 5 pricing is nominally unchanged from Sonnet 4.6 at $3 per million input tokens and $15 per million output tokens, with an introductory discount of $2/$10 per million tokens in effect through August 31, 2026 — but because the new tokenizer produces more tokens for the same text, the effective cost of an equivalent request can differ from Sonnet 4.6
- **Evidence**: Official docs page "Pricing" section, and Willison's blog post restating the same figures with the discount end date.
- **Confidence**: settled (official vendor documentation)
- **Quote**: "Claude Sonnet 5 is priced at $3 per million input tokens and $15 per million output tokens, unchanged from Claude Sonnet 4.6. Because the new tokenizer produces approximately 30% more tokens for the same text, the cost of an equivalent request can differ from Claude Sonnet 4.6 even though per-token pricing is unchanged."
- **Our assessment**: This is Anthropic's own docs page explicitly naming the phenomenon Willison's headline implies: identical *nominal* per-token pricing plus a ~30% token-count increase equals a real cost increase for the same workload. Note Willison's blog post itself renders this pricing line with an apparent typo — "$3/million input, $15/million input" (both labeled "input") — where the official docs page correctly states $15/million *output* tokens; this note relies on the official docs page wording for the corrected figure. Practitioners should budget using effective (post-tokenizer) cost per request, not list price per token, when comparing Sonnet 5 to Sonnet 4.6.

### Claim 8: Claude Sonnet 5 is the first Sonnet-tier model with real-time cybersecurity safeguards, and refusals triggered by those safeguards return as a successful HTTP 200 response with `stop_reason: "refusal"`, not an error
- **Evidence**: Official docs page, "Cybersecurity safeguards" section, fetched directly.
- **Confidence**: settled (official vendor documentation)
- **Quote**: "Claude Sonnet 5 is the first Sonnet-tier model with real-time cybersecurity safeguards. Requests that involve prohibited or high-risk cybersecurity topics may be refused. Refusals return as a successful HTTP 200 response with stop_reason: \"refusal\", not an error."
- **Our assessment**: The HTTP-200-not-error behavior is an important integration detail: harnesses that treat non-200 responses as the only failure signal will not detect a cybersecurity-safeguard refusal unless they explicitly check `stop_reason`. This is a new capability tier boundary crossing down from Opus-class models into Sonnet-class for the first time, per this source.

### Claim 9: Anthropic's Sonnet 5 system card states Sonnet 5 is "significantly less capable at cyber tasks than Mythos 5," and its safety safeguards are accordingly similar to those applied to Opus 4.7 and Opus 4.8 rather than to Mythos 5
- **Evidence**: Blockquote from Anthropic's Sonnet 5 system card PDF, quoted directly in Willison's post, which Willison presents as explaining "how they were able to release the model without being blocked by the US government."
- **Confidence**: settled (direct quote from Anthropic's own system card, as relayed and verified in Willison's post)
- **Quote**: "Sonnet 5 is significantly less capable at cyber tasks than Mythos 5: its safeguards are thus similar to those we apply to Opus 4.7 and Opus 4.8 (models that are more capable than Sonnet 5 but much less capable than Mythos 5)."
- **Our assessment**: This directly connects Sonnet 5's release to the Mythos-class capability/export-control saga already documented in this corpus (`blog-simonwillison-claude-fable-5.md`, `blog-simonwillison-fable-5-export-controls.md`, `blog-simonwillison-fable-mythos-access-directive.md`, `blog-latentspace-fable-5-mythos-launch.md`). Anthropic is explicitly using a comparative capability ranking (Sonnet 5 < Opus 4.7/4.8 < Mythos 5, on cyber tasks specifically) to justify a lighter safeguard regime for Sonnet 5 than for Mythos-class models — and, by implication, to justify releasing Sonnet 5 without triggering the same export-control scrutiny that affected Fable 5/Mythos 5. Willison's own framing ("helps explain how they were able to release the model without being blocked by the US government") is his editorial interpretation of why Anthropic included this comparison in the system card, not a claim Anthropic states directly in the quoted passage itself.

### Claim 10: Anthropic states Sonnet 5's performance "is close to that of Opus 4.8, but at lower prices," and the largest capability gains over Sonnet 4.6 are in coding and agentic tasks
- **Evidence**: Willison's post quotes Anthropic directly on relative performance; the official docs page separately states the gains are concentrated in coding/agentic tasks.
- **Confidence**: settled for the quote itself as a vendor claim; **anecdotal** for whether the claim holds up in practice — no benchmark numbers are given in either the blog post or the docs page to substantiate it.
- **Quote**: "its performance is close to that of Opus 4.8, but at lower prices"
- **Our assessment**: Neither this post nor the docs page cited within it provides benchmark evidence for the "close to Opus 4.8" claim — the docs page instead defers to "Anthropic's Transparency Hub" for benchmark results, which is out of scope for this note. This should be treated as a vendor capability claim pending independent verification, not a settled fact, and flagged accordingly if cited in the guide (consistent with how `docs-github-copilot-sonnet5-ga.md` Claim 2 flags GitHub's own "strong results" framing as vendor-asserted).

### Claim 11: Claude Sonnet 5 has the same set of tools and platform features as Claude Sonnet 4.6, except Priority Tier, which is not available on Claude Sonnet 5
- **Evidence**: Official docs page, model summary table, fetched directly; corroborated by Willison's blog post ("the same set of tools and platform features as Claude Sonnet 4.6").
- **Confidence**: settled (official vendor documentation)
- **Quote**: "Claude Sonnet 5 supports the 1M token context window by default (1M tokens is both the default and the maximum; there is no smaller context variant), 128k max output tokens, adaptive thinking, and the same set of tools and platform features as Claude Sonnet 4.6, except Priority Tier, which is not available on Claude Sonnet 5."
- **Our assessment**: The Priority Tier exclusion is a specific, actionable gap for practitioners who depend on Priority Tier for latency-sensitive production workloads — they cannot get Priority Tier access by upgrading to Sonnet 5 at launch, unlike every other platform feature that carries over unchanged.

### Claim 12: At launch, Claude Sonnet 5 is available via the Claude API to all customers, on AWS (Claude in Amazon Bedrock and Claude Platform on AWS, but explicitly not the legacy Amazon Bedrock InvokeModel/Converse APIs), on Google Cloud, and on Microsoft Foundry, and supports zero data retention (ZDR) for organizations with ZDR agreements
- **Evidence**: Official docs page, "Availability" section, fetched directly.
- **Confidence**: settled (official vendor documentation)
- **Quote**: "Claude Sonnet 5 is not available on Claude on Amazon Bedrock (legacy) (the InvokeModel and Converse APIs)."
- **Our assessment**: This is a specific, narrow gap worth flagging for practitioners on AWS: the exclusion applies only to the *legacy* Bedrock APIs, not to Bedrock generally — teams already migrated to the current Claude Platform on AWS integration are unaffected, but teams still on the legacy InvokeModel/Converse integration path cannot access Sonnet 5 without migrating first. This corroborates the general ZDR availability already documented for the Sonnet tier in GitHub Copilot specifically (`docs-github-copilot-sonnet5-ga.md` Claim 9: "Like other Sonnet models in GitHub Copilot, Claude Sonnet 5 operates under Zero Data Retention (ZDR)"), extending it to direct API/cloud-platform access rather than only the Copilot integration.

### Claim 13: Willison's informal "pelican riding a bicycle" SVG benchmark judged Sonnet 5's output unremarkable, and the model itself misidentified its own drawing as a goose rather than a pelican
- **Evidence**: Willison's own generated SVG test and his direct observation of the model's self-assessment.
- **Confidence**: anecdotal (a single informal, non-standardized test by one practitioner)
- **Quote**: "It's nothing to write home about. Sonnet 5 thinks it looks like a goose."
- **Our assessment**: This is Willison's long-running informal cross-model capability spot-check (referenced via the `pelican-riding-a-bicycle` tag corroborated in `blog-simonwillison-gemini35-flash-pricing.md`'s Source Context), not a rigorous benchmark. It is included here for completeness per MINER.md's "extract every interesting claim" guidance, but should not be cited in the guide as evidence of Sonnet 5's visual/SVG-generation capability beyond "one practitioner found it unremarkable and the model misjudged its own output."

## Concrete Artifacts

### Token count comparison table (Willison's own testing, via his Claude Token Counter tool)

```
Document                                          Sonnet 4.6   Opus 4.7          Sonnet 5
Universal Declaration of Human Rights (English)   2,356        3,347 (1.42x)     3,341 (1.42x)
Universal Declaration of Human Rights (Spanish)   3,572        4,753 (1.33x)     4,747 (1.33x)
Universal Declaration of Human Rights
  (Chinese, Mandarin Simplified)                  3,334        3,366 (1.01x)     3,360 (1.01x)
sqlite_utils/db.py (4,279 lines of Python)        44,014       56,118 (1.28x)    56,113 (1.27x)

Source: Simon Willison, simonwillison.net/2026/Jun/30/claude-sonnet-5/, June 30, 2026,
using his Claude Token Counter tool (tools.simonwillison.net/claude-token-counter)
```

### Migration guide code snippet (from Anthropic's official docs page)

```python
# Not supported on Claude Sonnet 5 (returns 400)
thinking = {"type": "enabled", "budget_tokens": 32000}

# Use this instead
thinking = {"type": "adaptive"}
```

```python
# Update your model ID:
model = "claude-sonnet-4-6"  # Before
model = "claude-sonnet-5"    # After
```

```
Source: Anthropic, "What's new in Claude Sonnet 5" docs page,
platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5
```

### System card excerpt on comparative cyber-task capability (quoted in Willison's post)

```
"Sonnet 5 is significantly less capable at cyber tasks than Mythos 5: its
safeguards are thus similar to those we apply to Opus 4.7 and Opus 4.8 (models
that are more capable than Sonnet 5 but much less capable than Mythos 5)."

Source: Claude Sonnet 5 System Card (Anthropic), quoted in Simon Willison,
simonwillison.net/2026/Jun/30/claude-sonnet-5/, June 30, 2026
```

## Cross-References

- **Corroborates**:
  - `docs-github-copilot-sonnet5-ga.md` Claim 9 (Sonnet 5 operates under Zero
    Data Retention "like other Sonnet models" in GitHub Copilot): Claim 12 of
    this note independently confirms ZDR support for Sonnet 5 at the direct
    API/cloud-platform level (Anthropic's own docs page), extending the ZDR
    claim from a Copilot-specific integration detail to a platform-wide model
    property.
  - `docs-github-copilot-sonnet5-ga.md` Claim 1 (Sonnet 5 positioned as
    Anthropic's latest Sonnet-class model): Claim 1 of this note independently
    confirms the same release, sourced directly from Anthropic rather than
    relayed through GitHub's changelog.
  - `blog-simonwillison-gemini35-flash-pricing.md` Claim 5 (cross-vendor
    pricing synthesis noting "Claude Opus 4.7 is around 1.46x the price of 4.6
    when you take the new tokenizer into account"): this note's Claims 2–3 and
    7 provide a second, independent instance of the same Anthropic pattern —
    nominally stable per-token pricing paired with a new tokenizer that
    increases effective cost — this time for Sonnet 5 vs. Sonnet 4.6 rather
    than Opus 4.7 vs. Opus 4.6. Together the two notes establish that
    tokenizer-driven effective price increases are now a recurring pattern
    across at least two separate Anthropic model-tier upgrades in 2026, not a
    one-off Opus-specific event.

- **Contradicts**: None filed. No existing corpus source claims Anthropic
  pricing or tokenizer behavior that this source disagrees with; the apparent
  "input"/"input" typo in Willison's own pricing sentence (Claim 7) is an
  error internal to this single source, corrected here by cross-checking
  Anthropic's own docs page, not a cross-source contradiction.

- **Extends**:
  - `blog-simonwillison-fable-5-export-controls.md`, `blog-simonwillison-claude-fable-5.md`,
    `blog-latentspace-fable-5-mythos-launch.md`, and
    `blog-simonwillison-fable-mythos-access-directive.md` (the Fable 5/Mythos 5
    launch, safeguard, and export-control saga from June 2026): Claim 9 of this
    note is the first source in this corpus to show Anthropic explicitly
    invoking the Sonnet-5-vs-Mythos-5 comparative capability ranking in a
    system card to justify a *different, lighter* safeguard regime for a
    non-Mythos-class model — connecting the general-availability Sonnet 5
    release directly to the capability-tiering logic established during the
    Mythos 5 controversy one to three weeks earlier.
  - `docs-github-copilot-sonnet5-ga.md`: that note documents Sonnet 5's GitHub
    Copilot integration (plans, platforms, billing, ZDR) without covering the
    tokenizer change, the removed sampling parameters, the 400-error migration
    behaviors, or the cybersecurity safeguard framing — all of which are new
    to the corpus via this note (Claims 1–9, 12).

- **Novel**:
  - First corpus documentation of Sonnet 5's new tokenizer and its measured,
    per-language/per-format token-inflation multipliers (Claims 2–3).
  - First corpus documentation of the specific 400-error migration behaviors
    for sampling parameters and manual extended thinking on Sonnet 5 (Claims
    4–5), including the explicit code-level migration guidance.
  - First corpus documentation of Sonnet 5's cybersecurity safeguard framing
    and its HTTP-200-with-`stop_reason:"refusal"` response mechanics (Claim 8).
  - First corpus source to connect a Sonnet-class model's system card directly
    to the Mythos-class capability-tiering framework via an explicit
    less-capable-than-Mythos-5 comparison (Claim 9).

## Guide Impact

- **Chapter 01 (Daily Workflows — Model Selection)**: Add Sonnet 5's headline
  capability claim ("close to Opus 4.8, but at lower prices," per Claim 10) as
  a vendor-asserted, not independently benchmarked, data point — consistent
  with how the guide already treats similar vendor "strong results" framing
  from GitHub's Sonnet 5 changelog (`docs-github-copilot-sonnet5-ga.md` Claim
  2). Do not present it as settled capability evidence.

- **Chapter 02 (Harness Engineering — Cost/Token Budgets)**: This is the most
  actionable update from this source. Add a specific warning, citing Claims
  2–3 and 7: "Migrating to Claude Sonnet 5 from Sonnet 4.6 is API-compatible
  and will not raise errors on its own, but the new tokenizer produces
  ~30% more tokens for English content (up to 1.42x measured), ~33% more for
  Spanish, ~27–28% more for Python code, and roughly no change for Simplified
  Mandarin. Per-token list pricing is unchanged ($3/$15 per million
  input/output, or $2/$10 introductory through August 31, 2026), so the actual
  cost and `max_tokens` impact of a migration must be measured by recounting
  representative prompts against the new tokenizer, not assumed from the
  nominal price list." Also add the two loud (400-error) API changes from
  Claims 1, 4, and 5 as a hard migration checklist: remove non-default
  `temperature`/`top_p`/`top_k`, and replace manual `budget_tokens` thinking
  with adaptive thinking.

- **Chapter 04 (Context Engineering — Context Window Sizing)**: Add Claim 6:
  Sonnet 5's 1M-token context window is fixed (no smaller variant to select),
  but because the same window now holds less text on average (per the
  tokenizer change in Claim 2), practitioners sizing context budgets in *text*
  terms rather than token terms should re-measure effective capacity, not
  assume parity with Sonnet 4.6's 1M-token window.

- **Chapter 06 (Claude API — Migration and Error Handling)**: Add the specific
  400-error behaviors (Claims 4–5) and the cybersecurity-safeguard HTTP-200
  refusal mechanism (Claim 8) as concrete integration details: harnesses
  should check `stop_reason` for `"refusal"` on 200 responses, not rely solely
  on non-200 status codes to detect refusals, and should expect immediate 400
  errors (not silent degradation) if legacy sampling-parameter or
  manual-thinking code paths are not updated before migrating.

## Extraction Notes

1. **Followed a linked sub-page per MINER.md §1**: Willison's post is a short
   link-post whose primary technical content is explicitly sourced from
   Anthropic's official "What's new in Claude Sonnet 5" docs page. This Miner
   fetched that docs page directly (it is JS-rendered but the rendered text
   content was extracted) since it is substantive, central to the blog post's
   own framing, and provided several claims (the exact 400-error mechanics,
   the Priority Tier exclusion, the availability/ZDR details, the cybersecurity
   safeguard section) not fully spelled out in the shorter blog post text
   itself. The HN discussion thread linked from the post's "(via)" link and the
   pelican-drawing gist were not followed — the former is community discussion
   rather than primary content, and the latter is only the raw SVG output
   already characterized in Claim 13.
2. **Verbatim quote verification**: All quotes were verified against raw HTML
   fetched directly via `curl` for the Willison blog post (avoiding
   WebFetch's copyright-triggered summarization/paraphrase behavior for this
   post) and against extracted rendered text for the Anthropic docs page. No
   quote in this note was produced by an intermediate summarizing model.
3. **Corrected a source typo, not a contradiction**: Willison's own post states
   pricing as "$3/million input, $15/million input" (both labeled "input"),
   which is very likely a typo for "output" given Anthropic's docs page
   explicitly states "$15 per million output tokens." This note's Claim 7 uses
   the docs page's corrected wording and flags the discrepancy explicitly
   rather than silently fixing it or treating it as a cross-source
   contradiction (it is an internal error in a single source, not a claim
   conflict between two sources).
4. **No contradiction issue filed**: Cross-referencing against existing
   tokenizer/pricing notes (`blog-simonwillison-gemini35-flash-pricing.md`) and
   the Mythos-class safeguard notes found corroboration and extension, not
   contradiction. No `C-NNN` entry was warranted.
