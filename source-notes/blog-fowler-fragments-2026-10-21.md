---
source_url: https://martinfowler.com/fragments/2026-10-21.html
source_type: blog-post
title: "Fragments: October 21"
author: Martin Fowler (curator); primary linked source — Cindy Sridharan, "How to effectively debug when you no longer understand the code"; also Gergely Orosz (X)
date_published: 2026-10-21
date_extracted: 2026-10-22
last_checked: 2026-10-22
status: current
confidence_overall: anecdotal
issue: "#4275"
---

# Fragments: October 21 (Martin Fowler, summarizing Cindy Sridharan on agent debugging)

> Fowler's summary of Sridharan's long article gives an agent-debugging method: collect raw facts first, read code last, pick a control, tabulate hypotheses against signals, validate each survivor against every fact, and keep the human in the role of choosing controls and constraints.

## Source Context

- **Type**: blog-post (Fowler's "Fragments" link-blog, 21 October 2026; four sections separated by snowflake dividers). Only the third section is relevant to the guide.
- **Author credibility**: Martin Fowler is Chief Scientist at Thoughtworks; `martinfowler.com` is a `trusted-feed` source. The quoted author, Cindy Sridharan, is a practitioner known for observability and distributed-systems writing (Fowler: "I've always found Cindy Sridharan's writing to be worth reading"). Her evidence is three of her own bug hunts, reported second-hand here.
- **Scope**: Fowler summarizes and quotes the article; he does not give the bugs' details. No configs, metrics, or transcripts.
- **Not extracted**: Orosz's "No AI" essay-competition frustration and Fowler's AI-voice caveats (about AI-authored prose, not engineering practice); the Grace Hopper Celebration cancellation (off-topic).
- **Primary source NOT read**: The Medium article (https://copyconstruct.medium.com/how-to-effectively-debug-when-you-no-longer-understand-the-code-bd3dcb2c5f7b) returned HTTP 403 to both curl and WebFetch. Every quotation below is as reproduced on Fowler's page; none was checked against Sridharan's original. Fowler says Medium estimates the article as a 64 minute read, so this note captures only a small slice of it.

## Extracted Claims

### Claim 1: Agents are not humans, so agent workflows should lean into agent strengths instead of copying human problem-solving patterns
- **Evidence**: Authority/observation from Sridharan's three bug hunts, quoted by Fowler. No measurement.
- **Confidence**: anecdotal
- **Quote**: "Agents are not humans. They’re far more capable than humans when it comes to many things, and we should be leaning into these strengths, rather than trying to get agents to replicate human patterns of problem solving which might be suboptimal in agentic contexts."
- **Our assessment**: Plausible framing and the premise for the other claims. Stated as principle, not tested against alternatives.

### Claim 2: Starting an agent's debugging investigation by reading the code is an anti-pattern; code reading should be the last resort
- **Evidence**: Sridharan's experience across three bugs (second-hand). Fowler endorses it.
- **Confidence**: anecdotal
- **Quote**: "having an agent start an investigation by first reading the code is an anti-pattern. In fact, reading the code first to formulate hypotheses about a bug should always be the very last resort of the agentic investigation process, not the starting point."
- **Our assessment**: Counter-intuitive, since most agent tools default to code reading. The word "always" is strong for n=3. It likely holds best for bugs observable at runtime (latency, intermittent failures) and less for deterministic logic errors with a failing test. Worth stating the condition in the guide.

### Claim 3: Gather all available evidence first, then form hypotheses from the code that best explain it
- **Evidence**: Same as Claim 2.
- **Confidence**: anecdotal
- **Quote**: "An agent should first collect all available evidence about the bug, and only then formulate the hypotheses from the code that might best explain what’s being observed."
- **Our assessment**: A concrete ordering (evidence → hypotheses → code) the guide can turn into a debugging-prompt template. Code is demoted, not banned: it is the source of hypotheses, not of facts.

### Claim 4: Debugging has two tiers — a bottom tier of raw facts and an upper tier of hypotheses — and a diagnosis is a hypothesis satisfying every fact
- **Evidence**: Conceptual model from Sridharan, as paraphrased by Fowler (the first sentence of the pair below is Fowler's paraphrase; the quote is Sridharan's).
- **Confidence**: anecdotal
- **Quote**: "Diagnosing a bug now becomes a problem of finding the hypothesis in the top tier that satisfies every fact from the bottom tier."
- **Our assessment**: Useful vocabulary, and it makes "root cause" checkable: one contradicting fact falsifies a hypothesis. It is the debugging analogue of the verification-loop idea in Ch03.

### Claim 5: Step one — identify the signals; most facts are noise, and a high-quality control is what lets the agent find them
- **Evidence**: Sridharan's process, via Fowler. A control is defined on the page as "a behavior of the system that doesn’t exhibit the bug" (Fowler's wording).
- **Confidence**: anecdotal
- **Quote**: "The factual tier has many data points. Not all of them are equally valuable. In fact, some of it might be active noise that doesn’t help an agent to be steered towards most promising hypothesis."
- **Our assessment**: The control is essentially differential debugging (good vs. bad request/build/environment), a long-standing human technique. The new point is explicitly handing the agent a control. Fowler lists three kinds: requests that trigger the bug versus those that don't, different builds, the same build in different environments.

### Claim 6: Step two — use a hypotheses × signals table; signals satisfied by few hypotheses are the most valuable
- **Evidence**: Process description by Fowler; no example table is reproduced on the page.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Fowler says "A table of hypotheses and signals helps visualize the strength of the signals and the likelihood of the hypotheses." (Fowler's own narration, not a Sridharan quote.) The idea is a discriminating-power ranking of evidence. We would need the primary article to see an actual table and whether agents generate it unaided.

### Claim 7: Step three — validate each promising hypothesis against every fact, treating each fact as a constraint
- **Evidence**: Process description, via Fowler.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Fowler writes that the third step is "validating the promising hypotheses against every fact, treating each fact as constraint on the solution" (his phrasing). It guards against the agent stopping at the first plausible story, a known failure mode.

### Claim 8: The human's most valuable contributions were picking a control, choosing a constraint, and rejecting an unvalidated hypothesis — not code knowledge
- **Evidence**: Sridharan's self-report across three bugs.
- **Confidence**: anecdotal
- **Quote**: "Across the three bugs chronicled in this post, my most valuable contributions weren’t knowledge of the code. They were picking a control, choosing a constraint, and rejecting a hypothesis that hadn’t been validated."
- **Our assessment**: Interesting claim about where human judgment sits (verification design, not code comprehension). The author is an experienced engineer, so a less experienced person might not know which control to choose. Survivorship and self-report bias apply.

### Claim 9: The engineers who thrive will be good at designing verification loops, whether or not they understand the code
- **Evidence**: Opinion/extrapolation by Sridharan.
- **Confidence**: anecdotal
- **Quote**: "The engineers who thrive in an agent-native world will be the ones who are good at designing such verification loops, whether or not they understand the code it verifies."
- **Our assessment**: Forecast, not finding. "Whether or not they understand the code" is contestable; Ch03 and the corpus's code-review notes argue comprehension still matters. Treat as a position.

### Claim 10: Humans need less data, so human tools aggregate; agents need more raw data, and aggregation often destroys the signal for them
- **Evidence**: Reasoned argument from agent strengths (processing volume at speed). No measurements.
- **Confidence**: anecdotal
- **Quote**: "Aggregation — the thing that makes a dashboard useful to a human — is often the thing that destroys the value of the signal for an agent"
- **Our assessment**: Strong, actionable claim for harness design: expose raw logs/traces/queries to agents rather than only dashboards. Practical limits (context window size, cost, privacy) are not discussed on Fowler's page, and the guide should note that tension with token-budget advice.

### Claim 11: More logging gives agents more data to chew on, so agent use should change how systems are built
- **Evidence**: Fowler's inference from Claim 10.
- **Confidence**: anecdotal
- **Quote**: "More logging gives agents more data to chew on."
- **Our assessment**: Short and unqualified. Connects to the observability notes in the corpus but adds a new rationale (logging for the agent as reader). Cost/volume tradeoffs are unexamined.

### Claim 12: The agent could reach the root cause alone in all three bugs but did not — e.g. it didn't set up a control in the "latency bug" until asked
- **Evidence**: Sridharan's report from three bug hunts.
- **Confidence**: anecdotal
- **Quote**: "It didn’t set up a control in the “latency bug” until I asked it to"
- **Our assessment**: Evidence that the control step must be prompted explicitly (or encoded in a skill/AGENTS.md). Also supports encoding this method as a reusable agent instruction. The page gives no detail on the model or tool used.

## Concrete Artifacts

No code, configs, or transcripts appear on Fowler's page. The only procedure is the following, reconstructed from the page (attributed to Sridharan via Fowler; my formatting):

```
Agent debugging method (Sridharan, as summarized by Fowler, 2026-10-21)
0. Principle: collect evidence first; read code last (only to form hypotheses).
1. Identify signals in the factual tier, using a control
   (control = system behavior without the bug: non-triggering requests,
    a different build, or the same build in a different environment).
2. Rank hypotheses against signals in a hypotheses x signals table;
   signals that few hypotheses satisfy are the most valuable.
3. Validate promising hypotheses against EVERY fact (each fact is a constraint).
Human role: pick the control, choose the constraints, reject unvalidated hypotheses.
```

## Cross-References

- **Corroborates**: None directly. Related: `source-notes/blog-simonwillison-linus-torvalds-ai-debug-session.md` is another agent-debugging anecdote (Claims 4 and 6 there: the agent kept producing useful debug code, and the fix took 24 patches and 18 boots of instrumentation) and is consistent with evidence-gathering (instrumentation) being the bulk of debugging work; it does not state the control/hypothesis method.
- **Contradicts**: None found. No contradiction issue filed. The claim that human code knowledge matters little (Claims 8–9) is in tension with general comprehension-preserving advice elsewhere in the corpus (not checked claim-by-claim), but Sridharan's claim is about the debugging contribution, so it is a context difference, not a contradiction.
- **Extends**: `source-notes/blog-ghaw-agent-observability.md` and `source-notes/blog-anthropic-agent-observability-claude-platform.md` treat observability as monitoring of agents; this source adds observability data as input to agents when they debug other systems. Same curator: `source-notes/blog-fowler-fragments-2026-10-04.md` (different content).
- **Novel**: The evidence-before-code ordering; facts/hypotheses two-tier model; controls for agent debugging; hypotheses × signals table; "aggregation destroys signal for agents."

## Guide Impact

- **Chapter 03 (verification)**: Add a "debugging loop" subsection: gather raw evidence → pick a control → hypotheses × signals table → validate against every fact; flag as a single-practitioner, anecdotal method (cite this note).
- **Chapter 04 (context engineering)**: Add the raw-vs-aggregated point: give agents raw logs/traces rather than dashboard summaries, with the caveat that context budget and cost limit how much raw data fits.
- **Chapter 02 (harness)**: Note that logging/trace access is a harness capability for debugging agents, and that the control step may need to be encoded in a skill or prompt since the agent did not do it unprompted.
- **Chapter 01 (daily workflows)**: Suggest a debugging prompt that tells the agent not to open source files until it has listed the available runtime evidence.
- **Follow-up**: File a new issue for the Sridharan primary article once an accessible copy (e.g. archive or alternate host) is found; it would replace this secondhand summary as the cited source.

## Extraction Notes

- Read Fowler's page in full (fetched with curl, HTML stripped). The relevant section is roughly a dozen paragraphs.
- Attempted the primary Medium article; HTTP 403 from both curl and WebFetch. No archive copies were attempted. Quotes are therefore Fowler's reproductions of Sridharan; Claims 6 and 7 use no quote because the wording on the page is Fowler's own narration.
- Prospector triage comments asked for the primary article; this could not be done, so the confidence is `anecdotal` (three self-reported bug hunts, relayed second-hand, no metrics).
- Triage asked about the "Fragments: October 21" section on AI-voice detection; skipped as not engineering-relevant.
