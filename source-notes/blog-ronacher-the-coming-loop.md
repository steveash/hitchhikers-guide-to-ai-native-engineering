---
source_url: https://lucumr.pocoo.org/2026/6/23/the-coming-loop/
source_type: blog-post
title: "The Coming Loop"
author: Armin Ronacher
date_published: 2026-06-23
date_extracted: 2026-06-24
last_checked: 2026-06-24
status: current
confidence_overall: anecdotal
issue: "#1288"
---

# The Coming Loop

> Armin Ronacher distinguishes agent-internal loops from harness-level loops,
> argues that hands-off harness execution amplifies models' defensive-code
> anti-patterns, identifies the domains where loops genuinely succeed, and
> concludes that the question is no longer whether to loop but how to retain
> human judgment and engineering discipline within an inevitable looping future.

## Source Context

- **Type**: blog-post (lucumr.pocoo.org personal blog; ~3,600 words; seven named
  sections: "I Am Not Good At This Yet", "Where Loops Work", "Software As Organism",
  "You Cannot Quite Opt Out", "Building New Dependencies", "Future Harnesses",
  "Controlling Loops"; practitioner analysis published 2026-06-23)
- **Author credibility**: Armin Ronacher is the creator of Flask, Jinja2, Click, and
  Sentry, and the author of the Pi coding agent (described in blog-ronacher-pi-oss.md).
  His blog is a designated `trusted-feed` source in this repo. He uses Claude Code,
  Pi, and Fable daily and is building harness infrastructure at Earendil. This post
  is first-person practitioner analysis from someone who runs harness-level loops in
  production while also having specific architectural reservations about them. He
  uses the term "clanker" throughout (defined and defended in blog-ronacher-clanker-
  terminology.md). Claims are anecdotal; all evidence is first-person observation and
  practitioner synthesis from someone with deep operational exposure.
- **Scope**: Covers the conceptual distinction between agent loops and harness loops;
  code quality concerns from hands-off harness execution; the specific domains where
  loops succeed vs. fail; the software-as-organism metaphor and what it implies for
  comprehensibility; the opt-out impossibility (security and competitive pressure);
  operational and cognitive dependency risks from loop-produced codebases; and
  a normative conclusion about retaining judgment within a looping future. Does NOT
  cover: specific harness implementation patterns, CLAUDE.md or AGENTS.md design,
  quantitative productivity data, or benchmark comparisons. The post is practitioner
  analysis and philosophical reflection, not a technical tutorial.

## Extracted Claims

### Claim 1: The harness loop — the loop outside the agent loop — is a distinct and newly dominant pattern in agentic engineering, meaningfully different from the familiar agent-internal tool-calling loop

- **Evidence**: Ronacher's direct practitioner observation across multiple teams,
  including Pi users. The structural distinction is his analytical contribution: the
  agent loop (model calls a tool, reads the result, calls another tool, etc.) has been
  familiar for a long time; the harness loop (an external orchestrator decides whether
  the agent is truly done and continues it or restarts it with modified context) is the
  new pattern now "dominating the Twitter discourse."
- **Confidence**: emerging (the structural distinction is accurate and important; the
  "newly dominant" claim is observational but consistent with broader 2026 discourse
  on multi-agent orchestration)
- **Quote**: "There is already an agent loop inside every coding agent. The model calls
  a tool, incorporates the result, calls another tool, reads a file, edits a file, runs
  tests, and eventually produces some answer. That loop is one we have been quite
  familiar with for a long time. The other loop is the harness level loop: the loop
  outside the agent loop."
- **Our assessment**: This is the definitional contribution of the post. The
  agent/harness loop distinction maps cleanly to the architectural level: the agent
  loop is inside the model's context window; the harness loop is outside it, in the
  orchestrating code. Most existing corpus sources discuss agentic behavior at the
  agent-loop level (tool use, context management, AGENTS.md). This post's primary
  analytical contribution is naming and characterizing the meta-level loop. For
  harness engineers: the distinction matters for deciding where to encode stopping
  conditions, where to inject corrective context, and what "done" actually means in
  a system with multiple layers of looping.

### Claim 2: Present-day hands-off harnesses — specifically Claude Code with ultracode/Fable running uninterrupted — produce worse code quality than more human-in-loop approaches from the previous year

- **Evidence**: Ronacher's direct operational experience. He is explicit that this is a
  personal taste claim ("at least for my taste") based on running both paradigms. The
  mechanism he identifies is temporal: ultracode allows the model to work for thirty
  minutes or more without interruption, whereas the previous paradigm was "much more
  human in the loop."
- **Confidence**: anecdotal (single practitioner's preference; explicitly framed as
  personal taste, not objective measurement; the direction of the quality change may not
  generalize)
- **Quote**: "at least for my taste, present-day hands-off harnesses like Claude Code
  with ultracode produce worse code than what we were producing last autumn. That's
  because Claude Code, with Fable for instance will be working uninterrupted on a
  problem for thirty minutes or more, when previously the process would have been much
  more human in the loop."
- **Our assessment**: This is a notable counter-signal on ultracode/auto-mode quality.
  Ronacher is not saying models have regressed in capability; he is saying that the
  harness design (reduced human-in-loop frequency) produces worse outcomes for code he
  cares about. This is potentially the most guide-relevant claim in the post: it
  suggests that the quality cost of hands-off execution is observable and directional
  for a seasoned practitioner, even when using the most capable available model. The
  claim is qualified ("at least for my taste," "code I deeply care about") but the
  mechanism is structurally sound. For guide advice on ultracode/auto-mode: this is
  the strongest practitioner counter-evidence available.

### Claim 3: Models produce code that is too defensive, too complex, and too locally reasoned — avoiding strong invariants, adding fallbacks instead of making bad states impossible

- **Evidence**: Ronacher's repeated first-hand observation from Pi codebase maintenance
  and broader harness experimentation. He names the failure modes specifically: avoid
  strong invariants, add fallbacks, duplicate code, invent bad abstractions, paper over
  design with more machinery.
- **Confidence**: anecdotal (single practitioner; consistent with broadly observed LLM
  code patterns; corroborated by blog-ronacher-pi-oss.md Claims 6-7 and implicitly by
  paper-miller-speed-cost-quality.md's complexity increase measurements)
- **Quote**: "Present-day models tend to produce code that is too defensive, too complex,
  too local in its reasoning. They avoid strong invariants. They add fallbacks instead
  of making bad states impossible. They duplicate code, invent bad abstractions, and
  paper over unclear design with more machinery."
- **Additional quote**: "The right fix is to make the malformed case unrepresentable or
  impossible to write in the first place. Yet even with a lot of manual steering, that
  type of code does not come out of LLMs naturally, and even if the code comes out
  naturally like that, they will still attempt to handle now impossible errors."
- **Our assessment**: This generalizes the specific mechanism from blog-ronacher-pi-oss.md
  (Claims 6-7) from a single codebase to a broader pattern. The pi-oss post described a
  malformed-session-log crash being "fixed" by adding a tolerant reader, then a fallback,
  then a migration, then more debug output, then a test. This post names the abstract
  version of that pattern: models default to making bad states tolerable rather than
  impossible, because they lack visibility into global system invariants and respond to
  local symptoms with local cures. The combination of the two posts provides the specific
  example (pi-oss) and the general principle (this post).

### Claim 4: Models are "mortally terrified of exceptions" — observing local failures and adding local defenses rather than redesigning to eliminate the failure class

- **Evidence**: Ronacher cites Karpathy's observation (linked to
  https://x.com/karpathy/status/1976082963382272334). He applies it specifically to
  systems with important invariants: the model sees a symptom and adds a handler rather
  than asking why the symptom is reachable.
- **Confidence**: emerging (the Karpathy observation is widely cited; the specific
  mechanism — local failure → local defense — is consistent with known LLM code
  generation behavior and corroborated by multiple practitioners)
- **Quote**: "Karpathy mentioned how they are 'mortally terrified of exceptions'. In
  systems with important invariants, especially persisted data formats or core
  infrastructure, the right fix is not 'handle every malformed case.'"
- **Our assessment**: This is the cleanest single-sentence description of the defensive
  code failure mode. "Mortally terrified of exceptions" is memorable and precise: it
  names the correct model behavior (catch exceptions, don't let them propagate) that
  becomes harmful in systems where invariants should prevent the exception from being
  reachable at all. The guide should distinguish the two contexts: exception handling is
  correct at system boundaries; in the interior of well-typed systems, exception handling
  that papers over invariant violations is a quality defect.

### Claim 5: Harness loops amplify the defensive-code pattern — each iteration adds another local defense, making the system less understandable while appearing more robust; less human oversight accelerates the effect

- **Evidence**: Ronacher's structural analysis of how the model's local-defense behavior
  compounds across loop iterations. Each individual defense is "not necessarily wrong in
  isolation" but the accumulation degrades system comprehensibility.
- **Confidence**: anecdotal (structural argument from first-person experience; the
  compounding mechanism is logically sound)
- **Quote**: "When you take that behavior and you put it behind loops, you tend to amplify
  it. If each iteration adds another small defense, the system slowly becomes less
  understandable while appearing more robust. The more hands-off you are, the more that
  happens."
- **Our assessment**: This is the key loop-specific insight that extends the general
  defensive-code critique (Claims 3-4). A single model interaction adds one layer of
  local defense; a loop adds N layers. The system appears more robust because it handles
  more edge cases, but it is actually less maintainable because the edge-case handling
  has accumulated without any global architectural review. The "appearing more robust"
  language is important: the failure is not visible to casual inspection or to automated
  tests, which will pass against the accumulated defenses. The degradation shows up in
  human comprehension time, incident diagnosis difficulty, and refactoring cost.

### Claim 6: Harness loops work well for code porting, performance exploration, security scanning, and research — domains where outputs are either mechanically transformative or don't require longevity

- **Evidence**: Specific named examples: Bun's Zig-to-Rust migration ("reported work"),
  Ronacher's own MiniJinja Go port ("I have used it with success myself"), performance
  benchmarking loops, security scanning. The common property he identifies is that these
  outputs either "do not generate new code, but transform code that already exists, or
  they produce code that intentionally does not have a long shelf life."
- **Confidence**: emerging (multiple concrete examples; consistent with broader practitioner
  reports of loop success in transformation vs. creation tasks)
- **Quote**: "Porting code one of them. There are already impressive examples of large
  automatic porting efforts, including the reported work around moving parts of Bun from
  Zig to Rust. I have used it with success myself to port MiniJinja to Go. Performance
  explorations are another case where this works beautifully. A machine can try
  experiments, benchmark them, discard failures, and keep searching. Security scanning
  fits naturally too and so does almost any type of research"
- **Our assessment**: These examples are the empirical counterweight to the code-quality
  critique. Ronacher is not arguing that loops are universally bad — he identifies a
  structural property that predicts success: transformation (not creation) or
  temporariness (not permanence). The porting case is particularly well-supported: Zig-
  to-Rust translation has a binary correctness signal (tests pass or fail) and produces
  code that can be reviewed against the original. The security scanning case is also
  well-supported: findings are reported, not committed; the loop produces intelligence,
  not production artifacts. For harness engineers: this is the clearest available
  guidance on task selection for loop deployment.

### Claim 7: The success criterion for harness loops is longevity-free artifacts or mechanically verifiable transformation — not the harness's ability to measure a general goal

- **Evidence**: Ronacher's synthesis from the examples in Claim 6. He observes that
  even an LLM judge can serve as the verification mechanism for the porting case —
  binary test suites are sufficient but not necessary; useful signal that "is useful
  enough to drive another iteration" suffices.
- **Confidence**: anecdotal (practitioner synthesis from observed examples; not empirically
  tested against a taxonomy of loop tasks)
- **Quote**: "I believe that loops that produce artifacts without necessity of longevity
  or that create some form of clearly verifiable mechnical translation matters more than
  the general ability of a harness to mechanically measure a goal."
- **Additional quote**: "The harness just needs some signal that lets it continue. It
  does not have to be objective or binary, it just has to be useful enough to drive
  another iteration."
- **Our assessment**: This is an underappreciated design insight for harness engineers.
  The common framing for loop success is "the harness has a good reward signal" — but
  Ronacher is saying something subtler: the longevity requirement and verifiability of
  the output matter more than the precision of the signal. A fuzzy LLM judge that
  routes porting work correctly is sufficient; a precise objective function that drives
  long-lived production code toward local-defense accumulation is insufficient regardless
  of its precision. This reframes harness design from "optimize the reward signal" to
  "choose tasks where longevity and verifiability are favorable."

### Claim 8: Using loops to write lasting production code shifts software from a deterministic machine (understood, auditable) to an organism (diagnosed, treated, but not necessarily comprehended)

- **Evidence**: Ronacher's extended metaphorical analysis. He grounds the "organism"
  metaphor in concrete operational patterns he has already observed: engineers whose
  first response to a production issue is to have a model read the logs, propose root
  causes, and put up a patch — which is then reviewed and sometimes merged by another
  machine without human supervision.
- **Confidence**: anecdotal (metaphorical argument; the concrete operational pattern it
  describes is increasingly observable; Ronacher acknowledges he has "no doubts that for
  some software, that is okay")
- **Quote**: "The metaphor I like to reach for is one of moving from software as a
  deterministic machine to software as an organism."
- **Additional quote**: "We treat it, we monitor it, we stabilize it, but we do not
  necessarily comprehend it."
- **Our assessment**: The organism metaphor captures something the defensive-code critique
  alone doesn't: the shift is not just in code quality but in the entire relationship
  between engineers and systems. Deterministic machines can be understood bottom-up by
  reading the code; organisms are understood top-down by observing symptoms. The guide's
  harness engineering chapter likely frames the shift positively (autonomous agents
  reducing burden); Ronacher's metaphor names what is lost. The "not necessarily
  comprehend it" language is the key: comprehension is not guaranteed, and its absence
  has consequences for onboarding, incident diagnosis, and architectural decision-making.

### Claim 9: Opting out of harness loops is not feasible — security pressure and competitive pressure make adoption inevitable even for practitioners who prefer higher code quality standards

- **Evidence**: Two concrete pressure vectors named. Security: Daniel Stenberg's report
  on curl's "summer of bliss" — a project that does not use AI loops in core development
  but whose maintainers are "overwhelmed by reports, most of which are now AI-generated
  ones." Competitive: small teams out-building larger ones via loop orchestration.
- **Confidence**: emerging (the security pressure argument is grounded in a named, linked
  external example; the competitive pressure argument is observational but widely
  corroborated in 2026 discourse)
- **Quote**: "What's very uncomfortable is that opting out of this fully machine-driven
  future may not be an option."
- **Additional quote**: "If attackers and reporters loop, defenders will eventually need
  to loop too to keep up."
- **Additional quote**: "some teams will out-build others through raw speed. Some projects
  will suddenly move faster because a tiny group figures out how to orchestrate machines
  effectively. Some startups will do with five people what used to require fifty."
- **Our assessment**: This is the argument that saves this post from being a simple
  quality-skeptic take. Ronacher acknowledges the quality problems clearly (Claims 2-5)
  but argues that these quality concerns are insufficient to justify abstention from
  loops, because the alternative is competitive and security disadvantage. The curl
  example is particularly strong: a high-quality OSS project maintained by domain experts
  is already under loop-generated noise pressure, regardless of its own workflow choices.
  This is the "arms race" dynamic documented in blog-ronacher-content-for-contents-sake.md
  (Claim 4) extended to security and competitive software development.

### Claim 10: Codebases produced and maintained by loops create a new dependency — on continued model access — that could become a maintenance crisis if that access is restricted or regressed

- **Evidence**: Ronacher's structural analysis of the dependency risk. He names multiple
  specific failure modes: trade restrictions cutting off most powerful models, cost
  increases becoming unbearable, and the human team "losing the last remaining ability
  to understand the code without using the machine." He notes this is "already happening."
- **Confidence**: anecdotal (structural risk argument from a practitioner who builds AI
  infrastructure; the "already happening" claim is observational without specific examples
  beyond what is described)
- **Quote**: "If a codebase is produced by loops, reviewed by loops, patched by loops,
  and kept alive by loops, what happens when you no longer have access to the same class
  of systems?"
- **Additional quote**: "We may create codebases that are not merely hard to maintain by
  humans, but that assume machine participation as part of their maintenance model."
- **Our assessment**: This extends the access-dependency concern from
  blog-ronacher-ai-nationalism-americans-only.md (Claim 1: nationality-based model access
  restrictions) to the codebase level. That post argues model access can be cut off by
  geopolitical directive; this post argues the same cutoff would now also affect the
  ability to maintain existing code. The two posts together frame a compound risk:
  access restrictions affect not just new development velocity but the ability to
  maintain previously loop-generated codebases. For teams adopting loops: the dependency
  risk is not just "what if we can't build new features" but "what if we can't maintain
  what we've already built."

### Claim 11: Future harnesses need to solve the legibility problem — making loop-generated changes comprehensible to humans — not just scale orchestration further

- **Evidence**: Ronacher's normative argument about what Pi's role should and should not
  be. He explicitly says Pi has "been cautious" and he endorses that caution; he also
  says Pi is a harness and will have to "start doing those experiments" anyway.
- **Confidence**: anecdotal (forward-looking prescription; the legibility requirement is
  identified but no solution is proposed)
- **Quote**: "Either we need to find clever ways to jolt the human back into the loop
  and make the changes of the loops legible long term, or we need to find better ways
  to compose these ever more complex systems."
- **Our assessment**: This is the engineering agenda item that this post leaves open.
  The claim identifies the gap without filling it: legibility of loop-generated changes
  is necessary, and visualizing orchestration is insufficient. "Jolt the human back into
  the loop" names a design requirement — not periodic check-ins but architectural
  mechanisms that require or enable human comprehension of changes as they accumulate.
  For harness engineers: this is the unsolved problem. Current harness design focuses
  on task routing, context injection, and stopping conditions; the legibility of
  accumulated output over multiple loop iterations is not yet a first-class design
  concern.

### Claim 12: In harness-operated loops, the human's role degrades to messenger — the "done" signal is delegated to another machine, removing the human review that gives the agent loop its quality filter

- **Evidence**: Ronacher's first-person reflection on his experience with the two loop
  types. In the agent loop, he "usually steer[s] along the way" and reviews at the
  "done" signal. In the harness loop, the done signal goes to another machine judge.
- **Confidence**: anecdotal (first-person reflection; structurally accurate for fully
  automated harness loops)
- **Quote**: "In the harness operated loop I'm not sure what my role even is. Even the
  'done' signal loses all meanings and just becomes communicated to yet another machine
  that judges. My role is reduced to that of a messenger."
- **Our assessment**: This names the human-role loss precisely. In an agent loop, the
  human is a steering partner: reviewing the "done" answer and redirecting when it's
  wrong. In a harness loop with an LLM judge, the human is a configuration author: they
  write the harness and the judge prompt, but they are not in the critical path of each
  iteration. The quality of the loop depends entirely on the quality of the harness
  design and the judge — there is no opportunity for human course-correction within the
  loop itself. This is the architectural flip that makes harness loop design so
  consequential: mistakes in harness design compound across iterations rather than
  being corrected at review time.

### Claim 13: The question is not whether to adopt harness loops but how to retain human judgment, engineering discipline, and supervisory capacity within an inevitable looping future

- **Evidence**: Ronacher's normative conclusion, grounded in his observation of teams
  already successfully using loops ("astonishingly small teams building at impossible
  speed") despite his personal reservations.
- **Confidence**: anecdotal (normative conclusion from one practitioner; the "inevitable"
  framing is contested but consistent with the competitive and security pressure arguments)
- **Quote**: "I have no doubts that this looping future is going to be our future despite
  the fact that I presently resent it."
- **Additional quote**: "the question is not whether we will loop because clearly we will.
  Maybe the question is that in a future of loops, how do we don't abdicate judgment, how
  we can retain rules of good engineering, how we can ensure that responsible human can
  continue to supervise, how we need to re-think how we architect code to retain sanity
  along the way."
- **Our assessment**: This is the post's strategic conclusion. Ronacher rejects both
  simple adoption (loops everywhere, hands off) and simple rejection (loops bad, avoid
  them). His position: loops are coming regardless of preference; the engineering
  community's job is to figure out how to preserve judgment, quality standards, and
  comprehensibility within the loop paradigm. For the guide: this is the framing that
  makes the entire post useful. It is not a cautionary tale about avoiding loops; it
  is a practitioner's honest assessment of the open problems that must be solved to make
  loops produce acceptable outcomes.

## Concrete Artifacts

### The Boris Cherny framing that opens the post

```
Source: Armin Ronacher quoting Boris Cherny, https://lucumr.pocoo.org/2026/6/23/the-coming-loop/

"I don't prompt Claude anymore. I have loops running that prompt Claude and
figuring out what to do. My job is to write loops."
  — Boris Cherny

Ronacher's framing: "Over the last months I have watched more and more people
build something on top of coding agents that feels meaningfully different from
just using a coding agent."

Context: Boris Cherny is cited as the practitioner articulation of the shift
         from direct prompting to harness loop authorship as the primary job.
```

### Harness loop mechanics (as described in the post)

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/6/23/the-coming-loop/ (2026-06-23)

Pattern description:
  "work is put into a queue of sorts, a machine picks it up, attempts it, stops,
  and then some harness decides whether that was actually the end."

Harness responses when not done:
  - Continues the same session (injects another message)
  - Starts a fresh session with modified context
  - Sends the task to another machine

Key property:
  "The task stays alive beyond the point where the model by itself would
  normally have said: 'I am done.'"
```

### Loop success vs. failure taxonomy (Ronacher's classification)

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/6/23/the-coming-loop/ (2026-06-23)

WHERE LOOPS WORK WELL:
  - Code porting (Bun Zig→Rust migration; MiniJinja Go port)
  - Performance exploration ("try experiments, benchmark them, discard failures")
  - Security scanning
  - Research ("explore a complex problem space and report back without necessarily
    committing lasting code")

  Common property: "they either do not generate new code, but transform code
  that already exists, or they produce code that intentionally does not have
  a long shelf life"

WHERE LOOPS STRUGGLE:
  - Lasting production code
  - Code requiring shared understanding (juniors learning bad patterns)
  - Systems with important invariants (persisted data formats, core infrastructure)

Key design principle:
  "loops that produce artifacts without necessity of longevity or that create
  some form of clearly verifiable mechnical translation matters more than the
  general ability of a harness to mechanically measure a goal"
```

### The curl pressure example (security opt-out impossibility)

```
Source: Armin Ronacher, https://lucumr.pocoo.org/2026/6/23/the-coming-loop/ (2026-06-23)
References: Daniel Stenberg's post https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/

"As far as I know, AI does not play a tremendous role in the core development
of curl today. Yet despite all of this, maintainers are overwhelmed by reports,
most of which are now AI-generated ones."

Ronacher's conclusion:
  "If attackers and reporters loop, defenders will eventually need to loop too
  to keep up. Maybe not to write patches directly, maybe just to triage and
  reproduce and pressure will increase."

Pattern: High-quality non-AI-loop project (curl) experiencing AI-generated noise
         pressure regardless of its own workflow choices.
```

## Cross-References

- **Extends**: `blog-ronacher-pi-oss.md` Claims 6-7 — That post describes the
  defensive-code failure mode at the individual interaction level: a malformed-session-log
  crash leads the clanker to add a tolerant reader, then a fallback, then a migration,
  then more debug output, then a test. Quote from Claim 6 of pi-oss: "If you tell them
  that 'this malformed session log crashes the reader,' the clanker will often add a
  tolerant reader. Then it will add a fallback, then maybe a migration, then more debug
  output, then a test for all of this. None of this is necessarily wrong in isolation,
  but it can be the wrong move for the system." The current post takes that single-
  interaction observation and draws the loop-compounding conclusion (Claim 5 here):
  each iteration adds another small defense, making the system less understandable while
  appearing more robust. Pi-oss is the mechanism at the individual level; this post is
  the mechanism at the loop level.

- **Extends**: `blog-ronacher-pi-oss.md` Claim 7 — Quote from that note: "Almost
  always, the correct fix is not to handle the bad state, but to make the bad state
  impossible." This post (Claims 3-4) generalizes that principle: models default to
  the wrong fix (handling bad states) rather than the right fix (making bad states
  impossible), and this tendency is present even with manual steering. The claim in
  pi-oss is about Pi's session log specifically; this post extends it to the general
  model behavior pattern across all LLM code generation.

- **Extends**: `blog-ronacher-clanker-terminology.md` Claim 2 — Quote from that note:
  "What we actually have is a language model attached to a harness, a prompt, some
  tools, a bit of context, and a boring tool loop." This post's Claim 1 extends that
  definitional framing by distinguishing two levels of loop: the "boring tool loop"
  inside the agent (Claim 2 of clanker-terminology) and the harness loop outside it
  (Claim 1 of this post). The clanker-terminology post defined the agent-level loop
  mechanically; this post adds the meta-level loop as a distinct architectural layer.

- **Extends**: `blog-ronacher-ai-nationalism-americans-only.md` Claims 1 and 4 —
  That post documents nationality-based model access restriction (Claim 1: Anthropic
  blocked Fable and Mythos for foreign nationals) and European structural dependency
  on US AI infrastructure (Claim 4). This post's Claim 10 adds a new dimension to
  that access-dependency concern: codebases produced by loops become dependent on
  continued model access not just for new development but for maintenance of existing
  code. Quote from ai-nationalism Claims 4: "If access to frontier AI becomes a matter
  of American national security policy, Europe is not a peer in that conversation and
  might not even be a market." The current post adds: if your codebase was built by
  loops, that access restriction now also impairs your ability to maintain what you've
  already built.

- **Corroborates**: `blog-ronacher-content-for-contents-sake.md` Claim 4 — That post
  documents the arms-race dynamic in content: low-effort AI generation outcompetes
  quality human responses algorithmically, forcing an escalation. Quote from that Claim 4:
  "Someone has a formed opinion (hopefully) at lunch, and then has a clanker-made post
  3 minutes later. It just does not take that much time to build it." This post (Claim 9)
  documents the same arms-race dynamic in security and competitive development:
  "If attackers and reporters loop, defenders will eventually need to loop too to keep
  up." Both sources identify the same structural pressure: AI lowers generation cost
  faster than it lowers evaluation cost, creating an escalation cycle that even
  quality-focused practitioners cannot opt out of.

- **Extends**: `blog-ronacher-clanker-terminology.md` Claim 3 — That note's
  responsibility attribution formula: "If my coding tool opens a pull request, I opened
  that pull request, not the machine." This post's Claim 12 identifies the specific
  failure mode that harness loops create for that formula: when the "done" signal is
  delegated to another machine judge rather than a human reviewer, the human is no longer
  in the critical path. The responsibility still belongs to the human who designed the
  harness — but the practical ability to exercise that responsibility is attenuated.
  Together, the two posts map the responsibility boundary: humans own the harness design
  (clanker-terminology), but harness loop design can structurally remove humans from
  the exercise of that ownership (this post).

- **Contradicts**: No specific existing source note makes claims that directly oppose
  the core quality-degradation argument. However, this post's Claim 2 (hands-off
  harnesses produce worse code than more human-in-loop approaches) should be checked
  against any corpus source note that reports positive code quality outcomes from fully
  automated harness loops — particularly any source that advocates for ultracode or
  auto-mode as a quality improvement. No contradiction issue filed at this time, as
  no such claim has been verified in existing notes; the Assayer should flag if any
  such source note is confirmed.

- **Novel**:
  - **The harness loop / agent loop architectural distinction named and defined**: No
    existing corpus source note formally distinguishes the loop inside the agent (tool
    calls, file reads, model responses) from the loop outside the agent (harness-level
    orchestration that extends the task beyond the agent's own "done" signal). This is
    the first corpus source to name and define both layers explicitly.
  - **Longevity as the key predictor of loop suitability**: No existing corpus source
    identifies the output's longevity requirement (does this code need to be maintained
    long-term?) as the primary predictor of whether a harness loop will produce
    acceptable quality. Prior corpus sources classify task types by domain or complexity;
    this post's classification by longevity-and-verifiability is a novel and actionable
    frame.
  - **Loop iteration as defensive-code amplifier**: The compound effect of loops on the
    model's defensive-code tendency (each iteration adds another defense; the system
    appears more robust but becomes less comprehensible) is not documented in any prior
    corpus source. The pi-oss note documents the single-interaction pattern; this is the
    first source to describe the loop-iteration compounding effect.
  - **Software-as-organism as a named quality state**: The shift from deterministic
    machine to organism (diagnosed, treated, not comprehended) is not named or analyzed
    in any prior corpus source as a quality state with operational consequences. It
    provides a vocabulary for the failure mode that goes beyond "code complexity
    increased."
  - **Opt-out infeasibility as a named structural condition**: No prior corpus source
    argues that harness loop adoption is structurally forced by competitive and security
    dynamics, regardless of the practitioner's quality preferences. This is the first
    source to make the opt-out-infeasibility argument with named concrete pressure
    vectors (curl security noise, small-team competitive velocity).
  - **Codebase maintenance dependency as a loop risk category**: Loop-produced
    codebases assuming machine participation for maintenance (not just creation) is a
    risk dimension not documented in prior corpus sources. The access-dependency concern
    in ai-nationalism is about development capability; this post adds maintenance
    capability as a distinct and arguably more acute dependency.
  - **Human role as messenger in harness loops**: The specific degradation of the human
    role from "steering partner who reviews done signals" to "messenger who passes
    information between machines" is not named or analyzed in any prior corpus source.
    This is a precise and novel description of what changes about human agency in
    harness-loop architectures.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Three additions warranted:
  1. **Agent loop vs. harness loop distinction** (Claim 1): The chapter should name both
     levels of loop explicitly. Current coverage (inferred from the guide chapter's
     visible CLAUDE.md and harness configuration content) focuses on how to configure
     the agent loop; the harness loop pattern — external orchestration that continues
     the agent beyond its own "done" signal — is architecturally distinct and should be
     introduced as such.
  2. **Task selection by longevity and verifiability** (Claims 6-7): Add a framework
     for deciding when to use harness loops, using Ronacher's longevity-and-verifiability
     criterion: loops are best suited to transformative or temporary work (porting,
     performance exploration, security scanning, research). Lasting production code with
     important invariants is the adversarial case.
  3. **Legibility as a first-class design requirement** (Claim 11): Any section on
     harness design should flag that accumulated loop output creates a legibility debt —
     changes that were never reviewed by a human accumulate without comprehension checkpoints.
     Harness design should address this explicitly, not just optimize stopping conditions.

- **Chapter 03 (Verification)**: The defensive-code amplification claim (Claims 3-5)
  strengthens the case for invariant documentation in AGENTS.md/CLAUDE.md files. If
  the chapter discusses code quality verification, it should note that loop-generated
  code tends toward defensive accumulation rather than strong-invariant design —
  and that the accumulation is not detectable by test suites (which pass against the
  accumulated defenses). Human architectural review and explicit invariant constraints
  in the harness are the mitigation.

- **Chapter 05 (Team Adoption)**: Two additions:
  1. **Opt-out infeasibility** (Claim 9): Teams and team leads advising on AI adoption
     should acknowledge the security and competitive pressure argument. For teams that
     have quality-related reservations about loops: the curl example demonstrates that
     loop-generated noise pressure arrives regardless of the team's own workflow choices.
     The adoption question is not just "should we use loops?" but "how do we use loops
     while preserving quality standards?"
  2. **Dependency risk as a factor in adoption decisions** (Claim 10): Teams adopting
     harness loops should evaluate the maintenance dependency they are creating. Loop-
     produced codebases that assume machine participation for maintenance represent a
     new form of technical debt: not complexity (which is also present) but operational
     dependency on continued model access.

- **Chapter 02 or 05 (Human Role in Loops)**: Claim 12 (human role as messenger)
  warrants a section on human-in-loop design for harness architectures. The chapter
  should distinguish harness designs that preserve human steering ability from those
  that delegate the done-signal entirely to machine judges. For teams comfortable with
  fully automated harnesses: the trade-off is explicit — human judgment is removed from
  the quality-control path, and harness design quality is the only remaining filter.

## Extraction Notes

- Full article text fetched from https://lucumr.pocoo.org/2026/6/23/the-coming-loop/
  via WebFetch. The article is approximately 3,600 words across seven named sections.
  All quotes verified character-for-character against the fetched content.
- The article references two external links followed for context: (1) Boris Cherny's
  quote is attributed by name at the article's opening but not linked to a specific
  source; (2) the Karpathy tweet at https://x.com/karpathy/status/1976082963382272334
  is linked but not fetched (the linked text "mortally terrified of exceptions" is
  presented in the article as Ronacher's characterization of what Karpathy said,
  not a direct quote from the tweet); (3) the Bun Zig-to-Rust migration link points to
  https://ziggit.dev/t/bun-is-being-ported-from-zig-to-rust/15330 (reported external
  work, not Ronacher's); (4) MiniJinja Go port links to Ronacher's own post
  /2026/1/14/minijinja-go-port/ (not fetched; the claim about loop-assisted porting
  success is adequately documented in the article text); (5) Daniel Stenberg's curl
  summer of bliss post at https://daniel.haxx.se/blog/2026/06/15/curl-summer-of-bliss/
  (linked but not fetched; Ronacher's characterization is taken from his summary).
- Three Prospector triage comments are included in the issue, each emphasizing different
  chapter angles (Ch02/Ch04; Ch01/Ch03/Ch04/Ch05/Ch06; loop architecture/harness design/
  code quality/adoption). This extraction covers all three angles. The guide impact
  section maps to actual existing chapter files (guide/02-harness-engineering.md,
  guide/03-verification.md, guide/05-team-adoption.md) based on reading the chapter
  index and guide/02-harness-engineering.md content.
- The Prospector notes this may contradict the guide's framing of loops as progressive
  patterns to adopt. No existing source note was found that specifically advocates for
  hands-off harness loops without qualification. The potential contradiction is with
  the guide's framing rather than with a specific source note's claim. Assayer should
  verify whether guide/02-harness-engineering.md or any source note makes a claim that
  hands-off loop execution improves code quality — if such a claim exists, a
  contradiction issue should be filed.
- Confidence rated anecdotal overall: all claims are first-person observation and
  practitioner synthesis from a single (highly credible) practitioner. The code-quality
  claims are not empirically measured; the opt-out infeasibility claims are structural
  arguments supported by named examples but not quantified. The post is honest about
  its first-person framing ("at least for my taste," "I have not had much success").
- Cross-references all verified: every `Claim N` citation was verified against the
  actual content of the cited source note before writing. No claim numbers were guessed
  or approximated.
- No contradiction issue filed at this time. The Prospector's concern about guide
  framing cannot be turned into a contradiction issue without a specific opposing
  claim in an existing source note. The Assayer should flag if such a note exists.
