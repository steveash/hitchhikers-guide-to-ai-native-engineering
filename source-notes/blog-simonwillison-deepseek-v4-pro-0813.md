---
source_url: https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/
source_type: blog-post
title: "DeepSeek V4 Pro 0813 (on OpenRouter)"
author: Simon Willison
date_published: 2026-08-12
date_extracted: 2026-08-22
last_checked: 2026-08-22
status: current
confidence_overall: anecdotal
issue: "#2855"
---

# DeepSeek V4 Pro 0813 (on OpenRouter)

> A short Willison link-blog post announcing DeepSeek-V4-Pro-0813 (API-only
> at launch, open weights confirmed days later at 1.7T parameters/893GB) and
> a genuinely novel observation — unlike prior reasoning-effort tests in this
> corpus, low/medium/high here produced *stylistically* different pelican
> illustrations, not just better-or-worse ones. The post's linked Hacker
> News benchmark table (itself a thirdhand WeChat-leak → deleted-Reddit-post
> → HN-ASCII-table relay) is the only quantitative capability data available
> for this checkpoint, and it should be treated with corresponding caution.

## Source Context

- **Type**: blog-post (Willison's link-blog format — a single short post of
  roughly 120 words of original prose plus three image alt-text
  descriptions and one linked external discussion; auto-discovered via the
  `simon-willison` trusted feed).
- **Author credibility**: Simon Willison is creator of Django and the `llm`
  CLI, and the corpus's most-cited practitioner commentator on LLM tooling
  (see `blog-simonwillison-deepseek-v4.md`, `blog-simonwillison-deepseek-v4-flash-0731.md`,
  `blog-simonwillison-kimi-k3-pelican-benchmark.md`). This post is his
  standard pattern: a link to the model + a short first-person reaction +
  his own hands-on pelican-SVG test. The benchmark data he links to
  (Hacker News item 49274600, comment 49275180) is explicitly *not* his own
  testing or endorsement — he describes only the chain of custody by which
  it reached him, and does not vouch for its accuracy.
- **Scope**: Covers the model's launch channel (API-only via OpenRouter),
  a later-confirmed open-weights release with parameter count and HF file
  size, a three-way (low/medium/high) reasoning-level pelican-SVG
  comparison, and a pointer to a thirdhand benchmark table on Hacker News
  (which this note follows, per MINER.md §1's up-to-5-linked-pages
  allowance, since the post's own text treats the benchmark provenance as
  the substantive part of that paragraph). Does NOT cover: official
  DeepSeek pricing for this checkpoint (no DeepSeek pricing page is linked
  or cited anywhere in the post or its HN thread), active-parameter count/
  MoE sparsity, context window size, license terms, or any agentic-task
  benchmark run or verified by Willison himself.

## Extracted Claims

### Claim 1: DeepSeek-V4-Pro-0813 launched API-only via OpenRouter, with no DeepSeek-authored announcement page identified by Willison at time of writing
- **Evidence**: Direct statement in the post's opening sentence.
- **Confidence**: settled (directly observed by the author at time of posting)
- **Quote**: "The latest DeepSeek Pro model is now available, via API only. I had to link to OpenRouter because DeepSeek don't have any obvious announcement page for their new model."
- **Our assessment**: This is a minor but concrete data point about DeepSeek's release practices: unlike some vendors that pair a model drop with a dedicated blog post or system card, this checkpoint shipped with no first-party write-up that Willison could find, forcing him (and this note) to rely on a third-party API host's listing and, for capability data, a multi-hop leak (Claim 5). Practitioners tracking DeepSeek releases should not expect a canonical announcement page for every checkpoint.

### Claim 2: Open weights for V4-Pro-0813 were confirmed on Hugging Face days after the API launch, at 1.7 trillion parameters and 893GB
- **Evidence**: An inline "Update" appended to the post's second paragraph, linking to the Hugging Face model page.
- **Confidence**: settled (published Hugging Face listing, linked directly)
- **Quote**: "I haven't been able to confirm if they plan to release the open weights, but given the weights are available for both April's deepseek-ai/DeepSeek-V4-Pro and July's deepseek-ai/DeepSeek-V4-Flash-0731 it seems likely. Update: the weights are now available on Hugging Face, 1.7T parameters, 893 GB."
- **Our assessment**: This confirms the checkpoint grew from April V4-Pro's 1.6T/865GB (`blog-simonwillison-deepseek-v4.md` Claim 1 and its Concrete Artifacts spec table) to 1.7T/893GB — a modest ~6% increase in both parameter count and file size, consistent with an incremental point-release rather than a architectural overhaul. No active-parameter count is given for 0813, so (as with the July Flash checkpoint per `blog-simonwillison-deepseek-v4-flash-0731.md` Claim 2) the MoE sparsity ratio for this specific checkpoint remains unconfirmed — practitioners should not assume the April Pro's 49B-active figure still applies.

### Claim 3: Willison observed unusually large *stylistic* divergence between reasoning levels in the pelican-SVG test — a kind of variation he says he has not seen from any other model
- **Evidence**: Willison's own hands-on test across OpenRouter's low/medium/high reasoning-level parameter, described in prose and illustrated with three distinct rendered SVGs (alt-text captured below).
- **Confidence**: anecdotal (single practitioner, single creative-code test, no systematic multi-run sweep at each level)
- **Quote**: "Interestingly I got very different looking pelicans for the three different reasoning levels of low, medium, and high. I've not noticed this kind of difference from any other model:"
- **Our assessment**: This is a different observation from the one already in this corpus's July V4-Flash note. `blog-simonwillison-deepseek-v4-flash-0731.md` Claim 7 documents reasoning-effort sensitivity as a *quality* axis — default reasoning produced a structurally broken bicycle, `reasoning_effort high` produced a correctly-assembled one. Here, all three levels (per the image alt-text below) produced structurally coherent pelican-on-bicycle scenes; what changed was *style* — color palette, linework, and added decorative elements (a hat, a flag, musical notes) — not correctness. Willison's own framing ("I've not noticed this kind of difference from any other model") explicitly marks this as novel to his testing, distinct from the pass/fail-style divergence documented for the July Flash checkpoint. This is a single anecdotal data point, not a systematic finding, and the underlying mechanism (does higher reasoning effort change persona/creativity, not just correctness, for this specific checkpoint?) is not explained or investigated further in the post.

### Claim 4: The three reasoning-level pelican illustrations differ concretely in composition and decorative elements (verbatim image alt-text)
- **Evidence**: Three image alt-text descriptions embedded in the post, one per reasoning level.
- **Confidence**: anecdotal (descriptive alt-text for a single test's outputs)
- **Quote (low)**: "Flat vector illustration of a white pelican with a large orange beak, wearing a straw hat with an orange band, riding a teal road bicycle in profile, set against a pale cream circle with a dashed outline and small motion marks trailing behind."
- **Quote (medium)**: "A similar cartoon pelican cycling, drawn in a looser outlined style: the bird's body is mostly white line art, its orange beak pouch hangs open under a yellow cap, a long red tongue streams backwards towards a yellow sun, and a small blue fish sits on a tray by the handlebars of a green bicycle whose wheels are drawn as broken yellow arcs."
- **Quote (high)**: "The pelican again, this time on a red bicycle against a pale blue background, with a bright yellow beak and pouch, a purple pennant flag on the back, a wicker front basket holding a small fish, and black musical notes floating in the top right corner."
- **Our assessment**: Notably, the alt-text for the "medium" output describes "wheels... drawn as broken yellow arcs" — a compositional flaw similar in kind (though not identical) to the July Flash checkpoint's default-reasoning failure mode ("the wheels are just orange arcs with no rims or spokes," per `blog-simonwillison-deepseek-v4-flash-0731.md` Concrete Artifacts). This suggests reasoning-level sensitivity in DeepSeek's V4 family may still include some correctness variation alongside the stylistic variation Claim 3 highlights, even though Willison's own framing emphasizes the stylistic novelty rather than this compositional flaw. Practitioners should not read Claim 3 as "all three levels were equally well-formed, only the style changed" — the medium-reasoning wheels are described as broken.

### Claim 5: The only benchmark data cited in the post reached Willison through an unverifiable, multi-hop relay: an internal DeepSeek WeChat group, a deleted Reddit post, and finally an ASCII table pasted into a Hacker News comment
- **Evidence**: Willison's own description of the provenance chain, with links to the Reddit post (showing "removed by moderator") and the specific Hacker News comment.
- **Confidence**: anecdotal (explicitly flagged by the author himself as an untraceable relay, not a citable primary source)
- **Quote**: "In terms of benchmarks... as far as I can tell those were released to the Official DeepSeek WeChat Group, then copied and pasted into a post on Reddit which was deleted by the moderators for being "low-effort", then copied into this ASCII-art table on Hacker News."
- **Our assessment**: This is itself a useful data point about how benchmark information for Chinese frontier-adjacent models sometimes propagates in practice: no DeepSeek-hosted benchmark page exists for this checkpoint (consistent with Claim 1), so the only numbers available to the community are several hops removed from any DeepSeek-controlled source, with no stated author, methodology, or reproducibility guarantee at any hop. Any capability numbers extracted from that table (Claim 6) should be weighted accordingly — this is closer to an unverified leak than a benchmark.

### Claim 6: The Hacker News ASCII table gives DS-V4-Pro-0813 higher scores than both its own "Preview" predecessor and DS-V4-Flash-0731 across all ten listed benchmarks, and places it ahead of GLM-5.2 on every listed benchmark, with mixed results against Kimi-K3, Claude Opus-4.8, and "Fable 5 (w/ fallback)"
- **Evidence**: An ASCII-formatted markdown table posted in Hacker News comment id 49275180 (thread for item 49274600, the story Willison links to), attributed to user "scrlk," sourced by that commenter to a (now-inaccessible) Reddit post.
- **Confidence**: anecdotal (unverified thirdhand relay per Claim 5; no stated benchmark methodology, run count, or independent reproduction; poster's own identity/authority unconfirmed)
- **Quote**: "Benchmarks:" (introducing the table; full table reproduced verbatim in Concrete Artifacts)
- **Our assessment**: Selected figures from the table: DS-V4-Pro-0813 scores 87.9 on Terminal Bench 2.1 (vs. 82.7 for DS-V4-Flash-0731, 72.1 for "DS-V4-Pro Preview," 81.0 for GLM-5.2, 88.3 for Kimi-K3, 85.0 for Opus-4.8, 88.0 for Fable 5); 42.7/60.0 on HLE without/with tools (vs. 49.8/57.9 for Opus-4.8 and 53.3/63.0 for Fable 5 — Pro-0813 trails both); and 31.8 on "AutomationBench (Public)" (vs. 27.2 for Opus-4.8 and 29.1 for Fable 5 — Pro-0813 leads both on this specific listed variant). Taken at face value, this would suggest V4-Pro-0813 closed much of the gap to Opus-4.8 on agentic/coding-style benchmarks (Terminal Bench, Toolathlon-Verified, DSBench) while still trailing on raw knowledge/reasoning (HLE). But given Claim 5's provenance chain, "taken at face value" is doing a lot of work here — this is not independently verifiable from this source, and the Assayer/Smith should treat it as a rumor with directional plausibility, not a citable benchmark result.

### Claim 7: A Hacker News commenter cross-checked the leaked table against Qwen's own officially published Qwen3.8-Max benchmarks and concluded V4-Pro-0813 is "better on average but overall performance is comparable," at substantially lower cost
- **Evidence**: A follow-up comment (user "parsimo2010," HN item 49275709, replying to comment 49275180) manually comparing six of the leaked table's benchmark figures against Qwen3.8-Max's own published numbers.
- **Confidence**: anecdotal (a single HN commenter's own manual comparison across two separately-sourced benchmark sets — one thirdhand/leaked, one vendor-published — not independently re-verified by this Miner)
- **Quote**: "Assuming each published set of benchmarks is believable, it looks like v4 Pro 0813 is better on average but overall performance is comparable. Pro 0813 is much cheaper. If you don't need vision capabilities then you don't have much reason to use Qwen3.8-max."
- **Our assessment**: The commenter's own hedge ("Assuming each published set of benchmarks is believable") is the load-bearing caveat here — one side of the comparison is the same unverified leak flagged in Claims 5-6, and the other is Qwen's own vendor-published figures (see `blog-latentspace-ainews-qwen38-max-27b-launch.md` Claim 6, which documents Qwen3.8-Max at 87.3% SWE-bench and 67.4 Terminal-Bench 2.1 via the independent evaluator Vals AI, not Alibaba's own launch tweet). This is a comment-section synthesis of two different-provenance data sets, not a citable finding, but it is directionally consistent with the broader corpus pattern that Chinese open-weight frontier-adjacent models increasingly cluster together on capability while differentiating sharply on price.

### Claim 8: The same commenter reports an unofficial, uncited price figure of $0.435/$0.87 per million input/output tokens for V4-Pro-0813 via OpenRouter, alongside a mention that DeepSeek had announced an unspecified price increase
- **Evidence**: A follow-up exchange in the same Hacker News thread (comments 49275829, 49275937 between users "eli" and "parsimo2010").
- **Confidence**: anecdotal (an uncited, unattributed figure from an HN commenter — not from Willison's post, not from a DeepSeek pricing page, and not corroborated elsewhere in this corpus)
- **Quote**: "It still matters as a point of comparison until other providers come online. If the consensus price from other providers is much different that can be compared then. But for now we have $0.435 / $0.87 for v4 Pro 0813 (with increase announced but we don't know the new pricing), and $2 / $6 for Qwen3.8-max. So until we get other data points that is what we have to look at."
- **Our assessment**: If accurate, $0.435/$0.87 would sit well below April V4-Pro's $1.74/$3.48 (`blog-simonwillison-deepseek-v4.md` Claim 3 and Concrete Artifacts pricing table) — a roughly 4x price drop for the Pro tier. But this figure has no traceable source in either the blog post or the HN thread (no link to a DeepSeek or OpenRouter pricing page is given), and the same comment flags an "increase announced but we don't know the new pricing," meaning even the commenter treats this as provisional. This should be tracked for confirmation from a citable pricing source before being used in any guide cost table; it is not corroborated here.

### Claim 9: A separate Hacker News commenter computed an unweighted geometric mean across the leaked table's ten benchmarks, ranking DS-V4-Pro-0813 fourth of seven models compared (behind GPT-5.6 Sol, "Fable 5 (w/ fallback)," and Opus 5; ahead of Kimi-K3, DS-V4-Flash-0731, and GLM-5.2)
- **Evidence**: A standalone comment (user "goldenarm," HN item 49275754) presenting a self-computed geometric mean per model from the same leaked table.
- **Confidence**: anecdotal (an unaffiliated commenter's own arithmetic on an already-unverified thirdhand table; aggregation methodology, e.g. handling of the table's "-" entries for untested benchmarks, is not disclosed)
- **Quote**: "Geometric mean of all these benchmarks :" followed by "GPT-5.6 Sol: 65.5", "Fable 5 (w/ fallback): 64.5", "Opus 5: 64.0", "DS-V4-Pro 0813: 62.5", "Kimi-K3: 62.3", "DS-V4-Flash 0731: 55.8", "GLM-5.2: 47.3"
- **Our assessment**: This is a second-order derivative of already-anecdotal data (a geometric mean computed by an anonymous commenter over an unverified leak), and should not be treated as an independent benchmark result. It is included here only because it is the most-legible single-number summary anyone has produced from the leaked table, and because another commenter in the same subthread ("Maybe it's me but I don't see how DS Flash is better than GLM at all... no one should pick a model by the benchmarks") pushes back on exactly this kind of aggregation — a useful reminder, sourced from the same thread, not to over-index on it.

## Concrete Artifacts

### Post body (verbatim, simonwillison.net, 12th August 2026)

```
The latest DeepSeek Pro model is now available, via API only. I had to link
to OpenRouter because DeepSeek don't have any obvious announcement page for
their new model.

I haven't been able to confirm if they plan to release the open weights,
but given the weights are available for both April's
deepseek-ai/DeepSeek-V4-Pro and July's deepseek-ai/DeepSeek-V4-Flash-0731 it
seems likely. Update: the weights are now available on Hugging Face, 1.7T
parameters, 893 GB.

Interestingly I got very different looking pelicans for the three different
reasoning levels of low, medium, and high. I've not noticed this kind of
difference from any other model:

[Low / Medium / High pelican images — alt-text reproduced in Claim 4]

In terms of benchmarks... as far as I can tell those were released to the
Official DeepSeek WeChat Group, then copied and pasted into a post on
Reddit which was deleted by the moderators for being "low-effort", then
copied into this ASCII-art table on Hacker News.

Tags: ai, generative-ai, llms, pelican-riding-a-bicycle, deepseek,
llm-release, ai-in-china

Source: simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/, 12th August 2026
```

### Hacker News benchmark table (verbatim, comment id 49275180)

```
    | Benchmark                | DS-V4-Pro | DS-V4-Flash | DS-V4-Pro | DS-V4-Flash | GLM-5.2   | Kimi-K3   | Opus-4.8  | Fable 5       |
    |                          | 0813      | 0731        | Preview   | Preview     |           |           |           | (w/ fallback) |
    |--------------------------|-----------|-------------|-----------|-------------|-----------|-----------|-----------|---------------|
    | HLE (wo/w tools)         | 42.7/60.0 | 37.8/51.5   | 37.7/48.2 | 34.8/45.1   | 40.5/54.7 | 43.5/56.0 | 49.8/57.9 | 53.3/63.0     |
    | Terminal Bench 2.1       | 87.9      | 82.7        | 72.1      | 61.8        | 81.0      | 88.3      | 85.0      | 88.0          |
    | NL2Repo                  | 61.5      | 54.2        | 38.5      | 39.4        | 48.9      | -         | 69.7      | -             |
    | Cybergym                 | 83.3      | 76.7        | 52.7      | 38.7        | -         | 80.0      | 78.3      | 83.1          |
    | DeepSWE                  | 62.7      | 54.4        | 12.8      | 7.3         | 46.2      | 67.5      | 58.0      | 70.0          |
    | Toolathlon-Verified      | 74.1      | 70.3        | 55.9      | 49.7        | 59.9      | 76.5      | 76.2      | 77.9          |
    | Agents' Last Exam        | 25.7      | 25.2        | 16.5      | 15.8        | 23.8      | 27.6      | 25.7      | -             |
    | AutomationBench (Public) | 31.8      | 25.1        | 12.8      | 10.8        | 12.9      | 30.8      | 27.2      | 29.1          |
    | DSBench-FullStack        | 71.1      | 68.7        | 41.8      | 37.0        | 61.8      | 73.7      | 71.6      | 77.2          |
    | DSBench-Hard             | 67.2      | 59.6        | 31.1      | 25.8        | 54.5      | 63.0      | 71.7      | 68.3          |

Source: Hacker News comment by user "scrlk," item id 49274600, comment id
49275180, citing https://reddit.com/r/LocalLLaMA/comments/1vmi0fg/deepseek_v4pro0813_benchmarks/
(linked from simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/)
```

### Geometric-mean synthesis (verbatim, comment id 49275754)

```
Geometric mean of all these benchmarks :
* GPT-5.6 Sol: 65.5
* Fable 5 (w/ fallback): 64.5
* Opus 5: 64.0
* DS-V4-Pro 0813: 62.5
* Kimi-K3: 62.3
* DS-V4-Flash 0731: 55.8
* GLM-5.2: 47.3

Source: Hacker News comment by user "goldenarm," item id 49274600, comment
id 49275754
```

## Cross-References

### Cross-reference verification notes
`blog-simonwillison-deepseek-v4.md`, `blog-simonwillison-deepseek-v4-flash-0731.md`,
`blog-latentspace-ainews-qwen38-max-27b-launch.md`, and
`blog-latentspace-ainews-field-guide-fable.md` were each re-read directly
and the specific claim numbers cited below were confirmed against each
note's numbered `### Claim N:` headings in document order before writing
this section, per MINER.md §4b.

- **Corroborates**:
  - `blog-simonwillison-deepseek-v4.md` Claim 1 (V4-Pro established as "the
    new largest open weights model" at 1.6T/865GB in April 2026): Claim 2
    here shows the Pro line continuing to grow (1.7T/893GB by August),
    consistent with an incremental scale-up within the same architecture
    family rather than a reset.
  - `blog-simonwillison-deepseek-v4-flash-0731.md` Claim 7 (reasoning-effort
    sensitivity: DeepSeek's default reasoning level produced a structurally
    broken pelican SVG for the July Flash checkpoint, `reasoning_effort
    high` fixed it): Claim 4 here shows a similar compositional flaw
    ("wheels... drawn as broken yellow arcs") at the *medium* reasoning
    level for V4-Pro-0813, suggesting reasoning-level-dependent structural
    quality issues are not unique to the July Flash checkpoint or to
    default-vs-non-default settings specifically.
  - `blog-latentspace-ainews-qwen38-max-27b-launch.md` Claim 6 (Vals AI's
    independent evaluation of Qwen3.8-Max at 87.3% SWE-bench, 67.4
    Terminal-Bench 2.1): Claim 7 here documents an HN commenter's informal
    comparison of the leaked V4-Pro-0813 table against Qwen3.8-Max's own
    published figures, reaching a qualitatively similar "comparable
    capability, DeepSeek much cheaper" conclusion to the broader
    cost/capability pattern this corpus has documented for DeepSeek's V4
    family generally (`blog-simonwillison-deepseek-v4.md` Claims 2-3, 6-7).

- **Contradicts**: None filed. A numeric discrepancy was considered and
  does not meet the bar for a formal MINER.md §4a contradiction: the
  leaked HN table's "AutomationBench (Public)" column gives Claude Opus-4.8
  a score of 27.2 and "Fable 5 (w/ fallback)" a score of 29.1 (Claim 6),
  while `blog-latentspace-ainews-field-guide-fable.md` Claim 7 documents
  Artificial Analysis's own "AutomationBench-AA" leaderboard placing Opus
  4.8 at 48.5% and Claude Fable 5 at 48.6%. These are markedly different
  numbers for what could be the same underlying benchmark family. This was
  not filed as a contradiction because (a) the benchmark names differ
  ("AutomationBench (Public)" vs. "AutomationBench-AA," suggesting
  possibly different task subsets — a public sample vs. the full 657-task
  suite — rather than the same measurement), and (b) the HN-table side of
  the comparison is already flagged in Claims 5-6 as an unverified thirdhand
  leak with no named methodology, which does not rise to a "real claim" in
  the sense MINER.md §4a excludes from filing. Flagged prominently here for
  the Assayer and Smith: if a future source independently confirms
  "AutomationBench (Public)" as the same measurement as Artificial
  Analysis's "AutomationBench-AA," this would become a citable
  contradiction worth filing.

- **Extends**:
  - `blog-simonwillison-deepseek-v4.md` and `blog-simonwillison-deepseek-v4-flash-0731.md`:
    together those notes documented V4-Pro (April) and V4-Flash-0731 (July)
    specs, pricing, and efficiency metrics. This post extends the timeline
    with V4-Pro-0813 (August), though — unlike the two prior posts — this
    one carries no official DeepSeek pricing data at all (Claim 1), and its
    only capability data is a thirdhand leak (Claims 5-6) rather than a
    paper-cited efficiency metric or a named third-party leaderboard chart.
  - `blog-simonwillison-kimi-k3-pelican-benchmark.md`: that note's broader
    reflection on the pelican test's declining value as a capability
    ranking (once a benchmark becomes widely known, it stops
    discriminating) is implicitly relevant to Claim 3's finding — here the
    pelican test surfaces a *stylistic* rather than capability signal,
    arguably supporting the view that the test's remaining value is as "a
    forcing function for actually running a model" rather than a ranking
    tool.

- **Novel**:
  - **Stylistic (not just correctness) reasoning-level variance** (Claim
    3): the first instance in this corpus of a model producing materially
    different *visual style* — not just pass/fail quality — across
    reasoning-effort settings on the same creative-code prompt.
  - **A documented WeChat → deleted-Reddit → Hacker-News benchmark relay
    chain** (Claim 5): the first time this corpus has captured, in the
    author's own words, a specific multi-hop informal distribution path
    for a frontier-adjacent model's benchmark numbers, as opposed to either
    a vendor paper citation or a named third-party evaluator's leaderboard.
  - **An unofficial, uncorroborated sub-$0.50/M pricing figure for a
    Pro-tier DeepSeek model** (Claim 8): if confirmed, this would be a
    significant new low for the "large frontier-adjacent model" pricing
    tier this corpus has tracked since April (`blog-simonwillison-deepseek-v4.md`
    Claim 3, Novel section), but it is not corroborated by any citable
    source in this note.

## Guide Impact

- **Ch03 (Model Selection)**: Do not add the leaked benchmark table (Claim
  6) or the uncited pricing figure (Claim 8) to any guide-facing pricing or
  capability table as settled data — both lack a traceable, citable source.
  If the guide already has a "DeepSeek V4 Pro" pricing entry sourced from
  `blog-simonwillison-deepseek-v4.md` (April, $1.74/$3.48), it should not be
  silently updated from this source; flag the entry as "pricing for the
  0813 checkpoint unconfirmed as of August 2026" and watch for an official
  DeepSeek or OpenRouter pricing page.
- **Ch02 (Reasoning-Effort Configuration)**: Claim 3/4 add a data point to
  the guide's reasoning-effort discussion (already informed by
  `blog-simonwillison-deepseek-v4-flash-0731.md` Claim 7): reasoning-level
  settings can shift a model's *style* of output, not only its correctness,
  and at least one intermediate setting (medium, here) can still produce a
  structurally flawed result even when the highest setting does not.
  Recommend the guide caveat that reasoning-effort testing should check for
  both correctness and stylistic consistency across settings, not assume a
  monotonic quality improvement from low to high.
- **Ch09 (Source Evaluation / Evidence Standards)**: This source is a useful
  worked example for a guide passage on how to weigh benchmark claims by
  provenance: a WeChat-leak-via-deleted-Reddit-post-via-HN-ASCII-table
  relay (Claim 5) should be treated categorically differently from a named
  third-party evaluator's own published leaderboard (contrast with
  `blog-latentspace-ainews-qwen38-max-27b-launch.md` Claim 6's Vals AI
  figures, or `blog-latentspace-ainews-field-guide-fable.md` Claim 7's
  Artificial Analysis figures) — both may end up cited in adjacent
  paragraphs of a digest or post, but only one is independently checkable.

## Extraction Notes

- **Fetch method**: The blog post was fetched via `curl` with a browser
  user-agent to obtain exact HTML (WebFetch's summarizing pass returned
  paraphrased content that did not preserve verbatim wording or the full
  image alt-text). All `Quote` fields for the post body and image alt-text
  were copied character-for-character from that HTML. The linked Hacker
  News discussion (item 49274600) was likewise fetched via `curl` to locate
  and quote comment 49275180 (the specific ASCII-table comment the blog
  post links to via its fragment `#49275180`) and the surrounding reply
  thread verbatim; HTML entities (`&#x27;`, `&#x2F;`) were decoded to plain
  characters (`'`, `/`) when transcribing quotes.
- **Sub-page followed**: One sub-page was followed per MINER.md §1's
  up-to-5 allowance — the Hacker News discussion thread the post links to
  for benchmark data. The Reddit post in that chain was not independently
  fetched, as the post itself states it was deleted by moderators; the
  linked URL was not re-checked for this note beyond confirming it is
  present as a citation in the HN comment.
  The `tools.simonwillison.net/markdown-svg-renderer` gist links (used to
  render the pelican SVGs interactively) and the Qwen3.8-Max blog link
  referenced by an HN commenter were not separately fetched — they support
  claims already covered via the image alt-text (Claim 4) and the existing
  `blog-latentspace-ainews-qwen38-max-27b-launch.md` note (Claim 7),
  respectively.
- **Prospector guidance followed with one deviation**: three triage
  comments on the issue gave differing recommendations on the pelican
  reasoning-level observation — two urged skipping it as duplicative of the
  July Flash note's reasoning-effort finding, one urged extracting it as
  "genuinely novel... if repeatable." This note extracts it (Claims 3-4)
  but explicitly distinguishes it from the July note's finding (a
  *stylistic* variance claim, not a repeat of the *correctness* variance
  already documented in `blog-simonwillison-deepseek-v4-flash-0731.md`
  Claim 7), so a reader comparing the two notes side-by-side can see they
  are not redundant.
- **Source is thin**: the post itself is roughly 120 words of original
  prose. To reach a substantive claim count without padding, this note
  follows the linked Hacker News discussion (per MINER.md §1) for the
  benchmark-relevant claims (5-9), consistent with the Prospector's
  standing "key question" about whether quantitative benchmarks exist for
  this checkpoint — they do exist, but only as an unverifiable leak, which
  this note documents as precisely as possible while repeatedly flagging
  that provenance limitation rather than letting it fade into the
  background after the first mention.
- **Confidence rationale**: rated `anecdotal` overall. Claims 1-2 (launch
  channel, open-weights spec) are `settled` — directly observed/linked
  facts. Claims 3-4 (reasoning-level pelican variance) and 5-9 (the entire
  benchmark-provenance thread) are all `anecdotal` — a single practitioner's
  single test, or an unverified multi-hop leak and commenters' own
  arithmetic on top of it. Because the numerically interesting content
  (Claims 6-9) is concentrated in the weakest-provenance tier, the
  note-level rating reflects that weighting rather than the stronger
  confidence of Claims 1-2 alone.
- No contradictions filed per MINER.md §4a; one discrepancy considered and
  explicitly not filed, with reasoning documented in Cross-References →
  Contradicts.
