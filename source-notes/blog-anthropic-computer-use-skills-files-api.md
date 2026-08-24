---
source_url: https://claude.com/blog/computer-use-skills-api-files-api
source_type: blog-post
title: "Build production agents with computer use, the Skills API, and the Files API"
author: Anthropic (Claude.com blog)
date_published: 2026-08-20
date_extracted: 2026-08-24
last_checked: 2026-08-24
status: current
confidence_overall: emerging
issue: "#2907"
---

# Build production agents with computer use, the Skills API, and the Files API

> Anthropic's GA announcement for computer use (with a new browser use tool),
> the Skills API, and the Files API on the Claude Platform — positioning the
> three as composable building blocks for production agents that operate
> software, apply reusable domain expertise, and return finished files, backed
> by two enterprise customer testimonials with concrete before/after metrics.

## Source Context

- **Type**: blog-post (official claude.com product announcement, August 20, 2026)
- **Author credibility**: First-party Anthropic announcement. This is vendor
  communication marking a capability's transition from research
  preview/beta to general availability, plus two named customer
  testimonials (Asteroid, Box) with specific metrics attributed to named
  individuals (Davide Locatelli, Research Engineer at Asteroid; Matthew
  Midson, Managing Director of Banking at Box). The GA framing and technical
  specifics (multi-action turns, HIPAA BAA eligibility, rate limits, storage
  limits) are authoritative product statements. The customer metrics are
  self-reported by the customers via Anthropic's marketing copy, not
  independently audited — same caveat as any vendor case-study quote.
- **Scope**: Covers three GA capabilities and one new tool: (1) computer use,
  now supporting multiple actions per model turn and HIPAA BAA eligibility;
  (2) a new browser use tool that layers page-structure targeting on top of
  computer use for web apps; (3) the Skills API, a simplified upload/versioning
  API for custom Skills; (4) Files API enhancements — automatic expiration,
  5x higher rate limits, 1 TB org storage. Does NOT cover pricing details
  beyond a link, migration steps from the prior computer-use tool version, or
  independent benchmarks of the claimed speed/cost improvements. This note
  also folds in detail from the two documentation pages the post links to
  (Agent Skills overview, Files API guide) to fill in mechanics the blog post
  only gestures at.

## Extracted Claims

### Claim 1: Computer use, the Skills API, and the Files API are now generally available together, explicitly positioned as three composable building blocks for a single production agent
- **Evidence**: Opening framing statement plus a worked example (the "claims agent") that uses all three capabilities in one workflow: Files API for intake, a Skill for the filing procedure, browser use tool for portal submission, Files API again for the output.
- **Confidence**: settled (direct GA statement; the compositional example is presented as illustrative, not a benchmarked case)
- **Quote**: "Computer use, the Skills API, and the Files API are generally available on the Claude Platform today. Computer use also adds a new browser use tool for agents that work in web applications. Together they let you build agents that operate software, apply your team's expertise, and return finished files."
- **Our assessment**: This is the first source in the corpus to frame computer use, Skills, and Files as one composable capability triad rather than documenting them separately. The claims-agent example (read intake doc via Files API → follow a Skill encoding the filing procedure → submit via browser use tool → save confirmation via Files API) is a concrete, reusable reference architecture for "agent that touches an external system with no API," which is exactly the gap the March 2026 connector-first hierarchy (see [[blog-anthropic-dispatch-computer-use]]) identifies computer use as filling.

### Claim 2: The updated computer use tool takes several actions per model turn instead of one action per model call, reducing calls and latency for a given task
- **Evidence**: Stated as one of the "what's new with general availability" bullet items, without a specific quantified before/after latency number in the post itself (the Asteroid testimonial supplies a concrete number for one workflow — see Claim 5).
- **Confidence**: emerging (first-party architectural claim; no independent multi-workflow benchmark given, only one customer's single-workflow figure)
- **Quote**: "the updated computer use tool lets Claude take several actions per turn instead of one per model call, so tasks finish in fewer calls and less time"
- **Our assessment**: This is a meaningful harness-level change: prior computer-use guidance (see [[blog-anthropic-computer-use-best-practices]]) was written against a one-action-per-call tool. Practitioners with existing computer-use harnesses built around single-action turns should re-check whether their action-execution loop and screenshot-refresh logic still assume one action per response — multi-action turns change the loop's control flow, not just its speed.

### Claim 3: Computer use is now eligible for HIPAA-regulated workloads under Anthropic's Business Associate Agreement (BAA)
- **Evidence**: Stated directly in the "what's new" list, and corroborated by the Asteroid testimonial, which explicitly operates "inside healthcare and insurance systems."
- **Confidence**: settled (compliance-eligibility statements are the kind of claim vendors state precisely because they carry legal weight)
- **Quote**: "Computer use is also now eligible for HIPAA-regulated workloads under our BAA."
- **Our assessment**: This is new information to the corpus — no existing computer-use source note addresses regulatory eligibility. This directly changes the risk calculus for Chapter 03 (Safety and Verification) guidance: computer use was previously framed as "still early... starting with the apps you trust and not working with sensitive data" (dispatch-computer-use note, Claim 6); BAA eligibility signals Anthropic considers the safeguards mature enough for regulated health data, which is a meaningfully different trust posture from the March 2026 "trusted apps only" framing seven months earlier.

### Claim 4: The new browser use tool extends computer use to web applications by reading page structure and acting on specific elements, rather than clicking screen coordinates
- **Evidence**: Direct product description contrasting the mechanism with pixel-position clicking; described as using "the same multi-action turns and adds page structure, so agents target web elements more reliably than with pixels alone."
- **Confidence**: emerging (mechanism described qualitatively; no accuracy benchmark comparing browser use vs. pixel-based computer use given in the post)
- **Quote**: "Alongside the screenshot, the agent reads the structure of the page and acts on a specific field or button rather than a position on screen."
- **Our assessment**: This directly addresses the root-cause failure mode documented in the May 2026 best-practices post — click-accuracy problems caused by screenshot downscaling and coordinate-space mismatch (see [[blog-anthropic-computer-use-best-practices]], Claims 1–2). If browser use targets DOM/structural elements instead of screen coordinates for web targets, the entire `scale_coordinates()` / pixel-limit workaround documented in that post becomes unnecessary for web-app automation specifically — it would still apply to native desktop apps, where no page structure exists. The guide should note this is a *web-specific* fix, not a general computer-use fix.

### Claim 5: A named customer (Asteroid) reports a healthcare/insurance claims workflow that went from 32 minutes to 13 minutes, with cost per task falling about 30% and completion reaching 100%, after switching to the updated computer use tool with no prompt changes
- **Evidence**: Direct customer testimonial attributed to Davide Locatelli, Research Engineer at Asteroid, describing agents operating "inside healthcare and insurance systems that have no API."
- **Confidence**: anecdotal (single customer, self-reported, no methodology disclosed — sample size, task variance, or measurement window are not stated)
- **Quote**: "Our agents work inside healthcare and insurance systems that have no API. On the new computer use tool, our longest claims workflow went from 32 minutes to 13, cost per task fell about 30% across every workflow we tested, and completion hit 100%, with no changes to our prompts."
- **Our assessment**: The "no changes to our prompts" detail is the most useful part of this claim for practitioners — it implies the multi-action-turn upgrade (Claim 2) is a drop-in speed/cost improvement for existing computer-use harnesses, not something requiring a prompt rewrite to benefit from. That said, this is one customer's one workflow category; treat the specific 32→13 minute and 30% figures as illustrative upper-bound results, not an expected default improvement.

### Claim 6: A named customer (Box) uses the Skills API to encode a bank's proprietary credit methodology and memo format as a reusable Skill, applied automatically to that bank's existing documents to produce a source-grounded credit memo for analyst review
- **Evidence**: Direct customer testimonial attributed to Matthew Midson, Managing Director of Banking at Box, describing "Box Agent" applying a Skill to "financial statements and deal documents already in Box."
- **Confidence**: anecdotal (single customer testimonial, no metrics given for this example — unlike the Asteroid quote, no time/cost/accuracy numbers are stated)
- **Quote**: "The Skills API gave us a straightforward way to build specialized document creation into Box Agent. For a bank, a skill captures the firm's credit methodology and approved memo format; Box Agent applies it to the financial statements and deal documents already in Box and produces a source-grounded credit memo for analyst review. Banks get agents for complex workflows without building each one from scratch."
- **Our assessment**: This is a concrete illustration of the "reusable domain expertise via a Skill" pattern already documented for Claude Code Skills in [[blog-anthropic-claude-code-skills-lessons]] (Claim 4: skills as folders with scripts/assets/data, not just markdown), but applied at the *API/workspace* level via a third-party product (Box Agent) rather than inside Claude Code itself. It corroborates that Claude Code skills-lessons Claim 1's "skills are one of the most used extension points" pattern is generalizing beyond Claude Code into third-party agent products built on the Skills API.

### Claim 7: A Skill is defined as "a folder of instructions, scripts, and templates that Claude loads only when a task calls for it," which runs in Claude's code execution sandbox so the developer hosts nothing
- **Evidence**: Direct definitional statement in the post, corroborated by the linked Agent Skills documentation, which describes the same content types (instructions, executable code, reference materials) and states Skills "run in a sandboxed container with no network access and no runtime package installation" when used via the API.
- **Confidence**: settled (definitional/architectural claim, consistent across the blog post and the linked first-party docs)
- **Quote**: "a folder of instructions, scripts, and templates that Claude loads only when a task calls for it" — "They run in Claude's code execution sandbox, so there is nothing for you to host."
- **Our assessment**: This confirms and generalizes [[blog-anthropic-claude-code-skills-lessons]] Claim 4 (skills are folders, not just markdown) and Claim 5 (skills folders are a form of progressive disclosure) at the API level rather than the Claude Code CLI level. The "nothing for you to host" framing is new to the corpus — it's a deployment-model claim (managed sandbox execution) that the Claude Code-focused skills note does not make, since Claude Code skills execute on the user's own machine, not in a hosted sandbox.

### Claim 8: The Skills API is described in the announcement as "a simpler API for uploading and versioning your own skills" — the documentation specifies the underlying mechanism as `/v1/skills` endpoints referenced by `skill_id` in the `container` parameter, requiring the code execution tool
- **Evidence**: Blog post states the simplification claim without mechanism detail; the linked Agent Skills overview documentation supplies the mechanism: "Use pre-built Agent Skills by referencing their `skill_id`... or create and upload your own through the Skills API (`/v1/skills` endpoints)... Custom Skills are shared workspace-wide."
- **Confidence**: settled (API mechanism is a factual, first-party technical specification, not a marketing claim)
- **Quote**: "a simpler API for uploading and versioning your own skills" (blog post); "Custom Skills are shared workspace-wide: all workspace members can access them" (Agent Skills overview docs)
- **Our assessment**: "Simpler" is relative to what came before — the docs page does not describe a prior, more complex API, so the comparison point is implicit (likely: before this API existed, custom Skills for API use required manual container/file setup rather than a first-class versioned upload). The workspace-wide sharing model is a notable operational detail: it matches the Files API's workspace-scoped access model (Claim 10 below) and means Skills, like Files, are not scoped to an individual end user or API key — a security/isolation consideration for any practitioner building multi-tenant products on the Skills API.

### Claim 9: Skills use three-level progressive disclosure — YAML frontmatter metadata always loaded (~100 tokens), SKILL.md instructions loaded only when triggered (under 5k tokens), and bundled resources/scripts loaded only when referenced (zero cost until accessed)
- **Evidence**: The linked Agent Skills documentation provides an explicit table with token-cost estimates per level, plus a worked example (`pdf-processing` Skill) walking through startup → trigger → conditional file reads → script execution with output-only context cost.
- **Confidence**: settled (specific, first-party architectural specification with quantified token estimates per level)
- **Quote**: "This lightweight approach means you can install many Skills without context penalty: until a Skill is triggered, only its name and description occupy context." — "the script's code never loads into the context window. Only its output... consumes tokens"
- **Our assessment**: This is the most concrete articulation of "progressive disclosure" the corpus has for Skills — it quantifies what [[blog-anthropic-claude-code-skills-lessons]] Claim 5 states as a design principle ("the entire file system of a skill folder should be designed as a form of context engineering and progressive disclosure") without giving numbers. The `~100 tokens` per Skill at Level 1 is the load-bearing number for "no practical limit on bundled content" — it directly justifies why teams can install "many Skills" (per the internal-marketplace pattern in skills-lessons Claim 14) without a linear context tax per installed Skill.

### Claim 10: Files uploaded via the Files API are scoped to the entire workspace, not to an individual end user, conversation, or session — any API key in that workspace can access any file uploaded there, and the docs explicitly warn against accepting user-supplied file IDs
- **Evidence**: Explicit warning block in the Files API documentation: "Uploaded files are accessible to your entire workspace, not scoped to an end user, conversation, or session... Never accept `file_id` values from end users or other untrusted sources: a user-supplied file ID would let one user of your application read content that another user uploaded." The docs recommend a separate workspace per tenant for multi-tenant applications, with a stated cap of 100 workspaces per organization by default.
- **Confidence**: settled (explicit first-party security warning with a stated mitigation and a specific numeric limit)
- **Quote**: "Never accept `file_id` values from end users or other untrusted sources: a user-supplied file ID would let one user of your application read content that another user uploaded." — "The workspace is the isolation boundary for files, so a workspace per tenant gives each tenant's data hard isolation from every other tenant. Each organization can have up to 100 workspaces; contact your account team if you need more."
- **Our assessment**: This is a security-critical, easy-to-miss default that is not mentioned anywhere in the blog post itself — it only surfaces by reading the linked docs. Any practitioner building a multi-tenant product on the Files API who treats `file_id` as a capability token scoped to one user has a direct data-leak vulnerability. This is exactly the kind of concrete, non-obvious harness-security constraint the guide should surface explicitly rather than let practitioners discover in production.

### Claim 11: Files API GA enhancements are automatic file expiration (configurable 1 hour to 90 days at upload time), 5x higher rate limits, and 1 TB of storage per organization; file operations themselves (upload/download/list/delete) are free and only file content used in Messages requests is billed as input tokens
- **Evidence**: Blog post states the three headline enhancements; the linked Files API documentation supplies exact numbers: `expires_in_seconds` between 3,600 and 7,776,000 seconds, a 500 MB per-file maximum, 1 TB org total, and an explicit billing statement.
- **Confidence**: settled (specific first-party numeric limits stated in official API documentation)
- **Quote**: "Files API: automatic file expiration, 5x higher rate limits, and 1 TB of storage per organization." (blog post) — "Uploading files... Downloading files... Listing files... Getting file metadata... Deleting files [are free]. File content used in Messages requests is priced as input tokens." (Files API docs)
- **Our assessment**: The free-operations-except-token-billing model matters for cost modeling: a Files-API-heavy agent (upload intake doc, list files, retrieve metadata, delete when done) incurs no API line-item cost for the file lifecycle itself — cost only accrues when file content is actually read into a Messages request as context. This means the Files API is effectively "free storage with pay-per-read," which changes the cost calculus versus re-sending file content on every request (which would be billed as input tokens on every call, not just the first read).

### Claim 12: Computer use, the browser use tool, the Skills API, and the Files API are rolling out across multiple platforms at different paces — available on the Claude Platform and through Microsoft Foundry today, with updated computer use and browser use "coming soon" to Google Cloud's Vertex AI
- **Evidence**: Direct statement of platform availability in the post's closing section.
- **Confidence**: settled (platform-availability statements are factual claims a vendor states precisely, since customers make integration decisions based on them)
- **Quote**: "now available on the Claude Platform" and also "available through Microsoft Foundry," with "the updated computer use and browser use tools are coming soon to Google Cloud's Vertex AI."
- **Our assessment**: Notably, the Files API documentation separately states it is available on Claude Platform and Claude Platform on AWS / Microsoft Foundry (both beta) but explicitly "not available on Amazon Bedrock, Google Cloud" — a more specific and slightly different picture than the blog post's platform summary, which does not mention Bedrock or clarify the Files API's own multi-cloud status. Practitioners planning a multi-cloud deployment should check the current docs page rather than relying on the blog post's summary, since the two sources already show minor discrepancies seven months into GA rollouts historically moving quickly (per the cadence between the March, May, and August 2026 computer-use posts in this corpus).

## Concrete Artifacts

### Files API — upload and reference a file (Python, from linked docs)
```python
# Source: Files API documentation, linked from this announcement
uploaded = client.files.upload(
    file=("document.pdf", open("/path/to/document.pdf", "rb"), "application/pdf"),
)
file_id = uploaded.id

response = client.messages.create(
    model="claude-opus-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Please summarize this document for me."},
                {
                    "type": "document",
                    "source": {"type": "file", "file_id": file_id},
                },
            ],
        }
    ],
)
```

### Files API — storage, expiration, and error limits (from linked docs)
```
Maximum file size:       500 MB per file
Total storage:           1 TB per organization
Expiration window:       1 hour (3,600s) to 90 days (7,776,000s), set at upload
Rate limit:               ~500 requests/minute for file-related calls
Billing:                  upload/download/list/metadata/delete = free
                          file content read in a Messages request = billed as input tokens
Post-expiration behavior: content 404s immediately; metadata stays readable up to 30 days
```

### Skill folder structure and progressive-disclosure token cost (from linked Agent Skills docs)
```
pdf-processing/
  SKILL.md         <- Level 2: loaded only when Skill triggers (<5k tokens)
  FORMS.md         <- Level 3: loaded only if referenced (0 tokens until read)
  REFERENCE.md      <- Level 3: loaded only if referenced
  scripts/
    fill_form.py    <- Level 3: run via bash; only stdout enters context, not the code

YAML frontmatter (Level 1, always loaded, ~100 tokens/skill):
---
name: pdf-processing
description: Extract text and tables from PDF files, fill forms, merge documents.
             Use when working with PDF files or when the user mentions PDFs,
             forms, or document extraction.
---
```

### Skills API — required SKILL.md field constraints (from linked docs)
```
name:         max 64 chars; lowercase letters/numbers/hyphens only;
              no XML tags; cannot contain "anthropic" or "claude"
description:  non-empty; max 1024 chars; no XML tags;
              must state both WHAT the skill does and WHEN to use it
              (this is the string Claude matches the request against to decide
              whether to trigger the skill)
```

### Files API multi-tenant isolation warning (verbatim, from linked docs)
```
Uploaded files are accessible to your entire workspace, not scoped to an
end user, conversation, or session. Any API key in the same workspace can
access any file uploaded there... Never accept file_id values from end
users or other untrusted sources: a user-supplied file ID would let one
user of your application read content that another user uploaded.

Mitigation: create a separate workspace per tenant (up to 100 workspaces
per organization by default; contact account team for more).
```

## Cross-References

- **Corroborates**:
  - [[blog-anthropic-dispatch-computer-use]] (issue #177): Confirms and extends
    the March 2026 connector-first → computer-use fallback hierarchy — the
    claims-agent example in Claim 1 here is exactly the "no connector exists"
    scenario that post's Claim 1 describes, now shown composed with Skills and
    Files rather than computer use in isolation.
  - [[blog-anthropic-claude-code-skills-lessons]] (Claim 4, Claim 5): This
    post's Claim 7 and Claim 9 confirm, at the API level with token-cost
    numbers, the same "skills are folders, not just markdown" and
    "progressive-disclosure-as-context-engineering" claims that source made
    for Claude Code specifically. Claim 6 here (Box's credit-memo Skill) is a
    concrete third-party product illustration of that note's Claim 1 claim
    that skills are "one of the most used extension points," now generalizing
    beyond Claude Code into API-based third-party agent products.

- **Contradicts**: None found. No existing source note makes a claim this
  post's technical specifics conflict with. Note the minor internal
  discrepancy flagged in Claim 12 (blog post's platform summary vs. the
  Files API docs' more specific, slightly different platform-availability
  statement) — this is a same-source inconsistency, not a cross-source
  contradiction, and does not rise to a filed contradiction issue per
  MINER.md §4a (it's a stale-marketing-copy-vs-docs gap, not a claim that
  would change guide advice either way).

- **Extends**:
  - [[blog-anthropic-computer-use-best-practices]] (issue #735): The May 2026
    post's entire screenshot-scaling/coordinate-mapping section (Claims 1-2,
    the `scale_coordinates()` workaround) addresses a failure mode this
    post's Claim 4 (browser use tool, structural targeting instead of pixel
    coordinates) appears to obsolete for web-app targets specifically. The
    May post's guidance still applies unchanged for native desktop
    applications, where no page structure exists to target.
  - [[blog-anthropic-claude-code-verification-loops-skills]] (issue, not
    captured here): That post documents verification-skill patterns within
    Claude Code specifically (chaining, embedded loops). This post's Skills
    API section describes the same Skill packaging model at the
    API/workspace level, outside Claude Code — a different deployment
    surface for the same underlying Skill concept, with different sharing
    semantics (workspace-wide via API vs. personal/project-based filesystem
    skills in Claude Code, per the Agent Skills docs' "Sharing scope"
    section).

- **Novel**:
  - HIPAA BAA eligibility for computer use (Claim 3) — no existing source
    note addresses regulatory/compliance eligibility for any agentic
    capability in the corpus.
  - The browser use tool as a distinct, structurally-aware variant of
    computer use (Claim 4) — new tool, not previously documented.
  - Files API workspace-scoping security warning and the accompanying
    multi-tenant-isolation-via-separate-workspaces mitigation (Claim 10) —
    new to the corpus and directly actionable for anyone building a
    multi-tenant product on Files.
  - Quantified per-level token costs for Skills progressive disclosure
    (Claim 9: ~100 tokens metadata, <5k tokens instructions, 0 until accessed
    for resources) — the existing Claude Code skills note states the
    principle but not the numbers.
  - Free-except-input-tokens billing model for the Files API lifecycle
    (Claim 11) — new cost-modeling detail.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add a section on the Skills API +
  Files API + computer use/browser use composition pattern, anchored by the
  claims-agent worked example (Claim 1). This is a concrete reference
  architecture for "agent needs to read a document, apply team-specific
  procedure, act in a system with no API, and return a finished artifact" —
  a pattern distinct from the pure connector/MCP integration path the guide
  already covers.

- **Chapter 02 (Harness Engineering — computer use)**: Update the existing
  computer-use guidance (anchored on [[blog-anthropic-computer-use-best-practices]])
  to note that multi-action turns (Claim 2) change the per-call action-loop
  assumptions that guide's screenshot-refresh and coordinate-scaling code
  examples were written against, and that the new browser use tool (Claim 4)
  removes the need for `scale_coordinates()`-style pixel-mapping workarounds
  specifically for web targets, while native-desktop targeting is unchanged.

- **Chapter 03 (Safety and Verification)**: Add the Files API workspace-scoping
  warning (Claim 10) as a named security consideration for any harness that
  lets end users reference files by ID — flag "never accept a user-supplied
  file_id" as a concrete anti-pattern with a stated exploit (cross-user data
  read) and the workspace-per-tenant mitigation.

- **Chapter 03 (Safety and Verification)**: Note HIPAA BAA eligibility for
  computer use (Claim 3) as a data point when updating any prior guidance
  that characterized computer use as unsuitable for sensitive data — this
  doesn't mean "safe by default," but it changes the regulatory-eligibility
  baseline established in March 2026.

- **Chapter 04 (Advanced Patterns)**: Add the quantified Skills progressive-disclosure
  token model (Claim 9: ~100 tokens/skill metadata, <5k tokens for triggered
  instructions, zero for unread resources) as the concrete numbers backing
  the "install many skills without context penalty" design principle already
  described qualitatively in [[blog-anthropic-claude-code-skills-lessons]].

## Extraction Notes

- The blog post itself is short (~5 minute read per its own metadata) and
  light on mechanism detail; most of the technically substantive material in
  this note (Claims 7-11, all Concrete Artifacts) came from following the two
  most load-bearing linked documentation pages — the Agent Skills overview
  and the Files API guide — both fetched in full per MINER.md's
  follow-up-to-5-links guidance. Two other linked docs pages (computer use
  tool reference, browser use tool reference) were not fetched; they would
  likely yield additional API-mechanism claims for a future source note if
  the guide needs deeper computer-use API implementation detail than
  [[blog-anthropic-computer-use-best-practices]] already provides.
- WebFetch processes HTML through an intermediate model before returning
  text, so quotes attributed to the blog post itself (as opposed to the
  documentation pages, which were returned as close-to-raw Mintlify/Markdown
  source) carry a small residual risk of not being byte-exact, despite two
  separate fetch passes returning consistent wording for every quote used
  here. The documentation-page quotes are higher-confidence since those pages
  were returned as structured Markdown that reads as a direct rendering of
  the source rather than a summarization.
- No paywall or access issues. All three URLs (blog post, Agent Skills docs,
  Files API docs) are public.
- The two customer testimonials (Asteroid, Box) are the only quantified
  before/after metrics in the post; both are single-customer, self-reported,
  and without disclosed methodology — treated as anecdotal per MINER.md
  confidence grading, not settled, despite being first-party-published.
