---
source_url: https://latent.space/p/codex-work/
source_type: blog-post
title: "AI Engineer Code Summit: OpenAI on New Ways of Working With Codex"
author: Richard MacManus
date_published: 2026-11-10
date_extracted: 2026-11-25
last_checked: 2026-11-25
status: current
confidence_overall: anecdotal
issue: "#4947"
---

# AI Engineer Code Summit: OpenAI on New Ways of Working With Codex

> A secondhand workshop recap (OpenAI DevEx engineers Dominik Kundel and Charlie Guo) that contributes two narrow practitioner points: local-to-cloud Codex handoff is still awkward, and "voice as a control plane" (managing threads, not just dictating) is a distinct usage pattern from voice dictation; plus first-hand usage habits for OpenAI's "dots" personal agent.

## Source Context

- **Type**: blog-post (conference workshop report, ~6 min read, plus the author's after-session Q&A with Kundel)
- **Author credibility**: Richard MacManus writes for Latent Space and attended the workshop in person. The speakers are OpenAI Developer Experience engineers, so the product claims are vendor-presented; MacManus's own friction report is independent.
- **Scope**: Codex cloud transition, voice usage, and dots. No code, configs, or metrics. The full article was readable, including the Dots and Conclusion sections (an earlier triage comment thought they were truncated).

## Extracted Claims

### Claim 1: Codex Cloud was an awkward experience until the v2 revamp announced at DevDay
- **Evidence**: Speaker admission plus author narrative; no usage data.
- **Confidence**: anecdotal
- **Quote**: "it took a while for models and harnesses to equalize into something where we can build a really engaging experience."
- **Our assessment**: Credible as a candid vendor admission; it corroborates the guide's view that harness/model maturity gates cloud-agent usability. Quote is Kundel's, as relayed by MacManus.

### Claim 2: Codex Cloud v2 environments are publish-once and reusable across tasks, shareable within a company
- **Evidence**: Quoted from the official workshop writeup and Kundel's description.
- **Confidence**: anecdotal
- **Quote**: "publish an environment once and run multiple tasks in isolated instances of that setup."
- **Our assessment**: Product description (vendor-sourced); consistent with environment-reuse patterns elsewhere. Little new.

### Claim 3: Local-to-cloud handoff remains confusing, even to a close observer, and the vendor concedes it
- **Evidence**: MacManus's own experience, Kundel's reply, and a demo in which a reopened cloud task still had its local Appshot (a capture of a Mac app window) attached.
- **Confidence**: anecdotal
- **Quote**: "We definitely want to have it be easier,"
- **Our assessment**: The most useful point in the note. The friction is context differences between local and cloud; Kundel's workaround was asking local Codex to hand the task off. Single-observer evidence, but the vendor confirmation makes it a credible friction point.

### Claim 4: Local and cloud Codex are converging; the cloud is "just a background executor" that local Codex can dispatch to
- **Evidence**: Kundel's statement in post-workshop Q&A; no demo of local-to-cloud spawning beyond his anecdote.
- **Confidence**: anecdotal
- **Quote**: "just a background, like a different executor of where things are happening,"
- **Our assessment**: Direction-of-travel statement, vendor framing. Useful as a harness-architecture signal (executor abstraction), not as a verified capability.

### Claim 5: Voice is better treated as a control plane over many threads than as a dictation medium
- **Evidence**: Guo's personal practice, stated as contrast with what he sees most people do.
- **Confidence**: anecdotal
- **Quote**: "Most people I see that use voice with coding essentially treat it as just a different medium on top of their normal work,"
- **Our assessment**: A distinct framing from dictation-only voice use. Guo's list ("How do I manage my threads? How do I check in on stuff? ... How do I create new threads in the application?") is a concrete usage pattern, but no evidence of effectiveness is offered.

### Claim 6: Voice dictation speeds up exploratory iteration when the desired outcome is unclear
- **Evidence**: Live demo editing a fictional record-company site ("Blossom Music"); Kundel's comment.
- **Confidence**: anecdotal
- **Quote**: "You can really quickly iterate on these things and get to a world that you're actually envisioning with your stuff, especially if you're unsure what you actually want to get to,"
- **Our assessment**: Plausible, demo-level only.

### Claim 7: A personal agent with access to dev boxes, laptop, and cloud environments can be voice-driven to start PRs asynchronously (e.g., while commuting)
- **Evidence**: Kundel's self-reported habit.
- **Confidence**: anecdotal
- **Quote**: "start up some PRs while I'm driving, so that when I come home or when I come to the office, I can go and review them."
- **Our assessment**: Illustrates the delegate-now/review-later loop; the human review step is preserved. Self-report, no failure data.

### Claim 8: Guo finds dots useful as a safety net, a "delegation sink", and a ubiquitous presence, but calls them awkward for Codex power users
- **Evidence**: Guo's power-user opinion; MacManus notes dots were only briefly discussed.
- **Confidence**: anecdotal
- **Quote**: "As a Codex power user, dots feel a little bit awkward to work with,"
- **Our assessment**: Candid and notable that a vendor engineer says so. The three uses are named but not elaborated beyond Slack for delegation.

### Claim 9: Kundel starts many tasks from his dot rather than from Codex because it already holds context
- **Evidence**: Self-report.
- **Confidence**: anecdotal
- **Quote**: "it often already has a lot of the context and understands how to manage things, and it can push these PRs forward for me."
- **Our assessment**: Suggests persistent cross-surface context as the value of a personal agent; vendor-employee usage, so treat with caution.

### Claim 10: Do not get attached to the current way of working
- **Evidence**: Closing advice, summarized by MacManus (tips included lowering effort level and asking agents for help).
- **Confidence**: anecdotal
- **Quote**: (no direct quote; see paraphrase in Our assessment)
- **Our assessment**: Kundel's closing point per the author is that "things are constantly changing"; generic, but matches the guide's stance on tooling volatility.

## Concrete Artifacts

No code, config, or metrics. The only concrete items are Kundel's tip list ("turn it down" for effort level; "ask your agents for help") and the workflow of handing a local task to cloud by asking Codex to do it (source: MacManus's account of the workshop).

## Cross-References

- **Corroborates**: `blog-simonwillison-openai-devday-2026-live-blog.md` Claim 4 (dots emerged from the Codex harness becoming reliable on longer tasks) and Claim 1 (user-controlled delegation); Claim 13 there (voice front-end delegating to stronger background executors) matches Claim 5/7 here. `blog-simonwillison-gptlive-voice-delegation.md` Claim 1 describes the model-side background delegation that voice control-plane use relies on.
- **Contradicts**: None filed. Mild tension with `blog-simonwillison-voice-mode-weaker.md` (voice mode as a weaker interface); this is a difference of context and use pattern, not a contradiction.
- **Extends**: `blog-openai-codex-knowledge-work.md` and `blog-latentspace-openai-devday-cua-and-api-interview.md` (Codex/DevDay coverage) with candid friction on local-to-cloud handoff.
- **Novel**: The "voice as control plane" vs "voice as medium" distinction; vendor acknowledgment that local-to-cloud handoff is confusing; dots as "delegation sink" in Slack.

## Guide Impact

- **Chapter 01**: Add voice-as-control-plane (manage/check in on/create threads) as a distinct pattern next to dictation, attributed to Guo as an anecdote.
- **Chapter 02**: In cloud/background-executor discussion, note local-to-cloud handoff as an unresolved friction point (context differences), citing Claim 3-4, flagged as anecdotal and vendor-confirmed.

## Extraction Notes

Read the full page (all sections). Prospector asked for narrow extraction; I included dots claims since the section was available, marked anecdotal. Quotes are copied from the fetched page text; the page text is MacManus's relay of spoken remarks. No sub-pages followed (workshop writeup on ChatGPT Sites was not linked in readable form).
