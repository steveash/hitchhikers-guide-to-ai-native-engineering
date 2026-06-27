---
source_url: https://simonwillison.net/2026/Jun/18/datasette-apps/
source_type: blog-post
title: "Datasette Apps: Host custom HTML applications inside Datasette"
author: Simon Willison
date_published: 2026-06-18
date_extracted: 2026-06-27
last_checked: 2026-06-27
status: current
confidence_overall: emerging
issue: "#1328"
---

# Datasette Apps: Host custom HTML applications inside Datasette

> Simon Willison documents the datasette-apps plugin — a system for hosting
> sandboxed HTML+JavaScript applications inside Datasette, with defense-in-depth
> security (iframe sandbox + Content Security Policy), a MessageChannel-based API,
> and explicit support for LLM-generated apps — built using three AI models in
> specialized roles and hardened by a Fable 5 security evaluation that discovered
> a privilege-escalation-via-exfiltration attack.

## Source Context

- **Type**: blog-post (Simon Willison's weblog, June 18, 2026; a substantive
  feature announcement covering architecture, security mechanisms, development
  process, and future direction for the new datasette-apps plugin. The post
  has five named sections: "The TL;DR", "Why build this?", "Neat ideas in
  Datasette Apps", "Built with so much AI assistance", and "It's looking good
  so far". Length is substantial — multiple paragraphs per section, code
  examples, and security analysis.)
- **Author credibility**: Simon Willison is the creator of Datasette and the
  `llm` Python CLI. He is the primary developer of Datasette Agent and the
  datasette-apps plugin. This is first-party documentation of a system he
  built himself, with named model usage, specific security vulnerability
  details, and a clear development chronology. He has no vendor affiliation
  with Anthropic or OpenAI. His Datasette notes in this corpus are consistently
  first-party, authoritative, and technically specific.
- **Scope**: Covers the datasette-apps plugin's sandbox security architecture
  (iframe + CSP + MessageChannel), the JavaScript datasette API for in-app
  queries, write access via stored queries, the LLM-friendly copyable-prompt
  design, the multi-model development workflow, a specific Fable 5-discovered
  security vulnerability and its fix, and the tool's positioning in Datasette's
  broader evolution. Does NOT cover: internal plugin implementation details,
  performance benchmarks, full plugin API documentation, or the Datasette Cloud
  integration roadmap for this feature.

## Extracted Claims

### Claim 1: Datasette Apps run in `<iframe sandbox="allow-scripts allow-forms">` combined with an injected Content Security Policy meta tag, creating defense-in-depth isolation that prevents cookie access and external data exfiltration

- **Evidence**: First-party documentation from the tool's creator; specific
  attribute value and CSP string provided verbatim in the post. The "defense
  in depth" framing is Willison's own characterization of the layered approach.
- **Confidence**: settled (first-party author documentation; the specific
  technical mechanisms — sandbox attribute, CSP tag — are concrete and
  verifiable by inspection of the plugin source)
- **Quote**: "the `<iframe sandbox="allow-scripts allow-forms">` they run in
  prevents them from accessing cookies or localStorage"
  *(Source: simonwillison.net/2026/Jun/18/datasette-apps/)*
- **Quote (CSP tag)**: "`<meta http-equiv=\"Content-Security-Policy\" content=\"default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; img-src data: blob:;\">`"
  *(Source: simonwillison.net/2026/Jun/18/datasette-apps/)*
- **Our assessment**: The two-layer isolation design is architecturally significant.
  The `sandbox` attribute prevents the iframe from accessing the parent's cookies
  or localStorage — protecting session credentials. The CSP meta tag blocks all
  external network requests from within the iframe (`default-src 'none'`), preventing
  data exfiltration to external hosts. Together they address two distinct attack
  classes: credential theft (sandbox) and data leakage (CSP). The CSP is injected
  as a meta tag by Datasette at serve time, not supplied by the app itself — this
  means a malicious app cannot override it or weaken the network restrictions. This
  design is specifically relevant to systems that host LLM-generated code, where the
  generated code may contain unintentional or intentional exfiltration vectors.

### Claim 2: Datasette Apps use MessageChannel() for parent-to-iframe communication rather than postMessage(), because MessageChannel channels close automatically when the frame navigates to another URL

- **Evidence**: Willison's direct statement of the architectural decision and
  its rationale; he describes the initial postMessage() prototype explicitly.
- **Confidence**: emerging (first-party; the rationale — channel auto-close on
  navigation — is stated directly and is technically accurate for MessageChannel)
- **Quote**: "I built the first version of this with `postMessage()`, which allows a
  child iframe to send messages to the parent window."
  *(Source: simonwillison.net/2026/Jun/18/datasette-apps/)*
- **Quote (MessageChannel rationale)**: "I ported to a MessageChannel() based
  transport instead. `MessageChannel()` has the advantage that if a page navigates
  to somewhere else the channel closes automatically."
  *(Source: simonwillison.net/2026/Jun/18/datasette-apps/)*
- **Our assessment**: The channel-teardown-on-navigation property is the key
  security advantage of MessageChannel() over postMessage(). With postMessage(),
  a malicious app could navigate the frame to an attacker-controlled page and
  continue sending messages (potentially containing data) to the parent. With
  MessageChannel(), the authenticated channel is established at iframe load time
  and destroyed if the frame navigates away — any subsequent communication from a
  navigated frame would require establishing a new, unauthenticated channel, which
  Datasette would reject. The progression from postMessage() to MessageChannel()
  is the kind of security hardening that requires either deep browser API knowledge
  or an AI interlocutor to surface — Willison attributes this change to GPT-5.5.

### Claim 3: Write access from Datasette Apps is restricted to pre-configured stored queries only — apps cannot execute arbitrary SQL for write operations

- **Evidence**: Willison's direct description of the write access design;
  the JavaScript API example confirms the constraint at the code level.
- **Confidence**: settled (first-party; the stored-query restriction is described
  as the architectural choice for write safety, not as a current limitation)
- **Quote**: "Users can create a stored write query that performs an insert or
  update, then allow-list that specific query for an app."
  *(Source: simonwillison.net/2026/Jun/18/datasette-apps/)*
- **Our assessment**: This is the right design choice for a system that hosts
  LLM-generated apps with database write access. Arbitrary SQL write access would
  be extremely dangerous — a malicious or buggy LLM-generated app could DROP tables,
  UPDATE every row, or INSERT attacker-controlled data. Restricting writes to
  pre-configured, administrator-approved stored queries narrows the attack surface
  to what the administrator explicitly permitted. The `datasette.storedQuery()`
  call in app code references a named query; the query itself lives in Datasette's
  controlled configuration, not in the app code. This separates the concern of
  "what can an app do" from "what SQL does that action translate to" — an important
  defense-in-depth boundary. This parallels the approval-gate pattern documented
  in `blog-simonwillison-datasette-agent-write-sql.md` Claim 1, extended to the
  app context where no human is present for per-operation approval.

### Claim 4: Datasette Apps include a "copyable prompt" in the create-app form that contains the schema of selected databases, enabling users to paste directly into an LLM to generate app code

- **Evidence**: Willison's direct description of the create-app form UX feature.
- **Confidence**: settled (first-party; the UI feature is described explicitly)
- **Quote**: "These self-contained apps are the perfect shape to be written by a
  modern LLM."
  *(Source: simonwillison.net/2026/Jun/18/datasette-apps/)*
- **Our assessment**: This is the most strategically interesting aspect of
  Datasette Apps for the guide. The copyable-prompt pattern inverts the typical
  "AI writes tools for developers" flow: here, the data tool provides a structured
  prompt with schema context that any user — not just developers — can paste into
  Claude, ChatGPT, or Gemini to generate a working database-backed app. The "perfect
  shape" characterization is load-bearing: the app format (self-contained HTML +
  JavaScript with no external dependencies, communicating via a single API object)
  is deliberately designed to match what LLMs generate well. LLMs produce
  self-contained HTML files reliably; they struggle more with multi-file projects
  requiring coordinated changes. Datasette Apps' single-file format plays to this
  capability.

### Claim 5: Datasette Apps expose a `datasette` JavaScript object to apps with `query()` for read-only SQL and `storedQuery()` for write operations; query logs and CSP errors are surfaced visibly for debugging

- **Evidence**: Code example from the post demonstrates the API; the visible-logs
  feature is described in the "Neat ideas" section.
- **Confidence**: settled (first-party; code example is verifiable by inspection)
- **Quote**: (no single direct quote covering both methods; see Concrete Artifacts
  for the code example verbatim)
- **Our assessment**: The explicit separation of `query()` (arbitrary read-only SQL)
  and `storedQuery()` (named write operations) at the JavaScript API level makes
  the security boundary visible to app authors at coding time, not just at runtime.
  An app author who wants to insert data must explicitly call `storedQuery()` with
  a named operation — they cannot pass arbitrary SQL. The visible log surfacing
  (SQL query logs and CSP errors shown in the Datasette UI) is a developer experience
  choice with a security benefit: CSP violations are immediately visible to the
  administrator running the app, making blocked exfiltration attempts observable.
  This is a useful pattern for any system hosting untrusted code.

### Claim 6: Datasette Apps were motivated partly by Claude Artifacts' limitation — they lack persistent database access — and position Datasette as the backend that Artifacts conceptually need

- **Evidence**: Willison's "Why build this?" section naming Claude Artifacts as
  one of three influences.
- **Confidence**: anecdotal (author's stated motivation; the comparison is
  architectural, not benchmarked)
- **Quote**: "adding a Datasette-style backend to a self-contained HTML frontend
  is an astonishingly powerful combination"
  *(Source: simonwillison.net/2026/Jun/18/datasette-apps/)*
- **Our assessment**: Claude Artifacts are self-contained HTML/CSS/JS files that
  Claude generates and the user can view interactively. Their limitation is that
  they have no persistent data layer — state resets with each new artifact. Datasette
  Apps fill this gap: the same self-contained HTML format, but with access to a
  persistent SQLite database via the `datasette` JavaScript object. The combination
  Willison describes (Datasette backend + self-contained HTML frontend) is effectively
  the stateful version of what Artifacts do. This is a notable architectural
  observation: browser-rendered LLM-generated HTML becomes significantly more capable
  when connected to a structured data layer, even via a narrow, pre-approved API.

### Claim 7: Claude Fable 5 performed a security evaluation of Datasette Apps and identified a privilege-escalation-via-exfiltration attack: a less-privileged user with `create-app` permission creates a malicious app to steal an admin's data

- **Evidence**: Willison's direct description of the security review and its
  finding, including the specific attack vector named.
- **Confidence**: settled (first-party; the vulnerability is described with
  enough specificity to be credible — named permission, named mechanism, named
  mitigation)
- **Quote**: "A less privileged user with `create-app` permission creates an app
  that queries SQLite for all available tables and exfiltrates data to an
  allow-listed host. They trick an administrator into visiting their app, which
  can then run queries as that user."
  *(Source: simonwillison.net/2026/Jun/18/datasette-apps/)*
- **Our assessment**: This is the most guide-relevant security finding in the
  source. The attack is not a technical bypass of the sandbox — the sandbox still
  works. The attack exploits the *social engineering* surface: the privilege model
  allows less-trusted users to create apps, and the CSP allow-list allows those
  apps to communicate with external hosts. An attacker with `create-app` permission
  creates an app that, when visited by an admin, uses the admin's higher-privilege
  session to run queries and send results to the attacker's allowed host. This is
  a confused deputy attack at the permission model level, not a sandbox escape. The
  fact that Fable 5 identified this independently (not the human designer) demonstrates
  that LLM security evaluation can surface non-obvious threat vectors in new systems
  — specifically threats that arise from combining correct individual components
  (working sandbox, working CSP allow-list) in a way that creates an emergent risk.

### Claim 8: The `apps-set-csp` permission restricts CSP domain allow-listing to trusted staff, closing the privilege-escalation vulnerability without removing write-capable CSP origins entirely

- **Evidence**: Willison's direct description of the fix applied after Fable 5
  identified the vulnerability.
- **Confidence**: settled (first-party; specific permission name and design
  rationale provided)
- **Quote**: "I fixed it by restricting the ability to allow-list any domain to
  a new `apps-set-csp` permission, which is intended just for trusted staff."
  *(Source: simonwillison.net/2026/Jun/18/datasette-apps/)*
- **Our assessment**: The fix is minimal-surface: it doesn't remove CSP allow-listing
  (which is legitimately useful for apps that need external libraries) — it promotes
  the configuration of allowed origins to a separate, higher-trust permission class.
  An alternative approach — pre-configuring an `allowed_csp_origins` list as
  administrator-controlled configuration — is also noted in the post, allowing regular
  users to select from approved sources without holding the `apps-set-csp` permission
  themselves. The two-tier design (admin configures allow-list, user selects from it)
  is a robust pattern for similar systems: separation of "defining the allow-list"
  from "using items from the allow-list." This is a directly transferable pattern
  for any system where LLM-generated code needs to communicate with external services.

### Claim 9: Development used three AI models in specialized roles: Claude Opus 4.6 for implementation (via Claude Code), GPT-5.5 / Codex Desktop for planning and transport architecture, and Claude Fable 5 for security evaluation

- **Evidence**: Willison's "Built with so much AI assistance" section names specific
  models and their roles in the development of the plugin.
- **Confidence**: emerging (first-party; the model-to-role mapping is explicitly
  stated by the author)
- **Quote**: "mainly built using Claude Opus 4.6 in Claude Code"
  *(Source: simonwillison.net/2026/Jun/18/datasette-apps/; referring to
  the initial datasette-agent-artifacts prototype)*
- **Our assessment**: The three-model workflow documents a specialization pattern:
  one model for implementation (Claude Opus 4.6 in Claude Code, which has strong
  code-generation and multi-file editing), another for planning and transport
  architecture (GPT-5.5 / Codex Desktop, which suggested the MessageChannel
  transport port over postMessage()), and a third specifically for security
  evaluation (Fable 5, which identified the privilege-escalation attack). This
  is not just a multi-model workflow — each model was selected for a distinct
  role that maps to its known strengths. This corroborates the pattern documented
  in `blog-simonwillison-csrf-multimodel-review.md` Claim 2 (multi-model
  cross-review: Claude Code for implementation, a second model for review),
  extending it to a three-model design-implement-audit division of labor.

### Claim 10: The post explicitly links Fable 5's security evaluation capability to the US government export controls on the model, positioning the security review as an example of the capability that was later restricted

- **Evidence**: Willison's editorial note in the "Built with so much AI assistance"
  section, with a link to his prior coverage of the export control directive.
- **Confidence**: anecdotal (editorial framing; the underlying facts — Fable 5
  export controls, its security evaluation capability — are documented in other
  corpus sources)
- **Quote**: (no direct verbatim quote available with certainty; the post states
  that Fable 5's security evaluation ability "would get it banned by the US
  government" with a link to the export control directive; see Our assessment)
- **Our assessment**: The editorial observation connects the datasette-apps security
  review to the broader Fable 5 export control controversy documented in
  `blog-simonwillison-fable-5-export-controls.md` Claim 1: the "jailbreak" that
  triggered export controls was asking a model to review/fix vulnerable code — which
  is exactly what Willison did when he asked Fable 5 to evaluate Datasette Apps'
  security. The irony Willison highlights: a model capability that was genuinely
  useful for defensive security (finding a real vulnerability in a new system) is
  the same capability the government characterized as a jailbreak. This is the
  most politically significant claim in the post and the one most likely to date
  quickly; it should be read alongside the export-controls corpus notes.

### Claim 11: Datasette Apps represent a capability evolution arc: Datasette went from read-only data publishing → agent-readable SQL → agent-writable SQL → user app-hosting, with each step driven by AI capability expansion

- **Evidence**: Willison's "It's looking good so far" section frames Datasette Apps
  as the latest step in this evolution.
- **Confidence**: anecdotal (author's retrospective framing of a trajectory he
  lived through; the individual steps are separately documented in corpus notes)
- **Quote**: (no single direct quote captures the full arc; see Our assessment)
- **Our assessment**: The evolution Willison describes can be reconstructed across
  corpus source notes: Datasette started as a read-only data exploration and
  publishing tool; Datasette Agent (May 2026, `blog-simonwillison-datasette-agent.md`)
  added LLM-driven conversational SQL querying; datasette-agent 0.3a0 (June 15,
  2026, `blog-simonwillison-datasette-agent-write-sql.md`) added agent-gated write
  SQL; datasette 1.0a34 (June 16, 2026, `blog-simonwillison-datasette-1-0a34.md`)
  added CRUD UI driven by the agent write capability; and now datasette-apps (June
  18, 2026) adds user app-hosting. Each step was enabled by AI capability: agents
  needed SQL access, agents needed write access, UIs needed to match agent
  capabilities, and now apps need to be generated by LLMs. This is a concrete
  multi-step case study of how AI agent development drove iterative expansion of
  an underlying data tool's scope beyond its original read-only conception.

## Concrete Artifacts

### The datasette.storedQuery() JavaScript API (from simonwillison.net/2026/Jun/18/datasette-apps/)

```javascript
const result = await datasette.storedQuery("todos", "add_todo", {
  title: "Buy milk",
  due_date: "2026-06-20",
  priority: "high",
  completed: false
});
```

*Source: simonwillison.net/2026/Jun/18/datasette-apps/, June 18, 2026.
Arguments: database name ("todos"), stored query name ("add_todo"), and
a parameters object. The stored query template must be pre-configured by
an administrator — apps cannot provide arbitrary SQL for write operations.*

### Sandbox and CSP Configuration (from simonwillison.net/2026/Jun/18/datasette-apps/)

```
Iframe sandbox attribute:
  <iframe sandbox="allow-scripts allow-forms">
  Effect: prevents access to parent cookies or localStorage

Injected CSP meta tag (added by Datasette at serve time, not by the app):
  <meta http-equiv="Content-Security-Policy"
    content="default-src 'none'; script-src 'unsafe-inline';
             style-src 'unsafe-inline'; img-src data: blob:;">
  Effect: blocks all external network requests from the app

Defense-in-depth layers:
  1. sandbox= attribute: isolates app from parent window credentials
  2. CSP tag: prevents external data exfiltration via network
  3. MessageChannel(): channel auto-closes if frame navigates away
  4. Stored queries only: no arbitrary SQL for write operations
  5. apps-set-csp permission: only trusted staff can add CSP origins
```

*Source: simonwillison.net/2026/Jun/18/datasette-apps/, June 18, 2026.*

### Privilege-Escalation Attack Pattern (Fable 5 discovery)

```
Attack: Confused-deputy privilege escalation via CSP allow-listed exfiltration

Attacker prerequisites:
  - Datasette account with `create-app` permission (less privileged user)
  - Knowledge of an admin's Datasette instance
  - At least one CSP-allow-listed external host

Attack steps:
  1. Attacker creates an app that runs SELECT queries across all tables
  2. App sends query results to the CSP-allow-listed external host
  3. Attacker tricks admin into visiting the app URL
  4. App executes with admin's session credentials (full read access)
  5. Data exfiltrated to attacker's server without sandbox bypass

Root cause:
  - CSP allow-list configuration was accessible to any user with create-app
    permission, not restricted to trusted staff
  - Attacker's app uses victim's (admin's) query permissions when visited

Fix:
  - New `apps-set-csp` permission gates CSP allow-list configuration
  - Alternative: administrator pre-configures allowed_csp_origins; regular
    users can only select from that pre-approved list
```

*Source: Simon Willison, simonwillison.net/2026/Jun/18/datasette-apps/, June 18, 2026.
Vulnerability identified by Claude Fable 5 during security evaluation.*

### Three-Model Development Workflow (from the "Built with so much AI assistance" section)

```
Development of datasette-apps (June 2026):

Model               Role
-----------------   -----------------------------------------------
Claude Opus 4.6     Initial prototype (datasette-agent-artifacts),
(via Claude Code)   later datasette-agent-edit, then datasette-apps

GPT-5.5 /           Planning and transport architecture; suggested
Codex Desktop       MessageChannel() port over postMessage()

Claude Fable 5      Security evaluation; identified the
                    privilege-escalation-via-exfiltration attack

Human (Willison)    Design direction, mitigation decisions,
                    apps-set-csp permission design
```

*Source: Simon Willison, simonwillison.net/2026/Jun/18/datasette-apps/, June 18, 2026.*

## Cross-References

- **Corroborates**:
  - `blog-simonwillison-csrf-multimodel-review.md` Claim 2: "Multi-model cross-review
    — Claude Code for implementation, a second model for review — is a viable workflow
    for production security changes." This source extends the two-model pattern from
    that note (Claude Code for implementation + GPT-5.4 for review) to a three-model
    division of labor (Claude Opus 4.6 for implementation + GPT-5.5 for planning +
    Fable 5 for security audit). Both sources show Willison deliberately selecting
    different models for different roles, with an explicit security-review phase using
    a model different from the implementation model.
  - `blog-simonwillison-html-effectiveness.md` Claim 1: "Requesting HTML output from
    Claude enables richer presentation than Markdown — specifically SVG diagrams,
    interactive widgets, and in-page navigation." Datasette Apps are structurally the
    same artifact class as HTML output from Claude. Willison's "perfect shape to be
    written by a modern LLM" claim about Datasette Apps directly corroborates the
    broader pattern that self-contained HTML files are a natural LLM output format.
    The copyable-prompt feature in Datasette Apps is the explicit mechanism for
    exploiting this alignment.
  - `blog-simonwillison-rss-vibe-coded-apps.md` Claim 1: "Vibe-coding accelerates app
    development to the point where the release cadence becomes blog-post-like rather
    than product-launch-like." Datasette Apps are explicitly designed for this cadence:
    a user generates a self-contained HTML app from a prompt, pastes it into Datasette,
    and it is immediately hosted. The create-app form's copyable-prompt feature removes
    the friction between "I have a data question" and "I have a running app that answers
    it." This is the infrastructure realization of the blog-post-cadence app pattern.

- **Extends**:
  - `blog-simonwillison-datasette-1-0a34.md` Claim 3 (agent capability inversion
    pattern): "Agent write capability created an absurd capability inversion — the
    chat interface could modify data but the regular UI could not — which made the
    missing UI feature immediately visible." Datasette Apps is the next step in this
    progression: the agent conversation interface could generate self-contained apps,
    but there was no built-in way to host them. datasette-apps closes that gap. Both
    the CRUD UI (1.0a34) and the apps hosting (datasette-apps) were driven by agent
    capabilities revealing UI gaps.
  - `blog-simonwillison-datasette-agent-write-sql.md` Claim 1 (execute_write_sql
    requests user approval): The stored-query write restriction in Datasette Apps
    is the app-context counterpart to the approval gate in datasette-agent 0.3a0.
    Both restrict write operations: the agent uses human-in-the-loop approval at
    runtime; the apps plugin uses administrator-pre-configured stored query allow-lists
    at configuration time. Together they show two architecturally distinct approaches
    to the same problem (safe write access from an AI-facing interface): runtime
    human approval vs. compile-time capability restriction.
  - `blog-simonwillison-datasette-agent.md` overall: The platform announcement
    documented Datasette Agent as an extensible, plugin-based conversational SQL
    agent. datasette-apps is a separate plugin that extends the Datasette ecosystem
    in a different direction — from agent-driven queries to user-generated apps.
    The two plugins together show Datasette's extensibility model working as designed:
    independently-installable plugins each adding distinct AI-native capabilities
    without modifying the core tool.
  - `blog-simonwillison-fable-5-export-controls.md` Claim 3 ("Defenders need to be
    able to ask AI to fix the bugs in a file, explain why the fix matters, and write
    tests that confirm the patch works. That is not a guardrail bypass. It is the most
    valuable thing an AI model can do for defensive security"): Willison's use of
    Fable 5 for security evaluation of datasette-apps is a concrete practitioner
    instance of the defensive "find, fix, and test loop" that Moussouris describes.
    The vulnerability Fable 5 identified was a real, non-obvious attack that Willison
    then fixed — this is the pattern the export controls inadvertently targeted.

- **Contradicts**: None identified. No existing corpus note makes claims about sandbox
  isolation patterns for LLM-generated code, MessageChannel as a security transport,
  or the specific attack surface of CSP allow-lists in multi-privilege systems that
  conflict with this source's claims. No contradiction issue required.

- **Novel**:
  - **First corpus documentation of iframe sandbox + CSP as a defense-in-depth
    pattern for hosting LLM-generated code**: No prior source note describes this
    specific layered isolation architecture in the context of untrusted LLM-generated
    apps. Prior corpus notes on sandboxed code execution use MicroPython WASM
    (`blog-simonwillison-datasette-agent-micropython.md`) or Fly Sprites persistent
    sandboxes (`blog-simonwillison-datasette-agent.md` Claim 6) — this is the first
    iframe + CSP approach.
  - **First corpus documentation of MessageChannel() vs. postMessage() as a security
    choice in AI-native systems**: The specific rationale (channel teardown on frame
    navigation) as a security property, in the context of sandboxed app hosting, is
    not documented elsewhere in the corpus.
  - **Confused-deputy privilege escalation via CSP allow-listed exfiltration**: The
    specific attack pattern (less-privileged user creates app, tricks admin into
    visiting it, exfiltrates data via pre-approved CSP origin) is a novel threat
    model not documented in any prior source note. It generalizes to any system where
    (a) low-privilege users can create hosted content, (b) that content runs with the
    visitor's permissions, and (c) CSP allow-listing is user-configurable.
  - **apps-set-csp permission tier as a CSP delegation pattern**: Separating
    "configuring the CSP allow-list" from "selecting from the allow-list" via a
    dedicated permission class is a specific mitigation pattern not documented elsewhere.
  - **Copyable-prompt-with-schema as an LLM app generation UX pattern**: Including a
    ready-to-paste LLM prompt with full schema context in the create-app form is the
    first in-corpus documentation of a data tool explicitly providing LLM generation
    scaffolding as a built-in UI feature.
  - **Three-model design-implement-audit division of labor**: The explicit use of
    three specialized models (implementation, planning/architecture, security audit)
    extends the two-model pattern documented in `blog-simonwillison-csrf-multimodel-review.md`
    by adding a dedicated security evaluation phase with a model selected specifically
    for its evaluation depth.

## Guide Impact

- **Chapter 05 (Building with Agents — AI-generated code as first-class feature)**:
  Add Datasette Apps as the primary example of a data tool designed explicitly to
  host LLM-generated code. The key design decisions — single-file HTML format,
  narrow JavaScript API, copyable-prompt-with-schema — are architectural choices
  that match what LLMs produce well. Cite Claim 4 ("perfect shape to be written by
  a modern LLM") as the practitioner's own characterization of this alignment. The
  guide should discuss designing systems to *receive* LLM-generated code as a
  distinct concern from designing systems to *use* LLMs as agents.

- **Chapter 05 (Building with Agents — defense-in-depth for untrusted code)**:
  The four-layer isolation architecture (iframe sandbox + injected CSP + MessageChannel
  + stored-query restriction) is a concrete reference implementation for sandboxing
  LLM-generated code. Currently no guide section documents a worked example at this
  level of specificity. Cite Claim 1 for the sandbox + CSP layer, Claim 2 for
  MessageChannel, Claim 3 for stored-query restriction, and the Concrete Artifacts
  section for the full defense-in-depth stack. Pair with Claim 7 (the Fable 5 attack)
  to illustrate that correct individual layers can still produce emergent
  vulnerabilities at the system level.

- **Chapter 05 (Building with Agents — AI-assisted security evaluation)**:
  Add the Fable 5 security evaluation (Claims 7–8) as a worked example of using
  a frontier model for independent security review of a new system. Key points:
  (1) the vulnerability Fable 5 found was a non-obvious confused-deputy attack, not
  a simple bug; (2) the model found it in the context of a system whose individual
  components were each correctly designed; (3) the fix required a design change
  (new permission tier), not just a code fix. This is a stronger case for AI security
  review than "AI found a typo in the sanitization logic" — it shows AI evaluating
  emergent system-level risks. Cite Claim 7 for the attack and Claim 8 for the fix.

- **Chapter 03 (Patterns for AI-Native Systems — multi-model role specialization)**:
  Extend the multi-model workflow section with the three-model pattern documented in
  Claim 9. The guide currently documents two-model patterns (implementation + review).
  This source adds an explicit design-planning role (GPT-5.5 for architecture, which
  suggested MessageChannel), demonstrating that planning/design, implementation, and
  security audit can each benefit from different model characteristics. The guide
  should note that this is an emerging pattern — only anecdotally documented here —
  but one worth practitioners experimenting with for high-stakes systems.

- **Chapter 04 (AI-native tooling ecosystem — Datasette evolution arc)**:
  Update the Datasette evolution narrative (currently documented across multiple
  source notes) to include datasette-apps as the latest step. The arc now reads:
  read-only data tool → agent-readable SQL (Datasette Agent, May 2026) →
  agent-writable SQL (0.3a0, June 15) → CRUD UI (1.0a34, June 16) → user app
  hosting (datasette-apps, June 18). Each step was enabled by AI capability
  expansion and each was released within days of the prior step. This is a
  documented, verifiable case study of how AI agent development drives rapid
  scope expansion of an underlying data tool. Cite Claim 11 for the overall arc.

## Extraction Notes

- **Source reading depth**: All five named sections were read via multiple WebFetch
  passes with targeted prompts. The technical content (sandbox attribute, CSP string,
  MessageChannel quotes, vulnerability description, permission fix) was extracted
  across three independent fetch attempts with consistent results.
- **Quote confidence**: Verbatim quotes marked as such in this note were confirmed
  across at least two WebFetch fetch attempts returning consistent text. The Fable 5
  vulnerability description (Claim 7) was particularly stable across passes —
  identical text returned on both passes that asked about it. The `apps-set-csp`
  permission quote (Claim 8) was similarly consistent. The "mainly built using Claude
  Opus 4.6 in Claude Code" attribution (Claim 9) and the Fable 5 development section
  quotes were confirmed once; marked `emerging` accordingly.
- **Claim 10 quote**: The exact phrasing of Willison's editorial note linking Fable 5's
  security capability to the export controls could not be confirmed as perfectly
  verbatim — the WebFetch tool returned a summary rather than the precise wording.
  The claim is marked with "(no direct quote; see paraphrase in Our assessment)" per
  extraction policy.
- **Fragment URL**: The issue URL includes `#atom-everything` (Atom feed anchor).
  The `source_url` uses the canonical page URL without the fragment, consistent with
  prior Willison source notes in this corpus.
- **Predecessor prototype**: The post describes a development history starting with
  `datasette-agent-artifacts` (April), renamed to `datasette-agent-edit` (keeping
  only editing tools), with the app-hosting concept spun into the separate
  `datasette-apps` plugin. This development history is noted but not extracted as
  a separate claim — it is primarily relevant for understanding the plugin's scope.
- **Cross-references verified**:
  - `blog-simonwillison-csrf-multimodel-review.md` Claim 2 confirmed at lines
    70–92 of that note: "Multi-model cross-review — Claude Code for implementation,
    a second model for review — is a viable workflow for production security changes."
    Verified as document-order Claim 2 (second `### Claim:` heading).
  - `blog-simonwillison-datasette-1-0a34.md` Claim 3 confirmed at lines 43–55
    of that note: agent write capability inversion pattern. Verified as Claim 3
    (third `### Claim:` heading).
  - `blog-simonwillison-datasette-agent.md` overall confirmed at lines 1–372
    of that note: documents the Datasette Agent platform.
  - `blog-simonwillison-datasette-agent-write-sql.md` Claim 1 confirmed at lines
    43–57 of that note: "The new `execute_write_sql` tool requests user approval
    and then writes to a database." Verified as document-order Claim 1.
  - `blog-simonwillison-fable-5-export-controls.md` Claim 3 confirmed at lines
    91–109 of that note: Moussouris's "find, fix, and test loop" characterization.
    Verified as document-order Claim 3.
  - `blog-simonwillison-html-effectiveness.md` Claim 1 confirmed at lines 46–61
    of that note: "Requesting HTML output from Claude enables richer presentation."
    Verified as document-order Claim 1.
  - `blog-simonwillison-rss-vibe-coded-apps.md` Claim 1 confirmed at lines 45–63
    of that note: vibe-coding app cadence shift. Verified as document-order Claim 1.
- **No contradictions filed**: No existing corpus note makes claims that conflict
  with this source's documented security architecture, multi-model workflow, or
  Datasette evolution arc. The Fable 5 export controls reference connects to existing
  corpus notes that document the same event from different angles; there is no
  contradiction between this source's characterization (Fable 5's security evaluation
  capability was genuinely useful) and those notes (the same capability was restricted
  by export controls). No contradiction issue required.
