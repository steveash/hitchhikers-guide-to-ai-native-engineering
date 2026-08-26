---
source_url: https://newsletter.pragmaticengineer.com/p/why-ramp-built-inspect
source_type: blog-post
title: "Why Ramp built its own in-house coding agent, Inspect"
author: Gergely Orosz, Jessica Salmon, and Ivan Klaric (The Pragmatic Engineer newsletter)
date_published: 2026-08-25
date_extracted: 2026-08-26
last_checked: 2026-08-26
status: current
confidence_overall: emerging
issue: "#2968"
---

# Why Ramp built its own in-house coding agent, Inspect

> Fintech Ramp built and dogfooded an in-house, remote-sandboxed, model-agnostic
> coding agent (Inspect) that now produces the large majority of the company's
> merged PRs; the reported reasons for building rather than buying center on
> concurrency limits of local third-party tools, a need for centrally-configured
> remote dev environments, and being able to out-build third-party verification
> features (e.g. screenshot verification) by roughly a year.

## Source Context

- **Type**: blog-post (The Pragmatic Engineer newsletter/Substack, byline
  "Gergely Orosz, Jessica Salmon, and Ivan Klaric," published 2026-08-25)
- **Author credibility**: Gergely Orosz is a well-established, high-signal
  engineering-org reporter (this corpus already carries nine other
  `blog-pragmaticengineer-orosz-*` notes and a broader
  `survey-pragmaticengineer-ai-tooling-2026.md`). The piece names specific
  Ramp employees as sources (CTO Rahul Sengottuvelu, Head of Engineering
  Hamid Dadkhah, Principal/founding engineer Zach Bruggeman) rather than
  relying on anonymous or unattributed claims, which is consistent with this
  outlet's usual sourcing style.
- **Scope**: **This note covers only the freely-visible preview of the
  article.** The piece is paywalled; the visible portion covers "What is
  Inspect?", "Rapid adoption when background agent released," "Why build
  your own background coding agent?," "How Ramp uses Inspect," and the
  opening of "Architecture and tech stack" before cutting off after the
  sentence introducing "the _same_ context and tools" principle. Sections
  behind the paywall (the remainder of the architecture discussion and any
  further sections) were **not** read and are not represented here. See
  Extraction Notes.

## Extracted Claims

### Claim 1: The article frames Ramp as one of a small group of companies where most code is written by a custom-built, internal AI coding agent rather than a third-party tool
- **Evidence**: Opening framing sentence of the piece.
- **Confidence**: emerging (stated as the article's own framing, not an independently sourced industry survey)
- **Quote**: "At a select few tech companies, they write most of their code with their own, custom-built, internal AI coding agents."
- **Our assessment**: This is the article's thesis statement rather than a measured claim — it asserts Ramp is part of a small cohort without naming the other companies in the preview portion. Worth treating as framing/context rather than as independent evidence on its own; the specific Ramp metrics below (Claims 2-4) are the load-bearing evidence.

### Claim 2: 75% of all merged PRs at Ramp come from Inspect sessions, up from 60% two months after the v2 launch
- **Evidence**: Adoption metrics attributed to the "Rapid adoption when background agent released" section, given as a progression: 60% by January 2026 (about two months post-v2 launch), rising to 75% by May 2026.
- **Confidence**: emerging (specific, dated company-reported figures; no independent audit or methodology disclosed in the visible preview)
- **Quote**: "75% of all merged PRs come from Inspect sessions"
- **Our assessment**: A concrete, dated adoption curve (60% → 75% over roughly four months) is more specific than a single snapshot figure, which makes it more useful evidence than most self-reported adoption claims — but it is still self-reported by Ramp with no stated measurement methodology (e.g., how "from Inspect sessions" is attributed for a PR with mixed human/agent edits).

### Claim 3: Inspect itself is largely built using Inspect — roughly 90% of PRs merged into the Inspect repository come from Inspect sessions, and over 80% of Inspect's own codebase was written in Inspect sessions, with 150+ engineers having contributed to it
- **Evidence**: Dogfooding statistics attributed to the "How Ramp uses Inspect" section.
- **Confidence**: emerging (specific, quantified dogfooding claim; self-reported, no external verification)
- **Quote**: (no direct quote; see paraphrase above — the specific ~90%/80%+/150+ figures were confirmed via a fetch summary rather than a verbatim excerpt of the underlying sentence)
- **Our assessment**: Dogfooding-your-own-tool-to-build-itself is a strong internal-trust signal if accurate, and having 150+ distinct contributing engineers (not just the 5.5-person core team) suggests broad internal adoption rather than a single team's pet project. Because this note could not verify the exact source sentence verbatim (only a paraphrased fetch summary was available before the paywall), treat the precise percentages as indicative rather than exact until the full article can be read.

### Claim 4: Ramp reports reaching 1 million total Inspect sessions as of July 2026, and more than 200 internally-built agents now run on top of the Inspect platform
- **Evidence**: Scale/milestone figures attributed to the "How Ramp uses Inspect" section.
- **Confidence**: emerging (specific, dated milestone figures; self-reported)
- **Quote**: "Engineers at Ramp have built more than 200 agents running on top of the Inspect platform"
- **Our assessment**: The 200+-agents figure is the most concrete evidence in the preview that Inspect functions as an internal *platform* (with its own ecosystem of derivative agents), not just a single coding-agent product — this distinguishes Ramp's framing from a simple "we built a Claude Code alternative" story and is worth citing separately from the raw session-count/PR-share metrics.

### Claim 5: Ramp's stated reasons for building rather than buying include that local third-party tools were limited to one or two concurrent sessions, that designers needed better frontend tooling to make UI tweaks without engineer involvement, and that scaling required remote environments for debugging cross-service issues like backward-compatibility and broken API contracts
- **Evidence**: Reasons attributed to the "Why build your own background coding agent?" section.
- **Confidence**: emerging (specific, named rationale attributed to Ramp engineering leadership; not independently benchmarked against what third-party tools actually supported at the time)
- **Quote**: "Engineers already knew how to go to a file and edit a single line of code, so didn't have a reason to use it"
- **Our assessment**: The concurrency-limit reason is the most externally checkable and most corroborated claim in this set (see Cross-References — it matches independent practitioner reports of local parallel-session ceilings). The designer-tooling and cross-service-debugging reasons are more Ramp-specific and harder to verify independently from the preview alone.

### Claim 6: Inspect spins up a fully provisioned, sandboxed remote development environment in under 5 seconds, run by a core team of 5.5 people (four engineers, a director, and a part-time PM)
- **Evidence**: Team-size and provisioning-speed figures attributed to the "Why build" section.
- **Confidence**: emerging (specific, self-reported figures)
- **Quote**: "Under 5 seconds to spin up environments"
- **Our assessment**: A 5.5-person team supporting a platform used by 150+ contributing engineers and producing 75% of merged PRs is a striking leverage ratio if the adoption figures (Claim 2) hold — this is the kind of "small platform team, broad org-wide leverage" pattern that is directly relevant to any guide discussion of how much staffing an in-house coding-agent platform actually requires, in contrast with the multi-team, multi-year investment Cognition reports for its own cloud-agent infrastructure (see Cross-References).

### Claim 7: Ramp reports it built screenshot-based verification for agent-made UI changes roughly a year before this capability was available from third-party coding-agent vendors
- **Evidence**: Competitive-timing claim attributed to the "Why build" section.
- **Confidence**: anecdotal (a single, self-reported timing claim with no named comparison vendor or date given in the visible preview)
- **Quote**: "Almost a year ago, Ramp built screenshot verification before it was supported by third-party vendors"
- **Our assessment**: This is the article's clearest "build gave us a durable lead" claim, but it names no specific competing vendor or product, so it cannot be independently checked from the preview. Treat as Ramp's own competitive narrative rather than a verified timeline until a named comparison point is available.

### Claim 8: Inspect verifies its own changes rather than simply proposing them, and Ramp frames the agent's constraint as model intelligence rather than missing tools or access
- **Evidence**: Capability framing attributed to the "What is Inspect?" section.
- **Confidence**: emerging (a stated design philosophy; not independently benchmarked)
- **Quote**: "The only constraint on agents' ability is model intelligence, not missing tools or access"
- **Our assessment**: This is a notable inversion of the more common "the harness/tooling is the bottleneck, not the model" framing found elsewhere in this corpus (see Cross-References) — Ramp's claim is that once you've solved tool/environment access comprehensively (which is exactly what building Inspect's remote-sandbox platform did), the remaining gap actually is model capability. This is worth flagging as a distinct position on the tooling-vs-model-intelligence question, conditioned on already having invested heavily in the tooling side.

### Claim 9: Inspect's harness is OpenCode — a model-agnostic, open-source coding-agent harness exposing an HTTP API — chosen partly because that API made it straightforward to build a remote-environment product around it, created by Dax Raad
- **Evidence**: Architecture detail from the start of the "Architecture and tech stack" section (pre-paywall).
- **Confidence**: emerging (specific, named technical choice; visible only in the pre-paywall portion, so full architectural rationale is not available to this note)
- **Quote**: "They were also encouraged by seeing that OpenCode exposed an HTTP API which made it straightforward to set up"
- **Our assessment**: Building on an open-source, model-agnostic harness (OpenCode) rather than a single vendor's proprietary agent is a specific, checkable architectural decision — it decouples Ramp's internal platform from any one frontier lab's release cadence or API changes, which is a distinct build-vs-buy tradeoff from either "use a vendor's managed agent" or "build a fully custom harness from scratch."

### Claim 10: The pre-paywall architecture description names a stack of React/Vite frontend, Cloudflare Durable Objects + SQLite + Cloudflare Agents SDK for backend state, and Modal for sandboxing, with each remote sandbox containing OpenCode plus development services (Postgres, Redis, RabbitMQ, Temporal), Chromium, and a VS Code Server
- **Evidence**: Architecture/tech-stack detail from the pre-paywall portion of the "Architecture and tech stack" section.
- **Confidence**: emerging (specific, named technology choices; this is the section that is cut off by the paywall, so it may be incomplete relative to the full article)
- **Quote**: (no direct quote; see paraphrase above — this list of named technologies was confirmed via a fetch summary of the pre-paywall architecture section, not copied from a single verbatim source sentence)
- **Our assessment**: The specific combination — Cloudflare's stateful edge primitives (Durable Objects, Agents SDK) for orchestration/session-state, paired with Modal for the actual sandboxed compute — matches a pattern independently corroborated elsewhere in this corpus: Modal's own CTO names Ramp by name as a customer running "their external-facing accounting agent" on Modal specifically because it needed fine-grained control over file persistence, snapshotting, and networking beyond what a managed-agent product offers (see Cross-References). That independent, third-party confirmation of "Ramp uses Modal" gives this claim more weight than a single self-reported architecture diagram would carry alone.

## Concrete Artifacts

```
Source: newsletter.pragmaticengineer.com/p/why-ramp-built-inspect (free preview only)

Named people:
- Rahul Sengottuvelu — CTO, Ramp
- Hamid Dadkhah — Head of Engineering, Ramp
- Zach Bruggeman — Principal Engineer, founding engineer of Inspect
- Jason Quense — frontend engineer (v1 team)
- Dax Raad — creator of OpenCode (the harness Inspect is built on)

Dated milestones (as reported):
- November 2025 — Inspect v2 release
- ~1 year before Aug 2026 — v1 Chrome extension launch; screenshot
  verification built ("almost a year ago")
- January 2026 (~2 months post-v2) — 60% of merged PRs from Inspect
- May 2026 — 75% of merged PRs from Inspect
- July 2026 — 1 million total Inspect sessions milestone

Tech stack (pre-paywall section only):
- Frontend: React / Vite
- Backend/orchestration: Cloudflare Durable Objects, SQLite, Cloudflare
  Agents SDK
- Sandbox compute: Modal
- Harness: OpenCode (open-source, model-agnostic, HTTP API)
- Sandbox contents: OpenCode, Postgres, Redis, RabbitMQ, Temporal,
  Chromium, VS Code Server
- Environment spin-up time: under 5 seconds
```

## Cross-References

- **Corroborates**: `failure-sukit-parallel-session-ceiling.md` — that note's
  practitioner account documents a hard, independently-reported ceiling on
  how many coding-agent sessions can be run locally/interactively at once
  (2-3 sessions without worktree isolation). This source's Claim 5 gives a
  vendor/organizational-scale version of the same underlying constraint:
  Ramp reports that local third-party tools were "limited to running only
  1-2 sessions locally" as one of its stated reasons for building a
  remote-sandbox platform instead. The two sources describe the same
  concurrency ceiling from opposite vantage points — one individual
  practitioner hitting it, one company engineering around it at platform
  scale.

- **Extends**: `blog-latentspace-modal-agent-experience.md` Claim 16 — that
  note (an interview with Modal's CTO) independently names Ramp as a Modal
  customer, stating "Ramp also runs their accounting agent on us, so their
  external-facing agent," specifically because production-grade agents need
  "a lot more control over your compute primitive" (file persistence,
  snapshotting, networking) than a managed-agent product provides. This
  source's Claim 10 (Modal as the sandbox layer in Inspect's architecture)
  is independently corroborated by a source published from the opposite
  side of that vendor relationship, which increases confidence in the
  architecture claim beyond what either single source would support alone.

- **Extends**: `blog-cognition-what-we-learned-building-cloud-agents.md`
  Claims 3 and 8 — Cognition reports its own microVM isolation layer took
  "over a year of hypervisor engineering" and its orchestration layer took
  "over three quarters of dedicated engineering" with a dedicated team per
  infrastructure layer, i.e., building cloud-agent infrastructure from
  scratch is a multi-year, multi-team undertaking. This source's Claim 6 (a
  5.5-person Inspect team) is not a contradiction of that claim but a
  different point on the same build-effort spectrum: Ramp did not build its
  own isolation/orchestration layer from scratch — it composed existing
  providers (Cloudflare, Modal) and an open-source harness (OpenCode), per
  Claims 9-10, rather than building hypervisor-level isolation itself the
  way Cognition did as an infrastructure *vendor*. This is a conditioning
  variable (what layer of the stack you build vs. buy), not a genuine
  disagreement, so no contradiction issue was filed per MINER.md §4a.

- **Extends**: `blog-cursor-self-hosted-cloud-agents.md` Claim 4 (per-session
  VM isolation enabling safe parallelization for Cursor's self-hosted cloud
  agents) — this source's Claim 6 (Inspect's sandboxed remote environments
  "unlocking unlimited session concurrency") describes the same underlying
  problem (local/shared-resource contention limits agent concurrency) being
  solved via remote per-session sandboxing, corroborating that this is a
  convergent architectural pattern across at least three independent
  organizations (Cursor as a vendor, Cognition as a vendor, Ramp as an
  end-user company building its own equivalent in-house).

- **Novel**: The explicit "model intelligence, not missing tools or access,
  is the constraint" framing (Claim 8) is a distinct position not previously
  captured in this corpus in this form — most existing harness/tooling
  sources argue the opposite emphasis (that tooling and environment access
  are the bottleneck, not the model). Also novel: the specific dogfooding
  ratio (an internal platform team of 5.5 people whose product is used to
  write 80%+ of its own codebase, with 150+ distinct internal contributors)
  as a concrete "small platform team, broad leverage" data point for an
  in-house coding-agent platform; and OpenCode (Dax Raad's project) as the
  specific named open-source harness choice underlying a large, production
  in-house agent platform, which is new to this corpus's coverage of
  OpenCode.

## Guide Impact

- **Chapter 03 (Decision-making about tools) / Ch04 (Org practices)**: Add
  Claim 5 (concurrency limits, designer-tooling needs, cross-service
  debugging) as a concrete, named set of build-vs-buy triggers for when an
  organization might build a custom coding-agent platform instead of using a
  third-party or managed-agent offering — currently the guide's build-vs-buy
  material (via the Cognition and Modal notes) skews toward "building cloud
  agent infrastructure from scratch is very expensive"; this source adds a
  contrasting, lower-cost path (compose existing sandbox/orchestration
  providers plus an open-source harness) that reached large-scale internal
  adoption with a 5.5-person team. Recommend the guide distinguish "building
  the full infrastructure stack" (Cognition's story) from "building the
  harness/product layer on top of composed infrastructure providers"
  (Ramp's story) as two very different build-effort tiers.
- **Chapter 05 (Team adoption)**: Add Claim 2's dated adoption curve
  (60% → 75% of merged PRs over ~4 months) and Claim 3's dogfooding
  statistics as a concrete case study of what rapid, org-wide internal
  agent adoption looks like when the platform team actively dogfoods its
  own product. Caveat clearly that these are self-reported, unaudited
  figures per this note's confidence rating.
- **Note for future mining**: If a paid-subscriber account or archived
  full-text version of this article becomes available, re-mine it — the
  paywall cuts off partway through "Architecture and tech stack," and later
  sections (implied by the section list but not visible) may contain
  additional architectural detail, named competitor comparisons for the
  screenshot-verification timing claim (Claim 7), and further named
  companies referenced in the opening framing (Claim 1).

## Extraction Notes

- **This source is paywalled beyond a specific point**, and this note
  reflects only the freely-visible preview. The paywall was confirmed to cut
  off after the sentence introducing "the _same_ context and tools" design
  principle, partway through the "Architecture and tech stack" section.
  Sections that may exist after that point were not read and are not
  represented in this note's claims, artifacts, or cross-references.
- Direct WebFetch of the source URL returned the free-preview content
  summarized by an intermediate model rather than the raw page HTML;
  several claims in this note (Claims 3 and 10, marked accordingly) rely on
  a paraphrased fetch summary of specific figures/technology names rather
  than a single verbatim source sentence, because the fetch tool's summary
  did not preserve a clean, quotable sentence boundary for those specific
  details. All quotes marked as direct quotes above were confirmed as
  short, exact character strings returned by the fetch tool from the source
  page; none were reconstructed or embellished.
- Per MINER.md §2a, `Quote` fields for Claims 3 and 10 are explicitly marked
  as "(no direct quote; see paraphrase in Our assessment/Evidence)" rather
  than fabricating a verbatim sentence, since the fetch tool returned those
  specific figures as a structured summary rather than a quotable excerpt.
- Cross-references verified before writing: re-read
  `failure-sukit-parallel-session-ceiling.md` in full and confirmed the
  concurrency-ceiling claims and quotes cited above; re-read
  `blog-cognition-what-we-learned-building-cloud-agents.md` in full and
  confirmed Claims 3 and 8 by number and content; re-read
  `blog-cursor-self-hosted-cloud-agents.md` in full and confirmed Claim 4 by
  number and content; re-read `blog-latentspace-modal-agent-experience.md`
  in full and confirmed Claim 16 by number and content, including the exact
  "Ramp also runs their accounting agent on us" wording used in that note.
  No claim number was guessed or approximated.
- No contradiction meeting the MINER.md §4a filing bar was identified. The
  apparent tension between this source's low-effort composed-infrastructure
  build (Claim 6, Claim 9-10) and Cognition's multi-year, multi-team
  from-scratch build was assessed as a conditioning-variable difference
  (which layer of the stack each company built vs. bought), not a genuine
  disagreement about the same claim under the same conditions — see the
  "Extends" entry for `blog-cognition-what-we-learned-building-cloud-agents.md`
  above for the reasoning. No contradiction issue was filed.
- Confidence is rated `emerging` overall: the source combines named,
  attributed company sources (CTO, Head of Engineering, founding engineer)
  and specific, dated metrics with independent third-party corroboration on
  one architectural point (Modal), but nearly every figure is self-reported
  by Ramp with no disclosed measurement methodology, and the note is
  explicitly based on a partial (paywalled) read of the source — it does
  not reach `settled`.
