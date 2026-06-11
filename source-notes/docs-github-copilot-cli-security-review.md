---
source_url: https://github.blog/changelog/2026-06-10-dedicated-security-review-command-now-available-in-copilot-cli
source_type: docs
title: "Dedicated security review command now available in Copilot CLI"
author: GitHub (official changelog)
date_published: 2026-06-10
date_extracted: 2026-06-11
last_checked: 2026-06-11
status: current
confidence_overall: settled
issue: "#1144"
---

# Dedicated Security Review Command Now Available in Copilot CLI

> GitHub's June 10, 2026 changelog introduces `/security-review` as a dedicated
> experimental slash command in Copilot CLI — a Copilot-driven, on-demand security
> scanner targeting injection flaws, XSS, insecure data handling, path traversal,
> and weak cryptography that operates independently of GitHub's pipeline security
> tooling (code scanning, Dependabot, secret scanning) and is designed as a
> lightweight pre-commit gate.

## Source Context

- **Type**: docs (GitHub official product changelog, June 10, 2026; approximately
  300 words)
- **Author credibility**: GitHub engineering team announcing a production experimental
  feature in Copilot CLI. Authoritative for: the feature's existence, its invocation
  pattern, the stated vulnerability categories, the relationship to existing GitHub
  security tooling, and the availability gating (experimental public preview). Not a
  credible source for: empirical detection rates or precision/recall data for the new
  command, how this command differs mechanically from general Copilot code review,
  plan-tier availability details, or behavior under edge cases (large diffs, binary
  files, non-supported languages).
- **Scope**: The announcement covers the new `/security-review` command: how to invoke
  it, what it detects, what it produces, and how it relates to GitHub's existing
  pipeline security tools. Does NOT cover: cost per invocation, which programming
  languages are supported, how findings are deduplicated across runs, whether the
  command can be integrated into CI/CD pipelines, how scan scope is determined (current
  branch diff vs. full working tree), or whether experimental status applies to all
  Copilot plans or only specific tiers.

## Extracted Claims

### Claim 1: GitHub's Copilot CLI now has a dedicated `/security-review` slash command, released as experimental public preview — requiring `/experimental on` to access

- **Evidence**: Official GitHub product changelog announcing the feature as available
  in public preview. The experimental designation means it is gated behind experimental
  mode and may change before general availability.
- **Confidence**: settled (product fact — feature announced and available in official changelog)
- **Quote**: (no direct quote naming the command; command name and availability status
  confirmed across two independent fetches of the source)
- **Our assessment**: This is a distinct, named security command separate from general
  Copilot code review. Prior Copilot CLI security analysis was ad hoc — achieved by
  general Copilot prompting or rubber duck; `/security-review` is now a first-class
  slash command with defined scope and output format. The experimental designation
  mirrors the availability pattern documented in
  `docs-github-copilot-cli-rubber-duck-scheduling-voice.md` (Claim 9): rubber duck
  and voice input shipped GA; prompt scheduling and experimental terminal shipped
  experimental. `/security-review` follows the experimental path, meaning teams
  cannot rely on it for production workflows without accepting potential behavioral
  changes before GA. The pattern suggests a trajectory toward GA — consistent with
  how rubber duck moved from preview to GA.

### Claim 2: The command produces high-confidence security findings scored by severity and confidence, plus actionable recommendations usable within the terminal

- **Evidence**: Official changelog description of the command's output. The scoring
  dimensions (severity and confidence) and in-terminal actionability are explicitly
  stated in the source.
- **Confidence**: settled (product fact stated in official changelog)
- **Quote**: "High-confidence security findings, scored by severity and confidence"
- **Our assessment**: The severity + confidence scoring model is architecturally
  significant for adoption. Scoring by both dimensions enables structured triage:
  high severity / high confidence findings demand immediate action; lower-confidence
  findings warrant investigation before acting. This two-axis scoring mirrors the
  confidence-threshold approach Sentry uses for its `sentry-security` skill
  (HIGH/MEDIUM threshold) — both systems filter findings by confidence before
  surfacing them, reducing the false-positive burden that makes unfiltered LLM
  security review annotations noisy. The in-terminal actionability constraint
  suggests output is formatted for immediate developer response, not as a batch
  report requiring a separate tool to consume. The "high-confidence" framing implies
  the command does not surface all possible findings — it trades recall for
  precision, consistent with Claude Code's general security review characteristic
  (88.89% precision documented in `discussion-hn-autofix-hybrid-review.md` Claim 2,
  though measured on a different product — see Extraction Notes).

### Claim 3: The command targets five specific vulnerability categories: injection flaws, cross-site scripting (XSS), insecure data handling, path traversal, and weak cryptography

- **Evidence**: Official changelog enumerates the targeted vulnerability categories
  as the stated detection scope.
- **Confidence**: settled (product specification in official changelog)
- **Quote**: (no single verbatim quote lists all five; categories confirmed across
  both source fetches as the stated detection scope)
- **Our assessment**: The five categories represent a focused but meaningful threat
  taxonomy — broadly consistent with OWASP Top 10 coverage for common web and
  application vulnerabilities. The explicit enumeration of targets is architecturally
  analogous to the six vulnerability classes in Cursor's Agentic Security Review
  (`blog-cursor-security-agents.md`, Claim 5): both define a bounded threat model
  rather than promising open-ended vulnerability detection. Bounded scope helps
  practitioners calibrate expectations: `/security-review` is a scanner for a defined
  class of vulnerabilities, not a general security oracle. Teams with cryptographic
  or access-control requirements beyond these five categories need complementary
  tooling. Notably absent from the stated taxonomy: authentication bypasses, SSRF,
  race conditions, business logic vulnerabilities, and supply chain / dependency
  vulnerabilities — gaps the guide should surface when recommending `/security-review`
  as a security gate.

### Claim 4: The command is a Copilot-driven scan that operates independently of GitHub's existing pipeline security tools — it does not rely on code scanning, Dependabot, or secret scanning

- **Evidence**: Official changelog explicitly states the independence and the
  complementary positioning.
- **Confidence**: settled (stated definitively in official changelog)
- **Quote**: "This is a Copilot-driven scan that doesn't rely on GitHub code scanning,
  Dependabot, or GitHub secret scanning."
- **Our assessment**: This positioning is operationally important for teams that
  already use GitHub Advanced Security (GHAS). The `/security-review` command is
  additive — not a replacement — and runs at the developer's terminal rather than as
  a pipeline gate. The independence also means it can operate in repositories where
  GHAS is not licensed or enabled. For teams without GHAS: `/security-review` provides
  a Copilot-based substitute for targeted vulnerability categories. For teams with
  GHAS: the tool adds a pre-commit layer that catches issues before pipeline scanners
  run, reducing late-stage remediation cost. The explicit "doesn't rely on" framing
  also means the command's findings are generated independently — they may overlap
  with, contradict, or extend code scanning findings. Teams using both should expect
  some duplication in findings and may benefit from a triage workflow that reconciles
  both outputs.

### Claim 5: The command is designed for lightweight, on-demand pre-commit use as a complement to pipeline tools

- **Evidence**: Official changelog describes the intended use pattern explicitly and
  positions the tool relative to GitHub's existing pipeline security tooling.
- **Confidence**: settled (stated in official changelog)
- **Quote**: "a lightweight, on-demand way to review your changes before you commit"
- **Our assessment**: The "before you commit" positioning is the key architectural
  distinction from GitHub's pipeline tools (code scanning, Dependabot), which operate
  post-commit or post-PR-open. A pre-commit security layer adds a leftward-shift in
  the feedback loop: developers see security findings at the same point they would
  invoke rubber duck critique — both are terminal-native, on-demand, pre-commit. This
  is the CLI-native equivalent of Cursor's Agentic Security Review gate, but invoked
  by the developer interactively rather than triggered automatically on PR submission.
  The "lightweight" descriptor suggests the scan is tuned for speed appropriate to
  interactive pre-commit use, not deep analysis appropriate for a scheduled hardening
  campaign. Breunig's three-phase development cycle
  (`blog-simonwillison-cybersecurity-proof-of-work.md`, Claim 7) positions hardening
  runs at ~$12,500 each; this command occupies a lower-cost, higher-frequency slot —
  the Phase 2/3 boundary: more thorough than a code review pass, less intensive than
  a full hardening campaign.

## Concrete Artifacts

### `/security-review` Invocation Pattern

```
# Prerequisites
/experimental on          — activate experimental mode (required for access)

# Scan current project's local changes for security vulnerabilities
/security-review

# Output format:
#   - High-confidence security findings, scored by severity and confidence
#   - Actionable recommendations (implementable within the terminal)

# Note: scans local code modifications; designed for pre-commit use
```

*Source: GitHub Copilot CLI changelog, June 10, 2026*

### Vulnerability Detection Scope

```
Targeted vulnerability categories for /security-review (as of June 2026):
  1. Injection flaws
  2. Cross-site scripting (XSS)
  3. Insecure data handling
  4. Path traversal
  5. Weak cryptography

Not stated as in scope (gap areas for complementary tooling):
  — Authentication bypasses
  — Server-side request forgery (SSRF)
  — Race conditions / TOCTOU
  — Business logic vulnerabilities
  — Supply chain / dependency vulnerabilities (→ Dependabot)
  — Secrets detection (→ GitHub secret scanning)
```

*Source: GitHub Copilot CLI changelog, June 10, 2026*

### Updated Copilot CLI Verification and Feature Matrix

```
Feature                       Status         Enable
──────────────────────────────────────────────────────────────────
Rubber duck (/rubber-duck)    GA             (available by default)
Voice input                   GA             (available by default)
Prompt scheduling (/every,    Experimental   /experimental on
  /after)
Experimental terminal         Experimental   /experimental on
Security review               Experimental   /experimental on
  (/security-review)

CLI update command: copilot update
Feedback:          /feedback

Relationship to pipeline security tooling (not replaced by /security-review):
  — GitHub code scanning   → post-commit, pipeline
  — Dependabot             → dependency vulnerabilities, scheduled
  — Secret scanning        → secrets in committed code

Updated from docs-github-copilot-cli-rubber-duck-scheduling-voice.md
to include /security-review, announced June 10, 2026.
```

*Source: Combined from rubber-duck/scheduling/voice changelog (June 2, 2026) and this changelog (June 10, 2026)*

## Cross-References

- **Corroborates** `docs-github-copilot-cli-rubber-duck-scheduling-voice.md` (Claim 9):
  That source documented the two-tier availability pattern (GA vs. experimental) for
  Copilot CLI features and established that rubber duck and voice input are production-
  stable while prompt scheduling and terminal redesign remain experimental. This source
  adds `/security-review` as another experimental feature following the same gating
  pattern. Together, the June 2 and June 10 changelogs show GitHub systematically
  layering verification primitives into the CLI within a single week: rubber duck
  (quality/design peer review, GA), and now security review (vulnerability scanning,
  experimental). The CLI is evolving from a code-generation interface into a multi-
  layer pre-commit verification platform.

- **Corroborates** `blog-cursor-security-agents.md` (Claim 5): Cursor's argument that
  dedicated security agents "prompt-tuned to specific threat models" outperform
  general-purpose code review for security is directly instantiated here. GitHub made
  the architectural decision to build `/security-review` as a distinct named command
  rather than prompting Copilot to "review for security issues" — the same
  specialization principle Cursor applied when building their four-agent fleet. Both
  sources validate the design thesis: for security, a dedicated command with bounded
  threat scope outperforms a general-purpose review prompt.

- **Corroborates** `blog-simonwillison-cybersecurity-proof-of-work.md` (Claim 1):
  Breunig's proof-of-work framing argues that developers must outspend attackers in
  token-based security hardening. The `/security-review` command instantiates the
  low-cost end of that spectrum: a lightweight, on-demand, pre-commit terminal scan
  that requires no additional budget authorization. In Breunig's three-phase model
  (`blog-simonwillison-cybersecurity-proof-of-work.md`, Claim 7), this occupies the
  Phase 2/3 boundary — more thorough than a standard code review pass but far less
  resource-intensive than a full automated hardening campaign at $12,500 per run.
  The command reduces the friction of adding security review to every commit without
  requiring the budget authorization of a Phase 3 hardening run.

- **Extends** `docs-github-copilot-cli-rubber-duck-scheduling-voice.md`: That June 2
  changelog established the current Copilot CLI verification stack (rubber duck, voice,
  scheduling, terminal); this June 10 changelog adds a new verification layer. The
  rubber duck + `/security-review` combination creates a two-step pre-commit
  verification pattern: rubber duck for quality/design critique; `/security-review`
  for vulnerability detection — available entirely within native CLI commands with no
  external tooling, configuration, or pipeline integration required.

- **Extends** `docs-github-copilot-agent-skills-cli.md` (Claim 1): That source
  established the Copilot CLI as the primary surface for new GitHub agent feature
  development. This source continues the pattern: a security-specific CLI agent
  command joins rubber duck (peer review agent), prompt scheduling, and skills
  management as successive CLI-first feature releases. GitHub is consistently
  choosing the CLI as the initial delivery surface for new agent capabilities.

- **Related** `discussion-hn-autofix-hybrid-review.md` (Claim 2): The DeepSource
  benchmark (December 2025) measured "Claude Code" using "official security review
  command with diff simulation" and found 88.89% precision / 48.78% recall. Two
  important distinctions: (a) the benchmark tested Claude Code (Anthropic's CLI),
  not GitHub Copilot CLI's `/security-review` command — these are different products
  from different vendors; (b) the benchmark predates the `/security-review` command
  announcement by six months — the command did not exist when the benchmark ran.
  The benchmark data cannot be used to estimate `/security-review`'s precision or
  recall characteristics. Teams should not assume Copilot CLI's dedicated security
  command has the same precision/recall profile as the December 2025 Claude Code
  security review results.

- **Novel**:
  - **First dedicated security review slash command in Copilot CLI**: No prior corpus
    source documents a named, purpose-built security scanning command in Copilot CLI.
    Prior coverage of Copilot CLI security analysis was limited to general review
    via prompting or rubber duck critique. `/security-review` is a new first-class
    CLI primitive.
  - **Five-category vulnerability taxonomy as explicit product scope**: Prior corpus
    sources on AI security tooling either describe unbounded "security review" or
    enumerate specific CVE classes from benchmarks. This is the first source to
    define a product's security scanning scope as a named, exhaustive five-category
    list — establishing a scoping model other tools may adopt.
  - **Pre-commit, developer-initiated as a distinct security timing tier**: The corpus
    documents pipeline tools (Dependabot, code scanning), post-PR tools (Cursor
    Agentic Security Review, DeepSource Autofix Bot), and scheduled scanners (Cursor
    Vuln Hunter). This command introduces a new category: developer-initiated,
    pre-commit, interactive terminal security scan — a timing tier not previously
    documented in the corpus. Developers can now close the loop without waiting for
    CI, PR feedback, or a scheduled run.

## Guide Impact

### Chapter 03: Safety and Verification

- **Add `/security-review` as the lowest-friction pre-commit security gate in the
  guide's toolkit**: This command represents the simplest documented path to pre-commit
  security scanning — no configuration, no CI integration, no license gating required,
  invokable in any Copilot CLI session with `/experimental on`. Recommend as a default
  pre-commit habit for teams on Copilot CLI. The caveat: experimental status means it
  should not yet replace pipeline-based security tools for production workflows.
- **Document the five-category scope limitation explicitly**: Teams relying on
  `/security-review` as their primary security gate must understand it does not cover
  authentication bypasses, SSRF, race conditions, supply chain vulnerabilities, or
  secrets. Pair with pipeline tools (code scanning for other categories, Dependabot
  for supply chain, secret scanning for credentials) to achieve comprehensive coverage.

### Chapter 04: Agent Behaviors and Patterns

- **Name the CLI-native pre-commit verification stack**: The rubber duck + `/security-review`
  combination is the most complete pre-commit verification stack available from a
  single tool (Copilot CLI) without external infrastructure. Add as a named pattern:
  invoke `/rubber-duck` for quality and design critique, then `/security-review` for
  vulnerability detection before accepting or committing agent-generated code.
- **Use to illustrate the specialization principle**: This source alongside
  `blog-cursor-security-agents.md` (Claim 5) demonstrates why dedicated security
  commands beat general-purpose review: GitHub itself separated `/security-review`
  from general Copilot review, validating the architectural principle with a product
  decision. The guide can cite both as evidence for the recommendation to use
  specialized agents for security, not general-purpose prompts.

### Chapter 05: Tools and Frameworks — Copilot CLI

- **Update the Copilot CLI feature matrix**: Add `/security-review` (experimental,
  requires `/experimental on`) to the features table alongside rubber duck, voice
  input, and prompt scheduling. Reference the Concrete Artifacts section above for
  the updated matrix.
- **Clarify the complement positioning with GitHub Advanced Security**: The changelog
  explicitly states the command does not replace GitHub code scanning, Dependabot,
  or secret scanning. Teams with GHAS should deploy both; teams without GHAS can
  use `/security-review` as targeted coverage for the five categories. The guide
  should map these as complementary layers at different development lifecycle stages:
  `/security-review` (pre-commit, developer-initiated) + pipeline tools (post-commit,
  automated).

## Extraction Notes

1. **Source is a short changelog (~300 words)**: Two WebFetch calls were made to the
   source URL. The WebFetch tool summarized content rather than reproducing it verbatim.
   The three verbatim quotes in Claims 2, 4, and 5 were extracted from passages the
   tool placed in quotation marks (presented as direct quotations from the changelog).
   Claims 1 and 3 rely on consistent paraphrased descriptions across both fetches.
2. **Quote confidence**: The quotes "High-confidence security findings, scored by
   severity and confidence" (Claim 2), "This is a Copilot-driven scan that doesn't
   rely on GitHub code scanning, Dependabot, or GitHub secret scanning." (Claim 4),
   and "a lightweight, on-demand way to review your changes before you commit" (Claim 5)
   were obtained in quotation marks from the summarizing model's output across
   independent fetch passes. These are presented as verbatim, but the Assayer should
   verify against the source URL if precision is critical.
3. **No sub-pages linked**: The changelog does not link to detailed documentation
   for `/security-review`. The five vulnerability categories, command syntax, and
   availability gating are the full substantive content of the changelog entry.
4. **Experimental status**: All behavioral claims about command output are from an
   experimental public preview. Behavior may change before GA. Claims are marked
   settled where the product fact (feature exists, categories listed, output format
   described) is confirmed by the official changelog.
5. **DeepSource benchmark scoping**: The December 2025 DeepSource benchmark
   (`discussion-hn-autofix-hybrid-review.md`) measured Claude Code (Anthropic CLI),
   not GitHub Copilot CLI. The benchmark predates the `/security-review` command
   by six months. No precision/recall data exists in the corpus for this command.
6. **No contradictions identified**: The command is additive to the Copilot CLI
   feature set and explicitly positioned as complementary to, not replacing,
   GitHub's pipeline security tools. No existing corpus note makes claims that
   this source contradicts. No contradiction issue filed.
