---
source_url: https://addyosmani.com/blog/good-spec/
source_type: blog-post
title: "How to Write a Good Spec for AI Agents"
author: Addy Osmani
date_published: 2026-01-13
date_extracted: 2026-04-08
last_checked: 2026-04-08
status: current
confidence_overall: emerging
issue: "hi-e93.2"
---

# Addy Osmani: How to Write a Good Spec for AI Agents

> A concrete SPEC.md template with six required sections and a three-tier
> boundary system. Treats the spec as a living, persistent document that
> survives across sessions and anchors the agent on re-entry — making it the
> primary artifact for "specs/plans as compressed context" in Ch04. Includes a
> warning about "the curse of instructions" (the model's adherence drops as
> instruction count grows).

## Source Context

- **Type**: blog-post
- **Author credibility**: Addy Osmani is an engineering lead at Google
  Chrome, the author of multiple O'Reilly books on web performance, and one
  of the most-followed developer voices in the JavaScript community. The post
  was republished on the O'Reilly Radar (Feb 20, 2026), giving it
  editorial endorsement. Osmani is already in our corpus via
  "blog-addyosmani-code-agent-orchestra"; this is a distinct, more recent
  post specifically about specs.
- **Scope**: How to structure a spec file (SPEC.md or AGENTS.md / CLAUDE.md /
  similar) so the agent has unambiguous context to work from. Covers the
  six-section template, the three-tier boundary system, the "specify → plan
  → tasks → implement" workflow, the vagueness failure mode, and the
  "curse of instructions" that limits how much you can pile in. Does NOT cover
  hooks, settings.json, MCP configuration, or runtime context management.

## Extracted Claims

### Claim 1: A good spec has six required sections
- **Evidence**: Author's prescriptive template, distilled from his own
  practitioner work and the broader spec-driven development discourse.
- **Confidence**: editorial (single-author prescription, but defensibly
  comprehensive)
- **Quote**: "1. Commands: Put executable commands early... 2. Testing: How
  to run tests, what framework you use... 3. Project structure: Where source
  code lives... 4. Code style: One real code snippet showing your style...
  5. Git workflow: Branch naming, commit message format... 6. Boundaries:
  What the agent should never touch."
- **Our assessment**: This template is defensible. The six sections cover
  what an agent typically discovers by file-spelunking on each fresh session
  — and discovery is expensive in tokens (Bswen's Claim 6 in a separate
  source: conversation is only 4% of typical context, the rest is
  boilerplate the agent has to figure out). A SPEC.md that front-loads
  commands, tests, structure, style, git workflow, and boundaries is
  exactly the "compressed context" Ch04 wants to recommend. Use this six-
  section template as the canonical Ch04 example.

### Claim 2: Three-tier boundary system: Always do / Ask first / Never do
- **Evidence**: Author's prescriptive structure for the Boundaries section.
- **Confidence**: editorial
- **Quote**: "✅ Always do: Actions the agent should take without asking...
  ⚠️ Ask first: Actions that require human approval... 🚫 Never do: Hard stops."
  Example: "Never commit secrets or API keys."
- **Our assessment**: The three-tier model is a useful clarification of
  "boundaries." It distinguishes between affirmative defaults (Always),
  human-in-the-loop pauses (Ask first), and absolute prohibitions (Never).
  Cross-reference with failure-claudemd-ignored-compaction (separate source):
  the failure report shows that "Never" rules in CLAUDE.md are followed
  ~70-80% of the time, so the "Never" tier should be backed by hooks or
  settings.json wherever possible. Osmani's tiers describe intent; the
  guide should explain how to enforce each tier with actual machinery.

### Claim 3: Save the spec as SPEC.md and feed sections to the agent as needed
- **Evidence**: Author's recommended workflow.
- **Confidence**: emerging
- **Quote**: "Once approved, save this spec (e.g. as SPEC.md) and feed
  relevant sections into the agent as needed... the spec file persists between
  sessions, anchoring the AI whenever work resumes on the project."
- **Our assessment**: This is the load-bearing claim for "specs as compressed
  context." The spec is not a one-shot prompt; it is a persistent artifact
  that the agent re-reads at the start of every session. This is what makes
  it cheaper than building context conversationally — a 200-line SPEC.md is
  ~600-800 tokens, vs the thousands of tokens an agent burns in discovery.
  Pair with research-wasnotwas-context-compaction Claim 5 (Claude Code
  re-injects the active plan file after compaction): if the spec is the plan,
  the harness will preserve it for you.

### Claim 4: Most agent files fail because they're too vague
- **Evidence**: Author's stated failure observation from reviewing many
  practitioner CLAUDE.md / AGENTS.md files.
- **Confidence**: emerging
- **Quote**: "Most agent files fail because they're too vague. 'Build me
  something cool' or 'Make it work better' gives the agent nothing to anchor
  on."
- **Our assessment**: This is the diagnostic for the failure mode. Vague specs
  underperform empty specs because they take up budget without giving the
  agent traction. Use as the framing for "what makes a spec actually useful."

### Claim 5: The "curse of instructions" — adherence drops as instruction count grows
- **Evidence**: Author's empirical observation, framed as a known
  phenomenon. Echoes the long-prompt failure modes documented in
  failure-claudemd-ignored-compaction (separate source) and ETH Zurich's
  AGENTbench results in paper-gloaguen-agentsmd-effectiveness (separate
  source).
- **Confidence**: emerging
- **Quote**: "As you pile on more instructions or data into the prompt, the
  model's performance in adhering to each one drops significantly... even
  GPT-4 and Claude struggle when asked to satisfy many requirements
  simultaneously."
- **Our assessment**: This is the brake on the "make the spec exhaustive"
  impulse. There is a U-curve: too vague is bad (Claim 4), too verbose is
  also bad (Claim 5). Recommended response: "Decomposing complex requirements
  into sequential, simple instructions." This connects directly to session
  segmentation in Ch04 — split the work, don't pile it into one prompt.

### Claim 6: Spec-driven workflow has four phases: Specify → Plan → Tasks → Implement
- **Evidence**: Author's process recommendation.
- **Confidence**: editorial
- **Quote**: "The spec drives the implementation, checklists, and task
  breakdowns. Your primary role is to steer; the coding agent does the bulk
  of the writing."
- **Our assessment**: This is the loop Ch04 should describe. It is also
  structurally similar to the Superpowers plugin's brainstorm → plan →
  implement → review (separate source: Dewhurst). The two patterns differ in
  vocabulary but agree that planning is a distinct phase that produces a
  concrete artifact (a spec or a design doc) before any code is written.

### Claim 7: Iterate on the spec interactively before implementation; use Plan Mode
- **Evidence**: Author's recommendation, with Claude Code's Plan Mode as the
  concrete enabling feature.
- **Confidence**: emerging
- **Quote**: "Before writing any code, review and refine the AI's spec. Make
  sure it aligns with your vision and correct any hallucinations or off-target
  details... Tools like Claude Code offer a Plan Mode... that restricts the
  agent to read-only operations... refine the plan until there's no room for
  misinterpretation. Only then do you exit Plan Mode."
- **Our assessment**: Plan Mode is the mechanism that operationalizes Claim 6.
  Use this as the concrete tool recommendation for the "specify before you
  implement" workflow. Note for the guide: Plan Mode is Claude Code-specific;
  Cursor and other tools have analogous features under different names.

## Concrete Artifacts

The post includes a concrete spec template:

```markdown
# Project Spec: My team's tasks app

## Objective
- Build a web app for small teams to manage tasks...

## Tech Stack
- React 18+, TypeScript, Vite, Tailwind CSS
- Node.js/Express backend, PostgreSQL, Prisma ORM

## Commands
- Build: `npm run build`
- Test: `npm test`
- Lint: `npm run lint --fix`

## Project Structure
- `src/` – Application source code
- `tests/` – Unit and integration tests
- `docs/` – Documentation

## Boundaries
- ✅ Always: Run tests before commits
- ⚠️ Ask first: Database schema changes
- 🚫 Never: Commit secrets
```

This is the cleanest minimal spec we have seen. Use as the canonical
Ch04 example. It is short enough (~25 lines) to fit comfortably under
Bswen's 100-300 line CLAUDE.md guidance.

## Cross-References

- **Corroborates**: blog-french-owen-coding-agents-feb-2026 ("externalize
  context to filesystem" — Osmani's SPEC.md is the concrete file the
  agent reads instead of rediscovering)
- **Corroborates**: research-wasnotwas-context-compaction Claim 5
  (Claude Code re-injects the active plan file after compaction — Osmani's
  SPEC.md, if treated as the plan, is preserved by the harness)
- **Corroborates**: paper-gloaguen-agentsmd-effectiveness (developer-written
  AGENTS.md gives marginal improvement; Osmani's six-section template is the
  prescriptive instance of "well-written developer-written AGENTS.md")
- **Corroborates**: failure-claudemd-ignored-compaction (Claim 5: "the
  curse of instructions" provides a mechanistic explanation for the
  observed degradation in CLAUDE.md adherence as files grow)
- **Extends**: blog-addyosmani-code-agent-orchestra (Osmani's earlier piece
  framed orchestration; this one provides the specific artifact the
  orchestrator manages)
- **Contradicts**: practitioner-supabase-supabase-js (931-line CLAUDE.md
  exceeds the implicit "decompose, don't pile in" guidance — though
  Supabase has the resources to make a long file work; for solo and
  small-team users, Osmani's six-section template is a safer default)

## Guide Impact

- **Chapter 04 (Specs/plans as compressed context)**: This is the primary
  source for the section. Use the six-section template as the canonical
  example. Use Claim 3 (spec persists between sessions) as the framing for
  why specs ARE context engineering, not separate from it.

- **Chapter 04 (Context as budget)**: Cite Claim 5 (the "curse of
  instructions") as the brake on cramming more into the spec. There is a
  U-curve. The cheapest spec that conveys intent is the best spec.

- **Chapter 02 (Harness Engineering)**: The six-section template should be
  the recommended starting point for new CLAUDE.md / AGENTS.md / SPEC.md
  files. Replace any current Ch02 example with Osmani's template if Osmani's
  is more concrete.

- **Chapter 03 (Safety and Verification)**: The three-tier boundary system
  (Always / Ask first / Never) maps to enforcement mechanisms: Always is
  a default behavior, Ask first is a hook gate, Never is a settings.json
  permission denial. Use Osmani's tiers as the conceptual frame, then
  point to Ch03 for the enforcement machinery.

- **Chapter 01 (Daily Workflows)**: The Specify → Plan → Tasks → Implement
  loop is one of several spec-first workflows worth describing. Cross-cite
  with the Superpowers brainstorm → plan → implement → review pattern
  (Dewhurst, separate source) — both agree planning should produce a
  written artifact before any code.

## Extraction Notes

- The post is dense with prescriptive material; we extracted 7 claims, but
  there are more (e.g., on README vs SPEC distinction, on iterative
  refinement, on the Tasks layer between Plan and Implement). If Ch04 needs
  more depth on workflow, return to the source.
- Osmani's "Plan Mode" recommendation is Claude Code-specific. The guide
  should generalize: any tool that allows read-only exploration before
  writes is implementing the same pattern under different names.
- Osmani is a vendor-adjacent author (Google) but his Ch04-relevant claims
  are tool-agnostic and grounded in workflow advice, not Google-specific
  features. Treat as practitioner content, not vendor marketing.
- The "curse of instructions" framing is borrowed from prompting research
  but Osmani applies it specifically to spec / AGENTS.md files. Worth
  citing as the mechanism behind the failure-claudemd-ignored-compaction
  observations.
