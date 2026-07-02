---
source_url: https://addyosmani.com/blog/new-sdlc-vibe-coding/
source_type: blog-post
title: "The New Software Lifecycle"
author: Addy Osmani
date_published: 2026-06-16
date_extracted: 2026-07-02
last_checked: 2026-07-02
status: current
confidence_overall: emerging
issue: "#1424"
---

# The New Software Lifecycle

> Osmani's synthesis of a Google whitepaper he co-authored ("The New SDLC With
> Vibe Coding," with Shubham Saboo and Sokratis Kartakis), giving a rough
> 10%-model/90%-harness split, an eval-over-demo verification framework, a
> phase-by-phase account of where the SDLC compresses unevenly, and a
> total-cost-of-ownership argument that vibe coding costs 3-10x more per
> feature than agentic engineering past a lifespan-dependent crossover point.

## Source Context

- **Type**: blog-post (personal blog, addyosmani.com; ~1,500 words; published
  June 16, 2026). The post is explicitly a curated digest of a longer Google
  whitepaper ("The New SDLC With Vibe Coding," hosted on Kaggle), not a
  standalone piece of original research — Osmani states he is deliberately
  skipping the paper's introductory material and picking out "the handful of
  ideas in it I think actually matter, plus six figures."
- **Author credibility**: Addy Osmani spent 14+ years at Google leading
  developer experience across Chrome and, more recently, AI (Gemini, coding
  agents, agentic engineering), most recently as a Director at Google Cloud
  AI. He is already a top-cited corpus source via `blog-addyosmani-code-agent-orchestra.md`,
  `blog-addyosmani-loop-engineering.md`, `blog-addyosmani-intent-debt.md`, and
  `blog-osmani-good-spec.md`. Unlike those posts, this one carries a co-authorship
  credential — Osmani is a named co-author of the underlying Google whitepaper,
  not just a synthesizer citing someone else's work — which raises the
  authority of the framework claims (10/90 split, context taxonomy, output/trajectory
  eval split) above his usual practitioner-synthesis baseline, though the two
  headline benchmark statistics (Terminal Bench, LangChain) are still reported
  secondhand without methodology.
- **Scope**: Covers the model/harness split and its benchmark evidence; a
  six-type context taxonomy and the static/dynamic architectural boundary;
  the tests-vs-evals (output eval + trajectory eval) verification framework;
  a phase-by-phase account of how AI compresses the SDLC unevenly
  (requirements, architecture, implementation, testing/QA, maintenance); the
  "80% problem" ceiling; a total-cost-of-ownership argument for why vibe
  coding is more expensive per feature past a crossover point; context
  engineering and model routing as financial levers; the collapse of
  prototype-building and production-agent-building into one workflow
  (illustrated by Google's Agents CLI and an Anthropic multi-agent C-compiler
  experiment); the conductor/orchestrator mode distinction; and 2026 adoption
  statistics. Does NOT include the whitepaper's full text, its six figures
  (referenced but not reproduced by Osmani in the blog post itself), its
  "recommendations for individuals, leaders and organizations" section (Osmani
  explicitly declines to repeat these), or any first-hand benchmark
  methodology for the Terminal Bench/LangChain numbers.

## Extracted Claims

### Claim 1: An agent is a model plus a harness, with a rough 10% model / 90% harness split
- **Evidence**: Author's framing, attributed directly to the co-authored
  Google whitepaper.
- **Confidence**: emerging (a named split from a co-authored whitepaper, not
  an independently measured ratio)
- **Quote**: "The paper's rough split is 10% model, 90% harness. That sounds
  high until you've spent a week debugging one. The model is the engine. The
  harness is the car, the road, and the traffic laws."
- **Our assessment**: This is the same "Agent = Model + Harness" formulation
  already in the corpus via `blog-addyosmani-loop-engineering.md` Linked
  Source 1 ("Agent Harness Engineering," attributed there to Viv Trivedy's
  formulation: "If you're not the model, you're the harness"), but this is
  the first appearance in our corpus of the specific 10%/90% numeric split,
  and it now carries whitepaper-level attribution rather than a single
  practitioner's framing. The number itself is not derived from a stated
  methodology — treat the ratio as illustrative shorthand for "the harness
  dominates," not a measured proportion of engineering effort or token spend.

### Claim 2: Two independent teams improved coding-agent benchmark performance substantially by changing only the harness, not the model
- **Evidence**: Two cited data points: Terminal Bench 2.0 (one team moved a
  coding agent from outside the top 30 into the top 5) and a separate
  LangChain experiment (+13.7 points on the same benchmark via system prompt,
  tools, and middleware changes only).
- **Confidence**: emerging (specific, citable benchmark deltas, but reported
  secondhand with no named team, no methodology, and no link to the primary
  benchmark writeups)
- **Quote**: "On Terminal Bench 2.0, one team moved a coding agent from
  outside the top 30 into the top 5 by changing only the harness, with the
  same model underneath. A separate experiment at LangChain added 13.7 points
  on the same benchmark by changing just the system prompt, tools and
  middleware around a fixed model. Neither touched the model."
- **Our assessment**: The Terminal Bench top-30-to-top-5 figure is not new to
  our corpus — `blog-addyosmani-loop-engineering.md` Linked Source 1 already
  documents this identical statistic, there attributed by name to "Viv
  Trivedy's team." This post repeats the number without that attribution,
  which is a small fidelity loss worth flagging (a reader of only this post
  would not know whose result it is). The LangChain +13.7-points figure is
  new to our corpus. Both data points support the same underlying claim
  (harness changes move benchmark scores more than model changes do), which
  strengthens the harness-engineering thesis already well-represented in the
  guide's source base, but neither figure should be cited without the caveat
  that we have not independently verified the benchmark methodology.

### Claim 3: Most agent failures are configuration (harness) failures, not model failures, so debug the harness first
- **Evidence**: Author's practitioner heuristic, following directly from
  Claim 1 and Claim 2.
- **Confidence**: anecdotal (a diagnostic heuristic, not a measured failure
  taxonomy)
- **Quote**: "So when an agent does something dumb, I've learned to debug the
  harness first. Usually it's a missing tool, a rule I wrote too loosely, a
  guardrail I forgot, or a context window full of junk. Most agent failures
  are configuration failures."
- **Our assessment**: This is a restatement of a load-bearing thesis already
  present across our Osmani-sourced notes and consistent with the guide's
  existing harness-engineering content, so it corroborates rather than
  extends the corpus. Its value here is that it is now explicitly tied to the
  whitepaper's model/harness split rather than presented as personal opinion
  alone.

### Claim 4: The static-versus-dynamic context boundary is the decision that determines an agent's token bill, and should be treated as a reviewed, versioned architectural decision
- **Evidence**: Author's description of the whitepaper's six-type context
  taxonomy (instructions, knowledge, memory, examples, tools, guardrails) and
  the static/dynamic split within it.
- **Confidence**: emerging (a prescriptive architectural recommendation
  attributed to the whitepaper, not a measured cost-optimization result)
- **Quote**: "Static context is loaded on every turn, so it's reliable and
  expensive. Dynamic context is loaded on demand, so you only pay for what a
  task needs. [...] The paper's advice, which I agree with, is to treat the
  boundary as a real architectural decision: reviewed in a pull request,
  versioned like code."
- **Our assessment**: This gives explicit process backing (PR review,
  versioning) to a static/dynamic split that our corpus has previously
  discussed mainly in terms of what belongs in each category, not how the
  boundary itself should be governed. This is a concrete, actionable addition:
  it reframes context engineering from a content question ("what goes in
  CLAUDE.md") to a governance question ("who approves moving something from
  dynamic to static context, and how is that change reviewed").

### Claim 5: Agent Skills with progressive disclosure are the mechanism that makes dynamic context scale economically
- **Evidence**: Author's description of skill-loading behavior.
- **Confidence**: emerging (feature-mechanism description, not a benchmarked
  comparison against a non-progressive-disclosure baseline)
- **Quote**: "The trick that makes dynamic context scale is Agent Skills with
  progressive disclosure. The agent sees a little metadata at startup, loads
  the full instructions when a task matches, and only pulls in the heavy
  reference material when it actually needs it. That's how one agent can
  carry dozens of skills and still only pay for the one it's using."
- **Our assessment**: This directly corroborates
  `blog-addyosmani-loop-engineering.md` Claim 6 (skills exist to stop an agent
  from re-deriving project context every session) and extends it by naming
  progressive disclosure specifically as the economic mechanism, not just the
  authoring format. No new evidence is introduced beyond what that note
  already covers; this is best read as a restatement anchored to the
  whitepaper's context taxonomy.

### Claim 6: Verification splits into tests (deterministic) and evals (output evaluation plus trajectory evaluation); the bar for trustworthy agent work should be set at the eval, not the demo
- **Evidence**: Author's description of the whitepaper's verification
  framework.
- **Confidence**: emerging (a named framework distinction attributed to the
  whitepaper; not independently benchmarked in this post)
- **Quote**: "Tests cover the deterministic parts: this input, that output.
  Evals cover the parts that aren't deterministic, and the paper splits them
  in a way I found useful. Output evaluation asks whether the final result is
  correct. Trajectory evaluation asks whether the path it took to get there,
  the tool calls and the reasoning, was sound. [...] If I had to hand a
  leader one line from the paper, it's this: set the bar at the eval, not the
  demo. A demo shows an agent can work once. An eval suite with a real rubric
  shows it works reliably."
- **Our assessment**: This is one of the two most load-bearing claims in the
  post for our guide. It gives a clean, two-part vocabulary (output eval vs.
  trajectory eval) for a distinction our corpus has previously gestured at
  without naming crisply — `blog-addyosmani-code-agent-orchestra.md` Claim 5
  frames verification as the shifted bottleneck but does not decompose
  "eval" this way. "Set the bar at the eval, not the demo" is a strong,
  quotable one-liner for a guide chapter on verification maturity.

### Claim 7: AI compresses the software lifecycle unevenly — implementation collapses from weeks to hours while requirements, architecture, and verification stay slow because they are judgment work — which relocates the bottleneck rather than removing it
- **Evidence**: Author's framing of the whitepaper's central lifecycle
  argument, elaborated phase by phase in the rest of the post.
- **Confidence**: emerging (a structural thesis attributed to the whitepaper;
  corroborated directionally by the phase-specific evidence below, but the
  thesis itself is asserted rather than measured as a single statistic)
- **Quote**: "AI compresses the lifecycle, but unevenly, and the unevenness
  is the whole story. Implementation drops from weeks to hours. Requirements,
  architecture and verification stay slow, because they're judgment work. So
  specification quality becomes the bottleneck, and verification moves to
  the middle. Same phases, different bottlenecks, different proportions."
- **Our assessment**: This is the organizing thesis of the whole post and is
  directly continuous with the corpus's existing convergence on
  "verification/specification, not generation, is the bottleneck" —
  `blog-addyosmani-code-agent-orchestra.md` Claim 5 and Claim 10,
  `blog-addyosmani-intent-debt.md` Claim 9, and Fung's identical observation
  in `blog-anthropic-ai-native-engineering-org.md`. This source's specific
  contribution is framing that convergence as a *lifecycle-phase* argument
  (which phases compress, which don't) rather than a general bottleneck
  statement, which is a more directly guide-actionable structure.

### Claim 8: Architecture is the most stubbornly human-resistant SDLC phase because its trade-offs depend on business context the model cannot see
- **Evidence**: Author's phase-specific claim within the lifecycle breakdown.
- **Confidence**: emerging (asserted, not benchmarked; consistent with the
  general "judgment work resists automation" framing used elsewhere in the
  post)
- **Quote**: "Architecture is the most stubbornly human phase. Trade-offs
  like consistency versus availability depend on business context the model
  can't fully see. The developer's job becomes making and documenting the
  structural calls the agent then implements."
- **Our assessment**: This is a specific, testable claim (architecture
  resists compression more than any other phase) that the post does not
  actually support with comparative data across phases — it is presented as
  self-evident rather than measured against, say, requirements or testing.
  We find it plausible on structural grounds (trade-offs requiring
  unstated business context are a known LLM blind spot) but flag it as the
  weakest-evidenced of the phase-specific claims in this note.

### Claim 9: Implementation shows contradictory productivity numbers depending on measurement method — survey-reported gains of 25-39% versus a METR-measured 19% slowdown once review and fix time is counted — and both are true
- **Evidence**: Author cites two different figures without reconciling them
  into one number, instead arguing the discrepancy itself is the finding.
- **Confidence**: settled for the METR sub-claim (an existing, independently
  measured study already in our corpus), emerging for the survey figure and
  for Osmani's synthesis of the two
- **Quote**: "Surveys put the productivity gain at 25 to 39%. A METR study
  found experienced developers going 19% slower on some tasks once you count
  the time spent checking and fixing. Both are true. The honest summary is
  that AI turns implementation from writing into reviewing."
- **Our assessment**: The METR figure directly corroborates
  `research-anthropic-ai-transforming-work.md` (Claim 2's assessment
  discussion), which already documents "the METR study (pre-cutoff) found
  that experienced developers self-reported a 24% productivity gain while
  objective measurement showed a 19% slowdown on the same tasks" — same
  study, same 19% figure, independently cited by two different sources. This
  is a strong corroboration point. The 25-39% survey figure is new to our
  corpus and less trustworthy on its own (no survey named, no methodology),
  but Osmani's framing — that the discrepancy itself is the honest finding,
  because "implementation" now means "writing then reviewing," and
  self-reported velocity and measured wall-clock time are answering different
  questions — is a genuinely useful synthesis that the guide should adopt
  rather than trying to pick one number.

### Claim 10: Maintenance is the most underrated phase — code previously "too risky to touch" because only its original authors understood it can now be read, refactored, and modernized by an agent
- **Evidence**: Author's phase-specific claim, framed as a personal
  assessment ("the one I think is most underrated") rather than a whitepaper
  attribution.
- **Confidence**: anecdotal (author's opinion, no measurement or case study
  cited)
- **Quote**: "Maintenance is the one I think is most underrated. Code that
  was "too risky to touch" because only its authors understood it can now be
  read, refactored and modernized by an agent. The migrations and
  deprecation cleanups that never happened because they were tedious and
  risky start happening."
- **Our assessment**: This is a novel, specific claim for our corpus — none
  of the existing Osmani-sourced notes name maintenance/legacy-migration as
  the phase with the most latent, previously-blocked upside. It is worth
  testing against practitioner reports rather than accepting on Osmani's
  authority alone, since it is explicitly marked as his personal ranking, not
  the whitepaper's.

### Claim 11: The "80% problem" persists as a ceiling — agents deliver the first 80% of a feature fast, but the last 20% (edge cases and the seams between systems) still requires context models usually don't have
- **Evidence**: Author's closing statement on the phase-by-phase section,
  linking out to a separate Osmani piece ("The 80% Problem in Agentic
  Coding," hosted on Substack, not addyosmani.com) for the concept's origin.
- **Confidence**: emerging (a named, recurring practitioner concept; not
  measured with a specific percentage-of-features-blocked statistic in this
  post)
- **Quote**: "The ceiling on all of this is still the 80% problem: agents get
  the first 80% of a feature fast, and the last 20%, the edge cases and the
  seams between systems, still needs context the models usually don't have."
- **Our assessment**: This names a ceiling concept not previously labeled
  this way anywhere in our corpus (a targeted search for "80% problem" and
  "last 20%" phrasing across existing source notes returned no hits before
  this extraction). It is consistent with, and gives a memorable label to,
  the general "generation is solved, the edges aren't" pattern already
  present via the verification-bottleneck claims above, but the specific
  "80/20" framing and its origin as a separate Osmani Substack post are new
  and worth a dedicated future extraction (see Additional Sources to
  Enqueue).

### Claim 12: Vibe coding costs 3 to 10x more per feature than agentic engineering once a lifespan-dependent crossover point is passed, because the cost structure inverts — cheap up front and expensive to run, versus more up front and cheaper per feature after
- **Evidence**: Author's total-cost-of-ownership argument, explicitly
  self-caveated as illustrative rather than measured.
- **Confidence**: emerging, with an explicit author caveat downgrading it
  further — the post itself states this specific multiplier is not a
  measured constant
- **Quote**: "Past the crossover, vibe coding costs 3 to 10x more per
  feature. How long the code has to live decides whether you ever get
  there. [...] Vibe coding is cheap up front and expensive to run. [...]
  Agentic engineering flips that: more up front (schemas, tests, structured
  context), less per feature after. [...] The "vibe coding costs 3 to 10x
  more per feature" crossover is illustrative, not a measured constant."
- **Our assessment**: We weight this appropriately low because Osmani
  himself flags it as illustrative rather than a measured number — a rare
  and useful bit of self-correction that the guide should preserve alongside
  the claim itself, since the multiplier is likely to get cited without that
  caveat if lifted out of context. The underlying cost-structure logic (token
  burn from unstructured fixing, later maintenance tax, security cleanup vs.
  upfront schema/test/context investment) is directionally consistent with
  the corpus's existing TCO-style arguments but is not new evidence on its
  own.

### Claim 13: Context engineering and model routing are financial levers, not just technical ones — route hard reasoning to a large model and routine work (test generation, code review, CI checks) to a small, cheap model
- **Evidence**: Author's prescriptive economic argument, tying together the
  context and routing threads of the post.
- **Confidence**: emerging (practitioner recommendation, no cost-benchmark
  data provided in this post)
- **Quote**: "You can't pass a 100,000-token repo into every prompt and
  expect it to scale. Route the hard reasoning to a big model and the
  routine work, test generation, code review, CI checks, to a small cheap
  one. The quality holds and the bill comes down. That's the money side of
  what I've called the orchestration tax."
- **Our assessment**: This corroborates `blog-addyosmani-code-agent-orchestra.md`
  Claim 9 (multi-model routing improves cost and quality), which our
  existing note already flagged as "plausible strategy but no evidence
  provided for effectiveness." This post does not add new evidence for the
  routing claim either — it repeats it, now explicitly tied to the
  "orchestration tax" concept documented in depth via
  `blog-addyosmani-loop-engineering.md` Linked Source 2. The claim remains at
  the same confidence level the corpus already assigned it; this source adds
  reinforcement, not new proof.

### Claim 14: Building, evaluating, and deploying a production agent is collapsing into the same terminal workflow used for throwaway prototypes
- **Evidence**: Description of Google's Agents CLI workflow (`uvx
  google-agents-cli setup`, then natural-language instructions inside the
  existing coding agent) plus a cited example of an Anthropic team building a
  working C compiler in Rust with a group of agents over two weeks, with
  humans "setting direction and reviewing rather than writing the code."
- **Confidence**: anecdotal (a vendor CLI description plus a single
  unattributed-by-name example, not a benchmarked or reproducible result)
- **Quote**: "The same terminal workflow that spits out a throwaway script
  can now produce a production agent, in the same place, often by talking to
  the coding agent you were already using. [...] There's one experiment in
  the paper I keep mentioning to people. An Anthropic team had a group of
  agents build a working C compiler in Rust over two weeks, with humans
  setting direction and reviewing rather than writing the code. That's
  roughly the shape of where this is heading."
- **Our assessment**: The Google Agents CLI description is a vendor feature
  description (Google-affiliated author describing a Google product), so we
  weight the "no rewrite needed" framing as marketing-adjacent rather than
  independently verified. The C-compiler anecdote is a striking data point
  but is secondhand (via the whitepaper, no link to a primary writeup, no
  team named) — treat as illustrative of "the ceiling of what's
  demonstrated," not as a reproducible benchmark. Coordination is stated to
  run on MCP (tools) and A2A (agent-to-agent), which is consistent with
  existing corpus coverage of MCP-based agent coordination.

### Claim 15: Conductor and orchestrator are two coexisting daily-use modes, not a linear evolution from one to the other — practitioners switch between them, sometimes within the same hour
- **Evidence**: Author's description of the whitepaper's two named modes:
  conductor (real-time, in-IDE, keystroke-by-keystroke) and orchestrator
  (async, goal-handoff, review-what-comes-back).
- **Confidence**: emerging (a named framework distinction; the "same hour"
  co-occurrence claim is asserted, not measured)
- **Quote**: "Day to day you switch between two modes the paper calls the
  conductor and the orchestrator. The conductor is real-time and in the IDE,
  keystroke by keystroke, good for exploring and for code you don't know
  yet. The orchestrator is async: you hand a goal to one or more agents and
  review what comes back, good for well-specified work like migrations or
  test generation. The tooling does both now, sometimes in the same hour."
- **Our assessment**: The conductor/orchestrator distinction did not
  originate in this post or in `blog-addyosmani-code-agent-orchestra.md`
  (which uses the terms in its own summary but does not extract them as a
  numbered claim) — it traces to Osmani's earlier, dedicated post "The
  future of agentic coding: conductors to orchestrators" (January 2, 2026),
  which frames the two modes as a career-stage progression ("junior
  developers might start as 'AI conductors'... before they take on
  orchestrating many") rather than same-hour coexistence. This post's
  framing — both modes used fluidly by the same practitioner in the same
  session — is a meaningfully different emphasis from the original post's
  progression framing, though not a contradiction (the original post itself
  also says "these roles are fluid, not rigid categories"). See Additional
  Sources to Enqueue: the originating post has not yet been separately mined
  and contains substantially more detail (a full tool-by-tool survey circa
  January 2026) than either post's brief restatement.

### Claim 16: As of early 2026, adoption has crossed a threshold — 85% of professional developers use AI coding agents regularly, 51% use them daily, and roughly 41% of new code is AI-generated
- **Evidence**: Author's cited adoption statistics, attributed to the
  whitepaper but without a named survey or methodology.
- **Confidence**: emerging (concrete, specific numbers, but no named source
  study, sample size, or methodology given in this post)
- **Quote**: "As of early 2026, 85% of professional developers use AI coding
  agents regularly, 51% use them daily, and roughly 41% of new code is
  AI-generated."
- **Our assessment**: These are point-in-time adoption figures useful for
  guide framing ("is this real yet") but should not be over-cited as
  precise measurements — we searched the corpus for matching 85%/51%/41%
  figures and found no exact corroborating match (the 41% figures appearing
  elsewhere in the corpus, e.g. in `survey-pragmaticengineer-ai-tooling-2026.md`,
  refer to a different metric — a 41% complexity increase, not adoption
  share). Treat as a standalone, whitepaper-sourced data point pending
  independent verification of the underlying survey.

## Concrete Artifacts

```
Source: Addy Osmani, "The New Software Lifecycle," https://addyosmani.com/blog/new-sdlc-vibe-coding/ (June 16, 2026)

Google Agents CLI workflow, as described in the post:

# one-time setup
uvx google-agents-cli setup

# then, in your coding agent:
> Build a support agent that answers questions from our docs.
> Evaluate it on the FAQ dataset.
> Deploy it to Agent Engine.
```

```
Source: same post

Whitepaper attribution and title:
"Google published The New SDLC With Vibe Coding this week. I co-wrote it
with Shubham Saboo and Sokratis Kartakis, and it's the first in a short
series."
Full paper hosted at: https://www.kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding
(not independently fetched or verified as part of this extraction — see
Additional Sources to Enqueue)
```

```
Source: same post

Six agent context types named in the post (not individually defined beyond
the static/dynamic split): instructions, knowledge, memory, examples, tools,
guardrails.
```

## Cross-References

- **Corroborates**:
  - `blog-addyosmani-loop-engineering.md` Linked Source 1 ("Agent Harness
    Engineering"): the Terminal Bench 2.0 top-30-to-top-5 harness-only
    improvement (Claim 2 here) is the identical statistic that note
    attributes by name to Viv Trivedy's team — this post repeats the number
    without that attribution.
  - `blog-addyosmani-loop-engineering.md` Claim 6 (skills exist to stop an
    agent re-deriving project context every session): directly corroborated
    and extended by Claim 5 here (progressive disclosure as the specific
    economic mechanism).
  - `blog-addyosmani-loop-engineering.md` Linked Source 2 ("The Orchestration
    Tax") and `blog-addyosmani-code-agent-orchestra.md` Claim 9 (multi-model
    routing): both corroborated by Claim 13 here, without new supporting
    evidence beyond what those sources already establish.
  - `research-anthropic-ai-transforming-work.md` (Claim 2's assessment
    discussion): the METR "19% slowdown" figure in Claim 9 here is the same
    study and the same number already documented there ("experienced
    developers self-reported a 24% productivity gain while objective
    measurement showed a 19% slowdown on the same tasks") — independent
    citation of the same underlying study by two different source authors.
  - `blog-addyosmani-code-agent-orchestra.md` Claim 5 and Claim 10, and
    `blog-addyosmani-intent-debt.md` Claim 9: all converge with Claim 7 here
    on "verification/specification, not generation, is the bottleneck" —
    this post's specific contribution is framing that convergence as a
    lifecycle-phase argument.

- **Contradicts**: None filed. The one internal tension worth flagging
  without treating as a corpus contradiction is Claim 15 here (conductor and
  orchestrator as same-session, coexisting modes) versus the career-stage
  progression framing in Osmani's own earlier "conductors to orchestrators"
  post (January 2026, not yet separately mined — see Additional Sources to
  Enqueue), which frames the shift more as a maturity ladder. This is a
  difference in emphasis within the same author's body of work, not a claim
  that would drive opposite guide advice (the earlier post also explicitly
  calls the roles "fluid, not rigid categories"), so per MINER.md 4a this was
  not filed as a contradiction issue.

- **Extends**:
  - `blog-addyosmani-code-agent-orchestra.md`: gives the conductor/orchestrator
    terminology used loosely in that note's summary a specific "same hour"
    coexistence framing (Claim 15) and traces it to its actual origin post.
  - `blog-osmani-good-spec.md`: the "curse of instructions" U-curve (too
    vague vs. too much) in that note's Claim 5 has a lifecycle-level
    analogue here in the static/dynamic context governance claim (Claim 4) —
    both are about where to draw a boundary under token/attention budget
    constraints, at different granularities (spec content vs. context
    architecture).
  - `blog-addyosmani-intent-debt.md`: Claim 5's "orchestration tax I wrote
    about is partly an intent-debt tax" already cites the orchestration-tax
    concept; Claim 13 here reinforces the same concept from the cost-routing
    angle rather than the intent-debt angle.

- **Novel**:
  - The specific 10%/90% model/harness split (Claim 1) is new to our corpus
    as a numeric ratio, even though the underlying "Agent = Model + Harness"
    framing is already present via the loop-engineering note.
  - The LangChain +13.7-points harness-only benchmark result (Claim 2) is new
    to our corpus.
  - The output-eval/trajectory-eval verification vocabulary (Claim 6) is a
    cleaner, more citable decomposition of "eval" than anything previously in
    the corpus.
  - The explicit phase-by-phase lifecycle breakdown (Claims 7-11) — naming
    architecture as most human-resistant and maintenance as most
    underrated — is a new organizing structure not previously present in
    this form.
  - The "80% problem" label (Claim 11) and its origin as a separate,
    not-yet-mined Osmani Substack post are new to the corpus.
  - The 85%/51%/41% 2026 adoption statistics (Claim 16) are new, specific
    figures not matched by any existing corpus source.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the 10%/90% model/harness split
  (Claim 1) as a memorable framing device alongside the existing "Agent =
  Model + Harness" content from the loop-engineering note, with the caveat
  that the ratio is illustrative, not measured. Add the LangChain +13.7-points
  and Terminal Bench top-30-to-top-5 data points (Claim 2) as two independent,
  though secondhand, benchmark examples of harness-only improvement — note
  the Terminal Bench figure is already sourced with better attribution
  (Viv Trivedy's team) via the loop-engineering note's linked-source
  extraction, so cite that version preferentially.

- **Chapter 02 (Harness Engineering) — Context governance**: Add Claim 4's
  recommendation to treat the static/dynamic context boundary as a
  PR-reviewed, versioned architectural decision. This is a concrete process
  recommendation ("who approves this, how is it reviewed") not currently
  present in the guide's context-engineering content, which has so far
  focused on what belongs in static vs. dynamic context rather than how
  changes to that boundary should be governed.

- **Chapter 02/03 (Verification)**: Add the output-eval / trajectory-eval
  vocabulary (Claim 6) as the canonical decomposition of "eval" for a
  verification-maturity section, alongside the "set the bar at the eval, not
  the demo" framing as a quotable summary line.

- **Chapter 05 (SDLC phases / Team Adoption, skeleton)**: This is the primary
  new content this source provides. Use Claim 7's uneven-compression thesis
  as the organizing structure for a phase-by-phase section: implementation
  compresses hardest, requirements/architecture/verification stay judgment-bound.
  Add Claim 8 (architecture as most human-resistant), Claim 9 (implementation's
  contradictory productivity numbers — cite this alongside the existing METR
  citation in `research-anthropic-ai-transforming-work.md` rather than as a
  standalone figure), Claim 10 (maintenance as most underrated, flagged as
  anecdotal/personal-opinion-graded), and Claim 11 (the "80% problem" ceiling,
  flagged for follow-up extraction of its origin post) as the phase-specific
  content.

- **Chapter 05 (Economics)**: Add Claim 12 (vibe coding costs 3-10x more per
  feature past a lifespan-dependent crossover) with Osmani's own caveat
  preserved prominently ("illustrative, not a measured constant") — this
  caveat must travel with the number or it will be miscited as measured.
  Add Claim 13 (context engineering and model routing as financial levers)
  as reinforcement of the existing routing recommendation, not as new
  evidence for it.

- **Chapter 01 (Daily Workflows)**: Add Claim 15's "same hour" coexistence
  framing for conductor/orchestrator modes as a corrective nuance to any
  guide content that presents the two as a strict progression — cite
  alongside a flag that Osmani's original January 2026 post on the topic has
  not yet been separately mined and likely contains more actionable detail
  (a tool-by-tool survey) than either restatement.

## Linked Source Extractions

Followed 5 of the post's internal links in total. Three lead to topics
already covered in depth elsewhere in the corpus and were used only for
cross-referencing (not re-fetched in full for this note, since their
extraction is already complete and citable):
- "Agent Harness Engineering" (April 19, 2026) — fully extracted as Linked
  Source 1 in `blog-addyosmani-loop-engineering.md`.
- "The Orchestration Tax" (May 24, 2026) — fully extracted as Linked Source 2
  in `blog-addyosmani-loop-engineering.md`.
- "The Factory Model" (Feb 25, 2026) — fully extracted as Linked Source 2 in
  `blog-addyosmani-code-agent-orchestra.md`.

Two links were fetched in full for this extraction because they underpin
central claims in this post (verification-as-bottleneck and the
conductor/orchestrator distinction) and are not yet separately mined:

### Linked Source A: "Agentic Code Review" (June 15, 2026)

**URL**: https://addyosmani.com/blog/agentic-code-review/

**Key findings** (partial — this post is dense enough to merit its own
dedicated source-note extraction; the following is what supports claims in
the main post, not an exhaustive extraction):
- Faros AI instrumented 22,000 developers across 4,000 teams (March 2026
  data): as AI adoption rose, code churn rose 861%, incident-to-PR ratio rose
  242.7%, per-developer defect rate rose from 9% to 54%, median review
  duration rose 441.5%, and PRs merged with zero review rose 31.3%.
  "Reviewers simply could not keep pace with the volume, so code began
  merging unread, and that became normal."
- GitClear: daily AI users produce ~4x the raw output of non-users, but
  measured against their own prior-year output, the real productivity gain is
  only ~12% — "You are generating roughly four times the code for something
  like a tenth more delivered value."
- CodeRabbit studied 470 open-source PRs (Dec 2025, 320 AI-coauthored vs. 150
  human-only): AI changes carried ~1.7x more issues (logic/correctness
  problems up ~75%, security issues 1.5-2x more common, readability problems
  more than tripling).
- GitHub Copilot review has run over 60 million reviews, a 10x increase in
  under a year; more than one in five reviews on GitHub now involves an
  agent.
- Anthropic's Code Review tool: under 1% of findings marked incorrect by
  their own engineers; raised the internal rate of PRs receiving a
  substantive review from 16% to 54%.
- An independent engineer ran four AI reviewers (CodeRabbit, Sentry Seer,
  Greptile, Cursor BugBot) in parallel across 146 real PRs / 679 findings
  over 3.5 weeks: of 617 distinct flagged locations, 93.4% were caught by
  exactly one of the four tools, ~6% by two, almost none by three, none by
  all four — direct empirical evidence for adversarial/heterogeneous review.
- Prescriptive framework: match review depth to blast radius, code lifespan,
  and number of people who need to understand it (not a one-size-fits-all
  review bar); "human in the loop becomes human on the loop" — sampling and
  auditing rather than reading every diff, with the "load-bearing paths" kept
  under human review regardless of scale.

**Guide impact**: This is the primary evidentiary basis for the "set the bar
at the eval, not the demo" claim (Claim 6 in the main note) and is
substantially more detailed and better-evidenced (four independent
measurement sources, one of them an original 146-PR field experiment) than
anything currently in our corpus on the volume-of-AI-code-vs-review-capacity
problem. **This should be flagged as the single highest-priority follow-up
source to mine separately** — it is denser and more rigorously evidenced than
the post that links to it.

### Linked Source B: "The future of agentic coding: conductors to orchestrators" (January 2, 2026)

**URL**: https://addyosmani.com/blog/future-agentic-coding/ (republished via
Osmani's Substack, "Elevate")

**Key findings** (partial): This is the originating post for the
conductor/orchestrator terminology used in both this post and
`blog-addyosmani-code-agent-orchestra.md`. It predates both. Key content not
carried forward into either later post:
- A detailed, named tool-by-tool survey circa January 2026 mapping specific
  products to each mode: conductors (Claude Code CLI in basic usage, Gemini
  CLI, Cursor inline/chat, VSCode/Cline/Roo Code) vs. orchestrators (GitHub
  Copilot Coding Agent, Google's Jules, OpenAI Codex cloud agent, Claude Code
  for Web, Cursor 2 Background Agents, plus orchestration platforms like
  Conductor by Melty Labs and Claude Squad).
- A five-dimension comparison table: scope of control, degree of autonomy,
  synchronous vs. asynchronous, artifacts/traceability, and human-effort
  profile (front-loaded + back-loaded for orchestrators vs. continuously
  engaged for conductors).
- Frames the shift as a career-stage progression: "Junior developers might
  start as 'AI conductors'... before they take on orchestrating many. Seasoned
  engineers are more likely to early-adopt orchestrator workflows."
- Names five open challenges for orchestrator-mode work: quality
  control/trust, coordination/conflict between parallel agents, context and
  state hand-offs, prompting/specification quality, and tooling/debugging
  when an autonomous agent gets stuck.

**Guide impact**: This is the actual origin of terminology the guide would
otherwise attribute only to the later, briefer restatements. If Chapter 01 or
05 cites the conductor/orchestrator distinction, this source — not the later
posts — has the concrete tool-mapping and the five-challenges list that would
make the distinction actionable rather than just definitional. Flagged as a
second high-priority follow-up source (see Additional Sources to Enqueue).

## Extraction Notes

- Full article text fetched via `curl` (with a browser user-agent) plus
  HTML-tag stripping, not the WebFetch summarization tool, so that every
  quote in this note could be checked character-for-character against the
  source's actual markup. An initial WebFetch pass was also run for
  triage purposes but its condensed output was not used as a quote source —
  cross-checking the WebFetch summary against the raw HTML found no outright
  fabrications, but the WebFetch version was too compressed to support
  verbatim quoting per MINER.md 2a, so it was discarded in favor of the raw
  extraction once the pattern from `blog-addyosmani-loop-engineering.md` and
  `blog-addyosmani-intent-debt.md` (both of which independently arrived at
  the same curl-based method) confirmed this was the reliable approach for
  this domain.
- Followed 5 internal links total (see Linked Source Extractions): 3 already
  have complete extractions elsewhere in the corpus and were used only for
  cross-referencing; 2 ("Agentic Code Review" and "The future of agentic
  coding: conductors to orchestrators") were fetched in full because they
  underpin central claims in the main post and are not yet separately mined.
  Both are flagged below as high-priority follow-up sources given their
  density of original data.
- Did not fetch the underlying Google whitepaper itself (hosted on Kaggle:
  `kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding`) — this note extracts
  Osmani's blog-post digest of it, not the primary document. The whitepaper
  is the actual primary source for the 10%/90% split, the context taxonomy,
  and the output/trajectory eval framework, and would merit its own
  extraction at higher confidence than this secondhand digest.
- Did not fetch the six figures the post references ("plus six figures
  you're welcome to reuse") — these are visual assets within the blog post
  itself (or the whitepaper) and were not reproducible as text; no attempt
  was made to describe their content since the post's prose does not
  describe what each figure shows beyond the topics already extracted above.
- No contradiction issue was filed. The one candidate tension (Claim 15
  here vs. the career-stage-progression framing in the January 2026
  originating post) was judged to be a difference in emphasis within the
  same author's own body of work, not a factual disagreement that would
  drive opposite guide advice — see Cross-References → Contradicts for the
  full reasoning. The Assayer should independently check this judgment.
- All cross-reference claim numbers cited above (from `blog-addyosmani-code-agent-orchestra.md`,
  `blog-addyosmani-loop-engineering.md`, `blog-addyosmani-intent-debt.md`,
  `blog-osmani-good-spec.md`, and `research-anthropic-ai-transforming-work.md`)
  were verified by re-reading the cited note's actual claim numbering before
  writing this note; none were guessed.

## Additional Sources to Enqueue

1. **The underlying Google whitepaper, "The New SDLC With Vibe Coding"**
   (Osmani, Saboo, Kartakis) — hosted at
   `kaggle.com/whitepaper-the-new-SDLC-with-vibe-coding`. Highest priority:
   it is the actual primary source for the 10%/90% split, the six-type
   context taxonomy, and the output/trajectory eval framework that this note
   only has secondhand via Osmani's digest.
2. **"Agentic Code Review"** (addyosmani.com/blog/agentic-code-review/, June
   15, 2026) — dense, multi-source empirical post (Faros AI 22,000-developer
   study, CodeRabbit 470-PR study, GitClear productivity data, an original
   146-PR four-reviewer field experiment) that is more rigorously evidenced
   than most of our existing corpus on the review-capacity bottleneck. See
   Linked Source A above for a partial extraction.
3. **"The future of agentic coding: conductors to orchestrators"**
   (addyosmani.com/blog/future-agentic-coding/, January 2, 2026) — the actual
   origin of the conductor/orchestrator terminology, with a detailed
   tool-by-tool survey and a five-challenges list not carried forward into
   later restatements. See Linked Source B above for a partial extraction.
4. **"The 80% Problem in Agentic Coding"** — hosted on Osmani's Substack
   (`addyo.substack.com/p/the-80-problem-in-agentic-coding`), linked from this
   post's "80% problem" reference (Claim 11). Not yet in our corpus; worth
   checking whether it contains a measured percentage or concrete examples
   beyond the one-sentence summary extracted here.
