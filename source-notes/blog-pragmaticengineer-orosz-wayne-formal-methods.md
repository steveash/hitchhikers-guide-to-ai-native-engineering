---
source_url: https://newsletter.pragmaticengineer.com/p/formal-methods-with-hillel-wayne
source_type: blog-post
title: "Formal methods with Hillel Wayne"
author: Gergely Orosz, featuring Hillel Wayne (The Pragmatic Engineer podcast)
date_published: 2026-07-29
date_extracted: 2026-07-30
last_checked: 2026-07-30
status: current
confidence_overall: anecdotal
issue: "#2325"
---

# Formal methods with Hillel Wayne (The Pragmatic Engineer)

> A podcast-episode companion post in which Gergely Orosz interviews formal-methods
> consultant Hillel Wayne about TLA+, Alloy, and property-based testing, closing with
> Wayne's considered prediction that AI will meaningfully but not dramatically expand
> formal-methods adoption ("from maybe 0.1% to 0.3% across the industry") because the
> practitioners who succeed at using AI to generate formal specs are already formal-methods
> experts — a claim that stands in direct tension with a third-party blog post the episode
> itself links as "mentioned during the episode."

## Source Context

- **Type**: blog-post / podcast episode companion page. The Pragmatic Engineer newsletter
  (`newsletter.pragmaticengineer.com`, Gergely Orosz) publishes a written page for each
  podcast episode consisting of a short intro, a numbered "Takeaways from the conversation"
  list (10 items), a timestamped chapter index of the ~82-minute audio/video episode, and a
  "References" list of every tool/paper/post mentioned during the conversation. The full
  spoken transcript is referenced ("See the episode transcript at the top of this page") but
  is not present in the page's fetchable text content — it appears to load only in an
  audio/video player embed, not as static page text. This note is built from the Takeaways
  list, the References list, and two linked pages followed per extraction guidance (see
  Extraction Notes).
- **Author credibility**: Hillel Wayne is a formal-methods consultant, educator, and author
  of *Logic for Programmers*, described in the episode intro as "one of the best people to
  tackle the prediction" of whether AI will make formal verification mainstream. He also
  authored *The Crossover Project*, a ~20-interview study comparing software engineering to
  traditional engineering disciplines. Gergely Orosz writes The Pragmatic Engineer, a
  widely-read software-engineering newsletter/podcast already present in this corpus via
  `blog-pragmaticengineer-orosz-kentbeck-career.md`, `blog-pragmaticengineer-orosz-loop-engineering.md`,
  and others.
- **Scope**: Covers TLA+ mechanics and Amazon's use of it, why most formal specs are hard to
  write, property-based testing as the practical middle ground, a roster of alternative
  formal-methods tools, and Wayne's views on AI's effect on formal-methods adoption and on
  software engineering's future prestige/pay. Does NOT cover: a line-by-line transcript of
  the conversation, quantitative adoption data beyond Wayne's own order-of-magnitude
  estimate, or any AI-native harness/tooling guidance — this is a formal-methods expert's
  opinion piece, not an empirical study.

## Extracted Claims

### Claim 1: Software engineers "earn the right" to the engineer title through the rigor the discipline requires, based on a ~20-interview comparative study against traditional engineering fields
- **Evidence**: Hillel Wayne's own research project (*The Crossover Project*), ~20 interviews across traditional-engineering and software-engineering fields, cited in the episode's first takeaway.
- **Confidence**: anecdotal
- **Quote**: "For [The Crossover Project], Hillel interviewed ~20 people in different fields of traditional engineering and software engineering, and found plenty of similarities and differences. He concluded that the rigor needed in software engineering means we earn the right to the title of "engineer.""
- **Our assessment**: Interesting framing but not directly actionable for the guide — it's a disciplinary-identity claim, not a workflow recommendation. Included for completeness since it's the episode's lead takeaway.

### Claim 2: Software engineering's version control is more sophisticated than traditional engineering's change-management equivalents, and traditional engineers wish they had it
- **Evidence**: Comparative observation from the same Crossover Project interviews.
- **Confidence**: anecdotal
- **Quote**: "Other fields of engineering have change management, but "traditional" engineers wish the concept of version control in software engineering existed in their fields because it's far more sophisticated."
- **Our assessment**: Plausible but unverifiable from this source alone (no traditional-engineer quote given, only Wayne's summary of ~20 interviews). Low direct guide relevance.

### Claim 3: TLA+ works by modeling a system as a state machine and exhaustively checking every reachable state against properties defined upfront
- **Evidence**: Description given during the episode's TLA+ walkthrough/demo segment.
- **Confidence**: settled (this is a factual description of how TLA+'s model checker works, not a contested claim)
- **Quote**: "The language represents the state machine of the system and every possible state it can transition to. From the initial state, the system enumerates to get to every reachable state and checks whether properties defined upfront apply to those states."
- **Our assessment**: Accurate, standard description of TLA+'s exhaustive model-checking approach (as opposed to testing, which samples). Useful baseline definition if the guide ever introduces TLA+ by name.

### Claim 4: Amazon used TLA+ to find a bug with a 35-step minimum error trace — a bug class formal methods are specifically suited to catch because it is nearly undiscoverable through conventional testing
- **Evidence**: Citing the AWS team's own published paper, "How AWS uses formal methods" (CACM).
- **Confidence**: settled (published, attributed AWS engineering account)
- **Quote**: "In the paper [How AWS uses formal methods], the AWS team shared that they'd found a complicated bug for which "the shortest error trace to exhibit was 35 steps (!!)" without conventional testing approaches."
- **Our assessment**: This is the strongest concrete evidence in the note for formal methods' value proposition — a bug requiring 35 sequential steps to trigger is exactly the class of bug conventional unit/integration testing is structurally unlikely to generate at random. Directly relevant to Ch03's existing "coverage gap" argument (guide/03-verification.md: "You cannot write tests for unspecified behaviors").

### Claim 5: Race conditions modeled in TLA+ surface immediately when the tool runs, versus months later (or never) in production without formal modeling
- **Evidence**: Wayne's characterization of the feedback-loop-speed difference, from the episode's concurrency segment.
- **Confidence**: anecdotal
- **Quote**: "When a system has a race condition due to your code, you usually don't find out until a few months later – if ever! In contrast, a system modeled in TLA+ can tell you about race conditions as soon as the tool is run, making it a fast feedback loop."
- **Our assessment**: A reasonable characterization of formal verification's feedback-loop advantage for concurrency bugs specifically. Not quantified (no time-to-detection numbers), so treat as directional rather than measured.

### Claim 6: Formal methods aren't used for everything because real-world specs are a "nightmare to write" — even simple-sounding problems explode into edge-case questions (encoding, unreadable files, symlinks) that ordinary code can leave implicit
- **Evidence**: Wayne's example of "find the file in a directory that has the most lines" as a formally-hard problem.
- **Confidence**: anecdotal
- **Quote**: "It's because specs in the real world are a nightmare to write. Even a simple problem like "find the file in a directory that has the most lines" gets complicated when modeled with formal methods."
- **Our assessment**: This is the core adoption-barrier claim and matches the general software-engineering intuition that formalization cost scales with edge-case surface area, not implementation complexity. Directly explains why formal methods stay niche regardless of AI involvement (see Claim 8).

### Claim 7: Wayne recommends property-based testing as the practical formal-methods-adjacent technique for most engineers, reserving true formal methods (TLA+, Alloy, etc.) as a niche tool
- **Evidence**: Direct recommendation stated as a episode takeaway.
- **Confidence**: emerging (a named expert's considered recommendation, not yet a measured industry outcome)
- **Quote**: "Hillel is convinced that formal methods are a niche tool for most engineers, whereas property-based testing is the most practical approach for building robust software with this lightweight formal method."
- **Our assessment**: This is the single most actionable claim in the note for the guide's verification chapter. Property-based testing (defining invariants, then fuzzing thousands of generated inputs against them) sits between example-based unit tests and full formal specification, and is not currently named anywhere in `guide/03-verification.md`'s Verification Stack. Ch03 covers deterministic tools, hooks, CI, two-agent review, and human review — property-based testing is a distinct technique that could sit in "Layer 1: Deterministic Tools" or as its own layer.

### Claim 8: Wayne predicts AI will meaningfully but not dramatically expand formal-methods adoption — roughly from 0.1% to 0.3% of the industry — and that the engineers who succeed at using AI to generate formal specs are disproportionately already formal-methods experts
- **Evidence**: Wayne's own stated prediction, closing the episode's AI segment.
- **Confidence**: anecdotal (a single expert's order-of-magnitude guess, explicitly presented as a prediction, not a measurement)
- **Quote**: "AI bringing formal verification up from maybe 0.1% to 0.3% across the industry would still be huge!" ... "He also finds that people who succeed at using AI to generate formal specs are often formal verification experts."
- **Our assessment**: This is the episode's direct answer to the Prospector's key question, and it is a skeptical one: AI does not democratize formal methods to non-experts in Wayne's account — it makes existing experts somewhat more productive. This is corroborated by his own separate blog post (Claim 9) but stands in tension with a third-party account the episode itself links to (Claim 10). See Cross-References.

### Claim 9: LLMs generate formally "weak" (easily-true) properties rather than the strong properties that make formal specs valuable, and getting an LLM to do useful formal methods still requires the user to already know formal methods
- **Evidence**: Hillel Wayne's own blog post, "LLMs are bad at vibing specifications" (buttondown.com/hillelwayne, dated 2026-03-10), linked from the episode's References list under "Mentions during the episode." Verified verbatim by two independent fetches of the source page returning identical wording.
- **Confidence**: anecdotal
- **Quote**: "If you need to know formal methods to get the LLM to do formal methods, is that really helping?"
- **Our assessment**: This is Wayne's fuller reasoning behind the 0.1%-to-0.3% estimate in Claim 8 — not a contradiction of it, but its supporting argument. The surrounding sentence in the blog post ("Which is good for my current livelihood, but bad for the hope of LLMs making formal methods mainstream") makes his self-interest in this assessment explicit, which is worth noting as a mild conflict-of-interest caveat even though it doesn't undermine the technical argument (weak vs. strong properties) he's making.

### Claim 10: A third-party account claims AI can now autonomously generate production-quality TLA+ specifications from large real-world codebases, discovering a genuine race condition in Azure Storage, with output that "rivals" a decade of expert hand-crafted specs
- **Evidence**: Cheng Huang's blog post "The Coming AI Revolution in Distributed Systems" (zfhuang99.github.io, dated 2025-05-24), linked from the same episode's References list under "Mentions during the episode." Verified verbatim by two independent fetches of the source page.
- **Confidence**: anecdotal
- **Quote**: "After a decade of manually crafting TLA+ specifications, I must acknowledge that this AI-generated specification rivals human work." ... "Within hours of iterative refinement, the AI had surfaced a critical race condition: an old Paxos primary could perform a deletion while a new primary simultaneously added a reference."
- **Our assessment**: This directly opposes the substance of Claims 8 and 9. Huang self-identifies as having a decade of TLA+ experience — so even this optimistic account is arguably still consistent with Wayne's "the people who succeed are already experts" observation (Huang is exactly such an expert, not a formal-methods novice). We don't read this as a clean contradiction of Wayne's claim so much as a data point that could go either way depending on how "democratize" is defined: Huang's own expertise did the heavy lifting of prompting, evaluating, and iterating on the AI's output. We are not resolving this tension in the note — see Cross-References.

## Concrete Artifacts

### Formal-methods tool roster referenced in the episode (from the page's References section, verbatim link list)

```
NuSMV: https://nusmv.fbk.eu/
TLA+: https://github.com/tlaplus
Alloy: https://alloytools.org
P (Formal Modeling and Analysis of Distributed Systems): https://github.com/p-org/P
Quint: https://quint.sh
PRISM: https://www.prismmodelchecker.org
Event-B: https://eventb-soton.github.io/en-us
MCRL2: https://mcrl2.org/web/index.html
KeYmaera X: https://keymaerax.org
Dafny: https://dafny.org
JML: https://www.openjml.org
Frama-C: https://frama-c.com
Ada SPARK: https://www.adacore.com/languages/spark
```

*Source: newsletter.pragmaticengineer.com/p/formal-methods-with-hillel-wayne, "References" section*

### Episode chapter index (from the page's Timestamps section, illustrates topic ordering/weight)

```
00:00 Intro
04:32 The Crossover Project
11:37 What software engineering does better
15:30 What traditional engineering does better
18:17 Formal methods
29:32 TLA+: what it is and demo
36:58 TLA+ at Amazon
38:10 Ways distributed systems break
41:03 Formal methods and systems thinking
46:20 The value of learning math
50:23 What TLA+ is good for and isn't
52:50 Alloy: a declarative language for software modeling
58:53 Other formal methods tools
1:01:24 Property-based testing
1:05:31 AI and the need for formal verification
1:12:29 Logic for programmers
1:14:35 Hillel's 2025 prediction on AI's impact
1:21:30 Book recommendation
```

*Source: newsletter.pragmaticengineer.com/p/formal-methods-with-hillel-wayne, "Timestamps" section*

## Cross-References

- **Corroborates**: `discussion-hn-agentic-coding-jobs.md` Claim 6 and Claim 7 describe a practitioner (hackermailman) using Alloy for pre-generation modeling of security role models, network protocols, game rules, and CSS layout states — Wayne's episode independently confirms Alloy is "a declarative language for software modeling" (episode timestamp 52:50) used for exactly this class of problem, giving that HN anecdote corroboration from a recognized formal-methods expert rather than leaving it as an isolated practitioner report.
- **Contradicts**: Claims 8/9 (Wayne, expert-skeptical: AI mostly amplifies existing formal-methods experts rather than creating new ones) vs. Claim 10 (Huang, optimistic: AI can autonomously produce expert-rivaling specs from production code). Both sides are extracted in this same note (Claim 10 is a link the episode itself surfaces as related "mentions"), and per MINER.md §4a this is not filed as a separate contradiction issue: it does not oppose any existing claim already in a source note in this corpus (formal methods are novel to the corpus — see Novel below), and Huang's account is arguably reconcilable with Wayne's framing rather than a clean opposite (Huang is himself a decade-long TLA+ expert, which is consistent with Wayne's "expert-dependency" argument even though Huang frames his result as "AI-autonomous"). Flagging here for the Smith/Assayer to weigh rather than picking a verdict.
- **Extends**: `discussion-hn-agentic-coding-jobs.md` Claim 5 ("Pre-generation formal design... enables reliable 'never look at the code' agent generation") — Wayne's episode gives the missing expert-level caveat that HN anecdote lacks: formal methods are effective but "a nightmare to write" (Claim 6) and remain a niche skill (Claim 7), so the HN practitioner's workflow is likely representative of a small, already-skilled minority rather than a technique any engineer can pick up cheaply.
- **Novel**: Formal methods (TLA+, Alloy, property-based testing, model checking generally) are not covered by any existing source note or by `guide/03-verification.md` as of this extraction. This is the first source in the corpus to address whether AI changes the cost/adoption calculus for formal verification specifically (as opposed to test-suite-based verification, which the guide already covers extensively).

## Guide Impact

- **Chapter 03 (Verification)**: The current "Verification Stack" (guide/03-verification.md) enumerates five layers — deterministic tools, hooks, CI, two-agent review, human review — none of which is property-based testing or formal specification. Claim 7 (Wayne's practical recommendation) supports adding property-based testing as a named technique, likely within "Layer 1: Deterministic Tools" or as a distinct layer between deterministic tools and CI, since it is runnable automatically but tests a different property than example-based unit tests (invariants over generated inputs vs. fixed expected outputs). Separately, Claim 4 (Amazon's 35-step TLA+ bug) is strong supporting evidence for the chapter's existing "coverage gap" argument ("Tests cannot fully answer correctness... it cannot catch 'this code does something we never thought to test'") — formal methods are presented by an expert source as the answer to exactly that named gap, for the minority of systems where the cost is justified.
- **Chapter 03 (Verification) — do NOT overclaim AI democratizes formal methods**: If a future edit to Ch03 or elsewhere in the guide is tempted to recommend "have the agent write your TLA+ spec" as a way to make formal verification broadly accessible, Claims 8 and 9 are the citation to add a caveat: the source's own formal-methods expert predicts only a 3x adoption increase off a ~0.1% base (still leaving formal methods niche) and states that the people who succeed at AI-assisted spec-writing are largely already experts. Claim 10 is the counter-anecdote to weigh alongside it, not to omit.
- **Chapter 02 (Harness Engineering)**: If Ch02 develops a pre-generation/spec-driven design section, cite this note alongside `discussion-hn-agentic-coding-jobs.md` (Claims 5-7) — Wayne's episode is the first expert-level corroboration in the corpus that lightweight formal methods (Alloy specifically) are a legitimate pre-generation design technique, not just one practitioner's idiosyncratic workflow.

## Extraction Notes

- The episode's full spoken transcript ("See the episode transcript at the top of this page") was not present in the page's fetchable text content across multiple fetch attempts — it appears to load only inside an audio/video player embed rather than as static/server-rendered page text. This note is therefore built from the newsletter page's own written artifacts: the 10-item "Takeaways" list, the "Timestamps" chapter index, and the "References" link list, all of which were verified as stable/verbatim across 2-3 independent re-fetches of the same page (repeated fetches returned identical wording, which is the basis for treating them as genuine page text rather than model-generated paraphrase).
- Per MINER.md §1 ("follow up to 5 linked pages that seem substantive"), two links from the episode's References section were followed and read: Hillel Wayne's own blog post "LLMs are bad at vibing specifications" (Claim 9) and Cheng Huang's "The Coming AI Revolution in Distributed Systems" (Claim 10). Both were the most directly relevant to the Prospector's key question about AI and formal-methods adoption. Three other referenced links (the AWS CACM paper, other Hillel Wayne dreidel-modeling posts, and the Grady Booch episode) were not followed in full — the AWS paper's one load-bearing fact (the 35-step error trace) was already quoted verbatim within the primary source itself (Claim 4), and the dreidel posts and Booch episode looked tangential to the Prospector's key question rather than substantive to it.
- No paywall was encountered; the newsletter page itself is fully public. The inaccessibility is specific to the transcript content, not the article.
