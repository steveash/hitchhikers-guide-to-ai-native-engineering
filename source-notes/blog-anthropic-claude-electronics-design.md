---
source_url: https://www.anthropic.com/research/claude-electronics-design
source_type: blog-post
title: "Claude can design electronic prototypes from start to finish"
author: Anthropic (Science team), with Diode Computers
date_published: 2026-11-09
date_extracted: 2026-11-11
last_checked: 2026-11-11
status: current
confidence_overall: emerging
issue: "#4641"
---

# Claude can design electronic prototypes from start to finish

> A vendor case study in which Claude Fable 5.2 designed three PCB-based devices with Diode Computers; it shows self-revision, writing a bespoke tool (a grid router) when the stock tool was too coarse, code-based constraint checks (enclosure fit), and on-demand datasheet reading, while humans built and tested the hardware.

## Source Context

- **Type**: blog-post (anthropic.com/research, published 2026-11-09)
- **Author credibility**: Anthropic first-party research post. Acknowledgements credit Diode Computers staff; Anthropic has worked with Diode on PCB design since 2025. Vendor-authored: the model, one benchmark (PCB Gym) and the framing are Anthropic's own.
- **Scope**: Three prototype devices (USB speakerphone, voice-assistant hub, handheld virtual pet), two benchmark numbers, qualitative descriptions of Claude's behaviours, and a limitations section. Does NOT cover: token/time cost, number of human interventions, failure cases, or the prompts/harness used.

## Extracted Claims

### Claim 1: Claude Fable 5.2 can design and prototype electronic hardware end to end
- **Evidence**: Three devices designed by Claude and manufactured by Diode; per the post all still worked after weeks of use, and Diode built all three without design-change rounds.
- **Confidence**: emerging (n=3, single collaborator, vendor-reported)
- **Quote**: "Claude can both design and prototype electronic hardware from start to finish."
- **Our assessment**: Credible as a capability demonstration; "start to finish" is bounded by the post's own limitations (Claude had no access to test equipment or machines; humans built and tested). Do not generalize to production hardware.

### Claim 2: Claude revised its own work substantially, discarding layouts rather than patching them
- **Evidence**: Narrative description: reassigned pins, rerouted boards dozens of times, redid a crowded area judged untraceable.
- **Confidence**: anecdotal
- **Quote**: "It proceeded to delete and reroute copper connections dozens of times until it found an arrangement that worked."
- **Our assessment**: A concrete example of "throw away and redo" self-correction in a physically constrained domain. The triage question of whether this was prompted is not answered by the post as retrieved; treat it as unspecified.

### Claim 3: When the stock tool was too slow, Claude wrote its own tool (a grid-based router)
- **Evidence**: Post says KiCad's one-track-at-a-time router was too slow for long tracks, so Claude wrote a router that divides the board into a grid, and tuned it to keep sensitive tracks clear.
- **Confidence**: anecdotal
- **Quote**: "Claude wrote its own router: an algorithm that divides the board into a grid"
- **Our assessment**: Strong parallel to "build the tool you need" patterns. Evidence is descriptive only, no code or timing data shown.

### Claim 4: Claude verified physical constraints with code, catching a fit problem
- **Evidence**: It checked a 3D model of the board against the enclosure; the speakerphone board had to be tilted about 25 degrees during installation. It also tuned the microphone port resonance from about 3.4 kHz to about 8.9 kHz via a wedge-shaped enclosure.
- **Confidence**: anecdotal
- **Quote**: "check that a 3D model of the circuit board would fit inside the enclosure"
- **Our assessment**: A programmatic verification step substituting for a physical test; the numbers are as reported by the vendor and unverified by us.

### Claim 5: Claude read datasheets to make part-specific decisions
- **Evidence**: Example: predicting that the charging LED would flicker without a battery.
- **Confidence**: anecdotal
- **Quote**: "predicted that the charging light would flicker, because the charger keeps recharging a small capacitor in the battery's place."
- **Our assessment**: Illustrates on-demand retrieval of authoritative docs as context rather than relying on parametric memory.

### Claim 6: Claude triaged manufacturing (DFM) checks, fixing real issues and ignoring a false positive
- **Evidence**: Fixed six thin solder-mask slivers; judged a ground-connection flag harmless.
- **Confidence**: anecdotal
- **Quote**: "Claude correctly reasoned that it wouldn't affect performance and ignored the flag."
- **Our assessment**: Useful for the guide's point that verification output needs judgment, not blind compliance with every flag. Who adjudicated "correctly" is Anthropic/Diode.

### Claim 7: Benchmarks show a large jump over predecessors
- **Evidence**: PCB Gym (Anthropic-internal): 69% vs 25% for Fable 5. BenchCAD 2.1 (public, per the post's link): 83.5%, nearly double Fable 5.1.
- **Confidence**: emerging
- **Quote**: "Fable 5.2 scored 69% on the benchmark, compared with 25% for Fable 5"
- **Our assessment**: Attribute to the vendor; PCB Gym is not independently reproducible. Directionally useful.

### Claim 8: The prototypes carry explicit limits; humans did the physical build and test
- **Evidence**: Limitations paragraph; Claude had no connection to test equipment or manufacturing machines; Diode engineers built and tested.
- **Confidence**: settled (the post's own statement)
- **Quote**: "they haven't been through electrical validation, antenna tuning, thermal testing, or certification"
- **Our assessment**: The human-in-the-loop role (build, measurement) is part of the pattern. Planned next steps (simulation-based verification, learning from measurements of finished devices) imply the loop is not yet closed.

### Claim 9 (from linked Diode article): Domain improvements came from a custom testbench checking requirements, not exact parts, plus human blind review
- **Evidence**: Linked page https://claude.com/resources/articles/making-claude-a-better-electrical-engineer: designs in the Zener DSL were graded by a testbench of higher-level requirements; Diode engineers' blind comparisons preferred Sonnet 4.5 designs 8 of 10 times.
- **Confidence**: emerging
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Requirement-level (rather than exact-output) graders are a transferable eval design idea. Secondary page, only skimmed.

## Concrete Artifacts

```
Reported results (Anthropic, anthropic.com/research/claude-electronics-design, 2026-11-09)
Devices: USB speakerphone; voice-assistant hub; handheld virtual pet
PCB Gym (internal):  Fable 5.2 = 69%   Fable 5 = 25%
BenchCAD 2.1:        Fable 5.2 = 83.5% (nearly 2x Fable 5.1)
Speakerphone: board tilted ~25 deg on install; mic port resonance ~3.4 kHz -> ~8.9 kHz
DFM: 6 solder-mask slivers fixed; 1 ground-connection flag ignored as false positive
```

## Cross-References

- **Corroborates**: `blog-anthropic-claude-code-verification-loops-skills.md` Claim 1 (verification loop = check-and-attempt-fix) is illustrated here by a non-software domain.
- **Contradicts**: none found; no contradiction issue filed.
- **Extends**: `blog-anthropic-claude-design-product-designer-workflow.md` Claim 7 (Claude builds a bespoke video editor, then uses it) parallels Claude writing its own router. `blog-thebatch-nvidia-chip-design-robotics.md` Claim 9 (end-to-end GPU design from a prompt is a "distant goal") is a different domain/scale; boards here are simple prototypes.
- **Novel**: First note in the corpus on AI-driven PCB/electronics design, physical-world verification gaps, and Diode collaboration.

## Guide Impact

- **Chapter 03**: Add as a cross-domain example of self-revision and triage of verification flags (fix real DFM issues, ignore false positives), noting that physical build/test stayed human.
- **Chapter 02**: Cite Claim 3 as an example of an agent writing a purpose-built tool when a stock tool is too coarse; flag as anecdotal.
- **Chapter 04**: Cite Claim 5 for consulting authoritative docs on demand for part-specific decisions.
- Any capability claim should carry the caveat: n=3, vendor-run benchmarks, no certification.

## Extraction Notes

- The fetch tool returns summarized/paraphrased text, not raw page text. Quotes were obtained via a targeted excerpt request and are short fragments; the Assayer should spot-check them against the live page.
- Whether Claude's revisions were prompted is not established by the retrieved text.
- Followed one linked page (Diode collaboration article); the BenchCAD and OpenAI links were not followed.
