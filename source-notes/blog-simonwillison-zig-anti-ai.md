---
source_url: https://simonwillison.net/2026/Apr/30/zig-anti-ai/
source_type: blog-post
title: "The Zig project's rationale for their firm anti-AI contribution policy"
author: Simon Willison (relaying Loris Cro, Zig Software Foundation VP of Community)
date_published: 2026-04-30
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#569"
---

# The Zig project's rationale for their firm anti-AI contribution policy

> Simon Willison covers Zig's explicit code-of-conduct ban on LLM contributions,
> grounding it in Loris Cro's "contributor poker" philosophy: open-source project
> reviewing is a long-term investment in people, not code, and LLM-assisted PRs
> break that investment loop even when the code is technically correct.

## Source Context

- **Type**: blog-post (Simon Willison's Weblog, a `trusted-feed` source)
- **Author credibility**: Simon Willison is one of the highest-signal commentators on
  LLM tooling. He is synthesizing and endorsing the argument of Loris Cro, VP of
  Community at the Zig Software Foundation, who wrote the original "Contributor Poker
  and Zig's AI Ban" essay at kristoff.it (also fetched; full text verified). Cro's
  position is institutional — he is speaking as a named officer of a major OSS
  foundation explaining a ratified policy.
- **Scope**: Covers the rationale for Zig's anti-LLM CoC policy, the "contributor
  poker" philosophy for OSS contributor development, the Bun/Zig fork case study
  (4x speedup blocked from upstreaming), and a Zig core contributor's independent
  technical explanation for why the patch wouldn't be accepted regardless of the AI
  ban. Does NOT cover AI productivity metrics in general, corporate AI adoption, or
  any empirical measurement of code quality.

## Extracted Claims

### Claim 1: Zig has an explicit, comprehensive ban on LLM-generated content in all official contribution channels

- **Evidence**: Verbatim text from Zig's published Code of Conduct at ziglang.org/code-of-conduct/.
  The policy covers issues, PRs, and all bug-tracker comments including translations.
- **Confidence**: settled (the CoC is a published institutional document)
- **Quote**: "No LLMs for issues. No LLMs for pull requests. No LLMs for comments on
  the bug tracker, including translation. English is encouraged, but not required. You
  are welcome to post in your native language and rely on others to have their own
  translation tools of choice to interpret your words."
- **Our assessment**: This is the most comprehensive AI contribution ban documented
  among major open-source projects. The inclusion of "translation" is notable — even
  using an LLM to translate your bug report into English is prohibited. The policy is
  not about code quality; it covers the entire communication surface of the project.

### Claim 2: Open-source reviewer time is better understood as a long-term investment in contributors, not an evaluation of individual PRs

- **Evidence**: Loris Cro's essay (kristoff.it/blog/contributor-poker-and-ai/), quoted
  directly in the Willison post. Cro is drawing on his experience as ZSF VP of Community.
- **Confidence**: anecdotal (practitioner argument, not measured study)
- **Quote**: "In successful open source projects you eventually reach a point where you
  start getting more PRs than what you're capable of processing. Given what I mentioned
  so far, it would make sense to stop accepting imperfect PRs in order to maximize ROI
  from your work, but that's not what we do in the Zig project. Instead, we try our
  best to help new contributors to get their work in, even if they need some help
  getting there. We don't do this just because it's the 'right' thing to do, but also
  because it's the smart thing to do."
- **Our assessment**: The core insight is that the "smart" reason — not just the ethical
  reason — to invest in imperfect PRs is the long-term contributor relationship they
  create. This reframes code review not as quality assurance but as talent development.
  Applies directly to how AI-native teams should think about onboarding junior engineers
  who lean heavily on AI tools.

### Claim 3: "Contributor poker" — the name for the OSS investment philosophy — frames the game as betting on people, not code

- **Evidence**: Loris Cro's own explanation of the name, quoted in the Willison post and
  confirmed verbatim in the original kristoff.it essay.
- **Confidence**: anecdotal (conceptual framing, not empirical)
- **Quote**: "The reason I call it 'contributor poker' is because, just like people say
  about the actual card game, 'you play the person, not the cards'. In contributor poker,
  you bet on the contributor, not on the contents of their first PR."
- **Our assessment**: The metaphor is precise and communicates something empirically
  important: the expected value of onboarding a contributor is front-loaded in the
  relationship (reviewer time, mentoring), and back-loaded in the contributor's later
  independent and trusted contributions. If the reviewer never learns anything about the
  human submitting the PR, the investment cannot pay off.

### Claim 4: LLM-assisted PRs break the contributor-development investment loop even when the code is technically correct

- **Evidence**: Loris Cro's argument, as summarized by Simon Willison in his own words.
- **Confidence**: anecdotal (logical argument from practitioner, not measured)
- **Quote**: "LLM assistance breaks that completely. It doesn't matter if the LLM helps
  you submit a perfect PR to Zig - the time the Zig team spends reviewing your work does
  nothing to help them add new, confident, trustworthy contributors to their overall
  project."
  *(Note: This passage is Willison's own paraphrase/summary in the article body, not a
  direct Cro quote — confirmed against the Willison source page.)*
- **Our assessment**: This is the crux of the policy and it is independent of code
  quality. Even a flawless LLM-generated PR fails the contributor-poker test because the
  reviewer learns nothing about the human. For AI-native teams, this raises a design
  question: what is the equivalent of "contributor poker" in an internal engineering
  context? If AI generates most of a junior's output, does the senior reviewer stop
  learning about that engineer's judgment?

### Claim 5: The ban is game-theoretically rational: it is irrational to bet on LLM contributors when there is a pool of non-LLM contributors available

- **Evidence**: Loris Cro's argument from the kristoff.it essay, confirmed verbatim.
- **Confidence**: anecdotal (logical argument, not empirical)
- **Quote**: "from the perspective of contributor poker it's simply irrational for us to
  bet on LLM users while there's a huge pool of other contributors that don't present
  this risk factor"
- **Our assessment**: This is the sharpest version of the argument. It does not claim
  LLM-assisted code is always worse; it claims that given a choice between two PRs of
  similar apparent quality, the one from a non-LLM contributor has higher expected future
  value. The argument depends on OSS projects having excess contributor supply — it would
  not apply to a team desperate for any code that compiles. Useful for the guide's
  discussion of when AI adoption creates genuine trade-offs vs. when it is unambiguously
  beneficial.

### Claim 6: Bun's Zig fork achieved a 4x compilation speedup using AI assistance but will not be upstreamed due to Zig's ban

- **Evidence**: Bun's own X/Twitter post relayed by Willison, plus Willison's description
  of the changes (parallel semantic analysis, multiple LLVM codegen units).
- **Confidence**: emerging (public announcement from Bun, technically plausible)
- **Quote**: "We do not currently plan to upstream this, as Zig has a strict ban on
  LLM-authored contributions."
- **Our assessment**: This is the most concrete case study in the article. Bun (acquired
  by Anthropic in December 2025, a company at the frontier of AI assistance) used AI
  tools to build something genuinely useful — a 4x speedup — and then explicitly
  declined to contribute it upstream because of the policy. The cost of the AI ban is
  real and specific: a meaningful performance improvement stays siloed in a fork. This is
  the engineering trade-off practitioners should understand, not a hypothetical.

### Claim 7: A Zig core contributor states the technical barrier to the Bun patch is independent of the AI ban — the parallel semantic analysis causes non-deterministic compilation

- **Evidence**: Post #19 by mlugg on ziggit.dev (linked from the Willison article as an
  update). Mlugg is identified as a Zig core contributor. The post contains detailed
  technical explanation with build benchmark data.
- **Confidence**: emerging (expert practitioner, but single source)
- **Quote**: "AI is entirely besides the point here. The changes in this Zig fork are not
  desirable to upstream for several reasons. [...] implementing this feature correctly has
  implications not only for the compiler implementation, but for the Zig language itself!
  [...] which means their parallelized semantic analysis implementation will exhibit
  non-deterministic behavior. That's pretty much a non-starter for most serious
  developers: you don't want your compilation to randomly fail with a nonsense error 30%
  of the time."
- **Our assessment**: This claim significantly complicates Claim 6. The AI ban and the
  engineering objection coexist but are independent. Bun's statement ("Zig has a strict
  ban") is accurate but incomplete — even if the ban did not exist, the patch has
  technical problems that the Zig team would reject. For the guide: when analyzing
  real-world costs of AI policies, verify whether the stated policy reason is the only
  reason, or whether there are underlying technical concerns that would have produced the
  same outcome regardless.

### Claim 8: Zig already achieved a comparable 4x speedup via a different technical path — self-hosted x86_64 backend — available in Zig 0.16.0

- **Evidence**: mlugg's post (ziggit.dev/t/bun-s-zig-fork-got-4x-faster-compilation-times/15183/19)
  with concrete build benchmark output.
- **Confidence**: emerging (technical claim with benchmark data from Zig core contributor)
- **Quote**: "There's the 4x speedup claimed by the Bun team, already available on Zig
  0.16.0! [...] Each update is taking less than 0.4s, compared to the 120+ seconds taken
  to rebuild with LLVM. In other words, incremental updates are over 300 times faster on
  this codebase than fresh LLVM builds are."
- **Our assessment**: Zig's path (self-hosted backends + incremental compilation) achieves
  orders-of-magnitude improvement where Bun's AI-assisted approach is "capped" at 4x.
  This is not an argument against the AI ban; it is an argument that the technical
  approach Zig chose is superior. The policy debate and the engineering debate are
  independent.

### Claim 9: Practical LLM-assisted OSS contributions caused concrete operational harm to the Zig project before the ban

- **Evidence**: Loris Cro's firsthand account from the kristoff.it essay, confirmed verbatim.
- **Confidence**: anecdotal (practitioner account; no external measurement)
- **Quote**: "from an increase in background noise due to worthless drive-by PRs full of
  hallucinations (that wouldn't even compile, let alone pass CI), to insane 10 thousand
  line long first time PRs. In-between we also received plenty of PRs that looked fine
  on the surface, some of which explicitly claimed to not have made use of LLMs, but
  where follow-up discussions immediately made it clear that the author was sneakily
  consulting an LLM and regurgitating its mistake-filled replies to us."
- **Our assessment**: This is important context: the ban was not theoretical. Zig
  experienced measurable triage burden from LLM-assisted contributions before the policy
  was formalized. The "sneaky LLM use in follow-up discussions" detail is notable —
  contributors who explicitly claimed not to use LLMs, then used them in discussion
  threads. This matches `blog-ronacher-content-for-contents-sake.md` Claim 5, which
  documents the Pi OSS project receiving AI-generated issues (some without the
  submitter's knowledge). The pattern is emerging: LLM-generated OSS contribution noise
  is a real, documented phenomenon across multiple projects.

### Claim 10: Willison's meta-observation — reviewing LLM-generated PRs is irrational if the maintainer can solve the same problem with their own LLM

- **Evidence**: Willison's own synthesis at the end of the article.
- **Confidence**: anecdotal (editorial commentary, not empirical)
- **Quote**: "This makes a lot of sense to me. It relates to an idea I've seen
  circulating elsewhere: if a PR was mostly written by an LLM, why should a project
  maintainer spend time reviewing and discussing that PR as opposed to firing up their
  own LLM to solve the same problem?"
- **Our assessment**: This generalizes beyond Zig's contributor-poker framing. If
  maintainers have equal access to the same AI tools as contributors, the reviewer's
  time spent on LLM-generated patches is not a net gain for the project — the reviewer
  is doing the same work they could do themselves, plus the overhead of reading and
  critiquing someone else's AI output. This is a genuine challenge for AI-native teams:
  at what point does the productivity gain from AI-assisted contributions become a
  productivity loss for the reviewers of those contributions?

### Claim 11: Contributor development and engagement is an explicit business strategy for Zig, not merely a social nicety

- **Evidence**: Loris Cro's essay, confirmed verbatim from the kristoff.it source.
- **Confidence**: anecdotal (institutional statement from a named officer)
- **Quote**: "For us the ability to provide contributors with an engaging ecosystem where
  they can improve their systems thinking and interact with other competent, trusted and
  prolific engineers is a critical aspect of our business model."
- **Our assessment**: Cro is explicit that contributor development is how Zig "punches
  above its weight" given its funding. The AI ban is a business decision, not a moral
  one. This framing is useful for practitioners making the same calculation in corporate
  contexts: "how do we grow engineers" is a business question, and AI-heavy workflows
  have real implications for whether that growth happens.

## Concrete Artifacts

### Zig Code of Conduct LLM policy (from ziglang.org/code-of-conduct/, as quoted in Willison's article)

```
No LLMs for issues. No LLMs for pull requests. No LLMs for comments on the bug
tracker, including translation. English is encouraged, but not required. You are
welcome to post in your native language and rely on others to have their own
translation tools of choice to interpret your words.
```

### mlugg's build benchmark comparing LLVM backend vs. self-hosted x86_64 backend (Zig 0.16.0)

Source: https://ziggit.dev/t/bun-s-zig-fork-got-4x-faster-compilation-times/15183/19

```
$ zig build --summary new -Dno-lib -Duse-llvm
Build Summary: 4/4 steps succeeded
install success
└─ install zig success
   └─ compile exe zig Debug native success 2m MaxRSS:4G

$ zig build --summary new -Dno-lib
Build Summary: 4/4 steps succeeded
install success
└─ install zig success
   └─ compile exe zig Debug native success 31s MaxRSS:1G
```

### Incremental compilation benchmark (Zig 0.16.0, from same mlugg post)

```
$ zig build --summary new -Dno-lib -fincremental --watch
Build Summary: 4/4 steps succeeded
...compile exe zig Debug native success 40s

Build Summary: 4/4 steps succeeded
...compile exe zig Debug native success 361ms

Build Summary: 4/4 steps succeeded
...compile exe zig Debug native success 368ms
```
*(Full series shows sub-400ms incremental rebuilds vs. 120+ seconds for LLVM,
"over 300 times faster" for iterative development.)*

## Cross-References

- **Corroborates**: `blog-ronacher-content-for-contents-sake.md` Claim 5 — "Existing
  text-based infrastructure systems are failing under AI-generated content flooding."
  Ronacher documents the Pi OSS project receiving AI-generated issues (some without
  submitters' knowledge). Claim 9 above documents Zig experiencing the same phenomenon
  earlier and more severely (drive-by PRs with hallucinations, 10K-line first PRs,
  sneaky LLM use in discussion threads). Two independent OSS maintainers are converging
  on the same observation.

- **Extends**: `paper-miller-speed-cost-quality.md` — The Miller et al. DiD study
  measures what happens to code quality when projects adopt AI tools (41.6% persistent
  complexity increase). Zig's contributor-poker policy is a proactive governance
  mechanism designed to prevent exactly this dynamic — not by limiting AI use in general,
  but by controlling which AI-assisted artifacts enter the project's upstream. The two
  sources together provide a framework: AI tools increase velocity but may degrade
  quality (Miller), and one defensible response is to gate contributions by contributor
  trustworthiness (Zig).

- **Extends**: `research-anthropic-ai-transforming-work.md` Claim 8 — "Engineers
  explicitly identify skill atrophy and supervision-paradox risks," with the quote "When
  producing output is so easy and fast, it gets harder to actually take time to learn
  something." Zig's policy addresses the same concern in the OSS contributor-development
  context: if contributors use LLMs to produce their first PRs, they may not develop the
  systems thinking that makes them valuable long-term contributors. Anthropic engineers
  identified this risk internally; Zig institutionalized a policy response to it
  externally.

- **Extends**: `blog-bvp-shopify-ai-playbook.md` Claim 8 — Shopify warns that
  engineers must understand systems "two or three layers below" where they work. Zig's
  contributor-poker framing makes the same point from the OSS governance direction: the
  project's value comes from contributors who have deeply internalized the codebase, not
  contributors who delegated that understanding to an LLM.

- **Novel**: The "contributor poker" conceptual framework itself is entirely new to this
  corpus. No existing source note frames OSS code review as a long-term investment in
  people rather than a quality gate on code. The game-theoretic argument (Claim 5) that
  it is *irrational* to bet on LLM contributors when non-LLM contributors are available
  — independent of code quality — is also novel. The Bun/Zig case study (Claims 6-8) is
  novel as a documented instance of an AI productivity gain that was created but
  explicitly not contributed upstream.

## Guide Impact

- **Chapter 02 (AI adoption fundamentals / when to use AI-native approaches)**: The
  guide currently discusses adoption from the perspective of teams *using* AI. This
  source introduces the legitimate counter-case: receiving AI-assisted contributions.
  Recommend adding a section or callout that addresses "AI contributions to shared
  codebases" as a distinct governance question from "using AI in your own workflow."
  The contributor-poker framework should be surfaced as the strongest available
  articulation of the anti-adoption argument — not to endorse it, but to ensure readers
  can reason about it.

- **Chapter 02 / organizational governance**: The Bun/Zig case study (Claims 6-8)
  should be cited when discussing real-world costs of AI policies. Key nuance: Claim 7
  (mlugg's independent technical objection) shows that policy analysis requires
  separating the AI policy from the engineering objection — they can produce the same
  outcome for different reasons.

- **Chapter 02 / common objections section**: Claim 4 (reviewer time doesn't grow
  contributors if LLM generated the code) is the sharpest version of the "AI harms
  mentoring" objection. Currently, `research-anthropic-ai-transforming-work.md` Claim 8
  is the strongest source for this concern from the internal engineering angle. This
  source provides the same concern from the OSS governance angle.

- **Any chapter discussing code review under AI load**: Claim 10 (Willison's
  meta-observation) is useful: if maintainers and contributors have equal access to AI
  tools, the value proposition of AI-generated PRs becomes unclear. This should be
  mentioned alongside the code-review-as-bottleneck finding from
  `blog-bvp-shopify-ai-playbook.md` Claim 4.

## Extraction Notes

Both the primary source (Willison's blog post at simonwillison.net) and the secondary
source it quotes extensively (Loris Cro's "Contributor Poker and Zig's AI Ban" at
kristoff.it/blog/contributor-poker-and-ai/) were fetched and read in full. Quotes
attributed to Cro were verified against the kristoff.it source — they appear verbatim
in both places.

The mlugg post at ziggit.dev (post #19 in the linked forum thread) was also fetched in
full. It was linked from the Willison article as an "(Update:)" addition. The
build benchmark data in the Concrete Artifacts section is verbatim from that post.

The Zig Code of Conduct at ziglang.org/code-of-conduct/ was checked; the specific LLM
ban text (Claim 1 Quote) was confirmed to appear on the Willison page as a blockquote
and matches the CoC content described by secondary sources. The CoC page itself returned
a tool-mediated summary rather than full verbatim text during extraction; the quote was
verified against the Willison article's blockquote reproduction.

One important nuance to flag for the Assayer: Claims 6 and 7 are in tension with each
other. Bun's statement blames the AI ban for not upstreaming; mlugg's technical post
says the AI ban is "entirely besides the point" and the patch has independent engineering
problems. Both claims are accurately extracted from their sources. No contradiction issue
is filed because both accounts can be simultaneously true (the ban would prevent
upstreaming even if the technical issues were fixed; the technical issues would prevent
upstreaming even if the ban were lifted). The guide should present both layers.
