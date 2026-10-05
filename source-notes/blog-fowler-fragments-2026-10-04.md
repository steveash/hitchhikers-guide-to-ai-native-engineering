---
source_url: https://martinfowler.com/fragments/2026-10-04.html
source_type: blog-post
title: "Fragments: October 4"
author: Martin Fowler (curator); linked sources — Metalanguage (X), Eric Evans (DDD Europe interview), Paul Graham (X), Geoffrey Huntley, Sam Ruby, DHH (via Ruby), Unmesh Joshi, an X post on Gemini 4 Argon
date_published: 2026-10-04
date_extracted: 2026-10-05
last_checked: 2026-10-05
status: current
confidence_overall: emerging
issue: "#3908"
---

# Fragments: October 4 (Martin Fowler)

> Fowler frames LLM systems as things we "nurture" rather than "build" (so bugs may not be fixable or disableable), and collects the code-readability debate (Huntley vs. Ruby and Joshi) toward the view that a compact, high-level notation and an explicit conceptual model must stay at the top of the stack.

## Source Context

- **Type**: blog-post (Fowler's "Fragments" link-blog, 4 October 2026; about ten short sections separated by snowflake dividers, mostly blockquotes plus brief commentary).
- **Author credibility**: Martin Fowler is Chief Scientist at Thoughtworks and author of *Refactoring*; `martinfowler.com` is a `trusted-feed` source. Content here is opinion and curation, not measurement.
- **Scope**: Covers the nurture-vs-build metaphor, an Eric Evans/Fowler interview, code representation and notation, a "partial view of the elephant" framing of agent capability, and one model-benchmark data point. It has no configuration, tooling, or measured outcomes of its own.
- **Not extracted**: The Ola Bini deportation section (personal/political; the Prospector asked to skip it), and the Economist quip about IPOs.
- **Linked pages**: Not followed. All quotations below are as they appear on Fowler's page (the quoted authors' words as reproduced there); they were not checked against the original posts, X threads, or the YouTube video.

## Extracted Claims

### Claim 1: Working with LLMs is "nurturing" an inferential system rather than "building" a deterministic one, and our processes must change accordingly
- **Evidence**: Analogy only: the film *Forbidden Planet* (1956), bridges and locomotives versus gardens and children. Prompted by a reply from "Metalanguage" ("we shipped the id and forgot the superego").
- **Confidence**: anecdotal
- **Quote**: "We talk of building software, but building implies a degree of determinism."
- **Our assessment**: A framing, not an empirical claim. Useful vocabulary for the guide's case that agent behavior is shaped (prompts, harness, feedback) rather than specified. Fowler states the open question himself: "understanding what has changed in this shift from building a computational system to nurturing an inferential one, and how our processes need to change in response." He gives no answers.

### Claim 2: Unlike deterministic bugs, misbehavior in inferential LLMs generally has no simple fix or disablement
- **Evidence**: Argument by contrast with conventional software. No examples of failed fixes are given.
- **Confidence**: anecdotal
- **Quote**: "With inferential LLMs however, there is no such simple fix or disablement, which may lead us to the fate of the Krell."
- **Our assessment**: Overstated as written. Harness-level controls (permissions, sandboxing, turn caps, hooks) can disable *capabilities* even where the model's disposition can't be patched, which is what much of the corpus is about. The claim is best read as "you can't patch the model's behavior like a code bug". It is a hypothesis; it is not supported by evidence on the page.

### Claim 3: Eric Evans reports that the shift to AI-assisted work can be frustrating but ultimately liberating, and that agile habits (small steps, attention to feedback) help with the uncertainty
- **Evidence**: Fowler's summary of a DDD Europe (June 2026) interview video with Eric Evans, hosted by Gien Verschatse. Evans says it has reinvigorated his love of programming. Fowler did not reproduce transcript beyond one quote.
- **Confidence**: anecdotal
- **Quote**: "people are probably going to feel very frustrated by [the new way of thinking about software]… but when you get through that, there is a kind of a wonderful feeling of my brain’s been loosened up."
- **Our assessment**: Two experts' testimony; no data. The bracketed text is Fowler's insertion. Corroborates the guide's iterative-practice theme, but note the video itself was not viewed. The page says "don’t miss Eric’s important final tip" without stating it, so that content is missing from this note.

### Claim 4: Writing and thinking are intertwined, and chatting with an LLM is likewise an iterative process of exploration and refinement
- **Evidence**: Fowler's description of the interview conversation.
- **Confidence**: anecdotal
- **Quote**: "how its very much an iterative process of exploration and refinement - the same is true when we chat with our LLMs."
- **Our assessment**: Consistent with iterative-loop guidance; a one-line assertion. Low novelty, included for completeness.

### Claim 5: Paul Graham — many practices only worked because humans operate at a limited rate, and we will discover which as they break
- **Evidence**: A single quoted post by Paul Graham; no examples.
- **Confidence**: anecdotal
- **Quote**: "There were a lot of things that only worked because there’s a limit to the rate at which humans can operate. We’re about to find out what all of them are, as they break."
- **Our assessment**: A prompt for investigation rather than a finding. Pairs well with the corpus's theme that human-paced review and process are the bottleneck agents expose. Untestable as stated.

### Claim 6: Code need not be stored in the form it is presented to a human reader (projectional-editing view)
- **Evidence**: Fowler's reading of Huntley's demo, where an LLM explains a Haskell function by translating it to Python. Huntley says humans no longer need readable code as a goal.
- **Confidence**: emerging
- **Quote**: "People are still saying, very loudly, that code should be readable so that humans can understand it. I no longer think that’s the goal."
- **Our assessment**: Fowler agrees only partially: he reads the demo as showing "there is a role for code - just that LLM need not store code in the same form that it presents it to a reader." This is a modest reconciliation of Huntley's stronger position (see `blog-ghuntley-readable-explainable.md`, Claim 1). Fowler's projectional-editing link is a useful concept: editable representation ≠ storage representation.

### Claim 7: Even if agents "drill" down to lower-level targets (Rust, C++, assembler, microcode), a high-level notation must stay at the top as the source of truth
- **Evidence**: Sam Ruby's exercise on a Rails app, as relayed by Fowler: about 60,000 tokens in Ruby/Rails versus about 4,000,000 tokens compiled to C. DHH had argued that languages like Rust and C++ are prompt compilation targets "for the moment" and that assembler and microcode will follow. Fowler states the larger size will "hamper the LLM", as it has to fit the context window and decide where to focus attention. The measurement is Ruby's, shown only as a summary on Fowler's page.
- **Confidence**: emerging
- **Quote**: "Let the drill go as deep as it can. Just keep the notation at the top."
- **Our assessment**: The 60k→4M token ratio is a concrete, memorable data point (single app, single measurement, language-compilation choice unspecified on this page). The underlying argument (compactness matters for context and attention independent of human readers) is a genuine harness-design consideration and is plausible. It extends the token-economics threads in the corpus.

### Claim 8: A high-level framework like Rails can serve as "the most compact, precise and conventional specification" of an application when agents write the code
- **Evidence**: Ruby's conclusion from the token exercise above.
- **Confidence**: emerging
- **Quote**: "what Rails becomes when agents write the code: the most compact, precise and conventional specification of a web application, whatever it ends up compiled to."
- **Our assessment**: An argument for convention-heavy frameworks and DSLs as agent-friendly targets. Ties to the "what do we keep, edit and trust as the source of truth?" question that Ruby poses and that the page quotes. No comparative evidence across frameworks.

### Claim 9: Code has two intertwined purposes (machine instructions and a conceptual model), and in the LLM era the conceptual-model role matters more
- **Evidence**: Unmesh Joshi's article (martinfowler.com "What is code", Cognitive Debt section), quoted at length by Fowler. Argument, not data.
- **Confidence**: emerging
- **Quote**: "Code is still instructions for a machine. But it is also a model of understanding. In the LLM era, that second role becomes even more important."
- **Our assessment**: Strong conceptual anchor for guidance on why teams should not delegate understanding wholesale to agents. Joshi's practical corollary is vocabulary work: "making the conceptual model explicit, discovering the right vocabulary, and refining that vocabulary through iteration, domain expertise, and feedback." He also rejects passive review: "We are not meant to be passive reviewers of generated code." That runs against Huntley's direction (Claim 6), which Fowler sets side by side without adjudicating.

### Claim 10: "The role of coding is not disappearing. But it is changing."
- **Evidence**: Joshi's conclusion, reproduced by Fowler.
- **Confidence**: emerging
- **Quote**: "The role of coding is not disappearing. But it is changing."
- **Our assessment**: Consensus-flavored and hard to falsify; value lies in the specifics in Claim 9. The statement "The act of writing code is itself part of our thinking" is the testable edge (does writing code, versus reviewing it, build the understanding that makes later changes safe?). The corpus's intent-debt/cognitive-debt notes cover the same ground.

### Claim 11: The practical question about agents is where the information comes from and what checks the result
- **Evidence**: Sam Ruby's post (26–27 Sep 2026), using a blind-men-and-the-elephant analogy for partial views of agent capability.
- **Confidence**: emerging
- **Quote**: "The practical question isn’t whether agents are good. It’s this: for the task in front of you this week, where will the information come from, and what will check the result?"
- **Our assessment**: A compact, usable checklist question for task planning (context sourcing + verification). It is advice, not evidence, and the most directly actionable sentence in the fragment.

### Claim 12: A model with a much lower hallucination rate that says "I don't know" is a trade-off worth preferring, even at the cost of fewer correct answers
- **Evidence**: An X post quoting Artificial Analysis numbers: Gemini 4 Argon 15% hallucination rate, versus Grok 4.7 29%, GPT-6 Astra 45%, Opus 5.5 59%, Fable 5.1 69%; Gemini gets 50% right against 66% for Opus 5.5 on max. Fowler relays it without verifying.
- **Confidence**: anecdotal
- **Quote**: "Being clearer about what it doesn’t know, at a cost of getting less answers right, is definitely a trade-off I prefer."
- **Our assessment**: Secondhand benchmark data from a social-media post; the benchmark's definition of hallucination rate isn't given on this page. The preference statement is Fowler's judgment and is fair, but it is task-dependent: for verified, tool-checked loops, higher raw accuracy may win. Treat the numbers as unverified.

## Concrete Artifacts

```
Source: Fowler, "Fragments: October 4", quoting an X post about Gemini 4 Argon
(Artificial Analysis hallucination rate; lower is better)

Gemini 4 Argon  15%
Grok 4.7        29%
GPT-6 Astra     45%
Opus 5.5        59%
Fable 5.1       69%

Correct answers: Gemini 4 Argon 50% vs Opus 5.5 (max) 66%
```

```
Source: Sam Ruby (as summarized by Fowler), token-count exercise on a Rails app
Ruby/Rails representation: ~60,000 tokens
Compiled to C:             ~4,000,000 tokens
```

```
Source: DHH, quoted by Sam Ruby, quoted by Fowler
"Rust is a good prompt compilation target for the moment, but so is C++. And soon assembler. Then microcode. Myopic to think we’re going to stop the agentic drill bit until it reaches computing bedrock."
```

## Cross-References

- **Corroborates**:
  - `blog-fowler-fragments-2026-07-06.md` — its retreat notes include "we need abstractions to communicate with agents (echoing Unmesh Joshi's thoughts on building conceptual models)". That is the same Joshi thread; this fragment supplies the substance.
  - `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 2 (hallucination rates on AA-Omniscience) — same benchmark family, showing wide variance in hallucination across frontier models. Note that note's rates apply to wrong answers and are not directly comparable to the numbers here.
- **Contradicts**: None filed. There is a tension between Huntley's stance (`blog-ghuntley-readable-explainable.md`, Claim 1: code's goal shifts from human readability to being explainable on demand) and Joshi's ("We are not meant to be passive reviewers of generated code"). Fowler presents both and reconciles them as differing storage vs. presentation representation, so this is a difference of emphasis and context rather than a clean contradiction; no `C-NNN` issue was filed.
- **Extends**:
  - `blog-fowler-fragments-2026-09-29.md` — its Claim 4 (agent defenses built on token scarcity) concerns controls; this fragment's Claim 7 adds the opposite concern, that tokens are also a *capacity* constraint for the model's own comprehension.
  - `blog-fowler-fragments-2026-09-29.md` Claim 1 (agents make engineering harder) — Claim 11 here (where will information come from, what will check the result) is a similar practical framing from a different author.
  - `blog-ghuntley-readable-explainable.md` Claim 1 — adds Fowler's projectional-editing framing and Ruby/Joshi counterarguments.
- **Novel**: The nurture-vs-build framing and the "no simple fix or disablement" claim; the 60k→4M token Rails-vs-C data point and the "keep the notation at the top" argument; Ruby's "where will the information come from, and what will check the result?" question; Joshi's two-purposes model of code (as quoted).

## Guide Impact

- **Chapter 2 (behavioral risks)**: Consider adding the nurture-vs-build distinction as a framing for non-deterministic failure modes, with the caveat from Claim 2 above that harness controls can still disable capabilities. Cite as anecdotal/framing, not evidence.
- **Chapter 3 (patterns for iterative work)**: Add Ruby's "where will the information come from, and what will check the result?" as a pre-task planning question; cite alongside the Evans interview for iterative-exploration framing.
- **Chapter 4 (practices / code as conceptual model)**: Add the notation-at-the-top argument with the 60k vs 4M token data point (flagged single-measurement), paired with Joshi's two-roles-of-code framing and the Huntley-vs-Joshi disagreement on whether humans should still read and write code.
- **Model choice (if any chapter covers it)**: Note the accuracy-vs-calibrated-abstention trade-off, flagged as unverified secondhand benchmark data.

## Extraction Notes

- Read the full page as served HTML (via curl, converted to text) and quoted from that text; no sub-pages followed. Quotes of Huntley, Ruby, DHH, Joshi, Graham, and Evans are as reproduced on Fowler's page and were not verified at the original sources.
- The Gemini 4 Argon figures are relayed from an X post and could not be independently checked; the post's numbers (e.g., 50% vs 66%) were copied as written.
- The Evans interview video was not watched; the "final tip" Fowler alludes to is not captured.
- Cross-referenced claim numbers were checked against the cited notes: `blog-fowler-fragments-2026-09-29.md` Claims 1 and 4, `blog-ghuntley-readable-explainable.md` Claim 1, and `blog-thebatch-gpt55-hallucination-kimi-k26.md` Claim 2.
