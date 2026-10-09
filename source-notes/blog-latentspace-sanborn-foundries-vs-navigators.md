---
source_url: https://www.latent.space/p/foundries-vs-navigators-lowering
source_type: blog-post
title: "Foundries vs Navigators: Lowering the Cost of Science"
author: Adrian Sanborn (guest post, Latent Space "AI for Science"; CEO and co-founder, Endura Therapeutics)
date_published: 2026-09-24
date_extracted: 2026-10-09
last_checked: 2026-10-09
status: current
confidence_overall: anecdotal
issue: "#4016"
---

# Foundries vs Navigators: Lowering the Cost of Science

> A biotech CEO's first-hand account of how cheap code and cheap LLM "expert-level depth" changed one company's analysis loops, internal tooling (build over buy), and disease-target triage, with explicit caveats on verification, reproducibility and where the pattern does not transfer.

## Source Context

- **Type**: blog-post (guest essay on Latent Space's "AI for Science" series)
- **Author credibility**: Sanborn holds a Stanford CS PhD (largely spent at the bench) and is CEO/co-founder of Endura Therapeutics. Per the page, "Adrian did a CS PhD at Stanford and spent much of it running experiments at the bench, which makes him one of the rare people who can tell you what an LLM is doing to a codebase and to a wet lab." He reports his own company's practice, with a commercial interest in the narrative.
- **Scope**: Strategy essay on biotech. Covers (1) agile analysis code, (2) in-house data portals vs. vendor software, (3) a two-stage fleet-of-LLM-agents disease triage, (4) speculation about on-demand software. Contains no code, config, prompts, or measured metrics (only the author's own estimates). Science-specific material (CRISPR-in-a-pill, drug repurposing) is out of scope for this extraction.

## Extracted Claims

### Claim 1: Cheaper coding yields more software in software, but in science physical experiments gate everything, so "thinking got cheap and doing did not"
- **Evidence**: Argument by assertion; footnote 2 invokes the Jevons paradox for software ("every drop in the cost of writing code has so far been followed by more software rather than fewer engineers").
- **Confidence**: emerging
- **Quote**: "Thinking got cheap and doing did not."
- **Our assessment**: A useful framing of where AI speedups stop: wherever verification is slow or physical, cheaper generation does not raise end-to-end throughput. Maps onto software domains with slow verification (hardware, production rollout, regulated change). The Jevons claim is stated, not evidenced.

### Claim 2: Cheap code makes it practical to change experimental analysis in step with a changing protocol, removing a disincentive to propose experimental changes
- **Evidence**: Practitioner reasoning, no measurement. The historical seam between the person who understands the experiment and the person who writes the analysis is said to cause fewer experimental changes proposed.
- **Confidence**: anecdotal
- **Quote**: "Now that writing code is fast, adapting the analysis to a modified protocol is an afternoon's work rather than a project."
- **Our assessment**: Plausible and consistent with the general "requirements churn is cheap to absorb" argument. Note the author's explicit contrast: in engineering, changing requirements signal poor planning, in research they are "the objective". The transferable point is that rework cost shapes which options a team is willing to explore.

### Claim 3: Dashboards that took days now take minutes to hours, and the scientist who ran the experiment can present her own results instead of queuing behind a computational specialist
- **Evidence**: Single screenshot caption ("An internal dashboard at Endura Therapeutics, built in a few hours") and assertion. Earlier the author says analysis "takes an hour instead of a week".
- **Confidence**: anecdotal
- **Quote**: "Now the scientist who ran the experiment and has the context presents their own results."
- **Our assessment**: Believable but unquantified; the "days to minutes" figure is the author's own. The real claim is organizational: removing the analyst-as-gatekeeper queue.

### Claim 4: The old rule "never build what you can buy" is replaced by "build the tools that shape how you think", because bought software outsources the question of how you accomplish your goals
- **Evidence**: Reasoning plus one example: an in-house data portal said to take one day to implement, while "deciding what the portal should do can take weeks". No comparison data on cost or outcomes.
- **Confidence**: anecdotal
- **Quote**: "The old rule was “never build what you can buy”. The new rule is build the tools that shape how you think."
- **Our assessment**: The most quotable build-vs-buy statement in the piece, but it is a single-company, early-stage-startup claim. The useful nuance is that implementation is cheap while specifying behavior is the costly part. It also rests on a vendor-lowest-common-denominator argument ("These vendors build one system for a thousand labs"), which applies most to niche internal tooling, not commodity infrastructure.

### Claim 5: The build-over-buy shift has stated costs and limits: less polish, no support team, and large organizations with validation and contractual burdens will struggle to follow
- **Evidence**: Author's own caveat, not evidence-backed. Also states navigation "runs fastest at early-stage startups, which have no legacy to shed".
- **Confidence**: emerging
- **Quote**: "There are tradeoffs: an in-house portal is less polished and there is no support team to call."
- **Our assessment**: Valuable because the author names the counter-arguments. This directly answers the triage question about evidence beyond one anecdote: there is none, and the author concedes the pattern is not universal.

### Claim 6: "Every research team can be its own forward-deployed engineer", because the best internal tools come from engineers embedded with the users
- **Evidence**: Appeal to long-standing software practice; no example beyond the Endura portal.
- **Confidence**: anecdotal
- **Quote**: "Now every research team can be its own forward-deployed engineer."
- **Our assessment**: Extends the FDE discussion from engineers deployed to customers to domain experts who can themselves build. Compatible with, but distinct from, the Sierra FDE material (see Cross-References).

### Claim 7: A fleet of LLM research agents ran a two-stage triage over ~500 disease targets (≈3-page reports each), then ~100 survivors (≈30-page reports each)
- **Evidence**: Author-reported description of Endura's own pipeline. No prompts, code, model names, cost, or error rates are given.
- **Confidence**: anecdotal
- **Quote**: "We built a two-stage triage and pointed a fleet of LLM research agents at it."
- **Our assessment**: Concrete enough to describe the architecture: cheap broad pass filtering on foundational yes/no questions (prevalence, existing coverage, mechanism fit), then expensive deep pass. This is a funnel pattern generalizable to evaluating many candidate libraries/designs, but only the shape is transferable; nothing here is reproducible.

### Claim 8: Second-pass prompts were written as a "skeptical expert" rather than a summarizer, forcing the agent to name failed prior programs, why they failed, and what would have to be true to succeed
- **Evidence**: Author's description of prompt design; actual prompts not shown.
- **Confidence**: anecdotal
- **Quote**: "We wrote the second-pass prompts to behave like a skeptical expert rather than a summarizer: name the programs that failed, why each failed, and what would have to be true for us to succeed where they didn’t."
- **Our assessment**: The most transferable prompt-design idea: ask for prior failures and falsification conditions rather than a summary. Untested here against a baseline.

### Claim 9: Scale estimates: stage one would have needed about one person-year of reading and stage two about a century of expert time
- **Evidence**: Author's own back-of-envelope estimate, vendor-reported.
- **Confidence**: anecdotal
- **Quote**: "At the old rate, the first stage would have required about one person-year of reading, and the second closer to a century of expert time."
- **Our assessment**: Treat as order-of-magnitude marketing-style framing, not a measurement. Notably it compares against a counterfactual nobody would have run, so the real benefit is "a search that was not possible", not saved time.

### Claim 10: Agent output is verified by checking the second pass against primary sources, with human diligence only for selected programs; errors were tolerated because stage-one mistakes only cost missed opportunities
- **Evidence**: Main text plus footnote 6; no error rate given. The author concedes errors occurred.
- **Confidence**: anecdotal
- **Quote**: "The second pass still gets checked against primary sources and selected programs receive the full human diligence it always would have."
- **Our assessment**: Key verification claim. The error-tolerance argument is asymmetry-based: footnote 6 says "a mistake in the first pass only means a missed opportunity, not time lost chasing a bad idea". I.e. false negatives are cheap, false positives are caught downstream. A good design rule: place high-recall/low-cost agent stages where errors are non-damaging and put verification before irreversible commitment. No rate of checking ("selected") is specified.

### Claim 11: Early "no" from expert-level depth at scale is the main value, since the expensive mistakes in research are unknown ones found months later
- **Evidence**: Reasoning; illustrative list of what a specialist could say in a sentence.
- **Confidence**: emerging
- **Quote**: "In research, the expensive mistakes are the unknown ones."
- **Our assessment**: Transfers to engineering design review: breadth-first falsification of candidate approaches before committing. Not demonstrated with outcomes.

### Claim 12: Future direction: software stops being a work product and is assembled on demand around the question, but analysis generated this way has weaker provenance and reproducibility
- **Evidence**: Speculation; the reproducibility caveat is in footnote 7.
- **Confidence**: anecdotal
- **Quote**: "Software stops being a work product and becomes something that appears around the question."
- **Our assessment**: Speculative. Footnote 7 ("If the code behind a figure was assembled for one question, its provenance is weaker than a versioned pipeline’s.") names an unresolved tension with versioned, reviewable pipelines, relevant to any guide advice on disposable agent-written analysis code.

## Concrete Artifacts

No code or configuration is provided. The only concrete artifacts are the pipeline description and the prompt directive (attributed to Sanborn, Latent Space, 2026-09-24):

```
Stage 1: ~500 disease targets -> ~3-page report each (LLM research agents)
         filter: Is the disease prevalent enough? Is it already addressed by
                 existing drugs? Would the target-lowering effect relieve the disease?
Stage 2: ~100 surviving targets -> ~30-page report each
         prompt stance: "skeptical expert rather than a summarizer: name the programs
                 that failed, why each failed, and what would have to be true for us
                 to succeed where they didn’t"
Verification: stage 2 "checked against primary sources"; selected programs get full human diligence
Author estimates of manual equivalent: ~1 person-year (stage 1), ~a century of expert time (stage 2)
```

(The filter questions are a paraphrase of the source's sentence listing them, not a quotation.)

## Cross-References

- **Corroborates**: `blog-latentspace-meurer-agent-engineer-fde.md` Claim 10 (cheap code authorship shortens the path from user insight to shipped product; Sanborn's analysis-change and in-house-portal examples are a domain-expert variant of the same mechanism). `blog-latentspace-aiewf-loops-software-factories-dispatch.md` Claim 10 (Cursor positions forward-deployed engineering within the software-factory shift) is loosely consistent with Sanborn's "every research team can be its own forward-deployed engineer", though that note is about engineers deployed to customers.
- **Contradicts**: None found. No filed contradiction issue. (Sanborn's concession that large organizations will struggle is a conditioning variable on build-vs-buy, not an opposed claim.)
- **Extends**: `blog-latentspace-lila-sciences-lab-data-center.md` and `blog-latentspace-xaira-causal-data-drug-discovery.md` (same "AI for Science" series; both are "foundry" companies in Sanborn's taxonomy. Those notes cover the foundry side, this one the "navigator" side). `blog-latentspace-lila-sciences-lab-data-center.md` Claim 11 (models reaching correct conclusions while skipping the experiment in their stated reasoning, so physical verification matters) pairs with Sanborn's "thinking got cheap and doing did not".
- **Novel**: The foundry/navigator taxonomy; a first-hand build-over-buy rule with named costs; a two-stage broad-then-deep LLM triage funnel with skeptical-expert prompting; asymmetry-based justification for tolerating first-stage agent errors; an explicit reproducibility caveat for on-demand analysis code.

## Guide Impact

- **Chapter 05 (team adoption)**: Possible short example supporting the build-vs-buy shift for niche internal tools ("build the tools that shape how you think"), explicitly flagged as a single early-stage-startup practitioner claim with named limits (polish, support, large-org validation). Do not present as settled.
- **Chapter 00 (principles)**: Optional supporting framing that AI speedups concentrate where verification is cheap and stall where verification is slow or physical; cite Claim 1 with anecdotal confidence.
- **Chapter 02 (harness engineering)**: The funnel pattern (cheap broad pass, deep skeptical pass on survivors, verification against primary sources before commitment) is a candidate illustration for evaluating many candidate libraries/designs, but only as shape; no reproducible evidence. Recommend waiting for a stronger software-domain source before adding guidance.

## Extraction Notes

- Read the full article (via direct HTML fetch, text extracted) including all eight footnotes; no paywall. The page's linked paper (footnote 1) was not followed because the triage asked only for the verification and build-vs-buy claims.
- All quotes were copied verbatim from the fetched text; curly apostrophes are preserved as in the source.
- Evidence is entirely author-reported from one company, with no metrics, code or prompts. All throughput figures are the author's estimates.
- Cross-reference claim numbers were checked against the cited notes' numbered headings.
