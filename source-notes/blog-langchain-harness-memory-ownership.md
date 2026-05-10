---
source_url: https://blog.langchain.com/your-harness-your-memory/
source_type: blog-post
title: "Your harness, your memory"
author: Harrison Chase (LangChain, CEO/co-founder)
date_published: 2026-04-11
date_extracted: 2026-05-10
last_checked: 2026-05-10
status: current
confidence_overall: emerging
issue: "#134"
---

# Your harness, your memory

> LangChain CEO Harrison Chase argues that agent harnesses are permanent infrastructure,
> that memory is inseparable from harness design, and that using closed/API-based harnesses
> (including OpenAI's Responses API, Anthropic's server-side compaction, and Codex) strips
> builders of memory ownership — creating competitive lock-in that cannot be escaped without
> losing accumulated context.

## Source Context

- **Type**: blog-post (LangChain company blog, April 11, 2026)
- **Author credibility**: Harrison Chase is CEO and co-founder of LangChain, the team behind
  LangGraph (agent orchestration framework), LangSmith (observability platform), and the newly
  announced Deep Agents product. He has hands-on practitioner knowledge of agent harness design
  at scale, having observed hundreds of production agent deployments. This post is explicitly
  vendor-positioned — Deep Agents is the open-harness alternative Chase is promoting — so all
  recommendations should be read as coming from a competitor to the closed harnesses he critiques.
  The underlying architectural arguments (memory tied to harness, lock-in through state storage)
  are analytically sound regardless of vendor motivation. The Sarah Wooders citation (attributed
  to a named authority on agent architecture; exact affiliation not confirmed) adds additional
  voice to the memory/harness claim.
- **Scope**: Covers the relationship between agent harnesses and memory ownership; catalogs
  specific lock-in mechanisms in closed harnesses (OpenAI Responses API, Anthropic server-side
  compaction, Codex encrypted summaries); argues for open harnesses with portable storage;
  introduces Deep Agents as LangChain's answer. Does NOT cover harness performance benchmarks,
  specific memory retrieval algorithms, multi-agent coordination patterns, cost/latency tradeoffs
  of different memory approaches, or technical architecture of the open storage backends.

## Extracted Claims

### Claim 1: Agent harnesses are permanent infrastructure — scaffolding needs evolve but harnesses do not disappear

- **Evidence**: Author's direct assertion supported by the Claude Code leak as a concrete data
  point (512k LOC of harness code from the world's leading AI lab). Lists Claude Code, Deep Agents,
  Pi/OpenClaw, OpenCode, Codex, and Letta Code as examples of active harnesses to illustrate
  ongoing investment.
- **Confidence**: emerging (vendor-positioned assertion with a concrete example; the Claude Code
  LOC figure is independently corroborated by the source-leak analysis)
- **Quote**: "There is sometimes sentiment that models will absorb more and more of the scaffolding.
  This is not true."
- **Quote**: "What has happened (and will continue to happen) is that a lot of the scaffolding
  needed in 2023 is no longer needed. But this has been replaced by other types of scaffolding."
- **Our assessment**: The nuanced position — scaffolding types change, scaffolding as a category
  persists — aligns with what Anthropic's own engineers observe (TodoWrite replaced by Task tool;
  context-reset logic replaced by context-editing patterns). The 512k LOC data point is compelling:
  if the world's most capable AI lab still invests in 512k lines of harness code, the "models
  will absorb harnesses" thesis needs strong evidence to overcome it. This is a practitioner
  counterweight to "just use the model" minimalism.

### Claim 2: Claude Code's 512,000 lines of leaked source code constitute the harness — evidence that even best-in-class AI labs invest heavily in harness infrastructure

- **Evidence**: The March 2026 Claude Code source map leak, analyzed by multiple practitioners.
  The 512k figure is attributed to the leaked codebase.
- **Confidence**: emerging (the leak is independently documented; the exact 512k LOC count comes
  from Chase's post, consistent with what practitioners reported from the leak)
- **Quote**: "When Claude Code's source code was leaked, there was 512k lines of code. That code
  is the harness."
- **Our assessment**: The 512k LOC framing is a rhetorical use of the leak to make a structural
  point: the harness is the product, not an afterthought. The Alex Kim analysis of the leak
  (`failure-alex000kim-claudecode-source-leak.md`) independently documents what those lines
  contain — autoCompact logic, coordinator orchestration, 14-vector cache tracking, 23-check
  bash security — confirming that this is substantive infrastructure, not boilerplate. Chase's
  argument is valid: Anthropic, with access to the world's most capable models, still wrote
  512k lines of harness code.

### Claim 3: Memory is inseparable from the harness — managing context IS managing memory, and harnesses own both

- **Evidence**: Direct assertion by Chase, bolstered by a named authority (Sarah Wooders) on the
  same point.
- **Confidence**: emerging (two practitioners making the same structural claim; consistent with
  Anthropic's own architectural descriptions)
- **Quote**: "Managing context, and therefore memory, is a core capability and responsibility of
  the agent harness." (attributed to Sarah Wooders)
- **Quote**: "ultimately, how the harness manages context and state in general is the foundation
  for agent memory."
- **Our assessment**: This is the load-bearing architectural claim of the post. If context
  management = memory management and the harness owns context management, then wherever memory
  lives, the harness is responsible for it. The conclusion (closed harnesses own your memory)
  follows directly from this premise. Corroborated by Anthropic's own framing: their harness
  posts (`blog-anthropic-harnessing-claude-intelligence.md`) treat compaction, memory folders,
  and context editing as core harness design decisions — not model-level features.

### Claim 4: Short-term and long-term memory have distinct harness responsibilities with different mechanics

- **Evidence**: Architectural distinction drawn by Chase; no benchmark evidence.
- **Confidence**: anecdotal (reasonable taxonomy stated by a practitioner; widely consistent with
  how harness authors actually implement memory)
- **Quote**: "Short term memory (messages in the conversation, large tool call results) are handled
  by the harness. Long term memory (cross session memory) needs to be updated and read by the
  harness."
- **Our assessment**: This two-tier taxonomy (in-session context vs. cross-session persistence)
  maps cleanly onto the harness decisions documented elsewhere in the corpus. Short-term memory
  is the context window management problem (compaction, context editing, subagents). Long-term
  memory is the persistence problem (memory folders, external storage, vector databases). Framing
  both as harness responsibilities — not model capabilities — is the key move that sets up the
  lock-in argument.

### Claim 5: A deleted-and-recreated personal assistant loses all accumulated preferences and must be retrained from scratch — illustrating memory's irreplaceable accumulated value

- **Evidence**: Harrison Chase's personal experience with an internal email assistant that was
  accidentally deleted. Recreating it from the same template produced an inferior experience.
- **Confidence**: anecdotal (single personal anecdote from the author)
- **Quote**: "the experience was so much worse. I had to reteach it all my preferences, my tone,
  everything."
- **Our assessment**: This is the strongest intuition-pump in the post. The anecdote makes
  abstract "memory lock-in" concrete: you feel it when the agent forgets who you are. For guide
  readers who have not yet run into this problem, this is the clearest illustration of what is
  at stake. The business implication follows directly: if your agent's accumulated memory is
  your competitive differentiator, losing it (to an accidental delete, a provider switch, or
  a model migration) is a serious business risk.

### Claim 6: Using a closed harness behind an API means you do not own your memory

- **Evidence**: Architectural argument: API-based harnesses store state server-side, out of
  the user's control.
- **Confidence**: emerging (logical deduction from how these APIs are structured; well-reasoned
  but the specific accessibility of stored state in these systems is not tested empirically)
- **Quote**: "If you use a closed harness, especially if its behind an API, you don't own your
  memory."
- **Our assessment**: The claim depends on the architectural framing of Claim 3: if memory =
  harness-managed context, and the harness is a black-box API you don't control, you cannot
  inspect, export, migrate, or version your agent's accumulated context. This is a structural
  argument, not an empirical one — whether it matters in practice depends on whether you intend
  to migrate models, recover from failures, or audit agent behavior over time.

### Claim 7: OpenAI's Responses API and Anthropic's server-side compaction store state on provider servers, making cross-provider model swaps impossible for existing sessions

- **Evidence**: Architectural description of how these APIs work. No citation to API documentation
  or empirical test; reasoning from API design.
- **Confidence**: emerging (plausible architectural claim; consistent with how stateful APIs
  typically work; not independently verified against current API documentation)
- **Quote**: "If you use a stateful API (like OpenAI's Responses API, or Anthropic's server side
  compaction), you are storing state on their server."
- **Quote**: "if you want to swap models and resume previous threads - that is no longer doable."
- **Our assessment**: This is the most specific and actionable lock-in claim in the post. If
  accurate, it means: a team using Anthropic's server-side compaction accumulates session state
  in Anthropic's infrastructure. When Claude 5 replaces Claude Opus 4.6, migrating those sessions
  to a competing provider requires re-establishing all accumulated context from scratch — or
  accepting session loss. The practical implication for architecture decisions: if long-running
  session persistence across months of interactions is a design goal, the storage layer must be
  under the builder's control, not the model provider's.

### Claim 8: Codex is nominally open-source but generates encrypted compaction summaries that are unusable outside the OpenAI ecosystem

- **Evidence**: Direct observation by Chase about Codex's behavior; not independently verified.
- **Confidence**: anecdotal (single practitioner observation; plausible given Codex's design as
  an OpenAI product; not confirmed against Codex source code or documentation)
- **Quote**: "Even though Codex is an open source, it generates an encrypted compaction summary
  (that is not usable outside of the OpenAI ecosystem)."
- **Our assessment**: If accurate, this is a concrete example of "open-source theater" — the
  source is open but the state artifacts are locked. This is a meaningful distinction for teams
  evaluating Codex: open weights/code does not guarantee portability if the runtime's accumulated
  state format is opaque and provider-specific. Practitioners evaluating open-source harnesses
  should verify whether the memory/state format is independently decodable.

### Claim 9: Memory lock-in is alarming because it ties accumulated context to a single platform and model

- **Evidence**: Chase's direct assertion about the competitive/strategic implications of
  provider-owned state.
- **Confidence**: anecdotal (strategic concern stated by a vendor with a competing product)
- **Quote**: "This is incredibly alarming - it means that memory will become locked into a single
  platform, a single model."
- **Our assessment**: This is the strategic framing of the architectural claims above. The
  concern is well-founded: platform lock-in through state accumulation is a well-documented
  switching cost mechanism. The vendor motivation doesn't invalidate the concern — it's in
  providers' interests to accumulate sticky state, and it's in builders' interests to be aware
  of this dynamic.

### Claim 10: Memory is the primary differentiator that makes agents non-replicable — it creates a proprietary dataset

- **Evidence**: Chase's direct assertion.
- **Confidence**: anecdotal (plausible strategic framing; consistent with how accumulated
  user-specific context functions in practice)
- **Quote**: "Without memory, your agents are easily replicable by anyone who has access to
  the same tools. With memory, you build up a proprietary dataset."
- **Our assessment**: This is a competitive strategy argument, not an engineering one. The claim
  is that memory = accumulated context = proprietary knowledge base that competitors cannot
  replicate even with identical model access. This is true in the same sense that a trained
  ML model is proprietary: the training data (in this case, accumulated interaction history)
  is the differentiator. The implication for builders: owning your memory layer is owning
  your data moat.

### Claim 11: Memory and harnesses should be separate from model providers to preserve model optionality

- **Evidence**: Chase's prescription; illustrated with Deep Agents' storage backends.
- **Confidence**: anecdotal (reasonable design recommendation; no comparative benchmark evidence)
- **Quote**: "Memory (and therefor harnesses) should be separate from model providers. You should
  want optionality to try out whatever models are best for your use case."
- **Our assessment**: This is the architectural prescription the post builds toward. The
  argument: model capabilities evolve fast; the best model today may not be best in six months;
  locking memory to a specific model/provider forfeits the ability to upgrade. Open storage
  backends (Mongo, Postgres, Redis) let the harness layer persist state independently of which
  model processes it. For guide purposes: this is a vendor recommendation from LangChain, but
  the underlying design principle (separate state from compute) is sound engineering.

## Concrete Artifacts

### Lock-in Taxonomy: Closed Harnesses and Their Memory Storage Mechanisms

```
# Memory lock-in taxonomy (from "Your harness, your memory", Harrison Chase, April 11, 2026)
# Three specific closed-harness lock-in mechanisms identified:

1. OpenAI Responses API (stateful)
   Lock-in mechanism: State stored on OpenAI servers.
   Portability: Cannot resume threads on a different provider's model.

2. Anthropic server-side compaction
   Lock-in mechanism: Compacted session state stored on Anthropic servers.
   Portability: Sessions cannot be resumed outside the Anthropic ecosystem.

3. OpenAI Codex (nominally open-source)
   Lock-in mechanism: Generates encrypted compaction summaries.
   Portability: Summaries are not usable outside the OpenAI ecosystem.
   Note: "open source" ≠ portable state format.
```

### Open Harness Reference: Deep Agents Architecture

```
# Deep Agents architecture summary (from "Your harness, your memory", Harrison Chase, April 11, 2026)
# LangChain's answer to the memory ownership problem:

Storage backends: Mongo, Postgres, Redis (user-controlled)
Deployment options:
  - LangSmith Deployment (cloud, self-hostable, deployable on any cloud)
  - Fleet (no-code platform for Enterprise OpenClaw deployments)
Open standards: agents.md
Framework: Built on LangGraph

Key properties claimed:
  - Memory stored in user-controlled infrastructure
  - Model-swappable (memory format not tied to a specific provider)
  - Self-hostable (no mandatory cloud dependency)
```

### Article Structure

```
# Section structure of "Your harness, your memory" (Harrison Chase, April 11, 2026)
# Sections in order:

1. Agent Harnesses are how you build agents, and they're not going anywhere
2. Harnesses are tied to memory
3. if you don't own your harness, you don't own your memory
4. Memory is important, and it creates lock in
5. Open Memory, Open Harnesses
```

## Cross-References

- **Corroborates**:
  - `failure-alex000kim-claudecode-source-leak.md` — Claim 2 here (512k LOC = the harness) is
    directly supported by that note's detailed analysis of what those lines contain: autoCompact
    logic, multi-agent coordinator, 14-vector cache tracking, 23-check bash security. The Alex
    Kim note provides the technical inventory of what "512k lines of harness code" actually means
    in practice, transforming Chase's rhetorical data point into a documented fact.
  - `blog-anthropic-harnessing-claude-intelligence.md` — Claim 1 here (harnesses persist, types
    evolve) corroborates Claim 15 there ("what can I stop doing?" at each model upgrade / harness
    components become dead weight). Both sources agree: old scaffolding retires but new scaffolding
    takes its place. The LangChain post provides the competitor's-eye view of the same observation
    Anthropic's own engineers make.
  - `blog-anthropic-seeing-like-an-agent.md` — The RAG→Grep→Skills evolution documented there
    (Claim 8 and 9) is a concrete instance of Claim 1 here: old scaffolding (RAG) was replaced
    by new scaffolding (Grep tool, Agent Skills), not eliminated. The "harnesses evolve" claim
    in this post has a specific three-step example in the Anthropic note.
  - `blog-anthropic-harness-long-running.md` — Corroborates Claim 1 here on harness persistence.
    That post documents systematic removal of harness components as model capability grows —
    and replacement with new ones. Both sources reach the same conclusion ("harnesses are here
    to stay") through different arguments.

- **Contradicts**:
  - None identified. The lock-in claims (Claims 6–8) describe a capability-vs-portability
    tradeoff: Anthropic's compaction produces better results (as documented in
    `blog-anthropic-harnessing-claude-intelligence.md` Claim 7: 43%→68%→84% BrowseComp scaling)
    but Chase argues it does so at the cost of memory portability. These are different dimensions
    (performance vs. ownership) rather than opposing claims about the same dimension. Verify
    before the Smith synthesizes: if Ch04 or Ch05 makes a recommendation to use server-side
    compaction, this source adds the portability caveat that should accompany it.

- **Extends**:
  - `blog-thebatch-nemotron-agent-infra.md` — Claim 8 there (OpenAI/AWS stateful agent runtime)
    describes the architecture that Chase is warning against in Claims 7 and 9 here. The Batch
    note describes stateful runtimes as a capability enabler (managed memory, tool connections,
    permissions); this LangChain post describes the same design pattern as a lock-in mechanism.
    Together they provide both sides of the architectural tradeoff: managed state lowers harness
    build burden but creates provider dependency.
  - `blog-anthropic-harnessing-claude-intelligence.md` — Adds the memory-ownership and lock-in
    dimension to that post's compaction capability data. That post answers "how much better does
    compaction make your agent?"; this post adds "and here's the portability cost of using
    provider-managed compaction." The two notes together form the complete picture of the
    compaction tradeoff space.

- **Novel**:
  - **Memory ownership as a first-class architectural concern**: No other corpus source frames
    the memory/context question in terms of *ownership*. Anthropic posts treat memory as a
    capability; this post treats it as an ownership and portability question. This framing
    is new to the corpus and belongs in Ch05 (Vendor Lock-in & Architectural Portability).
  - **Encrypted compaction summaries in nominally open-source harnesses (Codex)**: The specific
    finding that Codex generates encrypted, non-portable state despite being open-source is
    not documented anywhere else in the corpus. "Open source" ≠ portable state is a
    practitioner distinction worth surfacing explicitly.
  - **Memory as proprietary dataset / competitive moat**: The claim that accumulated agent
    memory constitutes a proprietary dataset not easily replicated by competitors (Claim 10)
    is a business-strategy framing of memory not found in other corpus sources.
  - **Lock-in taxonomy for specific closed harnesses**: The three-provider taxonomy (OpenAI
    Responses API, Anthropic compaction, Codex encrypted summaries) as specific lock-in
    mechanisms is new. Other sources mention individual mechanisms; this is the first to
    present them as a coherent category.

## Guide Impact

- **Chapter 02 (Agent Harness Architecture & Design)**: Claim 1 and Claim 2 together should
  anchor the "harnesses are here to stay" position with two supporting data points: (a) Chase's
  evolutionary argument ("scaffolding types change, not scaffolding as a category"), which
  corroborates Anthropic's own practitioner observations; (b) the 512k LOC data point as the
  strongest concrete evidence that harness investment is real even at the world's most capable
  AI lab. Recommend pairing with `failure-alex000kim-claudecode-source-leak.md` for the
  technical content of those 512k lines.

- **Chapter 04 (Memory & Context Management)**: Claims 3 and 4 establish the architectural
  premise that memory is a harness responsibility, not a model-layer feature. The two-tier
  taxonomy (short-term = in-session context; long-term = cross-session persistence) provides
  a simple organizing framework for the chapter's discussion of memory strategies. Add
  Claim 5 (email assistant anecdote) as the human-scale illustration of what memory loss
  feels like — useful before introducing the technical solutions.

- **Chapter 05 (Vendor Lock-in & Architectural Portability)**: This source belongs here more
  than anywhere else. Claims 6–9 provide the first corpus-level treatment of memory lock-in
  as a category with named instances. Specific additions warranted:
  (a) Add the three-provider lock-in taxonomy (Concrete Artifacts section) as a reference
      checklist for evaluating harness choices.
  (b) Add Claim 7 (stateful API = state stored on provider servers = no cross-provider thread
      resumption) as the core mechanism behind memory lock-in.
  (c) Add the Codex observation (Claim 8) as a concrete example of "open source does not
      guarantee portability" — relevant to teams evaluating apparently-open harnesses.
  (d) Pair with the capability argument from `blog-anthropic-harnessing-claude-intelligence.md`
      Claim 7 (compaction scales performance 43%→84%) to present the full tradeoff: better
      performance vs. portability loss.

- **Chapter 05 (Vendor Lock-in & Architectural Portability)**: Claim 10 (memory as proprietary
  dataset / competitive moat) adds a business-strategy dimension not currently in the corpus.
  This is the "why it matters" complement to the technical lock-in claims: locked memory is
  both a competitive asset (hard to replicate) and a risk (hard to migrate). The guide should
  present both sides.

## Extraction Notes

- The source URL redirects from https://blog.langchain.com/your-harness-your-memory/ to
  https://www.langchain.com/blog/your-harness-your-memory — both URLs resolve to the same
  post. The redirect URL is the canonical address.
- All quotes were extracted via WebFetch intermediary analysis, not direct page rendering.
  The intermediary confirmed these as verbatim text from the article, but minor punctuation
  differences cannot be entirely ruled out. The Assayer should spot-check against the live
  URL if any quote attribution is contested.
- Sarah Wooders is cited in the article as an authority on the memory/harness claim; her
  organizational affiliation was not stated in the portions of the article accessible to
  extraction. The quote itself is attributed to her by name.
- The article is explicitly promotional for Deep Agents (LangChain's product). Chase's
  critique of OpenAI Responses API, Anthropic compaction, and Codex is not empirically tested
  — it is architectural reasoning from someone who builds competing infrastructure. All Claims
  6–8 and 11 should be labeled as vendor-positioned and verified against primary API
  documentation before the Smith synthesizes them as settled.
- No code examples or configuration snippets are present in the source. The Concrete Artifacts
  section extracts the taxonomic content (lock-in mechanisms, Deep Agents architecture) as
  structured descriptions rather than code.
- The "agents.md" standard mentioned in relation to Deep Agents is referenced but not defined
  in the portions of the article extracted. It appears to be an emerging open standard for
  agent configuration; further research may be warranted.
- Cross-references were verified by re-reading the cited source notes before writing. Claim
  numbers cited above correspond to top-to-bottom document order in each cited note.
