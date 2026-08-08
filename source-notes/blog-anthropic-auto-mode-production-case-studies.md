---
source_url: https://claude.com/blog/auto-mode-in-production
source_type: blog-post
title: "Running auto mode in production"
author: Molly Vorwerck (Anthropic)
date_published: 2026-08-07
date_extracted: 2026-08-08
last_checked: 2026-08-08
status: current
confidence_overall: emerging
issue: "#2568"
---

# Running auto mode in production

> Anthropic's practitioner-facing follow-up to its auto mode architecture post,
> profiling three named customers (Nuro, Gusto, Garner Health) who have moved
> auto mode into daily production use — with concrete guardrail patterns
> (skills-based deny-lists, MCP proxy governance, communication-channel
> carve-outs) layered on top of the classifier described in
> `blog-anthropic-claude-code-auto-mode.md`.

## Source Context

- **Type**: blog-post (Anthropic/Claude official blog, first-party but built
  entirely from customer testimonials rather than internal engineering data)
- **Author credibility**: Byline is Molly Vorwerck, published on Anthropic's
  official Claude blog. The claims about *classifier design* are Anthropic's
  own (and are the settled subject of `blog-anthropic-claude-code-auto-mode.md`);
  the claims about *how customers use and govern* auto mode are attributed to
  named individuals at named companies (Kai Zhou at Nuro; Martin Emde and Chad
  Kunsman at Gusto; Evan Magnussen at Garner Health), which is stronger sourcing
  than an anonymous case study but is still vendor-selected and vendor-published
  — these are success stories chosen by Anthropic's marketing/blog team, not an
  independent survey of auto mode adoption.
- **Scope**: Covers three case studies of auto mode in production (autonomous
  driving R&D, SMB SaaS, healthcare SaaS) with usage stats, quoted guardrail
  practices, and one aggregate metric ("9x longer between interruptions").
  Does NOT cover: failure cases, companies that tried auto mode and reverted,
  cost/latency data, or any of the classifier internals (those live in the
  companion architecture post). No adoption timeline, control-group comparison,
  or methodology is given for the "9x" and "caught more dangerous actions than
  developers" claims.

## Extracted Claims

### Claim 1: The auto mode classifier caught more dangerous actions in aggregate than developers did when manually clicking through permission prompts
- **Evidence**: Asserted directly by the article as a summary framing claim, not attributed to a specific company or accompanied by a dataset, methodology, or comparison metric in this post.
- **Confidence**: anecdotal (unsupported assertion; contrast with the quantified 17% FNR figure in the companion architecture post, which shows the classifier still misses roughly 1 in 6 real overeager actions)
- **Quote**: "the classifier caught more dangerous actions than developers did when clicking through permission prompts by hand"
- **Our assessment**: This is the article's headline safety claim but it is not backed by the kind of dataset the March 2026 architecture post provided (10,000 real-traffic calls, 52 real overeager-action incidents). Read literally it is plausible — `blog-anthropic-claude-code-auto-mode.md` Claim 1 already established a 93% blanket-approval rate in manual mode, meaning manual review was already close to theater — but this post gives no number for the comparison, so it should be cited as a directional/qualitative claim, not a quantified result.

### Claim 2: Claude works roughly 9x longer between human interruptions under auto mode than under the previous default permission model
- **Evidence**: Aggregate usage-pattern statistic stated by the article, not attributed to a single company; no cohort size, time window, or measurement methodology disclosed in the post.
- **Confidence**: emerging
- **Quote**: "Claude works 9x longer between interruptions than under the previous default"
- **Our assessment**: This is the single most citable production metric in the post and is consistent with the qualitative case studies (Nuro's 7-hour unattended run; Gusto's "uninterrupted cross-repo work"). Treat as a real but coarse aggregate — it's a company-wide usage-telemetry number from Anthropic, not derived from the three named customers, and no baseline session-length figure is given, so "9x" cannot be converted into an absolute duration.

### Claim 3: Nuro uses auto mode for 100% of its coding work, including autonomous overnight research agents that run for hours unattended
- **Evidence**: Direct quote and a specific anecdote from Kai Zhou (staff software engineer, Nuro): an agent kicked off at 10 p.m. that ran until 5 a.m. and produced three pull requests by morning.
- **Confidence**: anecdotal (single named engineer, single anecdote, one company)
- **Quote**: "I don't want to sit there and click approve all the time. I use auto mode for 100 percent of my coding work." / "The other day, I kicked off an agent at 10 p.m. and it kept running until 5 a.m.—and it gave me three PRs in the morning."
- **Our assessment**: This is a concrete, verifiable-shape example (autonomous driving R&D, where evaluation metrics against recorded/simulated driving data give the agent a clear, checkable success signal) of the "clear measurement signal enables autonomous iteration" pattern. It's a strong illustration but a sample size of one engineer's one anecdote — the guide should present it as an existence proof (long unattended runs are possible when the domain has an automatic evaluation signal), not as a typical outcome.

### Claim 4: Nuro layers skills-based deny-lists under auto mode, explicitly blocking the most dangerous commands (e.g. recursive deletes) outright rather than relying on the classifier alone
- **Evidence**: Article description of Nuro's configuration.
- **Confidence**: emerging
- **Quote**: "engineers deny the most dangerous commands, like recursive deletes, outright in their settings."
- **Our assessment**: This corroborates the "auto mode is the second layer of defense, not the first" framing that recurs across all three case studies (see Claim 6, Claim 9) and matches the guardrail-stacking pattern already documented in `blog-anthropic-claude-code-auto-mode.md` Claim 4 (block-rule customization) — but here the practitioner adds a static settings-level deny-list *in addition to* the classifier, rather than relying on the classifier's own block-rule slot. This is a concrete, reusable pattern: don't trust the classifier as the sole safety net for irreversible commands.

### Claim 5: Nuro reverts to interactive/manual mode specifically for cross-team pull requests, keeping a human review step for work visible to other teams
- **Evidence**: Article description of Kai Zhou's workflow when Claude Code opens PRs on his behalf for cross-team work.
- **Confidence**: anecdotal
- **Quote**: "when Claude Code reviews a Pull Request on his behalf, Kai switches back to interactive mode and reviews each one before it goes out."
- **Our assessment**: This is a specific, actionable carve-out rule: scope auto mode to the actor's own blast radius, and drop back to manual review at the boundary where output becomes visible/consequential to people outside the immediate task (a colleague's PR, another team's queue). This is a narrower, more specific version of the "review bypass / affect others" block-rule category already named in the architecture post's default taxonomy, applied here as a manual policy rather than a classifier rule.

### Claim 6: Gusto has run auto mode across 2,425 Claude Code sessions since December, with roughly 10% of session transcripts (since mid-May 2026) including an auto mode denial
- **Evidence**: Specific usage counts attributed to Martin Emde at Gusto.
- **Confidence**: emerging (specific counts from a named practitioner at a named company, but single-company, undisclosed measurement window boundaries for the session count vs. the denial-rate window)
- **Quote**: "kicked off 2,425 Claude Code sessions since December" / "roughly 10% of session transcripts since mid-May 2026 included an auto mode denial"
- **Our assessment**: This is the most concrete adoption-scale + friction-rate data point in the post. Note the two stats use different windows (session count "since December," denial rate "since mid-May 2026") — they are not directly comparable as a single ratio. A ~10% denial rate is a meaningful data point for what "normal" classifier friction looks like in a real SMB SaaS engineering org, useful as a benchmark for teams evaluating whether their own denial rate is unusually high or low.

### Claim 7: Gusto's Martin Emde reports auto mode improved the speed/safety balance by removing repeated permission prompts without compromising safety
- **Evidence**: Direct quote from Martin Emde, Gusto.
- **Confidence**: anecdotal
- **Quote**: "Auto mode gave us a safer balance between speed and control. We were able to remove the repeated prompts and increase productivity without compromising safety."
- **Our assessment**: This is a subjective practitioner endorsement rather than a measured outcome — "without compromising safety" is an assertion, not something the post measures. Useful as a sentiment data point corroborating Claim 1 of `blog-anthropic-claude-code-auto-mode.md` (93% blanket-approval rate implies prompts weren't adding real safety), but should not be cited in the guide as evidence that safety outcomes were actually held constant.

### Claim 8: Gusto's Chad Kunsman considers auto mode a better default than `--dangerously-skip-permissions` specifically because of its prompt-injection protection and intent-alignment checking, and faster than manual permission prompts
- **Evidence**: Direct quote from Chad Kunsman, Gusto.
- **Confidence**: anecdotal
- **Quote**: "Given the protection against prompt injection, and the way it checks that what you're doing actually lines up with what you asked for, it's the better choice than bypass permissions and far faster than permission prompts."
- **Our assessment**: This is a practitioner explicitly framing auto mode as strictly dominant over the bypass-permissions flag along two axes (injection protection, speed) — directly useful for the guide's decision framework of "auto mode vs. `--dangerously-skip-permissions` vs. manual prompts." It corroborates the architecture post's positioning (Claim 10 of `blog-anthropic-claude-code-auto-mode.md`: "targeting users who would otherwise use the permissionless flag") from the customer side of that same tradeoff.

### Claim 9: Gusto still requires manual, per-tool-call verification when a session touches production infrastructure (Terraform, AWS, direct POST calls against live APIs)
- **Evidence**: Article description of Chad Kunsman's workflow.
- **Confidence**: emerging
- **Quote**: "When a session has its teeth into production infrastructure—Terraform, AWS, direct POST calls against live APIs—he switches to accept edits and verifies each tool call by hand."
- **Our assessment**: This is a direct practitioner-side confirmation of Claim 10 in `blog-anthropic-claude-code-auto-mode.md` ("not a drop-in replacement for careful human review on high-stakes infrastructure") — a real engineer independently drew the same line (production infra = manual review) that Anthropic's own scope caveat predicts. This convergence between vendor caveat and practitioner behavior strengthens confidence that the line is a real, load-bearing distinction rather than defensive marketing language.

### Claim 10: Gusto routes MCP traffic through a governed proxy layer with tool guards and prompt inspection, scoping agent permissions before auto mode's classifier is ever consulted
- **Evidence**: Article description of Gusto's infrastructure.
- **Confidence**: emerging
- **Quote**: "Gusto routes its MCP traffic through a governed proxy layer with tool guards and prompt inspection, so agents work with tightly scoped permissions before auto mode ever weighs in."
- **Our assessment**: This is a concrete, reusable enterprise architecture pattern not present in the companion architecture post: an MCP-layer proxy that pre-scopes what tools/servers are reachable at all, independent of and prior to the transcript classifier. It's the production analog of the enterprise MCP allowlist/denylist mechanism described in `docs-github-copilot-mcp-allowlists-enterprise.md` (GitHub Copilot's `allowedMcpServers`/`deniedMcpServers`), but implemented as Gusto's own governed proxy rather than a platform-native managed-settings feature — evidence that practitioners are building this control themselves where the platform doesn't yet provide it natively for Claude Code.

### Claim 11: Garner Health rolled out Claude Code to all 550 employees across every function in February 2026, built around auto mode
- **Evidence**: Article statement, attributed to Evan Magnussen (platform engineering manager, Garner Health).
- **Confidence**: emerging
- **Quote**: "rolled out Claude Code in February to all 550 employees across every function"
- **Our assessment**: The largest concrete rollout-scale figure in the post (550 employees, all-function, not just engineering) and one of the largest single-company adoption figures encountered in the corpus. "Across every function" implies non-engineering staff use it too, which the post doesn't further detail (what do non-engineers use it for?) — a gap for the guide to flag rather than assume.

### Claim 12: Garner Health built a standardized software development lifecycle around auto mode, including an "antagonistic research" phase that pressure-tests assumptions before implementation, which the company says was only possible because of auto mode
- **Evidence**: Direct quote from Evan Magnussen, Garner Health; the article does not further define "antagonistic research" beyond naming it.
- **Confidence**: anecdotal (single practitioner, term not independently defined or demonstrated with an example in this source)
- **Quote**: "We've built out a standardized software development lifecycle for the entire engineering organization that is really only possible because of auto mode."
- **Our assessment**: The causal claim ("only possible because of auto mode") is strong and unverified — the article gives no counterfactual (what stopped them from standardizing the SDLC before auto mode existed?). The "antagonistic research" term is evocative but underspecified in this source; if the guide wants to cite this pattern (agents pressure-testing their own/each other's assumptions before implementation), it should flag that this source only names it, it doesn't show it.

### Claim 13: Garner Health explicitly configured auto mode to withhold approval for actions that communicate with other people (Slack messages, emails), keeping a human in the loop for interpersonal/external-representation decisions
- **Evidence**: Article description plus direct quote from Evan Magnussen.
- **Confidence**: emerging
- **Quote**: "he configured auto mode not to approve actions that communicate with other people, like sending Slack messages or emails" / "I personally don't like Claude to just act on my behalf when I'm communicating with another person."
- **Our assessment**: This is the clearest, most guide-actionable carve-out rule in the post: classify "external representation" (anything that speaks as-you to another human) as its own risk category, separate from data destruction or security degradation, and keep it manual regardless of how well the classifier performs elsewhere. This is a category the four-category block-rule taxonomy in `blog-anthropic-claude-code-auto-mode.md` (destroy/exfiltrate, degrade security, cross trust boundaries, bypass review) does not explicitly name — interpersonal/communication actions don't map cleanly onto any of those four, which is a gap worth flagging in Guide Impact below.

## Concrete Artifacts

```
Production auto mode case studies
(Claude blog, "Running auto mode in production," Molly Vorwerck, 2026-08-07)

Nuro (autonomous driving R&D) — Kai Zhou, staff software engineer
  - Auto mode used for 100% of coding work
  - Overnight autonomous run: 10 p.m. -> 5 a.m. (~7 hrs), produced 3 PRs
  - Guardrail: settings-level deny-list for dangerous commands (e.g. recursive delete)
  - Carve-out: reverts to interactive mode to review cross-team PRs before they go out

Gusto (SMB SaaS) — Martin Emde; Chad Kunsman
  - 2,425 Claude Code sessions since December
  - ~10% of session transcripts (since mid-May 2026) included an auto mode denial
  - Guardrail: MCP traffic routed through a governed proxy layer (tool guards +
    prompt inspection) scoping permissions before auto mode's classifier runs
  - Carve-out: manual "accept edits" + hand-verification for production
    infrastructure (Terraform, AWS, direct POST calls to live APIs)

Garner Health (healthcare SaaS) — Evan Magnussen, platform engineering manager
  - Rolled out Claude Code to all 550 employees, every function, February 2026
  - Standardized SDLC built around auto mode, including an "antagonistic
    research" pressure-testing phase
  - Carve-out: auto-approval disabled for actions that communicate with other
    people (Slack messages, emails) — kept manual

Aggregate stats (not attributed to a single company):
  - "the classifier caught more dangerous actions than developers did when
     clicking through permission prompts by hand"
  - "Claude works 9x longer between interruptions than under the previous default"
```

## Cross-References

- **Extends**: `blog-anthropic-claude-code-auto-mode.md` — that note documents
  the classifier architecture (two-stage pipeline, three-tier permissions,
  four-category block-rule taxonomy, 17% FNR on real overeager actions,
  93% blanket-approval-rate motivation, and the explicit "not a drop-in
  replacement for careful human review on high-stakes infrastructure" scope
  caveat) this post builds on. This note supplies the missing practitioner
  half: how real teams configure, layer, and carve exceptions around that
  classifier in production. Claim 9 here is a direct practitioner-side
  confirmation of that note's Claim 10; Claim 8 here corroborates that note's
  Claim 10 from the customer's own comparison of auto mode vs. the
  `--dangerously-skip-permissions` flag.
- **Corroborates**: `docs-github-copilot-mcp-allowlists-enterprise.md` — Claim
  10 here (Gusto's governed MCP proxy layer, built by the practitioner
  themselves) is the practitioner-driven analog of the platform-native
  `allowedMcpServers`/`deniedMcpServers` enterprise control that GitHub shipped
  for Copilot in the same week (2026-08-06). Both sources independently
  converge on "gate which MCP servers/traffic an agent can reach, before any
  downstream permission/classifier logic runs" as a necessary enterprise
  control — one as a vendor-shipped feature, one as a customer-built proxy.
- **Novel**:
  - The three named-customer case studies (Nuro, Gusto, Garner Health) with
    specific usage counts (2,425 sessions, 550-employee rollout, 10% denial
    rate, 7-hour unattended run / 3 PRs) are new to the corpus — no other
    source has practitioner-attributed production metrics for auto mode.
  - The "communicate with other people" carve-out (Claim 13, Garner Health) is
    a new risk category not covered by the four-category block-rule taxonomy
    in the companion architecture post.
  - The settings-level deny-list stacked underneath the classifier (Claim 4,
    Nuro) and the cross-team-PR interactive-mode carve-out (Claim 5, Nuro) are
    new concrete guardrail patterns not documented elsewhere in the corpus.
  - The MCP governed-proxy pattern (Claim 10, Gusto) is a new enterprise
    architecture pattern for Claude Code specifically (distinct from, though
    parallel to, GitHub's platform-native MCP allowlist feature).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add a "layered guardrails in
  production" subsection alongside the existing classifier-architecture
  material (from `blog-anthropic-claude-code-auto-mode.md`): (1) settings-level
  deny-lists for irreversible commands as a belt-and-suspenders layer under the
  classifier (Claim 4), (2) an MCP-layer proxy/allowlist that scopes reachable
  tools *before* the classifier runs (Claim 10), and (3) a distinct
  "communicates on your behalf with other people" risk category (Slack, email)
  that should default to manual regardless of classifier confidence (Claim 13)
  — flag that this category isn't covered by the four block-rule categories in
  the architecture post, so teams need to add it themselves.
- **Chapter 01 (Daily Workflows)**: Cite the Nuro overnight-agent example
  (Claim 3) as a concrete illustration of "clear evaluation signal enables
  autonomous overnight iteration," with the caveat that it's a single anecdote
  from a domain (autonomous driving) with an unusually clean automated success
  metric — not a generalizable claim that unattended overnight runs work well
  in domains without such a signal.
- **Chapter 05 (Team Adoption)**: Use Gusto's 2,425-session / ~10%-denial-rate
  figures (Claim 6) as a reference point for what "normal" auto mode friction
  looks like at SMB scale, and Garner Health's 550-employee, all-function
  rollout (Claim 11) as an enterprise-scale reference point. Note the gap: the
  source doesn't explain what non-engineering staff at Garner Health actually
  use Claude Code for, so don't extrapolate specifics from that number.
- **Chapter 03 (Safety and Verification)**: When citing the headline claim
  that "the classifier caught more dangerous actions than developers did"
  (Claim 1) or the "9x longer between interruptions" stat (Claim 2), flag both
  as unquantified/methodology-free aggregate claims from this source — pair
  them with the quantified 17% FNR figure from `blog-anthropic-claude-code-auto-mode.md`
  so the guide doesn't overstate auto mode's safety record using this post
  alone.

## Extraction Notes

- Full verbatim reproduction of the article was not obtainable via automated
  fetch (copyright-guarded); all quotes above were independently confirmed via
  targeted verbatim-quote extraction (each under the tool's ~125-character
  quoting limit) rather than a single full-page scrape, and cross-checked
  across two separate fetch passes for consistency.
- No linked sub-pages were found to follow — the article is a single case-study
  page with no substantive internal links to follow per MINER.md §1.
- The "antagonistic research" concept (Claim 12) is under-specified in the
  source itself, not just in this extraction — the article names it but never
  defines or demonstrates it. Flagged explicitly in that claim's assessment
  rather than inferred or filled in.
- `confidence_overall` is set to "emerging" rather than "settled": the
  classifier architecture claims it references are settled (established in
  the companion note), but this post's own contribution — the production case
  studies — rests on a handful of quotes from three vendor-selected customers
  with no independent verification, disclosed methodology, or control group.
- No contradictions with existing source notes were found during
  cross-referencing (per MINER.md §4/§4a); this post is consistently
  corroborating/extending relative to the existing auto mode note.
