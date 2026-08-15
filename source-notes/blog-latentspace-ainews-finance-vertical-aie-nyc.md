---
source_url: https://www.latent.space/p/ainews-ai-is-eating-finance-aie-nyc
source_type: blog-post
title: "[AINews] AI is eating Finance; AIE NYC now open"
author: Latent Space / AINews (automated/editorial daily digest with a hand-written intro attributed to Shawn "swyx" Wang; aggregates tweets/Reddit for 7/28/2026-7/29/2026)
date_published: 2026-07-29
date_extracted: 2026-08-15
last_checked: 2026-08-15
status: current
confidence_overall: anecdotal
issue: "#2720"
---

# [AINews] AI is eating Finance; AIE NYC now open

> Latent Space's AINews digest for July 29, 2026 leads with a hand-written
> editorial section naming "AI in Finance" as a mainstage theme for the
> second annual AI Engineer NYC conference, previewing a ten-speaker
> conference track with one-line theses from named practitioners at
> FactSet, Nubank, Intuit, Kepler, Morgan Stanley, FlyersSoft, Fidelity,
> China Resources Holdings, and Auditoria AI — then continues into the
> digest's standard "AI Twitter Recap" sections, which include a
> cross-harness benchmark showing the same model performs very differently
> depending on the harness it runs in, and a concretely benchmarked case of
> a harness recursively improving itself.

## Source Context

- **Type**: blog-post (Latent Space's "AINews" — a daily, largely
  automated/editorial digest that aggregates official statements, tweets,
  and Reddit threads into a single dated post; structured here as a
  hand-written intro/analysis section on the Finance vertical, then an "AI
  Twitter Recap" with six named subsections and a "Top Tweets" summary,
  then a paywalled "AI Reddit Recap"). Published 2026-07-29 per the
  article's own dateline ("AI News for 7/28/2026-7/29/2026. We checked 12
  subreddits, 544 Twitters and no further Discords").
- **Author credibility**: No individual byline is attached to the digest
  as a whole, but the Finance-vertical intro section is written in first
  person ("This is why I am making AI in Finance our mainstage theme for
  the second annual AIE NYC this October") and references "our expected
  attendee list" for the AI Engineer conference — internally consistent
  with Latent Space being run by Shawn "swyx" Wang, who also organizes the
  AI Engineer (AIE) conference series. Per the credibility caveat already
  established in this corpus for the same publication
  (`blog-latentspace-ainews-fearing-rsi-pace-letter.md`,
  `blog-latentspace-ainews-cybersecurity-top-of-mind.md`,
  `blog-latentspace-ainews-kimi-k3-wiki-memory.md`), AINews-relayed claims
  further into the digest should be treated as attributed third-party
  opinion or vendor/incident self-disclosure, not as Latent Space's own
  independent testing or reporting. The ten Finance-track bullets are the
  digest editor's own one-line synopses of a freshly released conference
  video playlist ("the full Finance track was released today") — they are
  the editor's compressed paraphrase of each named speaker's talk, not
  verbatim speaker quotes, and this Miner did not watch the underlying
  videos to verify them independently.
- **Scope**: Covers (1) a hand-written editorial framing AI-in-finance as
  a broad, cross-lab adoption trend and previewing ten conference-talk
  theses from named financial-services practitioners; (2) the digest's
  standard "AI Twitter Recap," including agent-security incident fallout,
  OpenAI's Codex Security CLI release and academic-access program, the
  Kimi K3 ecosystem, and a cluster of harness/benchmark items; (3) the
  opening line of a paywalled "AI Reddit Recap" (inaccessible — see
  Extraction Notes). Does NOT provide the conference talks themselves, any
  named practitioner's own words beyond the digest's synopsis, or the
  paywalled Reddit recap and remaining Twitter-recap sections.

## Extracted Claims

### Claim 1: AI is being framed as broadly adopted across financial-services subsectors, evidenced by both OpenAI and Anthropic running dedicated NYC events with finance-specific product launches in the same period

- **Evidence**: Digest's own editorial framing, citing OpenAI's Codex equity-investing and investment-banking plugins launched at an OpenAI NYC event, and Anthropic's Financial Services team NYC event releasing Cowork and Claude Code agent templates for corporate finance workflows.
- **Confidence**: anecdotal (digest's own interpretive framing of two vendor product launches, not an independently sourced adoption metric)
- **Quote**: "One noteworthy trend we ARE tracking is the rise of AI in Finance, which though is often covered by Forward Deployed Engineering, is being broadly adopted in every subsector of financial services. You can tell it's a big deal when OpenAI gets ae to put on a suit for their NYC event with dedicated equity investing and investment banking plugins in Codex, and Anthropic's Financial Services team also does an NYC event and releases Cowork and Claude Code agent templates covering every workflow in corporate finance."
- **Our assessment**: This is framing, not measurement — "broadly adopted in every subsector" is an editorial claim with no adoption statistic attached. The concrete, checkable part is that both major labs shipped named finance-specific product surfaces (Codex plugins; Claude Code/Cowork templates) around the same period, which is consistent with (and gives dated, named-product evidence for) the general "coding tools expand into adjacent verticals" thesis already present in this corpus via `blog-anthropic-fong-finance-narrative.md` and `blog-anthropic-hebbia-financial-diligence.md`. Worth citing as a dated marker of both labs formalizing finance-vertical go-to-market, not as evidence of adoption depth.

### Claim 2: FactSet's Yogendra Miraje frames "AI skills" as needing ownership, search, evals, audits, and governance to become enterprise-grade agent infrastructure, not just features

- **Evidence**: Digest's one-line synopsis of the FactSet talk in the newly released AIE NYC Finance track.
- **Confidence**: anecdotal (single-sentence digest paraphrase of an unwatched conference talk from a named speaker at a named company)
- **Quote**: "At a company serving thousands of financial-data clients, "AI skills" aren't just features — they need ownership, search, evals, audits, and governance to become enterprise-grade agent infrastructure."
- **Our assessment**: The framing of "AI skills" (in the Claude Skills / Agent Skills sense) as requiring dedicated infrastructure — not ad hoc prompt files — directly parallels the "supply-chain security for AI skills" framing in Claim 6 below (Nubank/Palma) from the same track. Two independently named speakers converging on skills-as-infrastructure (rather than skills-as-artifact) in the same conference track is a notable directional signal, even though neither claim carries metrics.

### Claim 3: Nubank pairs its agent evaluation pipeline with Snowglobe simulation so that agent evals become the release mechanism for shipping customer-facing AI faster, rather than a bottleneck, at a 100M+-customer digital bank

- **Evidence**: Digest's one-line synopsis of the Nubank + Snowglobe talk.
- **Confidence**: anecdotal (single-sentence digest paraphrase of an unwatched conference talk)
- **Quote**: "For a digital bank with 100M+ customers, simulations can turn agent evals from a bottleneck into the release mechanism for shipping customer-facing AI faster."
- **Our assessment**: "Evals as the release mechanism" (rather than a pre-release gate that slows shipping) is a specific operational framing worth distinguishing from generic "add more evals" advice — it implies evals are wired directly into the deploy pipeline rather than run as a separate QA step. No detail is given on what Snowglobe's simulation actually does or measures; this is a thesis statement, not a described architecture.

### Claim 4: Intuit's Udi Menkes argues that at consumer/small-business/accountant scale, generic LLMs are insufficient — finance AI must understand real state, actions, outcomes, and risk

- **Evidence**: Digest's one-line synopsis of the Intuit talk.
- **Confidence**: anecdotal (single-sentence digest paraphrase of an unwatched conference talk)
- **Quote**: "When you serve ~100M consumers, small businesses, and accountants, generic LLMs aren't enough — finance AI has to understand real state, actions, outcomes, and risk."
- **Our assessment**: "Real state, actions, outcomes, and risk" is close in spirit to the deterministic-execution-layer argument already documented in depth in `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 3 (Claude as one stage in a pipeline whose surrounding deterministic infrastructure is load-bearing) — both frame generic model output as insufficient without grounding in real, verifiable system state. This source adds nothing architectural beyond the thesis statement, so treat it as corroborating direction, not new mechanism.

### Claim 5: Kepler's Vinoo Ganesh frames "verifiable AI" in financial research as requiring every answer to carry provenance, reconciliation, and review

- **Evidence**: Digest's one-line synopsis of the Kepler talk, naming Vinoo Ganesh and describing Kepler as indexing millions of filings and market documents.
- **Confidence**: anecdotal as stated in this source (single-sentence digest paraphrase); the underlying claim is independently corroborated by prior direct reporting — see Cross-References.
- **Quote**: "In financial research, where Kepler indexes millions of filings and market documents, "verifiable AI" means every answer needs provenance, reconciliation, and review."
- **Our assessment**: This directly **corroborates** `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 9 (provenance must be designed in from day one as an architectural constraint) and Claim 11 (auditability, not accuracy, is the irreducible trust requirement discovered through Kepler's pre-founding research with 147 financial firms) — both sourced from named Kepler leadership (Ganesh is CEO in that note) with substantially more depth (named quotes, architecture diagrams, production metrics) than this digest's one-line synopsis provides. This entry adds no new information beyond confirming Ganesh continues to make the same argument in public conference talks months after the original case study; cite the Kepler case-study note for depth, this source only for the dated confirmation that the framing persists.

### Claim 6: Nubank's Lucas Palma frames vetting thousands of AI skills before developers use them as a supply-chain security problem, not merely a developer-experience problem, at one of the world's largest digital banks

- **Evidence**: Digest's one-line synopsis of the Nubank talk.
- **Confidence**: anecdotal (single-sentence digest paraphrase of an unwatched conference talk)
- **Quote**: "At one of the world's largest digital banks, vetting thousands of AI skills before developers use them becomes a supply-chain security problem, not just a DX problem."
- **Our assessment**: "AI skills as a supply-chain security surface" at bank scale (thousands of skills, implying an internal skill marketplace or registry) is a specific framing not previously documented in this corpus in a financial-services context. It is directionally consistent with general agent-supply-chain concerns already covered elsewhere in the corpus (e.g., prompt-injection and third-party-tool trust threads), but this source gives no detail on Nubank's actual vetting process — only the framing that DX-first skill adoption underestimates the security surface.

### Claim 7: Morgan Stanley's Brendan Hogan Rappazzo frames multi-agent research as valuable only if humans can trust the experimental environment it optimizes in, at an institution managing trillions in client assets

- **Evidence**: Digest's one-line synopsis of the Morgan Stanley talk.
- **Confidence**: anecdotal (single-sentence digest paraphrase of an unwatched conference talk)
- **Quote**: "Inside a global financial institution managing trillions in client assets, multi-agent research only matters if humans can trust the experimental environment it optimizes in."
- **Our assessment**: This is a trust-in-the-harness argument distinct from trust-in-the-model — the claim is that the surrounding evaluation/simulation environment (not the multi-agent system's raw output) is the thing that must be trustworthy for the research to be actionable. No detail on what "the experimental environment" consists of or how trust is established is given; treat as a thesis pointer, not an architecture.

### Claim 8: FlyersSoft's Divakar Kumar argues event-sourced systems already preserve the historical trail financial agents need, making event sourcing a natural foundation for auditable production agent decision loops

- **Evidence**: Digest's one-line synopsis of the FlyersSoft talk.
- **Confidence**: anecdotal (single-sentence digest paraphrase of an unwatched conference talk)
- **Quote**: "Event-sourced systems already preserve the historical trail that financial agents need, making them a natural foundation for auditable production decision loops."
- **Our assessment**: This is the most architecturally specific and novel claim in the Finance-track cluster: it names a pre-existing software architecture pattern (event sourcing) as directly reusable for agent auditability, rather than proposing agent-specific logging infrastructure from scratch. It is conceptually adjacent to but distinct from the provenance-first architecture in the Kepler note (Claim 5 above) — Kepler's provenance chain traces outputs back to source documents, whereas this claim is about reusing an existing systems-architecture pattern (event sourcing) as the substrate for agent audit trails. No implementation detail is given beyond the one-sentence thesis.

### Claim 9: Fidelity Investments' Sai Krishna Rallabandi argues group-chat and wearable agent interfaces force new thinking around memory, permissions, and prompt-injection defense, at an asset manager with trillions under administration

- **Evidence**: Digest's one-line synopsis of the Fidelity talk.
- **Confidence**: anecdotal (single-sentence digest paraphrase of an unwatched conference talk)
- **Quote**: "At an asset manager with trillions under administration, group-chat and wearable agents force new thinking around memory, permissions, and prompt-injection defense."
- **Our assessment**: Naming wearable devices (not just group chat) as an agent interface surface requiring new prompt-injection defense thinking is novel to this corpus — prior prompt-injection coverage (e.g. `blog-simonwillison-prompt-injection-role-confusion.md`) does not address wearables specifically. No detail on the actual threat model or mitigation is given; this is a thesis pointer flagging a new attack surface, not a described defense.

### Claim 10: China Resources Holdings' Shawn Chan argues finance AI at Fortune Global 500 conglomerate scale must be built for the investment memo — reconciled numbers, uncertainty labels, and provenance beating demo polish

- **Evidence**: Digest's one-line synopsis of the China Resources Holdings talk.
- **Confidence**: anecdotal (single-sentence digest paraphrase of an unwatched conference talk)
- **Quote**: "For a Fortune Global 500-scale conglomerate, finance AI has to be built for the investment memo — reconciled numbers, uncertainty labels, and provenance beat demo polish."
- **Our assessment**: "Uncertainty labels" as a named deliverable component (alongside reconciled numbers and provenance) is a specific, checkable design requirement not present in the Kepler note's architecture — Kepler documents provenance and deterministic reconciliation but does not describe attaching explicit uncertainty labels to outputs. If this pattern is real (not just a synopsis artifact), it would be a novel addition to the corpus's regulated-AI-output design patterns; flagged here as worth following up if a fuller source on China Resources' finance-AI work surfaces.

### Claim 11: Auditoria AI's Ramana Siddanth Emani argues that in back-office finance automation, the bottleneck may be the developer loop itself — agents can increasingly generate the workflows while humans verify the financial truth

- **Evidence**: Digest's one-line synopsis of the Auditoria AI talk.
- **Confidence**: anecdotal (single-sentence digest paraphrase of an unwatched conference talk)
- **Quote**: "In back-office finance automation, the bottleneck may be the developer loop itself — agents can increasingly generate workflows while humans verify the financial truth."
- **Our assessment**: This reframes the human-in-the-loop boundary specifically for back-office finance: agents own workflow *generation*, humans own *financial-truth verification* — a narrower and more specific division of labor than the general "human review AI output" framing common elsewhere in the corpus. Whether "the developer loop is the bottleneck" is a defensible diagnosis (versus, e.g., data access or approval latency) is not argued or evidenced beyond the thesis statement.

### Claim 12: Composio's cross-harness benchmark found the same underlying model (Kimi K3) produces similar task-success rates but substantially different speed and cost profiles depending on which of three agent harnesses runs it

- **Evidence**: Digest's summary of a Composio benchmark comparing three harnesses (Kimi Code, Hermes, Claude Code) all running the same Kimi K3 model, reporting task-success counts out of 28 for each and qualitative speed/cost rankings.
- **Confidence**: emerging (a specific, named, numeric third-party benchmark relayed secondhand by the digest; this Miner did not independently open Composio's results link to verify methodology)
- **Quote**: "Composio's comparison using the same Kimi K3 model across three agent harnesses found similar success rates but very different speed/cost profiles: Kimi Code 22/28, Hermes 21/28, Claude Code 20/28, with Hermes fastest and Kimi Code cheapest/token-most-efficient. This neatly reinforces the "model + harness" thesis shaping many of today's agent eval discussions."
- **Our assessment**: This is a concrete, numeric demonstration of the "harness matters as much as the model" thesis already well-established in this corpus's harness-engineering literature (`blog-lilianweng-harness-engineering-rsi.md` Claim 1 defines the harness as the orchestration layer; multiple `blog-latentspace-ainews-*` notes document the recurring "model + harness" framing in agent-eval discourse). What's new here is a same-model, cross-harness A/B/C benchmark with actual numbers (22/28 vs 21/28 vs 20/28 success, plus speed and cost deltas) rather than a qualitative argument — success-rate variance is narrow (a 2-point spread out of 28) while the digest characterizes the speed/cost variance as "very different," suggesting the harness choice's main leverage in this benchmark was efficiency, not raw success rate. Worth citing as a concrete instance of the thesis rather than new theory.

### Claim 13: Cline reported that Kimi K3 spent 17 hours recursively improving the Cline harness itself, raising the harness's Terminal Bench score from 77.5% to 88.8% while cutting run cost from $79 to $49.8

- **Evidence**: Digest's summary of a Cline announcement describing an agent-driven harness self-improvement run with before/after benchmark and cost figures.
- **Confidence**: emerging (a specific, named, numeric claim from the tool vendor itself, relayed secondhand by the digest; this Miner did not independently open Cline's announcement to verify methodology or check for cherry-picking)
- **Quote**: "Cline reported that Kimi K3 spent 17 hours recursively improving the Cline harness, raising Terminal Bench performance from 77.5% to 88.8% while reducing run cost from $79 to $49.8."
- **Our assessment**: This **extends** `blog-lilianweng-harness-engineering-rsi.md`, which surveys harness recursive-self-improvement as an emerging research direction (Claim 7's Meta-Harness treating harness source code as an executable search space; Claim 12's Darwin Gödel Machine improving SWE-bench Verified from 20% to 50% via self-modifying harness code) but draws its concrete numeric examples from research papers, not shipped consumer tooling. This Cline/Kimi K3 datapoint is the first evidence in this corpus of a mainstream, publicly available coding-agent product (Cline) shipping a recursive harness-self-improvement run with a simultaneous quality gain (77.5%→88.8%) and cost reduction (\$79→\$49.8) reported by the vendor. Both improvements moving together (rather than trading off) is notable and worth flagging for independent verification, since vendor-reported harness-improvement claims are exactly the kind of self-reported benchmark the `blog-lilianweng-harness-engineering-rsi.md` note (Claim 14) warns are prone to reward-hacking the eval signal — this Miner did not confirm Terminal Bench methodology or check whether Cline's own self-improvement loop had held-out evaluation separate from the optimization signal.

### Claim 14: OpenAI open-sourced a Codex Security CLI — a repository scanner for codebases and CI/CD pipelines that scans code, tracks findings across runs, verifies fixes, and integrates security checks into pipelines

- **Evidence**: Digest's summary of an OpenAI announcement, described as "one of the clearest product releases" in that day's Twitter recap.
- **Confidence**: emerging (a specific, named, dated open-source product release relayed secondhand by the digest; this Miner did not independently open the announcement/docs links)
- **Quote**: "OpenAI open-sourced Codex Security CLI: the company quietly released an open-source repository scanner for repos and CI/CD that can scan codebases, track findings across runs, verify fixes, and integrate security checks into pipelines."
- **Our assessment**: This **extends** `blog-latentspace-ainews-fearing-rsi-pace-letter.md` Claim 8, which mentions "OpenAI open-sourced its Codex Security CLI" only as one clause inside a longer sentence about the Open Secure AI Alliance, with no product description. This source adds the actual product description (repo/CI-CD scanner; scan, track findings across runs, verify fixes, pipeline integration) that the earlier note lacks. Combined, the two notes establish both the "why now" context (open security tooling as a response to the OpenAI/Hugging Face agent-intrusion incident, per the earlier note) and the "what it does" product shape (per this note).

### Claim 15: OpenAI's ChatGPT for Academic Researchers program will give free frontier-model access to 10,000 researchers initially, expanding to 100,000 by 2027, including the GPT-5.6 family, with business-grade privacy/security and up to four collaborators per workspace

- **Evidence**: Digest's summary of an OpenAI program-launch announcement with named scale figures.
- **Confidence**: emerging (a specific, named, dated program-launch figure relayed secondhand by the digest; this Miner did not independently open the announcement link)
- **Quote**: "ChatGPT for Academic Researchers: OpenAI launched a program to give 10,000 researchers initially, expanding to 100,000 by 2027, free access to frontier models including the GPT-5.6 family, with business-grade privacy/security and up to four collaborators per workspace."
- **Our assessment**: This **extends** `blog-openai-chatgpt-work-education-plugins.md` Claim 13, which documents the same ChatGPT for Academic Researchers program (from an August 4, 2026 OpenAI announcement page) with a different fact about it: "12 months of free Pro-level access." That note does not give a researcher-population figure; this source (dated five days earlier, July 29) gives the population scale (10,000 → 100,000 by 2027) but not the access duration. The two notes are complementary, not contradictory — different facts about the same program from what appear to be two separate OpenAI communications (an initial digest-relayed launch mention here, a fuller announcement page five days later in the other note). Neither this Miner nor (per its extraction notes) the earlier note's Miner independently confirmed both figures against a single primary source, so cite them together rather than assuming either is the complete picture.

## Concrete Artifacts

```
AIE NYC Finance Track — speaker roster and one-line theses
Source: AINews digest, July 29, 2026 (digest's own synopsis of a newly
released conference video playlist; speakers' own words not confirmed)

FactSet / Yogendra Miraje         — AI skills need ownership, search, evals,
                                     audits, governance to be enterprise-grade
                                     agent infrastructure
Nubank + Snowglobe                — simulations turn agent evals into the
                                     release mechanism, not a bottleneck
Intuit / Udi Menkes                — generic LLMs insufficient at ~100M-user
                                     scale; need real state/actions/
                                     outcomes/risk understanding
Kepler / Vinoo Ganesh              — verifiable AI = provenance + reconciliation
                                     + review on every answer
Nubank / Lucas Palma                — vetting thousands of AI skills is a
                                     supply-chain security problem, not just DX
Morgan Stanley / Brendan Hogan     — multi-agent research only matters if
  Rappazzo                          humans trust the experimental environment
FlyersSoft / Divakar Kumar          — event-sourced systems are a natural
                                     foundation for auditable agent decisions
Fidelity Investments / Sai Krishna  — group-chat/wearable agents force new
  Rallabandi                        thinking on memory, permissions,
                                     prompt-injection defense
China Resources Holdings /          — finance AI must serve the investment
  Shawn Chan                        memo: reconciled numbers, uncertainty
                                     labels, provenance over demo polish
Auditoria AI / Ramana Siddanth      — developer loop may be the bottleneck;
  Emani                             agents generate workflows, humans verify
                                     financial truth
```

```
Composio cross-harness benchmark (same model, three harnesses)
Source: AINews digest relay of Composio results, July 29, 2026

Harness        | Task success (of 28) | Notable trait
----------------|----------------------|---------------------------
Kimi Code       | 22/28                | cheapest / most token-efficient
Hermes          | 21/28                | fastest
Claude Code     | 20/28                | (baseline in this comparison)

All three ran the same underlying Kimi K3 model.
```

```
Cline / Kimi K3 recursive harness self-improvement run
Source: AINews digest relay of Cline announcement, July 29, 2026

Duration:        17 hours
Terminal Bench:  77.5% -> 88.8%
Run cost:        $79 -> $49.8
```

## Cross-References

- **Corroborates** `blog-anthropic-kepler-verifiable-ai-financial.md` Claim 9
  (provenance must be designed in from day one as an architectural
  constraint) and Claim 11 (auditability, not accuracy, is the irreducible
  trust requirement Kepler's founders discovered through pre-founding
  research with 147 financial firms): Claim 5 above (Ganesh's "verifiable
  AI means every answer needs provenance, reconciliation, and review")
  is the same claim made by the same named CEO, in a public conference
  talk months after the original case study, confirming the framing has
  persisted rather than being a one-off marketing line.

- **Corroborates** `blog-lilianweng-harness-engineering-rsi.md` Claim 1
  (the harness, not the prompt, is the orchestration layer that determines
  how a model performs) and the broader "model + harness" framing
  documented across this corpus's `blog-latentspace-ainews-*` notes: Claim
  12 above (Composio's same-model, three-harness benchmark) gives that
  thesis a concrete numeric instance (22/28 vs 21/28 vs 20/28 success,
  with larger speed/cost spread) rather than a qualitative argument.

- **Extends** `blog-lilianweng-harness-engineering-rsi.md` Claim 7 (Meta-
  Harness treats harness source code as an executable search space) and
  Claim 12 (the Darwin Gödel Machine improved SWE-bench Verified from
  20%→50% via self-modifying harness code): Claim 13 above (Cline/Kimi K3's
  17-hour, 77.5%→88.8% harness self-improvement run) is this corpus's first
  example of a mainstream shipped coding-agent product, rather than a
  research paper, reporting a recursive harness-self-improvement result —
  worth flagging that this note's Claim 14 (in the harness-engineering-rsi
  note) warns self-improvement loops are prone to reward-hacking their own
  eval signal, and this Miner did not verify Cline's methodology.

- **Extends** `blog-latentspace-ainews-fearing-rsi-pace-letter.md` Claim 8
  (which mentions OpenAI's Codex Security CLI open-sourcing only as one
  clause, with no product description): Claim 14 above supplies the actual
  product shape (repo/CI-CD scanner; scan, track findings across runs,
  verify fixes, pipeline integration) that the earlier note lacks.

- **Extends** `blog-openai-chatgpt-work-education-plugins.md` Claim 13
  (ChatGPT for Academic Researchers gives 12 months of free Pro-level
  access): Claim 15 above adds the researcher-population scale (10,000
  initially, expanding to 100,000 by 2027) that the later, fuller
  announcement-page note does not include. Neither note's Miner
  independently confirmed both figures against a single primary source —
  cite together, not as fully reconciled.

- **Novel**:
  - The ten-speaker AIE NYC Finance track roster and one-line theses
    (Claims 2–4, 6–11) are the corpus's first coverage of this specific
    conference track. Several individual theses are novel framings not
    previously documented: "AI skills as supply-chain security problem"
    (Nubank/Palma), "event sourcing as a natural foundation for auditable
    agent decisions" (FlyersSoft/Kumar), "wearable agents as a new
    prompt-injection surface" (Fidelity/Rallabandi), and "uncertainty
    labels" as a named deliverable component alongside reconciled numbers
    and provenance (China Resources/Chan).
  - The Composio cross-harness benchmark (Claim 12) and the Cline
    recursive-self-improvement run (Claim 13) are both novel, dated,
    numeric data points not present elsewhere in the corpus, though both
    are only secondhand digest relays of vendor/third-party results this
    Miner did not independently verify.

## Guide Impact

- **Chapter 05 (Team Adoption)**: If the guide adds a financial-services
  adoption-pattern subsection, cite the AIE NYC Finance track roster
  (Claims 2–4, 6–11) as a dated snapshot (July 2026) of what named
  practitioners at ten financial institutions are publicly framing as
  their priorities — but flag every entry as a one-sentence digest
  synopsis of an unwatched talk, not a verified architecture or metric.
  Only Claim 5 (Kepler/Ganesh) has independent, deeper corroboration
  already in the corpus; the guide should prefer citing the Kepler case
  study directly and use this source only to note the framing has
  persisted in public talks.

- **Chapter 06 (Security/Threat Model)**: Add "AI skills as a supply-chain
  security surface" (Claim 6, Nubank/Palma) and "wearable agents as a new
  prompt-injection attack surface" (Claim 9, Fidelity/Rallabandi) as named
  emerging threat framings from regulated-industry practitioners, flagged
  as thesis statements without described mitigations — worth tracking for
  a fuller source if either company publishes technical detail.

- **Chapter 02 (Harness Engineering)**: If the guide's harness section
  cites the "model + harness" thesis, add Composio's cross-harness Kimi K3
  benchmark (Claim 12: 22/28 vs 21/28 vs 20/28 success, larger speed/cost
  spread) as a concrete numeric instance, and Cline's recursive
  harness-self-improvement run (Claim 13: 77.5%→88.8% Terminal Bench,
  $79→$49.8 cost, 17 hours) as the first shipped-product example alongside
  the research-paper examples already cited from
  `blog-lilianweng-harness-engineering-rsi.md`. Flag both as vendor-
  reported and unverified by this corpus's Miners.

## Extraction Notes

- The article is paywalled roughly two-thirds of the way through the "AI
  Reddit Recap" section header — the "AI in Finance" editorial section and
  the full "AI Twitter Recap" (six subsections plus "Top Tweets") are
  free and were read in full; the "AI Reddit Recap" section and beyond
  were not accessible and are not represented in this note.
- All quotes were verified character-for-character against the raw
  fetched HTML (tags stripped, HTML entities unescaped) rather than
  against a markdown-converted version, to avoid quoting markdown-escape
  artifacts (e.g. backslash-prefixed list markers) introduced by
  HTML-to-markdown conversion.
- The ten Finance-track bullets are the digest editor's synopses of a
  video playlist, not transcribed speaker quotes — this Miner did not
  watch the linked YouTube playlist. Confidence is rated "anecdotal" for
  each individual speaker claim on that basis, even where the underlying
  company/speaker is independently credible.
- No linked sub-pages were followed; the source's own linked playlist,
  X/Twitter posts, and vendor announcement pages were not independently
  opened by this Miner — all Twitter-recap claims (12–15) are relayed
  secondhand through the digest's paraphrase, consistent with the
  standing caveat already established for this publication elsewhere in
  the corpus.
- Overall confidence is rated "anecdotal" at the note level because the
  single most novel and highest-value section (the Finance track roster)
  rests entirely on unverified, unwatched one-line synopses; the Twitter-
  recap claims (12–15) are individually rated "emerging" where they carry
  specific vendor-reported numbers, but the note-level rating reflects the
  weakest-sourced major section rather than the strongest.
