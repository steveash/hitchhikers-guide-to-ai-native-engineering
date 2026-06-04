---
source_url: https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills
source_type: blog-post
title: "Lessons from building Claude Code: How we use skills"
author: Thariq Shihipar (member of technical staff, Claude Code, Anthropic)
date_published: 2026-06-03
date_extracted: 2026-06-04
last_checked: 2026-06-04
status: current
confidence_overall: emerging
issue: "#1055"
---

# Lessons from building Claude Code: How we use skills

> A first-party Anthropic engineering account from the Claude Code team on how to design, categorize, and distribute skills — introducing a nine-category skill taxonomy, six concrete design best practices, and two distribution models, with the specific claim that verification skills have had the most measurable impact on Claude's output quality internally.

## Source Context

- **Type**: blog-post (claude.com/blog, June 3, 2026; practitioner engineering account from the Claude Code team)
- **Author credibility**: Thariq Shihipar is a member of technical staff on Claude Code at Anthropic — a direct practitioner who builds and uses Claude Code as part of the team that develops the product. This is the highest-credibility source for Claude Code skills design: first-party account of internal engineering practices from the organization that ships the tool. Limitations: single organization (Anthropic), which has unique characteristics (dogfoods the product intensively, has high AI engineering sophistication). The design patterns described are grounded in hundreds of internal examples, which gives them practical weight, but generalizability to teams with different workflows is not tested.
- **Scope**: Covers what types of skills Anthropic has built (nine-category taxonomy with named examples for each), six best practices for designing skills, distribution strategies (repo-embedded vs. internal plugin marketplace), a memory pattern using append-only logs, helper scripts to reduce boilerplate, and on-demand hooks for destructive operations. Does NOT cover: specific API or SDK parameters for creating skills, how skills interact with auto mode or routines at an implementation level, token cost or context overhead measurements, comparative benchmarks against non-skill approaches, or how skills differ across CLI vs. IDE extension contexts.

## Extracted Claims

### Claim 1: Skills have become one of the most used extension points in Claude Code, with hundreds in active use at Anthropic

- **Evidence**: First-party opening claim from the Claude Code team with a specific internal usage count.
- **Confidence**: settled (first-party fact from the team that builds the tool; the scale indicator is specific enough to be credible)
- **Quote**: "Skills have become one of the most used extension points in Claude Code. They're flexible, easy to make, and easy to distribute."
- **Our assessment**: This establishes skills as the primary harness extension mechanism in practice. "Hundreds in active use" at the organization with the deepest usage of its own tool is the strongest possible adoption signal. The trifecta — flexible, easy to make, easy to distribute — explains why skills outpace other extension points (CLAUDE.md customization, hooks, plugins, MCP servers) for most day-to-day context engineering needs.

### Claim 2: Anthropic has identified nine distinct categories of skills based on internal use of hundreds of examples

- **Evidence**: First-party taxonomy derived from observed internal patterns, with named skill examples for each category.
- **Confidence**: emerging (the categories are Anthropic's own framing based on observed patterns; whether this taxonomy is exhaustive or generalizable is a design claim rather than a verified measurement)
- **Quote**: (no single direct quote for the overall taxonomy claim; see Concrete Artifacts for the complete taxonomy)
- **Our assessment**: The nine-category taxonomy is the most practically useful organizing artifact in the post. Teams building a skills library can use it to audit coverage and identify gaps. The fact that Anthropic arrived at this taxonomy from hundreds of real internal skills gives it empirical grounding — these are observed categories, not theoretical classifications. Teams that map their existing skills against this taxonomy will likely find uneven coverage that reveals where to invest next.

### Claim 3: Verification skills have had the most measurable impact on Claude's output quality internally

- **Evidence**: First-party internal measurement claim from the Claude Code engineering team.
- **Confidence**: emerging (stated as a measured fact with "most measurable" framing, but no specific methodology or comparison metrics are provided in the article)
- **Quote**: "Verification skills have had the most measurable impact on Claude's output quality internally."
- **Our assessment**: This is the single most important signal for practitioners building a skills library from scratch: if you can only build one skill type, build verification skills. The claim is consistent with the broader corpus finding that verification is the primary bottleneck in AI-native engineering (see `blog-anthropic-ai-native-engineering-org.md` Claim 1). The specific examples (signup-flow-driver, checkout-verifier, tmux-cli-driver) make the pattern concrete: verification skills drive Claude to run actual product flows rather than reason theoretically about correctness.

### Claim 4: Skills are folders that can include scripts, assets, data, and other resources — not just markdown files

- **Evidence**: First-party architectural description explicitly countering a stated common misconception.
- **Confidence**: settled (first-party architectural fact directly refuting a named common misconception)
- **Quote**: "A common misconception we hear about skills is that they are 'just markdown files.' They're actually folders that can include scripts, assets, data, etc. that the agent can discover, explore and manipulate."
- **Our assessment**: This is one of the most important architectural claims in the post because it expands the design space from "text instructions" to "packaged environment including executable code, data files, and reference material." The misconception is specifically named as common — suggesting many practitioners are underutilizing skills by writing only markdown. The full folder model enables progressive disclosure (Claim 5), helper scripts (Claim 12), stored memory (Claim 11), and reference data that Claude can consult dynamically.

### Claim 5: The entire file system of a skill folder should be designed as a form of context engineering and progressive disclosure

- **Evidence**: First-party design recommendation with explicit architectural framing.
- **Confidence**: emerging (design recommendation from experienced practitioners; the principle is sound but implementation depends on team context)
- **Quote**: "You should think of the entire file system as a form of context engineering and progressive disclosure."
- **Our assessment**: This reconceptualizes skill folders from "docs dump" to "context architecture." Progressive disclosure means Claude loads only the files relevant to the current task rather than consuming everything upfront. A well-structured skill folder places the most universal content at the top level, with deeper subdirectories holding examples, reference material, and edge-case documentation that Claude reaches for only when the task requires it. This is the skills analog of the "lean and layered CLAUDE.md" principle from `blog-anthropic-large-codebase-best-practices.md` (Claim 6): hierarchical structure with essential content at the root, detail in subdirectories.

### Claim 6: The Gotchas section is the highest-signal content in any skill — built from observed failure points accumulated over actual usage

- **Evidence**: First-party design recommendation named explicitly as "highest-signal" by the team with hundreds of internal examples.
- **Confidence**: emerging (authoritative claim from the team with deep internal experience; but "highest-signal" is relative and not formally measured)
- **Quote**: "The highest-signal content in any skill is the Gotchas section. These sections should be built up from common failure points that Claude runs into when using your skill."
- **Our assessment**: The Gotchas section is a failure-driven quality mechanism, not written in advance but accumulated through observed failures during real skill usage. This makes it the densest encoding of hard-won knowledge in a skill — content that exists only because the skill was actually used and failed in specific ways. For practitioners: a skill without a Gotchas section is a skill that hasn't been sufficiently battle-tested. The maintenance activity for skills is updating the Gotchas section after each observed failure, not periodic general revision.

### Claim 7: Skills should not restate capabilities Claude already has — only information Claude cannot infer from the codebase or training adds value

- **Evidence**: First-party design anti-pattern with an explicitly stated rationale.
- **Confidence**: settled (the principle is clearly articulated; consistent with general prompt engineering principles about avoiding redundancy; the stated rationale is sound)
- **Quote**: "Claude already knows how to code and can read your codebase."
- **Our assessment**: This is a corrective for the most common skill-writing failure: padding skills with generic coding guidance that adds context load without informational value. What belongs in a skill: proprietary APIs Claude has never seen, team-specific conventions that differ from open-source norms, internal tool invocation patterns, non-obvious failure modes, and domain knowledge absent from training data. Applying this filter makes skills shorter, faster to load, and higher-signal — and reduces the context overhead that scales with the number of installed skills (Claim 14).

### Claim 8: Skills should avoid railroading Claude with overly specific instructions — provide information without constraining the agent's flexibility to adapt

- **Evidence**: First-party design principle about skill over-specification.
- **Confidence**: emerging (design recommendation based on internal experience; the failure mode is described but without specific examples of what went wrong)
- **Quote**: "Give Claude the information it needs, but give it the flexibility to adapt to the situation."
- **Our assessment**: Railroading is the opposite failure from redundancy (Claim 7): instead of including what Claude already knows, railroading prescribes a fixed sequence of steps that eliminates the agent's ability to adapt to the specific context. Skills are reusable across varied contexts; overly specific instructions that assume one scenario become unhelpful or wrong when the scenario varies. For practitioners: a skill that prescribes a fixed command sequence is a script, not a skill. A skill that provides context, known failure modes, and available tools — while leaving sequencing to Claude — is substantially more robust across varying task conditions.

### Claim 9: Config.json enables skills to store setup information and prompt users when required configuration is missing

- **Evidence**: First-party design pattern with a concrete standup-to-Slack example.
- **Confidence**: emerging (specific design pattern from internal practice; the standup example is plausible and specific)
- **Quote**: "If you are making a skill that posts your standup to Slack, you may want Claude to ask which Slack channel to post it in."
- **Our assessment**: The config.json pattern is the skills equivalent of environment variables or user settings: a machine-readable file that Claude reads to check for pre-configured values, and fills via user prompting when values are absent. This enables skills to be distributed generically (no hardcoded team-specific values) while capturing team-specific configuration at first use. A skill that needs an API endpoint, channel name, or project identifier should store this in config.json rather than hardcoding it (not portable) or prompting every time (annoying after the first run).

### Claim 10: The description field is a trigger specification for the model, not a human-readable summary

- **Evidence**: First-party design principle with explicit framing correction.
- **Confidence**: settled (the mechanism is described definitively: the description is what Claude reads to decide whether to invoke the skill)
- **Quote**: "Which means the description field is not a summary, it's a description of when to trigger this skill."
- **Our assessment**: This framing correction has direct implications for skill discoverability. A description written for human browsing ("This skill helps with CI/CD pipelines") will cause Claude to miss the skill when a user phrases a request concretely ("babysit my PR"). A description written as a trigger ("use this skill when the user wants to monitor a PR for CI failures") fires at the right moment. The description field is not metadata — it is the mechanism by which Claude selects skills from the available library. Practitioners should draft descriptions as trigger conditions: "use this when..." framing rather than "this skill does..." framing.

### Claim 11: Skills can implement stateful memory using append-only log files that Claude reads to recall prior history across invocations

- **Evidence**: First-party design pattern with a concrete standup example and mechanism description.
- **Confidence**: emerging (the pattern is named and exemplified; simple and plausible but not quantitatively evaluated)
- **Quote**: "Some skills can include a form of memory by storing data within them...a `standup-post` skill might keep a standups.log with every post it's written, which means the next time you run it, Claude reads its own history and can tell what's changed since yesterday."
- **Our assessment**: The append-only log pattern converts a skill from stateless (each invocation is independent) to stateful (each invocation reads prior state). The standup example is the simplest case: the log provides a delta (what changed since yesterday), enabling richer output than starting fresh. More complex uses: a code review skill that logs its findings could skip already-reviewed issues; a monitoring skill could track which alerts it has already triaged. This is a lightweight alternative to external memory systems for patterns where the full history fits in a log file — no database, no vector store, just a text file in the skill folder.

### Claim 12: Helper scripts included in skill folders reduce boilerplate by letting Claude compose rather than reconstruct common operations

- **Evidence**: First-party design pattern naming the principle and efficiency mechanism.
- **Confidence**: emerging (described as a specific internal design pattern; the principle is sound and specific)
- **Quote**: "Giving Claude scripts and libraries lets Claude spend its turns on composition, deciding what to do next rather than reconstructing boilerplate."
- **Our assessment**: This is the skills equivalent of providing Claude with utility functions rather than asking it to implement them from scratch each session. A data analysis skill that includes pre-built data-fetching functions (the funnel-query, cohort-compare examples) lets Claude write analysis logic without writing query boilerplate. The "spend turns on composition" framing is economically important: each Claude turn has cost; turns spent reconstructing standard boilerplate from memory are wasteful when the boilerplate could be provided directly in the skill folder. For practitioners: if Claude is writing the same utility code repeatedly across sessions for a skill, extract it into a helper script.

### Claim 13: On-demand hooks provide session-scoped safeguards for destructive operations, activated only when the user knows they are in a high-risk context

- **Evidence**: First-party design pattern with a concrete `/careful` hook example specifying blocked commands.
- **Confidence**: emerging (described as an internal pattern; mechanism is specific and plausible)
- **Quote**: (no single verbatim quote covers the full pattern; the article describes on-demand hooks including `/careful` that blocks `rm -rf`, `DROP TABLE`, force-push, `kubectl delete` via PreToolUse matcher on Bash, activated only "when you know you're touching prod")
- **Our assessment**: On-demand hooks solve the false-positive problem with continuous safety hooks: if a hook blocks `rm -rf` in all sessions, it interferes with legitimate cleanup in development environments. Activating the hook on-demand scopes the protection to sessions where it is actually needed. This is architecturally distinct from auto mode's continuous semantic classifier: auto mode always evaluates every Tier 3 action; on-demand hooks are explicit, user-initiated policy enforcement. The two are complementary: auto mode provides always-on semantic safety; on-demand hooks provide explicit opt-in for high-stakes sessions.

### Claim 14: For smaller teams, checking skills into repos is sufficient; at scale, an internal plugin marketplace enables selective installation and avoids universal context overhead

- **Evidence**: First-party distribution recommendation with explicit rationale for the scale threshold, including the mechanism (context overhead) that drives the recommendation.
- **Confidence**: emerging (design recommendation based on internal experience; the context overhead mechanism is specific and credible)
- **Quote**: "For smaller teams working across relatively few repos, checking your skills into repos works well. But every skill that is checked in also adds a little bit to the context of the model. As you scale, an internal plugin marketplace allows you to distribute skills and let your team decide which ones to install, as well as include a setup flow."
- **Our assessment**: The context overhead argument is an important architectural consideration: repo-checked skills are always loaded, accumulating context cost proportional to the number of skills installed. At small scale (tens of skills), this overhead is negligible. At large scale (hundreds of skills), it materially affects model performance and cost. The internal plugin marketplace solves this by moving from "all skills always present" to "each engineer installs the skills they need." The selective installation model also enables teams to test skills in isolation before promoting them to the full team. This is the scale threshold that triggers investment in skills infrastructure.

### Claim 15: Internal skills marketplaces should use a peer-curation sandbox-to-promotion workflow to manage quality organically

- **Evidence**: First-party recommended workflow with specific steps: sandbox upload, community trial, then PR to promote.
- **Confidence**: emerging (described as a recommended workflow; specific enough to be actionable)
- **Quote**: "If someone has a skill that they want people to try out, they can upload it to a sandbox folder in GitHub and point people to it in Slack or other forums. Once a skill has gotten traction (which is up to the skill owner to decide), they can put in a PR to move it into the marketplace."
- **Our assessment**: The sandbox-to-promotion workflow prevents the marketplace from becoming cluttered with untested or low-quality skills. Sharing in Slack before PR review is the skills equivalent of an informal "does anyone find this useful?" check. The "up to the skill owner to decide" framing on traction is notable: it makes traction self-assessed rather than requiring an explicit adoption vote, keeping the barrier to promotion low while still requiring demonstrated usage. For organizations: this model trusts practitioners to judge skill readiness rather than creating a formal review gate, enabling organic quality management at scale.

## Concrete Artifacts

### Nine Skill Category Taxonomy

```
Anthropic Internal Skills Taxonomy
(Thariq Shihipar, "Lessons from building Claude Code: How we use skills," June 3, 2026)

1. Library and API Reference
   Purpose: Documentation for internal libraries and CLIs
   Examples: billing-lib, internal-platform-cli, sandbox-proxy

2. Product Verification
   Purpose: Driving Claude to test product flows directly
   Examples: signup-flow-driver, checkout-verifier, tmux-cli-driver
   Note: "Verification skills have had the most measurable impact on
         Claude's output quality internally."

3. Data Fetching and Analysis
   Purpose: Query internal data sources and monitoring tools
   Examples: funnel-query, cohort-compare, grafana, datadog

4. Business Process and Team Automation
   Purpose: Automate recurring team coordination tasks
   Examples: standup-post, create-<ticket-system>-ticket, weekly-recap

5. Code Scaffolding and Templates
   Purpose: Generate boilerplate for new code structures
   Examples: new-<framework>-workflow, new-migration, create-app

6. Code Quality and Review
   Purpose: Enforce coding standards and review practices
   Examples: adversarial-review, code-style, testing-practices

7. CI/CD and Deployment
   Purpose: Manage build pipelines and deployment workflows
   Examples: babysit-pr, deploy-<service>, cherry-pick-prod

8. Runbooks
   Purpose: Step-by-step operational guides for known procedures
   Examples: <service>-debugging, oncall-runner, log-correlator

9. Infrastructure Operations
   Purpose: Routine maintenance and operational procedures
   Note: "some of which involve destructive actions that benefit from guardrails"
   Examples: <resource>-orphans, dependency-management, cost-investigation
```

### Six Best Practices for Skill Design

```
Best Practices for Writing Claude Code Skills
(Thariq Shihipar, Anthropic, June 3, 2026)

1. DON'T STATE THE OBVIOUS
   "Claude already knows how to code and can read your codebase."
   → Skills should contain only information Claude cannot infer from
     training or the codebase itself.

2. BUILD A GOTCHAS SECTION
   "The highest-signal content in any skill is the Gotchas section.
    These sections should be built up from common failure points that
    Claude runs into when using your skill."
   → Write it reactively from observed failures; update after each failure.

3. USE THE FILE SYSTEM AND PROGRESSIVE DISCLOSURE
   "A common misconception we hear about skills is that they are 'just
    markdown files.' They're actually folders that can include scripts,
    assets, data, etc. that the agent can discover, explore and manipulate."
   "You should think of the entire file system as a form of context
    engineering and progressive disclosure."
   → Essential content at top level; deep material in subdirectories.

4. AVOID RAILROADING CLAUDE
   "Give Claude the information it needs, but give it the flexibility
    to adapt to the situation."
   → Provide context, failure modes, and available tools.
   → Do not prescribe fixed command sequences.

5. THINK THROUGH THE SETUP
   "If you are making a skill that posts your standup to Slack, you may
    want Claude to ask which Slack channel to post it in."
   → Store team-specific configuration in config.json.
   → Prompt users when configuration is missing rather than hardcoding.

6. WRITE DESCRIPTIONS FOR THE MODEL, NOT FOR HUMANS
   "Which means the description field is not a summary, it's a description
    of when to trigger this skill."
   → Write as a trigger condition: "use this when..."
   → Descriptions are Claude's discovery mechanism, not a human summary.
```

### Skill Distribution Models

```
Claude Code Skills Distribution
(Thariq Shihipar, Anthropic, June 3, 2026)

STORAGE LOCATION: ./.claude/skills (repo-embedded) or plugin registry

MODEL 1: REPO-EMBEDDED SKILLS
  "For smaller teams working across relatively few repos, checking your
   skills into repos works well."
  Best for:    Small teams, few repos
  Trade-off:   "Every skill that is checked in also adds a little bit to
                the context of the model" — context overhead scales with
                number of installed skills
  Advantage:   Zero friction; skills available to all contributors by default

MODEL 2: INTERNAL PLUGIN MARKETPLACE
  "An internal plugin marketplace allows you to distribute skills and let
   your team decide which ones to install, as well as include a setup flow."
  Best for:    Larger teams, many skills
  Advantage:   Engineers install only the skills they need; no universal
               context overhead; includes setup flow for configuration
  Curation:    Peer-driven sandbox-to-promotion workflow:
    Step 1: Author uploads to sandbox folder in GitHub
    Step 2: Points to it in Slack or forums
    Step 3: Once traction is established, opens PR to move to marketplace
    Note: "Once a skill has gotten traction (which is up to the skill owner
           to decide), they can put in a PR to move it into the marketplace."

SELECTION HEURISTIC:
  Small team + few repos  → check into repo
  Scaling team + many skills → invest in internal plugin marketplace
```

### Memory Pattern: Append-Only Log

```
Skills Memory Pattern: Append-Only Log
(Thariq Shihipar, Anthropic, June 3, 2026)

"Some skills can include a form of memory by storing data within them...
 a `standup-post` skill might keep a standups.log with every post it's
 written, which means the next time you run it, Claude reads its own
 history and can tell what's changed since yesterday."

EXAMPLE: standup-post skill
  On each invocation:
    1. Claude reads standups.log to see prior post history
    2. Claude generates standup reflecting what changed since yesterday
    3. Claude appends new standup entry to standups.log

EXTENSION PATTERNS:
  - Code review skill: log reviewed issues → skip on next invocation
  - Monitoring skill: log triaged alerts → avoid re-triaging on next run
  - Weekly recap skill: log all daily entries → synthesize over the period

TRADE-OFFS:
  + No external dependencies; plain text, human-inspectable
  + Entire history available to Claude on each invocation
  - Log grows indefinitely without pruning
  - Full history loaded into context even when only recent entries are needed
```

### On-Demand Safety Hook Pattern

```
On-Demand Hook Example: /careful
(Thariq Shihipar, Anthropic, June 3, 2026)

Trigger:    On-demand activation ("when you know you're touching prod")
Mechanism:  PreToolUse matcher on Bash
Blocks:     rm -rf, DROP TABLE, force-push, kubectl delete

DESIGN PRINCIPLE:
  Continuous hooks can interfere with legitimate dev operations.
  On-demand hooks scope protection to high-stakes sessions only.

COMPLEMENT TO AUTO MODE:
  Auto mode: continuous semantic classifier (evaluates all Tier 3 actions)
  On-demand hooks: explicit, user-activated policy enforcement
  → Complementary: auto mode provides always-on safety;
    on-demand hooks cover sessions where the user knows the risk level
```

## Cross-References

- **Corroborates**: `blog-anthropic-large-codebase-best-practices.md` (Claim 5): That note's harness taxonomy names skills as one of five primary extension points ("The harness is built from five extension points—CLAUDE.md files, hooks, skills, plugins, and MCP servers—each serving a different function."). This source fills in what the large-codebase note treats as given: a concrete taxonomy of what skills actually contain, how to design them, and how to distribute them. The two sources form a natural pair: the large-codebase note provides the harness architecture; this source provides the skills engineering layer. Note also that `blog-anthropic-large-codebase-best-practices.md` Claim 6 ("lean and layered CLAUDE.md") is the architectural parallel to this source's progressive disclosure principle (Claim 5 here) — the same principle applied to two different extension points.

- **Corroborates**: `blog-anthropic-ai-native-engineering-org.md` (Claim 1, Claim 5): Fung's finding that "Verification, code review, and security took their place" as the primary bottlenecks directly corroborates this source's claim that verification skills have had the most measurable internal impact. Fung's automation reflex ("Is there a way to automate it?") also maps directly to the Business Process and Team Automation skill category — the standup-post example in this source is the exact pattern Fung describes ("having Claude summarize customer feedback channels every morning went from a ritual I did manually...to something I just have running automatically in the background"). Two independent Anthropic authors converge on the same operational patterns.

- **Corroborates**: `docs-github-copilot-code-review-skills-mcp-tier.md` (Claim 1, Claim 7): GitHub Copilot's agent skills for code review implement a parallel concept in a competing tool. Key similarities: skills invoke team tools and standards; skills are contextually selected when relevant. Key structural differences: GitHub Copilot skills live in `.github/skills/code-review/SKILL.md`; Claude Code skills live in `.claude/skills/` as full folders with multiple files. The convergence of two competing AI coding tools on the skills abstraction (packaged context + tool invocation + contextual selection) is a strong signal that this is the right architectural pattern for extending AI agents with team-specific knowledge.

- **Corroborates**: `docs-github-copilot-agent-skills-cli.md` (Claim 1): GitHub's `gh skill` package manager defines agent skills as "portable sets of instructions, scripts, and resources that teach AI agents how to perform specific tasks." This is independently consistent with this source's description of skills as folders containing scripts, assets, and data. The convergence of the folder/multi-resource model across two tools confirms it is an emerging cross-tool standard rather than a Claude Code-specific pattern.

- **Extends**: `blog-anthropic-claude-code-auto-mode.md` (Claim 4, Claim 7): The on-demand hook pattern (Claim 13 here) extends auto mode's always-on semantic classifier by providing user-controlled, session-activated policy enforcement. Auto mode's three-tier permission structure handles Tier 3 actions with continuous classification; on-demand hooks provide an additional layer for sessions where the user explicitly knows they are in a high-risk context. Together they form a layered safety model rather than a single mechanism.

- **Extends**: `blog-anthropic-claude-code-routines.md` (Claim 9, Claim 3): The Business Process and Team Automation skill category (standup-post, weekly-recap) maps directly to the scheduled routine patterns. Skills provide the context and execution tools; routines provide the scheduling and triggering layer. The combination — a skill with helper scripts + a scheduled routine to invoke it — is the complete implementation of recurring background automation. This source fills in what the routines note leaves implicit: the skill design that makes a routine's task execution effective.

- **Contradicts**: None found. The closest potential tension is between the GitHub Copilot skills model (`.github/skills/` directory, SKILL.md files, contextual relevance selection) and the Claude Code skills model (`.claude/skills/` directory, folder-based with multiple files, description-triggered selection). These are parallel implementations of the same concept across competing tools — not a factual contradiction. No contradiction issue required.

- **Novel**:
  - **Nine-category skill taxonomy with concrete internal examples**: No prior corpus source provides a structured taxonomy of skill types with named examples. This is the first categorization framework for answering "what skills should I build?" and auditing library coverage.
  - **Verification skills as the highest-impact category**: The specific claim that verification skills have "the most measurable impact on Claude's output quality internally" is the first first-party quantitative signal about which skill category to prioritize. No prior source provides this category-level impact ranking.
  - **The Gotchas section as a specific, named skill quality mechanism**: No prior source names a specific skill section type or describes how it should be built reactively over time from observed failures. This is a concrete design practice, not a generic "document edge cases" recommendation.
  - **The "description as trigger" framing**: The explicit distinction between summary-for-humans and trigger-for-Claude in the description field is a specific, actionable design principle not documented in any prior corpus source.
  - **Append-only log memory pattern**: No prior corpus source documents the file-based memory pattern for making skills stateful across invocations. Prior memory discussions focus on external systems (vector stores, MCP-backed knowledge bases, Managed Agents built-in memory).
  - **On-demand hooks as user-activated session-scoped policy enforcement**: The distinction between always-on classifiers (auto mode) and user-activated session-scoped hooks (`/careful`) is a new architectural dimension. Prior sources treat hooks as always-on or system-configured; this is the first description of user-activated enforcement.
  - **Context overhead as the scale threshold for skill distribution**: The explicit claim that repo-checked skills accumulate context load — and that this drives the need for a marketplace at scale — is a specific, named mechanism with practical architecture implications not documented elsewhere.
  - **Peer curation model (sandbox → traction → PR to promote)**: The specific sandbox-to-marketplace promotion workflow is novel to the corpus. Prior sources describe the concept of skill marketplaces but not this organic curation workflow.

## Guide Impact

- **Chapter 02 (Harness Engineering) — Skills Design**: This source should anchor the skills design section. Currently the corpus covers skills as an extension point (`blog-anthropic-large-codebase-best-practices.md` Claim 5) but not how to design them effectively. Add a "Skills Engineering" subsection using the six best practices as the organizing frame. The three most important design practices to highlight: Gotchas section (reactive failure documentation), description-as-trigger (skill discoverability), and progressive disclosure (folder architecture). The nine-category taxonomy is a "what to build" companion to the "how to build it" best practices.

- **Chapter 02 (Harness Engineering) — Skills Taxonomy as Coverage Audit**: Add the nine-category taxonomy as a skills library audit framework. Teams can map existing skills against the nine categories to identify gaps. A team strong in Library/API Reference but absent in Verification and Runbooks has gaps this taxonomy makes visible. Present as a planning heuristic, not a prescriptive checklist.

- **Chapter 02 (Harness Engineering) — Safety for Skills**: The on-demand hook pattern (Claim 13) should appear in the safety section as a complement to auto mode. Add: "For sessions where you know you are operating on production infrastructure, activate a session-scoped hook rather than relying entirely on auto mode's continuous classifier. The `/careful` pattern blocks the canonical destructive commands (`rm -rf`, `DROP TABLE`, force-push, `kubectl delete`) for the duration of the high-risk session."

- **Chapter 03 (Verification)**: The claim that verification skills have "the most measurable impact on Claude's output quality internally" is the primary motivating evidence for investing in verification skills first. Pair with `blog-anthropic-ai-native-engineering-org.md` Claim 1 (verification as the post-AI bottleneck). Together: two independent Anthropic sources point to verification as the highest-leverage skills investment. The specific verification skill examples (signup-flow-driver, checkout-verifier, tmux-cli-driver) provide concrete starting points.

- **Chapter 05 (Team Adoption) — Distribution Strategy**: Add the "repo-embedded vs. internal marketplace" decision framework using the context overhead threshold as the scale trigger. Small teams → check into repos. Teams scaling to many skills → invest in an internal marketplace with peer curation. The sandbox-to-promotion workflow is the recommended curation model. Cross-reference `docs-github-copilot-agent-skills-cli.md` for the GitHub ecosystem's `gh skill` package manager as an alternative distribution mechanism.

- **Chapter 01 (Daily Workflows)**: The append-only log memory pattern enables recurring workflow skills to have temporal continuity. For teams building standup, weekly recap, or oncall monitoring skills, the log pattern is the recommended approach. Add the standup-post example as the concrete illustration of how skills gain session history without external infrastructure.

## Extraction Notes

- The source is a blog post from claude.com. WebFetch was unable to return the full verbatim article text and declined to do so for copyright reasons. All quoted passages were extracted via multiple targeted fetch requests asking for specific sections and verbatim text. All quoted passages in this note are taken from WebFetch responses where the model reproduced them with explicit quotation marks. The Assayer should spot-check all quotes against the live URL at https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills.
- The on-demand hook claim (Claim 13) has a quote note "(no single verbatim quote covers the full pattern)" because the WebFetch response synthesized the example from article content without providing a single extractable verbatim sentence. The specifics (`rm -rf`, `DROP TABLE`, force-push, `kubectl delete`, PreToolUse on Bash, activated "when you know you're touching prod") were provided in the WebFetch response with implied attribution to the article text. This specific claim should be spot-checked with extra care.
- Author name confirmed as "Thariq Shihipar, a member of technical staff at Anthropic working on Claude Code" from WebFetch response. The article may have a more specific title — check the live URL.
- No contradiction with existing corpus notes was found. No contradiction issue filed.
- Confidence is set to `emerging`: while Thariq Shihipar is a first-party practitioner from the Claude Code team with authoritative access to internal usage data (hundreds of skills), the claims are based on a single organization's internal experience without quantitative methodology. The "most measurable impact" claim for verification skills lacks specific metrics that would justify `settled`.
