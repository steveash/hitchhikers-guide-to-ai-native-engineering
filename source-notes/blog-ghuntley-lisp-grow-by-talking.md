---
source_url: https://ghuntley.com/lisp/
source_type: blog-post
title: "an application in lisp you grow by talking to it"
author: Geoffrey Huntley
date_published: 2026-10-05
date_extracted: 2026-10-06
last_checked: 2026-10-06
status: current
confidence_overall: anecdotal
issue: "#3929"
---

# an application in lisp you grow by talking to it

> Huntley introduces Jiti, a small Common Lisp kernel where an LLM uses inspect/define/execute tools to grow a running application through conversation, offered as a concrete demonstration of "the product builds the product from the product" — a working demo, but with no evaluation, metrics, or failure analysis.

## Source Context

- **Type**: blog-post (personal blog, ghuntley.com, 5 Oct 2026). Short (~1,000 words), with a 41-second demo video, two SVG architecture diagrams, a link to the GitHub repo (ghuntley/jiti) and a tweet embed.
- **Author credibility**: Creator of the Ralph loop and prolific practitioner of agentic coding; also building "Latent Patterns" (the post references an "embedded software factory" inside that product). Claims here are design opinions and a demo, not measured results.
- **Scope**: Covers the Jiti architecture (controller, persistent worker, tool interface), the vocabulary-accumulation idea, and the "no compile/CI" thesis. Does NOT cover safety/sandboxing, failure rates, cost, multi-user concurrency, or how it scales beyond toy functions. A promised follow-up post on "the product develops the product, in the product" is not yet published. The repo code and video were not examined; only the blog text.

## Extracted Claims

### Claim 1: A software factory is about developing the product while it runs, inside the product itself, not about automating existing process
- **Evidence**: Author's opinion; the embedded-factory preview in Latent Patterns is only linked, not detailed here.
- **Confidence**: anecdotal
- **Quote**: "It's about using this substrate so you can develop your product while it runs whilst in the product itself."
- **Our assessment**: A distinct framing from the "factory = pipeline of agents + verification" view in other notes. Interesting vision, but unevidenced here; Latent Patterns is also the author's own product.

### Claim 2: Anyone in the company should be able to develop the product in the product, with no external vendor tooling
- **Evidence**: Assertion only.
- **Confidence**: anecdotal
- **Quote**: "The only tool that exists is your product itself. The product should build the product from the product."
- **Our assessment**: Raises governance questions (who reviews, who can change production behaviour) that the post does not address.

### Claim 3: Software could be grown by chatting with a live application, with no compilation steps
- **Evidence**: The Jiti demo (41s video) and open-source repo.
- **Confidence**: emerging
- **Quote**: "You ask for a capability, the model writes Lisp, and the application permanently acquires that capability until you ask for that capability to be removed."
- **Our assessment**: Credible as a mechanism given Lisp's image-based model. "Permanently acquires" implies persistent revisions but the post gives little detail on rollback or review.

### Claim 4: The kernel provides machinery to inspect, change, execute and recover a managed Lisp world; behavior comes entirely from what the user prompts for
- **Evidence**: Architecture description and diagram (controller routes actions; persistent worker owns evaluation and live restarts; world adapter defines managed resources, catalogue and recovery hooks).
- **Confidence**: emerging
- **Quote**: "The kernel supplies the machinery to inspect, change, execute, and recover a managed Lisp world."
- **Our assessment**: A clean separation between a small trusted kernel and an LLM-authored application layer. Recovery hooks are the safety-relevant part and are underspecified in the post.

### Claim 5: The model is grounded by tool calls and real worker observations, not by guessing
- **Evidence**: Description of the loop: model receives request, operating instructions, tool definitions and state observations; can list functions, read a definition, propose source, or execute an expression.
- **Confidence**: emerging
- **Quote**: "Actual worker results inform its next step; accepted functions and managed data remain available for later requests."
- **Our assessment**: Matches the general agent-harness pattern of observe→act→observe with real tool results; here the "environment" is a live REPL image.

### Claim 6: Accepted definitions run as ordinary code with no further inference
- **Evidence**: Design description.
- **Confidence**: emerging
- **Quote**: "Calling it does not inherently require another inference request."
- **Our assessment**: Important economic point: the LLM is used at authoring time, and runtime behaviour is deterministic code — contrasts with agent-per-request designs. Not quantified.

### Claim 7: Two tools suffice — develop_form (change) and execute_form (use) — sharing one evaluator and transaction machinery
- **Evidence**: Tool interface description.
- **Confidence**: emerging
- **Quote**: "The distinction helps the model choose whether the user is asking to change the application or simply use it."
- **Our assessment**: A useful tool-design pattern: split by user intent (mutate vs. invoke) while sharing the underlying machinery. The claimed benefit (better model choice) is not tested.

### Claim 8: The application accumulates an executable vocabulary through use, with composition handled by Lisp itself
- **Evidence**: Worked example: uppercase-string and reverse-string composed, then saved as shout-backwards.
- **Confidence**: anecdotal
- **Quote**: "The application accumulates an executable vocabulary through use."
- **Our assessment**: Compelling for tiny pure functions; the example is trivial and says nothing about managing a growing, possibly conflicting catalog.

### Claim 9: Lisp's interactive machinery (definitions, inspection, conditions, restarts) deserves the credit; this makes the language a good agent substrate
- **Evidence**: Appeal to decades-old language features.
- **Confidence**: emerging
- **Quote**: "Definitions, inspection, conditions, and restarts have been there for decades."
- **Our assessment**: Plausible and consistent with REPL-driven agent work. Tension with Huntley's own statement that "$language is best" claims won't hold — here a specific language property is doing the work.

### Claim 10: Compile + CI/CD phases after an agent writes code are becoming "undefined"
- **Evidence**: Opinion; demo has no build step.
- **Confidence**: anecdotal
- **Quote**: "the idea that an agent writes source code and then there's a costly compilation phase involving CI/CD is now truly undefined now that we have AI"
- **Our assessment**: Contestable. Other Huntley notes stress verification/back-pressure; removing the CI gate removes a main verification point. The post's "caller safety checks govern acceptance" is the only gate mentioned.

### Claim 11: Programming languages will converge toward an as-yet-undefined "something"; claims that a given language is best won't remain true
- **Evidence**: Opinion.
- **Confidence**: anecdotal
- **Quote**: "It's very clear, however, that programming languages will converge toward something, but that 'something' is undefined for now."
- **Our assessment**: Consistent with the language-fungibility view in blog-ghuntley-readable-explainable (Claims 8–9).

## Concrete Artifacts

Tool interface (from the post, ghuntley.com/lisp/):

```
develop_form adds, redefines or removes functionality.
execute_form calls functionality that exists, including combinations of existing functions.
```

Composition example (from the post):

```lisp
(reverse-string (uppercase-string "Hello"))

(defun shout-backwards (text)
  (reverse-string (uppercase-string text)))
```

Architecture summary (post diagram caption): controller routes actions; persistent worker owns evaluation and live restarts; world adapter defines managed resources, catalogue and recovery hooks; accepted managed changes become durable revisions. Repo: github.com/ghuntley/jiti ("Live Common Lisp image repair with OpenAI tools, persistent revisions, and a conversational CLI").

## Cross-References

- **Corroborates**: blog-ghuntley-readable-explainable.md Claim 8 (languages are fungible) and Claim 6 (conventions existing for human legibility can be reopened); blog-ghuntley-engineer-away-slop.md Claim 2 (software authoring commoditized, everyone can be a developer) in the "everyone in the company can develop the product" sense.
- **Contradicts**: None filed. Soft tension (a difference of emphasis, not a filed contradiction): blog-ghuntley-engineer-away-slop.md Claim 9 positions verification tooling (deterministic testing, adversarial review, pre-commit analyzers) as central to software factories, while this post downplays the CI/CD gate and relies on in-kernel acceptance checks.
- **Extends**: blog-ghuntley-readable-explainable.md Claim 10 (software factories need revived CS techniques) — Jiti is an example of reviving a classic technique (live Lisp images).
- **Novel**: Live image-based "grow by conversation" development; the develop_form/execute_form intent split; runtime-without-inference for accepted capabilities; the "product builds the product" definition of a software factory.

## Guide Impact

- **Chapter 04 (tools)**: Candidate example of tool design by intent (mutate vs. invoke sharing one evaluator/transaction layer); cite as anecdotal/emerging.
- **Chapter 05 (paradigms)**: Could add as an example of a "no build loop, live-system" paradigm and of AI used at authoring time with deterministic execution afterward. Flag that it lacks evidence on safety and scale.
- **Software-factory discussion**: Add the "factory inside the product" framing as a minority view alongside the pipeline-and-verification view; note the absence of verification detail.
- Recommend waiting for the promised follow-up post and any user reports before making stronger recommendations.

## Extraction Notes

- Fetched the full post HTML via curl and read all text; quotes were copied from the extracted text. The video, SVG diagrams and GitHub repo were not inspected (the repo link was not followed).
- Quotes in Claims 1 and 10 preserve the source's original wording and grammar ("now truly undefined now").
- Confidence is anecdotal overall: single-author demo, no metrics, author has a commercial interest in Latent Patterns.
