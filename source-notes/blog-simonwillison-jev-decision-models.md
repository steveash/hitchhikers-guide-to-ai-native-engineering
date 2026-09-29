---
source_url: https://simonwillison.net/2026/Sep/21/jev/
source_type: blog-post
title: "Jev introduces a new shape of LLM—System One, aka Decision Models"
author: Simon Willison
date_published: 2026-09-21
date_extracted: 2026-09-29
last_checked: 2026-09-29
status: current
confidence_overall: emerging
issue: "#3778"
---

# Jev introduces a new shape of LLM—System One, aka Decision Models

> Simon Willison introduces TypeSafe AI's Jev, a "decision model" that takes text in and returns only probabilities/scores (no text), priced at input-only $0.042/M tokens, and argues that this black-box output shape makes bias concerns and evals more important, not less.

## Source Context

- **Type**: blog-post (with an update dated 22 Sep 2026 announcing `llm-typesafe`)
- **Author credibility**: Simon Willison, creator of Datasette and the `llm` CLI/Python library; prolific hands-on experimenter with LLM tooling. Here he is reporting personal experiments (search reranking, a city-ranking bias probe), not benchmarks.
- **Scope**: Covers Jev's API shape (three question types), pricing, stated weaknesses, suggested use cases, black-box/bias concerns, community reactions and open-weight clones. Does not give accuracy benchmarks, latency numbers, or details of how Jev is built; those live in the linked TypeSafe blog and docs (not read here).

## Extracted Claims

### Claim 1: Jev is a new category of model whose output is typed probabilistic decisions rather than text
- **Evidence**: Description of the API by Willison plus TypeSafe's own framing; no independent verification.
- **Confidence**: emerging
- **Quote**: "Think of Jev as a frontier-intelligence function call: unstructured state in, typed probabilistic decisions out."
- **Our assessment**: The quote is TypeSafe's description, relayed by Willison. It is distinct from structured-output/JSON-mode, where the model still generates tokens; here the output is numeric scores and confidences by construction. Vendor-originated framing, but the API shape is concrete and checkable.

### Claim 2: "Decision models" (Maggie Appleton's term) is a better name than TypeSafe's "System One models"
- **Evidence**: Naming preference; Willison links a tweet from Maggie Appleton.
- **Confidence**: anecdotal
- **Quote**: "I’m with Maggie Appleton, I think “decision models” is a better name for these"
- **Our assessment**: Terminology only, but useful for the guide: "decision model" describes the usage pattern (classify/score/rank), which is the vocabulary we'd want in chapters.

### Claim 3: Pricing is input-only and undercuts even the cheapest text LLM
- **Evidence**: Cites $0.042/M input for Jev vs $0.05/M for GPT-5 Nano; output free.
- **Confidence**: emerging (vendor price list as of the post date)
- **Quote**: "Jev charges only for input—output is free—and the input price of their first model is $0.042 per million tokens—cheaper even than OpenAI’s GPT-5 Nano ($0.05/million)."
- **Our assessment**: The pricing is a point-in-time fact. The structural point matters more: because output is free and fixed-size, cost scales with the document, so asking many questions per document is cheap.

### Claim 4: The API takes one "state" and many questions, evaluated in parallel, with three question types (Noul/yes-no, Choice, Score)
- **Evidence**: API description from the post.
- **Confidence**: emerging
- **Quote**: "Questions are evaluated in parallel, so sending many questions should take a similar time to sending just one."
- **Our assessment**: The "should" is hedged; Willison doesn't show timings. The three question types are listed in the post as: Noul (Bernoulli; float 0–1 that a statement is true), Choice (confidence plus distribution over options), Score (float along a described numeric range). Enables multi-label classification in one call.

### Claim 5: Jev is well suited to anything expressible as a classification task
- **Evidence**: Willison's judgement plus his own experiments; no benchmark.
- **Confidence**: anecdotal
- **Quote**: "It’s great for anything that can be expressed as a classification task—think spam detection, suggesting labels, prioritization and ranking."
- **Our assessment**: Plausible and consistent with the model's output shape. Untested for accuracy versus a small text LLM; treat as a hypothesis.

### Claim 6: Jev is weak on numbers, dates and adversarial content
- **Evidence**: Cites the vendor's own "jaggedness" documentation for Jev 1.13.
- **Confidence**: emerging
- **Quote**: "It’s currently not great with numbers, dates, or “adversarial content”."
- **Our assessment**: Notable that the vendor publishes a jaggedness page. Weakness on adversarial content matters for spam/moderation use, exactly the use case Willison suggests. Docs not fetched by us.

### Claim 7: Search reranking with a cheap first-stage retriever plus Jev scoring is a promising pattern
- **Evidence**: Willison's own experiment; no numbers reported.
- **Confidence**: anecdotal
- **Quote**: "where you fetch 100 likely matches using an inexpensive algorithm like BM25, then have Jev score those 100 candidates for relevance against the original query."
- **Our assessment**: A concrete two-stage architecture (cheap recall, model-based precision). Without quality results this is a pattern description, not evidence that it works better.

### Claim 8: Decision models are a regression toward black-box ML, even worse than text LLMs for explainability
- **Evidence**: Reasoning from output format: only a float is returned, so there is no rationale to inspect.
- **Confidence**: emerging (reasoned argument)
- **Quote**: "Jev doesn’t even give you that: put in all the text you want, the only thing you’re going to get back is a floating point number."
- **Our assessment**: Sound. Note that the preceding sentence in the source concedes text-LLM justifications are also unreliable ("you can’t guarantee that what they say is useful or accurate"), so the difference is one of degree. Also implies no self-explanation debugging loop.

### Claim 9: Bias concerns should be front and center; do not use for high-stakes ranking such as job applicants
- **Evidence**: Argument plus an informal probe: Jev scored Bay Area cities on "Good city?", ranking Cupertino top and East Palo Alto bottom.
- **Confidence**: anecdotal
- **Quote**: "I really hope nobody uses Jev to rank job applicants—that floating point number could conceal all manner of unseen bias baked into the models"
- **Our assessment**: The city probe is a single anecdote and is suggestive rather than proof of bias (the rankings may reflect wealth/demographic correlates in training data, which is the concern). The stronger contribution is the risk framing: a scalar output makes bias hard to see and hard to dissect.

### Claim 10: Evals and structured experiments matter more for decision models, and are cheap to run
- **Evidence**: Cost argument: experiments cost cents.
- **Confidence**: emerging
- **Quote**: "Thankfully, Jev is so cheap that running hundreds or even thousands of experimental prompts through it costs just a few cents."
- **Our assessment**: Good practical point: low cost plus scalar outputs makes bulk probing (e.g., counterfactual/paired-input tests for bias) feasible. Willison also says "experimentally picking that bias apart is going to be a tricky business," so cheap doesn't mean easy.

### Claim 11: Rapid community uptake, including open-weight clones and a benchmark, within about a week
- **Evidence**: Links to Kev (Qwen 3.5-based 0.8B/4B/9B models), JevBench, and creative hacks (jevchat, jev-leftpad, jev-2048).
- **Confidence**: anecdotal
- **Quote**: "Given Jev was released just under a week ago, the amount of activity around it is extremely impressive."
- **Our assessment**: Signals interest, not quality. The hacks (chat via next-symbol choice, left-pad via a Choice question) illustrate that Choice questions can emulate constrained generation, at absurd cost in calls. Kev and JevBench were not examined by us.

### Claim 12: Tooling integration arrived quickly via the `llm` CLI plugin
- **Evidence**: Update of 22 Sep 2026: Willison released `llm-typesafe` and shows an example.
- **Confidence**: settled (the plugin exists per the post)
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: The example asks whether a message "explicitly request[s] a refund" using a system-prompt-as-question, showing the ergonomics: one text, one yes/no question, one probability back.

## Concrete Artifacts

```
# Source: Simon Willison, "Using Jev from LLM" (update 22 Sep 2026)
llm -m jev 'Please refund my last payment.' \
  -s 'Does this message explicitly request a refund?'
```

Question types as described in the post (paraphrased summary, not verbatim):
- Noul (yes/no): statement → float in [0,1]
- Choice: options → confidence + distribution across options
- Score: ordered numeric levels with descriptions → float on that range

Pricing datum from the post: Jev $0.042 / M input tokens, output free; GPT-5 Nano $0.05 / M.

Bias probe from the post: Jev asked "Good city?" (yes/no) for each Bay Area city; Cupertino ranked top, East Palo Alto bottom.

## Cross-References

- **Corroborates**: None directly. Loosely adjacent to `blog-cursor-router-model-classifier.md` Claim 1 and Claim 3, which describe a cheap classifier used to make routing decisions in front of expensive models; both show classifiers replacing generative calls for decision work.
- **Contradicts**: None found. No existing note takes a position on decision models.
- **Extends**: `blog-hamel-eval-smell.md` Claim 1 (hard-to-evaluate outputs are a design smell): a bare float is an extreme instance where nothing is exposed for a user to verify. Also `blog-cursor-router-model-classifier.md` Claim 6 on offline evals being small and hard to reduce to a rubric, since bias in scalar scores needs designed experiments.
- **Novel**: The decision-model output shape (probabilities only, no text), input-only pricing, the BM25 + model-scoring reranking pattern, and the explicit "black boxes are back" bias/eval argument are all new to the corpus.

## Guide Impact

- **Structured outputs / model-selection chapters (Ch03–04)**: Add a short section on decision models as a distinct output shape from JSON-mode structured outputs, with the three question types and the classification/ranking/reranking use cases. Cite this note and mark as emerging (single vendor, single commentator).
- **Cost chapter (Ch05)**: Note that pricing can be input-only, changing the cost calculus for many-questions-per-document workloads ($0.042 vs $0.05 per M input for GPT-5 Nano as of Sep 2026). Time-sensitive; flag for re-verification.
- **Evals chapter (Ch06)**: Add the guidance that opaque scalar outputs raise the eval bar: run bulk, cheap paired experiments to probe bias, and avoid high-stakes ranking of people without them. Use the Cupertino/East Palo Alto probe as a cautionary anecdote, labeled anecdotal.
- **Production patterns (Ch07)**: Candidate pattern: cheap first-stage retrieval (BM25) plus decision-model scoring of top ~100 candidates. Wait for corroborating evidence before recommending.

## Extraction Notes

- Read the full post via the raw HTML of the source URL, including the 22 Sep update. The linked TypeSafe announcement, Jev 1.13 jaggedness docs, HN threads, Kev and JevBench were NOT followed; claims about them rest on Willison's summary.
- The Prospector comments mention "Kev" and "JevBench"; both are in the source. Claim 12 has no verbatim quote because the relevant text is code plus prose I chose not to splice.
- No contradictions filed: no existing note covers this topic.
