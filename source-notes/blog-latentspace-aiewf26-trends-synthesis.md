---
source_url: https://www.latent.space/p/aiewf26trends
source_type: blog-post
title: "5 Trends That Defined AI Engineering at World's Fair 2026"
author: Richard MacManus (Latent Space / AINews)
date_published: 2026-07-14
date_extracted: 2026-07-30
last_checked: 2026-07-30
status: current
confidence_overall: emerging
issue: "#2328"
---

# 5 Trends That Defined AI Engineering at World's Fair 2026

> A post-conference trend synthesis distilling AIEWF 2026 into five
> cross-cutting themes — harness/systems over agents, loop engineering as
> the outer-loop/inner-loop control pattern, forward deployed engineers as
> the enterprise adoption vehicle, coding agents replacing IDEs, and skills
> as a portable unit of agent knowledge — rather than day-by-day dispatch
> coverage.

## Source Context

- **Type**: blog-post — a retrospective, cross-conference trend-synthesis
  piece (Latent Space's AINews), published roughly two weeks after AIEWF
  2026 concluded, distinct from the three same-day dispatches already in
  this corpus (`blog-latentspace-aiewf-loops-software-factories-dispatch.md`,
  `blog-latentspace-aiewf-autoresearch-agency-dispatch.md`,
  `blog-latentspace-aiewf-loops-debate-dispatch.md`).
- **Author credibility**: Richard MacManus is the named byline; Latent
  Space (swyx) is a `trusted-feed` source in this repo's scanning
  configuration and MacManus attended AIEWF 2026 in person across all
  three of its days (per the dispatch notes above). This piece is his
  synthesis after the fact rather than live reportage — it draws on
  talks/interviews he covered directly, plus at least one work he did not
  attend live (Lilian Weng's essay, cited and paraphrased, not delivered
  as a conference talk).
- **Scope**: Covers five trends the author identifies as defining AIEWF
  2026: (1) systems/harnesses over agents, (2) loop engineering as a
  control pattern, (3) Forward Deployed Engineers as the enterprise
  adoption vehicle, (4) coding agents replacing IDEs, (5) agent skills as
  portable knowledge. Does not include a full talk-by-talk transcript,
  session recordings, or attendance/audience data — it is thematic
  synthesis and citation, most of it already covered in more depth
  elsewhere in this corpus (see Cross-References).

## Extracted Claims

### Claim 1: The industry's center of gravity has shifted from building the agent itself to building the system/harness around it — Lilian Weng's new essay is cited as the definitive statement of this shift
- **Evidence**: MacManus paraphrases Lilian Weng's 2026 essay "Harness Engineering for Self-Improvement," contrasting it with her earlier 2023 "LLM Powered Autonomous Agents" essay, to frame the trend.
- **Confidence**: emerging
- **Quote**: "Rather than focusing on the agent itself, Weng argues that the system surrounding the model has become just as important: the harness that manages workflows, context, permissions, evaluation, persistent state and continuous improvement."
- **Our assessment**: This is a secondary citation, not a direct quote from Weng — her own essay is independently mined in this corpus as `blog-lilianweng-harness-engineering-rsi.md` (see Claim 1 there: harness as orchestration layer). MacManus's framing is a faithful summary of Weng's central claim but adds no new evidence beyond what the primary source already provides; its value here is as an indicator that this framing reached mainstream AI-engineering discourse as a named "trend," not just one essay's argument.

### Claim 2: "Loop engineering" is identified as a second defining trend, structured around an inner loop (execution) and an outer loop (oversight/maintenance)
- **Evidence**: MacManus cites Roland Gavrilescu (Introspection) defining the inner-loop/outer-loop split, drawn from an interview Latent Space conducted separately.
- **Confidence**: emerging
- **Quote**: "You can think of the system as having an inner loop and an outer loop. The inner loop is the primary system interacting with users and performing the work. Autoresearch is more concerned with the outer loop: another system that studies and maintains the primary system."
- **Our assessment**: This is a verbatim restatement of Claim 2 in `blog-latentspace-gavrilescu-autoresearch-introspection.md` ("Autoresearch's 'inner loop' is the primary production system serving users; the 'outer loop' is a separate system of agents that studies and maintains the primary system"). No new information — corroborating evidence that this framing was treated as one of the conference's headline ideas rather than a single speaker's idiosyncratic framing.

### Claim 3: Human oversight is explicitly located in the outer loop, even as agents take over more of the inner loop's execution — a structural relocation of responsibility rather than its removal
- **Evidence**: MacManus quotes Addy Osmani directly on this division of labor.
- **Confidence**: emerging
- **Quote**: "agents can run much more of the inner execution loop, but that outer loop is still engineering."
- **Our assessment**: Consistent with — and likely drawn from — Osmani's own posts already in this corpus (`blog-addyosmani-own-the-outer-loop.md` Claim 2: "Agents run the inner loop; engineers own the outer loop — a structural relocation of accountability, not a reduction of human work"; `blog-addyosmani-loop-engineering.md`). The synthesis piece adds no new argument here, just confirms Osmani's framing was picked up as conference-wide vocabulary.

### Claim 4: A live counter-narrative at the conference held that loop/software-factory claims are still unproven and may not hold up over the following year
- **Evidence**: MacManus quotes Geoffrey Huntley (creator of the "Ralph Loop" technique) voicing skepticism about the durability of loop/factory claims.
- **Confidence**: anecdotal
- **Quote**: "My biggest concern is that this time next year at the conference, we're going to see a whole bunch of folks saying, our factories failed, our loops failed. These are things that we are still yet to figure out."
- **Our assessment**: Notably, this is a skeptical/hedging quote embedded inside a trend-synthesis piece that otherwise reads as fairly triumphalist about loops and systems. It's worth keeping as a marker that even proponents (Huntley coined a named loop pattern) flagged loops/factories as an open, unresolved bet rather than a settled win — a useful caveat for any guide section that cites loop engineering as established practice.

### Claim 5: Forward Deployed Engineers (FDEs) are identified as the enterprise adoption vehicle for agentic AI, doing orchestration work to keep an organization's "agentic ecosystem" functioning
- **Evidence**: MacManus paraphrases the FDE role generally, then quotes Natalie Meurer (Sierra) on the orchestration burden it carries.
- **Confidence**: emerging
- **Quote**: FDEs "work directly with organizations to implement AI capabilities," and enterprises need to "maintain everything its agentic ecosystem is capable of doing."
- **Our assessment**: The FDE framing and the Meurer quote both restate ground already covered in depth by `blog-latentspace-meurer-agent-engineer-fde.md` (see Claim 4: "Most customer-specific work in agent engineering happens at the orchestration layer, not inside the underlying models") and `blog-thebatch-fde-agents-aiact-issue355.md` (Claim 1). No new evidence; the synthesis value is that FDE/agent-engineering was independently judged conference-wide "trend" status rather than a single company's talking point.

### Claim 6: Coding agents (Claude Code, Codex, Gemini CLI, Cursor, Warp) are now positioned as replacements for the IDE workflow itself, not as autocomplete additions to it
- **Evidence**: MacManus names the specific tools and describes their expanded capability set, contrasting explicitly with 2023-era GitHub Copilot-style autocomplete.
- **Confidence**: emerging
- **Quote**: These agents "can typically understand a broader objective, explore a codebase, modify multiple files, run tests, debug failures and iterate on their own work before presenting it back to the developer" — versus 2023's "GitHub Copilot completing the next few lines of code" with developers "writing almost everything themselves, using AI as an intelligent autocomplete."
- **Our assessment**: This before/after framing (autocomplete → autonomous multi-file iteration) is a clean, quotable one-paragraph summary of a shift this corpus otherwise documents piecemeal across many individual Cursor/Claude Code/Devin source notes. Useful as a citable "state of the industry, mid-2026" anchor point even though none of the underlying capability claims are new.

### Claim 7: Agent "skills" — encoded, portable procedures/best-practices — are named as the fifth defining trend, adopted across multiple platforms beyond Anthropic's original implementation
- **Evidence**: MacManus cites Addy Osmani's definition of skills, Andrew Qu's framing of skills as "portable, on-demand knowledge" (Vercel), and Philipp Schmid's presentation on skills for "agents without code" (Google DeepMind), noting Anthropic introduced agent skills to Claude in October 2025.
- **Confidence**: emerging
- **Quote**: Osmani's definition, as quoted in the piece: skills "encode the workflows, quality gates, and best practices that senior engineers use when building software." Andrew Qu's framing: skills are useful "as portable, on-demand knowledge."
- **Our assessment**: The Qu quote restates ground already covered by `blog-latentspace-vercel-andrew-qu-eve.md` (Claim 9: "Skills exist because models often contain outdated information about a company's own product, and a skill can forward-correct that"). The cross-platform adoption claim (Anthropic → Vercel → Google DeepMind) is the one piece of genuinely new information this note contributes: it's the first source in this corpus to explicitly name Google DeepMind (via Philipp Schmid) as adopting the skills pattern, alongside Vercel and GitHub (`docs-github-copilot-agent-skills-cli.md`).

### Claim 8: Paul Bakaus argues most existing skills are poorly built and advocates for "skill engineering" as a discipline distinct from writing skills themselves
- **Evidence**: MacManus paraphrases and directly names Bakaus's proposed discipline.
- **Confidence**: anecdotal
- **Quote**: "Bakaus argued that most skills...and he advocates for 'skill engineering' as a discipline in its own right."
- **Our assessment**: This is a genuinely novel data point for this corpus — no existing source note documents "skill engineering" being proposed as a named discipline analogous to "prompt engineering" or "context engineering." It's a single practitioner's framing relayed secondhand (Bakaus is not directly interviewed in this piece; his own talk/interview is not separately mined here), so treat as anecdotal until a primary source surfaces.

### Claim 9: The overall arc across all five trends is that AI engineering has matured from proof-of-concept experimentation toward production-scale systems, shifting the central conversation to reliability, orchestration, and integration
- **Evidence**: MacManus's own closing synthesis across the five trends, not attributed to any single speaker.
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase — this is the author's own framing synthesis, not a quoted passage)
- **Our assessment**: This is the article's thesis statement rather than an independently verifiable claim. It's a reasonable read of the other four trends (harness focus, loop control patterns, FDE-driven enterprise rollout, coding-agent maturity, skills standardization) taken together, but it is MacManus's editorial synthesis, not new evidence in itself.

## Concrete Artifacts

```
Named speakers/practitioners by trend section (per source, as relayed by MacManus):

Trend 1 (Systems over Agents): Lilian Weng, Romain Huet (OpenAI), Thariq Shihipar (Anthropic)
Trend 2 (Loop Engineering): Roland Gavrilescu (Introspection), Addy Osmani, Peter Steinberger (OpenClaw),
  Dex Horthy (HumanLayer), Geoffrey Huntley (Ralph Loop creator)
Trend 3 (Forward Deployed Engineers): Natalie Meurer (Sierra), Pauline Brunet (Cursor), Zach Lloyd (Warp),
  Prukalpa Sankar (Atlan)
Trend 4 (Coding Agents replace IDEs): Barr Yaron, Andrew Qu (Vercel), Charlie Holtz (Conductor)
Trend 5 (Skills as Portable Knowledge): Philipp Schmid (Google DeepMind), Paul Bakaus, Matt Pocock,
  Garry Tan (Y Combinator), Tyler Brown

Named coding-agent tools cited as IDE replacements: Claude Code, Codex, Gemini CLI, Cursor, Warp
```

## Cross-References

- **Corroborates**:
  - `blog-lilianweng-harness-engineering-rsi.md` (Claim 1) — harness-as-orchestration-layer framing, cited here secondhand as the "systems over agents" trend.
  - `blog-latentspace-gavrilescu-autoresearch-introspection.md` (Claim 2) and `blog-addyosmani-loop-engineering.md` / `blog-addyosmani-own-the-outer-loop.md` (Claims 1–2) — inner-loop/outer-loop framing, quoted verbatim in both places.
  - `blog-latentspace-meurer-agent-engineer-fde.md` (Claim 4) and `blog-thebatch-fde-agents-aiact-issue355.md` (Claim 1) — FDE-as-orchestration-layer framing.
  - `blog-latentspace-vercel-andrew-qu-eve.md` (Claim 9) — skills-as-portable-knowledge framing, restated near-verbatim.
  - `docs-github-copilot-agent-skills-cli.md` — cross-platform skills adoption, corroborates the "skills going cross-platform" claim from a different vendor (GitHub) than the ones named in this piece (Vercel, Google DeepMind).
- **Contradicts**: None identified. This is a synthesis piece drawing on sources already in this corpus rather than staking out a disputed position; Claim 4 (Huntley's skepticism about loops/factories) sits in mild tension with the otherwise confident framing of loop engineering as a settled trend, but this is a caveat embedded within the same source, not a contradiction between sources — the article itself presents it as an open risk rather than asserting loops are proven, so no contradiction issue was filed.
- **Extends**: `blog-latentspace-aiewf-loops-software-factories-dispatch.md`, `blog-latentspace-aiewf-autoresearch-agency-dispatch.md`, `blog-latentspace-aiewf-loops-debate-dispatch.md` — this piece is MacManus's own later synthesis of themes he covered live across those three day-by-day dispatches, now organized as five named trends rather than chronological coverage.
- **Novel**: The explicit cross-platform enumeration of skills adoption (Anthropic → Vercel → Google DeepMind, via Philipp Schmid) is new to this corpus in this combination. Paul Bakaus's proposed "skill engineering" as a named discipline (Claim 8) is also new — no other source note in this corpus documents that specific framing.

## Guide Impact

- **Chapter 02 (Harness Engineering)**: No new recommendation. This source's harness/loop-engineering claims are downstream restatements of `blog-lilianweng-harness-engineering-rsi.md` and the Osmani loop-engineering notes, which should remain the primary citations. This note's value is as a secondary "this became industry-wide vocabulary" citation if the guide wants to note that harness/loop framing reached broad conference-level consensus by mid-2026, not as a source of new technical claims.
- **Chapter 04 (Context/Skills)**: If the guide adds a claim that skills adoption has gone cross-platform beyond Anthropic and GitHub, this source (Claim 7) is the citation for Google DeepMind's adoption via Philipp Schmid — currently the only source in this corpus naming that specific vendor.
- **No chapter currently cites "skill engineering" as a named discipline** (Claim 8). If the guide ever wants to flag this as an emerging (not yet settled) framing, this is the only source note that documents it, and it should be flagged as anecdotal/single-practitioner pending a primary source.

## Extraction Notes

- The article is paywalled/rendered behind a script-heavy page for full-text scraping; I retrieved it via targeted fetches rather than a single full-text pull, cross-checking each trend section separately (Systems over Agents / Weng; Loop Engineering / Gavrilescu, Osmani, Huntley; FDEs / Meurer; Coding Agents / named tools; Skills / Osmani, Qu, Schmid, Bakaus) to confirm exact wording before quoting.
- This is explicitly a synthesis/aggregation piece: nearly every substantive claim in it restates a primary source already deeply mined elsewhere in this corpus (Weng's own essay, Osmani's own posts, the Meurer interview, the Qu interview, the Gavrilescu interview). I have flagged this in "Our assessment" for each claim rather than treating the restatements as independent corroboration of equal weight to the primary sources. The two points I found genuinely novel to this corpus are the explicit cross-platform skills enumeration (Claim 7) and the "skill engineering" discipline proposal (Claim 8).
- No contradictions with existing source notes were found; Claim 4 (Huntley's skepticism) is a caveat internal to this same source, not a cross-source disagreement, so no contradiction issue was filed per MINER.md §4a guidance on conditioning-variable vs. genuine contradiction.
- I did not follow outbound links from the article (e.g., to Weng's essay or Osmani's posts) as separate "linked sub-pages" per MINER.md §1, because each of those is already an independently mined primary source in this corpus — following them would have duplicated existing notes rather than surfaced new material.
