---
source_url: https://simonwillison.net/2026/Aug/1/ten-advances-in-mathematics/#atom-everything
source_type: blog-post
title: "Ten advances in mathematics and theoretical computer science"
author: Simon Willison (link-blog commentary on an OpenAI research announcement)
date_published: 2026-08-01
date_extracted: 2026-08-07
last_checked: 2026-08-07
status: current
confidence_overall: anecdotal
issue: "#2542"
---

# Ten advances in mathematics and theoretical computer science

> Simon Willison's link-blog reaction to OpenAI setting an internal Astra-based
> model on ten decade-stale open math/TCS problems (all ten solved, OpenAI
> claims under $2,000 in GPT-5.6 Sol tokens per problem), framed against
> Anthropic's $100k cryptographic-weakness discovery and Terence Tao's "big
> mathematics" vision of human-AI mathematical collaboration.

## Source Context

- **Type**: blog-post (simonwillison.net link-blog format — a short editorial
  reaction plus quoted excerpts, pointing to a primary OpenAI research
  announcement). Per Miner step 1, all substantive linked pages were fetched
  and read: the `openai/ten-proofs` GitHub repository (README, build
  instructions, and the `ComparatorChallenges/README.md` independent-checking
  instructions), the 253-page OpenAI paper PDF (`ten-proofs-oai.pdf` — abstract,
  table of contents, and both ends of the document sampled directly), the
  62-page LLM-generated "reasoning walkthroughs" PDF, and the IEEE Spectrum
  feature on Terence Tao and "big mathematics" that Willison quotes from. The
  primary `openai.com/index/ten-advances-in-mathematics/` page itself returned
  a Cloudflare JavaScript challenge on direct fetch and could not be read
  beyond what Willison quotes from it (see Extraction Notes).
- **Author credibility**: Simon Willison is the creator of Django and the
  `llm` Python CLI, and one of the most widely cited practitioner commentators
  on LLM tooling; this is a `trusted-feed` entry, meaning it already passed
  the corpus's "is this author worth listening to" bar. The load-bearing
  claims, however, originate from OpenAI's own announcement (a directly
  interested first-party vendor account) and, for the "big mathematics"
  framing, from Terence Tao and other named mathematicians quoted in an IEEE
  Spectrum feature — an independent journalistic source, not OpenAI's own
  framing.
- **Scope**: Covers OpenAI's claim to have solved ten open math/TCS problems
  with an internal Astra-based model, the cost figure claimed per problem, the
  transparency artifacts OpenAI published (Lean formalizations, paper,
  LLM-generated reasoning-walkthrough PDF), Willison's own skeptical asides,
  and Tao's "big mathematics" framing of human-AI mathematical collaboration
  as reported by IEEE Spectrum. Does NOT cover: the mathematical content of
  the ten proofs themselves (confirmed pure mathematics/TCS, see Claim 4 and
  Extraction Notes), independent verification of OpenAI's claims by anyone
  outside OpenAI, or the actual prompts/harness OpenAI used (explicitly not
  published — see Claim 3).

## Extracted Claims

### Claim 1: OpenAI set "an internal version of Astra, our next major model" on ten mathematical problems that had seen no progress on their main result for at least a decade, and claims to have solved all ten at under $2,000 per problem in GPT-5.6 Sol token prices
- **Evidence**: Willison's paraphrase and direct quotation of OpenAI's announcement; no independent verification of the cost figure by Willison or by this Miner.
- **Confidence**: anecdotal (single vendor's self-reported cost claim, no methodology disclosed for how the $2,000 figure was computed, e.g. whether it includes failed attempts)
- **Quote**: "They set \"an internal version of Astra, our next major model\" on finding solutions to ten mathematical problems that \"have seen no progress on the main result for at least a decade\". They claim to have spent less than $2,000 at GPT-5.6 Sol token prices on each one."
- **Our assessment**: This is a striking cost figure — two orders of magnitude below Anthropic's self-reported ~$100,000 for the HAWK cryptographic result (see Cross-References) — but it is an unaudited vendor claim about the vendor's own frontier model, reported secondhand through a link-blog post rather than read directly from OpenAI's page (which was unreachable, see Extraction Notes). Willison's own immediate follow-up (Claim 2) is skepticism about what the figure excludes, which we treat as the appropriate caveat rather than accepting the number as a settled per-problem cost baseline.

### Claim 2: Willison flags that OpenAI's cost figure has no disclosed denominator for failed attempts — the $2,000 figure covers only the ten successes, with no reporting on how many additional problems were attempted and not solved
- **Evidence**: Willison's own editorial aside, not part of OpenAI's announcement.
- **Confidence**: anecdotal (an editorial observation, not a measured figure)
- **Quote**: "(No news on how many problems they spent $2,000 on without reaching a solution though.)"
- **Our assessment**: This is the single most important caveat on Claim 1's economics. A per-solved-problem cost of $2,000 is a very different number from a per-attempted-problem cost if the success rate on decade-old open problems is low — and OpenAI's announcement, per Willison, discloses only the numerator. Any guide citation of "$2,000 to solve a hard open math problem" should carry this caveat explicitly rather than presenting it as a general cost-per-attempt figure.

### Claim 3: OpenAI published Lean 4 formalizations of all ten results plus a paper, and a separate LLM-generated PDF in which the model "reconstructs how the proof came together" from its own unpublished reasoning traces — but did not publish the prompts used to produce the results
- **Evidence**: Direct links to the `openai/ten-proofs` GitHub repository, the paper PDF, and the reasoning-walkthroughs PDF, all fetched and confirmed to exist and match Willison's description; Willison's own editorial reaction to the disclosure.
- **Confidence**: settled (the artifacts themselves are directly verifiable — this Miner fetched and confirmed all three exist as described) for the transparency claim; anecdotal for Willison's judgment that this is "a decent level" but incomplete
- **Quote**: "The openai/ten-proofs repository has Lean 4 formalizations of their results, and there's also a paper describing the solutions and an additional LLM-generated PDF where the model \"reconstructs how the proof came together\" based on the unpublished reasoning traces. That's a decent level of transparency, but I want to see the prompts they used!"
- **Our assessment**: This is a real, verifiable transparency artifact for the *outputs* (machine-checkable Lean proofs, a full paper, a narrative reconstruction) but Willison's explicit gap — no published prompts or harness description — means the actual elicitation method (what OpenAI's internal Astra model was told, how many attempts it took, whether iteration/self-correction was involved) is undocumented. This mirrors a recurring pattern in the corpus: vendors disclose polished output artifacts more readily than the process that produced them.

### Claim 4: The published paper and its content are confirmed to be pure mathematics and theoretical computer science — ten independent chapters (sphere packing, binary/spherical codes, non-sofic groups, Connes's rigidity conjecture, arithmetic circuit complexity, quantum parallel repetition, closest vector problem, Ehrhart's volume conjecture, multicolor Ramsey numbers, and two extremal graph theory conjectures) with no methodology, cost, or engineering-process content anywhere in the document
- **Evidence**: This Miner extracted and read the paper's abstract, table of contents, opening pages, and closing/reference pages directly from the 253-page PDF (`ten-proofs-oai.pdf`), and separately grepped the full 62-page reasoning-walkthroughs PDF for cost/token/methodology keywords, finding none outside pure mathematical proof text.
- **Confidence**: settled (directly verified by this Miner against the primary document, not secondhand)
- **Quote**: (no direct quote; see paraphrase above — the paper's own abstract lists the ten results verbatim as: "1. High-dimensional sphere packing... 2. Binary and spherical codes... 3. Nonsofic groups exist... 4. Connes's rigidity conjecture... 5. Arithmetic circuit complexity... 6. Quantum parallel repetition... 7. Closest vector problem... 8. Ehrhart's volume conjecture... 9. Multicolor Ramsey numbers... 10. Compactness and degeneracy")
- **Our assessment**: This confirms the Prospector's triage assessment that the source is thin on engineering practice — the primary artifact is a genuine academic mathematics paper, not a systems or methodology paper. There is no discoverable content in the paper or its reasoning-walkthrough companion about the harness, prompting strategy, or iteration process, which is consistent with Claim 3's observation that prompts were withheld. Any guide use of this source must draw on Willison's framing and the linked reactions (Tao, Hampshire), not on the mathematical content itself.

### Claim 5: OpenAI built and shared an independent proof-checking pipeline ("Comparator") that re-verifies the Lean formalizations using a second, separately-implemented proof checker rather than relying solely on Lean's own kernel
- **Evidence**: The `ComparatorChallenges/README.md` file in the `openai/ten-proofs` GitHub repository, fetched and read directly by this Miner.
- **Confidence**: settled (directly verified concrete artifact — build/run instructions for an actual tool)
- **Quote**: "Install `landrun`, `lean4export`, and `nanoda_bin`, and make them available on `PATH`. Then, from the repository root: ... `lake exe comparator ComparatorChallenges/A_SpherePacking.json` ... Replace `A_SpherePacking.json` with any other challenge configuration in this directory."
- **Our assessment**: This is the most concrete, reusable engineering artifact in the source: rather than asking readers to trust the Lean compiler alone, OpenAI exports each proof via `lean4export` and re-checks it with `nanoda_bin`, an independently implemented kernel checker (Comparator, from the `leanprover/comparator` project), giving a second, differently-coded verification path for the same claim. This is a directly applicable pattern for any AI-native workflow that produces formally checkable output: pair the primary verifier with an independently implemented second checker rather than trusting one toolchain's kernel as the sole arbiter of correctness.

### Claim 6: Terence Tao frames AI's growing mathematical capability not as a threat but as the catalyst for "big mathematics" — large-scale, decentralized human-AI collaborations where humans do the creative work and AI does the technical grunt work
- **Evidence**: IEEE Spectrum feature (Benjamin Skuse, 25 Jun 2026, "What It Means to Be a Mathematician When AI Does the Math"), quoted verbatim by Willison and independently confirmed by this Miner against the original IEEE Spectrum article.
- **Confidence**: emerging (a named Fields Medalist's stated position and working philosophy, not a measured outcome)
- **Quote**: "Unlike some of his peers, Tao is neither dismissive of AI nor fearful. Instead, he sees it as the catalyst for a fundamental shift in the discipline—a transition toward what he calls \"big mathematics.\" He envisions a future of large-scale, decentralized collaborations between humans and machines, where complex mathematical tasks can be diced and sliced, with humans claiming the creative parts and AI doing the lion's share of the technical grunt work."
- **Our assessment**: This is the clearest general-purpose framing in the source for how a domain expert wants to divide labor with AI: not full delegation, and not a refusal to use AI, but task decomposition where humans retain the creative/judgment layer and AI absorbs the mechanical layer. This generalizes the "AI does the grunt work, humans steer and verify" division-of-labor pattern documented elsewhere in the corpus for coding agents, applied here to a domain (pure mathematics) with no existing corpus coverage.

### Claim 7: Tao argues that formal verification is what makes decentralized, low-trust collaboration in mathematics possible at all — without it, opening a project to unknown contributors (human or AI) would be unworkable
- **Evidence**: IEEE Spectrum feature, direct quote from Tao explaining the mechanism behind his "big mathematics" vision.
- **Confidence**: emerging (a named expert's causal claim about why a collaboration model works, not an independently measured result)
- **Quote**: "If it wasn't for this formal verification layer, opening projects up without any safeguards would just be a disaster," adds Tao. "But in math, we can completely check and verify outputs, and this really filters out a lot of the rubbish."
- **Our assessment**: This is a specific, load-bearing claim about *why* formal verification (Lean/Isabelle/Rocq-style proof checking) is the enabling mechanism for trusting contributions from unvetted or unknown sources, including AI — trust shifts from reputation to verification. This directly parallels the guide's verification-chapter concerns about trusting AI-generated output generally: in domains with a cheap, mechanical ground-truth checker (a proof assistant), the verification bottleneck is far lower than in domains without one (compare Claim 6 of `blog-simonwillison-cryptographic-weaknesses-mythos.md`, where verifying an AI-discovered AES attack took two human researchers nearly a month specifically *because* no equivalent mechanical checker existed for that claim).

### Claim 8: An independent reasoning-agent product (Math, Inc.'s "Gauss") formalized a Fields-Medal-winning proof — first assisting humans on the 8-dimensional sphere-packing case in days, then autonomously completing the harder 24-dimensional case in two weeks
- **Evidence**: IEEE Spectrum feature, reporting on a named AI company's named product and a specific mathematician/result.
- **Confidence**: emerging (third-party journalistic reporting on a vendor's product claim, not the vendor's own primary-source announcement, and not independently verified by this Miner beyond the article's account)
- **Quote**: "In February, for example, the AI company Math, Inc. used its aspirationally named reasoning agent Gauss to formalize a proof that had earned the mathematician Maryna Viazovska, of EPFL, in Switzerland, a Fields Medal in 2022. Gauss first helped human mathematicians complete the formalization of Viazovska's solution to the 8-dimensional sphere-packing problem in a matter of days, and then autonomously formalized the more complicated 24-dimensional case in just two weeks."
- **Our assessment**: This is a second, independent data point (different vendor, different result, earlier in 2026) for the same pattern as the OpenAI ten-proofs result and Claim 5's Comparator tooling: LLM-based agents are being paired with formal proof assistants specifically to convert informal human proofs into machine-checkable form, with autonomy increasing on harder sub-problems once the easier case has been assisted. This is a capability-trend data point, not an engineering-practice recommendation on its own, but it corroborates that "LLM assists/automates formalization into Lean-style proof assistants" is now a repeated pattern across at least two vendors (OpenAI, Math Inc.) rather than a one-off.

### Claim 9: Domain experts are explicitly debating whether AI mathematical capability will erode human mathematicians' motivation and skill development, not just their job security
- **Evidence**: IEEE Spectrum feature, quoting Princeton mathematician Akshay Venkatesh (a Fields Medalist) on the motivation question, in the context of a broader debate reported at the 2025 Heidelberg Laureate Forum.
- **Confidence**: anecdotal (personal reflection from a named expert, part of a reported debate rather than a study)
- **Quote**: "There have been times where I've spent years thinking about something, and I've slowly struggled to understand it," he says. "If your computer can do large chunks of that for you, will you have the motivation to spend that time?"
- **Our assessment**: This is a rarely-articulated risk in AI-adoption discourse: not "will AI take my job" but "will AI remove the intrinsic reward that made me want to do this work at all, and will that erode the next generation's skill-building." The IEEE Spectrum piece pairs this with Yang-Hui He's more extreme framing that mathematicians could become "priests to oracles" — passive interpreters of AI output rather than active discoverers. This is squarely a human-factors/adoption concern rather than a capability or engineering claim, but it is a distinct concern from the "will AI replace this role" framing more commonly discussed elsewhere in the corpus.

## Concrete Artifacts

### Independent Lean proof re-verification pipeline (from `openai/ten-proofs` GitHub repository, `ComparatorChallenges/README.md`)
```
Source: https://github.com/openai/ten-proofs (README.md and
ComparatorChallenges/README.md), fetched directly by this Miner.

Build all ten formalizations (Lean 4.32.0, mathlib, Lake):
  lake exe cache get
  lake build All

Build a single formalization:
  lake build SpherePacking

Independently re-check a formalization with a second, separately
implemented kernel checker (Comparator, github.com/leanprover/comparator):
  # requires landrun, lean4export, and nanoda_bin on PATH
  lake exe cache get
  lake exe comparator ComparatorChallenges/A_SpherePacking.json
  # substitute any other challenge configuration file in that directory
```

### The ten published results (from the paper's own abstract, `ten-proofs-oai.pdf`)
```
Source: "Ten Advances in Mathematics and Theoretical Computer Science",
OpenAI paper, abstract (page i), fetched and read directly by this Miner.

1. High-dimensional sphere packing (Cohn-Elkies linear program, exact
   asymptotic rate)
2. Binary and spherical codes (exponential improvement to classical bounds)
3. Nonsofic groups exist (explicit construction, resolves a longstanding
   open question)
4. Connes's rigidity conjecture (disproved via explicit counterexample
   construction)
5. Arithmetic circuit complexity (new lower bounds for the permanent)
6. Quantum parallel repetition (exponential repetition for finite
   two-player entangled games)
7. Closest vector problem (n^(1/400)-factor hardness via 3SAT reduction)
8. Ehrhart's volume conjecture (sharp volume upper bound proved)
9. Multicolor Ramsey numbers (new superexponential lower bound)
10. Compactness and degeneracy conjectures in extremal graph theory
    (two conjectures disproved)

Note: page i of the PDF states "Updated August 6, 2026. The original
version can be found at https://cdn.openai.com/pdf/ten-proofs-oai-original.pdf"
— i.e. this is a revised version of the paper, dated after Willison's post
(1 August 2026).
```

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-cryptographic-weaknesses-mythos.md` Claim 6
    (verification, not generation, is the binding human-effort constraint on
    AI-discovered claims — that source's AES result took a week to discover
    but "nearly a month" and "several hundred hours" for two researchers to
    verify). This source's Claim 7 (Tao: formal verification "filters out a
    lot of the rubbish" and enables low-trust collaboration) explains *why*
    the mathematics domain does not suffer the same verification bottleneck
    as cryptanalysis: a proof assistant gives a cheap, mechanical
    ground-truth check that cryptographic claims about real-world primitive
    security do not have. The two notes together suggest verification cost
    is not a fixed property of "AI produced a hard claim" in general, but
    depends heavily on whether the domain has an existing cheap verifier.
  - `blog-simonwillison-cryptographic-weaknesses-mythos.md` Claim 1 (the
    ~$100,000/60-hour HAWK cost figure) is directly juxtaposed by Willison
    against this source's claimed <$2,000-per-problem figure (Claim 1) — both
    are vendor-self-reported costs for open-ended, research-grade agentic
    work on genuinely hard problems, giving the corpus two cost anchors of
    very different magnitude for a similar class of task (open mathematical
    research vs. open cryptanalytic research). Note per Claim 2 that the two
    figures are not apples-to-apples: the Anthropic figure is a single
    result's all-in cost including discovery and internal verification, while
    OpenAI's figure explicitly excludes the cost of unsuccessful attempts.

- **Contradicts**: None identified against existing corpus source notes. No
  prior note makes a claim about LLM mathematical-proof capability, Lean/proof
  assistant workflows, or Terence Tao's "big mathematics" framing that this
  source disagrees with — this is a genuinely novel topic area for the corpus
  (see Novel below), not a competing claim on an already-covered topic.

- **Extends**: `blog-simonwillison-cryptographic-weaknesses-mythos.md` — that
  note documents a coding-agent-style harness (multiple sandboxed worker
  agents) repurposed for open-ended cryptanalytic research; this source
  documents a distinct but structurally similar pattern (frontier model
  tackling decade-open problems) in a different research domain
  (mathematics/TCS) with a different verification substrate (machine-checked
  formal proof rather than human cryptanalytic review), and adds the
  Comparator independent-recheck pattern (Claim 5) as a concretely reusable
  verification technique not present in the cryptography note.

- **Novel**:
  - **Independent-kernel re-verification pattern**: Claim 5's Comparator
    tooling (re-checking a Lean proof export with a second, separately
    implemented checker) is the first concrete "verify the verifier"
    artifact in the corpus — a reusable pattern for any AI-native workflow
    producing machine-checkable output, distinct from the human-verification
    bottleneck documented in the cryptography note.
  - **"Big mathematics" as a named human-AI division-of-labor philosophy**:
    Claims 6-7 introduce Terence Tao's explicit framing (decentralized
    collaboration, humans keep the creative layer, formal verification
    replaces reputation as the trust mechanism) as a named, articulated
    philosophy from a domain expert, not present elsewhere in the corpus.
  - **Motivation/skill-atrophy as a distinct adoption concern**: Claim 9
    surfaces a human-factors concern (loss of intrinsic motivation and
    skill-building, not job displacement) that is conceptually distinct from
    the displacement/automation-risk framing more commonly seen elsewhere in
    the corpus's team-adoption discussions.
  - **Cross-vendor formalization-assistance pattern**: Claim 8 (Math, Inc.'s
    Gauss agent formalizing a Fields-Medal proof) is the first corpus mention
    of a vendor other than OpenAI/Anthropic/Google applying LLM agents
    specifically to proof formalization, corroborating that this is an
    emerging category of AI agent product, not a single vendor's isolated
    experiment.

## Guide Impact

- **Chapter 03 (Verification)**: Add Claim 5's Comparator pattern (independent
  re-checking of a machine-verifiable claim via a second, separately
  implemented checker, not just re-running the same toolchain) as a concrete
  technique for any AI-native workflow producing formally checkable output.
  Add Claim 7 (Tao on formal verification enabling low-trust collaboration) as
  supporting rationale, paired explicitly with the contrasting case in
  `blog-simonwillison-cryptographic-weaknesses-mythos.md` Claim 6: verification
  cost is low when a domain has a cheap mechanical checker (formal math
  proofs) and can be extremely high when it doesn't (cryptanalytic claims
  about real-world primitives) — the guide should frame "how expensive is it
  to verify an AI's claim" as domain-dependent, not universal.

- **Chapter 04 (Context Engineering)**: Use Claim 3 (OpenAI disclosed outputs
  — Lean proofs, paper, reasoning-walkthrough PDF — but explicitly not the
  prompts or harness) as a cautionary example when citing vendor capability
  announcements: published artifacts describing *what* a model produced do
  not establish *how* it was elicited, and the guide should not imply a
  reproducible technique exists just because a polished output does.

- **Chapter 00 (Principles) / team-adoption framing**: Add Tao's "big
  mathematics" division-of-labor framing (Claim 6: humans keep the creative
  layer, AI absorbs the technical grunt work, decentralized collaboration
  enabled by cheap verification) as an articulated philosophy worth citing
  alongside the guide's existing human-AI collaboration principles, and add
  Claim 9's motivation/skill-atrophy concern as a nuance for any section
  discussing risks of over-delegating cognitively rewarding work to AI, not
  just risks of job displacement.

## Extraction Notes

- **OpenAI's primary announcement page was unreachable**: A direct fetch of
  `openai.com/index/ten-advances-in-mathematics/` returned a Cloudflare
  managed-challenge page (JavaScript-gated, no readable content). All claims
  attributed to OpenAI's own framing in this note are sourced through
  Willison's quotations of that page, not read directly from it. If the
  Assayer can reach the OpenAI page directly, Claims 1-3 should be
  spot-checked against the original.
- **Both linked PDFs and the GitHub repository were fetched and read
  directly** by this Miner (not summarized via a third-party tool): the
  253-page paper (`ten-proofs-oai.pdf`, abstract/TOC/opening pages and closing
  pages/references sampled directly via PDF text extraction), the 62-page
  reasoning-walkthroughs PDF (grepped in full for cost/methodology/process
  keywords — none found outside pure mathematical proof narrative), the
  `openai/ten-proofs` repository README, and the `ComparatorChallenges/README.md`
  file.
- **The IEEE Spectrum article was fetched and read in full** (Benjamin Skuse,
  "What It Means to Be a Mathematician When AI Does the Math," 25 Jun 2026) —
  this is the source of Claims 6, 7, 8, and 9, all independently confirmed
  against the original article text, not solely against Willison's excerpt of
  it. The Tao quote (Claim 6) appears identically in both Willison's post and
  the original IEEE Spectrum article.
- **Kirwin Hampshire's essay ("The Dark Night of Mathematics") was not
  separately fetched** — it is mentioned by Willison only via a characterizing
  paraphrase ("a profound spiritual crisis brought on by previous... results")
  and was judged too far outside the guide's engineering scope (a personal
  essay about mathematicians' emotional response, not a claim about AI
  capability or practice) to warrant a dedicated fetch and claim extraction.
  If the Assayer judges this in scope, it has not yet been read by this
  Miner.
- **Confirms Prospector's thin-extraction expectation**: as flagged in two of
  the three triage comments on the issue, the primary OpenAI paper itself
  contains no engineering-relevant content — it is a genuine, dense
  mathematics/TCS paper. The engineering-relevant material in this note comes
  almost entirely from the surrounding artifacts (the GitHub repo's
  verification tooling) and the linked IEEE Spectrum piece (human-AI
  collaboration framing), not from OpenAI's own primary claims about the
  results themselves.
- **Three duplicate Prospector triage comments** were posted to the issue;
  all three converge on "low-to-medium novelty, thin on direct engineering
  practice, worth mining for capability-boundary and verification framing" —
  consistent with this note's eventual claim mix (mostly framing/verification
  claims, few if any directly actionable engineering techniques beyond
  Claim 5).
