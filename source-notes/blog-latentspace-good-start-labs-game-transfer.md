---
source_url: https://www.latent.space/p/good-start-labs
source_type: blog-post
title: "Can Skills Learned in Games Transfer to Real-World Work?"
author: Richard MacManus (Latent Space), interviewing Alex Duffy (Good Start Labs)
date_published: 2026-09-15
date_extracted: 2026-09-30
last_checked: 2026-09-30
status: current
confidence_overall: emerging
issue: "#3810"
---

# Can Skills Learned in Games Transfer to Real-World Work?

> Interview-based report that a 30B model trained in the 1830 railroad game improved on the Finance-Agent benchmark only when trained as a multi-turn tool-using terminal agent (not single-turn game-move QA), supporting the claim that harness/environment design determines what transfers.

## Source Context

- **Type**: blog-post (interview write-up; Latent Space)
- **Author credibility**: Richard MacManus writes for Latent Space; the primary voice is Alex Duffy, co-founder/CEO of Good Start Labs (spun out of Every, $3.6M funding), a vendor of RL environments and game trajectory data to frontier labs. Duffy has a commercial interest in the "environment as curriculum" thesis. The article reports results but does not publish numbers.
- **Scope**: Covers the 1830 → Finance-Agent transfer experiment, Diplomacy → customer support/industrial operations, harness design, whether stronger frontier models reduce the importance of harnesses, Good Start Labs' business model, and the open question of broad transfer. No benchmark scores, sample sizes, or training details are given in the article; it points to a COS-PLAY paper and Good Start Labs' own posts.

## Extracted Claims

### Claim 1: Training design, not the game itself, determined whether 1830 training transferred to financial research
- **Evidence**: Reported 1830 experiment on a 30B model; two training designs compared. No numbers in the article.
- **Confidence**: emerging
- **Quote**: "Both training designs improved their respective in-game objectives, but only the terminal-agent design improved performance on the Finance-Agent benchmark."
- **Our assessment**: Strong qualitative signal that in-game improvement is not sufficient evidence of transfer. Single vendor result, unquantified in this article; treat as a hypothesis worth citing with that caveat.

### Claim 2: The winning design was a multi-turn terminal agent with tools; the losing one was single-turn game-state QA
- **Evidence**: Author's description of the published results.
- **Confidence**: emerging
- **Quote**: "a “multi-turn terminal agent that uses tools to explore its environment, plan a strategy, and adapt in real time.”"
- **Our assessment**: Consistent with the intuition that training in the same interaction shape (tools, exploration, iteration) as the target task is what transfers. Note the contrast with Qwen-AgentWorld (single-turn prediction transferring to multi-turn), see Cross-References.

### Claim 3: The game task was deliberately built to mirror a finance workflow
- **Evidence**: Duffy's description of the task setup.
- **Confidence**: anecdotal
- **Quote**: "we’ve set up tasks where models are going through a database to find information about how the game’s been played, putting it into an Excel file, reasoning over it, creating some functions within it, and then calculating its answer in that way."
- **Our assessment**: The "transfer" is to a structurally similar task (the author admits this in the closing section), so it demonstrates near transfer, not general skill transfer.

### Claim 4: The harness determines what the model can learn
- **Evidence**: Duffy's assertion, illustrated by modality examples (images vs. text vs. Python framing).
- **Confidence**: emerging
- **Quote**: "How you design that [the harness] totally changes what the model can learn,"
- **Our assessment**: Plausible and aligned with the 1830 result; no ablation across modalities is shown.

### Claim 5: Stronger base models make the harness matter more, not less, when the environment is the curriculum
- **Evidence**: Duffy's argument, using GPT-6 Astra's reported tendency to do less chain-of-thought as the example.
- **Confidence**: anecdotal
- **Quote**: "If you want a model to work a certain way while solving a problem, the harness is what forces it. Astra can probably do the math in its head, but you’d rather it use code so you can trust the result."
- **Our assessment**: Useful reframing: harnesses as process enforcement (verifiability) rather than capability crutch. Conditioned on the training-curriculum use case; Duffy concedes "a more capable model needs less handholding to finish the same task, certainly."

### Claim 6: Games provide verifiable rewards, making them good RL environments
- **Evidence**: Duffy's stated reasoning for founding the company; the game engine acts as the reward source.
- **Confidence**: settled (as a general RL principle)
- **Quote**: "It became really clear that reinforcement learning environments were one of the most reliable ways to teach models anything you could verify,"
- **Our assessment**: Matches the verification-gates-progress theme in the corpus.

### Claim 7: Diplomacy fine-tuning improved customer support and industrial operations benchmarks
- **Evidence**: Secondhand: article quotes Duffy's earlier Every article; not verified here.
- **Confidence**: anecdotal
- **Quote**: "fine-tuning a model on the strategy game Diplomacy improved its performance on customer support and industrial operations benchmarks."
- **Our assessment**: Second transfer instance from the same vendor; independent replication absent.

### Claim 8: Environments can use the game engine as verifier for tasks solved in unexpected ways, and an expert model can supply denser stepwise rewards
- **Evidence**: Description of product offerings.
- **Confidence**: anecdotal
- **Quote**: "We’ll also make a lot of tasks where the models are using the game engine as the verifiable source of rewards, but are solving problems in a way that you might not expect."
- **Our assessment**: Design pattern (engine-as-verifier + task variants over one simulator); no detail on reward shaping given.

### Claim 9: Frontier models diverge in behavioral "personality" even as capability rises
- **Evidence**: Diplomacy observations (o3 planned betrayal and won; Opus 4 refused to lie); Duffy says every new model is compared.
- **Confidence**: anecdotal
- **Quote**: "diverge on the personality axes: betrayal, collaboration, theory of mind, etc.”"
- **Our assessment**: Games as behavioral evals is interesting for Ch03-style evaluation; evidence is anecdotal.

### Claim 10: Evidence for transfer is real but its breadth is an open question
- **Evidence**: Duffy cites Surge AI (office-work post-training improved coding), DeepSeek R1, plus their two internal cases. The author's own conclusion is qualified.
- **Confidence**: emerging
- **Quote**: "Today’s evidence supports pretty clearly that goal-directed execution matters, and reasoning transfers,"
- **Our assessment**: Honest hedge; the author states the overall answer is "a qualified yes." We should not cite this as evidence of general game-to-work transfer.

### Claim 11: Every environment built also improves downstream tool use
- **Evidence**: Duffy assertion, no data.
- **Confidence**: anecdotal
- **Quote**: "Every environment we’ve built also improves tool use downstream.”"
- **Our assessment**: Consistent with Claim 2 but unquantified.

### Claim 12: A skill bank co-evolved by a separate agent is one route to learnable guidance (COS-PLAY)
- **Evidence**: Paper co-authored by Duffy and Marques; article summarizes only.
- **Confidence**: emerging
- **Quote**: "a learnable skill bank to guide action taking."
- **Our assessment**: Pointer to a paper worth separate mining; skill-bank agent revising skills from trajectories parallels skills/memory-consolidation patterns.

## Concrete Artifacts

```
Experiment (per article, Good Start Labs):
- Environment: 1830: The Game of Railroads and Robber Barons
- Model: 30B
- Variant A: single-turn QA — game state in, next move out
- Variant B: multi-turn terminal agent using tools to explore, plan, adapt
- Transfer test: Finance-Agent benchmark
- Result: both improved in-game; only B improved Finance-Agent
```

```
Task shape mirroring finance workflow (Duffy, quoted in article):
database lookup of game history -> Excel file -> reasoning -> functions in sheet -> calculated answer
```

## Cross-References

- **Corroborates**: `blog-latentspace-ainews-simulation-taking-over.md` Claim 10 (progress is gated by verification, here game-engine rewards) and Claim 7 (RL environments with verifiers as a training stack); `blog-latentspace-ainews-harness-drift-quantization.md` Claim 3 (encoding value into evals and environments as durable edge).
- **Contradicts**: None filed. Tension worth noting (not filed as a contradiction, as it differs in setting): `blog-latentspace-ainews-meta-harness-summer.md` Claim 8 reports single-turn environment-prediction training transferring to multi-turn agent performance, whereas Good Start Labs found single-turn QA did not transfer to Finance-Agent. Different objectives (world-model prediction vs. next-move QA), so a conditioning variable rather than a contradiction.
- **Extends**: `blog-latentspace-ainews-simulation-taking-over.md` Claim 5 (curriculum design as a model-made component) with a concrete case that environment/harness shape is the curriculum; `blog-latentspace-ainews-meta-harness-summer.md` Claim 9 (training-data design choices independently matter).
- **Novel**: The 1830 → Finance-Agent single-turn vs. terminal-agent comparison; the argument that harnesses matter more with stronger models when training; games as behavioral-divergence evals.

## Guide Impact

- **Chapter 05/06 (training, data/environments)**: Add a cited, caveated example that environment interaction shape (multi-turn tool-using agent vs single-turn QA) determined transfer, and that in-game gains are not evidence of transfer. Label as a single-vendor, unquantified result.
- **Harness chapter**: Add the framing that harnesses enforce process (use code rather than mental arithmetic) so results are trustworthy, even for stronger models (Claim 5).
- **Evaluation chapter**: Optional mention of games as measurable behavioral-divergence evals (Claim 9), anecdotal.

## Extraction Notes

- Read the full article (raw HTML via curl, text extracted); quotes copied from that text. Curly quotes are preserved as in the source. Some quotes end at a source-internal closing mark.
- Did not follow COS-PLAY, Every, Surge AI, or Good Start Labs posts; article gives no numeric results, so confidence is capped at emerging. A follow-up source on the published 1830 results would help.
- Issue triage comments described "Diplomacy improved customer support" etc.; those are confirmed in the article text.
