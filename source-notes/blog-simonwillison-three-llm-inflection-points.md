---
source_url: https://simonwillison.net/2026/Nov/24/llm-inflection-points/
source_type: blog-post
title: "Three LLM inflection points in twelve months"
author: Simon Willison
date_published: 2026-11-24
date_extracted: 2026-11-26
last_checked: 2026-11-26
status: current
confidence_overall: anecdotal
issue: "#4960"
---

# Three LLM inflection points in twelve months

> Willison's retrospective names three capability inflection points (Opus 4.5 coding reliability, "Fable class" goal-driven models, Opus 5.5 game "fun"/3D modeling) and a working definition of "Fable class" as the new frontier baseline; all evidence is first-person anecdote (n=1, no metrics).

## Source Context

- **Type**: blog-post (single-author retrospective, written from a keynote at the AI Engineer Code Summit)
- **Author credibility**: Simon Willison, prolific hands-on LLM tooling practitioner (Datasette, LLM CLI); claims rest entirely on his own daily use and side projects.
- **Scope**: Timeline and framing of three inflection points plus a tentative "is Fable 5.2 a fourth?" section. Mostly links to his earlier posts for evidence; no measurements, no comparisons beyond his own impressions. The "Fable class" definition itself appears only as an image (slide) in the post; its alt text reads "Inflection point 2: Fable class models If you can define a goal and provide necessary tools They can solve your problem with brute force".

## Extracted Claims

### Claim 1: Opus 4.5 (Nov 2025) was the first model where Claude Code's default output was generally right, making it a daily driver
- **Evidence**: Personal experience; he had previously not used Claude Code daily because he had to correct it too often.
- **Confidence**: anecdotal
- **Quote**: "Opus 4.5 was the first model I had used with Claude Code where the default result was generally the right thing."
- **Our assessment**: Plausible and consistent with wider practitioner reports, but a single user's threshold of "reliable enough". The useful signal is the criterion: the shift from "I must correct it often" to "default result is right".

### Claim 2: GPT-5.1 family had a similar effect on Codex in the same month
- **Evidence**: Personal experience, no specifics.
- **Confidence**: anecdotal
- **Quote**: "These had a similar effect on their Codex coding agent: it became reliably useful for many of my coding tasks."
- **Our assessment**: Corroborates the cross-vendor nature of the Nov 2025 shift; thin on detail.

### Claim 3: Holiday tinkering in Dec 2025 turned into real work usage by Jan 2026
- **Evidence**: Anecdote about "a lot of people, myself included".
- **Confidence**: anecdotal
- **Quote**: "By January we were ready to use them for our actual work."
- **Our assessment**: Describes an adoption lag between capability and workflow integration; useful framing, unmeasured.

### Claim 4: "Fable class" models are those that, given a goal and the necessary tools, solve problems by brute force
- **Evidence**: Definition given on a slide (image alt text); supported by two of his earlier posts (Safari debugging, beep finder).
- **Confidence**: anecdotal
- **Quote**: "Give it a goal, give it the right tools, and watch it cook."
- **Our assessment**: A useful, if informal, taxonomy: the defining trait is proactive tool acquisition/use toward a goal, not benchmark scores. The definition text itself is only in the slide alt text ("If you can define a goal and provide necessary tools They can solve your problem with brute force"); the prose gives only examples.

### Claim 5: Fable-class membership list and the "frontier baseline" expectation
- **Evidence**: His own judgment of which models behaved this way.
- **Confidence**: anecdotal
- **Quote**: "I’d currently class Claude Fable 5, 5.1, 5.2 and Claude Opus 5.5 as Fable class (I think of Opus 5.5 as “cheap Fable”)."
- **Our assessment**: Also "These now represent the baseline for what I expect from a frontier model." GPT-6 Astra is included; Gemini 4 Neon is hedged ("may count"). Treat as one practitioner's classification, not a standard.

### Claim 6: Fable proactively built its own verification/debug tooling (screenshot mechanism, localhost logging server)
- **Evidence**: Recap of an earlier post: Safari display glitch fixed after Fable spun up a pyobjc-framework-Quartz screenshot mechanism and a CORS-enabled localhost logging server.
- **Confidence**: anecdotal
- **Quote**: "it spun up its own pyobjc-framework-Quartz screenshot mechanism and a CORS-enabled localhost logging server to help resolve the bug"
- **Our assessment**: Not new (detail lives in the earlier note) but here it is used as the exemplar of agents choosing their own verification tools.

### Claim 7: Opus 5.5 then Fable 5.2, given five WebAudio microphones, triangulated a beep to about 40cm
- **Evidence**: His beep finder project (earlier post); single physical room, no ground-truth error analysis in this post.
- **Confidence**: anecdotal
- **Quote**: "it was able to triangulate the source of an infuriating mysterious beep to within about 40cm"
- **Our assessment**: Concrete but self-reported; the 40cm figure is approximate and unvalidated here.

### Claim 8: Frontier LLMs became "really good" at 3D modeling in roughly the last four months (Blender or Three.js)
- **Evidence**: Own observation across Fable 5, Opus 5.5, GPT-5.6 Sol, GPT-6 Astra, Gemini 4; one linked Gemini 4 Neon demo.
- **Confidence**: anecdotal
- **Quote**: "Set them up with Blender or ask them to write Three.js code and they’ll produce credible models of almost anything you ask for."
- **Our assessment**: Plausible; "credible" is subjective. He explicitly says he does not know whether 3D ability is a side effect of robotics-oriented spatial-awareness work "or vice-versa".

### Claim 9: Opus 5.5, told "make it a LOT more fun", turned a boring RTS into a deeply entertaining one after 12 hours of self-playtesting and rebalancing
- **Evidence**: One game project (Command & Conquer-style RTS), author's subjective judgment of "fun".
- **Confidence**: anecdotal
- **Quote**: "This game isn’t fun enough yet. Make it a LOT more fun."
- **Our assessment**: Notable because it reverses his own Sept 2026 claim that fun design was uniquely human. Fun is not verifiable by automated checks, so the "12 hours" is agent-run playtest/rebalance loop plus a human taste verdict. Follow-up: "Think hard about how to make sure it is both fun and beautiful" kept him engaged "for significant amounts of time".

### Claim 10: Opus 5.5 "appeared to understand fun"
- **Evidence**: Same RTS plus several small games; second-hand reports of "proper, worthwhile games" shown at two conferences.
- **Confidence**: anecdotal
- **Quote**: "Opus 5.5 was the first model I’d used that appeared to understand fun."
- **Our assessment**: Hedged by "appeared"; do not state as a capability finding. The conference anecdotes are unattributed.

### Claim 11: Whether Fable 5.2 is a fourth inflection point is undecided; if so, the feature is "imagine and clearly describe it → Fable can build it"
- **Evidence**: A three-week flood of releases (Datasette 1.0a42-1.0a44, LLM 0.37-0.38) and his sense that the model's taste matches his own.
- **Confidence**: anecdotal
- **Quote**: "I’m still trying to decide if Fable 5.2 represents a new inflection point, or just another incremental improvement."
- **Our assessment**: Speculation by the author's own account; do NOT cite as a finding. The release cadence is a weak productivity proxy (release count ≠ value). Related line: "if you can imagine and then clearly describe a piece of software, Fable can build it".

## Concrete Artifacts

Timeline as stated by the author (dates from the post):

```
2025-02-24  Claude Code introduced alongside Claude 3.7 Sonnet
2025-11     Opus 4.5 (released 2025-11-24) + GPT-5.1 / GPT-5.1-Codex(-Max): coding agents become reliable
2026-04     Claude Mythos announced, withheld as "too dangerous" (cybersecurity)
2026-06     Claude Fable 5 released; ~3 days later placed under US export controls; back July 1
2026-08     Raccoon heist game (Fable 5) fun-poor; GPT-5.6 Sol Ultra better but dull after ~90s
2026-09-22  Opus 5.5 released
2026-10     "Make it a LOT more fun" RTS result (12h playtest/rebalance)
2026-11     Beep finder (Opus 5.5 -> Fable 5.2, ~40cm)
```

Prompts quoted in the post:

```
"This game isn’t fun enough yet. Make it a LOT more fun."
"Think hard about how to make sure it is both fun and beautiful"
```

## Cross-References

- **Corroborates**: `blog-simonwillison-vibe-game-development.md` Claims 1-3 (Opus 5.5 game-design inflection; generic "make it more fun" prompt); `blog-simonwillison-fable-relentlessly-proactive.md` Claim 3 (self-built CORS server) and Claim 9; `blog-simonwillison-mysterious-beeps.md` Claim 1 (agent given a perception channel); `blog-simonwillison-raccoon-heist.md` Claim 9 (technically impressive but gameplay-mediocre, which this post cites as the "before" state); `blog-simonwillison-claude-fable-5.md` (Fable 5 release context).
- **Contradicts:** none filed. Internal tension: his Sept 2026 talk claimed fun design stays human (see `blog-simonwillison-2026-in-llms-so-far.md`); this post reverses that, which is a self-correction, not a contradiction between sources.
- **Extends**: `blog-simonwillison-fable-5-export-controls.md` (timeline: 3 days of access, restored July 1); `blog-simonwillison-opus55-gpt6-sol-luna-price-war.md` (Opus 5.5 date, "cheap Fable" framing).
- **Novel**: The "Fable class" taxonomy and model list; the Opus 4.5 "default result is right" threshold as the first inflection; the explicit three-inflection timeline; the 3D-modeling capability claim; the admission that the Fable 5.2 inflection call is undecided.

## Guide Impact

- **Chapter 00**: Could cite this as one practitioner's framing that the frontier baseline moved to "goal + tools → brute-force solution", labeled anecdotal; avoid presenting the model list as authoritative.
- **Chapter 01**: Add the Opus 4.5-era threshold (default output right without frequent correction) as a signal for when to make an agent a daily driver; note the Dec-to-Jan adoption lag.
- **Chapter 03**: Add "fun/taste" as a hard-to-verify quality dimension: the agent can run a 12-hour playtest loop, but the acceptance judgment remains the human's subjective one (n=1).
- Do not add the Fable 5.2 inflection speculation to the guide.

## Extraction Notes

- Read the full post (fetched raw HTML). The "Fable class" definition is an embedded slide image; only its alt text was readable, quoted above. The linked talk video and earlier posts were not re-read; evidence relies on existing source notes for them.
- Opus 4.5's one-year anniversary is stated as 24 Nov 2026 in the post.
- All quotes copied verbatim from the post (apostrophes are typographic as in the source).
