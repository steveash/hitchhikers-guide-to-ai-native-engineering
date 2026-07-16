---
source_url: https://www.latent.space/p/autoresearch-introspection
source_type: blog-post
title: "Autoresearch: The feedback loop behind self-improving agents"
author: Richard MacManus, interviewing Roland Gavrilescu (Latent Space)
date_published: 2026-07-01
date_extracted: 2026-07-16
last_checked: 2026-07-16
status: current
confidence_overall: anecdotal
issue: "#1927"
---

# Autoresearch: The feedback loop behind self-improving agents

> A Latent Space interview with Roland Gavrilescu, co-founder/CEO of
> Introspection, defining "autoresearch" as an outer-loop system of agents
> that studies and maintains a primary (inner-loop) production system —
> introducing "agent recipes" (documented harness/eval/judge/human-expertise
> history), the "ask a human" tool for bootstrapping agent judgment, and a
> practical three-part starting checklist (invest in signals, control cost,
> follow research patterns) — while explicitly arguing full autonomy
> ("software factory") is a further-out goal than the human-in-the-loop
> ("orchestra") stage most practitioners are actually in today.

## Source Context

- **Type**: blog-post (interview/Q&A transcript), Latent Space
  (latent.space, run by Shawn "swyx" Wang), interviewer Richard MacManus,
  published 2026-07-01. `trusted-feed` source per this repo's scanning
  configuration (`latent-space` feed), auto-discovered and pre-screened
  before Prospector triage.
- **Author credibility**: Roland Gavrilescu is co-founder and CEO of
  Introspection, a company the post describes as "building infrastructure
  for deploying these self-improving systems." Before founding Introspection
  he worked on agent infrastructure and cloud agents at xAI, where he met
  his co-founder, Julian Bright. This is first-party practitioner testimony
  from a vendor whose product is built directly around the autoresearch
  pattern being described — the interview is a credible source for what
  Introspection is building and the vocabulary it uses, but Gavrilescu has
  a direct commercial interest in the "autoresearch"/"loop is the product"
  framing landing as the industry-standard vocabulary, and no independent
  metrics, customer names, code, or benchmark data appear anywhere in the
  interview to substantiate the architectural claims. Richard MacManus is
  the named interviewer/byline for this piece.
- **Scope**: Covers Introspection's founding narrative (from xAI); the
  "loop is the product" framing (models → harnesses → loops); "agent
  recipes" as a documentation/provenance concept; the inner-loop/outer-loop
  distinction specific to autoresearch (primary system vs. the system that
  studies it); "Pi" (Introspection's harness, compared to "the Linux of
  agent harnesses"); practical reliability concerns (infrastructure, cost,
  security); the "ask a human" tool and an employee-onboarding analogy for
  agent judgment; Git as the audit-log substrate; Introspection's plan to
  move into non-coding vertical markets; the "orchestra vs. software
  factory" distinction for how much autonomy is realistic today; and closing
  practical advice for engineers starting with autoresearch. Does NOT
  cover: any concrete code, config, or prompt artifacts; named customer
  deployments; quantified cost, latency, or accuracy figures; or any
  description of what happens when an autoresearch loop makes a mistake
  (failure modes are not discussed in the interview).

## Extracted Claims

### Claim 1: "The loop is the product" — the industry's focus has shifted from models, to harnesses, and now to loops
- **Evidence**: Gavrilescu's stated first of several framing points in the
  interview.
- **Confidence**: anecdotal (a single practitioner's framing assertion, no
  external data or timeline evidence given)
- **Quote**: "The first is that the loop is the product. We have moved from focusing on models, to harnesses, and now to loops."
- **Our assessment**: This is a compact restatement of the "models → harness
  → loop" progression already present in this corpus's vocabulary (see
  Cross-References — corroborates `blog-ronacher-the-coming-loop.md` and the
  AIEWF dispatch's "chat, to tools, to goals, to automations" periodization).
  It functions here as Gavrilescu's opening thesis for the whole interview:
  everything that follows (recipes, inner/outer loop, Pi) is scaffolding
  under this one claim. Useful primarily as a vendor-voice corroboration of
  a trend the guide already documents from other angles, not as new
  evidence for the trend itself.

### Claim 2: Autoresearch's "inner loop" is the primary production system serving users; the "outer loop" is a separate system of agents that studies and maintains the primary system
- **Evidence**: Gavrilescu's explicit definitional statement distinguishing
  autoresearch from ordinary agent execution.
- **Confidence**: anecdotal (a definitional/architectural claim, not
  measured or demonstrated with an example)
- **Quote**: "The inner loop is the primary system interacting with users and performing the work. Autoresearch is more concerned with the outer loop: another system that studies and maintains the primary system."
- **Our assessment**: This is a load-bearing definitional claim and it
  reuses the exact term pair "inner loop"/"outer loop" with a *third*,
  structurally distinct referent from the two already in the corpus:
  `blog-addyosmani-own-the-outer-loop.md` Claim 2 defines outer loop as the
  *human accountability boundary* around one agent's execution; this source
  defines outer loop as an *entirely separate agentic system* studying a
  different (inner-loop) system, with no human-accountability referent at
  all. Per MINER.md §4a, this term collision has been filed as a
  contradiction — see Cross-References → Contradicts. No verdict is
  asserted here.

### Claim 3: "Agent recipes" document a system's full evolution — harness behavior across models, evals, judges, human expertise, and the failures that produced new evals
- **Evidence**: Gavrilescu's definitional description, drawing an explicit
  analogy to "data recipes" in model training.
- **Confidence**: anecdotal (a named concept from one practitioner, no
  worked example or template shown)
- **Quote**: "A recipe might describe how your harness works with different models, the evals you use, the judges you have created, the human expertise you have captured and the failures that led to new evals."
- **Our assessment**: This is the interview's most concrete, guide-citable
  artifact concept even though no actual recipe is reproduced. It names five
  components explicitly (harness-per-model behavior, evals, judges, captured
  human expertise, failure history) as what should be documented about an
  agentic system over time — a more specific decomposition than "keep good
  docs." It resembles, but is distinct from, the "agent recipes"/data-recipe
  analogy: the source draws the comparison itself but does not explain what
  a "data recipe" is beyond the analogy, so that half of the claim is not
  independently verifiable from this interview alone.

### Claim 4: Agents can be trained to ask people questions through an "ask a human" tool, relying heavily on it early on and asking fewer questions as they learn
- **Evidence**: Gavrilescu's description of how agents bootstrap judgment,
  paired with an explicit employee-onboarding analogy.
- **Confidence**: anecdotal (described mechanism and analogy, no
  implementation detail, no data on how quickly reliance on the tool
  decreases)
- **Quote**: "Agents can be trained to ask people questions through an 'ask a human' tool. During its first few loops, an agent may rely heavily on asking questions and learning what a human would do."
- **Additional quote (onboarding analogy)**: "It is similar to an employee joining a new company. Initially, that employee asks a lot of questions. As they learn how the organization works, they can make more decisions independently."
- **Our assessment**: This corroborates, at a conceptual level, the corpus's
  existing documentation of a concrete "ask a human"-style mechanism —
  Datasette Agent's `ask_user()` tool (see Cross-References). Gavrilescu's
  framing adds the bootstrapping/onboarding narrative (heavy early reliance,
  declining over time) that the Datasette Agent release note does not make —
  that note documents the mechanism's API and persistence behavior but not
  a claim about usage declining as the agent "learns." No evidence is given
  here for the decline itself; it is presented as expected behavior, not
  measured behavior.

### Claim 5: The broader goal is to turn a product organization into a "miniature research lab," with agents acting as "miniature researchers"
- **Evidence**: Gavrilescu's stated vision for where autoresearch leads.
- **Confidence**: anecdotal (aspirational framing, not a description of a
  current deployed state)
- **Quote**: "The broader goal is to turn your product organization into a miniature research lab, with agents acting as miniature researchers."
- **Our assessment**: This is the interview's most abstract, least-evidenced
  claim — a vision statement with no example of what a "miniature
  researcher" agent actually does day-to-day, what it investigates, or how
  its output is validated. Useful as color for framing the outer-loop
  concept (Claim 2), not as an operational recommendation on its own.

### Claim 6: "Pi is like the Linux of agent harnesses" — a base system designed to be extended, with room for distributions built on top
- **Evidence**: Gavrilescu's own analogy for Introspection's harness
  product, "Pi."
- **Confidence**: anecdotal (a branding/positioning analogy for the
  company's own product, no architectural detail given about what makes Pi
  extensible)
- **Quote**: "Pi is like the Linux of agent harnesses. Linux has distributions such as Ubuntu, but the underlying system is designed to be extended."
- **Our assessment**: This is vendor positioning language for Introspection's
  own product (Pi) and should be read with the same caution the corpus
  already applies to other vendor "factory"/platform framing claims (see
  Cross-References — corroborates the AIEWF dispatch's documentation of
  "software factory" as a converging but self-interested vendor vocabulary).
  No technical detail is given about Pi's plugin model, extension points, or
  what a "distribution" of Pi would concretely look like.

### Claim 7: Making autoresearch loops reliable in production requires knowing what infrastructure the loops need, keeping costs under control, and maintaining security
- **Evidence**: Gavrilescu's stated requirements for production reliability.
- **Confidence**: anecdotal (a list of concerns named without elaboration —
  no specific infrastructure pattern, cost figure, or security control is
  described)
- **Quote**: "You need to know what infrastructure is required to make the loops work, keep costs under control and maintain security."
- **Our assessment**: This is a high-level checklist rather than an
  actionable pattern — it names three concern areas (infrastructure, cost,
  security) without specifying how Introspection or its customers address
  any of them. Weight this as a signal of what practitioners should ask
  about, not as a solved problem with a documented solution.

### Claim 8: Everything in the autoresearch workflow is Git-based, and Git becomes the audit log maintained over time
- **Evidence**: Gavrilescu's stated design choice for why the work happens
  in Git.
- **Confidence**: anecdotal (a stated architectural choice, no detail on
  what specifically is committed — code only, or also recipes/evals/
  decisions)
- **Quote**: "Everything is Git-based, and Git becomes the audit log that you maintain over time."
- **Our assessment**: This corroborates the corpus's existing documentation
  of Git as the substrate for agentic work and accountability records (see
  Cross-References). It is stated as a flat assertion with no example of
  what a Git-based audit trail for an autoresearch loop actually contains —
  contrast with `blog-addyosmani-own-the-outer-loop.md` Claim 13's more
  developed "accountability contract" proposal, which specifies what a
  per-change record should include.

### Claim 9: Coding agents are already working; the next question is how to deploy agents in vertical, non-coding domains without becoming dependent on a single provider
- **Evidence**: Gavrilescu's framing of Introspection's stated next-market
  direction.
- **Confidence**: anecdotal (a stated business direction/opinion, no named
  customer or vertical example given)
- **Quote**: "Coding agents are clearly working, and we have seen a number of companies succeed in that area. The next question is how to deploy agents in vertical and non-coding domains." / "Companies in those markets are asking how they can do this securely without becoming dependent on a single provider."
- **Our assessment**: The single-provider-dependency concern corroborates
  the corpus's existing "model neutrality" architecture thread (see
  Cross-References). No specific vertical (healthcare, finance, legal, etc.)
  is named, and no evidence is given that non-coding verticals are actually
  adopting autoresearch loops yet — this reads as a forward-looking business
  thesis from a vendor, not a documented deployment.

### Claim 10: "An orchestra might retain a human conductor who controls how the loops operate. A factory implies something more fully autonomous" — software factories are a further-out goal than most practitioners' current stage
- **Evidence**: Gavrilescu's explicit metaphor distinguishing two stages of
  autonomy.
- **Confidence**: anecdotal (a metaphor for a maturity progression, not tied
  to any measured adoption data)
- **Quote**: "An orchestra might retain a human conductor who controls how the loops operate. A factory implies something more fully autonomous."
- **Our assessment**: This is a useful, citable distinction for the guide's
  autonomy-maturity framing: "orchestra" (human conductor retains control
  over loop operation) as a nearer-term, more realistic stage than "factory"
  (fuller autonomy). It complements rather than duplicates the corpus's
  existing "software factory" vocabulary (see Cross-References) by
  explicitly naming an intermediate, human-supervised stage using a
  different metaphor (orchestra) than any existing corpus source.

### Claim 11: The human can become "a tool and a source of signals" for agents — models do not initially have the context or understand every decision people inside an organization make
- **Evidence**: Gavrilescu's stated rationale for why humans remain part of
  the autoresearch system rather than being fully removed.
- **Confidence**: anecdotal (a stated rationale, consistent with but not
  independently evidencing Claim 4's "ask a human" mechanism)
- **Quote**: "The human can effectively become a tool and a source of signals. Agents can be trained to ask people questions through an 'ask a human' tool." / "Models do not initially possess all the context or understand every decision people inside an organization make."
- **Our assessment**: This reframes "human in the loop" not as an oversight
  gate but as an input source the agent actively queries — a "human as
  tool" framing that is a genuinely different emphasis from the corpus's
  existing accountability-boundary framings (Osmani's Verdict/Answerability,
  Thoughtworks' supervisory review). It does not contradict those framings
  (Gavrilescu is not arguing against human oversight) but it describes a
  different *mechanism* — the human as a queried data source for agent
  judgment, versus the human as a gatekeeper who approves or blocks agent
  output.

### Claim 12: Practical advice for engineers starting with autoresearch: invest in signal design, control cost, and follow research patterns from frontier labs
- **Evidence**: Gavrilescu's closing three-part recommendation.
- **Confidence**: anecdotal (prescriptive advice from one practitioner, no
  evidence that following this advice produces better outcomes)
- **Quote**: "The first step is to invest in your signals. What are the things you actually want agents to respond to?" / "The second requirement is control over cost. You do not want to wake up to an unexpected thousand-dollar bill because an agent has been running an inefficient loop." / "The third is to follow the research. Look at the kinds of harnesses models are being trained to use and remain close to those patterns."
- **Our assessment**: This is the interview's most actionable, checklist-like
  content — three named priorities (signal design, cost control, staying
  close to how frontier labs train models to use harnesses) for a
  practitioner starting an autoresearch project. It corroborates the
  corpus's existing cost-control concerns (e.g., orchestration-tax fixes in
  `blog-addyosmani-own-the-outer-loop.md` Claim 8) and adds a specific
  autoresearch-flavored risk: an "inefficient loop" running unattended can
  generate an "unexpected thousand-dollar bill" — a concrete failure mode
  named for self-improving/autonomous loops specifically, not for
  single-shot agent tasks.

## Concrete Artifacts

```
Source: Latent Space, "Autoresearch: The feedback loop behind self-improving
agents" (Richard MacManus interviewing Roland Gavrilescu, 2026-07-01)

Section structure of the interview, in order:
  1. From xAI to Introspection
  2. The loop becomes the product
  3. Agent recipes
  4. The inner loop and the outer loop
  5. Pi as the Linux of agent harnesses
  6. Making loops reliable in production
  7. Humans remain part of the system
  8. Taking agent infrastructure into vertical markets
  9. Why the work happens in Git
  10. From orchestras to software factories
  11. How to start with autoresearch

No code blocks, diagrams, numbered procedures, or quantified metrics
(cost figures, latency, accuracy, or adoption numbers) appear anywhere in
the interview — it is conversational Q&A prose throughout. The closing
"How to start with autoresearch" section is the closest the piece comes to
a structured list, and even that is three prose paragraphs rather than an
enumerated list.
```

## Cross-References

- **Corroborates**:
  - `blog-ronacher-the-coming-loop.md` and the AIEWF dispatch note
    (`blog-latentspace-aiewf-loops-software-factories-dispatch.md` Claim 1)
    — Claim 1 here ("the loop is the product," models → harnesses → loops)
    restates the same trend periodization from a different practitioner
    voice (a harness/infrastructure vendor CEO rather than a conference
    keynote or an individual practitioner).
  - `blog-simonwillison-datasette-agent-askuser.md` Claim 1 (the `ask_user()`
    tool: agent tools can pause mid-execution to ask the user a yes/no,
    multiple-choice, or free-text question) — Claim 4 here corroborates the
    existence and purpose of an "ask a human"-style mechanism at the
    conceptual level, though Gavrilescu's account gives no implementation
    detail comparable to that note's documented API, suspension/persistence
    behavior, or re-execution semantics. The two sources are complementary:
    Datasette Agent documents *how* such a tool is built; this interview
    documents *why* a practitioner in a different company would want one
    (bootstrapping agent judgment, declining reliance over time).
  - `blog-addyosmani-own-the-outer-loop.md` Claim 8 (orchestration tax —
    unmanaged agent parallelism creates cost risk) — Claim 12 here's
    "unexpected thousand-dollar bill" risk from "an agent... running an
    inefficient loop" is a specific, autoresearch-flavored instance of the
    same underlying cost-control concern, from a harness-vendor's
    perspective rather than a practitioner's.
  - `blog-latentspace-satya-loopcraft-frontier-ecosystems.md` Claim 2, Claim
    5 (Nadella's "the real opportunity is not in picking the best model but
    instead in building a learning loop on top of models" and "every
    organization can own the learning loop that encodes its institutional
    knowledge") — Claim 1 and Claim 5 here corroborate, at the vendor/
    infrastructure level, the same "the loop (not the model) is the
    durable value" thesis Nadella articulates at the CEO/enterprise-strategy
    level. Both sources use "loop" as the differentiator; neither cites the
    other.
  - AIEWF dispatch note Claims 3, 6, 7, 9, 10 (cross-vendor convergence on
    "software factory" vocabulary: Microsoft, Factory, Warp, Cursor) —
    Claim 10 here's "orchestra vs. factory" distinction adds Introspection
    as a further, independent vendor voice using "factory" as the label for
    the fully-autonomous end state, while contributing a new complementary
    metaphor ("orchestra," human conductor retains control) for the
    nearer-term stage that dispatch note's sources do not name.

- **Contradicts**: `blog-addyosmani-own-the-outer-loop.md` Claim 2. Both
  sources reuse the identical term pair "inner loop"/"outer loop" for
  agentic-system architecture, but assign incompatible referents: Osmani's
  outer loop is the human-accountability boundary wrapped around a single
  agent's execution loop; this source's outer loop is a wholly separate
  agentic system (the autoresearch system) that studies and maintains a
  different, primary (inner-loop) system, with no human-accountability
  referent. This is the same class of terminology collision already flagged
  between Osmani and `blog-thoughtworks-gall-supervisory-engineering.md` in
  issue **[#1940](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/1940)**
  (currently closed as a mismatched pre-screen rejection, per the Assayer's
  assessment on that issue, which recommends reopening it). A new
  contradiction issue has been filed for this third collision:
  **[#1943](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/1943)**.
  No verdict is asserted in this note per MINER.md §4a — the verdict is
  assigned by a human or Smith+human when the issue is resolved and a
  `C-NNN` entry is appended to CONTRADICTIONS.md. Given the overlap in
  subject matter, #1940 and #1943 should likely be resolved together.

- **Extends**:
  - `blog-simonwillison-datasette-agent-askuser.md` — that note documents a
    concrete, shipped implementation of an "ask a human"-style tool; Claim 4
    and Claim 11 here extend it with a stated rationale (bootstrapping
    agent judgment, human as a queried signal source rather than an
    approval gate) that the implementation-focused note does not itself
    argue for.
  - `blog-addyosmani-own-the-outer-loop.md` Claim 13 (the hedged
    "accountability contract" proposal — a per-change record of checklist,
    evidence, owner, and status) — Claim 8 here's flat "Git becomes the
    audit log" assertion is a much less developed version of the same
    underlying idea (durable, queryable provenance for agentic work); it
    adds no new detail beyond naming Git as the substrate.

- **Novel**:
  - The "agent recipes" concept (Claim 3) — a five-part decomposition
    (harness-per-model behavior, evals, judges, captured human expertise,
    failure history) of what should be documented about an evolving
    agentic system over time. Not present in any existing corpus source
    under this name.
  - The "orchestra vs. software factory" maturity metaphor (Claim 10) — a
    new, complementary framing for the human-supervised-vs-fully-autonomous
    distinction, distinct from the corpus's existing "factory" vocabulary
    (which names the end state but, prior to this source, had no named
    metaphor for the human-supervised intermediate stage).
  - "Pi" as a named harness product explicitly positioned as "the Linux of
    agent harnesses" (Claim 6) — new to the corpus's inventory of named
    harness products.
  - The "human as a tool and a source of signals" framing (Claim 11) — a
    distinct mechanism (human as queried input) from the corpus's existing
    "human in the loop" framings, which are predominantly gatekeeper/
    approval-oriented (Osmani's Verdict, Thoughtworks' supervisory review,
    Datasette Agent's approval gates).

## Guide Impact

- **Chapter 02 (Harness Engineering)**: Add "agent recipes" (Claim 3) as a
  named documentation pattern — recommend that teams running long-lived
  agentic systems maintain an explicit record of harness-per-model behavior,
  evals, judges, captured human decisions, and the failures that produced
  new evals, distinct from ordinary code documentation. Flag that no worked
  template or example recipe is available from this source; this is a
  concept to name, not yet a pattern to reproduce verbatim.

- **Chapter 02/Chapter 05 — Terminology caution**: Because this source's
  "inner loop"/"outer loop" pairing is a third, incompatible definition of
  the same term pair already contested between
  `blog-addyosmani-own-the-outer-loop.md` and
  `blog-thoughtworks-gall-supervisory-engineering.md` (see issue #1940), the
  guide should not cite this source's inner/outer-loop terminology without
  resolving issues #1940 and #1943 together first. If the guide adopts
  Osmani's pairing as canonical (per the Assayer's proposed resolution on
  #1940), this source's "outer loop" (the autoresearch system) should be
  cited under different vocabulary — e.g., "the autoresearch system" or "the
  outer-loop system," as a proper noun, not as the guide's canonical
  "outer loop."

- **Chapter 03 (Practitioner Patterns / self-improving loops)**: Add the
  "orchestra vs. software factory" distinction (Claim 10) as a maturity
  framing for autonomy adoption — orchestra (human conductor retains control
  over loop operation) as the realistic near-term stage most teams are
  actually in, factory (fuller autonomy) as a further-out goal. Pair with
  Claim 12's three-part starting checklist (invest in signals, control cost,
  follow frontier-lab harness patterns) as practical first steps for a team
  considering an autoresearch-style outer loop.

- **Chapter 02 (Harness Engineering) — cost risk**: Add Claim 12's specific
  named risk ("an unexpected thousand-dollar bill because an agent has been
  running an inefficient loop") as a citable, autoresearch-specific instance
  of the orchestration-tax cost-control concern already documented via
  `blog-addyosmani-own-the-outer-loop.md` Claim 8.

## Extraction Notes

- **Fetch method**: This source was accessed only via the WebFetch
  summarizing tool (no direct `curl` access was available in this
  environment). A request for full verbatim reproduction of the interview
  was declined by the tool on copyright grounds and returned a summary
  instead — that summary was used only for orientation (confirming section
  structure and overall argument), not as a source for any `Quote` field.
  All `Quote` fields in this note were obtained through a series of
  narrowly-scoped follow-up requests, each asking for the exact, word-for-
  word sentence(s) on a single named topic (e.g., "the exact quote where
  the speaker defines 'agent recipes'") with explicit instructions not to
  paraphrase. This is a lower-certainty verification method than directly
  diffing raw HTML (used in several other corpus notes, e.g.
  `blog-addyosmani-own-the-outer-loop.md`), since it depends on the
  fetch tool's own fidelity rather than this extraction directly inspecting
  the page source. Each targeted request was made independently, and the
  quotes returned were consistent in phrasing and speaker attribution
  across separate requests covering overlapping topics (e.g., the "ask a
  human" quote was returned identically twice, once as part of a
  human-involvement query and once as part of a Claim-4-specific query),
  which is treated as internal corroboration but not a substitute for
  direct HTML verification. Flagged for the Assayer to spot-check directly
  against the live URL if stronger verification is required.
- **Full source read**: All eleven named sections of the interview were
  covered by at least one targeted extraction request; no section was
  skipped. No sub-pages or linked follow-up content were present to follow
  — this is a single, self-contained interview page.
- **No metrics, code, or named customers**: The interview contains no
  quantified data (cost, latency, adoption, accuracy), no code or config
  examples, and no named customer deployments. This is reflected in the
  `anecdotal` overall confidence rating and in the "Does NOT cover" line of
  Source Context — flagged explicitly so the Assayer does not expect
  artifacts that are not present in the source.
- **Contradiction filed**: Per MINER.md §4a, a new contradiction issue
  ([#1943](https://github.com/steveash/hitchhikers-guide-to-ai-native-engineering/issues/1943))
  was filed for the three-way "inner loop"/"outer loop" terminology
  collision (Osmani, Thoughtworks Gall via existing issue #1940, and this
  source). No verdict is asserted in this note.
- Cross-references verified: `blog-addyosmani-own-the-outer-loop.md`,
  `blog-latentspace-aiewf-loops-software-factories-dispatch.md`,
  `blog-latentspace-satya-loopcraft-frontier-ecosystems.md`,
  `blog-cursor-multi-agent-kernels.md`, and
  `blog-simonwillison-datasette-agent-askuser.md` were each re-read in full
  before citing; no claim numbers were guessed.
