---
source_url: https://martinfowler.com/articles/llm-and-dsls.html
source_type: blog-post
title: "DSLs Enable Reliable Use of LLMs"
author: Unmesh Joshi (Distinguished Engineer, Thoughtworks)
date_published: 2026-07-14
date_extracted: 2026-07-15
last_checked: 2026-07-15
status: current
confidence_overall: emerging
issue: "#1881"
---

# DSLs Enable Reliable Use of LLMs

> Joshi argues that Domain-Specific Languages make LLM output reliable by
> constraining the generation space and shipping a deterministic validator,
> demonstrates the pattern through a real internal-DSL framework (Tickloom)
> for testing distributed systems, and frames the LLM's role as splitting into
> two phases — brainstorming partner while the DSL is being designed, then
> natural-language interface once it exists — with the DSL itself, not the
> prompt, becoming the durable source of truth.

## Source Context

- **Type**: blog-post (martinfowler.com, published 14 July 2026)
- **Author credibility**: Unmesh Joshi is a Distinguished Engineer at
  Thoughtworks, based in Pune, India, and the author of *Patterns of
  Distributed Systems*. The article was reviewed by Martin Fowler and Rebecca
  Parsons per the acknowledgments ("I would like to thank Martin Fowler and
  Rebecca Parsons for their valuable feedback and suggestions"), and is
  published directly on martinfowler.com rather than a personal blog or
  Thoughtworks Insights — the highest-visibility outlet in this author's
  ecosystem. Evidence is first-person and grounded in a real, working
  framework (Tickloom) with linked source code, not a hypothetical or a
  survey of others' practices.
- **Scope**: Covers two worked examples — a YAML/PlantUML DSL for generating
  diagram-rich presentations, and an internal Java DSL (Tickloom) for
  constructing and testing distributed algorithms and failure scenarios.
  Argues DSLs and domain abstractions constrain LLM output and enable
  autonomous agent repair loops, and closes with a two-phase model for how
  LLMs should be used relative to a DSL's lifecycle. Does NOT cover: DSL
  design tooling or DSL-building frameworks generically (ANTLR, Xtext, etc.),
  quantitative comparison against non-DSL/general-purpose-language baselines,
  team-scale adoption of this practice, or domains outside distributed
  systems and diagram/presentation generation. All demonstrated code is
  Java/YAML in one author's own framework — the article does not report
  another team or domain replicating the pattern.

## Extracted Claims

### Claim 1: LLMs generate code fast, but need clear boundaries — abstractions and DSLs supply that harness
- **Evidence**: Article's opening thesis, restated in the closing summary.
- **Confidence**: emerging
- **Quote**: "LLMs generate code incredibly fast, but to ensure they generate exactly what is intended, they need clear boundaries. Abstractions and Domain-Specific Languages (DSLs) provide a strong harness that guides LLMs right from the start."
- **Our assessment**: This is the article's framing claim, not yet a measured result — but it is consistent with this corpus's broader convergence that unconstrained LLM output needs an external structure to be reliable (cf. `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 5, `blog-anthropic-multi-agent-coordination-patterns.md` Claim 2). The specific contribution here is naming DSLs/abstractions as the harness mechanism rather than prompting discipline or verifier agents.

### Claim 2: A specification is only a starting hypothesis — the real constraints and edge cases are discovered iteratively through implementation, not specified upfront
- **Evidence**: Author's argument, explicitly citing a prior Fowler-site article that coined the term "Upfront Specification Impossibility."
- **Confidence**: emerging
- **Quote**: "A specification is at best a starting hypothesis: the real constraints, trade-offs, and edge cases are discovered iteratively, as we proceed with the implementation... The point is not that specs are worthless, but that the first one is a hypothesis to be revised, never a finished blueprint."
- **Our assessment**: This sets up the article's central design-phase/generation-phase split (Claim 4): if design can't be specified upfront, then during the design phase the LLM cannot simply generate from a spec — it has to participate in an iterative discovery loop. This is the same "design is discovered, not specified" position argued from a different angle in `blog-maganti-syntaqlite-ai.md` Claim 7 (AI makes design-decision deferral feel consequence-free, but deferring corrodes clear thinking) — Maganti describes the cost of skipping this discovery; Joshi describes the DSL as the artifact that discovery should converge on.

### Claim 3: Code has two intertwined purposes — machine instructions and a conceptual model of the domain — and with LLMs, good abstractions/types/tests/invariants become essential context, not just documentation
- **Evidence**: Author's framing of "What Is Code?", linking to an earlier companion article by the same author (12 May 2026, cited inline in the fetched page).
- **Confidence**: emerging
- **Quote**: "Code has two distinct but intertwined purposes. It is a set of instructions for a machine, and it is also a conceptual model of the problem domain... With LLMs, code acts as essential context: good abstractions, executable behavior, tests, types, and invariants all help constrain the model and make its output more useful."
- **Our assessment**: This reframes abstractions/types/tests from "code quality practices" to "context engineering inputs" — the same abstractions that make code maintainable for humans are the same signal that constrains an LLM's generation space. This is a distinct angle from `blog-anthropic-claude-code-skills-lessons.md` Claim 7 (skills should only add what Claude cannot infer) — here the claim is that the codebase's own domain model is itself a form of context that reduces hallucination, independent of any skill or prompt.

### Claim 4: The LLM plays two distinct roles depending on whether the domain model exists yet — brainstorming partner while the vocabulary is being shaped, natural-language interface once it is established
- **Evidence**: Author's direct statement of the article's organizing principle, stated early and revisited as the closing section.
- **Confidence**: emerging
- **Quote**: "I see LLMs playing two roles. They are a great help while we shape the design and its vocabulary, acting as brainstorming partners to help us explore the design space and discover the right abstractions. Once the vocabulary is established, LLMs work as an excellent natural language interface to it."
- **Our assessment**: This two-role framing is the article's throughline, restated concretely in the "Two phases working with LLMs" section (Claim 12 below) and demonstrated in every worked example. It's a cleaner formulation than "LLM as pair programmer" because it ties the LLM's role directly to whether the abstraction/vocabulary already exists, giving a concrete test for which mode you're in.

### Claim 5: DSLs make LLMs more reliable because they respond well to a few in-context examples — a general-purpose language offers many valid ways to express the same intent, a DSL strips that variation away
- **Evidence**: Author's direct observation, illustrated with PlantUML, Mermaid, Graphviz, SQL, and Kubernetes YAML as examples of narrow, constrained DSLs that LLMs are "remarkably good" at generating from plain English.
- **Confidence**: emerging
- **Quote**: "My observation is that DSLs make LLMs more reliable because they respond so well to a few in-context examples. A general-purpose language like Java offers lots of valid ways to express the same intent. A DSL strips the variation away. Giving the model a few examples is enough to reliably generate the correct syntax."
- **Our assessment**: This is the article's core mechanism claim. It is a plausible and specific causal story (reduced solution-space variation → fewer valid-but-different outputs → few-shot suffices), but it's an author observation, not a controlled comparison against generating equivalent logic in a general-purpose language with the same number of examples. The article itself flags a confound: "frontline models are already heavily exposed to PlantUML or Java fluent interfaces during training, so they aren't starting from scratch" — meaning some of the reliability may be existing training-data exposure to popular DSLs rather than the DSL's constrainedness per se. Joshi explicitly notes this is untested for "smaller, more constrained models... tasked with a truly novel DSL," which is exactly Tickloom's scenario DSL (addressed in Claim 11) and where the claim is best supported in the article.

### Claim 6: For an agent running an autonomous generate-and-check loop, a DSL's built-in deterministic validator (parser, schema, type checker, compiler) lets it repair its own output from domain-level errors, without a human in the loop
- **Evidence**: Author's argument for agentic (not single-shot) use specifically, with the specific mechanism of domain-level vs. stack-trace-level error messages.
- **Confidence**: emerging
- **Quote**: "A DSL almost always ships with a deterministic validator: a parser, a JSON schema, a type checker, or a compiler. The agent can generate a candidate, run it past the validator, and repair it from the error, all without a human in the loop. Crucially, the errors are phrased at the level of the domain — 'you cannot select an action before choosing a client' — rather than as a stack trace buried deep in generated code."
- **Our assessment**: This is the article's strongest and most corpus-relevant claim, because it names the exact mechanism that closes the generator/validator loop described more abstractly in `blog-anthropic-multi-agent-coordination-patterns.md` Claim 2 (generator-verifier requires explicit, formal acceptance criteria) and mirrors `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 5 ("a rule only binds when a deterministic runtime checks it"). Joshi's contribution is specifically that a DSL's grammar/type system supplies that deterministic check for free — no separate verifier agent or rubric needs to be built, because the DSL's own compiler or parser is the validator. Concretely demonstrated in Claim 11's progressive-interface example, where illegal scenarios simply fail to compile.

### Claim 7: The DSL advantage is not one-size-fits-all — it holds only while the DSL stays small and constrained enough for a few in-context examples to convey its usage, and there is a real upfront cost to designing and maintaining the DSL and its semantic model
- **Evidence**: Author's explicit caveat immediately following the core claims (Claims 5-6).
- **Confidence**: emerging
- **Quote**: "It is important to note that this is not a one-size-fits-all solution. The advantage holds while the DSL stays small and constrained enough that a few in-context examples can convey its usage. There is also a real upfront cost in designing and maintaining the language and its semantic model. The payoff is therefore concentrated in well-factored, genuinely constrained DSLs backed by a validator."
- **Our assessment**: This is a load-bearing qualifier that limits the generalizability of Claims 5-6 — the article is explicit that this is a narrow-DSL pattern, not a general "build a DSL for your domain" recommendation. It also implicitly argues against building large or sprawling DSLs specifically for LLM reliability, which pairs directly with `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 7 (ontology programs fail from scope creep — "modeling all of reality before shipping anything").

### Claim 8: A working example — a step-marked PlantUML extension plus a small YAML slide-spec DSL — let an LLM generate diagram-rich presentation content directly usable by a presentation-generation tool
- **Evidence**: Concrete worked example with two full prompts and their generated outputs (PlantUML with `'[step]` markers; YAML slide spec), plus a link to the full spec on GitHub.
- **Confidence**: emerging (single author, single tool, but with runnable, linked code)
- **Quote**: "It's important to note that even if the prompt is saying create a slide YAML, it's not any random YAML spec. Because the tool to generate the powerpoint presentation and the YAML specification understood by the tool is used as a context in the prompt, the LLM is able to generate the correct YAML spec which can be directly used by the tool to generate the powerpoint presentation."
- **Our assessment**: This is the article's simplest and most approachable demonstration of Claims 4-5 together: the LLM first helped shape the step-marker convention and YAML shape (co-designer role), then became a natural-language-to-YAML translator once that convention existed (interface role). Notably, the article states this YAML was processed via its parsed syntax tree directly, i.e., "effectively using the syntax tree itself as my Semantic Model (though this couples the syntax to the execution semantics)" — a caveat the author flags as a simplification relative to the more complex Tickloom case (Claim 9).

### Claim 9: Tickloom's semantic model — a fixed vocabulary of Replica, quorumRequest, countResponseIf, MessageType, Handler, deterministic tick-based scheduling — lets prompts stay at the level of protocol logic rather than distributed-systems plumbing
- **Evidence**: Concrete worked example: a single prompt ("Using the Tickloom Replica abstraction, implement a quorum-based key-value store...") produces a full handler implementation for a last-writer-wins quorum store, shown as compiling Java code with a link to source.
- **Confidence**: emerging
- **Quote**: "Because the framework supplies the vocabulary — Replica, quorumRequest, countResponseIf, MessageType, Handler — a prompt can stay at the level of the protocol rather than the plumbing... The semantic model itself acts as a context. The prompt names concepts that exist as concrete types in the codebase, so the LLM is not inventing a threading model or a networking layer — it is filling in protocol logic against a fixed, well-understood substrate."
- **Our assessment**: This is the article's deepest worked example, and it demonstrates the "verification complexity, not just generation complexity" problem the author names for distributed systems specifically: "the resulting state space created by all possible interleavings across thread scheduling, network delays, process pauses, and clock skew becomes so large that systematically reviewing and validating correctness across all interacting behaviors is nearly impossible... This is the reason we see that Jepsen tests find bugs even in the most battle-tested distributed systems." That framing — that DSLs/semantic models reduce not just what the LLM can generate but what a human reviewer has to verify — is the article's most original point beyond the generic "DSLs constrain output" claim.

### Claim 10: Even without building a DSL, a clean set of named abstractions is a lighter version of the same benefit — a library's types and methods are themselves a vocabulary the model can be grounded in
- **Evidence**: Author's generalization from Tickloom's four seams (Process/Replica, Network, Storage, Clock) to abstractions generally.
- **Confidence**: emerging
- **Quote**: "Tickloom's semantic model is really just four such seams — Process/Replica for compute and message handling, Network for communication, Storage for persistence, and a logical Clock for time — and that decomposition does most of the work with no new syntax at all. This is why abstractions, not just DSLs, pair well with LLMs."
- **Our assessment**: This claim widens the article's applicability considerably — it explicitly says building a full DSL is not required to get much of the benefit; a well-factored library/framework with a small number of named seams already grounds the LLM. This is the article's answer to the "upfront cost" caveat in Claim 7: teams that can't justify a DSL can still get a partial version of the benefit from disciplined abstraction design alone.

### Claim 11: An internal DSL for distributed-system test scenarios — enforced by the host language's compiler via progressive interfaces — makes malformed scenarios fail to compile rather than fail silently at runtime, giving the LLM almost no room to hallucinate
- **Evidence**: Before/after code comparison: the same clock-skew test scenario written directly against the testkit (manual `tick()` loops, futures, factory calls) versus written against the scenario DSL (`QuorumStepBuilder.scenario(...).servers(...).clients(...).steps(...)`), plus a second, more complex non-linearizable-read scenario generated from a natural-language prompt referencing "DDIA §10.6."
- **Confidence**: emerging
- **Quote**: "The grammar is enforced by the type system through progressive interfaces — you cannot declare a step before the topology, or an action before selecting a client — so whole classes of malformed scenarios simply do not compile. Because the DSL is an internal DSL built in Java, the host compiler validates the grammar for free, and a malformed generation comes back as a compile error pinned to exactly the illegal step rather than a runtime surprise... Because the surface is so small — and the space of valid code it can generate is so much smaller than the space of valid Java programs — the LLM has very little room to hallucinate, and a reviewer can read the result as a description of an experiment rather than as code to be audited line by line."
- **Our assessment**: This is the concrete, working instance of Claim 6 (deterministic validator = compiler) and Claim 5 (few in-context examples suffice) combined, using host-language type-system enforcement rather than a separate parser — a genuinely novel DSL not present in LLM training data, which directly addresses the article's own caveat in Claim 5 about untested novel-DSL performance. The reviewability claim ("a reviewer can read the result as a description of an experiment rather than as code to be audited line by line") is the article's clearest statement of DSLs reducing review burden, not just generation error rate.

### Claim 12: A pattern emerges across every example — the LLM's usefulness splits into two phases: brainstorming partner during design (iterative, feedback-driven, human stays in the driver's seat), then dependable natural-language-to-code generator once the abstraction exists
- **Evidence**: Author's explicit synthesis section ("Two phases working with LLMs"), restating and generalizing Claim 4 across all three worked examples.
- **Confidence**: emerging
- **Quote**: "The first phase is designing the abstraction or DSL itself. Here the LLM is best treated as a brainstorming partner rather than a code generator... you propose a structure, try it against a real case, see where it turns out awkward, and feed what you learned back into the next round. The LLM speeds that loop up... but you stay firmly in the driver's seat, because these are exactly the decisions you need to understand and own... The second phase begins once the abstraction or DSL is in place. Now what the LLM does changes: it becomes a natural-language interface to what you have built."
- **Our assessment**: This is the article's central organizing claim, and it's the most directly actionable takeaway for the guide: it gives practitioners an explicit test for which of the two modes to use the LLM in — "does the abstraction/vocabulary already exist?" — rather than a vague "use judgment" recommendation. It is consistent with, and gives DSL-specific mechanics to, the Zone 1/Zone 2/Zone 3 "relativity framework" in `blog-maganti-syntaqlite-ai.md` Claim 12: Joshi's design phase maps to Maganti's Zone 3 (outcomes unclear, AI as brainstorming partner only, human owns the decision), and Joshi's generation phase maps to Maganti's Zone 1 (deeply known territory, AI excels, reviewable quickly).

### Claim 13: A well-designed DSL shifts the durable artifact from the prompt to the DSL/semantic model itself — the generated program, not the prompt that produced it, becomes what humans read and maintain
- **Evidence**: Author's closing argument, explicitly contrasted against "a growing trend of treating prompts as the primary source of truth."
- **Confidence**: emerging
- **Quote**: "There is a growing trend of treating prompts as the primary source of truth. A well-designed DSL fundamentally changes this dynamic... If an LLM generates a Tickloom failure scenario from a natural language request, the resulting scenario is already expressed in the vocabulary of the domain. If the scenario needs to change next month, there is no need to recover the original prompt and regenerate everything. The DSL has enough context for LLM to know the intent and work with it. The enduring asset is not the prompt, but the DSL and the semantic model."
- **Our assessment**: This directly challenges the "prompt as source of truth" position implicitly held by pure prompt-to-artifact regeneration workflows, and is the article's most guide-relevant closing claim: it argues DSL output is dense and domain-expressive enough to be a legitimate maintenance artifact on its own, obviating the need to preserve or re-run the generating prompt. This is a distinct, narrower claim than the general "code as documentation" argument — it specifically requires the DSL to be "dense, expressive, and largely free of incidental boilerplate," a property not all generated artifacts have.

## Concrete Artifacts

```
PlantUML with step markers (generated from a single natural-language prompt)
Source: martinfowler.com/articles/llm-and-dsls.html, Unmesh Joshi, 2026-07-14

@startuml
actor Alice
box "Cluster" #lightblue
participant athens
participant byzantium
participant cyrene
end box
'[step]
Alice -> athens: "title", "After Dawn"
'[step]
athens -> athens: save()
note right of athens
state:
title: After Dawn
end note
'[step]
athens -[#red]x byzantium: "title", "After Dawn"
'[step]
athens -> cyrene: "title", "After Dawn"
note right of cyrene
state:
title: After Dawn
end note
'[step]
athens -> athens: isQuorumReached()
'[step]
athens --> Alice: Success
@enduml
```

```
YAML slide-spec DSL output (generated from "Create a slide YAML referring to
the diagram 'quorum-write' with a title 'Quorum Write Example'")
Source: martinfowler.com/articles/llm-and-dsls.html, Unmesh Joshi, 2026-07-14

- slide:
  title: "Quorum Write Example"
  diagram: "quorum-write"
```

```
Tickloom scenario DSL — before (raw testkit) vs. after (scenario DSL)
Source: martinfowler.com/articles/llm-and-dsls.html, Unmesh Joshi, 2026-07-14

# BEFORE: same clock-skew scenario written directly against the testkit
Cluster cluster = new Cluster()
    .withProcessIds(Arrays.asList(ATHENS, BYZANTIUM, CYRENE))
    .useSimulatedNetwork()
    .build(QuorumReplica::new);
cluster.start();
try {
    cluster.tickUntil(cluster::areAllNodesInitialized);
    cluster.setTimeForProcess(ATHENS, 1000L);
    cluster.setTimeForProcess(BYZANTIUM, 2000L);
    QuorumReplicaClient alice = cluster.newClientConnectedTo(ALICE, ATHENS, QuorumReplicaClient::new);
    QuorumReplicaClient bob = cluster.newClientConnectedTo(BOB, BYZANTIUM, QuorumReplicaClient::new);
    QuorumReplicaClient reader = cluster.newClientConnectedTo(READER, ATHENS, QuorumReplicaClient::new);
    TickCompletableFuture<SetResponse> bobWrite = bob.set(KEY.getBytes(StandardCharsets.UTF_8), "B".getBytes(StandardCharsets.UTF_8));
    cluster.tickUntilComplete(bobWrite);
    TickCompletableFuture<SetResponse> aliceWrite = alice.set(KEY.getBytes(StandardCharsets.UTF_8), "A".getBytes(StandardCharsets.UTF_8));
    cluster.tickUntilComplete(aliceWrite);
    TickCompletableFuture<GetResponse> read = reader.get(KEY.getBytes(StandardCharsets.UTF_8));
    cluster.tickUntilComplete(read);
    assertEquals("B", new String(read.getResult().value(), StandardCharsets.UTF_8));
} finally {
    cluster.close();
}

# AFTER: the same scenario expressed in the scenario DSL
Scenario<QuorumReplicaClient> scenario =
    QuorumStepBuilder.scenario("LWW lost update via server clock skew")
        .servers(ATHENS, BYZANTIUM, CYRENE)
        .clients(ALICE, BOB, READER)
        .client(ALICE).connectedTo(ATHENS)
        .client(BOB).connectedTo(BYZANTIUM)
        .given(g -> g.serverTimeAt(ATHENS, 1_000L)
                     .serverTimeAt(BYZANTIUM, 2_000L))
        .steps(s -> {
            s.client(BOB).writes(KEY, "B").expectSuccess();
            s.client(ALICE).writes(KEY, "A").expectSuccess();
            s.client(READER).reads(KEY)
                .expectResponse(v -> "B".equals(v));
        });
```

```
Tickloom scenario DSL — generated from a natural-language DDIA §10.6 prompt
Source: martinfowler.com/articles/llm-and-dsls.html, Unmesh Joshi, 2026-07-14

Scenario<QuorumReplicaClient> scenario =
    QuorumStepBuilder.scenario("Non-linearizable quorum read")
        .servers(ATHENS, BYZANTIUM, CYRENE)
        .clients(WRITER, ALICE, BOB)
        .client(WRITER).connectedTo(ATHENS)
        .client(ALICE).connectedTo(BYZANTIUM)
        .client(BOB).connectedTo(BYZANTIUM)
        .steps(s -> {
            s.client(WRITER).writes(KEY, VOLD).expectSuccess();
            s.client(WRITER).writes(KEY, VNEW)
                .whileClusterEvent(delay(QuorumMessageTypes.INTERNAL_SET_REQUEST)
                    .from(ATHENS).to(BYZANTIUM, CYRENE).byTicks(100))
                .expectSuccess();
            s.client(ALICE).reads(KEY)
                .whileClusterEvent(partition(BYZANTIUM).from(CYRENE))
                .expectResponse(v -> VNEW.equals(v));
            s.client(BOB).reads(KEY)
                .whileClusterEvent(reconnect(BYZANTIUM))
                .whileClusterEvent(partition(BYZANTIUM).from(ATHENS))
                .expectResponse(v -> VOLD.equals(v));
        });
ScenarioResult result = scenario.run();
```

## Cross-References

- **Corroborates**:
  - `blog-thoughtworks-asthagiri-ontology-failure-modes.md` Claim 5 ("a rule
    only binds when a deterministic runtime checks it and respects the
    answer and when you can show the check actually happened"): Joshi's
    Claim 6 is the same principle applied to DSL grammars instead of
    ontology-encoded rules — a DSL's parser/type checker/compiler is the
    enforcement layer, not the DSL's existence alone. Both sources
    independently converge on "structure without enforcement is not a
    guardrail."
  - `blog-anthropic-multi-agent-coordination-patterns.md` Claim 2
    (generator-verifier requires explicit, formal acceptance criteria; vague
    criteria produce the "early victory problem"): Joshi's Claim 6 supplies
    a concrete instance where the verifier is not a separate LLM-judged
    rubric but the DSL's own compiler/parser — the criteria are inherently
    formal because they're a grammar, sidestepping the "early victory
    problem" entirely for the subset of correctness the grammar can express.
  - `blog-maganti-syntaqlite-ai.md` Claim 12 (the three-zone "relativity
    framework" — deeply known / describable-unknown / outcomes-unclear
    territory) and Claim 13 (the implementation/design asymmetry): Joshi's
    two-phase model (Claim 12 here) is a domain-specific instance of the
    same distinction — the DSL-design phase is Maganti's Zone 3 (human owns
    the decision, AI brainstorms), the DSL-generation phase is Maganti's
    Zone 1 (AI excels, fast review). Joshi adds the DSL-specific mechanism
    (constrained grammar + compiler feedback) that explains *why* the
    generation phase reaches Zone 1 reliability once the abstraction exists.
  - `blog-anthropic-claude-code-skills-lessons.md` Claim 7 (skills should
    only add information Claude cannot infer — not restate what it already
    knows): Joshi's Claim 9 (the semantic model itself acts as context,
    grounding the prompt in concrete types) is a structural analog —
    instead of a skill file supplying non-obvious information, the codebase's
    own domain vocabulary supplies it, with the added benefit of compiler
    enforcement that a skill's prose cannot provide.

- **Contradicts**: None identified. No existing corpus note argues DSLs or
  constrained abstractions are unhelpful for LLM reliability, or that prompts
  should be the durable source of truth over generated artifacts — Claim 13's
  position (the DSL, not the prompt, is the enduring asset) is novel to the
  corpus rather than opposed to an existing claim.

- **Extends**:
  - `blog-thoughtworks-asthagiri-ontology-failure-modes.md`: that note
    covers ontologies/knowledge graphs as semantic infrastructure for
    retrieval and guardrails at the data layer; this article extends the
    same "constrained semantic structure improves agent reliability"
    argument to the code-generation layer specifically, with a working
    compiler-enforced example (Claim 11) that the ontology note does not
    provide (it has no code, per that note's Extraction Notes).
  - `blog-anthropic-harness-long-running.md` (generator/evaluator
    architecture, sprint contracts with explicit criteria): Joshi's Claim 6
    describes a lighter-weight version of the same generator/evaluator
    split — the DSL's own compiler substitutes for a dedicated evaluator
    agent when the correctness property is expressible as a grammar
    constraint, avoiding the cost of running a second LLM evaluation pass
    for that subset of checks.

- **Novel**:
  - The specific mechanism claim that a DSL's built-in deterministic
    validator (parser/schema/type-checker/compiler) enables autonomous
    agent repair loops with domain-level (not stack-trace-level) error
    messages (Claim 6) — no prior corpus note names this exact mechanism.
  - The two-phase LLM-role model tied explicitly to whether the DSL/
    abstraction already exists (Claim 4, Claim 12) as a concrete test for
    "when to let the LLM design vs. when to let it generate" — more
    specific than the general "LLM as brainstorming partner" framing
    elsewhere in the corpus.
  - The claim that DSL/semantic-model quality reduces *verification*
    complexity, not just generation complexity, illustrated via the
    Jepsen-bugs-in-battle-tested-systems framing for distributed systems
    (Claim 9) — a distinct angle from prior corpus claims about DSLs or
    constrained generation, which focus on reducing hallucination rate
    rather than reviewer cognitive load.
  - The claim that a DSL becomes the durable source of truth in place of
    the prompt (Claim 13) is a novel, explicit counter-position to
    "prompt as source of truth" workflows not previously argued against in
    this corpus.
  - The "four seams" generalization (Claim 10) — that a small number of
    named abstractions (not a full DSL) already captures most of the
    benefit — is a novel lower-cost variant of the DSL pattern.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add a "DSLs and constrained
  abstractions as a harness mechanism" subsection, using Claim 6 (compiler/
  parser as free deterministic validator) as the anchor. This complements
  the existing generator-verifier taxonomy (`blog-anthropic-multi-agent-
  coordination-patterns.md`) by naming a cheaper alternative to a dedicated
  evaluator agent: when correctness is expressible as a grammar, use the
  DSL/type system as the verifier instead of a second LLM call. Cite Claim
  7's caveat (upfront cost, narrow applicability) so this isn't presented as
  a universal recommendation.

- **Chapter 02 (Harness Engineering)**: Add Claim 4/Claim 12's two-phase
  model (LLM as brainstorming partner during design, natural-language
  interface once the DSL/abstraction exists) as an explicit decision
  heuristic alongside Maganti's relativity framework — same underlying
  distinction, DSL-specific mechanics. Practitioners building a new
  abstraction should expect to spend the design phase in the driver's seat
  (per Claim 12's "you stay firmly in the driver's seat") and only delegate
  generation once the vocabulary stabilizes.

- **Chapter 03 (Verification)**: Add Claim 9's "verification complexity, not
  just generation complexity" framing as a distinct verification argument:
  a well-factored semantic model or DSL reduces not only what the LLM can
  generate incorrectly but what a human reviewer has to check by hand. The
  Jepsen citation (bugs surviving in battle-tested distributed systems even
  with careful review) is a concrete, citable illustration of why review
  alone doesn't scale for combinatorially large interleaving spaces, and why
  constraining the generation surface (Claim 11's progressive interfaces)
  is a verification strategy, not just a generation-quality one.

- **Chapter 04 (Context Engineering)**: Add Claim 10 (a small number of named
  abstractions/seams grounds the LLM almost as well as a full DSL, with no
  new syntax) as a lower-cost entry point for teams that can't justify
  building a DSL. This gives Ch04 a graduated recommendation: start with
  clean, named abstractions; only invest in a full DSL when the domain
  genuinely needs its own constrained syntax (per Claim 7's cost caveat).

- **Chapter 04 (Context Engineering)**: Add Claim 13 (the DSL, not the
  prompt, should be the durable source of truth for generated artifacts) as
  a counter-position to workflows that treat prompts as the thing to
  version and re-run. Frame as: if your generated artifact is dense and
  domain-expressive (a DSL output), maintain the artifact directly; if it's
  boilerplate-heavy generated code, the prompt-as-source-of-truth pattern
  may still be more practical — this is a conditioning variable, not a
  universal rule.

## Extraction Notes

- The article was fetched via `curl` and converted from raw HTML to plain
  text locally (WebFetch's small-model summarization pass returned only a
  high-level paraphrase and did not preserve verbatim wording), then read in
  full. All quotes in this note were copied character-for-character from
  that extracted plain text against the source's paragraph structure, not
  reconstructed from a summary.
- No sub-pages were followed. The article links to two external resources
  cited by name but not fetched as separate sources for this note: the
  full YAML presentation-spec repo ("The full YAML spec can be viewed at
  this Github repo") and the Tickloom source snippets (marked "source" at
  three points in the article). These are code artifacts illustrating
  claims already extracted directly from the article's inline code blocks,
  not additional textual claims, so they were not treated as required
  sub-pages under MINER.md §1. A future mining pass could fetch the
  Tickloom GitHub repo directly if deeper extraction of the framework's
  design rationale (e.g., commit history, README, or test suite) is wanted.
  It also links to an earlier companion article by the same author (12 May
  2026, on code as a conceptual model with LLMs) and to an unnamed prior
  Fowler-site article introducing "Upfront Specification Impossibility" —
  neither is yet a separate note in this corpus; either could be a
  worthwhile future source submission given how load-bearing they are to
  this article's opening argument (Claim 2, Claim 3).
- Confidence is rated `emerging` overall: the author is highly credible
  (Thoughtworks Distinguished Engineer, published directly on
  martinfowler.com, reviewed by Fowler and Parsons) and every claim is
  grounded in real, linked, compiling code rather than a hypothetical — but
  every worked example comes from a single author's own framework in a
  single domain (distributed systems testing, plus one presentation-
  generation tool). The article itself flags an open question (whether the
  pattern holds for smaller models on truly novel DSLs) that it only
  partially answers via the Tickloom scenario DSL. No independent
  replication by another practitioner or team is present in this source.
- No contradiction with existing corpus notes was found; see
  Cross-References → Contradicts. No contradiction issue was filed.
