---
source_url: https://cognition.com/blog/devin-is-getting-a-windows-pc
source_type: blog-post
title: "Devin is Getting a Windows PC"
author: The Cognition Team
date_published: 2026-05-21
date_extracted: 2026-07-18
last_checked: 2026-07-18
status: current
confidence_overall: anecdotal
issue: "#2002"
---

# Devin is Getting a Windows PC

> Cognition's short product-announcement post: Devin now builds, runs, and
> tests natively inside its own Windows VM (not just generating code that a
> human must later build/test on Windows), with a named highlight capability
> — .NET Framework to .NET Core migration, previously blocked because
> Framework only runs on Windows — plus Windows-application computer-use
> testing, SQL Server/Windows Service support, and enterprise security
> parity with Devin's existing Linux offering. In beta, gated to Enterprise
> Cloud and Dedicated Deployment customers only.

## Source Context

- **Type**: blog-post (Cognition's own blog, cognition.com, published
  05.21.26 per the page's byline, i.e. 2026-05-21; byline "By The Cognition
  Team," no individual author named)
- **Author credibility**: First-party product-announcement post from the
  vendor that builds and sells Devin. No named individual author, no named
  customer quote (Citi and Mercedes-Benz are named only as existing Devin
  users in a general sentence about the product, not as sources of a
  testimonial), and no metric of any kind (no adoption number, no speed
  figure, no success-rate percentage) appears anywhere in the post. This is
  the same thin evidentiary shape as `blog-cognition-devin-in-windsurf.md`
  and `blog-cognition-cognizant-partnership.md` — a short, unattributed
  vendor announcement rather than a practitioner account.
- **Scope**: Covers what the Windows capability is (native build/run/test in
  a Windows VM), one named highlighted use case (.NET Framework → .NET Core
  migration), two additional named use cases (computer-use testing of
  Windows applications; SQL Server and Windows-native workflow support),
  the security/governance posture for the Windows offering, and the
  beta/access gating. Does **not** cover: any metric (adoption, session
  count, migration success rate, time saved), any named customer quote or
  case study specific to the Windows capability, technical detail on how
  the Windows VM is provisioned or isolated, what changes (if any) in
  Devin's underlying model or orchestration for Windows vs. Linux sessions,
  pricing, or a firm GA date beyond "beta." The post is short (~350 words
  of body text) and entirely first-party.

## Extracted Claims

### Claim 1: Devin now builds, runs, and tests natively inside its own Windows VM, rather than only generating code that a human must separately build and test on Windows
- **Evidence**: Opening statement immediately following a framing sentence
  about Windows's device footprint, presented as the post's single core
  announcement.
- **Confidence**: emerging (first-party capability-launch statement for a
  concrete, describable execution environment — "its own Windows VM" — with
  no metric, but the underlying architectural claim, native VM execution
  rather than code generation alone, is specific and falsifiable)
- **Quote**: "Windows runs on over 1.4 billion devices and is deployed everywhere from Fortune 500 companies to the living rooms of indie developers. Devin now builds, runs, and tests natively in its own Windows VM."
- **Our assessment**: The load-bearing distinction is "builds, runs, and
  tests natively," not just "writes Windows-targeted code." This matters
  because it is exactly the gap Claim 6 below names explicitly: Devin could
  already generate .NET Framework migration code, but without a Windows
  execution environment it could not build or test that code itself. This
  claim is the general capability; Claim 6 is the specific, previously-
  blocked use case it unblocks.

### Claim 2: Cognition names Citi and Mercedes-Benz as existing enterprise customers already using Devin — across industries — for migrations, test writing, new feature development, and codebase hardening, running many tasks at once to multiply engineering capacity
- **Evidence**: Second paragraph, general product-positioning statement
  naming two customers by name before introducing the Windows-specific
  announcement.
- **Confidence**: anecdotal (two named enterprise customers, but the
  sentence is a general product claim about existing usage, not a
  Windows-specific testimonial or case study — no quote is attributed to
  either company, and no metric backs the "already use Devin" claim)
- **Quote**: "Devin is an AI software engineer that plans, builds, tests, and ships code autonomously, on its own machine in the cloud. Engineering teams across industries, including Citi and Mercedes-Benz, already use Devin to complete migrations, write tests, build new features, and harden their codebases - running many tasks at once to multiply their engineering capacity."
- **Our assessment**: This sentence is not evidence that Citi or
  Mercedes-Benz use Devin *on Windows* specifically — it is general
  context establishing Devin's existing customer base before the Windows
  announcement. Mercedes is independently named as a Devin customer in
  `blog-cognition-hilsil-triage-test-generation.md` Claim 1, for a
  different, more specific workflow (HIL/SIL automotive test triage) — see
  Cross-References. This is the first appearance of Citi by name anywhere
  in this corpus's Cognition coverage.

### Claim 3: Windows-native support is framed as extending the general benefits of cloud AI agents — task delegation, parallel execution, and autonomous iteration — specifically to Windows applications
- **Evidence**: Direct framing statement connecting the general cloud-agent
  value proposition to the new Windows-specific execution target.
- **Confidence**: anecdotal (a one-sentence framing claim with no
  Windows-specific evidence of parallel execution or autonomous iteration
  actually being used on a Windows codebase — those properties are
  asserted by extension from Devin's general cloud-agent design, not
  demonstrated in this post for the Windows case specifically)
- **Quote**: "Devin can now operate natively in a Windows environment, bringing the full power of autonomous AI engineering to the world's most mature developer ecosystem. The benefits of cloud AI agents - task delegation, parallel execution, and autonomous iteration - now apply to Windows applications."
- **Our assessment**: "The world's most mature developer ecosystem" is
  vendor framing for Windows's install base and enterprise legacy-code
  density, not a technical claim. The substantive content is the assertion
  that Devin's already-documented cloud-agent properties (parallel
  execution is documented at the "10 to 20 Devins in parallel" scale in
  `blog-cognition-verifying-agentic-development.md` Claim 3, for Linux/
  general cloud sessions) now extend to Windows targets — but this post
  supplies no Windows-specific instance of parallel execution, only the
  general assertion that it applies.

### Claim 4: A demo video shows Devin building a new feature in a .NET Framework application, then migrating that application to .NET Core, building and testing throughout in an actual Windows environment
- **Evidence**: Direct description of an embedded demo video, naming both
  the starting framework (.NET Framework) and the target (.NET Core) and
  specifying that building/testing happens "in an actual Windows
  environment."
- **Confidence**: anecdotal (a described video demo, not independently
  viewable/verifiable from the extracted text, and no outcome data such as
  test-pass rate or duration is given for what the video shows)
- **Quote**: "Watch Devin build a new feature in a .NET Framework app. Then, Devin migrates the app to .NET Core - building and testing in an actual Windows environment."
- **Our assessment**: This is the concrete worked example behind the
  general .NET Framework → .NET Core capability claim (Claim 6). Note that
  the video reportedly shows two distinct actions in sequence — feature
  addition *then* migration — not a migration-only demo, suggesting the
  intended narrative is "Devin can do ordinary Windows feature work and
  legacy-framework migration with the same native execution capability,"
  not migration exclusively.

### Claim 5: Devin can build and test new features on, and modernize, Windows codebases containing pre-existing legacy technology that predates the current engineering team — specifically naming VB apps, classic ASP, and Windows Forms
- **Evidence**: Direct statement under the "Map, Build and Modernize
  Windows Applications" section heading, naming three specific legacy
  Windows technologies.
- **Confidence**: anecdotal (a general capability claim naming specific
  legacy tech stacks by name, but with no worked example, customer
  reference, or outcome metric for any of the three named technologies)
- **Quote**: "Every enterprise that runs on Windows has code that predates the current team - VB apps, classic ASP, Windows Forms. Devin can now build and test new features on Windows codebases. Devin can also modernize Windows applications - iterating and testing its work autonomously."
- **Our assessment**: Naming VB, classic ASP, and Windows Forms specifically
  is a concrete, checkable scope statement about which legacy Windows
  stacks the announcement targets — these are three distinct, decades-old
  Microsoft application models, not a vague "legacy code" gesture. No
  claim is made about COBOL, mainframe, or non-Microsoft legacy stacks,
  distinguishing this source's legacy-migration scope from
  `blog-cursor-nab-legacy-migration.md`'s Assembly-mainframe case (a
  different legacy category entirely — see Cross-References).

### Claim 6: Devin could already generate .NET Framework-to-.NET Core migration code, but previously could not build or test that code because .NET Framework only runs on Windows — Devin now builds, runs tests, and iterates in a real Windows environment until the migration passes
- **Evidence**: Direct before/after statement under the "Highlight: Migrate
  .NET Framework to .NET Core" subheading, explicitly naming the prior
  limitation (no Windows execution environment) and the specific technical
  reason for it (.NET Framework is Windows-only).
- **Confidence**: emerging (the most specific, falsifiable claim in the
  post — it names a concrete prior gap with a stated technical cause, not
  just an improvement in the abstract, though "until the migration passes"
  is not backed by any success-rate, iteration-count, or duration figure)
- **Quote**: "Devin could generate migration code for .NET Framework, but couldn't build or test it because .NET Framework only runs on Windows. Devin now builds, runs tests, and iterates in a real Windows environment until the migration passes."
- **Our assessment**: This is the single most citable claim in the source:
  it names the *mechanism* of the prior limitation (build/test capability
  gated on OS availability, not a model capability gap) rather than
  asserting only that migrations are now "better" or "faster." "Iterates
  in a real Windows environment until the migration passes" is consistent
  with the general Anthropic-documented migration methodology in
  `blog-anthropic-code-migration-playbook.md` (translate → compile → run →
  match-behavior, repeated until passing), but this post gives none of
  that methodology's disclosed detail (no test-pass percentage, no
  iteration count, no verification-judge description) — see
  Cross-References → Extends.

### Claim 7: Devin can test Windows applications using computer use — building and launching the application and clicking through its UI directly to verify behavior — for behavior that can only be verified by actually running the application
- **Evidence**: Direct capability statement under the "Test Windows
  Applications with Computer Use" subheading, naming the specific
  mechanism (build, launch, click through UI) and the stated rationale
  (some behavior is only verifiable by running the app).
- **Confidence**: anecdotal (a general capability statement with no worked
  example specific to a Windows application, no named failure mode, and no
  outcome data — contrast with the substantially more detailed, mechanism-
  level computer-use testing account in
  `blog-cognition-verifying-agentic-development.md`, which is not
  Windows-specific)
- **Quote**: "Some behavior can only be verified by actually running the application. Devin can build and launch Windows applications and interact directly, clicking through the UI to verify behavior is as expected."
- **Our assessment**: This is an extension of Devin's already-documented
  computer-use self-testing capability (test-plan generation, in-session
  annotation, "hard edges" around timing and JS-shortcut "cheating" — all
  detailed in `blog-cognition-verifying-agentic-development.md`) to a new
  execution target: native Windows desktop/GUI applications rather than
  the browser-based web applications that source's examples imply. This
  post gives none of that source's implementation depth (no annotation
  mechanism, no test-report structure, no named failure modes) for the
  Windows case specifically — it should be read as "the same class of
  capability now also applies to Windows apps," not as new technique
  detail.

### Claim 8: Devin works natively inside Windows Server environments to refactor, migrate, and validate end-to-end SQL Server and Windows-native workflows such as stored procedures and Windows Services
- **Evidence**: Direct capability statement under the "Run SQL Server and
  Windows-Native Workflows" subheading, naming two specific Windows-native
  workflow types (stored procedures, Windows Services).
- **Confidence**: anecdotal (a general capability claim naming two specific
  workflow types, with no worked example, customer reference, or outcome
  data for either)
- **Quote**: "Stored procedures, Windows Services, etc. all run on Windows Server. Devin works inside that environment natively to refactor, migrate, and validate these workflows end to end."
- **Our assessment**: This is the third and least-elaborated of the three
  named Windows use cases (alongside .NET Framework migration and
  computer-use UI testing) — it names a specific class of
  server-side/backend Windows workload (stored procedures, Windows
  Services) distinct from the desktop/GUI-application framing of Claim 7,
  but supplies no detail on how "refactor, migrate, and validate end to
  end" is actually performed for database or service-level workflows
  versus application code.

### Claim 9: Devin on Windows carries the same enterprise security and governance controls as Devin on Linux — isolated VM sessions, no customer code used for training, SOC 2 Type II and ISO 27001 compliance, and SSO/RBAC support
- **Evidence**: Direct statement under the "Security and governance"
  heading, explicitly naming the Linux offering as the parity baseline and
  listing four specific controls.
- **Confidence**: settled (a specific, named compliance and architecture
  claim — SOC 2 Type II and ISO 27001 are externally auditable
  certifications, not vague assurances — though this note cannot verify
  the certifications' current validity independently, and no scope
  statement clarifies whether the Windows offering is covered under the
  same certification as the Linux offering or a separate one)
- **Quote**: "Devin on Windows carries the same enterprise security and governance controls as Devin on Linux. Sessions run on isolated VMs, and no customer code is used for training. We are SOC 2 Type II and ISO 27001 compliant, with SSO and RBAC support."
- **Our assessment**: "Isolated VMs" as the session-isolation architecture
  is consistent with the same pattern already documented for a different
  vendor's cloud coding agent in `blog-cursor-ios-mobile-app.md` Claim 6
  ("Cloud agents run in isolated VMs with full development environments")
  and `blog-cursor-faire-cloud-agents.md` — see Cross-References. The
  SOC 2 Type II / ISO 27001 pairing matches the same compliance floor
  already documented for other AI vendors in
  `blog-anthropic-kepler-verifiable-ai-financial.md` and
  `blog-anthropic-legal-industry-deploy.md`, suggesting this pairing is
  becoming a standard enterprise-trust baseline claim across the AI coding
  and AI agent vendor landscape, not a differentiator specific to
  Cognition or to Windows.

### Claim 10: Devin for Windows is in beta and available only to Enterprise Cloud and Dedicated Deployment customers, requiring contact with Cognition to access it — not a self-serve or general-availability launch
- **Evidence**: Direct statement under the "Getting started" heading,
  naming the two eligible customer tiers and the access mechanism (contact
  form).
- **Confidence**: settled (a specific, unambiguous statement of current
  access restrictions — this is the kind of claim that is either true or
  false at time of publication, not a qualitative or aspirational
  statement)
- **Quote**: "Devin for Windows is in beta, available now for Enterprise Cloud and Dedicated Deployment customers. Contact us here to try it out."
- **Our assessment**: This is an access-gating detail the guide should
  carry alongside any citation of the Windows capability: it is not
  available to Devin's standard/self-serve tier, only to two named
  enterprise deployment tiers, and requires direct contact with Cognition
  rather than an in-product toggle. This tempers Claims 1, 6, 7, and 8 —
  the capabilities described are real and shipped, but access-limited, at
  time of publication (2026-05-21).

## Concrete Artifacts

### Full article body text, verbatim, in section order
```
Source: cognition.com/blog/devin-is-getting-a-windows-pc, "By The Cognition
Team," 05.21.26 (fetched via raw HTML, HTML entities decoded, tags
stripped)

[Intro, unheaded]
"Windows runs on over 1.4 billion devices and is deployed everywhere from
Fortune 500 companies to the living rooms of indie developers. Devin now
builds, runs, and tests natively in its own Windows VM.

Devin is an AI software engineer that plans, builds, tests, and ships code
autonomously, on its own machine in the cloud. Engineering teams across
industries, including Citi and Mercedes-Benz, already use Devin to complete
migrations, write tests, build new features, and harden their codebases -
running many tasks at once to multiply their engineering capacity.

Devin can now operate natively in a Windows environment, bringing the full
power of autonomous AI engineering to the world's most mature developer
ecosystem. The benefits of cloud AI agents - task delegation, parallel
execution, and autonomous iteration - now apply to Windows applications.

Watch Devin build a new feature in a .NET Framework app. Then, Devin
migrates the app to .NET Core - building and testing in an actual Windows
environment."

[Map, Build and Modernize Windows Applications]
"Every enterprise that runs on Windows has code that predates the current
team - VB apps, classic ASP, Windows Forms. Devin can now build and test
new features on Windows codebases. Devin can also modernize Windows
applications - iterating and testing its work autonomously.

Highlight: Migrate .NET Framework to .NET Core
Devin could generate migration code for .NET Framework, but couldn't build
or test it because .NET Framework only runs on Windows. Devin now builds,
runs tests, and iterates in a real Windows environment until the migration
passes."

[Test Windows Applications with Computer Use]
"Some behavior can only be verified by actually running the application.
Devin can build and launch Windows applications and interact directly,
clicking through the UI to verify behavior is as expected."

[Run SQL Server and Windows-Native Workflows]
"Stored procedures, Windows Services, etc. all run on Windows Server. Devin
works inside that environment natively to refactor, migrate, and validate
these workflows end to end."

[Security and governance]
"Devin on Windows carries the same enterprise security and governance
controls as Devin on Linux. Sessions run on isolated VMs, and no customer
code is used for training. We are SOC 2 Type II and ISO 27001 compliant,
with SSO and RBAC support."

[Getting started]
"Devin for Windows is in beta, available now for Enterprise Cloud and
Dedicated Deployment customers. Contact us here to try it out."
```

### Section structure (headings, in order)
```
Source: cognition.com/blog/devin-is-getting-a-windows-pc

1. (intro, unheaded)
2. Map, Build and Modernize Windows Applications
   - Highlight: Migrate .NET Framework to .NET Core
3. Test Windows Applications with Computer Use
4. Run SQL Server and Windows-Native Workflows
5. Security and governance
6. Getting started
```

### In-body outbound links (excluding site nav/footer/related-articles)
```
Source: raw HTML anchor extraction, cognition.com/blog/devin-is-getting-a-windows-pc

"Contact us here" -> https://cognition.ai/contact?dcid=5f13f404-e9b2-4344-830e-9514fe5bfa01#company
```

## Cross-References

- **Corroborates**:
  - `blog-cognition-devin-in-windsurf.md` Claim 2 (Devin defined as a cloud
    agent that "runs in its own infrastructure and in its own environment"
    and independently opens PRs, runs tests, and QAs its own work) — this
    source's Claim 1 (Devin "builds, runs, and tests natively in its own
    Windows VM") is the same general cloud-agent architecture extended to a
    second, named operating-system target; both sources describe the same
    underlying "own machine/environment" execution model, one for the
    general case and this one for Windows specifically.
  - `blog-cognition-verifying-agentic-development.md` Claim 2 ("Devin will
    spin up the app, click through it, and confirm its changes actually
    work, the same way an engineer would") — this source's Claim 7
    (building and launching Windows applications, clicking through the UI
    to verify behavior) is the same computer-use self-testing mechanism
    applied to a new execution target (native Windows GUI/desktop
    applications) rather than the browser-based applications implied by
    that source's examples. This source adds no new mechanism detail (no
    annotation, no test-report structure, no named failure modes) beyond
    what that source already documents in depth.
  - `blog-cognition-hilsil-triage-test-generation.md` Claim 1 (Cognition
    names Mercedes as a customer using Devin for automotive HIL/SIL
    workflows) — this source's Claim 2 independently names "Mercedes-Benz"
    as an existing Devin customer in a general product-positioning
    sentence. The two sources corroborate that Mercedes (or Mercedes-Benz)
    is a real, named, recurring Devin customer across at least two
    separate Cognition posts, though for different workflows (HIL/SIL test
    triage there vs. an unspecified general "migrations, tests, features,
    hardening" list here) — this source gives no detail connecting the two
    mentions to the same team or project.
  - `blog-cursor-ios-mobile-app.md` Claim 6 ("Cloud agents run in isolated
    VMs with full development environments and can iterate toward
    merge-ready PRs without human intervention") and
    `blog-cursor-faire-cloud-agents.md` (each Swarm agent "runs in its own
    isolated VM on Cursor's infrastructure") — this source's Claim 9
    ("Sessions run on isolated VMs") names the identical session-isolation
    architecture from a second, independent cloud-coding-agent vendor
    (Cognition vs. Cursor), reinforcing that per-session VM isolation is a
    now-standard architectural baseline across at least two vendors in
    this corpus, not a Cognition-specific design choice.
  - `blog-anthropic-kepler-verifiable-ai-financial.md` (SOC 2 Type II
    achieved, ISO 27001 underway) and `blog-anthropic-legal-industry-deploy.md`
    (ISO/IEC 42001:2023 and SOC 2 Type II named as the compliance baseline)
    — this source's Claim 9 (SOC 2 Type II and ISO 27001 compliance, named
    as already achieved rather than "underway") corroborates that this
    specific certification pairing is becoming a recurring enterprise-trust
    baseline claim across independent AI vendors in this corpus, though
    this source's phrasing does not disclose whether ISO 27001 is fully
    certified or in progress the way the Kepler source explicitly
    distinguishes "achieved" from "underway."

- **Contradicts**: None identified. No claim in this source conflicts with
  an existing source note's claim under matching conditions.

- **Extends**:
  - `blog-anthropic-code-migration-playbook.md` (Anthropic's generalized
    six-step migration methodology — rulebook/dependency-map/gap-inventory,
    stress-test, translate, compile, run, match-behavior — validated
    against two named case studies with disclosed test-pass rates and
    iteration detail) — this source's Claim 6 (.NET Framework → .NET Core:
    "Devin now builds, runs tests, and iterates in a real Windows
    environment until the migration passes") describes the same
    translate-build-test-iterate-until-passing shape at a much shallower
    evidentiary depth: no test-pass percentage, no iteration count, no
    verification-judge description, and no named practitioner. Read
    together, the Anthropic source supplies the methodology-level detail
    this Cognition post's headline claim lacks, though the two sources
    describe different vendors' different products (Claude Code vs.
    Devin) and this source does not claim to use the same methodology.
  - `blog-cursor-nab-legacy-migration.md` Claim 6 (Assembly mainframe
    migration at NAB — previously "categorically impossible" due to
    expertise scarcity, unblocked by AI-generated flowcharts and business
    summaries) — this source's Claim 5 (naming VB apps, classic ASP, and
    Windows Forms as legacy Windows technology "that predates the current
    team") describes the same general legacy-modernization problem shape
    (code written in a technology the current team lacks expertise in or
    tooling for) applied to a different, Windows-specific legacy stack.
    Unlike the NAB source, this source gives no named practitioner, no
    "couldn't even think about attempting this" viability claim, and no
    velocity or completion-time figure — it names the target technologies
    but not a specific project outcome.
  - `blog-cognition-cognizant-partnership.md` Claim 4 (Cognizant plans to
    extend Devin/Windsurf rollout to client engineering teams in
    healthcare, financial services, and insurance) — this source's Claim 2
    names Citi (financial services) as an existing Devin customer,
    consistent with financial services being a named target industry
    elsewhere in Cognition's enterprise-customer messaging, though this
    source does not mention Cognizant, insurance, or healthcare, and the
    two posts describe independent customer relationships (direct
    enterprise customer here vs. a systems-integrator partnership there).

- **Novel**: Windows-native VM execution as a distinct, named cloud-agent
  target environment is new to this corpus — prior Cognition and Cursor
  cloud-agent sources in this corpus describe Linux-based cloud VMs
  (implicitly, via dev-server and container framing) without naming
  Windows as a supported execution target. The specific .NET Framework →
  .NET Core capability-gap narrative (Claim 6: code generation was already
  possible, but build/test was blocked purely by OS availability, not by a
  model capability gap) is a new and specific instance of "environment
  access, not model capability, was the limiting factor" that this corpus
  has not previously documented for a migration use case. The three named
  legacy Windows technologies (VB apps, classic ASP, Windows Forms —
  Claim 5) and the SQL Server/Windows Services workflow claim (Claim 8)
  are also new to this corpus's legacy-modernization coverage, which
  previously centered on Assembly mainframe (`blog-cursor-nab-legacy-migration.md`)
  and Python/Zig-family migrations (`blog-anthropic-code-migration-playbook.md`).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: If the guide discusses cloud-agent
  execution environments (what a cloud coding agent actually runs on), add
  Claim 1 and Claim 9 (native Windows VM execution, with the same
  isolated-VM session architecture and no-training-on-customer-code policy
  already documented for Linux) as a concrete instance of a vendor
  expanding a cloud agent's supported execution environment beyond Linux —
  citing this source alongside the general cloud-agent architecture
  already documented in `blog-cognition-devin-in-windsurf.md`. Flag that
  this is a beta feature gated to two named enterprise deployment tiers
  (Claim 10), not a generally available capability.

- **Chapter 05 (Team Adoption) / legacy modernization coverage**: Add
  Claim 6 (the .NET Framework → .NET Core capability-gap narrative: code
  generation was already possible, but build/test was blocked by OS
  availability alone) as a specific, named example of environment access
  — not model capability — being the limiting factor for a legacy
  migration use case. Pair with `blog-cursor-nab-legacy-migration.md`
  Claim 6's Assembly-mainframe expertise-gap-bridging pattern as a second,
  differently-shaped legacy-modernization value category (missing
  execution environment vs. missing human expertise), and with
  `blog-anthropic-code-migration-playbook.md`'s six-step methodology for
  readers wanting more rigorous migration-process detail than this source
  provides. Explicitly flag that this source gives no test-pass rate,
  iteration count, or named practitioner outcome for the .NET migration
  claim — it should be cited as a described capability, not a validated
  case study.

- **Chapter 03 (Verification)**: If the guide's computer-use-testing
  coverage is extended to non-browser targets, add Claim 7 (Devin building,
  launching, and clicking through native Windows applications to verify
  behavior) as a named instance of computer-use self-verification applied
  to desktop/GUI applications, distinct from the browser-based examples in
  `blog-cognition-verifying-agentic-development.md`. Flag that this source
  supplies no mechanism detail (no annotation step, no test-report
  structure, no named failure modes) for the Windows case — cite the
  verifying-agentic-development note for implementation depth and this
  source only for the claim that the target surface now includes native
  Windows apps.

- **Chapter 06 (Security & Threat Model)**: If the guide maintains a list
  of recurring enterprise-trust baseline claims across AI coding-agent
  vendors, add Claim 9 (isolated VM sessions, no customer-code training,
  SOC 2 Type II, ISO 27001, SSO, RBAC) as a third data point alongside
  `blog-anthropic-kepler-verifiable-ai-financial.md` and
  `blog-anthropic-legal-industry-deploy.md`, showing this specific
  compliance/architecture bundle recurring across at least two independent
  AI vendor categories (coding agents and general-purpose AI platforms).

## Extraction Notes

- WebFetch's default summarizing pass on this URL declined to reproduce
  verbatim text at all, citing an internal "125-character maximum" quote
  constraint that directly conflicted with the request to reproduce the
  article in full — it returned only a short paraphrase instead (see the
  first WebFetch attempt in this session). This is a more severe version
  of the same verbatim-extraction difficulty already documented in several
  other Cognition source notes in this corpus (e.g.
  `blog-cognition-devin-in-windsurf.md`, `blog-cognition-devin-desktop.md`
  Extraction Notes). To obtain and verify verbatim text, the raw HTML was
  fetched directly via `curl` with a browser user-agent, HTML entities were
  decoded and markup stripped with a Python script, and every quote used
  above was copied character-for-character from that stripped, decoded
  text — not from any WebFetch summarizer output. The full article body
  text is reproduced verbatim in Concrete Artifacts for independent
  verification.
- The article's publish date (05.21.26, i.e. 2026-05-21) was read directly
  from the page's visible byline in the extracted text (line immediately
  following "By The Cognition Team").
- All in-body anchor links were extracted from the raw HTML via regex and
  reviewed; the only substantive in-body link is the "Contact us here" CTA
  pointing to Cognition's contact form. The "04. Articles" block listing
  nine other Cognition blog posts (including `blog-cognition-devin-desktop.md`'s
  and `blog-cognition-devin-productivity-estimation.md`'s primary sources)
  is a site-wide related-articles navigation footer, not an inline link
  within the article body, so per MINER.md §1 it was not treated as a
  linked page to follow — none of those nine listed posts are referenced
  or linked from within the article's actual body text.
- Cross-references verified before writing: re-read
  `blog-cognition-devin-in-windsurf.md` in full and confirmed Claim 2 by
  number and content; re-read `blog-cognition-verifying-agentic-development.md`
  in full and confirmed Claim 2 by number and content; re-read
  `blog-cognition-hilsil-triage-test-generation.md` in full and confirmed
  Claim 1 by number and content; re-read `blog-cursor-ios-mobile-app.md`
  in full and confirmed Claim 6 by number and content; re-read
  `blog-cursor-nab-legacy-migration.md` in full and confirmed Claim 6 by
  number and content; re-read `blog-cognition-cognizant-partnership.md`
  in full and confirmed Claim 4 by number and content; re-read
  `blog-anthropic-code-migration-playbook.md` Source Context and Claim 1-2
  region and confirmed its six-step methodology and case-study framing.
  `blog-cursor-faire-cloud-agents.md`, `blog-anthropic-kepler-verifiable-ai-financial.md`,
  and `blog-anthropic-legal-industry-deploy.md` were checked via grep for
  the specific "isolated VM" / "SOC 2" / "ISO 27001" phrasing cited above,
  confirming the quoted phrasing appears in each at the cited location; no
  claim number was guessed or approximated.
- No contradiction meeting the MINER.md §4a filing bar was identified —
  see Cross-References → Contradicts. No contradiction issue filed.
- Confidence is rated `anecdotal` overall, one tier below the `emerging`
  rating given to the related `blog-cognition-devin-in-windsurf.md` and
  `blog-cognition-devin-desktop.md` notes: like those sources, this is a
  short, first-party, unattributed announcement post with zero metrics —
  but unlike `blog-cognition-devin-desktop.md` (which carries five named,
  attributed customer testimonials) this source's only customer mentions
  (Citi, Mercedes-Benz) are unattributed, unquoted, and not specific to the
  Windows capability being announced. The two claims with the strongest
  evidentiary grounding (Claim 6's specific before/after technical
  limitation, and Claim 9's named, externally-auditable compliance
  certifications) are individually rated higher (emerging and settled,
  respectively) within the note.
