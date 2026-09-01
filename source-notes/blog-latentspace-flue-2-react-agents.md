---
source_url: https://www.latent.space/p/flue-2
source_type: blog-post
title: "React for Agents: Astro Creator Brings Hooks to his Meta-Harness, Flue"
author: Richard MacManus (Latent Space), interviewing Fred Schott (creator of Astro and Flue, Cloudflare)
date_published: 2026-08-15
date_extracted: 2026-09-01
last_checked: 2026-09-01
status: current
confidence_overall: emerging
issue: "#3145"
---

# React for Agents: Astro Creator Brings Hooks to his Meta-Harness, Flue

> A first-person interview with Fred Schott (creator of Astro, now at Cloudflare) on Flue 2 —
> a "harness-first" agent framework whose central composition primitive is a set of 16
> React-style "Agent Hooks" (`useSkill()`, `useTool()`, `useSubagent()`) that let an agent,
> represented as a JavaScript function that "re-renders on every turn," dynamically attach
> capabilities at runtime — plus Schott's account of why Flue abandoned file-based routing,
> how it positions against Vercel's `eve`, and why "there is no agent without a harness."

## Source Context

- **Type**: blog-post (Latent Space, a new "written interview series" the publication is
  piloting for subscribers, per the article's closing line: "This is a new written interview
  series we are trying out for subscribers — let us know your feedback!"). Not paywalled
  (`audience: everyone` in the page's own post metadata); 1,436 words per the post's own
  `wordcount` field. Format is narrative reporting interleaved with direct quotes from Schott,
  not a raw Q&A transcript — distinct from the Q&A-transcript format of
  `blog-latentspace-vercel-andrew-qu-eve.md`.
- **Author credibility**: Richard MacManus is the interviewer/reporter (Latent Space).
  Fred Schott, the interview subject, is a first-party, maximally-credible source for claims
  about Flue's own design: he is Flue's creator, and per the article, "the creator of the web
  framework Astro, which led to his company being acquired by Cloudflare in January [2026]."
  He personally tested-drove the framework's onboarding with MacManus during the interview
  ("I myself tested out Flue using Claude Code, which guided me through setting up my first
  Flue agent"), giving the piece a first-hand verification element beyond pure quotation.
  No metrics, benchmark numbers, or named customer case studies are given anywhere in the
  piece — every technical claim is Schott's own qualitative design narrative, not measured
  data.
- **Scope**: Covers Flue 2's hooks-based composition model and execution semantics, the
  "harness-first" design philosophy and its origin in Flue's underlying harness (Pi), the
  evolution from Flue 1's file-based-routing model to Flue 2's React-inspired composability,
  Flue's own origin story (an Astro-repo issue-triage script that grew into a headless
  Claude-Code-like framework), competitive positioning against Vercel's `eve` and against
  "OG agent frameworks" (Vercel AI SDK, Cloudflare Agents SDK, Mastra), Schott's stance on
  host portability despite his employer being Cloudflare, and his explicit non-answer on
  cross-harness "meta-harness" interoperability (Databricks' Omnigent, Exo). Does **not**
  cover: Flue's actual code/API syntax beyond hook names, pricing, adoption numbers, named
  customer deployments (only two illustrative, unnamed use-case categories — support bots,
  triage bots — are given), or a technical description of Pi itself beyond "an open source
  minimal harness." No sub-pages were followed: the article contains no inline links to
  Flue's own documentation, the Flue 2 launch post it quotes from, or Pi's repository: all
  citable content is contained in the interview text itself.

## Extracted Claims

### Claim 1: Flue 2's foundational primitive is a set of React-style "Agent Hooks"; an agent is represented as a JavaScript function that "re-renders on every turn," i.e., before every model call
- **Evidence**: Direct architectural description from the article's opening paragraphs.
- **Confidence**: settled (unambiguous first-party description of a shipped, stable release — "its first stable release")
- **Quote**: "In Flue, an agent is represented by a JavaScript function. This function “re-renders on every turn,” meaning before every model call."
- **Our assessment**: This is the article's core technical claim and the one most useful for Ch02: it names a specific execution model (agent-as-function, re-evaluated each turn) borrowed directly from React's render-on-state-change model, rather than the more common "agent as a fixed loop with a system prompt and tool list" framing found elsewhere in the corpus. Whether "re-render on every turn" is a good mental model for agent state management (vs. e.g. an explicit state machine) is an open design question the article does not itself argue for beyond Schott's own conviction.

### Claim 2: Flue 2 ships 16 built-in hooks — including `useSkill()`, `useTool()`, and `useSubagent()` — authored in TypeScript, that let developers build dynamic agents managing their own state, listening to lifecycle events, and attaching resources/capabilities dynamically at runtime; custom hooks can also be added
- **Evidence**: Direct enumeration plus a quote the article attributes to "the Flue 2 launch post" (a Schott-authored primary source the interview quotes but does not link).
- **Confidence**: settled (first-party feature enumeration, though the specific behavior of all 16 hooks beyond the three named is not detailed in this source)
- **Quote**: "There are 16 built-in hooks in Flue 2, including useSkill(), useTool(), useSubagent(). You can also add custom hooks."
- **Quote (from the Flue 2 launch post, as quoted in the article)**: "let you build dynamic agents that can manage their own state, listen to agent lifecycle events, and even attach different resources and capabilities dynamically to enhance themselves at runtime"
- **Our assessment**: The three named hooks map onto three distinct composition concerns — skill attachment, tool attachment, and subagent delegation — as first-class, composable function calls rather than static configuration (e.g., a fixed tool list in a system prompt or config file). This is the concrete API surface underneath Claim 1's "re-renders on every turn" execution model. The remaining 13 hooks are not named or described in this source; a follow-up mining pass on Flue's own documentation would be needed to enumerate them.

### Claim 3: Hooks enable runtime reconfiguration for use cases that "can't be fully configured in advance" — illustrated by a support agent that brings in an account-management tool only after first verifying the user's identity
- **Evidence**: Direct example from the article, following Schott's framing of why static agent configuration is insufficient for support/triage bot use cases.
- **Confidence**: anecdotal (a single illustrative example, not a documented production deployment or named customer)
- **Quote**: "For example, a support agent might bring in an account management tool after first verifying a user."
- **Our assessment**: This is a concrete, checkable pattern: gate tool availability on a runtime condition (verification state) rather than exposing all tools unconditionally from turn one. It's a specific instance of the general "principle of least capability, granted incrementally" pattern that recurs elsewhere in the corpus for agent identity/permissioning (see Cross-References), applied here at the framework-composition level rather than the platform-identity level. No named production deployment backs this — it is Schott's own illustrative example, not a documented case study.

### Claim 4: Flue's central design bet is that a harness is not an optional feature but constitutive of what an agent is — "there is no agent without a harness"
- **Evidence**: Direct quote from Schott explaining Flue's foundational architectural commitment.
- **Confidence**: settled (unambiguous first-party statement of the framework's core design philosophy, though it is a design conviction, not an empirically tested claim)
- **Quote**: "Our early bet was that the harness is actually not a feature, but it's fundamental to what you think an agent is," Schott said. "There is no agent without a harness."
- **Our assessment**: This is the article's title-level thesis and the clearest, most quotable single-sentence articulation in our corpus of "harness-first" agent-framework design philosophy — stronger and more absolute in phrasing than the comparable claims in `blog-latentspace-vercel-andrew-qu-eve.md` (see Cross-References), which frame harness-related primitives (context, tools, resumability) as necessary requirements rather than as a definitional claim about what an agent *is*.

### Claim 5: Flue is built on top of Pi, "an open source minimal harness," with Flue positioned as an opinionated, batteries-included layer atop Pi's minimal abstraction — Schott likens the Pi/Flue relationship to Vite's foundational role beneath Astro
- **Evidence**: Direct architectural description and analogy from Schott, who also created Astro (which itself now uses Vite as its build tool).
- **Confidence**: emerging (first-party architectural description; the source does not identify who built Pi, so Pi's own provenance/authorship is not established by this article)
- **Quote**: "Flue is built on top of Pi, an open source minimal harness." … "I think Pi can serve that role, where it's the right abstraction — it doesn't do too much, but it gives the right APIs that then we can go and say, well, let's have an opinionated take on this that does more."
- **Our assessment**: This names a specific two-layer architecture pattern — a minimal, unopinionated harness (Pi) plus an opinionated developer-experience layer (Flue) built on top of it — directly analogous to the Vite/Astro or (in web-framework terms generally) engine/framework split. This is a distinct architectural pattern from the single-layer "harness is the framework" framing implied elsewhere; it suggests Flue's specific value-add is developer ergonomics and conventions layered onto a separately-maintained minimal execution substrate, not the substrate itself. The article gives no technical detail on what Pi actually provides beyond "the right APIs."

### Claim 6: Flue abandoned a file-based-routing model (ported naively from web frameworks, where each file/agent maps to a route) after early customer feedback showed most enterprise users run a single agent per company, not many routed agents — this drove the pivot toward React's composability model as Flue 2's foundation
- **Evidence**: Direct first-person narrative from Schott describing the specific feedback and reasoning that changed Flue's architecture between v1 and v2.
- **Confidence**: emerging (single-framework origin narrative from its creator; not independently corroborated, but told in specific, falsifiable terms)
- **Quote**: "So we kind of naively ported that over to Flue, thinking — great, well, I'll put your five agents in these five files, and that'll be the five routes that they expose. But for a lot of people building with Flue, especially the bigger customers, their whole company is one agent. They don't care about routing. There's one agent."
- **Our assessment**: This is a specific, checkable design-mistake-and-correction narrative: web-framework concepts (file-based routing) do not transfer cleanly to agent frameworks because the underlying unit of value is different — a website has many routes serving many pages, but (per this practitioner's customer base) an enterprise agent deployment is often architecturally singular, with the composition problem occurring *within* one agent (which skills, tools, and subagents it can reach) rather than *across* many routed agents. This is a useful cautionary data point for anyone porting web-framework idioms directly into agent-framework design.

### Claim 7: Schott identifies Vercel's `eve` as Flue's most directly competitive framework because both treat the harness as foundational rather than as an added feature, and both launched in the same year; he separately names "OG agent frameworks" (Vercel's AI SDK, Cloudflare's Agents SDK, and Mastra) as frameworks now retrofitting harnesses as an add-on rather than a founding concept
- **Evidence**: Direct quote and framing from Schott, with the article's own framing note ("Vercel and Cloudflare have been known to beef in public, but Schott is generous in his opinion of eve").
- **Confidence**: emerging (a competitor's own characterization of the competitive landscape — credible as a first-party design-philosophy claim, but not an independently verified market analysis)
- **Quote**: "Eve, I think, is the most directly competitive," Schott said. "It came around at the same time, so it had that same take that a harness is built-in."
- **Our assessment**: This corroborates, from a second and independent framework author, `blog-latentspace-vercel-andrew-qu-eve.md`'s framing that a built-in (not bolted-on) harness is `eve`'s defining architectural choice — Schott is naming the exact same distinguishing feature (harness-as-foundational vs. harness-as-add-on) as the axis on which he judges Flue's own closest competitor. The "OG agent frameworks... adding harnesses now" claim is a specific, named, checkable list (Vercel AI SDK, Cloudflare Agents SDK, Mastra) worth cross-checking against those frameworks' own changelogs if this becomes load-bearing for the guide.

### Claim 8: Despite being built by a Cloudflare employee and able to leverage Cloudflare's infrastructure, Flue is explicitly designed and positioned as an "open source framework for every host" — Schott frames host portability as a deliberate, durable design principle, distinguishing Flue from `eve`, which (while self-hostable) is optimized specifically for Vercel's platform features
- **Evidence**: Direct quotes from Schott plus the article's own comparative framing against `eve`'s Vercel-optimization.
- **Confidence**: emerging (a stated design principle and current behavior, not a technically verified claim about the absence of host lock-in in Flue's actual implementation)
- **Quote**: "Flue is an 'open source framework for every host,' as he put it, and he wants it to stay that way." … "The best tools are the ones that float above the host," he said. "That opens the door for the most developer adoption and the most innovation."
- **Our assessment**: This is presented as Flue's key differentiator from `eve` specifically ("perhaps that's where the fundamental difference to Vercel's eve is"), and the article notes the asymmetry is not absolute in either direction: "Vercel itself has shown that a Flue agent can be deployed on Vercel," and `eve` "can also be self-hosted" despite being Vercel-optimized. This is a stated intent and current framing from the framework's creator, not an independently audited absence of platform-specific dependencies — worth noting for the guide as a design *principle* to evaluate against, not a settled technical guarantee.

### Claim 9: Flue originated inside the Astro repository as an internal LLM-driven issue-triage script/workflow, which gained the ability to take repo actions, and was then reframed around making "the Claude Code experience... headless... hostable and run it in the cloud" — Schott's own Flue 1 launch post described the result as "like Claude Code, but 100% headless and programmable"
- **Evidence**: Direct origin narrative from Schott, with a quote attributed to his own earlier (May 2026) Flue 1 launch post.
- **Confidence**: emerging (single-framework, first-party origin narrative; internally consistent and specific, but not independently corroborated)
- **Quote**: "It started to transition from just automation in a repo to wanting to take the Claude Code experience, make it headless, make it hostable and run it in the cloud." … Flue 1 launch post: "like Claude Code, but 100% headless and programmable."
- **Our assessment**: This is a specific, named lineage from a narrow internal tool (issue-triage automation for one open-source project) to a general-purpose framework — structurally similar to `eve`'s "dogfooding produced the framework" origin story (see Cross-References), but starting from a much narrower initial use case (repo issue triage vs. `eve`'s "our own agent in v0"). The "Claude Code, but headless and programmable" framing is a useful, quotable positioning line for describing what an agent framework is *for* to readers already familiar with Claude Code's interactive CLI experience.

### Claim 10: The "React for agents" framing was arrived at after rejecting two earlier framing candidates ("the Astro for agents," "the Next.js for agents") — Schott concluded no one had actually built the composability-focused analog to React specifically, which motivated the hooks-based pivot
- **Evidence**: Direct quote describing Schott's own naming/framing evolution.
- **Confidence**: anecdotal (a single practitioner's self-reported framing evolution, not an independently verifiable technical claim)
- **Quote**: "I originally tweeted that we were building the Astro for agents or the Next.js for agents," he told us. "But then I realized: maybe no one has even built the React for agents."
- **Our assessment**: This is a naming/positioning narrative rather than a technical claim, but it's a useful signal for how Schott himself understands what's novel about Flue 2: not "a new web-framework-style tool for agents" (Astro/Next.js analogy — routing, file conventions) but specifically "a new *composability model* for agents" (React analogy — component composition via hooks). This reframing is the stated motivation for Claim 6's pivot away from file-based routing.

### Claim 11: Schott declines to pursue a unified cross-"meta-harness" abstraction (spanning frameworks like Databricks' Omnigent or Exo) because he judges the term poorly defined at this stage and believes a common API across harnesses would blur Flue's own value proposition, which depends on Flue's framework and its specific harness being "very intertwined"
- **Evidence**: Direct response to being asked how Flue relates to emerging "meta-harness" architectures, reported partly via direct quote and partly via the reporter's paraphrase.
- **Confidence**: anecdotal (a stated personal/product-strategy position from one framework author, on a term the article itself notes is not yet well-defined industry-wide)
- **Quote**: "the framework [Flue] and the harness are very intertwined" — describing Schott's view that Flue's own framework "specifically defines how skills work in Flue, how subagents work, and so on."
- **Our assessment**: This is a deliberate architectural non-goal, not an oversight: Schott is explicitly choosing framework/harness coupling over cross-harness interoperability, on the grounds that a common "meta-harness" API would "muddle the story for Flue." This directly complicates the meta-harness lineage question raised in `blog-latentspace-ainews-meta-harness-summer.md` (see Cross-References) — Flue's own creator, when asked directly, does not accept "meta-harness" (in the harness-of-harnesses, cross-framework-interoperability sense) as a goal for Flue, even though that earlier source lists "Cloudflare's Flue" as part of a meta-harness lineage. The two sources may be using "meta-harness" in different senses (see Cross-References for the terminology issue this raises).

### Claim 12: Flue has no managed-hosting/agent-platform product on its roadmap, in explicit contrast to offerings like LangChain's Managed Deep Agents — Schott frames this as "so early for us, we're just focused on building the best harness"
- **Evidence**: Direct response to being asked about hosted-agent-platform competition.
- **Confidence**: settled (unambiguous first-party statement of current, stated non-roadmap)
- **Quote**: "It's so early for us, we're just focused on building the best harness," he said.
- **Our assessment**: This scopes what Flue currently is (a framework/harness) versus what it explicitly is not yet (a managed hosting platform) — useful for readers trying to place Flue in a build-vs-buy decision alongside fully-managed alternatives; the comparison point named (LangChain's Managed Deep Agents) is not otherwise elaborated in this source.

### Claim 13: Fred Schott is the creator of the Astro web framework, and his company was acquired by Cloudflare in January 2026; Flue 1 launched publicly in early May 2026 and Flue 2 (the first stable release, hooks-based) is the subject of this August 15, 2026 interview
- **Evidence**: Direct biographical and timeline statements in the article.
- **Confidence**: settled (biographical and timeline facts stated directly, not in dispute)
- **Quote**: "Schott is the creator of the web framework Astro, which led to his company being acquired by Cloudflare in January." … "Schott's thinking about how to build an agent framework has evolved rapidly since he publicly launched Flue 1 in early May."
- **Our assessment**: Establishes both Schott's authorship credibility (a web-framework creator with a successful acquisition, applying the same design instincts to agent frameworks) and a rapid iteration timeline: Flue went from a first public launch (early May 2026) to a hooks-based, "first stable release" architecture rewrite (Flue 2, by mid-August 2026) in roughly three months — a fast pace of architectural churn worth flagging for readers evaluating framework maturity/stability.

### Claim 14: A secondhand editorial aside (not from Schott) cites Bret Taylor (CEO of Sierra, Chairman of OpenAI) characterizing agent frameworks broadly as still being in "the jQuery era... not the react era" — i.e., pre-consolidation, with no settled dominant paradigm yet
- **Evidence**: An "Editor's Note" inserted by Latent Space referencing a separate, earlier interview with Bret Taylor, not part of the Schott interview itself.
- **Confidence**: anecdotal (a single secondhand quote from a different interview, inserted as editorial context rather than argued or elaborated in this piece)
- **Quote**: "We're still trying to figure out who the reactive agents are and the jury is still out… We're sort of in the jQuery era of agents, not the react era."
- **Our assessment**: This is explicitly framed by the editors as prior context, not as Schott's own view — Schott's own framing (Claims 1, 4, 10) is confident that Flue 2 *is* a "React for agents" candidate, in implicit tension with Taylor's "jury is still out" framing. We do not read this as a MINER.md §4a-worthy contradiction: Taylor's quote is a single secondhand aside about the industry generally, not a developed, evidenced position that materially opposes a specific claim in an existing source note, and both statements can be true simultaneously (a candidate solution existing does not mean the field has converged on it). Flagged here as useful framing/context — a reminder that "react-style hooks for agents" is, as of this source, one contender's self-assessment, not an industry-settled consensus.

## Concrete Artifacts

### Named "OG agent frameworks" that added harnesses as a later feature (per Schott, as quoted/paraphrased in the article)
```
Source: https://www.latent.space/p/flue-2

Vercel's AI SDK
Cloudflare's Agents SDK
Mastra (built by the team behind Gatsby, a web framework predating Astro)

Per the article: "While these 'OG agent frameworks' are all adding harnesses
now, Schott considers that an added feature — whereas Flue and eve both
have built-in harnesses."
```

### Flue's stated architecture layering (Pi -> Flue), by analogy to Astro's own stack
```
Source: https://www.latent.space/p/flue-2

Pi        = "an open source minimal harness" (foundational, unopinionated)
Flue      = an opinionated take on Pi, adding developer-facing features
Analogy given by Schott: Pi : Flue :: Vite : Astro
Also noted: "hosted agents in Flue 2 are now built with Vite"
```

### Named hooks (of 16 total built-in hooks; only 3 are named in this source)
```
Source: https://www.latent.space/p/flue-2

useSkill()
useTool()
useSubagent()
(+ 13 further built-in hooks, unnamed in this source; custom hooks
also supported)
```

## Cross-References

### Cross-reference verification notes
`blog-latentspace-ainews-meta-harness-summer.md`, `blog-latentspace-vercel-andrew-qu-eve.md`,
and `blog-vercel-eve-extensions.md` were re-read in full during this extraction per MINER.md
§4b, and every claim number cited below was located and confirmed against that note's own
numbered claims in document order before writing this section.

- **Corroborates**:
  - `blog-latentspace-vercel-andrew-qu-eve.md` Claim 4 ("agents are a new type of
    software... you need different primitives for context, tools, resumability and
    long-running work") and Claims 2–3 (eve's origin as an internal-tool-turned-framework):
    this source's Claim 4 ("there is no agent without a harness") is a second, independent
    framework author arriving at harness-centrality as the core design commitment for an
    agent framework — Schott's own words even name `eve` directly as sharing "that same
    take that a harness is built-in" (Claim 7 above), making this one of the few cases in
    the corpus where two competing framework authors explicitly agree on their shared
    defining principle rather than the corpus inferring the parallel independently. Claim 9
    above (Flue's origin as an internal Astro-repo tool that grew into a general framework)
    is structurally the same "dogfooding produced the framework" narrative as that note's
    Claim 2 (eve emerging from v0's internal "paper cuts"), from a second, independent
    company.
  - `blog-latentspace-ainews-meta-harness-summer.md` Claim 1 ("a largely undocumented
    lineage of 'meta-harnesses'... Cloudflare's Flue, and then Vercel's Eve and
    HarnessAgent") explicitly named "Cloudflare's Flue" as part of an asserted,
    self-described "little undocumented" lineage and flagged it as "a pointer to go
    research... rather than a settled claim." This source is exactly that research: a
    detailed, first-party account of Flue directly from its creator. It corroborates that
    Flue is a real, actively developed harness-first framework (as that note's lineage
    implied) — see Contradicts/Complicates below for how it also complicates that note's
    "meta-harness" framing specifically.

- **Contradicts / Complicates**: None rises to a MINER.md §4a-filable contradiction, but one
  terminology tension and one definitional complication are worth flagging prominently:
  - **"Meta-harness" — definitional mismatch, not filed as a contradiction**: The AINews
    digest's Claim 1 groups "Cloudflare's Flue" into a lineage of tools it labels
    "meta-harnesses," and its own Guide Impact section recommends the guide "disambiguate
    which sense" of that already-overloaded term is meant. This source's Claim 11 supplies
    exactly that disambiguation for Flue specifically, directly from Schott: when explicitly
    asked how Flue relates to "meta-harnesses" like Databricks' Omnigent and Exo, Schott
    does *not* claim Flue is one — he says the term is unsettled at this stage, and that
    Flue deliberately does *not* pursue a common cross-harness API, because "the framework
    [Flue] and the harness are very intertwined." This is not two sources disagreeing about
    a fact (both agree Flue exists and is harness-first); it is evidence that the AINews
    digest's casual grouping of Flue under "meta-harness" does not match how Flue's own
    creator uses or accepts that term. No contradiction issue filed: the digest's claim was
    already self-graded `anecdotal` and explicitly flagged as unverified in its own note: this
    is a pointer being resolved by first-party evidence, not two argued positions in
    opposition (same treatment the eve interview note gave this identical situation for
    `eve`'s meta-harness-lineage membership).
  - **"Hooks" — terminology collision with `eve`'s unrelated sense of the same word**:
    `blog-vercel-eve-extensions.md` Claim 1 documents that `eve` extensions bundle "tools,
    channels, connections, skills, schedules, subagents, instruction fragments, and hooks"
    as one of eight *packaged capability types*, and that note's Source Context describes
    `eve`'s hooks (via `eve.dev/docs/guides/hooks`) as narrowing tool-result types (a
    `toolResultFrom` mechanic) — i.e., `eve`'s "hooks" are a file-based convention
    (a `hooks/` directory) for post-processing tool output. This is a substantively
    different concept from Flue's "Agent Hooks" (Claims 1–2 above): React-style, in-function
    composition primitives (`useSkill()`, `useTool()`, `useSubagent()`) that an agent
    function calls to manage its own state and attach capabilities as it re-renders each
    turn. Both frameworks use the word "hooks" for a load-bearing primitive, but the two
    are not interchangeable concepts — one is a tool-output-narrowing convention, the other
    is a React-inspired composition/state-management primitive. The guide should not treat
    "framework X has hooks" as a comparable feature across `eve` and Flue without this
    distinction.

- **Extends**: `blog-latentspace-vercel-andrew-qu-eve.md` — that note documents `eve`'s
  design philosophy and origin from its own lead engineer but had no comparable account
  from a competing framework author. This source extends the corpus's harness-first-
  framework coverage with a second, independent practitioner's account, including a
  direct (and generous) assessment of `eve` from a competitor (Claim 7) that the `eve`
  note itself could not supply.

- **Novel**:
  - **React-style hook composition as an agent-framework primitive** (Claims 1–2): no
    other corpus source describes an agent framework using a component-hook-style API
    (`useSkill()`, `useTool()`, `useSubagent()`) as its foundational composition model, or
    an agent-as-function "re-renders on every turn" execution semantics.
  - **"There is no agent without a harness" as an explicit, absolute design axiom**
    (Claim 4): stronger and more definitional in phrasing than the comparable "agents need
    different primitives" framing in the `eve` interview note.
  - **Pi as a named, separately-maintained minimal harness underlying an opinionated
    framework** (Claim 5): the two-layer minimal-harness/opinionated-framework split
    (analogous to Vite/Astro) is a new architectural pattern in the corpus.
  - **A framework author's explicit refusal to pursue cross-harness "meta-harness"
    interoperability, and his reasoning why** (Claim 11): no other corpus source documents
    a harness-first framework author explicitly declining this direction and explaining the
    product-strategy reasoning (avoiding "muddling the story").
  - **File-based routing named as a specific, abandoned anti-pattern for agent frameworks**
    (Claim 6): the specific failure mode (porting web-framework routing metaphors to
    agent frameworks, then discovering most enterprise deployments are architecturally
    "one agent") is new to the corpus.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add Flue's hook-based composition model (Claims 1–2)
  as a concrete, named example of a framework treating agent composition as a first-class,
  runtime-dynamic concern (attach a skill/tool/subagent via a function call inside an
  agent function that re-renders each turn) rather than a static configuration surface
  (a fixed tool list, a CLAUDE.md file, a settings.json). This is architecturally distinct
  from the CLAUDE.md/hooks/skills/MCP taxonomy the guide currently documents for Claude
  Code — it is a framework-level (not CLI-level) composition primitive, and should be
  presented as a different point in the design space, not a replacement for the CLI-based
  patterns.

- **Chapter 02 (Harness Engineering)**: Add "there is no agent without a harness" (Claim 4)
  as a second, independent framework author's articulation of harness-centrality, alongside
  the existing `eve` citation — and explicitly note the two frameworks' own creators agree
  with each other on this point (Claim 7's "Eve... had that same take that a harness is
  built-in"), which is stronger corroboration than two sources independently arriving at
  similar language without cross-acknowledgment.

- **Chapter 02 (Harness Engineering)**: Add Claim 6 (file-based routing as an abandoned
  anti-pattern) as a specific cautionary example for anyone designing a new agent framework
  by porting web-framework conventions directly: the unit of composition in an agent
  framework may not map to "one file = one route" the way it does for a website, because
  (per this practitioner's customer base) enterprise agent deployments are often
  architecturally singular.

- **Chapter 02 (Harness Engineering) — terminology hygiene**: When the guide compares
  `eve` and Flue (or cites "hooks" as a feature of either), it must use the terminology
  distinction surfaced above: `eve`'s "hooks" (a packaged, file-based tool-result-narrowing
  convention) and Flue's "Agent Hooks" (React-style composition/state primitives) are not
  the same concept despite the shared name.

- **Chapter 02 (Harness Engineering) — meta-harness disambiguation**: When citing the
  meta-harness lineage from `blog-latentspace-ainews-meta-harness-summer.md`, note that
  Flue's own creator does not accept the "meta-harness" (cross-harness-interoperability)
  framing for Flue specifically (Claim 11) — the guide should not present Flue as a
  self-identified meta-harness without this caveat.

## Extraction Notes

- WebFetch's initial summarizing pass produced only a short bulleted overview, consistent
  with the pattern already documented in `blog-latentspace-vercel-andrew-qu-eve.md`'s and
  `blog-latentspace-ainews-meta-harness-summer.md`'s Extraction Notes. Per those notes'
  precedent, the page's embedded Substack JSON payload (`window._preloads` →
  `post.body_html`) was recovered directly (via `curl` with a browser user agent, then
  parsed and HTML-stripped) to guarantee every `Quote` field below was copied
  character-for-character from the source, not reconstructed from a summarizing pass. The
  post is not paywalled (`audience: everyone` in its own metadata) and the full 1,436-word
  body was recovered this way.
- No linked sub-pages were followed: unlike `blog-vercel-eve-extensions.md` (which follows
  4 linked docs pages), this article contains no inline links to Flue's own documentation,
  the Flue 1/2 launch posts it quotes from, or Pi's repository — nothing met MINER.md §1's
  "follow up to 5 linked pages" bar because the article itself contains no such links in the
  recovered body HTML.
- Three duplicate Prospector triage comments exist on issue #3145 (consistent chapter
  guidance — Ch02/Ch03 — with varying novelty language across passes); all three were read
  and reconciled into the single extraction above, the same situation documented in
  `blog-latentspace-databricks-agent-clouds.md`'s and
  `blog-latentspace-ainews-meta-harness-summer.md`'s Extraction Notes.
- Overall confidence rated **emerging**: this is a single first-party interview with the
  framework's own creator (high credibility for design-philosophy and origin-story claims,
  several of which are individually rated `settled` where they are unambiguous factual
  statements — e.g., Claims 1, 2, 4, 12, 13), but the source contains no independent
  verification, no benchmark or adoption data, no named production customers, and several
  claims (6, 9, 10, 11) are self-reported narrative/strategy rather than externally checkable
  fact. Flue 2 is also a very recent (August 2026), fast-iterating release — the framework's
  API and roadmap claims (e.g., Claim 12's "no managed hosting on the roadmap") should be
  treated as a snapshot, not a durable guarantee.
