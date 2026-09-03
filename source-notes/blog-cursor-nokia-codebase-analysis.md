---
source_url: https://cursor.com/blog/nokia
source_type: blog-post
title: "Nokia analyzes 50M+ lines of code in two weeks with Cursor"
author: "Cursor Team (vendor case study; named practitioner: Kal De — SVP of Product and Engineering, Core Networks, Mobile Infrastructure Group at Nokia)"
date_published: 2026-09-02
date_extracted: 2026-09-03
last_checked: 2026-09-03
status: current
confidence_overall: emerging
issue: "#3190"
---

# Nokia Analyzes 50M+ Lines of Code in Two Weeks with Cursor

> A named-practitioner enterprise case study (Nokia's Core Network division, telecom infrastructure) documenting four Cursor deployments across the SDLC — a two-engineer 50M+-line architecture analysis that replaced a dozen-plus-specialist multi-month effort, a sub-week PRD-to-working-tool build automating 80% of a cross-team deployment workflow, a multi-agent parallel root-cause-analysis pipeline that compressed weeks of cross-team diagnosis into days, and an SDLC redesign extending into requirements gathering and PRD generation — with a forward-looking plan to use agents for automated network-element cataloguing.

## Source Context

- **Type**: blog-post (vendor case study published on Cursor's commercial blog, September 2, 2026; short — five sections, ~450 words, four attributed quotes all from a single named executive)
- **Author credibility**: One named Nokia executive, Kal De (SVP of Product and Engineering, Core Networks, Mobile Infrastructure Group), provides all four attributed quotes. Nokia is a major telecommunications/networking infrastructure company; the Core Network division's hybrid C/C++/Go multi-repository codebase is a credible domain for a 50M+-line scale claim. Published on Cursor's commercial blog — this is vendor marketing, and every quote in the piece is attributed to a single executive rather than the individual engineers who did the work. No independent validation, no named individual contributors (unlike the NAB and PayPal case studies, which quote multiple named engineers by role). Treat as practitioner evidence at emerging confidence for the specific project claims, anecdotal confidence for the single-executive framing statements.
- **Scope**: Covers four distinct Nokia use cases — (1) a 50M+-line codebase architecture analysis for decomposition planning, (2) a PRD-to-working-tool build automating a 5G deployment coordination workflow, (3) a multi-agent parallel root-cause-analysis pipeline for customer-impacting defects, and (4) SDLC redesign extending into requirements gathering, PRD generation, and architectural planning, plus a forward-looking network-element cataloguing plan. Does NOT cover: how the codebase-analysis project actually decomposed the architecture (only that it produced "an evidence-based plan"), which specific models were used for which tasks, team size beyond "two engineers" and "a Nokia engineer" (singular, for the second use case), the identity of the systems engineers running root-cause analysis, quantified success/accuracy rates for the multi-agent triage, or any cost/pricing detail.

## Extracted Claims

### Claim 1: Two Nokia engineers analyzed a 50M+ line, multi-language (C, C++, Go, and other languages) hybrid codebase spanning numerous repositories in two weeks using Cursor, without custom tooling, work the team estimates would otherwise have required a dozen or more specialists over several months

- **Evidence**: Named scale (50M+ lines), named team size (two engineers), named duration (two weeks), and a comparative estimate (a dozen or more experts, several months, with custom tooling) attributed to the Core Network team.
- **Confidence**: emerging (vendor-sourced; specific scale and duration given; the "dozen or more experts / several months" comparison is a retrospective team estimate, not a measured baseline from a prior attempt)
- **Quote**: "In one project, two engineers analyzed more than 50 million lines of code in two weeks – work that would have taken a dozen or more experts several months with custom tooling."
- **Our assessment**: This is a labor-reallocation claim rather than a pure velocity claim: the headline number is not "how much faster" but "how many fewer specialists were needed." That framing is distinct from PayPal's 4-6x Java-upgrade speedup (`blog-cursor-paypal-enterprise-adoption.md` Claim 5) and NAB's 3x BizCalc compression (`blog-cursor-nab-legacy-migration.md` Claim 5), which measure elapsed-time compression on a fixed team. The "without requiring custom tools" detail is notable for a hybrid C/C++/Go multi-repo codebase, where bespoke static-analysis tooling would traditionally be expected. No detail is given on what "analyzed" meant operationally (which agent modes, how findings were structured, or how the two engineers divided the work).

### Claim 2: The 50M+-line analysis produced an evidence-based architecture-decomposition plan identifying where changes would have the greatest impact on reliability and customer outcomes, giving Nokia insight into known historical challenges in the codebase

- **Evidence**: Named quote from Kal De describing the analytical output; article text describes the plan's purpose (decomposition, reliability/customer-outcome prioritization).
- **Confidence**: emerging (single named executive's characterization of the analysis output; no artifact from the plan itself is shown)
- **Quote**: "It gave us a very analytical, insightful view into our known historical challenges that we've had in the codebase."
- **Our assessment**: "Known historical challenges" implies Nokia already had tacit knowledge of problem areas in the codebase; the value claimed is not discovery of unknown issues but a systematic, evidence-based confirmation and prioritization of what engineers already suspected. This is a distinct value proposition from NAB's Assembly migration (`blog-cursor-nab-legacy-migration.md` Claim 6), where AI unblocked work that was previously not attempted at all due to expertise scarcity — here the codebase and its problems were already known to Nokia; AI compressed the effort to formalize that knowledge into an actionable plan.

### Claim 3: By completing the codebase analysis with only two engineers, the Core Network team estimates it freed up more than a dozen specialists over several months to focus on other projects

- **Evidence**: Direct restatement of the labor-reallocation outcome as an opportunity-cost claim, distinct from the project-completion claim in Claim 1.
- **Confidence**: anecdotal (self-reported estimate; no accounting of what the freed specialists' time was redirected to, or independent verification of the counterfactual staffing plan)
- **Quote**: "By completing the analysis with only two engineers, the Core Network team estimates it freed up more than a dozen specialists over several months, allowing them to focus on other projects."
- **Our assessment**: This reframes Claim 1's estimate as an internal capacity-planning outcome rather than a pure speed metric. For enterprise decision-makers evaluating AI tool ROI, "specialist-months freed for other projects" is a more organizationally legible unit than "X times faster," since it maps directly onto headcount allocation decisions. No corpus source so far frames an AI coding outcome explicitly in specialist-months-freed terms; this is the most literal "opportunity cost avoided" framing in the corpus to date.

### Claim 4: A single Nokia engineer used Cursor to go from problem statement to detailed PRD to a working project-management tool in under a week, automating and visualizing approximately 80% of a workflow that previously required coordination between 6–10 project managers and program managers across a multi-month deployment process

- **Evidence**: Named project (5G mobile core function deployment tooling), named timeline (less than a week), named prior process (multi-month, dozens of people), and a specific automation-coverage metric (approximately 80% of the workflow, 6–10 PMs/program managers coordinated previously).
- **Confidence**: emerging (specific metric and timeline given; single-engineer attribution; vendor-sourced; no detail on what the remaining ~20% of the workflow requires or how "automated and visualized" was measured)
- **Quote**: "To reduce complexity, a Nokia engineer used Cursor to go from problem statement to a detailed PRD to a working project-management tool, all in Cursor, in less than a week. The tool automated and visualized approximately 80% of a workflow that ordinarily would have required coordination between 6–10 project managers and program managers."
- **Our assessment**: This is the clearest single-practitioner "idea to internal tool" pipeline in the corpus that explicitly includes the requirements-authoring step (problem statement → PRD) as part of the compressed timeline, not just the build step. Compare with Faire's stacked-PR pattern (`blog-cursor-faire-cloud-agents.md` Claim 6: plan mode → five stacked PRs in two hours) — Faire's engineer authored the plan and handed it to a cloud agent for the build; here, a single Nokia engineer appears to have authored both the PRD and the tool within Cursor. The specific 80% coverage figure is a rare instance in the corpus of a bounded (not "eliminated entirely") automation claim — the source explicitly does not claim the coordination workflow was fully replaced.

### Claim 5: Nokia's own multi-month, multi-people deployment coordination process is characterized by Kal De as being "knocked off our seats" by a single engineer's unprompted tool-building initiative

- **Evidence**: Named quote from Kal De reacting to the PRD-to-tool project.
- **Confidence**: anecdotal (single executive's reaction quote; not an operational metric)
- **Quote**: "He identified a problem and then used Cursor to build a full-blown solution. He knocked us off our seats."
- **Our assessment**: The quote's framing — an individual contributor identifying and solving a coordination problem unprompted — is a bottom-up capability-enablement narrative distinct from top-down tool rollout narratives (like NAB's structured sprint-day enablement in `blog-cursor-nab-legacy-migration.md` Claim 4, or PayPal's seeded high-impact-team rollout in `blog-cursor-paypal-enterprise-adoption.md` Claim 1). It suggests that once a baseline tool is deployed, individual engineers can independently discover and execute high-value automation projects without being assigned to do so — an adoption dynamic not previously documented in the corpus in this specific "surprised leadership" framing.

### Claim 6: For root-cause analysis on customer-impacting defects, Nokia systems engineers load environment logs, past tickets, the codebase, and debugging traces into Cursor, where multiple agents run in parallel to flag potential hotspots and propose actionable triage steps — compressing a process that previously took weeks into days

- **Evidence**: Article describes the specific input context (logs, tickets, codebase, debugging traces) and the multi-agent parallel investigation mechanism; contrasts with the prior "semi-manual process" requiring "weeks of work and multiple meetings across teams."
- **Confidence**: emerging (specific mechanism described — multiple context sources, parallel agents, hotspot-flagging output; no quantified before/after time measurement beyond "weeks" to "days"; vendor-sourced)
- **Quote**: "With Cursor, systems engineers load environment logs, past tickets, the codebase, and debugging traces. Multiple agents run in parallel to flag potential hotspots and propose actionable triage steps, so engineers can act without waiting on cross-team coordination. What used to take weeks now takes days."
- **Our assessment**: This is the corpus's clearest telecom/infrastructure-domain instance of a multi-agent parallel-investigation architecture applied to production incident diagnosis, structurally analogous to Anthropic's own CI-incident triage system (`blog-anthropic-claude-oncall-cicd.md` Claim 9: an orchestration agent spins up executor subagents to investigate six connected systems in parallel, reducing MTTR). Both sources independently converge on the same architecture — parallel agents each investigating a different data source, feeding a synthesized triage output — for time-critical diagnostic work. The explicit "without waiting on cross-team coordination" framing identifies the mechanism of the speedup: the prior bottleneck was cross-team meeting overhead, not compute or analysis time per se, and parallel agents let one engineer's session substitute for what previously required several teams to convene.

### Claim 7: Nokia is extending Cursor into early-SDLC stages historically low on automation — requirements gathering, PRD generation, high-level design, and detailed architectural planning — with engineers selecting among multiple models based on the accuracy and token efficiency each task requires

- **Evidence**: Article text describes the SDLC stages Cursor now supports at Nokia and names task-based model selection as an operating practice.
- **Confidence**: emerging (vendor-described scope expansion; the model-selection claim is stated as current practice but with no specifics on which models or which task-to-model mappings are used)
- **Quote**: "Teams are using Cursor to support requirements gathering and to generate product requirements documents, accelerating creation of high-level designs and detailed architectural plans. Engineers can select among multiple models based on the accuracy and token efficiency each task requires."
- **Our assessment**: The task-based model-selection practice corroborates NAB's explicit model-flexibility evaluation criterion (`blog-cursor-nab-legacy-migration.md` Claim 2: "Cheaper models are used for routine, straightforward implementations...while more expensive thinking models are used for complex, long-running tasks like architecture design"). Nokia's framing adds "token efficiency" as an explicit second axis alongside accuracy — the first corpus instance naming token cost (not just capability) as a stated criterion for enterprise task-to-model routing. The extension into requirements gathering and PRD generation before any code is written is consistent with the "categorically new SDLC stage automated" pattern also seen in Claim 4 (the PRD-to-tool build).

### Claim 8: Nokia plans to use Cursor to automatically catalogue network elements and define how they are configured, connected, and governed by policy, to reduce manual work and speed the move of new capabilities into development

- **Evidence**: Forward-looking statement of Nokia's roadmap for extending Cursor use into requirements discovery for its telecommunications network infrastructure.
- **Confidence**: anecdotal (stated future intention, not a completed or in-progress deployment; no timeline given)
- **Quote**: "Looking ahead, the company plans to use Cursor to help discover requirements within the complex telecommunications networks it supports. By using Cursor to automatically catalogue network elements and define how they are configured, connected, and governed by policy, Nokia will be able to give its teams the context they need to reduce manual work and move new capabilities into development more efficiently."
- **Our assessment**: This is a context-engineering roadmap item specific to a physical/network-infrastructure domain — building a machine-generated context layer (a catalogue of network elements, their configuration, connectivity, and governing policy) that downstream development and requirements-discovery agents can draw on. It is structurally similar in intent to NAB's internal context engineering library, NAB CEL (`blog-cursor-nab-legacy-migration.md` Claim 3: centralizing institutional knowledge and enforcing standards via tool primitives), but applied to physical network topology and policy rather than codebase conventions. As a stated future plan rather than a completed deployment, this claim carries the lowest confidence in the note.

### Claim 9: Kal De frames Nokia's overall initiative as redesigning its entire software development lifecycle from inception to product delivery around Cursor, not as isolated point-tool adoption

- **Evidence**: Closing executive quote summarizing the cumulative scope of the four use cases described in the article.
- **Confidence**: anecdotal (single executive's summary framing, not an operational measurement)
- **Quote**: "We are redesigning our entire software development lifecycle from inception to product delivery and everything in between."
- **Our assessment**: This framing places Nokia alongside NAB and Amplitude as a third named enterprise stating an explicit full-SDLC redesign intent (`blog-cursor-nab-legacy-migration.md` Claim 10: "Re-thinking our engineering processes around agents is a key area of investment for NAB"; `blog-cursor-amplitude-autonomous-pipeline.md` Claim 9). Nokia's version is distinctive in stating that the redesign already spans "inception" (requirements/PRD, per Claim 7) through delivery (deployment tooling, per Claim 4) and operations (root-cause analysis, per Claim 6) — i.e., the claim describes current breadth across SDLC stages, not solely a forward roadmap like NAB's code-review/QA/deployment plan. This strengthens the corpus's cross-enterprise convergence on "SDLC redesign around agents" as a named strategic frame independently articulated by three different companies.

## Concrete Artifacts

### Four Nokia Cursor Deployments (summary table, article structure)

```
Nokia Cursor Deployments (Cursor blog, "Nokia analyzes 50M+ lines of code
in two weeks with Cursor," September 2, 2026)

1. LARGE-CODEBASE ARCHITECTURE ANALYSIS
   Scope:      50M+ lines, C/C++/Go, numerous repositories (Core Network division)
   Team:       2 engineers
   Duration:   2 weeks
   Baseline:   "a dozen or more experts several months with custom tooling"
   Output:     Evidence-based architecture-decomposition plan
                (prioritized by reliability / customer-outcome impact)

2. DEPLOYMENT-COORDINATION TOOL
   Prior process: Multi-month project, dozens of people, for new 5G mobile
                   core function deployment
   New process:   1 Nokia engineer, <1 week
                   Problem statement -> detailed PRD -> working
                   project-management tool, entirely in Cursor
   Coverage:      ~80% of a workflow that required coordinating
                   6-10 project/program managers

3. ROOT CAUSE ANALYSIS (customer-impacting defects)
   Prior process: Semi-manual; engineers dig through complex codebase with
                   limited trigger information; weeks of work, multiple
                   cross-team meetings
   New process:   Systems engineers load environment logs, past tickets,
                   codebase, and debugging traces; multiple agents run in
                   parallel to flag hotspots and propose triage steps
   Outcome:       Weeks -> days; engineers act without waiting on
                   cross-team coordination

4. EARLY-SDLC AUTOMATION
   Scope:      Requirements gathering, PRD generation, high-level design,
               detailed architectural plans
   Practice:   Engineers select among multiple models based on accuracy
               and token efficiency required per task

FORWARD ROADMAP:
   Automatically catalogue network elements (configuration, connectivity,
   governing policy) to give teams context that reduces manual work and
   speeds new capabilities into development
```

### Executive Quote Collection

```
Kal De, SVP of Product and Engineering, Core Networks,
Mobile Infrastructure Group — Nokia:

  On the codebase analysis: "It gave us a very analytical, insightful view
  into our known historical challenges that we've had in the codebase."

  On the deployment tool: "He identified a problem and then used Cursor to
  build a full-blown solution. He knocked us off our seats."

  On root cause analysis: "We can radically accelerate our root cause
  analysis, which directly impacts our ability to put a patch in place
  faster."

  On overall strategy: "We are redesigning our entire software development
  lifecycle from inception to product delivery and everything in between."
```

## Cross-References

- **Corroborates**:
  - `blog-anthropic-large-codebase-best-practices.md` Claim 1 ("Claude Code is running in production across multi-million-line monorepos, decades-old legacy systems, distributed architectures spanning dozens of repositories") — Nokia's 50M+-line, multi-language, multi-repository Core Network codebase (Claim 1 above) is a named practitioner instance of exactly this scale claim, independently reported for a competing tool (Cursor rather than Claude Code). This strengthens the corpus's evidence that multi-million-line production codebases are now a mainstream AI-coding-tool deployment target, not an edge case, across vendors.
  - `blog-anthropic-claude-oncall-cicd.md` Claim 9 ("an orchestration agent spins up executor subagents to investigate each of six connected systems in parallel, reducing MTTR") — Nokia's root-cause-analysis pattern (Claim 6 above: multiple agents run in parallel over logs, tickets, codebase, and traces to flag hotspots and propose triage steps) is structurally the same architecture — parallel per-source investigation feeding a synthesized diagnostic output — independently arrived at by Anthropic (for internal CI incidents) and Nokia (for customer-impacting network defects). Two different organizations, in different domains, converge on parallel multi-agent investigation as the mechanism for compressing incident diagnosis time.
  - `blog-cursor-nab-legacy-migration.md` Claim 2 ("Cheaper models are used for routine, straightforward implementations...while more expensive thinking models are used for complex, long-running tasks like architecture design") — Nokia's stated practice of engineers selecting among multiple models "based on the accuracy and token efficiency each task requires" (Claim 7 above) corroborates NAB's task-based model-routing criterion as an independent enterprise practice, adding "token efficiency" as an explicit named axis alongside accuracy.
  - `blog-cursor-faire-cloud-agents.md` Claim 13 ("Cursor's value comes from great context management and getting useful proprietary information across the company and codebase") — Nokia's root-cause-analysis workflow, which aggregates environment logs, past tickets, the codebase, and debugging traces as agent context (Claim 6 above), is a concrete practitioner instance of proprietary-context aggregation as the source of agent value, in a different domain (network/telecom operations rather than e-commerce engineering).

- **Extends**:
  - `blog-cursor-nab-legacy-migration.md` Claim 10 ("Re-thinking our engineering processes around agents is a key area of investment for NAB") and `blog-cursor-amplitude-autonomous-pipeline.md` Claim 9 (near-term roadmap including CI/CD and deployment automation) — Nokia's closing framing (Claim 9 above: "redesigning our entire software development lifecycle from inception to product delivery and everything in between") is a third named enterprise independently articulating full-SDLC redesign as strategic intent. Nokia's version is distinctive in describing current breadth (requirements/PRD through deployment tooling through root-cause diagnosis) rather than only a forward roadmap, extending the corpus's evidence that this is an achieved state at some enterprises, not solely an aspiration.
  - `blog-cursor-nab-legacy-migration.md` Claim 3 (NAB CEL: internal context engineering library centralizing institutional knowledge on tool primitives) — Nokia's forward plan to automatically catalogue network elements, their configuration, connectivity, and governing policy (Claim 8 above) extends the "build a machine-generated context layer for the tool to draw on" pattern into a physical-infrastructure/telecom domain, distinct from NAB's codebase-convention-focused library.

- **Contradicts**: None found. No existing corpus source note makes a claim that materially opposes any claim extracted here.

- **Novel**:
  - **Specialist-months-freed framing** (Claims 1 and 3): No prior corpus source frames an AI coding outcome explicitly as "X specialist-months freed for other projects" rather than as a velocity multiplier or elapsed-time compression. This is a more organizationally legible ROI unit for enterprise capacity planning than the corpus's typical "Nx faster" metrics.
  - **PRD-authorship-included "idea to tool" pipeline in under a week** (Claim 4): While Faire's stacked-PR pattern (`blog-cursor-faire-cloud-agents.md` Claim 6) covers plan-to-build compression, no prior corpus source documents a single engineer taking a project from unwritten problem statement through PRD authorship to a working internal tool within the same compressed timeframe.
  - **Multi-agent parallel root-cause analysis for customer-impacting network defects** (Claim 6): The specific combination of inputs (environment logs, ticket history, codebase, debugging traces) and the "flag hotspots, propose triage steps" output framing, in a telecom/network-infrastructure incident context, is new to the corpus — the closest analog (`blog-anthropic-claude-oncall-cicd.md`) is an internal CI/CD incident-response system, not a customer-facing network defect diagnosis workflow.
  - **Token efficiency as a named model-selection axis** (Claim 7): NAB names accuracy/task-complexity as the model-selection criterion; Nokia is the first corpus source to explicitly name token efficiency alongside accuracy as a stated selection criterion.
  - **Automated network-element cataloguing as a context-engineering roadmap item** (Claim 8): No prior corpus source documents a plan to auto-generate a context layer describing physical network topology, configuration, and governing policy for a telecommunications infrastructure domain.

## Guide Impact

- **Chapter 02 (Harness Engineering) — Large-codebase agent deployment**: Add Nokia's 50M+-line, two-engineer, two-week analysis (Claim 1) as a fourth named enterprise-scale evidence point alongside NAB's BizCalc/Assembly migrations and PayPal's 3,000-app Java upgrade, but note the framing difference: Nokia's headline metric is labor reallocation (specialist-months freed), not elapsed-time compression on a fixed team. The guide's large-codebase section should present both framings as valid ways enterprises measure AI-coding-tool ROI.

- **Chapter 02 (Harness Engineering) — Multi-agent coordination for diagnosis/triage**: Add Nokia's root-cause-analysis architecture (Claim 6: parallel per-source-agent investigation → synthesized hotspot/triage output) alongside Anthropic's own CI on-call system (`blog-anthropic-claude-oncall-cicd.md` Claim 9) as a second independent instance of the orchestrator/parallel-investigator pattern applied to time-critical diagnosis. This strengthens a "parallel multi-agent investigation" pattern as reusable guidance, now evidenced across two organizations and two incident domains (CI/CD failures vs. customer-impacting network defects).

- **Chapter 03/04 (Context Engineering) — SDLC-stage context aggregation**: Add Nokia's root-cause-analysis input set (environment logs, ticket history, codebase, debugging traces loaded together, Claim 6) as a concrete named example of "aggregate proprietary context sources for the agent" — corroborating and giving a domain-specific instance of Faire's context-management-as-value-driver claim (`blog-cursor-faire-cloud-agents.md` Claim 13).

- **Chapter 05 (Team Adoption) — SDLC redesign framing**: Add Nokia's closing quote (Claim 9) as a third named-enterprise data point (with NAB and Amplitude) for the "redesign the SDLC around agents, don't bolt AI onto existing processes" strategic framing. Distinct from NAB and Amplitude, Nokia's quote describes achieved breadth across SDLC stages rather than only forward roadmap — useful as an example of what the end-state of that redesign looks like in practice.

- **Chapter 05 (Team Adoption) — Model routing practice**: Add Nokia's task-based model-selection practice (Claim 7, "accuracy and token efficiency") as a second corroborating data point for NAB's model-flexibility evaluation criterion (`blog-cursor-nab-legacy-migration.md` Claim 2), with token efficiency named as an explicit additional axis worth including in any guide checklist for enterprise model-routing policy.

## Extraction Notes

- Source is short vendor marketing copy (~450 words, five sections) published on Cursor's commercial blog. All four attributed quotes come from a single named executive (Kal De); no individual contributor engineers are named or quoted directly, which is a lower attribution density than the NAB and PayPal case studies in the corpus (both of which quote multiple named practitioners by role). Treat all quantitative and comparative claims as vendor-sourced and unverified by any third party.
- The article is a single, self-contained page with no linked sub-pages to follow.
- All quotes in this note were verified against the raw HTML of the source page (fetched via `curl`) in addition to a WebFetch verbatim-text request; the same wording appeared identically in both extraction methods (the raw HTML embeds the article text multiple times for hydration), which gives high confidence the quotes are character-for-character accurate.
- No contradictions with existing corpus source notes were found. All claims are additive or corroborating.
- The "50 million lines of code" and "two weeks" figures are the headline metric but the source gives no detail on what specific Cursor modes or workflows the two engineers used to perform the analysis, nor any artifact from the resulting decomposition plan — this is a gap relative to, e.g., the NAB case study's mode-level detail (Ask Mode, Plan Mode named explicitly for the BizCalc project).
