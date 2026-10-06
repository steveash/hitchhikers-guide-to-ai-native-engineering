---
source_url: https://simonwillison.net/2026/Sep/28/claude-sonnet-5-5/
source_type: blog-post
title: "Claude Sonnet 5.5"
author: Simon Willison
date_published: 2026-09-28
date_extracted: 2026-10-06
last_checked: 2026-10-06
status: current
confidence_overall: emerging
issue: "#3921"
---

# Claude Sonnet 5.5

> A short Willison link post on Sonnet 5.5's launch: Anthropic's speed/cost claims, a repeat of the Opus 5.5 "max" thinking-effort failure (128k tokens, $1.28, no output), and the observation that Sonnet 5.5 is now claude.ai's free-tier model, ahead of OpenAI's free tier.

## Source Context

- **Type**: blog-post (link post with commentary; ~250 words)
- **Author credibility**: Simon Willison runs systematic same-day model tests (pelican-on-a-bicycle SVG sweeps across thinking levels) and is a consistent, well-regarded LLM-tooling commentator. Evidence here is his own informal runs, not benchmarks.
- **Scope**: Anthropic's headline claims for Sonnet 5.5, one reasoning-effort sweep, one free-tier WebGL prompt, and a note on Haiku 5.5. Does NOT cover: pricing figures, benchmark numbers, context window, agentic/coding-harness testing, or methodology beyond a single prompt per setting.

## Extracted Claims

### Claim 1: Anthropic says Sonnet 5.5 is faster and cheaper than Sonnet 5 at the same list price
- **Evidence**: Anthropic's announcement (relayed by Willison); Willison infers it "should be cheaper to run" rather than measuring.
- **Confidence**: emerging (vendor claim, unmeasured here)
- **Quote**: "runs 30%+ faster, and costs up to 30% less for most work"
- **Our assessment**: Vendor claim with hedges ("up to", "most work"). Willison notes it is "priced the same as Sonnet 5", so savings come from token efficiency, not list price. Matches GitHub's qualitative "fewer steps, tokens, and tool calls" claim (docs-github-copilot-sonnet55-availability.md Claim 2), so two independent channels relay the same vendor story, but neither measures it.

### Claim 2: Sonnet 5.5 appears to beat Sonnet 5 on every benchmark
- **Evidence**: Willison's reading of Anthropic's announcement; no numbers given.
- **Confidence**: emerging
- **Quote**: "appears to beat it on every benchmark"
- **Our assessment**: Hedged ("appears"), second-hand. Useful only as direction of travel; do not cite as a measured result.

### Claim 3: Sonnet 5.5 reproduces the Opus 5.5 "max" thinking-effort failure: 128,000 tokens of reasoning, $1.28, no output
- **Evidence**: Willison's own pelican-SVG run at "max" effort; cross-linked to his earlier Opus 5.5 post.
- **Confidence**: anecdotal (single run reported, simple prompt)
- **Quote**: "the \"max\" thinking effort pelican thought for 128,000 tokens (at a cost of $1.28) before running out of tokens and failing to produce an SVG."
- **Our assessment**: Strong corroboration that the failure is a property of the "max" setting across the 5.5 family rather than a one-off. The Opus note records 2/2 failures at $2.56 each; here $1.28 for 128k tokens is exactly half the Opus per-run cost, consistent with Sonnet's lower output price (inference). Practical lesson: cap or test the top effort tier, and set budget limits, before defaulting to it.

### Claim 4: Sonnet 5.5 at "xhigh" produced a usable pelican for 5.74 cents in 41 seconds
- **Evidence**: Willison's run on the same prompt, contrasted with "max".
- **Confidence**: anecdotal
- **Quote**: "at a cost of 5.74 cents and taking 41 seconds"
- **Our assessment**: The contrast (~22x cheaper, successful) with "max" shows the step from xhigh to max adds cost and risk without a payoff on simple tasks. n=1 on a low-complexity prompt, so don't generalize to hard tasks.
  (Note: the triage comment gave "$0.057"; the post says 5.74 cents.)

### Claim 5: Sonnet 5.5 is almost as good as Opus 5.5 on some coding tasks
- **Evidence**: Willison's qualitative testing on "viral 3D animation tricks"; no scores.
- **Confidence**: anecdotal
- **Quote**: "Sonnet 5.5 appears to be almost as good as Opus 5.5 on some coding tasks"
- **Our assessment**: Supports routing everyday work to the cheaper tier, consistent with GitHub's "well-scoped everyday work" framing. The qualifier "some" matters; no long-horizon agent evidence is offered.

### Claim 6: Sonnet 5.5 is now claude.ai's free-tier model, giving Anthropic a much more capable free offering than OpenAI's
- **Evidence**: Willison's statement of the product change and his comparison to ChatGPT's free-tier model.
- **Confidence**: emerging (product fact is checkable; "much more capable" is his judgment)
- **Quote**: "OpenAI's ChatGPT free tier uses Luna 5.6, which means Anthropic currently have a much more capable free offering."
- **Our assessment**: Free-tier model quality is now a competitive axis relevant to onboarding and learning. The capability gap is asserted, not benchmarked.

### Claim 7: The free tier can one-shot a decent 3D WebGL page
- **Evidence**: Willison ran a single prompt on the free tier and linked the result, calling it "a solid effort".
- **Confidence**: anecdotal
- **Quote**: "build me an HTML page that renders a three-dimensional pelican riding a bicycle using WebGL"
- **Our assessment**: A single demo, but a concrete capability floor for zero-cost users. Treat it as an existence proof, not a reliability measure.

### Claim 8: Haiku 5.5 is still pending and Willison hopes it will be price-competitive with GPT-6 Luna
- **Evidence**: Anthropic's announcement reiterating "in the coming weeks"; Willison's stated hope.
- **Confidence**: anecdotal
- **Quote**: "I really hope that one is price-competitive with GPT-6 Luna!"
- **Our assessment**: Extends the price-war thread: the cheap-model tier is where Anthropic is seen as lagging (see Cross-References). Forward-looking; revisit when Haiku 5.5 ships.

## Concrete Artifacts

```
Prompt (free tier, claude.ai), per Willison:
build me an HTML page that renders a three-dimensional pelican riding a bicycle using WebGL

Reported runs (Willison, pelican SVG, Sonnet 5.5):
- thinking effort "max":   128,000 tokens, $1.28, ran out of tokens, no SVG
- thinking effort "xhigh": 5.74 cents, 41 seconds, SVG produced
```

## Cross-References

- **Corroborates**: `blog-simonwillison-opus55-gpt6-sol-luna-price-war.md` Claim 9 (Opus 5.5 "max" hits the 128,000 output-token cap) and Claim 10 (max effort effectively unusable); `docs-github-copilot-sonnet55-availability.md` Claim 2 (efficiency of 5.5 vs 5 with fewer tokens) and Claim 1 (positioning for everyday work).
- **Contradicts**: None found. No contradiction issue filed.
- **Extends**: `blog-simonwillison-opus55-gpt6-sol-luna-price-war.md` Claim 12 (price war affects tiers below flagship; Haiku faces a price gap) and Claim 13 (Willison's defaults by model); `blog-simonwillison-gpt56-luna-price-drop.md` Claim 4 (Luna vs Haiku 4.5 pricing) by showing the Haiku 5.5 wait; `blog-simonwillison-2026-in-llms-so-far.md` for the broader 2026 context.
- **Novel**: The same "max" failure observed on a second model family member (Sonnet); the free-tier-as-competitive-axis framing (Sonnet 5.5 vs Luna on free tiers).

## Guide Impact

- **Chapter 02 (model selection)**: Add Sonnet 5.5 as the cost/speed tier with the caveat that its quality is "almost as good" as Opus 5.5 only on some coding tasks (Claim 5); cite the vendor speed/cost claims as vendor-reported (Claim 1).
- **Chapter 03 / effort settings**: Where the guide discusses reasoning-effort levels, add a caution that "max" has failed on both Opus 5.5 and Sonnet 5.5 by exhausting the 128k output cap with no answer (Claim 3, plus the Opus note), and recommend testing the top tier and enforcing budget caps before making it a default.
- **Chapter 04 (cost)**: Note that 5.5 savings come from token efficiency, not list price (Claim 1), and show the xhigh-vs-max cost contrast (Claim 4) as a worked example.
- **Free-tier / onboarding material**: One sentence that free-tier model quality now differs materially between vendors (Claim 6), flagged as Willison's judgment.

## Extraction Notes

- Read the full page (very short link post). No sub-pages followed; the linked Opus 5.5 post is already covered by an existing note, and the linked pelican/WebGL outputs are images or demos, not text.
- Quotes copied verbatim from the fetched HTML text; the backslashes before inner quotes in Claim 3 are only escaping of the post's own double quotes.
- The Prospector's "$0.057 per task" corresponds to the post's "5.74 cents".
- Source is thin; confidence is capped at emerging.
