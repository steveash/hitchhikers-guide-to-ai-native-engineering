---
source_url: https://developers.googleblog.com/enable-on-demand-expertise-with-agent-skills-in-genkit-go/
source_type: blog-post
title: "Enable on-demand expertise with Agent Skills in Genkit Go"
author: Daniela Petruzalek (Senior Developer Relations Engineer, Google)
date_published: 2026-07-31
date_extracted: 2026-08-01
last_checked: 2026-08-01
status: current
confidence_overall: emerging
issue: "#2388"
---

# Enable on-demand expertise with Agent Skills in Genkit Go

> Google's official Genkit Go implementation guide for Agent Skills — the first source in our corpus to document the agentskills.io progressive-disclosure lifecycle (Discovery → Activation → Execution) at the middleware-hook level (WrapModel/WrapTool/WrapGenerate), with two complete runnable Go examples.

## Source Context

- **Type**: blog-post (Google Developers Blog, July 31, 2026; practitioner implementation tutorial)
- **Author credibility**: Daniela Petruzalek is a Senior Developer Relations Engineer at Google, writing an official first-party tutorial on developers.googleblog.com for the Genkit Go framework her team maintains. High credibility for Genkit-specific APIs, middleware semantics, and code correctness (the post links two complete runnable example repos). Not an independent third-party evaluation — no adoption data, no comparison to how other frameworks implement the same spec, and no discussion of failure modes or limitations of the pattern.
- **Scope**: Covers how to implement the agentskills.io Agent Skills open specification inside Genkit Go: the SKILL.md file/frontmatter format, the three-stage activation lifecycle (Discovery, Activation, Execution), the underlying Genkit middleware hooks (WrapModel, WrapTool, WrapGenerate) that make on-demand loading possible, and two worked examples (a recipe-generation CLI and a multi-modal art-restoration app using Gemini 3.1 Flash Image). Does NOT cover: security or trust concerns about installing third-party skills, cost/latency benchmarks quantifying the token savings, skill authoring best practices (Gotchas sections, description-writing guidance), skill distribution/versioning, or how Genkit's implementation compares to Claude Code's or GitHub Copilot's skill-loading mechanics.

## Extracted Claims

### Claim 1: Agent Skills operate on "progressive disclosure" — skill content is revealed to the model only when needed, not loaded persistently

- **Evidence**: First-party definitional statement framing the entire feature.
- **Confidence**: settled (definitional claim about how the shipped feature works)
- **Quote**: "Agent skills operate on a principle called progressive disclosure, meaning information will only be revealed to the model when it is necessary."
- **Our assessment**: This is the same progressive-disclosure principle documented in `blog-anthropic-claude-code-skills-lessons.md` (Claim 5: "You should think of the entire file system as a form of context engineering and progressive disclosure"), but here it names the mechanism as a formal, spec-level principle of the agentskills.io standard rather than an internal design recommendation. That two independently-authored implementations (Anthropic's Claude Code and Google's Genkit Go) converge on the same architectural principle strengthens the case that progressive disclosure is a property of the open specification itself, not a per-vendor design choice.

### Claim 2: Persistently loading all standard operating procedures and reference material into context is explicitly framed as unsustainable — it consumes tokens, dilutes focus, and increases error likelihood

- **Evidence**: First-party rationale statement explaining why progressive disclosure exists.
- **Confidence**: settled (stated as the design motivation for the shipped feature)
- **Quote**: "Loading every standard operating procedure, reference guide, and document into the persistent context window is not sustainable: it consumes valuable tokens, dilutes the model's focus, and increases the likelihood of incorrect responses."
- **Our assessment**: This is a specific, named three-part cost model for context bloat (token cost, focus dilution, error rate) — more granular than most sources, which mention only token/cost overhead. It corroborates `blog-anthropic-claude-code-skills-lessons.md` Claim 14 (repo-checked skills "add a little bit to the context of the model" at scale) but adds the "dilutes the model's focus" and "increases likelihood of incorrect responses" mechanisms explicitly, which that source leaves implicit.

### Claim 3: Agent Skills package specialized expertise into discoverable capabilities that the agent loads only when needed

- **Evidence**: First-party definitional statement of what an Agent Skill is, in the context of the open specification.
- **Confidence**: settled
- **Quote**: "The agent skills standard lets developers package specialized expertise into discoverable capabilities that the agent loads only when needed."
- **Our assessment**: Functionally identical framing to `docs-github-copilot-agent-skills-cli.md` Claim 1 ("Agent skills are portable sets of instructions, scripts, and resources that teach AI agents how to perform specific tasks") — both GitHub's and Google's descriptions independently converge on "discoverable, on-demand-loaded capability packages" as the definition of a skill. This is now the third major agent framework (after Claude Code and GitHub Copilot) in our corpus implementing the agentskills.io spec, following the pattern the Prospector's triage comment flagged.

### Claim 4: The SKILL.md frontmatter's description field is the primary trigger the middleware uses to decide when to activate a skill

- **Evidence**: First-party technical statement about the activation mechanism.
- **Confidence**: settled (mechanism stated definitively about the shipped implementation)
- **Quote**: "The YAML frontmatter description acts as the primary trigger for the middleware."
- **Our assessment**: This directly corroborates `blog-anthropic-claude-code-skills-lessons.md` Claim 10 ("the description field is not a summary, it's a description of when to trigger this skill"). Two independent implementations (Genkit Go, Claude Code) both use the description field as the activation trigger rather than as human-readable metadata. This is strong convergent evidence that "write descriptions as trigger conditions, not summaries" is a spec-level requirement for any agentskills.io-compliant skill, not vendor-specific advice.

### Claim 5: Skill activation proceeds through three distinct stages — Discovery (metadata scan into system prompt), Activation (description match triggers a `use_skill` tool call), and Execution (full content + bundled resources loaded into context)

- **Evidence**: First-party technical description of the middleware's internal lifecycle, stated as three named, sequential stages.
- **Confidence**: settled (mechanism described definitively for the shipped implementation)
- **Quote (Discovery)**: "When initializing Genkit with the skills middleware, the system scans your configured SkillPaths for SKILL.md files and injects their metadata into the system prompt."
- **Quote (Activation)**: "When a user request matches a skill's description, Genkit calls the use_skill tool to retrieve the specific instructions needed for the current task."
- **Quote (Execution)**: "The full content of the SKILL.md file, along with access to bundled resources like scripts and references, is loaded into the active context."
- **Confidence**: settled
- **Our assessment**: This is the first source in our corpus to name and describe the underlying activation lifecycle as three discrete stages with a concrete mechanism (a `use_skill` tool call triggers the transition from Discovery to Execution). Prior corpus sources (Anthropic, GitHub) describe the effect of progressive disclosure but not the mechanism by which a model transitions from "sees metadata" to "sees full content" — here it's explicit: activation is itself a tool call the model makes, not an automatic context-injection event. This is a concrete implementation detail that generalizes well to explaining "how skill loading actually works under the hood" regardless of which agent host is used.

### Claim 6: The skills middleware is implemented on top of three generic Genkit middleware hooks — WrapModel, WrapTool, and WrapGenerate — each firing at a different granularity

- **Evidence**: First-party architecture description with per-hook firing semantics.
- **Confidence**: settled (architecture stated definitively for the shipped framework)
- **Quote (WrapModel)**: "Model Wrapper (WrapModel): Fires once per model API call inside an iteration and handles logic about the model call itself, such as retry, fallback, and caching."
- **Quote (WrapTool)**: "Tool Wrapper (WrapTool): Fires once per tool execution and may run concurrently for parallel tool calls in the same iteration."
- **Quote (WrapGenerate)**: "Generate Wrapper (WrapGenerate): Fires once per tool-loop iteration (N tool turns means N+1 invocations) and handles logic that needs to see the whole conversation, such as rewrites, system-prompt injection, and message accumulation."
- **Our assessment**: This is a novel, concrete architectural detail not present anywhere else in our corpus: skill loading is implemented as system-prompt injection at the WrapGenerate layer (whole-conversation granularity), not as a special-cased feature. This means the same middleware layer that Genkit uses for retries, fallback, and caching (WrapModel) is generically reusable for injecting skill content — a design that could inform how teams building custom agent harnesses on other frameworks structure their own on-demand context-loading layer, by decomposing it into "per-call," "per-tool," and "per-conversation-turn" hook granularities rather than one monolithic mechanism.

### Claim 7: Registering skills in Genkit Go is a single middleware declaration pointing at a directory of skill folders

- **Evidence**: First-party code snippet showing the exact registration call.
- **Confidence**: settled (exact API surface shown)
- **Quote**: `ai.WithUse(&middleware.Skills{SkillPaths: []string{"./skills"}})`
- **Our assessment**: Low ceremony for adoption — a single middleware option pointed at a skills directory. This mirrors Claude Code's `./.claude/skills` and GitHub Copilot's `.github/skills/` conventions (per `blog-anthropic-claude-code-skills-lessons.md` and `docs-github-copilot-code-review-skills-mcp-tier.md`): every implementation of the spec we've seen so far uses a filesystem directory of folders as the skill source of truth, configured via a single path parameter.

### Claim 8: Token efficiency is framed as the primary named benefit — Genkit loads only skill metadata initially and defers detailed instructions until the skill activates

- **Evidence**: First-party benefit statement.
- **Confidence**: settled (restates the mechanism as a benefit)
- **Quote**: "Token efficiency: Genkit loads only the skill's metadata initially, injecting detailed instructions only when the skill becomes active."
- **Our assessment**: The article asserts token efficiency as a benefit but — per Extraction Notes below — provides no quantitative measurement (no token counts, no cost comparison, no benchmark) to substantiate the magnitude of savings. This is consistent with the rest of our corpus's agent-skills coverage: every source we have asserts progressive disclosure saves tokens, but none quantifies by how much. This remains a gap for the guide to flag rather than resolve.

### Claim 9: The recipe-flow example demonstrates basic on-demand loading by activating different skills (`banana-bread` vs. `cheese-bread`) based on user input

- **Evidence**: First-party example description plus a public example repository.
- **Confidence**: settled (concrete, verifiable example with linked source code)
- **Quote**: (no direct quote; see Concrete Artifacts for repo details) The example demonstrates "basic on-demand loading."
- **Our assessment**: A minimal but concrete illustration: the activation mechanism (Claim 5) is directly observable by giving the same agent two mutually-exclusive skills and varying the input keyword ("cheese" vs. no "cheese") to show only the relevant skill's full content loads. Useful as a template for teams wanting a minimal reproducible test of skill-activation behavior in their own harness.

### Claim 10: The art-restoration example shows skills orchestrating a non-deterministic, multi-modal task by choosing among three specialized skills (drawings, paintings, photography) using Gemini 3.1 Flash Image

- **Evidence**: First-party example description plus a public example repository; names the specific model used.
- **Confidence**: emerging (concrete example exists and is linked, but no evaluation of restoration quality or comparison to a non-skill baseline is given)
- **Quote**: (no direct quote for the model name/skill list; see Concrete Artifacts) The example demonstrates using skills to allow "agents to orchestrate and apply specialized instructions to non-deterministic tasks."
- **Our assessment**: This is the more architecturally interesting of the two examples: it shows skills applied to a generative, non-deterministic domain (image restoration) rather than a simple text-generation branch (the recipe example). The three-skill structure (drawings/paintings/photography) demonstrates skills as a routing mechanism for domain-specific processing instructions in a multi-modal pipeline — relevant to any team building agents that must apply different specialized processing logic depending on input media type or domain, not just text-based task routing.

## Concrete Artifacts

### SKILL.md directory structure (Genkit Go)

```
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
```
Source: "Enable on-demand expertise with Agent Skills in Genkit Go" (Google Developers Blog, 2026-07-31)

### SKILL.md frontmatter example

```yaml
---
name: adr-template
description: Activate this skill when proposing significant architectural changes, documenting codebase refactorings, or resolving design/technical debates. Use this skill to author and maintain Architecture Decision Records (ADRs) to preserve engineering context.
license: Apache-2.0
metadata:
  author: example-org
  version: "1.0"
---
```
Source: same article. Note the description field is written as a trigger condition ("Activate this skill when...") rather than a human summary — directly consistent with Claim 4/Claim 10 in `blog-anthropic-claude-code-skills-lessons.md`.

### Middleware registration (Go)

```go
ai.WithUse(&middleware.Skills{SkillPaths: []string{"./skills"}})
```
Source: same article.

### Three-stage activation lifecycle

```
1. Discovery:  Genkit scans SkillPaths for SKILL.md files at init;
               injects only their metadata into the system prompt.
2. Activation: A user request matches a skill's description; Genkit
               calls a use_skill tool to retrieve the full instructions.
3. Execution:  Full SKILL.md content + bundled resources (scripts,
               references) load into the active context.
```
Source: same article, "Discovery," "Activation," "Execution" sections.

### Middleware hook granularities

```
WrapModel:    fires once per model API call within an iteration
              (retry, fallback, caching)
WrapTool:     fires once per tool execution, may run concurrently
              for parallel tool calls in the same iteration
WrapGenerate: fires once per tool-loop iteration (N tool turns =
              N+1 invocations); sees the whole conversation
              (rewrites, system-prompt injection, message
              accumulation) — this is where skill content injection
              happens
```
Source: same article.

### Example repositories

```
Recipe flow example (banana-bread / cheese-bread skills):
https://github.com/GoogleCloudPlatform/devrel-demos/tree/main/frameworks/genkit/go-skills/example01

Art restoration example (drawings / paintings / photography skills,
Gemini 3.1 Flash Image):
https://github.com/GoogleCloudPlatform/devrel-demos/tree/main/frameworks/genkit/go-skills/example02
```
Source: same article, linked example repos.

### Related resources cited by the article

```
Agent Skills open specification: https://agentskills.io/
Genkit "Getting Started" docs: genkit.dev
Genkit middleware docs: genkit.dev
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-claude-code-skills-lessons.md` (Claim 5, Claim 10): Both sources independently converge on progressive disclosure as the organizing principle for skill folders, and on the description field as a machine-readable trigger rather than a human summary. Two independently engineered implementations (Anthropic's Claude Code, Google's Genkit Go) reaching the same design conclusions is strong evidence these are properties of the agentskills.io specification itself, not vendor idiosyncrasies.
  - `docs-github-copilot-agent-skills-cli.md` (Claim 1, Claim 5): GitHub's definition of skills as "portable sets of instructions, scripts, and resources that teach AI agents how to perform specific tasks" and its claim that the open spec at agentskills.io spans multiple agent hosts is now independently confirmed by a third implementation. This source is the first in our corpus to actually document what a non-Claude, non-Copilot implementation of the same spec looks like at the code level.

- **Contradicts**: None identified. No claim in this source conflicts with existing corpus notes on skills.

- **Extends**:
  - `docs-github-copilot-agent-skills-cli.md`: That note documents the package-manager/distribution layer for skills (`gh skill install`, SHA pinning, provenance) but explicitly states it does not cover "how skill resolution works" mechanically. This source fills that specific gap for one implementation: the Discovery/Activation/Execution lifecycle and the `use_skill` tool-call mechanism are the missing "how it actually works" detail that note flagged as absent.
  - `blog-anthropic-claude-code-skills-lessons.md`: That note documents skill *design* (Gotchas sections, config.json, memory patterns) from Claude Code's perspective but does not describe the underlying request/response mechanics of activation. This source's middleware hook breakdown (WrapModel/WrapTool/WrapGenerate) is a concrete architectural model for how "system-prompt injection" (mentioned only in passing in the Anthropic post) is actually implemented.

- **Novel**:
  - **Middleware-hook-level architecture for skill loading**: No prior corpus source decomposes skill activation into generic middleware hooks (model-call-level, tool-call-level, conversation-level) reusable for other cross-cutting concerns (retry, fallback, caching). This is a transferable architectural pattern for teams building their own on-demand context-loading layer on any framework, not just Genkit.
  - **The `use_skill` tool-call as the explicit activation mechanism**: This is the first source in our corpus to state explicitly that skill activation is itself a tool call the model makes (not an automatic, framework-triggered context injection). This resolves an ambiguity left implicit in both the Anthropic and GitHub sources.
  - **A third independent agentskills.io implementation (Genkit Go / Google)**: Prior corpus coverage of the open spec was limited to Claude Code and GitHub Copilot. This is the first evidence of a third major agent framework (per the Prospector's characterization of the trusted feed) implementing the same spec, strengthening the case that agentskills.io is converging into a genuine cross-vendor standard rather than a two-vendor bilateral agreement.
  - **Multi-modal (non-text) skill routing example**: The art-restoration example (skills selecting among drawings/paintings/photography processing approaches for an image-generation task) is the first example in our corpus of skills applied outside a text-generation or CLI-automation context.

## Guide Impact

- **Chapter 02 (Harness Engineering — Skills)**: Add a note that the agentskills.io specification now has three independently-documented implementations in our corpus (Claude Code, GitHub Copilot, Genkit Go), and that all three converge on: (a) a filesystem directory of skill folders as the source of truth, (b) the YAML frontmatter `description` field as the activation trigger rather than a human-readable summary, (c) progressive disclosure (metadata-first, full-content-on-activation) as the loading strategy. Recommend that any team authoring skills for cross-host portability write `description` fields as explicit trigger conditions ("Activate this skill when...") per the SKILL.md example here, matching the pattern independently validated by Claude Code.

- **Chapter 02 (Harness Engineering — Skills Architecture)**: For teams building custom agent harnesses (not using an off-the-shelf agent framework), add the WrapModel/WrapTool/WrapGenerate decomposition as a reference architecture for implementing on-demand context loading: separate hooks for per-model-call, per-tool-call, and per-conversation-turn concerns, with skill/system-prompt injection living at the conversation-turn granularity. This is a concrete, generalizable pattern beyond Genkit specifically.

- **Chapter 08 (Resource Optimization)**: Cite this source alongside `blog-anthropic-claude-code-skills-lessons.md` Claim 14 for the token-cost argument behind progressive disclosure, but flag explicitly that no source in our corpus yet quantifies the token savings from progressive disclosure with a benchmark. This is a specific, named gap: if the guide makes a quantitative claim about skill-based context savings, it currently has no empirical backing in the corpus — only vendor assertions that the pattern saves tokens.

## Extraction Notes

1. **WebFetch could not return raw full-article HTML/markdown in one pass**; the source was extracted via four targeted WebFetch calls, each asking for specific verbatim quotes and code snippets (definitions/lifecycle stages; middleware hooks/code/benefits; repo links/frontmatter example/skill names; benchmarks/security discussion/doc links). Quotes reported as verbatim by WebFetch are reproduced here in quotation marks; anything WebFetch could only summarize is presented without quotation marks and flagged as paraphrase. The Assayer should spot-check all quoted passages against the live URL.
2. **No security/trust discussion in the source**: unlike `docs-github-copilot-agent-skills-cli.md` (which carries GitHub's explicit prompt-injection warning about third-party skills), this Genkit Go article does not address trust, verification, or supply-chain concerns for skills loaded from arbitrary `SkillPaths`. This is a gap worth noting if the guide cites this source for the technical mechanism — the security posture question (should teams `preview` skills before enabling them in `SkillPaths`?) is unanswered here.
3. **No quantitative benchmarks**: the article asserts "token efficiency" as a benefit (Claim 8) but provides no token counts, cost figures, or latency numbers. Confidence on that specific claim is capped at `settled` for the mechanism (it does load metadata-then-content) but the guide should not cite this source for a magnitude-of-savings number.
4. **Two linked example repos were not independently cloned/run** — their existence and URLs were confirmed via WebFetch extraction of the article's links, but code correctness was not independently verified by fetching the GitHub repos directly. If the guide wants to reference specific code from those examples beyond what's summarized here, a follow-up read of the repos is recommended.
5. **Followed no additional linked pages beyond the two GitHub example repos and the two doc links (agentskills.io, genkit.dev)** — none of those four were separately fetched in depth; they were only confirmed as citations within the primary article. Per MINER.md guidance to follow up to 5 linked pages, this was judged unnecessary since the primary article's own content (progressive disclosure architecture, code snippets, lifecycle description) was sufficiently deep and complete on its own, and the linked docs pages are general framework documentation rather than sources specific to this claim.
