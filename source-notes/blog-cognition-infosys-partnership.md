---
source_url: https://cognition.com/blog/infosys-cognition
source_type: blog-post
title: "Infosys partners with Cognition to expand engineering capacity and help scale its enterprise business"
author: The Cognition Team
date_published: 2026-01-07
date_extracted: 2026-07-21
last_checked: 2026-07-21
status: current
confidence_overall: anecdotal
issue: "#2100"
---

# Infosys partners with Cognition to expand engineering capacity and help scale its enterprise business

> A short, unattributed partnership-announcement post: Infosys (a large global
> IT-services and consulting firm) is deploying Cognition's Devin across its
> own engineering organization and its global client base, starting in
> regulated Financial Services accounts, via three named deployment models —
> internal productivity, services delivery (hybrid human/agent delivery
> pods), and managed service provider — with qualitative six-month
> productivity claims on COBOL and JCP servlet migration work.

## Source Context

- **Type**: blog-post (Cognition's own blog, cognition.com, published
  2026-01-07; a partnership/announcement post, not a technical or
  first-person practitioner account)
- **Author credibility**: Byline is "By The Cognition Team" — no individual
  author or spokesperson is named anywhere in the post, on either the
  Cognition or the Infosys side. This matches the pattern of this corpus's
  other Cognition systems-integrator partnership announcement,
  `blog-cognition-cognizant-partnership.md`, which is likewise entirely
  unattributed corporate narration with zero quoted individuals.
- **Scope**: Covers the fact and shape of the partnership: what is being
  deployed (Devin only — Windsurf is not mentioned, unlike the Cognizant
  post), current vs. planned scope (Financial Services practice today;
  retail, energy, healthcare, and other verticals planned), a six-month
  qualitative productivity claim naming two specific legacy technology
  stacks (COBOL, JCP servlets), and three named deployment models with a
  short description of each. Does NOT cover: any quantified metric (percent
  faster, headcount, dollar figure, timeline for the "record time" claim),
  any named individual at either company, any technical detail about how
  Devin integrates with Infosys's delivery tooling or workflows, any named
  client project, or any discussion of challenges, failures, or risks
  encountered during the six months described.

## Extracted Claims

### Claim 1: Infosys, described as "a global leader in digital services and consulting," has partnered with Cognition to deploy Devin across its own organization and its global client base, and the collaboration is framed as "one of the largest global deployments of agentic software engineering to date," operating in complex, regulated enterprise environments
- **Evidence**: Opening two sentences of the announcement, naming the product (Devin only), the two deployment scopes (Infosys's own organization, its global client base), and an explicit superlative framing of scale.
- **Confidence**: anecdotal (single unattributed corporate announcement; "one of the largest... to date" is an unverifiable superlative with no headcount, seat count, or session-volume figure given)
- **Quote**: "Infosys, a global leader in digital services and consulting, has partnered with Cognition to deploy Devin, the AI software engineer, across its organization and global client base. By augmenting its workforce with autonomous software engineers, Infosys will dramatically expand its delivery capacity. This collaboration represents one of the largest global deployments of agentic software engineering to date, operating within some of the world’s most complex and regulated enterprise environments."
- **Our assessment**: The "one of the largest global deployments... to date" claim should be read as marketing framing, not a measured fact — there is no accompanying number (engineers enabled, sessions run, or client count) to substantiate the superlative, consistent with how this corpus already treats similarly unquantified scale claims from vendor-authored partnership posts (see Cross-References → Corroborates).

### Claim 2: Infosys began its Devin rollout within its Financial Services practice — covering banking, payments, capital markets, insurance, and wealth management — deployed both inside its own teams and inside customer organizations, with planned expansion to retail, energy, healthcare, and other verticals
- **Evidence**: Direct statement of the initial vertical, the five named sub-domains within it, the dual internal/customer-facing deployment surface, and the named expansion verticals.
- **Confidence**: anecdotal (stated rollout scope and plan; no adoption percentage, seat count, or timeline given for the "then" expansion)
- **Quote**: "Infosys has begun by rolling out Devin in its Financial Services practice, across banking, payments, capital markets, insurance, and wealth management use cases—both within its own teams and inside customer organizations. Then, the rollout is aimed towards expanding to retail, energy, healthcare, and other verticals where Infosys operates."
- **Our assessment**: Leading with Financial Services — the most heavily regulated vertical named — as the *first* rollout target (rather than a lower-stakes internal pilot) is a notable sequencing choice for an autonomous coding agent; it implies Infosys and Cognition consider the regulated-banking use case sufficiently mature to deploy first rather than last, which is a different risk posture than a "prove it internally on low-stakes work first" adoption pattern.

### Claim 3: Over the six months preceding this post, Infosys "unlocked material productivity gains" with Devin, with complex COBOL and JCP servlet migration projects specifically named as shifting "from long, resource-heavy undertakings to streamlined processes completed in record time"
- **Evidence**: Direct productivity claim naming two specific legacy technology stacks (COBOL, Java Servlet Pages/JCP) as the illustrative example.
- **Confidence**: anecdotal (purely qualitative — "material productivity gains" and "record time" are given with no percentage, hours-saved figure, project count, or before/after timeline; contrast with `blog-cognition-devin-productivity-estimation.md`, which is Cognition's own quantified, held-out-validated productivity methodology)
- **Quote**: "Over the past six months, Infosys has unlocked material productivity gains with Devin. Complex migrations, including COBOL and JCP servlet projects, have shifted from long, resource-heavy undertakings to streamlined processes completed in record time."
- **Our assessment**: This is the post's sole evidentiary claim about outcomes, and it is entirely qualitative. Naming COBOL and JCP servlets specifically (rather than speaking generically about "legacy migration") does add some specificity — it identifies exactly the kind of scarce-expertise, hard-to-read legacy stack that this corpus's other migration sources single out as where AI coding agents deliver the clearest wins (see Cross-References → Corroborates) — but the claim itself carries no number that could be checked or compared across sources.

### Claim 4: Infosys will use Devin in three primary ways: (1) Internal Productivity — deployed within Infosys's own teams to accelerate internal development; (2) Services Delivery — embedded into customer engagements, pairing human and autonomous engineers into "hybrid delivery pods" that "significantly accelerate execution"; and (3) Managed Service Provider (MSP) — deployed and managed by Infosys directly inside customer environments with ongoing operation, governance, and optimization, supplemented by Infosys's own vertical playbooks
- **Evidence**: Direct three-part enumeration of deployment models, each with a short description of mechanism and stated goal.
- **Confidence**: anecdotal (stated operating model with no data on how many engagements currently use each of the three models, or their relative scale)
- **Quote**: "Internal productivity. Infosys will deploy Devin within its own teams to accelerate internal development and delivery. Services delivery. Infosys will embed Devin into customer engagements, pairing human engineers with autonomous engineers to form hybrid delivery pods that significantly accelerate execution. Managed Service Provider (MSP). Infosys will deploy and manage Devin directly within customer environments, providing ongoing operation, governance, and optimization of agentic software engineering systems. Infosys will provide vertical expertise to these deployments via curated knowledge and playbooks to accelerate adoption and impact."
- **Our assessment**: This three-model taxonomy (internal-only, embedded-hybrid, fully-managed) is the most structurally useful content in the post — it is a concrete, named spectrum of how a systems-integrator can operationalize an autonomous coding agent across an increasing degree of customer-facing responsibility, from "we use it ourselves" to "we run it as a managed service inside your environment with governance." The MSP model in particular (Infosys operating Devin *inside* a client's own environment, with governance, rather than delivering work product from Infosys's own environment) is a deployment shape not previously named this explicitly in this corpus's SI-partnership material (see Cross-References → Novel).

### Claim 5: To support the rollout, Infosys and Cognition are jointly developing engineering frameworks and enablement programs specifically designed for large, regulated enterprises, intended to provide standardized architecture, best practices, and automation capabilities that reduce complexity and enhance operational resilience
- **Evidence**: Direct statement of joint supporting infrastructure under development, naming its intended outputs (standardized architecture, best practices, automation capabilities) and goals (reduced complexity, operational resilience).
- **Confidence**: anecdotal (stated future/ongoing work; no description of what the frameworks actually contain, no release date, no named example enterprise using them yet)
- **Quote**: "To support this rollout, Infosys and Cognition are developing engineering frameworks and enablement programs designed for large, regulated enterprises. Infosys aims to provide enterprises with standardized architecture, best practices, and automation capabilities that reduce complexity and enhance operational resilience."
- **Our assessment**: This is a forward-looking, unshipped claim (frameworks are "developing," not delivered) framed specifically around regulated-enterprise needs (architecture standardization, governance, resilience) rather than raw velocity — a different emphasis than the pure speed/cost framing common in less-regulated adoption stories elsewhere in this corpus.

### Claim 6: The post closes with an unattributed statement of enthusiasm about continuing to work with Infosys "to accelerate software engineering across the firm and its enterprise clients," and — like the corpus's other Cognition SI-partnership post — contains no quote attributed to any named individual at either Infosys or Cognition
- **Evidence**: Closing sentence of the announcement, phrased in first-person plural without attribution to any named individual; confirmed by re-reading the full stripped page text for any quoted spokesperson.
- **Confidence**: anecdotal (unattributed corporate sentiment, not a substantive claim)
- **Quote**: "We’re excited to continue working closely with Infosys to accelerate software engineering across the firm and its enterprise clients."
- **Our assessment**: Contentless as a claim on its own, but notable by omission in the same way `blog-cognition-cognizant-partnership.md` Claim 6 is: no executive, engineering lead, or named practitioner from either company is quoted anywhere in the piece. This should inform how the guide weighs this source relative to case studies that do quote named practitioners (e.g. `blog-cursor-nab-legacy-migration.md`, `blog-openai-bbva-banking-transformation.md`) — it is evidence that the partnership exists and roughly what it covers, not first-person testimony about how the rollout is actually going day to day.

### Claim 7: This post follows a near-identical structural template to Cognition's earlier Cognizant partnership announcement — same unattributed byline convention, same "internal adoption then client-base expansion" narrative arc, same closing call-to-action sentence inviting enterprises to contact Cognition's enterprise team — but for a different systems-integrator partner (Infosys vs. Cognizant), a different initial vertical emphasis (Financial Services-first vs. no single named lead vertical), and a three-model deployment taxonomy not present in the Cognizant post (which names no equivalent internal/services/MSP breakdown)
- **Evidence**: Structural comparison against `blog-cognition-cognizant-partnership.md`'s full reproduced text (see that note's Concrete Artifacts section).
- **Confidence**: emerging (a direct textual/structural comparison between two source documents rather than an inference about intent — but a corpus-internal, meta-structural observation rather than a strongly-evidenced claim about the world, so `emerging` fits this corpus's confidence taxonomy better than `settled`)
- **Quote**: (no direct quote; see paraphrase above — this is a cross-document structural observation, not a claim quotable from either single source)
- **Our assessment**: Cognition appears to be running a repeatable announcement format for systems-integrator partnerships (unattributed "By The Cognition Team" byline, internal-then-client-facing narrative, closing enterprise-team CTA). This Infosys post is more operationally specific than the Cognizant post in one respect — it names three distinct deployment models (internal, services-delivery/hybrid-pod, MSP) where the Cognizant post describes only a two-stage internal-then-client rollout with an embedded forward-deployed-engineer support team — suggesting Cognition's own articulation of its SI-partnership playbook has become more granular between the two posts (Cognizant: 2026-01-28; this post: 2026-01-07 — note this Infosys post is actually the *earlier* of the two by three weeks, so the added granularity is not simply "later post is more detailed"; the two posts differ in structure independent of publication order).

## Concrete Artifacts

```
Full body text of the announcement (cognition.com/blog/infosys-cognition,
published 01.07.26, byline "By The Cognition Team"), reproduced in full from
raw HTML — this is the entire substantive content of the post:

"Infosys, a global leader in digital services and consulting, has partnered
with Cognition to deploy Devin, the AI software engineer, across its
organization and global client base.

By augmenting its workforce with autonomous software engineers, Infosys will
dramatically expand its delivery capacity. This collaboration represents one
of the largest global deployments of agentic software engineering to date,
operating within some of the world’s most complex and regulated enterprise
environments.

Infosys has begun by rolling out Devin in its Financial Services practice,
across banking, payments, capital markets, insurance, and wealth management
use cases—both within its own teams and inside customer organizations. Then,
the rollout is aimed towards expanding to retail, energy, healthcare, and
other verticals where Infosys operates.

Over the past six months, Infosys has unlocked material productivity gains
with Devin. Complex migrations, including COBOL and JCP servlet projects,
have shifted from long, resource-heavy undertakings to streamlined processes
completed in record time.

Infosys will leverage Devin in three primary ways:

Internal productivity. Infosys will deploy Devin within its own teams to
accelerate internal development and delivery.

Services delivery. Infosys will embed Devin into customer engagements,
pairing human engineers with autonomous engineers to form hybrid delivery
pods that significantly accelerate execution.

Managed Service Provider (MSP). Infosys will deploy and manage Devin
directly within customer environments, providing ongoing operation,
governance, and optimization of agentic software engineering systems.
Infosys will provide vertical expertise to these deployments via curated
knowledge and playbooks to accelerate adoption and impact.

To support this rollout, Infosys and Cognition are developing engineering
frameworks and enablement programs designed for large, regulated
enterprises. Infosys aims to provide enterprises with standardized
architecture, best practices, and automation capabilities that reduce
complexity and enhance operational resilience.

We’re excited to continue working closely with Infosys to accelerate
software engineering across the firm and its enterprise clients.

Organizations interested in deploying Devin at scale can contact Cognition’s
enterprise team to learn more."
```

## Cross-References

- **Corroborates**: `blog-cognition-cognizant-partnership.md` — both are
  unattributed, vendor-authored SI-partnership announcements from Cognition
  with the same narrative shape (deploy internally first, expand to client
  base, name target verticals, close with an unattributed enthusiasm
  statement and enterprise-team CTA). Claim 7 above documents the structural
  parallel directly. This source's Claim 2 (Financial Services as the
  regulated, legacy-heavy first vertical) also corroborates
  `blog-thoughtworks-harrison-insurance-legacy-modernization.md` Claim 1 and
  Claim 7 (legacy is best defined by how expensive/slow/risky change is
  rather than by technology vintage, and AI reduces the uncertainty/manual
  effort of understanding a legacy estate) — this source's Claim 3 (COBOL
  and JCP servlet migrations shifting to "record time") is a concrete,
  named vendor-side instance of exactly the kind of legacy-modernization
  acceleration Thoughtworks argues AI now makes possible, from an
  independent organization (Cognition/Infosys vs. Thoughtworks/Mechanical
  Orchard).
- **Corroborates**: `blog-cursor-nab-legacy-migration.md` Claim 6 (mainframe
  Assembly migration at NAB was "previously categorically impossible due to
  expertise scarcity" and unblocked by AI-generated flowcharts/business-logic
  summaries) and `blog-cursor-paypal-enterprise-adoption.md` Claim 5 (a
  3,000-application Java upgrade completed in 2 months vs. an 8-12 month
  original estimate) — this source's Claim 3 (COBOL/JCP servlet migrations
  shifting to "record time") is a third, independent vendor's claim of
  large-scale legacy-migration acceleration via AI coding agents, though
  unlike NAB and PayPal this source gives no quantified speedup figure,
  making it the weakest-evidenced of the three migration claims.
- **Corroborates**: `blog-thebatch-fde-agents-aiact-issue355.md` Claim 1
  (forward-deployed engineers embed within client organizations to
  customize agentic workflows) and `blog-latentspace-meurer-agent-engineer-fde.md`
  Claim 4 (most customer-specific agent-engineering work happens at the
  orchestration/integration layer) — this source's Claim 4 "Services
  delivery" model (pairing human engineers with autonomous engineers into
  "hybrid delivery pods" embedded in customer engagements) is a concrete,
  named instance of the same embedded-delivery pattern, adding the "hybrid
  delivery pod" framing (human + autonomous engineer paired together) as a
  specific team-composition detail neither of those two sources gives.
- **Contradicts**: None identified. This source's qualitative, unquantified
  productivity claim (Claim 3) does not contradict
  `blog-cognition-devin-productivity-estimation.md`'s quantified estimator
  methodology; the two are complementary (marketing-level claim vs.
  methodology for measuring such claims), not opposing.
- **Extends**: `blog-cognition-cognizant-partnership.md` — this source adds
  a three-model deployment taxonomy (internal / services-delivery-hybrid-pod
  / MSP) that the Cognizant post does not name explicitly, and names a
  specific legacy-technology pair (COBOL, JCP servlets) where the Cognizant
  post speaks only generically of "code migration, refactoring, testing, and
  maintenance." Also extends `blog-cognition-devin-productivity-estimation.md`
  by providing a second, independent (unquantified) enterprise-productivity
  claim to sit alongside that source's quantified estimator methodology —
  together they illustrate the gap between how Cognition markets
  productivity claims in partnership announcements (qualitative, "material
  gains," "record time") versus how it claims to actually measure them
  internally (r_log = 0.74 held-out validated estimator).
- **Novel**: The explicit three-model SI deployment taxonomy (Internal
  Productivity / Services Delivery / Managed Service Provider) is new to
  this corpus — no prior source note names this specific three-way split for
  how a systems integrator operationalizes an autonomous coding agent across
  its own use, embedded client engagements, and fully-managed deployment
  inside a client's own environment. The MSP model specifically — an SI
  deploying and *managing* an autonomous agent directly inside a customer's
  own environment, with "ongoing operation, governance, and optimization" —
  is a deployment shape not previously documented this explicitly in this
  corpus's enterprise-adoption material; it goes further than the FDE
  pattern (an embedded engineer helping a client use a tool) toward the SI
  operating the agent as an ongoing managed service on the client's behalf.

## Guide Impact

Note on chapter mapping: the current guide (`guide/00`–`06`) has no chapter
dedicated to enterprise deployment/orchestration. The closest existing home
for this source's material is **Chapter 05 (Team Adoption)**, which already
covers scaling, team-composition, and legacy-migration evidence and already
hosts the NAB Assembly-migration case study (around line 981). Chapter 02
(harness-engineering / CLAUDE.md config) and Chapter 04 (context-engineering
/ context-window budget) are unrelated to this source's content, so it is
*not* mapped to them.

- **Chapter 05 (Team Adoption)**: Add this source's three-model deployment
  taxonomy (Claim 4: Internal Productivity, Services Delivery/hybrid pods,
  Managed Service Provider) as a named framework for how systems integrators
  can operationalize autonomous coding agents at increasing levels of
  customer-environment responsibility. This is a team/organization-scaling
  pattern and fits alongside Chapter 05's existing scaling and
  team-composition material. Flag explicitly that the source gives no data
  on relative adoption or scale across the three models — it is a stated
  taxonomy, not a measured distribution of effort. If the maintainers judge
  the SI-deployment-model material to be substantial enough, it may warrant
  its own new section (or a new chapter) rather than being folded into
  Chapter 05, since no current chapter squarely covers enterprise/SI
  deployment shapes.
- **Chapter 05 (Team Adoption)**: Add the "hybrid delivery pod" concept
  (Claim 4) — pairing a human engineer with an autonomous engineer inside a
  single customer-facing delivery team — as a named team-composition pattern
  for services-delivery engagements, cross-referenced against the FDE
  material in `blog-thebatch-fde-agents-aiact-issue355.md` and
  `blog-latentspace-meurer-agent-engineer-fde.md`.
- **Chapter 05 (Team Adoption), legacy-migration evidence**: This source's
  COBOL/JCP servlet claim (Claim 3) belongs alongside the NAB
  Assembly-migration content already in Chapter 05 (around line 981) and
  PayPal's Java-upgrade claim as a third vendor data point on
  AI-accelerated legacy migration — but explicitly note it is the
  weakest-evidenced of the three (no percentage, no before/after timeline,
  no project count), unlike NAB's and PayPal's quantified figures.
- Do NOT cite Claim 1's "one of the largest global deployments... to date"
  framing as an independently verified fact in the guide — it should only
  be attributed as Cognition's own characterization of the partnership's
  scale.

## Extraction Notes

- The source is a JavaScript-rendered (Next.js-style) page. A first-pass
  WebFetch (which processes content through a small model before returning
  it) produced a paraphrased, re-worded version of the post rather than
  verbatim text — consistent with the verbatim-extraction difficulty already
  documented for other Cognition posts in this corpus (see
  `blog-cognition-devin-productivity-estimation.md` Extraction Notes). To
  obtain and verify verbatim text, the raw HTML was fetched directly via
  `curl` with a browser user-agent, stripped of script/style tags and HTML
  markup with a small Python script, and every quote used above was located
  and confirmed character-for-character in that stripped text before being
  copied into this note (per MINER.md §2a). The WebFetch paraphrase was
  discarded and is not used or quoted anywhere in this note.
- No sub-pages were followed. The page's only other links are to a generic
  "recent Cognition blog posts" footer list (same nine-title pattern seen in
  `blog-cognition-cognizant-partnership.md`) and standard nav/legal pages —
  none met the MINER.md §1 "substantive linked page" criterion.
- Publish date (01.07.26, read as 2026-01-07 in the site's MM.DD.YY
  convention, matching the "01.28.26" = 2026-01-28 reading already used for
  the Cognizant post) was confirmed from the visible page byline text in the
  stripped HTML.
- Claim 7's structural comparison against `blog-cognition-cognizant-partnership.md`
  was made by re-reading that note's full Concrete Artifacts section (the
  Cognizant post's complete reproduced body text) side by side with this
  post's body text; the claim that the Cognizant post "names no equivalent
  internal/services/MSP breakdown" was verified by confirming its reproduced
  text contains no such three-part enumeration.
- All cross-reference claim numbers cited from other source notes
  (`blog-cognition-cognizant-partnership.md` Claim 6;
  `blog-thoughtworks-harrison-insurance-legacy-modernization.md` Claim 1 and
  Claim 7; `blog-cursor-nab-legacy-migration.md` Claim 6;
  `blog-cursor-paypal-enterprise-adoption.md` Claim 5;
  `blog-thebatch-fde-agents-aiact-issue355.md` Claim 1;
  `blog-latentspace-meurer-agent-engineer-fde.md` Claim 4) were verified by
  re-reading each cited note's actual numbered claims before citing; none
  were guessed or approximated.
- No contradiction meeting the MINER.md §4a filing bar was identified — this
  source's unquantified productivity claim does not oppose any existing
  source note's claim about Devin or comparable agents; it simply carries
  less evidentiary weight than the quantified sources it sits alongside. No
  contradiction issue was filed.
- Overall confidence is set to `anecdotal`, matching
  `blog-cognition-cognizant-partnership.md`'s rating and for the same
  reason: every substantive claim in this source is an unattributed vendor
  statement of intent, plan, or qualitative outcome, with zero accompanying
  metrics, timelines, or named practitioner testimony from either company.
