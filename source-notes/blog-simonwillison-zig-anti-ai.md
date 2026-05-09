---
source_url: https://simonwillison.net/2026/Apr/30/zig-anti-ai/
source_type: blog-post
title: "The Zig project's rationale for their firm anti-AI contribution policy"
author: Simon Willison (linking to and summarizing Loris Cro / Zig Software Foundation)
date_published: 2026-04-30
date_extracted: 2026-05-09
last_checked: 2026-05-09
status: current
confidence_overall: anecdotal
issue: "#569"
---

# The Zig project's rationale for their firm anti-AI contribution policy

> Simon Willison documents Zig's explicit code-of-conduct ban on LLM contributions,
> explains the "contributor poker" philosophy behind it (investing in people, not PRs),
> and surfaces the real-world cost: Bun's Zig fork achieved a 4x compilation speedup
> that cannot be upstreamed under the policy.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog — a curated trusted-feed source in
  this repo. Willison aggregates and comments on LLM/AI tooling developments; this
  post links to and summarizes Loris Cro's standalone essay "Contributor Poker and
  Zig's AI Ban" at kristoff.it, plus the Zig code of conduct and Bun's public
  statements.)
- **Author credibility**: Simon Willison is one of the highest-signal commentators
  on LLM tooling in the developer community (Django co-creator; runs the `llm` CLI
  project; prolific practitioner blogger). His role here is curator and analyst, not
  primary source. The primary source on rationale is Loris Cro, VP of Community at
  the Zig Software Foundation — the most authoritative voice on Zig's contributor
  policy. The Bun evidence is from Bun's own public statements (tweets, paywalled
  at extraction time) and a Ziggit forum thread with response from mlugg, a Zig
  core contributor.
- **Scope**: Covers Zig's LLM contribution ban, Loris Cro's "contributor poker"
  rationale, the Bun fork case study (4x compilation speedup, no-upstream decision),
  and brief Willison commentary. Does NOT cover: LLM use for internal development
  (only external contributions), Zig's technical architecture, or quantitative data
  on contributor growth.

## Extracted Claims

### Claim 1: Zig's code of conduct explicitly bans LLMs from issues, pull requests, and bug tracker comments

- **Evidence**: The Zig Software Foundation's published code of conduct at
  ziglang.org/code-of-conduct/, verified directly. Policy covers three distinct
  contribution surfaces and is enforced by Andrew Kelley and Loris Cro.
- **Confidence**: settled
- **Quote**: "No LLMs for issues. No LLMs for pull requests. No LLMs for comments
  on the bug tracker, including translation." (verbatim from ziglang.org/code-of-conduct/)
- **Our assessment**: This is one of the clearest and most explicit AI contribution
  policies in a major open-source project. The "including translation" clause is
  notable — it closes the loophole of using an LLM as a translation assistant for
  non-English speakers. The policy applies to the bug tracker communication layer,
  not just code itself, which is broader than most AI-use policies seen in engineering
  orgs.

### Claim 2: The rationale for the ban is "contributor poker" — investing in contributor relationships rather than individual PRs

- **Evidence**: Loris Cro's essay "Contributor Poker and Zig's AI Ban" (kristoff.it),
  cross-referenced via Willison's post and the Lobsters discussion thread. This is
  Cro's direct articulation of Zig's philosophy, not a third-party characterization.
- **Confidence**: anecdotal (single organization's explicit philosophy, stated by the
  VP of Community — authoritative for that org, but anecdotal as a general principle)
- **Quote**: "In contributor poker, you bet on the contributor, not on the contents
  of their first PR." (verbatim from kristoff.it/blog/contributor-poker-and-ai/)
- **Our assessment**: This is the most philosophically coherent rationale for an AI
  contribution ban we have seen documented publicly. It reframes the question: not
  "is this code good?" but "does reviewing this PR develop a person I can invest in?"
  LLM PRs are rejected because they are a one-shot game — the reviewer's time buys
  no relationship equity. The framing is directly applicable to code review philosophy
  in any team or community, not only OSS.

### Claim 3: The contributor poker model treats each PR as an opportunity to develop a long-term trusted contributor, and LLM use breaks this feedback loop

- **Evidence**: Loris Cro's essay; corroborated by the Lobsters discussion thread
  (126 comments, 212 upvotes), which confirms the framing is understood and debated
  by the broader OSS community.
- **Confidence**: anecdotal
- **Quote**: "you play the person, not the cards" (verbatim from
  kristoff.it/blog/contributor-poker-and-ai/)
- **Our assessment**: The poker metaphor is precise: in poker, you fold or bet based
  on your read of the *opponent*, not just the cards dealt. Cro applies this to OSS
  review: you accept or reject based on your read of the *contributor's potential*,
  not just the PR diff. LLM contributions remove the signal about the contributor —
  there may be no persistent contributor behind the PR at all, or the contributor
  may have bypassed the learning process that makes them a future asset. This is a
  different objection from "AI code is bad quality"; it persists even when AI code
  is perfect.

### Claim 4: The overwhelming majority of actual LLM-based contributions to Zig before the ban were low quality

- **Evidence**: Loris Cro's direct observation from reviewing contributions to the
  project. "Worthless drive-by PRs full of hallucinations" and "insane 10 thousand
  line long first time PRs" are cited as concrete examples.
- **Confidence**: anecdotal (first-person observation from a maintainer; no formal
  count or audit cited)
- **Quote**: "this is clearly a misuse of the tool, but it is also what the
  overwhelming majority of LLM-based contributions looked like for our project"
  (verbatim from kristoff.it/blog/contributor-poker-and-ai/)
- **Our assessment**: This is important context: the ban is not purely philosophical.
  Zig maintainers observed a real volume of low-quality AI contributions before
  codifying the ban. The policy is both a pre-emptive philosophical stance (contributor
  poker) and a reactive response to observed experience. The Lobsters thread notes
  that this "overwhelmingly negative" majority may not generalize to other projects —
  Zig's code complexity and contributor expectations are unusually high.

### Claim 5: Even when AI contributions are technically good, it is irrational (under contributor poker) to invest in them while high-quality human contributors are available

- **Evidence**: Loris Cro's reasoning in his essay, applied to Zig's specific context
  (an active contributor pool, strong demand for maintainer time).
- **Confidence**: anecdotal
- **Quote**: "from the perspective of contributor poker it's simply irrational for
  us to bet on LLM users while there's a huge pool of other contributors that don't
  present this risk factor" (verbatim from kristoff.it/blog/contributor-poker-and-ai/)
- **Our assessment**: This is the sharpest edge of the argument: it is not "AI code
  is bad" but "our review time has a higher-return use." In an under-resourced project
  with a small maintainer team and a large contributor pool, the opportunity cost of
  reviewing AI PRs is real. The argument weakens if the contributor pool is thin or
  if the AI-assisted code solves a problem that no human contributor is addressing.
  Cro explicitly acknowledges this is a rational risk assessment, not a blanket
  rejection of AI tools for development.

### Claim 6: Bun (Zig-based JavaScript runtime, Anthropic-owned) achieved a 4x compilation speedup in its own Zig fork but will not upstream due to Zig's AI ban

- **Evidence**: Bun's own public statements (tweets at x.com/bunjavascript, paywalled
  at extraction time); Willison's article which summarizes Bun's position; GitHub
  compare link between Bun's upgrade-0.15.2 and upgrade-0.15.2-fast branches
  (github.com/oven-sh/zig/compare/...).
- **Confidence**: emerging (Willison's characterization of Bun's position is credible;
  Bun's direct statements were inaccessible due to X paywall; the GitHub branch
  comparison is publicly verifiable)
- **Quote**: (no direct quote from Bun's tweets; Willison's article states Bun cited
  "a strict ban on LLM-authored contributions" as the reason for not upstreaming —
  see Extraction Notes)
- **Our assessment**: This is the most concrete evidence of the ban's real-world
  engineering cost. Bun joined Anthropic in December 2025 — an AI company — and uses
  AI assistance for its own development work. The fact that AI-assisted improvements
  in Bun's fork cannot flow back to the upstream project is a concrete opportunity
  cost on both sides. However, see Claim 7 for the Zig core team's separate technical
  objection, which suggests the AI ban may not be the only or even primary barrier.

### Claim 7: A Zig core contributor cites engineering correctness — not the AI ban — as the actual technical barrier to upstreaming Bun's changes

- **Evidence**: Ziggit forum post #19 in the "Bun's Zig fork got 4x faster compilation
  times" thread, attributed to mlugg, a Zig core contributor. Direct quotes from the
  post, verified via WebFetch of the Ziggit thread.
- **Confidence**: emerging (single forum post from a named Zig core contributor;
  technically detailed and specific; internally consistent with known Zig design
  philosophy around determinism)
- **Quote**: "implementing this feature correctly has implications not only for the
  compiler implementation, but for the Zig language itself!" and "their parallelized
  semantic analysis implementation _will_ exhibit non-deterministic behavior. That's
  pretty much a non-starter for most serious developers" (verbatim from ziggit.dev
  thread /t/bun-s-zig-fork-got-4x-faster-compilation-times/15183/19)
- **Our assessment**: This is a significant nuance that Willison's article does not
  surface. The Zig core team's objection to Bun's fork changes appears to be
  *engineering correctness* (non-deterministic behavior from parallel semantic analysis,
  fundamental language design implications) rather than the AI contribution ban.
  Mlugg additionally asserts that "There's the 4x speedup claimed by the Bun team,
  already available on Zig 0.16.0!" — suggesting Zig's own approach (self-hosted
  x86_64 backend, incremental compilation) achieves the same performance without
  the parallel-analysis approach. These two explanations are not mutually exclusive —
  Bun may cite the AI ban while the Zig team has separate technical objections —
  but the framing in Willison's article (AI ban = the barrier) is incomplete.

### Claim 8: The Zig policy may exclude technically strong contributors who use AI tools responsibly and would not disclose usage

- **Evidence**: Lobsters discussion thread (212 upvotes, 126 comments) on Cro's essay;
  Cro's own acknowledgment of the nuance in his essay.
- **Confidence**: anecdotal
- **Quote**: (no direct quote captures this claim verbatim; see Our assessment for the
  synthesized critique from the Lobsters discussion)
- **Our assessment**: The Lobsters discussion surfaces the sharpest objection to
  contributor poker as a policy: "Top performers increasingly use AI tools; banning
  them could exclude valuable contributors. The rule cannot effectively filter
  low-quality contributions from people ignoring guidelines anyway." A high-performing
  developer who uses AI to polish their contribution but discloses usage will be
  excluded; one who uses AI without disclosing cannot be distinguished from a
  high-performer who did not. Cro's response is that the expected-value calculation
  still favors the ban given the contributor pool, but this is a live debate. For
  teams applying the contributor poker logic internally (not in an OSS context), this
  objection is sharper: excluding internal engineers who use AI responsibly is a
  very different decision than filtering external OSS contributors.

### Claim 9: Simon Willison finds the "contributor poker" rationale compelling, particularly the insight that maintainers might prefer solving problems themselves with LLMs rather than reviewing AI-generated PRs

- **Evidence**: Willison's own commentary in the blog post.
- **Confidence**: anecdotal (one practitioner's reaction)
- **Quote**: "Zig values contributors over their contributions" (attributed to Willison's
  characterization in the article; see Extraction Notes on verbatim confidence)
- **Our assessment**: Willison's endorsement is worth noting because he is himself a
  prolific AI tool user (he maintains the `llm` CLI, writes extensively about LLM
  usage). His finding the Zig rationale "compelling" — from a pro-AI-adoption position —
  suggests the contributor poker argument has cross-ideological traction. The insight
  he highlights: if AI can write the code, the maintainer can also use AI to write
  the code themselves, and skip the review overhead entirely. This reframes LLM
  contributions as competition for maintainer attention rather than a gift of free code.

## Concrete Artifacts

### Zig Software Foundation Code of Conduct — AI/LLM Policy (verbatim excerpt)

```
Source: https://ziglang.org/code-of-conduct/
Extracted: 2026-05-09

"No LLMs for issues. No LLMs for pull requests. No LLMs for comments on
the bug tracker, including translation."

Enforcement contacts:
  Andrew Kelley (andrew@ziglang.org)
  Loris Cro (loris@ziglang.org)

Scope: Codeberg, IRC (Libera.chat), Zulip spaces
```

### Loris Cro's "Contributor Poker" Framework (verbatim key passages)

```
Source: Loris Cro, https://kristoff.it/blog/contributor-poker-and-ai/
Role: VP of Community, Zig Software Foundation
Extracted: 2026-05-09

Core thesis:
  "In contributor poker, you bet on the contributor, not on the contents
  of their first PR."

Summary metaphor:
  "you play the person, not the cards"

On LLM contributions specifically:
  "from the perspective of contributor poker it's simply irrational for
  us to bet on LLM users while there's a huge pool of other contributors
  that don't present this risk factor"

On the observed quality of actual LLM contributions:
  "this is clearly a misuse of the tool, but it is also what the
  overwhelming majority of LLM-based contributions looked like for
  our project"
```

### Ziggit Forum: mlugg's (Zig Core Contributor) Technical Objections to Bun's Fork

```
Source: ziggit.dev/t/bun-s-zig-fork-got-4x-faster-compilation-times/15183/19
Author: mlugg (Zig core contributor)
Extracted: 2026-05-09

On the parallel semantic analysis approach:
  "implementing this feature correctly has implications not only for the
  compiler implementation, but for the Zig language itself!"

On determinism:
  "their parallelized semantic analysis implementation _will_ exhibit
  non-deterministic behavior. That's pretty much a non-starter for
  most serious developers"

On whether the speedup is actually novel:
  "There's the 4x speedup claimed by the Bun team, already available
  on Zig 0.16.0!"

  (Via self-hosted x86_64 backend instead of LLVM + incremental
  compilation, which achieves ~300x faster rebuilds in demonstrated
  scenarios)
```

### Linked Resources (for Assayer verification)

```
Zig code of conduct:     https://ziglang.org/code-of-conduct/
Loris Cro's essay:       https://kristoff.it/blog/contributor-poker-and-ai/
Lobsters discussion:     https://lobste.rs/s/ifcyr1/contributor_poker_zig_s_ai_ban
Bun joins Anthropic:     https://bun.com/blog/bun-joins-anthropic
Bun fork compare:        https://github.com/oven-sh/zig/compare/upgrade-0.15.2...upgrade-0.15.2-fast
Bun tweet 1:             https://x.com/bunjavascript/status/2048427636414923250 (paywalled)
Bun tweet 2:             https://x.com/bunjavascript/status/2048428104893542781 (paywalled)
Ziggit thread:           https://ziggit.dev/t/bun-s-zig-fork-got-4x-faster-compilation-times/15183/19
```

## Cross-References

- **Corroborates**: `blog-ronacher-content-for-contents-sake.md` Claim 5 ("Existing
  text-based infrastructure systems are failing under AI-generated content flooding")
  and Claim 10 ("Platforms accepting text submissions need friction and 'backpressure'
  mechanisms against AI-generated content flooding"). Ronacher documents AI content
  flooding and argues for backpressure mechanisms in general; Zig's explicit ban is
  the strongest example of applied backpressure in an OSS contribution context. Both
  sources identify the same asymmetric-cost structure: AI generation is cheap for
  the sender, expensive to evaluate for the receiver.

- **Corroborates**: `blog-ronacher-content-for-contents-sake.md` Claim 7 ("Some
  AI-generated content reaches recipients accidentally, without the sender's
  knowledge or intent"). Zig's "including translation" clause in the LLM ban suggests
  awareness that AI can mediate contributions below the contributor's explicit
  awareness — consistent with Ronacher's Pi GitHub examples.

- **Contrasts (not contradicts)**: `blog-bvp-shopify-ai-playbook.md` Claim 3
  ("Shopify does not allow AI to commit code automatically; senior human review
  remains mandatory"). Both examples show a major tech organization maintaining
  human control points over AI. The contrast is context: Shopify's policy is
  permissive for internal development (AI assists, human commits) while Zig's policy
  is prohibitive for external contribution (AI involvement = rejection). These are
  different domains (internal engineering culture vs. OSS contribution governance)
  and are not in contradiction.

- **Novel**:
  - **"Contributor poker" as a named, philosophical framework for OSS contribution
    governance**: No other corpus source articulates an explicit philosophy of
    contributor relationship investment as the primary reason to accept or reject
    PRs. The framing is distinct from code-quality review, security review, or
    scope management.
  - **Principled rejection of AI contributions by a high-profile OSS project with
    detailed public rationale**: Other corpus sources address AI adoption strategy
    for teams building with AI; this is the first corpus source documenting a major
    project's structured case for not accepting AI-generated code from external
    contributors.
  - **The AI-ban vs. engineering-correctness distinction in the Bun/Zig case**: The
    Ziggit forum reveals that the commonly cited reason (AI ban blocks upstreaming)
    may coexist with or be secondary to a technical correctness objection (parallel
    semantic analysis causes non-deterministic behavior). This split between policy
    and engineering justification for the same rejection is a novel complexity.
  - **Bun as the concrete cost of the policy**: Bun (an Anthropic-owned project)
    achieving performance improvements it cannot contribute upstream is the most
    concrete engineering cost documented for an AI contribution ban in our corpus.

## Guide Impact

- **Chapter 02 (when and where to adopt AI-native approaches)**: Add this as a
  structured counterexample to the assumption that more AI assistance = better
  outcomes. The guide should distinguish between AI assistance for internal
  development (where Zig itself presumably uses whatever it wants) and AI use in
  external contribution contexts (where the relationship dynamics and community
  investment logic apply). Recommend adding a callout: "Deliberate non-adoption as
  a strategic choice" — with Zig as the primary case study.

- **Chapter 04 (organizational patterns)**: The "contributor poker" framework is
  directly applicable to any team thinking about its contribution review process —
  not just OSS. Teams that review AI-generated code from contractors, interns, or
  junior developers face an analogous trade-off: does reviewing AI-polished PRs from
  someone who doesn't understand the code develop the contributor, or just consume
  reviewer time? The guide should surface this as an organizational design question
  for teams running AI-augmented onboarding or mentoring.

- **Chapter 02 or 04 — Bun/Zig fork as a supply-chain fragmentation case**: The
  Bun fork maintaining divergent AI-assisted changes that cannot rejoin upstream is
  a new pattern. As AI-native teams fork and improve foundational OSS components
  using AI assistance, they risk permanent divergence from upstream if those upstreams
  adopt AI bans. Guide should note this as an emerging supply-chain fragmentation
  risk for teams building on AI-ban-policy upstreams.

## Extraction Notes

- Primary article at simonwillison.net/2026/Apr/30/zig-anti-ai/ was fetched but
  verbatim content was limited by the WebFetch tool's copyright compliance. Key
  quotes attributed to the article are best-effort from the tool's output; the most
  reliable quotes are those verified against linked primary sources (Zig CoC and
  Loris Cro's essay).
- The Zig code of conduct quote ("No LLMs for issues...") was verified verbatim
  against ziglang.org/code-of-conduct/ directly.
- Loris Cro quotes were verified verbatim against kristoff.it/blog/contributor-poker-and-ai/
  directly.
- Bun tweets (x.com/bunjavascript/status/2048427636414923250 and /2048428104893542781)
  returned HTTP 402 (X paywall) at extraction time. Bun's stated position on not
  upstreaming is mediated through Willison's article summary.
- Ziggit forum post at /15183/19 (mlugg's technical response) was fetched and
  quotes are verbatim from that post. This is the primary evidence for Claim 7
  (engineering objection distinct from AI ban).
- The Lobsters discussion thread (lobste.rs/s/ifcyr1/...) was fetched and
  summarized; quotes from the discussion are paraphrased in Our assessment sections,
  not presented as verbatim.
- Confidence rated anecdotal overall: core claims about the contributor poker
  philosophy come from a single organization's VP articulating their own policy.
  The claims are internally consistent and supported by corroborating evidence
  (actual policy text, real-world cost case), but this is one project's experience
  and philosophy, not a studied or validated framework.
