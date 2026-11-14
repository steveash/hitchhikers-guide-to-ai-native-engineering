---
source_url: https://latent.space/p/building_legal_agents_when_you_can_t_see_the_data_-_jacob_lauritzen_cto_of_legora/
source_type: discussion
title: "Building Legal Agents When You Can't See the Data - Jacob Lauritzen, CTO of Legora"
author: Jacob Lauritzen (guest, CTO of Legora) / swyx and Basil Chatha (hosts), Latent Space Podcast
date_published: 2026-11-02
date_extracted: 2026-11-14
last_checked: 2026-11-14
status: current
confidence_overall: anecdotal
issue: "#4728"
---

# Building Legal Agents When You Can't See the Data - Jacob Lauritzen, CTO of Legora

> A vendor CTO describes how Legora evaluates and operates a production agent when customer confidentiality means engineers can never read traces: RL-style "worlds" built by engineers and lawyers, failure-type clustering over paraphrased data, and a model-upgrade-driven citation jump from about 70% to 99%.

## Source Context

- **Type**: discussion (67-minute podcast interview; page carries show notes and chapter list, with a linked VTT transcript)
- **Author credibility**: Lauritzen is CTO of Legora, a fast-growing legal-AI company, so he is a first-hand practitioner. All numbers are self-reported by a vendor and unaudited. The hosts are Latent Space (swyx) and Basil Chatha of Forward Deployed.
- **Scope**: Covers evals and product metrics under data-visibility limits, model choice and routing, harness and retrieval design, Tabular Review and Lists, legal engineers vs forward-deployed engineers, and Azure/vendor privacy posture. It also covers business topics (law-firm partnerships, billable hour, junior lawyers) that are not extracted here. The transcript has no speaker labels and its timestamps are inconsistent, so attributions and times are approximate.

## Extracted Claims

### Claim 1: Legora builds evals as full "worlds" modeled on how lawyers work, like RL environments
- **Evidence**: Interview description of an eval team of engineers and lawyers building end-to-end scenarios (for example a due diligence over a large data room), with a target output defining red flags, what to omit, and conciseness; each subtask (drafting a report, finding red flags) is scored. The show notes describe a "10,000-file data room."
- **Confidence**: anecdotal
- **Quote**: "So we have different basically, like, worlds, like RL environments essentially"
- **Our assessment**: A concrete example of scenario-level (not unit-level) evals with domain-expert-authored success criteria. No environment count, scoring method, or inter-rater data is given, so this is a pattern to note, not a validated method.

### Claim 2: The eval team is mixed: about three engineers plus three lawyers, supported by a wider pool of "legal engineers"
- **Evidence**: Stated team composition. The show notes say three engineers and three lawyers build the test environments. Lauritzen says legal engineers are ex-Big-Law people who also help with evals, and that they are the hardest role to hire.
- **Confidence**: anecdotal
- **Quote**: "there's, like, three engineers and, like, three lawyers right now"
- **Our assessment**: Credible and consistent with domain-expert-in-the-loop eval practice. The show notes' "100 legal engineers" figure belongs to the wider legal-engineer pool, not the eval team.

### Claim 3: Legora tracks every model by practice area and task, because releases often improve some areas and regress others
- **Evidence**: Description of a "big heat map" of model performance by practice area, used to decide routing.
- **Confidence**: anecdotal
- **Quote**: "a lot of model releases where they improve some and, and regress in others"
- **Our assessment**: Supports per-slice (not aggregate) regression tracking at model upgrade time. Matches the vendor-reported gap between ~40% task-specific and ~3% all-task average improvement in `blog-openai-legora-financial-statement-tie-out.md` Claim 6.

### Claim 4: Legora de-prioritized heavy evals because "all models just got better", then saw citation accuracy move from about 70% to about 99% in one model release with no Legora change
- **Evidence**: Lauritzen's anecdote (~11:03 chapter: "When evals didn't seem worth it and one release took citations from 70% to 99%"). The transcript does not say what changed in the model or harness; it is a citation-formatting problem.
- **Confidence**: anecdotal
- **Quote**: "It's just like we did nothing and, like, great."
- **Our assessment**: A single vendor-reported number, with the cause unexplained. It is a useful counter-example to "evals first" advice: model upgrades can silently fix (or break, see Claim 3) behaviors. It should be cited as an anecdote and not as a general rate of improvement. Mixed signal: the same team later invested in an evals team (Claims 1-3).

### Claim 5: Without trace access, Legora relies on standard product metrics, feature-flag comparisons, and cheap-LLM online evals
- **Evidence**: Description of metrics (active use, hours spent, renewals), feature-flag rollout comparison, and online evals with a cheap LLM.
- **Confidence**: anecdotal
- **Quote**: "we can't look at any traces, basically."
- **Our assessment**: Honest statement of the constraint. The trade-off is that the team has coarse signals about what users actually do ("I have no idea what people are actually doing with it").

### Claim 6: Failure clustering into roughly 10-20 types over paraphrased or anonymized examples substitutes for reading raw traces
- **Evidence**: Lauritzen describes using an LLM to paraphrase, treating paraphrase as a spectrum, choosing the safest option, and assuming failure modes fall into about ten or twenty categories. The notes say the approach is still being refined.
- **Confidence**: anecdotal
- **Quote**: "the failure modes are probably these ten or twenty"
- **Our assessment**: The "10-20" figure is an assumption, not a measured result. Lauritzen himself notes that stripping names may not be enough for privacy ("If you just remove the names, then that's may-may-maybe not fine."), so paraphrase-based pipelines carry residual leakage risk.

### Claim 7: For a customer-reported problem, Legora asks for anonymized documents to reproduce it
- **Evidence**: Interview description (~1:00:16 chapter, "Getting anonymized examples"). The hosts joke about buying a law firm for its data; Lauritzen notes data ownership is unclear.
- **Confidence**: anecdotal
- **Quote**: "Can you like anonymize the documents"
- **Our assessment**: A pragmatic escalation path: customer-initiated, per-incident data sharing instead of standing access.

### Claim 8: Legora resisted a model picker for years, ultimately added one, and is unsure it will stay; model choice is meant to be the platform's job
- **Evidence**: Interview statements; the picker currently offers five options including Fable, Opus and Astra; some internal tools (for example Tabular Review) route to different models; heavier models consume usage credits faster.
- **Confidence**: anecdotal
- **Quote**: "I'm not sure if that's gonna stay there always, to be honest."
- **Our assessment**: Useful as a product-design datapoint on exposing model choice to non-technical users. The shape of the argument is "lawyers can't know which tier a task needs."

### Claim 9: Models already do about 60% of legal work well; the rest needs smarter models
- **Evidence**: Lauritzen's estimate (show notes: "models already do about 60% of legal work well").
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: An unmeasured intuition, not a benchmark. Do not cite as a capability measurement.

### Claim 10: Fable and Opus are "extremely chatty" for drafting; concision is hard to prompt in; Astra is preferred for drafting
- **Evidence**: Lauritzen's model-comparison opinion (~56:20-57:05), with a mention that Legora has discussed it with the labs.
- **Confidence**: anecdotal
- **Quote**: "extremely chatty"
- **Our assessment**: Task-specific subjective preference by one vendor. It reinforces per-task routing (Claim 8) but is not evidence of general model quality.

### Claim 11: Drafting a long contract is essentially a search problem, and Lauritzen advises against default embeddings
- **Evidence**: Explanation that drafting requires locating the right precedent clause from similar deals, and that "similar" has many meanings. The chapter list lists "Why Jacob advises against default embeddings" (~1:01:53); late-interaction retrieval is not currently used but a team member pushes for it, with "loads of low-hanging fruit" in the harness before training.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Plausible framing that retrieval quality bounds output quality. The embeddings advice is listed in the chapters but its reasoning was not recovered from the transcript portion read, so it should not be cited beyond the chapter title.

### Claim 12: Scaffolding such as MapReduce over chunks keeps being revised as models improve; chunking loses nuance across chunks
- **Evidence**: Discussion at ~58:19 of MapReduce vs one large context window for million-token contracts. Per the notes, a host said moving from MapReduce to whole-document context performed better, and Lauritzen said long-document edits remain hard and relevant passages can span chunks.
- **Confidence**: anecdotal
- **Quote**: "the scaffolding that we build around as models change"
- **Our assessment**: Consistent with the broader theme that harness scaffolding is perishable. Anecdote only, without measurements.

### Claim 13: Citations are enforced structurally: every claim links to a source (bounding box in the PDF), traceable through layers, yet lawyers do not always check them
- **Evidence**: Description of the citation system (~57:03-58:19), including tracing from agent output down to a Tabular Review cell.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: A provenance-by-construction design. The admission that checking is uneven mirrors the coding analogy the speaker draws (some engineers "just send agents").

### Claim 14: Privacy posture: everything runs on Azure, and ElevenLabs is avoided to keep the data-processing agreement to few vendors
- **Evidence**: Interview statements (~28:42, ~30:55): early law-firm customers trusted Microsoft already; vendors that offer many services under one agreement (OpenAI, Gemini) are valuable even when not state of the art; on-prem demands have "completely disappeared".
- **Confidence**: anecdotal
- **Quote**: "we can't trust them with any of our data."
- **Our assessment**: A concrete vendor-minimization practice. The quoted line's referent (other parties) is ambiguous in a transcript without speaker labels, so use it with care; the sub-processor-count argument is the more reliable takeaway.

### Claim 15: Tabular Review and Lists are agent-facing primitives: a document-by-question grid, with agents creating lists and lists triggering agents
- **Evidence**: Description of a grid run over thousands of files (up to about a million cells), with a first-10-rows test before the full run; Lists work like a Notion/Linear database with triggers; the Slack intake bot feeds a list.
- **Confidence**: anecdotal
- **Quote**: "agents can create lists, and lists can create agents"
- **Our assessment**: The "run the first 10 rows" step is a cheap verification pattern worth noting for batch agent jobs.

### Claim 16: Legal engineers configure the product (no code); forward-deployed engineers write production code; larger clients get both
- **Evidence**: Role definitions and onboarding model.
- **Confidence**: anecdotal
- **Quote**: "Legal engineers configure the product as a power user would."
- **Our assessment**: A two-tier customer-facing model that differs from Sierra's single "agent engineer" role; see Cross-References.

## Concrete Artifacts

```
Per Lauritzen / Latent Space show notes (https://latent.space/p/building_legal_agents_when_you_can_t_see_the_data_-_jacob_lauritzen_cto_of_legora/):
- "three engineers and three lawyers build test environments modeled on customers' work, much like the 'worlds' used in reinforcement learning"
- "A citation problem where the model got it right 70% of the time, then 99% after one release. Legora didn't have to change anything."
- Chapters: 9:18 simulated worlds and a 10,000-file data room; 26:12 product metrics when you can't read the traces; 27:41 paraphrasing traces and narrowing failures down to 10 or 20 types; 58:19 MapReduce or one big context window
```

Observed eval/ops loop (our synthesis of the interview, not a source diagram):

1. Author scenario "worlds" (engineers + lawyers) with target outputs and per-subtask scoring.
2. Track each model release per practice area/task (heat map) to catch regressions.
3. In production, use product metrics, feature flags, and cheap-LLM online evals; no trace reading.
4. For failures, cluster paraphrased examples into about 10-20 types; for customer-reported issues, request anonymized documents.

## Cross-References

- **Corroborates**: `blog-openai-legora-financial-statement-tie-out.md` Claim 6 (Legora's proprietary BAR benchmark; large task-specific improvement vs ~3% average) is consistent with Claim 3 here that model releases move different areas unevenly.
- **Contradicts**: None filed. The "evals weren't worth it" statement (Claim 4) is in tension with `blog-hamel-eval-smell.md` Claim 1 (hard-to-eval is a product smell), but the same speaker later describes a dedicated eval team, so this is a stage-dependent view and not an opposing position; no contradiction issue was filed.
- **Extends**: `blog-anthropic-agent-observability-claude-platform.md` Claim 5 (trace content defaults to metadata only) and Claim 7 (real traces become evals) describe a trace-rich route; this source describes the opposite constraint, where traces are never readable. `blog-latentspace-meurer-agent-engineer-fde.md` Claim 4 (customer-specific work lives at the orchestration layer) pairs with the legal-engineer/FDE split in Claim 16.
- **Novel**: Evals under a no-trace-access constraint (paraphrase plus failure-type clustering, customer-supplied anonymized repro documents); vendor-minimization as a deliberate privacy choice; "agents create lists, lists start agents" as a coordination primitive.

## Guide Impact

- **Chapter 03 (verification)**: Add a short example of scenario-level "world" evals authored by domain experts plus engineers, and of per-slice model-release tracking, citing Claims 1 and 3. Cite the 70%→99% citation figure only as a single practitioner anecdote (Claim 4) that model upgrades can change behavior without harness changes.
- **Chapter 06 (security)**: Add a subsection or sidebar on observability when data is customer-owned: no-trace operation, paraphrase/cluster pipelines (with the leakage caveat in Claim 6), and per-incident anonymized sharing (Claim 7); and on vendor minimization (Claim 14).
- **Chapter 02 (harness engineering)**: Cite Claims 11-12 for "retrieval quality bounds drafting quality" and "scaffolding around models is perishable". Treat as anecdotal.
- **Chapter 05 (team adoption)**: Cite Claim 16 as a legal-engineer (configure) vs FDE (code) split and as a counterpoint to Sierra's single-role model.

## Extraction Notes

- The page itself holds show notes, a chapter list and a link to a VTT transcript. The transcript URL returned a Cloudflare challenge to curl, so I read it through a fetch tool that summarizes pages. That tool returns short snippets and paraphrase rather than the raw file, so the quotes above are short fragments taken from its output and **have not been confirmed against the raw transcript**. The Assayer should spot-check them against the VTT. The last ~9,000 characters of the transcript were not read.
- Quotes in the Artifacts block are verbatim from the page show notes.
- The transcript has no speaker labels; the Lauritzen attributions are inferred from context. The fetch tool rendered the guest's surname as "Lauridsen" and the company as "Lagora"; this note uses the page's spelling.
- The triage comments suggest the transcript might say what changed in the citation fix. It does not appear to.
- Claims 9, 11 and 13 have no verbatim quote because I could not recover an exact fragment.
- No contradiction issue was filed; see Cross-References.
