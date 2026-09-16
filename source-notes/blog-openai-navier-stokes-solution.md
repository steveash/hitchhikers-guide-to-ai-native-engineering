---
source_url: https://openai.com/index/navier-stokes-solution
source_type: blog-post
title: "On the Navier–Stokes Millennium Prize Problem"
author: OpenAI
date_published: 2026-09-08
date_extracted: 2026-09-16
last_checked: 2026-09-16
status: current
confidence_overall: emerging
issue: "#3479"
---

# On the Navier–Stokes Millennium Prize Problem

> OpenAI's first-party announcement that an internal (unreleased,
> more-capable-than-GPT‑6-Astra) model, run as a ~10,000-concurrent-agent
> system over 88 hours plus 17 hours of Lean formal verification, produced
> a proof that 3D incompressible Navier–Stokes can develop a finite-time
> singularity — resolving one of the seven Millennium Prize Problems. The
> post is as much an engineering-process disclosure (parallel
> hypothesis-testing across agent groups, mid-run model swaps, Codex-driven
> cross-pollination of intermediate results, and a post-hoc data-governance
> investigation into a rival lab's product usage) as a mathematics
> announcement.

## Source Context

- **Type**: blog-post (`openai.com/index/`, unsigned corporate "Research /
  Publication" voice, published September 8, 2026, with a disclosed
  September 10, 2026 update to the "Concurrent work" section).
- **Author credibility**: First-party institutional post from OpenAI,
  the same evidentiary register as every other `openai.com/index/` post
  already in this corpus (e.g. `blog-openai-astra-safety-overview.md`,
  `blog-openai-astra-critical-cyber-capabilities.md`). It is the primary
  source for a claimed mathematical result and for OpenAI's own account of
  the engineering process used to produce it — self-reported, with no
  named external verification of the process claims (message counts,
  token counts, agent counts, timeline) beyond the openly published paper
  and Lean formalization link, which mathematically-inclined third parties
  can independently check but which this Miner pass did not attempt to
  verify.
- **Scope**: Covers the mathematical result itself (at a summary level,
  not the proof mechanics), the multi-agent process used to find it
  (agent counts, coordination structure, tooling, timeline, token/message
  volume), safety/isolation practices applied during the effort, and a
  detailed account of concurrent/overlapping work by an Anthropic
  researcher and an NYU professor, including a data-governance
  investigation into whether a rival lab's customer product usage could
  have leaked into OpenAI's training data. Does **not** cover: the
  mathematical proof details themselves (deferred to the linked paper),
  any external replication of the timeline/scale figures, or the specific
  architecture/training recipe of the internal model used.

## Extracted Claims

### Claim 1: OpenAI's internal (unreleased, more-capable-than-GPT‑6-Astra) system produced both a written proof and a Lean formalization showing that 3D incompressible Navier–Stokes flow, starting from rest with finite energy and a smooth applied force, can develop a finite-time singularity — resolving statements "C" (and "D") of the official Millennium Prize formulation
- **Evidence**: Direct first-party result claim, backed by a published paper ("Read the paper") and a linked Lean-formalized proof, both referenced in the post but not independently re-verified by this Miner pass.
- **Confidence**: emerging (specific, falsifiable, and accompanied by a machine-checkable Lean formalization link — but a same-week, single-source announcement with no disclosed third-party replication yet)
- **Quote**: "Our system produced an analytical proof and a Lean formalization that an initially smooth fluid at rest can develop a singularity in a finite time. The fluid has a smooth force applied to it, and its energy remains finite through the entire dynamics, from rest to the formation of the singularity. This resolves the Navier–Stokes Millennium Prize problem by establishing statement "C" (and also "D") in the official Millennium Prize formulation."
- **Our assessment**: The math itself is out of the guide's scope, but the pairing of a natural-language proof with an independently-checkable Lean formalization is directly relevant as a verification pattern — see Claim 6 and Guide Impact (Ch03) below.

### Claim 2: OpenAI states the result was produced using an internal model "significantly more capable than GPT‑6 Astra," whose training began August 28, 2026 and was still ongoing (and improving) during the effort
- **Evidence**: Direct first-party statement in the opening section.
- **Confidence**: emerging (specific date and comparative capability claim, self-reported, no external benchmark disclosed)
- **Quote**: "To solve the Navier–Stokes problem, we used an internal model that is significantly more capable than GPT‑6 Astra. We believe it is important to inform the world about the pace of AI progress and what to expect from upcoming models." / "Since August 28 we have been training a new internal model that has exhibited unprecedented performance in our benchmarks, including mathematics. This model's training is ongoing and its performance continues to improve."
- **Our assessment**: This is an explicit "capability preview via a research stunt" disclosure pattern — OpenAI is using a hard, externally-legible benchmark (a Millennium Prize problem) to signal an unreleased model's capability level rather than publishing benchmark numbers directly. Notable for Ch01/Ch02 framing of how frontier labs communicate progress.

### Claim 3: The effort used a system of coordinating agents, subdivided into communicating groups, with the Navier–Stokes-solving group running on the order of 10,000 concurrent agents; agents had tool access to a cached internet snapshot and code execution, and OpenAI states it applied the same safeguards used for all frontier model evaluations, including monitoring and isolation
- **Evidence**: Direct first-party process description.
- **Confidence**: emerging (specific concurrency figure and tooling description, self-reported, not independently auditable)
- **Quote**: "We used a system of coordinating agents powered by our internal model. The agents had access to tools such as the ability to read from a cached version of the internet and the ability to run code. Agents were subdivided into groups with the ability to communicate within the group. The groups varied in size, and the group that produced the Navier–Stokes resolution involved on the order of 10,000 concurrent agents. At all times we maintained the same strict safeguards that we apply to all our frontier model evaluations, including monitoring and isolation."
- **Our assessment**: 10,000 concurrent communicating agents on a single problem is an order of magnitude beyond the multi-agent scales documented elsewhere in this corpus (see Cross-References). It corroborates, at much larger scale, `blog-openai-astra-safety-overview.md`'s disclosed practice of "stricter isolation" and "universal monitoring" for frontier-capability internal model use — this post confirms those safeguards were carried over to a large-scale internal research/evaluation deployment, not just to externally-shipped models.

### Claim 4: OpenAI hedged the problem's ambiguity by assigning different agent groups to different provable/disprovable variants of the same problem statement in parallel, rather than committing the whole system to one hypothesis
- **Evidence**: Direct first-party process description.
- **Confidence**: emerging
- **Quote**: "For each problem, we prompted different groups of agents with different variants of the problem statement, covering all variants of the problem. For the Navier–Stokes problem, we suggested versions "A" and "B" (particular forms of the Navier–Stokes problem which would result in a proof) and versions "C" and "D" (which would result in a disproof) to separate groups of agents."
- **Our assessment**: This is a concrete "parallel hypothesis exploration" harness pattern — running agent groups against mutually exclusive outcome directions simultaneously so that whichever direction turns out to be true, some group has already been working on it. Directly relevant to Ch02 harness-engineering patterns for open-ended/uncertain-outcome tasks.

### Claim 5: A side effort on an "easier" adjacent problem (the unforced Euler regularity/blowup question) was resolved first by a small agent group (~100 agents, ~50 hours) and that surprise result caused OpenAI to redirect the bulk of its resources onto Navier–Stokes
- **Evidence**: Direct first-party process narrative, footnoted with a link to the separate Euler proof paper and its own Lean formalization.
- **Confidence**: emerging
- **Quote**: "In addition to the full Millennium Prize problems, we asked our multiagent system to try a set of "easier" problems. One of these problems was a similar blowup question for the limit of the Navier–Stokes problem with the viscosity term removed. This is known as the regularity problem for the Euler equations, and our agents surprised us by resolving this question. ... Nearly 100 agents worked together for approximately 50 hours to produce our Euler regularity disproof. ... Once we saw the Euler solution, we thought that Navier–Stokes was the most promising problem to work on. Thus, we decided to devote our resources to Navier–Stokes."
- **Our assessment**: An explicit "unplanned result reshapes resource allocation" narrative — the org treated an unexpected agent output as a signal to redirect a large-scale effort, rather than sticking to the original problem list. Relevant as a case study in adaptive, evidence-driven resourcing of large agent deployments.

### Claim 6: Mid-effort, OpenAI swapped the underlying model powering the agents to a further-trained checkpoint without restarting the effort, and found the winning approach by using Codex to cross-pollinate insights across independently-exploring agent groups
- **Evidence**: Direct first-party process description.
- **Confidence**: emerging
- **Quote**: "When a further trained version of our internal model became available over the course of the effort, we updated our agents to that model. We encouraged different groups of agents to explore a diversity of approaches. After some time, we cross-pollinated the agent groups by using Codex to consolidate the most useful insights from each agent group. These follow-up prompts drew on the agents' own intermediate results. The group that found the solution to Navier–Stokes was guided in such a way."
- **Our assessment**: Two distinct, separately notable harness techniques bundled in one paragraph: (1) live model upgrade of an in-flight, long-running multi-agent task, and (2) a dedicated synthesis pass — using a coding agent (Codex) as a cross-group insight aggregator rather than relying on any single group to converge alone. This "diverge, then synthesize" pattern is a concrete, large-scale example of the kind of orchestration topology `blog-anthropic-multi-agent-coordination-patterns.md` describes generically (see Cross-References).

### Claim 7: The agents reached their resolution 88 hours after the first agents were launched; a separate 17-hour Lean formalization-and-verification pass, run via GPT‑6 Astra (a different, already-shipped model), followed as a distinct stage
- **Evidence**: Direct first-party timeline disclosure.
- **Confidence**: emerging (specific, dated figures, self-reported)
- **Quote**: "The agents arrived at their resolution on Saturday, September 5, about 88 hours after the first agents were launched. Lean formalization and verification took an additional 17 hours via GPT‑6 Astra."
- **Our assessment**: The discovery model (an unreleased internal checkpoint) and the verification model (GPT‑6 Astra, already shipped) are explicitly different models. This is a clean, dated example of separating "the model that produces an artifact" from "the model/process that verifies it" — directly relevant to Ch03 verification patterns (see Guide Impact).

### Claim 8: Across all attempted Millennium/high-impact problems the agents sent 4.9 million messages and used ~300 billion output tokens; the Navier–Stokes effort specifically used 2.7 million messages and ~130 billion output tokens
- **Evidence**: Direct first-party aggregate usage figures.
- **Confidence**: emerging (specific, but self-reported with no disclosed cost/dollar figure, unlike the earlier `blog-simonwillison-ten-advances-mathematics.md` per-problem cost disclosure)
- **Quote**: "Across all attempted problems, the agents sent 4.9 million messages and used about 300 billion output tokens. In the process of resolving the Navier–Stokes problem, the agents sent 2.7 million messages and used approximately 130 billion output tokens."
- **Our assessment**: 130 billion output tokens for one proof is roughly two orders of magnitude larger than the "under $2,000 in GPT-5.6 Sol tokens per problem" figure OpenAI gave a month earlier for its ten-open-problems effort (see Cross-References: Extends). No dollar cost is given here, which is a gap relative to that earlier disclosure — a natural target for a future Miner pass if OpenAI publishes one.

### Claim 9: OpenAI's effort was itself triggered by a rumor about concurrent work by Levent Alpöge (an Anthropic employee) and Tristan Buckmaster (an NYU math professor); on completing its own result, OpenAI proactively reached out to offer a joint/concurrent announcement and to recognize the other team's priority, and learned the other team had instead resolved the (different) forced Euler problem using an internal Anthropic model
- **Evidence**: Direct first-party narrative in the "Concurrent work" section.
- **Confidence**: emerging
- **Quote**: "Our effort began on September 1st after hearing a rumor which we later realized was related to Levent Alpöge, an Anthropic employee, and Tristan Buckmaster, a math professor at NYU. ... After the completion of our full project and Lean verification (on September 6th), believing from the rumor they also had a solution of Navier–Stokes, we reached out to them to offer a concurrent release of our result and to recognize their priority in a joint announcement. At that point we found out that, using an internal Anthropic model, they had produced a resolution of the forced Euler problem. ... We recognize the priority of their work on forced Euler and congratulate them on their remarkable mathematical achievement."
- **Our assessment**: A concrete instance of cross-lab research-priority etiquette (offering joint/concurrent release, sharing prompts and the proof itself with the other team) at a moment of genuine competitive stakes. Relevant less as an engineering pattern and more as evidence of norm-setting among frontier labs when results overlap — a thin but real Ch05/industry-context data point.

### Claim 10: OpenAI states no specific user data was accessed to solve the problem, and that a post-hoc investigation confirmed Buckmaster's Codex prompts over the two months preceding the announcement could not have influenced the system in any way, including through training
- **Evidence**: Direct first-party governance claim, explicitly added as a September 10, 2026 update to the original September 8 post (per footnote 2).
- **Confidence**: emerging (a specific, falsifiable data-governance claim, but self-investigated and self-reported — no named external auditor)
- **Quote**: "We (the researchers and the agents) did not see any of their work through any means until they released it publicly — in particular, no specific user data was accessed in order to solve this problem. Following an investigation, we have confirmed that Buckmaster's Codex prompts over the two months preceding this announcement and paper on September 8, 2026, could not have influenced the system in any way, including through training. The OpenAI internal model used for this result was developed through large-scale reinforcement learning on top of a previously pretrained model."
- **Our assessment**: This is the most consequential claim in the post for the guide's security/governance chapter: OpenAI is publicly attesting, in response to an implicit "did you train on a competitor's customer's prompts" question, that a specific customer's (Buckmaster's) product usage (Codex prompts) could not have leaked into a training run that produced a headline result — and that it ran a dedicated investigation to confirm this after the fact, then amended the live post to disclose the finding. This is a rare, concrete, dated example of a lab publicly self-auditing and disclosing findings about training-data/customer-prompt isolation, prompted by a specific real-world scenario rather than as a generic policy statement.

### Claim 11: OpenAI explicitly disclaims any intent to claim the Millennium Prize money for this result and frames it as "a snapshot in time" rather than a culmination, tying the release to a stated philosophy of wanting AI progress to be "steerable, accountable, and connected to people"
- **Evidence**: Direct first-party framing statement closing the post.
- **Confidence**: anecdotal (values/intent statement, not a falsifiable claim)
- **Quote**: "Our goal in releasing this result is to report on the substantial progress of our AI models. We do not intend to claim the Millennium Prize for this result. This milestone represents substantial work by mathematicians and AI researchers. However, this is not a culmination, but rather a snapshot in time, of progress on AI development." (a source-side inline-link span splits "We" across a line break in the raw extracted text — rendered here as a single word per this corpus's normalization convention) / "One of our key goals is to build AI systems which are steerable, accountable, and connected to people, which may require more deliberate choices about the pace of progress..."
- **Our assessment**: Consistent with the "capability preview, not a product" framing of Claim 2 — OpenAI is using this result primarily as a public signal of internal model capability and pacing philosophy, not as a mathematics-prize claim.

## Concrete Artifacts

```
Timeline (from "How we found the proof" section, OpenAI, Sep 8 2026):
- Aug 28, 2026:            training begins on new internal model (still training/improving during the effort)
- Tue Sep 1, 2026:         rumor of two solved Millennium Prize problems heard; effort launched
                           against all open Millennium Prize problems + other high-impact problems
- (early, ~50 hrs, ~100 agents): unforced Euler regularity disproof found as a side "easier" problem
- (mid-effort):            model swap to a further-trained checkpoint; Codex used to cross-pollinate
                           insights across independently-exploring agent groups
- Sat Sep 5, 2026 (T+88h): agents arrive at Navier-Stokes resolution
- Sep 6, 2026 (+17h):      Lean formalization and verification complete, via GPT-6 Astra
- Sep 8, 2026:             public announcement + paper + Lean formalization published
- Sep 10, 2026:            post updated with data-governance investigation findings ("Concurrent work" section)

Scale (self-reported, OpenAI):
- ~10,000 concurrent agents in the group that produced the Navier-Stokes resolution
- Across ALL attempted problems: 4.9M messages, ~300B output tokens
- For Navier-Stokes specifically: 2.7M messages, ~130B output tokens
- Agent tooling: cached-internet read access, code execution
- Coordination: agents subdivided into groups, agents communicate within their group;
  separate groups assigned different provable ("A"/"B") vs disprovable ("C"/"D") problem variants
```

## Cross-References

- **Extends**: `blog-simonwillison-ten-advances-mathematics.md` — the same OpenAI
  program (internal-model-on-hard-math-problems, Lean formalization, independent
  checking) one month earlier, at ten decade-stale open problems for "under $2,000
  in GPT-5.6 Sol tokens per problem." This source shows the program escalating to
  a Millennium Prize problem with a far larger single-problem token budget (~130B
  output tokens, no dollar figure disclosed) and a far larger agent count, plus
  a second-model verification stage (GPT‑6 Astra doing Lean formalization) that
  the "ten advances" post's "Comparator" independent-checker concept parallels.
- **Corroborates**: `blog-openai-astra-safety-overview.md` — that post's disclosed
  internal-use safeguards ("stricter isolation," "universal monitoring of full
  trajectories," "a blocking alignment evaluation process before internal use")
  are the same category of safeguard this post references generically ("the same
  strict safeguards that we apply to all our frontier model evaluations, including
  monitoring and isolation") for the ~10,000-agent Navier-Stokes deployment —
  this post is the first in the corpus to confirm those safeguards were applied
  at that specific scale for an internal research effort, not just for shipped-model
  external deployment.
- **Corroborates**: `blog-anthropic-multi-agent-coordination-patterns.md` — this
  post's "diverse independent exploration, then Codex-driven cross-pollination"
  technique (Claim 6) is a concrete, extreme-scale instance of the generic
  "diverge then synthesize" orchestration idea that Anthropic's coordination-patterns
  post describes taxonomically (e.g. its agent-teams / orchestrator-subagent
  patterns) — this source adds a dated, quantified real-world data point at a
  scale (10,000 agents) far beyond the illustrative examples in that post.
- **Related tension (not a formal contradiction)**: `blog-pragmaticengineer-orosz-wayne-formal-methods.md`
  — Hillel Wayne predicts AI will only modestly expand *industry-wide* formal-methods
  adoption (his estimate: "from maybe 0.1% to 0.3%"), because successful AI-assisted
  formal-spec authors are already formal-methods experts. This post doesn't contradict
  that industry-adoption claim (different scope: one frontier lab's internal capability
  demonstration vs. broad practitioner adoption rates), but it is a striking existence
  proof that a frontier lab can now run a full natural-language-proof-to-Lean-formalization
  pipeline as a standard verification stage (17 hours, via an already-shipped model) on a
  problem of genuine difficulty — worth flagging as a data point if Ch03 ever revisits
  Wayne's adoption-rate prediction.
- **Novel**: The mid-run model swap on a single long-running multi-agent task (Claim 6);
  the "assign different agent groups to mutually exclusive outcome hypotheses in parallel"
  pattern (Claim 4); and the dated, publicly-disclosed post-hoc investigation into whether
  a specific named individual's product usage at a *different company* could have leaked
  into a training run (Claim 10) are all new to this corpus.

## Guide Impact

- **Ch02 (harness-engineering)**: Add this as a large-scale case study of two
  orchestration patterns not yet documented at this scale in the guide: (1)
  parallel hypothesis exploration — assigning independent agent groups to
  mutually exclusive outcome directions so progress isn't blocked on picking
  the right direction upfront (Claim 4); and (2) diverge-then-synthesize —
  independent agent groups explore freely, then a dedicated agent pass (Codex)
  consolidates cross-group insights before any group converges alone (Claim 6).
  Cite alongside `blog-anthropic-multi-agent-coordination-patterns.md` for the
  generic pattern description.
- **Ch03 (verification)**: Add as a concrete example of separating the
  artifact-producing model from the artifact-verifying model/process: the
  unreleased internal model produced the proof (88 hours), and a different,
  already-shipped model (GPT‑6 Astra) performed independent Lean formalization
  and verification as a distinct 17-hour stage (Claim 7, Claim 1). This is a
  clean illustration of "verify with a different agent/pass than the one that
  produced the work," a pattern the guide already recommends in principle.
- **Ch06 (security/threat model)**: Add the data-governance disclosure (Claim
  10) as a concrete example of a lab publicly attesting to, and investigating,
  whether a specific customer's product prompts at a rival lab could have
  leaked into a training run that produced a public result. Useful as a
  real-world reference point for enterprise customers asking "could our
  prompts end up training a competitor's model, or vice versa" — this shows
  what a public, dated response to that exact question looks like in practice
  (including the caveat that the claim is self-investigated, not externally
  audited).

## Extraction Notes

- The live page at `openai.com/index/navier-stokes-solution` returned an
  HTTP 403 (Cloudflare challenge / anti-bot interstitial) on direct fetch,
  consistent with the Prospector's triage note that the source was "currently
  not accessible due to Cloudflare protection." It was read via the Wayback
  Machine's archived snapshot from September 15, 2026
  (`web.archive.org/web/20260915112909/https://openai.com/index/navier-stokes-solution/`),
  which returned HTTP 200 with the full page content, fetched one day before
  extraction and seven days after publication — post-dating the disclosed
  September 10, 2026 update to the "Concurrent work" section, so that update
  is included in this note.
- The page links to two external artifacts not fetched by this Miner pass:
  the full proof paper ("Read the paper") and the Lean-formalized proof
  repository/link. This note extracts the announcement's own text and process
  claims; it does not verify the mathematical proof itself, which is out of
  scope for this guide.
- The "Keep reading" footer links to two same-day-adjacent OpenAI/Willison
  posts already in this corpus (`blog-simonwillison-research-acceleration-view-inside-openai.md`
  covers "An Alien Mind" and "Research acceleration: The view inside OpenAI,"
  both Sept 6, 2026) and to a GPT-6 Astra launch post (Sept 3, 2026,
  underlying `blog-openai-astra-safety-overview.md`); no new sub-pages beyond
  those already-mined notes were followed, since the "Keep reading" links
  point to distinct articles rather than continuations of this one.
- A companion commentary piece, Simon Willison's "Some thoughts on the
  Navier–Stokes Millennium Prize Problem," is tracked separately as issue
  #3421 (open, not yet triaged/mined at the time of this note) — a future
  Miner pass on that issue should cross-reference this note under Extends.
