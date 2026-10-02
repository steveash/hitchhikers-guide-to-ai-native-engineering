---
source_url: https://ghuntley.com/readable/
source_type: blog-post
title: "software doesn't need to be readable anymore. it needs to be explainable."
author: Geoffrey Huntley
date_published: 2026-10-02
date_extracted: 2026-10-02
last_checked: 2026-10-02
status: current
confidence_overall: anecdotal
issue: "#3862"
---

# software doesn't need to be readable anymore. it needs to be explainable.

> Huntley's write-up of a 21-minute AI21 YAAP podcast appearance argues that code should be optimized for agents and explainable to humans on demand (not readable cold), with strong typing as agent "back pressure", languages becoming fungible via agent porting, and simulator-first development — all asserted from personal experience, not measured.

## Source Context

- **Type**: blog-post (written companion to a podcast episode; the 21-minute video was not watched, only the post and chapter list)
- **Author credibility**: Geoffrey Huntley, originator of the Ralph loop and author of the Loom research project; self-reports no hand-written code for two years. Strong practitioner, but claims here are first-person and unmeasured. Note he has disclosed an Antithesis affiliation in a prior post (see `blog-ghuntley-engineer-away-slop.md` Claim 11).
- **Scope**: AI economics and model spend, unikernels/OS design, readable-vs-explainable code, type systems as feedback, language-design evolution, cross-language porting, and his in-progress source-control rebuild. Does not provide benchmarks, cost figures for his own setup, or results for the language-design experiments ("No results to show yet").

## Extracted Claims

### Claim 1: Code's goal should shift from human readability to being explainable to a human by a model on demand
- **Evidence**: A deliberately obfuscated Haskell function (a reverse-then-bubble-sort of a string) that an LLM explains in Python when prompted "explain this function to me as if you were explaining it to my son or daughter but in Python as a reference." No comparison, no user study.
- **Confidence**: emerging
- **Quote**: "The artifact doesn't need to be optimized for a human to read cold. It needs to be something a model can explain to a human on demand."
- **Our assessment**: Compelling demo for small, self-contained functions, but one toy example. It leaves open whether explanations stay trustworthy for large, stateful systems, and who verifies the explanation is correct (the explainer is itself an LLM). Pairs with intent-debt/comprehension concerns in the corpus.

### Claim 2: Strong static types act as back pressure, making Rust far more agent-maintainable than Python and enabling cheaper models
- **Evidence**: Author's experience; a "continuum of power" from Haskell (strictest) through Rust to Ruby/Python/PHP/Perl.
- **Confidence**: emerging
- **Quote**: "Types are a form of verification. They provide back pressure: compiler errors that the LLM picks up and fixes automatically, every loop."
- **Our assessment**: Mechanism is plausible and consistent with compiler-in-the-loop practice in migrations. No measurement is offered for "far more maintainable". Python with type checkers/linters is a middle path the post ignores.

### Claim 3: Choosing a language that verifies for you lets you use cheaper models
- **Evidence**: Author runs a mix of low/no-reasoning GPT and GLM/Kimi; attributes feasibility to language choice.
- **Confidence**: anecdotal
- **Quote**: "Pick a language that does the verification for you, and you need less intelligence to stay on the rails."
- **Our assessment**: Useful cost-routing heuristic (verification substitutes for model intelligence), untested here. Model names are as given by the author ("GPT 6.1 sol").

### Claim 4: Frontier intelligence is not needed for every task; model capability has been roughly flat since the Sonnet 3.5 → Opus 4 era, and how you use the model matters more
- **Evidence**: Assertion; mentions open-weights GLM on Baseten and cheap yearly GLM plans versus big-lab plans.
- **Confidence**: anecdotal
- **Quote**: "It's not about the model anymore. It's about how you use the model."
- **Our assessment**: The "capability has been marginal since" claim sits in tension with sources documenting large recent model jumps (e.g. the Bun rewrite notes relying on a new frontier model); worth treating as one author's opinion, not filed as a formal contradiction since it is not evidence-backed.

### Claim 5: AI economics are "cooked" at the lab level even as individual development has fundamentally changed
- **Evidence**: Cites adoption vs capital deployed; labs hiring professional-services staff; refers readers to Ed Zitron. No numbers.
- **Confidence**: anecdotal
- **Quote**: "Both things can be true at once. The economics can be cooked, and how I develop software has completely, fundamentally changed."
- **Our assessment**: Macro opinion outside the guide's core scope; the useful bit is the separation of vendor economics from practitioner productivity.

### Claim 6: Many "how computers work" conventions exist only to make machines legible to human operators; removing the human reopens those design decisions (unikernels, deleting the OS layer)
- **Evidence**: Personal experiments with OCaml, MirageOS, and rebuilding "essentially Erlang as a distributed operating system"; Kubernetes operator loops as an example of humans already out of the loop. Author admits it may be a dead end.
- **Confidence**: anecdotal
- **Quote**: "Delete the OS layer, and you delete that class of problem."
- **Our assessment**: Speculative prediction ("Unikernels are going to come back into fashion hard"). Interesting framing, no evidence of adoption.

### Claim 7: Language evolution is paced to human learning; with agents doing migrations, designers can ship breaking changes plus a skills pack and use decades of PL theory
- **Evidence**: Anecdotes: LINQ/monads taking years to be accepted, Python 2→3; cites José Valim's post on agent-first languages.
- **Confidence**: anecdotal
- **Quote**: "But what happens if the language designer ships a skills pack alongside the breaking change, and the agent just does the migration?"
- **Our assessment**: Novel and testable; the author concedes "No results to show yet." Relevant to skill-pack distribution as a migration mechanism.

### Claim 8: Programming languages are now fungible because agents can port cheaply when the result is easy to verify
- **Evidence**: Anecdote of an Australian medical founder whose ASP.NET Web Forms rewrite was quoted as "years" by the team and finished in a week by the founder running loops; ls ported to Rust via objdump by a reader (Daniel Joyce, ls-rs repo).
- **Confidence**: emerging
- **Quote**: "Porting is easy when the end result is easy to verify."
- **Our assessment**: The qualifier (verifiability) is the important part and matches the Bun rewrite and Anthropic migration playbook; the ASP.NET story is unverifiable hearsay. The "CTO maintains three language teams" business-case argument ignores maintenance/ownership after the port.

### Claim 9: Ecosystem adoption and library availability no longer constrain language choice ("V8 hot rod")
- **Evidence**: Analogy; links to his "what is the point of libraries now that you can just generate them?" post.
- **Confidence**: anecdotal
- **Quote**: "Like, what libraries exist in this ecosystem don't factor into my decision to create a new project these days."
- **Our assessment**: Overstated for security-sensitive or complex-domain libraries (crypto, parsers), and ignores supply of training data in new languages. Treat as a contrarian provocation.

### Claim 10: Software factories need better models, better languages, or revived CS techniques like simulators; simulator-first development keeps agents on the rails
- **Evidence**: Author's in-progress distributed source-control system in Rust (encrypted contents, per-agent claims giving a materialized view, path-level ACLs), built simulator-first.
- **Confidence**: anecdotal
- **Quote**: "It's a distributed system, so I'm building it in Rust and building the simulator first, then driving the agent to validate everything through the simulator."
- **Our assessment**: Consistent with his earlier deterministic-simulation claim; still no results or public evidence of outcomes. Source-control-for-agents (claims/ACLs) is a distinct, novel design idea.

### Claim 11: Git is approaching end-of-life for agent-scale work and should be replaced
- **Evidence**: Opinion, citing Piper/Rosie, EdenFS/Mononoke/Sapling, Phabricator as better systems.
- **Confidence**: anecdotal
- **Quote**: "I think Git is somewhat end-of-life; I really wish people would stop trying to extend Git's lifespan."
- **Our assessment**: Opinion; Loom is explicitly "research" and "not intended" to be usable.

## Concrete Artifacts

Obfuscated Haskell (from the post) that the LLM was asked to explain:

```haskell
f :: String -> String
f = g . h
  where
    h []     = []
    h (x:xs) = h xs ++ [x]
    g x =
      let (y, z) = p x
      in if y then z else g z
    p []       = (True, [])
    p [x]      = (True, [x])
    p (x:y:xs)
      | x > y     = let (a, b) = p (x:xs) in (False, y:b)
      | otherwise = let (a, b) = p (y:xs) in (a, x:b)
```

Prompt used (from the post): "explain this function to me as if you were explaining it to my son or daughter but in Python as a reference."

Source-control design bullets (from the post): contents are encrypted; agents get a claim, which provides a materialized view of the repository; real ACLs, e.g. sharing a sub-path with a contractor.

## Cross-References

- **Corroborates**: `blog-ghuntley-engineer-away-slop.md` Claim 8 (simulators are cheaper to build now and expose bug classes otherwise missed) and Claim 9 (verification tooling as a software-factory component); `blog-anthropic-code-migration-playbook.md` Claim 5 (a "judge" that evaluates original and target code is a prerequisite for migration), Claim 10 (compiler placed in the implementation loop), and Claim 11 (smaller models for high-volume fan-out); `blog-simonwillison-rewriting-bun-rust.md` Claim 2 (language-independent test suite as conformance suite) for the "porting is easy when verifiable" claim.
- **Contradicts**: None filed. The "capability mostly flat since Sonnet 3.5→Opus 4" aside (Claim 4) is in tension with the model-jump framing in `blog-pragmaticengineer-bun-rust-rewrite.md` Claim 6, but it is unsupported opinion and does not rise to a contradiction issue.
- **Extends**: `blog-ghuntley-engineer-away-slop.md` (same author; adds language-design and type-as-verification dimensions), `blog-ghuntley-miami-hot-takes.md` (same hot-take register).
- **Novel**: Readable→explainable framing with an explain-on-demand demo; types as agent back pressure as a language-selection criterion; skills-pack-shipped-with-breaking-change; agent claims/ACLs source control; unikernel/OS-deletion argument.

## Guide Impact

- **Verification/back-pressure chapter**: Add the "language choice as verification budget" heuristic (strict types substitute for model intelligence), citing Claim 2–3 as anecdotal and noting the lack of measurement.
- **Code-generation/patterns chapter**: Add "explainability over readability" as a contested position, with the explain-on-demand pattern and its risk (explainer correctness) flagged.
- **Migration material**: Cite Claim 8 as additional anecdotal support that verifiability gates porting feasibility; do not cite the ASP.NET story as evidence.
- **Future-directions/ecosystem material**: Mention skills-pack-with-breaking-change (Claim 7) as an untested idea.

## Extraction Notes

- Fetched the raw HTML and read the full post text; did not watch the 21-minute video or follow the linked Valim post or the libraries post.
- Several quoted-adjacent details (model names like "GPT 6.1 sol") are reproduced as the author wrote them.
- Source is thin on evidence; confidence kept at anecdotal overall.
