---
source_url: https://martinfowler.com/articles/exploring-gen-ai/refactoring-economic-benefit.html
source_type: blog-post
title: "The Economic Benefit of Refactoring"
author: Giles Edwards-Alexander
date_published: 2026-07-30
date_extracted: 2026-07-31
last_checked: 2026-07-31
status: current
confidence_overall: emerging
issue: "#2356"
---

# The Economic Benefit of Refactoring

> A controlled, repeatable experiment on a 150K-line, entirely agent-authored
> Rust/TypeScript application shows that refactoring a 17,155-line monolithic
> data-access file into 19 smaller files cut the input-token cost of an
> identical representative change by 83% (159,564 → 27,360 tokens), because
> the saving comes from agents reading less code, not from there being less
> code overall.

## Source Context

- **Type**: blog-post (Martin Fowler's site, part of the "Exploring Gen AI"
  Thoughtworks technologist series)
- **Author credibility**: Giles Edwards-Alexander is CTO for Europe, Middle
  East and India at Thoughtworks, with over 25 years of engineering and
  technology leadership experience across mobile, AI, retail, fintech, and
  healthcare. He is the sole author, sole developer, and sole experimenter —
  this is a first-person practitioner report with a designed experiment, not
  peer-reviewed research, but it is unusually rigorous for a blog post: a
  controlled methodology, a full appendix of prompts used, and explicit
  acknowledgment of limitations (see Claim 9, Claim 10).
- **Scope**: Covers one experiment — refactoring one 17,155-line Rust data
  access layer in a single 150K-line application built entirely by Claude
  Code and Cursor — measuring input/output token cost of a fixed
  representative change across 15 refactoring steps. Does NOT cover: multiple
  codebases, other languages beyond this one Rust file (the app is also
  TypeScript and Terraform, untouched by the experiment), refactoring types
  other than the Fowler catalog moves applied here, or a rigorous token count
  for the refactoring effort itself (the author explicitly did not measure
  this — see Claim 9). It is a single case study on a greenfield app
  maintained by one developer, not a longitudinal or multi-team study.

## Extracted Claims

### Claim 1: A 150,000-line application, including a sophisticated web UI, ML/text analysis, background jobs, and full deployment automation, was built entirely by AI agents with no ongoing human code review

- **Evidence**: Author's first-person account of building his own application.
- **Confidence**: anecdotal
- **Quote**: "It's a sophisticated app: high-quality web UI with dynamic refresh and look-up, modals and auto-save, integrations to external systems, machine learning and text analysis, background jobs, and a proper environment setup with fully automated deployment. It's approximately 150,000 lines of code, primarily in Rust (~120 kLoC) with the remainder in TypeScript and Terraform. This was entirely written by agents. Mostly Claude Code, and some use of Cursor. I didn't read or review any of the code, except occasionally, out of interest."
- **Our assessment**: This is a striking scale claim (150K LOC, near-zero human review) that establishes the experiment's context: this is not a toy repo, and the code that grew unchecked (Claim 2) did so under realistic, largely unsupervised agent-authorship conditions. The "no ongoing review" detail matters for interpreting why the data access layer was allowed to reach 17,155 lines in the first place — nothing was catching it.

### Claim 2: Without human review, a data access layer grew unchecked to a single 17,155-line Rust file with no de-duplication, no internal query language, and minimal function/class extraction

- **Evidence**: Author's direct inspection after noticing an edit scroll past line 4,000 in the terminal.
- **Confidence**: anecdotal
- **Quote**: "Eventually, it reached 17,155 lines. In a single Rust file." … "Reviewing the code, there was no de-duplication, no internal language, limited extraction of functions, and very little extraction of classes. It did have a clear boundary with an interface to preserve. It was a great target for refactoring."
- **Our assessment**: This is a concrete, quantified instance of agent-authored code quality decay absent review — corroborating the general pattern (see Cross-References) that unsupervised agent output accumulates duplication rather than abstraction. The "clear boundary with an interface to preserve" detail is important: the author picked this file because refactoring could be behavior-preserving and verifiable, not because it was representative of worst-case decay.

### Claim 3: The experiment design (fresh sub-agent per measurement, discard-after-measure) exploits the fact that agents don't learn between sessions to get a clean before/after comparison a human-only study couldn't get

- **Evidence**: Author's explicit methodology description and six-step protocol.
- **Confidence**: emerging
- **Quote**: "Precisely because agents never learn this was now possible to run as an experiment. I could prompt a fresh agent to make exactly the same change after every refactoring stage. Unlike a human engineer, the experiment would not be tainted by learning from previous steps."
- **Our assessment**: This is a genuinely clever methodological point, not just a footnote — a human-only version of this study would be confounded by the engineer remembering the change from the previous step and typing it faster/more directly the second time. Agent statelessness, normally a liability (repeated re-supply of context every session — see `blog-addyosmani-intent-debt.md` Claim 5), is turned into a controlled-experiment asset here. Worth flagging in the guide as a case where agent statelessness is a feature for measurement, not just a cost to be managed.

### Claim 4: Refactoring the file (15 steps, no interface change) reduced input tokens for an identical representative task by 83%, from 159,564 to 27,360 tokens

- **Evidence**: Measured token counts (approximated via tiktoken on character counts, since the author reports Claude does not expose a reliable live token count) recorded at baseline and after each of 15 refactoring steps.
- **Confidence**: emerging (single-experiment measurement, not replicated, but with full raw data published in the article's results table)
- **Quote**: "Between the base line and the final refactoring, input tokens for the same task reduced from 159,564 to 27,360. A saving of 132,204 tokens, or 83%. And that saving is not a one-off. Every single change that touches the data access layer from this point forward now costs significantly less."
- **Our assessment**: This is the article's core, quantified finding and the reason it was triaged high-novelty — no other note in the corpus has a controlled before/after token measurement tied specifically to a refactoring intervention. The 83% figure is the single most citable number from this source. One caveat worth flagging in the guide: this is one representative task on one file in one codebase; the figure should be presented as "a demonstrated upper bound in a favorable case," not a general refactoring multiplier.

### Claim 5: The savings did not come from there being less code overall — total data-access-layer LOC stayed roughly flat (~49,673–50,359 total Rust lines) — but from the agent successfully narrowing its read scope to the smallest necessary subset of (now smaller, more numerous) files

- **Evidence**: The results table shows "Total Rust LoC" staying within a ~700-line band (49,673–50,359) across all 15 steps, while input tokens dropped 83%; author's direct interpretation plus a stated check against Claude's own file-read behavior.
- **Confidence**: emerging
- **Quote**: "This saving is because the agent has to read less code. But it is not because there is less code to read. The overall code in the data access layer as a whole has stayed fairly constant. Therefore to be able to bank this saving, the agent must be able to successfully identify the smallest subset of files necessary to read. The results make it appear this was happening. Reading the Claude Code thinking output and file read summaries as the change was being applied also indicates the sub-agent was successfully reading smaller and smaller sections of code each time."
- **Our assessment**: This is the mechanistic finding that matters most for the guide's context-engineering advice — it locates the saving specifically in *read locality*, not in code deletion. It reframes "refactor for token efficiency" from "write less code" (false — the code didn't shrink) to "organize code so an agent's context-gathering step can bound itself to a small, relevant slice" — which is squarely a context-budget claim, not a code-volume claim.

### Claim 6: Randomly splitting a large file into smaller files would likely not reproduce the saving; the effect is tied to the largest single file's line count specifically falling, which requires refactoring toward a "repeating core" structure, not arbitrary fragmentation

- **Evidence**: Author's direct comparison of the "total LoC" and "largest file LoC" columns in the results table, plus interpretive reasoning about why naive splitting would fail.
- **Confidence**: emerging
- **Quote**: "In other words, randomly cutting the file into smaller files is unlikely to help as much: even if each file were smaller, the agent would be forced to read through many files looking for the relevant code. While the step with the biggest effect happens at the end, the previous steps were refactorings to set up this saving. This was not planned. It was simply a result of how refactoring typically proceeds: local file changes to extract duplication, before breaking down into smaller files once a repeating core emerges."
- **Our assessment**: This is an important qualifier the guide should preserve alongside Claim 4's headline number — it forecloses a naive reading ("just split big files into smaller ones for token savings"). The author is explicit that the ordering (de-duplicate first, then split along the boundaries that de-duplication reveals) is what made the final split effective, and that this ordering emerged organically rather than being planned upfront.

### Claim 7: Refactoring reduced input (context-read) tokens but did not meaningfully reduce output (code-generation) tokens for the same task, even though output tokens are priced roughly 5x input tokens

- **Evidence**: The results table's "Output tokens per change" column stays in a narrow band (~1,700–2,500) across all 15 steps while input tokens fall 83%; author's direct observation.
- **Confidence**: emerging
- **Quote**: "The refactoring did not make the representative change smaller. The number of tokens produced when writing code was largely unaffected: the output tokens do not move very much. Those tokens are five times the price of the input tokens. But, there are a lot less of them. Are there refactorings that could be applied to reduce output token production? I need a more complex sample change to explore these questions."
- **Our assessment**: This is a valuable negative result the article reports honestly rather than papering over — refactoring-for-token-economics in this experiment is a read-cost story, not a write-cost story, and the author openly flags that reducing output tokens (the more expensive per-token category) is an open, unanswered question requiring a different experimental design (a more complex representative change).

### Claim 8: At Sonnet 5 pricing ($3/MTok), the per-change saving from this single refactoring was about 39.7 cents — modest per instance, but compounding on every future change that touches the same code

- **Evidence**: Author's direct cost calculation from the 132,204-token reduction at stated pricing.
- **Confidence**: emerging
- **Quote**: "How much of a saving? Assuming Sonnet 5 pricing at the time of writing of $3/MTok, 39.7 cents. Not a lot. Does it multiply? How will this play out across debugging? More complicated features? This is refactoring only one portion of the code base, can the whole code base be aggressively refactored to find savings everywhere? How much would those refactorings cost?"
- **Our assessment**: The author is appropriately modest about the absolute dollar figure and explicitly raises, without answering, the compounding/scaling questions (debugging costs, more complex features, whole-codebase refactoring, and the cost of the refactoring investment itself). The guide should present the 39.7-cent figure honestly as small per-instance, with the ROI case resting on repetition frequency (how many future changes touch this layer) rather than on the single-instance saving.

### Claim 9: Claude could not independently identify which refactorings to apply — a human had to direct it via an explicit refactoring plan — and was also mechanically unreliable at applying the refactorings it was told to make

- **Evidence**: Author's direct observation of the refactoring-plan-generation and refactoring-application phases, including a comparison between Claude Code and Claude.ai for plan quality.
- **Confidence**: emerging
- **Quote**: "Claude was not good at refactoring. If you read the prompt and the refactoring steps below, it's clear that the refactorings produced were directly in response to the prompt. Claude is unable to look at code, look at refactorings in general and work out which are suitable to apply: a human needs to actively guide it. … More anecdotally, Claude.ai was better than Claude Code. I used both interfaces to create the refactoring plan. Claude Code spotted extract function as the first step. Claude.ai went further and saw an entire client class to be extracted." … "It was also bad at applying them. The mechanical act of refactoring was performed by writing Python scripts using grep and sed. These scripts frequently got confused by indentation."
- **Our assessment**: This is a load-bearing limitation the guide should not omit alongside the headline 83% number — the token savings required active, expert-level human refactoring judgment (a Fowler-catalog-literate CTO applying Extract Class/Extract Function deliberately) plus a workaround (Python/grep/sed scripts) for the mechanical application step, because the agent's own file-editing was unreliable for large, indentation-sensitive rewrites. The result is not "point an agent at messy code and it self-refactors for token savings"; it is "an expert-directed refactoring plan, executed with tooling assistance, yields these token savings."

### Claim 10: The token cost of designing and running the refactoring itself was not rigorously measured; the author's own upper-bound estimate is 5 million tokens, and the process took about 8 hours, mostly unattended

- **Evidence**: Author's direct acknowledgment of a measurement gap plus a rough estimate from aggregate usage during the relevant time window.
- **Confidence**: anecdotal
- **Quote**: "Unfortunately, it didn't occur to me to perform a count of the tokens required to create and execute the refactoring plan until it was already complete. I've looked at my aggregate consumption across the time window where I was doing this work, including designing and running the experiment. I can't say how many tokens were required to perform the refactoring. The upper bound is five million, however." … "It took about eight hours to complete the entire experiment. This was mostly unattended. The only intervention was after six hours 40 minutes when it appeared to have finished, but had skipped that step and needed to be redirected."
- **Our assessment**: This is a genuine gap in the study's cost accounting, and the author is transparent about it rather than hiding it — the 5M-token upper bound includes plan creation (done twice), experiment design, and "various other tasks," so it cannot be cleanly attributed to the refactoring itself. Any guide treatment of this source's ROI claim should state plainly that the "investment" side of the refactoring ROI equation is not rigorously quantified here, only the "return" side (the 83% ongoing saving).

### Claim 11: The author frames the core economic principle as: spend tokens now on refactoring specifically to lower token consumption for all future work touching that code, and explicitly calls this "just the beginning," with harder open questions (larger-scope refactoring, continuous refactoring, comparing refactoring approaches) left for future work

- **Evidence**: Author's closing framing and stated next steps.
- **Confidence**: emerging
- **Quote**: "The goal of refactoring an agentic code base is to spend tokens now in refactoring to make token consumption for future work lower." … "This is just one experiment, on a significant application that is still greenfield and built and maintained by a single developer. But, I believe this is a potentially interesting first step. … It would be interesting to look at more complex changes, at wider refactoring, refactoring continuously, and even the relative value of different refactoring approaches. This is just the beginning."
- **Our assessment**: The author's own framing is appropriately provisional — a single-developer, single-codebase, single-refactoring-target pilot, explicitly offered as a first step rather than a general result. The guide should cite this as the clearest one-sentence statement of the economic principle (tokens-now-for-tokens-later), while treating generalizability (team codebases, non-greenfield legacy code, other languages) as unverified.

## Concrete Artifacts

### Experimental protocol (verbatim, six steps)

```
Create an overall refactoring plan, following strict refactoring discipline.
Craft a representative change, described in a single prompt.
Establish a baseline cost of change: in a sub-agent, execute that prompt,
  including asking the sub-agent to report token consumption.
Throw away the change.
In a loop:
  Apply a single step of the overall refactoring.
  In a sub-agent, execute exactly the same change receiving the token cost
    of the change.
  Throw away the change.
Record all token costs, time to execute the change, and lines of code after
  each step of the refactoring, including the baseline.
```
— martinfowler.com, "The Economic Benefit of Refactoring" (Edwards-Alexander, 2026-07-30)

### Results table (verbatim data, selected columns)

```
Step                          | Largest file LoC | Total Rust LoC | Input tokens | Output tokens | Time (s)
Baseline                      | 17,155            | 50,359         | 159,564      | 1,705          | 342
Step 1 (FirestoreClient)      | 16,706            | 49,910         | 155,205      | 1,723          | 530
Step 2 (extract_doc_id, ...)  | 16,562            | 49,766         | 159,227      | 2,105          | 574
Step 5 (value ctors)          | 16,469            | 49,673         | 171,251      | 2,036          | 1,353
Step 7 (queries.rs)           | 15,670            | 49,678         | 151,850      | 1,800          | 587
Step 8 (traits.rs)            | 13,845            | 49,712         | 132,558      | 1,723          | 446
Step 10 (codec.rs)            | 12,846            | 49,725         | 131,871      | 1,750          | 540
Step 12 (store/ split)        | 9,269              | 49,754         | 104,080      | 2,050          | 490
Step 14 (complete fake_store) | 7,225              | 49,757         | 107,205      | 2,453          | 523
Step 15 (store/ split)        | 3,695              | 49,812         | 27,360       | 2,113          | 454
```
— martinfowler.com, full 15-row table in original article; reproduced here as a
representative subset showing the correlation between falling "largest file LoC"
and falling input tokens, while "Total Rust LoC" stays roughly flat.

### The representative change prompt (verbatim, appendix)

```
You are working in the Rust project at ~/dev/your-project-name.

Add a new ItemWatchStore public async trait to the Firestore layer,
following existing patterns exactly. The trait must have three methods:
  async fn watch_item(&self, item_id: &str, user_id: &str) -> Result<()>
  async fn unwatch_item(&self, item_id: &str, user_id: &str) -> Result<()>
  async fn watched_items_for_user(&self, user_id: &str) -> Result<Vec<String>>

Watches are stored in a item_watches Firestore collection. Each document has
fields: itemId (string), userId (string), createdAt (timestamp). There is no
Rust struct for a watch record — the methods return Vec<String> (item ids).

Implement the trait for both FakeStore (using an in-memory
Vec<(String, String)> field added to FakeStoreInner) and FirestoreStore
(using the same HTTP patterns used for other store impls in this file).

At the very end of your response, output exactly this JSON block
(fill in real values):
{
  "files_read": [{"path": "src/firestore.rs", "chars": 123456}, ...],
  "response_chars": 7890
}

Do NOT commit the change. Stop after writing the code.
```
— martinfowler.com, appendix, "The representative change"

### Refactoring steps applied (attributed to Fowler's Refactoring catalog)

```
1. Extract Class: FirestoreClient (§7.5) + Extract Function ×4 (§6.1)
   — separates Firestore HTTP transport from domain query orchestration
   — est. ~1,200 line savings in FirestoreStore; FirestoreClient adds ~120 net
2. Extract Function: extract_doc_id, new_link (§6.1) — ~500 lines
3. Extract Function: link-query pipeline helpers (§6.1) — ~200 lines
4. Extract Function: FakeStore link predicates (§6.1) — ~120 lines
5. Replace Inline Code: Firestore value constructors — ~80 lines
6. Extract Class: FieldsBuilder — ~500-600 lines
7. Move Function: extract queries.rs — ~800 lines
8. Move Function: extract traits.rs — ~1,900 lines
9. Move Function: split traits/ by domain (300-650 line files)
10. Move Function: extract codec.rs — ~500 lines
11. Move Function: extract fake_store.rs — ~4,700 lines
12. Move Function: split store/ implementations (120-650 line files)
13. Move Function: co-locate tests (~2,000 lines added, 200-700/file)
14-15. Complete fake_store.rs / store split completion
```
— martinfowler.com, appendix, "Refactoring steps"; step count does not exactly
match the measured-steps table because the author notes the single most
valuable refactoring (splitting the store into sub-files) was skipped on the
first pass and had to be reapplied as two follow-up steps.

## Cross-References

- **Corroborates**: `failure-thailandjohn-schema-refactor-context-collapse.md`
  (a large, unbounded schema-rename refactor exceeded the model's context
  window and triggered a hallucination "death spiral"). That failure report
  and this experiment point at the same underlying mechanism from opposite
  directions: ThailandJohn's failure happened because a large-scope
  refactor was attempted as one big, context-overloading operation, while
  Edwards-Alexander's success came from doing the opposite — 15 small,
  individually-testable, behavior-preserving steps, each verified before
  moving on. This experiment is a concrete illustration of the discipline
  that would have prevented ThailandJohn's failure: bound each step so an
  agent's read/write footprint stays small enough to reason about reliably.

- **Extends**: `blog-simonwillison-james-shore-maintenance-costs.md` (Claim 6:
  "Teams must invest as much effort in reducing maintenance costs as in
  increasing coding speed"). This source is a concrete, quantified
  demonstration of exactly that prescription in action — Edwards-Alexander
  deliberately invested in refactoring and measured an 83% reduction in
  ongoing token cost for future work on that code. Important caveat for the
  guide: the two sources measure different cost dimensions. Shore's claims
  (Claim 3, Claim 5) concern human/model-measured *maintenance cost* proxies
  such as cognitive complexity and static-analysis warnings (per
  `paper-miller-speed-cost-quality.md`), while this source measures *agent
  input-token cost* for a fixed task. A codebase could plausibly see token
  costs fall while cognitive complexity for human maintainers stays flat or
  worsens (or vice versa) — the two metrics are related but not shown to be
  the same thing in either source. This is a conditioning-variable
  difference in what "maintenance cost" means, not a contradiction between
  the sources, so no contradiction issue is filed.

- **Extends**: `blog-addyosmani-intent-debt.md` (Claim 5: agent statelessness
  means un-externalized intent is re-paid every session). This source's
  Claim 3 shows the same statelessness property (agents don't learn between
  sessions) being deliberately exploited as a methodological asset — a clean
  controlled experiment — rather than only being a cost to manage. Worth
  presenting together as two faces of the same property: statelessness is a
  tax when it forces re-supplying context, and a tool when it enables
  before/after measurement free of learning effects.

- **Contradicts**: None identified that rises to a contradiction issue per
  MINER.md §4a's bar (see the Shore discussion above — treated as a metric
  scope difference, not a material disagreement leading to different guide
  advice).

- **Novel**: The controlled, before/after token-count experiment tied
  specifically to a refactoring intervention is new to the corpus — no
  existing source note has measured input-token cost across a step-by-step
  refactoring with a held-constant representative task. The specific
  mechanism claim (savings come from narrowed read-locality, not reduced LOC
  — Claim 5) and its explicit rebuttal of naive file-splitting (Claim 6) are
  also new. The observation that agent statelessness can be exploited as an
  experimental control (Claim 3) is a novel framing not present elsewhere in
  the corpus.

## Guide Impact

- **Chapter 04 (Context Engineering)**: Add this experiment to the "Context
  as Budget" section as concrete quantitative evidence that codebase
  organization is itself a context-budget lever, not just prompt/session
  hygiene. Specifically cite Claim 5 (savings come from narrowed read-scope,
  not less code) and Claim 6 (the effect requires de-duplicating before
  splitting, not arbitrary fragmentation) as the mechanism, and Claim 4's
  83% figure as the demonstrated result. This is a distinct, complementary
  lever to the chapter's existing session-segmentation and compaction
  guidance — refactoring reduces the *per-task* context floor, while the
  existing content addresses *within-session* budget management.

- **Chapter 02 (Harness Engineering)**: Add refactoring discipline as an
  explicit "Engineering Standards" recommendation for agent-authored
  codebases, citing Claim 2 (unreviewed agent output accumulated to a
  17,155-line undifferentiated file) as the failure mode this guards
  against, and Claim 9 as an important caveat — the guide should be explicit
  that this requires a human directing specific, catalog-referenced
  refactorings (Extract Class, Extract Function, Move Function per Fowler),
  not a generic "ask the agent to refactor" step, since Claim 9 shows Claude
  could not independently identify which refactorings were worth applying.

- **Chapter 00 (Principles)**: Consider citing Claim 11's framing ("spend
  tokens now in refactoring to make token consumption for future work
  lower") as a specific, quantified instance of an economic principle for
  agent-native codebases — tokens are a real, measurable operating cost, and
  refactoring investment has a demonstrated (if narrowly-scoped) payoff
  against that cost, analogous to how the guide already treats context and
  time as budgeted resources.

## Extraction Notes

- Fetched the article twice: once via WebFetch (AI-summarized) and once by
  downloading the raw HTML directly (`curl` with a browser user agent) and
  stripping tags with a Python script, to verify every quote above against
  the unprocessed source text rather than the AI-summarized version. All
  quotes in this note were checked against the raw-HTML extraction.
- The full results table has 15 rows across 6 columns; the Concrete
  Artifacts section reproduces a representative subset (baseline plus every
  other step, prioritizing the ones with the largest LoC/token movement) to
  keep the note readable rather than transcribing all 90 cells. The 83%
  headline figure (Claim 4) and the flat-total/falling-largest-file pattern
  (Claim 5, Claim 6) are both directly checkable against the reproduced
  subset.
- The article's appendix lists 15 refactoring-plan steps but the measured
  results table has different step boundaries, because (per the author) the
  single most valuable refactoring was skipped on the first pass and applied
  as two follow-up steps instead — the Concrete Artifacts section preserves
  this discrepancy rather than silently reconciling it, per the author's own
  explanation.
- No sub-pages were followed. The article is self-contained (a single essay
  with an appendix on the same page); it does not link out to substantive
  external sources beyond the Thoughtworks "Exploring Gen AI" series index
  and Martin Fowler's own "Refactoring" book, neither of which needed
  separate fetching for this extraction.
- Checked all cross-referenced source notes' claim numbers directly against
  their files before citing them (see Cross-References): `failure-thailandjohn-schema-refactor-context-collapse.md`,
  `blog-simonwillison-james-shore-maintenance-costs.md` (Claims 3, 5, 6),
  `blog-addyosmani-intent-debt.md` (Claim 5).
- Considered filing a contradiction issue against
  `blog-simonwillison-james-shore-maintenance-costs.md` (Shore's Claim 5:
  "coding agents increase maintenance costs... not decrease"). Decided
  against it: the two sources measure different things (token cost for a
  fixed task vs. cognitive-complexity/static-analysis proxies for human
  maintenance burden), and Shore's own Claim 6 explicitly prescribes the
  kind of deliberate investment this source demonstrates — so this reads as
  Shore's prescription in action, not a disagreement with the value of
  refactoring. Documented as a scope caveat in Cross-References instead, per
  MINER.md §4a's "differs only in context" exclusion.
