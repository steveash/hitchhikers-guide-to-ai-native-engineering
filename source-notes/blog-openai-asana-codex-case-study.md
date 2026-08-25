---
source_url: https://openai.com/index/asana
source_type: blog-post
title: "Asana cleared 5 years of engineering work in 2 weeks with Codex"
author: OpenAI (customer case study, featuring Amritansh Raghav, Chief Technology Officer, Asana)
date_published: 2026-08-18
date_extracted: 2026-08-25
last_checked: 2026-08-25
status: current
confidence_overall: anecdotal
issue: "#2938"
---

# Asana cleared 5 years of engineering work in 2 weeks with Codex

> An OpenAI customer case study describing how Asana used up to four parallel
> Codex agents, launched from a single five-sentence prompt and checked twice
> daily by one engineer, to remove an unmaintained testing framework (Enzyme)
> in about two calendar weeks — work Asana had estimated would take at least
> five years and roughly $6M in staffing, versus the ~$12K the agent-driven
> effort actually cost in model and infrastructure spend.

## Source Context

- **Type**: blog-post (OpenAI customer case study, `openai.com/index/asana`, published August 18, 2026; ~400 words — shorter than the comparable Notion case study). Structured identically to other OpenAI customer-story posts: a company metadata block (Company size: Enterprise, Region: North America, Industry: Technology, Products: Codex, API), a two-stat headline block, a single named-executive pull quote, and a short narrative body. Not a technical or engineering blog post.
- **Author credibility**: Written and published by OpenAI, not Asana, as promotional customer-success content — OpenAI has a direct commercial incentive to present Codex favorably. The only named individual is Amritansh Raghav, Chief Technology Officer of Asana, who supplies one quote. No engineer who actually ran the migration is named or quoted, no methodology is given for the "~$6 million" staffing estimate, and no independent party verifies the $12K cost figure or the "5 years" counterfactual.
- **Scope**: Covers one specific migration (removing the Enzyme testing framework from Asana's frontend stack), the workflow used (up to four parallel Codex agents from a single prompt, twice-daily human review), a cost comparison, and one hedged executive quote about generalizability. Does NOT cover: the actual prompt text, the size of the affected codebase, what "review and approve" concretely involved (code review? test verification? both?), how the $6M staffing estimate was derived, whether any regressions or rework followed the migration, or any account from the engineer(s) who ran it.

## Extracted Claims

### Claim 1: Asana used Codex to complete a project in about two calendar weeks that the company had estimated would otherwise take at least five years
- **Evidence**: Headline stat block and opening sentence of the case study.
- **Confidence**: anecdotal (a single vendor-selected project at a single company; "five years" is described as an "estimate" for a "previous staffing plan," not a project that was ever actually attempted and measured over five years)
- **Quote**: "In about two weeks, Asana completed work it expected to take five years."
- **Our assessment**: The ratio (years-long estimate compressed to two weeks) is a striking headline number, but — as with the Notion case study's "2 Weeks → 3 hours" framing — the counterfactual side of the ratio (five years) is an estimate for a staffing plan that was never executed, not a measured baseline. Treat this as "a single unmaintained-dependency-removal project shipped in two weeks," with the "five years" figure carrying much lower evidentiary weight than the "two weeks" figure, since only one side of the comparison actually happened.

### Claim 2: The migration's model and infrastructure costs came to about $12,000, compared with Asana's roughly $6 million estimate for the staffing plan it replaced
- **Evidence**: Headline stat block ("$12K — Model and infrastructure cost versus Asana's ~$6M staffing estimate") and restated in the body text.
- **Confidence**: anecdotal (self-reported by OpenAI/Asana jointly, no breakdown of what the $12K covers — API/token spend only, or also compute/infrastructure — and no disclosed methodology for the $6M staffing estimate)
- **Quote**: "Model and infrastructure costs came to about $12,000, compared with Asana's roughly $6 million estimate for the previous staffing plan."
- **Our assessment**: This is the most quantitatively concrete and novel figure in the source — a direct dollar-cost-versus-staffing-estimate comparison, distinct from a time-savings claim. It is comparable in kind (though not scale) to the token-cost figures documented in `blog-anthropic-code-migration-playbook.md` Claim 4 (Bun migration: ~$165,000 in API costs for ~1M lines over two weeks) — Asana's figure is roughly 13x cheaper for what appears to be a narrower-scope migration (a single testing framework, not a full-language port). Neither the $12K nor the $6M figure is independently audited; the $6M in particular is a hypothetical staffing estimate for work that was never done the old way, so it functions as marketing framing as much as a real cost baseline.

### Claim 3: Asana's engineering organization already uses Codex routinely for large codebase changes, following a review-and-approve workflow, as standing practice — this migration was not a one-off pilot
- **Evidence**: Narrator (OpenAI-authored) framing sentence describing Asana's general engineering practice before introducing the specific Enzyme project.
- **Confidence**: anecdotal (unattributed narrator claim, no numbers on how many engineers, how many projects, or over what period)
- **Quote**: "Asana brings the same approach to its engineering organization, where people use OpenAI Codex, powered by frontier models, to tackle large codebase changes, then review and approve each proposed change."
- **Our assessment**: This frames the Enzyme removal as an instance of an existing organizational practice rather than a novel experiment — worth noting because it changes how the headline result should be read: not "a company tried Codex once and got lucky," but "a company with an established Codex-for-large-changes workflow applied it to this particular project." The claim gives no specifics on maturity or scale of that standing practice, so it should be read as context, not as independent evidence of adoption depth.

### Claim 4: The target of the migration was Enzyme, a testing tool that had fallen out of active maintenance and had become a blocker to modernizing Asana's frontend stack
- **Evidence**: Narrative description of the specific technical target, in the case study body.
- **Confidence**: anecdotal (single-project technical detail)
- **Quote**: "Their old testing tool, Enzyme, had fallen out of active maintenance and was becoming a blocker to modernizing Asana's frontend stack."
- **Our assessment**: This grounds the headline claim in a specific, checkable technical scope: removing a single deprecated dependency across a frontend codebase, not a full-application rewrite or language port. This scoping detail matters for comparing this case study against larger migrations in the corpus (see Cross-References) — "five years of engineering work" almost certainly refers to Asana's own internal estimate for a large, tedious, low-glamour dependency-removal project (the kind of work that chronically gets deprioritized), not five years of net-new feature engineering.

### Claim 5: The workflow used a single five-sentence prompt to launch up to four coding agents working in parallel, each operating in its own separate copy of the codebase
- **Evidence**: Narrative description of the specific engineering workflow used for the Enzyme removal.
- **Confidence**: anecdotal (single project, self-reported workflow, no detail on how the four agents' outputs were reconciled/merged)
- **Quote**: "From a five-sentence prompt, up to four coding agents worked in parallel, each in a separate copy of the codebase."
- **Our assessment**: A concrete, small-scale data point on the "parallel-agents-in-isolated-codebase-copies" migration pattern already documented at much larger scale in `blog-anthropic-code-migration-playbook.md` (Mike Krieger's port used "hundreds of agents" across eight phase gates). Asana's four-agent version, launched from a five-sentence prompt with no described gap-inventory or rulebook step, suggests this pattern scales down to lightweight, low-ceremony use for narrower migrations — though the source gives no detail on how conflicting or overlapping work across the four parallel copies was reconciled, which is a real gap given the playbook source's emphasis on that exact problem (adversarial review, rule-vs-patch fixes) at larger scale.

### Claim 6: One engineer checked progress twice a day and reviewed every proposed change; simpler instructions worked better than a more elaborate setup
- **Evidence**: Narrative description of the human-in-the-loop cadence and a stated lesson-learned, in the same sentence as Claim 5's workflow description.
- **Confidence**: anecdotal (single project, self-reported, no definition of what "reviewed" entailed — code review only, or also test/behavior verification)
- **Quote**: "An engineer checked progress twice a day and reviewed every proposed change. Simpler instructions worked better than a more elaborate setup."
- **Our assessment**: Two distinct, useful claims bundled in adjacent sentences. First, a minimal human-review cadence (one engineer, twice daily, full review of every change) for a four-agent-parallel migration — a much lighter review structure than the "two adversarial reviewers plus a third-agent tiebreaker" mechanism described for Anthropic's own large-scale migrations. Second, an explicit "simpler is better" prompt-engineering finding that sits in some tension with the more elaborate rulebook/dependency-map/gap-inventory methodology `blog-anthropic-code-migration-playbook.md` recommends as a prerequisite step for migrations. We read this as a scope-conditioned difference rather than a genuine contradiction: Enzyme removal is a narrower, single-dependency task, while the Anthropic playbook's methodology was built for a ~1M-line full-language port — the "how much upfront structure does a migration need" answer plausibly depends on migration scale/complexity, not on which vendor's tool is used. Worth flagging for the guide as an open question rather than settled guidance either way.

### Claim 7: Asana's CTO explicitly disclaims generalizability of the result, framing it as expanding what's worth attempting rather than as a universal productivity multiplier
- **Evidence**: Direct, attributed quote from Amritansh Raghav, Chief Technology Officer, Asana — the only named individual and only first-person voice in the piece.
- **Confidence**: anecdotal (single executive's characterization, but notable for its self-limiting framing in a vendor-published promotional piece)
- **Quote**: "Not every years-long project will collapse into weeks. But agents can give engineers more room for craft—and make once-impossible work worth attempting."
- **Our assessment**: This is an unusually self-aware caveat for a vendor case study to publish — most of the case studies in our corpus (e.g., the Notion piece) let a flat headline number stand without an on-the-record hedge from the featured executive. The second half of the quote reframes the value proposition away from "5 years → 2 weeks, always" and toward "some previously-impractical projects become worth attempting" — a materially more defensible claim, and one worth citing precisely because it's the more conservative framing volunteered by the customer, not by OpenAI's marketing copy.

### Claim 8: Completing the Enzyme migration changed which long-running software projects Asana now believes are practical to attempt, and the company plans to test agents on other migrations, rewrites, and performance problems it previously assumed would take years
- **Evidence**: Narrator closing statement.
- **Confidence**: anecdotal (forward-looking intention, not a measured outcome; no specifics on which other projects)
- **Quote**: "With this migration complete, Asana can test agents on other migrations, rewrites, and performance problems it once assumed would take years. The team hopes this will give engineers more room to focus on craft while people continue to review the work."
- **Our assessment**: A forward-looking claim, not a result — treat as intention/hope rather than evidence of a second successful migration. The "people continue to review the work" clause is a notable, if brief, acknowledgment that human review remains part of the model going forward rather than being a one-time step that gets removed once trust is established.

### Claim 9: The "two calendar weeks" headline figure resolves, on closer reading, to 1.5 weeks of engineering effort spread across two calendar weeks
- **Evidence**: A precision-clarifying detail in the case study's closing paragraph, distinct from the rounder headline figure.
- **Confidence**: anecdotal (single-project self-report; "1.5 weeks of engineering effort" is not further defined — effort by how many people, measured how)
- **Quote**: "After 1.5 weeks of engineering effort spread across two calendar weeks, Enzyme was fully removed."
- **Our assessment**: As with the Notion case study (where the headline "3 hours" collapsed a hedged "three or four hours" quote), the precise supporting detail here is slightly more conservative than the rounded headline. The gap is small (1.5 vs. 2 weeks) compared to Notion's, so this is a minor rather than major instance of headline rounding, but it is worth noting as a recurring pattern in how OpenAI's case-study team packages practitioner-level detail into a rounder headline stat.

## Concrete Artifacts

### Case study metadata and stat block

```
Source: https://openai.com/index/asana (August 18, 2026)

Company size: Enterprise
Region:       North America
Industry:     Technology
Products:     Codex, API

Headline stats:
  2      Calendar weeks to finish work expected to take 5 years
  $12K   Model and infrastructure cost versus Asana's ~$6M staffing estimate
```

### Workflow description — verbatim

```
Source: https://openai.com/index/asana (August 18, 2026)

"Their old testing tool, Enzyme, had fallen out of active maintenance and
was becoming a blocker to modernizing Asana's frontend stack. Asana used
Codex, powered by frontier models, to do the work. From a five-sentence
prompt, up to four coding agents worked in parallel, each in a separate
copy of the codebase. An engineer checked progress twice a day and
reviewed every proposed change. Simpler instructions worked better than a
more elaborate setup.

After 1.5 weeks of engineering effort spread across two calendar weeks,
Enzyme was fully removed. Model and infrastructure costs totaled about
$12K. For comparison: the previous plan was expected to take at least
five years and estimated to cost roughly $6M. The experience changed
which long-running software projects the company believes are practical
to take on."
```

### CTO quote — verbatim

```
Source: https://openai.com/index/asana (August 18, 2026)
Attribution: Amritansh Raghav, Chief Technology Officer, Asana

"Not every years-long project will collapse into weeks. But agents can
give engineers more room for craft—and make once-impossible work worth
attempting."
```

## Cross-References

- **Corroborates**: `blog-anthropic-code-migration-playbook.md` Claim 3 (Mike Krieger's 165,000-line Python-to-TypeScript port using "hundreds of agents" across eight phase gates) and Claim 4 (Bun migration: ~$165,000 in API costs for ~1M lines of code in under two weeks). This source is a second vendor's (OpenAI Codex, vs. Anthropic Claude Code) customer example of the same general pattern — spinning up multiple parallel coding-agent instances against a codebase, with human review gating merges — at a much smaller scale (4 agents, a single deprecated testing library) and a much lower absolute cost (~$12K vs. ~$165K). Together these sources suggest the "parallel agents + human review checkpoints" migration pattern scales down from hundred-agent, million-line ports to four-agent, single-dependency removals, which is a useful data point on the low end of that spectrum that the Anthropic playbook source doesn't cover.
- **Corroborates**: `blog-thoughtworks-mishra-ai-assisted-migration.md` Claim 8 (a Thoughtworks/AWS framework compressed a 10-sport migration program from an estimated two-to-three years down to three-to-four weeks). This is a third, independently-sourced case (different vendor, different company, different technical domain — legacy-sports-platform modernization vs. frontend-testing-framework removal) of an AI-assisted effort compressing a multi-year internal estimate into a multi-week actual delivery. Three separate vendors/companies making structurally similar "years-to-weeks" compression claims strengthens the general pattern, though each individual claim remains a single vendor-published case study with an unaudited counterfactual estimate.
- **Extends**: `blog-openai-notion-codex-case-study.md` and `blog-openai-codex-knowledge-work.md`. This is a third OpenAI customer case study in the corpus, following the same promotional format (company metadata block, headline stat, single named-practitioner quote), but the first to include (a) a genuine multi-agent parallel workflow (Notion's case was one engineer using Codex directly, not orchestrating parallel agent copies) and (b) an actual dollar cost figure set against a staffing-cost estimate, rather than only a time-savings figure. It also extends the "headline number rounds a more hedged practitioner detail" pattern first noted in the Notion source's Claim 1/Claim 7 (see this note's Claim 9).
- **Contradicts**: None filed. Claim 6's "simpler instructions worked better than a more elaborate setup" sits in tension with the rulebook/dependency-map/gap-inventory-first methodology in `blog-anthropic-code-migration-playbook.md`, but per MINER.md §4a this reads as a scope-conditioned difference (single-dependency removal vs. full-language port at ~1M lines) rather than a genuine contradiction that would change guide advice at the same scale — not filed as a contradiction issue.
- **Novel**:
  - A direct dollar-cost-versus-staffing-estimate comparison ($12K actual vs. ~$6M estimated) — the first source in the corpus to set an actual agent-driven project cost against a counterfactual staffing-cost estimate for the identical project, rather than only reporting time savings or an absolute token cost in isolation.
  - A small-N (up to four) parallel-agent-copies data point, giving the corpus a lower-bound-of-scale example to compare against Krieger's "hundreds of agents" and Sumner's Bun migration.
  - An explicit, on-the-record executive hedge disclaiming generalizability of the headline result — unusual for a vendor-published customer case study.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add this source as a smaller-scale corroboration of the parallel-agent-copies-plus-human-review migration pattern already documented from `blog-anthropic-code-migration-playbook.md`, specifically noting that the pattern appears usable at both ends of a wide scale spectrum (4 agents / single dependency vs. hundreds of agents / full-language port). Flag Claim 6's "simpler instructions worked better than a more elaborate setup" as a data point worth testing against the more elaborate rulebook-first methodology — likely scale-conditioned, not a universal rule, and the guide should say so explicitly rather than picking a side.
- **Chapter 05 (Team Adoption)**: Cite Claim 2 (the $12K-vs-$6M dollar comparison) alongside the Bun migration's $165K token-cost figure as a second concrete case study on the economics of agent-driven migrations, with the explicit caveat (per Our assessment) that the "$6M staffing estimate" is an unaudited hypothetical, not a measured baseline. Cite Claim 7 (the CTO's hedge) as a citable, vendor-published example of realistic framing that the guide can point to when cautioning readers against over-generalizing headline productivity ratios.
- **Chapter 01 (Daily Workflows)**: Claim 6's review cadence (one engineer, twice daily, reviewing every proposed change across four parallel agent copies) is a concrete, minimal human-in-the-loop staffing pattern for a small-scale parallel-agent migration — worth citing alongside the DRI/review-cadence material already in `blog-anthropic-large-codebase-best-practices.md` as a lighter-weight alternative for narrower-scope work.

## Extraction Notes

- The live OpenAI URL (`https://openai.com/index/asana`) returned HTTP 403 to WebFetch, consistent with the Cloudflare bot-blocking behavior already documented for `openai.com` in `blog-openai-codex-knowledge-work.md`'s and `blog-openai-notion-codex-case-study.md`'s Extraction Notes. Retrieved instead via the Wayback Machine snapshot `http://web.archive.org/web/20260821101055/https://openai.com/index/asana/` (crawled August 21, 2026, three days after the August 18 publication date), fetched with `curl` and parsed by stripping `<script>`/`<style>` blocks and remaining tags rather than through an AI-summarization pass, specifically to guarantee the `Quote` fields above are copied character-for-character rather than paraphrased, per MINER.md §2a. Every quote was independently cross-checked against raw quoted string literals in the archived HTML (the `og:description`/`meta description` tags and inline JSX-string literals both contain duplicate copies of several of the body sentences, which served as a second verification pass).
- The source is short (~400 words, shorter than the comparable Notion case study) with no linked sub-pages containing further substantive content about this specific case study; the page's "Keep reading" footer links to three unrelated OpenAI posts ("Introducing AI Futures," "How ChatGPT Work helps Stampli move ideas to market," "Offering Zero Data Retention for frontier models"), none of which concern Asana or this migration, and were not followed.
- This is a single-source, single-company, vendor-published case study with exactly one named individual (the CTO) and no quote from any engineer who actually ran the migration. Every claim above should be read with that ceiling in mind: OpenAI selected what to publish, Asana did not publish an independent account, and neither the $12K cost figure nor the $6M/five-year counterfactual is independently audited or methodologically explained.
- No contradictions were filed; see the Cross-References `Contradicts` entry for the reasoning on why the "simpler instructions" claim was treated as scope-conditioned rather than filed as a contradiction issue.
