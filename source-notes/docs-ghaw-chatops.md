---
source_url: https://github.github.com/gh-aw/patterns/chat-ops
source_type: docs
title: "GitHub Agentic Workflows: ChatOps Pattern"
author: GitHub Agentic Workflows team (GitHub Next / Microsoft Research)
date_published: null
date_extracted: 2026-05-01
last_checked: 2026-05-01
status: current
confidence_overall: emerging
issue: "#322"
---

# GitHub Agentic Workflows: ChatOps Pattern

> The authoritative reference for the `slash_command` trigger type in gh-aw —
> documents the command-trigger syntax, event-filter model, roles-based runtime
> access control, and sanitized-context injection as a prompt-injection defense;
> the first source note in the corpus to cover human-initiated agentic workflows
> via slash commands in GitHub comments.

## Source Context

- **Type**: docs (official GitHub Agentic Workflows documentation, Design
  Patterns > ChatOps section — prescriptive pattern reference, not a blog post
  or conceptual overview. Patterns pages document proven interaction models
  rather than architectural principles.)
- **Author credibility**: First-party from GitHub Next / Microsoft Research —
  the same team behind Peli de Halleux's "Agent Factory" blog series and the
  `gh aw` platform. Claims about the `slash_command` trigger schema, role
  enforcement behavior, and sanitization semantics are authoritative for this
  platform. Claims about generalizability of the HITL interaction model beyond
  gh-aw require additional evidence.
- **Scope**: The ChatOps pattern specifically — `slash_command` trigger syntax,
  `events:` field filtering, runtime role-based access control, sanitized
  context access, and prompt injection defense for human-triggered workflows.
  Does NOT cover: the five-layer security architecture (in
  `docs-ghaw-how-they-work.md`), MCP server integration (`docs-ghaw-mcps.md`),
  IssueOps or DispatchOps patterns (not addressed on this page), the
  compilation model or `gh aw compile` development workflow.

## Extracted Claims

### Claim 1: The `slash_command` trigger is a distinct gh-aw trigger type that activates a workflow when a user posts a matching slash command in a GitHub comment

- **Evidence**: The page shows the complete trigger schema with `name:` (the
  command string, e.g., `review` to activate `/review`), an optional `events:`
  field, and the integration with `permissions:` and `safe-outputs:` blocks.
  The pattern "enables automation into GitHub conversations through command
  triggers that respond to slash commands in issues, pull requests, and
  comments."
- **Confidence**: settled (first-party documentation; the trigger type exists
  and is operational on the gh-aw platform)
- **Quote**: "Command triggers respond to all comment contexts by default. Use
  the `events:` field to restrict where commands activate."
- **Our assessment**: This trigger type closes a gap in the existing corpus —
  no prior source note documents a human-initiated trigger for agentic
  workflows. Prior trigger types covered in existing notes are event-driven
  (push, PR open, schedule). The `slash_command` trigger is human-pull rather
  than system-push: a human explicitly requests agent action by typing a
  command. This is the mechanism that makes ChatOps interactive rather than
  automated. For Ch02 (Harness Engineering): `slash_command` belongs in the
  trigger taxonomy alongside schedule-based and event-based triggers. For
  Ch08/HITL chapters: this is the primary mechanism for human-in-the-loop
  interaction in the gh-aw model.

### Claim 2: The `events:` field provides six filter values that scope a slash command to specific comment contexts — including a distinction between issue comments and PR comments that both map to the same underlying GitHub event

- **Evidence**: The page documents six event identifiers:
  - `issues` — issue bodies (opened, edited, reopened)
  - `issue_comment` — comments on issues only (excludes PR comments)
  - `pull_request_comment` — comments on pull requests only (excludes issue comments)
  - `pull_request` — PR bodies (opened, edited, reopened)
  - `pull_request_review_comment` — PR review comments
  - `*` — all comment-related events (default when `events:` is omitted)
  Key clarification from the page: "Both `issue_comment` and
  `pull_request_comment` map to GitHub Actions' `issue_comment` event but with
  automatic filtering to distinguish between issue comments and PR comments."
- **Confidence**: settled (first-party; the six event identifiers are explicitly
  enumerated)
- **Quote**: "Both `issue_comment` and `pull_request_comment` map to GitHub
  Actions' `issue_comment` event but with automatic filtering to distinguish
  between issue comments and PR comments."
- **Our assessment**: The `issue_comment` / `pull_request_comment` distinction
  is significant because it reveals that gh-aw abstracts over a GitHub Actions
  limitation — the underlying `issue_comment` GitHub event fires for both issue
  and PR comments, requiring manual filtering in raw GitHub Actions. The gh-aw
  platform provides that filtering automatically via the `events:` field. This
  means a harness author can write `events: [pull_request_comment]` and be
  confident the workflow will not trigger on issue comments, without writing
  filtering logic in the workflow body. For Ch02: the `events:` field is an
  example of gh-aw providing harness ergonomics on top of raw GitHub Actions
  primitives — worth naming as a pattern where the platform absorbs complexity
  the author would otherwise manage manually.

### Claim 3: By default, the `slash_command` trigger restricts execution to users with admin, maintainer, or write permissions on the repository — a runtime access-control layer

- **Evidence**: Directly documented: "By default, workflows restrict execution
  to users with admin, maintainer, or write permissions." The `roles:` field
  accepts a list to customize (e.g., `roles: [admin, maintainer]` for stricter
  control). The platform enforces this at runtime before the agent executes —
  a comment containing a slash command from an unpermitted user will not trigger
  the workflow.
- **Confidence**: settled (first-party; the default role set and `roles:` field
  are explicitly documented)
- **Quote**: "By default, workflows restrict execution to users with admin,
  maintainer, or write permissions."
- **Our assessment**: This is a concrete authorization model for human-triggered
  agentic workflows. It answers the question "who can invoke the agent?" at the
  platform level, without requiring the harness author to write permission-check
  logic in the workflow body. The default (write+) is a reasonable threshold for
  repository collaboration — it excludes anonymous users and read-only observers.
  For Ch03 (Safety and Verification): this role-based runtime check is a
  meaningful access control layer specifically for ChatOps patterns. It prevents
  external actors from triggering agent workflows in open-source repositories
  simply by posting a comment. Cross-reference with `docs-ghaw-how-they-work.md`
  Claim 4 (no write access by default for agent outputs) — both operate as
  permission layers, but at different stages: this claim covers who can *invoke*
  the agent; the Safe Outputs model covers what the agent can *do* once invoked.

### Claim 4: Using `roles: all` in a public repository is a documented security risk — any authenticated GitHub user could trigger the workflow

- **Evidence**: The documentation explicitly warns: "Avoid `roles: all` in
  public repositories as any authenticated user could trigger workflows."
- **Confidence**: settled (first-party; the risk is directly named)
- **Quote**: "Avoid `roles: all` in public repositories as any authenticated
  user could trigger workflows."
- **Our assessment**: This is actionable security guidance with a clear threat
  model: in a public repository, GitHub authentication is not a meaningful
  authorization barrier because any GitHub account can authenticate. `roles: all`
  effectively makes the workflow open to the entire internet. The risk is
  resource abuse (spamming slash commands to consume workflow minutes and AI
  API tokens) and potentially prompt injection at scale (many users crafting
  malicious comment content to influence agent behavior). For Ch03: include
  `roles: all` as an anti-pattern with a concrete risk description. The
  default (write+) should be presented as the safe default for any public
  repository ChatOps workflow.

### Claim 5: User-provided slash command content is accessed via `steps.sanitized.outputs.text` — a sanitized output step that the platform injects before the agent's instruction body executes

- **Evidence**: The page documents the access pattern:
  `"Analyze this content: "${{ steps.sanitized.outputs.text }}""`. The
  sanitization step is platform-provided (not authored by the workflow writer)
  and runs before the agent's natural language instructions execute.
- **Confidence**: settled (first-party; the output reference is explicitly
  documented)
- **Quote**: (from the documentation's usage example)
  `Analyze this content: "${{ steps.sanitized.outputs.text }}"`
- **Our assessment**: `steps.sanitized.outputs.text` is the safe channel for
  consuming human-provided input in a ChatOps workflow. The pattern is
  analogous to parameterized queries in SQL — the user's input is processed
  through a sanitization layer before it reaches the agent's context, rather
  than interpolated directly. This is structurally superior to directly
  embedding GitHub event payload fields (e.g., `github.event.comment.body`)
  into the workflow's instruction body, because the sanitization layer filters
  before the agent sees the content. For Ch03 (Safety): name
  `steps.sanitized.outputs.text` as the correct access pattern for user-provided
  content in ChatOps workflows; using raw payload fields bypasses the
  sanitization step and increases prompt injection risk.

### Claim 6: The platform's sanitization step filters "unauthorized mentions, malicious links, and excessive content while preserving essential information"

- **Evidence**: The documentation states: "Sanitization filters unauthorized
  mentions, malicious links, and excessive content while preserving essential
  information." The sanitization is platform-provided — the harness author does
  not implement it; accessing content via `steps.sanitized.outputs.text` is
  sufficient.
- **Confidence**: emerging (the filter categories are named; the specific
  filtering logic is not disclosed. "Preserving essential information" while
  removing "malicious links" implies heuristic processing, which may have edge
  cases.)
- **Quote**: "Sanitization filters unauthorized mentions, malicious links, and
  excessive content while preserving essential information."
- **Our assessment**: The three filter categories (unauthorized mentions,
  malicious links, excessive content) are meaningfully distinct: unauthorized
  mentions likely prevents `@ghost-users` or `@all` spam; malicious links
  prevents embedding exfiltration URLs in agent context; excessive content
  prevents context-stuffing attacks that try to overwhelm the agent's
  instruction window. The "preserving essential information" qualification
  matters — sanitization is not a simple truncation; it is selective filtering.
  The opacity of the filtering logic is a mild concern: harness authors cannot
  know exactly what the agent sees vs. what was filtered. For Ch03: document
  this as the platform's injection defense at the input boundary, but note that
  it is a platform-provided heuristic, not a verifiable guarantee. Practitioners
  relying on this sanitization for security-critical workflows should layer
  additional defenses (e.g., narrow `roles:` configuration).

### Claim 7: The documentation's explicit security mandate for ChatOps is "treat user-provided content as untrusted" and design workflows to resist prompt injection

- **Evidence**: Direct quote from the page: "Treat user-provided content as
  untrusted. Design workflows to resist prompt injection attempts in issue
  descriptions, comments, or pull request content."
- **Confidence**: settled (this is a first-party security guidance statement
  from the platform documentation)
- **Quote**: "Treat user-provided content as untrusted. Design workflows to
  resist prompt injection attempts in issue descriptions, comments, or pull
  request content."
- **Our assessment**: This is the clearest prompt-injection guidance in the
  gh-aw corpus, stated in the context of human-triggered workflows. The
  guidance extends beyond the `steps.sanitized.outputs.text` pattern: even
  with sanitization in place, the workflow's instruction body should be written
  defensively (e.g., clear role framing, bounded scope, explicit rejection of
  instructions embedded in user content). For Ch03 (Safety and Verification):
  this quote belongs in the prompt-injection defense section as the canonical
  guidance for ChatOps workflows. It also generalizes: any workflow that
  processes user-supplied content (issue bodies, PR descriptions, comments)
  should treat that content as untrusted regardless of whether the `slash_command`
  trigger is used.

### Claim 8: ChatOps workflows use read-only permissions for the agent and route all write operations through Safe Outputs — consistent with the five-layer security model

- **Evidence**: The `/review` example uses `permissions: contents: read,
  pull-requests: read`. The documentation states: "the agent runs with
  read-only permissions while Safe Outputs (validated GitHub operations) handle
  write operations securely." The example's `safe-outputs:` block lists
  `create-pull-request-review-comment` and `add-comment` as the specific write
  operations permitted.
- **Confidence**: settled (first-party; the example is concrete and the design
  rationale is stated explicitly)
- **Quote**: "the agent runs with read-only permissions while [safe-outputs]
  (validated GitHub operations) handle write operations securely"
- **Our assessment**: This is the application of the Safe Outputs permission
  model (documented in `docs-ghaw-how-they-work.md` Claim 5) to the ChatOps
  pattern specifically. The concrete result: a `/review` command can post PR
  review comments (via `create-pull-request-review-comment`) and add comments
  (via `add-comment`), but the agent cannot directly push code, merge PRs, or
  modify repository settings. The `max: 5` annotation on
  `create-pull-request-review-comment` is notable — it caps the number of
  review comments the agent can post per invocation, preventing verbose
  reviews from flooding a PR. For Ch02: the `max:` annotation on safe-outputs
  is a new pattern not documented in prior notes — it provides a built-in
  rate-limiting mechanism for agent output volume.

### Claim 9: The Grumpy Code Reviewer is a named production example that combines slash-command triggering, cache-based memory across reviews, and read-only permissions

- **Evidence**: The documentation describes: "Triggered by `/grumpy` on PR
  comments, reviews code changes with a grumpy senior developer personality,
  identifying code quality issues and posting specific review comments. Uses
  cache memory to track previous reviews and avoid duplicate feedback."
  The workflow spec is available at
  `github.com/github/gh-aw/blob/main/.github/workflows/grumpy-reviewer.md`.
- **Confidence**: anecdotal (the description is from the platform documentation;
  the full spec at the linked URL was not fetched for this note)
- **Quote**: "Uses cache memory to track previous reviews and avoid duplicate
  feedback."
- **Our assessment**: The Grumpy Code Reviewer is notable for three reasons:
  (1) it demonstrates memory integration with ChatOps — cache-based state
  persists across invocations so the agent avoids repeating the same feedback;
  (2) it shows that a personality/persona can be embedded in a slash-command
  workflow (the "grumpy senior developer" framing is a prompt engineering
  choice, not a platform feature); (3) it is a concrete production example
  from the same team that built the platform, lending it practitioner credibility
  beyond a hypothetical demo. For Ch08 (Human-in-the-Loop): the memory +
  ChatOps combination is a design pattern for stateful conversational agents
  that remember context across multiple human interactions. The `avoid duplicate
  feedback` use case is a concrete motivation for why ChatOps workflows benefit
  from memory.

### Claim 10: ChatOps is suited for interactive, human-triggered scenarios — specifically code reviews, deployments, analysis, and triage — where the human controls when the agent acts

- **Evidence**: The page names four documented use cases: `/review` (code
  reviews), `/deploy staging` (deployments), `/analyze` (analysis), `/triage`
  (issue triage). The framing is that ChatOps "enables automation into GitHub
  conversations through command triggers" — the human initiates action, the
  agent responds.
- **Confidence**: anecdotal (use cases are listed without performance metrics
  or comparison data; no IssueOps/DispatchOps comparison is provided on this page)
- **Quote**: "enables automation into GitHub conversations through command
  triggers that respond to slash commands in issues, pull requests, and comments"
- **Our assessment**: The absence of a comparison to IssueOps and DispatchOps
  on this page means the "when to use ChatOps vs. alternatives" question is
  not answered here. Based on the pattern description alone: ChatOps is
  appropriate when (1) the trigger is a human decision rather than an automated
  event, and (2) the interaction context (the comment thread) is the natural
  place for the response. For on-demand workflows where the human does not have
  a strong contextual reason to initiate from a comment (e.g., running a one-off
  analysis not tied to a specific PR), IssueOps or DispatchOps might be more
  appropriate, but that comparison requires additional source evidence.

## Concrete Artifacts

### Slash Command Trigger — Full `/review` Example

```yaml
---
on:
  slash_command:
    name: review
    events: [pull_request_comment]
permissions:
  contents: read
  pull-requests: read
safe-outputs:
  create-pull-request-review-comment:
    max: 5
  add-comment:
---
# Code Review Assistant
When someone types /review in a pull request comment, perform a thorough
analysis of the changes. Examine the diff for potential bugs, security
vulnerabilities, performance implications, code style issues, and missing
tests or documentation. Create specific review comments on relevant lines
of code and add a summary comment with overall observations and recommendations.
```

*Source: docs-ghaw-chatops, ChatOps pattern reference — `/review` example*

### Slash Command Trigger — Event Filtering Example (`/triage`)

```yaml
---
on:
  slash_command:
    name: triage
    events: [issues, issue_comment]
---
# Issue Triage Bot
This command only responds when mentioned in issues, not in pull requests.
```

*Source: docs-ghaw-chatops, ChatOps pattern reference — `/triage` example*

### Event Identifier Reference Table

```
events: field values for slash_command trigger:

  issues                   — Issue bodies (opened, edited, reopened)
  issue_comment            — Comments on issues only (excludes PR comments)
  pull_request_comment     — Comments on pull requests only (excludes issues)
  pull_request             — PR bodies (opened, edited, reopened)
  pull_request_review_comment — PR review thread comments
  *                        — All comment-related events (DEFAULT when omitted)

Note: both `issue_comment` and `pull_request_comment` map to GitHub Actions'
`issue_comment` event but with automatic filtering by the gh-aw platform.
```

*Source: docs-ghaw-chatops, event filtering documentation*

### Sanitized Content Access Pattern

```yaml
# In the workflow's natural language instruction body:
Analyze this content: "${{ steps.sanitized.outputs.text }}"

# steps.sanitized.outputs.text is platform-injected before the agent executes.
# The sanitization step filters:
#   - unauthorized mentions
#   - malicious links
#   - excessive content
# while preserving essential information.
#
# DO NOT use ${{ github.event.comment.body }} directly —
# that bypasses sanitization and exposes the agent to raw user input.
```

*Source: docs-ghaw-chatops, sanitized context access documentation*

### Roles-Based Access Control Configuration

```yaml
# Default (admin, maintainer, write) — safe default for public repos
on:
  slash_command:
    name: review
    events: [pull_request_comment]

# Stricter — admin and maintainer only
on:
  slash_command:
    name: deploy
    events: [pull_request_comment]
    roles: [admin, maintainer]

# AVOID in public repos — any authenticated user can trigger:
# roles: all   ← anti-pattern for public repositories
```

*Source: docs-ghaw-chatops, role-based access control documentation*

### Grumpy Code Reviewer — Pattern Description

```
Name:    Grumpy Code Reviewer
Command: /grumpy (on PR comments)
Trigger: slash_command with events: [pull_request_comment]
Permissions: read-only (contents: read, pull-requests: read)
Memory:  Cache-based; tracks previous reviews to avoid duplicate feedback
Persona: "grumpy senior developer" — embedded in workflow instructions
Source:  github.com/github/gh-aw/blob/main/.github/workflows/grumpy-reviewer.md
```

*Source: docs-ghaw-chatops, Grumpy Code Reviewer example description*

## Cross-References

- **Corroborates**:
  - `docs-ghaw-how-they-work.md` Claim 5 (Safe Outputs as pre-approved write
    operations without write permissions): Claim 8 in this note is a direct
    application of the Safe Outputs pattern to ChatOps workflows. The `/review`
    example's `safe-outputs:` block shows exactly how a ChatOps workflow uses
    Safe Outputs — the agent has `read` permissions only; write operations
    (posting review comments, adding comments) go through the Safe Outputs
    channel. Both sources agree: agent reads, Safe Outputs writes.
  - `docs-ghaw-how-they-work.md` Claim 4 (no write access by default): The
    read-only permissions in the `/review` example (`contents: read,
    pull-requests: read`) are the ChatOps-specific instantiation of the
    platform's "no write access by default" principle (Claim 4 in that note).
    Both sources are consistent; this note provides the concrete example.
  - `docs-ghaw-how-they-work.md` Claim 10 (critical actions can require human
    approval): The ChatOps `slash_command` trigger is the mechanism through
    which humans exercise approval or initiation in the gh-aw model. Where
    Claim 10 describes human approval as a configurable gate on agent actions,
    ChatOps inverts the relationship — the human initiates via command, and
    the agent responds. Both patterns keep humans in control of when consequential
    actions occur.
  - `blog-ghaw-pelis-agent-factory-intro.md` — "Interactive & ChatOps Workflows"
    is listed as one of 19 series categories (Concrete Artifacts section), and
    the factory's task taxonomy includes use cases that map to ChatOps-style
    interaction. This note provides the implementation reference that the intro
    post names but does not detail.

- **Extends**:
  - `docs-ghaw-how-they-work.md` — that note covers the general trigger model
    (schedule-based, event-based) and the five-layer security architecture.
    This note extends it with the `slash_command` trigger type and its specific
    security considerations (roles-based access control, sanitized inputs) that
    apply uniquely to human-initiated workflows.
  - `docs-ghaw-mcps.md` Claim 1 (custom MCP servers must be read-only; write
    goes through Safe Outputs): the ChatOps read-only permission pattern
    (Claim 8 here) is consistent with and extends that note's read/write
    separation. MCP handles read-side tool integration; Safe Outputs handles
    write-side operations. ChatOps adds a human-trigger layer on top of this
    same architecture.
  - `docs-ghaw-agentic-authoring.md` Claim 8 ("what, not how" for instruction
    sections): the ChatOps workflow examples follow the "what, not how"
    principle — the `/review` instruction says what to analyze and what to
    produce, not how to analyze diffs. Consistent with the Planner pattern.

- **Contradicts**: None. The ChatOps page is fully consistent with the
  security architecture in `docs-ghaw-how-they-work.md`, the MCP read-only
  policy in `docs-ghaw-mcps.md`, and the authoring conventions in
  `docs-ghaw-agentic-authoring.md`. No existing source note makes claims that
  the `slash_command` trigger contradicts.

- **Novel**:
  - **`slash_command` trigger type** (Claim 1): No prior source note documents
    this trigger type. All existing GHAW trigger coverage is schedule-based or
    repository-event-based. The `slash_command` trigger is the first
    human-initiated trigger type in the corpus.
  - **`events:` field with six filter values including the `issue_comment` /
    `pull_request_comment` distinction** (Claim 2): The automatic filtering
    that distinguishes issue comments from PR comments (both map to the same
    underlying GitHub Actions event) is not documented in any existing source
    note. This is a platform ergonomics finding.
  - **Roles-based runtime access control** (Claims 3 and 4): The specific
    runtime permission check (admin/maintainer/write default; `roles: all`
    risk) is documented only here. No other source note describes a
    caller-identity check for workflow invocation.
  - **`steps.sanitized.outputs.text` as the safe input channel** (Claim 5):
    The specific output reference for accessing sanitized user content is new
    to the corpus. This is the concrete mechanism for prompt injection defense
    in ChatOps workflows.
  - **`max:` annotation on safe-outputs** (Claim 8): The `max: 5` on
    `create-pull-request-review-comment` as a volume-limiting mechanism for
    agent output is not documented in any existing source note. This extends
    the Safe Outputs model with a rate-limiting dimension.
  - **Memory + ChatOps integration** (Claim 9): The Grumpy Code Reviewer
    pattern (cache memory across invocations to avoid duplicate feedback)
    is the first documented example of stateful memory in a human-triggered
    agentic workflow.

## Guide Impact

### Chapter 02: Harness Engineering

- **Add `slash_command` to the trigger taxonomy** (Claim 1): The guide's
  trigger taxonomy currently covers schedule-based and repository-event-based
  triggers (per `docs-ghaw-how-they-work.md`). Add `slash_command` as the
  third trigger category — human-initiated, on-demand. The design decision
  is: use `slash_command` when the agent should respond to an explicit human
  request in a comment context; use event-based triggers when the agent should
  respond automatically to repository events.
- **Document `events:` field filtering as a harness ergonomics pattern** (Claim 2):
  The `events:` field demonstrates that gh-aw absorbs GitHub Actions complexity
  (the `issue_comment` event fires for both issue and PR comments; gh-aw filters
  automatically). Name this as a platform ergonomics pattern — the harness
  author specifies intent (`pull_request_comment`), not implementation
  (`github.event.issue.pull_request != null`).
- **Document `max:` on safe-outputs as a volume-control mechanism** (Claim 8):
  The `max: 5` annotation limits how many review comments the agent can post
  per invocation. This is a built-in rate-limiting pattern for agent output
  volume — relevant to any ChatOps workflow that could produce verbose output.

### Chapter 03: Safety and Verification

- **Add roles-based runtime access control as a ChatOps safety mechanism**
  (Claims 3 and 4): For any ChatOps workflow, the `roles:` configuration is the
  first line of defense — it determines who can invoke the agent. Recommend
  the default (write+) for all public repositories and document `roles: all`
  as an explicit anti-pattern with a concrete risk statement ("any authenticated
  user can trigger the workflow, enabling resource abuse and prompt injection
  at scale").
- **Name `steps.sanitized.outputs.text` as the required input channel** (Claims
  5 and 6): Add a concrete rule to the prompt injection defense section:
  ChatOps workflows must access user content via `steps.sanitized.outputs.text`,
  not via raw event payload fields (`github.event.comment.body`). The
  sanitization step filters unauthorized mentions, malicious links, and
  excessive content. Pair with the "treat user-provided content as untrusted"
  principle (Claim 7).
- **Add "treat user-provided content as untrusted" as a named mandate** (Claim 7):
  This quote belongs in Ch03 as a first-person directive from the platform
  builders. It is broader than ChatOps — any workflow that processes issue
  bodies, PR descriptions, or comment content should apply this principle.

### Chapter 08 / Human-in-the-Loop

- **`slash_command` as the canonical HITL interaction mechanism** (Claim 1):
  In the gh-aw model, ChatOps slash commands are how humans trigger agentic
  action on demand. Frame this as complementary to the human approval gate
  (from `docs-ghaw-how-they-work.md` Claim 10): the approval gate blocks agent
  action until a human approves; the slash command initiates agent action when a
  human decides it is needed. Together they give a HITL spectrum: passive gate
  (approve before action) and active invocation (request when needed).
- **Memory + ChatOps for stateful interaction** (Claim 9): The Grumpy Code
  Reviewer pattern demonstrates that ChatOps workflows can be stateful — cache
  memory persists context across invocations. This enables agents that remember
  prior interactions with the same PR or issue, avoiding repetitive output. Add
  as a design pattern for conversational agentic workflows.

## Extraction Notes

1. **Source is a patterns page, not a comprehensive reference**: The ChatOps
   patterns page provides representative examples and key guidance, but does not
   cover every configuration option exhaustively. The `slash_command` trigger
   field schema (e.g., whether additional fields exist beyond `name:`, `events:`,
   and `roles:`) is documented from the examples shown; additional fields may
   exist in the full CLI reference.

2. **No IssueOps/DispatchOps comparison on this page**: The triage comment
   identified comparison to IssueOps and DispatchOps as a key question. This
   page does not provide that comparison. The decision model for ChatOps vs.
   alternatives requires additional source evidence. Claim 10 includes the
   Miner's interpretive assessment rather than source-quoted guidance.

3. **Grumpy Code Reviewer spec not fetched**: The full `grumpy-reviewer.md`
   workflow spec is linked from the page but was not fetched for this note.
   Claim 9 is based on the page's description of the example. A separate mining
   of `github.com/github/gh-aw/blob/main/.github/workflows/grumpy-reviewer.md`
   would yield additional concrete artifacts (the full YAML spec and instruction
   text), but that is a distinct source requiring its own issue.

4. **Rendering note**: The page is an Astro/Starlight-rendered SPA. WebFetch
   returns rendered text. No interactive diagrams or video content is present
   on this page; the text content appears complete.

5. **No publication date**: The documentation does not carry an explicit
   publication date. `date_published` is left null. Content is consistent with
   gh-aw platform state as of 2026-05-01.

6. **No contradictions filed**: Reviewed all existing source notes. No claims
   in this source materially oppose existing source notes at the MINER.md §4a
   threshold. The ChatOps pattern is fully consistent with the five-layer
   security model in `docs-ghaw-how-they-work.md` and the MCP read-only policy
   in `docs-ghaw-mcps.md`.
