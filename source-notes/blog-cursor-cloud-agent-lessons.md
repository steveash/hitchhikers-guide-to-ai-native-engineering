---
source_url: https://cursor.com/blog/cloud-agent-lessons
source_type: blog-post
title: "What we've learned building cloud agents"
author: Josh Ma (Cursor)
date_published: 2026-05-21
date_extracted: 2026-05-22
last_checked: 2026-05-22
status: current
confidence_overall: emerging
issue: "#849"
---

# What we've learned building cloud agents (Josh Ma, Cursor)

> Cursor's first-party operational synthesis of five lessons from building and scaling cloud agents in production — covering environment quality as the primary determinant of output quality, Temporal-based durable execution reaching 50M+ actions/day, a three-component decoupling pattern (agent loop / machine state / conversation state), the progressive shift from deterministic harness logic to agent-controlled tools, and a forward-looking self-healing agent environment vision — all grounded by the metric that 40%+ of Cursor's internal PRs now originate from cloud agents.

## Source Context

- **Type**: blog-post (Cursor engineering blog, published May 21, 2026; single author, Josh Ma; approximately 1,000–1,500 words). This is a synthesis post by a Cursor engineer drawing on lessons from operating cloud agents at production scale — part retrospective, part architectural guidance.
- **Author credibility**: Josh Ma writes from direct operational experience at Cursor. The post does not identify his specific role, but the technical specificity (Temporal primitives named, concrete reliability numbers, named architectural patterns) indicates genuine engineering involvement rather than marketing prose. Cursor has tens of thousands of active developer users and demonstrably runs cloud agent workflows at production scale; their operational observations carry substantial weight. Treat as emerging: directionally reliable for the named patterns, but not independently audited.
- **Scope**: Covers five lessons mapped to five article sections: (1) the development environment as the product, (2) durable execution for long-running agents, (3) decoupling components for flexible deployment, (4) progressively handing responsibility to agents, (5) self-healing agent environments. Does NOT cover: specific model identities, cost structure, security boundary details, failure rates, agent quality benchmarks beyond the PR-origin metric, or the full implementation of the Temporal agent loop.

## Extracted Claims

### Claim 1: The single biggest factor in cloud agent output quality is the development environment — poor environments cause subtle degradation, not crashes

- **Evidence**: First-party operational observation from Cursor engineers. The post contrasts local agents (which inherit a developer's environment) with cloud agents (which must reconstruct the full environment from scratch).
- **Confidence**: emerging (first-party practitioner observation; mechanism is architecturally sound; consistent with what would be expected when agents lack the tools needed to execute or verify their work)
- **Quote**: "The single biggest factor in cloud agent output quality is ensuring it has a full development environment, like a developer has."
- **Our assessment**: The failure mode described is insidious: "Instead of a crash or an error message, often the only indication is a subtle degradation in output quality." This is harder to detect than a hard failure — the agent appears to complete the task but produces lower-quality results. This places environment quality squarely in the monitoring and harness-design domains, not just DevOps infrastructure. The implication for practitioners: cloud agent quality cannot be evaluated without first verifying environment completeness; benchmarking on incomplete environments will underestimate what the agent can do.

### Claim 2: As models improve, environment setup has become the determining factor — it is now the bottleneck, not model capability

- **Evidence**: First-party observation from operational evolution of Cursor's cloud agent product.
- **Confidence**: emerging (stated operational insight; consistent with the trajectory described in blog-cursor-continual-harness-improvement.md Claim 12, where static harness components were removed as models improved)
- **Quote**: "As they've gotten smarter, the environment setup has become the determining factor in whether they execute at their full potential."
- **Our assessment**: This is a significant reframing of the improvement frontier. The historical framing was: better models → better output. This source argues the frontier has shifted: models are now sufficient for many tasks, and the limiting factor is whether the environment provides what models need to act on their reasoning. This has direct consequences for how teams allocate engineering effort — investing in environment quality rather than waiting for model improvements.

### Claim 3: An initial work-stealing architecture for cloud agents achieved only one 9 of reliability; migration to Temporal pushed reliability past two 9s

- **Evidence**: Explicit comparison of pre- and post-Temporal reliability with named numbers.
- **Confidence**: emerging (first-party claim; specific reliability numbers are stated; no external audit)
- **Quote**: "It transplanted what works locally to a server and it was a fragile setup—our early beta of cloud agents often operated at one 9 of reliability."
- **Our assessment**: The work-stealing architecture is the "naive" cloud migration: take the local agent loop and run it on a server. One 9 (90% uptime) is production-unusable for a developer tool. Moving past two 9s (99%+) via Temporal was the turning point that made cloud agents viable. The lesson is architectural: local agent loops make implicit assumptions about environment stability that fail in cloud contexts, and reliable cloud execution requires dedicated durable execution infrastructure.

### Claim 4: Temporal enables cloud agent loops to survive inference blips, pod hibernation, and multi-day or multi-week runs, and now handles 50M+ actions/day across 7M+ workflows

- **Evidence**: Named production metrics with a named infrastructure component (Temporal) and description of what it enables.
- **Confidence**: emerging (first-party claim with specific metrics; Temporal is a known production-grade durable execution system; the scale figures are plausible given Cursor's user base)
- **Quote**: "Our current agent loop on Temporal can survive blips in inference reliability, pod hibernation and resumption, and runs that stretch across days or even weeks." And: "Temporal handles more than 50 million actions per day across more than 7 million unique workflows."
- **Our assessment**: The Temporal architecture is the concrete infrastructure answer to "how do you run cloud agents reliably?" The three survival properties (inference blips, pod hibernation, multi-day runs) map to three distinct failure modes that a naive loop cannot handle. The 50M actions/day scale metric establishes that this is not a prototype — it is a production system at substantial scale. For practitioners: Temporal (or equivalent durable execution systems) is the appropriate infrastructure primitive for production cloud agent loops; naive in-process loops will not meet production reliability requirements.

### Claim 5: More than 40% of Cursor's internal PRs originate from cloud agents

- **Evidence**: First-party metric on Cursor's own engineering organization.
- **Confidence**: anecdotal (self-reported; no external audit; specific denominator unknown)
- **Quote**: "Internally, more than 40% of our PRs come from cloud agents, and growing."
- **Our assessment**: This is the most concrete organizational-scale adoption metric in the corpus for cloud agent production use. At 40%+ PR origin, cloud agents have crossed from "experiment" to "primary workflow" within Cursor's own team — the team that builds the product. The "and growing" qualifier suggests this has not peaked. For the guide: this is practitioner evidence that cloud agents can reach majority-contribution at engineering team scale, not just as occasional assistance.

### Claim 6: Keeping the agent loop, machine state, and conversation state as decoupled components enables flexible deployment patterns

- **Evidence**: First-party architectural principle with concrete deployment modes enumerated.
- **Confidence**: emerging (named architectural pattern; deployment mode examples are specific and concrete)
- **Quote**: "We've found it valuable to keep the agent loop, the machine state, and the conversation state as decoupled components." And: "An agent might run on one machine, spawn async subagents across several, or start locally then delegate work to the cloud."
- **Our assessment**: The three-component decoupling is the key architectural insight for cloud agent infrastructure. Without it, all three are coupled: the agent loop lives in the process, machine state is local storage, and conversation state lives in memory. Decoupling them into separate logical components enables each to be managed independently: the Temporal workflow (agent loop) can survive infrastructure changes; the VM (machine state) can be replaced or scaled without restarting the agent; conversation state can stream to web/desktop clients. The three deployment modes (single machine, multi-machine subagents, local-then-cloud delegation) are only possible because of this decoupling.

### Claim 7: Separating conversation storage and streaming from the core agent workflow enables pod lifecycle independence and streaming to multiple clients

- **Evidence**: Specific description of what conversation state decoupling enables.
- **Confidence**: emerging (described architectural outcome; mechanism is technically coherent)
- **Quote**: "We separated the storage and streaming layer from the core agent workflow" and created "an efficient append-only storage mechanism that streams conversation updates out to web and desktop clients."
- **Our assessment**: The append-only storage mechanism for conversation state is the concrete implementation of component 3 in the decoupling pattern. It solves two problems: (1) pod lifecycle independence — the agent workflow does not lose conversation state when the pod hosting it restarts; (2) client streaming — the conversation can be observed in real time from web or desktop clients without coupling those clients to the agent's execution environment. This is a pattern well-established in distributed systems (event sourcing) being applied to agent infrastructure.

### Claim 8: Moving from "eternal" agent workflows to shorter task-scoped workflows improves version manageability

- **Evidence**: Explicit architectural evolution described with a named motivation.
- **Confidence**: emerging (described evolution with a specific rationale)
- **Quote**: "We've moved from 'eternal' agent workflows to multiple shorter ones that exit after completing a single task, which makes version upgrades easier."
- **Our assessment**: "Eternal" workflows — agent loops that run indefinitely — create a versioning problem: you cannot upgrade the agent harness code without stopping the running workflow. Shorter workflows that exit after task completion create natural upgrade windows. This is the cloud agent equivalent of the "stateless service" principle in distributed systems: stateless short-lived workers can be upgraded by simply deploying new workers; stateful long-running processes cannot. The architectural recommendation is to avoid eternal agent loops in favor of task-scoped workflows that create upgrade windows.

### Claim 9: Building a cloud agent harness requires constantly reevaluating how much behavior is deterministic harness logic vs. agent-controlled

- **Evidence**: First-party framing of the harness engineering challenge.
- **Confidence**: emerging (philosophical principle stated with operational basis)
- **Quote**: "Building a cloud agent harness means constantly reevaluating how much behavior is deterministic and how much gets handed to the agent."
- **Our assessment**: This is the meta-principle of cloud agent harness design. It rejects a fixed architecture in favor of treating the harness as a continuously evolving boundary between deterministic infrastructure and agent reasoning. As models improve, behavior that previously required deterministic logic can be delegated to the agent. The key insight: "The harness isn't going away so much as what it contains is changing" — the harness structure persists, but its content shifts progressively toward infrastructure and away from embedded logic.

### Claim 10: As models improved, multi-repo setup logic moved from hardcoded harness behavior to agent-controlled via exposed tools

- **Evidence**: Concrete example of the harness-to-agent shift with before/after description.
- **Confidence**: anecdotal (single named example; illustrative of a broader principle)
- **Quote**: "A year ago, multi-repo setups required hardcoded harness behavior. Now, we can give the agent the repo layout, expose tools for branches and PRs, and let it decide how to do the work."
- **Our assessment**: This is the most concrete example in the source of the harness evolution principle. The pattern is: (1) identify behavior that is currently hardcoded in the harness; (2) expose the relevant information and capabilities as tools; (3) let the agent reason about how to use them. The multi-repo case is illustrative but the pattern generalizes: any hardcoded harness behavior that encodes "what the model cannot figure out on its own" is a candidate for migration as models improve. This is the operational analogue of the principle stated abstractly in blog-anthropic-harness-long-running.md Claim 9.

### Claim 11: The vision for cloud agents is self-healing: agents that detect environment problems and act to resolve them without human intervention

- **Evidence**: Explicit forward-looking statement about the direction of cloud agent capability.
- **Confidence**: anecdotal (stated aspiration, not current capability; referenced as in-progress research)
- **Quote**: "We want cloud agents to be able to report when secrets are missing, network access is blocked, or when their environment is otherwise preventing them from making progress, and to then be able to act in a self-healing way."
- **Our assessment**: Self-healing agents are the logical completion of the environment quality story: if poor environment quality is the primary quality determinant, and agents can detect and fix their own environment deficiencies, then environment quality becomes a solved problem at the agent layer rather than a managed problem at the infrastructure layer. The "autoinstall" work (blog-cursor-autoinstall-bootstrapping.md) is the research step in this direction — currently applied to training environments, with the implication of generalizing to any agent environment. This vision is forward-looking, not a current production capability.

### Claim 12: "Autoinstall" is Cursor's named research path toward self-healing agent environments

- **Evidence**: Cross-reference to a separate Cursor research blog post.
- **Confidence**: anecdotal (pointer to external work; the autoinstall mechanism is described in a companion research blog, not in detail here)
- **Quote**: "In a recent research blog we talked about one path for achieving this which we call 'autoinstall.'"
- **Our assessment**: The autoinstall reference connects this synthesis post to the concrete mechanism described in blog-cursor-autoinstall-bootstrapping.md (two-stage goal-setter/executor pattern for bootstrapping development environments). The cloud-agent-lessons post positions autoinstall as one step toward the broader self-healing vision. This is an explicit cross-post link that should be tracked in the guide's coverage of environment bootstrapping.

## Concrete Artifacts

### Cloud Agent Architecture: Five Lessons Summary

```
"What we've learned building cloud agents" — Josh Ma, Cursor (May 21, 2026)
Source: https://cursor.com/blog/cloud-agent-lessons

Five lessons from production cloud agents:

1. The development environment is the product
   - "The single biggest factor in cloud agent output quality is ensuring
     it has a full development environment, like a developer has."
   - Poor environment → subtle degradation (not crashes or errors)
   - "the environment setup has become the determining factor in whether
     they execute at their full potential"

2. Long-running agents need durable execution
   - Work-stealing architecture: fragile, "one 9 of reliability"
   - Temporal: past two 9s; survives inference blips, pod hibernation,
     multi-day/multi-week runs
   - "Temporal handles more than 50 million actions per day across more
     than 7 million unique workflows"
   - "Internally, more than 40% of our PRs come from cloud agents, and growing."

3. Decoupling agents and machines from conversation state
   Component 1: Agent loop (Temporal workflow)
   Component 2: Machine state (VM / pod)
   Component 3: Conversation state (append-only storage + streaming layer)
   - "An agent might run on one machine, spawn async subagents across several,
     or start locally then delegate work to the cloud."
   - Evolved from "eternal" workflows to shorter task-scoped ones (easier versioning)

4. Knowing how to get out of the way
   - "Building a cloud agent harness means constantly reevaluating how much
     behavior is deterministic and how much gets handed to the agent."
   - "As models got smarter, we started moving logic out of the harness and
     into tools the agent controls."
   - Multi-repo example: hardcoded → agent-controlled via exposed tools
   - "The harness isn't going away so much as what it contains is changing"

5. Self-healing agent environments
   - Vision: "We want cloud agents to be able to report when secrets are
     missing, network access is blocked, or when their environment is
     otherwise preventing them from making progress, and to then be able
     to act in a self-healing way."
   - Current step: "autoinstall" (see blog-cursor-autoinstall-bootstrapping.md)
```

### Reliability Evolution

```
# Cursor cloud agent reliability evolution (May 2026)
# Source: "What we've learned building cloud agents," Josh Ma, Cursor

Phase 1: Work-stealing architecture
  Description: "transplanted what works locally to a server"
  Reliability: "often operated at one 9" (~90% uptime)
  Assessment: "a fragile setup"

Phase 2: Temporal-based durable execution
  Reliability: "past two 9s" (>99% uptime)
  Capabilities added:
    - Survives "blips in inference reliability"
    - Survives "pod hibernation and resumption"
    - Supports "runs that stretch across days or even weeks"
  Scale (as of May 2026):
    - 50+ million actions per day
    - 7+ million unique workflows
    - 40%+ of Cursor's internal PRs from cloud agents
```

### Three-Component Decoupling Pattern

```
# Cloud agent component decoupling pattern (Cursor, May 2026)
# Source: "What we've learned building cloud agents," Josh Ma, Cursor

COMPONENT 1: Agent Loop (Temporal workflow)
  - Orchestrates the agent's reasoning and tool call cycle
  - Lives in Temporal; survives infrastructure changes
  - Evolved from "eternal" → task-scoped short workflows
    (reason: "makes version upgrades easier")

COMPONENT 2: Machine State (VM / pod)
  - The execution environment (terminal, files, processes)
  - Managed independently from agent loop lifecycle
  - Enables: pod lifecycle independence, different pod types
    "we can manage pod lifecycles independently and run agents
     across different kinds of pods"

COMPONENT 3: Conversation State (append-only storage + streaming)
  - "We separated the storage and streaming layer from the core agent workflow"
  - "an efficient append-only storage mechanism that streams conversation
     updates out to web and desktop clients"
  - Enables streaming to web/desktop without coupling to execution

ENABLED DEPLOYMENT MODES:
  "An agent might run on one machine, spawn async subagents across several,
   or start locally then delegate work to the cloud."
```

### Harness-to-Agent Shift Pattern

```
# Harness-to-agent shift pattern (Cursor, May 2026)
# Source: "What we've learned building cloud agents," Josh Ma, Cursor

Principle:
  "Building a cloud agent harness means constantly reevaluating how much
   behavior is deterministic and how much gets handed to the agent."

Mechanism:
  As models improve → identify hardcoded harness logic →
  expose as tools → let agent decide → remove from harness

Example: Multi-repo setup
  Before: "multi-repo setups required hardcoded harness behavior"
  After:  "we can give the agent the repo layout, expose tools for branches
           and PRs, and let it decide how to do the work"

Key reframe:
  "The harness isn't going away so much as what it contains is changing"
  i.e., the harness infrastructure persists; its embedded logic migrates
  to agent-controlled tools
```

## Cross-References

- **Corroborates**: `blog-cursor-self-hosted-cloud-agents.md` — That source covers WHERE cloud agents run (on-prem execution workers with cloud inference). This source covers HOW cloud agents should be architected internally (component decoupling, durable execution, environment quality). They are complementary layers of the same product: self-hosted covers the deployment boundary; this covers the internal architecture. Both identify environment access as critical — self-hosted enables internal tool access; this source identifies environment quality as the primary quality determinant.

- **Corroborates**: `blog-cursor-continual-harness-improvement.md` Claim 12 — That source documents Cursor's harness evolution from heavy static context toward fully dynamic tool-fetched context: "That is mostly long gone." This source provides the parallel trajectory from the cloud agent perspective: hardcoded multi-repo harness logic → agent-controlled via exposed tools. Both sources corroborate the meta-principle that harness components encoding "what the model can't do" should be removed as model capability grows. The claims are about different harness domains (context injection vs. agent workflow logic) but state the same principle.

- **Corroborates**: `blog-anthropic-harness-long-running.md` Claim 9 — The Anthropic post states: "every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing." This source operationalizes the same principle through Cursor's production trajectory: multi-repo hardcoded logic was an assumption that the model couldn't reason about repo layout on its own; exposing it as tools proved that assumption wrong. Two independent engineering teams (Anthropic, Cursor) have arrived at the same harness evolution principle from different starting points.

- **Extends**: `blog-cursor-autoinstall-bootstrapping.md` — The autoinstall post describes the technical mechanism (two-stage goal-setter/executor for environment bootstrapping) that this source explicitly references as "one path" toward self-healing agents. This cloud-agent-lessons post provides the business motivation (environment quality as primary quality determinant) and the broader vision (self-healing agents) that autoinstall is a step toward. Together: autoinstall is the mechanism; this post is the strategic context.

- **Extends**: `blog-cursor-security-agents.md` — The security agents post describes Cursor's internal agent fleet (3,000+ PRs/week reviewed by agents). This post adds that 40%+ of Cursor's internal PRs now originate from cloud agents. Together they establish the full production-scale AI contribution: cloud agents generate >40% of PRs; security agents review 3,000+ PRs/week. The two posts together show Cursor operating both generation and review at agent scale, within the same organization.

- **Novel**: The following claims are new to the corpus:
  - **Temporal as the named infrastructure primitive for cloud agent loop durability**: No other corpus source identifies Temporal by name as the durable execution system for agent loops, or documents the 50M+ actions/day / 7M+ workflows scale for agent orchestration infrastructure.
  - **One 9 → two 9s reliability via Temporal migration**: The specific reliability progression from work-stealing to Temporal is not documented elsewhere in the corpus.
  - **Three-component decoupling pattern (agent loop / machine state / conversation state)**: The specific three-way decoupling with its rationale (independent lifecycle management, flexible deployment modes, version upgrade windows) is new. Prior sources discuss multi-agent coordination and execution isolation but not this specific architecture.
  - **"Eternal" to task-scoped workflow evolution**: No other corpus source describes the evolution away from long-running eternal workflows toward task-scoped short workflows specifically for version manageability.
  - **40%+ PR-from-cloud-agent organizational metric**: The highest organizational-scale cloud agent contribution metric in the corpus; no other source documents a comparable figure.
  - **Environment quality as primary production quality determinant (cloud context)**: While the principle that environment matters is implicit in other sources, this is the first corpus source to state it as the *primary* factor with the specific failure mode articulated (subtle degradation, not crashes).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add the three-component decoupling pattern (agent loop / machine state / conversation state) as the reference architecture for production cloud agent infrastructure. The "eternal → task-scoped workflow" evolution should be included as an architectural recommendation with the stated rationale (version upgrade manageability). The harness-to-agent shift principle (Claim 9) should be cited alongside `blog-cursor-continual-harness-improvement.md` Claim 12 and `blog-anthropic-harness-long-running.md` Claim 9 as triple-corroborated practitioner evidence for the meta-principle: harness components encoding model limitations should be progressively removed as model capability increases. Currently the guide cites the Anthropic source for this principle; the Cursor operational examples strengthen the case considerably.

- **Chapter 02 (Harness Engineering — reliability)**: Add the Temporal migration story (Claim 3, Claim 4) as the canonical cloud agent reliability pattern. Recommend Temporal (or equivalent durable execution systems) over naive work-stealing architectures for production cloud agent loops. The one 9 → two 9s improvement with a named infrastructure change is the most specific production reliability progression in the corpus. Pair with `blog-cursor-continual-harness-improvement.md` Claim 7 (tool call reliability driven to "at least 2 or often 3 9s") for the full picture: Temporal handles workflow durability; tool-call reliability requires separate per-tool-per-model monitoring investment.

- **Chapter 04 (Context Engineering — environment quality)**: Add Claim 1 and Claim 2 as the foundation for a section on cloud agent environment quality. The key insight: environment quality is no longer a DevOps concern separate from agent quality — it IS the primary agent quality determinant in cloud contexts. The specific failure mode (subtle degradation, not crashes) has implications for monitoring: teams cannot rely on error detection to identify environment problems; they need quality-signal-based monitoring instead.

- **Chapter 04 (Context Engineering — self-healing environments)**: Add Claim 11 and Claim 12 as the forward-looking section on agent environment self-repair. The autoinstall cross-reference to `blog-cursor-autoinstall-bootstrapping.md` provides the current concrete mechanism; this post provides the strategic vision and the motivation (environment quality as primary determinant). The self-healing agent vision is emergent — not current production capability — but is the logical conclusion of the environment quality thesis.

- **Chapter 00 (Principles) or Chapter 01 (Daily Workflows)**: The 40%+ PR-from-cloud-agent metric (Claim 5) is the strongest practitioner evidence in the corpus for cloud agents reaching "primary workflow" status at organizational scale. This metric should anchor any section on AI-native engineering adoption trajectories. At 40%+ PR origin, cloud agents are not a supplement — they are a primary contributor.

## Extraction Notes

- Source was fetched from https://cursor.com/blog/cloud-agent-lessons and read in full across multiple targeted fetches. The article structure has five named sections corresponding to five lessons; all five were extracted.
- The WebFetch tool returned summaries rather than complete verbatim text due to copyright reproduction constraints. All quotes in this note were specifically requested and verified as verbatim against the source through multiple targeted fetch operations.
- Author name (Josh Ma) is confirmed from the article. Publication date (May 21, 2026) is confirmed from the RSS feed entry in the issue body.
- The article references a "recent research blog" about autoinstall. This maps to `blog-cursor-autoinstall-bootstrapping.md` (issue #551, published May 6, 2026, two weeks prior). The cross-reference is explicit.
- No contradictions to file: the harness-to-agent shift principle corroborates (not contradicts) both `blog-cursor-continual-harness-improvement.md` and `blog-anthropic-harness-long-running.md`. The environment quality thesis is novel, not contradictory to any existing note. The reliability improvement story is also novel.
- The source is a synthesis post, not a feature announcement — it is inherently more reflective and architectural in tone than Cursor's product announcement posts. Treat confidence as emerging: the patterns are drawn from real operational experience at scale, but are described by a single author without external validation.
