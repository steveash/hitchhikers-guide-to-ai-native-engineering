---
source_url: https://simonwillison.net/2026/Jul/28/discovering-cryptographic-weaknesses-with-claude/
source_type: blog-post
title: "Discovering cryptographic weaknesses with Claude"
author: Simon Willison (link post highlighting Anthropic's research team)
date_published: 2026-07-28
date_extracted: 2026-08-01
last_checked: 2026-08-01
status: current
confidence_overall: emerging
issue: "#2380"
---

# Discovering cryptographic weaknesses with Claude

> Simon Willison highlights Anthropic's research disclosure that Claude Mythos
> (Preview), running as multiple worker agents in a sandboxed harness for up to
> 60 hours (~$100,000 in API cost for the HAWK result alone) and producing on
> the order of a billion output tokens over about a week for the AES result,
> found a genuine lattice weakness in the HAWK post-quantum signature scheme
> and an improved attack on reduced-round AES — with human input reduced almost
> entirely to project-management nudges and repeated encouragement not to
> settle for "low hanging fruit."

## Source Context

- **Type**: blog-post (simonwillison.net link-blog format — a short editorial
  framing plus quoted excerpts, pointing to a primary Anthropic research
  article). Per Miner step 1, the primary source — Anthropic's research
  article at anthropic.com/research/discovering-cryptographic-weaknesses — was
  fetched and read in full, along with the accompanying GitHub repository
  (`anthropics/cryptography-research-demo`), the CryptanalysisBench paper
  abstract (arXiv:2607.18538), and the top of the Hacker News discussion
  thread linked from Willison's post.
- **Author credibility**: Simon Willison is the creator of Django and the
  `llm` Python CLI, and one of the most widely cited practitioner commentators
  on LLM tooling; this post is a `trusted-feed` link-blog entry, meaning it
  already passed the corpus's "is this author worth listening to" bar. The
  substantive claims, however, originate from Anthropic's own research team
  (first-party account of their own experiment) and from the CryptanalysisBench
  paper's academic authors (Lukas Fluri, Avital Shafran, Nicholas Carlini,
  Matthew Jagielski, Milad Nasr, Orr Dunkelman, Eyal Ronen, Florian Tramèr —
  a mix of Anthropic/Google researchers and university cryptographers from ETH
  Zurich, Tel Aviv University, and TU Berlin). Both are directly interested
  parties (Anthropic reporting on its own model's capability) rather than
  independent third-party auditors, which the extraction treats as a scope
  boundary, not disqualifying evidence — the HAWK and AES results were
  disclosed to the primitive authors/NIST and required months of independent
  human verification before publication (see Claim 6).
- **Scope**: Covers Anthropic's own framing of the HAWK and reduced-round AES
  cryptanalysis results, the prompting/intervention pattern used to keep the
  agent working on the problem, the harness architecture at a high level
  (multi-worker, sandboxed, Python/Sage access), cost and token figures, the
  responsible-disclosure process, and the CryptanalysisBench evaluation
  results across five frontier models. Does NOT cover: the full mathematical
  detail of the τ-cocycle lattice attack or the Möbius Bridge fingerprinting
  algorithm (those live in the linked academic papers, not extracted here in
  full); the internal harness code/prompts beyond what Anthropic quoted; or
  independent replication of the results by parties outside Anthropic's
  verification process.

## Extracted Claims

### Claim 1: Claude Mythos (Preview), running as multiple worker agents in a sandboxed harness, discovered a nontrivial mathematical automorphism in the HAWK lattice that cuts the effective key size in half
- **Evidence**: Anthropic's research article, first-party technical account with concrete before/after security-margin figures.
- **Confidence**: emerging (novel result, disclosed to HAWK's authors and NIST, but validated only by Anthropic's own team per Claim 6 — no independent third-party cryptanalytic replication cited in the source)
- **Quote**: "Finding, developing and verifying the attack took about 60 hours in total. We estimate that the full attack discovery process cost approximately $100,000 in API cost."
- **Our assessment**: The keysize-halving framing (HAWK-256 attack cost dropping from 2^64 to 2^38, per the article's own figures) is a real reduction in security margin for a NIST post-quantum candidate, which is a higher-stakes result than a benchmark score. The $100k/60-hour figure is a single data point for what "research-grade" agentic inference costs when the target is a genuinely open mathematical question, not a coding task — this is a useful economics anchor distinct from token-cost figures elsewhere in the corpus, which mostly describe software engineering workloads.

### Claim 2: The harness architecture was "a Claude Code-like harness that supports multiple worker agents collaborating together in a sandboxed environment, with access to computational tools like Python and Sage as well as access to published cryptographic works"
- **Evidence**: Direct quote from Anthropic's research article describing the harness design.
- **Confidence**: settled (Anthropic's own description of infrastructure it built and controls)
- **Quote**: "a Claude Code-like harness that supports multiple worker agents collaborating together in a sandboxed environment, with access to computational tools like Python and Sage as well as access to published cryptographic works"
- **Our assessment**: This is a coding-agent harness repurposed for pure mathematical research rather than software delivery — the "workers" collaborate on a shared research problem instead of a shared codebase. The pattern (multiple parallel workers, sandboxed compute tools, access to the literature) generalizes the Claude-Code-as-generic-agentic-substrate pattern documented elsewhere in the corpus (e.g. the Mozilla Firefox security-scanning harness) to open-ended research rather than bug-finding.

### Claim 3: A multi-worker dynamic directly produced the HAWK breakthrough — one worker prematurely rejected a promising idea as infeasible, but a second worker (working the same idea independently) found a way to exploit it fully
- **Evidence**: Anthropic's research article narrative of the discovery process.
- **Confidence**: anecdotal (single-episode, first-party narrative account; no controlled comparison of single-worker vs. multi-worker outcomes)
- **Quote**: "Both started investigating the idea; the first worker prematurely rejected the idea as infeasible, but the second found a way to fully exploit it."
- **Our assessment**: This is a concrete, named example of "self-correction via redundancy" — running the same speculative idea through multiple independent agent instances catches a false-negative that a single instance would have produced. It is a stronger practical argument for parallel/redundant worker fan-out on ambiguous research questions than an abstract claim would be, because Anthropic ties it to the specific idea that became the published attack. Caution: this is one anecdote from one project, not a measured rate of false-negative recovery.

### Claim 4: Human input for the HAWK discovery was reduced almost entirely to project-management nudges rather than technical direction
- **Evidence**: Anthropic's research article, direct statement about the human role during the HAWK work.
- **Confidence**: settled (direct first-party quote about their own process)
- **Quote**: "For the most part, Mythos agents worked independently, and human input was limited to project management like advising Mythos how to keep track of ideas or which libraries to use for computational verification."
- **Our assessment**: This is a stronger and more specific "hands-off" claim than the AES result (Claim 5), where human intervention was substantive and repeated. The contrast between the two results in the same article — one nearly autonomous, one requiring persistent researcher pushback — suggests the amount of human steering needed is problem-dependent rather than a fixed property of the harness, and should temper any generalized claim that "the harness runs unsupervised."

### Claim 5: For the reduced-round AES attack, Claude initially refused to continue, explicitly telling researchers the target was too well-studied to yield anything — and only produced the eventual result after three separate, terse, typo-laden human prompts insisting it keep trying and aim higher than "low hanging fruit"
- **Evidence**: Anthropic's research article quoting both Claude's refusal and the human prompts verbatim (also reproduced by Willison in his post).
- **Confidence**: settled (verbatim quotes from Anthropic's own account of the interaction)
- **Quote (Claude's refusal)**: "If you want a different outcome, the target has to change … AES-128 r5/r6 is just genuinely hard" and "on AES-128 r5/r6/r7 it found nothing because there's nothing easy to find; this is the most-studied block cipher in existence."
- **Quote (first human prompt)**: "the models tend to think it is impossible to solve so they don't try they [sic] need a good amount of prompting."
- **Quote (later human prompts)**: "no again the goal is that we have highly inteligent [sic] model as good top researcher, we want to find new attacks"; "no we don't want to change the targets [..] agian [sic] we need to find something that worth [sic] publishing"; "again we are not looking for low hanging fruit, we want proper research to find genuinly [sic] hard findings."
- **Our assessment**: This is the single most concrete, reusable artifact in the source: real, informal, typo-laden prompts (not polished prompt-engineering copy) that moved a frontier model from "declaring the problem intractable" to producing a publishable attack. The pattern — refuse to accept the model's first-pass "this is too hard" verdict, and repeatedly redirect it away from easy/incremental results toward the actually-hard target — is directly reusable guidance for any open-ended research or hard-debugging task where a model's default behavior is to declare defeat prematurely. Note the HN discussion (see Extraction Notes) frames this pattern more skeptically: commenter `_dwt` argued the repeated redirection shows the model following well-constructed human guidance rather than exhibiting independent research judgment — a useful counterweight to reading this as a purely autonomous result.

### Claim 6: The AES-attack discovery itself took roughly a week of agent time and about a billion output tokens, but independent human verification of the model's claim took researchers "several hundred hours" and nearly a month — an order of magnitude more human effort than the discovery itself
- **Evidence**: Anthropic's research article, direct quotes contrasting discovery time and verification time.
- **Confidence**: settled (first-party account, but the verification-effort figures are self-reported without external audit)
- **Quote**: "Over the course of the next three days, Claude autonomously produced several hundred million tokens while working on the problem," and later, "after Claude output a total of one billion output tokens, it had refined the attack to the one described in our paper."
- **Quote (verification burden)**: "Researchers at Anthropic then spent several hundred hours learning enough cryptography research to validate the model's claim," and "whereas it took just one week for Mythos to autonomously discover the improved attack on AES, it took two researchers nearly a month to gain confidence that the method it discovered is correct."
- **Quote (article's own framing of the bottleneck)**: "The vast majority of our time over the past few months has been in verifying the correctness of Claude's results."
- **Our assessment**: This is the single most important economics/workflow claim in the source for AI-native engineering practice generally, not just cryptography: as agentic discovery gets faster and cheaper, human verification — not generation — becomes the binding constraint, and verification of a genuinely novel claim can require the verifiers to first build expertise they didn't previously have ("learning enough cryptography research to validate the model's claim"). This generalizes beyond cryptanalysis to any domain where an agent can produce a claim faster than a domain expert can check it.

### Claim 7: Claude's AES attack ("Möbius Bridge" fingerprinting) achieved a 200x to 800x speedup over prior attacks, depending on measurement methodology, but independent cryptographers characterized the underlying result as an incremental extension of a decade-old known technique rather than a fundamentally new discovery
- **Evidence**: Anthropic's article for the speedup figure; Hacker News discussion (linked from Willison's post) for the cryptographer pushback, specifically from Orr Dunkelman — who is himself a co-author of the CryptanalysisBench paper cited in this same source.
- **Confidence**: emerging (the speedup figure is Anthropic's own measurement; the "incremental" characterization is expert commentary, not a formal peer-reviewed rebuttal, though it comes from a recognized AES cryptanalyst)
- **Quote (Anthropic)**: "200 and 800 times faster" (attack speedup, depending on measurement methodology, per WebFetch summary of the research article).
- **Quote (Orr Dunkelman on Hacker News, via WebFetch summary — not independently verified against the raw HN page by this Miner)**: characterized the work as "improving the Derbez, Foque, Jean attack from EUROCRYPT 2013," on a deliberately weakened 7-round AES variant, comparing the security-margin impact to "knocking out Mike Tyson's brother's cousin's uncle's sister's nephew."
- **Our assessment**: This tension is the most important nuance missing from a surface reading of "Claude broke AES." The reduced-round variant attacked (AES-128, r5/r6/r7 — not the full 10-round cipher used in production) is a research target chosen specifically because it's on the frontier of known cryptanalysis, not because it threatens deployed systems; Anthropic's own article concurs ("neither of these results has a practical impact on today's computer systems," per Willison's paraphrase). The guide should not repeat "Claude broke AES" as a headline claim without this qualification. This is not treated as a formal cross-note contradiction (see Cross-References) since no existing corpus note makes a conflicting claim about this specific result — it is a nuance internal to this source and its immediate discussion thread, not a disagreement between two source notes.

### Claim 8: Anthropic partnered with academic cryptographers at ETH Zurich, Tel Aviv University, and TU Berlin to build CryptanalysisBench, a standardized 191-task benchmark across six cryptographic primitive families and three difficulty tiers, and found five frontier models could already break a majority of the easiest tier
- **Evidence**: The CryptanalysisBench paper abstract and methodology (arXiv:2607.18538), a peer-reviewable academic artifact separate from Anthropic's blog post.
- **Confidence**: settled (peer-reviewable arXiv paper with named multi-institution authorship, though this note only extracts the abstract/methodology summary, not the full paper)
- **Quote**: "Cryptanalysis - the task of finding attacks against cryptographic schemes - sits at the intersection of mathematical reasoning and cybersecurity, two areas where LLMs have advanced fastest... In this paper we ask whether LLMs can do cryptanalysis, and find that the answer is increasingly yes."
- **Our assessment**: This is the evaluation-benchmark backbone that gives the HAWK/AES anecdotes broader context: five frontier models (Claude Opus 4.8, Sonnet 5, Mythos 5, GPT 5.5, GLM 5.2) collectively break "65%-86% of Tier 1 schemes" (primitives with known practical breaks — i.e., can the models rediscover known attacks) but only "6-12 Tier-2 schemes at full strength" (primitives with no known breaks) — a much lower hit rate on genuinely open problems. This tiered breakdown is important context: models are already strong at rediscovering known cryptanalytic techniques, but genuinely novel breaks at full cipher strength (like the headline HAWK/AES results) remain rare, hard-won outcomes requiring the extended human-intervention pattern documented in Claims 4-6, not a routine capability.

### Claim 9: A separate, smaller result — a practical attack recovering a 13-round LEA cipher key in under 2^30 plaintexts, running in under an hour on a desktop — improved on a prior requirement of 2^98 plaintext pairs, but the article is explicit that this does not extend to the full 24-round cipher used in practice
- **Evidence**: Anthropic's research article, direct quote with the specific plaintext-count figures.
- **Confidence**: settled (specific quantitative claim from the first-party account, with an explicit scope caveat included by the authors themselves)
- **Quote**: "does not apply to the 24-round cipher, and so has no immediate practical consideration."
- **Our assessment**: Anthropic including this caveat unprompted (rather than only in response to external skepticism, as with the AES result) suggests the article is generally careful about scoping its claims to reduced/weakened variants rather than overselling practical impact — this is worth noting when calibrating the overall trustworthiness of the article's other, less-hedged claims (e.g., Claim 1's HAWK result, which does not carry an equivalent "no practical impact" caveat because HAWK's exponent reduction is closer to being a real security-margin loss on the actual candidate scheme).

### Claim 10: Responsible disclosure was built into the process — HAWK findings were shared with the scheme's authors in June 2026 and coordinated with the public NIST mailing list at release, and advance copies of both results were shared with US government and industry partners
- **Evidence**: Anthropic's research article, direct statements on disclosure practice.
- **Confidence**: settled (first-party account of a disclosure process; consistent with standard responsible-disclosure norms in security research)
- **Quote**: "Throughout the research process, we followed responsible disclosure procedures, and consulted with academics to confirm the validity of our findings. We also shared advance copies with US government and industry partners." And, specific to HAWK: "we shared our attack with the authors of HAWK in June and coordinated disclosure to the public NIST mailing list at the same time our results were released."
- **Our assessment**: This establishes that Anthropic treated an AI-discovered cryptographic weakness with the same disclosure rigor as a human-discovered one — a relevant precedent for any organization whose AI-assisted research or security work might surface a genuine vulnerability. The pattern (author notification, standards-body coordination, government/industry advance notice) is a reusable checklist for teams whose agentic research tooling might someday produce a similarly consequential finding outside the cryptography domain.

### Claim 11: Anthropic frames the overall trajectory as a one-year capability jump — from language models being unable to perform cryptanalysis of even basic ciphers to finding flaws that had "escaped discovery despite years of human expert review"
- **Evidence**: Anthropic's research article's own concluding framing.
- **Confidence**: anecdotal (this is Anthropic's own narrative framing/marketing language about its own model's trajectory, not an independently measured capability curve)
- **Quote**: "In just one year, language models have gone from being unable to perform cryptanalysis of even the most basic ciphers to being capable of finding flaws in cryptographic designs that have escaped discovery despite years of human expert review."
- **Our assessment**: This is the article's thesis statement and should be read with appropriate skepticism as a vendor characterizing its own product's progress — it is directionally consistent with the CryptanalysisBench Tier-1 results (Claim 8) but the specific "escaped discovery despite years of human expert review" framing applies most cleanly to the HAWK result, less cleanly to the AES result (Claim 7's incremental-extension pushback), and not at all to the LEA result (Claim 9's explicit no-practical-impact caveat). Treat as directional evidence of real capability growth, not as a precise, uniformly-applicable claim across all three results in the article.

## Concrete Artifacts

### Human intervention prompts, AES discovery (verbatim as quoted in Anthropic's article and reproduced by Willison)
```
Source: anthropic.com/research/discovering-cryptographic-weaknesses,
via simonwillison.net/2026/Jul/28/discovering-cryptographic-weaknesses-with-claude/

1. "the models tend to think it is impossible to solve so they don't try they
   [sic] need a good amount of prompting."

2. "why not do aes-128 r7? the whole point is to find something better than
   existing approaches."

3. "no again the goal is that we have highly inteligent [sic] model as good
   top researcher, we want to find new attacks"

4. "no we don't want to change the targets [..] agian [sic] we need to find
   something that worth [sic] publishing"

5. "again we are not looking for low hanging fruit, we want proper research
   to find genuinly [sic] hard findings."
```

### Claude's initial refusal, AES target (verbatim)
```
Source: anthropic.com/research/discovering-cryptographic-weaknesses

"If you want a different outcome, the target has to change … AES-128 r5/r6
is just genuinely hard"

"on AES-128 r5/r6/r7 it found nothing because there's nothing easy to find;
this is the most-studied block cipher in existence."
```

### Timeline and cost summary (compiled from Anthropic's article)
```
HAWK result:
  - Duration: ~60 hours total (discovery + development + verification)
  - Cost: ~$100,000 in API cost (Anthropic's own estimate)
  - Human input: project-management nudges only ("how to keep track of
    ideas or which libraries to use for computational verification")

AES result:
  - Agent discovery time: ~1 week autonomous work (article's own framing);
    a specific 3-day window is called out as producing "several hundred
    million tokens," with the full effort reaching "one billion output
    tokens" total
  - Human input: 5 short, informal, typo-laden prompts over the period,
    after an initial refusal from the model
  - Verification time: "several hundred hours," "nearly a month," two
    researchers, to validate correctness of the model's claim

LEA result (smaller, preliminary):
  - 13-round key recovery in <2^30 plaintexts, <1 hour on a desktop
    (prior best: 2^98 plaintext pairs)
  - Explicitly does not extend to the practical 24-round cipher
```

### CryptanalysisBench summary (from arXiv:2607.18538 abstract)
```
Authors: Lukas Fluri, Avital Shafran, Nicholas Carlini, Matthew Jagielski,
Milad Nasr, Orr Dunkelman, Eyal Ronen, Florian Tramèr
Submitted: 2026-07-20 (v2: 2026-07-29); 46 pages, 5 figures, 4 tables
License: CC BY 4.0

Design: 191 tasks across 6 cryptographic primitive families, 3 tiers:
  Tier 1 - primitives with known practical breaks
  Tier 2 - primitives without known breaks, at full and reduced strength
  Tier 3 - production-level challenge primitives

Models evaluated: Claude Opus 4.8, Sonnet 5, Mythos 5, GPT 5.5, GLM 5.2

Results (per WebFetch summary of the paper's stated findings):
  - 65%-86% of Tier 1 schemes broken
  - 6-12 Tier-2 schemes broken at full strength
  - 24-61 Tier-2 variants broken across all scaled-down versions
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-firefox-claude-mythos.md` (the Mozilla Firefox
    security-hardening note) — both sources describe a "Claude Code-like"
    harness repurposed for a non-software-delivery research/discovery task
    (Firefox: vulnerability hunting in existing code; here: open mathematical
    cryptanalysis), both use multi-agent/multi-worker parallelism as the
    scaling mechanism, and both report that the harness/pipeline compounds in
    value over time as models improve (Firefox Claim 7: "once the pipeline is
    in place, it's trivial to swap in different models"; this source's Claim
    2 harness description plays the same generic-substrate role). This source
    adds a data point outside software engineering: the same class of harness
    generalizes to pure research problems, not just code auditing.
  - `blog-simonwillison-firefox-claude-mythos.md` Claim 9 (defense-in-depth
    validated by AI harness logs) is a distant echo of this source's
    responsible-disclosure practice (Claim 10): in both cases, a vendor
    treats an AI-discovered finding (a blocked exploit attempt in one case, a
    genuine cryptographic weakness in the other) with the same rigor it would
    apply to a human-discovered one, rather than dismissing AI output as
    inherently lower-confidence.

- **Contradicts**: None identified against existing corpus source notes — no
  prior note makes a claim about LLM cryptanalysis capability that this
  source disagrees with (novel topic in the corpus, see Novel below). The
  internal tension noted in Claim 7 (Anthropic's "novel discovery" framing vs.
  Orr Dunkelman's "incremental, decade-old technique" framing on Hacker News)
  is *not* filed as a formal contradiction issue per MINER.md §4a, because
  it is not a disagreement between two source notes in the corpus — it is
  expert commentary reacting to this same source, captured here as a
  qualifier on Claim 7 and Claim 11 rather than as a competing claim with its
  own evidentiary basis independent of this source.

- **Extends**: `blog-simonwillison-firefox-claude-mythos.md` — that note
  establishes the general pattern of coding-agent harnesses (parallel
  workers, sandboxed tools, pipeline-over-model durability) applied to
  security bug-hunting in existing code. This source extends the pattern to
  open-ended mathematical research where there is no existing codebase to
  scan and no ground-truth "bug" to find — the harness has to originate and
  validate a genuinely new claim, which is a qualitatively harder task than
  finding an instance of a known bug class.

- **Novel**:
  - **Research-grade agentic cost anchor**: The ~$100k / 60-hour figure for a
    single research result is the first cost/duration data point in the
    corpus for open-ended agentic research (as distinct from software
    engineering token-cost figures elsewhere in the corpus).
  - **The "keep insisting it's not too hard" intervention pattern**: The
    verbatim, informal AES prompts are the first documented example in the
    corpus of a human overriding a model's own "this problem is intractable"
    self-assessment through repeated, low-effort encouragement rather than
    technical redirection, and having that succeed.
  - **Verification-as-bottleneck economics**: Claim 6's finding that
    verification took an order of magnitude more human time than discovery
    is a new, generalizable claim not present elsewhere in the corpus about
    where the human bottleneck shifts to as agentic generation speeds up.
  - **Multi-worker redundancy catching a false-negative**: Claim 3's HAWK
    anecdote (one worker wrongly rejects an idea, a second worker independently
    finds it works) is a first concrete example in the corpus of parallel
    agent redundancy recovering from a premature-rejection failure mode.
  - **CryptanalysisBench as a tiered, cross-vendor benchmark**: No prior
    corpus note documents a cryptanalysis-specific benchmark; this is the
    first evidence in the corpus of frontier-model capability specifically in
    mathematical cryptanalysis, cross-vendor (Claude, GPT, GLM).

## Guide Impact

- **Chapter on Prompt Engineering / Real-World Strategies (Ch03/Ch04)**: Add
  the AES intervention pattern (Claim 5, Concrete Artifacts) as a named
  technique: when a model declines a hard, open-ended task by asserting it's
  intractable, do not accept the self-assessment at face value — brief,
  repeated, low-polish encouragement that explicitly rejects "easy" partial
  results can be sufficient to unlock further progress. Note the caveat from
  Claim 5's HN discussion: this may reflect the model following explicit
  redirection rather than demonstrating independent judgment, so the
  technique should be framed as "steering," not as evidence the model is
  reasoning about research value unprompted.

- **Chapter on Economics of LLM Use (Ch05)**: Add the $100k/60-hour HAWK
  figure and the AES verification-time figures (Claim 6) as a research-grade
  agentic cost anchor, explicitly distinct from software-engineering token
  costs documented elsewhere in the corpus. Cite the verification-bottleneck
  finding as a generalizable claim: as generation gets cheaper, the binding
  cost shifts to human verification, and verifiers may need to build
  domain expertise they didn't previously have before they can even evaluate
  the claim.

- **Chapter on Agentive Loops / Long-Running Inference (Ch02)**: Add the
  multi-worker redundancy pattern (Claim 3) as a concrete argument for
  running the same speculative idea through multiple independent agent
  instances on ambiguous research questions, since a single instance can
  produce a false negative that redundant instances catch. Cross-reference
  the Mozilla Firefox harness note for the parallel pattern applied to
  security bug-hunting.

- **Chapter on Model Capabilities / Evaluation (Ch02 or wherever benchmark
  evidence lives)**: Add CryptanalysisBench's tiered results (Claim 8) as
  calibration: models are already strong (65-86%) at rediscovering known
  cryptanalytic breaks (Tier 1) but weak (6-12 out of many) at finding novel
  breaks against full-strength primitives (Tier 2) — the guide should not let
  a single headline result (HAWK) imply routine capability at genuinely novel
  cryptanalysis.

## Extraction Notes

- Primary source (Willison's post) is short; the substantive technical
  content was fetched from Anthropic's linked research article
  (anthropic.com/research/discovering-cryptographic-weaknesses), which was
  read via two separate fetches to cross-check section structure and exact
  quotes — both fetches agreed on all quoted text used in this note.
- The GitHub repository (`anthropics/cryptography-research-demo`) is a code
  artifact (the HAWK recovery implementation, an AES component, and an LEA
  component), not primarily documentation — its top-level README states only
  "Research artifact. Not maintained and not accepting contributions." The
  HAWK subdirectory README documents the *recovery tool* (how to run the
  attack once discovered — SVP solving via Sage, sieve backends, runtime
  ~3h42m on a 96-core server) rather than the discovery process itself; this
  is included in Concrete Artifacts context but not extracted as a claim
  since it describes the published attack's implementation, not a new
  finding.
- The Hacker News discussion (news.ycombinator.com/item?id=49087091) was
  fetched via WebFetch's summarization rather than read as raw HTML; the
  commenter quotes attributed to Orr Dunkelman, `_dwt`, `pseudohadamard`,
  `jandrewrogers`, and `staticshock` in Claim 5's note and Claim 7 are as
  returned by that summarization pass, not independently re-verified against
  the raw page by this Miner. The Assayer should treat the HN attributions as
  lower-confidence than the Anthropic-article quotes and, if spot-checking,
  verify directly against the raw HN thread rather than trusting this note's
  secondhand summary.
- Note that Orr Dunkelman, quoted on Hacker News as skeptical of the AES
  result's novelty, is also a listed co-author of the CryptanalysisBench
  paper (Claim 8) that Anthropic cites as validating the same body of work —
  this is a useful signal that the skepticism comes from a domain expert who
  was simultaneously involved in the adjacent academic evaluation effort, not
  an outside critic.
- No paywall encountered on any of the four fetched URLs (Willison's post,
  Anthropic's article, the GitHub repo, the arXiv abstract page).
- No contradiction issue filed — see Cross-References "Contradicts" for
  reasoning.
