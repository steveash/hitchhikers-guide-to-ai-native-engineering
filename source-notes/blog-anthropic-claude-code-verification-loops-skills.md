---
source_url: https://claude.com/blog/building-verification-loops-in-claude-code-with-skills
source_type: blog-post
title: "Building verification loops in Claude Code with skills"
author: Delba de Oliveira (member of the Claude Code team, Anthropic)
date_published: 2026-07-22
date_extracted: 2026-07-23
last_checked: 2026-07-23
status: current
confidence_overall: emerging
issue: "#2163"
---

# Building verification loops in Claude Code with skills

> A first-party Anthropic implementation guide that names four deployment
> patterns for turning manually-repeated verification checks into Claude
> Code skills — standalone, embedded, chained, and on-every-PR — with a
> minimal SKILL.md example, an internal-team chaining example
> (`/code-review` → `/simplify` → `/verify` → `/design`), and a six-step
> process for converting a manual check into a loop.

## Source Context

- **Type**: blog-post (claude.com/blog, published July 22, 2026; 5-minute
  read per the page's own reading-time label)
- **Author credibility**: Delba de Oliveira is credited at the end of the
  article as "a member of the Claude Code team" — a first-party Anthropic
  practitioner account, consistent with this corpus's other Claude Code
  team sources (e.g. `blog-anthropic-claude-code-skills-lessons.md`,
  written by Thariq Shihipar, also Claude Code team). No further
  biographical detail is given in the article itself.
- **Scope**: Covers the taxonomy of built-in Claude Code verification
  features (`/verify`, toolchain error handling, Code Review research
  preview, GitHub Actions, spec validation, Managed Agents rubrics), the
  process for writing a custom verification loop as a skill, one minimal
  SKILL.md example, and four deployment patterns (standalone, embedded,
  chained, on every PR) with a worked chaining example and a wrapper-skill
  code example. Closes with a six-step "verification loop creation
  process." Does NOT cover: skill design best practices in general (Gotchas
  sections, description-as-trigger, progressive disclosure — that is
  `blog-anthropic-claude-code-skills-lessons.md`'s territory), the `/verify`
  skill's internal implementation, benchmark or before/after metrics for
  any of the four deployment patterns, or the Managed Agents rubric
  mechanism beyond a one-sentence description.

## Extracted Claims

### Claim 1: A verification loop is defined as an iterative process where Claude checks its own work and attempts to fix it, distinct from the broader agentic loop of gathering context, taking action, and verifying results
- **Evidence**: Direct definitional statement early in the article, following a description of the general agentic loop.
- **Confidence**: emerging (first-party framing/definitional claim from the Claude Code team; not a measured or benchmarked finding)
- **Quote**: "In Claude Code, a verification loop is an iterative process where Claude checks and attempts to fix the work."
- **Our assessment**: This gives a precise, narrower definition than the general "agents check their work" framing already in the corpus — a verification loop is specifically the check-and-fix sub-cycle, not the whole gather/act/verify loop. This precision matters for the guide: "verification loop" as a term should refer to this fix-attempting iteration, not verification-as-a-single-check.

### Claim 2: Claude Code ships six built-in verification approaches: the `/verify` skill, toolchain error/warning handling, a Code Review research-preview multi-agent PR review service, GitHub Actions-triggered verification skills, markdown spec validation, and rubric-based grading with automatic rework in Claude Managed Agents (beta)
- **Evidence**: Enumerated list with a one-to-two-sentence description of each item, presented as the baseline a practitioner should understand before building custom loops.
- **Confidence**: settled (first-party enumeration of shipped/beta product features, not a measured claim)
- **Quote**: "/verify skill: builds, runs, and observes the changes in your application." / "Rubrics in Claude Managed Agents (beta): A managed agentic service that allows you to verify outcomes against a rubric using a separate grader agent. Failures loop back for rework automatically."
- **Our assessment**: This is a useful checklist for practitioners deciding whether to build a custom skill at all — the guidance elsewhere in the article ("Try out the built-in `/verify` skill first," Claim 9) explicitly tells readers to exhaust this list before writing a bespoke skill. The Code Review item is a first-party naming of the same "automated review pass on PRs" capability documented from the competing-tool side in `docs-github-copilot-code-review-skills-mcp-tier.md` (GitHub Copilot's code-review skills/MCP tiers) — see Cross-References.

### Claim 3: The first step in building a custom verification loop is writing down, in plain English, the checks a developer finds themselves repeating — "the way you'd hand it to a new teammate on day one" — including deterministic rules a generic linter cannot express
- **Evidence**: Direct process instruction with a worked example of a non-generic deterministic rule.
- **Confidence**: emerging (process recommendation, not independently measured)
- **Quote**: "Write the best-practices version in plain English, the way you'd hand it to a new teammate on day one." / "'Reject any migration that drops a column without a backfill step' is a deterministic rule no generic linter will catch but a project-specific one will."
- **Our assessment**: The migration/backfill example is a concrete illustration of the article's core distinction: verification loops exist to encode project-specific judgment that a generic toolchain (Layer 1 in the guide's existing verification stack) structurally cannot express, because a generic linter has no way to know your project's migration conventions. This is the same "capture what's specific to you, not what's generic" filter documented for CLAUDE.md content in `blog-anthropic-claude-code-skills-lessons.md` (Claim 7: "Skills should not restate capabilities Claude already has"), applied here to verification checks specifically rather than skills in general.

### Claim 4: The fastest way to turn a written-down check into a skill is the skill-creator plugin, which interviews the developer about their workflow via a single slash-command invocation
- **Evidence**: Named tool with an example invocation.
- **Confidence**: settled (first-party description of a shipped tool/workflow)
- **Quote**: "/skill-creator Create a skill for verifying frontend changes end-to-end. Interview me about my workflow."
- **Our assessment**: This is a concrete, actionable entry point distinct from hand-writing a SKILL.md from scratch (Claim 5) — the interview format lowers the barrier for practitioners who know what they check for but haven't formalized it into skill frontmatter and instructions.

### Claim 5: The simplest hand-written verification skill is a few lines of YAML frontmatter (name, description, allowed-tools) plus a short instruction body that names the specific check and the specific fix
- **Evidence**: A complete minimal worked example (`verify-log-hygiene`) checking that error logs include a request ID and never log the request body.
- **Confidence**: settled (directly reproduced from the article; a complete, self-contained code example)
- **Quote**: "The simplest possible verification skill is a few lines of frontmatter plus a body:" [followed by the `verify-log-hygiene` SKILL.md example — see Concrete Artifacts]
- **Our assessment**: This example is small enough to be a template practitioners can copy directly. Notably the body pairs detection with remediation in one instruction ("Report each violation with file:line, then fix it") — the skill is not just a checker, it is a check-and-fix loop consistent with Claim 1's definition of what makes something a "verification loop" rather than a static check.

### Claim 6: Standalone verification skills are invoked deliberately after an artifact exists, and earn their place for cross-cutting checks that do not apply to every change (security scans, accessibility audits, license-header verification); the signal that a team has outgrown standalone is running it after every single change
- **Evidence**: Direct description of the deployment pattern plus named example checks plus an explicit graduation signal.
- **Confidence**: emerging (design guidance from the Claude Code team, not independently measured)
- **Quote**: "A standalone skill earns its place for cross-cutting checks that don't apply every time: a pre-commit security scan, a pre-PR accessibility audit, license-header verification across a repo." / "The signal that you've outgrown standalone is when you're running it after every change. At that point, the procedure has earned a permanent home: embed it or chain it."
- **Our assessment**: This is the article's decision framework at its most concrete: standalone is explicitly a starting point, not an end state, for high-frequency checks. The "cost is that each invocation is still a turn you have to remember to take" framing names the specific weakness standalone has that the other three patterns solve.

### Claim 7: Embedded verification loops are appended directly to the body of the producing skill so the check fires automatically without being asked, but this pattern only works on skills the practitioner can edit — built-in skills and plugin-managed skills that get overwritten on update are explicitly off-limits
- **Evidence**: Direct description with a worked example (a `scaffold-component` skill with an appended eslint-and-fix step) and an explicit stated limitation.
- **Confidence**: emerging (design guidance from the Claude Code team)
- **Quote**: "Embedded only works on skills you can edit: ones you wrote yourself, or ones installed at a project level where the SKILL.md file is under your control. Built-in skills and plugin-managed skills (the kind that get overwritten on update) are off-limits for this pattern; for those, chain instead."
- **Our assessment**: This is a specific, checkable constraint that determines which of the four patterns is even available for a given skill — practitioners working with vendor-distributed or plugin-marketplace skills (the marketplace model documented in `blog-anthropic-claude-code-skills-lessons.md` Claim 14) cannot use embedding and must fall back to chaining. The article also gives a concrete verification-of-the-embed step: "invoke the skill on a fresh task and confirm the new step runs as part of the output" — testing that the embed actually fired, not just that the text was appended.

### Claim 8: Chaining lets one skill call another at completion, and members of Anthropic's own Claude Code team use this in their day-to-day work: `/code-review` hunts for bugs, `/simplify` cleans up the diff, a `/verify` skill confirms end-to-end behavior, and a custom `/design` skill checks UI changes against a DESIGN.md file
- **Evidence**: Direct first-party description of an internal team's actual verification chain, named skill by skill.
- **Confidence**: settled (first-party statement of the Claude Code team's own current practice, not a hypothetical example)
- **Quote**: "Members of Anthropic's Claude Code team use this pattern in their day-to-day: /code-review hunts for bugs, /simplify cleans up the diff, a /verify skill confirms end-to-end behavior, and a custom /design skill checks against guidelines in a DESIGN.md file if the change touched UI."
- **Our assessment**: This is the single most concrete, checkable claim in the article — a named four-skill chain from the team that builds Claude Code, used on their own changes. It is a first-party instantiation of the two-agent/multi-pass review pattern already documented in the guide's existing Chapter 03 (the two-agent review pattern from `blog-addyosmani-code-agent-orchestra.md`) but from the vendor's own internal practice rather than a synthesized recommendation, and it names four distinct passes (bug-hunt, simplify, behavioral verify, design-guideline check) rather than the generic two-pass (implement/review) pattern currently in the guide.

### Claim 9: Chaining also lets a practitioner add verification to a skill they cannot modify, by building a custom wrapper skill that invokes the original skill and then invokes the verification skill in sequence
- **Evidence**: A worked example (`safe-refactor` wrapper skill that runs `/simplify` then `/verify-no-public-api-changes`) plus a framing statement about what the wrapper accomplishes.
- **Confidence**: emerging (design pattern from the Claude Code team; the mechanism is specific and directly demonstrated in the article's example)
- **Quote**: "What started as a habit ('I always run /verify after /simplify') becomes a contract ('/simplify always runs /verify when it finishes'). The chain runs the whole dev cycle on its own. You only step in when something escalates back to you."
- **Our assessment**: This "habit becomes a contract" framing is the article's clearest statement of what chaining actually buys a team over standalone or embedded: it converts a practitioner's personal discipline (remembering to run the follow-up check) into an unconditional guarantee that does not depend on the practitioner remembering anything. This is the direct counterpart to the embedding-graduation signal in Claim 6 — chaining is what you reach for once a check needs to run after a skill you don't own.

### Claim 10: Chaining trades flexibility for automation and can increase token spend, so chains should be tested before being deployed broadly; the same trade applies at the next stage, running a stable chain on every PR through CI, which should be held off while the chain is still in flux because every adjustment becomes a team-visible event
- **Evidence**: Two paired caution statements — one about chaining's cost/flexibility trade-off, one about the additional caution needed before promoting a chain to PR-wide infrastructure.
- **Confidence**: emerging (cost/caution claim stated qualitatively; no specific token-overhead figures given)
- **Quote**: "You can skip chaining when the steps are independent enough that you sometimes want to run one without the others; chaining trades flexibility for automation. Chained verification loops can increase token spend, so it's best to test these loops before deploying them broadly." / "Hold off on PR-wide gates while the chain is still in flux; every adjustment becomes a team-visible event."
- **Our assessment**: This is the article's only explicit statement of a cost/downside for any of the four patterns — notably it gives no quantified token-overhead figure, so this should be cited as a qualitative caution, not a measured cost claim (contrast with `blog-jetbrains-caveman-token-savings-test.md`'s measured token/dollar figures already in Chapter 03, which this claim cannot be conflated with). The "every adjustment becomes a team-visible event" reasoning for holding off on PR-wide gates is a specific, practical argument for why team-facing infrastructure changes carry a different cost than personal-workflow changes, distinct from the token-cost point in the same paragraph.

### Claim 11: Running a chain on every PR (via GitHub Actions or similar infrastructure) moves verification from personal practice to team infrastructure — a teammate's change passes the same gates regardless of whether they remembered to invoke the chain themselves
- **Evidence**: Direct framing statement describing the qualitative shift from individual to team-level enforcement.
- **Confidence**: emerging (framing/design claim, not independently measured)
- **Quote**: "This is where verification stops being personal infrastructure and becomes team infrastructure. The check you wrote down to save yourself two minutes a week is now saving everyone two minutes a week, on every change."
- **Our assessment**: This closes the same escalation ladder described in Claims 6–9 (standalone → embedded/chained → PR-wide) with an explicit statement of what changes at each step: standalone requires remembering to invoke it, embedded/chained requires owning or wrapping the producing skill, and PR-wide removes the dependency on any individual teammate's diligence entirely. This maps directly onto the guide's existing CI-as-verification-backstop framing (Chapter 03, Layer 3) but frames CI-gated skills specifically as the terminal state of a *personal* verification habit that has been formalized, rather than treating CI as a separate, pre-existing layer unrelated to individual practice.

### Claim 12: The verification loop creation process is a consistent six-step sequence regardless of what is being automated or in what environment: identify the most common manual follow-up, try the built-in `/verify` skill first, write the procedure in plain English, hand it to skill-creator or write markdown directly, invoke and iterate on a new task, then experiment with chaining for an end-to-end flow
- **Evidence**: An explicit six-item ordered list closing the article, presented as environment-agnostic.
- **Confidence**: emerging (first-party prescriptive process; not independently tested by a third party)
- **Quote**: "Pick the manual follow-up you did most often this week." / "Try out the built-in /verify skill first and see if it helps your process." / "Write the procedure in plain English, the way you'd hand it to a new teammate on day one." / "Hand it to skill-creator, or drop the markdown file in .claude/skills/ yourself." / "Invoke it on a new task and confirm the check runs as part of the output, iterate if needed." / "Experiment with skill chaining to create an end-to-end verification flow."
- **Our assessment**: This six-step list is the article's synthesis of everything documented in Claims 3–11 into a single repeatable procedure. It is useful as a guide checklist precisely because each step maps to a specific claim already extracted above (step 2 → Claim 2's built-in list; step 3 → Claim 3; step 4 → Claims 4/5; step 6 → Claims 8–10) rather than introducing new content — its value is as an ordering/checklist artifact, not as a novel claim in its own right.

## Concrete Artifacts

### Built-in verification approaches (verbatim list)

```
Source: claude.com/blog/building-verification-loops-in-claude-code-with-skills

- /verify skill: builds, runs, and observes the changes in your application.
- Toolchain: Claude aims to catch and act on error codes and warnings from
  any tool you provide such as a linter. A good practice is to list your
  exact build and test commands in CLAUDE.md so Claude doesn't have to
  infer them.
- Code Review (research preview): A managed multi-agent service that runs
  an automated review pass on PRs in the repos you enable. You can
  manually fix the finding and push, or close the loop by commenting
  @claude on the finding (if you've already set up and configured GitHub
  Actions, below).
- GitHub Actions: Define a job that invokes Claude with a verification
  skill, and the same checks you run locally fire on every push or PR.
- Spec validation: A skill that helps verify each change against a
  markdown spec in the repo and looks to fix violations.
- Rubrics in Claude Managed Agents (beta): A managed agentic service that
  allows you to verify outcomes against a rubric using a separate grader
  agent. Failures loop back for rework automatically.
```

### Minimal hand-written verification skill (verbatim)

```markdown
# .claude/skills/verify-log-hygiene/SKILL.md
---
name: verify-log-hygiene
description: Check that error logs include the request ID and never
include the request body. Use when the diff touches error handling
or logging.
allowed-tools: [Read, Edit, Grep]
---
Read the error-handling paths in the current diff.
For each log call on an error path, confirm it includes the request ID
and does not pass the request body, headers, or any user-supplied payload.
Report each violation with file:line, then fix it: add the request ID
where it's missing and strip the payload from the log call.
```
*Source: claude.com/blog/building-verification-loops-in-claude-code-with-skills*

### Embedded verification example (verbatim, `scaffold-component`)

```markdown
# .claude/skills/scaffold-component/SKILL.md
---
name: scaffold-component
description: Scaffold a new React component under src/components/, including
the component file, its co-located test, and an index export. Use when the
user asks to create a new component.
allowed-tools: [Read, Write, Edit, Bash, Glob]
---
# Scaffold a new React component
Given a component name (PascalCase), create the following under
`src/components/<Name>/`:
1. `<Name>.tsx`: function component with a typed props interface and a
   default export.
2. `<Name>.test.tsx`: React Testing Library test that renders the
   component and asserts it mounts without throwing.
3. `index.ts`: re-export the default and any named exports.
Follow the patterns in `src/components/Button/` as the reference. Match
the import alias style (`@/components/...`) used throughout the codebase.
# code continues...
After creating the component file, run eslint on it and
address any errors before reporting completion.
```
*Source: claude.com/blog/building-verification-loops-in-claude-code-with-skills — the trailing eslint step is the "embedded" append onto an otherwise unrelated scaffolding skill.*

### Chained wrapper-skill example (verbatim, `safe-refactor`)

```markdown
# .claude/skills/safe-refactor/SKILL.md
Run /simplify on the current diff first.
When /simplify finishes, invoke /verify-no-public-api-changes.
```
*Source: claude.com/blog/building-verification-loops-in-claude-code-with-skills*

### Six-step verification loop creation process (verbatim, ordered)

```
1. Pick the manual follow-up you did most often this week.
2. Try out the built-in /verify skill first and see if it helps your
   process.
3. Write the procedure in plain English, the way you'd hand it to a new
   teammate on day one.
4. Hand it to skill-creator, or drop the markdown file in
   .claude/skills/ yourself.
5. Invoke it on a new task and confirm the check runs as part of the
   output, iterate if needed.
6. Experiment with skill chaining to create an end-to-end verification
   flow.
```
*Source: claude.com/blog/building-verification-loops-in-claude-code-with-skills*

## Cross-References

- **Corroborates**: `blog-anthropic-claude-code-skills-lessons.md` (Claim 3: "Verification skills have had the most measurable impact on Claude's output quality internally"). That source establishes verification as the highest-impact skill category from an internal-usage-count perspective; this source is the implementation-level companion that shows *how* to build that category of skill, including the specific deployment mechanics (standalone/embedded/chained/PR-wide) that the June source does not cover. Both are Claude Code team first-party sources, published roughly seven weeks apart.
- **Corroborates**: `docs-github-copilot-code-review-skills-mcp-tier.md` (Claim 1: Copilot code review invoking custom agent skills during review; Claim 7: skills in `.github/skills` automatically becoming available to code review "if relevant"). This source's built-in "Code Review (research preview)" item (Claim 2 above; Concrete Artifacts) is Anthropic's parallel first-party feature — a managed multi-agent review pass on PRs. The two tools converge on "automated review agent that can invoke project-specific skills," though this source gives far less implementation detail (one sentence) than the GitHub Copilot note's dedicated extraction.
- **Extends**: Guide Chapter 03 (Verification) — "The Two-Agent Review Pattern" section, sourced from `blog-addyosmani-code-agent-orchestra.md` Linked Source 5. That section documents a generic two-pass (Agent A implements, Agent B reviews) pattern. This source's Claim 8 (the Claude Code team's own `/code-review` → `/simplify` → `/verify` → `/design` chain) is a first-party, named, four-pass instantiation of the same underlying idea, directly from the tool vendor's internal practice rather than a synthesized recommendation — a concrete example the guide's existing section does not have.
- **Extends**: `blog-humanlayer-skill-issue-harness-engineering.md` (Claim 8: verification success is correlated with an agent's ability to verify its own work, and raw verification output — e.g. full test suite runs — flooding the context window is itself a failure mode motivating "back-pressure" as a harness surface). That source documents the *failure mode* of unfiltered verification output; this source documents a complementary, upstream concern — *how the verification check itself gets built and deployed* — without addressing output volume or context flooding at all. The two are compatible, non-overlapping halves of a "build good verification skills, and don't let their output flood context" pair.
- **Extends**: Guide Chapter 03 (Verification) — "Layer 3: CI as Verification Backstop." The existing chapter treats CI gates as a layer practitioners should simply add. This source's Claim 11 (PR-wide gates as the endpoint of an escalation ladder from standalone → embedded/chained → PR-wide) reframes CI-gated skills as the terminal state of a personal verification habit that has been formalized and derisked through prior use — a sequencing argument the existing chapter does not make.
- **Contradicts**: None found. No claim in this source conflicts with an existing corpus note or with itself.
- **Novel**:
  - **The four-pattern deployment taxonomy for verification skills (standalone / embedded / chained / on-every-PR) with an explicit escalation signal between each pair.** No prior corpus source names this specific set of four patterns or the graduation criteria between them (Claims 6, 7, 9, 11).
  - **The `/code-review` → `/simplify` → `/verify` → `/design` internal Anthropic chain**, a named, first-party, current example of the vendor's own multi-skill verification chain (Claim 8) — more specific than any prior corpus mention of Anthropic's internal practices.
  - **The wrapper-skill technique for adding verification to a skill the practitioner cannot modify** (Claim 9, the `safe-refactor` example) — a concrete mechanism not documented elsewhere in the corpus for the specific problem of built-in or plugin-managed skills being off-limits to direct editing.
  - **The "habit becomes a contract" framing for what chaining buys over standalone invocation** (Claim 9) is a new, quotable articulation of why automation matters beyond "it saves a manual step."

## Guide Impact

- **Chapter 03 (Verification)**: Add a new subsection, e.g. "Deployment Patterns for Verification Skills," presenting the four-pattern taxonomy (standalone, embedded, chained, on every PR) as a decision framework for *where* a verification check should live once a team has decided to encode it — this is new territory; the existing chapter documents verification *layers* (deterministic tools, hooks, CI, two-agent review, human review) but not the mechanics of turning a specific repeated manual check into a Claude Code skill and choosing its trigger mechanism. Cite this source directly, using the `verify-log-hygiene` and `safe-refactor` examples as copy-ready templates.
- **Chapter 03 (Verification) — "The Two-Agent Review Pattern" section**: Add the Claude Code team's own `/code-review` → `/simplify` → `/verify` → `/design` chain (Claim 8) as a concrete, first-party, four-pass alternative to the existing generic two-pass example, citing this source alongside the existing `blog-addyosmani-code-agent-orchestra.md` citation.
- **Chapter 03 (Verification) — Layer 3 (CI as Verification Backstop)**: Add the escalation-ladder framing (Claim 11: standalone → embedded/chained → PR-wide) as the argument for *why* teams should move a stabilized personal-workflow check into CI, paired with the caution (Claim 10) to hold off on PR-wide gates until the chain is stable, since every adjustment becomes team-visible.
- **Chapter 02 (Harness Engineering)**: The six-step verification loop creation process (Claim 12) is a reusable checklist that fits alongside the existing skills-design content sourced from `blog-anthropic-claude-code-skills-lessons.md` — it answers "how do I decide what to build a skill for" specifically for the verification-skill category, complementing that source's general skill-design best practices.

## Extraction Notes

- The article was fetched twice: first via WebFetch (which returned a condensed, non-verbatim summary — consistent with this corpus's established WebFetch behavior for claude.com/blog articles, e.g. the Extraction Notes in `blog-anthropic-claude-code-skills-lessons.md`), then via a direct `curl` fetch of the raw page HTML, stripped of markup with a plain Python script, to guarantee verbatim quotes. All quotes in this note were copied from the curl-fetched raw text, not from the WebFetch summary. The WebFetch pass surfaced the general shape of the article but omitted specific verbatim phrasing (e.g. the "chaining trades flexibility for automation" token-cost caution, Claim 10) that only appeared in the raw-text fetch — a useful confirmation that the WebFetch-only extraction method used by some earlier notes in this corpus can undercount source content, not just reword it.
- The author is credited only as "Delba de Oliveira, a member of the Claude Code team" in the article's closing line — no further biographical detail (title, tenure) is given, unlike the Thariq Shihipar byline in the companion June source note.
- The article does not link out to substantive sub-pages beyond a "complete guide to building skills" reference (unlinked in the extracted text — no URL was recoverable from the raw HTML fetch for this specific inline reference) and a generic "documentation" link in the page's product-CTA boilerplate; neither was followed, since both point to general product documentation rather than content specific to verification loops.
- No contradiction with any existing corpus source was identified. No contradiction issue filed.
- Confidence set to `emerging`: this is a first-party, authoritative account from the team that builds Claude Code, with one claim (Claim 8, the internal team's actual chain) rising to `settled` as a direct statement of current internal practice — but the deployment-pattern taxonomy as a whole is presented as design guidance without benchmarks, before/after metrics, or external validation, consistent with how this corpus rates the companion `blog-anthropic-claude-code-skills-lessons.md` source.
