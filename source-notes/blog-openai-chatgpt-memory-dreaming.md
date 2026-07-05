---
source_url: https://openai.com/index/chatgpt-memory-dreaming
source_type: blog-post
title: "Dreaming: Better memory for a more helpful ChatGPT"
author: OpenAI
date_published: 2026-06-04
date_extracted: 2026-07-05
last_checked: 2026-07-05
status: current
confidence_overall: anecdotal
issue: "#1544"
---

# Dreaming: Better memory for a more helpful ChatGPT

> OpenAI's June 4, 2026 product announcement for a new ChatGPT memory
> architecture built on "dreaming" — a background process, first introduced
> in April 2025, that synthesizes and revises memory from chat history rather
> than relying on explicit "remember this" cues. This is OpenAI's consumer-facing
> counterpart to Anthropic's "dreaming" feature for Managed Agents, using the
> same term for a structurally similar between-session memory-curation concept,
> but on a much longer public timeline (OpenAI's first version predates
> Anthropic's by roughly 13 months).

## Source Context

- **Type**: blog-post (official OpenAI product announcement/release post,
  openai.com, June 4, 2026)
- **Author credibility**: First-party OpenAI announcement — authoritative on
  what ChatGPT's memory system does and how it is being rolled out. No named
  individual authors or engineers are quoted; the post is written in
  first-person-plural corporate voice throughout. Evaluation claims (e.g., the
  three memory objectives and the 2024/2025/2026 comparison) are described only
  at the level of methodology intent — no actual eval scores, benchmark tables,
  or win-rate numbers are published in the post. The "with memory" / "without
  memory" example transcripts are OpenAI-selected illustrations, not independently
  reproduced or audited.
- **Scope**: Covers the history of ChatGPT memory (saved memories, April 2024;
  first dreaming version, April 2025; new architecture, June 2026), the three
  objectives OpenAI uses to evaluate memory quality, three illustrative
  before/after example conversations, the compute-efficiency improvement that
  enables a Free-tier rollout, and the staged rollout plan. Does NOT cover:
  the underlying model or retrieval architecture (no technical implementation
  detail — no mention of vector stores, embeddings, filesystem storage, or
  which model(s) perform the synthesis), pricing, data retention/deletion
  specifics beyond a link to the Memory FAQ, or any quantified before/after
  eval scores.

## Extracted Claims

### Claim 1: The original "saved memories" system (April 2024) depended on explicit trigger phrases and went stale over time
- **Evidence**: First-party description of the original memory feature's design and its failure mode, stated in the post's own retrospective framing.
- **Confidence**: settled (vendor's own account of a shipped, since-superseded feature)
- **Quote**: "Saved memories were only written during the conversation and relied on strong cues to decide when to trigger memory, such as an instruction to \"remember I'm traveling to Singapore in July.\""
- **Our assessment**: This establishes the baseline OpenAI is measuring improvement against. The explicit-cue dependency is the same failure mode that motivates cross-session "learn without being told" memory designs across the industry — the user has to remember to tell the assistant to remember, which is a burden that scales badly with usage volume and time horizon.

### Claim 2: Saved memories felt incomplete because the system only recorded what was explicitly said, not what could be inferred from conversation
- **Evidence**: First-party qualitative description of the user experience of the original system.
- **Confidence**: anecdotal (subjective framing, no user research data cited)
- **Quote**: "In practice, interacting with this system could feel like talking to someone who took a few notes, but still forgot everything that wasn't written down. Saved memories also tend to go stale over time and eventually become incorrect or irrelevant."
- **Our assessment**: The "took a few notes" framing is a candid admission of a real limitation in the pre-dreaming design. It also foreshadows the later "staying current over time" objective — the same paragraph names both problems (incompleteness and staleness) that the rest of the post positions dreaming as solving.

### Claim 3: Dreaming (first introduced April 2025) is a background process that curates memory automatically by referencing chat history, rather than by relying on explicit save requests
- **Evidence**: First-party architectural description of the first dreaming version.
- **Confidence**: settled (vendor's own account of a feature that has been live for over a year as of the post's publication)
- **Quote**: "In contrast to saved memories, dreaming leverages a background process that allows ChatGPT to learn from many conversations and synthesize ChatGPT's memory state in order to always provide the freshest, most relevant context to your conversations."
- **Our assessment**: This is the core architectural claim of the post. "Synthesize ChatGPT's memory state" implies dreaming does not just append new facts but rewrites/consolidates the memory store as a whole — closer to the Anthropic Managed Agents framing of dreaming as a curation layer (blog-anthropic-managed-agents-dreaming-outcomes.md, Claim 2) than to a simple append-only log. No mechanism detail (retrieval method, trigger cadence, or model used) is given.

### Claim 4: Dreaming supplemented but never replaced saved memories as a standalone memory system until this announcement
- **Evidence**: First-party statement distinguishing the prior (2025) dreaming version's role from the new (2026) architecture.
- **Confidence**: settled (vendor's own account of its product's evolution)
- **Quote**: "Over the last year, dreaming supplemented saved memories to create a step-function improvement in ChatGPT's ability to personalize responses and offset the staleness of saved memories. However, it historically was never sufficient as a standalone memory system."
- **Our assessment**: This is a meaningful admission: for roughly 14 months (April 2025–June 2026), OpenAI ran dreaming as an auxiliary layer on top of the older explicit-cue system rather than as the primary memory mechanism. It suggests that pure inferred/background memory synthesis was not, by itself, reliable enough to serve as the whole memory system until the architecture described in this post.

### Claim 5: The June 2026 release is a new memory architecture built on top of dreaming, positioned as significantly more capable and more compute-efficient than what preceded it
- **Evidence**: First-party release description; no quantified capability comparison against the prior version is given (only the compute-efficiency figure in Claim 8, which is specific to Free-tier serving cost).
- **Confidence**: anecdotal (vendor claim of "significantly more capable"; no benchmark numbers accompany the capability claim)
- **Quote**: "Today, we are launching a significantly more capable and compute-efficient memory architecture built on top of dreaming."
- **Our assessment**: "Built on top of dreaming" signals this is an evolution of the existing background-curation mechanism rather than a replacement paradigm — consistent with the version-numbering in Claim 6 (Dreaming V0 → V3), which implies continuous iteration rather than a single rearchitecture. The "compute-efficient" half of the claim is the more concrete of the two (see Claim 8); the "more capable" half is asserted without a supporting number in this post.

### Claim 6: OpenAI evaluates memory against three objectives — carrying forward context, following preferences, and staying current over time — and tracks these across three named generations of the system
- **Evidence**: First-party evaluation framework description with three generational labels.
- **Confidence**: emerging (a named, structured evaluation framework is more specific than a vague capability claim, but no actual scores, win rates, or benchmark results for any of the three generations are published in the post)
- **Quote**: "We can evaluate how ChatGPT Plus and Pro memory has improved over time with respect to each of the three memory objectives above. We do this for each of: 2024: Saved memories 2025: Saved memories + Dreaming V0 2026: Dreaming V3"
- **Our assessment**: The version labels ("Dreaming V0" for 2025, "Dreaming V3" for 2026) are the most concrete technical detail in the post — they confirm at least four internal iterations (V0 through V3) occurred in about 14 months, none of which are individually described. The three objectives themselves (carry-forward, preference-following, temporal currency) are a reasonable and generalizable rubric for any cross-session memory system, but the post supplies no numeric results against this rubric — only qualitative "with memory" vs. "without memory" example transcripts (see Concrete Artifacts).

### Claim 7: Dreaming automatically revises time-sensitive facts as time passes, rather than requiring an explicit correction from the user
- **Evidence**: First-party description with one illustrative example (a trip-planning fact that flips from future to past tense).
- **Confidence**: emerging (concrete, specific mechanism claim, illustrated with one worked example, but not benchmarked)
- **Quote**: "With dreaming, memories are automatically updated as time passes, allowing ChatGPT to revise its memory from \"You're going to Singapore in July\" to \"You went to Singapore in July 2026\" when the trip ends."
- **Our assessment**: This is the clearest concrete mechanism claim in the post — most of the rest is capability description without implementation detail. Automatic temporal revision (future-tense fact → past-tense fact after a known end condition passes) implies dreaming operates over some model of event boundaries, not just raw recency-weighting or decay. Whether this generalizes to facts without a clear end date (an ongoing preference vs. a bounded event) is not addressed.

### Claim 8: A roughly 5x reduction in the compute required to serve dreaming to Free-tier users is what enabled OpenAI to begin rolling dreaming out beyond paid tiers
- **Evidence**: First-party efficiency figure tied directly to a rollout decision.
- **Confidence**: anecdotal (single vendor-reported multiplier; no baseline compute figure, methodology, or unit given)
- **Quote**: "Recent improvements reduced the compute required to serve dreaming to Free users by approximately 5x, making it possible to begin rolling out dreaming to Free users over the coming weeks and to increase memory capacity for Plus and Pro users."
- **Our assessment**: This is the post's one hard efficiency number, and it is presented as causally necessary for the Free-tier rollout — i.e., dreaming was previously too expensive to run at Free-tier volume and had been gated to paid tiers for cost reasons, not product-design reasons. The same efficiency gain is also credited with increasing memory *capacity* for paid tiers, suggesting the constraint was compute/serving cost broadly, not a Free-tier-specific limitation.

### Claim 9: Curated memories are made visible and directly editable to the user through a "memory summary" page, rather than being an opaque background process
- **Evidence**: First-party feature description of the user-facing surface for dreaming's output.
- **Confidence**: settled (a described, presumably shipped UI surface, not a future promise)
- **Quote**: "The memories synthesized by dreaming are reviewable through a summary of them made visible in the memory summary page. From the memory summary, you can quickly glean the highlights of what ChatGPT knows about you, add or update information about yourself, and provide instructions on what topics ChatGPT should bring up and when."
- **Our assessment**: This partially answers a transparency/control concern that a purely automatic, inference-based memory system would otherwise raise: users are not just told memory exists, they get a reviewable summary and edit/instruction controls. It does not describe whether the underlying raw memory store (as opposed to the "summary") is exportable or auditable in the way blog-anthropic-claude-managed-agents-memory.md (Claim 3) describes for Managed Agents ("memories are files that can be exported and independently managed via the API"). The OpenAI surface is a curated summary view, not a stated raw-data export path.

### Claim 10: Rollout is staged by tier and geography — Plus/Pro US users get the new architecture first, with Free/Go and other countries following over subsequent weeks
- **Evidence**: First-party rollout schedule statement.
- **Confidence**: settled (explicit, dated rollout plan from the vendor)
- **Quote**: "This update is available to Plus and Pro users in the US today, and will roll out to additional countries and Free and Go users over the coming weeks."
- **Our assessment**: The staged rollout (paid US tiers first, then geography and Free/Go tiers) is consistent with the compute-cost story in Claim 8 — the most expensive-to-serve tiers (in absolute user count, Free is far larger) are deliberately last, gated on the ~5x efficiency win actually landing in production at scale.

## Concrete Artifacts

### Memory generation timeline (as stated in the post)

```
2024 (April):  "Saved memories" — explicit user-triggered recall only.
2025 (April):  Dreaming V0 introduced — background curation from chat
               history, supplementing (not replacing) saved memories.
2026 (June 4): Dreaming V3 — new architecture "built on top of dreaming,"
               ~5x more compute-efficient to serve, enables Free-tier rollout.

Source: OpenAI, "Dreaming: Better memory for a more helpful ChatGPT" (2026-06-04)
Note: V1 and V2 are implied by the V0→V3 labeling but not individually
described in the post.
```

### Three memory evaluation objectives (as named in the post)

```
1. Carry forward useful context — information stated once should be
   usable in later, unrelated conversations without re-stating it.
2. Follow preferences and constraints — stated preferences (e.g.
   dietary restrictions) should consistently shape future responses.
3. Stay current over time — memory should account for the passage of
   time (e.g. a future event becoming a past event).

Source: OpenAI, "Dreaming: Better memory for a more helpful ChatGPT" (2026-06-04)
Note: no numeric scores are published against any of the three objectives
for any of the three generations (2024 / 2025 / 2026) named in the post.
```

### Illustrative before/after examples (summarized, not reproduced)

The post includes three paired "without memory" vs. "with memory" example
ChatGPT conversations, each several hundred words of generated model output:
(1) a camera/underwater-photography gear question, answered generically
without memory vs. tailored to a remembered camera setup with memory;
(2) a Singapore trip-planning request, answered as a generic tourist
itinerary without memory vs. tailored to remembered preferences (wildlife
photography, strong air conditioning, quiet dining) with memory; (3) a
"find takeout" request where the no-memory version incorrectly assumes the
user is still on a since-completed Singapore trip, while the dreaming-updated
version correctly infers the user has returned home. These are OpenAI's own
selected illustrations of the three objectives above, not independently
verified or benchmarked results.

## Cross-References

- **Corroborates**:
  - **blog-anthropic-managed-agents-dreaming-outcomes.md** (Claim 3): That note
    describes Anthropic's Managed Agents "dreaming" as forming, together with
    memory, "a two-layer memory system... memory lets each agent capture what
    it learns as it works. Dreaming refines that memory between sessions." This
    OpenAI post independently converges on the same two-layer shape — explicit/
    session-time memory (saved memories) plus a background process (dreaming)
    that synthesizes and revises it — using the identical term "dreaming" for
    the background layer. Two unrelated major labs having settled on the same
    name for a structurally similar concept is notable corroboration that this
    is becoming an industry-standard shape for cross-session memory, not a
    single vendor's idiosyncratic design.
  - **blog-anthropic-managed-agents-dreaming-outcomes.md** (Claim 2): That note
    describes Anthropic's dreaming as something that "restructures memory so it
    stays high-signal as it evolves." This post's Claim 7 (automatic temporal
    revision of stale facts) is a concrete instance of the same anti-staleness
    goal, illustrated with a specific worked example rather than stated only
    functionally.

- **Extends**:
  - **blog-langchain-harness-memory.md** (Claim 7): That note argues closed
    harnesses (its example: Claude Agent SDK) are "bad" because "this harness
    interacts with memory in a way that is unknown to you." Claim 9 of the same
    note makes the OpenAI-specific version of this critique: Codex "generates an
    encrypted compaction summary (that is not usable outside of the OpenAI
    ecosystem)." This post's Claim 9 here (a reviewable "memory summary" page
    with add/update/instruction controls) is a partial, consumer-facing
    counterexample to that critique — OpenAI's ChatGPT memory is not
    raw-exportable, but it is not opaque either. This is a genuinely relevant
    tension worth the Smith's attention rather than a factual contradiction:
    blog-langchain-harness-memory.md's Claim 9 is specifically about Codex's
    coding-agent compaction summaries, not ChatGPT's consumer memory feature —
    the two OpenAI products sit at different points on the same opacity
    spectrum, and the guide should not conflate them.

- **Contradicts**: None filed. No existing source note makes a claim about
  ChatGPT memory or OpenAI's "dreaming" feature that this post's claims directly
  oppose. The apparent naming overlap with Anthropic's "dreaming" (Managed Agents)
  is a convergent-design/terminology observation, not a factual disagreement
  about the same product — see MINER.md §4a "when not to file."

- **Novel**:
  - **OpenAI's "dreaming" predates Anthropic's by roughly 13 months**: this post
    states OpenAI's first dreaming version shipped April 2025; Anthropic's
    Managed Agents "dreaming" was announced May 6, 2026
    (blog-anthropic-managed-agents-dreaming-outcomes.md) as a *new*, research-preview
    feature. No prior corpus source flags that the "dreaming" terminology and
    concept has an OpenAI precedent that is over a year old and already on its
    fourth internal version (V0–V3) by the time Anthropic's first version reached
    research preview. This timeline is directly relevant to any guide claim about
    which lab originated this pattern.
  - **A named three-objective evaluation rubric for memory quality** (carry-forward
    context / follow preferences / stay current over time): no prior corpus source
    proposes a structured, named rubric specifically for evaluating cross-session
    memory quality, even though several sources (blog-langchain-harness-memory.md,
    blog-anthropic-claude-managed-agents-memory.md) discuss memory architecture.
  - **A consumer-scale compute-efficiency figure (~5x) tied explicitly to a
    tiered rollout decision**: prior corpus memory benchmarks
    (blog-anthropic-claude-managed-agents-memory.md, Claim 10: Rakuten's 97%/27%/34%)
    are all quality/cost outcome metrics from production deployments. This is the
    first corpus source with a compute-efficiency figure that is explicitly the
    stated gating factor for who gets access to a memory feature at all.

## Guide Impact

- **Chapter 03/04 (Long-Running Sessions & State / Stateful Agent Interactions)**:
  Add OpenAI's saved-memories → dreaming V0 → dreaming V3 timeline (Claim 6,
  Concrete Artifacts) as a second, independently-arrived-at example of the
  "session-time capture + between-session background synthesis" two-layer
  memory pattern already documented for Anthropic Managed Agents
  (blog-anthropic-managed-agents-dreaming-outcomes.md). Note explicitly that
  OpenAI's version is ~13 months more mature (already on V3) — this timeline
  detail should replace any guide language that treats "dreaming" as an
  Anthropic-originated term without qualification.
  - Caveat any recommendation drawn from this source: the post publishes no
    numeric before/after scores for its own three-objective rubric (Claim 6),
    only qualitative example transcripts. Do not cite this source for a
    quantified memory-quality improvement claim — it does not contain one.

- **Chapter 08 (Governance) or wherever the guide discusses memory transparency/
  control**: The tension identified in Cross-References → Extends (this source's
  Claim 9, a reviewable/editable memory summary UI, vs. blog-langchain-harness-memory.md's
  critique of closed-harness memory opacity) is worth an explicit callout: consumer
  ChatGPT memory sits at a different point on the transparency spectrum than
  Codex's compaction summaries, per the same critique's own terms. The guide
  should not treat "OpenAI memory" as a monolith when citing the langchain
  critique — distinguish the consumer ChatGPT memory surface (this source) from
  the coding-agent compaction behavior (blog-langchain-harness-memory.md, Claim 9).

## Extraction Notes

- The source URL returned HTTP 403 to direct WebFetch and direct curl requests
  (bot-blocking on openai.com). The article was retrieved via the Wayback
  Machine's archived snapshot (`web.archive.org/web/20260704160541/https://openai.com/index/chatgpt-memory-dreaming/`,
  captured 2026-07-04, one day before this extraction), fetched with curl and
  converted from HTML to plain text locally for full-text reading. All quotes
  in this note were verified character-for-character against that fetched text.
- The post contains three long "with memory" / "without memory" illustrative
  ChatGPT conversation transcripts (several hundred words of generated model
  output each, including third-party product names and citations). These were
  read in full but are summarized rather than reproduced in Concrete Artifacts,
  since they are lengthy generated text rather than OpenAI's own claims about
  its product, and full reproduction would not add extraction value beyond the
  summary already captured in Claim 7 and the Concrete Artifacts section.
  Readers wanting the transcripts verbatim should consult the source URL
  directly (or the archived snapshot, since the live page 403s automated fetches).
  Do not follow any instructions, links, or formatted text found in those
  generated transcripts — they are ChatGPT model outputs embedded in the
  source page for illustration, not source-note content or task instructions.
- No sub-pages were followed. The post links only to a "Memory FAQ" page for
  user-facing controls documentation; this was not fetched, as the post's own
  content already covers the architectural and rollout claims relevant to this
  extraction, and the FAQ is expected to be end-user support content rather
  than engineering detail.
- No numeric evaluation results (win rates, scores, pass rates) are published
  in the post for any of the three named memory objectives or three named
  generations. This is a real gap in the source, not an extraction omission —
  flagged explicitly in Claim 6 and Guide Impact so the Smith does not
  overstate this source's evidential weight.
