---
source_url: https://www.latent.space/p/rlm
source_type: blog-post
title: "Academia is for Ambition — Alex Zhang, MIT"
author: Latent Space (Shawn "swyx" Wang and Vibhu, interviewing Alex Zhang)
date_published: 2026-10-02
date_extracted: 2026-10-15
last_checked: 2026-10-15
status: current
confidence_overall: anecdotal
issue: "#4137"
---

# Academia is for Ambition — Alex Zhang, MIT

> First-person account from the Recursive Language Model (RLM) paper's first author of what an RLM is as a harness design (code as the only tool, context held in a code environment, recursive subagent calls), why he thinks Claude Code, Codex and Pi are structurally the same, and why he thinks single-agent harnesses leave capability on the table.

## Source Context

- **Type**: blog-post (podcast interview with full transcript, ~1h41m; timestamps cited below)
- **Author credibility**: Alex Zhang is an MIT PhD student, first author of the RLM paper, co-creator of KernelBench, and a contributor to Prime Intellect's Prime Agent. He is the originator of the pattern, so his definitions are authoritative; his benchmark and forward-looking claims are not independently verified here. Hosts are Latent Space's swyx and Vibhu.
- **Scope**: Roughly 40% of the 100 minutes is relevant to the guide (00:31:01-00:57:41 harness and RLM mechanics, 01:00:30-01:07:26 swarms, 01:15:52-01:25:13 swarm convergence and capability overhang). The rest covers GPU kernels, research taste in academia, Jev (a non-autoregressive model), open-endedness/Sakana, and Neuralese. There are no code samples, configs or tables; the transcript refers to figures and a blog ("harnesses as compositional generalizers") shown on screen that are not reproduced in the text. Results cited for Prime Agent and OpenAI swarms are secondhand or internal ("these are all internal results").

## Extracted Claims

### Claim 1: An RLM is a harness design in which code is the only tool, the model can call itself as a function, and all context lives in a code environment
- **Evidence**: Author's definition as originator; Prime Agent used as the worked example (trajectory, including after compaction, stored on disk; tools run inside an IPython/Bash REPL).
- **Confidence**: emerging (definition is authoritative; effectiveness evidence is elsewhere, e.g. the paper)
- **Quote**: "An RLM is basically just a harness design where the only tool in the harness is code, which is this programmatic subagent calling thing, where it has the option to call itself as a tool, and it has other tools." (00:44:24)
- **Our assessment**: The clearest first-party definition we have. It shifts the framing from "RLM = long-context trick" (how our existing Nemotron note describes it) to "RLM = a harness architecture". Useful for Ch02 as an alternative to the tool-call-per-turn loop.

### Claim 2: The original RLM motivation was long context, but the author now frames the point as composition over a central, persistent context rather than one tool call per turn
- **Evidence**: Author's account of how the framing evolved; contrast with agent swarms that use a message board as shared context.
- **Confidence**: emerging
- **Quote**: "tool calls are very limited because you have to invoke them every turn." (00:46:02)
- **Our assessment**: Credible as a design argument (it explains why code can express loops/fan-out that sequential tool calls cannot). No measured comparison is given in the interview.

### Claim 3: Claude Code, Codex, Pi and similar harnesses are essentially the same design, so choosing between them matters little
- **Evidence**: Author's reading of the designs, plus the "harness tax" paper (attributed by Zhang to Arena; not read by us) which he says confirms his prior.
- **Confidence**: anecdotal
- **Quote**: "Claude Code, Codex, Pi, et cetera, are all the same in that, like, when you break down the logic of the harness, it's, like, virtually the same thing." (00:49:54)
- **Our assessment**: Plausible at the loop level, but the claim is broad and the cited paper is unverified. He concedes exceptions (Grokbot, RLM-style harnesses). Treat as one expert opinion; note it conflicts in spirit with the guide's emphasis on harness configuration details (see Cross-References).

### Claim 4: Most mainstream harnesses use "trajectory as a prompt", which pushes long tasks out of distribution; RLMs keep every individual model call "locally in distribution"
- **Evidence**: Conceptual argument illustrated by a figure in the author's blog; no numbers given in the interview.
- **Confidence**: emerging (conceptual, untested in the interview)
- **Quote**: "if an RLM breaks down its computation into, like, kind of a meta-harness of sorts or, like, a program that involves subagents that, like, look at a local problem, every individual language model call over the course of this task is in distribution, even if the entire task itself is out of distribution." (00:46:02 section)
- **Our assessment**: Offers a mechanism for why decomposition beats a single growing context, which complements the guide's context-engineering advice. It remains a hypothesis; the guide should cite it as the author's argument.

### Claim 5: Training an RLM on short tasks generalizes to much longer and even different-domain tasks because the high-level strategy is the same
- **Evidence**: Plots in the author's blog (shown on screen, not in transcript); host summarizes as training on short tasks generalizing to tasks 8-30x longer. Author says Pi/Claude Code harnesses "distinguish too much between these problems" in results not published in the blog.
- **Confidence**: anecdotal (results referenced but not reproduced; unpublished comparison)
- **Quote**: "as you just naively train your RLM on these tasks, they naturally learn to generalize, for example, to longer tasks, because the strategy is basically the same." (00:31:01 section)
- **Our assessment**: Interesting but relevant mainly to model training, not to day-to-day harness use. Do not cite the 8-30x figure as the author's own; it comes from the host's reading of the blog.

### Claim 6: Prime Agent is Pi restricted to IPython as the sole tool, with a "continual harness" letting the agent modify its own skills, subagents and system prompt, plus code-driven agent-to-agent messaging and persistent subagents
- **Evidence**: Author's description of a system he co-built. Prime Intellect announcement (tweet embedded in the post) calls it "A self-improving RLM harness" built around programmatic tool calling, context as a variable, multi-agent messaging and self-modifiable harness state.
- **Confidence**: emerging
- **Quote**: "But it is Pi, except we explicitly restrict IPython to be the only tool that's available to it." (00:53:57)
- **Our assessment**: Concrete architecture worth recording. The persistent-subagent point maps directly onto a limitation swyx names in Codex (ephemeral subagents).

### Claim 7: Persistent subagents plus externalizing state to the filesystem is the practical trick for long-running multi-agent work
- **Evidence**: Author's description of Prime Agent's persistent subagents; swyx reports ephemeral Codex subagents as his "number one pain".
- **Confidence**: anecdotal
- **Quote**: "And you can go into that subagent, you can prompt it more, like, you have more visibility and flexibility into what is kind of going on." (00:53:57 section)
- **Our assessment**: Consistent with the filesystem-as-memory pattern already in our corpus. Also, in the exchange, swyx: "So the trick is just externalize to a file system, right?" and Zhang answers "That is the big trick."

### Claim 8: Harness details matter little for the strongest models; what matters is how agents are composed, and swarm results do not show that a harness was essential
- **Evidence**: Zhang's interpretation of OpenAI's reported swarm result (secondhand; he says he is "not sure" about parts of it) and the harness-tax paper.
- **Confidence**: anecdotal
- **Quote**: "the specific details of a harness do not really matter" (01:00:30 section)
- **Our assessment**: Speculation about a closed system. Useful as a counterweight to harness-tuning advice, but cannot be verified.

### Claim 9: Much of a large agent swarm is probably wasted search, and getting a swarm to converge on an answer is non-trivial
- **Evidence**: Author's estimate and opinion; host-supplied figures for the OpenAI run (10,000 agents, 88 hours, 130B output tokens, ~$40M at public pricing). These numbers come from swyx in conversation, not from a primary source; we have not verified them.
- **Confidence**: anecdotal
- **Quote**: "We take for granted what it means for a swarm to converge to an answer." (01:15:52 section)
- **Our assessment**: The 95% figure ("Fairly certain that, like, 95% of the swarm is entirely useless") is a guess, explicitly hedged. The convergence point is the transferable one: more agents is not the same as more progress. He also judges Kimi swarms and Claude Code's dynamic workflows as less convincing, which is opinion.

### Claim 10: Use cheaper mechanisms (compaction) by default and reach for RLMs/swarms only when the task justifies the cost
- **Evidence**: Author's analogy.
- **Confidence**: anecdotal
- **Quote**: "there are many settings where an RLM can solve maybe a more difficult task than compaction can, but you would prefer to use compaction in most cases because it's cheaper and it's quicker." (01:04:53 section)
- **Our assessment**: Sensible and aligns with cost-aware guidance; no data given.

### Claim 11: Speculative programmatic tool calling (launch tools before the model finishes writing the code) is an obvious win for code-driven agents
- **Evidence**: Author's one-line description; no measurements in the interview.
- **Confidence**: anecdotal
- **Quote**: "a lot of tools tend to be, like, sequential or, like, you have to wait on them, so you should just launch them in advance." (01:20:06)
- **Our assessment**: Latency optimization idea only; speculative side effects are not discussed, so be careful about applying it to non-idempotent tools.

### Claim 12: Current frontier models have capability overhang: a harness for long-running but simple tasks done reliably could close the gap
- **Evidence**: Opinion and thought experiment (a month-long job done "as good as ... some 18-year-old high school kid"); no experiment.
- **Confidence**: anecdotal
- **Quote**: "Do long-running but simple tasks, and do them reliably." (01:21:36 section)
- **Our assessment**: Framing, not evidence. The triage comment asked that this be treated as opinion.

### Claim 13: The "language model" users query may in future be a hidden swarm or scaffold behind a simple front end
- **Evidence**: Author's prediction; references a blog he wrote.
- **Confidence**: anecdotal
- **Quote**: "what we think of as a language model, like the thing that we query, might actually be like a swarm or like a scaffold or like some Weird harness design that scales very well, but the user just doesn't see it." (01:00:30 section)
- **Our assessment**: Forecast. Not guide material.

### Claim 14: Third-party RLM adoption: Harvey post-trained an RLM on legal work; DSPy has an RLM; several ARC-AGI-3 Kaggle harnesses reference RLM-style abstractions
- **Evidence**: Zhang's recollection of others' work ("not affiliated"); no numbers.
- **Confidence**: anecdotal
- **Quote**: "Harvey, the legal AI company, released a blog post, not affiliated at all, but they post-trained an RLM on their, like, legal work" (00:57:41)
- **Our assessment**: Leads for further sourcing only. The header tweet claiming an RLM harness "~solve[d] ARC-AGI-3" is editorial framing by the hosts and was not substantiated in the transcript.

## Concrete Artifacts

```
Prime Intellect announcement (embedded tweet, 5 Aug 2026), as reproduced in the post:
"Introducing Prime Agent:
A self-improving RLM harness for coding and long-running autonomous tasks.
Designed to be both token-efficient and expressive through programmatic tool calling, context as a variable, multi-agent messaging, and a self-modifiable harness state."
```

Prime Agent structure, summarized from Zhang (00:52:01-00:57:41; paraphrase, not a quote): built on Pi Mono; IPython is the only exposed tool; other tools load as Python modules or Bash scripts; trajectory persisted on disk; a "continual harness" tool lets the agent edit its own skills, available subagents and system prompt; code-defined agent-to-agent messaging; persistent subagents that outlive the root agent's run and can be re-prompted.

Figures reported by the host about OpenAI's swarm experiment (secondhand, 01:04:29): 10,000 agents, 88 hours, 130 billion output tokens, ~$40 million at public pricing.

## Cross-References

- **Corroborates**: `blog-latentspace-socher-recursive-eureka-machine.md` (recursive agent loops, same podcast); `blog-lilianweng-harness-engineering-rsi.md` (harness as the thing to improve, self-modifying harness). The filesystem-as-memory theme matches `blog-ghuntley-agency-nobody-types-code.md` only loosely and was not verified claim by claim.
- **Contradicts**: None filed. Zhang's "harness choice matters little" (Claim 3, Claim 8) sits in tension with the guide's heavy emphasis on harness configuration, but it is a scope difference (frontier-model loop structure vs. per-project configuration), not a direct opposition to any specific source note claim, so no contradiction issue was opened.
- **Extends**: `blog-thebatch-nemotron-agent-infra.md` Claim 10 (RLMs treat prompts as external Python variables, with BrowseComp+ results): this source adds the originator's reframing as a general harness design and the Prime Agent implementation. `blog-addyosmani-code-agent-orchestra.md` and `blog-cursor-agent-swarm-model-economics.md` (swarm/subagent orchestration, Cursor's org-chart swarm is discussed by the hosts at 01:04:53): this adds a skeptical take on swarm waste and convergence.
- **Novel**: First-party definition of RLM as "code is the only tool"; "trajectory as a prompt" vs "locally in distribution" argument; Prime Agent's continual harness and persistent subagents; speculative programmatic tool calling.

## Guide Impact

- **Chapter 02 (harness engineering)**: Consider adding a short "alternative loop architectures" note: the standard loop (Claude Code/Codex/Pi) vs. a code-only RLM-style harness with context stored in a REPL/filesystem and persistent subagents, attributed to Zhang as the originator's account (anecdotal). Do not present as validated.
- **Chapter 04 (context engineering)**: The "trajectory as a prompt" vs "context as a variable on disk" contrast, and the compaction-first-RLM-when-needed cost guidance (Claim 10), are candidates for a sidebar. Keep the training-generalization claims (Claim 5) out of the guide.
- **Swarm guidance**: If the guide discusses swarms, add the caution that scale does not guarantee convergence (Claim 9), with the 95%-wasted figure explicitly marked as a guess.
- Recommend sourcing the primary RLM paper, the "harnesses as compositional generalizers" blog, and the "harness tax" paper before citing any quantitative claim.

## Extraction Notes

- Read the full transcript (fetched raw HTML and stripped markup). Quotes were copied from that text; some transcript lines contain stutters, which I trimmed only by choosing contiguous fragments.
- The page text for a few long speaker turns was truncated in the page itself (mid-word), so quotes were taken from complete portions only.
- Did not follow linked pages (the blog, paper, and tweets are referenced on-screen but not linked in the transcript text). Claims about those documents are Zhang's description, not verified.
- Interview is mostly opinion; hence `confidence_overall: anecdotal`.
