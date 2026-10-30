---
source_url: https://martinfowler.com/rachels-ramblings/good-devs-wary.html
source_type: blog-post
title: "Why are good developers so wary of agentic development?"
author: Rachel Laycock (CTO, Thoughtworks)
date_published: 2026-10-29
date_extracted: 2026-10-30
last_checked: 2026-10-30
status: current
confidence_overall: anecdotal
issue: "#4433"
---

# Why are good developers so wary of agentic development?

> A CTO essay arguing that experienced developers' hesitancy to hand agents all execution is a trust-in-production concern, supported by a secondhand report of a Thoughtworks all-agent week in which the app ran but the build was frequently red.

## Source Context

- **Type**: blog-post (essay, "Rachel's Ramblings" on martinfowler.com)
- **Author credibility**: Rachel Laycock is CTO at Thoughtworks and describes 25+ years in technology. She reports secondhand from conversations with the experiment team (led by Giles Alexander) and from a September Technology Radar open space. Martin Fowler commented on a draft.
- **Scope**: Explains developer hesitancy, summarises one internal experiment (time split, red build), raises open questions on CI, TDD and batch size, and closes with a ski/backcountry analogy plus a call to leaders and developers. No metrics beyond the self-estimated time split; no prescriptions are settled.

## Extracted Claims

### Claim 1: Experienced developers' hesitancy is about trusting agent-built systems in production, not fear of job loss or of losing the joy of coding
- **Evidence**: Author's observation from conversations and the September Radar open space; no survey data.
- **Confidence**: anecdotal
- **Quote**: "Good developers’ caution about agentic development comes from knowing that built isn’t the same as working in production."
- **Our assessment**: Useful reframing for the adoption chapter. It is a practitioner interpretation, not measured. The author concedes job/code-love fears are "true for some people, some of the time".

### Claim 2: The hesitancy is specifically about letting agents do all the execution without proven guardrails, not about using coding assistants
- **Evidence**: Author's characterisation of the hesitant group.
- **Confidence**: anecdotal
- **Quote**: "they are not hesitant to use a coding assistant, they are hesitant to go all in and let the agents do all the execution."
- **Our assessment**: Draws a line between assisted and fully delegated modes; the objection is to missing guardrails ("take their hand off the wheel"), which maps to harness maturity rather than tool rejection.

### Claim 3: Underlying question: how much can we trust a system when nobody has experience building it this way?
- **Evidence**: Argument; all current production systems were built "the old way".
- **Confidence**: emerging
- **Quote**: "Nearly every system we have in production now was built the old way, by hand, by people we could trust (hopefully)."
- **Our assessment**: Echoes Beck's code-vs-trust asymmetry (see Cross-References). The "no one has lived with this yet" point is a fair epistemic limit on all current agent-built-system claims.

### Claim 4: With agents writing all code, human effort shifts to the whiteboard (domain, boundaries, plans) and to the harness (tests, contracts, architecture checks, pipeline)
- **Evidence**: Self-estimated by the experiment team, relayed by the author; one team, one week.
- **Confidence**: anecdotal
- **Quote**: "When I asked them to estimate they said they spend about ⅔ of their time at the whiteboard and ⅓ on the harness"
- **Our assessment**: Interesting but thin: an estimate, no measurement. The author herself cautions "before you get ahead of yourself redesigning your team". Also notes most keyboard work was "directing agents to put this learning into the harness" so the next run is better, i.e. human lessons are encoded into the harness rather than into code.

### Claim 5: In the experiment the application ran but the build was frequently red
- **Evidence**: Reported by the author from the experiment conversations; no counts or logs.
- **Confidence**: anecdotal
- **Quote**: "The application ran, but the build was frequently red."
- **Our assessment**: A concrete failure mode of fully-agentic work: functional output without a trustworthy integration signal. Same experiment is narrated in the Edwards-Alexander note, which also records CI overload from many agents in one repo.

### Claim 6: A chronically red build destroys the signal value of both red and green
- **Evidence**: Reasoning from CI principles.
- **Confidence**: settled (as CI doctrine); anecdotal as applied to this experiment
- **Quote**: "If it’s red so often that people stop paying attention, how do we spot the next real failure? And if we can’t trust the checks, a green build stops being reassuring too."
- **Our assessment**: Agree. Strong guide-ready framing for why harness checks must be kept reliable (non-flaky, fast) as agent change volume grows.

### Claim 7: Candidate causes of the red build are unresolved: parallel agents colliding, insufficient modularity, or changes arriving faster than checks finish
- **Evidence**: Three hypotheses posed as questions; the author says "We’re still working through how to address it."
- **Confidence**: anecdotal
- **Quote**: "Were too many agents working in parallel and stepping on each other’s changes? Was the system not yet modular enough for agents to work on separate parts? Or were changes simply arriving faster than the checks could finish?"
- **Our assessment**: Hypotheses, not findings. Must not be cited as established causes. Useful as a checklist of what to instrument.

### Claim 8: DORA 2025 links AI adoption to higher delivery throughput but lower delivery stability
- **Evidence**: Cited secondhand from DORA 2025; not independently checked by the author in this post. We did not verify against the DORA report.
- **Confidence**: emerging
- **Quote**: "DORA’s 2025 research found AI adoption is now linked to higher delivery throughput, but to lower delivery stability."
- **Our assessment**: If the Smith uses it, cite DORA directly, not this post.

### Claim 9: Continuous delivery/DevOps may see a resurgence and rethink in the agentic era ("last mile" problems)
- **Evidence**: Author's forecast.
- **Confidence**: anecdotal
- **Quote**: "I can see continuous delivery/DevOps as a movement having a resurgence and a rethink in the agentic era"
- **Our assessment**: Opinion; consistent with the quality-is-speed note's view that rigor relocates to CI and testing.

### Claim 10: Open questions: TDD when the agent writes tests alongside code, where acceptance/contract/boundary checks add confidence, how much design up front, and batch size (Stories vs Epics against CI throughput)
- **Evidence**: Internal arguments summarised by the author; explicitly unresolved.
- **Confidence**: anecdotal
- **Quote**: "What role should test-driven development play when you aren’t reading every line and the agent created the tests alongside the code?"
- **Our assessment**: Good list of open questions for the verification chapter. The batch-size claim ("I have heard many teams are moving from Stories to Epics") is hearsay; the question is whether CI can "handle that size unit of work at speed and in parallel".

### Claim 11: Agentic development is like backcountry travel, not a groomed slope; a heavily agent-built system can only be judged after production time and rounds of change
- **Evidence**: Analogy; the backcountry framing is attributed to Martin Fowler's reply to the draft.
- **Confidence**: anecdotal
- **Quote**: "we won’t know whether a heavily agent-built system works until it has run in production for a while, survived a few rounds of change, and not sent all our planes to Aberystwyth."
- **Our assessment**: Sound epistemic caution: feedback on agent-built systems is slow, so early success reports (including this experiment's 80%) should be discounted.

### Claim 12: Leaders should create room for experimentation and not judge success by agent code output; developers should test their own assumptions too
- **Evidence**: Author's recommendation.
- **Confidence**: anecdotal
- **Quote**: "That means time, permission to get things wrong, and not judging success by how much code the agents produced."
- **Our assessment**: Relevant to adoption guidance and metrics (counter to lines-of-code style measures). The author also warns "experience can also make us too attached to familiar practices", a balanced counterpoint.

## Concrete Artifacts

No code or configs. Experiment details as reported by the author (secondhand, from Giles Alexander's team):

```
- No code written by any human; everything built by agents (airline application)
- Reached roughly 80% ("they got 80% done"); experiment run twice with different teams
- Self-estimated time: ~2/3 whiteboard, ~1/3 harness
- Human-designed feedback: tests, contracts, architecture checks, delivery pipeline
- Outcome: app ran, build frequently red
- The product person committed more feature code than anyone else on the team
```
(Attribution: paraphrased summary of the "A week at the whiteboard" and "The application ran. The build was red." sections.)

## Cross-References

- **Corroborates**: `blog-kentbeck-trust-factory.md` (Claims 2 and 7: code accumulating faster than trust); `blog-thoughtworks-murray-fowler-quality-is-speed.md` (Claim 1: discipline moves rather than disappears); `blog-thoughtworks-nandyala-pani-engineering-the-harness.md` (human work centres on the harness).
- **Contradicts**: None found. No contradiction issue filed.
- **Extends**: `blog-fowler-edwards-alexander-accidental-blackboard.md` — same experiment seen from the CTO-for-Europe side; its Claim 2 records CI/build pipeline overload from many agents in one repo, which this post frames as an unresolved red-build trust problem. Also `blog-fowler-malykhin-archaeologist-copilot.md` (distrust of an unverified green/“looks fine” result) and `blog-thoughtworks-mugrage-comprehensibility-liability.md` (unreviewed agent code).
- **Novel**: The explicit framing of developer hesitancy as trust-in-production rather than job fear; the red-build-erodes-green-signal argument applied to agent-volume CI; the Stories-to-Epics batch-size question against CI throughput; the self-estimated 2/3 whiteboard vs 1/3 harness split.

## Guide Impact

- **Chapter 03 (Verification)**: Add the "chronically red build makes green meaningless" point (Claim 6) with the three unresolved causes (Claim 7) as an open problem, flagged as hypotheses. Cite DORA directly rather than this post for the throughput/stability finding.
- **Chapter 02 (Harness)**: Optionally cite the observation that human keyboard time went into encoding lessons into the harness so subsequent runs improve (Claim 4), noting it is a single-team anecdote.
- **Chapter 05 (Team adoption)**: Where hesitancy is discussed, add the trust-in-production framing (Claims 1, 2, 12) as practitioner opinion, labelled anecdotal.

## Extraction Notes

- Read the full article (fetched directly, all sections). Followed no sub-pages: the linked experiment write-up is already covered by the Edwards-Alexander note; DORA 2025 was not checked.
- Triage priority was low/medium; the essay is thin on evidence, so confidence is anecdotal throughout. Quotes were copied from the page text (curly apostrophes preserved).
- Related post linked as previous: "Maybe We Shouldn't Be Reviewing All This Code" (no source note found at time of extraction).
