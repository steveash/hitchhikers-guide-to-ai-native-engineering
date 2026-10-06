---
source_url: https://simonwillison.net/2026/Sep/29/openai-devday-2026-live-blog/
source_type: blog-post
title: "OpenAI DevDay 2026 live blog"
author: Simon Willison
date_published: 2026-09-29
date_extracted: 2026-10-06
last_checked: 2026-10-06
status: current
confidence_overall: emerging
issue: "#3923"
---

# OpenAI DevDay 2026 live blog

> Simon Willison's timestamped, first-hand notes from OpenAI DevDay 2026 cover the Dots personal-agent launch, GPT-6.1 Sol and Ultrafast pricing, Codex Security's "Defense Factory" sprint numbers (36% duplicates, 1% rollback), and closing-Q&A remarks on agent autonomy and "outcome per dollar".

## Source Context

- **Type**: blog-post (live blog)
- **Author credibility**: Simon Willison is a widely read independent LLM tooling commentator who attended in person (OpenAI gave him a free ticket and a "creator" area seat, which he discloses). Entries are real-time notes with candid commentary.
- **Scope**: Keynote, a ChatGPT Sites session, a Codex Security session, a GPT-Live session and the closing Q&A. Vendor claims are relayed secondhand from the stage, not independently verified. Terse one-line entries; several items are screenshots/videos not captured in text.

## Extracted Claims

### Claim 1: OpenAI's Dots agents are positioned around a user-controlled delegation model ("as much responsibility as you are comfortable with")
- **Evidence**: Keynote statement (Altman) and closing Q&A answer (Brown); no technical detail on the mechanism.
- **Confidence**: anecdotal
- **Quote**: "Sam called Astra "our most aligned model", to allow you to trust your Dot with "as much responsibility as you are comfortable with"."
- **Our assessment**: Delegation scope as a user-set dial matches the "autonomy proportional to trust" pattern already in the corpus, but here it is a marketing statement with no mechanism disclosed. Treat as vendor direction.

### Claim 2: Dots do not get default access to everything the user has shared with ChatGPT; access is granted incrementally
- **Evidence**: Answer to a Q&A question about when agents should act versus check in.
- **Confidence**: anecdotal
- **Quote**: "Thibault: dots don't have access by default to everything you have shared with ChatGPT already."
- **Our assessment**: A least-privilege default is a sound pattern; the live blog does not say how scopes are expressed or enforced.

### Claim 3: Agents get their own identities in team tools (Slack) and shared Spaces for human+agent collaboration
- **Evidence**: Demo of "Dottie" with access to ChatGPT, Slack, Teams; OpenAI staff delegating to Dots in Slack. Willison compares it to Claude Tag.
- **Confidence**: emerging
- **Quote**: "People at OpenAI started delegating to their Dots directly in Slack, which have their own identities in OpenAI Slack."
- **Our assessment**: Independent convergence with Anthropic's agent-as-teammate design (see Cross-References). Two vendors shipping the same shape raises confidence in the pattern.

### Claim 4: Dots emerged from the Codex harness becoming more reliable on longer tasks
- **Evidence**: Statement by Thibault Sottiaux in the closing Q&A.
- **Confidence**: anecdotal
- **Quote**: "Thibault talks about how dots came out of the Codex harness getting more reliable and being able to handle longer tasks."
- **Our assessment**: Suggests general-purpose agents are being built on coding-agent harnesses. Note the triage comment's "10%→35% success on 8-16 hour tasks" figure does NOT appear in this post; do not attribute it here.

### Claim 5: GPT-6.1 Sol claims near-Astra intelligence at a fifth of the price; Ultrafast offers 8x speed at 6x price
- **Evidence**: Keynote slides as relayed by Willison; no benchmarks in the post.
- **Confidence**: anecdotal
- **Quote**: ""Near-Astra level intelligence at a fifth of the price"."
- **Our assessment**: A concrete tiering datapoint (capability vs. price vs. speed), but unverified; check against OpenAI's own GPT-6.1 Sol post before the guide cites numbers.

### Claim 6: Ultrafast inference (up to 300 tokens/s) is priced at a premium that OpenAI argues is worth it, and was credited with enabling a large merge project
- **Evidence**: Keynote pricing; Thibault claim about merging desktop apps.
- **Confidence**: anecdotal
- **Quote**: "Ultrafast: 8x faster - up to 300 tokens/second. Available in the API, ChatGPT, and Codex. 6x the price of standard - "you know what, it's worth it" says Sam."
- **Our assessment**: Quote is the source's own text for this entry. Latency-for-cost trading is a real design axis for agent loops; the 28-day merge claim is unsubstantiated self-report.

### Claim 7: Decisions API constrains a small model to a predefined option set to get sub-second responses
- **Evidence**: Preview announcement; Willison links it to the Jev decision-model category.
- **Confidence**: emerging
- **Quote**: "It works by giving the Luna model "a predefined set of options to choose from"."
- **Our assessment**: Corroborates the "decision/classifier model as agent routing component" pattern in existing Jev notes.

### Claim 8: OpenAI used its own models to optimize the Computer Use harness, yielding a 2x latency win
- **Evidence**: Tejal Patwardhan keynote remarks; no measurement methodology.
- **Confidence**: anecdotal
- **Quote**: ""Our models helped optimize the harness we use for Computer Use"."
- **Our assessment**: Model-assisted harness optimization is an interesting recursive-improvement datapoint; the 2x figure is unverified. Also notes WebMCP being "much more efficient than using Computer Use" (13:01), another vendor-side claim.

### Claim 9: OpenAI's internal security sprint ("The Defense Factory") fixed 53 critical findings on day one, with 36% duplicate discoveries and a 1% rollback rate for generated patches
- **Evidence**: Kyle Brown / Ian Webster session figures relayed by Willison.
- **Confidence**: emerging
- **Quote**: "In their internal sprint 36% of the discoveries were duplicates. Eliminating these saved a lot of developer time."
- **Our assessment**: Specific, operational numbers (dedup rate, rollback rate) are more useful than typical security-agent marketing. Still vendor-reported. Also: "fixed 53 critical findings on the first day" and "only had a 1% rollback rate, thanks to a verify-fix command, which you can think of as an adversarial agent against the fix."

### Claim 10: Security-agent autonomy was introduced as a dial turned up gradually; scanner loops until exhaustion and uses SECURITY.md plus a knowledge base
- **Evidence**: Session description of Codex Security.
- **Confidence**: emerging
- **Quote**: "Over time they got to the point where the system could generate patches. This was more of a "dial you turn up" as you get more comfortable with the quality of the results."
- **Our assessment**: Strong corroboration of staged autonomy. SECURITY.md as a product-owner-authored threat model parallels AGENTS.md/CLAUDE.md-style context files.

### Claim 11: Ownership attribution was a hard problem in agent-driven remediation
- **Evidence**: Session remark.
- **Confidence**: anecdotal
- **Quote**: "They put a lot of work into figuring out who owned what - a surprisingly hard problem in a company growing at OpenAI's rate."
- **Our assessment**: Practical lesson: routing findings to owners is a bottleneck separate from detection.

### Claim 12: OpenAI leaders expect agent-choice "decision fatigue" (subagents, reasoning level) to be absorbed by smarter systems, and frame cost as "outcome per dollar"
- **Evidence**: Closing Q&A.
- **Confidence**: anecdotal
- **Quote**: "Thibault says me thinks people are hitting decision fatigue over when to use subagents, what reasoning level to make."
- **Our assessment**: Signals vendor intent to automate model/effort routing. Also "Likes to see people talk about "outcome per dollar"" is useful for Ch03 economics framing.

### Claim 13: Delegating from a low-latency voice agent to a stronger background model is an emerging architecture
- **Evidence**: GPT-Live demo where GPT-Live kept interacting while Astra wrote code to draw images.
- **Confidence**: anecdotal
- **Quote**: "This was a demonstration of delegation, where a more powerful model ran the drawing while GPT-Live continues to listen and interact."
- **Our assessment**: Fast-front-model/slow-back-model split; single demo.

### Claim 14: Product reliability gaps remain visible: live demos failed and the Dots signup link told the author to switch to desktop
- **Evidence**: Willison's first-hand observations (10:13, 11:32, 16:32).
- **Confidence**: anecdotal
- **Quote**: "Live demo! "Dottie is having a slow morning" - we got a "still checking" and an embarrassing silent moment."
- **Our assessment**: Small but honest counterweight to keynote claims; not a failure report in itself.

## Concrete Artifacts

```
Simon Willison live blog, 10:23 / 10:21 / 10:22 (pricing and tiers):
- GPT-6.1 Sol: "Near-Astra level intelligence at a fifth of the price"
- Ultrafast: 8x faster, up to 300 tokens/second, 6x price of standard; Astra 6 today, Sol 6.1 soon
- New plan "Pro 500": Ultrafast access, 25x the usage of Plus; $200/month plan back on sale
```

```
Codex Security session figures (13:33-13:45):
- Security sprint: quarter of product engineers; 53 critical findings fixed day one
- 36% of discoveries duplicates
- 1% rollback rate with `verify-fix` (adversarial agent against the fix)
- Commands named: codex-security patch (generates patches and opens PRs), verify-fix, dedup workflow in CLI
- Inputs: security knowledge base + SECURITY.md per product owner
```

```
ChatGPT Sites (12:47-12:54): 8m sites hosted; 70% of OpenAI employees make their own; SQLite database per Site; scheduled tasks; Sign in with ChatGPT; default private; editor role.
```

## Cross-References

- **Corroborates**: `blog-anthropic-claude-tag-employee-workflows.md` and `blog-anthropic-human-agent-teams.md` (Claim 2: persistent memory, independent credentials; Claim 9: autonomy proportional to demonstrated reliability) — Dots with own Slack identity and incremental responsibility mirror these. `blog-simonwillison-jev-decision-models.md` — Decisions API restricts a model to predefined options, same shape as Jev.
- **Contradicts**: None found. No claim materially opposes an existing note, so no contradiction issue was filed.
- **Extends**: `blog-openai-astra-safety-overview.md` (Astra safety/alignment framing; here "most aligned model" is used to justify delegation) and the Cursor/Cognition security-agent notes (`blog-cursor-security-agents.md`, `blog-cognition-devin-security-vulnerability-remediation-program.md`) with OpenAI's sprint metrics.
- **Novel**: Dots product pattern; ChatGPT Space; Ultrafast 6x-price speed tier; Defense Factory dedup/rollback numbers; "Sign in with ChatGPT"; Plugins in Sites; SECURITY.md as threat-model input.

## Guide Impact

- **Chapter 02**: Add Dots and Claude Tag as two vendors converging on named, identity-bearing agents in team chat with scoped, expandable access (Claims 1-3). Cite Defense Factory as an example of staged autonomy ("dial you turn up") with an adversarial verifier (Claims 9-10).
- **Chapter 03**: Add GPT-6.1 Sol / Ultrafast as a price-speed-capability datapoint, flagged as vendor-stated and pending verification against OpenAI's primary post (Claims 5-6); "outcome per dollar" framing (Claim 12).
- **Chapter 05**: Add Codex Security operating practices: dedup, ownership mapping, SECURITY.md threat models, verify-fix, rollback rate as a metric (Claims 9-11).

## Extraction Notes

- Fetched the full page HTML and read every entry; there are no sub-pages. Quotes were copied from the page text; the entry prefix timestamps were omitted. Claim 9 and Claim 12 include second quotes inline in the assessment, copied from the same entries.
- Triage listed "10%→35% success rate on 8-16 hour tasks" and "Computer Use 2x latency" as key questions; only the latter is in this post. The reliability figure is absent and must come from another source.
- Willison links OpenAI blog posts (GPT-6.1 Sol, Introducing dots, DevDay Recap) which were not followed; they are better primary sources for numbers.
- Screenshots and videos referenced in the post were not visible to text extraction.
