---
source_url: https://sourcegraph.com/blog/a-smarter-way-to-run-code-migrations-with-less-llm-context
source_type: blog-post
title: "A smarter way to run code migrations with less LLM context"
author: Kalan Chan (Sourcegraph)
date_published: 2026-08-28
date_extracted: 2026-08-29
last_checked: 2026-08-29
status: current
confidence_overall: emerging
issue: "#3056"
---

# A smarter way to run code migrations with less LLM context

> Sourcegraph vendor blog post arguing that migration and audit tasks should
> not dump raw search results into an LLM's context window; instead, Deep
> Search's sandboxed "evaluator" tool runs the search, filtering, and
> aggregation itself and hands the LLM only the aggregated findings and a
> generated CSV/JSON/SVG artifact — trading a thin, undemonstrated efficiency
> claim for a concrete, previously-shipped mechanism this Miner traced back to
> two dated Sourcegraph changelog entries.

## Source Context

- **Type**: blog-post (Sourcegraph company blog, published August 28, 2026;
  auto-discovered via the `sourcegraph` trusted feed named in the triage
  issue). Short-form (~600 words) argumentative/explainer piece: one framing
  paragraph, five section headings ("The problem with naive agent workflows,"
  "Why this changes the economics," "Primary use case: migrations,"
  "Secondary value: better context quality," "Broader applications"), and a
  conclusion. Ends with "A special thanks to Justin Dorfman and Stephanie
  Jarmak for their contributions to this blog post" — both are bylined authors
  of other Sourcegraph posts already in this corpus (see Cross-References).
- **Author credibility**: Byline is Kalan Chan, published on Sourcegraph's
  official company blog (confirmed independently via Sourcegraph's own RSS
  feed at `sourcegraph.com/blog/rss.xml`, which lists the same title, author,
  and publish date). This is vendor content: Sourcegraph sells Deep Search,
  the product being described. Unlike the companion `jarmak-evaluate` and
  `tanner-vulnerability-remediation` notes already in this corpus, this post
  contains no independently-checkable statistic of its own (no benchmark, no
  percentage, no dollar figure for the migration/audit use case it describes)
  — every concrete claim about *what the product does* was verified by this
  Miner against Sourcegraph's own dated changelog entries (see Concrete
  Artifacts), but the *value proposition* (cost savings, quality improvement)
  is asserted, not measured, within this post.
- **Scope**: Covers the architectural pattern of running searches and
  aggregation inside a sandbox before any data reaches the LLM, illustrated by
  migration audits, TODO-comment inventories, and dependency-version audits.
  Does NOT cover: a worked cost comparison (tokens or dollars) between the
  sandboxed-evaluator approach and a naive context-dumping approach on the
  same task, the sandbox's security/isolation model beyond "sandboxed," or any
  named customer's before/after migration timeline.

## Extracted Claims

### Claim 1: Token costs are under increased executive scrutiny as enterprises scale AI use, making runaway token usage a real risk for large-scale migration and audit projects specifically
- **Evidence**: Opening framing claim, linked to an external EY newsroom
  survey ("EY survey: C-suites pivot from AI adoption to unlocking value as
  escalating token costs trigger fiscal scrutiny," July 2026) rather than any
  Sourcegraph-first-party data.
- **Confidence**: emerging (the underlying EY survey was not independently
  fetched by this Miner; treated as a secondhand citation)
- **Quote**: "Token costs are under scrutiny as enterprises scale their use of AI. While businesses are eager to leverage AI to modernize their codebases, runaway token usage can quickly make large-scale projects prohibitively expensive. Tasks like migration and codebase audits are particularly high-risk; they often require scanning thousands of files, and dumping all that intermediate data into an LLM's context window is a recipe for inflated costs and diluted performance."
- **Our assessment**: This is the article's justification for why migrations
  and audits specifically (not AI-assisted coding generally) are the target
  use case — the claim is that these tasks structurally require scanning many
  files, which is the precondition for the "naive workflow" failure mode
  described in Claim 2. Directly corroborates this corpus's existing token-
  cost-scrutiny material (see Cross-References).

### Claim 2: Standard AI agent workflows treat the LLM as the sole processor for every step, pulling vast amounts of raw data into the context window and hoping the model finds the signal in the noise — but more context does not always mean better context
- **Evidence**: Author's own diagnostic claim, presented as the article's
  central problem statement.
- **Confidence**: anecdotal (asserted architectural critique, no named example
  of a specific naive workflow measured against this pattern)
- **Quote**: "Standard AI agent workflows often treat the LLM as the sole processor for every step of a task. They pull vast amounts of data directly into the context window, hoping the model can sort through the noise to find the signal. However, more context does not always mean better context."
- **Our assessment**: This is a restatement, from the tool-vendor side, of a
  failure mode this corpus already documents from the practitioner side (see
  Cross-References — Corroborates). The claim is directionally credible and
  consistent with known context-window degradation mechanisms, but the post
  gives no example of a specific naive workflow's token count or failure rate
  to substantiate it — it functions as the setup for Deep Search's proposed
  fix, not an independently measured finding.

### Claim 3: Deep Search's evaluator tool runs sandboxed scripts around Sourcegraph's search APIs — running multiple searches, cross-referencing data, filtering findings, and calculating totals — so the LLM receives only the aggregated findings and a final structured artifact, not the raw intermediate search results
- **Evidence**: Author's own architectural description, linking to two
  Sourcegraph changelog entries as evidence: `changelog/releases/7.3#evaluator-tool-for-code-execution`
  and `changelog/deep-search-evaluator-files`. This Miner independently
  fetched both linked changelog pages (see Concrete Artifacts) and confirmed
  the described mechanism matches Sourcegraph's own dated release notes for
  the underlying feature.
- **Confidence**: emerging (a first-party architectural description,
  independently corroborated by two dated changelog entries describing the
  same underlying feature, but with no independent third-party verification
  of how the sandbox itself is isolated or resourced)
- **Quote**: "Deep Search can run scripts in a sandboxed environment around Sourcegraph's search APIs. Instead of feeding every intermediate search result into the LLM, Deep Search does the heavy lifting: it can run multiple searches, cross-reference data, filter findings, calculate totals, and even generate structured artifacts like CSVs, JSON, or SVG reports. The LLM then receives only the aggregated findings and the final artifact, keeping your context window focused and efficient."
- **Our assessment**: This is the post's central mechanism and its most
  concrete, checkable claim — and it holds up against independent
  verification (Claim 4 below). The "LLM receives only the aggregated
  findings and the final artifact" framing is the load-bearing architectural
  idea: it moves the search-and-filter loop entirely out of the token-billed
  context window and into a separate execution environment, rather than
  merely compressing or summarizing what would otherwise be dumped into
  context.

### Claim 4 (verified against Sourcegraph's own changelog, not just this post): The evaluator is specifically a code-execution tool that lets sandboxed Lua scripts call keyword, regex, commit, or diff searches and process the results programmatically
- **Evidence**: This Miner independently fetched `sourcegraph.com/changelog/releases/7.3`
  (the page linked from Claim 3) and located the changelog entry with anchor
  `id="evaluator-tool-for-code-execution"`, titled "Evaluator tool for code
  execution," under the "Deep Search" product domain badge.
- **Confidence**: settled (a first-party, dated changelog entry describing a
  specific shipped feature — the most concrete and independently-locatable
  claim in this note)
- **Quote**: "Added a code execution 'evaluator' tool to Deep Search that allows sandboxed Lua scripts to call keyword, regex, commit or diff searches and process results programmatically." (from `sourcegraph.com/changelog/releases/7.3`, changelog entry "Evaluator tool for code execution")
- **Our assessment**: This is a materially more specific and technically
  verifiable claim than anything stated in the blog post itself — the blog
  post never names the scripting language. The Miner traced the mechanism
  back to its origin: the same release's fuller "Quantitative answers in Deep
  Search" changelog post (linked from the same page, dated implicitly by an
  April 2026 screenshot asset) frames it as "Deep Search has always been good
  at finding and explaining code. It can now also count, rank, and aggregate
  it without blowing up the context window," with a worked example: "In
  github.com/kubernetes/kubernetes, who left the most TODO(&lt;username&gt;)
  comments? Show the top 15." This confirms the feature substantially
  predates the blog post being mined here (first shipped as of the 7.3
  release, with the blog post republishing it as a migration-specific use
  case four months later) — the blog post is a use-case repackaging of an
  existing shipped capability, not an announcement of new functionality.

### Claim 5: Offloading processing to the sandbox provides three advantages: paying only for high-level insights (not per-file processing), keeping the model undistracted by irrelevant file content, and producing reliable structured data ready for immediate team action
- **Evidence**: Author's own enumerated claim, presented as "Why this changes
  the economics."
- **Confidence**: anecdotal (asserted list of benefits, no quantified
  before/after comparison for any of the three)
- **Quote**: "By offloading processing to the sandbox, you gain three key advantages: You only pay for the high-level insights, not the intermediate processing of every file. The model isn't distracted by thousands of lines of irrelevant file content. You get reliable, structured data that is ready for teams to act on immediately."
- **Our assessment**: The first two advantages are cost and quality claims
  already covered by Claims 2-3; the third (structured, immediately-actionable
  output) is the more novel point specific to migrations — see Claim 6. None
  of the three is quantified in this post; a reader wanting a specific cost
  multiplier or accuracy delta will not find one here.

### Claim 6: For a migration moving services from one package to another, Deep Search can produce a complete, comprehensive audit of every repository still importing the old package as a clean CSV checklist, which a team can open and begin migrating from directly
- **Evidence**: Author's own worked example, presented as the article's
  "Primary use case: migrations" section.
- **Confidence**: anecdotal (illustrative example, not a named customer case
  study with before/after timing or accuracy figures)
- **Quote**: "Consider a common migration scenario: moving services from old/package to new/package. Using Deep Search, you can ask for a complete audit of every repository that still imports the old package. Deep Search scans the codebase, identifies the files, and generates a clean CSV checklist. Your team can then open that file and start the migration process, confident that the report is comprehensive and accurate."
- **Our assessment**: "Confident that the report is comprehensive and
  accurate" is an assertion, not a demonstrated property — the post gives no
  method for verifying completeness (e.g., no mention of a control like
  `blog-sourcegraph-jarmak-evaluate-on-your-codebase.md`'s "audit actual tool
  use" or "pin the code" controls). Readers relying on this pattern for a
  real migration should independently validate coverage rather than trust the
  "comprehensive and accurate" framing at face value.

### Claim 7: Because Deep Search only passes relevant data to the LLM, the model stays focused on synthesizing conclusions rather than acting as a data processor, which improves the probability of more useful, accurate outputs
- **Evidence**: Author's own claim, presented as "Secondary value: better
  context quality."
- **Confidence**: anecdotal (asserted mechanism, no accuracy measurement
  comparing evaluator-mediated output against a naive-context-dump baseline
  on the same task)
- **Quote**: "Because Deep Search only passes relevant data to the LLM, the model remains focused on synthesizing conclusions rather than acting as a data processor. This improves the probability of more useful, accurate outputs."
- **Our assessment**: "Improves the probability" is a hedge with no attached
  number — this is the weakest-evidenced claim in the post, restating Claim 2
  in the positive direction without new evidence. Should not be cited in the
  guide as a settled quality claim; it is a plausible mechanism, not a
  demonstrated one.

### Claim 8: The evaluator pattern generalizes beyond migrations to any search-driven artifact-generation task: cross-organization service-usage inventories, code-health audits for outdated or vulnerable dependencies (explicitly naming Log4j versions below 2.17), and cross-implementation pattern comparison
- **Evidence**: Author's own enumerated list, presented as "Broader
  applications."
- **Confidence**: anecdotal (illustrative categories, no named example
  execution of any of the three beyond the migration case in Claim 6)
- **Quote**: "Deep Search is powerful for any search-driven artifact generation: Inventories: Track how shared services are consumed across the organization. Code health: Identify repositories using outdated or vulnerable dependencies (e.g., Log4j versions < 2.17). Cross-referencing: Compare implementations across patterns to identify inconsistencies."
- **Our assessment**: The Log4j example is notable because it is nearly
  identical to a worked prompt in Sourcegraph's own linked changelog entry
  (see Concrete Artifacts) — "create a CSV of services still using Log4j
  versions earlier than 2.17" — confirming this is a real, previously-
  demonstrated capability rather than a hypothetical the author invented for
  this post. It also directly matches the "code health" audit scenario this
  corpus's `blog-sourcegraph-tanner-vulnerability-remediation-scale.md`
  argues enterprises structurally cannot answer today (see Cross-References).

### Claim 9: As AI adoption matures, token efficiency is becoming a critical buying consideration for engineering leaders, and Deep Search's evaluator is positioned as a concrete architectural answer to that consideration for large-scale migration or audit work
- **Evidence**: Author's own closing claim, presented as the conclusion.
- **Confidence**: anecdotal (a market-positioning assertion, not a measured
  industry trend within this post — though it echoes Claim 1's externally-
  cited EY survey)
- **Quote**: "As AI adoption matures, token efficiency is becoming a critical buying consideration for engineering leaders. Deep Search's evaluator offers a concrete, architectural solution for lowering costs while improving the quality of AI-assisted development. If you are planning a large-scale migration or audit, it's time to move beyond standard agent workflows and let Deep Search handle the scale."
- **Our assessment**: This is a sales close, not a new claim — it restates
  Claims 2, 5, and 7 as a single call to action. Included here for
  completeness (the article's own framing of stakes) rather than as
  independent evidence.

## Concrete Artifacts

### The evaluator mechanism, as shipped (verbatim from Sourcegraph's own changelog, independently fetched by this Miner — not from the blog post itself)
```
Source: https://sourcegraph.com/changelog/releases/7.3
Changelog entry id: evaluator-tool-for-code-execution
Domain badge: Deep Search

"Evaluator tool for code execution"

"Added a code execution 'evaluator' tool to Deep Search that allows
sandboxed Lua scripts to call keyword, regex, commit or diff searches
and process results programmatically."
```

### The fuller feature announcement this changelog entry belongs to (same release, linked as "Quantitative answers in Deep Search")
```
Source: https://sourcegraph.com/changelog/releases/7.3 (embedded post,
also independently published at sourcegraph.com/changelog/deep-search-evaluator)

"Deep Search has always been good at finding and explaining code. It can
now also count, rank, and aggregate it without blowing up the context
window."

"A new sandboxed scripting tool lets the agent run programmatic
aggregations across many searches in a single turn. Questions that don't
fit into a single query, e.g. top-N rankings, cross-search joins,
distributions across many files, can now be answered end-to-end, with
every underlying search still cited so you can verify how the answer was
assembled."

Example prompts given verbatim:
- "In github.com/kubernetes/kubernetes, who left the most TODO(<username>)
  comments? Show the top 15."
- "How far along is the interface{} -> any migration in golang/go? Break
  it down by top-level package."
- "In microsoft/vscode, which files have been touched in the most
  fix/bugfix commits in the last 6 months, and who's been fixing them?"
- "List the top 20 internal Go packages in sourcegraph/sourcegraph by
  number of distinct other internal packages that import them."
- "What's the total of all resources (cpu + mem) across all deployments
  on k8s in myorg/infra?"
```

### The follow-on feature this post also links to: downloadable structured reports (verbatim)
```
Source: https://sourcegraph.com/changelog/deep-search-evaluator-files
Published: 2026-07-31, author Kalan Chan (same author as the mined blog post)

Title: "More exhaustive Deep Search, now with downloadable reports"
Tagline: "Deep Search can now cross-reference and aggregate larger result
sets, and write its findings to downloadable CSV, JSON, and SVG files."

"Ask Deep Search for codebase wide inventories, audits, or migration
reports that would be too large to present cleanly in an answer. Deep
Search summarizes the key findings in chat and attaches the full
structured output for further analysis or tracking."

"Deep Search can also read generated CSV and JSON files in follow-up
investigations. This allows it to filter, join, or enrich previously
collected results without repeating the original codebase searches."

Example prompts given verbatim:
- "Trace every field requested from profile-service through
  getProfileFeatures. Create a CSV with the consuming service,
  repository, source URL, field mask, feature group, and request type."
- "Across all repositories, create a CSV of services still using Log4j
  versions earlier than 2.17. Group the results by repository and
  detected version."
- "Create a migration checklist of every service that imports old/package
  but does not yet import new/package."
```

### Demo caption from the blog post itself (verbatim)
```
Source: https://sourcegraph.com/blog/a-smarter-way-to-run-code-migrations-with-less-llm-context

"Deep Search scans kubernetes/kubernetes for the files under pkg/ with
the most TODO comments, then returns a CSV and an SVG chart instead of
the file contents it read to get there."
```

## Cross-References

- **Corroborates** `failure-thailandjohn-schema-refactor-context-collapse.md`
  Lesson 1 (cross-cutting refactors are a context-window cliff) and Lesson 6
  (a database-indexed codebase gives AI agents ground truth without loading
  all files into context): ThailandJohn's failure was triggered by exactly
  the scenario this post names as the target use case — a schema/package
  migration requiring the agent to hold too many files' worth of context
  simultaneously. Deep Search's evaluator is architecturally the same class
  of fix as TheAuditor's SQLite index (route the agent through a pre-built
  query surface instead of raw file loading), but implemented as sandboxed
  script execution over a search API rather than a locally-indexed graph
  database. Neither source's author appears aware of the other's approach;
  both independently converge on "don't let the agent read the raw files to
  answer an aggregate question" as the fix for the same failure mode.
- **Corroborates** `blog-mattwood-unit-of-return.md` Claim 8 (the full cost of
  an AI-produced result includes more than the model call — search, other
  software, self-checking, retries — and a token-only cost model
  understates it): this post's Claim 3/5 describe a concrete implementation
  that removes the "search and intermediate processing" cost component from
  the LLM-billed portion of a migration task entirely, by moving it into a
  sandboxed script. Where Wood's essay argues from first principles that
  full-path cost must be measured, this post is a vendor's specific
  architectural response to one piece of that full-path cost (the
  search/filter/aggregate step) for one task class (migrations and audits).
- **Extends** `blog-sourcegraph-jarmak-evaluate-on-your-codebase.md`: that
  note evaluates whether Sourcegraph's *retrieval* (finding relevant files)
  changes task completion and cost, using F1/recall/cost metrics across 288
  tasks, and finds retrieval quality and task completion move independently.
  This post describes a different, additive capability layered on the same
  search APIs — programmatic *aggregation* across many searches (counting,
  ranking, cross-referencing), not just finding files — and gives no
  equivalent quantified evaluation of its own. A reader who takes the
  Jarmak note's lesson seriously (measure retrieval quality, task
  completion, and cost separately, and don't trust a vendor's single
  aggregate claim) should apply the same skepticism to this post's
  unquantified "comprehensive and accurate" (Claim 6) and "improves the
  probability of...accurate outputs" (Claim 7) claims — no equivalent
  nine-control evaluation of the evaluator tool itself is presented here.
- **Extends** `blog-sourcegraph-tanner-vulnerability-remediation-scale.md`
  Claim 12 (the proposed fix for enterprise vulnerability remediation
  requires "exact answers: given a CVE...an exhaustive list of every
  occurrence instead of a sampling") and `blog-sourcegraph-dorfman-repo-security-posture.md`:
  this post's Log4j-version code-health example (Claim 8) is the same
  Sourcegraph capability those two posts describe in the abstract as
  "universal code search" — this note supplies the concrete underlying
  mechanism (sandboxed evaluator script + generated CSV) that would produce
  the "exact answers" and "exhaustive list" those posts promise, closing the
  gap between their architectural claim and this post's implementation
  detail.
- **Extends** `blog-anthropic-large-codebase-best-practices.md` Claim 2
  (Claude Code uses agentic search — live filesystem traversal and grep —
  rather than RAG-based embedding retrieval, to avoid index staleness): this
  post's evaluator operates on top of Sourcegraph's own search index (a
  different retrieval substrate than Claude Code's live-filesystem
  approach), but addresses an orthogonal problem — not *how* to find
  relevant code, but what happens to the results *after* they're found. An
  agent using either agentic search or a Sourcegraph-style index still faces
  the "dump everything into context" failure mode this post names in Claim
  2 if it processes aggregation and filtering inside the LLM's own context
  rather than in a separate execution step.
- **Extends** `blog-thoughtworks-mishra-ai-assisted-migration.md`: that note
  documents a different large-scale-migration cost-reduction architecture
  (separating legacy-code extraction from spec generation, with Golden
  Rules and file:line traceability to prevent hallucination) that reduced a
  10-sport sports-data migration from 2-3 years to 3-4 weeks. Both sources
  converge on the same underlying principle — large migrations fail or
  become prohibitively expensive when an LLM is made to process everything
  itself — but propose non-overlapping architectural fixes: Mishra's
  framework restructures *when* and *how* the LLM is invoked in a
  multi-stage pipeline; this post keeps the LLM invocation pattern the same
  but moves search/aggregation work out of its context window entirely via
  a sandbox. Neither approach is presented as a substitute for the other; a
  team could plausibly combine both (sandboxed evaluator for the audit/
  discovery phase, spec-mediated generation for the migration phase).
- **Contradicts**: None identified. No existing corpus note argues that
  dumping raw intermediate search results into an LLM's context window is
  preferable to sandboxed pre-processing for aggregate/audit-style tasks, or
  that sandboxed evaluator tools introduce a cost or quality problem this
  post's claims would need to answer. No contradiction issue filed.
- **Novel**: The specific "evaluator" mechanism name and its Lua-scripting
  implementation detail (Claim 4, sourced from Sourcegraph's own changelog
  rather than the mined blog post); the "aggregated findings and final
  artifact only, not raw intermediate results" framing as an explicit
  context-window-reduction architecture (Claim 3) is a more precise
  articulation than this corpus's existing "index instead of raw files"
  pattern (TheAuditor) because it targets computation/aggregation
  specifically, not just lookup; the three concrete worked artifact types
  (CSV, JSON, SVG) as LLM-context-avoidance outputs is new to this corpus.

## Guide Impact

- **Chapter 04 (Context Engineering)**: Add the "evaluator" pattern —
  offload search, filtering, and aggregation to a sandboxed execution step
  and pass only the aggregated result and a generated artifact (CSV/JSON/
  SVG) into the LLM's context — as a named architectural mitigation for the
  "context collapse on cross-cutting refactors" failure mode already
  documented via `failure-thailandjohn-schema-refactor-context-collapse.md`.
  Present it alongside the existing "database-indexed codebase" mitigation
  as two implementations of the same underlying principle (ground the agent
  in externally-computed facts rather than raw file dumps), noting neither
  is validated against the other in this corpus.
- **Chapter 02 (Economics) / cost-of-migrations guidance**: When discussing
  migration or audit task costs, cite this post's Claim 1 (migrations and
  audits are specifically high-risk for runaway token cost because they
  require scanning thousands of files) as the structural reason these task
  types deserve dedicated cost-reduction architecture rather than being
  treated as a generic agentic-coding task. Explicitly flag that this
  post's own cost-savings claims (Claims 5, 7, 9) are unquantified — pair
  any recommendation to adopt an evaluator-style pattern with
  `blog-sourcegraph-jarmak-evaluate-on-your-codebase.md`'s nine-control
  checklist so a team validates the savings on its own workload rather than
  taking the vendor's framing at face value.
- **Chapter 06 (Security & Threat Model) / code-health audits**: Add the
  Log4j-version code-health example (Claim 8, corroborated by the changelog
  artifact) as a concrete, demonstrated instance of the "exact answers...
  exhaustive list of every occurrence" capability that
  `blog-sourcegraph-tanner-vulnerability-remediation-scale.md` argues
  enterprises need but usually lack — this post supplies the mechanism,
  Tanner's post supplies the enterprise-scale motivation.

## Extraction Notes

- The blog post itself renders as an empty shell under a plain `curl`
  fetch (a SvelteKit client-hydrated app) but a browser-user-agent `curl`
  request returned the fully server-rendered HTML, including the article
  body inside `<div class="markdown-body">`. All Claim quotes above were
  copied directly from that server-rendered HTML, not from a WebFetch
  summarization pass (WebFetch against this URL returned HTTP 403 and was
  not used for any content in this note).
- Per MINER.md §1, this Miner followed the two Sourcegraph changelog links
  embedded in the post body (`changelog/releases/7.3#evaluator-tool-for-code-execution`
  and `changelog/deep-search-evaluator-files`), fetching both directly. This
  was the most consequential extraction step in this note: the blog post
  alone describes the evaluator only as "scripts in a sandboxed
  environment," while the linked changelog entry names the exact mechanism
  (sandboxed Lua scripts calling keyword/regex/commit/diff searches) and
  establishes that the underlying feature shipped as part of release 7.3,
  months before this blog post republished it as a migration-specific use
  case. Readers relying only on the blog post would not know the scripting
  language or that the feature predates the post.
- The outbound EY newsroom link (Claim 1's source) was not independently
  fetched; that claim is graded `emerging` accordingly. The "Rethinking
  coding agent benchmarks" and CodeScaleBench companion links referenced in
  the sibling `blog-sourcegraph-jarmak-evaluate-on-your-codebase.md` note
  are unrelated to this post and were not revisited here.
- `confidence_overall` is set to `emerging`: one claim (Claim 4, the Lua
  evaluator mechanism) is independently corroborated by a first-party dated
  changelog entry and graded `settled` individually, but the post's central
  value proposition (cost savings, output quality improvement) rests
  entirely on unquantified assertions (Claims 2, 5, 6, 7, 9) with no
  before/after measurement anywhere in the source or its linked changelog
  pages. This is a thinner evidentiary base than the sibling
  `jarmak-evaluate-on-your-codebase.md` note (which reports a specific
  288-task quantified result) but stronger than a pure marketing claim,
  since the core mechanism was independently verified against dated,
  specific changelog entries rather than taken on the post's word alone.
- No contradiction issues filed; see Cross-References — Contradicts.
