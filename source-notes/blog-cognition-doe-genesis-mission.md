---
source_url: https://cognition.com/blog/cognition-doe-genesis-mission
source_type: blog-post
title: "Cognition Signs MOU with U.S. Department of Energy to Join The Genesis Mission"
author: The Cognition Team
date_published: 2026-07-22
date_extracted: 2026-08-02
last_checked: 2026-08-02
status: current
confidence_overall: emerging
issue: "#2421"
---

# Cognition Signs MOU with U.S. Department of Energy to Join The Genesis Mission

> Cognition announces a signed MOU with the U.S. Department of Energy to join
> the Genesis Mission — a national AI-for-science initiative launched by
> executive order — naming four contribution areas (security remediation,
> legacy scientific code modernization, workforce-capacity offload, cloud
> modernization), disclosing specific FedRAMP/ITAR/IL4-IL6 compliance status,
> and naming the U.S. Army, U.S. Navy, and NASA JPL as existing Devin users.

## Source Context

- **Type**: blog-post (Cognition's own blog, cognition.com, published
  2026-07-22, byline "By The Cognition Team," no individual author named —
  confirmed via the page's `article:published_time` meta tag
  `2026-07-22T10:00:00-07:00`). A short partnership/announcement post (~450
  words), not a technical article or case study.
- **Author credibility**: First-party vendor announcement from Cognition, the
  company that builds and sells Devin. This matches the unattributed
  corporate-narration pattern of Cognition's other partnership posts
  (`blog-cognition-infosys-partnership.md`, `blog-cognition-cognizant-partnership.md`)
  — no individual spokesperson, DOE official, or named lab representative is
  quoted anywhere in the piece, and no DOE or national-laboratory source
  corroborates the MOU independently in this extraction. Unlike those two
  purely qualitative SI-partnership posts, this one names specific,
  checkable facts (a FedRAMP authorization tier, three named federal
  engineering-team customers, a named OPM program) rather than only
  qualitative "material gains" language.
- **Scope**: Covers the fact of the signed MOU, brief background on the
  Genesis Mission itself (executive order date, scale, stated goal), the
  four areas Cognition says it will contribute in, current FedRAMP/ITAR/IL
  compliance status for the Cognition platform and for Devin Desktop/CLI
  specifically, three named existing federal engineering-team users plus one
  named OPM partnership, a paragraph on the security angle (Devin Security
  Swarm, CISA's AI-era vulnerability remediation guidance), and Cognition's
  stated in-kind offer (free security scans/reports for national labs, free
  compute for Genesis Mission RFA-selected teams). Does **not** cover: any
  dollar value or contract terms of the MOU, a timeline for when Genesis
  Mission projects will actually start using Devin, any named individual at
  DOE or a national laboratory, any delivered outcome or pilot result under
  the MOU (the piece is explicitly forward-looking — "as the mission's first
  projects stand up"), or technical detail on how Devin Security Swarm's
  vulnerability validation actually works beyond the one-sentence description
  given.

## Extracted Claims

### Claim 1: Cognition has signed an MOU with the U.S. Department of Energy to join the Genesis Mission, which the post describes as a national initiative characterized as "America's Manhattan Project for AI"
- **Evidence**: Opening two sentences of the post, stating the MOU as an
  already-completed action ("has signed"), not a pending or planned one.
- **Confidence**: settled (a first-party statement that a specific legal/
  administrative action — signing an MOU — has already occurred, as distinct
  from a forward-looking marketing pitch)
- **Quote**: "Cognition has signed a memorandum of understanding (MOU) with the U.S. Department of Energy (DOE) to join the Genesis Mission, a national initiative described as \"America's Manhattan Project for AI.\""
- **Our assessment**: This is a concrete, falsifiable claim (an MOU either
  exists or it does not) rather than a marketing aspiration — a materially
  stronger evidentiary starting point than the pre-event webinar pitch in
  `blog-cognition-devin-federal-security-swarm.md`, which described a product
  ahead of an unheld demo. This Miner did not independently verify the MOU's
  existence against a DOE or Genesis Mission primary source; the "Manhattan
  Project for AI" framing is presented as a description of how the Genesis
  Mission is characterized generally, not a quote attributed to a specific
  DOE official.

### Claim 2: The Genesis Mission was launched by executive order in November 2025 and mobilizes America's 17 national laboratories, along with industry and academia, to connect the country's most powerful supercomputers with its largest collection of federal scientific datasets
- **Evidence**: Second paragraph, presented as background/context on the
  mission Cognition is joining.
- **Confidence**: emerging (a specific, checkable factual claim about a
  named executive order and a named number of laboratories — this Miner did
  not independently fetch the executive order text or a DOE primary source to
  verify the November 2025 date or the "17 national laboratories" count)
- **Quote**: "Launched by executive order in November 2025, the Genesis Mission mobilizes America's 17 national laboratories, along with industry and academia, to connect the world's most powerful supercomputers with the largest collection of federal scientific datasets."
- **Our assessment**: This is background context rather than a claim about
  Cognition's own product or performance, but it is specific enough
  (a named month/year, a named lab count) to be independently checked against
  a primary government source — worth flagging as a verification target for
  a future Miner pass, consistent with how `blog-cognition-devin-federal-security-swarm.md`
  flagged its own unverified "Gold Eagle Initiative" naming (see
  Cross-References).

### Claim 3: The Genesis Mission's stated goal is doubling the productivity of American science within a decade, and Cognition frames this goal as depending on software — research workflows, data pipelines, simulation codes, and the platforms connecting them — which is the stated rationale for Devin's relevance to the mission
- **Evidence**: Opening sentence of the "How Cognition will support the
  mission" section, presented as the mission's own goal followed by
  Cognition's software-dependency argument for its own relevance.
- **Confidence**: anecdotal (the "doubling... within a decade" goal is
  presented as fact but not sourced to a specific DOE document in this post;
  the software-dependency argument is Cognition's own framing for why an
  AI coding agent is relevant to a science-productivity mission, not an
  independently corroborated claim)
- **Quote**: "The Genesis Mission's goal — doubling the productivity of American science within a decade — depends on software: research workflows, data pipelines, simulation codes, and the platforms that connect them."
- **Our assessment**: This is the post's core relevance argument (science
  productivity depends on software, therefore an AI software engineer is
  relevant to a science-productivity mission) — a reasonable but
  self-serving framing from a vendor whose product is exactly the thing being
  argued as necessary. No independent evidence is given that software
  specifically (as opposed to compute, data access, or scientific staffing)
  is the primary bottleneck to the stated productivity goal.

### Claim 4: Cognition states it will contribute to the Genesis Mission in four areas: software and data security (finding/remediating vulnerabilities in scientific codebases built on aging open-source components), modernizing legacy scientific code (documenting, testing, and translating decades-old Fortran/C++/COBOL as the researchers who wrote it retire), expanding scientific workforce capacity (offloading data-pipeline/model-infrastructure/deployment engineering so researchers can focus on science), and cloud modernization (migrating legacy applications and infrastructure to modern cloud-native platforms)
- **Evidence**: A four-item bulleted list under "How Cognition will support
  the mission," each item with a one-sentence elaboration.
- **Confidence**: anecdotal (a stated intent/scope of contribution, not a
  description of work already delivered — no named project, laboratory, or
  codebase is given for any of the four areas)
- **Quote**: "Software and data security. Helping find and remediate vulnerabilities across scientific codebases, many of which depend on aging, open-source components. Modernizing legacy scientific code. Supporting the documentation, testing, and translation of decades-old codebases — Fortran, C++, COBOL — to help preserve institutional knowledge as the researchers who wrote it retire. Expanding scientific workforce capacity. Giving researchers a way to offload engineering work — data pipelines, model infrastructure, deployment — so they can spend more time on the science itself. Cloud modernization. Helping migrate legacy applications and infrastructure to modern, cloud-native platforms."
- **Our assessment**: The "preserve institutional knowledge as the
  researchers who wrote it retire" framing for legacy scientific code
  (Fortran/C++/COBOL) is a specific, notable variant of the retiring-expert
  legacy-migration rationale documented elsewhere in this corpus for
  enterprise/financial legacy code (see Cross-References → Corroborates) —
  here applied to scientific/research codebases rather than banking or
  insurance systems. None of the four areas is backed by a named example,
  project, or laboratory in this post; they read as a stated scope of intent
  rather than a report of delivered work.

### Claim 5: As of this post, the Cognition platform is FedRAMP Class D (High) In Process and listed in the FedRAMP Marketplace, while Devin Desktop and CLI are already FedRAMP Class D (High) Authorized and compliant for ITAR and DoW IL4–IL6 workloads
- **Evidence**: Direct compliance-status statement, immediately following the
  four contribution areas.
- **Confidence**: emerging (a specific, checkable compliance-status claim
  with named authorization tiers; independently corroborated by a companion
  Cognition post — see Extraction Notes — but not independently verified
  against the FedRAMP Marketplace listing itself by this Miner)
- **Quote**: "The Cognition platform is FedRAMP Class D (High) In Process and listed in the FedRAMP Marketplace; Devin Desktop and CLI are already FedRAMP Class D (High) Authorized and compliant for ITAR and IL4–IL6 workloads."
- **Our assessment**: This draws a specific distinction between two
  compliance states — the full "Cognition platform" (In Process, not yet
  Authorized) versus "Devin Desktop and CLI" specifically (already
  Authorized) — which is a more granular disclosure than most vendor
  compliance claims in this corpus. Note that "FedRAMP Class D (High)" is
  Cognition's own terminology; standard FedRAMP nomenclature categorizes
  authorizations by impact level (Low/Moderate/High) rather than by lettered
  "class," so this phrasing should be treated as Cognition's internal naming
  convention rather than assumed to map directly onto official FedRAMP
  program vocabulary without further check. This is the corpus's most
  specific compliance-status disclosure yet for Cognition/Devin specifically
  (contrast with `blog-anthropic-claude-code-cowork-government.md`, which
  documents Anthropic's FedRAMP High authorization for a different product).

### Claim 6: Engineering teams at the U.S. Army, U.S. Navy, and NASA's Jet Propulsion Laboratory use Devin today, and Cognition is a partner in the U.S. Office of Personnel Management's Tech Force
- **Evidence**: Direct statement, same sentence group as Claim 5's compliance
  disclosure.
- **Confidence**: anecdotal (three named federal engineering organizations
  and one named OPM program, stated as present-tense fact with no
  description of deployment scale, use case, or duration at any of the four
  — this Miner did not independently confirm usage with the Army, Navy, JPL,
  or OPM)
- **Quote**: "Engineering teams at the U.S. Army, U.S. Navy, and NASA's Jet Propulsion Laboratory use Devin today, and Cognition is a partner in the U.S. Office of Personnel Management's Tech Force."
- **Our assessment**: This is the first corpus source naming Army, Navy, and
  JPL specifically as existing Devin users, and the first naming OPM's "Tech
  Force" as a named partnership — a broader and more specific set of named
  federal customers than the general "engineering teams at the U.S. Army,
  U.S. Navy, and NASA's Jet Propulsion Laboratory" framing gives any
  individual customer's scale or scope. Should be cited only as evidence
  that these relationships exist and are named by Cognition, not as evidence
  of deployment size or outcome, consistent with how this corpus already
  treats similarly unquantified named-customer claims (see Cross-References).

### Claim 7: Cognition frames the mission's combined supercomputer/experimental-facility/federal-scientific-data platform as "an attack surface of national consequence," built on software depending on thousands of open-source libraries and often predating modern security practice
- **Evidence**: Opening sentence of the "A focus on software security"
  section.
- **Confidence**: anecdotal (a framing/problem-statement claim with no
  supporting data point — no count of libraries, no age statistic for the
  software in question, no named vulnerability or incident)
- **Quote**: "The mission's integrated discovery platform will connect supercomputers, experimental facilities, and decades of federal scientific data — an attack surface of national consequence, built on software that depends on thousands of open-source libraries and often predates modern security practice."
- **Our assessment**: This is diagnostic problem-framing preceding the
  Devin Security Swarm pitch in Claim 8, similar in rhetorical structure to
  the "traditional tooling cannot keep up" framing in
  `blog-cognition-devin-federal-security-swarm.md` Claim 4 — an unsourced
  vendor characterization of scale/risk that sets up the following
  capability claim, not an independently evidenced security assessment of
  the Genesis Mission's actual codebases.

### Claim 8: Devin Security Swarm is described as built to find vulnerabilities across large codebases, verify whether they're actually exploitable in a safe sandbox, and open remediation pull requests for engineers to review and approve — framed as supporting the security posture the Genesis Mission and CISA's guidance on AI-era vulnerability remediation call for
- **Evidence**: Direct capability description, immediately following the
  attack-surface framing in Claim 7.
- **Confidence**: anecdotal (a vendor's own product description with no
  named benchmark, customer, or delivered example in this post specifically
  — no data point beyond the mechanism description itself)
- **Quote**: "This is an area Cognition has invested in directly: Devin Security Swarm is built to find vulnerabilities across large codebases, verify whether they're actually exploitable in a safe sandbox, and open remediation pull requests for engineers to review and approve, aiming to support the kind of security posture this mission and CISA's guidance on AI-era vulnerability remediation call for."
- **Our assessment**: This three-step mechanism description (find → verify
  exploitability in sandbox → open remediation PR) is consistent with, but
  worded differently from, the "tracing data flows, validating what's
  actually exploitable at runtime, and shipping reviewed remediation PRs"
  description in `blog-cognition-devin-federal-security-swarm.md` Claim 1 —
  the two posts converge on the same three-stage architecture (detect,
  verify exploitability, remediate) using different phrasing, which
  strengthens confidence that this is Cognition's settled product
  description for Devin Security Swarm rather than a one-off framing for a
  single audience. Neither post gives a metric in its own body text (see
  Extraction Notes for a companion Cognition post that does).

### Claim 9: As part of its Genesis Mission consortium membership, Cognition has offered in-kind code security scans and remediation reports for national laboratory codebases, along with complimentary compute for teams selected under Genesis Mission Requests for Applications (RFAs)
- **Evidence**: Direct statement of Cognition's stated in-kind contribution,
  closing the "A focus on software security" section.
- **Confidence**: anecdotal (a stated offer/commitment, not a report of
  scans or compute already delivered — no count of labs served, scans run,
  or RFA teams that have received compute)
- **Quote**: "As part of our consortium membership, Cognition has offered in-kind code security scans and remediation reports for national laboratory codebases, along with complimentary compute for teams selected under Genesis Mission Requests for Applications (RFAs)."
- **Our assessment**: "Consortium membership" is a specific structural detail
  — it implies the Genesis Mission has a formal consortium structure with
  named member organizations, of which Cognition is one, rather than a
  simple bilateral MOU relationship. This is the clearest concrete, in-kind
  commitment in the post (specific goods offered: scans, reports, compute)
  even though no quantity or delivery timeline is attached to any of the
  three offered items.

### Claim 10: The MOU is explicitly framed as creating "a framework" for future collaboration rather than describing delivered work — Cognition states it will work with DOE, the national laboratories, and Genesis Mission awardee teams "as the mission's first projects stand up," and directs interested agencies/laboratories/teams to devin.ai/government or a named contact email
- **Evidence**: The "What comes next" closing section.
- **Confidence**: settled (an explicit first-party statement about the
  MOU's present scope and stage — the post itself states its own claims are
  forward-looking, which is a directly checkable characterization of the
  post's own content)
- **Quote**: "The MOU creates a framework for Cognition to work with DOE, the national laboratories, and Genesis Mission awardee teams as the mission's first projects stand up... Agencies, laboratories, and Genesis Mission teams can learn more at devin.ai/government or reach us at public.sector@cognition.ai."
- **Our assessment**: This is the post's own explicit admission that no
  Genesis Mission project has yet started using Devin — "as the mission's
  first projects stand up" is future tense. This should govern how every
  other claim in this note is read: Claims 4, 6-9 describe intent, existing
  general-purpose federal usage (Army/Navy/JPL, which predates and is
  independent of the Genesis Mission MOU specifically), and offered
  in-kind resources — not delivered Genesis-Mission-specific outcomes. No
  claim in this post should be cited as evidence of a completed or in-progress
  Genesis Mission deployment.

## Concrete Artifacts

```
Full article structure (headings, in order), source: cognition.com/blog/
cognition-doe-genesis-mission, "By The Cognition Team," 07.22.26:

1. (intro, unheaded) — MOU announcement + Genesis Mission background
2. How Cognition will support the mission
   - four-item bulleted list (security, legacy modernization, workforce
     capacity, cloud modernization)
   - FedRAMP/ITAR/IL4-IL6 compliance status
   - named federal users (Army, Navy, JPL) + OPM Tech Force partnership
3. A focus on software security
   - attack-surface framing
   - Devin Security Swarm mechanism description
   - in-kind consortium contribution (scans, reports, compute)
4. What comes next
   - MOU framework language
   - contact: devin.ai/government, public.sector@cognition.ai
```

```
Compliance status, verbatim (from "How Cognition will support the mission"):

"The Cognition platform is FedRAMP Class D (High) In Process and listed in
the FedRAMP Marketplace; Devin Desktop and CLI are already FedRAMP Class D
(High) Authorized and compliant for ITAR and IL4–IL6 workloads."

Named federal users, verbatim:

"Engineering teams at the U.S. Army, U.S. Navy, and NASA's Jet Propulsion
Laboratory use Devin today, and Cognition is a partner in the U.S. Office of
Personnel Management's Tech Force."
```

## Cross-References

- **Corroborates**:
  - `blog-cognition-devin-federal-security-swarm.md` Claim 1 (Devin Security
    Swarm's parallel agents "reason across an entire codebase like a
    security engineer: tracing data flows, validating what's actually
    exploitable at runtime, and shipping reviewed remediation PRs") — this
    note's Claim 8 independently describes the same product with a
    differently-worded but architecturally consistent three-step mechanism
    (find vulnerabilities → verify exploitability in a sandbox → open
    remediation PRs), from a different Cognition post two-plus weeks later
    (2026-07-22 vs. the federal-security-swarm event page's 2026-08-01
    extraction date for an 2026-08-07 event). Two independently-worded
    Cognition descriptions of the same product converging on the same
    three-stage architecture strengthens confidence that this is Cognition's
    settled internal description of the product, though neither post
    supplies an independent benchmark within its own text (see Extraction
    Notes for where such a benchmark figure does appear, in a third,
    not-yet-mined Cognition post).
  - `blog-anthropic-claude-code-cowork-government.md` Claim 1 (Claude Code
    and Claude Cowork delivered through a FedRAMP High authorized
    environment, "built on the same application our commercial customers
    use") — this note's Claim 5 (Devin Desktop/CLI already FedRAMP Class D
    (High) Authorized, platform-wide authorization In Process) is a second,
    independent frontier-AI-coding-vendor data point for the same broader
    2026 pattern of AI coding/agent products pursuing FedRAMP High
    authorization for federal deployment, though the two posts use different
    internal terminology for the authorization tier ("FedRAMP High
    authorized environment" for Anthropic vs. "FedRAMP Class D (High)" for
    Cognition) and this note has not independently reconciled whether "Class
    D" is Cognition-specific internal shorthand for the same official FedRAMP
    High impact level Anthropic's post describes in standard terms.
  - `blog-openai-government-national-security-partnerships.md` Claim 3
    (OpenAI disclosing an existing, named Department of War contract with
    specific contractual restrictions, "announced earlier this year") — this
    note's Claim 1 (a signed, named DOE MOU) is a third major AI vendor
    (alongside Anthropic and OpenAI) formalizing a named, specific federal
    government partnership within the same several-month window in 2026,
    though the Cognition MOU is science/civilian-agency-focused (DOE,
    national laboratories) rather than national-security/military-focused
    like the OpenAI and Anthropic sources, and unlike OpenAI's post, this
    Cognition post discloses no restriction, prohibited-use list, or
    governance principle attached to the partnership.
  - `blog-cognition-infosys-partnership.md` Claim 5 (Infosys and Cognition
    "developing engineering frameworks and enablement programs designed for
    large, regulated enterprises") — this note's Claim 9 (in-kind consortium
    contributions: security scans, remediation reports, complimentary
    compute for Genesis Mission RFA-selected teams) is a second instance of
    Cognition offering supporting infrastructure/resources beyond the core
    Devin product itself as part of a large institutional partnership,
    though the Infosys framework is enterprise-regulatory-focused while this
    Genesis Mission offer is specifically scoped to national-laboratory
    security scanning and RFA-team compute.

- **Contradicts**: None identified. No existing corpus source makes a claim
  about Cognition's FedRAMP status, named federal customers, or Devin
  Security Swarm's mechanism that opposes what this post states; the
  three-stage Devin Security Swarm description in this post and in
  `blog-cognition-devin-federal-security-swarm.md` are worded differently
  but architecturally consistent (see Corroborates above), not conflicting.
  No contradiction issue filed.

- **Extends**: `blog-cognition-devin-federal-security-swarm.md`, which
  documented a pre-event webinar pitching Devin Security Swarm for BOD 26-04/
  Gold Eagle compliance and a named "Cognition Federal" go-to-market team,
  but with zero named federal customer and no FedRAMP/compliance-status
  disclosure. This note extends that coverage with three named federal
  engineering-team customers (Army, Navy, JPL), a named OPM partnership
  (Tech Force), and a specific FedRAMP/ITAR/IL4–IL6 compliance-status
  disclosure — filling in exactly the customer-evidence and compliance-status
  gaps that note's Extraction Notes and Guide Impact sections flagged as
  missing from the federal-security-swarm event page.

- **Novel**: The Genesis Mission itself (a named national AI-for-science
  initiative, launched by executive order in November 2025, mobilizing 17
  national laboratories) is new to this corpus — no prior source note
  documents it. The specific "FedRAMP Class D (High)" compliance-tier naming
  for Cognition/Devin, the named Army/Navy/JPL federal engineering-team
  customers, the named OPM "Tech Force" partnership, and the "consortium
  membership" structural detail (implying the Genesis Mission has named
  member organizations) are all first appearances in this corpus.

## Guide Impact

- **Chapter 05 (Team Adoption) or a future Enterprise/Government Deployment
  chapter**: Add this source's named federal customers (Claim 6: Army, Navy,
  JPL, OPM Tech Force) and FedRAMP/ITAR/IL4-IL6 compliance status (Claim 5)
  as a citable data point that Cognition/Devin has reached specific,
  named-tier federal compliance authorization and named federal engineering
  customers, distinct from — and complementary to — Anthropic's FedRAMP High
  Claude for Government posture (`blog-anthropic-claude-code-cowork-government.md`).
  Flag that "FedRAMP Class D (High)" is Cognition's own terminology, not
  independently reconciled against standard FedRAMP impact-level naming in
  this note.
- **Chapter 06 (Security & Threat Model)**: This post's Devin Security Swarm
  description (Claim 8) should be cited only as a second, independently
  worded corroboration of the mechanism already described in
  `blog-cognition-devin-federal-security-swarm.md` Claim 1 — it adds no new
  metric or benchmark of its own. Do not cite this post as the source for
  any quantified Devin Security Swarm performance figure; none appears in
  its text (see Extraction Notes for where one does appear, in an unmined
  companion post).
- **Do not cite this source as evidence of a delivered or in-progress
  Genesis Mission outcome**: per Claim 10, the post's own language ("as the
  mission's first projects stand up") states that no Genesis Mission project
  has yet begun using Devin as of publication. Any guide reference to this
  source should be scoped to "Cognition has signed an MOU and named intended
  contribution areas," not "Cognition is delivering results under the
  Genesis Mission."
- **Chapter 05, legacy-code-migration evidence**: Claim 4's framing of
  legacy scientific code (Fortran/C++/COBOL) modernization as preserving
  "institutional knowledge as the researchers who wrote it retire" is a
  scientific-domain variant of the retiring-expert rationale this corpus
  already documents for enterprise/financial legacy migration (see
  `blog-cognition-infosys-partnership.md` Claim 3, COBOL/JCP servlet
  migrations). Worth noting as a second domain (federal science vs.
  financial services) making the same expertise-scarcity argument for AI-
  assisted legacy migration, though — like the Infosys claim — this one is
  entirely qualitative with no percentage, timeline, or delivered example.

## Extraction Notes

- **Fetch method**: An initial WebFetch pass against
  `https://cognition.com/blog/cognition-doe-genesis-mission` returned what
  appeared to be the full article text. To verify per MINER.md §2a, this
  Miner additionally fetched the raw page HTML directly via `curl` with a
  browser user-agent, stripped script/style/markup with a Python script, and
  confirmed the resulting plain text was character-for-character identical
  to the WebFetch output (both texts match verbatim, including the exact
  section headings "How Cognition will support the mission," "A focus on
  software security," and "What comes next"). All `Quote` fields above are
  drawn from, and confirmed against, this raw-HTML extraction. Publish date
  (2026-07-22) was independently confirmed via the page's
  `article:published_time` and `datePublished` meta values
  (`2026-07-22T10:00:00-07:00`), not inferred from the visible "07.22.26"
  byline alone.
- **Sub-pages followed**: The article links to two other Cognition blog
  posts — `/blog/devin-fedramp-high-in-process` and
  `/blog/introducing-devin-security-swarm` — plus `devin.ai/government` (a
  landing page, not fetched, and a `mailto:` contact link). Both linked blog
  posts were fetched via WebFetch (not raw-HTML-verified, since no `Quote`
  from either is used in this note) to check for consistency: the FedRAMP
  post corroborates this post's Claim 5 compliance status and additionally
  names Anduril as a federal/defense customer (not mentioned in this post);
  the Security Swarm post corroborates this post's Claim 8 mechanism
  description and additionally reports a quantified benchmark (72% recall
  at $90.23/run on a 50-vulnerability benchmark, versus named competitors
  at 26-68% recall). Neither linked post has its own source note in this
  corpus yet (checked via directory listing before writing this note) —
  flagging both as candidate future Miner targets, particularly the Security
  Swarm post, since it is the only place this Miner found an actual
  quantified performance figure for a product otherwise described only in
  qualitative terms across this note and
  `blog-cognition-devin-federal-security-swarm.md`.
- **Source is short**: Consistent with the Prospector's triage note, this is
  a ~450-word announcement post, not a long-form technical article. Ten
  claims were extracted, each anchored to a distinct sentence or clause in
  the post; this is within MINER.md's "5-15 claims" guideline for a
  content-rich source, though on the lower end given the source's brevity —
  every substantive sentence in the post is represented by at least one
  claim above.
- **Cross-references verified before writing**: re-read
  `blog-cognition-devin-federal-security-swarm.md` in full and confirmed
  Claim 1 and Claim 4 by number and content; re-read
  `blog-anthropic-claude-code-cowork-government.md` in full and confirmed
  Claim 1 by number and content; re-read
  `blog-openai-government-national-security-partnerships.md` in full and
  confirmed Claim 3 by number and content; re-read
  `blog-cognition-infosys-partnership.md` in full and confirmed Claim 3 and
  Claim 5 by number and content. No claim number was guessed or
  approximated.
- **No contradiction meeting the MINER.md §4a filing bar was identified** —
  see Cross-References → Contradicts. No contradiction issue was filed.
- **Confidence rated `emerging` overall**: this is a first-party vendor
  announcement of a real, specific legal action (a signed MOU) with several
  independently-nameable, checkable facts (FedRAMP tier, named federal
  customers, a named OPM program, a named executive-order date) — stronger
  evidentiary footing than a pure marketing pitch — but the substantive
  content describing what Cognition will actually *do* under the MOU
  (Claim 4's four contribution areas, Claim 9's in-kind offers) is entirely
  forward-looking intent with zero delivered example, project, or metric,
  and the post's own language (Claim 10) explicitly frames itself as
  pre-project-start. This mix of checkable-but-unverified factual claims and
  entirely prospective substantive claims places this source between the
  `anecdotal` rating given to Cognition's purely qualitative SI-partnership
  posts and the `settled` rating reserved for sources with independently
  reproducible or third-party-corroborated results.
