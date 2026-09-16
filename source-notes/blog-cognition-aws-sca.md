---
source_url: https://cognition.com/blog/aws-sca
source_type: blog-post
title: "Cognition and AWS team up to help ambitious teams ship more, faster"
author: The Cognition Team
date_published: 2026-09-15
date_extracted: 2026-09-16
last_checked: 2026-09-16
status: current
confidence_overall: anecdotal
issue: "#3484"
---

# Cognition and AWS team up to help ambitious teams ship more, faster

> A cloud-platform partnership announcement: Cognition and AWS have signed a
> multi-year Strategic Collaboration Agreement putting Devin on AWS
> Marketplace with native Agent Toolkit for AWS integration, describing a
> single-tenant, VPC-isolated deployment architecture and naming
> Mercedes-Benz's and an unnamed automaker's COBOL-modernization results —
> unusually for this corpus's Cognition partnership posts, it also quotes
> named spokespeople from both companies and a joint customer.

## Source Context

- **Type**: blog-post (Cognition's own blog, cognition.com, published
  2026-09-15; a partnership/announcement post, not a technical or
  independent-journalist account)
- **Author credibility**: Byline is "By The Cognition Team," matching the
  unattributed-corporate-byline convention of this corpus's other Cognition
  partnership posts (`blog-cognition-cognizant-partnership.md`,
  `blog-cognition-infosys-partnership.md`). Unlike those two posts, however,
  the body text itself quotes three named individuals by name and title: Art
  Levy (VP of Global Partnerships, Cognition), Anasuya Strasner (Director of
  North America ISVs, AWS), and Christina Garcia (SVP of Engineering, Echo
  Global Logistics — a joint customer, not either partner company). This is
  a materially stronger attribution profile than the Cognizant and Infosys
  posts, though the quotes are still vendor-selected and vendor-published,
  not independently sourced.
- **Scope**: Covers the fact and shape of the partnership (multi-year SCA,
  AWS Marketplace listing, Agent Toolkit for AWS integration), three named
  target workflows (legacy migration, security/engineering backlog
  clearance, capacity for strategic work), the technical deployment
  architecture (single-tenant, region-selectable, dedicated VPC, per-session
  isolated VMs, audit-log API integration), and two named customer results
  (Mercedes-Benz, an unnamed "global automaker") plus one named customer
  testimonial (Echo Global Logistics) and one customer name-drop with no
  detail (ActiveCampaign). Does NOT cover: any dollar figure for the SCA
  itself, any timeline for when the deeper "engineering integrations" being
  "explored" will ship, any headcount or seat-count figure, any discussion
  of challenges or failure modes, or any detail on how Mercedes-Benz's or
  the automaker's COBOL migration was actually executed beyond the two
  headline numbers.

## Extracted Claims

### Claim 1: Cognition and AWS have entered a multi-year Strategic Collaboration Agreement (SCA) explicitly framed as helping enterprises "deploy autonomous engineers in production," with a stated purpose of giving engineers "time back to build and solve hard problems" rather than a purely cost- or speed-framed purpose
- **Evidence**: Opening statement of the announcement, naming the agreement type and its stated human-capacity rationale.
- **Confidence**: anecdotal (single unattributed corporate announcement; no contract value, duration in years, or headcount given)
- **Quote**: "Cognition and Amazon Web Services (AWS) have entered a multi-year Strategic Collaboration Agreement (SCA) to help enterprises deploy autonomous engineers in production, giving engineers time back to build and solve hard problems."
- **Our assessment**: The "time back to build" framing — rather than a pure cost-reduction or velocity framing — echoes this corpus's other Cognition posts (see Cross-References → Corroborates) that emphasize freeing engineers for higher-value work rather than headcount reduction. As with the Cognizant/Infosys posts, this is a stated rationale, not a measured outcome.

### Claim 2: Devin is already purchasable through AWS Marketplace, and joint customers can use the "Agent Toolkit for AWS" directly inside Devin, with Cognition and AWS additionally "exploring deeper engineering integrations" not yet shipped
- **Evidence**: Direct statement distinguishing what is live today (Marketplace listing, Agent Toolkit for AWS) from what is still exploratory (unspecified "deeper engineering integrations").
- **Confidence**: anecdotal (stated current capability plus an unspecified future-work claim; no detail on what the Agent Toolkit for AWS actually does beyond being named, and no timeline for the "deeper" integrations)
- **Quote**: "Joint customers can already purchase Devin through AWS Marketplace and use the Agent Toolkit for AWS directly in Devin. Cognition and AWS are also exploring deeper engineering integrations that make Devin easier to use within customers' existing AWS environments."
- **Our assessment**: This is the concrete, checkable part of the announcement — a live Marketplace listing and a named toolkit integration are specific, present-tense facts rather than stated intent, distinguishing this claim from most of the rest of the post's forward-looking language. No corpus source note previously documents an AI coding agent's AWS Marketplace listing or an "Agent Toolkit for AWS" integration (see Cross-References → Novel).

### Claim 3: Cognition names three specific target workflows for the AWS partnership: moving legacy workloads to AWS faster (via Devin analyzing an existing system, recreating its behavior, writing replacement code, and testing against known outputs), clearing security and engineering backlogs inside existing AWS environments (via a dedicated AWS VPC running multiple parallel sessions on migrations, framework upgrades, and security fixes), and unlocking capacity for more strategic work by having Devin absorb repetitive/legacy-maintenance tasks
- **Evidence**: Three-item bulleted list under "Devin helps teams modernize on AWS," each item with a one-sentence mechanism description.
- **Confidence**: anecdotal (stated workflow taxonomy with no data on relative usage across the three categories)
- **Quote**: "Move legacy workloads to AWS faster. Cognition and AWS will work with customers on modernization projects where Devin analyzes an existing system, recreates the system's behavior, writes replacement code, and tests the new system against known outputs, compressing modernization timelines from years to months. Clear security and engineering backlogs within existing AWS environments. Customers can connect to Devin's dedicated AWS VPC and run multiple sessions in parallel on migrations, framework upgrades, and security fixes. Unlock capacity for more strategic work on AWS. Devin takes on the repetitive tasks and legacy maintenance, giving engineering teams more time and headspace to build new products."
- **Our assessment**: The "recreates the system's behavior... tests the new system against known outputs" description is a slightly more specific methodology statement than the generic "migration, refactoring, testing, maintenance" workflow list in `blog-cognition-cognizant-partnership.md` Claim 3 — it implies a behavior-preservation/regression-testing approach to legacy rewrites specifically, though still without a named technique (e.g., differential testing, golden-output comparison) or tooling detail.

### Claim 4: Mercedes-Benz used Devin to analyze more than 200,000 lines of COBOL, reducing an estimated eight-month modernization project to eight days
- **Evidence**: Named customer, quantified line count, and a specific before/after timeline comparison (8 months → 8 days).
- **Confidence**: anecdotal (single named customer, single vendor-reported figure; no description of what "analyze" specifically produced — e.g., documentation, a migration plan, or executable replacement code — and no independent verification of the 8-month baseline estimate)
- **Quote**: "Mercedes-Benz used Devin to analyze more than 200,000 lines of COBOL, reducing an estimated eight-month modernization project to eight days."
- **Our assessment**: This is the single most quantified and attention-grabbing claim in the post — a stated 30x-plus timeline compression (8 months = ~240 days → 8 days) on a named Fortune 500 customer with a specific line count. However, "analyze" is a narrower verb than "migrate" or "modernize" — the claim as written does not say Mercedes-Benz's COBOL system was actually replaced or is running on AWS, only that Devin analyzed it, which likely corresponds to a discovery/documentation phase (similar to the flowchart/business-logic-summary output in `blog-cursor-nab-legacy-migration.md` Claim 6) rather than a completed migration. The guide should not cite this as "Mercedes-Benz migrated 200K lines of COBOL in 8 days" — that overstates what the sentence actually claims.

### Claim 5: A second, unnamed "global automaker" used Devin to move a 25,000-line COBOL workflow from a mainframe to AWS Lambda, at an estimated 73% lower cost
- **Evidence**: A second customer example, this one anonymized, with a specific line count, a specific migration target (mainframe → AWS Lambda), and a specific cost-reduction percentage.
- **Confidence**: anecdotal (single vendor-reported figure for an unnamed customer; no baseline cost figure given to make the 73% reduction checkable, and no detail on migration duration or validation method)
- **Quote**: "Another global automaker used Devin to move a 25,000-line COBOL workflow from a mainframe to AWS Lambda, at an estimated 73% lower cost."
- **Our assessment**: Unlike Claim 4, this example describes a completed migration (mainframe to Lambda) rather than only an analysis phase, but the customer is anonymized, which is a lower attribution bar than the named Mercedes-Benz example in the same paragraph — a common pattern where a vendor pairs one attributable, high-profile logo with one unattributable but more operationally complete result.

### Claim 6: Art Levy, VP of Global Partnerships at Cognition, is quoted framing legacy-system work as historically inevitable friction for engineers that Devin removes, enabling enterprises to "pair their engineers with autonomous agents on infrastructure they already trust" and address deferred work
- **Evidence**: Named, titled spokesperson quote from the Cognition side of the partnership.
- **Confidence**: anecdotal (single named spokesperson's characterization; rhetorical framing, not a measured claim)
- **Quote**: "For most of software's history, engineers have been stifled by the need to work on legacy systems. That changes with Devin," said Art Levy, VP of Global Partnerships at Cognition. "With Devin, enterprises can pair their engineers with autonomous agents on infrastructure they already trust, and take on the work they've been deferring for years, leaving them time to build."
- **Our assessment**: The "infrastructure they already trust" phrase is the partnership's underlying value proposition for choosing AWS specifically over a vendor-hosted-only deployment — trust is being outsourced to the existing cloud relationship rather than established fresh with Cognition. This is a notable strategic rationale for why an agent vendor would seek a hyperscaler SCA at all, distinct from the SI-distribution rationale in the Cognizant/Infosys posts (see Cross-References → Contrasts).

### Claim 7: Devin's AWS deployment model runs in a single-tenant environment in a customer-selected AWS region, with a dedicated VPC for data/organizational-knowledge residency; each Devin session runs in its own virtual machine created per-task and destroyed on completion; and Devin's audit-log APIs feed the customer's existing monitoring/compliance tooling, letting platform teams apply the same regional, network, and audit controls used elsewhere in their AWS environment
- **Evidence**: A dedicated "How Devin runs inside an AWS environment" section describing the architecture in four sentences.
- **Confidence**: anecdotal (architecture description, not independently audited; no detail on which specific compliance frameworks or monitoring tools are supported, and no mention of the VM isolation technology used)
- **Quote**: "Customers deploy Devin in a single-tenant environment on AWS and choose the region where it runs. Their data and organizational knowledge remain inside a dedicated VPC, helping teams meet internal policies and local data residency requirements. Each Devin session runs in its own virtual machine, created for the task and removed when the work is finished. Devin's audit log APIs record user actions and feed the monitoring and compliance tools a customer already operates. Platform teams apply the same regional, network, and audit controls they use across the rest of their AWS environment."
- **Our assessment**: The "own virtual machine, created for the task and removed when the work is finished" description is consistent with, and a customer-facing restatement of, the per-session VM-isolation architecture Cognition describes at the infrastructure-engineering level in `blog-cognition-what-we-learned-building-cloud-agents.md` Claim 3 (microVM-based isolation, "over a year of hypervisor engineering"). This post does not name the isolation technology (no "microVM" or hypervisor mention here), so it should be read as the product-marketing restatement of that internal architecture claim, not as new technical detail.

### Claim 8: Anasuya Strasner, Director of North America ISVs at AWS, is quoted endorsing the partnership from AWS's side, framing it as bringing "autonomous software engineering to enterprises on the secure, global infrastructure they already rely on"
- **Evidence**: Named, titled spokesperson quote from the AWS side of the partnership — the only AWS-side individual quoted in the post.
- **Confidence**: anecdotal (single named spokesperson's characterization; no metric given)
- **Quote**: "Our customers want to modernize faster and put AI to work in production, and Devin running on AWS gives them a proven way to do it," said Anasuya Strasner, Director of North America ISVs at AWS. "This collaboration brings autonomous software engineering to enterprises on the secure, global infrastructure they already rely on, so they can accelerate migrations, clear technical debt, and focus their teams on what moves the business forward."
- **Our assessment**: This is structurally notable relative to the corpus's other Cognition partnership posts: neither `blog-cognition-cognizant-partnership.md` nor `blog-cognition-infosys-partnership.md` quotes anyone from the partner organization by name. Having a named AWS director on record is a stronger (though still vendor-curated) attribution signal than either of those posts achieves, even though AWS is a much larger organization than the quote alone would suggest is co-invested in the relationship.

### Claim 9: Christina Garcia, SVP of Engineering at Echo Global Logistics, is quoted describing Devin as "an important part of how our engineering teams work," citing DeepWiki-powered code insights and closing gaps in legacy systems as specific use cases, and identifying Echo as "a long-standing AWS customer"
- **Evidence**: Named, titled customer-side spokesperson quote — the only quote in the post from an actual end-user organization rather than either partner vendor.
- **Confidence**: anecdotal (single named customer's characterization of its own usage; no metric, headcount, or before/after figure given)
- **Quote**: "Devin has become an important part of how our engineering teams work at Echo — from DeepWiki-powered code insights that help us understand our codebases, to closing gaps in legacy systems," said Christina Garcia, SVP of Engineering at Echo Global Logistics. "As a long-standing AWS customer, we're excited to see Devin and AWS integrate more deeply through this collaboration."
- **Our assessment**: This is the strongest attribution in the post — a named customer executive, not a Cognition or AWS employee, describing actual current usage rather than a stated future plan. The specific mention of "DeepWiki-powered code insights" corroborates that DeepWiki (documented as a feature shipped in August 2025 per `blog-cognition-one-year-of-building-together.md` Claim 8) is in active customer use roughly a year after launch, though the claim remains a single customer's qualitative characterization with no usage metric.

### Claim 10: ActiveCampaign is named alongside Mercedes-Benz and Echo Global Logistics as a joint customer whose "strong momentum" the AWS collaboration builds on, but receives no quote, no usage detail, and no outcome figure anywhere else in the post
- **Evidence**: A single mention in the opening paragraph's customer-momentum sentence; the name does not recur in the "What our customers are achieving together" section, which covers only Mercedes-Benz, the unnamed automaker, and Echo Global Logistics.
- **Confidence**: anecdotal (bare name-drop with zero supporting detail)
- **Quote**: "The collaboration builds on strong momentum with Mercedes-Benz, Echo Global Logistics, ActiveCampaign, and other joint customers."
- **Our assessment**: This is the weakest-evidenced customer reference in the post — a logo listed for social proof with no accompanying claim of any kind. It should not be cited in the guide as an example of anything beyond "named as a customer," since the post itself provides no further detail to attribute to ActiveCampaign specifically.

## Concrete Artifacts

```
Full body text of the announcement (cognition.com/blog/aws-sca, published
09.15.26, byline "By The Cognition Team"), reproduced verbatim from
stripped raw HTML (WebFetch's small-model summarization paraphrased this
page, consistent with other Cognition posts in this corpus — see Extraction
Notes; the text below was independently verified against raw HTML fetched
via curl):

"Cognition and Amazon Web Services (AWS) have entered a multi-year Strategic
Collaboration Agreement (SCA) to help enterprises deploy autonomous
engineers in production, giving engineers time back to build and solve hard
problems. Cognition and AWS will help customers move legacy workloads to
AWS faster and clear security and engineering backlogs, freeing teams to
build new products on AWS.

Joint customers can already purchase Devin through AWS Marketplace and use
the Agent Toolkit for AWS directly in Devin. Cognition and AWS are also
exploring deeper engineering integrations that make Devin easier to use
within customers' existing AWS environments. The collaboration builds on
strong momentum with Mercedes-Benz, Echo Global Logistics, ActiveCampaign,
and other joint customers.

Devin helps teams modernize on AWS, so they can get back to building new
things

Even the best-resourced engineering team has more migration, security, and
maintenance work than it has capacity for, especially as legacy systems
age.

Devin helps teams get that work done. It can understand a codebase, plan an
approach, write code, test its work, and remediate issues it finds.
Engineers decide what gets built and review the output; Devin handles the
rest.

Through this collaboration, teams can use Devin to:

Move legacy workloads to AWS faster. Cognition and AWS will work with
customers on modernization projects where Devin analyzes an existing
system, recreates the system's behavior, writes replacement code, and
tests the new system against known outputs, compressing modernization
timelines from years to months.

Clear security and engineering backlogs within existing AWS environments.
Customers can connect to Devin's dedicated AWS VPC and run multiple
sessions in parallel on migrations, framework upgrades, and security
fixes.

Unlock capacity for more strategic work on AWS. Devin takes on the
repetitive tasks and legacy maintenance, giving engineering teams more time
and headspace to build new products. Coupled with AWS infrastructure, this
allows new ideas to move into production faster.

"For most of software's history, engineers have been stifled by the need
to work on legacy systems. That changes with Devin," said Art Levy, VP of
Global Partnerships at Cognition. "With Devin, enterprises can pair their
engineers with autonomous agents on infrastructure they already trust, and
take on the work they've been deferring for years, leaving them time to
build."

How Devin runs inside an AWS environment

Customers deploy Devin in a single-tenant environment on AWS and choose the
region where it runs. Their data and organizational knowledge remain inside
a dedicated VPC, helping teams meet internal policies and local data
residency requirements.

Each Devin session runs in its own virtual machine, created for the task
and removed when the work is finished. Devin's audit log APIs record user
actions and feed the monitoring and compliance tools a customer already
operates. Platform teams apply the same regional, network, and audit
controls they use across the rest of their AWS environment.

"Our customers want to modernize faster and put AI to work in production,
and Devin running on AWS gives them a proven way to do it," said Anasuya
Strasner, Director of North America ISVs at AWS. "This collaboration
brings autonomous software engineering to enterprises on the secure,
global infrastructure they already rely on, so they can accelerate
migrations, clear technical debt, and focus their teams on what moves the
business forward."

What our customers are achieving together

Leading enterprises, like Echo Global Logistics, are already building and
shipping more with Devin.

"Devin has become an important part of how our engineering teams work at
Echo — from DeepWiki-powered code insights that help us understand our
codebases, to closing gaps in legacy systems," said Christina Garcia, SVP
of Engineering at Echo Global Logistics. "As a long-standing AWS customer,
we're excited to see Devin and AWS integrate more deeply through this
collaboration."

Devin is also helping companies complete modernization work faster.
Mercedes-Benz used Devin to analyze more than 200,000 lines of COBOL,
reducing an estimated eight-month modernization project to eight days.
Another global automaker used Devin to move a 25,000-line COBOL workflow
from a mainframe to AWS Lambda, at an estimated 73% lower cost.

Get started

Devin is available on AWS Marketplace. Organizations interested in
deploying Devin at scale can contact Cognition's enterprise team to learn
more."
```

## Cross-References

- **Corroborates**: `blog-cognition-what-we-learned-building-cloud-agents.md`
  Claim 3 (Cognition's internal account of building microVM-based,
  per-session isolated compute after concluding shared-kernel containers
  are a real security threat, taking "over a year of hypervisor
  engineering"). This source's Claim 7 (each Devin session runs in "its own
  virtual machine, created for the task and removed when the work is
  finished") is the customer-facing, product-marketing restatement of that
  same internal architecture decision — consistent with, though not adding
  new technical detail to, the internal account.
- **Corroborates**: `blog-cognition-one-year-of-building-together.md` Claim
  8 (product changelog naming "DeepWiki in the IDE" as an August 2025
  release). This source's Claim 9 (Christina Garcia of Echo Global
  Logistics citing "DeepWiki-powered code insights" as an actively used
  feature roughly a year later) is independent evidence that DeepWiki has
  moved from a shipped feature to reported customer-facing usage.
- **Corroborates**: `blog-cursor-nab-legacy-migration.md` Claim 6 (Assembly
  mainframe migration at NAB, previously "categorically impossible due to
  expertise scarcity," unblocked by AI-generated flowcharts/business-logic
  summaries) and `blog-cognition-doe-genesis-mission.md` Claim 4
  ("modernizing legacy scientific code" — Fortran/C++/COBOL — framed around
  preserving institutional knowledge "as the researchers who wrote it
  retire"). This source's Claim 4 (Mercedes-Benz's 200,000-line COBOL
  "analysis") is a third, independent instance of the same
  retiring-expertise/scarce-legacy-skill rationale for AI-driven
  modernization, this time in an automotive-enterprise rather than a
  banking or scientific-research context, and for COBOL specifically rather
  than Assembly or Fortran.
- **Corroborates**: `blog-cursor-paypal-enterprise-adoption.md` Claim 5 (a
  3,000-application Java upgrade completed in 2 months vs. an 8-12 month
  original estimate). This source's Claim 5 (an unnamed automaker's
  25,000-line COBOL mainframe-to-Lambda migration at an estimated 73% lower
  cost) is a fourth independent vendor's large-scale legacy-migration
  acceleration claim, though — unlike PayPal's — framed as a cost reduction
  rather than a timeline compression, making it not directly comparable in
  units.
- **Contrasts**: `blog-cognition-cognizant-partnership.md` and
  `blog-cognition-infosys-partnership.md` — both are also unattributed-byline
  ("By The Cognition Team") Cognition partnership announcements, but both
  contain zero quoted individuals from either partner company (each
  source's own Claim 6/Claim 6 respectively notes this explicitly). This
  source breaks that pattern: it quotes three named, titled individuals —
  one from Cognition (Art Levy), one from the partner (Anasuya Strasner of
  AWS), and one from a joint customer (Christina Garcia of Echo Global
  Logistics) — the first Cognition partnership post in this corpus's
  cluster to include customer-side, on-the-record testimony rather than
  only vendor-to-vendor narration. This source's Claim 6 also names a
  different partnership *type* than either: Cognizant and Infosys are
  systems-integrators redistributing Devin to their own client bases (a
  two-hop channel), while this is a direct cloud-platform/marketplace
  integration (a one-hop channel: AWS lists Devin, customers buy and run it
  on AWS directly) — see Claim 2's Marketplace/Agent-Toolkit detail, which
  neither SI post has an equivalent for.
- **Contradicts**: None identified.
- **Extends**: `blog-cognition-doe-genesis-mission.md` Claim 4's "cloud
  modernization" contribution area ("helping migrate legacy applications
  and infrastructure to modern, cloud-native platforms," stated there as an
  intent with no named example) — this source's Claim 5 (automaker's
  mainframe-to-Lambda migration) supplies a concrete, quantified instance of
  exactly that stated intent, for a commercial (not federal-science)
  customer.
- **Novel**: (1) An AI coding agent's AWS Marketplace listing and a named
  "Agent Toolkit for AWS" integration (Claim 2) — no prior corpus source
  documents a cloud-marketplace listing or a hyperscaler-branded toolkit
  integration for any coding agent. (2) The single-tenant/region-selectable/
  dedicated-VPC/per-session-VM/audit-log-API deployment architecture
  description (Claim 7) is the first customer-facing (rather than
  internal-engineering) description of this shape in the corpus. (3) The
  customer-side named testimonial (Claim 9, Christina Garcia/Echo Global
  Logistics) is the first instance in this corpus's Cognition-partnership
  cluster of an actual end-user organization (rather than only Cognition or
  a systems-integrator) being quoted by name.

## Guide Impact

- **Chapter 05 (Team Adoption)**: Add this source alongside
  `blog-cognition-cognizant-partnership.md` and
  `blog-cognition-infosys-partnership.md` as a third, structurally distinct
  enterprise-distribution channel for an autonomous coding agent:
  cloud-platform-marketplace integration (AWS Marketplace + Agent Toolkit
  for AWS), as opposed to the systems-integrator-resale model those two
  posts document. Flag that this is the first of the three to include a
  named, on-the-record customer testimonial (Echo Global Logistics) rather
  than only vendor-to-vendor narration, which should be weighted as a
  (still vendor-curated) step up in evidentiary strength relative to the
  Cognizant/Infosys posts, though still short of an independent case study.
- **Chapter 05 (Team Adoption), legacy-migration evidence**: Add the
  Mercedes-Benz (200K-line COBOL, 8 months → 8 days claimed) and unnamed
  automaker (25K-line COBOL, mainframe → Lambda, ~73% cost reduction)
  examples alongside the existing NAB (Assembly), Infosys (COBOL/JCP
  servlet), and PayPal (Java) legacy-migration data points. Explicitly flag
  that the Mercedes-Benz claim's verb is "analyze," not "migrate" or
  "replace" — the guide should not represent this as a completed migration
  without qualification, since the source itself does not claim the COBOL
  system was actually replaced or is now running on AWS.
- **Chapter 04 (Agentic Orchestration/Deployment) or wherever the guide
  covers enterprise deployment architecture**: Add Claim 7's single-tenant/
  dedicated-VPC/per-session-VM/audit-log-API deployment pattern as a named,
  vendor-published example of what "enterprise-grade" agent deployment
  architecture is currently marketed to look like, cross-referenced against
  the internal engineering account in
  `blog-cognition-what-we-learned-building-cloud-agents.md` Claim 3 for the
  underlying (microVM) isolation technology this product description does
  not itself name.
- Do NOT cite the Mercedes-Benz or automaker figures as independently
  verified outcomes — both are single vendor-reported numbers with no
  disclosed baseline methodology, consistent with how this corpus already
  treats the Infosys post's unquantified "record time" claim and the
  Cognizant post's zero-metric announcement.

## Extraction Notes

- A first-pass WebFetch of this URL produced a paraphrased, re-worded
  summary (e.g., converting the three-bullet workflow list into a
  condensed "Key Capabilities" section and rewording direct quotes) rather
  than verbatim text — the same small-model-summarization behavior already
  documented for Cognition's Next.js-rendered blog in
  `blog-cognition-infosys-partnership.md` Extraction Notes. To obtain
  verbatim text, the raw HTML was fetched directly via `curl` with a
  browser user-agent, stripped of script/style/markup with a Python script,
  and every quote used above was located and confirmed character-for-
  character in that stripped text before being copied into this note (per
  MINER.md §2a). The WebFetch paraphrase was discarded and is not quoted
  anywhere in this note.
- No sub-pages were followed. The stripped page's only other links are
  generic site navigation (Home, Careers, Research, Blog, Get a Demo,
  Devin) and legal/footer links (Terms of Use, Privacy Policy, etc.) — none
  met the MINER.md §1 "substantive linked page" criterion. The post does
  not link to any other Cognition blog posts, customer case-study pages, or
  the AWS Marketplace listing itself.
- Publish date (09.15.26, read as 2026-09-15 in the site's MM.DD.YY
  convention used elsewhere in this corpus, e.g. `blog-cognition-cognizant-partnership.md`'s
  "01.28.26" = 2026-01-28) was confirmed from the visible page byline text
  in the stripped HTML: "By The Cognition Team09.15.26".
- All cross-reference claim numbers cited from other source notes
  (`blog-cognition-what-we-learned-building-cloud-agents.md` Claim 3;
  `blog-cognition-one-year-of-building-together.md` Claim 8;
  `blog-cursor-nab-legacy-migration.md` Claim 6;
  `blog-cognition-doe-genesis-mission.md` Claim 4;
  `blog-cursor-paypal-enterprise-adoption.md` Claim 5;
  `blog-cognition-cognizant-partnership.md` Claim 6;
  `blog-cognition-infosys-partnership.md` Claim 6) were verified by
  re-reading each cited note's actual numbered claims before citing; none
  were guessed or approximated.
- No contradiction meeting the MINER.md §4a filing bar was identified.
  Claim 4's narrower "analyze" verb versus the headline framing of
  "modernization project" is a potential internal tension worth flagging in
  Guide Impact (see above), but it is an ambiguity in the vendor's own
  wording rather than a claim that materially opposes another source note's
  claim, so it does not meet the filing bar. No contradiction issue was
  filed.
- Overall confidence is set to `anecdotal`, matching this corpus's other
  Cognition partnership-announcement posts: every substantive claim here is
  either an unattributed vendor statement, a single vendor-curated quote,
  or a vendor-reported customer figure with no disclosed baseline
  methodology — the presence of three named spokespeople (an improvement in
  attribution over the Cognizant/Infosys posts) raises the post's
  rhetorical credibility but does not supply independent verification of
  any of its quantified claims.
